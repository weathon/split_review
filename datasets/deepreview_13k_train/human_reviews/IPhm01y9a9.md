# Window Attention is Bugged: How not to Interpolate Position Embeddings

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-0.7em}
Window attention, position embeddings, and high resolution finetuning are core concepts in the modern transformer era of computer vision. However, we find that na\"ively combining these near ubiquitous components can have a detrimental effect on performance.
The issue is simple: interpolating position embeddings while using window attention is \textit{wrong}. We study two state-of-the-art methods that have these three components, namely Hiera and ViTDet, and find that both do indeed suffer from this bug. To fix it, we introduce a simple absolute window position embedding strategy, which solves the bug outright in Hiera and allows us to increase both speed and performance of the model in ViTDet. We finally combine the two to obtain HieraDet, which achieves 61.7 box mAP on COCO, making it state-of-the-art for models that only use ImageNet-1k pretraining. This all stems from what is essentially a 3 line bug fix, which we name ``absolute win''.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper identifies an issue that arises when using absolute position embeddings with windowed attention in vision transformers. The key points are:

- Many vision transformers use both absolute position embeddings and windowed attention for efficiency. However, naively interpolating the position embeddings when finetuning on larger image sizes misaligns them with the window partitions. 

- This causes significant performance degradation when finetuning on larger images, which the paper demonstrates on Hiera and ViTDet models.

- To fix this, the authors propose "absolute win" embeddings, which separately learn an interpolated global position embedding and a tiled window position embedding. This aligns the embeddings with window attention properly.

- Applying absolute win embeddings improves performance substantially in Hiera and ViTDet across tasks like image classification, object detection, video action recognition.

- With the fix, Hiera and ViTDet establish new state-of-the-art results on COCO and other datasets using only ImageNet-1K pretraining, while also being faster due to reduced need for relative position biases.

- The paper provides practical guidelines for using absolute position embeddings with windowed attention when finetuning vision transformers at higher resolutions.

The key contribution is identifying and fixing a bug that improves SOTA vision transformers. The fix is simple but impactful - just changing the position embeddings.

### Strengths
The authors identify an important yet overlooked interaction between commonly used components in vision transformers - window attention and absolute position embeddings. When naively combined and interpolated for high-resolution finetuning, they show this leads to degraded performance.

The key novelty is in formally characterizing and providing strong empirical evidence for this bug. While simple in retrospect, it is a creative insight to recognize that the position embeddings effectively "tile" based on the window size due to the weight sharing in attention. The visualizations and analysis of the learned embeddings clearly demonstrate this phenomenon.

Fixing the bug is also quite elegant - simply embrace the tiling behavior with "absolute win" position embeddings. This simple change allows models to properly interpolate and achieves significantly improved performance across various vision tasks.

The paper is very clearly written and easy to follow. The introduction motivates the problem well, and the methodology is laid out in a structured manner. Experiments comprehensively ablate the impact of the bug fix on state-of-the-art methods.

Overall, this is a significant finding - identifying and correcting an important issue affecting a large class of vision transformer models. The clarity and thoroughness of the empirical validation make a compelling case for the prevalence and implications of this bug.

### Weaknesses
 * The proposed fix of "absolute win" embeddings is intuitive, but the paper does not provide much analysis into why tiling the window embeddings specifically works better than other potential solutions. Some ablation studies on the design choices could add more clarity. For instance, it's not clear why simply learning a separate embedding for each window position is superior to other possible parameterizations, such as a convolutional approach or a learned function of the window coordinates. The paper should explore the sensitivity of the results to different window embedding parameterizations.
* The simplicity of the proposed fix somewhat limits the depth of technical novelty and contribution. Providing more design motivation and analysis for "absolute win" would strengthen this aspect. While the empirical results are compelling, the paper could benefit from a deeper dive into the underlying mechanisms that make the proposed approach effective. A more detailed analysis of the learned embeddings and their interaction with the attention mechanism would be valuable.
* Tiling the window position embeddings makes sense based on the observed tiling behavior, but other arrangements could also resolve the misalignment issue when interpolating. The design space is not explored in depth. For example, the paper could investigate whether a learned interpolation scheme for the position embeddings, rather than a direct tiling, could achieve similar or better results. The current approach assumes a rigid tiling structure, which might not be optimal for all scenarios. Exploring alternative interpolation techniques could reveal more nuanced insights.
* While shown to work empirically, the approach lacks theoretical analysis into why tiling embeddings avoids the misalignment issue during interpolation. A more formal understanding could improve the method. Specifically, a mathematical analysis of how the interpolation of absolute position embeddings interacts with windowed attention, and how the proposed tiling resolves this interaction, would significantly strengthen the theoretical underpinnings of the work. This could involve analyzing the gradients or the effective receptive fields of the attention mechanism under different position embedding schemes.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors discuss the challenges faced when combining window attention, position embeddings, and high-resolution finetuning in the modern transformer era of computer vision. They identify a bug that arises when interpolating position embeddings while using window attention. Two state-of-the-art methods, Hiera and ViTDet, are found to be affected by this bug. To address this, the authors introduce an "absolute window position embedding strategy" which rectifies the issue in Hiera and enhances the speed and performance of ViTDet.

### Strengths
In-depth Analysis: The paper provides a comprehensive analysis of the problem, identifying the root cause of the issue with window attention and position embeddings.

