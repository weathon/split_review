Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces **dynamic frames** for SE(3)-invariant crystal structure modeling. The core idea is that frames — coordinate systems used to extract invariant directional features — should be constructed *per atom and per layer* using learned attention weights, rather than being statically determined from the global structure. The authors instantiate this through weighted PCA and a "max" neighbour-direction selection, integrate them into the Crystalformer architecture, and evaluate on JARVIS, MP, and OQMD benchmarks. The best variant (max frames) outperforms Crystalformer and surpasses published numbers for strong baselines like PotNet, Matformer, and iComFormer on 7 of 9 property prediction tasks.

## Strengths

1. **Conceptually novel and well-motivated.** The paper provides a principled grounding for dynamic frames in Section 3 by rewriting the general message-passing equation (Eq. 5) and arguing that frames should align with learned interatomic interactions rather than the static global structure. This cleanly departs from prior frame methods (PCA frames, lattice frames) which are statically determined.

2. **Quantitative superiority across multiple benchmarks.** CrystalFramer with max frames achieves the lowest mean absolute error on 7 out of 9 tasks across JARVIS and MP (Tables 1–2), outperforming prior state-of-the-art methods including iComFormer, PotNet, Matformer, and the Crystalformer baseline. On JARVIS formation energy it reaches 0.0263 eV/atom vs. 0.0272 for the next best, and on MP bulk modulus 0.0338 vs. 0.0354.

3. **Ablation evidence isolating the contribution of learned weights.** The comparison between max frames (dynamic, attention-derived weights) and static local frames (distance-only weights using the same per-atom construction) shows that max frames wins on 8 of 9 tasks and on 7 of 9 against all methods — directly demonstrating that learned dynamic weights provide additional benefit beyond simply having local frames.

4. **Favorable efficiency-accuracy trade-off.** Table 4 shows CrystalFramer (952K params, 16.8 ms/test) achieves better accuracy than iComFormer (5.0M params, 54.8 ms) and PotNet (1.8M params, 313 ms) with substantially fewer parameters and faster inference, despite 2× training time vs. Crystalformer.

5. **Scalability on a large dataset.** Table 3 shows CrystalFramer outperforms Crystalformer on OQMD (817,636 materials) across all three properties (formation energy: 0.01871 vs. 0.02115 eV/atom), confirming dynamic frames remain effective at scale.

## Weaknesses

### Major

- **No error bars or uncertainty quantification.** The paper reports single-run mean absolute error without standard deviations or confidence intervals. Given that several comparisons involve very small margins (e.g., 0.000x eV/atom differences), it is not possible to assess whether these improvements are statistically significant or within run-to-run noise. This is the most significant gap in empirical rigor — at minimum the main JARVIS and MP comparisons should be reported over multiple seeds.

### Minor

- **Attribution of gains: "dynamic" vs. "local" is partially confounded.** The static-local frame ablation (distance-only weights, per-atom) already yields large improvements over Crystalformer and occasionally outperforms max frames (e.g., JARVIS E_hull: 0.0444 static vs. 0.0471 max). While max frames win on most tasks, the margin over static-local is often modest, making it difficult to cleanly attribute the gains to *learned* dynamism vs. simply having *per-atom* local frames. The paper lacks an ablation using random learned weights or uniform weights to test whether any dynamic weighting helps or whether the specific attention-derived distribution matters. This does not undermine the contribution (the results are clear) but weakens the specific claim that "dynamic" as opposed to "local" is the key factor.

- **OQMD evaluation compares only to Crystalformer.** Table 3 compares CrystalFramer against only the Crystalformer baseline on OQMD. Including at least one additional top baseline (e.g., iComFormer or PotNet) on this larger dataset would substantially strengthen the claim of state-of-the-art scalability.

- **Gradient stopping limits the "learned" frame claim.** The frame construction (both PCA and max) is non-differentiable, so gradients are not propagated from edge features back through frame computation to the attention weights. The authors acknowledge this and report that gradient approximations (straight-through estimator, softmax temperature annealing) empirically underperformed ignoring them. While a pragmatic and clearly documented choice, the frames are only indirectly shaped by the prediction task through the distance-decay attention loss, not directly optimized to improve frame quality.

### Trivial

- **The strength finder's claim of "8 out of 9 tasks" is inaccurate; the correct count is 7 out of 9** (max frames loses on JARVIS E_hull and MP shear modulus to other methods).

## Nice-to-Haves

- A quantitative comparison of different gradient strategies (straight-through, softmax relaxation, no gradients) in an appendix, to substantiate the claim that ignoring gradients gave the best results.
- An ablation using random weights and uniform weights for the same per-atom local frame construction, to cleanly separate the "local" effect from the "dynamic/learned" effect.
- A small quantitative study showing the distribution of attention weights (e.g., what fraction are near-zero) to motivate why weighted frames are needed over uniform local frames.

