### Summary

This paper proposes a method to test whether two models are trained independently or not. The method consists of measuring some similarity metric (e.g. cosine similarity) on the weights of the models and comparing it to a distribution of the similarity metric obtained by training two models independently. The method is also extended to the case where one wants to keep the testing of independence robust to retraining some layers of the models by learning a mapping between the hidden activations of these layers. Experiments are conducted to show the effectiveness of the proposed method.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

The strengths of the paper are as follows:

* The proposed method can be applied to test the independence of any kind of models, including vision models and language models.
* The proposed method can be applied to test the independence of two models trained on different data distributions.

### Weaknesses

#### Some Related Works


#### comment

The weaknesses of the paper are as follows:

* The proposed method can only be applied to test the independence of models with the same architecture. This is a significant limitation, as in practice, models are often fine-tuned or adapted from pre-trained models with different architectures. The method's reliance on direct weight comparison makes it unsuitable for comparing models with different layer structures, activation functions, or even numbers of parameters. This severely limits the method's applicability in real-world scenarios where model architectures are not always known or standardized.
* The proposed method cannot be applied to test the independence of a model with its fine-tuned version. This is a critical flaw, as fine-tuning is a very common practice in machine learning. The method's inability to handle fine-tuning, where the model weights are slightly adjusted from a pre-trained state, makes it practically useless for many common use cases. The core issue is that fine-tuning alters the weights of the base model, and the proposed method is not robust to these changes, which are often subtle but can significantly impact model behavior.
* The proposed method cannot be applied when one model is a pruned version of the other model. Pruning is another common technique for model optimization, and the inability to handle pruned models further restricts the method's practical use. Pruning involves removing specific connections or neurons, which changes the weight distribution and structure. The proposed method, relying on direct weight comparison, is not designed to handle such structural changes, making it unsuitable for scenarios where model pruning is involved.

In summary, the proposed method can only be applied to test the independence of two models with the same architecture trained on different datasets. All other use cases, which are very common in practice, are not covered by this method. Therefore, the practical utility of the proposed method is very limited.

### Suggestions

The authors should address the limitations of their method by exploring ways to extend it to handle models with different architectures. This could involve investigating techniques such as feature alignment or representation learning to map the internal representations of different models into a common space where similarity can be measured. For example, one could explore using adversarial training to learn a mapping between the hidden layers of two different architectures, allowing for a more meaningful comparison of their internal states. This would significantly broaden the applicability of the method.

Furthermore, the authors need to tackle the issue of fine-tuning. The current method is not robust to the subtle changes in weights that occur during fine-tuning. To address this, the authors could explore methods that focus on comparing the functional behavior of the models rather than just their weights. For instance, one could compare the models' responses to a set of input stimuli or analyze the similarity of their gradients during training. This would provide a more robust measure of independence that is less sensitive to minor weight adjustments. Another approach could be to use a metric that quantifies the difference in the learned representations of the models, such as the centered kernel alignment (CKA) score, which has been shown to be effective in comparing representations across different models.

Finally, the authors should also consider the case of pruned models. The method should be extended to handle scenarios where models have different numbers of parameters due to pruning. One possible approach is to use a technique called 'weight masking' to simulate the effect of pruning on the original model, allowing for a more direct comparison. Another approach could be to focus on comparing the functional behavior of the models, as suggested above. This would involve analyzing the similarity of the models' outputs or gradients, which is less sensitive to the specific structure of the model. By addressing these limitations, the authors can significantly improve the practical utility of their method.

### Questions

* Please address the limitations mentioned in the weaknesses section.

### Rating

3

### Confidence

3

**********
