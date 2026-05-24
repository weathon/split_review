Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

**Round-1 Bracket:** Based on initial calibration, the paper is clearly above the weak band (1.5–3.0), comfortably above the mid-range band (4.4–6.0), and below the strongest band (7.6–10.0). Initial bracket: 6–8.

**Round-2 Narrowing:** Reading anchors in the 5.5–7.5 range: WithAnyone is stronger than UIFace (6.00), Vec2Face (6.00), DreamBench++ (6.00), ClassDiffusion (6.25), and InstantPortrait (6.67) — all of which have weaker evaluation, narrower scope, or more significant methodological concerns. WithAnyone falls below RB-Modulation (8.00), which has a novel theoretical framework (optimal control). Final score: 7.0.

---

## Summary

This paper identifies, formalizes, and mitigates a failure mode in identity-consistent image generation called "copy-paste artifacts" — where models directly replicate the reference face rather than generating natural variations in pose, expression, or lighting. Three contributions are made: (1) **MultiID-2M**, a large-scale dataset of 500K paired multi-ID images and 1.5M unpaired group photos; (2) **MultiID-Bench**, a benchmark with a Copy-Paste metric (ℳ_CP) that quantifies the trade-off between identity fidelity and over-copying; and (3) **WithAnyone**, a training pipeline on FLUX that combines a GT-aligned ID loss, an ID contrastive loss with extended negatives, and a four-phase training schedule. Experiments across 14 baselines show that WithAnyone achieves the best or near-best identity similarity (Sim(GT)) while having substantially lower copy-paste scores, effectively shifting the operating point of the fidelity-variation trade-off.

## Strengths

1. **Large-scale paired multi-ID dataset (MultiID-2M).** The paper constructs 500K group photos with paired reference images across ~25K identities, averaging hundreds of references per identity. Prior datasets lack this paired structure, forcing reconstruction-only training. The four-stage pipeline (single-ID collection → clustering → multi-ID retrieval → pairing/filtering) is clearly documented with specific thresholds. This is a significant community resource.

2. **Copy-Paste metric that formalizes an underappreciated problem.** ℳ_CP (Eq. 2) uses angular distances among generated, reference, and ground-truth embeddings to measure whether the output is biased toward copying the reference versus matching the natural variation of the identity. Table 1 demonstrates the metric's utility: methods like InstantID achieve high Sim(GT)=0.464 but CP=0.337, while WithAnyone achieves comparable Sim(GT)=0.460 with CP=0.144 — directly revealing that Sim(Ref) alone masks copy-paste.

