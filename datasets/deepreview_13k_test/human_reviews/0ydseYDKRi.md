# Beyond The Rainbow: High Performance Deep Reinforcement Learning On A Desktop PC

- Decision: Reject
- Scores: 8, 5, 6, 3

## Abstract
Rainbow Deep Q-Network (DQN) demonstrated combining multiple independent enhancements could significantly boost a reinforcement learning (RL) agent’s performance. In this paper, we present ``Beyond The Rainbow'' (BTR), a novel algorithm that integrates six improvements from across the RL literature to Rainbow DQN, establishing a new state-of-the-art for RL using a desktop PC, with a human-normalized interquartile mean (IQM) of 7.4 on Atari-60. Beyond Atari, we demonstrate BTR's capability to handle complex 3D games, successfully training agents to play Super Mario Galaxy, Mario Kart, and Mortal Kombat with minimal algorithmic changes. Designing BTR with computational efficiency in mind, agents can be trained using a desktop PC on 200 million Atari frames within 12 hours. Additionally, we conduct detailed ablation studies of each component, analyzing the performance and impact using numerous measures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Beyond The Rainbow (BTR), a novel reinforcement learning (RL) algorithm that enhances Rainbow DQN by integrating six key improvements. The BTR algorithm is computationally efficient, capable of training powerful agents on a standard desktop computer within a short time. Experimental results show that BTR outperforms state-of-the-art RL algorithms on both the Atari-60 and Procgen benchmarks. Additionally, BTR can handle training agents for challenging levels in complex, modern games. Finally, this paper includes a comprehensive ablation study to analyze the performance and impact of each component within the BTR algorithm.

### Strengths
1. This paper is well-written and well-organized. The ideas are clear and could be easily understood
2. The experiments are comprehensive and the results are strong. As shown in Section 4, the proposed BTR algorithm could greatly outperform state-of-the-art baselines in two classic benchmarks and handle three hard and complex modern games with a desktop PC.
3. The paper includes extensive ablation studies and experimental data. Section 5 presents a detailed analysis of the performance and impact of each component of the BTR algorithm, providing readers with insights into the sources of the algorithm's performance gains. Additionally, the authors include complete experimental results and settings in the appendix, helping to clarify any potential confusion or misunderstanding for readers.

### Weaknesses
1. The BTR integrates six improvements from existing RL literature to Rainbow DQN. While the algorithm demonstrates strong performance, its novelty might appear limited.  Could you further clarify the novelty of this work? Or specifically, could you briefly discuss if there is any challenges in integrating these existing improvements into the BTR algorithm?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a variant of Rainbow that adds further architectural and algorithmic improvements to improve not only the agent's score but also to increase its training speed to around 3x what has been previously reported, while running it on top-notch consumer hardware. Finally the authors also show that their improved version of rainbow can deal with modern games with complex graphics and physics.

### Strengths
The presentation is overall clear, the methodology is sound, and the results are compelling. Both extensive use of ablations, and the connection to other important metrics related to pathologies in Deep RL algorithms are an example that more papers should follow.
The appendices are also data rich, showing ablations' performances on each of ALE's 60 games, and even having one appendix about things that were tried but did not lead to improvements in performance, which may help others not repeat the experiments.

### Weaknesses
1. Adaptive Maxpooling is never defined. It's not a common layer in reinforcement learning and it's never defined in the paper, in fact skimming (Schmidt and Schmied, 2021) that layer is also not defined, I believe this is the only seious weakness in the paper's presentation, but still I believe it is a serious weakness (though hopefully the authors can fix it and so I can increase their grade).
2. There are at least 2 relevant citations missing, "Spectral Normalisation for Deep Reinforcement Learning: An Optimisation Perspective" when talking about Spectral Normalisation, and "On the consistency of hyper-parameter selection in value-based deep reinforcement learning" when talking about the need for tuning Deep RL hyperparameters and the benefits of using layer norm between dense layers.
3. I believe it's slightly misleading to not specify "a high-end PC" when talking about the kind of machine that can run the algorithm in 12 hours (4090 RTXs are quite expensive, and i9s are Intel's high-end consumer line)
4. I believe a more direct comparison with Schmidt and Schmied, 2021 is warranted, given its foundational importance to the paper.
5. Using only 3 seeds while having a large increase in the number of tuned hyperparameters weakens the validity of the results as explained in "Empirical Design in Reinforcement Learning", though at the same time the analysis of metrics beyond simply the score and the extensive use of ablations help.

