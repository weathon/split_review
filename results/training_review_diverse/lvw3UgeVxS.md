Now I have a thorough understanding of the paper. Let me compile the final consolidated review, verifying each claim against the actual paper text.

---

## Summary

gRNAde is a geometric deep learning pipeline for RNA inverse design that conditions on 3D backbone structures. It introduces a multi-state Graph Neural Network encoder that processes conformational ensembles with permutation-invariant pooling, enabling both single-state and multi-state sequence design. The method is evaluated on a single-state benchmark (14 RNA structures, 56% recovery vs. 45% for Rosetta), a multi-state benchmark showing 3–5% improvement over single-state variants, and a zero-shot ranking study on a ribozyme fitness landscape (~75K mutants).

## Strengths

1. **Superior sequence recovery and speed over Rosetta, with additional comparison against a concurrent deep learning method.** gRNAde achieves 56% native sequence recovery on 14 benchmark RNAs, outperforming Rosetta (45%), FARNA (32%), and RDesign (43%), while reducing inference from hours to under a second on GPU (Section 4.1, Figure 3). The inclusion of RDesign (Tan et al., 2023) as a baseline strengthens the case beyond the historical Rosetta numbers alone.

2. **First multi-state inverse folding pipeline with per-nucleotide evidence for architectural benefit.** The multi-state GNN explicitly conditions on conformational ensembles, yielding 3–5% improvement over an equivalent single-state model. The per-nucleotide analysis (Figure 4b) shows that gains concentrate in nucleotides that undergo base-pairing changes or have high RMSD across states — a fine-grained pattern that is not trivially explained away as a data-quantity artifact. The model is described as a plug-and-play component applicable to other geometric GNN pipelines (Section 2.2).

3. **Zero-shot fitness landscape ranking with practical significance.** On ~75K mutants of an RNA polymerase ribozyme, gRNAde's perplexity outperforms random baselines and single-site saturation mutagenesis at low design budgets (top 10 mutants yield 4-fold fitness improvement over wild type). The model is used zero-shot (no fine-tuning on assay data), demonstrating practical utility for prioritizing mutants in wet-lab campaigns (Section 4.3, Figure 5).

4. **Rigorous generalization evaluation via structural clustering.** The dataset is split using US-align with TM-score >0.45, ensuring that test sets contain structurally dissimilar RNAs from the training set. The single-state split explicitly excludes the 14 benchmark RNAs and structurally similar clusters; the multi-state split progressively tests on more flexible RNAs (Section 3).

5. **Comprehensive in-silico evaluation framework.** Beyond recovery, the pipeline evaluates designs using secondary structure self-consistency (MCC via EternaFold), tertiary structure metrics (RMSD, TM-score, GDT_TS via RhoFold), and perplexity — providing multi-faceted design quality assessment (Section 2.3).

## Weaknesses

### Fatal
None.

### Major

1. **Multi-state vs. single-state comparison: potential confound between architecture and data quantity.** The paper trains "equivalent single-state and multi-state gRNAde models on the multi-state split" (Section 4.2, line 309) but does not specify how the single-state model is trained. If the single-state model sees only one conformation per RNA per epoch while the multi-state model sees all available conformations, then the 3–5% improvement could partly reflect more training data rather than the architectural benefit of multi-state processing. The per-nucleotide analysis (Figure 4b) partially mitigates this — improvements concentrated in flexible regions suggest architectural benefit beyond raw data — but without clarification or a controlled experiment (e.g., training the single-state model on the same total number of structural examples by treating each conformation independently), the core architectural claim is not fully isolated. *Severity: this weakens, but does not invalidate, the multi-state contribution.*

2. **Single-state benchmark against Rosetta relies on 15-year-old published numbers without contemporary validation.** The paper transparently states it has not run Rosetta itself (line 265: "recent builds do not include RNA recipes") and uses recovery numbers from Das et al. (2010). This introduces uncertainty about whether the exact benchmark protocol, structures, and pre-processing are reproduced. The comparison to RDesign (43% recovery) provides a fallback — gRNAde still leads — but the headline "56% vs 45%" is not as cleanly supported as the paper's framing implies. The paper should report per-structure recovery for the 14 RNAs and clarify the relationship between the 14 benchmark structures and the 100-sample test set (line 195: "add all the RNAs in these clusters to the test set (100 samples)").

3. **Zero-shot ranking experiment lacks a non-trivial baseline.** The comparison is to random selection from various pools and single-site saturation mutagenesis. While outperforming random is a low bar, the paper does show gRNAde beats single-site saturation (a real experimental strategy). However, the absence of any sequence-based baseline (e.g., nucleotide conservation from homologs, a Rosetta energy score, or a simpler statistical potential) limits confidence that perplexity captures genuinely useful signal beyond trivial sequence properties. The paper would be stronger with at least one additional non-random baseline.

### Minor

1. **Missing error bars on the main multi-state figure (Figure 4a).** The paper notes that the figure plots results for "one consistent random seed across all models" and defers variance estimates to the appendix (line 297). The experimental setup states "standard deviations are reported across 3 consistent random seeds for all models" (line 211), but the main figure — which readers will primarily consult — does not show this. For a claimed 3–5% improvement, readers need to see whether the difference is statistically significant across seeds.

