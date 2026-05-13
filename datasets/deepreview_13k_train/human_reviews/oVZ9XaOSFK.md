# Downstream Task Guided Masking Learning in Masked Autoencoders Using Multi-Level Optimization

- Decision: Reject
- Scores: 3, 5, 5, 6, 3

## Abstract
Masked Autoencoder (MAE) is a notable method for self-supervised pretraining in visual representation learning. It operates by randomly masking image patches and reconstructing these masked patches using the unmasked ones. A key limitation of MAE lies in its disregard for the varying informativeness of different patches, as it uniformly selects patches to mask. To overcome this, some approaches propose masking based on patch informativeness. However, these methods often do not consider the specific requirements of downstream tasks, potentially leading to suboptimal representations for these tasks. In response, we introduce the Multi-level Optimized Mask Autoencoder (MLO-MAE), a novel framework that leverages end-to-end feedback from downstream tasks to learn an optimal masking strategy during pretraining. Our experimental findings highlight MLO-MAE's significant advancements in visual representation learning. Compared to existing methods, it demonstrates remarkable improvements across diverse datasets and tasks, showcasing its adaptability and efficiency

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a new MAE training framework, Multi-Level Optimization MAE (MLO-MAE). The authors add two additional learning objectives to conventional MAE training: linear probing and mask selector optimization. Linear probing loss trains a classifier using class labels, and the mask selector learns a mask that maximizes classification performance. The mask selector also used for MAE training that is effective for MAE's finetuning performance. The three objectives are optimized by `betty-ml` library's multi-level optimization algorithm.

### Strengths
- Learning the mask with multi-level optimization is an interesting approach.
- ImageNet performance in Table 1 is impressive. It is hard to achieve 84.8 accuracy with MAE framework.

### Weaknesses
 - The paper lacks motivation and insight explaining the improvement of MLO-MAE. Although MLO-MAE achieves impressive performance, I believe it is hard to contribute to MAE researchers without proper theoretical background or analysis.

- MLO-MAE is not a self-supervised learning (SSL) method. It utilizes image class labels as a multi-objective training method. Since target task-agnostic pre-training is an important characteristic of SSL, MLO-MAE's contribution is significantly limited to conventional SSL.

- The presentation is not good. The main algorithm is hard to understand through formulas in 3.2. It would be better to revise the formula to improve readability.

- The experiment only covers a single model size (ViT-B), which is not enough to validate MAE-variant performance. Validation on various model sizes in ImageNet is required to argue for an improved MAE framework in general.

### Questions
- MLO-MAE utilizes learnable masking that is trained to maximize linear probing performance. What is the theoretical background and insight behind this design? Why does this masking improve MAE fine-tuning performance?

- MLO-MAE makes classification-friendly random masking, which can be considered as an easy masking strategy. Can it achieve performance improvement in large models? How about small models like ViT-S?

- In Table 3, improvement in downstream tasks looks smaller than in ImageNet. Does this mean MLO-MAE's improvement is biased toward the pretraining dataset? How about using the downstream dataset as an objective in Stage 2 and Stage 3?

- Even though another learnable masking (SemMAE and AutoMAE) is not effective on benchmarks, MLO-MAE achieves a completely different pattern with a learnable mask. What makes the difference? What are the minimal changes to make learnable masks beneficial?

- Table 5 omits $AP_{mask}$. Does MLO-MAE also improve $AP_{mask}$ of mask-RCNN in COCO?

- It is a surprising result that BLO-MAE has no positive effect on performance. Why is it so different from MLO-MAE? Does BLO-MAE fail to converge on any of Stage?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes an interesting pretraining framework, MLO-MAE, which guides the masking process in masked image modeling by leveraging labels from downstream tasks to learn representations that meet task-specific requirements. The pretraining of MLO-MAE involves three main stages: pretraining the image encoder, training the classification head, and updating the masking network. MLO-MAE optimizes these three stages through a multi-level optimization algorithm.

### Strengths
1. This paper addresses a valuable and important problem. Given the inherent differences between images and text, using random masking as in NLP may not be optimal for masked image modeling. 
2. The proposed method is concise and effective, achieving strong performance across multiple benchmarks.
3. The paper is well-organized, making it easy to reproduce and follow.

