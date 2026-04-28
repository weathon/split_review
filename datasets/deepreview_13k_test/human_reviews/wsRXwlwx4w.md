# Consistency-guided Prompt Learning for Vision-Language Models

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
We propose Consistency-guided Prompt learning (CoPrompt), a new fine-tuning method for vision-language models. Our approach improves the generalization of large foundation models when fine-tuned on downstream tasks in a few-shot setting. The basic idea of CoPrompt is to enforce a consistency constraint in the prediction of the trainable and pre-trained models to prevent overfitting on the downstream task. Additionally, we introduce the following two components into our consistency constraint to further boost the performance: enforcing consistency on two perturbed inputs and combining two dominant paradigms of tuning, prompting and adapter. Enforcing consistency on perturbed input serves to further regularize the consistency constraint, thereby improving generalization. Moreover, the integration of adapters and prompts not only enhances performance on downstream tasks but also offers increased tuning flexibility in both input and output spaces. This facilitates more effective adaptation to downstream tasks in a few-shot learning setting. Experiments show that CoPrompt outperforms existing methods on a range of evaluation suites, including base-to-novel generalization, domain generalization, and cross-dataset evaluation. On generalization, CoPrompt improves the state-of-the-art on zero-shot tasks and the overall harmonic mean over 11 datasets. Detailed ablation studies show the effectiveness of each of the components in CoPrompt.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new adaptation method for CLIP like large scale vision-language models for generalization benchmarks. Specifically, the authors propose 3 techniques to improve generalization of CLIP. Firstly, they observe that the main cause of poor generalization is the lack of consistency constraints between the learned embeddings and the original pretrained embeddings. To overcome this issue, consistency losses are used at the text side as well as the image side separately. Secondly, the inputs to the original models are perturbed with the help of augmentations and LLM captions for image and text side respectively. Lastly, the proposed method combines the adapter and prompt learning modules with-in the same architecture for improved performance. 

Extensive benchmark comparisons are conduced on 3 different generalization tasks where the proposed approach shows improvements against prior methods. Furthermore, ablation studies are provided for analyzing contributions of each component separately and motivating the design choices.

### Strengths
1) This paper addresses an important aspect of generalization of pre-trained CLIP like models for downstream task adaptation. Most of the prior methods struggles to achieve good performance on unseen classes and datasets, while this method explicitly add training constraints to mitigate the issue.
2) The proposed framework is motivated fairly, and the strength of its individual components have been demonstrated clearly in the ablation studies.
3) The method shows impressive performance against the previous prompt learning methods.
4) Paper is easy to read.

### Weaknesses
1. The authors mentioned that their baseline is MaPLe, which uses coupling functions between vision and text branches, but in Figure 3, no coupling functions are visible. It will be good to clarify the exact architecture used in the proposed framework. Also I think there is graphic error in image encoder as the visual prompts (orange color) are not shown in intermediate layers of CLIP visual encoder. 

2. It will be good to see the proposed method generalization for a newer V-L model. CLIP is relatively outdated and the authors are encouraged to show result on at least another recent CLIP variant. For example on EVA-CLIP[1] model. 

3. There is a recent prompt learning method PromptSRC [2], which also seems to introduce consistency constraints to prompt learning to improve generalization. How is the proposed method different from this work? Also, all fair comparisons should be added in the main paper. 

4. The diagrams in the paper are of very poor quality. Specially the text in the Figure 2. graph is very small and the color scheme used is confusing. Also in the Figure 1, their is no indication of using adapters in Fig. 1b. 

5. I think there is some writing logical errors in the paper. For example, in the Adapters heading in section 3, adapter based method are being mentioned but prompts have been written instead of the adapter blocks. 

[1] Exploring the Limits of Masked Visual Representation Learning at Scale (CVPR-23)
[2] Self-regulating Prompts: Foundational Model Adaptation without Forgetting (ICCV-23)

### Questions
Please refer to the weaknesses section for additional questions and queries!

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a consistency-enforced fine-tuning method for large foundation model CLIP that enables learning a new task from a few samples while maintaining the zero-shot generalizability. The proposed method incorporates the knowledge of a pretrained LLM with consistency constraints on the text branch and data augmentations on the image branch to improve the generalization further along with learnable adaptors on both image and text branches.

### Strengths
- The  paper is well-written and easy to follow.
- The authors have shown decent results on base-to-novel generalization.

