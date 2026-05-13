# CIM: Constrained Intrinsic Motivation for Reinforcement Learning

- Decision: Reject
- Scores: 6, 3, 8, 6

## Abstract
This paper investigates two fundamental problems that arise when utilizing Intrinsic Motivation (IM) for reinforcement learning in Reward-Free Pre-Training (RFPT) tasks and Exploration with Intrinsic Motivation (EIM) tasks: 1) how to design an effective intrinsic objective in RFPT tasks, and 2) how to reduce the bias introduced by the intrinsic objective in EIM tasks.
Existing IM methods suffer from static skills, limited state coverage, sample inefficiency in RFPT tasks, and suboptimality in EIM tasks.
To tackle these problems, we propose \emph{Constrained Intrinsic Motivation (CIM)} for RFPT and EIM tasks, respectively: 1) CIM for RFPT maximizes the lower bound of the conditional state entropy subject to an alignment constraint on the state encoder network for efficient dynamic and diverse skill discovery and state coverage maximization; 2) CIM for EIM leverages constrained policy optimization to adaptively adjust the coefficient of the intrinsic objective to mitigate the distraction from the intrinsic objective.
In various MuJoCo robotics environments, we empirically show that CIM for RFPT greatly surpasses fifteen IM methods for unsupervised skill discovery in terms of skill diversity, state coverage, and fine-tuning performance. Additionally, we showcase the effectiveness of CIM for EIM in redeeming intrinsic rewards when task rewards are exposed from the beginning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on two problems: reward-free exploration in RL and reducing the bias caused by intrinsic motivation. For the first problem, the proposed method CIM, solves a constrained maximization of a state entropy lower bound. The constraints encourage skill discovery and state coverage. Furthermore, CIM adaptively adjusts the intrinsic motivation strength to reduce the bias caused by the intrinsic reward. The proposed approach has a better sample efficiency on MuJuCo tasks.

### Strengths
- Empirically, CIM has a better sample efficiency and state coverage, especially in certain environments such as Ant.
- The proposed approach has significantly better skills discovery compared to prior methods. 
- The authors propose a scheduling technique that effectively reduces intrinsic motivation bias.

### Weaknesses
 - Novelty is limited; the algorithm mainly combines two algorithmic approaches in exploration: increasing state coverage and skill discovery.



### Questions
Comments: 

- I’m not sure the knowledge-based and data-based classification of methods in the introduction is entirely accurate. For example, the objective given in Zhang et al. 2021 can recover maximum entropy exploration technique in special case.
- $\tau_k$ is more like a hyperparameter to control the trade-off between exploration and exploitation and is not really a temperature parameter—those are usually used in the form $\exp(\tau x)$ such as in softmax outputs or Boltzmann exploration.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a constrained intrinsic motivation (CIM) for the exploration of Reinforcement Learning. The claimed advantage of CIM is that it reduces the bias introduced for exploration with intrinsic motivation (EIM). CIM combined the advantage of data-based IM and the mutual information based IM. The simulations on various robotic control environments demonstrate the advantage of the proposed methods in terms of skill diversity and sample efficiency.

### Strengths
I believe the proposed form of intrinsic motivation is novel and a good way to combine the benefits of max-entropy exploration and mutual information-based exploration that generally leads to a diverse skill set. 

The paper did comprehensive simulations studies with detailed comparisons between previous IM methods in the literature and illustrative visualizations that help the audience access the advantage of the proposed method.

### Weaknesses
The paper is hard to follow. Part of the reason is that there are too many abbreviations of previous approaches. I have to go back and forth to make sure I do not miss important information. I think the authors should replace them with in-text citation if possible. In general, I understand that good empirical results themselves can make a good paper. However, the use of notations and formulas should help to clarify the high-level idea and reduce the ambiguity. However, I found it hard to follow the notations and they are not self-contained in this paper and some formulas can be extremely confusing. I am listing a number of examples here.

1. We should not call Theorem 2 a theorem as it is a text-book level property in information theory, which should not considered as a contribution of the paper

2. (5), despite being the main contribution of the paper, is be very confusing. The constraint seems to be on the function $\phi$. However, the intrinsic objective does not depend on $\phi$. Should the constraint be on the learned skill $z$ such that there exists a representation of state that leads to good alignment. In such case, the constraint should be $\exists \phi, L_a(\phi(s), z) \leq c$, where $c$ is some constant. I think the definition of the CIM really has to be made clear as it is the main contribution of the paper.

3. Right above (10), the paper mentioned that the bound is tight when \phi(s) and z is well aligned. I don’t think this is correct. The function $g$ is already not invertible, so $H(g(s) \mid z)$ bound is never tight.

