# CoLiDE: Concomitant Linear DAG Estimation

- Decision: Accept
- Scores: 6, 8, 3

## Abstract
We deal with the combinatorial problem of learning directed acyclic graph (DAG) structure from observational data adhering to a linear structural equation model (SEM). Leveraging advances in differentiable, nonconvex characterizations of acyclicity, recent efforts have advocated a continuous constrained optimization paradigm to efficiently explore the space of DAGs. Most existing methods employ lasso-type score functions to guide this search, which (i) require expensive penalty parameter retuning when the \emph{unknown} SEM noise variances change across problem instances; and (ii) implicitly rely on limiting homoscedasticity assumptions. In this work, we propose a new convex score function for sparsity-aware learning of linear DAGs, which incorporates concomitant estimation of scale and thus effectively decouples the sparsity parameter from the exogenous noise levels. Regularization via a smooth, nonconvex acyclicity penalty term yields CoLiDE (\textbf{Co}ncomitant \textbf{Li}near \textbf{D}AG \textbf{E}stimation), a regression-based criterion amenable to efficient gradient computation and closed-form estimation of noise variances in heteroscedastic scenarios. Our algorithm outperforms state-of-the-art methods without incurring added complexity, especially when the DAGs are larger and the noise level profile is heterogeneous. We also find CoLiDE exhibits enhanced stability manifested via reduced standard deviations in several domain-specific metrics, underscoring the robustness of our novel linear DAG estimator.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of DAG structure learning from a score-based viewpoint for linear models. 
The authors propose a new score function that also estimates the noise levels and experimentally show that it can lead to better accuracies by leveraging recent advances in continuous non-convex characterizations of DAGs.

### Strengths
* The paper is clearly written and the contributions are easy to digest.
* The proposed score leads to structure improvements w.r.t. sota methods.

### Weaknesses
 * Significance: The paper considers only linear models, hindering the significance of the proposed loss function. While linear models are a common starting point, the real-world applicability of DAG learning often involves non-linear relationships. The restriction to linear models limits the impact of the proposed method, as many practical scenarios exhibit non-linear dependencies. The paper does not adequately address how the proposed score function could be extended or adapted to handle non-linear models, which is a critical limitation.
* Novelty: The authors borrow ideas from concomitant lasso, and straightforwardly apply it to the score function for DAG learning. While it is totally okay with borrowing ideas from prior work, it feels that this is indeed the only technical contribution of the paper. The optimization part feels identical to prior work expect for the extra noise terms. The core idea of incorporating noise variance estimation into the score function, while useful, lacks substantial novelty beyond the existing literature on concomitant variable selection. The paper does not provide a deep theoretical analysis of why this specific adaptation leads to improved DAG learning performance compared to alternative approaches.

### Questions
* With respect to my point in the weaknesses section, in my opinion, it would be more enlightening to show that the proposed score function leads to identify the true underlying DAG. The current contribution feels like just "another score function" with no guarantees of identifiability. The non-equal noise variances was also studied in Loh and Buhlmann (2014) where they proposed a weighted LS that would lead to identifiability of the true DAG, this weighted LS depends on the noise levels as well, I wonder if jointly optimizing such objective would also lead to accuracy improvements.

* I wonder if the authors experimented with non-linear models as well?  Given that I would consider this work to be "empirical", it would be good to use these ideas into nonlinear models as well. 

* I will also note, a recent method called TOPO by Deng et al. (2023) "Optimizing NOTEARS objectives via topological swaps" shows improvements in structure estimation for score-based methods. Their theory suggests that given a convex score (as in this paper) their optimization algorithm would guarantee a local optimum. It would be interesting to see if using the proposed convex score + TOPO can  obtain even more accurate DAGs, specially for non-equal variances. Finally, the same authors have provided initial insights into global optimality of continuous DAG learning methods which can also help to motivate this line of work in the continuous-constrained framework, see Deng et al (2023) "Global Optimality in Bivariate Gradient-based DAG Learning".

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a new continuous optimization problem for DAG learning. It leverages results from the concomitant scale estimation literature to learn a weighted adjacency matrix while estimating the scale of the exogenous noise variables. The experiments clearly show that optimizing the new objective (by inexact block coordinate descent) instead of the original l1-regularized objective of DAGMA results in better estimation of the graph across various settings.

### Strengths
1. The paper tackles an important problem of interest to the general ICLR community. 

2. The proposed regularization is general enough that it can be plugged in many of the continuous optimization problems recently proposed for learning DAGs. The work's impact is hence potentially high as it could improve performance of many state-of-the-art methods.

