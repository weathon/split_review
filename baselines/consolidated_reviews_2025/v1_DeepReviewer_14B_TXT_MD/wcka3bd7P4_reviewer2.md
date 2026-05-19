### Summary

This paper introduces a novel graph neural network framework called FROND, which utilizes the Caputo fractional derivative to leverage the non-local properties of fractional calculus. The authors demonstrate that this approach can capture long-term dependencies in feature updates and mitigate the oversmoothing problem. They also provide a non-Markovian random walk interpretation of the node feature updating process. The FROND framework is shown to be compatible with existing integer-order continuous GNNs and can enhance their performance across diverse datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to graph neural networks by incorporating fractional calculus, which is a significant contribution to the field.

2. The authors provide a detailed theoretical analysis of the proposed method, including a non-Markovian random walk interpretation and a demonstration of oversmoothing mitigation.

3. The experimental results show that the FROND framework consistently improves the performance of various established integer-order continuous GNNs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research.

2. The paper could provide more insights into the choice of the fractional order $\beta$ and its impact on the performance of the model.

### Suggestions

The paper introduces an interesting approach by incorporating fractional calculus into graph neural networks, but it would benefit from a more thorough discussion of the practical limitations and computational costs associated with the proposed FROND framework. Specifically, the authors should elaborate on the computational complexity of calculating the Caputo fractional derivative, especially in the context of large-scale graphs. It would be valuable to see a comparison of the computational time and memory requirements of FROND with existing integer-order continuous GNNs. Furthermore, the paper should discuss the sensitivity of the method to the choice of the fractional order $\beta$. While the authors mention that $\beta$ can be any positive real number, they should provide more guidance on how to select an appropriate value for $\beta$ in practice. For example, are there any heuristics or rules of thumb that can be used to guide the selection of $\beta$? A more detailed analysis of the impact of different values of $\beta$ on the model's performance would be beneficial.

Additionally, the paper should explore the potential limitations of the proposed method in handling dynamic graphs or graphs with evolving structures. The current formulation of FROND seems to be primarily designed for static graphs, and it is unclear how it would perform in scenarios where the graph structure changes over time. The authors should discuss the challenges of applying FROND to dynamic graphs and suggest potential modifications or extensions to address these challenges. For example, could the fractional derivative be adapted to handle time-varying graph Laplacians? Furthermore, the paper should discuss the potential impact of the choice of the time horizon $T$ on the performance of the model. While the authors mention that $T$ can be considered as the number of layers, they should provide more insights into how the choice of $T$ affects the model's ability to capture long-term dependencies and mitigate oversmoothing. A more detailed analysis of the relationship between $T$ and the model's performance would be valuable.

Finally, the paper should provide a more detailed discussion of the potential applications of the proposed method in real-world scenarios. While the authors mention that the method can be used in various domains, they should provide specific examples of how FROND can be applied to solve practical problems. For instance, how can FROND be used in social network analysis, drug discovery, or traffic prediction? Providing concrete examples of real-world applications would help to demonstrate the practical relevance and potential impact of the proposed method. Furthermore, the authors should discuss the potential challenges of applying FROND to real-world datasets, such as the presence of noise, missing data, or outliers. A more thorough discussion of these practical considerations would enhance the paper's overall impact.

### Questions

1. How does the computational cost of the proposed method compare with existing methods?

2. Are there any potential limitations or challenges in applying the proposed method to real-world datasets?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
