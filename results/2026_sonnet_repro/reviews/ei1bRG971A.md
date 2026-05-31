Now let me run the calibration search to score this paper appropriately.Round 1 bracket: The paper appears to fall between **5 and 7**. Weak papers (2.5–3.0) in this space were straightforward token-skipping ideas. Strong anchors at 8.0 are more theoretically complete or comprehensive. Let me narrow within 5–7.Now I have enough calibration data to write the final review. Let me assess the anchors:

- **Layerwise Recurrent Router (5.75, accept)**: Small MoE models (36M parameters), limited benchmarks, minor gains. DND clearly exceeds this in scale and evaluation breadth.
- **Selective Attention (6.75, accept)**: Clean parameter-free mechanism, but evaluated on only one downstream task. DND has broader evaluation but a crucial missing ablation.

**Round 1 bracket: 5.0–7.0**
**Round 2 narrowing: 5.5–6.5** — DND's evaluation scope exceeds 5.75-class papers but is missing the core selective-vs-uniform ablation that would push it clearly above 6.25.

---

## Summary

Dynamic Nested Depth (DND) is a post-training method that inserts a token-selective re-processing pass through weight-shared transformer layers at the end of a standard forward pass. Identified critical tokens are compacted, given fresh positional embeddings, and re-run through the same layer, with outputs fused back via a normalized gating mechanism. Two novel training strategies—a push-pull router controlling loss and a buffer-proportional + EMA threshold control scheme—govern selection precision and stability. DND is validated post-training on three ~1B dense models and one 30B MoE model, achieving average gains of +1.88–+2.61 points on the dense models and +0.87 on the MoE model across up to 17 benchmarks.

---

## Strengths

1. **Consistent, non-trivial gains across four models**: Tables 1 and 2 show DND improves average performance by +1.88 (Qwen3-1.7B), +2.61 (Llama3.2-1B), +2.50 (Gemma3-1B), and +0.87 (Qwen3-30B-A3B) over full-scale SFT baselines on 11–17 benchmarks, with no benchmark showing consistent degradation. The gains on reasoning-heavy tasks are especially pronounced: BBH +5.02/+3.70/+4.69 and GPQA +5.80/+3.86/+5.30 across the three dense models.

2. **Ablations validate each training component**: Table 4 shows that removing both router controlling (RC) and threshold control (TC) degrades the average gain from +1.88 to +1.01 on Qwen3-1.7B; each component independently contributes partial gains, and their combination is needed for full improvement. This directly validates the paper's claim that the training strategy is essential.

3. **Negligible parameter and throughput overhead**: The method adds only 0.03M parameters (Section 4.3) and reaches 91.6–93.1% of the vanilla model's throughput across four input/decode length configurations (Table 3), confirming practical efficiency.

4. **Mechanistically grounded token selection analysis**: Figure 4b (r = −0.58) shows tokens more frequently selected by DND exhibit substantially greater entropy reduction after nested processing, providing the clearest causal evidence that the selected tokens genuinely benefit from additional computation.

5. **Threshold and ratio control visualized convincingly**: Figures 5, 6a, and 6b show quantitatively that the buffer proportional controller and EMA synchronization together suppress selection-ratio oscillations to within a 5% band, confirming the training strategy's stability.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing 100%-token uniform baseline — the paper's central thesis cannot be fully established.** DND's stated contribution is that *selective* reprocessing outperforms no extra processing. Table 4 ablates 10%, 20%, and 30% selection ratios but never tests 100% (i.e., running all tokens through the same weight-shared layer an extra time). This comparison is critical: if a uniform extra pass yields equivalent or better gains, the routing mechanism and its elaborate training strategies add complexity without benefit — the paper would simply be showing that one extra recurrent layer helps. The absence of this baseline leaves the paper unable to cleanly distinguish "selective routing is beneficial" from "any additional compute at this position helps." This is the most important missing ablation given the thesis.

- **Attention mechanism in the nested pass is architecturally under-specified.** Equation 3 describes `Pack`, new positional embeddings, and `Unpack`, but never states what selected tokens attend to during the nested pass: only each other in the compacted subsequence, all original sequence positions (full-context cross-attention), or a causal sub-mask derived from original positions. This is not a minor omission: choice (a) breaks causal structure, choice (b) dramatically increases memory beyond the 6% FLOPs claim in Section 4.3, and choice (c) requires non-trivial implementation. Without this specification, neither the computational overhead claim nor the quality of the "review" representation can be independently verified.

