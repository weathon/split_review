### Summary

This paper proposes a direction-aware message-passing scheme for GNNs that is applied to the simulation of deformable objects. The authors show that their method is able to capture material anisotropy, and that it outperforms the baseline method MeshGraphNets.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow
- The proposed method is simple and intuitive
- The experiments are well-designed and demonstrate the effectiveness of the proposed method

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only applied to the simulation of deformable objects, which limits its applicability to other domains
- The method is only compared to one baseline method, which is not sufficient to demonstrate its superiority
- The paper lacks a discussion of the limitations of the proposed method

### Suggestions

The paper would benefit from a more thorough exploration of the method's limitations. For instance, the current evaluation focuses on relatively simple deformations and material properties. It would be valuable to investigate how the method performs under more complex scenarios, such as large deformations, non-linear material behavior, or the presence of contact forces. Furthermore, the paper should discuss the sensitivity of the method to hyperparameter choices, such as the number of message-passing steps or the architecture of the neural networks used for encoding and decoding. A detailed analysis of these aspects would provide a more complete understanding of the method's capabilities and limitations. It would also be beneficial to explore the computational cost of the proposed method, especially in comparison to the baseline, as this is a crucial factor for practical applications.

To strengthen the evaluation, the authors should consider comparing their method against a wider range of baseline methods. While MeshGraphNets is a relevant baseline, there are other GNN architectures and simulation techniques that could be used for comparison. For example, methods based on graph convolutional networks or physics-informed neural networks could provide a more comprehensive benchmark. Additionally, it would be useful to compare the proposed method against traditional numerical simulation techniques, such as finite element methods, to assess its accuracy and efficiency in different scenarios. A more extensive comparison would help to better position the proposed method within the existing literature and highlight its unique advantages and disadvantages. The authors should also consider reporting the variance of their results across multiple runs to demonstrate the robustness of their method.

Finally, the paper should include a more detailed discussion of the practical implications of the proposed method. While the authors mention the potential for real-time simulation, they do not provide concrete examples or scenarios where their method would be particularly useful. It would be beneficial to discuss potential applications in areas such as robotics, computer graphics, or engineering design. Furthermore, the authors should address the challenges of deploying their method in real-world settings, such as the need for accurate material property characterization and the potential for model drift over time. A more thorough discussion of these practical aspects would help to increase the impact and relevance of the paper.

### Questions

- How does the proposed method compare to other GNN architectures for simulation?
- What are the limitations of the proposed method?
- How does the proposed method perform in more complex scenarios, such as large deformations or non-linear material behavior?

### Rating

3

### Confidence

4

**********
