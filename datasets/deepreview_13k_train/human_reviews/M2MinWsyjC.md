# SHIFTING TIME: TIME-SERIES FORECASTING WITH KHATRI-RAO NEURAL OPERATORS

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
We present an operator-theoretic framework for time-series forecasting that involves learning a continuous time-shift operator associated with temporal and spatio-temporal problems. The time-shift operator learning paradigm offers a continuous relaxation of the discrete lag factor used in traditional autoregressive models enabling the history of a function up to a given time to be mapped to its future values. To parametrize the operator learning problem, we propose Khatri-Rao neural operators -- a new architecture for defining non-stationary integral transforms which achieves almost linear cost on spatial and spatio-temporal problems. From a practical perspective, the advancements made in this work allow us to handle irregularly sampled observations and forecast at super-resolution in both space and time. Detailed numerical studies across a wide range of temporal and spatio-temporal benchmark problems suggest that the proposed approach is highly scalable and provides results that compares favourably with the state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach for time series forecasting by learning a continuous time-shift operator with the Khatri-Rao Neural Operator (KRNO). Unlike traditional autoregressive models that require regular sampling intervals, KRNO handles irregularly sampled data and can forecast in high resolution across both time and space. Through extensive testing on temporal and spatio-temporal datasets, the authors demonstrate that KRNO performs competitively against state-of-the-art methods in terms of scalability, accuracy, and computational efficiency.

### Strengths
1. Robustness to Irregular Sampling: KRNO effectively addresses the challenge of irregularly sampled data, making it applicable in real-world scenarios where regular sampling isn’t guaranteed.
2. Computational Efficiency: The model achieves almost linear computational costs while allowing for exact, non-stationary kernel evaluations, which is highly advantageous for large-scale spatio-temporal problems.
3. High-Resolution Forecasting: KRNO’s ability to generate super-resolution forecasts in both time and space allows it to capture fine-grained details that are valuable in fields like climate modeling and medical monitoring.
4. Comprehensive Benchmarking: The paper includes thorough experiments across various benchmark datasets, highlighting KRNO’s performance in comparison to existing models.

### Weaknesses
 - Complexity and Resource Demand: KRNO’s architecture and training process are complex and may require substantial computational resources, which could limit its accessibility and practical deployment. The paper does not fully explore the computational scaling of the method with respect to the input size, particularly for high-resolution spatio-temporal data. A more detailed analysis of memory usage and training time as a function of spatial and temporal resolution would be beneficial. 
- Generalization Across Data Types: While KRNO performed well on the tested datasets, it’s unclear how well it generalizes to data with distinct irregular patterns or high variability, which may affect its robustness. The experiments do not sufficiently explore the impact of different types of irregular sampling patterns on the model's performance. For example, it is unclear how the model would perform with highly clustered or sparse sampling patterns, which are common in real-world datasets.
- Hyperparameter Sensitivity: The need for extensive hyperparameter tuning (such as for tp and tf) in KRNO might increase the complexity of implementation, especially in cases where computational resources are limited. The paper lacks a systematic study of the impact of these hyperparameters on the model's performance and how to choose them effectively for different types of datasets. A sensitivity analysis of these parameters would be valuable.

### Questions
- How does KRNO handle irregular patterns or noise in datasets that differ significantly from those used in the experiments?
- While the authors claim near-linear computational costs, could more specific benchmarks on processing time and resource usage for high-resolution spatio-temporal data be provided?
- Are there specific industry applications where KRNO’s advantages would be most beneficial, or is it generally applicable across various domains?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces a continuous time-shift operator for time-series forecasting. Using Khatri-Rao neural operators, they claim to achieve efficient handling of irregular sampling and high-resolution forecasting in spatio-temporal settings, with results that are claimed to compete strongly with current methods.

### Strengths
It is an interesting take on the topic and I appreciate tackling the spatio-temporal forecasting problems. I like the choice of datasets they are rather interesting. Appeal to Koopman operator theory is quite welcome.

