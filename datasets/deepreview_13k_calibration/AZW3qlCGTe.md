# Enhancing Instance-Level Image Classification with Set-Level Labels

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Instance-level image classification tasks have traditionally relied on single-instance labels to train models, e.g., few-shot learning and transfer learning. However, set-level coarse-grained labels that capture relationships among instances can provide richer information in real-world scenarios. In this paper, we present a novel approach to enhance instance-level image classification by leveraging set-level labels. We provide a theoretical analysis of the proposed method, including recognition conditions for fast excess risk rate, shedding light on the theoretical foundations of our approach. We conducted experiments on two distinct categories of datasets: natural image datasets and histopathology image datasets. Our experimental results demonstrate the effectiveness of our approach, showcasing improved classification performance compared to traditional single-instance label-based methods. Notably, our algorithm achieves 13\% improvement in classification accuracy compared to the strongest baseline on the histopathology image classification benchmarks. Importantly, our experimental findings align with the theoretical analysis, reinforcing the robustness and reliability of our proposed method. This work bridges the gap between instance-level and set-level image classification, offering a promising avenue for advancing the capabilities of image classification models with set-level coarse-grained labels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper propose to utilize set-level coarse-grained labels to improve fine-grained image classification. Essentially the paper is proposing a new pretraining method, key to the method is selecting a dataset with coarse label, and use the set prediction on coarse label as pretraining task. The paper provides theoretical analysis for the proposed approach, showing that using coarse-grained labels speed up the learning on the fine-grained classification task. The paper also demonstrates the effectiveness on several datasets.

### Strengths
1. The idea of using set prediction on coarse label as pretraining task seems novel
2. The performance seems strong compared to other baselines

### Weaknesses
1. More baselines for strong self-supervised pretraining methods (e.g., BYOL, DION  are needed to demonstrate the effectiveness. As proposed method is essentially a pretraining strategy, that bears a lot of similarity with exisiting self-supervised learning method

2. More ablations and discussion on some key questions are needed (see below)

### Questions
1. To what extent does the similarity between the pretraining dataset and its coarse labels and the target dataset with its fine labels affect the effectiveness of the method? For instance, can the method perform well when the pretraining dataset is CIFAR-100 while the downstream task involves a medical dataset? In such a scenario, which pretraining method is preferable: supervised pretraining on ImageNet, self-supervised pretraining (ignoring labels entirely), or the proposed method?

2.  Given the same 'related' dataset, if you have both the fine-grained label and coarse-grained label, which pretraining strategy is preferable?
(Let say your downstream task is classification on a medical image dataset, with fine-grained label A,B,C. The pretraining dataset you have is another medical image dataset (thus more related than ImageNet). You have both coarse label D,E,F and fine-grained label G,H,I,J,K,L. In this case, is fully supervised pretraining on G,H,I,J,K,L more beneficial on set level coarse pretraining on D,E,F more beneficial?)

### Soundness
3 good

### Presentation
2 fair

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
The paper presents a new technique aimed at boosting instance-level image classification by utilizing set-level labels. Compared to conventional methods that rely on single-instance labels, the proposed approach achieves a 13% increase in classification accuracy when tested on histopathology image datasets. A theoretical examination of the method outlines conditions for rapid reduction of excess risk rate, adding credibility and robustness to the technique. This research serves to connect instance-level and set-level image classification, providing a noteworthy direction for enhancing image classification models that use coarse-grained set-level labels.

### Strengths
- The paper presents a new technique for enhancing instance-level image classification by making use of set-level labels. This serves to fill the existing gap between instance-level and set-level image classification.

- The robustness and reliability of the proposed method are underscored by a theoretical analysis, which outlines conditions for the rapid reduction of excess risk rate.

- The paper clearly articulates the proposed method, shedding light on both its theoretical underpinnings and empirical results. These results are demonstrated on both natural and histopathology image datasets.

- The method put forth in the paper holds promise for extending the capabilities of image classification models. By leveraging set-level coarse-grained labels, the approach achieves better classification performance compared to traditional methods reliant on single-instance labels. This is particularly relevant in real-world contexts where set-level labels may offer more comprehensive information.

### Weaknesses
 - The use of coarse-grained labels like TCGA or NCT is an interesting choice. These are indeed umbrella terms for various subcollections, and traditionally they may not provide a strong learning signal. It could be beneficial to delve into why these particular labels were chosen and what advantages they offer in this context.

- Your team's approach to pretraining with coarse labels and then fine-tuning on a support set is a solid and proven method. However, it would enrich the work to articulate what sets this particular application or implementation apart in terms of novelty.

- The comparison with SimCLR and simSIAM provides useful insights, but considering the advancements in the field, benchmarking against more recent self-supervised learning methods like DINO or DINOv2 might offer a more comprehensive evaluation.

- To further validate the generalizability of the method, it could be insightful to include results against standardized few-shot learning benchmarks, such as Mini-Imagenet 5-way (1-shot) or SST-2 Binary classification.

- Adding ablation studies that feature additional pretrained models—or even models pretrained without the coarse labels—could help underscore the specific benefits of using coarse-grained label-based pretraining in your approach.

- Your methodology would be even more robust if additional training details are shared. Information on image augmentations, learning schedules, and optimizer settings could offer valuable insights and help in the reproducibility of your results.

### Questions
- Do you think you could pictorially diagram the approach adding the relevant details? It is unclear to me if the method essentially pretrains using coarse-labels and then fine-tunes on the test set using the support set or is there more to the method

- Why are the methods for pretraining SupCon and FSP chosen for pre-training? Adding rationale for this might help motivate the choice of pretraining method

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new setup for few-shot learning. The proposed model is pre-trained on coarse-grained set-level labels first and fine-tuned with fine-grained labels. Authors also provide theoretical analysis on the convergence rate for downstream tasks, which shows coarse-grained pre-training can enhance the learning process of fine-grained label tasks. The experiments are performed on both natural image datasets and medical histopathology datasets, where the baselines are mostly self-supervised learning methods.

### Strengths
I think the idea of using coarse-grained label is reasonable. The conclusion of enhancing learning process of fine-trained labels is inspiring.

### Weaknesses
 - I have some questions about the method part, Sec. 2.1. In Fig.2 (a), are input samples all belongs to the same set-level labels? I am confused by this figure and Fig.1(a) CIFAR images. What I believe is correct is that each batch contains samples belong to different set-level labels, and the coarse label is assigned to each sample for pre-training. 
- How is SupCon trained? It is superised that supervised contrastive learning perform a lot worse than basic CE approach in most setups. There is not much information about training details.


### Questions
- There should be more training details about the framework in Sec.2.1. 
- Fig. 3 is referenced in text before Fig. 2
- Most of the refernece hyperlinks other than page 1 is not working.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
