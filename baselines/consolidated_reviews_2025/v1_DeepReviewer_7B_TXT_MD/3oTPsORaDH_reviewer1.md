### Summary

This paper proposes SEGNO, which combines GNNs with Neural ODEs to model multi-object physical systems. The proposed method is claimed to consider the continuous nature of physical systems and second-order motion laws. The authors also provide theoretical analysis to show that the proposed method can learn a unique trajectory between adjacent states. Experiments are conducted on N-body systems, MD22 and CMU motion capture.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow. The problem formulation and method description are clear and easy to understand.
- The proposed method is simple and easy to implement. The idea of incorporating the second-order continuity into the framework is straightforward and intuitive.
- The authors provide theoretical analysis to show that the proposed method can learn a unique trajectory between adjacent states.

### Weaknesses

#### Some Related Works

[1] Graph Gaussian Process
[2] Scaling Up Interpretable ODE with Factor Graph Neural Network
[3] Neural Motion Diffusion
[4] HOPE: Higher Order Physics-aware GNNs for Molecular Dynamics
[5] Coupled Graph Ordinary Neural Differential Equations
[6] LG-ODE: Learning Latent Guided Ordinary Differential Equations for Human Motion Generation
[7] HOPE++: Learning Accurate and Interpretable Higher-Order Physics with Neural Differential Equations

#### comment

 - The proposed method is not novel enough. The idea of incorporating the second-order continuity into the framework is not new. For example, [1, 2] have already explored this idea. The authors should clearly articulate the differences between the proposed method and these existing works.
- The theoretical analysis is not solid enough. The authors only show that the proposed method can learn a unique trajectory between adjacent states. However, it is not clear how this analysis can be extended to the whole trajectory. The analysis does not address the stability of the learned trajectory over extended time horizons, which is crucial for physical simulations. The analysis also does not consider the impact of numerical integration errors on the uniqueness of the learned trajectory.
- The experiments are not comprehensive enough. The authors only compare their method with some baselines. More recent baselines should be included for a more comprehensive evaluation. The experimental evaluation should include more diverse datasets and tasks to demonstrate the generalizability of the proposed method. The current experiments are limited to relatively simple systems, and it is unclear how the method would perform on more complex and realistic physical systems.
- The presentation of the paper can be further improved. For example, the authors should provide more details about the implementation of the proposed method. The description of the experimental setup is also not detailed enough. The authors should also provide more details about the hyperparameter settings and the training procedure.

### Suggestions

The authors should more clearly differentiate their approach from existing methods that incorporate second-order continuity. While the idea of using a Neural ODE with a second-order continuity constraint is not entirely novel, the specific implementation and its application within a GNN framework could be a contribution. However, the authors need to provide a more detailed comparison with methods like [1, 2], highlighting the specific differences in the formulation, the type of continuity constraint used, and the overall architecture. A more thorough analysis of the advantages and disadvantages of each approach would be beneficial. For example, the authors could discuss how their method handles different types of physical systems compared to the methods in [1, 2], and what are the computational trade-offs.

To strengthen the theoretical analysis, the authors should extend their analysis to consider the stability of the learned trajectory over extended time horizons. The current analysis only focuses on the uniqueness of the trajectory between adjacent states, which is not sufficient to guarantee the long-term stability of the simulation. The authors should also consider the impact of numerical integration errors on the uniqueness of the learned trajectory. A more rigorous analysis of the error propagation during numerical integration would be beneficial. Furthermore, the authors should provide a more detailed explanation of how the theoretical results translate into practical benefits for the proposed method. For example, how does the theoretical analysis inform the choice of hyperparameters or the design of the GNN architecture?

The experimental evaluation needs to be significantly expanded to include more recent and relevant baselines. The authors should consider including methods such as [3, 4, 5, 6, 7] in their comparison. The experimental evaluation should also include more diverse datasets and tasks to demonstrate the generalizability of the proposed method. The current experiments are limited to relatively simple systems, and it is unclear how the method would perform on more complex and realistic physical systems. The authors should also provide more details about the experimental setup, including the specific hyperparameter settings and the training procedure. The authors should also consider including ablation studies to analyze the impact of different components of their method.

### Questions

- How does the proposed method compare to other methods that incorporate the second-order continuity?
- How does the proposed method perform on more complex and realistic physical systems?
- How does the proposed method handle different types of physical systems?

### Rating

5

### Confidence

4

**********