Solution-Oriented: The authors not only identify the problem but also propose a solution in the form of an "absolute window position embedding strategy".

Empirical Evidence: The paper presents empirical results, showcasing the effectiveness of their proposed solution, especially with the HieraDet model's performance on COCO.

Relevance: The topic is highly relevant given the prominence of transformer architectures in computer vision.

### Weaknesses
Limited Scope: The study primarily focuses on two methods, Hiera and ViTDet. Expanding the scope to include more methods might provide a broader understanding of the issue.

Assumption-based: Some conclusions, especially regarding the behavior of position embeddings, seem to be based on observations and assumptions. More rigorous testing might solidify these claims.

Furthermore, the paper's contribution appears to be limited. It primarily addresses a minor bug in Hiera and ViTDET. The resulting improvements, while noteworthy, are not substantial, suggesting that the issue wasn't fundamental. Nonetheless, I appreciate the effort and contribution of this work

### Questions
Please see above.

### Soundness
3 good

### Presentation
4 excellent

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
This paper identifies and fixes a bug that occurs when using both window attention and absolute position embeddings in vision transformers. The authors show that naively interpolating absolute position embeddings when finetuning on larger image sizes misaligns the embeddings with the window attention, hurting performance.

The bug is analyzed in detail using Hiera and ViTDet as case studies. Hiera learns repetitive absolute position embeddings aligned with its window attention during pretraining. Interpolating these embeddings when finetuning on larger images misaligns them, causing a drop in accuracy.

ViTDet suffers from a similar issue - it uses interpolated absolute position embeddings with added window attention, which provides each window only a sliced portion of the full embedding.

To fix the bug, the authors propose "absolute win" - embedding strategies that align position embeddings with window attention after interpolation. This involves learning separate window and global position embeddings.

On Hiera, absolute win embeddings fix the bug and achieve strong image classification accuracy when finetuning on larger resolutions. The embeddings also enable removing most relative position embeddings from ViTDet while increasing performance.

The authors then apply absolute win to create HieraDet for detection, outperforming ViTDet by 1.5+ box AP on COCO using only ImageNet pretraining.

### Strengths
- Identifies and clearly analyzes an important bug in modern vision transformers
- Proposes a simple and effective solution - "absolute win" position embeddings
- Achieves SOTA detection performance with HieraDet using only ImageNet-1k pretraining
- Improves performance across multiple architectures (Hiera, ViTDet) and tasks

### Weaknesses
 - The gains from fixing this bug seem somewhat task/architecture dependent (smaller gains on ViTDet).
- Unclear if the bug manifests in other architectures with window attention and absolute embeddings.
- Does not explore more powerful global position embedding strategies for ViTDet.

### Questions
Does relative position encoding exhibit similar phenomena as absolute position encoding?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a new problem that there could be a misalignment in the learned position embedding when fine-tuning a model at a higher resolution, the model is composed of both window-attention and absolute position embedding. The solution is to applied separate embeddings for window and global position. The proposed separate position embedding can improve the suffered models, Hiera and ViTDet for classification and object detection respectively.

### Strengths
Position embedding is widely used in modern Transformer-based vision architectures. This paper aims at studying important questions on position embedding, and attention-mechanism. The draft is well-written and organized, the proposed method is clearly demonstrated.

### Weaknesses
The paper is well-presented, but some issues could be further discussed or studied to avoid misleading. A list of questions is shown below, a short summary for the weaknesses is:  1. The whole idea is based on the visualization of the position embedding, but if the visualization can represent position information is a question, I hope the draft can further explain this question to make the draft clear. 2. The proposed method utilizes the "bug" of the learned window position embedding, which raises a question of if the learned embedding is a bug.
This draft could be summarized as HieraV2 which uses both global and window position embedding based on the feature in Hiera.



### Questions
There exist weaknesses in the current draft, which should be discussed further before publication.

1. The motivation: 
The whole problem(bug) is found and discussed based on the "learned" feature embedding, which is shown in Figs. 1 and 2 in the draft. And this example plays a foundation role in this study, why it is a bug and what the fix is. However, I am trying to figure out why the visualization can be considered position information? This study uses Hiera as an example to showcase the bug, and Hiera is a modified version of MViTv2. I know some of the learned position embedding also goes through or fused with semantic features, so how can one confirm the defined position embedding is really position embedding? Could the learned block also contain semantic feature and could the semantic feature be the reason behind?(Please correct me if I am wrong on Hiera, MViTv2 uses decomposed position). Assuming if it is position embedding, how one confirm the bug is from window-attention + absolute position? Could the learned embedding is the main reason, in another word, what if I use pre-defined absolute position information with window-attention, could the bug still be there?(I guess the performance could drop, but the claim was on exposing the bug.) 

2. The fix:
This study proposes to use separate position embedding for window and global for the bug. This solution could be trivial or the demonstration of the question can be further studied. Hiera is a simplified version of the model, MViTv2, and Hiera replaced relative position with absolute position on purpose because they did not observe differences in their ablation table. Empirically, if mask unit(window-att)+ absolute position could lead to lower performance on higher resolution images, one can simply use relative position as used in original MViTv2. This proposed method can be formulated as combining both window and global position for a slightly higher performance, as shown in Tab 2 in the draft. A further question is that if the method is proposed based on the "bug" not fixing it, is it still a "bug"?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
