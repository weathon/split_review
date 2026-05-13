# Generalization for Least Squares Regression with Simple Spiked Covariances

- Decision: Reject
- Scores: 5, 3, 5, 5, 6

## Abstract
Random matrix theory has proven to be a valuable tool in analyzing the generalization of linear models. However, the generalization properties of even two-layer neural networks trained by gradient descent remain poorly understood. To understand the generalization performance of such networks, it is crucial to characterize the spectrum of the feature matrix at the hidden layer. Recent work has made progress in this direction by describing the spectrum after a single gradient step, revealing a spiked covariance structure. Yet, the generalization error for linear models with spiked covariances has not been previously determined. This paper addresses this gap by examining two simple models exhibiting spiked covariances. We derive their generalization error in the asymptotic proportional regime. Our analysis demonstrates that the eigenvector and eigenvalue corresponding to the spike significantly influence the generalization error.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors analyze the generalization properties of spiked covariate models. The theoretical analysis is motivated by recent works on two-layer networks trained with a single gradient step that showed how the feature matrix possesses different spikes associated with the learning rate scaling used in the optimization step. The proof scheme uses tools coming from random matrix theory that enables the asymptotic computation of the generalization error. The theoretical claims are accompanied by coherent numerical illustrations.

### Strengths
The paper is nicely written. The mathematical claims are correctly phrased and the numerical illustrations are coherent with the main text. The research problem is relevant in the theoretical machine learning community.

### Weaknesses
My main concern with the present submission is the lack of clear elements of novelty. The paper heavily relies on results coming from related works and it restricts their setting in many ways (as fairly reported by the authors at the end of the manuscript). More specifically, the analysis seems to be a direct application of random matrix theory tools to a specific, simplified model of feature learning, closely related to the settings considered in (Ba et al., 2022; Moniri et al., 2024). The restriction to a single spike in the feature matrix, while simplifying the analysis, limits the applicability of the results to more realistic scenarios where multiple spikes may emerge due to the learning dynamics. Furthermore, the paper does not adequately address the connection with other lines of work that analyze learned representations with gradient descent using different tools, focusing primarily on the random matrix theory literature. The absence of a discussion regarding the relationship with non-rigorous methods that characterize the generalization error, such as the one in Cui et al. 2024, further weakens the contribution of the present submission.

### Questions
As hinted above my main concern on this manuscript is the close relationship with previous works, namely (Ba et al., 2022; Moniri et al., 2024). 

Could the authors comment on the link between their results and (Ba et al. 2022) in the context of Gaussian Universality (see e.g. [1]) ? From my understanding of their paper, i.e. a single spike in the feature matrix, they show that in the learning rate regime considered in this paper Gaussian Universality should hold. There is indeed an extensive regime of learning rates after the BBP transition that still falls under the umbrella of Gaussian models, resulting in effectively "linear" generalization properties. 

One additional weakness of this submission is the related works coverage. The authors do a great job in covering the random matrix theory literature, while many manuscripts that analyze learned representations with gradient descent with different tools are not properly mentioned, see e.g. [2,3,4]. Although in these works the authors do not focus on the exact asymptotic calculation of the test error, many insights should translate to the present setting. On the other hand, [5] precisely characterize the generalization error using non-rigorous methods; what is the relationship with the present work?

The results in the present submission should relate directly to the ones in Section 4 of (Moniri et al. 2024), albeit the differences correctly reported by the authors in the two settings. Could the author elaborate on this? 

What is the bottleneck for the present thereotcial tools to analyze multiple spikes (corresponding to higher learning rate scaling in Moniri et al. 2024)? 

Closely related to the above, [5] worked along the lines of (Moniri et al. 2024) to provide the equivalent description in the regime where the spikes recombine with the bulk (maximal scaling regime). Do the authors see a possible extension of their analysis to this scaling? 


