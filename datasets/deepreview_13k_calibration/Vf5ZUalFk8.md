# Conformal Reasoning: Uncertainty Estimation in Interactive Environments

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
We introduce conformal reasoning, a principled method for models in interactive environments to reason about their uncertainty and decide whether to seek out more information or to return a prediction. The challenge with standard conformal prediction---a popular statistical framework for uncertainty estimation that constructs prediction sets with formal coverage guarantees---is that it relies on a fixed set of calibration data points. In interactive environments, however, the calibration trajectories require certain termination criteria determined a priori, introducing heuristic bias and/or circular dependency that break the assumptions needed for coverage guarantees. We address this issue by building on adaptive conformal inference techniques. On two real-world tasks on medical diagnosis and embodied question answering, we show that conformal reasoning empirically achieves its theoretical coverage guarantees---in contrast with standard conformal prediction approaches that can significantly over- or under-cover---while improving exploration efficiency by approximately 20% on both tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a method called conformal reasoning. It extends the algorithm of Ren et al. to an online, multi-turn setting, and makes the set construction more flexible (no more running intersection needed) by applying theory from adaptive conformal prediction. Experiments are shown on medical diagnosis and question answering datasets.

### Strengths
* The english prose is written relatively well, and it was easy to follow. 
* I believe this problem setting is interesting and important to solve.
* Lifting the restriction of needing to take the running set intersection makes the algorithm of Ren et al. more practical.

### Weaknesses
(1)
There are fundamental and serious issues with the idea of terminating when |C| = 1, as proposed in Figure 1. To be fair, these problems appear not just in this paper, but in the prior work of Ren et al. as well. 

The issue is this: marginal coverage does _not_ guarantee coverage when |C|=1. The latter is a form of conditional coverage. Thus, on the termination event in Figure 1, the coverage guarantee provided by conformal prediction does _not_hold. That is, precisely on the event that the reasoning is deemed reliable (|C|=1), we cannot provide a reliability guarantee. (Formally, $\mathbb{P}(y \in C(x) \mid \|C(x)\| = 1)$ has no guarantee.)

Conformal prediction methods have been developed for abstention, such as the conformal alignment algorithm of https://arxiv.org/abs/2405.10301, or the conformal selective classification subroutine of https://arxiv.org/abs/2110.01052. Such procedures _are_ able to guarantee $\mathbb{P}(y \in C(x) \mid \|C(x)\| = 1) \geq 1-\alpha$.

(2)
The mathematical details of the paper are unclear, largely due to many typos. It is also overly formal in some sections, while being under-developed in critical parts.

The biggest issue is on page 7, where the score function is defined. We see $s(\bar x, y) = s(x_i^{min(t_{ans},T)},y)$. But $t_{ans}$ is unknown at $t=1$; so how can we expect to construct the prediction set at time $t=1$? That is: we can obviously define any score function we would like, as a function of the whole trajectory. The harder part, at least in this multi-turn setup, is inverting the test to get a sensible prediction set. Therefore, the form of the set should be written out, as it is for the baseline at the bottom of page 5.

There are also a number of typos in the math throughout. My general suggestion would be to cut down on the amount of notation and formalism as much as possible, to reduce to the minimal amount needed to convey the ideas.

Math typos:
* Bottom of page 5, definition of sets: $C^{\tau}$ does not seem to depend on $\tau$ except through $x^{\tau}$, which calls into question why it should have the second superscript.
* in the definition of SCP on page 5, the quantile function has been defined over measures, but it takes an empirical PDF as an argument earlier (these objects are of a different type)
* the conformal quantile isn’t the 1-alpha empirical quantile, it is the$ (1-\alpha)(1+1/n)$ empirical quantile due to the delta mass placed at infinity
* The correct notation for a set cardinality is not $\| \mathcal{C} \|$, but $|\mathcal{C}|$ (the former is normally reserved for a norm)

(3)
The paper could also use a more comprehensive literature review around methods for conformal prediction under feedback loops, for agents, and for decisions. There are many such papers.

_______

