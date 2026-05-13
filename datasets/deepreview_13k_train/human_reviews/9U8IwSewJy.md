# Mixture-of-Queries Transformer: Camouflaged Instance Segmentation via Queries Cooperation and Frequency Enhancement

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Due to the high similarity between camouflaged instances and the surroundings and the widespread camouflage-like scenarios, the recently proposed camouflaged instance segmentation (CIS) is a challenging and relevant task. Previous approaches achieve some progress on CIS, while many overlook camouflaged objects’ color and contour nature and then decide on each candidate instinctively. In this paper, we contribute a Mixture-of-Queries Transformer (MoQT) in an end-toend manner for CIS which is based on two key designs (a Frequency Enhancement Feature Extractor and a Mixture-of-Queries Decoder). First, the Frequency Enhancement Feature Extractor is responsible for capturing the camouflaged clues in the frequency domain. To expose camouflaged instances, the extractor enhances the effectiveness of contour, eliminates the interference color, and obtains suitable features simultaneously. Second, a Mixture-of-Queries Decoder utilizes multiple experts of queries (several queries comprise an expert) for spotting camouflaged characteristics with cooperation. These experts collaborate to generate outputs, refined hierarchically to a fine-grained level for more accurate instance masks. Coupling these two components enables MoQT to use multiple experts to integrate effective clues of camouflaged objects in both spatial and frequency domains. Extensive experimental results demonstrate our MoQT outperforms 18 state-of-the-art CIS approaches by 2.69% on COD10K and 1.93% on NC4K in average precision.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors tackle the problem of camouflaged instance segmentation (CIS). To this end, the authors proposed Mixture-of-Queries Transformer (MoQT). The experiments on COD10K and NC4K show that the MoQT outperforms other CIS baselines.

### Strengths
+ The paper is well-organized and easy to follow. 
+ The proposed work outperforms 18 CIS baselines on COD10K and NC4K. 
+ The authors did perform the ablation study to show the effectiveness of each component in MoQT.

### Weaknesses
 + There is a concern about the novelty. The authors explore frequency domain for feature extraction which is not new. The idea of using experts (several queries comprise an expert) is not new either. Specifically, the application of Fourier transforms for feature extraction, while potentially useful, has been explored in various contexts, and the paper does not sufficiently articulate how their specific approach differs fundamentally from these existing methods. The concept of using multiple 'experts' or specialized sub-networks is also not novel, as similar ideas have been used in ensemble methods and mixture-of-experts models, and the paper does not provide a clear explanation of how their implementation of experts is significantly different from prior work.
+ The number of decoder layers, L, is questionable. There is a huge gap between 4 and 12. Why did the authors choose 6? The justification for selecting 6 decoder layers is not sufficiently strong. The ablation study should include more intermediate values to better understand the performance trend. The lack of a clear rationale for this specific choice raises concerns about the robustness of the model's architecture.
+ The visualization is not clear. How about the failure cases? How about the case of no camouflaged instance? The paper lacks a thorough analysis of failure cases. It is essential to understand the limitations of the model, and the visualization should include examples where the model fails to segment camouflaged instances correctly. Furthermore, it would be beneficial to show how the model behaves in scenes where no camouflaged instances are present, as this would provide a more comprehensive understanding of the model's performance.

### Questions
+ I have question about the novelty. 
+ There is a question about the parameters such as the number of decoder layers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to explore the influence of contour and color for discovering camouflaged instances and utilizes MoE technology to localize the multiple instances of camouflaged objects. First, the Frequency Enhancement Feature Extractor is proposed to capture the camouflaged clues in the frequency domain. To expose camouflaged instances, the extractor enhances the effectiveness of contour, eliminates the interference color, and obtains suitable features simultaneously. Second, a Mixture-of-Queries Decoder utilizes multiple experts of queries for spotting camouflaged characteristics with cooperation. The proposed MoQT achieves SOTA performance and outperforms 18 camouflaged instance segmentation methods on COD 10K and NC4K datasets.

### Strengths
1. This paper attempts a new respective to explore the concealed attribute of camouflaged instances: the visual cues of camouflaged objects are concealed, but the other domain (like frequency) cues of camouflaged objects are not completely hidden, which allows deep parsing of camouflage detection and segmentation. This idea is interesting and worth emulating.
2. The ablation experiments are sufficient.
3. The presentation of the paper is easy to understand, including some visual comparisons, etc.

