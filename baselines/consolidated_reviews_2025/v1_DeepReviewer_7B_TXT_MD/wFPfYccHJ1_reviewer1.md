### Summary

The paper proposes to combine two existing OOD detection methods, namely a learned temperature (introduced in [1]) and the energy score (introduced in [2]). The proposed method, AbeT, is a straightforward combination of the two. The authors show that the combination of the two methods improves OOD detection performance and provide some visualizations and analysis to understand why this combination works.

[1] Hsu et al. "Generalized temperature scaling." International conference on machine learning. PMLR, 2020.
[2] Liu et al. "A simple unified framework for detecting out-of-distribution samples and adversarial attacks." Advances in Neural Information Processing Systems 33 (2020): 19324-19335.

### Soundness

2

### Presentation

3

### Contribution

1

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide some visualizations and analysis to understand why the proposed method works.

### Weaknesses

#### Some Related Works

[1] Generalized temperature scaling
[2] A simple unified framework for detecting out-of-distribution samples and adversarial attacks
[3] On the importance of gradients for detecting distributional shifts in the wild
[4] Openood: Benchmarking generalized out-of-distribution detection
[5] On the importance of gradients for detecting distributional shifts in the wild

#### comment

 - The technical novelty is limited. The proposed method is a straightforward combination of two existing OOD detection methods, namely a learned temperature (introduced in [1]) and the energy score (introduced in [2]). The authors should clearly articulate the novelty of the proposed method and how it differs from the existing methods.

- The authors claim that the proposed method learns to distinguish between misclassified ID examples and OOD examples. However, there is no analysis or experiments to support this claim. The authors should provide more evidence to support this claim.

- The authors should compare the proposed method with other OOD detection methods, such as ODIN [3] and Mahalanobis [3], which are not compared in the paper.

- The authors should compare the proposed method with more recent OOD detection methods, such as OpenOOD [4], which is a more comprehensive benchmark than the one used in the paper.

- The authors should provide a more detailed analysis of the proposed method's performance under different types of distributional shifts. For example, how does the proposed method perform under covariate shift, concept shift, and semantic shift?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of OOD data. For example, how does the proposed method perform under different types of adversarial attacks?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of architectures. For example, how does the proposed method perform under different types of convolutional neural networks and transformers?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of datasets. For example, how does the proposed method perform under different types of image datasets and text datasets?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of experimental settings. For example, how does the proposed method perform under different types of hyperparameter settings and training settings?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of evaluation metrics. For example, how does the proposed method perform under different types of evaluation metrics, such as precision, recall, and F1-score?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of ablation studies. For example, how does the proposed method perform under different types of ablation studies, such as removing the learned temperature or the energy score?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of visualization studies. For example, how does the proposed method perform under different types of visualization studies, such as visualizing the learned temperature and energy score?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of theoretical analysis. For example, how does the proposed method perform under different types of theoretical analysis, such as analyzing the convergence of the learned temperature and energy score?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of limitations. For example, how does the proposed method perform under different types of limitations, such as the computational cost of the proposed method and the scalability of the proposed method?

- The authors should provide a more detailed analysis of the proposed method's performance under different types of future work. For example, how does the proposed method perform under different types of future work, such as exploring the application of the proposed method to other domains and tasks?

### Suggestions

The paper introduces AbeT, a method that combines learned temperature scaling and the energy score for out-of-distribution (OOD) detection. While the simplicity of the approach is a strength, the paper lacks a thorough investigation into the specific mechanisms that lead to improved performance. The authors claim that AbeT learns to distinguish between misclassified in-distribution (ID) examples and OOD examples, but this claim is not supported by any empirical evidence or analysis. To strengthen this claim, the authors should conduct experiments that directly measure the separation between these two classes in the feature space. For example, they could visualize the feature distributions using techniques like t-SNE or UMAP, and analyze the overlap between ID misclassifications and OOD samples. Furthermore, they should investigate the sensitivity of the method to different types of OOD data, such as adversarial examples or data from different domains. This would help to understand the robustness of the method and its limitations.

To address the lack of comparison with other OOD detection methods, the authors should include a more comprehensive benchmark. Specifically, they should compare AbeT with methods like ODIN and Mahalanobis, which are widely used and have established baselines. The comparison should not only focus on overall performance but also on the behavior of the methods under different types of distributional shifts. For example, the authors should evaluate the methods under covariate shift, concept shift, and semantic shift, and analyze how each method performs under these different scenarios. Furthermore, the authors should compare AbeT with more recent OOD detection methods, such as those included in the OpenOOD benchmark. This would provide a more complete picture of the strengths and weaknesses of the proposed method. The authors should also analyze the computational cost of AbeT compared to other methods, as this is an important factor for practical applications.

Finally, the authors should provide a more detailed analysis of the method's performance under different experimental settings. This includes varying hyperparameters, architectures, datasets, and evaluation metrics. For example, the authors should evaluate the method's performance with different network architectures, such as ResNets and Transformers, and with different datasets, such as CIFAR-10, CIFAR-100, and ImageNet. They should also analyze the method's performance under different hyperparameter settings, such as the learning rate, batch size, and temperature scaling parameters. Furthermore, the authors should provide a more detailed analysis of the method's limitations, such as its computational cost and scalability. The authors should also discuss potential future research directions, such as exploring the application of AbeT to other domains and tasks. By addressing these points, the authors can significantly strengthen the paper and make a more compelling case for the proposed method.

### Questions

Please see the weaknesses above.

### Rating

1

### Confidence

4

**********