Other typos, errors, and minor suggestions:

$\|y - f(x)\|$ is not bounded. (Conformal scores do not generally need to be bounded or non-negative.)

“originally designed to handle external distribution shifts in dynamic environments” not really. It was designed to handle arbitrary distribution shifts of any kind.

Figure 1: right-side of the right-most panel, I think that there is an error. The algorithm shouldn’t yet terminate because both A and B cross the red line, so the prediction set should be {A, B}. Maybe the bar for A should be lower.

“minimal prediction sets” -> “minimal size prediction sets”

“We emphasize that Theorem 1 holds for arbitrary score function” typo

“The main challenge of the task is for the Expert system to ask
information-seeking questions to expand Kt until the the Expert system is sufficiently” typo in Appendix A.

On pg. 7, why does $x_i$ appear in the definition of $s(\bar x, y)$? This must be a typo, given the way $\bar x$ is defined on pg 5 in terms of $x^i$.

Not sure why this is called conformal reasoning. Name does not reflect the nature of the method, which can be applied to any trajectories, and does not really include reasoning as a subroutine.

### Questions
Main question: how is the set constructed when inverting the score on pg. 7?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents conformal reasoning, a method to reason about uncertainty in interactive environments. 

Conformal reasoning builds upon two key techniques: (1) adaptive conformal inference that performs online uncertainty set prediction in the presence of distribution shifts, and (2) refresh prediction that design a new score function.

Experiments on medical information seeking and embodied question answering show the proposed method is better than existing baselines.

### Strengths
- Well motivated problem of reasoning about uncertainty in interactive environments
- Good empirical performance
- Paper and method are well presented and easy to understand

### Weaknesses
 - Major weakness is limited novelty in the methods. The adaptive conformal inference is a straightforward application of the previous work, and the refresh prediction, as presented in the paper, is merely a new score function. So in this perspective the methodological contribution is quite limited.

- The ACI framework is a bit outdated now in the literature of online conformal prediction (with distribution shifts). In addition, several issues are known about ACI, including the requirement of parameter tuning in the algorithm. There are several recent algorithms that are theoretically more sound than ACI, such as:
  - Bastani, Osbert, Varun Gupta, Christopher Jung, Georgy Noarov, Ramya Ramalingam, and Aaron Roth. "Practical adversarial multivalid conformal prediction." Advances in Neural Information Processing Systems 35 (2022): 29362-29373.
  - Bhatnagar, Aadyot, Huan Wang, Caiming Xiong, and Yu Bai. "Improved online conformal prediction via strongly adaptive online learning." In International Conference on Machine Learning, pp. 2337-2363. PMLR, 2023.
  - Zhang, Zhiyu, David Bombara, and Heng Yang. "Discounted Adaptive Online Learning: Towards Better Regularization." In Forty-first International Conference on Machine Learning.
and the references therein.

- In the limitations section, the paper mentioned 

> convergence and stability of Conformal Reasoning is dependent on the choice of learning rate in adapting $\alpha_t$, requiring some hyperparameter tuning for the best performance

However, there are no ablation studies on the sensitivity of hyperparameter tuning. If the performance of the algorithm is very sensitive to the hyperparameters, then it is unclear if the proposed method is actually better than baselines in a statistical sense.

- It should be noted that the coverage guarantee is "asymptotic", and we do not when the coverage guarantee starts to hold, when using conformal prediction in the presence of distribution shifts.

### Questions
Ablation studies are needed to study the sensitivity of hyperparameters on the performance of the algorithm.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper considers the conformal reasoning problem in a multi-turn environment. The authors introduce the conformal reasoning problem and focus on the confidence set construction for this problem. They propose the adaptive conformal inference and refresh prediction as two main components. The efficacy of the proposed algorithm is verified via experimental results.

### Strengths
1.	The paper introduces the problem formulate and the algorithm clearly.
2.	The authors provide theoretical analysis of the proposed method in Theorem 1.

