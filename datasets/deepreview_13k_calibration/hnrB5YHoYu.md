# Finetuning Text-to-Image Diffusion Models for Fairness

- Decision: Accept
- Avg Score: 4.33
- Scores: 6, 1, 6

## Abstract
The rapid adoption of text-to-image diffusion models in society underscores an urgent need to address their biases. Without interventions, these biases could propagate a skewed worldview and restrict opportunities for minority groups. In this work, we frame fairness as a distributional alignment problem. Our solution consists of two main technical contributions: (1) a distributional alignment loss that steers specific characteristics of the generated images towards a user-defined target distribution, and (2) adjusted direct finetuning of diffusion model's sampling process (adjusted DFT), which leverages an adjusted gradient to directly optimize losses defined on the generated images. Empirically, our method markedly reduces gender, racial, and their intersectional biases for occupational prompts. Gender bias is significantly reduced even when finetuning just five soft tokens. 
Crucially, our method supports diverse perspectives of fairness beyond absolute equality, which is demonstrated by controlling age to a $75\%$ young and $25\%$ old distribution while simultaneously debiasing gender and race. Finally, our method is scalable: it can debias multiple concepts at once by simply including these prompts in the finetuning data. We share code and various fair diffusion model adaptors at \href{https://sail-sg.io/finetune-fair-diffusion/}{https://sail-sg.io/finetune-fair-diffusion/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how to finetune diffusion models with fairness as the goal. By formulating generation fairness as distribution alignments, the paper introduces a distributional alignment loss and an end-to-end fine-tuning framework. Experiments show that the fine-tuned model can generate facial images with targeted distribution of certain sensitive attributes.

### Strengths
1. The fairness of image generation studied in this paper is an important and practical problem. 
2. The proposed fine-tuning method is sound, and the results validate the effectiveness of the method.
3. The paper has made a comprehensive analysis of which part of the model to fine-tune as well as the challenges in fine-tuning, providing insights into future fair fine-tuning work.

### Weaknesses
1. The paper only tested the method on single-face generation, limiting the applicability of the proposed method. It is unclear how the method would perform with multiple faces in the generated images, as the fairness constraints might become more complex and require different handling of each face. For instance, if the goal is to generate a group of people with equal representation of sensitive attributes, the current method, which focuses on the most prominent face, might not be sufficient.
2. It is unclear whether fine-tuning with the fairness loss affects the quality and diversity of the generated images on general prompts. The paper focuses on targeted prompts related to specific occupations and sensitive attributes. It is important to evaluate how the fine-tuning affects the model's ability to generate high-quality and diverse images for a broader range of prompts, as it might lead to a degradation in overall generation quality or a reduction in the diversity of the generated images.
3. Although experiments in the paper show better performance than baseline methods, it is unclear how expensive the fine-tuning is compared with the baseline methods. The paper does not provide a clear comparison of the computational cost of the proposed fine-tuning method with the baselines, which makes it difficult to assess the practical feasibility of the proposed method. It is important to know the training time, GPU usage, and other computational resources required for the proposed method in comparison to the baseline methods to determine its efficiency.

### Questions
1. In Equation (4), how to obtain the expectation in practice?
2. In Table 2, on unseen prompts, how good is the proposed method compared with the baselines? Does the fine-tuning have an overfitting problem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new method for debiasing text-to-image diffusion models. While the approach is general, the authors focus on the mitigation of demographic biases here, such as gender, racial, or age-related biases in generated depictions of different occupation types or sports activities. 

The method consists of a supervised fine-tuning step for different model components, which minimizes (in addition to two regularization losses that aim to preserve image quality) a loss that penalizes deviations in the demographic distribution of the generated images from a prescribed target demographic distribution. 

The authors demonstrate experimentally that naive autodifferentiation-based gradient descent on this loss fails to achieve successful optimization; they provide a theoretical explanation, backed by empirical experiments, for this behavior. They then proceed to propose a simple gradient adjustment mechanism that mitigates this problem and enables successful optimization of the proposed loss function. 

Finally, the authors perform extensive experiments (using Stable Diffusion as an example), an ablation study, and comparisons with previously proposed debiasing mechanisms. Throughout all experiments, the proposed method is highly successful in mitigating demographic biases for unseen prompts, especially also in regards to intersectional biases.

### Strengths
The manuscript addresses a topic of immediate and urgent concern. 

It is very well written, appropriately references relevant prior work, and compares the proposed new method extensively to previously proposed methods. 

The proposed approach is derived from first principles (distribution alignment) and intuitively appealing. The method is widely applicable - also beyond demographic debiasing - and, importantly, allows for 
1) customized and explicit choices of the target data distribution, and 
2) debiasing along multiple demographic dimensions at once. 

The experiments are extensive, well described, and convincingly demonstrate the utility of the proposed method and its superiority over previously proposed approaches to address the same problem.

### Weaknesses
I could not find any major weaknesses in this manuscript. I only have a few minor questions and suggestions that I will list below.

