# Efficient Expert Pruning for Sparse Mixture-of-Experts Language Models: Enhancing Performance and Reducing Inference Costs

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
The rapid advancement of large language models (LLMs) has led to architectures with billions to trillions of parameters, posing significant deployment challenges due to their substantial demands on memory, processing power, and energy consumption. Sparse Mixture-of-Experts (SMoE) architectures have emerged as a solution, activating only a subset of parameters per token, thereby achieving faster inference while maintaining performance. However, SMoE models still face limitations in broader deployment due to their large parameter counts and significant GPU memory requirements. 
In this work, we introduce a gradient-free evolutionary strategy named \underline Efficient \underline Expert \underline{P}runing (EEP) to enhance the pruning of experts in SMoE models. Specifically, EEP searches the pruning pattern and use expert merging as an memory-efficient way of fine-tuning the pruned model. EEP relies solely on model inference (i.e., no gradient computation) and achieves greater sparsity while maintaining or even improving performance on downstream tasks. EEP can be used to reduce both the total number of experts (thus saving GPU memory) and the number of active experts (thus accelerating inference).
For example, we demonstrate that pruning up to 75\% of experts in Mixtral $8\times7$B-Instruct results in a substantial reduction in parameters with minimal performance loss. 
Remarkably, we observe improved performance on certain tasks, such as a significant increase in accuracy on the SQuAD dataset (from 53.4\% to 75.4\%), when pruning half of the experts. With these results, EEP not only
lowers the barrier to deploying SMoE models,
but also challenges the conventional understanding of model pruning by showing that fewer experts can lead to better task-specific performance without any fine-tuning.
\footnotetext{Correspondence to Yu Wang <yu-wang@mail.tsinghua.edu.cn>, Zinan Lin <zinanlin@microsoft.com>, Xuefei Ning <foxdoraame@gmail.com>.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper works on the topic of pruning experts in SMoE models. They propose a gradient-free evolutionary strategy named EEP. In EEP, there are two matrices named expert merging matrix and experts mapping matrix, used to search for pruning configurations. The goal is to achieve sparsity while reaching good performance on downstream tasks. The paper shows the performance of the proposed method on four different model sizes and uses more than 10 datasets.

### Strengths
SMoE can achieve faster inference while maintaining performance. To search for the subset of experts, this paper proposes a gradient-free approach based on evolutionary strategy. By using two phases expert pruning and expert merging, the method achieves high sparsity.

### Weaknesses
1. While the method is gradient-free, it does not necessarily imply a low search cost. The evolutionary strategy used requires multiple iterations and epochs, and the search cost is highly dependent on the settings for iterations, epochs, and the data size used for calculating the validation metric. To better illustrate the efficiency of the method, I suggest the authors provide concrete runtime numbers for different dataset sizes, comparing them to gradient-based alternatives, including both search time and the time to achieve comparable performance after pruning. This would help clarify whether the method can be effectively extended to more complex datasets. Furthermore, the authors should clarify if the search cost is amortized over multiple pruning tasks or if it is a one-time cost per model.

2. The method heavily relies on evaluation results from selected data to conduct the search process. While Table 15 shows in-distribution results for two dataset sizes, it is unclear whether similar trends hold for out-of-distribution cases. A comprehensive study on the influence of dataset size is recommended. Specifically, it would be beneficial to include a plot showing the performance vs. dataset size across a range of sizes for both in-distribution and out-of-distribution settings. Additionally, the authors should explain the counterintuitive result where a smaller dataset size provides better performance than a larger dataset size, and whether this is a consistent trend or an anomaly due to the specific datasets used.

3. For out-of-distribution evaluation, 7 datasets from MMLU are used for validation. It would be helpful to know whether the number of validation datasets affects performance. To address this, I recommend conducting an ablation study that varies the number of validation datasets (e.g., from 1 to 7) and reporting how this impacts performance. This would offer insight into the method’s robustness in extreme cases where only a single dataset is available for validation, and whether the method is sensitive to the diversity of the validation set.

4. The writing of the paper could be improved, as the key ideas are not easy to follow. A significant portion of the text is devoted to background and preliminaries, such as the description of the self-attention mechanism in Section 3, which is well-known and could be condensed or moved to the appendix. This would create more space to emphasize the main algorithm and core contributions in the main paper. I suggest reorganizing the structure to focus on the core algorithm earlier in the text for better clarity and accessibility. Specifically, the paper could benefit from a clearer explanation of the expert merging and mapping matrices, and how they are updated during the evolutionary search.

### Questions
1. Why is the full model performance significantly higher in this paper compared to the NAEE paper? For example, in Table 2, the full model (Mixtral 8×7B-Instruct) achieves 85.8 on ARC-c with 8 experts, while in the NAEE paper's Table 1, the performance is only 62.20.

2. Can the proposed method still work for out-of-distribution cases when there is only one dataset available for validation?

3. What does the performance vs. dataset size curve look like during the search process? What is the rationale for choosing specific dataset sizes for validation?

4. How is the performance of the proposed method compared to dynamic MoE methods?

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
This paper introduces Efficient Expert Pruning (EEP), a gradient-free evolutionary strategy for optimizing Sparse Mixture-of-Experts (SMoE) language models. The work addresses the challenge of reducing model size and computation costs while maintaining performance. The authors propose a two-phase approach combining expert pruning and expert merging, which can be executed using only model inference capabilities without requiring gradient computation or extensive GPU resources. The method is implemented through router mapping and expert merging matrices, enabling evolutionary search for optimal pruning configurations.

### Strengths
1. The paper is exceptionally well-written and organized, with comprehensive experimental validation across multiple model scales and diverse datasets. The methodology is clearly presented with thorough ablation studies and reproducible code.
2. The proposed two-phase EEP framework presents a novel and effective paradigm for model compression. The authors provide insightful analysis of router network behavior that justifies their approach.
3. The method achieves remarkable results while only requiring inference capabilities, with pruned models sometimes even outperforming the original uncompressed models.

### Weaknesses
1. The analysis of why performance sometimes improves after pruning in Sec. 5.6. remains somewhat speculative, lacking rigorous theoretical foundations and comprehensive empirical validation. The discussion does not delve into the specific mechanisms by which pruning alters the router network's behavior, nor does it provide a clear explanation of why certain pruning configurations lead to better performance. The analysis would benefit from a more detailed exploration of the router's decision-making process and how pruning affects the activation patterns of different experts. Furthermore, the paper lacks a theoretical framework to explain the observed phenomena, relying primarily on empirical observations.
2. The performance gap between global setting and task-specific setting in OOD experiments suggests that EEP's impressive results might be more dependent on task-specific optimization than claimed, potentially limiting its general applicability across different tasks. The paper does not adequately address the potential for overfitting to the specific tasks used during the evolutionary search. The fact that performance degrades significantly in out-of-distribution scenarios raises concerns about the robustness of the method and its ability to generalize to unseen tasks. A more thorough investigation of the method's behavior across a wider range of tasks and datasets is needed to fully assess its general applicability.
3. The search process of EEP is computationally expensive and time-consuming, particularly for large datasets. The paper does not address this efficiency bottleneck. While the paper mentions that the method can be applied using only inference capabilities, the computational cost of the evolutionary search itself is not sufficiently discussed. The paper should provide a more detailed analysis of the computational complexity of the search algorithm and explore potential strategies for reducing the search time, such as using more efficient search algorithms or employing parallelization techniques.

### Questions
Could the authors elaborate on how the choice of group numbers and search iterations affects the final performance? A more systematic analysis of these hyperparameters would be valuable for implementation.

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
2

### Summary
This paper addresses the challenge of pruning in sparse mixture of experts (SMoE) models. The authors propose a gradient-free evolutionary strategy called Efficient Expert Pruning (EEP) to improve the pruning process for experts within these models. Experimental results on diverse models and datasets demonstrate the effectiveness of this approach.

### Strengths
(1) The writing is clear and easy to follow.  

(2) The proposed method is interesting, suggesting that evolutionary strategies can effectively optimize parameter combinations for model pruning.   

(3) The insights presented are valuable, demonstrating that MoE models contain redundancy and hold significant potential for pruning while maintaining performance and improving efficiency.

### Weaknesses
 (1) Lack of Reliable Evaluations: I find it puzzling that Mixtral-8x22B's average performance improves despite being pruned from 8 experts down to 2. This raises questions about the robustness of the evaluation methods, especially given the relatively small datasets used in this study. The use of small datasets, particularly for complex models like Mixtral, makes it difficult to generalize the findings. Furthermore, the fact that a pruned model outperforms the full model is counterintuitive and warrants further investigation into the evaluation protocol. In contrast, NAEE—a key baseline—evaluates on the comprehensive MMLU dataset, which could serve as a more reliable benchmark.

(2) In Table 6, even after pruning from 8 experts down to 4 and then 2, the speedup is small. What factors might explain this limited increase in speed? The lack of significant speedup despite substantial expert reduction suggests that the computational bottleneck may not be solely determined by the number of experts. This raises concerns about the practical efficiency gains of the proposed method.

(3) The method’s efficiency is largely limited by its computational demands and the dataset used. The pruning dataset is relatively small, yet the process still requires significant time—up to several hours. This high computational cost, even with limited data, makes the method less practical for large-scale applications. The long pruning time, coupled with the small dataset size, suggests that the method may not scale well to more complex scenarios.

(4) Are the training and evaluation samples drawn from the same distribution? This could make sense as a task-agnostic pruning approach. However, given the long pruning time even with limited samples, why not fine-tune a roughly pruned model instead?

### Questions
see weakness

### Soundness
2

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
3

### Summary
This paper proposes Efficient Expert Pruning (EEP), a gradient-free evolutionary strategy to optimize the pruning and merging of experts within Sparse Mixture-of-Experts (SMoE) models. EEP aims to enhance performance while saving GPU memory and reducing inference costs by minimizing both the total number of experts and the number of active experts during inference. This is achieved through an evolutionary search process that optimizes two matrices: a router mapping matrix for expert selection and an expert merging matrix to retain pruned experts' knowledge. EEP is evaluated across various downstream tasks and shows considerable improvement over baselines in terms of memory efficiency, inference speed, and overall performance.

### Strengths
1. This paper is well-written, well-organized including problem formulation, methodological exposition, and experimental setup, making it accessible to readers with a background in the field. Besides, the implementation details and code are provided for reproducing.
2. The EEP method employs a gradient-free evolutionary search strategy for expert pruning and merging in the SMoE model, which is a relatively novel method.
3. This paper conducts extensive experiments on multiple datasets and models to validate the effectiveness of the method, demonstrating significant improvements over existing baselines, which greatly enhances the practicality of SMoE pruning.

### Weaknesses
1. In the NAEE [1] method, the authors use the C4 dataset as the calibration dataset and evaluate the zero-shot accuracy of the pruned model, which is a common experimental setup in the field of LLM compression. The authors should conduct similar experiments and provide data in this regard to allow for a more comprehensive assessment of the effectiveness of the EEP method. Specifically, it would be beneficial to see how EEP performs when evaluated on a held-out dataset after being calibrated on C4, as this is a standard benchmark for evaluating generalization in pruning methods.
2. I am concerned about the search cost of EEP. The total time spent on EEP for each dataset is several hours, and this is just for the smallest Mixtral 8x7B Instruct model. For larger datasets and larger models, EEP will take even longer, which is often unacceptable. The practicality of the method is limited by this high computational overhead, especially when considering the need to retrain or fine-tune the model after pruning. The paper should include a more detailed analysis of the time complexity of the evolutionary search process and discuss potential strategies to mitigate this cost.
3. The out-of-distribution accuracy of EEP is much lower than that of NAEE [1] on many datasets (Tables 5, 12 and 13), so I am concerned about the generalization ability of EEP. This raises questions about the robustness of the method when applied to datasets that differ significantly from the training data used for the evolutionary search. It would be valuable to explore the reasons behind this performance gap and to investigate whether the method is prone to overfitting to the training distribution.
4. Some notations are confusing.
    - The authors use bold uppercase symbols to represent matrices. In line 91, $W_{RM}$ and $W_{EM}$ should be bolded to ensure consistency with the notation used in Section 4.2.
    - The symbol $\boldsymbol{W}_G$ in Equation 2 is not explained. I suspect it refers to the router network $\boldsymbol{W}_R$ in line 179.

### Questions
1. In Section 5.1, the authors state that the dataset is randomly divided into training and test set, with the training set used for evolutionary search and the test set used for evaluation. How exactly is this division performed? Table 14 seems to contain some data on the trainset size, but it is not comprehensive enough. 
2. The authors used 50 MMLU datasets as the training set and 7 as the test set, utilizing a large number of datasets as the training set to test accuracy on out-of-distribution datasets. I would like to know the total search time EEP took in this case, and whether using fewer training sets would impact the out-of-distribution accuracy.
3. How does the accuracy of the EEP pruned model obtained from one dataset perform on other datasets? For example, if BoolQ is used as the training set, what is the accuracy of the pruned model on other validation sets?

### Soundness
3

### Presentation
3

### Contribution
3
