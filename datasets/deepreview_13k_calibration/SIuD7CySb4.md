# High-Dimensional Bayesian Optimisation with Gaussian Process Prior Variational Autoencoders

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5

## Abstract
Bayesian optimisation (BO) using a Gaussian process (GP)-based surrogate model is a powerful tool for solving black-box optimisation problems but does not scale well to high-dimensional data. Previous works have proposed to use variational autoencoders (VAEs) to project high-dimensional data onto a low-dimensional latent space and to implement BO in the inferred latent space. In this work, we propose a conditional generative model for efficient high-dimensional BO that uses a GP surrogate model together with GP prior VAEs. A GP prior VAE extends the standard VAE by conditioning the generative and inference model on auxiliary covariates, capturing complex correlations across samples with a GP. Our model incorporates the observed target quantity values as auxiliary covariates learning a structured latent space that is better suited for the GP-based BO surrogate model. It handles partially observed auxiliary covariates using a unifying probabilistic framework and can also incorporate additional auxiliary covariates that may be available in real-world applications. We demonstrate that our method improves upon existing latent space BO methods on simulated datasets as well as on commonly used benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Bayesian Optimization is a class of methods for optimizing expensive black box functions $f:\mathbb{R}^d \to \mathbb{R}$ typicality for low dimensional search spaces $d<10$.

In the high dimensional case (e.g. $d>100$) such as the space of images, if we have access to an unlabelled dataset of points in the search space, in this work denoted $y_1,...,y_N \in \mathbb{R}^d$, one may first train a variational autoencoder to map from the high dim search space to a low dim latent space $q:\mathbb{R}^d \to \mathbb{R}^L$ and back $p:\mathbb{R}^L \to \mathbb{R}^d$ where $L<<d$ (simplifying  notation somewhat). Then we simply use $z=q(y)$ and $y=p(z)$ as intermediate translation layers mapping between high and low dimensional spaces. BO is performed in the low dimensional space, modelling a dataset of points $\\{z_i, f(p(z_i))\\}$ with a GP and optimizing the acquisition function over $z\in\mathbb{R}^d$, meanwhile the objective function is evaluated in the high dimensional space $f(p(z))$.

This work considers the case where we have even more data available for some or all of the points in search space denoted $(x_i, y_i) \in \mathcal{X}\times \mathbb{R}^D$ with $\mathcal{X} \subset \mathbb{R}^k$ where $k < 10$. In such a case, we have a regression dataset with low dim inputs and high dim outputs, we may use the GP-VAE architecture. As above with BO, we use the VAE function $z=q(y)$ to convert all the $y_i$ values to low dimensional and now we have a dataset $(x_i, z_i)$ which we can use for normal GP regression, mapping from $x$ to $z$.

