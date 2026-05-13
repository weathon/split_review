# Improving Intrinsic Exploration by Creating Stationary Objectives

- Decision: Accept
- Scores: 8, 5, 6, 5

## Abstract
Exploration bonuses in reinforcement learning guide long-horizon exploration by defining custom intrinsic objectives. Several exploration objectives like count-based bonuses, pseudo-counts, and state-entropy maximization are non-stationary and hence are difficult to optimize for the agent.  While this issue is generally known, it is usually omitted and solutions remain under-explored. The key contribution of our work lies in transforming the original non-stationary rewards into stationary rewards through an augmented state representation. For this purpose, we introduce the Stationary Objectives For Exploration (\methodName) framework. \methodName requires \textit{identifying} sufficient statistics for different exploration bonuses and finding an \textit{efficient} encoding of these statistics to use as input to a deep network. \methodName is based on proposing state augmentations that expand the state space but hold the promise of simplifying the optimization of the agent's objective. We show that SOFE improves the performance of several exploration objectives, including count-based bonuses, pseudo-counts, and state-entropy maximization. Moreover, SOFE outperforms prior methods that attempt to stabilize the optimization of intrinsic objectives. We demonstrate the efficacy of SOFE in hard-exploration problems, including sparse-reward tasks, pixel-based observations, 3D navigation, and procedurally generated environments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on a problem faced by approaches that use intrinsic rewards for guiding exploration; they introduce non-stationarity in the reinforcement learning objective. This non-stationarity in rewards can destabilize learning in many RL approaches. The non-stationarity arises because the agent cannot predict the intrinsic reward as the features required to predict it (such as visitation counts) are not observable.

Focussing on generalizations of count-based approaches, the paper proposes Stationary Objectives For Exploration (SOFE) that aim to augment the state space with sufficient statistics for intrinsic reward prediction to eliminate the partial observability and associated non-stationarity.

Experiments in sparse and no-reward navigation tasks show that including SOFE improves the performance of a previously proposed count-based intrinsic reward approach (E3B).

### Strengths
**S1.** Using count-based bonuses to explore sparse-reward environments is a widespread technique in RL. Improving the performance of count-based approaches would interest the research community.

**S2.** The paper focuses on a relatively under-explored issue of addressing the non-stationarity introduced due to count-based bonuses. The proposed solution of augmenting states with sufficient statistics for intrinsic rewards seems novel, simple, and well-motivated.

**S3.** The paper presents concepts clearly and is easy to follow.

### Weaknesses
 **W1.** The paper should adjust the claim that it identifies that intrinsic reward functions induce a non-stationary RL objective. While solutions may be under-explored, the issue is generally known and noted in previous papers (e.g., [1]). Specifically, the non-stationarity arises because the agent's policy changes, which in turn affects the visitation counts and thus the intrinsic reward. This creates a moving target for the agent, making the learning problem more difficult. Other works have chosen not to tackle the non-stationarity in intrinsic reward as it slowly varies and could be tracked [2]. Also, see the references in W2.

**W2.** A crucial weakness of the paper is that it misses comparisons with previous works that have proposed decoupling exploration and exploitation policies [3, 4] to tackle the non-stationarity introduced due to intrinsic bonuses. These methods explicitly separate the policy used for exploration from the policy used for exploitation, which can help to stabilize learning when using intrinsic rewards. The paper would significantly benefit from comparing their approach with baselines based on decoupling exploration and exploitation. For example, a comparison with an approach that uses a separate policy for exploration, trained on the intrinsic reward, and a separate policy for exploitation, trained on the extrinsic reward, would be highly relevant.

**W3.** An aspect that merits further discussion is that RL algorithms with recurrent architectures (like PPO + LSTM used in the paper) could learn representations that resolve this partial observability [5]. The LSTM's hidden state could potentially capture the history of visited states and thus implicitly track the visitation counts, mitigating the non-stationarity. One way to promote this effect could be to have an auxiliary task of predicting intrinsic rewards (which could make for an interesting baseline). This auxiliary task could be implemented by training an additional head on the LSTM to predict the intrinsic reward at each time step. While this might perform worse compared to directly providing sufficient statistics in the state (in terms of sample efficiency), it is potentially a more general solution to the problem for other intrinsic rewards. For instance, it has previously been shown that LSTMs can learn to count in discrete settings [6], which could be helpful in episodic exploration settings. Previous work has also shown that recurrent architectures can learn contexts that resolve non-stationarity due to partial observability in bandit problems [7].

