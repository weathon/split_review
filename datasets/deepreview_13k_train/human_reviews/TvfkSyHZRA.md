# Grokking at the Edge of Numerical Stability

- Decision: Accept
- Scores: 8, 5, 8, 8, 6

## Abstract
Grokking, or sudden generalization that occurs after prolonged overfitting, is a surprising phenomenon that has challenged our understanding of deep learning. While a lot of progress has been made in understanding grokking, it is still not clear why generalization is delayed and why grokking often does not happen without regularization. In this work we argue that without regularization, grokking tasks push models to the edge of numerical stability, introducing floating point errors in the Softmax that we refer to as _Softmax Collapse_ (SC). We show that SC prevents grokking and that mitigating SC leads to grokking _without_ regularization. Investigating the root cause of SC, we find that beyond the point of overfitting, the gradients strongly align with what we call the _naïve loss minimization_ (NLM) direction. This component of the gradient does not change the predictions of the model but decreases the loss by scaling the logits, usually through the scaling of the weights along their current direction. We show that this scaling of the logits explains the delay in generalization characteristic of grokking, and eventually leads to SC, stopping learning altogether. To validate these hypotheses, we introduce two key contributions that mitigate the issues faced in grokking tasks: (i) $\mathrm{StableMax}$, a new activation function that prevents SC and enables grokking without regularization, and (ii) $\perp\mathrm{Grad}$, a training algorithm that leads to quick generalization in grokking tasks by preventing NLM altogether. These contributions provide new insights into grokking, shedding light on its delayed generalization, reliance on regularization, and the effectiveness of known grokking-inducing methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper uncovers the critical role of numerical stability in grokking, demonstrating that Softmax Collapse  (SC) prevents grokking and that mitigating SC leads to grokking without regularization.

### Strengths
- The authors make a novel discovery regarding the crucial role of numerical stability in grokking and identify the Softmax Collapse (SC) phenomenon.
- They reveal that SC results from naive loss minimization (NLM) of cross-entropy loss.
- Based on these theoretical insights, the authors propose two methods—StableMax and $\perp$Grad—to mitigate issues faced in grokking tasks.

### Weaknesses
 - **Softmax Collapse (SC).** 
  - The current definitions in Section 3.1 is somewhat abstract and could be more practically grounded. For example, when using float16, what is the $\epsilon$ in Definition 1, and what specific difference between the two logits in Definition 3 would lead to SC? It would be helpful to provide a concrete example, perhaps showing a small set of logits and how they evolve during training to illustrate the collapse. Furthermore, the definition of SC should explicitly state the threshold for the logit difference that triggers the collapse, rather than leaving it as an implicit condition.
  - In transformers, softmax is applied in all self-attention layers, not just the last layer. Does SC also occur in these layers? The paper should investigate and clarify if the same SC phenomenon is observed in the attention layers, and if so, how it impacts the overall model behavior. It's possible that the effects of SC in earlier layers are different from those in the final layer, and this needs to be explored.

- **StableMax.**
  - I am concerned that StableMax may not be suitable for the softmax in attention layers of transformers. Many experiments show that attention matrices in transformers are highly sparse, but the *slower growth rate* of StableMax (compared to softmax) could hinder its ability to model such sparsity. The paper should provide a more detailed analysis of how StableMax affects the sparsity of attention matrices and whether this impacts model performance. It would be beneficial to see a comparison of the sparsity patterns of attention matrices when using softmax versus StableMax.

- **Naive Loss Minimization (NLM).**
  - It is worth noting that this emperical observation has been proven in related works, such as in linear models [1], deep linear networks [2], and homogeneous networks [3]. As training progresses, the "angular velocity" becomes much slower than the growth of the norm, and the directional convergence holds: $\left<-\frac{\nabla L(\theta_t)}{\|\|\nabla L(\theta_t)\|\|},\frac{\theta_t}{\|\|\theta_t\|\|}\right>\to1$. The paper should more explicitly acknowledge and discuss these connections to prior work, and clarify how the current work builds upon these existing results. The current discussion of NLM feels somewhat isolated from these well-established findings.
  - It seems that this explanation holds only for cross-entropy loss. For squared loss, NLM does not appear to hold. The paper should discuss the limitations of NLM and SC with respect to different loss functions, and clarify why the proposed methods are specifically designed for cross-entropy loss.

