# ReGen: Generative Robot Simulation via Inverse Design

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Simulation plays a key role in scaling robot learning and validating policies, but constructing simulations remains labor-intensive. In this paper, we introduce ReGen, a generative simulation framework that automates this process using inverse design. Given an agent's behavior (such as a motion trajectory or objective function) and its textual description, we infer the underlying scenarios and environments that could have caused the behavior.
Our approach leverages large language models to construct and expand a graph that captures cause-and-effect relationships and relevant entities with properties in the environment, which is then processed to configure a robot simulation environment. Our approach supports (i) augmenting simulations based on ego-agent behaviors, (ii) controllable, counterfactual scenario generation, (iii) reasoning about agent cognition and mental states, and (iv) reasoning with distinct sensing modalities, such as braking due to faulty GPS signals. 
We demonstrate our method in autonomous driving and robot manipulation tasks, generating more diverse, complex simulated environments compared to existing simulations with high success rates, and enabling controllable generation for corner cases. This approach enhances the validation of robot policies and supports data or simulation augmentation, advancing scalable robot learning for improved generalization and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces ReGen, a generative simulation framework that automates the process of constructing simulations using inverse design.  Given an agent’s behavior (such as a motion trajectory or objective function) and its textual description, ReGen infers the underlying scenarios and environments that could have caused the behavior.  This approach leverages large language models (LLMs) to construct and expand a graph that captures cause-and-effect relationships and relevant entities with properties in the environment, which is then processed to configure a robot simulation environment.  ReGen is demonstrated in autonomous driving and robot manipulation tasks, generating more diverse and complex simulated environments compared to existing simulations with high success rates, and enabling controllable generation for corner cases.

### Strengths
1. ReGen presents an inverse design approach for generative simulation, which allows for the creation of diverse and complex simulated environments based on agent behavior and textual descriptions.
2. ReGen generates more diverse and complex simulated environments compared to existing simulations, as demonstrated in autonomous driving and robot manipulation tasks.
3. ReGen enables controllable generation for corner cases, which is important for safety-critical applications like autonomous driving.

### Weaknesses
1. The evaluation of ReGen is primarily focused on diversity and complexity, with less emphasis on the realism and physical accuracy of the generated simulations.
2. ReGen heavily relies on LLMs, which can be computationally expensive and may not always generate semantically accurate or physically plausible scenarios due to LLMs.
3. The applicability of ReGen to other robotics domains beyond autonomous driving and robot manipulation is not extensively explored.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents ReGen, which, given an existing agent's behavior and motion trajectory, generates simulated environments counterfacturally that explains the possible causes and preconditions of this agent trajectory via LLM and VLM. In this way, authors are able to augment simulation data that allows the training of more robust models and policies. The authors then compare their approach to previous baselines in self driving (Carla simulator) and in robot manipulation (PyBullet), demonstrating that their approach effectively generates more diverse simulation environments.

### Strengths
Diversifying and augmenting existing simulated environments and trajectories through counterfactural generation is an important research problem. It provides a promosing way to improve the robustness and safety of agents and policies under corner cases and unexpected scenarios.

### Weaknesses
The paper suffers from significant weaknesses in writing clarity and the depth of analysis, specifically:
- The methodology section 2 does not detail the models, the model versions, and the important hyperparameters used for prompting LLM / VLM for counterfactual generation. Some of the details are deferred to page 9, which should have been in much earlier in the paper.
- No prompt examples for LLM / VLM are provided in the appendix, making the method unreproducible. No concrete, detailed examples for the entire process of constructing Carla and PyBullet environments through counterfactual generation (following algorithm 1) are provided. 
- Algorithm 1 will very likely result in infinite loop, as there will likely always be at least 1 node with input degree < 1 (unless there are circular cause and effect dependencies).
- L320 - ReGen is able to generate simulated environments by augmenting visual observations like GPS measurement jamming. However there is no detailed description of how the visual observations are augmented. It seems that some tool use ability of LLM is invoked.
- The experiments only demonstrate that ReGen outperforms baselines, but **why** ReGen outperforms the baseline is unclear. There are no ablations in e.g., prompting to answer this question. For example, why does ReGen outperform ChatScene? Is it due to better prompting and / or the better VLM used (note that no prompts are provided throughout the paper)? Is the comparison with baseline fair, with the same specific versions of GPT4o / GPT4 / Claude 3.5?

### Questions
Please address all weaknesses listed above.

