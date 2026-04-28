# Divergence of Neural Tangent Kernel in Classification Problems

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
This paper primarily investigates the convergence of the Neural Tangent Kernel (NTK) in classification problems. This study firstly show the strictly positive definiteness of NTK of multi-layer fully connected neural networks and residual neural networks. Then, through a contradiction argument,  it indicates that, during training with the cross-entropy loss function, the neural network parameters diverge due to the strictly positive definiteness of the NTK. Consequently, the empirical NTK does not consistently converge but instead diverges as time approaches infinity. This finding implies that NTK theory is not applicable in this context, highlighting significant theoretical implications for the study of neural networks in classification problems. These results can also  be easily generalized to other network structures, provided that the NTK is strictly positive definite.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper considers the convergence of the neural tangent kernel of fully-connected ReLU networks and ResNets for classification problems trained with cross-entropy loss functions.  The key result of the paper is a proof that, during training (in the gradient-flow approximation), the network parameters diverge due to the strict positive definiteness of the NTK, implying that many results from NTK theory may not be applicable in this context.

### Strengths
The result appears to be sound and certainly has relevance insofar as it demonstrates the non-applicability of many NTK results in a common scenario (training with cross-entropy).  The presentation is mostly readable and the derivation appears to be correct, though admittedly I did not dive too deeply into the appendices, and certainly the material appears novel (at least to me).

### Weaknesses
While I don't question to novelty of the result in literature, I don't necessarily find it too surprising.  To truly minimize the cross-entropy would require $f(x_i,\theta) \to +\infty$ for $y_i=+1$ (and similarly for the other class).  Without regularization and given infinite time, recalling that the NN is a universal approximator in the infinite-width limit, you should expect precisely this, in which light theorem 1 (and subsequently corollary 1 and theorem 2) is to be expected.  Nevertheless it is important to see this intuition proven formally, so I do not consider this a serious criticism.

Minor points - the presentation of the paper could certainly be improved, for example:

- line 163: you don't optimize the parameters with gradient flow.  Gradient flow is used to (approximately) analyze the optimization process.
- line 185: this is badly written.  You already defined $K_t$ in (3.1) - why are you repeating it in (3.3) as though it was new?
- line 283: "...will converges to NTK with probability as width comes to infinity..." Do you mean "will converge with probability 1" or "will converge in probability"?
- Theorem 2: (4.4) is precisely equivalent to (4.3).  Are these meant to refer to different networks (ie should (4.4) be modified to refer to ResNet)?

### Questions
See previous sections.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the divergent properties of neural network kernels (NNK, empirical NTK) in classification problems using the softmax loss. Specifically, it demonstrates that the NTKs of fully connected neural networks and ResNets are strictly positive, and that model outputs and parameters will diverge as long as the NNK is bounded below by a positive constant during training (Theorem 1 and Corollary 1). Additionally, it is shown that, unlike in regression problems, the NNK is not fixed during training (Theorem 2).

### Strengths
- The paper proves the divergence of NNK during training, indicating the inapplicability of NTK theory for regression problems.
- The paper is well-structured and easy to read.

### Weaknesses
 - The divergence result of the NNK is not particularly surprising, as it is evident that parameters and outputs must diverge to minimize standard classification losses such as logistic, softmax, or exponential losses. For example, refer to the following papers:

[D. Soudry, et al] THE IMPLICIT BIAS OF GRADIENT DESCENT ON SEPARABLE DATA. ICLR 2018.

[Z. Ji and M. Telgarsky] The implicit bias of gradient descent on nonseparable data. COLT, 2019.

- Given the scale of $\lambda_0$, which typically degenerates as $n\to \infty$, I am curious about the significance of the deviation $\lambda_0/2n^2$, which goes to $0$ as well.

- The results do not address the convergence of gradient descent. If the positivity of the NNK (Eq. (5.3)) holds, convergence can be shown as in NTK theory, but this requirement seems redundant for classification problems. The NTK separability assumption, a weaker condition than positivity, is sufficient for proving the convergence of gradient descent. See the following papers for details:

[A. Nitanda, G. Chinot, and T. Suzuki] Gradient descent can learn less over-parameterized two-layer neural networks on classification problems. 2019.

[Z. Ji and M. Telgarsky] Polylogarithmic width suffices for gradient descent to achieve arbitrarily small test error with shallow relu networks. ICLR 2020.

