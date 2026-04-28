# $\beta$-DQN: Diverse Exploration via Learning a Behavior Function

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 3, 5, 6

## Abstract
Efficient exploration remains a pivotal challenge in reinforcement learning (RL). 
While numerous methods have been proposed, their lack of simplicity, generality and computational efficiency often lead researchers to choose simple techniques such as $\epsilon$-greedy.
Motivated by these considerations, we propose $\beta$-DQN. 
This method improves exploration by constructing a set of diverse polices through a behavior function $\beta$ learned from the replay memory.
First, $\beta$ differentiates actions based on their frequency at each state, which can be used to design strategies for better state coverage. 
Second, we constrain temporal difference (TD) learning to in-sample data and derive two functions $Q$ and $Q_{\textit{mask}}$.
Function $Q$ may overestimate unseen actions, providing a foundation for bias correction exploration.
$Q_{\textit{mask}}$ reduces the values of unseen actions in $Q$ using $\beta$ as an action mask, thus yields a greedy policy that purely exploit in-sample data.
We combine $\beta, Q, Q_{\textit{mask}}$ to construct a set of policies ranging from exploration to exploitation.
Then an adaptive meta-controller selects an effective policy for each episode.
$\beta$-DQN is straightforward to implement, imposes minimal hyper-parameter tuning demands, and adds a modest computational overhead to DQN. 
Our experiments, conducted on simple and challenging exploration domains, demonstrate $\beta$-DQN significantly enhances performance and exhibits broad applicability across a wide range of tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new method to perform diverse exploration in the reinforcement learning setting. A behavior function beta is learned on in-sample data to model the coverage of different state action pairs. Then standard DQN learning learns a state-action value function Q. Based on the behavior function and the state-action value function Q, the authors proposed to construct a new Q_mask function that corresponds to a pure exploitation policy due to that less explored actions are suppressed by altering its Q value. Next the paper constructs two basic policies pi_cov and pi_cor that aim at better coverage and bias correction respectively. From there, a set of diverse policies are created. These diverse policies have different levels of exploration and exploitation that intuitively help with the learning process. A meta controller is designed based on non-stationary multi-armed bandit (MAB) algorithms to select a policy from the diverse set, which is then used to interact with the underlying environment to collect new data. Experiments on synthetic data demonstrate the effectiveness of the proposed methodoloy.

### Strengths
(1) The paper studied diverse exploration, which is an important topic in RL.

(2) The proposed method makes intuitive sense, and the way to construct diverse policy set based on interpolation between pi_cov and pi_cor is a reasonable approach.

(3) There are experiments that demonstrate the effectiveness of the proposed method.

### Weaknesses
(1) The paper does not have enough technical contribution. The way to construct diverse policies is elementary. It only concerns learning some function beta that models the data coverage and then doing some policy combination. The way to construct meta controller borrows the MAB framework and does not contain enough novel investigations.

(2) The paper has no theoretical results. The proposed method is not built based on foundational theory but instead some intuitions. This makes the methodology not very trustworthy.

(3) The experiments are performed only on synthetic data and very simple environments. It remains not clear how well the method generalizes to more complicated scenarios such as continuous environment.

### Questions
(1) The experiments are performed on simple environment with finite state and action space. How does the proposed method behave on more complicated tasks that involve continuous states and actions.

(2) How can we derive theoretical results to understand better why the proposed exploration strategy works well?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel off-policy RL algorithm $\beta$-DQN based on DQN. $\beta$-DQN aims to reduce the computation complexity, and the hyperparameter sensitivity compared to the previous exploration RL algorithms. The authors provide experiments on MinAtar and MiniGrid for back up their claim.

### Strengths
The authors propose a novel framework for solving exploration problems in reinforcement learning. The strength can be decomposed as the following:
* Unlike most of the exploration algorithms, the proposed algorithm $\beta$-DQN does not use auxiliary intrinsic reward neural networks to estimate the uncertainty, instead, $\beta$-DQN constructs a set of policy, and treat the RL problem as a MAB (Multi-Armed Bandit) problem by selecting different policies for each episode, with the usage of UCB-alike bonus for exploration.
* The proposed algorithm is much more computationally efficient compared to previous intrinsic-reward based exploration algorithms and has a more structured exploration strategy than \epsilon-greedy.
* $\beta$-DQN adopts the technique of top-$p$ sampling, with a diverse range of $p$ to construct a diverse set of policies with different preferences.

