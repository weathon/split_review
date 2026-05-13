# Ceci n'est pas une pomme: Adversarial Illusions in Multi-Modal Embeddings

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Multi-modal embeddings encode images, sounds, texts, videos, etc. into a single embedding space, aligning representations across modalities (e.g., associate an image of a dog with a barking sound).  We show that multi-modal embeddings can be vulnerable to an attack we call ``adversarial illusions.''  Given an image or a sound, an adversary can perturb it so as to make its embedding close to an arbitrary, adversary-chosen input in another modality. This enables the adversary to align any image and any sound with any text.  

Adversarial illusions exploit proximity in the embedding space and are thus agnostic to downstream tasks.  Using ImageBind embeddings, we demonstrate how adversarially aligned inputs, generated without knowledge of specific downstream tasks, mislead image generation, text generation, and zero-shot classification.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies adversarial attacks for images and audio using multimodal embeddings. The method builds upon a pretrained multimodal embedding model such as ImageBind, and can be used to attack downstream models that also use this model as the embedding model. Given an image/audio and an adversarial text, the adversarial attack is applied to the image/audio space to maximize the cosine similarity between the image/audio embedding and the adversarial text embedding. Experiments show that adversarial examples can fool downstream tasks that use the same embedding model.

### Strengths
1. Experiments include image attacks and audio attacks, which are more comprehensive than previous works that mostly experiment with one modality.
2. The paper is well-written.

### Weaknesses
1. The downstream task uses exactly the same embedding model as the one being attacked. Therefore, it is not surprising that they can be fooled. It would be more interesting if some unexpected findings/insights were provided. Specifically, the paper lacks a thorough investigation into the transferability of the adversarial examples to other models or tasks that utilize similar but not identical embeddings. The current setup, where the attack and evaluation are performed on the same model, provides limited insight into the practical implications of the proposed method. It is crucial to demonstrate that the adversarial examples can generalize beyond the specific model used for attack generation.
2. As the authors acknowledged, several existing papers have studied adversarial attacks for multimodal learning (e.g., for CLIP and for multimodal large language models). More thorough comparisons with the previous works should be done. The paper should include a more detailed discussion of how the proposed method differs from existing adversarial attack techniques, particularly those targeting similar multimodal models. A more comprehensive comparison should highlight the novelty and advantages of the proposed approach.

### Questions
How robust is the attack to adversarial defense?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper demonstrates that the semantic meaning of multi-modal embeddings can be easily manipulated using a simple white-box attack, which is termed adversarial illusion. An attacker only needs to describe in text what they want the input data to mean, and the multi-modal model ImageBind will interpret the attacked but seemingly normal images or audio as conveying the attacker's intended meaning, resulting in cross-modal illusions. This causes ImageBind to make mistakes on downstream tasks even without knowing what these tasks are.

### Strengths
- This paper's approach to cross-modal adversarial attacks on images, audio, and text is quite novel.
- The discovery that multi-modal embeddings can be aligned to a target input arbitrarily chosen by an attacker is interesting.
- The paper is mostly well-written and well-organized.

### Weaknesses
The main weakness of this paper is the incompleteness of the experiments. There's a lack of experiments involving other models, and the variety of experimental tasks is insufficient. Therefore, I give a 5-point rating initially.
- Using just one multi-modal model, ImageBind, in the experiments to demonstrate that “multi-modal embeddings can be vulnerable to an attack” may be somewhat insufficient. Conducting experiments on AudioCLIP[1], another contrastively pre-trained multi-modal model, would make the claim more convincing.
- Regarding using ImageBind in the experiments, more experiments, e.g. audio classification, image-to-text retrieval, and audio-to-video retrieval, could have been done to strengthen the claim.



