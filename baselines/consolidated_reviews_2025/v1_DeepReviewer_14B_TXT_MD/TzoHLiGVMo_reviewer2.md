### Summary

The authors propose a Transformer-based approach for symbolic regression of dynamical systems. The method is trained on a large dataset of synthetic ODEs. The authors also introduce a new benchmark dataset for evaluating dynamical symbolic regression methods. The proposed method is evaluated on the new benchmark and an existing benchmark dataset. The results show that the proposed method outperforms existing methods in terms of accuracy and robustness to noise and irregular sampling.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is the first Transformer-based approach for symbolic regression of dynamical systems.
- The authors introduce a new benchmark dataset for evaluating dynamical symbolic regression methods. The new benchmark dataset is more comprehensive and diverse than existing benchmark datasets.
- The proposed method outperforms existing methods in terms of accuracy and robustness to noise and irregular sampling.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only evaluated on two benchmark datasets. It is unclear how it would perform on other datasets or in real-world applications.
- The authors do not provide a detailed analysis of the limitations of the proposed method. It is important to understand the limitations of a method in order to determine its applicability to different problems.
- The paper does not discuss the computational cost of the proposed method in detail. It would be useful to know how the computational cost scales with the size of the dataset and the complexity of the ODEs.
- The method's performance on higher-dimensional ODEs is not thoroughly explored. While the authors mention the model can theoretically handle higher dimensions, the practical limitations and performance degradation are not clearly addressed with empirical evidence.
- The paper lacks a discussion on the sensitivity of the method to hyperparameter choices. It is unclear how the performance of the method varies with different hyperparameter settings and what are the optimal settings for different types of ODEs.

### Suggestions

The authors should provide a more comprehensive evaluation of their method by testing it on a wider range of datasets, including real-world datasets. This would help to better understand the generalizability of the method and its applicability to different types of problems. Specifically, the authors could consider datasets from different domains, such as physics, biology, or chemistry, to assess the method's performance in various contexts. Furthermore, it would be beneficial to evaluate the method on datasets with varying levels of noise and irregular sampling to better understand its robustness. The authors should also consider comparing their method with other state-of-the-art methods for symbolic regression of dynamical systems, including those based on different machine learning architectures, to provide a more comprehensive comparison of the proposed method's performance.

To address the lack of analysis on the method's limitations, the authors should provide a detailed discussion of the types of ODEs that the method can and cannot handle effectively. This should include an analysis of the method's performance on ODEs with different characteristics, such as linearity, stiffness, and dimensionality. The authors should also discuss the limitations of the method in terms of the complexity of the symbolic expressions that it can discover. For example, it would be useful to know if the method can handle ODEs with trigonometric, exponential, or logarithmic functions, and how the performance degrades as the complexity of the symbolic expressions increases. Additionally, the authors should discuss the limitations of the method in terms of the length of the solution trajectories required for accurate inference. It would be beneficial to provide guidelines on the minimum length of the trajectory needed for different types of ODEs.

Finally, the authors should provide a more detailed analysis of the computational cost of the proposed method. This should include an analysis of how the computational cost scales with the size of the dataset, the dimensionality of the ODEs, and the complexity of the symbolic expressions. The authors should also discuss the memory requirements of the method and the hardware resources needed to run it efficiently. Furthermore, the authors should provide a sensitivity analysis of the method's performance to hyperparameter choices. This should include an analysis of how the performance of the method varies with different settings of the learning rate, batch size, and the number of layers in the Transformer. The authors should also provide guidelines on how to choose the optimal hyperparameter settings for different types of ODEs.

### Questions

- How does the proposed method compare to other state-of-the-art methods for symbolic regression of dynamical systems?
- What are the limitations of the proposed method in terms of the types of ODEs that it can handle effectively?
- How does the performance of the proposed method vary with the length of the solution trajectory?
- How does the performance of the proposed method vary with the dimensionality of the ODEs?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
