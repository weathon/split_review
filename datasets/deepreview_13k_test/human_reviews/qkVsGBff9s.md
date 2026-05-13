# Q-Supervised Contrastive Representation: A State Decoupling Framework for Safe Offline Reinforcement Learning

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Safe offline reinforcement learning (RL), which aims to learn the safety-guaranteed policy without risky online interaction with environments, has attracted growing recent attention for safety-critical scenarios. However, existing approaches encounter out-of-distribution problems during the testing phase, which can result in potentially unsafe outcomes. This issue arises due to the infinite possible combinations of reward-related and cost-related states. In this work, we propose *State Decoupling with Q-supervised Contrastive representation* (SDQC), a novel framework that decouples the global observations into reward- and cost-related representations for decision-making, thereby improving the generalization capability for unfamiliar global observations.
Compared with the classical representation learning methods, which typically require model-based estimation (e.g., bisimulation), we theoretically prove that our Q-supervised method generates a coarser representation while preserving the optimal policy, resulting in improved generalization performance. Experiments on DSRL benchmark problems provide compelling evidence that SDQC surpasses other baseline algorithms, especially for its exceptional ability to achieve almost zero violations in more than half of the tasks, 
while the state-of-the-art algorithm can only achieve the same level of success in a quarter of the tasks. Further, we demonstrate that SDQC possesses superior generalization ability when confronted with unseen environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel method to solve offline safe reinforcement learning problems by introducing representations to **distinguish reward-related and cost-related states by contrastive learning**. It leverages **three different policies to handle different conditions** (safe, unsafe, borderline safe). The paper's main motivation is to achieve a rough state representation while promising the optimal Q-value. Furthermore, it demonstrates that their method is better than prior work like bisimulation. After getting the representation, it aims to learn the reward Q-value and cost Q-value so it can extract the policy by following FISOR [1]. In the experiments, it illustrates that the method has good performance and can be generalized to complex tasks. However, this method struggles with the complexity of hyperparameter selection, network structure, and algorithm steps.

It seems to be a novel and strong method. But when carefully examined, there are some **fatal issues** in the method and the experimental results may be **overclaimed**. In addition, it lacks some important ablation experiments.

References:

[1] Yinan Zheng, Jianxiong Li, Dongjie Yu, Yujie Yang, Shengbo Eben Li, Xianyuan Zhan, and Jingjing Liu. Safe offline reinforcement learning with feasibility-guided diffusion model. arXiv preprint arXiv:2401.10700, 2024.

### Strengths
- The paper is well-written. It explains the method step by step and also provides a comprehensive and detailed introduction to the experiment. The figures in the text are clearly expressed and easy to follow.
- The method is novel since no prior work uses contrastive learning to solve vector-based safe RL problems. 
- It provided detailed proof about why the method is more efficient than bisimulation. It is a theoretical guarantee.
- The main experiments and experiments about contrastive learning are sufficient. Meanwhile, it provides some details about the tasks and hyperparameters.

### Weaknesses
- The contributions are not claimed in the introduction. Since the method has borrowed a lot from FISOR, it should emphasize its improvements.
- The lack of pseudocode algorithms in the methods section, even in the appendix, hinders understanding. Due to the algorithm's complexity ("the necessity of executing three distinct training phases"), authors need to provide pseudocode to make their method more clear.
- This method needs to be optimized jointly for learning Q-values and the representations (Section 3.3). However, It did not clearly explain the convergence of doing so. Obviously, the learning process of representations uses optimal Q-values as distance measurements. It is not realistic in the training phase since the Q-value should be initialized at the beginning. Plus, the learning of Q-values involves embedding representation vectors. Inaccurate representation can affect the optimization of Q-values. This is like whether the chicken or the egg came first. It is unlikely to get the optimal Q-values or representations if optimizing them together. I think this is an **essential issue** of the algorithm.
- The learning processes of $V^{low}_h$ and $V^{up}_h$ are unreasonable. I suspect authors misunderstand the function of expectile regression. And I can't understand the term "reverse expectile regression" (why is it called that). Expectile regression is proposed in IQL. IQL leverages the advantages of expectile regression to improve the learning of value functions by changing the weights of different items. It demonstrates that IQL can achieve the best performance when $\tau=0.9$. This indicates that the value function estimation can be relatively accurate in the offline setting. However, in this paper, the method uses expectile regression to learn the upper-bound and lower-bound of cost value functions. This usage is incomprehensible. Furthermore, even if it can learn the upper-bound and lower-bound of cost value functions, the formulations can not make sense. $L^{\tau}(Q-V) = |\tau - 1(Q-V<0)|(Q-V)^2$ (expectile regression) indicates that when $\tau \in (0.5,1)$, the weights before $Q-V>0$ are larger than the weights before $Q-V<0$. Thus, it only can show the value function involving $Q>V$ will be considered more rather than learning an upper-bound value function. Meanwhile, defining a "reverse expected regression" is quite strange and I understand that it should be equivalent to constraining the $\tau$ of the expected regression to $(0,0.5)$.
- The generalization experiment only generalized on the number of obstacles, which needs to be emphasized. Since traditional generalization includes task generalization and scene generalization, involving unseen objects, it is important to explain the experiments here only generalize to tasks with more obstacles (it is obviously a state-based method can not deal with unseen objects). Otherwise, it would be an overclaim.
- The ablation experiments are not sufficient. One of the method's main contributions is the new state-decoupling framework, which contains three conditions. It should be compared with only two conditions in the ablation.
- One of my biggest regrets is that I cannot see any visual analysis in the paper on how to divide state-related and cost-related states, which is a core contribution of the method.
- The method involves many hyperparameters. I suspect its performances are because of parameter tuning and Appendix C, Appendix D demonstrate that. Additionally, the ablations of contrastive term coef are not presenting.

