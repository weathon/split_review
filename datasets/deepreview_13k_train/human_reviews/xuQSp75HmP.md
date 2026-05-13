# PixWizard: Versatile Image-to-Image Visual Assistant with Open-Language Instructions

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
This paper presents a versatile image-to-image visual assistant, \textbf{PixWizard}, designed for image generation, manipulation, and translation based on free-from language instructions. To this end, we tackle a variety of vision tasks into a unified image-text-to-image generation framework and curate an \textit{Omni Pixel-to-Pixel Instruction-Tuning Dataset}. By constructing detailed instruction templates in natural language, we comprehensively include a large set of diverse vision tasks such as text-to-image generation, image restoration, image grounding, dense image prediction, image editing, controllable generation, inpainting/outpainting, and more. Furthermore, we adopt Diffusion Transformers (DiT) as our foundation model and extend its capabilities with a flexible any resolution mechanism, enabling the model to dynamically process images based on the aspect ratio of the input, closely aligning with human perceptual processes. The model also incorporates structure-aware and semantic-aware guidance to facilitate effective fusion of information from the input image. Our experiments demonstrate that PixWizard not only shows impressive generative and understanding  abilities for images with diverse resolutions but also exhibits promising generalization capabilities with unseen tasks and human instructions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces PixWizard, a visual assistant that performs diverse image generation, manipulation, and translation tasks based on free-form language instructions. PixWizard unifies various vision tasks into a single image-text-to-image framework using a newly created Omni Pixel-to-Pixel Instruction-Tuning Dataset. Built on the DiT architecture, PixWizard supports dynamic resolutions, integrates structure- and semantic-aware guidance, and demonstrates competitive performance and generalization across unseen tasks and instructions, making it a powerful interactive tool for visual tasks.

### Strengths
- The paper effectively explores the unification of multiple tasks within a single framework.
- The proposed model demonstrates strong performance across a wide range of tasks.
- The method is adaptable to images of varying resolutions.

### Weaknesses
The reviewer does not have significant concerns but notes a few minor weaknesses:
- Some implementation details are unclear; For example, in the statement, “In the first stage, we initialize the model by combining the weights of a pretrained text-to-image model with randomly initialized weights for the newly added modules,” it is unclear which model is used for initialization. Furthermore, the specific method of combining these weights is not detailed, which could impact reproducibility. It is also unclear how the 'newly added modules' are structured and what their specific roles are within the overall architecture.
- The paper reads more like an engineering report than a research paper with deep insights. However, it would be valuable if the model, code, and/or dataset were made publicly available. The lack of a deeper analysis of the underlying mechanisms limits the scientific contribution. The paper would benefit from a more thorough discussion of the theoretical underpinnings of the proposed approach, rather than just focusing on empirical results.
- A concluding analysis on how different tasks influence each other within the unified framework would be beneficial. It is unclear if the multi-task learning approach leads to positive transfer or negative interference between tasks. A deeper investigation into task-specific performance changes and potential trade-offs would be valuable.

### Questions
NA

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
4

### Summary
PixWizard presents a unified approach to  conduct various kind of image generation, manipulation, and translation tasks with one DiT model.  The contributions are:

1. The authors constructed an image-instruction-image triplet instruct tuning dataset to train this model.  

2. The authors proposed Structural-Aware Guidance to fix the structure of reference image and Semantic-Aware Guidance to learn the instruction-based image to image capability.  Inspired by DynamicVit, the authors designed a task-aware dynamic sampler to squeeze the image tokens for different image to image tasks and utilized Multi-Hot Gumbel-Softmax to extract topK tokens in order to decrease computational cost in DiT.

3. PixWizard inherits the dynamic ability of lumina-next model to handle images of any resolution and aspect ratio. In addition, a two-stage training strategy is designed to improve the performance of the model.

4. Extensive experiments on various dataset and benchmarks concretely verified the generalization of PixWizard