### Questions
1. What exactly is adaptive maxpooling? Would it be possible to add a description of it with either an equation, pseudo-code, or diagram?
2. Where did the formula 0.05/batch_size for Adam's epsilon come from?
3. The final algorithm has a considerable number of hyperparameters, would it be possible to discuss a bit which ones are the most important to tune should someone try to apply this algorithm to a new domain?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper combines several different RL improvements to a single algorithm, with a focus on high performance with reasonable computational requirements. In doing so, they find that their approach achieves a new SoTA (not including recurrent methods), while being able to be run on a desktop machine in under a day.

They analyse the factors that led to this performance in detail through several ablations.

Overall, this paper makes rainbow/dqn-type methods more accessible to non-industry labs

### Strengths
- This paper gives RL researchers a way to do pretty well in atari without expending too significant computational resources.
- They perform ablations on their individual changes to identify what helps and what has the most effect on performance/walltime. This is quite useful.

I am not giving this a lower score because I think making RL more accessible is worthwhile, and this paper takes a step towards this, and further analyses many of these independent components to see what their effect is. I am not giving a higher score because I think the paper's significance does not warrant it.

### Weaknesses
- To me it is unclear if 12 hours is for all games or just 1.
- I wonder how this fits in with the recent trend of hardware-accelerated RL (see e.g., Stoix/PureJaxRL/Gymnax and all of the hardware-accelerated environments). Does that line of work better achieve the goal of making RL more accessible? In that setting, the environment is often run entirely on the GPU, leading to hundreds or thousands of times speedups.

