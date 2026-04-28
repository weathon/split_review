# Successor Representations Enable Emergent Compositional Instruction Following

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Behavioral cloning (BC) has seen widespread adoption in scalable robot learning pipelines. These methods struggle to perform compositional generalization, where a new out-of-distribution evaluation task can be viewed as a sequence of simpler in-distribution steps. We augment goal-conditioned BC methods with a temporal alignment loss that learns to associate present and future states. This approach is able to generalize to novel composite tasks specified as goal images or language instructions, without assuming any additional reward supervision or explicit subtask planning. We evaluate our approach across diverse tabletop robotic manipulation tasks, showing substantial improvements for tasks specified with either language or goal images.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates a novel approach called Temporal Representation Alignment (TRA) to enhance compositional generalization in robotic tasks, particularly for multi-step instruction following and goal-oriented tasks. TRA emphasizes learning representations that align temporally across different states, goals, and language instructions, which enables agents to perform complex, sequential tasks without additional planning. The method is tested on various robotic manipulation tasks in the BridgeData setup, showing significant improvements in compositional performance compared to other baseline methods like AWR and LCBC.

### Strengths
1. **Innovation in Representation Learning**: TRA introduces a creative approach to compositional generalization by structuring the alignment of temporal representations, which minimizes reliance on explicit planning or RL-based strategies.

2. **Zero-shot Compositionality**: TRA’s ability to generalize to unseen task combinations without retraining is a notable achievement, providing significant potential for scaling robotic applications in real-world, dynamically changing environments.

### Weaknesses
1. **Limited Scope of Task Complexity**: Although TRA shows compositionality, the tested tasks focus on relatively simple manipulations. More complex or multi-agent settings might challenge TRA's capabilities. (Most of them are pick-and-place)

2. **Dependence on Goal Representation Quality**: Success in tasks depends heavily on the quality and specificity of goal representations, which may require fine-tuning for certain task types.

3. **Missing Ablation Studies**: The authors have no ablation study on object-level instruction following and task-level instruction following since the work focuses on languange Instruction following. For example, "move the bell pepper to the bottom right of the table" v.s. "move the bell pepper to the bottom left of the table". It might overfit or replay the action sequence in the replay buffer.

### Questions
1. **Poor Baselines**: Why not choose diffusion policies for imitation learning baselines?

