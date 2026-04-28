# How to distill task-agnostic representations from many teachers?

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
Casting complex inputs onto tractable representations is a critical step in many fields. Differences in architectures, loss functions, input modalities, and datasets lead to embedding models that capture diverse information of the input.  Multi-teacher distillation seeks to exploit this diversity to create richer representations but often remains task-specific. We extend this framework by proposing a task-oriented setting that introduces an objective function based on the "majority vote" principle. We demonstrate that the mutual information between the student and the teachers is an upper bound for this function, providing a task-agnostic loss for our distillation procedure. An extensive evaluation is performed in different domains ---natural language processing, computer vision, and molecular modeling --- indicating that our method effectively leverages teacher diversity to produce more informative representations. Finally, we use our method to train and release new state-of-the-art embedders, enabling improved downstream performance in NLP and molecular modeling.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work aims perform Knowledge Distillation (KD) of task-agnostic representations from multiple teacher networks.

### Strengths
1. The work is motivated by a challenging and realistic setting in representation KD. The method is built upon a rigorous, bounded formulation, concerning the multi-teacher and task-agnostic challenges.

2. In details, the method train embedders to project the teacher's and student's representations to the same space, then minimize the divergence between the student's representations with those of the teacher's. While existing methods usually minimize a sample-wise divergence loss (KL Divergence, cross-entropy), novelly, the proposed method minimize the divergence between the student's representations with a conditional, parametric Gaussian distribution.

3. The evalutation spans three different modalities: vision, language, and molecular modelling, proving the flexibility of the method.

### Weaknesses
1. There are some questioning concerns regarding the empirical results, which hinders the significance of the work
- The CelebA dataset is mentioned but, surprisingly, never evaluated.
- Even though KD performance of the proposed methods is the highest with the proposed module, it is strangely sub-par to:
    - Training a student model on the training set, especially considering the student is a ResNet18 - a medium-sized models. For instance: 99%+ on MNIST, 97%+ on SVHN and 90%+ on CIFAR10
    - Standard KD methods: Early KD methods such as (Hinton et al., 2015) and FitNets (Romero et al., 2015) have also surpassed the reported KD performance.
    - Considering these deficits, is it possible that there exists any flaws in the training setup or it could be improved?

2. While the problem is formulated clearly and in details (Sec. 3.1-3.2), it is not majorly different from existing work, just in a different approach.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method for task-agnostic distillation from multiple pretrained teachers.
The problem is formulated as minimizing the disagreement between the student's predictions and the teacher's for any given task, which can be bounded by the conditional entropy of the teacher's embedding given the student's. This upper-bound does not depend on the specific task, and can therefore be chosen as a loss for task-agnostic distillation. The conditional distribution of teacher's embedding given the student's is parametrized by a Gaussian model whose mean and covariance are learned.

The distillation method is evaluated on three different applications:
- **Image classification** on CIFAR10, STL10, SVHN and variants of MNIST, with a ResNet18 as student and 9 teachers ranging in size from SqueezeNet to WideResNet50-2. Task-agnostic distillation is performed on the combination of datasets used for downstream evaluation.
- **Molecular property prediction (regression and classification)** on the ADMET and HTS tasks, with 9 teachers trained on different modalities (textual representations of molecular graphs, 2D-GNN and 3D-GNN) and a 10-layer GINE as the student. Task-agnostic distillation is performed on two datasets (ZINC-250k and ZINC-2M).
- **Natural language processing** on the MTEB benchmark, with four large teachers and the snowflake Merrick models as students. Task-agnostic distillation is performed on 6 million entries from a collection of datasets from the Huggingface Hub.

In these different settings, the teachers are chosen to be diverse in size, and with a performance varying across tasks. The trained student is shown to have consistently good results across all tasks, and to outperform all teachers on average.

### Strengths
- The paper tackles the important question of task-agnostic knowledge distillation from multiple teachers.  While task-agnostic knowledge distillation and task-specific multi-teacher distillation have been broadly studied, task-agnostic multi-teacher distillation is still understudied. 
- The proposed distillation loss is original and well-motivated.
- The proposed approach is evaluated on diverse applications: classification in 2D vision, molecular property prediction with GNNs, and natural language processing.

