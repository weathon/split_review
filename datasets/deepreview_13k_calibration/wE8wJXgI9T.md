# It's Not a Modality Gap: Characterizing and Addressing the Contrastive Gap

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
Learning jointly from images and texts using contrastive pre-training has emerged as an effective method to train large-scale models with a strong grasp of semantic image concepts. For instance, CLIP, pre-trained on a large corpus of web data, excels in tasks like zero-shot image classification, object detection, geolocalization, and more. These contrastive models embed input images and texts into a shared representational space. Recently, it was claimed that models like CLIP show a *modality gap*, where image and text embeddings occupy disjoint areas in the representational space. Previous studies attribute this gap to factors like data artifacts (mismatched pairs), model architecture artifacts (the cone effect), and the nature of the loss landscape (getting stuck in local minima). We demonstrate that, even after accounting for these factors, and even when using the *same modality*, the contrastive loss actually *creates* a gap during training. As a result, we propose renaming this phenomenon the *contrastive gap*. We show that the contrastive gap is exacerbated by training with small batch sizes in high-dimensional spaces, causing embeddings of each modality to occupy small disjoint portions of the latent space. Our experiments show that minimizing the contrastive gap via the addition of uniformity and alignment terms optimizes the representational space and conveys better performance on downstream tasks such as zero-shot image classification and multi-modal arithmetic.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
An empirical study on the impact of several loss functions on the CLIP embedding space has been presented in this work. The experiment tries to investigate the modality gap between images and text in retrieval and classification tasks.

### Strengths
- A comprehensive loss analysis and introduction have been provided for the CLIP embedding space. 
- The experiment is well-designed to demonstrate the *contrastive gap* in terms of several gap metrics and utility (e.g., retrieval accuracy).

### Weaknesses
 - **Unclear Definition**: The proposed *contrastive gap* lies at the core of this work; however, it has never been defined clearly. While an intuitive example on the "idealized" dataset was given to demonstrate the concept, the setting of this example is less convincing (see the detailed comments below), and a clear, formal definition for the contrastive gap is still lacking. 
- **Contrastive Gap v.s. Margin**: The experiment settings of `Table 1` and `Section 3.2` are unconvincing in investigating the modality gap and somewhat confused with the margin in a single image modality. As shown in Eq (2), the CLIP contrastive loss may work as a triplet loss to push the margin between positive and negative pairs. Thus, by using the same modality on both encoders, the learned contrastive gap is more like a margin among different samples instead of showing the modality gap. 
- **Lack of Technical Novelty**: The key contribution of this work is relatively marginal. First, the proposed contrastive gap lacks insightful theoretical evidence and guarantees. Second, the proposed mitigation strategies all build on top of existing works. 
- **Experiments**: While the new proposed fine-tuning loss shows some improvements, the CLIP embeddings badly degrade in retrieval, raising a severe concern about the utility of closing the "contrastive gap".

### Questions
- What's the formal definition of a contrastive gap? 
- Is there any theoretical guarantee that closing the contrastive gap can bridge the modality gap?
- What's the difference between a contrastive gap and a margin? 
- Can the proposed loss improve other common tasks, such as image captioning and text2image retrieval?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper analyzes the contrastive gap, a phenomenon previously referred to as the modality gap in existing research. The authors make two main observations: (1) they demonstrate that this gap also occurs within the same modality, prompting a shift in terminology from "modality gap" to "contrastive gap," and (2) they show that small batch sizes in high-dimensional spaces are particularly susceptible to the contrastive gap. After characterizing the contrastive gap through the use of uniformity and alignment losses, the authors illustrate that addressing this gap can benefit certain downstream tasks. However, it is worth noting that all experiments are conducted in a small-scale fine-tuning setting, which differs significantly from real-world, large-scale pre-training environments. Additionally, while the authors claim benefits for downstream tasks, these results appear limited to a narrow set of tasks, such as classification.

### Strengths
1. The paper is well-written and easy to follow.
2. Although the experiment is conducted on a small scale and with restricted fine-tuning areas, the finding that a gap also arises within the same modality is significant and could impact a broad range of applications.
3. The analysis of the rationale behind how contrastive loss induces a gap is clear and reasonable.

### Weaknesses
1. Most experiments are conducted on a small-scale training dataset within a fine-tuning setup, which differs significantly from real-world setting. Additionally, the batch size and dimensionality are also limited to a small-scale setting, raising concerns about the applicability of these results to large-scale contexts. Ideally, additional experiments in a more realistic, large-scale setting would strengthen the findings.
2. The proposed method closely resembles existing work (e.g., Al-jaff, 2023), with the primary difference being the inclusion of cross-modal uniformity. This similarity raises questions about the extent of the methodological contribution.
3. While the authors claim that bridging the contrastive similarity gap benefits representation learning, the results in cross-modal retrieval do not demonstrate significant performance improvements, which is concerning. Although the authors argue that their method captures meaningful concepts, the discussions and experiments provided are insufficient to convincingly support this claim. 

