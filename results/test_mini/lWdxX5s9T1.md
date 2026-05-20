Now I have all the evidence needed to write the final consolidated review.

## Summary

This paper introduces RADAR, a neural framework for solving asymmetric Vehicle Routing Problems (VRPs). RADAR addresses asymmetry through two clean components: (1) an SVD-based initialization that encodes static asymmetry from the distance matrix into compact node embeddings, and (2) a replacement of softmax with Sinkhorn normalization in the attention mechanism to model dynamic asymmetry during encoder propagation. The method is architecture-agnostic and can augment existing neural VRP solvers. Experiments across 17 synthetic and 3 real-world VRP variants show consistent improvements over strong neural baselines, with strong out-of-distribution generalization from size-100 training to size-1000 testing.

## Strengths

- **Principled, theoretically grounded initialization for asymmetric inputs.** The paper formalizes an "asymmetry-aware embedding" condition (Definition 1) and proves that the proposed SVD-based construction (Eq. 2–5) provably satisfies it. Ablation Table 6 confirms this is not just theoretical: removing SVD increases the gap from 0.72% to 2.08% on ATSP100 and from 1.01% to 5.23% on ATSP200. The SVD approach is a novel application of a classical decomposition to a practical NCO bottleneck.

- **Sinkhorn normalization is a simple yet effective fix for a genuine limitation of softmax in asymmetric settings.** The paper correctly diagnoses that row-wise softmax ignores the neighborhood structure of the attended-to node \(j\). Replacing it with Sinkhorn normalization (Algorithm 2) consistently improves performance across all sizes in Table 6 (e.g., from 1.19% to 0.72% on ATSP100 when combined with SVD). This is not a generic tweak—it directly targets the "dynamic asymmetry" problem the paper identifies.

- **Broad and convincing evaluation across diverse settings.** The paper covers synthetic single-task (ATSP, ACVRP at 4 scales), a multi-task setting with 16 asymmetric VRP variants, and 3 real-world datasets (ATSP, ACVRP, ACVRPTW with in/out-of-distribution splits). RADAR achieves the best results among neural methods in nearly every setting, and on ACVRP200 it even surpasses LKH. The out-of-distribution generalization (training on N=100, testing up to N=1000) is particularly informative and shows RADAR degrades far less than baselines.

- **Well-executed ablation and design analysis.** Section 6 systematically ablates each component (Table 6), compares against alternative initialization methods (Figure 2, Table 10 in appendix), analyzes sensitivity to SVD rank \(k\) (Figure 3), and examines Sinkhorn iterations (Appendix D.7). These studies provide concrete evidence for each design choice.

- **Insightful analysis of the role of coordinates under asymmetry.** Section 5.4 shows that RADAR without coordinates (cost 38.958) outperforms RRNCO with coordinates + augmentation (cost 39.077) on real-world ATSP. This demonstrates that SVD-based distance embeddings capture structural information effectively without positional cues, and that coordinates mainly enable data augmentation diversity rather than encoding structure.

## Weaknesses

### Fatal
None.

### Major

- **No statistical significance or variance reporting in any experiment.** Tables 1–6 report single point estimates with no confidence intervals, standard deviations, or significance tests, despite testing on only 1,000 instances per setting. This is a significant evidential gap: on ATSP100, RADAR's gap (0.72%) is close to ReLD (1.64%) and MatNet-Single (Random) (2.08%). Without error bars, it is impossible to assess whether the reported improvements are reliably reproducible or within noise. While single-run evaluation is common in the NCO literature, the margins are small enough in several comparisons that this omission weakens the headline claim of "consistently outperforming" baselines.

### Minor

- **Baseline training details are insufficiently specified.** The paper states that baselines (MatNet, ICAM, ELG, ReLD) were "retrained under our setup" and that "mixed-size training is disabled for both ICAM and UDC" for fairness, but does not specify whether RADAR and all baselines share the same training epochs, learning rate schedules, batch sizes, or early stopping criteria. Given that ICAM's original work reports stronger performance with mixed-size training (which was disabled) and that MatNet's original 2100-epoch training yields different gaps, the reported baseline results may not reflect their best achievable performance. This does not invalidate the comparison but makes its fairness harder to fully assess.

- **The synthetic asymmetry generation (Section 5.5) uses multiplicative Gaussian noise on Euclidean distances, which does not preserve the triangle inequality and may not mirror real-world asymmetry patterns.** The paper acknowledges that real-world matrices "often violate geometric assumptions such as the triangle inequality" (line 262), which mitigates this concern somewhat, but the connection between the synthetic noise model and naturally occurring asymmetry is not discussed.

### Trivial

- On ATSP1000, RADAR's gap is 4.13% compared to 0.72% on ATSP100. While this still far outperforms baselines (ELG: 10.74%, ReLD: 13.39%), the near-doubling of the gap from ATSP500 (2.13%) to ATSP1000 (4.13%) warrants a brief comment in the main text.

## Nice-to-Haves

