# Maximum Next-State Entropy for Efficient Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Maximum entropy algorithms have demonstrated significant progress in Reinforcement Learning~(RL), which offers an additional guidance in the form of entropy, particularly beneficial in tasks with sparse rewards. Nevertheless, current approaches grounded in policy entropy encourage the agent to explore diverse actions, yet they do not directly help agent explore diverse states. In this study, we theoretically reveal the challenge for optimizing the next-state entropy of agent. To address this limitation, we introduce Maximum Next-State Entropy (MNSE), a novel method which maximizes next-state entropy through an action mapping layer following the inner policy. We provide a theoretical analysis demonstrating that MNSE can maximize next-state entropy by optimizing the action entropy of the inner policy. We conduct extensive experiments on various continuous control tasks and show that MNSE can significantly improve the exploration capability of RL algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article presents a new reinforcement learning method called Maximum Next State Entropy (MNSE) which optimizes next-state entropy through a reversible action mapping layer. MNSE shows better performance than existing methods in complex environments with nonlinear actuators and emphasizes the importance of appropriate model and parameter settings.

### Strengths
1. The experiments cover multiple continuous control tasks, including complex environments like robotic arm control. The results show that MNSE outperforms traditional maximum entropy reinforcement learning methods and other reward-based exploration strategies in these tasks. This indicates the significant potential of the MNSE method in practical applications.


2. The paper provides rigorous theoretical analysis and demonstrates its effectiveness, which is significant for advancing research and development in the field of reinforcement learning.


3. The paper is written in a clear and concise manner. This helps readers better understand and grasp the core ideas and technical features of the method.

### Weaknesses
Given that MNSE relies on the accurate estimation of the dynamic model, how do you ensure the accuracy of these estimations and avoid overfitting? 

Additionally, could you provide guidance on how to reasonably select the hyper-parameters to optimize the algorithm's performance?

### Questions
See questions in Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a new maximum entropy reinforcement learning algorithm where the entropy of the next state is enforced while learning the policy. First a particular policy parameterization is used. Inner actions are first sampled according to a parameterized inner policy (i.e., a parameterized distribution from states to features, called inner actions) and the actions are transformations of these inner actions (piecewise linear in practice, such that the density of actions can be computed based on the density of inner actions using the change of variable theorem). Second, the entropy of next states is decomposed as the sum of: the entropy of the inner policy, the expected probability of the inner actions knowing the state transitions (i.e., knowing the current state and the future state), and a constant term. Then the inner policy is maximized using SAC (applying the outer actions in the MDP). The piecewise-linear transformation is computed to maximize the expectation of the probability of inner actions knowing the state transitions. The probability of (inner) actions knowing the state transition is learned by maximum likelihood estimation. This approach eventually leads to better control policies compared to algorithms that only accounts for the entropy of actions.

### Strengths
1. The problem at hand is very important to the RL community.
2. The approach is novel, the authors introduce a new promising intrinsic reward bonus.

### Weaknesses
1. Some points are unclear and have raised questions, some of which may be critical to the paper. See questions bellow.
2. The authors have missed a large part of the literature that is active in maximizing the entropy of states visited by a policy along trajectories [1, 2, 3, 4, 5]. The latter can be performed with simpler algorithms compared to the one proposed in the paper. In practice those algorithms allow to have a good state coverage, which is the objective pursued by the authors. They should be added in the related works, discussions and experiments.
3. There are errors (or shortcuts) in some equations and notations that make the paper hard to follow and prevent ensuring the correctness of all mathematical developments. Here are those I noticed:

a. In section 3, the reward function is sometimes a function of the action, sometimes not.

b. In equation (2), the distribution $P^\pi$ is undefined.

c. In section 4.1, how are $p(x)$ and $\pi$ related? (There is also a clash of notation between the constant $\pi$ and the policy $\pi$)

d. The inverse dynamic of inner policy is not defined in the main body.

