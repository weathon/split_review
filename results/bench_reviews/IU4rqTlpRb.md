## Summary

This paper argues that syntactic similarity (surface-form overlap between queries and answers), rather than topical relevance, is the primary driver of benign relearning in machine unlearning. The authors first reassess the BLUR benchmark, showing that equalizing step budgets largely erases the apparent advantage of topically relevant relearn sets. They then conduct a controlled experiment on TOFU comparing topically relevant vs. syntactically similar relearn sets, finding that syntactically similar data—even without topical overlap—consistently triggers stronger recovery. They provide mechanistic analysis through representation/gradient similarity and a template-vs-keyword loss ratio, and propose *syntactic diversification* (paraphrasing the forget set into heterogeneous surface forms) as a practical mitigation that suppresses relearning and improves model utility.

## Strengths

- **Methodological correction of BLUR (Section 4):** The paper identifies genuine confounds in BLUR's evaluation—unequal step budgets from different dataset sizes and fixed-epoch reporting that can miss recovery peaks. Standardizing the step budget and reporting maximum ROUGE-L across the trajectory is a fairer comparison, and the result that topical relevance advantages diminish under this protocol is a valuable finding that challenges the prevailing narrative.

- **Novel template-vs-keyword loss ratio diagnostic (Section 6):** The decomposition of answer tokens into template and keyword categories, and the loss ratio metric that tracks how unevenly unlearning suppresses structure versus content, is a genuinely useful diagnostic tool. Figure 6 convincingly shows that unlearning disproportionately drives up template loss while keyword loss remains comparatively low, and Figure 9 shows diversification brings the ratio back toward 1. This provides a clear mechanistic explanation for why syntactic fine-tuning reactivates forgotten content.

- **Syntactic diversification as a practical mitigation (Section 7):** The proposed strategy—paraphrasing forget-set queries via GPT-4o to break structural homogeneity—is simple, intuitive, and effective on TOFU. Figure 8 shows dramatic suppression of relearning under diversification, and Table 2 shows consistent utility improvements across Real Authors, World Facts, and Retain set metrics.

- **Multi-method validation:** The core findings are demonstrated across three qualitatively different unlearning methods (GA, NPO, SCRUB), and the BLUR reassessment covers four method variants (GA, GA+KL, NPO, NPO+KL), strengthening the claim that the observed effects are not method-specific artifacts.

## Weaknesses

### Fatal
None.

### Major

- **Confounded comparison between relearn sets in the core TOFU experiment (Section 5):** The two relearn sets differ on two dimensions simultaneously. D_relearn^topic uses non-name questions about the same target authors (different task, same entities), while D_relearn^syntactic uses name-format questions about different authors (same task, different entities). Higher recovery from the syntactically similar set could therefore be driven by task-type overlap—fine-tuning the model to answer any "what is the full name of..." query may reactivate the unlearned name-retrieval mapping—rather than by syntactic similarity per se. The design does not isolate surface structure from task type, so the central claim that *syntactic similarity* is the primary driver is not cleanly tested. The mechanistic analyses in Section 6 (representation/gradient similarity, loss ratio) provide supporting evidence but remain correlational and do not resolve this confound.

- **All controlled experiments and the diversification evaluation are confined to TOFU:** TOFU's QA pairs are generated from a rigid template with a single fixed surface form for each query type. This setting makes template-level imitation trivially easy and may exaggerate the role of structural overlap. The BLUR reanalysis (Section 5.4) provides correlational evidence across WMDP, WHP, and RWKU, but no controlled experiment isolating syntactic similarity is performed on any non-TOFU benchmark, and diversification is never tested outside TOFU. The paper's conclusions about generality therefore rest heavily on a single highly templated synthetic benchmark.

### Minor

- **"Syntactic similarity" operationalized via Levenshtein distance captures surface-form edit distance rather than linguistic syntax:** The normalized Levenshtein distance measures character-level string similarity, which can be driven by shared filler tokens, template length, and character overlap rather than grammatical structure. The term "syntactic similarity" is misleading—"surface-form similarity" or "template similarity" would be more precise. This terminological issue does not invalidate the empirical findings but weakens the paper's framing.

- **Maximum ROUGE-L over the training trajectory may overstate recovery for lower-relevance tiers:** Reporting the maximum value observed across all steps (Section 4) can favor conditions with noisier trajectories. While this is a reasonable choice for a conservative assessment (finding the worst-case recovery), it merits acknowledgment as a potential source of overestimation for conditions where recovery is less stable.

- **Diversification robustness tested only against the syntactically similar relearn set:** Section 7 demonstrates that diversification suppresses relearning when the relearn set is D_relearn^syntactic, but does not test whether it also helps against topically relevant or other types of relearn data. This limits the claim that diversification mitigates benign relearning in general.

- **No statistical significance or variance reported:** Table 2 reports utility improvements without confidence intervals, error bars, or significance tests, making it unclear whether the gains are reliable or within noise.

### Trivial

- The Levenshtein-based similarity of D_low (Lorem Ipsum) to D_target in WHP (0.1818) is reported as comparable to D_hi (0.1894), but the mechanism by which Latin filler achieves this similarity deserves more discussion, as it likely reflects length and character-distribution artifacts rather than genuine structural overlap.

## Nice-to-Haves

