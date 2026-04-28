# High Probability Contextual Bandits for Optimal Dosage Selection

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
Multi-Armed Bandit ($\textit{MAB}$) formulations are commonly used to model the problem of $\textit{Optimal Dose-Finding}$.
However, in many practical applications, it is necessary to receive data about the patient’s current state and then administer a drug dosage adapted to that state. 
To overcome this issue, we adopt a linear contextual bandit formulation with stage-wise constraints.
At each round, the learner selects a dosage and receives both a reward signal and a cost signal.
The learner’s goal is to maximize the drug's efficacy—captured as the expected cumulative reward—while ensuring that the toxicity, reflected by the cost signal, remains below a known threshold.
Satisfying the cost signal constraint only in expectation can be dangerous, as it may lead to over-dosage complications in certain cases.
To address this issue, we introduce a novel model that controls the realization of the cost signal with high probability, in contrast to previous works where control was only applied to the expected cost signal.
Our algorithm follows the $\textit{UCB}$ approach, for which we establish a regret bound over 
$T$ rounds and run numerical experiments.
We further generalize our results to $\textit{non-linear}$ functions and provide a regret bound in terms of the $\textit{eluder dimension}$, a measure of function class complexity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigates linear contextual bandits, with a brief exploration of a nonlinear case at the end, in the context of optimal dosage selection under a constraint function. A UCB-type algorithm is proposed to minimize regret while ensuring that the constraint is satisfied with high probability. Theoretical results are presented, and the approach is validated through numerical experiments.

### Strengths
This work introduces a new area of research: contextual bandits applied to dosage optimization while accounting for a (toxicity) constraint. The reviewer believes that this framework has broad practical relevance, making it a valuable and worthwhile topic to explore further.

### Weaknesses
The main concern raised by the reviewer is related to the assumptions. Specifically, the assumptions for the efficacy generation $R_t=\alpha_t <X_t,\theta^*> + \alpha_t\xi_t^r$ and $C_t=\alpha_t <X_t,\mu^*> + \alpha_t\xi_t^c$ are not intuitive to the reviewer. 

Specifically, the linear relationship between dosage and efficacy/toxicity, as modeled by the inner product, requires more rigorous justification. If $X_t$ and $\theta^*$ represent the efficacy of a medicine per unit, the model implies that efficacy increases linearly with dosage. While this might hold in some cases, it needs more careful consideration and support. Furthermore, the assumption that the variance of the error term increases quadratically with dosage (due to the $\alpha_t$ multiplier on the noise term) is not well-justified. While some increase in variance with dosage is plausible, a quadratic growth rate seems extreme and may not accurately reflect many real-world scenarios. A constant variance of the error term might be a more appropriate choice in many cases. 

Additionally, the presentation of the paper needs improvement for better readability, and the theoretical results should be expanded and explained in greater detail.

There are some minor comments:
$\gamma_\alpha$ is not defined. This should be stated in Assumption 1.
L134-138: not clear
L159-170: Thought X and Y are introduced, they are not explained. Also, the meaning of p_k and q_k should be stated.
L171-176: For the reviewer, it is hard to find some connection between this paragraph and the previous one.
The definition of K(x) should be more clear.
The citation format needs correction, and the language throughout the paper should be made more formal.

### Questions
1. Could the authors please provide justifications of the suggested efficacy and toxicity function by providing real-word examples?
2. In the regret, is it guaranteed that alpha_t is less than alpha_t^\star?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers the problem regret version of the optimal dose finding with constraints that need to be satisfied with high probability.

### Strengths
The paper is well-written and solves a relevant problem. The paper is well-written and organized and is easy to follow.

### Weaknesses
The paper claims that is it the first to consider high-probability constraints on costs. I do not agree, since https://arxiv.org/pdf/2401.08016 ("Contextual Bandits with Stage-wise Constraints") seems to consider the setting with constraints that need to be satisfied with high probability as well. It is true that they need the knowledge of safe action, but I feel that data is benign in this application where there is likely to be a historical data set.

2)The motivation of the regret formulation is not clear. What does high regret mean ? Suppose the safety constraints were easy to satisfy, can then the algorithm just give out the maximum dosage? to make regret negative (Assuming the rewards are positive)

3)The techniques overall are standard in the linear function case. Maybe in future versions, the authors can specifically describe the main challenges faced in the proofs as a separate section

