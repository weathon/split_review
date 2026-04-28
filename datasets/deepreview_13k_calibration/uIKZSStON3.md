# In-context Exploration-Exploitation for Reinforcement Learning

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 5, 8, 8

## Abstract
In-context learning is a promising approach for online policy learning of offline reinforcement learning (RL) methods, which can be achieved at inference time without gradient optimization. 
However, this method is hindered by significant computational costs resulting from the gathering of large training trajectory sets and the need to train large Transformer models. 
We address this challenge by introducing an In-context Exploration-Exploitation (\ours{}) algorithm, designed to optimize the efficiency of in-context policy learning. Unlike existing models, \ours{} performs an exploration-exploitation trade-off at inference time within a Transformer model, without the need for explicit Bayesian inference. 
Consequently, \ours{} can solve Bayesian optimization problems as efficiently as Gaussian process biased methods do, but in significantly less time. 
Through experiments in grid world environments, we demonstrate that \ours{} can learn to solve new RL tasks using only tens of episodes, marking a substantial improvement over the hundreds of episodes needed by the previous in-context learning method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel way to leverage the powerful autoregressive sequence learning capabilities in transformer architectures to decision making problems by finding a way to bring in exploration-exploitation for in context policy learning. This goes beyond recent work along with a similar theme for decision making problems (Decision transformers, Algorithm distillation) in two important ways. First, it learns to explore and exploit across multiple episodes concatenated as one sequence, and secondly it is designed to exploit data generated from arbitrary policies that can, in principle, be highly inefficient. 

Experiments are conducted on two well motivated settings -- (1) bayesian optimization and (2) a family of episodic toy RL tasks in a 2d discrete maze. The authors also investigate controlled variations in the data collection policy to highlight how the proposed technique compares favorably to Algorithm Distillation.

### Strengths
- Simple and well articulated but technically precise characterization of the issues surrounding in context policy learning, especially related to epistemic uncertainty.
- The experimental results, while in simple domains at small scale, are nevertheless well motivated and designed to illustrate the promise of the proposed ideas.
- For the BO benchmark, the proposed approach is competitive with EI, but at a small fraction of the cost. For the sequential RL tasks, it achieves better performance compared to other comparable meta learning approaches which were not designed to do exploration in context.

### Weaknesses
The context length requires a sequence of episodes for in-context learning, which can make it fundamentally quite challenging in terms of scale to go beyond small dimensional problems. The reliance on long sequences of episodes, especially when each episode might be of considerable length itself, poses a significant practical hurdle for scaling this approach to more complex, real-world scenarios. The computational cost associated with processing such long sequences, both in terms of memory and time, could become prohibitive. Furthermore, the method's performance is likely to be highly sensitive to the quality and diversity of the training data, particularly the distribution of sub-optimal policies used for data collection. If the training data is not sufficiently representative of the range of possible behaviors, the model's ability to generalize to new situations could be severely limited. 

Nits/minor typos:
- GP biased -> GP based
- pg 3: indefinite -> infinite
- Sec 6: wildly -> widely

### Questions
- The last statement in page 3 seems somewhat ambiguous, could the authors clarify what they mean by this? e.g. _"...Note that the epistemic uncertainty associated with cross sequence latent variables if exist, e.g., the posterior of parameters in $p(\theta)$, would be not learned into the sequence model."_ But shouldn't the true predictive distribution of $y_t$ implicitly encode both the epistemic and aleatoric in the limit of infinite data?

- There could be several reasonable ways to generate suboptimal data for analysis in toy experiments, and the authors have investigated an $\epsilon-$greedy version of the (oracle) optimal where $\epsilon$ is sampled independently for each _episode_ with full $[0,1]$ support. As long as there are enough samples covering a large enough $\epsilon$, a non-trivial part of the episode collection would effectively be oracle policy demos? If that's the case, a more effective stress might be more meaningful e.g. as one possible minimal change, one could sample $\epsilon$ more generally as a beta distribution with two params and rerun the experiments across a range of those params.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies in-context RL and proposes a method that addresses the exploration-exploitation tradeoff. Specifically, during the pre-training, the method assigns a reward to each trajectory so that the model can learn to improve the policy. Furthermore, the paper applies the method on discrete Bayesian Optimization and several RL environments, which show better performance than those of some baselines such Algorithm Distillation.

### Strengths
+ In-context RL is a timely topic in the study of RL and this work provides some interesting idea about the design of in-context RL algorithms.
+ The design of cross-episode reward successfully removes the requirement that the offline dataset is generated from some RL learning algorithms. This design improves the applicability of in-context RL.
+ The experimental results show promising performance of ICEE in the early episodes.

### Weaknesses
 - The experimental evaluation is not sufficient. There is no comparison between in-context RL algorithms and traditional offline RL algorithms, multi-task RL algorithms or posterior sampling based algorithms. The lack of comparison to offline RL methods is particularly concerning, as the method is trained on offline data and should be benchmarked against state-of-the-art offline RL techniques. Furthermore, the absence of comparisons with multi-task RL and posterior sampling methods leaves the reader unsure of the specific advantages of the proposed approach over these established paradigms.
