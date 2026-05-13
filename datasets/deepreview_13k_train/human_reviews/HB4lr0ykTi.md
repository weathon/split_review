# Wasserstein Flow Matching: Generative modeling over families of distributions

- Decision: Reject
- Scores: 5, 8, 6

## Abstract
Generative modeling typically concerns the transport of a single source distribution to a single target distribution by learning (i.e., regressing onto) simple probability flows. However, in modern data-driven fields such as computer graphics and single-cell genomics, samples (say, point-clouds) from datasets can themselves be viewed as distributions (as, say, discrete measures). In these settings, the standard generative modeling paradigm of flow matching would ignore the relevant geometry of the samples. To remedy this, we propose \emph{Wasserstein flow matching} (WFM), which appropriately lifts flow matching onto families of distributions by appealing to the Riemannian nature of the Wasserstein geometry. Our algorithm leverages theoretical and computational advances in (entropic) optimal transport, as well as the attention mechanism in our neural network architecture. We present two novel algorithmic contributions. First, we demonstrate how to perform generative modeling over Gaussian distributions, where we generate representations of granular cell states from single-cell genomics data. Secondly, we show that WFM can learn flows between high-dimensional and variable sized point-clouds and synthesize cellular microenvironments from spatial transcriptomics datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new type of generative model based on flow matching, i.e., Wasserstein flow matching. The proposed model allows for working with the *distributions of distributions* and was tested in a variety of experimental setups.

### Strengths
The proposed method can be used to deal with families with distributions, i.e., distributions over distributions. It was tested on a variety of Gaussian-based where it shows better performance than naive baselines.

### Weaknesses
My main concern is related to the limited significance of the developed methodology. As the authors themselves admit (lines 235-236), the main contribution of this article is the developed algorithm. From a theoretical point of view, the method is based on the results proposed in previous works (Ambrosio et al., 2008, Lambert et al., 2022). At the same time, the authors note that these theoretical results are correct if the algorithm is applied to absolutely continuous measures, which is not true in the case when the measures are approximated as point clouds. Thus, it is not absolutely fair to apply the algorithm to any measures other than Gaussians.

Meanwhile, the theoretical groundlessness of the algorithm could be overlooked if it showed inspiring results from a practical point of view. However, the method demonstrates good results only when working with distributions that can be approximated by families of Gaussian distributions (including the spatial transcriptomics dataset, see lines 414-420). In the case of working with more general measures (point clouds), the method shows results that do not outperform those of its competitors (see Table 3 and authors comment in lines 95-96).

In addition, the experimental part could be improved by including more baselines, for example in problems from the single cell biology domain. In this regard, you might be interested in considering the methods from two recent papers that also rely on flow matching and consider problems from single cell biology (Klein et al., 2024, Eyring et al., 2024).

### Questions
- The notation $\overline{(\cdot)}^{L^2(\mu)}$ is not sufficiently clear in lines 182-183. Could you please write rigorously what is meant here? And I recommend moving such kind of notations in the corresponding part of Section 2.

**References.** 

Luigi Ambrosio, Nicola Gigli, and Giuseppe Savare ́. Gradient flows in metric spaces and in the space of probability measures. Lectures in Mathematics ETH Zu ̈rich. Birkha ̈user Verlag, Basel, second edition, 2008. ISBN 978-3-7643-8721-1. 

