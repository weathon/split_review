# A grid world agent with favorable inductive biases

- Decision: Reject
- Scores: 6, 6, 5, 6, 5, 8

## Abstract
We present a novel experiential learning agent with causally-informed intrinsic reward that is capable of learning sequential and causal dependencies in a robust and data-efficient way within grid world environments. After reflecting on state-of-the-art Deep Reinforcement Learning algorithms, we provide a relevant discussion of common techniques as well as our own systematic comparison within multiple grid world environments. Additionally, we investigate the conditions and mechanisms leading to data-efficient learning and analyze relevant inductive biases that our agent utilizes to effectively learn causal knowledge and to plan for rewarding future states of greatest expected return.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose NACE, a technique to efficiently solve grid world environments and compare this to state-of-the-art deep reinforcement learning algorithms.

### Strengths
The experimental results are easy to follow, and the figures are well made.

### Weaknesses
I find the motivation of the authors' interest in gridworld problems to be lacking, and the testbeds to be simplistic. I am not convinced that RL is unable to solve such simple tasks as is claimed by the authors, and believe this to be due to suboptimal hyperparameters which appear to be missing from the text. The overall presentation of the paper lacks sufficient depth in details to where it is difficult to follow along in a meaningful way with notation left undefined. It is written in a manner not meant to be read by someone seeing this material for the first time. For example, Subsection 4.3 should likely be in the beginning of Section 4 or at least before Section 4.2, as it formally defines a rule, what a cell is, that you are doing conjunction, etc. All of this we can assume in 4.3, but for clarity, it should be clearly stated beforehand. 

Some areas the authors spend too much time explaining - for example, DQN or PPO, and a whole page is dedicated to these algorithms; each algorithm's description/shortcoming should have been reduced to 1-2 sentences (e.g., don't need to define DQN here just get to the point), giving the authors 0.5 page back that could have been used to better explain their contribution. At the end, I am left with a feeling that this is nothing new, I am still unclear how this compares to existing work *that is similar*, and how everything ties together. Also, how can DQN not solve MiniGrid-Empty-16x16-v0 but can solve MiniGrid-DistShift2-v0? This makes me question hyperparameters, because it should have been possible for DQN to randomly discover at least once a path from start to goal and then improve upon it, like is seen in the other more difficult task.

Many notations are not defined in 4.4 to the point where the paper is frustrating to read. What are c, v, a, R(r). Is lower-case r rules? Or reward? Why a lower-case r for a set of rules?

### Questions
1. Where does the Curiosity Model fit into the overall NACE Architecture in 4.4?
2. What are c, v, a, R(r). Is lower-case r rules? Or reward? Why a lower-case r for a set of rules?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
NACE (Non-Axiomatic Causal Explorer) is a novel experiential learning agent leveraging causal reasoning and intrinsic reward signals to enable more efficient learning within grid world environments. The authors compare the proposed method against state-of-the-art RL algorithms, demonstrating its benefit in terms of sample efficiency across many different grid world environments.

### Strengths
- Novelty: the work brings novelty due to the adoption of a curiosity model based on causal reasoning. 
- Narration: the paper's narration is well-done and sound, and the work is generally well-written.
- Experiments: the experimental campaign is convincing since it considers several state-of-the-art RL algorithms and exploration frameworks. The evaluation metric regards the sample efficiency of each method, demonstrating NACE's brilliant results.
- Supplementary materials: the attached zip file containing NACE's codebase runs easily and smoothly.

### Weaknesses
 - **Some notations are not very clear.** In particular, the section dedicated to the NACE architecture (section 4.4) leaves some symbols unexplained, such as the observer's sets $M_t^{change}, M_{t}^{observation-mismatched}, M_t^{prediction-mismatched} $, which have been introduced here only in mathematical notation. Still, I would suggest to explain their meaning. Same for the function $f_{exp}$ whose usage and terms composition are not completely clear. The lack of clarity around these sets makes it difficult to understand the precise mechanism by which the agent identifies changes, mismatches between observations and predictions, and how these are used to drive the learning process. The function $f_{exp}$ is also critical to the agent's exploration strategy, and without a clear definition of its inputs and outputs, it's hard to assess the effectiveness of the proposed approach.
