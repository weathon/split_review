# Pessimistic Nonlinear Least-Squares Value Iteration for Offline Reinforcement Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Offline reinforcement learning (RL), where the agent aims to learn the optimal policy based on the data collected by a behavior policy, has attracted increasing attention in recent years. While offline RL with linear function approximation has been extensively studied with optimal results achieved under certain assumptions, many works shift their interest to offline RL with non-linear function approximation.
However, limited works on offline RL with non-linear function approximation have instance-dependent regret guarantees.
    In this paper, we propose an oracle-efficient algorithm, dubbed Pessimistic Nonlinear Least-Square Value Iteration (PNLSVI), for offline RL with non-linear function approximation. Our algorithmic design comprises three innovative components: (1) a variance-based weighted regression scheme that can be applied to a wide range of function classes, (2) a subroutine for variance estimation, and (3) a planning phase that utilizes a pessimistic value iteration approach. Our algorithm enjoys a regret bound that has a tight dependency on the function class complexity and achieves minimax optimal instance-dependent regret %\todoq{problem-dependent or instance-dependent, which one is better? let's discuss} 
    when specialized to linear function approximation. Our work extends the previous instance-dependent results within simpler function classes, such as linear and differentiable function to a more general framework.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of offline reinforcement learning in finite-horizon MDPs with general function approximation, from a theoretical perspective.
The main assumptions are:
- Bellman completeness: completeness of the of the value-function hypothesis class under first and second order Bellman optimality operators, possibly with misspecification
- Uniform coverage of the hypothesis class by the offline dataset, in a novel form suited to general nonlinear value function approximation.
- Access to a computational oracle (nonlinear least-squares regression)

The algorithm is UCBVI-like and combines pessimism variance-weighted least squares regression, where in turn the variance is estimated pessimistically from a fold of the dataset. It is oracle-efficient.

The main theoretical result is an upper bound on the simple regret that scales with the square root of the logarithm of the cardinality (or covering number) of the hypothesis class, and with inverse data coverage as measured by a D^2 divergence. The latter makes the bound instance-dependent. In this way, an instance-dependent regret bound is achieved in a more general setting and with weaker assumptions w.r.t. previous works.

### Strengths
The paper is well written and clear. Theoretical claims are supported by detailed and well commented proofs, the main technical tools are highlighted and explained, and the assumptions are clear.
The summary of the state of the art is particularly complete and detailed. Both the strengths and the limitations of the work are properly highlighted and discussed.

### Weaknesses
I just have some minor remarks:
1. In section 3 I think you went a bit too far with the abuse of notation when defining Bellman operators. Is f a function of the state or the state and action? How can you define the relationship between the Q and the V function of a fixed policy by Bellman's *optimality* operator? The notation $f(s) = \max_a f(s,a)$ is used without explicit definition, which is confusing. Furthermore, the Bellman optimality operator should relate the optimal Q-function to the optimal V-function, not a fixed policy's Q and V functions.
2. Assumption 3.2 is followed/complemented by other assumptions that are just given in-line. I suggest to state them as separate assumptions to improve clarity. Specifically, the realizability and completeness assumptions are intertwined within the discussion of Assumption 3.2, making it difficult to parse the exact requirements.
3. You define $\mathcal{N}$ as the cardinality of the hypothesis class but refer to it as the "covering number". The two are not the same, and the only covering argument that I could find was in Remark 5.3. for the linear case. It's crucial to distinguish between the cardinality of a finite set and the covering number of a function class, especially when the theory is meant to apply beyond the finite case. The current presentation blurs this distinction.

Typos:
- page 4 "closed to the optimal value function"
- page 6: "construct this variance estimator with..."

### Questions
Could you give an intuitive reason for why you also need an *under*estimation of the variance? Also, does it make sense to call it "pessimistic" in this case? A smaller variance estimate has the effect of inflating the value estimate since you are using inverse variance weights, so it would seem more optimistic than pessimistic.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies offline reinforcement learning with non-linear function approximation. It proposes an oracle-efficient algorithm, Pessimistic Nonlinear Least-Square Value Iteration (PNLSVI), for offline RL with non-linear function approximation. The algorithmic design comprises three innovative components: (1) a variance-based weighted regression scheme that can be applied to a wide range of function classes, (2) a subroutine for variance estimation, and (3) a planning phase that utilizes a pessimistic value iteration approach. The algorithm enjoys a regret bound that has a tight dependency on the function class complexity and achieves minimax optimal instance-dependent regret when specialized to linear function approximation.

### Strengths
This paper proposes a pessimism-based algorithm Pessimistic Nonlinear Least-Square Value Iteration (PNLSVI) designed for nonlinear function approximation, which strictly generalizes the existing pessimism-based algorithms for both linear and differentiable function approximation (Xiong et al., 2023; Yin et al., 2022b). The algorithm is oracle-efficient, i.e., it is computationally efficient when there exists an efficient regression oracle and bonus oracle for the function class (e.g., generalized linear function class). In addition, this paper introduces a new type of D2-divergence to quantify the uncertainty of an offline dataset, which naturally extends the role of the elliptical norm seen in the linear setting and the D2-divergence.

### Weaknesses
1. Even though there is an Appendix C explaining the computational aspect of computing the bonus, it seems only address the first bullet point in 4.3. How to computationally efficiently obtain the condition for the second bullet point in 4.3? Specifically, the paper needs to clarify how to efficiently compute or approximate the D2-divergence, which is crucial for the bonus calculation. The current explanation lacks details on how to solve the optimization problem involved in calculating the D2-divergence, especially for complex function classes. It is unclear if there is a closed-form solution or if iterative methods are required, and if so, what are the convergence properties and computational costs. 

2. This paper claims it generalizes over the differentiable parametric models in [Yin et al. 22b], would the main theorem 5.1 improves the results obtained in  [Yin et al. 22b]? It is not clear how the regret bound in Theorem 5.1 compares to the specific bounds derived for differentiable parametric models in prior work. A more precise comparison, highlighting the improvements and potential trade-offs, is needed. For example, does the improved dependency on the function class complexity come at the cost of a worse dependence on other parameters, such as the dataset size or the horizon length?

3. This paper seems to be closely related to [Alekh et al. 23], however is not enough discussion about. May I consider this paper as an offline version of [Alekh et al. 23]? If not, what are differences? The paper should explicitly discuss the similarities and differences between the proposed algorithm and the approach in [Alekh et al. 23]. While the paper mentions the inspiration drawn from [Alekh et al. 23] regarding the D2-divergence, it does not delve into the algorithmic differences. A detailed comparison is needed, including a discussion of whether the techniques used in this paper can be applied to the online setting, and vice versa.

### Questions
Please answer the questions above.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an offline RL algorithm called Pessimistic Nonlinear Least-Square Value Iteration (PNLSVI) for general function approximation. It introduces a type of D$^2$-divergence to quantify the uncertainty of the offline dataset, and proves an instance-dependent regret bound that has a tight dependence on the function class complexity (its covering number).

### Strengths
+ This work fills a gap of designing efficient offline RL algorithms with general function approximation.
+ It extends the concept of D$^2$-divergence in online RL to offline RL.
+ It generalizes reference-advantage decomposition to general function approximation.

### Weaknesses
 - The work is overall incremental. The key techniques are largely known, either from online RL or offline RL. I can see that there are technical barriers in directly extending them to the problem of offline RL with general function approximation, but such extensions are mostly not too difficult.
- Improving the regret by a square-root of $d$ is quite standard for reference-advantage decomposition. This is more about the previous paper not doing the best job than developing truly novel method/analysis.

### Questions
- How to interpret Thm 5.1? 
- When is Thm 5.1 better than instance-independent regret bounds?
- Your coverage assumption is weaker, but does it really matter in practice?
- You assume that dataset is produced by a single BP. In reality, this may not always be true. What is the impact of different BPs?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers offline RL with non-linear function approximation. The authors propose a new pessimism-based algorithm, Pessimistic Nonlinear Least-Square Value Iteration, to solve this problem. The proposed algorithm is oracle-efficient, and achieves instance-dependent regret bound characterized by the newly-proposed $D^2$ divergence.

### Strengths
- The paper proposes an algorithm for offline RL with non-linear function approximation that has instance-dependent regret guarantees, which is new in literature.
- The author extend techniques used for linear MDPs (including variance-weighted ridge regression and reference-advantage decomposition) to nonlinear function classes.
- The paper is generally well-written and clear.

### Weaknesses
 - This paper poses a very strong converage assumption (Assumption 3.5), which may not be realistic in practice. In contrast, most pessimism-based offline RL papers that I'm aware of adopt weaker partial coverage assumptions. I wonder how valuable it is to prove an instance-dependent bound when we have to impose a uniform coverage condition. Specifically, the requirement that the data covers the entire state-action space uniformly seems overly restrictive, limiting the practical applicability of the theoretical results. It's unclear if the derived instance-dependent bound provides a significant advantage over existing methods under such a strong assumption.
- The lower bound cited by the paper only works for linear cases. The authors do not provide a matching lower bound to showcase the optimality of the proposed algorithm with general function approximations. This lack of a lower bound makes it difficult to assess the tightness of the derived upper bound and the true optimality of the proposed algorithm for general function approximation.
- The authors do not provide any numerical experiments in the paper. In my opinion, adding numerical experiments can better showcase the benefits of the proposed algorithm compared to other offline RL algorithms with general function approximation. Without empirical validation, it's hard to assess the practical performance and compare it with existing methods.

### Questions
- Which part of the proof requires uniform data coverage while partial data coverage does not work?
- This paper considers general function approximation, yet I'm unclear what types of function classes & instance structures will satisfy the conditions listed in the paper. Can you give some concrete examples beyond linear MDPs?
- Can you provide a lower bound for general function approximations?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
