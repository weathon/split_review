# Open-Vocabulary Customization from CLIP via Data-Free Knowledge Distillation

- Decision: Accept
- Scores: 8, 10, 6, 8

## Abstract
Vision-language models such as CLIP have demonstrated strong zero-shot performance, but their considerable size and inefficient inference limit customizable deployment for users. While knowledge distillation is a solution, it still requires the original data, which is not always available due to copyrights and privacy concerns. For many users seeking open-vocabulary customization, Data-Free Knowledge Distillation (DFKD) emerges as a promising direction. Upon rethinking DFKD, we find that existing methods fail on CLIP due to their heavy reliance on BatchNorm layers, which are unexpectedly unusable in CLIP. Based on our findings, we adopt image-text matching to achieve DFKD for CLIP, enabling customization based on arbitrary class texts. This involves (i) inversing a surrogate dataset from CLIP based on text prompts; and (ii) distilling a student model from CLIP using the surrogate dataset. Specifically, we introduce style dictionary diversification to enhance the diversity of synthetic images. To prevent uncontrollable semantics introduced by diversification, we propose a class consistency maintaining strategy to ensure the consistency of synthetic images. Based on synthetic images with various styles, we further propose meta knowledge distillation to train the student model with good generalization ability. Moreover, we introduce a simple yet effective method to enable customization based on few example images. Comprehensive experiments showcase the superiority of our approach across twelve customized tasks, achieving a 9.33\% improvement compared to existing DFKD methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel approach for open-vocabulary customization in vision-language models like CLIP, utilizing Data-Free Knowledge Distillation. The authors address limitations of existing DFKD methods, which depend heavily on BatchNorm layers incompatible with CLIP. Their method incorporates image-text matching to invert a surrogate dataset, enabling text- and image-based customization. Key innovations include style dictionary diversification, class consistency maintaining, and meta knowledge distillation to enhance the generalizability of a student model.

### Strengths
The paper provides a meaningful contribution to open-vocabulary customization for VLMs, especially under data-free constraints. It addresses practical issues in adapting CLIP without original data, proposing a unique approach to handle limitations posed by BatchNorm layers. Techniques like style dictionary diversification and meta knowledge distillation are well-conceived, though the performance improvements are modest. While the theoretical analysis is detailed, the practical gains might benefit from further validation. Overall, the paper offers useful insights but may require more refinement and broader evaluation to strengthen its impact.

### Weaknesses
The paper's writing could be improved for clarity, as the relevance of BatchNorm (BN) statistics to the later-introduced contrastive learning method is somewhat confusing. The presentation would benefit from clearer contextualization and integration with recent advancements in VLM customization to help situate the contributions more effectively. While the proposed techniques are valuable, additional clarity around specific limitations—such as the potential for style dictionary diversification to introduce noise—could strengthen the paper. Additionally, the reliance on the CLIP model may limit generalizability across other VLM architectures. Expanding future work to include broader applications of the method across diverse vision-language architectures would help validate its adaptability.

### Questions
1. Could the authors elaborate on potential methods to mitigate noise introduced by style dictionary diversification, especially in fine-grained tasks?
2. Are there specific aspects of CLIP’s architecture that are essential to this approach, or could it be adapted to other VLM architectures?
3. In Figure 6, the style differences are not very apparent—could the authors clarify how style diversification manifests visually?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper shows that the existing works that use DFKD methods using CLIP do not perform well. This is blamed on their use of BatchNorm that biases towards faces. The paper introduces an alternate technique for performing DFKD well using CLIP - a text-image matching technique.

### Strengths
This paper presents a novel approach to open-vocabulary customization of Vision-Language Models (VLMs) like CLIP. The authors identify the limitations of existing Data-Free Knowledge Distillation (DFKD) methods and propose a novel solution to address these limitations.

The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a concise overview of their proposed technique. The introduction effectively sets the stage for the paper, with a clear articulation of the research gap and the proposed solution.

