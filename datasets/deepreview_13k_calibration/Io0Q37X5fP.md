# Counterfactual Generative Models for Time-Varying Treatments

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Estimating the counterfactual outcome of treatment is essential for decision-making in public health and clinical science, among others. Often, treatments are administered in a sequential, time-varying manner, leading to an exponentially increased number of possible counterfactual outcomes.
Furthermore, in modern applications, the outcomes are high-dimensional and conventional average treatment effect estimation fails to capture disparities in individuals. 
To tackle these challenges, we propose a novel conditional generative framework capable of producing counterfactual samples under time-varying treatment, without the need for explicit density estimation. 
Our method carefully addresses the distribution mismatch between the observed and counterfactual distributions via a loss function based on inverse probability re-weighting, and supports integration with state-of-the-art conditional generative models such as the guided diffusion and conditional variational autoencoder.
We present a thorough evaluation of our method using both synthetic and real-world data. 
Our results demonstrate that our method is capable of generating high-quality counterfactual samples and outperforms the state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a framework that can be used to simulate counterfactual outcomes in temporal experiments. The proposed method is a combination of conditional variational autoencoder and inverse probability weighting.

### Strengths
The proposed framework is simple, easy to use, and accessible. Judging from the experiments, the performance of the proposed method seems to be good.

### Weaknesses
 - Proposition 1 doesn’t make sense. How could $\bar{a}$, a fixed value, be drawn from $\mathcal{D}$? Why is it a sum instead of an average? Wouldn’t the RHS of (4) be the same for all $\bar{a}$ while the LHS is supposed to be different? And why is the index in (5) from $t-d$ instead of from $t-d+1$? In proof of proposition 1, where does the expectation over $\bar{a}$ come from? I would be concerned if the authors actually used this formula in their experiments.

- I don’t seem to understand the comment in Remark 1 that doubly robust methods are less robust to model misspecification than IPW methods, and I cannot find relevant discussions in Appendix D as claimed. I'm curious about why the authors would think so.

- One pivotal assumption is that d, the length of history dependence, is finite and known, in which case the IPW methods in a temporal experiment are only a trivial extension to IPW methods in a static experiment. Also, as d gets large, the variance of those IPW-style methods can easily blow up.

- The only theoretical guarantee provided in the paper is that the weighted log likelihood is unbiased. In that sense, this is closer to treatment effect estimations where the estimand of interest is a single value, and it is very different from density estimations. Kennedy et al. (2023) (and some of the other papers mentioned by the authors) require stronger conditions simply because their goals are a lot harder. Since this paper is purely applied, I don’t see how they are comparable.  

- Related to the last point, I fail to see how the absence of a unified theory for doubly robust density approximation in longitudinal settings serves as a reason for not using DR estimators, given that the authors never estimated the density. When the goal is not density estimation, there have been a plethora of studies on variations of IPW and AIPW estimators in longitudinal settings, especially from the dynamic treatment regimes and reinforcement learning literature.

- I find the notations occasionally confusing, and the authors are somewhat vague regarding the assumptions.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author delved into examining the counterfactual results of treatments in dynamic treatment scenarios. They introduced a novel generative framework designed to produce counterfactual outcomes without explicitly learning the counterfactual distribution. In their approach, they put forth a learning objective that relies on reweighted Evidence Lower Bound (ELBO) within a conditional Variational Autoencoder (VAE), utilizing inverse propensity weights.

### Strengths
- Paper tackles the complex issue of estimating counterfactual outcomes in the face of time-varying treatment effects.
-The proposed method adeptly handles high-dimensional outcomes.
- Capable of generating counterfactual samples without imposing rigid assumptions on the distribution of the counterfactual outcome.

### Weaknesses
IPTW values can be notably small and, as highlighted by the author, require precise definition. This circumstance can exacerbate in sequential treatment scenarios.

Given we're handling a treatment sequence, it's important to note that the counterfactual treatment is not unique. However, the notation used does not reflect this.

I believe the following two papers could also serve as baseline references:
1. "Disentangled Counterfactual Recurrent Networks for Treatment Effect Inference Over Time"
2. "Estimating Counterfactual Treatment Outcomes Over Time Through Adversarially Balanced Representations"

### Questions
If x isn't utilized in the generator, what's the rationale for calculating weights based on x? Why not solely estimate treatment probability based on the treatment sequence?

Can you provide a proof for equation 2? What would be the difference in objective if we were to define the distance in terms of Maximum Mean Discrepancy (MMD) or Wasserstein distance?

