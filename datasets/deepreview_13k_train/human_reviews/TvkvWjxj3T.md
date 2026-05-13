# Negative-prompt Inversion: Fast Image Inversion for Editing with Text-guided Diffusion Models

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
In image editing employing diffusion models, it is crucial to preserve the reconstruction fidelity to the original image while changing its style. Although existing methods ensure reconstruction fidelity through optimization, a drawback of these is the significant amount of time required for optimization. In this paper, we propose \textbf{negative-prompt inversion}, a method capable of achieving equivalent reconstruction solely through forward propagation without optimization, thereby enabling ultrafast editing processes. We experimentally demonstrate that the reconstruction fidelity of our method is comparable to that of existing methods, allowing for inversion at a resolution of 512 pixels and with 50 sampling steps within approximately 5 seconds, which is more than 30 times faster than null-text inversion.
Reduction of the computation time by the proposed method further allows us to use a larger number of sampling steps in diffusion models 
 to improve the reconstruction fidelity with a moderate increase in computation time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a method called negative prompt inversion that modified null text inversion for diffusion models and achieved a faster inversion method with forward computation only without optimizing, i.e., optimizing the null text embedding.  More specifically, in conventional null text inversion, one can optimize the null text embedding so that the predicted $z_{t-1}$ with CFG and $z_{t-1}^*$ in DDIM inversion. In this paper, instead, the authors investigated the conditions/constraints on noise $\epsilon_{\theta}$ to make $z_{t-1}$ equal to  $z_{t-1}^*$, which leads to a simper and faster inversion method. The methods are evaluated on 100 randomly selected COCO images with quality metrics like PSNR, LPIPS, etc., and speed.

### Strengths
1) The proposed idea of negative prompt inversion that only needs forward computation  but not optimization is qutie interesting.

2) The paper is organized and presented quite well, and friendly to understand, and easy to follow. Moreover, the introduction and related works parts are also quite helpful and informative to provide the big picture and the motivation.

3) Some promising results are shown in the experiments, with 30 times faster inversion than null text inversion methods.

### Weaknesses
1) The assumption that the predicted noises at adjacent diffusion steps are equal seems neither rigorous nor practical. The authors may need to provide more justification why this assumption is valid. Specifically, the diffusion process is a Markov chain, and while the noise prediction network is trained to approximate the reverse process, it doesn't guarantee that the predicted noise at step t will be identical to the predicted noise at step t-1, even with small step sizes. The error in this approximation could accumulate over multiple steps, leading to deviations in the inversion, especially for complex image structures.

2) The evaluation is done with only 100 COCO images, which is quite small. Moreover, only objective metrics are provided. Human subjective evaluation should also be provided since it is more reliable to judge the quality, which is quite easy to do considering the data set is small. The objective metrics like PSNR and LPIPS, while useful, do not fully capture the perceptual quality of the reconstructed images. Subtle artifacts or distortions might be missed by these metrics but are easily noticeable by human observers. A human study would provide a more comprehensive assessment of the method's performance.

3) The authors claimed some limitations about can not reconstruct faces well. It will be helpful to provide some failure face cases (and failure cases beyond faces if there are). Without specific examples, it's difficult to understand the nature of these failures. Are the faces blurry, distorted, or do they exhibit other types of artifacts? Providing visual examples of these failure cases would be crucial for understanding the limitations of the proposed method and for guiding future improvements.

### Questions
I actually like the proposed idea and this paper overall. If authors can resolver the questions in the weakness section, I will be happy to increase my rating.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the Negative Prompt Inversion method, which is designed for fast image reconstruction in the context of diffusion models, with a particular focus on image editing. The primary motivation behind this work is to achieve high-quality image reconstruction while reducing the computational cost and processing time involved.

