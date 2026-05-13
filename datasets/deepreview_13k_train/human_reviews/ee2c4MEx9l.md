# TweedieMix: Improving Multi-Concept Fusion for Diffusion-based Image/Video Generation

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Despite significant advancements in customizing text-to-image and video generation models, generating images and videos that effectively integrate multiple personalized concepts remains a challenging task. To address this, we present TweedieMix, a novel method for composing customized diffusion models during the inference phase. By analyzing the properties of reverse diffusion sampling, our approach divides the sampling process into two stages. During the initial steps, we apply a multiple object-aware sampling technique to ensure the inclusion of the desired target objects. In the later steps, we blend the appearances of the custom concepts in the de-noised image space using Tweedie's formula. Our results demonstrate that TweedieMix can generate multiple personalized concepts with higher fidelity than existing methods. Moreover, our framework can be effortlessly extended to image-to-video diffusion models, enabling the generation of videos that feature multiple personalized concepts. Results and source code are in our anonymous project page

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method to fuse multiple concepts for personalized T2I diffusion-based models that are generalizable to both image and video generation. The method mainly involves two parts: (1) concept-aware sampling that coarsely localizes the concepts in the latent space, and (2) multi-concept fusion that generates the personalized concepts based on the extracted regional masks. The qualitative and quantitative results both demonstrate the effectiveness of the proposed method.

### Strengths
+ The proposed method is reasonable and intuitive.
+ The generated results of multi-concept fusion are impressive.
+ The model is properly extended from image generation to video generation.
+ From the quantitative results, the proposed method outperforms previous models.

### Weaknesses
- $t_{con}$ and $P$ are two important hyperparameters. Can the authors provide generated results with varying $t_{con}$ and $P$, while keeping all other settings fixed? It would be beneficial to see a more comprehensive analysis of how these parameters influence the quality and diversity of the generated images, particularly in terms of concept blending and localization.
- DINO [1] can extract subtle visual features that are not specific to any particular category. The metric of DINO image similarity should also be reported. The current evaluation focuses on CLIP similarity, which may not fully capture the nuances of visual feature alignment, especially when dealing with complex multi-concept compositions. A comparison with DINO similarity would provide a more robust assessment of the method's ability to preserve fine-grained details.
- The evaluation is conducted on combinations of more than three concepts; however, the paper does not present any results of combinations involving more than three concepts. While the method is claimed to be generalizable, the absence of results with a higher number of concepts raises questions about its scalability and performance in more complex scenarios. It is important to demonstrate the method's effectiveness when combining a larger number of concepts to fully validate its generalizability.
- It is recommended to compare the sampling time of the proposed method with that of other models. The current evaluation lacks a comparison of computational efficiency, which is crucial for practical applications. Providing a detailed analysis of the sampling time would help assess the method's feasibility for real-world use cases.
- Missing reference on unsupervised multi-concept extraction [2].

### Questions
- Please see the weaknesses.

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
3

### Summary
This paper introduces a new approach called TWEEDIEMIX for multi-concept text-to-image generation. The author introduce a tuning-free approach during the inference stage and divides the process into two main stages. The key contribution of this paper is using a resampling strategy and multi-concept fusion sampling enabling generate multiple personalized concepts with higher fidelity than existing methods.

### Strengths
1. The idea is easy to follow and the paper is well written.
2. The results on Custom Concept 101 dataset outperforms the previous baselines, demonstrating better generation qualities compared to the concept personalization methods. 
3. The author's code has been open-sourced, which is somewhat helpful to the community.

### Weaknesses
1. My main concern lies in the technical contribution of this paper. It seems like an incremental work of ConceptWeaver[1] which is also a training-free method that combines multiple concepts during inference.
2. In terms of qualitative results, there doesn't seem to be a significant improvement compared to ConceptWeaver which is also can handle more than two concepts.

### Questions
Please refer to the weaknesses above.

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
3

### Summary
The paper introduces TweedieMix, a novel method designed to customize diffusion models during the inference phase, particularly for the challenge of integrating multiple personalized concepts in image and video generation. It operates by dividing the reverse diffusion sampling process into two distinct stages: an initial stage that uses multiple object-aware sampling to ensure the inclusion of desired target objects, and a later stage that employs Tweedie’s formula to blend the appearances of custom concepts in the de-noised image space. The results indicate that TweedieMix outperforms existing methods in generating images and videos with multiple personalized concepts with higher fidelity.

### Strengths
1、The multi-concept generation results looks good；
2、The authors illustrate the framework details and experimental setting well.

### Weaknesses
1、The whole pipeline seems naive and lack of novelty.
2、Some problems exist in experimental settings.
See questions for more details.

### Questions
1、Making use of Text-SAM and Tweedie’s formula do not contribute to the novelty.
2、Each concept a model. I suspect the performance gain may derived from the overfitting of specific concept. And the hard mask composition seems like a naive post processing. The whole framework is more like a system which is designed under substantial ablation experiments and lack of novelty and essential understanding towards this task.
3、The extension to video, if I do not misunderstand, is a technical trick on a off-the-shell I2VGen-XL. I2VGen-XL is finetuned from ModelScopeT2V with a large dataset. While DreamVideo use ModelScopeT2V only for subject injection with a little amount of custom videos. Maybe this need further discussion and I'd like to see opinions from other reviews.

### Soundness
3

### Presentation
3

### Contribution
2
