# Physics-Informed Self-Guided Diffusion Model for High-Fidelity Simulations

- Decision: Reject
- Scores: 3, 3, 6, 5, 6, 5

## Abstract
Machine learning (ML) models are increasingly explored in fluid dynamics as a promising way to generate high-fidelity computational fluid dynamics data more efficiently. A common strategy is to use low-fidelity data as computational-efficient inputs, and employ ML techniques to reconstruct high-fidelity flow fields. However, existing work typically assumes that low-fidelity data is artificially downsampled from high-fidelity sources, which limits model performance. In real-world applications, low-fidelity data is generated directly by numerical solvers with a lower initial state resolution, resulting in large deviations from high-fidelity data. To address this gap, we propose PG-Diff, a novel diffusion model for reconstructing high-fidelity flow fields, where both low- and high-fidelity data are generated from numerical solvers. Our experiments reveal that state-of-the-art models struggle to recover fine-grained high-fidelity details when using solver-generated low-fidelity inputs, due to distribution shift. To overcome this challenge, we introduce an \textit{Importance Weight} strategy during training as self-guidance and a training-free \textit{Residual Correction} method during inference as physical inductive bias, guiding the diffusion model toward higher-quality reconstructions. Experiments on four 2D turbulent flow datasets demonstrate the effectiveness of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to improve on prior super-resolution works by introducing a new importance weighting and training-free correction method to train a diffusion model. The paper presents experiments on 4 benchmarks, and shows improved performance over baselines.

### Strengths
The paper has a few key strengths: (1) the model improves over baseline models, (2) the benchmarks are a challenging and convincing set of problems, (3) the DWT-based importance sampling seems to work well, and is well-motivated, (4) the results and ablation studies are well done and provide good insight.

### Weaknesses
Unfortunately, this paper also has significant flaws that lead me to doubt its novelty and contributions, and as a result, this paper should be rejected in its current state. The main concern is that many of the claims made in the paper are either not well-supported or are false.

(1) Section 1, Introduction: “We study a novel problem on reconstructing high-fidelity flow fields with solver-generated low-fidelity data, benefiting real-world applications. Our experiments reveal that state-of- the-art reconstruction models fail to generate high-quality outputs due to large distribution shifts between low- and high-fidelity data.”

The first part of this claim, which is central to the paper, is not true. Upsampling solver-generated low-fidelity data has been both posed as well as solved before [1, 2]. While the provided references are not exhaustive, prior work has considered the limitation of super-resolution works downsampling high-resolution data and have worked directly with solver-generated low-fidelity data. The novelty is further diminished by the fact that the core idea of using a diffusion model for super-resolution is already established.

The second part of this claim does not seem to be well-supported. While it is true that the proposed model outperforms current diffusion models, there is not much evidence for the provided reason being due to a distribution shift. In fact, one of the main insights presented in the cited prior work from Shu et al. [3] is that by noising data samples, they all approach the same distribution regardless of the original distribution being from high or low fidelity data. By that argument, diffusion models should be agnostic to whether the guide data comes from downsampled high-resolution simulations or low-resolution simulations, since when fully noised these samples are drawn from nearly identical distributions. The paper does not provide any analysis or experiments to support the claim that a distribution shift is the primary cause of poor performance in other models.

(2) Section 4.6, Model Generalization: “We observe that PG-Diff generalizes well even beyond its training distribution”

The spatial domain size variations don’t seem to generate samples outside of the training distribution, since the smaller domains are a subset of the larger training domain. The other test cases could be out of the training distribution, but even then, using a smaller dt shouldn’t significantly alter the data distribution. The claim of generalization is not thoroughly validated, and the experiments do not convincingly demonstrate generalization to truly unseen distributions.

(3) Section 4.3, Runtime Comparison:“PG-Diff is considerably faster than the time required to produce high- fidelity data directly through numerical solver”

Following one of the cited papers from McGreivy & Hakim [4], the runtime comparison with a numerical solver is not faithfully done. In particular, the numerical solver should be coarsened until it achieves a similar L2 error as the proposed method. The runtime of the coarsened solver should be compared with the proposed method instead of the zero-error, ground truth numerical runtime. The current comparison is misleading and does not provide a fair assessment of the computational benefits.

There are a few more minor concerns about the work.

(1) Section E.4: The argument about LPIPS being a suitable metric is not empirically or theoretically sound. The given reasoning about ImageNet containing multiscale features and textures leading to it generalizing to CFD applications is somewhat hand-wavy and without providing evidence, it is challenging to claim that a model trained on ImageNet would be “a robust metric” for physics simulations. The LPIPS metric is not a standard metric for evaluating physical simulations, and its use requires more justification.

