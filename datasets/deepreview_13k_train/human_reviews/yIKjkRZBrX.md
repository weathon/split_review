# Learning variable-length skills through Novelty-based Decision Point Identification

- Decision: Reject
- Scores: 3, 8, 5, 3

## Abstract
Intelligent agents are able to make decisions based on different levels of granularity and duration. Recent advances in skill learning with data-driven behavior priors enabled the agent to solve complex, long-horizon tasks by effectively guiding the agent in choosing appropriate skills. However, the practice of using fixed-length skills can easily result in skipping valuable decision points, which ultimately limits the potential for further exploration and faster policy learning. For example, making a temporally-extended decision at a crossroad can offer more direct access to parts of the state space that would otherwise be challenging to reach. In this work, we propose to learn variable-length skills by identifying decision points through a state-action novelty module that leverages offline agent experience datasets, which turns out to be an efficient proxy for the critical decision point detection. We show that capturing critical decision points can further accelerate policy learning by enabling a more efficient exploration of the state space and facilitating transfer of knowledge across various tasks. Our approach, NBDI (Novelty-based Decision Point Identification), substantially outperforms previous baselines in complex, long-horizon tasks (e.g. robotic manipulation and maze navigation), which highlights the importance of decision point identification in skill learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach to learn variable length skills in RL, closely building on SpiRL [1]. This is done using state-action novelty to predict a termination condition for the skills. 








[1] - Pertsch, Karl, Youngwoon Lee, and Joseph Lim. "Accelerating reinforcement learning with learned skill priors." Conference on robot learning. PMLR, 2021

### Strengths
RL with skills can enable much more efficient learning, and is an important problem. Learning variable length skills should allow for more effective learning. However, I have some concerns regarding this paper - please see weaknesses.

### Weaknesses
1. Clarity of proposed approach

The method of variable length skills relies heavily on using state-action novelty to prediction termination conditions. However the exact details for how the state-action novelty module is trained is not explained in the paper (box (i) in the method figure). The paper includes some description of characterizing novelty as inverse visitation count, so do the authors explicitly maintain counts of each seen state? (This will be difficult to scale to environments with continuous states and actions). Or is there some other metric of pseudo counts, involving density estimation? What is the relative effect of using different means to estimate the novelty metric, to predict termination? The reason for this particular analysis is that the novelty estimation is the main contribution of this paper. 

2. Significance of contribution

The proposed method heavily builds on prior work [1], for the components that learn skills and perform RL in the skill space. From the experimental results, the quantitive gains over [1] seem very marginal in the more complex environments (sparse block stacking, kitchen). Can the authors include some analysis of how their discovered skills differ qualitatively in these more complex envs, as compared to [1]?. What are the specific cases in these environments that variable length skills are actually helpful/needed?

### Questions
Please address questions in the weaknesses section

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a unsupervised skill learning algorithm that can extract variable-length skills from a task-agnostic offline dataset. Variable-length skills are motivated by the observation that fixed-length skills often move past critical decision points, like crossroads, resulting in suboptimal performance on downstream tasks. The authors propose to detect such decision points using state-action novelty. The resulting algorithm, Novelty-based Decision Point Identification (NBDI), learns skills together with their termination probability and a prior over the skill space using a latent variable model similar to SpiRL [1]. The authors furthermore provide a complementary perspective on variable termination of skills by relating it to the potential performance gains achieved by terminating and switching to higher-value options, arguing that state-action novelty serves as a proxy for situations where this is likely to be beneficial. Experiments in two maze environments and two robotic manipulation tasks demonstrate that the variable-length skills learned by NBDI lead to better performance in downstream tasks.

[1] Karl Pertsch, Youngwoon Lee, and Joseph Lim. Accelerating reinforcement learning with learned skill priors. In Conference on robot learning, pp. 188–204. PMLR, 2021.

### Strengths
The need for variable-length skills is well motivated by practical examples and a more theoretical argument based on the potential benefits of early option termination.

The paper is furthermore well written and structured and easy to follow. The figures generally do a good job in conveying the intuition behind the algorithm as well as in illustrating the three phases of the algorithm.

The variations of NBDI with different kinds of novelty signals for the training of the termination probability are a good addition to the experiments as they demonstrate that considering state-action novelty is crucial.

The authors furthermore already made the code public.

### Weaknesses
The algorithm is motivated with the concept of novelty, explicitly using a count-based notion of novelty in equation (1). In the experiments section the paper then briefly mentions that Intrinsic Curiosity Module (ICM) is used to obtain state-action novelty values. However, ICM obtains its intrinsic motivation signal from the prediction error of the next state in a learned feature space which is conceptually somewhat different. I think it would be a good idea to discuss to which extent the exact nature of the curiosity signal influences the learned skills. Specifically, the use of a learned feature space within ICM introduces a potential for instability or bias in the novelty signal, as the feature space itself is learned from the data. This could lead to situations where the novelty signal is not truly indicative of novel states or actions, but rather reflects the limitations or biases of the learned feature representation. A more detailed analysis of how the choice of feature space impacts the quality of the learned skills is warranted. 

As evident in the motivating examples, the learned skill termination probabilities depend on the data, in particular on where different actions have been chosen frequently. This poses the question of how dependent NBDI is on a suitable structure being present in the offline dataset. For example, could NBDI work with exploratory data, and if yes, under which circumstances? How does the complexity of the environment influence the requirements on the data? A discussion of these questions would be a good addition to the paper. It is not clear how the method would perform with a dataset that does not have clear decision points, or if the dataset is biased towards certain actions in particular states. This is important to understand the limitations of the method. 

