# Can One Modality Model Synergize Training of Other Modality Models?

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
Learning with multiple modalities has recently demonstrated significant gains in many domains by maximizing the shared information across modalities. However, the current approaches strongly rely on high-quality paired datasets, which allow co-training from the paired labels from different modalities. In this context, we raise a pivotal question: Can a model with one modality synergize the training of other models with the different modalities, even without the paired multimodal labels? Our answer is 'Yes'. As a figurative description, we argue that a writer, i.e., a language model, can promote the training of a painter, i.e., a visual model, even without the paired ground truth of text and image. We theoretically argue that a superior representation can be achieved by the synergy between two different modalities without paired supervision. As proofs of concept, we broadly confirm the considerable performance gains from the synergy among visual, language, and audio models. From a theoretical viewpoint, we first establish a mathematical foundation of the synergy between two different modality models, where each one is trained with its own modality. From a practical viewpoint, our work aims to broaden the scope of multimodal learning to encompass the synergistic usage of single-modality models, relieving a strong limitation of paired supervision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to answer whether imperfectly aligned paired data from other modalities can help learning in a multimodal setting.
Specifically, the authors propose an additional latent loss, to directly align the target modalities' latent representation with that of the output of a pre-trained encoder of the secondary (supportive) modality. The authors introduce and study a theoretical framework and show that even imperfect paired data can help approximate a hypothetical, perfectly aligned representation. They further demonstrate empirically that the additional latent loss led to stronger performance of the target modalities' encoder across various tasks and modalities.

### Strengths
The work considers a range of relevant modalities and conducts experiments across language, vision, and audio in various cross-combinations.
The mathematical framework introduced is intuitive and easy to follow.

### Weaknesses
The paper asserts in multiple locations that prevailing multimodal learning methods require "perfectly paired datasets" (quote from the introduction) between modalities. This, in my opinion, is not accurate an accurate representation of the thinking in the field. The authors cite CLIP as a notable multimodal model, which famously is trained on noisy web-scale paired data in the form of image alt text. Training multimodal models on noisy labels such as alt-text from web-scraped images is common practice and widely established (Radford et al. 2021, Dosovitskiy et al. 2020.,...). While improving the alignment of the training modalities is generally seen as desirable (e.g. Fang et al., 2023), "perfection" seems not a requirement.
The paper does not cite and / or discuss other works in the space of aligning multiple modalities without direct paired supervision data, including popular works such as ImageBind (Girdhar, et al., 2023) or 4M (Mizrahi et al., 2024). These works do not (solely) rely on paired multimodal data, seemingly directly addressing the limitations discussed by this work in section 2.3.
This, together with arguably understating how much alignment on noisily paired data has been previously studied in the field, arguably limits the novelty of this work.

One of the main statements of this work is that the label does not need to be perfectly paired / can be noisy. However, the transformations to introduce this noise studied in the work may not be sufficiently realistic. For example for the L -> V case, the noisy label \hat z^j is constructed by embedding the text "This is about (Class|Emotion) #." as per table 5. In terms of the measured downstream task, which is classification, this label is arguably not noisy, but perfectly represents the target task. In table 4 it is shown that changing this supervision signal with a caption produced by LLaVA leads to only minor improvement, which may not be surprising in this setting. (See the Questions section for suggestions around this.)

### Questions
Regarding Remark 2.1. "δ does not hinder the synergy", you say that
"We can extract an imperfect feature representation from Pj by giving
imperfect input to the modality Mj . This allows ˆzj exist in the distribution Pj 2. Consequently, ˆzj
is closer to or part of the latent space of the Mj than to that of the Mi or the true latent space."

Wouldn't this quite directly depend on how far \hat P_j is from P_j, as well as how aligned P_i is to P_j to begin with? Surely one could construct counter examples with adversarially chosen δ? This may not be much of a practical concern for reasonably close \hat P_j but is this statement not a bit strong in the general case?
Expanding on this, perhaps this could be empirically verified by exploring different levels of noise to introduce in \hat z^j, particularly in the L -> V task as suggested above. Have you perhaps already considered / explored different noising functions and compared their impact?

For the V -> A case in AVMNIST, you say "For the [V→A] case with AVMNIST, we use randomly shuffled images from AVMNIST as ˆzj in audio classification tasks". Could you clarify the random sampling in this case? Is it a random image from the entire dataset or a random image from the samples of the same target class? If it is a random image (i.e. unrelated to the paired modality at all), this seems significantly more "noise" than in other settings, it'd be great to understand a bit better to understand the motivation for this choice and perhaps similar experiments for other modalities.

