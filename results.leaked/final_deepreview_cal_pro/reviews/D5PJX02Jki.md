Now I have all the information needed. Let me compose the final review.

---

## Summary

This paper proposes RoPE++, which re-incorporates the imaginary component of the complex-valued attention dot product (normally discarded in standard RoPE) as a parallel set of attention heads. The authors introduce two variants: RoPE++_EH (equal heads, halved KV cache and QKV parameters) and RoPE++_EC (equal cache, doubled heads). Through theoretical analysis of characteristic curves, they argue the imaginary attention captures longer-range dependencies. Experiments at 376M and 776M scales across short-context and long-context benchmarks (RULER, BABILong) show RoPE++ outperforms standard RoPE and other position embeddings, with the imaginary attention playing a dominant role in long-context modeling as confirmed by noise-ablation experiments.

## Strengths

- **Novel idea with clear motivation.** The paper identifies a genuinely overlooked aspect of RoPE — the discarded imaginary component of the complex-valued attention — and re-purposes it as a complementary attention pathway. The mathematical derivation showing the imaginary attention corresponds to a π/2 rotation of the query before applying standard RoPE (Equation 4) is elegant and leads to a simple implementation.

- **Practical dual-configuration design.** The two variants address different deployment needs: RoPE++_EH halves KV cache and QKV parameters while maintaining comparable or better performance (Tables 1, 2; Figure 4), offering immediate practical value for resource-constrained long-context inference. RoPE++_EC doubles attention heads at equal cache cost for maximum performance.

- **Comprehensive benchmark evaluation.** Unlike many position-embedding papers that report only perplexity, this work evaluates on 11 short-context tasks (Open LLM Leaderboard suite: TruthfulQA, PIQA, HellaSwag, Winogrande, ARC-e, GPQA, etc.) plus two long-context benchmarks (RULER, BABILong) at multiple context lengths up to 64k. The long-context gains are substantial: RoPE++_EC improves RULER-64k from 5.5→9.0 at 376M and BABILong-64k from 7.8→12.8 (Table 2).

- **Causal evidence via noise ablation (Section 5.2).** The experiment injecting Gaussian noise separately into real vs. imaginary attention components provides direct evidence that imaginary attention is disproportionately important for long-context performance — an 8-point RULER gap at 776M when imaginary attention is corrupted vs. real attention. This is a well-designed mechanistic test.

- **Compatibility demonstrated.** RoPE++ combines effectively with existing context-extension techniques (Linear PI, YaRN), showing consistent gains across all combinations (Table 3), which strengthens the case for practical adoption.

- **Theoretical grounding.** The characteristic curve analysis (Equation 5, Figure 1) provides a principled explanation for why the imaginary component should favor long-range dependencies — the sine integral decays far more slowly than the cosine integral.

## Weaknesses

### Fatal

None.

### Major

- **Limited model scale.** All experiments use 376M and 776M parameter models trained on 50B tokens. While the evaluation breadth is commendable, the model sizes are modest for a paper targeting long-context LLMs, where the primary operating regime is 7B+. The paper references "larger model scale" analysis in Appendix C, but the stripped appendix cannot be verified. The effectiveness of RoPE++ at scales where long-context capability is most practically relevant remains an open question.

- **Missing capacity-controlled baseline for RoPE++_EC.** RoPE++_EC doubles the number of attention outputs and has a correspondingly larger W_o projection matrix compared to standard RoPE. While the paper argues that the real and imaginary heads share W_q (Section 3.3, line 112), making them not fully independent, a fair comparison would include a standard RoPE baseline with an equivalent increase in head count and W_o size. The gains attributed to the imaginary component in the EC configuration may be partially explained by increased model capacity. The EH variant partially addresses this (same head count, fewer parameters, yet matched performance), but the headline long-context results (Table 2) are driven primarily by EC.

### Minor