- [1] Hu & Lu 2022, Universality laws for high-dimensional learning with random features. 
- [2] Damian et al. 2022, Neural networks can learn representations with gradient descent. 
- [3] Dandi et al. 2023, How two-layer neural networks learn, one (giant) step at a time.
- [4] Ba et al. 2023, Learning in the presence of low-dimensional structure: a spiked random matrix perspective.
- [5] Cui et al. 2024, Asymptotics of feature learning in two-layer networks after one gradient-step.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Motivated by a recent work studying two-layer neural networks (Moniri et al., 2023), the paper studies linear regression under a data model with a spiked covariance (Couillet & Liao, 2022). The spiked covariance consists of a spike component (signal) and a bulk component (noise). Thus, the authors characterize the risk (a.k.a generalization error) with a specific focus on the effect of the spike. They find that the spike does not impact the risk in the underparameterized case. In contrast, the spike introduces an additional term (called "correction term") in the risk for the overparameterized case. However, they mention that the correction term is of order $O(1/d)$, which vanishes in the asymptotic case. Thus, the spike does not affect the risk in the asymptotic case but does in the finite case. Then, the authors focus on a case where the targets $y$ only depend on the signal (spike) component of inputs $\mathbf{x}$ in order to highlight the effect of the spike on the risk. In this case, the correction term depends on the alignment between the spiked eigenvector $\mathbf{u}$ corresponding to the spike and the target function $\boldsymbol{\beta}$. Furthermore, the paper illustrates how the generalization error for this setting exhibits the so-called double-descent phenomenon with a formula for the peak location (a.k.a interpolation threshold).

### Strengths
* The motivation for this paper is good since the recent line of work studying two-layer neural networks after one gradient step (Ba et al., 2022; Moniri et al., 2023) has received significant attention.
* The authors precisely characterize generalization errors (risk) for two linear regression problems with spiked covariance data, while the problems differ regarding the target function.
   + They provide bias and variance decomposition of the risk.
   + They illustrate the "double-descent phenomenon" and provide a formula for the peak location (a.k.a interpolation threshold) of the double-descent phenomenon, which is beneficial for understanding the phenomenon.
   + The authors specifically focus on the impact of the spike (in the data model) on the risk for different cases. Thus, they show when and how the spike affects the generalization error.

### Weaknesses
### weaknesses:
* The presentation in this paper is not good
 + Although the paper is motivated by Moniri et al. (2023) [3], there are significant discrepancies between the setting of this paper and that of Moniri et al. (2023) [3], as the authors mention in Section 5. While Moniri et al. (2023) [3] considered two-layer neural networks after one gradient step under isotropic data assumption, this work considers linear regression under spiked covariance data assumption. There exists a relationship between these two, but they are not exactly the same. For example, the target $y$ generation process differs between the two settings. Specifically, the dependence between $\mathbf{A}$ (noise component) and $\mathbf{Z}$ (spike component) present in Moniri et al. (2023) [3] is not considered here (see lines 251-255 of the current paper). This discrepancy needs to be addressed more thoroughly.
 + Some notations are used without definition (e.g, $\delta_{\lambda_i}(\lambda)$ in Line 126, or $\Sigma(d_k)$ in Line 147). These should be clearly defined upon first use.
 + There are significant typos in equations. For example, $y$ should be a scaler in Line 76, but it is written as a vector, which makes the equation wrong. Another example is that $l_j$ in Theorem 2 (Line 204) is not defined, and I think the authors meant $l$ instead of $l_j$. A third example is that the function $R_{spn}(c;\tau,\theta)$ defined in Line 301 and its usage $R_{spn}(c,0,\tau)$ in Theorem 3 (Line 317-321) are different in terms of parameters. These inconsistencies need to be rectified.

* Limited contribution/novelty
 + Most of the results in this paper appear to be trivial extensions of the results by Hastie et al. (2022) [1] and Li & Sonthalia (2024) [2], which significantly limits the novelty and originality of the paper. Hastie et al. (2022) [1] studied linear regression under a generic covariance assumption with bounded eigenvalues. While this work allows some eigenvalues to diverge as dimensions go to infinity, this case is also covered by Li & Sonthalia (2024) [2]. The authors should clearly delineate how their work goes beyond these prior studies, particularly in the context of finite-sample analysis and the impact of the specific spiked covariance structure.
 + There exists a related work (Cui et al., 2024) [4] that is not mentioned in this paper. Cui et al. (2024) [4] characterized the generalization error (risk) for two-layer neural networks after one gradient step under isotropic data (same setting as that of Moniri et al. (2023) [3]). Although there exist methodological differences between Cui et al. (2024) [4] and this paper, the motivations are the same, and their settings are similar. The authors should discuss how their work relates to and differs from Cui et al. (2024) [4].
 + During the review period of this paper, a related work (Dandi et al., 2024) [5] that can be considered as follow-up of (Cui et al., 2024) [4] was appeared on arXiv. While Cui et al. (2024) [4] used (non-rigorous) replica method from statistical physics for their analysis, Dandi et al. (2024) [5] studied the same setting with random matrix theory, which is also the main tool in this paper. Therefore, this paper and (Dandi et al. 2024) [5] studied similar settings with similar methodologies. The authors should discuss the relationship between their work and Dandi et al. (2024) [5] to highlight the unique contributions of their paper.

