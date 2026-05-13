# Bayesian Bi-clustering of Neural Spiking Activity with Latent Structures

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Modern neural recording techniques allow neuroscientists to obtain spiking activity of multiple neurons from different brain regions over long time periods, which requires new statistical methods to be developed for understanding structure of the large-scale data. In this paper, we develop a bi-clustering method to cluster the neural spiking activity spatially and temporally, according to their low-dimensional latent structures. The spatial (neuron) clusters are defined by the latent trajectories within each neural population, while the temporal (state) clusters are defined by (populationally) synchronous local linear dynamics shared with different periods. To flexibly extract the bi-clustering structure, we build the model non-parametrically, and develop an efficient Markov chain Monte Carlo (MCMC) algorithm to sample the posterior distributions of model parameters. Validating our proposed MCMC algorithm through simulations, we find the method can recover unknown parameters and true bi-clustering structures successfully. We then apply the proposed bi-clustering method to multi-regional neural recordings under different experiment settings, where we find that simultaneously considering latent trajectories and spatial-temporal clustering structures can provide us with a more accurate and interpretable result. Overall, the proposed method provides scientific insights for large-scale (counting) time series with elongated recording periods, and it can potentially have application beyond neuroscience.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a nonparametric Bayesian biclustering algorithm to simultaneously form spatial (neuron) clusters and temporal clusters for multiple (count) time series. The algorithm is carried out through efficient MCMC sampling and is shown to be able to recover all model parameters in simulation studies. The proposed algorithm is then applied to a real data set to show its effectiveness.

### Strengths
The algorithm is clearly described, reasonable assumptions are imposed, and it has a potentially large range of applications.
The overall writing is good and the presentation is clear.

### Weaknesses
The numerical results, including simulation studies and real data application, are not enough convincing. The authors only reviewed some work in time series clustering. However, the neural spiking activity data is originally a point process and one has to aggregate them using small bins into count time series. There is some existing work on finding clusters in point process literature as well, which in my opinion should be reviewed for relevance. For example, [1], [2], [3], and references therein. The simulation study is a little bit too simple, with only one parameter setting, and there are no comparisons to the state-of-the-art methods.   I would suggest investigating three things: (1) the sensitivity of the bin sizes; (2) how the estimation performances change when the number of nodes and the Time length increases; (3) compared to some existing methods in terms of the predictive performances (one may consider using cross-validations.) In the real data analysis, the authors argue that it is necessary to use the biclustering algorithm. However, no comparison to any existing method is given.  Similar to the simulation studies, I suggest comparing the predictive performance of the proposed algorithm to some existing methods. In the simulation study, there is no histogram in Figure 3(c). Could you please clarify?

### Questions
1. The authors only reviewed some work in time series clustering. However, the neural spiking activity data is originally a point process and one has to aggregate them using small bins into count time series. There is some existing work on finding clusters in point process literature as well, which in my opinion should be reviewed for relevance. For example, [1], [2], [3], and references therein. 

2. The simulation study is a little bit too simple, with only one parameter setting, and there are no comparisons to the state-of-the-art methods.   I would suggest investigating three things: (1) the sensitivity of the bin sizes; (2) how the estimation performances change when the number of nodes and the Time length increases; (3) compared to some existing methods in terms of the predictive performances (one may consider using cross-validations.)

3. In the real data analysis, the authors argue that it is necessary to use the biclustering algorithm. However, no comparison to any existing method is given.  Similar to the simulation studies, I suggest comparing the predictive performance of the proposed algorithm to some existing methods.

4. In the simulation study, there is no histogram in Figure 3(c). Could you please clarify?

[1] Xu, H., & Zha, H. (2017). A dirichlet mixture model of hawkes processes for event sequence clustering. Advances in neural information processing systems, 30.

[2] Yin, L., Xu, G., Sang, H., & Guan, Y. (2021). Row-clustering of a Point Process-valued Matrix. Advances in Neural Information Processing Systems, 34, 20028-20039.

[3] Fang, G., Xu, G., Xu, H., Zhu, X., & Guan, Y. (2023). Group network Hawkes process. Journal of the American Statistical Association, (just-accepted), 1-78.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Motivated by modeling of neural spiking activities, the paper proposes a bi-clustering approach at both spatial and temporal levels. Individual count data are modeled through negative binomial regression. The spatial (subject) clusters are modeled through mixture of finite mixtures. The temporal (state) clusters are modeled through hierarchical Dirichlet process. The dependency of negative binomial regression on the temporal dimension is given by a hidden Markov model. A MCMC algorithm is designed for sampling from the posterior distribution. Both synthetic numerical experiments and real applications are provided.

### Strengths
1. The problem is well-motivated with a meaningful and important application.
2. The paper is mostly well-written and clearly presented.
3. Sufficient background and preliminaries are provided.
4. Details on the derivation of the MCMC algorithms are provided.
5. The challenging goal of conducting full Bayesian inference for a complex clustering task is of itself great importance.

