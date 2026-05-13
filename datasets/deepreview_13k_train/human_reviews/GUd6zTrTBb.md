# Zero-shot Text-based Personalized Low-Light Image Enhancement with Reflectance Guidance

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Recent advances in zero-shot low-light image enhancement have largely benefited from the deep image priors encoded in network architectures. However, these models require optimization from scratch for each image and cannot provide personalized results based on user preferences.
In this paper, we propose a training-free zero-shot personalized low-light image enhancement model that integrates Retinex domain knowledge into a pre-trained diffusion model, enabling style personalization based on user preferences specified through text instructions. Our contributions are as follows:
First, we incorporate the total variation optimization into a single Gaussian convolutional layer, enabling zero-shot Retinex decomposition. Second, we introduce the Contrastive Language-Image Pretraining (CLIP) model into the reflectance-conditioned sampling process of Denoising Diffusion Implicit Models (DDIM), guiding the enhancement according to user-provided text instructions. Third, to ensure consistency in content and structure, we employ patch-wise DDIM inversion to find the initial noise vector and use the reflectance as a condition during the reverse sampling process.
Our proposed model, RetinexGDP, supports any image size and produces noise-suppressed results without imposing extra noise constraints. Extensive experiments across nine low-light image datasets show that RetinexGDP achieves performance comparable to state-of-the-art models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new model called RetinexGDP which leverages Retinex decomposition model and DDIM inversion to address the zero-shot text-guided low-light enhancement problem. Specifically, the light component is estimated using a total-variation tailored Gaussian convolutional layer, and the enhanced image is estimated with the help of patch-wise DDIM inversion to maintain content and structure consistency. Experiments on multiple datasets indicate that the proposed method achieves comparable performance with state-of-the-art methods in terms of noise suppression and enhancement quality.

### Strengths
++ The experiments take various datasets (specifically 9 datasets) into consideration, providing a thorough evaluation of the proposed model.

### Weaknesses
-- My main concern is the limited novelty of the paper. The proposed method combines Retinex composition with GDP, and enables textual control. Most of the used techniques come from existing work, e.g., GDP, Retinex model, patch-wise DDIM inversion. The introduced total variation layer borrows the idea of Yeh et al. (2022). The proposed idea is not that inspiring. 

-- The effectiveness of the model is not impressive. The model does not achieve state-of-the-art performance compared to other methods. Also, the proposed model does not achieve consistent performance across different metrics, as seen from Table 1, 2, and 3. Besides, the qualitative examples shown in Figure 5, 12, and 15 indicate that the proposed method could suffer from poor fidelity (some enhanced images have unnatural colors and styles (e.g., Figure 5) while some of them have over-smoothed effect (e.g., Figure 15)).

-- The paper proposes to replace the original total variation layer with fixed Guassian initialized kernels. I wonder whether the layer can still be called "total variation layer" or not. I think it has nothing to do with the "total variation layer".

-- The introduced patch-wise DDIM inversion has high computational complexity, which makes the proposed method less appealing and hinders possible application.

-- The textual control ability and granularity has not been fully demonstrated.

### Questions
1. Please further elaborate the proposed Guassian convolutional layer, and discuss its significance with thet original total variation layer.

2. Please futher explain how to specifically ensure content consistency across different textual prompts. More examples would be helpful.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces RetinexGDP, a training-free method for personalized low-light image enhancement, based on Retinex theory and a pre-trained text-to-image diffusion model. The method begins by employing a single Gaussian convolutional layer to perform Retinex decomposition. Subsequently, the decomposed reflectance is used as a condition in the diffusion model. RetinexGDP has been evaluated across several low-light image datasets and demonstrates performance comparable to state-of-the-art (SOTA) models.

### Strengths
1. Integrating Retinex information into deep learning models enhances the interpretability of the proposed method.

2. RetinexGDP is a training-free, zero-shot method that generates enhanced images based on user preferences via text instructions.

### Weaknesses
1. In Figure 1, the gray line representing the loss function is not visible. What do the blue and yellow lines represent? It seems there may be some confusion regarding these lines.

