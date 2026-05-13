# NegMerge: Consensual Weight Negation for Strong Machine Unlearning

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Machine unlearning aims to selectively remove specific knowledge from a model. Current methods, such as task arithmetic, rely on fine-tuning models on the forget set, generating a task vector, and subtracting it from the original model. However, we argue the effectiveness of this approach is highly sensitive to hyperparameter selection, necessitating careful validation to identify the best model among many fine-tuned candidates. In this paper, we propose a novel method that leverages all given fine-tuned models rather than selecting a single one. By constructing task vectors from models trained with varied hyperparameters and merging only the components of the task vectors with consistent signs, we perform unlearning by negating the merged task vector from the original model. Given that existing methods also utilize multiple fine-tuned models, our approach delivers more effective unlearning without incurring additional computational costs. We demonstrate the effectiveness of our method on both vision-language models and standard image classification models, showing improved unlearning performance with minimal degradation on the retain set, outperforming state-of-the-art techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the machine unlearning problem, which aims to selectively remove knowledge from a pre-trained model without retraining from scratch. Instead of subtracting a single task vector from a pre-trained model, this paper proposed to use multiple task vectors with different hyperparameters. Multiple task vectors are merged by averaging elements with the same signs, while the remaining elements with different signs are replaced with zeros. Experimental results showed the effectiveness of merging multiple models during the unlearning process. More importantly, the elements with the same signs have more impact than the elements with conflict signs.

### Strengths
* This paper tackles an important and relatively new topic of machine unlearning. It would be very impactful to remove specific data slices from a pre-trained model, without retraining from scratch due to the training cost. 
* This paper proposed an intuitively simple idea to merge multiple fine-tuned task vectors into a single one. Empirical results showed the effectiveness. 
* Not only the classification results are reported, but also the Membership Inference Attack (MIA) metric is used to assess privacy protection. This could be more useful in practice than just checking classification results.

### Weaknesses
 * The core idea of using task vector negation for machine unlearning was proposed in (Ilharco et al., 2022). The idea proposed in this paper is a bit incremental, though coming up with this simple idea could still be non-trivial. It would be more convincing to augment this paper with more in depth discussion and analysis of why the proposed method could work.
* Evaluation of a few design choices are missing, please refer to the following questions section for more details.

### Questions
* Could you provide stats about how much ratio of the merged task vector becomes ratio? Especially when tuning the number of task vectors (e.g. 5, 10, 20, 30), would that have a significant impact on the zero ratio of the merged vector?
* How do you decide on the hyperparameters? For example, augmentation variants are used for CLIP finetuning but weight decay / epochs / label smoothing are used for standard image classifications. Is it sensitive to choose the hyperparameters to create a set of task vectors? What're the recommendations for a practitioner to create variants?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends the existing work of machine unlearning by generating a task vector based on a forget set for finetuning and subtracting it from the original model. The new proposal gives an approach to merge finetuned candidates by merging only the components of the task vectors with consistent signs. 
One advantage of the approach is computational efficiency in the merging step. 
The model both shows improvements on unlearning tasks and maintains performance on the retain set.

### Strengths
The paper has sufficient numerical results to support the claim for advantages of the proposal on several tasks, including better unlearning, less degradation on the retain set, and computation efficiency. These experiments show concrete evidence, especially the appendix. 
For “relationship with TIES-merging,” it is stated that “elements with inconsistent signs across task vectors are more closely related to the retain set than the forget set.” This is an essential claim for this paper, which is indicated by aggregated metrics of two methods and visualization of model activation during inference.

### Weaknesses
The evaluation set of forget and retain do not have clear separability and they may have overlap - ImageNet still requires knowledge relevant to the eight tasks of fine-grained datasets and the CIFAR-10 is sampled randomly. Though the higher accuracy for the current retain set can still be a positive evidence, some eval sets completely irrelevant to the forget set may be more strong. The lack of clear separation between the forget and retain sets makes it difficult to definitively assess the unlearning capabilities of the proposed method. Specifically, the use of ImageNet as a base for fine-grained datasets introduces a potential confound, as the model may retain general knowledge from ImageNet that is also useful for the fine-grained tasks, thus masking the true extent of unlearning. Furthermore, the random sampling of CIFAR-10 for the retain set does not guarantee that it is entirely independent of the forget set, potentially leading to an overestimation of the method's ability to preserve performance on unrelated data. This lack of clear separation and potential overlap between the forget and retain sets raises concerns about the generalizability of the results and the true effectiveness of the unlearning process.

