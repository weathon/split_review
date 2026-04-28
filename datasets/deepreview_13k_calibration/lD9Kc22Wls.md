# Quantized Optimistic Dual Averaging with Adaptive Layer-wise Compression

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
We develop a general layer-wise and adaptive compression framework with applications to solving variational inequality problems (VI) in a large-scale and distributed setting where multiple nodes have access to local stochastic dual vectors. This framework encompasses a broad range of applications, spanning from distributed optimization to games. We establish tight error bounds and code-length bounds for adaptive layer-wise quantization that generalize  previous bounds for global quantization. We also propose Quantized and Generalized Optimistic Dual Averaging (QODA) with adaptive learning rates, which achieves optimal rate of convergence for distributed monotone VIs. We empirically show that the adaptive layer-wise compression achieves up to a 150% speedup in end-to-end training time for training Wasserstein GAN on 12+ GPUs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
## Update

After some discussion with the authors, I am increasing my score as they clarified the novelty of their quantization scheme compared to the prior literature. I remain convinced that the studied setting is still somewhat niche and the empirical results are very limited.

---


This paper develops a theoretical framework for adaptive layer-wise compression in distributed variational inequality (VI) problems, along with a novel algorithm called Quantized Optimistic Dual Averaging (QODA). The work makes several key contributions:
1. It establishes a rigorous theoretical framework for layer-wise and adaptive quantization schemes that accounts for heterogeneity across layers, providing variance and code-length bounds that generalize previous bounds for global quantization.
2. It introduces QODA, which uses optimistic updated with adaptive learning rates. The algorithm achieves optimal convergence rates of $O(1/\sqrt{T})$ and $O(1/T)$ under absolute and relative noise models respectively, without requiring the common assumption of almost sure boundedness of stochastic dual vectors. The provided theory shows how convergence rates depend on the gradient compression constant.
3. The authors also test QODA in training Wasserstein GAN on distributed systems with 4/8/12/16 GPUs.

The work builds upon the combination of Markov et al. (2022, 2024) and Ramezani-Kebrya et al., (2023). The former presented compression schemes and their empirical evaluations, while the latter had theory for distributed VI problems.

### Strengths
1. Distributed training remains a challenge and good methods that compress gradients are desired to make it faster.
2. Relaxation of common boundedness assumptions while maintaining optimal convergence rates.

### Weaknesses
This paper presents two contributions. The first one is to study the compression schemes previously proposed and studied empirically.
1. It appears to me that the theoretical study is very similar to the well-known bounds of Alistarh et al. (2017), and while the notation is heavy, the underlying math is quite simple. I'm also not confident how important the studied compressions techniques are as they have not been around for a long time and do not seem to be popular in practice, for instance, the github repo of L-Greco has 12 stars.
2. The algorithmic contribution of QODA is marginal. It is a method based on the combination of two widely studied techniques: gradient/operator compression and optimism. Since the compression operator is unbiased, it seems very straightforward to derive the convergence guarantees. The adaptive learning rates have been used in the prior literature on VI problems too.
3. The experimental evaluation is a bit limited and serves more as a proof of concept. However, the work appears to be mostly theoretical, so I wouldn't put too much emphasis on this.

### Questions
1. The authors refer to Q-GenX as "SoTA". Can you clarify in what sense it is state of the art? What exactly makes it worthy improving upon? Is there evidence the method is widely used in practice?
2. The authors study a general family of compressors using arbitrary $\ell_q$ norms. Should we expect a specific choice to always perform better in practice?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a theoretical framework for layer-wise and adaptive unbiased quantization with novel fine-grained coding protocol analysis, which is the first to incorporate distributed VI with adaptive learning rate and layer-wise quantization. They obtain acceptable convergence results under standard noises without the almost sure boundness.

### Strengths
1. The theoretical analysis of compression bounds and convergence complexity propose a new framework for understanding distributed VI with layer-wise quantization, illustrating that distributed VI with layer-wise quantization can obtain standard $\Omega(d)$ variance and $\mathcal{O}(1/ \sqrt{T})$ or $\mathcal{O}(1/T)$ convergence rate.
2. The theoretical analysis achieve same rate with more relaxed assumptions compared with SOTA algorithm.

### Weaknesses
1. This paper needs more clarification on the importance on the problem they study. In other words, why $\textbf{layer-wise}$ quantization is important in distributed VI? Even though the author introduces the heterogeneity observed by other work, this paper is also lack of enough examples and evidences to explain why this setting makes sense. In large-scale models (more than 1b parameters), especially beyond Transformer-XL or ResNet mentioned in [1], the effect of layer-wise quantization seems not obvious.  
2. Even though this paper proposes the compression bounds and convergence rates, it is lack of the theoretical analysis of total communication complexity, which is the per-iteration communication cost multiplies the communication rounds. Noticing that the convergence rate includes $\epsilon_Q$ which is $\Omega(d)$, I think the total communciation complexity is the same order of the algorithm without quiantization, which means no improvement in theory.
3. The writing of  this paper need improvement. This paper is lack of motivation and has too much notations and definitions (like encoding techniques) in main body, and the main theorem needs more remarks. Some typo needs to be modified like a superfluous "literature" in line 60.

