Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proposes RoPE++, which recovers the discarded imaginary component of the complex-valued dot product in Rotary Position Embeddings (RoPE) and deploys it as a parallel set of attention heads. The authors provide a clean mathematical derivation showing that the imaginary attention corresponds to a fixed −π/2 rotation of query vectors, present two architectural configurations (EH: equal heads, halved KV cache; EC: equal cache, doubled heads), and demonstrate improvements on short- and long-context benchmarks at 376M and 776M scales. The core insight — that the imaginary part of RoPE has been overlooked and may preferentially model long-range dependencies — is genuinely novel and well-motivated.

## Strengths

- **Novel and well-motivated idea**: The observation that standard RoPE discards the imaginary component of the complex-valued attention score is precise and specific. The derivation that the imaginary attention corresponds to a fixed −π/2 rotation of query vectors (Equation 4) is clean and practical. To my knowledge, this specific gap has not been identified or exploited in prior work.

- **Principled theoretical motivation for long-range modeling**: The characteristic-curve analysis (Section 3.2) deriving the sine-integral decay of imaginary attention provides a mathematical rationale for why this component should help with long-context dependencies — the curve decays much more slowly than the cosine-integral of real attention.

- **Clean controlled comparison via EH configuration**: RoPE++_EH keeps the same number of attention heads as standard RoPE while halving KV cache and QKV parameters. It still achieves comparable or better performance (e.g., 776M short-context average 42.5 vs. RoPE 42.0; 776M long-context 42.0 vs. 41.3), providing evidence that the imaginary component contributes independently of any head-count changes.

- **Comprehensive evaluation across baselines and context-extension methods**: The paper compares against RoPE, FoPE, Pythia, and ALiBi on both short- and long-context benchmarks, and further shows compatibility with Linear PI, YaRN, and NTK-aware scaling for long-context training (Table 3).

## Weaknesses

### Fatal

None.

### Major

- **RoPE++_EC head-count confound is not controlled**: RoPE++_EC doubles the number of attention heads relative to standard RoPE (as the paper itself states in Section 3.3). The paper provides no baseline that matches this increased head count while using ordinary RoPE. While the QKV parameter budget is held fixed (query dimensions are halved, key dimensions doubled), the change in head count alters the inductive bias of the architecture. The large gains attributed to EC on long-context tasks (e.g., RULER average 25.0 vs. 18.8 at 376M in Table 2) cannot be fully attributed to the imaginary component — some fraction may reflect the change in attention-head structure. The EH configuration partially addresses this (it has equal heads and still shows gains), but the paper's strongest claims rest on EC results and do not acknowledge this confound. A RoPE baseline with doubled heads (or an ablation that disables imaginary heads within the EC architecture) would resolve this.

### Minor

- **Noise-injection experiment lacks scale normalization**: Section 5.2 adds Gaussian noise with equal standard deviation to real and imaginary attention logits. If the two sets of logits have different magnitude scales, equal absolute perturbation does not imply equal perturbative impact. The qualitative conclusion (imaginary heads are more important for long-context) is supported by the attention heatmaps and the continuous noise-sweep curves, so this does not threaten the core claim, but the experiment would be more convincing with a scale-normalized perturbation (e.g., matching the pre-softmax variance).

- **Single-run pre-training without variance characterization**: All results are from single training runs. Pre-training at this scale is expensive, and the field norm is to report single runs, so this is not a serious flaw. However, some short-context differences are small (e.g., 40.3 vs. 40.1 average at 376M), and long-context differences for EH are sometimes within a few points of RoPE (e.g., RULER 376M: 18.2 vs. 18.8). The larger differences on EC (e.g., +6.2 on RULER at 376M) are unlikely to be noise, but the EH results would benefit from a variance estimate to strengthen the claim.

- **Length-extrapolation benefit is argued theoretically but not directly tested**: Section 3.4 argues that exposing dimensions to both cos and sin value ranges should improve length extrapolation, but no perplexity-vs-length curves without additional long-context training are provided. The long-context evaluation in Table 2 does show gains at 64k (beyond the 32k training length), which is suggestive, but a direct extrapolation curve would be more compelling.

### Trivial

- Figure 4 caption says "higher TPOT" when lower time-per-output-token would be the efficiency gain (the figure itself correctly shows this — just a caption wording issue).
- The description of EC/EH architectures in Section 3.3 could be clearer about the mapping between Q/K/V dimensions and head counts to aid reproducibility.

## Nice-to-Haves

