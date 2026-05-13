# UniVis: A Universal Framework for Computer Vision Tasks

- Decision: Reject
- Scores: 3, 8, 5, 5

## Abstract
We propose $\texttt{UniVis}$, a universal learning framework to tam a wide range of computer vision tasks, including visual understanding (e.g., semantic segmentation), low-level image processing (e.g., denoising), and conditional image generation (e.g., edge-to-image synthesis). Built on a large-scale pre-trained text-to-image diffusion model, $\texttt{UniVis}$ unifies various vision tasks through a general framework using instruction tuning, where its unifying ability comes from the generative and reasoning power of the pre-trained model. Specifically, $\texttt{UniVis}$ defines a general image completion task wherein the input consists of a pair of input-output images corresponding to the target task and a query image, and the aim is to generate the ''missing'' data paired to the query. The paired images play the role of image instruction defining the task, e.g., semantic segmentation is represented by an RGB image and its segmentation mask. Our rationale is that each computer vision task can be characterized by its unique input-output pair, which informs our $\texttt{UniVis}$ model about the expected output for the given query. Furthermore, a task-level or instance-level prompt can be optionally added to provide text instruction. By unifying various visual tasks, $\texttt{UniVis}$ has the advantage of minimizing the inductive bias inherent in designing models for individual tasks, and it also suggests that the understanding of different visual tasks can be achieved through a shared generative model. In experiments, $\texttt{UniVis}$ showcases impressive performance on a bunch of standard computer vision benchmarks including ten tasks in total. The source code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes UniVis, a framework that can deal with several visual tasks, including visual understanding (e.g., semantic segmentation), low-level image processing (e.g., denoising), and conditional image generation. The idea is to perform instruction tuning on a large-scale pre-trained text-to-image diffusion model. During training, the model is trained to fill in the missing query output based on the provided instructions, which consists of task-specific input-output pairs.

### Strengths
This paper proposes a unified framework for multiple common visual tasks across different categories, including image understanding, image processing, and image generation. The idea of using instruction tuning on Stable Diffusion is novel and interesting, and the experimental results are reasonable. The presentation of the paper is also clear.

### Weaknesses
1. The proposed method is limited to dense image tasks, where the output is at a high-dimensional image level. It does not demonstrate feasibility on a wide range of computer vision tasks where the output is low-dimensional, such as image classification, image captioning, VQA, etc.
2. Even for dense image tasks, it misses multiple tasks. For example, for the task of conditional image generation, the paper misses two important tasks: class-conditional generation and text-conditional generation. Thus, I feel the claim that Univis is a "Universal Framework for Computer Vision Tasks" is exaggerated, making the contribution of the paper limited.
3. Overall, the experiment results shown in the paper are weak. In two of the three categories, it is far behind the Painter baseline. It might be because of computation limitations, but it also might be because the proposed method does not scale with more computation resources. Therefore, it would be good to show at least one experiment that is trained with the same computation budget as the Painter baseline, otherwise, the results are not convincing enough to demonstrate any improvement over previous methods.
4. The method does not show scaling ability with more tasks and data. As shown in Table 4, a model trained with multiple tasks is worse than a model trained on a single task. This raises concerns that this method may not scale up well with multi-task training, which is not desirable in a universal framework.

### Questions
Please see weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present and evaluate "UniVis," which is an approach to training and obtaining inferences from a Stable Diffusion model across a variety of tasks from three distinct categories of tasks. The model is trained using an instruction image pair that demonstrates the task to be perform (e.g., for the depth estimation task, the "instruction" or "example" pair would be an RGB query image of a scene and a corresponding depth image as example output). At training time, the model is also presented an input query image of the kind expected for the task (e.g. a RGB scene) and trained to produce the ground-truth output for that particular example. This can be supplemented with a textual prompt to further condition the denoising U-Net within the Stable Diffusion model (e.g. the text instruction for the depth estimation task would be "depth map").

This is essentially an instruction-tuning framework for Stable Diffusion, where the instruction is an image pair that demonstrates the task, optionally supplemented with a text description of the task.

Most of the evaluations are conducted by retraining UniVis for a specific task (e.g. depth estimation, or denoising, or pose-to-image image generation). Because of this, this paper is largely a demonstration of the generalizability of the training _process_, rather than the generalizability of a single trained model across the multiple kinds of tasks.

However, one experiment is conducted to show that a single trained model can also generalize across tasks from the three task categories (from image understanding: depth estimation; from low-level image processing: denoising; and from conditional image generation: mask-to-image). One experiment also demonstrates that a single trained model can generalize across tasks from within one category: a model was trained to be able to perform inference for four conditional image generation tasks (mask-to-image, depth-to-image, pose-to-image, and edge-to-image).

