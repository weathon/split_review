# Scalable Lifelong Multimodal Instruction Tuning via Dynamic Data Selection

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Visual instruction datasets from various distributors are released at different times and often contain a significant number of semantically redundant text-image pairs, depending on their task compositions (\ie, skills) or reference sources. This redundancy greatly limits the efficient deployment of \textbf{lifelong adaptable} multimodal large language models, hindering their ability to refine existing skills and acquire new competencies over time.
To address this, we reframe the problem of Lifelong Instruction Tuning (LiIT) via data selection, where the model automatically selects beneficial samples to learn from earlier and new datasets based on the current state of acquired knowledge in the model. 
Based on empirical analyses that show that selecting the best data subset using a static importance measure is often ineffective for multi-task datasets with evolving distributions, we propose \ours, a new multi-way and adaptive data selection approach that dynamically balances sample efficiency and effectiveness during LiIT. 
We first construct pseudo-skill clusters by grouping gradient-based sample vectors. 
Next, we select the best-performing data selector for each skill cluster from a pool of selector experts, including our newly proposed scoring function, \textit{Image Grounding score}. This data selector samples a subset of the most important samples from each skill cluster for training. To prevent the continuous increase in the size of the dataset pool during LiIT, which would result in excessive computation, we further introduce a cluster-wise permanent data pruning strategy to remove the most semantically redundant samples from each cluster, keeping computational requirements manageable.
We validate the effectiveness and efficiency of \ours{} over a sequence of various multimodal instruction tuning datasets with various tasks, including (Knowledge) VQA, multilingual, grounding, reasoning, language-only, and multi-image comprehension tasks. Training with samples selected by \ours{} alleviates catastrophic forgetting, especially for rare tasks, and promotes forward transfer across the continuum using only a fraction of the original datasets.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This is an interesting article that addresses the issue of forgetting in multimodal large models within multi-task and continual learning scenarios from the perspective of instruction dataset selection and proposes effective strategies. Traditional training methods often lead to the model forgetting previously learned skills when new tasks are introduced. However, the article introduces the LAMP (Lifelong and Adaptive Multi-way Pruning) method, which uses gradient vectors for pseudo-task clustering and combines an entropy-maximization strategy for sample selection, achieving effective sample filtering and diversity balance. LAMP employs semantic redundancy detection and coverage-based sampling strategies to prune the data pool, control its size, and prevent unrestrained data pool expansion, while ensuring the representativeness and diversity of tasks. Moreover, training budgets are allocated reasonably across task clusters, allowing the model to be sufficiently trained on each task, thereby reducing forgetting and enhancing generalization capabilities. Overall, LAMP performs well in multi-task and continual learning environments, ensuring that the model retains previously learned skills when training on new tasks, even with limited computational resources, thus achieving efficient and balanced continual learning.

### Strengths
This article starts from the current situation where the instruction-tuning datasets used in fine-tuning multimodal large models are continuously increasing and points out the redundancy problem among these datasets. It then proposes a solution to address the issue of continual learning, demonstrating significant practical relevance. In the design of the proposed solution, the authors first analyze the problems and limitations of existing methods, then detail how the new solution effectively addresses these issues, showcasing clear research objectives and a logical structure. The narrative of the paper reflects the author’s deep understanding of the field and direction, providing readers with extensive knowledge and unique insights. Moreover, the article verifies the correctness and validity of the proposed solution through extensive experiments, opening up new avenues for future research and demonstrating considerable i

### Weaknesses
Although it is good to see the paper as a whole, there still exist some minor drawbacks in this work.
1.	In Figure 2, the meanings of the axes in subfigure C are unclear, and the explanatory content for subfigure A is insufficient, failing to adequately explain the issue that the figure is intended to illustrate. Specifically, for subfigure A, it is not clear what the different colored regions represent, and how they relate to the concept of forgetting. For subfigure C, the axes lack labels, making it impossible to understand the relationship being depicted. The lack of clarity in these figures hinders the reader's understanding of the core concepts.
2.	The text descriptions in all the images are not very clear and appear somewhat distorted. This makes it difficult to read the labels and annotations within the figures, further impeding the comprehension of the presented data and results.
3.	In the paper, clustering operations on datasets based on gradients and subsequent pruning of redundant data use k-means and pair-wise cosine similarity, respectively. This computational approach likely incurs significant time and space costs in such large-scale instruction datasets. The paper does not adequately address the computational complexity of these operations, especially considering the large scale of instruction datasets used in modern multimodal models. The k-means algorithm, in particular, can be computationally expensive, and the paper should provide more details on how this is managed. Furthermore, the pairwise cosine similarity calculations also scale quadratically with the number of samples, which could pose a significant bottleneck.
4.	During the data selection process, a pool of function tools is used, and the function that produces higher average entropy is ultimately chosen. In this process, combining multiple functions can be considered to achieve more robust data selection. The current approach of selecting only one function based on average entropy might be suboptimal, as different functions could capture different aspects of the data, and a combination could lead to a more diverse and representative selection.

### Questions
please refer to the weakness part

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Lifelong Multimodal Instruction Tuning, which differs from continual Multimodal Instruction Tuning in that the previous datasets are still included in the dataset pool. To effectively select the data at each timestep, the authors propose a framework that adaptively  selects data samples based on their importance and data balance. The experiments show that the method is more effective than baselines.

