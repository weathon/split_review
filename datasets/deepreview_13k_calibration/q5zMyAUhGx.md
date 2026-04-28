# Generalization Bounds and Model Complexity for Kolmogorov–Arnold Networks

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 6, 5, 6

## Abstract
Kolmogorov–Arnold Network (KAN) is a network structure recently proposed in \cite{liu2024kan} that offers improved interpretability and a more parsimonious design in many science-oriented tasks compared to multi-layer perceptrons. This work provides a rigorous theoretical analysis of KAN by establishing generalization bounds for KAN equipped with activation functions that are either represented by linear combinations of basis functions or lying in a low-rank Reproducing Kernel Hilbert Space (RKHS). In the first case, the generalization bound accommodates various choices of basis functions in forming the activation functions in each layer of KAN and is adapted
to different operator norms at each layer. For a particular choice of operator norms, the bound scales with the $l_1$ norm of the coefficient matrices and the Lipschitz constants for
the activation functions, and it has no dependence on combinatorial parameters (e.g., number of nodes) outside of logarithmic factors. Moreover, our result does not require the boundedness assumption on the loss function and, hence, is applicable to a general class of regression-type loss functions.
In the low-rank case, the generalization bound scales polynomially with the underlying ranks as well as the Lipschitz constants of the activation functions in each layer. These bounds are empirically investigated for KANs trained with stochastic gradient descent on simulated and real data sets. The numerical results demonstrate the practical relevance of these bounds.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work addresses a gap in the current research on Kolmogorov–Arnold Networks (KANs) by (i) quantifying the complexity of KANs, and (ii) establishing high probability upper bounds of excess risk in regression task. Specifically, this work studies two special classes of KAN: (i) KAN with activation functions represented by basis functions, and (ii) KAN with activation functions on the RKHS induced by Matern kernel.

### Strengths
- I found the paper well-written, has a good flow, and I believe it presents very solid theoretical results.
- The theoretical results are novel as they present the first generalization error bound and complexity estimate of KAN.
- Frankly, KAN is an "interesting" yet "contentious" topic in the machine learning community ---   "interesting" in the sense that it has caught a lot of attentions and discussions in the community; "contentious" in the sense that it hasn’t achieved broad acceptance or visibility, especially since all the cited KAN-related papers (including the very first KAN paper (Liu et al. 2024)) have not been published in major machine learning venues. I believe this paper contribute to the theoretical understanding of KAN by estimating the excess risk in regression setting of two special classes of KAN. Although the current results are insufficient to conclude whether KAN achieves better generalization performance than traditional MLPs, they provide valuable insights that can encourage the community to further investigate the potential advantages and impact of KAN.

### Weaknesses
 -  I find the purpose of the numerical experiments in Section 3 unclear. Are these experiments used to corroborate the complexity result in Theorem 1? If so,  are the activation functions in the implemented KAN chosen to be linear combination of basis functions? It's not clear if the experiments are designed to validate the theoretical claims about the complexity measure, or if they serve a different purpose entirely. The connection between the experimental setup and the theoretical results needs to be explicitly addressed. Specifically, if the activation functions are indeed linear combinations of basis functions, the specific choice of basis functions and their impact on the results should be discussed.
- Can the authors comment further on the convergence rate of excess risk established in Corollary 1 and Corollary 2? What does the parameter $s$ represent? Also, how do these convergence rates compare to that of traditional MLP (say, ReLU feed-forward neural network)? Do we observe any advantage in the generalization of regression by using KAN? The current discussion of the convergence rates is insufficient. A more detailed explanation of the parameters, especially $s$, is needed. Furthermore, a direct comparison with the convergence rates of standard MLPs is crucial to understand the practical implications of the theoretical results. The paper should also clarify whether the derived bounds suggest any practical advantage of using KANs over MLPs in regression tasks.
- It appears that Section 2.3 only considers RKHS induced by Matern kernel, instead of a general low-rank RKHS. Because of the equivalence between this specific RKHS and Sobolev space, would it be a better idea to change the title of Section 2.3 to ``Activation functions on Sobolev space"? The restriction to the Matern kernel-induced RKHS is a significant limitation. The authors should justify this choice or extend the analysis to a more general class of low-rank RKHS. Given the connection to Sobolev spaces, renaming the section could indeed be more accurate and informative, but this does not address the fundamental limitation of the analysis.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the generalization capability of Kolmogorov-Arnold Networks (KANs). Specifically, the authors estimated the covering number under certain regularity assumptions and derived the generalization gaps (Theorems 2 and 3) and the excess risk bound (Corollary 1). Additionally, they examined the case where the activation function belongs to a Reproducing Kernel Hilbert Space (RKHS) with a low-rank structure, proving the generalization gaps (Theorems 4 and 5) and the excess risk bound (Corollary 2) that leverage this structure. Experiments validate the relevance of the theoretical bounds to the observed excess risk.

