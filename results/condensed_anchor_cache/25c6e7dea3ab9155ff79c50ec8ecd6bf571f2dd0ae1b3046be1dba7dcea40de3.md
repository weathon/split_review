- Decision: Accept
- Scores: 8, 8, 6, 6, 6, 3

## Merged Review

### Summary

The paper addresses the problem of missing data in simulation-based inference (SBI), formalizing how naive imputation can bias posterior estimates. It proposes RISE (Robust Inference under imputed SimulatEd data), which jointly learns an imputation model (based on neural processes) and a posterior estimator (neural posterior estimation with normalizing flows). The method is amortized and can handle different missingness mechanisms (MCAR, MAR, MNAR). Experiments on four SBI benchmarks and two intractable models show RISE outperforms baselines (NPE-Zero, NPE-Mean, NPE-NN) in terms of MMD and RMSE.

### Strengths

- **Important, timely, and underexplored problem**: Handling missing data is a significant challenge for real-world SBI applications (astrophysics, high-energy physics). The paper draws attention to this issue and provides a solution. (R1, R2, R3, R4, R5, R6)
- **Clear motivation and formalization**: The paper clearly shows how naive imputation (zero, mean) can bias posteriors (Figure 1) and provides a formal analysis of bias under MCAR, MAR, MNAR. Proposition 2's simplification of the RISE loss is convenient. (R1, R3)
- **Novel and general method**: Jointly learning an imputation model and inference network within the NPE framework is original and more general than prior work. The use of neural processes for imputation is a sensible choice. (R1, R2, R3, R4)
- **Amortization across missingness levels**: RISE-Meta can generalize to varying levels of missing data, which is practical. (R3)
- **Evaluation across diverse problems**: The evaluation spans statistical benchmarks (Ricker, OUP, etc.) and real-world datasets (Adrenergic, Kinase). RISE consistently outperforms baselines. (R2, R4, R5)
- **Good presentation and clarity**: The paper is generally well-written and clearly structured, with visually appealing figures. (R1, R4, R6)

### Weaknesses

**Missing comparisons and inaccurate literature coverage**

- **Overlooked prior work on learned imputation in SBI**: The paper fails to discuss Lueckmann et al. (2017), which automatically learns imputation values for NPE using an MDN embedding network, evaluated on the same Hodgkin-Huxley benchmark. RISE's NPE-NN baseline appears very similar to that approach; a direct comparison or discussion is needed. (R1, R5)
- **Inaccurate description of Gloeckler et al. (2024, Simformer)**: The paper claims the Simformer cannot handle MAR/MNAR and only estimates partial posteriors given fixed missing indices. In fact, the Simformer can perform arbitrary conditioning and evaluation, essentially learning imputation. The authors should provide a more accurate discussion and ideally compare RISE against Simformer under MCAR. (R1, R4, R5)
- **Misrepresentation of Wang et al. (2024)**: The paper's summary of Wang et al. (2024) is poor; it fails to mention that they use data augmentation with artificially missing values and a binary mask indicator during NPE training. This approach is not simply constant-value imputation, and the paper does not adequately justify why it is insufficient. (R2, R6)
- **Limited baseline comparisons**: The only baselines are NPE-Zero and NPE-Mean (constant imputation), which are overly simplistic and introduce obvious bias. Comparisons against Wang et al.'s mask-augmented NPE, Gloeckler et al.'s Simformer, and traditional imputation methods (EM, MICE) are missing. (R2, R4, R6)
- **Incomplete related work on missing-data handling**: The paper omits relevant methods from the deep learning literature (GAIN) and traditional statistics (expectation-maximization, MICE). It also misses prior SBI works on missing data (e.g., arXiv:2211.03747, IOP Science 2023). (R3, R6)
- **Citation inaccuracies**: The VAE paper is cited as 2022 instead of 2013. Radev et al. (2022) should be Radev et al. (2020). NPE is credited to Radev et al. (2022) instead of Papamakarios & Murray (2016). Gloeckler et al. is an ICML paper, not arXiv. (R1, R5)

