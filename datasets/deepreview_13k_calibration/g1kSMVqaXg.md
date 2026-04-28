# Dynamic Influence Tracker: Estimating Sample Influence in SGD-Trained Models across Arbitrary Time Windows

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 8, 3

## Abstract
Understanding how training samples affect models improves model interpretability, optimization strategies, and anomaly detection. However, existing methods for estimating sample influence provide only static assessments, rely on restrictive assumptions, and require high computational costs. 
	We propose Dynamic Influence Tracker (DIT), a novel method to estimate time-varying sample influence in models trained with Stochastic Gradient Descent (SGD). DIT enables fine-grained analysis of sample influence within arbitrary time windows during training through a two-phase algorithm. The training phase efficiently captures and stores necessary information about the SGD trajectory, while the inference phase computes the influence of samples on the model within a specified time window. We provide a theoretical error bound for our estimator without assuming convexity, showing its reliability across various learning scenarios. Our experimental results reveal the evolution of sample influence throughout the training process, enhancing understanding of learning dynamics. We show DIT's effectiveness in improving model performance through anomalous sample detection and its potential for advancing curriculum learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce the Dynamic Influence Tracker (DIT), a novel approach for estimating the influence of individual training samples within specific time windows in models trained via stochastic gradient descent (SGD). Unlike traditional methods, which provide static influence estimates, DIT dynamically tracks how the influence of each sample varies throughout training. The method comprises a two-phase algorithm: a training phase that stores information about the SGD process and an inference phase that computes the influence within a specified window. Experimental results across various datasets and models demonstrate DIT’s advantages in both accuracy and robustness over existing methods.

### Strengths
1. DIT addresses limitations in current methods by providing dynamic estimates, which allow for a more nuanced understanding of sample influence as training progresses. The authors also provide theoretical guarantees for the error bounds, ensuring the model is reliable, even in non-convex landscapes.

2. The experiments cover diverse datasets and various model architectures. The results demonstrate the advantages of DIT over existing methods in terms of accuracy and robustness.

3. DIT reduces computational overhead by using Hessian-vector approximations instead of directly computing or storing the Hessian, making it feasible for large-scale models and datasets.

### Weaknesses
1. It seems that the proposed method can only deal with models trained with SGD. Considering that many models are trained with more complex optimization methods such as Adam, the application of the proposed method seems somewhat limited.

2. It’s unclear whether the DIT is sensitive to hyperparameters, especially the learning rate and batch size, which can vary widely in real-world settings. Further analysis of these factors would strengthen the applicability of the method.

3. The error bound analysis relies on many assumptions (A1-A7) that look strong and may not hold in practice, such as the behavior of Hessians in deep networks. Specifically, the assumption of Lipschitz continuity of the gradient and the boundedness of the Hessian might not be realistic for highly non-convex loss landscapes common in deep learning.

4. It seems that the space and time complexity of the proposed method could still be challenging for very large-scale datasets and deep models. While the method avoids full Hessian computation, the iterative Hessian-vector product calculations and the storage of intermediate gradient information could still pose scalability issues for extremely large models and datasets.

### Questions
See Weakness.

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
3

### Summary
Understanding sample influence is an important task that has multiple different use tasks. However, existing estimators only provide a single static assessment. The authors propose a novel way that can dynamically and efficiently estimate sample influence across different stages. They provide theoretical bounds and the empirical evaluation shows a much stronger performance than the baseline.

### Strengths
1. The paper addresses an important problem. While providing a static assessment of sample influence is already useful, providing dynamic assessment potentially enables many interesting usages such as pinpointing why the model performance degrades or certain unwanted behavior appears after a certain training period.

2. The empirical performance is strong. The correlation with the ground truth is often pretty high (> 0.9), which is much higher than the influence function baseline.

### Weaknesses
1. It is unclear whether the error bound is meaningful as it grows exponentially. If the exponential growth is inevitable for the non-convex case, then it seems better to show a stronger bound for the convex case instead.