### Strengths
1.  The task studied by this paper is the main-stream trend nowadays: unifying multiple image generation tasks in one DiT model.

2.  Solid quantitative experiments demonstrate the generalization capability of the proposed method.

3.  The authors designed a DiT version of DynamicViT. The Multi-Hot Gumbel-Softmax is also interesting. The proposed task-aware dynamic sampler, which sparsifies the image token to reduce computational cost and utilizes one of the two text encoders for task specific embedding, is a brilliant design. 

4. Many properties of pixwizard inherit from previous work lumina-next, including the DiT pretrained weigth, dynamic resolutions, which makes pixwizard a meaningful extension of the lumina-next-t2i DiT model in terms of omni image generation.

### Weaknesses
1. One of my main concerns is that pixwizard seems to be incapable of conducting non-rigid editing, which is a very common and important, yet challenging topic in image editing, for example, let the standing dog sit, let the polar bear raise its hand, close the open book, etc.  In figure 1, I cannot find  such a common task being presented. I doubt from two perspectives whether pixwizard is capable of conducting such non-rigid editings:  

first, the authors designed the structural aware guidance, which concats the vae latent with random noise in  channel dimension. This is identical with instructpix2pix, which claims that "our model is not capable of performing viewpoint changes, can make undesired excessive changes to the image, can sometimes fail to isolate the specified object, and has difficulty reorganizing or swapping objects with each other.".  From my experiments, instructpix2pix completely fails in non-rigid editing. Thus I doubt whether pixwizard inherits such a incapability of instructpix2pix  due to the same concat operation.

second, the datasets utilized for training image editing task are strongly biased and do not contain non-rigid editing data. In section 2, the authors listed the training datasets: UltraEdit (2024), MagicBrush (2024a), GQA-Inpaint (2023), Instruct P2P (2023), SEED-X-Edit (2024), GIER (2020), and HQ-Edit (2024). However, almost none of these datasets contain non-rigid editing data. Instead, these datasets focus on very simple editing tasks, which could simply be solved by inpainting models for adding, deleting and replacing objects or backgrounds,  or controlnet+text to image to change textures and style transfers (of course, pixwizard integrates all these capabilities in one model and demonstrates comparable or better quantitative results than separate models, which is still a contribution. I just want to convey my personal opinion that these tasks are generally considered simple image editing tasks).   These tasks are rather simple in general without changing spatial and structural features. Without training data on non-rigid editing, it is almost impossible for pixwizard to conduct such edits. 

2.  my second concern is that although the quantitative experiments are solid, the quantitative results in table 1 show that for many image to image tasks, there is still a significant gap between  pixwizard and task-specific model. In table 2 the image editing results are close, yet the testsets are very biased towards simple editing tasks. In table 3 the results on controlnet and t2i tasks are close though.


3. shown in table 6,  the gain of task aware dynamic sampler and two stage training strategy  is minimal, which weakens the effectiveness of the propose method.

### Questions
1. The current state-of-the-art general image editing methods, Imagic, followed by its speedup and less overfitting open-sourced version Forgedit, is capable of conducting general image editing tasks including the non-rigid editing. Is pixwizard capable of conducting non-rigid editing like Imagic and current state-of-the-art  Forgedit? If yes, I would like to see some examples compared with Imagic and  Forgedit with examples from TEdBench in the revised version. If not, I would like to see some discussions on this issue and how to solve it in the revised version.  Imagic and Forgedit require test-time fine-tuning, which costs at least 30 seconds. Is it possible for pixwizard to somehow distill and integrate these methods to tackle the non-rigid editing problem? Considering the time limit of rebuttal period, I won't require the authors to fix this issue in such a short time. Yet  discussions and possible solutions to this problem in the revised paper are compulsory . 


