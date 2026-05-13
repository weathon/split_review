# TUAP: Targeted Universal Adversarial Perturbations for CLIP

- Decision: Reject
- Scores: 3, 3, 3, 8

## Abstract
As Contrastive Language-Image Pretraining (CLIP) models are increasingly adopted in a wide range of downstream tasks and large Vision-Language Models (VLMs), their vulnerability to adversarial attacks has attracted growing attention. In this work, we examine the susceptibility of CLIP models to Universal Adversarial Perturbations (UAPs). Unlike existing works that focus on untargeted attacks in a white-box setting, we investigate targeted UAPs (TUAPs) in a black-box setting, with a particular emphasis on transferability. In TUAP, the adversary can specify a targeted adversarial text description and generate a universal $L_{\infty}$-norm-bounded or $L_2$-norm perturbation or a small unrestricted patch, using an ensemble of surrogate CLIP encoders. When TUAP is applied to different test images, it can mislead the image encoder of unseen CLIP models into producing image embeddings that are consistently close to the adversarial target text embedding. We conduct comprehensive experiments to demonstrate the effectiveness and transferability of TUAPs. This universal transferability extends not only across different datasets and models but also to downstream models, such as large VLMs including OpenFlamingo, LLaVA, MiniGPT-4 and BLIP2. TUAP can mislead them into generating responses that contain text descriptions specified by the adversaries. Our findings reveal a universal vulnerability in CLIP models to targeted adversarial attacks, emphasizing the need for effective countermeasures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
This work explores the vulnerability of CLIP models to targeted Universal Adversarial Perturbations (TUAPs) in a black-box setting, focusing on transferability. TUAPs enable adversaries to specify a targeted text description and generate universal perturbations that mislead unseen CLIP models into producing embeddings aligned with the adversarial text. Experiments demonstrate the effectiveness and transferability of TUAPs across various datasets and large Vision-Language Models (VLMs) like OpenFlamingo and MiniGPT-4. The findings highlight a significant vulnerability in CLIP models to targeted attacks, underscoring the need for effective countermeasures.

### Strengths
Strengths.
1. The paper is clearly written and motivates the proposed approach well in a lucid manner.
2. The paper demonstrates universal transferability across different datasets and various Vision-Language Models (VLMs), consistently misleading image encoders.
3. The paper proposes a targeted Universal Adversarial Perturbations (TUAPs) method. The proposed TUAPs allow adversaries to specify precise text descriptions for targeted attacks while functioning effectively in a black-box setting.
4. The paper highlights significant vulnerabilities in CLIP models, underscoring the need for improved defenses against targeted adversarial attacks.

### Weaknesses
Weaknesses

1. The novelty, in my opinion, is limited. This paper simply migrates the Universal Adversarial Perturbations generation method in image classification to the VLM task, and there is no technical innovation.


2.  Lack of comparison with Universal Adversarial Attack methods for VLM models[1][2]. They have proposed to adopt the image encoder to generate adversarial perturbations. 


3. How does the proposed method perform on closed-source models such as chatgpt4?


4. In Figure 1, there are apparent shark textures in the generated adversarial images, and I think there is no problem for VLM to identify them as sharks.

### Questions
Refer to Weaknesses.

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
5

### Summary
This paper proposes the first targeted UAP attack against VLP models and conducts extensive experiments across various tasks and models. By specifying a targeted adversarial text description, TUAP is able to generate a universal L_{inf} norm-bounded or L_{2}-norm perturbation or a small unrestricted patch, exhibiting outstanding transferability.
Besides, the ensemble of surrogate CLIP encoders further enhances the attack effects.

### Strengths
(1) The authors provide sufficient experiments on diverse downstream tasks and models, showing the efficacy of the proposed TUAP.
(2) The tables are in good format.
(3) The experimental analysis is reasonable and convincing.
(4) Visualization results are intuitive and reveal that TUAP successfully achieves the attack.

### Weaknesses
 (1) My major concern is that this paper provides no significant technical innovation. Specifically, the proposed method makes an intuitive attempt by simply combining existing techniques from former studies of adversarial attacks, lacking in-depth exploration and novel insights into vulnerabilities of VLP models against UAP.  
(2) The introduction section requires further reformulation to reduce the unnecessary space.
(3) Despite the extensive experiments, I do not see any insightful analysis regarding the underlying mechanism of the attack algorithm.  

