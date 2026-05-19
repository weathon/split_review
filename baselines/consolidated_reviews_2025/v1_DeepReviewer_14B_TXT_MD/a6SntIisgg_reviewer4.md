### Summary

This paper proposes a Local-Global Representation Alignment framework (LOGRA) for unsupervised domain adaptation (UDA) of time series data. The framework uses a two-branch encoder to extract both local and global features, and a fusion module to integrate these features. The authors employ various strategies to achieve effective alignment, including invariant feature learning, triplet loss, and adversarial training. The paper demonstrates the superiority of LOGRA over existing methods on four time-series datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a clear motivation for their work and explain the limitations of existing methods.
3. The proposed LOGRA framework is novel and addresses the limitations of existing methods by extracting and aligning both local and global features.
4. The authors conduct extensive experiments on four time-series datasets and show that LOGRA outperforms existing methods.
5. The paper includes ablation studies to demonstrate the effectiveness of each component of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to compare the computational cost of LOGRA with existing methods.
2. The paper does not discuss the potential limitations of the proposed method. It would be helpful to discuss the scenarios where LOGRA might not perform well and the potential reasons for these limitations.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the LOGRA framework. Specifically, the authors should provide a breakdown of the time and space complexity for each component of the model, including the local and global feature extraction modules, the fusion module, and the alignment strategies. This analysis should not only consider the theoretical complexity but also include empirical measurements of training and inference time on the datasets used in the experiments. Furthermore, a comparison of the computational cost with existing methods, such as VRADA, CoDATS, AdvSKM, CLUDA, and RAINCOAT, should be provided, detailing the differences in FLOPs, parameter counts, and memory usage. This would allow for a more comprehensive understanding of the practical trade-offs associated with using LOGRA.

In addition to computational complexity, the paper should also discuss the limitations of the proposed method in more detail. The authors should explore scenarios where LOGRA might fail to achieve effective domain adaptation. For example, it would be beneficial to analyze the performance of LOGRA when the source and target domains have significantly different temporal dynamics or when the time series data is highly noisy. The authors should also consider the impact of the choice of hyperparameters on the performance of the model and discuss the sensitivity of the method to these parameters. Furthermore, the paper should discuss the potential limitations of the local and global feature extraction modules, such as their ability to capture complex temporal dependencies or their robustness to adversarial attacks. A more detailed discussion of these limitations would provide a more balanced view of the proposed method and guide future research directions.

Finally, the paper should include a more detailed discussion of the experimental setup, including the specific hyperparameter settings used for each dataset and the rationale behind these choices. The authors should also provide more details on the data preprocessing steps, such as normalization or filtering, that were applied to the time series data. This would allow for a more reproducible and transparent evaluation of the proposed method. Furthermore, the authors should consider including additional experiments on more diverse datasets to further validate the generalizability of LOGRA. This would help to demonstrate the robustness of the method to different types of time series data and domain shifts.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
