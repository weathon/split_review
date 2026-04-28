# Secure Diffusion Model Unlocked: Efficient Inference via Score Distillation

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 5, 3

## Abstract
As services based on diffusion models expand across various domains, preserving the privacy of client data becomes more critical. Fully homomorphic encryption and secure multi-party computation have been employed for privacy-preserving inference, but these methods are computationally expensive and primarily work for linear computations, making them challenging to apply to large diffusion models. While homomorphic encryption has been recently applied to diffusion models, it falls short of fully safeguarding privacy, as inputs used in the $\epsilon$ prediction are not encrypted. In this paper, we propose a novel framework for private inference for both inputs and outputs. To ensure robust approximations, we introduce several techniques for handling non-linear operations. Additionally, to reduce latency, we curtail the number of denoising steps while minimizing performance degradation of conditional generation through score distillation from the unconditional generation of the original model with full denoising steps. Experimental results show that our model produces high-quality images comparable to the original, and the proposed score distillation significantly enhances performance, compensating for fewer steps and approximation errors.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Secure Diffusion introduces an approximation function and employs a Score Distillation method, which utilizes the score of an unconditional generation path in an unencrypted space to efficiently handle encrypted inputs. This approach reduces computational load in encrypted data environments while maintaining quality similar to the original model, achieving faster inference speeds.

### Strengths
- A new method called SDU is introduced.

- For model comparison, it is necessary to derive the distribution $p(z|y)$ using the encrypted condition $y$. The idea here is that this can be approximated by using randomly sampled $p(z)$, which provides a similar outcome.

### Weaknesses
 - The approximation function was only compared with CrypTen, an open-source library, without any comparisons to approximation functions used in recent papers. (CrypTen was published in 2021, but it’s unclear how up-to-date its approximation methods are in this paper.) These are some examples of the recent papers.

* Qu, Hongyuan, and Guangwu Xu. "Improvements of Homomorphic Secure Evaluation of Inverse Square Root." International Conference on Information and Communications Security. Singapore: Springer Nature Singapore, 2023.
* Luo, Jinglong, et al. "SecFormer: Fast and Accurate Privacy-Preserving Inference for Transformer Models via SMPC." Findings of the Association for Computational Linguistics ACL 2024. 2024.
* Lu, Wen-jie, et al. "Bumblebee: Secure two-party inference framework for large transformers." Cryptology ePrint Archive (2023).

- They point out that the main limitation of existing approximation functions is that they fail outside certain ranges. Their contribution is adding simple scaling and other nonlinear functions, like tanh, to improve stability for larger inputs.

- However, there is no analysis of the approximation accuracy of their proposed function.

- The experiments are very limited. There is no comparison with prior research, and the results consist only of a single chart comparing their method with the score of the original model.

**Overall review**

There were many unclear points in the scenario, making it difficult to understand.

Ultimately, the model proceeds as follows:
1. Encrypt the original diffusion model using an approximation function.
2. Apply Score Distillation to align the encrypted model’s output with the original model’s output based on encrypted inputs.
3. Return the result.

The idea in step 2—approximating via Score Distillation without obtaining the original model’s result on encrypted inputs—seems promising. However, the paper does not show any experiments to illustrate the efficiency of this idea.

The two main contributions are improvements in approximation functions and Score Distillation. However, the approximation function appears poorly developed, as it seems they did not follow up on the latest research in approximation functions.

### Questions
1. it is necessary to measure performance in an MPC environment rather than in a plaintext setting.
2. In the presented experiment, FID, CLIP-Score, and latency were measured. However, without a baseline for comparison, it may be difficult for users to intuitively understand the efficiency of the proposed PIDM based on the numbers alone. Demonstrating different FID, CLIP-Score, and latency results using other standard models, such as HE-Diffusion (Chen & Yan, 2024) or a model other than SDv1.5, under the same conditions may help substantiate the usefulness of PIDM.
3. It was mentioned that GeLU includes both the sigmoid and Gaussian error functions, but the GELU function does not actually include the sigmoid. How can you explain this?
4. A cubic approximation using tanh was presented, which is a method proposed in Gaussian Error Linear Units (GELUs) by Dan Hendrycks and Kevin Gimpel, so a citation for this would be appropriate.
* Hendrycks, Dan, and Kevin Gimpel. "Gaussian error linear units (gelus)." arXiv preprint arXiv:1606.08415 (2016).
5. For Reciprocal, LayerNorm, GroupNorm, and Softmax, it was mentioned that previous approximation functions had range issues, and scaling was applied to increase this range. Increasing the approximation range via scaling is a very common method. However, if the range is scaled by a factor of d, the impact of error in the approximation function is proportionally increased by d. Therefore, approximation function research typically aims to achieve the highest accuracy within a limited degree, rather than merely extending the range. An analysis on this aspect seems necessary.
6. An accurate analysis of the accuracy of the approximation functions in relation to the number of computations and the feasible approximation range seems necessary. The need for a wide approximation range has not been mentioned.
7. For the approximation of erf, it was only mentioned that crypten used a Taylor approximation, but the degree used was not specified. Furthermore, there was no mention of which approximation methods were applied to other non-linear functions by crypten. An analysis of the approximation methods and computation count used in the library should be included.
8. In Appendix B, it is mentioned that 20 iterations are used for exp in the GeLU approximation. However, 20 iterations cannot achieve a stable approximation within the range of [-10, 10], as shown in figure 2b. Additional clarification on the number of iterations used in figure 2b would be helpful.
9. It is unclear why the encrypted model was not tuned to match the original model from the beginning. The approach involves encrypting a model trained on public data, then adjusting for error accuracy with the user’s encrypted inputs. This raises a fundamental question: if the encrypted model had been pre-tuned to match the original model’s error accuracy on public data, wouldn’t techniques like Score Distillation on encrypted inputs be unnecessary? Please clarify why they chose this approach over pre-tuning the encrypted model.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes running secure inference from a latent diffusion model, in a way that reduces the amount of computation that has to be done in ciphertext space (that is either in MPC or under homomorphic encryption).