- **"Information loss" framing is imprecise.** The paper repeatedly describes standard RoPE as discarding information and incurring "irreversible information loss" (Abstract, Section 1, Section 3). In reality, the real part of the complex dot product (Equation 1) already contains both cosine- and sine-weighted combinations of all query/key dimensions. The imaginary part is a different linear projection of the same vectors, not an independent piece of information that is "lost." The contribution is better described as adding a complementary attention pathway rather than recovering lost information. This does not affect the technical validity but weakens the motivation.

- **Other position embeddings not evaluated on long-context tasks.** FoPE, ALiBi, and Pythia are compared only on short-context benchmarks (Table 1). On long-context benchmarks (Table 2), only RoPE serves as the baseline. This leaves open the question of whether RoPE++ is specifically better than RoPE or would also outperform these alternatives for long-context modeling.

- **No variance estimates.** All results are from single training runs. On short-context tasks where performance differences are often <1% absolute (Table 1), it is difficult to distinguish genuine improvement from run-to-run variance. The long-context gains are larger and more robust, but confidence intervals or multi-seed results would strengthen the evidence.

### Trivial

- The characteristic curve derivation (Section 3.2) assumes independent, isotropic query/key distributions. The paper does not discuss how sensitive the conclusions are to violations of this idealized assumption, nor does it directly verify the predicted curve shapes against empirically observed attention patterns in trained models.

- Exact parameter counts for each configuration (RoPE, RoPE++_EH, RoPE++_EC) are not reported, making it harder to assess the fairness of comparisons on a parameter-matched basis.

## Nice-to-Haves

- A standard RoPE baseline with doubled attention heads (or equivalently larger W_o) to isolate the effect of the imaginary formulation from the capacity increase in EC.
- Evaluation at a larger model scale (≥1B parameters) to confirm that the long-context benefits persist.
- Long-context evaluation of FoPE, ALiBi, and Pythia to strengthen the comparative claims.
- Reporting results over multiple random seeds with standard deviations.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Missing capacity control undermines the central claim" → DEMOTED to Major.** The concern is valid that EC has more capacity, but the EH variant provides a reasonable partial control by showing comparable performance with fewer parameters. The harsh critic claimed this was "fatal" but the EH results demonstrate the imaginary component contributes value even when parameter-matched or parameter-disadvantaged.

- **Harsh critic: "Insufficient evidence at scale makes the practical significance unclear" → KEPT as Major but softened.** The scale concern is real but common for methods papers. The harsh critic's claim that the models "have not effectively learned to use long contexts" because absolute RULER scores are low (~10% at 64k) ignores that this is normal for models of this size — the relative gains are what matter methodologically.

- **Harsh critic: "The 'information loss' motivation is misleading" → KEPT as Minor.** Verified against the paper text; the framing is indeed imprecise. However, this is a presentation issue, not a technical flaw, and does not affect the validity of the method.

- **Strength Finder: "Strong empirical gains on long-context benchmarks" → KEPT.** The gains are real and substantial, particularly for EC. Verified against Table 2.

- **Strength Finder: "Mechanistic evidence of imaginary attention's role" → KEPT.** The noise-ablation experiment is well-designed and provides strong causal evidence. Verified against Section 5.2.

- **Harsh critic: "Section 3.4 claims not supported by data" → DEMOTED and merged into Trivial.** The harsh critic says the claim "no longer suffer from the length extrapolation problem" is not supported. Actually, the paper doesn't make this unqualified claim — it says "these dimensions no longer suffer from the length extrapolation problem" in a specific technical sense about embedding range coverage, and the empirical results show RoPE++ does maintain more stable performance as context grows.

- **Harsh critic: "Fairer comparison would be against standard RoPE with equivalent KV-cache budget" → REMOVED.** The EH variant already compares against standard RoPE with full cache, showing EH matches or exceeds performance with half the cache. This is a favorable comparison for the baseline, not the proposed method, and thus falls under the rule about removing criticisms where the asymmetry favors the baseline.

