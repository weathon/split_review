# Rethinking and Defending Protective Perturbation in Personalized Diffusion Models

- Decision: Reject
- Scores: 6, 8, 6, 3

## Abstract
Personalized diffusion models (PDMs) have become prominent for adapting pretrained text-to-image models to generate images of specific subjects using minimal training data. However, PDMs are susceptible to minor adversarial perturbations, leading to significant degradation when fine-tuned on corrupted datasets. These vulnerabilities are exploited to create protective perturbations that prevent unauthorized image generation. Existing purification methods attempt to mitigate this issue but often over-purify images, resulting in information loss. In this work, we conduct an in-depth analysis of the fine-tuning process of PDMs through the lens of shortcut learning. We hypothesize and empirically demonstrate that adversarial perturbations induce a latent-space misalignment between images and their text prompts in the CLIP embedding space. This misalignment causes the model to erroneously associate noisy patterns with unique identifiers during fine-tuning, resulting in poor generalization. Based on these insights, we propose a systematic defense framework that includes data purification and contrastive decoupling learning. We first employ off-the-shelf image restoration techniques to realign images with their original semantic meanings in latent space. Then, we introduce contrastive decoupling learning with noise tokens to decouple the learning of personalized concepts from spurious noise patterns. Our study not only uncovers fundamental shortcut learning vulnerabilities in PDMs but also provides a comprehensive evaluation framework for developing stronger protection. Our extensive evaluation demonstrates its superiority over existing purification methods and stronger robustness against adaptive perturbation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to improve the personalization performance of Diffusion Models on images with protective perturbation, a kind of noise avoiding images to be learned by models. The authors fist empirically analyze the latent mismatch between the perturbed and original images, finding that perturbation significantly alternate the latent representations of images. The authors believe that the mismatch causes shortcut learning and therefore fail the personalization of diffusion models on such perturbed data. Therefore, a novel method is proposed to improve the personalization training by contrastive learning and super resolution.

### Strengths
1. The proposed contrastive learning method is well motivated by the empirical finding on the latent mismatch of perturbed images.
2. In multiple domains, the method presents better fine-tuning performance than baselines given protective perturbation on images.
3. Comprehensive experiments are conducted to understand and evaluate the method.

### Weaknesses
1. It is not clear to me the connection between the latent mismatch and the shortcut learning. Why does the existence of latent mismatch lead to shortcut learning? 
2. I don't think the word "defending" (in the title) should be used against a good technique, protective perturbation. The paper is a good red-teaming paper that explored a stronger threat model for protective perturbation. Unfortunately, many description of the method is defined as a mitigation method, which could mislead the readers about the negative impacts of the methods. The authors should discuss how this method can break the existing protective perturbation. It would be appreciated if the authors can discuss potential solutions toward better copyright protection via protective perturbation or other alternatives.

### Questions
* It is not clear to me the connection between the latent mismatch and the shortcut learning. Why does the existence of latent mismatch lead to shortcut learning? 
* What are the potential mitigation against to the proposed method?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper uncovers and validates the underlying mechanism by which adversarial perturbations disturb the fine-tuning of personalized diffusion models by latent-space image-text misalignment. Then, it introduces a systematic defense framework that mitigates the misalignment with data purification and contrastive decoupled learning and sampling.

### Strengths
- This paper finds that adversarial perturbation leads to latent image-text mismatch and provides an explanation from the perspective of shortcut learning. Their analysis contributes to the further development of protective perturbation in personalized diffusion models.
  
- The proposed framework provides a system-level defense covering data purification, model training, and sampling strategy. Compared with previous data transformation and diffusion-based methods, the proposed method achieves the best semantic and image quality restoration.

### Weaknesses
 - In Table I, the authors would better add a setting that the clean images are processed by the proposed and baseline methods. This would provide a clearer understanding of the impact of the proposed method on unperturbed data and establish a baseline performance for comparison. Specifically, it would be beneficial to see how much the proposed data purification and contrastive decoupled learning and sampling alter the original clean images, allowing for a more comprehensive evaluation of the method's overall effect.

- In Table II, why only calculate the time for data purification? Will CDL incur additional time costs? It is crucial to understand the complete computational overhead of the proposed framework. The omission of the time cost for contrastive decoupled learning (CDL) raises concerns about the practical applicability of the method, especially in resource-constrained environments. A breakdown of the time costs for each component of the framework, including data purification, CDL training, and sampling, is necessary for a thorough evaluation.

