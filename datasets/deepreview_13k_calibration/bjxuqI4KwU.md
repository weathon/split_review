# Linear SCM Identification in the Presence of Confounders and Gaussian Noise

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Noisy linear structural causal models (SCMs) in the presence of confounding variables are known to be identifiable if all confounding and noise variables are non-Gaussian and unidentifiable if all are Gaussian.
    The identifiability when only some are Gaussian remains concealed. 
    We show that, in the presence of Gaussian noise, a linear SCM is uniquely identifiable provided that \emph{(i)} the number of confounders is at most the number of the observed variables, \emph{(ii)} the confounders do not have a Gaussian component, and \emph{(iii)} the causal structure of the SCM is known.
    If the third condition is relaxed, the SCM becomes finitely identifiable; more specifically, it belongs to a set of at most $n!$ linear SCMS, where $n$ is the number of observed variables.
    The confounders in all of these $n!$ SCMs share the same joint probability distribution function (PDF), which we obtain analytically.  
    For the case where both the noise and confounders are Gaussian, we provide further insight into the existing counter-example-based unidentifiability result and demonstrate that every SCM with confounders can be represented as an SCM without confounders but with the same joint PDF.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper establishes general conditions under which linear structured causal models are identifiable in the presence of hidden confounding variables and Gaussian noise. Briefly, if the number of confounding random variables is at most the number of observable random variables, then a finite number of equivalent models can be recovered from observations of the observables (the number of models is $n!$, where $n$ is the number of observables). If, in addition, the confounders are non-Gaussian, then the model is uniquely identifiable. Some minor technical assumptions are needed.

### Strengths
This is a very general result on a fundamental model of causality.

### Weaknesses
The result is information-theoretic. It assumes perfect statistics and does not analyze the resilience to perturbations due to finite sampling. Also, the paper does not state clearly any algorithmic consequences (complexity etc.), though the methods are mostly linear-algebraic and hence possibly effective.

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper is a theoretical work on the identifiability problem of the linear structure causal models. Specifically, the authors showed that under the general Gaussian assumptions for all components, the linear SCM is unidentifiable. The authors also provided mild sufficient conditions for the linear SCM mode to be (i) uniquely identifiable or (ii) finitely identifiable.

### Strengths
- Originality: The paper is a novel work that discusses the identifiability of the SCM model under different model assumptions. 
- Quality: The paper provides a thorough discussion of the identifiability issue with complete theoretical justification. It is of high quality in terms of the results and writing. 
- Clarity: The paper is organized in a mathematical paper style. It is easy to follow the assumptions and theorems. 
- Significance: The result of this paper is appealing. The analysis is solid.

### Weaknesses
 - One assumption seems confusing to me (see details in the questions part).
- Although the paper has solid theoretical results, it is a bit difficult to directly apply the results to any real application as the assumptions are hard to verify for real data.



### Questions
Major questions:
1. Assumption 2 requires "Confounders $H_i$ .... cannot be decomposed into multiple random variables where any is Gaussian".  This is difficult to verify. Can this condition be translated to any condition on the characteristic functions? For example, suppose we let $Z\sim N(0, v)$ and let another independent variable $W$ have the c.f. $\phi_W(t)=\phi_H(t)e^{vt^2}$. Then $\phi_W$ should not be in $L_2$ space for any $v>0$. 
Also, this condition mentioned "multiple" random variables. 
However, any density function can be approximated by an infinite mixture of Gaussians (in the weak topology sense). Does this limit scenario break this assumption?

2. Suppose for a real data where $\mathrm{X}$ and $\mathrm{H}$ are collected. How do we verify the model is identifiable? 
3. For Definition 3, the rigorous definition for $X\stackrel{d}{=}Y$ should be: for any measurable set $A$ in the space, $P(X\in A)=P(Y\in B)$.  The equality in p.d.f. is a bit unrigorous. 
4. In terms of finding the equivalence class in Sec. 6, is that equivalent to finding the invariant permutations of $\mathbf{\Sigma}$, i.e. {$\mathbf{P}\in\mathcal P: \mathbf{P}\mathbf{\Sigma}\mathbf{P}^T$}, where $\mathcal P$ is the permutation class? If so, one can divide the indices {1,2,.., n} (corresponding to rows/cols of $\mathbf{\Sigma}$) into equivalent classes ($i\sim j$ if and only $\Sigma_{ik}=\Sigma_{jk}\ \forall k$). The invariant permutation of $\mathbf{\Sigma}$ is group-isomorphic to the direct product of the permutation groups of the equivalent classes.

Minor issues:
1. For narrative citations, please remove the paratheses. 
2. Pg. 2. Ln 56. Add a space between "," and "$\mathbf{B}$".
3. Remarks 4 and 5 are important results. They can be transformed into two Theorems/Propositions.

