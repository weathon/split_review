# ToVE: Efficient Vision-Language Learning via Knowledge Transfer from Vision Experts

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Vision-language (VL) learning requires extensive visual perception capabilities, such as fine-grained object recognition and spatial perception. Recent works typically rely on training huge models on massive datasets to develop these capabilities. As a more efficient alternative, this paper proposes a new framework that Transfers the knowledge from a hub of Vision Experts (ToVE) for efficient VL learning, leveraging pre-trained vision expert models to promote visual perception capability. Specifically, building on a frozen CLIP image encoder that provides vision tokens for image-conditioned language generation, ToVE introduces a hub of multiple vision experts and a token-aware gating network that dynamically routes expert knowledge to vision tokens. In the transfer phase, we propose a "residual knowledge transfer" strategy, which not only preserves the generalizability of the vision tokens but also allows selective detachment of low-contributing experts to improve inference efficiency. Further, we explore to merge these expert knowledge to a single CLIP encoder, creating a knowledge-merged CLIP that produces more informative vision tokens without expert inference during deployment. Experiment results across various VL tasks demonstrate that the proposed ToVE achieves competitive performance with two orders of magnitude fewer training data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the ToVE (Transfer of Vision Experts) framework, leveraging pre-trained vision models to enhance vision-language learning efficiency by transferring expert knowledge via a token-aware gating network, resulting in competitive performance on vision-language tasks with significantly reduced data requirements.

### Strengths
1. The ToVE framework introduces a novel approach for efficient vision-language learning by utilizing a hub of pre-trained vision experts. This method promotes the effective transfer of knowledge, addressing the challenge of limited data availability in specialized domains.

2. The experimental results demonstrate that ToVE achieves competitive performance across various vision-language tasks using significantly less training data compared to existing models. 

3. The paper includes visualizations of the gating network's routing decisions, illustrating how expert knowledge is allocated across different image regions. This enhances interpretability, showing how ToVE leverages expert knowledge in a token-specific manner to improve performance on complex visual tasks.

### Weaknesses
1.  The process of routing expert knowledge to vision tokens, particularly the token-aware gating network, adds complexity. Although the authors propose methods for detaching low-contributing experts to improve efficiency, the initial setup and training remain computationally intensive, which may hinder practical application. The computational overhead of training the gating network and the multiple MLPs for each expert, combined with the need to manage and select from a pool of experts, could lead to significant memory and processing demands, especially when scaling to larger models or datasets. This complexity might limit the accessibility of the method for researchers with limited computational resources.

2.  The paper introduces a load-balancing loss to ensure a balanced use of experts, but the effectiveness of this loss in preventing over-reliance on certain experts is not extensively validated, leaving questions about how it affects the model’s performance and robustness. The current evaluation lacks a detailed analysis of how the load-balancing loss impacts the final performance across different expert configurations. It is unclear if the load-balancing loss is sufficient to prevent the model from primarily relying on a subset of experts, potentially neglecting valuable information from others. A more thorough investigation, including ablation studies with different load-balancing loss parameters, is needed to fully understand its contribution to the model's overall performance and robustness.

3.  The paper emphasizes the efficiency benefits of transferring pre-trained expert knowledge, yet it lacks a detailed discussion on how ToVE handles potential domain mismatches between the knowledge of vision experts and specific downstream vision-language tasks, such as highly specialized applications. The current work does not address the potential challenges of transferring knowledge from general-purpose vision models to specialized domains. For instance, if the pre-trained experts are trained on natural images, their knowledge might not be directly applicable to tasks involving medical images or satellite imagery. The paper should include a discussion on the limitations of the proposed approach in such scenarios and suggest potential strategies for adapting the method to handle domain mismatches effectively.

### Questions
As shown in Weaknesses.

### Soundness
3

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
This paper introduces ToVE, a selection method for vision encoders in vision-language models. ToVE utilizes multiple vision encoders, each pre-trained differently, and uses a gating network to select their output tokens, which are then added to the tokens from a CLIP encoder as visual features. Notably, these vision encoders can be distilled into a single encoder to reduce inference computation.