Minor:
- Fig 4 caption: "desipte" -> "despite"
- "table {x}" should be "Table x"; "figure {x}" should be "Figure {x}"

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces ReGen, a generative simulation framework that automates the creation of robot simulation environments using inverse design. ReGen takes a robot's behavior and textual descriptions as input, then uses large language models to construct and expand causal graphs that capture relationships between events, entities, and their properties, which are then converted into executable simulation environments. The framework is implemented and validated in both autonomous driving and robot manipulation tasks, demonstrating capabilities in augmenting simulations based on ego-agent behaviors, generating counterfactual scenarios, reasoning about agent cognition, and handling different sensing modalities. The experimental results show that ReGen generates more diverse environments compared to existing simulations, effectively creates corner cases for safety-critical applications, and produces more challenging vision-language-action datasets for vision language models.

### Strengths
While I do not see a clear strength in terms of novelty. However, the authors provide a comprehensive evaluation against multiple baselines, and thorough implementation across autonomous driving and manipulation tasks to demonstrate the applicability of the proposed method.

### Weaknesses
The main contribution of this paper is vague. The use of LLMs to generate simulated task environments for robotic tasks cannot be considered as a major contribution. The proposed method of using LLMs for graph expansion and simulation generation appears to be a straightforward extension of existing work such as [a, b]. I do not see a convincing argument that states the technical contributions of the proposed approach other than some prompt engineering. The "inverse design" is essentially a rebranding of standard goal-conditional generation approaches, where the goal is guided by the inverse design and feed into the LLMs.

The evaluation of the proposed method is not thorough enough, with only brief mentions of success rates without analysis of failure modes, no comparison with human-designed scenarios, and unclear metrics for scenario complexity beyond embedding diversity. Furthermore, the paper inadequately addresses fundamental simulation constraints, as many proposed scenarios can't be fully simulated due to engine limitations, but there is no systematic approach for dealing with these limitations or assessing their impact on practical utility.

[a] Wang, Yufei, et al. "Robogen: Towards unleashing infinite data for automated robot learning via generative simulation." arXiv preprint arXiv:2311.01455 (2023). 
[b] Zhang, Jiawei, Chejian Xu, and Bo Li. "ChatScene: Knowledge-based safety-critical scenario generation for autonomous vehicles." In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

### Questions
1. Regarding the LLM implementation: Could you provide more details about the specific prompting strategies used for graph expansion? How do you ensure consistency and reliability in the LLM output, and how do you handle cases where the LLM generates invalid or inconsistent relationships? 
2. Regarding the failures: The paper reports success rates of 80% for driving and 78% for manipulation. Could you provide a detailed analysis of the failure modes? 
3. About simulation constraints: How do you systematically identify and handle cases where desired scenarios exceed the capabilities of the simulation engine? Is there a formal process for determining which aspects of a scenario can be reasonably approximated and which must be excluded?
4. About generated task completeness. How do you guarantee that the generated tasks are feasible for a robot or autonomous agent? i.e., that there is a practical solution to the generated tasks.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents ReGen, a generative simulation framework that automates the creation of robot simulation environments through inverse design. The approach leverages large language models (LLMs) to construct and expand graphs capturing cause-and-effect relationships and environmental properties, which are then converted into executable simulation environments.

### Strengths
- Appealing core functionality: leveraging inverse design with large language models to generate realistic and diverse simulation environments by capturing cause-and-effect relationships and relevant environmental properties. 
- Great experiments to show the strong capability to generate diverse and corner-case of the scenarios.

### Weaknesses
1. The paper's novelty analysis is insufficient:
- The causality reasoning and diversity aspects appear to be inherent properties of the LLMs rather than unique contributions of the framework
- The generation capabilities seem heavily dependent on the underlying simulator's features

2. There is no analysis of the generated graph, only the results are shown, making it unclear whether the main contributions come from the LLM rather than the proposed graph structure. Additionally, there is no ablation study on the graph; for instance, it is unclear what would happen without edge construction.

### Questions
1. In line 161, what description is used when inferring the property node from the source node?
2. In line 155, is there an example that clarifies what the prior represents exactly?
3. This paper demonstrates a plausible generation ability; however, it lacks analysis of the entire generated graph. Could you provide the complete graph generated by ReGen?
4. Is there an issue with the brackets in line 182? It seems there are multie understandings here. A more precise notation or explanation is needed.
5. When expanding the event-to-event nodes, if the LLM generates events that the simulator cannot execute, how does the system handle this?
6. ReGen exhibits strong capabilities in generating diverse scenarios, yet realism is not thoroughly addressed in the large-scale experiments. Could you elaborate on the realism of the generated scenarios? If the generated scenarios are not reasonable, off-the-shelf VLM understanding may perform poorly, as observed in Table 3.

### Soundness
3

### Presentation
3

### Contribution
2
