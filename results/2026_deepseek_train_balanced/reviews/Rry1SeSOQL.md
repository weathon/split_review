Now I have enough information to write the final consolidated review. Let me compose it.

## Summary

MT-Ranker reformulates reference-free machine translation evaluation from a regression problem (predicting an absolute quality score) to a pairwise ranking problem (given a source sentence and two translations, predict which is better). The system uses a three-stage training pipeline — pretraining on XNLI (indirect NLI supervision), fine-tuning on human-vs-machine translation discrimination, and weakly supervised synthetic data generation — and achieves strong results across five benchmarks (DA20, MQM20–22, ACES). The core contributions are: (1) the first reference-free pairwise ranking formulation for MT evaluation, (2) SOTA correlation with human judgments on DA20 and ACES without using human-annotated quality scores, and (3) an honest analysis of failure modes (untranslated errors).

## Strengths

- **First to formulate reference-free MT evaluation as pairwise ranking.** Section 2 (lines 46–52) explicitly documents that all prior pairwise ranking approaches (Ye et al. 2007, Duh 2008, Guzman et al. 2014/2015) required reference translations. The empirical payoff is clear: on DA20 X-to-English, MT-Ranker-XXL achieves 22.0 average Kendall's Tau vs. 17.6 for OpenKIWI-XLMR (+4.4), and on English-to-X, 52.2 vs. 48.4 for T5Score-XL_sup (+3.8) — all without direct human quality annotations (Table 1).

- **State-of-the-art on ACES against both reference-free and reference-based systems.** Table 3 shows MT-Ranker-XXL achieves 18.46 ACES-Score, surpassing KG-BERTScore (17.49) which uses external knowledge graphs, and CometKiwi (16.95). Per-category breakdowns show specific edges: 0.97 on Omission (vs. 0.93 UniTE), 0.97 on Punctuation (vs. 0.73 UniTE), and 0.66 on Real World Knowledge (vs. 0.58 CometKiwi).

- **Three-stage training pipeline with verifiable contribution from each stage.** The ablation study (Figure 1) directly demonstrates that removing any stage degrades performance on DA20, with Stage III (synthetic data) causing the largest drop. This provides causal evidence for the pipeline's design rather than just claiming it works. The use of cross-lingual NLI as indirect supervision (Stage I) is a genuinely clever idea.

- **Honest quantification of limitations.** The paper openly reports negative Kendall's Tau on untranslated-vs-ref-word (−0.25 for XXL) and untranslated-vs-synonym (−0.30 for XXL) with a clear explanation of why these are hard for reference-free systems (Table 5, Section 4). The zero-shot generalization analysis (Table 4) honestly shows a meaningful gap on the "nonsense" phenomenon (δ = 0.219 even for XXL).

## Weaknesses

### Fatal
None.

### Major

- **MQM evaluation protocol is ambiguously specified, undermining confidence in those results.** The paper (lines 246–249) acknowledges that the Kendall's Tau implementation used for MQM differs from the "flattened" approach used in prior work, instead employing the "segment averaging approach" from Freitag et al. (2022). However, the paper never explicitly states whether the baseline numbers in Table 2 (COMET-QE, UniTE, CometKiwi) were **re-computed under this same protocol** or taken from published papers that used a different protocol. Since MT-Ranker's margins on MQM are modest (1.3, 0.4, and 2.8 points), even small discrepancies in evaluation protocol could alter the comparison. The paper must clarify this — ideally by stating that all systems were evaluated under the same protocol and reporting the re-computed numbers.

### Minor

- **Ablation study is limited to one benchmark and one model size.** Figure 1 only shows DA20 results for MT-Ranker-Large. Showing the effect of removing each training stage on MQM and ACES, and at different model sizes, would significantly strengthen the claim that each stage generalizes across evaluation scenarios.

- **No statistical significance or variance reported.** All tables show point estimates of Kendall's Tau without confidence intervals, standard errors, or significance tests. Given the modest margins on MQM21 (0.4 points), statistical significance is relevant for interpreting these results.

