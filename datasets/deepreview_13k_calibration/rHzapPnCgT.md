# Advancing Pose-Guided Image Synthesis with Progressive Conditional Diffusion Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Recent work has showcased the significant potential of diffusion models in pose-guided person image synthesis.
However, owing to the inconsistency in pose between the source and target images, synthesizing an image with a distinct pose, relying exclusively on the source image and target pose information, remains a formidable challenge.
This paper presents \textbf{P}rogressive \textbf{C}onditional \textbf{D}iffusion \textbf{M}odel\textbf{s} (PCDMs) that incrementally bridge the gap between person images under the target and source poses through three stages.
Specifically, in the first stage, we design a simple prior conditional diffusion model that predicts the global features of the target image by mining the global alignment relationship between pose coordinates and image appearance.
Then, the second stage establishes a dense correspondence between the source and target images using the global features from the previous stage, and an inpainting conditional diffusion model is proposed to further align and enhance the contextual features, generating a coarse-grained person image.
In the third stage, we propose a refining conditional diffusion model to utilize the coarsely generated image from the previous stage as a condition, achieving texture restoration and enhancing fine-detail consistency.
The three-stage PCDMs work progressively to generate the final high-quality and high-fidelity synthesized image.
Both qualitative and quantitative results demonstrate the consistency and photorealism of our proposed PCDMs under challenging scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a three-stage diffusion pipeline to perform human pose transfer in a progressive way. The first stage predicts a global alignment feature to address the pose-level alignment and the second stage further aligns and enhances the contextual features to generate a coarse result. Finally, the third further refine the details according to the source image. The experiments demonstrate the SOTA performance of the proposed method.

### Strengths
- The proposed method is conducted in a coarse-to-fine paradigm. The technical novelty of each component is not high. While the whole system combining three diffusion stages can achieve new SOTA performance on the human pose transfer task.

- Comprehensive experiments, ablations and user studies have been conducted to show the effectiveness of the proposed method.

- The paper is well-written and easy to follow.

### Weaknesses
 - The qualitative ablation in Figure 8 is good to show the effectiveness of each component of the proposed method. However, the quantitive ablation is also very important. Besides, I would expect adding results of PCDMs w/o refining in Table 1.

- The refining results reported on different methods are on different samples. To better understand the refining benefits for different methods, it would be good to show the results of before-refining and after-refining on the same samples both quantitatively and qualitatively. For example, authors can add visual samples in Figure 10, and add quantitative results of PIDM + refining. I wonder if PIDM + refining can also achieve close performance.

- According to the ablation study, the features predicted by the first stage is important for pose-level alignment. I would expect more analysis of the progressive alignment procedure. For example, the authors may make some visual analysis based on the features, such as pixel correspondence or warp results similar to CoCosNet.

- In the metric section, it would be good to add references for R2G, G2R, and Jab to make the paper more self-contained.

- I would suggest adding some samples of source image with invisible logo and target image with visible logo to the main paper. Otherwise, one may be concerned about the overfitting issue.

- Since the proposed method has three diffusion stages, I wonder if its time cost will be much higher. Some analysis of the inference time could be discussed, which is important for practical applications.

- The pipeline contains stages and such a coarse-to-fine paradigm has been adopted in other works in different ways. For example, [a,b] also adopt a human prior + inpaint + refinement strategies. More discussions on the whole pipeline and related works could make the paper more comprehensive.

### Questions
- A quantitive ablation study is needed.
- The qualitative refining comparisons with PIDM + refining is necessary.
- A visual analysis of the progressive alignment procedure at each stage is needed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Progressive Conditional Diffusion Models (PCDMs) that tackles pose-guided person image synthesis with three stages: 1. predicts the global feature of target image; 2. establish dense correspondence and inpaint; 3. enhance and refine details. The authors show that the proposed method outperforms prior work.

### Strengths
1. The proposed method is clear and well-motivated. Studying the stage decomposition for solving a specific task with diffusion models could be a worthy contribution.
2. The evaluation is comprehensive, and the proposed method show advantages over prior works in general, with user study and clear visualization.
3. The effect of different components are studied with ablations, which further demonstrated the effectiveness of the proposed techniques and provides a better understanding of the proposed method.

### Weaknesses
In Table 1, the FID of the proposed method is sometimes worse than the prior work PIDM. Since both models are diffusion models, what are the potential main reasons that PIDM has a better FID, which is inconsistent to the user study / visualization that shows the proposed method is better? It would be beneficial to have a more in-depth discussion on the nuances of FID in this context, especially given the discrepancy with other evaluation metrics and qualitative results. Specifically, are there known biases in FID that might favor PIDM's outputs, or are there specific characteristics of the generated images that are not well-captured by FID, such as the preservation of fine-grained details or the overall structural coherence?

[minor]
"Although PCDMs have a lower FID score than PIDM" -> "worse FID score"?

### Questions
In Figure 6 visualization, it seems the proposed method is much better at the reconstruction of text patterns. Is this because the proposed method utilize a pretrained stable diffusion v2? How much performance gain over prior works could be due to having a pretrained stable diffusion v2?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Progressive Conditional Diffusion Models (PCDMs) for pose-guided person image synthesis. Unlike existing diffusion-guided methods that directly generate an image from source image and target pose, PCDMs progressively predict the global feature, inpaint a coarse target image, and further refine it with a conditional diffusion model. Qualitative and quantitative results show that the proposed method can effectively generate images that are structurally aligned with the target pose while preserving faithful and detailed texture from the source image. It achieves the state-of-the-art performance on the DeepFashion and Market-1501 datasets in terms of both objective metrics and user study.

