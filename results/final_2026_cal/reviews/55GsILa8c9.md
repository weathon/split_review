Now I have all the evidence needed. Let me produce the consolidated review.

---

## Summary

CausalNovo proposes a model-agnostic causal framework for *de novo* peptide sequencing that learns to focus on signal fragment ions rather than spurious noise peaks. Grounded in Reichenbach's Common Cause Principle, the method uses a Structural Causal Model to derive two principles—independence and sufficiency—operationalized through causal interventions in latent space and information-theoretic objectives. Experiments across three benchmark datasets (Nine-species, Seven-species, HC-PT) with three strong baselines (CasaNovo, AdaNovo, π-HelixNovo) show consistent improvements at the amino acid, peptide, and PTM levels, along with enhanced robustness to noise perturbations and better generalization across varying noise-signal ratios.

## Strengths

- **Principled causal formulation grounded in theory.** Section 3.2 introduces a Structural Causal Model (Figure 2A) for peptide sequencing and derives two testable properties—independence and sufficiency—from Reichenbach's Common Cause Principle. This goes beyond ad-hoc denoising by grounding the framework in causal theory, and the SCM is clearly connected to the practical objectives in Section 3.3.

- **Consistent and substantial performance gains across multiple baselines and datasets.** Table 1 shows gains that are reproduced across all three baseline models. For example, on HC-PT, CasaNovo + CausalNovo improves amino acid precision by +9.0% (0.525→0.635) and peptide precision by +13.5% (0.324→0.459); π-HelixNovo + CausalNovo improves amino acid precision by +7.1% (0.465→0.536) on Seven-species. These gains are consistent and often substantial.

- **Robustness to noise perturbation convincingly demonstrated.** Figure 1 and Figure 3 show CausalNovo consistently mitigates performance degradation when noise peaks are perturbed, with average relative improvements of +14.9%, +15.7%, and +13.5% over the three baselines on HC-PT. The NSR analysis (Figure 4) further confirms that CausalNovo maintains higher precision as noise increases, with average improvements of +10–12%.

- **Model-agnostic design validated across diverse architectures.** The framework improves CasaNovo (Transformer), AdaNovo (conditional mutual information), and π-HelixNovo (spectrum augmentation), demonstrating generality beyond any single architecture. The cross-species validation (Table 3) shows consistent improvements across all nine species.

- **Attention analysis provides interpretable evidence of causal focus.** Table 7 shows CausalNovo increases the proportion of predictions attending to all three causal peaks from 19.26% to 32.87%, and decreases predictions ignoring all causal peaks from 12.73% to 10.76%, providing direct evidence that the framework shifts attention toward causal fragment ions.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparisons against directly relevant recent methods.** The paper's related work cites ContraNovo (Jin et al., 2024) and RankNovo (Qiu et al., 2025), and the Conclusion explicitly notes these methods use a different training protocol. Yet neither appears in the main comparison tables. The abstract claims CausalNovo "surpasses several recent methods by considerable margins," but without comparison to these two closely related methods—one of which (ContraNovo) also uses contrastive learning between spectra and peptides—the strength of this claim cannot be fully evaluated. The authors acknowledge this limitation in the Conclusion, but it remains a gap in the current evidence. Including these methods under the same evaluation protocol (NovoBench), even if only on the shared datasets, would significantly strengthen the paper.

### Minor

- **No statistical significance or variance reporting.** Every metric in Tables 1–3 is reported without standard deviations, confidence intervals, or replication information. This is especially concerning for the ablation studies (Table 4), where individual component contributions are as small as 0.4–1.2%. Without variance estimates, it is difficult to assess whether these smaller gains are reliable. Following standard practice in the field, reporting results over multiple runs would improve confidence in the findings.

- **SearchNovo comparison is insufficiently caveated.** The paper states "CausalNovo improves CasaNovo's precision by +3.5% on Nine-species, which also outperforms SearchNovo by +1.4%." However, SearchNovo uses a hybrid search strategy (not pure *de novo*), as the paper itself notes in the Related Work. This comparison should be more clearly caveated in the main text, not just in the related work section.

