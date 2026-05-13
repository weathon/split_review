# CardiCat: a Variational Autoencoder for High-Cardinality Tabular Data

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
High-cardinality categorical features are a common characteristic of mixed-type tabular datasets. Existing generative model architectures struggle to learn the complexities of such data at scale, primarily due to the difficulty of parameterizing the categorical features. In this paper, we present a general variational autoencoder model, CardiCat, that can accurately fit imbalanced high-cardinality and heterogeneous tabular data. Our method substitutes one-hot encoding with regularized dual encoder-decoder embedding layers, which are jointly learned. This approach enables us to use embeddings that depend also on the other covariates, leading to a compact and homogenized parameterization of categorical features. Our model employs a considerably smaller trainable parameter space than competing methods, enabling learning at a large scale. CardiCat generates high-quality synthetic data that better represent high-cardinality and imbalanced features compared to competing VAE models for multiple real and simulated datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to address the generation of high-cardinality tabular data by proposing CardiCat, a variational autoencoder (VAE) model that employs regularised dual encoder-decoder embedding layers.

### Strengths
1. The paper is generally well-written.
2. The authors follow consistent notations throughout the paper.
3. The code is provided.

### Weaknesses
 **1. [Important] Seemingly inaccurate claim of contribution.** CardiCat does not seem to be the first to employ dual embeddings in tabular data generation. I would suggest the authors refer to some recent papers, like TabSyn [1], where the VAE is equipped with a trainable tokeniser as 1. CardiCat.

**2. [Important] Incomprehensive comparison to benchmark methods.** The paper seems to only include some conventional VAE and GAN methods for comparison. However, there has been some recent work on generating tabular data with mixed types [1]. I would suggest the authors refer to them and at least include some of the recent methods for a more general comparison.

**3. [Important] Evaluation metrics are not comprehensive.** Following the above concern on benchmark methods. Usually, it would be insufficient and inconclusive to only evaluate the generator with marginal and bi-variate statistical fidelity metrics. Please refer to the literature [2, 3, 4] for more indicative metrics like downstream performance and multivariate fidelity metrics.

**4. [Important] Unclear descriptions of conditional CardiCat.** And the corresponding results of conditional CardiCat seem missing in the paper.

**5. Code is a bit hard to go through.** I carefully checked the provided codebase. Although it is not necessary to have clear-to-read code for everyone, the current open-source version seems somewhat messy. One example is that the comments for functions remain unfinished: get_pred in src/postprocessing.py, the explanations of arguments are simply `_description_`. I would suggest the authors clean their codebase to save time for potential users.

### Questions
1. Why not treat binary features as categorical features?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, authors have proposed a new method called CardiCat that can accurately fit the imbalanced high-cardinality and heterogeneous tabular data. It employs a dual encoder-decoder embedding layers architecture and a customized loss function that computes the reconstruction in the embedding space. The model was tested on 8 datasets and showed a better performance compared to other methods.

### Strengths
The authors introduced a novel to fit the imbalanced tabular data. The paper is easy to follow and understand.

The results in the Table 2 shows better performance than other VAE based methods.

### Weaknesses
Lack of state-of-the-art comparative methods. Most of the comparative methods are methods before (vae, tvae) 2019, while the most advanced methods are necessary.

In Figure 3, the proposed model seems to have similar or worse performance than tGAN, especially for the marginal reconstruction. In Table 2, do you have any comparisons with tGAN?

The datasets do not seem to be high cardinality. What if the number of cardinalities is greater than the number of samples?

The evaluation metrics seem to be limited. Are there any experiments showing the generated data's performance?

### Questions
The datasets do not seem to be high cardinality. What if the number of cardinalities is greater than the number of samples?

The evaluation metrics seem to be limited. Are there any experiments showing the generated data's performance?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes CardiCat, a VAE-based generative model designed to handle high-cardinality categorical features in tabular data by using dual encoder-decoder embedding layers. The authors claim that this approach avoids the need for one-hot encoding, reduces the number of trainable parameters, and provides a compact parameterization that improves the model’s ability to capture complex dependencies. Empirical results indicate that CardiCat outperforms traditional VAE models and other baselines.

### Strengths
- The method addresses a well-known and relevant problem. 
- The structure of the paper is well-organized.

### Weaknesses
 - The contribution appears technically minimal or lacks sufficient justification.
- Certain theoretical aspects require further review and clarification.
- The related work section provides only a high-level overview and omits several relevant references.
- Additional baselines are needed to strengthen the empirical evidence supporting the contributions and demonstrate their significance.

### questions:
 ### Theoretical Issues