(2) Multiscale Evaluation: The authors claim to achieve best or near-best results on all subdomains but there are results where the proposed method is not the best, especially in the Appendix Figures 11, 12, 13. The claim of superior performance across all subdomains is not entirely accurate, and the paper should acknowledge the limitations of the proposed method in certain subdomains.

(3) Residual Correction During Inference: While the technique improves performance, it seems highly dependent on hyperparameters. In particular, there is reduced performance when using more correction steps, likely due to the data being corrected to samples outside of the model’s training distribution. It seems odd that a core method of the paper asymptotically reduces performance (i.e., as more compute/refinement is done, the worse the model gets). The instability of the residual correction method and its sensitivity to hyperparameters raise concerns about its robustness and practical applicability.

### Questions
Do you have any intuition as to why the model trained on Re=2000 performs worse than the model trained on the original data when evaluated on a Re=2000 test case? (Table 3)
Is there a reason why the bicubic upsampling is quite slow? (Table 8)

As a whole, the main contributions of the paper seem to be an importance weighting and correction step during inference, which seems to be an incremental improvement on a prior work from Shu et al. [3].

Rajat Kumar Sarkar, Ritam Majumdar, Vishal Jadhav, Sagar Srinivas Sakhinana, Venkataramana Runkana. Redefining Super-Resolution: Fine-mesh PDE predictions without classical simulations. https://arxiv.org/abs/2311.09740
Francis Ogoke, Quanliang Liu, Olabode Ajenifujah, Alexander Myers, Guadalupe Quirarte, Jonathan Malen, Jack Beuth, Amir Barati Farimani. Inexpensive high fidelity melt pool models in additive manufacturing using generative deep diffusion. https://www.sciencedirect.com/science/article/pii/S0264127524005562
Dule Shu, Zijie Li, Amir Barati Farimani. A physics-informed diffusion model for high-fidelity flow field reconstruction. https://www.sciencedirect.com/science/article/pii/S0021999123000670
Nick McGreivy, Ammar Hakim. Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations. https://www.nature.com/articles/s42256-024-00897-5

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes PG-Diff which uses diffusion model to generate high-fidelity computational fluid dynamics (CFD) data when given low-fidelity CFD data. To make it works, during the training phase, the authors introduce "Importance Weight" to the loss function; during the inference phase, the authors introduce "Residual Correction" as physical guidance.

### Strengths
This paper leverages diffusion model to solve problems in fluid dynamics. One advantage of this current version is that the authors incorporate physical information to guide diffusion model. In addition, the authors also conduct detailed analysis on important hyper-parameters and model generalization.

### Weaknesses
There are several weaknesses for this current version.
1) The motivation and problem setting are not clear. I would suggest the authors re-organize the "Introduction" to clearly sate the problems as well as the challenges.
2) The overall presentation is a little bit messy.
3) The experiments are only conducted on simulated datasets; how this proposed method would work in a real-world application? For example, what will happen if the low-fidelity CFD data containing nosies such as Gaussian noise/shot noise? Will this proposed method still work?
4) Based on the visual results, the proposed method does not show superior performance compared to other diffusion models.

### Questions
I list my questions in "weaknesses" section.

### Soundness
2

### Presentation
1

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
This paper proposes PG-Diff, a diffusion model for high-fidelity flow field reconstruction. They introduce importance weight strategy during training as self-guidance and a training-free residual connection method during inference as physical inductive bias, to overcome the distribution shift challenge in this task.

### Strengths
- This paper found that current SOTA reconstruction models fail to generate high-quality outputs due to large distribution shifts between low- and high-fidelity data.
- To address this issue, they propose a diffusion model to reconstruct the high-quality outputs through the guidance of an Importance Weight strategy during training as self-guidance and
a training-free Residual Correction method during inference as physical inductive bias.

### Weaknesses
 - Literature review is not comprehensive, some papers in solving high-fidelity fluid flow reconstruction are not properly cited: 
[1] “Fu, Cong, Jacob Helwig, and Shuiwang Ji. "Semi-Supervised Learning for High-Fidelity Fluid Flow Reconstruction." Learning on Graphs Conference. PMLR, 2024.” 
[2] “Esmaeilzadeh, Soheil, et al. "Meshfreeflownet: A physics-constrained deep continuous space-time super-resolution framework." SC20: International Conference for High Performance Computing, Networking, Storage and Analysis. IEEE, 2020.” 
[3] “Ren, Pu, et al. "PhySR: Physics-informed deep super-resolution for spatiotemporal data." Journal of Computational Physics 492 (2023): 112438.” 
[4] “Gao, Han, Luning Sun, and Jian-Xun Wang. "Super-resolution and denoising of fluid flow using physics-informed convolutional neural networks without high-resolution labels." Physics of Fluids 33.7 (2021).” 