Overall, I think this paper should be rewritten with more focus on the impacts of the spike covariance on the generalization error of linear regression, and the new presentation should clearly differentiate the current work from the work by Hastie et al. (2022) [1], Li & Sonthalia (2024) [2], Cui et al. (2024) [4], and Dandi et al. (2024) [5].

### Questions
1. In Line 178, $F_1$ denotes the case with a single spike (as shown by Moniri et al., 2023). However, Moniri et al., 2023 showed that $F_1$ can include multiple spikes, and the number of spikes depends on the step size of the gradient step. Where is the discussion about the effect of step size in this paper? Similarly, where is the discussion on the impact of $o(\sqrt{n})$ term for $F_1$?

2. What is $l_j$ in Theorem 2 (Line 204)? Do the authors mean $l$?

3. In footnote 3 (Line 266), the authors say "... the limiting e.s.d for $F_0$ is not necessarily Marchenko-Pastur distribution ... This difference is not too important, as instead of using the Stieltjes transform for the Marchenko-Pastur distribution in our paper, we could use the result from Péché (2019); Piccolo & Schröder (2021) instead." Why wouldn't the authors directly use the mentioned result directly?

4. Why is there no regularization for the signal-plus-noise problem when there is regularization for the signal-only problem (Line 278-285)?

5. Typo in Line 285: "We consider on the instance-specific risk.". Typo in Line 313: " Then, any for data ...". 

6. Undefined symbols in Theorem 3 (Line 312 - 324): $\asymp$ and $<<$.

7. How do the authors arrive at "Hence, we see that if the target vector y has a smaller dependence on the noise (bulk) component A, then we see that the spike affects the generalization error." in Line 380? Its connection to the previous part seems to be missing.

8. How do the authors come up with the equation for the peak point of double descent in Line 477? Is it an empirical observation or a theoretical result?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers the linear least squares regression for data with simple spiked covariance. They quantify the empirical risk of test data.

### Strengths
1. They construct two linear regression problems with spiked covariance.
2. They well explain the previous work of Moniri et al. (2023).
3. Precise quantification of the generalization errors are also provided for both model.

### Weaknesses
1. They reference the work of Moniri et al., but this work is unrelated to neural networks or gradient descent; it addresses a purely linear regression problem for data with simple spiked covariances.

2. They do not account for the generalization ability of neural networks after a single gradient step, as they bypass the gradient step entirely by assuming the W1 matrix directly, which does not reflect the full process of neural network training. This simplification, while potentially useful for analysis, significantly deviates from the actual dynamics of neural network learning, where the weight matrix W1 is a result of iterative optimization rather than a direct assumption. The analysis, therefore, lacks direct applicability to understanding the generalization properties of neural networks trained via gradient descent.

### Questions
1. Could you provide a reference for the statement, 'It has been shown that to understand the generalization...' on line 39?
2. Is your generalization analysis very different from the work  of Li & Sonthalia (2024)?

### Soundness
3

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
3

### Summary
This paper analyses the generalization error of linear regression with spiked covariance. Previous literature has been using asymptotic limit of the empirical spectral density to analyse the generalization error of linear regression. At the limit, the effect of the spike vanishes. However, it is not the case for finite sample size. This paper fills the gap by showing there is a correction term for finite sample size $n$.

### Strengths
This paper provides a detailed proof of their main theorems with clearly stated definitions. It extends over previous results like [1,2].


[1]: Trevor Hastie, Andrea Montanari, Saharon Rosset, and Ryan J Tibshirani. Surprises in highdimensional
ridgeless least squares interpolation. Annals of statistics, 50(2):949, 2022.
[2]: Xinyue Li and Rishi Sonthalia. Least squares regression can exhibit under-parameterized double
descent. Advances in Neural Information Processing Systems, 2024.

### Weaknesses
However, this paper has some obvious weaknesses:

1. The paper is motivated by the spiked covariance from the one-step gradient feature learning in neural networks (Section 1). However, it did not show how the results can be applied to the feature learning scenario. I question the amount of contribution this paper provides.
2. The assumption in line 2221-222 and 253-255 is too strong. The analysis breaks down if there is dependency in the cross term. However, the paper did not show how big the difference the predicted result would be when there is dependence in the cross term. It is questionable if the result in this paper is applicable in realistic machine learning settings.
3. This paper has problems with the wordings, even in main theorems. This makes the reading difficult. For instance:

> Theorem 3 (line 313): ...Then, any for data $X\in\mathbb{R}^{n\times d}, y\in\mathbb{R}^n$ from the signal-plus-noise model that satisfy: $1\ll \tau_{A_{trn}}^2,\tau_{A_{tst}}^2\ll d, \theta_{trn}^2/\tau_{A_{trn}}^2<<n, \theta_{tst}^2/\tau_{A_{tst}}^2 << n_{tst}$. Then for $c<1$,...

The first sentence needs to be rephrased and the symbol $\ll$ is not consistent. Also, there are some typos like:
> line 350: Hence the spike has does not have an effect...

> line 372, ... we see an affect that...

### Questions
Regarding the weaknesses mentioned above, I would like to ask:

1. What novel results could the authors conclude in the feature learning setting in neural networks using the main theorems 3,4?

2. How could the authors show the assumption on the dependence does not affect the result? Is there any experimental validation?

3. From Figure 4.1, we can see that the effect of the spike correction term is small when $n$ is large. Is the main theorem still useful to explain the phenomenon we see from feature learning?

### Soundness
2

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
Motivated by the problem of training the readout of a two-layer network after on large gradient step on the first layer, the authors consider the problem of linear regression on a spiked data model. They provide a characterization of the test error, for two linear target functions, respectively depending on only the spike part or the complete input. They discuss how for the latter, the spike does not asymptotically influence the test error, but does non-asymptotically.

### Strengths
The paper is well written, clearly motivating the study, and describing in simple terms the model considered. Sufficient intuition is provided at most steps of the discussion. The technical results are clearly exposed and sufficiently discussed. Although I did not go through the proof in detail, the technical results seem scientifically sound.

### Weaknesses
 I have a number of concerns related to the technical discussions, and the relation to previous works, which I detail below, and in the question section. These concerns regard the discussion of the main theorems, and not the theorems themselves, although I have not carefully verified the proof. These concerns prevent me from giving a higher score to this submission. On the other hand, I would be very happy to increase my score, were those concerns to be addressed by the authors.

- The authors claim l.083 that Moniri et al. (2023) do not quantify the test error after one gradient step. To the best of my understanding, they do provide such a tight characterization (Theorem 4.5). Could the authors clarify their claim, and emphasize how their work is positioned with respect to Moniri et al. (2023)?

- I find the discussion l.332-355 somewhat confusing, as they discuss the specialization of Theorem 3 for $\theta=\tau\sqrt{n}$. Doesn't this directly contradict the assumption $\theta^2/\tau^2\ll n$ stated in the Theorem? Since this specialization leads to one of the main qualitative results of the paper (namely the spike only affects the test error in non-asymptotic cases), this point would gain to be clarified.  The same holds for l.452 with respect to Theorem 4.

- I believe more intuition about the different scaling considered would help solidify the intuition for the spn case, regarding when the spike matters. In particular, the authors could for instance recall the scaling of the terms $z_i^\top\beta_*$, $a_i^\top \beta_*$, and emphasize their respective strengths in the different scalings of $\theta, \tau$ considered. I am curious if the signal part is much smaller than the second term when the spike has no effect, or if the argument is more subtle.



### Questions
- In the discussion above 4.1, the assumption $\theta=\tau^2 n$ seems again to contradict the assumption $\theta^2/\tau^2\ll n$ in the statement of the Theorem. Furthermore, this seems to correspond to a strong spike regime, how can the authors recover the spikeless results of Hastie et al. (2022) in this case? This might be a misunderstanding on my side, but more discussion would be beneficial.

Minor:

- l.074, 347 : incomplete sentences
- l.203 I think $\ell_j$ is not defined
- In 3.3, more discussion in the main text about why only the unregularized case is considered for the spn case, while generic $\mu$ is considered for the signal-only model, would be helpful for intuition, whether it is for technical reasons or because it is not interesting.

### Soundness
3

### Presentation
4

### Contribution
3
