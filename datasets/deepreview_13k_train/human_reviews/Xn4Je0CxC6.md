# Dynamic Learning Rate for Deep Reinforcement Learning: A Bandit Approach

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
In Deep Reinforcement Learning models trained using gradient-based techniques, the choice of optimizer and its learning rate are crucial to achieving good performance: higher learning rates can prevent the model from learning effectively, while lower ones might slow convergence. Additionally, due to the non-stationarity of the objective function, the best-performing learning rate can change over the training steps. To adapt the learning rate, a standard technique consists of using decay schedulers. However, these schedulers assume that the model is progressively approaching convergence, which may not always be true, leading to delayed or premature adjustments. In this work, we propose dynamic Learning Rate for deep Reinforcement Learning (LRRL), a meta-learning approach that selects the learning rate based on the agent's performance during training. LRRL is based on a multi-armed bandit algorithm, where each arm represents a different learning rate, and the bandit feedback is provided by the cumulative returns of the RL policy to update the arms' probability distribution. Our empirical results demonstrate that LRRL can substantially improve the performance of deep RL algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a meta-learning algorithm, LRRL, which selects the learning rate throughout the training process using a bandit algorithm. This algorithm is tested in with DQN on deep RL benchmark environments and in conjunction with differnet optimizers such as RMSProp and Adam. Some analysis is done to assess the learning rate choices through learning.

### Strengths
The paper presents the proposed algorithm quickly and the motivation is clear. 
I find that the formulation of the meta-learning problem as a bandit problem is interesting and it is nice to see this direction explored more in this paper.

There are some interesting insights into which learning rates are favourable for different environments by looking at the ones chosen by the proposed algorithm (in Fig.2).

### Weaknesses
Generally, my main concern are the purported benefits of the algorithm.
The original motivation is that learning rates can be important to tune in general and also throughout training. 
From the results (e.g. Fig.1), it looks like the choice of the set of learning rates for LRRL is important. 
Many of the settings do not lead to any benefit over the baseline agent. Moreover, simply choosing the largest set of learning rates, $\mathcal{K}(5)$, does not necessarily lead to any improvements.
This runs counter to the original motivation of reducing hyperparameter sensitivity to the learning rate.

- Tables 1 and 2 which report max average returns seem unecessary given that the entire learning curves are also presented.
Also, reporting the maximum return is generally not a good practice due to the additional noise in the estimate. See [1] for a more in-depth discussion of this. 

- In section 5.1, which optimizer is used with DQN? Is it RMSProp, Adam or a different choice?

- In fig.1, what are "# iterations" on the x-axis? How many training steps are done in total?

- When formulating the meta-learning problem as a bandit problem, the formulation does not make use of the fact that different learning rates are related. In this paper, the learning rates are treated as separate discrete actions while they are in fact continuous quantities. Similar learning rates should have similar optimization properties. 
Perhaps using a formulation that allows some generalization between the bandit actions (learning rates) could be useful here. i.e. linear bandits or more general contextual bandits. 


- Because of the way the reward is structured, it seems like sparse rewards would be a problem for these methods. 
If a feedback window happens to be in the middle of the episode where no rewards are given, then it would make it seem like that meta-action was not useful.
That could explain why in Pong, which has a relatively sparse reward, the agent does not manage to adapt the learning rate much and ends up mostly picking learning rates relatively uniformly.

- As a comment: In the background section (lines 177 onward), it is mentioned that the adversarial bandit framework deals with nonsationarity, but this is not quite accurate. For that, you would need to consider sequences of changing best actions, not just one action in hindsight. For a more detailed discussion, see Ch 31.1 from [2]. I would suggest rewording this section a little.
This does not negatively impact the algorithm in the end since the actual bandit algorithm used does have a decay parameter which does try to account for the nonstationarity by emphasizing recent experiences.

