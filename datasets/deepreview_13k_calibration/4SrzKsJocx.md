# Simultaneous Dimensionality Reduction: A Data Efficient Approach for Multimodal Representations Learning

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3

## Abstract
Current experiments frequently produce high-dimensional, multimodal datasets—such as those combining neural activity and animal behavior or gene expression and phenotypic profiling—with the goal of extracting useful correlations between the modalities. Often, the first step in analyzing such datasets is dimensionality reduction. We explore two primary classes of approaches to dimensionality reduction (DR): Independent Dimensionality Reduction (IDR) and Simultaneous Dimensionality Reduction (SDR). In IDR methods, of which Principal Components Analysis is a paradigmatic example, each modality is compressed independently, striving to retain as much variation within each modality as possible. In contrast, in SDR, one simultaneously compresses the modalities to maximize the covariation between the reduced descriptions while paying less attention to how much individual variation is preserved. Paradigmatic examples include Partial Least Squares and Canonical Correlations Analysis. Even though these DR methods are a staple of statistics, their relative accuracy and data set size requirements are poorly understood. We use a generative linear model to synthesize multimodal data with known variance and covariance structures to examine these questions. We assess the accuracy of the reconstruction of the covariance structures as a function of the number of samples, signal-to-noise ratio, and the number of varying and covarying signals in the data. Using numerical experiments, we demonstrate that linear SDR methods consistently outperform linear IDR methods and yield higher-quality, more succinct reduced-dimensional representations with smaller datasets. Remarkably, regularized CCA can identify low-dimensional weak covarying structures even when the number of samples is much smaller than the dimensionality of the data, which is a regime challenging for all dimensionality reduction methods. Our work corroborates and explains previous observations in the literature that SDR can be more effective in detecting covariation patterns in data. These findings strengthen the intuition that SDR should be preferred to IDR in real-world data analysis when detecting covariation is more important than preserving variation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a generative linear model to synthesize multimodal data for comparing the ability to find shared latent (covariance structure) of different dimensionality reduction approaches, including PCA, PLS, CCA, and regularized CCA (rCCA). Through numerical experiments on the synthetic datasets, they find that simultaneous dimensionality reduction (SDR) methods (PLS, CCA, and rCCA)  consistently outperform PCA (as an independent dimensionality reduction (IDR) method). Different configurations have been applied to the experiments, and remarkably, rCCA is significantly better than others when the number of samples is much smaller than the dimensionality of the data.

### Strengths
* The paper is written in a clear and logical way. Experimental results are well presented and understandable.
* The metrics provided for comparing different methods are meaningful.

### Weaknesses
 * The proposed model is just a simple linear model, which is easy to understand but hard to fit any real-world data
* These analyses are hard to migrate or generalize to real-world experimental data. For example, all results and conclusions in this paper are limited to the proposed generative linear model. At least, no real-world instruction is provided. See questions.



### Questions
I think the main drawback of this paper is that the generative linear model is too simple. It seems like it is not something new, but just a linear model for generating a synthetic dataset. Therefore, most conclusions in this paper are drawn from that generative linear model but are hard to generalize to any real-world dataset due to the high nonlinearity in the real-world dataset. Also, the real-world data is generated in a very complicated manner (in addition to nonlinearity). Therefore, the experimental results seem intuitive and easy to me. In other words, I'm not surprised by these results, since we can expect that SDRs are better than IDRs, especially in such a simple synthetic dataset generated from a linear model. Although authors provide detailed analysis with quantitative results (metrics), I still don't see what we can tell more when facing a real-world dataset. While SDRs might still be better than IDRs. However, this seems like a very direct possible result since SDRs are methods that consider correlations/covariances between $X$ and $Y$, but IDRs are not.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript conducts some numerical experiments comparing PCA to CCA, PLS, and regularized CCA in some linear-Gaussian multivariate settings.

### Strengths
The numerical experiments seem straightforward and correct.

