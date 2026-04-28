# PnP Inversion: Boosting Diffusion-based Editing with 3 Lines of Code

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Text-guided diffusion models have revolutionized image generation and editing, offering exceptional realism and diversity. Specifically, in the context of diffusion-based editing, where a source image is edited according to a target prompt, the process commences by acquiring a noisy latent vector corresponding to the source image via the diffusion model. This vector is subsequently fed into separate source and target diffusion branches for editing. The accuracy of this inversion process significantly impacts the final editing outcome, influencing both essential content preservation of the source image and edit fidelity according to the target prompt. 
Prior inversion techniques aimed at finding a unified solution in both the source and target diffusion branches. However, our theoretical and empirical analyses reveal that disentangling these branches leads to a distinct separation of responsibilities for preserving essential content and ensuring edit fidelity. Building on this insight, we introduce “PnP Inversion,” a novel technique achieving optimal performance of both branches with just three lines of code. To assess image editing performance, we present PIE-Bench, an editing benchmark with 700 images showcasing diverse scenes and editing types, accompanied by versatile annotations and comprehensive evaluation metrics. Compared to state-of-the-art optimization-based inversion techniques, our solution not only yields superior performance across 8 editing methods but also achieves nearly an order of speed-up.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents "direct inversion", a general inversion technique to improve essential content preservation and edit fidelity of diffusion-based image editing methods. An editing benchmark is also proposed for performance evaluation.

### Strengths
- The paper is well-written and well-presented with nice figures.
- The results are pleasing to look at and are convincing.
- The proposed method is simple and effective.
- Dataset/evaluation benchmark contribution.
- The experiments are comprehensive. The proposed method is quite general and is evaluated on 8 recent editing methods.

### Weaknesses
 - The method section 4.2 is not very clear to me, especially the bracket notations in the algorithm box. It would be helpful to explain lines 3, 7-9 in more detail.
- It might be worth adding discussion and comparison of a related but concurrent work [1].
- The name "direct inversion" clashes with another existing work [2], which might cause ambiguous.
- Typo: Algorithm 1, Part I: "Invert" z_0^{src}; sec 4.2, "optimization-based" inversion.
- The paper shows promising empirical results but is still not theoretically motivated.

### Questions
please see my questions in weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a method for Diffusion based inversion and editing, where all the intermediate generated zt values are stored and then utilized for sampling new samples based solely on the difference from the zt values generated during the sampling process. This approach is easy to apply to all editing methods. The method demonstrated its applicability to P2P, MasaCtrl, P2P-Zero, and PnP by calculating the difference between the zt values during the editing process (with those methods) and the zt values obtained from the original DDIM inversion. To evaluate this method, the paper introduced PIE-Bench, which used 700 images divided into 10 categories for editing to showcase the preservation of structure, background, and CLIP similarity.

### Strengths
This paper provided well-organized evaluation criteria, encompassing 10 different categories that include tasks such as changing or adding and removing objects, altering poses, changing colors, modifying materials, and changing backgrounds. Additionally, editing masks are also provided.

Based on these evaluation criteria, the paper presented a wide array of numerical evaluation results, proving superior performance across all categories. A detailed ablation study was provided, and in the supplementary material, various experimental setups and their results were thoroughly documented, offering valuable insights and enhancing reproducibility.

### Weaknesses
First and foremost, I would like to make a strong suggestion to the authors. The content of Figure 3 seems to be largely irrelevant to the content of the paper. While I express my utmost gratitude for the detailed explanation and organization of previous works, Figure 3 does not play a significant role in aiding understanding. Instead, I would prefer if Figure 5 from the supplementary material were included in the main text. Additionally, a more detailed explanation of the benchmarks and evaluation metrics in the main body of the text would be beneficial. This information is considered one of the major contributions of the paper, yet it is not present in the main text.