2. shown in table 6, the task-aware dynamic sampler do not bring significant performance gain. What are the computational savings then? They are not reported in the paper.

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
The paper proposes a generalist vision model that unifies various image generation and recognition tasks into an image-instruction-to-image problem. To address this problem, they collected a dataset, Omni Pixel-to-Pixel Instruction-tuning Dataset, consisting of 30 million image-instruction-image triplets. Fueled by this dataset, they train a conditional DiT model that takes the conditional image and instruction as the input. The paper shows extensive comparisons against specialized and generalist baselines on various benchmarks.

### Strengths
1. Collecting and preprocessing the Omni Pixel-to-Pixel Instruction-tuning Dataset is a huge effort, which is the largest of its kind to my best knowledge and can be a great contribution to the community.

2. The paper is clearly written with rich details.

3. Extensive evaluation is done to demonstrate the performance of the model on various visual tasks, from image editing to image grounding.

4. Ablation studies are performed to verify the proposed methods, helping to understand the significance of each individual components.

### Weaknesses
1. While the authors claimed "competitive performance compared to task-specific models and surpass general visual models," this is not directly reflected by the results: there is a clear gap in tasks like depth estimation, semantic segmentation, and image grounding with task-specific models. The general visual model also outperforms some of these tasks. The authors should state the contribution in a more clear way.

2.  The other contribution claimed in the abstract that was not well-demonstrated in the paper is that "the model exhibits promising generalization capabilities with unseen tasks." How much can the model generalize beyond instruction that it does not see during the training? For example, can the model follow the instruction "Mark the specified area with a star in red: {caption}"?

3. The baselines chosen for image generation were not state-of-the-art anymore, e.g., UniControl is not compared, although their dataset (MultiGen-20M) was used.

(Minor) Although some ablation studies are provided to justify the proposed methods, some other choices that seem novel are not well-proved, such as using Gemma-2 instead of T5 as the text encoder and RoPE as the positional embedding.

### Questions
1. "To balance tasks, we assign manual sampling weights to each dataset, randomly selecting data when a weight is less than 1.0." - could the author elaborate on how this is done? Like, what does it mean by the weight is less than 1, when the weights are manually assigned?

2. As one of the major contributions of the paper is the public data, will the processed dataset be released in any form? 

3. Which layers of the CLIP image features are used as the conditions, is that the 1D feature after pooling or 2D feature before pooling?

### Soundness
3

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
The authors propose PixWizard, a flow-based model that can tackle a range of visual tasks including text-to-image generation, inpainting and outpainting, as well as a long list of image-to-image translation tasks (sketch-to-image, depth-to-image, denoising, box-drawing based detection, segmentation and more).

The core of their approach revolves around teaching a pre-trained text-to-image model (Lumina-Next) to tackle multiple novel tasks by conditioning it on additional image input features and features describing the specific tasks the network should handle. The authors propose a set of blocks to extract said features and integrate them into the network, and propose a data curation and balancing strategy to ensure the model does not ignore rare tasks.

Finally, the authors conduct a wide range of experiments on many different tasks and demonstrate that their approach is competitive (and sometimes even improves over) networks trained for each individual task, and also outperforms most generalist network approaches which aim to concurrently tackle many tasks.

### Strengths
The paper does a remarkable job in evaluating against a long range of baselines and across a wide list of tasks. It also demonstrates good performance across most of the tasks, showing that their approach can indeed lead to a fairly general multi-task model.

The authors also provide a fairly detailed overview of their network, block choices, and the sources and handling of their training data. In the appendix, they further analyze many of their contributions in an ablation study, and report on choices even when they do not meaningfully impact the results (which is good in my eyes, as it lets future work know which components they may want to discard in favor of simplicity).

Finally, the appendix also contains an interesting application for the all-in-one approach, where they use the model to segment parts of the image and then edit them. Such interactive multi-step approaches that use different network skills to improve results can serve as a good reason for exploring multi-task models. Please see more on this in the weakness section below.