4. What is $k$ in the sentence “the intrinsic reward of CIM for RFPT is then ….”? 

5. In (11), I don’t see how this constraint optimization problem solve the issue of suboptimality. This basically ensures that the value of the online-policy is non-decreasing if we consider the approximation of $\hat R_{k}$ you mentioned in the following paragraph. This does not guarantee that the policy can always be optimized to the true optimal policy.

### Questions
1. Could the authors explain what it means by having bias for exploration, which occurs many times in Introduction? By bias, we typically mean that some estimator is inconsistent. It is not clear what it means by bias for exploration.
2. You mentioned that knowledge-based and data-based IM introduces non-negligible bias. Why doesn’t skill-based exploration introduce bias? In a EIM setting, it seems that all IM methods with non-decreasing temperature introduce bias.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new constrained intrinsic motivation (CIM) objective to both maximize state coverage and distill skills, which solves limitations of coverage-based IM (like RND, not learning skills) and MI-based IM (like DIAYN, discouraging state coverage). It is examined on reward-free pre-training tasks and exploration using intrinsic motivation tasks. CIM works better than most baselines regarding state coverage and skills learning on various mujoco tasks.

### Strengths
1. Very exhaustive related work, good summary and comparison among them. 
2. Baselines are exhaustive. Authors compared the proposed method with more than 10 baselines and outperform most of them, which is quite impressive.

### Weaknesses
Experiments performed for EIM tasks are a bit insufficient. Only on two environments, one directly trains using the proposed intrinsic reward while one trains a meta-controller on the top of learned skills. It would be more convincing to test on more environments.

In section 4.2, State Coverage paragraph, APT and CIC outperform CIM on two tasks, FetchPush and FetchSlide. Do you have any intuition as to why these two methods are particularly better in these two tasks?

### Questions
1. In section 4.2, State Coverage paragraph, APT and CIC outperform CIM on two tasks, FetchPush and FetchSlide. Do you have any intuition as to why these two methods are particularly better in these two tasks?
2. In Fig.3(a), in which task these discrete skills are learned? Also Ant or some other tasks?

Minior comments:
1. 5th line of page 2, “..., only maximizing MI only…”, one of “only”s should be removed?
2. S_T, s’, z from table 1 are not explained in the caption, although they are here and there in the paper, I do think it would be clearer to add them in the caption as well.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
As per the paper, there are two branches of intrinsic motivation RL (IMRL). 
RFPT: Here, one expects to learn the occupancy measure, hence exploration is necessary. 
EIM: Here, one wants to maximize the extrinsic objective, however, to do so agent also needs to explore (which is driven by intrinsic motivation). Hence the agent needs to balance the Intrinsic and extrinsic objectives with a $\tau$.  

The author introduces Constrained Intrinsic Motivation (CIM) for RFPT and EIM. For RFPT, CIM maximizes a lower bound of the state entropy with a constraint that aligns with skill. For EIM, they propose a way to choose $\tau$.

### Strengths
- The paper is easy to understand 
- Proposes a reward function that maximizes a lower bound of state entropy while aligning to skills
- CIM achieves good empirical performance

### Weaknesses
1. In the introduction, maybe focus early on
- the latent skill, why is it important 
- what is the bias and what are its implications, e.g. why is it bad?

2. The work primarily focuses on reward shaping which can be considered a heuristic development (e.g., eqn 7) upon the prior works. 
 However, the authors also tried to give intuitions defending their choices. I am unable to judge contribution/novelty here.

3. The presentation of theoretical results is not so sharp. Need to say about s,z,g. Is it true for any s,z, g? Are there some assumptions on g and what does "with equality" mean?

### Questions
On page 5, how are the last 4 lines related to eqn 10? I got a bit lost there.

What are typical latent skills? and how is policy conditioned on it? Is already apriori known which skills we want to learn?

There are quite some Macros, Maybe do images for e.g., with a Venn diagram to explain the relation of IMRL, RRFT, URLB, CIM, etc.

What is N in MI lower bound (above sec 3.1.2) 

Typos: Page 5 Walfe -> Wolfe, sec 4.3 dynamic is -> dynamics is, Lemma 1 and Theorem 2 extra bracket ).

Comment: The paper studies an interesting problem of maximizing mutual information. It is related to experiment design kind of objectives or more widely maximizing submodular functions under MDP constraints. These functions capture that visiting the same state will result in reduced rewards and hence naturally encourage exploration to gain higher rewards. The submodular functions can thus encode state coverage, entropy maximization, and Mutual information (D-design) kind of objectives. There are works on submodular reinforcement learning that might be interesting and related to the authors.
The work is also related to convex RL but I see two papers cited (Hazan & Mutti) in that direction so I believe the authors are aware of it.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
