# Learning to Adapt Frozen CLIP for Few-Shot Test-Time Domain Adaptation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Few-shot Test-Time Domain Adaptation focuses on adapting a model at test time to a specific domain using only a few unlabeled examples, addressing domain shift. Prior methods leverage CLIP's strong out-of-distribution (OOD) abilities by generating domain-specific prompts to guide its generalized, frozen features. However, since downstream datasets are not explicitly seen by CLIP, solely depending on the feature space knowledge is constrained by CLIP's prior knowledge. Notably, when using a less robust backbone like ViT-B/16, performance significantly drops on challenging real-world benchmarks. Departing from the state-of-the-art of inheriting the intrinsic OOD capability of CLIP, this work introduces learning directly on the input space to complement the dataset-specific knowledge for frozen CLIP. Specifically, an independent side branch is attached in parallel with CLIP and enforced to learn exclusive knowledge via revert attention.  To better capture the dataset-specific label semantics for downstream adaptation, we propose to enhance the inter-dispersion among text features via greedy text ensemble and refinement. The text and visual features are then progressively fused in a domain-aware manner by a generated domain prompt to adapt toward a specific domain. Extensive experiments show our method's superiority on 5 large-scale benchmarks (WILDS and DomainNet), notably improving over smaller networks like ViT-B/16 with gains of \textbf{+5.1} in F1 for iWildCam and \textbf{+3.1\%} in WC Acc for FMoW.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach for few-shot test-time domain adaptation (FSTT-DA) by learning to adapt frozen CLIP models to specific domains using only a few unlabeled examples. The method leverages strong CLIP`s OOD abilities and further learns on the input space to complement CLIP's generalized features with dataset-specific knowledge. Additionally, it enhances text features through a greedy ensemble strategy and proposes a domain-aware fusion approach for adapting both text and visual features toward a target domain.

### Strengths
1. The overall writing is good and clear.
2. Promising results are obtained in the studied benchmarks. 
3. Comprehensive evaluations are conducted, and the effectiveness of the proposed modules is also shown.

### Weaknesses
Novelty is somewhat limited.  I appreciate the proposed method improved the base CDPG obviously and the proposed method (as in Fig.2) also includes many submodules. However, except for the greedy text ensemble strategy, the techniques used in the submodels e.g., domain prompt, and cross-attention-based fusion all look not new.



### Questions
1. what are the additional number of parameters and computation costs?
2. In Lines 510-511, the paper mentions that compared to previous work external constraints are not used. I am curious why these losses are not used. Will the results become worse when using them?
3.	How does the similarity between the target domain and the source domain affect the method?
2.	In Fig. 4, for some datasets, the increasing number of layers (parameters) of CPNet can not bring further improvement in accuracy but makes the accuracy lower.  What is the reason behind this? 
5.   Open question: why the FSTT-DA task with few-shot unlabeled data is selected as the testbed, what about the few-shot labeled data but also with the cross-domain (CD-FSL) [ref1,2,3] setting?  To me, the unlabeled and small labeled data don't come together quite often.  

[ref1]  A Broader Study of Cross-Domain Few-Shot Learning
[ref2] Cross-Domain Few-Shot Classification via Adversarial Task Augmentation
[ref3] StyleAdv: Meta Style Adversarial Training for Cross-Domain Few-Shot Learning

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To address the Few-shot Test-Time Domain Adaptation task, this paper proposes a new method named L2C. 

Compared to previous work, L2C adds an input-space learning branch to the frozen CLIP model, overcoming limitations associated with relying solely on CLIP’s feature space. It introduces a greedy text ensemble and domain-aware fusion, enhancing the model's ability to capture dataset-specific semantics.

Extensive experiments on five large-scale benchmarks demonstrate performance improvements, particularly with less robust backbones like ViT-B/16.

### Strengths
1. The research task Few-shot Test-Time Domain Adaptation seems practical and meaningful.

2. With less robust backbones like ViT-B/16, the proposed method L2C shows significant performance improvement.

### Weaknesses
I have some questions about this paper that need further discussion. Please see them below.

## Performance
1. As the author mentioned, the proposed L2C shows better performance with the CLIP ViT-B model, but the performance improvement on the CLIP ViT-L model is limited. Therefore, I would like to know if the proposed L2C method is mainly effective for smaller or "not well-trained" models, and whether L2C might become less effective as models and data scale up.

## Setting
To be honest, Few-shot Test-Time Adaptation (FSTTA) is a new field, so I may have some questions about the settings that I'd like to discuss with the authors.

1. In the traditional TTA setting, once the model is trained on the source domain, most existing works, like TENT [1], make minimal or no changes to the pretrained model, focusing instead on designing methods for the inference stage. However, the L2C method modifies the training process on the source domain (Figure 2). I'm not certain if this approach is permitted.

2. The figure7 shows that the FSTT-DA setting has several target domain, does the FSTTA will occur the catastrophic forgetting like CTTA setting? (CoTTA [2])

3. This method uses prompt guidance and includes multiple domains, which reminds me of PODA [3] and ULDA [4]. I hope the authors can discuss or compare these methods in the paper to enhance its completeness.

## Method
1. As shown in Figure 1, can I understand that, compared to VDPG, L2C introduces a new trainable network to learn more domain-specific knowledge? If so, is the performance comparison fair, given that L2C has more trainable parameters and a larger overall network?

### Questions
I want to disccuss with authors:
## Performance
1. As the author mentioned, the proposed L2C shows better performance with the CLIP ViT-B model, but the performance improvement on the CLIP ViT-L model is limited. Therefore, I would like to know if the proposed L2C method is mainly effective for smaller or "not well-trained" models, and whether L2C might become less effective as models and data scale up.

