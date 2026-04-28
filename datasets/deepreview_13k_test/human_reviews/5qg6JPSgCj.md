# Score-based free-form architectures for high-dimensional Fokker-Planck equations

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Deep learning methods, which incorporate the PDE residual as loss function, have recently emerged to solve Fokker-Planck equations. Without reference solutions, proper normalization condition is required to avoid a trivial solution. However, soft constraints require careful balancing of multi-objective loss function, and specific network architectures may limit representation capacity. In this paper, we propose a novel framework: Fokker-Planck neural network (FPNN) that adopts a score PDE loss to decouple the score learning and the density normalization into two stages. Our method is mesh-free and causality-free, allowing for free-form network architectures to model the unnormalized density and strictly satisfy normalization constraints by post-processing. We demonstrate the effectiveness on various high-dimensional steady-state Fokker-Planck (SFP) equations, achieving superior accuracy and over a 20$\times$ speedup compared to state-of-the-art methods. Without any labeled data, FPNNs achieve the mean absolute percentage error (MAPE) of 11.36\%, 13.87\% and 12.72\% for 4D Ring, 6D Unimodal and 6D Multi-modal problems respectively, requiring only 256, 980, and 980 parameters. Experimental results highlights the potential as a universal fast solver for handling more than 20-dimensional SFP equations, with great gains in efficiency, accuracy, memory and computational resource usage.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors focus on steady state Fokker-Planck (SFP) equations and propose novel score-based PDE loss. The proposed loss does only depend on the score function $s_\theta$, avoiding the necessity to compute the normalization constant of the probability distribution. Furthermore, the authors propose to investigate the proposed loss on two types of architectures, namely tensor neural networks (TNNs) and MLPs. Experiments on several PDE examples are performed, showing the good performance of the proposed method.

### Strengths
1. The paper is overall well written and easy to follow.
2. Experimental results are interesting and support the authors' claims.

### Weaknesses
1. There is a potential clash with the notion of score in the ML/DL community, see questions.
2. It is difficult to evaluate the novelty of the work. For example, authors only compare the proposed approach to TFFN but no other baselines are provided. I would strongly suggest that the authors add more baselines to allow for an easier comparison with existing approaches, e.g. [1,3].
3. Similarly, it is not clear whether the set of chosen experiments are commonly used in the  PINN community. For example, is the dataset of the authors present in [2]?

(see refs in questions)

### Questions
**Main comments**
1. I am afraid that the notion of "score" that is central to the paper is fairly different to the one usually referred to in deep learning, where the score is implicitly learned through denoising and the associated distribution is never explicitely computed. Here, the authors rather use a differentiable network and use this property within the loss. Can the authors comment on that?
2. Why is the computation of $Z_\theta$ important in the context of Fokker-Planck (FP)? If I understand well, the authors parametrize FP with a neural network, with a direct access to both $\nabla \log p$ and $p$. Is the summation approach of (8) and (10) tractable as dimension increase?
3. I struggle to understand the point of the authors lines 453-473. Firstly, the notation $|D_{norm}|$ is slightly confusing. Secondly, what is the source of randomness in $D_{norm}$  mentionned by the authors line 465 ? If the dataset for $\mathcal{D}_{norm}$ is simulated, could the authors generate more samples?
4. Fig. 9 is slightly unclear. The plots on top and bottom show two different things (top: MAP and MAPE, bottom: MAPE and Z) for two different architectures. In particular, why should Z and the MAPE be related? Could the authors comment on that?

**Minor comments**
1. While the paper is well written, some typos are remaining, e.g. "Score-based generate model" (line 129)
2. The color scheme from Fig. 4 (c) (bottom) is not clear, it seems most of the maps are identically 0. The authors may want to reduce the threshold.
3. The message would be more striking in Fig. 5 and 6 if experiment was run multiple time with different random seeds. This would allow the authors to provide smoother curves with mean and error bars. 


**References**

[1]
@inproceedings{zhai2022deep,
  title={A deep learning method for solving Fokker-Planck equations},
  author={Zhai, Jiayu and Dobson, Matthew and Li, Yao},
  booktitle={Mathematical and scientific machine learning},
  pages={568--597},
  year={2022},
  organization={PMLR}
}

[2]
@article{lu2021deepxde,
  author  = {Lu, Lu and Meng, Xuhui and Mao, Zhiping and Karniadakis, George Em},
  title   = {{DeepXDE}: A deep learning library for solving differential equations},
  journal = {SIAM Review},
  volume  = {63},
  number  = {1},
  pages   = {208-228},
  year    = {2021},
  doi     = {10.1137/19M1274067}
}


[3]
@article{cho2024separable,
  title={Separable physics-informed neural networks},
  author={Cho, Junwoo and Nam, Seungtae and Yang, Hyunmo and Yun, Seok-Bae and Hong, Youngjoon and Park, Eunbyung},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}

### Soundness
2

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
3

### Summary
This paper introduces the Fokker-Planck Neural Network (FPNN), a novel framework for solving high-dimensional steady-state Fokker-Planck (SFP) equations. Traditional deep learning approaches to these equations face challenges with representation capacity, loss function balancing, and maintaining normalization constraints. The proposed FPNN addresses these issues by decoupling score learning from density normalization, using a score PDE loss that enables strict adherence to normalization constraints while allowing flexible, mesh-free architectures. FPNN achieves significant computational efficiency, with over a 20x speedup compared to state-of-the-art methods, and requires only minimal parameters for high accuracy. The authors demonstrate its effectiveness on 4D, 6D, and even 20D problems, achieving low relative errors without labeled data. The FPNN framework contributes a fast, efficient, and accurate solution method for high-dimensional Fokker-Planck equations, with applications in computational physics and related fields.

