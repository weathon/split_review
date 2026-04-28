# Neural Diffusion Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Diffusion models have shown remarkable performance on many generative tasks. Despite recent success, most diffusion models are restricted in that they only allow linear transformation of the data distribution. In contrast, broader family of transformations can potentially help train generative distributions more efficiently, simplifying the reverse process and closing the gap between the true negative log-likelihood and the variational approximation. In this paper, we present Neural Diffusion Models (NDMs), a generalization of conventional diffusion models that enables defining and learning time-dependent non-linear transformations of data. We show how to optimise NDMs using a variational bound in a simulation-free setting. Moreover, we derive a time-continuous formulation of NDMs, which allows fast and reliable inference using off-the-shelf numerical ODE and SDE solvers. Finally, we demonstrate the utility of NDMs with learnable transformations through experiments on standard image generation benchmarks, including CIFAR-10, downsampled versions of ImageNet and CelebA-HQ. NDMs outperform conventional diffusion models in terms of likelihood and produce high-quality samples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Diffusion models traditionally use only linear transformations, however using a broader family of transformations can potentially help train generative distributions more efficiently. This work presents Neural diffusion models that generalize existing diffusion models by adding learnable transformation of data which are parameterized with a neural network. The corresponding forward and reverse process are derived by modifying DDPM forward and reverse process. The variational loss objective has been generalized to include learnable transformations. NDM can also be extended to continuous time diffusion models based on previous work by Song et al. 2020. Many previously proposed diffusion models are instances of NDM. Overall, NDM shows gains in NLL and negative ELBO over DDPM.

### Strengths
- The idea of generalizing diffusion models to learnable non-linear transformations is interesting.
- Many previously proposed diffusion models and flow models are special cases of NDMs with specific choice of transformation.
- The qualitative results of learned transformations for different datasets in Figure 2 are interesting.
- NDM provides consistent gains in terms of NLL and NELBO over DDPM (See Table 4 and 7).

### Weaknesses
 - One of the primary motivations for learnable transformations is that it simplifies the data distribution and therefore leads to predictions of x that are more aligned with data. Ideally, if transformations indeed helped with simplification of data distribution, one should have observed better quantitive metrics in fewer sampling steps. However, the actual gains in quantitative metrics like NLL and NELBO seem marginal. Further, there seems to be no consistent gains in terms of FID. In addition, as listed in limitations, the model uses 2.3$\times$ more training time than DDPM (which by itself is slow and needs hundreds of thousands of steps to get good FID). Therefore, I am not sure if the minor gains in NLL and NELBO can be justified when compared to 2.3$\times$ increase in training time as well as $\sim 2\times$ increase in model size.
- Benefits of learnable transformations hasn’t been explored much in the paper and as a result its benefits remain unclear. There is a toy experiment on training optimal transport on 1D data in the appendix. However, larger scale experiments on real data would make this work much stronger. Overall, I feel that NDMs are well-motivated but it remains unclear from the experimental results that introducing learnable transformations as a standard practice for training diffusion models is beneficial.

### Questions
- After going through the implementation details (Section 4.1, Appendix C),  the architectural details of neural network used to model the transformation $F_\psi$  remains unclear to me. Could the authors further elaborate on these details? 
- Table 4 compares DDPM and NDM. However, NDM has non-Markovian forward and reverse process and for a fair comparison, results for DDIM should also be included, especially in the cases when the number of sampling steps is smaller than the number of training steps.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes neural diffusion models, or NDMs, extending conventional diffusion models to using learnable non-linear transformation. An objective function is developed within this framework to optimize NDMs, providing an upper bound for the negative log-likelihood.  Empirical studies showcase NDMs' ability to consistently enhance log-likelihood while improving generation quality for scenarios involving a small to medium number of steps.

### Strengths
- The background and techniques of NDMs are clearly described. 
- The visualization of the transformed data is insightful and pretty helpful in understanding the benefits of NDMs.

### Weaknesses
 - It seems that the technical details are similar to the conventional DMs. So, what are the technical challenges and novelties here?

- In my opinion, the argument "a key limitation of most existing diffusion models is that they rely on a fixed and pre-specified forward process that is unable to adapt to the specific task or data at hand" is not convincing enough. The extensive empirical studies in the community reflect that conventional DMs have enough flexibility to accommodate diverse data. So, more clearly, I want the authors to clarify what practical consequences would the conventional "inflexible" modeling lead to. On the other hand, conventional modeling bears great simplicity, where the denoising process is training-free. Compared to that, NDMs may rely on more complicated training. 

- As mentioned in the paper, the prior term and the reconstruction term should also be trained. What are the weights of these objectives in the entire training objective?

- More clarifications should be put on the training cost and stability of NDMs, compared to vanilla DMs. 

