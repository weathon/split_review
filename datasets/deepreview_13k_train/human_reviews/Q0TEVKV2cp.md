# Debiasing Mini-Batch Quadratics for Applications in Deep Learning

- Decision: Accept
- Scores: 8, 8, 3, 8

## Abstract
Quadratic approximations form a fundamental building block of machine learning
  methods. E.g., second-order optimizers try to find the Newton step into the minimum of a
  local quadratic proxy to the objective function; and the second-order approximation of
  a network's loss function can be used to quantify the uncertainty of its outputs via
  the Laplace approximation.
When computations on the entire training set are intractable---typical for deep
  learning---the relevant quantities are computed on mini-batches. This, however,
  distorts and biases the shape of the associated \textit{stochastic} quadratic
  approximations in an intricate way with detrimental effects on applications.
In this paper, we (i) show that this bias introduces a systematic error, (ii) provide
  a theoretical explanation for it, (iii) explain its relevance for second-order
  optimization and uncertainty quantification via the Laplace approximation in deep
  learning, and (iv) develop and evaluate debiasing strategies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates biases in mini-batch quadratic approximations, for second-order optimization in deep learning. Authors show that when computing quadratic on mini-batches rather than the full dataset, it introduces curvature distortions, leading to overly narrow approximations. The bias, assigned to “regression to the mean”, affects Newton steps in optimizers and Laplace approx for uncertainty quantification. They provide a “two-batch” strategy to decouple direction selection from magnitude estimation, to align mini batch approx more closely with full-batch behaviour with minimal computational overhead. They demonstrate the improve stability of their strategy on CG and K-FAC experiments.

### Strengths
Authors study a well-known but often overlooked issue in mini-batch approx within second-order optimisations and uncertainty quantification for deep learning: the bias in curvature estimates due to mini-batch sampling. While the issue is not new, the approach of a two-batch debasing strategy is an effective and novel (to my knowledge) way to address it and improve the accuracy of the approximates without suffering too much of a computational overhead. This strategy could generalise well across various settings in ML where the full-batch quadratics are intractable. The paper is supported by nice empirical experiments on CG and K-FAC demonstrating the effectiveness of their solution. The authors provide a theoretical intuition for the bias arising from that “regression to the mean” adding an interesting insight.  The experiments are systematically presented and show clear performance difference between single-batch and debasing method . While very technical, authors make an effort to make it as digestible as possible, with the inclusion of figures to visualise the bias and the impact of their debasing strategy.

### Weaknesses
The experimental scope is pretty limited, with only ablations on CNN architecture and CIFAR-10/100 datasets. Testing on a wider variety of architectures, such as transformers or larger datasets, would strengthen a lot the paper’s claims on general applicability. Specifically, the paper lacks experiments on models with different architectural features, such as attention mechanisms or skip connections, which could exhibit different curvature properties and sensitivities to mini-batch biases. Furthermore, the datasets used are relatively small, and it's unclear how the observed biases and the effectiveness of the two-batch debiasing strategy would translate to larger, more complex datasets with different data distributions. Another limitations lies in the lack of ablations to investigate the sensitivity of the two-batch approach to mini-batch size, as well as the composition of mini-batches used for debasing. Without these, it’s unclear how the two-batch batch method would perform under different resource constraints or mini-batch sampling strategies. For example, it's not clear if the method is robust to very small mini-batch sizes, or if there's a critical mini-batch size below which the debiasing strategy becomes ineffective or unstable. Last, the paper discusses the computational trade-offs, but does not provide sufficient detail to me on actual runtime and memory costs for different debasing configuration, leaving with an incomplete understanding of the true method’s scalability. The paper mentions a doubling of computational cost, but it does not specify if this is a strict doubling or if the overhead scales differently with batch size or model complexity. A detailed breakdown of the computational cost, including the time spent on each step of the two-batch method, would be beneficial.

### Questions
— How do you anticipate the method to scale or adapt with different architecture and larger dataset, which have different curvature profiles and optimisation challenges?
— Could you clarify the criteria for selecting mini-batches in the two-batch debasing process? Is there any benefit to use overlapping vs. non-overlapping mini-batches, or would a mini-batch with a specific loss profile provide better results? 
— Can you provide more details on runtime/memory costs associated with the two-batch approach? While authors claim it roughly doubles, it would be helpful to understand how this really scales with batch size, and whether costs remain manageable as model size and dataset complexity grow

### Soundness
4

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
3

### Summary
This paper addresses the systematic bias in mini-batch quadratic approximations used for second-order optimization and uncertainty quantification in deep learning. Mini-batch methods distort the quadratic shape, making uncertainty estimates unreliable. The authors provide a theoretical explanation, discuss the impact on optimization, and propose debiasing strategies to improve accuracy.

### Strengths
This is an interesting theoretical investigation collaborated with numerical justifications. It teaches me something that I would expect with a nice and convincing narrative. The overall clarity and language of this paper is good. The insights are well-delivered. The theoretical analyses are mostly backed up by numerical experiments.

### Weaknesses
I did not identify any obvious weaknesses.

I did not check the proofs.

### Questions
How well do the proposed debiasing strategies scale for large foundation models with millions or billions of parameters?

Can debiased mini-batch quadratics improve uncertainty quantification in foundation models, especially in tasks requiring precise uncertainty, like language modeling or image synthesis?

Can the theoretical insights and debiasing techniques be effectively adapted for transformer-based foundation models?

Could reduced bias in mini-batch quadratics enhance transfer learning by improving local loss landscape approximations during fine-tuning?