### Weaknesses
1. The proposed algorithm is limited to the discrete action domain while most other exploration algorithms do not have such a limitation, and there is no obvious way to directly apply it to the continuous action domains. 
2. The environments of choice are not standard, and potentially too easy to solve. The scale of both environments is too small, and it is skeptical that the proposed algorithm does not scale to a more standard discrete action domain like Atari. The details of my concern are the following:
* First, the behavior policy \beta is changing every environment step, which means that the "mask" is changing every step. Given that the experiments are only conducted in environments with a limited diversity of observations, the stability of the algorithm when learning in a more complex environment is concerning.
3. The baselines are not tuned, and the selection of the baseline does not align with the main motivation of the experiment. I am going to decompose my reasons as the following:
* The purpose of this paper is to propose a computationally efficient, hyperparameter-insensitive, and well-performing exploration algorithm. However, $\beta$-DQN has two hyperparameters, $L$ and policy set size. Policy set size controls the hardness of the MAB algorithm, whereas the $L$ affects the process of the learning of MAB. The authors provide an ablation study on the analysis of the sensitivity of the size of the policy set but do not provide the ablation study on $L$, which is not enough to convince the reader that $\beta$-DQN is not sensitive to hyperparameters.
* As the authors mentioned in the paper, most exploration algorithms are sensitive to hyperparameters. For intrinsic-reward based ones, they are particularly sensitive to the bonus scale factor $\alpha$. Specifically, the implementation of RND is from the LESSON paper by Kim et al., but the authors use a different $\alpha$ in this paper and achieved better performance compared to the RND in LESSON paper, which further shows that the the hyperparameter selection can be crucial for the performance of exploration algorithm like RND. Without the systematic tuning of hyperparameters for the baselines, it is hard to convince the readers that $\beta$-DQN is preferred. Additionally, the ablation study of the size of the policy set does not show an insensitivity of $\beta$-DQN to this hyperparameter.
Overall, the experiment setup, including the choice of environments, the hyperparameter selections for baselines, and the ablation study on hyperparameters of $\beta$-DQN, does not provide enough information for the reader to decide whether or not $\beta$-DQN is more hyperparameter insensitive, or performs better than other exploration methods.

### Questions
Question:
1. LESSON provides a set of hyperparameters for the MiniGrid domain for RND-based DQN, why do the authors use $\alpha=10$, which is way larger than the hyperparameters that LESSON paper used?

Suggestions:
The authors propose a novel algorithm, that smartly integrates the MAB algorithm in the RL setting to help reduce the computation complexity, however, the claims of "hyperparameter-insensitivity" and "effective exploration" are not sufficiently backed up by the experiment. The detailed suggestions are the following:  
1. Tune the hyperparameters of RND, Bootstrapped DQN in a systematic manner, and show that even the best hyperparameter would not yield better performance compared to $\beta$-DQN, i.e. showing that $\beta$-DQN is indeed favorable compared to them.
2. Compare $\beta$-DQN against the public implementation of RND-PPO and Bootstrapped DQN with the original selection of hyperparameters on the Atari domain, on two sets of environments one contains environments with sparse reward and requiring heavy exploration, the other contains environments with dense reward where even $\epsilon$-greedy can perform well. 
3. Provide a more systematic ablation study for the hyperparameter of $\beta$-DQN.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
$\beta$-DQN is a method proposed to address the challenge of efficient exploration in reinforcement learning. It improves exploration by constructing a set of diverse policies through a behavior function $\beta$ learned from the replay memory. The method is straightforward to implement, imposes minimal hyper-parameter tuning demands, and adds a modest computational overhead to DQN. Experimental results demonstrate that $\beta$-DQN significantly enhances performance and exhibits broad applicability across a wide range of tasks.

### Strengths
1. The method proposed in this paper only requires learning a behavior function, which is straightforward to implement and computationally efficient compared to other methods.
2. The method incorporates both exploitation and exploration at the intra-episodic level, allowing for effective temporal-extended exploration that is state-dependent.
3. The paper reports promising results on MinAtar and MiniGrid, demonstrating that the method significantly enhances performance and exhibits broad applicability in both easy and hard exploration domains.

