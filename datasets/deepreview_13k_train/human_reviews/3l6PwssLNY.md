# CR2PQ: Continuous Relative Rotary Positional Query for Dense Visual Representation Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Dense visual contrastive learning (DRL) shows promise for learning localized information in dense prediction tasks, but struggles with establishing pixel/patch correspondence across different views (cross-contrasting). Existing methods primarily rely on self-contrasting the same view with variations, limiting input variance and hindering downstream performance. This paper delves into the mechanisms of self-contrasting and cross-contrasting, identifying the crux of the issue: transforming discrete positional embeddings to continuous representations. To address the correspondence problem, we propose a Continuous Relative Rotary Positional Query ({\mname}), enabling patch-level representation learning. Our extensive experiments on standard datasets demonstrate state-of-the-art (SOTA) results. Compared to the previous SOTA method (PQCL), our approach achieves significant improvements on COCO: with 300 epochs of pretraining, {\mname} obtains \textbf{3.4\%} mAP$^{bb}$ and \textbf{2.1\%} mAP$^{mk}$ improvements for detection and segmentation tasks, respectively. Furthermore, {\mname} exhibits faster convergence, achieving \textbf{10.4\%} mAP$^{bb}$ and \textbf{7.9\%} mAP$^{mk}$ improvements over SOTA with just 40 epochs of pretraining.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Continuous Relative Rotary Positional Query to enhance dense visual contrastive learning by improving pixel/patch correspondence across different views. It addresses limitations in existing self-contrasting methods by transforming discrete positional embeddings into continuous representations. The proposed CR2PQ enables more effective patch-level representation learning, achieving state-of-the-art results and faster convergence in detection and segmentation tasks on the COCO dataset.

### Strengths
1. Writing quality is good. The paper is well-structured, and clearly written.
2. SOTA performance. The paper demonstrates the state-of-the-art performance on mainstream detection and segmentation datasets, such as COCO and ADE20K, which is impressive.
3. Versatility of the method. The paper shows the simplicity of CR2PQ, which can be easily integrated into a variety of popular representation learning frameworks, such as mask-based learning, contrastive learning, and distillation methods.

### Weaknesses
1. Reliance on random cropping. Although random cropping can increase the variability of the input, its results may still be limited by the randomness of the cropping. In extreme cases, it may result in almost no overlap between the generated views, affecting the learning effect of the model. The lack of a systematic approach to view generation could lead to inconsistent performance, especially when the overlap between views is minimal, potentially hindering the model's ability to learn robust correspondences.
2. Computational complexity. Complex matrix operations are required when calculating relative position embedding and rotating embedding, which increases the burden in scenarios with limited computing power. The paper does not provide a detailed analysis of the computational overhead associated with these operations, making it difficult to assess the practical applicability of the method in resource-constrained environments. This lack of analysis raises concerns about the scalability of the approach.

P.S. There is an error in Figure 1. [CLS] should be global information, while patch is local information.

### Questions
Please refer to the weaknesses above.

### Soundness
3

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
3

### Summary
The authors propose a distillation technique where a student is densely trained to match teacher features. The novelty comes from using 2D RoPE in the network as well as a cross-attention module with relative positional information. They show good empirical results on detection and segmentation.

### Strengths
-The empirical results are good and outperform previous SOTA.

-I think this paper can be worthwhile to accept, I'm willing to improve my score based on the author's reply.

### Weaknesses
-L142: Relative positional encoding = RoPE? This statement is unclear, as RoPE is a specific type of positional encoding, and the text suggests they might be equivalent. This needs clarification, as it is not clear if the authors are using RoPE directly or a modified version.

-L161: W_{pos} v.s. P_{pos} ? The distinction between these two terms is not clear, and it is not explained why they are used differently. The notation should be consistent and well-defined.

-The notation in equation 1 is confusing. It is as if the patches don’t interact with each other. I would use a new variable to define a patch representation. Also if f_\theta denotes the ViT, why does it take z as input, which already contains the linear layer on the left side of the equation but not on the right side. I think the notation should be made more precise. The lack of clarity makes it difficult to understand the exact computations being performed.