- **$\perp$Grad.** 
  - Based on my understanding, the motivation behind $\perp$Grad is to amplify the angular velocity of GD, similar to the effects of normalization layers and weight decay. Additionally, related work [4] also explores how to amplify the angular velocity of GD. The paper should provide a more detailed comparison of $\perp$Grad to these existing techniques, and clarify the specific advantages of the proposed method. A more thorough analysis of the relationship between $\perp$Grad and other methods that manipulate the gradient direction would be valuable.
  - Adaptive algorithms like Adam may not encounter the same NLM problem as GD late in training. Would it be effective to use $\perp$Grad+Adam to accelarate the grokking process of Adam? The paper should investigate the effectiveness of $\perp$Grad when combined with adaptive optimizers like Adam, and discuss if the same benefits can be observed. It would be useful to see empirical results comparing the performance of $\perp$Grad with different optimizers.

### Questions
Refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates the phenomenon of grokking, where deep learning models suddenly generalize after a period of overfitting, and it proposes new mechanisms that explain why generalization is often delayed. The authors identify Softmax Collapse, a numerical instability in Softmax, as a key factor preventing grokking in models trained without Weight Decay. To address this, they introduce "StableMax," a modified Softmax function that reduces numerical errors, and "⊥Grad," an optimizer that excludes the naive loss minimization direction.  The latter refers to an optimization path that reduces the loss by scaling logits without changing model predictions and potentially leading to numerical errors.

### Strengths
- The paper is well-written and easy to follow.
- The research problem is conceptually well-motivated and aligns with current challenges in understanding grokking.
- The hypothesis presented, that Softmax Collapse inhibits grokking, is interesting.

### Weaknesses
1.  **Unclear Justification for Proposed  Adjustments Over Established Regularization Techniques** While the paper suggests several adjustments to address generalization delay, it remains unclear if and why these modifications should be preferred over established techniques such as weight decay, particularly at larger scales. A comparative analysis with standard approaches would strengthen the argument for these adjustments. Specifically, the paper lacks a clear demonstration of how the proposed methods offer advantages in terms of computational efficiency, hyperparameter sensitivity, or robustness compared to weight decay or other common regularization techniques. The absence of such analysis makes it difficult to assess the practical utility of the proposed adjustments.

2.  **StableMax Analysis:** The introduction of StableMax is a substantial change to the training paradigm. However, the paper lacks an in-depth analysis of its properties, such as the impact on the optimization landscape and the types of solutions this modified model converges towards. Given the importance of StableMax, its introduction should be supported by either extensive experimental validation or a rigorous theoretical justification. For example, it would be beneficial to see an analysis of how StableMax affects the sharpness of the loss landscape or the distribution of the model's weights, and whether it introduces any new optimization challenges.

3.  **Optimizer in Section 5.1:** Similar to StableMax, the optimizer proposed in Section 5.1 would benefit from additional empirical or theoretical analysis. Specifically, how it compares with other optimizers in terms of convergence behavior and stability beyond the context of grokking tasks. The paper should provide a more detailed analysis of the optimizer's convergence properties, such as its sensitivity to learning rate and momentum, and how it compares to standard optimizers like Adam or SGD in terms of training time and final performance on a wider range of tasks.

4.  **Insufficient Evidence for Naive Loss Minimization:** The evidence provided for the claim of naive loss minimization is limited. Existing literature, such as that referenced work of Lyu and Li (2019)​[1] (in Appendix K.1 ), shows that even after achieving 100% training accuracy, gradient descent with cross-entropy loss implicitly performs margin maximization. This result seems to contradict the authors’ hypothesis that the optimization follows a direction of naive loss minimization, where the function remains unchanged across the entire input space (as described in Equation 9).  Further evidence is needed to validate naive loss minimization from this established understanding of implicit bias in gradient descent. The paper needs to provide more direct empirical evidence that the optimization trajectory aligns with the proposed naive loss minimization direction, and to address the apparent contradiction with the established understanding of margin maximization in gradient descent.

