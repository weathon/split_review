Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper identifies that Mamba's inability to generalize to long contexts stems from out-of-distribution (OOD) discretization steps Δ_t, which grow with context length and cause excessive forgetting of early tokens. To address this, the authors propose MambaExtend, which calibrates per-layer (or per-channel) scaling factors on Δ_t via either gradient-based (CF_BP) or zeroth-order SPSA (CF_ZO) optimization while freezing all model weights. The method achieves up to 32× context extension (2k→64k) with minimal perplexity degradation and orders-of-magnitude fewer parameter updates than fine-tuning alternatives like DeciMamba.

## Strengths

1. **Identification of OOD discretization steps as the root cause of Mamba's long-context failure**: Section 3 (Fig. 2) empirically demonstrates that accumulated Δ_t grows with context length and that larger Δ_t causes stronger forgetting of earlier tokens via the exp(−∑Δ_t) term in the recurrence. This insight is novel for Mamba models and cleanly motivates the scaling strategy, distinguishing the work from transformer-based approaches that focus on positional embeddings.

2. **Training-free (weight-freezing) calibration with orders-of-magnitude fewer parameter updates**: MambaExtend optimizes only per-layer scaling factors (L scalars or D per-channel) while freezing all weights. The paper reports up to ~5.42×10⁶× fewer parameter updates and 3.87× lower peak memory vs. DeciMamba (Fig. 6, Section 5.3), a concrete efficiency gain over full fine-tuning.

3. **Achieves up to 32× context extension with minimal perplexity degradation**: On PG-19 (Fig. 4), MambaExtend-130M yields PPL of 30.62 vs. 995,328 for the pre-trained model at 70k context. On Pile (Table 1), PPL improves by up to ~8145×. These results directly support the central claim of effective training-free extension.

4. **Zeroth-order optimization (SPSA) demonstrated to match backpropagation**: Table 4 shows that CF_ZO achieves perplexity nearly identical to CF_BP on Pile, while enabling even greater memory savings (Section 5.3). This makes the method practical for resource-constrained settings.

5. **Passkey retrieval results with far fewer calibrated parameters**: In Fig. 5, MambaExtend calibrates ~3500× and ~7100× fewer parameters than fine-tuning for Mamba-130M and Mamba-1.4B respectively, yet achieves comparable or better retrieval accuracy. This highlights the effectiveness of targeting Δ_t scaling alone.

## Weaknesses

### Fatal
None.

### Major
- **Claimed Mamba2 evaluation absent from experiments**: The abstract and introduction state that MambaExtend is evaluated on "different Mamba and Mamba2 variants" (line 18). Yet all reported experiments use only Mamba-130M and Mamba-1.4B — these are Mamba-1 models. No Mamba2 results appear in any table or figure. Given that Mamba2 uses a different S6 formulation (with different discretization), it is non-trivial to assume transfer. The paper's stated scope includes Mamba2, but the evidence does not. The authors must either include Mamba2 results or retract the claim.

### Minor
- **No direct head-to-head comparison against the best uniform scaling factor**: Fig. 3 shows that a single global scaling factor reduces PPL from ~268 to ~23.5 at 32k on Pile. The paper's argument that per-layer scaling is needed is well-motivated by Fig. 2 (heterogeneous ∑Δ_t across layers), but the reader cannot quantitatively judge the incremental benefit of MambaExtend over the best optimized uniform s. Adding this comparison (e.g., overlaying the best uniform s line on Fig. 4 or reporting it in Table 1) would cleanly justify the per-layer complexity.

- **Missing DeciMamba comparison on LongBench**: Table 2 reports Mamba vs. MambaExtend on LongBench but omits DeciMamba, which is the only existing Mamba context-extension method. Since DeciMamba comparisons appear for perplexity (Fig. 4) and passkey (Fig. 5), the absence on LongBench is a noticeable gap that would contextualize the claimed 6.03% improvement.

- **Passkey retrieval baseline may be under-explored**: The paper fine-tunes Mamba and DeciMamba for only one epoch (line 113: "as we get significant failure in the retrieval"). The phrase is ambiguous about whether longer training was attempted. If one epoch was chosen because more epochs caused overfitting/degradation, that should be stated explicitly with evidence. If multiple epochs were not tried, the claimed up to 20% accuracy advantage could partly reflect undertrained baselines.

