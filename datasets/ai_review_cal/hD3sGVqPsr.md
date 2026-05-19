- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have verified all claims against the paper. Let me construct the final consolidated review.

## Summary

This paper introduces P²OT (Progressive Partial Optimal Transport), a framework for deep imbalanced clustering — the setting where underlying class distributions are long-tailed. The method formulates pseudo-label generation as an optimal transport problem that jointly enforces: (1) a KL divergence constraint on cluster size (enabling imbalanced pseudo-labels, unlike the equality constraints used in prior OT-based clustering), and (2) a progressive total mass constraint ρ that softly selects high-confidence samples without manual thresholding. The optimization is reformulated as an unbalanced OT problem with a virtual cluster, solved via an efficient scaling algorithm (2× faster than the generalized scaling algorithm). Results across five imbalanced benchmarks (CIFAR100-LT, ImageNet-R, iNature100/500/1000) show consistent improvements over existing methods, with gains concentrated on medium and tail classes.

## Strengths

1. **Well-motivated joint formulation addressing two key problems in one OT problem.** The P²OT objective (Eqs. 5–6) simultaneously handles class imbalance (via KL divergence on cluster marginal, replacing the equality constraint) and confident sample selection (via a total mass constraint ρ). The ablation study (Table 2) demonstrates that removing either component degrades performance substantially: the version without the KL constraint (POT) loses 5.8 ACC on CIFAR100-LT, and the version without progressive ρ (UOT) loses 2.3–5.4 ACC across datasets. This cleanly isolates the contribution of each component.

2. **State-of-the-art results on a challenging, newly constructed benchmark.** On five imbalanced datasets covering different scales, domains, and imbalance ratios, P²OT outperforms all baselines — e.g., +2.4 ACC on ImageNet-R, +5.9 ACC on iNature100, +3.4 ACC on iNature500 over prior best methods (Table 1). Gains are concentrated on medium and tail classes (Figure 1), directly supporting the imbalance-aware design.

3. **Efficient solver with theoretical grounding.** The reformulation of P²OT as an unbalanced OT problem with a virtual cluster (Eqs. 6–14) and the proof of equivalence (Propositions 1, 2) are technically sound. The resulting scaling algorithm runs 2× faster than the generalized scaling algorithm (Chizat et al., 2018), with time cost decreasing as ρ → 1 (Figure 5), giving a practical advantage.

4. **Transparent self-critique and honest analysis.** The paper explicitly acknowledges that its ρ ramp-up function "may not be optimal" and that "raising to 1 for ρ may not be necessary" (Section 5.3), and leaves adaptive ρ for future work. This candor strengthens rather than weakens the paper.

## Weaknesses

### Fatal
None.

### Major

1. **No direct comparison with the closest prior method (Zhang et al., 2023).** The paper correctly identifies Zhang et al. (2023) as the work that first relaxed the equality constraint to a KL divergence constraint on cluster size for imbalanced clustering — the same relaxation this paper builds on. However, there is no experiment comparing against this method. The UOT ablation (which removes progressive ρ from P²OT) *partially* addresses this, since UOT uses the same KL-constrained OT without progressive sample selection, and outperforming UOT (by 2.3–5.4 ACC) shows that the progressive component adds value. But the paper should either (a) explicitly note that UOT corresponds to the Zhang et al. approach and argue the comparison holds, or (b) run the actual Zhang et al. implementation. As written, the reader cannot rule out implementation-level differences.