### Questions
My questions are mostly based on the weakness:

**Main concerns**:
1. Please explain the convergence of joint optimation. How can it learn optimal Q-value and representation if the initialization is random?
2. Why using expectile regression can learn the upper-bound and lower-bound of the value function? What's your motivation? Is this reasonable?

**Other questions**:

3. If it cannot provide generalization at the level of obstacle types or tasks, why can it simply say that this method has generalization ability?
4. How about the state-decoupling framework's ablation?
5. In Table 4, what does it mean "Task: All/Vel"?

**Writing**:

6. In line 1229, there is a repetition of "Zhang".

My initial recommendation is 'reject' because of my main concerns. If the authors can explain them clearly and convince me, I will raise my score.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a collection of algorithms for reducing the impact of OOD samples on constraint satisfaction when using RL to solve constrained MDPs. The main hypothesis seems to be that learning independent latent representations for state-conditioned value and state-conditioned cost, and then selectively conditioning several different policies on these representations, may help decoupling cost-related and reward-related concepts within the networks parameterizing the policies and thus lead to more robust decision making with respect to cost.

### Strengths
This paper presents an interesting approach that, although does not contain much novelty for each individual aspect, does as whole seem relatively new.

The paper addresses an important topic in RL and has some relevance to representation learning.

The paper demonstrates impressive experimental results.

The large amount of math notation is handled well and I did not find it confusing.

### Weaknesses
This paper has no major weaknesses in my opinion. Below I offer some smaller suggestions.

The biggest weakness in my opinion is that, with a very complicated method like the one the authors present, it is difficult as a reader to follow all the moving parts. I understand there is limited space, and thus many details must be omitted or relegated to the appendix, but I offer two concrete suggestions.

1) Provide a diagram, pseudocode/algorithm block, or add some text within the writing that transitions the reader from one part to another while providing some context. At a certain point I felt like I was reading a long list of individual method descriptions without really understanding how they fit together.

2) There are many, many steps to the proposed system. Almost none of them can be derived from first principles. Thus, they all need some form of justification. Often, AI/ML researchers just assert that their method makes some intuitive sense. That is sometimes sufficient, but it is much more convincing when the authors provide a list of properties they desire or a list of alternatives followed by some reasons why they think those alternatives would not work as well. This will also help the reader understand *why* each step is being taken, rather than simply that it has been taken.

Given the extreme complexity and many moving parts of the proposed approach, as well as how the paper is written, I am skeptical about its scientific value. Engineering-wise it is a very impressive system and stands as a good example of what kind of performance we might hope to achieve on some of these RL benchmarks. However, it is very difficult to be certain that we have learned something general (about representation learning, reward/cost decoupling, etc.) from this paper. Every time a new module is added it becomes exponentially more difficult to conduct or design the experiments necessary to rule out its confounding effect on whatever dependent variable we are interested in measuring, and conference papers generally do not contain enough space for such experiments.

Miscellaneous:

“such as industrial management, autonomous driving, and robot control” Is autonomous driving not a subset of robot control?

“(the set of the probability distribution over \mathcal{X} is denoted as \Delta (\mathcal{X}))” I don’t see \mathcal{X} defined before this… Maybe this is meant to be states \mathcal{S}? That would make the most sense.

“predefined cost limits” --> predefined cost limit

Try to avoid using citations as nouns e.g. "The most relevant works to ours are (Bellemare et al., 2019; Le Lan et al.,
2021), which learn representations via Bellman value functions." You could instead say something like "The most ... are from Bellemare et al. (2019) and Le Lan et al. (2021), who ..."

### Questions
- “(with \eta representing the temperature factor)” How to set \eta?
- “where \nu is a temperature parameter” How to set \nu?
- I don’t see how temperatures are set anywhere, though I do see some values in the appendix. Does this complicate hyperparameter tuning? I know that many algorithms are very sensitive to temperature settings. Is that the case for SDQC as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a contrastive learning framework for safe offline RL problems. It decouples states into reward-related and cost-related representations based on a reward-related Q network and a cost-related Q network. The Q networks are used as the supervision signal in the contrastive learning of the state representations. As a result, the learned representation clusters states with similar reward or cost Q-values, enhancing generalization in OOD environments. The framework also learns three policies and switches between the policies based on the safety assessments for each state. Experimental results show that SDQC provides a robust solution for safe RL across multiple offline safe RL tasks and also shows generalization in unseen environments.

