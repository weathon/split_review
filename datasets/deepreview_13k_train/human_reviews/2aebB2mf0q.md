# SemiAugIR: Semi-supervised Infrared Small Target Detection via Thermodynamics-Inspired Data Augmentation

- Decision: Reject
- Scores: 3, 5, 1

## Abstract
Convolutional neural networks have shown promising results in single-frame infrared small target detection (SIRST) through supervised learning. Nevertheless, this approach requires a substantial number of accurate manual annotations on a per-pixel basis, incurring significant labor costs. To mitigate this, we pioneer the integration of semi-supervised learning into SIRST by exploiting the consistency of paired training samples obtained from data augmentation. Unlike prevalent data augmentation techniques that often rely on standard image processing pipelines designed for visible light natural images, we introduce a novel Thermodynamics-inspired data augmentation technique tailored for infrared images. It enhances infrared images by simulating energy distribution using the thermodynamic radiation pattern of infrared imaging and employing unlabeled images as references. Additionally, to replicate spatial distortions caused by variations in angle and distance during infrared imaging, we design a non-uniform mapping in positional space. This introduces non-uniform offsets in chromaticity and position, inducing desired changes in chromaticity and target configuration. This approach substantially diversifies the training samples, enabling the network to extract more robust features. We also devise an adaptive exponentially weighted loss function to address the challenge of training collapse due to imbalanced and inaccurately labeled samples. Integrating them together, we present SemiAugIR, which delivers promising results on two widely used benchmarks, e.g., with only 1/8 of the labeled samples, it achieves over 94\% performance of the state-of-the-art fully supervised learning method. The source code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a data augmentation technique, that was claimed to be inspired from thermodynamic properties, for detecting small objects in infrared (IR) imagery. The paper also proposes a semi-supervised training strategy and a loss function for IR detection. The method was tested on publicly available datasets for this task.

### Strengths
I can see the benefits of data augmentations tricks and semi-supervised approach for IR detection where data is scarce and objects of interest have higher degree of variation in appearance.

### Weaknesses
1. Scope: Target detection in IR images has a very limited scope, considering the ICLR audience. None of the methods presented seems to be beneficial for general vision/machine learning methods and therefore would not draw enough attention from the participants.

2. Technical novelty/soundness:

2a. Data augmentation: the core idea seems to be adding a random value drawn from a sine curve to the pixel value. I could not connect how this strategy is deduced from thermodynamic modeling (of temperature field). In addition, were there any experiments performed to check if random numbers from a normal distribution would lead to an inferior augmentation? Why the sine function is essential here?
It looks like non-uniform chromaticity augmentation is described within Section 3.2 for non-uniform position augmentation. From Table 2, it looks like they are different. If so, they should be described clearly highlighting the distinction between them.

2b. Adaptive loss  function: Section 3.3 text claims the loss function is designed to handle the positive-negative imbalance. Idont understand how loss function in Eqn 3 is addressing this imbalance. The probability p_i seems to be agnostic to label of the pixel.
Does the x in Eqn 2 denote location? If so, I dont understand why pixel location should be part of a loss function.

2c. Semi-supervised learning: There seems to be a rather complex loss function proposed in Eqn 7 to incorporate the unlabeled examples. The text does not explain the rational/theory/intuition as to why this loss function is appropriate for this problem (or any semi-supervised learning in general). Unless we understand what the loss function is doing, it is difficult to judge its merit.

3. Evaluation: The measures for evaluation needs to be explained and supported by referring to past studies that also used it. Since the measures are not the conventional ones, this is essential for the paper to clarify. Just an example, readers from natural image object detection will be confused why IoU is used for accuracy -- it is typically used to match the predictions with GT to compute mAP.

### Questions
..

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel semi-learning approach, image augmentation method and loss function for Infrared small target detection. These methods decline the training samples and conquer the extreme imbalance between the target and the background. Consequence, the exist networks achieve the promising performance.

### Strengths
The semi-supervised approach for SIRST is pioneering. The augmentation method is novel, from the perspective of thermal radiation and model the IR image augmentation by the thermodynamic system. They also devise a loss function for SIRST which conquer the imbalance issue existing pervious work, leading to better performance.

