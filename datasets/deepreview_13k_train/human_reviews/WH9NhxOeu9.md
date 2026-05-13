# Sharp Generalization for Nonparametric Regression by Over-Parameterized Neural Networks: A Distribution-Free Analysis

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
Sharp generalization bound for neural networks trained by gradient descent (GD) is of central interest in statistical learning theory and deep learning. In this paper, we consider nonparametric regression
by an over-parameterized two-layer NN trained by GD. We show that, if the neural network is trained by GD with early stopping, then the trained network renders a sharp rate of the nonparametric regression risk of $\cO(\eps_n^2)$, which is the same rate as that for kernel regression trained by GD with early stopping, where $\eps_n$ is the critical population rate of the Neural Tangent Kernel (NTK) associated with the network and $n$ is the size of the training data. It is remarked that our result does not require distributional assumptions on the training data, in a strong contrast with many existing results which rely on specific distributions such as the spherical uniform data distribution or distributions satisfying certain restrictive conditions.
As a special case of our general result, when the eigenvalues of the associated NTK
decay at a rate of $\lambda_j \asymp j^{-\frac{d}{d-1}}$ for $j \ge 1$ which happens if the training data is distributed uniformly on the unit sphere in $\RR^d$, we immediately obtain the minimax optimal rate of
$\cO(n^{-\frac{d}{2d-1}})$, which is the major results of several existing works in this direction. The neural network width in our general result is lower bounded by a function of only $n,d,\eps_n$, and such width does not depend on the minimum eigenvalue of the empirical NTK matrix whose lower bound usually requires additional assumptions on the training data.
Our results are built upon two significant technical results which are of independent interest. First, uniform convergence to the NTK is established during the training process by GD, so that we can have a nice decomposition of the neural network function at any step of the GD into a function in the Reproducing
Kernel Hilbert Space associated with the NTK and an error function with a small $L^{\infty}$-norm. Second, local Rademacher complexity is employed
to tightly bound the Rademacher complexity of the function class comprising all the possible neural network functions obtained by GD.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies nonparametric regression using overparameterized ReLU feed-forward neural network with one hidden layer in a neural tangent kernel (NTK) regime. 

The input features $(\vec{x_i})_{i=1}^n$ are assumed to come from a $d$-dimensional sphere. 

The labels of the regression task $(y_i)_{i=1}^n \in \mathbb{R}$ are generated using a ground truth function that lies in a RKHS associated with the NTK, perturbed with zero-mean Gaussian noise. This paper proves that when the neural network is trained with GD with respect to square loss with early stopping, it achieves a convergence rate of loss of order $\mathcal{O}(\varepsilon_n^2)$, where $\varepsilon_n$ is the critical population
rate of the NTK associated with the network, and $n$ is the
number of the training data. Remarkably, such risk bound is attained without any distributional assumption of data. The authors show that the risk bound is minimax optimal under some special cases and recovered results obtained by previous papers (Hu et al., 2021; Suh et al., 2022; Li et al., 2024).

### Strengths
- Overall, this paper is well-written, has a good flow, and I believe it presents very solid theoretical results. 
-  This paper contributes by providing a more general result in nonparametric regression by neural networks trained with GD with early stopping. It improves the prior results in the literature in the sense that (1) they present a distribution-free risk bound while existing results require at least a uniform distribution assumption on the data; (2) they give an explicit characterization of the distribution-free stopping  $\widehat{T}$, which is of order $\widehat{T} \asymp \varepsilon_n^{-2}$; (3) they present a lower bound of network width which depends only on $d$ and $\varepsilon_n$; (4) their theory holds for simply employing constant learning rate in GD.

