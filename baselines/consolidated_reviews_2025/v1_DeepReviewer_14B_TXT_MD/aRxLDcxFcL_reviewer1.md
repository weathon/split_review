### Summary

This paper introduces Virtual Community, a simulation platform designed for embodied AI research, which generates large-scale, interactive 3D environments and socially connected agents. The platform addresses the limitations of existing simulators by offering scalable 3D scene generation grounded in real-world geospatial data and creating embodied agents with detailed social relationship networks. Two key challenges—Route Planning and Election Campaign—are introduced to evaluate agents' social reasoning and planning capabilities in open-world scenarios.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The Virtual Community platform combines large-scale 3D scene generation with socially rich agent communities, providing a unique and comprehensive environment for embodied AI research.
- The use of real-world geospatial data and generative models to create diverse and scalable environments enhances the realism and applicability of the simulation.
- The introduction of challenges like Route Planning and Election Campaign sets practical benchmarks for evaluating social reasoning in embodied agents.

### Weaknesses

#### Some Related Works


#### comment

 - The paper describes the use of real-world data, including geospatial information, but it lacks a detailed discussion on the ethical implications and potential privacy concerns associated with using such data. It is crucial to address how personal information is anonymized and how the simulation ensures compliance with data protection regulations.
- The process of generating agent social relationships and daily schedules seems to rely on LLMs, which may introduce biases or inconsistencies in the simulation. How does the framework handle these potential issues to maintain realistic and unbiased agent behavior?
- The evaluation of the platform is limited to a few baseline agents and specific tasks, which may not fully demonstrate the versatility of the Virtual Community in handling diverse, complex social interactions. Broader testing with varied agent models and scenarios would strengthen claims of general applicability.
- While the platform aims for large-scale simulations, the paper does not provide clear benchmarks or performance metrics regarding the system’s scalability and efficiency when supporting numerous agents and complex interactions across extensive environments.
- The agent motion model, while supporting basic interactions, lacks sophistication in simulating complex social behaviors, such as group dynamics or non-verbal communication cues. This limitation may affect the realism of the simulated social interactions.
- The social relationship model, though innovative, appears somewhat simplistic in its current form. Real-world social structures are influenced by various dynamic factors, such as external events and individual emotional states, which are not accounted for in the proposed framework.

### Suggestions

The paper should include a thorough discussion of the ethical considerations related to the use of real-world geospatial data. This discussion should go beyond a simple statement of anonymization and delve into the specific methods used to ensure that no personally identifiable information is included in the simulation. For example, the paper should specify the level of granularity of the geospatial data, the sources of this data, and the steps taken to remove or obfuscate any potentially sensitive information. Furthermore, the authors should address the potential for bias in the selection of geospatial data and how this might impact the generalizability of the simulation results. A detailed explanation of the data processing pipeline, including any data cleaning or transformation steps, is necessary to demonstrate compliance with data protection regulations and to ensure the ethical integrity of the research.

To address the potential biases and inconsistencies introduced by LLMs in generating agent social relationships and daily schedules, the authors should implement a more robust validation framework. This framework should include both automated checks and human evaluation to ensure that the generated behaviors are realistic and unbiased. For example, the authors could use statistical methods to analyze the distribution of social relationships and daily activities, comparing them to real-world data to identify any anomalies. Additionally, the paper should describe the specific prompts used to generate these behaviors and the reasoning behind their design. A sensitivity analysis of the LLM parameters and prompts would also be beneficial to understand how these choices affect the simulation outcomes. The authors should also consider incorporating mechanisms to introduce variability and adaptability in agent behaviors over time, rather than relying on static schedules and relationships.

The evaluation of the platform should be expanded to include a wider range of agent models and scenarios. The current evaluation is limited to a few baseline agents and specific tasks, which does not fully demonstrate the versatility of the Virtual Community. The authors should consider including more complex social interactions, such as negotiation, collaboration, and conflict resolution, in their evaluation. Furthermore, the paper should provide clear benchmarks and performance metrics regarding the system’s scalability and efficiency when supporting numerous agents and complex interactions across extensive environments. This should include measurements of CPU and memory usage, as well as frame rates, under different simulation conditions. The authors should also explore the limitations of the motion model and consider incorporating more sophisticated techniques for simulating complex social behaviors, such as group dynamics and non-verbal communication cues.

### Questions

- Can the authors provide more detailed benchmarks or performance metrics that demonstrate the platform's scalability, particularly in terms of CPU and memory usage, when simulating large agent populations and complex environments?
- How does the motion model intend to incorporate more complex social behaviors in future versions? Are there plans to include non-verbal cues or group interaction dynamics to enhance the realism of agent interactions?
- Given the reliance on LLMs for generating agent behaviors and social structures, what measures are in place to detect and mitigate biases that may arise from the training data of these models?
- Could the authors elaborate on how the social relationship model might be expanded to include more dynamic and context-sensitive interactions, such as responses to unexpected events or changes in agent emotional states?
- What are the plans for allowing other researchers to access and utilize the Virtual Community platform? Is there a timeline for open-sourcing the platform or providing access through other means?

### Rating

6

### Confidence

4

**********
