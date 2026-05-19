### Summary

This paper proposes a new model merging method called AdaMerging, which adaptively learns the coefficients for model merging without requiring the original training data. Specifically, AdaMerging optimizes the merging coefficients by minimizing the entropy of the prediction loss on unlabeled test samples from the multi-task setup. Extensive experiments show that AdaMerging outperforms existing task vector-based merging methods in multi-task learning, generalization, and robustness.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The motivation of this paper is clear and reasonable.
3. The experiments are extensive, including the comparison with the state-of-the-art methods, the ablation study, and the analysis of the learned coefficients.

### Weaknesses

#### Some Related Works

[1] Task arithmetic: A simple approach to multi-task learning
[2] TIES-Merging: Mitigating Representation Conflicts in Multi-Task Model Merging
[3] Model merging in the dark: On the importance of fine-grained task attribution
[4] Model merging in the dark: On the importance of fine-grained task attribution

#### comment

1. The novelty of this paper is limited. The proposed AdaMerging is essentially a fine-tuning method, which adjusts the merging coefficients of the task vectors. The core idea of using task vectors for multi-task learning is not new, and the proposed method does not introduce a fundamentally novel approach to multi-task learning. The method essentially performs a weighted average of task vectors, where the weights are learned through entropy minimization. This is a relatively straightforward application of existing techniques.
2. The motivation of this paper is not clear. The authors claim that the proposed method can adaptively learn the merging coefficients without requiring the original training data. However, the method still requires the test samples of the multi-task setup, which are essentially the original training data of each task. The method does not truly operate without original training data; it uses a subset of the training data for evaluation. The claim of not requiring original training data is misleading.
3. The experiments are insufficient. The authors should compare AdaMerging with more SOTA methods, such as TIES-Merging [2] and TIES++-Merging [3]. The current experiments only compare against a limited set of baselines, and it is unclear how AdaMerging would perform against more recent and advanced merging techniques. The lack of comparison with these methods makes it difficult to assess the true contribution of the proposed method.
4. The authors claim that AdaMerging can handle unseen tasks. However, the experiments are not sufficient to support this claim. The authors should conduct experiments on more unseen tasks, such as the Taskonomy dataset [4]. The current experiments only show results on a limited number of unseen tasks, and it is unclear if the method would generalize well to a broader range of unseen tasks.

### Suggestions

The paper's core idea of adaptively learning merging coefficients for task vectors, while interesting, needs further justification to establish its novelty. The authors should more clearly articulate the specific limitations of existing task vector-based merging methods that AdaMerging addresses. For instance, do existing methods struggle with a large number of tasks, or are they sensitive to specific task characteristics? A more detailed analysis of these limitations would strengthen the motivation for the proposed approach. Furthermore, the authors should provide a more in-depth discussion of the theoretical underpinnings of their method. Why does minimizing the entropy of the prediction loss lead to better merging results? A theoretical analysis would provide a more solid foundation for the proposed method and help to understand its behavior in different scenarios. The authors should also consider exploring alternative loss functions or optimization strategies to further improve the performance of AdaMerging.

The claim that AdaMerging operates without original training data is misleading and needs to be revised. The method requires a subset of the original training data for evaluation, which is not truly 'unseen'. The authors should clarify this point and acknowledge that the method still relies on some information from the original training data. A more accurate description of the method's data requirements would be beneficial. Additionally, the authors should explore the sensitivity of AdaMerging to the size and composition of the test samples used for entropy minimization. How does the performance of the method vary with different test sets? This analysis would provide insights into the robustness of the method and its applicability in different scenarios. The authors should also consider comparing AdaMerging with other methods that also use a subset of the training data for model selection or hyperparameter tuning.

Finally, the experimental evaluation needs to be significantly expanded to include more state-of-the-art merging methods and a broader range of unseen tasks. The authors should compare AdaMerging with methods like TIES-Merging [2] and TIES++-Merging [3], which are relevant baselines for this work. The experiments should also include a more diverse set of tasks, including those from the Taskonomy dataset [4], to demonstrate the generalizability of the method. Furthermore, the authors should provide a more detailed analysis of the performance of AdaMerging under different conditions, such as varying the number of tasks, the complexity of the tasks, and the size of the model. This would provide a more comprehensive understanding of the method's strengths and limitations. The authors should also consider including ablation studies to analyze the impact of different components of the method, such as the entropy minimization objective and the use of layer-wise coefficients.

### Questions

1. What is the difference between AdaMerging and AdaMerging++? The authors should clarify the difference between the two methods.
2. What is the performance of AdaMerging on the Taskonomy dataset? The authors should conduct experiments on the Taskonomy dataset to validate the generalization ability of AdaMerging.

### Rating

5

### Confidence

5

**********