### Weaknesses
I am not fully convinced of the novelty of the results. To better emphasize their contributions, the authors should consider elaborating on the technical methods used to derive the risk bound, particularly in terms of how they relax the uniform distributional assumptions on the data. While the roadmap of proofs in Section 6 provides a good overview of the proof procedures, the authors should further highlight the novelty of their proof by answering the question, ``Why are our methods able to yield a distribution-free risk bound where others (Hu et al., 2021; Suh et al., 2022) have not?'' Specifically, the current discussion lacks a detailed comparison of the specific mathematical techniques employed in this work versus those used in prior analyses. For instance, it would be beneficial to understand how the authors' approach to bounding the Rademacher complexity differs from existing methods in the context of neural networks, and how these differences allow them to circumvent the need for distributional assumptions. The paper should also delve deeper into the specific properties of the neural tangent kernel (NTK) that make this distribution-free result possible, and how these properties are exploited differently from previous analyses.

### Questions
See Weaknesses

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
This paper considers the generalization of a 2-layer NN trained with early stopping in the NTK (kernel) regime for *arbitrary* distributions. It is known (Raskutti et al. 2014) that a kernel model trained with GD with early stopping on $n$ samples from an arbitrary distribution can achieve the risk $\epsilon_n^2$, where $\epsilon_n$ is the "critical population rate" which relates to the local Rademacher complexity.  The novelty in this paper is showing this for finite-width 2-layer NNs, where the width is only required to grow polynomially in the ambient dimension $d$ and in $\epsilon_n$. 

This result is then applied to yield a risk bound of $n^{-d/(2d - 2)}$ for uniformly distributed covariates --- which are known to yeild a certain polynomial eigenvalue decay rate (EDR)  of the Kernel --- recovering the rate achieved in several other works. The advantage of this work is that it holds if this EDR holds regardless of distributional requirements. The uniformly distributed covariate case, along with another distributional assumptions priorly studied, lead to the EDR holding.

### Strengths
This paper gives a cleaner and more unified analysis of early stopping for the NTK which works for arbitrary distributions. In comparison to other results that study the same polynomial EDR, this result on requires a *weaker* assumption on the width.

### Weaknesses
The contribution in this work seems marginal, because the convergence of 2-layer NNs in some regimes to the NTK is well-studied, and thus it is unsurprising given the early stopping result for kernels from Raskutti et al. 2014 that this same result could be achieved for NNs.
- I am not sure what the technical difficulty or novelty is of proving the convergence to the NTK in this particular regime is --- can Theorem 6.1 not be proven using existing results on the converge of NNs to the NTK kernel?
-  Further, for the second half of the proof involving generalization given the uniform convergence to the kernel, can the results of Raskutti et al. 2014 not be used as a black box? If not, what new technical tools are required to prove generalization?

Better comparison to related work needed.
- There are many comparisons to work specifically on the EDR results, but there is no discussion on general results on convergence to the NTK and how this results compares or improves upon those results.

The paper is not written clearly
- Many details are undefined/left out:
  - The fact that the network activations are relu was never mentioned
  - When the kernel K is defined in equation (2), it is unclear what this Kernel is associated with. I would have expected it to associated with the finite width network, but I think it is actually an infinite width relu network?
  - When "critical population rate" and "critical radius" are first mentioned (page 4), they should be defined (or there at least should be a link to the definition later in the paper).
  - In link 180 $f_0$ is not defined.
  - Line 232 what is s?
  - Line 462 what is $\kappa$?
- The theorems are not clearly written. It would be much clearer to say something like: "Let $\hat{T} := BLAH$. Then for any $t \in [c\hat{T}, C\hat{T}]$, the following holds...". It is hard to parse what is currently written.
- The roadmap of the proof given in Figure 1 is very had to make sense of, becaue not all of the Lemmas/theorems in the diagram are explained and stated. Even if they are mentioned in the text, it is very breif, and it is not clear if they are technically novel. And where does Theorem 6.1 appear in the the diagram? The authors should choose a few of their key lemmas and theorems, state them, and explain how they are stichted together. The current "summary" just briefly mentions (some of) the lemmas, but too many lemmas are mentioned, and not enough details are given.

