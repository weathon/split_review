# RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
While recent low-cost radar-camera approaches have shown promising results in
multi-modal 3D object detection, both sensors face challenges from environmen-
tal and intrinsic disturbances. Poor lighting or adverse weather conditions de-
grade camera performance, while radar suffers from noise and positional ambigu-
ity. Achieving robust radar-camera 3D object detection requires consistent perfor-
mance across varying conditions, a topic that has not yet been fully explored. In
this work, we first conduct a systematic analysis of robustness in radar-camera de-
tection on five kinds of noises and propose RobuRCDet, a robust object detection
model in bird’s eye view (BEV). Specifically, we design a 3D Gaussian Expan-
sion (3DGE) module to mitigate inaccuracies in radar points, including position,
Radar Cross-Section (RCS), and velocity. The 3DGE uses RCS and velocity priors
to generate a deformable kernel map and variance for kernel size adjustment and
value distribution. Additionally, we introduce a weather-adaptive fusion module,
which adaptively fuses radar and camera features based on camera signal confi-
dence. Extensive experiments on the popular benchmark, nuScenes, show that
our RobuRCDet achieves competitive results in regular and noisy conditions. The
source codes and trained models will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper conducts a systematic analysis of radar-camera detection robustness under five types of noise and proposes RobuRCDet, a robust object detection model in bird’s-eye view (BEV). To address radar point inaccuracies, including position, Radar Cross-Section (RCS), and velocity, this work introduces a 3D Gaussian Expansion (3DGE) module. This module uses RCS and velocity priors to create a deformable kernel map, adjusting kernel size and value distribution. Additionally, this paper proposes a weather-adaptive fusion module that dynamically merges radar and camera features based on camera signal confidence. Experiments show the effectiveness of the proposed RobuRCDet.

### Strengths
(1)The figures in this paper are well-crafted.
(2)The proposed 3D Gaussian Expanding method is both novel and effective, as demonstrated by the experiments.

### Weaknesses
1) The CMCA module seems to be a standard method, how does the degradation-aware head assess the confidence of the camera and radar features? Specifically, what mechanism does it employ to quantify the degradation level in camera images and how is this degradation score used to modulate the fusion process? It's unclear how the network learns to differentiate between minor and severe degradation, and how this affects the weighting of camera and radar features. The paper lacks detail on the specific architecture and loss functions used to train this degradation-aware head, making it difficult to assess its novelty and effectiveness.
2) Although Pepper is designed as a robust fusion method between radar and camera, its performance is not much stronger than that of RCBEVDet in tab.2, particularly regarding the NDS. The improvement in NDS seems marginal, raising questions about the practical significance of the proposed method. Furthermore, the paper does not provide a detailed analysis of the scenarios where Pepper outperforms RCBEVDet, and conversely, where it does not. This makes it difficult to understand the specific advantages and limitations of the proposed fusion approach.

### Questions
please see the weakness section

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the problem of robustness in radar-camera fusion techniques for 3D object detection. The authors point out that adverse weather conditions, poor lighting, and sensor noise often cause existing methods to fail specifically because of the "flat" fusion approach that is usually used. The paper introduces RobuRCDet to overcome the shortcomings of existing approaches by using confidence-based fusion.
Key contributions:
Analysis of common noise types affecting radar data in real-world scenarios (key-point missing, spurious points, point shifting, non-positional disturbance) and create a benchmark by simulating noise patterns for evaluating robustness.
A model with 2 key contributions: 3D Gaussian Expansion (3DGE) for filtering out noisy radar points based on the sparsity distribution. And a Confidence-guided Multimodal Cross Attention (CMCA) for dynamically and reliably fusing the radar and camera features based on the confidence in the camera signal.
Ablation studies to corroborate the effectiveness of the added contributions on noisy radar and camera signals.

### Strengths
The paper is tackling a relevant problem hindering the reliability of machine learning approaches for sensor fusion in challenging scenarios. The related work is comprehensive and detailed. The approach presented is simple yet effective and builds on top of proven concepts. Although "confidence-based fusion" is not a new concept in itself and has been used for a long time in classical fusion approaches (e.g. Kalman Filters), the approach presented by the authors seems to be effective while not overly complicated. The authors combine multiple tried and proven ideas to achieve their results.

### Weaknesses
While the idea is presented clearly, there seem to be some missing definitions of parameters used in equations that are possible to infer but could be clearer. The diagrams, although readable, they can be more detailed to reflect the equations and information in the text. One of the methods mentioned in Table 1 is not cited (StreamPETR).

