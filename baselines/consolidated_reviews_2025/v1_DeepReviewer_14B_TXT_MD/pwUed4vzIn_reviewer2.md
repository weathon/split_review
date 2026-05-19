### Summary

This paper proposes that behavioral variability facilitates flexible representations of the body that can be used to adapt to changes in the environment, the body, or the neural controller. This hypothesis is tested by training a simulated four-link agent to reach to three different targets. The agent is controlled by a neural network with eight inputs, a single hidden layer, and eight outputs. The network is trained using backpropagation. The authors test three different training methods: 1) the network is trained to reach to the three target locations (H0); 2) the network is first trained with the outputs fixed to the inputs (H1); 3) the network is trained with the outputs fixed to the inputs for 10,000 time steps and then trained using the reaching task (H2). The results show that H2 outperforms H0 and H1 when the agent is trained to reach to a new target location, when the agent loses a joint, or when a node in the neural network is no longer functional. The authors conclude that behavioral variability facilitates flexible representations that can be used to adapt to changes in the environment, the body, or the neural controller.

### Soundness

1

### Presentation

1

### Contribution

2

### Strengths

The idea that behavioral variability can facilitate learning is interesting and has been explored in the context of reinforcement learning [1]. The idea that behavioral variability can help build a representation of the body is also interesting and has been explored in the context of body schema learning [2, 3, 4]. It would be interesting to see a better-executed study on this topic.

[1] Pekny, A., & Schmidhuber, J. (2018). The diversity bonus: Generalization through multiple random initializations. arXiv preprint arXiv:1803.10871.

[2] Kuperberg, M. R., & Galloway, G. E. (2015). A reinforcement learning approach to body schema adaptation. Journal of neurophysiology, 114(6), 2563-2575.

[3] Nef, T., & Dominey, P. F. (2016). Active perception and body schema learning in a humanoid robot. Frontiers in psychology, 7, 1867.

[4] Kaan, M., & Schröder, J. (2021). Learning the body schema through active perception. Frontiers in Psychology, 12, 653269.

### Weaknesses

#### Some Related Works

[1] The diversity bonus: Generalization through multiple random initializations

#### comment

There are several weaknesses of this paper.

First, the figures are poorly made. The font size is too small and the figures are not well labeled. The figures are screenshots of a simulation, which is not a proper figure. The figures should be plotted using a plotting library such as matplotlib.

Second, the methods are poorly described. The authors do not describe the neural network architecture, the training algorithm, the number of training epochs, or the hyperparameters used. The authors also do not describe the evaluation metrics used to compare the different training methods. The authors should provide more details about the methods used.

Third, the results are poorly described. The authors do not provide any statistical analysis of the results. The authors should provide more details about the results obtained.

Fourth, the authors do not compare their results to any existing work. The authors should compare their results to existing work on behavioral variability and body schema learning.

Fifth, the authors do not provide any insights into the mechanisms underlying the observed results. The authors should provide more insights into the mechanisms underlying the observed results.

Sixth, the authors do not discuss the limitations of their work. The authors should discuss the limitations of their work.

Seventh, the authors do not discuss the potential implications of their work. The authors should discuss the potential implications of their work.

Finally, the authors should proofread their paper to correct any grammatical errors or typos.

### Suggestions

The paper's core idea, that behavioral variability facilitates flexible representations, is intriguing and warrants further investigation. However, the current execution lacks the necessary rigor and detail to support its claims. To improve the figures, the authors should use a plotting library like matplotlib to generate clear, well-labeled graphs with appropriate font sizes and axis labels. Screenshots of simulations are not acceptable in a scientific publication. The figures should also include error bars or confidence intervals to indicate the variability in the results. Furthermore, the figures should be designed to clearly highlight the key findings of the study, rather than simply showing the simulation environment. For example, instead of showing the agent moving, the figures could show the performance of the agent over time, or the learned representations of the body.

To address the lack of methodological detail, the authors should provide a comprehensive description of the neural network architecture, including the number of layers, the number of neurons per layer, the activation functions used, and the initialization method. The training algorithm should be described in detail, including the loss function, the optimization algorithm, the learning rate, and any other relevant hyperparameters. The number of training epochs should be specified, along with the batch size and the frequency of weight updates. The evaluation metrics used to compare the different training methods should be clearly defined, and the authors should justify their choice of metrics. For example, if the authors are using a mean squared error loss function, they should explain why this is an appropriate metric for their task. Additionally, the authors should provide a detailed description of the simulation environment, including the parameters used to simulate the agent and the environment.

Finally, the authors should provide a more thorough analysis of their results, including statistical analysis to determine the significance of the differences between the different training methods. The authors should also compare their results to existing work on behavioral variability and body schema learning, and discuss the similarities and differences between their findings and those of other researchers. The authors should also provide more insights into the mechanisms underlying the observed results, such as by visualizing the learned representations of the body or by analyzing the neural activity of the network. The limitations of the work should be discussed, and the potential implications of the work should be explored. The authors should also proofread their paper to correct any grammatical errors or typos.

### Questions

What are the takeaways from this paper? What is the evidence that behavioral variability facilitates flexible representations of the body? How does behavioral variability facilitate learning? What is the role of behavioral variability in body schema learning?

### Rating

1

### Confidence

4

**********
