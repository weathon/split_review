Now let me run calibration searches to anchor the score.Round 1 bracket: 4–6.5. Let me narrow with a more targeted round 2.Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

APDD (Active Probabilistic Drug Discovery) is an early-stage virtual screening framework that chains three steps: (1) probabilistic clustering of a molecule library using Tanimoto-similarity as co-binding probability (MPC), (2) selective VinaGPU+ docking of cluster representatives, and (3) active-learning selection of candidates for simulated wet-lab experiments with probability-updating feedback. Evaluated on 90 targets from DUD-E and LIT-PCBA, the paper claims an average 80% reduction in docking computations and 70% reduction in wet-lab experiments relative to a brute-force docking baseline.

---

## Strengths

- **Extensive empirical scope**: Results cover 79 DUD-E targets and 11 LIT-PCBA targets with per-target breakdowns (Tables 1–2 / 3 in §5.2), providing more breadth than typical drug-discovery ML papers.
- **Cluster-distribution hypothesis validated empirically**: Table 3 in §5.3 directly measures active molecule cluster concentration (ratio $R_k$ and cluster purity $P_k$), showing that on DUD-E, nearly all actives fall in clusters with fewer than 8 molecules, providing evidence for the central assumption driving the method.
- **Scalability test**: §5.4 / Table 4 demonstrates the pipeline on 1.4M-molecule libraries across five proteins, confirming that the efficiency advantage (≈80% cost reduction) persists at realistic library sizes.
- **Coherent probabilistic machinery**: The multi-modal score fusion formula (Eq. 2, §4.2) under conditional independence is principled and consistent with the MPC framework; the accumulated-pairwise representative selection criterion (§4.2) is a reasonable way to avoid docking outlier molecules.

---

## Weaknesses

### Fatal
None. The methodology is internally coherent and the experiments are real. The flaws below are evidential and evaluative, not structural.

### Major

- **DUD-E evaluation inflates apparent benefit.** DUD-E was designed so that decoys are matched to actives on physicochemical properties but are structurally dissimilar; the paper itself confirms this in §5.3: *"active molecules are completely separated from inactive molecules in datasets of DUD-E."* Any Tanimoto-similarity-based method will exhibit anomalously high performance on DUD-E because the dataset's construction guarantees actives form tight, isolated clusters in fingerprint space. The headline figures (82% docking / 75% wet-lab reduction) are therefore largely a dataset artifact. The LIT-PCBA results—where actives and inactives are drawn from the same assay, producing less artificial separation—tell the more honest story: 85% docking but only **40%** wet-lab reduction. The paper never acknowledges or discusses this 35-percentage-point gap between DUD-E and LIT-PCBA wet-lab savings, leaving the core efficiency claim unsubstantiated for real compound libraries.

- **Single strawman baseline.** The only comparison is Vina Enumeration (VE): dock every molecule, pick the top scorers by raw score. This is the weakest imaginable baseline—any pre-filtering whatsoever would beat it. The paper justifies excluding ML-based methods (§5.1: "machine learning models cannot be retrained due to the limited number of wet experiments"), which is reasonable, but this does not eliminate the large class of ligand-based, non-ML pre-filters (e.g., simple Tanimoto k-NN search from known actives, pharmacophore filters, or even a naïve cluster-once-then-dock-randomly baseline). Without at least one such comparison, it is impossible to determine whether the efficiency gains come from the probabilistic framing specifically or simply from not docking every molecule in the library. The probabilistic active-selection machinery (§4.3) is the methodological novelty, and its contribution over vanilla similarity clustering is never demonstrated.

- **No ablations.** APDD combines several interacting components: MPC clustering with Tanimoto probability, isotonic-regression probability calibration, accumulated-pairwise representative selection, the two-step cluster-then-molecule query strategy, and the context probability refinement. None of these are ablated. It is unknown whether the probabilistic MPC formulation outperforms k-means or agglomerative clustering at the same distance cutoff; whether isotonic-regression calibration adds value; whether the two-step active selection improves over random selection within top clusters; or whether capping probabilities at 0.3 (§4.2) is critical. Without ablations, the reader cannot attribute the results to any specific component.

