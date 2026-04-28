# Semantically Consistent Video Inpainting with Conditional Diffusion Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Current state-of-the-art methods for video inpainting typically rely on optical flow or attention-based approaches to inpaint masked regions by propagating visual information across frames. While such approaches have led to significant progress on standard benchmarks, they struggle with tasks that require the synthesis of novel content that is not present in other frames. In this paper, we reframe video inpainting as a conditional generative modeling problem and present a framework for solving such problems with conditional video diffusion models. We introduce inpainting-specific sampling schemes which capture crucial long-range dependencies in the context, and devise a novel method for conditioning on the known pixels in incomplete frames. We highlight the advantages of using a generative approach for this task, showing that our method is capable of generating diverse, high-quality inpaintings and synthesizing new content that is spatially, temporally, and semantically consistent with the provided context.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a conditional generative framework for video inpainting that leverages diffusion models to synthesize new, semantically coherent content for large occlusions. Unlike traditional methods dependent on optical flow, this approach achieves realistic object behavior and maintains temporal consistency even when entire content regions must be generated. Evaluated on newly constructed datasets, the framework demonstrates superior quality and consistency in inpainted sequences compared to existing methods.

### Strengths
1. The method effectively captures temporal and spatial dependencies, enabling high-quality synthesis for occluded scenes and objects.
2. Quantitative results show clear improvements over state-of-the-art methods, especially in challenging video inpainting scenarios.

### Weaknesses
1. Please provide inference costs (e.g., time and peak GPU memory usage) for a specified input size and number of frames, and compare these with other SOTA methods.

2. A dedicated ablation study comparing the method trained on standard datasets used by other methods versus the newly introduced datasets is suggested. This would help isolate the effects of the method itself from those of the datasets, as data alone can often address significant aspects of the problem.

3. The framework lacks clear illustration, making it difficult to grasp the main concepts. For instance, it is unclear how conditional inputs are processed in the forward pass, the roles of the trainable and frozen modules, or if any new layers for controllable generation are introduced.

4. Please also discuss the potential limitations or failure cases of the proposed method. Beyond inpainting cars, can this method inpaint other objects in a zero-shot manner?

### Questions
Please see the weaknesses.

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
3

### Summary
The authors extend the idea of Flexible Diffusion Model (FDM) to the video inpainting domain. A different sampling and training scheme is also developed to accomodate the new task.

### Strengths
- The paper is easy to follow
- The idea is intuitive and works also practically well
- The authors showcased that their model is better than flow- and attention-based video inpainting methods both qualitatively and quantitatively
- Different sampling schemes are also evaluated extensively.

### Weaknesses
Given that the authors proposed a variety of inference techniques, it would be interesting to investigate whether different sampling schemes during **training** makes a difference. It seems from Equation 3 that the $\mathcal{X}$ and $\mathcal{Y}$ are randomly sampled; would a benefit be gained e.g., when training the model in a similar way to how you sample at inference? Specifically, the current training procedure appears to treat all possible combinations of input and output frames equally, which might not be optimal. The lack of evaluation on standard video inpainting benchmarks, such as YouTube-VOS and DAVIS, is also a significant limitation. The current evaluation is limited to datasets that are not widely used, making it difficult to compare the proposed method with existing state-of-the-art techniques. Furthermore, the paper does not provide a clear analysis of the computational cost associated with the different sampling schemes, which is important for practical applications.

### Questions
Is the model trained from scratch? How well does it generalize to other, more complicated open video domains?

### Soundness
4

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
5

### Summary
State-of-the-art video inpainting methods focus on propagating visual information but struggle with generating novel content. This paper redefines video inpainting as a conditional generative task using video diffusion models, enabling synthesis of inpaintings with long-range temporal consistency. The approach leverages inpainting-specific sampling schemes to handle incomplete frames and is effective even when objects are partially visible or absent in the initial context.

### Strengths
1. The authors invest significant effort in building a large-scale video dataset to train the diffusion model.
2. Compared to previous video inpainting methods, the proposed model emphasizes filling in unseen content rather than relying solely on propagation.

### Weaknesses
1. Practicality concerns: The proposed dataset is heavily focused on scenarios involving cars, which restricts its generalizability to broader real-world applications.

2. Lack of control over inpainting content: The proposed model does not offer mechanisms to specify what should fill the missing regions.

3. Limited diversity in demonstrations: All examples shown in the paper involve cars in the inpainted regions. Are there demonstrations with objects other than cars?

4. Comparison with recent methods: Some recent mask-guided video editing techniques can also fill gaps with cars, offering options to specify the car model and color via text prompts. Why is there no comparison with these methods?

5. The claim of “strong experimental results” is potentially biased. The authors only test their model on BDD-Inpainting and Traffic-Scenes (datasets used for model training), while baselines are only trained on Youtube-VOS and DAVIS. This discrepancy in training data limits fair comparison.

### Questions
Inference time: How long does the proposed model take to process a typical 2-second video clip?

### Soundness
3

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
4

### Summary
This paper introduces a novel video inpainting framework based on conditional diffusion models, which can generate semantically consistent content that remains realistic over extended occlusions and diverse scene complexities. The authors present sampling schemes tailored for inpainting that capture essential long-range dependencies within the context and develop a new method to condition on known pixels in incomplete frames. Results show that the proposed method consistently outperforms methods based on optical flow or attention.

### Strengths
- The motivation is clear and the techniques sound reasonable.
- The writing and organization are easy to follow.
- The experiment result validates the effectiveness of this approach, especially for complex scenarios where occlusions (input information is scarce) prevent conventional methods from performing well.

### Weaknesses
1. The author needs to highlight this paper’s innovative contributions in the INTRODUCTION part and present a completed method graph rather than just showing model inputs.
2. This work relies heavily on the inpainting model to handle object occlusions and interactions. However, the authors do not address how the model performs in highly cluttered or dense environments with multiple possible object placements. Specifically, the paper lacks a discussion on how the model handles scenarios where multiple objects simultaneously enter and exit the masked regions, potentially leading to ambiguities in the generated content. The absence of analysis on how the model resolves these ambiguities is a significant weakness.
3. Additional experiments are needed to demonstrate the effectiveness of the sampling schemes and the model's generalization to non-traffic datasets, along with further comparisons/discussions with recent works, such as [1] [FFF-VDI](https://arxiv.org/pdf/2408.11402) [2] [FGT++](https://arxiv.org/pdf/2301.10048) [3] [SViT](https://openaccess.thecvf.com/content/ICCV2023/papers/Lee_Semantic-Aware_Dynamic_Parameter_for_Video_Inpainting_Transformer_ICCV_2023_paper.pdf). The current evaluation is limited to traffic datasets, which may not fully represent the model's capabilities in more diverse and complex scenarios. Furthermore, the lack of quantitative comparisons with the cited methods makes it difficult to assess the true advancement of this work.

### Questions
- Could you also provide quantitative comparisons of your method on the YouTube-VOS and DAVIS datasets? Additional results for object removal tasks would be more convincing.

### Soundness
3

### Presentation
3

### Contribution
2