### Weaknesses
My chief concerns with the paper are as follows, ranked from most-important to least important:

1) The paper does not appear to distinguish itself from prior, published multi-task approaches like Emu Edit [Sheynin et al, CVPR 2024], and it does not actually outperform them. More specifically, Emu Edit already introduced a multi-task approach based on a pre-trained text-to-image model. It already has learned task embeddings, and it shows a range of similar downstream tasks. 
I appreciate that outperforming closed models trained on unknown datasets is difficult, but when I ask myself what I learned from reading this paper that I did not already know from Emu Edit, I have a hard time coming up with an answer, and this is an issue.

2) The paper claims to generalize to unseen tasks (e.g. L26). I may have missed the results that corroborate this claim, but the closest I could find are the zero-shot restoration experiments in the appendix. However, these are close enough to existing restoration tasks that even non-multi-task baselines can generalize well to them and outperform this model? I would have liked to see generalization to actual new tasks, even using inverted task embeddings like Emu Edit. Otherwise, this weakens the contribution.

3) Related to (1) – most of the paper focuses on comparisons to other methods, to the point where ablation is relegated to the end of the appendix. I think ablation is crucial here and should be moved into the core paper, even at the cost of pushing out some experiments. since it is the only section that gives us validation for the specific new ideas introduced by the paper. This method uses a different base-model, is trained on different data, and has a significantly different number of parameters from the baselines. I understand that you beat them, but I also want to understand why. 

4) There is relatively weak motivation for why multi-task models are needed. Saving some memory compared to specialized approaches is okay, but its not a significant contribution. Again, this can be contrasted with Emu Edit which show that training on multiple tasks can improve each of them individually, and that training on discriminative tasks like segmentation can also improve performance on generative tasks like editing. I had a hard time finding similar motivations here.

5) The paper can be better self-contained. Some components (e.g., dynamic partitioning and padding scheme) refer back to recent preprints with no citations, and if these parts are important then they should probably be given a bit more detail (even in the preliminaries in the appendix).


Minor issues that did not affect my score:

1) L121: without extra any -> without any extra

2) “Next, we concatenate the image latent with the noise latent along the channel dimension” – Consider citing SR3 [Saharia et al, TPAMI 2022] or Palette [Saharia et al, SIGGRAPH 2022].

3) Table 3 – Bold numbers are missing from the baselines when they win.

4) L483 notes that the method outperforms the inpainting baselines based on FID and LPIPS scores, but the method seems to underperform the baselines on LPIPS?

5) Appendix C.4. – It seems like the gains highlighted here are not related to any change in the proposed paper, but are just due to selecting a flow-matching baseline over a diffusion model? Did I miss something?

6) L1544: less tokens requiring less inference time should be shown experimentally because it’s not trivial that the gain here is meaningful.  The method uses extra layers to actually select what tokens to drop, and the tokens enter through cross-attention (as opposed to self-attention) which means they scale compute linearly and not quadratically?

### Questions
I tried to outline my concerns in the weakness section above. To sum them up in two main questions:

1) What does this paper bring to the table that doesn’t already exist in prior published work like Emu Edit?

2) What is the extent of generalization that your model actually supports? Can you back this up with experiments?

I appreciate the effort the authors clearly put into the work, so if these are answered in a satisfactory manner, I’ll gladly increase my score.

Minor clarification questions (skip these if you don’t have time):

3) What are the details of the MHGS? How is it implemented?

4) L100 says “We extend the dynamic partitioning and padding scheme to handle input images of any resolution, aligning closely with human perception.” but L279 says these resolution capabilities are inherited from [Zhuo et al., 2024]. Do you mean that Zhou support multiple resolutions but not good enough, and you improve this? Are you extending the scale of resolutions that they support? 

5) L298: “we assign manual sampling weights to each dataset” How? Can you describe your criteria?

### Soundness
3

### Presentation
3

### Contribution
2
