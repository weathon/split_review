# Genesis: Advancing Towards Efficient Embodiment Co-Design

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Embodiment co-design aims to optimize a robot's morphology and control simultaneously. 
Previous research has demonstrated its  potential for generating environment-adaptive robots.
However, the problem is inherently combinatorial and the morphology is changeable and agnostic in its vast search space, optimization efficiency remains complex and challenging to address. 
We prove that the inefficient morphology representation and unbalanced reward signals between the design and control stages are key obstacles against efficiency. In order to advance towards efficient embodiment co-design to unlock its full potential, we propose *Genesis*, which utilizes (1) a novel topology-aware self-attention architecture, enabling efficient morphology representation while enjoying lightweight model sizes; (2) a temporal credit assignment mechanism for co-design that ensures balanced reward signals for optimization. With our simple-yet-efficient methods, Genesis achieves average **60.03%** performance improvement against the strongest baselines. We provide codes and more results on the website: https://genesisorigin.github.io.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors investigate the problem of joint optimization of agent design and control with reinforcement learning. They propose that two outstanding problems for addressing this are imbalanced reward signals between the control and design generation steps and the effective use of morphology information. They address these two problems with two components. First, they address this by modifying the advantage function to give a better signal during design development. The latter is addressed by proposing the MoSAT layer, which uses self-attention instead of a graph neural network and an embodiment-aware positional encoding approach. Experimentally the combination of these components is necessary for performance benefits based on their results

### Strengths
Overall, the paper proposes several sound components that address their proposed problems (reward mismatch and using morphology information). Modifying the training objective for the design policy makes intuitive sense, at leas twith how the author's describe it. Self-attention mechanisms have been effective in other embodiment-aware research, so using these mechanisms seems a natural step for co-design and control methods. The authors also compare their positional embedding mechanism to prior works, which adds support to the benefit of their embedding approach. The experiments used to validate the components, and the author provides supporting materials support their claims

### Weaknesses
Our biggest concern is that although the proposed framework yields strong performance, the authors need to pay more attention to the novelty of their contributions. We point out, for example, that the author's "Topology Design Stage" sounds similar to the previous work in Transform2Act (Yuan et al., 2021, in their citations). Specifically, both approaches appear to use a graph-generating component and an attribute-generating policy to create the robot's morphology. The MoSAT layer is simply a typical Transformer Encoder layer, so it seems strange that the authors renamed a previously established neural network model. This renaming obscures the fact that the core mechanism is a standard self-attention module, which could lead to confusion about the actual contributions. Stating this explicitly would simplify their discussion on the MoSAT layers and allow more room for discussing other components. The reward signal modifications do not adequately provide readers with the intuition of the author's proposed solution in section 4.3. The description lacks sufficient detail on how the modified advantage function addresses the reward imbalance between design and control. In our estimates, the major contribution is merging these components into a single design and control deployment framework, which is a good contribution. Still, the components in themselves do not seem notably novel alone or need to be justified more clearly to this reviewer.

### Questions
1. What distinguishes the author's Topology Design Stage from the design stage in Transform2Act? They also seem to have a graph-generating component and attribute-generating policy. 

2. How is MoSAT different from a typical Transformer Layer?

3. What exactly is U_t in comparison to the value function V? 

4. How was 60.52% performance improvement calculated?

5. In the w/o TopoPE ablation, was any form of positional information provided? Also, is the adjacency information included explicitly in the limb embeddings?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a robotics co-design framework that co-optimized morphology and control using a Morphology Self-attention (MoSAT) architecture, inspired by transformers. It employs Topology Position Encoding (TopoPE) to enhance the integration of positional data within self-attention mechanisms. The framework optimizes these configurations through a Proximal Policy Optimization (PPO) approach, incorporating specialized credit assignments to accommodate both immediate control actions and long-term design adjustments.

### Strengths
The authors propose a new method to overcome the computationally heavy nested design of morphology and control of robotics systems. Based on the literature review provided, the authors have substantially improved the drawbacks of previous approaches, and the results are sufficient to prove it. The proposed method significantly will alter future research in the co-design domain.

### Weaknesses
I expect a big computational increase due to the 3 complex neural networks involved. The paper didn't talk about it or compare it with baselines. 
The robots and simulation environments used are toy problems and not sure how this can be applied to complex robotics systems like UGVs and UAVs.

