### Summary

The paper proposes two techniques to improve the performance of differentially private training of transformers. The first technique, Phantom Clipping, is an efficient way to perform per-sample gradient clipping for transformers. The second technique, Re-Attention, is a way to correct for the bias in attention scores that is introduced by the noise that is added during DP-SGD. The authors evaluate their techniques on two real-world datasets and show that they improve the performance of DP-SGD.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes two novel techniques for improving the performance of DP-SGD on transformers.
- The techniques are well-motivated and have a clear theoretical basis.
- The paper evaluates the techniques on two real-world datasets and shows that they improve the performance of DP-SGD.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a theoretical analysis of the privacy guarantees of the proposed techniques.
- The paper does not compare the proposed techniques to other state-of-the-art methods for differentially private training of transformers.

### Suggestions

The paper introduces Phantom Clipping and Re-Attention as methods to improve differentially private training of transformers. While the empirical results are promising, a more rigorous theoretical analysis of the privacy guarantees is needed. Specifically, the paper should provide a formal proof that the proposed techniques satisfy differential privacy under the composition theorem. This would involve analyzing how the noise added by Phantom Clipping and Re-Attention affects the overall privacy budget. Furthermore, it would be beneficial to explore the relationship between the clipping threshold, the noise variance, and the resulting privacy guarantees. A clear understanding of these relationships is crucial for practitioners to use the proposed methods effectively and to ensure that the privacy guarantees are met in practice. The analysis should also consider the impact of the Re-Attention mechanism on the sensitivity of the gradient, as this could affect the overall privacy budget.

In addition to the theoretical analysis, the paper should include a more comprehensive comparison to existing state-of-the-art methods for differentially private training of transformers. While the paper mentions that the proposed techniques improve upon DP-SGD, it does not provide a detailed comparison to other methods, such as those based on objective perturbation or output perturbation. A thorough comparison should include a discussion of the trade-offs between privacy, accuracy, and computational cost. For example, it would be useful to compare the proposed techniques to methods that use adaptive clipping or noise scaling. Furthermore, the comparison should include a discussion of the practical challenges of implementing each method, such as the need for hyperparameter tuning or the computational overhead of the different techniques. This would help readers understand the strengths and weaknesses of the proposed methods in relation to the existing literature.

Finally, the paper should provide more details on the implementation of the proposed techniques. For example, it would be helpful to include a pseudocode description of the Phantom Clipping and Re-Attention algorithms. This would make it easier for other researchers to reproduce the results and to build upon the proposed methods. The paper should also discuss the computational cost of the proposed techniques and how they scale with the size of the model and the dataset. This is important for practitioners who need to consider the computational resources required to use the proposed methods. Furthermore, the paper should provide more details on the hyperparameter settings used in the experiments, such as the learning rate, batch size, and noise variance. This would help readers understand the sensitivity of the results to these parameters and to reproduce the results.

### Questions

- How does the performance of the proposed techniques compare to other state-of-the-art methods for differentially private training of transformers?
- What are the practical challenges of implementing the proposed techniques?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