**Incomplete evaluation and insufficient metrics**

- **Only MMD and RMSE reported**: These metrics are insufficient for assessing posterior accuracy and calibration. MMD is sensitive to kernel bandwidth; RMSE measures point estimation, not density quality. The paper should report: C2ST, negative log probability of true parameters under the posterior (log nominal density), and median distances between simulated and observed data. (R1, R4, R5)
- **No calibration metrics**: Calibration (e.g., expected coverage, simulation-based calibration, probability calibration error) is critical, especially since approximation errors in the imputation model can inflate posterior variance. The paper does not assess whether posteriors are well-calibrated. (R1, R2, R5)
- **Missing quantitative evaluation on Hodgkin-Huxley**: The HH example only provides qualitative analysis. Metrics such as SBC, C2ST, or log posterior density should be reported here as well. (R5)
- **Meta-learning results incomplete**: Meta-results for Ricker and OUP (beyond the simple Gaussian example) are not shown. (R5)

**Methodological concerns**

- **Trivial solution for single observations not addressed**: For a single observation, one can simply remove the missing indices from the simulated data and train the posterior only on the observed dimensions. The paper focuses on single-observation examples and does not discuss this trivial alternative. (R6)
- **Joint training may not be beneficial**: The objective in Equation (5) appears separable into independent objectives for the imputation model and inference model (disjoint parameters, fixed expectation). The paper does not justify why joint training is necessary or beneficial. (R6)
- **Gaussian assumption for imputation model not highlighted as limitation**: The imputation model assumes a Gaussian distribution (with mixture expansion). While theoretically infinite mixtures are flexible, this is computationally infeasible, and the Gaussian assumption can affect posterior credibility (as the authors themselves note in line 476). This contradiction between claiming robustness and acknowledging credibility issues is confusing. (R3)
- **Choice of MAFs over NSFs not justified**: Neural Spline Flows (NSFs) are more flexible and widely used in SBI. The paper uses MAFs without justification or an ablation study comparing the two. (R4)
- **Overkill for simple data**: For low-dimensional data with simple missingness (MCAR/MAR), data augmentation with a mask indicator (as in Wang et al.) is simpler and efficient. RISE may be unnecessarily complex. (R2)

**Missing technical details and ablation studies**

- **No simulation budgets reported**: It is unclear how many simulations were used for each method and benchmark. This is essential to assess data efficiency. (R1, R2)
- **No computational cost analysis**: Training time and memory usage compared to baselines are not provided. The extra complexity of neural processes and normalizing flows may be costly. (R1, R3)
- **No ablation on imputation model quality**: The paper states that learning the imputation model correctly is central, but does not study how errors in $p(x_{miss} | x_{obs})$ affect posterior accuracy and calibration. (R2)
- **Sensitivity to neural process architecture not studied**: No ablation on choice of NP architecture or hyperparameters. (R3)
- **No code provided**: Source code was not made available for reproduction. (R3, R6)
- **Formalization not novel**: Equations (2-3) are standard missing-data formulations, not specific to SBI. Propositions 1 and 2 are straightforward. (R2)
- **Notation confusing**: The use of $x_{obs}$ for a subset of *simulated* data (not actual observed data) is misleading. Bold/unbold notation for vectors is inconsistent. (R2, R6)
- **Algorithm 1 should illustrate ensemble**: The method yields an ensemble of posteriors (one per imputation sample), but the algorithm does not show this explicitly. (R2)
- **Section 5 structure confusing**: The description of datasets is unclear. (R3)
- **Title too broad**: The title describes an area, not the specific method. (R6)

**Reviewer disagreement**: One reviewer (R6) is significantly more negative, arguing that the joint training is not justified, the trivial solution of removing missing indices is overlooked, and the literature review is insufficient. This contrasts with other reviewers who find the method novel and valuable. (R6)