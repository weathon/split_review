# Causal Bayesian Optimization with Unknown Causal Graphs

- Decision: Reject
- Avg Score: 6.50
- Scores: 5, 8, 3, 10

## Abstract
Causal Bayesian Optimization (CBO) is a methodology designed to optimize an outcome variable by leveraging known causal relationships through targeted interventions. Traditional CBO methods require a fully and accurately specified causal graph, which is a limitation in many real-world scenarios where such graphs are unknown. To address this, we propose a new method for the CBO framework that operates without prior knowledge of the causal graph. We demonstrate through theoretical analysis and empirical validation that focusing on the direct causal parents of the target variable is sufficient for optimization. Our method learns a Bayesian posterior over the direct parents of the target variable.  This allows us to optimize the outcome variable while simultaneously learning the causal structure. Our contributions include a derivation of a closed-form posterior distribution for the linear case. In the nonlinear case, we present a Gaussian Process (GP) approximation that still enables CBO in cases where the posterior is not tractable. The proposed method performs competitively with existing benchmarks and scales well to larger graphs, making it a practical tool for real-world applications where causal information is incomplete.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the problem of causal Bayesian optimization when the causal graph is unknown. Under certain assumptions, the authors propose an algorithm for linear and non-linear structural causal models (SCMs). The approach simultaneously learns the Bayesian posterior over the parent variables (where the best action lies) and optimizes the target variable. The effectiveness of the approach is demonstrated through various experiments.

### Strengths
1- The paper addresses an important and challenging problem in causal Bayesian optimization, particularly under the realistic scenario where the causal graph is unknown.

### Weaknesses
1- It would be beneficial to review relevant work in the causal bandits literature, where the setting is similar, and some studies address scenarios without a known causal graph.

2- Assumption 4.3 is quite restrictive, limiting the approach’s applicability to graphs without confounders between $Y$ and its ancestors. This assumption essentially requires that all common causes of $Y$ and its ancestors are observed, which is a strong condition not often met in real-world scenarios. The absence of unobserved confounders significantly simplifies the problem, and the paper should more clearly acknowledge this limitation.



### Questions
1- I didn’t understand Equation 2—why is it conditioned on $C$? Is not $E[Y | \xi, G]$ the target?


2- As the authors mentioned, previous work has shown that the optimal action is an intervention on parent sets, which is why the focus is on parents in similar settings. My question is, how does your approach perform when there is a confounder between $Y$ and its ancestors? Specifically, how does it handle cases where Assumption 4.3 does not hold?

Typos:

Line 167: $P(Y \vert X_s = \nu, C)$

Line 215: “For the algorithm” is repeated.

Line 251: Missing a period at the end of the sentence.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors study causal Bayesian optimization (CBO) with an initially completely unknown causal graph. They apply sufficient graphical assumptions for hard interventions (Gultchin et al., 2023) across the parents (Lee and Bareinboim, 2018) of the reward variable $Y$ to be optimal. 

To ensure tractability, the support over plausible parents of $Y$ is restricted by the observational dataset using bootstrapped doubly robust causal feature selection. The average causal effect (ACE) of interventions over the plausible parents on $Y$ is modelled by a Gaussian process over intervened datasets. 

The authors' approach applies to models where $Y = f ( \mathrm P \mathrm a_Y ) + \epsilon_Y$ is subject to additive, Gaussian noise $\epsilon_Y$. For linear $Y$ with Gaussian noise, a closed form solution for the Bayesian update rule over the linear coefficients $\theta_{\mathrm{Pa}_Y}$ (and thus the ACE) is given. An approximation using the kernel trick is applied for general $f(\cdot)$.

### Strengths
The paper is written very well and the authors' contributions, underlying assumptions and limitations are made clear. The performance of the authors' method was evaluated with synthetic datasets and real(?) gene expression datasets. The authors' contributions are high impact and possible theoretical extensions are also clear.

### Weaknesses
I do not have many weaknesses to discuss.

Presumably the authors' approach becomes suboptimal when the ground truth parents of $Y$ are not ``discovered'' in the feature selection stage. Was this kind of error rate (a type 2 error rate) measured by the authors at any point? Figure 4 appears to show an error rate of variables falsely included as parents of $Y$ but not those falsely excluded. A breakdown of the underperformance of CBO-U due to type 1 and type 2 errors would give more detailed insight into the limitations of the authors' approach. Specifically, it would be useful to understand how often the algorithm fails to identify a true parent, and the impact of this failure on the final optimization performance. This is particularly important given the reliance on the initial feature selection step.

Minor comments:

(Section 4) The notation $X_j^c$ for the complement of $X_j$ is used when defining the doubly robust estimator, but the notation is not introduced anywhere in the main text. 

(Section 5) The authors appear to be referencing causal expected optimization (CEO) without having defined this in the main text. 

(Section 5) In the experiments, were the authors referring to the DREAM5 challenge: i.e., a real-world dataset or earlier synthetic datasets such as DREAM4?

