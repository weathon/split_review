# Towards Imitation Learning to Branch for MIP: A Hybrid Reinforcement Learning based Sample Augmentation Approach

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Branch-and-bound (B\&B) has long been favored for tackling complex Mixed Integer Programming (MIP) problems, where the choice of branching strategy plays a pivotal role. Recently, Imitation Learning (IL)-based policies have emerged as potent alternatives to traditional rule-based approaches. However, it is nontrivial to acquire high-quality training samples, and IL often converges to suboptimal variable choices for branching, restricting the overall performance. In response to these challenges, we propose a novel hybrid online and offline reinforcement learning (RL) approach to enhance the branching policy by cost-effective training sample augmentation. In the online phase, we train an online RL agent to dynamically decide the sample generation processes, drawing from either the learning-based policy or the expert policy. The objective is to strike a balance between exploration and exploitation of the sample generation process. In the offline phase, a value function is trained to fit each decision's cumulative reward and filter the samples with high cumulative returns. This dual-purpose function not only reduces training complexity but also enhances the quality of the samples. To assess the efficacy of our data augmentation mechanism, we conduct comprehensive evaluations across a range of MIP problems. The results consistently show that it excels in making superior branching decisions compared to state-of-the-art learning-based models and the open-source solver SCIP. Notably, it even often outperforms Gurobi.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the use of imitation learning (IL) and Reinforcement Learning (RL) to tackle Mixed Integer Programming (MIP) problems. The main contribution of the paper is a framework that is specifically designed for MIP problems. Empirical results on a number of MIP problems show that the proposed method can achieve good performance with reduced model training time.

### Strengths
**originality**
- The paper's main novelty is a new framework that is designed to use IL and RL to tackle MIP problems. 

**quality**
- The overall presentation is good
- The paper discusses related works in a fairly clear manner

**clarity**
- Overall the paper is clear and easy to follow, however, the explanation on how the agent works can be improved

**significance**
- The paper studies how IL and RL can be applied to the MIP problems, which seems to be an important research direction
- The improved training time and better performance can be a significant result.

### Weaknesses
Discussion on the proposed method:
- I find the writing on how the proposed method works is a bit confusing, this might be partly due to the complexity of the problem. For example, what exactly actor critic method did you use in the online setting (for example, A type of SAC? DQN?)? And how exactly does the online RL agent decide whether to use the expert or to use the learned policy? (if for example, you say the action space is discrete, with 2 actions, one to choose the expert and the other to choose the learned policy for the online RL agent and it is a Q-learning type of agent, then it becomes much clearer) Currently I don't fully follow what is happening here. (also see questions)
- Another concern is the proposed method seems to only apply to only the MIP problems, and although the empirical results are interesting, it is a little unclear to me how much technical novelty is in the design of this framework and whether the contributions in this paper is significant enough.



### Questions
- How time consuming is strong branching compared to your method? Can you provide a wall-clock time comparison? 
- It is a bit unclear to me how exactly does the online agent decide whether to use the learned policy or expert policy? 
- Page 5, section 3.3, "batch DRL" is a general concept and is essentially the same as "offline DRL", which is initially discussed in some earlier papers (e.g. "Off-policy deep reinforcement learning without exploration" by Fujimoto et al.). The method in Chen et al., 2020 (Best Action Imitation Learning) is one of the imitation learning methods to tackle the batch/offline DRL problem. You might want to change the writing here to be more accurate. 
- What is the "ActorCritic" algorithm you are using? 
- Table 6 why there is no highlight on the best performing method for each task? Or the values are not related to performance?- Typically RL agents can take time to train, why is it the case that the proposed method, despite its complexity and a multi-stage/agent setup, can reduce training time compared to other methods?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a hybrid RL approach for variable selection in mixed integer programming (MIP). The proposed approach uses online RL to select between a rule-based expert and imitation learning based policy. The data collected from this online agent is filtered by a mechanism referred to as the offline agent and sent to a GCNN-based imitation-learning agent. This process repeats iteratively for a number of iterations. Results are presented on a number of integer programming problems and compared to an open-source and commercial solver with expert branching rules and two imitation learning methods. The proposed method outperforms the baselines on most domains and an ablation shows the importance of the proposed sub components.

### Strengths
Overall the results in the paper look strong. I do not have much experience with the MIP problem and cannot comment on the baselines but from the presentation they seem relevant and appropriate. From an RL and algorithmic perspective there are some additional ablations that could be interesting, but the presented ablations seem reasonable to me.

### Weaknesses
To me, the primary weakness in the current draft is the presentation. The ordering of the Tables in the Experiments section are confusing - tables are introduced and described in a non-sequential order and there are typos and odd sentences in the text that make the descriptions hard to follow at times. For example Table 3 and 4 show the Ablation results of comparing HRL-Aug to ML4CO-KIDA while the main results are presented later in Table 7 and 8. Just re-ordering the Table sequences would make it much easier to read.

I have a number of questions and clarifications relating to the algorithm which I will described under `Questions` but could also count as weaknesses. 

Apart from that there are a few typos and textual clarifications I will list below:

    1. Page 4 sentence 1: ‘Framework’ should be ‘framework’.
    2. Section 3.3: off-policy methods should be ‘offline methods’.
    3. Section 4.1: Dataset has `We’ appear in many places which should be `we’.
    4. Section 4.4 mentions: “We genuinely appreciate the collaborative effort of the reviewers and their invaluable role in shaping our work’. This is an awkward phrase that isn’t warranted before the review process? To me, it seems likely this is a vestige of a resubmission.

