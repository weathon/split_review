# Learning energy-based models by self-normalising the likelihood

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Training an energy-based model (EBM) with maximum likelihood is challenging due to the intractable normalisation constant. Traditional methods rely on expensive Markov chain Monte Carlo (MCMC) sampling to estimate the gradient of normalisation constants. We propose a novel objective called self-normalised likelihood (SNL) that introduces a single additional learnable parameter representing the normalisation constant compared to the regular likelihood. SNL is a lower bound of the likelihood, and its optimum is the maximum likelihood estimate of the model parameters and the normalisation constant. We show that the SNL objective is concave in the model parameters for exponential family distributions. Unlike the regular likelihood, the SNL can be directly optimised using stochastic gradient techniques by sampling from a crude proposal distribution. We validate the effectiveness of our proposed method on various low-dimensional density estimation tasks as well as EBMs for regression. Our results show that the proposed method, while simpler to implement and tune, outperforms existing techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to change the loss function of energy based model based on a variational formulation. The proposed algorithm estimate an extra parameter b together with the energy function $E_\theta(x)$. The author use importance sampling with base distribution $q(x)$ to estimate the normalizing term of the energy function. They carry out the experiments on toy example datasets and energy regression task.

### Strengths
I think this paper is well written and the idea is easy to follow. The reformulation trick, though simple, is interesting to me.

### Weaknesses
However, I am not fully convinced by whether the proposed algorithm really works better in practice than original EBM training when modeling complex distributions. This lies in several aspects:

1. From my own experience, the most challenging part when training the EBM is to get valid samples from the current fitted distribution to estimate the (gradient of) normalizing constant. Previous works try to solve this problem with different sampling techniques. While this work proposes a linear lower bound, it still needs to estimate the normalizing constant with Monte Carlo based method. Thus, it might not really alleviate the training difficulties.

2. To do this Monte Carlo estimation, the work employs important sampling using a base distribution $q(x)$ and $q(x)$ are simple distributions like Gaussian. I suspect this algorithm works because the target distributions tested in this work are very simple, either toy distribution or conditional distribution $p_\theta(y|X)$ where y is low dimensional. If we are modeling model complex distribution like unconditional distribution $p(x)$ on high dimensional data like images, then we still need Monte Carlo based methods and the previous diffculties are still there.

3. The proposed algorithm introduces a variational parameter b, and it requires to update b together with the energy function iteratively. Then similar to the VAE case, whether there can be a mismatch between the estimate of b and the energy function $E_\theta(X)$.  (Not sure whether the $\exp^{-b}$ term will make the training more unstable if b is not well optimized.) Or in other words, how diffcult is it to design the schedule of updating b and energy function to make this algorithm work. 

4. As also mentioned in 2, the modeled distributions in the experiments are too simple to be convincing to me. The modeled experiments are either unconditional distribution on toy data or with image input but only models the conditional distribution on some low dimensional label. The VAE experiment in 5.3 models binary MNIST (which is also not very complex). And with the help of encoder and decoder, the latent space might be more simple. (Beside, what if we train the model VAE-EBM not with $l_{snl}$ but with plain MLE loss? There seems to be included as a baseline in Table 5.) I think in order to make the proposed algorithm more convincing, the authors need to demonstrate better results than pure MLE loss on more complex distributions like real image (face or cifar or SVHN).

5. The review for EBM study seems to be insuffcient, may consider the following works:

[1] Improved contrastive divergence training of energy-based models.

[2] Learning energy-based models by diffusion recovery likelihood.

[3] A tale of two flows: Cooperative learning of langevin flow and normalizing flow toward energy-based model.

### Questions
Please see weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce a novel objective function for estimating Energy-Based Models (EBM), offering a promising alternative to the costly Markov Chain Monte Carlo (MCMC) sampling method. Their proposed objective function not only eliminates the need for MCMC but also provides an estimate of the log-normalizing constant as a byproduct. The paper showcases the effectiveness of this new approach by demonstrating its ability to recover the Maximum Likelihood (ML) estimate and its favorable performance within the exponential family of distributions. To validate their method, the authors conduct comprehensive empirical tests on both low-dimensional synthetic and real-world datasets, illustrating its efficacy and its superiority over Noise Contrastive Estimation (NCE). Additionally, the authors extend the application of their method to Variational Autoencoders (VAEs) with energy-based priors, broadening the scope of their contribution in the field of generative models.

