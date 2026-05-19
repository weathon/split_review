### Summary

This paper proposes two methods to train Transformers with differential privacy. The first method, called "phantom clipping", is an efficient way to clip gradients in Transformers with parameter sharing. The second method, called "re-attention", is a way to mitigate the attention distraction phenomenon. Experiments on two datasets show the effectiveness of the proposed methods.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed methods are interesting and novel.
3. The experiments are conducted on two real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a theoretical analysis of the proposed methods. Specifically, there is no formal privacy analysis demonstrating that the proposed methods satisfy differential privacy. The paper should include a rigorous proof that the proposed methods, particularly the re-attention mechanism, do not introduce additional privacy risks beyond those inherent in the base DP-SGD algorithm. This analysis should consider the impact of the clipping and re-attention operations on the overall privacy budget.
2. The paper lacks a thorough discussion of the limitations of the proposed methods. For example, the paper does not discuss the potential impact of the proposed methods on the convergence rate of the training process. It would be beneficial to analyze how the phantom clipping and re-attention mechanisms affect the optimization landscape and whether they introduce any instability or slow convergence. Additionally, the paper should discuss the computational overhead of the proposed methods compared to standard DP-SGD. While the paper claims efficiency for phantom clipping, a detailed analysis of the computational cost of re-attention is missing.
3. The experiments are conducted on only two datasets. It would be beneficial to evaluate the proposed methods on a wider range of datasets to demonstrate their generalizability. The current datasets may not be representative of all possible applications of the proposed methods. For example, the paper should consider datasets with different characteristics, such as varying sequence lengths, vocabulary sizes, and data distributions. Furthermore, the paper should include a more detailed analysis of the performance of the proposed methods under different privacy budgets and model architectures.

### Suggestions

To address the lack of theoretical analysis, the authors should provide a formal proof that their proposed methods satisfy differential privacy. This proof should explicitly show how the clipping and re-attention mechanisms interact with the noise addition process to maintain the desired privacy guarantees. The analysis should consider the composition theorem to ensure that the privacy budget is not exceeded after multiple iterations. Furthermore, the authors should analyze the sensitivity of the clipping operation and the re-attention mechanism to changes in the input data. This analysis should demonstrate that the proposed methods do not introduce additional privacy risks beyond those inherent in the base DP-SGD algorithm. The proof should also consider the impact of the parameter sharing in Transformers on the overall privacy guarantees.

To address the lack of discussion on limitations, the authors should provide a more detailed analysis of the convergence behavior of the proposed methods. This analysis should investigate how the phantom clipping and re-attention mechanisms affect the optimization landscape and whether they introduce any instability or slow convergence. The authors should also analyze the computational overhead of the proposed methods compared to standard DP-SGD. This analysis should consider the time complexity of the phantom clipping and re-attention mechanisms and provide a detailed comparison with the computational cost of DP-SGD. The authors should also discuss the potential impact of the proposed methods on the model's generalization performance. This analysis should consider the trade-off between privacy and accuracy and provide insights into the conditions under which the proposed methods are most effective.

To address the limited experimental evaluation, the authors should conduct experiments on a wider range of datasets to demonstrate the generalizability of their proposed methods. The datasets should have different characteristics, such as varying sequence lengths, vocabulary sizes, and data distributions. The authors should also include a more detailed analysis of the performance of the proposed methods under different privacy budgets and model architectures. This analysis should consider the trade-off between privacy and accuracy and provide insights into the conditions under which the proposed methods are most effective. The authors should also compare the performance of their proposed methods with other state-of-the-art DP methods for Transformers. This comparison should consider both privacy and accuracy metrics and provide a comprehensive evaluation of the proposed methods.

### Questions

1. What is the privacy analysis of the proposed methods? Specifically, how do the proposed methods satisfy differential privacy?
2. What are the limitations of the proposed methods? For example, how do the proposed methods affect the convergence rate of the training process?
3. How does the proposed method perform on other datasets?

### Rating

5

### Confidence

4

**********