### Strengths
S1: Sensible model design
The idea of aligning source and targets progressively at the image, pose, and feature levels is sensible and shown to be effective. The design of the prior conditional diffusion model and inpainting conditional diffusion model are quite interesting and technically sound.

S2: Convincing qualitative and quantitative results
The visual results show a consistent improvement from prior methods in terms of pose/structural alignment with the target pose as well as texture details and faithfulness to the source image. Quantitatively, PCDMs produce slightly higher FID than a prior method (PIDM) but outperforms existing methods in other metrics. The user study also show a clear preference for PCDM results over other methods.

S3: Good writing
The paper is well-written and easy to follow overall.

### Weaknesses
W1: Model complexity and computation overhead
The proposed framework is quite complicated and involves training multiple diffusion models whose inputs/outputs depend on one another. Since it is done in a multi-stage fashion, I’m wondering if the model performance is sensitive to certain training strategies or hyper-parameter tuning. Perhaps a more detailed quantitative ablation study can better justify the model design. Also, it would be good to show the computation overhead of each stage as well as the training/inference time.

W2: Incomplete ablation study
Section 4.2 shows qualitative results of the ablation study. However, quantitative comparisons of these variations are missing. Since each progressive training stage requires additional computation overhead but the visual differences between B2, B3, and full model are quite subtle, it is essential to show more evidence to justify the effectiveness of individual components.

### Questions
[Questions]

* What is the overall training and inference time and how is it compared to the prior methods?
* Why use different image encoders (CLIP and DINOv2) in different stages?
* Are the MLP networks in the inpainting stage (Figure 4) and refining stage (Figure 5) the same?
* Do you use the same guidance scale w in all training stages?

[Minor suggestions]

* Figures 1 and 2 seem to have a lot of redundancy. Maybe consider consolidating them into one?
* Typo in user study paragraph 2: “J2b” -> “Jab”
* Typo in ablation study paragraph 2: “Although the personal images generated by B2 can retain the appearance of the source image is limited”

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new pipeline based on image diffusion to tackle pose-guideed human image generation problem. The problem is decomposed into three stages, each stage requiring a separate network. At least two stages use a diffusion process, which means they involve multiple iterations, with a neural network inference step at each iteration. The first stage extracts features from the source image and source and target pose encodings. Next stage generates a coarse image, and the final stage involves refinement of the image.

The results outperform state-of-the-art in most metrics with a significant margin. The code and models will be available upon acceptance.

### Strengths
The paper outperforms state-of-the-art on a challenging DeepFashion dataset, as well as on the Market-1501 dataset, both in algorithmic metrics and according to a user study. User study in particular shows a big gap between the results of the proposed method and the competitive methods.

### Weaknesses
The paper does not clearly define its novelty. The contributions are formulated very vaguely. For example, "we propose a novel inpainting conditional diffusion model to explore the dense correspondence between source and target images" - what does "explore" really mean in this sentence? "we introduce a new refining conditional diffusion model by further using post hoc image-to-image techniques to enhance the quality and fidelity of synthesized images." - what is new in this model? Is it a typical diffusion model for image refinement, or is there something special? All in all, it is hard to say whether the theoretical/technical novelty is significant enough.

Next, the method is described quite inaccurately. Only red arrows in Fig. 2 indicate that there is some iterative process of image generation. The paper should describe in details the whole process.

x_t should go under the expectation (E) symbol in (3), because x_t is x_0 plus random noise, am I right?

"Additionally, we add an extra embedding to predict
the target global embedding." - what is the target global embedding exactly? Is it a feature vector representation of the target image?

Fig. 3 shows some noisy image labelled as ‘Target’ fed into the Image Encoder - what is that exactly?

In 3.3., “ To prevent confusion between black and white in the source and
target images,” - unclear

"the timestep embedding" - means the timestep of the diffusion model, right?

In (5), x_0 is under the expectation symbol, but not in the formula - why?

In Fig. 4, what do the noisy Source and Target images actually represent?

In general, to disuambiguate the text, I would suggest to reserve a term ‘target’ only for the dataset target image, and call a generated image aimed to resemble the target as ‘target estimate’.

In the experiments section there are no images for ‘Market-1501’ results. The results for DeepFashion show un-natural faces, and all faces look the same. This makes me think that the performance of the model for person re-identification will be limited, however the experiments show good performance on Market-1501. Would be nice to see some illustrations.

How long does it take to generate a new image using the proposed pipeline?

### Questions
What is novel in the submission? I do not assume there is no novelty at all, but I'd like to see a clear formulation of the novelty.

How does the whole process of image generation look like? How many iterations are used?

x_t should go under the expectation (E) symbol in (3), because x_t is x_0 plus random noise, am I right?

"Additionally, we add an extra embedding to predict
the target global embedding." - what is the target global embedding exactly? Is it a feature vector representation of the target image?

Fig. 3 shows some noisy image labelled as ‘Target’ fed into the Image Encoder - what is that exactly?

In 3.3., “ To prevent confusion between black and white in the source and
target images,” - unclear

"the timestep embedding" - means the timestep of the diffusion model, right?

In (5), x_0 is under the expectation symbol, but not in the formula - why?

In Fig. 4, what do the noisy Source and Target images actually represent?

In general, to disuambiguate the text, I would suggest to reserve a term ‘target’ only for the dataset target image, and call a generated image aimed to resemble the target as ‘target estimate’.

In the experiments section there are no images for ‘Market-1501’ results. The results for DeepFashion show un-natural faces, and all faces look the same. This makes me think that the performance of the model for person re-identification will be limited, however the experiments show good performance on Market-1501. Would be nice to see some illustrations.

How long does it take to generate a new image using the proposed pipeline?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
