# Proximal Policy Gradient Arborescence for Quality Diversity Reinforcement Learning

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Training generally capable agents that thoroughly explore their environment and learn new and diverse skills is a long-term goal of robot learning.
Quality Diversity Reinforcement Learning (QD-RL) is an emerging research area that blends the best aspects of both fields -- Quality Diversity (QD) provides a principled form of exploration and produces collections of behaviorally diverse agents, while Reinforcement Learning (RL) provides a powerful performance improvement operator enabling generalization across tasks and dynamic environments.
Existing QD-RL approaches have been constrained to sample efficient, deterministic \textit{off-policy} RL algorithms and/or evolution strategies, and struggle with highly stochastic environments. 
In this work, we, for the first time, adapt on-policy RL, specifically Proximal Policy Optimization (PPO), to the Differentiable Quality Diversity (DQD) framework and propose additional improvements over prior work that enable efficient optimization and discovery of novel skills on challenging locomotion tasks. 
Our new algorithm, Proximal Policy Gradient Arborescence (PPGA), achieves state-of-the-art results, including a 4x improvement in best reward over baselines on the challenging humanoid domain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose Proximal Policy Gradient Arborescence (PPGA), a new QD-RL algorithm that builds on a DQD algorithm, specifically CMA-MAEGA, with an on-policy RL algorithm, specifically PPO, as the gradient estimator. To make this integration more stable, the authors propose multiple changes: 1) replace the CMA-ES in CMA-MAEGA with a more contemporary xNES algorithm to update the distributions, as a solution to accommodate the noisy RL objective, 2) use PPO with weighted rewards to walk the search point to avoid gradient staleness. The authors also implement a vectorized PPO for efficient gradient estimation.

Empirically, the author demonstrates that PPGA achieves much higher quality solutions compared with previous QD-RL baselines with matching coverage rates in multiple Mujoco locomotion domains.

### Strengths
- The paper is generally well-written and easy to follow.
- The proposed techniques to accommodate the integration issues of PPO are all logically and empirically justified.
- There are substantial empirical improvements over previous baselines, especially in terms of solution qualities. As a side note, I do find the introduction of the Complementary Cumulative Distribution Function provides a very intuitive way of evaluating the solution quality and diversity.

### Weaknesses
 - At the beginning of Sec 3.2, the authors claim "Being an approximate trust region method, it provides some formal guarantees on the quality of the gradient estimates". Could the authors expand on this and more formally establish this claim? This claim is an important reason of choosing PPO since there are other parallelizable RL algorithm choices such as IMPALA[1]. Specifically, the authors should elaborate on the specific trust region guarantees that PPO provides in the context of non-stationary objectives, and how these guarantees are more suitable than those of alternative methods like IMPALA. The current justification is not sufficiently rigorous to justify the choice of PPO over other parallelizable RL algorithms.
- I have a slight concern that all the ablation studies show a dramatic decrease in performance. Could finding a better set of hyperparameters instead of inheriting the PPGA hyperparameters help? The ablation study for xNES vs CMA-ES, for example, should include a more thorough hyperparameter optimization for CMA-ES, as the current results do not definitively rule out the possibility that a better-tuned CMA-ES could achieve comparable performance. Similarly, the TD3GA ablation should explore a wider range of hyperparameters, including replay buffer size and update frequency, to ensure that the observed performance drop is not due to suboptimal parameter choices.

### Questions
I don't have more questions apart from the ones in the weaknesses section.

### Soundness
3 good

### Presentation
3 good

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
A RL policy can learn to maximize cumulative reward in an environment by discovering an optimal policy. This paper shows that there are potentially many different sets of behaviors that could achieve optimal or near optimal performance. For example the authors highlight that in the humanoid walker environment different strategies can be discovered that all perform well: jumping, galloping, walking... These strategies can all be characterized by some measurements that are computed on trajectories. Figure 1 demonstrates this concept quite well. It plots two different measures with a heatmap of how well the policy at each point fulfilled the main objective (locomotion)

