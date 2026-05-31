Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces gRNAde, a geometric deep learning pipeline for RNA inverse design conditioned on 3D backbone structures. The model uses a multi-state GNN (GVP-based) with autoregressive decoding to design RNA sequences for single structures or conformational ensembles. The paper reports 56% native sequence recovery on a 14-RNA benchmark (vs. 45% for Rosetta numbers from 2010 and 43% for the concurrent deep learning method RDesign), demonstrates 3-5% improvement from multi-state conditioning, and shows zero-shot ranking of mutant fitness on a ribozyme fitness landscape.

## Strengths

1. **Clean multi-state GNN extension with practical value.** The multi-state encoder processes conformational graphs independently with order-invariant pooling — a simple, plug-and-play extension to any geometric GNN pipeline. The 3-5% sequence recovery improvement over single-state models is convincingly shown to concentrate on structurally flexible nucleotides (Figure 4b), providing mechanistic insight into where multi-state conditioning helps.

2. **Outperforms the state-of-the-art deep learning baseline (RDesign).** On the 14-structure Das et al. benchmark, gRNAde achieves 56% vs. RDesign's 43% recovery. This is the fairest contemporary comparison in the paper and represents a clear advance over an existing GNN-based RNA inverse folding method.

3. **Dramatic speed advantage.** The paper documents inference times of ~1 second on GPU and ~10 seconds on CPU for RNAs of 60+ nucleotides, vs. hours reported for Rosetta. This practical advantage for high-throughput design is well-supported.

4. **Structural clustering for fair generalization evaluation.** The training/validation/test splits are based on US-align structural similarity (TM-score > 0.45), ensuring test RNAs are structurally dissimilar from training RNAs. The single-state split further excludes all RNAs in the same structural clusters as the 14 benchmark structures.

5. **Per-nucleotide analysis of multi-state benefit.** The breakdown in Figure 4b showing improved recovery on nucleotides that change base pairing or have high inter-state RMSD is clean evidence for the multi-state model's mechanism of action.

## Weaknesses

### Fatal
None.

### Major

- **The Rosetta comparison is uncontrolled and dated.** The headline "56% vs. 45%" compares gRNAde against Rosetta numbers taken from Das et al. (2010) — a 15-year-old publication. As the paper honestly acknowledges (footnote, line 264-265), the authors did not run Rosetta themselves because recent builds lack RNA recipes. This means hardware, random seeds, protocol versions, and exact structure inputs are not matched. Variance for Rosetta is also unreported, so the reader cannot assess significance. The paper's fairest contemporary comparison — gRNAde (56%) vs. RDesign (43%) — is comparably strong and should be the primary claim. The Rosetta comparison is still informative as a historical reference, but the current framing overstates its rigor.

### Minor

- **The zero-shot fitness study's "saturation mutagenesis" baseline is imprecisely characterized.** The paper labels baseline (2) as "random choice from all 449 single mutant sequences" and claims gRNAde "performs better than single site saturation mutagenesis, even when all single mutants are explored" (Figure 5 caption). However, the baseline simulates random draws from the single-mutant set (with 10,000 simulations) rather than the deterministic best among all single mutants tested exhaustively. At design budgets below 449, random draws underestimate what a true saturation experiment would discover. The core result (gRNAde's perplexity-based ranking beats random baselines) is unaffected, but the phrasing conflates random sampling with exhaustive testing. The authors should either recompute the deterministic saturation baseline or clarify the comparison.

- **Self-consistency metrics are described but only sequence recovery is prominently reported in the results section.** The paper describes secondary-structure (MCC via EternaFold) and tertiary-structure (scRMSD, scTM, GDT_TS via RhoFold) self-consistency as evaluation metrics (Section 2.3) and states they are computed (line 209), but the Results section primarily reports recovery. Reporting scRMSD or scTM for the single-state and multi-state benchmarks would strengthen the claim that designed sequences actually fold into the target structure.

- **No statistical significance testing across the 14-benchmark structures.** The paper reports standard deviations for gRNAde (across 3 seeds) but not for baselines. Paired tests or confidence intervals across the 14 RNAs would clarify whether improvements over RDesign and Rosetta are robust.

- **Multi-state test set composition not reported.** The multi-state split uses median intra-sequence RMSD for clustering, but the paper does not report how many test RNAs have 2, 3, 4, or 5+ available states. Since evaluation uses up to 5 states and the optimal is 3, knowing this distribution would help interpret the results.

### Trivial
None.

## Nice-to-Haves

- Comparison to other computational ranking methods (e.g., Rosetta energy, simple sequence-based baselines) in the fitness study would strengthen the claim that gRNAde's perplexity is a useful ranker beyond beating random selection.
- A discussion of whether ensembling a single-state model over states at inference time (a cheaper alternative) achieves similar gains to the multi-state model would be practically useful for users with limited GPU memory.
- Reporting the impact of the resolution mismatch (training data at ≤4.0Å, test ribozyme at 5.0Å) on perplexity reliability would add nuance to the fitness study.

## Removed Points

- **"The single-state benchmark is very small (14 structures)"** — The paper also evaluates on the 100-structure held-out test set from the clustering split. The 14-structure benchmark is a standard set from prior work (Das et al. 2010), and the paper presents both. This criticism is valid as a general concern but overly harsh given the supplementary evaluation.
- **"No comparison to any other computational ranking method (e.g., Rosetta energy)"** — Scope creep. The paper's claim is that gRNAde perplexity beats random baselines in a zero-shot setting, which it does. Adding other predictors is a nice-to-have, not a weakness.
- **"The multi-state model uses more GPU memory"** — The paper already reports this (line 316: 12GB/28GB/50GB for 1/3/5 states). This is an acknowledged practical tradeoff, not an oversight.
- **"Missing discussion of resolution cutoff (5.0Å for the ribozyme)"** — The paper explicitly notes this mismatch in a footnote (line 342). It is not missing.
- **"gRNAde is the first geometric deep learning architecture for multi-state biomolecule representation learning — check prior work"** — Speculative. There is no evidence of a prior claim to invalidate this.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the single-state benchmark to emphasize the gRNAde vs. RDesign comparison (the controlled contemporary baseline) and move the historical Rosetta/FARNA/ViennaRNA numbers to supplementary or present them with an explicit caveat about the uncontrolled comparison.
2. Recompute the fitness study's "single-site saturation" baseline as the deterministic best among all 449 single mutants at any budget ≥ 449, and clarify in the text that random draws underestimate this.
3. Report self-consistency (scRMSD, MCC) results for at least the single-state benchmark as a table in the main text.
4. Add the distribution of number of states per test RNA for the multi-state split (how many have 2, 3, 4, 5+ states?).
5. Add confidence intervals or paired significance tests for the 14-structure benchmark.

## Score and Decision

The paper makes a genuine contribution: a practical, fast, multi-state-capable RNA inverse design method with clear evidence of improvement over a contemporary deep learning baseline (RDesign). The multi-state analysis is the cleanest part of the paper. The evaluation has two notable weaknesses — the uncontrolled Rosetta comparison and the imprecise fitness baseline — but both are acknowledged (the Rosetta caveat) or fixable (the fitness baseline). Neither undermines the core contribution. The method is well-described and the code release would enable adoption. I recommend acceptance with revisions to address the above concerns.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>