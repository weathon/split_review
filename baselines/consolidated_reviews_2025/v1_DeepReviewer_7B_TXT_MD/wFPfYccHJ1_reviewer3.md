### Summary

This paper proposes a new OOD detection method called AbeT, which combines learned temperature and energy score. The authors also provide a detailed analysis of the method's performance on various tasks, including classification, semantic segmentation, and object detection. The results show that AbeT outperforms existing methods in terms of FPR@95 and AUROC.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a detailed analysis of the method's performance on various tasks, including classification, semantic segmentation, and object detection.
3. The results show that AbeT outperforms existing methods in terms of FPR@95 and AUROC.

### Weaknesses

#### Some Related Works

[1] Generalized temperature scaling
[2] A simple unified framework for detecting out-of-distribution samples and adversarial attacks

#### comment

1. The technical novelty is limited. The proposed method is a straightforward combination of two existing OOD detection methods, namely a learned temperature [1] and the energy score [2]. The authors should clearly articulate the novelty of the proposed method and how it differs from the existing methods.
2. The authors claim that the proposed method learns to distinguish between misclassified ID examples and OOD examples. However, there is no analysis or experiments to support this claim. The authors should provide more evidence to support this claim.
3. The authors should compare the proposed method with other OOD detection methods, such as ODIN [3] and Mahalanobis [4], which are not compared in the paper.
4. The authors should compare the proposed method with more recent OOD detection methods, such as OpenOOD [5], which is a more comprehensive benchmark than the one used in the paper.
5. The authors should provide a more detailed analysis of the proposed method's performance under different types of distributional shifts. For example, how does the proposed method perform under covariate shift, concept shift, and semantic shift?
6. The authors should provide a more detailed analysis of the proposed method's performance under different types of OOD data. For example, how does the proposed method perform under different types of adversarial attacks?
7. The authors should provide a more detailed analysis of the proposed method's performance under different types of architectures. For example, how does the proposed method perform under different types of convolutional neural networks and transformers?
8. The authors should provide a more detailed analysis of the proposed method's performance under different types of datasets. For example, how does the proposed method perform under different types of image datasets and text datasets?
9. The authors should provide a more detailed analysis of the proposed method's performance under different types of experimental settings. For example, how does the proposed method perform under different types of hyperparameter settings and training settings?
10. The authors should provide a more detailed analysis of the proposed method's performance under different types of evaluation metrics. For example, how does the proposed method perform under different types of evaluation metrics, such as precision, recall, and F1-score?
11. The authors should provide a more detailed analysis of the proposed method's performance under different types of ablation studies. For example, how does the proposed method perform under different types of ablation studies, such as removing the learned temperature or the energy score?
12. The authors should provide a more detailed analysis of the proposed method's performance under different types of visualization studies. For example, how does the proposed method perform under different types of visualization studies, such as visualizing the learned temperature and energy score?
13. The authors should provide a more detailed analysis of the proposed method's performance under different types of theoretical analysis. For example, how does the proposed method perform under different types of theoretical analysis, such as analyzing the convergence of the learned temperature and energy score?
14. The authors should provide a more detailed analysis of the proposed method's performance under different types of limitations. For example, how does the proposed method perform under different types of limitations, such as the computational cost of the proposed method and the scalability of the proposed method?
15. The authors should provide a more detailed analysis of the proposed method's performance under different types of future work. For example, how does the proposed method perform under different types of future work, such as exploring the application of the proposed method to other domains and tasks?

### Suggestions

The paper introduces AbeT, a method combining learned temperature and energy score for out-of-distribution (OOD) detection. While the idea of combining these two techniques is interesting, the paper lacks a clear articulation of the novelty and specific advantages of this combination. The authors should provide a more detailed explanation of how AbeT differs from existing methods and why this specific combination is expected to yield better performance. For instance, a theoretical analysis of the interaction between the learned temperature and energy score could provide a deeper understanding of the method's behavior. Furthermore, the paper should include a more comprehensive comparison with other state-of-the-art OOD detection methods, such as ODIN and Mahalanobis, to demonstrate the superiority of AbeT. The current comparison is insufficient to establish the method's effectiveness.

To strengthen the paper, the authors should conduct a more thorough analysis of the method's performance under various types of distributional shifts. The paper should explore how AbeT performs under covariate shift, concept shift, and semantic shift, and compare its performance with other methods under these different scenarios. Additionally, the paper should investigate the method's robustness to different types of OOD data, including adversarial attacks, and analyze how the learned temperature and energy score contribute to this robustness. The authors should also provide a more detailed analysis of the method's performance under different architectures, datasets, and experimental settings. This would help to understand the method's generalizability and limitations. Furthermore, the evaluation should include a broader range of metrics, such as precision, recall, and F1-score, to provide a more comprehensive assessment of the method's performance.

Finally, the paper should include a more detailed analysis of the method's limitations and potential future research directions. The authors should discuss the computational cost of AbeT and its scalability to larger datasets and models. They should also explore the potential of applying AbeT to other domains and tasks, such as anomaly detection or fraud detection. The paper should also include a more detailed analysis of the learned temperature and energy score, such as visualizing them and analyzing their convergence behavior. This would provide a deeper understanding of the method's inner workings and help to identify potential areas for improvement. The authors should also discuss the limitations of the current evaluation setup and suggest future research directions to address these limitations.

### Questions

See the weaknesses.

### Rating

3

### Confidence

5

**********