The paper builds upon null-text inversion, a technique that leverages the denoising diffusion implicit model (DDIM) inversion and Classifier Free Guidance (CFG). Null-text inversion optimizes the embedding vector of an empty string to align the diffusion process calculated by DDIM inversion with the reverse diffusion process calculated using CFG. Negative Prompt Inversion is based on the observation that using the origin (resp. target) prompt instead of optimizing the null prompt brings comparable results in reconstruction (resp. edition). This simple modification offers a substantial improvement in processing speed.

### Strengths
- **Well-written paper**

- **Technically sound** The paper provides a clear summary of preliminary works as well as extensive justifications.

### Weaknesses
 - **Lack of comparison with existing baselines** The paper could benefit from a more comprehensive comparison with existing baseline methods. Specifically, it does not compare the proposed Negative Prompt Inversion with recent image editing methods based on prompt interpolation, such as Imagic or UniTune. This comparison would help assess the relative strengths and weaknesses of the proposed method in the context of image editing. Moreover, the proposed work as well as the Null-text inversion are also very close to the prompt tuning inversion paper and could also be compared to it. 

- **Mixed performances** The paper mentions that the image editing performances of Negative Prompt Inversion are below DDIM with CFG. This observation raises questions about the practical utility of the proposed method. 

- **Lack of justification** The paper does not sufficiently justify the underlying hypotheses and assumptions of the Negative Prompt Inversion method in the main paper. Specifically, the paper relies on two strong hypotheses regarding the equivalence of null-text inversion features and initial DDIM trajectories, as well as the equality of predicted noise at adjacent denoising steps. These hypotheses are not adequately explained or justified in the main paper and are relegated to the supplementary material. Providing a more robust rationale for these assumptions would enhance the paper's credibility and comprehensibility. Furthermore,  Proposition 3 in the supplementary is supposed to justify the second hypothesis in the general case, but it lacks clarity. In particular, the implication that $\alpha_t \simeq \alpha_{t-1} \Rightarrow z_t^{\ast} \simeq z_{t-1}^{\ast}$ should be clarified and expanded.

### Questions
- Are the edited images provided in the supplementary Fig. 8, second column, obtained with DDIM + CFG or just DDIM? In the former case, the results seem in disagreement with the CLIP score shown in Table 1. In the latter case, editing results with DDIM + CFG could be provided here. 

- Most of the justifications in the supplementary material (sec. A.1)  are provided for the case where the noise component is conditioned on the clean sample $z_0$. In this case, the conclusion holds $\bar{z}_t = z^*_t$. However, as stated later, the denoising model does not have $z_0$ as input. If it does not support the justification in the actual process of DDIM sampling, I wonder how useful are Prop. 1 and all the discussion from eq. (7) to (23)?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces negative-prompt inversion, a method that is capable of achieving comparable yet slightly degraded reconstruction quality as null-text inversion solely through forward propagation without optimization, thereby enabling much faster editing processes. Such an inversion technique is implemented by replacing the unconditional null-text prompt embedding with the conditional prompt embedding to modify the classifier-free guidance (CFG) in null-text inversion. Experiments demonstrate that the proposed negative-prompt inversion obtains comparable reconstruction quality as existing methods and is more than 30 times faster than null-text inversion. The authors also show that increasing sampling steps can further boost the reconstruction quality. Combining the proposed method with existing image editing methods like prompt-to-prompt allows fast real image editing.

### Strengths
- The paper is generally easy to follow. The symbols, terms, and concepts are adequately defined.

- The proposed method is very simple and easy to understand. Sufficient details are provided.

- The relevant literature is well-discussed and organized.

### Weaknesses
 - The reviewer's primary concern is the actual soundness of the proposed negative-prompt inversion. To the reviewer's understanding, replacing the unconditional null-text embedding with the conditional prompt embedding in null-text inversion is akin to/the same as DDIM inversion without CFG. It is necessary to provide the results of DDIM inversion w/o CFG and compare it with the proposed negative-prompt inversion to verify its soundness. If the proposed negative-prompt inversion has the same effect as DDIM inversion without CFG, such contribution is a bit slim.