### Questions
The paper shows the feasibility of the theory. My personal intuition is that the most promising application of machine unlearning is safety and privacy. However, the experiments focus on some functional recognition and, thus, have a retain eval set with overlap with the forget set. Is there any reason for not having related experiments?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for machine unlearning in deep learning models. Unlike existing methods that rely on a single fine-tuned model's task vector, NegMerge combines task vectors from multiple fine-tuned models trained with different hyperparameters, keeping only elements with consistent signs. This approach enables robust forgetting of the forget set while minimizing the impact on the retain set.

### Strengths
* Easy to follow
* Simple yet effective performance : intuitive approach 
* Experiments with different archihtectures (e.g CLIP and ResNet) which are commonly used.

### Weaknesses
 * Lack of technical contribution 
: They introduce practical approach but still lacks the theoretical depth. The paper may need for more analysis why sign-consistency aligns with forget set or exploring alternative merging method. 
* Reliance on empirical evidence
: As mentioned in Section 4.3, the paper relies on empirical results regarding performance on the forget set and retain set. The experimental results show that while the method achieves effective unlearning on the forget set, it compromises performance on the retain set, showing degradation in preserving non-targeted information compared to baselines. Without further analysis, it remains unclear whether these findings generalize across diverse datasets and model architectures.

### Questions
* As mentioned in the paper, only the final layer of CLIP's text encoder remains frozen during fine-tuning. Given that the CLIP model’s image-text alignment might still influence the unlearning process, I wonder if unfreezing the final layer would provide any additional benefits. Was this approach tested, or was it determined that freezing the final layer would not significantly impact the results? If so, what was the reasoning behind this choice?

* The method relies on multiple fine-tuned models, which can increase memory costs due to the need of several sets of weights. Compared to baselines, could you compare how computationally efficient this approach is and whether this efficiency is associated with performance improvements across the models?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The article introduces a model aggregation method for unlearning, which relies on task arithmetic. It uses multiple sets of hyperparameters to generate several task vectors for a single forget task, then merges them. During this merge process, parameters with sign conflicts are discarded, as they show low correlation with the forget set. Experiments demonstrate that this method is more effective in unlearning compared to other model merge techniques.

### Strengths
*   The paper proposes aggregating multiple models in unlearning, which is more advantageous than using a single model.
*   The method is simple and effective.

### Weaknesses
 *   The paper lacks an explanation of why the proposed method specifically targets unlearning. From the description, it seems more like an optimization method for task vectors. The core idea of discarding parameters with sign conflicts, while empirically effective, lacks a theoretical justification rooted in the specific challenges of unlearning. It's not clear why this approach would be more suitable for unlearning compared to other model merging scenarios, such as multi-task learning or continual learning, where similar optimization techniques might be applied.

*   Naturally, this raises further questions about how this model merge method performs on other tasks, such as multi-task adding and task analogies in task arithmetic. The paper does not explore the performance of the proposed method in these scenarios, which limits the understanding of its general applicability and the scope of its potential use cases. Without such analysis, it is difficult to assess whether the method is truly specialized for unlearning or if it is a more general optimization technique that happens to work well in this specific context.

*   The comparison of computational complexity is puzzling. The paper discusses the complexity of the validation process, but the training process's complexity is of greater concern. Moreover, for vanilla task arithmetic, multiple models are not used, so the (O(mn)) notation is misleading. The paper should clarify whether the multiple models are generated during the hyperparameter tuning process, and if so, this should be explicitly stated. The analysis should also consider the computational cost of generating these multiple models, not just the cost of merging them.

### Questions
*   The paper uses an averaging method to obtain the final task vector. Has there been any exploration of other methods, such as taking the maximum (similar to MagMax) or minimum values?
*   Why was RandAugment used for the CLIP model instead of varying hyperparameters?

### Soundness
4

### Presentation
4

### Contribution
3
