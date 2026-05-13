# Generalization through variance: how noise shapes inductive biases in diffusion models

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
How diffusion models generalize beyond their training set is not known, and is somewhat mysterious given two facts: the optimum of the denoising score matching (DSM) objective usually used to train diffusion models is the score function of the training distribution; and the networks usually used to learn the score function are expressive enough to learn this score to high accuracy. We claim that a certain feature of the DSM objective—the fact that its target is not the training distribution's score, but a noisy quantity only equal to it in expectation—strongly impacts whether and to what extent diffusion models generalize. In this paper, we develop a mathematical theory that partly explains this 'generalization through variance' phenomenon. Our theoretical analysis exploits a physics-inspired path integral approach to compute the distributions typically learned by a few paradigmatic under- and overparameterized diffusion models. We find that the distributions diffusion models effectively learn to sample from resemble their training distributions, but with `gaps' filled in, and that this inductive bias is due to the covariance structure of the noisy target used during training. We also characterize how this inductive bias interacts with feature-related inductive biases.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main idea of the paper is that diffusion models generalize since the training step of estimating the score uses the “proxy score” as its target, which is a noisy version of the true score, or more accurately, a pointwise version of the score, conditioned also on the training data point. This introduction of this randomness into the nonlinear estimation process, and then into the diffusion process is claimed to lead to randomness in the generation process, and in turn, to generalization.

### Strengths
Understating the empirical success of diffusion models in creating new samples that are similar to the training set is a timely and central question. The analysis made in the paper is dedicated to the generative question, and does not impose generalization measures from other problems (e.g., the MSE of the score function). The intricate details of the diffusion models considered are clearly discussed, and how they affect the generalization process. The paper is well written and conveys its ideas in an interesting way. 

An analytic stochastic path integral technique is used to derive closed-form expressions for the sampling distribution of new samples, with focus on the covariance structure, which highlights the role of the variance of the score proxy in the generation of new samples. It is also a direct performance measure compared to the MSE of the score. This technique is exemplified on two analyzable architectures.

### Weaknesses
1) The paper assures that the generated samples are different from the training samples due to the noise in the score proxy, but this does not seem to explain why the generated samples are meaningful in some sense (e.g., have similar features to the training samples). If one assumes a ground truth distribution then this is obvious, but the authors emphasize that they refrain from that, but it is not clear what replaces this assumption (beyond the generated sampled being different from the training samples). Specifically, while the paper argues that the variance in the score proxy leads to generalization, it doesn't clarify what properties of this variance ensure that the generated samples remain within a reasonable manifold or possess features similar to the training data. The argument that the generated samples are different is insufficient; it needs to be shown why they are *meaningfully* different, and not just random noise.

2) Except for the appearance of a non zero covariance matrix in noise of the reverse diffusion process, the expressions in Propositions 5.1 and 5.2 are somewhat implicit. For example, it is not obvious how easy it is to compute them, or how its form affects generalization. The paper provides closed-form expressions, but lacks a discussion on the practical implications of these forms. For instance, how does the structure of the V-kernel, which depends on the covariance of the proxy score and the feature maps, influence the diversity and quality of the generated samples? A more detailed analysis of how these expressions can be used to understand and control the generalization process would be beneficial.

### Questions
1. Line 67: What is exactly meant by “boundary regions” ? One example is regions that are close to multiple training points, but how these are defined in general ? As high likelihood regions ? This term is used repeatedly afterwards so it would be good to accurately define it. 

2. Line 75: How does the claim “models generalize better when they are somewhat underparameterized” agree with the (Karras et al, 2024) paper mentioned on line 48 ? 

3. Line 78: Why interpolation considered a non-trivial generalization ? 

4. Line 138: It would be better to introduce the proxy score before (4). 

5. How is the operator \mathcal{D} is defined on (6) ? 

6. Section 4: It is explained that even using the generated samples to estimate the score leads generalization. But what is the starting point of the process X_T (the noise point). Isn't this point generated from the training data in a noisy manner, and this also contributes to generalization ? 

7. Line 207: Once the higher order terms in (7) are neglected, it is mentioned that this implies that the estimator distribution is approximately Gaussian. However, due to the Gaussianity of the forward process, doesn't this tacitly also approximate the data distribution as Gaussian ? In other words, if we assume that the data distribution is Gaussian, would the result be the approximated integral of (7) ?

### Soundness
3

### Presentation
4

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
This paper investigates the generalization capabilities of diffusion models through the perspective of "generalization through variance," a novel concept where the inherent noise in the denoising score matching (DSM) objective used in training significantly influences model generalization. The authors develop a mathematical theory using a physics-inspired path integral approach, which reveals how the covariance structure of the noisy training target impacts inductive biases. The findings suggest that diffusion models are not merely reproducing training data but are capable of filling in 'gaps' that enhance their generative abilities.

