## Summary

This paper introduces a formal framework of *inner* and *outer subgrammars* for probabilistic context-free grammars (PCFGs) and proves that the KL divergence of a language model decomposes recursively over this subgrammar structure (Theorems 4.3, 4.6). Empirically, it shows that small transformers trained on PCFGs learn all subgrammars in parallel (unlike the sequential pattern observed in child language acquisition), that pretraining on a subgrammar can improve final loss and change internal representations (measured via CKA), and that these models struggle with deep recursion even when they handle long flat sequences correctly.

## Strengths

- **Novel subgrammar framework (Definitions 3.3, 3.5).** The formal notions of inner and outer subgrammars provide a clean vocabulary for analyzing how the substructure of a CFG relates to learning dynamics. These definitions are conceptually useful and are the foundation for the paper's theoretical and empirical contributions.

- **Clean theoretical decomposition of KL loss over subgrammar structure (Theorems 4.3, 4.6).** The paper formally shows that the language-modeling loss (KL divergence) decomposes as a sum of "restricted" divergences over subgrammars, and incorporates expected recursion as a multiplicative factor. This is a mathematically sound connection between loss and grammatical substructure.

- **The parallel-learning observation is striking and clearly visualized.** Figure 1 shows that subgrammar-level KL divergences all decrease simultaneously during training — a non-obvious finding that directly contrasts with sequential acquisition patterns in child language. This observation is the paper's most interesting empirical result.

- **Clean depth-vs-length experiment (Figure 3).** The paper demonstrates that small transformers fail on deep recursive contexts but handle equally long flat contexts, with a shaded variance band and quantitative error values reported. This is a well-controlled, reproducible finding.

## Weaknesses

### Major

- **Figure 1 shows visual trends but the claimed additive decomposition is not quantitatively validated.** The paper states "the KL divergence (loss) is the sum over the corresponding loss for each subgrammar" (line 199) but provides no numerical check — no computation of the sum of subgrammar curves, no residual plot, no error metric. This is the main empirical illustration of the paper's central theoretical claim, and the lack of quantitative verification is a significant evidential gap. A single check (e.g., plotting the summed subgrammar divergences against the full KL and reporting the mean absolute deviation) would resolve this.

- **Corollary 4.7 is a tautology dressed as a result.** It states: if gradient updates on one subgrammar do not harm performance on others, then the model learns subgrammars in parallel. This is definitional — it does not advance understanding. The paper acknowledges this is a sufficient condition but does not attempt to verify whether the condition holds empirically. The interesting scientific question is *when and why* the independence condition arises, which is left entirely unaddressed.

- **CKA results lack statistical rigor.** Table 1 reports percentage changes (e.g., +21.7% for attention layers, -4.7% for MLP layers) without standard deviations, confidence intervals, or significance tests, despite the use of 30 random seeds. Some changes are small (e.g., +8.3%) or negative (MLP layers), which weakens the paper's claim that pretraining leads to "very different internal representations." The paper needs to report variance and run paired significance tests.

- **Missing baselines for curriculum learning experiments.** Section 5.1 claims subgrammar pretraining improves final loss, but the only baseline is "from scratch." Without comparisons to random pretraining (unrelated CFGs), uniform data reweighting, or other curriculum strategies, it is unclear whether the benefit is specific to subgrammar structure or simply an effect of any additional training.

### Minor

- **The theoretical results are presented as "fundamental theorems" but the decomposition follows straightforwardly from the autoregressive chain rule and the definition of subgrammar restriction.** The paper would be better served by honestly calibrating its language — the subgrammar framework itself is the genuine contribution; the theorems are clean but direct consequences. The gap between presentation and substance weakens the paper's credibility.

- **No variance reported in most figures.** Despite mentioning 30 random seeds, only Figure 3 shows any measure of variance (a shaded region). All other figures show single curves without error bands, and Table 1 reports averages without standard deviations. For a paper studying learning *dynamics*, this is a significant omission.

- **The depth-generalization finding (Section 6), while cleanly demonstrated, is already well-established** in the literature (Bhattamishra et al., 2020; Lampinen, 2024, both cited). The paper's contribution here is the controlled comparison between length and depth, which is a useful but incremental refinement.

- **The GPT-5.1 anecdotal experiment** (5 non-deep vs. 5 deep examples) is appropriately caveated by the authors but should not factor into the paper's evidentiary weight.

## Nice-to-Haves

- A more mechanistic investigation of parallel learning (e.g., computing gradient interference or cosine similarity between subgrammar-specific gradients) would turn the parallel learning observation from descriptive to explanatory.
- The context-insensitivity assumption in Corollary 4.5 could be directly tested by measuring how much subgrammar distributions vary across different prefixes during training.
- Reporting whether the observed KL decomposition holds at every training step (not just qualitatively in a figure) would dramatically strengthen the core empirical claim.

## Removed Points

