# Stochastic Matching Bandits under Preference Feedback

- Decision: Reject
- Scores: 5, 5, 6, 3, 5

## Abstract
In this study, we consider multi-class multi-server asymmetric queueing systems consisting of $N$ queues on one side and $K$ servers on the other side, where jobs randomly arrive in queues at each time. The service rate of each job-server assignment is unknown and modeled by a feature-based Multi-nomial Logit (MNL) function. At each time, a scheduler assigns jobs to servers, and each server stochastically serves at most one job based on its preferences over the assigned jobs. The primary goal of the algorithm is to stabilize the queues in the system while learning the service rates of servers. To achieve this goal, we propose algorithms based on UCB and Thompson Sampling, which achieve system stability with an average queue length bound of $\Ocal(\min\{N,K\}/\epsilon)$ for a large time horizon $T$, where $\epsilon$ is a traffic slackness of the system. Furthermore, the algorithms achieve sublinear regret bounds of $\tilde{\Ocal}(\min\{\sqrt{T}Q_{\max},T^{3/4}\})$, where $Q_{\max}$ represents the maximum queue length over agents and times. 
 Lastly, we provide experimental results to demonstrate the performance of our algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers stochastic matching bandit that allows stochastic choice behaviors of arms and inclusion of outside options. Multinomial Logit (MNL) choice model with feature information is used to describe the unknown preferences of arms. The new bandit model has applications in ride-hailing services, online job markets and online labor markets. The goal is to maximize the likelihood of successful matches and learn the unknown arm preferences. The authors analyze the regret bound of an elimination-based algorithm. They show the regret bound achieves $\tilde{O}(K\sqrt{rKT})$ regret where r is the rank of feature space. The algorithm is shown to outperform two existing deterministic matching bandit algorithms via simulation experiments.

### Strengths
This paper fills an important gap in existing matching bandit literature that considers arm behavior as deterministic. It is indeed important in real world applications to not only focus on maximizing the likelihood of successful matches, but also learning arm preferences.
The paper develops an elimination-based algorithm to solve the stochastic matching bandit problem that can be divided into three phases, estimation, elimination and exploration. Detailed theory and proof is provided to prove the algorithm regret upper bound. The authors also discussed the computational complexity by optimization using $\alpha$-approximation oracle.

### Weaknesses
The important and practically relevant aspect of the setting is stochastic matching developed using MNL choice model with feature information. The powerfulness of the model is not demonstrated well. The experiment section assumes uniformly distributed features and does not cover the learning of arm performances. Theorem 1 is the key result for the paper. While detailed analysis is provided, it would be good to explain the key insights of the proof and clearly demonstrate how the three steps of the main stage contributes to the regret and which dominates the regret. Also, it will be good to have a full comparison of regret bounds and computational hardness with existing methods.

### Questions
• Can you further explain the $\pi$ in exploration step and how it affects the regret analyis?   
• Tight regret bound is claimed for Thm 1. How does the regret bound compare to other matching bandit problem and is there a lower bound case?   
• Outside option is considered in the paper. How about collision such that two arm choose the same agent?   
• Please, see weaknesses and further elaborate on those points.

----------------------------After Rebuttal-----------------------------------
Thank you for the response. This helps me better understand the paper. G/D design seems to be the key - it would be good to revise Thm1 sketch proof. The current version is unnecessarily long.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study introduces a stochastic matching bandit framework using the Multinomial Logit model with features. Agents are matched to arms, which stochastically choose agents or reject all. The goal is to minimize regret by maximizing successful matches.

### Strengths
1. The proposed model introduces an innovative framework for matching bandits, featuring novel stochastic behaviour of the arm that enhances its functionality in real-world application.
2. In addition to SMB (Algorithm 1), the integration of Algorithm 3 significantly addresses and mitigates computational challenges.

### Weaknesses
1. While the dynamic stochastic model presented is interesting, the objective in the given setting appears somewhat unreasonable. Specifically, in Section 3, the objective is to maximize the expected number of successful matches without regard to specific assignment matches, only focusing on whether there are no empty slots for each arm. This raises questions about the role of the MNL model introduced. It seems incongruent to assume the model includes preference feedback (in Line 172) when the objective disregards the resulting preferences, focusing solely on the absence/presence of assignment. The core issue is that the MNL model learns preferences between agents and arms, but the objective function only cares about whether an arm has *any* successful match, not *which* agents are matched. This disconnect undermines the motivation for using the MNL model in the first place, as the learned preferences are not directly used in the optimization target.

