# ELBOing Stein: Variational Bayes with Stein Mixture Inference

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Stein variational gradient descent (SVGD) \citep{liu2016stein} performs approximate Bayesian inference by representing the posterior with a set of particles. However, SVGD suffers from variance collapse,  i.e. poor predictions due to underestimating uncertainty \citep{ba2021understanding}, even for moderately-dimensional models such as small Bayesian neural networks (BNNs). To address this issue, we generalize SVGD by letting each particle parameterize a component distribution in a mixture model. Our method, \textit{Stein Mixture Inference} (SMI), optimizes a lower bound to the evidence (ELBO) and introduces user-specified guides parameterized by particles. SMI extends the Nonlinear SVGD framework \citep{pmlr-v97-wang19h} to the case of variational Bayes.
 SMI effectively avoids variance collapse, judging by a previously described test developed for this purpose, and performs well on standard data sets. In addition, SMI requires considerably fewer particles than SVGD to accurately estimate uncertainty for small BNNs. The synergistic combination of NSVGD, ELBO optimization and user-specified guides establishes a promising approach towards variational Bayesian inference in the case of tall and wide data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors improve Stein variational gradient descent (Liu & Wang, 2016) by extending nonlinear SVGD (Wang & Liu, 2019) by learning a density-based mixture model to approximate the posterior, instead of solely relying on particles (i.e., delta-distributions).
They evaluate their method on a set of (small) scale regression tasks.

### Strengths
- The method is a straightforward and effective extension of SVGD/NSVGD
- The paper is well-written and easy to follow and the same goes for the provided codebase

### Weaknesses
 - The experiments are rather small-scale and limited to regression data sets. Their aim seems to be primarily to demonstrate the relative performance of the proposed approach compared to prior SVGD-related approaches rather than, its absolute performance. In the list of baselines, at least a comparison against an HMC performance on the UCI data sets would have been nice to see how close it can come to it (or improve upon it).
- The paper lacks ablations to evaluate what happens as an underlying BNN gets deeper, i.e., to what extent it can handle the increase in parameters. A deep experiment could be a combination with last-layer BNNs, i.e., learn the mixture not for the whole net, but treat only the penultimate layer in a Bayesian fashion.
- The experiments are limited to regressions with a homoscedastic, known observation noise. What about classification or heteroscedastic regression tasks?
- Citing Agarap (2018) in l478 as a reference for ReLUs seems rather odd. In their work, they evaluate the usage of a ReLU in place of a softmax for classification, i.e., nothing related to the current work nor has the ReLU been introduced in that paper.



### Questions
- Q1: Can the authors speculate on performance as a function of the parameter count, e.g., sticking to BNNs, at which depth/width would the method start to struggle?
- Q2: What are the increased runtime costs compared to compared baselines?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces Stein Mixture Inference (SMI), which optimizes a lower bound to the Evidence Lower Bound (ELBO). 
SMI extends Nonlinear Stein Variational Gradient Descent (NSVGD) to the variational Bayes setting and addresses the issue of variance collapse. 
The effectiveness of SMI is demonstrated on both synthetic and real-world datasets.

### Strengths
1. The problem addressed in this paper is both important and compelling. Traditional approaches like ordinary mean-field variational inference (OVI) and Stein Variational Gradient Descent (SVGD) often experience variance collapse, whereas SMI provides more accurate variance estimates, improving uncertainty quantification.

2. The paper is well-written, providing a clear background and a thorough summary of related work. As someone slightly unfamiliar with the field, I particularly appreciated the authors' effort to re-explain and contextualize prior results, which greatly helped in assessing the paper's contributions.

3. SMI is compared with other methods across a variety of synthetic and real-world datasets.

### Weaknesses
1. Variational inference offers a compelling alternative to sampling methods like MCMC due to its efficiency, especially in high-dimensional settings and with large-scale datasets. 
However, the current validation of SMI is limited to small to moderately-sized models, which somewhat limits its appeal and persuasiveness for broader, large-scale applications. The experiments do not explore the behavior of SMI with very high-dimensional posteriors, which is a key area where variational methods are most beneficial. The lack of evaluation on complex, high-dimensional models makes it difficult to assess the practical impact of SMI in real-world scenarios.

2. The paper lacks theoretical insights or guidance on how SMI’s performance depends on the number of particles $m$. While the authors demonstrate empirical results, there is no analysis of how the approximation quality changes with varying $m$. This makes it difficult to choose an appropriate $m$ for a given problem. The absence of a theoretical framework makes it challenging to understand the trade-offs between computational cost and approximation accuracy when selecting the number of particles. Furthermore, without theoretical guidance, it is unclear how the choice of $m$ interacts with other hyperparameters in the model.

