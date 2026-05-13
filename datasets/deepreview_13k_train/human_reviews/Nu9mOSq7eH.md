# InstructCV: Instruction-Tuned Text-to-Image Diffusion Models as Vision Generalists

- Decision: Accept
- Scores: 5, 6, 8, 3

## Abstract
Recent advances in generative diffusion models have enabled text-controlled synthesis of realistic and diverse images with impressive~quality.~Despite~these~remarkable advances, the application of text-to-image generative models in computer vision for standard visual recognition tasks remains limited. The current de facto approach for these tasks is to design model architectures and loss functions that are tailored to the task at hand. In this paper, we develop a {\it unified language~interface}~for~computer vision tasks that abstracts away task-specific~design~choices~and enables task execution by following natural language~instructions. Our approach involves casting multiple computer vision tasks as text-to-image~generation~problems. Here, the {\it text} represents an {\it instruction} describing the task, and the resulting {\it image} is a visually-encoded {\it task output}. To train our model, we pool commonly-used computer vision datasets covering a range of tasks, including segmentation, object detection, depth estimation, and classification. We then use a large language model to paraphrase prompt templates that convey the specific tasks to be conducted on each image, and through this process, we create a multi-modal and multi-task training dataset comprising input and output images along with annotated instructions. Following the InstructPix2Pix architecture, we apply instruction-tuning to a text-to-image diffusion model using our constructed dataset, steering its functionality from a generative model to an instruction-guided multi-task~vision~learner.~Experiments demonstrate that our model, dubbed {\it InstructCV}, performs competitively compared to other generalist and task-specific vision models. Moreover, it exhibits compelling generalization capabilities to unseen data, categories, and user instructions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a vision generalist, InstructCV, which casts various computer vision tasks as text-guided image generation. Based on a text-guided image editing model, InstructCV learns to generate visually encoded outputs of different vision tasks. Experimental results on several visual recognition tasks showcase the effectiveness of InstructCV.

### Strengths
1. Different from previous attempts to build vision generalists, this paper provides a solution built upon text-to-image diffusion models. Task prompting is achieved by text instructions, which are human-intuitive and general.

2. The experimental results indicate the validity of InstructCV in handling a variety of visual recognition tasks.

### Weaknesses
1. After reading the paper, I am a bit confused about the visually encoded outputs for different tasks.
a) Semantic segmentation: How to derive the mask of all semantic classes for an input image? If predicting them one by one and each class is manually indicated, I would say it is more like a task of referring segmentation rather than semantic segmentation. It would be helpful if the authors could provide more elaboration on this.
b) Object detection: What do the authors mean by saying “cross-reference the bounding boxes with the dataset annotations” in Appendix A.3?

2. What type of instructions is used during inference? Fixed templates or random rephrased ones? Does it remain the same for InstructCV-FP and InstructCV-RP during inference? As reported in Table 3, InstructCV-FP outperforms InstructCV-RP if both use template prompts during inference, so why bother training InstructCV using rephrased prompts? I understand this could improve the robustness of variations in wording, but one can just adopt a fixed template prompt to address a standard computer vision task. In addition, the rephrased prompts for each task are not that diverse (only 7 variations according to Table 4), why do we need to leverage LLMs as this could be readily done by humans? I would like to see more discussions about the benefits brought by utilizing rephrased prompts.

3. More ablations should be conducted to compare InstructCV-FP with InstructCV-RP. For example, the authors could report the results of InstructCV-FP in Table 1.

4. For the organization of this paper, I suggest the authors move the introduction of diffusion models in Section 2.2 (which takes up most of this section) to a “Prerequisites” subsection or Appendix.

5. The proposed method claims to be a vision generalist but it is validated only in some visual recognition tasks. What about other vision tasks such as low-level tasks (e.g., denoise, deblur, and derain) and generation (as done in Prompt Diffusion [1*])?

6. Further comparisons with other SOTA unified models such as Painter [2*] should be conducted. Painter is currently performing the best in prediction tasks as a vision generalist.

7. In terms of the computational cost, the authors claim that InstructCV exhibits much faster inference speed than previous methods such as Unified-IO. However, InstructCV needs multiple inferences for some tasks (e.g., semantic segmentation and classification), which could consume N×times where N is the number of semantic classes. Besides, the reported inference time of InstructCV on a single NVIDIA A100 GPU for an image is 5 seconds in the main paper but 10 seconds in the Appendix.

8. In the second paragraph of Section 1, the authors claim that “However, these prompts consist of (uninterpretable) numerical values derived from specific training datasets, which may limit their ability to generalize to new datasets, tasks, or categories”. Why do the prompts used in inpainting-based methods (which are visual examples) contain uninterpretable numerical values?

9. The format of references is messy and inconsistent. For example, a bunch of references do not list the conference/journal title.