[H. Taheri and C. Thrampoulidis] Generalization and Stability of Interpolating Neural Networks with Minimal Width. JMLR 2024.

- These related works are not discussed in the paper. 

- (Minor) 
A few typos: (1) Line 110: $f(x_1, f(x_2),$ (2) In the second statement of Theorem 2: Should this be the result for $K_t^{Res}$?

### Questions
- The obtained results rely on the positivity of the NNK. Could you clarify the required conditions (e.g., number of neurons) for this assumption?

- Could you discuss the relationships with the related papers mentioned in the weaknesses?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the convergence properties of the Neural Tangent Kernel (NTK) in classification tasks, with a focus on multi-layer fully connected neural networks and residual neural networks. The authors establish that the NTK of both types of networks is strictly positive definite, a key characteristic for comprehending the training behavior of neural networks. Using a contradiction argument, the authors demonstrate that when employing the cross-entropy loss function, the parameters of the neural network tend to diverge due to the strictly positive definiteness of the NTK. The results imply that NTK theory may not hold in the context of classification problems, leading to significant theoretical implications for understanding the dynamics of neural networks.

### Strengths
1.	The paper provides valuable insights into the behavior of the NTK in classification problems, highlighting a significant divergence from established understandings in regression tasks.

2.	By demonstrating that NTK does not uniformly converge in classification scenarios, the authors identify a critical limitation of NTK theory.

### Weaknesses
1. The claim that current NTK theories might not fully explain generalization properties in classification tasks could be seen as an overgeneralization without comprehensive evidence. A more nuanced discussion on the conditions under which NTK theory might still apply could add depth to the argument. The paper's analysis focuses on the divergence of parameters under cross-entropy loss, but it does not explore scenarios where the NTK might still provide useful approximations, such as in the early stages of training or with specific regularization techniques. The conclusion that NTK theory is fundamentally flawed for classification seems premature without a more thorough investigation into these potential mitigating factors.

2. Although the paper recognizes the need for new theoretical tools, it doesn't provide specific directions or approaches for developing these frameworks. The paper identifies a problem but does not offer any initial ideas on how to address it. For example, it would be beneficial to suggest alternative kernel formulations, modified training procedures, or different analytical techniques that could potentially overcome the limitations of the standard NTK approach. Without these suggestions, the paper leaves the reader with a problem but no clear path forward.

### Questions
1. In Theorem 1, it is assumed that the minimum eigenvalue of the NNK matrix has a lower bound. However, the eigenvalues of the NNK Gram matrix approach zero as the number of training examples increases, as demonstrated in the two papers below. Can this observation offer any insights into NTK theory for classification problems?

[1] Lili Su and Pengkun Yang. On learning over-parameterized neural networks: A functional approximation perspective. In Advances in Neural Information Processing Systems, pp. 2637–2646, 2019.

[2] Atsushi Nitanda and Suzuki Taiji. Optimal rates for averaged stochastic gradient descent under neural tangent kernel regime. In International Conference on Learning Representations, 2021.

2. Could the scope be broadened to incorporate other classification loss functions in order to gain a more comprehensive understanding of NTK behavior?

3. What will happen if the data is completely separable or follows a Gaussian mixture in classification problems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper showed that the multi-layer fully connected neural networks and residual neural networks satisfy the NTK in classification problems. Based on this building, this paper shows the positive definiteness and the convergence of NTK.

### Strengths
This paper is easy to follow.

### Weaknesses
The main contributions of this paper are trivial since the derivation in Eqs. (2.7)-(3.2) is common-used. Besides, the finding that the empirical NTK does not consistently converge but instead diverges as time approaches infinity has been observed by existing studies.


The main claim of this paper is that the neural network parameters will diverge due to the strict positive definiteness of NTK. This is an interpretation, and the core technology behind it is the estimation of strictly positive definite NTK eigenvalues. This is an existing conclusion [1-2]. Therefore, the technical contribution of this paper is not novel, but more like a reinterpretation.

When people talk about a new interpretation of a formula, they should consider what the new interpretation means. I found that there is a statement, "this finding implies that NTK theory is not applicable in this context, highlighting significant theoretical implications for the study of neural networks in classification problems." Unfortunately, this paper does not provide further analysis.

### Questions
Nothing.

### Soundness
2

### Presentation
3

### Contribution
1
