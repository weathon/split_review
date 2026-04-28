# Improved Variational Inference in Discrete VAEs using Error Correcting Codes

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Despite significant advancements in deep probabilistic models, effective learning of low-dimensional discrete latent representations remains challenging. This paper introduces a novel method to improve variational inference in discrete latent variable models by employing Error Correcting Codes (ECCs) to add redundancy to the latent representations, later exploited by the variational approximated posterior to provide more accurate estimates, thereby reducing the variational gap. Drawing inspiration from ECCs used in digital communications and data storage, we demonstrate proof-of-concept using a Discrete Variational Autoencoder (DVAE) with binary latent variables and block repetition codes. We then extend it to a hierarchical structure inspired by polar codes, in which some latent bits are more robustly protected than others. Our approach significantly enhances generation quality, data reconstruction, and uncertainty calibration compared to the uncoded DVAE, even when trained with tighter bounds such as the Importance Weighted Autoencoder (IWAE) objective. In particular, we demonstrate superior performance on MNIST, FMNIST, CIFAR10, and Tiny ImageNet datasets. The general approach of integrating ECCs into variational inference is compatible with existing techniques to boost variational inference, such as importance sampling or Hamiltonian Monte Carlo. We also formulate the properties that ECCs need to possess to be effectively used for improved discrete variational inference.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the method of Error-Correcting Codes (ECC) into the problem of DVAE. The goal is to safeguard the latent variables to add redundancy to the latent representations.  In this way, the proposed method utilizes the redundancy introduced by the ECC to constrain the solution space of $q(c|x)$, given that each bit from $m$ is repeated L times (through the known G) to create c. Empirical result demonstrated the reconstruction signal to noise ratio of the VAE with ECC is improved than that without ECC.

### Strengths
Novelty: The paper is novel in it borrows the method of Error-Correcting Codes (ECC) and introduces it into the problem of DVAE. The motivation is to safeguard the latent variables by adding redundancy to the latent representations through the error correction method in information theory.  In this way, the proposed method claims that it is able to utilizes the redundancy introduced by the ECC to constrain the solution space of $q(c|x)$, therefore leading to a better reconstruction signal to noise ratio of the DVAE than that without ECC. To me, this seems to be the first paper that introduces this method.  

Motivation and Significance: The paper aims to improve the reconstruction of the DVAE by introducing the ECC method from information theory. This is a good example of how the techniques in information theory and communication techniques can help improve generative models. The motivation of the work is good and interesting.

