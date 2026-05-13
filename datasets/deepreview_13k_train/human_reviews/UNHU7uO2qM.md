# Knowledge Retention in Continual Model-Based Reinforcement Learning

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
We propose DRAGO, a novel approach for continual model-based reinforcement learning aimed at improving the incremental development of world models across a sequence of tasks that differ in their reward functions but not the state space or dynamics. DRAGO comprises two key components: $\textit{Synthetic Experience Rehearsal}$, which leverages generative models to create synthetic experiences from past tasks, allowing the agent to reinforce previously learned dynamics without storing data, and $\textit{Regaining Memories Through Exploration}$, which introduces an intrinsic reward mechanism to guide the agent toward revisiting relevant states from prior tasks. Together, these components enable the agent to maintain a comprehensive and continually developing world model, facilitating more effective learning and adaptation across diverse environments. Empirical evaluations demonstrate that DRAGO is able to preserve knowledge across tasks, achieving superior performance in various continual learning scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses continual model-based reinforcement learning where an agent faces a sequence of tasks that share state/action spaces and dynamics yet differ in terms of rewards and initial states. The agent is assumed not to have access to data collected from previous tasks and, hence, utilizes a learned world model to adapt to such nonstationarity. The authors claim that naive model-based RL methods struggle with catastrophic forgetting, a phenomenon where the agent loses knowledge acquired in earlier tasks. To address this, the authors develop DRAGO, combining two components called 'Synthetic Experience Rehearsal' and 'Regaining Memories Through Exploration', respectively. The former utilizes a generative model to learn from synthetic experiences resembling the agent's past experiences in earlier tasks. Through an intrinsic reward function, the latter incentivizes the agent to explore states similar to those seen in the previous task while penalizing for visiting states that its current learned dynamics model is familiar with. The authors evaluate DRAGO on three domains, where as the task changes, the dynamics remain the same, yet there is a small overlap between the parts of the state space where the agent spends time. The empirical results indicate that DRAGO can retain previous knowledge and use it to transfer it to new tasks. In contrast, baselines either fail to do so or achieve similar performance but inconsistently.

### Strengths
- The motivation behind this work and the intuition behind why naive methods fail are clearly explained with the support of visualizations. Section 3 is generally well-written, but it may be missing some details about how a generative model operates in this setting.

- The experimental set-up makes sense and is clear about the properties of the environments, e.g., overlap between visited states in different tasks.

- Qualitative and quantitative results demonstrate how DRAGO is more advantageous than the baselines in the studied domains. The ablation study and the experiments on few-shot transfer provide more details about DRAGO's performance.

- Related work is very detailed.

### Weaknesses
 - Although the nonstationary nature of the environment comes from the change in rewards and initial states, DRAGO focuses on continually learning a world model. If I understand it correctly, the agent needs access to reward and value models associated with a task at hand at inference time, and these models are relearned for every new task. This is possibly why the other methods can perform similarly in continuous control benchmarks (middle and bottom rows in Figure 5), where there is sufficient overlap between visited states in different tasks.

- If the agent knows when there is a new task, continually learning reward and value models would be possible, possibly by using unique IDs for each task. Could you please discuss the potential advantages and drawbacks of continually learning reward and value models as well?

- Four sentences start with 'And'. I also see multiple instances of orphan words, i.e., single words left alone at the end of a paragraph.

- EWC is a nice continual learning baseline, yet I believe more recent approaches should be evaluated in the experiments. The related work mentions some toward the end of the related paragraph, yet they are not evaluated in the experiments.

- An ablation study over different prediction horizons for inference would help understand how well the world model adapts and how long it can last.

### Questions
- Is there a reason why ORSO couldn't address changing dynamics, too?

- During inference, does DRAGO use learned reward and value models associated with the test task while utilizing the most recent world model? For example, in Walker back2run, does DRAGO use the reward and value models it learned during training for Walker run and use the world model it obtained after Walker backward? Have you mentioned this anywhere in Section 3, as this indicates you need more than the world model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes two techniques to enhance the continual learning capability of the TDMPC MBRL agent: Synthetic Experience Rehearsal and Regaining Memories Through Exploration.

In Synthetic Experience Rehearsal, the authors propose to learn a separate generative model (via VAE) for the distribution of state-action pairs $(s, a)$, such that the synthetic pairs $(\hat{s}, \hat{a})$ can augment the prior tasks' data for re-training, mitigating forgetting of the dynamics model. To reduce forgetting of the generative model itself, the authors use the generative model at the end of the previous task to synthesize data and mix it with the current task's real data for training.

Regaining Memories Through Exploration uses an intrinsic reward defined by the accuracies of the current dynamics model and the previous one to encourage exploration. The hope is that the agent could explore pathways (in the state-action space) in the real environment that connect different tasks seen so far in order to build a cohesive understanding of the world.

The proposed method is tested on simulation environment tailored for a continual setting, and is shown to perform better than vanilla TDMPC (either re-training or continual-training) and a EWC TDMPC baseline.

### Strengths
1. The motivation is clear, with a nice illustration in Figures 1 and 2 showing the need for continual MBRL and the intuition of the proposed method.
2. The presentation of the method is easy to follow.
3. The empirical results look promising.

### Weaknesses
W1. System complexity. To enable continual MBRL, the authors propose two techniques, synthetic data and exploration. The former needs to build an additional generative model for the state-action pair, and the latter even requires training an extra reviewer (a full set of reward model, value model, and policy). But this is okay as long as during the continual learning process, the computation/memory does not grow with the number of tasks.

