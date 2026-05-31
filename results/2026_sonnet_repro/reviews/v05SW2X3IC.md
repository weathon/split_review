Now let me run calibration searches to determine the score range for this paper.**Round 1 bracket**: The paper sits likely between **4.5 and 6.5** — it has genuine theoretical contributions (Theorems 1 and 2, extensions of GWN to lossy setting) and real empirical results, but the structural experimental gap (single-source only) and missing comparisons to prior multi-task codecs weigh against a higher score. Let me narrow this bracket.Let me read the two most relevant anchors in detail.Now I have sufficient calibration data to write the final review.

**Anchor summary before scoring:**
- x33vSZUg0A (5.33, Accepted): Multi-task compression with causal discovery, similar domain, no theoretical bounds, complex unvalidated components
- vdUYa7N8Mt (5.50, Rejected): Pure theory on RD-perception tradeoff, no experiments, cleaner mathematics
- Tv36j85SqR (7.20, Accepted): Strong RD theory with lattice transform coding, novel theory + convincing experiments with clean empirical validation

**Round 1 bracket**: 4.5–6.5
**Round 2 narrowing**: The paper sits between x33vSZUg0A (5.33) and vdUYa7N8Mt (5.50). It is more theoretically grounded than x33vSZUg0A (which lacks formal bounds) but has weaker empirical scope than the 7+ tier papers. The structural gap between the distributed-coding motivation and the single-source experiments, plus missing direct comparisons to prior multi-task codecs, prevents a higher score. Final position: **5.0**.

---

## Summary

This paper proposes a learnable three-channel codec grounded in Gray-Wyner (GW) theory that separates shared from task-specific information for two-task computer vision. The core theoretical contributions are Theorem 1, which extends Wyner's lossless common-information bounds to the lossy setting via interaction information, and Theorem 2, which re-expresses the GW objective for deterministic encoders in terms of conditional entropy functions, yielding a practical single-hyperparameter Lagrangian. The resulting architecture demonstrates empirically that varying β predictably shifts the transmit–receive tradeoff, and the method substantially outperforms independent single-task codecs on CV benchmarks.

---

## Strengths

- **Theorem 1 (Equations 6–7)**: The paper provides a non-trivial extension of Wyner's lossless bound to the lossy case through interaction information, establishing bounds that bracket the two lossy common-information measures and formalizing the gap that motivates the transmit–receive tradeoff. This is a concrete and verifiable theoretical contribution.

- **Theorem 2 (Equation 10)**: The reformulation of the GW objective from mutual-information terms to entropy functions (H(Y₀) and conditional entropies H(Y₁|Y₀), H(Y₂|Y₀)) under deterministic encoders is the key theoretical bridge that makes the framework trainable with learned entropy models, and the derivation connects classical information theory to modern learned codecs.

- **Synthetic experiment (Figure 3a)**: Using a controlled dataset with known mutual information (I(X₁;X₂) = 1.32 bits), the paper shows that β = 1 places R₀ above the empirical mutual information, β = 2 places it below, and β = 3/2 sits between — exactly matching the theoretical predictions. This is a precise, principled validation of the optimization objective.

- **MNIST edge-case analysis (Section 4.2, Figure 4)**: The method is tested on three well-characterized PMFs (Dependent, Independent, Mixture) where ground-truth mutual information is known. The method behaves consistently with theory across extremes: Dependent PMF produces a low transmit rate by utilizing the common channel fully, and Independent PMF produces a low receive rate with minimal common-channel usage.

- **Conditioning private entropy models on common representation (Section 3.3)**: The design choice to condition the private-channel entropy models h₁ and h₂ on Y₀ is explicitly justified by the difficulty of achieving I(Y₁,Y₂;Y₀) = 0 in practice, and it directly addresses residual redundancy between channels — a real and frequently overlooked issue in multi-channel codec design.

---

## Weaknesses

### Fatal
None.

### Major

- **Single-source experimental scope vs. distributed-coding motivation**: The paper's introduction and theoretical framework are built around distributed coding — a camera transmitting shared vs. task-specific information so that a later second-task request requires only the additional private bits. Section 4 explicitly specializes to (X₁, X₂) = X throughout every experiment, including the CV benchmarks on Cityscapes and COCO. In this regime, the transmit-receive tradeoff reduces to a rate-allocation trade between the common and private channels of a *single-encoder* codec, and there is no actual distributed-inference scenario. While this specialization is transparently acknowledged ("our experiments... specialize to a single source X"), the abstract and introduction strongly frame the motivating use case as separate-device distributed inference. The paper does not include even one experiment with X₁ ≠ X₂ (e.g., stereo pairs, temporally adjacent frames, or cross-modal pairs), leaving the central motivating scenario entirely undemonstrated. This gap between framing and evidence is the paper's most significant limitation.

