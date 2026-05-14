Now I have sufficient calibration context. Let me write the final consolidated review.

---

## Summary

This paper identifies that standard RoPE discards the imaginary component of the complex-valued attention score and proposes RoPE++, which re-incorporates it as a separate group of attention heads. Two configurations are introduced: RoPE++EC (equal KV cache, doubled attention heads) and RoPE++EH (equal head count, halved KV cache). Mathematical analysis shows the imaginary attention follows a sine-integral characteristic curve that decays more slowly than the cosine-integral curve of real attention, suggesting natural suitability for long-range dependencies. Experiments at 376M, 776M, and 1.5B scales on RULER and BABILong benchmarks show RoPE++EC consistently outperforms vanilla RoPE at the same cache cost, while RoPE++EH achieves comparable results with half the cache.

## Strengths

- **Identifies an overlooked source of information in RoPE**: The paper points out that standard RoPE keeps only the real part of the complex-valued attention score (Equation 1) and shows the discarded imaginary part can be recovered by a simple −π/2 rotation of queries (Equation 3–4). This is a genuinely novel insight that prior work on RoPE improvement has missed. The mathematical derivation is clean and enables efficient implementation through the same FlashAttention kernel.

- **Proposes two practical configurations with clear trade-offs**: RoPE++EH halves KV cache and QKV parameters while keeping head count fixed, and RoPE++EC doubles heads at the same cache cost. The paper verifies these trade-offs with memory and throughput measurements (Figure 4). At 776M, RoPE++EH achieves RULER avg 28.6 vs RoPE's 27.4 (better) while using half the cache — a meaningful efficiency result. RoPE++EC delivers consistent gains at the same cache cost (376M: RULER 25.0 vs 18.8; 776M: 29.4 vs 27.4).

- **Validates at multiple scales with consistent trends**: Experiments span 376M, 776M, and 1.5B parameters. Training loss curves (Tables 7–9) show RoPE++ converges without stability issues. The method is also shown to be compatible with existing context-extension techniques (YaRN, Linear PI) in Table 3, demonstrating it is orthogonal to standard interpolation methods.

- **Theoretical analysis of length extrapolation improvement**: Section 3.4 and Figure 3 provide a concrete argument that RoPE++ exposes certain dimension pairs to both positive and negative position embedding values during training (via the imaginary attention), unlike vanilla RoPE where they only see non-negative values. Perplexity curves in Figure 6 verify that RoPE++ perplexity rises more slowly beyond the training length.

## Weaknesses

### Fatal
None.

### Major

1. **Head-count confound for RoPE++EC isolates imaginary-attention benefit ambiguously.**  
   RoPE++EC doubles the number of effective attention heads relative to vanilla RoPE at the same KV-cache cost. The paper attributes the gains to "imaginary attention," but a controlled baseline — standard RoPE with twice the attention heads (and the same KV cache, achieved by grouping more query heads to the same KV heads) — is not included. Without this, it is unclear how much of the improvement comes from the imaginary component versus simply having more attention heads operating on the same keys/values.  

   This concern is partially mitigated by RoPE++EH (same head count, half cache), which shows that imaginary attention alone can match or exceed vanilla RoPE. However, RoPE++EH is not a clean ablation either: it halves the number of KV heads, changing the representation capacity. The central claim that "imaginary attention specifically enhances long-context modeling" would be substantially strengthened by a controlled experiment where the number of heads is varied independently of the imaginary component.

2. **Noise experiment (Section 5.2) has a methodological flaw that undercuts its conclusion.**  
   The paper adds Gaussian noise of equal standard deviation to the *pre-softmax* attention scores of real vs. imaginary heads and concludes that imaginary attention plays "a more dominant role" because its perturbation degrades RULER scores more. However, real attention scores are systematically larger in magnitude for nearby tokens (due to the cosine-based characteristic curve), while imaginary scores are smaller (especially at small distances). Adding noise of equal σ to both therefore produces a lower signal-to-noise ratio for the imaginary scores, making them more disrupted regardless of their functional importance. A proper ablation would zero out the imaginary heads entirely (or remove them) and compare against a same-head-count baseline with all heads using standard RoPE. The current experiment does not establish dominance; it likely measures the noise susceptibility of smaller-magnitude scores.

