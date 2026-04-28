# SemanticMIM: Marring Masked Image Modeling with Semantics Compression for General Visual Representation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
This paper represents a neat yet effective framework, named SemanticMIM, to integrate the advantages of masked image modeling (MIM) and contrastive learning (CL) for general visual representation. We conduct a thorough comparative analysis between CL and MIM, revealing that their complementary advantages fundamentally stem from two distinct phases, \textit{i.e.,} compression and reconstruction. 
Specifically, SemanticMIM leverages a proxy architecture that customizes interaction between image and mask tokens, bridging these two phases to achieve general visual representation with the property of abundant semantic and positional awareness. Through extensive qualitative and quantitative evaluations, we demonstrate that SemanticMIM effectively amalgamates the benefits of CL and MIM, leading to significant enhancement of performance and feature linear separability. SemanticMIM also offers notable interpretability through attention response visualization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper first compares the pros and cons of two related but different lines of work: masked image modeling (MIM) and contrastive learning (CL). They then propose SemanticMIM which brings the pros of CL, i.e. suppression, and global representation, etc, into MIM. Experiments show improvement in several tasks.

### Strengths
1. The analysis of MIM and CL can be beneficial to the community.
2. Introducing [PROXY] tokens between [CLS] and [MASK] as the solution is simple.
3. Visualization in the experiments highlights the claims of the paper.

### Weaknesses
1. The presentation is not good. The figures do not help explain the methods.

2. The layout of Fig. 1 can be changed to fit its goal of comparing MIM and CL as the following.
Image A BeiT-A MoCov-A Ours-A
Image B BeiT-B MoCov-B Ours-B
The current layout is confusing at first glance since A and B are "up vs. down" on the left subfigure but "left vs. right" on the right subfigure.

3. Fig. 1 needs a clearer caption to explain it. The caption does not explain what the reader should be observing here. In what way is "ours" better than the baselines? The paper only explains it later in L49, L246, and L264. Moreover, in L49, how does a reader realize the following claim "MIM focuses on the reconstruction of partially corrupted images, serving as a pretext task that facilitates the model’s ability to infer local patterns from contextual information rather than grasping global semantics" from the figure? The color yellow for the boxes is too similar to the chosen colormap.

4. Fig. 2 can be also made clearer. What is the purpose of the target generators here? What is being trained? The [CLS] tokens and [MASK] tokens should be indicated in this figure. The token color of Fig.2 and Fig.3 should match.

5. In Fig 3, why does the [MASK] token in MIM go straight to [TARGET]? As in Fig. 2, same as CL, MIM also outputs some tokens (blue). The major difference of [MASK] token having positional embedding should be indicated in Fig.2 or 3.

6. In L262, there is a missing space between SimMIM and the citation.

7. In Fig. 4, it does not seem like compression for SemanticsMIM since the number of [MASK] matches the number of [IMG].

8. In L344, semanticMIM -> SemanticMIM.

9. The baselines seem outdated (2021~2022). Can SemanticMIM be compared to [1] or [2]?

10. In the experiment section, why use the term  "[CLS] token with i.e. [PROXY] token" but not just "[PROXY] token"? It is confusing to read.

11. I think the caption in Fig.5 and Fig. 6 should be y-axis (singular).

12. In Sec. 4.4, as a comparison, how many [IMAGE] tokens are there?

13. In Tab. 1, Why compare to only Linear for PascalVOC and only FT for ADE20K? Is using the CLS and Patch tokens as auxiliary inputs for the classifier necessary in the ImageNet experiments? Why is there no "using CLS or Patch tokens" for PascalVOC and ADE20K?

### Questions
1. The layout of Fig. 1 can be changed to fit its goal of comparing MIM and CL as the following.
Image A BeiT-A MoCov-A Ours-A
Image B BeiT-B MoCov-B Ours-B
The current layout is confusing at first glance since A and B are "up vs. down" on the left subfigure but "left vs. right" on the right subfigure.

2. Fig. 1 needs a clearer caption to explain it. The caption does not explain what the reader should be observing here. In what way is "ours" better than the baselines? The paper only explains it later in L49, L246, and L264. Moreover, in L49, how does a reader realize the following claim "MIM focuses on the reconstruction of partially corrupted images, serving as a pretext task that facilitates the model’s ability to infer local patterns from contextual information rather than grasping global semantics" from the figure? The color yellow for the boxes is too similar to the chosen colormap.