### Soundness
3

### Presentation
4

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
The paper discusses identifiability criteria for linear structural causal models (SCMs) with different scenarios for Gaussianity of confounders and noise, and varying assumptions. More specifically, the paper fills in the gap of identifiability for Gaussian noise and non-Gaussian confounders. The main proof technique involves analysis of characteristic functions and reliance on Gaussian properties. Some numerical examples are provided.

### Strengths
The paper shows that linear SCMs with Gaussian noise are finitely identifiable under the assumption that confounders are non-constant and cannot be decomposed into random variables where any are Gaussian (Assumption 2). This result fills in gaps in identifiability where earlier results already identified finite identifiability of SCMs with non-Gaussian noise and confounders. From this perspective, the paper contributes original new results.

In terms of significance, it is clear that the main results contribute to the field of linear SCMs and is a relevant topic for the conference. While the framework may be simple, the main results are interesting. 

Finally, it is worthwhile to point out that the paper is clearly polished. The authors provided an extensive discussion of existing literature, problem formulations, main results, and concerns.

### Weaknesses
 - The linear model framework restricts the scope of the paper
- As the authors also pointed out, there are no discussions of algorithms to find an SCM
- Novelty in proof techniques are limited and appear to be a mixture of gaussian properties, characteristic function analysis, and reliance on Gaussianity assumptions

While the points above raise concerns of weaknesses on the applicability of the results, the paper's main theoretical results are still meaningful and interesting.

### Questions
The paper does a good job of addressing multiple aspects of the problem. The largest concern is the scope of the problem and whether it has sufficient significance. Some questions and suggestions include:

1. It may be helpful to highlight the main theoretical tools used in the proof (i.e., the use of characteristic functions) and connect these tools with other contexts beyond the SCM. While the technique may be novel within applications to SCM, it is not particularly novel in the broader statistical literature. Are there other areas in machine learning that can significantly benefit from the techniques?

2. Regarding causal orders -- the SCM is uniquely identifiable given the causal order, provided gaussian noise and non-gaussian confounders. What if an expert only gives a partial order, would it still be uniquely identifiable in some scenarios?

3. Are there any existing results in identifying the SCM that can benefit from results presented in this paper? How are the results of identifiability connected with classical results in estimating linear model parameters?

4. A minor typo: Line 125 "novel approached".

### Soundness
3

### Presentation
3

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
The paper investigates the identifiability of noisy linear structural causal models (SCMs) in settings where confounders and noise variables have distributions with Gaussian and/or non-Gaussian components. Specifically, the authors investigate necessary and sufficient conditions for the SCM to be uniquely, finitely or infinitely identifiable, depending on the distributions of confounders and noise and certain assumptions on the causal structure of the model. Theorem 1 extends the known counter examples addressing identifiablity under Gaussian confounders.

Theorem 2 provides sufficiency conditions for linear SCM's to be finitely identifiable and provides a wonderful characterization in terms of the number of permutations and the characteristic function of the confounders. Theorem 3 characterizes when a permutation of an SCM leads to a new SCM and affects the causal order. Section 6 provides numerous examples and illustrations of the results.

### Strengths
Solid contributions: The paper provides significant insights into SCM identifiability, that extend existing work. 

Clear writing and proof structure: The writing is clear and concise, with proofs that are both rigorous and easy to follow. The presentation of theoretical results is structured and clear. I enjoyed reading the article.

### Weaknesses
I think the writing/accessibility of the article could be improved slightly:

Grammar and Punctuation: There are minor punctuation issues in the introduction, particularly with the use of commas. For example in line 41, line 42, or "It is near impossible to claim that all causes of a specified process are considered, and hence, the consideration of confounders is inevitable" in line 49 (I would suggest "It is nearly impossible to claim that all causes of a specified process are considered; hence, the consideration of confounders is inevitable." or two separate sentences).

Certain definitions can be assumed to be known by the reader, such as Definition 3 and Definition 7 (along with Remark 2 and Remark 3). I would suggest moving these to the appendix to streamline the main text.

The examples illustrating Remarks 5 and 6 could use some further steps to help the reading along. This could be done in the appendix. 

Typos:
line 67: "base on"
200: \ref used instead of \eqref{}
387: 'is' illustrated by SCMs:

### Questions
Full identifiability of a causal model is typically a strong ask. Often, one only cares for a small part of the model to be identifiable (e.g. some treatment effect). Do the findings of the authors (in particular Theorem 2) give immediate insight in when part of the model is uniquely identifiable, even when the full model is not?

### Soundness
4

### Presentation
3

### Contribution
3