### Questions
1. What are the computational demands of the MoSAT architecture, particularly when scaling to robots with a high number of limbs or complex joint structures? Is there a limit to the number of nodes (limbs) and edges (joints) the system can effectively manage? 
2. How well does the Topology Position Encoding (TopoPE) generalize across robots with significantly different morphologies? Are there any limitations in the encoding approach when dealing with highly irregular or non-standard robotic structures?
3. given the use of multiple networks (Topology Design, Attribute Design, and Control) within the Genesis framework, how is the synchronization of updates managed between these networks? Let's say with episode I, with timestep t that is not a terminal step, if a backpropagation is performed here. How does the t+1 work, does the morphology change and controls change?

### Soundness
3

### Presentation
4

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
This work tackles the problem of learning a control policy and improving the agent's morphology in a unified learning framework. The authors propose to improve both the morphology of the agent and the control policy via reinforcement learning.  Several previous works employed a combination of reinforcement learning for learning the policy and of evolutionary algorithms to improve the agent's embodiment, using a new neural network for each agent. Other papers used policies based on graph neural networks to enable weight sharing across morphologies, but suffered from inefficient communication between joints. With an attention-based policy, it is possible to both share the network's weights across different morphologies, and avoid the message passing bottleneck. The morphology self-attention architecture, paired with a mechanism to facilitate credit assignment for the policy improving the morphology, largely outperforms previous methods in co-evolving the agent's morphology and control policy.

### Strengths
The paper is well written and easy to follow. The motivation is clear: previous work employed certain design choices (specifically evolutionary algorithms, graph neural networks) which, if successfully replaced with more effective solutions (reinforcement learning and self-attention) should lead to a clear improvement, as indeed demonstrated by the final performance. The proposed framework required the introduction of new solutions for the positional encoding of the agent's joints and to improve the credit assignment for the "slower" reinfrocement learning process, which is the morphology improvement. Both problems have been successfully addressed. Therefore, the paper fills a a gap in this specific field, obtaining a large performance improvement over previous methods.

### Weaknesses
In the introduction and in the related work, this paper cites previous studies on policy-morphology co-evolution. However, the authors likely missed other papers proposing attention policies to deal with variable morphologies ([1] and [2]) and it would be important to at least compare MoSAT with those architectures. Furthermore, from the description of MoSAT I could not understand whether it is any different from a standard Transformer network. I would suggest explaining MoSAT in terms of its differences from a Transformer, rather than defining each component of the block.

The paper includes some details about methods introduced by other papers (e.g., details about PPO, or about the topology design, which seems identical to [3]), which could be shortened and the saved space used to better analyze the results. In fact, while the performance is convincing and the ablations satisfactory, the authors could draw inspiration from, e.g., the analysis in [4], to better grasp the effects of the morphology's evolution beyond the task performance.

The topology position encoding (TopoPE) is listed among the main contributions, so it would be good to better show its properties. For example, the authors claim that TopoPE is more stable than previous encodings when the morphology changes, but this claim is not supported by any specific experiment.

The modified GAE requires better explanation. For the "Control Stage", why is there a discounted advantage summed to the temporal difference? While for the Design Stage, U_t seems like a monte-carlo estimation of the reward, why using that instead of bootstrapping the value function?

Minor:
* line 080, facilitating -> facilitates
* line 139, an -> a
* line 242, "achieve the co-design process"?
* line 369, what exactly is inspired by BERT?
* line 443, Yuan et al. repeated
* line 463, I would rather express the size of the model in number of weights
* line 479, I would avoid sentences like "despite the impressive results of our approach"

### Questions
* How does TopoPE compare to other morphology encodings? E.g., the one used in [1]

* Is the morphology search space the same as in [2] (unimal)? What is different and why?

* How large is the delay in the Design stage? It is not obvious to me that the rewards come particularly delayed, unless the design stage has many steps. In fact, while the reward due to the updated design comes after some interactions of the agent with the environment, during the interaction there is no design decision being made, so this should not be perceived as a delay by the Design policy.

* How do the agents' morphologies look at the end of the training? What is their performance, e.g., compared to agents with the base morphology trained with RL? Can the learnt morphology be used to train a new agent with it?