### Weaknesses
The methodology section of augmentation part is unclear. The description of the non-uniform chromaticity augmentation lacks sufficient detail, making it difficult to reproduce. Specifically, the process of fitting a cubic function to the chromaticity offsets is not well-defined. It's unclear how the five sampled pixels are used to determine the coefficients of the cubic function, and how this fitting process ensures a smooth and continuous chromaticity variation across the image. The overview figure is informal and ambigous. The figure does not clearly illustrate the overall pipeline of the proposed method, making it hard to grasp the relationships between different components. The roles of the semi-supervised learning, augmentation, and the custom loss function are not clearly depicted in the figure. The equation(2) and (3) might be incorrect. Equation (2) lacks clarity in how the 1D mapping is extended to a 2D mapping, and the interpolation process is not clearly defined. The parameters 'T' and 'a' are mentioned, but their specific values and how they are chosen are not explained. Equation (3) only presents the loss function for positive samples, which is incomplete. The mechanism of how the thresholds η_h and η_l are used to select positive and negative samples is not clearly explained, and the specific values of these thresholds are not justified.

### Questions
The equation(2) and (3) might be incorrect.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the challenge of single-frame infrared small target detection (SIRST) through a semi-supervised approach names SemiAugIR, marking the pioneering instance of semi-supervised method in this domain. The author introduces a novel thermodynamics-inspired, non-uniform data augmentation technique aimed at emulating the chromaticity and positional alterations in infrared imagery caused by spatial distortions. This plug-and-play augmentation significantly amplifies the diversity of training samples, thereby enhancing the network's robustness. Additionally, the author presents an adaptive exponential loss function to effectively manage the pronounced class imbalance between targets and backgrounds. The experimental results substantiate the efficiency of the proposed method.

### Strengths
1. The paper is clearly written and well organized.
2. This is the first work to apply a semi-supervised method to the IRSTD task.
3. The proposed SemiAugIR can achieve over 94% performance of the SOTA fully-supervised method, while utilizing only 1/8 of the labeled samples.
4. The proposed plug-and-play non-uniform data augmentation method is well sounded and rounded, exhibits a high degree of robustness and adaptability. Its applicability extends across various infrared tasks, thereby making a valuable contribution to the advancement of infrared research.

### Weaknesses
1. Non-uniform chromaticity enhancement, as one of the pivotal contributions in this paper, necessitates a more comprehensive exposition. In addition to employing the translation of five key points for data generation, the author has harnessed specific techniques and threshold settings to ensure that the chromaticity enhancement results align with the intended expectations. These techniques warrant an in-depth elucidation, specifically detailing how the five points are selected and how their corresponding luminance values are determined to avoid clustering or drastic changes in the generated images. The explanation should include the mathematical formulations or algorithms used to generate these points and their luminance values.

2. In Section 3.4, the author conducts an analysis of the proposed Non-uniform Chromaticity Enhancement (NUC) and Non-uniform Position Enhancement (NUP), categorizing NUC as robust enhancement and NUP as mild enhancement. Is this distinction related to the concepts of strong and weak augmentation in semi-supervised learning? Furthermore, it is advisable to provide the theoretical basis for the demarcation of strong and weak augmentation to substantiate the rationale for this division. The paper should clarify the specific criteria that determine whether an augmentation is considered strong or weak, and how these criteria relate to the observed performance differences between NUC and NUP.

3. The author introduces the AEWLoss as a means to address class imbalance issues; however, the paper only expounds on its treatment of positive samples. To enhance readability and the comprehensiveness of the article, please supplement the elucidation of the treatment for negative samples along with the corresponding formulas. The explanation should include the specific threshold used for negative samples, how the loss is calculated for these samples, and how the overall loss function combines the contributions from both positive and negative samples.

4. Table 2 clearly demonstrates the effectiveness of the non-uniform data augmentation method proposed in this paper. However, the author has not expounded on the foundational data augmentation methods used for comparison. It would be beneficial to include a brief description of the baseline data augmentation methods, specifying the types of transformations used (e.g., geometric, photometric), their parameters, and how they are applied to the input images. This would provide a clearer understanding of the performance gains achieved by the proposed method.

5. Is there any inconsistency in the magnification scale in the visual comparison figures? A meticulous examination is recommended to provide more accurate and intuitive visual contrast, ensuring that the scale and alignment of the images are consistent across all comparisons.

### Questions
1. We expect the authors to included more data augmentation methods for comparison.
2. It is advisable to provide the theoretical basis for the demarcation of strong and weak augmentation to substantiate the rationale for this division.
3. To enhance readability and the comprehensiveness of the article, please supplement the elucidation of the treatment for negative samples along with the corresponding formulas.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