- The relevance of the proposed method is not entirely clear. VAEM individual VAEs already preprocess input data into a smooth latent space, and the posterior of the uni-dimensional VAEs can be seen as an embedding similar to CardiCat. Thanks to this, VAEM’s dependency model learns the inter-feature dependencies effectively. Notably, VAEM generalizes CardiCat by using a VAE framework, while CardiCat employs a simpler, deterministic autoencoder (AE) with regularization applied through a loss term. Why would CardiCat theoretically outperform VAEM? Line 160 references Section 4 for empirical justification, but this evidence is not provided.

- The authors claim that "This allows us to avoid altogether the need to one-hot encode the non-binary categorical features at any point in the process." However, the significance of avoiding one-hot encoding is unclear. With an appropriate design, VAEM, and possibly more recent methods for heterogeneous data [2-5], could potentially achieve comparable results while maintaining a similar parameter count as CardiCat.

- While the model is framed as a VAE adaptation, the reconstruction loss relies on mean-squared errors and cross-entropy rather than likelihoods, with added regularization terms. These modifications make the objective to diverge from the traditional ELBO used in VAEs. Although this optimization approach may still be effective (since the Gaussian pdf’s exponent is effectively a squared error weighted by variance), it deviates from a purely generative probabilistic model.

- In line 258, the likelihood is defined as a factorized Gaussian, which conflicts with the loss function described in Section 3.3.

- It is unclear how the decoded embeddings of categorical features are transformed back into parameters for categorical distributions.

- One of the strengths of VAEs is their ability to approximate likelihoods. How can likelihood approximations be evaluated within the proposed model?

- Technical inaccuracies:
  - Line 256: "parametrization" should be replaced with "reparameterization" [1].

### Experimental Issues

#### Baselines

- The baselines employed are insufficient and outdated, with the most recent comparison model dating back to 2020. Including the original VAE from 2014, which has limited value given the significant advancements in handling heterogeneous data, undermines the comparison. Why were recent methods [2-5] for heterogeneous missing data not considered as baselines? The comparison with tGAN is not adequately discussed in the text, and its relevance remains unclear.

### Minor Comments

- Typographical errors:
  - Quotation mark issues (e.g., lines 49 and 288).

### Questions
### Theoretical Issues

- The relevance of the proposed method is not entirely clear. VAEM individual VAEs already preprocess input data into a smooth latent space, and the posterior of the uni-dimensional VAEs can be seen as an embedding similar to CardiCat. Thanks to this, VAEM’s dependency model learns the inter-feature dependencies effectively. Notably, VAEM generalizes CardiCat by using a VAE framework, while CardiCat employs a simpler, deterministic autoencoder (AE) with regularization applied through a loss term. Why would CardiCat theoretically outperform VAEM? Line 160 references Section 4 for empirical justification, but this evidence is not provided.

- The authors claim that "This allows us to avoid altogether the need to one-hot encode the non-binary categorical features at any point in the process." However, the significance of avoiding one-hot encoding is unclear. With an appropriate design, VAEM, and possibly more recent methods for heterogeneous data [2-5], could potentially achieve comparable results while maintaining a similar parameter count as CardiCat.

- While the model is framed as a VAE adaptation, the reconstruction loss relies on mean-squared errors and cross-entropy rather than likelihoods, with added regularization terms. These modifications make the objective to diverge from the traditional ELBO used in VAEs. Although this optimization approach may still be effective (since the Gaussian pdf’s exponent is effectively a squared error weighted by variance), it deviates from a purely generative probabilistic model.

- In line 258, the likelihood is defined as a factorized Gaussian, which conflicts with the loss function described in Section 3.3.

- It is unclear how the decoded embeddings of categorical features are transformed back into parameters for categorical distributions.

- One of the strengths of VAEs is their ability to approximate likelihoods. How can likelihood approximations be evaluated within the proposed model?

- Technical inaccuracies:
  - Line 256: "parametrization" should be replaced with "reparameterization" [1].

### Experimental Issues

#### Baselines

- The baselines employed are insufficient and outdated, with the most recent comparison model dating back to 2020. Including the original VAE from 2014, which has limited value given the significant advancements in handling heterogeneous data, undermines the comparison. Why were recent methods [2-5] for heterogeneous missing data not considered as baselines? The comparison with tGAN is not adequately discussed in the text, and its relevance remains unclear.

### Minor Comments

- Typographical errors:
  - Quotation mark issues (e.g., lines 49 and 288).

[1] Kingma, Diederik P., and Max Welling. "Auto-encoding variational bayes." arXiv preprint arXiv:1312.6114 (2013).