There are already prior works which establish this idea of characterizing policies with measures and attempting to maximize diversity in measure space. There are works that focus on differentiable measures and works that use non differentiable measures. This paper considers non-differentiable measures and approximates them using the bellman equation.

Several value functions are learned which each approximate the instantaneous measure functions (deltas) and the overall objective function f. ***Each measure function is the average of the instantaneous measurement (delta) in each state.***

Since all value functions are differentiable then a gradient of policy parameters with respect to a linear combination of these value functions can be obtained. Different weights can be assigned to each value function to cause the actor update to move in a different direction in the archive / measure space.

### Strengths
Overall this is an interesting work. Massive (4x) performance gain compared to baselines.
Nice interpretability of archive exploration. The archives produced by PPGA seem more
interesting to look at. There are more distinct peaks shown in Fig 3 than the baseline.

### Weaknesses
I would suggest the authors make the explanation of the policy sampling more clear since that is what confused me the most.

The notation for the gradient of the measures (\nabla m) is not clear. Is it the gradient of the measure with respect to the policy parameters? (this is explained only later in the paper)

I suggest moving pseudocode Algorithm 1 to the main text.

CMA-ES is introduced but not really elaborated upon. It seems to be very important in sampling different policy parameters. how is branching the policy parameters in different directions in measure space done?

looks like Section 3.3 contains unnecessary formalism which is not used elsewhere in the paper. why is it provided?

### Questions
CMA-ES is introduced but not really elaborated upon. It seems to be very important in sampling different policy parameters. how is branching the policy parameters in different directions in measure space done?

looks like Section 3.3 contains unnecessary formalism which is not used elsewhere in the paper. why is it provided?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents Proximal Policy Gradient Arborescence (PPGA), a novel algorithm that combines PPO with Differentiable Quality Diversity to improve the performance of QD-RL in challenging locomotion tasks. The authors propose several key changes to existing methods, including a vectorized implementation of PPO, generalizing CMA-based DQD algorithms using Natural Evolution Strategies, introducing Markovian Measure Proxies, and a new method for moving the search point in the archive. The experiment results show that PPGA achieves state-of-the-art results, with a 4x improvement in best reward over baselines on the challenging humanoid domain.

### Strengths
1. The paper addresses a significant gap in performance between QD-RL and standard RL algorithms on continuous control tasks. The results demonstrate state-of-the-art performance of PPGA, which combines the strengths of PPO and DQD, on challenging locomotion tasks, with a 4x improvement in best reward over baselines.
2. The paper provides a clear and well-structured presentation of the proposed algorithm and its components.

### Weaknesses
1. The paper could benefit from a more detailed comparison with other QD-RL methods and an explanation of why PPO was specifically chosen over other RL algorithms.
2. The generalizability of the proposed algorithm to other domains and tasks beyond locomotion is not discussed.
3. It would be better to see some discussion about the scalability of the proposed algorithm, especially in comparison to existing methods.

### Questions
1. Can you provide more insight into why PPO was specifically chosen over other RL algorithms for this work?
2. How does the proposed PPGA algorithm perform in other domains and tasks beyond locomotion?
3. Can you discuss the scalability of the proposed algorithm, especially in comparison to existing methods?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose PPGA, a QDRL algorithm where the RL part is based on PPO, an on-policy RL algorithm, whereas all existing QDRL algorithms use the off-policy PPO. This change makes it possible to benefit from the good parallelization capabilities of PPO, and the authors claim that there are also other interesting synergies between PPO and their QD approach. The authors show that PPGA outperforms previous SOTA QDRL algorithms in four locomotion benchmarks.

After the authors rebuttal and given their revised version, I change my evaluation to "accept".

### Strengths
- The proposed PPGA algorithm is novel and interesting. It outperforms relevant previous SOTA baselines. To me, this should be sufficient to warrant publication.