### Questions
- Tables 1 and 2 which report max average returns seem unecessary given that the entire learning curves are also presented.
Also, reporting the maximum return is generally not a good practice due to the additional noise in the estimate. See [1] for a more in-depth discussion of this. 

- In section 5.1, which optimizer is used with DQN? Is it RMSProp, Adam or a different choice?

- In fig.1, what are "# iterations" on the x-axis? How many training steps are done in total?

- When formulating the meta-learning problem as a bandit problem, the formulation does not make use of the fact that different learning rates are related. In this paper, the learning rates are treated as separate discrete actions while they are in fact continuous quantities. Similar learning rates should have similar optimization properties. 
Perhaps using a formulation that allows some generalization between the bandit actions (learning rates) could be useful here. i.e. linear bandits or more general contextual bandits. 


- Because of the way the reward is structured, it seems like sparse rewards would be a problem for these methods. 
If a feedback window happens to be in the middle of the episode where no rewards are given, then it would make it seem like that meta-action was not useful.
That could explain why in Pong, which has a relatively sparse reward, the agent does not manage to adapt the learning rate much and ends up mostly picking learning rates relatively uniformly.

- As a comment: In the background section (lines 177 onward), it is mentioned that the adversarial bandit framework deals with nonsationarity, but this is not quite accurate. For that, you would need to consider sequences of changing best actions, not just one action in hindsight. For a more detailed discussion, see Ch 31.1 from [2]. I would suggest rewording this section a little.
This does not negatively impact the algorithm in the end since the actual bandit algorithm used does have a decay parameter which does try to account for the nonstationarity by emphasizing recent experiences. 


[1] "Deep Reinforcement Learning that Matters" Henderson et al.

[2] "Bandit Algorithms" Lattimore and Szepesvari (Chapter 31.1)  https://tor-lattimore.com/downloads/book/book.pdf

### Soundness
3

### Presentation
3

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
The paper proposes to use a non-stationary version of Exp3 (a multi-armed bandit algorithm) to dynamically adjust the learning rate in deep reinforcement learning models during training. The algorithm begins by initializing a set of learning rates. During training, the Exp3 algorithm selects a learning rate from the set based on the agent’s recent performance. The agent then interacts with the environment for a fixed number of steps using the selected learning rate, before the process repeats.

### Strengths
* The authors show that LRRL achieves competitive performance compared to standard deep RL algorithms that use fixed learning rates or traditional learning rate schedulers. They test the algorithm using the DQN algorithm with the Adam optimizer on a variety of Atari games.
* LRRL reduces the need for hyperparameter optimization in principle, but see below for my concern about this.

### Weaknesses
 * The choice of the number of learning rate arms and their values still requires task-specific tuning. This is evidenced in Table 1, where LRRL seems to have significantly different performance depending on what choice of learning rates are used. I would have expected the bandit algorithm to be relatively robust to its set of arms, but this is not the case. 
    * K_sparse(3) performs far better than the other choices. In my view, this approach seems to just shift hyperparameter tuning to a different parameter.

* One intuition for decay of learning rates is that the optimizer takes large steps toward the optimal policy first (perhaps incurring less reward), but later on "hones in" on the best policy using a smaller learning rate (incurring high reward). The bandit approach wouldn't be able to encode this kind of intuition, where you sacrifice some reward initially so that higher rewards can be attained later on. I think this is a main drawback of this approach.

### Questions
* How would the authors address the concern of having to tune the set of learning rates for Exp3?

* Would Exp3 be able to encode the intuition I described above in some way? How would the authors reconcile this potential drawback?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a bandit algorithm for selecting the learning rate of DQN in a set of Atari games. The paper shows how the bandit-selected learning rates over one fixed set of learning rates can, in some cases, yield better performance than the default DQN learning rate.

### Strengths
* Clear Writing, easy to follow and understand
* Good empirical description. Almost all the necessary details about how the experiment was run were included in the main body or Appendix B

