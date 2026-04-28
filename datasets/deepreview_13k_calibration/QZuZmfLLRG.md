# LW2G: Learning Whether to Grow for Prompt-based Continual Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 5, 6

## Abstract
Continual Learning (CL) aims to learn in non-stationary scenarios, progressively acquiring and maintaining knowledge from sequential tasks. Recent Prompt-based Continual Learning (PCL) has achieved remarkable performance with Pre-Trained Models (PTMs). These approaches grow a prompt sets pool by adding a new set of prompts when learning each new task (\emph{prompt learning}) and adopt a matching mechanism to select the correct set for each testing sample (\emph{prompt retrieval}). Previous studies focus on the latter stage by improving the matching mechanism to enhance Prompt Retrieval Accuracy (PRA). To promote cross-task knowledge facilitation and form an effective and efficient prompt sets pool, we propose a plug-in module in the former stage to \textbf{Learn Whether to Grow (LW2G)} based on the disparities between tasks. Specifically, a shared set of prompts is utilized when several tasks share certain commonalities, and a new set is added when there are significant differences between the new task and previous tasks. Inspired by Gradient Projection Continual Learning, our LW2G develops a metric called Hinder Forward Capability (HFC) to measure the hindrance imposed on learning new tasks by surgically modifying the original gradient onto the orthogonal complement of the old feature space. With HFC, an automated scheme Dynamic Growing Approach adaptively learns whether to grow with a dynamic threshold. Furthermore, we design a gradient-based constraint to ensure the consistency between the updating prompts and pre-trained knowledge, and a prompts weights reusing strategy to enhance forward transfer. Extensive experiments show the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes a strategy for determining the dynamic expansion of the prompt pool over time for prompt-based Continual Learning methods, based on techniques inspired by Gradient Projection Memory for Continual Learning.

### Strengths
The motivation of the proposed method is clear. There are theoretical supports. The experimental superiority over baselines can be seen.

### Weaknesses
1. It seems to me that this paper is the application of the technique in [1] to the existing methods with the criteria to expand the prompt pool. However, this technique is quite similar to those in [2], [3]. The authors should highlight the novelty and innovative contribution of this work.

2. It is not clear how the performance on CUB of HiDE is has minimal change, while those on CIFAR100 and ImageNet-R is decrease significantly. If the codebase of HiDE has some problem, why didn't the authors consider other codebases of other baselines?

3. The authors claim their method can promote positive knowledge transfer, however relevant experimental results seem to be lacking.

4. The method saves the number of parameters to learn, but storing the basis vectors of the subspaces is also expensive.

5. This work is close to [1], thus, it is essential to have the comparisons between them.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

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
The paper proposes a new method called LW2G (Learning Whether to Grow) for prompt-based continual learning.
LW2G decides whether to grow the prompt pool or reuse existing prompts when learning a new task, based on measuring the hindrance of learning the new task on old prompts compared to an ideal hindrance-free scenario. I think the idea of Hinder Forward Capability (HFC) is inspiring, that measures the difference between new and old tasks as well as the hindrance imposed on learning new tasks under a strict orthogonality constraint to old task feature spaces.
Extensive experiments demonstrating the effectiveness of adding LW2G to existing prompt-based continual learning methods across multiple datasets and settings.

### Strengths
- LW2G is an approach that actively decides whether to grow new prompts or reuse existing ones for each new task. This aspect distinguishes LW2G from previous methods.

- Introduces a new Hinder Forward Capability (HFC) metric to quantify the hindrance of learning a new task on old prompts under orthogonality constraints. 

- The three main components of LW2G - DGA, CPK, and FFT - provide a complete implementation for reusing existing prompts in continual learning tasks. However, to some extent, the approach is quite redundant, as it requires repeatedly training all the prompts to determine the optimal reuse strategy.

- The authors have shared their code and implementation, which, although I haven't personally tested it, lends some credibility to the soundness of their method. At least, from the README.md file, it appears they have provided a full implementation of the Hide-Prompt version.

- Overall, the proposed method is sound as there are so comprehensive experiments.

### Weaknesses
 - One important aspect missing from the experiments in this paper is the average results from multiple runs. This is particularly evident in the paper, as the experimental results in Tables 1, 2, and 3 show that the proposed method has only a slight difference compared to the baselines. It's quite possible that running the baselines multiple times could yield a better result. I'm not claiming that this paper has done so. But providing the mean and standard deviation would better demonstrate statistical robustness.

- LW2G  needs for significant manual intervention and careful hyperparameter selection to ensure the prompt resule/increase strategy works appropriately. For example, HFC thresholds, CPK's soft constraint coefficient and FFT's top-N selection.

### Questions
see above

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
3

### Summary
This paper proposes a plug-in module within existing Prompt-based Continual Learning (PCL), 
called Learning Whether To Grow (LW2G). LW2G enables PCL to dynamically learn to whether to add a new set of prompts for each task (to grow) or to utilize an existing set of prompts (not to grow) based on the relationships between tasks. LW2G consists of three components: Dynamic Growing Approach (DGA), Consistency with Pre-trained Knowledge (CPK), and Facilitation for Forward Transfer (FFT). Its superiority across multiple benchmarks and various CL settings is also verified.

### Strengths
(1)By learning whether to grow or not to grow set of prompts, this work forms an effective and efficient prompt sets pool where each single set contains knowledge from multiple tasks, thus facilitating cross-task promotion. 
(2)LW2G is a plug-in and effective module within existing PCL.