3. Fig. 2 can be also made clearer. What is the purpose of the target generators here? What is being trained? The [CLS] tokens and [MASK] tokens should be indicated in this figure. The token color of Fig.2 and Fig.3 should match.

4. In Fig 3, why does the [MASK] token in MIM go straight to [TARGET]? As in Fig. 2, same as CL, MIM also outputs some tokens (blue). The major difference of [MASK] token having positional embedding should be indicated in Fig.2 or 3.

5. In L262, there is a missing space between SimMIM and the citation.

6. In Fig. 4, it does not seem like compression for SemanticsMIM since the number of [MASK] matches the number of [IMG].

7. In L344, semanticMIM -> SemanticMIM.

8. The baselines seem outdated (2021~2022). Can SemanticMIM be compared to [1] or [2]?

9. In the experiment section, why use the term  "[CLS] token with i.e. [PROXY] token" but not just "[PROXY] token"? It is confusing to read.

10. I think the caption in Fig.5 and Fig. 6 should be y-axis (singular).

11. In Sec. 4.4, as a comparison, how many [IMAGE] tokens are there?

12. In Tab. 1, Why compare to only Linear for PascalVOC and only FT for ADE20K? Is using the CLS and Patch tokens as auxiliary inputs for the classifier necessary in the ImageNet experiments? Why is there no "using CLS or Patch tokens" for PascalVOC and ADE20K?

[1] MIMIC: Masked Image Modeling with Image Correspondences. CVPRW 2024.
[2] Learning Vision from Models Rivals Learning Vision from Data. CVPR 2024.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces SemanticMIM, a framework that combines Masked Image Modeling (MIM) and Contrastive Learning (CL) for enhanced visual representation.

Key Contributions:

Theoretical Insights: It analyzes the complementary strengths of MIM and CL, emphasizing their different approaches to semantic modeling—CL focuses on global semantics, while MIM emphasizes local details.

Framework Design: SemanticMIM integrates CL's benefits within the MIM framework using a proxy architecture that combines compression and reconstruction processes into a single learning framework.

Experimental Results: The framework demonstrates significant performance improvements in distinguishing specific object semantics and identifying relevant features, outperforming both MIM and CL in various tasks.

Conclusion: SemanticMIM effectively captures global and spatial information, leading to notable advancements in visual representation for downstream applications.

### Strengths
The strengths of this paper lie in its innovative integration of Masked Image Modeling (MIM) and Contrastive Learning (CL) within a unified framework, effectively leveraging the advantages of both approaches. Additionally, SemanticMIM excels at capturing both global semantics and local features, enhancing the ability to distinguish specific object semantics. Finally, in addition to quantitative experiments, the paper also includes extensive qualitative analyses and visualizations to demonstrate the effectiveness of the framework.

### Weaknesses
The paper's limitations include insufficient quantitative experiments, particularly a lack of tests with models of varying sizes across different settings. Additionally, while the paper provides segmentation results for downstream tasks, the promising attention effects raise expectations for object detection performance as well. It would be beneficial for the authors to include more experimental results in the rebuttal stage. The core issue lies in the experimental setup, specifically with the object detection results. The reported performance is significantly lower than what has been achieved with similar backbones in the literature. For example, the object detection performance using a plain Vision Transformer backbone should be much higher than what is presented in the paper. Furthermore, the model size experiments lack a direct comparison with existing Masked Image Modeling (MIM) methods, making it difficult to assess the true effectiveness of the proposed approach. The absence of comparisons with established methods, such as MAE, under similar experimental conditions, makes it hard to determine if the performance gains are due to the method itself or other factors, such as training settings.

### Questions
The shortcomings in the experimental section raise concerns about whether this training method can scale to larger models and be applied to a broader range of downstream tasks. If the authors can provide additional experimental results, I would be willing to reconsider and potentially increase the score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a self-supervised learning method to pretrain vision transformers named SemanticMIM. SemanticMIM tries to take the advantage from both masked image modeling and contrastive learning by leveraging a proxy architecture that customizes interaction between image and mask tokens, bridging these two phases to archieve general visual representation with the property of abundant semantic and positional awareness. I think the novelty of this paper is good. But my presentation is poor and the experiments are so insufficient.

