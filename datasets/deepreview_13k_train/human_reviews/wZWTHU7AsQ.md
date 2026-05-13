# Game-Theoretic Robust Reinforcement Learning Handles Temporally-Coupled Perturbations

- Decision: Accept
- Scores: 5, 6, 5

## Abstract
Deploying reinforcement learning (RL) systems requires robustness to uncertainty and model misspecification, yet prior robust RL methods typically only study noise introduced independently across time. However, practical sources of uncertainty are usually coupled across time.
We formally introduce temporally-coupled perturbations, presenting a novel challenge for existing robust RL methods. To tackle this challenge, we propose GRAD, a novel game-theoretic approach that treats the temporally-coupled robust RL problem as a partially-observable two-player zero-sum game. By finding an approximate equilibrium within this game, GRAD optimizes for general robustness against temporally-coupled perturbations. Experiments on continuous control tasks demonstrate that, compared with prior methods, our approach achieves a higher degree of robustness to various types of attacks on different attack domains, both in settings with temporally-coupled perturbations and decoupled perturbations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The classic robust RL focuses on worst-case scenarios, which may result in an overly conservative policy. Instead, this paper introduces temporally-coupled perturbations. Additionally, this paper proposed an adversarial training approach named the game-theoretic response approach for adversarial defense. Finally, the authors show the robust performance of the proposed methods in several MuJoCo tasks compared with several baselines.

### Strengths
* This paper is easy to follow.
* This paper does thorough experiments for state attacks and action attacks and compares the proposed method with several baselines. 
* The temporally-coupled adversarial perturbation seems new.

### Weaknesses
 * Although the temporally-coupled adversarial perturbation seems new, it is quite limited. Definition 3.2 only considers the temporally-coupled perturbation from the last time step. Even if the authors don't consider the general partially observable MDP, they should consider a more general case, e.g., m-order MDP [Efroni et al. 2022, Provable Reinforcement Learning with a short-term memory]. Specifically, the current formulation only considers a first-order Markovian dependency, neglecting the potential for longer-range temporal dependencies in adversarial attacks. This is a significant limitation as adversaries could exploit vulnerabilities arising from multi-step dependencies. 
* The zero-sum game-based approach is not new for robust training in RL, e.g., [Tessler et al., 2019]. The paper does not adequately distinguish its approach from existing game-theoretic methods, particularly in terms of the specific game formulation and the algorithm used to find the equilibrium. The novelty of the proposed approach is not clearly established compared to existing literature.
* This paper misses one classic setting of robust MDP (i.e., transition adversaries) [e.g., Iyengar'05, Robust Dynamic Programming] as well as related baselines [e.g., Zhou et al. 2023, Natural Actor-Critic for Robust Reinforcement Learning with Function Approximation]. The absence of experiments and comparisons with methods that consider transition adversaries limits the scope of the paper and its applicability to a broader range of robust RL problems. The paper should have included a discussion on how the proposed method would handle uncertainties in the transition dynamics.
* Figure 1 doesn't make sense to me. The robust baseline considers the worst-case scenario, which should be more stable for different kinds of attacks compared with the less conservative model that is proposed in this work. The figure suggests that the proposed method is more robust than a worst-case robust baseline, which is counter-intuitive. The paper should provide a more detailed explanation of why the baseline is not robust to the temporally-coupled adversaries.

### Questions
Please refer to the "weakness" section for further information.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces a novel-framework of temporally-coupled robust RL problem that is closer to the real-world setting. This work proposes GRAD, a game-theoretic approach to provide robust policies played against an adversary which attacks states and actions fitting in the temporally-coupled robust RL problem setting. This work also gives extensive complementing experiment results.

### Strengths
I think this work really pushes the robust RL community research efforts further by answering:

> can we design robust RL algorithms for realistic nature attacks?

The main contribution of game-theoretic algorithm with temporal-based nature attacks (robust RL problem) is a really nice idea worthy for publication. But the score reflects my weakness section.

### Weaknesses
I have only a few weakness for this work as follows:

> The current framework considers robustness against state and action uncertainty. More closer work [1] and thereafter are not included. Model uncertainty is justified in the framework mentioning the evolution of the environment depends on the perturbed actions. Model uncertainty in robust RL is defined in more generality [2-10]. So it will be better to include more detailed Related Works including [2-10] and more relevant works in the revision. I agree this work includes experiments with model uncertainty, but the baselines are also only action robust algorithms. I'd rather see more extensive writing and experiments for model-uncertainty OR the current work just focusing on state-action uncertainty is a big step forwards in itself. I've also stopped at '10' since you get the idea of inadequate related work discussion.

> GRAD shares similar idea of RARL algorithm (Pinto et al., 2017), that is, zero-sum structure to get the robust policy against the nature adversary. More details than below must be added to point out key differences (like state-action uncertainty inbuilt) and due references need to be given.
` Pinto et al. (Pinto et al., 2017) model the competition between the agent and the attacker as a zero-sum two-player game, and train the agent under a learned attacker to tolerate both environment shifts and adversarial disturbances `

### Questions
-n/a-

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenge of deploying reinforcement learning (RL) systems that can withstand uncertainties, particularly those that are temporally coupled. Recognizing that conventional robust RL methods may falter against such temporally-linked perturbations, the authors introduce a game-theoretic approach called GRAD (Game-theoretic Response approach for Adversarial Defense). GRAD conceptualizes the robust RL problem as a partially observable two-player zero-sum game and uses Policy Space Response Oracles (PSRO) to achieve adaptive robustness against evolving adversarial strategies. The study's experiments confirm GRAD's performance in ensuring RL robustness against both temporally coupled and standard adversarial perturbations.

### Strengths
The authors formulate the robust RL objective as a zero-sum games and demonstrating the efficacy of game-theoretic RL in tackling this objective.

### Weaknesses
1. This paper does not have a clear mathematical representation of the problem it intends to address. 

2. The article claims its primary contribution lies in using zero-sum games to formulate the robust RL problem. However, employing zero-sum games to account for uncertainties, whether in single-agent or multi-agent RL, is well-established, as seen in works like Robust Adversarial Reinforcement Learning, Robust Reinforcement Learning as a Stackelberg Game via Adaptively-Regularized Adversarial Training, and Robust Multi-Agent Reinforcement Learning with State Uncertainty. Given this widespread application, the paper's stated novelty becomes questionable.

3. In terms of algorithmic design, the proposed method is largely an application of the Policy-Space Response Oracles (PSRO). The novelty seems limited, and it's unclear how PSRO uniquely addresses the issue of temporally-coupled perturbations.

4. Considering that the PSRO algorithm converges to an NE in two-player, zero-sum games and has seen recent extensions to other equilibria types [1, 2], the paper's proposed method, essentially a reiteration of PSRO, makes the convergence proof for GRAD appear somewhat lackluster in its contribution.

5. This paper has ample room for improvement in writing, problem formulation, and the method itself. For instance, by simply using the triangle inequality, we could give the range of $\bar{\epsilon}$ that break the temporally-coupled property, rather than merely stating, "By setting \epsilon ̄ to a large value, it converges to the non-coupled attack scenario." Additionally, the motivation behind temporally-coupled perturbations lacks clarity and persuasiveness, leaving me unconvinced of its pressing relevance.

### Questions
Please see the Weaknesses, I will decide the final rating after the rebuttal.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
