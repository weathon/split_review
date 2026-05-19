### Summary

This paper makes three contributions to diffusion models by considering the departure from standard variational diffusion models. The authors first propose to generalize the noise schedule so that the noise schedule need not be the same in the forward and reverse process. The authors show that while this is possible in the discrete time setting, in the continuous time limit the ELBO diverges unless the noise schedules are the same. The authors then propose to generalize the forward process by introducing a time/depth dependent encoder. The authors show how the variational loss changes in this case and propose a parameterization of the encoder that approximately eliminates the additional terms in the loss resulting from the generalized encoder. Finally, the authors provide some experiments on CIFAR10, MNIST, and ImageNet32 which show that the proposed generalizations can improve likelihood.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

I found the paper to be well-written and easy to follow. The authors do a nice job of highlighting how their proposed generalizations relate to standard variational diffusion models. I also found the authors' discussion of the various parameterizations of the encoder to be very helpful. Overall, although the contributions of the paper are not particularly significant (see weaknesses), I thought the paper was well-executed and I am grateful to the authors for the meticulous details they provide in the appendices.

### Weaknesses

#### Some Related Works

[1] Blurring diffusion models
[2] Improved denoising diffusion probabilistic models

#### comment

My primary concern with the paper is that the generalizations proposed by the authors already appear in the literature. In particular, the generalization of the noise schedule proposed by the authors appears to be a special case of blurring diffusion models (see e.g. Hoogeboom et al. 2022 and Rissanen et al. 2022) while the generalization of the forward process with a time-dependent encoder is done in the context of blurring diffusion models and also in Daras et al. 2022. The authors should discuss how their work relates to these existing approaches. The authors should consider re-framing their work as a more careful study of blurring diffusion models. For example, the theoretical analysis of the continuous-time limit could be applied to blurring diffusion models and could potentially recover existing results (e.g. the result that blurring diffusion models are not well-defined in the continuous-time limit unless the blurring operator is time-invariant) in a more general way. The authors could also study the performance of different choices of time-dependent encoders and different parameterizations empirically.

Another concern I have is that the paper does not provide enough evidence that the proposed generalizations are useful. The experiments show that the proposed generalizations can improve likelihood on some datasets but it is not clear how the results compare to existing methods. For example, the authors should compare the performance of their method to the performance of blurring diffusion models and other related approaches. It is also not clear if the improvement in likelihood is significant. The authors should provide more evidence that the proposed generalizations are useful in practice.

### Suggestions

The authors should more clearly position their work within the existing literature on diffusion models, specifically in relation to blurring diffusion models and other generalizations of the forward process. While the paper introduces a generalized framework, it lacks a thorough comparison to established methods. For instance, the proposed time-dependent encoder, while presented as a novel contribution, bears a strong resemblance to the time-dependent transformations used in blurring diffusion models. A more detailed analysis is needed to differentiate the proposed approach from these existing methods, highlighting the specific advantages and disadvantages of each. The authors should provide a more rigorous comparison, both theoretically and empirically, to justify the novelty and practical benefits of their approach. This should include a discussion of the limitations of existing methods that their approach overcomes, or a demonstration of improved performance or efficiency.

Furthermore, the empirical evaluation needs to be significantly strengthened. The current experiments, while demonstrating some improvement in likelihood, do not provide sufficient evidence of the practical utility of the proposed generalizations. The authors should compare their method against a wider range of existing diffusion models, including blurring diffusion models, on standard benchmark datasets. This comparison should not only focus on likelihood but also on other relevant metrics such as sample quality and computational cost. It is crucial to demonstrate that the proposed method offers a significant improvement over existing approaches, not just a marginal gain in likelihood. The authors should also investigate the sensitivity of their method to different choices of the time-dependent encoder and its parameterization, providing a more comprehensive understanding of the method's behavior and limitations.

Finally, the theoretical analysis, while interesting, needs to be more tightly integrated with the empirical findings. The authors should explore how the theoretical results, such as the analysis of the continuous-time limit, inform the design and performance of their method. For example, they could investigate whether the theoretical conditions for well-defined continuous-time limits are met in their experiments and how deviations from these conditions affect the results. The authors should also consider extending their theoretical analysis to cover more general cases, such as non-Gaussian forward processes, to further demonstrate the significance of their framework. This would help to establish a stronger theoretical foundation for their work and provide a more compelling justification for the proposed generalizations.

### Questions

- Is the parameterization of the encoder proposed by the authors the best way to approximately eliminate the additional terms in the loss? How important is it that the additional terms are eliminated exactly vs approximately?
- What is the relationship between the encoder used by the authors and the encoder used in blurring diffusion models?
- What is the performance of the proposed generalizations compared to existing methods on standard benchmarks?
- How sensitive are the results to the choice of the time-dependent encoder and its parameterization?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