### Questions
Q1. There still remains a source of non-stationarity for RL as the considered tasks have a maximum number of steps, but agents are not provided the time step in the state. In the episodic exploration setting $C_t$ can probably be used to infer the time step. However, it might make sense to include the time step in the global exploration setting. I am curious to know the authors’ thoughts regarding this and whether they have tried something along these lines.

Q2. Is there a reason why Figure 3 shows visitations with A2C as the base algorithm, but the evaluation in Figure 4 uses PPO? Would these qualitative results change with the base algorithm?

### Soundness
3 good

### Presentation
3 good

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
The paper claims that exploration bonus induces a non-stationary reward function, which causes instability in policy learning. The paper proposes to solve this instability by incorporating a sufficient statistic over the exploration bonus. The paper conducts experiments on 2D and 3D maze-like environments and demonstrates the proposed method can cover the state space more efficiently when compared to existing approaches.

### Strengths
- The idea is simple and intuitive---by augmenting the state space the method converts the non-stationary exploration bonus to stationary.
- The results on navigation tasks seem promising---in particular the policy appears to explore the maze more efficiently and recovers behaviour akin to a goal-conditioned policy when the goal state is set to unvisited

### Weaknesses
 
**Comments**
I am happy to increase my score after these points are addressed:
- The formulation in E3B doesn't really cover the action which is also important for count-based exploration for particular tasks (e.g. deterministic dynamics will be okay but not stochastic). Consequently, I don't think this is particularly a sufficient statistic but only for environments tested.
	- This also raises another question---why does the paper only focus on navigation tasks? There are many other difficult exploration tasks (e.g. Montezuma's Revenge on Atari, Minecraft, etc.)
	- The paper claims that it is a sufficient statistic and empirically demonstrated that it does perform well, but it will be great if there is a proof showing that this is true under some assumptions.
- In section 4, the paper indicates that "we consider that the only unobserved components in the POMDP are the parameters of the reward distribution." I am curious as to why this is a good assumption? In particular if $\phi_t$ is only a sufficient statistic for exploration bonus, it may not be a sufficient statistic for deriving the state $s_t$ (with observation $o_t$).
	- By adding $\phi_t$ to the state space, we are essentially exploding the state space (potentially to $\infty$.) from a finite state space (e.g. the maze example in experimentation.) What is the intuition that the algorithm is still able to tractably find a optimal policy?
	- In continuous state-action space, the counting mechanism depends on the quantization---how do we still ensure stationary reward in this case? I believe it will be non-stationary reward since we cannot differentiate two states within the same bin. Otherwise, we can just use global timestep as the count.



### Questions
- I find the paper confusing to read at times:
	- There is some mention of $\phi_t$ but in experimentation we only mention $N_t$ (i.e. count) and $C_t$ (i.e. elliptical bonus). Are they the $\phi_t$?
	- Under section 5.1, what is $N_0$? Is it a binary mask over the map in the maze with only the $j$'th cell is 0? Is the observation the "state"?
	- What is salesman reward and $\sqrt{}$-reward on figure 5? I believe it is Eq. 3 and 2 respectively

**Possible typos**
- Abstract, fourth last line: "holds" instead of "hold"
- Generally, "state visitation frequency" should be "state-visitation frequency"
- Page 3, first paragraph, fourth last line: "should not" instead of "shouldn't"
- Five lines after Eq. 1: $\forall s_t, a_t$ instead of $\forall_{a, s, t}$
- Page 4, second paragraph, line 1: "Eq. 2 and 3" instead of "2 and 3".

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies intrinsic motivation for RL. First, the authors notice that common intrinsic bonuses (count-based is considered as the illustrative instance) induce non-stationary objectives, which can make the learning process unstable. Then, they propose a solution to this problem by designing a method, called SOFE, to make the objective stationary through state augmentation. Finally, they empirically evaluate the proposed algorithm in a variety of domains, including 3D navigation and ProcGen tasks.

### Strengths
- (Originality) Although limitations of count-based bonuses for intrinsic exploration have been considered before, the algorithmic idea of augmenting the state representation to make the objective stationary is new to the best of my knowledge;
- (Significance) The experimental results look promising at least and experiments are carried out in some challenging and interesting domains, such as ProcGen Maze;
- (Clarity) The main ideas of the paper are presented with clarity, but most of the relevant implementation details are deferred to a very brief section in the supplementary (Appendix A.5).

### Weaknesses
 - (Motivation) The paper does not clarify that most of the reported considerations are valid when count-based bonuses are the actual learning objective rather than shaping of (sparse) external rewards. The former is arguably not the setting count-based methods have been designed for; specifically, count-based bonuses are often used to provide a dense reward signal in environments with sparse external rewards, and the paper does not adequately address this common use case. The focus on pure exploration with count-based bonuses as the sole objective seems somewhat artificial, given that these bonuses are typically used as a component of a larger reward structure.
- (Novelty and scope) Identifying the non-stationarity of the bonuses as a limitation of count-based methods does not look to be novel (e.g., Schafer et al., Decoupled reinforcement learning to stabilise intrinsically-motivated exploration, 2022) and the paper does not credit previous works on that; the paper needs to more clearly distinguish its contribution from prior work that has identified and addressed similar issues with non-stationary intrinsic rewards. The novelty of the state augmentation approach needs to be more clearly articulated in light of existing methods that also aim to stabilize learning with intrinsic rewards.
- (Robustness of the empirical evaluation) The experiments section does not specify how count-based bonuses are implemented. Several strategies exist, and they are known to make a significant difference in the resulting performance, which leaves one wondering how general the reported comparison really is. Moreover, the paper does not compare SOFE against alternative pure exploration methods aside from E3B, ICM, RND in Fig.7. The lack of comparisons to other pure exploration methods, particularly those that maximize state entropy, limits the scope of the empirical evaluation, and the paper should include a broader set of baselines to demonstrate the advantage of the proposed approach.

### Questions
1) Count-based bonuses have been largely employed for hard-exploration tasks, either in terms of regret minimization in theoretical papers or shaping of sparse rewards in empirical literature. From my perspective, count-based bonuses are not a great fit for pure exploration instead: They are not only non-stationary, as the authors noted, but also vanishing, and suffer from some other well-known issues (see Ecoffet et al., Go-Explore: A new approach for hard-exploration problems, 2021). However, only in the pure exploration setting the POMDP argument and optimality of history-based policies seem to make sense. If an external reward is there, it is a actually good to converge to a Markovian deterministic policy. Can the authors comment on why they think it is worth studying count-based methods for pure exploration?

