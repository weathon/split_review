# The Blessing of Randomness: SDE Beats ODE in General Diffusion-based Image Editing

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
We present a unified probabilistic formulation for diffusion-based image editing, where a latent variable is edited in a task-specific manner and generally deviates from the corresponding marginal distribution induced by the original stochastic or ordinary differential equation (SDE or ODE). Instead, it defines a corresponding SDE or ODE for editing. In the formulation, we prove that the Kullback-Leibler divergence between the marginal distributions of the two SDEs gradually decreases while that for the ODEs remains as the time approaches zero, which shows the promise of SDE in image editing. Inspired by it, we provide the SDE counterparts for widely used ODE baselines in various tasks including inpainting and image-to-image translation, where SDE shows a consistent and substantial improvement. Moreover, we propose \emph{SDE-Drag}  -- a simple yet effective method built upon the SDE formulation for point-based content dragging. We build a challenging benchmark (termed \emph{DragBench}) with open-set natural, art, and AI-generated images for evaluation. A user study on DragBench indicates that SDE-Drag significantly outperforms our ODE baseline, existing diffusion-based methods, and the renowned DragGAN. Our results demonstrate the superiority and versatility of SDE in image editing and push the boundary of diffusion-based editing methods. See the project page \url{https://ml-gsai.io/SDE-Drag-demo/} for the code and DragBench dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper show theoretically and experimentally the benefit of using diffusion model SDEs over ODEs for image editing. The authors formulate the image editing with diffusion model process in three steps : 1) encoding with deterministic or random noise 2) alteration of the latent which means modification of the prior distribution representing this latent 3) SDE or ODE sampling starting from the altered latent.
On the theoretical side, it is proven that during step 3, the KL distribution between the SDE marginals : a) when sampling from the altered latent and b) sampling from the original latent, decreases, while remaining constant when sampling with ODEs. On the experimental side, it is analyzed, from different works, the benefit of using SDEs over ODEs in step 3.

### Strengths
The argumentation is limpid, and the contributions are clearly stated.  

Although I am not an expert in image editing, I think that the main strength of the paper is its experimental study, which looks impressive. It contains numerous comparisons in three different tasks.  Moreover, the authors created an evaluation benchmark for point dragging and conducted a user study for evaluation on this problem. The advantage of SDEs over ODEs is clearly demonstrated experimentally.

I like the fact that the authors took care to expose a very easy Gaussian toy example to illustrate the theorems.

### Weaknesses
Major weaknesses : 
- The problematic of the paper (end of Section 3.1) is never clearly answered. Actually, I do not think that the paper properly gives the answer to this question. This is link to the following point.
- It is not clear that the proposed theoretical arguments prove the right point. Given $x_0$ (resp. $\tilde x_0$) sampled from the latent $x_{t_0}$ (resp.  $\tilde x_{t_0}$. ), with Theorem 3.1, it is proven that the $x_0$ and $\tilde x_0$ are closer “in distribution” than $x_{t_0}$ and $\tilde x_{t_0}$. Why is that desired ? 
I think that the authors see $p_0$ as the distribution of clean images $q_0$, and then wish to minimize $KL(p_0, \tilde p_0)$ to get well-looking images. However, $p_0$ is very different from $q_0$ because the score is not (and for from being) perfectly matched with the denoiser. From this fact, could the authors explain why it makes sense to try to minimize $KL(p_0, \tilde p_0)$ ? I am more likely to think that, for the purpose of image editing, it does not make sense to try to minimize the distance between these two distributions. 
- In the experimental section, some important information is missing : which model are you using, trained on which dataset ? 

Minor weaknesses : 
- In the paragraph "Samples" from Section 2. The term "equivalent" is not true. Sampling is not "equivalent" to discretization ! Moreover, discretizing (4) or (5) does not enable to sample from $q_0$ if the score is not perfectly matched with $\epsilon_\theta$.
- The ODE inversion process explanation should be clarified. The links and differences between deterministic ODE inversion and random Gaussian noise should be explained. 
- The "mild assumption" should be detailed, at least in the Appendix.

### Questions
- If the noise is fixed, is CycleSDE still an SDE ? 
- Is the log-Sobolev inequality likely to be verified in practice ?

I am prepared to improve my score by taking into account the author's feedback.

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
This paper focuses on image editing using pre-trained diffusion models. The authors propose a unified probabilistic formulation for diffusion-based image editing, including inpainting, image-to-image translation, and dragging, based on existing methods. Experiments show that the proposed method achieves better performance than the original ODE version.

### Strengths
1. The authors provide SDE versions for existing ODE-based editing methods and achieve better performance.

2. The authors build a benchmark called DragBench for evaluation, which may benefit the community.

3. The paper is well written, and the experiment and presentation are solid.

### Weaknesses
1. The core idea that SDE beats ODE in image editing seems similar to CycleDiffusion [6]. This article seems to just generalize this phenomenon to multiple tasks and verify them. Overall, the innovative contribution seems insufficient. 

2. The authors claim to propose a unified probabilistic formulation for diffusion-based image editing. However, many related image editing/I2I methods are not mentioned, e.g., RePaint [1], DDNM [2], DPS [3], T2I-Adapter [4], and ControlNet [5].

### Questions
Please see the Weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a unified probabilistic formulation for diffusion-based image editing and introduces a simple yet effective dragging algorithm based on this formulation. The authors conduct experiments on various tasks, including inpainting, image-to-image translation, and dragging, demonstrating the superiority of their SDE-based approach.

### Strengths
1. The paper provides a comprehensive theoretical analysis of the SDE and ODE formulations for general image editing.
2. The authors propose the SDE-Drag algorithm for dragging.
3. The experiments across different tasks, including inpainting, image-to-image translation, and dragging, demonstrate the effectiveness of the SDE formulation in improving image editing tasks compared with the ODE baselines.
4. The authors also provide the code, which shows the solidness of the work.

### Weaknesses
1. While the paper shows that SDE outperforms ODE baselines in inpainting and image-to-image translation, it lacks a comparison with the latest methods in these tasks. Specifically, the paper does not benchmark against state-of-the-art inpainting models that leverage contextual attention or transformer-based architectures, nor does it compare against recent GAN-based or diffusion-based image-to-image translation methods that have demonstrated superior performance on benchmark datasets. This makes it difficult to assess the true practical impact of the proposed SDE formulation in these well-established tasks.
2. The paper provides the cost time for the dragging task but does not provide similar information for inpainting and image-to-image translation. This omission makes it hard to evaluate the practical applicability of the proposed method in these tasks, especially given that computational cost is a critical factor in image editing applications. The lack of this information prevents a comprehensive comparison with existing methods, which often report detailed timing results.

### Questions
1. It is suggested to compare the performance of SDE in inpainting and image-to-image translation with the latest methods.
2. Provide the running time of their proposed methods for inpainting and image-to-image translation tasks. And including the running time of the latest methods in these tasks to provide a more complete picture of the computational efficiency.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
