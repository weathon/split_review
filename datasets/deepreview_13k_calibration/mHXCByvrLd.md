# Rethinking Optimal Transport in Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
We propose a novel algorithm for offline reinforcement learning using optimal transport. Typically, in offline reinforcement learning, the data is provided by various experts and some of them can be sub-optimal. To extract an efficient policy, it is necessary to \emph{stitch} the best behaviors from the dataset. To address this problem, we rethink offline reinforcement learning as an optimal transportation problem. And based on this, we present an algorithm that aims to find a policy that maps states to a \emph{partial} distribution of the best expert actions for each given state. We evaluate the performance of our algorithm on continuous control problems from the D4RL suite and demonstrate improvements over existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In offline reinforcement learning, optimal transport can be used to assess the distance between a certain policy and an expert policy. When using the Wasserstein distance, this leads to the W-BRAC algorithm from [Wu et al, 2022]. This paper overcomes some drawbacks of BRAC and related methods (choice of regularizing hyperparameter and Lipschitz constraints) by looking at offline RL as a saddle-point problem that arises from the dual form of the Kantorovich problem, and leveraging standard duality machinery. To avoid inefficient actions (stichting between “good” trajectories in the dataset), set inclusion constraints are replaced by inequality constraints, providing extremal transport in some cases. The proposed method, which appears to be sensitive to a regularizing hyperparameter, provides improvements over relevant baselines in the MuJoCo and Antmaze benchmarks.

### Strengths
- Novel formulation of offline RL using standard duality results and OT machinery.
- The empirical evaluation contains 9 Mujoco and 6 Antmaze environments against relevant benchmarks. Although performance improvements are not significant in some environments, the proposed method is almost consistently among the top 3. By comparing XMRL with BC and CQL alone, the impact of the proposed approach is disentangled from that of the techniques used to avoid overestimation bias.
- The paper is clearly written and, to the best of my knowledge, the related work is adequately described.

### Weaknesses
 - I do not see the relevance of proposition 3.1 (policy improvement), since it does not appear to give any insight about the method (the proposition is not cited/used anywhere in the paper) and the proof is basically the same as the one for classic policy iteration improvement.
- Evaluating the performance of the method in more challenging environments or tasks would enrich the experimental section. The impact of entropy regularization on the performance of the method is not assessed. 
- The method seems considerably sensitive to the parameter w (as seen in appendix 2), so one of the drawbacks of W-BRAC is still present in this method.
- Typos: “Fol all experiments” section 4.2.

### Questions
-

### Soundness
2 fair

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
The key idea of the paper is to compute the optimal transport between states and actions with an action-value cost function. This provides a new way to balance the two tasks in offline RL: policy improvement and distribution shift avoidance. Based on this idea, the authors propose a new algorithm called Extremal Monge Reinforcement Learning and have shown that the new algorithm outperforms BC and previous offline RLs.

### Strengths
1. The idea of thinking of an offline RL problem as an Optimal Transport (OT) problem is interesting. Especially considering that the Extremal Optimal Transport (ET) can be used for policy improvement.
2. The experimental results are sufficient and promising.

### Weaknesses
1. This contribution of the paper is insignificant, as it is barely a direct application of  Extremal Optimal Transport [1], without providing a new understanding of offline RL or solving/alleviating existing problems in offline RL.
2. The idea is not convincing. It is hard to see why we should consider an offline RL task an OT problem. Why do we want to preserve the distribution of $\mathcal{A}$ instead of considering the distribution $\mathcal{A}(s)$ or support $Supp(\mathcal{A}(s))$ independently for each state? According to my understanding, offline RL considers the distribution $\mathcal{A}(s)$ instead of the distribution of $\mathcal{A}$, as shown in W-BRAC (eq. 8).
3. XMLR does not seem better than W-BRAC. As stated in 2, the theoretical foundation of XMLR is not convincing. Furthermore, in practice, XMLR faces the same problems as W-BRAC. 1) both of them train an additional discriminator $f$. 2) both have a hyper-parameter to control the extreme of the policy, which is difficult to choose. 
4. The experimental results are not surprising. According to Table 2, the results of XMRL are close to the results of ReBRAC.
5. The Writing should be improved. Typos, e.g., in the first line in section 2.4, should be fixed.

### Questions
1. What is the benefit of formulating an offline RL problem as an OT problem?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel offline RL algorithm that comes from the popular optimal transport methods. Experiment results on Meta-World show that it achieves SOTA performance on various tasks.

### Strengths
Offline RL is recently a heated topic, and the authors propose a novel offline RL algorithm that has strong theoretical support. The idea of using optimal transport as policy regularization is novel and interesting. Experiment results are quite strong.

### Weaknesses
I am not quite familiar with optimal transport, so actually I did not fully check the methods. One possible weakness is that XMRL introduces an additional component $f$, which introduces additional learning complexity, especially in complex tasks.

### Questions
1. $f$ seems to be learned in an adversarial training manner. Is there any connection between XMRL and ATAC [1], an offline algorithm that also uses adversarial training?
2. How much additional computation complexity does XMRL introduce? The authors discuss about absolute training time, but how much more time does XMRL take compared to methods like IQL or CQL?
3. It seems that the larger $w$ is, the higher the performance. Can the authors further discuss the impact of $w$ on performance?


[1] Cheng, Ching-An, et al. "Adversarially trained actor critic for offline reinforcement learning." International Conference on Machine Learning. PMLR, 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
