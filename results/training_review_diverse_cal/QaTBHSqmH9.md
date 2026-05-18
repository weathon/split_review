Here is my consolidated review.

---

## Summary

This paper proposes EquiRNA, a hierarchical equivariant GNN for RNA 3D structure evaluation. The model decomposes RNA into three levels (atom, subunit, nucleotide) and performs E(3)-equivariant message passing at each level, reusing nucleotide representations across RNAs of different sizes to address what the paper calls "size generalization." The authors also introduce rRNAsolo, a new dataset of 200/15/15 RNAs (80k/6k/6k candidate structures) spanning 50–200 nucleotides, which is larger and covers a wider size range than the existing ARES dataset. EquiRNA achieves consistent SOTA results on both rRNAsolo (e.g., Mean RMSD 5.79 vs. next best 7.79 on validation) and ARES across multiple metrics.

---

## Strengths

- **Consistent and substantial SOTA performance across two datasets and multiple metrics.** EquiRNA outperforms all six baselines (PaxNet, ARES, EGNN, dyMEAN, GET, RDesign) on Mean RMSD, Median RMSD, and Relative Error metrics on both rRNAsolo (Table 1) and ARES (Table 2), and also achieves the best Relative Ranking (Table 3). The improvement on rRNAsolo is notably large (e.g., ~2.0 drop in Mean RMSD over the next best method), which is credible evidence that the hierarchical design captures useful structural information.

- **rRNAsolo dataset is a genuine resource for the community.** The dataset is ~7× larger than ARES, spans a wider size range (50–200 nt vs. <50 nt for ARES training), uses more recent data, and implements careful purification at atomic and nucleotide levels (valence checks, continuity checks, removal of non-canonical pairs, etc.). It fills a gap in benchmarking RNA structure evaluation methods on larger RNAs.

- **Ablation studies systematically isolate each component's contribution.** Table 4 removes atom-level, subunit-level, nucleotide-level modules, the KNN sampling strategy, and equivariance one at a time, and each ablation degrades performance. This provides evidence that the full architecture, not just one component, drives the gains.

- **The hierarchical design is well-motivated biologically.** The paper builds on the valid insight that nucleotides are reusable building blocks across RNAs of varying sizes, and the three-level architecture (atom → subunit → nucleotide) follows the natural compositional structure of RNA.

---

## Weaknesses

### Major

- **The "size generalization" claim is broader than the experimental evidence supports.** The paper tests only one training/test size split (train on 50–100 nt, test on 100–200 nt). While this demonstrates generalization within this specific range, the paper's framing (e.g., "effectively addresses the size generalization challenge" in the abstract) implies a more general capability. The paper does not test (a) train on 50–100, test on >200; (b) train on 100–200, test on <50; or (c) train on 50–100, test on 100–200 with a finer-grained analysis of how performance degrades as the size gap widens. Without these, it is unclear whether the method generalizes to size shifts in general or works specifically within the 50→200 nt range. Figure 5 helps by showing per-interval results (100–110, 110–120, 120–150, 150–200), but all these intervals are within the held-out test range, not beyond it.

- **Baselines are evaluated with default configurations rather than tuned on the target task.** The paper states that all baselines use "default configurations in the corresponding source codes" (Section 4). This risks inflating EquiRNA's relative gains because default hyperparameters are typically tuned to the original authors' tasks and datasets (which involve smaller RNAs). A fairer comparison would involve at least a basic hyperparameter search for each baseline on the rRNAsolo validation set. Since the reported improvements (e.g., 2.00 RMSD) are substantial, it is important to verify they are not partly artifacts of suboptimal baselines.

### Minor

- **Efficiency claims are qualitative and unsupported.** The paper states that EquiRNA "costs much less inference time than ARES" and is "even faster than EGNN" but provides no runtime measurements, FLOP counts, or memory usage numbers. This claim cannot be evaluated and should either be removed or substantiated with empirical measurements.

- **Ablation study does not include Relative Ranking metric.** Relative Ranking (Table 3) is introduced as a more intuitive metric given the high absolute RMSD values, but it is not reported in the ablation study (Table 4). Including it would help attribute which components contribute to ranking quality vs. absolute scoring accuracy.