### Questions
- CLIP is not without its own issues; see e.g. Shtedritski et al., Wang et al., Wolfe et al., or Zhang and Ré. Could the authors discuss how this might affect the efficacy of their proposed method?
- How do the authors implement using different lambda values for different regions of the same image, as they describe at the end of section 4.1? ("We use a smaller weight for the non-face region ... and the smallest weight for the face region.") L_img is per image, not per pixel, no?
- I was confused about the training of the gender and race classifiers for the evaluation. Were separate classifiers trained for the training and the evaluation stage? If yes, why? Or is this maybe some kind of unintended text duplication? ("The gender and race classifiers used for the evaluation loss are trained on the CelebA and FairFace datasets. ... Evaluation. We train new gender and race classifiers using CelebA and FairFace.")
- It was unclear to me which of (soft prompt, text encoder, U-Net) were actually finetuned for all of the main experiments in section 5.1?
- Can the authors think of (and comment on) any drawbacks of applying their method at scale and for many fairness-relevant properties simultaneously? Could there be any negative consequences (e.g., in terms of image quality or biases) when e.g. generating very different images (bears, tables, groups of people, ... )? Recent observations by Qi et al. could also be interesting to discuss in this regard.

### Questions
### Questions
- CLIP is not without its own issues; see e.g. Shtedritski et al., Wang et al., Wolfe et al., or Zhang and Ré. Could the authors discuss how this might affect the efficacy of their proposed method?
- How do the authors implement using different lambda values for different regions of the same image, as they describe at the end of section 4.1? ("We use a smaller weight for the non-face region ... and the smallest weight for the face region.") L_img is per image, not per pixel, no?
- I was confused about the training of the gender and race classifiers for the evaluation. Were separate classifiers trained for the training and the evaluation stage? If yes, why? Or is this maybe some kind of unintended text duplication? ("The gender and race classifiers used for the evaluation loss are trained on the CelebA and FairFace datasets. ... Evaluation. We train new gender and race classifiers using CelebA and FairFace.")
- It was unclear to me which of (soft prompt, text encoder, U-Net) were actually finetuned for all of the main experiments in section 5.1?
- Can the authors think of (and comment on) any drawbacks of applying their method at scale and for many fairness-relevant properties simultaneously? Could there be any negative consequences (e.g., in terms of image quality or biases) when e.g. generating very different images (bears, tables, groups of people, ... )? Recent observations by Qi et al. could also be interesting to discuss in this regard.

### Suggestions for improvement
- The optimal transport approach in Eq. (4) was a bit confusing to me at first because it differs from the usual setting in which the optimal transport scheme between two *distributions* is considered. By contrast, the authors consider an expectation over the optimal transport schemes between two *vectors* here. I believe everything is actually described correctly, but maybe there is a way to make this section even easier / more intuitive for readers to grasp? (Sorry, possibly not very helpful.)
- It is a little bit confusing that y denotes both the generated target labels (normal font) as well as the images generated by the frozen model (boldface). 
- What does it mean that CLIP-ViT-bigG-14 and DINOv2 vit-g/14 are "more performative than the ones used in training"?
- The authors might want to consider citing Lester et al. regarding soft prompt tuning?

### References
- Lester et al., The Power of Scale for Parameter-Efficient Prompt Tuning,  https://arxiv.org/abs/2104.08691
- Qi et al., Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!, https://arxiv.org/abs/2310.03693
- Shtedritski et al., What does CLIP know about a red circle? Visual prompt engineering for VLMs, https://arxiv.org/abs/2304.06712
- Wang et al., FairCLIP: Social Bias Elimination based on Attribute Prototype Learning and Representation Neutralization, https://arxiv.org/abs/2210.14562
- Wolfe et al., Contrastive Language-Vision AI Models Pretrained on Web-Scraped Multimodal Data Exhibit Sexual Objectification Bias, https://dl.acm.org/doi/abs/10.1145/3593013.3594072
- Zhang and Ré, Contrastive Adapters for Foundation Model Group Robustness, https://arxiv.org/pdf/2207.07180.pdf

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to tackle the fairness problem in text-to-image generation. They define the problem as a distribution alignment problem and use the optimal transport as the alignment loss; they also enable the user-defined target distribution as the fairness metrics. They also analyzed the straightforward end-to-end fine-tuning failure and proposed using the adjusted gradient. The experiment also shows that their method is able to reduce the bias while reserving the sematic information.

### Strengths
The paper is clearly written and proposes a straightforward finetuning solution to improve the fairness of the text-to-image generation model. They also propose an alignment loss based on the optimal transport and provide an analysis of the gradient of the finetuning step. Their experiments also show the effectiveness of their method.

### Weaknesses
This paper kind of mixing fairness and bias and uses both terms interchangeably, especially for the experiment evaluation part, they define the metric for bias by themself which reduces the credential of the evaluation. I wonder if any other metrics from other research papers have been used for evaluation. Is it possible to use well-defined fairness metrics like demographic parity/ equal opportunity, etc?

### Questions
1. for the equation 4, what is the u? 
2. As for the alignment loss, have you tried some other metrics other than the optimal transport loss? And why did you choose the optimal transport metric?
3. For the face classifier, how accurate it is? and if the combination of face detector and face classifier is not performed well on some datasets, how does it affect the debias experiment result?

some minor comments:
1. In section 4.2, when you talk about U-net, please provide the necessary background info.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
