### Summary

This paper introduces Virtual Community, a simulation platform designed to support embodied AI research by creating large-scale, interactive 3D environments. The platform features two key components: scalable 3D scene generation and embodied agents with grounded characters and social relationship networks. The authors propose two challenges, Route Planning and Election Campaign, to evaluate the social reasoning and planning capabilities of embodied agents in open-world scenarios. The paper demonstrates the potential of Virtual Community to address the limitations of existing simulators and advance the development of embodied AI.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel simulation platform, Virtual Community, which addresses the limitations of existing simulators by providing large-scale, interactive 3D environments. This is a significant contribution to the field of embodied AI.

2. The integration of scalable 3D scene generation with embodied agents and social relationship networks is a creative and innovative approach. The use of real-world geospatial data and generative models to create diverse and realistic scenes is particularly noteworthy.

3. The paper is well-structured and clearly written. The authors provide a comprehensive description of the methodology, including the scene generation process, agent creation, and the design of the two challenges. The figures and tables are informative and effectively illustrate the concepts presented in the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough comparison with existing simulation platforms. While Table 1 provides a comparison, it would be beneficial to include a more detailed analysis of the advantages and disadvantages of Virtual Community compared to other state-of-the-art simulators. Specifically, the comparison should delve into aspects such as the fidelity of physics simulation, the complexity of agent behaviors supported, and the scalability of the environment in terms of both size and agent population. A more granular comparison would help to better position the contribution of this work.

2. The evaluation of the platform is limited to two specific challenges, Route Planning and Election Campaign. While these challenges are relevant, it would be beneficial to include a wider range of tasks to demonstrate the versatility and generalizability of the platform. For example, tasks involving collaborative problem-solving, negotiation, or resource management could provide a more comprehensive assessment of the platform's capabilities. The current evaluation does not fully explore the potential of the social relationship networks and grounded characters in more complex scenarios.

3. The paper does not provide sufficient details on the computational resources required to run the simulations. This information is crucial for researchers who may want to use the platform for their own research. Details on the hardware requirements, software dependencies, and the expected runtime for different simulation scenarios would be valuable. Furthermore, the paper should discuss the scalability of the platform in terms of the number of agents and the size of the environment, and how these factors impact computational cost.

4. The paper lacks a discussion on the limitations of the proposed approach. While the authors acknowledge that the platform is not perfect, a more detailed discussion of the potential challenges and future research directions would be beneficial. For example, the paper could discuss the limitations of the current scene generation method in terms of the diversity of environments, the realism of the agent behaviors, and the complexity of the social relationship networks. Addressing these limitations would provide a more balanced perspective on the contribution of the work.

### Suggestions

To strengthen the paper, the authors should include a more detailed comparison with existing simulation platforms, focusing on specific aspects such as physics simulation fidelity, agent behavior complexity, and scalability. This comparison should not only highlight the advantages of Virtual Community but also acknowledge its limitations relative to other state-of-the-art simulators. For instance, the authors could compare the platform's ability to simulate complex physical interactions, such as object manipulation or collisions, with platforms like MuJoCo or Isaac Gym. Similarly, a comparison of the complexity of agent behaviors supported, such as planning, reasoning, and social interaction, with platforms like Habitat or SocialNav would be beneficial. Furthermore, the authors should provide a more detailed analysis of the platform's scalability in terms of both environment size and agent population, and how these factors impact computational cost. This would help researchers understand the practical limitations of the platform and its suitability for different research problems.

To demonstrate the versatility and generalizability of the platform, the authors should include a wider range of evaluation tasks beyond Route Planning and Election Campaign. Tasks involving collaborative problem-solving, negotiation, or resource management could provide a more comprehensive assessment of the platform's capabilities. For example, the authors could design a task where agents need to collaborate to achieve a common goal, such as building a structure or solving a puzzle. This would allow them to evaluate the platform's ability to support complex social interactions and collaborative behaviors. Similarly, tasks involving negotiation or resource management could be used to assess the platform's ability to simulate economic or strategic interactions between agents. These additional tasks would provide a more robust evaluation of the platform's capabilities and its potential for supporting a wide range of embodied AI research.

Finally, the authors should provide more details on the computational resources required to run the simulations, including hardware requirements, software dependencies, and expected runtime for different simulation scenarios. This information is crucial for researchers who may want to use the platform for their own research. The authors should also discuss the scalability of the platform in terms of the number of agents and the size of the environment, and how these factors impact computational cost. Furthermore, the authors should include a more detailed discussion of the limitations of the proposed approach, including the limitations of the current scene generation method, the realism of the agent behaviors, and the complexity of the social relationship networks. Addressing these limitations would provide a more balanced perspective on the contribution of the work and help guide future research directions.

### Questions

1. Could the authors provide more details on the computational resources required to run the simulations? This information would be valuable for researchers who may want to use the platform for their own research.

2. How does the platform handle the scalability of the environment and the number of agents? Are there any limitations in terms of the size of the environment or the number of agents that can be simulated?

3. What are the potential challenges and future research directions for the Virtual Community platform? Are there any plans to extend the platform to support more complex tasks or environments?

### Rating

6

### Confidence

3

**********
