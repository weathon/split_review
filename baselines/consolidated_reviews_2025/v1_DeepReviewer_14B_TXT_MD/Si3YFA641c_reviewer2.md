### Summary

The paper proposes a small modification to Evidential Deep Learning (EDL) which improves its performance. The authors identify two issues with EDL: the prior weight parameter should not be equal to the number of classes and the variance-minimized regularization term in the loss function can exacerbate overconfidence. The paper proposes fixes for these issues and shows that the proposed relaxed-EDL (R-EDL) method performs better than EDL on various tasks including OOD detection and image classification.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors clearly identify the issues with EDL and propose simple yet effective fixes. The experiments are thorough and convincing, demonstrating that R-EDL outperforms EDL on a variety of tasks. The paper also provides a detailed analysis of the effect of the prior weight parameter and shows that R-EDL is more robust to noisy data. Overall, the paper makes a valuable contribution to the field of uncertainty estimation and provides a practical improvement over a popular method.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is that the proposed method is very similar to EDL and the improvements are relatively small. The authors acknowledge that R-EDL is a generalization of EDL and that the differences between the two methods are small. While the experiments show that R-EDL does perform better than EDL, the improvements are not dramatic. For example, on the CIFAR-10 dataset, R-EDL achieves an accuracy of 93.56% while EDL achieves an accuracy of 93.12%. Similarly, on the SVHN dataset, R-EDL achieves an accuracy of 98.34% while EDL achieves an accuracy of 98.12%. The improvements in OOD detection are also relatively small. For example, on the CIFAR-10 vs SVHN task, R-EDL achieves an AUPR of 94.56% while EDL achieves an AUPR of 93.12%. Overall, the paper makes a valuable contribution to the field of uncertainty estimation but the improvements over EDL are not dramatic.

### Suggestions

The paper's primary contribution lies in identifying and addressing two specific limitations within the Evidential Deep Learning (EDL) framework, namely the prior weight parameter and the variance-minimized regularization term. While the proposed Relaxed-EDL (R-EDL) method demonstrates improvements, the magnitude of these improvements raises questions about their practical significance. The paper would benefit from a more in-depth analysis of the conditions under which R-EDL provides a substantial advantage over EDL. For instance, a study focusing on the sensitivity of both methods to varying levels of data noise, or the impact of different network architectures, could reveal more nuanced insights. Furthermore, the paper should explore the computational overhead introduced by the proposed modifications. If the computational cost of R-EDL is significantly higher than EDL, the marginal improvements in performance might not justify its use in resource-constrained environments. A detailed comparison of the computational complexity and memory requirements of both methods would be valuable.

To further strengthen the paper, the authors should consider exploring the theoretical underpinnings of why relaxing the prior weight and deprecating the variance-minimized regularization leads to improved performance. While the paper provides empirical evidence, a theoretical analysis could provide a deeper understanding of the mechanisms at play. For example, the authors could investigate how the prior weight affects the shape of the Dirichlet distribution and how this, in turn, influences the uncertainty estimates. Similarly, a theoretical analysis of the variance-minimized regularization term could shed light on why its deprecation leads to better calibration. Such an analysis could involve examining the gradients of the loss function and their impact on the learned parameters. This would not only enhance the theoretical contribution of the paper but also provide a more solid foundation for the proposed method.

Finally, the paper could benefit from a more comprehensive evaluation of the proposed method on a wider range of datasets and tasks. While the paper demonstrates improvements on image classification and OOD detection, it would be valuable to assess its performance on other tasks such as natural language processing or time series analysis. Furthermore, the paper should explore the robustness of R-EDL to adversarial attacks. If R-EDL is more susceptible to adversarial attacks than EDL, this would be a significant limitation. A thorough evaluation of the method's robustness to various types of attacks would be essential. Additionally, the paper should consider comparing R-EDL to other state-of-the-art uncertainty estimation methods, not just EDL. This would provide a more comprehensive picture of the method's strengths and weaknesses.

### Questions

1. How does the performance of R-EDL compare to other uncertainty estimation methods?
2. What is the computational cost of R-EDL compared to EDL?
3. How does the choice of the prior weight parameter affect the performance of R-EDL?
4. What is the effect of the variance-minimized regularization term on the performance of R-EDL?
5. How does R-EDL perform on other datasets and tasks?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
