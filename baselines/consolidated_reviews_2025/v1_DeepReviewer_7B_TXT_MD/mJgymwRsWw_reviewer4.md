### Summary

This paper proposes a new approach to active probabilistic drug discovery (APDD), which iteratively updates the binding probabilities of molecules to a target protein of interest. The method consists of three consecutive steps of probabilistic clustering, molecular docking, and active wet-experiment. The authors demonstrate the effectiveness of their approach on two benchmark datasets and show that it achieves substantial cost savings with an average reduction of 80% in computational docking expenses and 70% in wet experimental costs, while maintaining high accuracy in lead molecule discovery.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-organized and easy to follow.

2. The authors have conducted extensive experiments on two benchmark datasets, demonstrating the effectiveness of their approach.

3. The authors have provided a detailed description of the proposed method, including the probabilistic clustering, molecular docking, and active wet-experiment steps.

### Weaknesses

#### Some Related Works


#### comment

1. The authors have not provided any theoretical analysis of the proposed method, such as convergence analysis or error bounds.

2. The authors have not provided a comparison of their method with other state-of-the-art methods in the field of active probabilistic drug discovery.

3. The authors have not discussed the limitations of their method and potential directions for future research.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the proposed method. Specifically, a convergence analysis is needed to demonstrate that the iterative process of probabilistic clustering, molecular docking, and active wet-experiment will converge to a stable solution. This analysis should consider the impact of each step on the overall performance and provide guarantees on the quality of the final results. Furthermore, error bounds should be derived to quantify the uncertainty associated with the binding probability estimates. This would provide a measure of the reliability of the method and allow for a more informed decision-making process in drug discovery. Without these theoretical underpinnings, the practical utility of the method remains unclear, and it is difficult to assess its robustness and generalizability.

In addition to the theoretical analysis, the paper needs a more comprehensive comparison with existing state-of-the-art methods in active probabilistic drug discovery. The authors should benchmark their approach against other active learning strategies, such as those based on Gaussian processes or Bayesian neural networks, to demonstrate its advantages and limitations. A detailed comparison should include not only the performance metrics but also the computational cost and the sensitivity to different parameters. This would help to contextualize the contribution of the proposed method and highlight its unique strengths and weaknesses. Without such a comparison, it is difficult to assess the novelty and practical value of the proposed approach.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential avenues for future research. The authors should discuss the sensitivity of their method to the choice of clustering algorithm, the parameters of the probabilistic model, and the selection of the active wet-experiment molecules. They should also consider the scalability of their method to larger datasets and more complex protein targets. Furthermore, the authors should discuss the potential impact of data bias and noise on the performance of their method. Addressing these limitations would provide a more balanced and realistic view of the proposed approach and guide future research in this area.

### Questions

1. What is the convergence rate of the proposed method?

2. What is the computational complexity of the proposed method?

3. What is the sensitivity of the proposed method to the choice of clustering algorithm and the parameters of the probabilistic model?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
