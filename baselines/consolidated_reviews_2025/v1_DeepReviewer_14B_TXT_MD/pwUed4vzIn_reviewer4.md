### Summary

The authors propose that intrinsic behavioral variability (IBV) is a mechanism for motor adaptation. They test this hypothesis by training a simple 4-joint simulated arm to reach to three targets. They compare three different training methods: (1) training directly on the target-reaching task (H0), (2) training on a self-supervised task (H1), and (3) a combination of (1) and (2) (H2). They find that H2 outperforms H0 and H1 in three different adaptation tasks: learning a new target, adapting to amputation, and adapting to a neural stroke.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

The authors propose a novel hypothesis for motor adaptation, which is well-motivated from a developmental neuroscience perspective. The experiments are well-designed, and the results provide strong support for the hypothesis. The paper is generally well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is that the model is extremely simple. The simulated arm has only four joints, the neural network is very small, and the tasks are relatively simple. This raises concerns about the generalizability of the findings to more complex scenarios. Specifically, the limited number of joints may not capture the complex dynamics and coordination required for more realistic reaching tasks. The small neural network size could limit the agent's ability to learn intricate motor patterns and adapt to more challenging environments. Furthermore, the simplicity of the tasks, such as reaching to static targets, does not fully explore the agent's capacity for adaptation to dynamic or unpredictable conditions. 

Additionally, the paper lacks a thorough discussion of the limitations of the model and its potential impact on the generalizability of the results. The authors should address how the simplicity of the model might affect the conclusions drawn from the experiments. For example, it is unclear whether the observed benefits of the H2 training method would still hold with a more complex model or in more realistic scenarios. The absence of a detailed discussion on these limitations makes it difficult to assess the broader implications of the findings.

Finally, the paper could benefit from a more detailed explanation of the self-supervised task used in H1 and H2. The current description is vague, and it is unclear how this task contributes to the agent's ability to adapt. A more thorough explanation of the self-supervised task, including its specific objectives and how it relates to the target-reaching task, would improve the clarity and understanding of the paper.

### Suggestions

To address the concerns about model simplicity, the authors should consider conducting additional experiments with more complex models and tasks. For example, they could explore the use of simulated arms with a greater number of joints, larger neural networks, and more challenging reaching tasks that involve dynamic targets or obstacles. This would provide a more robust assessment of the generalizability of their findings. Furthermore, the authors should include a detailed discussion of the limitations of their current model and how these limitations might affect the interpretation of their results. This discussion should explicitly address the potential impact of model simplicity on the observed benefits of the H2 training method. It would be beneficial to include a sensitivity analysis to determine how the model's performance changes with varying levels of complexity.

To improve the clarity of the paper, the authors should provide a more detailed explanation of the self-supervised task used in H1 and H2. This explanation should include a clear description of the task's objectives, the specific inputs and outputs of the neural network during this task, and how this task relates to the target-reaching task. A visual representation of the self-supervised task, such as a diagram or a short video, would be helpful. Additionally, the authors should discuss the rationale behind choosing this particular self-supervised task and how it is expected to promote motor adaptation. This would help the reader better understand the mechanisms underlying the observed results.

Finally, the authors should consider including a more detailed analysis of the neural network's internal representations. This could involve visualizing the activation patterns of the hidden units or analyzing the learned weights to gain insights into how the network encodes motor information. Such an analysis could provide a deeper understanding of how the different training methods affect the network's ability to adapt to new situations. Furthermore, the authors should discuss the potential implications of their findings for the development of more robust and adaptable robotic systems. This would help to broaden the impact of their work and highlight its relevance to the field of robotics.

### Questions

1. How does the self-supervised task work? I don’t understand how the agent is supposed to learn anything useful by trying to predict its own inputs. 
2. How well does the model generalize to more complex tasks? I would be more convinced of the significance of the results if they were demonstrated with a more complex model.

### Rating

6

### Confidence

3

**********
