# Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Learning to sample from complex unnormalized distributions over discrete domains emerged as a promising research direction with applications in statistical physics, variational inference, and combinatorial optimization. Recent work has demonstrated the potential of diffusion models in this domain. However, existing methods face limitations in memory scaling and thus the number of attainable diffusion steps since they require backpropagation through the entire generative process. To overcome these limitations we introduce two novel training methods for discrete diffusion samplers, one grounded in the policy gradient theorem and the other one leveraging Self-Normalized Neural Importance Sampling (SN-NIS). These methods yield memory-efficient training and achieve state-of-the-art results in unsupervised combinatorial optimization.
Numerous scientific applications additionally require the ability of unbiased sampling. We introduce adaptations of SN-NIS and Neural Markov Chain Monte Carlo that enable for the first time the application of discrete diffusion models to this problem. We validate our methods on Ising model benchmarks and find that they outperform popular autoregressive approaches. Our work opens new avenues for applying diffusion models to a wide range of scientific applications in discrete domains that were hitherto restricted to exact likelihood models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents improvements to existing diffusion-based methods for sampling from discrete unnormalized distributions by introducing two techniques that reduce memory requirements for training the forward and reverse KL objectives. For the reverse KL objective, the authors utilize the policy gradient theorem to lower memory costs, which typically scale linearly with the number of diffusion steps in most samplers. In addressing the forward KL objective, they reformulate the loss using importance sampling and employ Monte Carlo estimation to compute the sum over diffusion steps, thereby minimizing memory usage during backpropagation. The authors validate their methods through experiments on Ising model benchmarks.

### Strengths
* The innovative approach to computing the forward and reverse KL loss functions is the paper's main strength. Developing memory-efficient loss functions is particularly important for diffusion models.
* The paper is clearly written and all the results are well presented.

### Weaknesses
 * The innovative approach to computing the forward and reverse KL loss functions is the paper's main strength. Developing memory-efficient loss functions is particularly important for diffusion models.
* The paper is clearly written and all the results are well presented.

* The empirical validation of the proposed algorithms is insufficient to convincingly demonstrate their practical benefits. It would be more compelling if the authors included comparisons to standard diffusion-based samplers under the same computational constraints or memory budget in the Ising model experiments. The current comparisons against the AR baselines do not adequately highlight the potential advantages of the proposed methods over conventional diffusion-based samplers.

* The experiments conducted do not appear to be sufficiently challenging, and the memory requirements of standard diffusion-based samplers in these cases may not pose significant issues in practice. It would be beneficial for the authors to test their methods in more complex settings in statistical physics (e.g., the phi-4 model) or on image generation tasks (e.g., CIFAR-10).

### Questions
* I am interested in the memory usage for each set of experiments reported in the paper. Including this information would enhance the presentation. Additionally, it would be valuable to see how model performance varies with the number of diffusion steps and memory budget. Specifically, I wonder if the memory budget is genuinely a bottleneck for standard diffusion-based samplers in the experiments presented.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Scalable Discrete Diffusion Samplers (SDDS) for generating samples from complex, unnormalized distributions over discrete domains, with applications in combinatorial optimization and statistical physics. Traditional methods in this area are limited by memory scaling issues and lack of unbiased sampling capability. To address these challenges, the authors propose two new training methods for diffusion samplers: one based on policy gradient reinforcement learning (RL) for minimizing the reverse KL divergence and another using Self-Normalized Neural Importance Sampling (SN-NIS) for unbiased forward KL divergence estimation. These approaches enable more diffusion steps within fixed memory constraints and allow for unbiased sampling, which is crucial for many scientific applications. Experiments on combinatorial optimization benchmarks show that SDDS achieves state-of-the-art performance, and unbiased sampling evaluations on the Ising model demonstrate improved accuracy over traditional autoregressive models.

### Strengths
- The paper introduces two novel methods (RL-based reverse KL and SN-NIS-based forward KL) to address memory scaling issues, enabling the use of more diffusion steps while staying within fixed memory constraints.
- By extending importance sampling and Markov Chain Monte Carlo methods to diffusion models, the authors enable unbiased sampling—a critical requirement for scientific applications that require accurate expectation estimates.

### Weaknesses
 - Although the paper reports inference time alongside results, a more comprehensive analysis of computational costs is needed, particularly in terms of training time and overall efficiency. The provided inference times are insufficient to fully assess the practical applicability of the proposed methods. A detailed breakdown of training time, including wall-clock time and GPU hours, is necessary to understand the real-world resource requirements.
