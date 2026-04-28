# Counterfactual Generative Modeling with Variational Causal Inference

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
Estimating an individual's potential outcomes under counterfactual treatments is a challenging task for traditional causal inference and supervised learning approaches when the outcome is high-dimensional (e.g. gene expressions, facial images) and covariates are relatively limited. In this case, to predict one's outcomes under counterfactual treatments, it is crucial to leverage individual information contained in its high-dimensional observed outcome in addition to the covariates. Prior works using variational inference in counterfactual generative modeling have been focusing on neural adaptations and model variants within the conditional variational autoencoder formulation, which we argue is fundamentally ill-suited to the notion of counterfactual in causal inference. In this work, we present a novel variational Bayesian causal inference framework and its theoretical backings to properly handle counterfactual generative modeling tasks, through which we are able to conduct counterfactual supervision end-to-end during training without any counterfactual samples, and encourage latent disentanglement that aids the correct identification of causal effect in counterfactual generations. In experiments, we demonstrate the advantage of our framework compared to state-of-the-art models in counterfactual generative modeling on multiple benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies counterfactual generative modeling in terms of neural variational causal inference. The authors claimed that they proposed a new VAE formulation for this purpose with fundamental changes and achieved latent disentanglement through distribution alignment. Several experiments are conducted to demonstrate the author's claim.

### Strengths
The work is theoretically grounded.

### Weaknesses
The manuscript should properly discuss the previous works, such as CEVAE, in the main paper.

Figure 1 could be more specified with additional links that indicate the inference network in the VAEs.

If the proposed method has novelty or contribution in terms of latent identifiability and disentanglement, appropriate experiments should be conducted with fair comparison against the works within such sub-fields.

What I am concerned about is the following. I found that this paper is an extension of a workshop paper where some theoretical results and experimental results are almost duplicated from the previous version. While the recent AI community is rapidly growing and being generous in such situations, I don't think this is the right direction for the development of academia.

### Questions
None

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies counterfactual generation through a newly proposed variational inference paradigm specific to causal models. The proposed Variational Causal Inference (VCI) framework considers the generation of counterfactual outcomes relying on the consistency assumption, where potential outcomes and the true outcomes are the same under a counterfactual treatment. The authors propose a data-generating process from a counterfactual perspective where the latent variables derived from covariates, treatment, and outcome are aligned with latent variables derived from counterfactual outcomes. Utilizing the new counterfactual formulation, an appropriate variational lower bound is derived. The authors show theoretical identifiability guarantees of the proposed formulation. Empirical results show the effectiveness of the VCI framework in generating accurate counterfactuals.

### Strengths
- Overall, I believe this work sets forth a very interesting formulation for counterfactual inference in generative models and criticizes the use of conditional generative models for counterfactual generation.
- The VCI framework is formulated well and the consistency assumption to ensure counterfactuals keep individual components of the factual but also reflect changes according to a treatment is intuitive.
- The theoretical results for ELBO derivation, identifiability, and disentanglement further strengthen the paper and properly contextualize the work within the broader literature of causal generative models.
- The empirical results show the capability of the proposed framework to generate accurate counterfactuals on several datasets including image and single-cell perturbation datasets.

### Weaknesses
 - It seems that the Effectiveness metric from [1] is utilized through the MAE, where an anti-causal predictor is trained to predict the values of thickness and intensity, and a counterfactual reconstruction is fed in for evaluation. I believe this to be a sound metric. However, I do not think the MSE between the true and generated images is necessarily a good metric to evaluate the quality of the counterfactual. The MSE evaluates a pixel-wise similarity between the two images. However, in a counterfactual, the changes are more in the abstract variables describing the image. Specifically, MSE is highly sensitive to minor pixel shifts or noise, which may not reflect meaningful differences in the counterfactual generation. A counterfactual should ideally preserve the exogenous noise while only altering the features affected by the intervention, and MSE does not capture this nuance well.
- Although there are theoretical intuitions for disentanglement, there is no strict evaluation of the latent disentanglement of z. The DCI metric [2] evaluates the level of one-to-one correspondence between latent factors and the ground truth generative factors. I am not sure if this metric applies in evaluating disentanglement between z and the treatment variable t, but it would certainly be good to use a similar metric (perhaps Mean Correlation Coefficient) to evaluate disentanglement. The current evaluation lacks a quantitative measure of how well the latent space separates the treatment-related factors from the treatment-agnostic factors, which is crucial for the validity of the proposed approach.
- There does not seem to be any explicit modeling of causal mechanisms in the proposed framework. For example, the causal graph thickness → intensity can be imposed on the MorphoMNIST dataset. Previous work, such as DeepSCM, CausalHVAE, and CausalDiffAE, explicitly model the causal mechanism between the two variables. For systems with complex causal relations, can the proposed framework model the causal mechanisms? The lack of explicit causal modeling raises concerns about the framework's ability to handle more complex scenarios where the causal relationships are not as straightforward as in the MorphoMNIST dataset.
- The notion of disentanglement in this work is quite different than in disentangled representation learning from non-linear ICA based approaches. If T is observed, what is the intuitive meaning behind disentangling the latent factors Z from T? It is not clear to me why enforcing the latent space loss yields a disentangled objective. The paper needs to provide a more intuitive explanation of how the latent space loss leads to disentanglement between the latent representation and the treatment variable, especially given that the treatment variable is observed.

### Questions
- There does not seem to be any explicit modeling of causal mechanisms in the proposed framework. For example, the causal graph thickness → intensity can be imposed on the MorphoMNIST dataset. Previous work, such as DeepSCM [3], CausalHVAE [4], and CausalDiffAE [5], explicitly model the causal mechanism between the two variables. For systems with complex causal relations, can the proposed framework model the causal mechanisms?
- The notion of disentanglement in this work is quite different than in disentangled representation learning from non-linear ICA based approaches. If T is observed, what is the intuitive meaning behind disentangling the latent factors Z from T? It is not clear to me why enforcing the latent space loss yields a disentangled objective.

