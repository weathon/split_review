### Summary

This paper proposes a method for data-driven spatio-temporal simulation of physical systems. The authors formulate the problem as a double observation problem and propose recurrent GNNs and a state observer to solve it. The method is evaluated on three fluid dynamics datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The problem of data-driven physical simulation is important and interesting. 
- The proposed method outperforms the compared baselines.

### Weaknesses

#### Some Related Works

[1] Learning data-driven discretizations for partial differential equations
[2] Learning to simulate complex material dynamics
[3] Learning to simulate new physics with graph networks

#### comment

 - The paper is not well written and is hard to follow. The authors should revise the paper and make it more self-contained. 
- The proposed method is not novel enough. The authors should discuss more about the difference between the proposed method and existing methods, e.g. [1, 2, 3]. 
- The authors should compare the proposed method with more baselines, e.g. [1, 2, 3]. 
- The authors should include the training and inference time in the evaluation. 
- The authors should include the number of parameters in the evaluation. 
- The authors should include the number of training data in the evaluation. 
- The authors should include more analysis about the proposed method, e.g. why it is better than the compared baselines, etc. 
- The authors should include more ablation studies, e.g. the impact of the choice of the neural network architecture, etc.

### Suggestions

The paper needs significant improvement in terms of clarity and technical depth. The current presentation makes it difficult to understand the core contributions and how they advance the field. The authors should provide a more detailed explanation of the double observation problem formulation, including a clear definition of the observation spaces and the underlying assumptions. The connection between the proposed method and existing approaches, particularly those using recurrent GNNs for spatio-temporal modeling, needs to be more thoroughly discussed. Specifically, the authors should clarify how their state observer approach differs from standard recurrent GNN architectures and what specific advantages it offers. A more rigorous mathematical treatment of the method, including a detailed derivation of the equations and a clear explanation of the network architecture, would greatly enhance the paper's credibility. Furthermore, the authors should provide a more intuitive explanation of the method, perhaps with a simplified example, to help readers grasp the core concepts more easily.

To address the lack of novelty, the authors should provide a more detailed comparison with existing methods, such as those mentioned in the original review [1, 2, 3]. This comparison should not only focus on the differences in architecture but also on the theoretical underpinnings and the specific problem settings where each method excels. For instance, the authors should discuss how their approach handles long-range dependencies in space and time compared to methods that rely on fixed grid structures or graph-based representations. A more in-depth analysis of the limitations of existing methods and how the proposed approach overcomes these limitations would be beneficial. The authors should also consider including a discussion of the computational complexity of their method and how it scales with the size of the simulation domain. This would help readers understand the practical applicability of the proposed method.

Finally, the evaluation section needs to be significantly strengthened. The authors should include a more comprehensive set of baselines, including state-of-the-art methods for spatio-temporal modeling of physical systems. The evaluation should also include a more detailed analysis of the results, including a discussion of the strengths and weaknesses of the proposed method in different scenarios. The authors should provide a more thorough analysis of the impact of different hyperparameters on the performance of the method. Furthermore, the authors should include a more detailed analysis of the training and inference time, as well as the number of parameters and training data. This would allow for a more fair and comprehensive comparison with existing methods. The authors should also consider including ablation studies to understand the impact of different components of their method, such as the choice of neural network architecture and the specific design of the state observer.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
