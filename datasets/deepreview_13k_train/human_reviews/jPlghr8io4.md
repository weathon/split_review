# Learning with Analogical Reasoning for Robust Few-Shot Learning

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Few-shot learning (FSL) is challenging due to limited support data for model training. The situation is much worse when the support data is contaminated with noise. To address this issue, we propose a novel \textbf{T}ransformer-based \textbf{A}nalogical \textbf{R}easoning model for \textbf{N}oisy \textbf{F}ew-\textbf{S}hot learning (TarNFS), by mimicing the human's ability of learning by analogy. Concretely, we assume the existence of a large human cultivated or AI-powered knowledge base, and hypothesize that similar concepts in the knowledge base are visually similar in the latent space as well. Then we design a transformer-based analogical reasoning model to utilize inter-concept connections among these concepts, aiming to build robust and discriminative classification boundaries. In addition, we propose a task-level contrastive learning to analogically learn from negative tasks to facilitate training with noisy tasks. Experiments demonstrate that our TarNFS enables more effective learning from limited and imperfect data. It not only improves the generalization ability of FSL in different noisy settings but also achieves competitive performance in the common clean FSL settings. Code is publicly available \href{https://anonymous.4open.science/r/iclr2088}{here}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of Few-shot Learning with contaminated support data. To tackle this issue, the authors introduce a learning paradigm inspired by analogical reasoning. Specifically, the paper proposes a new approach to model inter-concept connections, which is then leveraged to improve inference in the presence of noisy support data. Additionally, the paper introduces a task-level contrastive learning strategy to mitigate the impact of noisy labels. To validate the effectiveness of the proposed method, the authors conduct experiments on several widely-used datasets, including MiniImageNet and TieredImageNet. The results demonstrate a significant enhancement in performance compared to existing methods.


=========================================================================
The rebuttal has addressed my concerns. I choose to increase my score.

### Strengths
The concept of employing semantic and analogical reasoning to improve the performance of few-shot learning with noisy labels appears promising. The writing and presentation of the methods in this paper are clear and well-articulated.
This paper conducts a thorough analysis of the method using two datasets to demonstrate the contributions of each component and to compare performance across different benchmarks.
The results obtained from the two datasets indicate a significant enhancement in performance of the proposed method compared to existing approaches.

### Weaknesses
While the author presents a detailed analysis using two datasets, I am concerned about their similarity. It would be beneficial if additional results could be demonstrated using other datasets, such as CUB and CIFAR-FS, to further validate the robustness of the method. Specifically, the datasets used, MiniImageNet and TieredImageNet, share a similar structure and origin, which might not fully expose the limitations of the proposed approach. The methodology would be more convincing if it were also validated on a larger dataset, such as the Meta-Dataset. This would help in assessing its scalability and effectiveness across a broader range of learning scenarios. The current evaluation does not sufficiently explore the method's performance under diverse conditions. The training procedure is multi-staged and could pose challenges in terms of reproducibility. Unfortunately, the author does not provide the code, which would be extremely helpful for those attempting to replicate the study's results. The absence of code makes it difficult to verify the implementation details and to ensure that the reported performance gains are not due to specific implementation choices or hyperparameter tuning.

### Questions
From Table 4, I noted that the proposed method outperforms the oracle under a 20% noise setting. Could the author provide examples of several pairs of support and query instances where the oracle fails to classify correctly, but the proposed TarNFS method succeeds? This would offer deeper insights into the strengths of the method.
I observe that the TCL module exhibits a larger margin of improvement compared to AR. Could the author present an analysis that isolates the impact of using the TCL module alone? This comparison would help clarify the individual contribution of the TCL module to the overall performance.

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
5

### Summary
This paper proposes TarNFS, a Transformer-based analogical reasoning model to improve Few-Shot Learning (FSL) in noisy environments. It enhances class prototypes using a knowledge base with multi-head self-attention and introduces task-level contrastive learning to improve generalization under noisy conditions.