### Weaknesses
1. The main concern is that the proposed method has a large overlap with a prior work: BAC [1], but there are neither discussion nor comparison in this paper. For example, the idea of learning in-sample state-action pairs in Eq. (2) is similar to Eq. (4.1) in BAC. The idea of making trade-off between standard and conservative Q-value functions in Eq. (5) is similar to Eq. (4.3) in BAC. Apart from being overlapped with BAC, the idea of constructing a policy set has been extensively studied in literature, e.g. [2].
2. There is a lack of baseline algorithms to compare with. The curiosity-driven exploration algorithms should be included as baselines. Specifically, methods like Random Network Distillation (RND) or those based on prediction error should be considered to evaluate the exploration efficiency of the proposed method.
3. The behavior function $\beta$ is learned with supervised learning, and is not robust when facing policy or dynamics shifts. The supervised learning approach might not generalize well when the underlying data distribution changes significantly due to the evolving policy or environment dynamics. This could lead to instability in the training process and hinder the method's performance in more complex scenarios.
4. The DQN-style formulation constrains the action space to be discrete. Therefore, the porposed algorithm cannot fit to continuous control tasks. This significantly limits the applicability of the method in real-world scenarios where continuous control is often required.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper works on improving the exploration-exploitation trade-off in discrete control.
The key idea is to introduce a behaviour network that is trained by supervised update to the replay data.
And further use such a behaviour network to control the behaviour for exploration or exploitation.
The authors further introduce a meta controller to select from a set of potential combinations.

### Strengths
The idea is straightforward and easy to follow. The problem addressed in this paper is important.

The authors conducted plenty of empirical studies, and the results seem to be highly replicable.

### Weaknesses
1. High-level idea: the key insight behind exploration is not simply to visit the actions that are infrequently visited, but to add frequency measure (like the count-based methods) to the value, to perform an exploration-exploitation trade-off. The idea of learning a behaviour density estimator is interesting. However, integrating this with a count-based Multi-Armed Bandit (MAB) for exploration makes the algorithm complex. It becomes difficult to isolate the performance gains specifically attributable to the behavior density estimator, especially when compared to simpler, count-based exploration strategies.

2. The presentation of the paper can be improved. There are many misleading terminology usages. e.g., the *space coverage*, *bias correction*, what does those terms mean in this context? These terms need precise definitions within the framework of the proposed method to avoid confusion.

3. Is the MAB trained concurrently with the Q networks? The interplay between MAB and Q-network training dynamics is unclear. How does the choice of hyper-parameters affect learning stability (it was partially revealed in Figure 6)?  The sensitivity to these hyperparameters is a concern. In practice, is there a golden standard for selecting those hyper-parameters to ensure stable and efficient learning?

4. It would be helpful to have a standard deviation in results (table 1.). Reporting standard deviations would provide a clearer picture of the statistical significance of the performance improvements.

5. In Equation (1), it’s not clear what \beta exactly is and how it is parameterised and optimised. Is it a supervised / behaviour cloning policy?  The paper needs to elaborate on the nature of \beta, its parameterization, and the optimization procedure used to train it. More detail here would enhance the clarity of the core mechanism.

6. Some related works are missing:

Ensemble:
- https://arxiv.org/pdf/1611.01929.pdf discussed ensemble methods in DQN. This is relevant as the proposed method uses a behavior network that could be considered a form of ensembling.
- https://arxiv.org/pdf/2209.07288.pdf discussed the ensemble methods using different hyperparameter settings. This is relevant to the discussion of exploration-exploitation trade-off.

Curiosity-Driven Exploration:
- https://arxiv.org/abs/2206.08332 BYOL-Explore is one of the state-of-the-art exploration algorithms for discrete and continuous control. Comparing the proposed method to BYOL-Explore would provide a better understanding of its performance in the broader context of exploration methods.
- https://arxiv.org/abs/2211.10515
- https://openreview.net/forum?id=_ptUyYP19mP further improves the RND. These works should be discussed and compared, particularly regarding how they address the exploration-exploitation dilemma.

7. The authors mentioned Montezuma's Revenge environment in the introduction but did not experiment in this challenging setting. I wonder if the authors could provide results in such a setting. This is a crucial benchmark for evaluating exploration methods, and its absence raises questions about the method's effectiveness in sparse reward environments.

### Questions
1. High-level idea: the key insight behind exploration is not simply to visit the actions that are infrequently visited, but to add frequency measure (like the count-based methods) to the value, to perform an exploration-exploitation trade-off. The idea of learning a behaviour density estimator is interesting, but integrating this idea with a count-based MAB exploration algorithm makes the algorithm no longer elegant, and hard to identify the performance improvement.

2. The presentation of the paper can be improved. There are many misleading terminology usages. e.g., the *space coverage*, *bias correction*, what does those terms mean in this context?