- An ablation within the EC architecture that disables or masks the imaginary attention heads (forcing their contribution to zero) would directly quantify the imaginary component's contribution without architectural confounds.
- A comparison with a RoPE model that simply doubles the number of attention heads (without imaginary extension) would isolate the head-count effect from the imaginary-component effect.
- A direct length-extrapolation perplexity curve (without additional long-context training) to validate the Section 3.4 argument.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper provides no baseline that matches this increased head count while using ordinary RoPE"** — Actually, this is a valid criticism and is KEPT as a Major weakness (see above). The harsh critic correctly identifies a genuine confound.

- **"All training and evaluation are based on single runs; no standard error, confidence intervals, or multi‑seed replication is reported"** — Kept as a Minor weakness because it is factually correct, but downgraded from the harsh critic's framing as a "critical issue." Single-run pre-training is standard in this subfield due to computational cost.

- **"Gaussian noise with identical standard deviation is added to the real and imaginary attention logits... The two sets of logits may have different magnitude scales"** — Kept as Minor. The point is technically correct but the continuous noise sweep at multiple σ levels provides qualitative evidence even without normalization.

- **"The characteristic-curve argument... does not constitute a guarantee about actual attention patterns"** — Removed. This is a strawman; the paper presents this as an approximate heuristic, not a formal guarantee, and follows it with empirical validation.

- **"The description of the two configurations is confusing. Figure 2b is labelled 'RoPE++ EC' but shows a structure with doubled query heads and halved key heads..."** — Removed. The paper consistently describes EC as doubling attention heads with equal cache, which is exactly what Figure 2b shows. The description is clear.

- **"No direct long-context perplexity curves without additional training are provided"** — Kept as Minor. The paper does make a theoretical claim about extrapolation that could be tested more directly.

- **"Does not match the textual claim of equal cache size"** — Removed. Figure 2b clearly shows halved key heads sharing one value head, which yields equal cache size. The critic appears to have misread the figure.

- **"The definition of 'attention head number' and the mapping to QKV parameter budgets remain ambiguous"** — Removed. The paper explicitly states that EC doubles head count and EH halves parameters, which is sufficient.

- **Strength Finder: "this paper is well motivated"** — Removed as too generic.

- **Strength Finder: "the idea is elegant"** — Removed as too generic; the specific strengths above capture the substance.

- **Strength Finder: "the paper identifies a previously overlooked source of signal"** — Kept in substance under the first strength bullet.

## Novel Insights

The key novel insight — that the imaginary part of RoPE's complex-valued attention encodes a −π/2 rotation of query vectors and has fundamentally different distance-decay characteristics (sine integral vs. cosine integral) — is genuinely original and well-supported. The observation that this imaginary component survives in the computation but is systematically discarded is specific enough to be actionable. What makes this more than a mathematical curiosity is the demonstration that an architecture with equal head count (EH) can match or beat standard RoPE with half the KV cache, suggesting the imaginary component carries complementary positional signal rather than being redundant with the real part.

## Suggestions

- Add a RoPE baseline with doubled attention heads (matching EC's head count) to cleanly separate the imaginary-component contribution from the architectural change. This is the single most important addition.
- Normalize the noise perturbation in Section 5.2 to control for differences in logit scale between real and imaginary heads (e.g., match pre-softmax variance).
- Provide a direct length-extrapolation perplexity curve (without long-context training) to validate the Section 3.4 claim.
- Consider reporting bootstrap confidence intervals over evaluation examples for the key results, which is inexpensive and would strengthen the EH comparisons where margins are smaller.

## Score and Decision

**Anchor comparison:**

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| D0u0glT060 | Deconstructing Positional Information | 7.20 | Deeper theoretical analysis, more polished, stronger paper overall |
| 1J63FJYJKg | MrRoPE | 6.50 | Unified framework, training-free, stronger empirical results at larger scale |
| W8ZXfNaqku | Frayed RoPE | 6.00 | Similar structure (analysis+method+experiments), similar scale, cleaner contribution without confound |
| AQo1SEElNb | Selective RoPE | 4.50 | Weaker LM experiments, limited scale; RoPE++ has more comprehensive evaluation |
| kf2mzS6xfk | PoPE | 4.00 | Missing key benchmarks; RoPE++ has better empirical coverage |
| RlPVSeKjoc | DroPE | 3.50 | Very small scale (0.5B), weaker experimental rigor; RoPE++ is clearly stronger |

RoPE++ sits between Frayed RoPE (6.0) and Selective RoPE (4.50). It has a more novel core insight than either, and more comprehensive experiments than Selective RoPE. The EC head-count confound is a real issue that Frayed RoPE does not have, which pulls RoPE++ below 6.0. But the EH configuration provides a clean comparison that Selective RoPE lacks, keeping it above 4.50. I calibrate to **5.5**.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>