-Equation 2 has some n and m mixed. The inconsistency in the use of these variables makes the equation difficult to interpret and verify.

-L219: “we set each patch size of the view A as 1”, but in L227 p_A (the patch size) is defined? This is contradictory and needs to be clarified. The patch size should be consistently defined throughout the paper.

-L228: There is a sentence “Since we set each grid size of the anchor view as 1.” What is that supposed to mean? The meaning of setting the grid size to 1 is not clear and requires further explanation.

-L297: If I’m not mistaken, the definition of q doesn’t make sense. The definition of q appears to be incorrect or inconsistent with the rest of the paper, and it should be reviewed and corrected.

-The first stated contribution is using 2D RoPE for SSL based methods. Then, in L358, shoud state “We also evaluate the detection and segmentation without pretraining i.e. directly using 2D RoPE”. First, that entry is only in Table 1 and not Table 2. Second, I think you should also independently show empirical evidence of your 2 first contributions (2D RoPE and cross-attention module) and report results for that. The lack of independent validation for each contribution makes it difficult to assess their individual impact.

-In general, I think the paper could be more explicitaly precise with how sizes/positions are encoded e.g. is it relative to the original image input grid or relative to the crop? The lack of clarity regarding the reference frame for size and position encoding makes the method difficult to reproduce and understand.


Minor:

-L082: “as the downstream task only input”

-If I’m not mistaken, there is a problem with sentence at L203 starting with i.e.

### Questions
-Why use a pretraining network for the teacher? You are comparing with other baselines which some of which learn everything from scratch. This seems like a logical thing to try, have you tried that?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
1. The paper introduces Continuous Relative Rotary Positional Query (CR2PQ), a novel method for dense visual representation learning.
CR2PQ addresses the challenge of establishing pixel/patch correspondence across different views in dense contrastive learning (DRL) by transforming discrete positional embeddings to continuous representations.

2. It utilizes a rotary positional embedding to represent the relative positions between two views and reconstructs the latent representations of one view from another through a rotary positional query.

3. The method simplifies the dense contrastive learning paradigm by making it correspondence-free and integrates easily into various representation learning frameworks.

4. Extensive experiments on standard datasets demonstrate state-of-the-art (SOTA) results, outperforming the previous SOTA method (PQCL) significantly in detection and segmentation tasks on COCO with improved mAP scores.

### Strengths
1. CR2PQ introduces a pioneering method for dense visual representation learning by utilizing continuous relative rotary positional embeddings, which is a significant departure from traditional discrete embeddings.

2. The method achieves state-of-the-art results across various benchmarks, including object detection and segmentation tasks on COCO and semantic segmentation on ADE20K, outperforming previous leading methods by a considerable margin.

3. The introduction of a positional-aware cross attention module enhances the learning of semantic information without incurring significant additional computational costs. CR2PQ's use of rotary positional embeddings makes it robust to various view augmentations, including random cropping, which is a common challenge in contrastive learning methods.

4. The paper supports the method's strengths through extensive experiments and ablation studies, providing a thorough analysis of CR2PQ's performance under different conditions and configurations.

### Weaknesses
1. Experiments. The author should provide more scales of backbone to validate the scalability of the method. Most experiments are conducted on ViT-S. The reviewer understands the efficiency of the experiments, however, there should be some experiments on larger backbones.



### Questions
1. What is the performance of the CR2PQ backbone performance on some strong detectors, such as DINO or Co-DETR?

2. CR2PQ requires the teacher model to provide contrastive pairs, however, the performance does not improve as the model becomes larger (ViT-L vs ResNet50). The reviewer wonders about the performance of a larger model for the student. Does this approach work for a larger backbone as a student, such as ViT-L/ViT-G? The authors are suggested to validate the scalability of the method.

3. Some small mistakes

- The font of the paper is different from other papers. Should it be correct? 

