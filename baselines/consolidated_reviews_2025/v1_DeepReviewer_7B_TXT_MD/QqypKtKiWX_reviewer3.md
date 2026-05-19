### Summary

This paper proposes a data augmentation method for ECG-based early ventricular activation origin (SoA) localization. The proposed method is called Onset-based data augmentation. The proposed method is based on the physical characteristics of ECG signals and is able to increase the amount of training data for deep learning models. The proposed method is simple and easy to implement. The proposed method is evaluated on a pacing-site dataset and achieves a localization error of 9.83 mm, which is below the clinical acceptable error of 10 mm.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement.
2. The proposed method is able to increase the amount of training data for deep learning models.
3. The proposed method achieves a localization error of 9.83 mm, which is below the clinical acceptable error of 10 mm.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the physical characteristics of ECG signals. However, the proposed method is not compared with other data augmentation methods that are based on the physical characteristics of ECG signals.
2. The proposed method is only evaluated on a pacing-site dataset. The proposed method is not evaluated on other datasets.
3. The proposed method is not compared with other data augmentation methods that are based on the physical characteristics of ECG signals.

### Suggestions

The paper introduces an onset-based data augmentation method for ECG-based early ventricular activation origin localization. While the method is simple and achieves a clinically relevant localization error, the evaluation is limited. The authors should compare their method against other data augmentation techniques that leverage the physical characteristics of ECG signals. For example, methods that use temporal warping, signal resampling, or other transformations based on the morphology of the ECG waveform could provide a more comprehensive evaluation. This comparison would help to quantify the specific benefits of the proposed onset-based approach and determine if it offers a significant advantage over existing methods. Furthermore, the authors should explore the impact of different augmentation parameters on the performance of the proposed method. This would provide a more thorough understanding of the method's sensitivity to parameter changes and help to optimize its performance.

Additionally, the evaluation should be expanded to include multiple datasets. The current evaluation is limited to a single pacing-site dataset, which may not be representative of all clinical scenarios. Evaluating the method on other datasets, such as those with different patient populations or recording conditions, would provide a more robust assessment of its generalizability. This would also help to identify potential limitations of the method and areas for improvement. For example, the method's performance on datasets with different types of arrhythmias or different recording modalities should be investigated. Furthermore, the authors should consider evaluating the method's performance on datasets with varying levels of noise or artifacts, as these factors can significantly impact the accuracy of ECG-based localization methods. This would provide a more comprehensive understanding of the method's robustness and its applicability in real-world clinical settings.

Finally, the paper lacks a detailed analysis of the computational cost of the proposed method. While the method is described as simple and easy to implement, it is important to quantify its computational requirements, especially when compared to other data augmentation techniques. This analysis should include the time and memory requirements for both training and inference. This information is crucial for assessing the practicality of the method in resource-constrained environments. The authors should also discuss the potential for optimizing the method to reduce its computational cost. This could involve techniques such as model pruning, quantization, or other methods for reducing the complexity of the deep learning model. A thorough analysis of the computational cost would provide a more complete picture of the method's overall performance and its suitability for clinical applications.

### Questions

1. How does the proposed method compare with other data augmentation methods that are based on the physical characteristics of ECG signals?
2. How does the proposed method perform on other datasets?
3. How does the proposed method compare with other data augmentation methods that are based on the physical characteristics of ECG signals?

### Rating

5

### Confidence

4

**********
