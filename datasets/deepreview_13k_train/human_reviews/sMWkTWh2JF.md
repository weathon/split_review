# ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
\looseness=-1 Intelligent embodied agents need to quickly adapt to new scenarios by integrating long histories of experience into decision-making. For instance, a robot in an unfamiliar house initially wouldn't know the locations of objects needed for tasks and might perform inefficiently. However, as it gathers more experience, it should learn the layout of its environment and remember where objects are, allowing it to complete new tasks more efficiently. To enable such rapid adaptation to new tasks, we present \method, a new approach for in-context reinforcement learning (RL) for embodied agents. With \method, agents are capable of adapting to new environments using 64,000 steps of in-context experience with full attention while being trained through self-generated experience via RL. We achieve this by proposing a novel policy update scheme for on-policy RL called ``partial updates'' as well as a Sink-KV mechanism that enables effective utilization of a long observation history for embodied agents. Our method outperforms a variety of meta-RL baselines in adapting to unseen houses in an embodied multi-object navigation task. In addition, we find that \method is capable of few-shot imitation learning despite never being trained with expert demonstrations. We also provide a comprehensive analysis of \method, highlighting that the combination of large-scale RL training, the proposed partial updates scheme, and the Sink-KV are essential for effective in-context learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces ReLIC (Reinforcement Learning In Context), a new approach that enables embodied AI agents to adapt to new environments using up to 64,000 steps of in-context experience. ReLIC addresses two key challenges in scaling in-context reinforcement learning: efficiently training with long context windows and effectively utilizing visual information from multiple episodes. To solve these challenges, the authors introduce "partial updates," a novel policy update scheme that allows more frequent learning during long rollouts, and "Sink-KV," a modification to transformer attention that helps the model selectively attend to relevant information in long sequences.

The authors evaluate ReLIC on an extended version of object navigation where agents must find multiple objects in unseen house layouts. ReLIC significantly outperforms baseline approaches, achieving a 43% success rate compared to 22% from the closest baseline after 15 episodes of in-context experience. The method also demonstrates an unexpected capability for few-shot imitation learning despite never being trained with expert demonstrations. Through extensive ablation studies, the authors show that both partial updates and Sink-KV are crucial for effective learning, and that sufficient training scale is necessary for in-context learning capabilities to emerge. The approach also performs well on existing benchmarks like Darkroom and Miniworld tasks, showing better and faster adaptation compared to prior work.

### Strengths
1. Strong Empirical Results: The method achieves substantial improvements over baselines, nearly doubling the success rate (43% vs 22%) in challenging navigation tasks. The results are thoroughly validated across multiple environments (EXTOBJNAV, Darkroom, Miniworld) with comprehensive ablation studies.
2. Scalability: The paper demonstrates impressive scaling capabilities, showing that their method can handle up to 64,000 steps of context - a significant improvement over previous approaches. More importantly, they show that models trained on shorter contexts (4k steps) can generalize to much longer contexts (32k steps) at inference time.

### Weaknesses
1. Limited Success Rate: Despite significant improvements over baselines, the absolute performance (43% success rate) is still relatively low for practical applications. The paper doesn't thoroughly discuss why this ceiling exists or potential paths to improve it. Specifically, the paper lacks an analysis of the factors limiting performance in the ExtObjNav task, such as the agent's ability to explore effectively, the quality of its visual perception, or the limitations of the in-context learning mechanism itself. A more detailed investigation into these bottlenecks would be beneficial.

2. Computational Cost: The method requires substantial computational resources - 12 days of training on 4 NVIDIA A40 GPUs. This high computational requirement could limit the practical applicability and accessibility of the approach, especially for researchers with limited resources. The paper does not provide sufficient detail on the computational bottlenecks, such as the transformer's memory usage or the overhead of partial updates, making it difficult to assess the feasibility of optimizing the implementation.

3. Task Limitation: The evaluation focuses primarily on navigation tasks with discrete action spaces. There's no exploration of how the method might extend to continuous action spaces or more complex tasks like manipulation, limiting our understanding of the approach's broader applicability. The paper does not discuss the potential challenges of applying ReLIC to continuous control, such as the need for different action parameterizations or the increased complexity of the policy optimization process. The lack of experiments on manipulation tasks also leaves open questions about the method's ability to handle more complex state spaces and action dependencies.

