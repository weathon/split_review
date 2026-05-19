### Summary

This paper proposes a new method for identifying the domain of unknown models. Unlike traditional methods that rely on static datasets like ImageNet, this approach uses generative algorithms, combining Stable Diffusion, CLIP, and BLIP to iteratively refine descriptions and classify the domain of the model. The proposed method is validated across various scenarios, including identifying input data domains for classifiers, using generated datasets for further investigation, and determining domains for real-world models.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. This paper proposes a new method for identifying the domain of unknown models, which is interesting.
2. The proposed method is validated across various scenarios, including identifying input data domains for classifiers, using generated datasets for further investigation, and determining domains for real-world models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of the corpus-based approach used as a baseline, making it difficult to understand the comparison. The description provided is insufficient to grasp the nuances of the baseline method, particularly how the 'operational characteristics' of a model are quantified and used in conjunction with dataset metadata. This lack of clarity hinders a proper assessment of the proposed method's advantages.
2. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. The iterative refinement process, involving multiple components like Stable Diffusion, CLIP, and BLIP, suggests a potentially high computational overhead. However, the paper lacks a quantitative analysis of the time and resources required for each step, making it difficult to evaluate the practical feasibility of the approach, especially for large-scale applications.
3. The paper lacks a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, such as the balance between relevance and generality. While the paper mentions a parameter λ, it does not explore how different values of λ affect the performance of the method. A sensitivity analysis is needed to understand the robustness of the method and to provide guidelines for selecting appropriate hyperparameter values. The absence of such analysis makes it difficult to assess the reliability of the results.

### Suggestions

The paper should provide a more detailed explanation of the corpus-based approach used as a baseline. Specifically, the authors should clarify how the 'operational characteristics' of a model are quantified and integrated with dataset metadata. For example, if the operational characteristic is the model's accuracy on different subsets of the data, the paper should explain how this accuracy is calculated and used in the baseline method. Furthermore, the paper should provide a concrete example of how the baseline method selects a subset of data from a large dataset like ImageNet, and how this selection is used to determine the model's domain. This would allow for a more meaningful comparison with the proposed method and a better understanding of the baseline's limitations.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and resources required for each step of the proposed method. This should include the time taken for the iterative refinement process, the cost of using Stable Diffusion, CLIP, and BLIP, and the memory requirements for each component. The analysis should also consider the impact of different parameters, such as the number of iterations and the size of the generated datasets, on the overall computational cost. Furthermore, the authors should compare the computational cost of the proposed method with the baseline method, providing a clear understanding of the trade-offs between accuracy and computational efficiency. This analysis should be presented in a table or graph, making it easy to understand and interpret.

Finally, the paper should include a detailed sensitivity analysis of the proposed method to the choice of hyperparameters. This analysis should explore how different values of λ affect the performance of the method, and how the optimal value of λ can be determined. The authors should also investigate the sensitivity of the method to other hyperparameters, such as the number of iterations and the size of the generated datasets. The analysis should include a quantitative evaluation of the method's performance under different hyperparameter settings, and provide guidelines for selecting appropriate values. This would help to ensure the robustness of the method and to provide a clear understanding of its limitations.

### Questions

1. Could you provide a more detailed explanation of the corpus-based approach used as a baseline in your experiments? This would help in understanding the comparison and the advantages of your proposed method.
2. Can you provide a detailed analysis of the computational cost associated with your proposed method? This would help in understanding the practicality of the approach, especially for large-scale applications.
3. How sensitive is the proposed method to the choice of hyperparameters, such as the balance between relevance and generality? A detailed analysis of this would help in understanding the robustness of the method.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
