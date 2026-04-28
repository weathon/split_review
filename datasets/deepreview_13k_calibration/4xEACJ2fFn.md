# Is the sparsity of high dimensional spaces the reason why VAEs are poor generative models?

- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 3, 6, 6, 6

## Abstract
Variational autoencoders (VAE) encode data into lower dimension latent vectors before decoding those vectors back to data. Once trained, decoding a random latent vector usually does not produce meaningful data, at least when the latent space has more than a dozen dimensions. In this paper, we investigate this issue drawing insight from high dimensional physical systems such as spin-glasses, which exhibit a phase transition from a high entropy random configuration to a lower energy and more organised state when cooled quickly in the presence of a magnetic field. The latent of a standard VAE is by definition close to a uniform distribution on a hypersphere, and thus similar to the high entropy spin-glass state. We propose to formulate the latent variables of a VAE using hyperspherical coordinates, which allows to compress the latent vectors towards an island on the hypersphere, thereby reducing the latent sparsity, analogous to a quenched spin-glass. We show that this is feasible with modest computational increase and that it improves the generation ability of the VAE.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose to convert the latent variables of a VAE to hyperspherical coordinates. This allows them to constrain samples from the prior distribution to a small region in latent space especially if the latent dimension is large. They provide experimental evidence that this improves the performance of the VAE when generating new data. They also provide some theoretical justification arguing that the sparsity of the latent space impairs the smoothness of the latent manifold.

### Strengths
1.	The introduction of hyperspherical coordinates to better capture samples obtain from high dimensional Gaussians is useful especially in the context of constraining the latent variables
2.	The paper attempts to establish an ambitious connection between replica symmetry breaking in spin glasses and their proposed modifications of the loss function that avoids ‘high sparsity’ equatorial regions of the hypersphere.

### Weaknesses
1. The connection to spin glasses is made via a formal similarity of the energy function of a spin glass and their regularization term (equation 8). This connection appears weak as it does not explain: a) how the regularization helps escaping local minima that correspond to low-quality outputs of the VAE, b) the effect on Parisi’s order parameter which seems at the heart of the spin glass theory of neural networks, and c) the role of temperature i.e., the learning rate in the proposed scheme by which desired low-entropic states are reached.
2. I am not sure that sparsity of the latent representation is the root cause of poor generative performance in VAEs. “Posterior collapse” seems a more likely explanation (also of the empirically observed improvements in section 4) as the proposed constraints not only compress the volume but also simply decrease the variance of the prior distribution. 
3. As a minor point, in line 189-190 the authors see sparsity as an impediment to learning a data representation as a smooth manifold. I am not sure I agree unless the objective would be to explicitly construct the manifold (e.g., via simplicial complexes). But the manifold hypothesis (like the spin glass model) is only a conceptual aid (of how to think about VAE representations of data) not a fully developed theory from which algorithms and their convergence properties can be derived.

### Questions
Have you tried running experiments without angular constraints but only radius constraints (to test against the lower variance of the prior effect)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents an enhancement to Variational Autoencoders (VAEs) by introducing a hyperspherical latent space with a novel loss function. The method aims to improve generative quality by concentrating embeddings in denser latent regions, moving them away from the equatorial band often associated with sparsity. The approach offers compatibility with existing VAE structures, requiring minimal adaptation to the standard VAE framework.

### Strengths
• Innovation and Relevance: The use of hyperspherical coordinates in latent space with principles drawn from statistical physics is a unique and potentially impactful innovation.
• Clear Problem Statement: The paper presents the problem of sparse latent spaces in VAEs clearly, providing a well-motivated solution.
• Practical Usability: The proposed method integrates easily with current VAE models and introduces a manageable computational overhead.
• Clarity of Presentation: The visual support, especially in Figure 1b, effectively illustrates the approach, aiding in understanding the latent space adjustments.

### Weaknesses
• Limited Experiments: The method is only evaluated on two datasets (MNIST and another dataset). More examples of generated samples and interpolations would better support the claim of improved density in latent space.
• No Comparison with Relevant Competitors: The paper lacks comparative experiments with established hyperspherical VAEs, such as Davidson et al. (2018), or with Riemannian approaches like “A geometric perspective on VAEs” by Chadebec and Allassonniere.
• Inconclusive Results: The results in downstream tasks like classification are mixed, and the paper’s claims of denser latent space do not
consistently reflect in performance metrics.

