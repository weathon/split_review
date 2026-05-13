# Blending Imitation and Reinforcement Learning for Robust Policy Improvement

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
While reinforcement learning~(RL) has shown promising performance, its sample complexity continues to be a substantial hurdle, restricting its broader application across a variety of domains. 
Imitation learning~(IL) utilizes oracles to improve sample efficiency, yet it is often constrained by the quality of the oracles deployed. 
which actively interleaves between IL and RL based on an online estimate of their performance. 
\algname draws on the strengths of IL, using oracle queries to facilitate exploration---an aspect that is notably challenging in sparse-reward RL---particularly during the early stages of learning. As learning unfolds, \algname gradually transitions to 
RL, effectively treating the learned policy as an improved oracle. %
This algorithm is capable of learning from and improving upon a diverse set of %
black-box oracles. %
Integral to \algname are Robust Active Policy Selection~(RAPS) and Robust Policy Gradient~(RPG), both of which reason over whether to perform state-wise imitation from the oracles or learn from its own value function %
when the learner's performance surpasses that of the oracles in a specific state. 
Empirical evaluations and theoretical analysis validate that \algname excels in comparison to existing state-of-the-art methodologies, demonstrating superior performance across various benchmark domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a new policy gradient algorithm named Robust Policy Improvement (RPI), which learns policies through IL and RL. They propose the Robust Active Policy Selection (RAPS) to improve value function efficiently and then use the Robust Policy Gradient (RPG) to update policies, which is a variant of the actor-critic method. In addition to some theoretical proof of the optimality of the method, some experiments show that RPI outperforms other baselines to a degree.

### Strengths
1. Paper writing is clear to understand. And the method is natural.
2. The theoretical analysis is adequate.

### Weaknesses
 (1) Novelty.
- The policy improvement of perfect knowledge is similar to making ensembles of several imitated policies. The theoretical analysis of the method seems a little redundant. 
- The exploration in RPI is uniformly random sampling (line 3 of Alg.1).
These seem trivial.

(2) The experimental setting is not clear and sufficient.
- How many demonstrates for imitation learning? How many online interactions for reinforcement learning? The x-axis of the curves is training step, what is 100 training step means? And do the baselines use the same examples and online interactions?
- The selected tasks are easy. In meta-world, as I know, button-press and window-close are not hard. What about bin-picking and door-open? In DMC, what about hopper or even humanoid?
- Lack of baselines. Except for MAPS, all the baselines are from before 2020. I think there are more works than listed.

### Questions
As listed in weakness.

By the way, why are the links in the paper invalid? (such as citation and equations)

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
This paper investigates the setting of learning from multiple oracles that can also be framed as an imitation learning setting. The work proposes a novel procedure for combining learning from oracles with active exploration using a framework called robust active policy selection in combination with a robust policy gradient. The method interoperates between imitation learning and reinforcement learning and smoothly transitions between the two. A theoretical introduction of the presented method is followed by empirical evaluations that show improved performance over several baselines.

### Strengths
Motivation
* The work is well-motivated as an approach to learn from multiple oracles and improve upon them. Building frameworks that can blend between existing knowledge via oracles and exploration using a learners policy seems like a good way to enhance the setting of only learning from oracles.

Structural clarity
* The paper is well structured and well written. The flow is very clear. I do have to say that I did get lost in the notation details at times because there is a lot of notation that is quite similar. The switch from theoretical analysis to empirical investigation is handled nicely in the text.

Mathematical rigor
* The work uses strict mathematical definitions and states its assumptions clearly. The proof for proposition 4.5 is intuitive. I did not carefully check the proof of proposition 5.1 in the Appendix. However, it seems reasonable that an online no-regret learning algorithm would obtain high value.

Novelty
* The work provides a sufficiently novel version of an existing algorithm that enables a mixture of online and offline optimization. Some of the novelty might be slightly exaggerated though and could be made more clear, see Weakness: Contextualization with prior work).

Experimental evaluation
* The experiments consider a sufficient number of environments and baselines and all evaluation is done over a reasonable number of random seeds. Ablations give insight into the behavior of the algorithm and provide intuition that the algorithm works as intended.

