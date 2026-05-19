### Summary

This paper proposes a new method for data-driven spatio-temporal simulation of physical systems. The main idea is to formulate the task as a double observation problem and propose a solution with two interlinked dynamical systems. The first system is a discrete dynamical model used to compute a sequence of latent anchor states $\bm{z}_d$, while the second is a continuous dynamical model used to estimate the dense physical state at arbitrary locations and times. The proposed method is evaluated on three benchmark datasets and compared with three baseline methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The proposed method outperforms existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed explanation of the proposed method. The authors should provide more details about the proposed method, including the architecture of the neural networks used, the training procedure, and the loss function. Specifically, the interaction between the two dynamical systems needs to be clarified. How are the latent states and the physical space states connected? What are the specific forms of the discrete and continuous-time dynamical systems? What are the inputs and outputs of each system? How is the loss function defined to ensure that the latent states and physical space states are consistent with the observed data?
- The paper does not provide a detailed comparison with existing methods. The authors should provide a more detailed comparison with existing methods, including a discussion of the advantages and disadvantages of the proposed method compared to existing methods. Specifically, how does the proposed method compare to other data-driven methods for spatio-temporal simulations in terms of accuracy, computational cost, and generalization ability? What are the limitations of the proposed method compared to existing methods?
- The paper does not provide a detailed analysis of the experimental results. The authors should provide a more detailed analysis of the experimental results, including a discussion of the performance of the proposed method on different datasets and under different conditions. What are the factors that affect the performance of the proposed method? How does the performance of the proposed method vary with the size of the training data? What are the limitations of the experimental evaluation?

### Suggestions

The paper would benefit significantly from a more detailed explanation of the proposed method. The authors should provide a clear and concise description of the architecture of the neural networks used, including the number of layers, the number of neurons in each layer, and the activation functions. They should also provide a detailed explanation of the training procedure, including the optimization algorithm, the learning rate, and the batch size. Furthermore, the authors should provide a clear definition of the loss function, including the specific terms and their weights. A diagram illustrating the interaction between the two dynamical systems would be very helpful. The authors should also provide a more detailed explanation of the continuous-time dynamical system, including the specific form of the differential equation and the parameters. The inputs and outputs of each system should be clearly defined. The authors should also provide a more detailed explanation of how the latent states and physical space states are connected. This would greatly improve the clarity and reproducibility of the paper.

In addition, the paper needs a more comprehensive comparison with existing methods. The authors should provide a detailed discussion of the advantages and disadvantages of the proposed method compared to other data-driven methods for spatio-temporal simulations. This discussion should include a comparison of the accuracy, computational cost, and generalization ability of the proposed method with existing methods. The authors should also discuss the limitations of the proposed method compared to existing methods. For example, how does the proposed method handle noisy or incomplete data? How does it perform on systems with complex dynamics? The authors should also discuss the computational cost of the proposed method, including the training time and the inference time. A table summarizing the performance of the proposed method and existing methods on different datasets would be very helpful. This would allow the reader to better understand the strengths and weaknesses of the proposed method.

Finally, the paper needs a more detailed analysis of the experimental results. The authors should provide a discussion of the performance of the proposed method on different datasets and under different conditions. They should also discuss the factors that affect the performance of the proposed method, such as the size of the training data, the choice of hyperparameters, and the complexity of the system. The authors should also discuss the limitations of the experimental evaluation. For example, how well does the proposed method generalize to unseen data? How does the performance of the proposed method vary with the size of the training data? The authors should also discuss the statistical significance of the results. A more detailed analysis of the experimental results would greatly improve the credibility of the paper.

### Questions

See the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