- An analysis of whether Sinkhorn normalization ever hurts (e.g., under extreme column-skewed cost structures or severe triangle inequality violations). The ablation shows it helps empirically, but a discussion of failure modes would strengthen the paper.
- A comparison of Sinkhorn against alternative normalizations (e.g., column-wise softmax, or a learnable convex combination of row and column normalization).
- Testing on higher asymmetry levels (\(\sigma = 0.5\)) to see if RADAR's advantage holds and whether SVD reconstruction degrades.
- Since the paper fixes SVD rank \(k=10\) based on N=100 data, a brief analysis of whether increasing \(k\) for larger test instances improves generalization would be useful.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Multi-task results aggregated; per-variant not reported in main paper."** — REMOVED. The paper explicitly cites "See Table 8" in the appendix. Deferring per-variant breakdowns to the appendix is standard practice for a 9-page paper covering 16 variants.

2. **"Definition 1 is formally weak; tautological."** — REMOVED. The definition serves as a design goal that the SVD construction provably satisfies (Eq. 4–5). The reviewer misinterprets it as a theoretical guarantee rather than a formalization of the design objective.

3. **"Section 5.6 results missing from main text; Table 9 cited but absent."** — REMOVED. The appendix (containing Table 9) was stripped by the parser. The results exist in the original submission.

4. **"Alternative SVD methods not described; Table 10 cited but not present."** — REMOVED. Details are in the appendix, which was stripped. The main paper summarizes the key comparisons (Figure 2).

5. **"RRNCO not retrained under identical conditions."** — REMOVED. The paper explicitly states "we directly reuse the GCN and MatNet results reported in their paper," transparently disclosing the comparison protocol.

6. **"Generalization degrades at larger sizes (4.13% at 1000)."** — REMOVED. The paper reports these numbers transparently. RADAR still dramatically outperforms all baselines at all sizes; the observation is a factual description, not a weakness.

7. **"Sinkhorn's doubly stochasticity may not always be appropriate."** — MOVED to Nice-to-Haves. This is a valid design question but the paper provides empirical evidence that it helps; exploring failure cases would strengthen but is not a current flaw.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from the reviewer cross-analysis is how the paper cleanly decomposes a messy real-world problem (encoding asymmetric distance matrices) into two crisply defined subproblems: static asymmetry handled at initialization via SVD, and dynamic asymmetry handled during encoder propagation via Sinkhorn normalization. This decomposition is itself a conceptual contribution that future work on asymmetric NCO can build on. The finding in Section 5.4 that SVD-based distance embeddings can effectively substitute for coordinate information is also noteworthy—it suggests that for asymmetric problems, learned embeddings from a spectral decomposition of the cost matrix carry more structural signal than geometric coordinates.

## Suggestions

- Add standard deviations or bootstrapped 95% confidence intervals to the main results (Tables 1, 3, 5–6). This is the single highest-impact improvement the paper could make.
- Provide a table comparing training configurations (epochs, learning rate, batch size, optimizer, schedule) across all retrained baselines to demonstrate fair comparison.
- Include a brief discussion in Section 5.1 explicitly noting that while RADAR's gap increases from 0.72% (N=100) to 4.13% (N=1000), it still dramatically outperforms the next-best neural baseline at each scale.
- Add a sentence clarifying whether the synthetic asymmetry model (multiplicative Gaussian noise) preserves or violates the triangle inequality, and how this compares to patterns observed in real asymmetric distance matrices.

## Score and Decision

### Calibration Anchors (retrieved from human-review corpus)

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| RRNCO (sKvo9ZZfpe.md) — Asymmetric VRP solver with dataset | 5.50 | Similar topic and approach. RRNCO contributed a new dataset; RADAR contributes more novel methodology (SVD + Sinkhorn). RADAR's ablations are cleaner, but both lack statistical rigor. Comparable quality. |
| CaR — Constraint handling (raDFGuQxvD.md) | 6.00 | Both have strong empirical evaluation and clean ablations. CaR's problem is narrower; RADAR covers more variants. RADAR's methodological novelty is higher. Marginally weaker on reporting rigor. |
| URS — Unified routing solver (EiEbn6FZsK.md) | 4.50 | RADAR is clearly stronger: more principled components (SVD, Sinkhorn) versus URS's LLM-driven masking which reviewers found questionable. RADAR's novelty is higher. |
| HADES — Hierarchical improvement (NLgJcADMtr.md) | 4.00 | RADAR's reported improvements are larger and more consistent than HADES's marginal gains. RADAR's ablations more clearly attribute gains to specific components. Stronger paper overall. |
| Distance Metric Generalization (R6np5nEhJo.md) | 2.50 | RADAR is much stronger: genuine methodological contribution versus simple multi-task training. Not comparable in novelty or impact. |
| Symmetric Sinkhorn Diffusion (BCir2oVTVj.md) | 5.50 | Different domain but uses similar Sinkhorn tool. RADAR's application domain (VRP) is more concretely evaluated. Comparable quality. |

**Score reasoning**: RADAR sits in the 5.5–6.0 range. Its main weaknesses (lack of variance reporting, partially opaque baseline training details) are issues of reporting rigor rather than fundamental flaws. The methodological contributions (SVD-based initialization and Sinkhorn normalization for asymmetric VRPs) are novel, principled, and well-supported by ablation. The evaluation is broad and convincing. The paper is comparable in quality to RRNCO (accepted at 5.50) and CaR (accepted at 6.00), and clearly stronger than URS (4.50, rejected) and HADES (4.00, rejected).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>