### Questions
1. Could the authors further discuss naive loss minimization in relation to the max-margin implicit bias as described in [1]? In particular the claim that the direction of the optimization trajectory is the one that does not change the prediction for all data points in the input space (Equation 9). 


2. Could the authors clarify why the proposed adjustments should be prioritized over traditional methods like weight decay?


3. Can the authors elaborate on how the proposed optimizer relates to [2]?


4. Is there a connection between the projected optimizer in this paper and the rotational equilibrium update discussed in [3] as an effect of weight decay?


5. For Figure 2, could the authors specify the task on which the models are trained?


6. In Figure 6, do the authors have experiments demonstrating the impact of different weight decay values on the delay in generalization?

[1] Lyu, Kaifeng, and Jian Li. "Gradient descent maximizes the margin of homogeneous neural networks." _arXiv preprint arXiv:1906.05890_ (2019).


[2] Heo, Byeongho, et al. "Adamp: Slowing down the slowdown for momentum optimizers on scale-invariant weights." _arXiv preprint arXiv:2006.08217_ (2020).


[3] Kosson, Atli, Bettina Messmer, and Martin Jaggi. "Rotational equilibrium: How weight decay balances learning across neural networks." _arXiv preprint arXiv:2305.17212_ (2023).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies grokking. It found that when the loss function is cross-entropy loss, the floating point errors caused by softmax prevents the model from generalization if trained without any regularization. They proposed a modified loss function and a modified optimizer that  enable the model to generalize without regularization.

### Strengths
This work studies grokking from an interesting view and provided an explanation for why the model is trapped in an overfitting regime.

### Weaknesses
 - The application of the proposed method is limited. It only turns from overfitting without generalization to generalization when there is no regularization and the original loss is cross-entropy loss. Is ⊥AdamW still better than AdamW with non-zero weight decay? E.g. can you compare ⊥AdamW against AdamW with various non-zero weight decay values for transformers and MLP on modular addition task?
- The proposed method is only tested on some toy models such as two-layer neural networks and one-layer transformer. It would be more convincing to apply the method on deeper transformers, e.g. the same architecture as GPT2-small.
- Sec 4.1 compares one-hot encoding with binary and scalar representation to show overfitting is harder, which is not fair: 
    - 1. the one-hot vector does not have any information of the integers, but binary and scalar vectors do contain some info. 
    - 2. the model trained on binary and scalar vectors has fewer parameters, making overfitting harder. 
A fair comparison would be using randomly generated d-dim vectors on a uniform sphere as the low-dim representation, and using a model with larger width to make sure the number of params is roughly the same.

### Questions
- What’s the difference between absorption error and Roundoff error?

- Why setting the gradient of correctly predicted (overfitted) samples to zero prevents generalization? Is there an intuitive explanation?

- In Figure 1c, can grokking still occur after careful hyper parameters(initialization scale, learning rate) tunning?

- [1] found that one-layer transformer trained with float32 precision has loss spikes and use float64 for more stable training. This implies that the slingshot mechanism [2] may be caused by numeric stability. Can softmax collapse explain slingshot?

[1] Progress measures for grokking via mechanistic interpretability

[2] The Slingshot Mechanism: An Empirical Study of Adaptive Optimizers and the Grokking Phenomenon

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
4

### Summary
This paper investigates why grokking happens and why it often does not happen without regularization. They show that lack of regularization in tasks where grokking is observed, can lead to overfitting, which is caused by floating point errors in the softmax. Mitigating this softmax collapse (SC) leads to grokking. Further, they show the root cause of SC to be the alignment of gradients with a naive loss minimization (NLM) direction, which does not improve generalization, even though it reduces train loss via scaling. Finally, they propose a StableMax activation that prevents SC and a training algorithm $\perp$ Grad that leads to faster generalization, by amplifying gradients orthogonal to the NLM direction.