### Strengths
KANs, inspired by the Kolmogorov-Arnold representation theorem, have gained attention for potentially efficient parameterization compared to MLPs. However, their statistical performance remains unclear, despite numerous attempts to develop more sophisticated structures and applications. To the best of my knowledge, this is the first work to derive generalization bounds for KANs.

### Weaknesses
 - Assumption 1 presumes the uniform boundedness of the dataset. Typically, this bound scales with $\sqrt{n}$, which could degrade the derived bounds.

- Although KANs are expected to demonstrate superior approximation capability due to their inherent nature, there is no comparison with other models such as MLPs. The paper lacks a clear theoretical or empirical demonstration of when KANs might be preferred over MLPs. Specifically, the generalization bounds derived for KANs are not directly compared to existing bounds for MLPs, leaving the reader without a clear understanding of the relative advantages or disadvantages of KANs from a statistical learning perspective.

### Questions
- Based on the obtained theory, is it possible to identify a problem setting where KANs outperform MLPs?

- How tight are the obtained results? Is it feasible to derive lower bounds on generalization gaps and excess risk bounds in a simple setting?

- Can you discuss the approximation (representation) capabilities of KANs for certain function classes? This type of approximation analysis is often necessary for fully understanding the statistical performance of the model.

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
4

### Summary
This paper investigates the generalization ability of Kolmogorov-Arnold Networks (KAN). Multiple generalization bounds are provided for both bounded and unbounded loss functions, which may help understanding how the network complexity impacts the generalization behavior of KANs. The results are further extended to the cases where activation functions belong to RKHS, and empirical results are given to demonstrate the relationship between performance and network complexity.

### Strengths
This paper provides multiple generalization bounds for both bounded and unbounded loss functions, which may help in understanding how the network complexity impacts the generalization behavior of KANs.

### Weaknesses
 * It is consensus that traditional complexity measures (e.g. Rademacher complexity or covering numbers) are not sufficient to explain generalization for deep networks. As the analysis of this paper heavily relies on these metrics, the derived bounds are likely vacuous in practice.
* The theoretical analysis relies on tons of strong assumptions (e.g. Lipschitzness, boundedness) for almost every single part of the network (input, function space, loss function). To what extent these assumptions can be met in practice needs more clarification.

### Questions
* Could the authors provide some empirical results on the comparison between the bounds and the actual generalization error? This would help convince me that these bounds are indeed non-vacuous in practice.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies generalization bounds for Kolmogorov–Arnold Network (KAN) using covering numbers (through Rademacher complexity). The authors further present a quantity $\alpha$ which they dub the network complexity and show empirically this measure qualitatively follows the excess risk.

### Strengths
**Originality**. The contribution seems to be novel. To the best of my knowledge, this is the first work to present generalization bounds for KANs.

**Quality**. The theoretical contribution seems to be sound.

**Clarity**. The paper is well organized.

**Significance**. KANs have attracted much attention from the community lately and theoretical contributions would be very welcome.

### Weaknesses
 **Clarity**. While the flow of the paper is clear, I wish technical results were complemented by an intuitive discussion. Specifically,
- The third point under main contributions claims “The results shed new light on how the performance of KANs is affected by the underlying network structure and the network complexity.” However, this point is never presented or discussed in the paper.
- Empirical results lack discussion completely.

