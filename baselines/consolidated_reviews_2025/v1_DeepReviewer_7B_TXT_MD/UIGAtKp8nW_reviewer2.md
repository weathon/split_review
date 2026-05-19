### Summary

The authors present MUBEN, a benchmark designed to evaluate uncertainty quantification (UQ) methods for molecular representation models. The study aims to address the issue of overconfidence in large-scale models by assessing the performance of UQ methods across various molecular representation models, including deterministic and ensemble-based approaches, and different types of molecular descriptors. The benchmark includes a comprehensive set of molecular property prediction tasks and uncertainty metrics, allowing for a systematic comparison of UQ methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-structured and clearly written, making it accessible to a broad audience. The authors provide a thorough analysis of the results, including visualizations and discussions of the findings. The study addresses an important problem in molecular property prediction, where overconfidence in models can lead to unreliable predictions, especially in real-world applications. The benchmark covers a wide range of molecular representation models and uncertainty quantification methods, making it a valuable resource for researchers in the field.

### Weaknesses

#### Some Related Works


#### comment

The paper could benefit from a more detailed discussion of the limitations of the proposed benchmark and potential biases in the datasets used. For example, the authors could discuss the impact of dataset size and diversity on the evaluation of UQ methods. Additionally, the paper could include a more in-depth analysis of the computational cost associated with different UQ methods, which is an important factor for practical applications. The authors should also consider including a discussion on the generalizability of the findings to other molecular property prediction tasks and datasets. 

The paper could also benefit from a more detailed explanation of the specific UQ methods used in the benchmark, including their strengths and weaknesses. For example, the authors could discuss the assumptions and limitations of each method and how they might affect the results. Furthermore, the authors should consider including a more detailed analysis of the uncertainty estimates produced by each method, including their calibration and sharpness. This would provide a more comprehensive understanding of the performance of each UQ method.

### Suggestions

To enhance the benchmark's robustness, the authors should incorporate a more rigorous analysis of dataset biases. This could involve stratifying datasets based on molecular properties or structural features and evaluating UQ methods across these stratified sets. For instance, if the dataset contains molecules with varying degrees of hydrogen bonding capability, the benchmark should assess whether UQ methods perform consistently across these different subsets. Furthermore, the authors should consider using datasets with known biases to evaluate the sensitivity of UQ methods to such biases. This would provide a more comprehensive understanding of the reliability of UQ methods in diverse real-world scenarios. The authors should also explore the impact of different data preprocessing techniques on the performance of UQ methods, as these techniques can introduce their own biases. A detailed analysis of these factors would significantly improve the benchmark's credibility and applicability.

In addition to dataset analysis, the authors should provide a more detailed discussion of the computational cost associated with each UQ method. This should include not only the training time but also the inference time, which is crucial for practical applications. The authors should categorize UQ methods based on their computational complexity and provide guidelines on which methods are suitable for resource-constrained environments. For example, ensemble methods are generally more computationally expensive than simpler methods like temperature scaling. The authors should also discuss the memory requirements of each method, which can be a limiting factor for large-scale molecular property prediction tasks. A clear comparison of the computational cost and performance of each UQ method would allow researchers to make informed decisions about which methods to use for their specific needs. Furthermore, the authors should consider providing a tool or framework that automates the selection of the most appropriate UQ method based on the dataset and computational resources available.

Finally, the authors should provide a more in-depth analysis of the uncertainty estimates produced by each UQ method. This should include not only the calibration of the uncertainty estimates but also their sharpness. A well-calibrated uncertainty estimate should reflect the true confidence of the model, while a sharp uncertainty estimate should provide a more precise indication of the model's uncertainty. The authors should use metrics such as Expected Calibration Error (ECE) and Brier Score to evaluate the calibration of the uncertainty estimates. They should also use metrics such as the predictive variance and the entropy of the predictive distribution to evaluate the sharpness of the uncertainty estimates. A detailed analysis of these metrics would provide a more comprehensive understanding of the performance of each UQ method and allow researchers to choose the most appropriate method for their specific needs. The authors should also discuss the limitations of each uncertainty metric and how they might affect the interpretation of the results.

### Questions

1. How do the results of MUBEN generalize to other molecular property prediction tasks, such as those involving protein-ligand interactions or drug discovery? 
2. Can the authors provide more details on the computational cost associated with each UQ method, especially for large-scale molecular property prediction tasks?
3. How sensitive are the results to the choice of hyperparameters for each UQ method? Did the authors perform a sensitivity analysis to ensure the robustness of the findings?

### Rating

6

### Confidence

3

**********