### Weaknesses
 **Related work.**
The related work overlooks a large portion of the literature on task-agnostic distillation. The question has been extensively studied, see e.g, Abbasi Koohpayegani
et al., 2020; Fang et al., 2021; Xu et al., 2022; Gao et al., 2022; Navaneet et al., 2021; Wu et al., 2022; Duval et al., 2023. None of these works require, *finetuning the teacher*, or *jointly training the teacher and the student* as claimed in the related work, and most of them do not require *the teacher and the student to have the same architecture*.

In light of the abundance of works on task-agnostic knowledge distillation, the following claim of the study could be revised:
*To the best of our knowledge, there are few methods that address task-agnostic representation distillation, especially in the context of multi-teacher approaches.*


**Experimental validation.**

Being unfamiliar with the literature on molecular property prediction and natural language processing, my remarks are focusing on the experiments on 2D vision.

1. The evaluation protocol for vision tasks is based on very small datasets (MNIST, STL10, SVHN, CIFAR10) with very small image sizes (MNIST is 28 $\times$ 28, CIFAR10 is 32 $\times$ 32). Using larger, more varied datasets would better showcase the method’s applicability across real-world scenarios. Even if computational resources were a constraint, there are numerous small-scale datasets more relevant than CIFAR or MNIST, such as those from the fine-grained classification community (e.g., CUB bird classification, FGVC-Aircraft, DTD for texture classification).

2. The teachers are small CNN models, which makes it challenging to fully appreciate the contributions of the authors. This study would benefit greatly from evaluations using larger ViT teachers such as DINOv2. The current choice of teacher models limits the potential for demonstrating the effectiveness of the proposed distillation method, as these smaller models may not fully capture the complexities of the data.

3. Lastly, as there is no data augmentation applied (Appendix D.1 only mentions a resizing to $(225, 225)$), the experimental results are very low. The achieved results are far lower than what could be obtained from training from scratch with proper data augmentation. It is not clear whether in a more challenging scenario with properly trained teachers, the conclusion would still hold. I suggest using standard augmentation strategies for training the teacher and student models, such as color jittering, cutout and random cropping (for CIFAR or MNIST), random resizing and cropping (for larger RGB images). The lack of data augmentation makes it difficult to assess the true potential of the method in realistic scenarios.

**Minor remarks.**

- *To do so, we first measure the agreement between the student’s Bayes classifier and the teachers’ for any given task. We show that it can be bounded by the conditional entropy of the teacher’s embedding given the student’s,*
$\rightarrow$ the conditional entropy bounds the **disagreement**, not the **agreement**.

### Questions
**Summary of suggestions** - please refer to Weaknesses section
- In the related work, mention the abundant literature on task-agnostic knowledge distillation
- For vision tasks, using **larger pretrained teachers** such as DINOv2, **evaluating on more impactful downstream tasks**, and **training models with appropriate data augmentation**. These experiments would demonstrate the applicability of the proposed approach to real-world scenarios.

### Soundness
2

### Presentation
2

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
The paper presents a multi-teacher knowledge distillation approach for creating task-agnostic representations, leveraging conditional entropy and Gaussian kernel-based learning. The authors aim to transfer diverse information from multiple pretrained teacher models to a student model, with applications in NLP, vision, and molecular modeling. The method introduces a task-agnostic loss function optimized by minimizing negative log-likelihood, showing improvements over baseline distillation methods (e.g., MSE and cosine similarity) across tasks.

### Strengths
1. The authors introduce a task-agnostic knowledge distillation framework, moving beyond traditional task-specific approaches. This is particularly valuable for generalizing representations across diverse tasks.

2. The paper offers a strong theoretical grounding for the proposed task-agnostic distillation loss, including insights into its formulation using conditional entropy and mutual information maximization.

3. The method is evaluated across three domains: vision, molecular modeling, and NLP, demonstrating consistent improvements in each, suggesting general applicability.

4. Results consistently show that the student models trained with this method outperform those trained with traditional distillation methods in accuracy, robustness, and generalizability.

### Weaknesses
1. The paper lacks a detailed discussion of potential challenges, such as computational overhead in training with multiple teacher models or the scalability of the method to even larger models and datasets. Specifically, the paper does not address the memory footprint of maintaining multiple teacher models in memory during training, which could become a bottleneck, especially with large models. Furthermore, the paper does not discuss the potential for increased training time due to the need to process data through multiple teacher models, which could limit the practical applicability of the method.