### Minor

- **Many individual 30B gains are marginal with no variance.** Table 2 reports single-run point estimates for Qwen3-30B-A3B: BBH +0.13, MATH +0.15, MATH-500 +0.20, DROP +0.27. AIME24 (+0.91) uses ~30 problems in pass@1 format, which itself has high per-run variance. Without any seed-variance or confidence-interval reporting on even a representative subset of these 17 benchmarks, the small-margin gains are not credibly established as signal rather than noise. The larger-gain entries (BFCL +2.05, C-Eval +1.83) are more credible, but the average of +0.87 is pulled up by those.

- **Notation inconsistency in Eqs. (6) and (7).** The score dispersion loss (Eq. 6) sums over layers $L_a$ to $L_c$, while the distribution preservation loss (Eq. 7) sums over $L_e$ to $L_r$ — four new subscripted symbols undefined relative to the architecture's $L_s$ and $L_e$. Whether each loss applies to all DND layers or a subset is left unclear, complicating reproducibility of the training strategy.

- **Ablation limited to Qwen3-1.7B.** Table 4 covers only Qwen3-1.7B for all training strategy variants. It is unconfirmed whether the same hyperparameter configuration (e.g., $\lambda_{\text{sd}}$, $\lambda_{\text{dp}}$, $\alpha$, $\gamma$, $k_{\text{target}} = 20\%$) transfers to Llama3.2-1B and Gemma3-1B or was independently tuned, making it unclear whether the +2.61 and +2.50 gains are robust across architectures or artifacts of per-model tuning.

- **ITT comparison is limited to one model.** The paper compares DND to ITT (Chen et al., 2025) only on Qwen3-1.7B (Table 1). The near-zero gain of ITT (+0.05) vs. DND's +1.88 is striking, but it is unclear whether this holds across Llama and Gemma or is specific to Qwen3.

### Trivial

- **r = 0.34 slightly overstated.** Section 4.5 characterizes the r = 0.34 correlation (Figure 4a) between selection frequency and logit entropy as validating that DND "preferentially selects tokens with greater uncertainty." At r = 0.34, the relationship is real but moderate; "preferentially" slightly overstates the strength of this evidence. The r = −0.58 result in Figure 4b is more compelling and carries the mechanistic argument.

---

## Nice-to-Haves

- Adding a 100%-token variant (all tokens re-processed through the same weight-shared layer) as a direct ablation column in Table 4 would be the single highest-leverage improvement. If DND at 20% matches or exceeds this, it validates both efficiency and the selection hypothesis. If the 100% variant wins, it reframes the contribution as showing that one recurrent layer with selective re-entry is a strong post-training signal — itself a finding worth reporting.
- Reporting 3-seed variance for a representative subset (e.g., 5 benchmarks) of the 30B experiments would immediately establish which small-margin gains are reliable.
- A routing score distribution histogram at training convergence (showing where scores actually land) would empirically resolve the theoretical tension between $\mathcal{L}_{\text{sd}}$ and $\mathcal{L}_{\text{dp}}$ and confirm the push-pull equilibrium the paper describes.
- Explicitly stating what selected tokens attend to during the nested pass — even in a single sentence — would make the method fully reproducible.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Push-pull objectives are in direct tension"**: Retained as a minor observation but not as a major weakness. The paper explicitly addresses this in Section 3.2.1: "Together, these two losses create a balanced 'push-pull' dynamic. The entropy-based dispersion loss pushes scores apart to cover a wider spectrum, while the MSE-based preservation loss pulls them collectively towards the responsive center." The functional purpose of each loss is clear enough, and Figure 3c illustrates the target behavior. The absence of an equilibrium analysis is a nice-to-have, not a flaw.

- **Training data under-disclosure**: The paper states hyperparameters and training settings are in Appendix Sec.B (stripped by the parser). The claim that both DND+SFT and vanilla SFT use identical data is consistent with the framing throughout; the generic description of the training set is not a methodological gap but a reproducibility nitpick.

- **Introduction motivation described as "loose"**: The connection to latent test-time scaling (Hao et al., 2024; Saunshi et al., 2025) is described in the introduction as inspiration, not equivalence. This is appropriate framing; the critic's concern is style, not substance.

- **Strengths filtered**: "DND targets an important problem" and similar generic framing was not carried forward. Only concrete, evidence-backed strengths are retained above.