### Strengths
The paper advances our understanding of why generalization or grokking may not happen without regularization and proposes ways to induce grokking or faster generalization via StableMax and $\perp$ Grad.

The paper is well-written and easy to understand. The claims are well supported by the presented results.

### Weaknesses
There are no major weaknesses. Some minor concerns are as follows.

- The phase ‘grokking tasks’ can be reworded as ‘tasks where grokking is commonly observed’, since there is no formal definition of grokking tasks.
- The readability can be improved by better placement of the figures (same page as the corresponding discussion).
- In lines 302-304, the digits 1- can be replaces with i) for better readability.

### Questions
- How do other factors such as initialization scale, learning rate, etc. interact with grokking?
- Do the results shown in Fig. 4 correspond to one the settings shown in Fig. 2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the phenomenon of grokking in deep learning, where a model unexpectedly starts to generalize well after a period of severe overfitting. To combat this, the authors propose two primary methods: (1) a numerically stable StableMax activation function aimed at mitigating softmax collapse (SC), and (2) ⊥Grad (orthogonal gradient optimization) to counteract Naïve Loss Minimization (NLM), where gradients become aligned in a way that fails to drive effective learning. These methods are tested on a range of tasks, with a specific focus on scenarios where delayed generalization is a challenge.

### Strengths
**Novel Approach to Softmax Collapse**: The introduction of the StableMax activation is an innovative approach to addressing potential issues with Softmax, providing a novel perspective on controlling model output stability.

**Orthogonal Gradients for Effective Training**: The concept of ⊥Grad is compelling and introduces a new approach to optimization that could be useful in a variety of training settings where standard gradient descent shows limitations.

**Comprehensive Analysis**: The paper provides detailed insights into the mechanics of grokking and includes empirical examples to illustrate the phenomenon.

### Weaknesses
 **Overemphasis on StableMax**: The proposed StableMax activation may be overengineered, as issues with softmax stability are often handled with simpler methods, like temperature scaling or loss smoothing. The authors could provide a comparison with such methods. The practical necessity and advantage of StableMax might be limited in many standard applications. Specifically, the paper lacks a clear justification for why StableMax is superior to these established techniques in the context of grokking, especially given that temperature scaling and label smoothing are computationally cheaper and easier to implement. The authors should clarify the specific scenarios where StableMax provides a unique benefit that cannot be achieved by these simpler alternatives.

**Underdeveloped Exploration of ⊥Grad**: Although ⊥Grad is promising, the current study lacks a thorough exploration of how it compares to more traditional optimization methods across a variety of tasks. Additional benchmarking could help clarify its broader applicability and effectiveness. The paper does not sufficiently explore the sensitivity of ⊥Grad to different learning rates, batch sizes, and network architectures. It is unclear if the observed benefits of ⊥Grad are consistent across different hyperparameter settings and model types. Furthermore, the paper should include a comparison with other optimization techniques that also aim to prevent gradient alignment, such as those based on gradient diversity or variance regularization. This would help to contextualize the contribution of ⊥Grad and identify its specific advantages and limitations.

### Questions
1. How does StableMax compare to standard techniques like loss smoothing? If StableMax’s advantage lies mainly in mitigating SC, could similar results be achieved with regularization techniques already in use? Some experiments with loss smoothing and temperature scaling to establish a fair comparison could be beneficial to the paper.

2. Is ⊥Grad beneficial for tasks where overfitting is not prominent? Understanding if this method generalizes to other contexts could add depth to the findings.

3. ⊥Grad prevents scaling in the logits; is there any impact on margin and generalization, or is it compensated because the norm of weights remains low? 
The paper would benefit from additional experiments in varied settings to benchmark ⊥Grad against standard optimizers and even on non grokking tasks. 

4. What is the computational overhead of implementing StableMax and ⊥Grad? Practical adoption would require insight into the trade-off between stability and additional computational complexity.

### Soundness
3

### Presentation
3

### Contribution
2