- The experimental study looks correct.

### Weaknesses
 - The paper (still) needs improvements in the presentation to make it more interesting to a large machine learning audience.

- The claim about the synergies between DQD and PPO looks insufficiently backed-up. In particular, the main paper does not even mention the TD3GA algorithm, while the study of combining DQD with TD3 is crucial to understand these synergies. More generally, your central claim is that using on-policy RL better fits the DQD framework, so the comparison to TD3GA should be central.

Abstract: 

- "Existing QD-RL approaches have been constrained to sample efficient, deterministic off-policy RL algorithms and/or evolution strategies, *and struggle with highly stochastic environments*." -> the rest of the abstract makes it clear that you switch to on-policy RL, but it does not make clear that you will solve the highly stochastic environments issue. Do you really need to mention that? If yes, you need to mention how you will solve it.

- "propose several changes" -> changes wrt what? It is a weird formulation, you have a new algorithm, you propose new things, no need to mention that...

Introduction:

parag 1 is OK (maybe a ref at the end of the sentence finishing with "high-quality solutions" or merge the sentence with the next ones, where the references are).

parag 2 has several issues:

- "For example, all QD-RL algorithms for locomotion to date use non-differentiable measure functions, which in most cases prevents direct RL optimization."

-> At this point, the standard ML reader does not know what a measure function is, 

-> I don't agree that having non-differentiable measure functions prevents direct RL optimization. RL methods are precisely good at approximating some gradients when they are not available. Even if you want to discuss this with me, this sentence is ill-placed, as the standard reader cannot get its meaning.

- "Prior methods that investigated combining DQD". You should re-explain the acronym, doing it once in the abstract is not enough.

- "However, given the gap in performance between standard RL and QD-RL algorithms in terms of best-performing policy, we believe that DQD algorithms, under a different formulation more synergistic with its underlying mechanisms, can close this gap. We instead believe that one or both of existing DQD and RL methods must be adapted to each other in order to maximally exploit their synergy."

-> Both sentences say more or less the same thing, I suspect this is a last-minute-no-reread edition issue.

- "maintain a single search point within the archive that" -> at this point, the standard ML reader does not know what the search point is, and what the archive is.

- "The question we aim to answer becomes clear through this high-level view – can we better adapt DQD algorithms to challenging RL domains by exploiting its synergy with PPO?" -> the third time you mention exploiting this synergy in the same paragraph...

I afraid that, with all the points above, you have already lost the standard reader, who won't read your paper any further. Instead, you must give a high-level view of PPGA from the RL viewpoint, with the RL vocabulary (a search point is a policy, etc.).

- As contribution (1), you propose an implementation ... : I see no link to a source code in the paper, so you should not mention such a contribution [EDIT: OK, the source code is in the supplementary, forget this comment]

- What a "non-stationary QDRL task"? 

- Contrib (4) sould be reformulated with the RL vocabulary. Otherwise, rather submit your paper to GECCO, as I already advised you twice...

- where T is (the) episode length

- the deep neural network represents *a* state-action mapping, not necessarily the optimal one.

### Deep RL background:

- About your Deep RL background, it is close to good (there is no major mistake), but it is still confusing for the non-expert and you can do a better job.
- I think the point you want to make is that PPO is on-policy. In the current classification, it is not in the "on-policy" part, but in the "trust region" part
- Mentioning actor-critic in the on-policy part the way you do brings confusion. It is true that A2C and A3C are actor-critic and on-policy, but DDPG, TD3, SAC and others are actor-critic too and they are off-policy.
- I think what you need is the distinction between policy-based methods (Reinforce, A2C, TRPO, PPO) which derive their gradient from the policy and are on-policy, and value-based methods (DQN, DDPG, TD3, SAC, ...) which derive their gradient from the critic and are off-policy.

