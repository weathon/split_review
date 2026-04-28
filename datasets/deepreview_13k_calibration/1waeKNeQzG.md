# Style-Coherent Multi-Modality Image Fusion

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Multi-modality image fusion (MMIF) integrates heterogeneous images from diverse sensors. However, existing MMIF methods often overlook significant style discrepancies, such as saturation and resolution differences between modalities, resulting in overly smooth features in certain modalities. This tendency causes models to misjudge and disregard potentially crucial content. To address this issue, this paper proposes a novel style-coherent multi-modality fusion model that adeptly merges heterogeneous styled features from various modalities. Specifically, the proposed style-normalized fusion module progressively supplements the complete content structure by merging style-normalized features during cross-modal feature extraction. Meanwhile, a style-alignment fusion module is developed to align different feature representations across modalities, ensuring consistency. Additionally, to better preserve information and emphasize critical patterns during fusion, an adaptive reconstruction loss is applied to multi-modal images transformed into a unified image domain, enforcing mapping to a consistent modality representation. Extensive experiments validate that our method outperforms existing approaches on multiple MMIF tasks and exhibits greater potential to facilitate downstream applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel style-coherent multi-modality fusion model, based on frequency analysis, which creatively decouples the style and content of modality for image fusion. This work argues that styles represent modality-specific differences in texture, saturation, and resolution, so the SNF module adaptively performs style preservation and enhancement during the fusion process, and SAF aligns cross-modal fused features to a designated modality, ensuring stylistic consistency. In addition, distinguishing from the traditional methods that directly supervise with source data, this work employs an adaptive reconstruction loss function.

### Strengths
1.The decoupling of style and content based on frequency domain analysis is creatively applied to image fusion, and the stylistic features of the source image are preserved and enhanced considering the characteristics of image fusion.

2. Adaptive reconstruction loss with good generalization is proposed.

### Weaknesses
1. This method has a preference for one modality in the fusion process, but how to choose the preference for two modalities whose dominance is not clear?

2. Poor interpretability of SAF modules and Losses.

### Questions
1. What’s advantageous of using information entropy-based clipping to constrain α?

2. What is the rationale for designing the fusion form in equation 8?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to Multi-Modality Image Fusion (MMIF) that addresses the issue of style discrepancies (e.g., saturation, resolution) in existing methods, which can obscure important features. The proposed model includes a style-normalized fusion module for more effective feature merging and a style-alignment fusion module to ensure consistency across modalities. An adaptive reconstruction loss enhances information preservation during the fusion process. Experimental results show that this method outperforms existing approaches, indicating strong potential for various image processing applications.

### Strengths
1.The style-coherent approach is applied to multimodal fusion field and valid to be effective.

2.The paper is well-written and easy to follow.

### Weaknesses
While the adaptive reconstruction loss is a key part of the proposed approach, the paper provides limited analysis on its impact compared to other loss functions. Further ablation studies focusing specifically on this component could strengthen the claims.

### Questions
See "Weaknesses"

### Soundness
3

### Presentation
3

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
This paper presents the Style-coherent Content Fusion Model (SCFNet) for Multi-Modality Image Fusion (MMIF), addressing the challenges posed by significant style discrepancies between images from different sensors. The proposed model utilizes a dual-branch encoder architecture, incorporating a Fourier Prior Embedded (FPE) block, a Style-Normalized Fusion (SNF) module, and a Style-Alignment Fusion (SAF) module to enhance content representation and align features across modalities. An adaptive reconstruction loss function is introduced to improve content supervision and detail retention during fusion.

### Strengths
1. This paper aligns heterogeneous modal features to a shared and unified fusion space instead of directly fusing them, which is reasonable to reduce the differences between modalities.
2. The performance of this paper seems better compared to some related SOTA works.

