# Identifiability for Gaussian Processes with Holomorphic Kernels

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Gaussian processes (GPs) are widely recognized for their robustness and flexibility across various domains, including machine learning, time series, spatial statistics, and biomedicine. In addition to their common usage in regression tasks, GP kernel parameters are frequently interpreted in various applications. For example, in spatial transcriptomics, estimated kernel parameters are used to identify spatial variable genes, which exhibit significant expression patterns across different tissue locations. However, before these parameters can be meaningfully interpreted, it is essential to establish their identifiability. Existing studies of GP parameter identifiability have focused primarily on Mat\'ern-type kernels, as their spectral densities allow for more established mathematical tools. In many real-world applications, particuarly in time series analysis, other kernels such as the squared exponential, periodic, and rational quadratic kernels, as well as their combinations, are also widely used. These kernels share the property of being holomorphic around zero, and their parameter identifiability remains underexplored.
In this paper, we bridge this gap by developing a novel theoretical framework for determining kernel parameter identifiability for kernels holomorphic near zero. Our findings enable practitioners to determine which parameters are identifiable in both existing and newly constructed kernels, supporting application-specific interpretation of the identifiable parameters, and highlighting non-identifiable parameters that require careful interpretation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a new theoretical framework that can be used to determine identifiably of parameters in a stationary kernel under the infill asymptotic. Using this framework, the authors are able to determine the parameter identifiably of several popular kernels in the literature, extending the theoretical framework for the Matern class in the literature. Some numerical experiments are used to validate the theoretical findings.

### Strengths
This is a very well-written paper addressing an important research question in the literature. The theory is solid, especially Theorem 3.4, can be very useful for researchers in related areas.

### Weaknesses
No apparent weakness. (Note: I have reviewed this paper for another conference before, and all my previous questions have been addressed. Personally, I think this is a great work based on my research experience and should have been accepted.)

### Questions
I have to admit that I did not go through the proof line by line, but the arguments make intuitive sense.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the identifiability of parameters in a Gaussian process (GP) model with a kernel that is stationary and holomorphic around zero. Identifiability in GPs is a critical issue for both parameter estimation and interpretability. However, according to the authors, identifiability remains insufficiently studied for a wide range of kernels, as most existing methods apply only to a limited set of kernels.

To address this, the authors introduce a new method for establishing the identifiability of GP parameters. Using this approach, they demonstrate that parameters for several well-known kernels are identifiable. They also derive conditions under which parameters of sums of products of kernels remain identifiable, extending the applicability of their method. Finally, experiments on datasets support their theoretical findings, confirming the identifiability of parameters across various kernels.

### Strengths
- The motivation for studying identifiability conditions for kernels of GP is strong, as it enables clearer interpretation of model parameters. Additionally, the focus on widely used kernels is a practical and relevant choice.

- The authors introduce a novel reasoning approach to derive the identifiability condition, which could be of interest to researchers beyond the immediate scope of this paper.

- Overall, the paper is well-written, and the authors have provided code to facilitate reproducibility of the results.

### Weaknesses
 - While the results are presented for various kernels, the scope is still limited to stationary and holomorphic kernels around zero, which restricts the broader applicability of the identifiability condition.

- The experimental results are somewhat inconclusive. It would be helpful to clarify what should happen when parameters are identifiable. For instance, if the parameters are indeed non-identifiable, we might expect the estimated values to fluctuate across a range of possibilities. Can the experiment demonstrate that this is not occurring? Perhaps there is a statistical test that could be developed to verify whether the model is, in fact, identifiable. The observed reduction in variance is promising evidence, yet it leaves unanswered questions about cases where variance does not decrease. It would also be useful to test the behavior of parameters that are known to be non-identifiable—particularly those that would not be easily identifiable without the specific reasoning introduced in this paper.

### Questions
It is true that the decreasing variance with an increasing number of samples is reasonably convincing evidence that the parameters identified as "identifiable" are indeed identifiable. However, in cases where this pattern does not hold, do you have any additional arguments to support that the experiments still validate the theory's conclusions about identifiability? Conversely, what kind of behavior would you expect to see if a parameter were not identifiable? More broadly, is there a way to develop a meaningful statistical test to empirically confirm that the parameters theoretically classified as identifiable or non-identifiable actually exhibit these properties?

### Soundness
3

### Presentation
3

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
The paper studies identifiability of the parameters of certain kernels (squared exponential, periodic, rational quadratic, and cosine) and some of their sums and products, in Gaussian process regression (fixed domain asymptotic scenario). In certain cases, it finds microergodic parameters: the functions of parameters that _are_ identifiable, and thus can be consistently estimated. It illustrates the results with an empirical study of convergence of maximum likelihood estimators.

### Strengths
- The paper presents new theoretical results on identifiability, which are, in principle, intersting.
- The results look plausible (I didn’t check the 13 pages of proofs in the appendix though).
- The code is provided in the supplementary materials.

### Weaknesses
 - The paper promises a theoretical framework for determining the identifiability of parameters in arbitrary combinations of squared exponential, periodic, rational quadratic, and cosine kernels. However, the results don’t appear as such: they consider a few special cases, like sums and products of cosine kernels only. The general sum/product combination of the mentioned kernels is not explicitly handled. The theorems provided are limited to specific combinations, and a systematic approach for arbitrary combinations is lacking. For example, a general result for a sum of a squared exponential and a rational quadratic kernel is not presented, which would be a more practical scenario.