### Strengths
1. The novelty seems good, a very interesting method to combine the MIM and CL together;
2. Many analysis experiments enhance the quality of this paper;

### Weaknesses
1.I do not think attention response (figure 1&7&8) can represent the the quality of the learned features. For example, the attention responses of models using the CLIP model as a supervisory signal all appear poor, but their actual performance is often much better. Furthermore, the comparison of attention maps between the proposed method and BEiT is not a fair comparison, as BEiT is explicitly designed to reconstruct masked tokens, leading to inherently different attention patterns. The attention maps of BEiT are expected to be more focused on the masked regions, while SemanticMIM's attention might be distributed differently due to its contrastive learning component. This difference in design makes direct visual comparison of attention maps misleading.
2.It seems that the authors did not use \citep{} correctly while writing and instead used \cite{}. This resulted in an inconsistent citation format throughout the entire paper.
3.I suggest the authors to provide a comparison on training cost, because the proposed method seems have larger computational cost. Specifically, the introduction of proxy tokens and the additional computations required for the contrastive learning component could significantly increase the training time and resource consumption. A detailed analysis of the computational overhead, including FLOPs and memory usage, is needed to assess the practical feasibility of the method.
4.Experimental results are insufficient: longer epochs and larger models (L-scale) need to be validated, which is crucial for self-supervised learning. Downstream task results are also needed, such as semantic segmentation and object detection. (This is the biggest concern!) The current experiments do not adequately demonstrate the scalability and generalizability of the proposed method. The absence of results on standard downstream tasks makes it difficult to assess the practical value of the learned representations.

### Questions
Do you think the downstream task performance is good enough to evaluate a self-supervised model? If so, the current MIM methods have achieved very good results and I think the proposed method has NO potential to reach such high results. If not, what metrics is needed do you think to evaluate a pretrained model?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes SemanticMIM, a framework that integrates the strengths of masked image modeling (MIM) and contrastive learning (CL) to achieve general visual representation learning. Specifically, SemanticMIM leverages a proxy architecture to compress information from image tokens into proxy tokens and then reconstructs masked tokens, thereby combining the semantic awareness of CL with the spatial sensitivity of MIM. As the approach only modifies the encoder architecture, it can be seamlessly integrated into any MIM framework. Extensive experiments further validate the effectiveness of the model and offer interpretability through attention visualization.

### Strengths
1. The analysis of the fundamental principles underlying CL and MIM is insightful and thought-provoking.

2. The proposed SemanticMIM is well-motivated, which leverages the strengths of both CL and MIM.

3. SemanticMIM improves the performance of two MIM methods when applied using the training scheme introduced in this paper.

### Weaknesses
1. Some important details about the training process are missing. For instance, are the [PROXY] tokens supervised with specific targets, similar to the supervision used in CL? Are the [MASK] tokens trained using the same loss function employed in typical MIM frameworks? Clarifying these aspects would enhance the reproducibility and understanding of the proposed approach.

2. The classification of SSL methods into only CL and MIM may not be entirely accurate. Earlier works also introduced a variety of pretext tasks, such as image colorization and rotation prediction, which play an important role in the development of SSL methods. A more comprehensive overview of these earlier approaches can be found in the survey “Self-supervised visual feature learning with deep neural networks: A survey”.

3. The reproduced performance of BEiT and Maskfeat in this paper appears much lower than the original results reported in their respective papers. Could you clarify why the official training schemes were not followed? Additionally, if the official training schemes were applied, how much improvement would SemanticMIM bring to these MIM methods?

4. The citation format in some sections of the text requires correction. For example, “Self-supervised learning (SSL) algorithms Liu et al. (2021); Balestriero et al. (2023) have emerged as …” should be revised to “Self-supervised learning (SSL) algorithms (Liu et al. 2021; Balestriero et al. 2023) have emerged as …” to conform to general academic writing practices.

### Questions
From Fig. 14, it appears that different layer depths yield different types of attention maps. In Fig. 1, are all the displayed attention maps derived from the same layer depth? Providing this clarification will help readers better understand the visual interpretability.

### Soundness
2

### Presentation
2

### Contribution
3
