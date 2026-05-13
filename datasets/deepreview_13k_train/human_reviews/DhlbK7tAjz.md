# MaskInversion: Localized Embeddings via Optimization of Explainability Maps

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Vision-language foundation models such as CLIP have achieved tremendous results in global vision-language alignment, but still show some limitations in creating representations for specific image regions. %
To address this problem, we propose MaskInversion, a method that leverages the feature representations of pre-trained foundation models, such as CLIP, to generate a context-aware embedding for a query image region specified by a mask at test time.
MaskInversion starts with initializing an embedding token and compares its explainability map, derived from the foundation model, to the query mask.
The embedding token is then subsequently refined to approximate the query region by minimizing the discrepancy between its explainability map and the query mask. During this process, only the embedding vector is updated, while the underlying foundation model is kept frozen
allowing to use MaskInversion with any pre-trained model. 
As deriving the explainability map involves computing its gradient, which can be expensive, we propose a gradient decomposition strategy that simplifies this computation.
The learned region representation can be used for a broad range of tasks, including open-vocabulary class retrieval, referring expression comprehension, as well as for localized captioning and image generation. We evaluate the proposed method on all those tasks on several datasets such as PascalVOC, MSCOCO, RefCOCO, and OpenImagesV7 and show its capabilities compared to other SOTA approaches.\footnote{Project page: \url{https://walidbousselham

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces MaskInversion, a method that leverages pre-trained vision-language models (such as CLIP) to generate context-aware embeddings for specific image regions by optimizing explainability maps. It aims to improve localized image representation tasks, such as referring expression comprehension and captioning, while employing a gradient decomposition strategy to reduce computation.

The contributions of this paper include:
1) a new method that is able to learn localized embeddings for given queries;
2) an efficient gradient decomposition approach for multi-query masks;
3) improved performance on various downstream tasks.

### Strengths
1. The motivation is interesting. The problem of poor localization capabilities does exist in CLIP.
2. The proposed method is intuitive.
3. The performance is good. MaskInversion achieves superior results on a wide range of vision-language benchmarks.

### Weaknesses
1. Very important baselines are missing. I noticed that you have discussed the paper of MaskCLIP [1] but did not compare with it in the experiments. Actually, CLIP's localization issues can be addressed in a very simple way. You just need to reform the last layer's self-attention in the fasion of MaskCLIP (removing Q and K), SCLIP [2] (Q-to-Q and K-to-K attention), or CLIPSurgery [3] (V-to-V attention with dual paths). I believe by simply modifying CLIP with these methods (they are all training-free), the performance can be improved by a very large margin.

2. Given these baselines are missing, it's difficult to evaluate whether the new method is effective enough. As MaskInversion involves a much more complex process, I expect it to perform significantly better than those three baselines. The lack of comparison makes it unclear if the performance gains justify the added complexity.

3. The other contribution of the paper, gradient decomposition, is not that significant. As shown in Table 5, It makes clear speed improvements only if we have >10 masks/image. What is the general case of the number of masks involved in your tasks? The practical benefit of this optimization seems limited to niche scenarios involving a high number of masks.

4. Minor comments: there are some typos in the paper such as in Line 481, what does Table 4.5 refer to?

### Questions
See Weaknesses.

---- updates after rebuttal ----
I appreciate the authors' response and additional experiments for the metioned baselines. While MaskInversion outperforms the training-free approaches in most cases, some of my concerns are addressed. Howerver, the authors did not discuss the new results in the revised paper, which may cause misleading for readers. Overall, I still think this is a boarderline paper and have changed the score to 5. I still have concerns about the scalability of the method, as on OpenImagesV7, which is relatively more complex and has more masks in the images, MaskInversion performs worse than CLIPSurgery.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MaskInversion, a method designed to generate localized embeddings for specific image regions using pre-trained vision-language foundation models like CLIP. This approach leverages the feature representations of these models to create context-aware embeddings for a query image region specified by a mask at test time.

### Strengths
1. This paper is overall well-written.
2. The paper provides a comprehensive set of experiments and results, including quantitative metrics and qualitative visualizations, which helps in understanding the method's effectiveness and behavior.
3. MaskInversion operates in a zero-shot setting, which means it can handle tasks without requiring additional training data for specific tasks, leveraging the knowledge embedded in pre-trained models.

### Weaknesses
1. This paper may be a bit short on innovation, as it actually uses the explainability map obtained from LeGrad to improve the feature extraction of the pre-trained models. Besides, some of the methods section is devoted to reviewing LeGrad, reinforcing the perception that this article is not innovative enough.
2. The regulaization loss seems very important to avoid trivial solutions. However, I find no ablation study on the hyper-paramter $\alpha$, which modulates the influence of the regularization loss. 
3. The performance of MaskInversion is heavily dependent on the quality of the input masks. In practical applications, obtaining high-quality masks might be challenging, which could limit the method's real-world applicability.
4. The paper could benefit from a deeper analysis of scenarios where MaskInversion might fail or underperform, and how such cases could be addressed.

### Questions
If the pre-trained model itself does not have strong local feature capture capability, then post-training can give limited improvement. I'm curious if this idea of mask-guided feature capture can be applied to the training phase to improve the fine-grained perception of pre-trained VL models.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new method that uses explainability maps from pretrained models to generate localized embeddings. These embeddings can represent object properties while capturing the broader image context. The paper further demonstrates that these learned region representations are versatile and can be applied to various tasks, including retrieval, grounding, captioning, and image generation.

### Strengths
The paper introduces a novel approach leveraging explainability methods to enable the model to focus on specific regions within an image. Unlike traditional techniques like clipping, blurring, or masking, this approach allows the model to retain access to global image information. The method is clearly outlined and validated through comprehensive downstream tasks, demonstrating its effectiveness.

### Weaknesses
The paper primarily focuses on single-object scenarios, lacking analysis on multiple objects and their interactions. Including experiments and analysis on multi-object scenarios would strengthen the study and provide a more comprehensive evaluation of the method's effectiveness. For instance, datasets like MSCOCO, with complex captions involving multiple objects, could offer valuable insights; sharing examples from such datasets would further illustrate the model's performance in these scenarios.

The paper does not adequately explore the nature of the global image context captured by the method. While the method aims to retain global information, the specific mechanisms and the extent to which this context influences localized embeddings remain unclear. The lack of visualizations or analysis demonstrating how the global context modulates the localized embeddings across different scenarios is a significant gap.

In referring expression retrieval tasks, MaskInversion with ViT-B/16 underperforms compared to Masked Crop in RefCOCO+. The paper does not provide a sufficient analysis of why this discrepancy occurs, particularly given the method's supposed ability to leverage global context. This raises questions about the method's robustness and its suitability for tasks that rely heavily on appearance-based descriptions.

### Questions
1. What type of global image context does this method capture? Could the authors provide visualizations, like attention map, to illustrate how the global context influences localized embeddings across different scenarios? This would clarify the method’s effectiveness in capturing and utilizing global context for downstream tasks.
2. In referring expression retrieval tasks, MaskInversion with ViT-B/16 underperforms compared to Masked Crop in RefCOCO+. Could the authors provide a detailed analysis investigating the reasons for this discrepancy?
3. Minor comment: In the related work section, "maks" should be corrected to "masks".

### Soundness
3

### Presentation
3

### Contribution
3
