# Diff-2-in-1: Bridging Generation and Dense Perception with Diffusion Models

- Decision: Accept
- Scores: 3, 6, 8, 6, 6

## Abstract
Beyond high-fidelity image synthesis, diffusion models have recently exhibited promising results in dense visual perception tasks. However, most existing work treats diffusion models as a
standalone component for perception tasks, employing them either solely for off-the-shelf data augmentation or as mere feature extractors. In contrast to these isolated and thus sub-optimal efforts, we introduce a unified, versatile, diffusion-based framework, \methodname, that can simultaneously handle both multi-modal data generation and dense visual perception, through a unique exploitation of the \textit{diffusion-denoising process}.
Within this framework, we further enhance discriminative visual perception via multi-modal generation, by utilizing the denoising network to create multi-modal data that mirror the distribution of the original training set.
Importantly, \methodname optimizes the utilization of the created diverse and faithful data by leveraging a novel self-improving learning mechanism. Comprehensive experimental evaluations validate the effectiveness of our framework, showcasing consistent performance improvements across various discriminative backbones and high-quality multi-modal data generation characterized by both realism and usefulness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents Diff-2-in-1, a framework leveraging diffusion models for both multi-modal data generation and dense visual perception tasks. Unlike previous works that treat diffusion models as standalone components for perception or data augmentation, Diff-2-in-1 integrates generative and discriminative learning through a self-improving mechanism using EMA update. This mechanism involves two sets of parameters: one for data creation (θC) and another for data exploitation (θE). The training process iteratively enhances both generation and discriminative task performance with backpropagation and EMA update.

### Strengths
1.	Unified Framework: The paper integrates generative and discriminative processes to improve discriminative tasks using the diffusion model.
2.	Favorable performance on benchmarks: The method is evaluated on NYUD-MT and PASCAL-Context, and shows consistent performance improvements.

### Weaknesses
1.	The term “unified framework” is overstated and potentially misleading. The proposed method does not employ a single model to handle both data generation and prediction. Instead, it uses a pre-trained latent diffusion model for RGB image generation and a separate task-specific head for discriminative tasks. While there is interaction between these components during the update process, the term “unified” suggests a more cohesive integration than what is presented. From the description, it is likely to be expected that the model to perform both data generation and discriminative tasks by denoising process. Clarifying this would better align reader expectations with the actual implementation.
2.	Clarity. It is unclear whether θE and θC represent parameters of the task head alone or include latent diffusion parameters. 
3.	Limited Novelty in Core Components: While the integration of generative and discriminative learning is an interesting direction, the core underlying techniques are adaptations of existing methods. The generation component relies on the widely used latent diffusion model, while the discriminative part uses VPD, a previously proposed method. The main technical contribution lies in the self-training mechanism using EMA updates, which is a general concept that could be applied to various ML tasks. The technical contribution and the motivation behind the problem are not well connected.
4.	Incomplete literature survey.
There have been recent works [1][2][3] on tackling discriminative tasks using the denoising process. These works are closely relevant but not mentioned nor discussed. These works should be discussed.
[1] Ke, Bingxin, et al. "Repurposing diffusion-based image generators for monocular depth estimation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
[2] Liu, Xian, et al. "Hyperhuman: Hyper-realistic human generation with latent structural diffusion." arXiv preprint arXiv:2310.08579 (2023).
[3] Fu, Xiao, et al. "GeoWizard: Unleashing the Diffusion Priors for 3D Geometry Estimation from a Single Image." arXiv e-prints (2024): arXiv-2403.
5.	Unrelated works in the related work section. The related work section has two subsections. While the second subsection discusses relevant prior studies, the first subsection, titled “Pixel-level dense visual perception,” includes a list of works that are not relevant to the contributions of this paper. 
6.	Minor Performance Gain: Performance gains over existing augmentation methods such as DA-Fusion are marginal.

### Questions
Questions
It is unclear whether θE and θC represent parameters of the task head alone or include latent diffusion parameters. Is the pre-trained latent diffusion fine-tuned during self-training, or does it remain frozen?

Comments
The paper is missing recent related works. While it explores the self-training of a framework using only VPD, there are more recent studies that apply the diffusion process to discriminative prediction tasks. Extending the idea to these diffusion-based discriminative methods would be an interesting direction.

### Soundness
2

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
5

### Summary
This paper introduces Diff2in1, a method to enhance discriminative capability by generating diverse and faithful synthetic data, particularly beneficial for discriminative learning with limited training data. The authors propose a self-improving learning mechanism that leverages synthetic data. Experiments and ablation studies demonstrate the effectiveness of the proposed method.

### Strengths
1. The approach of using synthetic data pairs and integrating a self-improving mechanism is interesting and valuable for discriminative tasks using pre-trained diffusion models.
2. The method shows promise in scenarios with limited training data.
3. Comprehensive experiments and ablation studies across multiple dense prediction tasks (surface normal estimation, semantic segmentation, depth estimation) and multiple datasets demonstrate the effectiveness and versatility of the approach.

