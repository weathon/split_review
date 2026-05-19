- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have verified all claims against the paper. Let me write the consolidated review.

## Summary

This paper proposes FreeCG, a method for machine learning force fields that "frees" the design space of Clebsch-Gordan (CG) transforms from the constraint of permutation equivariance. The key idea is to construct permutation-invariant "abstract edges" via attention-based aggregation over neighboring edges, then perform CG transforms on these abstract edges—where invariance transitivity guarantees that any design of the CG layer preserves overall permutation equivariance. This freed design space enables three novel components: (1) group CG transform with sparse O(3) paths for efficiency, (2) abstract edges shuffling for cross-irrep information exchange, and (3) attention enhancer that feeds abstract edges back into the cross-attention mechanism. Experiments on MD17, rMD17, MD22, and QM9 show SOTA or competitive results, with several force prediction improvements >15% and up to >20%.

## Strengths

- **SOTA force prediction on MD17 (all 7 molecules) and near-SOTA on rMD17 force (7/10).** Table 1 shows FreeCG achieves the best force MAE across every MD17 molecule, with a 15.8% improvement on aspirin (0.122 vs. QuinNet's 0.145). Table 2 shows FreeCG best on 7/10 rMD17 force tasks. These results directly support the paper's core performance claims.

- **Clean conceptual contribution with a principled mathematical justification.** The paper identifies a genuine limitation in prior EGNNs (the narrow CG design space imposed by permutation equivariance, Problems 1 and 2 in Sec. 3.2) and provides a mathematically sound solution via invariance transitivity: if abstract edges are permutation-invariant (by construction, as sums over neighbors), then any CG transform applied to them inherits that invariance, freeing design choices like per-edge learnable weights, grouping, and shuffling that were previously impossible.

- **Well-designed ablation confirms each component contributes.** Table 5 shows incremental gains on aspirin force MAE: baseline ViSNet 0.155 → +group CG transform (32 groups) 0.129 → +shuffling 0.125 → +attention enhancer 0.122. Each step is cleanly isolated and quantified.

- **Efficiency benchmarking shows low overhead.** Figure 2 demonstrates FreeCG uses comparable memory and inference time to ViSNet (a non-CG baseline) and substantially less than NequIP and Allegro (both CG-based). The group CG transform with sparse path achieves O(3) equivariance with low computational cost.

- **Strong results on MD22 and real-world MD simulations.** FreeCG leads on 4/7 MD22 force tracks with >20% improvement on Ac-Ala3-NHMe (both energy and force), and demonstrates practical MD simulations on periodic systems (water, LiPS) and the mini-protein Chignolin.

## Weaknesses

### Fatal
None.

### Major

- **Catastrophic failure on MD22 Stachyose force prediction is not discussed.** Table 3 shows FreeCG achieves 0.612 MAE on Stachyose force, while QuinNet achieves 0.0543—a factor of ~11× worse. This is an order-of-magnitude degradation on a large-molecule benchmark. The paper states FreeCG "leads in most tracks" (technically true: 4/7 force tracks) but provides zero analysis or even acknowledgment of this dramatic failure. Without understanding why FreeCG catastrophically fails on this particular system, readers cannot assess the method's reliability or generality. This is a significant evidential gap in an otherwise strong empirical evaluation.

### Minor

- **Large negative outliers on QM9 (μ, ⟨R²⟩) are not acknowledged or discussed.** FreeCG is best on 8/12 QM9 properties, but scores 11.4 on dipole moment μ (vs. ViSNet 9.5, ~20% worse) and 82.1 on ⟨R²⟩ (vs. ViSNet 29.8, 2.8× worse). The paper says FreeCG "performs the best for most properties," which is accurate, but the magnitude of these gaps—especially the 2.8× regression on ⟨R²⟩—deserves a candid discussion to help readers calibrate where the method excels versus struggles.

- **Sparse path claim is not ablated against a full O(3) path set.** The paper proposes keeping only irrep types (l=1,p=-1) and (l=2,p=1) as a more efficient alternative to maintaining both parity values per l. However, no ablation compares this sparse path set against a full O(3) irrep set with the same architecture and training budget. Without this, it is unclear whether the sparse path trades expressivity for efficiency. An ablation would directly confirm the claim that the restricted set is sufficient.

- **QuinNet extension lacks final benchmark numbers.** Section 4.5 shows only training curves over 1000 epochs for QuinNet+FreeCG, without reporting final test MAE on standard benchmarks (MD17, MD22). While the convergence improvement trend is promising, the "new paradigm" claim would be substantially stronger with a quantitative comparison on the same benchmarks reported in Tables 1–4.

- **Attention enhancer design choice (max pooling) is not justified or ablated.** Equation 7 uses max over abstract edges for the attention enhancement term. No justification or ablation is provided for this choice over alternatives (sum, mean, learned attention pooling). Given that this component contributes to the final improvement (Table 5: 0.125 → 0.122), its design rationale should be clarified.

### Trivial

- **Redundant path in sparse path enumeration.** The sparse path description in Section 3.3 lists "(l=1, p=-1)*(l=1,p=-1)→(l=2,p=1)" twice (the 2nd and 4th listed paths). The 4th path should presumably be the symmetric case "(l=2,p=1)*(l=1,p=-1)→(l=1,p=-1)."

- **"1.5*T/G" shuffling constant is heuristic without explanation.** The value 1.5 for the shuffling stride is validated by ablation (Table 5 shows it works best), but no intuition is offered for why 1.5× the group size is the right scale.

## Nice-to-Haves

- An ablation varying the number of abstract edges T, to characterize the complexity-expressivity trade-off of this key hyperparameter.
- A brief analysis of why Stachyose force is so challenging for FreeCG—e.g., is it the molecular size, the topology, or a hyperparameter sensitivity issue?
- A comparison of FreeCG against the newer EquiformerV2 architecture.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Theoretical argument for free design has unaddressed subtlety about learned features not being perfectly invariant."** Removed because the reviewer misunderstands permutation invariance. The abstract edges are computed as a sum (or attention-weighted sum) over neighbors—this operation is structurally permutation invariant regardless of whether the attention weights are learned. The invariance is a property of the aggregation operation, not an empirical property of the learned values. This is standard and well-understood.

2. **"The paper claims SOTA uniformly across all datasets."** Removed because the paper is more precise: the abstract says "SOTA results in force prediction for MD17, rMD17, MD22" and "well extended to property prediction in QM9." The word "SOTA" is only applied to force prediction on those three datasets. The conclusion does say "SOTA... in molecular properties prediction for QM9," which is defensible as FreeCG wins 8/12 properties.

3. **"Missing training details (hyperparameters, cutoff radius, etc.)."** Removed because these are standardly deferred to the appendix, which is stripped by the parser. This is a known artifact of the review process, not an author error.

4. **"Missing ablation of number of abstract edges T."** Moved to Nice-to-Haves—it would strengthen the paper but its absence is not a flaw in the presented evaluation.

5. **"Missing related works (EquiformerV2)."** Removed per instructions: I do not have external sources to confirm existence and should not mention missing related works.

6. **"rMD17 energy results are weaker, not discussed."** Removed because the paper's core claims are about force prediction, not energy. The paper says "The force prediction accuracy of FreeCG is still leading in majority of the molecules" (referring to force), which is accurate. Energy is not the focus.

7. **"Malondialdehyde energy is worst in MD17."** Removed because the paper only claims "competitive" energy results, and FreeCG wins 4/7 MD17 energy tracks—"competitive" is accurate.

## Novel Insights

The most interesting point emerging from cross-referencing the reviews is the tension between the paper's clean theoretical framing (invariance transitivity) and its messy empirical profile (SOTA on most tasks, catastrophic on one). The Stachyose result is not just a random fluctuation—it is an order-of-magnitude failure on a large molecule. This pattern (excellent on small-to-medium molecules, failing on the largest one in MD22) suggests the sparse path may lose information needed for certain molecular environments, or the group CG transform's grouping strategy may interact poorly with specific molecular topologies. The paper's own claim that it "performs well for large scale data" is directly contradicted by this one result. This is precisely the kind of insight that would be addressed by an honest failure analysis, which the paper sadly lacks. The core method is likely sound, but its boundary conditions remain unexplored.

## Suggestions

- Add a frank discussion section analyzing the Stachyose failure and the QM9 μ/⟨R²⟩ gaps. Hypothesize causes (e.g., is the sparse path insufficient for certain interaction environments? does the group structure limit cross-irrep communication for large molecules?) and suggest mitigation strategies.
- Include an ablation comparing the sparse O(3) path set against a full O(3) irrep set (with both parities for both l=1 and l=2) to verify no expressivity loss, as this directly supports the paper's core efficiency claim.
- For the QuinNet extension, report final test MAE on MD17 or rMD22 after convergence, not just training curves.
- Clarify the basis for the "4 vs. 8" path comparison with SO(3) and fix the redundant path listing.
