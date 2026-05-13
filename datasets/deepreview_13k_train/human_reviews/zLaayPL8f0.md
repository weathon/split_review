# Decomposition Ascribed Synergistic Learning for Unified Image Restoration

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Learning to restore multiple image degradations within a single model is quite beneficial for real-world applications.
Nevertheless, existing works typically concentrate on regarding each degradation independently, while their relationship has been less exploited to ensure the synergistic learning.
To this end, we revisit the diverse degradations through the lens of singular value decomposition, with the observation that the decomposed singular vectors and singular values naturally undertake the different types of degradation information, dividing various restoration tasks into two groups, \ie, singular vector dominated and singular value dominated.
The above analysis renders a more unified perspective to ascribe the diverse degradations, compared to previous task-level independent learning.
The dedicated optimization of degraded singular vectors and singular values inherently utilizes the potential relationship among diverse restoration tasks, attributing to the Decomposition Ascribed Synergistic Learning (DASL).
Specifically, DASL comprises two effective operators, namely, Singular VEctor Operator (SVEO) and Singular VAlue Operator (SVAO), to favor the decomposed optimization, which can be lightly integrated into existing image restoration backbone.
Moreover, the congruous decomposition loss has been devised for auxiliary.
Extensive experiments on blended five image restoration tasks demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Decomposition Ascribed Synergistic Learning (DASL), a method for unified image restoration that optimizes singular vectors and values for handling multiple degradations within a single model, and integrates seamlessly into existing restoration architectures.

### Strengths
1. The paper uncovers an observation that the decomposed singular vectors and values naturally undertake the different types of degradation information, ascribing various restoration tasks into two groups, i.e., singular vector dominated and singular value dominated.
2. Two operators are developed to favor the decomposed optimization of degraded singular vectors and values for various restoration tasks.

### Weaknesses
1. There is a limited evaluation with recent AIR methods like PromptIR, GenLV, and the diffusion-based AIR techniques. Such comparisons ensure the research is aligned with the latest advancements in the field.
2. Do the observations regarding the decomposition of singular vectors and singular values hold true in terms of other degradations (low-resolution, jepg compression, etc.) or compound degradations (noise+blur, rain+haze, etc.)? Whether the proposed method is available in multiple degradation combinations?
3. How well do the decomposed singular vectors and singular values represent degradation information, and are they discriminative enough to distinguish between different degradations?
4. Some typos like ", ,"

### Questions
Please see the above Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript explored the restoration of multiple image degradations through a unified model. By employing singular value decomposition, the authors classified restoration tasks into singular vector dominated and singular value dominated categories. They introduced the Decomposition Ascribed Synergistic Learning (DASL) framework, which optimized the decomposed components to exploit relationships among various restoration tasks. The framework included two operators, Singular VEctor Operator (SVEO) and Singular VAlue Operator (SVAO), along with a supporting decomposition loss.

### Strengths
This paper addresses a significant gap in the field by proposing a unified approach to handling multiple image degradations, moving beyond the conventional practice of treating each degradation in isolation.

The use of singular value decomposition to categorize restoration tasks into singular vector dominated and singular value dominated groups provides a fresh perspective on the relationships between different types of degradations.

### Weaknesses
The manuscript raises several important questions regarding its methodology and results that require clarification.

The current description lacks clarity.

Are there specific references supporting the findings presented in Figures 1 and 2? Additionally, clarification is needed on the type of Singular Value Decomposition (SVD) employed in the analysis and whether any post-processing techniques were applied to produce the displayed images. It is noted that the deblurring case exhibits a relatively large area of damaged pixels, while the hazy and low-light image enhancement cases only show minor pixel degradation. What factors contribute to this discrepancy?

The authors conducted tests on underwater enhancement and sandstorm enhancement but did not include these results in Figure 1 & 2. Are the observations in Figure 1 commonly encountered across different datasets, including underwater and sandstorm? Moreover, Figure 2 is based on 100 images; Additional images should be tested to validate the findings. It is unclear whether only synthetic images were used to generate Figures 1 and 2, such as in the rainy case.

The assumptions regarding singular vectors capturing content information and spatial details, and singular values representing global statistical properties, are questionable. The authors should provide more supporting references for these claims. Furthermore, given that degradations are categorized into two groups, does the proposed method require prior knowledge of which group the degradation falls into before reconstruction?

A clear diagram illustrating the entire blueprint of the proposed methods should be included to demonstrate how the SVEO and SVAO are integrated into the algorithm. The current description lacks clarity, particularly the statement about substituting convolution layers with SVEO.

The experiments primarily report PSNR results; however, additional metrics should also be considered to provide a more comprehensive evaluation of the proposed method's performance.

The rationale for using the L1 norm in L_dec should be clarified.

Figure 5 does not effectively illustrate progressive component reconstruction as intended.

Typos in the abstract: 'tasks into two groups, , '

### Questions
Are there specific references supporting the findings presented in Figures 1 and 2? Additionally, clarification is needed on the type of Singular Value Decomposition (SVD) employed in the analysis and whether any post-processing techniques were applied to produce the displayed images. It is noted that the deblurring case exhibits a relatively large area of damaged pixels, while the hazy and low-light image enhancement cases only show minor pixel degradation. What factors contribute to this discrepancy?

The authors conducted tests on underwater enhancement and sandstorm enhancement but did not include these results in Figure 1 & 2. Are the observations in Figure 1 commonly encountered across different datasets, including underwater and sandstorm? Moreover, Figure 2 is based on 100 images; Additional images should be tested to validate the findings. It is unclear whether only synthetic images were used to generate Figures 1 and 2, such as in the rainy case.

