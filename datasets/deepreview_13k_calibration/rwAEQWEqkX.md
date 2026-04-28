# Contrastive Localized Language-Image Pre-Training

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 6, 6, 1

## Abstract
Contrastive Language-Image Pre-training (CLIP) has been a celebrated method for training vision encoders to generate image/text representations facilitating various applications. Recently, CLIP has been widely adopted as the vision backbone of multimodal large language models (MLLMs) to connect image inputs for language interactions. The success of CLIP as a vision-language foundation model relies on aligning web-crawled noisy text annotations at \emph{image levels}. Nevertheless, such criteria may become insufficient for downstream tasks in need of fine-grained vision representations, especially when \emph{region-level} understanding is demanding for MLLMs. In this paper, we improve the localization capability of CLIP with several advances. We propose a pre-training method called \textbf{C}ontrastive \textbf{Loc}alized Language-Image Pre-training (\textbf{\Ours}) by complementing CLIP with region-text contrastive loss and modules. We formulate a new concept, \emph{promptable embeddings}, of which the encoder produces image embeddings easy to transform into region representations given spatial hints. To support large-scale pre-training, we design a visually-enriched and spatially-localized captioning framework to effectively generate region-text pseudo-labels at scale. By scaling up to billions of annotated images, CLOC enables high-quality regional embeddings for image region recognition and retrieval tasks, and can be a drop-in replacement of CLIP to enhance MLLMs, especially on referring and grounding tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses a critical limitation of CLIP by introducing CLOC (Contrastive Localized Language-Image Pre-training), which enhances CLIP's capability to understand region-level semantics while maintaining its strong image-level performance. The key contributions include: (1) a novel concept of "promptable embeddings" that allows easy transformation of image embeddings into region representations, (2) a lightweight Prompter module that effectively extracts region features without compromising CLIP's original capabilities, and (3) a scalable pseudo-labeling pipeline (VESL) that generates high-quality region-text annotations. The approach is validated through extensive experiments across 31 evaluation tasks, showing particular effectiveness in MLLM applications.

### Strengths
1. Strong practical value:
    - Addresses a real limitation in CLIP that affects its use in MLLMs
    - Provides a drop-in replacement solution without compromising original capabilities
    - Demonstrates consistent improvements across various downstream tasks
2. Technical novelty:
    - Introduces an elegant concept of "promptable embeddings"
    - Develops a lightweight and effective Prompter module (though it reminds me of prompt encoder of SAM[^1])
    - Proposes a scalable approach to generate region-text annotations
3. Comprehensive evaluation:
    - Extensive experiments across 31 tasks
    - Thorough ablation studies
    - Strong performance improvements in MLLM applications

[^1]: Kirillov, Alexander, et al. "Segment anything." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

### Weaknesses
1. Insufficient comparison with related works:
    - Missing comparison with DenseCLIP [1] and similar region-aware CLIP variants [2, 3, 4, 5], as well as more recent methods like MaskCLIP, SILC and BRAVE.
    - While RegionCLIP [6] is mentioned, the differentiation from other similar approaches is not clearly articulated, particularly regarding the specific advantages of the proposed method over existing techniques for enhancing CLIP's localization capabilities.
    - Limited discussion of trade-offs compared to existing solutions, especially concerning computational cost and performance gains.
2. Missing implementation details:
    - The region sampling strategy (how 4 regions per image are selected) is not specified, including whether the regions are sampled randomly or based on some criteria, and if there is any consideration for the size or aspect ratio of the regions.
    - The rationale for setting λ as the ratio of images with region labels in the mini-batch is not explained, specifically why this ratio is an appropriate weighting factor for the CLOC loss.
    - The impact of batch composition (ratio of images with/without region labels) on training is not discussed, including potential biases or imbalances introduced by varying this ratio.
    - The threshold (0.9) for similar text filtering lacks justification, and it is unclear how sensitive the results are to this parameter.
    - The definition and extraction method of "leaf entities" in NER is unclear, and it is not explained how these entities are used to generate region-text annotations.
    - Computational overhead analysis of the Prompter compared to RoI pooling is missing, including a breakdown of the additional parameters and FLOPs introduced by the Prompter module.
3. Limited analysis of scalability:
    - The saturation of performance at 300M images for region tasks needs more investigation, including whether this saturation is due to the quality of the pseudo-labels or the model's capacity.
    - The impact of the threshold for similar text filtering on training time is not analyzed (in addition to (10) in table 2), and it is unclear how this parameter affects the convergence speed and computational cost.

### Questions
1. Region Sampling Strategy
    - How are the 4 regions per image selected during training?
    - Is there any consideration for overlap between regions?
    - How does the sampling strategy affect the model's performance?
