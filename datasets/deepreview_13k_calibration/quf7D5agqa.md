# Deep Reinforcement Learning from Weak Hierarchical Preference Feedback

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Reward design is a fundamental, yet challenging aspect of practical reinforcement learning (RL). For simple tasks, researchers typically handcraft the reward function, e.g., using a linear combination of several reward factors. However, such reward engineering is subject to approximation bias, incurs large tuning cost, and often cannot provide the granularity required for complex tasks. To avoid these difficulties, researchers have turned to reinforcement learning from human feedback (RLHF), which learns a reward function from human preferences between pairs of trajectory sequences. By leveraging preference-based reward modeling, RLHF learns complex rewards that are well aligned with human preferences, allowing RL to tackle increasingly difficult problems. Unfortunately, the applicability of RLHF is limited due to the high cost and difficulty of obtaining human preference data. In light of this cost, we investigate learning reward functions for complex tasks with less human effort; simply by ranking the importance of the reward factors. More specifically, we propose a new RL framework -- HERON, which compares trajectories using a hierarchical decision tree induced by the given ranking. These comparisons are used to train a preference-based reward model, which is then used for policy learning. We find that our framework can not only train high performing agents on a variety of difficult tasks, but that it can also provide additional benefits such as improved sample efficiency and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces HERON, which leverages the rankings of multiple reward factors (objectives) to derive reward functions using a hierarchical decision tree. This paper is focused on scenarios where numerous reward factors are available for every state-action pair, and it assumes that human experts have ranked these factors to establish their relative importance (weak preferences). When comparing two trajectories, HERON systematically evaluates the reward factors in sequence to determine their preferences. To elaborate, HERON initiates the comparison with the first reward factor, and the labeling procedure (i.e., assigning a binary label) concludes if the disparity exceeds a predefined threshold. If the dissimilarity falls below the threshold, HERON proceeds to compare the next reward factor, iteratively following this process until all the reward factors have been assessed.

### Strengths
* Paper is well structured and easy to follow.

* Extensive evaluation: The authors have extensively validated their method across a wide selection of tasks, including classic control, robotic control, multi-agent traffic light control, and large language model fine-tuning for code generation.

### Weaknesses
 * Lack of justification in reward learning from preferences. In this work, based on ranking between multiple objectives, the authors first generate preferences and train a reward function using cross-entropy loss, which stems from the Bradley–Terry model. Here, the motivation for utilizing a preference-based reward learning framework is unclear. In the original preference-based RL framework, human preferences are generated from the Bradley–Terry model under an unknown utility function and the goal of reward learning is approximating this function based on preference datasets. However, when we have a ranking between multiple objectives, why we also use this framework is unclear. Basically, what is the target of the reward learning? The authors need to clarify this part.

* Lack of ability in personalization. Unlike the standard preference-based learning framework, the ability to obtain personalized rewards is limited. Humans only can specify the ranking between objectives and it is hard to control the tradeoff between objectives. For example, let's consider a case where there are two objectives. Assume that there are two human annotators with the same ranking but the first human wanna get a reward function that emphasizes the first objective more. In this case, this framework can't provide a different reward for two human annotators (because the ranking is still the same). It would be nice if the authors could discuss this limitation.

### Questions
* Learning curves on robotics environments. It would be nice to include the learning curves on robotics environments in the main draft or appendix. 

* Standard deviation across different trials is quite high in Figure 3a and Figure 3c. It would be nice to tune some hyper-parameters for DDPG or Q-learning.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In reinforcement learning, it is crucial to design a reward function that reflects the objective of the task. It can be complicated or error-prone to define the exact reward function. In practice, we can define some reward factors and the reward function is a weighted combination of the reward factors.

Instead of using a weighted sum of reward factors, this work proposes a ranking approach, where the reward function is determined by the ranking of the reward factors. The HERON framework is evaluated on various domains.

### Strengths
Compared to weights, ranking can be more interpretable and easier to design. Empirically, RL trained using the ranking-based reward model outperforms other baselines.

### Weaknesses
Rankings of reward factors can be less expressive than weighted combinations of reward factors. In other words, some reward functions can be expressed as weighted sums, but not as a ranking of reward factors. It would be helpful to have discussions on this.

Clarity: It would be helpful to make the setting clearer. My understanding is that the input to the reward model training process is no longer preference data ($ \{ (\tau_w, \tau_l), \dots \} $), but an ordered list of reward factors. In other words, the reward model training part is not changed, but only the input to the reward model training is changed.

Minor:
* In Alg 1, the condition in while is not syntactically correct ($l \leq n \ \mu = 0$).
* You may move the legend in Fig. 3 out of the plot so readers can see the plot clearly.

### Questions
In the experiments, if the ground-truth reward function is a linear combination of reward factors, using the rank of significance of the reward factors is enough to learn a good policy? Empirically, this seems to be the case for robotic control tasks. Can authors provide an intuition behind this?

Can reward factors serve as a reward model directly without using the method proposed in this paper? For example, we can define a reward function like 10^4 * first_reward_factor + 10^3 * second_reward_factor + ..., where 10^i can be adjusted.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addressed the reward design problem in RL. This paper proposed HERON, a novel RL framework that utilizes rankings of reward factors to design reward functions by employing a hierarchical decision tree for trajectory comparisons and preference-based reward modeling. This paper assumed weak preference supervision where there are three labels in comparison: A is better, B is better, and tie. If the comparison result is "tie", then, this method moves to the next stage and does the same thing. This decision tree is a cascade of binary classifiers. In experiments, HERON outperforms reward engineering approaches, reduces tuning costs, improves accessibility, and achieves robustness in various RL environments.