### Weaknesses
1. The pretraining of MLO-MAE relies on labels from downstream tasks, which does not align with the self-supervised learning paradigm of learning general representations from the data itself. MLO-MAE resembles a supervised pretraining approach, so the experimental setup that mainly compares it with SSL methods is somewhat inappropriate.
2. The main weakness of this paper lies in the experiments:
    - Although MLO-MAE demonstrates improved fine-tuning and linear probing performance (Sec 4.3), it already leverages class information during pretraining, making comparisons with self-supervised baselines unfair and insufficient to verify MLO-MAE's effectiveness. The performance gains could be attributed to the use of labels during pretraining rather than the effectiveness of the masking strategy itself.
    - I notice that in the transfer learning experiments (Sec 4.4), the pretrained model undergoes additional supervised fine-tuning on imagenet, which diverges from the typical transfer learning paradigm. Is this fine-tuning necessary? Can MLO-MAE be transferred to downstream tasks without it? Does the use of different labeled data during pretraining affect the performance of transfer learning?
    - The paper also lacks an analysis of the learned masking patterns. How do the masking patterns learned by MLO-MAE differ from those of other methods? Why do the learned masking patterns help in learning better representations? A more in-depth analysis is needed to support the main claims of this work.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a variant of the masked autoencoder (MAE) designed to explicitly enhance the performance of downstream tasks. The framework consists of three main stages: (1) pretraining an image encoder using the MAE approach based on the mask generator network, (2) training a classification head with the frozen MAE-pretrained encoder on a downstream task, and (3) training a masking network with the trained classification head to minimize the loss to tune the masks. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
- The idea of explicitly introducing these three steps to improve downstream task performance is intuitive and reasonable.
- The performance improvements over the baseline looks impressive.

### Weaknesses
 - While the idea appears practical and well-founded, the rationale behind including specific steps and how each contributes to overall performance are missing. Furthermore, it is unclear why the proposed method would outperform SemMAE and AutoMAE, which also use adaptive mask generation. The authors are encouraged to provide some insights into why their approach may offer an advantage over these similar methods.
- The multi-level optimization presented appears to depend heavily on the previous steps. While the problem formulation in Eq. (4) integrates all sub-objectives, each optimization step must wait for the completion of the previous one. This approach seems a bit cumbersome, potentially leading to cache and memory issues (which may not be fully resolved by standard packages) and slowing down the process due to the sequential nature of the steps.
-  There are no analyses of the generated masks during or after training, nor comparisons with the outputs of other mask generators (e.g., SemMAE's and AutoMAE's). The reviewer believes presenting this analysis is crucial, as it could provide insights into training dynamics, specifically which parts of images should be visible or reconstructed to impact performance.
- In training, stages 2 and 3 utilize downstream task data, which seems to be used more extensively than in standard practice, where downstream data is only introduced during the fine-tuning stage. This incurs an unfair evaluation. The memory issue is not just about the Jacobian computation but also about the overall memory footprint during the multi-stage training, which could limit the batch size and affect training stability. The authors should clarify the memory usage and how it scales with the model size and dataset.
- The analysis of the generated masks is not convincing. The authors claim that the method masks background regions, but the visualizations do not clearly support this. The patterns appear random, and it's unclear if they are truly focusing on object-relevant regions. The authors should provide a more rigorous analysis of the mask patterns, perhaps with higher masking ratios to see if a trend emerges.
- The use of downstream data during pre-training is a major concern. Standard pre-training methods do not use downstream task data to ensure the pre-trained model's generalizability. The authors' approach of using downstream data in stages 2 and 3, and then again during fine-tuning, raises questions about the validity of the evaluation. It is recommended to evaluate the method on downstream datasets that are not related to the fine-tuning dataset to assess its generalization capability.
- The impact of the random data split on performance is not addressed. The authors use an 8:2 split of the ImageNet training set, but the randomness of this split could lead to performance variations, especially given potential mislabeled samples in the original dataset. The authors should investigate this issue through experiments and provide a clear plan for addressing this limitation in future work.

### Questions
- The reviewer still speculates some results, for example, why ImageNet pre-training/fine-tuning requires only 50 epochs to surpass other methods, especially since all steps use the same ImageNet dataset and the pre-training stage even trains on smaller images (80%). Could the authors provide some insights?
- The proposed method appears to adapt specifically to ImageNet when pre-training the classification head on ImageNet in step 2. This may raise issues, such as difficulty handling discrepancies in patch size between pre-training and fine-tuning stages. How can a model trained on ImageNet in this way be effectively applied to downstream tasks like CIFAR?
- The dataset is split into training and validation data for the three-step training proposed in this paper. Can the authors ensure consistent performance when the data split varies due to changes in random seeds or other factors?

### Soundness
2

### Presentation
3

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
In this submission, the authors aim to improve visual representation learning in self-supervised pretraining. Their motivation is that traditional Masked Autoencoders (MAE) overlook the varying informativeness across different patches. They hope to leverage feedback from downstream tasks to guide the learning of masking strategies during pretraining. The proposed framework, named Multi-level Optimized Mask Autoencoder (MLO-MAE), consists of three interdependent stages: pretraining the image encoder, training the classification head, and updating the masking network. These stages are executed end-to-end through a multi-level optimization (MLO) strategy. Finally, their experiments show performance improvements of MLO-MAE across multiple datasets and tasks.

### Strengths
The experiments involve multiple benchmark datasets and also validate the transfer learning ability on downstream tasks such as fine-grained classification and semantic segmentation. Additionally, various visualization analyses are provided.

