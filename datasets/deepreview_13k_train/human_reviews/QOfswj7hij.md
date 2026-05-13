# Online Neuro-Symbolic Predicate Invention for High-Level Planning

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Broadly intelligent agents should form task-specific abstractions that selectively expose the essential elements of a task, while abstracting away the complexity of the raw sensorimotor space. In this work, we present Neuro-Symbolic Predicates, a first-order abstraction language that combines the strengths of symbolic and neural knowledge representations. We outline an online algorithm for inventing such predicates and learning abstract world models. We compare our approach to hierarchical reinforcement learning, vision-language model planning, and symbolic predicate invention approaches, on both in- and out-of-distribution tasks across five simulated robotic domains. Results show that our approach offers better sample complexity, stronger out-of-distribution generalization, and improved interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Neuro-Symbolic Predicates (NSPs), a first-order abstraction language that combines symbolic and neural knowledge representations for high-level planning in robotics. The authors propose an online algorithm for inventing such predicates and learning abstract world models from interactions with the environment, without relying on demonstrations. The method leverages Vision-Language Models (VLMs) to ground predicates in perceptual data and integrates them into a planning framework that interleaves predicate proposal, validation, and goal-driven exploration. The approach is evaluated across five simulated robotic domains, comparing it with hierarchical reinforcement learning, VLM planning, and symbolic predicate invention methods. The results demonstrate that the proposed method offers better sample efficiency, stronger out-of-distribution generalization, and improved interpretability.

### Strengths
1. Novel Approach: This paper proposes a novel approach to effectively integrate symbolic reasoning with neural perceptual representations using NSPs to address the challenge of forming task-specific abstractions in robotics.

2. Online Predicate Invention: The proposed method uses online invention of predicates from environment interactions that does not need demonstrations. This is a valuable property in real-world applications, since collecting demonstrations could be expensive or even infeasible.

3. Integration of VLMs: VLMs are leveraged to enable the agent to handle rich representations of concepts, both visually and logically, grounding predicates in the perceptual data, thus enabling more flexible and stronger abstractions.

4. Strong Empirical Results: Their results show strong empirical results, outperforming other baselines over various domains in terms of sample efficiency and generalization to unseen tasks, and planning efficiency.

5. Interpretability: The model uses NSPs, providing interpretable outputs. This helps in understanding or debugging the behavior of the agent. This is critical in safety-critical applications.

### Weaknesses
1. The reliance on VLMs raises questions about its scalability to more complex or noisy real-world settings in which VLMs might perform poorly, hence affecting the robustness of the method.

2. In their approach it is assumed that there is access beforehand to well-defined motor skills and object-centric state representations that in practice are not always available.

3. Comparisons to more SOTA methods in hierarchical planning or neuro-symbolic reasoning could strengthen empirical evaluations and position the work better within the literature.

### Questions
1. How would your method scale to real-world environments with more complex visual scenes and possible noise? Have you considered the potential limitation of current VLMs in these settings, and what could be the effect on NSPs' performance?

2. Considering the fact that VLMs are not infallible, how sensitive is your approach to inaccuracies or biases in the VLM outputs? Do you observe cases where VLM errors lead to incorrect predicate invention or planning failures, and how could these be mitigated?

3. Your approach assumes a given fixed set of low-level motor skills. How much can that assumption be relaxed, and could the approach be extended towards learning or adapting these skills jointly with the high-level predicates?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a new method to learn grounded symbolic predicates and operators from online interaction data for high-level planning. The core of this method is to generate predicates represented in python functions by prompting an VLM. Such predicate functions can invoke VLMs to process image observations and incorporate logical structure to build predicate hierarchies (i.e., derived predicates). Then the most useful predicates are selected and operators are learned following variants of previous works [1, 2]. In experiments, the method is evaluated on 5 domains with multiple baseline methods including Hierarchical RL and VLM planning, showingcase that the method can recover symbolic planning domains that allows effective planning.

[1] Silver, Tom, et al. "Predicate invention for bilevel planning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 10. 2023.

[2] Chitnis, Rohan, et al. "Learning neuro-symbolic relational transition models for bilevel planning. In 2022 IEEE." RSJ International Conference on Intelligent Robots and Systems (IROS).