### Strengths
The paper's originality lies in its novel theoretical framework, which is a significant leap in understanding the mechanics behind diffusion models' ability to generalize. The quality of the theoretical analysis is high, and the writing is clear. The significance of the work is evident as it gives a new understanding of the generalization of diffusion models.

### Weaknesses
1. The paper's main weakness is the lack of empirical validation of the theoretical claims. While the theoretical intuition is clear, the paper would be greatly strengthened by including simulations or experiments that demonstrate the practical impact of the "generalization through variance" phenomenon. Specifically, the paper lacks concrete examples where the predicted covariance structure directly influences the generative process, and how this effect compares to other factors like model architecture or training data size. Without such validation, the theory remains somewhat abstract and its practical relevance is unclear.
2. There is a lack of theory directly bridging the gap between variance and generalization error. The paper introduces the concept of a V-kernel, but it does not provide a clear mathematical link between the properties of this kernel and the generalization performance of the diffusion model. It would be beneficial to have a more explicit theoretical framework that connects the V-kernel to metrics such as the expected generalization error, or at least provide bounds on this error based on the characteristics of the V-kernel.

### Questions
**1.** On the bottom of page 1 “At present, there is arguably no theory that describes…” It seems there exists a bunch of papers analyzing the generalization ability of diffusion models including their generalization time and its relation to data structure, see [1], [2].

[1] Li, P., Li, Z., Zhang, H., & Bian, J. (2023). On the generalization properties of diffusion models. Advances in Neural Information Processing Systems, 36, 2097-2127.

[2] Fu, S., Zhang, S., Wang, Y., Tian, X., & Tao, D. (2024). Towards Theoretical Understandings of Self-Consuming Generative Models. arXiv preprint arXiv:2402.11778.

**2.** It would be clearer to add more description to Figure 1, including the scale of the variance heat map, etc.

**3**. How does the "generalization through variance" compare with other known mechanisms of generalization in diffusion models, such as those related to model capacity and training set structure? In particular, is there a specific formula between V-kernel with any kind of generalization error (or its bound)? If so, the generalization could be more quantitively measured based on V-kernel. 

**4**. Could the authors provide empirical evidence or simulations that specifically illustrate the effects of the covariance structure on generalization as hypothesized in the paper?

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
The authors study the generalization in diffusion models. They highlight six key factors influencing generalization: noisy objective functions, forward process dynamics, nonlinear score dependencies, model capacity, architectural features, and the structure of the training set. They 
attribute the generalization of diffusion models to the fact that the training objective is in fact equal to the ground truth score function only in expectation. The key statement is that generalization occurs if and only if the V-kernel is not zero. Then they characterize the generalizability of diffusion models by analyzing the structures of V-kernel under several simplified conditions.

### Strengths
1. Expressing PF-ODE in terms of the path integral is novel and offers important insight i.e, generalization occurs if and only if the V-kernel is nonzero.

2. The paper provides comprehensive study on three distinct cases through the V-kenrl: (i) memorization (ii) linear model (iii) NTK model. These results demonstrate V-kernel as a useful tool toward understanding generalization.

### Weaknesses
(i) The authors claim that generalization occurs if and only if V-kernel is nonzero since otherwise the reverse sampling process can only produce training examples. However, this definition seems restricted since when diffusion models generalize, they not only differ from the PF-ODE dynamics, but generate "high quality" samples as well. In other words, the V-kernel should have certain benign properties. This point is not adequately addressed in the current paper. Specifically, the paper does not discuss what properties of the V-kernel lead to desirable generalization, such as generating samples that are diverse and not simply noisy variations of training data. The current definition seems to only capture the ability to deviate from the training data, but not the quality of that deviation.

(ii) In section 5 the authors derive the analytical form of the V-kernels under three circumstances. However, the resulting equations (9), (13) and (17) are really hard for me to interpret. Can the authors provide more explanation on the unique properties of these different V-kernels and how they shape the distributions corresponding to the reverse sampling process? The paper would benefit from a more intuitive explanation of these equations. For example, how do the different terms in these equations relate to the properties of the training data or the model architecture? What are the implications of these different forms of V-kernels for the generated samples? A more detailed analysis of the impact of these kernels on the reverse process is needed.

(iii) As a researcher focuses on empirical works, I don't find the results of this paper very useful. I think the paper could benefit from a further discussion on how the results can help improving practical diffusion models. The paper does not offer concrete guidance on how the theoretical findings can be translated into practical improvements for diffusion models. For example, how can the understanding of the V-kernel be used to design better architectures, training procedures, or sampling strategies? The paper should provide a more explicit connection between the theory and practical applications.

### Questions
See my questions in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