### Questions
(Selecting the plausible parents) Have the authors considered an approach to combine the observational and interventional datasets during feature selection? If $X_j$ is not a parent of $Y$ then $\chi_j$ will equal zero across *all* datasets, interventional and observational, due to Assumption 4.3. Would performing the test over pooled data yield better type 1 and 2 error rates? 

(Relaxed assumptions) What approaches might one take for a CBO-U extension in cases in which the optimal interventions are soft interventions? Are there similar sufficient conditions under which the optimal interventions are hard interventions but where Assumption 4.3 is violated. The authors' future work section is somewhat terse and it may help to discuss open questions more thoroughly.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel Causal Bayesian Optimization (CBO) method that operates without a fully known causal graph, focusing on learning only the direct causal parents of a target variable. They propose posterior update rules for the linear case with additive Gaussian noise. For the nonlinear case, they suggest using a Gaussian Process (GP) surrogate model. The authors empirically demonstrate that the proposed method achieves the same optimal target value on synthetic and semi-synthetic causal graphs as methods with fully specified causal graphs.

### Strengths
The main contributions of the paper include deriving a closed-form posterior update rule for additive Structural Causal Models (SCMs) with Gaussian noise and formalizing Causal Bayesian Optimization (CBO) for scenarios with unknown causal graphs. For the nonlinear case, the authors propose using Gaussian Processes (GPs). Additionally, they present a scalable solution for handling larger graphs by deriving an initial prior probability for nodes being direct parents of the outcome using observational data.

### Weaknesses
The paper has some novelty in the formalism of causal Bayesian optimization with an unknown causal graph. However, I am not entirely convinced of the novelty of the theoretical results in Section 4.1. My primary concern is that there is already existing work on Bayesian causal discovery for linear SCMs with additive Gaussian noise. Since identifying the parents  is a simpler problem, it seems possible that existing approaches could be directly applied for Bayesian optimization purposes. I am referring to the following papers:

https://proceedings.neurips.cc/paper_files/paper/2022/file/675e371eeeea99551ce47797ed6ed33e-Paper-Conference.pdf

https://arxiv.org/pdf/2307.13917

https://proceedings.neurips.cc/paper_files/paper/2021/file/39799c18791e8d7eb29704fc5bc04ac8-Paper.pdf

I would appreciate it if the authors could clarify what makes the results presented in Section 4.1 non-trivial, especially in light of the existing literature. I can consider increasing the score in this case. Additionally, I have concerns regarding some of the assumptions made in the paper, which I have mentioned in the questions section.

### Questions
I have few questions for the Authors:

* Can the authors explain why Assumption 4.1 is needed for the proposed solution to work?

* The paper by Lee & Bareinboim (2018), which the authors cite, also provides a complete characterization of possible optimal arms for arbitrary causal graphs with confounders in Proposition 4 and Theorem 6. Can the authors comment on why this result cannot be used to relax Assumption 4.3?

* Additionally, regarding the literature on causal discovery for linear SCMs with additive Gaussian noise, how do the results in the paper compare with them, and what is the novelty of the results in Section 4.1?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper is a significant contribution to the CBO literate:
- it makes the very practical observation that we do not require the complete graph to do "good" CBO, as previous methods have tackled, but only an idea of the parents of the target variable
- as a consequence, the method can handle bigger larger graphs which is a substantial contribution, see - [ ] 466 which has the strongest statements

### Strengths
- authors have a strong grasp of both causal literature, as well as CBO literature which helps exposition of their whole idea
- execution is done well
-- introduction is informative
-- lit review and preliminaries are weighted well
-- methods are clearly introduced and explained
-- experiments are well chosen and support the results well

most importantly, limitations are transparently stated which is of huge importance in the causal inference literature, and science in general

e.g. line 190 appreciate clarity

### Weaknesses
I found it hard to find weaknesses in this paper, the idea is clear, the execution is excellent, and the presentation and writing is very effective. It makes a very valid point that previous literature had somewhat overlooked.

Regardless, one strong initial confusion was how this paper is different to the previous literature. 

The key sentence is only made in 056 which for the 'fast reader' could easily be missed. 

E.g. the abstract does mention the idea, but it's ambiguous: "We demonstrate through theoretical analysis and empirical validation that focusing on the direct causal parents of the target variable is sufficient for optimization." There are other methods that focus on the parental set, and so the contribution of this paper is not immediately clear. 

This statement would be possibly better phrased as "We demonstrate through theoretical analysis and empirical validation that focusing ONLY/PRIMARILY/EXCLUSIVELY etc on the direct causal parents of the target variable is sufficient for optimization."

Otherwise, see questions.

### Questions
- [ ] Figure 3: what’s red line (apologies if I missed the definition)
- [ ] Fig 6 why are "CBO" and "random" straight lines in the right hand side plots (trials as x-axis)

typos:
- [ ] 215/216 repetition 
- [ ] Figure 4 typo ‘an interventions’
- [ ] 421 typo
- [ ] 460 typo

### Soundness
4

### Presentation
4

### Contribution
4