### Questions
1. In this paper, the author considers the unbiased quatization in VI. However, in distributed optimization error feedback technique is widely used to reduce the information loss when encoding. I am interested in whether error feedback and corresponding biased quantization can be  applied to distributed VI and obtain faster rate?
2. The whole framework is still worthy, especially loosing the assumption. If author could explain my concerns in weakness and questions, I would like to improve my scores.

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
The authors develop a general layer-wise and adaptive compression framework with applications to solving variational inequality problems (VI) in a large-scale and distributed setting. This paper also propose a specific algorithm called Quantized and Generalized Optimistic Dual Averaging (QODA) with adaptive learning rates. The best convergence rate is achieved under the monotonicity assumption. Finally, the authors demenstrate the superiority of the QODA algorithm in training time through experiments.

### Strengths
1.This work is the first to incorporate optimism in solving distributed VI with adaptive learning rates and layer-wise quantization. The authors propose QODA algorithm and establish joint convergence and communication guarantees for it.

2.The authors provide a very detailed and solid theoretical proof.

3.The experimen show that QODA with layer-wise compression significantly improves the convergence and training time compared to both the SoTA Q-GenX and the full precision baseline.

### Weaknesses
I have tried my best to understand the authors' contributions in this paper, but I am not very familiar with the authors' research field. I can only give the authors some suggestions from the perspective of writing.

1.Line 116, "our work is the first work", deleting the second work.

2.Line 119, missing comma at the end of sentence.

3.Line 166, "such that each node retains only local copy of the current parameter vector" -> "such that each node retains only a local copy of the current parameter vector".

4.Line 179, "We first outline the general formulation for the layer-wise and unbiased quantization." -> "We first outline the general formulation for layer-wise and unbiased quantization.".

5.Line 344, "The proof is in Appendix C." -> "The proof is provided in Appendix C.".

6.Line 365, "The proofs are in Appendix D.2 and D.3, respectively." -> "The proofs are provided in Appendix D.2 and D.3, respectively.".

7.Line 385, "...... are updated with learning rate schedule in (6) for all t=......" -> "...... are updated with the learning rate schedule given in (6) for all t=......".

8.Line 456~Line 460, the tense is different.

### Questions
I am not an expert in this field, I can only give some advice on writing papers：

1.Line 116, "our work is the first work", deleting the second work.

2.Line 119, missing comma at the end of sentence.

3.Line 166, "such that each node retains only local copy of the current parameter vector" -> "such that each node retains only a local copy of the current parameter vector".

4.Line 179, "We first outline the general formulation for the layer-wise and unbiased quantization." -> "We first outline the general formulation for layer-wise and unbiased quantization.".

5.Line 344, "The proof is in Appendix C." -> "The proof is provided in Appendix C.".

6.Line 365, "The proofs are in Appendix D.2 and D.3, respectively." -> "The proofs are provided in Appendix D.2 and D.3, respectively.".

7.Line 385, "...... are updated with learning rate schedule in (6) for all t=......" -> "...... are updated with the learning rate schedule given in (6) for all t=......".

8.Line 456~Line 460, the tense is different.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper develops a general layer-wise compression framework to solve variational inequalities in a large scale distributed setting. Convergence guarantee for the proposed QODA algorithm with adaptive learning rates is provided. Empirical evidences supporting the claims of the paper are also provided.

### Strengths
1. The paper provides theories and guarantees for layer-wise adaptive compression schemes, including tight-variance and code length bounds. The proposed algorithm combines optimism with adaptive layer-wise quantization, achieving state of the art performance.

2. Numerical evidences are provided in support of the effectiveness of the proposed algorithm, with improved in convergence performance.

3. The assumptions used in the paper are less restrictive compared to other existing work.

### Weaknesses
1. How do we select between protocal 1 and 2 in real scenario? Is there a clear guideline we can rely on?

2. Will the proposed mechanism impact on the stability of training especially in GANs, are there any experimental evidence? 

3. The layer-wised scheme in the paper refers to using different hyper-parameters for compression happens at each layer. Given the importance determined by existing information of each layer, is it possible to develop a compressor, that selects certain layers at some probabilities while temporarily ignores the other layers in this iteration? Previous studies suggests that this leads to benefits in solving empirical risk minimization problem, see [1].

4. The experiments focus on a relatively narrow range of applications (WGAN training), it could benefits from further validation on other models if possible.

### Questions
1. How do we select between protocal 1 and 2 in real scenario? Is there a clear guideline we can rely on?

2. Will the proposed mechanism impact on the stability of training especially in GANs, are there any experimental evidence? 

3. The layer-wised scheme in the paper refers to using different hyper-parameters for compression happens at each layer. Given the importance determined by existing information of each layer, is it possible to develop a compressor, that selects certain layers at some probabilities while temporarily ignores the other layers in this iteration? Previous studies suggests that this leads to benefits in solving empirical risk minimization problem, see [1].

4. The experiments focus on a relatively narrow range of applications (WGAN training), it could benefits from further validation on other models if possible.

### Soundness
3

### Presentation
3

### Contribution
3
