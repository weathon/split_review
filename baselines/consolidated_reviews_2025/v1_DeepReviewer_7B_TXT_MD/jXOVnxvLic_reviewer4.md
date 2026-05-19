### Summary

This paper presents a framework for simulating neural organoids, which are 3D structures that mimic the development of neurons in a culture dish. The framework is based on a spiking neural network (SNN) that is trained to replicate the behavior of real neural organoids. The authors claim that this framework can be used to pre-experiment, saving time and resources in the development of AI models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a novel approach to simulating neural organoids using a spiking neural network (SNN), which is a significant contribution to the field of neural engineering.
2. The authors provide a detailed description of the framework and its implementation, which is valuable for researchers who want to replicate or build upon their work.
3. The paper is well-written and easy to understand, which makes it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed explanation of the neural organoid simulation framework, which makes it difficult to understand the underlying mechanisms and assumptions of the model.
2. The paper does not provide a comparison of the proposed framework with existing methods for simulating neural organoids, which makes it difficult to assess the novelty and effectiveness of the approach.
3. The paper does not provide a discussion of the limitations of the proposed framework, which makes it difficult to understand the scope and applicability of the model.

### Suggestions

The paper would benefit significantly from a more thorough explanation of the neural organoid simulation framework. Specifically, the authors should detail the mathematical model used to represent the neural activity within the organoid, including the specific equations governing the spiking behavior of the neurons and the interactions between them. It is crucial to clarify how the spiking neural network (SNN) is trained to mimic the complex dynamics of real neural organoids. This should include a description of the training data, the loss function used, and the optimization algorithm. Furthermore, the authors should elaborate on the specific parameters of the SNN and how they are chosen, as well as the rationale behind the chosen architecture. A clear explanation of the simulation environment, including the geometry of the organoid and the properties of the medium, is also necessary. Without these details, it is difficult to assess the validity and generalizability of the proposed framework.

To address the lack of comparison with existing methods, the authors should include a detailed comparison of their framework with other simulation approaches for neural organoids. This comparison should not only focus on the differences in the simulation techniques but also on the performance of the different methods in terms of accuracy, computational cost, and biological fidelity. The authors should also discuss the advantages and disadvantages of their approach compared to other methods. For example, they could compare their SNN-based approach with other types of neural network models or with agent-based models. This would help to establish the novelty and effectiveness of their approach and to understand its strengths and weaknesses compared to existing methods. Furthermore, the authors should discuss the limitations of their approach, such as the computational cost of simulating large-scale neural organoids or the potential for the model to oversimplify complex biological processes.

Finally, the authors should provide a more detailed discussion of the limitations of their proposed framework. This should include a discussion of the assumptions made in the model, the potential for the model to oversimplify complex biological processes, and the limitations of the training data. For example, the authors should discuss the limitations of using a spiking neural network to model the complex dynamics of neural organoids, including the potential for the model to fail to capture certain types of neural activity or to generalize poorly to different types of organoids. The authors should also discuss the limitations of the simulation environment, such as the simplification of the medium and the lack of consideration for other factors that may influence neural activity. A thorough discussion of these limitations is essential for understanding the scope and applicability of the model and for guiding future research in this area.

### Questions

1. How does the proposed framework compare to other existing methods for simulating neural organoids?
2. What are the limitations of the proposed framework, and how can these limitations be addressed in future work?
3. How can the proposed framework be used to pre-experiment, and what are the potential benefits of using this framework in the development of AI models?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
