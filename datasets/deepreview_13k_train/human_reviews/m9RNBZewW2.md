# Overcoming False Illusions in Real-World Face Restoration with Multi-Modal Guided Diffusion Model

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
We introduce a novel Multi-modal Guided Real-World Face Restoration (MGFR) technique designed to improve the quality of facial image restoration from low-quality inputs.
Leveraging a blend of attribute text prompts, high-quality reference images, and identity information, MGFR can mitigate the generation of false facial attributes and identities often associated with generative face restoration methods. By incorporating a dual-control adapter and a two-stage training strategy, our method effectively utilizes multi-modal prior information for targeted restoration tasks. We also present the Reface-HQ dataset, comprising over 23,000 high-resolution facial images across 5,000 identities, to address the need for reference face training images. Our approach achieves superior visual quality in restoring facial details under severe degradation and allows for controlled restoration processes, enhancing the accuracy of identity preservation and attribute correction. Including negative quality samples and attribute prompts in the training further refines the model's ability to generate detailed and perceptually accurate images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper propose to utilize diffusion prior, as long as multi-modality input to perform real world face restoration. The method can receive text or reference image for face restoration. 

They also present a dataset that contains identity-image pair. 

There is both quantitative  and qualitative metric, which demonstrate the effectiveness of this method.

### Strengths
1. The motivation that using multi-modality input to assist face restoration is nice. As shown in the paper, there could be ambiguity during restoration, and the additional input could be helpful. 
2 .  The use of diffusion prior for this work also make sense, and it models a probability given the input. 
3. The dataset could be beneficial to the community.

### Weaknesses
1. The method used in the paper is not new. The main contribution of this works seems to be on the dataset and using expositing method on a newer task. 
2. Ablation of the effectiveness of using  trained diffusion prior is missing.

### Questions
1. The design of the Dual control Adapter is a little but tricky. Can one just replace it by a transformer?
    2. There can be different  result for every sample. How diverse is the model? And how to decide which sample to use?
    3. Will be dataset be realised?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work addresses the challenge of real-world face restoration. The authors introduce the Multi-modal Guided Real-World Face Restoration (MGFR) method, which improves facial image restoration from low-quality inputs using attribute prompts and reference images. Specifically, MGFR employs a dual-control adapter and a two-stage training strategy, leveraging a dataset of over 23,000 high-resolution images to enhance visual quality, identity preservation, and attribute correction. Experimental results demonstrate that the proposed method achieves superior performance.

### Strengths
1. The topic of real-world face restoration is interesting. 
2. The overall writing of the manuscript is clear and easy to follow.
3. This work introduces the Reface-HQ dataset, which comprises over 23,000 high-resolution images. This dataset can provide a foundation for training and evaluating the model.

### Weaknesses
1. The proposed method appears complex, and its running time and memory consumption are not superior to existing methods like DiffBIR and DR2. Since running time and memory usage are crucial for real-world applications, this raises concerns about its practical feasibility. The complexity stems from the dual-control adapter and the two-stage training strategy, which likely introduce significant overhead. A detailed analysis of the computational cost, including a breakdown of the FLOPs and memory usage for each component of the architecture, is needed to justify the method's practical applicability. Furthermore, the lack of specific comparisons to other state-of-the-art methods in terms of computational efficiency makes it difficult to assess the trade-off between performance and resource consumption.
2. There is a lack of comparison in FLOPs and Params in the main comparison and ablation study. This makes it difficult to assess the efficiency of the proposed method and to understand the impact of different components on the overall computational cost. The absence of this data limits the ability to compare the method's efficiency with other approaches and to identify potential bottlenecks in the architecture. A thorough analysis of the computational cost, including FLOPs and parameter counts, is essential for a comprehensive evaluation.
3. Lacking comparison to recent works (SUPIR, BFRffusion) in Table 1.
a. Scaling up to excellence: Practicing model scaling for photo-realistic image restoration in the wild
b. Towards real-world blind face restoration with generative diffusion prior.

