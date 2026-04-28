# Language Reward Modulation for Pretraining Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Using learned reward functions (LRFs) as a means to solve sparse-reward reinforcement learning (RL) tasks has yielded some steady progress in task-complexity through the years. In this work, we question whether today's LRFs are best-suited as a direct replacement for task rewards. Instead, we propose leveraging the capabilities of LRFs as a pretraining signal for RL. Concretely,  we propose \textbf{LA}nguage Reward \textbf{M}odulated \textbf{P}retraining (LAMP) which leverages the zero-shot capabilities of Vision-Language Models (VLMs) as a \textit{pretraining} utility for RL as opposed to a downstream task reward. LAMP uses a frozen, pretrained VLM to scalably generate noisy, albeit shaped exploration rewards by computing the contrastive alignment between a highly diverse collection of language instructions and the image observations of an agent in its pretraining environment. LAMP optimizes these rewards in conjunction with standard novelty-seeking exploration rewards with reinforcement learning to acquire a language-conditioned, pretrained policy. Our VLM pretraining approach, which is a departure from previous attempts to use LRFs, can warmstart sample-efficient learning on robot manipulation tasks in RLBench.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to pretrain a language-conditioned RL policy using feedback from a vision-language model (that aligns video frames with the task completion) combined with an exploration bonus. Such a policy is then finetuned on individual RL tasks. Performance is analyzed across a few different tasks, and components of the method are ablated.

### Strengths
- The proposed method shows a solid benefit on some of the evaluation tasks, and at least a minor benefit on all (Figure 5)
- The writing is in general quite clear and easy to follow

### Weaknesses
 - As far as I can tell, the main contribution here is the choice of vision-language model, the particular temporal objective (a minor change), and the addition of an exploration reward (Plan2Explore), but if the authors claim that this method is worth further study regardless of the specifics in the paper, they need to be ablated. The exploration reward is ablated (RND shows up as standalone pretraining in Figure 13). The vision-language model is only ablated on a single task (Figure 7). The objective is never ablated, unless we count the comparison to ZeST as a combination, in which case it's unclear that there is a benefit to the proposed scheme.
- Regardless of claims of novelty, the result is not super strong. From Appendix C.4 and Figure 12 it is my understanding that pretraining is a minimum of 100k steps, which would be nice to see in the main paper. From Figure 5, we see that in the worst case, pretraining saves us 50k steps (Pick Up Cup, Take Lid Off Saucepan) and pretraining with P2E is quite close. Combine this with the missing baselines and I wonder if the method is competitive on a fixed-compute budget with single-task training.
- I'm not sure if the evaluations are separated into in-distribution and out-of-distribution tasks, but it would be worthwhile to understand the performance drop on OOD tasks that were not used in pretraining to further understand the benefit of this pretraining.
- I think it would be worthwhile to include a baseline that is finetuned from some supervised language-conditioned model to further justify why we need to pretrain in the RL setting. RL is complex and unwieldy, so it would be nice to justify its necessity through an experiment.
- There are many moving parts in this method (proposed method, Masked World Model policy, Plan2Explore additional reward, architectural choices against baselines, notice the number of hyperparameters in Tables 5, 6, 7, 8 and 9) which are significantly more complex than the standard deep RL setting, and it would be nice to see experiments justifying all of these choices, or at least further argument. It is also unclear why Masked World Models were chosen over other common RL algorithms such as SAC, PPO, or DreamerV3, and this choice should be justified in the main text. The exploration reward ablation is also relegated to the appendix, which makes it difficult to understand the core contributions of the work.

### Questions
- How many tasks are used for pretraining and evaluation?
- Is there a split in the evaluation into seen and unseen tasks? This was the original motivation for the method so I think it is worthwhile to test.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes LAMP, a pre-training algorithm that uses the reward from R3M plus plan2explore rewards to pre-train the agents, and then finetunes the agents with task rewards. LAMP achieves better sample efficiency on 5 tasks from RLBench, and ablation results show that the correct language prompt and the vision-language model are key to the success.

### Strengths
The usage of R3M is overall interesting. Since the reward from out-of-domain models is noisy naturally (Figure 3), this work proposes to use such noisy signals as a pre-training method. Also, some factors presented to enhance such rewards, including plan2explore rewards and language prompts, are natural and well-motivated.

Overall I think this paper is interesting and would tend to give acceptance.

### Weaknesses
- **The weight of plan2explore rewards.** The authors use a weight of 0.9 for plan2explore rewards, and only a weight of 0.1 for their proposed rewards. Would the weight impact much? It could be interesting to see more ablation results for this parameter. 
- **Lack of baseline**. I think VIPER [1] and VIP [2] could also serve as baselines. It would be good to see more baseline results in Figure 5.
- **No results about pre-training stages.** What is the success rate of directly applying rewards of LAMP for in-domain task learning?

### Questions
See **weakness**.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an approach for RL pre-training that relies on collecting data with VLM-based rewards functions for some semantically meaningful tasks + an exploration objective. Then, the policy is fine-tuned for the task of interest with the scripted reward and the authors show that learning is faster when pre-training is used in several environments.

### Strengths
The presented method is well explained and clear, the paper is well structured. The illustrations facilitate paper understanding. I find the idea of the use of VLM based rewards for semantic exploration interesting and promising. The novelty of the method is how the VLMs are used in exploration: through the noisy reward function. The ablations on the style of the prompt are interesting.

