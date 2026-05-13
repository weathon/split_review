# RANKCLIP: Ranking-Consistent Language-Image Pretraining

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Self-supervised contrastive learning models, such as CLIP, have set new benchmarks for 
vision-language models in many downstream tasks.
However, their dependency on rigid one-to-one mappings overlooks the complex and often
multifaceted relationships between and within texts and images. 
To this end, we introduce \textbf{\algname}, a novel pretraining method that extends 
beyond the rigid one-to-one matching framework of CLIP and its variants. 
By extending the traditional pair-wise loss to list-wise, and leveraging both in-modal and 
cross-modal ranking consistency, \algname improves the alignment process, enabling it to 
capture the nuanced many-to-many relationships between and within each modality.
Through comprehensive experiments, we demonstrate the effectiveness of \algname in 
various downstream tasks, notably achieving significant gains in zero-shot classifications 
over state-of-the-art methods, underscoring the importance of this enhanced learning process.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents RANKCLIP, a vision-language pretraining method that enhances the alignment between visual and textual modalities. It shifts from traditional pair-wise loss to a list-wise approach, allowing the model to capture many-to-many relationships. RANKCLIP introduces a ranking consistency mechanism to optimize similarity levels within and across modalities. This approach helps the model learn nuanced relationships, such as the closeness between similar images and texts. By leveraging secondary similarities among unmatched pairs, RANKCLIP improves learning efficiency without needing extra data or resources. Comprehensive experiments demostrates the effectiveness of the proposed method in downstream tasks, particularly in zero-shot classification and retrieval accuracy.

### Strengths
- Reasonable Motivation: The paper identifies the limitations of existing models like CLIP, discussing the importance of capturing many-to-many relationships in multimodal data, which provides a reasonable motivation for the development of RANKCLIP.

- Extensive Evaluation: RANKCLIP is evaluated across a variety of downstream tasks, including zero-shot image classification, retrieval, and linear probe classification, showing its applicability in different contexts.

### Weaknesses
 - Lack of Discussion on Related Works: The paper does not adequately discuss other works that also aim to construct many-to-many relationships in vision-language pretraining. For example, [1] proposed a progressive self-distillation method that uses image-to-text logits (and vice versa) as targets, while [2] introduced in-modal consistency.

- Lack of Novelty: RANKCLIP closely resembles the method described in [1], raising questions about its novelty.

- Misaligned Experiment Settings: The experimental setup is misaligned, making the results less convincing. While many CLIP-related works utilize the ViT-B/32 architecture as the vision backbone, RANKCLIP employs RN50, which could affect the comparability of the results.

- Performance Downgrade in Linear Probe Classification: The proposed method underperforms in linear probe classification on fine-grained datasets, such as GVGAircraft, Food101, and GTSRB. The paper does not address this phenomenon, which limits the interpretation of its effectiveness.

- Unconvincing Results in Zero-Shot Text/Image Retrieval: There is a substantial disparity between the results of image retrieval and text retrieval (84.1% vs. 8.1%), which raises doubts about the reliability of these findings.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
RANKCLIP is a language-image pre-training method that incorporates ranking consistency into contrastive learning to enhance model performance. It seeks to better understand complex many-to-many relationships between diverse text-image pairs by optimizing a self-supervised ranking loss. Extensive experiments show that RANKCLIP improves performance, robustness, and semantic understanding across tasks like zero-shot classification and image-text retrieval, outperforming existing models such as CLIP and ALIP.

### Strengths
1.	RANKCLIP is designed to handle the tricky many-to-many relationships between images and text. Instead of just looking at pairs in isolation, it uses a ranking approach to enhance model performance.
2.	When testing against data that’s a little different than what it was trained on, RANKCLIP still holds up well. It also has a knack for understanding semantic nuances, making it better at tasks like image-text retrieval.

### Weaknesses
1.	Although it performs well on variants of ImageNet1K with natural distribution shifts, its top-3 and top-5 accuracy on CIFAR-10 is even lower than that of CLIP. 
2.	The comparison includes too few SOTA methods; additional methods such as CyCLIP and SoftCLIP should be included to convincingly demonstrate the superiority of the proposed method.

### Questions
see weakness.

### Soundness
2

### Presentation
2

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
This paper introduces **RANKCLIP**, a method for training visual-text embedding models that enforces consistent similarity ranking within and between modalities. The objective comprises two components:

1. **Cross-Modal Rank Consistency**: This ensures that the similarity ranking of text instances to an image sample aligns with the ranking of corresponding images to the text sample.
  
