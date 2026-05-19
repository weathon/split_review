### Summary

This paper introduces CoPrompt, a novel fine-tuning method for vision-language models designed to improve generalization in few-shot learning scenarios. CoPrompt addresses the overfitting problem often encountered in few-shot learning by enforcing a consistency constraint between the trainable and pre-trained models, preventing overfitting on downstream tasks. Additionally, CoPrompt incorporates adapters and prompts to enhance model performance, achieving state-of-the-art results across various evaluation suites, including base-to-novel generalization, cross-dataset evaluation, and domain generalization. The method combines prompt learning with adapter tuning, integrating both into a single framework to improve generalization while maintaining zero-shot capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is well-motivated and clearly explained. The authors provide a thorough description of the consistency constraint, adapters, and prompts, making it easy to understand the motivation and implementation of CoPrompt.

2. The experiments are comprehensive and well-designed. The authors evaluate CoPrompt on multiple datasets and tasks, demonstrating its effectiveness in few-shot learning, base-to-novel generalization, cross-dataset evaluation, and domain generalization. The ablation studies further validate the importance of each component in the proposed method.

3. The paper is well-written and easy to follow. The authors provide clear explanations of the related work, the proposed method, and the experimental results. The figures and tables are well-organized and informative.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper is well-written, the authors could consider adding more visualizations to enhance understanding. For example, visualizing the feature space before and after fine-tuning could provide insights into how CoPrompt improves generalization. Additionally, visualizing the attention maps of the adapters could help understand how they contribute to the model's performance.

2. The paper could benefit from a more detailed discussion of the computational cost of CoPrompt compared to other methods. While the authors mention that CoPrompt has a higher computational cost than MaPLe, a more thorough analysis of the time and memory requirements would be valuable. Specifically, a breakdown of the computational cost of each component (prompt learning, adapter tuning, and consistency constraint) would be helpful.

3. The authors could explore the limitations of CoPrompt in more detail. For example, how does CoPrompt perform on datasets with different characteristics (e.g., different image resolutions, different object categories)? Are there any specific scenarios where CoPrompt might not perform well? Addressing these questions would provide a more complete picture of the method's applicability and robustness.

### Suggestions

The authors should consider adding visualizations of the feature space before and after applying the consistency constraint. This could be achieved by projecting the high-dimensional feature vectors into a 2D or 3D space using techniques like t-SNE or PCA. Comparing the feature distributions of the pre-trained model and the CoPrompt-tuned model would provide a clear picture of how the consistency constraint helps to regularize the feature space and prevent overfitting. Furthermore, visualizing the attention maps of the adapters could offer insights into which parts of the input image the adapters are focusing on. This could be done by visualizing the attention weights for a few representative examples and analyzing the patterns. Such visualizations would not only enhance the understanding of the method but also provide a more intuitive explanation of its effectiveness.

To address the computational cost concerns, the authors should provide a detailed breakdown of the time and memory requirements for each component of CoPrompt. This should include the time taken for prompt learning, adapter tuning, and enforcing the consistency constraint. The analysis should also consider the impact of different hyperparameters, such as the number of adapters and the learning rate, on the computational cost. Furthermore, it would be beneficial to compare the computational cost of CoPrompt with other state-of-the-art few-shot learning methods, not just MaPLe. This would provide a more comprehensive understanding of the trade-offs between performance and computational efficiency. The authors could also explore techniques to reduce the computational cost, such as using more efficient optimization algorithms or reducing the number of parameters in the adapters.

Finally, the authors should investigate the performance of CoPrompt on datasets with varying characteristics. This could include datasets with different image resolutions, different object categories, and different levels of noise. Analyzing the performance of CoPrompt on these datasets would help to identify its strengths and weaknesses and provide a more complete picture of its applicability. For example, it would be interesting to see how CoPrompt performs on datasets with fine-grained object categories or datasets with limited image quality. The authors should also explore the sensitivity of CoPrompt to different hyperparameters and provide guidelines for selecting appropriate values for different datasets. This would make the method more practical and easier to use for a wider range of applications.

### Questions

1. How does the performance of CoPrompt vary with different choices of the consistency constraint loss function? For example, have the authors experimented with other loss functions besides cosine distance?

2. How does the number of adapters affect the performance of CoPrompt? Have the authors explored different numbers of adapters and analyzed the trade-off between performance and computational cost?

3. How does CoPrompt perform on datasets with different characteristics (e.g., different image resolutions, different object categories)? Are there any specific scenarios where CoPrompt might not perform well?

### Rating

6

### Confidence

4

**********