### Weaknesses
Clarity and rigour: I am a lost in section 4, where how the $m$ is sampled and encoded into the required $c$ is introduced. It seems to me that c is now a linear transformation of $m$ through the known $G$. However, how c is sampled and backpropogated through the DVAE is unclear to me. This section also says: `When comparing uncoded vs. coded DVAEs, the structure of the decoder NN is equal in both cases except for the first Multilayer Perceptron (MLP) layer that attacks the input z'. This is very confusing to me. What does the ``attack'' mean here? Where did the attack come from? In the earlier section of the paper, I did not assume there is any noise injection or attacks existing in the generative model. Also, as the c is linear transformation of the original m. it is unclear to me why such redundancy can improve the signal to noise ratio of the reconstruction. For communication channels, yes, because there is loss during the signal transmission in the channels, but I do not understand why the c=mG can help better constrain the sampling space of $m$ and why this is relevant in achieving a better generative model. I guess better instantiation of the the method with further theoretical support and an algorithmic flow can better support the idea of the paper.

### Questions
1. Please clarify what is the gain of introducing ECC into the encoding of $m$ is beneficial intuitively. Where does the noise come from (analogously to communication channels), and why ECC helps reducing the reconstruction error through this encoding. 

2. If possible, please use theoretical support to prove that the encoded DVAE can achieve a better SNR (signal to noise ratio) through the proposed encoding of latent variable. 

3. I appreciate if any algorithmic flow is further provided in the appendix or somewhere to better clarify the sampling process of c and how it is backpropogated.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose to improve variational inference in discrete variational autoencoders by utilizing error correcting codes (ECCs) in the latent space. Despite significant advances in VAEs, the ability to learn low-dimensional discrete latent-variable models remains a challenging task. To that end, the authors employ ECCs as borrowed from digital communications in order to add redundance in the posterior samples. During training, the VAE is able to capture meaning in the latent variables, resulting in significantly improved generation quality and more accurate estimates. The authors emphasize that this technique is general and can be used alongside existing VAE techniques, such as tighter importance weighted autoencoders and Hamiltonian Monte Carlo.

### Strengths
The authors present a theoretically sound and practically useful enhancement to discrete VAEs, noting its practical utility in digital communication. The paper is well-presented; it is easy to follow the contribution from the problems and weaknesses of contemporary approaches to the proposed solution. The experiments validate the theoretical claims, including the claim that the proposed method can be used alongside existing enhancements like IWAEs.

### Weaknesses
Although the particular enhancement presented is novel, the motivation behind has been thoroughly studied within the context of VAEs in previous papers, specifically in relation to lossy/lossless compression and communication [1, 2]. The paper mentions Vector Quantized VAEs as an existing approach only briefly, failing to discuss the significance of it in relation to the aforementioned overlapping subjects. It would be helpful to discuss the general relationship between compression and variational inference and how certain VAE implementations exploit this close relationship to their advantage for certain applications, such as lossy compression [2, 3] and lossless compression [4]. Specifically, the paper does not adequately address how the proposed method compares to other techniques that explicitly leverage the rate-distortion trade-off, such as those that use bits-back coding or hierarchical latent structures to achieve better compression and, consequently, better generative performance. Furthermore, the paper does not discuss the computational overhead of the proposed error-correcting codes, which could be a significant factor in practical applications, particularly when dealing with high-dimensional data or complex models.

### Questions
My suggestion to the authors is to read the papers referenced in 'Weaknesses' and write a small section in the introduction describing the relationship between variational inference and Shannon's rate-distortion theory of lossy compression. This will substantially reinforce the validity of the proposed approach, as there is theoretical justification for utilizing a tool originally used in digital communications. Alternatively, the overlap between digital communications and variational inference is made more explicit, so that the unfamiliar reader can make sense of why such a tool is useful.

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
4

### Summary
The authors propose to introduce redundancy into the latent representation in a Discrete Variational Autoencoder (DVAE) by employing error-correcting codes (ECC). This would reduce errors in samples drawn from the variational posterior, resulting in a better estimation of the true posterior.

### Strengths
- The contribution is novel and interesting.
- The paper is well-written, and mathematics is easy to follow.
- Introducing ECCs results in significant performance improvement in DVAEs across several datasets as demonstrated in the paper.

### Weaknesses
While I appreciate the contribution and the presented results in the paper, there are few concerns I have which are listed below:

- Comparison baselines: The baseline used for comparison is just DVAE with a simple independent prior. It would better highlight the effectiveness of the proposed approach if the comparison is also done with DVAEs with Boltzmann machine priors and other discrete VAE models such as VQ-VAE (discussed in the introduction section).
- The ablation study is conducted by adjusting the number of parameters of a neural network. I think it’s more convincing to compare the results of the uncoded and coded DVAEs with the same dimensionality of latent space (let's say D). (The case where the coded DVAE has redundancy included in it (D = ML with only M original message bits) while the uncoded VAE has D original message bits.)
- To directly verify the improvement in variational inference, I believe measuring the variational gap (inference gap) between the uncoded and the coded DVAEs (as done in [1]) would be helpful. This would provide a direct verification of the main claim of the paper.
- Minor: The resolution of Figure 1(b) is poor. Also, the metric used for measuring reconstruction loss in the vertical axis is not stated.

### Questions
- Can the proposed method be extended to VAE with continuous latent space?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel approach to enhancing variational inference for discrete latent variable models. The method introduces redundancy in the latent space by leveraging error-correcting codes (ECC) from coding theory, resulting in improved performance. The proposed technique is applied to discrete variational autoencoders (DVAEs) with binary latent variables. It demonstrates improvements in generative quality, data reconstruction, and uncertainty calibration across datasets such as MNIST, Fashion MNIST, CIFAR-10, and Tiny ImageNet.

### Strengths
- The integration of ECC into variational inference is innovative, and the concept shows promise for applicability across various latent space models.
- The method is validated on diverse datasets, including MNIST, Fashion MNIST, CIFAR-10, and Tiny ImageNet, providing evidence of its generalizability.
- The paper comprehensively evaluates coded and uncoded models using various metrics, such as PSNR, log-likelihood, reconstruction quality, and uncertainty calibration.

### Weaknesses
 - The paper appears to mix theoretical claims with empirical results. For instance, the statement, "This way, it is possible to reduce the mistakes committed when comparing $m$ with samples drawn from $q(m|x)$, obtaining a tighter approximation to the true posterior $ p(m|x)$," suggests a theoretical result. However, it is unclear if this has been formally proven. Additionally, there is no explicit theoretical proof showing that the inclusion of ECC improves generalization performance. Based on my review, such proof does not seem present in the paper.
- As Equation (9) indicates, using ECC increases the number of parameters due to the added redundancy. This corresponds to an effective increase in the dimensionality of the latent variables compared to the original model without ECC. In the numerical experiments, comparisons should be made with uncoded models with the same total number of latent dimensions. For example, in the case where $ c=10$, it would be more appropriate to compare against an uncoded model with $z=10$. Whether the observed performance improvements are due to the added parameters or the ECC itself remains unclear. The authors should clarify the number of parameters in the models and specify the dimensions used for $c$ and $z$. Based on my understanding, the notation "CODED 5/100" in Figures 4, 5, and 6 likely corresponds to $z=5$ and $c=100$, meaning the model has parameters associated with $c=100$. In this case, wouldn't the appropriate baseline be an uncoded model with $z=100$?
- The paper appears to exceed the page limit, which I understand to be 10 pages. Could you confirm whether the page count adheres to the conference guidelines?

### Questions
- Why is the parameter $c$ absent on the left-hand side of Equation (8)? Could you clarify the reasoning behind this formulation?
- How does the dependency on $\beta$ manifest in Equation (7)? It would be helpful to have a more detailed explanation of its role.
- If the transformations in Equations (10) and (11) are applied, can it still be demonstrated that the Evidence Lower Bound (ELBO) serves as a lower bound for the log-likelihood?

### Soundness
3

### Presentation
3

### Contribution
4
