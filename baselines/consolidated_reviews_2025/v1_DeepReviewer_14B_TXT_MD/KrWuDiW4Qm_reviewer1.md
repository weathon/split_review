### Summary

This paper proposes a meta-learning based method for training neural ODEs that generalize better for out-of-distribution initial conditions and ODE parameters.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper makes first steps towards solving the difficult problem of OOD generalization for neural ODEs. The proposed method is shown to outperform existing methods on simulated examples.
- The paper is well-organized and the writing is clear.

### Weaknesses

#### Some Related Works


#### comment

 - The ODE systems considered in the simulated examples are very simple, with only 2 dimensions and at most 4 RHS terms. This does not seem to be sufficient to support the claim that the proposed algorithm is scalable to complex, high-dimensional systems.
- The paper does not discuss the computational cost of the proposed algorithm compared to existing methods.
- The paper lacks real-world applications.

### Suggestions

The paper would benefit from a more thorough investigation into the scalability of the proposed method. While the current ODE systems are useful for initial validation, the lack of experiments on higher-dimensional systems raises concerns about its practical applicability. The authors should consider testing their method on more complex ODEs, such as those arising in chemical kinetics or fluid dynamics, which often involve dozens or even hundreds of equations. Furthermore, it would be valuable to analyze how the performance of the method scales with the number of parameters in the ODE system. This could involve systematically increasing the number of terms in the RHS of the ODEs and observing the impact on accuracy and computational cost. Such experiments would provide a more robust assessment of the method's scalability and help to identify potential bottlenecks.

Regarding computational cost, the paper should provide a detailed analysis of the time and memory requirements of the proposed algorithm. This analysis should include a breakdown of the computational cost of each step, such as the causal structure discovery, meta-training, and test-time adaptation. It would be helpful to compare the computational cost of the proposed method to that of existing methods, such as APHYNITY, under various conditions, including different ODE systems and training dataset sizes. This comparison should not only focus on the total training time but also consider the time required for each step. Furthermore, the authors should discuss the memory requirements of their method, particularly the memory needed to store the learned causal structure and the meta-learned parameters. This analysis would provide a more complete picture of the computational resources required by the proposed method and help to assess its practical feasibility.

Finally, while simulated examples are useful for initial validation, the paper would be significantly strengthened by the inclusion of real-world applications. The authors should consider applying their method to real-world datasets, such as those arising in epidemiology, climate science, or systems biology. These applications would provide a more realistic assessment of the method's performance and help to demonstrate its practical relevance. For example, the authors could consider using data from real epidemiological studies to model the spread of infectious diseases or use climate data to model the dynamics of atmospheric phenomena. Such real-world applications would not only demonstrate the practical utility of the proposed method but also help to identify potential challenges and limitations that may not be apparent from simulated examples.

### Questions

- How does the computational cost of the proposed algorithm compared to existing methods, e.g., APHYNITY, under various conditions, such as different ODE systems and training dataset sizes?
- Does the proposed algorithm generalize to complex, high-dimensional, and noisy real-world ODE systems? Can the proposed algorithm be applied to real-world applications?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
