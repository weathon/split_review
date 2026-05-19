### Summary

This paper presents Virtual Community, a platform for simulating large-scale, interactive 3D environments populated with socially connected agents. The platform aims to support research in embodied AI by providing a rich, open-world setting where agents can engage in complex social interactions and navigate realistic scenarios. Key contributions include scalable 3D scene generation from real-world geospatial data and the creation of embodied agents with detailed social networks and daily routines. The authors introduce two tasks, Route Planning and Election Campaign, to evaluate the social reasoning and planning capabilities of embodied agents within this environment.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The integration of large-scale 3D environments with socially grounded agents is a significant advancement, addressing a critical gap in embodied AI research.
- The use of real-world geospatial data and generative models for scene creation enhances the realism and scalability of the simulation.
- The introduction of socially connected agents with detailed profiles and daily schedules adds depth to the simulation, enabling more complex and realistic social interactions.
- The paper is well-structured, with clear explanations of the methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

 - The evaluation of the platform is limited to a few baseline agents and specific tasks, which may not fully demonstrate the versatility of the Virtual Community in handling diverse, complex social interactions. Broader testing with varied agent models and scenarios would strengthen claims of general applicability.
- While the platform aims for large-scale simulations, the paper does not provide clear benchmarks or performance metrics regarding the system’s scalability and efficiency when supporting numerous agents and complex interactions across extensive environments.
- The agent motion model, while supporting basic interactions, lacks sophistication in simulating complex social behaviors, such as group dynamics or non-verbal communication cues. This limitation may affect the realism of the simulated social interactions.
- The social relationship model, though innovative, appears somewhat simplistic in its current form. Real-world social structures are influenced by various dynamic factors, such as external events and individual emotional states, which are not accounted for in the proposed framework.

### Suggestions

The evaluation of the Virtual Community platform should be significantly expanded to include a more diverse set of agent models and scenarios. Currently, the evaluation is limited to a few baseline agents and specific tasks, which does not fully demonstrate the platform's capabilities in handling complex social interactions. To address this, the authors should consider incorporating a wider range of agent architectures, such as those based on reinforcement learning, planning algorithms, or hybrid approaches. Furthermore, the evaluation should include scenarios that involve more intricate social dynamics, such as negotiation, collaboration, and conflict resolution. This would provide a more comprehensive assessment of the platform's versatility and its ability to support various embodied AI research questions. The inclusion of more complex tasks, such as organizing events or managing resources within the simulated community, would also be beneficial.

To address the lack of clarity regarding the platform's scalability, the authors should provide detailed benchmarks and performance metrics. These metrics should include CPU and memory usage, as well as frame rates, under different simulation conditions. Specifically, the authors should evaluate the system's performance when simulating a varying number of agents, ranging from a few dozen to several hundred, and when simulating different levels of environmental complexity. This would provide a clearer understanding of the platform's limitations and its suitability for large-scale simulations. Furthermore, the authors should discuss the computational resources required to run the simulations, including the type of hardware and software needed. This information is crucial for researchers who may want to use the platform for their own research.

Finally, the motion model and social relationship model should be enhanced to better capture the complexities of real-world social interactions. The current motion model, while supporting basic interactions, lacks the sophistication needed to simulate complex social behaviors, such as group dynamics and non-verbal communication cues. To address this, the authors should consider incorporating more advanced motion planning algorithms and techniques for simulating realistic human-like movements. The social relationship model, while innovative, appears somewhat simplistic in its current form. Real-world social structures are influenced by various dynamic factors, such as external events and individual emotional states, which are not accounted for in the proposed framework. The authors should consider incorporating these dynamic factors into the model to make it more realistic and nuanced. This could involve using machine learning techniques to model the evolution of social relationships over time and in response to different events.

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
