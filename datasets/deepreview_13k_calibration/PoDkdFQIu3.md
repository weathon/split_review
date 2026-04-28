# A Linear Algebraic Framework for Counterfactual Generation

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Estimating individual treatment effects in clinical data is essential for understanding how different patients uniquely respond to treatments and identifying the most effective interventions for specific patient subgroups, thereby enhancing the precision and personalization of healthcare. However, counterfactual data are not accessible, and the true calculation of causal effects cannot be performed at the individual level. This paper proposes a linear algebraic framework to generate counterfactual longitudinal data that exactly matches pre-treatment factual data. Because causation travels forward in time, not in reverse, counterfactual predictability is further strengthened by blocking causal effects from flowing back to the past, thus limiting counterfactual dependence on the future. Using simulated LDL cholesterol datasets, we show that our method significantly outperforms the most cited methods of counterfactual generation. We also provide a formula that can estimate the time-varying variance of individual treatment effects, interpreted as a confidence level in the generated counterfactuals compared to true values.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work focuses on estimating time-varying individualized treatment effects within a linear model. The authors formulate a linear static-state model and provide a novel method to estimate the corresponding counterfactual data. They have demonstrated that the proposed approach can achieve better performance in their experiments.

### Strengths
1. Generating the counterfactual data is a challenging task.

2. The proposed method is both novel and interesting.

3. The analyses are sound and presented in a logical manner.

### Weaknesses
1. The method is only applicable to linear models.

2. In some instances, the description is not sufficiently clear. For example, the model's explanation here lacks clarity, particularly in the description of assumption 2, which necessitates further comprehension through reading the instructions in the appendix.

### Questions
Can you provide an intuitive explanation for Assumption 2? Typically, people use a linear dynamical system model to describe the generative mechanism. It would be beneficial to include some descriptions in the main text rather than placing them in the appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on counterfactual generation. In particular, it introduces a Gaussian mixture model as a prior probability distribution over the static states, and uses it as a generative model for synthetic counterfactual longitudinal data. The proposed method can be used to estimate the individual treatment effects (ITE) using the synthetic counterfactual outcomes data.

### Strengths
This paper considers counterfactual generation, which is an important problem. Also, it uses a Mixture of Gaussians to approximate general data distributions; this is the main difference compared to previous papers.

### Weaknesses
The difference of the proposed method is that it assumes a Gaussian mixture model to approximate distributions, in contrast to previous works which employed neural networks. However, the experimental results may not provide sufficient evidence to fully assess the performance of the proposed method. Notably, the paper lacks experimental results on benchmark datasets such as IHDP and Jobs.

The paper asserts its ability to identify ITE as defined in Equation 11 and provides results on ITE estimation accuracy. However, it's important to note that the defined ITE is a random variable. Consequently, I'm uncertain whether the reported results pertain to ITE itself or its expected value.

### Questions
Are the reported results regarding ITE or the expected value of ITE?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a linear algebraic framework for generating synthetic counterfactual data that matches pretreatment factual data. The approach claims to be the first-ever counterfactual generative model for creating personalized clinical trial digital twins. The method outperforms other methods of counterfactual generation and individual treatment effect estimation, as demonstrated using simulated ground truth counterfactual data. Additionally, the paper provides a formula to estimate the time-varying variance of individual treatment effects, which can be interpreted as a confidence measure for the generated counterfactuals.

### Strengths
- The paper is well-written and easy to follow.

- The experiments on California cigarette sales data and simulated LDL cholesterol data showcase the effectiveness of the proposed method as some extent.

### Weaknesses
 - The motivation of this paper is unclear. The contribution also seems limited. The restriction on counterfactual generation that receiving treatment at a time $T_0$ cannot cause any difference reversely to counterfactual generation at $t < T_0$, comes across as self-evident. It remains ambiguous whether prior research infringed upon this constraint. The comparative advantages of the introduced method with the existing work are not distinctly highlighted, leading to a gap in understanding its unique value proposition.

- To evaluate how true synthetic counterfactuals are, more experiments on synthetic datasets including ground-truth counterfactual data are required. It would be insightful to demonstrate the method's robustness under diverse treatment times and over prolonged post-treatment durations. 

- The paper could benefit from a rigorous theoretical exploration addressing the method's resilience against noise and confounding bias. Would this be challenging with such a linear framework?

- There is a lack of literature review or an introduction to some of the methods appearing in the experimental part, such as MC-NNM (Athey et al., 2021) and CGP (Schulam and Saria, 2017).

### Questions
Regarding Fig.4, what methodology did the authors employ to randomly produce counterfactual pre-treatment data?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the problem of generating synthetic counterfactual data that exactly matches pretreatment factual data under a linear algebraic framework (namely, the static state of the factual and counterfactual data are all in affine subspace). By defining the shift from a factual state to a counterfactual state under a soft intervention, the counterfactual data can be generated by solving the log-likelihood function as a static state analysis with priors of an ω-dependent Gaussian mixture model. Such a generation method can be used to estimate an ITE and the experimental results of the simulated data show that the proposed method outperforms the baselines in estimating ITE.

### Strengths
1. This paper deals with a challenging but important problem of counterfactual generation, which may be useful to the field of causal inference.

2. A practical estimating method is provided in estimating parameters (EM algorithms) and formalizes a generation process of counterfactual data according to estimated results. 

3. The experimental results verify the generated counterfactual data is useful for estimating ITE.

### Weaknesses
1. My main concern is the identification of parameters in the log-likelihood function, i.e., how to ensure the unique solution of target parameters by the EM algorithm. Specifically, the use of a Gaussian mixture model introduces the possibility of multiple local maxima, and it's unclear how the algorithm avoids converging to suboptimal solutions that would lead to inaccurate counterfactual generation. The paper should discuss the sensitivity of the results to different initializations of the EM algorithm and provide a more rigorous analysis of the parameter identifiability.

2. I think it is necessary to discuss the reasonableness for the same linear observation "W" in the factual data and counterfactual data generation. If the observation matrix "W" is learned from the factual data, then applying the same "W" to the counterfactual state seems to imply that the observation process remains unchanged after the intervention. This assumption needs more justification, as it may not hold in many real-world scenarios. Furthermore, if we resolve the "W" from factual data, we can naturally obtain the counterfactual state under this setting. Such a method does not surprise me and I guess there are some similarities with the SCM-based framework (used for estimating counterfactual framework).

3. Assumption 4 assumes that the soft intervertion on "s" is linearity and additive. Some limitations or reasonableness to it also require to be discussed. The assumption of a linear and additive intervention in the latent space might be too restrictive. Real-world interventions can often have complex, non-linear effects. The paper should discuss the potential impact of this assumption on the accuracy of the generated counterfactuals and consider scenarios where this assumption might not be valid.

### Questions
Refer to "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