- More detailed discussions and analyses on the computational cost and memory usage should be provided since the authors claim them as one of the main contributions. Specifically, a breakdown of the computational cost, including FLOPs and time, for each step of the proposed method compared to null-text inversion is needed. Furthermore, memory usage should be quantified, detailing the memory footprint of the different components of the method, such as the model, intermediate tensors, and embeddings.

- It is advisable to avoid too many detailed discussions on the relevant studies in the Introduction section, which can be moved to the Related Work section. Also, the general idea of the proposed method should be briefly discussed in the Introduction. The previous version is a bit vague.

- The Method section also presents too many preliminaries and background on DDIM inversion, CFG, and null-text inversion. Such content can be shortened since the information is generally well-known.

### Questions
- Will the authors release all the code, models, and data to verify the soundness and ensure the reproducibility of this work?

- Line 2 of Abstract: Image editing not only changes the style of the image. Sometimes it involves certain semantics or geometry changes.

- The authors mentioned that by parallelizing and optimizing the program, there is potential to further accelerate their, where even real-time processing would be possible. The reviewer is interested in how to parallelize the program since reverse diffusion is an iterative process.

- Section 7 on Page 10: Please remove any main paper content beyond Page 9 to avoid the potential of template/formatting violations of the conference.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an efficient inversion technique for text-conditioned diffusion models. The aim of inversion is to recover the original image as faithfully as possible in the reverse process from the noisy latents obtained in the forward process of the diffusion model. Authors build on an existing technique that rely on solving an optimization problem for each time step in the reverse process, and propose a modification that does away with the costly optimization. The resulting fast inversion technique can be used with diffusion-based editing framework to perform purely text-based image editing.

### Strengths
- To the best of my knowledge, the idea to replace the null-text embedding with the fixed-prompt embedding is original.
- Speeding up realistic image editing via diffusion models has significant impact, as the compute cost of such models is the main factor hindering wider adoption. 
- Based on the presented experiments, the speed-up can be significant (factor of 30x) while maintaining similar reconstruction quality to null-text inversion.

### Weaknesses
 - I find the core assumptions of the paper difficult to understand and I think more justification/verification is needed (see questions below).
- The experiments could be more thorough, especially on editing. How does the performance of DDIM inversion scale with $w$? If I understand correctly it is only shown for $w=1$. Moreover, editing performance should be evaluated on the same benchmark as Mokady et. al (2023) (Table 2. in Mokady et. al).

- Why would the predicted noise in adjacent steps equal (Eq. 6)? This would completely undermine the idea of iterative noising/denoising and would be very inaccurate for fairly large steps (such as N=50). How is the approximation impacted by the number of steps?

- If we approximate the optimized null-text embedding with C, it means that the same solution could have been found by null-text inversion, especially with shared embedding across time steps. How does null-text inversion compare with shared embeddings? Can we improve upon simply plugging in C by performing *some* optimization around C (not necessarily in every time step to reduce cost)?

- The experiments would be better presented in a way that compares inversion/editing performance *given a fixed time budget* in order to highlight the efficiency of the algorithm.

- I don't quite understand why the method is called negative-prompt inversion. Negative prompting commonly refers to a description of features in an image we do not want to generate in the context of text-conditioned diffusion models.

### Questions
- Why would the predicted noise in adjacent steps equal (Eq. 6)? This would completely undermine the idea of iterative noising/denoising and would be very inaccurate for fairly large steps (such as N=50). How is the approximation impacted by the number of steps? 

- If we approximate the optimized null-text embedding with C, it means that the same solution could have been found by null-text inversion, especially with shared embedding across time steps. How does null-text inversion compare with shared embeddings? Can we improve upon simply plugging in C by performing *some* optimization around C (not necessarily in every time step to reduce cost)?

- The experiments would be better presented in a way that compares inversion/editing performance *given a fixed time budget* in order to highlight the efficiency of the algorithm.

- I don't quite understand why the method is called negative-prompt inversion. Negative prompting commonly refers to a description of features in an image we do not want to generate in the context of text-conditioned diffusion models.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
