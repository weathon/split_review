Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text.

## Summary

The paper identifies a "tokenization dilemma" in Scientific LLMs (Sci-LLMs): treating biomolecular sequences as language destroys functional motifs, while treating them as a separate modality introduces semantic misalignment. The authors propose a context-driven paradigm that bypasses raw sequences entirely, providing LLMs with structured textual context derived from bioinformatics tools (InterProScan, BLASTp). Through systematic comparison across three input modes (sequence-only, context-only, sequence+context) using multiple models, they show that context-only consistently outperforms sequence-only, and that adding raw sequence to context often degrades performance. The paper also provides representation analysis, temporal analysis, efficiency comparisons, and wet-lab validation on novel proteins.

## Strengths

- **Systematic empirical comparison across three input paradigms (Table 1).** The paper evaluates 7 models (4 specialized Sci-LLMs + 3 general LLMs) across three input configurations. The finding that context-only consistently outperforms sequence-only for all models, and that context-only beats sequence+context for all specialized Sci-LLMs, directly supports the core claim. For example, Intern-S1: 86.15 (context-only) vs 43.33 (seq-only) vs 84.03 (seq+context); Evolla: 74.02 vs 59.93 vs 70.53.

- **Representation analysis quantifies the "weak representation" horn of the dilemma (Figure 2, Section 5.2).** The context-driven approach achieves ARI = 0.958 for functional embedding separation, far exceeding NatureLM (0.492), Intern-S1 (0.690), and Evolla (0.809). This provides concrete evidence that sequence tokenization produces poorly organized latent spaces.

- **Layer-wise analysis reveals the "semantic misalignment" horn (Figure 3, Section 5.3).** In Evolla, the SaProt encoder maintains ARI = 0.945, but this drops to 0.916 after Q-Former alignment and to 0.809 at the decoder output. This directly traces the information loss to the cross-modal alignment step — a mechanistic validation of the dilemma.

- **Temporal analysis across 30 years (Figure 4, Section 5.4).** The context-driven approach (DeepSeek-V3) shows graceful degradation (slope −0.618) across proteins from 1995–2024, while Evolla collapses sharply (−0.923). This demonstrates robustness to training-data temporal bias and confirms the method's practical value for real biological discovery.

- **Efficiency analysis (Table 2, Section 5.5).** Even with caveats about preprocessing costs, the context-driven method is substantially cheaper and faster than end-to-end specialized models like Evolla, while achieving higher performance. The practical deployability argument is well-motivated.

## Weaknesses

### Fatal
None.

### Major

