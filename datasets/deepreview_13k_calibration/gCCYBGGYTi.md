# Contextual Kernels for Task-Aware Fine-Tuning in Vision-Language Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Vision-Language Models (VLMs) exhibit impressive generalization due to training on vast datasets like ImageNet. However, their performance diminishes on unfamiliar tasks. While downstream fine-tuning enhances adaptability, it often sacrifices inherent generality. To address this, we propose a novel method leveraging contextual generation for enhanced task representation within a semantic space. Our approach utilizes VLMs to generate detailed contextual descriptions for test image batches, developing Contextual Kernels (CK) for each class in the semantic space. 
Our test-time fine-tuning preserves core VLM features by freezing fundamental components and extending a linear network for semantic kernel density projection. This strategy significantly boosts model adaptability for real-world tasks. Despite strong zero-shot capabilities, we explore additional training samples to improve adaptability in dynamic Task Incremental Learning (TIL) scenarios. Each task's unique CK distribution serves as a fingerprint, enabling high-performance TIL with minimal forgetting. Experiments on four TIL datasets demonstrate the efficacy of our framework, achieving state-of-the-art performance. Our findings reveal that the semantic space within the text mode encapsulates both VLMs' generality and adaptability, paving the way for robust applications in diverse, evolving task environments. This work systematically balances generality and adaptability in VLMs, addressing a critical gap in current research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Generally, VLMs can be used in a zero-shot setting. However, this paper assumes that there are some training samples at test time. More specifically, the paper focuses on the Task Incremental Learning problem (TIL). The authors propose a novel method for test-time fine-tuning of VLMs. Given a test image, a (contextualized) image description is generated. Here context refers to things like view point (e.g. side view, front view, etc.) , style (e.g. art, sketch, etc.) or background (e.g. sky, forest, beach, etc). The key challenge is to balance between maintaining generality (not forgetting old tasks) and adapting to the new tasks. To maintain the generality, the VLM is frozen. To adapt to new tasks a projection matrix (a linear layer) is learned at test time through gradient decent. The loss function is a hinge loss rather than the usual cross-entropy loss.

### Strengths
The method is fairly simple. 
Comparison is done with a good number of the previous methods (10 methods), although I have some concerns about datasets (more on this will follow).

### Weaknesses
It seems that a good chunk of the experimental results on several data sets is completely missing. Table 1 shows the performance on the imagenet-R data set. I can’t seem to find similar tables for Cifar-100 and tiny-imagenet and imagenet-100 datasets.

Use of a predefined threshold on K(xs) to identify outliers and exclude them from training is not well justified. My concern is that at the beginning of the training process, where the projection matrix L is randomly initialized,  K(xs) values are poor estimates of the true similarity between an image and text and early exclusion of some training samples by thresholding based on such a noisy estimate of similarity may not be reliable. Furthermore, the impact of this threshold on the final performance is not explored, and it's unclear how sensitive the method is to this hyperparameter. A more principled approach to handling potential outliers, perhaps through a robust loss function or adaptive thresholding, would be beneficial.

All the experiments are done using ViT B/16 backbone. Performance using backbones other than ViT B/16 will provide more insight into the robustness of the proposed method. The choice of ViT-B/16 is not justified, and it's unclear how the method would perform with smaller or larger models. An ablation study on different backbones, including those with varying architectures and sizes, is necessary to assess the generalizability of the approach.

On page 6, N_j is defined as the number of pre-defined context. It is not clear what that means and if it is predefined. More broadly, the authors use the term “context” throughout the paper without clearly explain what that mean. A clear example would help. Or at least properly explain Figure 2. The brief list provided in the appendix feels disconnected from the main body of the paper. The lack of a clear definition of 'context' makes it difficult to understand the scope and limitations of the method. The authors should provide a more rigorous definition and examples of how different contexts are used in the experiments.

In eq4, Ks is for text modality and Kt is for image. But in explanation that follows eq 5, s is for image modality and t is for text. In the table of symbols in A4, l is for text, t is for task and s is for image. Please clarify the notation. The inconsistent notation across different parts of the paper creates confusion and makes it difficult to follow the technical details. A consistent and clearly defined notation is crucial for the clarity and reproducibility of the work.

### Questions
The loss function is a margin base or hinge loss (Eq6) instead of the usual cross-entropy loss. When using a hinge loss usually the choice of negative samples affects the convergence. Did the authors face any issue in regards to convergence and the choice of negative samples in the hinge loss?

### Soundness
3

### Presentation
2

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
This paper introduces the concept of context kernels (CKs) to deal with Task Incremental Learning scenarios. Specifically, the paper proposes a framework that operates in two stages: 1) Generate CK representation for each class using a context prompt pool; 2) Train a projection network to learn the semantic representation and effectively separate different tasks and classes in the semantic kernel space. A threshold CK-based confidence check is further introduced to filter out task-irrelevant test samples during inference and ensure robustness in safety-critical applications. Extensive experiments over a wide range of datasets show that the proposed approach achieves significantly better performance over existing techniques.

### Strengths
1. The paper provides a comparison of the proposed method against a number of competitive prior works, and carried out experiments on various datasets for the TIL task, which is sufficient to validate the approach. The empirical results demonstrate that the framework achieves significantly better performance than previous techniques. 

2. The CK-based confidence score is a clever way to make models refrain from making decisions over input samples outside the scope of the tasks that it learns to handle. This module allows for the possibility of application in safety-critical scenarios such as autonomous driving and medical diagnostics, adding to the practicality of the paper.

3. The paper offers an interesting observation on the semantic distribution of different datasets in the introduction, efficiently displaying the motivation behind the framework design.

### Weaknesses
1. The formulation of the proposed framework as well as presentation of each module is convoluted at times and not easy to follow. In my view, the paper needs to put more effort into explaining the entire pipeline without jumping into the specifics first. Additionally, too much space is dedicated to describing the framework design and the analysis on experimental results is too brief. In Section 4.1, the paper says “…Tables 1 illustrate that our proposed method consistently outperforms existing techniques…”. Perhaps it should be “Tables 1 and 2” since Table 1 only shows the results on ImageNet-R. Another crucial section missing is ablation study on different modules, which seems not to be included anywhere in the paper.

2. The figures in the paper are aesthetically unappealing and doesn’t really highlight the streamline of the framework to help readers understand. Especially in Figure 1, the figure is not centered and some of the fonts even overlap with the title.

3. Throughout the paper, “generality” is consistently used, but the correct word should be “generalizability” or “generalization capability”.

### Questions
Do we need to hand-craft the word list in the context prompt pool, or is that done somehow automatically? The paper claims that the context prompt pool is extensible. It would be nice if the authors could shed some light on how to do so.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a Contextual Kernel Density-Based Task Representation Learning Framework to enhance the performance of VLMs for Task Incremental Learning. This method constructs Contextual Kernels (CKs) in the semantic space, enabling task-specific class separation and enhanced model adaptability during fine-tuning. Authors conducted extensive experiments on multiple datasets and the results validate the effectiveness of this approach.

### Strengths
- Originality: The proposed CK framework provides a new approach to TIL by focusing on contextual kernels for task-specific fine-tuning. 

- The overall presentation is clear.

- The performance of the CK framework is superior to that of existing methods.

### Weaknesses
 - The proposed CK framework needs kernel computing, which might be time-consuming. Could authors provide a training time comparison of CK and other methods to demonstrate the training efficiency of the CK framework?

- The implementation is unclear. Since the authors did not provide any code, could authors further provide a pseudo-code to better understand how authors implement their framework? 

- The form of $P$ in Eq. 8 is different from other parts.

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
