### Summary

This paper proposes a new regularization technique for RNN model to mitigate the numerical overflow issue when training with FHE, which results in a more FHE-evaluation efficient RNN model with high accuracy.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

The technical contributions are clear and the numerical results on MNIST are quite impressive (90.82% top-1 accuracy). The authors compare the proposed method with the baseline, and the improvement is significant.

### Weaknesses

#### Some Related Works


#### comment

1. The evaluation is only performed on the MNIST dataset, which is very simple. It is unclear whether the method can be generalized to larger and more complicated datasets like CIFAR-100 or ImageNet. The MNIST dataset's low dimensionality and simple structure make it an inadequate benchmark for assessing the robustness of the proposed regularization technique, particularly in the context of FHE. The numerical overflow issues that arise with FHE may be significantly exacerbated by the higher dimensionality and more complex feature distributions found in more realistic datasets. Therefore, the lack of evaluation on more challenging datasets raises serious concerns about the practical applicability of the proposed method.
2. The presentation of this paper is poor. The paper does not clearly explain why the overflow mitigation technique of the proposed method works. The paper lacks a clear explanation of the underlying mechanisms that cause numerical overflow in FHE-based RNN training and how the proposed regularization technique addresses these issues. Without a detailed explanation of the interaction between the regularization and the FHE operations, it is difficult to assess the validity and generalizability of the approach. The paper should provide a more rigorous analysis of the proposed method's effect on the distribution of intermediate values during FHE computation.
3. The paper should have more competition. There are only 3 prior works, where two of them are outdated. The field of FHE has been actively developing in recent years. There should be more research works on FHE + RNN. The lack of comparison with recent state-of-the-art methods in FHE-based RNNs makes it difficult to contextualize the contribution of this work. The paper should include a more comprehensive review of the existing literature and provide a more detailed comparison with the most relevant prior works.

### Suggestions

The authors should significantly expand their experimental evaluation to include more complex and higher-dimensional datasets. Specifically, they should consider evaluating their method on datasets such as CIFAR-100 or ImageNet, which are commonly used in machine learning research. These datasets would provide a more rigorous test of the proposed regularization technique's ability to mitigate numerical overflow issues in FHE-based RNN training. Furthermore, the authors should provide a detailed analysis of the performance of their method on these datasets, including accuracy, latency, and other relevant metrics. This would allow for a more thorough assessment of the practical applicability of the proposed method.

The paper needs a much clearer and more detailed explanation of the proposed regularization technique. The authors should provide a step-by-step explanation of how the regularization term is derived and how it interacts with the FHE operations. This explanation should include a rigorous mathematical analysis of the proposed method's effect on the distribution of intermediate values during FHE computation. The authors should also provide a clear explanation of why the proposed method is effective in mitigating numerical overflow issues. This explanation should be supported by empirical evidence and theoretical analysis. The paper should also include a discussion of the limitations of the proposed method and potential areas for future research.

The authors should conduct a more comprehensive literature review and compare their method with the most relevant prior works in FHE-based RNNs. This comparison should include a detailed analysis of the strengths and weaknesses of each method, as well as a discussion of the differences in their approaches. The authors should also provide a clear explanation of how their method improves upon the existing state-of-the-art. This would allow for a more accurate assessment of the contribution of this work. The authors should also consider comparing their method with other approaches to FHE-based machine learning, even if they do not directly address RNNs, to provide a broader context for their work.

### Questions

1. Why is the MNIST dataset not reshaped as $28 \times 28$ when input to the RNN model in Figure 3? Is it a typo?
2. Why is the dropout layer necessary? If you are using the dropout at test time, you should use the scaled weights during training.
3. What is the "FF" layer in Figure 3?
4. The abstract is too difficult to understand.

### Rating

3

### Confidence

4

**********
