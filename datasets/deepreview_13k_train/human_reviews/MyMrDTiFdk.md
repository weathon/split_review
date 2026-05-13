# Approximating Two-Layer ReLU Networks for Hidden State Analysis in Differential Privacy

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
The hidden state threat model of differential privacy (DP) assumes that the adversary has access only to the final trained machine learning (ML) model, without seeing intermediate states during training. Current privacy analyses under this model, however, are limited to convex optimization problems, reducing their applicability to multi-layer neural networks, which are essential in modern deep learning applications. Additionally, the most successful applications of the hidden state privacy analyses in classification tasks have been for logistic regression models. We demonstrate that it is possible to privately train convex problems with privacy-utility trade-offs comparable to those of one hidden-layer ReLU networks trained with DP stochastic gradient descent (DP-SGD). We achieve this through a stochastic approximation of a dual formulation of the ReLU minimization problem which results in a strongly convex problem. This enables the use of existing hidden state privacy analyses, providing accurate privacy bounds also for the noisy cyclic mini-batch gradient descent (NoisyCGD) method with fixed disjoint mini-batches. Our experiments on benchmark classification tasks show that NoisyCGD can achieve privacy-utility trade-offs comparable to DP-SGD applied to one-hidden-layer ReLU networks. Additionally, we provide theoretical utility bounds that highlight the speed-ups gained through the convex approximation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates a privacy algorithm for the two-layer ReLU minimization problem by using a convex dual formulation and privacy amplification through iterative DP analysis.

### Strengths
The technical approach appears largely sound (though I have not conducted a detailed verification). The core idea of transforming the two-layer ReLU network into a stochastic convex formulation to enable privacy analysis is interesting.

### Weaknesses
Under the restricted setting of the two-layer ReLU network, it theoretically yields an improved utility-privacy tradeoff by resorting to a dual form of the original problem. However, its applicability is limited since the approach does not extend to more general non-convex formulations. I would expect papers in this area to provide implications for broader non-convex cases, an aspect that is missing here. Specifically, the paper does not address how the proposed convex dual formulation could be adapted to handle more complex architectures, such as deeper networks or those employing different activation functions. The reliance on a two-layer ReLU network, while simplifying the analysis, significantly restricts the practical relevance of the findings. Furthermore, the paper lacks a discussion on the potential challenges in extending this method to scenarios with more complex data distributions or higher-dimensional inputs, which are common in real-world applications.

### Questions
Can this method outperform the method of directly applying DP-SGD to a state-of-the-art (non-convex) neural network, in terms of utility-privacy tradeoff?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper works on the hidden state threat model of differential privacy, which means the adversary only has access to the final trained machine learning model. The authors consider the model of two-layer Relu activate neural networks, which has not been studied under the hidden state threat model. The idea is to first relax the two-layer network to a stochastic convex program, then solve the relaxaztion with noisy cyclic mini-batch gradient descent. Experiment results show that the proposed method has similar performance as DP-SGD.

### Strengths
This paper extends the study of the hidden state threat model  to non-convex models, which is novel and interesting.

### Weaknesses
 - The novelty seems to be limited. The major technical components, the (stochastic) convexification of 2-layer neural networks and privacy guarantee of NoisyCGD, are from previous works. This main result of this work seems to be a combination of the two components and feels incremental. Also, the paper claims that the proposed method can obtain similar privacy-utility trade-offs as DP-SGD, but actually there is no formal statement on the privacy-utility tradeoff. That is, in order to achieve $(\epsilon,\delta)$-DP in the hidden state threat model, how large the regularization parameter $\lambda$ and noise variance $\sigma^2$ we shall pick up. I do not follow how we can compare the theoretical results with DP-SGD.

- It is not clear how we shall interpret the experiment results. If I understand correctly, the hidden state threat model is a weaker threat model, because the intermediate states are not known to the adversary. So under the same privacy level, we shall need smaller noise and hence observe better utility. But the experiment result is that DP-SGD has similar or even better utility. Why is it the case? What is the advantage of introducing the hidden state threat model then?

- It is hard to distinguish existing results and new finds. For instance, Theorem 5.1 appears with neither reference nor proof. If it is known, please cite where it comes from.
- In Section 3.4 you explicitly mentioned about clipping the gradients. I am not sure if this will break the privacy guarantees of NoisyCGD. [1] discussed about this point and said "...in general, clipped gradients do not correspond to gradients of a convex loss, in which case our results (as well as all other works in the literature that aim at proving convergent privacy bounds) do not apply''. Can you explain a bit more on this?

### Questions
- It is hard to distinguish existing results and new finds. For instance, Theorem 5.1 appears with neither reference nor proof. If it is known, please cite where it comes from.
- In Section 3.4 you explicitly mentioned about clipping the gradients. I am not sure if this will break the privacy guarantees of NoisyCGD. [1] discussed about this point and said "...in general, clipped gradients do not correspond to gradients of a convex loss, in which case our results (as well as all other works in the literature that aim at proving convergent privacy bounds) do not apply''. Can you explain a bit more on this?

[1] Altschuler, Jason, and Kunal Talwar. "Privacy of noisy stochastic gradient descent: More iterations without more privacy loss." Advances in Neural Information Processing Systems 35 (2022): 3788-3800.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates a hidden state threat model in differential privacy, where it assumes the adversary can only access the final model. By leveraging convex reformulation of ReLU networks and privacy amplification via iterative DP analysis, the paper presents a privacy-utility trade-off in the hidden state setting.