3. The paper is generally well presented. Its claims are well supported by an extensive empirical analysis that illustrates the DAG recovery capabilities of the method on several settings and for noise estimation.

### Weaknesses
1. Although the adjacency matrix $W$ can be efficiently updated with stochastic gradient steps, the closed-form for the noise scale is evaluated on the full data because it is not decomposable. Specifically, the current formulation requires computing the noise scale using the entire dataset, which hinders the method's applicability to large-scale datasets. This limitation should be highlighted in the text. An efficient approximation for the noise scale update could be discussed and empirically evaluated to mitigate this issue.

2. The derivation of Problem 2 is not clearly explained. The assumptions under which the noise-dependent terms appear in the objective function need to be explicitly stated. Providing a detailed derivation in the appendix would greatly enhance the paper's clarity and reproducibility. This would in particular allow for verifying if the sparsity inducing term $||W||_1$ can be replaced by the score-equivalent term $||W||_0$, used e.g. in [1,2], without loss in noise estimation performance. The use of the L0-norm could potentially lead to better performance in certain scenarios, and a thorough discussion of this possibility would be beneficial.

3. The paper lacks a detailed description of the hyperparameter tuning process, particularly for $\lambda$. In Section 4.1, it is only mentioned that $\lambda$ was "empirically determined." A more comprehensive explanation of the tuning procedure, including the range of values considered and the criteria used for selection, is necessary to ensure the reproducibility and robustness of the results.

4. The results for Sortnregress are not fully presented in Figure 1. While the text mentions Sortnregress results for two values of the noise scale and a single graph type, including all results for this baseline across all settings in Figure 1 would improve its readability and provide a clearer comparison. This would allow readers to easily identify which settings are trivial and which are more challenging, thus highlighting the strengths and weaknesses of the proposed method.

### Questions
(minor) There is a sign typo in the second-last equation of page 14.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work proposes a new differentiable structure learning method for learning linear acyclic model that eliminates the assumption of equal error variances needed by several existing differentiable methods based on least squares. Building upon existing idea on smoothed concomitant lasso, the proposed method develops a regression-based score function that includes concomitant estimation of scale and decouples the sparsity parameter from the exogenous noise levels. Experiments with simulated and real-world datasets are provided.

### Strengths
The problem considered is highly relevant because it is important to relax the assumption of equal error variances to handle heteroscedastic noises.

### Weaknesses
The formulation (5) in the heteroscedastic setting lacks identification guarantee. It is unclear which specific settings it is theoretically correct for. For the linear Gaussian setting, one should use Gaussian likelihood, e.g., in GOLEM, while for linear non-Gaussian setting, one should use non-Gaussian likelihood, e.g., in NOTEARS-ICA.

There are some possible issues with the experiments, elaborated in the next section.

There is a significant drop in performance after data standardization in heteroscedastic settings, as shown in Appendix E.4. This contrasts with methods like GES/PC, which are less sensitive to such transformations. This suggests that the proposed method may not fully address the challenges posed by heteroscedasticity.

The discussion of identifiability in Appendix C lacks rigor. The argument involving $\lambda=0$ and $\mu_k \rightarrow \infty$ leading to equation (40) and then referencing (Ng et al., 2020) is problematic. The proof in (Ng et al., 2020) still requires sparsity, contradicting $\lambda=0$. Furthermore, the use of $\mu_k \rightarrow \infty$ appears inconsistent with the barrier method's typical approach of $\mu_k \rightarrow 0$.

### Questions
- Does the method work after data standardization (see the study by Reisach et al. (2021)? Since the method is specifically for heteroscedastic setting, this experiment should be included to support the claim.
- For heteroscedastic Gaussian noise, the paper should compare the recovery results of Markov equivalence classes instead of DAGs, since the true DAG cannot be identified in theory.
- Regarding performance of DAGMA and GOLEM:
    - For DAGMA, did the authors try using the log-likelihood in the heteroscedastic setting? The authors of DAGMA paper consider such log-likelihood for nonlinear setting, but could be straightforwardly done for linear setting.
    -  For GOLEM, did the authors use the EV version to initialize the NV version, as suggested by their paper? Also, Section 5.1 says that GOLEM is based on profile-log-likelihood--I think a more straightforward comparison with Eq. (5) is their version without profiling.
    - Did the paper try to tune the hyperparameters for these two methods, since the settings considered here are quite different from their papers?
- What does "decouples the sparsity parameter from the exogenous noise levels" mean? I did not manage to find any elaboration or explanation of it.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
