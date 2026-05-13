# Solving robust MDPs as a sequence of static RL problems

- Decision: Reject
- Scores: 3, 1, 3, 3, 6

## Abstract
Designing control policies whose performance level is guaranteed to remain above a given threshold in a span of environments is a critical feature for the adoption of reinforcement learning (RL) in real-world applications. 
The search for such robust policies is a notoriously difficult problem, related to the so-called dynamic model of transition function uncertainty, where the environment dynamics are allowed to change at each time step.
But in practical cases, one is rather interested in robustness to a span of static transition models throughout interaction episodes. 
The static model is known to be harder to solve than the dynamic one, and seminal algorithms, such as robust value iteration, as well as most recent works on deep robust RL, build upon the dynamic model.
In this work, we propose to revisit the static model. 
We suggest an analysis of why solving the static model under some mild hypotheses is a reasonable endeavor, based on an equivalence with the dynamic model, and formalize the general intuition that robust MDPs can be solved by tackling a series of static problems. 
We introduce a generic meta-algorithm called IWOCS, which incrementally identifies worst-case transition models so as to guide the search for a robust policy. 
Discussion on IWOCS sheds light on new ways to decouple policy optimization and adversarial transition functions and opens new perspectives for analysis.
We derive a deep RL version of IWOCS and demonstrate it is competitive with state-of-the-art algorithms on classical benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the robust MDP problem in the context of uncertain transition dynamics, assumed to lie within a rectangular uncertainty set. Building on the non-duality-gap property established in previous work, the authors propose a discretization approach to tackle the adversarial problem. Specifically, they sample transition functions from the uncertainty set and iteratively solve the non-robust problem using the sampled transition dynamics. A deep version is also introduced to handle continuous state-action spaces. Numerical results are provided on various MuJoCo benchmarking tasks, comparing the proposed methods with other robust MDP approaches.

### Strengths
- Robust MDP is an important area of study.
- The proposed algorithm appears simple to implement.
- The Deep IWOC represents a meaningful improvement over existing robust MDP methods, which mainly focus on discrete state-action spaces.

### Weaknesses
- The primary sampling-based approach raises significant concerns. Typically, solving a max (or min) problem through sampling requires an exponential number of points to achieve the desired accuracy, making this approach generally intractable from a theoretical standpoint. 

- There is no discussion on the number of transition samples needed to obtain a robust solution.

- The sampling-based approach appears overly simplistic and could be seen as a straightforward baseline for robust MDP. Combined with the lack of theoretical analysis (e.g., theoretical analyses on the impact of the number of samples on the convergence), the contributions feel incremental.

- The proposed algorithm does not seem scalable. The authors should consider comparisons with some model-free algorithms and test on larger benchmarking tasks.

### Questions
- How does the sampling-based approach converge as the number of samples increases? Can the authors provide more analyses (theoretical and experimental)  to support the sampling-based approach?
- Would this approach work with non-rectangular uncertainty sets?
- How does your method compared to model-free algorithms (e.g, Q-learning, SAC, PPO, TRPO ...)?
- How does your method perform with other environments  other than Mujoco (Atari, DM control)?
- Could a simple dual-gradient method solve the minimax problem?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper targets reinforcement learning for MDPs whose transition probabilities are known up to an uncertainty set. Hence, it aims to robustify against these uncertainties and justify the proposed approach empirically.

### Strengths
* The general problem targeted by the paper is relevant and timely. 
* The amount of empirical results is appropriate.

### Weaknesses
* It is hard to talk about soundness of the results because there is no precise problem statement. 
* As such, it is impossible to prove a meaningful result, which is critical when dealing with uncertainties and their impact on performance and safety. 
* The literature within which the paper places itself misses a large body of more relevant work on RL and IRL (which solves a series of RL problems as a subroutine) for robust/uncertain MDPs. This body of work originates from probabilistic formal methods and investigates how existing approaches for planning in robust/uncertain MDPs can be utilized in RL. Examples include the following. https://www.prismmodelchecker.org/papers/neurips22.pdf, https://arxiv.org/html/2312.06344v1, https://arxiv.org/html/2312.06344v1, https://ojs.aaai.org/index.php/ICAPS/article/view/19785
* The method is, at best, ad hoc. The implementation leaves many choices to the user.

