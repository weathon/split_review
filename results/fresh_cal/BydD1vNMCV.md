## Summary

The paper proposes using a stochastic neural network (StoNet) — formulated as a composition of linear/logistic regressions with injected noise at each layer — as a bridge between classical statistical models and deep neural networks. Leveraging an asymptotic equivalence result (Lemma 1, from prior work) between StoNet and DNN, the paper derives consistency rates for Lasso-penalized StoNets (Theorem 1), extends these to Lasso-penalized DNNs (Corollary 1), and develops a recursive uncertainty quantification procedure via Eve's law. A post-StoNet procedure is proposed for uncertainty quantification of large pre-trained DNNs. Experiments on synthetic data, CoverType, CIFAR-10, and several UCI regression datasets provide initial validation.

## Strengths

- **First consistency theory for Lasso-penalized DNNs (Corollary 1):** The paper provides the first theoretical backing for the commonly practiced Lasso-penalized DNN training (Scardapane et al. 2017, Lemhadri et al. 2019) by establishing consistency in both parameter estimation and structure selection. This is a genuine contribution that fills a notable gap between practice and theory.

- **Explicit convergence rates for sparse StoNets (Theorem 1):** Theorem 1 gives concrete rates $r_n$ involving layer widths, sparsity levels, noise variances, and sample size, for both linear and logistic output layers. These rates adapt the Lasso convergence theory from linear models to a hierarchical latent-variable structure.

- **Recursive UQ via Eve's law (Section 4):** The layer-by-layer variance propagation formula for constructing prediction intervals from the StoNet is principled and exploits the model's Markov decomposition in a clean way.

- **Empirical evidence for post-StoNet calibration improvement:** On CIFAR-10 (Table 2), the post-StoNet procedure consistently lowers ECE compared to temperature scaling and matrix scaling across three architectures (DenseNet40, ResNet110, WideResNet-28-10). On UCI regression datasets (Table 3), it produces shorter prediction intervals at comparable coverage to split conformal prediction.

- **Comprehensive framework connecting two research communities:** The paper doesn't just prove one result but lays out a systematic approach (asymptotic equivalence → sparse learning theory → UQ) that could enable further transfer of statistical methods to deep learning.

## Weaknesses

### Fatal
None.

### Major

1. **Tension between the asymptotic theory and practical noise-variance settings:** Theorem 1's rates contain terms $\sigma_{l,n}^2 / \sigma_{l-1,n}^4$ that can blow up if later-layer variances shrink faster than earlier-layer variances. Yet Remark 1 and the experimental setup recommend setting all $\sigma_{l,n}^2$ to "very small values" to approximate the DNN. The paper does not discuss how to reconcile these — i.e., what scaling of $\sigma_{l,n}^2$ with $n$ simultaneously satisfies (a) the asymptotic equivalence in Lemma 1 (which requires the StoNet to approximate the DNN), (b) the rate conditions in Theorem 1, and (c) the practical heuristic of small uniform $\sigma^2$. This gaps the connection between the theory and the experimental protocol.