### Strengths
- __impactful problem__ high dimensional BO and VAE-BO are large problems, and the case where we have extra "meta-data" for points in the high dim search space seems perfectly reasonable and impactful (and surprising it hasn't been considered seriously until now)
- __nice architecture__ the combination of GP-VAE and VAE-BO seems like an intuitive and good choice for such a problem.
- __good benchmarks__ a toy example with MNIST images, mathematical expression tuning and molecule tuning, while the MNIST example  is rather artificial, I felt the molecule example really highlighted the benefit of incorporating covariates.
- __accounting for missing data__ the authors also integrate previous approaches that handle missing data, although this is not novel in this work it is a nice to have and demonstrates broader practicality.

### Weaknesses
## Technical Comments
- __Trip 2021 baseline__ is this baseline with weighted retraining or not? It weould be nuice to see a vanilla VAE-BO approach as well as the method of Tripp 2021 with weighted retraining.
- __preference for high valued $y$__ The method of Trip et. al. 2020. starts with a VAE that is a generative model of the whole search space (on a high dim manifold) and after collecting a few fitness values, gradually retrain the VAE to become a generative model of high value parts of the search space, conceptually similar to CMA-ES or a trust region approach. In my view, this method has a nice intuition. In contrast with the above point, I may have misunderstood however it appears as though the proposed ELBO for GP-VAE with missing data does not have a bias for learning high valued $y$.
- __learning without covariates possible failure mode__ when there are no extra covariates beside fitness values $c$, there are two GPs in the latent space,
  - the first GP within the BO algorithm maps from latent points to fitness, modelling $\hat{f}(z): \mathbb{R}^L\to\mathbb{R}$,  
  - the second GP maps from fitness back to latent $q(z|c):\mathbb{R}\to\mathbb{R}^L$.

  in a normal BO setting (e.g. VAE encoder and decoder are identity functions) I find this very counter-intuitive, the inverse GP must learn to map from a scalar value $c$ to all the points $\{z|\hat{f}(z)=c\}\subset\mathbb{R}^L$, the level set of $c$ for multi-modal function, and this is being modelled by a single uni-modal Gaussian distribution. I have not seen this in the BO literature and it is not immediately obvious why such an approach would help. With _extensive_ retraining the latent space can be remoulded so that the level sets are clustered but this is speculative.

- __limitations__ I may have missed this, but I there does not seem to be much discussion of failure cases and limitations, I have mentioned one above. As with any method that allows to incorporate more data/complexity also allows for more ways to break, if the $x_i$ values are pure noise or if all the optimal $y_i$ points happen to have dramatically different $x_i$ values. The paper does not seems to expose any failure modes or warning for users.

## Minor Comments
- __background__ the proposed method is an intelligent combination of prior methods, and much of section 4 (all of 4.1, 4.2 and parts of 4.3) are describing such prior works and may arguably belong in section 3.
- __section 4.3__ I found this section to be a little bit dense and confusing, adding "yet another" distribution over $x$ (which conditions $z$ which conditions $y$). Although handling missing data is nice and shows practicality, moving this to the appendix as a "bonus feature" and using the space to provide more intuition and justification for the benefit of the main method might be better.

### Questions
- is it possible to include Trip 2021 as a baseline with and without retraining?
- what is the intuition that means training the GP-VAE would improve the outer BO modelling? Whiles integrating more data can helpat is the justification for the main hypothesis?
- can the autrhors

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
&nbsp;

The authors propose a novel VAE-based Bayesian optimization (VAE-BO) scheme that makes use of a Gaussian process prior VAE to leverage auxiliary covariates in learning a latent space that is better suited for Bayesian optimization. The method is evaluated against several baselines on synthetic data as well as the penalized logP molecule generation benchmark. While the framework is novel and interesting, I have some concerns about the empirical evaluation of the method as well as the reproducibility of the results. In relation to the empirical evaluation, the use of additional covariates that are correlated with the objective would appear to be biased if the baseline methods are not supplied with these covariates. Additionally, I have questions about the discrepancy between the LOL-BO optimization trace reported in the original paper [19] for penalized logP and the trace reported in the current paper. If these issues can be addressed in the rebuttal I will be happy to increase my score.

&nbsp;

### Strengths
&nbsp;

1. The work proposes a principled probabilistic framework for VAE-BO leveraging GP prior VAEs to enable conditioning on auxiliary covariates. The scheme is highly general and may be used in conjunction with many disparate VAE-BO architectures.

2. The paper is exceptionally well-written and presented and the scholarship is excellent (an example of which is tracing back the ideas of label guidance to construct discriminative latent spaces to Urtasun et al. 2007).

3. The empirical results are impressive pending the clarifications below as well as the release of the code.

&nbsp;

### Weaknesses
 
**MAJOR POINTS**

1. It would be great to perform diagnostic experiments on the GP surrogate fit on the latent space as in Grosnit et al. 2021 [16] in order to validate that improved BO performance is achieved due to a better GP fit on the latent space. Specifically, assessing the GP fit via log likelihood on holdout data would provide strong evidence for the mechanism by which the GP prior VAE approach benefits VAE-BO by aiding the construction of a more discriminative latent space.

2. On lines 468/469, the authors state, "We augmented the ZINC-250K with five additional covariates: molecular weight, number of hydrogen donors, number of hydrogen acceptors, number of rotatable bonds, and total polar surface area.". Are all baseline methods given access to these covariates? These additional descriptors are highly correlated with the water-octanol partition coefficient logP and so for fair comparison, I would expect that all methods be able to make use of these features in some fashion? It would be great if the authors could clarify exactly how these additional covariates are used for each method. A straightforward, principled, and fair approach for existing methods to leverage such descriptors (covariates) would simply be to incorporate them as part of the initial, un-encoded molecular representation x. This would necessitate a VAE architecture to operate on mixed continuous/discrete (heterogeneous) molecular featurizations. An advantage of the authors' approach is that they can leverage additional covariates without requiring a VAE architecture for heterogeneous data. The authors should not attempt to obfuscate the utility of this comparison. The improved performance of the authors' method with "auxiliary covariates" is likely due to incorporating molecular descriptors that are correlated with the objective. In principle, the baseline methods could also consider such covariates through the design of a VAE architecture for heterogeneous data.

3. The results reported in Figure 1 of the LOL-BO paper [19] are vastly at odds with the optimization trace reported for LOL-BO in Figure 5b) of the current paper. Why is this the case?

