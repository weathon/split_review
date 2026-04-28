# Sharper Guarantees for Learning Neural Network Classifiers with Gradient Methods

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
In this paper, we study the data-dependent convergence and generalization behavior of gradient methods for neural networks with smooth activation. Our first result is a novel bound on the excess risk of deep networks trained by the logistic loss, via an alogirthmic stability analysis. Compared to previous works, our results improve upon the shortcomings of the well-established Rademacher complexity-based bounds. Importantly, the bounds we derive in this paper are tighter, hold even for neural networks of small width, do not scale unfavorably with width, are algorithm-dependent, and consequently capture the role of initialization on the sample complexity of gradient descent for deep nets. Specialized to noiseless data separable with margin $\gamma$ by neural tangent kernel (NTK) features of a network of width $\Omega(\poly(\log(n)))$, we show the test-error rate to be $e^{O(L)}/{\gamma^2 n}$, where $n$ is the training set size and $L$ denotes the number of hidden layers. This  is an improvement in the test loss bound compared to previous works while maintaining the poly-logarithmic width conditions. We further investigate excess risk bounds for deep nets trained with noisy data, establishing that under a polynomial condition on the network width, gradient descent can achieve the optimal excess risk. Finally, we show that a large step-size significantly improves upon the NTK regime's results in classifying the XOR distribution. In particular, we show for a one-hidden layer neural network of constant width $m$ with quadratic activation and standard Gaussian initialization that SGD with linear sample complexity and with a large step-size $\eta=m$ reaches the perfect test accuracy after only $\ceil{\log(d)}$ iterations, where $d$ is the data dimension.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper obtains convergence and generalization bounds for gradient descent training of neural networks with smooth activation functions. An algorithmic stability analysis exploiting the Hessian properties in the gradient descent path allows to bound the generalization gap with the cumulative optimization error.  Ultimately, the bound on the test loss depends on the Euclidean distance with initialization and the Lipschitz constant of the network at initialization. Experiments with a 2-hidden layer network on MNIST and FashionMNIST show that the theoretical bounds provide accurate approximations for the test loss and generalization gap.  Under an NTK separability condition, the results of the paper (with smooth activations) lead to a better bound on the test loss then previous results with ReLU activation functions ($\sqrt{\frac{m}{n}}$ is replaced with $\frac{1}{n}$). Furthermore, on the specific problem of a d-dimensional XOR distribution, using quadratic activations with a large step size, only log(d) iterations (and constant width) are needed to obtain perfect test accuracy with n = O(d) samples. An experiment also confirms the logarithmic dependency on data dimension.

### Strengths
-The paper is clearly written and well organized.

-The paper provides novel convergence and generalization bounds for neural networks with smooth activations, which are significantly better than prior bounds derived for ReLU networks (the test loss bound obtained is width independent). This is important for understanding how generalization of neural networks with smooth activations compares to generalization of ReLU neural networks.

-The result showing efficient learning for the XOR problem with linear sample complexity is a notable contribution.

### Weaknesses
 -Experiments on deep networks are done on a small neural network. Also, the expectations over S are estimated with one realization of S.

-The method to bound the spectral norm of the Hessian based on the distance from initialization is not new, limiting the novelty of the approach.

-The paper does not clarify whether the improved bounds are fundamentally due to the smoothness of the activation functions or if they result from limitations in the proof techniques used in previous bounds for ReLU networks, which may have led to weaker results in the non-smooth case.

### Questions
1) Do you think that the bounds holding for ReLu networks could be improved to match the bounds of your paper, or is the smoothness assumption necessary to obtain the improvement?

2) Could you clarify the main novel techniques or approaches used in the proofs of your main results, particularly in relation to previous work in this area?

### Soundness
3

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
4

### Summary
This paper studies the training convergence guarantee and the generalization error of deep MLPs with quadratic activation when applied to binary classification tasks. The paper considers the parameterization of the neural network in the NTK regime, and shows a tigher generalization bound together with a smaller over-parameterization requirement compared with previous work. In addition to the analysis of the noiseless separable data scheme, the paper also considers a noisy data scheme and a XOR classification task. In particular, the paper shows that for the XOR classification, using a large step size and effectively escape the NTK regime and learns useful features. The paper also provided experimental results to verify its theoretical conclusion.