The results appear to show performance from the single-task UniVis on par with the "Painter" model of Wang et al. (https://arxiv.org/abs/2212.02499), when Painter's training is constrained to use the same amount of computing power as UniVis's authors used for UniVis.

Results did not appear to significantly deteriorate when UniVis was trained as a multi-task (but still single-category) model for the four conditional image generation tasks (see Table 3). Nor did results appear to significantly deteriorate when UniVis was trained on multiple tasks that spanned the three categories of tasks (see Table 4).

### Strengths
The ability to produce a single trained model that can generalize across diverse computer vision tasks by simple altering the "instructions" would be very useful. While instruction tuning is not original, the specific construction of the "instructions" for UniVis _is_ original. It has much in common with the instruction pairs from "Painter" (https://arxiv.org/abs/2212.02499), but instead of masking random subregions of the target images, the authors here train UniVis by masking the entire target image and train UniVis to generate the complete output. It did not seem to me that this would be significant, so I was quite surprised that it appears this change in masking strategy is crucial to unlocking the unifying capability of a pre-trained Stable Diffusion model (see Table 5).

### Weaknesses
I note that these concerns have largely been addressed in response and revision, but I leave these comments here for context. I have updated my scoring, however.

My biggest concern is that the results in the tables cannot be understood without knowing the variation that might be produced from one repetition of an experiment to the next. It is crucial that you state whether you only ran each experiment once, or whether the numbers you are reporting are the averages across several trials. If the latter, it is also essential to provide some measure of variation (standard deviation, confidence interval). If you have no estimation of the experiment-to-experiment variation, how do you know that what you are observing as differences in the tables is not simply noise?

In two places, you make assertions / claims that could use further elaboration or specificity. They are also maybe unnecessary in light of what you are actually showing in this paper.

1. At the bottom of p. 1, you say that LLMs exhibit "superior linguistic understanding due to the highly organized and structured nature of language." But images also have significant structure. You go on to say that the "disparity between low-level features and high-level semantics... is typically more pronounced in vision than in text." This is all very vague. Do you need to say it? If you do, could you be more precise about how you are assessing "disparity" or the degree of organization or structure? For example, are you referring to the relative entropy of the feature distributions at different layers of a deep network trained on images versus text? Or perhaps the number of bits required to encode the same amount of information in each modality at different levels of abstraction?
2. At p. 6, you say that "patch-level inpainting that resembles word completion training schemes in NLP is not adequate for a holistic and profound understanding of vision tasks because images _have much lower semantic density than texts_." This is vague. I think I know what you mean: that there is a lot of redundancy and spatial correlation in images that is not present in text. Could you make this more precise? For instance, could you quantify semantic density as the number of independent concepts per unit of spatial or temporal dimension? Or perhaps use an information-theoretic measure like mutual information between pixels versus words to demonstrate this difference?

Some of the concepts are under-explained, or used without any explanation:

1. DDIM is mentioned at p. 16 (B.2) without any explanation. A brief explanation of its role in accelerating the reverse diffusion process would be helpful, especially for readers not intimately familiar with diffusion models.
2. I know U-Net is a well-understood term-of-art by now, but I think it could still use a brief explanation of its purpose, given that it is what is being trained to fit the distribution of latent codes. It would be helpful to briefly explain how the U-Net architecture, with its skip connections, facilitates the learning of hierarchical representations necessary for modeling complex image distributions.
3. You use the phrase "spatial-wise concatenation" at p. 4 (first paragraph of 3.1). Can you describe this? I think you simply mean you can stitch the images together in a grid as you visualize in Figure 2, right? A more precise definition, perhaps referencing the specific dimensions along which the concatenation occurs, would be beneficial.

Some of the phrasing is unclear or awkward. I can provide some suggestions for improvement.

1. At p. 3, you talk about "three _implementations_" of UniVis. But I would hesitate to call these different _implementations_. I think the contribution of your paper is that these are all the _same_ implementation, but simply trained in three different regimes (single-task, single-category, and multi-category). I prefer the phrase you use later: "three types of model training."
2. In the first sentence of the abstract: the word "tam" seems to be a typo.
3. In the introduction, "all-rounder" is unclear. It might be more appropriate to use a term like "general-purpose" or "multi-task" to better convey the intended meaning.
4. In the introduction, the sentence "The Challenges are in three aspects, elaborated in the following" is an awkward sentence. I suggest simply: "There are three main challenges."

### Questions
1. Why do you ignore the apparently better-performing comparator models in several of the tables when reporting the "best" and "second best"? For instance, in Table 1, why does OneFormer not get bolded as the "best"? If you are ignoring specialized models in your ranking of best and second best, you should include this caveat in your description of "best."

2. I see that you trained a single-category UniVis on the four conditional image generation tasks. Did you attempt training your multi-task/single-category UniVis on either of the two other categories? If not, why did you choose conditional image generation as the category to try as the single-category UniVis?

3. I see that for multi-category UniVis, you selected depth estimation, denoising, and mask-to-image. Did you attempt training other combinations of tasks across the categories (e.g. semantic segmetation + deraining + pose-to-image)? If not, why did you choose the three you chose?

4. Do you expect some combinations of tasks to be particularly difficult for UniVis to be trained for at the same time?

5. If you have no estimation of the run-to-run variation, how do you know that what you are observing as differences in the tables is not simply noise?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces UniVis, a universal learning framework designed for various computer vision tasks. Drawing inspiration from the success of large language models (LLMs) in natural language processing (NLP), UniVis seeks to offer a unified solution for visual tasks. Based on the text-to-image diffusion model, Stable Diffusion (SD), the framework leverages instruction tuning to adapt pre-trained knowledge to diverse downstream vision tasks. This approach employs an image completion framework, where input comprises a query image paired with another input-output image related to the target task. Through this, the model discerns the desired output for the query. The central tenets include:  1. Vision tasks can be represented as unique input-output pairs. 2. Vision tasks can benefit from optional text prompts. 3. The reasoning ability of SD can be harnessed for diverse vision tasks. 
The authors undertook comprehensive experiments across ten vision tasks and three distinct training methodologies, aiming to ignite further exploration into fostering a deeper comprehension of vision tasks via a unified generative modeling approach.

### Strengths
[Task] The undertaking of employing SD as an interface for diverse downstream tasks presented in this study is intriguing. It enables the pre-trained knowledge to be adaptable and applicable across various downstream vision tasks.

[Experimental Results] The authors carried out a thorough evaluation across many downstream tasks.

[Paper Writing] The manuscript is well written, effectively conveying the primary concepts.

### Weaknesses
 [Model Performance] While the authors claim reduced computational resource usage, the model's performance significantly lags behind the open-sourced baseline model, Painter [1], as evident in Table 2.

[Universality with Text Instructions] The framework's universality is diminished by its reliance on task-specific text instructions. A more compelling setup would operate without any task prompts. Text instructions should be supplemental, enriching tasks like text-to-image generation with finer details, rather than being a mandatory prerequisite for all tasks. The current design necessitates a task-specific text prompt, which limits the model's ability to truly generalize across diverse visual tasks without explicit textual guidance.

[Task Prompt Limitation] The inclusion of task prompts detracts from the intriguing properties of in-context instruction tuning. The essence of in-context learning lies in the model's emergent properties, deciphering the logic and connections within paired VISUAL inputs to undertake related tasks. Ideally, we'd want to furnish only in-context visual cues, enabling the model to manage a myriad of downstream tasks. Yet, the current design seems to veer away from this ideal. The reliance on task-specific text prompts prevents the model from fully leveraging the potential of in-context visual learning, where the model should ideally infer the task directly from the visual input-output pairs without explicit textual instructions.

[1] Wang, Xinlong, Wen Wang, Yue Cao, Chunhua Shen, and Tiejun Huang. "Images speak in images: A generalist painter for in-context visual learning." In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 6830-6839. 2023.

### Questions
Most of my questions are in the weakness section. In addition, I'm curious how the model performs without relying on task prompts. Have you conducted any ablation studies to shed light on this aspect?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a framework called UniVis, with the aim of handling various categories and granularities of computer vision tasks. The framework is built upon a pre-trained stable diffusion model, thus enabling the transformation of some computer vision tasks into image generation (completion) tasks. The authors tested the framework on multiple benchmarks, and the experimental results showcased competitive performance.

### Strengths
The authors unify some computer vision tasks in terms of training format, viewing them as image generation tasks based on stable diffusion model (SD). With SD, this approach achieves better or competitive results on some benchmarks.

### Weaknesses
1. Constrained by the pretraining model (i.e., SD), UniVis performs better in image generation (Table 3) while average in visual understanding and low-level image processing (Table 1&2). This indicates that the framework is coupled with the training format of the pretraining model. Furthermore, the authors claim that there is no need for high training costs, but this method requires more parameters. Specifically, while the authors frame the method as a unified approach, the performance disparities across tasks suggest that the method is not equally suited for all tasks, and its reliance on a generative model like SD limits its effectiveness in discriminative tasks. The parameter overhead also raises questions about the practical efficiency of the approach, especially when compared to task-specific models.

2. When using multiple datasets for joint training, there is no significant gain, even a slight decrease, for the three different categories of tasks (Table 4). This seems to suggest that this work is limited when using only one model to unify computer vision tasks (joint training doesn't yield gains). If it's just about unifying the training format, it doesn't seem to be very meaningful, as it doesn't outperform task-specific models on specific benchmarks. The lack of improvement with joint training suggests that the unified framework does not effectively leverage shared representations across different tasks. This raises concerns about the true unification of the tasks, as the model appears to be learning separate task-specific representations rather than a common, transferable representation.

3. Fig4 is significant as I personally believe one of the benefits of unifying computer vision tasks should be the ability to generalize to other unseen tasks (analogous to LLM), but unfortunately, only one figure is provided to demonstrate this. How to further enhance generalizability is an interesting point. The limited evidence of generalization, particularly with only one figure, makes it difficult to assess the true potential of the framework for out-of-distribution tasks. The analogy to LLMs is interesting, but the paper needs to provide more substantial evidence to support this claim.

4. The testing scheme in the paper is similar to one-shot, how can it be extended to few-shot (>1)?

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