While the paper offers valuable theoretical insights, additional empirical support is needed to substantiate the generative benefits relative to state-of-the-art sampling methods.

### Questions
1. Could you provide comparisons with hyperspherical VAEs or other structured latent space models?
2. Have you explored interpolation in the latent space to support your density claims?
3. Why were only two datasets used? Including more diverse datasets could better validate your method.
4. Why would a latent space as tightly concentrated as shown in Figure 1 be desirable? This remains unclear.

### Soundness
2

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
3

### Summary
The paper proposes a new way to formulate the latents of VAE on hyperspherical coordinates. They use real MNIST data to show the improved generalization ability of VAE.

### Strengths
- The paper is well written. 
- The relevant works are clearly listed. 
- The idea of drawing insights from high dimensional physical systems is interesting.

### Weaknesses
The experiment results section is weak.
- The evaluation is only qualitative comparison. Is there any quantitive metric (e.g. classification/prediction error) that can be used to compare the proposed method with existing methods?
- Lack of comparison with other related hyperspherical VAE work listed in the section 2. related works. e.g. Hyperspherical Variational Auto-Encoder’ Davidson et al. (2018),  Yang et al. (2023), Bonet et al. (2022), etc. 
- The paper only shows results on one real dataset. How well does the proposed method generalize to more datasets?

### Questions
See the weakness section above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose expressing the latent variable of a standard VAE in hyperspherical coordinates, reformulating the KL term of the ELBO loss accordingly, to reduce the sparsity in high-dimensional latent spaces and improve the generative performance of the model. Their approach draws on a parallel between high-dimensional spaces in statistical physics, specifically spin glasses, and the training dynamics of a VAE.

### Strengths
- To the best of my knowledge, this work introduces a novel approach to improve generative performance in VAEs by constraining latent representations, exploiting the hyperspherical coordinates formulation to reduce sparsity in the high-dimensional latent space.
- I find the connection between VAE training and physical systems, such as spin glasses, particularly valuable, as it provides a novel perspective for understanding the model's training dynamics.

### Weaknesses
 - The authors should revise the references (e.g., replace arXiv preprints with published versions where available, add access dates for blog references, and consider replacing Wikipedia links with more reliable sources). Additionally, some typos were noted in the main text, and Figures 4 and 5 appear in low resolution, making the text difficult to read.
- I think the experimental section could be strengthened. Although the primary aim of this work is to improve the model's generative performance, the authors present generated samples only on MNIST, which is a simple dataset. Also, they do not compare the generative performance of the method with any other baseline (in the introduction they mention methods that improve generative performance by using more flexible priors but do not show if the results achieved are comparable).
- The paper lacks a concluding discussion and does not explore potential limitations of the method or directions for future research, which I believe would add significant value.
- The paper's discussion of generation performance relies heavily on FID scores, which can be misleading. For example, lower FID scores are sometimes associated with blurry images, while higher FID scores can correspond to more visually detailed and appealing samples. This discrepancy suggests that FID alone may not be a sufficient metric for evaluating the generative capabilities of the model, and a more comprehensive evaluation is needed.
- The figures lack clarity regarding the specific metric being shown, particularly whether it is the self-FID or a different variation. This ambiguity makes it difficult to interpret the results and compare them across different experiments. Furthermore, the figures should clearly indicate the specific configurations being compared, as the current presentation makes it challenging to discern which settings lead to improved performance.

### Questions
- What are the main limitations of this method?
- Could the authors provide a comparison with additional baselines and training times? It would be valuable to compare the generative performance and training times of the proposed method with other state-of-the-art approaches to evaluate whether the additional computations required for using hyperspherical coordinates are justified by the improvements in generation performance.
- The authors state that ‘the random samples of an independent multivariate Gaussian distribution fall in the equator of a hypersphere, and thus none of them is near the singularities of the hyperspherical coordinates’. However, once the latent samples are forced away from the equator, could it be possible to fall near the singularities of the hyperspherical coordinates?
- The authors have presented generated images only on MNIST, a relatively simple dataset that does not require a high-dimensional latent space to capture its features. As a result, introducing additional constraints in the latent space does not appear to limit its capacity to represent information. However, with more complex datasets, how can these constraints affect the expressivity of the model given that the representations tend to overlap (as stated in Figure 1)? 
- Comparing the results in Figure 2 is challenging because the configurations (dimensionality of the latent space) are positioned at different points (not aligned). Consequently, it is difficult to determine in which configurations or regimes the VAE with hyperspherical coordinates surpasses the vanilla VAE and vice versa.
- In section 4.4, the authors generate new data sampling from a von Mises–Fisher distribution with the same mean and covariance as the ones empirically calculated from the latent embedding of the full test dataset. What is the motivation to use the empirical statistics of the test set instead of the training set for generation? 
- Could this method be extended/generalized to other distributions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the poor image generation quality of VAEs at inference time when the latent representation is high dimensional. After hypothesising, based on spin glasses theory from statistical physics, that the issue comes from the sparsity of high-dimensional spaces. Based on this, they propose to apply a mechanism akin to the quenching process used to reduce the entropy of such systems. Practically, this is done by implementing a change of coordinates from Euclidean to hyperspherical during the KL divergence computation and setting the priors of each dimension of these new coordinates such that the latent samples are pushed away from highly entropic regions. This results in an improved generation quality for MNIST while keeping latents that are interpretable enough to perform clustering.