### Questions
Please see above

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the optimal dosage finding problem with two objectives, maximize the drug’s efficacy and ensuring the toxicity especially from a high probability perspective. The authors adopt a linear contextual bandit formulation with stage-wise constraints, and design an efficient algorithm based on the idea of UCB. They establish a regret bound for this high-probability constrained approach, ensuring sublinear regret over time, meaning the model becomes more accurate as it learns.

### Strengths
1. The two-objective problem in dosage finding formulated by the paper is meaningful and practical relevant.
2. The way that how the authors adopt the idea of UCB looks interesting. The technical results are solid.
3. The paper is well written and relatively easy to follow.

### Weaknesses
1. Formulation. I am not sure whether it is common to think that the efficacy and the toxicity are linear with the dosage. From my experience in clinical trials, it is not usually the case. 
2. Technical contribution. I like the authors' way of adpoting UCB, but the techniques seem very standard, mainly based on the repetitive use of the inequality from Abbasi-Yadkori et al., (2011). Is there any technical contribution that the authors want to highlight?
3. A very minor comment: I do not think you need to have a new paragraph only to say like "Proof. The proof is in A.3." You can save a lot of space to present more interesting results.

### Questions
An additional question to the weakness above, what does "stage-wise constraint" mean in the abstract? I can not see any explanation on this in the main text.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel approach for determining optimal drug dosages using a linear contextual bandit model with stage-wise constraints. The key contribution is an algorithm that controls the toxicity of the administered dosage with high probability per step, rather than just in expectation as done in prior literature, thus addressing safety concerns in clinical settings. This method maximizes drug efficacy while minimizing the risk of overdose by ensuring toxicity remains below a threshold. The paper establishes theoretical regret bounds and demonstrates the algorithm's effectiveness through synthetic experiments, highlighting its potential in adaptive dose-finding scenarios.

### Strengths
+ The paper pushes the boundary of dose-finding methodology designs by considering the per-step toxicity constraint in a bandit-based solution. This setting has practical relevance and the solution thus can move the MAB-type methodology to be useful in practice. This aspect itself is very important not only to the ML community but probably more importantly, to the clinical trial methodology design community where safety and efficiency have been two of the critical considerations. 
+ The high probability guarantee of cost violation is a novel component of this work. Prior works have only considered the average cost constraint, which as the authors argued may not be useful in practice. The algorithmic and theoretical aspects of linear contextual bandits are also of interest to other problems.
+ The trick to get around the problem of not having an initial safe dosage is clever.
+ The work makes some effort to extend the design to non-linear functions, with some initial results.

### Weaknesses
 - One aspect that might be interesting to consider is that the toxicity tolerance threshold is often varying across patients. A more practical model would be to set $\tau$ also as a function of $X_t$. Specifically, different patients may have different tolerances to the drug, and this should be reflected in the model by allowing the toxicity threshold to vary based on patient-specific features encoded in $X_t$. This would require a more sophisticated approach to constraint satisfaction, potentially involving learning a mapping from $X_t$ to a suitable threshold.
- The argument in Section 4 relies on using $L$ and $S$ to construct the initial safe interval. This depends on the prior knowledge of accurate $L$ and $S$, which is, in some sense, reflecting the initialization of the trial. So fundamentally this is not surprising. The reliance on accurate bounds for $L$ and $S$ is a critical assumption that may not hold in practice, especially in early-phase clinical trials where the behavior of the drug is not well understood. The sensitivity of the algorithm to inaccurate bounds should be analyzed more thoroughly.
- The algorithm design part in Sec. 4 can be improved by more clearly articulating the differences to LinUCB. While the authors mention that their algorithm builds upon LinUCB, the specific modifications and their implications for the theoretical guarantees are not sufficiently highlighted. A more detailed explanation of how the constraint is incorporated into the LinUCB framework, and how this affects the exploration-exploitation trade-off, would be beneficial.

### Questions
- Back to the issue of not having an initial safe dosage... why can't we just use the minimum dosage as the initial safe dosage?
- What is the theoretical novelty in deriving Theorem 5.1? How is it different than prior proofs of LinUCB or cost-expectation-based solutions?
- The simulations did not have any comparison to prior solutions. Can you add such comparisons? In particular, you have criticized prior solutions as only caring about expected cost constraint -- then how bad are they when you count step-wise constraint violation? What is the tradeoff of regret and constraint violation for all methods?

### Soundness
3

### Presentation
4

### Contribution
3
