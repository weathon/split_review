### Summary

This paper proposes a synthetic data validation strategy for training AI models for medical image segmentation. The authors propose to use synthetic tumors generated from healthy CT volumes to validate the trained models. The authors demonstrate the effectiveness of their method on liver tumor segmentation task.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive review of related works on synthetic data generation for medical image segmentation.
- The authors propose a synthetic data validation strategy for training AI models for medical image segmentation.
- The authors demonstrate the effectiveness of their method on liver tumor segmentation task.

### Weaknesses

#### Some Related Works


#### comment

 - The authors claim that the proposed method can alleviate the overfitting problem. However, the authors do not provide any theoretical analysis or empirical evidence to support this claim. It is unclear why the proposed method can alleviate overfitting. The authors should provide more details on how the synthetic data validation strategy helps to alleviate overfitting.
- The authors only evaluate their method on the liver tumor segmentation task. It is unclear whether the proposed method can be applied to other medical image segmentation tasks. The authors should provide more experiments to demonstrate the generalizability of their method.
- The authors should provide more details on how the synthetic tumors are generated. The authors should provide more details on the parameters used in the synthetic data generation process. The authors should also provide more details on how the synthetic tumors are validated. The authors should provide more details on how the synthetic tumors are used to validate the trained models.

### Suggestions

The paper introduces a synthetic data validation strategy for medical image segmentation, which is a promising approach. However, the lack of theoretical justification for the claim that the method alleviates overfitting is a significant weakness. The authors should provide a more detailed explanation of how the synthetic data validation strategy helps to alleviate overfitting. For instance, they could analyze the distribution of the synthetic data and compare it to the real data to show that the synthetic data is not simply a re-sampling of the real data. Furthermore, the authors should provide empirical evidence to support their claim. This could include experiments that compare the performance of models trained with and without the synthetic data validation strategy, and analyze the training curves to show that the proposed method leads to better generalization. Without this, the claim of alleviating overfitting remains unsubstantiated.

To further strengthen the paper, the authors should conduct more experiments to demonstrate the generalizability of their method. The current evaluation is limited to the liver tumor segmentation task. It is important to evaluate the method on other medical image segmentation tasks, such as brain tumor segmentation or abdominal organ segmentation. This would provide a more comprehensive understanding of the method's applicability and robustness. The authors should also consider evaluating the method on datasets with different characteristics, such as different imaging modalities or different anatomical regions. This would help to identify the limitations of the method and to determine the conditions under which it is most effective. Furthermore, the authors should provide a more detailed analysis of the results, including a discussion of the strengths and weaknesses of the method in different scenarios.

Finally, the authors should provide more details on the synthetic data generation process. The current description is too high-level and lacks the necessary information for reproducibility. The authors should provide more details on the parameters used in the synthetic data generation process, such as the parameters of the generative model and the parameters of the tumor generation process. They should also provide more details on how the synthetic tumors are validated. For example, they should describe the criteria used to evaluate the quality of the synthetic tumors and how these criteria are related to the performance of the trained models. The authors should also provide a more detailed explanation of how the synthetic tumors are used to validate the trained models, including the specific steps involved in the validation process. This would help to ensure that the method is reproducible and that the results are reliable.

### Questions

- The authors claim that the proposed method can alleviate the overfitting problem. However, the authors do not provide any theoretical analysis or empirical evidence to support this claim. It is unclear why the proposed method can alleviate overfitting. The authors should provide more details on how the synthetic data validation strategy helps to alleviate overfitting.
- The authors only evaluate their method on the liver tumor segmentation task. It is unclear whether the proposed method can be applied to other medical image segmentation tasks. The authors should provide more experiments to demonstrate the generalizability of their method.
- The authors should provide more details on how the synthetic tumors are generated. The authors should provide more details on the parameters used in the synthetic data generation process. The authors should also provide more details on how the synthetic tumors are validated. The authors should provide more details on how the synthetic tumors are used to validate the trained models.

### Rating

5

### Confidence

4

**********
