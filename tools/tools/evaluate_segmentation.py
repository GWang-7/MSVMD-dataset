import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate binary transmission-line segmentation.")
    parser.add_argument("--pred_dir", type=str, required=True, help="Path to predicted masks.")
    parser.add_argument("--gt_dir", type=str, required=True, help="Path to ground-truth masks.")
    return parser.parse_args()


def load_binary_mask(path):
    mask = np.array(Image.open(path).convert("L"))
    return mask > 0


def compute_metrics(pred, gt):
    pred = pred.astype(bool)
    gt = gt.astype(bool)

    tp = np.logical_and(pred, gt).sum()
    fp = np.logical_and(pred, np.logical_not(gt)).sum()
    fn = np.logical_and(np.logical_not(pred), gt).sum()

    iou = tp / (tp + fp + fn + 1e-8)
    dice = 2 * tp / (2 * tp + fp + fn + 1e-8)
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)

    return iou, dice, precision, recall


def main():
    args = parse_args()

    pred_dir = Path(args.pred_dir)
    gt_dir = Path(args.gt_dir)

    pred_files = sorted([
        p for p in pred_dir.iterdir()
        if p.suffix.lower() in [".png", ".jpg", ".jpeg", ".bmp"]
    ])

    ious, dices, precisions, recalls = [], [], [], []

    for pred_path in pred_files:
        gt_path = gt_dir / f"{pred_path.stem}.png"

        if not gt_path.exists():
            print(f"Warning: ground-truth mask not found for {pred_path.name}")
            continue

        pred = load_binary_mask(pred_path)
        gt = load_binary_mask(gt_path)

        if pred.shape != gt.shape:
            raise ValueError(f"Shape mismatch: {pred_path.name}, pred={pred.shape}, gt={gt.shape}")

        iou, dice, precision, recall = compute_metrics(pred, gt)
        ious.append(iou)
        dices.append(dice)
        precisions.append(precision)
        recalls.append(recall)

    print(f"Evaluated samples: {len(ious)}")
    print(f"mIoU:      {np.mean(ious) * 100:.2f}")
    print(f"mDice:     {np.mean(dices) * 100:.2f}")
    print(f"mPrecision:{np.mean(precisions) * 100:.2f}")
    print(f"mRecall:   {np.mean(recalls) * 100:.2f}")


if __name__ == "__main__":
    main()