- Apart from the notation, also **intuitions behind the need for some components of the architecture are not immediately understandable**. I would have rather added an appendix to explain those details more deeply. For example, I would explain the interactions between the different components of the architecture more verbosely, also describing the flow diagram in Figure 1 and the role of each component in natural language, to give an intuition about the maths behind it. Perhaps, a pseudocode of the entire algorithm could come in handy. The paper would benefit from a more detailed explanation of why each component is necessary and how they interact to achieve the desired behavior. The current description leaves the reader wondering about the specific purpose of each module and how they contribute to the overall learning process. A more intuitive explanation would greatly enhance the accessibility of the work.
- The main limitation of NACE is due to its application since it is **usable only in deterministic grid world settings**. However, authors highlight as future works possible extensions to more complex problems.
- **Experimental setups could have been explained more in detail** in the Appendix, by reporting a more extended description of the presented scenario, perhaps with the support of the relative images (bird-view map). Furthermore, authors could add those scenarios that have not been presented in the main paper, but that can be run in the codebase, such as the *soccer world*. The lack of detailed experimental setup descriptions makes it difficult to reproduce the results and to fully understand the scope of the experiments. The inclusion of bird-view maps and descriptions of additional scenarios would greatly enhance the reproducibility and the overall impact of the work.
- **Hardware employed to run the experiments and time consumption of the framework** not provided.

### Questions
- From learning curves is evident that NACE is more sample efficient than all the other tested algorithms. However, I would like to ask why it is not able to reach the optimal policy and which can be the intuition behind this recurrent behavior.
- Thinking out of the grid world environment, I would like to ask how this method can work and if you see limitations and challenges that have to be considered in more complex problems.
- Regarding non-deterministic transitions, how can NACE give "system tolerance" as stated in line 294?

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
4

### Summary
The authors present NACE, a learning agent which uses strong inductive biases, causal reasoning and a causally-informed intrinsic reward to explore more efficiently in grid-world environments. NACE maintains an internal state consisting of a 2D array corresponding to each cell of the grid world, a 1D array to track non-spatial values such as inventory, as well as a set of rules of the form “(preconditions, action) => consequence” with counts of associated positive and negative evidence. At each step, it updates the 2D array and calculates which observed cells changed and which did not match their predicted values, uses this evidence to update the set of rules, then plans an action sequence to maximize expected return– or if no positive return trajectory is found, then to reach a state with minimum familiarity (average over all cells of how well they match the best fitting rule). Finally, the best-fitting rules are used to predict the cell values of the next state. They test on a number of minigrid environments and show that NACE reaches good performance in about 1000 steps, while existing DRL methods take around 1e6-1e7 steps to reach similar performance, although the best methods converge to higher average rewards at the end of training.

### Strengths
The sample efficiency results look very good.

 In general, the writing quality is high. 

The Observer and Hypothesizer components of NACE, along with the State Match measure of state familiarity, appear to be quite novel. 

Such a method should be quite interpretable - though the authors do not show any of the rules learnt by NACE in the test environments.

### Weaknesses
The authors do not mention or compare to existing methods for efficient structured learning which capture inductive biases, for example [1]. It is hard to evaluate the work’s originality given that the authors did not contextualize it among existing related approaches. 

Though NACE heavily relies on an explicit model of the gridworld, they also do not compare to any explicitly model-based deep RL algorithms such as [2] or [3]. The explicit representation of the grid world as a 2D array, where each cell corresponds to a location in the environment, is a strong prior that is not justified by the experiments. The method's reliance on this explicit representation, and the lack of comparison to model-based RL methods that learn a latent representation of the environment, is a significant weakness.

The significance of the contribution seems limited. NACE shares a lot of weaknesses with existing methods- (depends heavily on quality of state representations, would struggle where defining impactful state changes is difficult) - while lacking strengths (adaptable to continuous state spaces or high-dimensional action spaces, theoretical optimality guarantees). It seems limited to very simple rules, and the environments the authors tested on likewise covered a very small number of dynamics- navigating to a goal location with obstacles, and picking up a key to unlock a door to test sequential dependencies. 

 - The authors did not test the ability to develop rules that capture dependencies across space rather than time, e.g. the need to flip a switch to unlock a set of doors. In fact, because the precondition constraints are defined on cells’ relative positions to the consequence cell, this method would likely do poorly on this dynamic, since this constraint would be best expressed as a condition on a cell specified by its global position (the switch location). 

 - The constraints also require the cells to be exactly equal to a certain value, and are limited to cases where all constraints must be satisfied, rather than other conjunctions like Or, which excludes dynamics where values need only be above some threshold or within a set of allowable values (e.g. the Put Near minigrid environment where the agent must place one object near to another object).

 - The environments did not contain any stochasticity or objects that can move independently of the agent, e.g. the Dynamic Obstacles environment. A core component of NACE is observing which cells changed at each step and using that to create and update rules- is this method robust to settings where cells change irrespective of the agent’s action?