### Weaknesses
1. The proposed MoQT employs the Fourier transform to obtain color and contour features. But introduction of Fourier transform is similar to the previous work CamoFourier:
Unveiling Camouflage: A Learnable Fourier-based Augmentation for Camouflaged Object Detection and Instance Segmentation, arXiV, 2023
2. Compared with the vanilla query-based decoder, the MoQ decoder introduces a Mixture-of-Queries (MoQ) layer with initialized M experts. Then, the M+1 outputs of the MoQ layer are aggregated via an adaptive weight. The novelty of MoQ is limited. The improvement of the query mechanism is a novel approach, but the proposed MoQ is only a token aggregation method. Besides, each layer of the MoQ decoder introduces initialized experts, which should hurt cross-attention enhanced query tokens. That sounds unreasonable.
3. The structure of Fig. 4 is not consistent with Eq. (4). The aggregated query tokens of multiple experts are input the vanilla query-based decoder in Eq. (4). But, the Fig. 4 does not present this process. Actually, the layer of MoQ decoder is twice the one of vanilla query-based decoder.

### Questions
1. I suggest that the author clearly compares this method with existing query-based transformer methods, and explicitly states the advantages and innovations of the method proposed in this paper.
OSformer: One-stage camouflaged instance segmentation with transformers. In European conference on computer vision, 2022
Camouflaged instance segmentation via explicit de-camouflaging. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023
A unified query-based paradigm for camouflaged instance segmentation, ACM International Conference on Multimedia, 2023
2. I suggest that authors provide a more in-depth comparison with CamoFourier, highlighting any specific differences in how they utilize Fourier transforms and discussing how their approach advances beyond CamoFourier's techniques.
3. Authors should add some CIS methods from 2024 for comprehensive evulation, such as GLNet. Authors are suggested to directly compare their results with GLNet’s.
Camouflaged Instance Segmentation From Global Capture to Local Refinement, IEEE Signal Processing Letter, 2024.
4. The author should clearly articulate the number of query tokens used on each dataset and verify the impact of varied query token counts on different datasets.

In summary, the author should clearly elucidate the contributions of FEFE and MoQ to assess whether the paper meets the quality standards for acceptance at ICLR. For FEFE, simply using Fourier transform is not sufficient. For MoQ, aggregating multiple experis with query tokens and then inputing transformer decoder layers, this technology is not novel enough.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes the Mixture-of-Queries Transformer (MoQT), a new model for camouflaged instance segmentation (CIS). The main contributions include: 1) Frequency Enhancement Feature Extractor (FEFE): This module leverages frequency-domain transformations to emphasize object contours and minimize color interference, aiding in detecting camouflaged instances by focusing on contour details rather than color; 2) Mixture-of-Queries Decoder (MoQ Decoder): This component employs multiple groups of object queries in a hierarchical framework, enhancing segmentation precision by refining masks at each layer. The model was benchmarked against 18 state-of-the-art CIS models and showed improved performance on the COD10K and NC4K datasets, with gains of 2.69% and 1.93% in average precision, respectively.

### Strengths
1. The paper introduces a novel approach to camouflaged instance segmentation (CIS) with the Frequency Enhancement Feature Extractor (FEFE) and Mixture-of-Queries Decoder (MoQ Decoder). These components creatively combine frequency-domain analysis and hierarchical query collaboration, offering a unique solution to the challenge of segmenting camouflaged objects.

2. The approach is rigorously validated, outperforming 18 state-of-the-art methods on key datasets. The paper's ablation studies and parameter analyses reinforce the model’s robustness and effectiveness, showcasing thorough and high-quality experimentation.

3. The paper is well-structured, clearly explaining its methods and their significance. Visual aids, including performance tables and diagrams, enhance understanding, and the rationale for each component is presented logically.