### Minor

- **Large-scale experiment artificially preserves the DUD-E artifact.** Section 5.4 constructs a 1.4M-molecule library by pooling DUD-E decoys from multiple proteins and assigning them all as inactives for a single target. Since DUD-E decoys are by construction structurally distinct from actives, this augmentation amplifies the active/inactive separation that already inflates DUD-E results; the 20% cost retention figure for million-scale libraries is not a reliable proxy for performance on real commercially diverse compound libraries.

- **Core probabilistic assumption lacks quantitative calibration in the main text.** Equation (1) defines P(co-binding | FP(i), FP(j)) = Tanimoto(i, j). The paper states this "is further validated using statistics from Lit-PCBA/DUD-E/PubChem datasets" (§4.1) but provides no details in the main text—no figure of Tanimoto bins versus empirical co-activity rates, no calibration curve. Given that the entire recall-improvement objective (Eq. 3) rests on this mapping, the absence of validation evidence from the main body is a real gap.

- **Multi-modal fusion (Eq. 2) presented but never evaluated.** Section 4.2 derives a closed-form fusion formula for combining multiple docking-method probabilities and explicitly notes "alternative or multiple docking methods can also be employed." All reported experiments use only VinaGPU+. The multi-modal capability is a theoretical contribution that has no empirical support.

### Trivial

- Section 5.2 discusses failure cases (MAPK1, KAT2A, PKM2, where VinaGPU+ AUC < 0.5) only qualitatively in one paragraph; a systematic analysis of when APDD loses advantage would strengthen the paper but is not critical.

---

## Nice-to-Haves

- **Add a minimal similarity-based pre-filter baseline**: cluster by Tanimoto, dock one representative per cluster, select top clusters, pick final candidates at random. This single addition would reveal how much of APDD's gain comes from clustering alone versus the probabilistic active-selection refinement, and would directly address the "what does the ML component contribute?" question.
- **Characterize LIT-PCBA cluster purity analogously to Table 3 on DUD-E**: an analysis of $R_k$ and $P_k$ on LIT-PCBA would explain why wet-lab savings drop from 75% to 40% and would clarify the method's operating regime.
- **Include at least one calibration plot** for Eq. (1): Tanimoto bins vs. empirical co-activity rates on a held-out split of PubChem or LIT-PCBA.
- **Use a genuinely diverse compound library** (e.g., a ZINC fragment subset or Enamine REAL subset) for the large-scale experiment rather than repurposed DUD-E decoys.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "hit rate statistics work against the clustering assumption"**: The paper cites 10–35% hit rates and 50% structural similarity to motivate diversity-aware ranking. The critic claims this contradicts tight active clustering. This is a framing tension, not a logical inconsistency — hits can cluster in chemical space while still being diverse from final drugs after optimization. Removed as speculative.

- **Harsh Critic — "preset recall number is circular"**: The critic suggests that if the target recall is set to match whatever VE achieves, the comparison is circular. No evidence of this appears in the paper; the paper says it terminates "when recall rate of the top 100 molecules reaches the target recall rate" (§5.1). This is a speculation, not a verified problem. Demoted/removed.

- **Harsh Critic — "prior methods cannot separate actives from decoys is asserted but not demonstrated"**: While this claim in §4.1 is not backed by a citation directly in that paragraph, it is a reasonable and widely accepted characterization of unsupervised UMAP clustering and physicochemical-property-based filtering. The harsh framing as an unsupported assertion is overstated.

- **Strength Finder — "principled probabilistic fusion (Eq. 2) as a strength"**: This is removed from the strengths section because the capability is never evaluated experimentally; listing it as a strength is misleading given it is an unvalidated theoretical extension.

- **Strength Finder — general statements about importance of the problem**: Removed as generic.

---

## Novel Insights

