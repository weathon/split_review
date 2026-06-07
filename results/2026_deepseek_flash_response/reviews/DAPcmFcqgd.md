Now I have all the context I need. Let me write the final review.

## Final Review: MoEP — Compact and Efficient Sparsity with Modular Expert Paths

---

## Summary
This paper proposes MoEP, a decoder-only architecture that introduces sparsity via top-k routing across parallel Transformer blocks and MoE-style linear projections, while keeping the total parameter count fixed at 28M (matching a dense GPT-2 baseline). The method is evaluated on the BabyLM strict-small track. The core architectural idea — using parallel blocks at reduced dimensionality with top-k routing to achieve sparsity without parameter inflation — is interesting and represents a genuinely different design trade-off from standard MoE. However, the paper suffers from a critical evidential gap: it motivates sparsity and efficiency but provides zero measurements of computational cost. The headline claim is also misleadingly framed. The evaluation is insufficient to support the paper's central thesis.

---

## Strengths

1. **Fixed parameter count with introduced sparsity, verified.** Table 2 confirms MoEP and GPT-2 both at 28M total parameters despite MoEP having 10 parallel layers × 4 blocks each with top-2 routing. Standard MoE (e.g., Mixtral, DeepSeek-R1) increases total parameters by the number of experts; this paper shows a design where sparsity is introduced without parameter overhead — a genuinely different design trade-off.

2. **Outperforms the matched GPT-2 baseline under controlled conditions.** Table 1 shows MoEP achieves macro average (excluding AoA) of 49.00 vs the paper's own GPT-2 at 48.10 and the official BabyLM GPT-2 baseline at 46.60. Since MoEP and GPT-2 share the same sublayer structure and total parameter count (28M), this is a clean apples-to-apples comparison showing that the added sparsity yields measurable gains.

3. **Evidence of faster early training convergence.** Section 5.1 and Appendix A.3 show MoEP reaches its peak fast-evaluation performance at 30M words versus MoEP-SwiGLU at 80M words, supporting the claim of better sample efficiency.

4. **Non-obvious finding from SwiGLU ablation.** The comparison between MoEP (linear projections, 28M params, macro avg 49.00) and MoEP-SwiGLU (SwiGLU-based experts, 38M params, macro avg 47.70) reveals that lightweight linear experts outperform a more expressive variant at small scale. This is a concrete, interesting finding.

5. **Careful experimental controls.** Shared training seed, pre-tokenized data with identical stride, epoch-based sampling ensuring all models trained on the same examples (Section 4, "Training Procedure"). The paper also trains its own GPT-2 reimplementation alongside the official baseline, providing two independent reference points.

---

## Weaknesses

### Major

1. **No efficiency metrics — the central claim is untested.** The paper's thesis is about sparsity and efficiency: "add sparsity while keeping the total parameter count fixed" (Abstract), enabling "compact models [to] still benefit from sparsity." Yet there is no measurement of activated parameters per token, FLOPs per forward pass, training/inference throughput, or memory consumption. Given the architecture (2 full-size layers + 10 parallel layers each routing top-2 of 4 blocks), the activated parameter count per token could be *higher* than GPT-2's dense pass through 12 layers — the paper neither confirms nor denies this. Without these measurements, the efficiency claim is purely rhetorical. This is the most serious weakness. (Verifiable from paper: nowhere in Sections 3–5 are any efficiency measurements reported.)

2. **Introduction overclaims the empirical results.** Line 31 states MoEP "was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well." Table 1 shows GPT-BERT (causal) achieves macro average (excluding AoA) of 54.10 vs MoEP's 49.00 — a clear discrepancy. While Section 5.1 correctly qualifies the claim ("when the AoA task score was included in the Macro Average"), the abstract and introduction do not. The paper's strongest framing is misleading.

3. **Load-balancing loss is unusual and unvalidated.** The balancing regularizer (Equation 2) uses negative entropy of routing probabilities: −Σ p_i log p_i, encouraging uniform probabilities. Standard MoE practice (Switch Transformers, DeepSeek MoE, ST-MoE) uses auxiliary losses based on the product of probability and actual token assignment fraction, or the coefficient of variation of expert loads. The chosen entropy-based loss encourages uniform probabilities but does not directly control *load balance* under discrete top-k assignment — a router could assign uniform probabilities yet have imbalanced token assignments due to argmax discretization. No ablation or comparison to standard alternatives is provided. (Verifiable from Section 3.4.)

### Minor

1. **No confidence intervals or variance estimates.** Results are reported as point estimates from a single run per configuration. For a small-scale study (BabyLM, ~10M words), this makes it impossible to assess whether the 0.9-point macro-average improvement over the paper's own GPT-2 (49.00 vs 48.10) is statistically significant.

2. **Routing mechanism is underspecified.** The paper states P=4 parallel blocks, top-k=2, and N=10 parallel layers from Table 2. But it never clarifies whether the top-k routing is applied independently per parallel layer (10 independent routing decisions per token) or globally. The effective computational graph — a token could follow 2^10 different paths — is not described, and no worked example is provided. (Verifiable from Section 3.3: "Linear router is shaped d_P × P and it applies a token-level top-k selection among the P Parallel Block" — but does not specify whether this happens per layer or globally.)

