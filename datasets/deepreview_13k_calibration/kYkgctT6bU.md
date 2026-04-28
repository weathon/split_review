# Practical and Rigorous Extremal Bounds for Gaussian Process Regression via Chaining

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Gaussian Process Regression (GPR) is a popular nonparametric regression method based on Bayesian principles that, unlike most machine learning techniques, provides uncertainty estimates for its predictions. Recent research has focused on robustness to model misspecification but has neglected improvements to the underlying methods for computing bounds. Inspired by the chaining method, we applied it to the prediction intervals of GPR. This work addresses the limitations of current GPR methods, which rely heavily on scaling posterior standard deviations and assume well-specified models, limiting their adaptability and accuracy. We propose a novel chain-based approach that decomposes the problem into smaller, refined stages, enabling better error control and enhanced robustness, particularly in challenging scenarios. Additionally, we innovate by providing tighter,  practical and theoretically sound bounds for commonly used kernels, including RBF and Matérn, improving both their theoretical understanding and practical utility. Numerical experiments validate our theoretical findings, demonstrating that our method outperforms existing approaches on synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper focuses on the problem of enhancing robustness to model misspecification in Gaussian process regression (GPR). In particular, taking important inspiration from the chaining methods of Talagrand (2014), the manuscript introduces new chaining bounds (lower and upper) for evaluating the prediction intervals of GPR. The work first revisits a decent amount of previous work, refreshes a key part of Talagrand (2014)'s contributions, derives the bounds for both RBF and Matern kernels, and finally evaluates them on a few datasets also comparing with another 3 methods.

### Strengths
The manuscript starts very well, with a clear description of the goals and contributions to be introduced. Later on, the review of SOTA methods and references to chaining methods in the Related work is quite enlightening. I really enjoyed reading it.

Definitely, the idea of taking chaining methods and in particular Talagrand's (2014) bound of Theorem (1) for later combining it with the Expectation of a non-negative variable Y in Eq. (3) is interesting. It is however difficult for me to evaluate the degree of the contribution here, even the novelty, but that part is a strength of the paper. 

I do not particularly think that sections 4.1 and 4.2 + 4.3 are strengths of the manuscript for several reasons that I will add later in the weaknesses part. Additionally, the aspect of comparing the bounds with three recent methods is a good point, and performance seems to be on-pair or better than them (not sure if I would say "stellar" as written in L481).

### Weaknesses
Three thoughts that make me concerned and that I do think are points of weakness in the manuscript.

**[W1]** - The paper spends quite a lot of effort in motivating and adding context to the problem, so far the related work part is really good to me. However, after the introduction of Talagrand's method, the re-definition of RBF and Matern kernels is extremely trivial, as they are super well-known. The main problem here is that it stops the flow of explanations, and the thread of the context is lost. Later on, bounds are not really introduced but just written with two unnecessary proofs (they should really go into the Appendix). With this, I'm basically saying that bounds are not put into context and clarity is far from what is expected for a submission of this type.

**[W2]** - I'm not entirely convinced by the empirical results. Defining the performance as stellar is perhaps a bit far from humble, in my opinion, but more important than that is the analysis and evaluation of what bounds are indicating. Why is that wave-style behavior happening in Figure 1c? Is it due to the pre-training of the GP hyperparameters of some weird length-scale? I'm curious in the sense that it is different from the rest of SOTA methods.

**[W3]** - It seems that this should not be mentioned, but I have to do it. In the paper, all the scalability issues of GPR are completely ignored. In that regard, I cannot stop asking myself what is the maximum number of observations that one can consider for using Algorithm 1. Moreover, I am curious about the computational cost of such bounds, which is neither considered.

### Questions
Some additional questions that I thought about while reading the work.. and one minor typo:

**[Q1]** - L84: *"When many variables Xt in T are nearly identical, strong correlations between them can obscure the true variation in the process. Grouping similar variables together helps reduce this redundancy by allowing us to approximate these highly correlated variables with a representative value"* — Does this have a theoretical justification?

**[Q2]** - L97: for sufficiently large n, pi_n(t) equals t and the approximation stops.