The clarity of the paper has room for improvement:
 - The cell notation is inconsistent and confusing- the subscript changes between $c$, $c_r$, $c_{t,x,y}$, $c_t$ without any explanation. Different symbols should be used for cell variables than for cell values e.g. in the definition $ar{c}:=(c_r=c)$. If the precondition constraints are on cells’ relative positions, there should be notation for that in contrast to the global position notation $c_{t,x,y}$ 

 - K is used for the number of rules and also the number of equality constraints- consider using a different symbol.
some aspects of the method were not fully explained- see the Questions section.

 - Should consider using a different notation for the Match Quotient, since Q is usually used for the Q value function in RL. 

 - Small grammar errors throughout the paper. E.g. “Such [an] approach” on line 154, quotation marks are flipped on line 163

### Questions
Is the match quotient Q(r,c) defined for cell c being the consequence cell?

New rules are created “when positive evidence is found for the first time” - but how are the set of precondition equality constraints determined for the new rule? I.e., how does NACE determine which cells are relevant? 

Why is positive evidence only counted for a rule if all of the precondition cells changed values and/or didn’t match the prediction at the last step? Since the precondition is an AND conjunction of many cell values, it is possible only one might need to change for a rule to be activated. And why can the positive evidence count still increase even if the rule fails to predict the outcome?

Why is the predicted reward not the sum, rather than the average, of the reward of each of the N utilized rules? Each rule seems to describe a way to obtain a certain reward, so if multiple rules are satisfied shouldn’t multiple rewards be obtained?

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
4

### Summary
The authors designed NACE (Non-Axiomatic Causal Explorer), a learning agent that incorporates a set of inductive biases that the authors consider to be important for an acting agent. These include causal relations, temporal locality, spatial equivariance, state tracking, and attentional biases. 
The design of the agent is based on predicate rules that are proposed by the agent given the observations. The agent then plans to either explore rules (to collect new evidence about the rule) or maximize reward.
Finally, the authors test this agent in various scenarios of Minigrid and compare it against a wide range of (deep) RL agents. They show that in these particular scenarios, NACE is particularly sample efficient compared to the RL agents.

### Strengths
1. The paper is motivated by the importance of the inductive biases they propose to grid world environments. Thus, the authors proposed to study these by incorporating them all in their agent design. Finally, showing that these biases have a huge effect on sample efficiency.
2. The paper is mostly well written with some gaps in notation that I had a hard time following (see Questions)
3. The agent design seems to be novel in the way they instantiate the different biases based on predicate rules.

### Weaknesses
1. It is clear that NACE beats all the (deep) RL agents. However, given the comprehensive design, it is hard to understand where the benefit comes from. Perhaps ablating the effects of each inductive bias would be a good way to understand its contribution. For instance, the spatial equivariance is implemented by using a convolutional layer, but it's not clear how much of the performance gain is due to this specific inductive bias, or the use of convolutions in general. Moreover, all RL agents considered are used in all experiments, but each one of them incorporates different biases that are incorporated in NACE. Perhaps grouping the RL agents based on the biases would make a clearer point of the importance of each bias.
2. RL baselines are shown to be less sample efficient. This could be the result of their generality (less inductive biases) as claimed. But I’m concerned that it seems that in all these cases the problems violate the Markov assumption, putting all these RL agents at a disadvantage. Is there an explicit handling of partial observability? Are there any RNNs/memory involved? The paper mentions that NACE maintains a "mental map", but it is unclear how this map is updated and used in the planning process. Specifically, how does the agent handle situations where the map is incomplete or inaccurate due to partial observability?
3. In the formal presentation of the agent, some notation is overloaded (e.g. c for cells, clauses in a rule, c(r) in line 288) which makes some of the method presentation hard to follow. For example, the use of 'c' to represent both cells in the environment and clauses within a rule creates ambiguity, making it difficult to understand the precise meaning of expressions involving 'c'. The notation c(r) is also unclear, as it is not immediately obvious how a cell relates to a rule.
4. Although this is stated at the core of the paper, NACE is specifically designed for the grid world considered. It’s unclear how the results would extrapolate to other type of tasks. Also, I think it would be relevant to compare NACE to RMax, at least to discuss its similarities and differences. Specifically, RMax's exploration strategy, based on counting state-action visits, seems conceptually related to NACE's rule exploration. A discussion of how NACE's approach differs from and potentially improves upon RMax's exploration would be beneficial.