The authors provide a comprehensive analysis of related work, demonstrating the novelty of their approach. The experimental findings are compelling, particularly the observation that CLIP's BN layers tend to favor faces, highlighting their unsuitability for DFKD.

The proposed framework's ability to handle both text-based and image-based customization enhances its applicability and significance. The use of instance-level contrastive loss for increased diversity is well-justified, both in practice and through theoretical analysis (Theorem 4.1).

The experimental setup and training details are described thoroughly, which is commendable. The choice of the ImageNet dataset is appropriate, given its scale and diversity. The result analysis is comprehensive and insightful, with the authors exploring various aspects of their approach, including the unique "warm-up" strategy.

### Weaknesses
1. While Figure 1 provides a good overview of the framework, consider replacing the "frozen" and "not frozen" symbols with more intuitive icons, such as a lock and an unlocked lock. Additionally, ensure the frozen symbol is clearly visible in the blue boxes, perhaps by changing its color.
2. Tables 2, 4, and 5 don’t have any units for the numbers or any text mentioning the metric used for those results. Please consider adding metrics and units.

### Questions
1. Why did you use VQGAN? Will the generated data have enough diversity? What other architectures did you consider?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper delves into Data-Free Knowledge Distillation for CLIP so as to distill a compact student model with customized zero-shot or few-shot image classification capacity. Specifically, the proposed framework is composed of surrogate dataset generation and knowledge distillation. For the former component, this paper uses model inversion and style dictionary diversification based on the framework of VQGAN-CLIP. For the latter component, this paper designs a meta method for knowledge distillation. Experiments validate the effectiveness of the proposed framework.

### Strengths
-	This paper is well written.
-	This paper is well motivated to study DFKD for vision-language foundation models.
-	Experiments show the effectiveness of the proposed framework.

### Weaknesses
 - My concern mainly lies in technique novelty. In Fig.1, the proposed framework is composed of dataset inversion process and knowledge distillation process. However, in dataset inversion process, the proposed method is mainly similar to [1] and [2], especially [2], which is also a related work to study DFKD in CLIP. In knowledge distillation, the proposed method is mainly similar to [3], which uses a MAML-like meta learning to enhance cross-domain generalization capacity.

[1] VQGAN-CLIP: Open domain image generation and editing with natural language guidance. ECCV 2022.

[2] Distilling vision-language foundation models: A data-free approach via prompt diversification. ACMMM 2023.

[3] Learning to Generalize: Meta-Learning for Domain Generalization. AAAI 2018.

### Questions
My concern mainly lies in technique novelty. Can you summarize your contribution again based on my concern?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the customization of CLIP for specific user-defined tasks without using original data. The proposed approach involves generation of synthetic images using VQGAN in different styles to increase diversity, while following a data-free meta learning based knowledge distillation technique to adapt a lioghtweight student encoder from teacher CLIP. It aims to overcome the reliance on BatchNorm layers, which hinder customization for ViT variants of CLIP model. The authors have shown extensive experiments with significant improvement of performance of the proposed method compared to CLIP.

### Strengths
1. The method eables model customization without accessing the original data, preserving privacy of the users.
2. The proposed approach captures invariant representations through style diversification and meta knowledge distillation, which is interesting.

### Weaknesses
1. As CLIP is already a very good domain-aware model, what is the motivation behind generating style tranferred images? The diversification could be better and challenging with generation of very fine-grained realistic images.

2. Can pretrained diffusion models be used instead of VQGAN, as it can generate more diverse datasets very easily? What are the pros and cons of using a diffusion model?

3. Why meta learning based knowledge distillation over traditional supervised learning? Any theorectical reason?

    experiments of distillation techniques like TinyCLIP [1], CLIP-KD [2], LP-CLIP [3] are likely to be preferable.

### Questions
See the weakness section. I would like to increase my rating, if the proper justification of my questions will be given.

### Soundness
3

### Presentation
3

### Contribution
3