- For comprehensive evaluation, I recommend authors also add commonly used metrics from image super-resolution such as PSNR and SSIM. 
- For Figure 4, the high-resolution and low-resolution simulations basically have very similar pattern, which doesn’t well demonstrate the assumption that coarse-grained simulation differ from high-resolution simulation. I recommend authors use the test equation in this paper (“Machine learning accelerated computational fluid dynamics”: https://arxiv.org/pdf/2102.01010), In Fig 2 of that paper, it’s clear at time step 1500 that fluid flow simulated from low-resolution input deviate a lot from high-resolution input, where simple super-resolution cannot be applied. I would like to see PG-Diff can reconstruct high-fidelity flow in this scenario.

### Questions
- In algorithm 1, during inference the input is not pure noise, then how to determine T_guide?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript aims to solve the problem of super-resolution of physical fields. Specifically, they draw on the framework in [1]. The difference lies in 1) weighting the denoising loss over pixels using the wavelet transform and 2) performing physical loss gradient descent over clean predictions.

[1] A physics-informed diffusion model for high-fidelity flow field reconstruction

### Strengths
1. Authors present four turbulence datasets with different characteristics.

2. I agree with one of the author's points in the introductory section. They note that some of the current work focuses on low-resolution data that is downsampled. This is not consistent with reality, and in fact, to apply these super-resolution models, such data should come from the low-resolution simulation of a PDE solver, which typically has lower fidelity than downsampled ones.

2. The amount of experiments is rich enough, and all the graphs are clear.

### Weaknesses
1. I have some questions about the authors' contributions to modeling. First is the training phase. The authors use the wavelet transform to determine which pixels need to be weighted. As can be seen from the visualization in Figure 10, the weighting seems to be added only at high frequencies. This raises the question of whether a complex wavelet transform needs to be introduced. This is because we can simply call the Laplace operator to achieve this effect. Furthermore, from the quantitative results in Table 1, it seems that this measure does not contribute much to the results.

2. In addition, another contribution of the authors is to perform gradient descent on clean samples at each step to reduce the residuals on the equations. The authors ignore many related diffusion model guided generation literature [1,2,3] that the authors do not cite and discuss here.

3. The authors claim that their high-fidelity data is actually simulated on a grid of 256. It is important to realize that for such a large Reynolds number (1000+), this resolution is usually insufficient. shu et al. [4]'s data was simulated on a grid of 2048.

### Questions
see Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a diffusion-based method for reconstructing high-fidelity physics simulation data given low-fidelity input. The paper also proposes to incorporate prior knowledge via the gradient of PDE residual and a new weighting scheme based on multi-resolution analysis (Wavelet transform) for diffusion loss. The numerical experiments on several 2D flow problem showcase that the proposed method has better L2 accuracy and lower residuals over other baseline methods.

### Strengths
1. Upsampling and reconstructing under-resolved physics is important for building hybrid solver and inverse problem in PDE applications.

2. A new spatial weighting scheme based on Wavelet transformation which modulate the loss based on the spectrum of signal. The new scheme is technically sound and experiments show that it consistently improves model performance.

3. The introduction to the proposed method is clear and easy-to-follow.

