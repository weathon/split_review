# Unifying Diverse Decision-Making Scenarios with Learned Discrete Actions

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Designing effective action spaces for complex environments is a fundamental and challenging problem in reinforcement learning (RL). 
Although various action shaping and representation learning methods have been proposed to address some specific action spaces and decision-making requirements (e.g. action constraints), these methods often are typically customized to fixed scenarios and require extensive domain knowledge.
In this paper, we introduce a general framework that can apply any common RL algorithms to a class of discrete latent actions learned from data. This framework unifies a wide range of action spaces, including those with continuous, hybrid, or constrained actions.
Specifically, we propose a novel algorithm, General Action Discretization Model (GADM), that can adaptively discretize raw actions to construct unified and compact latent action spaces. 
Moreover, GADM also predicts confidence scores of different latent actions, which can help mitigate the instability of parallel optimization in online RL settings, and serve as an implicit contraint for offline RL cases.
Quantitative experiments and visualization results demonstrate that our proposed framework can match or outperform various approaches specifically designed for different environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes GADM, a method for learning discrete representations of action spaces. GADM applies to a variety of training settings and environment action spaces. GADM shows better results than methods that operate directly in the raw action space.

### Strengths
- GADM is a broadly applicable method, and the paper empirically demonstrates this. The paper shows strong GADM performance across different training settings (online and offline RL) and different environment action spaces (discrete, continuous, and hybrid). The paper compares GADM across these domains to a variety of baseline approaches. 
- GADM consistently outperforms various baselines across most of the considered settings. 
- Thorough experiments between the paper and supplementary.

### Weaknesses
 - *Insufficient Method Details*: The paper doesn't sufficiently describe the method. It's not until Page 6 that the paper discusses GADM in detail. Furthermore, this discussion omits many key details about GADM and only presents them in the supplementary. For example, the main paper doesn't discuss the latent confidence prediction. It also doesn't clearly refer to the section in the supplementary that contains this content (instead referring to "other design details are also listed in Appendix A.2"). Other important details not mentioned in Sec. 3 include: using focal loss, the weight initialization of the confidence predictor, random collection warmup, and EAR. The lack of detail in the main paper makes it difficult to understand the core mechanisms of GADM and how these components interact.
- *Insufficient Experimental Details*: Details about the online RL results in Sec 4.1.1 are not sufficiently described. No details about MPDQN and HPPO are described anywhere in the paper. It's therefore unclear if the experiment shows a fair comparison between GADM+DQN, MPDQN and HPPO. Furthermore, the main paper never mentions the 4 environments used in Fig. 5. While the supplementary contains these details, they are crucial to describe in the main paper. Especially the details concerning the environment action space since that is what the method is learning a representation of. Details about the offline RL results are likewise lacking in details, such as the specific datasets used for each environment and the evaluation protocols. The absence of these details makes it hard to reproduce the results and assess the validity of the experimental claims.
- *No Comparison to Action Representation Learning Methods*: As the authors stated in Sec. 5, there exists prior work that learns discrete representations of actions. For example, the paper states, "Dadashi et al. (2022) and Gu et al. (2022) propose to learn a set of plausible discrete actions from expert demonstrations to overcome the curse of dimensionality problem". Yet, as far as I can tell, GADM isn't compared to any other action representation learning methods. Instead, GADM is only compared to methods that operate directly in the raw action space. Without this comparison, I cannot assess the empirical benefit of the method over prior works. This is a critical omission, as it's unclear if GADM's performance gains are due to its specific action representation learning approach or simply due to the discretization of the action space.
- *Connection to Prior Work*: The connection to prior work is unclear. When referring to related work in learning action spaces, the paper states, "we argue that these algorithms can naturally be seen as a special case of our framework," but the paper doesn't explain why this is the case. The novelty of GADM and why prior works aren't applicable in the considered settings are unclear. The paper needs to clearly articulate the limitations of existing methods and how GADM overcomes these limitations, especially given the claim that GADM is a generalization of prior approaches. Without this, the reader cannot assess the true contribution of the work.
- *GADM Complexity*: I don't see how GADM enables "researchers to concentrate on only one of the topics" of action representation learning and RL since there are many details of GADM that are coupled with the RL process itself. GADM requires a pre-collected dataset to train the action model, strategies to mask the action space, action remapping, and handling extreme actions. All these added options affect the RL training. Furthermore, at the end of Sec. 1, the paper states the experiments demonstrate the "scalability" of the method, yet these added components seem to limit scalability. The paper needs to clarify how these components are decoupled from the RL process and how the method scales to more complex environments given these added complexities.
- GADM is described as an action representation model, yet ultimately, the encoder is learning a representation of action _and state_. GADM doesn't compare to the effect of learning the action representation conditioned on the state versus not using the state information. This is a crucial ablation that needs to be included to understand the importance of state-conditioning in GADM. Without it, it's unclear if the performance gains are due to the state-conditioned action representation or simply the action representation itself.
- $K$ is an important hyperparameter in GADM. How robust is GADM to the choice of $K$? Table 3 shows GADM performing better with a $K$ value of 4 vs. 8. How does performance vary across more values of $K$? The paper needs to include a more thorough hyperparameter study on the effect of $K$ on the performance of GADM. The current results are insufficient to understand the sensitivity of the method to this key parameter.

