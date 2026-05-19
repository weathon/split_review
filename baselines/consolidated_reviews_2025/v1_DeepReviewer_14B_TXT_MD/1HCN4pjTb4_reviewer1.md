### Summary

This paper studies the neural collapse phenomenon in the unconstrained features model, where the features of the penultimate layer are free variables. The authors first provide a generic analysis of neural collapse under certain assumptions, such as low training error and balancedness of the linear layers. Then, they demonstrate that these assumptions hold for gradient descent training with weight decay in networks with a wide first layer. They also show that the assumptions hold when the solutions are nearly optimal or stable under large learning rates. Finally, the authors conduct experiments to validate their theoretical results.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The authors provide a detailed analysis of the neural collapse phenomenon under certain assumptions.
2. The authors demonstrate that these assumptions hold for gradient descent training with weight decay in networks with a wide first layer.

### Weaknesses

#### Some Related Works


#### comment

1. The authors assume that the features of the penultimate layer are free variables, which is not realistic. In practice, the features of the penultimate layer are learned during training and are not independent of the data. This assumption significantly simplifies the problem and may not accurately reflect the behavior of neural networks in real-world scenarios. The analysis does not account for the complex interactions between the learned features and the data distribution, which could lead to different outcomes than predicted by the theory.
2. The authors only consider the case where the network has a wide first layer, which is not always the case in practice. Many modern architectures employ narrow or even single-layer networks, and it is unclear whether the theoretical results would extend to these cases. The assumption of a wide first layer may impose a specific inductive bias that is not present in other architectures, potentially limiting the generalizability of the findings. The paper does not provide sufficient justification for why this specific architecture is crucial for their analysis.
3. The authors do not provide any experimental results to validate their theoretical findings. Without empirical evidence, it is difficult to assess the practical relevance of the theoretical claims. The paper lacks a crucial step in the scientific method, which is to test the theory against real-world data. This makes it hard to determine if the theoretical results are meaningful or just mathematical artifacts.

### Suggestions

The authors should consider relaxing the assumption of unconstrained features in the penultimate layer. One approach could be to explore the impact of different regularization techniques on the learned features and how these regularizations affect the neural collapse phenomenon. For example, they could investigate the effect of adding a penalty term to the loss function that encourages the features to be more orthogonal or to have a specific distribution. This would make the analysis more realistic and applicable to practical scenarios. Furthermore, it would be beneficial to explore how the depth of the network influences the neural collapse, as the current analysis is limited to a specific architecture with a wide first layer. It would be valuable to investigate whether the observed phenomena are consistent across different network architectures and depths, or if they are specific to the considered case. This could involve conducting experiments with various network configurations, including those with narrow or single-layer architectures, to determine the robustness of the theoretical findings. 

To strengthen the paper, the authors should provide more detailed experimental results to validate their theoretical findings. This should include a clear description of the experimental setup, including the datasets used, the network architectures, and the training parameters. The results should be presented in a way that is easy to understand and interpret, with clear metrics that quantify the extent of neural collapse. It would also be beneficial to compare the experimental results with the theoretical predictions, highlighting any discrepancies and providing possible explanations for them. The experiments should also explore the sensitivity of the results to different hyperparameters, such as the learning rate and the weight decay, to ensure that the findings are robust and not specific to a particular set of parameters. 

Finally, the authors should provide a more detailed discussion of the limitations of their analysis and the potential directions for future research. This should include a discussion of the assumptions made in the theoretical analysis and how these assumptions might affect the generalizability of the results. It would also be helpful to identify specific areas where further research is needed, such as exploring the impact of different activation functions or investigating the role of the optimization algorithm in the neural collapse phenomenon. By addressing these limitations and suggesting future research directions, the authors can provide a more complete and nuanced understanding of the neural collapse phenomenon.

### Questions

1. Can the authors provide more detailed explanations of the assumptions they make in their analysis? For example, why do they assume that the features of the penultimate layer are free variables, and how does this assumption affect their results?
2. Can the authors provide more detailed experimental results to validate their theoretical findings? For example, can they provide experiments on different datasets and network architectures?
3. Can the authors provide more detailed discussions of the limitations of their analysis and the potential directions for future research? For example, what are the key challenges in extending their analysis to more realistic scenarios, and what are the most promising directions for future research in this area?

### Rating

3

### Confidence

2

**********
