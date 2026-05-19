### Summary

This paper proposes a new approach to active probabilistic drug discovery (APDD), which iteratively updates the binding probabilities of molecules to a target protein of interest. The method consists of three consecutive steps of probabilistic clustering, molecular docking, and active wet-experiment. The authors demonstrate the effectiveness of their approach on two benchmark datasets and show that it achieves substantial cost savings with an average reduction of 80% in computational docking expenses and 70% in wet experimental costs, while maintaining high accuracy in lead molecule discovery.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-organized and easy to follow.

2. The authors have conducted extensive experiments on two benchmark datasets, demonstrating the effectiveness of their approach.

### Weaknesses

#### Some Related Works


#### comment

1. The authors have not provided any theoretical analysis of the proposed method, such as convergence analysis or error bounds.

2. The authors have not provided a comparison of their method with other state-of-the-art methods in the field of active probabilistic drug discovery.

3. The authors have not discussed the limitations of their method and potential directions for future research.

### Suggestions

The lack of theoretical analysis is a significant weakness. While the empirical results are promising, without a convergence analysis, it's difficult to ascertain the robustness and reliability of the method. For instance, it would be beneficial to understand how the probabilistic clustering and active wet-experiment steps interact, and whether the iterative process is guaranteed to converge to a stable solution. Furthermore, error bounds would provide a measure of the uncertainty associated with the binding probability estimates, which is crucial for practical applications in drug discovery. The authors should consider exploring techniques from the field of stochastic optimization or Bayesian inference to establish such theoretical guarantees. This would significantly strengthen the paper and provide a more solid foundation for the proposed method.

The absence of a comparison with state-of-the-art methods is another major concern. The authors should benchmark their approach against existing active learning strategies for drug discovery, or at least provide a detailed comparison with other probabilistic clustering methods. This would help to contextualize the contribution of the proposed method and highlight its advantages and disadvantages. For example, comparing against methods that use Gaussian processes for uncertainty quantification or Bayesian neural networks for active learning would be valuable. Without such comparisons, it is difficult to assess the novelty and effectiveness of the proposed approach. The authors should also consider including a discussion of the computational complexity of their method compared to other approaches.

Finally, the paper would benefit from a more thorough discussion of the limitations of the proposed method and potential avenues for future research. For example, the authors should discuss the sensitivity of their method to the choice of clustering algorithm, the parameters of the probabilistic model, and the selection of the active wet-experiment molecules. They should also consider the scalability of their method to larger datasets and more complex protein targets. Furthermore, the authors should discuss the potential impact of data bias and noise on the performance of their method. Addressing these limitations would provide a more balanced and realistic view of the proposed approach and guide future research in this area.

### Questions

1. What is the convergence rate of the proposed method?

2. What is the computational complexity of the proposed method?

3. What is the sensitivity of the proposed method to the choice of clustering algorithm and the parameters of the probabilistic model?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
