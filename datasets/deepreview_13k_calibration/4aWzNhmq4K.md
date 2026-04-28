# Choose Your Anchor Wisely: Effective Unlearning Diffusion Models via Concept Reconditioning

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
Large-scale conditional diffusion models (DMs) have demonstrated exceptional ability in generating high-quality images from textual descriptions, gaining widespread use across various domains. However, these models also carry the risk of producing harmful, sensitive, or copyrighted content, creating a pressing need to remove such information from their generation capabilities. While retraining from scratch is prohibitively expensive, machine unlearning provides a more efficient solution by selectively removing undesirable knowledge while preserving utility. In this paper, we introduce \textbf{COncept REconditioning (CORE)}, a simple yet effective approach for unlearning diffusion models. Similar to some existing approaches, CORE guides the noise predictor conditioned on forget concepts towards an anchor generated from alternative concepts. However, CORE introduces key differences in the choice of anchor and retain loss, which contribute to its enhanced performance. We evaluate the unlearning effectiveness and retainability of CORE on UnlearnCanvas. Extensive experiments demonstrate that CORE surpasses state-of-the-art methods including its close variants and achieves near-perfect performance, especially when we aim to forget multiple concepts. More ablation studies show that CORE's careful selection of the anchor and retain loss is critical to its superior performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel method, termed CORE, designed for the unlearning of diffusion models by selectively eliminating undesirable knowledge. The proposed approach includes an innovative strategy for anchor selection and a newly formulated retain loss. Experimental results demonstrate the method's superior performance compared to existing techniques.

### Strengths
1. The experimental setup is well-structured, effectively addressing the majority of my inquiries regarding this method.  
2. The performance outcomes appear to be satisfactory.  
3. The writing is commendable; the method is articulated clearly, and its key distinctions from other approaches are clearly stated.

### Weaknesses
1. The visual results presented are insufficient. I am particularly interested in scenarios where the forget concepts and the retain concepts contain the same object but differ in adjectives. For instance, in Figure 3, "Dadaism *Cat*" is expected to be forgotten, while "Vibrant Flow *Cat*" should be retained. Could you provide additional visual results for this kind of situation? The current results do not sufficiently demonstrate the method's ability to disentangle style from object identity when both are present in the training data. It is crucial to see examples where the same object is rendered with both the forgotten and retained styles to fully assess the method's selectivity.
2. Ablation study. Without the retain loss, how much worse will the model be? The impact of the retain loss is not sufficiently quantified. It is necessary to see a more detailed analysis of how the model's performance degrades across all evaluation metrics when the retain loss is removed, not just a single aggregated score. This should include a breakdown of the unlearning accuracy, retain accuracy, concept retain accuracy, and the style FID score to understand the specific effects of the retain loss on each aspect of the model's performance.
3. In line 230, the statement "In the unlearning objective, p_a acts as an anchor concept to recondition images from the forget set onto" appears incomplete. It seems that there is a missing component following the word "onto."

### Questions
The explanation of the key differences from other methods, along with the experimental results, solve most of my questions. I have no further questions aside from those mentioned before.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes Concept REconditioning (CORE), a simple yet effective approach for unlearning harmful, sensitive, or copyrighted content from diffusion models. The key contribution lies in the selection of anchor concepts and the retain loss. Extensive experiments demonstrate that CORE surpasses state-of-the-art methods.

### Strengths
1. The paper writing is well.
2. Machine unlearning is an interesting topic and studing how to unlearn some concepts in SD model is important.

### Weaknesses
1. The proposed method appears rather trivial. The author simply presents a pairing method of anchor and forget concepts (either from the retain set or other forget concepts) within the unlearning objective of Concept Ablation (CA)[1]. This is highly engineering-focused and lacks adequate innovation. The proposed retaining loss only transitions from predicting Gaussian noise to aligning with the prediction of the pretrained model. Although experimentally proven effective by the author as indicated in Table 3, the author does not discuss this aspect in sufficient depth, and it is regarded as a relatively minor improvement.

2. There is a deficiency in the comparison with some state-of-the-art methods in the experiments [2, 3, 4].

3. The experiments lack comparisons with more models. For example, SD v1.4, which is commonly employed by previous methods, and larger models like SD - XL. Additionally, there is a lack of results validating the retaining effect on large-scale datasets, such as COCO - 30K.

4. The visualization results do not utilize the commonly used prompts adopted by previous works [1][2], making it difficult to demonstrate advantages over previous efforts. Moreover, the retained concepts also exhibit changes in the image content, as seen in Figure 2.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces concept reconditioning (CORE), a simple yet effective approach for unlearning diffusion models. By guiding the noise predictor conditioned on forget concepts towards an anchor generated from alternative concepts, CORE surpasses state-of-the-art methods including its close variants and achieves nearperfect performance, especially when CORE aim to forget multiple concepts. The difference between CORE with other existing approaches is the choice of anchor and retain loss.

### Strengths
1. This paper produces COncept REconditioning (CORE), a new efficient and effective unlearning method on diffusion models.
2. Extensive tests on UnlearnCanvas demonstrate that CORE surpasses existing baselines, achieving near-perfect scores and setting new state-of-the-art performance for unlearning diffusion models. CORE also exhibits strong generalization in unlearning styles.
3. The ablation studies in paper show that the benefits of using a fixed, non-trainable target noise over other unlearning methods.

### Weaknesses
1. The entire paper feels quite redundant. The related work section and Chapter 2 cover the same material. The content after line 294 in Section 3.2 seems to repeat what was mentioned earlier.
2. The paper mentions various unlearning concepts, such as privacy and explicit content, but in practice, it only focuses on style. The paper claims generalization as one of its contributions, so how is this demonstrated? Or is CORE only applicable to style unlearning? The lack of experiments on other content types limits the scope of the claimed generalization.
3. The paper compares many unlearning methods, but there is only one figure (Figure 2) showing the actual results, and each concept has just one result. The presentation of the outcomes is too sparse. Although the tables show some differences between the models, I still think some of the redundant content could be reduced to include more actual results. The absence of more visual examples makes it difficult to assess the practical impact of the proposed method.
4. In addition to the fact that the methods for removing concepts mentioned in the paper are not comprehensive, there are also methods described in references [1] and [2].
【1】.Ni Z, Wei L, Li J, et al. Degeneration-tuning: Using scrambled grid shield unwanted concepts from stable diffusion[C]//Proceedings of the 31st ACM International Conference on Multimedia. 2023: 8900-8909.
【2】.Patrick Schramowski, Manuel Brack, Björn Deiseroth, and Kristian Kersting. 2023. Safe latent diffusion: Mitigating inappropriate degeneration in diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 22522–22531.

### Questions
1.How does the CORE method perform on other content, such as specific entities or specific concepts?
2.Why can't CORE be directly applied to SD1.5 and instead requires fine-tuning on UnlearnCanvas? From my personal experience, fine-tuning SD1.5 leads to significant changes in its performance, and unlearning on a fine-tuned model makes it relatively easier to control its performance on other non-unlearning concepts. However, this shouldn't reflect the actual scenario.

### Soundness
2

### Presentation
2

### Contribution
2
