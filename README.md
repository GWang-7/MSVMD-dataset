# 
MSVMD is a multi-scenario visual measurement dataset for transmission line safety monitoring under complex conditions. It contains 4,000 finely annotated transmission-line images collected from fixed visible-light surveillance cameras mounted on transmission towers in Henan Province, China. The dataset covers regular scenes and challenging safety-related scenarios, including rain, snow, nighttime, low illumination, complex backgrounds, and complex illumination.

# MSVMD: A Multi-Scenario Visual Measurement Dataset for Transmission Line Safety Monitoring Under Complex Conditions
Accurate and reliable monitoring of transmission lines is critical for power grid safety, especially under complex and adverse environmental conditions. Currently, visual measurement methods based on deep learning are widely used for transmission line monitoring, with performance largely dependent on dataset quality. However, most public datasets are collected under normal weather and illumination conditions, and often suffer from insufficient annotation quality, which limits their applicability to real-world safety monitoring. To address this limitation, we present MSVMD, a multi-scenario visual measurement dataset for transmission line monitoring. Specifically, a spatiotemporal random sampling strategy together with a two-stage data filtering process is adopted to better align the data distribution with real operating conditions and to increase the proportion of safety-critical scenarios. Then, a mixed annotation strategy is designed to balance annotation efficiency and accuracy, providing reliable pixel-level ground truth for visual measurement. As a result, MSVMD contains 4,000 finely annotated images acquired by fixed cameras mounted on transmission towers, covering challenging scenarios such as rain, snow, nighttime, and complex illumination. On this basis, a projected displacement measurement framework is further developed for transmission-line galloping determination, enabling conductor-wise displacement estimation from consecutive frames and rapid window-level galloping determination. Experimental results validate the dataset construction strategy and demonstrate the effectiveness of MSVMD, while experiments on a constructed galloping dataset verify the feasibility of the proposed measurement framework.


The dataset covers multiple scenarios, and several groups of representative scenarios along with their corresponding annotation information are shown in the figure.
![标注数据集](https://github.com/user-attachments/assets/2e66e21c-12a4-47c1-b873-ae9960ac4051)



# Data Access 
Currently, a partial release of the MSVMD dataset is available. Researchers seeking to utilize the dataset are requested to contact author at gwang@whut.edu.cn, providing a clear statement of their research objectives and intended usage of the data.
The associated research paper is currently under review. Upon acceptance, the official paper link will be made available on this platform.

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
 
## Dataset Split

We provide a simple script to generate training and validation splits for the released subset.

```bash
python tools/split_dataset.py --image_dir images --mask_dir masks --save_dir splits --train_ratio 0.75 --seed 42

## Evaluation

We provide an evaluation script for binary transmission-line segmentation.

```bash
python tools/evaluate_segmentation.py --pred_dir predictions --gt_dir masks