The most genuinely informative observation in the reviews — not widely emphasized in the paper itself — is the **diagnostic value of the DUD-E / LIT-PCBA performance gap**. The 35-percentage-point difference in wet-lab savings (75% vs. 40%) directly quantifies how much of the headline efficiency gain depends on the artificial active/decoy structural separation built into DUD-E. This gap effectively functions as an internal ablation on dataset difficulty: when actives and inactives are less cleanly separated, the method's wet-lab advantage collapses substantially. The authors should treat LIT-PCBA as their primary benchmark going forward, and use the DUD-E/LIT-PCBA delta as a diagnostic for how sensitive any similarity-based pipeline is to the degree of latent active/inactive separation in the library.

---

## Suggestions

1. Replace or supplement the VE baseline with a minimal similarity-based pre-filter (cluster → dock representative → score) so reviewers can isolate what the probabilistic ML component contributes.
2. Treat LIT-PCBA as the primary benchmark and lead with its numbers (85% docking / 40% wet-lab); report DUD-E numbers with an explicit caveat about the dataset's active-decoy construction bias.
3. Add a 2–3 component ablation: (a) MPC vs. simple k-means at the same radius, (b) isotonic regression calibration on vs. off, (c) active query strategy vs. random within top clusters.
4. Move the Tanimoto-probability calibration validation from "further validated in datasets" to a concrete figure (Tanimoto bin vs. empirical co-activity rate) in the main text.
5. Replace the large-scale test's artificially assembled DUD-E-decoy background with a structurally diverse compound library to provide a more credible million-scale benchmark.

---

## Score and Decision

**Axis evaluations**:
- *Originality*: Moderate. Combining probabilistic clustering, selective docking, and active learning in this three-step pipeline is a reasonable engineering contribution, but each component draws on existing work (MPC, VinaGPU+, isotonic regression). The integration is new, but not novel in individual parts.
- *Importance of research question*: High. Reducing virtual-screening cost while maintaining recall is a genuine practical problem.
- *Whether claims are well-supported*: Weak. The headline 80%/70% claim relies primarily on a biased benchmark with a strawman baseline.
- *Soundness of experiments*: Moderate. Large target count (90) is a strength; DUD-E bias and single baseline are significant gaps.
- *Clarity of writing*: Acceptable. The method description is reasonably clear.
- *Value to research community*: Limited in current form. The evaluation design choices prevent the community from knowing whether the probabilistic machinery genuinely works better than simpler alternatives.

**Calibration**:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| kYg04pmX7i | Molecular Active Learning: LLMs | 4.40 | R2 | Similar in scope (active learning for drug discovery), APDD has more experiments but comparable evaluation limitations |
| bKAqK7Bh7n | MF-LAL | 5.20 | R2 | More sophisticated multi-fidelity methodology, similar evaluation concerns; APDD is at roughly this level or slightly below |
| gVkX9QMBO3 | Efficient Biological Data Acquisition | 6.25 | R2 | More theoretically grounded with real biological assay validation; APDD is weaker due to biased benchmarks and single baseline |
| RyWypcIMiE | Reframing SBDD Evaluation | 6.50 | R2 | Higher-impact methodological contribution; APDD is weaker |
| HBbbhAZuia | DockedAC | 5.75 | R1 | Dataset paper with broader scope; APDD's methodology is more original but evaluation is weaker |
| An87ZnPbkT | GNNAS-Dock | 3.00 | R1 | Clearly weaker; APDD has more experiments and a complete pipeline |
| gHLWTzKiZV | FlexDock / Unbalanced FM | 8.00 | R1 | Much stronger; novel methodology, solid evaluation |
| S8gbnkCgxZ | Redefining Bioactivity Prediction | 7.00 | R2 | More principled dataset contribution addressing bias systematically; APDD is weaker |

**Round 1 bracket**: 4–6.5  
**Round 2 narrowing**: The paper sits between kYg04pmX7i (4.40) and bKAqK7Bh7n (5.20): more experimental work than the LLM active learning paper, but evaluation design is as problematic as MF-LAL. The major issues (DUD-E bias + single baseline + no ablations) together make it clearly weaker than gVkX9QMBO3 (6.25), which has genuinely principled AL and real biological assay experiments. APDD's LIT-PCBA results remain positive (40% wet-lab reduction) and the system works, so it's not at the 3.0 tier. Score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>