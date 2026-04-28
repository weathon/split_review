# HFDream: Improving 3D Generation via Human-Assisted Multi-view Text-to-Image Models

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Large-scale text-to-image models have demonstrated the potential for performing text-to-3D synthesis. However, existing approaches, e.g., DreamFusion, suffer from unstable 3D optimization due to the limitations of current text-to-image models that they struggle to synthesize images from certain viewpoints even when specified in the text prompt. Obtaining a view-aligned image-text pair dataset is challenging due to the limited availability of such data, and the inherent subjectivity and ambiguity of view-alignment. In this paper, we propose to enhance text-to- 3D generation by learning from human feedback for generating desired views. We generate multi-view images with the text-to-image model and engage human labelers to select a valid viewpoint. Using the human-labeled dataset, we train a reward model designed to verify whether the generated image aligns with the viewpoint specified in the text prompt. Finally, we fine-tune the text-to-image model to maximize the reward score. We find that our text-to-image diffusion models fine-tuned with human feedback, coined HFDream, consistently generate diverse viewpoints without the need for multi-view datasets created from 3D assets. This leads to high-quality text-to-3D generations with consistent geometry, when combined with view-dependent prompting in DreamFusion.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to enhance text-to3D generation by learning from human feedback for generating desired views. It collects a human-labeled dataset to train a reward model and adopts this model to fine-tune a diffusion model, and this reward model can help the diffusion model generate the image aligned with the viewpoint text.

### Strengths
1. The whole idea is Intuitive and effective.
2. The reward model can help the model generate images that match the viewpoint text.
3. The paper is well written.

### Weaknesses
My main concern is the motivation of this work. Indeed, Dreamfusion has a multi-face problem since the diffusion can not generate the image aligned with the camera. There are two main methods that can solve this problem. First type: we can train a camera-aware diffusion model like Zero123 and MVdreamer. These models can generate an image aligned with the camera.  These methods use the camera parameter as guidance, which is much more correct than viewpoint text since the viewpoint text only has three settings (front, side, and over). Second type: We can introduce the Controlnet or the mesh as the 3D prior to solve the multi-face problem.  
So, what is the advantage of human feedback? The whole process is time-consuming and cumbersome, and I found the results were not very well either.  Meanwhile, in addition to the multi-face problem, the proposed method still has the same issues with Dreamfusion: Over smooth and over-saturated.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work presents a text-to-3D pipeline by using human feedback to enhance multi-view image generation. Both text-to-3D and personalized text-to-3D tasks are performed to evaluate the proposed HFDream.

### Strengths
++ Extensive human survey evaluation is performed.

++ It is interesting to apply HFDream for Text-to-3D DreamBooth generation task.

### Weaknesses
-- The whole method seems a simple human-in-the-loop engineering pipeline and is composed of several existing techniques (ImageReward and DreamFusion). The main difference is the fine-tuning of ImageReward tailed for multi-view image generation, which is somewhat not novel.

-- The experimental results are not convincing, due to the lack of many recent state-of-the-art text-to-3D baselines (e.g., Magic3D and Fantasia3D) in performance comparison.

-- I also have the concern on the human-labeled dataset which is a subset of ImageReward-v1.0 data and only has 200K pairs. So how to testify that the generalization of fine-tuned text-to-image model is not degraded?

Moreover, the evaluation prompt set is extremely small (only 61 text prompts). At least authors should report their results over the most test prompts in DreamFusion website (https://dreamfusion3d.github.io/gallery.html).

### Questions
The overall technical contribution is limited, and more strong baselines should be included for performance comparison.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors adopt RLHF into text-to-image diffusion model and propose a new text-to-image diffusion model, termed as HFDream, which can produce viewpoint specified images with the text prompt. Furthermore, HFDream combined with DreamFusion can lead to high-quality text-to-3D generations. Specifically, they firstly collect multi-view data using human feedback, then train a reward model using these multi-view data. Subsequently, they finetune a text-to-image diffusion model with the reward model to learn multi-view image generation. Finally, DreamFusion with the finetuned diffusion model can enable high-quality 3D generation. In addition, they conduct extensive experiments to validate the proposed method.

### Strengths
+ The proposed method is an alternative to improve the geometric consistency of 3D generation. It adopts RLHF into diffusion models, leading to multi-view image generations and avoiding large-scale 3D assets.  Besides, it can produce pleasant 3D generations and is validated with various experiments.
+ This paper is written well and easy to follow. In addition, it provides enormous quantitative and qualitative results to validate the proposed method.

### Weaknesses
- To my knowledge, collecting multi-view data using human feedback is costly and somewhat difficult for some viewpoint, such as backside views. Moreover, as shown in section 4.2, it is essential to collect larger and more diverse human datasets  to improve generalization on more and unseen prompts. Thus, I raise a concern: is collecting these multi-view data cheaper than 3D assets? Specifically, the authors should provide a detailed cost analysis, including the time and resources required for human annotation, and compare it with the cost of acquiring or creating 3D assets with comparable quality and diversity. This comparison should consider not only the monetary cost but also the time and effort involved, as well as the potential limitations in terms of viewpoint coverage and annotation consistency.
- For the objects used in this paper, it is easy for human to identify their view direction, such as front view. But, there are objects for which different views is the same. Moreover, it is difficult to identify direction for 3D scenes. Thus, how to solve these problems with the proposed method? The authors need to address the ambiguity in view direction for certain objects, and how their method would handle scenes where view direction is not well-defined or is highly subjective. Furthermore, the paper should discuss how the human annotators were trained to identify view directions consistently and what measures were taken to ensure that the annotations are accurate and reliable, especially for complex or ambiguous cases. This discussion should include specific examples of such cases and how they were resolved during the annotation process.
- To validate the proposed method, the authors only use DeepFloyd-IF (pixel-based model) as their baseline text-to-image model. But, the proposed method has a generalization on diffusion models. Thus, it is better to validate the proposed method on other diffusion models, such as StableDiffusion (latent-based model). The authors should provide a comprehensive evaluation of their method across a variety of diffusion models, including both pixel-based and latent-based models, to demonstrate the general applicability and effectiveness of their approach. This evaluation should include a comparison of the performance of the proposed method on different models, as well as an analysis of any model-specific challenges or limitations.

### Questions
- As shown in the experiments, HFDream produces unnatural images. In detail, these images are oversaturated. In contrast, IF generates realistic images, although it does not have a good geometric consistency. Is the guidance scale high for HFDream?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
