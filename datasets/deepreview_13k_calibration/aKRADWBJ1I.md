# ActSafe: Active Exploration with Safety Constraints for Reinforcement Learning

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
\looseness=-1
Reinforcement learning (RL) is ubiquitous in the development of modern AI systems. However, state-of-the-art RL agents require extensive, and potentially unsafe, interactions with their environments to learn effectively. 
These limitations confine RL agents to simulated environments, hindering their ability to learn directly in real-world settings. In this work, we present \algo{}, a novel model-based RL algorithm for safe and efficient exploration. 
\algo{} learns a well-calibrated probabilistic model of the system and plans optimistically w.r.t.~the epistemic uncertainty about the unknown dynamics, while enforcing pessimism w.r.t.~the safety constraints. Under regularity assumptions on the constraints and dynamics, we show that \algo{} guarantees safety during learning while also obtaining a near-optimal policy in finite time. In addition, we propose a practical variant of \algo{} that builds on latest model-based RL advancements and enables safe exploration even in high-dimensional settings such as visual control. We empirically show that \algo{} obtains state-of-the-art performance in difficult exploration tasks on standard safe deep RL benchmarks while ensuring safety during learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces ACTSAFE, a model-based reinforcement learning (RL) algorithm designed for safe exploration within continuous state-action spaces. ACTSAFE utilizes epistemic uncertainty in the model as an intrinsic reward mechanism to encourage safe set expansion during exploration. The authors provide theoretical analysis that includes safety and sample-complexity guarantees, suggesting that ACTSAFE achieves near-optimal policy convergence within finite episodes. Additionally, a practical implementation of ACTSAFE is proposed, enabling the method to scale to high-dimensional tasks, including visual control. Empirical evaluations demonstrate ACTSAFE’s performance across various benchmarks, supporting both safe exploration and strong task performance.

### Strengths
- Theoretical Rigor: The paper offers a thorough theoretical framework for ACTSAFE, deriving safety guarantees and sample-complexity bounds for safe exploration in continuous state-action spaces—a notable contribution in the safe RL domain.
Scalability in Practical Settings: The authors extend ACTSAFE to visual control tasks, demonstrating scalability beyond low-dimensional models. This practical application is a significant step towards bridging the gap between theoretical safe RL algorithms and real-world, high-dimensional deep RL applications.

- Comprehensive Experimental Analysis: The experimental analysis is extensive, covering both theoretical settings (under the Gaussian process assumptions) and more complex visual motor control tasks in the SAFETY-GYM environment, as well as sparse reward exploration. This breadth of evaluation provides valuable insights into the algorithm's performance under varied conditions.

### Weaknesses
 - Reliance on Assumptions: The theoretical guarantees rely on idealized assumptions (e.g., well-calibrated Gaussian processes and specific Lipschitz conditions), which may limit generalizability. However, the authors provide strong empirical evidence that ACTSAFE performs well even when these assumptions are not strictly met, somewhat mitigating this concern.


### Questions
- The paper mentions the use of offline-collected data comprising 200K environment steps from a random policy. Can the authors clarify how this offline dataset is incorporated into ACTSAFE? Also, are all baseline algorithms utilizing this offline dataset consistently? If not, it may introduce unfairness in the comparisons.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors present a model-based algorithm, called ActSafe, that has strong theoretical safety guarantees.

### Strengths
The paper is very well written. The high level idea of the algorithm is presented in an understandable way, without sacrificing mathematical rigour. By combining existing ideas, like intrinsic motivation or safe Expansion operators, the authors seem to have created a conceptually simple but very powerful algorithm for safe RL. 

Based on a strong theoretical foundation a practical implementation is provided, that crucially maintains the safety constraints. The experiments seem well designed, highlighting the clear strengths of the algorithm (its safety guarantees), while also discussing weaknesses. The authors especially discuss scalability weaknesses that may result from the choice of Gaussian Processes to approximate the system dynamics.

### Weaknesses
While the two-phase approach that ActSafe employs are the foundation for its safety guarantees, I would expect that this comes at a cost. A comparison of total environment steps in both loops required, wall clock or memory requirements would have been a nice addition. Specifically, the paper lacks a detailed analysis of the computational overhead introduced by the initial 'safe set expansion' phase. It's unclear how the number of iterations in this phase scales with the complexity of the environment or the desired level of safety. Furthermore, the practical implications of using Gaussian Processes for dynamics approximation, especially in terms of computational cost and memory usage, are not fully explored. The paper mentions scalability issues, but a more quantitative analysis would be beneficial. For example, how does the time taken for each GP update and prediction scale with the number of data points? Finally, the trade-off between the exploration in the first phase and the exploitation in the second phase is not clearly quantified. It would be useful to see a comparison of the performance of the algorithm with different ratios of exploration to exploitation steps.

### Questions
Safe RL is not my area of expertise, and I therefore ask the metareviewer to discount my (unfortunately brief) review accordingly.

### Soundness
3

### Presentation
3

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
This paper tackles the problem of safe exploration in reinforcement learning by proposing a new model-based constrained RL algorithm. Under the constrained MDP formulation, with regularity assumptions on the underlying dynamical system, the paper demonstrates theoretical safety guarantees and sample complexity guarantees. A practical version of the algorithm with weaker guarantees is shown to be applicable for visual control tasks in different simulated benchmarks. The results show less safety violations compared to prior constrained RL approaches.

### Strengths
- The paper targets a problem that is relevant to a broad community including controls, reinforcement learning, and robotics. Safe exploration in the context of model-based control is interesting because a reliable approach in this space has the potential for being deployed in safety critical scenarios as well as in scenarios that require sample efficiency and real-world exploration is challenging. 