3. **Convincing empirical demonstration of the shifted trade-off.** Figure 5 shows all 13 baselines lying near a fitted curve where higher Sim(GT) correlates with higher CP, while WithAnyone deviates into the desirable region (high Sim(GT, low CP). This is the single strongest piece of evidence in the paper and is supported by both single-ID (Table 1) and multi-ID (Table 2) quantitative results.

4. **GT-aligned ID loss enabling supervision across all noise levels.** By using ground-truth landmarks rather than predicted landmarks to align the generated face for ArcFace embedding, the ID loss can be applied at any noise level without computational overhead or noisy alignment. Figure 7 and Table 3 ablation show this component improves identity similarity.

5. **Ablations cleanly isolate the effect of each component.** Table 3 shows that removing Phase 3 (paired tuning) increases CP from 0.161 to 0.239 while Sim(GT) stays nearly identical, directly attributing copy-paste suppression to the paired-data training stage. Removing GT-aligned ID loss drops Sim(GT) from 0.405 to 0.385.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The Copy-Paste metric's reliance on a single GT photograph is under-discussed.** Sim(GT) measures similarity between the generated image and one specific ground-truth photograph. Differences irrelevant to identity (background crop, lighting, expression intensity, hair part) can lower Sim(GT) even when identity is well-preserved and the prompt is followed. The paper filters cases with Sim(GT) < 0.40 for the CP ranking, which helps but this limitation is not explicitly discussed. The metric is still clearly more informative than using Sim(Ref) alone, and the qualitative results (Fig. 6) corroborate that WithAnyone genuinely generates more controllable outputs, but the paper would benefit from acknowledging this nuance.

2. **The "breaking the trade-off" claim is slightly overstated.** WithAnyone achieves Sim(GT)=0.460 vs. InstantID's 0.464 (within rounding) and UMO's 0.458, while achieving much lower CP (0.144 vs. 0.337/0.359). This is a Pareto improvement at a better operating point — a significant advance — but the language of "breaking" (used in the abstract, introduction, and conclusion) implies a fundamental restructuring of the trade-off curve rather than shifting to a better operating point. This is a rhetorical issue, not an evidential one.

3. **Limited analysis of what the model learns about identity variation beyond the CP metric.** The paper shows the model produces lower CP scores and better prompt adherence, but does not analyze whether the generated identity manifold matches the natural variation of real identities. The density plot in Fig. 2 is the only distributional analysis. Controlled experiments (e.g., varying only expression while fixing identity) or analysis of within-identity vs. between-identity embedding distances would strengthen the argument that the model has learned genuine identity-conditional generation rather than a better form of reconstruction.

4. **Several hyperparameters are stated without justification or ablation.** The 50% paired-to-unpaired ratio in Phase 3, the threshold of 0.4 for ArcFace matching in data construction, and the number of negatives (4096) in the contrastive loss are all reasonable choices but are not ablated. The paper would be strengthened by even a small study showing sensitivity to these values.

5. **No inference cost comparison.** WithAnyone is built on FLUX (a heavy DiT backbone). A comparison of generation time and memory against other FLUX-based methods (PuLID, InstantID) would help calibrate the practical cost of the improvements.

6. **User study is limited.** Ten participants and 230 groups is a modest sample. The results are supportive but the statistical power is low.

### Trivial
- The 435 test cases in MultiID-Bench lack confidence intervals or bootstrap estimates. Adding these would improve precision reporting.
- The number of unique identities in the paired subset (vs. the full corpus of ~25K) is not explicitly stated.

## Nice-to-Haves
- A controlled experiment tracking Sim(Ref) for the same identity across prompts with varying pose, expression, and lighting would directly demonstrate that WithAnyone's reference similarity distribution matches real-world identity variation more closely than baselines'.
- Analysis of failure cases: when does WithAnyone still produce copy-paste artifacts, and when does identity fidelity drop?
- Ablation of the 50% paired data ratio in Phase 3 (even 25% vs. 75%) and of the number of negatives in the contrastive loss.
- Evaluation on user-provided (non-celebrity) photos to test generalization beyond the benchmark.

## Removed Points

- **"The paper does not report the number of unique identities in the paired subset"** — The paper states the full corpus covers ~25K identities and the single-ID reference bank has ~3K identities. The paired subset count is implicitly bounded by these figures. Extremely minor; removed.
- **"The filtering threshold (0.4) is given without justification"** — This is a standard ArcFace matching threshold used throughout the face recognition literature. Removed as generic.
- **"Missing standard deviations"** — While technically correct, single-run evaluation on 435 samples is the norm in this space. Retained as trivial, not a structural weakness.
- **"Paired training may encourage target-specific overfitting"** — The harsh critic raised this as a potential concern, but the paper's contrastive loss with 4096 negatives from different identities explicitly addresses this. The ablation (w/o Ext. Neg. column in Table 3) shows Sim(GT) drops from 0.405 to 0.368 when negatives are removed, confirming the negatives help prevent such overfitting. Removed as the paper already addresses it.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's central finding — that a paired dataset with contrastive identity training can shift the fidelity-variation trade-off — but do not generate new observations outside this frame.

## Suggestions

1. Soften the "breaking the trade-off" language to "significantly shifting the operating point" or "achieving a Pareto improvement."
2. Add a brief discussion of the Copy-Paste metric's limitation: Sim(GT) measures similarity to a specific photograph, not identity in the abstract, and filtering at 0.40 mitigates but does not eliminate this.
3. Add an analysis of the learned identity manifold (within-identity vs. between-identity embedding variance compared to real data) to strengthen the claim that the model learns general identity-conditional generation.
4. Ablate the 50% paired ratio and the number of negatives (4096) with at least one alternative value each.
5. Add inference speed/memory comparison against PuLID and InstantID on FLUX.

## Score and Decision

**Score analysis against calibration anchors:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| UIFace | riieAeQBJm.md | 6.00 | R1/R2 | WithAnyone has a larger dataset contribution, more baselines, and addresses a more practical problem. **WithAnyone is stronger.** |
| Event-Customized | 88Qm4fGWzX.md | 5.00 | R1 | Limited evaluation (retrieval-based only), limited novelty. **WithAnyone is significantly stronger.** |
| DreamMakeup | WUibctXLT7.md | 4.75 | R1 | Insufficient validation, lack of comparison with relevant baselines. **WithAnyone is significantly stronger.** |
| DreamBench++ | 4GSOESJrk6.md | 6.00 | R2 | Purely a benchmark contribution. WithAnyone has dataset + benchmark + method. **WithAnyone is stronger.** |
| ClassDiffusion | iTm4H6N4aG.md | 6.25 | R2 | Simple method with clear motivation but narrower scope. **WithAnyone is stronger.** |
| InstantPortrait | ZkFMe3OPfw.md | 6.67 | R2 | Impressive one-step editing but limited to fixed poses. WithAnyone addresses a broader, more fundamental problem. **WithAnyone is slightly stronger.** |
| Vec2Face | RoN6NnHjn4.md | 6.00 | R2 | Strong results but significant concerns about unfair comparison and privacy. **WithAnyone is stronger.** |
| RB-Modulation | bnINPG5A32.md | 8.00 | R1 | Novel theoretical framework (optimal control), strong results. **WithAnyone is weaker.** |

The paper is clearly stronger than all anchors in the 5.00–6.67 range and falls below the 8.00 anchor. The final score of **7.0** reflects a strong, well-executed paper with a substantial dataset and benchmark contribution, a clear and well-supported method, and comprehensive evaluation — held back slightly by rhetorical overclaim, a few unablated hyperparameters, and limited analysis of the learned identity manifold.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>