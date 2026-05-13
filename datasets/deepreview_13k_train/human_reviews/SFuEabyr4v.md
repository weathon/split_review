# Controlling Statistical, Discretization, and Truncation Errors in Learning Fourier Linear Operators

- Decision: Reject
- Scores: 1, 6, 6, 6

## Abstract
We investigate the problem of learning operators between function spaces, focusing on the linear part of a layer in the Fourier Neural Operator architecture. First, we identify three main errors that occur during the learning process: statistical error due to finite sample size, truncation error from finite rank approximation of the operator, and discretization error from handling functional data on a finite grid of domain points. Finally, we analyze a Discrete Fourier Transform (DFT) based least squares estimator, establishing both upper and lower bounds on the aforementioned errors.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
Fourier neural operators (FNO) have been widely using in learning nonlinear operators between function spaces. Motivated by FNO, this paper studies a simple case when the FNO is reduced to the composition of a Fourier transform, a learnable linear transform, and an inverse Fourier transform. The goal is to learn a linear operator using this simplified trainable linear operator network. This paper studies the error analysis of this simplified linear operator learning.

### Strengths
This paper is very well written.

### Weaknesses
1) The trainable operator in this paper is too simple to be useful for more general analysis. This is a linear operator and the problem is essentially a linear regression problem in the Fourier domain. This is a well-studied problem. The discretization error related to DFT is a textbook subject in applied harmonic analysis. The generalization error analysis of a linear regression problem is also classical. The only difference is that this paper consider the linear regression with an infinite coefficient vector instead of a finite coefficient vector in textbooks. But the statistical learning error is trivial after the finite truncation with the parameter K in this paper, because after a finite truncation, the infinite coefficient vector is reduced to a finite one and the classical statistical analysis can be directly apply to analyze the error. I don't see any technical challenge to finish the analysis in this paper. It is very straightforward.

2) The proposed method cannot be directly extended to learning nonlinear operators because the main idea is a simple linear regression in the Fourier domain. 

3) The authors missed many important recent development in the error analysis of operator learning. A recent JMLR paper (https://jmlr.org/papers/v25/22-0719.html) has studied a very general error analysis for learning nonlinear operators. When the deep neural network in the JMLR paper is simplied to a linear model, and the encoder and decoder in the JMLR paper is the DFT and inverse DFT, then the analysis there can be directly applied to analyze the problem considered in this paper. 

4) There are other important generalization analysis of operator learning should be dicussed. For examples,
[1] Generalization error guaranteed auto-encoder-based nonlinear model reduction for operator learning, Hao Liu, Biraj Dahal, Rongjie Lai, Wenjing Liao, Applied and Computational Harmonic Analysis Volume 74, January 2025, 101717.
[2] Deep Operator Learning Lessens the Curse of Dimensionality for PDEs. Ke Chen, Chunmei Wang, Haizhao Yang. Transactions on Machine Learning Research, 2023
[3] On the Training and Generalization of Deep Operator Networks. Sanghyun Lee and Yeonjong Shin, SIAM Journal on Scientific ComputingVol. 46, Iss. 4 (2024)

### Questions
I don't have specific questions. I rank this paper mainly based on the problem and setting this paper has.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper is focused on establishing error estimates for operator learning with Fourier neural operators (FNOs). The authors specifically focus on the linear integral operator inherent to the FNO architectures, and establish error estimates for statistical errors (due to finite numbers of samples), truncation errors (from the fact that higher frequency modes are thrown away in the FNO), and a discretization error (arising from the fact that the input functions are sampled on a finite grid). The authors also use the discrete Fourier transform (DFT) to develop a least squares type error estimator that can be bound the other errors both from above and below.

### Strengths
This paper represents an important step in the direction of certifiable and trustworthy operator learning by establishing different error bounds for the FNOs. The authors' exposition is mostly clear, and the connection to other works such as functional data analysis (FDA) is well-highlighted. The authors also make a number of other interesting and insightful observations on the way to their main results; for instance, they use the Mercer decomposition of the kernel to suggest that the FNO's Fourier layers simply parametrize the eigenvalues of a kernel while fixing the eigenfunctions to be complex exponentials/ trigonometric polynomials.