### Weaknesses
Contextualization with prior work
Before I start, I would like to mention that I am not familiar with this sub-field of RL but do know the standard online and offline RL literature quite well.
* The prior work section is rather brief with a total of 6 citations. I am not familiar with the exact sub-field but this seems rather little given the literature is several years old.
* My first main concern is related to the contextualization of various parts of the paper to previous work. I think it could be made clearer which parts are inspired by previous work. For instance, the ideas of UCB value selection and multi-step advantage over several value functions seem already present in previous work but this is not immediately apparent from the current manuscript. I understand that the present manuscript defines these things with the inclusion of an additional learner policy, which requires the development of novel machinery. However, I think it would be good to give credit to the general formulations in previous work where appropriate.

Experimental evaluation
* My second main concern is the following. The experimental setting seems very similar to that studied in Liu et al., since environments and baselines are relatively similar. However, it seems that the performance of the reported baselines in this paper differs significantly from the performance reported in the previous study of MAPS. Both MAPS and MAMBA seem to be unable to even achieve performance close to the best oracle while in the MAPS paper both algorithms perform significantly better on the tasks that seem to be identical to the ones chosen here. See Q6.

Textual clarity suggestions
* This might be a me thing but the term robust policy gradient has been used several times in the literature before. It might make sense to consider a less generic name for the algorithm. Examples:

Xuezhou Zhang et al. Robust Policy Gradient against Strong Data Corruption. ICML 2021.
Yue Wang and Shaofeng Zou. Policy Gradient Method For Robust Reinforcement Learning. ICML 2022.

* I’m being a little nitpicky here but the policy gradient theorem with baseline is definitely older than 2015 (P6 section 6.2). It might be good to cite relevant prior work here.
* Some of the notation can be quite confusing and I lost track of what index refers to which object several times. This is mostly because lot’s of variables are indexed by multiple things but all objects are somewhat similar. I don’t really have a good suggestion on how to fix this though other than reducing the size of separate, less relevant sections.

Overall, I do think that the community will benefit from the publication of this work. I am inclined to raise my score if my two main concerns can be addressed.

### Questions
Q1. What is the relationship between the studied setting and offline RL? Offline RL, similar to the studied setting, tries to blend behavioral cloning with value function learning. In that sense, is any offline RL algorithm a candidate for learning from multiple experts? I’m not claiming that offline RL needs to be added in prior work if it turns out to be unfitting but it would be great if the authors could elaborate on this point.

Q2. Does the max-following policy execute a mixture over policies or does it, given a state, fix a policy and then execute this policy throughout time? This sentence is slightly confusing me here: “Specifically, if all oracles perform worse than the learner policy at a given state, the max-following policy will still naively imitate the best (but poor) oracle.” If the former is true, then it would be better or equal to the best poor oracle.

Q3. I’m confused about Line 5 of the algorithm. $D^k$ contains data from possibly two different policies, however it is used to update a single value function. Is this a typo or am I misunderstanding the algorithm here? I would think this should only be taking the second portion of the roll-out data, not the roll-in data. Could you elaborate why this is okay to do?

Q4. In the policy selection step, the text states “Using LCB for the learner encourages exploration unless we are very sure that the learner surpasses all oracles for the given state”. What exactly does the term exploration refer to here? Is this just meant as exploration for the learner’s policy?

Q5. To clarify that I am understanding this correctly. In Eq 14, the gradient is computed with respect to the learner’s actor policy, but with the overall multi-step advantage from the collection of value functions correct? I’m not 100% sure that I understand why this is okay since $\hat{f}^+(s_{t+1})$ and $\hat{f}^+(s_{t})$ can be from different policies, right? My guess is that it is fine because they are both independent of the action but I would appreciate some clarification.

Q6. Did you use the original implementations for MAPS and MAMBA or did you reimplement the methods? Do you have an intuition why in the present comparisons these methods perform significantly worse than in the previous literature?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the max+ algorithm, which is a hybrid imitation + reinforcement learning algorithm which utilizes a set of expert policies to aid a policy in initial learning and exploration, and gradually transitions to reinforcement learning as the learner policy improves. The method maintains a value estimate for each expert policy as well as the learner's, and uses the value functions to construct an update rule that improves over the best expert in the set. The authors then apply their proposed method to the continuous control domain on DM Control Suite and Metaworld tasks, where they demonstrate that their method achieves greater learning speed than prior baselines.

