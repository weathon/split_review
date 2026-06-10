Now I have all the verification I need. Let me compose the final review.

## Summary

This paper proposes TUI (Test Uncertainty Indicator), a conformal prediction (CP) wrapper for continual test-time adaptation (CTTA). TUI has two components: (1) a CP-based uncertainty indicator that compensates for the coverage gap under domain shift by measuring joint distribution differences between source and current models, and (2) a weighting scheme that uses prediction set size to weight adaptation updates. Experiments on CIFAR10C/CIFAR100C/ImageNetC with five CTTA methods show coverage maintenance and improved downstream metrics.

## Strengths

- **Joint domain shift measurement using both source and current models (Eq. 4–5).** The paper identifies a genuine limitation of existing non-exchangeable CP methods for CTTA: NexCP assumes a pre-defined domain shift value (infeasible at test time), and QTC ignores model degradation from error accumulation. TUI's joint distribution approach — comparing JS divergence between calibration and test batches in the representation space of both the source and current models — is a well-motivated design that addresses both limitations simultaneously. This is a concrete technical contribution over the prior CP-for-CTTA literature.

- **Coverage maintenance demonstrated against other CP methods.** Table 4 and Figure 2 provide direct evidence that TUI maintains coverage closer to the desired (1−α) level across a sequence of domain shifts, while THR, NexCP, and QTC all exhibit larger coverage gaps. For α=0.2, TUI achieves 0.831 coverage vs. QTC's 0.748, NexCP's 0.481, and THR's 0.416. This directly supports the paper's central uncertainty-estimation claim.

- **Multi-metric evaluation beyond coverage alone.** The paper evaluates NLL, Brier Score, and ECE alongside coverage and inefficiency, giving a fuller picture of uncertainty quality than coverage-only reporting.

- **Storage-efficiency analysis vs. replay strategies.** Table 5 compares TUI against a source replay strategy using the same stored samples, showing that the CP-based approach yields better accuracy with the same data budget. This addresses the practical concern about maintaining a calibration set.

## Weaknesses

### Major

- **Missing original-method baselines in Tables 1–3.** The tables report two rows per CTTA method: "method + TUI (uncertainty estimation only)" and "method + TUI + CPAda (with adaptation guidance)." The original methods without TUI are absent. This means the reader cannot determine whether the TUI-guided adaptation improves upon the original method or merely recovers performance degradation introduced by adding TUI. The paper's claim that TUI "help[s] multiple existing CTTA methods…achieve better performance" (Contribution 3) is therefore unsubstantiated by the evidence presented — the comparison only shows that CPAda helps relative to the TUI-only variant. Adding one column or row per method showing the original error rate would directly address this.

- **Critical hyperparameter β is completely unspecified.** The quantile compensation formula (Eq. 9) is the paper's central mechanism: τ̂ = τ* − β·ρ. Yet β is described only as "a predefined factor" with no value, sign convention, search range, or sensitivity analysis reported anywhere in the paper. Since β determines both the magnitude *and direction* of the coverage compensation — the paper's core technical device — its omission makes the results effectively irreproducible. This must be specified and at minimum accompanied by a sensitivity analysis across a plausible range.

- **Sign ambiguity in the compensation formula (Eq. 9).** When domain shift ρ > 0, the model's confidence drops, raising non-conformity scores. To maintain coverage, τ̂ must *increase* (admit more labels). The formula τ̂ = τ* − β·ρ would decrease τ̂ if β > 0 — the opposite of what is needed. The paper's stated intent ("include some more uncertain classes to the prediction set to meet the coverage requirement") describes the correct behavior, but if β is taken as a conventional positive scalar, the sign is inverted. If β is intended to be negative (making τ̂ = τ* + |β|·ρ), this must be stated explicitly. The paper currently provides no resolution, leaving the core mechanism ambiguous. (Note: this is not necessarily a fatal error — a negative β would resolve it — but the ambiguity itself is a serious flaw that must be fixed.)

### Minor