### Strengths
Originality
========
- I like the creative approach of solving the issue of poor image quality generation by applying a solution to a similar problem from physics.
This is quite different from previous publications about hyperspherical VAEs, where the main motivation (as far as I know) was to provide a better prior than the standard multivariate Gaussian.
- The proposed model also differs from others in the hyperspherical VAE literature. Usually, changing the prior and posterior distribution can be complex as the reparametrisation trick and the KL divergence need to be updated accordingly. Here, the proposed solution is an elegant change of coordinates done after the reparametrisation trick during the KL divergence computation, making it easy to implement and intuitive to understand.

Quality/Clarity
===========
- The section on spin glasses is well vulgarised, intuitive, and reads very well for non-physicians.
- The paper is generally well-written and easy to follow.

Significance
=========
- Given the simplicity of the implementation, practitioners looking for better image generation quality with VAEs could easily adopt the proposed model.
- The explanation of why the generation is bad at inference time is interesting for the research community working on the learning dynamics of VAEs.

### Weaknesses
While I really like this paper's approach, I have some concerns about its empirical soundness and found several mistakes in the given equations (see major comments below). Clarifying some aspects of the paper would also strengthen it (see major and minor comments below). If these concerns were addressed, I would happily raise my score.

Major comments
=============

Experimental soundness
---------------------------------
- The experiment compares the results of $\beta$-VAEs with change of coordinates + annealing with the results obtained with $\beta$-VAEs without annealing. As a result it is not possible to see if the improved generation comes from the annealing or the change of coordinates. Additional results with $\beta$-VAEs using the same annealing schedule would be needed to ensure that the improvement is really due to the change of coordinates.
- While the experiment is partially done on CIFAR 10, it is hard to assess how several results generalise. For example, a comparison of the classification accuracy, examples of images generated, and a comparison of the projection into spheres using both models would be nice to have on CIFAR 10 as well.

Mathematical soundness
----------------------------------
In section 1.1, several equations were incorrect.
- In Eq. (1) $KLD(q_{\phi}(z) || p_{\theta}(z))$ should be  $KLD(q_{\phi}(z|x) || p_{\theta}(z))$
- In Eq. (2) the given formula is not for $KLD(z,\epsilon)$ but for $-KLD(z,\epsilon)$. Furthermore, subscripts from the summations are missing. I would suggest either removing the second summation and using a matrix form like $KLD(z,\epsilon) = \frac{1}{2} \sum^{N_b} \bigl(Tr(\sigma) + || \mu||^2_2 - \log det(\sigma) - n\bigr)$, or rewriting it with subscripts as  $KLD(z,\epsilon) = \frac{1}{2} \sum^{N_b} \sum_{k=1}^n \bigl(\sigma_i^2 + \mu_i^2 - \log(\sigma_i^2) -1 \bigr)$.
- In Eq. (3), this is not the ELBO $\mathcal{L}$ from Eq. (1) but its negative approximation $- \tilde{\mathcal{L}}$ which is minimised by the VAE. While the original formulation of VAEs by [1] does not contain a $\beta$ term and is equivalent to setting $\beta=1$, it would be interesting to briefly discuss what is the impact $\beta$ when $\beta > 1$ and when $\beta < 1$. Indeed, the motivation for both settings is very different: the first is to provide "disentangled representations" [2] and to force the VAE to learn in a polarised regime (a.k.a selective posterior collapse), which is akin to a PCA-like behaviour [3,4,5], while the second aims at mitigating posterior collapse and is often used together with annealing [6]. Thus, the choice of $\beta$ has a practical impact on the proposed experiment (see further discussion on the questions part below).

