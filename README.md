# MSVMD: A Multi-Scenario Visual Measurement Dataset for Transmission Line Safety Monitoring Under Complex Conditions
MSVMD is a multi-scenario visual measurement dataset for transmission line safety monitoring under complex conditions. It contains 4,000 finely annotated transmission-line images collected from fixed visible-light surveillance cameras mounted on transmission towers in Henan Province, China. The dataset covers regular scenes and challenging safety-related scenarios, including rain, snow, nighttime, low illumination, complex backgrounds, and complex illumination.

The dataset covers multiple scenarios, and several groups of representative scenarios along with their corresponding annotation information are shown in the figure.
<img width="4157" height="1909" alt="mv" src="https://github.com/user-attachments/assets/44809fc9-ad41-4044-8117-a9f75f122386" />

## Public Release

Due to practical constraints related to real transmission-line monitoring data, the full MSVMD dataset is not fully released at this stage. A representative subset of MSVMD is publicly available for research use.

- Public subset size: 500 images
- Released proportion: 12.5%
- Annotation format: binary PNG masks
- Foreground: transmission-line pixels
- Background: non-line pixels

## Annotation Format

The annotations are provided as binary PNG masks with the same spatial size as the corresponding images.

- `0`: background
- `1`: transmission-line region
 
## Dataset Split and Evaluation

We provide simple scripts for dataset splitting and segmentation evaluation.

```bash
# Generate training/validation splits
python tools/split_dataset.py --image_dir images --mask_dir masks --save_dir splits --train_ratio 0.75 --seed 42

# Evaluate segmentation results
python tools/evaluate_segmentation.py --pred_dir predictions --gt_dir masks
```

# Contact
Currently, a partial release of the MSVMD dataset is available. Researchers seeking to utilize the dataset are requested to contact author at gwang@whut.edu.cn, providing a clear statement of their research objectives and intended usage of the data.
The associated research paper is currently under review. Upon acceptance, the official paper link will be made available on this platform.


