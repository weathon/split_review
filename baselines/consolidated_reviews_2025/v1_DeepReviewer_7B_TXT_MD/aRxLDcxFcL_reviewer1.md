### Summary

This paper introduces Virtual Community, a platform designed to support embodied AI research in open-world environments. The platform addresses limitations in current embodied AI simulators by enabling scalable 3D scene creation and the simulation of socially grounded agents with realistic characters and social relationships. Two social challenges are proposed: Route Planning and Election Campaign, to test agents' abilities in social interaction and navigation within a large-scale, open-world setting. The authors evaluate baseline agents on these tasks, demonstrating the potential of Virtual Community to advance embodied AI research.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a scalable 3D scene creation pipeline that leverages real-world geospatial data to generate interactive environments, addressing a key limitation in existing simulators that often rely on limited or manually designed scenes.
2. The platform simulates socially grounded agents with realistic characters and social relationships, which is a significant step towards creating more realistic and complex social interactions in embodied AI research.
3. The paper introduces two novel social challenges, Route Planning and Election Campaign, that test agents' abilities in social intelligence and planning within a large-scale, open-world setting.

### Weaknesses

#### Some Related Works


#### comment

1. The paper claims to introduce a scalable 3D scene creation pipeline that leverages real-world geospatial data to generate interactive environments. However, the pipeline appears to be a combination of existing techniques, such as generative models for scene construction and texture refinement, object placement, and automatic annotation. While the integration of these techniques is valuable, the paper does not clearly articulate the novelty of the pipeline or how it significantly advances the state of the art in 3D scene generation for embodied AI. The specific contributions of the pipeline, beyond the combination of known methods, remain unclear.
2. The paper introduces two social challenges, Route Planning and Election Campaign, to test agents' abilities in social interaction and navigation within a large-scale, open-world setting. However, the paper does not provide a thorough analysis of how these challenges are designed to be representative of real-world social interactions. The complexity and diversity of human social behaviors are not fully captured by the proposed challenges, and the paper lacks a discussion on the limitations of these challenges in simulating realistic social dynamics.
3. The evaluation of baseline agents on the proposed challenges is limited in scope. The paper primarily focuses on a few baseline agents, such as a rule-based agent, an MCTS agent, and an LLM agent, without exploring a wider range of agent architectures or learning algorithms. This limited evaluation does not provide a comprehensive understanding of the challenges posed by the platform and the potential of different approaches to address them. The paper should include a more diverse set of baselines to better assess the difficulty and potential of the proposed challenges.

### Suggestions

The paper should provide a more detailed explanation of the novelty of the proposed 3D scene generation pipeline. While the integration of existing techniques is valuable, the paper needs to articulate specific contributions that go beyond simply combining known methods. For example, the authors could discuss how their approach addresses limitations of existing scene generation techniques, such as scalability, realism, or interactivity. A more in-depth analysis of the pipeline's design choices, including the specific generative models used, the object placement strategies, and the annotation methods, would be beneficial. Furthermore, the paper should include a quantitative comparison of the generated scenes with existing datasets to demonstrate the advantages of the proposed pipeline. This would help to establish the significance of the contribution and justify the claim of scalability.

To address the limitations of the proposed social challenges, the paper should provide a more thorough analysis of how these challenges are designed to capture real-world social interactions. The authors should discuss the specific aspects of human social behavior that are being modeled and the limitations of these models. For example, the paper could discuss how the challenges capture aspects such as communication, cooperation, and competition, and how these aspects relate to real-world social dynamics. The paper should also include a discussion of the limitations of the challenges in simulating more complex social behaviors, such as negotiation, compromise, and conflict. A more detailed analysis of the challenges' limitations would help to establish the scope and applicability of the proposed platform.

The evaluation of baseline agents should be expanded to include a wider range of agent architectures and learning algorithms. The paper should explore different approaches to address the challenges posed by the platform, including both traditional AI methods and more recent deep learning techniques. For example, the paper could include agents based on reinforcement learning, imitation learning, and hierarchical planning. A more comprehensive evaluation would provide a better understanding of the challenges posed by the platform and the potential of different approaches to address them. The paper should also include a discussion of the performance of different agents on the proposed challenges, highlighting the strengths and weaknesses of each approach. This would help to identify promising directions for future research in embodied AI.

### Questions

1. How does the proposed pipeline for scalable 3D scene generation address the limitations of existing methods in terms of scalability, realism, or interactivity?
2. How are the social challenges, Route Planning and Election Campaign, designed to capture the complexity and diversity of real-world social interactions?
3. What are the limitations of the proposed social challenges in simulating more complex social behaviors, such as negotiation, compromise, or conflict?
4. How do the baseline agents perform on the proposed challenges, and what insights do their results provide about the difficulty and potential of the platform?

### Rating

3

### Confidence

4

**********