2) To follow-up the previous question, count-based bonuses have been used in recent reward-free RL literature as well (e.g., Jin et al., Reward-free exploration for reinforcement learning, 2020). Also in the latter setting, the bonuses are freezed at the start of the episode, so that a Markovian policy optimizing a stationary objective is always deployed to collect data.

3) To address pure exploration settings, other stationary objectives have been designed, e.g., state entropy maximization. Can the authors relates their contributions with this stream of works:
- Hazan et al., Provably efficient maximum entropy exploration, 2019;
- Mutti et al., Task-agnostic exploration via policy gradient of a non-parametric state entropy estimate, 2021;
- Liu & Abbeel, Behavior from the void: Unsupervised active pre-training, 2021;
- Seo et al., State entropy maximization with random encoders for efficient exploration, 2021;
- Yarats et al., Reinforcement learning with prototypical representations, 2021;
- and many others.
Moreover, is state entropy maximization a meaningful baseline for the reported experimental evaluation?

4) While I am not particularly familiar with the literature of count-based methods, my feeling is that this kind of bonuses have been deeply studied. From a brief research, I am not sure the authors made a thorough due diligence of prior works, especially those addressing the limitations of count-based methods (e.g., Shafer et al., 2020 and Ecoffet et al., 2021 mentioned before). Interestingly, previous works also showed that $1/n$ bonuses bring faster learning in pure exploration settings (Menard et al., Fast active learning for pure exploration in reinforcement learning, 2021).