### Strengths
1.	The proposed analogical reasoning mechanism effectively incorporates contextual information from a knowledge base to overcome the limitations of noisy support data.

2.	The combination of multi-head self-attention and a large-scale knowledge base results in efficient enhancement of class prototypes.

3.	The inclusion of task-level contrastive learning provides additional regularization, significantly improving model generalization.

### Weaknesses
1.	The details of knowledge base construction and selection for analogical reasoning are insufficient, particularly regarding applicability in different tasks. The paper lacks a clear explanation of how the knowledge base is structured and how specific entries are selected for enhancing class prototypes. It is unclear how the relationships between categories are represented within the knowledge base, and how these relationships are leveraged by the multi-head self-attention mechanism. The paper should provide more details on the specific criteria used to determine which knowledge base entries are relevant for a given task and how this selection process affects the final performance.

2.	While task-level contrastive learning enhances generalization, the computational complexity is high, with no discussion on training time and efficiency. The paper does not provide sufficient information on the computational overhead introduced by the task-level contrastive learning component. Specifically, the paper should include a detailed analysis of the time and memory costs associated with the contrastive learning process, including the construction of positive and negative task pairs and the computation of the contrastive loss. The absence of this analysis makes it difficult to assess the practical feasibility of the proposed approach, especially for large-scale datasets or resource-constrained environments.

3.	Scalability with larger or different types of knowledge bases is not discussed, which may limit the generalizability of the approach. The paper does not explore how the performance of the proposed model is affected by the size and diversity of the knowledge base. It is unclear whether the model can effectively utilize larger knowledge bases or if the performance saturates beyond a certain size. Furthermore, the paper should discuss the potential challenges and limitations of using different types of knowledge bases, such as those with varying levels of granularity or different types of relationships between concepts. The lack of discussion on these aspects limits the understanding of the model's applicability in real-world scenarios.

### Questions
1.	During the construction of the query set using mixup, does the correlation between the sampled image and the combined augmented image affect the model's performance and stability? For instance, do cases where they belong to the same class or are completely unrelated impact the outcome?

2.	Under time constraints, does the computational cost of this construction method lead to a significant performance improvement in the model?

3.	How sensitive is the model's performance to the parameters used in the query set construction method?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a Transformer-based Analogical Reasoning model, TarNFS, designed for robust few-shot learning (FSL) in noisy environments. It leverages analogical reasoning to improve classification by building connections among categories within a semantic knowledge base, like WordNet, and introduces task-level contrastive learning to separate distinct tasks further. The proposed approach is evaluated on MiniImageNet and TieredImageNet, showing improvements over previous FSL methods, particularly under noisy conditions, and demonstrating competitive performance on standard clean data.

### Strengths
- The paper is well-organized, with a logical progression from problem formulation to methodology and experimental evaluation, making it accessible and easy to follow.

- The experiments cover a variety of settings, including different noise levels, ablation studies, and comparisons with several FSL baselines, providing a solid foundation for evaluating the model's effectiveness.

- TarNFS demonstrates advantages in handling noisy data, a challenging aspect of FSL, particularly through its strategy of refining noisy prototypes using analogical knowledge.

### Weaknesses
 - While MiniImageNet and TieredImageNet are commonly used benchmarks, the model’s real-world applicability could be tested on additional datasets, e.g. Meta-dataset.
- The model relies on an existing knowledge base (WordNet), which may limit its applicability in domains lacking such resources or where these resources are incomplete.
- The Transformer-based architecture and contrastive learning process, especially with Bi-LSTM in the task-level contrastive learning, may require considerable computational resources, which are not addressed in terms of efficiency or scalability.
- The model is tailored to the structure of WordNet for analogy-based learning. Adapting this method for domains with different types of semantic structures could present challenges, and further explanation of this adaptation process is warranted.

### Questions
Can the proposed method outperforms the latest Noisy FSL method DETA [1]?

[1] DETA: denoised task-adaptation for few-shot learning, ICCV 2023.

### Soundness
2

### Presentation
3

### Contribution
2