See e.g. Nachum, O., Norouzi, M., Xu, K., & Schuurmans, D. (2017). Bridging the gap between value and policy based reinforcement learning. Advances in neural information processing systems, 30.

### Other points

- the equation with L(theta) should finish with a dot.

- In the QD optimization section, don't you want to mention QDRL in the last parag?

- "gradients around the search point ∇ 1 , ..., ∇ λ" -> gradients ∇ 1 , ..., ∇ λ around the search point. 

- Again, why not call the search point "the current policy"? The same for "solutions", they are policies.

- "some minimum threshold". Why call this a minimum threshold? Threshold for what? I rather see it as an exploration bonus...

- "in the direction of the archive that is least" -> doesn't this also take performance into account?

- In 2.4: "In prior work (ref) ... In this work" -> You should not write this in a way that let us know who you are. *Your paper could be desk-rejected for that. Actually, this is transparent given the (too) many self-references, but you have to follow the rules*.

- In 3.2, I'm afraid the claim that trust region methods provide formal guarantees on the quality of the gradient estimates is wrong. The proof in TRPO comes with unrealistic assumptions that are always violated in experimental RL work.

- You use the MMPs as rewards to optimize. So it means that your algorithm is looking for as much leg contact as possible. Shouldn't it be looking for as much "leg contact diversity" as possible instead? This is unclear. Could you clarify?

- "We additionally modify the computation of the policy gradient into a batched policy gradient method, where intermediate gradient estimates of each function w.r.t. policy params only flow back to the parameters corresponding to respective individual policies during minibatch gradient descent." -> This part is very unclear to me, a small diagram or equations would probably help.

- jacobian -> Jacobian

- There are many considerations about using constant variance or not. Actually in the literature, there are 3 options: using a constant variance, using a tunable variance which is not a function of states, and using a tunable state-dependent variance where the NN outputs a mean and a variance for each state. The second one is used e.g. in the TRPO paper, see Fig. 3 here: https://proceedings.mlr.press/v37/schulman15.pdf
I think you need to further study this point, your work is not convincing in that respect. The fact that you "disable gradient flow" to the variance parameter or not depending on the environment is not satisfactory at all.

- About Section 3.3, I think the first paragraph which establishes that xNES is a better option that CMA-ES in your context could be moved in an appendix together with the corresponding sutdy, as this is not central to your story. You could make profit of the earned space to add a paragraph about the comparison between TD3GA and PPGA (with selected results), which is much more important.

- At the end of 3.4, you mention the outer optimization loop, but the inner/outer loop distinction has not been made explicit in the main paper.

- "We use an archive learning rate of 0.1, 0.15, 0.1, and 1.0..." -> The fact that there is such a learning rate is not explained before.

- All experimental figures and tables make a poor use of space. By reworking this aspect you can both save more space and make your results more readable and explicit.

- In Fig. 4, using +/- one std as variance information is a bad practice in RL, where the variance is generally not Gaussian. See 
Patterson, A., Neumann, S., White, M., & White, A. (2020). Draft: Empirical Design in Reinforcement Learning. Journal of Artificial Intelligence Research, 1. and Agarwal, R., Schwarzer, M., Castro, P. S., Courville, A. C., & Bellemare, M. (2021). Deep reinforcement learning at the edge of the statistical precipice. Advances in neural information processing systems, 34, 29304-29320, the latter comes with a useful visualization library.

- Figure 4 is cited before fig 3, you should reorder

- "We present a new method, PPGA, which is one of the first QD-RL methods to leverage on-policy RL," -> one of the first, so what are the others?

- "We show that DQD algorithms and on-policy RL have emergent synergies that make them work particularly well with each other." -> I'm sorry but this point does not emerge clearly from reading the paper. You should have somewhere a paragraph about the investigations of these synergies.

- Your paper needs slightly more than 9 pages. Again, *it could have been desk-rejected for that*. Please follow the rules.

