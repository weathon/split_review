# SingleInsert: Inserting New Concepts from a Single Image into Text-to-Image Models for Flexible Editing

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Recent progress in text-to-image (T2I) models enables high-quality image generation with flexible textual control. To utilize the abundant visual priors in the off-the-shelf T2I models, a series of methods try to invert an image to proper embedding that aligns with the semantic space of the T2I model. However, these image-to-text (I2T) inversion methods typically need multiple source images containing the same concept or struggle with the imbalance between editing flexibility and visual fidelity. In this work, we point out that the critical problem lies in the foreground-background entanglement when learning an intended concept, and propose a simple and effective baseline for single-image I2T inversion, named SingleInsert. SingleInsert adopts a two-stage scheme. In the first stage, we regulate the learned embedding to concentrate on the foreground area without being associated with the irrelevant background. In the second stage, we finetune the T2I model for better visual resemblance and devise a semantic loss to prevent the \textit{language drift} problem. With the proposed techniques, SingleInsert excels in single concept generation with high visual fidelity while allowing flexible editing. Additionally, SingleInsert can perform single-image novel view synthesis and multiple concepts composition without requiring joint training. To facilitate evaluation, we design an editing prompt list and introduce a metric named Editing Success Rate (ESR) for quantitative assessment of editing flexibility. Our project page is: \href{https://jarrentwu1031.io/SingleInsert-web/}{\textcolor{magenta}{https://jarrentwu1031.io/SingleInsert-web/}}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a two-stage Diffusion-based Image-to-Text Inversion algorithm that can mitigate overfitting when training with a single source image. It applies constraints to suppress the inversion of undesired background and the problem of language drift. Segmentation masks for foreground and background and predictions from the original diffusion model conditioned on the class of inversed concept are utilized to form the regularizations. It also designs an editing prompt list to quantitatively evaluate the edit flexibility of the inversed concept. With the proposed algorithm, in the non-trivial single-source-image scenario, this work achieves both high visual fidelity and editing flexibility, enabling novel view synthesis and multiple inversed concepts composition without joint training.

### Strengths
(1) The method allows more flexible ediitng for the inversed concepts from a single image, surpassing its baselines.
(2) The method presents a novel way to regularize the Image-to-Text Inversion process with predicted distributions by the original model.
(3) The paper presents an ediitng prompt list and a metric for quantitative evaluation of editing flexibility of inversed concepts.
(4) The paper clearly illustrates the motivations and the designs of the new proposed loss functions.
(5) The ablation studies clearly presents the value of each design of the proposed method.

### Weaknesses
 (1) In section 4.4, the authors claim that the proposed approach enables single-image novel view synthesis. However, the experiments on this point are quite weak. Firstly, the algorithm cannot accurately control the viewpoint angle but can only control the view with text prompts "left side", "frontal", and "back side". Secondly, no evidence is provided to demonstrate how this constitutes an advancement compared to previous work on previous approaches. Thirdly, the generated novel view images also have drastic change on the background and even foreground appearance, which does not meet the requirement of novel view synthesis. Thus, I doubt that the claim of this contribution is not grounded.
(2) The application scenario of multiple concept composition is only demonstrated with a few examples but without comparison to previous work.
(3) On P6, section 4.1, a brief, if not detailed, introduction about the proposed metric ESR and the editing prompt list is expected to be given. The readers are supposed to have the basic idea about what is done in this evaluation after reading this section, instead of having to read the supplemental file to grasp it.

### Questions
(1) The proposed algorithm in this paper does not have a design specified for the single-source-image scenario and achieves single-source-image scenario by finetuning a large number of parameters, i.e. the whole T2I model and a ViT-B image encoder. So it would be natural to expect that the good performances generalize to the multiple-source-image scenario. Have you tried using the proposed algorithm for the multiple source-image inversion?
(2) Please refer to the questions in the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new method for customized text-to-image generation, which considers disentanglement in learning the concept contained in user-provided image.

### Strengths
The proposed method tries to disentangle the influence of foreground and background in the given image, which is reasonable and straightforward.

Good results are presented in the paper, compared to related baselines.

Ablation studies are conducted, which help readers better understand the proposed method.

### Weaknesses
The proposed method seems to require more fine-tuning time compared to some related works (E4T only requires 5~15 steps, the proposed method requires 100 steps which is mentioned in section 4.1).

The idea of disentangling the foreground and background information has also been exploit in related works [1, 2]. Some of the related work have code publicly available online [2], but are not compared in this paper's experiments.

In quantitative evaluation, the authors didn't follow the setting in Dreambooth [3] to test the proposed methods on objects comprehensively. Specifically, the prompts used in the paper, on both human face and objects domain, may not be comprehensive enough. Dreambench proposed in [3] contains recontextualization, accessorization, and property modification prompts. On the contrary, example prompts shown in the paper are less comprehensive. Thus more comparisons are suggested.

Some related works also work on similar task with related ideas, which are suggested to be discussed in the paper.

### Questions
Can the authors provide more details about the data they collected from the web? Specifically, do those data consist of common object, human face, or both? What is the number of the collected samples?

In the fine-tuning stage, because a frozen T2I model is also used, how much extra memory do we need compared to the scenario without this model (both under LoRA setting).

Have the authors considered pre-training the model on a large-scale dataset? Will it reduce the fine-tuning time on testing images?

The author mentioned number of iterations needed, what is the actual total time needed in terms of seconds/minutes for customizing a new testing image?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This research addresses challenges in image-to-text (I2T) inversion and proposes "SingleInsert," a two-stage method that effectively separates foreground and background in learned embeddings. It enhances visual fidelity and flexibility in single-image concept generation, novel view synthesis, and multiple concept composition without joint training. The paper introduces the Editing Success Rate (ESR) metric for quantitative assessment of editing flexibility.

### Strengths
The paper is very easy to follow.

### Weaknesses
1. This paper seems to miss many related works or baselines.

- Taming encoder for zero fine-tuning image customization with text-to-image diffusion models [1].

- InstantBooth: Personalized Text-to-Image Generation without Test-Time Finetuning [2].

- Enhancing Detail Preservation for Customized Text-to-Image Generation: A Regularization-Free Approach [3].

2. Does hyper-dreambooth finetune t2i part?

3. The idea is not novel. Using mask to get more accurate object embedding is not new, and BG loss is largely used for this purpose also. Specifically, the application of foreground and background losses in a two-stage process, while presented as a core contribution, lacks sufficient differentiation from existing techniques in the field. A more thorough comparison highlighting the unique aspects of this approach is needed.

4. The two-stage training/finetuning plus the additional losses as restriction are more complicated than previous works, but lacking comparison with above related works [1,2,3]. The complexity introduced by the two-stage pipeline and additional loss terms does not appear to be adequately justified, especially given the absence of comparative results against the mentioned related works.

5. According to the implementation details, the model requires retraining for each new concept, and in the finetuning stage, it relies on lora for better fidelity, which makes the soundness of the method even weaker. The reliance on LoRA and the necessity for retraining with each new concept significantly limit the method's practicality and generalizability.

6. The proposed ESR is worth more descriptions in the main part, since it is  a contribution. The introduction of ESR as a new metric is a potential contribution, but its current presentation is too brief. A more detailed explanation of its calculation, significance, and advantages over existing metrics is necessary.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
