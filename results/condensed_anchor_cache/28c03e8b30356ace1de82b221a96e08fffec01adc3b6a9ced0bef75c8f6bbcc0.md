- Decision: Reject
- Scores: 5, 3, 3, 5

## Merged Review

### Summary
The paper proposes a variational inference framework for causal discovery in time series data that originates from a mixture of different causal models. It simultaneously infers underlying causal graphs, functional equations, and per-sample mixture component assignments by maximizing an ELBO. Two variants are given (linear/additive noise and nonlinear/history-dependent noise), and identifiability is proven under mild assumptions. The method is evaluated on synthetic data, NetSim (fMRI), and DREAM3 gene network data, with comparisons to Rhino, PCMCI⁺, and VARLINEAL. Scores vary considerably: two reviewers rated 5 (positive, interested in the problem), and two rated 3 (critical of novelty and experimental design).

### Strengths
- The problem of discovering causal graphs from time series that are mixtures of different structural causal models is interesting, relevant, and under-explored (all reviewers).
- The variational inference formulation is a simple but effective extension that enables end-to-end training and is flexible with respect to the choice of core causal structure learning algorithm (R2, R4).
- Theoretical identifiability results for the mixture model are provided (R1, R4).
- Experiments are conducted on both synthetic and two real-world datasets (NetSim, DREAM3) with multiple baselines (R4).
- Ablation studies (e.g., varying K, cluster imbalance) are included (R4).
- Competitive performance (AUROC, F1, SHD) is reported on training data (R1, R2).
- The exposition is generally clear (R1).

### Weaknesses
- **Training‑data‑only evaluation:** All reported results are on training data. No generalisation performance on held‑out test samples from the same mixture distribution is given. This is a major limitation for assessing practical utility (R1, R2).  
- **No per‑sample probabilistic encoder:** The method learns deterministic sample‑specific parameters rather than an encoder that outputs a K‑way categorical variable; a probabilistic encoder would give a cleaner generative interpretation and likely allow test‑time inference (R2).  
- **Only one core causal discovery method tested:** Despite claiming flexibility, only the Rhino algorithm is used as the backbone; experiments with other base SGD‑based causal structure learners are missing (R2).  
- **Missing analysis of graph diversity:** The paper does not report how different the causal graphs in the mixture are (e.g., average SHD within clusters) or how the distance between graphs affects performance (R1).  
- **NetSim data concerns:** The NetSim time series are nearly i.i.d. (records are far apart), and past work shows that treating them as i.i.d. often yields better results. The paper does not compare to an i.i.d. analysis, which would be an important baseline for a time‑series method (R3).  
- **DREAM3 results near random:** For the DREAM3 gene network, all methods obtain an AUROC around 0.5, with negligible differences between them. This experiment does not demonstrate any advantage of the proposed approach (R3).  
- **Unclear metric definitions:** The paper uses AUROC and F1 but does not state whether they refer to adjacency (edge existence) or orientation (edge direction) (R2, R4).  
- **Inappropriate or missing baselines:**  
  - Baselines are not designed for multiple DAGs / mixture SCMs; no comparison with other multi‑DAG algorithms (R4).  
  - Comparison with Rhino applied to *grouped* data (using the true clustering) is missing, which would be a natural upper bound (R4).  
  - PCMCI⁺ results may be affected by post‑processing that could bias the comparison (R4).  
- **Netsim‑permuted experiment inherently favorable:** Permuting variables explicitly creates the mixture structure that the method assumes; results may be inflated relative to non‑mixture alternatives (R2).  
- **Limited statistical rigor:** Synthetic experiments average only 3 runs; reviewer expresses that this is insufficient for reliable conclusions (R4). Additionally, runs are not clearly described as independent dataset generations (R4).  
- **Missing details:**  
  - The hyperparameter K (number of mixture components) used for DREAM3 is not reported (R2).  
  - No illustrative toy example is provided (R1).  
  - The definition of \(a_i\) in Theorem 1 is unclear (R4).  
  - The SCM equations (1) and (6) are inconsistent; it is not clear whether additive noise is assumed (R4).  
  - The notation \(g_1,g_2\) in Theorem 1 is undefined – likely a typo for \(h\) (R1, R4).  
  - The statement “learning a mixture is only beneficial when SCMs differ significantly” is not quantified (R4).  
- **Missing code:** No code is provided, making results unverifiable (R4).  
- **Reviewer disagreement:** Two reviewers (scores 5) found the novelty and empirical evaluation adequate, while two (scores 3) considered the variational extension straightforward and the experimental validation insufficient, particularly concerning generalisation and dataset choices.