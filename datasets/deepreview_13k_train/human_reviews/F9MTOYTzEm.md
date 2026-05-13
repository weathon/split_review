# Instance-level Consistent Graph With Unsupervised Human Parts for Person Re-identification

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
The representation of human parts plays a crucial role in person re-identification (re-ID) by offering discriminative cues, yet it presents challenges such as misalignment, occlusion, and extreme illumination. Previous methods have primarily focused on achieving strict part-level consistency. However, individual part features change inevitably under harsh conditions, hindering consistent representation. In this article, we propose an Instance-level Consistent Graph (ICG) framework to address this issue, which extracts structural information by introducing graph modeling atop unsupervised human parts. Firstly, we introduce an attention-based foreground separation to suppress non-instance noise. Subsequently, an unsupervised clustering method is designed to segment pixel-wise human parts within the foreground, enabling fine-grained part representations. We propose a flexible structure graph that derives instance-level structure from part features, treating each part feature as a node in a graph convolutional network. In essence, ICG mitigates incompleteness through feature flow among nodes, broadening the matching condition from strict part-level consistency to robust instance-level consistency. Extensive experiments on three popular person re-ID datasets demonstrate that ICG surpasses most state-of-the-art methods, exhibiting remarkable improvements over the baseline.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new person reID method, including two main parts, i.e., the attention-based foreground mask unit and the unsupervised clustering unit. Futhermore, a graph model is built for instance-level consistence. The experimental results are good.

### Strengths
1. The motivation of address the confilct between the fine-grained and coarse-grained pipelines are reasonable, and the proposed graph model for instance consistency is new.
2. The introduced pixel-wise human parts clustering is novel, which play an important role for balance the fine-or-coarse constrain for parts.
3. The experimental evaluation is sufficient and the results are excellent.

### Weaknesses
1. The attention-based foreground mask learning is not new, which has been propsoed in previous work [1] for person reID.  The difference or the advantage of the the proposed AFM should be discussed.
2. The compared methods are most out-of-date, more recently propsoed methods should be compared.

### Questions
Why not adopt the well-segmented foreground mask directly? The learned attention map involves lots of noises.

### Soundness
2

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
This paper presents an Instance-level Consistent Graph (ICG) framework for person re-identification, addressing the challenging issues of part misalignment and feature inconsistency. The proposed method integrates attention-based foreground separation, unsupervised human parts clustering, and graph-based structural modeling to achieve instance-level consistency. The framework demonstrates promising results on several benchmark datasets.

### Strengths
1 The paper's primary contribution lies in its pragmatic approach to handling part misalignment in person re-ID. Instead of pursuing strict part-level consistency, which often fails under challenging conditions, the authors propose a more flexible instance-level consistency approach. 

2 The unsupervised nature of the human parts clustering is particularly noteworthy, as it eliminates the need for additional supervision or pre-trained models, making the solution more deployable in real-world scenarios. 

3 The experimental results across multiple datasets demonstrate the effectiveness of this approach.

### Weaknesses
1 The primary weakness of this work lies in its limited theoretical novelty and reliance on conventional methodologies. The core components - attention mechanism, K-means clustering, and graph convolutional networks - are well-established techniques that have been extensively studied in the field. While the integration of these components is practical, it does not present significant methodological advancement.

2 The use of basic K-means clustering and standard GCN architecture appears dated compared to recent developments in self-attention mechanisms, advanced clustering techniques, and modern graph learning approaches. The paper would benefit substantially from incorporating more contemporary methodologies and providing stronger theoretical justification for the chosen approach.

3 The paper lacks comprehensive analysis in several crucial aspects. The absence of detailed ablation studies makes it difficult to understand the relative importance of each component. The computational complexity and runtime performance considerations are not adequately addressed, which are crucial factors for practical deployment. The robustness of the clustering approach to different parameters and varying environmental conditions needs more thorough investigation.

### Questions
1 Include comprehensive ablation studies and failure case analyses to provide deeper insights into the framework's behavior and limitations. This should be accompanied by detailed computational complexity analysis and runtime performance evaluations.

2 Expand the experimental evaluation to include comparisons with recent transformer-based approaches and demonstrate the method's robustness under various challenging conditions. The addition of qualitative results showing the clustering and graph construction process would enhance the paper's clarity.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a newframework, Instance-level Consistent Graph (ICG), aimed at addressing the challenges of part misalignment and feature incompleteness in person re-identification tasks. The ICG framework innovatively integrates an attention-based foreground mask (AFM), pixel-wise human parts clustering (PPC), and a flexible structure graph (FSG) to extract robust structural features that are tolerant to variations in part arrangements or absences. 

The AFM module enhances the foreground features by suppressing background noise, while the PPC module performs pixel-level clustering to segment fine-grained human parts within the foreground. The FSG then constructs a graph where each part feature is treated as a node, allowing for feature interaction and consistent representation even with incomplete parts. Extensive experiments on three major person re-ID datasets demonstrate that the ICG framework outperforms state-of-the-art methods and showcases significant improvements over the baseline model.

