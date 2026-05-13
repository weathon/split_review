# Dissecting Gradient Masking and Denoising in Diffusion Models for Adversarial Purification

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Diffusion models exhibit remarkable empirical robustness in adversarial purification. The mechanisms underlying such improvements remain unclear. It is possible that diffusion models effectively purify the adversarial examples via the learned stimuli prior. Alternatively, the substantial randomness added in the diffusion models may cause gradient masking that contaminates the empirical estimate of adversarial robustness. Here, we seek to dissect the contribution of these two potential factors. Theoretically, we illustrate how a purification system with randomness can cause gradient masking, which can not be addressed by the standard expectation-over-time (EOT) method. Inspired by this, we propose and justify that a simple procedure, randomness replay, can provide a better robustness estimate when randomness is involved. Experimentally, we verify that gradient masking indeed happens under previous evaluations of diffusion models. After properly controlling the effect of randomness, the reverse-only diffusion model (RevPure) provides a better robustness improvement than the previous DiffPure framework, suggesting that the robustness improvement is solely attributed to the reverse process. Furthermore, our analyses reveal that robustness improvement is caused by a sequential denoising mechanism that transforms the stimulus to a direction orthogonal to the original adversarial perturbation, rather than reducing the $\ell_2$ distance between the transformed and clean stimuli. Our results shed new light on the mechanisms underlying the empirical robustness from diffusion models, and shall inform future development of more efficient adversarial purification systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors revealed that diffusion models gain robustness from randomness, which causes gradient masking. They showed that randomness challenges the traditional expectation-over-time (EOT) method, leading to an overestimate of robustness. Addressing this, they proposed "randomness replay" for a more accurate robustness measure. They also found that robustness in diffusion models doesn't require a forward process; a reverse-only process is sufficient. Importantly, they demonstrated that diffusion models improve robustness by altering perturbed samples in a direction orthogonal to adversarial perturbations, thus weakening the strong attacks by removing the adversarial projections.

### Strengths
(1) The experimental results support the claim that randomness in the diffusion model can cause gradient masking, which cannot be addressed EOT method. The simple example in section 4.2 provides good intuition behind the claim.

(2) The exploitation of the purification power of diffusion by removing the adversarial projection is novel and insightful for future work.

### Weaknesses
(1) The study, while insightful, falls short of providing fundamental theoretical analysis. The example in section 4.2 is overly specific, leaving a gap in the broader understanding. A more general, perhaps probabilistic, theoretical exploration of how randomness leads to gradient masking and how randomness replay enhances robustness would significantly strengthen the work. Specifically, the current analysis lacks a clear connection between the observed gradient masking and the underlying properties of the diffusion process, such as the noise schedule or the learned score function. A theoretical validation of the diffusion model's ability to remove adversarial projections would also be a valuable addition, perhaps by analyzing the spectral properties of the diffusion operator or the alignment of its denoising directions with the adversarial subspace.

(2) The presentation of the theorems requires clearer explanations for each notation. For instance, in Theorem 1, the precise meaning of each symbol is unclear without delving into the proof. Providing meaningful explanations alongside the statement of each theorem would enhance comprehension. For example, it is not immediately clear what the relationship is between the chi-squared distribution and the adversarial space. Furthermore, the assumptions underlying the theorems, such as the nature of the adversarial space, should be more explicitly stated and justified in the context of diffusion models.

### Questions
Can the authors explain why the diffusion model can remove adversarial projection? I believe this would be insightful for future work.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Besides generating stunning images, diffusion models have been shown to be very suitable defense for adversarial robustness, which later became an area of research called "Adversarial Purification". This paper first theoretically distinguishes the role of individual components: randomness (gradient masking) of synthesis process and learned generative prior. Then they experimentally (on CIFAR-10) show that previous adversarial purification methods rely on gradient masking. Finally they propose new method RevPure that better controls the effect of randomness, and thus provides better robustness. Interestingly, authors also found that denoising process in diffusion models is orthogonal to original perturbation.

### Strengths
1) Solid theoretical analysis of the key mechanisms in diffusion-based adversarial purification methods. Illustrations and theorems are clear and interesting.
2) Easy-to-follow writing with good introduction, motivation, related work, and theoretical methodology.
3) Interesting observation that sequential denoising processes in diffusion models transform an adversarial example in the direction orthogonal to the original adversarial perturbation.
4) Interesting finding that forward process of diffusion models is unnecessary for adversarial purification, although it was observed previously in DensePure.

