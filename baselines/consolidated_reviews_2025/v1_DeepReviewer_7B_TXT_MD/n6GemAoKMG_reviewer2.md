### Summary

This paper proposes a novel adversarial attack method for graph neural networks (GNNs) that does not rely on gradients. The authors introduce a genetic algorithm (GA) to directly optimize the objective function, eliminating the need for a differentiable proxy loss. The proposed method, called Evolutionary Attack (EvA), is shown to outperform state-of-the-art gradient-based attacks in reducing the effectiveness of robustness certificates and breaking conformal sets on graphs. The authors also introduce new attack objectives, such as reducing the certified ratio and decreasing the coverage, and demonstrate the effectiveness of EvA in these settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective, outperforming state-of-the-art gradient-based attacks.
3. The authors provide a comprehensive evaluation of the proposed method on several datasets and models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for understanding its scalability to larger graphs.
2. The paper does not compare the proposed method with other non-gradient-based adversarial attack methods, which would help to establish its relative strengths and weaknesses.
3. The paper does not discuss the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed Evolutionary Attack (EvA). While the authors mention the use of a genetic algorithm, they do not provide a detailed breakdown of the time and space complexity of each step, such as the population initialization, fitness evaluation, and selection. A formal analysis, even if asymptotic, would be valuable to understand the scalability of the method. For example, the authors could analyze the complexity in terms of the number of nodes, edges, and the population size. Furthermore, empirical results on the runtime of the attack on different graph sizes would be helpful to demonstrate its practical scalability. This analysis should also consider the number of evolutionary steps required for convergence, and how this scales with the graph size. Without this analysis, it is difficult to assess the practical applicability of the method to large-scale graphs.

In addition to the computational complexity, the paper should include a more comprehensive comparison with other non-gradient-based adversarial attack methods. While the authors compare against a gradient-based method, it is important to compare against other methods that do not rely on gradients, if they exist, or to adapt existing methods to the graph domain. This comparison should not only focus on the attack success rate, but also on other metrics such as the number of forward passes required, the computational time, and the memory usage. This would provide a more complete picture of the relative strengths and weaknesses of EvA. If no other non-gradient-based methods exist, the authors should discuss why and what are the challenges to adapt existing methods to the graph domain. This discussion should also include a comparison of the performance of EvA with other gradient-based methods, to understand the trade-offs between gradient-based and non-gradient-based attacks. Such a comparison would help to better contextualize the performance of the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include an analysis of the sensitivity of the attack to hyperparameters, such as the population size, the mutation rate, and the number of evolutionary steps. The authors should also discuss the robustness of the attack to different types of graph structures, such as sparse and dense graphs, and graphs with different degree distributions. This analysis should include empirical results on the performance of the attack on different types of graphs, and should discuss the potential reasons for any observed differences. Furthermore, the authors should discuss the limitations of the attack in terms of the types of objectives that can be optimized, and the challenges of optimizing more complex objectives. This discussion should also include a discussion of the potential for the attack to be adapted to other types of graph-based tasks, such as node classification and link prediction. Without this discussion, it is difficult to assess the generalizability and applicability of the proposed method.

### Questions

1. How does the proposed method perform on larger graphs?
2. How does the proposed method compare with other non-gradient-based adversarial attack methods?
3. What are the limitations of the proposed method?

### Rating

6

### Confidence

3

**********