3. **Unexplained regression on BABILong at 1.5B scale.**  
   At 1.5B (Table 6), RoPE++EC achieves RULER avg 37.5 vs RoPE's 35.1 (improvement) but BABILong avg drops to 22.9 vs RoPE's 29.5 (a 6.6-point regression). The paper does not acknowledge or hypothesize about this negative result. Since the pattern does not appear at 376M or 776M (where RoPE++EC outperforms on both benchmarks), this suggests the method may interact with scale in ways the current analysis does not account for. This is a significant gap in an otherwise thorough empirical evaluation.

### Minor

1. **The theoretical link between pre-softmax characteristic curves and post-softmax attention patterns is incomplete.**  
   The paper shows that the expected pre-softmax imaginary score follows a sine-integral that decays slowly (Figure 1), but attention weights are determined by *relative* magnitudes after softmax normalization. Because real attention produces high scores at small distances and imaginary attention produces near-zero scores at small distances, the combined softmax output may still be dominated by local real attention. The paper does not provide a theoretical or simulation-based analysis of how the two characteristic curves interact under softmax normalization. The anecdotal attention maps in Figure 5 (showing 2 heads per model) are insufficient to establish that imaginary heads systematically attend to longer ranges — a systematic average attention distance computation over all heads and layers is needed.

2. **The noise injection experiment is underspecified.**  
   It is unclear whether noise was added to the logits (pre-softmax), to the attention weights (post-softmax), or to the attention output. The y-axis label in Figure 5 says "score" without defining whether this is the RULER-4k average (range 0–100) or something else. The text says "Gaussian noise with equal standard deviation" but does not specify whether the noise was added to individual attention entries or to the entire head's output. This makes the experiment difficult to reproduce.

3. **Section 3.2 notes that imaginary attention scores are zero at zero distance** (since sin(0)=0), meaning the imaginary component cannot distinguish identical tokens from dissimilar ones at the same position. The paper does not discuss whether this fundamental difference from real attention has any practical implications, such as for the first token in a sequence or for positions where content is most important.

## Nice-to-Haves