2. **Post-StoNet compared against conformal prediction without coverage guarantees:** The post-StoNet procedure (Section 6.2) is compared to split conformal prediction (Table 3), which provides distribution-free finite-sample coverage validity. The post-StoNet provides no such guarantee — neither finite-sample nor asymptotic. The paper claims superiority based on shorter interval lengths at similar coverage rates, but this comparison is not on equal footing: shorter intervals from a method without validity guarantees do not constitute evidence of superiority over a method with proven validity. The paper either needs to provide asymptotic justification for the post-StoNet intervals (e.g., consistency of the variance estimator from Eve's law under the asymptotic equivalence) or substantially temper the comparative claims.

3. **Variable selection results are purely visual, lacking quantitative metrics:** The synthetic example (Section 5) evaluates variable selection only through regularization path plots (Figure 2). No quantitative metrics (true positive rate, false positive rate, selection frequency across runs, etc.) are reported. For a paper whose core theoretical claim is consistency in structure selection, this is a significant empirical gap — the reader cannot assess whether the theory translates to reliable identification in practice. Similarly, the CoverType feature identification (Section 6.1) shows a regularization path but includes no comparison to any feature importance baseline (e.g., permutation importance, SHAP) to validate the quality of the identified features.

### Minor

4. **Coverage rates reported without interval lengths in Table 1:** Table 1 reports coverage rates for the synthetic experiment across different $\sigma^2$ settings, but does not report interval lengths. Without interval lengths, it is impossible to assess calibration properly (wide intervals trivially achieve nominal coverage). The sensitivity to $\sigma^2$ — e.g., the half-$\sigma^2$ setting producing coverage as low as ~83% for the two-hidden-layer model — is noted but not discussed or explained.

5. **Post-StoNet description lacks reproducibility-critical details:** Section 6.2 states "learn a simple sparse StoNet (e.g. with one hidden layer only) using the transformed data" but does not specify how the sparse StoNet is trained (what penalty? what hyperparameter selection procedure? how are $\sigma^2$ values chosen?). These details are necessary for reproducibility of the paper's main practical contribution.

6. **Synthetic experiment limited in scope:** The synthetic data uses only 20 variables and 500 training samples, with a specific correlation structure (0.5 mutual correlation). While this serves as an illustration, it does not constitute the kind of thorough simulation study that would convincingly validate the asymptotic theory (e.g., varying $n$, $p$, sparsity levels, correlation strengths, and noise variances to verify the rates in Theorem 1).

### Trivial
None.

## Nice-to-Haves
- Adding Bayesian approximation baselines (MC dropout, deep ensembles) to the UQ comparison would help contextualize the post-StoNet's performance against the broader literature, though the paper's current comparisons (conformal, temperature scaling, matrix scaling) are reasonable for its stated scope.
- A small simulation directly validating the asymptotic equivalence (Lemma 1) — e.g., showing convergence of StoNet parameter estimates to DNN truth as $n$ increases with properly scaled $\sigma^2$ — would strengthen confidence in the bridging claim.

## Removed Points

- **Criticism about the paper lacking appendix / inability to evaluate without appendix:** The parser strips appendix content from all papers. The assumptions (A1–A6) and detailed training settings (Section G) referenced in the main text exist in the original submission; this is a parsing artifact, not an author omission.
- **Strength Finder's generic descriptors** (e.g., "theoretical foundation via asymptotic equivalence" framed as a strength): These are descriptive rather than evaluative. The concrete strengths above already capture the substantive contributions.
- **Request to add more related works:** Per instructions, missing related works are not flagged.
- **References to "not yet released" or reproducibility concerns about cited entities:** No such references appear in the reviews.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface standard concerns about verification of theoretical conditions, fairness of empirical comparisons, and experimental thoroughness — they do not identify a fundamentally novel perspective on the work's contribution.

## Suggestions

1. **Address the $\sigma^2$ scaling tension explicitly:** Provide a clear statement of how the noise variances $\sigma_{l,n}^2$ should scale with $n$ (and possibly with layer index $l$) such that (a) Lemma 1's conditions are satisfied, (b) the rates in Theorem 1 are well-behaved, and (c) the practical recommendation of "small $\sigma^2$" is recovered as a special case. If no single scaling regime satisfies all three, state the trade-off and which regime each result belongs to.

2. **Either prove coverage for the post-StoNet or reframe the comparison:** If the post-StoNet intervals can be shown to be asymptotically valid (e.g., via consistency of the Eve's-law variance estimator under Lemma 1), include this result. Otherwise, reframe the comparison with conformal prediction as an empirical illustration rather than a head-to-head claim of superiority, and acknowledge the lack of theoretical coverage guarantees.

3. **Add quantitative variable selection metrics** to the synthetic experiment (TPR, FPR, selection stability across repeated runs) and at least one feature importance baseline to the CoverType experiment. This is essential to substantiate the structure-selection consistency claim empirically.

4. **Report interval lengths alongside coverage rates in Table 1** so that calibration can be properly assessed, and discuss the $\sigma^2$ sensitivity observed in the results.

## Score and Decision

**Calibration anchors** (all from `/home/wg25r/split_review/datasets/deepreview_13k_calibration`):

| Path | Avg Human Score | Comparison |
|------|----------------|------------|
| `4xWQS2z77v.md` (Exploring Loss Landscape via Convex Duality) | 8.00 | Substantially stronger: cleaner theoretical contributions with complete proofs, unanimous reviewer support. StoNet paper is much less polished. |
| `eQggPqESBr.md` (Simplicity Bias) | 5.50 | Similar tier: both have genuine theoretical contributions constrained by scope and gap to practice. StoNet's theory is broader in intended reach but less self-contained. |
| `vcX0k4rGTt.md` (Approx. Full Conformal Prediction) | 5.75 | Similar tier: both have mixed reviews on validity of comparisons. StoNet has more theoretical ambition but weaker empirical support. |
| `MY8SBpUece.md` (Non-Linear Feature Learning) | 5.50 | Comparable: theory paper with clean results but strong assumptions. StoNet is less clean but tackles a different problem of comparable difficulty. |
| `381QSrWdF2.md` (Law of Balance of SGD) | 5.50 | Comparable quality: both have genuine contributions with some gap between theoretical claims and practical implications. |
| `vpo2K9Xivv.md` (Black Boxes and Looking Glasses) | 3.80 | Weaker paper: overly narrow architecture, overclaimed results, notation issues. StoNet has more substantive theory and broader applicability. |
| `n2RIkaf1S4.md` (Block Coordinate Descent) | 4.00 | Slightly weaker: convergence results for a niche algorithm. StoNet targets a more central problem (sparse DNN consistency). |

The paper makes a genuine contribution — first consistency theory for Lasso-penalized DNNs — and presents a coherent framework. However, the theory relies on a critical lemma from prior work without verification of its conditions in the paper's own regimes, the post-StoNet comparisons are made against methods with guarantees the proposed procedure lacks, and the experimental validation is too thin to fully substantiate the claims. These issues are addressable but significant in their current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>