On a general level, if we assume that the target distribution for a modality encoder g_i is similar to the one of a pre-trained encoder g_j of a different modality, the proposed latent alignment loss has some similarity to knowledge distillation. In this field there's been some notable prior work that suggests that the success of KD is partially attributable not only to a superior knowledge of the teacher but also to benefits of the training strategy itself. Notably, Born Again Networks (Furlanello et al., 2018) suggests a simple strategy of self-distillation can improve performance. Yuan Li et a., 2020 explores this further in "Revisiting Knowledge Distillation via Label Smoothing Regularization". This is relevant to this work since it could suggest a different mechanism leading to the empirically observed improvements that is less about multimodal transfer and perhaps more about a sort of regularization effect of the added latent loss. Has this been considered?

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
4

### Summary
This paper investigates whether one modality model can enhance the training of another modality model without requiring paired multimodal supervision. The authors propose both theoretical and empirical evidence that imperfect supervision from one modality (e.g., language) can improve the performance of another modality (e.g., vision). They establish mathematical foundations showing that an interpolated representation between two modalities can outperform single-modality representations, even with imperfect cross-modal supervision. The work is validated through extensive experiments across vision, language and audio modalities, demonstrating consistent performance improvements. For example, in the vision domain, they show improvements of 1.5-2.5% on ImageNet classification and similar gains on robustness benchmarks by leveraging simple language prompts during training.

### Strengths
- Novel insights: The work challenges common assumptions about requiring paired supervision for multimodal learning and demonstrates unexpected improvements using single-modality pre-training and synergies between seemingly unrelated modalities.

- Strong theoretical foundation: The paper provides rigorous mathematical proofs for how and why cross-modal learning can work without paired supervision, establishing bounds on the interpolation coefficient $\alpha$ and showing the existence of superior interpolated representations.

- Comprehensive empirical validation: The authors demonstrate their approach across multiple modality pairs (Vision-Language, Vision-Audio, Language-Audio) and various architectures, showing consistent improvements across different settings and tasks. Results include not just standard classification metrics but also out-of-distribution generalization and robustness benchmarks, showing broad improvements across different evaluation criteria.

### Weaknesses
 - Other language supervision: The language prompts used (e.g., "This is about Class #") are quite basic. It would be interesting to see how the method performs with more complex or varied language supervision.

- Theoretical assumptions: Some theoretical assumptions (e.g., Assumption 1 about $\Delta_{ij} \ge  0$) could benefit from more empirical validation or discussion of when they might not hold.

### Questions
- Figure 2 right, $Z_i$ should be $Z_j$.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper demonstrates that performance on a target modality can be improved by leveraging another modality, even without paired samples. Both theoretical and empirical evidence are provided to support this claim, showcasing the method's effectiveness.

### Strengths
* The paper tackles an important problem: obtaining paired data is often challenging in many setups.
* The approach is backed by both theoretical analysis and empirical results, showing clear improvements over baseline methods.
* The paper is well-structured, with illustrations that help clarify key messages.

### Weaknesses
 * The main contribution—showing that using an unpaired modality can improve performance—has already been explored in prior works. For instance, some studies demonstrate leveraging unpaired modalities through pretraining on one modality and fine-tuning on another, like from image to video to audio [1], or from text to image-text [2]. Additionally, the issue of handling unpaired or missing modalities has been addressed before, yet the paper does not discuss relevant works in this domain [3,4,5]. Including this discussion would better position the paper.

* It is not clear why the author decides to leverage other modality through an l2 loss between the features spaces. Other design choices can  be explored. For example, concatenation, addition or other multimodal features fusion techniques. The use of an auxiliary loss might not be the only way to leverage other modalities, and the paper lacks a convincing theoretical or empirical justification for this specific choice.

* The experiments use relatively small models on classification tasks. It remains unclear whether the proposed method would be effective on larger, more complex, maybe generative models (e.g., Multimodal LLMs, CLIP). The paper does not provide sufficient evidence to support the scalability of the approach to more complex architectures.

### Questions
Please check the weaknesses section, in particular the question about how leveraging other modalities is done.

### Soundness
3

### Presentation
4

### Contribution
2
