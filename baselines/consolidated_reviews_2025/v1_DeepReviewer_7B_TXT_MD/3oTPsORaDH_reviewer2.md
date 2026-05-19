### Summary

This paper proposes SEGNO, a new method that integrates equivariant graph neural networks with Neural ODEs to model complex multi-object physical systems. The key contributions of the paper are as follows:

1. The paper identifies two main limitations of existing equivariant GNNs: (a) they model discrete transitions between system states, which may not capture the continuous nature of physical dynamics, and (b) they only consider first-order velocity information, neglecting the importance of second-order acceleration in physical systems. 
2. To address these limitations, the paper proposes SEGNO, which incorporates Neural ODEs into equivariant GNNs to model continuous trajectories between system states. This approach allows for a more accurate representation of physical dynamics and better generalization to unseen states.
3. The paper provides theoretical analysis showing that SEGNO can learn a unique trajectory between adjacent states and bounds the approximation error. 
4. Empirical results on simulated N-body systems, MD22, and CMU motion capture datasets demonstrate that SEGNO outperforms state-of-the-art baselines, achieving significant improvements in prediction accuracy and generalization ability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a clear and well-motivated problem formulation, identifying the limitations of existing equivariant GNNs in modeling continuous physical dynamics. The motivation for incorporating Neural ODEs to address these limitations is well-justified.
2. The theoretical analysis of SEGNO is rigorous and provides valuable insights into the properties of the model, including the existence and uniqueness of learned trajectories and error bounds. This analysis strengthens the theoretical foundation of the proposed method.
3. The empirical results are comprehensive and demonstrate the effectiveness of SEGNO on multiple datasets. The paper includes experiments on simulated N-body systems, MD22, and CMU motion capture datasets, showing significant improvements over state-of-the-art baselines. The ablation studies and sensitivity analyses further validate the design choices of the model.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides theoretical analysis, it lacks a detailed discussion on the practical implications of the theoretical results. For example, how do the theoretical error bounds translate into real-world performance? What are the limitations of the theoretical analysis in practical scenarios? Specifically, the paper does not discuss how the Lipschitz continuity assumptions, which are crucial for the theoretical results, might be violated in real-world physical systems, and how this would affect the performance of SEGNO. Furthermore, the paper does not explore the impact of numerical integration errors on the theoretical bounds, which could be significant in practical applications.
2. The paper does not provide a thorough analysis of the computational complexity of SEGNO. How does the computational cost scale with the number of objects and the length of the simulation? What are the practical limitations of the method in terms of computational resources? The paper should include a detailed analysis of the time and memory complexity of the proposed method, especially in comparison to the baselines. It is also important to discuss the practical implications of the computational cost, such as the maximum simulation time that can be achieved with a given computational budget.
3. The paper does not discuss the limitations of the proposed method. For example, under what conditions might SEGNO fail to accurately model physical dynamics? What are the potential failure modes of the method? The paper should address the limitations of the method, such as its sensitivity to hyperparameter choices, the potential for numerical instability, and the applicability of the method to different types of physical systems. It is also important to discuss the limitations of the method in terms of the types of physical phenomena that it can model, such as systems with strong non-linearities or chaotic behavior.

### Suggestions

The paper would benefit from a more in-depth discussion of the practical implications of the theoretical results. Specifically, the authors should elaborate on how the derived error bounds translate into real-world performance metrics, such as prediction accuracy and generalization ability. It would be helpful to provide a concrete example of how the theoretical error bounds can be used to guide the selection of hyperparameters or to predict the performance of the model on unseen data. Furthermore, the authors should discuss the limitations of the theoretical analysis, such as the assumptions of Lipschitz continuity and the potential impact of numerical integration errors. A more detailed analysis of these aspects would strengthen the theoretical foundation of the paper and provide a more complete understanding of the proposed method. The authors should also consider including a discussion on the robustness of the theoretical results to violations of these assumptions.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the time and memory complexity of SEGNO, including a comparison with the baselines. This analysis should consider the impact of the number of objects, the length of the simulation, and the complexity of the neural network architecture. The authors should also discuss the practical limitations of the method in terms of computational resources, such as the maximum simulation time that can be achieved with a given computational budget. It would be beneficial to include a discussion on the trade-offs between computational cost and accuracy, and to provide guidelines for selecting appropriate model parameters and simulation settings. Furthermore, the authors should consider including a discussion on the potential for optimizing the computational performance of the method, such as through parallelization or other techniques.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. The authors should address the potential failure modes of the method, such as its sensitivity to hyperparameter choices, the potential for numerical instability, and the applicability of the method to different types of physical systems. It is important to discuss the limitations of the method in terms of the types of physical phenomena that it can model, such as systems with strong non-linearities or chaotic behavior. The authors should also discuss the limitations of the method in terms of the types of physical systems that it can model, such as systems with complex interactions or external forces. A more comprehensive discussion of these limitations would provide a more balanced and realistic assessment of the proposed method and would help guide future research in this area.

### Questions

1. How does the proposed method handle systems with complex interactions or external forces that are not captured by the GNN backbone?
2. How does the method perform on systems with non-constant acceleration or external forces that are not captured by the GNN backbone?
3. How does the method handle systems with a large number of objects or long simulation times?
4. How does the method compare to other methods that use different types of neural network architectures or different types of physical models?
5. How does the method handle systems with non-Euclidean geometries or non-Euclidean spaces?

### Rating

6

### Confidence

3

**********