The examples in Figure 9 appear to be cases of false negatives, a well-known issue in MS-COCO. Evaluating the proposed method on ECCV-caption[1], which addresses false negatives and uses a more robust metric, such as MaP, could provide a stronger demonstration of its effectiveness.

### Questions
Refer to the weakness section

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the phenomenon known as the "modality gap" in multi-modal contrastive learning models like CLIP. The authors propose renaming it to "contrastive gap," arguing that this gap emerges as a consequence of contrastive training rather than modality differences. They demonstrate that the gap persists even when controlling for previously suspected causes and show that it is exacerbated by small batch sizes in high-dimensional spaces. The paper proposes adding uniformity and alignment terms to the CLIP loss to reduce this gap and evaluates the impact on various downstream tasks.

### Strengths
- The paper provides a comprehensive empirical analysis of how dimensionality and batch size affect the contrastive gap, offering insights into why this phenomenon occurs in multi-modal models.
- The experiments are extensive, covering multiple evaluation metrics and downstream tasks, including zero-shot classification, retrieval, and multi-modal arithmetic.
- The proposed solution of adding uniformity and alignment terms is relatively simple to implement and shows some improvements in certain tasks.

### Weaknesses
## Major Weaknesses
1. Fundamental Misunderstanding of CLIP:
    - The paper incorrectly attributes CLIP's loss function to SimCLR's NT-Xent loss, when CLIP actually builds upon multi-class N-pair loss[^1]
    - This misunderstanding undermines the paper's theoretical foundation and technical credibility
2. Experimental Validity
    - Absence of crucial baselines: no comparison with untuned CLIP or from-scratch training
    - All fine-tuning methods appear to degrade the original CLIP's performance
    - The generalization from 3D to high-dimensional spaces lacks proper justification
3. Theoretical Framework
    - Misinterpretation of Wang & Isola (2020)[^2], incorrectly claiming uniformity and alignment as "desirable properties"
    - Insufficient justification for renaming "modality gap" to "contrastive gap"
    - Lack of causal analysis between gap reduction and performance improvement

## Minor Weaknesses
1. Experimental Design Choices:
    - Using identical images as positive pairs without proper justification
    - Arbitrary selection of only the first caption from MS COCO's five captions
    - Missing comparison with previous modality gap solutions (e.g., Liang et al. 2022[^3])
2. Result Analysis:
    - Inadequate explanation for contradictory results between retrieval and zero-shot classification tasks
    - Insufficient discussion of task-specific performance variations
    - Limited analysis of the trade-offs introduced by the proposed loss terms

### Questions
1. Could you explain why using identical images as positive pairs in your controlled experiment provides meaningful insights about the real-world scenario where modalities are genuinely different?
2. Your experiments show performance degradation in retrieval tasks but improvement in zero-shot classification. How do you reconcile these contradictory results with your claim that reducing the contrastive gap generally improves representation quality?
3. Have you conducted experiments comparing your method with the original CLIP model (without fine-tuning) and with models trained from scratch using your proposed loss functions? This would help establish the true effectiveness of your approach.
4. Given that the original paper showing the modality gap (Liang et al. 2022[^1]) demonstrated that the optimal gap size is task-dependent, how do you justify the claim that uniformly reducing the gap is beneficial?

[^1]: Liang, Victor Weixin, et al. "Mind the gap: Understanding the modality gap in multi-modal contrastive representation learning." Advances in Neural Information Processing Systems 35 (2022): 17612-17625.

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
5

### Summary
This paper explores the problem of modality gap in contrastive pre-trained models such as CLIP. This paper shows experimentally that the contrastive loss itself can also introduce gaps during training. This contrastive gap is particularly pronounced when training with small batches in high-dimensional spaces. To address this problem, this paper proposes a method to minimize the contrastive gap by adding uniformity and alignment terms. Experimental results show that this approach can optimize the representation space and achieve better performance in downstream tasks such as zero-shot image classification and multimodal arithmetic.

### Strengths
- Simple experiments prove the motivation.
- The paper is clearly written and the method can be well understood.

### Weaknesses
 - Alignment and Uniformity are properties often mentioned in the CLIP model, and the innovation of Section 4 seems to be limited.

- The experimental results of Figure 4 and Figure 5 are completely different. So is the poor image retrieval result related to the dataset? If we use categories as text for retrieval on datasets such as CIFAR-10, the retrieval conclusion will be similar to the conclusion in Figure 5.


### Questions
- In Figure 1, why is the accuracy only 0.1 in the first 150 epochs, and then quickly increases to 0.87? This phenomenon seems a bit abnormal. Can you explain the reason?


- Why does increasing batch size and s_max reduce the contrast gap?

### Soundness
3

### Presentation
3

### Contribution
3
