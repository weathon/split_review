### Summary

The paper introduces SimBOL, a simple data-parameter balancing framework for early ventricular activation origin localization in ECG signals. The key innovation is an onset-based data augmentation strategy that expands the training dataset by resampling ECG signals based on the onset of pacing signals. The authors demonstrate that SimBOL achieves a localization error of 9.83 mm, which meets clinical acceptance criteria of < 10 mm, and outperforms existing methods. The framework uses a small-scale 1D convolutional model that balances the relationship between available training data and model complexity, effectively mitigating overfitting. The paper provides a detailed analysis of the impact of data augmentation and model architecture on performance, showing that SimBOL is robust to changes in the amount of training data and is less sensitive to input data structure. The authors also discuss the clinical relevance of their method and its potential for real-world applications.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a clinically relevant problem with practical implications for ECG-based arrhythmia detection and treatment.
- The proposed method is simple, easy to implement, and computationally efficient.
- The authors provide a comprehensive evaluation of the method, including comparisons with existing methods and ablation studies to analyze the impact of different components.
- The paper is well-written and organized, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed discussion of the limitations of the proposed method, such as potential biases in the training data or scenarios where the method may not perform well.
- The paper does not explore the potential for overfitting in more detail, although the authors mention that SimBOL balances the relationship between training data and model complexity. A more thorough analysis of the model's generalization capabilities would be beneficial.
- The paper does not discuss the potential impact of different data preprocessing techniques on the performance of the method.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a limiting factor for real-world applications.

### Suggestions

The authors should include a more thorough discussion of the limitations of their approach. Specifically, they should address potential biases in the training data, such as the distribution of pacing sites and the types of arrhythmias present. It would be beneficial to analyze the performance of the method on different subsets of the data, such as those with varying degrees of noise or different pacing site locations. Furthermore, the authors should explore the sensitivity of the method to variations in the ECG signal, such as changes in sampling rate or signal-to-noise ratio. This analysis would help to identify potential weaknesses of the method and provide guidance for future improvements. The authors should also discuss the potential for overfitting in more detail, perhaps by analyzing the training and validation curves during training. This would provide a more rigorous assessment of the model's generalization capabilities and help to identify potential overfitting issues.

To address the lack of discussion on data preprocessing, the authors should explore the impact of different preprocessing techniques on the performance of their method. This could include techniques such as bandpass filtering, detrending, or normalization. The authors should also discuss the potential for data augmentation techniques to further improve the performance of the method. For example, they could explore techniques such as adding noise to the ECG signals or rotating the ECG signals. This would help to improve the robustness of the method to variations in the ECG signal. The authors should also provide a more detailed analysis of the computational cost of the proposed method, including the training time, inference time, and memory requirements. This analysis should be performed on a range of hardware platforms to provide a more comprehensive understanding of the method's computational cost. This would help to identify potential bottlenecks and provide guidance for future optimizations.

Finally, the authors should consider exploring the use of more advanced deep learning architectures, such as convolutional neural networks or recurrent neural networks, to further improve the performance of their method. They should also explore the use of transfer learning techniques to leverage pre-trained models and improve the performance of their method. This would help to push the performance of the method beyond the current state-of-the-art and provide a more robust solution for early ventricular activation origin localization. The authors should also discuss the potential for using the method in real-world clinical settings, including the challenges and limitations that may arise in such environments. This would help to provide a more realistic assessment of the method's potential impact and guide future research efforts.

### Questions

- How does the proposed method perform on datasets with different characteristics, such as different pacing sites or arrhythmia types?
- How does the proposed method compare to other state-of-the-art methods for early ventricular activation origin localization, such as those based on deep learning?
- What are the potential limitations of the proposed method, and how can they be addressed in future work?
- How does the proposed method perform in the presence of noise or artifacts in the ECG signals?
- What is the computational cost of the proposed method, and how does it compare to other methods?

### Rating

6

### Confidence

4

**********