While the authors have conducted sufficient experiments, no significant contributions are made compared with [1].
In summary, this paper is more like an experimental report rather than a top-tier conference paper, far from meeting the acceptance criteria for ICLR.

### Questions
Did you train the universal perturbation with the whole training set of the surrogate model?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a universal adversarial perturbation method against CLIP and its variants. Unlike previous white-box untargeted attacks against CLIP. This paper focus on a black-box targeted setting based on the transferability of adversarial examples. Experiments across diverse datasets and settings are conducted.

### Strengths
1. This paper is generally well organized.
2. The experiments are comprehensive. The authors have provided analyses across diverse scenarios.
3. The introduction of background knowledge is comprehensive.

### Weaknesses
1. This idea is trivial and not so novel. Universal adversarial attacks have been well explored in the context of standard adversarial attacks for single-modal architectures. It seems that the authors do not make any specific designs to transfer it into the vision-language models. According to the pseudocode, the proposed method seems to be a general approach for all the architectures but not specific to CLIP models.

2. The authors should also explore some related works [a, b] that apply black-box attacks based on transferability for a more comprehensive comparison analysis.

### Questions
1. Can the authors provide some comparisons with query-based black-box attack approaches?
2. Can the novel designs for attacking CLIP models be shown?
3. In addition to adversarial images, is it possible to generate universal adversarial texts?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces TUAP, a new method for crafting universal perturbations for specific outputs in the CLIP model in a black-box setting. TUAP aims to generate perturbations that, when universally applied to images, guide CLIP's image encoder to achieve predetermined adversarial text embeddings.

### Strengths
1. The paper explores the targeted universal adversarial perturbation (TUAP) for the CLIP model in a black-box setting, and shows that TUAP can still achieve efficient attack effects in unseen models without gradient information. By combining multiple alternative models for perturbation generation, the transferability of the attack is improved.
2. Unrestricted adversarial patches, $L_{\infty}$ norm-constrained perturbations, and $L_{2}$ norm-constrained perturbations provide users with flexibility to choose appropriate perturbation forms in different scenarios. This diversity not only enhances the applicability of the method, but also demonstrates the performance of TUAP under various constraints, which is suitable for adversarial needs in various scenarios.
3. The paper experimentally verifies TUAP on 9 datasets and multiple downstream tasks, covering tasks such as image-text retrieval, zero-shot classification, and image description generation. Through diverse datasets (such as ImageNet, CIFAR, and Food101, etc.) and task tests, the paper demonstrates the applicability of TUAP in different tasks and its wide range of attack effects.

### Weaknesses
1. The paper discusses the attack effects on a variety of target text descriptions, but the targeted support for the diversity of target texts and actual scenarios is relatively limited. The lack of in-depth analysis of target texts that may have complex semantics or contextual dependencies in reality limits the applicability of this method in practical applications. Specifically, the paper does not explore how the method performs when the target text involves negation, conditional statements, or nuanced emotional tones, which are common in real-world scenarios. Furthermore, the selection of only 10 target sentences may not be sufficient to capture the full spectrum of potential adversarial targets.
2. The paper focuses on the success rate and transitivity of the attack, but ignores the visual perceptibility of adversarial perturbations. Especially under $L_{\infty}$ and $L_{2}$ constraints, perturbations may produce visible artifacts, affecting the concealment of practical applications. In real application scenarios, perceptible perturbations may be easily discovered by the detection system, thereby limiting the effectiveness of the attack. The paper lacks a quantitative analysis of the structural similarity or perceptual distance between the original and perturbed images, making it difficult to assess the practical stealth of the attack.
3. There are some ablation experiments on different perturbation parameters in the paper, but the sensitivity analysis of key parameters such as perturbation intensity and perturbation position is not comprehensive enough. In particular, how the perturbation intensity of the $L_{\infty}$ constraint affects the concealment and transitivity of the attack, and the impact of the change in the position of the perturbation at the edge or main area of ​​the image on the success rate of the attack, has not been fully discussed. The paper should explore a wider range of perturbation intensities and locations, and analyze the trade-offs between attack success, perturbation imperceptibility, and transferability.
4. The experiments are mainly conducted on more typical datasets such as ImageNet, which may not fully reflect the complexity of real application scenarios. For example, the feature representation of CLIP may be significantly different in images in specific fields such as outdoor scenes or medical images, and there is a lack of verification of the attack effect in these specific fields. The paper should include experiments on datasets with more complex and diverse image content, such as those found in remote sensing, surveillance, or medical imaging, to better assess the generalizability of the proposed method.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