**Quality**. The empirical results should be more comprehensive and include more details.
- Some very particular choices are made for the synthetic target functions, however, they are never motivated or explained.
- The performance of the networks (loss/accuracy rather than excess loss) is never presented. This is important in order to evaluate whether the regime the authors present in their result is an interesting one or not.
- The paper does not include empirical results for the generalization bounds. It would be of great interest to the reader to see whether the bound is tight.
- The tightness of the bound is never discussed.
- I would expect an appendix with details of the experiments. Specifically, the “normalization” procedure for the complexity measure is never explained.

**Significance**. The significance of the result largely depends on the tightness of the bound, but it is never discussed or examined.

*Nits*:
- The appendices are never referenced. I would expect them to be referenced when relevant.
- The text in the figures is barely readable at any reasonable “zoom” level.

### Questions
- For the CIFAR-10 and MNIST experiments, why did the authors choose to run the experiments on top of the features of AlexNet instead of the “raw” input? How would that change the results presented in the paper?
- Figure 2 presents the excess loss and the “normalized” complexity measure as a function of the training time, however, it is never stated explicitly how the complexity measure depends on the training time. Am I correct that this dependence comes from the network parameters $B_i$? What are the values of $B_i$ used for the plot? Is it the $\ell_1$ norms of $\mathbf{B}_i$?
- Is it true that the theoretical results do not hold for cross-entropy loss? Can the authors comment on that in light of the use of cross-entropy loss in the experiments? 
- Can the authors provide an intuitive explanation for the role played by the value of $\phi$ evaluated at $0$ (and the constant $C$)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents generalization bounds for KANs, where the activation functions are learned from the datasets. The paper considers activation functions that are eighter represented by linear combinations of basis functions or lying in a low-dimensional RKHS. The paper presents generalization bounds based on covering number analysis under some assumptions on the Lipschitzness of the activation functions and the l1-norm on the coefficients. The paper further shows that the analysis can be extended to unbounded loss functions, which can be applied to general regression loss functions. Experimental results are also given to verify the theoretical findings.

### Strengths
KANs have found various applications in many scientific and engineering problems. The paper gives solid generalization analysis for KANs. The derived generalization bounds clearly show how the parameters affect the generalization, including the Lipschitzness and l1-norm constraint on the coefficients.

### Weaknesses
 - The technical contribution seems to be limited. As far as I see, the theoretical analysis follows from existing covering number estimates of fully-connected neural networks [R1]. The idea is to build a recursive relationship of covering number estimates for neural networks with different layers (Proposition 1), which shares similarity to Lemma A.7 in [R1]. Furthermore, Proposition 2 also essentially similar to Lemma 3.2 in R1.


- The paper also gives generalization bounds for learning with unbounded loss functions. However, the results admit some drawbacks. First, the bound in Theorem 3 has a linear dependency $1/\eta$, where $\eta$ is a confidence parameter. This is much worse than the logarithmic dependency. Therefore, the results for unbounded loss functions are not with high probability. Indeed, they are just derived by truncating the prediction followed by Markov's inequality. Second, the bound involves $n^{(1-s)/(2s)}$ and would be much worse than the case with bounded loss function ($n^{-1/2}$). For example, if $s=2$, then the bound in Theorem 3 is of the order of $n^{-1/4}$.




R1: Bartlett, P.L., Foster, D.J. and Telgarsky, M.J., 2017. Spectrally-normalized margin bounds for neural networks. Advances in neural information processing systems, 30.

### Questions
- It would be nice if the authors can included a detailed discussion on the technical challenge in the covering number estimates of the KANs. Especially, the authors should clarify the novelty of the theoretical analysis.



- Is it possible to give high-probability generalization bounds for unbounded loss functions.

- There is a lacking discussions of the generalization bounds for KANs with those for fully connected networks. Is there a clear advantage on the generalization behavior by theoretical analysis in the paper?

Minor point:

- $\mathcal{F}$ in Proposition 2 is not defined.

### Soundness
3

### Presentation
3

### Contribution
2
