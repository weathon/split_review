# Sobolev acceleration for neural networks

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
Sobolev training for neural networks, a technique that integrates target derivatives into the training process, has demonstrated significantly faster convergence towards lower test errors when compared to conventional loss functions. However, to date, the effect of this training has not been understood comprehensively. This paper presents analytical evidence that Sobolev training accelerates the convergence of rectified linear unit (ReLU)-networks in the student-teacher framework. The analysis builds upon the analytical formula for the population gradients of ReLU networks with centered spherical Gaussian input. Further, numerical examples were considered to show that the results may be extended to multi-layered neural networks with various activation functions and architectures. Finally, we propose the use of Chebyshev spectral differentiation as a solution to approximate target derivatives and address prior limitations on using approximated derivatives. Overall, this study contributes to a deeper understanding of the dynamics of ReLU networks in the student-teacher setting and highlights the convergence acceleration achieved through Sobolev training, known as Sobolev acceleration.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article presents a theoretical study of Sobolev Training, an alternative to least-squares fitting that replaces an $\mathcal{L}^2$ fitting error with $\mathcal{H}^p$ fitting error, for some $p > 0$. This method fits the target function by not only matching its values on the training data, but also matching higher order derivatives, leading to improved convergence speed. 

To understand this effect, the authors study a toy model for training neural networks. They focus on one layer, single node RELU and RELU^2 networks, and they study the dynamics of model parameters under gradient flow-based minimization of the Sobolev loss. The Jacobian of the Sobolev loss has additional terms which are positive semidefinite when $w_0$ is sufficiently close to $w^*$, leading to (potentially) improved convergence speeds. These additional terms are not surprising, since the Sobolev loss can be thought of as a sum of $\mathcal{L}^2$ loss and additional terms measuring the $\mathcal{L}^2$ mismatch of gradients, which improve the convergence speed of gradient flow. 

Finally, to approximate Sobolev Training in practice, the authors propose to use Chebyshev spectral differentiation, a popular numerical differentiation method. Across a variety of toy experiments, Sobolev Training is shown to accelerate convergence of GD and SGD.

### Strengths
- Simple idea and analysis: the idea behind Sobolev training is clearly presented and easy to understand. The authors identify a simple and straightforward theoretical explanation for empirical observations that Sobolev training improves convergence speed. 
- Clear and correct proofs: the proofs in this work are presented clearly and they are correct to the best of my knowledge.

### Weaknesses
 - Unfair/vacuous comparison: it is unfair to compare the convergence of gradient flow on $\mathcal{H}(w)$ and on $\mathcal{L}(w)$, since $\mathcal{H}(w)$ has extra terms that are added in an unnormalized way. To understand why this is unfair, consider another (trivial) way to accelerate the convergence speed of gradient flow, by rescaling the loss.  Set $\tilde{\mathcal{L}}(w) = \mathcal{L}(w) + \mathcal{L}(w)$, then in the notation of Theorem 1, $\partial \tilde{V} / \partial t = -2 (w - w^*)^T \nabla_w \mathcal{L} \leq 2 \partial V / \partial t < 0$, which is already a significantly stronger 'acceleration' than Theorems 2 and 3 because it converges twice as fast (whereas Theorem 2 and 3 show only convergence that is not any slower than Theorem 1). Simply adding extra convex terms to the loss isn't sufficient to argue an acceleration phenomena, any more than rescaling the loss would be. It would be more fair to average the terms in the Sobolev loss, or to rescale so that $\mathcal{L}(0) = \mathcal{H}(0)$, but then Theorems 2 and 3 might not hold.
- Synthetic/toy experiments: the experimental evaluation in this work is entirely focused training toy objectives. While the Sobolev loss is shown to improve convergence on these objectives, it's not clear whether this benefit extends to actual datasets.

### Questions
In Figure 3, Sobolev training seems to induce training instability in the form of large loss spikes during late training. Does the Sobolev training loss have higher variance over random initializations of GD? It would be helpful to add error bars to Figures 3, 4, and 5.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies empirically, the effects of sobolev acceleration on training neural networks. It has some theoretical guarantees on very specific usecases, and has some experimental evidence.

### Strengths
The paper is quite interesting, and it has promise in training neural networks. It also studies various different non-linearities.

### Weaknesses
The paper studies, both theoretically and empirically, very niche use-cases, which do not represent real architectures or real datasets. This dramatically decreases the effect of the work, as it is not clear these results mirror the true reality of what goes on in deep neural networks.

### Questions
Could the authors provide results on more "real" dataset, e.g. CIFAR10, CIFAR100, Imagenet? Using modern architectures such as ConvNext, Resnet, RegNet, ViT? this will make the paper much stronger.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study investigates Sobolev training for neural networks, demonstrating its ability to expedite convergence and reduce test errors in comparison to traditional training methods, particularly for rectified linear unit (ReLU) networks within the student–teacher framework. By leveraging the analytical formula for population gradients of ReLU networks and extending findings through numerical examples to various network architectures, the paper enhances the understanding of ReLU network dynamics. Additionally, it introduces Chebyshev spectral differentiation as a solution for approximating target derivatives, addressing previous challenges and underscoring the convergence benefits, or "Sobolev acceleration," of this training approach.

### Strengths
Sobolev training is an interesting topic in recent years. Authors theoretically and empirically  showed the acceleration effect for a specific NN. 
It's interesting to see authors proposed to approximate target function derivatives by using Chebyshev spectral differentiation

### Weaknesses
The work is restricted to a relatively simple architecture. 
I am not sure its practical usage for other communities.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the effect of Sobolev acceleration for neural networks, focusing on the case of a ReLU network in the teacher student setting. They theoretically show that replacing the L2 loss by the corresponding Sobolev (H1 or H2) loss can increase of the rate of convergence. They consider the use of Chebyshev spectral differentiation to approximate the derivatives in the case where one does not have access to an analytic form. They also provide experiments which show that in a variety of settings, training using the Sobolev norm leads to faster and better convergence of the MSE loss.

### Strengths
- The experimental evidence for the speed up of Sobolev training seems quite strong
- In the experiments they also consider a setting beyond the teacher student setup, where the goal is to learn a general function the derivative of which is then approximated using Chebyshev spectral differentiation.
- The high-level presentation of their work is clear

### Weaknesses
The theoretical analysis seems a bit shallow, see also questions

- In both theorem 2 and 3 it is written that  the convergence $\omega \to \omega^*$ is accelerated. How is this statement formally defined?
- Related to the above question, the bound on the derivative of $V$ in theorem 2 and 3 only shows that Sobolev training is at least as good as L2 training, but it is not clear how to derive any concrete quantitative bound from this result.
- In the beginning of section 4 it is stated that $\omega^*$ and $e$ are sampled randomly, what distributions are they sampled from?

### Questions
- In both theorem 2 and 3 it is written that  the convergence $\omega \to \omega^*$ is accelerated. How is this statement formally defined?
- Related to the above question, the bound on the derivative of $V$ in theorem 2 and 3 only shows that Sobolev training is at least as good as L2 training, but it is not clear how to derive any concrete quantitative bound from this result.
- In the beginning of section 4 it is stated that $\omega^*$ and $e$ are sampled randomly, what distributions are they sampled from?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