They describe this approach, describe some non-linear approximations they had to make and display some results of experiments done on this.

### Strengths
The problem makes sense as something to want to improve, shifting computation out of the encrypted space makes sense as an approach to do that.

The paper proposes some new seemingly improved approximations for non-linear functions in MPC.
The new non-linear approximations may be an improvement though I can't really understand whether they are appropriate and good without knowing the context better (see weaknesses) and it isn't justified that it constitutes a substantial contribution.

### Weaknesses
I can't follow what this paper is proposing, this may well be due to my lack of familiarity with diffusion models but I think the presentation is also confusing and that isn't helping.

The preliminaries define epsilon_theta in terms of epsilon_theta itself and epsilon which is never defined (though I infer from the expectation in (3) being taken over it that it is a random variable). I assume 'the epsilon prediction' is to be minimised though it isn't clear what it is as it depends on epsilon. epsilon_theta seems to be a vector when being taken off x would I therefor be right in thinking that the score function is vector valued?

Lines 9 and 10 in Algorithm 1 depend on an \hat{\epsilon_\theta} that isn't defined anywhere except possibly in (7) and (8) in terms of itself, though these seem to be describing corrections to some baseline that isn't defined.

There is no novelty specifically in secure computation itself here, though if the work can be substantially moved to the clear that would be valuable.

### Questions
I don't think I really have questions, just the above points on presentation that I think should be clarified and openness to the possibility that a reviewer with more knowledge of notation in diffusion model papers can identify understandable substantive novelty here.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new framework for privacy-preserving diffusion model inference. The authors introduce a new method to handle non-linear computations in diffusion models and reduce the number of denoising steps for faster inference. Finally, they conduct empirical studies to validate the effectiveness of the proposed method.

### Strengths
The main advantages can be listed as follows:

1.	The paper adopts several techniques for non-linear operations and proposes a new score distillation sampling method to reduce the computational overhead during private diffusion model inference.
2.	The paper conducts empirical studies on Stable Diffusion v1.5 to show the effectiveness of the proposed method.

### Weaknesses
Despite the strengths, there are some issues with the paper as follows:

1.	I am concerned about the novelty of this paper. The techniques for polynomial approximation of nonlinear functions in Section 3.1 appear to have been proposed in previous studies. For instance, [1] also employs the hyperbolic tangent function to approximate GeLU. The only new contribution in Section 3.1 seems to be the scaling factor, $\sqrt{d}$. Specifically, the use of a hyperbolic tangent to approximate the GeLU activation, while a common technique, lacks a detailed justification for its suitability in the context of diffusion models. The paper does not analyze the approximation error introduced by this substitution, nor does it discuss the potential impact on the stability and convergence of the diffusion process. Furthermore, the scaling factor $\sqrt{d}$, while presented as a novel contribution, needs a more thorough explanation of its derivation and its effect on the overall performance of the approximation.
2.	I am also concerned about the validity of the experimental evaluation of the proposed method. The authors conducted quantitative analysis on only one model and one benchmark dataset without comparison to other methods, as shown in Table 1. This limited evaluation makes it difficult to assess the true effectiveness and generalizability of the proposed approach. The absence of comparisons with other privacy-preserving diffusion techniques or even with standard non-private diffusion models makes it impossible to determine if the proposed method offers any significant advantages. Including comparisons across more datasets and models, especially those with different architectural characteristics, would significantly enhance the credibility and robustness of the experimental results. Moreover, the evaluation lacks a detailed analysis of the trade-off between privacy and performance, which is crucial for practical applications.

### Questions
1.	There seems to be a hyperparameter $m$ in Algorithm 1. What are the hyperparameters of the proposed method, and how are they configured to achieve the trade-off between latency and performance?
2.	How robust is the proposed framework across different types of diffusion models?

### Soundness
3

### Presentation
3

### Contribution
2