### Weaknesses
1. Applying diffusion model with guidance based on target constraint for the inverse problem is not an entirely new technique (for example, DPS: https://arxiv.org/pdf/2209.14687 and On conditional diffusion models for PDE simulations: https://arxiv.org/abs/2410.16415 has explored similar technique)

2. The evaluation of model’s prediction in terms of physics coherence is relatively vague. First, all the reported residuals are quite large and there is no reference showing what is a reasonable scale. While the average error of different frequency components in the wavelet domain is shown, there is no information on the spectrum of different wavelength. Furthermore, the paper does not provide a clear justification for the chosen residual calculation method, specifically how the residual is calculated and averaged across the spatial domain. This lack of detail makes it difficult to assess the physical relevance of the reported residual values.

3. The authors run the solver on a coarse grid to get the “low fidelity” data and then run the solver on fine grid to get “high fidelity” data, instead of artificially downsampling the data. The low-fidelity simulation will deviate from the high-fidelity one as time evolves due to the under-resolved error. Yet looking at the figure comparing data trajectory of different fidelities, the general structures of the vortices are very similar across different fidelities (for example, Figure 8) in my opinion. I hope the authors can provide more clarification and analysis regarding the dataset, such as the spectrum of different simulation and perhaps a simple study of mesh convergence.

### Questions
* Following point 2, what is the residual of the reference DNS simulation?

* The authors state that the high fidelity data for 2D Kolmogorov flow is derived by running DNS on a 256 x 256 grid (feel free to correct me if I’m wrong). However, under a similar setting (Re=1000), prior works like Shu et al. [1] and Kochkov et al. [2] have used a much finer discretization, i.e. 2048 x 2048. 

* (Minor) In algorithm 1, what is the rationale for using Adam instead of simpler gradient descent? In addition, is Adam re-initialized after very DDIM step?

[1] Shu, D., Li, Z., & Farimani, A. B. (2023). A physics-informed diffusion model for high-fidelity flow field reconstruction. Journal of Computational Physics, 478, 111972.

[2] Kochkov, Dmitrii, et al. "Machine learning–accelerated computational fluid dynamics." Proceedings of the National Academy of Sciences 118.21 (2021): e2101784118.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a diffusion model designed to reconstruct high-fidelity computational fluid dynamics (CFD) data from low-fidelity solver-generated inputs. Traditional machine learning models for CFD rely on low-fidelity data artificially downsampled from high-fidelity sources, which limits performance in real-world applications. This paper trains on the data run at two different grid sizes and proposes two directions to improve upon this:

- Importance Weight Strategy during training: It uses wavelet transformation to assign importance to high-frequency flow field components, guiding the model toward better reconstruction of detailed structures.
- Residual Correction during inference: This physics-informed module applies corrections based on governing equations (e.g., Navier-Stokes) to ensure physical accuracy, especially for turbulent flows.

The model is evaluated on four datasets, generated by the incompressible Navier-Stokes equations.

### Strengths
This paper points out an important issue with training ML models for super-resolving computational fluid dynamics (CFD) which is when running CFD at two different grid sizes, the dynamics between them can diverge and will not correspond to an interpolation of each other.  This paper argues that one should train ML models from simulations run at different resolutions.

The paper is very nicely written. There is a sufficient number of figures to explain the core ideas. 

I found the idea of using residual error correction an interesting development that makes sure that the generated high-fidelity solution matches with the underlying PDE.

### Weaknesses
The weighting function in 6 seems arbitrary and hacky. There is no intuitive explanation of why this form of weighting mechanism is needed. Note that this mechanism should be discussed in the context of prior work such as simple diffusion [1] who also suggest reweighting the objective based on the resolution of the data.

The paper discusses the fact that running PDEs at different resolutions will not correspond to the same solutions that are interpolated. However, it is known that running PDEs at different grid sizes will eventually diverge over time to the point that we cannot recover the high-fidelity solution from the low-fidelity input. This work does not discuss how one can correct the low-fidelity simulation with the information received from the high-fidelity solution. 

The choice of the weighting function in equation 6 lacks a clear justification. While the authors use a wavelet transform to identify high-frequency components, the linear mapping to importance weights between alpha and beta seems ad-hoc. There is no discussion on how the specific values of alpha and beta are chosen, or how sensitive the model is to these parameters. Furthermore, the connection to the reweighting strategies used in simple diffusion [1] is not thoroughly explored. A more rigorous analysis of the weighting function and its impact on model performance is needed.

The paper acknowledges that solutions from simulations at different resolutions diverge over time. However, the method does not address how to correct the low-fidelity simulation based on the high-fidelity information. The current approach focuses on reconstructing a single high-fidelity frame from a low-fidelity input, but it does not provide a mechanism for long-term correction of the low-fidelity simulation. This is a significant limitation, as the divergence of solutions over time is a key challenge in multi-scale simulations. The paper should discuss how the proposed method could be integrated into a simulation loop to provide continuous corrections to the low-fidelity simulation, or at least acknowledge this limitation more explicitly.

The paper claims that the residual correction module ensures physical accuracy, but the details of how this is achieved are not fully clear. The residual calculation, as described in the appendix, involves computing the gradient of the residual with respect to the predicted cleaned samples. However, the specific form of the residual and how it relates to the governing equations (e.g., Navier-Stokes) is not explicitly stated in the main paper. A more detailed explanation of the residual calculation and its connection to the underlying physics is needed to fully assess the effectiveness of this module.

### Questions
In Section 3, it is stated that the reverse process is started from $x_t{_{guide}}$. How do you choose t here? How do you ensure that adding noise does not wash out the necessary signal for high-fidelity output generation? 

R introduced in Algorithm 1 is central to the residual correction idea but it has not been defined properly. 

I am a bit surprised to see that the diffusion model outperforms conditional diffusion models in table 1. Several works including [2] have used conditional diffusion models for this? How is the diffusion baseline set up?

Table 1 is very hard to read with all scientific number notation (with e). I would recommend using fixed decimal points.



[2] Residual Corrective Diffusion Modeling for Km-scale Atmospheric Downscaling, Mardani et al. 2023

### Soundness
3

### Presentation
3

### Contribution
2