**[Q3]** - For completeness, it would be nice to make a mention of some probabilistic bounds for GPR, i.e. Adaptive Cholesky Gaussian Processes (Bartels et al. AISTATS 2023 ) — as there is a similar spirit in some degree.

**[Minor1]** - L133 More “ecently”

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper derives chaining bounds for GPR prediction intervals, inspired by Talagrand’s chaining method. This approach improves flexibility and accuracy in handling model uncertainty, overcoming issues with standard scaling of posterior deviations and assumptions of well-specified models.

### Strengths
1. The uncertainty quantification problem in GPR framework is very important to the community.

2. The chaining-based approach seems novel to me.

3. The bound provided in this paper is very clean, with a neat proof, and practical value.

4. The numerical results are presented clearly.

### Weaknesses
1. It's not clear how Theorem 1 relates to GPR bound problem. I suggest the authors to include a short discussion after Theorem 1, discussing why it's important here. 

2. $t_0$ remains a magic until the concrete algorithm is presented. For instance, what's $t_0$ in GPR setup? Is it a training sample, a test sample, or something else? I suggest the authors to explain it earlier, say, after Theorem 1 or Theorem 2. Otherwise non experts may be confused when reading Section 4. 

3. All examples in Figure 1 are for extrapolation (aka forecasting), but the theorem and the algorithm doesn't really depend on this setup, right? If so, can the authors either explain whether the method works for extrapolation only; or provide at least one more example to show it works for interpolation (aka infill)? 

A minor issue: the font of the metrics in Section 5.2 is not consistent. For example, $PICP=$ should be $\mathrm{PICP}=$.

### Questions
In additional to the questions in the above weakness section, I have some additional questions.

1. Can the Theorem for RBF and Matern 3/2 be extended to a generic Matern with arbitrary smoothness? If not, can the authors briefly discuss the main challenges, and at least provide the bound for nu = 1/2 and 5/2, which are also popular in practice?

2. What happens if the domain dimension is higher? Does it impact the bound? Theoretically it seems that the answer is no, but in practical I think it matters, given the fact that GPR doesn't work really well when the domain dimension is very high, say, 100.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work explores a novel method for establishing robust bounds on the predictions of Gaussian Process Regression (GPR) models. Specifically, they apply a chaining method (Talagrand 2014) for the particular cases of RBF and Matern kernels. This is tested empirically on real world datasets against existing baselines.

### Strengths
The paper is well written and clearly structured.

The application of chaining is novel and the area of application is of high interest.

The proposed method is tested on a selection of real world data and suitable baselines are chosen.

### Weaknesses
I have several concerns relating to the presentation of the empirical results:

- Specification of confidence interval
It is stated that the adopted confidence interval is (1-alpha) but I did not see alpha specified (apologies if I missed it), nor did I see results for different values of alpha. I'd recommend at least two different values are explored, though these extra results could be in the appendix.

- Presentation of PICP 
In Table 1, the PICP metric has an up arrow next to it, implying higher values are always better. This is not the case. Ideally, PICP should be very close to the nominal confidence level, not significantly exceeding the target. I'd recommend removing the arrow, and also clarifying some of the text to reflect this. For example, the statement " in Figure 1(a), one test point remains uncovered" is not by itself indicative of good or bad performance.

- Uncertainties in metrics
All of the metrics in the table are lacking uncertainty estimates, therefore the reader is left unable to determine whether the differences in metrics are statistically significant. Adding these uncertainties in is crucial if we are to draw rigorous conclusions.

### Questions
Aside from addressing the concerns on the empirical results in the Weaknesses section, I have a couple of further questions:

 - Title
One of the papers most frequently cited (and benchmarked) in this work is Fiedler et al. (2021),  which is entitled "Practical and Rigorous Uncertainty Bounds for Gaussian Process Regression". Is there a risk that readers may become confused by the close similarity to the title of the current paper which as it stands is "Practical and Rigorous Extremal Bounds for Gaussian Process Regression via Chaining"? I would recommend that the authors consider some suitable alternative.

- Scalability
What can we say about the computational cost and scalability of this method? How long do the different methods take to compute, and how does this scale with data size N?

### Soundness
3

### Presentation
3

### Contribution
2