### Weaknesses
1. While some constraints required for identifiability are provided at the end of section 2.1, I am not convinced that these are sufficient conditions. A theoretical proof of the model identifiability along with all necessary conditions seems important here, given the vast number of parameters. Specifically, the constraints mentioned address scaling and permutation ambiguities, but it's unclear if these are sufficient to ensure a unique parameterization, especially with the hierarchical Dirichlet process and mixture of finite mixtures components. The interaction between these components and the identifiability of the overall model needs more rigorous justification.
2. The MCMC algorithm has incorporated all the most modern efficient MCMC techniques, including the Polya-Gamma augmentation, Miller&Harrison sampler for mixture of finite mixtures, FFBS for state space models, etc. The effort here is worth being recognized. However, for both the simulation and application, the MCMC sampler is run for only 1000 iterations. I am concerned of whether the MCMC sampler has really converged given its complexity and the vast amount of model parameters. Given the hierarchical nature of the model and the use of non-conjugate priors, 1000 iterations seems insufficient to explore the posterior distribution adequately.  It would be beneficial to present trace plots of parameters, autocorrelation plots, and also conduct MCMC convergence diagnosis (e.g. using Gelman-Rubin or Geweke statistics) to ensure the validity of the results.
3. There are some typos in the paper and some terms undefined, e.g.
    - the distribution \mathcal{S} in equation (4) is only given in the appendix
    - in the first paragraph of Sec 2.1, where \log\mu_{i, t} = d_i + \tilde{c}' \tilde{x}_t^{(z_i)} has missing subscript i in \tilde{c}.

### Questions
The temporal clusters are captured in the temporal dynamic in the AR(1) model. What is the motivation of such modeling from an application perspective, compared to simpler modeling (e.g. directly model temporal clusters of \tilde{X}_t through change points, etc)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a spatio-temporal clustering method to analyze multiple neural populations. This method could find the clusters in neurons (spatial) and different states over time (temporal). To flexibly extract the bi-clustering structure, the authors model the spike data in a non-parametrical way, where the subject clustering structure is modeled by a mixture of finite mixtures model and the state clustering structure is modeled by a sticky Hierarchical Dirichlet Process Hidden Markov Model. The inference is performed by MCMC with the Polya-Gamma technique. In the experiments, the authors evaluate their method on both simulated data and neural recordings.

### Strengths
* Different from previous LDS methods, this paper explores multi-region neural data from a new perspective: the authors try to understand multi-neural populations by spatiotemporal clustering structures.

* Non-parametrically model the neural data so that there is no need to prespecify the number for subject and state clusters.

### Weaknesses
 * No analysis of the scalability of this method. For both syntactic data and real neural data, the number of neurons is small (e.g., 30, 60). Could this method generalize to a large neural recording? Such as a larger number of neurons and a longer time stamps. The lack of scalability analysis is a significant concern, as the computational cost of MCMC methods can increase dramatically with larger datasets. Specifically, the Polya-Gamma technique, while efficient for sampling binary data, may become a bottleneck when dealing with hundreds or thousands of neurons and extended recording durations. It is crucial to understand how the number of MCMC iterations scales with data size, and whether the method can be applied to more realistic neural datasets.

* No comparison of the proposed model with other latent variable models like SLDS and rSLDS. The absence of a comparison with established models like Switching Linear Dynamical Systems (SLDS) and recurrent SLDS (rSLDS) is a notable weakness. These models are commonly used for analyzing neural population activity and have well-understood properties. Without a direct comparison, it is difficult to assess the relative advantages and disadvantages of the proposed method. For instance, it is unclear whether the proposed clustering approach offers any benefits over the latent state representations learned by SLDS or rSLDS, particularly in terms of capturing temporal dynamics or identifying meaningful neural groupings. The authors should at least discuss the differences in model assumptions and potential use cases.

* Some typos, e.g., the "cite" doesn't refer to a paper in section 2.3, the figure index should be 2 rather than 3 in section 3, and the figure index should be 3 rather than 4 in section 4.

### Questions
*  What's the time complexity (concerning the number of iterations, trials, neurons, and time points) of the proposed model with the efficient MCMC algorithm? 

* What kind of desirable neural data could be better analyzed by such spatiotemporal clustering structures rather than LDS-based models (e.g., SLDS, r-SLDS)? 

* Could you please discuss the relationship of this method to the PP-Seq model [1]? PP-Seq is an unsupervised non-parametrical model to detect neural sequences in high dimensional neural recordings, which could be considered as a clustering approach to finding spatiotemporal neural patterns.

[1] Williams, Alex, et al. "Point process models for sequence detection in high-dimensional neural spike trains." Advances in neural information processing systems 33 (2020): 14350-14361.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