### Strengths
- HERON introduces an approach to distill rewards from relative feature rankings, filling a crucial gap in RLHF.
- The paper provides some evaluation, spanning a wide range of tasks.
- Addressing the challenge of reducing the human labeling burden in RLHF, HERON offers a solution that achieves parity with RL in various tasks, making it a valuable contribution to the field.

### Weaknesses
 - Marginal Improvement: HERON demonstrates only marginal or no substantial improvement over straightforward heuristic baselines in many environments, reducing confidence in its efficacy. The reported improvements, such as 7.8% in robotics, 33% in traffic light control, and 3.9-5.2% in coding, are not consistently significant across all tasks. In some cases, the gains appear to be incremental rather than transformative, raising questions about the practical impact of the method. The lack of a consistent and substantial performance boost across diverse environments suggests that the method's effectiveness might be limited to specific scenarios or tasks, rather than being a general solution.
- Unconvincing Comparison: Directly comparing HERON to standard RLHF methods, which often operate in settings with unavailable or human-annotated reward factors, may not provide a fair or meaningful benchmark. The paper's claim that it is not an RLHF method does not negate the fact that it draws inspiration from RLHF and tackles a similar problem of reward design, making comparisons to existing RLHF methods relevant. The comparison to heuristic baselines, while informative, does not fully address the question of how HERON compares to state-of-the-art methods designed for similar reward design problems, particularly those that also leverage preference-based learning.

### Questions
1. Performance Comparison: How does the proposed method compare to existing state-of-the-art approaches in terms of performance, and what are the key differentiators? Comparative analysis is crucial to demonstrate the novel contributions of the proposed method. Evaluating its performance against existing methods (such as PEBBLE or Meta-RewardNet in control domain) highlights its strengths and areas where it excels. I think that comparison with existing RLFH methods is important since this paper targets the same problem in RL. (If this paper targeted only NLP domain or focused on the contribution in code generation, I think it is not essential.)

2. Addressing Limitations: Have the authors considered potential limitations and challenges of their method? Are there opportunities for further exploration or improvements in addressing these limitations? 

3. Practical Significance: Is there a clear motivation and real-world application for the proposed research? How does the paper demonstrate the practical significance of the findings?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new method for reducing the cost of human annotations when trying to avoid manual reward engineering for reinforcement learning. Their method uses several easy to compute reward factors and it compares trajectories based on these factors by going from more important to a less important factor. These comparisons are then used to fit a reward function which is used in RL optimisation. The authors present results on a set of diverse benchmarks ranging from control to traffic simulation and coding.

### Strengths
- The paper attempts to design an alternative approach to reward engineering, which could potentially lead to more principle and stable performance.
- The method also avoids costly human annotations.
- The authors conduct a number of ablations and analysis targeted at understanding the strengths and weaknesses of the proposed method.
- The authors study a diverse set of applications from different domains.

### Weaknesses
 - The paper is not very clearly written and it left me with a few unclear points which are important for the proposed problem setting. The authors start by talking about human feedback in reinforcement learning, but it is not clear from the method description what feedback is provided by humans. Is it the order of factors? Or is it feedback in the form of comparisons? What exactly is the problem setting? For example, what are the assumptions about the relationship between the reward factors and the true reward? 
- Assuming that humans provide the comparisons in the form of weak preferences, it is not clear to me how it can be ensured that comparisons are in the form described on page 4 (fixed precise threshold, always correct). Also, usually in RLHF the humans would provide comparisons of full trajectories because this is a more reliable feedback compared to other types of feedback. Assuming that the comparisons are coming from the algorithm itself, it seems to me that the method is just a form of reward engineering that allows one to find the coefficients by ensuring certain rules (the importance order of factors) are respected. 
- One limitation of the method is that it requires reward factors which are hand crafted. In many real world applications of RL there has been a tendency of moving away from the hand crafted rewards and learning reward functions directly from the observations which are represented in the raw form (e.g., images or text). I would like to hear a discussion on the applicability of the method to the various realistic domains. 
- I have some questions and concerns about the experiments. For example, in all three environments the authors say that the ground truth reward is a linear combination of the factors. In this case it is not clear to me why one would need a non-linear function (MLP) for the learnt reward. Then, regarding the baselines, a classical baseline would be a (potentially linear) reward learnt as a function of factors on the basis of trajectory comparisons from human annotators. This is the most classical RLHF setting and it would be informative to compare the proposed method to it.

Minor points:
- I didn't find Algorithm 1 and Figure 2 necessary for understanding that part of the methodology, I think it can be skipped in favor of a more clear description of the problem setting and assumptions.
- I didn't understand why GT line is worse than other methods in Figure 3(c).
- Section 4.3 argues that the proposed method is quite flexible. It would be nice to hear a discussion of how this compares to the studied baselines such a reward engineering.

### Questions
I would like the authors to elaborate on the problem setting and assumptions (in particular relationship between the factors and true rewards). Also, I would like to understand better the principal difference of the proposed method to reward engineering and to see comparison to a more traditional reward learning scenario from RLHF.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
