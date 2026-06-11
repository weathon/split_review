## Summary

This paper proposes a learnable three-channel Gray-Wyner Network that separates common and task-specific information between two vision tasks. It contributes Theorem 1 (extending Wyner's lossless bounds to the lossy setting), a Lagrangian objective (Eq. 12) with a single hyperparameter β controlling the transmit-receive tradeoff, and a heuristic "matching" architecture for extracting the common representation. Experiments on synthetic data, colored MNIST, Cityscapes (segmentation+depth), and COCO (detection+keypoint) demonstrate the ability to trade off transmit vs. receive rates.

## Strengths

- **Theorem 1 extends Wyner's lossless bounds to the lossy setting.** The bounds relating Gács-Körner and Wyner's common information via interaction information (Eq. 6–7) are a non-trivial theoretical extension of Wyner (1975). This provides a formal foundation for expecting a gap between the two common-information measures in practice, which motivates the transmit-receive tradeoff.

- **Practical Lagrangian objective with single-parameter tradeoff control.** The transformation of the Gray-Wyner variational objective (Eq. 9) into a practical loss (Eq. 12) with β=1 optimizing transmit rate, β=2 optimizing receive rate, and β=3/2 balancing both is cleanly derived via Theorem 2. Prior multi-task coding work lacked this principled, theoretically grounded knob.

- **Controlled edge-case experiments on colored MNIST (Section 4.2).** The three designed PMFs (Dependent, Independent, Mixture) with known joint entropies and mutual informations provide ground-truth-verifiable validation. The Dependent PMF achieves the lowest transmit rate (most info on the common channel), and the Independent PMF achieves the lowest receive rate — confirming the method behaves as expected under extreme MI regimes.

- **Ablation comparing three encoder architectures on synthetic data (Section 4.1).** The comparison of Shared vs. Separated (independent transforms per channel) vs. Combined (single transform split) architectures demonstrates that the proposed architectural choices contribute beyond the loss function alone.

## Weaknesses

### Major

1. **Substantial underperformance against the Joint baseline is understated.** The proposed method requires 13–23% *more* bitrate than Joint coding at the same task accuracy (Figure 5: Cityscapes +23.32% BD-rate, COCO +13.16% BD-rate). This gap is described as "relatively close" (line 271), but in compression, 13–23% is a large penalty that would dominate deployment decisions. Joint coding (a single shared encoder + separate task decoders) is the natural baseline for the stated scenario (transmitting to a single device), yet the paper's headline claims ("substantially reduces redundancy") rely on comparisons against Independent coding — a weak baseline that any cooperative multi-task codec trivially beats.

2. **Headline BD-rate claim is unverifiable from presented data.** The conclusion states "between the three computer vision experiments, our codecs achieved, on average, a BD-rate advantage of -81.58% in transmit rate, against single-task codecs" (line 275). However, all BD-rates in Figure 5 are computed against Joint, not against single-task (Independent) codecs. The paper does not report the direct Proposed-vs-Independent BD-rates for these experiments, so the reader cannot verify this number. (Indirect computation from Figure 5's Joint-referenced data gives ~49% and ~36% for the two experiments, not -81.58%.)

3. **Theory-experiment misalignment.** Theorem 1 and the Gray-Wyner framework assume the Markov conditions Z₂ ↔ X₂ ↔ X₁ and Z₁ ↔ X₁ ↔ X₂ (Eq. 1). The experiments set (X₁, X₂) = X (a single source, line 191), and the paper acknowledges that "this effectively removes the requirement for the conditions in 1" (line 167). The paper never discusses whether the theoretical guarantees (the bounds in Theorem 1, the Gray-Wyner region characterization) carry over to this relaxed setting. The theoretical contributions and empirical evaluation thus operate under fundamentally different assumptions.

4. **Common-channel matching mechanism is heuristic and unablated.** The core architectural novelty — the matching operation in Eq. 14 (averaging matching elements, zeroing non-matching ones) — has no ablation study isolating its contribution. Alternatives such as a learned projection (concatenation + linear layer) or simple averaging without zeroing are not compared. There is no experiment verifying that Y₀ actually captures task-relevant common information (e.g., via cross-decoding from Y₀ alone, or measuring mutual information of learned representations). Without such validation, it is unclear whether the method is truly extracting common information or merely exploiting a training artifact.

### Minor

1. **Theorem 1 is never operationalized.** The paper does not compute interaction information empirically or use the bounds to interpret any experimental result. The theorem remains a standalone theoretical statement disconnected from the evaluation.

2. **No comparison against existing multi-task codecs.** Section 2 cites Chamain et al. (2021), Feng et al. (2022), and Guo et al. (2024) as relevant multi-task learnable codecs, but none are used as baselines. Including at least one would strengthen the positioning.

3. **No error bars or variance reporting.** All results are single-run point estimates. Given the stochasticity in training learnable codecs, the reported BD-rate differences (especially marginal ones) cannot be assessed for significance.

4. **Assumption α₁ = α₂ not discussed.** The loss assumes equal private-channel costs (line 151), which may not hold when tasks have vastly different rate requirements (e.g., dense prediction vs. classification).

### Trivial

None.

## Nice-to-Haves

- A cross-decoding experiment measuring whether Y₀ alone (without private channels) supports both tasks.
- Evaluation in a scenario where the receive-rate constraint actually binds (e.g., two devices receiving different task subsets).
- A genuine two-source experiment (e.g., correlated views of a scene) matching the theory's original setting.

## Removed Points

These points were raised in the reviews but are removed or demoted for the following reasons:

- **"Mixture PMF produces worse performance — precisely where the method should demonstrate value"** — Removed. The Mixture PMF is designed to be a hard case where common information is not separable; the paper acknowledges this, and finding it difficult is expected behavior, not a flaw.
- **"Independent baseline is a strawman"** — Softened. Independent coding is a practical baseline for some deployment scenarios, but the paper overstates the significance of beating it.
- **"No limitations section"** — Removed. Not a scientific weakness.
- **"No discussion of quantization's effect on common information"** — Removed. Niche concern without evidence that quantization specifically harms the approach.
- **"Gap between empirical and theoretical rates dismissed with a single citation"** — Removed. This gap is a well-known phenomenon in ML rate-distortion; a single citation to a relevant work is standard practice.
- **Various formatting/style nitpicks** — Removed. Parser artifacts, not author errors.

## Novel Insights

The harsh critic's observation that the matching operation (Eq. 14) is never validated to actually extract common information — beyond aggregate rate-distortion curves — is a genuinely insightful criticism. The paper presents the mechanism as an architectural contribution but provides no direct evidence (cross-decoding, mutual information measurement, or even a simple ablation against a learned merger) that the common channel contains task-relevant shared information rather than whatever noise happened to match between the two feature extractors. This is a concrete, actionable gap between claim and evidence that the authors could address in a few additional experiments.

## Suggestions

1. Report BD-rates directly against Independent coding in the main text, or clarify which baseline the -81.58% claim refers to and how it is computed.
2. Add an ablation replacing the matching operation (Eq. 14) with a learned projection or simple averaging, and report the effect on BD-rate.
3. Discuss whether Theorem 1's bounds remain valid when (X₁, X₂) = X and the Markov conditions are removed, or explicitly scope the theory's applicability.
4. Add a cross-decoding experiment measuring task accuracy from Y₀ alone vs. from (Y₀, Y₁) and (Y₀, Y₂), to verify the common channel's content.
5. Add error bars (multi-seed runs) for at least one key experiment.

## Calibration

**Round 1 — Bracket (3 queries):**
- Weak anchors (score < 3.5): Papers on text compression (3.00), NCA compression (3.40), GNN-as-channel (3.00), etc. → The paper under review is clearly stronger.
- Middle anchors (3.5–7.5): Multi-task compression paper (x33vSZUg0A.md, 5.33), rate-distortion quantization (LnKDcqOfgy.md, 5.00), multi-task representation theory (6Ey8mAuLiw.md, 5.25). → The paper under review is in this band. It is most comparable to the multi-task compression paper (5.33).
- Strong anchors (score > 7.5): Papers on identifiability, information bottleneck theory, etc. (all 8.00). → The paper under review is substantially weaker; these are finished, polished theory papers with clean experiments.

**Initial bracket:** 4.0 – 6.5

**Round 2 — Narrowing within bracket:**
- Lower middle (3.5–5.5): Most similar anchor is x33vSZUg0A.md (avg 5.33, scores 8/5/3), a multi-task compression paper accepted at the conference. It has stronger baselines and experiments but theory roughly comparable.
- Upper middle (5.5–7.5): Compression papers like bsnRUkVn63.md (avg 6.00, all scores 6). These have more polished experiments and cleaner alignment between theory and evaluation.
- The paper under review is weaker than the 6.00 anchors (which have thorough experiments and consistent scores) and slightly weaker than the 5.33 multi-task anchor (weaker experiments, unverifiable claims). It is comparable to the 5.00–5.25 range.

**Final score: 5.0**

**Decision rationale:** The paper's theoretical contributions (Theorem 1 and the Lagrangian formulation) are genuine, and the problem framing is timely. However, the experimental evaluation has significant issues — the headline result cannot be verified from presented data, the method underperforms the natural Joint baseline by a practically meaningful margin, the heuristic common-channel mechanism is unablated, and the theory operates under different assumptions than the experiments. These are not minor presentation issues; they cut to whether the paper's claims are supported. With major revisions, the paper could be a solid contribution, but in its current form it does not deliver what it promises.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>