### Strengths
* Originality: SDQC’s approach of decoupling reward and cost representations through contrastive learning is a unique solution in offline safe RL.  
* Quality: The paper has a theoretical comparison with bisimulation, and an emprical comparison with existing offline safe RL baselines.  
* Clarity: The paper clearly explains the motivation and the method.
* Significance: SDQC’s approach could learn policy to generalize to OOD scenarios better than existing methods. It has a meaningful impact on offline safe RL.

### Weaknesses
* The comparison with bisimulation seems redundant and unfocused. While SDQC claims theoretical advantages over bisimulation methods, no empirical comparisons with bisimulation techniques are provided. If there are no such methods in safe offline RL, why adding this comparison?
* The framework learns two types of state representations and trains three separate policies, which may add considerable computational overhead compared to most single-policy baselines.
* None of the baselines in the paper incorporate explicit representation learning as in SDQC. This difference may give SDQC a structural advantage in terms of performance, though at a higher computational cost.

### Questions
* Q1: How does SDQC’s computational and sampling cost compare to baseline models that do not include representation learning? Does the contrastive learning component require sampling and evaluating Q-values over large numbers of state pairs? Although the ablation study shows that contrastive learning is essential for the algorithm, how do the parameters in the contrastive loss affect the results?
* Q2: Given the theoretical comparison with bisimulation, would a bisimulation-inspired method indeed underperform relative to the proposed method in safe offline RL? Could the authors provide an empirical comparison using the same offline safe RL datasets featured in the experimental section?
* Q3: How does SDQC manage high-dimensional or complex state spaces, such as visual input, where the demands of contrastive learning may increase the challenge of representation learning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces State Decoupling with Q-supervised Contrastive representation (SDQC), a framework that decouples observations into reward-related and cost-related representations to improve generalization and address out-of-distribution issues. The proposed framework is evaluated on the DSRL benchmarks. The results point to a better capacity of SDQC in learning safe and generalizable policies compared with existing approaches.

### Strengths
This paper theoretically proves that SDQC generates a coarser representation than bisimulation-based methods while maintaining the optimal policy, evidenced by achieving higher information entropy of the global observations when conditioned on the representations.

### Weaknesses
1. The proposed method does not seem to be particularly elaborate or innovative, as it mainly makes use of known results/techniques. 
2. The evaluation results are not convincing, and certain comparisons of model-based methods are absent.

### Questions
1. In Section 3.2, the authors state that the representation and Q-values are learned and updated jointly (lines 243-244). How could this result in optimal policies and good representations? One could imagine that the Q-values during training are not yet optimal, and using these estimated Q-values to compute $d(s, \tilde{s})$ could introduce significant estimation errors for representation learning and then potentially lead to inaccurate Q-value estimations. 
2. Why are the trade-off policy $\pi_{to}$ and the upper-bound cost-related value function $V_{h}^{up}$ necessary? In Section 3.3, the authors adopt a similar approach to Zheng et al. (2024) for updating Q-values and policies, differing primarily by replacing $s$ with $z_{\theta}(s)$ and introducing $V_{h}^{up}$ and $\pi_{to}$. However, Zheng et al. (2024) demonstrate that optimal policies can be achieved without $V_{h}^{up}$ and $\pi_{to}$ when excluding representations. The authors assert that their representation method does not alter the optimal policy (lines 333-334). It seems possible that integrating the representation method directly into Zheng et al. (2024)'s approach could still yield optimal policies. Could the authors clarify the rationale behind introducing $V_{h}^{up}$ and $\pi_{to}$?
3. In Section 3.4, while the authors provide theoretical proof that their representation method outperforms bisimulation, empirical comparisons with methods that use bisimulation are absent. Could the authors provide additional evaluation results comparing their method with bisimulation-based approaches for a thorough evaluation?
4. The evaluation metrics (lines 356-359) are unclear. While the authors highlight zero-constraint violation in Section 4, they use a non-zero cost threshold for evaluation. Why do the authors emphasize 'zero-constraint violation' when the cost threshold is not set to zero? If my understanding is correct, the evaluation should focus on comparing rewards among safe agents with normalized costs below 1, as per the DSRL benchmark. Additionally, SDQC seems to achieve safety through over-conservatism, as indicated by the low rewards (less than 0.2 in CarButton, PointButton, PointPush, and SwimmerVel tasks). Could the authors clarify the reason for these low rewards and provide the actual reward results of all tasks for better insight?

Besides, please ensure that proper citations are included where necessary.

### Soundness
2

### Presentation
2

### Contribution
2