### Weaknesses
1. The overall writing lacks clarity. The paper's main focus is on improving discriminative learning using synthetic data. Claiming it as "A single, unified diffusion-based model for both generative and discriminative learning" may be not proper, as the method does not improve generative learning.

2. The method section should clearly state which parameters are trained or frozen during different stages.

3. Figure 2 needs clarification. If understood correctly, in the left subfigure, the data creation corresponds to discriminative learning, with input and output corresponding to the generative learning in the right figure.

4. It's unclear whether the proposed method works with fully fine-tuned models for depth estimation, such as DepthCrafter and GeoWizard.

5. The synthetic data generated with SDEdit may only exploit data similar to the dataset, potentially limiting its ability to generate significantly different objects. It's unclear how the method improves discriminative capability on data with large domain shifts.

### Questions
See [Weaknesses] part

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present Diff-2-in-1, a unified framework that seamlessly integrates multimodal generation with discriminative dense visual perception using diffusion models. With a self-improving mechanism, multi-modal generation can be progressively enhanced in a self-directed manner. Extensive experiments show that Diff-2-in-1 achieves superior performance consistently across various discriminative backbones and generate high-quality multi-modal data.

### Strengths
1. The authors propose a novel method with self-improving mechanism to bridge high-fidelity image synthesis and dense visual perception tasks.
2. The paper is well-written and the structure is well-organized and easy to follow.
3. The authors conduct extensive experiments and ablation studies to demonstrate the superiority of their designs, providing impressive qualitative and quantitative results.

### Weaknesses
1. The content of preliminary can be appropriately reduced, and add several visual comparisons from the appendix to the main paper.
2. It can be observed from Table.2 that the Diff-2-in-1 only improve the diffusion-based the segmentation method by 0.5, which seems to be incremental. Please explain the reason.

### Questions
1. It can be observed that Taskprompter achieve better result for Saliency in Table.4. Why does the performance of Taskprompter decrease after adding Diff-2-to-1 to Taskprompter?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a framework that unifies generative and discriminative tasks within diffusion models. The framework enables simultaneous handling of multi-modal data generation and dense visual perception, by leveraging a diffusion-denoising approach to enhance both tasks. By creating synthetic data through a self-improving mechanism, the framework aims to boost the performance of dense visual perception tasks, particularly in low-data settings. Experimental results show improvements in state-of-the-art performance across various dense vision tasks, including semantic segmentation, depth estimation, and surface normal prediction.

### Strengths
1. This paper creates a unified diffusion model for unifying discriminative and generative tasks.
2. The writing of this paper is clear and easy to understand.

### Weaknesses
1. The proposed framework is limited to dense perception tasks such as segmentation, as the outputs are generated by diffusion models. Can it achieve other types of perception tasks such as categorization, instance segmentation, object detection, or text captioning?

2. The cycle of discriminative and generative learning in this framework only improves perception tasks but not generative tasks. I expect to see more discussions or experiments on how the framework can leverage multimodal information to improve RGB image generation.

3. Image generation performance has not been studied in the paper.

4. The self-imrpoving mechanism is one of the two major contributions of this work. I didn't see ablation study on using/not using it. It requires detailed ablation study on it to further reveal its effectiveness.

5. The performance improvement on semantic semgnetation and depth estimation is not significant compared to normal prediction. Could authors try to interpret this?

### Questions
In summary, the paper has the potential to be a qualified paper for ICLR. However, there are some major concerns as disccused above. If authors can address some of them, I will consider raising my rating.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new diffusion-based framework called Diff-2-in-1, which integrates both multi-modal data generation and dense visual perception. Unlike most prior work where diffusion models are used in isolated manners (either for generating data or for perception tasks), the authors introduce a unified approach that leverages the denoising process of diffusion models to simultaneously perform both tasks.

### Strengths
1. The idea of merging both data generation and visual perception into one unified framework is interesting and novel.
2. The method is versatile enough to handle multiple tasks such as segmentation, depth estimation and surface normals estimation. demonstrating wide applicability in many downstream tasks.

### Weaknesses
1. Both the figure (Figure 2) and writing for the section of self-improving learning are bad and seem to not be well-motivated. The performance gain of self-improving learning is not good either as the scores for most metrics remain unchanged (in Table 7)).

2. There is no clear breakdown of which components of the self-improving mechanism or the diffusion-denoising process contribute most to the observed improvements. An ablation study would help pinpoint the critical aspects of the framework. For example, performing an additional experiment without using the diffusion-denoising process.

3. For depth and surface normal estimation, the authors do not compare their method against Marigold [1] and StableNormal [2], which are very powerful models for these tasks

### Questions
I have no further questions.

### Soundness
3

### Presentation
1

### Contribution
3
