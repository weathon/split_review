# PartEdit: Fine-Grained Image Editing using Pre-Trained Diffusion Models

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
We present the first text-based image editing approach for object parts based on pre-trained diffusion models.
Diffusion-based image editing approaches capitalized on the deep understanding of diffusion models of image semantics to perform a variety of edits.
However, existing diffusion models lack sufficient understanding of many object parts, hindering fine-grained edits requested by users.
To address this, we propose to expand the knowledge of pre-trained diffusion models to allow them to understand various object parts, enabling them to perform fine-grained edits.
We achieve this by learning special textual tokens that correspond to different object parts through an efficient token optimization process.
These tokens are optimized to produce reliable localization masks at each inference step to localize the editing region.
Leveraging these masks, we design feature-blending and adaptive thresholding strategies to execute the edits seamlessly.
To evaluate our approach, we establish a benchmark and an evaluation protocol for part editing.
Experiments show that our approach outperforms existing editing methods on all metrics and is preferred by users 77-90% of the time in conducted user studies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an inference-based image editing method that can perform fine-grained object parts editing. Specifically, this paper trains part-specific tokens that specialize in localizing the editing region at each denoising step, then develop feature blending and adaptive thresholding strategies that ensure editing while preserving the unedited areas.

### Strengths
(1) This paper focus on an interesting question, which as great significance to downstreaming research and tasks.

(2) The overall design of the model design is generally make sense.

(3) This paper is easy to follow.

### Weaknesses
(1) Some related works are missing. Discussing and compare these related works will be good for improving the paper's quality.

- [1] Pnp inversion: Boosting diffusion-based editing with 3 lines of code

- [2] Inversion-free image editing with natural language

- [3] Dragondiffusion: Enabling drag-style manipulation on diffusion models

(2) Can you provide more experimental results to prove the effectiveness of the proposed method? For example, more comparison results with training-based editing methods such as InstructPix2Pix[4]. More visualization for editing regions of various image-editing prompt pairs. Results of combining the proposed method to different pretrain checkpoints/different diffusion model backbones to show its generalization ability.

- [4] Instructpix2pix: Learning to follow image editing instructions

### Questions
See weakness.

### Soundness
3

### Presentation
2

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
The paper introduces a method to enhance pre-trained diffusion models for fine-grained image editing by training part-specific tokens for localizing edits at each denoising step. This approach uses feature blending and adaptive thresholding for seamless edits while preserving unaltered areas. A token optimization process expands the model’s semantic understanding without retraining, using existing or user-provided datasets. Qualitative as well as quantitative experimental comparison have been conducted to demonstrate the effect of the proposed method.

### Strengths
1. This paper addresses a critical problem in image editing: the inability to accurately edit specific parts of an object while keeping the rest of the image unchanged.

2. The use of token optimization to learn adaptable tokens for subsequent editing tasks is intuitive and intriguing.

3. The experiments are thorough, with comprehensive ablation studies that validate the effectiveness of the proposed approach.

4. The paper is well-written, easy to follow, and logically structured.

### Weaknesses
1. The images used for training part tokens are very limited, with only 10–20 images. In such cases, the representativeness of the images is crucial for generalization. It would strengthen the paper if the authors would conduct experiments to show the impact of varying the types of training images on the model's performance.

2. The method involves many hyperparameters that require tuning, including the number of diffusion timesteps for training part tokens and inference, the selection of layers for optimization, and the adjustable tolerance for transitions between edited parts and the original object. This adds complexity to the overall framework and could make it challenging to implement effectively.

3. In practical scenarios, one might want to adjust two parts simultaneously. Therefore, how will the method apply when handling instruction text that requires simultaneous editing of two parts? I suggest the authors include experiments or examples to show the model's performance on multi-part edits.

4. Will the evaluation dataset for PartEdit be made publicly available? Also, will the code be available?

5. Typo: The text inside Figure 1, "prompt-to-prompt (ICRL2023)," should be corrected to "ICLR."

### Questions
1. Given the limited number (10–20) of images used for training part tokens, how were these images selected to ensure representativeness, and what impact does this selection have on the model's generalization capabilities?

2. Are there guidelines or best practices provided for hyperparameter tuning?

3. How effectively does the method handle instructions that require simultaneous modifications to two or more parts of an image?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a text-based image editing method for object parts using pre-trained diffusion models. It enhances model understanding of object parts for fine-grained edits through optimized textual tokens and masks.

### Strengths
1. The paper presents a flexible method for text-based image editing focused on object parts, which is a novel contribution to the field of image processing and editing.
2. The paper is well-written and easy to follow.
3. The authors have conducted extensive experiments and provide a solid basis for its practical application.

### Weaknesses
1. The approach relies on a finite and manually defined set of part tokens, which could restrict the flexibility and applicability of the method in real-world scenarios where users might need to edit object parts that are not covered by the predefined tokens. This limitation could affect the generalizability of the technique to a broader range of editing tasks and objects.
2. There are many methods nowadays that utilize semantic segmentation to create masks, which are quite similar to this paper. You should supplement your study with some relevant ablation experiments, like replace the attention mask with semantic segmentation part  and compare it with similar methods [1][2][3].

[1] SmartMask: Context Aware High-Fidelity Mask Generation for Fine-grained Object Insertion and Layout Control.
[2] Accelerating Text-to-Image Editing via Cache-Enabled Sparse Diffusion Inference.
[3] Towards Understanding Cross and Self-Attention in Stable Diffusion for Text-Guided Image Editing.

### Questions
1. The paper does not explicitly mention how it deals with fine-grained edits for multiple objects within an image, such as distinguishing between two heads in an image for editing purposes. could you provide some form of a mechanism to differentiate between objects? How your method deal with this situation?
2. How many part tokens can you serve?
3. What's your random methods for initializing textual embeddings?
4. How do you generate reliable localization masks? Does this process rely on specific datasets or pre-trained models? Will the distribution of the training data for the mask overlap with the distribution of the images used for testing?
5. see weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method for part editing in images. The paper shows that current state-of-the-art fails when asked to change only particular parts of images (e.g. 'hood' of a car). The paper proposes to perform part token learning, and then uses the attention maps of the learned part tokens for accurate part-based editing of images. Results show improved results over several baseline methods.

### Strengths
- the objective of accurate part editing with text prompts is relevant for many users. 
- the method is simple and results show that the method successfully addresses the problem. 
- overall writing and presentation is good.

### Weaknesses
- I find the main scientific/technologic contribution of the paper insufficient for ICLR conference, nor does the paper provided new insights in the functioning of DM for editing. I agree part-based editing is relevant. Given existing methods, part-based editing can be addressed by solving part detection or just user provided masks (for example based on segment anything). The proposed method of learning part tokens makes sense. The computed attention maps reduce the problem to a text-based inpainting problem. 
- the method is only applied to a very limited set of parts (7). Are these stored in 7 different models or jointly held within a single network ? Could this scale to many more parts ? Some analysis of the quality as a function of number of parts (if contained in a single model) would be interesting.
- the method needs to learn new prompts for every new part users might want to change. The method dependents on existing part datasets for these parts, else they need to be created. Do the authors see any other solutions, using other existing models to preven t annotation? 

minor
- are all weights tuned, or do you use LoRA for layer optimization of the L layers
- figure 3 could be improved, it is hard to read in print

### Questions
See weaknesses. 

I think is not of ICLR quality (the scientific contribution is too small) and could be published in a more applied venue (e.g. WACV) or dedicated workshop.

### Soundness
3

### Presentation
3

### Contribution
2
