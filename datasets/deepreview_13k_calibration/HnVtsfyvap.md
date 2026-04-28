# Label-efficient Training of Small Task-specific Models by Leveraging Vision Foundation Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
Large Vision Foundation Models (VFMs) pretrained on massive datasets exhibit impressive perform on various downstream tasks, especially with limited labeled target data. However, due to their high memory and compute requirements, these models cannot be deployed in resource constrained settings. This raises an important question: How can we utilize the knowledge from a large VFM to train a small task-specific model for a new target task with limited labeled training data? In this work, we answer this question by proposing a simple yet highly effective task-oriented knowledge transfer approach to leverage pretrained VFMs for effective training of small task-specific models. Our experimental results on three target tasks under limited labeled data settings show that the proposed knowledge transfer approach outperforms task-agnostic VFM distillation, web-scale CLIP pretraining and supervised ImageNet pretraining approaches by 1-10.5%, 2-21%, and 2-14%, respectively. We also show that the dataset used for transferring knowledge has a significant effect on the final target task performance, and propose a retrieval-based approach to curate effective transfer sets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates how to construct a compute-efficient model from a pre-trained vision model for a downstream task with limited labeled training examples. To approach the task, the authors propose to first fine-tune the pre-trained vision model with the labeled data, distill it into a smaller model with a transfer set, and then fine-tune the distilled model with the labeled dataset. The effects of using in-domain and out-of-domain transfer sets are investigated and experiments are conducted to show the superiority of the approach against multiple baselines.

### Strengths
1. The investigation of using non-in-domain data for distillation and selecting relevant data for distillation is interesting.

### Weaknesses
1. Lacking Novelty: In essence, the proposed approach is knowledge distillation. Under the setup the authors consider, the proposed approach is the most straightforward approach one could consider. While the investigation of the use of not in-domain transfer dataset is interesting, the finding — when sufficient in amount, in-domain transfer set is better — is somewhat expected (e.g prior work[1] on open-set semi-supervised learning has shown that out-of-domain example can hurt performance of semi-supervised algorithm). It would be more interesting if the authors investigated the use of data from different domains (medical, satellite, clipart, etc) for distillation and proposed a strategy for selecting the right data for distillation. The current submission does contain some investigation on selecting the right data for distillation (section 3.5), but the investigation is not thorough enough to convince the reviewer that their strategy is applicable for different target tasks and with data from different domains. Furthermore, the paper does not consider the scenario where multiple pre-trained models are available, which is a more realistic setup given the current landscape of pre-trained models. The approach also relies on fine-tuning the pre-trained models which could be computationally prohibitive for extremely large models, limiting the practical applicability of the method.
2. Problematic Baselines: One would consider using the task-agnostic approach if fine-tuning the pre-trained models could be an issue (perhaps due to compute-constraint) but since the authors only consider compute-constraint during inference (instead of training), it seems unnatural to consider task-agnostic distillation as a baseline. In addition, the CLIP-pretrain baseline is trained on an internal dataset. Without knowing the distribution/statistics of the data and how the dataset compares to CC3M or DataComp-1B, it is difficult to understand whether the CLIP-pretrain baseline is worse because contrastive pretraining is not the right approach or the data used for training is flawed. Moreover, the task-agnostic distillation baseline is not a fair comparison as it does not involve the fine-tuning step, which requires significantly more compute than task-agnostic distillation. It is unclear if with the same compute budget, the task-agnostic approach could outperform the proposed approach, for example by distilling an ensemble of models.

### Questions
Questions:
1. 3.1 Alternative Approaches CLIP-Pretrain: The authors mentioned using a loss function similar to CLIP. Could the authors clarify what the difference is? 
2. Have the authors tried distilling from the patch tokens from CLIP? 


Suggestions:
1. Additional baseline: CLIP is a weakly supervised pre-training approach, the reviewer recommends adding self-supervised pre-training approaches such as DINO.
2. Transfer set: The use of not in-domain transfer set is worth more explanation. Right now, there is not much explanation/description on the use of not in-domain transfer set (e.g. why an in-domain transfer set is difficult to obtain).
3. Distillation mechanism: Distilling patch features is important for the segmentation task. However, there are only a few sentences describing the process. The reviewer recommends expanding the section on loss function either via using equations (the use of contrastive loss for distillation is uncommon) or by providing a figure explaining the process. 

Pre-rebuttal rating: Overall, the paper contains some interesting investigations on how to use distillation for constructing a small model from a large model pre-trained on different source tasks. However, the investigations are so far incomplete and the quality is not up to par with ICLR’s standards. The reviewer thus recommends rejecting the submission.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how we can train a smaller model for a new target task with limited training data using vision foundation models. They propose two frameworks task-agnostic and task-oriented for distilling data from foundation model to smaller model. Task agnostic or task oriented knowledge distillation involves creation of target set to transfer information from vision foundation model to smaller model. They show that their task agnostic approach or task oriented approach beats the models pretrained on large datasets like Imagenet or web-scale CLIP pretraining.

### Strengths
- Simple and clean experiments. Paper is well written as well. They experimented with different datasets including imabalnced ones showing the effectiveness of their approach.
- The paper shows that task agnostic and task oriented knowledge transfer beats the imagenet pretraining and CLIP based pre-training.

### Weaknesses
 - Most of the findings in the paper are obvious like task oriented or task agnostic knowledge transfer would lead to better performance than model pre-trained on CLIP or Imagenet because we are creating transfer set similar to target dataset.
