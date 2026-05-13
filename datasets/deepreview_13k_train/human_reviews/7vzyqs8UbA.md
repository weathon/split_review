# LMCC-MBC: Metric-Constrained Model-Based Clustering with Wasserstein-2 Distance of Gaussian Markov Random Fields

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
A wide range of temporal (1D) and spatial (2D) data analysis problems can be formulated as model-based clustering problems given metric constraints. For example, subsequence clustering of multivariate time series is constrained by 1D temporal continuity, while urban functional area identification is constrained by the spatial proximity in the 2D space. Existing works model such metric constraints independent of the model estimation process, failing to leverage the correlation between adjacent estimated models and their locations in the metric space. To solve this problem we propose a novel metric-constrained model-based clustering algorithm LMCC-MBC that softly requires the Wasserstein-2 distance between estimated model parameters (such as those of Gaussian Markov Random Fields) to be a locally monotonic continuous function of the metric distance. We theoretically prove that satisfaction of this requirement guarantees intra-cluster cohesion and inter-cluster separation. Moreover, without explicitly optimizing log-likelihood LMCC-MBC voids the expensive EM-step that is needed by previous approaches (e.g., TICC and STICC), and enables faster and more stable clustering. Experiments on both 1D and 2D synthetic as well as real-world datasets demonstrate that our algorithm successfully captures the latent correlation between the estimated models and the metric constraints, and outperforms strong baselines by a margin up to 14.3% in ARI (Adjusted Rand Index) and 32.1% in NMI (Normalized Mutual Information).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work attempts to address the metric autocorrelation problem in model-based clustering. To be specific, each data sample is modeled by a Gaussian Markov Random Field, and the distance between GMRFs are measured by Wasserstein-2 distance. The conventional clustering assumption objective is then optimized to minimize intra-cluster distances and maximize inter-cluster distances. The authors argue that the combination of Wasserstein-2 distance and GMRF is cautiously chosen and provide some theoretical analyses.

### Strengths
* The paper is well-written and easy to read.
* This work proposes to incorporate metric autocorrelation into the clustering model, which is important but overlooked by previous works.
* Empirical results on both synthetic and real-world datasets verify the effectiveness of the proposed method.

### Weaknesses
 * The effectiveness of modification from Eq. (5) to (6) is empirical and lacks a theoretical guarantee. Specifically, while the authors introduce a model-based semivariogram, the justification for using this specific form in the goodness-of-fit test, and how it directly relates to minimizing failed tests, is not rigorously established. The connection between the expected Wasserstein-2 distance and the threshold for the goodness-of-fit test requires more theoretical backing.
