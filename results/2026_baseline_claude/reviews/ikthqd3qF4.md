## Summary

This paper introduces a principled framework for evaluating and tuning unsupervised anonymous record linkage algorithms without labeled training data. The central idea is to exploit a structural constraint common in transactional data—that an individual can have at most one positive outcome (e.g., originating at most one first-lien mortgage)—to derive observable lower bounds on precision and relative recall. The authors instantiate this framework using hierarchical agglomerative clustering on 65.5 million HMDA mortgage applications, achieving an estimated 92.3% precision at their preferred hyperparameter setting.

---

## Strengths

- **Genuinely novel evaluation framework**: To the authors' knowledge (and the reviewer's), deriving observable lower bounds on precision and recall in unsupervised settings without any labeled data is new. The insight—using structural impossibility of multiple originations in a true-positive cluster to make Pr[Mult] an informative proxy for false positive rate—is elegant and non-trivial. The formalization in Theorem 1 and Corollaries 1–2 is clean and well-developed.

- **Method-agnostic scope**: The derived bounds depend only on predicted labels and the observable probability of origination, making them applicable to any label-generating algorithm. This broadens the contribution beyond a specific clustering approach to a general meta-evaluation tool for unsupervised record linkage.

- **Compelling simulation validation**: Figures 3 and 4 provide a direct comparison between the true precision (observable only in simulation with ground-truth identifiers) and the proposed lower-bound estimates. The close correspondence—e.g., 93.7% estimated bound vs. ~95% true precision for the "with date" specification at ε=0.06—gives convincing evidence that the bounds are tight and practically useful.

- **Large-scale application and scalability**: Applying the framework to 65.5 million real mortgage applications using an O(ℓ²) agglomerative clustering algorithm (fastcluster) demonstrates practical viability on datasets far exceeding what most ML papers address.

- **Clear practical utility for hyperparameter tuning**: The precision–sample-size frontier (Figure 5) provides an actionable, label-free tool for model selection. The explanation of how Corollary 2 recovers the optimal point on that frontier is a clean contribution to practitioners dealing with privacy-constrained data.

---

## Weaknesses

### Fatal
None.

### Major

- **Restriction to size-2 clusters substantially constrains recall**: Footnote 4 discloses that "we drop all clusters with more than two applications" in both the simulation and the real application. This is a consequential methodological choice. Real cross-applicants who submitted three or more applications are excluded from identification, potentially making true recall significantly worse than the reported ~92% bound. The paper does not quantify how many cross-applicants submit 3+ applications in either the simulated or real data. The conclusion that recall is "only minimally lost" is not substantiated without this analysis.

- **Absolute recall bounds require unknown P_tot**: Corollary 1 gives Recall(θ) ≥ α̂(θ) × N⁺(θ) / P_tot, but P_tot (the total number of true cross-applicants) is unknown. In practice, the bounds are only used in a relative sense to rank specifications, not to compute actual recall values. This limits the paper's claim of providing observable recall lower bounds—they are lower bounds only up to an unknown scalar, and the absolute recall reported in the simulation (92%) exploits known ground truth rather than the proposed bound alone. This gap between the theoretical framing and practical usage should be more carefully stated.

- **No comparison to alternative record linkage methods**: The method is presented as both a linkage algorithm and an evaluation framework for arbitrary algorithms. However, all experiments compare only different hyperparameter settings (ε, distance function) of the same agglomerative clustering approach. The value of the framework for comparing genuinely different algorithms (e.g., blocking-based vs. embedding-based methods) is not demonstrated, which is a missed opportunity given the paper's "method-agnostic" framing.

### Minor

- **Tightness of the bound is context-dependent**: The bound Pr[False] ≤ Pr[Mult]/p² is tight only when Pr[Mult|False] = p², which holds exactly for size-2 clusters under independence. For clusters of arbitrary size, the bound could be quite loose, and the paper does not characterize the gap. The discussion in Remark 1 is helpful but brief.

- **Assumption 2 (monotone origination probability) could be violated**: The assumption that applicants who submit more applications have weakly higher origination probability is treated as benign ("do not appear very strong to us"), but it can plausibly fail. Distressed or credit-constrained applicants may submit many applications precisely because of high rejection risk, implying lower origination probability despite more submissions. A brief robustness discussion or empirical check would strengthen the paper.

- **Categorical variable constancy assumption**: The partitioning step assumes that variables like applicant race, sex, and age are constant across applications from the same individual. In HMDA, these self-reported fields can vary across applications due to data entry or co-applicant inclusion, potentially causing false negatives (true cross-applicants assigned to different partitions). The paper does not assess how often this occurs.

### Trivial
None.

---

## Nice-to-Haves

- A brief analysis of how many true cross-applicants submit 3+ applications (even in simulation) would allow readers to assess the practical cost of restricting to size-2 clusters.
- An illustration comparing precision-recall bounds for two structurally different linkage algorithms (not just different ε) would better demonstrate the method-agnostic scope.
- An explicit worked example connecting the bounds to a concrete non-mortgage application (e.g., insurance or job offers) would strengthen the generalization claim.

---

## Novel Insights

The core novel insight is that a structural cardinality constraint—that one individual can have at most one positive outcome across all their records—converts an otherwise unobservable quantity (the false positive rate) into an observable one. Specifically, multiple positive outcomes in the same predicted cluster are certain indicators of false positives (since true positives can have at most one), so the empirical rate of "multiple originations per cluster" directly bounds the false positive rate from above under mild independence and monotonicity assumptions. This turns a privacy-constrained label-free evaluation problem into a straightforward moment comparison, and the observation that the same inverse-tree structure needed for clustering can be reused across ε values without recomputation is an efficient computational dividend.

---

## Suggestions

- Quantify the fraction of cross-applicants with 3+ applications in the simulation (where ground truth is available) to empirically bound the recall loss from restricting to pairs.
- State explicitly in the main text that Corollary 1 provides only a relative recall ordering (not an absolute bound) since P_tot is unknown, and reframe the abstract's "lower bounds on relative recall" accordingly.
- Provide a sensitivity analysis for Assumption 2 (e.g., what happens to the bound if origination probability is non-monotone, or if a small fraction of applicants violates the assumption).
- Consider relaxing the size-2 restriction for at least one specification and report how the bounds behave for clusters of size 3.

---

## Score and Decision

The paper makes a genuine, well-executed methodological contribution to unsupervised record linkage evaluation. The central theoretical result is clean, practically impactful, and well-validated in simulation. The real-data application is large-scale and demonstrates the method's feasibility. The main weaknesses—restriction to size-2 clusters without recall cost quantification, and the non-comparability to alternative algorithms—are real but not fatal. The work is relevant to the ML community's growing interest in privacy-preserving and label-efficient methods.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Accept</decision>