# GeNIe: Generative Hard Negative Images Through Diffusion

- Decision: Reject
- Scores: 5, 6, 6, 8

## Abstract
Data augmentation is crucial in training deep models, preventing them from overfitting to limited data. Recent advances in generative AI, e.g., diffusion models, have enabled more sophisticated augmentation techniques that produce data resembling natural images. We introduce \genie{} a novel augmentation method which leverages a latent diffusion model conditioned on a text prompt to combine two contrasting data points (an image from the source category and a text prompt from the target category) to generate challenging augmentations. To achieve this, we adjust the noise level (equivalently, number of diffusion iterations) to ensure the generated image retains low-level and background features from the source image while representing the target category, resulting in a \emph{hard negative} sample for the source category. We further automate and enhance \genie{} by adaptively adjusting the noise level selection on a per image basis (coined as \texttt{GeNIe-Ada}), leading to further performance improvements. Our extensive experiments, in both few-shot and long-tail distribution settings, demonstrate the effectiveness of our novel augmentation method and its superior performance over the prior art.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel data augmentation method based on a latent diffusion model. It combines target and source categories in the latent noise-level to generate hard-negative samples for the source category. The impact of the proposed GeNIe is evaluated on two famous data-scarce problems.

### Strengths
- This paper proposes a realistic solution for practical problems of data augmentation using recent text-to-image generative models.
- The proposed method, GeNIe, contains an effective and adaptive strategy for data augmentation.

### Weaknesses
- The exact method for GeNIe is not detailed in the main script, although the key idea is presented, which can cause confusion.
- The proposed GeNIe is a simple data augmentation method on the latent space of Stable Diffusion, which lacks the novelty of the method except for modifying noise levels for better augmentation.
- GeNIe-Ada requires an additional classifier to search the decision boundary between two categories.

### Questions
- Is the classifier used for GeNIe-Ada the same as the one trained for the target task? How does the performance of this classifier affect the effectiveness of GeNIe-Ada?
- Is there no information leakage by using stable diffusion in few-shot classification for mini-ImageNet and tiered-ImageNet?
- Does using images from all other classes as the source image in line 352 mean that source images are selected from the support set of the other 4 classes, or all other 63 classes (for mini-ImageNet)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a solution to generate augmentations using diffusion models to improve the performance of classifiers in few-shot and long-tailed settings, which are characterized by low-data scenarios. To that end, the authors propose using a latent diffusion model that combines a source image (with a known category, e.g., dog) with a target category prompt (e.g., cat), producing challenging samples that retain background features from the source category but resemble the target category. This approach aims to push model learning near decision boundaries, providing more informative augmentations than traditional methods.

GeNIe, inspired by image editing through diffusion models, works by adjusting noise levels in the diffusion process to control the balance between source and target features in the generated image. The authors demonstrate that lower noise levels retain more of the source image's visual characteristics, while higher levels focus on the target category. To automate the noise level per sample, the authors further introduce GeNIe-Ada. This variant stems from the observation that there is a sudden change in appearance when the noise levels are uniformly sampled. The authors leverage this observation along with the assumption that they also have access to another target sample. They then propose to compare the similarities of this sample and the generated sample in the latent space of a classifier.

To validate the utility of these augmentations, the authors conduct experiments on few-shot and long-tail classification tasks and demonstrate significant improvements on standard benchmarks.

### Strengths
The paper is well-written and easy to follow. The motivation is sound, and using diffusion models to generate augmented views, even though it is a well-explored area, the authors focus on generating hard negative images. This approach forces the classifiers to learn the true characteristics of the category rather than rely on spurious correlations, such as background. In many ways, the motivation is similar to foreground and background editing ideas. Their method also addresses the general problem of CNNs, which tend to rely more on textures than on the shapes of objects while classifying. Furthermore, the results are impressive across different benchmarks.

### Weaknesses
I have a few concerns and questions regarding GenIE. While generative models are indeed a powerful approach, they can be restrictive in the following sense: their applicability in general, and GenIE in particular, requires that the generative model already knows the concepts of the target category, which is a strong assumption to make. In that sense, generative model-based augmentations should be viewed from two perspectives: (I) those that change the background and (ii) those that change the category. In the first setting, the use of generative models makes a lot of sense because it aligns with the paper's motivation but is concept agnostic. The second category is harder to argue because it requires the generative model to have complete knowledge of all target categories, which would severely limit its applicability. Category 1 also has the added benefit of generalizing to newer domains. For example, in SiSTA: Target-Aware Generative Augmentations for Single-Shot Adaptation (ICML 2023), the authors do not view this as an image editing problem but rather adapt a generative model like StyleGAN to the target domain using a single image and then sample from the model to generate augmented variants. These variants are then used to train classifiers with source-free unsupervised domain adaptation. In this context, GenIE requires both source samples, and its general treatment of this problem as image editing is limiting.

I would like to see comparisons or discussions regarding the strong assumptions that GenIE makes in this context. This is an important discussion because even simpler methods like mixup do not require explicit knowledge of target categories, which GenIE's reliance on diffusion models necessitates.

