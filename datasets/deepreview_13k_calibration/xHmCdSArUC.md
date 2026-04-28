# Correlated Noise Provably Beats Independent Noise for Differentially Private Learning

- Decision: Accept
- Avg Score: 5.67
- Scores: 8, 8, 1

## Abstract
Differentially private (DP) learning algorithms inject noise into the learning process. While the most common private learning algorithm, DP-SGD, adds independent Gaussian noise in each iteration, recent work on matrix factorization mechanisms has shown empirically that introducing correlations in the noise can greatly improve their utility. We characterize the asymptotic learning utility for any choice of the correlation function, giving precise analytical bounds for linear regression and as the solution to a convex program for general convex functions. We show, using these bounds, how correlated noise provably improves upon vanilla DP-SGD as a function of problem parameters such as the effective dimension and condition number. Moreover, our analytical expression for the near-optimal correlation function circumvents the cubic complexity of the semi-definite program used to optimize the noise correlation matrix in previous work. We validate our theory with experiments on private deep learning. Our work matches or outperforms prior work while being efficient both in terms of compute and memory.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies DP-SGD with correlated noise, which is called DP-FTRL. Under the assumptions of i.i.d. data samples, Toeplitz correlation matrix, and unique minimizer, the authors characterized the asymptotic suboptimality of DP-FTRL. This considers mean estimation and linear regression and provides analytical expressions for the asymptotic suboptimality in a function of learning rate and effective dimension. Throughout experiments, the authors show the effectiveness of the proposed methods in various way.

### Strengths
The paper is well-written and pleasing to read. The motivation for this investigation is very clear. 
The analysis done in the paper is important in private ML, and the approaches to derive the results are interesting. I found that the closed-form expression for the optimal $\beta$ in mean estimation is interesting. It is quite surprising that the analysis of DP-FTRL on the simple mean estimation results in a better trade-off of DP-FTRL in experiments.

### Weaknesses
Most of the results are for Noisy-SGD and Noisy-FTRL, which are not DP as written in the paper. 
This paper uses lots of assumptions, and it seems difficult to adopt the results in practice. Specifically, the assumption of i.i.d. data samples and a Toeplitz correlation matrix are quite restrictive. The requirement for a unique minimizer also limits the applicability of the theoretical results. 
I understand it is a theory paper, but it would be useful to add more experimental results as they show the practical applicability.

### Questions
1) Is it possible to extend the analysis to general correlation matrices $B$ instead of Toeplitz?
2) What is the motivation to study mean estimation? Can Theorem 2.1. be extended to other problems?
3) What is $\mathcal{E}$ inside the expectation on page 7?
4) How to choose $\nu$ in general?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates DP linear regression and strongly convex problems. The goal is to minimize $F(\theta) = \mathbb{E}\_z [f(\theta, z)] + r(\theta)$ while providing a DP guarantee. The authors introduce a new version of DP-FTRL named $\nu$-DP-FTRL. Instead of independent noises, $\nu$-DP-FTRL uses a correlated noise $\tilde w_t = \sum_{\tau=0}^t \boldsymbol{B}\_{t,\tau} w_\tau$, where each $w_\tau$ is an i.i.d. Gaussian and $\boldsymbol{B}$ is a Toeplitz lower-triangle matrix. The parameter is then privately updated as $\theta_{t+1} = \theta_t - \eta(g_t + \tilde w_t)$, with $g_t$ representing the non-private stochastic gradient (which may or may not be clipped).

The paper sets $\nu$-DP-FTRL against DP-SGD, comparing their theoretical guarantees and empirical performances. Theoretically, the authors provide upper bounds for the suboptimality gap $\mathbb{E}[F(\theta_T)] - \inf F(\theta)$ for both algorithms. Notably, $\nu$-DP-FTRL attains an asymptotic suboptimality gap of $\tilde O(d_\text{eff}\eta^2/\rho)$, where $d_\text{eff} \le d$ is the effective dimension. This matches the existing lower bound up to a logarithmic factor and improves upon the $O(d\eta/\rho)$ rate of DP-SGD. Empirically, $\nu$-DP-FTRL also demonstrates better experiment performance compared to DP-SGD.

