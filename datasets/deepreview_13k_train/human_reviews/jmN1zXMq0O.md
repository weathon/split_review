# To Clip or not to Clip: the Dynamics of SGD with Gradient Clipping in High-Dimensions

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
The success of modern machine learning is due in part to the adaptive optimization methods that have been developed to deal with the difficulties of training large models over complex datasets. One such method is gradient clipping: a practical procedure with limited theoretical underpinnings. In this work, we study clipping in a least squares problem under streaming SGD. We develop a theoretical analysis of the learning dynamics in the limit of large intrinsic dimension—a model and dataset dependent notion of dimensionality. In this limit we find a deterministic equation that describes the evolution of the loss and demonstrate that this equation predicts the path of clipped SGD on synthetic, CIFAR10, and Wikitext2 data. We show that with Gaussian noise clipping cannot improve SGD performance. Yet, in other noisy settings, clipping can provide benefits with tuning of the clipping threshold. We propose a simple heuristic for near optimal scheduling of the clipping threshold which requires the tuning of only one hyperparameter. We conclude with a discussion about the links between high-dimensional clipping and neural network training.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper analyzes SGD with gradient clipping by constructing an analogous Stochastic Differential Equation (SDE) and studying its solution. The SDE developed by the authors follows the development in [1] with the addition of two factors $\mu_c$ and $\nu_c$ that capture the effect of gradient clipping. The authors show that their SDE is close to the SGD trajectory and also conduct a stability analysis to obtain a criterion for when clipped SGD is more or less stable than its unclipped version (and allows for larger learning rates). The authors study different noise conditions (Gaussian and Rademacher-type) noise and show that the clipping threshold can be set to obtain larger learning rates. Finally this paper explores the conditions under which clipped SGD can achieve lower risk values than unclipped SGD.

[1] Paquette, C., Paquette, E., Adlam, B., & Pennington, J. (2022). Homogenization of SGD in high-dimensions: Exact dynamics and generalization properties. arXiv preprint arXiv:2205.07069.

### Strengths
The theoretical analysis seems strong and the authors provide extensive technical proofs for their theoretical results. While I did not go through all the proofs to verify their correctness, the analysis seems correct. The authors go beyond just showing a correspondence between clipped SGD and the C-HSGD stochastic differential equation to provide some applications of their result to stability analysis and to study when clipping helps in SGD.

### Weaknesses
1. The theoretical analysis seems to mostly be an application of previous results obtained in [1]. The new machinery that is used here is Stein's lemma to obtain bounds on the quantities $\mu_c$ and $\nu_c$ that characterize the effects of clipping SGD. This only allows the authors to characterize $\mu_c, \nu_c$ for gaussian data, even though they are able to show the correspondence of the SDE to clipped SGD with non-gaussian data. The technical contribution is arguably only incremental.

2. The condition for testing whether clipped SGD reaches lower risk values (CCC) seems to be hard to evaluate. It involves estimating whether $\mu_c^2 / \nu_c > 1$ anywhere along the trajectory of the SDE. This seems to require solving the SDE to estimate whether clipped SGD is beneficial, as well as estimating the threshold $c$ at which to clip the gradients. This may be harder than simply solving the original least squares optimization problem.

3. While the authors explore how their results extend to the setting of training deep networks, the arguments are made in the regime where deep networks can be approximated well by linear models (the NTK regime). NTK models do not perform as well as deep networks that learn features and that cannot be approximated as linear models.

### Questions
1. The role of CSC is still unclear to me. Can the authors provide a demonstration of how clipped SGD allows for larger learning rates. None of the figures seem to illustrate how clipped SGD converges faster than unclipped SGD. In case I have missed this please direct me to where I can find this.

2. While there is a figure demonstrating the correspondence of clipped SGD and the SDE with heavy tailed Cauchy noise, there are no experiments comparing unclipped and clipped SGD in that condition. Does clipped SGD converge faster in that situation? Can this be demonstrated in an experiment?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the properties of clipped SGD for linear regression with mean squared error loss under specific data and noise distributions. The authors compare the parameters learned from clipped SGD (C-SGD) to the solution of a stochastic differential equation (C-HSGD), demonstrating their close alignment in terms of risk and optimality gap. They also derive an ODE to describe risk evolution. Additionally, learning stability (CSC) and instantaneous risk descent (CCC) are analyzed through descent and variance reduction factors. The authors show that under Gaussian noise, clipped SGD is inferior to unclipped SGD, but under other noise distributions, it improves both performance and stability. Theoretical results are supported by experiments.

### Strengths
The paper is very well-written, and the problem it addresses is important for large-scale learning settings.  Particularly, gradient clipping is an important  technique that proves useful in deep learning, which makes it crucial to understand its effects. This paper provides a rigorous characterization of clipped SGD in linear regression, focusing on the descent and variance reduction factors. The authors also propose a learning rate schedule that ensures clipped SGD performs at least as well as standard SGD, offering practical insights for optimization.

### Weaknesses
 * The problem setting is restricted to linear regression with mean squared loss  and the proposed heuristic seems to be meaningful only when the features follow a Gaussian distribution.

* Calculating the descent and variance reduction factors in more general settings appears challenging, since it involves numerical optimization at every step, which limits the practical applicability of the proposed learning rate scheduling and criteria.