### Strengths
1. This paper proposes a novel method for enhancing vision-language models by leveraging multiple vision encoders.
2. Experiments demonstrate the superiority of using multiple vision encoders.

### Weaknesses
1. My primary concern is the significance of this approach. Using multiple vision encoders will multiply the parameter count and computational cost, making comparisons with other base-sized VLMs unfair. On the other hand, if distillation is used to merge them into a single encoder, the resulting composite encoder does not performs obviously better than simply using EVA as the encoder.

| dataset  | EVA    | ToVE-lite |
| ----- | ----- | ----- |
| NoCaps | 109.1 | 104.1|
| VQAv2   | 74.4   | 74.0|
| VSR        |  63.8 | 65.9|
| POPE-R | 85.7 | 86.6|
| POPE-C | 80.8 | 81.9|
| average |82.76|82.50|


This suggests that using ToVE-lite might be less effective than carefully selecting a single, well-performing encoder. The performance of ToVE-lite is inconsistent, showing a decrease in performance on NoCaps and VQAv2, while only showing marginal improvements on VSR, POPE-R, and POPE-C. This inconsistency raises questions about the robustness of the approach.

2. As mentioned above, due to the difference in parameter counts, comparisons with other VLMs may be unfair. Additionally, although the amount of VL data used for pretraining is indicated, the vision encoders and language models themselves are trained on large datasets, enhancing their individual visual and linguistic capabilities, which in turn boosts multimodal performance. Therefore, the amount of pretraining data for both the vision and language models should also be specified. The paper lacks details on the specific datasets used for pre-training the individual vision encoders (e.g., DINO, Depth) and the language model. This makes it difficult to assess the true contribution of the proposed method, as the performance gains could be attributed to the pre-training of the individual components rather than the proposed selection mechanism.

3. The setting used in this paper seems somewhat outdated, as the current trend in VLMs is toward general-purpose multimodal LLMs, such as LLaVA. I recommend that the authors implement ToVE within the LLaVA setting to demonstrate its effectiveness in broader, more contemporary scenarios. The paper focuses on a relatively narrow set of tasks and does not demonstrate the applicability of the proposed method to more complex, open-ended tasks that are common in current multimodal LLMs.

4. The datasets used for comparison are somewhat limited. I suggest adding more datasets, such as GQA, TextVQA, and VizWiz, to provide a more comprehensive evaluation. Additionally, Table 3 should also report the CIDEr score for COCO.

### Questions
See weaknesses above.

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
5

### Summary
This paper presents a novel way to assimilate knowledge from different visual experts trained for different visual tasks into a pre-trained ViT  for solving visual language tasks. The idea of expert knowledge assimilation might not be new, but it is not trivial to align depth, surface normal or edge information along with a clip-based ViT model for vision language tasks. The authors achieve it by a carefully constructed architecture pipeline, where the experts and the ViT model are frozen, a token-based gating network selects which expert to distil knowledge from into that visual token, and then a language decoder utilizes these modified tokens for the final task. They further go on to merge all the expert knowledge into their vision encoder to relieve using multiple experts during inference.

### Strengths
1. The idea of fusing knowledge from multiple experts into the vision encoder is good.

2. The architecture design is novel, relating knowledge fusion to mixture of experts idea.

3. Although similar to Prismer in idea, ToVE does have better results

4. Ablations about types of knowledge merging, expert detachment are quite interesting and insightful

### Weaknesses
1. There are quite a few grammatical and sentence-construction mistakes throughout the paper, for e.g. "The projection function of can be delineated as" this sentence doesn't make sense. Also, the mapping function from d_k to d_lang should be about the feature dimension, since this is achieved by projection function MLPs, but it is written as token lengths, which is not the same as token feature dimension. Is this a writing mistake or the authors are changing token lengths, i.e., number of tokens?

2.  "Different from MOEs, which commonly activates the expert with the top-1 routing score," this is not true. The "original" MoE paper (Shazeer et al) did not have top -1, mainly switch transformer has top-1, and sparse MoE has top-k. Also, the authors employ a load balancing loss exactly similar to the Shazeer et al paper. So, stating that is a bit misleading. 

