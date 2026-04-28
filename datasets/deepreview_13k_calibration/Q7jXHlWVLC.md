# Re-imagine the Negative Prompt Algorithm for 2D/3D Diffusion

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Although text-to-image diffusion models have made significant strides in generating images from text, they are sometimes more inclined to generate images like the data on which the model was trained rather than the provided text. This limitation has hindered their usage in both 2D and 3D applications. To address this problem, we explored the use of negative prompts but found that the current implementation fails to produce desired results, particularly when there is an overlap between the main and negative prompts. To overcome this issue, we propose Perp-Neg, a new algorithm that leverages the geometrical properties of the score space to address the shortcomings of the current negative prompts algorithm. Perp-Neg does not require any training or fine-tuning of the model. Moreover, we experimentally demonstrate that Perp-Neg provides greater flexibility in generating images by enabling users to edit out unwanted concepts from the initially generated images in 2D cases. Furthermore, to extend the application of Perp-Neg to 3D, we integrate Perp-Neg with the state-of-the-art text-to-3D (DreamFusion) method. Our experimental studies clearly show the effectiveness of Perp-Neg in addressing the Janus (multi-head) problem. Perp-Neg has enabled the generation of 3D assets that were previously unattainable due to the persistent Janus problem, even after multiple attempts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed a Perp-Neg method to control the text-to-image diffusion model by pependicular gradient sampling. This method leverage the geometry properties of the score space in diffusion models.  Authors present experiments of this method in 2d image translation and 3D generative models with SDS to mitigate the janus problem in text-to-3D task.

### Strengths
1. The proposed pependicular gradient sampling is performed on the latent noise space of diffusion models, is easy to follow. 
2. This method gives a tractable method to balance betweet the score of postive and negative text prompts. 
3. The method is easy to implement and follow.

### Weaknesses
1. The assumption of this method is based on the pependicular gradient sampling, but this design is somewhat heuristic, and have not been proved in the paper. 
2. Weakness 1 caused the effectiveness of this method on text-to-3D is limited actually. Janus problems almost cannot be mitigated according to implementation in threestudio. [1]
3. The balance factor defined between eq.8 and eq.9 may be hard to tune in experiments

### Questions
please refer to the weakness part.

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
The submission discusses the limitations of text-to-image diffusion models that the 2D results of diffusion models can not align exactly with the provided prompt in terms of the view angles. To address this issue, the authors propose a new algorithm called Perp-Neg, which leverages geometrical properties of the score space and does not require any training or fine-tuning of the model. The algorithm can be applied to both 2D and 3D generation. The paper shows the effectiveness of Perp-Neg in addressing the Janus problem in 3D object generation, the results show a fair improvement in the success rate of side/back views, leading to more view-consistent 3D objects. Additionally, the appendix contains sufficient ablations that confirm the importance of the design choices.

### Strengths
While the proposed method is simple, the authors have demonstrated its efficacy in 2D/3D diffusion. In addition, it does not require offline training and fine-tuning of the image diffusion model and can preserve the generalizability of the original diffusion model to a great extent.

The paper is clearly written and well organized, and the pipeline described in this submission is technically sound and reproducible.

Sufficient evaluations, such as the quantitative results of the success rate and qualitative results of the generated images of the side and back sides.

### Weaknesses
One of the most important applications of the proposed method is to boost the text-to-3D generation task. However, the experiment results shown in the paper mainly focus on 2D images on the side/back views, rather than the 3D generation.

The generated 3D objects are rather simple, so the effectiveness of the proposed method in the 3D generation of detailed objects needs to be further verified.

The comparison is a bit weak, it seems like CEBM is not designed for the task of this submission. Instead, the work [1], which also focuses on the view-consistent text-to-3D generation, should be cited and compared.

### Questions
What is the Compositional Energy-based Model (CEBM) and why choose it as a competing baseline? The paper does not provide an explanation for this choice, nor does it refer to any related work for CEBM.

What are the consequences of using just negative prompts instead of the proposed Perp-Neg in 3D generation? I think simply using negative prompts the regulate the 2D results on the back/side views may also alleviate the janus problem.

### Soundness
3 good

### Presentation
3 good

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
The paper proposes Perp-Neg, a method of using negative prompting without the negative effect of semantic overlap. The basic idea is to find the component of the negative prompt gradient that is orthogonal to the original prompt gradient. The authors show that this method can be used as a more effective negative prompting method, and also helps alleviate the Janus problem in score distillation for 3D generation.

### Strengths
1. The motivation (Section 2.2.1) is insightful. Semantic overlap seems to be an important drawback of naive negative prompting, and is not mentioned in previous papers before as far as I know.

2. The proposed method (Section 2.2.2 and 2.2.3) is elegant and intuitive.

3. The proposed method shows good qualitative results in generating view-dependent images (Figure 6).

### Weaknesses
1. The proposed method seems to be applicable in many tasks where gradients are mixed during inference (See [1] for an example). But the authors only focus on alleviating the Janus problem in 3D generation. I think it would be a stronger paper if more applications are included.

2. The number of qualitative results of 3D generation is too small. All I can find is Figure 2, 7, 20, which contain 9 examples with overlapping prompts (e.g. lions). The Janus problem is very common in score distillation based generation methods, so more such comparisons with a diverse set of prompts should be presented.

3. The qualitative results for view-dependent image generation (Figure 6, 10-18) re-use the same prompts (lion, panda, peacock) over and over again. It is better to use more different prompts to showcase the effectiveness of the method in the wild.

4. The comparison to other methods of 3D generation is limited and incomplete. I only see it in Figure 2 with 3 examples, and the last one for Magic3D does not show obvious difference to me. Weirdly in Figure 7, the captions claims the original Magic3D model fails to generate satisfactory results, but the figures do not show any of these "unsatisfactory" results.

### Questions
I think this method is interesting, but why do you focus so much on the Janus problem of 3D generation, instead of trying to demonstrate the method's effectiveness on more applications?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper solves the training data bias problem in the text-to-image model using a new formulation of negative prompt: Perp-Neg. This paper first presents the perp-neg algorithm where the latents are updated in the perpendicular gradient of “negative prompt- unconditional prompt“ with “positive prompt - unconditional prompt”. Then, this idea is utilized in solving 2D image generation with Janus problem in text-to-3d.

### Strengths
It is clever to solve Janus problem using negative prompts. 
The illustration of the algorithm is very easy to understand and plausible.
Code is provided to reproduce the results.

### Weaknesses
The visual results in the paper are good and interesting. 
A quantitative successful generation rate is also provided. My only concern is result part lacks quantitative fidelity results like FID, clip similarity, and user preference.

### Questions
I am happy to see more quantitative results

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