- A controlled experiment that varies syntactic similarity while holding task type constant (e.g., rephrased name-format questions about the same target authors at varying edit distances) would cleanly isolate the effect of surface form and strengthen the central claim.
- Evaluation of syntactic diversification on at least one non-TOFU benchmark (e.g., WHP or WMDP) would substantially bolster the generality argument.
- Testing diversification against topically relevant relearn data would complete the robustness picture.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point 2 (Post-hoc, non-causal reanalysis of BLUR):** The critic describes the BLUR revisitation in Section 5.4 as "post-hoc, non-causal." While the reanalysis is indeed correlational, the paper does not claim it is causal in isolation; it is presented as one piece of a multi-pronged argument alongside the controlled TOFU experiment and mechanistic analyses. The criticism that "any fine-tuning may undo shallow unlearning regardless of syntactic similarity" is a reasonable alternative explanation, but the paper's multiple converging analyses make the point too strong to keep as a standalone major weakness. Moved to the Minor section in a weakened form.

- **Harsh Critic claim that "the advantage of topically relevant datasets largely disappears" is inconsistent with Figure 2:** The paper's claim is supported by the overall pattern—the gap between D_hi, D_mid, and D_low is substantially smaller than BLUR originally reported, and in WHP they are nearly identical. The claim is somewhat overstated (D_hi remains best in WMDP) but not factually wrong. Removed as a standalone criticism.

- **Strength Finder claim about "validated across several benchmarks (TOFU, WMDP, WHP, RWKU)":** The controlled experiment (the paper's core contribution) is only on TOFU. The BLUR analysis covers multiple benchmarks but is a reanalysis, not a controlled experiment isolating syntactic similarity. This overstates the breadth of validation. Removed as a strength.

- **Harsh Critic formatting/style nitpicks:** Removed per instructions.

- **Harsh Critic references to missing appendix content:** The parser strips appendix sections. Removed per instructions.

- **Strength Finder generic strengths** (e.g., "findings are validated across multiple methods" — already captured more precisely above): Removed as redundant.

## Novel Insights

The most genuinely novel observation is the *template-vs-keyword loss ratio* analysis. Prior work on unlearning robustness has largely focused on input-level metrics (e.g., topical relevance of relearn data) or output-level metrics (e.g., ROUGE-L recovery). The loss-ratio diagnostic reveals an intermediate mechanistic layer: unlearning algorithms disproportionately suppress the templated surface patterns shared across forget-set queries and answers, while leaving the content-bearing keywords comparatively intact. This explains *why* syntactically similar fine-tuning can so easily reactivate forgotten content—it restores the suppressed templates, which then carry the keywords along. This diagnostic is simple to compute, requires no architectural modifications, and generalizes across unlearning methods, making it a practical addition to the unlearning evaluation toolkit.

## Suggestions

- The paper should explicitly acknowledge the task-type confound in Section 5.2 and discuss why the converging evidence from Sections 5.4 and 6 still supports the syntactic-similarity account despite this limitation. Even a paragraph of honest discussion would significantly strengthen the paper's credibility.
- A follow-up experiment with a third relearn set—name-format questions about the same target authors but with rephrased surface forms (controlling task type while reducing syntactic similarity)—would be highly informative. If recovery drops, it directly supports the syntactic account.
- The term "syntactic similarity" should be replaced with "surface-form similarity" or "template similarity" throughout, since Levenshtein distance captures character-level edit distance rather than grammatical syntax.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `7cEMkTu7Lf.md` — "Unlearning Isn't Deletion" | 4.00 | Both identify problems in unlearning evaluation; the current paper goes further with a mitigation strategy and mechanistic analysis. Stronger. |
| `EyXBv291ST.md` — "Effective Unlearning in LLMs Relies on the Right Data Retention Strategy" | 3.50 | Both are data-centric; current paper has a more novel core insight and actionable mitigation. Notably stronger. |
| `odMc2ZRGcw.md` — "BLUR: A Benchmark for LLM Unlearning Robust to Forget-Retain Overlap" | 2.50 | Benchmark paper with limited novelty. Current paper substantially stronger. |
| `lk3j87oquF.md` — "LUSB: Formalizing and Benchmarking Unlearning Attacks" | 4.00 | Broad benchmark with mixed reviews; current paper is more focused and has a clearer narrative. Stronger. |
| `rzi77zNngG.md` — "Leak@k: Unlearning Does Not Make LLMs Forget Under Probabilistic Decoding" | 4.00 | Clean single contribution (metric); current paper has broader scope with a mitigation but the confound weakens the core claim. Comparable, slightly stronger due to actionable mitigation. |
| `DXqiaXrNLu.md` — "Old Memories Die Hard" | 4.50 | Identifies a problem AND proposes mitigation with broad empirical coverage; current paper has cleaner narrative but less empirical breadth. Comparable quality. |
| `6zcXThQIoR.md` — "Leverage Unlearning to Sanitize LLMs" | 1.33 | Much weaker; current paper far stronger. |
| `7bZuhygFB1.md` — "Understanding the Dilemma of Unlearning for LLMs" | 3.00 | Interpretability-focused; current paper has more actionable contributions. Stronger. |
| `WNUDOLYlbh.md` — "Learning to Unlearn" | 3.00 | Method-focused; current paper has broader scope and stronger empirical grounding. Stronger. |

**Calibration:** The paper contributes a genuine diagnostic insight (loss ratio), a practical mitigation (diversification), and a useful methodological correction (BLUR reassessment). These place it above the typical ~4.0 reject-level papers in this space. However, the confounded core experiment prevents the central claim from being definitively established, and the TOFU-only controlled evaluation limits confidence in generality. These issues keep the paper below stronger contributions that cleanly isolate their claimed mechanism. A score of 5.0 reflects a paper with real contributions that would benefit from addressing the confound and extending beyond TOFU.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>