# ViCo: Plug-and-play Visual Condition for Personalized Text-to-image Generation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
\hszz{Personalized text-to-image generation using diffusion models has recently emerged and garnered significant interest. This task learns a novel concept (\eg, a unique toy), illustrated in a handful of images, into a generative model that captures fine visual details and generates photorealistic images based on textual embeddings.
In this paper, we present \modelname, a novel lightweight plug-and-play method that seamlessly integrates visual condition into personalized text-to-image generation. \modelname stands out for its unique feature of not requiring any fine-tuning of the original diffusion model parameters, thereby facilitating more flexible and scalable model deployment. This key advantage distinguishes \modelname from most existing models that necessitate partial or full diffusion fine-tuning.
\modelname incorporates an image attention module that conditions the diffusion process on patch-wise visual semantics, and an attention-based object mask that comes at no extra cost from the attention module. Despite only requiring light parameter training ($\sim$6\% compared to the diffusion U-Net), \modelname delivers performance that is on par with, or even surpasses, all state-of-the-art models, both qualitatively and quantitatively. This underscores the efficacy of \modelname, making it a highly promising solution for personalized text-to-image generation without the need for diffusion model fine-tuning

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a text2image personalization method that learns the personalization text embedding and the proposed image attention. "Image attention" is a cross-attention module to integrate visual conditions into the denoising process for capturing object-specific semantics. A mask that is derived from the cross-attention map between reference image and text is applied to the "image attention" used to focus more on the object of the reference image.

### Strengths
- The method only requires learning relatively few parameters to effectively incorporate the information from reference image for personalized text2image generation.
- The results are very favorable compared to existing methods like DreamBooth and Textual Inversion, while having a low training time cost.
- Good ablation study and analysis provided in the paper.
- The paper is quite transparent and information-rich in many ways, which is good for reproducibility purposes.

### Weaknesses
 - In Table 4, the improvement introduced by masking is not so significant. 
- The method is incapable of using multiple reference images during inference, for more robust generation.
- Apparently, the method only works with images that have a single reference primary object.

### Questions
1. Do you use the same reference image for different model variations in the evaluation (especially T4)?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for customizing text-to-image generation models, which requires less number of parameters to be tuned and less training time compared to related works.

### Strengths
The paper proposes to introduce extra attention modules, which can introduce new concept into the diffusion process. The introduced attention modules contain much less parameters compared to the whole diffusion model, leading to more efficient fine-tuning.

Only fine-tuning introduced attention modules have the advantage of maintaining the original capability of pre-trained models, which might be important.

According to the experiment results shown in the paper, better results are obtained compared to vanilla DreamBooth. The needed training time is also much less.

### Weaknesses
The major concern is on the experiments, why do the authors only use 20 unique concepts from the Textual Inversion, DreamBooth, Custom Diffusion, rather than use a union of their testing samples or directly use the DreamBench dataset proposed in DreamBooth paper?

One important related work is missing [1], which requires fine-tuning less number of parameters compared to LoRA, and maintains the original capability of the pre-trained model. As shown in the paper, the method is also very stable (please see question in next section).

The low $T_{CLIP}$ score may indicate unsatisfactory edit-ability, thus more qualitative results in terms of complicated style change are suggested.

Although encoder-based methods are not directly related to the proposed method, comparison and discussion are strongly suggested. Especially considering the fact that encoder-based methods normally require much less fine-tuning time or are even tuning-free (although they need pre-training).

### Questions
Have the author considered using ground-truth mask in computing the diffusion loss (with a pre-trained model like SAM[1]), or forcing the attention map to be aligned with the mask?

In DreamBooth, when the model is fine-tuned for too much iterations, the model performance may degenerate even when augmentation data and prior loss is used. Will this also happen with the proposed method? Specifically, generated results with respect to different iterations are suggested to be shown, especially when the number of training steps are very large. This result is important as related work OFT is shown to be stable even after thousands of fine-tuning steps. 

[1]. Segment Anything. Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims to achieve personalized text-to-image generation that allows users to combine inputs of texts with example images and generates an image accordingly. Existing work on this task is either computationally inefficient or sacrifices the generation quality with computation cost. The authors propose a cross-attention based mechanism, which also has the benefit of helping isolate the foreground object using attention maps, that requires only training the cross-attention layers and optimizing the placeholder embedding. The proposed method is more efficient without sacrificing the reference object's identity.

### Strengths
The goal of this paper is to achieve personalized text-to-image generation that is lighter-weight (and faster) than existing methods with an on par quality or even better. Quantitative and qualitative results presented seem to support this.

### Weaknesses
How the proposed method avoids fine-tuning the entire diffusion model for each reference object is by using cross-attention: multi-resolution features maps of the reference image, C_I^l, are used to perform cross-attention with the intermediate outputs, n_t^l, of the main denoising UNet. With cross-attention blocks, they only train these blocks for each reference object, instead of the entire diffusion model. Using cross-attention blocks in conditioned image generation to warp a source image to target [i, iv, v, vi, vii] or to preserve a reference image's identity [ii, iii] has been a popular approach. Indeed, this may be one of the first work to explore cross-attention blocks in LDMs, but I don't think this contribution seems sufficiently novel.



### Questions
After reading both the main paper and supplementary sections, I'm still not 100% clear of the training procedure, which also raises questions for me regarding the results presented. Currently my understanding is that training is conducted for each object separately (in Sec.3.4 it reads "We train our model on 4-7 images with vanilla diffusion U-Net frozen..."), and during training, the learning of cross-attention layers and placeholder text embeddings S* are performed simultaneously (as described in Sec.3.4). If my understanding is correct, the question I have is: would the model learn better if cross-attention layers are trained with all available images (from all objects, or with any larger dataset where there are many objects, each with at least 2 images), and S* is optimized for each object? I have this question because when looking at the qualitative results, I think the preservation of the reference image's identity could be further improved, e.g., in Figure 1, the Batman toy's body pose changed in Figure 1, and in Figure 4, the cat statue's face changed, the texts on the can changed, and the drawing on the clock also changed. One possibility I can think of for why the reference image's identity is not perfect is that the cross-attention layers are not fully trained, and training with a larger dataset with a wider variety of objects may help. 

Another question I have is regarding where to incorporate cross-attention blocks. From Supplementary Section A, it mentions that the final design was incorporating cross-attention blocks in the decoder of the UNet. Existing work  [i, ii] that also use cross-attention incorporate it in both the encoder and decoder of the UNet. I wonder if this configuration was tried, and if yes, why it wasn't successful in this case?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents ViCo, a novel method for personalized text-to-image generation using diffusion models. This task aims to generate photorealistic images from textual descriptions without fine-tuning the original diffusion model. It utilizes an image attention module and a mask to condition the diffusion process on visual semantics. It outperforms existing models with minimal training, making it a promising solution for personalized text-to-image generation without the need for fine-tuning diffusion models.

### Strengths
1. This paper presents an efficient mechanism to generate object masks without relying on prior annotations, simplifying foreground object isolation from the background.

2. It is computationally efficient and non-parametric, reducing the influence of distracting backgrounds in training samples.

3. ViCo is highly flexible and easy to deploy, as it doesn't require fine-tuning of the original diffusion model.

4. The model requires no heavy preprocessing or mask annotations, making it easy to implement and use.

### Weaknesses
1. ViCo may have lower performance compared to fine-tuned methods, implying an ease-of-use vs. performance trade-off. Specifically, while the method avoids fine-tuning the entire diffusion model, it's unclear how the introduced visual conditioning module compares to the fine-tuning of the U-Net in terms of preserving fine-grained details of the object. The trade-off between computational efficiency and the ability to capture complex object semantics needs further clarification, especially in scenarios requiring high fidelity object representation.

2. The use of Otsu thresholding for mask binarization may slightly increase time overhead during training and inference for each sampling step. While the authors mention this overhead is offset by shorter training time, the impact of this thresholding on the quality of the generated masks, and consequently on the final image quality, is not thoroughly discussed. The robustness of Otsu's method across different image types and lighting conditions should be analyzed, as suboptimal masks could lead to artifacts in the generated images.

### Questions
1. Can you explain in more detail how ViCo generates object masks and incorporates them into the denoising process?

2. How does ViCo compare to other methods in terms of computational efficiency and parameter requirements?

3. Can you explain how ViCo achieves diverse poses and appearances in recontextualization and art renditions?

4. Can you clarify the limitations mentioned and how the trade-off between keeping the frozen diffusion model and not fine-tuning it affects performance?

5. How does ViCo's cross-attention method for capturing object-specific semantics differ from others, and what are its advantages?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
