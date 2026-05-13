# Efficient Action Robust Reinforcement Learning with Probabilistic Policy Execution Uncertainty

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Robust reinforcement learning (RL) aims to find a policy that optimizes the worst-case performance in the face of uncertainties. In this paper, we focus on action robust RL with the probabilistic policy execution uncertainty, in which, instead of always carrying out the action specified by the policy, the agent will take the action specified by the policy with probability $1-\rho$ and an alternative adversarial action with probability $\rho$. We  establish the existence of an optimal policy on the action robust MDPs with probabilistic policy execution uncertainty and provide the action robust Bellman optimality equation for its solution. Furthermore, we develop Action Robust Reinforcement Learning with Certificates (ARRLC) algorithm that achieves minimax optimal regret and sample complexity. Furthermore, we conduct numerical experiments to validate our approach's robustness, demonstrating that ARRLC outperforms non-robust RL algorithms and converges faster than the robust TD algorithm in the presence of action perturbations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the action robust framework where a mixture policy between the maximizing agent and the minimizing adversary is effectively prescribed in the environment. Focusing on the finite horizon setting, the authors derive a Bellman recursion that solves this type of MDP and introduce ARRLC, a method that is shown to achieve minimax optimal regret. Experiments are conducted in two environments and ARRLC is compared to two baselines: (I) a non-robust algorithm called ORLC; and (ii) a robust TD algorithm. The numerical results show that ARRLC improves robustness upon ORLC while converging faster than robust TD.

### Strengths
This paper analyzes a setting that has essentially been addressed heuristically, to the best of my knowledge. The minimax regret and sample complexity result provide a theoretical justification for action robustness under probabilistic policy execution.

### Weaknesses
- The motivation for this work is unclear to me. On the one hand, action-robust MDPs have already been solved by Tessler et al. (2019) but on the other hand, this paper does not claim any improvement upon Tessler et al., nor does it numerically compare ARRLC to their solution... at least in the main body of the paper. In the appendix, there is a brief discussion on the difference between ARRLC and Tessler et al., but it is not comprehensive. Also, I do not understand why there is no convergence plot there.
- Pertaining to my previous concern, related work is described without assessing what each reference misses that this paper adds. This section should emphasize more on what previous work did and what is still missing that this study fulfills. This would not only give motivation to this work but also strengthen its significance. 
- Clarity: 
    - I see several grammar mistakes here and there: "A lot of robust RL methods"--> many, "the episodic RL" --> remove the; "which is deterministic" --> that is; "via the induction" --> by induction; "action ... and reward" --> actions ... and rewards; "the initial states... is deterministic... in different episode" --> are ... episodes

    - the algorithm is too far away after the text referring to it; 

    - Thm. 2: "then" should follow an "if" statement

    - The uncertainty set definition in Eq. (3) is confusing: it says $\tilde{\pi}$ is a mixture between $\pi$ and $\pi'$ without specifying $\pi'$, whereas the text after states that $\pi'$ should be an argmin. Once I understood what the authors meant, I think it would have been clearer to write: $\\Pi^{\\rho}(\\pi):= \\{ \\tilde{\\pi}: \\forall s, \\forall h, \\exists \\pi_{h}'(\\cdot|s) \\in\\Delta_{\\mathcal{A}} \\text{ such that } $ $\\tilde{\\pi_{h}}$ $(\\cdot|s)=$ $(1-\\rho)\\pi_{h}(\\cdot|s)+ \\rho \\pi_{h}'(\\cdot |s) \\},$ or even simpler, $\\Pi^{\\rho}(\\pi):=  (1-\\rho)\\pi + \\rho $ $(\\Delta_{\\mathcal{A}})^{|\\mathcal{S}|\\times H}$

- It is not clear to me how this work improves upon Tessler et al.. It does give regret bounds and sample complexity, but how is the algorithmic approach essentially different?

