# TIPS: Text-Image Pretraining with Spatial awareness

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
While image-text representation learning has become very popular in recent years, existing models tend to lack spatial awareness and have limited direct applicability for dense understanding tasks. For this reason, self-supervised pretraining is still the go-to method for many dense vision applications (e.g. depth estimation, semantic segmentation), despite the lack of explicit supervisory signals. In this paper, we close this gap between image-text and self-supervised learning, by proposing a novel general-purpose image-text model, which can be effectively used off-the-shelf for dense and global vision tasks. Our method, which we refer to as Text-Image Pretraining with Spatial awareness (TIPS), leverages two simple and effective insights. First, on textual supervision: we reveal that replacing noisy web image captions by synthetically generated textual descriptions boosts dense understanding performance significantly, due to a much richer signal for learning spatially aware representations. We propose an adapted training method that combines noisy and synthetic captions, resulting in improvements across both dense and global understanding tasks. Second, on the learning technique: we propose to combine contrastive image-text learning with self-supervised masked image modeling, to encourage spatial coherence, unlocking substantial enhancements for downstream applications. Building on these two ideas, we scale our model using the transformer architecture, trained on a curated set of public images. Our experiments are conducted on 8 tasks involving 16 datasets in total, demonstrating strong off-the-shelf performance on both dense and global understanding, for several image-only and image-text tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a spatial-aware text-image pre-training method that combines contrastive image-text learning with self-supervised masked image modeling. Besides, the method proposes to combine the noisy web captions and synthetic captions that are more helpful to learn spatially aware representations. The method is evaluated on both zero-shot classification and dense prediction tasks.

### Strengths
- The paper presents a solid work on text-image pre-training: a large-scale synthetic caption dataset is created, the method is evaluated on both classification and dense prediction tasks, and extensive experimental studies are conducted for ablation studies and analyses. 

- The results look good. The proposed method can achieve good dense prediction and classification/retrieval performance simultaneously. Ablation results provided in the paper may be helpful for developing new text-image models.

### Weaknesses
 - The general idea of combining contrastive image-text learning and masked image modeling is not new. Previous work like EVA-CLIP [r1] has already show that MIM can improve the spatial awareness or locality of CLIP features and improve CLIP performance. The core different between TIPS and the line of work is to combine MIM and CLIP successively or simultaneously. I think simultaneously perform the two tasks may be better to preserve the spatial awareness/locality, but it may also make the training more costly, or possibly unstable. It would be better to provide a comparison/analysis on the pros and cons of the two strategies.  

[r1] EVA-CLIP: Improved Training Techniques for CLIP at Scale

- The study use the proprietary WebLI dataset to train the model. Is it possible that the improvements over previous methods mainly come from better data sources?  How about the results if both the proposed model and the baseline use publicly available datasets like LAION, COYO or DataComp.

### Questions
Please refer to my comments above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel pretrained image-text encoder with spatial awareness which is effective in a variety of downstream computer vision tasks. To achieve this, the author first employs pretrained multimodal generative models to generate high-quality synthetic image descriptions and develops a dual embedding approach that leverages both synthetic and noisy web captions in training. Additionally, contrastive image-text learning, coupled with self-distillation and masked image modeling, is introduced to encourage the model to learn spatially aware representations. Experiments conducted on eight downstream tasks validate the effectiveness of the proposed method.

### Strengths
1. The author proposes an effective approach that enhances the utility of both synthetic and noisy web captions in training. They also introduce contrastive image-text learning with self-supervised masked image modeling, which effectively encourage the learning of spatial coherence.
2. The author conduct a variety of experiments in 8 downstream tasks demonstrate the effectiveness of its spatial-aware text-image encoder.

### Weaknesses
The formatting of the paper needs improvement and there are  a lot of empty spaces around fig1 and fig2.

### Questions
Will the pretrained model and the curation dataset with synthetic captions be released?

### Soundness
4

### Presentation
4

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
This paper targets integrating the paradigms of both image-text representation learning and self-supervised learning to improve the spatial awareness of the former. For the SSL branch, the authors leverage the DINO V2 (iBOT) pre-training method; for the image-text branch, they propose the dual image-text embedding technique that learns from both noisy and sythetic captions while harnessing the distribution gap between two types of captions. The effeciveness of the proposed method is evaluated on several image-level multimodal tasks and comprehensive dense image prediction tasks.

