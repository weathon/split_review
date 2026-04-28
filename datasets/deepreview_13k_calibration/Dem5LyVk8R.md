# Efficient Policy Evaluation with Safety Constraint for Reinforcement Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
In reinforcement learning, classic on-policy evaluation methods often suffer from high variance and require massive online data to attain the desired accuracy. Previous studies attempt to reduce evaluation variance by searching for or designing proper behavior policies to collect data. However, these approaches ignore the safety of such behavior policies---the designed behavior policies have no safety guarantee and may lead to severe damage during online executions. In this paper, to address the challenge of reducing variance while ensuring safety simultaneously, we propose an optimal variance-minimizing behavior policy under safety constraints. Theoretically, while ensuring safety constraints, our evaluation method is unbiased and has lower variance than on-policy evaluation. Empirically, our method is the only existing method to achieve both substantial variance reduction and safety constraint satisfaction. Furthermore, we show our method is even superior to previous methods in both variance reduction and execution safety.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper provides an on-policy evaluation method that aims to reduce evaluation variance while also ensuring safety. This is done in the context of contextual bandits, sequential RL, and offline RL. Via theoretical results, this method is shown to be feasible, unbiased, and variance-reducing. Empirical results on GridWorld and MuJoCo demonstrate that under different cost budgets, the proposed method is able to improve performance (variance reduction) over baselines.

### Strengths
* This work is well-motivated in terms of aiming to reduce variance while also _ensuring safety_ during on-policy evaluation.
* The proposed method is simple, and theoretical results demonstrate that the method is feasible, unbiased, and variance-minimizing.
* The experimental demonstration is solid, with improved performance (variance reduction) over baselines under any given cost budget. The authors demonstrate good experimental practices, including averaging over many runs and comparing against strong baselines.

### Weaknesses
More discussion could be included on the specific form of the safety constraint. In what settings is it sufficient to ensure that "the expected cost of the designed behavior policy $\mu$ should be smaller than the multiple of the expected cost of the target policy $\pi$"? In what settings might this form of safety constraint be insufficient?

### Questions
* What are the implications of considering the undiscounted setting, as opposed to the discounted setting?
* See "Weaknesses"

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses high variance in on-policy evaluation in reinforcement learning by proposing a behavior policy that minimizes variance under safety constraints. Unlike previous methods that ignore safety, this approach provides unbiased, low-variance evaluation while ensuring safe execution. Empirical results show it outperforms prior methods in both variance reduction and safety compliance.

### Strengths
1. The study addresses the new and intriguing problem of incorporating safety constraints in policy evaluation.
2. The paper is well-organized and easy to follow.
3. It provides comprehensive support with both theoretical and empirical evidence.

### Weaknesses
1. While addressing safety constraints is novel, the approach to variance minimization under these constraints lacks significant innovation.
2. In the experimental section, the paper could benefit from comparisons with a broader range of work in safe reinforcement learning to better demonstrate its advantages.

### Questions
1. From my understanding, the algorithm proposed in this paper aims to learn a behavior policy that minimizes variance while satisfying safety constraints. However, I don’t see a clear connection in the theoretical results to the offline dataset used. Could you clarify this? Specifically, if the dataset lacks sufficient coverage, is it still possible to obtain a reliable behavior policy?

2. In the experimental section, the paper compares the proposed method to the Monte Carlo (MC) approach, which seems straightforward but rather basic. Could the authors also consider comparing with online bootstrapping methods, as they might provide more efficient solutions for online policy evaluation?

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
This paper studies the problem of policy evaluation under constraints and proposes an algorithm that reduces the policy evaluation variance while satisfying the constraint.

### Strengths
The proposed solution is derived by formulating and solving an optimization problem, which has support from the theoretical results.

The literature review is thoughtful and complete.

### Weaknesses
In the experiment, the performances of the constrained RL algorithm under different policy evaluation methods should be compared.

See **Questions**

