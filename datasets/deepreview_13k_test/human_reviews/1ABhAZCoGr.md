# DYSTIL: Dynamic Strategy Induction with Large Language Models for Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Reinforcement learning from expert demonstrations has long remained a challenging research problem, and existing methods resorting to behavioral cloning plus further RL training often suffer from poor generalization, low sample efficiency, and poor model interpretability. Inspired by the strong reasoning abilities of large language models (LLMs), we propose a novel strategy-based neuro-symbolic reinforcement learning framework integrated with LLMs called DYnamic STrategy Induction with Llms for reinforcement learning (DYSTIL) to overcome these limitations. DYSTIL dynamically queries a strategy-generating LLM to induce textual strategies based on advantage estimations and expert demonstrations, and gradually internalizes induced strategies into the RL agent through policy optimization to improve its performance through boosting policy generalization and enhancing sample efficiency. It also provides a direct textual channel to observe and interpret the evolution of the policy's underlying strategies during training. We test DYSTIL over challenging RL environments from Minigrid and BabyAI, and empirically demonstrate that DYSTIL significantly outperforms state-of-the-art baseline methods by 17.75% success rate on average while also enjoying higher sample efficiency during the learning process.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a way to leverage expert data for behavior cloning and RL to craft policies that are conditioned on a set of strategies which hopefully encode generalizable behavior. The authors claim that existing methods on BC+RL suffer from important issues (poor generalization, sample efficiency and interpretability), which the proposed approach can address. In particular, the authors train an open source LLM on expert data through behavior cloning by conditioning the policy on strategies that are devised by a teacher LLM (GPT-4o). The model is then trained with RL data, leading to a new list of strategies, which is then used to further guide the agent. The strategies are selected by verifying whether they help the model achieve higher performance. On a set of four environments, the paper shows that the proposed approach improves upon previous baselines.

### Strengths
The paper identifies an important area for research, that is, how to combine expert data and reinforcement learning. The proposed approach is different from some of the more traditional ways of leveraging both kinds of data, building on the strengths of LLMs to devise high level strategies.

### Weaknesses
The empirical setup brings a lot of questions. A major red flag is that there are no error bars at all and no mention of the number of seeds. Please see the rich literature on the subject of statistical relevance in decision making [1, 2].  For the tasks themselves, it is not clear why some choices are made. For example, is the max_steps=60 the default number? In the codebase of Minigrid I can see that the default value is set of 100, so an explanation would be necessary. 

Another important area of doubt is concerning the strategy for updating the list of strategies. Currently, this is a complicated method that relies on evolving the strategy list with respect to performance. Why is such a complex method used? How sensitive is it to the different hyperparameters? How does it compare to simply asking GPT-4o for a new list of strategies? These are key questions that are completely unanswered.

The authors claim that generalization is a limitation of BC+RL, yet the paper does not show any experiments on generalization. This would be a great opportunity for the authors to show the compositionally that is afforded by language. It would also be a great opportunity to address another important are of concern: how much does the list of strategies affect the model? How much can you steer its behavior by changing the list? At the moment, it really isn't clear that the RL agent really responds to this conditioning.

The performance numbers reported for some of these tasks seems very low, which also comes from a limited set of baselines. In particular, I would really like to see the performance of GPT-4o on these tasks. Another family of baselines would be to compare to LLMs generating goals for the RL agent [3], which is relatively close to the ideas presented here. Notice that in that paper the results are significantly better than the numbers presented here.

### Questions
In the introduction, it is mentioned that BC+RL can't enable an RL agent tot acquire higher level abstractions and understanding of the RL task. This is not only very loosely defined, but likely not true. Do the authors mean that an RL agent wouldn't acquire an understanding that can be translated in language? This is very different than the claims being made.

Why use GPT-4o for generating strategies? How does Llama 3.1 compare? It would be much more preferable to have it be the same family of models.

The word "neuro-symbolic" is used to characterize the method, but is it really a neuro-symbolic method? To me it just seems like the neural network is additionally conditioned on language. This qualifier seems a bit of stretch.

[1] Deep Reinforcement Learning at the Edge of the Statistical Precipice, Agrawal et al., 2022

[2] Deep reinforcement learning that matter, Henderson et al., 2018

[3] Code as Reward: Empowering Reinforcement Learning with VLMs, Venuto et al., 2024

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed DYSTIL which integrates LLMs into a strategy-based neuro-symbolic reinforcement learning framework. The method aims to address the generalization issue of RL.

### Strengths
1. The paper is well-written and easy to follow.
2. The authors provide illustrations of their method, which makes it clear to how it works.

### Weaknesses
1. My biggest concern is the limited novelty and experiments. There are many papers that proposed strategy-generating methods as a summary or reflection of the past trajectories, such as [1]. The authors failed to discuss the similarities and differences between their method and these works.
2. The experiments are only conducted in several environments from Minigrid. Whether this approach can generalize and how to design each component for different tasks remains unclear. Besides, the compared baselines are limited. I strongly encourage the authors to do literature reviews and add more baselines such as [1].

[1] Shinn et al., Reflexion: Language Agents with Verbal Reinforcement Learning.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces DYSTIL, a neuro-symbolic reinforcement learning framework that integrates large language models (LLMs) to dynamically induce and internalize textual strategies, enhancing policy generalization and sample efficiency. By leveraging LLMs to provide strategy guidance based on expert demonstrations, DYSTIL improves interpretability and transparency in reinforcement learning tasks. Empirical results demonstrate that DYSTIL outperforms state-of-the-art methods by 17.75% in success rate across complex environments like Minigrid and BabyAI.

### Strengths
- Quality: The paper presents ideas through clear text and figures, aiding understanding of the overall concepts.
- Significance: This paper demonstrates that the proposed method outperforms two baselines in grid-world environments.

### Weaknesses
- Scalability: DYSTIL’s reliance on closed-source, SOTA LLMs (e.g., GPT-4o) raises issues of scalability, reproducibility, and accessibility, especially for the model which needs to recurrently call strategy-generating LLM for each iteration. The paper also lacks ablation studies using different LLMs, which would help clarify the flexibility of using other LLMs for this work.

### Questions
1. Can DYSTIL generalize to other language-based decision-making tasks, such as those solved by ReAct (e.g., ALFWorld)? How could you extend your framework to accommodate these tasks?
2. In the GLAM baseline paper[1], the average success rate converges and reaches high performance (i.e., over 80%) at approximately 1e6 steps. Is there a reason you chose 1e5 steps for evaluation? What causes the discrepancy between your configuration and results compared to theirs?
3. In the ablation study, dynamic strategy updates are removed, so there is no $\mathcal{L}_2$ in the static strategy settings. Does this result in more iterations compared to the proposed method based on the same training frames? I also want to confirm whether $\mathcal{L}, \mathcal{L}_1, \mathcal{L}_2$'s executions are all counted in training frames.
4. Can the strategies generalize to novel tasks? For instance, would training on Unlock Pickup help in solving Key Corridor?

[1] Carta et. al. "Grounding large language models in interactive environments with online reinforcement learning". In Proceedings of ICLR 2023.

### Soundness
2

### Presentation
3

### Contribution
2