W2. Potential mode collapse. In eq5 part two, the dynamics model's training target (the next state) is labeled by the older version of itself, on synthetic data $(\hat{s}, \hat{a})$ sampled from the generative model. It is likely that such process would lead to mode collapse, especially when the real data $\mathcal{D}_i$ covers a very different region from the synthetic data, in which case little correction is possible.

W3. Unclear experimental setting & results. Taking MiniGrid in Figure 3 as an example, I expect the continual learning should start from room 1, and at some time the initial state distribution and reward function both switch to those of room 2 and then rooms 3 & 4. However, from the results in Figure 5, it is hard to tell when the task switching happens. Besides, there is no clear sign of forgetting in the results for the baselines (forgetting should result in a drop immediately after task switching), making the results confusing to me.

### Questions
Q1. Referring to W1, will you train a reviewer per task? Will the reviewers trained on prior tasks be discarded?

Q2. Regarding inference, eq8 requires a reward function and a value function for planning. Since the agent does not see the test tasks, I assume eq8 uses a known reward function to plan? Also, which value function did you use?

Q3. Section 5.1 introduces related work about MBRL, and concludes with "none of these methods investigate the continual learning setting for MBRL". However, at the end of section 5.2, the authors mentioned a few MBRL works for the continual setting. This is a bit contradicting, and perhaps the authors could reorganize to make it clearer.

Besides, to my knowledge, some related works are missing. For example, [1] learns the world model *online* for Dyna-style MBRL, which is closely related to yours, since both [1] and yours are trying to learn the world model while minimizing forgetting, such that it can benefit agent learning in the long run (without storing prior data). [2] also specifically studies forgetting in MBRL, and applies their method to a multi-task continual setting. Both the single-task online setting and the multi-task continual setting are reasonable to study the forgetting problem, hence [1,2] may be relevant to this work.

[1] Liu Z, Du C, Lee WS, Lin M. Locality Sensitive Sparse Encoding for Learning World Models Online. ICLR 2024.

[2] Huang Y, Xie K, Bharadhwaj H, Shkurti F. Continual model-based reinforcement learning with hypernetworks. ICRA 2021.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes DRAGO as a new method for continual model-based reinforcement learning. Unlike previous research, the author considers the continual reinforcement learning problem in which only the prior transition models are available instead of the collected data. To address the catastrophic forgetting problem occurring in this setting, DRAGO adopts two key components: synthetic experience rehearsal and regaining memories through exploration. A continual training strategy for the generative model and an intrinsic reward mechanism are introduced in the two components, respectively. The empirical results show that DRAGO outperforms the existing methods on several challenging continual learning benchmarks.

### Strengths
1. The paper is well organized and written, and the key idea is delivered clearly and easy to follow.
2. The problem setting in this paper is interesting and worth discussing, which has no access to the previously collected data. I didn't see many papers discussing this issue.
3. The experiments conducted in this paper are comprehensive and reproducible.

### Weaknesses
The motivations and analysis of the method could be explained further.  (see the questions)

### Questions
1. The continual learning for the generative model seems similar to some knowledge distillation tasks, but it's not included in the related works. I would appreciate it if the author could discuss it more and compare the similarities and differences.
2. At the beginning of each new task, the reward model, value model, and policy are all randomly initialized. I wonder if it's possible that similar methods could be used to utilize previously learned models/policies to facilitate the training, just like the generative model.
3. I'm not sure what's the main purpose of introducing another reviewer model. According to eq. (7), the calculation of intrinsic reward does not require an additional model. In such cases, what if the intrinsic reward is calculated and added directly to the total reward of the learner? I would appreciate it if the author could explain it more or provide experimental results using a single model.
4. The intrinsic reward defined in eq. (7) has a side effect that the agent will be penalized for visiting states that are less familiar to the previous model. Will it affect the final performance? If so, how did you solve that problem?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduced a new method for model-based reinforcement learning that mitigates the catastrophic forgetting problem for the world model. The authors operate in the unique setting where data from previous tasks cannot be carried over to the new task, which differs from some classic settings. The method involves using synthetic data replay and intrinsic reward to revisit previous areas to add to the training data of current task for the world model. Experiment results show superior performance compared to baseline methods.

### Strengths
- The method is intuitive and easy to understand
- The paper is well written and has good illustrations to enable clear understanding

### Weaknesses
 - I believe the baselines needs an additional one, Continual TDMPC+exploration. Since the DRAGO used intrinsic rewards, it would be fair to also add a strong intrinsic reward method like RND or curiosity, to see if classic exploration methods are enough for these settings and if the generative replay+your specific intrinsic reward design are superior and fitting for the problem setting
- (minor) Last two sentences in the conclusion are repeating
- The experiments domains are not very diverse, only 3 domains explored. For example, we are not sure how the method performs in POMDP settings like image observations
- Only TDMPC is used, would be useful to try other MBRL methods like dreamer to see the effects of the learning algorithm
- It is not entirely obvious that a better transition model translates to a better learner performance. How come your method is better compared to other? is it your policy during training has a better exploration or better world model equals better performance?

### Questions
- For the "dreamed" state action pairs are they from the generative model decoder where you sample $z$ to produce $(s, a)$, then you use the frozen old world model to produce $s'$?
- For the "reviewer" policy, whats the proportion of the time where each acts during online training/data collection? Is it half half? Do the baselines use the same number of steps for training/data collection as your learner steps+reviewer steps, to ensure fair comparisons?

### Soundness
3

### Presentation
3

### Contribution
2