10. Just a reminder that there is a very similar work, InstructDiffusion [3*], to this submission. The authors could consider citing that paper and provide comparisons and discussions.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces InstructCV, a unified language interface for computer vision tasks that enables task execution through natural language instructions. It leverages text-to-image generation by casting various computer vision tasks as instruction-based image synthesis problems. By creating a multi-modal and multi-task training dataset and applying instruction-tuning to a text-to-image diffusion model, InstructCV achieves competitive performance and compelling generalization capabilities compared to other vision models.

### Strengths
1. A valuable contribution of the paper is the introduction of a novel approach to integrate dense prediction tasks with a T2I model. Specifically, the paper suggests utilizing a generative model to perform a task similar to editing, which seems reasonable for tasks like segmentation, and depth prediction compared to sequence to sequence model.
2. With the help of T2I models, the algorithm has demonstrated good generalization ability in dealing with unseen categories.

### Weaknesses
1. The unique advantage of instruction tuning lies in its ability to generalize to unseen tasks[1], thereby enabling the model to become a general-purpose model. In the article, I believe it resembles more of a multi-task learning approach since the instructions are mapped to several tasks mentioned in the article. In my opinion, this approach does not have clear advantages compared to simply performing these tasks in a multitask learning setting on T2I model.
2. For certain tasks that do not require dense output, such as classification and detection, it may not be necessary to forcefully address them as image generation tasks. Sequence models are generally more suitable for modeling such tasks, and the approach described in the article seems highly inappropriate in such cases.

### Questions
1. The advantage of instruction tuning lies in its ability to enable the model to generalize to unseen tasks, which sets it apart from simple multi-task learning. However, in the paper titled "InstructCV," it seems that the approach primarily identifies instructions as task indicators within a predefined set of tasks. This may not demonstrate an advantage over traditional multitask learning. Could the author provide further explanation regarding the unique advantages of this approach?
2. I believe the good generation ability to new datasets is mostly because the comparison baselines lack the ability to handle open vocabulary. On the other hand, T2I  models are trained on a large amount of text-to-image pairs, which naturally gives them a good open vocabulary capability. Additionally, some unified models like x-decoder also demonstrate excellent generalization ability to new categories.

In summary, one aspect that concerns me is the lack of clear advantages in unifying dense prediction as an image-to-image generation task. The article mentions instruction tuning, but the experimental results do not generalize to new tasks. The open vocabulary capability is primarily attributed to the T2I models, and I don't believe this alone can be considered unique because The open vocabulary capability has also demonstrated impressive performance in previous works, such as xdecoder[1].

[1] X-Decoder: Generalized Decoding for Pixel, Image and Language

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors focus on the problem of a generalist visual model. To this end, they train a text-to-diffusion model on multiple tasks: Object Detection, Image Classification, Semantic Segmentation, and Depth Estimation. They use standard template phrases for each of these tasks and leverage a LLM to generate paraphrased variations of these questions and commands. They compare their visual model against other generalist models as well as task-specific models on each task. They show a level of performance which is competitive on most tasks.

### Strengths
1. The paper is very well organized and presented. Figures are very polished and simple to understand.

2. Given the strong performance of task-specific models and LLMs in recent years, the problem in question-generalist visual models-is a timely and relevant topic. 

3. Quantitative performance (except for Image Classification) is impressive.

### Weaknesses
1. Performance on image classification is weak versus baselines. It is unclear if diffusion models are well suited to object classification versus the other tasks which are spatially grounded. 

2. While generalist visual models are the frontier in Computer Vision, there should be more justification why such a system should rely on a single backend visual model versus a ensemble of experts (i.e. prompts to use Mask-RCNN for segmentation, ResNet for classification, etc.)

### Questions
1. Please add more justification in the paper specifically for the use of a single diffusion model versus an ensemble of experts.

2. Minor suggestion: Moving Section 3, Related Work, to come right after the introduction might help the paper flow better.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper slightly modifies the pipeline of InstructPix2Pix to use the diffusion model to achieve several compute vision tasks including segmentation, object detection, etc. The experimental results show that the proposed framework can be used to multiple tasks, but the performance is not very impressive.

### Strengths
1. This paper first uses instruct-tuning to adapt a pre-trained text-to-image diffusion model to several computer vision tasks.
2. This paper is well-written and easy to follow.

### Weaknesses
1. The novelty is limited. Formulating computer vision tasks as generative tasks is not novel and has been used in previous works. The overall pipeline highly resembles InstructPix2Pix
2. The performance is not impressive at all. The results lag far from the SOTA methods in Table 1. Note that SOTA methods of depth estimation are not listed for comparisons and other bold results (VOC) are computed on very old benchmarks. The authors might argue that their method is not task-specific, but I think this is not the reason for such poor results.
3. The inference pipeline of image classification (Figure 4) seems really weird. I think it would be really hard to perform evaluation on 1000-class ImageNet.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