### Questions
- What is the novelty of GADM with respect to prior work? What are the limitations of prior work that prevent them from learning latent actions that can be applied to a variety of RL settings and environments? 
- Why not compare to Sampled MuZero in experimental settings from the original Sampled MuZero paper? Instead, the authors compare it in a new setting in D4RL, making it hard to verify the performance of Sampled MuZero. 
- Why does the latent action dimension greatly vary between environments? For Hopper in the offline RL environments, it is 4, yet for online RL experiments, it is 256. Why do some environments require 64x more embedding table dimensions?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to discretize any action space used in RL with a state conditioned VQ-VAE using a dataset of collected experience. The authors claim this as a general solution for any action space — discrete, continuous, or hybrid.

### Strengths
- Formulating a general framework for various kinds of action space is an important problem in RL.
- The idea of separating action representation learning and RL is widely applicable to online and offline RL.
- The papers demonstrates the learned discrete action space can be used with different RL algorithms — DQN and MuZero.

### Weaknesses
## 1. Writing
### 1A. Incomplete Placement of the paper in the context of Prior Work
- Action representations are learned and utilized in prior work in different ways, which are not discussed or addressed:
	+ [1] separate RL into learning action representations and then performing RL over the action representations.
	+ [3, 4] learn a latent space of discrete actions during policy training by using forward or inverse models.
	+ [2, 5] propose RL frameworks that can learn with evolving or changing action spaces, and are compatible with action representations.
	+ [6] use demonstration data to extract action representations
- Alternate ways of discretizing the action space should be compared against as baselines to the proposed VQ-VAE approach:
	+ [7-9] are various approaches to discretize the continuous action space — which makes these methods applicable to hybrid action spaces as well.
### 1B. Unsubstantiated / hand-wavy claims
- "But we argue that these algorithms can naturally be seen as a special case of our framework." - How are prior works in action representation learning a special case for the proposed framework? The assumptions made are different and the kinds of representation spaces learned are different.
- "which show its potential as a general design of decision-making foundation models" - How?

### 1C. Missing Important Details
- The baselines should be introduced in writing and talked about — how they are expected to be worse in comparison to the GADM.
- Most of appendix experiments are not referenced in the main paper, so hard to find out what's relevant or not.