- **The "no human annotations" claim would benefit from more precise phrasing.** The paper states the system is trained "without any human annotations" and "without relying on human-annotated data." This is accurate in the narrow sense that no human-provided *quality scores* are used as training labels. However, Stage II training uses human-written reference translations as positive training examples, and Stage III uses BERTScore (a reference-based metric) as a teacher. The claim is defensible in the MT evaluation literature (where "annotations" standardly means quality-score labels), but "without any human-provided quality annotations" would be more precise and avoid misinterpretation.

- **No discussion of the O(N²) computational cost of pairwise evaluation.** For N translations, pairwise comparison requires O(N²) forward passes versus O(N) for scoring-based systems. This is a practical limitation for system-level evaluation with many systems that should be acknowledged.

- **System-level evaluation results not reported.** The paper motivates pairwise ranking by arguing it is "sufficient for the most important use case: comparing machine translation systems" but only reports segment-level Kendall's Tau. Reporting system-level Kendall's Tau or showing how pairwise predictions aggregate to system rankings would directly validate this central claim.

### Trivial
None.

## Nice-to-Haves

- The ablation study could be extended to MQM and ACES benchmarks, not just DA20.
- Reporting the size of synthetic data generated at each stage would improve reproducibility.
- Training hyperparameters (learning rate, batch size, epochs, compute budget) should be provided.
- The paper could explicitly discuss the O(N²) evaluation cost as a trade-off.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh Critic's claim about missing WMT21/22 Shared Task datasets (DA21/DA22).** REMOVED. The paper evaluates on MQM21 and MQM22, which are from the WMT21 and WMT22 Shared Metrics Tasks (noted in lines 183–184). The paper already covers five benchmarks; requesting additional DA datasets beyond this scope is not a substantive weakness.

2. **Harsh Critic's claim about "dated" baselines (OpenKIWI-XLMR submitted to WMT20).** REMOVED. This is a standard baseline for the DA20 benchmark — the benchmark itself is from WMT20, so WMT20-era baselines are appropriate. More recent baselines (CometKiwi, T5Score) are included on other benchmarks.

3. **Harsh Critic's claim about not justifying the exclusion of CometKiwi from DA20/ACES.** The paper does justify this: CometKiwi was trained on MQM data (line 252: "We only show results on MQM22 for CometKiwi since it uses MQM20 and MQM21 as training data"), so it cannot be fairly compared on those benchmarks as a "reference-free" system.

4. **Strength Finder's general/unsupported strengths.** None found — all cited strengths have specific evidence anchors.

## Novel Insights

The reviews surface an interesting tension: the paper's core innovation (pairwise ranking as an alternative to score-based regression) is both its biggest strength and the source of its most significant evaluation challenge. Because MT-Ranker does not produce scalar scores, it cannot use the standard Kendall's Tau implementations from prior work, forcing the authors to adopt a different protocol. This creates a meta-insight: a genuinely novel evaluation formulation may require novel evaluation protocols, and the community lacks standardized tools for comparing across these paradigms. The paper would be strengthened by directly engaging with this tension rather than simply adopting an alternative protocol.

## Suggestions

1. **Clarify the MQM evaluation protocol explicitly.** In the rebuttal/camera-ready, state: "All baseline numbers in Table 2 were re-computed by us using the segment averaging Kendall's Tau described in Freitag et al. (2022)." If this is already what was done, it needs to be stated clearly. If not, the re-computation should be done and reported.

2. **Extend ablation to at least one additional benchmark.** Showing the ablation on MQM20 or ACES would demonstrate that the three-stage pipeline's contribution generalizes beyond DA20.

3. **Add statistical significance or confidence intervals** for the main results, especially on MQM21 where the margin is only 0.4.

4. **Rephrase "without human annotations" to "without human-provided quality annotations"** or similar precision.

## Score and Decision

This is a solid paper with a clear, novel contribution: formulating reference-free MT evaluation as pairwise ranking, supported by a clever three-stage training pipeline and competitive empirical results across five benchmarks. The main concerns are addressable: the MQM evaluation protocol needs explicit clarification, and several minor improvements would strengthen the paper. The contribution is substantive enough for a top venue like ICLR.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>