Similarly, the diffusion models used in the paper are large-scale foundation models trained on LAION. This raises questions about the improvements: it is unclear whether the gains are due to the proposed method or the large-scale pretraining of the diffusion model. It would also be important to discuss relevant work, such as (Tian, Yonglong, et al. "Stablerep: Synthetic images from text-to-image models make strong visual representation learners." Advances in Neural Information Processing Systems 36 (2024).), which uses Stable Diffusion to generate synthetic positive samples for contrastive self-supervised learning training.

Lastly, it would be interesting to see if synthetic image augmentations can be used alongside general mixup, similar to (Graikos, Alexandros, Srikar Yellapragada, and Dimitris Samaras. "Conditional Generation from Pre-Trained Diffusion Models using Denoiser Representations." BMVC. 2023.), which has shown that synthetic images from a conditional diffusion model can provide complementary benefits to mixup.

### Questions
Please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors try to illustrate their idea by proposing these points:
1. The authors introduce GeNIe, a novel yet elegantly simple diffusion-based augmentation method to create challenging augmentations in the manifold of natural images. For the first time, to our best knowledge, GeNIe achieves this by combining two sources of information (a source image, and a contradictory target prompt) through a noise-level adjustment mechanism.
2. They further extend GeNIe by automating the noise-level adjustment strategy on a per-sample basis
(called GeNIe-Ada), to enable generating hard negative samples in the context of image classification, leading also to further performance enhancement.
3. To substantiate the impact of GeNIe, authors present a suit of quantitative and qualitative results including extensive experimentation on two challenging tasks: few-shot and long tail distribution settings corroborating that GeNIe (and its extension GeNIe-Ada) significantly improve the downstream classification performance.

### Strengths
1. GeNIe leverages a latent diffusion model to create challenging augmentation images by blending features from two classes (source and target). By adjusting the noise level, GeNIe maintains low-level details from the source image while incorporating semantic features of the target class, creating what the authors term "hard negative" samples. This process potentially aids in classifier training by providing near-boundary examples.

2.Adaptive Mechanism (GeNIe-Ada):
The GeNIe-Ada extension adds significant value by adaptively selecting noise levels for each sample, fine-tuning the augmentation to be more effective. This adaptive approach is well-aligned with real-world scenarios where data variability and distributional shifts are common, making it a practical addition.

### Weaknesses
1. They didn't give more contribute to the model itself. It's just an application to generate images.
2. Limited number of downstream cases.

### Questions
Could you add more experiments on some other mainstream tasks? Do you have comparisons with other models for data augmentation? Such as GAN?

### Soundness
2

### Presentation
2

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
The paper leverages Stable Diffusion to generate hard negatives as data augmentation for image classification. The hard negatives are generated by feeding a source image into the model's encoder but conditioning the reverse diffusion process with a text prompt corresponding to the target class. 

The proposed approach includes an automatic noise-level adjustment per sample, which controls the degree of deviation from the source image, thereby aligning more with the target class prompt. The authors show that the choice of the noise level is critical, as only a restricted range of values allow for a good balance between source and target classes. The noise is chosen by generating multiple images with different noise levels and choosing the level where the semantic shift between the source and target images is the highest.

The proposed augmentation is evaluated on image classification tasks, in few-shot and long-tail distribution settings.

### Strengths
- The proposed approach allows incorporating diversity into the image generation process, which is a crucial aspect in diffusion-based image generation.
- The paper effectively illustrates the importance of selecting an appropriate noise level in text-conditioned image generation.
- The proposed augmentation is evaluated with extensive experiments on image classification in few-shot and long-tail settings.

### Weaknesses
**Method section**
My main concern regards the automatic noise level selection process. It involves generating multiple images with various noise levels and selecting the one where the semantic shift is the highest. This seems highly inefficient given the time required to generate these images.

**Data augmentation.** 
I am confused about the *weak* and *strong* augmentation policies GeNIe is compared to. Are strong augmentations (random color jitter, random grayscale, Gaussian blur) applied in addition to weak augmentations (random resize crop, random flipping)? Otherwise, why are the weak augmentations solely geometric, and the strong ones solely photometric? 
A balanced policy combining both geometric and photometric transformations could be a better contender. For example, it could consist of random resize crop (with e.g., a scale of 0.4), random flipping, color jittering, and maybe MixUp or CutMix on top.

**Visualizations.** 
The PCA representations of DINOv2 in Figure 5 could be improved and expanded. DINOv2's representations are excellent, and their PCA is usually very insightful.

### Questions
**Visualizations.** Improve visualization of the PCA over DINOv2's embeddings as suggested in Weaknesses section. Also, increasing the resolution of images across all figures would help fully appreciating the variations in image generation. 

**Data augmentation.** Run experiments with data augmentation policies combining both geometric and photometric transformations, as suggested in Weaknesses section.

**Datasets.**
In the supplementary material Table A1, the augmentation is evaluated on fine-grained classification by training a SVM on DINOv2's pretrained **ViT-g**. This evaluation is quite insightful and would deserve being integrated in the main paper. To make space, consider relocating some few-shot table contents to the supplementary. It would also be very interesting to see the same evaluation in the non-few-shot setting (*i.e.* training with the full training set), which could be directly compared to the linear evaluation results reported by DINOv2. Note that for Aircraft, DINOv2 evaluates on the **variants** categories. 

**Minor remarks on formatting.**
- Consider using *multicol* to improve table readability.
- Please write **ViT-g** instead of **ViT-G** for DINOv2's model.

### Soundness
3

### Presentation
3

### Contribution
3