2. **The multi-state test set composition is underspecified.** The test set is constructed from "clusters with the highest median intra-sequence RMSD" (line 200). The paper does not report the distribution of the number of conformations per RNA in the test set. If some RNAs have 2 states and others have 10, the evaluation is heterogeneous and the results may be dominated by RNAs with many states. Reporting this distribution would aid interpretation.

3. **Self-consistency metrics are described but not prominently reported in main results.** Section 2.3 describes secondary and tertiary structure self-consistency scores, but the main results (Sections 4.1, 4.2) focus on recovery and perplexity. Given that self-consistency (especially scRMSD) is arguably more informative for practical design, its omission from the main figures is a missed opportunity. The authors note that RhoFold has limitations (Section 2.3), but reporting these scores would still strengthen the evaluation.

### Trivial
- The scatter plot in Figure 3b is shaded by perplexity, making it hard to interpret in black-and-white print.
- The paper notes that temperature 0.1 is used for sampling but does not explicitly discuss the recovery-diversity trade-off in the main text (only briefly in Section 2.3).

## Nice-to-Haves
- A controlled experiment where the single-state model is trained on the same total number of structural examples as the multi-state model, to fully isolate the architectural benefit.
- A non-random baseline for the zero-shot ranking experiment (e.g., sequence conservation from homologous RNAs, or a simple energy-based score).
- Self-consistency metrics (scRMSD, scTM, scMCC) reported in the main figures alongside recovery and perplexity.
- A table of per-structure recovery for the 14 benchmark RNAs, clearly separating the 14 Das et al. structures from the broader 100-sample test set.
- A plot showing the recovery-diversity trade-off across temperature values (0.1, 0.5, 1.0).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No comparison to other recently published RNA inverse folding methods"** — The paper *does* compare to RDesign (Tan et al., 2023) in Figure 3a and reports its recovery (43%). The reviewer's suggestion to extend this comparison to the multi-state benchmark is scope creep; the multi-state benchmark tests a capability (multi-state design) that RDesign does not offer.
- **"The dataset release is mentioned only implicitly"** — The paper describes using RNASolo data and states the data cutoff; any specific data release statement would be in the appendix (which the parser stripped). The paper's reproducibility documentation cannot be assessed from the parsed text alone.
- **"Missing error bars... stated to be available in the appendix"** — Per the parser, appendix content is not available. The paper states variance estimates are in the appendix (line 297), so this is not an omission — the information exists in the original submission. However, I retain the concern as a *Minor* weakness because the main figure should ideally include variance directly.
- **"The comparison is only to random baselines" (zero-shot ranking)** — Incorrect. The paper also compares to single-site saturation mutagenesis (line 328), which is a non-random experimental baseline. The reviewer overlooked this.
- **"No correlation coefficient reported for fitness vs. perplexity"** — The paper reports expected maximum improvement in fitness (Figure 5), not per-sequence correlation. This is a deliberate choice that matches the experimental design (simulating a screening campaign), not a mistake.
- **Pure formatting/style nitpicks** about readability in black-and-white print and presentation — these are minor presentation issues, retained in Trivial.

## Novel Insights

The reviews collectively surface an important tension in evaluating multi-state models: the architectural innovation (multi-state message passing + pooling) yields a plausible 3–5% improvement, but the lack of a data-quantity-controlled baseline means that part of this gain could be attributed to simply seeing more structural examples. This is a recurring challenge in multi-task multi-view learning papers more broadly — authors should distinguish "seeing more data" from "processing data in a multi-view-aware manner." The per-nucleotide analysis in Figure 4b (improvements concentrated in flexible regions) is the right kind of evidence to address this, and the paper would benefit from explicitly framing it as such.

## Suggestions

1. **Clarify the training data for the single-state baseline in the multi-state experiment.** State explicitly whether it trains on all available conformations as independent examples or on only one per RNA. If the former, this directly addresses the confound. If the latter, run a controlled experiment where data quantity is matched.

2. **Add error bars (over 3 seeds) to Figure 4a** directly, rather than deferring to the appendix, so readers can assess whether the 3–5% multi-state improvement is statistically significant.

3. **Report per-structure recovery for the 14 Das et al. RNAs in a table**, clearly showing which structures correspond to the benchmark and how gRNAde and Rosetta compare on each. Clarify whether the 56% figure is computed over the 14 structures or the 100-sample test set.

4. **Add at least one non-random baseline to the zero-shot ranking experiment** (e.g., sequence conservation from an MSA, or a simple position-weight matrix derived from homologs) to demonstrate that gRNAde's perplexity adds value beyond trivial sequence signals.

5. **Include self-consistency metrics (scRMSD, scMCC) in the main evaluation figures**, even if acknowledged to be noisy due to RhoFold's limitations. These are more informative for practitioners than recovery alone.

## Score and Decision

The paper makes a solid contribution to an underexplored area (3D RNA inverse design) with a practical method that outperforms existing tools. The weaknesses are real but addressable: the Rosetta comparison is transparently caveated and supported by a deep learning baseline (RDesign); the multi-state data quantity confound is a genuine concern but the per-nucleotide analysis provides supporting evidence for the architectural claim. None of the issues are fatal. With clarifications and controlled experiments, the paper would be a strong contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>