### Weaknesses
A lot of the background theory behind the methodology seems like there is some intentional obfuscation of the reader going on. This can be seen in the proof in Appendix A which is a very standard application of Gronwall's Lemma which can be found in most ODE textbooks (the authors use William F Ames and BG Pachpatte. Inequalities for differential and integral equations, volume 197), so really one should just cite its use rather than present a one page proof for it. To be clear I'm not against (re)showing of very standard proofs, but there should be signifanctly good reason, such as branching off of an intermediate step and so on. It is somewhat like presenting a "proof for the law of large numbers" when one should really in principle cite it as is common practice. Because this occurs it leads me to suspect a lot of the mathematical formulation shown, and overall notation  in this paper is just there for an intentional obfuscation for the reader. What could be intersting in this case, for example, would be if one could charactise the nature of constant C, otherwise there is not much point. 

As a result this (what is suspected to be) intentional mathematical obfuscation, Lines 85 - 107 can more or less be written in 3-4 lines with the same properties as follows:
"Consider an ODE z˙(t) = F(z(t)), z(0) = z0 with Lipschitz continuous F: Rn → Rn over t ∈ [0,T]. While the classical flow map solution maps only initial conditions to solutions, we define a time-shift operator At,tf tp that maps the history of z over [tp,t] to its future values over (t,tf], where 0 ≤ tp < t < tf ≤ T. At,tf tp is continuous and satisfies the semigroup property: At2,tf tp = At2,tf t1 ◦ At1,t2 tp . Unlike discrete autoregressive models, this continuous-time formulation naturally handles irregularly sampled data without requiring adjoint sensitivity calculations as in neural ODEs."

Similarly I feel there is no need for Proposition 1 or its associated proof. The authors do state: "Proposition 1 follows from similar results for Kronecker structured GP regression (Saatçi, 2011)" -- which gets the main point across essentially since it is not "similar" but rather more or less the same since by definition the "Khatri-Rao product *is* the Kroneckor product just generalized to block matrix structures. See the first 1-2 lines of: https://en.wikipedia.org/wiki/Khatri%E2%80%93Rao_product 
I simply cannot see the benefit of dedicating then, a lengthy proposition, and a proof in App B, unless I may be missing something.

As a result of establishing this link the pytorch implementation of the Khatri-Rao product doesn't seem completely necessary (Appendix C), since this is a standard implementation in many python / pytorch libraries on tensor algebra which are very, very optimized already, so I don't fully get its explicit novelty of why one would present the code for it as a novelty (or at least why there is a whole section dedicated to it - unless I am missing something). See: 
https://tensorly.org/dev/modules/generated/tensorly.tenalg.khatri_rao.html

Given that Appendix A - C do not seem to be genuine novelties from what I can tell, Appendix D appears to be the crux of the novelty  but it is only a few lines long, and rather than push for any meaningful novelty it gets relegated to a reference unfortunately. 

Moreover Figure 8 (Appendix D), the forecasts for GasRateCo2, Wooly, HeartRate seem a little bit worrying in selling the applicability of this model to real world data.

All in all, I think rather than finished work I think this could be the potential of a good start. May I suggest submitting these initial results to a workshop where the ideas can be foundationally built upon and further developed perhaps.

### Questions
Since the questions section is meant for persuading the reviewer (of which I am open), I may defer to the addressing of points in the above "weakness" section, of which quite a few points have been raised.

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
This paper addresses the challenges of irregular sampling problems in autoregressive models. A Khatri-Rao neural operator is proposed that 1) allows continuous relaxation of the discrete lag factor for irregular sampling and 2) defines non-stationary integral transforms for better model flexibility. Empirical results show improved performance on a range of benchmark problems compared to baseline models.

### Strengths
1. The problem of irregular sampling in time-series forecasting is important.
2. The idea of the continuous time-shift operator is creative and the methodology is well-structured.
3. Experiments were performed on temporal and spatio-temporal problems to present the effectiveness of the proposed method.