3. **No analysis of routing specialization.** Contribution 3 claims to "analyze expert networks routing behavior," but the only analysis is training dynamics (which tasks improve when across checkpoints). There is no analysis of which blocks different tokens are routed to, whether routing is consistent, or whether different blocks specialize in different linguistic phenomena. (Verifiable from Section 5 and Appendix A.3.)

4. **Checkpoint selection may introduce upward bias vs baselines.** The paper selects the checkpoint with best fast-evaluation performance (Section 4). The official BabyLM baselines are likely reported at a fixed checkpoint. The paper does not discuss whether the same selection procedure was applied to baselines, making the comparison potentially unfair.

---

## Removed Points
*These points were raised by reviewers but are removed as invalid, unreasonable, or addressed by the paper.*

- **"MoEP-SwiGLU undermines the narrative"** — The paper explicitly presents this as a finding ("lightweight simplicity is better than adding complexity," Contribution 4). The SwiGLU variant is clearly labeled with 38M params in Table 2; it is an ablation, not the primary claim.
- **"Layer-level expert networks remain a relatively unexplored area is overstated"** — The paper cites MoLE and PaPaformer as prior work in this area. "Relatively unexplored" is a fair characterization given how few works exist.
- **"Checkpoint selection inflates results" as a major issue** — The paper's own GPT-2 uses the same procedure, so the primary comparison (MoEP vs paper's GPT-2) is fair. The concern applies only to cross-paper comparisons with HF baselines, which is a minor issue.
- **Specific formatting/grammar nitpicks** — These are parser artifacts, not author errors.
- **Missing appendix content** — Appendices are stripped by the parser; they exist in the original submission.

---

## Nice-to-Haves

- Report activated parameter counts and FLOPs per token for GPT-2, MoEP, and MoEP-SwiGLU.
- Ablate the contribution of parallel block routing vs. MoE shrink/grow separately (e.g., dense ensemble of parallel blocks without routing; standard MoE on FFN without parallel blocks).
- Compare entropy-based load balancing to standard Switch Transformer-style auxiliary loss.
- Run multiple seeds and report confidence intervals.
- Analyze which parallel blocks/expertise handle which linguistic patterns.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add a table of efficiency metrics** (activated parameters per token, FLOPs, throughput) comparing GPT-2 dense, MoEP, and MoEP-SwiGLU. This is the single most important addition, without which the core thesis is untestable.
2. **Correct the framing.** Position MoEP as "outperforms a matched-parameter GPT-2 baseline" rather than "outperforms all baselines including GPT-BERT." The Section 5.1 qualification ("when AoA is included") should appear in the abstract and introduction.
3. **Validate the load-balancing loss.** Add an ablation comparing the entropy-based regularizer to the standard Switch Transformer auxiliary loss, showing that it prevents expert collapse equivalently or better.
4. **Clarify the routing mechanism.** State explicitly whether top-k=2 is applied independently per parallel layer or globally. Provide a worked example tracing a single token through the architecture.
5. **Report variance.** Run 3+ seeds and report means with standard deviations or confidence intervals, especially for the primary comparison (MoEP vs GPT-2).

---

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NanoMoE (04RLVxDvig.md) | 3.00 | R1 | Rejected. Missing efficiency metrics, toy experiments only. Our paper has stronger evaluation (BabyLM) and clearer architecture. |
| MOEfication (762u1p9dgg.md) | 3.40 | R1, R2 | Rejected. Same gap (no wall-clock/efficiency measurements for an efficiency-motivated paper). Our paper is somewhat better: cleaner architectural idea, controlled experiments. |
| LokiLM (bppG9srkpR.md) | 3.60 | R2 | Rejected. Lacked scientific insight; kitchen-sink approach. Our paper has clearer contributions. |
| Learning Parameter Sharing (tGsumqfOUk.md) | 4.75 | R2 | Rejected. Incremental contribution but thorough experiments. |
| Studying SLM Effects (4xBew7kuYB.md) | 5.50 | R2 | Rejected. Narrow scope but well-executed. |
| MoLEx (rWui9vLhOc.md) | 6.33 | R1, R2 | Accepted. Measured and discussed efficiency trade-offs, had theoretical grounding. Our paper lacks comparable rigor. |
| Merge-Then-Compress (eFWG9Cy3WK.md) | 6.33 | R2 | Accepted. Clear measured efficiency gains (80% memory, 20% FLOPs reduction). Our paper's efficiency claims are untested by comparison. |
| OLMoE (xXTkbTBmqq.md) | 8.67 | R1 | Accepted. Industry-scale release with comprehensive analysis. Not in the same category. |

**Round 1 bracket:** 3.0 – 6.33. The paper is below MoLEx and Merge-Then-Compress due to missing efficiency validation, but above NanoMoE/MOEfication due to cleaner architecture and standardized evaluation.

**Round 2 narrowing:** The closest comparator is MOEfication (3.40), which was rejected for the same structural flaw (claims efficiency without measuring it). Our paper has a more original architectural idea and cleaner experiments, placing it slightly higher but still below Learning Parameter Sharing (4.75) which had more thorough empirical validation. The final score of 4.0 reflects a paper with genuine potential that is not yet ready for a top venue.

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>