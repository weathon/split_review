# Learning Constrained Markov Decision Processes With Non-stationary Rewards and Constraints

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
In \emph{constrained Markov decision processes} (CMDPs) with \emph{adversarial} rewards and constraints, a well-known impossibility result prevents any algorithm from attaining both sublinear regret and sublinear constraint violation, when competing against a best-in-hindsight policy that satisfies constraints on average.
 	In this paper, we show that this negative result can be eased in CMDPs with \emph{non-stationary} rewards and constraints, by providing algorithms whose performances smoothly degrade as non-stationarity increases.
 	Specifically, we propose algorithms attaining $\tilde{\mathcal{O}} (\sqrt{T} + C)$ regret and \emph{positive} constraint violation under \emph{bandit} feedback, where $C$ is a corruption value measuring the environment non-stationarity.
 	This can be $\Theta(T)$ in the worst case, coherently with the impossibility result for adversarial~CMDPs.
 	First, we design an algorithm with the desired guarantees when $C$ is known.
 	Then, in the case $C$ is \emph{unknown}, we show how to obtain the same results by embedding such an algorithm in a general \emph{meta-procedure}.
 	This is of independent interest, as it can be applied to \emph{any} non-stationary constrained online learning setting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studied CMDP with non stationary rewards and transitions. A \sqrt{T} + C style regret bound is shown with LAG-FTRL, which is a combination of FTRL and UCB. The algorithm will maintain several instances of the UCB algorithm and pick one according to FTRL.

### Strengths
The paper is well-written and the proof is sound. To the best of my knowledge, this is the first result on CMDP with nonstationary rewards, transitions, and bandit feedback.

### Weaknesses
My main concern is about the static baseline employed. To my knowledge, dynamic regret is usually used as a benchmark in learning in nonstationary environments. The paper has only highlighted the importance of considering static regret when the nonstationary is small (as a constant), which is unlikely to be the case in most environments. When we consider static regret, it is not so surprising that adding a layer of FTRL that "guesses" the corruption level can work, as FTRL already guarantees the static regret. Furthermore, the analysis seems to heavily rely on the assumption that the corruption level is bounded by a constant, which is a strong assumption that limits the applicability of the result. The paper does not provide any justification for why this assumption is reasonable in practical scenarios. The algorithm's performance is likely to degrade significantly if this assumption is violated, which is a major concern.

### Questions
1. Can you elaborate on the comparison of dynamic and static regret when the nonstationary is large? 
2. Can the results be extended to dynamic regret?
3. Can you comment on the technical challenges of deriving the results for static regret?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers CMDPs with both non-stationary rewards and constraints. As the fully adversarial CMDP problem is shown to be statistically intractable, the authors propose to consider the case where the per-round reward $r_t$ / constraint $g_t$ are sampled from some time-dependent distributions whose means do not vary from a "reference" reward / constraint vector significantly.

When $C$ is known, to tackle with the extra uncertainty in rewards and constraints, the confidence intervals are enlarged by an additive factor of $C/N_t(s,a)$. Utilizing policy search over the (estimated) occupancy measures, the algorithm guarantees $\mathcal O(\sqrt T + C)$ regret and constraint violations where $C$ is the level of non-stationarity.

Moreover, when $C$ is unknown, an algorithm-selection meta-algorithm that performs log-barrier FTRL on many base-algorithms with doubling $C$'s is developed.

### Strengths
1. The constraint-violation metric is pretty strong: Albeit the static hindsight optimal policy is allowed to violate the constraints in some rounds and make it up in the remaining, the algorithm is not because of the $[\cdot]^+$ notion.
2. The known $C$ algorithm is pretty intuitive and well-motivated, especially regarding the enlargement of confidence radii.
3. The algorithm also works well when $C$ is unknown, with almost no performance degeneration -- though its quite hard to get the idea and applicability of the framework from the current writing; see the Weaknesses section.

### Weaknesses
1. The algorithmic definitions, especially the $\ell_{t,j}$ and $b_{t,j}$ are written in a highly technical way. For example, without any description on the $\beta$'s in the main text, it is almost impossible to understand the construction of $b_{t,j}$ -- I suggest the authors to exemplify what each $\beta$ would be like if the revised Algorithm 2 is executed on its own. The effect of $\nu_{t,j}$ is also not explained. Specifically, the connection between the bonus term $\nu_{t,j}$ and the exploration-exploitation trade-off is not clear. It's not immediately obvious why maximizing the cumulative sum of $\ell_{t,j}$ with this specific bonus term leads to the desired regret and constraint violation bounds. The role of the max operator in the definition of $\nu_{t,j}$ is also unclear, and how it relates to the confidence intervals is not well-explained.
2. The authors mentioned that the meta-algorithm Lag-FTRL can be of independent interest. Would it be possible to isolate the framework from the base algorithm -- say, what conditions of $\ell_t$ and $b_t$ are required for the framework to work, or it has to be constructed so meticulously as in Eqs. (6) and (7)? It's unclear if the specific structure of $\ell_t$ and $b_t$ is necessary for the meta-algorithm's convergence, or if the framework can be applied to other types of loss and constraint functions. The paper lacks a discussion on the generality of the framework and its potential applications beyond the specific problem considered.