The assumptions regarding singular vectors capturing content information and spatial details, and singular values representing global statistical properties, are questionable. The authors should provide more supporting references for these claims. Furthermore, given that degradations are categorized into two groups, does the proposed method require prior knowledge of which group the degradation falls into before reconstruction?

A clear diagram illustrating the entire blueprint of the proposed methods should be included to demonstrate how the SVEO and SVAO are integrated into the algorithm. The current description lacks clarity, particularly the statement about substituting convolution layers with SVEO.

The experiments primarily report PSNR results; however, additional metrics should also be considered to provide a more comprehensive evaluation of the proposed method's performance.

The rationale for using the L1 norm in L_dec should be clarified.

Figure 5 does not effectively illustrate progressive component reconstruction as intended.

Typos in the abstract: 'tasks into two groups, , '

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper mainly proposes Decomposition Ascribed Synergistic Learning (DASL) to restore multiple image degradations by SVD and FFT. Specifically, diverse degradations are ascribed into two groups, singular vector-dominated degradations and singular value-dominated degradations. The proposed DASL dedicates the decomposed optimization of them respectively, rendering a more unified perspective to inherently utilize the potential partnership among diverse restoration tasks for ascribed synergistic learning. Two effective operators SVEO and SVAO have been developed to favor the decomposed optimization. Experimental results demonstrate that DASL improves restoration quality while reducing model parameters and accelerating inference speed.

### Strengths
[S1] Lightweight networks have great application prospects at present.
﻿
[S2] DASL reduces the computations of the baseline model and improves the effect.

### Weaknesses
[W1] The paper writing is very poor, containing many typos. Many sentences, paragraphs, and sections are difficult to understand. 

[W2] The proposed method applies the SVD in the FFT space and validates its effectiveness to some extent. However, it does not clearly explain the insight and why it works. Specifically, the paper lacks a clear explanation of why optimizing the amplitude maps in the frequency domain is equivalent to, or even approximates, optimizing the singular values obtained from SVD. The connection between these two operations needs more rigorous justification.

[W3] More visualization results of DASL+baseline should be presented rather than only MPRNet. In addition, in Fig. 14-16, the superiority of the proposed method is hard to distinguish. The visual differences are subtle, and it's difficult to assess the practical impact of the proposed method based on these figures alone. More diverse examples and clearer visual comparisons are needed to support the claims.

[W4] The article presumes that the SVD and IDFT operate similarly in terms of signal formation, but does not show the Ablation Study of the restore results. This assumption is not sufficiently validated. An ablation study comparing the performance of the proposed method using SVD versus IDFT for signal decomposition is crucial to justify the choice of IDFT as an approximation for SVD.

### Questions
[Q1] As per my understanding, the orthogonal regularization loss and decomposition loss in formula (5) represent the reconstruction loss of singular vectors and singular values respectively, and different dominant factors are employed for various types of degradation. During the training process, the balanced weights are set as a fixed ratio. Will this setting negatively harm the mixed results?
﻿
[Q2] In Figure 2, which baseline method did you use? It seems that the exchange reconstruction error for dehazing is very close. Thus, this figure can't convince me of the effectiveness of the proposed idea in dehazing task.
﻿
[Q3] This work aims to use a single model to handle multiple kinds of degraded images with one degradation type. How does it perform on images that contain multi-types of degradation? What is the difference in performance between your model and a model that trains only with a single type of degradation?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The goal of this paper is to solve the image restoration task of multiple image degradation types. The paper explores the relationship between singular values and singular vectors between degraded images and clear images in different degradation types. Singular value-dominated and singular vector-dominated image restoration are ascribed. Singular vector operators and singular value operators are proposed and lightly integrated into the existing image restoration backbone. Experiments on multiple degradation types are conducted to verify the effectiveness of the method.

### Strengths
1. The paper is easy to understand and has a clear overall structure.
2. Exchange of the singular value and the singular vector analysis is performed on the image restoration tasks of different degradation types, showing the role of singular values ​​and singular vectors in image restoration.
3. The singular value operator and singular vector operator are proposed to make the existing methods lighter, with some improvement in computational complexity.

### Weaknesses
1. In Figure 2, the authors slightly show that the decomposed singular values ​​and singular vectors between different degradation types undertake different degradation information. Specifically, the exchange reconstruction error of Figure 2 (a) in the dehazing task is close to 50% for both singular value and singular vector, and the low-light and haze degradation in Figure 2 (b) are similar to other degradations such as rain and noise, while the blur and low-light in Figure 2 (c) are also very close. Therefore, I think that the authors don't explain the relationship between singular values ​​and singular vectors and degradation information well. The assumptions proposed are also untenable. The authors could consider conducting an in-depth analysis in high-dimensional space or frequency space to analyze the impact of singular values ​​and singular vectors in terms of signal-to-noise ratio, frequency changes, etc. Even ablation analysis without using singular values ​​or singular vectors can be used instead of just statistical analysis of reconstruction errors.

2. The experiments only include results on a single degradation task dataset, not on a mixed dataset. This does not meet the requirement of using a single model for a unified image restoration task. The authors could refer to the similar experimental setup in the work of Li et al. [1] to conduct experiments on mixed degradation datasets to demonstrate the effectiveness and robustness of the proposed DASL.

3. The stability improvements brought by the loss curves of the training trajectories in Figure 6 and  Figure 7 are also not clearly demonstrated for tasks such as denoise and derain, etc. The authors should include the corresponding intermediate feature map changes or any other visualization statistics that can assist in demonstrating the effectiveness of singular values ​​and singular vectors.

### Questions
Same as described in the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