### Strengths
- This paper is well written.

- The experiments on dense image prediction tasks are comprehensive and promising, outperforming DINO V2 on several tasks.

- Improving the spatial awareness of image-text representation learning is an important direction, combining DINO v2 and CLIP, where both are foundational works in their respective fields, is intuitive and promising.

### Weaknesses
 - The technical contributions are limited. The proposed method is a combination of existing methods, with the dual embedding technique being the only novel contribution. Nonetheless, I'm okay with this, since the proposed model effectively and adequately solves model's spatial awareness limitation.

- As claim in Line 300: 
>Our method is the first to demonstrate that combining contrastive image-text learning with self-distillation and masked image modeling leads to improvements across many tasks

However, both integrating CLIP with self-distillation and masked image modeling[1][2] have been proposed before. And this paper lacks a further discussion against these works.

- Since this is a multimodal model with spatial awareness, only I$\rightarrow$T and T$\rightarrow$I retrieval tasks are not enough to evaluate the model's fine-grained spatial awareness under multimodal settings. Including more experiments like open-vocabulary segmentation would be beneficial.

### Questions
- As the motivation of this paper is to bridge the gap between image-text representation learning and SSL, although the ablation studies are provided, this paper lacks an in-depth analysis on how the two paradigms interact with each other. For example, how the SSL design choices such as augmentations (mask ratio, etc.) affect the image-text representation learning. 

- The idea of dual embedding is interesting. I'm curious about the different roles of the two embeddings, and how they interact with the network. Could the authors provide more empirical analysis on this? For example, visualization of the attention maps of the two different $[CLS]$ to see their focus areas.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses dense and global vision tasks by enhancing textual supervision and integrating contrastive image-text learning with self-supervised techniques. The method combines noisy web captions with synthetically generated captions to improve spatial awareness and applies masked image modeling to promote coherence in spatial understanding. As a result, the model demonstrates robust performance across various tasks without the need for fine-tuning, showcasing its general-purpose applicability in both image-only and image-text applications.

### Strengths
1.	The paper is well-structured and clearly articulated, with detailed experimental records. By cleaning and constructing a high-quality dataset and incorporating self-supervision, methods such as dual captioning and masked image modeling enable the model to achieve significant (albeit incremental) advancements in dense prediction tasks.
2.	The trained model demonstrates strong generalizability across multiple tasks, indicating its broad applicability in vision tasks.
3.	The paper includes a substantial amount of experimental comparisons and work.

### Weaknesses
1.	The work presents only a limited amount of novelty. The main critique lies in the lack of significant innovation. The paper largely repurposes existing techniques like synthetic captioning and contrastive learning, and while the results are solid, they do not represent a substantial leap forward in the field. The combination of these techniques, while effective, does not introduce a fundamentally new approach to the problem of dense and global vision tasks. The core idea of using synthetic captions to enhance spatial awareness, while showing some improvements, is not conceptually groundbreaking, as similar ideas have been explored in other contexts, albeit not directly for this specific application.
2.	The improvements over existing models such as CLIP and DINOv2 are incremental, and the performance gains are sometimes marginal or context-specific. The originality in combining these techniques does not feel transformative. While the paper demonstrates improvements on certain benchmarks, the magnitude of these improvements does not suggest a paradigm shift in the field. The gains, especially in tasks where existing models already perform well, are not significant enough to justify the claim of a major advancement. The method's performance seems to plateau quickly, indicating that the combination of techniques might not scale effectively to more complex scenarios.
3.	More detailed ablation studies focusing on the contribution of each component (e.g., the specific impact of spatial coherence from the captions) could strengthen the claim of novelty. The current ablation studies do not sufficiently isolate the impact of individual components, making it difficult to ascertain the true contribution of each aspect of the proposed method. For instance, it is unclear how much of the performance gain is due to the synthetic captions versus the masked image modeling, and whether the spatial coherence of the captions is the primary driver of the observed improvements.

### Questions
1.	Authors are suggested to add detailed ablation results to isolate the impact of the synthetic captions on different spatial tasks.
2.	Have you considered alternative ways of introducing spatial awareness besides synthetic captions and masking?

### Soundness
2

### Presentation
3

### Contribution
2