### Questions
* The contrast with dynamic uncertainties is an odd choice. That is a generalization of the model considered in the paper. Why would one claim that the setting in the paper is more challenging? Especially without even giving a precise description of what is more challenging.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes solving a robust MDP using a worst-case model search. In particular, it focuses on a static model, where the transition function does not change during trajectory. This setting ensures that the policy computed is less conservative than a policy that solves for a dynamic model. However, solving problems with a static model is harder than problems with dynamic models.

To mitigate this issue, the paper assumes the agent optimizes a stationary policy. Under such assumption, the paper shows that it is sufficient to find optimize for the worst-case transition function: $V^*_\mathcal{T}(s)  = \min_{T\in \mathcal{T}}V^*_T(s)$.

In this case, given the uncertainty set, the proposed approach interleaves the optimization of the policy and the update of the transition dynamics, effectively searching for the worst-case transition function.

The paper provides empirical evidence that the method can converge to robust policies in a tabular setting as well as in a function approximation setting, adapting the SAC method to handle such a sequence of problems.

### Strengths
- The quality of the paper is high. The arguments are presented in a concise and effective way. The description of the algorithm for the tabular case is precise. 
- The writing is clear, and the mathematical notation is precise.
- Strong empirical results against the baseline algorithms under consideration.

### Weaknesses
- The main weakness of the paper is its originality. This is limited since prior work proposes a similar approach to estimate the worst-case MDP to compute a robust policy based on a single transition function (Gadot et al. 2024). 
- The significance of the proposed approach also seems limited when we put it in perspective with the work from Gadot et al. (2024), since this method requires a specialized implementation of the SAC algorithm, while the method from Gadot et al. (2024) does not requires any changes on the underlying RL algorithm. Furthermore, their method already shows the scalability of deep RL algorithms to robust settings, which puts the empirical contribution of this paper in check.
While the paper provides a considerable overview of the related work literature, it misses a key reference, as discussed above. The paper needs a clear discussion of such an approach and, if appropriate, an empirical comparison with it.
Lastly, the presentation of the worst-case identification on the deep IWOCS is difficult to parse. Furthermore, the provided supplemental material does not provide any instructions about how to use the code. A pseudo-code detailing this procedure and instructions to reproduce the experiment would significantly increase the clarity and reproducibility of the paper.   



- Gadot, U., Wang, K., Kumar, N., Levy, K. Y., and Mannor, S. (2024). Bring your own (Non-robust) algorithm to solve robust MDPs by estimating the worst kernel. *ICML*, 14408–14432. <https://proceedings.mlr.press/v235/gadot24a.html>

### Questions
Could you please elaborate on the differences between the proposed method and the approach from Gadot et al. (2024)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work addresses the robust static MDP problem. It is worth noting that when optimizing over stationary policies, the optimal robust static MDP model is equivalent to the dynamic variant. The authors propose an iterative approach that incrementally identifies worst-case transition models. Specifically, given a finite set of uncertain transitions, the method iterates over the uncertainty set to find the optimal policy $\pi_i$ at each iteration $i$ until the condition $V_{T+1}^{\pi_i}(s_0) = Q_i(s_0,\pi_i(s_0))$ is satisfied. The authors further demonstrate a deep RL variant of their algorithm across a variety of standard deep RL benchmarks.

### Strengths
(1) The paper is well-written, showcasing the authors' deep understanding of prior work and foundational concepts in the robust RL community. 

(2) The proposed methodology is clearly and comprehensively explained.

(3) The authors have thoroughly evaluated the performance of their algorithm across a wide range of deep RL control benchmarks, effectively validating its robustness and applicability.

### Weaknesses
The paper has two main weaknesses:

(1) The primary weakness is the lack of theoretical contribution, as most theoretical results presented are well-known. The application of established theories such as the lack of duality gap and the equivalence between static and dynamic stationary models, to the IWOCS setting seems trivial and adds limited novelty. A more in-depth discussion of how IWOCS provides advantages (i.e. scalability analysis, sample complexity) over existing robust MDP algorithms would strengthen the paper. 

(2) The motivation of the paper appears somewhat contradictory. On one hand, it is stated that the static model is more challenging to solve than the dynamic model and is valuable for decision-makers seeking robustness to static transition model uncertainty. On the other hand, the authors note that, under mild assumptions, the static and dynamic models are equivalent. This positioning makes it seem as though the approach achieves similar outcomes to robust value iteration (RVI) but with added complexity. The paper could benefit from more detailed analysis of IWOCS against other robust algorithms beyond short discussion on "rationale to why IWOCS might be a time-efficient algorithm in large scale robust RL problems".

