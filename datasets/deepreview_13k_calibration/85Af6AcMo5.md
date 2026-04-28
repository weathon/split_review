# SciRE-Solver: Accelerating  Diffusion Models Sampling by Score-integrand Solver with Recursive Difference

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Diffusion models (DMs) have made significant progress in the fields of image, audio, and video generation. One downside of DMs is their slow iterative process. Recent algorithms for fast sampling are designed from the perspective of differential equations.
However, in higher-order algorithms based on Taylor expansion, estimating the derivative of the score function becomes intractable due to the complexity of large-scale, well-trained neural networks.
Driven by this motivation, in this work, we introduce the recursive difference (RD) method to calculate the derivative of the score function in the realm of DMs.
Based on the RD method and the truncated Taylor expansion of score-integrand, we propose \emph{SciRE-Solver} with the convergence order guarantee  for accelerating sampling  of DMs.
To further investigate the effectiveness of the RD method, we also propose a variant named \emph{SciREI-Solver} based on the RD method and exponential integrator.
Our proposed sampling algorithms with RD method attain state-of-the-art (SOTA) FIDs in comparison to existing training-free sampling algorithms, across both discrete-time and continuous-time pre-trained DMs, under various number of score function evaluations (NFE).
Remarkably, SciRE-Solver using a small NFEs demonstrates promising potential to surpass the FID achieved by some pre-trained models in their original papers using no fewer than $1000$ NFEs.
For example, we reach SOTA value of $2.40$ FID with $100$ NFE for continuous-time DM  and of $3.15$ FID with $84$ NFE for discrete-time DM on CIFAR-10, as well as of $2.17$ (2.02) FID with $18$ (50) NFE for discrete-time DM on CelebA 64$\times$64.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Recursive Difference (RD) method to calculate the derivative of the score function network. Based on the RD method and the truncated Taylor expansion of score-integrand, the authors propose SciRE-Solver to accelerate diffusion model sampling. 
The core of their algorithm relies on evaluating higher-order derivatives of the score functions, which cannot be done by conventional finite difference methods, as errors can propagate easily. The RD method is proposed to tackle this problem. They provide extensive experiments on variant benchmark datasets to demonstrate the effectiveness of their approach.

### Strengths
The authors propose a fast sampling algorithm for diffusion models based on using an RD approach to evaluate higher-order derivatives of the score function. They clearly introduce the intuiotion and the background story. Extensive experiments on various datasets are conducted to support the use of their proposed algorithm. Compared to existing algorithms, the proposed SciRE-based algorithm in many cases achieve lower FID score with a fewer number of NFEs.

### Weaknesses
I have two major concerns:

1. Their main result, the RD procedure is not presented clearly enough. This algorithm is only described in words, and Figure 2 is hard to parse. From Equation (3.7) I see that to evaluate first order derivative at $s$, we need both the first and the second order derivatives at $t$. Then why the authors say in the caption of Figure 2 that we can evaluate the first order derivative at $s$ with only zero order derivative at $t$? I would suggest present the most general form algorithm in a pseudo-code format like Algorithm 1 and 2. The current description lacks the necessary detail to fully understand the recursive process. For instance, it's unclear how the intermediate derivatives are stored and reused, and how the algorithm handles different orders of derivatives in a general setting. The description should also clarify the base case for the recursion and how the algorithm terminates.

2. This paper might contain some critical typos that affect the entire proposal (see my second question).

### Questions
1. Is there any acceleration algorithm for diffusion SDE as well? If yes, I would love to see the authors providing a discussion. If no, could the authors elaborate a bit on why training-free acceleration is mostly for diffusion ODE? 
2. I thought $\alpha_t = \prod_{i = 1}^t \beta_i$ is piecewise constant?  Then how do you define $f(t)$ as the derivative of $\log \alpha_t$ with respect to $t$? It is unclear whether the authors use $t$ as a index for discrete time step or continuous time. 
3. In Eq (3.1), $h(r)$ should be $h_1(r)$. 
4. I understand that $NSR$ is monotone, but why is it strictly monotone? Namely, how to guaratee the existence of its inverse function. 
5. Why the authors say in Figure 1 that the proposed algorithm outperforms DDIM and DPM solver? 
6. Where is $t_i$ defined? 
7. Maybe this is a dumb question. Why can we assume the neural network is differentiable? I would imagine this is not the case when the activation function is ReLU. 
8. This sentence is hard to parse. "This method recursively extracts the hidden lower-order derivative information of the higher-order derivative terms in the Taylor expansion of the score-integrand at the required point, as illustrated in Figure 2". I would suggest the authors present their most general form algorithm in the format of Algorithm 1 and 2. 
9. Could the authors elaborate on what Figure 2 is trying to illustrate? In particular, why some blocks are colored in red and the others in blue? Why do you call the first row Taylor series and the second row Weighted sum? 
10. In Theorem 3.2, $m$ has to be larger than 2 or 3? 
11. The legend in Figure 3 is a bit misleading. I assume the first four ones are for dashed lines, but it is not apparent at first glance.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a new training-free sampling algorithm for diffusion models, called SciRE-solver. SciRE-solver is based on Taylor expansion and uses the proposed Recursive Difference (RD) method to estimate the derivative of the score model. The authors conduct extensive experiments on various datasets such as CIFAR10, CelebA, ImageNet, LSUN, showing that the proposed SciRE-solver consistently outperforms existing numerical samplers.