- The paper would benefit from a deeper theoretical exploration of the convergence properties of the proposed methods, especially the RL-based approach. Clarifying the conditions under which convergence is guaranteed would strengthen the paper's contributions. The current analysis lacks a rigorous treatment of the convergence behavior of the policy gradient method, and it is unclear how the choice of hyperparameters affects convergence.
- The experiments lack ablation studies to isolate the effects of individual components of their models. While the authors compare different training objectives, they do not systematically evaluate the impact of specific architectural choices or hyperparameter settings. For example, the effect of the mini-batch size in the PPO algorithm or the number of hidden layers in the neural network is not explored.
- The paper primarily compares the proposed methods with DiffUCO. While this comparison is relevant, it is insufficient to establish the superiority of the proposed methods. The lack of comparisons to other state-of-the-art methods limits the scope of the evaluation and makes it difficult to assess the true performance of the proposed approach.
- The presentation of the experimental results could benefit from clearer organization and more detailed explanations to improve readability and interpretability. The current presentation lacks clarity in explaining the experimental setup, and the results are not presented in a way that facilitates easy comparison across different methods and datasets.

### Questions
- How do the proposed methods affect overall computational efficiency? Specifically, does the integration of PPO in SDDS: rKL w/ RL significantly increase training time compared to standard diffusion models or autoregressive approaches?
- Why was PPO specifically chosen for optimizing the rKL-based objective?
- Can the authors provide theoretical or empirical insights into the convergence properties of the proposed methods? Specifically, under what conditions do the RL-based training procedures converge, and how stable are they across different problem instances?
- How does varying the number of diffusion steps during training and inference influence the model's performance? Is there an optimal range of steps beyond which improvements plateau or diminish?
- Why was DiffUCO the primary(or only) comparison, and have the authors considered additional benchmarks such as those in Zhang et al. (2023)? Given that MDS results might not be state-of-the-art, how would the method perform against others besides DiffUCO?

[1] Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron C. Courville, Yoshua Bengio, and Ling Pan. Let the flows tell: Solving graph combinatorial problems with gflownets. NeurIPS 2023

### Soundness
3

### Presentation
2

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
The article considers the task of learning to sample from complex unnormalized distribution for discrete variables, with application to optimization and sampling problems. The problem in this kind of task is the need to keep track of the entire diffusion trajectory, making it very demanding in memory. The authors alleviate this problem by using Importance Sampling (in one case) or Reinforcement Learning techniques in another one. More precisely, they propose two kinds of modification: first to use the forward KL (instead of the reverse one) in order to remove the problem of having to save the whole trajectory, at the cost of needed to use sampling from the target distribution (here done with importance sampling); second they reformulate the optimization problem on the reverse KL as a Reinforcement Learning problem, allowing to deal with the optimization using technique coming from RL.

### Strengths
The paper provides two different ways of solving the memory issue in the context of discrete diffusion model when using the reverse KL. 
A reasonable list of optimization's benchmarks are provided.

### Weaknesses
The benchmark of sampling on Ising is ok, but we could have expected more difficult cases. For instance, the 2D spin glass ($J= \pm 1$) might be
* a more challenging task not too different from the Ising case considered in the paper
* and for which the polynomial algorithm exists at least for the ground states.

In relation to both their work and this case, they can also refer to the following article: https://arxiv.org/pdf/2407.19483 which study using a different approach the sampling on the 2D Ising spin glass for comparison.

The reason why the whole trajectory is needed to optimize eq. 2 is not explicitly stated, but it seems to be because the gradient will be applied to the expectation value, from which all steps will be affected. This should be clarified right after eq. 2.

In 2.2, the distribution $\mathcal{D}(Q)$ is not specified. It is important to provide more details, since it seems that the goal is to use an ensemble of similar optimization problems. A reference to sec. 4 of the appendix with a detail on the distribution of Q for the different considered cases would be useful.

The difference between IS and SN-NIS is not clear. An explanation in the article would be beneficial for clarity.

Similarly, the distinction between neural MCMC and classical MCMC is not well-defined. An explanation in the article would be beneficial for clarity.

The part 2.3 is a bit misleading, as it seems to describe classical methods of sampling while it is not clear at that point where it will be used for. In fact, most of it is repeated in sec. 3.2...

Minor comment:
- eq. line 114, p should be p_B no ?

### Questions
- I guess the reason why the whole trajectory is needed to optimize eq. 2 is because the gradient will be applied to the expectation value, from which all steps will be affected. Is that correct ? if yes, it might be clearer to specify it right after eq. 2 (using main text, footnote or a reference to the supplementary materials).

- In 2.2, the distribution $\mathcal{D}(Q)$ is not specified. It might be useful to put a bit of precision, since I imagine that the goal is to use an ensemble of similar optimization problem. For instance, a reference to sec. 4 of the appendix with a detail on the distribution of Q for the different considered cases.

- What is exactly the difference between IS and SN-NIS ? it would be good for clarity to add an explanation in the article on that point.

- Same comment for neural MCMC, how is it any different from classical MCMC ? it would be good for clarity to add an explanation in the article on that point.

- The part 2.3 is a bit misleading, it seems to describe classical method of sampling while it is not even clear at that point where it will be used for. In fact, most of it is repeated in sec. 3.2...

Minor comment:
- eq. line 114, p should be p_B no ?

### Soundness
3

### Presentation
2

### Contribution
3