5) How are the pseudocounts implemented in the experiments? This seems to make a huge different. For instance, Bellemare et al. (2016), Ostrovski et al., Count-based exploration with neural density models (2017), Tang et al., (2017), Machado et al., Count-based exploration with the successor representation (2020) all make different design choices with varying results. Do the authors think their results are general for every implementation of count-based bonuses or for just one?

6) How many seeds are considered in the experiments and what is the meaning of the shaded areas? This crucial information seems to be missing for some of the results.

7) In the ProcGen Maze experiment, the paper comapres SOFE with E3B, ICM, RND. These does not seem to be the state of the art for procedurally generated tasks. Do the authors considered also tailored methods, such as (Ghosh et al., Why generalization in RL is difficult, 2021; Zisselman et al., Explore to generalize in zero-shot RL, 2023)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on count-based exploration (or its variants) in reinforcement learning problems. It investigates the issue that count-based bonuses make the reward function non-stationary. The authors propose to augment the state space with visitation count for states (or representative embeddings of states). Therefore, the reward function in count-based exploration becomes stationary and satisfies Markovian property (i.e. the reward is fully determined by the state in this and next step given the augmented state space).

The authors conduct extensive experiments on 3D navigation maps, and procedurally generated environments with high-dimensional observation space. The experiments combine the proposed approach with multiple count-based exploration algorithms, on both reward-free and sparse-reward RL problems. The empirical results validate that it is beneficial for exploration to include state visitation count as a component in state space.

### Strengths
The proposed method is straightforward and relatively easy to implement.
The proposed method is flexible enough to be combined with many existing count-based exploration approaches.
The method is simple and effective in improving the existing count-based exploration approaches, given extensive experimental results.

### Weaknesses
The technical contribution is not significant enough. It is straightforward to add state visitation count as state input. When it comes to high-dimensional observation space, the proposed method is fully built on E3B and relies on its encoding of the distribution of observed embeddings. So the technical contribution is incremental upon E3B. Is E3B the best approach to solve any hard-exploration problems with high-dimensional observation space? If not, could the proposed method be general enough to improve other exploration approaches for hard-exploration problems with high-dimensional observations?

The proposed method is specifically constrained to the count-based exploration approach. As for other exploration methods with intrinsic motivations, such as RND (random network distillation), the proposed method is not compatible with RND and cannot be used to improve the exploration result.

It has been mentioned several times that "we identify the matrix C_{t-1} as the sufficient statistics", but it is still vague to me. Where did you identify this? Could you provide any rigorous mathematical proof showing that C_{t-1} is a sufficient statistics for the count-based rewards?

In Section 3.2., the paper introduces the notation \phi_t without definition. For the context, I think it refers to sufficient statistics for count-based bonuses, but this point is very unclear in Section 3.2. Also, sufficient statistics in the problem setting are not defined.

In Equation 7, does s_t include sufficient statistics \phi_t or not? I think the state s_t means a fully observable state in the augmentation MDP \hat{M}, so s_t should already contain the information in \phi_t. Then it is weird to have the reward function and policy depending on both s_t and \phi_t in Equation 7.

The empirical results in Figure 4 look interesting. Could it successfully go to any goal position in the training map? If the exploration policy is trained on many different navigation maps. Could the policy be general enough to navigate to any goal position in unseen map?

### Questions
It has been mentioned several times that "we identify the matrix C_{t-1} as the sufficient statistics", but it is still vague to me. Where did you identify this? Could you provide any rigorous mathematical proof showing that C_{t-1} is a sufficient statistics for the count-based rewards?

In Section 3.2., the paper introduces the notation \phi_t without definition. For the context, I think it refers to sufficient statistics for count-based bonuses, but this point is very unclear in Section 3.2. Also, sufficient statistics in the problem setting are not defined. 

In Equation 7, does s_t include sufficient statistics \phi_t or not? I think the state s_t means a fully observable state in the augmentation MDP \hat{M}, so s_t should already contain the information in \phi_t. Then it is weird to have the reward function and policy depending on both s_t and \phi_t in Equation 7.

The empirical results in Figure 4 look interesting. Could it successfully go to any goal position in the training map? If the exploration policy is trained on many different navigation maps. Could the policy be general enough to navigate to any goal position in unseen map?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