---

## Novel Insights

The most mechanistically interesting contribution is the push-pull router training dynamic: $\mathcal{L}_{\text{sd}}$ prevents clustering that makes threshold-based selection brittle, while $\mathcal{L}_{\text{dp}}$ prevents sigmoid saturation that kills gradient flow at extreme selection ratios. Together with the EMA-synchronized buffer proportional controller, this produces what is, to the reviewer's knowledge, one of the more carefully engineered token-routing training pipelines in the post-training literature. The layer-wise visualization (Figure 7a–7b) suggesting that shallower DND layers select key entities while deeper DND layers select abstract relational tokens is a genuinely novel mechanistic observation that, if substantiated, implies the hierarchical processing of the nested pass is content-structured — not just uncertainty-driven.

---

## Suggestions

1. **Add a 100%-token DND variant in the ablation table** (or explain why this baseline is architecturally infeasible). This is the most critical experiment missing.
2. **Specify the attention mask inside the nested pass** (Section 3.1.2, after Eq. 3): do selected tokens attend only to each other, to the full original sequence, or to a causal sub-mask? A single clarifying sentence would resolve this.
3. **Report seed-level variance for a 5-benchmark subset on Qwen3-30B-A3B** to establish statistical credibility of the smaller-margin gains.
4. **Extend the ablation (Table 4) to at least one other architecture** (e.g., Llama3.2-1B), or explicitly confirm that the Qwen3-1.7B hyperparameters transfer unchanged.
5. **Extend the ITT comparison** to Llama3.2-1B and Gemma3-1B to isolate whether the architecture or the implementation quality drives the performance gap.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to DND |
|------|-----------|-------|-------------------|
| ulGwcj1egv (FiRST) | 3.00 | R1 (weak) | Much weaker: layer-skipping with limited results |
| 7DY2DFDT0T (EfficientSkip) | 2.50 | R1 (weak) | Much weaker: narrow contribution, few results |
| 6qUUgw9bAZ (How Hard to Think) | 6.50 | R1 (mid) | Comparable scope; that paper has cleaner theory, DND has broader empirical coverage |
| am5Z8dXoaV (LazyLLM) | 5.00 | R1 (mid) | DND has better evaluation breadth and a clearer training strategy |
| SYv9b4juom (OrthoRank) | 5.25 | R1 (mid) | DND has more comprehensive evaluation and post-training novelty |
| iOy2pITOoH (Spark Transformer) | 5.50 | R1 (mid) | Comparable: architectural idea at similar scale; DND has more models but one key ablation missing |
| OfjIlbelrT (FlexPrefill) | 8.00 | R1 (strong) | Much stronger: more rigorous theoretical grounding and comprehensive evaluation |
| eWNEqdH0vk (Layerwise Recurrent Router) | 5.75 | R2 | Weaker than DND: 36M parameter models, limited benchmarks |
| v0FzmPCd1e (Selective Attention) | 6.75 | R2 | Comparable: cleaner parameter-free mechanism, but evaluated on only 1 downstream task; DND has 4 models and 11–17 benchmarks |
| 8sSqNntaMr (RouteLLM) | 6.33 | R2 | Different application (routing between models); similar quality level |
| s3003xWtfd (CoreInfer) | 6.25 | R2 | Comparable: adaptive sparse activation, no post-training novelty angle |
| 0JjsZC0w8x (COrAL) | 5.75 | R2 | Similar borderline range; DND has stronger empirical validation |

**Bracket (Round 1):** 5.0–7.0
**Narrowed (Round 2):** 5.5–6.5

DND sits above the Layerwise Recurrent Router (5.75) and COrAL (5.75) due to significantly broader evaluation (4 real production-scale models, 11–17 benchmarks, clean ablations). It sits below Selective Attention (6.75) because that paper has a cleaner, self-contained contribution validated without an implementation gap, while DND has the critical missing 100%-token baseline and the unresolved attention-mechanism specification. The RouteLLM/CoreInfer cluster at 6.25–6.33 is the most apt anchor: DND has comparable polish and empirical scope, but the missing selective-vs-uniform ablation prevents the paper from fully substantiating its central thesis about the value of routing. 

**Final score: 5.5** — solid empirical contribution with consistent results across four models, but the missing ablation that validates selectivity over uniformity, paired with an under-specified architectural detail that affects both reproducibility and the FLOPs claim, keeps the paper at the lower end of the borderline range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>