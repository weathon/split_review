### Summary

This paper presents a computational framework for studying the role of intrinsic behavioral variability (IBV) in motor adaptation. The authors propose that IBV, such as spontaneous muscle activations (SMAs), plays a crucial role in shaping dynamic body representations and facilitating motor adaptation to changes in morphology or environment. The authors test three hypotheses: no IBV, pre-training IBV, and intermittent IBV. Their results show that intermittent IBV leads to better performance and higher neural representational variability, suggesting that this approach enhances the adaptability and flexibility of motor representations.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper presents a novel computational framework for studying the role of intrinsic behavioral variability (IBV) in motor adaptation. The use of SMAs as a model for IBV is innovative and provides a fresh perspective on how intrinsic variability can impact motor learning. The experimental design, including the three distinct hypotheses, allows for a clear comparison of different training regimes and offers insights into the benefits of intermittent IBV. The paper is well-written and clearly explains the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

The paper's experimental design, while innovative, could benefit from additional details to ensure reproducibility and robustness. For example, the specific parameters used for the IBV model and the neural network architecture are not fully explained. Providing a more detailed description of the simulation environment, including the range of motion, the complexity of the reaching tasks, and the specific metrics used to evaluate performance, would strengthen the paper's claims. Additionally, the paper could benefit from a more thorough discussion of the limitations of the current model and potential avenues for future research. The model's simplicity may limit its applicability to more complex motor tasks and environments. The paper could also benefit from a more detailed discussion of the biological plausibility of the model and how it relates to real-world motor control. The authors should consider the potential for extending their model to incorporate more complex aspects of motor control, such as the integration of sensory feedback and the development of motor synergies. Finally, the authors should consider the potential for using their model to study the effects of different types of interventions, such as pharmacological treatments or neurostimulation, on motor function. This would provide a more comprehensive understanding of the neural mechanisms underlying motor control and the potential for developing new therapies for motor disorders.

### Suggestions

To enhance the paper's reproducibility and robustness, the authors should provide a more detailed description of the simulation environment. This includes specifying the exact kinematic parameters of the agent, such as the length and radius of each joint, and the degrees of freedom available for movement. Furthermore, the complexity of the reaching tasks should be quantified, perhaps by describing the shape and size of the target regions, and the range of motion required to reach them. The authors should also clarify the specific metrics used to evaluate performance, such as the time taken to reach the target, the accuracy of the reaching movement, and the neural representational variability. Providing these details would allow other researchers to replicate the experiments and validate the findings. Additionally, a sensitivity analysis could be performed to assess how the model's performance is affected by changes in the simulation parameters. This would provide a better understanding of the model's robustness and generalizability.

In addition to clarifying the simulation environment, the authors should provide a more in-depth discussion of the limitations of their model and potential avenues for future research. For example, the current model assumes a relatively simple reaching task, and it would be valuable to explore how the model performs on more complex motor control tasks, such as those involving multiple degrees of freedom or dynamic environments. The authors should also discuss the potential impact of different types of intrinsic variability, such as variations in the timing or amplitude of SMAs, on motor representation. Furthermore, the authors could investigate the role of learning and adaptation in shaping the motor representations, and how these representations change over time. This could involve incorporating a learning algorithm that allows the agent to improve its reaching performance over multiple trials. Finally, the authors should consider the implications of their findings for understanding motor adaptation in biological systems, and how their model could be used to study the development of motor skills in humans and animals.

Finally, the authors should consider the potential for extending their model to incorporate more complex aspects of motor control. This could include the integration of sensory feedback, such as proprioception and visual input, which are essential for real-world motor control. The authors could also explore the use of more sophisticated neural network architectures, such as recurrent neural networks, to model the temporal dynamics of motor control. Furthermore, the authors should consider the potential for using their model to study the effects of different types of interventions, such as pharmacological treatments or neurostimulation, on motor function. This would provide a more comprehensive understanding of the neural mechanisms underlying motor control and the potential for developing new therapies for motor disorders. The authors should also discuss the biological plausibility of the model and how it relates to real-world motor control, and consider the potential for extending their model to incorporate more complex aspects of motor control.

### Questions

How does the model's performance compare to existing computational models of motor control?
What are the limitations of the model's simplicity in representing real-world motor control scenarios?
How does the model account for the effects of learning and adaptation over multiple trials?
What are the potential implications of this model for understanding motor adaptation in biological systems?

### Rating

3

### Confidence

3

**********