- Transfer set creation process is mostly heuristic based and it's one of the important factors to get good performance on the target task.
- The paper lacks a detailed analysis of the impact of different transfer set sizes on the final performance. It's not clear how the size of the transfer set influences the effectiveness of the knowledge distillation process. A more thorough investigation into this aspect would be beneficial.
- The paper does not explore the sensitivity of the proposed approach to the choice of the vision foundation model. It would be valuable to understand if the performance gains are consistent across different foundation models or if certain models are more suitable for this transfer learning approach. The experiments should include a comparison with different foundation models to show the robustness of the approach.

### Questions
- Based on the figure 5 (left) if we use random transfer set the performance of the model on target task is similar to models pretrained on Imagenet or CLIP based pretraining. 
- Additionally, it's essential to clarify whether the target models, specifically MobileViT-v2, are pre-trained. If they are indeed pre-trained, the comparison between a 'normal' pre-trained model and a fine-tuned model (IM-Pretrain, CLIP-Pretrain), versus a model that undergoes pre-training followed by further fine-tuning with task-specific or task-agnostic training (Task-Agn, Task-Oriented), may lack meaningful context.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work study the problem of knowledge transfer from vision foundation model. Specifically, VFM are use to train a small task-specific dataset with limited labeled training data.

### Strengths
+ Proposed a three stages training strategy to train small DNN models with limited labeled training data by utiziling knowledge from VFMs. The VFM is first finetuned with the target task data and task-specific head, hence the finetuned CFM is more suitable for transfers task-oriented knowledge to the target small model with a transfer set.
+ This work observe that the transfer dataset distribution play an important role on the knowledge transfer, and empirically validate several approaches to curate the transfer dataset.
+ The resulting models (demonstrated with two VFMs and two mobile target architectures) show good performance than task-agnostic VFM distillation or pre-trained models. The empirical results support several insights that are benefitial to the research community.

### Weaknesses
This work show a task-oriented knowledge transfer strategy. The method is simple and intuitive. One might be complaining all the computation tools are from prior art, and the technical novelty is low. But i think such work bring good contribution to the research community, to more effectively train specialist small model. I don't see major flow on the proposed approach.

### Questions
On Fig 2(a), what are the three lines for DINOV2 - MobileViT-V2 - CC3M?

Note: the uploaded supplementary material is almost identical with the main paper, but with broken reference in text.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method called "task-oriented knowledge transfer" for training smaller, task-specific models by leveraging knowledge from large Vision Foundation Models (VFMs). This approach involves three steps:

1. Fine-tuning the VFM on the target task using labeled data.
2. Transferring knowledge from the fine-tuned VFM to the target model using an unlabeled dataset (transfer set) based on the knowledge distillation framework.
3. Fine-tuning the target model with labeled target task data.

An alternative method, called "task-agnostic knowledge transfer", involves distilling knowledge from the frozen VFM image encoder to the target model image encoder and then fine-tuning the target model using labeled data. 

The paper makes a comparison of task-oriented knowledge transfer with task-agnostic transfer, direct web-scale CLIP pretraining, and supervised ImageNet-1k pretraining. The authors show that the task-oriented knowledge transfer method performs better on many benchmarks.

The study also emphasizes the importance of the transfer set, where using a transfer set with an image distribution similar to the target task image distribution leads to better performance. For cases where a large target task-related transfer set is not readily available, the paper proposes a solution: curating task-related transfer sets using image retrieval with images from the limited labeled target task dataset as queries. Authors show that this method improved segmentation performance when compared to using a generic transfer set.

### Strengths
Originality:
- Proposes a new task-oriented knowledge transfer approach to leverage large pretrained VFMs to train small specialized models for new tasks with limited labeled data. 
- While retrieval-based strategies have been explored before, using retrieval to curate task-related transfer sets specifically for knowledge transfer is a creative application.
However, the core ideas of knowledge distillation and leveraging related datasets are not entirely new. The novelty lies in how these techniques are tailored and applied.

Quality:
- Comprehensive experiments comparing task-oriented transfer to baselines like task-agnostic transfer, CLIP pretraining, and ImageNet pretraining.
- Also has an ablation studies analyzing impact of transfer set distribution.

Clarity:
- The comparisons to baselines and ablation studies are well-presented.
- The limitations of the approach are clearly stated.

Significance:
- Enables leveraging powerful VFMs for specialized small model training under limited target data regimes.
- Shows the potential to learn specialized models even for domains not well-covered by web data.

### Weaknesses
 - The curated task-related transfer sets are shown to be effective, but the retrieval approach to create them is rather simple. There is scope to explore more sophisticated retrieval and data selection techniques like active learning, core-set selection, adversarial filtering etc. This could potentially lead to even better task-specific transfer sets. Specifically, the paper uses a basic image retrieval method based on feature similarity, but does not consider more advanced techniques such as clustering-based selection to ensure diversity within the retrieved set, or methods that explicitly optimize for the informativeness of the selected images for the knowledge transfer process. Furthermore, the paper does not explore the impact of the size of the retrieved set on the final performance, which could be a crucial factor.
- The paper could benefit from a comparative analysis with a few other knowledge transfer approaches. This would help provide a clearer picture of how the proposed method stands against existing techniques. For example, methods that use intermediate feature matching or those that explicitly model the relationship between the source and target domains could provide valuable insights. A comparison with methods that use a more structured approach to knowledge transfer, such as those based on graph neural networks, could also be beneficial.

### Questions
- The paper mentions that the target models may inherit the biases of the foundation models. It would be beneficial to discuss potential ways to address this issue.
- Lack of detail on fine-tuning VFMs: The paper mentions using labeled target task data to fine-tune VFMs but doesn't provide much detail on this process. More information on how VFMs are fine-tuned could help readers better understand the complete methodology.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