### Strengths
- This paper provides a very detailed theoretical proof supporting the empirical observation that DP learning with correlated noise surpasses that with independent noise.
- The introduced algorithm, $\nu$-DP-FTRL, offers a notable improvement in the theoretical utility upper bound when compared to the leading bound of DP-SGD. Notably, this improved bound is dependent on the effective dimension $d\_\text{eff}$, which is often tighter than the vacuous dimension $d$ and thus adapts better to the problem difficulty. Furthermore, the bound demonstrates an improved dependence on the learning rate, improving from $O(\eta)$ to $O(\eta^2)$, which aligns with the existing lower bound.
- The authors utilize the Fourier transform as an instrumental analysis tool for bounding the suboptimality gap. This analytical approach is beyond my expertise, but it suggests an new perspective for analyzing the asymptotic behavior of optimization problems.

### Weaknesses
My main concern is about the privacy guarantee. The authors use a high probability bound to argue that most of the time, the stochastic gradients won't exceed the clipping norm. Consequently, $\nu$-DP-FTRL doesn't need any gradient clipping. But I'm not sure if this meets the standard DP definition, as sensitivity might be prohibitively high in rare cases. To me, the link between the high probability result and the standard definition isn't clear. Once this is addressed, this paper has very solid results.

### Questions
I'm curious about the role of $\nu$ in $\hat \beta_t^\nu$. Since $\binom{1/2}{t}$ in $\hat \beta_t^\nu$ already decreases rapidly (roughly $1/t$ if I'm correct), is it necessary to add an additional damping term $(1-\nu)^t$? Also, $\nu$ is currently set to some small value in the experiments, so $(1-\nu)^t$ decays significantly slower than $\binom{1/2}{t}$. Thus, I wonder if $\nu$ can be dropped to save some tuning effort. How would removing $\nu$ (or setting $\nu=0$) affect the theoretical bound and the empirical performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies optimization (e.g., SGD) under differential privacy where the noise added to gradients correlates.

### Strengths
It is plausible that correlated noise can help in some way.
Researching this seems a valuable contribution.

If the text (or at least the appendix) would be clear and self-contained, and if the text would make the claims fully explicit, then this may become an interesting contribution discussing several interesting issues.