- line 274, there is an overlap between the table and the caption.

### Soundness
2

### Presentation
3

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
The paper presents a novel self-supervised framework for dense visual representation learning, which avoids the need for explicit dense correspondences between local features across views. Instead, the framework reframes the task as predicting local representations from one view to another, guided by relative positional cues. It integrates rotary positional embeddings within the student model and distills knowledge from a pre-trained, frozen teacher model. This approach yields faster convergence and improved performance on standard benchmark evaluations.

### Strengths
- The proposed self-supervised framework for dense visual representation learning is novel.
- The method elegantly eliminates the need to establish explicit correspondence between local features across views by leveraging relative positional cues.
- The performance on dense downstream tasks is thoroughly evaluated, showing faster convergence and achieving state-of-the-art results on standard benchmarks.

### Weaknesses
 - The proposed self-supervised framework for dense visual representation learning is novel.
- The method elegantly eliminates the need to establish explicit correspondence between local features across views by leveraging relative positional cues.
- The performance on dense downstream tasks is thoroughly evaluated, showing faster convergence and achieving state-of-the-art results on standard benchmarks.

 - The method differs from existing baselines in three key ways: (1) the use of rotary positional embeddings, (2) the use of a pre-trained, frozen teacher model, and (3) the proposed pretext task. This makes it challenging to assess the contribution of each component to the overall performance. Specifically, the fairness of the experimental setup is questionable, as other methods are trained from scratch while CR2PQ benefits from a pre-trained teacher. More ablation studies are needed to separate the impact of each element. For instance, the impact of the teacher model's initialization (random vs pre-trained) and the effect of the teacher's architecture on the final performance are not explored. Furthermore, the specific choice of the pre-training dataset for the teacher model could also influence the results, which is not discussed.

- Overall, the writing is difficult to follow, with multiple notation inconsistencies, typos, and signs of negative vertical spacing used to fit within the page limit. The lack of clarity in the description of the method makes it hard to reproduce and evaluate the contribution of each component. For example, the description of the relative positional encoding is not clear, and the relationship between the different views and their patch sizes is confusing.

- Equation 1 is misleading/incorrect as it suggests that the representation of a single patch is independent of its context. The equation should reflect the fact that the representation of a patch is influenced by its neighboring patches. The current formulation implies that each patch is processed in isolation, which is not how transformer models operate. 
- Equation 2: The angle of the key seems incorrect. The angle should be relative to the reference patch, not an absolute angle. The current formulation does not clearly explain how the relative positional information is incorporated into the key.
- Line 210: The image dimensions are inconsistent with line 157. The inconsistency in image dimensions makes it difficult to understand the exact input to the model.
- Line 214: Inconsistent use of $\mathbf{p}{a}$ and $\mathbf{p}{A}$. The inconsistent notation makes the description hard to follow and understand.
- Line 234: The notation is inconsistent with the left side of Equation 3. The notation should be consistent throughout the paper to avoid confusion.
- Table 1: Framwork $\rightarrow$ framework.
- Figure 1: There seem to be inconsistencies in the notations used within the figure and also with respect to the method section. The notations in the figure should be consistent with the notations used in the method section.
- "pertaining" $\rightarrow$ "pretraining"/"pre-training" (11 occurrences).
- Line 86: exhausted $\rightarrow$ exhaustive.
- Line 161: $\mathbf{W}{pos}$ $\rightarrow$ $\mathbf{P}^{i}{pos}$.

### Questions
- In Table 1, what does the row "RoPE" exactly correspond to? A ViT-S/16 equipped with rotary positional embedding, randomly initialized and finetuned on the downstream task?

- In Table 4, what does the row "EMA update (Contrastive)" exactly correspond to? Is the teacher randomly initialized?

- At line 219. it is mentioned that the patch size of view A is set to 1, but then it is set to $p_{A}$. Can you clarify this?

- At line 227: I suggest using another notation for $p_{A}$ as the patch size, as it is confusing.

### Soundness
3

### Presentation
2

### Contribution
3