In the voxelization and kernel generation approaches there are unclarities or unanswered questions:
what voxel size is used and how does it affect the quality of the detection?
if there are multiple targets in the same voxel, does that affect the computation of the 3DGE? equation 6 indicates otherwise but this does not make sense since a voxel with more targets should have more influence than a voxel with a single target.
While nuScenes radar data includes the "z" value of the radar, it is unclear how accurate that value is and in reality, most of the radars on market are 2.5D and not 3D, aka they do not have a proper way to measure the elevation (no resolution in elevation) and thus the cartesian z value. How would the results of the 3D detection change if no "z" values were used?

### Questions
In the voxelization and kernel generation approaches there are unclarities or unanswered questions:
what voxel size is used and how does it affect the quality of the detection?
if there are multiple targets in the same voxel, does that affect the computation of the 3DGE? equation 6 indicates otherwise but this does not make sense since a voxel with more targets should have more influence than a voxel with a single target.
While nuScenes radar data includes the "z" value of the radar, it is unclear how accurate that value is and in reality, most of the radars on market are 2.5D and not 3D, aka they do not have a proper way to measure the elevation (no resolution in elevation) and thus the cartesian z value. How would the results of the 3D detection change if no "z" values were used?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a BEV space object detector using camera and radar data that uses a 3D Gaussian to mitigate radar noise and adaptively fuses camera and radar features based on camera feature quality. The 3D Gaussian Edge module learns to spread the RCS and velocity values to surrounding voxels and the Confidence-Guided Multi-modal cross attention module learns to adaptively fuse radar and camera features by learning to detect degradation of the image features. Training and evaluation is done using simulated nuScenes dataset and shows improvement over CRN and RCBEVDet.

### Strengths
The main strength of the paper is that it considers different types of sensor degradation and proposes a radar data expansion and camera-radar fusion approach to mitigate those degradations.

### Weaknesses
The proposed 3DGE seems to be densifying the radar data based on the reasoning in lines 306-316. How do the other noise types, i.e., spurious points, point shifting and non-positional disturbances get mitigated? Furthermore, spurious points may get worse due to being spread across multiple voxels, and there’s no discussion on how non-positional disturbances are addressed through 3DGE. Furthermore, the ablation experiments only include keypoint noise and missing the other 3 types of radar noises as mentioned in the paper.

There’s no discussion on the training process. How does the model learn M_c from the data? Adverse data are rare and what prevents the network from always choosing image features?

All the results are based on simulated data therefore the conclusions from the results would depend a lot on the fidelity of the simulation. There isn’t much discussion on how the radar noise simulations were done. As for the image signal, the performance will be limited by [Han et al. 2022] for adverse weather. For low-light, cameras have signal dependent noise characteristics which cannot be modeled by random gamma factor.

### Questions
Line 69: What is meant by “focus on the corruption graphic characteristics instead of the natural causes of the corruption”? If the noise distribution of the corruption doesn’t match the noise characteristics of the radar then the resulting model doesn’t add much benefit in practice.

Figure 2: how were the noise parameters of the plots determined? How were the ground truth points determined in the captured data, i.e., they can already have the 4 types of radar noise.

How is the camera signal confidence reliably learned in practice with imbalance data?

The need for the learned 3D Gaussian Expanding component is unclear especially given that the set of lambda_p is small, how does the model perform without learning the sigma and simply performing deformable convolution on a 5x5x5 grid?

How well does the proposed approach work on real adverse weather and noisy data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces RobuRCDET, a novel approach to effectively fuse radar and camera features for 3D object detection. The core idea is to suppress false radar points by predicting Gaussian kernel variance. The approach demonstrates promising results on the nuScenes validation set.

### Strengths
+ The paper is well-written and easy to comprehend.
+ The core idea of suppressing false radar points by predicting Gaussian kernel variance is nice and leverages the information bottleneck principle.
+ The proposed method of weighting camera and radar streams leads to robust feature representation.
+ The approach demonstrates promising results on the nuScenes validation set.

### Weaknesses
- The idea of predicting Gaussian variance in 3DGE module like decomposition and re-combining is one of the ways to denoise radar points. Another way to denoise is using self-attention blocks [A]. How does the method work when you replace the 3DGE module by multiple self-attention blocks.

- The claim of "Extensive Experiments" in the abstract is exaggerated. It would be beneficial to quantitatively include results from the nuScenes leaderboard, particularly comparing against a strong camera baseline like SparseBEV with 640x1600 resolution.

- The experiments are conducted with super small backbones (ResNet18 and ResNet50). It would be insightful to quantitatively evaluate the approach on higher resolutions (512x1508 and 640x1600) to assess its performance.

- The paper focuses on mid-level feature fusion. A quantitative comparative analysis with end-level fusion, as employed in RADIANT [B], would provide valuable insights. To further strengthen the argument for mid-level fusion, incorporating the radar association module from RADIANT should be considered.

### Questions
Please see the weakness. I will need nuscenes leaderboard results on the 640x1600 resolution and comparison against SparseBEV 640x1600 resolution.

### Soundness
2

### Presentation
3

### Contribution
2
