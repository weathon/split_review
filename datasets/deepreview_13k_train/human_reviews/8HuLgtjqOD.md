# SEPARATE: A Simple Low-rank Projection for Gradient Compression in Modern Large-scale Model Training Process

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Training Large Language Models (LLMs) presents a significant communication bottleneck, predominantly due to the growing scale of the gradient to communicate across multi-device clusters. However, how to mitigate communication overhead in practice remains a formidable challenge due to the weakness of the methodology of the existing compression methods, especially the neglect of the characteristics of the gradient. In this paper, we consider and demonstrate the low-rank properties of gradient and Hessian observed in LLMs training dynamic, and take advantage of such natural properties to design SEPARATE, a simple low-rank projection for gradient compression in modern large-scale model training processes. SEPARATE realizes dimensional reduction by common random Gaussian variables and an improved moving average error-feedback technique. We theoretically demonstrate that SEPARATE-based optimizers maintain the original convergence rate for SGD and Adam-Type optimizers for general non-convex objectives. Experimental results show that SEPARATE accelerates training speed by up to 2× for GPT-2-Medium pre-training, and improves performance on various benchmarks for LLAMA2-7B fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes an efficient way to communicate gradients between nodes for training large models. The method works by communicating random projections of the gradients, where the projections have zero mean and identity covariance. The projections can be regenerated from the random seed, so a shared random number generator between nodes is assumed. Thus, since the projections $P$ have identity covariance, an unbiased estimate of the original gradient $g$ can be found by noting $\mathbb{E}[gPP^\top]=g$. The authors further improve this method by incorporating an error-feedback mechanism that works like momentum. They derive an Adam variant of this method and show that it is effective in practice. They also provide convergence analysis of this method on non-convex objectives.

### Strengths
- Using the random seed for reconstructing the random projections is a smart trick for efficient communication and saving space.
- This method has the benefit of being an unbiased estimator of the true gradient, which is not the case with low-bit and some low-rank methods. Even though the variance might be bad (i.e., worse than the distance between the true gradient and its truncated SVD), error feedback (with restarts) seems to mitigate this issue during training, allowing SEPARATE to be stable and perform better than low-rank projection methods, such as PowerSGD. This implies that old gradient directions can still be relevant even after many iterations.
- The authors additionally show an Adam variant of SEPARATE and derive the convergence rate of both the normal variant and the Adam variant. 
- The low-rankedness in LLMs have been (empirically) demonstrated before, but the authors here show a theoretical analysis of this phenomenon in the appendix.

### Weaknesses
 - Sharing random generator between nodes might introduce a layer of complexity that could potentially make debugging difficult when things go wrong. For example, this might prevent a real-life implementation to use non-deterministic approaches for accelerating training. Elaborating on this part would be great. For example, the authors can emphasize that this is not a problem and discuss how to ensure a proper regeneration of the random variable across nodes.
- This trick for getting an unbiased estimator from a sketch matrix M is actually not new as far as I'm concerned. The authors did not claim its novelty, but I just wanted to mention this since they did not cite relevant works to this trick. For example, the Hutchinson estimator does a very similar thing to calculate the trace (or diagonal) of the Hessian. Citing this estimator can help future readers to look for relevant tricks in the literature.
- Table 1: the authors should explain what "performance" mean here, at least in the main text. I also do not think the use of average performance across datasets is sound. Perhaps the average rank or quantile per dataset is a better aggregated metric.
- Regarding regularization by projection, an elaboration of the claim in line 407 would be great. If the authors believe that some sort of regularization is happening, then it would be great to provide some experiments or analysis to corroborate this hypothesis, which would be interesting to see. Otherwise, this might feel like a handwavy explanation of the results.
- The discussion regarding the hessian spectrum is already known and have been demonstrated in quite a few works, e.g. [1], which the authors duly noted, but I'm mentioning to emphasize that this is a motivation rather than a novel discovery. This also applies to studies regarding low-rank properties in LLMs. Thus, the originality of the contribution comes from applying random low-rank projections with an error-feedback mechanism along with the analysis in the appendix. Perhaps stating this clearly in the contributions section can help understand this work better.
- Some explanations are provided without support, such as line 458: “When the random projection directions are far from the dominant directions of Hessian in several continuous iterations, the variance of error will become extremely large and misguide the next iteration.” It is easy to see how this holds intuitively, but it might not necessarily be the case that error feedback mitigates this phenomenon, or that this phenomenon occurs in the first place in practice. For example, SEPARATE1 in Table 2 seems to be working fine.
- I don't see how the Ablation study in Table 2 is conclusive. It would be better to provide the average + std for a few seeds, say 5. That would make it clearer whether the difference is significant or not.

### Questions
None.

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
2

### Summary
This paper introduces SEPARATE, a gradient compression technique designed to address communication bottlenecks in large-scale model training. SEPARATE leverages low-rank properties observed in the gradients and Hessians of large language models (LLMs), compressing gradients using random Gaussian projections. The method also includes an error-feedback mechanism to counteract compression-induced errors by averaging historical errors over time, which aims to stabilize training dynamics. Experimental results on models such as GPT-2 and LLAMA2 demonstrate SEPARATE’s potential for up to 2x speedup compared to baselines while maintaining similar accuracy across several downstream tasks.

### Strengths
SEPARATE introduces an innovative error-feedback mechanism that effectively addresses the inherent variability associated with random projections by smoothing out compression errors, leading to more stable gradient updates and robust training dynamics. To support its effectiveness, the authors provide a thorough theoretical analysis demonstrating that SEPARATE maintains the convergence rates for non-convex objectives across both SGD and Adam-type optimizers, ensuring that the compression process does not compromise the underlying optimization goals. Additionally, SEPARATE is designed as a flexible, plug-in module that operates independently of specific optimizers or model architectures, making it a versatile tool that can be seamlessly integrated into existing training frameworks. This adaptability simplifies its deployment in diverse training setups, enhancing its practical utility for large-scale distributed model training environments.