2. While the authors already show the Kendall’s Tau correlations across training stages, it would be of the interest of the readers to see the correlation with respect to each of the evolution patterns: Stable Influencer, Early Influencers, Late Bloomers, and HighlyFluctuating. Since stable influencers are the majority, one can have high correlation by only predicting stable influencers accurately, while it might not correctly identify the Early Influencers and the Late Bloomers, which in some use cases is more of the interest.

3. Can the authors clarify under which condition they think the error bound could be meaningful? Also, it might be useful if the authors can show the error bound for the convex case if it can be much better than the non-convex case. Additionally, bounding this term seems a bit weird as it can be influenced by reparametrization (scaling the data by c in LR seems to result in a 1/c scaling in the parameter and the error bound).

### Questions
1. While the authors already show the Kendall’s Tau correlations across training stages, it would be of the interest of the readers to see the correlation with respect to each of the evolution patterns: Stable Influencer, Early Influencers, Late Bloomers, and HighlyFluctuating. Since stable influencers are the majority, one can have high correlation by only predicting stable influencers accurately, while it might not correctly identify the Early Influencers and the Late Bloomers, which in some use cases is more of the interest.
2. Can the authors clarify under which condition they think the error bound could be meaningful? Also, it might be useful if the authors can show the error bound for the convex case if it can be much better than the non-convex case. Additionally, bounding this term seems a bit weird as it can be influenced by reparametrization (scaling the data by c in LR seems to result in a 1/c scaling in the parameter and the error bound).

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces the Dynamic Influence Tracker (DIT), a novel approach to estimate the dynamic influence of individual training samples in models trained with SGD. Unlike traditional influence methods that provide only static influence estimates, DIT tracks influence over arbitrary time windows during training. DIT operates through a two-phase algorithm: the training phase, which captures and stores relevant information about the model’s parameter trajectory, and the inference phase, which uses this information to estimate sample influence within specific time frames. The authors derive a theoretical error bound for their estimator, demonstrating its applicability in non-convex settings, and present extensive empirical evaluations that highlight how sample influence evolves during training. The experiments show that DIT outperforms existing methods in accuracy.

### Strengths
The example provided in Section 5.2 illustrates that sample influence changes dynamically over the course of training, effectively supporting the motivation for DIT.

### Weaknesses
1.	The theoretical bound in Equation (18) grows exponentially with t making it vacuous for long training intervals.

2.	The empirical evaluations primarily use simple models, like two-layer CNNs, and small datasets, such as MNIST, which limits the demonstration of DIT's scalability and applicability to more complex scenarios.

3.	The empirical results do not clearly show the practical utility of a dynamic influence function. In Section 5.5, the improvement from using DIT is marginal, and the correlations in Section 5.4 lack comparison with baseline methods. Although Figure 2 shows that DIT outperforms Influence Functions (IF) when using the full-time window, DIT’s approach comes with a high storage requirement, which could limit its scalability.

4.	The proposed algorithm relies on a Taylor approximation, requiring storage of all intermediate models during SGD, which results in a trade-off between time and memory complexity that could be problematic for large-scale models.

### Questions
Could the authors present a compelling application for the proposed DIT approach that justifies the substantial storage required for retaining all intermediate models and SGD batches throughout training?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Dear Authors, thanks for submitting to ICLR.

In this paper, the author introduce a novel method for monitoring learning dynamics, termed DIT, which is designed for application across arbitrary neural networks trained with stochastic gradient descent (SGD). Unlike traditional influence functions and their extensions, DIT is not restricted to convex scenarios, demonstrating enhanced effectiveness in common non-convex cases. Additionally, DIT is computationally efficient, avoiding large matrix multiplications and thus enabling its application to complex models. Importantly, the implementation of DIT integrates seamlessly with standard SGD without requiring any modifications, making it readily applicable to a broad range of existing models through standard training routines.

