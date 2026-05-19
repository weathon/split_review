### Summary

This paper presents MUBEN, a benchmark for evaluating uncertainty quantification methods in molecular representation models. The study investigates the performance of various UQ methods across different molecular representation models and tasks, including classification and regression. The findings suggest that Deep Ensembles consistently improve performance, while temperature scaling and MC dropout are effective for classification tasks. The study also highlights the importance of model architecture and task type in selecting appropriate UQ methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The benchmark covers a wide range of molecular representation models and uncertainty quantification methods, providing a comprehensive analysis of their performance.
3. The paper identifies trends in UQ method performance based on model architecture and task type, which can guide future research and practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear guideline on how to select the best UQ method for a given task and model architecture. The authors only provide a general guideline based on the type of task (classification vs. regression) and the architecture of the model (e.g., Uni-Mol vs. DNN). However, there is no clear explanation of how to choose the best UQ method for a specific task and model architecture. For example, the authors do not provide a detailed analysis of the trade-offs between different UQ methods in terms of computational cost, calibration performance, and uncertainty estimation accuracy. This makes it difficult for practitioners to choose the most appropriate UQ method for their specific needs.
2. The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of UQ methods. The authors mention using coarse-grained hyperparameter grids, but there is no discussion of how these hyperparameters affect the results. For example, the authors do not analyze the sensitivity of the results to different learning rates, batch sizes, or optimization algorithms. This makes it difficult to reproduce the results and to apply the methods to new datasets.
3. The paper does not provide a detailed analysis of the limitations of the proposed benchmark. The authors do not discuss the potential biases in the datasets or the limitations of the evaluation metrics. For example, the authors do not analyze the performance of the UQ methods on different subsets of the data or on different types of molecules. This makes it difficult to assess the generalizability of the results and to identify areas for future research.

### Suggestions

The paper would benefit significantly from a more detailed discussion on how to select the most appropriate uncertainty quantification (UQ) method for a given task and model architecture. Currently, the paper provides a general guideline based on task type (classification vs. regression) and model architecture (e.g., Uni-Mol vs. DNN), but it lacks specific recommendations for practitioners. A more in-depth analysis of the trade-offs between different UQ methods is needed. For instance, the authors could explore the computational cost, calibration performance, and uncertainty estimation accuracy of each method in more detail. This could involve a sensitivity analysis of the hyperparameters for each UQ method, showing how different settings affect the results. Furthermore, the authors should provide concrete examples of how to choose a UQ method based on the specific requirements of a real-world application. This would make the benchmark more useful for practitioners who need to select the most appropriate UQ method for their specific needs. 

In addition to the selection of UQ methods, the paper should also provide a more detailed analysis of the impact of different hyperparameters on the performance of UQ methods. The authors mention using coarse-grained hyperparameter grids, but there is no discussion of how these hyperparameters affect the results. For example, the authors should analyze the sensitivity of the results to different learning rates, batch sizes, and optimization algorithms. This could involve conducting a more thorough hyperparameter search for each UQ method and reporting the optimal settings for each method. Furthermore, the authors should discuss the potential impact of different hyperparameter settings on the calibration performance and uncertainty estimation accuracy of each method. This would make the benchmark more robust and reliable, and it would allow practitioners to apply the methods to new datasets with confidence. 

Finally, the paper should include a more detailed analysis of the limitations of the proposed benchmark. The authors should discuss the potential biases in the datasets and the limitations of the evaluation metrics. For example, the authors should analyze the performance of the UQ methods on different subsets of the data or on different types of molecules. This would help to assess the generalizability of the results and to identify areas for future research. The authors should also discuss the limitations of the evaluation metrics used in the benchmark and suggest alternative metrics that could be used to evaluate the performance of UQ methods. This would make the benchmark more comprehensive and reliable, and it would allow practitioners to choose the most appropriate UQ method for their specific needs.

### Questions

1. How do the results of MUBEN generalize to other molecular property prediction tasks, such as those involving protein-ligand interactions or drug discovery? 
2. Can the authors provide more details on the computational cost associated with each UQ method, especially for large-scale molecular property prediction tasks?
3. How sensitive are the results to the choice of hyperparameters for each UQ method? Did the authors perform a sensitivity analysis to ensure the robustness of the findings?

### Rating

6

### Confidence

3

**********