[2] Ma, Chao, et al. "VAEM: a deep generative model for heterogeneous mixed type data." Advances in Neural Information Processing Systems 33 (2020): 11237-11247.

[2] Peis, Ignacio, Chao Ma, and José Miguel Hernández-Lobato. "Missing data imputation and acquisition with deep hierarchical models and Hamiltonian Monte Carlo." Advances in Neural Information Processing Systems 35 (2022): 35839-35851. 

[3] Antelmi, Luigi, et al. "Sparse multi-channel variational autoencoder for the joint analysis of heterogeneous data." International Conference on Machine Learning. PMLR, 2019.

[4] Gong, Yu, et al. "Variational selective autoencoder: Learning from partially-observed heterogeneous data." International Conference on Artificial Intelligence and Statistics. PMLR, 2021.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors focus on the design of a better variational autoencoder architecture and training objective for tabular data, CardiCat. Specifically, they focus on the challenging task of modeling high cardinality categorical features with class imbalance. The standard approach with one-hot encodings is very expensive, introducing many more parameters and therefore increasing sample complexity. The core technique of this paper is to substitute one-hot encoding with a low-dimensional embedding layer used in both the encoder and decoder. Then, the reconstruction loss for these features is computed with MSE in embedding space instead of using a cross-entropy loss in the raw label space. To prevent embedding collapse, the authors propose a variance-based regularization term. Small-scale evaluations demonstrate that CardiCat outperforms vanilla VAE baselines in recovering marginal and pairwise conditional distributions on a variety of tabular datasets.

### Strengths
* Well-motivated: The problem setting is important and underappreciated (VAEs for modeling heterogenous tabular datasets), so this work is well-motivated.
* Clear writing: The paper is well-written and contextualized well in the VAE literature.
* Correctness: All mathematical statements appear correct.
* Appears reproducible: The method is presented in enough detail that I believe it could be reproduced straightforwardly.

### Weaknesses
 *Unconvincing evaluations.*

My major concern is that (1) the CardiCat framework gives up on optimizing a variational lower bound of the log-likelihood, which makes model comparison far more challenging, and moreover (2) does not provide convincing surrogate evaluations for sample quality or diversity.

In particular, the CardiCat objective (L228) is no longer a valid ELBO, and therefore it is not possible for the authors to directly compare the ELBO of their model versus other VAEs. (Aside: this fact was obfuscated by the writing near L218-220, where it appeared that the objective is indeed a valid ELBO. I would urge the authors to edit this writing to make clear that the CardiCat objective is not an ELBO.)

It is OK to not use a likelihood-based model as long as the downstream evaluations of sample quality and diversity are convincing. My concern is that they are not. The authors report two main metrics: matching the marginals of each feature distribution and pairwise conditionals between features. I did not find this to be a realistic test of the sample quality and diversity of their model. I recognize that evaluation of non-likelihood-based generative models for tabular data is challenging (there are no standard metrics like FID), but I would have at least hoped the authors could test the quality of their learned representations for supervised tasks. The experiments leave me unconvinced that CardiCat actually models the joint distribution $p(x)$ better than the alternatives.

In addition, the evaluation is done on a very small scale. The authors mention that they intentionally use a simple setting for a more direct comparison to VAE---I was not very convinced by this. Ideally, one would compare directly against state-of-the-art methods at a reasonably large scale, perhaps using their architectures etc. and showing that the new contribution (the CardiCat dual embedding and regularizer) improves performance.

*Giving up ELBO seems unnecessary.*

I am not convinced that it is even necessary to give up the ELBO in order to avoid one-hot embeddings. For example, Plaid [1] is a diffusion language model which uses low-dimensional embeddings for categorical data and still preserves the ELBO objective, allowing direct model comparison with autoregressive and other generative models.

*Lack of motivation for regularization term.*
The embedding regularization term (L245) was a little surprising: it regularizes the sum of the variances? Why not compute the element-wise variances as $V_j({e_j})$ and $V_j({e^0_j})$ then have the regularization term be $||V_j({e_j}) - V_j({e^0_j})||^2_2$? I believe readers would appreciate some more motivation for this.

### Questions
I would be willing to improve my score if the authors could:
1. Demonstrate clearly why a likelihood-based objective is not reasonable, thereby justifying their non-likelihood-based objective which sacrifices direct model comparison with the ELBO.
2. Improve the writing around the objective (L218-220) to make clear that the CardiCat objective is not a bound of the likelihood (mentioned in Weaknesses above).
3. Expand the scope of their evaluations to larger-scale settings with other tests of model quality, such as joint sample quality / diversity or supervised probes on representations.

### Soundness
3

### Presentation
4

### Contribution
2