### Questions
My questions mostly relate to the RL part of the proposed approach.

1. What agent was used to train RL online? Was it a REINFORCE-like algorithm or something more complex? This may be important because the convergence guarantees of RL algorithms are often made in the discounted setting with \gamma < 1. It is also important to specify the precise algorithm used for reproducibility. 
2. I’m confused as to the ‘Offline RL’ agent. To me, offline RL implies learning a policy i.e. an action selection mechanism - using fixed trajectories of data that were generated by some behavior policy (or policies). In the paper, what is described is more of a filtration mechanism where effectively a function is fit to returns generated in the first iteration and then subsequently used to threshold the trajectories to sample. Could the authors clarify this point?
3. There are a number of choices made in the paper whose impact is not clear. For example, the filtration mechanism parameters are fit on the first iteration and kept constant after. Equation 4 uses a \lambda parameter to regularize the fit.The online agent is trained every 5 iterations (Freq). Some unspecified choice of `z’ defines how the trajectories are sub-sampled. It is not clear to me how important any of these choices are. Ideally the paper would include ablations on these but I can understand the difficulty of presenting so much information with a page limit. If the authors could indicate why these choices were made (with possible empirical evidence in the Appendix), I think it would make the paper stronger.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Update on November 20:

I raised my score to 6 based on the authors' responses. I am willing to keep discussing with the authors and the other reviewers to achieve a fully discussed final score.


---
This paper proposes a novel iterative collection and filtering framework to leverage a combination of online and offline RL techniques. Experiments show it consistently outperforms the previous SOTA approaches. Moreover, the authors claim that the proposed approach can be regard as a plugin orthogonal to peer methods.

### Strengths
1. The experiment is thorough. The authors provide very detailed empirical results to demonstrate the effect of the proposed approach.
2. Clear writing, the paper is clearly structured and easy to go through flow.
3. The proposed approach is technically sound. The employment of RL in this task is technically sound.

### Weaknesses
1. Concerns about the motivation. Personally, I am not convinced about the motivation to introducing RL in the branching task. As reported in some previous work [1,2], the number of expanding nodes of FSB is significantly less than that of SOTA ML approaches, indicating that *FSB is a good enough expert policy to imitate*. Instead, the bottleneck in this topic may mainly lie in the low IL accuracy. The lower accuracy may due to the unsatisfactory model structure or the insufficient information in the widely-used bipartite graph states (observations, more precisely). However, currently I found no definitive answer about that in recent researches. The ablation study in a recent research [3] gives clues that the historical information is effective as the process is a POMDP. Thus, based on these results, I think all researches that proposing more complex online RL framework is somewhat incremental, as improving the IL accuracy seems to be the key. Specifically, the paper does not sufficiently address why a more complex RL approach is needed when simpler imitation learning methods struggle to match the performance of strong branching itself, suggesting the core issue might not be the quality of the expert demonstrations but rather the learning process or input representation.
2. Concerns about the unnecessary complexity for introducing RL. Though usually higher asymptotic performance, many RL approaches are usually sensitive to the hyperparameters, making their application requiring much manual tunings. I am doing research in both RL and CO, empirically, I found their combinations can be fragile. In this paper, the online RL is mainly used for data collection. However, as far as I know, RL approaches are usually sensitive to the data distribution due to the deadly triad. For example, TD3 [4] may fail in MuJoCo tasks when the initial 20k random steps of data collection is turned off; BCQ [5] may fail when the offline data are collected with hybrid policies. Thus, in real-world CO tasks, I prefer use simple GNN+IL approach rather than other complex but fragile approaches, even if they claim higher performance in the four synthetic benchmarks. For this paper, I am concerned about the complexity for introducing RL. The paper does not provide sufficient justification for the added complexity of the RL framework, especially given the potential instability and sensitivity to hyperparameters that are often associated with RL methods. The benefits of using RL for data collection, rather than a simpler approach, are not clearly demonstrated, and the potential fragility of the combined RL and CO approach raises concerns about its practical applicability.
3. More explanations is required. In this paper, the RL based approach achieves lower IL accuracy while higher e2e performance. Thus, I am interested in what kind of multi-step information it learns from the input states. I believe this is more meaningful than simply reporting performance improvements, as it can guide us in designing better input features as mentioned in Point 1. If only the approach is given but the explanations is missed, then this paper is more like just a application of existing RL approaches to a new "Atari". The paper needs to provide a deeper analysis of why the RL-based approach, despite having lower imitation learning accuracy, achieves better end-to-end performance. Understanding the specific multi-step information captured by the RL agent is crucial for advancing the field and designing better input features, rather than just treating the problem as a black-box application of RL.
4. Limited improvement compared to ML4CO-KIDA. The performance of HRL-Aug reported in Table 7 seems to be marginal to ML4CO-KIDA.

### Questions
1. Is the online RL training necessary? Intuitively, using an offline-trained policy to collect data and then update the policy with the collected data iteratively seems to be enough. Why is the online updating of the policy during data collection necessary?
2. What is the dual bound change when a child node is infeasible? In SCIP, the solver add the objective and the current global primal bound to the constraints, making the infeasible child appears in high frequency. Thus, in the calculation of FSB scores, the score of infeasible child is set to a dynamic large value. How about that in this paper?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
