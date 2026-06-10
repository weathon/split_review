Now I have a thorough understanding of the paper and both reviews. Let me synthesize the final review.

## Summary

This paper investigates the mechanism of robust overfitting in adversarial training. The key contributions are: (1) a factor ablation experiment that separates normal data from adversarial perturbations to identify normal data as the inducing factor of robust overfitting; (2) a qualitative mechanistic explanation centered on "non-effective features" — robust features on the training set that lack generalization to the test set — and a robustness gap between train/test sets that amplifies their proliferation; and (3) two practical methods (OROAT_AS via attack strength and OROAT_DA via data augmentation) derived from this analysis that mitigate robust overfitting. Experiments on CIFAR-10/100 with multiple architectures and AT variants show consistent improvements.

## Strengths

- **Controlled factor-ablation design (Section 3.1, lines 86–88):** The experiment cleanly separates normal data and adversarial perturbations as distinct factors. The "data & perturbation" group (removes both) substantially reduces robust overfitting while the "perturbation" group (removes only perturbations, keeps normal data) still overfits severely. Because all groups are identical until epoch 100, this isolation of normal data as the causal inducing factor is the paper's strongest and most novel finding — it goes beyond prior ablation studies that treated adversarial data as monolithic.

- **Dose-response relationship between attack strength and overfitting degree (Figure 1(c), lines 115–117):** The paper demonstrates a graded, monotonic relationship: applying stronger perturbation budgets to small-loss adversarial data progressively reduces robust overfitting, with essentially no overfitting at 16/255. This dose-response pattern provides specific correlational evidence consistent with the proposed mechanism and is more informative than a simple binary "works/doesn't work" finding.

- **Unified explanation of contradictory prior observations (Section 2.2, lines 69–70):** The paper identifies concrete contradictions in the literature (more data sometimes harming robustness, opposing reweighting strategies both working, data augmentation succeeding in some works but failing in others) and shows how its framework explains why these seemingly inconsistent results are compatible. This synthesis adds value beyond the individual experiments.

- **Ablation reveals a trade-off, not a purely monotonic benefit (Section 4.2, lines 146–147):** The ablation shows that as the proposed components become more aggressive, robust overfitting decreases but adversarial robustness first increases then decreases. This nuanced finding — acknowledging that suppressing non-effective features can also remove useful robust features — makes the analysis more credible than a claim of unqualified improvement.

## Weaknesses

### Fatal
None.

### Major

- **The mechanistic explanation is a qualitative narrative with unmeasured constructs, not a demonstrated causal chain.** The paper's central contribution (per its own framing) is a detailed causal mechanism: a robustness gap → differing adversarial perturbations on robust features → amplified distribution differences → generation of "non-effective features" → vicious cycle → robust overfitting. However, the key intermediate variables — "non-effective features" and the amplification cycle — are never directly measured or causally tested. No metric for non-effective features is defined, let alone tracked during training to test whether their accumulation precedes robust overfitting. Additionally, the construct is defined in a nearly circular way: "non-effective features" are robust features on the training set that "lack generalization" (line 100), and the paper then explains generalization failure (robust overfitting) as caused by learning these features. The evidence offered consists of experimental outcomes that are *consistent with* the narrative (removing small-loss data helps, stronger attacks reduce overfitting) but does not uniquely support it — alternative mechanisms (e.g., simple regularization, curriculum effects, standard overfitting to clean data) could produce the same observations. The paper presents the mechanism with language like "comprehensive understanding" and "validating our analysis" (contributions, lines 20–22) that overstates the strength of the evidence. The factor ablation finding (normal data as inducing factor) is well-supported; the mechanistic *why* is a plausible hypothesis that requires substantially stronger evidence.

- **The factor ablation inference has an interpretive confound that the paper does not address.** The "perturbation" group removes adversarial perturbations from small-loss adversarial data while keeping the original clean (unperturbed) data. This means the model now trains on a mixture of adversarial data (large-loss samples) and clean data (small-loss originals). The observed overfitting in this group could be, at least in part, a form of **standard overfitting to the clean examples** — the model memorizing unperturbed data it already classifies correctly — rather than specifically the hypothesized "non-effective features" mechanism driven by a robustness gap. The paper draws a clean causal inference about *what* the inducing factor is (normal data), and that inference is sound. But the inference about *why* normal data causes robust overfitting is confounded by this design choice, since the perturbation group's training distribution differs from standard AT in a way that introduces clean-data overfitting. The paper should acknowledge this ambiguity and discuss how to distinguish the two interpretations.