### Strengths
1. The paper is well-written with sufficient details and comprehensive ablation studies. 
2. The paper clearly explains its relationship to and differences from the related work to be well-placed in the literature. 
3. SOTA performance compared to existing numerical sampling algorithms on various datasets and diffusion models.

### Weaknesses
1. The paragraph above Figure 2 needs revision for clarity. The score approximation error is inevitable. How can the proposed sampling method mitigate this issue? The third sentence is also vague without explaining what the "additional variables" means. It is not clear how these considerations lead to the hypothesis either. Specifically, the discussion of replacing finite difference coefficients with equivalent infinitesimals lacks sufficient detail. What specific assumptions are made when considering these replacements, and how do these assumptions affect the accuracy of the derivative estimation? The connection between these replacements and the potential limitations of finite difference methods needs to be more clearly articulated. Furthermore, the term "additional variables" should be defined precisely, and its role in the proposed method needs to be explained with concrete examples.
2. While the authors demonstrate generated samples of pre-trained DMs on high-resolution datasets such as ImageNet, LSUN-bedroom, and stable diffusion model, there is lack of quantitative results on these datasets except for ImageNet128. Can you also add quantitative results on ImageNet256 and LSUN-bedroom? The absence of quantitative metrics, such as FID scores, for these high-resolution datasets makes it difficult to assess the true performance of the proposed method. It is crucial to provide these metrics to validate the visual quality of the generated samples.
3. In Table 1, SciRE-solver uses pre-trained model from EDM. But the results of the original EDM sampler is missing from the comparison. It is important to include the performance of the original EDM sampler to provide a fair comparison and to demonstrate the specific improvements achieved by the proposed SciRE-solver. Without this baseline, it's difficult to ascertain the true effectiveness of the proposed method relative to its direct predecessor.
4. Minor: in the abstract, "Experiments demonstrate also that demonstrate that" -> "Experiments also demonstrate that".

### Questions
1. While SciRE-solver outperforms its counterpart DPM-solver in the experimental results, can you elaborate more on why it is better than DPM-solver numerically? Does SciRE-solver provide more accurate higher-order derivative estimation than DPM-solver theoretically?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a new method, the recursive difference method, to improve the speed of Diffusion models by efficiently calculating score function derivatives. Their SciRESolver technique significantly accelerates DM sampling, achieving state-of-the-art FID scores with fewer NFEs. The method demonstrates remarkable performance on tasks like text-to-image generation, requiring few NFEs for high-quality samples.

### Strengths
In diffusion models, the NFE required for sampling has always been the main computational overhead, and reducing NFEs is very important for efficiency.

### Weaknesses
The improvement is not consistent, which makes the interpretation a little challenging.

### Questions
Given the current literature, as the distillation of score-based models can reduce NFE significantly. How can your algorithm be combined with distillation?

How can you explain the behavior of SciRE-V1-2 and SciRE-V1-3 from a theoretical perspective?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work investigates accelerating diffusion model sampling. Compared with existing works, the authors propose a new gradient estimation method,  named recursive difference, and show improvement compared with existing works.

### Strengths
1. The experiments are very comprehensive for image experiments in terms of FID. 
2. Based on experiments in the main paper and appendix, the proposed new method shows improvements.

### Weaknesses
1. After reading the main paper, I have difficulties in understanding why the proposed recursive difference works better. The authors claim " This method recursively extracts the hidden lower-order derivative information of the higher-order derivative terms in the Taylor
expansion of the score-integrand at the required point, as illustrated in Figure 2." The recursive difference trick is key contribution of the work, authors should consider rewriting the above high-density sentence into an easy-to-understand paragraph and highlight why it works, presenting more analysis.

2. Can the author show some comparison in terms of numerical accuracy (MSE against ground truth solution) besides FID? How fast of various methods converge to ground truth solution?

3. After reading the main paper and appendix, it is unclear to me why the chosen coefficient C6 is better than C5. Besides the empirical experiments, do authors have more principled math analysis for them?

4. Similar to Q2, can authors present evidence that the proposed method can better estimate score gradients?

5. A recent work investigates a similar problem and shares a similar algorithm. Can authors comment on the connection and difference[1]?

### Questions
See above

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