Overall the algorithm is fairly close to SpiRL but this is made transparent so it is not really a problem.

The additional ablations in Appendix A are quite interesting, in particular, the study of the novelty threshold. It would therefore be good to mention them more explicitly in the main text.

### Questions
* In the paragraph “Option Framework”, in the definition $\beta: \mathcal{S}^+ \rightarrow [0, 1]$ the symbol $\mathcal{S}^+$ is not defined anywhere. What does it stand for?
* In equation (5) $\tilde{r}$ is added to the objective in each time step even though $\tilde{r}$ itself is already the cumulative discounted reward for the execution of one skill. Could you maybe explain how to reconcile these definitions?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an approach to for learning variable-length skills by detecting decision points based on the state-action novelty. The algorithm is built based on SPiRL in the offline reinforcement learning setting. The proposed approach achieves positive results on a navigation task and two simulated manipulation tasks for down-streaming evaluation of the learned skills.

### Strengths
1. The proposed approach to find critical decision point during skill discovery makes sense and is an important problem to study in skill/option discovery.

2. The paper is generally well-written and easy to understand. Source code is provided.

### Weaknesses
My main concern for this paper is with the empirical evaluations.
1. Lack of option discovery/learning baselines. As the authors also mentioned in the introduction section, option framework and its related algorithms typically learn a termination condition which functions as a tool to determine whether the agent needs to switch to a different skill. Several recent papers [1, 2, 3] propose to do skill/option discovery from offline data while learning a flexible termination condition just like this paper. But none of them are compared in the empirical results or discussed in the related work section. The proposed approach is only compared to SPiRL which uses a fixed skill length.

2. As it's a offline RL test setting, I think standard offline RL algorithms should be compared to instead of SAC. Moreover, as a general skill discovery method, I would suggest the authors test the proposed approach on more domains.

### Questions
1. Figure 4 is a little confusing. Different training objectives lead to different termination improvement occurrences, but is one of the three results better than the other two? It's not quite straight-forward to me.
2. In section 4.2, the authors claim "The termination improvement theorem basically implies that we should terminate an option when
there are much better alternatives available from the current state." So how do the authors decide which option is a better alternative in this paper's scope?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies learning variable-length skills from data to accelerate RL. It assumes that novel state-actions in data are critical dicision points and the low-level skills should terminate at such points. Thus, the paper proposes NBDI, training an ICM to estimate the state-action novelty and labeling the termination for each data sample. Then, the paper adopts the method of SPiRL, training a latent skill representation, an action decoder (with a termination decoder), and a skill prior, providing temporal abstractions for training a high-level policy with RL. Experiments in Maze show that the method outperforms SPiRL.

### Strengths
1. Extracting skills with variable lengths is beneficial for hierarchical RL. The paper points out a significant issue that existing methods which learn skills from data only use fixed-length skills.

2. Terminating skills at novel state-actions is an interesting attempt to address this problem. Experiments in Maze show that the proposed method outperform the method without variable-length skills (SPiRL); In robotic simulations, it slightly outperforms SPiRL.

### Weaknesses
1. The assumption that "novel state-actions are critical decision points" is **too strong**. I find that datasets used in this paper just meet this assumption: in Maze, the behavior policy only chooses diverse actions at crossroads; in Kitchen, the dataset consists of expert policies accomplishing a fixed set of skills, making the actions diverse at skill success points only. If we use other environments (e.g., robotic tasks without clearly defined skills) or non-expert data collection policies with stochasticity, this assumption will no longer hold, and it is doubtful whether NBDI can outperform SPiRL.

2. In implementations, the ICM is trained and evaluated on a fixed dataset, which **may not reflect the notion of "novelty"** discussed in the paper. In the original usage of ICM, it can estimate novelty in online RL, since the model cannot predict unseen transitions. However, this paper uses ICM to estimate novelty for the training data. Assuming that the model can overfit the dataset, the ICM losses on all training samples are small, thus ICM can fail to evaluate the state-action novelty in the dataset. Furthermore, the paper does not specify the architecture of the ICM, which could significantly impact its ability to capture novelty. A shallow network might easily overfit, while a deeper network might be more robust but also more computationally expensive. The lack of details about the ICM's capacity and training regime makes it difficult to assess the validity of the novelty detection.

3. According to the context, the presentation of the Theorem in Section 4.2 seems redundant. The theorem tells that breaking skills into shorter pieces can improve the high-level controller. But the paper studies how to determine the skill termination points, instead of breaking pre-defined fixed-length skills into shorter pieces. Also, the conclusion in the theorem is straight-forward, while the detailed notations (Q and V) in it are no longer used in the paper. I think the the theorem should be moved to the Appendix.

4. The method is incremental to SPiRL. Its improvement on the two robotic simulation tasks is small, according to Figure 6.

### Questions
1. As I discussed in the Weaknesses (1), when the behavior policies in dataset are non-expert and stochastic, it is questionable whether NBDI can still provide benefits. I think more experimental results are required; otherwise, the authors should make this assumption and limitation clear in the paper.

2. In the experiments, how did you adjust the model capacity and training steps of ICM? If ICM overfits on training data, can it still represent state-action novelty, as I discussed in Weakness (2)?

3. When generating termination labels for the dataset, how to convert the continuous prediction loss of ICM into binary termination labels? Does this require selecting a threshold manually?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
