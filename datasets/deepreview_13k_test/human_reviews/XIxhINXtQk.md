# InstructPix2NeRF: Instructed 3D Portrait Editing from a Single Image

- Decision: Accept
- Scores: 5, 8, 6

## Abstract
With the success of Neural Radiance Field (NeRF) in 3D-aware portrait editing, a variety of works have achieved promising results regarding both quality and 3D consistency. However, these methods heavily rely on per-prompt optimization when handling natural language as editing instructions. Due to the lack of labeled human face 3D datasets and effective architectures, the area of human-instructed 3D-aware editing for open-world portraits in an end-to-end manner remains under-explored.
To solve this problem, we propose an end-to-end diffusion-based framework termed \textbf{InstructPix2NeRF}, which enables instructed 3D-aware portrait editing from a single open-world image with human instructions. 
At its core lies a conditional latent 3D diffusion process that lifts 2D editing to 3D space by learning the correlation between the paired images' difference and the instructions via triplet data.
With the help of our proposed token position randomization strategy, we could even achieve multi-semantic editing through one single pass with the portrait identity well-preserved.
Besides, we further propose an identity consistency module that directly modulates the extracted identity signals into our diffusion process, which increases the multi-view 3D identity consistency.
Extensive experiments verify the effectiveness of our method and show its superiority against strong baselines quantitatively and qualitatively. 
Source code and pretrained models can be found on our project page: \url{https://mybabyyh.io/InstructPix2NeRF}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The proposed approach, InstructPix2NeRF, is an end-to-end model designed for 3D-aware human head editing using a single image and an instructive prompt as inputs. To achieve this results, firstly the authors construct a multimodal 2D human head dataset by leveraging pretrained diffusion models such as e4e and InstructPix2Pix. Secondly, they propose a token position randomization strategy to enhance the model's ability to edit multiple attributes simultaneously. Last, an identity consistency module is incorporated to extract facial identity signals from the input image and guide the editing process. Experimental results demonstrate the effectiveness and superiority of the method.

### Strengths
The strengths of the proposed paper can be summarized as:
1. The authors propose a token randomization strategy that can increase the model's capability for editing multiple attributes simultaneously.
2. An identity-preserving module is proposed to guide the editing process and present the original identity in the final outcomes.
3. The proposed method is reported to be time-friendly, producing the results in few seconds.

### Weaknesses
The weaknesses of the proposed method can be summarized as:
1. Through the visualization in Figure 1, I find that the original identity and RGB image attributes are not well preserved. Large differences can still be observed in the areas that are not supposed to be edited.
2. Qualitative comparisons. (1) The proposed method seems to struggle with expression editing, e.g., it fails to make the head smiling; The instruct-pix2pix model doesn't encounter this problem; (2) Regarding the "bangs" example, I would prefer the instruct-pix2pix as it contains real bangs; (3) There is no comparisons with Instruct-NeRF2NeRF, AvatarStudio, and HeadSculpt, considering they are more similar works than the compared Talk-to-Edit and img2img; (4) More examples and more scenarios will largely improve the validation. Currently, there are only three types presented.
3. Quantitative comparisons. (1) The evaluations are not comprehensive. Still, only three examples are presented; (2) More quantitative evaluations, e.g., user studies, would be beneficial.

### Questions
Besides the weaknesses above, I may have some questions that hope the authors can answer:
1. There lack the reason for generating and using 20-30 instruction prompts for one single paired image. Will the number of instructions affect the training?
2. How will the model perform when it deals with novel characters as in the movie, long hair examples, black men/women, and human of different ages?
3. Will the background affect the edited results? It would be interesting to see the outcomes obtained when editing the same subject against various backgrounds.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a method that enables the creation of 3D portraits that have been edited based on text prompts. Leveraging the latent space of EG3D to impose 3D consistency, the proposed method finds a latent vector in the W+ space that matches the edits specified by the prompt and the identity in the input image. A diffusion model conditioned on the input 2D image and the editing prompt is used to predict this latent vector. Additionally, the paper proposes the following 1) Token position randomization to improve the quality of multi-instruction editing 2) An identity consistency module to improve identity preservation during edits.

### Strengths
1) While each individual component of the method isn’t novel, the whole method itself is

2) Qualitative results in both the paper and appendix demonstrate plausible editing, though some identity loss remains

3) Quantitative results demonstrate that the method better preserves the identity across edits. The user study additionally bolsters the main contribution of the paper.

### Weaknesses
1) The methods section could be written better, with a clear exposition of losses during training and the forward pass during inference. To that end, Fig 2 should be expanded to include both training and inference settings. 

2) While the identity consistency is better preserved that prior work, the still remains and identity drift during editing.

### Questions
1) Instead of an Encoder, if direct optimization of the W+ vector was used (assuming much larger compute), would it preserve the identity better? What if this is only done during inference and not training?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method that generates a 3D-edited NeRF from a single portrait image. The style is defined by an instructing prompt. Two streams of inputs of a real face and a 2D-edited face are passed through an encoder to generate identity conditions. The identity condition, together with text condition, is sent to a diffusion model to generate tri-plane features for NeRF rendering. Experimental results show that the proposed method outperforms compared baseline approaches under the authors' settings.

### Strengths
- It is the first (to my knowledge) paper that allows "instructed" 3D portrait editing from single images.

- The experiments show that the proposed method outperforms compared baselines under the authors' settings.

### Weaknesses
- The results shown in the paper lack race diversity. There are almost no Asian or black people. I'm worried whether the proposed method does not perform well on those cases.

- The identity may change after applying the proposed method. For example, in Fig. 1 first example, the eye shape changed after the beard was removed. In Fig. 3 middle example, the girl seems to look more Asian and the nose shape changed after editing. These are not analyzed in the limitation section.

- The proposed method adopts two streams of inputs (real and edited images). However, the ablation study does not show the necessity of  
 them. Will only one stream work?

### Questions
I would like to see the authors address my concerns mentioned in the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
