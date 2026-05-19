### Summary

This paper proposes a new PETL method for ViT. The proposed method is based on the idea of VPT, but with several improvements. First, it introduces a meta register to capture global features. Second, it introduces a side branch to fuse the intermediate features. Third, it introduces a transformation bridge to fuse the global features and the fused features. The proposed method is evaluated on VTAB-1K, FGVC, and some object detection and segmentation datasets. The proposed method outperforms other PETL methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is evaluated on a wide range of datasets. The proposed method outperforms other PETL methods on most datasets.
2. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is very similar to VPT. The main difference is that the proposed method introduces a meta register to capture global features and a side branch to fuse the intermediate features. The transformation bridge is similar to VPT. The overall idea is very similar to VPT. The authors should discuss the difference between the proposed method and VPT in detail. Specifically, the paper lacks a rigorous analysis of how the meta-register's global feature representation differs from the global feature representation used in VPT, and how this difference impacts performance. The paper should also provide a more detailed explanation of the side branch's role in feature fusion, including a comparison of its design choices with those in VPT, and a discussion of the specific advantages of this design.
2. The proposed method is evaluated on ViT-B and ViT-L. The authors should evaluate the proposed method on ViT-H. The absence of results on the largest ViT model makes it difficult to assess the scalability of the proposed method. It is important to determine if the performance gains observed on smaller models translate to larger models, or if the proposed method is limited by the model's capacity.
3. The proposed method is evaluated on MAE pre-trained models. The authors should evaluate the proposed method on supervised pre-trained models. The paper should investigate whether the proposed method is effective when applied to models trained with different pre-training objectives. This is important because the pre-training objective can significantly impact the learned representations and the effectiveness of parameter-efficient transfer learning methods.

### Suggestions

The paper should provide a more in-depth analysis of the differences between the proposed method and VPT, focusing on the specific mechanisms that lead to performance improvements. For example, the authors could analyze the feature representations learned by the meta-register and compare them to the global features used in VPT, perhaps using visualization techniques or quantitative metrics to demonstrate the differences. Furthermore, the paper should include a more detailed explanation of the side branch's design, including the specific fusion operations used and how they contribute to the overall performance. A comparison with the fusion mechanisms in VPT would be beneficial, highlighting the advantages of the proposed approach. This analysis should go beyond a simple statement of difference and provide a clear understanding of the technical contributions of the proposed method.

To address the lack of evaluation on larger models, the authors should include results on ViT-H, even if it requires additional computational resources. This would provide a more comprehensive evaluation of the method's scalability and robustness. The paper should also discuss the potential limitations of the proposed method when applied to larger models, such as increased computational cost or potential performance degradation. Furthermore, the authors should investigate the impact of model size on the effectiveness of the proposed method, potentially by comparing the performance of the proposed method on models of different sizes. This analysis would provide valuable insights into the method's scalability and its potential for use in real-world applications.

Finally, the paper should include experiments on supervised pre-trained models to assess the generalizability of the proposed method. This would involve training models using supervised learning and then applying the proposed method for transfer learning. The paper should compare the performance of the proposed method on supervised pre-trained models with its performance on MAE pre-trained models. This comparison would help to determine whether the proposed method is effective across different pre-training objectives. The paper should also discuss the potential reasons for any differences in performance and how these differences might be addressed in future work. This would provide a more complete picture of the proposed method's capabilities and limitations.

### Questions

See weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