### Weaknesses
The numerical results are essentially well understood already in the statistics community, though the specific numerics for these specific simulations are not obviously in the literature. PCA will keep the eigenvectors of the top eigenvalues of the data matrix, regardless of their source, whereas (r)CCA and PLS will keep those eigenvectors that span the joint subspace. A paper we wrote several years ago looks at the mathematics of this in some detail, https://www.nature.com/articles/s41467-021-23102-2#Sec12.  Specifically, the appendix explains how the eigenvalues matter, and we also provide theoretical guarantees using Chernoff bounds.  Another paper I like on this topic is https://www.sciencedirect.com/science/article/pii/S0047259X14001201?via%3Dihub. 

To me, this reads like a very nice senior thesis, or graduate level class project, suitable for a workshop, e.g., a Neurips workshop on high-dimensional data analysis.  To warrant publication in ICLR, I would want to see some strong theoretical results, and some results on benchmark data, and/or real world data.

### Questions
I think everything the authors wrote is quite clear.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript studies dimensionality reduction (DR) methods (PCA, PLS, CCA) for multimodal representation learning. To investigate these methods, the manuscript synthesizes data by introducing a generative linear model with known variance and covariance structures. The investigation explores whether the DR method extracts the relevant shared signal and identifies the dimensionality of the shared and self-signals from noisy, undersampled data. Based on investigation the manuscript suggests to prefer Simultaneous DR methods such as regularized CCA to recover covariance structures.

### Strengths
- Synthetic experiments for multiple cases

### Weaknesses
 **Novelty**:

- The manuscript proposes a generative linear model for multimodal data. However, the model is known and can be found in the literature. For example, it can be found in the probabilistic form (Murphy et al., 2022; Klami et al., 2012).
- The manuscript suggests preferring SDR methods over IDR methods to recover the shared signal between different modalities. However, I do not think this is novel knowledge. See Borga et al.: "A Unified Approach to PCA, PLS, MLR, and CCA." PCA, PLS, MLR, and CCA can be unified under a generalized eigenproblem. Figure 2 and Figure 3 in Borga et al. show that all the dimensionality reduction methods recover different solutions, which is expected since they have different inductive biases by construction.

**Technicality**: The experiments are very limited to synthetic data, and it is not clear how these insights will generalize to different settings. Specifically, suppose you read literature on neural networks like Deep CCA or DCCAE. In that case, they all use layer-wise unimodal pretraining or autoencoder for training, respectively, and the CCA is used only afterwards. Hence, only SDR won't be enough to model multimodal data. 

**Rigor**: The experiments do not show the solutions' variability since they have not been run over multiple initializations.

**Significance**: The significance to me is not clear.

### Questions
Overall, I do not think these results demonstrate new, relevant, and impactful knowledge.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper compares two approaches of dimensionality reduction for bimodality, namely, those methods independence between the modalities versus those assuming that some shared signal exist.
These methods are interested in different sub-blocks of a grand, unknown covariance matrix.
The authors provide a clear and well thought empirical comparison of both types of approaches.
The paper is mostly empirical and focusing on an artificial, fully-controlled framework for testing and comparing methods of each type.

### Strengths
The paper is well written, well organized, clearly structured, not missing anything with respect to its claims (which are reasonable, limitations are stated clearly as well).
The message, (limited) scope, contribution, and limitations are well described and clearly stated.

### Weaknesses
The technicality of the contribution is present but rather limited, as the paper is an empirical comparison of well established methods (PCA, CCA, etc.).
The limited scope makes it a pleasant paper to read, not too dense; the price to pay is that the novelty is weak and, as said, purely empirical and not unexpected knowing the intrinsic assumptions of the two different approaches.
Some parts could be clarified, like when discussing the variance in 2.2 (an identical variance uniformly appleid to all entries of the matrices?it seems so but the sentence comes a bit late) and the figure captions (the first figure caption could spend some more sentences describing the elements of the figure).
The paper would gain in extending the experimental section to real data.

### Questions
None at this stage.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors of this paper studies the variation preservation and covarying structure in dimensionality reduction (DR) methods for multimodal datasets through a generative linear model with known variance and covariance. The findings show that PSL and rCCA are preferred to OCA when detecting covariation is more important than variation preservation

### Strengths
Empirical studies from various perspectives of the simulated data are performed where the data are sampled from a generative model including both self-signal and shared-signal.