Is the transition from (12) to (13) too conservative? As (12) requires the total cost to be smaller than the threshold but (13) makes the feasible set smaller. What if the optimization problem (13) has an empty feasible set? How to derive Theorem 3 when (13) is too conservative, as the policy $\pi$ will not satisfy this conservative constraint?

How is the proposed method applied to continuous state-action space?

The mainstream policy evaluation uses a one-step method, such as the TD method. Can the proposed method be applied to these methods?

### Questions
Is the transition from (12) to (13) too conservative? As (12) requires the total cost to be smaller than the threshold but (13) makes the feasible set smaller. What if the optimization problem (13) has an empty feasible set? How to derive Theorem 3 when (13) is too conservative, as the policy $\pi$ will not satisfy this conservative constraint?

How is the proposed method applied to continuous state-action space?

The mainstream policy evaluation uses a one-step method, such as the TD method. Can the proposed method be applied to these methods?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes an optimal variance-minimizing behavior policy to guarantee the satisfaction of safety constraints. Theoretically, the authors prove that their proposed method is unbiased and with lower variance. Empirical experiments show that their proposed method achieves variance reduction and safety guarantee.

### Strengths
- The authors address a very important and interesting problem where safety constraint is considered in RL policy evaluation.
- The motivation behind the problem formulation is well-presented while using an example of Google's data center.
- The background section is well-written and easy to follow.
- I think it is a good idea to provide theoretical results and key ideas in the case of contextual bandit.
- Theoretical results are nice and proofs are well-presented.
- The empirical experiments are overall well-conducted.
- The authors' proposed method performs well in Grid-world and MuJoCO.

### Weaknesses
 - In the Related Work section, the literature review of safe RL can be written in a more organized way. There are several survey papers on safe RL, so the authors may want to refer to how to comprehend safe RL.
    - Brunke, Lukas, et al. "Safe learning in robotics: From learning-based control to safe reinforcement learning." Annual Review of Control, Robotics, and Autonomous Systems 5.1 (2022): 411-444.
    - Liu, Yongshuai, Avishai Halev, and Xin Liu. "Policy learning with constraints in model-free reinforcement learning: A survey." In IJCAI. 2021.
    - Gu, Shangding, et al. "A review of safe reinforcement learning: Methods, theory and applications." arXiv preprint arXiv:2205.10330 (2022).
    - Wachi, Akifumi, Xun Shen, and Yanan Sui. "A Survey of Constraint Formulations in Safe Reinforcement Learning." In IJCAI (2024)
- Readers cannot know that this paper deals with off-policy evaluation until line 160. Please clearly mention that in the Abstract or Introduction. It may be better to add "off-policy" in the title. 
- I think lines 309-369 are hard to follow. I understand that (12) is challenging to handle, but it is unclear whether the authors' transformation is reasonable or not. I think it is better to discuss the theoretical relations between (12) and (15, 16), e.g., equivalent, conservative approximation, etc. 
- I think readers cannot identify the magnitude of variance for each algorithm from Figures 1 or 2. There should be a table including the actual variance numbers (at least in the Appendix) like Tables 3 or 4.
- I am also wondering whether the variance of on-policy MC in Tables 3 or 4 is large. I agree with the authors that the proposed method achieves lower variance, but I am not fully convinced of how important are the differences in real applications.
- I think the reproducibility of this paper is rather low given there is no source code attached and there is little information on the experimental setups. It is problematic as a research paper that even basic information is not mentioned for reproducing experimental results.

### Questions
- Q1: I could not understand (12). Why is the safety threshold $(1+ \epsilon)$? In other words, could you tell me the reason why RHS in (12) does not depend on $\pi$? Perhaps is this a typo?
- Q2: The original MuJoCO environment does not have a notion of safety cost. How did the authors introduce safety costs?
- Q3: How was the offline dataset generated? Could you tell me the details? I know there is some statement in the Appendix, but it is critical for understanding the actual performance of the algorithm.
- Q4: Could you show me the experimental results or figures illustrating how the performance of each algorithm is affected by the number of offline datasets?

### Soundness
3

### Presentation
3

### Contribution
3