2. Training Implementation
    - What is the rationale behind setting λ as the ratio of images with region labels?
    - How do you handle the batch composition in terms of images with/without region labels?
    - Have you experimented with different similar text filtering thresholds besides 0.9?
3. Scalability and Efficiency
    - Why does the performance saturate at 300M images for region tasks but continue to improve for MLLM tasks?
    - How does the computational cost of Prompter compare to traditional RoI pooling approaches?
    - What is the memory overhead of storing region embeddings compared to traditional CLIP?

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
3

### Summary
Contrastive image-text pretraining has achieved significant success in recent years; however, low-quality annotations and the limitations of contrastive learning alone remain challenges. This work aims to enhance CLIP by incorporating fine-grained annotations, enabling the model to scale to billions of data points and demonstrating substantial improvements over the CLIP baseline.

CLOC can be viewed as a practical approach to enhancing dataset quality, with a particular focus on fine-grained grounding details.

### Strengths
1. The data refinement process is scalable to billions of samples, demonstrating its practical utility in vision-language pretraining.

2. The approach is intuitive and straightforward, leading to improved grounding capabilities.

3. The architecture is easily adaptable for downstream grounding tasks, enhancing versatility.

4. This method effectively handles large-scale datasets (billions-level in this work), with comprehensive experiments conducted despite significant computational demands.

5. In addition to widely used recaption, this work also include region phrase candidates extraction and open-vocabulary detection with extracted phrases.

### Weaknesses
1. Visually-enriched and spatially-localized models, such as QWEN, rely on robust training to achieve high-quality outputs. These models contribute essential knowledge to the process, with the quality of grounding pseudo-labels also largely dependent on these off-the-shelf models.

2. Significant work has already been done to improve dataset captions, as seen in studies like *Improving Multimodal Datasets with Image Captioning* by Thao et al. (NeurIPS 2023). Integrating object grounding information into vision-language pretraining is also an established concept, exemplified by X-VLM (Zeng et al., ICML 2021). Although CLOC’s approach to grounding differs somewhat from X-VLM, these differences are minor and do not detract from the overall contribution.

### Questions
1. What explains the significant improvement that CLOC achieves over LLaVAW and MME-C? In contrast, GQA, which heavily relies on precise object grounding, shows only limited improvement.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper enhances the region-level representation in CLIP and introduces a new concept termed "promptable embeddings." The region-level representation is a critical task in this domain. The experimental results appear promising.

### Strengths
1. This paper addresses a significant challenge: enhancing the region-level representation of CLIP, which is crucial for various applications, including multi-modal large language models (MLLMs).
2. The experimental results presented in this paper demonstrate promising performance across both image-level and region-level tasks.

### Weaknesses
Several related works are not adequately addressed in the manuscript, such as 'UMG-CLIP: A Unified Multi-Granularity Vision Generalist for Open-World Understanding' (ECCV 2024). The lack of a thorough comparison with existing methods that also explore region-level representations hinders a complete understanding of the novelty and advantages of the proposed approach. Specifically, the manuscript does not clearly articulate how the proposed 'promptable embeddings' differ from or improve upon existing region-level feature extraction techniques. The absence of a detailed analysis of the computational cost and efficiency of the proposed method compared to other region-based approaches is also a concern.

### Questions
Will the collected fine-grained region-text annotations be made publicly available? This aspect is highlighted as one of the main contributions of the study.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes to combine ITC with region text prediction. The authors show that a data labelling pipeline at scale for region proposal combined with a image-text dataset leads to model outperforming CLIP baseline for MMLLM among other tasks.

### Strengths
The author's model is well engineered to take latency into context while adding additional blocks.
The data engine uses synthetic captions rather than alt-text to generate data for the box predictor which is lesser explored.
The authors show improvement in multiple tasks over CLIP.

### Weaknesses
This paper would have been strong if other works did not explore better pretraining over CLIP for open vocabulary computer vision tasks. However, that is not true anymore. This work ignores all the advancement in the field of pretraining image-text representation models.
Several works in combining SSL with ITC exist and show better localization performance e.g. MaskCLIP and SILC. Moreover, BRAVE at ECCV2024 showed that these works also improve MMLLM performance. 
Moreover, the primary idea of this work has also been explored in "LocCa: Visual Pretraining with Location-aware Captioners" recently.

While I commend the authors for doing an extensive study of their method vs CLIP, we have a different landscape today. It is not fair to claim large improvements without putting other improvements from the field in context. Moreover, while the authors improve upon CLIP, their performance metrics on imagenet or LVIS fall short compared to other works from the field. Therefore I unfortunately have to recommend a rejection for this paper.

### Questions
No questions, the work is very easy to read. I commend the authors for that.

### Soundness
3

### Presentation
3

### Contribution
1