- **No variance or statistical significance reported.** All tables present single-run numbers with no standard deviations, confidence intervals, or indication of multiple seeds. CTTA methods are stochastic (random restorations, data augmentation, batch ordering), and CP calibration split introduces additional randomness. Without variance estimates, the reliability of every quantitative claim is unclear.

- **Joint distribution construction (Eq. 4) lacks justification and ablation.** Applying softmax to a 2K-dimensional concatenation of two independently trained models' outputs normalizes across incompatible logit scales, yielding a vector whose statistical meaning is unclear. The paper provides no analysis comparing this to simpler alternatives (e.g., using only the source model, only the current model, or a feature-space distance like MMD). This design choice is central to the domain shift estimation but remains unvalidated.

- **Empty prediction set frequency not reported.** The paper acknowledges that prediction sets can be empty (which violates coverage) but provides no analysis of how often this occurs across methods, α settings, or domains.

- **Batch size for ρ estimation not specified.** The domain shift estimate ρ (Eq. 5) operates over a batch B. The paper does not state the batch size used or analyze its effect. In the strict online setting (batch size 1), Eq. 5 reduces to pairwise JS divergence between a single test sample and each calibration sample — the reliability of ρ in that regime is unclear.

### Trivial

- **Eq. 8 (non-conformity score definition) is garbled in the PDF extraction** (reads `s(π(x)) = 1 − ŷ` where ŷ is undefined). The surrounding text describes the intended definition but the equation itself is corrupted.

## Nice-to-Haves

- Ablation of the weighting function γ (Eq. 11) against simpler alternatives (binary reliable/unreliable split, uniform weighting) would strengthen the adaptation design.
- Comparison with non-CP uncertainty methods (temperature scaling, MC Dropout) would contextualize the contribution, though the paper's CP framing makes this optional.
- Analysis of non-conformity score distributions across domains (standard CP diagnostics) would help readers understand where the coverage gap originates and how the compensation affects it.

## Removed Points

These points from the input reviews are excluded per the filtering rules:

- **"OCR garbling (lines 40–42)"** — Parser artifact; per instructions, formatting artifacts from PDF extraction are not author errors.
- **"Conflates multiple train-test scenarios"** in the related work — Unsubstantiated claim with no specific anchor in the paper.
- **"The characterization of NexCP as 'designed for training time' is imprecise"** — The paper states (line 65) that NexCP "is designed for training phase and highly depends on a pre-defined domain shift value." This is an accurate characterization of NexCP's limitation for test-time settings; the criticism reflects a knowledge disagreement, not a paper error.
- **Strength Finder's claim about "error-rate reduction across five CTTA methods"** — The Strength Finder presented improvement from "method+TUI" to "method+TUI+CPAda" as though it were improvement over the original methods (calling the first row "vanilla"). This is misleading; the tables do not contain original-method baselines.
- **Generic scope-creep criticisms** (e.g., "could the metric be measuring a proxy?") — Not anchored in a specific sentence or figure.
- **Criticism about no comparison to simpler uncertainty methods** (MC Dropout, temperature scaling, ensembling) — The paper explicitly scopes itself as a CP-based method; requesting these comparisons is outside the stated contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the compensation formula**: State explicitly: (a) whether β is positive or negative, (b) its numerical value(s), and (c) show sensitivity of coverage/error rate to β over a range (e.g., 0 to 1 or -1 to 0). If the sign is negative, explain the design rationale.

2. **Add original-method baselines to Tables 1–3**: Include the error rate of TENT, CoTTA, SATA, RMT, and C-CoTTA without any TUI component, so that the net effect of adding TUI+CPAda can be assessed.

3. **Report variance over at least 3 seeds** for all main tables.

4. **Ablate the joint distribution design** (Eq. 4): Compare against simpler alternatives (source model only, current model only, feature-space distance) to validate that the 2K-dimensional softmax concatenation is beneficial.

5. **Report empty-set frequency** and discuss its impact on coverage guarantees.

6. **Specify batch sizes** used in experiments and discuss the effect of batch size on the reliability of ρ.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>