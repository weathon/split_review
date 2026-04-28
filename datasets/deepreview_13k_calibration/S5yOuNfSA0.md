# Understanding Transferable Representation Learning and Zero-shot Transfer in CLIP

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Multi-modal learning has become increasingly popular due to its ability to leverage information from different data sources (e.g., text and images) to improve the model performance. Recently, CLIP has emerged as an effective approach that employs vision-language contrastive pretraining to learn joint image and text representations and exhibits remarkable performance in zero-shot learning and text-guided natural image generation. Despite the huge practical success of CLIP, its theoretical understanding 
 remains elusive. In this paper, we formally study transferrable representation learning underlying CLIP and demonstrate how features from different modalities get aligned. We also analyze its zero-shot transfer performance on the downstream tasks. %In addition, we conduct empirical evaluations on real data to back up our theory. 
 Inspired by our analysis, we propose a new CLIP-type approach, which achieves better performance than CLIP and other state-of-the-art methods on benchmark datasets. %Our results provide substantial insights into the mechanisms underlying the transferrable representation learning of CLIP and its application on zero-shot transfer.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates transferable representation learning underlying CLIP and demonstrates how features from different modalities can be aligned. Then a new CLIP-type method is proposed, the effectiveness of the proposed method is proved through experiments on multiple benchmark datasets.

### Strengths
- This paper is well-written and easy to follow. 
- This paper theoretically examines the transferable representation learning in CLIP. The theory seems sound.
- This paper proposes an easy regularization technique for CLIP that can effectively improve its zero-shot performance.

### Weaknesses
My major concerns lie in the empirical studies.
- The current pre-training experiments are all based on the CC3M, which is much smaller than the full 400M dataset used by the CLIP. It is unclear whether the proposed regularization technique holds when extended to a larger dataset. It is recommended to conduct experiments on datasets with different sizes. Specifically, the regularization effect might diminish or even become detrimental when the model is trained on a larger, more diverse dataset, as the regularization might over-constrain the model's capacity to learn complex relationships. The authors should explore how the regularization scales with dataset size.
- In Table 1, why incorporating the regularization term into the contrastive objective is harmful to DTD? The paper should provide a more in-depth analysis of why the regularization term negatively impacts performance on the DTD dataset, given that it improves performance on other datasets. It is important to understand the specific characteristics of the DTD dataset that make it sensitive to this regularization.
- It seems that the results of CyCLIP in Table 1 and Table 2 are inconsistent with the original CyCLIP paper. The discrepancy between the reported results and the original paper raises concerns about the reproducibility of the experiments. The authors should clarify the experimental setup and justify the differences in the reported results.
- Can the proposed regularization technology work in CyCLIP?
- Is the method equally effective for other downstream tasks such as retrieval?

### Questions
Please see weaknesses.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on providing theoretical support for the CLIP training and its zero-shot transferability. The main claim is that the contrastive learning objective in CLIP may not cover all the positive pairs, e.g., some features in an image may not be present in its corresponding captions. In section 3, the authors show that the empirical loss converges to the true loss when the number of batches is large enough. In section 4, they show that the learned similarity score f_hat between negative pairs is smaller than the score between positive pairs given that there exists a score function f* such that this relation holds. Based on such assumption, in section 5, they conclude that a trained CLIP model can achieve small top-r error and this generalizes to different distributions as the distribution shift is bounded. Based on the prior assumption and derivations, they have three claims: 1) Margin depends on the temperature tau, 2) We should only regularize positive pairs instead of both positive and negative pairs, 3) With sufficiently small tau, we can find a f_hat with large margin. They test these claims with experiments on CC3M.

### Strengths
The paper provides theoretical bounds on CLIP training and its zero-shot transferability.

### Weaknesses
1. Contrastive learning has been widely studied in the community with several variants of NCE loss, with different ways to regularize positive and negative pairs to improve the margins (e.g., [a]). The behavior of temperature in contrastive learning was also studied (e.g., [b]), and so was regularization (e.g., [c]). It is not surprising that adding the regularization of the distance between positive pairs can improve the performance. Also, how does the proposed solution compare to those methods?  

