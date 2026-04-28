# Diffusion Models for Multi-Task Generative Modeling

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Diffusion-based generative modeling has been achieving state-of-the-art results on various generation tasks. Most diffusion models, however, are limited to a single-generation modeling. Can we generalize diffusion models with the ability of multi-modal generative training for more generalizable modeling? In this paper, we propose a principled way to define a diffusion model by constructing a unified multi-modal diffusion model in a common {\em diffusion space}. We define the forward diffusion process to be driven by an information aggregation from multiple types of task-data, {\it e.g.}, images for a generation task and labels for a classification task. In the reverse process, we enforce information sharing by parameterizing a shared backbone denoising network with additional modality-specific decoder heads. Such a structure can simultaneously learn to generate different types of multi-modal data with a multi-task loss, which is derived from a new multi-modal variational lower bound that generalizes the standard diffusion model. %Our framework is general and flexible for learning from various tasks, which also explains existing methods such as classifier and classifier-free guidance from a new perspective. 
  We propose several multi-modal generation settings to verify our framework, including image transition, masked-image training, joint image-label and joint image-representation generative modeling. Extensive experimental results on ImageNet indicate the effectiveness of our framework for various multi-modal generative modeling, which we believe is an important research direction worthy of more future explorations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel approach to generative modeling by extending diffusion-based models to a multi-task learning framework. The proposed Multi-Task Diffusion Model (MT-Diffusion) is capable of generating multi-type data (e.g., images and their corresponding labels) within a single unified model. It integrates multi-task learning losses into the diffusion process, supported by a theoretical foundation. The authors propose and experiment with several multi-task generative settings, including image transition, masked-image training, joint image-label, and joint image-representation generation, demonstrating the framework's versatility and effectiveness on the ImageNet dataset. MT-Diffusion handles multiple data types through a shared diffusion space, with a forward process aggregating multi-task data and a reverse process using task-specific decoder heads to reconstruct data for different tasks. This approach results in a novel multi-task variational lower bound that generalizes the standard diffusion model, achieving simultaneous multi-task generation without compromising individual task performance.

### Strengths
- The paper provides a sound theoretical explanation for the utility of a multi-task loss using the Evidence Lower Bound (ELBO).
- The idea of enabling multi-task learning for inputs of various modalities through a shared latent space is innovative.
- Considering the connection to guided diffusion models is a thoughtful approach that takes into account the expansiveness of the research.

### Weaknesses
 - The paper does not specify the extent of increased training costs resulting from the proposed methodology.
- While significant performance improvements are shown across various metrics, including FID, the analysis lacks control of variables to confirm that these improvements truly stem from a multi-task setting. Following the previous point, it is my view that the proposed methodology likely entails considerably higher training costs and an increased number of data samples seen by the model compared to baseline learning. Therefore, it is necessary to deeply analyze whether the performance improvement is due to positive transfer resulting from multi-task learning, or merely an effect akin to data augmentation from masked samples. The absence of such analysis has influenced my evaluation towards rejection.
- (Minor point) There is prior (possibly concurrent) work proposing a multimodal, multi-task diffusion process through a Versatile Diffusion[1] multi-flow diffusion process.
- (Minor point) The caption of Table 2 does not provide sufficient information, making it difficult for the reader to interpret the experimental results.

### Questions
- How do you think the proposed off-the-shelf guidance method would integrate with previous research focused on efficient training of diffusion models, such as P2-Weighting[2], Min-SNR[3], ANT[4], and Task Routing[5]? Particularly, Min-SNR[3], ANT[4], and Task Routing[5] view the methodology of diffusion models as naturally creating a multi-task situation through various time steps, each requiring different levels of denoising. Considering this study aims to extend multi-task learning by increasing the input modality for denoising, there seems to be an overlap. I would be interested to hear your insights on this matter.


[2]: Choi, Jooyoung, et al. "Perception prioritized training of diffusion models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[3]: Hang, Tiankai, et al. "Efficient diffusion training via min-snr weighting strategy." arXiv preprint arXiv:2303.09556 (2023).

[4]: Go, Hyojun, et al. "Addressing Negative Transfer in Diffusion Models." arXiv preprint arXiv:2306.00354 (2023).

[5]: Park, Byeongjun, et al. "Denoising Task Routing for Diffusion Models." arXiv preprint arXiv:2310.07138 (2023).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work discusses the potential of diffusion-based models in generative modeling. While current diffusion models excel in single-generation modeling, the paper explores the possibility of extending them for multi-task generative training. The authors introduce a unified multi-task diffusion model, MT-Diffusion, that operates in a shared diffusion space. This model aggregates information from multiple types of task-data and employs a shared backbone denoising network with task-specific decoder heads. The paper presents several multi-task generation settings, such as image transition, masked-image training, joint image-label, and joint image-representation generative modeling. Experimental results on ImageNet demonstrate the model's effectiveness in multi-task generative modeling.