- **Absence of direct comparison to existing multi-task codecs**: Section 2 cites Chamain et al. (2021), Feng et al. (2022), and Guo et al. (2024) as directly relevant prior work with common channels for multi-task coding. The paper argues (Section 2, paragraph beginning "Multitask learnable codecs...") that these are equivalent to the Joint baseline because they lack private channels. This equivalence claim is asserted but not demonstrated experimentally. If any of these prior codecs outperform Joint on transmit rate (which is possible given their specialized design), the paper's BD-rate advantage relative to the field would be weaker than reported. At minimum, one direct empirical comparison with a cited prior multi-task codec is needed to substantiate the equivalence claim.

### Minor

- **Masking mechanism (Equation 14) is architecturally novel but analytically thin**: The element-wise agreement mask is the central architectural novelty — Y₀ retains elements only where Y₀^(1) and Y₀^(2) agree post-quantization. The paper fixes γ = 1 without sensitivity analysis and reports no statistics on what fraction of Y₀ elements are nonzero at convergence across different β values or task pairs. Since gradient flow to the common channel is blocked at all disagreeing positions, the sparsity pattern has direct bearing on whether the common channel learns shared structure or simply degenerates. Without any analysis of this quantity, the masking mechanism reads as an undervalidated design choice.

- **Architecture removes Markov conditions without sufficient discussion (Section 3.3, Equation 1 vs. paragraph 3 of Section 3.3)**: The paper states that having both f₁ and f₂ see both sources X₁ and X₂ "effectively removes the requirement for the conditions in 1." The Markov conditions Z₂ ↔ X₂ ↔ X₁ and Z₁ ↔ X₁ ↔ X₂ are not a technicality — they define which source has exclusive information and are foundational to the GWN decomposition. Departing from them is significant and deserves more than one sentence of acknowledgment. The paper should clarify whether the theoretical results in Section 3 still bound what the implemented system is actually learning, or whether Appendix C's compatibility analysis fully substitutes for this guarantee.

- **BD-rate headline figure is relative to the weaker baseline (Section 5)**: The conclusion highlights "−81.58% in transmit rate against single-task codecs" without mentioning that the proposed method costs +23–52% in BD-rate relative to the Joint baseline (Figure 5). Presenting only the Independent-relative figure creates a misleadingly favorable impression of practical competitiveness; both numbers should appear together in any summary.

### Trivial

- The paper reports operation "within an order of magnitude of theoretical bounds" (Section 4.2) without quantifying the factor. Stating the actual ratios (e.g., ×3 or ×8) would make this comparison informative rather than a vacuous bound.

---

## Nice-to-Haves

- An experiment with genuinely separate correlated sources (e.g., stereo pairs with segmentation on the left view and depth on the right) would directly demonstrate the distributed-inference scenario that motivates the paper, and would be the single most compelling addition to the work.
- Ablating masking sparsity at convergence (fraction of active Y₀ elements as a function of β and task pair) would convert the masking mechanism from an empirically used design choice into a validated architectural contribution.
- Showing the Shared vs. Separated vs. Combined architecture comparison across all β values in the main text (Section 4.1 currently defers other β values to the appendix) would strengthen the core ablation, since β is the paper's central control parameter.
- Quantifying the transmit/receive rate gap relative to theoretical bounds as a ratio rather than "order of magnitude" language in Section 4.2 would sharpen the empirical claims.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Lack of variance / reproducibility across training runs" (Harsh Critic)**: Removed as a reproducibility nitpick. Single-run evaluation is standard in learned image compression, and requesting training-variance statistics goes beyond community norms for this type of empirical evaluation.

- **"GK common information is zero for Gaussian sources — when does the tradeoff actually matter?" (Harsh Critic, Section 3.1)**: Removed as a strawman. The paper explicitly acknowledges this in Section 3.1 ("it is zero for Gaussian sources with correlation 1−ρ") and uses it as a positive motivation: "there is a significant motivation to explore the transmit-receive tradeoff." The critic's framing treats something the paper already addresses as a weakness.

- **"Quantifying the empirical-vs-theoretical rate gap in the synthetic experiment" (Harsh Critic, Section 4.1)**: Removed as a minor presentation request. The paper cites Bajić (2025) for the expected behavior and the qualitative trends are clearly validated; this is a nice-to-have, not a weakness.

- **"Low-compression performance dip on Cityscapes" (Harsh Critic, Section 4.3)**: Demoted from weakness. The paper acknowledges this informally ("often attributed to lack of regularization"), and the effect is visible but does not affect the BD-rate comparisons which span the full compression range. It's a known artifact in learned codecs and not specific to this method.

