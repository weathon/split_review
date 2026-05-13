# TaCA: Hot-Plugging Upgrades for Foundation Model with Task-agnostic Compatible Adapter

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Visual foundation models, such as CLIP, exhibit exceptional proficiency in learning feature representations from extensive datasets via self-supervised techniques, showcasing noteworthy aptitude for transfer learning and generalization. A growing number of applications based on visual foundation models are emerging, including innovative solutions such as BLIP-2. These applications employ pre-trained CLIP models as upstream feature extractors and train various downstream modules to accomplish diverse tasks. However, scenarios necessitating system upgrades that entail updating the foundational model pose challenges, as they entail the inefficient and inflexible process of retraining all downstream modules to align with the new foundational model. In this paper, we propose an innovative and valuable task, Hot-Plugging Upgrades for visual foundation models. The aim is to seamlessly integrate superior-performing foundation models into downstream applications without adjusting the downstream modules. To realize this objective, we introduce a parameter-efficient and task-agnostic Compatible Adapter, referred to as TaCA, which promotes compatibility across distinct foundation models while concurrently enhancing performance for the new models. We conduct extensive experimental validation of TaCA using different scales of models with up to one billion parameters on various tasks such as video-text retrieval, video recognition, and visual question answering. The results consistently affirm the efficacy of TaCA in facilitating hot-plugging upgrades for visual foundation models. Codes and models will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This manuscript introduces a new hot-plugging adapter, with which the task-specific model's foundation backbone can be replaced without re-training for both the backbone and the task-specific head. 
- The proposed method is tested on the CLIP series foundation models and evaluated on various vision-language tasks. The results validate the proposed method's effectiveness. Specifically, the performance of downstream tasks is improved when the backbone networks are replaced with more powerful ones.

### Strengths
1. The idea of hot-plugging adapters is interesting. It could have a good impact on future research and other applications. 
2. The proposed method is technically sound. 
3. The manuscript is well-written and easy to follow. 
4. The comprehensive experiments validate the model's effectiveness on various tasks.

### Weaknesses
1. While the idea of hot-plugging adapters is intuitively sound at first glance, this paper lacks quantitative evidence to support this motivation. Specifically, the motivation of this paper is: *When replacing the visual backbones, fine-tuning the proposed adapter is better than fine-tuning the downstream task-specific head*. Therefore, a comparison between these two fine-tuning methods should be presented, and such a comparison should be in a fair enough setting because, in my opinion, it should be the most important experiment for the whole manuscript. Specifically, the author should compare 1) the trainable parameter amounts, 2) training FLOPs, 3) The data amounts needed for fine-tuning, and 4) the fine-tuning schedule of these two fine-tuning paradigms. In addition, the results in Table 1 show that the *TACA-BetterModel*'s performance is inferior to directly fine-tuning the task-specific head with a *BetterModel*, i.g., ViT-H, which also shows the necessity of such a comparison. The paper needs to clarify under which conditions the proposed adapter is truly beneficial compared to simply fine-tuning the task-specific head, considering factors like the magnitude of backbone change and the downstream task complexity. The current presentation does not provide a clear picture of the trade-offs involved.
2. The symmetric adapter is a very interesting point of this manuscript, as it outperforms the standard adapter. It would be better to include some experiments to study its effectiveness on other tasks, e.g., image generation or some NLP tasks. The current experiments are limited to vision-language tasks, and it is unclear whether the symmetric adapter's benefits generalize to other modalities or tasks with different architectural requirements. For example, it would be valuable to see how it performs in a generative setting or in tasks where sequential processing is crucial.
3. The manuscript should include more experiments to show its generalization ability to other non-CLIP models. For example, can the proposed method work on classic vision tasks, like detection or segmentation? The paper should explore the applicability of the adapter approach to models with different architectures and pre-training objectives, such as those used in object detection or semantic segmentation. This would demonstrate the robustness and versatility of the proposed method beyond the CLIP framework. The current experiments are too narrowly focused on CLIP-based models.
4. I am also curious if the method can be applied to replacing *different* foundation models. For example, can we use it to replace a DINO ViT with an ImageNet-22k Supervised ViT? The paper needs to investigate the compatibility of the adapter with different pre-training paradigms and model architectures. It is unclear whether the adapter can effectively bridge the representational gap between models trained with different objectives and datasets. The current experiments only consider models within the same family.
5. The proposed head-fixing strategy makes me think about the head-inheriting trick that is commonly used in knowledge distillation [a][b]. Therefore, discussing it in the related work section will increase the comprehensiveness of this work.

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Hot-Plugging Upgrades for visual foundation models. The aim is to seamlessly integrate superior-performing foundation models into downstream applications without adjusting the downstream modules. To realize this objective, this paper introduces a parameter-efficient and task-agnostic Compatible Adapter, referred to as TaCA, which promotes compatibility across distinct foundation models while concurrently enhancing performance for the new models. The paper is written well and easy to follow.