### Weaknesses
Parts of the text are very hard to follow.  E.g.,
* The text introduces the limit with T going to \infty, without explaining how this can make sense for a bounded privacy budget (i.e., for a finite privacy budget and an infinite (large) number of iterations, an infinite (large) amount of noise should be added in every step to the gradient, making it hard to converge.
* While Eq (1) defines f(\theta, z) as objective function, Eq (6) seems to treat f as the derivative of the objective function.
* The proof of theorem 2.1 cites Fourrier analysis, but doesn't make explicit what is the derivation the authors have in mind.  There is even no proof that the asymptotic optimality defined by Eq (4) exists (i.e., the limit converges), which is non-trivial as the more iterations are performed, the higher the amount of noise per iteration needs to be.

The text also is insufficiently explicit leading the reader to incorrect assumptions on what is meant.  For example, while most of the text just uses "differential privacy", Appendix A.2 suddenly says that instead of "neighboring datasets" as most machine learning literature considers, the current paper considers zero-out neighborhood, where two sequences of gradients are adjacent if they only differ in one gradient.  This is clearly not the case if we are performing an optimization and are comparing the algorithm being run on neighboring datasets, in which case (almost) every gradient will be different.  As a result, Appendix B seems to be not really proving theorem 2.1 but a variant where "neighboring datasets" is replaced by "zero-out neighbors", which changes the meaning of the theorem.

The paper is not self-contained, and a lot of terms are not even explained in the appendix.


Before Eq (3) the text says that B is a Toeplitz matrix.  How shall we read B(\omega) after Eq (3)?  B is not a function, and the righthandside of B(\omega)=... evaluates to a complex number rather than a real-valued matrix.

Does the series \beta_t need to satisfy any property to make the sums and limits converge?

How is \gamma_T defined?  The text says that one can infer Eq (4) from this definition.  In Eq 4, how shall we read the superscript 2?  Does it square \gamma_T(B) or does it square its argument B?  (In the former case, many people would write (\gamma_T(B))^2 or \gamma_T^2(B), in the latter case, most people would write \gamma_T(B^2))



Now we get to applying Theorem F.2 in the proof of Theorem 2.1.  We should think of the following:

* $G$ in Thm 2.1 is not related to $\mathbf{G}(\omega)$ is Theorem F.2
* I guess $x_t$ in Thm F.2 corresponds to $\delta_t$ or $\beta_t$ or $w_t$ in Thm 2.1.  Unfortunately, for $x_t$ in Thm F.2, $t$ ranges from $-\infty$ to $+\infty$ while both $\delta_t$, $\beta_t$ and $w_t$ in Thm 2.1 are sequences for which $t$ ranges from $t=0$ to $t=\infty$.  Maybe, let us guess that $x_t$, $y_t$ and $H$ in Thm F.2 correspond to $w_t$, $\beta_t$ and $\delta_t$ in Thm 2.1.  
* The text doesn't explain why the transformation from $\theta_t$ into $\delta_t$ was useful, Eq (11) looked much more as a linear transformation, but apparently it was a preparation for applying Thm F.2, and hence could provide a clue, even though only some of the symbols in the $\delta_t$ equation occur in the resulting bound.  For example, the newly introduced $w_{sgd}$ doesn't occur in the resulting $F_\infty(B)$ equation.  Maybe the term $\eta\sigma_{sgd} w_{sgd}$ is not important and we should only look at the term involving $w_t$, but in that term $\sigma_{sgd}$ does not occur, while this variable does occur in the $F_\infty(B)$ equation.
* Applying Thm F.2 requires the LTI is asymptotically stable, but the text doesn't argue why this condition is fulfilled.  I guess this is a consequence of the assumption that the objective function is convex.  

Nevertheless, it is plausible that with adding half a dozen of additional intermediate steps and explanations this step can be shown to be correct.

Next, the text says "Thus $F_\infty$ is a product of ...".  In fact, $F_\infty$ is a function, and $F_\infty(B)$ is an integral, which we can interpret as a sum, but not immediately as a product.  For every specific $\omega$, indeed we have as integrand $|B(\omega)|^2 \gamma_\infty(B)^2$ multiplied with other factors, where $\gamma_\infty$ is an integral (a sum) with $|B(\omega)|^{-2}$ as one of its terms.  To write $F_\infty(B)$ as a product, an alternative strategy (not mentioned in the text) would be to first observe that $\sigma_{sgd}^2$ is a constant, and then to minimize the part remaining after removing $\sigma_{sgd}^2$, in that case one could write $F_\infty(B)$ as a product by getting $\gamma_\infty(B)$ out of the integral.  

Eq (14) then suggests that of the other factors in the product, including $G^2$ and $\sigma_{dp}^2$, only the denominator should be included when determining $B(\omega)$ to minimize $F_\infty(B)$, but the text doesn't give a reason.

"elliptic integrals coming from the $\sigma_{dp}$ term" -> I guess you mean "factor" rather than "term" here.

The text says the proof of the error bound now follows by applying a list of results it refers to.  However, the bound stated in Theorem 2.1 contains the variable $\rho$, but neither Lemma F.15 nor Corollary C.5 seem to introduce a $\rho$ into the equation we have so far.


Footnote 4 says "a $\rho$-zCDP guarantee can be readily translated into (\epsilon,\delta)-differential privacy" without giving the definition of either notion.  The conditions are hidden in appendix A.2, the main text could simply refer to them to get more self-contained.

Theorem 2.1 uses the term "$\rho$-zCDP sequence" while usually only algorithms are called private (not sequences).  Maybe you mean that the DP-SGD from which you obtained the sequence should get parameters so it is $\rho$-zCDP, but the text doesn't seem to say what parameters to choose to realize that.

It is still unclear to me why you define neighboring datasets in terms of gradients rather than the more more common definition in terms of the underlying data (even if one can reason that if two instances have the same gradient, their difference isn't relevant for the algorithm).

It is unclear why the statement of Theorem 2.1 says G=1, while the proof says $G\ge 1$.  Of course, $G\ge 1$ so it doesn't harm.

Definition F.1. if satisfies -> if it satisfies

Given that Definition F.1 talks about $\mathcal{X}$-valued sequences, it would be consistent for the sentence after Definition 2.1 to talk about $\mathcal{X}$-valued sequences rather than $\mathbb{R}^d$-valued sequences (or else that you irst say "From now on we will choose $\mathcal{D}=\mathbb{R}^d$." or use $\mathbb{R}^d$ already in the definition or ....).

"LTI systems can be described in linear algebraic notation by the action of an infinite Toeplitz matrix H on an element of $\ell_{2e}$" -> do you mean $\ell_{2e}^d$?

The text here doesn't use the original notation $\mathcal{A}_t$ anymore, I guess that you mean one can for such systems find a matrix $H$ such that $\mathcal{A}_t(x) = H_{t,:}x$.

Of course, this is easier to see if $x\in\mathbb{R}$ rather than the originally used $\mathbb{R}^d$.  If $x_\tau\in \mathbb{R}^d$, then to let $y=Hx$ match we need $x\in\mathbb{R}^{\infty\times d}$ rather than its transpose.

Later, before Theorem 9.2 we will discover this is in fact not correct, the authors are thinking of $y_t\in\mathbb{R}^p$, so $H$ will become an appropriate tensor (or maybe not, as Theorem F.2 says G (i.e., H) is in $\mathbb{R}^{p\times d}$, so I guess all components of $x_t$ and $y_t$ get the same linear transformation.

It is natural to denote the DTFT of $x$ by $X(\omega)$, of $y$ by $Y(\omega)$, but why is the DTFT of $h$ denoted by $G(\omega)$?  I suppose it is more confusing for the reader, especially as in Theorem 2.1 another $G$ (real number, clip norm) is being used (even if not bold-faced there).

In Theorem F.2, the product $\otimes$ isn't defined (but is hard to guess given the dimension confusion above).  Anyway, $\Sigma = \mathbb{E}[x_t \times x_{\tau}]$ seems to be a constant, not depending on $t$ and $\tau$, except perhaps that this may not be the correct interpretation as the integral over $G(\omega) \Sigma G(\omega)^*$ then shouldn't depend on $X(\omega)$ nor $Y(\omega)$.  So maybe $\Sigma$ does depend on $t$ and $\tau$ (a tensor with on the diagonal $d\times d$ matrices)?  In any case, this wouldn't write $\Sigma$ as a function of $\omega$ to fit in the integral.  The theorem doesn't say anything about $\mathbb{E}[y_t \otimes y_\tau]$ with $t\neq \tau$.

In Theorem 1.1, why do we have $\gamma_T(B) = \max_{t<T} ...$, i.e., why is the last $T$-th column of $B^{-1}$ not considered for $\gamma_T(B)$ ?

$B$ is called the "correlation matrix".  Normally, if $x$ is a random vector, then the correlation matrix of $x$ is defined as $\mathbb{E}[x x^\top]$, which is always a symmetric matrix.  However, the text says $b$ is a lower triangular matrix.  I conclude that $B$ is not the expectation of $w_t w_t^\top$ for $w_t$ the generated noise ?


### Questions
Before Eq (3) the text says that B is a Toeplitz matrix.  How shall we read B(\omega) after Eq (3)?  B is not a function, and the righthandside of B(\omega)=... evaluates to a complex number rather than a real-valued matrix.

Does the series \beta_t need to satisfy any property to make the sums and limits converge?

How is \gamma_T defined?  The text says that one can infer Eq (4) from this definition.  In Eq 4, how shall we read the superscript 2?  Does it square \gamma_T(B) or does it square its argument B?  (In the former case, many people would write (\gamma_T(B))^2 or \gamma_T^2(B), in the latter case, most people would write \gamma_T(B^2))

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