### Weaknesses
 * The biggest weakness is the range of learning rates tested. The paper uses a set of 5 learning rates, all within one order of magnitude, to test LRRL. Most deep RL algorithms are highly sensitive to learning rates. While these are known to be a good range for DQN, as it has been around for over a decade, it is difficult to say whether LRRL equipped with this range will work well with other new algorithms we want to deploy this one. Additionally, would the Adam vs RMSProp results still hold if different ranges of learning rates were given? Two suggestions could address this:
1. Different sets of learning rates for LRRLs.
     - A wider range; Like something that goes from 10^-1 to 10^-6
     - Randomly generated ranges. Maybe have uniform or log uniform sampling over some range 10^-1 to 10^-6, and see how LRRL works with 5 LRs in this range
2. Try with other algorithms (see next bullet point)

* The other big concern with this paper is that it makes claims for Deep Reinforcement Learning Algorithms but only provides evidence on one (DQN). Two fixes could be either:
     - Try LRRL with learning rates on other algorithms: PPO, SAC, A3C, TD3, DDQN etc.
     - Re-adjust the claims in the paper to make it clear that you are studying LRRL+DQN. This would include changes in wording throughout and changing the title to Dynamic Learning Rate for DQN.

* Since the experiments section uses 5 independent runs to measure the average return, we would recommend a different uncertainty measure for the reported results:
     - A bootstrapped confidence interval or a tolerance interval that could be representative of the variability in performance across different seeds and the same learning rate. This would be useful in figure 1.
    - 95% confidence intervals. Although this comes with an assumption that the returns for your given agent+learning rate is normally distributed.
    - The meaning shaded region was not explicitly mentioned any where. I assume it is std dev?

* It would have been useful to see how a bandit algorithm over this set K(5) would compare to other hyperparameter approaches such as bayesian optimization packages like Optuna, which is  commonly used for dynamically tuning learning rates and other deep reinforcement learning hyperparameters.

### Questions
Why was Pong swapped out for Video PinBall in section 5.2? How did the paper choose which Atari games to use for each section? Did the paper look at all Atari environments but reported those with a significant result in the main body? If so, this should be made clear in the main body.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work presents Dynamic Learning Rate for Reinforcement Learning (LRRL), a meta-learning approach that uses a multi-armed bandit algorithm to dynamically adjust the learning rate of an RL agent during training. Each arm of the bandit represents a different learning rate, and the bandit's feedback mechanism uses the cumulative returns of the RL policy to update the probability distribution over the arms. The authors argue that this approach addresses the non-stationarity of the objective function in RL, where the optimal learning rate can change throughout training, and claim that it reduces the need for extensive hyperparameter tuning compared to traditional learning rate decay schedules. Empirical results on several Atari games using the DQN algorithm are presented, comparing LRRL against fixed baselines, traditional schedulers, and alternative optimizers.

### Strengths
Overall, adjusting the learning rate during training is an important problem. The proposed approach is conceptually straightforward, using multi-armed bandits, which is also relatively easy to implement.

### Weaknesses
The main idea in the paper for using bandits for hyperparameter selection in RL is not new. Multiple prior works have explored similar ideas, using bandits to adapt various aspects of learning, including exploration strategies and policy updates. The authors' attempt to position LRRL as a distinct approach within the context of meta-learning is also not entirely convincing, as meta-gradient methods already address the adaptation of learning parameters (see e.g., Flennerhag, Sebastian, et al., among many others).

Re experiments: The scope of the experiments in the paper is limited. The authors focus on a single RL algorithm (DQN) and a restricted set of environments. I propose the authors run their approach using sota RL algorithms, as well as continuous control tasks, which would help understand the broader applicability of LRRL. Finally, the authors should include a comparison of their approach to sota meta-gradient method.

The paper could also benefit from a more detailed discussion of the theoretical properties of Exp3 in the context of learning rate adaptation and a more comprehensive exploration of alternative bandit algorithms (e.g., linear contextual bandits).

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
1