- **Discrepancy between published and retrained baseline numbers not discussed.** The retrained baselines (marked †) differ from the published NovoBench numbers, sometimes substantially (e.g., CasaNovo's amino acid precision on Nine-species: 0.697 published vs. 0.741 retrained). While the paper notes "We retrain the baselines with the same configurations," these differences are not explained. The variations go in both directions (AdaNovo retrained is *lower* than published on Nine-species), so this does not systematically favor CausalNovo, but a brief explanation of potential causes (data splitting, preprocessing differences, hyperparameter tuning) would be helpful.

- **Attention analysis uses an arbitrary fixed cardinality.** Table 7 reports counts of causal peaks among "top three most attended peaks" but does not justify why three was chosen or whether results are robust to different cardinalities. The total number of analyzed predictions (350,274) should also be stated explicitly in the caption or text rather than being left for the reader to infer.

### Trivial
- The Relative Improvement (RI) metric in Section 4.4 is defined as "the relative performance reduction of CausalNovo compared to the baseline models," but the text and figures describe it as an improvement; the definition could be stated more clearly.

## Nice-to-Haves

- **Run the same data augmentation without causal objectives as a control.** A natural control experiment: train CasaNovo with replace+enhance spectra as input but without the CEM and causal objectives. This would isolate whether gains come from richer input data or from the causal learning objectives themselves. Table 5 partially addresses this but does not test this specific control.

- **Extend ablation to additional baselines.** Table 4 ablates components only on CasaNovo. Showing that components transfer similarly to AdaNovo and π-HelixNovo would strengthen the claim of model-agnosticism.

- **Randomize the vulnerability perturbation.** The vulnerability analysis applies a deterministic perturbation. Randomizing the perturbation (different noise peaks replaced across runs) and reporting variance would strengthen the robustness claim.

- **Report training efficiency trade-offs more concretely.** The paper mentions 2.3× training time overhead. Reporting wall-clock time for each method would help practitioners assess the cost-benefit.

## Removed Points

These points were raised by reviewers but are removed per the filtering criteria:

- *Criticism about replace-based perturbation introducing batch-level correlations:* Speculative concern without evidence. This is a standard augmentation design. **REMOVED** (speculative, not verified against paper content).
- *Criticism about maximum peaks (150) being too small:* This is a common preprocessing threshold in mass spectrometry; no evidence is provided that it harms results. **REMOVED** (speculative, not grounded in evidence).
- *Criticism about RCCP derivation being "loose":* The paper's SCM makes standard causal assumptions. The paper acknowledges limitations and validates with 18 ion types. The theoretical concern is adequately addressed. **DEMOTED** from the reviewer's framing; no remaining actionable weakness.
- *Complaints about missing appendix content, proofs, references:* Parser artifact; the original submission includes these. **REMOVED** per hard rules.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is the structural tension between the paper's strong empirical results and the field's evolving evaluation standards. The paper convincingly demonstrates that imposing causal structure (independence + sufficiency) on latent representations yields measurable robustness gains across diverse architectures. However, the proteomics community is transitioning to more realistic evaluation protocols (large external corpora, OOD test sets, as used by ContraNovo/RankNovo). The paper's candid acknowledgment that its evaluation lags this emerging standard, while simultaneously claiming to "surpass several recent methods," creates a mismatch that future work in this area should carefully navigate.

## Suggestions

1. **Add comparisons against ContraNovo and RankNovo** under the same evaluation protocol (NovoBench). Even if their full training protocol cannot be replicated, running inference with their released models on the shared benchmark test sets would be feasible and would directly substantiate the claim of "surpassing several recent methods."
2. **Add variance estimates** by reporting mean and standard deviation over at least 3 independent training runs for the main results and ablation studies.
3. **Briefly explain the retrained baseline discrepancies** in the Experimental Setup section—e.g., whether differences stem from data splitting, preprocessing choices, or hyperparameter tuning.
4. **Caveat the SearchNovo comparison** more explicitly by noting its hybrid search nature in the main result text, not just in Related Work.
5. **State the total number of predictions analyzed** in the attention analysis table and justify the choice of "top three."

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Searched across three bands on topics related to *de novo* peptide sequencing, causal ML, and proteomics benchmarks.

- Weak band (< 3.5, avg scores: 1.60–3.33): Papers like "Protein Language Model–Aligned Spectra Embeddings for De Novo Peptide Sequencing" (2.50) and "PEPTRIX" (1.60). CausalNovo is clearly stronger than these.
- Middle band (3.5–7.5, avg scores: 4.00–6.00): Included PepBenchmark (6.00), PepTri (5.50), Delta Embeddings (6.00), "Mitigating Spurious Correlations in LLMs" (4.00), "Reducing Spurious Correlations in CNNs" (4.00). CausalNovo sits in this band.
- Strong band (> 7.5, avg scores: 8.00): Papers from unrelated domains (protein generation, language models). Not comparable.

**Initial bracket:** 5.0–6.5.

**Round 2 — Narrowing.** Searched within (5.0, 6.5):

- PepBenchmark (6.00, Accept Poster): Benchmark paper with comprehensive datasets but limited technical novelty. CausalNovo has more technical contribution but is slightly weaker due to missing comparisons and no variance reporting. → CausalNovo is *slightly below* this anchor.
- PepTri (5.50, Accept Poster): Diffusion model for peptide design with implementation clarity issues. Scores: 4,6,4,8. CausalNovo is better structured, has clearer ablations, and more convincing evaluation. → CausalNovo is *slightly above* this anchor.
- Delta Embeddings (6.00, Accept Poster): Well-structured causal representation learning paper. CausalNovo has a comparably clear causal formulation but weaker on evaluation rigor. → CausalNovo is *slightly below* this anchor.
- Strong Correlations CCO (5.20, Accept Poster): Theoretical paper with mixed reviews (scores: 6,8,4,2,6). CausalNovo is empirically stronger. → CausalNovo is *above* this anchor.
- GeomMotif (5.50, Accept Poster), 3DCS (5.50, Accept Poster): Benchmark papers in related domains.
- "Risk-Optimal Prediction" (5.50, Reject): Causal inference paper. Not directly comparable.

**Final calibration:** CausalNovo is most comparable to PepTri (5.50) on methodological novelty and evaluation scope, and slightly weaker than PepBenchmark (6.00) and Delta Embeddings (6.00) on rigor. The missing comparisons and lack of variance reporting prevent it from reaching the 6.0 level, but the core contribution is solid and better than the reject-range papers.

**Final score: 5.5** | **Decision: Accept**


MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>