### Questions
To be fully transparent, this is the third time I'm reviewing this paper, after ICML23 and NeurIPS23. Each time I was in favor of accepting the paper because I believe the proposed algorithm is truly interesting, but each time the authors failed to convince some reviewers, mostly due to some writing issues and insufficient focus on the comparison between TD3GA and PPGA. I hope this time could be the right time with a further writing effort that I will try to contribute to below. So my review will mostly focus on writing aspects, but keep in mind that the TD3GA vs PPGA comparison is crucial and not even mentioned in the main paper.

Abstract: 

- "Existing QD-RL approaches have been constrained to sample efficient, deterministic off-policy RL algorithms and/or evolution strategies, *and struggle with highly stochastic environments*." -> the rest of the abstract makes it clear that you switch to on-policy RL, but it does not make clear that you will solve the highly stochastic environments issue. Do you really need to mention that? If yes, you need to mention how you will solve it.

- "propose several changes" -> changes wrt what? It is a weird formulation, you have a new algorithm, you propose new things, no need to mention that...

Introduction:

parag 1 is OK (maybe a ref at the end of the sentence finishing with "high-quality solutions" or merge the sentence with the next ones, where the references are).

parag 2 has several issues:

- "For example, all QD-RL algorithms for locomotion to date use non-differentiable measure functions, which in most cases prevents direct RL optimization."

-> At this point, the standard ML reader does not know what a measure function is, 

-> I don't agree that having non-differentiable measure functions prevents direct RL optimization. RL methods are precisely good at approximating some gradients when they are not available. Even if you want to discuss this with me, this sentence is ill-placed, as the standard reader cannot get its meaning.

- "Prior methods that investigated combining DQD". You should re-explain the acronym, doing it once in the abstract is not enough.

- "However, given the gap in performance between standard RL and QD-RL algorithms in terms of best-performing policy, we believe that DQD algorithms, under a different formulation more synergistic with its underlying mechanisms, can close this gap. We instead believe that one or both of existing DQD and RL methods must be adapted to each other in order to maximally exploit their synergy."

-> Both sentences say more or less the same thing, I suspect this is a last-minute-no-reread edition issue.

- "maintain a single search point within the archive that" -> at this point, the standard ML reader does not know what the search point is, and what the archive is.

- "The question we aim to answer becomes clear through this high-level view – can we better adapt DQD algorithms to challenging RL domains by exploiting its synergy with PPO?" -> the third time you mention exploiting this synergy in the same paragraph...

I afraid that, with all the points above, you have already lost the standard reader, who won't read your paper any further. Instead, you must give a high-level view of PPGA from the RL viewpoint, with the RL vocabulary (a search point is a policy, etc.).

- As contribution (1), you propose an implementation ... : I see no link to a source code in the paper, so you should not mention such a contribution [EDIT: OK, the source code is in the supplementary, forget this comment]

- What a "non-stationary QDRL task"? 

- Contrib (4) sould be reformulated with the RL vocabulary. Otherwise, rather submit your paper to GECCO, as I already advised you twice...

- where T is (the) episode length

- the deep neural network represents *a* state-action mapping, not necessarily the optimal one.

### Deep RL background:

- About your Deep RL background, it is close to good (there is no major mistake), but it is still confusing for the non-expert and you can do a better job.
- I think the point you want to make is that PPO is on-policy. In the current classification, it is not in the "on-policy" part, but in the "trust region" part
- Mentioning actor-critic in the on-policy part the way you do brings confusion. It is true that A2C and A3C are actor-critic and on-policy, but DDPG, TD3, SAC and others are actor-critic too and they are off-policy.
- I think what you need is the distinction between policy-based methods (Reinforce, A2C, TRPO, PPO) which derive their gradient from the policy and are on-policy, and value-based methods (DQN, DDPG, TD3, SAC, ...) which derive their gradient from the critic and are off-policy.