### Weaknesses
1. The authors mentioned the time-shift operator maps the entire continuous history of the past time-window into its future values. Could the authors discuss the benefit of this neural operator versus neural controlled differential equations [1] and its variants? Specifically, the paper should address the potential for neural CDEs to model the underlying dynamics more explicitly, and how this approach compares in terms of capturing long-range dependencies and handling complex, non-linear temporal patterns.
2. The presentation in Section 3 needs to be better. In Figure 2 and Figure 4, the authors could provide a relative error similar to Figure 5 to better present the prediction accuracy. Figure 2 and Figure 4 are not referred to in the main text. In Figure 4, the authors should mark which variables are ground truths and which are predictions. Also, could the authors explain what causes the large fluctuations of certain variables in Figure 4 and Figure 5 error bars? It is unclear if these fluctuations are due to inherent instability in the model, or if they are related to specific characteristics of the datasets. Table 5 seems to show that the time resolution affects the performance of the proposed method. Could the authors further explain that? It would be beneficial to understand how the model's performance scales with varying time resolutions, and if there are optimal ranges for the time resolution parameter.
3. The ablation study is not sufficient. The authors should consider comparing the time complexity of the proposed method with Graph Neural operator, Multipole Graph Neural Operator, and Fourier Neural Operator. The comparison should include a detailed analysis of computational costs (both training and inference), memory usage, and scalability with respect to input size. Also, the effect of time resolution and spatial complexity should also be addressed. Specifically, how does the model's performance change with increasing spatial resolution, and what are the trade-offs between accuracy and computational cost?

### Questions
Please find the questions in the weaknesses section above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this manuscript, the authors developed a time series forecasting method based on a neural operator, called Khatri-Raio neural operator (KRNO). In essence, aside from the theoretical development, the proposed KRNO takes a window of time series data as an input and makes a prediction of a future time step. KRNO utilizes a cosine positional embedding to account for the time series data sampled at irregular intervals. KRNO is tested against a set of spatio-temporal problems as well as a few benchmark time series prediction problems. It is shown that KRNO achieves a state-of-the-art performance in many of the benchmark problems.

### Strengths
The manuscript is well written. It clearly defines the problem set up, succinctly outline the background, and introduce the method. The proposed method is theoretically robust compared to most of the recent time series papers, which are focused more on engineering aspects.

### Weaknesses
One of the major concerns is the applicability of the proposed method for a broader problem. While the proposed neural operator based method is interesting, most of the real data are in essence stochastic processes due to aleatoric uncertainty. For many physics data, the observation noise and natural variability make the observation stochastic. It is unclear if the neural operator theory can be extended to the modeling of such stochastic processes. More over, the model is based on modeling an autonomous system without any exogenous effects, which limits the class of problems that the proposed method can be applied.

One of the major claims of the method is its capability of dealing with irregularly sampled time series data. But in the experiments it is not shown how the proposed method performs with irregularly sampled time series data. The method is based on a numerical approximation of an integral equation. Then, the accuracy of the numerical integration strongly depends on the choice of the quadrature points, which makes the claim about modeling any irregular time series weaker. Depending on the sampling points, it may even induces a numerical instability.

It looks like there are some inconsistencies between the theory and the final model. Probably, it is because some of the terms are not fully explained in the manuscript. See the questions below.

### Questions
1. The notation on the right hand-side of Eq (6) is confusing. On LHS, $\kappa((t,X),(t',x'))$ is $R^{q\times p}$. But, on RHS, a similar notation $\kappa((t,X),(t,X))$ is $R^{Nq \times Np}$. Please, check the notations throughout the paper and distinguish between them to avoid a confusion.

2. Up to Eq. (8), the kernel depends only on the quadrature point, i.e., $\kappa((t,x),(t',x'))$. Then, suddenly, in section 2.3, the kernel becomes a function of the input data, $\kappa(U^{t_i}_p)$, which is inconsistent with the theory. If a neural network is used as a nonlinear map between the input data (NOT quadrature point) and output matrix, what's the difference between the proposed neural operator based method and other window based time series models? It becomes very similar to the popular mixer architectures.

3. How do you compute the weights $w$ in Eq (6)? The choice of $w$ is closely related with the accuracy of the numerical integration.

4. The authors claimed that their method can directly learn the "exact kernel". But the "exact kernel" is not a general kernel. It already made a very strong assumption on the kernel structure such that the kernel is based on a set of orthogonal projections of the input space. While the authors made an excuse that such orthogonal decomposition is widely used, for example, in GP, it is used in other previous methods not because it is robust and improves the approximation, but because it makes the problem easier to tackle. 

5. How are the error bars in the experiments computed. The proposed method is deterministic. It is not clear what 1,000 test simulation indicates.

### Soundness
3

### Presentation
3

### Contribution
2