### Questions
* In the conclusion, the authors suggest extending the analysis to more complex losses. What are the bottlenecks for such an analysis?
* The heuristic presented in the paper appears to be limited to normally distributed data due to the validity of Eqs. (10a) and (10b). Is it possible to extend this approach to a more general setting, such as sub-Gaussian distributions?
* While the authors used real-world data to validate the C-HSGD approximation, they did not evaluate the heuristics on real-world data (though the setup for Figure 4 is somewhat unclear, please correct me if I am mistaken). Could the authors clarify why this aspect was not explored?

Minor: 
* In Theorem 1, the subscript for $\theta_{sd}$  in the denominator of the definition of $\mathcal{E}$ should include a ceiling (or floor).

### Soundness
3

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
The paper studies the widely used gradient clipping technique in SGD under quadratic settings. Under specific assumptions, the paper develops a theoretical analysis of the training dynamics by proposing an SDE C-HSGD and proving its connection to clipped SGD. Based on this, the paper shows that when clipping can help convergence and stability, providing insights into understanding the clipping technique.

### Strengths
1. To my knowledge, this is a novel perspective looking into clipping, which is interesting and aligns with the common belief that clipping helps when noise is heavy-tailed.

2. The theory seems to be clear and complete.

### Weaknesses
1. Although the theory looks promising, I think it's still restrictive due to the settings it applies: 
    - As the author also mentioned in the paper, one of the key benefits of clipping is that it helps SGD converge in generalized smooth settings, which cannot be reflected by quadratics. This is a significant limitation, as many real-world loss functions are non-quadratic and exhibit complex geometries. The analysis does not capture the potential benefits of clipping in navigating these more complex landscapes, such as escaping saddle points or sharp minima, which are common in non-convex optimization.
    - The theory typically requires the data $x$ to be Gaussian, or close to Gaussian as in Appendix A. This is still a restrictive assumption. While the authors mention sub-Gaussianity, the practical implications of this assumption on real-world datasets, which often exhibit more complex distributions, are not fully addressed. For instance, the impact of heavy-tailed or multimodal data distributions on the theoretical results remains unclear.

2. I kindly suggest the authors gather more notation definitions in Section 2, as there are still new notations in the following sections, which may make it inconvenient to follow and refer to when reading.

### Questions
1. More intuitive explanations for the connection between C-SGD and S-HSGD are welcomed.

2. As also noted in the weakness part, I think possibly the authors can discuss how the analysis in the Gaussian quadratic settings may have impacts on broader machine learning applications.

3. Do you also take stability into consideration when comparing C-SGD and SGD in Section 5?

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
2

### Summary
This paper provides a theoretical investigation into the effects of gradient clipping in high-dimensional settings. Specifically, the authors analyze how clipping impacts SGD in terms of stability, convergence, and optimization dynamics. They derive a deterministic equivalent for clipped SGD, named Clipped Homogenized SGD, which approximates the risk evolution via a system of Ordinary Differential Equations (ODEs) under high-dimensional assumptions. Key findings indicate that while clipping does not improve performance with Gaussian noise, it can enhance stability and convergence under other noisy conditions. The paper also proposes a heuristic clipping schedule for near-optimal performance with minimal hyperparameter tuning.

### Strengths
1. The study provides a new theoretical perspective on gradient clipping, a widely used technique in training deep learning models, by framing it in high-dimensional analysis. This theoretical foundation is novel and helps bridge a gap in understanding the dynamics of SGD under clipping.

2. The paper is well-organized, with a clear presentation of problem setup, definitions, and theoretical results. The analysis is rigorous, covering a range of noise distributions and demonstrating the proposed model’s effectiveness across synthetic and real-world datasets

### Weaknesses
1. The analysis is specific to linear regression, which may limit the generalizability of the findings to other types of models. Insights into extending these results or experiments with more complex models, such as neural networks, could enhance the broader relevance of the work. Specifically, the paper does not address how the clipping threshold would need to be adapted for non-linear models or different loss functions. The current analysis assumes a quadratic loss landscape, and it is unclear how the derived ODEs would change with non-convex or more complex loss surfaces. Furthermore, the paper does not discuss the potential impact of the clipping operation on the feature representation learned by a neural network, which is a crucial aspect of deep learning models.

2. The descent and variance reduction factors play a central role in understanding the stability and effectiveness of clipping. However, the paper lacks a practical interpretation or intuition for these factors, which might make it challenging for practitioners to apply these insights beyond the linear regression context. While the paper provides mathematical definitions, it does not offer concrete examples of how these factors manifest in real-world scenarios or how they could be used to guide the selection of clipping parameters. For instance, it would be beneficial to understand how these factors are affected by different data distributions or model architectures, and how they relate to the generalization performance of the model.

### Questions
1. Can the authors provide more insights into how sensitive the results are to the hyperparameter choice in the proposed clipping heuristic? Would small variations in the threshold significantly affect the stability or convergence?

2. Could the authors discuss the potential for extending their theoretical findings beyond linear regression to other models, such as generalized linear models? Are there specific challenges or limitations in applying their stability analysis to non-linear models or more complex loss functions?

### Soundness
3

### Presentation
3

### Contribution
3