See e.g. Nachum, O., Norouzi, M., Xu, K., & Schuurmans, D. (2017). Bridging the gap between value and policy based reinforcement learning. Advances in neural information processing systems, 30.

### Other points

- the equation with L(theta) should finish with a dot.

- In the QD optimization section, don't you want to mention QDRL in the last parag?

- "gradients around the search point ∇ 1 , ..., ∇ λ" -> gradients ∇ 1 , ..., ∇ λ around the search point. 

- Again, why not call the search point "the current policy"? The same for "solutions", they are policies.

- "some minimum threshold". Why call this a minimum threshold? Threshold for what? I rather see it as an exploration bonus...

- "in the direction of the archive that is least" -> doesn't this also take performance into account?

- In 2.4: "In prior work (ref) ... In this work" -> You should not write this in a way that let us know who you are. *Your paper could be desk-rejected for that. Actually, this is transparent given the (too) many self-references, but you have to follow the rules*.

- In 3.2, I'm afraid the claim that trust region methods provide formal guarantees on the quality of the gradient estimates is wrong. The proof in TRPO comes with unrealistic assumptions that are always violated in experimental RL work.

- You use the MMPs as rewards to optimize. So it means that your algorithm is looking for as much leg contact as possible. Shouldn't it be looking for as much "leg contact diversity" as possible instead? This is unclear. Could you clarify?

- "We additionally modify the computation of the policy gradient into a batched policy gradient method, where intermediate gradient estimates of each function w.r.t. policy params only flow back to the parameters corresponding to respective individual policies during minibatch gradient descent." -> This part is very unclear to me, a small diagram or equations would probably help.

- jacobian -> Jacobian

- There are many considerations about using constant variance or not. Actually in the literature, there are 3 options: using a constant variance, using a tunable variance which is not a function of states, and using a tunable state-dependent variance where the NN outputs a mean and a variance for each state. The second one is used e.g. in the TRPO paper, see Fig. 3 here: https://proceedings.mlr.press/v37/schulman15.pdf
I think you need to further study this point, your work is not convincing in that respect. The fact that you "disable gradient flow" to the variance parameter or not depending on the environment is not satisfactory at all.

- About Section 3.3, I think the first paragraph which establishes that xNES is a better option that CMA-ES in your context could be moved in an appendix together with the corresponding sutdy, as this is not central to your story. You could make profit of the earned space to add a paragraph about the comparison between TD3GA and PPGA (with selected results), which is much more important.

- At the end of 3.4, you mention the outer optimization loop, but the inner/outer loop distinction has not been made explicit in the main paper.

- "We use an archive learning rate of 0.1, 0.15, 0.1, and 1.0..." -> The fact that there is such a learning rate is not explained before.

- All experimental figures and tables make a poor use of space. By reworking this aspect you can both save more space and make your results more readable and explicit.

- In Fig. 4, using +/- one std as variance information is a bad practice in RL, where the variance is generally not Gaussian. See 
Patterson, A., Neumann, S., White, M., & White, A. (2020). Draft: Empirical Design in Reinforcement Learning. Journal of Artificial Intelligence Research, 1. and Agarwal, R., Schwarzer, M., Castro, P. S., Courville, A. C., & Bellemare, M. (2021). Deep reinforcement learning at the edge of the statistical precipice. Advances in neural information processing systems, 34, 29304-29320, the latter comes with a useful visualization library.

- Figure 4 is cited before fig 3, you should reorder

- "We present a new method, PPGA, which is one of the first QD-RL methods to leverage on-policy RL," -> one of the first, so what are the others?

- "We show that DQD algorithms and on-policy RL have emergent synergies that make them work particularly well with each other." -> I'm sorry but this point does not emerge clearly from reading the paper. You should have somewhere a paragraph about the investigations of these synergies.

- Your paper needs slightly more than 9 pages. Again, *it could have been desk-rejected for that*. Please follow the rules.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