- The proposed algorithm based on intrinsic exploration for reducing uncertainty of policies at the boundary of the current safe set and expanding the safe set based on reachability beyond it, is novel to the best of my knowledge. It is also intuitively sound and doesn't make any fundamentally limiting assumptions of the underlying system. 

- The theoretical guarantees of the base algorithm are strong, and the regularity assumptions seem reasonable to me. 

- The experiments on simulated environments are good, and it is nice to see results in challenging control tasks like a simulated humanoid walking, that go beyond the predominant evaluations of prior safe RL works on simple simulations like SafetyGym.

### Weaknesses
 - A major weakness is that the paper's motivations are disconnected from the experiments. For example the intro states: 

"In many real-world settings, environments are complex and rarely align exactly with the assumptions
made in simulators. Learning directly in the real world allows RL systems to close the sim-to-real
gap and continuously adapt to evolving environments and distribution shifts. However, to unlock
these advantages, RL algorithms must be sample-efficient and ensure safety throughout the learning
process to avoid costly failures or risks in high-stakes applications." 

However the experiments are all in simulated environments and there are no real-world experiments either in a controls setting or in a robotics setting.

 
- It is unclear how the model-based version of ActSafe can be reliably be deployed in the real-world for safety-critical applications. Both theoretically and empirically in the simulated experiments, the constraint violations are lower than the baselines but nowhere close to 0. In addition learning a recurrent state-space model is a more complex choice than directly trying to learn a policy through model-free RL. It is unclear why there are no evaluations in a model-free setting, and what are the motivations for just considering model-based RL, after proposing a safe exploration algorithm that seems to be fairly generic and broadly applicable. It will be helpful to clarify these points. 

- In lines 233-235, it is mentioned that prior works do not have dimensional policies, but there is no explicit clarification about how high dimensional control tasks can the proposed approach tackle.  What are the relative differences? Are there any fundamental assumptions that prevent these prior works from being applicable to higher dimensional tasks?


- The related works seem to miss a lot of prior approaches that also have similar ideas of conservative exploration  and actually demonstrate results on real-world settings where safety in important. For example, see [A-C] below. [A] in particular demonstrates results on real robotic manipulation tasks where safety is critical. 

[A] Thananjeyan, Brijen, Ashwin Balakrishna, Suraj Nair, Michael Luo, Krishnan Srinivasan, Minho Hwang, Joseph E. Gonzalez, Julian Ibarz, Chelsea Finn, and Ken Goldberg. "Recovery rl: Safe reinforcement learning with learned recovery zones." IEEE Robotics and Automation Letters (RA-L)

[B] Bharadhwaj, Homanga, Aviral Kumar, Nicholas Rhinehart, Sergey Levine, Florian Shkurti, and Animesh Garg. "Conservative safety critics for exploration." ICLR 2021

[C] Srinivasan, Krishnan, Benjamin Eysenbach, Sehoon Ha, Jie Tan, and Chelsea Finn. "Learning to be safe: Deep rl with a safety critic."

### Questions
Please refer to the list of weakness above, 

- Can the authors explain the disconnect between the motivations in the paper and the experiments? 

- In lines 233-235, it is mentioned that prior works do not have dimensional policies, but there is no explicit clarification about how high dimensional control tasks can the proposed approach tackle.  What are the relative differences? Are there any fundamental assumptions that prevent these prior works from being applicable to higher dimensional tasks?

- It is unclear why there are no evaluations in a model-free setting, and what are the motivations for just considering model-based RL, after proposing a safe exploration algorithm that seems to be fairly generic and broadly applicable. It will be helpful to clarify these points. 

- In lines 225-226 it seems that in the general case the epistemic uncertainty will be uncalibrated / unreliable due to function approximation errors in the neural network model. Does the theory account for this?

- Can the authors clarify relations to the missing related works, including very related safe exploration works that actually show results in real-world settings?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces ActSafe, a model-based algorithm for addressing the challenge of safe and efficient exploration in continuous state-action spaces, and provides a detailed theoretical analysis of it. This algorithm integrates OPAX and LBSGD with typical model-based RL methods to achieve safe and efficient exploration performance in vision control tasks. They conduct sufficient experiments in Safety-Gym domain, demonstrating that their approach outperforms prior works regarding safe exploration.

### Strengths
1. The problem is well-motivated.
2. This paper is mostly well-written and has solid theoretical foundations. The code provided is very helpful for the reproducibility and review of this paper.
3. The empirical results in sparse reward tasks are impressive.

### Weaknesses
1. The proposed algorithm ActSafe, is a combination of  OPAX, LBSGD, and Dreamer(or other model-based RL methods). The technical contributions are incremental.   But considering the experiments are solid and sound, that should be fine.
2. Inconsistency. This algorithm addresses the problem of safe exploration by maintaining a 'safe set' of policies. However, after checking the code provided, there is no such concept of a 'safe set', they just optimize the actor with the typical safe actor-critic method. Since the theoretical results might be unconvincing because of the inconsistency between the theory and practical implementation, it would be nice if the authors could explain this.
3. Baselines.  In Figure 5, the author compares ActSafe with existing methods like OPTIMISTIC、UNIFORM and GREEDY. Are there any other more competitive baselines?  Comparison with methods like GoSafeOpt、OPAX might be necessary.

### Questions
1. It would be great if the author could address the main weaknesses I have outlined above. If they are properly addressed, I would be happy to raise my score, as I may have misunderstood the paper.
2. Considering that there are no hard constraints on safety during learning in practical implementations, can ActSafe maintain safety during training after removing the initial offline data?
3. I am very familiar with BSRP-Lag, but the algorithm's performance in the PUSHBOX task doesn't quite match my experience, can you disclose more experimental details?

### Soundness
3

### Presentation
4

### Contribution
3