### Weaknesses
1.	The logic behind Section 4.1 is not clear. The authors claim that ``While much of the traditional conformal prediction literature assumes i.i.d. (or exchangeable) sampled data or a calibration set collected offline’’. However, the authors adopt the i.i.d. assumption in Theorem 1. If the non-stationary factors can be absorbed in $s_t$, then the convergence of $s_t$ to $s$ will be an unrealistic assumption in the setting considered by this work. Specifically, the assumption that the scenarios are i.i.d. does not guarantee that the *trajectories* generated by the agent's policy are also i.i.d. The agent's policy induces a temporal dependency, and thus the sequence of states and actions are not independent, even if the initial scenarios are drawn i.i.d. This discrepancy between the i.i.d. assumption on scenarios and the non-i.i.d. nature of the generated trajectories needs to be addressed more carefully.
2.	Theorem 1 is a result from the existing works where the setting is different from the proposed multi-turn task. It is encouraged to derive the analysis of the algorithm for the setting proposed in this work. The theorem relies on the assumption of online data, which is not the core setting of this paper. The multi-turn interaction introduces a sequential dependency that is not captured by the standard online setting. Applying the result directly without considering the implications of this sequential dependency is questionable. The analysis should explicitly account for the temporal structure of the multi-turn setting.
3.	Table 2 indicates that refresh prediction indeed sacrifices the specificity for the improvement of efficiency. It is beneficial to simulate and discuss the pareto frontier of the trade-off between these two factors. The current discussion lacks a rigorous analysis of this trade-off. A more detailed exploration of how the choice of refresh prediction impacts both specificity and efficiency is needed. It would be beneficial to see a visualization of the Pareto frontier to understand the practical implications of this trade-off.

### Questions
Same as the weakness

### Soundness
3

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
2

### Summary
This paper studies conformal prediction in a multi-turn setting, where an agent interacts with a user repeatedly, adjusting its predictions at each turn. The authors first identify two major limitations in traditional split conformal prediction (SCP): (1) SCP requires the prediction set at time $t$ to be the intersection of all previous sets, which can be overly restrictive, and (2) SCP calibrates a quantile using offline data specific to a certain policy and cutoff parameter, which may not generalize well out-of-sample due to distributional shifts. To address these challenges, the authors employ adaptive conformal prediction (ACP), which dynamically adjusts the quantile value as the environment changes and relaxes the restrictive assumptions in (1). The main contribution of this paper is the application of ACP in this multi-turn context, where it demonstrates better empirical performance over SCP in the authors' experiments.

### Strengths
- Overall, the paper is well-written. The concepts and split and adaptive conformal prediction are clearly explained.

- Conformal prediction in this multi-turn setting is an important problem that has application in many settings (especially those that involves LLM).
    
- Computational experiments demonstrate favorable performance of the proposed method.

### Weaknesses
 - **Motivation.** I am not sure if I fully understand why the traditional SCP requires the assumption that the current prediction set should belong to the intersection of previous ones. This seems to be a design choice that can be avoided. I suggest the authors providing more contexts regarding why this is necessary to better motivate the application of ACP. 

- **Experiments.** For an applied paper like this, I suggest the authors consider the following points to strengthen their empirical contributions.

  - **Coverage**. It's unclear to me how the coverage metric was calculated. Specifically, did you calculate the coverage for every time step or only do this at the final step?
  - **Domain shift.** One of the motivations for applying ACP is to deal with domain shifts. However, this is not tested in the computational experiments.
  - **RP.** It is unclear to me why RP helps to improve % answered, although the experiment results said so. It would be helpful if the authors could provide high-level intuition on the reason. 
  - **Efficiency.** It is unclear what the baselines are when the authors claim that conformal reasoning improves efficiency.

### Questions
By breaking the connection between prediction sets constructed at consecutive steps, ACP and RP enhance flexibility in generating prediction sets. However, this approach might compromise interpretability. It would be interesting to know if the authors have considered this trade-off and have any insights on it. Additionally, it could be valuable to explore potential approaches that lie between these two extremes.

### Soundness
3

### Presentation
3

### Contribution
2
