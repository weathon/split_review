### Summary

This paper introduces a new data selection method called OptBatch, which focuses on the learnability of entire batch data rather than individual samples. OptBatch employs stratified sampling to ensure data distribution coverage and maximizes the relative distance between batch samples to enhance diversity. Additionally, it uses Hessian gradient optimization to guide the batch selection strategy. Experimental results demonstrate that OptBatch outperforms previous state-of-the-art methods and exhibits robust generalization performance across various downstream tasks and models.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The authors conducted experiments on various datasets and models, demonstrating the generalization capability of the proposed method.
2. The authors utilized a wide range of evaluation metrics, including GPT-4 evaluation, human evaluation, and reference-based metrics, providing a comprehensive assessment of the method's performance.

### Weaknesses

#### Some Related Works


#### comment

1. The authors employed a loss-probability-based stratified sampling approach. However, the specific formula for calculating loss probability is not clearly defined, and it is not explicitly stated whether this formula is an original contribution or derived from existing literature.
2. The authors proposed the use of Hessian-approximated gradient optimization. However, the specific formula for this optimization is not provided, and it is unclear whether this formula is an original contribution or sourced from existing literature.
3. The authors conducted experiments on various datasets and models, but the specific hyperparameters used for each model and dataset combination are not clearly outlined. Additionally, details regarding the tuning of these hyperparameters are not provided.
4. The authors conducted experiments on three different models but did not provide sufficient details regarding the model training process. It is unclear whether the models were trained from scratch or fine-tuned from pre-trained models. Additionally, the training procedures for each model may vary, but these differences are not clearly specified.
5. The authors conducted experiments on three different models but did not provide sufficient details regarding the model training process. It is unclear whether the models were trained from scratch or fine-tuned from pre-trained models. Additionally, the training procedures for each model may vary, but these differences are not clearly specified.
6. The authors conducted experiments on three different models but did not provide sufficient details regarding the model training process. It is unclear whether the models were trained from scratch or fine-tuned from pre-trained models. Additionally, the training procedures for each model may vary, but these differences are not clearly specified.

### Suggestions

The paper would benefit from a more detailed explanation of the loss-probability calculation used in the stratified sampling. Specifically, the authors should provide the exact mathematical formula used to compute this probability, including any normalization or scaling factors. It is crucial to clarify whether this formula is an original contribution or adapted from existing work, and if the latter, to provide proper citations. Furthermore, the authors should explain the rationale behind choosing this specific formula and how it relates to the overall objective of maximizing batch learnability. A more thorough discussion of the theoretical underpinnings of this approach would significantly enhance the paper's clarity and rigor. For example, it would be beneficial to discuss how the loss probability relates to the gradient norm or other measures of sample difficulty, and how this relationship is leveraged to improve data selection.

Regarding the Hessian-approximated gradient optimization, the authors need to provide the specific formula used for this approximation. It is essential to clarify whether this formula is an original contribution or derived from existing literature, and if the latter, to provide appropriate citations. The authors should also explain the computational advantages of using this approximation over computing the full Hessian, and discuss any potential trade-offs in terms of optimization performance. A detailed explanation of how this approximation is integrated into the batch selection process is also needed. For instance, it would be helpful to describe how the Hessian information is used to guide the selection of diverse and informative samples, and how this approach differs from other gradient-based optimization techniques. The authors should also discuss the limitations of this approximation and under what conditions it might not be effective.

Finally, the paper needs to include a comprehensive description of the hyperparameter tuning process. The authors should provide a table or list of all the hyperparameters used for each model and dataset combination, including learning rates, batch sizes, and any regularization parameters. It is also important to describe the method used for hyperparameter optimization, such as grid search or random search, and to specify the range of values explored for each hyperparameter. The authors should also discuss the criteria used to select the optimal hyperparameter settings, such as validation loss or accuracy. Furthermore, the paper should clearly state whether the models were trained from scratch or fine-tuned from pre-trained models, and provide details on the pre-training process if applicable. The training procedures for each model should also be clearly specified, including the number of training epochs, the optimization algorithm used, and any other relevant details.

### Questions

1. The authors employed a loss-probability-based stratified sampling approach. However, the specific formula for calculating loss probability is not clearly defined, and it is not explicitly stated whether this formula is an original contribution or derived from existing literature.
2. The authors proposed the use of Hessian-approximated gradient optimization. However, the specific formula for this optimization is not provided, and it is unclear whether this formula is an original contribution or sourced from existing literature.
3. The authors conducted experiments on various datasets and models, but the specific hyperparameters used for each model and dataset combination are not clearly outlined. Additionally, details regarding the tuning of these hyperparameters are not provided.
4. The authors conducted experiments on three different models but did not provide sufficient details regarding the model training process. It is unclear whether the models were trained from scratch or fine-tuned from pre-trained models. Additionally, the training procedures for each model may vary, but these differences are not clearly specified.

### Rating

3

### Confidence

4

**********