### Questions
See above

### Soundness
3

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
This paper investigates the excess risk of two-layer neural networks trained in the so-called NTK regime. While existing works impose some restrictive distributional assumptions, this paper derives a bound that is distribution-free and admissible for any eigenvalue decay rate. The derived bound includes an existing result on the minimax optimality of the neural networks in the NTK regime with a slight improvement of the bound on the network width.

### Strengths
As distributional assumptions are often imposed in deep learning theory literature, including the NTK-type analysis, the distribution-free analysis is of significant interest, and this paper provides a novel result. The writing of this paper provides a detailed explanation of theoretical outcomes and comparisons to existing literature, which makes the paper more accessible for readers to follow.

### Weaknesses
While the distribution-free analysis exhibited in this paper has a novelty in the NTK-type analysis literature, I have several concerns about the theoretical results as follows:

- While the authors relax the distributional assumption, the domain is still limited to $\mathbb{S}^{d-1}$, a unit sphere in $\mathbb{R}^d$, which still can be seen as a distributional assumption. The restriction to the unit sphere, while common, limits the practical applicability of the results. Many real-world datasets do not naturally reside on a sphere, and while normalization is possible, it can distort the underlying data structure and potentially affect the performance of the model. The theoretical analysis should ideally be extended to more general bounded domains, or at least provide a clear justification for why the spherical domain is a reasonable assumption for the specific problem being addressed. Furthermore, the impact of the normalization process on the derived bounds should be discussed.

- The constant learning rate, which the authors refer to as the advantage of their analysis, is also obtained in [1] while they treat the stochastic gradient descent. The authors may need to refer to the comparison with this paper.

	[1] Atsushi Nitanda and Taiji Suzuki, “Optimal Rates for Averaged Stochastic Gradient Descent under Neural Tangent Kernel Regime”, ICLR2021.

- (minor) While I imagine the authors treating ReLU activation throughout the analysis, section 2 does not refer to that.

### Questions
Besides the questions listed in the **weakness** part, I have the following question:

- The authors derive the result about the minimax optimality of the NTK regime shown in (Hu et al., 2021; Suh et al., 2022; Li et al., 2024) as an example. Could the authors provide other suggestive examples derived from Theorem 5.1?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides generalization bounds for overparameterized two-layer neural networks (NNs) with early stopping without making assumptions on the covariate distribution, except being supported on the unit sphere. The proof shows uniform convergence to the NTK and bounds the Rademacher complexity of the function class that is learned by the NNs.

### Strengths
This paper poses weaker assumptions on the covariate distribution, in particular no assumptions on the NTK’s eigenvalue decay rate, than previous works like Suh et al. (2022) or Li et al. (2024), which is a significant contribution.

The results suggest that the required network width can be estimated from data by estimating the NTK’s eigenvalue decay rate (EDR). However, a successful estimation of the EDR or of the required network width is not shown, neither empirically nor theoretically.

### Weaknesses
Overall, I believe this paper requires a significant revision and should be rejected, due to the following severe weaknesses:

- **Overstatement.** One of the main strengths that the authors claim is that their analysis is “distribution-free”.  This is an overstatement. While the assumptions on the covariate distribution are weak (that it should be supported on $\mathcal{X}=S^{d-1}$, in particular this implies that the covariates have compact, bounded support), the assumptions on the conditional distribution y|x are quite strong. In particular, the Bayes optimal function should lie in the NTK’s RKHS with low norm and the label noise is iid Gaussian. At no point in the paper is the claim of “distribution-free” qualified. For example, in the Abstract, the authors write “our result does not require distributional assumptions on the training data”, which is just wrong. The assumption that the Bayes optimal function lies in the RKHS with a bounded norm is a substantial restriction, as it implies a smoothness constraint on the target function that may not hold in practice. Furthermore, the requirement of i.i.d. Gaussian noise is also quite limiting, as real-world data often exhibits heteroscedastic or non-Gaussian noise patterns. These assumptions severely restrict the applicability of the results.
- **Artificial Setting.** Only first-layer weights of a 2-layer NN without biases are trained with GD and the anti-symmetric initialization trick is used. The comparable papers Suh et al. (2021) and Li et al. (2024) treat training all layers of L-hidden layer MLPs. Du et al. (2019) also discusses training both layers. The authors do not make sufficiently transparent in which ways this paper poses stronger assumptions or analyses more artificial settings than previous work that trains all layers, uses SGD (Allen-Zhu et al.,2019) or that poses weaker assumptions on y|x (Haas et al., 2024). The restriction to training only the first layer significantly simplifies the analysis but at the cost of practical relevance. Training only the first layer might not capture the full potential of feature learning in deep networks, and the antisymmetric initialization, while simplifying the analysis, is not a standard practice in training neural networks. The paper fails to adequately justify why this specific setup is chosen and how it relates to more realistic training scenarios.
- **Related work** has not been sufficiently acknowledged. In particular:
    - The antisymmetric initialization trick used in this work has been previously used in the literature, e.g. Zhang et al. (2020).
    - It is never mentioned that uniform convergence to the NTK has previously been shown.
    - The statement in lines 50-53 is imprecise. It is only correct under the neural tangent parameterization. Yang and Hu (2021) have shown that there are parameterizations such that NNs do learn features even in the infinite-width limit.
    - In lines 69-71, it is claimed that previous studies that achieve minimax optimal rates with overparameterized NNs impose strong distributional assumptions. Theorem G.5 from Haas et al. (2024) achieves minimax optimal rates up to log terms under a weak covariate assumption in the overparameterized limit. In particular, there $f^*$ may also lie outside of the NTK’s RKHS, which is much less restrictive than the boundedness assumption on the RKHS norm here, and label noise does not have to be Gaussian. The paper does not adequately position its contributions with respect to existing literature, especially regarding the assumptions on the target function and noise model. The claim about strong distributional assumptions in other works is misleading, as some existing works achieve minimax rates with weaker assumptions on the target function and noise.
- **Missing experiments.** While not necessary, experiments to quantify finite-width and finite-sample relevance of the derived bounds would be a valuable addition. E.g. Du et al. (2019) provide minimal experiments. Useful experiments could evaluate for increasing n:
    1. What is empirically the optimal stopping time $\hat T_{emp}$? Does the theoretically predicted $\hat T$ coincide at least in the rate?
    2. Does the generalization error decay with the predicted rate, for one typical covariate distribution, like uniform on the sphere, and one which does not satisfy the stronger assumptions in other works?
    3. Is the predicted necessary scaling of $m$ tight or can it be chosen even smaller? The lack of experimental validation makes it difficult to assess the practical relevance of the theoretical results. The paper should include at least some basic experiments to demonstrate the behavior of the proposed method in finite-sample regimes and to verify the tightness of the theoretical bounds.
- **Unpolished writing.** Throughout the paper, some descriptions are lengthy, repetitive or little informative. For example, the description in Section 6.2 could be shortened, and instead of only describing what has been done in the proofs, it could shortly be explained *how* it was possible to show uniform convergence to the NTK and to bound the local Rademacher complexity. Figure 1 would only be helpful, if it also contained what the respective results in the appendix say.

**Things to improve the paper that did not impact the score:**

- The notation $f_0$ is confusing. It would usually denote a function, not a constant.

**Typos:** 264: first, 363: small t in the minimum?, 379-380: several mistakes.

### Questions
- Can you provide a short sketch or a short overview how it was possible to show uniform convergence to the NTK and to bound the local Rademacher complexity?
- In which ways does the analysis differ from previous analyses?

### Soundness
2

### Presentation
2

### Contribution
2