How might the debiasing methods apply to multi-modal foundation models, where different data modalities add complexity to curvature estimation?

### Soundness
4

### Presentation
4

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
This paper demonstrates a systematic bias in stochastic 2nd order approximation of empirical risk for neural networks. The study start from an observation showing that a particular curvature structure on minibatch Hessian is biased towards underestimation. Then, authors proposes a debiasing method.

### Strengths
- A computationally-cheap estimate of 2nd order information is an important topic for optimization 
- Ample experimental observations 
- Designing computational-cheap experiments to study 2nd order derivative of training loss of neural networks

### Weaknesses
I believe the notion of unbiased estimate is not well defined and studied. Define the Hessian associate with full-batch training loss as  $$H(x) = \frac{1}{n} \sum_{i=1}^n \nabla^2 f_i(x)$$. Similarly, we define the unbiased estimate of this matrix as $$H'(x) = \frac{1}{m} \sum_{k=1}^m \nabla^2 f_{i_k}(x)$$ where $i_k$ are uniformly drawn from $\{1,\dots, n\}$. 
For each fixed vector $d$, we have $$E d^\top H' d^\top = d^\top H d$$. Thus, the **directional curvature**, defined in the paper, is unbiased. But, why this paper observe a bias in the estimate? The main issue is that they consider random directions $d$ depending on minibatches. I do not know why we need to choose random $d$s? 

I believe the quantity of interest is not well defined and motivated, here. It is easy to provide an unbiased estimation of  $q$, directional curvature and directional slop. But, the authors want to estimating another quality that they do not exactly defined and it is not clear how its estimation connect with Newton's method or Laplace approximation. 

If you want to estimate the maximum/minimum eigenvalue of the Hessian or even its condition number, the empirical Hessian provides an asymptotically unbiased estimate (see for example https://arxiv.org/pdf/1912.10754).

### Questions
- I recommend to replace $u_1$ and $u_2$ in Figure 1 by leading eigenvectors of full-batch Hessian to better grasp my comment in weaknesses. I expect to see that increasing batch size will lead to a better approximation of the curvature. 
- What is exactly the quantity that you want to estimate and why it is important to estimate? Directional curvature on which random directions?
- What do you exactly mean by bias? To prove an estimate has bias, we need to take average. But, experiments in Figure 1 are not computing an average. How can I conclude from these experiments that the estimate is biased?

### Soundness
2

### Presentation
2

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
Often one would like to obtain a second-order Taylor approximation to a deep learning objective based on a minibatch.  This paper shows that the use of a minibatch results in a strong overestimation of the top Hessian eigenvalues.  The basic problem is that the directions of highest curvature for a minibatch tend to slightly 'overfit' (my words) that minibatch, and do not generalize to other minibatches or to the full-batch objective.  This paper shows that this bias can be corrected with a scheme that uses two separate minibatches - one to compute the top eigenvectors, and another to compute the directional curvature along these eigenvectors.  The paper discusses applications in both optimization (conjugate gradient method for computing a newton step), and uncertainty quantification (laplace's method)

### Strengths
The paper offers a simple solution to a problem of interest to multiple areas of deep learning.

### Weaknesses
In the application to optimization, the paper does not actually carry out an end-to-end optimization run with a second-order method using the proposed conjugate gradient scheme; instead, the paper just uses the proposed scheme to compute a single newton step. This is a significant limitation, as the true value of a second-order method lies in its ability to navigate the loss landscape over multiple steps, not just a single step. The paper's approach might be beneficial for fine-tuning a model near a local minimum, but it does not demonstrate the method's capacity for full optimization. The lack of an end-to-end optimization experiment makes it difficult to assess the practical impact of the proposed debiasing scheme on the overall training process.

Regarding the motivation in section 3.1 -- just because the gradient lives in the top subspaces does _not_ mean that all the optimization progress occurs in that space. To the contrary, the evidence suggests that the vast majority of the motion along the top Hessian eigenvectors is oscillatory, and 'cancels out.' Long-term loss reduction is due to the components of the gradient that lie along the low-curvature Hessian eigenvectors. For example, see "Does SGD really happen in tiny subspaces?" by Minhak Song, Kwangjun Ahn, Chulhee Yun: https://arxiv.org/abs/2405.16002.

I don't think this is fatal for the paper, since you are basically only using your improved estimate of the the top Hessian eigenvalues in order to properly compute the conjugate gradient _step size_, which will depend on the top Hessian eigenvalues. But if you actually tried to optimize only along those eigenvectors, it wouldn't work (as the linked paper shows).

### Questions
Regarding the motivation in section 3.1 -- just because the gradient lives in the top subspaces does _not_ mean that all the optimization progress occurs in that space.  To the contrary, the evidence suggests that the vast majority of the motion along the top Hessian eigenvectors is oscillatory, and 'cancels out.'  Long-term loss reduction is due to the components of the gradient that lie along the low-curvature Hessian eigenvectors.  For example, see "Does SGD really happen in tiny subspaces?" by Minhak Song, Kwangjun Ahn, Chulhee Yun: https://arxiv.org/abs/2405.16002.  

I don't think this is fatal for the paper, since you are basically only using your improved estimate of the the top Hessian eigenvalues in order to properly compute the conjugate gradient _step size_, which will depend on the top Hessian eigenvalues.  But if you actually tried to optimize only along those eigenvectors, it wouldn't work (as the linked paper shows).

### Soundness
3

### Presentation
3

### Contribution
3
