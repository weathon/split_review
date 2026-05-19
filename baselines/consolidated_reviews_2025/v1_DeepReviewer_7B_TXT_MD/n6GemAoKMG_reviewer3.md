### Summary

The paper introduces a novel attack method for graph neural networks (GNNs) called Evolutionary Attack (EvA), which leverages a genetic algorithm to directly optimize the objective function without relying on gradients. This approach addresses the limitations of traditional gradient-based attacks, which often suffer from suboptimal solutions due to the relaxation of the original discrete optimization problem. EvA demonstrates superior performance in reducing the effectiveness of robustness certificates and breaking conformal sets on graphs, outperforming state-of-the-art gradient-based methods. The paper also explores new attack objectives, such as reducing the certified ratio and decreasing the coverage, and shows that EvA is effective in these settings as well.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to adversarial attacks on graphs by leveraging a genetic algorithm, which directly optimizes the objective function without relying on gradients. This is a significant departure from traditional gradient-based methods and addresses the limitations of relaxing the original discrete optimization problem.
- The paper demonstrates the effectiveness of EvA in reducing the certified ratio and decreasing the coverage, which are important metrics for evaluating the robustness of GNNs. The results show that EvA outperforms state-of-the-art gradient-based methods in these settings.
- The paper provides a comprehensive evaluation of EvA on several datasets and models, including CoraML, Citeseer, and PubMed. The results show that EvA is effective in attacking GNNs, even when the models are adversarially trained.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for understanding its scalability to larger graphs.
- The paper does not compare the proposed method with other non-gradient-based adversarial attack methods, which would help to establish its relative strengths and weaknesses.
- The paper does not discuss the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed Evolutionary Attack (EvA). While the authors mention the use of a genetic algorithm, a detailed analysis of the time and space complexity is crucial for assessing its practical applicability, especially on large-scale graphs. Specifically, the paper should analyze how the number of nodes, edges, and the population size of the genetic algorithm affect the runtime and memory usage. Furthermore, it would be valuable to compare the computational cost of EvA with that of other adversarial attack methods, including both gradient-based and non-gradient-based approaches. This comparison should not only focus on the total runtime but also on the number of forward passes required, which can be a limiting factor in many scenarios. A clear understanding of these computational aspects is essential for determining the scalability and feasibility of the proposed method in real-world applications.

To strengthen the paper's contribution, it is essential to compare the proposed method with other non-gradient-based adversarial attack techniques. While the authors compare EvA with a gradient-based method, a comparison with other methods that do not rely on gradients would provide a more comprehensive understanding of its relative strengths and weaknesses. This comparison should not only focus on the attack success rate but also consider other metrics such as the number of forward passes, the computational time, and the memory usage. If no other non-gradient-based methods exist for graph attacks, the authors should discuss the challenges of adapting existing methods to the graph domain and why a gradient-free approach is necessary. This discussion would help to contextualize the novelty and effectiveness of EvA. Furthermore, it would be beneficial to analyze the performance of EvA with different hyperparameter settings and discuss the sensitivity of the attack to these parameters. This analysis would provide insights into the robustness of the method and its potential limitations.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This discussion should address the sensitivity of the attack to hyperparameters, such as the population size, mutation rate, and the number of evolutionary steps. It would be valuable to analyze how these parameters affect the performance of the attack and provide guidelines for selecting appropriate values. Additionally, the paper should discuss the robustness of the attack to different types of graph structures, such as sparse and dense graphs, and graphs with different degree distributions. This analysis should include empirical results on the performance of the attack on different types of graphs and discuss the potential reasons for any observed differences. Furthermore, the authors should discuss the limitations of the attack in terms of the types of objectives that can be optimized and the challenges of optimizing more complex objectives. This discussion would provide a more complete picture of the capabilities and limitations of the proposed method.

### Questions

- How does the computational complexity of the proposed method scale with the size of the graph?
- How does the proposed method compare with other non-gradient-based adversarial attack methods?
- What are the limitations of the proposed method, such as its sensitivity to hyperparameters or its robustness to different types of graph structures?

### Rating

6

### Confidence

3

**********