## 2. Approach
### 2A. Complicated design Choices skipped or not justified.
- Many important components of the method are skipped in writing or not explained / justified properly, but then referred to in the experiments section:
	+ What does "diversity-aware codetable" mean? The paper mentions that the codebook is initialized with one-hot vectors or bisector point vectors, but doesn't explain why this is necessary or how it ensures diversity. The standard VQ-VAE codebook update is not discussed in the context of why it would fail in this setting.
	+ Why is the loss weighted by the reward function in Eq. 9? This is a myopic approach to loss weighting and would make long horizon credit assignment infeasible. Also, reward norm seems like a heuristic that won't necessarily work in all environments. For instance, in negative reward environments, norm(R(s,a)) would be higher for worse actions and the action model would ignore actions that give close to zero reward — which are actually better reward values. The paper does not discuss how the reward normalization is done, or if it's the same as the reward normalization used in the RL algorithm.
	+ Latent Action Confdience Predictor: How is this implemented and what is its purpose? The writing is very unclear. The paper does not specify the input and output of this predictor, the loss function used to train it, or how it is used in the RL algorithm.
	+ What is E.A.R. — it is never introduced in the approach?
	+ Warmup was never mentioned in the approach section. Anything that is important to make the method work should be discussed in the approach — for reproducibility.

## 3. Experiments
### 3A. Baselines
- For hybrid action space environments, a fairer baseline than HPPO is "Parameterized Action DDPG" because it is off-policy RL, whereas HPPO is on-policy. The paper should justify why HPPO is a good baseline, given that the proposed method is off-policy.
- No error bars in tables — important because the performance differences are miniscule.
- GADM+DQN should be compared against standard algorithms like SAC or TD3 on continuous action space environments. The paper mentions a comparison in the appendix, but it is not clearly referenced in the main paper.
- MuZero should be compared against on some discrete action task. The paper argues that MuZero is not applicable to discrete action spaces, but this is incorrect, as MuZero was originally designed for discrete action spaces. The paper should justify why it is not comparing against MuZero on a discrete task.
- A crucial comparison should be against continuous action representation learning instead of the discretization introduced by the VQ-VAE. This is also done in prior work listed above, so it's important to show why discretization is the right way to go.

### 3B. Environments
- Experiments on standard discrete and continuous online RL environments are missing. Only hybrid action space experiments are provided, while the paper claims: "learn unified and compact discrete latent actions for different environments that even correspond to continuous or hybrid action spaces." The paper should provide results on standard benchmark environments for continuous and discrete control.
- Appendix: "We evaluate on 4 environments", but I only see 1 (hopper-v3). Were the results on other tasks not promising? The paper should clarify which environments were used in the baseline experiments.
- Why inconsistent environments between baseline results (only hybrid action space environments) and ablations (HalfCheetah)? The paper should justify why different environments are used for the baseline and ablation experiments.

### 3C. Missing Ablations
- standard VQ-GVAE v/s diversity-aware codetable
- FiLM v/s no FiLM.
- Reward normalization v/s not

### 3D. Analysis Experiments
- Sensitivity to the codebook size?


Overall, looking at the experiment results shown, the two major concerns seem to be that the experiments might be cherry-picked to highlight the performant cases of GADM. Moreover, GADM seems to require a heavy amount of hyperparameter optimization, and it is not clear if when the baselines are provided with the same level of optimization, would they be generally better? If GADM is only meant to work with hybrid action space, that is fine, but then the paper should adjust its claims accordingly. A more thorough experimental evaluation is required to justify the proposed approach.

### Questions
- How is the extra predictor trained?
- Several questions raised above.

### Soundness
2 fair

### Presentation
1 poor

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
In this paper the authors present the General Action Discretization Model (GADM), a generic approach that is applicable to any RL task that can transform their action space into a compact set of discrete units. They separate RL tasks into two modules, i.e. action model and RL model, and advocate using a separately trained VQ-VAE inspired action model, which would discretize the action space, removing redundancies, and ultimately easing the job of the RL model. The authors evaluate GADM over several online and offline RL scenarios and report promising results.

