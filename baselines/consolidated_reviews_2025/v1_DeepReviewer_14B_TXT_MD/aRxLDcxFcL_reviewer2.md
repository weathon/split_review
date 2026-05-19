### Summary

The paper introduces Virtual Community, a social world simulation platform designed to support embodied AI research, featuring large-scale community scenarios derived from the real world. Virtual Community introduces two key features to enrich the virtual social world with generative AI: scalable 3D Scene creation, which supports the generation of expansive outdoor and indoor environments at any location and scale, addressing the lack of a large-scale, interactive, open-world scene for embodied AI research; and embodied agents with grounded characters and social relationship networks, the first to simulate socially connected agents at a community level, that also have scene-grounded characters. Two novel challenges are designed to showcase that Virtual Community provides testbeds to evaluate the social reasoning and planning capabilities of embodied agents in open-world scenarios: Route Planning and Election Campaign.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors have developed a comprehensive pipeline that integrates real-world geospatial data with generative AI models to create large-scale, interactive 3D environments. This pipeline includes mesh simplification, texture refinement, object placement, and automatic annotation, which together ensure that the generated scenes are both visually rich and simulation-ready.
2. The Virtual Community platform supports a large number of interconnected 3D agents, each with grounded characters and social relationship networks. This allows for the simulation of complex social interactions within a community setting, which is a significant advancement over existing simulators that typically focus on limited agent populations and constrained scenarios.
3. The platform is designed to be scalable and customizable, allowing researchers to generate diverse and realistic scenes and agent communities. This flexibility is crucial for studying a wide range of social interactions and embodied AI tasks in environments that closely resemble the real world.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed comparison with existing simulators, which would help in understanding the unique advantages and limitations of Virtual Community. A comparative analysis could highlight how Virtual Community stands out in terms of scalability, realism, and the complexity of social interactions it can support.
2. The evaluation of the platform is limited to a few baseline agents and specific tasks. To fully demonstrate the capabilities of Virtual Community, a broader range of experiments and more sophisticated agents should be tested. This would provide a more comprehensive understanding of the platform's potential and limitations.
3. The paper lacks a thorough discussion of the computational resources required to run the simulations. Providing details on the hardware and software requirements would help researchers assess the feasibility of using Virtual Community in their own labs.

### Suggestions

To strengthen the paper, the authors should include a detailed comparison table that contrasts Virtual Community with existing embodied AI simulators. This table should cover key aspects such as the number of agents supported, the size and complexity of the simulated environments, the types of social interactions that can be modeled, and the computational resources required. For example, the comparison should explicitly mention simulators like the Habitat and AI2-THOR, and highlight how Virtual Community's open-world, large-scale community simulation differs from these constrained environment simulators. Furthermore, the comparison should also include simulators that focus on social interactions, such as the SocialNav and SocialNav2, and clearly articulate how Virtual Community's approach to generating diverse and realistic social interactions is unique. This detailed comparison will help the reader understand the specific niche that Virtual Community fills and its advantages over existing tools.

In addition to the comparative analysis, the authors should expand the evaluation section to include a wider range of experiments and more sophisticated agents. The current evaluation is limited to a few baseline agents and specific tasks, which does not fully demonstrate the platform's capabilities. The authors should consider including more complex tasks that involve longer time horizons and require more sophisticated planning and social reasoning. For example, they could introduce tasks that require agents to form alliances, negotiate with other agents, or adapt to changing social dynamics. Furthermore, the evaluation should include a variety of agent architectures, such as reinforcement learning agents, planning-based agents, and hybrid approaches. This would provide a more comprehensive understanding of the platform's potential and limitations and allow researchers to better assess its suitability for their own research questions. The evaluation should also include metrics that quantify the complexity and realism of the social interactions, such as the number of unique social relationships, the frequency of social interactions, and the diversity of social behaviors.

Finally, the authors should provide a detailed discussion of the computational resources required to run the simulations. This should include information on the hardware requirements, such as the CPU, GPU, and memory specifications, as well as the software requirements, such as the operating system and the specific versions of the required libraries. The authors should also provide an estimate of the simulation speed, such as the number of frames per second, for different simulation scenarios. This information is crucial for researchers to assess the feasibility of using Virtual Community in their own labs. Furthermore, the authors should discuss the scalability of the platform in terms of the number of agents and the size of the environment, and provide guidelines on how to optimize the simulation performance. This will help researchers to effectively utilize the platform and avoid potential bottlenecks.

### Questions

1. How does Virtual Community compare to existing simulators in terms of scalability, realism, and the complexity of social interactions it can support? A detailed comparison would help in understanding the unique advantages of your platform.
2. What are the computational requirements for running simulations in Virtual Community? Providing details on the hardware and software requirements would help researchers assess the feasibility of using your platform in their own labs.
3. Can you provide more information on the limitations of the current agent population generation method? How do you plan to address these limitations in future work?
4. How does the platform handle the simulation of large-scale communities with hundreds or thousands of agents? Are there any specific optimizations or techniques used to ensure efficient simulation?
5. What are the plans for open-sourcing the Virtual Community platform? Making the platform accessible to other researchers would greatly enhance its impact and utility in the embodied AI community.

### Rating

6

### Confidence

4

**********