Secondly, the explanation of the method is unclear. There are no definitions provided for what the brackets [ ] mean in lines 3, 7, 8, and 9 of Algorithm 1, or what o_t represents. There is also a need for an explanation on whether z_t encompasses both src and tgt. If my understanding based on the code is correct, this paper stores all the zt values generated during DDIM inversion, uses them to calculate a small editing direction at each step, and then reflects this in the z^tgt used to generate the actual results. This algorithm feels somewhat similar to the approach used in CycleDiffusion [https://arxiv.org/abs/2210.05559]. A clearer explanation of the algorithm would greatly assist in correcting my understanding.

Thirdly, the benchmark is divided into 10 categories, but scores for each category are not reported. I am particularly interested in the scores for the category involving pose changes. I suspect that most of the proposed methodologies would struggle with changing poses. A discussion and reporting of scores on this matter would be appreciated, at least in the supplementary material.

Minor point: Regarding Figure 4, it is disappointing that the only result shown with our method applied is Ours+P2P. (But I saw additional results in Supple.)

### Questions
Please see the weakness part.

Especially I'm wondering about the Algorithm.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a simple but effective method that improves existing diffusion-based image editing methods. The method is very easy to implement, with only three lines of code. However, it helps resolve the discrepancy between source latent and target editing latent for many diffusion-based editing methods. This helps preserve essential content and maintain editing flexibility. The paper also presents a comprehensive image editing benchmark PIE-Bench covering ten editing types.

### Strengths
1. This paper presents a thorough investigation of existing diffusion-based prompt editing methods and identifies that previous methods improve essential content preservation through fine-tuning a learned variable to rectify the distance between the source branch latent and the target branch latent and propose a simple rectification method.
2. The proposed rectification method is simple but effective and is suitable for a large amount of diffusion-based editing methods. This paper presents comprehensive experiments to apply their method to different methods and see a universal improvement in both essential content preservation and edit fidelity.
3. This paper presents a comprehensive diffusion-based editing benchmark covering ten editing types and 700 human-reviewed high-quality samples with source prompt, target prompt, source image, and editing region annotation, which is helpful for future study.

### Weaknesses
1. The writing in the method part is hard to follow. I would suggest authors use meaningful subscripts to denote source latent, source prompt forward latent, and other patents instead of $z_0, z_t', z_{t}''$. Specifically, the notation does not clearly distinguish between the latents resulting from the forward process with the source prompt, target prompt, and the inverted latents. This lack of clarity makes it difficult to understand the precise operations being performed.

2. In the algorithm1, what is the meaning of argument $[C^{src}, C^{tgt}]$ in the DDIM_Forward function call? Is it suggesting that the forward function is called twice, with one of the calls on $C^{src}$ and the other on $C^{tgt}$? If so, why line 9 function call has only one output? The algorithm description lacks detail on how the source and target branches are processed within the DDIM forward step. It's unclear if the prompts are processed sequentially or in parallel, and how the information from each branch is combined or used.

3. I am confused about how the source branch interacts with the target branch. It seems that the $z_{t}^{tgt}$ is only updated using $z_{t+1}^{tgt}, C^{tgt}$ without any source branch information. Could authors clarify line 9 in the algorithm? Is it related to the implementation of $DDIMForward_{Editing_Model}$? The description of the interaction between source and target branches is vague. It is not clear how the source branch influences the target branch during the denoising process, particularly if the target branch is only updated with its own information. The role of the source branch in maintaining content is not well explained.

4. What's the number of images for each editing type in the PIE-Bench creation? As far as I understand, most of the editing types are local region editing, e.g., change object, add object, and large region editing is limited to style change only. I wonder if the dataset is mostly local editing images. The lack of specific information regarding the distribution of images across different editing types raises concerns about the benchmark's representativeness. It is unclear if the benchmark adequately covers both local and global editing scenarios.

5. What is the input text for CLIP similarity evaluation in **Whole** and **Edit**? As far as I understand, the target prompt in the PIE-Bench is a full description of the target image instead of the specification of the local region. Using a full description of the target image might not accurately reflect the quality of local edits, as the CLIP similarity might be dominated by the unchanged regions.

6. The CLIP Similarity for different methods seems very close in Table 1, 4, and 8. Is it possible the CLIP similarity cannot distinguish the editing quality? Could authors include BLIP similarity or human evaluation to make evaluation more comprehensive? The narrow range of CLIP similarity scores across different methods suggests that this metric might not be sensitive enough to capture the nuances of editing quality. The lack of alternative metrics raises concerns about the robustness of the evaluation.

### Questions
1. What is the meaning of step 1, 2 in Figure 2? 
2. In the algorithm1, what is the meaning of argument $[C^{src}, C^{tgt}]$ in the DDIM_Forward function call? Is it suggesting that the forward function is called twice, with one of the calls on $C^{src}$ and the other on $C^{tgt}$? If so, why line 9 function call has only one output?
3. I am confused about how the source branch interacts with the target branch. It seems that the $z_{t}^{tgt}$ is only updated using $z_{t+1}^{tgt}, C^{tgt}$ without any source branch information. Could authors clarify line 9 in the algorithm? Is it related to the implementation of $DDIMForward_{Editing_Model}$?
4. What's the number of images for each editing type in the PIE-Bench creation? As far as I understand, most of the editing types are local region editing, e.g., change object, add object, and large region editing is limited to style change only. I wonder if the dataset is mostly local editing images.
5. What is the input text for CLIP similarity evaluation in **Whole** and **Edit**? As far as I understand, the target prompt in the PIE-Bench is a full description of the target image instead of the specification of the local region.
6. The CLIP Similarity for different methods seems very close in Table 1, 4, and 8. Is it possible the CLIP similarity cannot distinguish the editing quality? Could authors include BLIP similarity or human evaluation to make evaluation more comprehensive?

I would increase my rating if the authors could resolve the questions.

### Soundness
3 good

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
The $\textbf{Direct Inversion}$ technique separates the source and target diffusion branches, enhancing content preservation and edit fidelity. It surpasses previous methods and substantially accelerates editing, as evidenced by the PIE-Bench benchmark.

### Strengths
This paper proposes a novel technique called Direct Inversion, which tackles the problem of balancing content preservation and edit fidelity in previous works. Motivation is clear and presentation is in a roughly good shape overall.

1. Direct Inversion is neat and can be used as a plug-and-play into popular optimizaiton-based diffusion editing methods to enhance the performances.

2. The paper provides a comprehensive and well-structured review of existing literature. Analysis of each method makes the motivation strong and presentation clear.

3. Experimental results are sound and analysis is rigorous.

4. Authors also provide a editing benchmark, called PIE-Bench, which is believed to benefit future works.

### Weaknesses
See questions.

1. In the column PnP of Fig.1, PnP doesn't do a good job in preserving content, sometimes texture and shape is hallucinated. Using direct inversion can correct them. But why not background color in the third row?

2. Following Fig.2, "...This results in a learned latent with a discernible gap between $z_0^{''}$ and the original $z_0$...". So how does the optimized $z_0^{''}$ deviates from original distribution? It's not quite clear how deviation happens, what does it look like, and why it negatively affects performances. Could authors provide concrete examples?

### Questions
1. In the column PnP of Fig.1, PnP doesn't do a good job in preserving content, sometimes texture and shape is hallucinated. Using direct inversion can correct them. But why not background color in the third row? 

2. Following Fig.2, "...This results in a learned latent with a discernible gap between $z_0^{''}$ and the original $z_0$...". So how does the optimized $z_0^{''}$ deviates from original distribution? It's not quite clear how deviation happens, what does it look like, and why it negatively affects performances. Could authors provide concrete examples?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
