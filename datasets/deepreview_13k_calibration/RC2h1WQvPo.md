# Interpretable Latent Distributions Using Space-Filling Curves

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Deep generative models are well-known neural network-based architectures that learn a latent distribution whose samples can be mapped to sensible real-world data such as images, video, and speech. Such latent distributions are, however, often difficult to interpret. In generative adversarial networks (GANs), some earlier supervised methods aim to create an interpretable (structured) latent distribution or discover interpretable directions for image editing which require exploiting the data labels or annotated synthesized samples during training, respectively. In contrast, we propose using an unsupervised structured distribution modeling technique that incorporates space-filling curves into vector quantization, which makes the latent distribution interpretable by capturing its underlying morphological structure. We apply this technique to model the latent distribution of pretrained StyleGAN2 and BigGAN networks on various image datasets. Our experiments show that the proposed approach yields an interpretable model of the latent distribution such that it determines which part of the latent distribution corresponds to specific generative factors such as age, pose, hairstyle, background, data class, etc. Furthermore, we can use the points and direction of a space-filling line for controllable data augmentation and applying intelligible image transformations, respectively. The implementation of our proposed method is publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the task of unsupervised learning of an interpretable latent space in GANs using space-filling vector quantization. The main idea is to model the latent space of pretrained GANs as a piece-wise continuous and linear curve anchored using a set of codebook vectors. The authors apply the proposed method to two different GAN architectures: StyleGAN and BigGAN. The proposed method is evaluated on different datasets, and a thorough analysis has been provided.

### Strengths
-- The paper is well-written and well-presented.

-- Although learning an interpretable latent space using space-filling vector quantization has been introduced in another previous work, its application to GANs is novel and interesting.

-- The proposed method can be applied to pre-trained GANs and does not require retraining the whole model.

-- The proposed method does not require a pre-defined number of semantic directions to be discovered.

-- The experiments are extensive, evaluating the method on two GAN models and 4 different datasets.

-- Based on the experiment, the proposed method seems effective in discovering meaningful semantic directions in the latent space

### Weaknesses
 -- The provided results for ImageNet (BigGAN) are limited. I could only find two examples limited to the Dog category. It would be interesting to see more visualizations of how the method works on other categories, especially objects.

-- The author has not discussed and evaluated how the latent-space inversion could be performed in the proposed latent space, and whether the discovered directions are meaningful and effective for the inverted latent code.

-- I could not find an ablation on the number of the codebook vectors. I would appreciate it if the authors could further clarify this.

-- I would assume sampling only on the obtained curve could affect the image quality and diversity quite a lot. Currently, no evaluations (e.g. FID scores) are provided for the generation quality.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a method for discovering interpretable distributions in the latent space of pre-trained GANs (StyleGAN2 and BigGAN) using the previously proposed Space-filling vector quantizer (SFVQ). The main intuition of the paper is that the corner points of the space-filling curves (i.e., VQ codebook elements), which is expected to capture the structure of the latent space, will refer to similar content, and thus will provide a path to control/interpret the generation process. The proposed method is compared qualitatively with GANSpace, an unsupervised method for discovering interpretable direction using PCA, on two GAN architectures (StyleGAN2 and BigGAN).

### Strengths
The idea of using space-filling curves in the context of pre-trained GANs, in order to model interpretable/controlable generative paths is interesting.

### Weaknesses
Whilst I find the idea of using the Space-filling vector quantizer (SFVQ) for discovering interpretable/controlable latent paths in pre-trained GANs interesting, the paper fails to convince why this is an effective approach towards that goal.

First and most importantly, the paper does not discuss or compare with two very relevant recent works [1, 2]. These works are both unsupervised and model-agnostic, and, similarly to GANSpace, should necessarily be included in the experimental evaluation of the proposed method. Specifically, the method in [1] uses a non-linear transformation of the latent space to achieve better control, and the method in [2] uses radial basis functions to model interpretable paths, both of which are highly relevant to the goals of this paper and should be compared against.

Second, the presented empirical evaluation is only qualitative, rendering impossible to compare its advantages against GANSpace (and other relevant works that are missing [1, 2]). Even in that case, in the only figure that provides comparison with an existing work (i.e., Fig. 7, comparison with GANSpace), it is hardly visible why the proposed method is better. The paper lacks any quantitative metrics to assess the quality of the discovered directions, such as those used in [1, 2], which makes it impossible to objectively evaluate the proposed method's performance.

In absence of any quantitative comparison, it is impossible to assess the merits of the proposed method. Appropriate quantitative metrics can be found in [1, 2]. In my point of view, the paper should compare with those methods using the suggested metrics. For example, metrics like commutativity error, side effect error, and identity error, as used in [1], would provide a much more rigorous evaluation. Similarly, metrics used in [2] to evaluate the quality of the discovered paths should also be considered.

Finally, I found the structure of the paper hard to follow. Specifically, Sect. 4 appears to be a few unstructured blocks of text discussing limited empirical results. Also, in many occasions, the paper makes unsupported or inaccurate claims. For instance, "our unsupervised proposed method neither needs any human labeling nor puts any constraint on the learned latent distribution" is not true according to Sect. 4.2 (for instance). The method does rely on a pre-trained GAN, which has an inherent learned latent distribution, and the selection of which latent vectors to modify is based on prior knowledge, which can be seen as a form of implicit human labeling.

### Questions
In Sect. 4.1 you mention: "When generating W’s latent vectors during training, StyleGAN2 asks for class label of the image."
How this is the case? StyleGAN2 is not a conditional GAN, that class label is not given during generation.

Have you considered other latent space, such as W+ or the so-called style space S? I think it would be interesting to do so, since:
i) W+ can be split into 18 512-dimensional sub-spaces, where learning a SFVQ for each sub-space (layer) could lead to further controlability/interpretability, and
ii) the style space S is remarkably disentangled (changing a single element/dimension could lead to a very specific and disentangled change, such as gaze movement).

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors have applied the method introduced in (Vali and Backström, 2023) to the intermediate latent space of Generative Adversarial Networks (GANs) used for generating image data. This method aims to disentangle the latent space of generative models by learning a set of vectors (codebook) that are designed to quantize a space-filling curve. The experiments mainly involve visualizing the images generated by the vectors from the learned codebook.

### Strengths
* The visualizations show interesting properties of the latent-space filling curve, with images from same classes being clustered at nearby indexes in an unsupervised manner.

### Weaknesses
 * Lack of Novelty and Originality: The paper primarily focuses on the application of an existing method to new models and datasets, without introducing any novel or original contributions. There is no apparent effort to adapt or modify the method to suit the characteristics of the new models and dataset. In my view, this lack of novelty and originality raises questions about whether this paper is suitable for submission to ICLR, as it could be perceived as a dual submission.

* Insufficient Experimental Rigor: The experimental setup in the paper is notably lacking in terms of rigor. The absence of quantitative metrics and reliance solely on visualizations is a significant shortcoming. Without comprehensive metrics, the results can be susceptible to cherry-picking and fail to provide a strong empirical validation of the method.

### Questions
-

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
