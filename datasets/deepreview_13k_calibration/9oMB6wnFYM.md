# Deconstructing Denoising Diffusion Models for Self-Supervised Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
\vspace{-.5em}
In this study, we examine the representation learning abilities of Denoising Diffusion Models (DDM) that were originally purposed for image generation. Our philosophy is to \emph{deconstruct} a DDM, gradually transforming it into a classical Denoising Autoencoder (DAE). This deconstructive procedure allows us to explore how various components of modern DDMs influence self-supervised representation learning. We observe that only a very few modern components are critical for learning good representations, while many others are nonessential. Our study ultimately arrives at an approach that is highly simplified and to a large extent resembles a classical DAE. We hope our study will rekindle interest in a family of classical methods within the realm of modern self-supervised learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the author studied the representation learning abilities of denoising-autoencoder-based diffusion models (DDMs). Throughout extensive ablation studies, they explored how various components of modern DDMs influence self-supervised representation learning. At the core of their philosophy is to deconstruct a DDM, changing it step-by-step into a classical DAE. This research process demonstrates that the main critical component for a DAE to learn good representations is a tokenizer that creates a low-dimensional latent space.

### Strengths
**1.** In general, this paper contributes significantly to the intersections of diffusion models and representation learning.  The findings open up new avenues for future research in leveraging diffusion processes to enhance representation quality across diverse applications

**2.** The authors conducted extensive experiments to support their results. The paper is well-written and easy to follow.

### Weaknesses
The reviewer has the following major concerns about this paper:

**1.** It is not comprehensive to study the representation ability of diffusion models only by considering the classification of downstream tasks. The authors should provide more experiments on other tasks to support their conclusions. Specifically, while classification is a common benchmark, it only assesses the separability of learned features. The authors should also investigate tasks that probe other aspects of representation quality, such as feature similarity or reconstruction. For instance, evaluating performance on tasks like image retrieval or few-shot learning could provide a more holistic view of the learned representations.

**2.** Although the observations of this work are really new and interesting, the authors seem to not fully discuss the implications of these findings. The paper presents a compelling deconstruction of diffusion models, but it lacks a thorough discussion of the broader impact. For example, the authors should elaborate on how their findings could influence the design of future self-supervised learning methods or how the discovered role of the tokenizer could be leveraged in other domains.

### Questions
**1.** The authors mainly focused on investigating the representation learning abilities of DiTs. Are there similar observations on U-Net-based diffusion models? 

**2.** Based on the experimental results, can we conclude that adding noise primarily impacts the generation capabilities of diffusion models rather than their representation learning ability? Are there any insights for this observation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the representation learning ability of denoising diffusion models. Through a set of ablation studies that deconstruct a denoising diffusion model into a classical denoising autoencoder (DAE), the authors observe that only a very few modern components (such as a low-dimensional latent space) are critical for learning good representations. Experiments also show that a latent DAE, which largely resembles the classical DAE, can perform competitively in self-supervised learning.

### Strengths
Studying the representation learning ability of denoising diffusion models is important and could provide useful insights for unifying models for generation and discrimination.

Overall, the paper is very well written. The experiments are solid, and the message is clear. The observation that a low-dimensional latent space is a critical component for representation learning is useful.

### Weaknesses
1. While the study begins with denoising diffusion models, it ultimately leads to models that demonstrate strong representations for classification but not for generation. The FID is reported only in Table 1, which reveals a significant contradiction between classification accuracy and FID. The paper does not explore the trade-offs between these two objectives, which is a critical aspect when studying diffusion models.

3. For the goal of representation learning for classification without fine-tuning, the obtained latent DAE achieves slightly worse performance than MAE and contrastive learning. The paper does not discuss the potential reasons for this gap, such as differences in training objectives or architectural choices, nor does it explore methods to close this gap.

4. The representation is extracted from the middle layer of the transformer for linear probing. Previous studies have found that the middle layer may not provide the best representation of a diffusion model for classification. The paper does not provide a detailed justification for this choice, nor does it explore the impact of using different layers on the final performance.

### Questions
1. What are the FID scores for other modifications beyond Table 1, such as operating in the image space with PCA?

2. Does better classification accuracy always lead to worse FID scores? In other words, are the tasks of generation and representation learning (for recognition) fundamentally contradictory to each other? Or could we unify them?