- **Internal contradiction in wet-lab validation (Section 5.6).** The body text states: "Evolla (Figure 6) attains a reasonable 80.0% accuracy on Rhodopsin, it fails catastrophically on PETase." However, Figure 6's caption reports 5.00% (1/20 correct) on Rhodopsin and 83.78% on PETase — the exact opposite pattern. These numbers describe completely different experimental outcomes. Since the figures are the primary data, this suggests either a serious error in the figure, a text-writing error, or an experiment that has been rerun with inconsistent reporting. The authors must clarify which numbers are correct and resolve the discrepancy. This does not undermine the paper's core claims (the context-driven method's results are consistent between text and figure), but it damages trust in the wet-lab results and must be fixed.

- **LLM-Score used without any human validation or correlation analysis (Section 5.1).** All quantitative results depend on an LLM-as-judge metric. While this practice is common in NLP, the paper would be substantially stronger with at minimum a human-annotated held-out subset showing correlation between LLM-Score and expert ratings. Given that the context-driven approach produces stylistically natural outputs (natively in the judge LLM's distribution), while raw-sequence outputs may be format-mismatched, even a small human validation would rule out systematic bias as an alternative explanation for the observed gaps.

- **Efficiency comparison may not fully account for preprocessing costs (Table 2, Section 5.5).** The batch-mode time of ~0.13s per sequence for "Our Method" appears to reflect only the LLM API call, not the end-to-end pipeline including BLASTp and InterProScan. The single-query mode shows ~70s (which plausibly includes tool overhead), but the 500× speedup in batch mode is suspicious without clarification that tool preprocessing is amortized and accounted for. The paper references Appendix M for cost details (removed by parser), so this is unverifiable from the main text.

### Minor

- **Label leakage is partially but not fully addressed.** The paper's defense (Section 4) distinguishes "intrinsic analysis" via InterProScan and "homology-based inference" via BLASTp from direct annotation lookup. However, for well-studied proteins with close homologs in Swiss-Prot, the retrieved annotations are nearly identical to ground truth. The wet-lab validation on unpublished sequences partially mitigates this, but only covers two protein families (20 + 37 sequences). A systematic report of BLAST identity scores between test proteins and their homologs would help assess how often the context functionally contains the answer.

- **Overclaim on "sequence degrades performance" consistency.** The paper states "the inclusion of the raw sequence alongside its high-level context consistently degrades performance" (Section 5.1 Takeaway). In Table 1, this holds for all 3 specialized Sci-LLMs, but for general LLMs the pattern is mixed: DeepSeek-V3 (86.03 seq+ctx vs 84.99 ctx-only), GPT-5 (76.45 vs 75.76), and Qwen3 (85.90 vs 84.99) show seq+context slightly *higher* than context-only. The differences are small, but "consistent degradation" overstates the full data. The paper should qualify this as applying primarily to specialized Sci-LLMs.

- **No confidence intervals or statistical tests for temporal trends (Section 5.4).** The slope values (−0.618, −0.923, −0.065) are reported without error bars, confidence intervals, or significance tests. Given the natural variability across proteins within each year, it is unclear whether these slopes are statistically distinguishable from each other or from zero.

### Trivial
None.

## Nice-to-Haves
- Report the distribution of BLASTp sequence identity between test proteins and the homologs used for context, to quantify the label leakage concern.
- Validate the LLM-Score against human expert judgments on a random subset of 50–100 examples.
- Provide confidence intervals for the temporal trend slopes.
- Include end-to-end timing for the batch mode of "Our Method" that accounts for all preprocessing.
- Run specialized Sci-LLMs with a few in-context examples adapted to their input format, to rule out prompt-format artifacts as a driver of the degradation pattern.

## Removed Points

These points were flagged in the inputs but are removed with justification:

1. **"Unvalidated LLM-Score invalidates all quantitative results (Structural/Fatal)"** — Overstated. LLM-as-judge is standard practice across NLP and ML evaluation. While human validation would strengthen the paper, the lack of it does not invalidate the relative comparisons, especially since the same metric is applied uniformly to all conditions. Demoted to Minor.

2. **"Unfair baseline comparisons inflate the performance gap"** — Factually incorrect about the models' capabilities. Intern-S1, Evolla, and NatureLM are LLMs trained on text data; feeding them text context is not "out of distribution." These models demonstrably improve with context (compare seq-only vs context-only in Table 1: Intern-S1 from 43.33→86.15, Evolla from 59.93→74.02), confirming they can process text context effectively. Removed.

3. **"Representation analysis is circular (context contains function)"** — Misunderstands the paper's claim. The paper argues that context provides better functional representation *because* it captures high-level information that sequences cannot easily express. This is the point, not a flaw. Removed.

4. **"BLASTp essentially retrieves the correct answer"** — The paper uses annotations from *homologs*, not from the query itself, and explicitly uses InterProScan for intrinsic feature analysis as a complementary source. The wet-lab validation on novel unpublished sequences directly tests generalization. The existing mitigation is reasonable, though imperfect. Moved to Minor (see label leakage point above).

5. **"5% on Rhodopsin implies evaluation bug affecting all results"** — The claim that this "suggests an evaluation bug that also affects the context-driven method's numbers" has no evidence. The context-driven method achieves 100% on the same task. A bug affecting only Evolla is possible (and the figure/data speak for themselves), but spreading it to unrelated results is unwarranted. Removed.

6. **Various generic nitpicks** (missing appendix content, formatting, missing statistical methodology not standard in this subfield) — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the Section 5.6 contradiction** between the text (80.0% on Rhodopsin for Evolla) and the figure caption (5.00%). Clarify which numbers are correct and rerun or explain the discrepancy before proceeding with any submission.

2. **Add a small human validation study** (50–100 examples) showing correlation between LLM-Score and expert biologist ratings to address the evaluation metric concern.

3. **Report BLAST identity statistics** for the test set to quantify how often the context-driven approach relies on near-identical homologs versus genuinely inferring function from distant or fragmentary matches.

4. **Qualify the "consistent degradation" claim** as applying to specialized Sci-LLMs, not universally to all models tested.

5. **Add confidence intervals** (bootstrapped or otherwise) to the temporal trend slopes in Figure 4.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>