Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

## Summary

This paper investigates why selective mixup (applying mixup to non-random pairs, e.g., only across classes or domains) improves OOD generalization. The central finding is that much of the observed improvement comes not from the mixing operation itself, but from an overlooked side effect: selective pairing implicitly resamples the training distribution toward uniformity ("regression toward the mean"), which happens to reduce distribution mismatch on common benchmarks. The paper provides a theoretical result (Theorem 1), introduces a clean ablation called *selective sampling* that isolates the resampling effect from mixing, and demonstrates across five datasets that selective sampling often matches or exceeds selective mixup. On datasets where mixing genuinely adds value (Yearbook), the paper shows the two effects are complementary.

## Strengths

1. **Clean ablation isolating resampling from mixing.** The *selective sampling* ablation — pairing examples using the same criteria as selective mixup but without mixing them, then keeping batch size constant by random dropping — is a methodological contribution in its own right. The paper shows that on Waterbirds, CivilComments, arXiv, and MIMIC-Readmission, selective sampling matches or exceeds selective mixup, directly demonstrating that the selection process (not mixing) drives most of the gain.

2. **Theoretical proof of implicit resampling.** Theorem 1 proves that the "different class" criterion increases the entropy of the training class distribution toward uniformity. The extension to "different domain" and covariate effects is appropriately heuristic, giving a principled explanation for the observed behavior.

3. **Empirical identification of "regression toward the mean" in benchmarks.** The paper shows that for all five studied datasets, the test distribution is systematically closer to uniform than the training distribution (Figure 5). This accidental property explains *why* the implicit resampling from selective mixup is beneficial, and the paper is transparent that this reliance on a dataset artifact constitutes a risk of overfitting to benchmarks.

4. **Correlation evidence linking resampling to performance.** The paper plots training/test distribution divergence against accuracy across selection criteria (Figures for Yearbook and arXiv), showing strong correlations that support the causal mechanism. The "cheating" baseline on arXiv (resampling to the test distribution) provides a particularly strong sanity check that the mechanism is label-shift correction.

5. **Novel combinations demonstrating complementarity.** On Yearbook and MIMIC-Readmission, combining simple resampling with within-class or vanilla mixup outperforms all existing selective mixup variants. This provides practical value beyond the critical analysis and validates the paper's decomposition of effects.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Abstract slightly oversells the universality of the finding.** The abstract states that resampling "explains much of the improvements in prior work." This is true on 4 of 5 datasets, but on Yearbook the best variant ("same class") has *no* resampling effect and yet significantly outperforms ERM — a case the paper itself acknowledges (lines 356-358: "it indicates a genuine benefit from mixup restricted to pairs of the same class"). The paper handles this transparently in the body (showing resampling *also* contributes on Yearbook via correlation evidence), but the abstract and introduction could more explicitly signal that on some datasets the mixing operation itself is the primary driver. This is a framing issue, not a factual error — "much of" is a hedge the paper earns — but tightening the framing would prevent misreading.

2. **The selective sampling ablation, while clever, has a subtle gap.** Selective sampling appends both elements of each pair in the mini-batch and then randomly drops half to keep batch size constant. The paper claims (line 307) "any difference between selective sampling and ERM is attributable only to resampling effects," which is correct. However, comparing selective sampling to selective mixup to attribute the *difference* to mixing assumes the two methods induce identical gradient distributions modulo the mixing operation. In selective sampling, the model sees two unmixed one-hot labels per pair (before dropping); in selective mixup, it sees one interpolated label. Mini-batch composition and gradient variance potentially differ in ways not controlled for. The paper's empirical results are strongly suggestive (the ranking of criteria is similar with or without mixing across multiple datasets), so this doesn't undermine the conclusion, but an analytical description of the induced sampling distribution — or importance-weighting to match distributions exactly — would tighten the logic.