- **No analysis of why different scaling granularity is needed for different tasks**: Table 3 shows per-channel scaling dramatically outperforms per-tensor for passkey retrieval, while per-layer (tensor) suffices for perplexity. The paper presents this as a finding but offers no discussion of why retrieval demands finer granularity. Understanding this distinction would strengthen the method's design principles.

### Trivial
- The "8145× improvement" ratio (Fig. 1, Table 1 caption) compares against the pre-trained model's extremely high PPL (~10⁶ at long contexts). While dramatic, this ratio is inflated by the denominator's magnitude. Supplementing with absolute PPL values or log-scale comparisons would be more informative.

## Nice-to-Haves
- **Analyze the learned scaling factors themselves**: Showing which layers get large vs. small scaling values and whether the pattern aligns with the ∑Δ_t accumulation in Fig. 2 would deepen the causal story and help the community understand Mamba's long-context failure mode.
- **Wall-time comparison of CF_ZO vs. CF_BP**: Since the number of parameters is tiny, backpropagation may already be cheap; showing whether ZO offers practical speed/memory advantages in this low-parameter regime would be useful.
- **Clarify the "training-free" terminology**: The paper uses "training-free" to mean no gradient updates to model weights (which is accurate in context), but adding a brief clarification (e.g., "weight-freezing calibration") would prevent potential confusion.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

1. **"Insufficient description of calibration optimization pipeline" / "Section 4 content missing"**: The parsed text jumps from a brief Section 4 to Section 5.2. This is almost certainly a parser truncation artifact — the original paper likely contains full algorithmic descriptions of CF_BP and CF_ZO. The remaining text already describes SPSA (line 18), calibration samples (line 96), and per-layer scaling factors (line 89), providing enough methodological context. Removed as a parser artifact.

2. **"'Training-free' is misleading"**: The paper explicitly clarifies that model weights are frozen and only scaling factors are calibrated (abstract, line 4; Section 4, line 89). The usage is consistent with the literature where "training-free" refers to no weight updates. Removed as factually inaccurate — the paper does not claim zero data or computation.

3. **Pure formatting/style nitpicks**: Any criticisms about typographical issues, figure/table placement, or missing punctuation are parser artifacts, not author errors.

## Novel Insights

The overall pattern across reviews reveals a paper whose core contribution — calibrating per-layer Δ_t scaling factors for Mamba's long-context extension — is empirically promising and computationally elegant. The most notable tension is that the method's incremental improvement over a much simpler uniform scaling baseline appears modest on perplexity (~22 vs. ~23.5 PPL at 32k), while its advantage is more striking on passkey retrieval (where per-channel scaling matters). This suggests the true contribution may not be "per-layer vs. uniform" per se, but rather "targeted calibration of Δ_t with appropriate granularity for the task" — a more nuanced claim than the paper currently emphasizes. The missing Mamba2 evaluation is a concrete gap between stated and delivered scope that needs resolution.

## Suggestions

1. **Include Mamba2 results** to match the paper's stated scope. Even a single perplexity table at two model sizes would significantly strengthen the generality claim.
2. **Add a direct comparison to the best uniform scaling factor** from the Fig. 3 grid search, either by overlaying on Fig. 4 or reporting in Table 1. This will cleanly quantify the benefit of per-layer calibration.
3. **Add DeciMamba results to the LongBench table** (Table 2) for a complete comparison.
4. **Clarify the passkey retrieval baseline tuning**: explicitly state whether more than one epoch was attempted and why one epoch was chosen.
5. **Discuss the task-dependent granularity finding** (per-layer for perplexity vs. per-channel for retrieval) — what does retrieval require that perplexity does not?
6. **Supplement the 8145× ratio** with absolute PPL values or log-scale plots for a more informative comparison.

## Score and Decision

The paper presents a simple, well-motivated, and demonstrably effective approach to extending Mamba's context length. The core finding — that scaling Δ_t alone, without any weight updates, enables up to 32× context extension — is novel and practically valuable. The efficiency gains over fine-tuning (orders of magnitude fewer parameter updates, significantly lower memory) are convincingly documented. However, the paper suffers from one major gap: Mamba2 results are claimed in the scope but absent from the experiments, and several secondary comparisons (best uniform scaling baseline, DeciMamba on LongBench) are missing. These are addressable but need to be resolved. The strengths outweigh the weaknesses, and the contribution is meaningful for the SSM community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>