- The proposed ICEE algorithm lacks theoretical performance guarantees. While empirical results are presented, the absence of any theoretical analysis makes it difficult to understand the conditions under which the algorithm is expected to perform well and what its limitations are. This is a significant weakness, as theoretical guarantees provide crucial insights into the robustness and reliability of the method.
- The ICEE algorithm heavily relies on importance sampling and Monte Carlo approximation, which are widely used techniques in traditional RL and not new. The novelty of the method is therefore questionable. The use of importance sampling and Monte Carlo approximation, while effective, does not introduce a significant conceptual leap over existing methods. The paper should more clearly articulate the specific way in which these techniques are applied in a novel way to address the in-context RL problem.

### Questions
1.	The return-to-go for cross-episode seems simple and straightforward. Is it possible to have a more sophisticated design such that the performance can be further improved? For example, current return-to-go seems depends on the order of the offline trajectories. Is there any possible way to avoid this and make design to be order-insensitive?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors develop a in-context exploration-exploitation algorithm for reinforcement learning. This algorithm can be viewed as an extension and refinement of Decision Transformer by generalizing the model from a single episode to multiple episode, and modified the objective to eliminate the bias. The algorithm is extensively tested against Bayesian optimization problems and multiple reinforcement
learning tasks, the proposed algorithm is able to solve sampled games much faster than baseline methods.

### Strengths
The experimental results are very promising. While the algorithm is an extension of Decision Transformer(CT), it certainly outperforms DT significantly.

The application of in-context learning in RL is innovative and has potentials to bring advancement to learning.

### Weaknesses
The explanation provided in the paper on why the proposed algorithm is not very convincing. There is no quantitative analysis provided for identifying the difference between ICEE and DT. As pointed below, some of the explanations of the key ideas in the paper are not very clear.

On page 4, below eq (5), the statement "true posterior distribution of action is biased towards the data collection policy" is not that straightforward from eq (5), could you add more explanations?

Between eq.(7) and eq.(8), maybe the author could be provide some details on the importance sampling trick they mentioned.

### Questions
On page 4, below eq (5), the statement "true posterior distribution of action is biased towards the data collection policy" is not that straightforward from eq (5), could you add more explanations?

Between eq.(7) and eq.(8), maybe the author could be provide some details on the importance sampling trick they mentioned.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel algorithm called In-context Exploration-Exploitation (ICEE). Learning to learn in context is promising but demands extensive learning trajectory data and expansive training of large Transformer models. The ICEE algorithm is designed to address these challenges by augmenting decision transformers with an extra cross-episode return-to-go and training on concatenated episodic trajectories. It learns to balance exploration versus exploitation directly within the Transformer model during inference, eliminating the need for separate Bayesian inference processes. This enables ICEE to tackle Bayesian optimization tasks as effectively as methods based on Gaussian processes but at a notably faster rate. Experimental results show that ICEE can adeptly learn and solve new RL tasks with just tens of episodes, corroborating its efficiency.

### Strengths
**Learning from Episodic Trajectories**: ICEE learns in-context reinforcement learning using merely concatenated episodic trajectories, which makes it a versatile choice for scenarios where abundant learning trajectories are unavailable and constitutes a novel and significant contribution to field of reinforcement learning.

**Connection to Thompson Sampling**: ICEE resolves the exploration-exploitation dilemma in a way analogous to posterior sampling methods, like Thompson Sampling. Given the history, it samples a move that could possibly lead to an improved outcome, gaining either a high return or new information. This method could be the most scalable and efficient implementation among all Thompson Sampling variants.

### Weaknesses
 **Ambiguous Presentation**: Section 3 of the paper feels disjointed from its succeeding sections, leading to some confusion regarding the role and definition of the parameter $\theta$ within ICEE's framework. Specifically, the connection between the theoretical formulation in Section 3 and the practical implementation of the cross-episode return-to-go mechanism is not clearly established. The paper introduces the concept of epistemic uncertainty in the action distribution, but it does not provide a concrete explanation of how this uncertainty is explicitly leveraged for exploration within the ICEE algorithm. The role of $\theta$ as a task parameter is not clearly defined in the context of the reinforcement learning tasks being addressed, making it difficult to understand how the posterior sampling analogy is realized in practice.

**Questionable Experimental Setup**: The experiments predominantly utilize noisy optimal policy variants for data collection. This raises concerns about the generalizability of the results. The use of noisy optimal policies might artificially inflate the performance of ICEE, as these policies already provide a strong signal for learning. It remains unclear how ICEE would perform when trained on trajectories generated from more diverse and less informative policies, such as random or near-random policies. The lack of experiments with such policies makes it difficult to assess the robustness of the proposed approach.

### Questions
1. How is the exploration-exploitation dilemma addressed in ICEE?
2. How does ICEE perform when trained with data collected by random policies?

I will be pleased to raise my score if these questions, especially the first one, can be properly answered.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
