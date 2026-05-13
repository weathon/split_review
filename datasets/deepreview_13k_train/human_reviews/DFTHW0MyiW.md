# Beyond Worst-case Attacks: Robust RL with Adaptive Defense via Non-dominated Policies

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
In light of the burgeoning success of reinforcement learning (RL) in diverse real-world applications, considerable focus has been directed towards ensuring RL policies are robust to adversarial attacks during test time. Current approaches largely revolve around solving a minimax problem to prepare for potential worst-case scenarios. While effective against strong attacks, these methods often compromise performance in the absence of attacks or the presence of only weak attacks. To address this, we study policy robustness under the well-accepted state-adversarial attack model, extending our focus beyond only worst-case attacks. We first formalize this task at test time as a regret minimization problem and establish its intrinsic hardness in achieving sublinear regret when the baseline policy is from a general continuous policy class, $\Pi$. This finding prompts us to \textit{refine} the baseline policy class $\Pi$ prior to test time, aiming for efficient adaptation within a finite policy class $\Tilde{\Pi}$, which can resort to an adversarial bandit subroutine. In light of the importance of a small, finite $\Tilde{\Pi}$, we propose a novel training-time algorithm to iteratively discover \textit{non-dominated policies}, forming a near-optimal and minimal $\Tilde{\Pi}$, thereby ensuring both robustness and test-time efficiency. Empirical validation on the Mujoco corroborates the superiority of our approach in terms of natural and robust performance, as well as adaptability to various attack scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to address performance loss of robust reinforcement learning under weak or no adversarial attacks. To be more specific, they propose a method called PROTECTED, which first find a suitable finite set $\tilde\Pi$ of non-dominated policie during the training, and them adaptively select the policy at each time in a bandit-like way when testing. Empirical results are presented to backup the method.

### Strengths
This paper proposes an interesting approach for robust reinforcement learning by adaptively switch among non-dominated policies. The definition of "non-dominated policy" seems new. The algorithm to discover $\tilde{\Pi}$ is non-trivial and might be considered in future studies.

### Weaknesses
Overall, the presentation of the current paper can be improved. I find the settings in Section 4 confusing. Specifically, please consider the followings.
1. While the authors define a discount factor $\gamma$ in Section 3 (which seems to be used in an infinite horizon MDP), it is not used in the rest of the paper, where a MDP with finite horizon $H$ is considered. Can the result be extended to infinite horizon?
2. The authors propose the new regret in equation 4.1 that is based on the value function rather than reward. I feel it is not fully discussed why such a regret is appealing and how is it related with the commonly used reward-based regret.  
3. Also in equation 4.1, it seems that the regret depend on the attacker policy $\nu^t$ for each time $t$, where $\nu^t$ can be arbitrary. Is this regret well-defined without further confining $\nu^t$?
4. In the paragraph below equation 4.1, the term $\pi^tt\in[T]$ seems like typo. Should it be {$\pi_t: t\in [T]$} instead?

With above issues (especially 2 & 3), I do not fully understand the setting considered in this paper and am unable to evaluate its theoretical contribution accurately.

Besides, another weakness is pointed out by authors in Theorem 4.11 that suggests the size of $\tilde{\Pi}$ can be very large in some cases that is exponential in time horizon $H$.

### Questions
Based on Theorem 4.11, will the method be very likely to fail for infinite horizon MDP?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach to learning robust RL policies that improve robustness in the case of no attacks or weak attacks while still maintaining robustness against worst-case attacks. This approach entails adaptively picking policies at each time step from a fixed policy class in order to minimize a particular notion of regret. The fixed policy class is constructed during training with the aim of minimizing its size while minimizing regret-related optimality gaps compared to using the full policy class - notably, via discovery of non-dominated policies. The authors provide theoretical results on the hardness of the problem, optimality gaps between the fixed (refined) policy class and the full policy class, the regret of their algorithm, and the worst-case size of the refined policy class. They demonstrate empirical performance on four Mujoco environments with continuous action spaces (Hopper, Walker2d, Halfcheetah, and Ant) and show strictly improved performance against baselines across no-attack, non-worst-case-attack, and worst-case-attack scenarios.

### Strengths
Formulation: The authors formulate an interesting and important task of improving RL performance against non-worst-case state-adversarial attacks, in addition to no attacks and worst-case state-adversarial attacks. They theoretically establish its difficulty, opening up an interesting line of future research.

Theoretical results: While I did not check the proofs in detail, the authors seemingly present useful theoretical results regarding optimality gaps presented by the use of non-infinite policy classes, as well as the performance of their algorithm.

Empirical results: The empirical performance is strong, with comparison on several environments against several baselines and attack strategies.