### Weaknesses
1. Insufficient Baseline Comparisons: While the paper includes comparisons with several CIS methods, it does not fully explore benchmarks with generic instance segmentation methods that could also apply to camouflaged segmentation. Including results for generic transformers or non-CIS-specific models with adaptations for camouflage (e.g., baseline Mask DINO [1] with FEFE added) would clarify the advantage of MoQT over generalized solutions. Specifically, the paper lacks a clear comparison to established instance segmentation models with the proposed FEFE module integrated. This would help to isolate the performance gains specifically attributable to the MoQ decoder versus the FEFE module, and determine if the FEFE module is generally useful for other segmentation architectures.

2. The originality of Frequency Enhancement Feature Extractor (FEFE): The paper asserts that frequency domain-based contour enhancement is effective for CIS, but frequency domain analysis for camouflage object detection has already proposed by previous works like [2][3]. Although these works are dedicated for COD, the methodology of locate the camouflage objects is similar to CIS task. The paper does not adequately distinguish its approach from these existing methods, particularly in terms of the specific frequency components targeted and the novelty of the feature extraction process. The paper should clarify how its use of Fourier transforms and separate processing of amplitude and phase components differs from prior work using DCT and band-wise enhancements.

3. Interpretability of the MoQ Decoder: Although the multi-expert query mechanism is innovative, the paper lacks insight into how each “expert” in the MoQ Decoder contributes uniquely to segmentation refinement. The paper provides no analysis of the individual contributions of each expert group in the MoQ Decoder. It is unclear if each expert is learning distinct features or if there is redundancy in their outputs. Visual or quantitative analysis of the individual contributions of each expert group in the MoQ Decoder would help to illustrate why this design is optimal and inform future work on multi-query designs. Without this, it is difficult to assess the necessity of each expert and the overall design of the MoQ decoder.

### Questions
1. Did the authors consider adapting standard segmentation models (e.g., Mask DINO, SAM) for CIS by incorporating frequency-domain enhancements like FEFE? If so, how did MoQT compare?

2. Why did the authors choose Fourier transforms over other frequency-based methods, such as wavelet transforms, for capturing contour information?

3. Can the authors visualize or quantitative analysis of the individual contributions of each expert group in the MoQ Decoder ?

4. Did the authors consider MoQT’s applicability to other segmentation tasks where objects are not necessarily “camouflaged” in the traditional sense?

### Soundness
3

### Presentation
3

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
The paper presents a Mixture-of-Queries Transformer (MoQT) designed for camouflaged instance segmentation (CIS). It incorporates two main components: a Frequency Enhancement Feature Extractor (FEFE) and a Mixture-of-Queries Decoder. The FEFE captures camouflaged clues in the frequency domain by enhancing contours, eliminating interference colors, and extracting suitable features. The Mixture-of-Queries Decoder uses multiple experts of queries to spot camouflaged characteristics cooperatively, refining outputs hierarchically for accurate instance masks. Experimental results show that MoQT outperforms 18 state-of-the-art CIS approaches on COD10K and NC4K in average precision.

### Strengths
The approach shows significant improvement over existing methods, as demonstrated by extensive experimental results on COD10K and NC4K datasets, highlighting its practical applicability and potential impact in the field.

### Weaknesses
1. Lack of Innovation: The proposed frequency domain feature extraction method closely resembles those in "Unveiling Camouflage: A Learnable Fourier-based Augmentation for Camouflaged Object Detection and Instance Segmentation" and "Camouflaged Instance Segmentation via Explicit De-camouflaging." The Mixture-of-Queries Mechanism is also similar to the Multi-scale Unified Query Learning mentioned in "A Unified Query-based Paradigm for Camouflaged Instance Segmentation," without adequately explaining the main differences.

2. Writing and Expression Errors: There are several grammatical and expression errors in the manuscript. For example, lines 156-157 contain mistakes where "combines" should be "combine" and "camouflaged objection detection" should be "camouflaged object detection."

### Questions
1. On line 296 of the manuscript, when you mention initializing M experts E, are you referring to Positional Embeddings?

2. In line 320, it is stated that "our MoQ Decoder does not contain just one group of queries for capturing various instances but multiple groups of queries in each MoQ Layer." How are these groups designed and divided? The number of groups is not specified.

3. It is suggested to provide the code to help readers better understand the novelty of the proposed method.

### Soundness
2

### Presentation
2

### Contribution
2