### Strengths
1. This paper spearheads the exploration into the scenario of upgrading large-scale foundation models and introduces hot-plugging upgrades of visual foundation models in modular frameworks.
2. This paper introduces a parameter-efficient upgrading strategy using a Task-agnostic Compatible Adapter (TaCA)
3. The paper is written well and easy to follow.

### Weaknesses
1. The approach is incremental, and the techniques employed are all verified strategies. Specifically, it utilizes a combination of distillation methods and contrastive learning, forming a hybrid approach.

2. Why not conduct experiments on more basic image classification and retrieval datasets (e.g., MSCOCO and imagenet)? If the effectiveness of this method can be verified on a more basic dataset, I am willing to increase my score

3. In my opinion, TaCA, which utilizes an adapter to align a large-scale visual model with a smaller-scale visual model, undermines the purpose of changing the visual model. This approach hampers the transferability of the large-scale visual model, potentially limiting its advantages. Moreover, based on the results presented in Table 2, TaCA only shows marginal enhancements in downstream video classification tasks compared to directly employing a large-scale visual model.

4. while this paper assesses the effectiveness of TaCA in video-related tasks, it overlooks numerous studies that apply CLIP to image-based tasks such as image-text retrieval, image segmentation, and few-shot image classification. The absence of experiments on image-related tasks in this paper creates a gap in evaluating TaCA.

5. What would happen if Old VFM and New VFM were different (e.g., VIT-B to ResNet-50)? Can we distill and transfer knowledge between VFMs of different architectures to each other? For example, distilling knowledge from miniGPT or LLAMA (decoder only architecture) to CLIP?

### Questions
1. The method is incremental, and the methods used are all validated schemes, which is actually distillation method combined with contrastive learning.
2. Why not conduct experiments on more basic image classification and retrieval datasets

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introducing the task of hot-plugging upgrades for visual foundation models. And it proposes TaCA, which aims at effectively replacing visual foundation model without any downstream adaptation. Extensive experiments on video-related tasks indicate the effectiveness of TaCA.

### Strengths
1. This paper introduces the task of hot-plugging upgrades for visual foundation models, which aims at effectively replacing upstream visual fundation model.

2. The experimental results prove TaCA can upgrade the visual foundation models without requiring the training data from downstream video-related tasks.

### Weaknesses
TaCA forces large-scale visual model to align with relatively small-scale visual model using adapter. It defeats the purpose of changing the visual model in my opinion. This approach restricts the transferability of the large-scale visual model, which may limit its potential benefits. Additionally, according to the results presented in Table 2, TaCA provides marginal improvements on downstream video classification tasks comparing to directly using large-scale visual model.

This paper evaluates the effectiveness of TaCA on video-related tasks. However, there are a number of works transfer CLIP to image-based tasks, e.g. image-text retrieval, image segmetation, and few-shot image classification. The absence of experiments on image-related tasks in this paper leaves a gap in evaluating TaCA's capability.

### Questions
What is the training overhead in terms of time?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a new task, Hot-Plugging Upgrades for visual foundation models. The aim is 
to seamlessly integrate superior-performing foundation models into downstream applications without adjusting the downstream modules. To realize this objective, The authors introduce a parameter-efficient and Task-agnostic Compatible Adapter, referred to as TaCA, which promotes compatibility across distinct foundation models while concurrently enhancing performance for the new models. The authors conduct extensive experimental validation of TaCA using different scales of models with up to one billion parameters on various tasks such as video-text retrieval, video recognition, and visual question answering.

### Strengths
- The authors propose a hot-plugging upgrading module, which is interesting.  
- The experiments have been conducted to illustrate the superiority of the proposed method.

### Weaknesses
 - The authors should validate the flexibility of the proposed TaCA module. How about the performance when the TaCA is aligned with the other LLMs? 
- The qualitative analysis and visualization in experiments are missing.

### Questions
- The authors should validate the flexibility of the proposed TaCA module. How about the performance when the TaCA is aligned with the other LLMs? 
- The qualitative analysis and visualization in experiments are missing.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
