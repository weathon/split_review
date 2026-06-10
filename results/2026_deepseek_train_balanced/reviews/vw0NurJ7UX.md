## Summary

This paper introduces PrefixQuant, a method that identifies high-frequency outlier tokens from calibration data and prefixes them in the KV cache during LLM inference, thereby eliminating token-wise outliers and enabling per-tensor static activation quantization to work effectively. The key contribution is demonstrating that static quantization (with prefixing) can match or outperform per-token dynamic quantization methods like QuaRot across multiple model families and quantization precisions (W4A4KV4, W4A8KV4, W8A8KV8), while offering substantial inference speedups (1.2×–1.3× over QuaRot, 1.6×–2.8× over FP16). The method is lightweight (12 seconds to configure vs. 12 hours for CushionCache) and does not require retraining.

## Strengths

- **First demonstration that per-tensor static quantization can outperform per-token dynamic quantization on LLMs**: On Llama-3-8B W4A4KV4, PrefixQuant with static quantization achieves 7.43 WikiText2 perplexity and 71.08% average accuracy, exceeding the dynamic-quantization-based QuaRot by 0.98 perplexity and +5.98 accuracy points (Section 6.2). This directly substantiates the paper's central claim.

- **Quantitative evidence that prefixing eliminates the extreme token-wise magnitude disparities that previously necessitated per-token quantization**: Section 5.1 reports that after prefixing outliers, the top-1/median ratio of down_proj inputs drops from 478 to 2.7, and the median/min-1 ratio of Q/K drops from >9 to <3.5. This provides direct evidence linking the mechanism to the root cause identified in Section 4.

- **Practical efficiency advantage over the closest prior work**: The offline token selection completes in 12 seconds for Llama-2-7B versus 12 hours for CushionCache (Section 2), a 3600× speedup that is clearly stated with concrete numbers rather than vague claims.

- **Clean ablation isolating the effect of prefixing**: The step-by-step ablation (Section 6.4) shows that static quantization without prefixing collapses (perplexity >34), while adding prefixing recovers performance to competitive levels, cleanly attributing the gains to the prefix mechanism rather than to other components.

- **Demonstrated generalization beyond activation quantization**: PrefixQuant improves weight-only quantization (W2A16g128 with EfficientQAT) by +5.05 and +4.73 average accuracy points on Llama-3-8B and Llama-3-70B respectively (Section 6.2), showing the method's broader applicability.

- **End-to-end speed measurements across two GPU types**: Concrete speedups reported on both A100-80GB and RTX 3090 GPUs (Table 7), providing real hardware evidence that the static quantization enabled by PrefixQuant translates to practical inference benefits.

## Weaknesses

### Major

- **Missing control experiment: FP16 + prefix**. The paper never reports the perplexity or accuracy of the full-precision model *with the same prefix tokens inserted*. The paper's mechanism claim is that prefixing prevents outlier generation during inference, but the prefix tokens themselves (".", "\n", "the", [BOS]) could potentially change the model's output distribution even in full precision. Without this control, part of the observed improvement from prefixing could theoretically be attributed to the prefix acting as implicit prompt engineering rather than enabling better quantization. This control experiment is straightforward to run and would either strengthen the attribution to quantization improvement (if FP16+prefix ≈ FP16 baseline) or reveal a confound that needs discussion.

### Minor

- **No sensitivity analysis for the threshold η (Equation 4)**. The threshold is set to η=64 "empirically," but the paper provides no analysis of how results change with different η values. The number of detected outlier tokens, the set of prefixed tokens, and downstream perplexity likely depend on this hyperparameter. A sensitivity sweep over η ∈ {16, 32, 64, 128} would strengthen the method's credibility and help readers understand how robust the approach is to this choice.

- **Mechanism evidence during auto-regressive decoding is indirect**. The paper shows that prefixing drops the top-1/median ratio measured on calibration/prefill data from 478 to 2.7, and the perplexity recovery (22.14 → 7.23) is strong indirect evidence. However, the paper does not provide direct tracking of outlier metrics (e.g., max/median ratio) across *auto-regressive decoding steps* with and without the prefix. The causal claim that prefixing "prevents generating new outlier tokens during inference" would be strengthened by such step-by-step evidence.