- A controlled baseline that doubles the number of KV heads (not just query heads) using standard RoPE, to match the head count of RoPE++EC while keeping the same cache cost. This would cleanly isolate the imaginary component's contribution.
- A post-softmax attention distance analysis (mean attention distance over all heads and layers across multiple prompts) to quantitatively verify that imaginary heads attend to longer contexts.
- An alternative ablation for the noise experiment: zero out imaginary/real attention entirely rather than perturbing by equal-σ noise.
- Discussion of why BABILong performance regresses at 1.5B for RoPE++EC, even as RULER improves.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"RoPE++EH halves the head count"** (Harsh Critic, Issue 1): Factually incorrect. The paper explicitly states RoPE++EH "keeps equal attention head number" (lines 78–79, 677–678). It halves *KV cache and QKV parameters*, not the number of heads.
- **"RULER avg 22.9 vs 29.5 for RoPE"** (Harsh Critic, Tables 5–9 section): The 22.9 is the *BABILong* average for RoPE++EC, not RULER. Table 6 shows RoPE++EC RULER avg is 37.5 (vs RoPE 35.1, which is better). The underlying concern about BABILong regression at 1.5B is valid and kept above.
- **"Imaginary-only ablation" request** (Harsh Critic, Missing Experiments #2): The paper explicitly states this is architecturally impossible (lines 688–692): "imaginary attention is defined relative to real attention and cannot exist independently. Therefore, configurations such as 75% imaginary vs. 25% real or 100% imaginary... are impossible under RoPE++."
- **"Section 3.2 shows imaginary cannot distinguish identity from dissimilar at zero distance — not discussed"** (Harsh Critic, Section-by-Section Notes): This is indeed discussed — the paper says "modeling distance with sin(θΔt) is counter-intuitive, since sin(θΔt) is zero at zero relative distance, rises, then falls" (lines 451–453). The property is acknowledged, not hidden.
- **Strength Finder point 3** (noise experiment as strong causal evidence): Overstated. Given the methodological flaw (equal-σ noise on smaller-magnitude imaginary scores), this experiment does not constitute reliable causal evidence. The underlying claim may still be true, but this specific experiment does not convincingly demonstrate it.

## Novel Insights

The two major confounds — head-count increase and flawed noise experiment — interact in an interesting way. The EH configuration (equal heads, half cache) shows that even when head count is held constant, using imaginary attention can match or exceed vanilla RoPE's performance with half the cache. This suggests the imaginary component *is* contributing real value, but the mechanism may be more about efficient allocation of a fixed parameter/cache budget than about the sine-integral characteristic curve per se. The paper's theoretical framing (slower-decaying sine integral) implies imaginary attention is better at long ranges, but the EH results could equally be interpreted as a form of representational efficiency: imaginary heads pack useful positional information into half the KV parameters. Neither the theoretical nor the experimental analysis currently distinguishes these two (not mutually exclusive) mechanisms, and future work could benefit from disentangling them.

## Suggestions

1. **Add a controlled ablation for RoPE++EC**: Train a baseline that uses standard RoPE with the same number of query heads as RoPE++EC and the same KV cache configuration. If the imaginary-attention version outperforms this baseline, the contribution is cleanly isolated.
2. **Report mean attention distance** over all heads (real and imaginary) to systematically support the claim that imaginary heads attend globally.
3. **Address the 1.5B BABILong regression**: Provide a hypothesis or analysis (e.g., does BABILong's specific reasoning pattern interact differently with imaginary attention at larger scales?).
4. **Fix the noise experiment**: Either use a signal-to-noise-ratio matched perturbation, or simply zero out the imaginary heads and report the performance drop relative to a same-head-count standard RoPE baseline.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| MrRoPE (1J63FJYJKg) | 6.50 | Stronger unified theory and training-free method; this paper has a more novel architectural insight but weaker experimental isolation |
| Frayed RoPE (W8ZXfNaqku) | 6.00 | Cleaner causal analysis with geometric perspective and a training-free fix; this paper has more extensive pretraining experiments but less clean attribution |
| Probing RoPE through FE (1JZuEDq62N) | 6.00 | Diagnostic paper with no method improvement; this paper has a practically useful architectural contribution |
| Frequency Bands in RoPE (PR1PPxvG9Q) | 5.20 | Analysis paper with limited practical impact; this paper proposes an actual architectural change with positive empirical results |
| Selective RoPE (AQo1SEElNb) | 4.50 | Similar scale of experiments (370M–1.5B), similar methodological concerns about validation; this paper is slightly better evidenced |
| PoPE (kf2mzS6xfk) | 4.00 | Also a RoPE improvement with limited evaluation and missing baselines; this paper has more experiments across more scales |
| HHPE (5eg1Ii0Nx6) | 1.50 | Withdrawn paper with poorly motivated claims; this paper is far more rigorous |

**Score rationale**: The paper identifies a genuinely novel architectural modification to RoPE, provides clean mathematical derivations, and shows consistent improvements on long-context benchmarks at 376M and 776M. However, two major methodological issues prevent a higher score: (a) the lack of a head-count controlled ablation for RoPE++EC makes it unclear whether gains come from imaginary attention or simply from more attention heads, and (b) the noise experiment intended to demonstrate imaginary attention's importance has a built-in confound that undermines its conclusion. The unexplained 1.5B BABILong regression further weakens the empirical picture. These issues are addressable but not resolved in the current submission. Compared to the anchors, the paper sits between the stronger RoPE-extension papers (MrRoPE at 6.50) and the weaker ones with incomplete validation (Selective RoPE at 4.50, PoPE at 4.00).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>