2. While the approach is tested against traditional distillation baselines, comparing with recent task-agnostic distillation methods, if any, would strengthen the empirical claims. The paper should include a more thorough comparison to other methods that aim to learn task-agnostic representations, even if they are not direct distillation methods. This would help to contextualize the contribution of the proposed method and highlight its unique advantages and disadvantages.

3. Although theoretically task-agnostic, the method’s robustness across a more extensive range of tasks within each domain is less explored. Additional benchmarks, particularly in NLP, could solidify the approach’s adaptability. For example, the NLP experiments could include tasks that require more complex reasoning or understanding of context, such as question answering or natural language inference. The paper should also explore the performance of the method on tasks with limited training data, which is a common challenge in many real-world applications.

### Questions
1. It is recommended to clarify how the task-agnostic nature of the proposed approach is ensured. For example, does this approach impose any constraints to PREVENT the method from IMPLICITLY learning task-specific nuances from the data?

2. How does the task-agnostic method generalize across tasks of a highly varying nature (e.g., between NLP, vision, and molecular modeling)? Are there tasks where performance might degrade without task-specific fine-tuning? Discussing them more will enhance the expressiveness of the paper.

3. The paper discusses the computational efficiency of the approach. It is suggested to provide additional details or empirical results on the computational cost, particularly when applying this method to large datasets or models.

4. How does the computational cost of this method compare to other baseline or existing SOTA task-agnostic and task-specific distillation techniques?

5. Is there a specific reason for choosing Gaussian kernel-based learning over alternative distance metrics for teacher-student alignment?

6. Although the method is compared to standard baselines, it is highly recommended to provide a comparison against recent task-agnostic distillation methods, if any exist. A comparative analysis would provide a clearer view of the approach’s relative advantages.

6. Please clarify if this approach uses different hyperparameters for the three domains (NLP, vision, molecular modeling) or maintains a consistent configuration across tasks.

7. The empirical evaluation seems broad, but how does the model handle fine-grained tasks or those with limited training data? For instance, is it still robust in few-shot learning scenarios?

8. Does the proposed method require specific architectures for the teacher and student models? Would the method be effective if applied to architectures like transformers versus CNNs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simple and effective method for distilling task-agnostic representations from an ensemble of teacher models. The authors frame the multi-teacher distillation problem as a task-enabling problem and introduce a novel approach using Gaussian kernels to estimate the conditional distribution of teacher embeddings given the student embedding.

### Strengths
1) Simplicity and Effectiveness: The proposed method is remarkably simple and yet achieves surprisingly strong results on various tasks. This is a significant strength of the paper.

2) Strong Empirical Gains: The experimental results demonstrate clear empirical gains over existing methods, showcasing the effectiveness of the proposed approach.

3) Comprehensive Evaluation: The authors evaluate their method on a diverse set of tasks, including image classification, text classification, demonstrating the versatility of the distillation technique.

### Weaknesses
1) Metric Space Preservation: As acknowledged by the authors, the proposed method might not always preserve the metric space of the teacher embeddings, depending on the task at hand. This could be a potential limitation but not something I would hold against the paper -- sometimes things might work better for a specific aspect, it would be nice to investigate why or how to fix things given normal embedding models are generalists for this one reason. 

2) Limited Model and Data Scale: The experiments are primarily conducted with relatively small models and datasets. It would be more compelling to see results with larger models for both vision and language and larger datasets to assess the scalability of the method.

### Questions
This paper presents an interesting and effective method for multi-teacher distillation with strong empirical results. However, the potential issue with metric space preservation and the limited exploration of larger models and datasets slightly weaken the current submission.

Recommendation:

I am leaning towards acceptance, but I believe the paper could be strengthened by addressing the following points:

1) Provide further analysis and discussion on the potential impact of metric space distortion on different tasks.
2) Consider experimenting with larger models and datasets to demonstrate the scalability of the method.

I am interested in seeing other reviewers' thoughts on these points during the discussion phase.

### Soundness
3

### Presentation
3

### Contribution
3