### Questions
1. It’s challenging to distinguish the lines representing different methods in Figure 2 (e.g. $SMI_{1}$, $SMI_{20}$). 
Using distinct colors for each method would improve the visualization and make the differences clearer.
2. The experiments in Section 6.1 demonstrate that SMI overcomes variance collapse. It would also be valuable to assess whether the approximate distribution given by SMI accurately captures the shape of the posterior. 
This could be evaluated by comparing the estimated covariance matrix with the target covariance matrix.

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
3

### Summary
- The authors propose a method called Stein Mixture Inference (SMI) to address the issue of variance collapse observed in Stein Variational Gradient Descent (SVGD).
- SMI extends the Nonlinear SVGD framework (Wang & Liu, 2019) to variational inference (VI) by allowing each particle to parameterize a component distribution within a mixture model, thereby introducing ELBO-like objectives.
- The authors show that SMI offers several advantages over standard SVGD by effectively mitigating variance collapse.

### Strengths
- The application of variational inference (VI) concepts to Stein Variational Gradient Descent (SVGD) appears novel and intriguing.
- The authors validate their VI-based approach through numerical experiments on several UCI benchmark datasets, demonstrating good performance. The results seem to suggest that this approach effectively mitigates the impact of variance collapse.

### Weaknesses
### Insufficient Analysis of the Motivation Behind Extending SVGD with VI for Variance Collapse Mitigation:
- The main objective of this paper, as I understand it, is to mitigate variance collapse by extending the SVGD objective function through a combination of an ELBO-like objective from VI and the Non-linear SVGD framework. However, it is not entirely clear "why" this extension effectively mitigates variance collapse. While Figure 1 provides a conceptual illustration, it does not intuitively explain how the proposed method addresses variance collapse. Additionally, while the third paragraph of the Introduction discusses the motivation for this approach, it remains unclear how using a mixture of approximate distributions around SVGD particles with a VI-inspired objective avoids variance collapse. Specifically, the paper lacks a clear explanation of how the repulsive forces in the kernelized SVGD framework interact with the variational distributions to prevent particles from collapsing to a single mode or underestimating the variance. A more detailed analysis of the interplay between the kernel and the variational parameters is needed.
- The authors propose controlling particles through variational distributions, similar to VI, as a solution to the variance collapse issue. However, given the use of the NSVGD framework, the critical role of this aspect remains unclear. The entropy regularization term could potentially affect not only mode collapse but also variance collapse. If the VI-inspired approach is indeed effective, the method should perform well even with $\alpha=0$. In this context, Figure 2 shows that variance collapse is mitigated even when $\alpha$ takes small values, suggesting that particle control via variational distributions may be effective. On the other hand, this result implies that regularization may not play a significant role, raising questions about the necessity of combining it with NSVGD. Overall, it remains unclear why the NSVGD framework is essential and which part of the proposed approach effectively addresses variance collapse. The paper needs to clarify whether the entropy term is crucial for mitigating variance collapse or if the variational parameterization alone is sufficient. The specific contribution of the NSVGD framework, beyond providing a kernelized repulsive force, is not well-articulated.

### Concerns Regarding the Limited Number of Comparative Methods:
- For sample approximations of the posterior distribution, methods such as HMC (Neal, 2011) and MMD descent (Arbel et al., 2019; Ba et al., 2021) are also effective. However, this study only compares performance within the SVGD family of methods and EVI, leaving questions about the extent to which the proposed method mitigates variance collapse in the broader context of approximate inference. Given that (Ba et al., 2021) also includes these methods in numerical experiments addressing variance collapse, this comparison is essential for validating contributions in this research area. The absence of a comparison with these established methods makes it difficult to assess the practical significance of the proposed approach. The paper should include a more comprehensive comparison to demonstrate the advantages of SMI over other state-of-the-art methods for posterior approximation.
- Additionally, the absence of a comparison with the resampling method proposed by (Ba et al., 2021) raises concerns regarding the integrity of the performance evaluation. While the authors argue in Section 5 that the resampling method is computationally infeasible, I believe this does not fully justify its exclusion as a comparative method. Given the availability of an “NVIDIA Quadro RTX 6000 GPU,” running such methods may not be computationally prohibitive, at least for datasets like the UCI benchmarks. The computational argument needs to be more rigorously justified, perhaps by providing empirical evidence of the computational cost of the resampling method on the specific datasets used in the paper. Furthermore, the claim that the method is an analytic tool and not scalable needs to be substantiated with more detailed analysis. 
- Furthermore, I find it difficult to agree with the authors’ claim: “Annealing SVGD (ASVGD) D’Angelo & Fortuin (2021a) is the only alternative that directly addresses variance collapse in SVGD with a viable method.” I believe that the resampling method proposed by (Ba et al., 2021) is also aimed at mitigating the variance collapse problem.