### Questions
1. How does this compare to RMax? It seems to me that it has a similar flavor, in which we observe transitions and the agent explores such transitions until sure.
2. The formal definition of a cell is missing. I supposed the cell is the value of the 3rd dimension of the state definition.
3. Is there any value estimation happening? If so, how are you estimating the value function?

Minor comments
- Planner. Lines 311-314. Unclear wording.
- Overloading c(r) I think (line 288)
- Fix notations (use \citep)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Non-Axiomatic Causal Explorer (NACE), an agent optimized for grid world environments using causality-informed intrinsic rewards and inductive biases, including temporal and spatial modeling, to achieve data-efficient learning. Unlike most standard RL approaches, which require extensive training data, NACE efficiently learns policies in fewer steps by systematically exploring unfamiliar states. Experiments in MiniGrid scenarios show NACE's superior sample efficiency across various environments. The paper suggests that NACE’s principles could extend to more complex domains, promising advancements in data-efficient reinforcement learning.

### Strengths
The authors target a very important and interesting question: How to incorporate inductive bias into Reinforcement Learning and increase the data efficiency. Moreover, the method is compared to various other already established algorithms and tested with different examples.

### Weaknesses
Unfortunately, the reviewer cannot recommend the paper for publication at ICLR due to the following issues:

- The reviewer notes that while NACE’s systematic exploration of unfamiliar states is highlighted as its primary distinction from other RL methods, the incorporation of additional inductive biases defined in Section 4.1 remains unclear. Could the authors elaborate on how each bias is implemented within NACE’s framework? Additionally, conducting ablation studies on the contribution of each inductive bias would provide valuable insight into their individual impacts on performance.

- In the experimental results, the authors present rewards over time steps. Could the authors clarify how time steps are defined in this context? Specifically, are these time steps equivalent to RL framework iterations, with each time step representing the generation and evaluation of a potential solution?

- The reviewer suggests that comparing computational costs between algorithms would enhance the study's rigor. The current comparison lacks detail, as one time step in NACE may involve higher computational complexity than in other algorithms.

- In many of the RL frameworks tested, rewards remain stagnant for extended periods. If the results were examined at a finer scale, would smaller reward changes become visible, or does the mean reward remain consistently at zero?

- After the initial rapid increase in reward, NACE plateaus below the maximum attainable reward across all environments. The reviewer recommends exploring this behavior further and considering modifications to the algorithm that might enhance performance during the latter stages of learning. This could provide insights into whether additional mechanisms could support continued improvement toward optimal rewards.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors introduce NACE, a novel learning agent that utilizes a causality-informed curiosity model to make intelligent hypotheses about causal information in grid world environments. NACE is comprised of 4 components: an observer that updates a "bird-view" map of the environment and assesses prediction-observation failures, a hypothesizer that generates new rules, a planner that balances an exploration-exploitation tradeoff for accruing reward and refining hypotheses, and a predictor that models the environment. The authors assess NACE in a variety of environments from the Minigrid library clustered into three relevant groups: stationary environments, dynamic environments, and dynamic environments with sequential dependencies. Although NACE does not always find the optimal policy, its data efficiency is unparalleled by modern DRL algorithms.

### Strengths
- Existing RL techniques for solving gridworlds are systematically laid out and elaborated on in Section 3, which makes it easy for the reader to contextualize the work.
- Section 4 introducing NACE is concise well-described.
- Section 5 provides compelling results with a comparison to multiple baselines. Figures highlight the salient contributions that the authors attempt to make with NACE: extreme sample efficiency.
- The overall prose of the paper is extremely clear.

### Weaknesses
 - A more thorough discussion of the 5 kinds of inductive biases, including examples, would make them easier to grasp.
- A diagram depicting the states and rule representations described in section 4.3 would be useful. Section 4.3 could use more development and examples.
- An example of a full set of causal rules for a simple environment would be welcomed.

### Questions
1. How were the hyperparameters chosen for the baseline algorithms?
2. Why is NACE unable to find the optimal policy? What improvements could be made to enable NACE to do so? A case-study on a specific environment would be interesting.

### Soundness
3

### Presentation
4

### Contribution
3
