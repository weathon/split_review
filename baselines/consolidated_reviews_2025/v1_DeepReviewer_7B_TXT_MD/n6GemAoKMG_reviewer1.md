### Summary

This paper proposes a novel adversarial attack method for graphs called Evolutionary Attack (EvA), which is designed to directly optimize the objective function without relying on gradients. The authors show that EvA outperforms gradient-based methods in reducing the effectiveness of robustness certificates and breaking conformal sets on graphs. The paper also introduces new attack objectives, such as reducing the certified ratio and decreasing the coverage, and demonstrates the effectiveness of EvA in these settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a new approach to adversarial attacks on graphs that does not rely on gradients, which is a significant departure from traditional methods.
2. The authors show that EvA outperforms state-of-the-art gradient-based attacks in reducing the effectiveness of robustness certificates and breaking conformal sets on graphs.
3. The paper introduces new attack objectives, such as reducing the certified ratio and decreasing the coverage, which are not well-addressed by traditional attacks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for understanding its scalability to larger graphs.
2. The paper does not compare the proposed method with other non-gradient-based adversarial attack methods, which would help to establish its relative strengths and weaknesses.
3. The paper does not discuss the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the Evolutionary Attack (EvA). While the authors mention that the method is efficient, a formal analysis of the time and space complexity, especially in relation to the size of the graph and the number of evolutionary steps, would be beneficial. This analysis should consider the number of forward passes required for each evaluation, and how this scales with the graph size. Furthermore, it would be helpful to provide empirical results on the runtime of the attack on different graph sizes, to demonstrate its practical scalability. This would allow readers to better understand the trade-offs between attack effectiveness and computational cost, and to assess the method's applicability to real-world scenarios with large graphs. The analysis should also discuss the memory requirements of the attack, which can be a limiting factor for large graphs.

To better contextualize the performance of EvA, the paper should include a more comprehensive comparison with other non-gradient-based adversarial attack methods. While the authors compare against a gradient-based method, it is important to compare against other methods that do not rely on gradients, if they exist, or to adapt existing methods to the graph domain. This comparison should not only focus on the attack success rate, but also on other metrics such as the number of forward passes required, the computational time, and the memory usage. This would provide a more complete picture of the relative strengths and weaknesses of EvA. If no other non-gradient-based methods exist, the authors should discuss why and what are the challenges to adapt existing methods to the graph domain. This discussion should also include a comparison of the performance of EvA with other gradient-based methods, to understand the trade-offs between gradient-based and non-gradient-based attacks.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include an analysis of the sensitivity of the attack to hyperparameters, such as the population size, the mutation rate, and the number of evolutionary steps. The authors should also discuss the robustness of the attack to different types of graph structures, such as sparse and dense graphs, and graphs with different degree distributions. This analysis should include empirical results on the performance of the attack on different types of graphs, and should discuss the potential reasons for any observed differences. Furthermore, the authors should discuss the limitations of the attack in terms of the types of objectives that can be optimized, and the challenges of optimizing more complex objectives. This discussion should also include a discussion of the potential for the attack to be adapted to other types of graph-based tasks, such as node classification and link prediction.

### Questions

1. How does the computational complexity of the proposed method scale with the size of the graph?
2. How does the proposed method compare with other non-gradient-based adversarial attack methods, if they exist?
3. What are the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures?

### Rating

6

### Confidence

3

**********