e. In equation (9), I suppose an expectation is missing over the random variable $s$ in the gap term.

f. In equation (10) and (12), the variable $s$ is again undefined in the optimization problem. Is it on expectation or for all $s$, how is it done in practice?

g. Same problem in equation (13), where a function independent of $s$ equals a function of $s$.

h. In section 5.3, is the $x$-variable in the equation the inner action $e$?

i. In many equations $e$ appear as a variable, but should be replaced by $f^{-1}(a, \theta)$ as the expectations are over $a$.

j. There are thee notations for parametric functions that are used together. For example, we have $f(e, \theta)$, $f^\theta$ and $f_\theta$.
4. Section 3 focusses on defining conditions under which the action entropy equals the state entropy. The latter is done based on non-redundant actions and non-redundant policies. From my understanding, the inner policy is not non-redundant, and there are no guarantee that the (outer) policy is eventually non-redundant after optimization. While it can be argued that the discussion is in itself interesting, I think it is confusing to introduce at the very beginning of the paper something that is unused afterwards.
5. There is a methodological error in the experiment. The entropy of the next state is never shown, there is thus no evidence that the method learns high entropy policies.

### Questions
1. What is the advantage of using the function $f$ to increase the gap (and thus control the next state entropy), compared to simply use as intrinsic reward the log likelihood of the inverse dynamics model (and choose f as an identity function, such that : actions = inner actions) in SAC? Similarily, why not simply learning a forward model of the MDP, and using the log likelihood of that model as intrinsic reward, to enforce the entropy of next states? 
2. Could the authors clarify the different parametric functions at hand? What is the advantage of the custom transformation in section 5.3 instead of a normalizing flow?
3. A discretized multinomial distribution is used for the inverse dynamics model. What is the justification for that instead of a normalizing flow (or auto-encoder + ELBO for learning) and how is it limiting in practice?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a thorough theoretical analysis of the relationship between maximizing next-state entropy and policy entropy. The authors propose a novel framework that links these two types of entropy through an innovative approach that utilizes an inner policy and an action mapping function. Based on this theoretical foundation, the authors introduce the Next-State Entropy Maximization algorithm (MNSE), which is shown to be particularly effective in environments with redundant action spaces. This work contributes valuable insights into entropy maximization, bridging next-state novelty concepts with policy design in reinforcement learning.

### Strengths
1. The paper offers a fresh perspective on state novelty by theoretically linking next-state entropy and policy entropy. While state novelty algorithms are known to enhance agent performance in various environments, the theoretical analysis of state entropy remains underexplored. This paper addresses this gap by establishing a detailed connection between next-state entropy and policy entropy, achieved through an internal policy and an action mapping function.

2. The authors provide a rigorous and structured proof process, making it easy for readers to follow the logical progression and understand the interplay between the entropies. This systematic approach gives a solid foundation for the proposed MNSE framework, and the clarity of the theoretical contributions makes the complex subject matter more approachable for readers.

3. The MNSE algorithm is an impressive practical outcome of this research, showcasing strong empirical results in environments with redundant action spaces. This suggests that the algorithm could be beneficial for a wide variety of applications where action redundancy exists, offering new avenues for exploration in reinforcement learning.

### Weaknesses
1. The paper includes performance comparisons at 20% and 40% EAP, as seen in Experiment 2. However, expanding these comparisons to include higher EAP levels, such as 80%, 60%, and 100%, would be beneficial. Analyzing performance across a broader range of EAP settings could offer a more comprehensive view of the algorithm’s robustness and adaptability to different entropy thresholds. Specifically, it is unclear how the performance of MNSE will scale as the entropy regularization term is increased, and whether the observed benefits at lower EAP values will persist or diminish at higher values. A more granular analysis of the performance landscape with respect to EAP is needed to fully understand the algorithm's behavior.

