# UIFace: Unleashing Inherent Model Capabilities to Enhance Intra-Class Diversity in Synthetic Face Recognition

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Face recognition (FR) stands as one of the most crucial applications in computer vision. The accuracy of FR models has significantly improved in recent years due to the availability of large-scale human face datasets. However, directly using these datasets can inevitably lead to privacy and legal problems. Generating synthetic data to train FR models is a feasible solution to circumvent these issues. While existing synthetic-based face recognition methods have made significant progress in generating identity-preserving images, they are severely plagued by context overfitting, resulting in a lack of intra-class diversity of generated images and poor face recognition performance. In this paper, we propose a framework to $\textbf{U}$nleash model $\textbf{I}$nherent capabilities to enhance intra-class diversity for synthetic face recognition, shorted as $\textbf{UIFace}$. Our framework first train a diffusion model that can perform denoising conditioned on either identity contexts or a learnable empty context. The former generates identity-preserving images but lacks variations, while the latter exploits the model's intrinsic ability to synthesize intra-class-diversified images but with random identities. Then we adopt a novel two-stage denoising strategy to fully leverage the strengths of both type of contexts, resulting in images that are diverse as well as identity-preserving. Moreover, an attention injection module is introduced to further augment the intra-class variations by utilizing attention maps from the empty context to guide the denoising process in ID-conditioned generation. Experiments show that our method significantly surpasses previous approaches with even less training data and half the size of synthetic dataset. More surprisingly, the proposed $\textbf{UIFace}$ even achieves comparable performance of FR models trained on real datasets when we increase the number of synthetic identities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of improving synthetic data generation for face recognition (FR) by tackling the issue of context overfitting, which leads to low intra-class diversity and diminished performance. The authors introduce a novel framework named UIFace, designed to enhance intra-class diversity while maintaining identity preservation. The approach begins by training a diffusion model capable of denoising under identity-conditioned contexts or a learnable empty context. The identity context generates images that maintain identity but lack variation, while the empty context leverages the model's intrinsic ability to produce diverse images, albeit with random identities.

### Strengths
1. UIFace seems to be closer to the dataset diversity of real datasets than the previous method IDiff-face.
2. better results can be achieved using less amount of synthetic data, and with increasing amount of data even approaching the performance of direct datasets

### Weaknesses
1. The main contribution of the paper lies in the observation that LDM learns different aspects during both pre-training and post-training. However, only the analysis based on Figure 2 is currently insufficient, and there is a lack of theoretical discussion. Specifically, the paper does not provide a clear explanation of why the diffusion model, during its reverse process, initially recovers identity-irrelevant content before focusing on identity-relevant details. The observation that the model first recovers low-frequency components and later high-frequency components is not sufficiently substantiated with theoretical backing, and the connection to identity is not clearly established. A more rigorous analysis is needed to explain this behavior in the context of diffusion model training and sampling.

2. The training and testing times for the two-stage LDM should be provided for comparison with the one-stage methods. The paper lacks a detailed analysis of the computational overhead introduced by the two-stage sampling process. It is crucial to understand the trade-offs between the improved performance and the increased computational cost. The authors should provide a breakdown of the time spent in each stage of the sampling process, and compare it to the time required by single-stage methods. This would allow for a more comprehensive evaluation of the practical applicability of the proposed approach.

3. The font size of the axis labels in Figure 2 is too small, and it appears that the author has not used \citep and \citet correctly.

### Questions
The authors are encouraged to include a theoretical analysis explaining how LDM learns different subjects at different training time steps.

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
This paper tries to solve the problem of intra-class diversity with the generation of synthetic images in face recognition, and proposes a two-stage pipeline framework of DDPM with two improvements, including adaptive stage partition strategy and attention injection module. Solid results are achieved.

### Strengths
Originality: The method was proposed upon the previous DDPM with two tricks raised by the observation that early stage and later stage of denoising step can capture different semantic meanings of images.  
Quality: The methodology is conceptually simple with massive experiments supported. The solid results have achieved on public benchmarks. 
Clarify: The idea, albeit simple, has been clearly presented. It is better to re-structure introduce and related work slightly by minimizing the depiction of FR while maximizing the work related to data synthesis by generation methods.  
Significance: The authors declared that the proposed methods achieved sota performance of face recognition by training models with synthetic images. There is no future work being declared to improve the work.

### Weaknesses
1. The method is proposed upon the previous DDPM work by using identity context maps as conditions. Two improvements, including adaptive partitioning strategy and attention injection module, have been added to enhance the performance of the methods.
2. The authors declared they proposed a framework of face image synthesis by generating methods. Can authors clarify if the framework is suitable for other image generation tech, besides DDPM.
3. The paper is well-structured. However, there are certain grammar and typo errors.
4.  For introduction and related work sections, the description of background can go more specific to synthetic data-based face recognition rather than face recognition. 
5. More recent face image synthetic methods should be investigated. 
6. The authors have implied that synthetic images can solve privacy and legal issues. Please clarify how your methods can avoid privacy and legal issues, since synthetic images are generated on real-world images. 
7. Extra experiments should be conducted to support the methods raised by this work. For example, different settings of fixed t_{0} should be examined, also "baseline + 2-stage-fixed + attn" should be conducted in the ablation experiment.

### Questions
1. In this abstract section, can authors explain how the methods raised in this paper preserve the privacy and legality. If this is not related to the research purpose, it is better to exclude it in case of misleading readers.  
2. There were more methods proposed upon IDiff and had better performance, for example, “SDFR: Synthetic Data for Face Recognition Competition”.
3. Line 308, ... by leveraging... Carefully check the grammar and typo errors.
4. It is not very clear about timestep interval T analysis in Figure. The interval upperbound of the x-axis is incrementally increased or resets as well the interval lowerbound.
5. For experimentation, different settings of fixed t_{0} should be examined, also "baseline + 2-stage-fixed + attn" should be conducted.

### Soundness
3

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
The paper addresses the challenge of generating diverse synthetic face images for the purpose of training face recognition models. The authors introduce a novel framework named UIFace, which employs a two-stage denoising approach alongside an attention injection module. This combination is designed to increase intra-class diversity while preserving identity consistency. As a result, UIFace achieves performance that is competitive with models trained on real-world datasets.

### Strengths
1. The two-stage denoising strategy and the attention injection module work together to generate diverse images while maintaining identity preservation, effectively addressing the issue of context overfitting.
2. The adaptive partitioning strategy dynamically identifies the optimal moment to transition between the two denoising stages, thereby enhancing both the quality and diversity of the generated images.
3. UIFace demonstrates its effectiveness by achieving performance on par with models trained on real datasets.

### Weaknesses
1. What about the scalability of the model? Are there any potential benefits to further increasing the number of identities beyond the 20K shown in Table 1?
2. While this paper focuses on enhancing the intra-class diversity for a specific identity, what about the inter-class discrepancies, which are also critical for training an effective face recognition model? How do the authors ensure this aspect is adequately addressed in their work?
3. The details of the overall training pipeline could be more clearly explained. For instance, in Stage 2, how are the losses from the unconditional and conditional branches calculated and combined? Furthermore, how does the adaptive partitioning strategy interact with the loss calculation, and what is the precise mechanism for determining the transition point between the two denoising stages?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