### Strengths
The paper addresses an interesting problem in the differential privacy community. I am particularly intrigued by the transition from a two-layer neural network model to a convex formulation, which I have raised questions about below.

### Weaknesses
 - The writing of the paper could be improved, as several aspects are unclear. In my opinion, the paper's structure should be: In the hidden state setting, the authors aim to achieve privacy preservation through convex approximation and privacy amplification by iteration. Specifically:
  - For the DP algorithms, the authors use NoiseCGD.
  - For convex approximation, the ReLU output is rewritten as a set of diagonal Boolean matrices, and the transition from Eq(3.2) to Eq(3.3) is made. However, I lost track in section 3.3. Several definitions and lemmas, in my opinion, should be moved to the appendix.

- There is a grammatical error in lines 270-271.

- The conclusion primarily relies on previous results.

- In the hidden state setting, the authors claim that the adversary only accesses the final model. Does this mean only the final model is privatized? If not, how does this differ from the regular setting in terms of the results? Could you provide some explanations and insights?

- How should one understand the transition from Eq(3.2) to Eq(3.3)? Why does the hidden width $m$ disappear in Eq(3.3)? What is the significance of the range of $|D_x|$, even though it is related to rank, as mentioned in line 267?

- Regarding Theorem 4.1, what is $d_1$, and why is it needed? How do your results compare to DPERM with convex functions? I am confused by this result. Also, Theorem 4.1 pertains to Algorithm 1 (DP-SGD), but I am unsure if this is a typo or if I misunderstood, as I thought the authors were analyzing NoiseCGD.

### Questions
- In the hidden state setting, the authors claim that the adversary only accesses the final model. Does this mean only the final model is privatized? If not, how does this differ from the regular setting in terms of the results? Could you provide some explanations and insights?

- How should one understand the transition from Eq(3.2) to Eq(3.3)? Why does the hidden width $m$ disappear in Eq(3.3)? What is the significance of the range of $|D_x|$, even though it is related to rank, as mentioned in line 267?

- Regarding Theorem 4.1, what is $d_1$, and why is it needed? How do your results compare to DPERM with convex functions? I am confused by this result. Also, Theorem 4.1 pertains to Algorithm 1 (DP-SGD), but I am unsure if this is a typo or if I misunderstood, as I thought the authors were analyzing NoiseCGD.

### Soundness
2

### Presentation
2

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
This paper considers the hidden state threat model, in which the adversary doesn't have access to intermediate outputs during training. Under this model, previous works have demonstrates that the privacy cost of DP-SGD (or DP-CyclicGD) converges for convex and smooth minimization problems (no additional privacy cost for training the model for additional gradient descent steps). However, in practice, these conditions (convexity and smoothness) are not always met. A simple example of a non-convex optimization problem is the training of a two-layer ReLU network under square loss and L2 regularization. 

This work focuses on addressing this issue by leveraging recent findings, which show that with square loss and L2 regularization, the 2-layer ReLU minimization problem becomes equivalent to a strongly convex minimization problem, provided the number of neurons is sufficiently large. This reformulation, being both convex and smooth, allows for the application of convergent privacy analysis under the hidden state threat model.

The authors show this DP-CGD of the alternative convex formulation enjoys similar utility-privacy tradeoff as solving the original non-convex problem with DP-SGD (under the threat model where the adversary can see all intermediate results). Specifically, they demonstrate that if the data follows a normal distribution, DP-CGD of the convex equivalence enjoys utility guarantee of the order $O(1/\sqrt{n}\epsilon)$. They also provide experimental results to support their claims.

### Strengths
Privacy analysis under the hidden state model is challenging for non-convex problems, as the privacy loss is typically intractable in such cases. The authors cleverly leverage recent findings that show certain non-convex problems can be reformulated as convex ones. Even though this work does not give general recipe for all non-convex problems, it is a first step towards privacy analysis under hidden state models for non-convex problems.

### Weaknesses
 - A limitation of this work, which perhaps coincides with its advantage, is that it offers a restricted solution for privacy analysis in non-convex problems. The approach still relies on tools for convex and smooth problems, meaning that only non-convex problems that can be reformulated as convex can be analyzed. However, determining whether a non-convex problem has a convex formulation is inherently challenging. Moreover, the reliance on a large number of neurons to achieve this convex equivalence introduces a practical constraint, potentially leading to computationally expensive models. The paper does not thoroughly explore the trade-offs between the number of neurons, the resulting model size, and the computational cost, which is a crucial aspect for practical applications.

- The preliminary section lacks coherence and is somewhat difficult to follow. Although the key concepts are introduced, their relevance to the privacy analysis is less clearly explained. For instance, the connection between the specific properties of the chosen convex reformulation and the subsequent privacy analysis is not made explicit, leaving the reader to infer the importance of these properties. The discussion could benefit from a more structured approach, clearly outlining how each concept contributes to the final privacy guarantees.

### Questions
1. In Figure 3, ReLU with DP-SGD outperforms DP-SGD and NosiyCGD for larger $\epsilon$. Is there any intuition for this phenomenon?

### Soundness
3

### Presentation
2

### Contribution
3