### Weaknesses
 - I have some doubts about the usefulness of the core of the proposed method for the realistic setting. It seems that the best reported results are obtained when the semantic tasks for exploration were based on the task that was later used for fine-tuning (prompt style 2 uses reformulations of that task). How realistic is the assumption of knowing the target task at the pre-training stage? Does it mean that the method would require a new pre-training stage when the task changes? In that case, why not use the exploration budget instead for extra data collection for the task of interest? Also, the authors used the scripted reward based on the environment state for the fine tuning on the task of interest. Why not continue using the learnt reward model in this case? In a real world scenario this would be the only way to obtain the rewards.
- The paper only considers two baselines for the proposed method: training from scratch or using an exploration objective. There is a large body of literature on exploration for RL pre-training, so it would be nice to add other baselines. In particular, methods that use semantic exploration in RL with the help of pre-trained VLMs are the most relevant. See for example:
Semantic Exploration from Language Abstractions and Pretrained Representations. Allison Tam, Neil Rabinowitz, Andrew Lampinen, Nicholas A. Roy, Stephanie Chan, DJ Strouse, Jane Wang, Andrea Banino, Felix Hill. NeurIPS 2022.
- It seems that the proposed method includes the component of semantic exploration with only 0.1 weight and the rest is based on the prior work Plan2Explore. I am wondering how sensitive the method is to the choice of this weight? If the proposed objective is used without Plan2Explore, does it still outperform the two baselines?

Some minor points:
- Why was it necessary to do scene augmentations with the same textures/images that were used for pre-training a VLM (Ego4D)? Could other (independent of pre-training) scene augmentations be used?
- The robotic scene is not taken into account when semantic tasks at the pre-training stage are selected and as authors notes, some of them are infeasible or even meaningless (prompt style 6). Then, would it be sufficient in that case to replace the rewards for exploration with just random rewards?

### Questions
I would like to hear the authors' discussion regarding the three weaknesses that I highlighted above:
- usefulness of the method given finetuning on similar tasks and use of scripted rewards for finetuning;
- baselines for explorations with the help of VLMs;
- the effect of constant 0.1 and the importance of prior explorations objectives.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Specifying the reward function is a longstanding yet fundamental problem in RL. While the learned reward functions (LRFs) can have errors, they may help exploration during the lower-stakes pretraining stage of training, where diverse, rather than task-specific, behaviors are desired to be learned. By the strong zero-shot ability of vision-language models (VLMs), one may utilize pre-trained VLMs to specify the different reward functions in different tasks. This paper investigates how to use the flexibility of VLMs to scalably generate rewards to pretrain an RL agent, so as to accelerate downstream learning when a specific task is given. The authors propose LAnguage Reward Modulated Pretraning (LAMP), a method for pretraining diverse policies by optimizing VLM parameterized rewards. In particular, they query a VLM with highly diverse language prompts and the visual observations of the agent to generate diverse pretraining rewards, which is further augmented with the intrinsic reward from Plan2Explore. Experimentally, the authors demonstrate that a general-purpose policy can be learned by pretraining the agent with VLM reward. Such a policy can speed up the downstream RL tasks.

### Strengths
1. The overall direction of language-conditional control and leveraging VLMs for (pre)training RL agent is promising and interesting.
2. The technique is generally novel of prompting VLMs with diverse synonyms language prompts to generate the (pretraining) rewards for an array of tasks.
3. It is interesting to see the ablation study on different prompt styles used during the pretraining phase.

### Weaknesses
1. It is not clear to me what is the main contribution of the proposed method. Many, if not most, of the components in the proposed method come from prior works, such as R3M, Plan2Explore, vision-language-embedding matching and so on. Meanwhile, the idea of conditioning the reward function on instructions/goals is also not novel, see the following Point 2.
2. It seems missing the connection of the proposed method with  goal-conditioned RL and and distinction from them. For example, how is prompting VLM with different language instructions different from inputting different goal states to the goal-conditioned reward function?
3. The proposed pre-training stage seems computationally expensive, requiring rollouts, language and visual embeddings, calling the R3M score predictors, and so on, before updating the RL components.
4. Considering the relatively wide error bars in Fig. 5, the performance gain of the proposed method LAMP may not be clear when comparing with the baseline P2E.
5. Figure 7 may not convincingly support the claim that the proposed method "is not inherently reliant on a particular VLM", since the authors only show the results of ZeST besides the main choice R3M.

### Questions
1. How does the performance of the proposed method compare with prior works that learns options/skills as pretraining? And what about compared with goal-conditioned RL methods, which may be used for pretraining similar to the proposed method?
2. Why is the pretraining stage lower-stakes? Do you have any reference or justification? 
3. Is there any intuition why the $r^{VLM}$ is combined with the intrinsic rewards from Plan2Explore,  which is itself a novelty-seeking score? Is there any intuition why in Fig. 7 the performance degrades quite significantly when using $r^{VLM}$ alone to pre-train the agent?
4. The $R_t$ just below the title of Section 3 seems missing an expectation symbol?
5. Are there any requirements on the downstream tasks so that the pretraining pipeline in Section 4.2 remains helpful? 
6. How sensitive is the proposed method to the $\alpha$ parameter in Eq. 2?
7. In Figure 6 (right), why does LAMP Prompt 6 (w/o P2E) perform so well, close to LAMP under Prompt Style 2 (even with P2E)? This is a bit counter-intuitive to me since Prompt 6 is "Snippets from Shakespeare".
8. Is there an ablation study on the novelty-seeking RL pretraning methods. For example, what if we change Plan2Explore to other methods?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