### Weaknesses
1. Considering the additional computational overhead introduced by the multi-level optimization, it is hoped that more comparisons with other baselines can be added, such as ColorMAE.
2. In Section 4.1, the authors mention that they divide the original training set of each dataset into two subsets, D_tr and D_val. From my understanding, this approach is essentially similar to dividing datasets into training, validation, and test sets in machine learning. The validation set is used to monitor the training process. The difference here is that instead of manual adjustments by developers, the authors use multi-level optimization (MLO) to automate the adjustment of model parameters. As I am not very familiar with this field, I am curious about the transferability and applicability of this automated approach.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Existing Masked Image Modeling (MIM) methods mask patches without considering feedback from downstream tasks. This study introduces a method to utilize such feedback for learning an optimal masking strategy. The authors propose a framework called Multi-level Optimized Mask Autoencoder (MLO-MAE), which leverages downstream task feedback to determine an effective masking strategy during pretraining. Specifically, MLO-MAE operates in three stages: pretraining the image encoder, training the classification head, and updating the masking network. The proposed masking strategy, guided by the feedback from the classification task, tends to mask patches on foreground objects directly related to class labels. Empirical results on eight benchmarks demonstrate the effectiveness of MLO-MAE, showing it outperforms the MAE baseline.

### Strengths
Extensive experiments across eight benchmarks and three different tasks (*i.e.*, classification, object detection, and semantic segmentation) demonstrate the effectiveness of the proposed MLO-MAE, surpassing the performance of the MAE baseline.

### Weaknesses
 **Deviation from the Motivation:**
The paper's motivation is that "previous MIM methods mask patches without incorporating feedback from downstream tasks (line 053)," and this study seeks to "use feedback from downstream tasks to learn the optimal masking strategy (line 062)." However, the current implementation only utilizes feedback from the classification task to guide the masking strategy, deviating from the original motivation. If downstream tasks were object detection or semantic segmentation, relying solely on a classification task in Stage 2 would likely result in a suboptimal masking strategy. Specifically, the features learned during Stage II, being optimized for classification, may not be the most effective for tasks like object detection or segmentation, which require different feature representations. The misalignment between the Stage II objective and the downstream task could limit the generalizability of the learned masking strategy.


**Unfair Experimental Comparisons:**
The proposed MLO-MAE method leverages additional knowledge from classification labels in ImageNet-1K, making a direct comparison with the MAE baseline unfair. The MAE baseline is trained solely on reconstruction loss, while MLO-MAE benefits from classification labels during pretraining. This additional supervision during pretraining gives MLO-MAE an advantage, making it difficult to isolate the impact of the proposed masking strategy. A fair comparison would require both methods to use the same level of supervision during pretraining, or to evaluate the methods in a transfer learning setting where neither method uses downstream labels during pretraining.


**Unconvincing Conclusions:**
- It remains unclear why the masking strategy in MLO-MAE effectively "masks patches on foreground objects directly relevant to the class labels" (line 1113), and further discussion is needed to clarify this aspect. The paper lacks a clear explanation of the mechanism by which the masking network learns to focus on foreground objects. It is not obvious how the classification loss directly translates to masking foreground regions, and this requires a more detailed analysis. For example, visualizing the learned masks and correlating them with object boundaries would be beneficial.
- The ablation study on the number of unrolling steps was conducted solely on the CIFAR-10 dataset, which shows that ''an increase in the unrolling steps leads to gradual improvement in accuracy'' (line 474). However, given the limited scale of CIFAR-10, the same study should also be performed on ImageNet-1K for a more convincing conclusion. The conclusions drawn from CIFAR-10 may not generalize to larger and more complex datasets like ImageNet-1K, making the ablation study less compelling.
- The ablation study for patch sizes was restricted to small images (32x32) on CIFAR-10. To strengthen the conclusion, similar studies should be conducted on larger images, such as those in ImageNet-1K. The performance of different patch sizes may vary significantly on larger images, and the current study does not provide sufficient evidence to support the generalizability of the findings.


**Writing Issues:**
- In Stage 3, the method for updating the masking network $T$ remains unclear, even after thoroughly reviewing the method section (lines 222-228) and Figure 1. The description of how the validation loss is used to update the masking network is vague, and the mathematical formulation is not sufficiently detailed. A clearer explanation of the gradient computation and the optimization process is needed.
- There is no explanation provided for "unrolling steps."

### Questions
- Q1: Why do the authors choose to use the classification task in Stage 2 for all downstream tasks, instead of tailoring different tasks in Stage 2 to match each specific downstream task?

- Q2: How does the masking strategy in MLO-MAE manage to "mask patches on foreground objects directly relevant to the class labels" (line 1113)?

- Q3: What makes "masking patches on foreground objects directly relevant to the class labels" an optimal masking strategy? If all patches of the foreground objects are masked, does it still qualify as an optimal strategy?

- Q4: Could you elaborate on the implementation of Stage 3? Specifically, how is the masking network updated using the validation loss?

- Q5: Could you provide a more detailed explanation of the unrolling steps?

### Soundness
2

### Presentation
2

### Contribution
2