2. Decomposing illumination and reflectance from low-light images is generally challenging. Many supervised methods struggle with accurate decomposition. How can the use of the Gaussian filter and the TV proximity operator ensure effective decomposition in this method?

3. Why is gamma correction applied after estimating illumination, and why is the reflectance obtained only after applying gamma correction? Additionally, the values for the gamma correction factor in Equation (4) and the \lambda in Equation (3) are not provided. I hope the authors could clarify these  parameters.

4. Does the illumination shown in Figure 3 represent the illumination before or after the gamma correction? Additional visualizations would aid in better evaluation. In my view, the reflectance appears over-saturated, as do the visual results presented later. I am unsure whether this over-saturation is an effect of integrating gamma correction.

5. Although the paper claims that the proposed method is a training-free, zero-shot method, several loss functions are introduced. It is unclear which components are fixed and which are learnable. I hope authors provide a diagram of the gradient flow for clarity.

6. The proposed method does not demonstrate enhanced performance compared to RetinexDIP, which is also a training-free method. Furthermore, the differences between results with different text instructions appear minimal, as illustrated by the bottom line in Figure 5.

### Questions
The questions are listed up in the Weaknesses. A point-by-point response would be helpful. I will consider raising my rating if all concerns are well-addressed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces RetinexGDP, a training-free, zero-shot personalized low-light image enhancement model that integrates Retinex theory into a pre-trained diffusion model. The authors overcome limitations of existing methods, such as per-image optimization and lack of personalization. Extensive experiments demonstrate that RetinexGDP achieves state-of-the-art performance across nine low-light datasets.

### Strengths
1. The paper proposes a training-free zero-shot personalized low-light image enhancement model that allows for style personalization based on user-provided text instructions.
2. The introduction of the CLIP model into the reflectance-conditioned sampling process of DDIM allows for enhancement guided by user text instructions, increasing model flexibility.

### Weaknesses
1. Why use Reflectance directly for enhancement, rather than enhancing the entire image? Wouldn't this approach lose information contained in the Illumination?
2. The proposed method is training-free, so how can the loss function be optimized?
3. The colors used in the caption about the loss function in Figure 1 do not match the colors used in the figure itself.
4. There is a lack of specific explanation regarding the image content and style distance metrics L_c and L_s in Equation 5.
5. The authors should compare some recent unsupervised SOTA methods to demonstrate the effectiveness of the proposed method, such as LightenDiffusion (ECCV2024) and FourierDiff (cvpr2024).

### Questions
Please refer to the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents RetinexGDP, a training-free, zero-shot personalized low-light image enhancement model that integrates Retinex domain knowledge into a pre-trained diffusion model. Key contributions include using total variation optimization for zero-shot Retinex decomposition, incorporating the CLIP model to guide enhancements based on user text instructions, and employing patch-wise DDIM inversion for consistent results. RetinexGDP supports any image size and delivers noise-suppressed results without extra noise constraints, achieving performance comparable to state-of-the-art models across nine low-light image datasets.

### Strengths
1. Well-designed structure, CLIP is introduced into the diffusion model, and the enhancement-related reflectivity is used as conditional information to assist in the generation of enhanced images.
2. The author incorporate the edge-aware property of total variation optimization into a single Gaussian convolutional layer, aiming to achieve zero-shot Retinex decomposition.
3. A large number of experiments have proved the effectiveness of the method.

### Weaknesses
1. The inconsistent use of metrics confuses me. This work uses different metrics on different datasets. Why is NIQE used in the ablation experiment but not in the comparison experiment? The cited NIQMC can also be used on the LOL and VELOL datasets.
2. In addition to this work, there are other work[1] that adopt similar core ideas. Compared with their methods, what are your significant advantages?

[1] He C, Fang C, Zhang Y, et al. Reti-diff: Illumination degradation image restoration with retinex-based latent diffusion model[J]. arXiv preprint arXiv:2311.11638, 2023.

3. Some experimental details need to be stated in the paper, such as the specific yperparameters of for each loss function term.

### Questions
please refers to the weakness

### Soundness
3

### Presentation
3

### Contribution
3