4. Missing Related work: 
Retrieval-Augmented Decision Transformer: External Memory for In-context RL, Schmied et.al
	 - Work is quite similar to yours. It would be interesting if the authors could point out the differences in the related work section. This will improve the paper.

### Questions
1. Scalability and Practical Applications: Given the high computational requirements (12 days on 4 A40 GPUs), what approaches have you considered to make ReLIC more practically applicable? Could techniques like model distillation or more efficient architectures reduce these requirements while maintaining performance?
2. Beyond Navigation: The current work focuses on discrete action spaces in navigation tasks. Have you explored how ReLIC could be extended to continuous action spaces or more complex tasks like manipulation? What modifications would be needed to handle such scenarios?
3. Emergent Few-shot Learning: The emergence of few-shot imitation learning capabilities without explicit training is intriguing. What mechanisms in ReLIC enable this capability, and how could it be enhanced? Have you analyzed how the quality of demonstrations affects performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
* This paper proposes a new in-context RL approach with 64K historied steps. They introduce partial update schemes to solve sample inefficiency problems and Sink-KV mechanism to address long observation history.

### Strengths
*  The problems proposed by the paper are meaningful. Generalization is a long-term goal for embodied AI. In context learning with longer prompts may be a potential solution.
*  This paper is well-structured, conducts rich experiments and achieves great performance.

### Weaknesses
 *  The description for "partial update" is confusing. Providing pseudocode would be good for understanding.
*  The contributions of the paper are confusing. This paper proposes two ways to solve long in-context RL: partial update and SINK-KV. "Partial update" is more like a training trick and "Sink-KV" is proposed by previous works. In the appendix, the paper explaints "Sink-KV" will help the policy for exploration. This is interesting and it should be place in the main paper.
*  Lack of some comparisons. Like transformer with multi episodes and DPT in ExtObjNav. 
*  Environments used in experiments are too simple and they are all navigations tasks. It would be interesting to include manipulation benchmarks like MetaWorld.
*  Inefficient and large GPU memory for long context length. What is the inference speed for ReLIC and other baselines?
*  This paper emphasise 64K in the title and introduction. But in the experiment sections, all results are evaluated under small context length.

### Questions
*  See weakness.
*  In the Darkroom and miniwork experiment, all baselines have very low performance (0 success rate) with no context while ReLIC has higher performance (30% success rate). Is it normal? And DPT can get a very higher improvement with 20 in-context episodes.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces ReLIC, a framework designed to extend in-context learning capabilities to embodied AI agents. ReLIC focuses on enabling agents to utilize up to 64,000 steps of contextual experience, aiming to allow rapid adaptation in unseen environments, especially for multi-object navigation tasks. This is achieved through two components: (1) Partial Updates, a policy update scheme that incrementally adjusts the policy within rollouts, and (2) Sink-KV, a mechanism for efficient attention management in transformers, which optimizes long-sequence processing by adding learnable sink key-value vectors in attention layers.

### Strengths
1. The paper is generally well-written and easy-to-understand.
2. Experiments show that the proposed approach is effective.
3. Hyperparameters and algorithm details are provided for reproducity.

### Weaknesses
1. The two major novel components of the paper as claimed by the authors are the partial updates and Sink-KV. For the former one, if I understand correctly, it is a very common technique used in common RL training (I don't if it's the same case for in-context RL as I'm not familiar with its literature), namely, update the policy/value in the middle of an episode to increase training frequency. For Sink-KV, it seems to be interesting but I'm not familiar with the literature exploring the architecture of transformer so I don't how novel this is, but one thing that is not clear to me is that, why this design especially helps in-context RL training? What makes it special compared to using it in vision/language tasks?

2. For the experiments, the author mainly compared their method to meta-rl baselines and different variants of their method - while this is good, I would expect to see how the proposed method compared to other in-context RL baselines. 

3. The emergent imitation learning results are not that surprising to me - a lot of recent work  do pretraining with imitation learning and then rl finetuning, the proposed scheme here is like first pretraining with rl then finetuning with imitation learning. This setting is also a little bit strange as in the real world case, if we have the expert demonstrations, pretraining on that usally greatly speed up RL.

4. std/error bar not included in the darkroom result plot and miniworld result plot

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2