### Strengths
- The paper introduces MT-Diffusion, a novel approach to multi-task generative modeling using diffusion models.
- The proposed model effectively aggregates information from different task-data types, enhancing its versatility.
- Extensive experiments on ImageNet validate the model's effectiveness and potential in various multi-task generative modeling scenarios.

### Weaknesses
 - Experiments are done on low resolution and small datasets, undermining its effectiveness. 
- The paper is lack of model details for each task

### Questions
- Can you explain the model structure for each task and result? Especially results in Fig 4 and Fig 5.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends the diffusion process in a multi-task learning, with a shared diffusion space for all task data. The paper verifies its formulation in multiple variations of a two-task setting (though it should be relatively straightforward to generalise into many tasks), showing improved performance over standard single task learning baselines. The paper also lists several accompanied architecture designs for the proposed multi-task diffusion formulation, based on different choices of data domains.

### Strengths
Disclaimer: I am probably not the right person to review this paper. I have background in multi-task learning but have limited experience in diffusion models. The paper seems to more focus on diffusion models and have limited context in multi-task learning.

-	The problem formulation is clean and straightforward. I have no problem understanding its derivation of ELBO and loss functions.
-	The presented architectures consider multiple choices of data types.

### Weaknesses
I will present my concerns and weaknesses here fully based on my experience in multi-task learning.

1.	The related work and experiments are all around diffusion models with very trivial baselines and simple experiments. I understand the author shape this paper as the one of the first to explore diffusion in a multi-task learning setting. But at the same time, I saw some other papers also using the multi-task learning technique in diffusion to enforce geometric constrains, particularly in the 3d shape synthesis.  For example, Wonder3D (https://www.xxlong.site/Wonder3D/) and DreamCraft3D (https://mrtornado24.github.io/DreamCraft3D/) are two examples applying diffusion on both RGB and normal maps to improve multi-view/geometric consistency. I am aware both papers were released very recently and seem to be submitted to ICLR as well, I am just wondering how the proposed paper differentiates itself from the straightforward implementation of using multi-task learning in diffusion like bering used in these two papers, and from which both were based on the same assumption of using shared diffusion space as well?
2.	As such, I am not exactly sure how to comment and understand the performance of the proposed formulation, since the experiment setting is simple and only compare with simple single task baseline. For example, it might be more intriguing to see i) the performance / formulation without having a shared diffusion space, ii) how to compare with multi-task predictive models without any diffusion (e.g. MTAN, Adasahre, Cross-Stitch, PadNet, as multi-task learning in computer vision is an active research area.), iii) is task conflict issue in multi-task learning alleviated? What are the other benefits other than improved performance?

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, four different scenarios for multi-task learning are presented to enhance the performance of image generation and classification. The authors emphasize two specific settings, namely masked-image training and joint image-label generation. Through experiments conducted on ImageNet, the paper successfully demonstrates the viability of the suggested multi-task frameworks.

### Strengths
- Multi-task learning in generation, the subject of investigation in this study, is a captivating and relatively unexplored area of research.

- The methods proposed in this study exhibit simplicity and effectiveness when applied to the ImageNet-64 baseline.

### Weaknesses
 - The explanation of the implementation details (2.2.4) regarding the encoders and decoders can be perplexing, particularly in terms of how the classification label is encoded and how it is "aggregated" with other tensors.

- The theoretical portion of the paper does not provide a clear and comprehensive explanation of the proposed multi-task models, as the focus of the paper is primarily empirical. It would be beneficial to have a more detailed architectural explanation of the models designed for various multi-task settings. If space constraints are a concern, the theoretical portion can be entirely moved to the appendix.

- While the proposed method demonstrates significant improvements on the ImageNet-64 benchmark, it lacks experiments on more widely used and challenging benchmarks, as well as comparisons with newer generation models. Additionally, some auxiliary experiments in the Appendix utilize stable diffusion, which is now commonly employed as a baseline, while the primary experiments do not present any relevant results. The absence of these experiments makes it challenging to provide sufficient justification for the superiority of the proposed complex multi-task training pipeline.

### Questions
- Could you please elaborate on the specific encoders employed for each task and the type of data they operate on? It would be helpful to understand the label space for each task, particularly regarding how a one-hot classification vector is encoded in the latent space.

- It is unclear from my understanding what the single-task learning model for ImageNet classification, depicted in Figure 6, entails. Further clarification would be appreciated.

- To ensure the readiness of the paper for publication, it is crucial to address the concerns mentioned in the Weakness section. These issues should be at least partially resolved. Thank you for your attention to these matters.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
