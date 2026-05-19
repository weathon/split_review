### Summary

This paper proposes a novel active probabilistic drug discovery (APDD) method, which iteratively updates the binding probabilities of molecules to progressively enhance drug discovery performance with three consecutive steps of probabilistic clustering, selective docking, and active wet-experiment. The results demonstrate the feasibility and efficiency of our approach, showcasing substantial cost savings with an average reduction of 80% in computational docking expenses and 70% in wet experimental costs, while maintaining high accuracy in lead molecule discovery.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective.
3. The experimental results are comprehensive and promising.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the baseline methods, such as the hyperparameters and implementation details. Specifically, the choice of similarity metric for clustering, the specific parameters used for the docking simulations, and the details of the active learning strategy are not sufficiently described. This lack of detail makes it difficult to reproduce the results and assess the true contribution of the proposed method.
2. The authors should compare the proposed method with more state-of-the-art methods to demonstrate its superiority. The current comparison is limited, and it is unclear how the proposed method performs against other established active learning or virtual screening techniques. A more thorough comparison is needed to establish the method's competitive advantage.
3. The authors should provide more details about the datasets used in the experiments, such as the size, diversity, and quality of the molecules. The description of the datasets is too brief, and it is not clear whether the datasets are representative of real-world drug discovery challenges. Information about the distribution of molecular properties and the presence of potential biases is also missing.
4. The authors should discuss the limitations of the proposed method and potential future directions. The paper lacks a critical discussion of the method's shortcomings, such as its sensitivity to the choice of parameters, its performance on different types of targets, and its scalability to larger datasets. Furthermore, the paper does not explore potential avenues for future research or improvements to the method.

### Suggestions

The authors should provide a more detailed description of the baseline methods, including the specific algorithms used, their hyperparameters, and the rationale behind their selection. For example, if a molecular dynamics-based method is used for comparison, the details of the force field, simulation time, and convergence criteria should be provided. Similarly, for docking-based methods, the specific docking software, search space definition, and scoring function should be clearly stated. This level of detail is crucial for reproducibility and for a fair assessment of the proposed method's performance. Furthermore, the authors should justify the choice of baseline methods and explain why they are appropriate for comparison with the proposed approach. A more thorough description of the baseline methods will allow readers to better understand the context of the results and the advantages of the proposed method.

To strengthen the paper, the authors should compare their method with a wider range of state-of-the-art techniques in active learning and virtual screening. This should include methods that utilize different types of molecular representations, such as graph neural networks or sequence-based models, and different active learning strategies, such as uncertainty sampling or query-by-committee. The comparison should not only focus on overall performance but also on specific aspects such as the number of wet-lab experiments required to achieve a certain level of performance, the diversity of the selected molecules, and the computational cost. A more comprehensive comparison will provide a more robust evaluation of the proposed method and highlight its unique contributions. The authors should also consider including ablation studies to assess the impact of different components of their method.

The authors should provide a more detailed characterization of the datasets used in the experiments. This should include information about the size of the dataset, the distribution of molecular weights and other relevant properties, and the diversity of the chemical space covered by the molecules. The authors should also discuss the quality of the data, including the presence of potential biases or errors. For example, if the dataset is derived from a commercial database, the authors should acknowledge any potential limitations associated with that source. Furthermore, the authors should justify the choice of datasets and explain why they are appropriate for evaluating the proposed method. A more detailed description of the datasets will allow readers to better understand the scope and limitations of the experimental results.

### Questions

Please refer to the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