### Questions
- Could you provide additional analysis or intuition on why the combination of an ELBO-like objective from VI and the Non-linear SVGD framework effectively mitigates variance collapse? Specifically, how does modeling a mixture of approximate distributions around the vicinity of SVGD particles help in avoiding variance collapse? A more detailed explanation or visual representation would be appreciated.
  - For example, could you provide a more detailed explanation or visual representation of how the mixture components interact with the ELBO objective to mitigate variance collapse? For instance, a step-by-step explanation or diagram illustrating how the proposed method addresses the variance collapse problem would be helpful.
- Why is the integration with the NSVGD framework necessary in your method? Is there evidence that the entropy regularization term alone is insufficient to address variance collapse? Given that Figure 2 shows variance collapse is mitigated even when $\alpha$ takes small values, does this imply that the regularization component may not be as critical? If so, what is the rationale for including it in the framework?
- Why were methods such as HMC and MMD descent not included in the comparative analysis, especially given their relevance in approximate inference and their use in experiments in (Ba et al., 2021)?
  - If possible, could you add comparisons with HMC (Neal, 2011) and MMD descent (Arbel et al., 2019; Ba et al., 2021) in the experimental section, particularly at least on the UCI datasets, to provide a broader context for evaluating SMI’s performance in addressing variance collapse? If a full comparison is not feasible, could you discuss how SMI might be expected to compare to these methods theoretically or empirically, based on existing literature?
- Could you elaborate on why the resampling method from (Ba et al., 2021) was excluded as a comparative method, despite the computational resources available (e.g., “NVIDIA Quadro RTX 6000 GPU”)? Is this method genuinely computationally infeasible for UCI benchmark datasets, or were there other factors influencing its exclusion?
  - So, could you include the resampling method from Ba et al. (2021) in your comparisons, particularly on the UCI datasets, to strengthen the evaluation? If this is not feasible, could you provide a more detailed justification for why it is computationally infeasible, even with the available GPU resources? Additionally, if an empirical comparison is truly not possible, could you discuss how SMI theoretically compares to the resampling approach?

### Soundness
2

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
3

### Summary
The posterior of a Bayesian model is sometimes intractable, calling for approximate inference techniques. This paper focuses on the idea of approximating the Bayesian posterior with a mixture distribution where each component is parameterized separately but still in the same family. By viewing the ELBO as an objective with permutation invariant parameters, this paper incorporates ideas from Nonlinear-SVGD (NSVGD) and develop a Stein-style update rule of the mixture parameters. The resulted method, called Stein mixture inference (SMI), prevents itself from variance collapse. The paper also shows that asymptotically the optimized bound is an ELBO.

In the experiments, it is first shown that Stein-based methods suffer from variance collapse in synthesized Gaussian models and 1D regression models. In contrast, SMI and vanilla VI (OVI) produce the desired uncertainty. On the UCI regression benchmarks, SMI gives the best NLL in the most cases, comparing with other Stein-based methods and OVI.

### Strengths
I believe the method is novel and the main idea is sound. The claims are clearly presented and supported by empirical evidences. Overall it is a complete work with a few concerns.

### Weaknesses
This paper has the title of ELBOing Stein, but I would rather call it Steining ELBO, which seems a bit unnecessary. To convince me to increase my score, I would like to see a discussion of [1], which also uses a mixture distribution to approximate the posterior.

If one is using a mixture distribution to target the Bayesian posterior, the most direct approach would be to try VI, instead of deriving a complicated Stein-based method. One pro of VI is that the mixture weights can be adjusted while one con is that it does not fully make use of the exchangeability of parameters. However, this work only considers mean-field VI, which is a really weak baseline. I would like to see how the permutation invariance helps the optimization of the mixture distribution.

It is not surprising that optimizing an VI objective prevents the approximate posterior from the pitfalls of SVGD. As shown in the paper, OVI does not have the issue. The argument that "SMI is more particle-efficient than SVGD" is translated to me as "VI with mixtures is more particle-efficient than SVGD". Then what is the point of using Stein?

Line 150 says that "Particle methods are attractive due to their freedom from strong parametric assumptions". Mixture distribution in this paper seems to be a strong parametric assumption, especially when it uses fewer particles than SVGD, which further drags this work away from Stein.

The experiment section is also rather weak. The benchmark models all have very low dimensions. I expect a Bayesian inference algorithm in 2024 to be tested on more recent benchmarks, like models in posteriorDB, or larger BNN problems.

### Questions
- How does SMI compare with ADVI with mixtures? 
- How is each component in the mixture distributions parameterized?

### Soundness
3

### Presentation
3

### Contribution
3