4. The authors do not appear to have released the code for the submission and hence I have some concerns over the reproducibility of the results. This could be supplied as an anonymous GitHub link during the rebuttal phase.

**MINOR POINTS**

1. There are some missing capitalizations in the references e.g. "Gaussian" and "Bayesian".

2. When introducing Bayesian optimization, it may be worth citing the originating papers for the method [1, 2] as discussed in [3].

3. The statement that, "Although BO offers an approach for black-box optimisation problems, it does not efficiently scale to high-dimensional data settings" should probably be expanded on in light of recent work [4] which demonstrates that a vanilla GP surrogate where the lengthscale prior is scaled with the dimensionality of the problem can perform effective Bayesian optimization in 100s of dimensions.

4. In terms of the references for applications of VAE-BO, Felton et al. 2020 use a multitask GP surrogate for Bayesian optimization over chemical reaction conditions (as opposed to chemical synthesis) and hence do not make use of a VAE-BO scheme. Additionally, Shields et al. use Bayesian optimization for chemical reaction conditions (as opposed to chemical synthesis) but do not use VAE-BO. Korovina et al. 2020 similarly do not use VAE-BO but rather define an optimal transport kernel directly over molecules. They do however consider chemical synthesis.

5. In Figure 1, the task is articulated as discovering novel drug-like molecules. The penalized logP objective function, however, does not optimize for drug-likeness as noted in e.g. Section 5 of [5]. The penalized logP objective introduced in [6] is misspecified as a metric for drug-likeness since it attempts to maximize logP. For drug-like molecules the logP should however lie within the range of -0.4 to 5.6 according to the commonly-used heuristic Lipinski Rule of 5. As such, I would recommend rephrasing the task to molecule optimization or something comparably generic.

6. In the related work, there has been limited empirical evidence that VAE-BO is beneficial in continuous high-dimensional spaces. In particular, techniques such as random embeddings [7] or SAASBO [8] or more well-known methods. VAE-BO however, has been demonstrated to help in applying Bayesian optimization over structured input spaces such as molecules, images, and biological sequences. As such, it may be worth rephrasing the discussion to focus slightly more on the structured nature of the input spaces as opposed to the dimensionality.

7. The related work does a very good job at covering the majority of VAE-BO methods. Some works that should also be mentioned are [9-12]. Additionally, [13] does not yet appear to be formally published but would be worth mentioning once it is.

8. The citation to Urtasun et al. 2007 shows great scholarship in tracing back the ideas underpinning VAE-BO. Additionally, it would be worth citing Jasper Snoek's PhD thesis [14] which also contained early ideas on label guidance to construct discriminative latent spaces.

9. The decision to use the variable y to represent a high-dimensional observation is somewhat confusing. It may be better to use this variable to represent (noisy) observations of the objective function f.