- **Generic strength: "the problem has multiple applications / is important" (Strength Finder)**: Removed as a generic/superficial strength without evidence specific to this paper.

- **Strength about Appendix C compatibility analysis as a standalone justification for feeding both X₁ and X₂ to both branches**: Partially removed. The appendix is cited and assumed to exist, but since the Markov-condition removal is flagged as a real (if minor) concern, this cannot be simultaneously cited as a full strength. It is noted in the Strengths section only in its function of providing partial grounding.

---

## Novel Insights

The paper's most insightful contribution beyond its listed results is the constructive connection it draws between the Gács-Körner block-diagonal separability condition (Equation 8) and the masking operation (Equation 14): the mask zeroes out positions where the two independently computed common-channel tensors disagree, which is a learnable approximation to the condition that Y₀ be a function simultaneously of both sources. This operationalizes a hard-to-compute information-theoretic property (GK CI requires a block-diagonal stochastic matrix) into a differentiable training procedure. Whether the approximation quality is sufficient — and under what task-pair conditions it degrades — remains an open question that the paper raises but does not resolve, and is a productive direction for follow-on work.

---

## Suggestions

1. Add one experiment with truly separate correlated sources (X₁ ≠ X₂) — stereo image pairs or temporally adjacent frames are natural choices given the existing CV task set — to demonstrate the distributed-inference scenario that the paper's introduction motivates.
2. Report the BD-rate relative to the Joint baseline alongside the Independent-relative figure in the abstract and conclusion, to give an accurate picture of practical competitiveness.
3. Add an analysis of Y₀ element-wise activation sparsity at convergence (fraction of nonzero elements in the masked Y₀ as a function of β) to validate that the masking mechanism is functioning as theoretically motivated.
4. Either run one prior multi-task codec (e.g., Chamain et al. 2021) as a direct baseline, or provide a theoretical argument demonstrating the equivalence to Joint more rigorously than the current one-sentence assertion.
5. Extend the discussion of the Markov-condition removal (Section 3.3) to clarify whether Theorem 1 and Theorem 2 still bound what the implemented architecture learns, or whether Appendix C's compatibility argument fully replaces that guarantee.

---

## Score and Decision

**Anchors used:**

| Path | Avg Score | Round | Comparison to paper under review |
|------|-----------|-------|----------------------------------|
| x33vSZUg0A | 5.33 | R1+R2 | Similar domain (multi-task compression); comparable depth but less rigorous theory; similar experimental scope limitation |
| aQ7qYnY2nF | 4.00 | R1 | Task-aware video compression with RL; much weaker theoretical grounding, clearly below the paper under review |
| Tv36j85SqR | 7.20 | R1 | Strong RD theory (lattice quantization) + clean convincing experiments; paper under review has weaker empirical scope |
| bsnRUkVn63 | 6.00 | R1 | Test-time adaptation for compression; incremental engineering contribution, no theoretical novelty; paper under review has stronger theory |
| vdUYa7N8Mt | 5.50 | R2 | Pure theory on RDP tradeoff with no experiments; paper under review has both theory and experiments but more experimental gaps |
| Piod76RSrx | 5.50 | R2 | MI generalization bounds; pure theory; paper under review has a similar theory-heavy profile |
| ulIW7Frjpn | 4.75 | R2 | LLM-based entropy models; incremental engineering, less novel theory |
| foKwWau15m | 6.00 | R2 | CMC benchmark for ultra-low bitrate; benchmark paper, no theory; different contribution type |

**Bracketing and narrowing**: Round 1 placed the paper between 4.5 and 6.5. Round 2 anchors cluster around 5.0–5.5. The paper is comparable to vdUYa7N8Mt (5.50) in theoretical quality but has the advantage of real experiments — though those experiments don't fully validate the paper's stated motivating scenario. It is above x33vSZUg0A (5.33) in theoretical rigor and comparable in experimental quality, but x33vSZUg0A was borderline-accepted (scores 8, 5, 3) suggesting the community values this work but finds real deficiencies. The two Major weaknesses — the single-source experimental scope and missing multi-task codec comparisons — are genuine barriers to acceptance without revision.

**Final Score: 5.0** — The paper has real theoretical contributions (Theorems 1–2 are non-trivial and correctly extend the GWN framework to the lossy setting) and solid empirical validation of the transmit–receive tradeoff in the single-source setting. However, the gap between the distributed-coding motivation and the single-source experiments, combined with the absence of direct comparison to existing multi-task codecs, prevents a clear acceptance recommendation without revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>