### Strengths
The paper presents a novel Fokker-Planck Neural Network (FPNN) that innovatively decouples score learning and density normalization for high-dimensional steady-state Fokker-Planck (SFP) equations. Traditional deep learning methods for Fokker-Planck equations generally incorporate the PDE residual as part of the loss function but often encounter issues with representation capacity, balancing multi-objective loss functions, and satisfying normalization constraints. FPNN addresses these challenges by using a score PDE loss, which separates score learning from normalization, allowing for a flexible, mesh-free network architecture. This approach is original as it removes the dependency on specific architectures, enables strict normalization through a single computation of the partition function, and offers substantial computational gains over existing methods. By rethinking how neural networks approach Fokker-Planck equations, the authors introduce a framework that improves upon limitations of previous methods, potentially broadening the scope of high-dimensional PDE applications in machine learning.

### Weaknesses
1. Limited Discussion on Practical Constraints and Limitations
2. Lack of Scalability and Computational Complexity Analysis
3. Lack of Comparison with Other Recent Advances

### Questions
1. Could be the proposed method widely used for other PDEs?
2. Please compare with recent developed methods.

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
2

### Summary
The paper introduces the Fokker-Planck Neural Network (FPNN) framework, a novel approach to solving high-dimensional steady-state Fokker-Planck equations by leveraging a score-based PDE loss that decouples density normalization from score learning. This decoupling allows FPNN to avoid continuous computation of the partition function, enhancing computational efficiency and stability, particularly for complex high-dimensional problems. Experimental results demonstrate FPNN’s superior performance over existing methods, achieving high accuracy and significant speedups, making it a promising candidate for scalable and efficient solutions to Fokker-Planck equations.

### Strengths
(1) This paper proposes a novel network for solving high-dimensional steady-state Fokker-Planck equations. By utilizing a score-based PDE loss that decouples score learning from density normalization, the network achieves an effective balance between representational capacity and the constraints required for accurate solutions.

(2) The performance results are promising, though further validation is needed to strengthen the findings.

(3) The presentation of this paper is good.

### Weaknesses
(1) In this paper, using SRK as part of the data generation process for steady-state Fokker-Planck equations is effective, but it might lead to an "unfair advantage" in comparisons if other baseline methods do not leverage a similar approach for handling randomness or approximating steady states. Thus, it will be meaningful to test the performance of the proposed method with the same training data as proposed in TFFN paper.

(2) Score-based methods have shown strong performance for in-distribution problems, but they often suffer from significantly reduced effectiveness on out-of-distribution (OOD) tasks. I am curious whether the authors evaluated the OOD performance for this model. Additionally, as mentioned previously, I wonder if the data generation approach used in this study simplified the distribution, making it easier for the network to learn. If that is the case, the improvements might be attributed more to the engineering aspects of data preparation rather than advancements in the network architecture itself.

(3) Additional comparisons would strengthen this paper. Although FPNN outperforms TFFN in the results presented, I could not find any published reference for TFFN, suggesting it may only be available on arXiv and has not yet undergone peer review. To more convincingly demonstrate the effectiveness of the proposed method, I recommend that the authors include additional, widely recognized baseline methods. This would provide a more comprehensive evaluation of FPNN’s efficiency and robustness.

### Questions
The questions are addressed in the weaknesses section. Although this research is not fully aligned with my area of expertise, I will follow the rebuttal process and hope that my suggestions help improve the clarity and presentation of the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper intends to solve high-dimensional Fokker-Planck equations which faces several challenges including curse of dimension, normalization constraint, etc. The solution proposed is to train neural network with a score-matching loss which bypasses normalization constraint by computing normalization constant as post-process. The method belongs to supervised learning, where training data is generated by stochastic Runge-Kutta method. The result seems effective and surpasses baseline model in accuracy.

### Strengths
**Originality** The score-based loss is novel and seemly interesting. Given the close connection between Fokker-Planck (FP) equations and diffusion process and the noticeable succuss of diffusion model with score-matching loss, it is worthy trying to solve FP with score-based loss.

**Clarity** I find the paper very clear to read and well organized.

### Weaknesses
At the first glance, it is a seemly natural and attractive idea to solve Fokker-Planck (FP) equations with the proposed score-matching loss, especially considering the success in training diffusion models and the close connection between stochastic process and FP equations. However, after more careful thoughts I find it hard to reason through the following questions:

1. If the proposed method needs a postprocess of calculating normalizing constant, why not treating PINN with the same postprocess? One of the major motivations of the paper is to deal with normalization condition (NC), which the authors criticized PINN being hard to satisfy with soft constraints. However, if PINN is obtained without NC and is normalized with the same quadrature technique afterwards, this motivation is weakened.

2. The score-based FP loss (equation (6)) is derived for static FP equations. What is the difficulty with non-stationary FP? It seems to me the residual loss can be transformed similarly and just one more term is needed in equation (15), which is $\partial_t \log p_{\theta}(x)$. Even if we only consider SFP, it is clear now that score-based FP loss is essentially equivalent to residual loss of PINN. Therefore, I wonder what benefit score-based FP loss can introduce? 

Based on these questions, I suggest the authors do an ablation study of replacing score-based FP loss with PINN loss (residual loss) without normalization constraint. Otherwise, the improvement of FPNN over TFFN may be purely due to removing normalization constraint from loss function.

### Questions
See weaknesses above. Also, when using MAPE for metric, how do you calculate $p(x)$ for test dataset?

### Soundness
3

### Presentation
3

### Contribution
3