## Setting
To be honest, Few-shot Test-Time Adaptation (FSTTA) is a new field, so I may have some questions about the settings that I'd like to discuss with the authors.

1. In the traditional TTA setting, once the model is trained on the source domain, most existing works, like TENT [1], make minimal or no changes to the pretrained model, focusing instead on designing methods for the inference stage. However, the L2C method modifies the training process on the source domain (Figure 2). I'm not certain if this approach is permitted.

2. The figure7 shows that the FSTT-DA setting has several target domain, does the FSTTA will occur the catastrophic forgetting like CTTA setting? (CoTTA [2])

3. This method uses prompt guidance and includes multiple domains, which reminds me of PODA [3] and ULDA [4]. I hope the authors can discuss or compare these methods in the paper to enhance its completeness.

## Method
1. As shown in Figure 1, can I understand that, compared to VDPG, L2C introduces a new trainable network to learn more domain-specific knowledge? If so, is the performance comparison fair, given that L2C has more trainable parameters and a larger overall network?

[1] Tent: Fully Test-time Adaptation by Entropy Minimization

[2] Continual Test-Time Domain Adaptation 

[3] PØDA: Prompt-driven Zero-shot Domain Adaptation

[4] Unified Language-driven Zero-shot Domain Adaptation

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new test-time CLIP adaptation method that learns domain-specific knowledge complementary to CLIP’s general knowledge. A parallel CPNet is introduced to achieve this by revert attention from CLIP image encoder. A domain prompt is proposed for domain-aware fusion between text and visual features. The experimental results demonstrate the effectiveness of the proposed method on several benchmarks.

### Strengths
1. The experimental results show the improvement over state-of-the-art methods.
2. This paper is well written and follows a good structure.
3. The supplementary material is extensive, offering a lot of supplements and support to the main text.

### Weaknesses
1. The motivation behind the proposed method is not clearly explained.  As shown in Figure 1, The method is organized in two branches, fusing domain prompt and complementing dataset-specific knowledge. However, these two branches seem to have very similar functions,  i.e.,  incorporating domain-specific knowledge, which makes the whole pipeline seem redundant. Specifically, it is unclear why a separate CPNet is needed to complement CLIP features when a domain prompt is already being used to adapt the text embeddings. The paper does not sufficiently justify the necessity of having two distinct mechanisms for injecting domain-specific information, and the potential overlap in their functionality raises concerns about the method's efficiency and conceptual clarity.

2. As shown in experiments, it seems that CPNet plays an important role. However, it is not clear that whether the improvement is due to the incorporation of domain knowledge or the addition of extra network parameters. The paper lacks a detailed analysis of the contribution of the CPNet, making it difficult to ascertain if the performance gains are genuinely due to domain adaptation or simply a result of increased model capacity. A more rigorous ablation study is needed to isolate the effects of the CPNet and rule out the possibility that the improvements are merely due to the introduction of additional learnable parameters.

3. Some relevant prompt-based works exploring domain knowledge for mitigating domain shift is not discussed, e.g., HybridPrompt[1], Pro[2].
    
    [1] Wu et al., HybridPrompt: Domain-Aware Prompting for Cross-Domain Few-Shot Learning

    [2] Ma et al., ProD: Prompting-to-disentangle Domain Knowledge for Cross-domain Few-shot Image Classification

### Questions
1. The introduced modules to refine text prompt, i.e., M_c and M_d are not ablatively evaluated. Can you provide ablation study about this?
2. In Table 3, the performance declines across most of indicators when domain-aware fusion is applied. Why would learning in a domain-aware manner lead to weaker performance?
3. What is the impact of unlabeled samples when learning the target domain prompt? It is advisable to conduct sensitivity analysis of number of samples.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces "Learning to Complement" (L2C) for Few-shot Test-Time Domain Adaptation, addressing domain shift with minimal unlabeled data. The method adds a parallel module, CPNet, to learn dataset-specific knowledge and complement CLIP’s frozen features. A greedy text ensemble strategy enhances text feature discrimination, improving adaptation by reducing domain bias. The fused text and visual features are guided by domain-specific prompts, leading to superior performance on five benchmarks, especially with smaller backbones like ViT-B/16.

### Strengths
*	The organization of this paper is well-structured, making it easy to read and comprehend.

*	The insight of learning dataset-specific knowledge is convincing and effective, making a significant contribution to the FSTT-DA community.

*	Experimental results are impressive, the proposed methods got SOTA in all proposed benchmarks.

*	Overall, the quality of the paper is commendable. The authors have conducted a thorough ablation study to examine the impact of various components.

### Weaknesses
 * In Section 4.2, although the authors highlight the improvement of the text dispersion strategy compared to [a], and demonstrate the effectiveness of the greedy text ensemble strategy for FSTT-DA, the advantages of these improvements over previous methods are not sufficiently discussed.

* The authors did not provide comparisons on the PACS dataset. Extra experiments on smaller datasets could further demonstrate the flexibility of the proposed method.

* While the paper makes significant progress compared to VDPG and achieves SOTA performance, the authors do not analyze the challenges of FSTT-DA tasks, nor do they provide a discussion on how these challenges are addressed.

### Questions
*	The idea of this work is interesting and effective in FSTT-DA scenario, can the authors provide the source code to facilitate reproduction?

*	In line 202, the authors mention that CPNet is introduced to acquire data-specific visual knowledge. However, throughout the paper, CPNet appears to learn dataset-specific knowledge. Could the authors clarify the difference between data-specific visual knowledge and dataset-specific knowledge?

---

I am open to discussing these points with the authors during the response period. If the concerns and questions are adequately addressed, I will consider raising my score.

### Soundness
3

### Presentation
3

### Contribution
3