2. The alignment is too similar to the VIP method, why not give more explanations? (The author cites the VIP, but doesn't give any descriptions or comparisons)

3. It seems the font of the paper is wired. Have you chosen the right style?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a self-supervised loss aimed at improving compositionality in language- and goal-image conditioned robot policies. The approach leverages contrastive learning with the NCE objective between states of similar trajectories while simultaneously aligning goal embeddings from language and image inputs. This improves compositional generalization and is tested in 4 experiment settings in the real world.

### Strengths
- simple extension to improve learning of policies using SSL

- strong results in real robot experiments

- easy to use for existing policy frameworks

### Weaknesses
Weaknesses:
- Technical omissions:
    - No theoretical foundation for why temporal alignment should enable task compositionality is provided. Experiments on a single dataset do not provide enough empirical evidence to justify the claims of the paper. 
    - Given the weak theoretical justification of the made claims experiments on a single dataset are not enough to verify those. More experiments in reproducible benchmarks are necessary or detailed theoretical discussion why aligning similar states should result in this compositional generalization.
- Limited experimental validation:
    - Evaluation restricted to a single real world kitchen dataset
    - No testing in reproducible benchmark environments (e.g., CALVIN, SIMPLER or similar simulators) that would enable fair comparison with future work. Given the huge performance gain of TRA compared to GRIF and other baselines I am interested to see how it performs in other domains.
    - Table 1 does not provide evidence for the made claims as just predicting trajectories without actual rollouts can be very misleading and robotics and does not have a clear correlation with success rate. 
- Writing and clarity issues:
    - Incomplete sentence in Chapter 3 disrupts flow
    - Complex, run-on sentences throughout make technical content difficult to understand
    - Overall writing requires substantial revision for clarity and coherence
    - Loss function lacks clear explanation and intuition

Summary: 
The paper's potential contributions are undermined by unclear writing, missing technical details, and limited experimental evaluation. The paper does not provide any theoretical justification on the gains of the method. Since experiments are limited to a single non-reproducible real world benchmark, there is not a lot of empirical evidence to support these claims. While I acknowledge the number of real world experiments and the related effort to test these, they are still coming from a single dataset. Given the big performance gains shown (+60% compared to second best baselines in a setting), I expect to see similar results in other simulation domains. 
Major revisions needed to address the following issues:
1. Improve writing clarity and technical explanations
2. Expand experimental validation across multiple environments
3. Include theoretical justification for the proposed claims

### Questions
- Can you test the proposed method on established in reproducible simulation benchmarks like CALVIN and SIMPLER to provide more empirical evidence for the claims of the paper? 

- How big is the computation overhead for the proposed method?

- Can you provide some theoretical analysis to why the proposed ssl loss enables compositional generalization by aligning similar states? 

- Performance of GRIF reported in the original paper for the same task is very different compared to the reported values here: "put the spoons on towels" from GRIF 0.9 and here "put the spoon on the towel" 0.2. How do you explain these big gaps?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Temporal Representation Alignment (TRA), a method for enabling compositional generalization in robotic manipulation tasks without explicit subtask planning or reinforcement learning. The key idea is to add a temporal alignment loss that encourages the policy to learn structured representations that capture temporal relationships between states. The authors evaluate TRA on a range of tabletop manipulation tasks using the BridgeData setup, showing improved performance on compositionally novel tasks specified through either language instructions or goal images. The main contribution is demonstrating that adding this auxiliary temporal alignment objective during training can enable a policy to implicitly decompose and execute multi-step tasks, even when the specific sequence of steps was never seen during training.

### Strengths
1） Novel approach that achieves compositional generalization without requiring explicit hierarchical structure or planning, demonstrating that temporal alignment of representations is sufficient
2） Comprehensive empirical evaluation across multiple task types and comparison against strong baselines
3） Clear ablation studies that validate the importance of the temporal alignment component

### Weaknesses
## Comparative Analysis:

- Need stronger justification for why TRA is preferable to VLM/LLM-based decomposition approaches


## Evaluation Limitations


- Tasks are limited to relatively simple manipulation scenarios in a highly controlled environment

- Missing comparison with recent language model-based task decomposition methods (e.g., RT-H)


## Methodological Comparison Gaps:

- The paper's main contribution focuses on compositional long-horizon tasks, but doesn't adequately compare against state-of-the-art VLM/LLM-based task decomposition methods
- No clear demonstration of advantages over approaches that use large language models for task decomposition combined with foundation models like Octo or OpenVLA for sub-task execution
- Missing analysis of computational efficiency compared to VLM/LLM-based approaches


## Insufficient Analysis:

- Limited theoretical analysis of when/why temporal alignment enables compositional generalization

### Questions
1. How sensitive is the method to the choice of discount factor γ in the temporal alignment objective? Was any ablation done on this hyperparameter?



2. For the semantic generalization experiments (Scene C), how robust is the method to variations in object appearance beyond what was seen in training?

3. How does TRA compare to recent LLM-based task decomposition methods (like RT-H) in terms of:




4. Could you provide quantitative comparisons with methods that use LLMs for task decomposition combined with foundation models (like Octo/OpenVLA) for execution?

5. What advantages does TRA offer over LLM-based decomposition approaches for long-horizon tasks? Please provide concrete examples and experimental results.

6How does the method scale to more complex real-world scenarios with greater environmental variation and uncertainty?

### Soundness
3

### Presentation
3

### Contribution
3