### Strengths
- The paper is clear and well written. The authors have done a good job of presenting an overview of their method, giving theoretical justification of why the method works, and benchmarking against several state-of-the-art baselines.
- The experiments are detailed, and I appreciate the ablation studies which show the usefulness of the robust policy selection rule vs naive rule, and the transition from utilizing the expert policies early in training while transitioning smoothly to RL as the policy improves.
- I am not familiar enough with the literature in this subdomain to judge the degree of novelty in the approach, but based on the information presented in the paper the proposed update rule (the robust policy gradient, and robust policy selection) is novel.

### Weaknesses
 - For reproducibility purposes, it would be great if the authors could include a table of algorithm hyperparameters used in the appendix, and hyperparameter sweeping strategies.

### Questions
- How would the following naive baseline perform? Initialize from the expert policy, and then finetune from there with RL. It seems like this baseline could perform quite well in the proposed experimental setup, given that PPO-GAE is one of the baselines and performs quite well.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method that combines RL and IL to learn a policy that improves upon a set of imperfect oracles. The method extends the MAMBA algorithm [1] by incorporating the learner policy into the set of oracles and using uncertainty-aware value-estimates to define the exploration strategy and advantage estimator. These changes enable the proposed method to behave like an RL algorithm in cases where the oracles do not provide beneficial supervision. The proposed method achieves good results in mujoco and meta-world tasks, beating most of the oracle policies and baselines.

### Strengths
- The proposed method beats a range of relevant baselines in a diverse set of benchmarks.
- The sections 1 to 5 are generally well written and reasonably easy to follow. Caveat: I did not verify the derivations myself.

### Weaknesses
## Presentation
- The method description has missing details. These are also issues with soundness of the paper.
    - The necessary details for understanding equation (12) are not clearly presented. See questions.
    - The value ensemble is central to the proposed method, yet there are only two sentences at the bottom of page 5 discussing how the value ensemble is trained.
- The theory section borrows from MAMBA, which is only natural since these methods are closely related, but it would have been clearer to emphasize the points of departure from MAMBA more and perhaps move the parts that are more closely shared to the appendix.
- Nitpick:
    - The definition of policy gradient with advantage is cited for Schulman, but there are prior works considering policy gradients with advantage estimation, e.g., [2].
    - The abstract mentions real-world scenarios but the paper does not talk about them.



## Soundness
- Computing the update requires evaluating the value ensembles for all of the oracles. Compared to normal RL algorithm, e.g., PPO, this means number of oracles times the size of ensemble more forward passes. Depending on the number of oracles and ensemble members, this may equate to a lot more expensive loss evaluation. In addition to the missing details about the ensemble size and number of oracles, it would be good to include some wall-time comparisons between the different methods.

## Experimental evaluation
- Cartpole is a bit too easy environment for the otherwise well-executed ablation study.
- In the appendix, it says that the value ensembles are pre-trained before the main loop starts. That sounds like the proposed method uses more samples (and more compute) than the baselines. This should be mentioned in the main paper and discussed as a limitation.

## Summary
The proposed method seems to do well, but the paper is missing too many details and is too hard to follow at parts that it is hard to evaluate whether the contribution is impactful or not. I think including a thorough discussion about the relationship of the proposed method and MAMBA as well as limitations would go a long way to make this easier to understand. Additionally, adding all of the missing details that I have listed here and in the questions would help.

### Questions
- Equation (12)
    - What does equation (12) mean when the "when"-clause equates to false?
    - What does $\hat{V}_{\mu}^{|\Pi^{\varepsilon}|}$ mean?
- How many members are there in the value-function ensemble?
- How many oracles does each experiment have?
- Why are the replay buffers for the oracles so small? The oracle policies do not change, so the data does not become more off-policy as the training proceeds.
- What are the x-axes in the result figures? Surely the algorithms do not converge in 100 gradient steps?
- How many timesteps are sampled for value-function pre-training? How would the learning curves look like if these steps were included on the x-axis? In general, using environment steps as the x-axis would make it easier to compare methods that are otherwise so different.


[1] Policy Improvement via Imitation of Multiple Oracles, Cheng et al. 2020

[2] Policy Gradient Methods for Reinforcement Learning with Function Approximation, Sutton et al. 2000

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
