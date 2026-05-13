# Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning

- Decision: Accept
- Scores: 5, 6, 6, 3

## Abstract
Self-supervised learning (SSL) offers a compelling solution to the challenge of extensive labeled data requirements in traditional supervised learning.
With the proven success of Vision Transformers (ViTs) in supervised tasks, there is increasing interest in adapting them for SSL frameworks. However, the high computational demands of SSL pose substantial challenges, particularly on resource-limited platforms like edge devices, despite its ability to achieve high accuracy without labeled data.
Recent studies in supervised learning have shown that token pruning can reduce training costs by removing less informative tokens without compromising accuracy. However, SSL’s dual-branch encoders make traditional single-branch pruning strategies less effective, as they fail to account for the critical cross-branch similarity information, leading to reduced accuracy in SSL.
To this end, we introduce SimPrune, a novel token pruning strategy designed for ViTs in SSL. SimPrune leverages cross-branch similarity information to efficiently prune tokens, retaining essential semantic information across dual branches. Additionally, we incorporate a difficulty-aware pruning strategy to further enhance SimPrune's effectiveness.
Experimental results show that our proposed approach effectively reduces training computation while maintaining accuracy. Specifically, our approach offers 24\% savings in training costs compared to SSL baseline, without sacrificing accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes Similarity-Based Pruning Method (SimPrune), a token pruning technique specifically designed for Vision Transformers in self-supervised learning (SSL). Unlike traditional pruning methods that rely on single-branch self-attention mechanisms, SimPrune uses cross-branch similarity to select tokens for pruning, preserving crucial cross-branch semantic consistency in SSL, thereby avoiding loss of important information due to improper pruning.

Experiments show that SimPrune can reduce training costs by approximately 24% while maintaining accuracy.

### Strengths
1. SimPrune is compatible and tailored for the dual-branch Siamese architecture used in SSL, where each branch processes different augmented versions of the same image. SimPrune ensures token consistency across branches, preventing unnecessary information loss, which is challenging to achieve with single-branch pruning. This makes it especially suitable for SSL.

2. SimPrune introduces a “difficulty adjustment during training” pruning strategy. In the early stages, it retains token pairs with high similarity, allowing the model to learn simpler patterns. As training progresses, it prunes increasingly similar tokens, enhancing the learning challenge. This design, inspired by the concept of “curriculum learning”, helps improve the model’s understanding of complex features.

### Weaknesses
I believe this paper has some interesting ideas on self-supervised token pruning.
As far as I know, the current SoTA is: Multi-criteria Token Fusion with One-step-ahead Attention for Efficient Vision Transformers, CVPR2024.

However, the performance is still inferior to the supervised token pruning.
And the proposed method requires many additional computation steps.

1. In Section 3.2, “Applying Existing Token Pruning Approach to SSL,” the authors note that SSL accuracy drops significantly when traditional self-attention pruning methods are applied. The experiments reveal that SSL is highly sensitive to token pruning; even slight over-pruning leads to substantial accuracy loss compared to supervised learning (pp. 5-6).

This sensitivity arises because SSL relies more heavily on feature consistency than supervised learning, making it vulnerable to inappropriate pruning. To avoid compromising model performance, SimPrune requires precise tuning of hyperparameters like pruning ratios and retention rates.


2. In Section 4.2, “Difficulty-Aware Pruning Strategy,” the authors propose a pruning approach that gradually increases in difficulty throughout training. Initially, token pairs with high similarity are retained, but as training progresses, more similar tokens are pruned (p. 6).

SimPrune’s design, which progressively raises training difficulty, challenges the model to handle increasingly complex features in later stages. If the model struggles to adapt to this increased difficulty, it may experience fluctuations or even declines in accuracy.


3. In Section 4.1, “Leveraging Cross-Branch Similarity for Token Pruning,” the authors explain that SimPrune involves calculating cross-branch similarities by matching tokens using cosine similarity to establish token pairs across branches (pp. 5-6).

SimPrune’s requirement for cross-branch similarity calculations introduces additional cosine similarity computations. While this overhead is minor relative to the overall computational cost, it can increase total runtime in resource-constrained environments.


4. In Section 4, “SimPrune Design,” the authors highlight that SimPrune includes key parameters, such as the “token keep rate,” which significantly affect final accuracy (p. 6).

SimPrune’s performance is highly sensitive to parameters like token retention rates and pruning stages, requiring careful adjustment based on the dataset and training setup. This need for customization adds complexity to implementation.


5. In Section 3.2, the authors note that traditional pruning methods do not ensure semantic consistency across branches, potentially resulting in a loss of cross-branch semantic information (p. 5).

While SimPrune seeks to maintain semantic consistency through cross-branch pruning, low precision in token matching may still cause semantic inconsistencies between branches, which can negatively impact model performance.


6. In Section 5.3, “Compatibility of SimPrune with Other Efficient SSL Methods,” the authors observe that SimPrune demands high computational resources in the early stages due to extensive token matching and pruning operations needed to maintain semantic consistency (pp. 8-9).

During initial training, SimPrune’s intensive token matching and pruning calculations lead to high resource demands. While these requirements lessen in later stages, the early computational load may pose challenges for resource-limited devices or environments.

### Questions
Please see weakness comments and I would like to see the author's response if I have interpreted these correctly.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper first conduct a preliminary study to analyze the effectiveness of conventional single-branch token pruning on dual-branch self-supervised learning (SSL) for vision transformers. Then, the authors propose SimPrune, which utilizes cross-branch similarity to guide token pruning and introduce a difficulty-aware pruning strategy to further enhance the approach. Experimental results demonstrate the effectiveness of the proposed SimPrune.