### Questions
- Why did the authors not compare ARRLC to the approaches of Pinto et al. (2017) or Tessler et al. (2019) in the experiments section, but chose a comparison to a non-robust approach ORLC instead? 
- I simply remark that $\\Pi^{\\rho}\\subset\\Pi^{D, \\rho}$, is that correct? Also, what does the relationship between those two types of uncertainty sets bring to the analysis? 
- As far as I remember, Tessler et al. (2019) proved the existence of an optimal policy for the action robust setting under probabilistic execution. Although their proof does not rely on Bellman recursion but a Markov game formulation, they show equivalence between this setting and the robust MDP setting, itself being solvable through Bellman recursion [1]. Could the authors please clarify?

[1] Iyengar, Garud N. "Robust dynamic programming." Mathematics of Operations Research 30.2 (2005): 257-280.

### Soundness
2 fair

### Presentation
1 poor

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
This paper explores the realm of action-robust reinforcement learning, wherein the policy prescribes an action with a high probability of certainty (1 - $\rho$) while considering an alternative adversarial action with a probability of $\rho$. The authors introduce an action-robust Bellman optimality equation and introduce a novel algorithm named Action Robust Reinforcement Learning with Certificate (ARRLC). The authors further establish the minimax optimal regret and illustrate the superior robust performance of ARRLC when compared to both non-robust algorithms and robust TD methods.

### Strengths
* This paper is easy to follow.
* The paper demonstrates technical rigor, with most claims substantiated adequately, and its theoretical guarantee appears to be novel.
* Several toy examples are included to illustrate experimental findings.

### Weaknesses
* Given the results in [Tessler, 2019], the first contribution listed on page 2 is not very original (no big difference between episodic setting and infinite discounted horizon setting). 
* All regret analyses in this paper highly depend on the choice of uncertainty sets and techniques in this paper cannot be extended easily to other uncertainty sets (e.g., noise action uncertainty sets in [Tessler, 2019]).
* It appears that the policy execution uncertainty set may not be suitable for addressing large-scale problems, as it necessitates computing the minimum over the action space. While this paper concentrates on a tabular environment, it would be more prudent to opt for a scalable uncertainty set, e.g., [Zhou et al., 2023, Natural Actor Critic for Robust Reinforcement Learning with Function Approximation].
* One important piece of literature on robust MDP is missing in the paper [Iyengar'05, Robust dynamic programming].

### Questions
Please refer to the ``weakness'' section for further information.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work provides a learning procedure for the action robust RL problem. This work also gives complementing experiment results.

### Strengths
Extension of ORLC algorithm (Dann et al, 2019) to solve action robust RL problem. Extensive experiments have been made to showcase action robustness of ARRLC algorithm. The score reflects the points made in Weaknesses.

### Weaknesses
The weaknesses are concerned more likely due to incremental contributions in this work, but I'd rather see this work as a published work rather than a blogpost. I explain this in a few points below.

-  Theorem 1 results in this work are already shown in Proposition 1 of (Tessler et al, 2019). Moreover, even though the latter work does not explicitly define "action robust Bellman equation" and the corresponding optimality equations, they can be inferred from (Eq.(11), Tessler et al, 2019). Although an independent analysis in this work is made for finite-horizon setting whereas (Tessler et al, 2019) is for infinite horizon, the proof ideas share similar characteristics due to the structure of the uncertainty set itself (helping commutability of the expectation and the minimization operations). Thus Theorem 1 proof largely following the proofs in (Iyengar, 2005) for the finite-horizon getting insights from Proposition 1 of (Tessler et al, 2019).

- With the separable form of action robust Bellman equation ($V^*(.) = (1-\rho) \max_{a}Q^*(.,a) + \rho \min_{a}Q^*(.,a)$), ARRLC is an extension of ORLC (Dann et al, 2019) with less technical challenges. The analysis is made finer by replacing $Var(\overline{V})$ with $Var((\overline{V}+\underline{V})/2)$ which is straightforward from Eq.31 due to monotonicity and induction.

I am open to discussions with the authors and reviewers to increase/maintain (already reflects the positive impact) my score. All the best for future decisions!

### Questions
-n/a-

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
