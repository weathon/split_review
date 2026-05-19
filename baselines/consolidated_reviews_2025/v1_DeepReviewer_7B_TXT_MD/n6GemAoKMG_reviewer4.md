### Summary

This paper proposes a novel attack method called Evolutionary Attack (EvA) that directly optimizes the objective function without relying on gradients. The authors show that EvA outperforms state-of-the-art gradient-based attacks on vanilla and adversarially trained models. The paper also introduces new attack objectives, such as reducing the certified ratio and decreasing the coverage, and demonstrates the effectiveness of EvA in these settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel attack method called Evolutionary Attack (EvA) that directly optimizes the objective function without relying on gradients. This is a significant departure from traditional gradient-based attacks and addresses the limitations of relaxing the original discrete optimization problem.
2. The paper provides a comprehensive evaluation of the proposed method on several datasets and models, including CoraML, Citeseer, and PubMed. The results show that EvA outperforms state-of-the-art gradient-based attacks in reducing the certified ratio and decreasing the coverage.
3. The paper introduces new attack objectives, such as reducing the certified ratio and decreasing the coverage, and demonstrates the effectiveness of EvA in these settings. This is a novel contribution to the field of adversarial attacks on graph neural networks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for understanding its scalability to larger graphs.
2. The paper does not compare the proposed method with other non-gradient-based adversarial attack methods, which would help to establish its relative strengths and weaknesses.
3. The paper does not discuss the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed Evolutionary Attack (EvA). While the authors mention the use of a genetic algorithm, a detailed breakdown of the time and space complexity of each step, such as population initialization, fitness evaluation, and selection, is necessary. This analysis should consider the number of nodes, edges, and the population size, and how these factors affect the overall runtime. Furthermore, empirical results on the runtime of the attack on different graph sizes would be helpful to demonstrate its practical scalability. This would allow readers to better understand the trade-offs between attack effectiveness and computational cost, and to assess the method's applicability to real-world scenarios with large graphs. The analysis should also discuss the memory requirements of the attack, which can be a limiting factor for large graphs.

To better contextualize the performance of EvA, the paper should include a more comprehensive comparison with other non-gradient-based adversarial attack methods. While the authors compare against a gradient-based method, it is important to compare against other methods that do not rely on gradients, if they exist, or to adapt existing methods to the graph domain. This comparison should not only focus on the attack success rate but also on other metrics such as the number of forward passes required, the computational time, and the memory usage. If no other non-gradient-based methods exist for graph attacks, the authors should discuss the challenges of adapting existing methods to the graph domain and why a gradient-free approach is necessary. This discussion should also include a comparison of the performance of EvA with other gradient-based methods, to understand the trade-offs between gradient-based and non-gradient-based attacks. Such a comparison would help to better understand the relative strengths and weaknesses of the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include an analysis of the sensitivity of the attack to hyperparameters, such as the population size, mutation rate, and the number of evolutionary steps. The authors should also discuss the robustness of the attack to different types of graph structures, such as sparse and dense graphs, and graphs with different degree distributions. This analysis should include empirical results on the performance of the attack on different types of graphs, and should discuss the potential reasons for any observed differences. Furthermore, the authors should discuss the limitations of the attack in terms of the types of objectives that can be optimized, and the challenges of optimizing more complex objectives. This discussion should also include a discussion of the potential for the attack to be adapted to other types of graph-based tasks, such as node classification and link prediction.

### Questions

1. How does the computational complexity of the proposed method scale with the size of the graph?
2. How does the proposed method compare with other non-gradient-based adversarial attack methods?
3. What are the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures?

### Rating

6

### Confidence

3

**********