### Strengths
1. Compared with conventional methods like influence function and its extension, the DIT can monitor the influence of whole training process, instead of solely showing the influence on final loss.
2. On the computational side, this method avoids large matrix multiplications, making it highly efficient. This efficiency is particularly critical for complex models where computational overhead is a key concern. In cases where computation is less of an issue, a leave-one-out test could be performed, but for large-scale or resource-intensive models, the lightweight nature of this approach makes it especially advantageous.
3. Overall, DIT outperform IF in terms of accruacy, showing very significant correlation with LOO test.
4. The paper is well-structured and presented in a clear, logical manner, with broadly sound reasoning throughout.

### Weaknesses
1. The evaluation is not comprehensive enough. So far only simple model like CNN and DNN are included. This limits understanding of DIT's performance on more advanced tasks. For instance, it remains unclear if DIT can be effectively applied to fine-tuning large language models (LLMs).
2. Need more detailed result about the computation overhead. So far the experiment is done on a 8 GPU server, and the LOO can be used for these tasks (CNN, DNN, LR etc.). Quantify the computing overhead will help the users to implement DIT properly.
3. In the abstract, the author mentions curriculum learning (CL); however, the paper lacks a direct use case demonstrating how DIT contributes to CL. I see the results in Table 2, but how it will guide a CL process is unclear.
(Please see more detailed suggestions in Questions )

### Questions
There are few detailed questions I would like to get more clarity.

1. For equation (1), line 080, page 2, is it  a critical condition to the DIT? For instance, if I use certain realy stopping method and the equation (1) is not minimized, would DIT still work? Suggestion: add a test for DIT when the model is fully converged.
2. Will this method helps the fine tunning of large pretrained models like LLM? Specifically, how does DIT handle new training samples for a pre-trained model, and does it require retraining the entire model from scratch? Suggestion: at least a clarification about the limitation would be helpful after the evluation, section 5. If the model is too large, maybe investigate a pretrained module inside would be good enough.
3. Please quatify the cumputation efficicency gain of DIT. The result includes but not limited to: computation time compared with LOO, memory consumption. This will highlight the efficiency gain of DIT. This content can appear in section 5.
4. Please add a use case for curriculum learning (CL) in section 5.5, as it is mentioned in the abstract. It's currently unclear how DIT manages dynamic training data, a common feature in CL setups. It is also not clear the correlation showed in Table 2 is sufficient without looking into a real CL task.
5. Given its potential as a highly useful tool, will DIT be made open-source upon acceptance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method, called Dynamic Influence Tracker (DIT), to estimate sample influence during the training process of SGD. The authors provide an error bound for their estimator and show DIT's effectiveness in various examples including anomalous sample detection and curriculum learning.

### Strengths
The authors proposed a method to track the sample influence during a training process. This approach allows us to discover samples that are important in the early stage of training but become dispensable in the end, whereas existing approaches focus on assessing the sample influence for the optimizer. They justified their approach from both theoretical and empirical perspectives.

### Weaknesses
I have two major concerns regarding this paper.

1. In the last term of Eq. (14) and subsequent definition of $\tilde{\mathbf{1}_j^{[t]}}$, the $\theta^{[t]}$ inside the function $g$ should be $\theta_{-j}^{[t]}$. This is not just a typo since it also exists in the proofs (e.g., the last term of Eq. (57)) and Alg. 2. Hence, the whole method requires significant revision.

2. The paper didn't discuss the literature properly which put their claimed contributions in question.
    1. On the computational aspect, the main criticism the authors hold on the influence function is the computation of inverse Hessian, and they propose to project the influence function onto a query function. However, on the one hand, there have been methods designed to reduce this computational complexity such as Arnoldi iteration [1]; on the other hand, the idea of projection has already appeared in the Maximum Influence Subset framework [2].
    2. The definition of influence function does not require convexity. Convexity is only assumed when analyzing its statistical properties (see [3] for an example). Even though convexity is not assumed in the proofs, boundedness of gradient and hessian are assumed instead, which are very strong. In [3], only tail assumptions are made, so it is unclear whether the authors' argument requires less stringent assumptions.

### Questions
See the comments in the previous section.

### Soundness
1

### Presentation
3

### Contribution
2
