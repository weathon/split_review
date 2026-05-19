Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes Mixture-of-Head Attention (MoH), which replaces the standard uniform sum of all attention heads with a token-wise weighted sum over a dynamically selected subset of heads, drawing inspiration from Mixture-of-Experts. MoH introduces shared heads (always activated) and a two-stage router that balances shared and routed head contributions. The method is evaluated across Vision Transformers (ViT), Diffusion Transformers (DiT), small LLMs trained from scratch, and a continue-tuning conversion of LLaMA3-8B. Results show that MoH typically matches or slightly exceeds baseline performance while activating only 50%–90% of attention heads.

## Strengths

1. **Well-motivated architectural innovation, validated across multiple domains.** The paper extends the MoE intuition to attention heads in a principled way (deriving the summation form of MHA, then introducing routing). It demonstrates the method on three distinct model families — ViT (image classification), DiT (image generation), and decoder-only LLMs — which is more comprehensive than typical attention-modification papers.

2. **Shared heads and two-stage routing are empirically shown to add value.** Ablation Table 6 shows that shared heads improve accuracy from 75.6% to 78.3% (+2.7%) and two-stage routing further improves to 78.6% on ImageNet classification (small-scale setting). The same table shows consistent FID improvements on DiT. These components are clearly motivated and validated.

3. **From-scratch experiments use fair, controlled comparisons.** The ViT experiments (Table 1) compare against TransNeXt with identical training recipes except for the attention mechanism. The LLM-from-scratch experiments (Table 4) compare models trained by the authors on the same data with the same budget. These are well-controlled and provide valid evidence that MoH can match or slightly exceed MHA baselines with fewer activated heads.

4. **Demonstration that pre-trained MHA models can be converted to MoH via continue-tuning is novel and practically valuable.** Section 4.3 shows that LLaMA3-8B can be adapted into MoH-LLaMA3-8B with a two-stage training protocol, including a parameter-free router based on query ℓ2 norms and straight-through estimation for routing scores. Even discounting the unfair comparison (see weakness below), the basic finding that conversion is feasible is nontrivial and distinguishes MoH from methods like MoA that require training from scratch.

## Weaknesses

### Major

1. **Continue-tuning LLaMA3 comparison is confounded by unequal training budgets.** The paper's headline claim — "MoH-LLaMA3-8B achieves 64.0% average accuracy across 14 benchmarks, outperforming LLaMA3-8B by 2.4%" — compares a model that received **400B additional tokens** (300B Stage 1 adaptation + 100B Stage 2 MoH training) against the original LLaMA3-8B that received **zero additional training**. The observed 2.4% improvement cannot be attributed to MoH alone; it could be partially or entirely due to the extra training. A proper control would require continue-tuning the original LLaMA3-8B on the same 400B tokens with standard MHA. This weakness does not invalidate the paper — the from-scratch experiments provide valid, fair evidence — but it undermines the most eye-catching result and the claim of "outperforming" in the abstract/introduction.

2. **No experimental comparison to existing dynamic attention routing methods (MoA, adaptive head pruning).** The paper distinguishes MoH from MoA (Zhang et al., 2022) conceptually in Section 5 but provides no empirical comparison. Given that both methods route tokens to subsets of attention-related "experts," an experimental comparison (on at least one task, e.g., language modeling or image classification) is expected. Without it, the claim that MoH is a "promising alternative" to MHA is weakened by the absence of evidence that it improves upon prior alternatives to MHA.

3. **The paper does not report FLOPs, latency, or throughput for any model.** Efficiency is stated as a primary motivation ("enhancing inference efficiency" appears in the abstract and throughout). However, the only evidence for efficiency is the percentage of activated heads. While fewer heads likely reduce computation, the router introduces overhead (scoring all heads, top-K selection) that is never quantified. For models with small head counts, this overhead could partially offset the savings. Reporting actual FLOPs or wall-clock measurements for at least one model scale (e.g., MoH-ViT-B vs TransNeXt-B) would substantially strengthen the efficiency claim.

### Minor

4. **No run-to-run variance reported.** Reported improvements are small in several settings (e.g., MoH-ViT-B at 75% heads: 84.9% vs TransNeXt 84.8%, a +0.1% gain; MoH-LLM-B at 75% heads: 47.8% vs 47.4%, a +0.4% gain). Without multiple seeds or confidence intervals, the statistical significance of these gains is unclear. Given that experiments are single runs, the paper should at minimum note this limitation.

5. **LLM from-scratch evaluation covers only 6 relatively simple benchmarks.** The paper justifies this by model size (~0.2B), which is reasonable, but the evaluation would be stronger with additional tasks (e.g., HellaSwag, ARC-Easy, WinoGrande-zero-shot) that are standard even for small models. The modest gains (0.4%–1.5%) on these limited tasks leave open questions about whether MoH helps on harder reasoning tasks.