* The proposed method just combines several existing components. Even though the authors argue that the chosen combination is not heuristic, and provides some special theoretical properties of them, the overall technical contribution looks less significant to me. The core idea of using a GMRF with Wasserstein-2 distance is not novel in itself, and the clustering objective, while framed differently, still relies on minimizing intra-cluster distances and maximizing inter-cluster distances, a common theme in clustering. The novelty of minimizing failed goodness-of-fit tests is not clearly demonstrated as a significant departure from existing clustering objectives.
* The experiments are weak. Only an overview of clustering performance is provided. Ablation studies of the design choices are lacking, so these claims are not well-supported. For example, the impact of the number of neighbors used in the semivariogram calculation, or the shift hyperparameter, is not explored. Comparisons with strong baselines are also lacking. The baselines, TICC and STICC, are not sufficiently strong given their publication dates and citation counts, and there is no comparison to more recent state-of-the-art clustering algorithms.

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors focus on metric-constrained clustering (when clustering is based not only on the features of the data points but also on constraints in a metric space (time, geo data points). Within that framework, they propose a new metric-constrained model-based clustering approach, LMCC-MBC (Locally Monotonically and Continuously Constrained Model-Based Clustering) optimized to maximize intra-cluster cohesion and inter-cluster separation, working as follows:

-For each data point, compute the neighboring set of points in the metric-constraint space (not using the features) and fit a Gaussian Markov Random Field model with Graphical Lasso algorithm. 

-For each pair of observations, compute model and metric distances (at this stage, we still don’t leverage features of the data points).

-Compute a semivariogram from the two distances and $\rho$ the range of the fitted semivariogram

-Compute weighted distance matrix M based on model, metric distances, semivariogram, $\rho$

-Run the some density-based clustering method (ex: DBSCAN) on M for the final clustering partition.

Wasserstein-2 distance is used as the model distance.

### Strengths
The paper is well written and quite enjoyable to read.

The only hyperparameters of the clustering approach are the number of neighbors to consider per data point, the metric-constraint strength ($\beta$) and a shift parameter  ($\delta$) that was found empirically to overlap the clustering boundaries if appropriately tuned. 

The authors generalize the concept of the classic semivariogram for multivariate data points.

Experiments are made on 2 synthetic datasets and 7 real-world datasets equally split between the temporal and spatial use case. LMCC model with and without metric constraints show promising results by providing systematically the best ARI and NMI.

A comparison is made between LMCC and TICC/STICC algorithms (the competing approaches for the metric-constrained case) regarding stability and robustness.

### Weaknesses
As with many clustering algorithms, there could be a theoretical comparison analysis of the space and time complexities for LMCC-MBC and competing SOTA techniques. 

Regarding the following claim:  “In fact, Wasserstein-2 distance is the only feasible choice of model distance that theoretically guarantees the generalized model-based semivariogram is compatible with the classic definition. Consequently, GMRF is chosen because it is the most computationally efficient model parameterization under Wasserstein-2 distance. The following section will prove this in detail.”
It does not sound to me that there is a proof here. The usage of Wasserstein-2 distance and GMRF is justified, yes, but I don't have the feeling that this proves that these are the only options as stated.   

No experimental study of the effects of the number of neighbors and the shift parameter on accuracy. 

Minor, typos:

-missing space after “unknown” in intro p.1

-requirment, p.7

-natrually, p.7 before eq. 11

-fittiing p.8 in Algorithm 1

-hyperparamters p.16

-missing space after “our baselines(Kang et al, 2022) p.16

-unlined instead of underlined in p.17

-It seems there is a missing paragraph in the Appendix related to Execution time comparison

### Questions
Q1: Could you please provide a theoretical comparison analysis of the space and time complexities for LMCC-MBC and competing SOTA techniques?

Q2: How in practice do you tune the shift parameter $\delta$? It seems to be the determinant hyperparameter of the method but there is no study to show the influence on accuracy. Same for the number of neighbors to consider. 

Q3: Can you please explain how you prove that the requirement of the Wasserstein-2 distance between estimated model parameters from GMRF (model distance) to be a locally monotonic continuous function of the metric distance guarantees intra-cluster cohesion and inter-cluster separation?

Q4: What is the purpose of the experiments with the synthetic datasets? They seem to be applying the same experiment setup as the real-word ones.

=== AFTER REBUTTAL ===

I thank the authors for taking the time to answer my questions that are now addressed (time complexity analysis, further justification of the Wasserstein-2 distance). Hence, I upgrade my score to Weak accept.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Problem: This paper studies a clustering problem for data with special properties like time or spatial positions. This paper focuses on the case when there is the effect of metric autocorrelation in data, which means the variance of feature vectors is positively correlated to their temporal/spatial distances.

Modelling: The authors propose a metric-constrained model-based model that leverages the correlation between adjacent estimated models and their locations in metric space. They use Gaussian Markov Random Fields to model inter-observation dependency and use Wasserstein-2 distance to measure the distance between estimated model parameters. Because of the metric autocorrelation, they use a metric penalty that decreases as distance increases.

Key results: From the experimental results, their algorithm appears to be computationally more efficient than other methods and has better performance in terms of ARI and NMI.

### Strengths
1. From the experimental results, their algorithm appears to be computationally more efficient than other methods and has better performance in terms of ARI and NMI.
2. The proposed method can deal with arbitrary dimensions of constraint space instead of just 1-D and 2-D.

### Weaknesses
Major comments:
1. In the contribution section: the authors indicate that they present a solid mathematical proof of the soundness of their generalized semivariogram. But there isn’t any proof in this paper and later they say “The soundness of this generalized definition can be easily verified on real-world datasets”.
2. Same problem for the fourth contribution. It would be better to at least have a complexity analysis for your algorithm to say that your algorithm solves the problem efficiently with “solid theoretical proofs”.
3. I think the authors need to justify the use of GMRF in the model since they are fitting a GMRF for each sample. It would make more sense to fit one GMRF for one cluster as different data clusters will naturally have different variable dependency structures. The current approach seems to assume that each data point's local neighborhood has a unique dependency structure, which is not necessarily true and could lead to overfitting.
4. One of the advantages of the proposed method they can deal with arbitrary dimensions of constraint space instead of just 1-D and 2-D. Did you try it with a 3-D dataset?

Minor comments:
1. In section 5.1, the authors claim that the proposed method has only three hyperparameters to tune. What about the tuning parameter for Graphical Lasso?

### Questions
See "Weaknesses"

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
