# Diffusion Sampling with Momentum for Mitigating Divergence Artifacts

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Despite the remarkable success of diffusion models in image generation, slow sampling remains a persistent issue. To accelerate the sampling process, prior studies have reformulated diffusion sampling as an ODE/SDE and introduced higher-order numerical methods. However, these methods often produce \emph{divergence} artifacts, especially with a low number of sampling steps, which limits the achievable acceleration. In this paper, we investigate the potential causes of these artifacts and suggest that the small stability regions of these methods could be the principal cause. To address this issue, we propose two novel techniques. The first technique involves the incorporation of Heavy Ball (HB) momentum, a well-known technique for improving optimization, into existing diffusion numerical methods to expand their stability regions.  We also prove that the resulting methods have first-order convergence. The second technique, called Generalized Heavy Ball (GHVB), constructs a new high-order method that offers a variable trade-off between accuracy and artifact suppression. 
Experimental results show that our techniques are highly effective in reducing artifacts and improving image quality, surpassing state-of-the-art diffusion solvers on both pixel-based and latent-based diffusion models for low-step sampling.
Our research provides novel insights into the design of numerical methods for future diffusion work.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission suggests to use higher order numerical scheme (heavy ball momentum coupled with higher order multi-step methods in numerical ODE) to compute the diffusion process in computer vision.

### Strengths
Authors' effort in experiments seem to be solid and thorough. 
Authors have also been patient to review basics of stability concept in numerical ODEs.

### Weaknesses
I recommend that authors add a paragraph explaining what "sampling" means in the context of diffusion in the appendix, so that the content can be more self-contained. From what I understand about the main text, authors mean generating/inferring an image with trained diffusion models. This is not equivalent to the meaning of illustrating the distribution of all potentially generated images given underlying diffusion models.


I also suggest that authors make a table to list all used numerical formats, explicitly, either in the main text or in appendix, to generate images. In this way, readers can associate the listed methods in each table/figure with specific algorithms. 
The current presentation stops at a conceptual derivation of discrete update format instead of concrete update formula. In a similar spirit, it will be also helpful for authors to detail the setup of the training paradigm (specifically, what the loss function is for training).

### Questions
- Are metrics "high-frequency error norm (HFEN)" [MR image reconstruction from highly undersampled k-space data by dictionary learning, Ravishankar and Bresler, 2011] and Structural Similarity Index (SSIM) potentially relevant to measure the divergence artifacts (section 5.1)? If yes, then reporting evaluation results in these two metrics can be helpful.

- Conceptually, I would like to understand better what authors mean by "classifier-guided diffusion sampling". What is the difference (conceptually and when it comes to implementation) between classifier-guidance and text-prompt based generation?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the artifacts problem of ODE/SDE-based diffusion sampling. Authors thought that the divergence artifacts are caused by the stability regions of high-order numerical methods for solving ODEs and proposed two solutions for expanding the stability regions of current diffusion numerical methods, called Heavy Ball (HB) momentum and Generalized Heavy Ball. And in the case of low-step sampling, the proposed methods are effective in reducing artifacts. But the actual improvement on diffusion sampling acceleration is unlear.

-------------
Post-rebuttal: I read the rebuttal and thanks for the authors' efforts. I would like to keep my score.

### Strengths
1.	The divergence artifacts problem is theoretically linked with the stability region of high-order numerical solvers for ODEs. The insight is very helpful for the design of diffusion sampling methods. 
2.	To enlarge the stability region, authors proposed Heavy Ball (HB) and generalized Heavy Ball (GHVB) as two solution without any training. Experiments show that the divergence artifacts are great mitigated in a low-step sampling case.
3.	This paper is well organized and solid in theory.

### Weaknesses
1.	The proposed method should be compared with the state-of-art methods in reducing divergence artifacts if it is a big challenge in diffusion models.
2.	The stated motivation is diffusion model acceleration. Experiments are limited in comparing the results of few-step sampling, lacking clear numerical experiments in model acceleration. The experiments focus on very low step counts, and it's unclear if the method provides benefits at higher step counts where image quality is typically better.
3.	It seems that the proposed methods show superior performance only in extremely low sampling steps. In the case of decent image quality, the improvement on sampling step is unclear.