### Strengths
1. This paper is well-written. The insights, methodology and experimental results are introduced very clearly.
2. The preliminary study of the effectiveness of conventional single-branch token pruning on dual-branch SSL can provide some valuable insights for researchers in this field.
3. The proposed approach SimPrune seems to be somewhat novel.
4. The experimental results demonstrate the effectiveness of SimPrune on image classification tasks.

### Weaknesses
1. The related work section is incomplete. There are other works, such as BeiT [1], MAE [2], and SimMIM [3], which also claim to be performing SSL for vision transformers. Although these are not dual-branch methods, the relationship between these methods and the proposed SimPrune should be clarified. For instance, it should be discussed whether dual-branch SSL approaches are better than MIM-based ones (e.g., on accuracy, speed or training costs), thereby highlighting the significance of this work's contribution.
2. The experiment section is incomplete. This paper only evaluates the effectiveness of SimPrune on image classification tasks. However, in classification tasks, local features may not be critical, which is quite different from other dense tasks like object detection and image segmentation. The effectiveness of this token-pruning based approach should be further evaluated on those tasks (e.g., COCO, ADE20K, etc) to demonstrate the significance.
3. The significance of this work is not very clear. It seems that saving such training costs of performing dual-branch SSL for these small models is not critical in this field, but the effectiveness on large models is not verified yet.

I will pay more attention to the first two concerns since the third one is not actionable in a short time.

[1] Bao, Hangbo, Li Dong, Songhao Piao, and Furu Wei. "BEiT: BERT Pre-Training of Image Transformers,” In ICLR, 2022. \
[2] He, Kaiming, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. "Masked autoencoders are scalable vision learners." In CVPR, 2022. \
[3] Xie, Zhenda, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin Bao, Zhuliang Yao, Qi Dai, and Han Hu. "Simmim: A simple framework for masked image modeling." In CVPR, 2022.

### Questions
1. The proposed similarity-based token pair pruning approach seems to be a little complicated due to many-to-one issue. Have you tried some other methods like bipartite matching?
2. Is “24% savings in training costs” significant enough? It seems that the other pruning based methods mentioned in this paper can save about 30%-40% costs.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper first analyzes the effectiveness of conventional single-branch token pruning frameworks on SSL and reveals these methods fail to efficiently prune tokens for SSL approaches. To alleviate this issue, this paper proposes to guide token pruning based on cross-branch similarity. Besides, a difficulty-aware pruning strategy is introduced to control the difficulty of the training process. Experiments are conducted to verify the effectiveness of the proposed method.

### Strengths
1. The motivation is clear. The finding that existing token pruning strategies fail to enhance SSL efficiencies is interesting. It is reasonable to prune the pair tokens from two branches based on the cross-branch similarities in the SSL paradigm. 

2. The conducted experiments and visualizations are extensive and well-organized.

3. The paper is well-written and easy to understand.

### Weaknesses
1. Some important references about token pruning are missing: 
[1] Not all images are worth 16x16 words: Dynamic transformers for efficient image recognition, NeurIPS 2021.
[2] Patch slimming for efficient vision transformers, CVPR 2022. 
[3] Self-slimmed vision transformer, ECCV 2022.

2. The downstream tasks, such as object detection and semantic segmentation, are widely adopted to verify the effectiveness of SSL methods (e.g., MAE and ViTDet). Could you present some finetuning results on downstream tasks?

3. Given that some layers of the ViT only observe a subset of tokens during SSL training due to token pruning, a potential discrepancy arises: downstream tasks typically utilize all tokens. Does this inconsistency decrease the downstream performance of SSL-trained models?

4. What's the sliding window size in your experiments?

5. This paper utilizes a dynamic pruning strategy. The visualizations shown in Figure 4 are static. Could you provide additional visualizations, statistics, or other observations illustrating how the pruning patterns change over time?

### Questions
Please see the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce SimPrune, a novel token pruning strategy designed for ViTs in SSL. SimPrune leverages cross-branch similarity information to efficiently prune tokens, retaining essential semantic information across dual branches.

### Strengths
* The method is easy to understand.

### Weaknesses
1. Why are the results in the article so different from the official results? In the Table1, the authors use DeiT-Small as the encoder and
use ImageNet dataset to do the self-supervised training. The performance of DINO is 57.16 without pruning. But according to the [official DINO paper](https://arxiv.org/pdf/2104.14294v2), it achieves 77.0 with a ViT-S backbone. The fact that the results in this paper are so different from those in other articles makes it difficult to compare the methods in this paper to other work, so I'm curious as to what differences in setups lead to such differences.
2. Many SSL methods outperform the DINO used in this paper, such as DINOv2/MIM-Refiner/Unicom, and there are already many methods that can boost up the vision transformer without training, such as [Expediting ViT](https://openreview.net/pdf?id=9ND8fMUzOAr). So the question is, if the task is boosting up the self-supervised training process, a better framework(DINOv2/MIM-Refiner/Unicom) with a smaller backbone may be a better choice; if the task is getting a faster model, choosing a better framework then apply the prune method without finetuning, or just use a smaller network may be the better solutions. Unless the method of this paper can be shown to be effective and better than methods such as Expediting ViT on the latest self-supervised frameworks, it is difficult for me to think of where the superiority of the method of this paper lies.

### Questions
1. Why the performance gap exists?
2. Does the proposed method works on the latest SSL framework and achieves the competitive results?

### Soundness
2

### Presentation
2

### Contribution
2