### Weaknesses
I have two main concerns: 
(1)The proposed LW2G is mainly designed for prompt-based CL methods, and further improves their performances. However, the improvements with respect to the mainstream CL metrics, FAA and FMM, as shown in Table 1, are not significant. In particular, for some stronger baselines, S-prompt++, the performance with LW2G makes no obvious performance. 
(2)It seems that the performance reported on the Hide-prompt paper is better than that in this work, in which Hide-prompt even performs better than S-prompt++.
(3) FFA or FAA? It is a little confused.

### Questions
(1)Does LW2G still work in the context of various pre-trained models?
(2)Is it still effective in more prompt-based CL methods, such as coda-prompt?
(3)As more recent studies show, lora-based CL methods are more effective than prompt-based in CIL tasks. So, does the proposed strategy have more advantages?
(4)When does the Theorem 1 hold? Any assumptions?

### Soundness
2

### Presentation
3

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
In this paper, the authors propose a method namely Learn Whether to Grow (LW2G), wherein a shared set of prompts is utilized when several tasks share certain commonalities, and a new set is added when there are significant differences between the new task and previous tasks. The proposed  LW2G develops a metric named Hinder Forward Capability (HFC) to measure the hindrance. With HFC, an automated scheme Dynamic Growing Approach adaptively learns whether to grow with a dynamic threshold. Furthermore, a gradient-based constraint is introduced to ensure consistency between the updating prompts and pre-trained knowledge. Extensive experiments are provided.

### Strengths
The experiments and analysis are very thorough and well-written, and the proposed method has some novelty

### Weaknesses
Weakness：

1: I agree that Prompt Retrieval Accuracy (PRA) has a certain impact on performance and is an urgent problem to be solved before 2023. However, some of the lasted prompt-based methods ([1], [2], etc) and some of the lasted Adapter-Based methods ([3], [4], [5], etc.) do not need to consider PRA issues and surpass the classical methods using the matching mechanism. I have doubts whether the PRA problem should be the main motivation for building continuous learning solutions using pre-trained models.

2: There are also some methods for optimizing the prompt selection (matching) mechanism. For example, [6], [7], [8] all try to improve the matching mechanism. Compared with the above methods, the improvement of the projection method seems to be relatively limited. it may not prove that your method is superior to them.

3: The comparison is not sufficient, lacking performance comparison of some of the latest methods (as above) and the display of plug-in effects in the latest methods, etc. 

4: Gradient projection and whether to choose growth are not novel in the field of CL, but they are somewhat novel in the PTM-based CIL task.

### Questions
see the weakness.

I'd like to raise my score if all my concerns are addressed.

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
This paper introduces Learning Whether to Grow (LW2G), a plug-in module for Prompt-based Continual Learning (PCL). LW2G determines whether to expand the prompt pool by adding new prompts or reusing existing ones based on the similarity between tasks, aiming to improve efficiency and knowledge transfer. Inspired by Gradient Projection Continual Learning (GPCL), the method leverages orthogonal projections to measure task interference using a new metric called Hinder Forward Capability (HFC). LW2G also introduces strategies for gradient-based prompt consistency and prompt weight reuse to further optimize learning. Experimental results show that LW2G improved the performances of three baseline PCL models.

### Strengths
1. Dynamically growing the prompt pool for PCL methods aligns well with the continual learning paradigm.

2. Using a gradient-projection-based metric to assess task similarity looks reasonable.

### Weaknesses
While the idea of leveraging orthogonal conditions to mitigate forgetting is reasonable, the paper does not sufficiently formulate this method within the context of PCL. Section 3 introduces the formulation for layer $l$, but it lacks clarity on how this formulation applies specifically for PCL, where prompts serve as the primary trainable parameters. Specifically, the paper needs to elaborate on how the gradient projection is performed with respect to the prompt parameters and how the representation matrix, $\mathbf{R}_t^l$, is constructed when prompts, rather than network weights, are the focus. A detailed and precise formulation, including the derivation of the update rules for prompt parameters, is essential to fully understand the proposed method.

The reported performance of baseline models appears lower than those reported in prior work. For instance, the paper does not address the significant performance gap between the reported results and those achieved by HiDe-Prompt when initialized with ImageNet-21K pre-trained weights. The authors should clarify whether their implementation of HiDe-Prompt differs from the original and provide a detailed comparison of the experimental setups. These discrepancies raise concerns about the reliability of the reported results and warrant further explanation.

The differences between the proposed LW2G and other orthogonal continual learning methods are not sufficiently highlighted. The paper should provide a more explicit comparison, particularly regarding how LW2G's approach to dynamic prompt pool expansion differs from existing methods that use orthogonal constraints. A table summarizing the key differences in terms of methodology, computational cost, and performance would help better position LW2G and clarify its unique contributions.

Some terminologies require clearer definitions. For example, the term “matrix with suitable dimensions” in the context of constructing the orthogonal basis is vague. A more precise description is needed to avoid confusion. The authors should explicitly define the dimensions and provide a concrete example of how this matrix is derived in practice.

Some minors. 1) There seem to be some messy codes in line 082. 2) Use “ViT” instead of “VIT” to align with established conventions. 3) The notion $l$ is slightly reused for the layer index and the number of bases for space $\mathcal{S}_1$. The authors should consider using a different symbol to avoid ambiguity.

### Questions
1. Does the proposed method require computing the representation matrix for every layer after learning each task? Additionally, what specific samples are used to calculate the representation matrix?

2. What does the variable $N$ in line 165 refer to? 

3. How is $\mathbf{B}_t^l$ obtained? While it appears to be introduced in the supplementary material, it is recommended to briefly explain this process in the main paper as it is essential for understanding the overall method.

### Soundness
3

### Presentation
2

### Contribution
2