- The proofs are hidden in appendices. This is normal for a theoretical paper submitted to a conference. However, in such cases I expect the main ideas/methods to be covered in the main text, so that a reader who doesn’t have time to read the actual proofs could at least get some idea of how they go and how plausible they are.
I believe the paper falls short of this. In particular, the paper studies kernels on $\mathbb{R}^n$, but uses the term “holomorphic” from the world of complex numbers, and assumes the properties of kernels with traditionally real inputs on complex domains. This connection between the world of real-input kernels and the world of complex-analytic methods seems crucial, but remains unclear to me from the main text. The paper does not adequately explain how the properties of kernels defined on $\mathbb{R}^n$ are extended to the complex domain, and how this extension is justified. The assumption of holomorphic extension is not trivial and needs more explanation.
- There are certain problems with writing/presentation, like tables going over the right margin (Table 2) and figures with overly small fonts (Figure 1).
- Empirical study doesn’t illustrate the theoretical findings well. It doesn’t identify them as wrong, but in many of the studied cases does not really show anything. The simulations often show a plateau in the variance of the Maximum Likelihood Estimator (MLE), which does not provide clear evidence of convergence or non-convergence. The chosen sample sizes might be insufficient to observe the asymptotic behavior predicted by the theory. The empirical study lacks a clear connection to the theoretical results, making it difficult to validate the theoretical claims.
- I noticed that in the second paragraph of Introduction, all the citations are copied from the 4th paragraph  of introduction of https://proceedings.neurips.cc/paper_files/paper/2023/file/dea2b4f9012686bcc1f59a62bcd28158-Paper-Conference.pdf. The general flow is also similar. The mentioned paper seems to tackle a different problem, so I don't suspect this paper plagiarizing it, but borrowings like this don’t look good. I hope the authors will make sure not to copy-paste things (almost) directly from other papers.

### Questions
A key technique used with RBF kernels (and not only with them) is automatic relevance determination (ARD), when each input coordinate corresponds to its own length scale parameter, each optimizable; or even when an input vector is multiplied by an optimizable matrix. The separate length scales are often used for interpretation, as a measure of relevance of each individual coordinate, which makes them a natural target for your study. Can your results be applied in this setting? Adding this would make the paper stronger.

(Minor) suggestions:
- In the abstract, perhaps you want to change “time series" into “time series forecasting” or “analysis of time series”, or something like that. Just “time series” doesn’t read like a “domain”.
- Lines 093-096, you mention non-identifiability of Matérn covariances, but you forget to mention that it only holds for dim <= 3.
- Line 132. “if for any” -> “if for all”.
- Line 198. “or they are supported on disjoint sets” - I strongly object to this intuition. Consider a non-degenerate Gaussian supported on $\mathbb{R}^2$ and a degenerate Gaussian supported on the line $\\{0\\} \times \mathbb{R} \subset \mathbb{R}^2$. These measures are orthogonal, but the support of the latter is a subset of the support of the former, the supports are not at all disjoint. Yes, you could exclude $\\{0\\} \times \mathbb{R}$ from the support of the former measure if you treat things up to probability 0 events, but this is not very natural and thus doesn't give a good intuition.
- Line 248. Please give a reference for the spectral density of Matérn kernels for the specific notion of the Fourier transform that you are using.
- Line 377. The notation $\\{ \pm s_1 \pm s_2 \pm \dots \pm s_m \\}$ is unclear, please expand on what you mean exactly by this.
- Lines 404-406. “In fact, even for simple kernels like the SE and Matérn kernels, whether the MLE is consistent remains open, and we still do not know whether the likelihood is unimodal or not.” - please support this claim by a reference.
- Please polish your reference list. As an example, in line 545, the word “gaussian” is missing a capital “G”.

### Soundness
3

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
4

### Summary
This paper addresses the identifiability issue of the hyperparameters of Gaussian Processes when holomorphic kernels are used. A novel theory is proposed that may help identify when hyperparameters are identifiable and when not, allowing meaningful interpretations in the future. From my own experience, the identifiability of hyperparameters for GPs is an important issue to address.  

The writing style and obvious practical implications made this paper an easy and interesting read.

### Strengths
- well written.
- a great contribution to answering the long-standing and practical-important question of identifiability for GPs.
- digestible theory.
- immediate practical impact.

### Weaknesses
This is a strong paper, I only have one major and a few minor issues with some of the presentation: 
Major: 
(1) The simulation results, while certainly confirming the theory, are insufficient to convince a critic. Identifiability of hyperparameters is such a rich and practical topic that the results seem somewhat bleak and unimpressive. My suggestions are to apply the methodology to a real dataset --- something of high impact, such as climate, or the mentioned spatial transcriptomics --- show the effects of misidentification by plotting and evaluating results (CRPS, RMSE) and possibly showing relevant snapshots of the log marginal likelihood function. In addition, where the data comes from right now is not well explained. The inputs are defined, but it only says "After generating the outputs". Please be more specific about where the data comes from. 

Minor:
(1) There are some errors in the text "summarize(s) existing literature", or table "above" when it is below. 
(2) The paragraph after Def. 3 is a little convoluted, possibly due to a grammar mistake, but it's hard to tell. Please be a little more specific and explicit in your logic there. 
(3) It would be valuable to the reader to discuss how other training methods (MCMC, Variation Inference) deal with the identifyability challenge. I would guess MCMC as a sampler might deal really well. This would be a great addition.

### Questions
- What is the impact of identifiability on the function approximation and uncertainty quantification of a real dataset? 
- How does non-identifiability might affect prediction quality? 
- What does the log marginal likelihood function look like in such a case?
- How do MCMC and variational inference deal with non-identifyability?

### Soundness
3

### Presentation
3

### Contribution
3