### Questions
1.	The main difference between HB and GHVB is that HB calculates the moving average after summing high-order coefficients, whereas GHVB calculates it before the summation. Why does such a difference lead a larger stability region? 
2.	Can the divergence artifacts be solved or mitigated by improving the dynamic range of pixel?
3.	With additional training, what is the proposed methods’ complexity or cost?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on accelerating general diffusion sampling, where both unconditional and guided sampling are considered. Motivated by the observation that recent higher-order numerical methods would lead to diverging artifacts at lower sampling steps, the authors propose to incorporate heavy ball (HB) momentum into existing diffusion ODE solvers such as DPM++ and PLMS to mitigating their artifacts. In addition, an improved high-order version, namely generalized heavy Ball (GHVB) is also presented in this paper.  Experimental results have shown the effectiveness of this proposal.

### Strengths
1), Both pixel-based and latent diffusion models are considered in this paper.

2), The presentation is overall easy to follow.

3), Good practical extension to DPM++ and PLMS.

4), The literature over existing high order ODE solvers seems up to date.

### Weaknesses
1), The technical novelty behind this work seems to be not significant. The main techniques used in this paper are directly borrowed from Polyak’s heavy ball (HB) momentum method, a conventional optimization algorithm. Besides, the main improvements of this work are built based on DPM++ and PLMS.

2), While two methods are proposed in the same paper, it is unclear which one should be used under what circumstances. The paper only gives some vague statements without comprehensive comparison. The lack of clear guidance on when to use HB versus GHVB makes it difficult to assess their practical utility. Specifically, the paper does not provide a detailed analysis of the trade-offs between the two methods in terms of computational cost, memory usage, and convergence speed, which are crucial for practical applications.

3), While guided diffusion sampling is considered, the effectiveness of the HB/GHVB under different scaling factor “s” is not well discussed. The paper lacks a systematic exploration of how the guidance scale 's' interacts with the proposed methods. This is particularly important because the optimal value of 's' can vary significantly depending on the specific task and dataset, and the performance of HB/GHVB might be sensitive to this parameter.

### Questions
1), While the authors mentioned that the problem setup is more challenging in this paper than previous works, it is unclear what the challenges are. More discussions about why PLMS and DPM-Solver ++ perform worth than their original claims would strengthen this proposal.

2), Given that the 1000-Step DDIM’s sample is considered the benchmark, it would be reasonable to include evaluation metrics such as L2, LIPIS, and FID comparing HB/GHVB to DDIM, as depicted in Figure 11.

3), In Figure. 12, the authors attribute the inconsistency of GHVB 2.5 and 3.5 to estimated error or other sources of error without further justifications. It would be helpful to discuss this more for better understanding. 

4), Seems the comparisons and discussions between HB and GHVB are not sufficient in the paper’s current state. There is no clear cut which method is better for both conditional and unconditional diffusion sampling.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the Heavy Ball (HB) momentum into diffusion numerical methods to expand the stability regions. Meanwhile, the authors propose the high-order method, Generalized Heavy Ball (GHVB), to select the suitable method. Experiments show that the proposed HB and GHVB improves existing on both pixel-based and latent-based diffusion model in reducing artifacts and improving image quality.

### Strengths
1. The authors introduce the Heavy Ball (HB) momentum into existing diffusion methods to expand the stability regions. And they propose a high-order method, Generalized Heavy Ball (GHVB), to trade off between accuracy and artifact suppression.
2. The analyses are adequate. Through visualization and theoretical analysis, it is discovered that the small stability regions lead to model artifacts.
3. The experiments are extensive. The authors apply HB and GHVB on pixel-based and latent-based diffusion models to prove the effectiveness of the proposed method.
4. The authors also provide the code, which shows the solidness of the work.

### Weaknesses
The paper primarily experiments with 10 or more generation steps. But, it lacks analyses of extreme cases, such as one or two steps. It is suggested to evaluate the effectiveness of the proposed methods in these scenarios, e.g., one or two steps. For instance, the consistency model [1] performs well in one- and few-step generation. How effective is the method proposed in this paper compared with CM?

### Questions
1. How effective are the proposed methods in extremely small generation steps, such as one or two?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