### Minor

- **Circularity in the definition of "non-effective features":** The paper defines non-effective features as "robust features in the training set that lack generalization" (line 100), then uses their proliferation to explain why generalization fails (robust overfitting). This is definitionally circular — a feature is identified by its failure to generalize, and that failure is then attributed to the feature itself. The concept is useful as a *description* of what happens during robust overfitting, but as an *explanation* it has limited explanatory power without an independent operationalization.

- **Loss threshold (1.5) used in factor ablation without sensitivity analysis.** The paper uses a fixed loss threshold to separate small-loss from large-loss adversarial data (line 86) but does not report how the factor ablation results depend on this choice. If the results change qualitatively with different thresholds, the inference narrows.

- **Standard deviations omitted from the main results tables** (line 130). The paper states they are "small" (<0.6% natural, <0.3% PGD-20, <0.2% AA) and reports averages over three trials, but omitting error bars prevents readers from assessing whether observed differences between methods are statistically meaningful for specific comparisons.

- **No discussion of alternative mechanisms** that could explain the same experimental observations. Given that the paper claims to have uncovered "the fundamental mechanism" (line 12), it should explicitly discuss whether and how the proposed account is distinguishable from simpler explanations (e.g., regularization, standard overfitting, curriculum learning dynamics).

### Trivial
None.

## Nice-to-Haves
- **Directly operationalize and measure "non-effective features"** — e.g., as the gap between training-set feature robustness and test-set feature robustness on matched subsets, tracked over training to test whether they accumulate *before* robust overfitting onset (causal evidence) or merely coincide with it.
- **Test the robustness-gap → differing-perturbations link** by comparing adversarial perturbations generated on training vs. test examples at fixed checkpoints, verifying whether they systematically differ in ways that correlate with the robustness gap.
- **Sensitivity analysis** for the loss threshold in factor ablation and for the data augmentation threshold in OROAT_DA.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"OROAT_DA method is underspecified / description cuts off"** — Removed because the parser strips appendix content; the original submission likely contains the full description (including Algorithm 1 and additional details) in sections unavailable in the parsed text.
- **"Tables are unreadable images / numerical results not accessible"** — Removed; this is a PDF parsing artifact, not a flaw in the original submission.
- **"Algorithm 1 not present in parsed text"** — Removed; appendix content stripped by parser.
- **Various formatting/typographical nitpicks** — Removed per hard rules about parser artifacts.
- **Criticism about "methods do not independently validate the mechanism"** — Demoted to Minor (see above) rather than removed; the core concern (circularity of consistency checks) has some validity but is standard for this type of paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension between the paper's strong wording ("comprehensive understanding," "fundamental mechanism") and the actual strength of evidence (a plausible qualitative narrative consistent with the data but not uniquely supported by it). This calibration issue — mechanistic narratives presented as established fact when they are well-motivated hypotheses — is a recurring pattern in deep learning papers and worth the authors' attention.

## Suggestions
1. **Calibrate the claims about the mechanism.** Present the factor ablation result (normal data induces robust overfitting) as the paper's strongest evidence, and frame the non-effective-features narrative explicitly as a *hypothesis* that is consistent with the data but requires direct measurement of its constructs for stronger validation. This would better align the paper's language with its evidence.
2. **Acknowledge the interpretive confound** in the factor ablation design (standard overfitting to clean data as an alternative explanation) and discuss how future work could distinguish between these accounts.
3. **Provide sensitivity analysis** for the loss threshold used in factor ablation and for key hyperparameters.
4. **Include error bars or confidence intervals** in the main results tables, even if small.
5. **Discuss alternative mechanisms** explicitly — what predictions would distinguish the non-effective-features account from simpler explanations?

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>