2. The authors propose only to regularize the distance between positive pairs, but there is no ablation comparison to the variants that regularize both or negative pairs only.

3. The introduction states that the contrastive learning objective in CLIP may not cover all the positive pairs, which makes sense. However, 
 it is unclear how the proposed solution addresses this issue.

4. The experiments are conducted on a relatively small dataset compared to CLIP. The training behavior and the generalization ability of the representation may be different.  

5. The derivations make sense but they are under several assumptions.

### Questions
My questions are listed in the weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper offers theoretical analysis of the underlying principles of CLIP, shedding light on why CLIP exhibits robust transferability. Additionally, the paper introduces a novel regularization technique designed to enhance the performance of CLIP.

### Strengths
This paper is well-written and novel. This paper offers a robust analysis, including mathematical proofs, of CLIP. These contributions greatly contribute to our understanding of CLIP.

### Weaknesses
1. The paper's primary focus appears to be on CLIP's zero-shot transferability. While this is undoubtedly a significant aspect, it's worth considering that CLIP's robust zero-shot performance results from a strong semantic space based on extensive vision-semantic data. Therefore, an exploration of the visual-semantic alignment aspect, specifically how the learned representations capture the correspondence between visual and textual features, could be an intriguing avenue for further investigation. This would involve analyzing the structure of the joint embedding space and how different modalities are aligned within it.

2. In introduction section, the author cites "blue sky" and "white cloud" as examples of unique features. However, these instances might be seen as special cases.  As CLIP is based on a large amount of vision-semantic data, it's possible that the missing elements could appear in various other captions. Therefore, I question the significance of this problem. To address this concern, the author may need to conduct overall statistics on the data, quantifying the frequency of such missing elements. Furthermore, the term 'unique features' could benefit from a more precise definition or explanation, perhaps in terms of feature importance or information content.

3.  Some notations and definitions in the paper can be challenging to follow. For instance, the terms 'one-to-one mapping' or 'one-to-one matching' could benefit from clearer explanations for readers, including a formal definition of these terms within the context of the paper's analysis. It would be helpful to specify whether this mapping refers to a strict bijection or a more relaxed correspondence.

4. Expanding the range of experiments to include various downstream tasks, rather than solely focusing on zero-shot and Linear probing, would provide a more comprehensive assessment of the paper's proposed methods and their practical applications. For example, evaluating performance on tasks such as image captioning, visual question answering, or object detection would offer a broader view of the model's capabilities and limitations.

### Questions
See `Weakness' above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper theoretically examines transferable representation learning of CLIP. The analysis reveals that with a near-optimal network trained on the data, features from different modalities align, allowing for zero-shot learning when appropriate prompts are used. The paper also demonstrates that contrastive learning with sparse features can lead to unexpected positive pairs, emphasizing the need for careful consideration. Building on these general theoretical findings, the authors provide deeper insights into specific cases, illustrating how multi-modal learning aligns different features and how CLIP's learned features outperform those obtained through naive square loss. To validate their theoretical predictions, the authors conduct experiments on real data. Additionally, inspired by their theoretical findings, they propose a novel regularization technique for CLIP, effectively improving zero-shot performance across various tasks, as confirmed by empirical results.

### Strengths
1. The paper is well-written and flows smoothly, making it relatively easy for readers to understand. 
2. This article focuses on what's behind the explosive effectiveness of CLIP, and the paper attempts to delve into the principles underlying CLIP, demonstrating a certain level of originality and innovation.

### Weaknesses
1. More relevant experimental results are expected, such as results from a wider range of downstream tasks.
2. The article exclusively analyzes and experiments with CLIP, without thoroughly exploring the applicability of this new methods to other relevant contrastive learning approaches.

### Questions
Can one simply replace the CLIP component in all CLIP-related work with CLIP+Reg to achieve a better performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