## Removed Points

- **Task-specific tuning disclaimer (Harsh Critic):** The paper already explicitly acknowledges this (Section 5, "It is important to note that the current state-of-the-art, ComFormer, uses finely-tuned hyperparameters… whereas we simply adjust the number of epochs and batch size for each dataset"). The criticism asks the authors to do more, but it is scope creep for a paper whose main contribution is a new architectural concept.
- **"Missing gradient strategy quantitative comparison" (Harsh Critic's Section 3.1 note):** This is a reasonable suggestion for strengthening but is framed as a weakness; moved to Nice-to-Haves.
- **"Claim of 8/9 tasks in Strength Finder":** Adjusted to 7/9 in the strengths above; the inflated count is removed.
- **"Frame evolution / OOD generalization concerns" (Harsh Critic references to Appendix I):** The paper references Appendices F and I which are not available in the extracted text (parser issue). Speculating about missing appendix content is not a valid criticism.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between "local" and "dynamic" that the paper partially leaves unresolved. The static-local ablation (distance-based exponential weights, no learning) already produces a dramatic improvement over Crystalformer — sometimes competitive with max frames. This suggests that the single most impactful design choice may be *per-atom* frame construction rather than *learned* frame construction. The dynamic component provides consistent but often modest additional gains. A reviewer might hypothesize that for many crystals, attention weights are relatively diffuse (many neighbors with similar weights), so the geometric locality matters more than the precise weighting. The paper already contains the data to test this (attention weight distributions from the trained model), and making this analysis explicit would sharpen the contribution.

## Suggestions

1. **Report error bars** (standard deviation over 3–5 seeds) for the main JARVIS and MP comparisons. This is the single biggest improvement the authors could make and would substantially increase confidence in the results.
2. Add an ablation with **uniform weights** and **random learned weights** for the per-atom frame construction to cleanly separate the "local" effect from the "dynamic" effect.
3. Include at least one additional top baseline (e.g., iComFormer or PotNet) on the OQMD dataset to strengthen scalability claims.
4. Add a quantitative analysis of attention weight distributions (e.g., entropy, fraction near-zero across layers) to provide intuition for when dynamic frames matter most.

## Score and Decision

**Round 1 bracket:** 6–8. The paper is clearly better than lower-band anchors (PDDFormer at 5.0, continuous invariants at 4.5), comparable to or better than mid-band anchors (Crystalformer at 7.25, DiffCSP++ at 7.33, AssembleFlow at 6.5), and below top-band generative modeling anchors (MOFDiff at 8.0).

**Round 2 narrowing:** Anchoring against Crystalformer (avg 7.25, accepted poster) — the most directly relevant comparison since CrystalFramer builds on and consistently improves Crystalformer's results. CrystalFramer has a more novel conceptual contribution (dynamic frames is a genuinely new idea, whereas Crystalformer's innovation was an attention formulation that some reviewers found incremental), better empirical coverage (OQMD data), and is cleaner methodologically. However, CrystalFramer lacks error bars (Crystalformer also lacked them, but it was noted as a limitation), has a partially confounded attribution, and 2× training time. On balance, CrystalFramer is a somewhat stronger paper than Crystalformer.

**Final anchors used:**
- `/home/wg25r/review_agent/human_reviews/fxQiecl9HB.md` (Crystalformer, avg 7.25, Round 1/2) — The baseline of this paper; CrystalFramer is clearly stronger conceptually and empirically.
- `/home/wg25r/review_agent/human_reviews/jkvZ7v4OmP.md` (DiffCSP++, avg 7.33, Round 1/2) — Crystal generation paper; comparable quality, similar level of contribution.
- `/home/wg25r/review_agent/human_reviews/jckKNzYYA6.md` (AssembleFlow, avg 6.50, Round 1/2) — Molecular assembly with frames; CrystalFramer is more novel conceptually and has more thorough evaluation.
- `/home/wg25r/review_agent/human_reviews/ewjN1MAnJi.md` (PDDFormer, avg 5.00, Round 1) — Crystal property prediction; CrystalFramer is substantially stronger on all axes.
- `/home/wg25r/review_agent/human_reviews/rcdR97P2Mp.md` (avg 4.50, Round 1) — Crystal invariants; weaker ML contribution.
- `/home/wg25r/review_agent/human_reviews/0VBsoluxR2.md` (MOFDiff, avg 8.00, Round 2) — MOF generation; higher-scoring work but in a different task (generation vs. prediction).

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>