3. Is the MAB trained concurrently with the Q networks? How does the choice of hyper-parameters affect learning stability (it was partially revealed in Figure 6). In practice, is there a golden standard for selecting those hyper-parameters?

4. It would be helpful to have a standard deviation in results (table 1.)

5. In Equation (1), it’s not clear what \beta exactly is and how it is parameterised and optimised. Is it a supervised / behaviour cloning policy?

6. Some related works are missing: 

Ensemble:
- https://arxiv.org/pdf/1611.01929.pdf discussed ensemble methods in DQN.
- https://arxiv.org/pdf/2209.07288.pdf discussed the ensemble methods using different hyperparameter settings.

Curiosity-Driven Exploration:
- https://arxiv.org/abs/2206.08332 BYOL-Explore is one of the state-of-the-art exploration algorithms for discrete and continuous control
- https://arxiv.org/abs/2211.10515
- https://openreview.net/forum?id=_ptUyYP19mP further improves the RND

7. The authors mentioned Montezuma's Revenge environment in the introduction but did not experiment in this challenging setting. I wonder if the authors could provide results in such a setting.

---

I'm happy to re-evaluate the work if those questions can be addressed.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of designing exploration schemes that are simple, general, and computationally efficient. Towards this end, the authors propose to combine three basic functions: a new beta function the authors learned to explore under-explored actions, the usual Q function for exploring overestimated actions, and finally a Q_mask function designed for exploitation. A diverse set of policies is constructed from them to encourage space coverage or bias correction, and the specific policy used per episode is selected by a meta-controller in a non-stationary multi-armed bandit fashion. Experiments are performed on a few environments and various components of the proposed method are analyzed, which validates the soundness of the proposed exploration scheme.

### Strengths
The authors propose an interesting method to improve exploration. The method is intuitive and the presentation is very clear. It makes sense to me by combining the three basic functions to construct a set of policies that explore for space coverage and another set of policies that explore for bias correction. The toy example on CliffWalk and the related figures are very helpful in understanding/visualizing the method. There are also experimental ablation studies on the method. Overall, the evaluation seems to confirm that this is a sound approach.

### Weaknesses
The experiments can be done more comprehensively. As of this manuscript, the method is only evaluated on a selected set of environments (Asterix, LavaCrossing, RedBlue-Doors). Given the simplicity and generality of the method, it makes sense to conduct a larger-scale experiments. For instance, one could categorize all environments on Atari into easy/hard exploration tasks based on existing literature or established benchmarks and systematically analyze the performance gain/loss of the proposed method. This would allow for a more robust evaluation and potentially reveal interesting insights regarding the method's strengths and weaknesses across different environment types. While the method works right now as of the current presentation, it's unclear how those environments are selected and whether the results generalize to a broader range of tasks.

Furthermore, the observation in Section 5.3.1 regarding the policy selection pattern (Figure 4) could be investigated further. The authors state that "At the beginning, the exploration policies for data coverage (πcov) are chosen more frequently. After a good coverage of the whole state space, the exploration policies for bias correction (πcor) are chosen more frequently in this sparse reward environment." However, this pattern becomes more complicated in the presented experiments. A more in-depth analysis across diverse environments could potentially reveal underlying factors that influence the interplay between πcov and πcor. This could lead to a more nuanced understanding of the method's behavior and potentially suggest improvements for the meta-controller. 

Finally, the claim in Section 5.3.2 that "The policy argmax Q takes greedy actions among the whole action space, it may take overestimated actions thus the performance is not as stable as argmax Qmask." is not fully supported by Figure 5. While argmax Q_mask does appear to perform better, the difference in stability is not immediately obvious from the figure. A more rigorous analysis of the stability of each policy, perhaps using quantitative metrics or statistical tests, would strengthen this claim.

### Questions
1. The toy example is presented well with interesting observations. For example, this makes intuitive sense: "At the beginning, the exploration policies for data coverage (πcov) are chosen more frequently. After a good coverage of the whole state space, the exploration policies for bias correction (πcor) are chosen more frequently in this sparse reward environment." The pattern however does not hold and becomes more complicated in Section 5.3.1 (Figure 4). Could the authors perform more experiments on a diverse environments to see if any insights can be obtained collectively wrt the environment charactristics? 
2. In Section 5.3.2, "The policy argmax Q takes greedy actions among the whole action space, it may take overestimated actions thus the performance is not as stable as argmax Qmask."  Figure 5 doesn't seem to suggest any clearly difference in terms of stability, though argmax Q_mask does perform better.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