### Weaknesses
- The idea of adaptors and prompt-tuning already exist in the literature. Merely combining the two ideas seems an incremental work and not novel.
- The idea of retaining the generalizability of the CLIP using consistency loss has already been explored in the paper "Self-regulating Prompts: Foundational Model Adaptation without Forgetting" (ICCV 2023) [1]. Hence,  the consistency loss doesn't contribute towards the novelty.
- The authors have not compared their approach to the above paper and there is also no reference to the paper.
- The improvements in the Domain generalization is marginal given that authors have fine-tuned the model. Same is true for cross-dataset evaluation.


[1] Muhammad Uzair Khattak, Syed Talal Wasim, Muzammal Naseer, Salman Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan. Self-regulating Prompts: Foundational Model Adaptation without Forgetting. ICCV 2023 (https://arxiv.org/abs/2307.06948)

### Questions
- Are the vision side prompts conditioned on text side? Do authors follow MaPLe settings or Independent VL prompting?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a consistency-guided prompt learning (CoPrompt) method to transfer CLIP to downstream tasks in a few-shot setting. Experimental results show the capacity of consistency-guided prompt learning to imporve the generalization comparing with the SOTA methods.

### Strengths
1. CoPrompt achieves the SOTA results on base-to-novel generalization and cross-domain setting. 

2. Ablation studies demonstrate the effectiveness of consistency constrain to prevent overfitting on the downstream tasks.

### Weaknesses
1.The prompt learning and adapter learning method mentioned in this paper are introduced by MaPLe and CLIP-Adapter. The primary contribution of this paper only lies in the introduction of consistency constraint learning.  Thus, regarding the method as prompt learning is a bit ambiguous in my opinion.

2. The comparison between CoPrompt and Zero-shot CLIP is not fair enought. The diverse text prompts generated by LLM can imporve the zero-shot classification ability of CLIP on downstream tasks. It is important to consider this aspect when evaluating the performance of  Zero-shot CLIP.

3. On small scale dataset like Eurosat, the higher value of λ leads to worse performance, accroding to Table 7. However, the analysis regarding this observation is missing from the paper. Can CoPrompt reaches better result on Eurosat if λ=0?

### Questions
1. What if combined consistency constrain learning with other existing methods, like CoCoOP. Can CoPrompt improve the generalization of CoCoOP?

2. What is the training overhead in terms of time? What is training and test-time inference speed compared with prior methods?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents an innovative prompt learning technique that integrates a consistency mechanism between trainable and pre-trained models to mitigate the risk of overfitting. This approach employs a consistency term applied to two altered inputs within the text and visual spheres. In text modality, the method leverages existing language models like GPT-2 and GPT-3 to introduce variations, whereas for images, it uses standard image augmentation techniques prevalent in self-supervised learning. The authors have skillfully merged two distinct approaches to adaptation - prompting and adaptation - demonstrating that this synergy, coupled with a consistency loss, enhances the method's ability to generalize. The improved generalization capability of this approach is evident in various prompt learning tasks, including adapting from base to new tasks, cross-dataset evaluation, and domain generalization, with consistent enhancements observed across these applications.

### Strengths
The paper is clear and of high quality, with significant numerical results. The authors offer a thorough analysis of their proposed method's various components, which overall appear sensible and well-founded.

### Weaknesses
While the paper is clear, and the numerical results are noteworthy, its novelty isn't entirely clear. The paper's self-consistency terms seem similar to those in self-supervised learning (SSL) methods. The authors' claim of differentiating their approach from SSL, where two perturbed inputs within a single encoder are used, doesn't fully convince. In SSL, typically there are two encoders: an online encoder and a momentum encoder. The paper’s pre-trained and trainable encoders appear analogous to SSL’s momentum and online encoders, respectively. The authors should clarify this similarity.

Additionally, the paper omits recent relevant studies like Bayesian Prompt Learning [1] and Prompt Distribution Learning [2], which address overfitting in vision and language models. Discussing these in the related work and comparing them in sections like domain generalization are necessary, especially given that in some cases, such as Bayesian Prompt Learning, they outperform the methods in this paper. For example, in the domain generalization task, the Bayesian Prompt Learning method (%60.44) works better than the paper performance (%60.42). 

[1]. Bayesian Prompt Learning for Image-Language Model Generalization, ICCV 2023

[2]. Prompt Distribution Learning, CVPR 2022

### Questions
Please see the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