### Questions
Please help to check weaknesses.

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
The paper conduct a comprehensive analysis to show that perturbations induce a latent-space misalignment between images and their text prompts in the CLIP embedding space, which leads to association between the noise patterns and the identifiers. Based on this observation, the paper introduces contrastive decoupling learning with noise tokens to decouple the learning of personalized concepts from spurious noise patterns.

### Strengths
1. The observation that adversarial perturbations induce a latent-space misalignment between images and their text prompts in the CLIP embedding space is interesting and insightful.

2. The paper is well-organized and easy-to-follow.

3. The paper conducts an extensive array of experiments and also considers adaptive perturbation.

### Weaknesses
1. The paper does not provide strong theoretical analysis to support the conclusions.

2. The technical contribution is a little limited since Decoupled Contrastive Learning is not a new technique proposed by the paper.

### Questions
I am wondering if the noisy images generated by DM without any defense can be denoised?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes viewing the fine-tuning process of Personalized Diffusion Models (PDMs) through the lens of shortcut learning, using causal analysis as motivation. The authors then introduce a defense framework designed to enable the model to correctly associate images with their original semantic meanings.

### Strengths
The paper provides preliminary experiments on CLIP, which help demonstrate the authors' ideas.
Personalized diffusion models present an interesting area for further exploration.

### Weaknesses
1. The paper lacks overall coherence, with some sections difficult to follow and, in some cases, contradictory. Additionally, several terms and graphs are missing clear definitions and explanations.

    1. Are "adversarial perturbations" and "protective perturbations" intended to be the same concept? The author seems to use these terms interchangeably; if they differ, please clarify each term carefully.
    2. In the introduction, the author presents multiple related works. It may be helpful to focus on those most relevant to the paper’s main motivation. Additionally, certain terms, such as "purification studies," would benefit from brief explanations—similar to the way "image purifications" is introduced on line 142.
    3. Several equations need further explanation, such as those on lines 178-179, regarding the function of an instance dataset and a class dataset. Additionally, the meaning of "r" on line 208 is unclear.

2.After reading the entire paper, I found it challenging to identify the specific question the author aims to address and the associated motivations. While the introduction attempts to outline these points, it is difficult to discern the relationship between the motivation and the problem being addressed. Additionally, there appears to be a disconnect between the problem definition in the introduction and the methods presented. Here are some specific suggestions for clarification:

    1. The introduction states, “The model trained on perturbed data will generate images that are poor in quality, and thus, unauthorized fine-tuning fails.” Does this imply that generating low-quality images of private content protects copyright and privacy? If so, why does the proposed method focus on enhancing image clarity for private content while defining it as a defense?
    2.The author mentions that shortcuts are key to avoiding the generation of private personal images. Given this, why does the method seem to eliminate these shortcuts?
    3.On line 46, adversarial perturbations are suggested as a means to protect users’ images from unauthorized personalized synthesis. However, line 100 describes an intention to "defend against" this. Could you clarify?
    4.Additionally, the highlighted question in the introduction, “How to design an effective, efficient, and faithful purification approach is still an open question,” lacks context. Although there is a mention of “Moreover, purification studies are also purposed to further break those protections” in the following sentence, there are no subsequent explanations, particularly concerning how this question connects with the paragraph's earlier discussion.
    5. In the end of introduction, it seems that the authors propose a new purify methods, "Our approach conducts comprehensive purification from three perspectives, including input image purification, contrastive decoupling learning with the negative token, and quality-enhanced sampling....". However, in the methods, the author says they propose a method to address the short cut learning...., which is a little bit confusing.

3. Minor: Although viewing fine-tuning from a causal effect and shortcut learning perspective is novel, it shares similarities with backdoor attacks. In the backdoor attack literature, several papers have employed causal graphs to analyze shortcut mechanisms.[1-3]

4. The causal graph is underexplained and possibly contains ambiguities. For example, the definitions of $\bar{C}$ and $\bar{x_o}$ are missing. While a brief introduction to the construction of the graph is provided, explanations of each node’s meaning and the meaning of the arrows are absent. Given that the causal graph is a key contribution, adding a paragraph to introduce and explain it in detail would be beneficial. The term "spurious path" may also be misapplied; in causal inference, this usually refers to a backdoor path between treatment and outcome. Since this doesn’t apply here, either avoid the term or define it within the paper’s context.

5. The causal graph may need structural revision. In causal inference, an arrow between A and B signifies that A causes B. However, in this graph, it seems that an arrow signifies containment rather than causation. I would suggest adhering closely to causal inference conventions and adjusting the graph accordingly.

### Questions
See weakness

### Soundness
2

### Presentation
1

### Contribution
2