[3] Pawlowski et al. Deep Structural Causal Models for Tractable Counterfactual Inference. NeurIPS 2020.
 
[4] Ribeiro et al. High Fidelity Image Counterfactuals with Probabilistic Causal Models. ICML 2023.

[5] Komanduri et al. Causal Diffusion Autoencoders: Toward Counterfactual Generation via Diffusion Probabilistic Models. ECAI 2024.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
A framework is presented in which a counterfactual observation is estimated via a new variational formulation, in which the observed outcome and treatment are used within the conditional distribution for the unobserved (counterfactual) data. Experiments are presented on a range of applications, from biology to various types of images, with impressive quantitative performance.

### Strengths
The formulation is sound.  Figure 2 is particularly helpful in explaining the model and setup.

### Weaknesses
While the formulation is sound, the terminology of "causal reasoning" is questionable. One could argue that you are performing imputation of missing data, and then conditioning on the observed data makes complete sense. The criticism of the CEVAE is inappropriate, because they are solving a very different problem (traditional causal inference), and they do not condition on specific observations (the predictions are not "personalized"). It is ok to comment on and compare to CEVAE, but the setup and assumptions are different.

Another weakness, commented on below, is the presentation. The paper could be much better written, and thereby easier for the reader. Details below.

In the beginning of Sec. 2.1, \Omega, \mathcal{Y}, \Sigma_Y, \mathcal{X}, \Sigma_{\mathcal{X}}, etc are not defined. This notation is unclear, and not clear why it is needed.

On p. 3, Assumptions 1 and 2, Remarks 1 and 2 are mentioned. The reader is very confused. None of these have been mentioned thus far, and the reader is not told such details are in the Appendix. This is unnecessarily confusing. By ICLR guidelines the main paper should be self contained. It is not.

On p. 3 it seems you use the adversarial discriminator D(X,T,Y) to manifest the loss. This seems ad hoc. The adversarial discriminator has a connection to the loss, but this is a surrogate and it is not particularly justified. I can see how it might work in practice, but this is an important point that deserves more discussion.

In (3), there is inconsistency in using upper case letters (Z for example) and lower case letters (e.g., z) for random variables. The way (2) useses notation on upper/lower case variables is not consistent with (3).

Does this really have to be framed as causal analysis? Why is it not just imputation of missing (counterfactual) data? I understand why you want to connect to methods like CEVAE, but they are doing something very different, and hence it seems unnecessary.

### Questions
1. In the beginning of Sec. 2.1, \Omega, \mathcal{Y}, \Sigma_Y, \mathcal{X}, \Sigma_{\mathcal{X}}, etc are not defined. This notation is unclear, and not clear why it is needed.

2. On p. 3, Assumptions 1 and 2, Remarks 1 and 2 are mentioned. The reader is very confused. None of these have been mentioned thus far, and the reader is not told such details are in the Appendix. This is unnecessarily confusing. By ICLR guidelines the main paper should be self contained. It is not.

3. On p. 3 it seems you use the adversarial discriminator D(X,T,Y) to manifest the loss. This seems ad hoc. The adversarial discriminator has a connection to the loss, but this is a surrogate and it is not particularly justified. I can see how it might work in practice, but this is an important point that deserves more discussion.

4. In (3), there is inconsistency in using upper case letters (Z for example) and lower case letters (e.g., z) for random variables. The way (2) useses notation on upper/lower case variables is not consistent with (3).

5. Does this really have to be framed as causal analysis? Why is it not just imputation of missing (counterfactual) data? I understand why you want to connect to methods like CEVAE, but they are doing something very different, and hence it seems unnecessary.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This article presents a variational inference model specifically designed for counterfactual generation, motivated by the goal of extracting information contained within high-dimensional potential outcomes. This concept is intriguing, and the relevant experiments demonstrate the efficacy of the proposed method.

### Strengths
1.	The article tackles a vital issue in counterfactual generation, contributing meaningfully to the understanding of causal relationships in diverse fields.

2.	The focus on high-dimensional potential outcomes offers a reasonable angle, as it may capture complexities that traditional methods might miss, thus enhancing counterfactual generation.

3.	The experimental outcomes appear encouraging, indicating that the proposed model effectively supports counterfactual generation.

### Weaknesses
1.	The article does not provide asymptotic experiments to assess the performance of the proposed ELBO, which limits the understanding of its behavior as the sample size increases and may raise questions about its robustness in practical applications.

2.	The absence of a comparison between Morpho-MNIST and diffusion model-based counterfactual generation models Diff-SCM undermines the evaluation's robustness, making it difficult to assess the proposed model's effectiveness relative to state-of-the-art methods and diminishing its perceived impact within the field.

### Questions
1.	I don’t quite understand the sentence “hence preserving maximum individuality yet minimum treatment characteristics in counterfactual construction  g_theta(y, t')  during inference.” Could you explain it in more detail?

2.	L841. I have some questions regarding this statement. Why do you think that the performance of intervening with digits cannot be assessed? In fact, I find that evaluating the counterfactual performance of intervening with digits is more intuitive. I am also looking forward to seeing how your model performs with digit interventions.

3.	In your paper, you discuss the introduction of a novel ELBO. I am curious about its properties in terms of tightness. Specifically, how does this new lower bound compare to existing bounds in the literature? Additionally, what methods or analyses have you employed to assess its tightness, and how might this impact the overall performance and effectiveness of your model?

### Soundness
3

### Presentation
3

### Contribution
3
