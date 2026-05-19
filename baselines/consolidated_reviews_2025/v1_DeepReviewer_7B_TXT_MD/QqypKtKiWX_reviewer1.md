### Summary

The paper introduces SimBOL, a data augmentation method for early ventricular activation origin (SoA) localization from ECG signals. The method involves resampling ECG signals based on the onset of the pacing signal, which are then used to train a simple 1D convolutional neural network. The authors show that their method outperforms previous methods in terms of localization error, achieving an error of 9.83 mm, which is below the clinical acceptable error of 10 mm. The authors also show that their method is robust to changes in the amount of training data and is less sensitive to input data structure.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The authors provide a clear description of their method and the experimental setup. The authors also provide a good discussion of the limitations of their method and potential future work.

### Weaknesses

#### Some Related Works


#### comment

The paper's novelty is limited, as it primarily focuses on a simple 1D convolutional neural network and data augmentation techniques. The authors do not provide a strong justification for why their specific approach is superior to other possible methods. The paper lacks a thorough comparison with other state-of-the-art methods for SoA localization, making it difficult to assess the true performance of the proposed method. The authors claim that their method is robust to changes in the amount of training data, but they do not provide a detailed analysis of how the performance changes with different amounts of training data. The paper also does not discuss the computational cost of the proposed method, which is an important factor for practical applications.

### Suggestions

The authors should provide a more detailed justification for their choice of a 1D convolutional neural network. While CNNs are commonly used in ECG analysis, the authors should explain why they believe this architecture is particularly well-suited for the task of SoA localization, especially given the simplicity of the approach. A comparison with other potential architectures, such as recurrent neural networks or transformer-based models, would strengthen the paper. Furthermore, the authors should provide a more in-depth analysis of the impact of different data augmentation techniques on the performance of the proposed method. While the authors mention that their method is robust to changes in the amount of training data, they do not provide a detailed analysis of how the performance changes with different amounts of training data. A more thorough analysis of the relationship between the amount of training data and the performance of the method would be beneficial. This analysis should include a discussion of the trade-offs between training data size and computational cost.

The authors should also provide a more comprehensive comparison with other state-of-the-art methods for SoA localization. While the authors compare their method to a few existing methods, they do not provide a detailed analysis of the strengths and weaknesses of each method. A more thorough comparison would help to contextualize the performance of the proposed method and highlight its unique contributions. This comparison should include a discussion of the limitations of the existing methods and how the proposed method addresses these limitations. The authors should also discuss the computational cost of their method, including the training time and inference time. This information is important for practical applications, as it allows other researchers to assess the feasibility of using the proposed method in real-world settings. The authors should also discuss the limitations of their method, such as the potential for overfitting and the sensitivity to noise in the ECG signals.

Finally, the authors should provide a more detailed discussion of the clinical relevance of their method. While the authors mention that their method is clinically relevant, they do not provide a detailed analysis of how the method could be used in practice. A more detailed discussion of the clinical implications of the proposed method would help to highlight its importance and potential impact. This discussion should include a description of how the method could be integrated into existing clinical workflows and the potential benefits that it could provide for patients with cardiac arrhythmias.

### Questions

How does the proposed method compare to other state-of-the-art methods for SoA localization? What are the advantages and disadvantages of the proposed method compared to these methods?
What is the computational cost of the proposed method? How does the training time and inference time compare to other methods?
How does the performance of the proposed method vary with different amounts of training data? Is there a point at which the performance plateaus?
What are the limitations of the proposed method? How does the method perform in the presence of noise in the ECG signals?
How could the proposed method be used in practice? What are the potential clinical benefits of the method?

### Rating

3

### Confidence

4

**********