Clarity
---------
- To facilitate the understanding of the paper, it would be great to have the derivations from Eq. (4) to Eq. (5) and from Eq (8) to Eq (9) in appendix.


Minor comments
=============

Mathematical notation
------------------------------
The current notation is sometimes confusing. For example, l. 77 $\mathcal{N}(z; \mu, \sigma)$ reads as "the univariate Gaussian with mean $\mu$ and standard deviation $\sigma$" while it is in fact a multivariate Gaussian. A suggestion to improve this is to use a different notation for numbers, vectors, and matrices, following, for example the notation suggested in the math_commands.tex file of the ICLR template.

Clarity
---------
- l. 478, I found the sentence "the quality of AE and VAE [...]" confusing as AEs are not discussed anywhere else in the paper and are not used in the experiment. I would suggest removing the part about AE to make the argument clearer.
- I struggle to see what 32% of computation time of the KLD represent in term of additional training time. It would be easier to see with an average run time with and without change of coordinates over n seeds and k epochs. Furthermore, if this increases with the number of dimensions, an estimate of the increase rate using big O notation would be very useful for practitioners to assess whether this implementation is suitable to their needs.
- The seminal papers on VAEs are [1,7] which are different from the ones references. I would suggest updating this.

Typos
--------
- l. 91 weighs -> weights
- l. 100 teh -> "that the" ?
- l. 133 there's -> there is
- l. 133 have -> has
- l. 157 it's -> it is
- l. 422 gven -> given
- KL divergence is inconsistently refered to as "KL divergence" and "KLD" in the paper.
- l.591-592, the title of Higgins et al. is capitalised while others are not.

### Questions
- As mentioned in the weaknesses section, a VAE usually learns in a polarised regime when $\beta$ is sufficiently high. In this setting, the latent representations contain two kinds of variables: active and passive. The passive variables are kept as close to the prior as possible and used to lower the KL divergence, while the active variables contain the information needed for reconstruction (or further use in downstream tasks). Active variables typically do not follow the prior as the KL is kept low by the passive variables. Instead, they have a very low $\\sigma$ such that during the reparametrisation trick, $z \approx \\mu$. One would usually remove passive variables for downstream tasks, only keeping the small subset of variables containing some information [8]. I wonder if keeping only active variables would change the sphere projection to something more akin to what is obtained with hyperspherical coordinates?
- What is the impact of using different values of $a_{\mu, k}$ (keeping $a_{\mu, k} \neq 0$ of course)? Was there a specific reason to choose $a_{\mu, k}=1$?

References
=========
- [1] Kingma, D. P. and Welling, M. (2014). Auto-Encoding Variational Bayes. In International Conference on Learning Representations, vol. 2.
- [2] Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., Shakir, M. and Lerchner, A. (2017). $\\beta$-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. In International Conference on Learning Representations, vol. 5.
- [3] Rolinek, M., Zietlow, D. and Martius, G. (2019). Variational Autoencoders Pursue PCA Directions (by Accident). In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
- [4] Dai, B., Wang, Y., Aston, J., Hua, G. and Wipf, D. (2018). Connections with Robust PCA and the Role of Emergent Sparsity in Variational Autoencoder Models. Journal of Machine Learning Research, 19(41), pp. 1–42
- [5] Lucas, J., Tucker, G., Grosse, R. B. and Norouzi, M. (2019a). Don’t Blame the ELBO! A linear VAE Perspective on Posterior Collapse. In Advances in Neural Information Processing Systems, vol. 32.
- [6] Bowman, S. R., Vilnis, L., Vinyals, O., Dai, A., Jozefowicz, R. and Bengio, S. (2016). Generating Sentences from a Continuous Space. In Proceedings of The 20th SIGNLL Conference on Computational Natural Language Learning.
- [7] Rezende, D. J., Mohamed, S. and Wierstra, D. (2014). Stochastic Backpropagation and Approximate Inference in Deep Generative Models. In Proceedings of the 31st International Conference on Machine Learning, Proceedings of Machine
Learning Research, vol. 32.
- [8] Bonheme, Lisa, and Marek Grzes. "Be more active! understanding the differences between mean and sampled representations of variational autoencoders." The Journal of Machine Learning Research 24.1 (2023): 15423-15452.

### Soundness
2

### Presentation
3

### Contribution
3