Marc Lambert, Sinho Chewi, Francis Bach, Silve`re Bonnabel, and Philippe Rigollet. Variational inference via Wasserstein gradient flows. Advances in Neural Information Processing Systems, 35:14434–14447, 2022.

Klein, D., Uscidda, T., Theis, F., \& Cuturi, M. (2024). GENOT: A Neural Optimal Transport Framework for Single Cell Genomics. NeurIPS 2024

Eyring, L., Klein, D., Uscidda, T., Palla, G., Kilbertus, N., Akata, Z., \& Theis, F. J. Unbalancedness in Neural Monge Maps Improves Unpaired Domain Translation. ICLR 2024

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper demonstrates an application of Riemannian Flow Matching for the novel problem of generating probability measures on the Wasserstein manifold, in particular, for the case of the Bures–Wasserstein space - i.e. distributions over Gaussian distributions, and for point-cloud data considered as empirical measures. The authors present tractable training objectives and sampling schemes for both settings, relying on closed-form solutions available in the Bures–Wasserstein space, and the approximation of the optimal transport map by entropic couplings in the point-cloud setting. Notably, their methodology allows for the generation of point-clouds with non-uniform size. They further validate their framework via experiments with single-cell genomics data and 2D and 3D point-clouds, presenting competitive results and improved scalability.

### Strengths
The paper tackles a novel and important problem within generative modelling of the generation of probability measures, with particular relevance for single-cell genomics data. The authors present a sound methodology in the particular cases of modelling distributions of Gaussian distributions and point-cloud data, with the notable attractive feature of being able to model point-cloud data of non-uniform sizes which is to the best of my knowledge, the first instance of this being tractable; this is backed up with convincing experimental validation. In addition, the paper is well-written and presented.

### Weaknesses
A potential criticism of the work is that the main components of the methodology such as Riemannian Flow Matching, closed-form solutions for geodesics etc. on the Bures–Wasserstein space, the entropic estimation of optimal transport maps etc. have been introduced elsewhere, and the main contribution of the paper is simply the original combination of these elements applied to their problem. In addition, the authors could have further discussed other settings in which generative modelling on the Wassertein manifold could be useful, such as amortising Bayesian inference, beyond the two cases considered in the paper.

### Questions
I do not have any questions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Wasserstein Flow Matching (WFM) for families of set of particles and Gaussians. In other words, this paper attempts to train the FM model on Wasserstein space. For given the pairs of probability densities $\Gamma$, the method first approximates McCann’s interpolant of $(\mu, \nu) \sim \Gamma$ through traditional OT algorithms or closed-form solutions. By this approximation, they obtain the interpolant $\mu_t$, and the velocity $v_t$. Then, the approach trains the model $F_\theta$ that learns the mean field on each $(t, \mu_t)$ through flow matching loss ($\\| F_\theta (t, \mu_t) - v_t \\|^2$). This paper evaluates their algorithm on the cell dataset and point cloud generation.

### Strengths
- The paper presents an new concept of Wasserstein Flow Matching, which extends the Flow Matching framework to probability distribution spaces.
- It effectively incorporates Gaussian cases through McCann’s (displacement) interpolant.
- The method is applied to a variety of data types, including genomic data and point cloud data.
- Overall, the paper is clear, well-structured, and easy to follow.

### Weaknesses
 - The motivation for learning the mean field on the Wasserstein space is not entirely clear, as the mean field may not capture meaningful structures like Wasserstein geodesics. Additionally, the approach first estimates McCann’s interpolation using traditional methods, followed by the FM algorithm. This sequential combination of the two algorithms feels somewhat incremental in terms of contribution.

- For cases where families of particle sets (point cloud) are considered, the paper estimates entropic OT, which deviates from the theoretical framework. Calculating the McCann's interpolant $\mu_t$ requires estimating the standard OT rather than entropic OT. Specifically, using entropic OT introduces an approximation error that is not well-quantified, and it's unclear how this affects the learned vector field's ability to accurately represent the Wasserstein geodesic. The paper does not provide a rigorous analysis of this approximation.

- Even with reduced computational overhead through estimating entropic OT, I believe there would be still huge computational burden when estimating $\mu_t$ in point cloud application. It might be helpful if the authors could specify the computational costs associated with solving entropic OT during training. I believe there would be scalability issues when the number of particles becomes more than 2000. The computational cost of solving entropic OT, even with approximations, scales poorly with the number of particles, making it impractical for larger point clouds. The paper lacks a detailed analysis of how the computational cost scales with the number of particles and the dimensionality of the data.

- Overall, the method involves an inaccurate approximation (e.g. standard OT -> entropic OT) and seems to be computationally demanding (e.g. sinkhorn for every iterations). Moreover, its performance results is not convincing for me, too. I believe the benefit of WFM method and the potential applications should be more carefully carried. The paper does not provide a clear theoretical justification for why learning the mean field on the Wasserstein space is a useful objective. The performance results, particularly in point cloud generation, do not convincingly demonstrate a significant advantage over existing methods. The lack of a rigorous theoretical analysis and the reliance on approximations raise concerns about the method's practical applicability and generalizability.

### Questions
- Could the authors provide training times, including times for solving entropic OT, for the point cloud generation tasks? Additionally, a comparison with other models, such as diffusion-based point cloud generation methods, would be insightful.

- Does the optimal velocity field $v_t$ that minimizes WFM objective guarantee the transportation of $\mathfrak{p}_0$ to $\mathfrak{p}_1$? Could the authors provide the theoretical proofs?

- What is the difference of this algorithm compare to mini-batch OT with Wasserstein distance cost (in point clouds)?

$ $

**Additional Comments** Thank you for your response. However, certain aspects of the authors' explanation remain unclear. First, the authors assume that the marginals must have a "pdf." Furthermore, they claim to apply this assumption to Flow Matching, which requires a positive density across the entire domain (generally, I think the domain is $\mathcal{W}_{2,ac}(M)$). I believe these two assumptions are contradictory since it is (typically) not possible to define a pdf in infinite-dimensional spaces; only distributions exist in such cases. This seems to create a fundamental inconsistency in the assumptions. 

That said, I do understand and appreciate some points the authors have discussed. For instance, the Bures-Wasserstein manifold is a finite-dimensional Riemannian manifold, which allows for the direct application of Riemannian Flow Matching. Consequently, I understood that we can define a "nice subspace" that ensures the flow matching vector field $v$ can transport one marginal to another. With this clarification, the discussion becomes much clearer. 

I believe that remaining small issues can be easily addressed, so I will raise my score to 6.

### Soundness
3

### Presentation
3

### Contribution
2
