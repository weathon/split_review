# Contextual Self-paced Learning for Weakly Supervised Spatio-Temporal Video Grounding

- Decision: Accept
- Scores: 8, 5, 6, 3

## Abstract
In this work, we focus on Weakly Supervised Spatio-Temporal Video Grounding (WSTVG). It is a multimodal task aimed at localizing specific subjects  spatio-temporally based on textual queries without bounding box supervision. Motivated by recent advancements in multi-modal foundation models for grounding tasks, we first explore the potential of state-of-the-art object detection models for WSTVG. Despite their robust zero-shot capabilities, our adaptation reveals significant limitations, including inconsistent temporal predictions, inadequate understanding of complex queries, and challenges in adapting to difficult scenarios.
We propose CoSPaL (Contextual Self-Paced Learning), a novel approach which is designed to overcome these limitations. CoSPaL integrates three core components: (1) Tubelet Phrase Grounding (TPG), which introduces spatio-temporal prediction by linking textual queries to tubelets; (2) Contextual Referral Grounding (CRG), which improves comprehension of complex queries by extracting contextual information to refine object identification over time; and (3) Self-Paced Scene Understanding (SPS), a training paradigm that progressively increases task difficulty, enabling the model to adapt to complex scenarios by transitioning from coarse to fine-grained understanding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces CoSPaL (Contextual Self-Paced Learning), a novel approach to Weakly Supervised Spatio-Temporal Video Grounding (WSTVG), which aims to locate objects in videos based on text descriptions without requiring detailed bounding box annotations during training. CoSPaL proposes three main components to overcome limitations of existing methods: Tubelet Phrase Grounding (TPG) for improved object tracking, Contextual Referral Grounding (CRG) for better query comprehension, and Self-Paced Scene Understanding (SPS) for progressive learning of complex scenarios. Results are reported on common grounding benchmarks such as VidSTG and HC-STVG-v1/v2.

### Strengths
1. The idea is innovative and well motivated.
2. The paper is well-written and easy to follow.
3. The method achieves strong performance improvements with respect to the baselines.

### Weaknesses
I have a few major concerns regarding the proposed method:

1. Regarding the Video Encoder: Existing works such as STCAT and TubeDETR utilize a Resnet-101 backbone to encode each frame. Even recent works such as VGDINO use the Grounding-DINO frozen image encoder. With this method using I3D as a separate video encoder, it could be an unfair comparison with existing works. How does this method perform if the authors utilize the same features as produced by the Grounding-DINO backbone as the video features? To make it consistent with previous works.

2. The method uses a pretrained tracker in the pipeline. I am concerned regarding the impact of this tracker, and how the performance changes if a different tracker is used? There does not seem to be any ablations regarding this.

### Questions
Please consider the weaknesses section. Essentially, my concerns are regarding the impact of the video encoder and the impact of the choice of tracker. I wish to understand how sensitive the method is to these two components, and whether the improvements are coming from the overall proposed design or certain specific components. I will further discuss this with fellow reviewers before making a final decision on the rating.

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
Targeting the issues of inconsistent predictions in time judgment, difficulty in comprehending complex queries, and the complexity of application scenarios faced by weakly supervised Spatio-Temporal Video Grounding (STVG), this paper introduces the self-paced learning method, which has achieved certain performance improvements on two conventional datasets.

### Strengths
1. The problem addressed in this paper is of certain significance and is interesting.
2. The introduction of self-paced learning is reasonably justified.
3. Experimental results on different datasets indicate that the algorithm has achieved certain improvements.

### Weaknesses
1. The motivation of introducing self-paced learning should be illustrated more clearly. Are there other methods that can address the challenges presented in this paper? It is suggested to provide a more detailed explanation in the related work section.
2. In Section 3.2.1, the tracking algorithm in the TPG module seems to play a vital role in learning the whole module. It makes a good start with GroundingDINO in the whole model, and it would be beneficial to add an analysis of the ablation of the tracking algorithm. Specifically, given that GroundingDINO already provides bounding boxes, the role of BoTSORT appears to be primarily one of refinement. An ablation study focusing on BoTSORT itself would be more informative to demonstrate the novelty of the entire workflow.
3. Also, in section 3.2.1, the part of the Spatial Grounding Module, the formula description seems confused. It does not give key dimension information, such as in the similarity calculations: $\text{SIM}(f_{w_m},f_{\tilde{T_k}})=(\mathrm{MLP_{q}}(f_{w_{m}})^{T}\mathrm{MLP_{k}}(f_{\tilde{T_{k}}}))/\sqrt{d}$, where $f_{w_m}\in \mathbb{R}^{1\times768}$ and $f_{\tilde{T_{k}}}\in\mathbb{R}^{T\times{256}}$ obtains from the above, so the $MLP_q(f_{w_m})\in\mathbb{R}^{1\times{D}}, MLP_{k}(f_{\tilde{T_{k}}})\in\mathbb{R}^{T\times{D}}$, where $D$ is the MLP output dimension, but if it is like this, then matrix multiplication is failed. Besides, in $\mathrm{A_T}(f_{T}, f_{w_{m}})=\sum_{k=1}^{K}\operatorname{softmax}\left(f_{\tilde{T}_{k}}, f_{w_{m}}\right) \mathrm{MLP}_{v}\left(f_{\tilde{T}_{k}}\right)$, what is the mean about $f_T$? Is $\sum_{k=1}^{K}$ meant to be a matrix addition of all tubelet features? Then it will give $ A_\in\mathbb {R}^{1\times{D}}$; at this point, how to get the distribution of scores between different tubelets? This part of the equation is confusing.
4. The comparison parameters of GPU memory use and training time in Figure 5 are ambiguous because the fully supervised models compared in the figure are experimented on different resolutions. However, the paper does not list the information about the resolution of the fully supervised models compared at the time of statistics and the resolution of their own models and whether the hardware parameters (e.g., information about CPU, GPU, memory) are unified across the different models, which I think are essential settings.