### Questions
1. Not super important, but how do the authors feel the proposed method can be extended for real-world video face restoration? Can they please add some discussion on the scalability of the proposed method?
2. Overall the paper looks promising and makes meaningful contributions, however, it lacks some important experiments and details. The authors can refer to the weaknesses section.

### Soundness
4

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
The paper introduces a Multi-modal Guided Real-World Face Restoration (MGFR) approach, which aims to enhance facial image restoration from low-quality inputs by leveraging multi-modal prior information. This includes attribute text prompts, high-quality reference images, and identity information to mitigate false facial attributes and identities typically generated by current restoration methods. MGFR employs a dual-control adapter and a two-stage training strategy to effectively utilize these priors for targeted restoration tasks. The paper also introduces the Reface-HQ dataset, containing over 23K high-resolution facial images from 5K identities, to support the training of reference-based restoration models. The proposed approach demonstrates superior performance in restoring facial details, particularly under severe degradation, while ensuring identity preservation and attribute correction.

### Strengths
* Novel framework:

The MGFR approach introduces a novel dual-control adapter and two-stage training strategy, effectively combining multi-modal priors for enhanced face restoration. The use of attribute text prompts alongside high-quality reference images and identity information is a significant advancement, offering more control over the restoration process.

* Dataset Contribution:  
The introduction of the Reface-HQ dataset addresses a critical gap in the availability of high-resolution reference images, providing a valuable resource for the community.

* Good Performance: 
The method achieves superior visual quality in restoring facial details under severe degradation, demonstrating its practical applicability in real-world scenarios. The ability to control restoration through textual prompts enhances the flexibility and precision of the restoration process.

* Mitigation of False Illusions: MGFR effectively addresses the problem of false facial attributes and identities, a common issue in existing generative face restoration methods.

### Weaknesses
 * Complexity of Implementation:
The integration of multiple modalities and the dual-control adapter may introduce complexity in implementation. Therefore, I recommend that this paper should consider a more detailed information on computational requirements and scalability would be beneficial. Specifically, the paper lacks a thorough analysis of the computational overhead introduced by the dual-control adapter and the multi-modal fusion process. It would be beneficial to quantify the increase in FLOPs and parameter counts compared to single-modal or simpler restoration models. Furthermore, the paper should discuss the memory footprint of the model, especially when processing high-resolution images, and how this might impact its usability on resource-constrained devices.

* Evaluation Metrics:
While the paper demonstrates superior performance, a more thorough discussion of the evaluation metrics used to assess visual quality, identity preservation, and attribute correction would strengthen the claims. The paper should provide a detailed justification for the selection of each metric, explaining its relevance to the specific aspects of restoration being evaluated. For example, while metrics like PSNR and SSIM are commonly used, they may not fully capture the perceptual quality of restored images. The paper should also discuss the limitations of the chosen metrics and how they might bias the evaluation results. It would be beneficial to include a discussion on the sensitivity of each metric to different types of artifacts and distortions.

* Ablation Studies:
The paper would benefit from additional ablation studies to isolate the impact of each component (e.g., attribute prompts, reference images) on the overall performance, providing deeper insights into the effectiveness of each modality. The current ablation studies do not fully explore the interaction between different modalities. For instance, it would be valuable to investigate how the performance changes when attribute prompts are used without reference images, or vice versa. Furthermore, the paper should analyze the impact of different types of attribute prompts (e.g., simple vs. complex) and reference images (e.g., similar vs. dissimilar) on the restoration quality. A more granular analysis of the contribution of each component would provide a more complete understanding of the model's behavior.

### Questions
1) How will the performance vary if different versions of diffusion models are used? That is, would diffusion models be the strong foundation of achieving the good performance?

2) Some figures, say fig.4 and 5, are with too small fonts and unclear color denotions, making it less readable.

### Soundness
3

### Presentation
3

### Contribution
3
