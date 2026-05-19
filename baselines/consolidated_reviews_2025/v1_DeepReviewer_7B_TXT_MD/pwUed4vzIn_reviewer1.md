### Summary

The paper presents a computational framework for modeling the development of dynamic body representations in agents, drawing inspiration from biological mechanisms such as spontaneous muscle activations (SMAs). The authors propose that intrinsic behavioral variability (IBV) plays a crucial role in facilitating flexible and adaptive motor representations. Through a series of simulated reaching tasks, they explore three hypotheses: no IBV, pre-training IBV, and intermittent IBV. The results indicate that intermittent IBV leads to better performance and higher neural representational variability, suggesting that this approach enhances the adaptability and flexibility of motor representations.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper introduces a novel computational framework for modeling the development of dynamic body representations, which is a valuable contribution to the field. The use of SMAs as a biological model for IBV is innovative and provides a fresh perspective on how intrinsic variability can impact motor learning. The experimental design, including the three distinct hypotheses, allows for a clear comparison of different training regimes and offers insights into the benefits of intermittent IBV. The findings have implications for understanding motor adaptation and representation in both biological and artificial systems.

### Weaknesses

#### Some Related Works


#### comment

The paper's experimental design, while innovative, could benefit from additional details to ensure reproducibility and robustness. For example, the specific parameters used for the IBV model and the neural network architecture are not fully explained. Providing a more detailed description of the simulation environment, including the range of motion, the complexity of the reaching tasks, and the specific metrics used to evaluate performance, would strengthen the paper's claims. Additionally, the paper could benefit from a more thorough discussion of the limitations of the current model and potential avenues for future research.

### Suggestions

To enhance the paper's clarity and reproducibility, the authors should provide a more detailed account of the simulation environment. This includes specifying the exact kinematic parameters of the agent, such as the length and radius of each joint, and the degrees of freedom available for movement. Furthermore, the complexity of the reaching tasks should be quantified, perhaps by describing the shape and size of the target regions, and the range of motion required to reach them. The authors should also clarify the specific metrics used to evaluate performance, such as the time taken to reach the target, the accuracy of the reaching movement, and the neural representational variability. Providing these details would allow other researchers to replicate the experiments and validate the findings. Additionally, the authors should consider including a sensitivity analysis to assess how the model's performance is affected by changes in the simulation parameters.

To further strengthen the paper, the authors should provide a more in-depth discussion of the limitations of their model and potential avenues for future research. For example, the current model assumes a relatively simple reaching task, and it would be valuable to explore how the model performs on more complex motor control tasks, such as those involving multiple degrees of freedom or dynamic environments. The authors should also discuss the potential impact of different types of intrinsic variability, such as variations in the timing or amplitude of SMAs, on motor representation. Furthermore, the authors could investigate the role of learning and adaptation in shaping the motor representations, and how these representations change over time. This could involve incorporating a learning algorithm that allows the agent to improve its reaching performance over multiple trials. Finally, the authors should consider the implications of their findings for understanding motor adaptation in biological systems, and how their model could be used to study the development of motor skills in humans and animals.

### Questions

1. Could the authors provide more details on the specific parameters used for the IBV model and the neural network architecture?
2. How does the model account for the effects of learning and adaptation over multiple trials?
3. What are the potential implications of this model for understanding motor adaptation in biological systems?

### Rating

3

### Confidence

3

**********