### Strengths
This paper has sufficient quality and soundness, and I'm satisfied with its approach and evaluations.
- The paper is well-structured and clearly-presented. It has good coverage of literature.
- Learning symbolic predicates is foundamental to high-level planning. The paper proposes a flexible approach to learn neural-symbolic predicates grounded on image observations and natural language.
- The proposed method is comprehensively evaluated via comparison with baselines and ablation studies.

### Weaknesses
 - I would suppose the VLM-based predicate functions can get wrong even after applying the techniques described in line 178-189. How will the invented predicates with wrong grounding affect downstream operator learning and planning?
- I wonder how are the low-level skills realized in experiments for the proposed method and baselines. Are they realized by motion planning? Do you learn low-level skills in the MAPLE baseline?
- In Figure 4, it seems that the oracle baseline doesn't achieve 100% success rate in Blocks and Coffee domain. Its performance is even slightly worse than the proposed method in Blocks. This seems to be weird as the Blocks domain is the most well-known classical domain that can be solved completely with a few predicates and operators. I wonder why this happens?

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel framework for robot planning by integrating NSPs, a method that combines neural and symbolic representations. The authors present an algorithm for online predicate invention, leveraging VLMs to dynamically learn abstract world models through real-time interaction in various robotic environments. The study compares the proposed approach to several HRL and symbolic methods, evaluating performance in terms of sample efficiency, generalization, and interpretability.

### Strengths
1.	**Innovative Approach**: The paper introduces neuro-symbolic predicates to robot planning, using VLMs to invent predicates in a task-relevant manner, a strategy that has clear advantages over static symbolic approaches. The approach also supports perceptual abstraction and logical complexity, enabling the system to better generalize across environments.
2.	**Experimental Design**: The authors evaluate their approach across five different simulated robotic domains with various tasks, making the results generalizable. Furthermore, the comparisons with other SOTA, are well-chosen and highlight the advantages of the proposed method in terms of efficiency and adaptability.
3.	**Methodology and Algorithmic Design**: The online NSP invention algorithm is well-structured and incrementally builds task-relevant abstractions. By leveraging both VLMs for perceptual understanding and a symbolic component for logical manipulations, this approach improves sample efficiency, crucial in robotic applications where data is limited or expensive to obtain.

### Weaknesses
1.	**Clarity of Explanation**: Some explanations in the paper are unclear. For example, in the paragraph beginning with line 178, the process of conditioning on the previous action should be explained in more detail. Specifically, it's unclear how the previous action is encoded and used to influence the predicate proposal or validation. The paper should clarify if the action is used as a direct input to the VLM, or if it's used to filter or modify the VLM's output. Furthermore, the validation process of these predicate proposals lacks detail. It is not clear how the system determines if a proposed predicate is useful or not, beyond a general notion of task relevance. The criteria for accepting or rejecting a proposed predicate should be more explicitly defined, including any thresholds or metrics used.
2.	**Reliance on VLMs and Practicality**: A potential limitation of this approach is its reliance on the accuracy of VLMs, which may be sensitive to changes in the environment. The approach assumes that perceptual cues relevant to task abstractions are identifiable through VLMs. However, variability in VLM performance, particularly with domain shifts or challenging visual inputs, can affect the system's robustness. Although the authors attempt to address this by conditioning predicates on past actions and object labeling, it is unclear how effective these strategies will be in practice, especially under less predictable real-world variations where perceptual noise could affect predicate accuracy. For instance, the paper does not discuss how the system handles situations where the VLM misinterprets an object or its state, leading to incorrect predicate assignments. This could lead to cascading errors in the planning process.
3.	**Time Complexity and Performance**: As an online learning method, computational efficiency is critical, particularly for real-time applications in robotics. While the paper presents experimental results in supplementary materials, these do not convincingly demonstrate that the proposed approach maintains efficiency at scale. The paper lacks a detailed analysis of how the computational cost scales with the number of objects, predicates, or the complexity of the environment. Including more detailed time complexity analysis or exploring algorithmic optimizations could address this concern, as current evaluations suggest that scalability in time-sensitive or resource-constrained environments may be limited. Moreover, the supplementary results lack a detailed breakdown, which would clarify how computational resources scale with task complexity. For example, it is unclear how much time is spent on VLM queries versus symbolic reasoning, and how these times change with increasing task complexity.

### Questions
1. How does the framework ensure a robust and diverse predicate set while maintaining task relevance?
2. Is there a systematic mechanism for leveraging failures to refine or adjust future planning decisions, rather than simply discarding infeasible options?

### Soundness
3

### Presentation
3

### Contribution
2