2. **In-Modal Rank Consistency**: This component maintains that rankings are consistent within each modality, such that text-to-text and image-to-image similarity searches yield comparable ranks.

These two ranking objectives are combined with the traditional CLIP objective to improve the learning of visual-language embeddings.

Experimental results on zero-shot, linear probing, and text-to-image search tasks demonstrate that the proposed objectives enhance embedding quality, yielding more accurate and consistentrepresentations.

### Strengths
- **Novelty of Rank Consistency Objective**: The rank consistency objective appears to be novel, as existing methods like the CLIP objective rely on an instance discrimination task focused on distinguishing positive examples from negatives. While embedding-level correlations between similar samples are known to emerge naturally from this approach, no method to date has directly leveraged this correlation. The proposed rank consistency loss effectively utilizes this inherent similarity, potentially improving the overall quality of the learned embeddings.

- **Improvement and Scalability in Embedding Quality**: Consistent improvements in embedding quality are observed across various benchmarks. Notably, the gains become more pronounced as training dataset sizes increase (e.g., from CIFAR to ImageNet to YFCC), indicating promising scalability with larger datasets.

### Weaknesses
 - **Integration with the Original CLIP Objective**: While the method improves experimental results, further analysis could clarify how the proposed rank consistency objective interacts with the original CLIP objective. For instance, it would be helpful to understand the balance between the two objectives, or if the rank consistency objective alone could effectively learn cross-modal alignment embeddings. Specifically, the paper lacks a detailed analysis on how the gradients from the rank consistency loss and the CLIP contrastive loss interact during training. Does the rank consistency loss simply refine the embedding space learned by CLIP, or does it significantly alter the learning dynamics? It's unclear if the rank consistency loss is truly necessary for cross-modal alignment, or if it primarily serves to improve the quality of the embeddings within each modality after the initial alignment is achieved by the CLIP objective. This discussion is currently lacking.

- **Limited Ablation Study on Loss Components**: The ablation study on the loss components appears insufficient. Table 5 shows that cross-modal consistency alone performs close to the combined objectives, suggesting that in-modal consistency may have limited impact. This raises questions about whether in-modal consistency is essential, or if the CLIP objective could also benefit from in-modality instance discrimination. The ablation study should also explore the impact of varying the weights of the different loss components, rather than just using a binary on/off approach. For example, what happens when the in-modal consistency loss is weighted more heavily than the cross-modal consistency loss, or vice versa? This could reveal the relative importance of each component and provide insights into their interplay.

- **Limited comparison with other CLIP modifications**: The paper compares with ALIP and CLIP in experiments. However, there are other recent works on improving the CLIP objective, such as SigLIP,. It is a bit difficult to justify the significance of the quality improvement introduced by the method without comparison with the recent methods and analysis of the comparison results. The paper should include a comparison with methods that also aim to improve the embedding space of CLIP, such as those that focus on better alignment or more robust training procedures. Without these comparisons, it's hard to determine if the gains are truly significant or if they are simply due to a different training strategy.

### Questions
Please see the weaknesses section for questions regarding the complementarity between rank consistency and the CLIP objective.

Importantly, I would like to see the authors provide a comparison to more baseline methods for advancing CLIP-style cross-modal learning. I am eager to raise my rating if this comparison can be presented.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduce RANKCLIP, a novel pretraining method that extends beyond the rigid one-to-one matching framework of CLIP and its variants. By extending the traditional pair-wise loss to list-wise, and leveraging both in-modal and cross-modal ranking consistency, RANKCLIP improves the alignment process, enabling it to capture the nuanced many-to-many relationships between and within each modality.

### Strengths
- Overall this paper is well-written and is easy to understand.
- RANKCLIP achieves significant gains in zero-shot classifications over state-of-the-art methods in various downstream tasks.

### Weaknesses
 - There is a lack of discussion and citation of some related works [A][B], which also propose new alignment objectives for efficient vision-language pre-training. The author should discuss them in the main table results or the related work.

     [A] SaCo Loss: Sample-wise Affinity Consistency for Vision-Language  Pre-training
     [B] ProtoCLIP: Prototypical Contrastive Language Image Pretraining


- The authors demonstrated the effectiveness of the framework on limited image encoder (e.g., ResNet50). In order to verify the generalization ability, the authors should conduct sufficient experimental comparisons on more backbone networks.


- This work resorts to the self-supervised ranking consistency for learning relative semantic similarities. However, without manual labeling, the reference ranking may be noisy and cause the construction of the optimal ranking to be unreliable. As a result, the derived objective does not necessarily learn the relative semantic similarity as the authors mention in the introduction.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
