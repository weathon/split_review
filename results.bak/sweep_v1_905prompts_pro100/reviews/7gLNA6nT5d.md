Now I have a complete calibration picture. Let me write the final review.

**Round 1 bracket**: Between 5.0 and 6.5, based on comparison with `b5MCteb3w7` (4.75, ICRL paper with metric/baseline issues — clearly weaker) and `STUGfUz8ob` (7.60, strong theory+empirical paper — clearly stronger). Both `5iWim8KqBR` (5.50, AD extension with limited novelty) and `iLUcsecZJp` (5.75, borderline accept with theory but synthetic-only experiments) sit inside this bracket.

**Round 2 narrowing**: The paper under review has cleaner empirical grounding than `iLUcsecZJp` (5.75 Accept — theory-heavy, synthetic-only, borderline) but lacks theoretical contribution. It has more diverse environments than `Pj06mxCXPl` (6.67 Accept — theory + simple experiments) but no theoretical analysis and has underspecification issues that `Pj06mxCXPl` does not. The paper is most comparable to `5iWim8KqBR` (5.50 Reject — also an AD extension) but has more novelty (first application of n-gram induction to ICRL vs. replacing AD's transformer with an existing efficient variant). Final placement: **5.5**, between `5iWim8KqBR` (5.50) and `iLUcsecZJp` (5.75), with the underspecification issues as the key differentiator preventing a higher score.

---

## Summary

This paper proposes integrating pre-built n-gram induction heads into transformer-based in-context reinforcement learning, building on Algorithm Distillation (AD). The central claim is that n-gram attention patterns reduce data requirements, decrease hyperparameter sensitivity, and can be adapted to image-based environments via vector quantization (VQ). The paper provides experimental evidence on Dark Room, Key-to-Door (discrete grid-worlds), and Miniworld (3D image-based) environments.

## Strengths

- **Novel and well-motivated architecture modification.** Applying n-gram induction heads — previously studied in language modeling — to in-context RL is a genuinely new combination. The motivation (addressing transformers' simplicity bias toward unigrams, reducing data needs via explicit pattern matching) is clearly articulated and builds on established findings from Edelman et al. and Akyürek et al.

- **Clean, convincing results on discrete environments.** The Dark Room experiments (Figure 2) clearly show the n-gram model reaching optimal EMP in far fewer hyperparameter assignments (~20 vs. >400 for 1K histories). The Key-to-Door experiments (Figure 4) demonstrate that with only 100 training goals — a low-diversity regime — the n-gram method reaches near-optimal return (~1.9) while the baseline plateaus at ~1.3. These results directly support the paper's core claims about data efficiency and reduced hyperparameter sensitivity.

- **Proper evaluation protocol.** Using Expected Maximum Performance (EMP) over random hyperparameter searches, with fixed training steps and equal batch sizes, avoids cherry-picking and provides a fair comparison of both final performance and training stability. This is a well-considered choice for demonstrating hyperparameter sensitivity.

- **Successful extension to image-based environments via VQ.** The adaptation of n-gram matching to pixel observations using a pretrained VQ auto-encoder (Section 2.3) is technically sound and enables the method to handle visual inputs without manual state abstraction. The Miniworld results (Figure 5) show consistent performance gains over the baseline.

## Weaknesses

### Major

- **Underspecified ablation and robustness experiments (Sections 4.4, 4.5).** Table 1(a)-(c) reports EMP values for n-gram length ablation, layer position ablation, and the permuted-mask control, but does not specify the data regime: number of training goals, number of learning histories, or training budget. Without this information, the reader cannot reconcile the reported EMP values (0.51–0.76) with the main Miniworld-Dark results in Figure 5 (where N-Gram reaches ~0.95 EMP with 30 goals and 50 histories). The claim that n-gram length and position are insensitive to hyperparameter search (Section 4.4) and that a broken n-gram mask does not hurt performance (Section 4.5) cannot be properly evaluated without knowing the experimental conditions under which these numbers were obtained. This is addressable — the missing details can be provided in a rebuttal — but as presented, two full subsections of results are not interpretable.

### Minor

- **Ambiguity about baseline input representation in image experiments.** Section 2.3 states that "we train both causal and n-gram attention layers simultaneously" using VQ, which implies the baseline (causal attention only) also receives VQ-encoded latent vectors. However, the paper never explicitly confirms that the baseline transformer uses the same VQ-derived representations rather than, say, raw pixels or a separate CNN embedding. While the simultaneous-training description strongly suggests both use the same VQ pipeline, an explicit statement would eliminate ambiguity about whether the observed gains are from n-gram attention or from a better input representation.

- **The "27× less data" headline number is unverifiable.** The computation is deferred to Appendix B, which is not available in the submission. The data efficiency benefit is already clearly demonstrated in Figure 4 without the multiplier, and the claim references AD's published configuration (2048 goals × 2048 histories). While the underlying result is solid, the specific multiplier cannot be checked and does not add independent evidential weight beyond what the controlled experiments already show.

### Trivial

- **Figure 1 (introduction) does not label which environment it corresponds to.** The figure previews the data-efficiency result but the reader must infer from Section 4 that it depicts the Dark Room environment. Minor presentation issue.

- **Section 4.3 states the Miniworld-Dark hyperparameter sensitivity result is "omitted for brevity" while Figure 6 (left) shows it.** This is a small inconsistency in the narrative.

## Nice-to-Haves

- An analysis of the frequency and nature of n-gram matches in learned sequences (e.g., what patterns are being matched, how often) would strengthen the mechanistic intuition connecting n-gram attention to improved ICRL performance.

- Confidence intervals or error bands on the EMP curves, particularly for the small-data experiments where variance may be high.

- Testing on more complex environments (e.g., Meta-World, XLand-Minigrid) would broaden the evidence base — the authors acknowledge this as future work.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic claimed the VQ confound "invalidates one of the three main contributions."** REMOVED as overstated. The paper says "train both causal and n-gram attention layers simultaneously" using the VQ model, which implies the baseline receives the same VQ representations. The ambiguity is real but the paper does not provide evidence of a confound — the critic assumes one. Kept as a Minor clarity issue above.

- **Harsh Critic claimed the EMP gap means "the whole system [is] performing badly under those conditions" and "erodes confidence in the entire experimental narrative."** REMOVED as speculative. The conditions for Table 1 are unknown — the problem is underspecification, not proven invalidity. The critic's interpretation that the system is failing is one possibility among many; the actual weakness is the missing information.

- **Harsh Critic requested hyperparameter ranges and search budgets in the main text.** REMOVED. Deferring these to Appendix C is standard practice.

- **Harsh Critic questioned whether n-gram matching is applied causally and whether the residual stream obscures contributions.** REMOVED. The n-gram formula inherently references past tokens, and the residual connection is standard transformer architecture — neither is a genuine concern.

- **Strength Finder claimed "fair and thorough evaluation protocol" as an independent strength.** KEPT but merged into the evaluation protocol strength above.

- **Strength Finder called the VQ-based matching "technically sound" for the image extension.** KEPT as part of the third strength.

## Novel Insights

The key insight from this review process is that n-gram induction heads appear to help most dramatically when task diversity is low — the Key-to-Door experiment with only 100 goals (Figure 4) is the paper's strongest result, and it directly addresses a practical data regime (many trajectories, few tasks) that the original AD work did not test. This connection between n-gram attention and low-diversity generalization is worth highlighting: explicit pattern matching may compensate for the statistical weakness that comes from limited task variety, whereas standard causal attention requires sufficient task diversity for in-context abilities to emerge.

## Suggestions

- **Specify the data conditions for all ablation/robustness experiments (Table 1).** Report number of training goals, learning histories, and gradient steps used. This is the single most important fix.

- **Add one sentence in Section 2.3 explicitly confirming that the baseline transformer receives the same VQ-encoded latent vectors as the N-Gram model.** This eliminates any ambiguity about input representations.

- **Include the 27× computation (currently in Appendix B) in the main text or at minimum ensure it is available to reviewers.** If the appendix cannot be restored, briefly state the formula: e.g., "AD uses 2048 goals × 2048 histories, our method achieves comparable performance with 100 goals × N histories; 27× = (2048×2048)/(100×N)."

- **Label Figure 1 with the environment name** (Dark Room) so the introduction preview is self-contained.

---

**Calibration anchors referenced across all rounds:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| 5iWim8KqBR | 5.50 | R1+R2 | Similar domain (AD extension); our paper has more novelty but similar scope |
| b5MCteb3w7 | 4.75 | R1+R2 | ICRL paper with metric/baseline issues; our paper is clearly stronger |
| iLUcsecZJp | 5.75 | R2 | Borderline Accept with theory+synthetic; our paper is empirically stronger but lacks theory |
| Pj06mxCXPl | 6.67 | R2 | Strong theory+empirical; our paper is clearly weaker (no theory, underspecification issues) |
| STUGfUz8ob | 7.60 | R1 | Strong theory+empirical with architecture insights; our paper is substantially weaker |
| 0spR7wDwBh | 6.00 | R2 | Grid-world agent paper; comparable empirical scope |
| 2PKLRmU7ne | 5.60 | R1 | Theory paper on ICL+Occam; different focus, similar score range |
| 9ngFxN83j2 | 5.75 | R2 | Theory on attention token selection; different focus |

Round 1 bracket: 5.0–6.5. Round 2 narrowed to 5.5 by comparison with 5iWim8KqBR (5.50, our paper more novel), iLUcsecZJp (5.75, our paper empirically stronger but lacks theory and has underspecification issues), and Pj06mxCXPl (6.67, our paper clearly weaker).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>