### Strengths
- The idea of learning a discrete action space and framing this as a generic framework for any RL task is sound. 

- Paper was well written and easy to understand.

- The Background section was helpful to refresh and familiarize with the RL notation. However this can be moved to appendix and the reader could be referred to it. 

- The authors conduct and share experiment results on several online and offline benchmarks, helping the reader to gauge the effectiveness of GADM better.

### Weaknesses
 - Verbosity and the structure of the paper can improve. As is, we do not get to the actual proposed method until page 6 out of a 9 page paper. Furthermore, the appendix is longer than the paper itself (13 pages), and has some experiment results that'd be better suited for the main manuscript, such as visual samples of the learnt action samples from different scenarios. Also failure case analysis would have been nice to have.



### Questions
- Figure 3: It'd have been nice to have current trajectory and other collected trajectories rendered differently, as it is hard to differentiate between them. 

- Why the authors use the term "codetable" instead of "code book" which is the commonly accepted VQ-VAE terminology?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Introduce a general framework that can apply common RL algorithms to a learned discrete latent actions. The authors proposed GADM, which use a modified VQ-VAE to discretize raw actions into compact latent action and predict confidence scores to help stable policy learning

### Strengths
In general, I think the idea to learn to compress action representation is interesting. The experiments also show interesting results.

### Weaknesses
1. In Figure 1, the authors show that the actions are redundant in terms of transition function or Q function. However, in the proposed method, they propose to use a modified VQ-VAE to reconstruct the action condition on the state. I think there might be a gap between the story and the proposed method.

2. The writing is sometimes confusing. It might be helpful to include necessary information in the main paper.

3. In section 3.3 “diversity-aware code table”, the authors design a diversity-aware code table (“which is initialized by a series of one-hot vectors or bisection points and remains fixed through the entire training process”). As for one hot vectors and bisection points, how is the code table initialized? From the description, it seems that the only loss is Eq.9. Compare to VQ-VAE, do you fix the code book and cancel the code book learning loss as well as the commitment loss? What is $L_d$ in Eq.9?

4. In the paragraph “latent action confidence predictor”, what does it mean by “the action model prefers to select the latent action with more recent training samples”? Does recent samples here refers to more frequently seen samples? Can you further explain why it is similar to RND?

5. Currently, evaluation seems to be limited in relatively simple / periodically locomotion tasks. As for the scalability of the method, can GADM solve relatively complicated tasks (e.g., manipulation, locomotion with obstacles)?

6. For D4RL tasks, in quite interesting to see the locomotion tasks require such a small $K$ (e.g., K=4 for hopper). Can you further explain on this? It is interesting to see what will happen if you directly discretize the action or cluster the (s,a) pairs for such tasks. This can test what is the key of the method: the proposed action model or just reducing the action size.

### Questions
1. In section 3.3 “diversity-aware code table”, the authors design a diversity-aware code table (“which is initialized by a series of one-hot vectors or bisection points and remains fixed through the entire training process”). As for one hot vectors and bisection points, how is the code table initialized?

From the description, it seems that the only loss is Eq.9. Compare to VQ-VAE, do you fix the code book and cancel the code book learning loss as well as the commitment loss? What is $L_d$ in Eq.9?

2. In the paragraph “latent action confidence predictor”, what does it mean by “the action model prefers to select the latent action with more recent training samples”? Does recent samples here refers to more frequently seen samples? Can you further explain why it is similar to RND?

3. Currently, evaluation seems to be limited in relatively simple / periodically locomotion tasks. As for the scalability of the method, can GADM solve relatively complicated tasks (e.g., manipulation, locomotion with obstacles)?

4. For D4RL tasks, in quite interesting to see the locomotion tasks require such a small $K$ (e.g., K=4 for hopper). Can you further explain on this? It is interesting to see what will happen if you directly discretize the action or cluster the (s,a) pairs for such tasks. This can test what is the key of the method: the proposed action model or just reducing the action size.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