### Strengths
- The paper is well written
- The idea of doing a variational approximation of the logarithm is elegant
- The application to VAEs with energy-based priors is interesting

### Weaknesses
 - The method seems very sensitive to the curse of dimensionality because of its IS component. This scaling issue is not investigated.
- The proposed method is not compared against MCMC-based methods.
- The sensitivity to the choice of proposal should be critical but it is only investigated in low-dimensional cases.
- Most experiments are toy experiments or in a very low dimension.

### Questions
1. Can you provide more real-world experiments ? For instance in generative modeling (without the VAE component) or out-of-distribution detection.

2. As mentioned in the weaknesses, I would expect your method to be very sensitive to the design of $q$.

(a) Did you run a sensitivity comparison with [1], [2] (which develop similar ideas) or NCE in higher dimensional settings (compared to Sec 4.2) ?

(b) Did you try to learn $q$ as done in [3] for NCE ?

3. In [4], the authors give a very similar result as your theorem 3.1 but for NCE. Is there more theoretical comparisons to be drawn against NCE ?

4. As mentioned in the weaknesses, I think it would be nice to compare SNL against MCMC-based methods (at least Langevin based) with apple-to-apple computational budgets.

[1] Will Grathwohl, Jacob Kelly, Milad Hashemi, Mohammad Norouzi, Kevin Swersky, & David Duvenaud. (2021). No MCMC for me: Amortized sampling for fast and stable training of energy-based models.

[2] Hanjun Dai, Rishabh Singh, Bo Dai, Charles Sutton, & Dale Schuurmans. (2020). Learning Discrete Energy-based Models via Auxiliary-variable Local Exploration.

[3] Ruiqi Gao, Erik Nĳkamp, Diederik P. Kingma, Zhen Xu, Andrew M. Dai, & Ying Nian Wu. (2020). Flow Contrastive Estimation of Energy-Based Models.

[4] Bingbin Liu, Elan Rosenfeld, Pradeep Ravikumar, & Andrej Risteski. (2021). Analyzing and Improving the Optimization Landscape of Noise-Contrastive Estimation.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the learning of the energy-based model (EBM). The typical MLE learning requires MCMC sampling of EBM to obtain the gradient of the normalizing function, which can be challenging in practice due to its instability and computational cost. The proposed self-normalized log-likelihood (SNL) method instead parameterizes the normalizing function via a linear variation formulation (Eq.8 in the paper), which does not involve the MCMC sampling but can train the EBM with the SNL estimate.

### Strengths
1. The energy-based model serves as a foundational generative model, and the proposed learning algorithm is thus well-motivated.
2. The paper is in general well-presented, especially the theoretical parts regarding the understanding of the proposed method.
3. The proposed method seems to be flexible as the author extends it to multiple settings, such as prior of VAE and regression tasks (in a supervised scenario).

### Weaknesses
1. This paper has a well-motivated idea and contains comprehensive theoretical derivation for understanding the key idea. However, as mentioned by the author, the NCE method is related, it would be nice to have a deeper theoretical connection and comparison with the NCE method. For now, the major comparison is shown by empirical experiments. 
2. Many other prior works can be applied to some more challenging real data, such as CIFAR-10, CelebA-64, or even the high-resolution (CelebA-HQ-256), so what limited this learning algorithm for such dataset?
3. As a novel learning method, it would be nice to have a practical learning algorithm to simplify and illustrate the main idea.

### Questions
(1) How do we understand the unbiased estimate of SNL (Eq.15) while the last term is based on Jensen's (Eq.6)?

(2) Some typos can be fixed (e.g., Eq.17 \nabla_\theta missing)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
