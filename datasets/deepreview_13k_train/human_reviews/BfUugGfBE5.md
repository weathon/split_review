# Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Recent studies have demonstrated that Transformers can perform in-context reinforcement learning (RL) by imitating a source RL algorithm. This enables them to adapt to new tasks in a sample-efficient manner without parameter updates. However, since the Transformers are trained to mimic the source algorithm, they also reproduce its suboptimal behaviors. Model-based planning offers a promising solution to this limitation by allowing the agents to simulate potential outcomes before taking action, providing an additional mechanism to deviate from the source algorithm's behavior. Rather than learning a separate dynamics model, we propose Distillation for In-Context Planning (DICP), an in-context model-based RL framework where the Transformer simultaneously learns environment dynamics and improves policy in-context. With experiments across a diverse set of discrete and continuous environments such as Darkroom variants and Meta-World, we show that this method achieves state-of-the-art performance, requiring significantly fewer environmental interactions than the baselines including both in-context model-free counterparts and existing meta-RL methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a model-based in-context reinforcement learning method called Distillation for In-Context Planning (DICP). With a dynamics model for planning, it provides the ability to deviate from the source algorithm's behavior. The authors show that DICP achieves better performance  on Darkroom and Meta-World benchmarks.

### Strengths
- The paper is clearly written, allowing readers to follow the main arguments.
- It provides a comprehensive experiments and ablations to demonstrate the effectiveness of DICP compared with the model-free counterparts.

### Weaknesses
I think the experimental results of this paper do not strongly support the main motivation. The authors claim that: “Model-free in-context reinforcement learning methods are trained to mimic the source algorithm, they also reproduce its suboptimal behaviors. Model-based planning offers a promising solution to this limitation by allowing the agents to simulate potential outcomes before taking action, providing an additional mechanism to deviate from the source algorithm’s behavior.” However, in the experiments section, DICP does not show significant performance advantages over its model-free counterparts. For example, as shown in Appendix B, the success rate of DICP-AD compared to AD only improves from 68% to 69%, and DICP-IDT compared to IDT only improves from 75% to 80%. Therefore, I believe model-based planning does not significantly enhance the policy beyond the source behavior. The relatively small performance gains, particularly for DICP-AD, raise questions about the practical benefits of the proposed model-based approach. The core argument for using a dynamics model to escape suboptimal behavior is not convincingly demonstrated by the reported success rate improvements. The fact that DICP-AD shows minimal improvement suggests that the learned dynamics model may not be sufficiently accurate or that the planning horizon is not long enough to effectively deviate from the source policy. Furthermore, while DICP-IDT shows a more noticeable gain, it is still not a dramatic improvement, leaving doubt about the general effectiveness of this approach across different base models.

### Questions
- Could the authors explain why improvements of DICP-AD over AD is not significant?
- Is it possible to evaluate on more challenging benchmarks like ML10?

### Soundness
3

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
2

### Summary
The paper proposes a novel method called Distillation for In-Context Model-Based Planning (DICP) to improve the efficiency and effectiveness of in-context reinforcement learning. DICP leverages a learned dynamics model to predict the consequences of actions and uses this information to plan more effectively.

### Strengths
-Transformer simultaneously learns environment dynamics and improves policy in-context

-Avoid sub-optimal behavior of the source algorithm

### Weaknesses
 -One of the flaws in model based planning is that the model might not be perfect. Errors of the world model might lead to sub-optimal policies as well which haven’t been discussed in the paper.

-Some analysis on how many times sub-optimal behvior from source algorithm was discovered and your approach was able to learn the optimal policy would be important to ensure extra computation of model based planning is worth it.

### Questions
1) Can you comment on how much the trade-off between performance vs computation is required in your approach and other comparisons? Do the gains outweigh computational expense?

2) What happens when the world model is incorrect? How is the performance affected? What steps are taken to ensure model-based planning can be accurate?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper extends the use of decision transformers for in-context meta-task learning to incorporate model-based planning. The main innovation here is to have the transformer output predicted state values (r, o, R) in addition to the next action, and to use this state-transition model to select better actions. This can be applied to multiple different transformer-based agents and yields improvements both in terms of sample efficiency and overall score.

### Strengths
- Advances the performance of in-context RL, an exciting recent direction
- Provides a mechanism to overcome suboptimal behaviors inherited from the source RL algorithms
- Achieves state of the art on Meta-World, compared with a large variety of RL and in-context RL algorithms
- This is an important new innovation that makes sense, and as far as I can tell (though I do not have full knowledge of the literature) is the first demonstration of incorporating model-based planning into transformer-based in-context RL. 
- This seems like a well-done paper with a straightforward but impactful contribution.

### Weaknesses
 - Nothing major.

### Questions
- How exactly are the actions sampled, and what is the sensitivity to the sampling approach? 

- What do you think would happen if the imitation loss and dynamics loss trained two separate models?

- I would be interested in more discussion of how this method might apply to online learning. For example, how might it interact with intrinsically-rewarded exploration to improve the world model? How much does this method depend on the quality of the offline dataset? How effectively would this approach adapt to an environment where the dynamics change?

- Would MCTS perhaps have benefits relative to beam search? Is there a way to not build the whole planning tree as an initial step, or what is the advantage to doing so?

- Are there scenarios where having a world model might detract. For example, what happens if the world model is not accurate enough?

- What are possible explanations for why model-based performs worse on Pick-Out-Of-Hole?

### Soundness
4

### Presentation
4

### Contribution
4