3. After eq 6, it says t_clip and t_fuse, which does not even appear in the equation.

4. The method requires token-specific output from each expert (eq 1). So, how are tokens obtained for an image from low-level vision experts?

5. In Table 1 and 2, ToVE is not sota but its results are marked bold. (e.g. BLIPv2 CIDEr score in Table1, InstructBLIP POPE-R score in table 2).  Since comparison is tough due to architecture modification, expert merging, it is essential to atleast show number of training parameters to understand the comparison validity

### Questions
1. The paper is not written that carefully. I would suggest the authors to properly rewrite the paper considering grammatical mistakes, notation inconsistencies, etc.

2. How is a token-level knowledge extracted from low-level vision experts? This is not described properly either in main paper or appendix.

3. What would be proper baselines to compare against, since BLIP and others do not use knowledge sharing from other experts? I think the tables need a bit of redesign.

Please address these comments as well as the weaknesses. I am inclined to accept this paper since I like the architecture but the paper needs quite a bit of rework.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method called ToVE, which fuses visual information from different visual encoders as the input of language model in a vision-language model. Specifically, the authors use CLIP-ViT as the main input and use it to weight the tokens from other backbones. Furthermore, the authors proposed a distillation algorithm to teach knowledge from different visual backbones to CLIP-ViT. Experiments show that the proposed method can bring certain improvements to the performance.

### Strengths
1) The proposed method is easy to understand.

### Weaknesses
1) The organization of this paper is somewhat confusing, especially the methods section.
2) The computation overhead can be siginifcantly higher than other methods.
3) The improvement of model capabilities may come from the introduction of a stronger visual backbone, rather than each model playing its own role in its professional field.

1) This article is confusing in several ways:

    a) The author needs to further explain why setting the weights of tokens from unnecessary backbones to -inf in Formula 3 can improve computational efficiency. And authors should clarify if/how they are able to avoid activating all experts.

    b) In the section ``Enhancing Exploration of Vision Experts,'' the authors use the concept of L_aux but only cite it, lacking an explanation of how to apply it in this method. The authors should provide some explanation in the main text.

2. The motivation behind the manuscript and the source of the proposed method's performance need further clarification. From Fig. 8 and Fig. 9, it appears that the strong visual backbone, EVA, plays the primary role in most scenarios. Have the authors considered re-running the baseline experiment using EVA as the sole visual feature extractor? This will help clarify the contribution of the other experts beyond EVA and provide deeper insights into the model's overall performance.

3. There are some methods that ToVE should compare with:

    [1] Zi-Yi Dou, Yichong Xu, Zhe Gan, et.al.. An Empirical Study of Training End-to-End Vision-and-Language Transformers. CVPR 2022.

    [2] Wonjae Kim, Bokyung Son, Ildoo Kim. ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision. ICML 2021

### Questions
1) This article is confusing in several ways:

    a) The author needs to further explain why setting the weights of tokens from unnecessary backbones to -inf in Formula 3 can improve computational efficiency. And authors should clarify if/how they are able to avoid activating all experts.

    b) In the section ``Enhancing Exploration of Vision Experts,'' the authors use the concept of L_aux but only cite it, lacking an explanation of how to apply it in this method. The authors should provide some explanation in the main text.

2. The motivation behind the manuscript and the source of the proposed method's performance need further clarification. From Fig. 8 and Fig. 9, it appears that the strong visual backbone, EVA, plays the primary role in most scenarios. Have the authors considered re-running the baseline experiment using EVA as the sole visual feature extractor? This will help clarify the contribution of the other experts beyond EVA and provide deeper insights into the model's overall performance.

3. There are some methods that ToVE should compare with:

    [1] Zi-Yi Dou, Yichong Xu, Zhe Gan, et.al.. An Empirical Study of Training End-to-End Vision-and-Language Transformers. CVPR 2022.

    [2] Wonjae Kim, Bokyung Son, Ildoo Kim. ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision. ICML 2021

### Soundness
2

### Presentation
2

### Contribution
2
