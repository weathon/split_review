# Learning Counterfactually Invariant Predictors

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
\noindent
Notions of counterfactual invariance (CI) have proven essential for predictors that are fair, robust, and generalizable in the real world. We propose graphical criteria that yield a sufficient condition for a predictor to be counterfactually invariant in terms of a conditional independence in the observational distribution. In order to learn such predictors, we propose a model-agnostic framework, called Counterfactually Invariant Prediction (CIP), building on the Hilbert-Schmidt Conditional Independence Criterion (HSCIC), a kernel-based conditional dependence measure. Our experimental results demonstrate the effectiveness of CIP in enforcing counterfactual invariance across various simulated and real-world datasets including scalar and multi-variate settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a counterfactually invariant prediction (CIP) method for achieving fairness, robustness, and generalization in the real world. By enforcing independence in kernel space with the prior causal structure, CIP achieves counterfactual invariance.

### Strengths
1. Theoretical analysis is sufficient, and the studied problem isinteresting.

### Weaknesses
1. My main concern is on the usage of counterfactual invariance. Counterfactual refers to individual-level potential outcomes, rather than conditional or sub-populational levels. Hence, pursuing counterfactual outcome relies on prior SCM model or very sharp bounds, and estimating counterfactual outcome from observational is nearly possible even with the aid of AB tests. Hence, as your independence regularization only enforces tthe populational independence, how can your CIP achieves targets in the counterfactual level?
2. Such invariance learning is not new to me. 
3. Prior causal graph is restrictive for realistic applications.

### Questions
See Weaknesses

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose graphical criteria that yield a sufficient condition for a predictor to be counterfactually invariant in terms of a conditional independence in the observational distribution. In order to learn such predictors, they propose a model-agnostic framework, called Counterfactually Invariant Prediction, building on the Hilbert-Schmidt Conditional Independence Criterion, a kernel-based conditional dependence measure.

### Strengths
Their experimental results demonstrate the effectiveness of their method in enforcing counterfactual invariance across various simulated and real-world datasets including scalar and multi-variate settings.

### Weaknesses
Please refer to Questions.

In figure 1(a), what is S and what is X? How does one distinguish the two or say how to decide which is S and which is X?

Sometimes the authors write "$\hat Y$ is counterfactually invariant in $A$ with respect to $W$", sometimes they write "$\hat Y$ is counterfactually invariant in $A$ with respect to $X$". Do they have the same meaning?

Theoretical results. Corollary 3.6 gives a population result about VCF($\hat Y$). However, no theoretical results on finite sample estimator are established.

### Questions
In figure 1(a), what is S and what is X? How does one distinguish the two or say how to decide which is S and which is X? 

Sometimes the authors write "$\hat Y$ is counterfactually invariant in $A$ with respect to $W$", sometimes they write "$\hat Y$ is counterfactually invariant in $A$ with respect to $X$". Do they have the same meaning? 

Theoretical results. Corollary 3.6 gives a population result about VCF($\hat Y$). However, no theoretical results on finite sample estimator are established. 

Besides fairness, what are other applications for learning counterfactually invariant predictors?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a graphical criterion to learn counterfactually invariant predictors by leveraging conditional independence within the observational distribution. The Hilbert-Schmidt Conditional Independence Criterion (HSCIC) is employed as a measure of conditional independence. Experimental results, based on both synthetic and real data, validate the efficacy of the proposed approach.

### Strengths
- Learning counterfactually invariant predictors solely from the observational distribution is a relevant and important research problem in the field of causal inference. 

- The extensive experiments on synthetic data and real data are conducted to demonstrate how the proposed method works.

### Weaknesses
 - A strong limitation of Theorem 3.2, which corresponds to the issue in the experiments mentioned next. The assumption made in Theorem 3.2, which presumes that $X = g(X, ...)$, seems to be a strong assumption. The authors clarify that this assumption implies $pa(V) \in \mathbf{X} \cup \mathbf{A}$, which should imply $\mathbf{A} \cup \mathbf{X}$ should be a maximal connected graph (and so $\mathbf{A} \cup \mathbf{W}$ ) and $Y$ is a root node, meaning $Y$ cannot be any parent of $\mathbf{X} \cup \mathbf{A}$. Therefore, for a common connected DAG with node $\mathbf{A} \cup \mathbf{W} \cup \mathbf{Y}$, the adjustment set for $(\mathbf{A} \cup \mathbf{W}, \mathbf{Y})$ should be empty, which corresponds to the issue in experiments mentioned below.

- The fairness example in section 4.3 is based on Fig. 1(e), where our goal is to learn a predictor $\hat{Y}$ that exhibits counterfactual invariance with respect to $\mathbf{A}$ within the context of $\mathbf{W}=\mathbf{X} \cup \mathbf{C}$. As per Theorem 3.2, our first step is to identify a valid adjustment set $\mathbf{S}$ for $(\mathbf{A} \cup \mathbf{W}, \mathbf{Y})$. However, in this case, the adjustment set $\mathbf{S}$ between $\mathbf{A} \cup \mathbf{W}$ and $\mathbf{Y}$ should be empty. Upon reviewing Appendix F.5 and Fig. 8, it seems that it is inappropriate to use a subset of $\mathbf{A} \cup \mathbf{W}$ as the adjustment set. A similar issue arises in the experiments conducted on synthetic and image datasets, in which, we have $\mathbf{W}$ encompassing all variables except for $\mathbf{Y}$ and $\mathbf{A}$. Besides, notice that, in the latter case, the authors state that 'We seek a predictor $\hat{Y}$ that is CI in the x-position with respect to $\textbf{all other observed variables}$', so $\mathbf{W}$ includes all the observational variables except $\mathbf{Y}$ and $\mathbf{A}$ as well.

- Clarification on the 'Injectivity' Assumption in Theorem 3.2. Fawkes & Evans (2023) shows that CI cannot be decided from the observational distribution unless strong assumptions are made. Theorem 3.2 provides a valid assumption: injectivity of $g$. I searched for the term ‘injectivity’ in the proof but cannot find it, so how does this assumption work here? Furthermore, while the authors claim that ‘Guaranteeing CI necessarily requires strong untestable additional assumptions, but we demonstrated that CIP performs well empirically even when these are violated’, they only provide an example of a specific violation scenario involving the absence of unobserved confounders. It is recommended that the authors conduct additional experiments to demonstrate the method's efficacy under more general violation conditions.

- Scalability and Computational Complexity. The experimental section primarily employs simple causal graphs with a small number of nodes. It is essential to evaluate the scalability of the proposed Counterfactual Invariance Predictor (CIP) on causal graphs with a larger number of nodes, such as 20, 30 nodes. Additionally, it would be better to provide insights into the computational complexity associated with finding the adjustment set and estimating the Hilbert-Schmidt Conditional Independence Criterion (HSCIC).

- Organisational Improvement. Section 2.2, "Related Work," requires more structured organization. Although the section discusses almost sure conditional independence, distributional conditional independence, and F-CI along with their relationships, it appears that they may not directly relate to the contributions of this work. Therefore, it would be advisable to omit this portion. Moreover, the paper should offer a concise and focused overview of the approaches used in prior research to attain counterfactually invariant predictors.

### Questions
How was the synthetic experiment design tailored to meet the assumption in Theorem 3.2 (injectivity assumption) explicitly?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