### Strengths
- The considered lifelong setting is more practical than the traditional continual learning setting for multimodal LLMs, since currently the most important aspect of large models is to use all data available better. 
- The proposed framework considers the key difficulties of data sampling in adapting multimodal LLMs with progressively growing datasets and reasonably tackles the problem with carefully designed pipelines. I find sections 3 and 4 meaningful with rigorous thoughts and experiment analysis.
- The experiments are thorough and clearly show the effectiveness of the proposed framework over the considered baselines.
- The paper is written very well.

### Weaknesses
 - The proposed method, except for the image grounding score, seems not to be specifically designed for multimodal LLMs and can be potentially applied to broader domains like pure LLMs. However, the paper only considers multimodal LLMs which lowers the impact and importance of the paper.

### Questions
the t-SNE visualization has been shown to have high stochasticity across seeds. Have you manually tuned for your method and other baselines throughout the paper?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel approach, LAMP, for optimizing Lifelong Instruction Tuning (LiIT) of Multimodal Large Language Models (MLLMs). Traditional visual instruction datasets, which are frequently redundant and task-specific, hinder MLLMs' ability to continuously adapt and learn new skills effectively. LAMP addresses this by dynamically selecting and pruning data to maximize training efficiency while minimizing computational demands. It groups data into pseudo-skill clusters, applying adaptive selection to prioritize relevant samples for each skill and using a cluster-wise pruning method to reduce redundancies. This approach mitigates catastrophic forgetting, enhances knowledge transfer, and improves performance on rare tasks, all while leveraging only a fraction of the original dataset. LAMP's adaptive tuning demonstrates significant benefits for sustaining long-term model growth in evolving multimodal learning environments.

### Strengths
1. The proposed method mitigates catastrophic forgetting and supports forward transfer, enabling the model to retain skills and adapt to new tasks seamlessly.
2. LAMP’s cluster-wise pruning manages dataset growth by removing redundancies, keeping training scalable and resource-efficient.
3. This paper is well-writing and its organization is logical.

### Weaknesses
1. A primary concern regarding the proposed sequential data structure and the lifelong-based instruction tuning strategy is their practical applicability, as the current MLLMs typically rely on the integration of diverse tasks together for effective multitask training instead of sequential learning. The paper's approach, which processes datasets sequentially, may not align well with the common practice of training on a large, unified dataset encompassing multiple tasks simultaneously. This raises questions about the method's relevance to real-world MLLM training scenarios.
2. The paper mentioned that (lines 301-302) "our proposed multi-way approach can be seamlessly extended with new scoring functions based on users’ needs", however, the proposed method only employs four scoring functions in practice and lacks ablation experiments for additional scoring functions. I suggest the authors conduct related experiments to demonstrate the proposed method’s flexibility and scalability. The absence of experiments exploring a wider range of scoring functions limits the understanding of the method's robustness and adaptability. It is unclear how the performance would be affected by different scoring functions or combinations thereof.
3. In Tab.2, the effectiveness of the random pruning strategy is notably highlighted. The computational costs and complexities associated with other sophisticated pruning techniques do not appear to correspond proportionately to the performance improvements achieved. This raises questions regarding the efficiency of the proposed pruning methods in comparison to simpler alternatives. The marginal gains achieved by the proposed method over random pruning may not justify the added complexity and computational overhead, especially considering the practical implications of large-scale model training.
4. In Tab.2, although LITE-LAMP utilizes 4 times less training data (25k vs. 100k), its relative improvement dropped significantly when compared to LAMP, i.e., 99.7 vs. 109.7. This suggests that the performance gains of the proposed method are highly sensitive to the amount of training data, and the benefits of the method may diminish when applied to smaller datasets. The observed drop in relative improvement for LITE-LAMP raises concerns about the method's scalability and its effectiveness in low-resource scenarios.

### Questions
Please focus on Weaknesses, and I encourage the authors to provide further discussion and clarification on these points.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new scenario of lifelong instruction tuning, where Multimodal Large Language Models (MLLM) continuously learns from new datasets that include both new and redundant data samples. They then propose LAMP, a adaptive data selection approach designed for this context. The authors claims that the proposed method can select beneficial samples to adapt the current model's knowledge to the continuously changing dataset distribution.

### Strengths
- The setting of lifelong instruction tuning introduced in the paper is practical in real-world applications.
- The paper is overall well organized and easy to follow.
- The proposed method achieves convincing results in experiments, and comprehensive ablation studies are provided to validate the effectiveness of individual components.

### Weaknesses
 - The method does not appear very novel to me, as both gradient-based clustering and ensemble scoring functions for data selection have been explored in previous works.
- In evaluation, the paper focuses on tasks with short answers but omits open-ended visual chat, where multimodal large language models (MLLMs) generate long responses. However, visual chat is essential for assessing the comprehensive capabilities of MLLMs.
- Compared to random pruning, which already serves as a strong baseline, the proposed method (including the LITE or efficient version) incurs significantly higher computational and time costs, and no efficiency analysis on the computational cost is provided.
- Clarification Issues. In Table 2, the authors do not clearly explain what "data size at *t*" refers to.

### Questions
- How is "accuracy" measured on LLaVA-Bench?
- In table 2, why does multi-task learning performs worse than random pruning which simply uses fewer data (e.g. accuracy 46.1% VS 47.2%) ? Can pruning more data lead to better result?
- Can you provide numerical comparisons on the computation cost of the proposed method against the random pruning baseline? Additionally, how does the computation cost of data selection compare with the training cost at step $t$?

### Soundness
2

### Presentation
3

### Contribution
3