- Is there an experiment on a larger dataset using a larger model? Are there technical challenges to achieving this?

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Neural Diffusion Models, which parameterize the forward diffusion process with a neural network. By training the neural network with the x-prediction network together, the authors yield new generative models that are better than naive diffusion models in terms of likelihood estimation and few-step generation.

### Strengths
1. The idea of using parameterized marginal distribution makes a lot of sense, since we have no idea which configuration of the marginal distributions is the best and most of them are handcrafted.

2.The empirical performance successfully demonstrates the effectiveness of the proposed method in likelihood estimation.

### Weaknesses
1. The presentation of the paper should be polished. The learning and sampling algorithm is difficult to find. I suggest the authors shorten/defer the discussion section to Appendix and add algorithm boxes in the main text. Moreover, I have several questions on the training process: (1) Are $\phi$ and $\theta$ jointly trained or alternatively trained? (2) How are the hyper-parameters of $F_\phi$ set? Are they similar to the x-prediction network?

2. Certain constraints of $F_\phi(x_t, t)$ should be satisfied. For example, when $t=0$, I think it must satisfy $F_\phi(x_0, 0) = x_0$. I wonder how the authors ensure that.

3. The proposed method brings additional computation overhead in the inference time when simulating Eq. (12) and Eq. (13). Because $F_\phi$ is a neural network and the authors use the same U-Net for both $F_\phi$ and $\hat{x}$ , it at least doubles the computation. Visually, Figure 2 shows that $F_\phi$ actually gives very close prediction to the real data $x$. I guess maybe simply double the size of the original $\hat{x}_\theta$ can get the similar results as NDM.

4. Ablation studies are missing. At least the influence of (1) the various choices of $\alpha_t$ and $\sigma_t$, and (2) the various choices of the network structure and number of parameters of $F_\phi$  should be investigated to verify that NDM brings consistent improvement. 

5. Relationship to learnable interpolation in [1] should be discussed in more detail, although I notice there are several sentences in the related works. The two methods are actually very close to each other (I think the only difference is the objective).

### Questions
Please refer to Weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Neural Diffusion Models (NDMs) as an extension of traditional diffusion models. While conventional diffusion models are limited to linear data transformations, NDMs allow for time-dependent non-linear transformations, potentially improving generative distribution training efficiency. The authors propose a variational bound for optimizing NDMs in a simulation-free setting and develop a time-continuous formulation for efficient inference. Experimental results on image generation benchmarks, such as CIFAR-10, downsized ImageNet, and CelebA-HQ, demonstrate that NDM is able to do generative tasks.

### Strengths
The paper introduces NDM as a framework that extends conventional diffusion models to both discrete and continuous time settings. The upper bound of the negative log-likelihood objective is provided. The authors claim that the generation quality is improved with small to medium steps in terms of log-likelihood. The approach is interesting, even though the idea of using a nonlinear forward process is not novel.

### Weaknesses
1. There are a few other learnable forward process which generalizes the diffusion model [1,2]. The authors should consider citing or comparing with them.

2. Actually I am not quite convincing by the effectiveness of proposed method. The numerical value is compared with the DDPM. The authors clearly present the differences with DDIM in Figure 1, but the experiment section is just focus on DDPM for fast sampling. The numerical value provided by authors is not impressive or competitive compared with the other fast sampling techniques on the market which is built on DDPM/DDIM [3,4]. The FID score for CIFAR-10 using DDPM with 1000 steps is reported as 11.44, which is significantly higher than the existing literature which reports FID scores around 3.x. This discrepancy raises concerns about the baseline implementation and the overall effectiveness of the proposed method.

[1]:Dongjun Kim et al. 'Maximum Likelihood Training of Implicit Nonlinear Diffusion Models.'

[2]: Tianrong Chan et al. 'Likelihood Training of Schrödinger Bridge using Forward-Backward SDEs Theory.'

[3]: Qinsheng Zhang et al. 'Fast Sampling of Diffusion Models with Exponential Integrator'

[4]: Fan Bao et al. 'Analytic-DPM'

### Questions
1. What is the difference between the NDM compared with [1,2]? What is the benefits over them?
2. In the experiment section, 'DDPM' represents for the SDE/stochastic model? If it is, it would be great to have the comparison for ODE model which is more favorable for fast sampling for both NDM and DDIM.
3. How do the authors obtain the $\hat{x}_{\theta}$ in eq.10? Does it include the inference of the network? If yes, then why the algorithm is simulation-free? From my understanding, it is implicitly simulating the dynamics which is also the part of reason for heavy training complexity as stated by the authors.

[1]:Dongjun Kim et al. 'Maximum Likelihood Training of Implicit Nonlinear Diffusion Models.'

[2]: Tianrong Chan et al. 'Likelihood Training of Schrödinger Bridge using Forward-Backward SDEs Theory.'

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
