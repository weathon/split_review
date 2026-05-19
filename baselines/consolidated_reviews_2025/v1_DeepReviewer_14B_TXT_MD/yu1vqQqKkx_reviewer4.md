### Summary

The paper introduces LICO, a novel approach that leverages Large Language Models (LLMs) for black-box optimization, specifically in the molecular domain. The authors address the limitations of existing methods that rely on natural language for optimization, which are often constrained by the scarcity of domain-specific data and the difficulty of expressing complex problems in text. LICO is designed to generalize to unseen molecular properties through in-context prompting, without requiring verbose textual descriptions. The model is trained on a diverse set of intrinsic and synthetically generated functions, enabling it to perform well on a range of molecular optimization tasks. The authors demonstrate LICO's effectiveness on the Practical Molecular Optimization (PMO) benchmark, where it achieves state-of-the-art performance across 21 optimization objectives.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The experimental results are sufficient to prove the claim. The ablation study is helpful to understand the method.
3. The method can be extended to other black-box optimization problems, which is very interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The training method needs more clarification. I suggest reorganizing the section by splitting Sec. 4.2 into two separate sections, where one section focuses on the training method and the other section focuses on the semi-synthetic training.
2. The novelty of this method is limited. The model is an extension of LLMs with additional embedding and prediction layers. The only novel part is the application of LLMs in molecular optimization. However, there are many existing methods that have been proved to be effective in molecular optimization. The performance is only comparable to these methods (e.g., GP BO).
3. The importance of the Tanimoto kernel is unclear. Since the semi-synthetic training method is a key contribution, it is important to understand the importance of the Tanimoto kernel. There are limited discussions about the Tanimoto kernel in the paper, and no ablation study is provided to show how the Tanimoto kernel affects the performance.
4. The comparison with existing methods is not fair. LICO leverages the prior knowledge learned from LLM pretraining, whereas other methods like GP BO do not have this prior knowledge. To make a fair comparison, I suggest comparing LICO with other methods that also leverage LLMs.

### Suggestions

The paper would benefit from a more detailed explanation of the training process, particularly regarding the integration of semi-synthetic data. The current description lacks clarity on how the intrinsic and synthetic functions are combined and used during training. It would be beneficial to separate the general training methodology from the specifics of the semi-synthetic approach, as suggested. This would allow for a clearer understanding of the core training process and the specific contributions of the semi-synthetic data. Furthermore, the paper should elaborate on the choice of loss function and optimization algorithm used during training, as well as the specific hyperparameters and their impact on the final performance. A more detailed explanation of the data generation process for both intrinsic and synthetic functions would also be valuable, including the specific molecular fingerprints used and how they are encoded.

To address the concerns about novelty, the authors should provide a more thorough comparison with existing methods, particularly those that also leverage LLMs. While the application of LLMs to molecular optimization is interesting, the core architecture of LICO appears to be an incremental extension of existing LLMs. The paper should include a more detailed analysis of how the LLM's pre-trained knowledge is leveraged in the context of molecular optimization. For instance, are there specific patterns or representations learned during pre-training that are particularly useful for this task? A comparison with a randomly initialized model of similar architecture would be beneficial to isolate the impact of pre-training. Additionally, the paper should discuss the limitations of the approach, such as the computational cost of using LLMs and the potential for overfitting to the training data. A more thorough discussion of these aspects would provide a more balanced view of the method's contributions.

Finally, the paper needs to provide a more in-depth analysis of the Tanimoto kernel's role in the semi-synthetic training process. While the Tanimoto kernel is a common choice for molecular similarity, its specific impact on the performance of LICO is not well understood. An ablation study comparing the Tanimoto kernel with other kernels, such as Gaussian kernels or random kernels, is essential to demonstrate its importance. This study should not only focus on the final performance but also on the training dynamics and the generalization capabilities of the model. Furthermore, the paper should discuss the theoretical properties of the Tanimoto kernel that make it suitable for this task. For example, how does the Tanimoto kernel capture the structural similarities between molecules, and how does this relate to the optimization process? A more detailed analysis of these aspects would significantly strengthen the paper's claims.

### Questions

1. In Sec. 4.2, the authors propose to train the model on synthetic functions generated by Gaussian Processes with a Tanimoto kernel. What is the importance of the Tanimoto kernel? How does the Tanimoto kernel affect the performance?
2. How to generate the synthetic functions? Are the synthetic functions related to the objective functions of the PMO benchmark?

### Rating

6

### Confidence

3

**********