- **The "full-atom" phrasing is slightly imprecise.** The paper states it "preserves full-atom information" (line 28) but then clarifies that hydrogen atoms are excluded following ARES (line 45). While this is transparently stated, the term "full-atom" could mislead readers who interpret it as including all atoms including hydrogens. A more precise term like "all-heavy-atom" or "full heavy-atom" would be clearer.

- **The architectural novelty is moderate.** The three-level hierarchy is a sensible design, but hierarchical GNNs for molecular systems are established (ProNet and others are cited), and the EGNN backbone is a published method. The paper's primary distinction—applying this combination to RNA structure evaluation with full-atom preservation across levels—is valuable but incremental rather than architecturally novel. This is not a flaw per se, but the framing as "novel" should be calibrated accordingly.

### Trivial

- None that survive filtering.

---

## Nice-to-Haves

- Add experiments with additional size shifts (e.g., train on 50–100, test on >200; train on 100–200, test on <50) to substantiate the "size generalization" claim beyond the current single split.
- Tune each baseline on the rRNAsolo validation set (or at minimum, report sensitivity to hyperparameters) to rule out the concern that default configurations disadvantage baselines.
- Report actual runtime and memory measurements for EquiRNA vs. baselines to back up the efficiency claim.
- State explicitly whether the rRNAsolo dataset (candidate structures, splits, and metadata) and EquiRNA code will be released to enable reproducibility.
- Include the Relative Ranking metric in the ablation study.
- Provide a more precise definition of "size generalization" (e.g., the specific distribution shift, the range of extrapolation considered).

---

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the meta-review guidelines:

1. **"Full-atom is misleading" overly harsh characterization.** The paper clarifies on the same line (line 45) that it excludes hydrogen following ARES. The terminology is slightly imprecise but the paper is transparent. Moved to Minor.
2. **"The paper does not address potential biases in rRNAsolo" / "method is evaluated primarily on it."** The paper evaluates on *both* rRNAsolo and ARES, so the claim of "primarily" on rRNAsolo is inaccurate. The cluster-based split also controls for topology leakage. Kept only as a suggestion about additional ablations.
3. **Missing appendix content criticism.** Per the meta-review guidelines, the parser strips appendix sections; these exist in the original submission. Removed.
4. **Criticism of KNN sampling as "not a new idea."** The combination with hierarchical design is what matters; individual components being established is not a weakness. Removed as a strawman.
5. **"Individual contributions of atom-level and subunit-level modules are small (0.09–0.16)."** This is a reasonable observation but I cannot independently verify the exact numbers from the image-only table. The paper's own text states these removals decrease performance; the magnitude is a secondary point. If accurate, this is a minor observation, not a structural flaw.

---

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface any genuinely novel insight that the paper's authors have missed. The main critical observation—that size generalization evidence is limited to one split—is a standard experimental design concern rather than a novel scientific insight.

---

## Suggestions

1. **Tone down the "size generalization" claim** to match the experimental scope. The paper currently claims to "effectively address the size generalization challenge" based on a single 50→200 nt shift. Rephrase to something like "demonstrate improved generalization across a 2× size increase from training (50–100 nt) to test (100–200 nt)" and discuss the limits of this evidence.

2. **Tune baselines or justify default configurations.** Even a small hyperparameter sweep (e.g., learning rate, number of layers) for each baseline on the rRNAsolo validation set would substantially strengthen the comparative claims.

3. **Add runtime numbers.** Provide wall-clock inference time per candidate structure and peak GPU memory for EquiRNA vs. at least ARES and EGNN on a representative RNA size (e.g., 150 nt).

4. **Explicitly state release plans** for the rRNAsolo dataset and EquiRNA code in the final version. This is important for reproducibility and community impact.

---

## Score and Decision

The paper presents a well-motivated method with strong empirical results on a practically important problem. The hierarchical equivariant architecture is sensible, the new dataset is a useful contribution, and the ablation study is thorough. However, the central "size generalization" claim is over-extrapolated from a single experimental split, and the baselines may be disadvantaged by using default configurations. These issues are addressable in a revision but weaken the paper in its current form. The paper's contributions are real and the results are convincing on their own terms, but the framing overstates the evidence.

**Score: 6.0 / 10** — Borderline accept. The core technical contribution is solid, but the paper would benefit from toning down the size generalization claim and adding rigorous baseline tuning before it is ready for a top-tier venue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>