### Questions
- The 12 hour number/other timings, is that the total time it takes to train BTR on a single game or on all 57 games?
- It seems like you made quite a few hyperparameter choices (e.g. how often to update, etc.) Do you use the same values for each domain?
- What is the shaded area in the plots? If it is standard deviation it seems like the proposed BTR algorithm is very inconsistent across seeds. Could you elaborate please/maybe provide results for individual seeds?
- Figure 3 does show that you can apply your approach to other games, which is great. I would really like to see some point of comparison, however, to act as a reference point. For instance, run vanilla PPO or DQN or Rainbow as a baseline.
- Why is fig 4 using raw score as the y-axis, as opposed to e.g. normalised?
- Figure 4 is somewhat hard to follow as there are so many lines and it seems like most of them overlap quite a lot.
- Is it feasible to run rainbow with vectorisation? This is not that crucial, it just seems like something obvious to run given figure 5, where vectorisation is the main speedup factor.
- Table 2: Would be nice to have another method, e.g. rainbow or DQN to act as a reference point.
- One recent work that seems to have a similar purpose is "Simplifying Deep Temporal Difference Learning" (https://arxiv.org/pdf/2407.04811). It seems like they use vectorisation as well to achieve large speedups. More importantly, however, is that they primarily use JAX---which is becoming increasingly common in RL, and is reducing computational load significantly/making RL more accessible to compute-poor labs/institutions. Could you please comment on a few things
	- How does this paper's score compare to yours?
	- How does the walltime compare to yours?
	- What do you see as the benefits/disadvantages of this hardware accelerated paradigm compared to the more classic approach you are taking?
- I know it is not usual in these types of papers but I would really appreciate a PPO comparison, both in terms of walltime and performance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present Beyond the Rainbow (BTR), an algorithm combining advances in Q-learning based approaches to Atari developed since Rainbow. 

The authors train their agent on Atari, Procgen and 3 games which aren't well-established benchmarks in RL (Super Mario Galaxy, Mario Kart and Mortal Kombat). They run ablations on their method and demonstrate that the Impala architecture contributes the most to their method's performance. They also demonstrate that vectorization of the environment is key to the faster runtime of their algorithm.

### Strengths
The paper has a number of positive points:
- The core idea of trying to achieve strong performance using Q-learning on a desktop PC has significant merit and would constitute an interesting contribution
- The introduction of new games to evaluate on is interesting and the games chosen would make good potential benchmarks.
- The paper is easy to follow and clearly written

### Weaknesses
I slightly feel for the authors of this paper. I would like to be able to commend the paper on its empirical results, or the performance on the new environments, but the results are not presented scientifically enough for me to do that, and so I can't recommend acceptance at this venue.

To make my objections more concrete:
- In Figure 2, the authors claim that their method outperforms the red baseline, but this is plainly not the case from the plot. The error bars so significantly overlap the red line there is no way this result is significant. 
- The authors do not aggregate their results in accordance with recommended practice [1]. Although they use the inter-quartile mean, they do not provide bootstrapped confidence intervals to estimate errors and do not seem to provide errors in their baseline results. This issue appears in Figures 1 and 2. As far as I know, the authors do not state what the error bars in Figures 1 and 2. If the plotted error bars are standard 
- While the evaluation of their method on new games is nice, I can't take any information away from this without even a semblance of a baseline. Training an RL policy on Wii games has no intrinsic scientific value -- it is only by contextualisation of a baseline that this would be a compelling result. Similarly, the authors provide no error bars in this domain.
- Figure 4 again because of the way the results were processed provides almost no information. Atari-5 [2] provides a way to estimate the median given performance on those 5 games. But this is only after the application of a regression procedure. Without the application of this summary metric, it is just not clear what to take away from these results. This figure does not even present human normalised scores, as is standard. This Figure should therefore be replaced by a plot of the regressed median for Atari-5 with bootstrapped confidence intervals. The authors can use rliable [1] for this.
- Again, the analysis in Section 5.2 *should* be compelling and interesting reading, but it's just not done thoroughly enough. Figure 6 is presented without error bars and so are the results in Table 2 and the IQM in Table 3. It's just not possible to believe the authors' conclusions on their work without any estimates of error. 
- Additionally, the authors use dormancy [3], but set a threshold of 0.1. Although resetting dormant neurons was shown to improve performance, neurons with a small activation are not in themselves a problem! A neuron followed by a ReLU activation that always outputs 0 is not learning, which clearly constitutes a problem, but a neuron that outputs a small value is still perfectly plastic. The dormancy results therefore also aren't a proxy for any form of plasticity. 
- The authors make multiple claims about their method being "state-of-the-art for a desktop PC" (or similar). These should be removed from the paper as they are just impossible to verify. Even as an expert, I do not know the hardware that every paper ran experiments on and whether it would be possible to run it on a desktop PC, and it is not a claim that can be clearly backed-up. I note that the authors did not do all their experimentation on a desktop PC, but only claim that their method can run on one effectively.

### Questions
See weaknesses.


Overall, this work is just not good enough in its current format. I recommend that the authors fix the presentation of the results, especially adding error bars and effective aggregation using a tool like rliable. Given the significant problems with every figure and table in the main body of the paper, this work is not good enough for this venue in its current form and would require wholesale changes to fix that.

[1] Deep Reinforcement Learning at the Edge of the Statistical Precipice. Agarwal et al. Neurips 2021.

[2] Aitchison, Matthew, Penny Sweetser, and Marcus Hutter. "Atari-5: Distilling the arcade learning environment down to five games." International Conference on Machine Learning. PMLR, 2023.

[3] Sokar, Ghada, et al. "The dormant neuron phenomenon in deep reinforcement learning." International Conference on Machine Learning. PMLR, 2023.

### Soundness
1

### Presentation
2

### Contribution
3