### Strengths
1. The paper obtains a tigher bound on the generalization error compared with previous work. In particular, while previous work usually achieves a $O(\frac{1}{\sqrt{n}})$ generalization error, this paper achieves a $O(\frac{1}{n})$ error.

2. In the noiseless data scheme, the paper derives favorable convergence guarantee under only a constant over-parameterization requirement.

3. The paper has a nice extension of their theoretical work from the noiseless data scheme to the noisy data scheme as well as the XOR classification task.

### Weaknesses
1. In Theorem 2.1, the over-parameterization requirement scales with $\Omega(\rho^{*6L+4})$. Later in the discussion, the paper stated $\rho = O(\log n / \gamma)$, where $\gamma$ is the margin width. When we treat $L$, the network depth, not as a constant, the over-parameterization requirement can be as large as $\Omega(\frac{(\log n)^{6L+4}}{\gamma^{6L+4}})$, which might be unfavorable. This exponential dependence on the depth $L$ makes the result less practical for deep networks, where $L$ can be quite large. The bound becomes meaningful only when the depth is relatively small, limiting the scope of the theoretical analysis.

2. The setting studied in the paper are not clearly explained, and some notations are not introduced before use. For instance, it is not clear what is $\mathcal{S}$ is in Eq.(5), and what it means to take expectation over it. Moreover, in Section 2.1.2, it is not clear how the noise in the data are generated. The lack of clarity regarding the training set $\mathcal{S}$ and the expectation operation makes it difficult to fully grasp the implications of the generalization bound. Additionally, the absence of a precise description of the noise generation process in Section 2.1.2 hinders the reproducibility and understanding of the results.

3. In Assumption 1, the separability condition is defined over the tangent feature at initialization. Because the separability is defined in this random feature model, it would naturally imply an implicit lower bound on the over-parameterization: for instance, the more parameters we have, the more random features we will have, and a higher probability the data will be separable when mapped to the feature space. This assumption, while common, obscures the true relationship between network width and separability. The implicit dependence on over-parameterization makes it difficult to isolate the impact of the proposed method from the effects of simply having a large number of parameters.

4. Some theoretical results seems confusing; see Questions below.

### Questions
1. In Eq. (5), consider the special case of $n=1$, where we have only one sample. Suppose we initialize $w_0$ at $w^\star$ and suppose $w^\star$ achieves zero training error. Then by Eq. (5), the generalization error will be $0$. This means that even in the case where we have only one trainig sample, every neural network parameter that achieves zero training error will generalize well, which is counter-intuitive. Am I missing something here?

2. In Eq. (6), plugging in $\hat{F} \leq \frac{4\rho^{*2}}{\eta T}$, should we have an additional $\log T$ on the right-hand side due to a summation of $\frac{1}{t}$ for $t = 1,\dots, T-1$?

3. In the cited paper Lei and Ying (2020), I did not found Lemma B.3, which is used in the proof of the generalization error. Is the paper referring to a different lemma? Also, it seems that the leave-one-out error in Lei and Ying is defined by replacing the $i$th sample with another random sample, not deleting the $i$th sample.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the data-dependent convergence and generalization of gradient methods in neural networks with smooth activations. The authors provide a tighter, algorithm-dependent bound on excess risk for deep networks trained with logistic loss, improving on Rademacher complexity-based bounds. These results emphasize the role of initialization, particularly in small-width networks and margin-separable data.

### Strengths
Overall, the contribution of this paper is great filling the gap between practice and theory.