Considering your framework, it appears straightforward to expand it to the individual outcome level. What led to the decision to overlook that possibility?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a method to estimate the high-dimensional counterfactual distributions for time-varying treatments. The method uses a generative model to do the task. The generative model allows for generating credible samples of the counterfactual outcomes given a time-varying treatment such that policymakers can assess a policy’s efficacy by exploring a range of probable outcomes and deepening their understanding of its counterfactual result.

### Strengths
The paper is technically sound. Generally, it is not hard for readers to follow. The ideas are presented well, but still, the clarity of the paper can be further improved.

### Weaknesses
Although readers should be able to follow and understand the notions presented in the paper, the paper is not organized well. For instance, the authors defer the standard causal assumptions to the Appendix.  The authors may not give detailed explanations about the causal assumptions in the main paper, but at least mention the names of the causal assumptions in the paper. Please refer to questions for further weakness.

1. In Algorithm 1, the authors suggest that we should draw a sample epsilon from $N(0,I)$, where $I$ is the total number of individuals. What is the point of setting epsilon as a realization with large variance? Usually, $I$ can be very large. Indeed, if there are a large number of individuals, say $I=10000$, a realization can be very large. Further, why do you model epsilon as normally distributed?

2. I have a question about the training process. The objective function is given in Eqn. (2) which is approximated by Eqn. (5). Nevertheless, the computation is given for each t only, where t lies in between 1, … , T according to the paper. We can obtain T approximations according to Eqn. (5). During training, the goal is to minimize one objective value, but we can calculate T approximations where each of the T approximations can be thought of as the objective value. What should be the objective value of training?

3. In the paper, the authors state that t=1, …, T in the section of PROBLEM SETUP. However, when the authors present Algorithm 1, t = d, …, T. It is strange that t=d, …, T in Algorithm 1. Is it a typo mistake? If not, from my realization about Algorithm 1, d should be determined. How to determine the value of d?

### Questions
1. In Algorithm 1, the authors suggest that we should draw a sample epsilon from $N(0,I)$, where $I$ is the total number of individuals. What is the point of setting epsilon as a realization with large variance? Usually, $I$ can be very large. Indeed, if there are a large number of individuals, say $I=10000$, a realization can be very large. Further, why do you model epsilon as normally distributed?

2. I have a question about the training process. The objective function is given in Eqn. (2) which is approximated by Eqn. (5). Nevertheless, the computation is given for each t only, where t lies in between 1, … , T according to the paper. We can obtain T approximations according to Eqn. (5). During training, the goal is to minimize one objective value, but we can calculate T approximations where each of the T approximations can be thought of as the objective value. What should be the objective value of training?

3. In the paper, the authors state that t=1, …, T in the section of PROBLEM SETUP. However, when the authors present Algorithm 1, t = d, …, T. It is strange that t=d, …, T in Algorithm 1. Is it a typo mistake? If not, from my realization about Algorithm 1, d should be determined. How to determine the value of d?

### Soundness
2 fair

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
This study addresses an important issue of causal inference (counterfactual outcome in time-varying situation) by generating a counterfactual distribution. They conducted various experiments as well as getting good results. I think this is a nice paper. However, there are many parts of this paper where the interpretation needs to be improved. As I have been busy lately, it is possible that there are some details that I have not checked sufficiently.

### Strengths
1. This study proposes a new approach that can be used for high-dimensional outcomes. Most existing studies consider low-dimensional outcomes.
2. Addressing the issue of counterfactual outcomes by generating counterfactual distributions is interesting.
3. They conducted experiments on various datasets. Importantly, they used real data.
4. The experiment results provided by the authors are good.

### Weaknesses
1. Many parts of the explanation need to be improved. For example, authors focus on describing what they did and used, but not why they did it. How do readers use this model to solve causal issues, such as ITE estimation? In addition, for the description of datasets, readers may wonder what is the treatment in these datasets (authors only said "treatment variable"). Specifically, the authors should clarify how the generative model's output can be used to estimate individual-level treatment effects, or if the method is fundamentally designed for population-level inference only, then this should be clearly stated. The description of the treatment variable is also too vague. For instance, in the COVID-19 datasets, what specific interventions are being modeled as the treatment? Is it mask mandates, lockdowns, or other policies? This needs to be clearly specified for each dataset used.
2. Lack of comparison of technological innovations from previous approaches. It might be helpful to understand the contribution of this paper by adding a paragraph discussing this. The current comparison to other methods is limited to experimental results. A more detailed comparison of the technical differences and innovations of the proposed method compared to existing methods like G-Nets, and KDE-based approaches is necessary. For example, how does the proposed method handle time-varying confounders and high-dimensional outcomes compared to these baselines?

### Questions
1. How should readers use your methods to estimate ITE?
2. What do treatments represent in the datasets used in experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