2. **Ambiguous ACC metric definition.** The paper states it uses "clustering accuracy (ACC) metric averaged over classes" (Section 5.1). Standard deep clustering papers report overall ACC after Hungarian matching (a form of macro-over-samples). "Averaged over classes" suggests macro per-class accuracy (averaging per-class accuracies after matching), which is a different metric and can produce different rankings in imbalanced settings. The paper does not specify whether Hungarian matching is used, nor how ties or per-class computation works. This affects reproducibility and comparability with prior work. *(Note: This is a verifiable ambiguity — the paper's exact wording is "averaged over classes," which departs from convention without clarification.)*

### Minor

3. **Insufficient detail on the mini-batch implementation.** The paper mentions (line 172) a "mini-batch approach" that "stores historical predictions as a memory buffer to stabilize optimization," but provides no detail on buffer size, update mechanism (FIFO? aggregated statistics?), or how samples are weighted from the buffer. This makes the practical implementation of P²OT hard to reproduce.

4. **The claim of "first introduc[ing]" deep imbalanced clustering is slightly overstated.** The paper says "we first introduce a more practical problem setting named deep imbalanced clustering" (abstract) and "propose a practical deep imbalanced clustering problem" (Section 1). However, Zhang et al. (2023) already addresses imbalanced clustering with a KL-relaxed OT approach. The paper should qualify this as "formalize" or "establish a challenging benchmark for" rather than "first introduce."

5. **The progressive ρ schedule's benefit is not fully disentangled.** The paper acknowledges that weighted precision/recall plateau at ρ≈0.15, and that the ramp-up "may not be optimal." The ablation (Table 3) shows fixed ρ₀=0.1 underperforms the sigmoid schedule, but it does not test a *higher* fixed ρ (e.g., 0.5 or 0.8) that might match the sigmoid schedule's terminal value. If a fixed ρ=0.15 were competitive, the "progressive" aspect would be less central. This is already partially addressed by the paper's own transparent discussion, but the experimental isolation is incomplete.

6. **No standard deviations reported.** The paper runs each method three times but reports only the mean (Section 5.1). For modest margins (e.g., 0.9 ACC on CIFAR100-LT), standard deviations or significance information would be valuable.

### Trivial
- None.

## Nice-to-Haves
- A brief limitations paragraph (e.g., sensitivity to λ/ε, the assumption that K is known, reliance on DINO-pretrained backbones) would strengthen the paper.
- Reporting both macro per-class ACC and standard overall ACC (after Hungarian matching) would resolve the metric ambiguity and ensure backward comparability.
- Testing an adaptive ρ based on model confidence (e.g., entropy threshold) rather than iteration count would align better with the curriculum learning motivation the paper invokes.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing related works"**: The harsh critic did not raise this directly, but I note that no related-work claims were made by the reviewers that I could not verify. The related work section discusses relevant OT-based pseudo-labeling methods (Asano, Tai, Zhang) and deep clustering approaches adequately.

- **"Reproducibility concern about hyperparameters not being tuned per baseline"** (from harsh critic's notes): The paper states "All of these methods are trained using the same backbone, data augmentation, and training configurations to ensure a fair comparison" (Section 5.1). This is a reasonable approach for a fair comparison — tuning each baseline separately could introduce its own bias. Removed as a strawman.

- **"The progression of ρ is introduced on the basis of curriculum learning intuition, but the analysis suggests it may not be optimal or even necessary" — framed as fatal**: The paper transparently acknowledges this limitation itself, and the ablation (Table 3) confirms that dynamically increasing ρ outperforms fixed ρ=0.1. The critic's speculation about higher fixed ρ values (0.5, 1.0) is a reasonable suggestion but does not constitute a fatal flaw — it is a direction for further analysis, not evidence that the method is unsound. Demoted to Minor (see Weakness #5).

- **"NMI lower on iNature100"** (from harsh critic's Section-by-Section): The paper discusses this directly ("our method is an efficient one-stage approach, unlike SCAN*" and notes the NMI decrease of 1.5). The paper's explanation that NMI is not directly optimized is reasonable. This is a data point the paper already addresses.

- **Strength from Strength Finder about "robustness to hyperparameter choices"**: Table 3 does show robustness across different ρ₀ values (0.05–0.3), but the strength claim that "a dynamically increasing ρ is essential" is confirmed by the table. This strength is valid and retained (merged into Strength #4).

## Novel Insights

The reviews' main insight beyond the paper's own contributions is the observation that the paper's *transparency about its own limitations* (openly questioning the optimality of its ρ schedule, leaving advanced designs for future work) paradoxically strengthens its credibility. The harsh critic correctly identified that this transparency reveals an incomplete analysis, but the paper's honesty about this is a virtue, not a flaw. The merged picture is of a technically sound paper with well-delineated contributions, whose primary evidential gap is the missing direct comparison with Zhang et al. (2023) — partially filled by the UOT ablation but not fully resolved. The ACC metric ambiguity is a genuine but easily fixable issue.

## Suggestions

1. **Add a direct comparison to Zhang et al. (2023), or explicitly state that the UOT ablation is equivalent** to the KL-constrained OT from that work (since UOT removes the progressive ρ component, leaving only the KL constraint on cluster size — the core idea of Zhang et al.). If the latter, add a citation and brief justification.

2. **Clarify the ACC metric definition**: explicitly state whether Hungarian matching is used, and whether "averaged over classes" means macro averaging. Consider reporting both overall ACC and macro ACC for backward compatibility with prior literature.

3. **Provide mini-batch implementation details**: specify the memory buffer size, update rule, and how historical predictions are aggregated and weighted.

4. **Add standard deviations** to the main results table, especially for CIFAR100-LT where margins are small.

5. **Test a fixed ρ at the plateau value** (~0.15) to further substantiate the claim that progressive increase is essential, or soften the claim if results are competitive.
