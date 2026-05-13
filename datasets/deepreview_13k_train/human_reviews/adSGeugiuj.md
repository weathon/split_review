# On the Posterior Distribution in Denoising: Application to Uncertainty Quantification

- Decision: Accept
- Scores: 8, 6, 3, 6

## Abstract
Denoisers play a central role in many applications, from noise suppression in low-grade imaging sensors, to empowering score-based generative models. 
The latter category of methods makes use of Tweedie's formula, which links the posterior mean in Gaussian denoising (\ie the minimum MSE denoiser) with the score of the data distribution.
Here, we derive a fundamental relation between the higher-order central moments of the posterior distribution, and the higher-order derivatives of the posterior mean. We harness this result for uncertainty quantification of pre-trained denoisers.
Particularly, we show how to efficiently compute the principal components of the posterior distribution for any desired region of an image, as well as to approximate the full marginal distribution along those (or any other) one-dimensional directions. 
Our method is fast and memory-efficient, as it does not explicitly compute or store the high-order moment tensors and it requires no training or fine tuning of the denoiser.
Code and examples are available on the project \href{https://hilamanor.io/GaussianDenoisingPosterior/}{website}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new method to compute posterior central moments of minimum mean squared error (MMSE) estimates from observations contaminated by additive white Gaussian noise. Then, this theoretical development is used to obtain uncertainty estimates in the context of image denoising. The method is cleverly adapted to the case where the denoiser is a black box (e.g., a neural network) only requiring forward passes through it, rather than back-propagation to compute derivatives exactly.

### Strengths
The method proposed in the paper is a relevant contribution to the important problem of estimating uncertainty in high-dimensional estimation problems, in this case, in image denoising from additive white Gaussian noise. The paper is very well written, with very precise and clear notation, and is a pleasure to read. The graphical illustrations of the results are very clear and useful and the experiments are also well presented, although not as impactful, as the variations depicted are very subtle.

### Weaknesses
The paper does not have, in my opinion, any major weaknesses, although a few minor things could be improved.

When the authors first mention denoising (second line of the introduction), they cite a couple of papers, the oldest of which is from 2017. This may give the wrong idea that image denoising started in 2017, when in fact it is arguably the oldest and longest-standing problem in image processing, going back at least to the 1960s. More classical references should be mentioned here, rather than just a couple of recent deep-learning-based methods. 

There are two common meanings for "score": gradient of the log-likelihood w.r.t. the parameters (more common in statistics) or w.r.t. the observations (more common in machine learning). It would be nice to make clear that you're using the second one, to make sure that some statistician reading the paper doesn't get confused. 

Equation (1) is not a denoising problem; it is the observation model underlying a denoising problem. 

According to Efron (2011), Tweedie's formula was derived by Robbins in 1956, which predates Miyasawa (1961). 

Notice that the first equality in Equation (4) is basically equivalent to Equation (2.8) in the paper by Efron (2011).

Minor typos: "memory efficient" -> "memory-efficient"; "...which connects between the MSE-optimal denoiser and the score function of noisy signals" -> "...which connects the MSE-optimal denoiser with the score function of noisy signals"; "...the most well known ..." -> "... the best known ..." or "...the most well-known ...".

### Questions
I have no questions.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Motivated by the recent success of using deep denoisers as priors (e.g, PnP and score matching),  this paper conduct connections between posterior central moments and the derivatives of posterior mean in a g higher order and recursive manor within the context of AWGN denoising. Then such conduction is applied for denoising  uncertainty visualization on multiple image datasets.

### Strengths
1)	The paper is well organized and easy to follow. The demonstration proof about posterior central moments and directional projection in a recursion manner is well presented and informative.

2)	The intuitive of using higher order moments to approximate posterior distribution is overall interesting. 

3)	The linear approximation in Eq.15 seems to be effective to handle differentiation complexity for higher-order tensor.

4)	Finally, the paper has shown its potential for uncertainty visualization within the context of image Gaussian denoising.

### Weaknesses
1), This paper only considers AWGN removal, making its practical relevance to real-world denoising (e.g., Poisson, Laplacian, Speckle, etc) very limited. Moreover, it would be more interesting to show how this method can be applied to other imaging inverse problems like inpainting and super-resolution both empirically and theoretically. The current scope significantly restricts the impact of the work, as real-world noise is rarely purely additive white Gaussian. The lack of exploration into other noise models and inverse problems makes it difficult to assess the broader applicability of the proposed method.

2), At the same time, since the analysis is built on Gaussian distribution,  it is difficult to evaluate its theoretical contributions since the recurrence relation for the central moments of the Normal Distribution is somehow standard. The theoretical novelty is questionable because the core analysis relies on properties of Gaussian distributions, which are well-established. The paper does not adequately address the limitations of this assumption, especially when considering that the posterior distribution is not guaranteed to be Gaussian, even if the noise is.