### Weaknesses
1. The core of this paper is to align heterogeneous modal features to a shared latent fusion space to reduce inter-modal differences, which is reflected in Equation 8. However, there is a lack of theoretical analysis and further experimental validation regarding the rationale behind the design of the modal alignment method and its varying impacts. In particular, it needs to be analyzed through experiments whether aligning infrared features to the visible light domain will lead to the loss of certain infrared detail information, requiring an examination of the information retention during the alignment process.
2. Currently, there is a substantial amount of research focusing on both modal consistency and modal heterogeneity, such as CDDFuse [1], which employs fusion methods to address modal differences. Earlier, DRF [2] utilized a style transfer approach by separating scene and attribute representations for image fusion. The paper lacks a thorough comparative analysis of this work with existing similar studies and do not provide enough experimental comparisons with other similar methods.
3. As to the method, this paper mainly combines and improves existing approaches in the design of key components. For example, the design of the FPE and SNF modules draws on previous works, which, while beneficial for the research, offers limited contributions in terms of innovation.
4. This paper proposes adaptive reconstruction loss as one of the innovations, with the Equations 9-11, but the rationale and effectiveness lack explanation and validation. First, how should the hyperparameter $\beta$ in Equation 9 be set, as it is very important. Second, in Equation 11, why use $\max(R(V), R(I))$ — is $\max$ the optimal choice? 
5. In the experiment section, the training set used by the authors follows the settings from [1] and [3]. In Table 2, the results of the CDD method on the TNO Dataset are consistent with [1], so the results of the same comparison methods, TarD and DeF, on the TNO Dataset should also match those in [1]. Why is there a discrepancy here?

### Questions
1. Please provide further ablation experiments on Equation 8, such as thoroughly analyzing the impact of different alignment strategies on the preservation of modal information and fusion effectiveness. Additionally, the paper should use visualization or quantitative methods to discuss and analyze the feature representation capability of the potential fusion space after alignment, as this is a core innovation of the study.
2. Related works need to be considered. I suggest that the authors include a more in-depth analysis of how their method compares to existing approaches in the introduction and related work sections. Additionally, since the paper extracts modal heterogeneity based on a decomposition approach, it is important to conduct experimental comparisons with previous related works. I suggest that the authors begin the discussion by referencing some earlier multimodal fusion papers based on decomposition approaches, such as DRF [2], DIDFuse [4], and LRRNet [5].
3. Please provide a sensitivity analysis experiment on the impact of different $\beta$ values on the fusion results. Additionally, an ablation experiment on the max operation in Equation 11 should also be conducted.
4. Please clarify the exact experimental settings used for comparison in the fifth Weakness and illustrate any differences from the settings used in CDDFuse [1].

[4] "DIDFuse: Deep image decomposition for infrared and visible image fusion," Proceedings of the International Joint Conference on Artificial Intelligence, 2020.

[5] "LRRNet: A novel representation learning guided fusion network for infrared and visible images." IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors study the problem of fusing images from multiple modalities for various downstream tasks. To this end, the authors propose a deep network to handle the discrepancies between different modalities. In this network, the authors first split the amplitude and the phase in the frequency domain, leveraging the observation that style (modality-specific details) are preserved in the amplitude where other details (content) are represented in the phase component. The network first style-normalizes features from both modalities and then uses a learnable alignment to obtain a unified representation in the visible domain.

The results on several benchmarks suggest significant improvements over the state of the art.

### Strengths
+ Multi-modal image fusion is a fundamental step in many applications.
+ The proposed approach of separating style and content is sound and promising.
+ The results are convincing.

### Weaknesses
1. I sense that the authors specifically avoided the use of the term disentanglement. In the disentanglement literature, people did introduce different methods for disentangling content and style for various applications. I believe positioning the paper with that literature would have been valuable. A quick Google search reveals some studies using disentanglement for some multimodal tasks, though with non-visual modalities.

2. Figure 1: I am not convinced with the visual results provided. The only difference I see is that the proposed method produces slightly sharper reconstructions. This does not necessarily entail that the style discrepancy is a major issue. The example in Figure 7 is more convincing.

3. Many crucial details are left unclear.

3.1. Figure 2: It is not clear how Merging is different from Summation or Concatenation. The figure/caption should state what FPE stands for.

3.2. "the twin encoder branches share the same structure and parameters." => This should be justified a bit.

3.3. "the degree of style modification is gradually adjusted by introducing learnable parameters" => How do we ensure that this is gradual if the parameters are learnable.

3.4. Eq 7: Not clear why pooling is required here or why there is a need for a spatial squeeze operation. Moreover, it is not justified why maxpool has to be combined with avgpool.

3.5. Eq 8: What's being performed here is not explained properly.

3.6. Entropy-aware alpha: Not clear why providing bounds on a variable enforces information entropy.

3.7. Eq 11: This overall loss formulation should have been explained in more detail. There are several unclear bits. Why do we use Max(R(V), R(I)) for similarity loss? Why is there no (f(V, I)-I) or (f(I, I)-I) term in the equation?

4. The paper should provide analysis on alpha and the parameters in Eqs 5 and 6.

Minor comments:
- "Fourier Prior Embedded" => "Fourier Prior Embedding".
- "we perform a content replacement" => "we replace content".
- Eq 9: I suppose it is better to use X instead of I.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