### Strengths
1. The concept of moving from strict part-level consistency to a more robust instance-level consistency is innovative and expands the possibilities for handling misalignment and occlusion in re-ID tasks.

2. The experiments are rigorous and well-designed, with performance metrics that are standard in the field. The paper demonstrates a significant improvement over the baseline and state-of-the-art methods, which speaks to the quality of the proposed approach.

3. The paper is well-written and organized, with a logical flow that makes it easy to follow. The introduction effectively sets the stage for the problem, the methodology is clearly described, and the results are presented in a manner that is easy to understand.

### Weaknesses
1. While the paper demonstrates strong performance on the three major datasets, it lacks a discussion on the generalizability of the ICG framework to other datasets or scenarios with different characteristics. Adding experiments on more diverse datasets, including those with more significant variations in lighting, pose, and background clutter, could strengthen the paper's claims. The computational complexity of the ICG framework is not discussed, making it difficult to assess its practicality for real-time applications or resource-constrained environments. A detailed analysis of the model size, FLOPs, and inference time would be beneficial. 

2. The paper could improve by providing a more in-depth discussion on the limitations of the ICG framework. For instance, are there specific scenarios or types of occlusion, such as severe occlusions caused by large objects or other people, where the method underperforms? A quantitative analysis of performance under different occlusion levels would be valuable. Furthermore, how does the method handle significant changes in clothing appearance, which is a common challenge in person re-identification? 

3. The paper could address potential ethical considerations and biases in the proposed system, especially since person re-identification has implications for privacy and surveillance. Discussing how the model handles different demographic groups and mitigating bias would be an important addition. For example, does the model exhibit performance disparities across different skin tones, genders, or age groups? The paper should also discuss the potential for misuse of the technology and propose safeguards.

4. The typesetting of this paper seems unreasonable, and the content is not rich enough. For example, Figure 2 is placed at the bottom of the page, while Table 1 exceeds the width of the page. Also, this paper seems like it should further discuss additional experiments and ethical issues in an appendix, but it does not provide one. The lack of an appendix limits the ability to include more detailed information without disrupting the main flow of the paper.

5. Based on the current version of the paper, it seems that the paper is difficult to replicate due to a lack of sufficient detail. The paper does not provide sufficient information regarding the similarity measurement between query and test images, nor does it provide sufficient detail on the loss function. The specific implementation details of the AFM, PPC, and FSG modules are also not fully elaborated, making it challenging for other researchers to reproduce the results.

### Questions
Will you make your code and model publicly available? This is important for the development of the field.

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
5

### Summary
This paper introduces the Instance-level Consistent Graph (ICG) framework to improve person re-identification (re-ID) by addressing challenges such as misalignment, occlusion, and varying illumination. ICG employs an attention-based foreground mask to separate instances from non-instance noise, followed by pixel-wise clustering for extracting fine-grained human part representations. A graph convolutional network then organizes these part features into a flexible structure graph, enabling instance-level structural consistency and improving resilience to feature incompleteness. Extensive evaluations on three popular re-ID datasets demonstrate superior performance over state-of-the-art methods.

### Strengths
1.Effective Module Design: The integration of three core components—the attention-based foreground mask (AFM), pixel-wise human parts clustering (PPC), and flexible structure graph (FSG)—is systematically designed and demonstrates effectiveness through improved feature alignment and robustness.

2.Solid Empirical Validation: The paper provides a thorough evaluation, with experimental results showcasing clear improvements over baseline models across various datasets (e.g., Market-1501, DukeMTMC-reID, and MSMT17), demonstrating ICG’s ability to handle occlusions and alignment issues.

### Weaknesses
1.Engineering-focused: The method, though innovative, may appear incremental as it combines known techniques (attention, clustering, graph convolution) without fundamentally novel theoretical contributions. Further insights into ICG’s scalability or potential applications could strengthen the impact.

2.Limited Component Analysis: More detailed ablation studies on individual settings within each module (such as varying clustering levels within PPC or adjacency thresholds in FSG) could provide a clearer understanding of the specific impact of each component.

3.The paper’s overall approach is straightforward, but many modules consist of existing techniques without significant innovation, making this work largely incremental.

4.The method comparisons are somewhat outdated. In recent years (2023-2024), traditional re-ID methods have continued to make advancements, with many reaching mAP scores around 91-92 on Market-1501 without relying on pretrained weights like CLIP. The authors should include more recent benchmarks to better contextualize their results.

5.The method heavily depends on the quality of the masks, yet in Figure 8, visualizations reveal that many irrelevant areas (e.g., background) are still extracted alongside the person. This interference can disrupt alignment. To improve robustness, the authors should prioritize generating higher-quality masks that better isolate the target person.

6.The paper lacks an analysis of computational complexity, including trainable parameters and FLOPs. The authors should provide this analysis and offer comparisons to similar methods to give a clearer understanding of the model’s efficiency.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2