### Weaknesses
1.	Table in page 2 is mis-labeled as Table 2. 
2.	The authors claim that leveraging the Hessian structure in the gradient descent path is the key for their theoretical improvements over the past literature. But I feel the mathematical intuition is not well stated in the main paper. When it is compared with the previous literature (for instance Chen et al, 2021), how does considering the hessian structure benefit the author to prove Theorem 2.1? 
3.	In least-squares regression, the Neural Tangent Kernel (NTK) benefits from the fact that gradient descent keeps weight updates close to their initialization, which linearizes the dynamics in parameter space and makes the analysis more tractable. I suspect this approach will similarly apply to classification tasks if the authors use the NTK framework. Given this, the role of initialization mentioned in the main paper isn't particularly surprising. Could the authors elaborate on the unique insights that arise when studying classification problems, which might not be evident when analyzing regression problems, specifically in terms of the role of initialization?
4.	Somehow, I felt Subsection 2.2 is disconnected to the remaining part of the paper, as the problem settings seem to be different from the previous parts. I suspect this is because of technical difficulties authors might have encountered, but it would be great if authors can make connections between this Subsection and previous parts. For example, how are the particular techniques from earlier sections linked to the XOR distribution analysis in 2.2?
5.	In Theorem 2.4, the step size is equal to the width of the network. Can it be arbitrarily large? Are there any restrictions on the step size?

### Questions
1.	Table in page 2 is mis-labeled as Table 2. 
2.	The authors claim that leveraging the Hessian structure in the gradient descent path is the key for their theoretical improvements over the past literature. But I feel the mathematical intuition is not well stated in the main paper. When it is compared with the previous literature (for instance Chen et al, 2021), how does considering the hessian structure benefit the author to prove Theorem 2.1? 
3.	In least-squares regression, the Neural Tangent Kernel (NTK) benefits from the fact that gradient descent keeps weight updates close to their initialization, which linearizes the dynamics in parameter space and makes the analysis more tractable. I suspect this approach will similarly apply to classification tasks if the authors use the NTK framework. Given this, the role of initialization mentioned in the main paper isn't particularly surprising. Could the authors elaborate on the unique insights that arise when studying classification problems, which might not be evident when analyzing regression problems, specifically in terms of the role of initialization?
4.     Somehow, I felt Subsection 2.2 is disconnected to the remaining part of the paper, as the problem settings seem to be different from the previous parts. I suspect this is because of technical difficulties authors might have encountered, but it would be great if authors can make connections between this Subsection and previous parts. For example, how are the particular techniques from earlier sections linked to the XOR distribution analysis in 2.2?
5.	In Theorem 2.4, the step size is equal to the width of the network. Can it be arbitrarily large? Are there any restrictions on the step size?

### Soundness
3

### Presentation
3

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
This paper studies convergence and generalization for deep neural networks with smooth activation trained by gradient descent. This paper shows several improved results on test error compared with previous works for the following scenarios: (1) noiseless data with separable NTK feature, and (2) noisy data and (3) XOR distribution.

### Strengths
This work presents several improved results from prior works. In particular, the authors are able to show an improved bound on the network width by requiring $\lvert w^\star - w_0 \rvert \lesssim m^{O(1/L)}$, which implies that the NTK regime can happen under a far more relaxed conditions than what previous work suggested. Such results can be important and interesting. The authors then utilize this improvement to derive improved bounds for several classical NTK settings like NTK separable data and noisy data.

### Weaknesses
Although the results in this work are impressive, a more detailed description on how the authors achieved this improvement is needed. In particular, the authors mentioned in line 84, 85 that the reason for the improvement in the network's width is by exploring the objective's Hessian structure in the gradient descent path. This sounds very interesting. However, I didn't find any high level discussion/description on this in the main text. I would like the authors to explain how they get this improvement. How does your analysis compare with the prior work that also utilized the Hessian structure? What is the novelty in your analysis such that you can achieve this improvement? Specifically, what are the key properties of the Hessian that are exploited? Are these properties specific to the smooth activation functions considered, or would they generalize to other activation functions? Furthermore, how does the analysis handle the non-convexity of the loss landscape, and what are the implications of this for the practical applicability of the results?

### Questions
None.

### Soundness
3

### Presentation
2

### Contribution
3
