### Summary

This paper proposes to use additional publicly available data (proxy data) in order to improve the performance of zero-shot quantization (ZSQ) of deep neural networks. The proposed method is inspired by prior work in zero-shot knowledge distillation and model stealing, but attempts to address the specific challenges in the ZSQ setting. The paper also proposes a proxy data selection method based on batch-normalization statistics (BNS), to select the optimal proxy data, among a set of candidates, for a given task. The proposed method is tested on a number of computer vision datasets (CIFAR10, CIFAR100, ImageNet-1K) and shows improvements in the accuracy compared to existing ZSQ methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

+ The paper is well-written, organized and easy to follow.
+ The idea of using proxy data to improve the performance of ZSQ is interesting and intuitive.
+ The proposed BNS-based proxy data selection method is simple and efficient.
+ The paper provides a comprehensive set of experiments and ablation studies to evaluate the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is not novel, since using proxy data in zero-shot quantization has been proposed before, for example in the paper "Qimera: Exploiting the Multi-Modality of Deep Representations for Data-Free Model Compression", Choi et al., CVPR 2021. While the paper acknowledges Qimera, it does not provide a detailed comparison of the proposed method with Qimera, highlighting the differences and advantages of the proposed method. The core idea of leveraging external data to aid in zero-shot quantization is not new, and the paper needs to more clearly articulate its unique contribution beyond simply using a different external dataset.
- The proposed method is only tested on convolutional neural networks (CNNs), and it is not clear how it would perform on other architectures, such as transformers. This limits the generalizability of the findings. The paper should acknowledge that the BNS-based selection method is specific to CNNs due to the reliance on batch normalization layers, and that its applicability to other architectures is not straightforward.
- The paper does not provide a theoretical analysis of why the proposed method works, or what are the properties of a good proxy data set. The paper lacks a deeper understanding of the underlying mechanisms that make the proposed method effective. It would be beneficial to explore the relationship between the proxy data and the original data distribution, and how this relationship impacts the quantization process.
- Some of the tables and figures are not very clear, or have low resolution. For example, Table 3 and Figure 4. The low quality of some figures and tables makes it difficult to fully grasp the experimental results and analysis.

### Suggestions

The paper should provide a more thorough comparison with existing methods that utilize proxy data for zero-shot quantization, such as Qimera. It is not sufficient to simply acknowledge these methods; a detailed analysis of the differences in approach, methodology, and performance is necessary to establish the novelty and contribution of the proposed method. Specifically, the paper should discuss how the proposed method addresses the limitations of existing methods and what specific advantages it offers. This comparison should not only focus on the performance metrics but also on the computational cost, the complexity of the approach, and the sensitivity to hyperparameter settings. A more detailed ablation study could also be beneficial to understand the impact of different components of the proposed method.

To enhance the generalizability of the proposed method, the paper should explore its performance on architectures beyond CNNs, such as transformers. Given that the BNS-based selection method is specific to CNNs, the paper should investigate alternative proxy data selection methods that are applicable to other architectures. This could involve exploring methods based on attention mechanisms or other architecture-specific features. Furthermore, the paper should provide a more in-depth analysis of the properties of a good proxy dataset. This analysis should go beyond the empirical observations and provide a theoretical understanding of the relationship between the proxy data and the original data distribution. For example, the paper could explore the concept of domain similarity or transferability to justify the selection of a particular proxy dataset. This theoretical analysis would provide a more solid foundation for the proposed method and guide the selection of proxy data in different scenarios.

Finally, the paper should improve the quality of the figures and tables. The low resolution of some figures and tables makes it difficult to interpret the results and analysis. The paper should ensure that all figures and tables are clear, high-resolution, and easy to understand. This includes using appropriate font sizes, labels, and legends. Additionally, the paper should provide more detailed captions for each figure and table, explaining the content and the key findings. This would make the paper more accessible and allow readers to fully grasp the experimental results and analysis.

### Questions

- How does the proposed method compare to other methods that use proxy data for ZSQ, such as Qimera? What are the main differences and advantages of the proposed method?
- How does the BNS-based proxy data selection method work for other architectures, such as transformers? Is there a similar method that can be used for non-CNN networks?
- What are the theoretical guarantees or bounds for the proposed method? How does the choice of proxy data affect the convergence and stability of the ZSQ process?
- Some of the tables and figures are not very clear, or have low resolution. For example, Table 3 and Figure 4. Can you improve the quality of these figures and tables?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