Minor Issue: Algorithm 1 missing close bracket in the if statement: $Q_i(s_0,\pi_i(s_0))$

### Questions
1. In line 199, the authors state, “We consider a (small) discrete set of MDPs,” yet it remains unclear why IWOCS is necessary in this context if $\min_{T \in \mathcal{T}} \max_{\pi} V_T^\pi(s_0)$ can be computed directly when the model uncertainty set of MDPs is small. Specifically, in Algorithm 1, it would be helpful to clarify the complexity of the "Find worst $T_{i+1} = \arg\min_{T \in \mathcal{T}} V_T^{\pi_i}(s_0)$" step compared to a direct computation of $\min_{T \in \mathcal{T}} \max_{\pi} V_T^\pi(s_0)$.

2. In line 252, the authors state that "$T_{i+1}$ can be chosen with another criterion than the worst-case without loosing property 1 and 2". However, for this to hold under alternative criteria, it may be necessary to assume equality when swapping the maximization over policies into other criteria. This assumption may not hold for criteria beyond average and extreme values, potentially limiting the generalizability of this claim.

3. In numerical experiment, the proposed method demonstrate a better performance than other robust RL algorithms. However, this algorithm aim to converge to the the optimizer for RVI, it is unclear to my why it would converge to a better rather than identical optimizer. It is because we worked in deep learning setting and the robust algorithm has no guarantee to converge to optimal? In tabular domain, would the proposed method and RVI have the same optimizer?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a new robust RL methods for MDP with uncertain transitions called IWOCS (Incremental Worst-Case Search). This method incrementally builds a discrete, non-sa-rectangular uncertainty set and a sequence of candidate robust policies. IWOCS can be utilized for classic RL tasks with discrete state/action spaces and Deep RL domains with continuous task settings. The experiments on windy gridworld and Mujoco tasks demonstrate its effectiveness.

### Strengths
1. Improving robustness of RL against transition uncertainty is meaningful for downstream tasks, such as  RL applications on robotics.
2. The extensive experiments on classic and deep RL settings demonstrate the effectiveness of the new method, especially in tasks with continuous state space and action spaces.

### Weaknesses
1. In appendix. I, the author shows the training times for SAC and IWOCS in Mujoco control tasks. As shown in Table 6, IWOCS requires about twice time cost for training compared to SAC, leading to additional burdens in real applications. According to this phenomenon, please provide the following results to analyze and improve the new method:
    1. Provide a more detailed breakdown of where the additional computation time is spent in IWOCS (e.g. worst-case search, policy optimization, etc.). This would help identify specific areas for potential optimization.
    2. Provide potential methods or approaches to reduce the computational cost of IWOCS.
    3. Include training times for other baseline robust RL methods to provide more context for evaluating IWOCS's computational efficiency relative to the state-of-the-art.
2. This work focuses on the RL task with uncertain transition, such as robotics control with dynamic friction settings. This issue is also researched in Meta-RL domains, such as Meta RL methods with task inference. Such methods can adapt to new environment transitions with limited interactions. Please explain the relationship or difference of this work and such meta RL methods. A brief introduction of Meta-RL with uncertain transition should be included in the related work, with highlighting key similarities and differences between IWOCS and meta-RL approaches.
3. Some typos in the manuscript, such as  line 085: denote -> denotes

### Questions
1. In this work, IWOCS only considers a unique starting $s_0$ (Line 067). However, in some tasks such as continuous control tasks, we need to tackle the distribution $p(s_0)$. For example, as shown in Algorithm 2, we need to compute $V_{T_{i+1}}^{\pi_i}(s_0)$ and $Q_i(s_0,\pi_i(s_0))$ during training. How to compute these values for uncertain $s_0$?  Discuss how IWOCS might be extended to handle a distribution of starting states, such as in IWOCS+SAC algorithm for Mujoco control tasks.  
2. As shown in table 2&3, IWOCS* obtains higher performance than IWOCS, which is normal because IWOCS*  utilize grid-search rather than CMA-ES. Please provide a detailed comparison of computation times for IWOCS and IWOCS* across different uncertainty set dimensions. Discuss the trade-offs between performance and computation time when using grid-search vs CMA-ES, and provide guidelines for when to use IWOCS vs IWOCS* based on problem characteristics.
3. Can the idea proposed in this work be utilized in other robust RL problems, such as robust RL under observation perturbations? Please discuss any modifications or potential challenges when applying IWOCS to observation perturbation problems.

### Soundness
3

### Presentation
2

### Contribution
3