- **No reported variance or uncertainty**. The paper reports single perplexity and accuracy numbers with no standard deviations, seeds, or discussion of run-to-run variation. The grid-search initialization (on 8 calibration samples) and fine-tuning (512 samples, stochastic optimization) have inherent randomness. While single-run reporting is common in this subfield, the paper's claim of establishing a new paradigm ("static beats dynamic") would benefit from at least reporting variance across multiple calibration seeds.

- **Decoding-stage speed evaluation receives limited treatment**. The main paper body covers prefilling-stage speedup only. The paper acknowledges that KV cache quantization primarily saves memory rather than speeding up decoding at small batch sizes, but given the practical importance of decoding latency, a more thorough discussion in the main text (rather than deferred to an appendix section) would be useful.

### Trivial

- Typo on line 133: "finr-tuning" → "fine-tuning"; line 127: "becuase" → "because"; line 169: "apple-to-apple" → "apples-to-apples".

## Nice-to-Haves

- A direct comparison of PrefixQuant(static) vs. PrefixQuant(dynamic) would cleanly separate the effect of quantization granularity from the effect of prefixing, making the "static beats dynamic" framing more precise. The paper's current claim (PrefixQuant+static outperforms prior dynamic methods) is supported, but holding the prefixing method constant would eliminate any ambiguity about whether static per se is responsible for the improvement.
- Decoding-phase speed measurements with large batch sizes (where KV cache quantization does provide speedup) would broaden the paper's practical impact analysis.

## Removed Points

- *Criticism about PrefixQuant static vs. PrefixQuant dynamic comparison being missing*: The paper's practical comparison (PrefixQuant+static vs. QuaRot+dynamic) is what matters for deployment. The within-method comparison would be informative but is not required to support the paper's main claim. Demoted to Nice-to-Have.
- *Criticism about the "static beats dynamic" framing being misleading*: The paper's claim (abstract, line 6) is specifically that PrefixQuant "enables efficient per-tensor static quantization to outperform expensive per-token dynamic quantization" — this is about enabling static to surpass dynamic *in practice*, supported by the system-level comparisons shown. The claim is precisely scoped.
- *Criticism about ratios being stated as single numbers without distribution context*: The paper includes figures (Figures 4, 5, etc.) visualizing the distributions. The numbers complement rather than replace the visual evidence. This is a style preference, not a substantive weakness.
- *Complaint about "'we find that...' is vague"*: Common academic phrasing; not a genuine weakness.
- *Complaint about prefixed tokens being mentioned only briefly*: Table 2 lists the specific prefixed tokens per model. The coverage is adequate.
- *Complaint about "appendix has more details" pattern*: Per instructions, missing appendix content is not a valid criticism since it was present in the original submission.
- *Various generic concerns from harsh critic about can we be sure X or Y*: Speculative concerns without concrete evidence from the paper text.
- *Strength about addressing an important problem*: Generic, not specific to this paper. Removed.

## Novel Insights

The paper's key insight — that the same tokens causing upper outliers in linear layer inputs also cause lower outliers in Q/K/V, and that these can be identified offline from calibration data and prefixed as attention sinks — synthesizes observations from the attention-sink literature (StreamingLLM) with the practical needs of LLM quantization in a way prior work (CushionCache, QFeP) did not achieve. The finding that Hadamard rotation (which addresses channel-wise outliers) is ineffective against lower outlier tokens in Q/K/V adds a nuance to the current understanding of LLM activation distributions. The connection between outlier suppression and improved MSE-based fine-tuning convergence is a secondary insight that opens a path for cross-pollination between activation and weight quantization techniques.

## Suggestions

1. **Run and report the FP16+prefix control experiment** for the main configurations (at least Llama-3-8B and Llama-2-7B on WikiText2). This single addition would address the most significant evidential gap.
2. **Add a sensitivity analysis for η** (Equation 4) showing how the number of detected outlier tokens and downstream perplexity vary with η ∈ {16, 32, 64, 128}.
3. **Report variance** for the fine-tuning experiments (at least range or standard deviation across 3 seeds) and for the grid-search initialization.
4. **Track outlier metrics during auto-regressive decoding** with and without the prefix to directly support the mechanism claim.
5. **Include decoding-phase speed measurements** in the main text, or at minimum expand the explanation of why prefilling-only evaluation is the appropriate metric for this method.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>