3. Why is the middle layer of the transformer chosen as the representation for linear probing?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the representation ability of generative denoising diffusion models (DDM). It specifically aims to identify crucial components for DDMs' representation ability during the process of removing modern components in DDMs until it becomes a simpler model very similar to classic Denoising Autoencoder (DAE). Notably, DAE is originally proposed for representation learning. The paper is highly empirical, conducting various experiments on different components, such as different loss terms, different tokenizers, class-conditioning, noise schedule, whether to predict clean data, etc. It can remove many components designed for generation, and show high-level representation abilities are not strictly related to generation ability.

### Strengths
(1) The paper has identified a thorough set of different components between classical DAE and modern diffusion models.

(2) The paper sheds light on a potential framework for understanding the representation ability of diffusion models - DAE.

(3) The paper is the first work trying to identify key representation components from generative models and could inspire future works.

(4) The paper has some interesting findings, such as the low-rank tokenizer is important, and the high-level representation ability may not correlate with the generation ability.

### Weaknesses
 (1) The paper only presents empirical findings, with no theoretical analysis or practical applications.

(2) The complex possible choices of components make the experiment order not strictly natural and logical. 

(3) Missing experiments on some possible choices of components make the conclusions of the paper not that strong, for example, it's hard to conclude whether predicting clean images is more helpful than predicting noise for representation learning.

### Questions
1. L 247: The paper claims "self-supervised learning performance is not correlated to generation quality". However, the selected tasks such as linear probes only consider coarse representations that are useful for high-level tasks. What about more fined representations such as segmentation, and positions of a specific object, etc, would it be correlated to generation quality?
2. L 369: why the DAE is expected to work directly on the image space, could you please explain the importance of working on the image space?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors perform an extensive ablation study on modern Denoising Diffusion Models (DDMs) to identify the critical components for effective representation learning, comparing these models to traditional denoising autoencoders (DAEs). The authors begin by comparing DDMs and DAEs on their design and purpose, indicating that generation (DDM objective) is not directly connected with good representations (DAE objective), and suggesting a possible trade-off between these them.

Then the authors test various modifications to make DDMs more similar to DAEs while preserving high-quality representations. Notably, they find that the tokenizer is beneficial mainly for its dimensionality reduction role and that a simplified approach, like patch-wise PCA, can serve this function without compromising performance. They also identify less critical components: noise scheduling (analogous to data augmentation), class conditioning (which may lessen the model’s need to capture class-specific, fine-grained semantics), and predicting noise versus the original image.

Based on these findings, the authors propose **l-DAE**, a DAE that operates in the latent domain. They validate the effectiveness of l-DAE through experiments on classification and object detection tasks, showing its competitive performance.

### Strengths
1. The authors aim to bridge modern self-supervised learning with classical methods by deconstructing diffusion denoising models (DDMs) and propose a simple but effective representation learner similar to traditional denoising autoencoders (DAEs).

2. Through this novel deconstructing process, the authors provide key insights. For instance, they highlight the importance of the low-dimensional latent space into which the tokenizer maps the patches, as it plays a crucial role in learning robust representations. Additionally, they demonstrate that adding noise in the latent space is more effective than in the pixel space, a finding that invites further exploration of latent space structures.

### Weaknesses
1. In the paper, the authors make numerous claims but test them only on a specific task (ImageNet classification) and model (DiT-L). Furthermore, the deconstructing process faces a limitation: the components may be correlated, making a sequential analysis potentially inadequate. Specifically, the authors do not explore the impact of different orders of ablating components, which could lead to different conclusions about the importance of each component. For example, removing the VQGAN loss before altering the noise schedule might yield different results than the reverse order. This lack of exploration limits the robustness of the conclusions.
2. Some of the claims may be overlooked. For instance, the statement that 'multiple levels of noise is analogous to a form of data augmentation' (lines 416–418) may be overly simplified. Prior research has shown that combining representations at different noise levels can lead to significant improvements. The authors do not adequately address the potential benefits of combining representations from different noise levels, which is a critical aspect of denoising diffusion models. The analogy to data augmentation is also not fully justified, as data augmentation typically involves geometric or color transformations, while noise addition is a fundamentally different type of perturbation.

### Questions
1. Could you explain on why noise scheduling can be considered a form of data augmentation? Is there any ablation study showing that the effects of noise scheduling and data augmentation are comparable?
2. Regarding the section on predicting the original image (Lines 392–406), shouldn't the matrix $V$ be of size $D \times d$? Also, if the weights $w_i$ are all 1, the loss would again become the reconstruction loss on the latent space. This suggests that the relative scale of these weights is important. Do you have any ablation studies on this aspect?"

### Soundness
3

### Presentation
3

### Contribution
3
