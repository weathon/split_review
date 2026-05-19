### Summary

This paper proposes SEGNO, a new method that combines equivariant GNNs with Neural ODEs to model multi-object physical systems. The key contributions of the paper are:

1. The paper identifies two main limitations of existing equivariant GNNs: (a) they model discrete transitions between system states, which may not capture the continuous nature of physical dynamics, and (b) they only consider first-order velocity information, neglecting the importance of second-order acceleration in physical systems.
2. To address these limitations, the paper proposes SEGNO, which incorporates Neural ODEs into equivariant GNNs to model continuous trajectories between system states. This approach allows for a more accurate representation of physical dynamics and better generalization to unseen states.
3. The paper provides theoretical analysis showing that SEGNO can learn a unique trajectory between adjacent states and bounds the approximation error.
4. Empirical results on simulated N-body systems, MD22, and CMU motion capture datasets demonstrate that SEGNO outperforms state-of-the-art baselines, achieving significant improvements in prediction accuracy and generalization ability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The problem formulation and method description are clear and easy to understand.
- The proposed method is simple and easy to implement. The idea of incorporating the second-order continuity into the framework is straightforward and intuitive.
- The authors provide theoretical analysis to show that the proposed method can learn a unique trajectory between adjacent states.
- The empirical results are comprehensive and demonstrate the effectiveness of the proposed method on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is not novel enough. The idea of incorporating the second-order continuity into the framework is not new. For example, [1, 2] have already explored this idea. The authors should clearly articulate the differences between the proposed method and these existing works.
- The theoretical analysis is not solid enough. The authors only show that the proposed method can learn a unique trajectory between adjacent states. However, it is not clear how this analysis can be extended to the whole trajectory. The analysis does not address the stability of the learned trajectory over extended time horizons, which is crucial for physical simulations. The analysis also does not consider the impact of numerical integration errors on the uniqueness of the learned trajectory.
- The experiments are not comprehensive enough. The authors only compare their method with some baselines. More recent baselines should be included for a more comprehensive evaluation. The experimental evaluation should include more diverse datasets and tasks to demonstrate the generalizability of the proposed method. The current experiments are limited to relatively simple systems, and it is unclear how the method would perform on more complex and realistic physical systems.
- The presentation of the paper can be further improved. For example, the authors should provide more details about the implementation of the proposed method. The description of the experimental setup is also not detailed enough. The authors should also provide more details about the hyperparameter settings and the training procedure.

### Suggestions

The paper would benefit from a more thorough comparison with existing methods that also incorporate second-order continuity. While the authors mention that their approach differs by learning instantaneous accelerations rather than average accelerations, a more detailed analysis of the specific differences in the mathematical formulations and the implications for the learned trajectories is needed. For instance, a comparison of the loss functions used in the proposed method and the methods in [1, 2] would be beneficial. Furthermore, the authors should provide a more in-depth discussion of the advantages and disadvantages of learning instantaneous accelerations versus average accelerations, including a theoretical analysis of the error bounds and convergence properties of each approach. This would help to clarify the novelty and contribution of the proposed method.

To strengthen the theoretical analysis, the authors should extend their analysis beyond the local uniqueness of trajectories. A more comprehensive analysis should address the global stability and convergence properties of the learned trajectories over extended time horizons. This could involve analyzing the spectral properties of the Neural ODE solver and the impact of numerical integration errors on the long-term behavior of the system. The authors should also investigate how the theoretical error bounds derived for adjacent states translate to the overall error over longer time intervals. Furthermore, the analysis should consider the impact of the choice of Neural ODE solver and its parameters on the stability and accuracy of the learned trajectories. A more rigorous analysis of these aspects would significantly enhance the theoretical foundation of the paper.

The experimental evaluation needs to be significantly expanded to include more recent and relevant baselines. The authors should include comparisons with state-of-the-art methods in the field of neural simulation, such as those based on Hamiltonian Neural Networks or other approaches that explicitly model physical constraints. The experimental evaluation should also include more diverse datasets and tasks to demonstrate the generalizability of the proposed method. For example, the authors could evaluate the method on more complex physical systems, such as fluid dynamics or granular materials. Furthermore, the authors should provide a more detailed description of the experimental setup, including the specific hyperparameter settings and the training procedure. This would allow for a more thorough evaluation of the proposed method and facilitate reproducibility.

### Questions

- How does the proposed method compare to other methods that incorporate the second-order continuity?
- How does the proposed method handle different types of physical systems?
- How does the proposed method perform on more complex and realistic physical systems?

### Rating

8

### Confidence

4

**********
