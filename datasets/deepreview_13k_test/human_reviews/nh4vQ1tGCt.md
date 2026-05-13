# Forgedit: Text Guided Image Editing via Learning and Forgetting

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Text-guided image editing on real or synthetic images, given only the original image itself and the target text prompt as inputs, is a very general and challenging task. It requires an editing model to estimate by itself which part of the image should be edited, and then perform  either rigid or non-rigid editing while preserving the characteristics of original image.   In this paper, we design a novel text-guided image editing method, named as Forgedit. First, we propose a vision-language joint optimization framework capable of reconstructing the original image in 30 seconds, much faster than previous SOTA and much less overfitting.  Then we propose a novel vector projection mechanism in text embedding space of Diffusion Models, which is capable to control the identity similarity and editing strength seperately. Finally, we discovered a general property of UNet in Diffusion Models, i.e., Unet encoder learns space and structure, Unet decoder learns appearance and identity. With such a property, we design forgetting mechanisms to successfully tackle the fatal and inevitable overfitting issues when fine-tuning Diffusion Models on one image, thus significantly boosting the editing capability of Diffusion Models. Our method, Forgedit, built on Stable Diffusion, achieves new state-of-the-art results on the challenging text-guided image editing benchmark: TEdBench,  surpassing the previous SOTA methods such as Imagic with Imagen, in terms of both CLIP score and LPIPS score.

  \keywords{text-guided image editing \and visual storytelling \and  overfitting}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an optimization-based image editing method capable of performing both rigid and non-rigid editing. Additionally, the paper proposes a forgetting strategy within the UNet architecture of diffusion models to prevent overfitting. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. The writing is clear and easy to follow.
2. To achieve the desired editing, the authors propose an adaptation of DreamBooth and also incorporate the optimization strategy from Imagic. To address potential overfitting arising from a single input image, a forgetting strategy is introduced.
3. The experiments provide evidence of the effectiveness of the proposed method, both in the context of rigid and non-rigid editing.

### Weaknesses
1. The training strategy of the proposed method is similar to Imagic, with the main differences being that the authors employ BLIP to generate a caption describing the input image, and combine the first and second stages in Imagic into one. Besides, authors use DreamBooth as the backbone.

2. I find the location of the point (1-y)e_src + ye_tgt in Figure 2 confusing, and I'm uncertain why the value of y (gamma) exceeds 1 in vector subtraction. Typically, y should fall within the range [0,1] if normalization has been applied. Furthermore, It would be beneficial to include a discussion explaining why projection is more suitable for editing compared to vector subtraction, in terms of identity preservation.

3. The qualitative comparison suggests that the results produced by the proposed method may have lower resolution compared to other methods, as evident in the examples of the dog, bird, and giraffe in Figure 7. I am concerned about the potential impact of the proposed method on image quality, and I notice that there are no evaluation metrics in the paper reflecting image quality, such as Inception Score (IS) and Fréchet Inception Distance (FID).

4. It would be beneficial to include a quantitative comparison for the various components employed in the proposed method. Additionally, it's unclear why the authors chose to apply the forgetting strategy only in vector subtraction and not in projection. Further clarification on this decision would be helpful.

### Questions
Please see above weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the Forgedit for text-guided image editing. There are three key components in the Forgedit:1) Fine-tuning the framework and the text embeddings jointly; 2) The vector subtraction and projection for image editing; 3) Forgetting strategy in the UNet-Structures. The proposed method achieves state-of-the-art performance.

### Strengths
1) The paper performs extensive explorations on diffusion-based image editing. The mechanisms the authors explore include the difference between vector subtraction and projection, changes brought by keeping and dropping different weights of unet. These explorations are meaningful and can provide insights to readers.

2) The paper is well-organized and easy to follow.

3) The proposed method achieves state-of-the-art performance on the image editing benchmark.

### Weaknesses
1) There are many components that should be adjusted at the inference time. It is troublesome to adjust all these parameters manually.

2) For vector subtraction and vector projection, we need to decide which variant to use and also there are some hyper-parameters in these two variants that need to be determined.

3) For Fig. 5 and Fig. 6, it is hard to tell the settings of each column from the captions.

4) In Table 1, the quantitative results of other methods are missing.

### Questions
Please see my concerns in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Forgedit, a novel text-guided image editing method that addresses challenges in preserving image characteristics during complex non-rigid editing. It employs an efficient fine-tuning framework, vector subtraction, projection mechanisms, and innovative forgetting strategies inspired by UNet structures in Diffusion Models. Forgedit outperforms previous methods on the TEdBench benchmark, achieving state-of-the-art results in both CLIP and LPIPS scores for text-guided image editing.

### Strengths
This paper overall is clear and easy to follow.

### Weaknesses
1. Although, the paper has presented convincing results to solve image editing problems of diffusion model, the bag of tricks are now new and just work as expected. 

2. Vector subtraction has been widely used in generative image editing, in VAEs, GANs and diffusion models.

3. Vector projection is a kind of component analysis, which has been well studied in latent code manipulation in GANs.

4. Using captioner to get source prompt is straightforward, and usually it's not even required, since vision-language learning is applied.

5. Many related editing works are missing, like plug-and-play, prompt-to-prompt, etc.

6. Model ensemble has been well-known to alleviate forgetting problems, both discriminative and generative modeling.

7. How does the hyper-parameters in vector subtraction and projection affect editing results, content and editing fidelity?

### Questions
See above in Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a framework to tackle some issues like overfitting and inconsistency in common optimization-based editing methods. It presents a novel vector projection mechanism to merge the source text embeddings and the target embeddings to better preserve inversion consistency. Finally, it proposes the forgetting strategy during sampling to overcome the common overfitting issue. Empirically, it achieves SoTA performance in TEdBench.

### Strengths
– The paper has many interesting empirical observations, like using BLIP caption instead of the target prompt as the source text is more generalized and finetuning only the first few layers of the encoder/decoder leads to better generalization as well.

 – The proposed vector projection mechanism is intuitive and effective, and can better preserve the visual appearance from the ablation study.

### Weaknesses
– It is not clear why using BLIP caption as source text embedding can avoid overfitting, it is empirically observed but no explanation from the authors

– The proposed forgetting strategy is not general. Although the author ablates a lot of forgetting layers, it is not clear how to apply this strategy in the practical use case. I hope the author can provide a clear conclusion on how to choose the forgetting layers.

### Questions
– I have concerns about the optimization time required for embedding the real image, i.e. each edit operation becomes harder and longer at the wait time, what are your options on balancing editing quality and editing interactiveness?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