6. **Shared heads ratio recommendation is not supported by the paper's own data.** Table 7 shows performance is essentially flat (78.4%–78.6%) across shared head ratios from 13.9% to 74.0%. The paper then recommends "using a higher ratio of shared heads (>40%)" based on Soft MoE literature. While this is externally motivated, the data in the paper shows no advantage for higher ratios, so the recommendation appears to come from outside the paper's evidence.

7. **DiT results with 75% activated heads underperform the 100% MHA baseline.** The authors acknowledge this (image generation as a dense prediction task has less head redundancy), which is honest, but it limits the generality of the efficiency claim to tasks where sufficient head redundancy exists.

8. **The load balance loss weight (β=0.01) is not ablated.** Given that load imbalance is a well-known failure mode in MoE, the sensitivity to this hyperparameter should be reported for at least one setting.

### Trivial

- The paper uses "7,000K" to denote 7 million training steps, which is an unusual notation that could cause confusion.
- Table 5 (LLaMA3) is split awkwardly across three subtables; a unified layout would improve readability.

## Nice-to-Haves

- For the LLaMA3 continue-tuning experiment, ablating whether the 300B Stage 1 adaptation is necessary (i.e., can MoH conversion be applied directly in 100B tokens?) would strengthen the efficiency argument.
- Adding a simple static random head-pruning baseline (dropping the same fraction of heads randomly) would help separate the benefit of learned routing from mere sparsity.
- The router overhead could be analyzed analytically (FLOPs added vs. saved) even without hardware measurements.

## Removed Points

These points were raised but removed after cross-checking against the paper:

- **"Parameter parity not explained"** — The paper states in the Figure 1 caption: "MoH does not increase the number of attention heads, ensuring that the total parameter for MoH is comparable to that of the multi-head attention." The router parameters (W_s, W_r, W_h) are small relative to the attention projections. The parity is adequately explained. REMOVED.
- **"DiT baselines might not be exactly replicated"** — The paper explicitly states "we only replace the standard multi-head attention with our MoH in MoH-DiT models, while keeping all other training parameters identical to DiT." Citing the original DiT results is standard practice. The criticism speculates about replication quality without evidence. REMOVED.
- **"The 7,000K notation is confusing"** — A formatting/presentation nitpick about the paper's macro rendering. REMOVED (trivial formatting, but moved here rather than kept as a weakness).
- **"Could the improvement be due to random seed?"** — Pure speculation without evidence. REMOVED.
- **"Ablation shared heads ratio is suspiciously flat"** — This is not a weakness; the data shows exactly what the paper claims: "performance remains relatively consistent across a wide range." The recommendation about >40% comes from external Soft MoE literature, not the paper's data. REMOVED (not a genuine flaw).
- **Strength: "MoH achieves higher accuracy with fewer activated heads"** — Partially conflicts with the verified Majors 1 (LLaMA3 unfair comparison) and 3 (no efficiency measurements), and the reported gains are very small (<1% in most cases). Downgraded from a strength to a qualified observation.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about MoH that the authors themselves do not already articulate.

## Suggestions

1. **Fix the LLaMA3 comparison.** Run a proper control: continue-tune the original LLaMA3-8B on the same 400B tokens with standard MHA (or at least the 100B Stage 2 tokens), and report the comparison. Frame the result as "pre-trained MHA models can be converted to MoH" rather than "MoH outperforms MHA" for this setting.
2. **Add efficiency measurements.** Report FLOPs or wall-clock latency for at least one model scale (e.g., MoH-ViT-B vs TransNeXt-B, or MoH-LLaMA3-8B vs LLaMA3-8B). This directly supports the efficiency claim.
3. **Add an experimental comparison to MoA** (or another dynamic routing baseline) on at least one task.
4. **Report variance.** Run at least one experiment setting with 3 random seeds to establish whether the small observed gains are statistically meaningful.
5. **Remove or soften the "outperforming" language** for the LLaMA3 experiment until a fair control is added.

## Score and Decision

The paper proposes an interesting and well-motivated modification to multi-head attention, with controlled experiments in three domains that provide valid evidence. The method is sound, and the ablation studies confirm the value of the proposed components. However, the paper has three significant weaknesses: (1) the headline LLaMA3 result is confounded by unequal training budgets, (2) no empirical comparison to existing alternatives like MoA, and (3) the central efficiency claim lacks direct measurement. These are all addressable, but in the current form the evidence is weaker than the claims. The from-scratch experiments provide positive but marginal support (gains ~<1% on single runs), and the most impressive result is compromised by a methodological flaw.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>