10. On line 163, it may be worth clarifying the training time complexity is O(N^3).

11. It would be worth citing UMAP [15] given that it is used.

12. Reference [17] should be cited when introducing the Quantitative Estimate of Drug-Likeness (QED) metric.

13. In Figure 5a) it may be worth plotting the log regret to see a clearer distinction between the methods.

14. It would be worth citing t-SNE [18] given that it is used.

15. Reference [20] should be cited when introducing Expected Improvement (EI) as discussed in [3].

16. When discussing Adam in Section C of the appendix it may be worth mentioning that it is an amalgam of the momentum and RMSProp optimizers.


### Questions
&nbsp;

1. My main question relates to how the additional covariates are used for each method. I would be very grateful if the authors could expand on this aspect of the empirical evaluation.

2. For future work the authors may wish to consider the inversion problem [13] namely that under the mapping x -> z -> x' there is typically a reconstruction gap meaning that x is not equal to x'. Enforcing invertibility has been shown in some recent papers to improve VAE-BO performance systematically across architectures. This being said, the contribution is somewhat orthogonal to the contribution of the current work. I believe approaches such as deep metric learning as the authors have compared against are indeed the most appropriate baselines.

&nbsp;

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel approach to Bayesian optimization (BO) that addresses high-dimensional data incorporating auxiliary covariates, even when some of the covariates contain missing values.  The method builds upon a variational autoencoder (VAE) where the latents follow a Gaussian Process (GP) prior. The approach is technically sound, and the experimental results show its effectiveness in both synthetic and real-world settings.

However, the paper's novelty is somewhat limited, as it builds on existing GP prior VAE models with missing covariates. Furthermore, the absence of a key baseline in one of the experiments raises concerns about the completeness of the experimental evaluation. Addressing these issues—especially by adding the missing baseline—would make a stronger case for the proposed method.

If the authors include this baseline in the first experiment and their method shows significant improvements (or they provide a justified reason for its absence), I would be inclined to increase my evaluation score from a weak reject to a weak accept.

### Strengths
**1. Clarity and Readability:** The paper is well-structured and clearly written. The authors explain complex ideas in an accessible way, ensuring that the technical details are easy to follow. I am not an expert for BO but could get a good understanding of the paper within a few hours. 

**2. Technical Rigor:** The paper is technically solid. The authors carefully describe the underlaying probabilistic model step-by-step. The integration of auxiliary covariates, even when some values are missing, is handling in a principled manner by applying variational inference. 

**3. Experimental Thoroughness:** The experiments are in general carefully executed. This was the part of the paper that I enjoyed reading the most. They span multiple datasets from different domains and the results are studied in-depth.

### Weaknesses
 **1. Limited Novelty:** While the application of the GP prior VAE to Bayesian optimization is novel, the underlying model itself—GP prior VAE with partial observations —has been published previously in Ramchandran et al. (2024). This implies that the core contribution of the paper lies primarily in applying the method to the BO context. This limits the overall novelty of the work.

**2. Competitive/Missing Baselines:** The method LOL-BO (Maus et al., 2022) shows competitive performance on the expression reconstruction dataset, and is only marginally outperformed on the molecular optimization experiment. However, in the first experiment on synthetic data, I found this method missing. It is important for the authors to include this baseline in this experiment to ensure a fair comparison. If their approach significantly outperforms this baseline, it would strengthen the contribution. If there is a specific reason why this approach cannot be applied for this experiments, it needs to be stated more clearly in the paper.

**3. Scalability Dependency:** The scalability of the method relies on leveraging sparse Gaussian Process (GP) techniques, using inducing points to approximate the GP. However, selecting meaningful inducing points becomes challenging when the dataset changes over time, as it is the case in BO applications. As new data arrives, it is unclear how to update the inducing points in a principled and computationally efficient manner. This is a critical issue for ensuring that the model scales well over BO iterations, and the paper should at least discuss this problem.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