Minor: Line 155 -- the definition of $C$ should be $\max(C_{G^\circ},C_{r^\circ})$?

### Questions
See Weaknesses. These two questions concern the technical hardness and applicability of the Lag-FTRL framework. I am happy to adjust my rating if the answers turn out to be pretty positive.

And also:

3. Is there any intuition why the non-stationarity metric is like this? Would other common metrics like path lengths be harder to tackle?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers constrained MDP under non-stationary rewards and constraints, where the reward, cost functions and the transition kernel are unknown, the level of non-stationarity is measured by $C$ and the constraints is in terms of the expected number of violations. It solves the problem with the knowledge of $C$, followed by an extension to the unknown $C$ case with the help of Corralling method by Agarwal et al. (2017).

### Strengths
- The paper is easy to follow and the intuition of the algorithms is natural.
- This paper adopts $C$ to quantify the level of non-stationarity, bridging the stationary setup and the adversarial setup.
- A meta algorithm is used to deal with the case where the knowledge of $C$ is not provided.

### Weaknesses
 - Given the previous literature (Efroni et al. (2020), Stradi et al. (2024a), Stradi et al. (2024b), Wei et al. (2023)), the proposed problem formulation lacks novelty and motivations. While considering a positive violation seems to be practical, it is more proper to consider a dynamic baseline. Therefore, it is encouraged to provide a more detailed comparison between this work and the literatures in terms of the setups, motivations, and results.
- The proposed algorithm follows the UCB design with $C$ involved, thus, achieving a sublinear regret with respect to the static policy is kind of expected. It would be great if the authors can highlight the technical novelty.
- Simulations are not provided to illustrate the efficacy of the proposed algorithms, as well as comparisons with other baseline algorithms in the literature.
- The paper's theoretical results, while bridging stochastic and adversarial extremes, lack a corresponding lower bound for the intermediate cases. The upper bound is shown to be tight in the stochastic case and adapts to the order of C in the adversarial case. However, the absence of a lower bound for environments that lie between these extremes limits the contribution, as it does not fully justify the tightness of the result in the general non-stationary setting.
- The paper considers a static baseline, which is not the typical choice for non-stationary environments. While the authors motivate this choice by bridging the stochastic and adversarial cases, the dynamic regret is often considered more meaningful in non-stationary setups, which this paper does not address.

### Questions
- Can the authors provide the motivation for considering a static baseline algorithm? When the time horizon $L$ is large, minimizing the regret in the current episode seems to be a natural choice. Thus, the dynamic regret seems to be more meaningful under this nonstationary setup.
- The paper suggests it can ease the negative result of Mannor et al. (2019) by introducing the nonstationary parameter $C$. Is there any lower bound that involves $C$ for the proposed problem under the proposed regret formulation?
- How efficient it is to solve the optimization problem in Line 5 of Algorithm 2?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the constrained Markov decision processes (CMDPs) with adversarial rewards and constraints. Given the negative result of Mannor et al., 2009, the authors propose algorithms whose regret bounds depend on the non-stationarity of rewards and constraints. The proposed algorithm works for unknown $C$ by using a Corral-based technique.

### Strengths
+ To my knowledge, This is the first work considering the CMDPs problem with adversarial rewards and constraints.

+ Authors provide theoretical guarantees for the proposed algorithms and achieve a linearly additive dependence on C.

+ The paper is generally well-written and easy to follow.

### Weaknesses
My primary concern is the limited novelty of the technical contribution, as the approach in this paper appears to be a direct application of techniques from (Jin et al., 2024) for the CMDPs setting. In particular, the core technique and main theoretical analysis to deal with unknown $C$ are largely based on that of (Jin et al., 2024). Given that the corral (Agarwal et al., 2017) with different guesses for $C$ has been used in prior work (e.g., Jin et al., 2024), I believe a more direct comparison to (Jin et al., 2024) is necessary to clarify the technical contributions of this paper.

### Questions
If there are unique technical challenges specific to the CMDPs setting that prevent a direct application of the techniques in (Jin et al., 2024), I would be happy to reconsider and adjust my evaluation accordingly.

### Soundness
3

### Presentation
3

### Contribution
2