### Weaknesses
1) The closest works (DiffPure, DensePure) validated their experiments not only on CIFAR-10, but on large-scale datasets such as ImageNet. To make the method closer to real world, ImageNet experiments are necessary. The lack of ImageNet experiments limits the generalizability of the findings, especially given the known differences in feature distributions and adversarial vulnerability between CIFAR-10 and ImageNet. The paper should demonstrate the effectiveness of the proposed method on a more complex and realistic dataset.
2) Only one architecture (WideResNet-28) is studied, while other works studied diverse set of architectures such as ViTs, ResNets, etc. This narrow focus on a single architecture makes it difficult to assess the robustness of the method across different model families. The paper should include experiments on a wider range of architectures to demonstrate the general applicability of the proposed approach. Specifically, the behavior of the method on transformer-based architectures, which have different inductive biases than convolutional networks, should be investigated.
3) Effect of generation quality of the model (FID) on the robustness is only studied using two models (EMA DDPM and Non-EMA DDPM). You can't conclude anything from two points. More diverse set of models (maybe checkpoints from different epochs) should be studied. The paper needs a more thorough investigation of the relationship between generation quality and adversarial robustness. A more comprehensive study should include a wider range of models with varying FID scores, potentially including models trained with different hyperparameters or at different stages of training. This would allow for a more robust conclusion about the impact of generation quality on the effectiveness of the proposed adversarial purification method.

Minor weaknesses:
1) $\chi^2$ should be properly introduced.

### Questions
1) "Consider we run an adversarial attack on a dataset and get an accuracy of 80%. Assume the attack is perfect, thus we can always find an adversarial example if there exists one in the region, which is the ultimate goal for adversarial attack research. Then the accuracy means for 80% of the data, we manage to find at least one adversarial example within the region. Thus, the empirical robustness with a perfect attack is a good approximation of the absolute robustness" 
Can you elaborate more on this example? What is accuracy here (accuracy of the model on perturbed data or attack success rate)? How based on first 3 sentences we can claim that empirical robustness is a good approximation?
2) How does your method affect the inference time of the classifier?

### Soundness
4 excellent

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper theoretically reveals the phenomenon that purification system with randomness provides false sense of robustness. A method named "randomness replay" is further proposed to better estimate the robustness. Experiments on Diffusion Models verify the proposals.

### Strengths
- The theoretical analysis is sound and easy to understand (e.g., illustration in Figure 1).
- The paper is easy to read.

### Weaknesses
 - The structure of the paper is somewhat confusing. Diffusion models and gradient masking appear and mentioned in Abstract and Introduction, but most of the theoretical analysis are irrelevant with them. 
- The experimental results shown in Tables seem weak. It will be better if more results are provided.

- Overall, this work is based on the DiffPure framework and present its one limitation. Moreover, attack on a system with randomness has been sudied. Therefore, I think the novelty is limited.

- Writing issue:
   - "Since the successful rate of applying the attack is the cdf of χ2(n), and n is the dimensionality of the data, which is typically very high for images (i.e., for CIFAR-10, n = 32 × 32 × 3 = 3072)."

### Questions
- It is mentioned "Gradient masking has been defined as “construct a model that does not have useful gradients”. Could you please explain how do you illustrate that a purification system with randomness can cause "a model does not have useful gradients"?
- It seems that the theoretical analysis are general and can be used for any preprocess-based defense methods. Could you please discuss more about the difference between this analysis and related work? 
   - For example, Carlini etal. 2019 proposes "Verify that attacks succeed if randomness is fixed.". What is the difference between randomness replay and this method?

- Could you please provide more explanation if the forward and reverse process in Diffusion Models? Why DiffPure proposed to utilize both the two processes while only use the reverse process is also workable?

- Could you please explain that how does the observation that "The reverse process indeed gradually removes the projection on the original adversarial direction..." further support that "forward process may not be useful for robustness"? I think it will be better if you can also illustrate the forward process in Figure 4a.

### Soundness
3 good

### Presentation
3 good

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
Theoretically, we illustrate how a purification system with randomness can cause gradient masking, which can not be addressed by the standard expectation-over-time (EOT) method. Experimentally, we verify that gradient masking indeed happens under previous evaluations of diffusion models. This paper studies an interesting phenomenon in the adversarial purification based on diffusion models. However, I am still concerned about the experiments.

### Strengths
1. The idea of studying the connection between Diffusion-based adversarial purification and gradient masking is novel.
2. The theoretical result provide some new insights.

### Weaknesses
1. I am not fully convinced by the experiments that the diffusion-based adversarial purification causes the gradient masking. Here, the problem is whether there is measure of the gradient masking phenomenon. Specifically, while the authors claim gradient masking, there isn't a clear metric to quantify the degree of masking. It's not sufficient to simply observe a drop in attack effectiveness; a direct measure of the gradient's quality is needed. For example, how does the cosine similarity between the true gradient and the gradient used for the attack change with the introduction of randomness? Without such a measure, it's difficult to definitively conclude that gradient masking is the primary cause of the observed effects.

2. The datasets are limited. Can the authors provide further experiments to verify their theoretical findings, i.e. performing experiments on other datasets, like Imagenet and MNIST?

### Questions
See the question above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