### Weaknesses
Questions regarding definition of regret (Definition 4.2): It is unclear to me why the notion of regret does not allow $\pi \in \Pi$ to be picked adaptively at each time step in the same way that $\pi^t \in \Pi$ is picked adaptively. While this may not matter in the case of an infinite $\Pi$ given that the adaptive policy is likely contained within $\Pi$, once $\Pi$ is restricted to $\tilde{Pi}$ with finite cardinality, this may no longer be the case. In other words, I wonder whether the notion of regret used in this work may be too weak. Specifically, the standard notion of regret compares against the best *fixed* policy in hindsight, which may not be a suitable benchmark when considering adaptive policies. The restriction of the policy set $\Pi$ to a finite $\tilde{\Pi}$ further exacerbates this issue, as the optimal adaptive policy may no longer be representable within the reduced set, leading to a potentially significant gap between the regret achieved by the algorithm and the regret with respect to the true optimal adaptive policy. This raises concerns about the practical relevance of the theoretical results derived using this notion of regret.

Questions regarding experimental results: While the aim of the paper is stated as improving performance against no attacks/non-worst-case adversarial attacks while *maintaining* performance against worst-case adversarial results, the empirical results show the proposed method *exceeding* performance against worst-case adversarial attacks compared to baselines (in some cases, substantially - see e.g. Walker2d vs. PA-AD). This seems to contradict "no free lunch" intuitions. The authors should further explain why we are seeing this behavior in the experiments (potentially through the use of ablation studies), and whether there are any tradeoffs. The current results suggest that the proposed method is not only robust to a wider range of attacks but also superior in the worst-case scenario, which requires further investigation to understand the underlying mechanisms and potential limitations.

Minor points:
* Section 3: $H$ does not seem to be defined
* Section 3: Typo - "discounted factor" --> "discount factor"
* Proposition 4.3: How does the choice of $\alpha$ relate to the rest of the problem setup?

### Questions
* Why is the notion of regret that is defined not overly weak?
* Why are the experimental results not too good to be true? Are there any tradeoffs inherent in the method or results?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the test-time adaptation idea to adversarial robustness of RL models. More specifically at training time instead of identifying a single fixed policy, the learner maintains a set of policies, and then at the test time, it adapts to a particular trajectory and then chooses a good policy to react.

The authors have also considered how to attack such adaptation defense in a clear way. And various experiments have demonstrated the superiosity of the framework.

### Strengths
A novel and natural idea to introduce test-time adaptation to the RL. The authors have done a great job in carefully considering the security model, and discussed in detail how to attack such a test-time adaptation framework.

The authors have also discussed in details both theoretical and empirical evidence of the proposed framework, and it seems that this work can improve state of the art by a large margin.

Overall I found this paper a really nice to read.

### Weaknesses
The part about adaptive attacks seem somewhat weak -- namely, if the adversary has more knowledge about the defender, what can happen? The paper does not really seem to have clearly formulated what adaptivity really means in this case. However, I think this could be a future direction, given that this paper already has some novel ideas.

### Questions
No specific questions, my main concerns have been stated above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider the problem of synthesising policies for reinforcement learning (RL) that are both robust to adversarial perturbations and accurate to natural data. In particular, the authors propose an online adaptive framework that learns a finite set of policies that is used to ensure protection to adversarial attacks. The effectiveness of the approach of the authors is investigated on several standard RL benchmarks.

### Strengths
- Finding robust policies that are not overly conservative is an important problem and of interest for the ICLR community

- The approach proposed by the authors is promising and shows empirical improvements compared to state of the art.

- The authors provide bounds on the regret of the proposed algorithm

### Weaknesses
 - The paper is not well written. There are typos, some notation is not defined, and some parts are not very clear. Some examples:

a) in the definition of J(\pi,v) ,in the first expectation, it is missing where z is sampled from. 
b) \pi^tt is not defined (I guess you missed {}, but the same notation appears multiple times)
c)The update rule for \omega is not explained in the main text
d) in the abstract and intro the authors talk about "the importance of a finite and compact \mathcal{\PI}", but any finite set is also compact.
e) k in line 6 of Algorithm 2 not defined

- In order to talk about optimality, convergence guarantees, and scalability, in Theorem 4.10, it would be important that the authors report an upper bound of K. The lack of a concrete bound makes it difficult to assess the practical implications of the theoretical results. A discussion on how K scales with problem parameters, such as the size of the state and action spaces, or the complexity of the environment, is needed.

- I am confused by the result in Table 1. From the results it seems that the proposed approach obtains higher rewards against worst case perturbations compared to methods explicitly trained against worst case perturbations. Am I missed something? In any case, a discussion on the results and about their interpretation should be given

### Questions
See Weaknesses Section

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
