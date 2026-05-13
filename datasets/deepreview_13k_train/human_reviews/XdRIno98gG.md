# Self-supervised Monocular Depth Estimation Robust to Reflective Surface Leveraged by Triplet Mining

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Self-supervised monocular depth estimation (SSMDE) aims to predict the dense depth map of a monocular image, by learning depth from RGB image sequences, eliminating the need for ground-truth depth labels.
Although this approach simplifies data acquisition compared to supervised methods, it struggles with reflective surfaces, as they violate the assumptions of Lambertian reflectance, leading to inaccurate training on such surfaces.
To tackle this problem, we propose a novel training strategy for an SSMDE by leveraging triplet mining to pinpoint reflective regions at the pixel level, guided by the camera geometry between different viewpoints.
The proposed reflection-aware triplet mining loss specifically penalizes the inappropriate photometric error minimization on the localized reflective regions while preserving depth accuracy on non-reflective areas.
We also incorporate a reflection-aware knowledge distillation method that enables a student model to selectively learn the pixel-level knowledge from reflective and non-reflective regions. This results in robust depth estimation across areas.
Evaluation results on multiple datasets demonstrate that our method effectively enhances depth quality on reflective surfaces and outperforms state-of-the-art SSMDE baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a reflection-aware training method for self-supervised monocular depth estimation. The proposed method leverages the triplet mining loss to regularize the inappropriate regions for photometric loss.
Key contributions of this work includes:
- Introducing reflection-aware triplet mining loss and knowledge distillation for reflective regions.
- first end-to-end method for self-supervised monocular depth estimation in reflective regions.
- diverse experimetns on various indoor datasets.

### Strengths
S1. This is the first end-to-end method for self-supervised monocular depth estimation in reflective regions. The proposed triplet loss is very simple and can be integrated into any framework for SSMDE.

S2. Diverse Experiments: The paper shows diverse experiments with multiple datasets and cross validations.

S3.  Writing and Presentation: The paper is well-written and easy to understand.

### Weaknesses
W1. Many self-supervised monocular depth estimation methods are evaluated in outdoor scenes like KITTI. However, this paper shows their results in only indoor scenes using Scannet, 7-Scenes and Booster datasets.

W2. I could not find the proof of the authors' assumption that reflective regions have low disparities (instead of larger disparities).

### Questions
I would like to start by thanking the authors for their contribution to this field with their submission. Here are some questions:

Q1: This relates to W1. Are there any reasons for not including experiments on outdoor scenes, such as the KITTI dataset? The proposed method is demonstrated on indoor datasets, where pose prediction networks might be challenging to train due to prevalent rotational camera movements. I am curious whether this method is adaptable when a pose network is involved or if it can be applied to depth estimation tasks in outdoor scenes.

Q2: This relates to W2. I am concerned about whether it is possible to say that the predicted depth maps for reflective regions always have small disparities (instead of randomness errors). Is there any provements or previous works showing this is true?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a novel self-supervised monocular depth estimation training strategy, which uses triplet mining loss and reflection-aware knowledge distillation to pinpoint reflective regions at the pixel level, resulting in a robust depth estimation.

### Strengths
1.The proposed triplet mining loss can be integrated into a general monocular depth estimation framework, enhancing the accuracy of reflective surfaces.

2.The proposed reflection-aware knowledge distillation enhances the accuracy of reflective surfaces while preserving high-frequency details of non-reflective surfaces.

3.Experiments on multiple datasets demonstrate that the proposed method achieves state-of-the-art performance.

### Weaknesses
1.Ablation study on the proposed pixel-level reflection regions Mr are necessary to further analyze its effectiveness in reflection-aware triplet mining loss and reflection-aware knowledge distillation.

2.Will the proposed triplet mining strategy and reflection-aware knowledge distillation introduce additional computational overhead?

3.The description in lines 246-247 is confusing. The relative pose [R|t]s2r is obtained by computing the inverse of [R|t]s2r?

4. Depth completion is an extended task from depth estimation. Thus, it would be better if adding some depth completion methods [1-5] into the related work section.

### Questions
I would appreciate it If the authors can address my concerns in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper aims to address inaccurate depth estimation on the reflective surfaces in a scene. To this end, this paper proposes a training strategy for self-supervised depth estimation by leveraging triplet mining. The key idea is to penalize the inappropriate photometric error minimization on the localized reflective regions while preserving depth accuracy on non-reflective areas. In addition, this paper introduces a reflection-aware knowledge distillation method that enables a student model to selectively learn the pixel-level knowledge from reflective and non-reflective regions. Finally, the proposed framework is validated on various indoor datasets.

### Strengths
1.	This paper is well-written and the proposed method is easy to comprehend.
2.	This method is simple and general, which can be used for most self-supervised depth estimation methods.

### Weaknesses
1. Whether Eq. (8) can accurately reflect the reflective surface? Due to the ambiguity of photometric errors, the magnitude of photometric errors is not even a measure of the accuracy of depth [1], let alone reflective surfaces .
2. The overall performance is very marginal. From the results on the test set in Table 4, we can find that, like most end-to-end self-supervised training solutions, all comparison methods have limited improvement or even worse after using the idea proposed by the author. 
3. Experimental verification is inadequate. The selected baselines, Monodepth2(2019), HRDepth(2021), MonoViT(2020) are the early works, not the SOTA framework. I am concerned about the effectiveness of the triplet mining loss when incorporated into recent works. Moreover, there is a lack of comparison on common depth estimation datasets, such as KITTI, NYUv2, etc., where reflective surfaces also exist.

### Questions
1.	Verify effectiveness on some recent SOTA frameworks, such as [1,2,3]
2.	Training and validation on common self-supervised depth estimation datasets like KITTI, NYUv2.
3.	See weaknesses for other issues.

[1] RA-Depth: Resolution Adaptive Self-Supervised Monocular Depth Estimation.
[2] GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes.
[3] Self-supervised Monocular Depth Estimation with Large Kernel Attention.

### Soundness
2

### Presentation
3

### Contribution
2