2. The current experiments effectively demonstrate MNSE’s performance in Mujoco and Meta-World environments. However, adding further experiments focused on pure exploration tasks—such as those found in maze environments or other exploration-heavy scenarios—would be valuable. Such experiments could provide deeper insights into how MNSE's maximization of next-state entropy impacts exploration behavior, highlighting its effectiveness in environments where exploration quality is critical. The current environments, while useful for benchmarking, do not isolate the exploration capabilities of the algorithm as clearly as maze-like environments would, where the agent must navigate through sparse reward regions.

3. While MNSE is compared with well-established state novelty and exploration algorithms, such as MinRed and NovelID (both published in 2021), comparisons with more recent approaches (from 2022 or 2023) could further strengthen the relevance and appeal of this work. Including newer algorithms in the comparative analysis could provide a more current context for MNSE’s performance and underscore its competitiveness among recent advancements in state novelty and exploration research. The field has progressed rapidly, and it is essential to benchmark against state-of-the-art methods to fully evaluate the contribution of MNSE.

### Questions
1. In the Related Works section, the authors reference several algorithms (such as SAC, DSPG, CBSQL, and max-min entropy frameworks). Could the authors elaborate on why these algorithms were not included in the experiment section? Understanding the selection criteria for comparison could provide further clarity on the position of MNSE within the broader landscape of state and policy entropy methods.

2. SAC is used as the baseline for updating the policy entropy term in the MNSE framework. It would be interesting to learn how MNSE might perform if alternative algorithms, such as DSPG or CBSQL, were used instead. Could the authors discuss potential outcomes or the theoretical basis for choosing SAC over these other algorithms? Insights into how the baseline choice affects MNSE’s performance would be helpful for researchers considering alternative implementations of the framework.

3. The entropy of all visited states has long been an interesting topic, though challenges remain in addressing it within a solid theoretical framework. Could the authors discuss the correlation between next-state entropy and the total entropy of visited states? This could provide further insight into MNSE’s implications for overall state entropy in agent behavior.

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
5

### Summary
This paper theoretically highlights the distinction between policy entropy and next-state entropy in Markov Decision Processes (MDPs) and makes a compelling argument that the two entropies are equivalent if the policy is non-redundant---meaning that different actions lead to different next states given the same state in the MDP. The paper then shifts its focus to demonstrating the advantages of incorporating maximum next-state entropy into the reinforcement learning process in MDPs. This is done by deliberately introducing saturation and deadzone effects into the control system to create redundant policies. Numerous experiments demonstrate their method can outperform the baselines.

### Strengths
The paper is well-written and clear, with a solid theoretical analysis and a sufficient set of experiments.

### Weaknesses
1. In the introduction, the authors present equipment aging as an example of redundancy in the action space. However, this example does not fully convince the reviewer. Specifically, reinforcement learning assumes that the Markov Decision Process (MDP) remains consistent. When changes occur in the action space, such as those caused by aging equipment, the previously learned policy may no longer perform effectively within the altered MDP. Further clarification or a more suitable example might strengthen this argument.

2. There is an abuse of notation for reward function r(s,a) while the paper assumes the reward is only affected by states.

### Questions
1. Based on the theory, when effective action proportion is 100%, the MNSE should have the same performance as SAC (the base model adopted by MNSE). But in Fig 4. there are some differences, any explanation or analysis on this observation?

2. For eq (4), how can we guarantee the mu variable is positive related with the entropy? The reviewer did not see any further analysis on this part (not even in the appendix).

3. All experiments are conducted in the continuous action space, will maximum next-state entropy benefit the policy learning in discrete action space environments?

4. Can you explain in more details on how to derive the content of equation (8)?

5. To minimize the gap term in Theorem 5.1, step 1 and 2 are provided in equation (11) and (12). Why the parameters of the inverse dynamic of inner policy are optimized first, instead of the ones of the mapping layer?

### Soundness
3

### Presentation
3

### Contribution
2