### Weaknesses
The presented model is formulated based on strong independent assumption for all variables in the linear model, so it doubts that the data generated from this model can align well with real data and the findings are informative. The scope of this study is limited to a small set of models based on the generative linear model, and the findings may not be properly extended to other methods. The study of this paper is mainly numerical, so it is unclear if there exists theoretical result to explain the findings.

This study is limited to specified methods, PCA, PLS and CCA, all of which are variance- or covariance-based models. It is unclear how the findings in this paper can be extended for broad family of dimensionality reduction methods.

In Section 2.2, authors present models (1) and (2) for each modality. It seems that all are random variables. Is every element in the random matrix i.i.d. sampled from a Gaussian with 0 mean and specified variance? Due to the strong assumptions used in (1) and (2), it is unknown how they align well with the generation process of real data. Authors should refer to the existing work like probabilistic PCA or probabilistic CCA for properly defining the generative linear model.

In Section 3, authors mentioned that training and test data sets are generated according to (1) and (2). Does it mean that all random variables are sampled accordingly to generate a sample pair X and Y? Due to some confusing in the definition of the presented models, it is better to describe the generation process in detail. For example, all samples may be generated with fixed U_X, U_Y and P. 

As this paper concentrates on the empirical evaluation of existing models on the data sampled from the presented generative linear model. The evaluation metric can be important. Authors introduce the so-called reconstructed correlations RC’, which is described in Appendix A.2. It is the scaled correlation of projected points in low-dimensional spaces obtained by corresponding models. The correlation values are within [-1, 1]. It is unclear why (15) should be in [0, 1]. And the measure RC_0 is introduced because the ideal uncorrelation is not achievable if the sample is few. But RC_0 is computed based on multiple random trials. That is to say, the evaluation metric is not deterministic. 

In experiments, figures with gamma_self and gamma_shared are generated. How do the two parameters are generated to form a grid? Both parameters are functions of other three variances. 

All the findings are concluded from the reconstructed correlations RC’, which is biased to CCA for maximizing the shared signals. This may not be new. Moreover, the conclusion or suggestion made by authors can be strong. It is possible that rCCA works better than PCA, but it is unclear SDR works better than IDR.

### Questions
This study is limited to specified methods, PCA, PLS and CCA, all of which are variance- or covariance-based models. It is unclear how the findings in this paper can be extended for broad family of dimensionality reduction methods.

In Section 2.2, authors present models (1) and (2) for each modality. It seems that all are random variables. Is every element in the random matrix i.i.d. sampled from a Gaussian with 0 mean and specified variance? Due to the strong assumptions used in (1) and (2), it is unknown how they align well with the generation process of real data. Authors should refer to the existing work like probabilistic PCA or probabilistic CCA for properly defining the generative linear model.

Bach, Francis R., and Michael I. Jordan. "A probabilistic interpretation of canonical correlation analysis." (2005).

In Section 3, authors mentioned that training and test data sets are generated according to (1) and (2). Does it mean that all random variables are sampled accordingly to generate a sample pair X and Y? Due to some confusing in the definition of the presented models, it is better to describe the generation process in detail. For example, all samples may be generated with fixed U_X, U_Y and P. 

As this paper concentrates on the empirical evaluation of existing models on the data sampled from the presented generative linear model. The evaluation metric can be important. Authors introduce the so-called reconstructed correlations RC’, which is described in Appendix A.2. It is the scaled correlation of projected points in low-dimensional spaces obtained by corresponding models. The correlation values are within [-1, 1]. It is unclear why (15) should be in [0, 1]. And the measure RC_0 is introduced because the ideal uncorrelation is not achievable if the sample is few. But RC_0 is computed based on multiple random trials. That is to say, the evaluation metric is not deterministic. 

In experiments, figures with gamma_self and gamma_shared are generated. How do the two parameters are generated to form a grid? Both parameters are functions of other three variances. 

All the findings are concluded from the reconstructed correlations RC’, which is biased to CCA for maximizing the shared signals. This may not be new. Moreover, the conclusion or suggestion made by authors can be strong. It is possible that rCCA works better than PCA, but it is unclear SDR works better than IDR.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