### Weaknesses
1. FNOs use lifting and projection operators (via MLPs). Lifted input functions are fed to the Fourier layers. To the best of my knowledge, the authors' error estimates don't take this lifting into account at all; they are agnostic to it. However, as far as I am aware, it is unclear how the (nonlinear) lifting procedure interacts with the smoothness assumptions the authors place on the input functions to the operator learning problem. If it in fact violates the assumptions (since the lift is learned via an MLP), I suspect the authors' results will break down. This needs to be addressed in the work.

2. The authors assume the input and output spaces to the operator learning problem are both in L^2(T^d,R), rather than the general Banach space setting; the choice of R here is to simplify analysis. However, practical operator learning problems are not usually in the convenient setting of periodic domains like T^d. Typically, the problems of interest are in L^2(R^d, R). Then, for non-periodic input functions, one would expect a fourth error term to come into play with the Fourier layer: a Gibbs-type error term that potentially "pollutes" both the truncation and discretization error terms. This also needs to be addressed. I think the setting in the work is too restrictive.

3. I'd like to see at least preliminary results with input functions that have limited smoothness. This will be vital in order to use operator learning for standard problems containing shocks or discontinuities.

4. FNOs are certainly not just used with the FNO integral operators studied in this work. Assume an input function in T^d (should be R^d as in the previous comment, but let's assume T^d!) is lifted by the input MLP to R^p, i.e., there are p channels. Each linear operator acts on p vector-valued input functions, and is augmented with a pointwise convolution operator that mixes information across those p channels. The analysis has completely ignored this, as far as I can tell, but those pointwise convolutions appear to be key in the approximation power of FNOs.

5. The authors should present at least one or two numerical experiments verifying their error bounds even in these restrictive settings (T^d, no pointwise convolution, arbitrary lift and projection). Currently, this work has none, and that is concerning. These numerical experiments would also give practitioners guidance on how to leverage the results from this paper in settings where a practitioner has control over the sampling and discretization procedures.

### Questions
1. See weaknesses above. I think this work is an important step in the right direction, but has certain critical weaknesses and assumptions that are not clearly stated in the work. It would be extremely useful to know whether those hidden assumptions drastically alter the results.

2. Another smaller quibble is the notation in the paper. Could we have a table in the appendix showing all the symbols and their meaning, at least if those symbols are FNO hyperparameters?

3. There is also a minor presentation issue. The three different error terms are all mixed together in the text. The authors should clearly separate them out and show us which is which.

4. The title of the paper says "controlling [various error terms]", but the authors do not specify a practical numerical procedure to control those errors nor do they demonstrate the efficacy of such a procedure. The title probably needs to be changed, or the numerical results I asked for (above) should contain an example demonstrating how to control these errors.

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
Authors derived upper and lower bounds on excess risk. Excess risk is formally defined on page 7, but in a gist it is an average of difference between error of selected statistical estimator and the best model in selected class. As a class of models authors consider linear functional model  $g(x) = \sum_{\left\|m\right\|\_{\infty}\leq K}\lambda\_m\phi\_{m}(x)\left<\phi\_{-m}, f\right>_{L_2}$ where  $\phi_m(x) = \exp(2\pi i \left(m^T x)\right)$, $\lambda_m$ are unknown parameters, $f$ and $g$ are input and output functions respectively. As an estimator authors use least squares with functions discretised on the uniform grid and scalar products computed with DFT.

### Strengths
The article is easy to read, rigorously written, and provides many details about related topics in functional data analysis and neural operators. Although I only reviewed appendices superficially, I have little doubts about the correctness of the theoretical results.

### Weaknesses
The main weakness is that the problem setup chosen by the authors is too simple (or too convenient) and not directly related to the operator learning problem. Somewhat subjectively, I do not find the results presented by the authors surprising. Given the simplicity of the setup, I am also not entirely sure that related results are not already available in the literature on functional data analysis.

 The problem authors consider is, how to estimate the error of a linear functional model with integral kernel diagonal in truncated Fourier basis, fitted with ordinary least squares and discretized on the uniform grid. This problem allows a succinct formulation on a single page. The excessive details on operator learning, Fourier neural operator, and straightforward results like Proposition 1 and Proposition 2, distract from the core problem. It would be more beneficial to directly formulate the problem and focus on its analysis.

It does not seem to me that there is a direct relation between the statistical or approximation properties of FNO and the model authors consider. For example, the authors claim "The inductive bias in FNOs is that the functions are sufficiently smooth so that the higher Fourier modes can be safely ignored." Although this is correct that FNO has some bias toward smoother function, the situation is not as simple as the author's frame. FNO contains nonlinear activation functions that are merely continuous. The resulting operator can transform frequencies well above the chosen truncation frequency for the integral kernel. In contrast, the linear model considered by authors can not possibly process high frequencies. This distinction compromises the relation between FNO and the linear model. Given that, it is unclear why FNO is introduced in such great detail.

The result seems to be straightforward in a way it contains a well-known statistical error, a well-known discretization error, and a well-known truncation error that essentially estimates the convergence rate of Fourier series for the functions from Sobolev space. It is very likely that related results are already available in the literature. The authors provide some discussion explaining why their results are different from already available ones. For example, they mentioned https://arxiv.org/abs/1208.2895 and claim that the differences are: (i) they consider an "agnostic setting" rather than additive noise model; (ii) parameter $K$ is not learned from the observed data; (iii) basis is not learned from observed data; (iv) functional data is given in a discrete. However, the significance of these differences is not fully justified. For example, the impact of data discretization is not thoroughly explained, given that discretization errors are well understood for functions in specific spaces. The setup given in https://arxiv.org/abs/1208.2895 is more natural and general than the one considered by the authors. The authors' setup seems to be an unnatural hybrid between operator learning and functional data analysis. On the one hand, the authors want to keep the structure of the linear operator from FNO, which seems too restrictive from a functional data analysis point of view. On the other hand, authors consider a single linear layer which is again too restrictive from a neural operator point of view.

Authors work with functions of $\mathbb{T}$. Intermediate layers of the Fourier neural operator do not produce exclusively periodic functions. This discrepancy is not addressed. On lines 503-504 authors made a strange claim that exponential dependence on $d$ does not matter for $d=3$. This statement is trivial. FNO can not be applied for large $d$ because it suffers from exponential increases in memory and computing. Line 423 $v_1$ contains incorrect subscript. It seems that the result obtained by authors can be extended to many families of functions, e.g., $\phi_{m}$ can be replaced with Chebyshev or Legendre polynomials. This is not discussed.

### Questions
**Major concerns:**
1. As I understand, the problem authors consider is, how to estimate the error of a linear functional model with integral kernel diagonal in truncated Fourier basis, fitted with ordinary least squares and discretized on the uniform grid.
   
   This problem allows a succinct formulation on a single page. Can the authors please discuss why they decided to provide excessive details on operator learning, Fourier neural operator, and straightforward results like Proposition 1 and Proposition 2? Would not it be easier (for the authors and the reader) to formulate the problem right away?

2. It does not seem to me that there is a direct relation between the statistical or approximation properties of FNO and the model authors consider. For example, the authors claim "The inductive bias in FNOs is that the functions are sufficiently smooth so that the higher Fourier modes can be safely ignored." Although this is correct that FNO has some bias toward smoother function, the situation is not as simple as the author's frame. FNO contains nonlinear activation functions that are merely continuous. The resulting operator can transform frequencies well above the chosen truncation frequency for the integral kernel. In contrast, the linear model considered by authors can not possibly process high frequencies.
   
   This distinction already compromises the relation between FNO and the linear model. Given that, it is unclear that one should introduce FNO (vaguely related model with completely different properties) in such great detail.

3. The result seems to be straightforward in a way it contains a well-known statistical error, a well-known discretization error, and a well-known truncation error that essentially estimates the convergence rate of Fourier series for the functions from Sobolev space. I can not point to the paper or monograph that contains results proven by authors in the paper, but it looks very unlikely that related results are not already available in the literature. The authors provide some discussion explaining why their results are different from already available ones. For example, they mentioned https://arxiv.org/abs/1208.2895 and claim that the differences are: (i) they consider an "agnostic setting" rather than additive noise model; (ii) parameter $K$ is not learned from the observed data; (iii) basis is not learned from observed data; (iv) functional data is given in a discrete. I would like the authors to extend the discussion of the differences. For example, why is it significant that data is not discretized? Is not it the case that discretization errors (or interpolation errors) are well understood when a particular space
   
   In my opinion, the setup given in https://arxiv.org/abs/1208.2895 is more natural and more general than considered by the authors of the current contribution. The reason for that, in my opinion, is https://arxiv.org/abs/1208.2895 in a standard functional-data analysis, while the setup of a present contribution is in-between operator learning and Functional data analysis. On the one hand, the authors want to keep the structure of the linear operator from FNO, which seems too restrictive from a functional data analysis point of view. On the other hand, authors consider a single linear layer which is again too restrictive from a neural operator point of view.

**Minor issues:**
1. Authors work with functions of $\mathbb{T}$. Intermediate layers of the Fourier neural operator do not produce exclusively periodic functions. Can the authors comment on that discrepancy?
2. On lines 503-504 authors made a strange claim that exponential dependence on $d$ does not matter for $d=3$. This statement is trivial. Perhaps, more importantly, FNO can not be applied for large $d$ because it suffers from exponential increases in memory and computing.
3. Line 423 $v_1$ contains incorrect subscript.
4. It seems that the result obtained by authors can be extended to many families of functions, e.g., $\phi_{m}$ can be replaced with Chebyshev or Legendre polynomials. Can the authors please comment on that?


All in all, I can not point to any significant technical flaw in the article, but I do not find the results surprising and useful for operator learning and functional data analysis. These points can be considered subjective, so I do not think they should significantly affect the decision to accept or reject the paper. I hope this explains the chosen "overall score".

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors investigate Fourier operators by analyzing the statistical, discretization, and truncation errors within the Fourier Neural Operator framework. There are error bounds derived from DFT-based least squares estimators and some insights into the efficient approximation of solution operators for PDEs.

### Strengths
The error bounds for approximation power and training landscapes are poorly understood in the context of FNOs. I enjoyed the analysis of the three types of error: (1) Finite training data (statistical error), (2) Representing continuous input/output on finite grid (Discretization error), and (3) Fourier series truncation (truncation error). 

In this paper, the discretization error and the truncation error are bounded very nicely. It is very welcomed to have both upper and lower bounds on these errors so that one can attempt to balance efficiency with accuracy. The upper bound of the statistical error makes sense as it is just a Monte Carlo rate of convergence, as expected. The lower bound is a little more mysterious because it comes from a particular difficult distribution that the authors have designed.

### Weaknesses
The statistical error is decaying only like the square root of the sample size n; however, much faster rates of convergence are usually observed in practice.  Getting at this discrepancy is important, because the analysis right now suggests that a large number of training data samples are needed for accurate FNOs.  One may have to make much bigger assumptions about the PDE to make this work or restrict the function space on which to learn the solution operator. 

The paper’s insights into the model structure only apply to the FNO’s linear core. While that is a first step, the nonlinear layers in an FNO’s architecture is the most important part.

I worry that the suggestion of selecting N>= n^{1/2s} and K>=n^{1/4s} is only because of the weaknesses of Theorem 1.  The only serious weaknesses between Theorem 1 and Theorem 2 is the 1/sqrt{n} versus the 1/n. 

In most PDE theory, we don’t assume that V = W. Instead, W is a smoother space than V.  Is it easy to adapt theorem 1 and theorem 2 so that V \neq W? 

Due to the Sobolev embedding theorem, one would usually imagine that the discretization error goes down like N^{s-d/2}, not N^s. Similarly, the truncation error goes down like K^{2s-d}, not K^{2s}. What’s your main idea for removing the dimension-dependency in the error bounds in Theorem 1?

### Questions
- I worry that the suggestion of selecting N>= n^{1/2s} and K>=n^{1/4s} is only because of the weaknesses of Theorem 1.  The only serious weaknesses between Theorem 1 and Theorem 2 is the 1/sqrt{n} versus the 1/n. 

- In most PDE theory, we don’t assume that V = W. Instead, W is a smoother space than V.  Is it easy to adapt theorem 1 and theorem 2 so that V \neq W? 

- Due to the Sobolev embedding theorem, one would usually imagine that the discretization error goes down like N^{s-d/2}, not N^s. Similarly, the truncation error goes down like K^{2s-d}, not K^{2s}. What’s your main idea for removing the dimension-dependency in the error bounds in Theorem 1?

### Soundness
3

### Presentation
3

### Contribution
3