### Questions
Please refer to the Weaknesses.

### Soundness
2

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
4

### Summary
This paper proposes CoSPaL (Contextual Self-Paced Learning) for Weakly Supervised Spatio-Temporal Video Grounding (WSTVG). The method introduces three key components: Tubelet Phrase Grounding (TPG), Contextual Referral Grounding (CRG), and Self-Paced Scene Understanding (SPS). CoSPaL aims to improve spatio-temporal video grounding by enhancing the model’s ability to understand complex queries and progressively adapt to more difficult scenarios. The effectiveness of CoSPaL is validated on three benchmark datasets, with significant performance improvements over baselines.

### Strengths
1.	The paper presents a method CoSPaL to address the key issues in WSTVG.
2.	The paper includes comprehensive quantitative analysis and visualization, providing empirical evidence to support the proposed method.
3.	The proposed CoSPaL model shows strong performance gains on multiple datasets, with notable improvements of 3.9% on VidSTG and 7.9% on HCSTVG-v1.

### Weaknesses
1.	The technical contribution and motivation is unclear. For example, TPG module uses cross-modal attention, contrastive learning, and feature reconstruction to facilitate interactions between words and tubelets, these techniques are common in the field. Why this particular implementation contributes to improved spatial and temporal grounding? It's not clear what specific design choices in the TPG module lead to the observed performance gains beyond standard applications of these techniques. The paper should elaborate on the novelty of the TPG module's architecture and how it differs from existing approaches that use similar components.
2.	The SPS component is not clearly described. It is unclear how sample complexity is determined within the curriculum learning framework, is the object number? But intuitively, videos with more objects, faster changes, and more interactions are more complex. The paper needs to provide a more rigorous definition of sample complexity and explain how it is quantified. It should also clarify how the curriculum is structured and how the model progresses through different levels of complexity. The current description lacks the necessary detail to understand the underlying mechanisms of the SPS component.
3.	What does “Self-Paced” mean? This concept is not clearly explained in the paper. The term 'self-paced' is used but not adequately defined within the context of the proposed method. A clear explanation of what makes the learning process 'self-paced' is needed, including how the model adapts its learning strategy based on its performance or the complexity of the input data.
4.	In Table 5, the introduction of SPS in the TPG module leads to a performance drop in vIoU@0.3 (TPG+SPS vs TPG). This raises concerns about the efficacy of SPS in certain settings. The authors should provide a deeper analysis of why this occurs. The paper should include a more detailed analysis of this performance drop, exploring potential reasons for the negative impact of SPS in this specific scenario. It would be beneficial to understand the conditions under which SPS is beneficial and when it might hinder performance.
5.	In page 10, the part of Impact on actor localization, the corresponding quantitative results for this claim are missing. The paper makes a claim about the impact on actor localization but does not provide the corresponding quantitative results in the main text. This makes it difficult to assess the validity of this claim and the overall contribution of the method.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper targets the Weakly Supervised Spatio-Temporal Video Grounding (WSTVG) task, which tries to retrieve specific objects and segment by sentence queries without relying on labeled data. The spatial and temporal grounding modules are used to mine the spatio-temporal information. Also, a contextual referral grounding module is utilized to extracts contextual information from query. Finally, a self-paced curriculum learning strategy is adopted for optimization. Some experiments are conducted.

### Strengths
Three WSTVG benchmarks are used for performance evaluation.

The compared methods are state-of-the-art. CG-STVG and VGDINO are published in 2024.

The figures and tables are clear.

Various figures are used to present the performance.

### Weaknesses
In Abstract, authors state that “we first explore the potential of state-of-the-art object detection models for WSTVG”. In fact, it is wrong since many STVG methods use object detection models, e.g., [1].

What is the difference between “self-paced scene understanding” and “self-paced curriculum learning”. In Section 3.2.3, authors use “self-paced scene understanding” as the section title, but all the contents describe the self-paced curriculum learning strategy. Besides, the strategy has been used in many works (Wang et al., 2022a; Soviany et al., 2022). Why you treat it as your third contribution and your title?

The technological novelty is not enough for ICLR. Most modules in the presented network in Figure 3 are popularly used. For example, cross attention in spatial grounding and temporal grounding.

Authors should conduct the main abalation study in the main paper.

The start and end timestamps need to be added in Fig 4.

Some grammatical errors. For example, "three benchmark WSTVG datasets" in Abstract.

### Questions
Please address the weakness.

### Soundness
1

### Presentation
2

### Contribution
2
