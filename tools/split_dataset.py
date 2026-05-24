import argparse
import os
import random
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Split MSVMD released subset.")
    parser.add_argument("--image_dir", type=str, required=True, help="Path to image folder.")
    parser.add_argument("--mask_dir", type=str, required=True, help="Path to mask folder.")
    parser.add_argument("--save_dir", type=str, default="splits", help="Path to save split files.")
    parser.add_argument("--train_ratio", type=float, default=0.75, help="Training set ratio.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    return parser.parse_args()


def main():
    args = parse_args()

    image_dir = Path(args.image_dir)
    mask_dir = Path(args.mask_dir)
    save_dir = Path(args.save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    image_files = sorted([
        p for p in image_dir.iterdir()
        if p.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp"]
    ])

    valid_names = []
    for img_path in image_files:
        mask_path = mask_dir / f"{img_path.stem}.png"
        if mask_path.exists():
            valid_names.append(img_path.stem)

    random.seed(args.seed)
    random.shuffle(valid_names)

    train_num = int(len(valid_names) * args.train_ratio)
    train_names = valid_names[:train_num]
    val_names = valid_names[train_num:]

    with open(save_dir / "train.txt", "w", encoding="utf-8") as f:
        for name in train_names:
            f.write(name + "\n")

    with open(save_dir / "val.txt", "w", encoding="utf-8") as f:
        for name in val_names:
            f.write(name + "\n")

    print(f"Total samples: {len(valid_names)}")
    print(f"Training samples: {len(train_names)}")
    print(f"Validation samples: {len(val_names)}")
    print(f"Split files saved to: {save_dir}")


if __name__ == "__main__":
    main()