3. **Correlation evidence is treated as confirmatory rather than suggestive.** The paper says the correlation between divergence reduction and accuracy "confirms the contribution of resampling" (line 379). While the paper has stronger causal evidence (the selective sampling ablation), the correlation plots serve as supporting diagnostics, not proof. The causal claim would be strengthened by explicit importance-weighting baselines on more datasets (the arXiv "cheating" point is excellent — extending this approach to other datasets would make the case definitive). As it stands, the language slightly overstates what the correlation alone establishes.

### Trivial
- The Yearbook analysis shows that the best selective mixup variant ("same class") has no resampling effect, yet improves over ERM. This is handled honestly in the paper, but it means the paper's central narrative (resampling explains improvements) has a clear exception that requires the reader to synthesize the body text. The paper would benefit from stating this caveat more prominently in the abstract.

## Nice-to-Haves
- **Importance-weighted ERM baselines.** The paper cites resampling/reweighting methods but does not include a baseline that reweights by the inverse of class frequencies (without test distribution knowledge). Adding this would directly test whether selective mixup's resampling effect is equivalent to standard importance weighting, rather than just reminiscent of it.
- **Controlled synthetic experiment.** A simple two-class dataset with controllable label shift (where the test distribution is sometimes more uniform and sometimes less uniform than training) would directly test the "regression toward the mean" explanation and verify the predicted failure case the paper acknowledges it cannot test (lines 584-586).
- **Exact characterization of induced resampling distributions for compound criteria.** For criteria combining class and domain (e.g., "same class / different domain"), deriving the exact resampling weights would make the theoretical connection to resampling fully rigorous.

## Removed Points
- The reviewer's suggestion about adding "Discuss the role of the mixing coefficient α" — this is a non-issue: the paper's resampling analysis depends only on pair selection, not α, and the paper already implicitly handles this. The reviewer acknowledges this but suggests noting it explicitly; this is a trivial presentation preference.
- The reviewer's characterization that the selective sampling ablation's limitations "deserve more discussion" as a "critical issue" — the gap described (gradient variance differences between mixed and unmixed examples) is inherent to any ablation study comparing different training objectives and does not threaten the paper's conclusions. Moved from "Critical Issue" to minor weakness (point 2 above).
- The reviewer's framing that correlation evidence is "treated as causal without sufficient caution" — the paper uses the selective sampling ablation as its primary causal evidence, with correlation as supporting diagnostics. The word "confirms" (line 379) is slightly strong but not misleading given the totality of evidence. Moved from a separate "critical issue" to a minor point folded into weakness 3.

## Novel Insights
None beyond the paper's own contributions. The paper's key insight — that selective mixup's gains on distribution-shift benchmarks are substantially attributable to implicit resampling, an accidental side effect of the selection process — is itself novel and well-supported. The reviews do not surface additional perspectives that extend beyond what the paper already provides.

## Suggestions
1. **Temper the abstract's framing** to explicitly mention that on some datasets (like Yearbook) the mixing operation itself drives improvement even when resampling is absent, while on others resampling dominates. This would make the paper's nuanced message clearer from the outset.
2. **Add an importance-weighted ERM baseline** (reweighting by inverse class/domain frequencies without test knowledge) as a direct comparison point for the implicit resampling from selective criteria. This is already implied by the paper's logic and would make the equivalence claims stronger.
3. **Add a synthetic experiment** with controllable label shift to demonstrate both the predicted benefit and the predicted failure case of the "regression toward the mean" mechanism, directly addressing the acknowledged limitation (lines 584-586).

## Score and Decision

This paper makes a genuine and valuable contribution by uncovering an overlooked mechanism in a widely-used family of methods. The theoretical observation is simple but important, the selective sampling ablation is a clean methodological contribution, and the empirical evidence is broad (5 datasets across vision, NLP, and tabular modalities). The paper is transparent about its limitations and does not overclaim. The weaknesses are minor framing and presentation issues, none of which threaten the core claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>