### Weaknesses
The random Gaussian projection approach employed by SEPARATE, though theoretically sound, introduces variance that is only partially mitigated by its error-feedback mechanism. This variance arises from SEPARATE’s use of fixed Gaussian random matrices in each round, which can sometimes yield suboptimal projections that distort the gradients, affecting convergence stability. The variance analysis indicates that stable convergence relies heavily on precise tuning of the error reset frequency and compression ratio, which compromises SEPARATE’s robustness, particularly in scenarios with limited tuning flexibility due to computational constraints. Moreover, while SEPARATE offers flexibility with varying compression ratios, it lacks a mechanism for dynamically adjusting the compression ratio based on factors like gradient sparsity or model variance. This limitation restricts SEPARATE’s adaptability to evolving model sizes or training dynamics, which may lead to suboptimal performance in cases where manual tuning is impractical. Additionally, the experimental results shown in Table 1 do not provide strong evidence of competitive performance.

### Questions
Can SEPARATE generalize to architectures without low-rank gradient properties? 
Could a more adaptive error-feedback mechanism improve stability? 
Could SEPARATE benefit from dynamically adjustable compression ratios?

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
3

### Summary
The paper proposes a gradient compression technique called SEPARATE that aims to reduce communication overhead  across multi-device clusters in LLM training. SEPARATE leverages the natural low-rank properties of gradient and Hessian matrices by projecting gradients onto a low-dimensional subspace using common Gaussian random matrices. The accumulated compression errors are then handled by an error-feedback mechanism. This paper shows a 2x speedup in training time for tasks like GPT-2 pre-training and improved performance in fine-tuning LLMs like LLAMA2-7B.

### Strengths
- The paper tackles the a very relevant issue of communication overhead in large-scale model training. The writing is clear and well presented. SEPARATE’s design as a simple, plug-and-play gradient compression method makes it highly practical. The paper also presents theoretical proof showing that the convergence rates of SGD and Adam are maintained while using SEPARATE and also shows relevant experiments.

### Weaknesses
The method GaLore (Zhao et.al) has proven that gradients are low rank during training. This work can be cited in this context.

Minor:
The experiments compare the training time of SEPARATE with other efficient communication techniques. This is a relevant indicator of communication overhead, but training time also includes computation time which could different for other methods. Therefore reporting bandwidth usage or total data transfer volume in addition to time could help demonstrate  reduction in data exchanged.

### Questions
Refer to weaknesses section

### Soundness
3

### Presentation
3

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
The paper proposes a random projection compression scheme for speeding up gradients' all-reduce operations in distributed training setting (e.g. DDP) via random Gaussian projection. By relying on the unbiased down project and up project and that the variance is bounded, convergence of stochastic optimizer like SGD and Adam are still guaranteed, albeit the bounds suffer a bit from the increased noise from the compression scheme. The authors provide experiments showing that the compression schemes speed up training compared to baselines while does not suffer too much performance degredation.

### Strengths
• Experimental speedup seems useful.

### Weaknesses
• Contributions: The compression scheme is not too new and have been recently explored in a variety of papers like GaLore and Flora (also uses dense Gaussian projection) [1,2]. While the focus of this paper is on communication, I do not see any new idea since the main ideas in GaLore and Flora are also to compress the gradients via some form of projection and then perform optimization in the compressed space before projecting it back up for the update. Extending the ideas from GaLore and Flora to the distributed setting seems straightforward to me. Furthermore, the convergence guarantees are just simple adaptation of well-known proofs i.e. convergence for unbiased and light-tailed noise (bounded variance).

• The moving average error feedback section is not well written. The authors make several claims that are not obvious to me. For example, “[due to the] instability and discontinuity of random projection, the compression error may fluctuate when the random directions are far from the dominant directions of Hessian or the random directions change acutely” is not obvious since the Hessian describes properties of the optimization landscape and the compression scheme impacts (primarily) the direction of the gradient. I think the authors should rewrite the section to compare with the previous error-feedback work and argue better for why their use of EMA and reset are better. The connection between the error fluctuation and the Hessian's dominant directions needs more clarification, as the Hessian relates to curvature, not necessarily the direction of the gradient itself. The claim about the moving average maintaining stability also lacks a clear justification, particularly how it bounds the accumulated error.

• Experiments and reproducibility concerns: The authors should disclose the tuning effort and hyperparameters for all methods being compared. I couldn't find how the experiments are conducted to determine the learning rate and what parameters are tuned for what amount. Providing code and reproduction steps should be standard. An improvement is not significant if one method is tuned (i.e. given a lot more compute) significantly more than others. Also, experimental improvement for the error feedback seems insignificant and noise prone. From Table 2, I couldn't tell if the error-feedback helps or not.

### Questions
• I'm sure I understand the authors' connection between the gradient being low rank and the eigenvalues of the Hessian. For gradient compression, low rank could imply that there is some low-error decomposition but I'm not sure what the top-heavy eigenvalues have to do with gradient compression? 

• In defining the error feedback, what is the domain for the argmin of e? Isn't that just the orthogonal component of the gradient relative to the random projection subspace? Also, how do you justify the claim “taking moving average of the historical error maintains the stability and variance of accumulated error?” I am not familiar with 

• The authors should consider other sketching scheme like fast-JL and importance sampling scheme that are much faster than dense Gaussian projection. 

• Theory requires fresh i.i.d. Gaussian matrix to be generated across all nodes identically every round to ensure the compression and decompression is unbiased. What is the additional cost to communicate this?

### Soundness
3

### Presentation
2

### Contribution
2