2. The significance of Theorem 1 and Theorem 3 is not clear. Notably, the dependency of $ K \sqrt{K} $ in the regret bounds is unusual within the bandit literature, where a dependency of $ \sqrt{K} $ is typically observed in most other bandit papers. Is  $ K \sqrt{K} $  unavoidable in this setting? Providing a tightness analysis for Theorem 1 and Theorem 3 would be valuable in elucidating the significance of these theoretical results. The $K\sqrt{K}$ dependency suggests a potential inefficiency in the algorithm's exploration strategy, or that the problem's inherent complexity is not fully captured by the standard $\sqrt{K}$ scaling. A more detailed analysis is needed to understand if this bound is fundamental or an artifact of the proof technique.

3. The use of Baseline algorithms (i.e., ETC-GS and UCB-GS) is not suitable, as they are designed for a very different objective. Unfortunately, I don't have a good recommendation for the baseline.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies a new kind of matching bandit model, in which several agents are assigned to an arm, and the arm accepts one of them (or none of them) following an MNL setting. The goal is to maximize the matching probability. Under general linear structure, the authors propose an elimination-based algorithm called SMB, which achieves a regret upper bound of $\tilde{O}(\sqrt{dK^3T}/\kappa )$. They also propose an approximate-oracle version algorithm to achieve a similar approximate regret, and use experiments to demonstrate the effectiveness of their algorithm.

### Strengths
The new model setting is well-motivated.

I read some of the proofs and they seem to be correct.

The writting is easy to understand (though there are some typos).

### Weaknesses
I think the primary contribution of this paper is proposing the new model setting. The contributions from the perspective of theoretical analysis seem limited, as they all follow the existing frameworks. 

The SMB algorithm is not efficient, and its approximate version needs to use $\alpha$-oracle, but can only obtain an sublinear $\alpha^2$-approxiamte regret upper bound.

Since the target and dynamics of the model is totally different with UCB-GS and ETC-GS, it is not really fair to compare with them.


Some minor typos:

- In Assumption 2, should it be $\inf_{||\theta||_2 \le 1}$?
- In Eq. (4), it should be $R^{LCB}$ but not $R^{LBC}$.

### Questions
Here are some of my quiestions.

1. It seems that there is a monotone property in your reward function, i.e., if we increase one arm's $x_n^T \theta_k$, the reward is increasing. Because of this, you can estimate the UCB and LCB by Eq. (2). So I am wondering what if we do not have such a monotone property? For example, in the case that each agent has its own score, and we want to maximize the average score (your case can be seen as the special one that the score is always 1). What can we do in this case? Also, are there any possible efficient approximate oracles in this case?

2. For the regret upper bound, we believe the factor of $T$ and $r$ are tight, then what about the other two factors? For the $K$ term, do we have a lower bound? Also, for the $\kappa$ term, there is a result that removes it in general linear model [1], could we use similar analysis to reduce it?

3. What's the exact value of $\alpha$ in your approximate version of the algorithm?


[1] Lee J, Yun S Y, Jun K S. A Unified Confidence Sequence for Generalized Linear Models, with Applications to Bandits[J]. arXiv preprint arXiv:2407.13977, 2024.



========After rebuttal=========

Thanks for the reply. I do not have further questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The aim of this paper is to study a stochastic matching problem with multinomial logit choices in selecting agents.

The authors consider a model that has N agents with K arms. Each agent n as a d-dimensional feature vector, while each arm k has a d-dimensional latent vector \theta_k.  In each period, the algorithm assign some agents to an arm.  Each arm will probabilistically select an agent (including a null agent which implies no selection of any assigned agent) which follows the Multi-nomial Logit (MNL) model.  The goal is to maximize the expected number of successful matching.

The authors extend the previous works in two fronts:
   - allows select the null-agent (or not selecting any of the assigned agent);
   - instead of having a "deterministic preference" of accepting agents, the authors consider a "probabilistic model" using the multinomial logit function.

The authors proposed an elimination-based algorithm that wherein the regret bound is O(ln(T)) (plus other terms).  Also, there is a computational issues in their proposed elimination-based algorithm,  To address this, the authors an approximation (or \alpha-approximation oracle).

Finally, the authors carried out simulation to illustrate the merits of their works.

### Strengths
The strength in this paper, as far as I am concern, is in the writing.

The authors did a good job in presenting the previous and related works, as well as in presenting the mathematical models.