3), In this paper, no baseline methods are compared against with. No quantitative results about the uncertainty calibration such as expected calibration error etc. are reported. The lack of comparison to existing uncertainty quantification methods makes it difficult to assess the effectiveness of the proposed approach. The absence of quantitative metrics for uncertainty calibration, such as expected calibration error, further weakens the evaluation. The paper needs to demonstrate that the proposed method provides better uncertainty estimates than existing approaches.

4), While the authors claim the ability to compute the principal components (PCs) of the posterior distribution for any specified image region, the implementation details remain unclear to me. Seems there are no clear connection between the PCs and image features. At least it is not controllable.

5), Figure 4, and Figure 5, the authors claims that the PCs show the uncertainty along meaningful directions. However, interpreting these findings remains challenging. Given that images often follow complex distributions, it's not evident how the curves presented by the authors establish a direct connection with changes in ground-truth geometric features.

6), The computational complexity should be reported in the revision.

7), More importantly, absolute error to the ground-truth should be also presented in Fig. 4 and Fig.5 to show that the uncertainty indeed can better reflect the restoration error.

### Questions
1), While the authors claim the ability to compute the principal components (PCs) of the posterior distribution for any specified image region, the implementation details remain unclear to me. Seems there are no clear connection between the PCs and image features. At least it is not controllable.

2), Figure 4, and Figure 5, the authors claims that the PCs show the uncertainty along meaningful directions. However, interpreting these findings remains challenging. Given that images often follow complex distributions, it's not evident how the curves presented by the authors establish a direct connection with changes in ground-truth geometric features.

3), The computational complexity should be reported in the revision.

4), More importantly, absolute error to the ground-truth should be also presented in Fig. 4 and Fig.5 to show that the uncertainty indeed can better reflect the restoration error.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors show that given a pretrained score-based model, they are able to approximate the higher-order moments of the posterior distribution of the unknown noise-free image given noisy image.

### Strengths
**Originality.** While authors provide theoretical results for higher-order moments, as they mention, the second order moment has already been used in the context of denoising uncertainty quantification.

**Quality and clarity.** The paper was not too hard to follow. There are a few typos and some sentences are not clear.

**Significance.** It is unclear what this approach brings to the table that was not possible with existing uncertainty quantification methods.

### Weaknesses
* $\sigma$^2 not defined in Eq. 4.

* This particular method for image denoising uncertainty quantification is not motivated. Why would one use this approach? Why not just write down the posterior distribution using a likelihood model and the pretrained score-based model as (log) prior and use MCMC? Why not use amortized Bayesian inference and just simply sample from the posterior distribution?

* Related to the previous point, a lot of emphasize has been given to higher-order moments of the posterior. Why do we care about computing these? Can't we compute these quantities using samples from the posterior distribution?

* How would one use this method when the noise level is unknown?

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A method is proposed to quantify uncertainties when solving denoising problems with data-driven pre-trained denoisers.  The high-order central moments of the target posterior distribution are related to higher-order derivatives of its mean.  For high-dimensional problems the top eigenvectors of the posterior covariance are computed to capture the main modes of variation for uncertainty visualization.  Experiments are presented to demonstrate application of the method on a number of data-sets.

### Strengths
For denoising problems, denoisers implicitly encode a posterior for the data on which they are trained, which is related to the denoiser through Tweedie's formula.  Tweedie's formula explicitly relates the first posterior moment to the score of the data.  Similar relations hold for higher order momements of the posterior and higher order scores.  These expressions are presented in Theorem 1 and 2, which are proved in the appendices.  For high dimensional problems (e.g. imaging), computing these terms directly is not computationally feasible.  Instead the top eigenvectors are computed by the subspace iteration method.  These eigenvectors are then used to visualize the main modes of variation in the posterior.  The method requires only a pre-training denoiser and forward evaluations of the denoiser, avoiding any need for additional training.  It is fast and memory efficient and so suitable for high-resolution images.

### Weaknesses
While the methodology introduced in is very nice, the uncertainty quantification visualizations presented are a little underwhelming. The MNIST example (Fig. 4) clearly highlights the merit of the approach, where different potential modes of a 9 or 4 are apparent. However, for the experiments performed on natural images (e.g. Fig. 5), it is difficult to distinguish much variation in the images. I had to really zoom into these images to see the changes that are highlighed by the annotated arrows. However, I suppose the eigenvectors themselves may be a more useful visualization aid since it is more clear what structure of the image changes. Nevertheless, the difficulting in distringuishing changes in the modified images may limit the practical application of the method proposed.

### Questions
Is there any way to create modified images that more clearly show uncertainties?  I suppose increasing the scaling of the eigenvalue could be considered, although this is not very well motivated.  It might also be interesing to consider adding multiple eigenvectors at once, to show the mutliple modes of variation at once, rather than just one mode at a time.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
