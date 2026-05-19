### Summary

The paper proposes a new approach for continual learning under specific trade-offs (CLuST), where the goal is to generate models that balance stability and plasticity according to user-defined preferences. The proposed method, Imprecise Bayesian Continual Learning (IBCL), updates a knowledge base in the form of a convex set of distributions and generates models via convex combination without retraining. The authors demonstrate the effectiveness of IBCL on image classification and NLP benchmarks, showing improvements in task accuracy and backward transfer compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel problem formulation for continual learning under specific trade-offs (CLuST), which is a valuable contribution to the field. The authors provide a clear and well-motivated problem definition, highlighting the importance of balancing stability and plasticity in continual learning scenarios.

2. The proposed IBCL algorithm is theoretically grounded and well-explained. The authors provide a detailed analysis of the algorithm's properties, including its ability to generate Pareto-optimal models and its probabilistic guarantees. The use of a Bayesian approach and the concept of finitely generated credal sets (FGCS) are innovative and contribute to the theoretical rigor of the paper.

3. The experimental results are comprehensive and demonstrate the effectiveness of IBCL. The authors evaluate the algorithm on various benchmarks and show significant improvements in task accuracy and backward transfer compared to existing methods. The ablation studies provide valuable insights into the impact of different hyperparameters on the algorithm's performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the computational complexity of the proposed algorithm. While the authors mention that the training overhead is constant, a more rigorous analysis of the time and space complexity would be beneficial. Specifically, the paper should analyze the complexity of updating the FGCS and generating new models, considering the number of tasks, the size of the knowledge base, and the dimensionality of the parameter space. A comparison with the computational complexity of existing methods would also be valuable to understand the trade-offs involved.

2. The paper could benefit from a more thorough comparison with state-of-the-art continual learning methods. While the authors compare IBCL with some baselines, a more comprehensive evaluation against a wider range of methods would strengthen the paper's claims. Specifically, the comparison should include methods that explicitly address the stability-plasticity trade-off, such as regularization-based methods (e.g., EWC, SI) and replay-based methods (e.g., iCaRL, Deep Generative Replay). This would provide a more complete picture of the proposed method's strengths and weaknesses relative to the current state of the art.

### Suggestions

To address the lack of detailed computational complexity analysis, the authors should provide a formal analysis of the time and space complexity of the IBCL algorithm. This analysis should include a breakdown of the computational cost associated with each step of the algorithm, such as updating the FGCS and generating new models. The analysis should consider the number of tasks (T), the size of the knowledge base (K), and the dimensionality of the parameter space (D). For example, the authors could analyze the complexity of the convex combination operation in terms of K and D, and discuss how the size of the FGCS impacts the overall computational cost. Furthermore, a comparison with the computational complexity of existing methods, such as EWC and replay-based methods, would be valuable to understand the trade-offs involved. This would allow readers to better assess the practical applicability of the proposed method in resource-constrained environments.

To strengthen the experimental evaluation, the authors should include a more comprehensive comparison with state-of-the-art continual learning methods. This comparison should include methods that explicitly address the stability-plasticity trade-off, such as regularization-based methods (e.g., EWC, SI) and replay-based methods (e.g., iCaRL, Deep Generative Replay). The authors should also consider including methods that use different learning paradigms, such as meta-learning approaches. The comparison should be performed on a wider range of datasets and tasks to ensure the robustness of the results. Furthermore, the authors should provide a detailed analysis of the performance of IBCL under different scenarios, such as varying degrees of task similarity and different levels of task complexity. This would provide a more complete picture of the proposed method's strengths and weaknesses relative to the current state of the art.

Finally, the authors should provide more details on the implementation of the IBCL algorithm, including the specific choices of hyperparameters and the optimization techniques used. This would allow other researchers to reproduce the results and build upon the proposed method. The authors should also discuss the limitations of the proposed method and potential directions for future research. For example, the authors could discuss the challenges of applying IBCL to more complex tasks or datasets, and explore potential solutions to these challenges. This would provide a more complete and balanced view of the proposed method and its potential impact on the field of continual learning.

### Questions

1. Can the authors provide more details on the computational complexity of the IBCL algorithm? How does the complexity scale with the number of tasks and the size of the knowledge base?

2. How does the performance of IBCL compare to other state-of-the-art continual learning methods, particularly those that explicitly address the stability-plasticity trade-off?

### Rating

6

### Confidence

4

**********