The proposed algorithm (e.g., elimination-based) as well as the alpha-approximation algorithm, as far as I am concerned, are really simple extension of some of the previous algorithms.

The technical proof looks correct, but then again, if one is familiar about MAB or matching MAB, many of the previous works also followed the same line/style in proving the regret bounds.

### Weaknesses
The major concern I have about this paper is about its novelty.

First of all, extending from previous matching MAB problem by allowing a null-agent (or arm can reject any of the assigned agent) is really a trivial extension.  In fact, many previous papers can  easily incorporate this case in their model.

Secondly, allowing arms to select an agent based on multinomial logit function for me is in fact a restriction.  Because in real-life, the preference probability can in fact be more "general" then the multinomial logit representation.  One may have a hard time fitting an arbitrary probability distribution using the multinomial logit function.  

Thirdly, the elimination-based algorithm is very similar to the previous work by Lattimore and Szepesvari (with minor alteration due to the mapping with the problem).  To resolve the computational issue using an approximation algorithm is also a very common technique, as stated by the authors, from Kakade et at in 2007. In fact, this form of alpha-approximation has been heavily used in many disciplines, from theoretical computer science to machine learning.

Fourthly, the explanation of the algorithm has some issues. The authors discussed about using SVD to compute X=U\sumV^T, but are they defined ?  It seems the authors just use the previous SVD approach to extract information.

Lastly, why just compare with ETC-GS and  UCB-GS?  For example, I want to see how the algorithm will compare when the preference is "deterministic" (as used by many previous matching MAB algorithms), and to see how the variation from the deterministic preference to stochastic preference can impact the complexity and accuracy of the proposed algorithms.

### Questions
- Explain and define X=U \sum V^T.  How you get these from the inputs to your algorithm.

- Why multinomial logit is not a restriction?  Since one needs to find the right values of \theta so as to match to any probabilitic distribution.  

- Can your algorithm handles time-varying preference in selecting agents?

- Authors need to do a more comprehensive benchmarking and evaluation by comparing with other MAB-matching works.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new bandit framework of stochastic matching model, where agents on one side are assigned to arms on the other side, and each arm stochastically accepts an agent among the assigned pool of agents based on its unknown preference, allowing a possible outside option of not accepting any.

### Strengths
- This paper proposes a new bandit framework of matching, where the agents can be stochastically rejected from the arm side. This framework has some reasonable real-world applications.
- It discusses the computation issue of the algorithm, which often becomes one of the main aspects of combinatorial badits. It shows a regret bound when using an $\alpha$-approximation oracle.

### Weaknesses
 - There is no lower bound for this framework, which weakens the contribution since we can not assess the upper bound quantitatively. Won't Merlis et al. (2020) help analyze the lower bound of MNL? 
- Although it proposes an algorithm with an approximation oracle, it is not shown in the experiment. It would be even better if there were numerical experiments showing that using an $\alpha$-approximation oracle improves calculation execution time.
- The parameter $\kappa$ is presented as a global parameter controlling rejection probability, which seems overly simplistic. It is unclear why a more granular approach, such as defining $\kappa_{ij}$ for each agent-arm pair, is not considered. This could potentially capture more realistic scenarios where rejection probabilities vary across agents and arms.
- The paper does not adequately address the computational complexity of the proposed algorithm, especially in relation to the number of agents and arms. While an approximation oracle is mentioned, there's no clear discussion of how this scales with problem size, and whether the approximation introduces a significant trade-off in solution quality.

### Questions
- On page 7, there is a proof sketch for Theorem 1. Is this necessary? If so, could you briefly explain which part of the proof is novel?
- $\kappa$ seems to be the only parameter related to the rejection of the arm side. Thinking straightforwardly, can't we directly define like $(\kappa_{ij})\_{i = 1, ..., n, j = 1, ..., k}$, where $\kappa_{ij}$ is the probability that agent $i$ will be rejected from arm $j$? 
- S. Wang (ICML2018) should be cited since this work also works on combinatorial bandit with semi-bandit feedback. Shouldn't their algorithm, CTS, at least be compared in the experiment section?
- I would like to know if there is a proper real-world dataset for the experiment. This study would be even more interesting to have a numerical experiment with real-world data since it seems to be more focused on real-world applications.

[Reference]
- Siwei Wang and Wei Chen. Thompson Sampling for Combinatorial Semi-Bandits. ICML, 2018.

### Soundness
2

### Presentation
3

### Contribution
2
