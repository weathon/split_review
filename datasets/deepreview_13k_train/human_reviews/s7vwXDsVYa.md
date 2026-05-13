# Conditional Diffusion on Web-Scale Image Pairs leads to Diverse Image Variations

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Generating image variations, where a model produces variations of an input image while preserving the semantic context has gained increasing attention. Current image variation techniques involve adapting a text-to-image model to reconstruct an input image conditioned on the same image. We first demonstrate that a diffusion model trained to reconstruct an input image from frozen embeddings, can reconstruct the image with minor variations. Second, inspired by how text-to-image models learn from web-scale text-image pairs, we explore a new pretraining strategy to generate image variations using a large collection of image pairs. Our diffusion model \textit{Semantica} receives a random (encoded) image from a webpage as conditional input and denoises another noisy random image from the same webpage. We carefully examine various design choices for the image encoder, given its crucial role in extracting relevant context from the input image. Once trained, \textit{Semantica} can adaptively generate new images from a dataset by simply using images from that dataset as input. Finally, we identify limitations in standard image consistency metrics for evaluating image variations and propose alternative metrics based on few-shot generation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses on the task of generating image variations and proposes the Semantica model. Unlike traditional diffusion model training, Semantica is trained on web-scale image pairs. It receives a random (encoded) image from a webpage as conditional input and denoises another noisy random image from the same webpage. Additionally, the paper explores the impact of different image encoders on the results.

### Strengths
1. This paper is easy to understand.
2. The proposed method achieves good results on several benchmarks.

### Weaknesses
1. I have some doubts about the task of generating image variations. The model trained in this paper only supports image input and does not support text guidance, so it doesn’t seem to have strong practical value for real-world image editing. Additionally, many AIGC models already support various tasks such as image editing and style transfer. Therefore, I don't quite understand the value of the generating image variations task.
2. Emu2 [1] has already discovered that using CLIP image embeddings as conditional inputs for training a diffusion model can successfully reconstruct images, which is similar to the findings in this paper.
3. From the visual results, it is difficult to see any advantage of the proposed method over IP-Adapter. Moreover, IP-Adapter has broader application scenarios, as it can adapt to various text-to-image models.

### Questions
Refer to Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new model, Semantica, which generates image variations given contextual input images. The model is trained on web-scale image pairs. Specifically, it is trained with pairs of images from the same webpage. Multiple design choices are discussed in the paper, such as the selection of the image encoder, diffusion decoder, etc. The model is evaluated on a few-shot version of FID, recall, and precision for the generation of image variations and outperforms prior works such as SD-v2, IP-adapter, and Versatile Diffusion.

### Strengths
* Generating diverse image variations by training on images from the same webpage is both simple and interesting.
* The paper is well-written and easy to follow. The visualizations seem to outperform the prior works listed in the paper.
* The designs and ablation studies of different model components are well explained.

### Weaknesses
 * There is a missing comparison with some related work, such as RIVAL [1] which also targets the image variation task.
* Few-shot FID, precision, and recall may not be sufficient to fully quantify performance. Some metrics proposed in the table 1 of RIVAL [1] could provide more insightful for evaluations.
* There is a lack of a user study to compare different methods, which would be more convincing, as numerical metrics may not fully quantify performance.

### Questions
1. In eqn 1, why there is 2 variable t? One of them is context?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper works on image variations generation based on two main observations. Firstly, conditional diffusion models with frozen condition embeddings can reconstruct the image with minor variations. Secondly, web-scale image can be used to train image variation models. This paper then examine various design choices for condition representation generation given its crucial role in the proposed method, and find DINOV2 can provide good image representation for better image variation generation.

### Strengths
1. With web-scale images, this paper successfully find a good application on top of it to perform Image variation generation, which is inspiring and effective as illustrated in the experiments section.
2. The final conclusion that DINOV2 produces image representation for better image variations is also interesting, explaining self-supervised representation learning is promising in achieving effective image generation/editing.
3. The proposed new way of evaluate performance of image variation techniques seems interesting and inspiring.

### Weaknesses
1. The analysis on image encoder part for image variation (sec 2.2) seems not informative enough, although it's one main contribution of the paper, as it's common sense that the effectiveness of conditional representation is crucial for image generation. The paper lacks a detailed exploration of why DINOv2 embeddings are superior for this task compared to other common self-supervised methods. It's not enough to simply state that DINOv2 works well; a deeper analysis into the properties of the embeddings that make them suitable for image variation is needed. For example, do the learned features capture more fine-grained details or are they more robust to variations in style and composition? 
2. A new application of web-scale image for image variation is not well explained. It's not clear how the authors come up with this idea of using web-scale image for image variation, making it hard to evaluate the significant of the contrition. The paper needs to elaborate on the specific challenges of using web-scale data for this task and how the proposed method addresses them. The motivation behind choosing web-scale data over other datasets should be clearly articulated, including the potential benefits and drawbacks.
3. Data filtering should be clearly introduced as it's one of the main contribution. However, Sec. 5 is not clear (see Questions 3). The paper lacks a clear explanation of the filtering criteria and the impact of different filtering thresholds on the final results. The method used to determine the similarity thresholds is not well-defined, and the paper should provide more details on how these thresholds were chosen and validated. The impact of the filtering process on the diversity and quality of the generated images should be analyzed.
4. The experimental results section seems weak in proving superiority of the proposed solution. (see Questions 4) The paper does not provide a comprehensive comparison with existing image variation techniques, and the metrics used do not fully capture the diversity and quality of the generated images. The analysis of Fig. 3 is insufficient to demonstrate the superiority of the proposed evaluation metric, and more detailed analysis is needed to justify its effectiveness.

### Questions
1. Image representation learning, e.g. self-supervised, image reconstruction based, contrastive learning and etc, are wildly studied. How the other encoders perform compared with DINO? e.g. MAE (ref 1)
2. Web-scale image is indeed Episodic WebLI in this paper. Are there any other web-scale images? Why choose Episodic WebLI in particular?
3. Please explain robustness of the method with respect to the cleanest of the web-scale images (line 306-315), e.g. what if the web-scale images are not well filtered out, how the method perform then?
4. As explained in the paper, the commonly used metrics, e.g FID, fail to evaluate variation performance. However, it's still not clear how the proposed solution (sec 7) can be effective in measure diversity, e.g. Fig. 3 should be further analysed to explain diversity superiority.

re1: Masked Autoencoders Are Scalable Vision Learners, CVPR 2022

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper if focus on the challenge of generating image variations, with large diversity while preserving the the conditions' semantics.
The authors suggest a new pre-training method exploiting the semantic relations of images within the same web page.   
It also discuss the challenge of measuring image diversity and suggest a few-short metrics approach

### Strengths
- The idea of using the semantic relations of image pairs with in the the same web page is a good contribution which can lead to even more  research direction then the focus of this paper
- The observation of image diversity issue in current SOTA , mitigate it and suggest new metric to evaluate it

### Weaknesses
The claim that "Standard image-level metrics such as LPIPS and distribution-level metrics such as FID fail
to capture diversity in image variations" is not backup with number and/or examples

### Questions
Please provide specific examples or quantitative evidence demonstrating how LPIPS and FID fail to capture diversity in image variations and should do a comparative analysis between the proposed one-shot metrics and LPIPS/FID, including specific examples where the new metrics better capture diversity.

### Soundness
3

### Presentation
3

### Contribution
3