[1] Trabucco, B., Phielipp, M., & Berseth, G. (2022, June). Anymorph: Learning transferable polices by inferring agent morphology. In International Conference on Machine Learning (pp. 21677-21691). PMLR.
[2] Gupta, A., Savarese, S., Ganguli, S. and Fei-Fei, L., 2021. Embodied intelligence via learning and evolution. Nature communications, 12(1), p.5721.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents "Genesis", a reinforcement learning (RL) framework for the co-design of robot morphology and control policies. Genesis addresses the main limitations of current methodologies which struggle with the high-dimensional design space and optimize the morphology separately from the control policy. The key contributions include (1) a temporal credit assignment mechanism to balance reward between morphology and control optimization and (2) a topology-aware self-attention mechanism for efficient morphology representation. Experiments across multiple environments and ablations demonstrate that Genesis significantly improves performance compared to baseline models.

### Strengths
- Genesis introduces an innovative end-to-end co-design optimization that combines attention-based morphology processing with reward balancing between morphology and control.
- The experiments demonstrate significant improvements over current methods, and the ablations highlight the importance of the topographical positional encoder.
- The paper generally explains its contributions and mechanisms clearly, with nice illustrations.
- This approach addresses important limitations in the field and, therefore, could influence future research in co-design optimization.

### Weaknesses
 - Although Genesis demonstrates substantial improvements over current methods, the paper lacks a detailed explanation of specific solution differences between Genesis and previous approaches. 
- Genesis's morphological decisions are not fully interpretable, and a detailed discussion of the morphological features it favors could enhance the paper. Specifically, it is unclear if the evolved morphologies are simply exploiting the hyperparameter space (e.g., varying thickness, limb length) to achieve better performance, or if there are more fundamental design principles being discovered. A comparison of the best morphologies found by Genesis with those found by other methods, controlling for hyperparameter configurations, would strengthen this aspect.
- While Genesis aims for continuous co-optimization, this approach risks overfitting to specific scenarios or static environments. The paper does not sufficiently address the generalization capabilities of the evolved morphologies and control policies to unseen environments or morphological variations. This is particularly important for real-world applications where perfect morphological consistency cannot be guaranteed.
- The clarity of some paragraphs related to the methods could be improved. For example, the role of the temporal credit assignment mechanism and the topology-aware self-attention could be further elucidated with more concrete examples and a more detailed explanation of how they interact to achieve the reported performance gains.

### Questions
- Does Genesis achieve better solutions than evolutionary search methods simply due to access to a superior hyperparameter space (e.g., varying thickness that may affect inertia and speed)? A direct comparison of best morphologies across methods, including an exploration of the role of hyperparameter configurations, would strengthen this aspect.
- Does Genesis prioritize certain features to boost robustness or performance in various environments? Furthermore, it would be good to visualize how morphologies evolve over time. Are the retrieved morphologies consistent across different seeds, or does Genesis find alternative solutions depending on initialization? Additionally, it would be interesting to analyze the topographical encoder representation and how attention shifts based on morphology.
- In real-world applications, slight morphological changes may occur. Ideally, the control policy should adapt to such changes in a zero-shot manner, as in [1,2,3]. A key question is how well Genesis handles IID morphologies (those seen in training) versus OOD morphologies.
- Once the best morphology has been found, does optimizing it independently yield the same or better performance? Does the control policy of Genesis benefit from the co-training?
- What are the main failure modes of Genesis?
- Why is model size evaluated in MB rather than by the number of parameters?
- What is U_t in equation 4.12?

[1]: Chiappa, A. S., Marin Vargas, A., & Mathis, A. (2022). Dmap: a distributed morphological attention policy for learning to locomote with a changing body. Advances in Neural Information Processing Systems.

[2]: Hong, S., Yoon, D., & Kim, K. E. (2021). Structure-aware transformer policy for inhomogeneous multi-task reinforcement learning. In International Conference on Learning Representations.

[3]: Huang, W., Mordatch, I., & Pathak, D. (2020). One policy to control them all: Shared modular policies for agent-agnostic control. In International Conference on Machine Learning.

### Soundness
4

### Presentation
3

### Contribution
4
