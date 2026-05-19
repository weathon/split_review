### Summary

This paper proposes CoPrompt, a novel few-shot learning method for vision-language models. The key idea is to enforce consistency between the trainable and pre-trained models to prevent overfitting. The method incorporates adapters and prompts to further regularize the model and improve generalization. The authors conduct extensive experiments on multiple datasets and tasks, demonstrating state-of-the-art performance in base-to-novel generalization, cross-dataset evaluation, and domain generalization. The paper is well-written and easy to follow.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The authors conduct extensive experiments on multiple datasets and tasks, demonstrating state-of-the-art performance in base-to-novel generalization, cross-dataset evaluation, and domain generalization.
4. The ablation study is comprehensive and provides insights into the contribution of each component of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very novel. The idea of enforcing consistency between trainable and pre-trained models has been explored in previous works, such as CoOp and PromptSRC. The authors should discuss the differences between CoPrompt and these methods more clearly.
2. The paper lacks some important experiments, such as the performance of CoPrompt on ImageNet, and the comparison with other state-of-the-art methods, such as CoOp and PromptSRC.

### Suggestions

The authors should provide a more detailed comparison of CoPrompt with existing methods like CoOp and PromptSRC, specifically highlighting the novel aspects of their approach. While the idea of consistency regularization is not new, the specific implementation and its impact on few-shot learning could be more thoroughly analyzed. For example, a discussion of how the proposed method differs in terms of the consistency loss function, the way adapters are used, and the overall optimization process would be beneficial. It would be helpful to see a breakdown of the computational overhead introduced by CoPrompt compared to these methods, as this could be a deciding factor in practical applications. Furthermore, a more in-depth analysis of the limitations of CoPrompt, such as its sensitivity to hyperparameter choices or its performance on specific types of datasets, would strengthen the paper.

To address the lack of experiments, the authors should include a more comprehensive evaluation of CoPrompt on the ImageNet dataset, which is a standard benchmark for image classification. This would allow for a more direct comparison with other state-of-the-art methods and provide a better understanding of the method's generalization capabilities. The authors should also consider including a comparison with other relevant few-shot learning methods, such as CoOp and PromptSRC, on a wider range of datasets and tasks. This would help to establish the superiority of CoPrompt over existing approaches. In addition, the authors should provide a more detailed analysis of the results, including error analysis and visualizations of the learned representations, to better understand the strengths and weaknesses of the proposed method.

Finally, the authors should provide a more detailed discussion of the hyperparameter tuning process for CoPrompt. While the authors mention that they used a grid search, they should provide more details about the range of values explored for each hyperparameter and the criteria used to select the optimal values. This would help to ensure the reproducibility of the results and provide a better understanding of the sensitivity of the method to different hyperparameter settings. It would also be beneficial to include a discussion of the computational resources required to train and evaluate CoPrompt, as this is an important factor for practical applications. The authors should also consider providing an analysis of the scalability of the method to larger datasets and models.

### Questions

Please see the weakness.

### Rating

6

### Confidence

4

**********