- **Harsh critic: "Figure 5 should clarify where noise is injected (pre-/post-softmax)" → REMOVED as nitpick.** The experimental design is clearly described and the result is interpretable regardless.

- **Strength Finder: "The paper derives the characteristic curve" → KEPT.** Verified against Section 3.2 and Equation 5.

## Novel Insights

The key insight that distinguishes this paper is the observation that the imaginary component of RoPE's complex-valued attention, when viewed through its characteristic curve (a sine integral), naturally favors long-range dependencies — and that this theoretical property can be directly exploited by simply rotating queries by π/2 to produce a parallel set of attention heads. This is a clean, principled augmentation that preserves RoPE's desirable properties (unified absolute-relative format, compatibility with FlashAttention) while addressing a specific weakness. The noise-ablation experiment provides unusually direct causal evidence for a position-embedding paper, showing that the imaginary heads are not merely decorative but play a dominant role in long-context performance.

## Suggestions

- Reframe the motivation around "complementary projections" or "dual attention pathways" rather than "information loss." The current framing may confuse readers who understand that the real part already contains full information from the rotation perspective.
- Add a RoPE baseline with double the head count to strengthen the claim that EC's gains come specifically from the imaginary formulation, not just from increased capacity.
- Prioritize at least one experiment at 1B+ scale, even if with shorter training, to demonstrate that the benefits are not confined to sub-billion-parameter models.

## Score and Decision

**Calibration anchors used:**

Round 1 (bracketing):
| Anchor | Score | Comparison |
|--------|-------|------------|
| jp4pxKqCRW (Long-context Extrapolation via Periodic Extension) | 2.50 | Clearly weaker — rejected paper with limited contribution |
| 5dDYhvt6dY (Efficient transformer with reinforced PE) | 3.00 | Weaker — smaller scale, less novelty |
| JO7k0SJ5V6 (Scaling Laws of RoPE-based Extrapolation) | 5.00 | Comparable — stronger scale (7B/13B) but weaker eval (perplexity only); RoPE++ has better benchmarks but smaller models |
| GtvuNrk58a (Round and Round We Go!) | 6.20 | Slightly stronger — deeper mechanistic analysis, Gemma 7B study, but weaker eval benchmarks; RoPE++ has more comprehensive evaluation and a more actionable method |
| OhauMUNW8T (Wavelet-based Positional Representation) | 5.25 | Comparable — both have theoretical framing and empirical validation at moderate scale |
| OvoCm1gGhN (Differential Transformer) | 8.00 | Clearly stronger — more general contribution, larger scale, stronger results |

Round 2 (narrowing):
| Anchor | Score | Comparison |
|--------|-------|------------|
| eoln5WgrPx (STRING — Why Does Effective Context Length Fall Short?) | 6.50 | Stronger — works on 70B models, training-free, SOTA results |
| wXpSidPpc5 (CLEX — Continuous Length Extrapolation) | 6.50 | Stronger — 7B models, 4-8× extrapolation |
| 3Z1gxuAQrA (PoSE — Positional Skip-wise Training) | 6.00 | Slightly stronger — 7B scale, efficient context extension |
| VkqqZcofEu (Controlled Study on Long Context Extension) | 5.75 | Comparable — controlled protocol, standardization focus |

**Round 1 bracket:** 5.0 – 6.5

**Round 2 narrowing:** The paper sits below the 6.0–6.5 cluster (STRING, CLEX, PoSE — all operate at larger scale or with more immediately impressive results) and above the 5.0 anchor (Scaling Laws — stronger scale but weaker evaluation). It is most comparable to the 5.25–5.75 range (Wavelet-based, Controlled Study) but with better evaluation breadth than those papers. The comprehensive benchmark coverage, dual-configuration design, and causal ablation evidence place it at the upper end of this range.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>