### Questions
- I'm uncertain about why black-box attacks cannot be applied in this context. For instance, images and mel spectrograms can still be misclassified into the target input by introducing specific noises calculated by SimBA[2]. Some further clarification regarding the limitations or inapplicability of black-box attacks in this context would be helpful.
- Are the other white-box attacks as effective as I-FGSM in performing adversarial illusions?
- The experiments are conducted using ImageBind, a model that is contrastively pre-trained and projects all modality data into an image embedding space. If ImageBind were replaced with a multi-modal model like ChatBridge[3], which is not contrastively pre-trained and projects all modality data into a text embedding space, would this still demonstrate the vulnerability of multi-modal embeddings to the adversarial illusion attack?
- In Figure 5, could you please clarify why the target input, a sheep image, is encoded by a text encoder rather than an image encoder?
- (Minor) Is the I-FGSM formula complete? I think a clipping operation is missing in it.
- (Minor) I find it a bit confusing whether unCLIP can be used as a generative model. In the "Downstream models" section of Section 2, the paper mentions that "diffusion models that operate on CLIP embeddings, e.g., unCLIP, can also operate on ImageBind embeddings." However, in Section 6, the paper also notes that BindDiffusion, which employs the unCLIP model, struggles to generate images from the multi-modal embeddings. Some clarification on this apparent discrepancy would be appreciated.

[2] Chuan Guo, Jacob R. Gardner, Yurong You, Andrew Gordon Wilson, Kilian Q. Weinberger. Simple Black-box Adversarial Attacks. ICML 2019.  
[3] Zijia Zhao, Longteng Guo, Tongtian Yue, Sihan Chen, Shuai Shao, Xinxin Zhu, Zehuan Yuan, Jing Liu. ChatBridge: Bridging Modalities with Large Language Model as a Language Catalyst. arXiv:2305.16103.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a new attack called "adversarial illusions" against multi-modal embedding models like ImageBind. These models embed inputs like images, text, and audio into a shared embedding space. The attack involves making small perturbations to an input, like an image, so that its embedding becomes very close to a completely different, adversary-chosen input in another modality, like text. This fools downstream tasks relying on the embeddings, as they now interpret the perturbed input based on the adversary's target instead of the original semantics. Experiments demonstrate the effectiveness of the attack. The authors also discuss potential defenses like adversarial training and certifications. Overall, the work demonstrates serious vulnerabilities in cross-modal alignment of current multi-modal embeddings.

### Strengths
This proposes adversarial illusions that are attacks for multimodal embedding models. Given the growing popularity of multi-modal models, this line of research is important and interesting. The idea to adversarially associate a modality with another one unrelated to the semantic of the input is interesting.

### Weaknesses
While the paper is interesting and this first version is decent, there are a lot of missing experiments that could strengthen the paper and better motivate certain choices: 

- The paper proposes to use the I-FGSM attack to create their adversarial illusions:
	- Why use I-FGSM and not PGD, which is the best-known and better attack? 
	- The authors could also experiment with DiffPGD, a newer PGD attack based on the diffusion model [1]. The adversarial perturbation is really visible in Figure 7, leveraging diffusion models could improve the attack. 
	- Why using the $\ell_\infty$ norm? Have the authors experimented with other norms (e.g. $\ell_2$)?

- The authors seem to have experimented only with cross-modality? Can the authors create adversarial illusions on the same modality? 
- Is it possible to investigate the transferability of the attack?  e.g. against other multimodal foundation models? 
- The authors seem to be experimenting only with targeted attacks. Would it be possible to maximize the following loss: 
$$
\ell = 1 - \cos\left( \theta^{m_1}(x^{m_1}+\delta), \theta^{m_1}(x^{m_1}) \right)
$$


**Other comments:**
- What is the difference between figures 1,3,4,5? It seems only the modality and examples are different. These figures take up a lot of space in the paper, I think these figures could be reduced or some of them could be put in the appendix to leave space for further experiments. 
- The authors devote a whole section to countermeasures, but it seems that they do not do any experiments. If the authors focus so much on countermeasures, some experiments should be done.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use adversarial perturbation to align the perturbed image with a given target text/sound.

### Strengths
- This paper studies the vulnerability of multi-modal embedding.
- The experiments also cover the acoustic information.

### Weaknesses
 - The literature is not well-surveyed, which makes the novelty of the attack not convincing. For example, BadEncoder (S&P'22) already implements such an idea to attack the CLIP model. There are also many following works which cite BadEncoder and study the vulnerability of multi-modal embeddings. How do the authors position the novelty of this work in these literatures? Specifically, the paper lacks a detailed discussion of how the proposed adversarial perturbation method differs from existing techniques, especially those that focus on manipulating embeddings in multi-modal spaces. It is not clear if the proposed method offers any advantages in terms of attack success rate, perturbation magnitude, or computational efficiency compared to these prior works. The paper should also clarify whether the attack is targeted or untargeted, and how this impacts the evaluation and comparison with other attacks.

### Questions
Please see the weakness part above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