- *"The introduction question about child-like sequential learning is never answered"* — The paper explicitly answers this in the abstract and Section 4 (line 219): models learn subgrammars in parallel, unlike children. This point was removed because it is factually inaccurate about what the paper contains.
- *"Cagnetta & Wyart work is misrepresented"* — The paper acknowledges Cagnetta & Wyart and adds the subgrammar-specific angle. The phrasing is slightly loose but not contradictory. Removed.
- *"Parser errors in equation (4)"* — These are parser artifacts, not author errors. Removed.
- *"No formal justification that subgrammar decomposition holds"* — The proof is in Appendix A (stripped by the parser). The main text derivation is informal, but the proof exists in the submission. Demoted from major concern to a minor presentation issue.
- *"Proper subgrammar is defined but never used"* — Minor but true; however, this level of granularity is not worth including in the final review.
- *"Supergrammar is not formally defined"* — The paper gives an informal definition ("a bigger grammar containing a subgrammar"). This is sufficient for context. Removed.

## Novel Insights

None beyond the paper's own contributions. The subgrammar framework is the main novel idea; the reviews do not surface a perspective that the paper's own analysis misses.

## Suggestions

1. **Validate the decomposition numerically.** Compute the sum of the subgrammar KL curves at each epoch and overlay it on the full KL curve, reporting the mean absolute residual. This single figure would make or break the paper's central empirical claim.
2. **Add error bars and significance tests** to all figures and tables. The 30 seeds are mentioned but unused — report standard deviations and run paired tests for the CKA comparisons.
3. **Add baselines to the curriculum learning experiments** (e.g., pretraining on a random unrelated CFG, or uniform data mixing) to isolate whether subgrammar structure specifically drives the improvement.
4. **Tone down the framing of the theoretical contributions.** The subgrammar definitions are genuinely novel and valuable. Presenting the decomposition theorems as direct consequences (rather than "fundamental theorems") would better align the paper's claims with its actual contribution.
5. **Investigate the mechanism of parallel learning.** Compute gradient cosine similarities between subgrammar-specific loss terms, or test whether the independence condition of Corollary 4.7 empirically holds.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Queried for papers on transformers learning formal languages / CFGs / learning dynamics. Weak anchors (avg <3.5): uOnElfFuey (3.0, automaton extraction), NSBP7HzA5Z (3.0, inductive transformers), qgLyKwXVDs (2.0, fine-tuning-free LM), OW5Gf4cse1 (3.0, task complexity). Middle anchors (3.5–7.5): 0pLCDJVVRD (7.0, emergence percolation), F0Zd3knG9j (5.0, hierarchical filtering), aN4Jf6Cx69 (4.5, in-context classification), fp77Ln5Hcc (4.5, depth extrapolation). Strong anchors (>7.5): STUGfUz8ob (7.6, abstract reasoning), Tzh6xAJSll (7.6, scaling laws), n2NidsYDop (8.67, parity with CoT), d8w0pmvXbZ (8.0, training instabilities). **Initial bracket: [4.5, 6.0]** — the paper has genuine contributions (subgrammar framework) but lacks empirical rigor compared to the 7.0 emergence paper.

**Round 2 — Narrowing.** Queried for papers in (4.5, 6.5) on formal grammar learning and CKA/probing analyses. Results: Oashk4fDD9 (6.0, structural inductive bias by simulation), CiiLchbRe3 (5.25, sequential decision making), aWLQTbfFgV (6.25, formal language recognizers), F0Zd3knG9j (5.0, hierarchical filtering), MO5PiKHELW (5.5, syntax acquisition phase transitions), q5lJxCXjiY (5.4, geometric compositionality), pK4Z6NZ2DB (5.2, loss decomposition), nt8gBX58Kh (6.33, neuron multifractal analysis).

Compared to aWLQTbfFgV (6.25, Accept) — that paper has rigorous methodology and clear task framing but less novel conceptual framing. Our paper has a more novel framework but weaker empirical validation. It is weaker overall. Compared to F0Zd3knG9j (5.0, Reject) — similar: both have interesting conceptual contributions but empirical support that does not fully back the claims. Our paper has somewhat stronger theory and framing. Compared to MO5PiKHELW (5.5, Accept) — that paper has thorough causal interventions despite single-model limitations; our paper has less rigorous experiments. **Final score: 5.0.** The subgrammar framework is a real contribution but the empirical validation is not yet at an acceptable standard.

**All anchors consulted (12 total):** uOnElfFuey (3.0, R1), NSBP7HzA5Z (3.0, R1), qgLyKwXVDs (2.0, R1), OW5Gf4cse1 (3.0, R1), 0pLCDJVVRD (7.0, R1), F0Zd3knG9j (5.0, R1+R2), aN4Jf6Cx69 (4.5, R1), fp77Ln5Hcc (4.5, R1), STUGfUz8ob (7.6, R1), Tzh6xAJSll (7.6, R1), n2NidsYDop (8.67, R1), d8w0pmvXbZ (8.0, R1), Oashk4fDD9 (6.0, R2), CiiLchbRe3 (5.25, R2), aWLQTbfFgV (6.25, R2), MO5PiKHELW (5.5, R2), q5lJxCXjiY (5.4, R2), pK4Z6NZ2DB (5.2, R2), nt8gBX58Kh (6.33, R2).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>