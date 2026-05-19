### Summary

The paper introduces DPFormer, a novel approach for training Transformer models with differential privacy on long-tailed data. It addresses two main challenges: the computational overhead of per-sample gradient clipping and unintentional attention distraction. The proposed solutions include Phantom Clipping and a Re-Attention Mechanism. Theoretical analysis and empirical results on real-world datasets demonstrate the effectiveness and efficiency of DPFormer.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow. The introduction provides a clear overview of the problem and the proposed solution.
2. The paper provides a thorough theoretical analysis of the proposed method, including proofs and justifications for the effectiveness of Phantom Clipping and the Re-Attention Mechanism.

### Weaknesses

#### Some Related Works

[1] Privacy-Aware Self-Supervised Learning
[2] Differentially Private Decoupled Graph Convolutional Networks
[3] Scaling Up Differentially Private Deep Learning with Gradient Accumulation

#### comment

1. The paper does not adequately compare its approach with existing methods for differentially private training of Transformers. A comparison with methods like those in [1] and [2] would be beneficial. Specifically, the paper lacks a detailed comparison with differentially private fine-tuning of pre-trained language models, which is a relevant and practical approach. The absence of such a comparison makes it difficult to assess the practical advantages of the proposed method over simply fine-tuning a pre-trained model with differential privacy.
2. The paper does not discuss the potential of applying Phantom Clipping to other models beyond Transformers. It would be interesting to know if this technique could be generalized to improve the efficiency of differentially private training for other architectures. For example, it is unclear if the specific structure of the Transformer is essential for Phantom Clipping to work, or if it could be applied to simpler sequence models or even non-sequence models.
3. The paper does not provide a detailed analysis of the computational overhead of the Re-Attention Mechanism. While the paper claims efficiency, a more rigorous analysis of the computational cost, including memory usage and runtime, would be valuable. It is not clear how the additional computations for the Re-Attention Mechanism scale with sequence length and model size, and whether this overhead is negligible compared to the overall training time.
4. The paper does not discuss the limitations of the proposed approach. For example, how does the performance of DPFormer vary with different privacy budgets? Are there any specific types of data or tasks where DPFormer is not effective? The paper should also discuss the sensitivity of the method to hyperparameter settings and the potential for performance degradation under very strict privacy constraints.

### Suggestions

The paper should include a more thorough comparison with existing differentially private fine-tuning methods for pre-trained language models. This comparison should not only focus on the final performance but also on the computational cost and the number of training steps required to achieve a certain level of performance. It would be beneficial to include a table that compares the proposed method with fine-tuning approaches in terms of accuracy, training time, and privacy guarantees for a few benchmark datasets. This would help to clarify the practical advantages and disadvantages of the proposed method. Furthermore, the paper should discuss the potential for combining the proposed method with pre-trained models, as this could lead to improved performance and reduced training time. The authors should also consider evaluating their method on a wider range of datasets, including those with different characteristics, to better understand the generalizability of their approach.

The paper should provide a more detailed analysis of the computational overhead of the Re-Attention Mechanism. This analysis should include a breakdown of the computational cost of each step in the mechanism, as well as an analysis of how the cost scales with sequence length and model size. It would be helpful to include a plot that shows the runtime of the Re-Attention Mechanism as a function of sequence length, and to compare this runtime with the runtime of the main Transformer computation. The authors should also discuss the memory usage of the Re-Attention Mechanism, and whether it introduces any additional memory overhead compared to standard attention mechanisms. This analysis should be performed on different hardware configurations to provide a more comprehensive understanding of the computational cost.

The paper should also include a more detailed discussion of the limitations of the proposed approach. This discussion should include an analysis of how the performance of DPFormer varies with different privacy budgets, as well as an analysis of the types of data or tasks where DPFormer is not effective. The authors should also discuss the sensitivity of the method to hyperparameter settings, and provide guidelines for choosing appropriate hyperparameter values. It would be beneficial to include a plot that shows the performance of DPFormer as a function of the privacy budget, and to discuss the trade-off between privacy and accuracy. The authors should also discuss the potential for performance degradation under very strict privacy constraints, and provide recommendations for mitigating this degradation.

### Questions

1. Can the authors provide more details on how Phantom Clipping is implemented in practice? Are there any specific hardware or software requirements for using this technique?
2. How does the Re-Attention Mechanism affect the interpretability of the Transformer model? Does it make it more difficult to understand which parts of the input sequence are most important for the model's predictions?
3. Can the authors provide more details on the datasets used in the experiments? What are the characteristics of these datasets, and how do they relate to real-world applications?
4. How does the performance of DPFormer compare to other differentially private training methods for Transformers? Are there any specific scenarios where DPFormer is particularly effective or ineffective?
5. Can the authors provide more details on the hyperparameter settings used in the experiments? How sensitive is the performance of DPFormer to the choice of hyperparameters?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
