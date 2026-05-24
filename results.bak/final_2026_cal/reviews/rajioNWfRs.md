Now I have all the information needed. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor

- weakness 1 — why it matters

### Trivial

- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Include something like this "These points are flagged to be removed, treat them with caution"
Weaknesses that are removed keep the details of the S/W just in case they are useful 

## Novel Insights
One paragraph synthesizing genuinely novel observations.
If no genuinely novel insight emerges from the reviews beyond the paper's own contributions, write
"None beyond the paper's own contributions."

## Suggestions
- specific actionable suggestion

## Score and Decision

Let me compose the final review.## Summary

This paper introduces TNT, a two-stage training paradigm for deep memory modules (e.g., Titans, TTT) that addresses the fundamental conflict between training efficiency and inference performance. Stage 1 uses a hierarchical memory architecture—a global module processing large chunks for long-range context and parallel local modules with *periodic state resets* that break sequential dependencies to enable context parallelism. Stage 2 is a lightweight fine-tuning phase that adapts only the local modules to smaller chunk sizes for high-resolution inference. The paper also proposes a Q-K Projection mechanism to resolve a compression-retrieval domain mismatch. Evaluated on the Titans architecture, TNT achieves up to 17× training speedup while maintaining or improving model quality (PPL 23.13 vs. Titans best 25.07). The core innovation—periodic resets enabling parallelization of non-linear deep memory modules—is well-motivated and addresses a genuine bottleneck.

## Strengths

1. **Periodic resets enable true context parallelism for non-linear deep memory modules.** The local memory update rule (Eq. 6) breaks inter-chunk sequential dependencies that previously made parallelization impossible for non-linear RNNs with normalization between steps. This directly produces the linear runtime scaling shown in Figure 4 (TNT stays ~400–550ms while Titan's grows to ~4000ms at 32K length) and the 17.37× time-to-quality speedup in Table 1. No prior work on deep memory modules achieves this level of parallelization.

2. **Q-K Projection is a well-motivated mechanism with clean ablation support.** The retrieval rule (Eq. 7) projects the query onto the subspace spanned by recent keys, resolving Challenge 2 (domain mismatch between compression and retrieval). The ablation (Table 3) shows removal degrades PPL from 21.04 to 22.01—a 0.97-point increase—confirming its critical role. The implementation via a running sum of outer products avoids storing all past keys, keeping memory O(d²) per local module.

3. **Clear identification of three challenges with empirical evidence.** Section 3 systematically identifies: (1) poor hardware utilization from small chunks, (2) compression-retrieval domain mismatch, and (3) chunksize-sensitivity over-specialization (Figure 2 convincingly shows inference PPL jumps from 13.78 to 22.40 when chunk size deviates from training size). These challenges are specific, falsifiable, and directly motivate the method.

4. **Comprehensive ablation validates each component.** Table 3 separately tests hierarchical memory (adding local modules improves PPL from 23.53 to 20.15), removing global memory (PPL rises to 25.60), removing Q-K projection (PPL rises to 22.01), and adding Stage 2 fine-tuning (PPL improves from 21.04 to 20.86). This gives confidence that each design choice contributes positively.

5. **Impressive runtime scaling with practical wall-clock advantage.** Figure 4 shows a native JAX TNT implementation at C_L=128 runs at ~550ms at 32K sequence length, exceeding FlashAttention's ~1000ms. The crossover point at ~16K demonstrates practical hardware-level speed, not just theoretical complexity.

## Weaknesses

### Major

1. **The abstract claims evaluation "on Titans and TTT models" that is not borne out by the experiments.** The abstract and introduction state TNT is "Evaluated on Titans and TTT models." However, the experiments section (line 209) says "we instantiate it with a strong deep memory model, Titans, to demonstrate its effectiveness." TTT appears only as a baseline in Table 2 (chunksize 256, PPL 27.62), not as an architecture on which TNT is applied. This is not a minor omission—it directly contradicts a stated contribution. Either TNT should be validated on a second architecture such as TTT or Atlas, or the claim must be scoped back to Titans only. At minimum, the abstract must be corrected.

2. **The "model-agnostic training paradigm" claim is unsubstantiated.** The paper repeatedly states TNT is "a general training paradigm applicable to any deep memory module rather than a specific architecture" (Section 1) and "While TNT is model-agnostic" (Section 5). Yet all experiments use only Titans. The formal definitions (Eqs. 5–7) are indeed architecture-agnostic in principle, but no empirical evidence is provided that the periodic reset mechanism and two-stage process transfer to another deep memory architecture (e.g., TTT, Atlas). Without at least one additional instantiation, this claim is speculative.

### Minor

3. **Stage 2 fine-tuning presentation is confusing and the headline improvement is very small.** The Stage 2 rows in Table 2 use different local-memory configurations (e.g., {2,4,8,16}) than the Stage 1 rows (e.g., {4,8,16,32}), but the paper does not state which Stage 1 checkpoint each Stage 2 configuration is fine-tuned from. The improvement from the best Stage 1 (23.13 PPL) to the best Stage 2 (23.09 PPL) is 0.04—a negligible reduction at 150M scale. The cleaner comparison in Table 3 (Stage 1 {8} → Stage 2 {1}: 21.04→20.86, a 0.18 PPL improvement) is more convincing. The authors should clarify the fine-tuning source for each Table 2 Stage 2 entry and explain why the improvement is meaningful.

4. **The local window size S_L is never ablated.** S_L (the periodic reset window, set to 2048 or 4096) is a critical hyperparameter that determines the parallelism-quality trade-off. If S_L is too large, parallelism benefits degrade; if too small, local context is lost. Despite this being central to the paper's core innovation, no sensitivity analysis is provided. A small table showing PPL and speed at different S_L values (e.g., 1024, 2048, 4096, 8192) would significantly strengthen the paper.

5. **Parameter/FLOPs accounting across models is not provided.** While the paper states "We train 150M parameter models" for all configurations, this likely refers to slow weights only. TNT adds global memory + up to 4 local memory modules, each with its own fast-weight sub-network. The paper does not explain how the 150M budget is distributed across modules, nor does it report per-step FLOPs. The PPL gap between TNT (23.13, 4 local memories) and Titans (25.07, single module) could partly reflect usable capacity rather than the training paradigm alone. A FLOPs-per-step table or a controlled experiment with matched per-step compute would clarify this.

6. **The target loss of 3.20 in Table 1 is not justified.** The time-to-quality comparison uses a fixed target loss of 3.20. The paper does not show that all baseline configurations actually reach this loss, nor explain why 3.20 was chosen. If some baselines never converge to 3.20, the speedup comparison is invalid for those entries. The authors should report final losses for all models or use an alternative metric (e.g., time to match the best baseline loss).

### Trivial

7. Table 1's Titans baseline at C=128 trains in 3.71hr (5.25× speedup), but the paper claims "up to 17×" relative to "the most accurate baseline configuration." Comparing TNT C_L=64 (17.37×) against Titans C=8 (which has smallest chunks but not best accuracy) is slightly inconsistent—Titans C=8 achieves PPL 25.07 while Titans C=256 achieves PPL 27.13. This is clear from the tables but the framing could be more precise.

## Nice-to-Haves

- Validate TNT on a second deep memory architecture (e.g., TTT or Atlas) to substantiate the model-agnostic claim.
- Include an ablation of S_L (e.g., values 1024, 2048, 4096, 8192) showing both PPL and runtime.
- Add a FLOPs-per-step comparison between TNT and Titans configurations to disentangle capacity from training-paradigm effects.
- Show the fine-tuning curve from a specific Stage 1 checkpoint (e.g., from {4,8,16,32} to {2,4,8,16}) with compute cost reported.

## Removed Points

These points were raised by the harsh critic or strength finder but are removed after verification:

- **"Model capacity confound (more parameters in TNT)"** – The paper states all models are 150M parameter models. The critic assumed TNT has more parameters without evidence. However, the FLOPs-per-step concern (Minor weakness 5) captures the real residual issue without the speculative parameter-count claim.
- **"TNT outperforms FlashAttention (different operations comparison)"** – The paper itself acknowledges TNT is a native JAX implementation lacking custom kernels, which is an honest disclosure. The runtime comparison in Figure 4 is a valid wall-clock benchmark on the same hardware.
- **"Q-K projection adds O(d²) memory per module"** – This is acknowledged in the paper via the running-sum description. It's a design trade-off, not an oversight.
- **"Stage 2 fine-tuning degrades at C'_L=1"** – Stage 2 {1} achieves PPL 23.99 vs Stage 1 {8} at 24.10, which is actually an *improvement*. The critic misread the comparison (comparing against different Stage 1 configs).
- **"Missing statistical significance"** – Single-run evaluation is standard for large-scale pre-training experiments at 150M/10B token scale. Not required.
- **"Missing related work"** – Removing per instructions (cannot verify completeness).
- **"Formatting/style nitpicks"** – Removing per instructions (parser artifacts).
- **Strength Finder: "Model-agnostic framework"** – Removed because it conflicts with verified Major weakness 2 (not validated on other architectures).
- **Strength Finder: "The experiments use both Titans and TTT"** – Removed because TTT only appears as a baseline, not as a TNT instantiation. The strength misrepresents the paper's own experimental setup.
- **"Stage 2 improvement is too small"** – The 0.04 PPL improvement in Table 2 is indeed small, but this is retained as Minor weakness 3 with proper context. The more meaningful comparison is in Table 3 (0.18 PPL improvement).
- **"Decoupling claim is overstated"** – The decoupling is real: Stage 1 maximizes throughput with large chunks, and Stage 2 fine-tunes with minimal compute (~5%). The critic's objection that "Stage 2 still requires compute" misunderstands what "decoupling" means—it does not mean zero cost, just that the bulk of training and the final accuracy optimization are separated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the abstract: replace "Evaluated on Titans and TTT models" with "Evaluated on the Titans architecture" or add TNT+TTT results.
2. Add a small table ablating S_L (e.g., values 1024, 2048, 4096, 8192) with PPL and runtime.
3. Clarify the Stage 2 fine-tuning protocol: state explicitly which Stage 1 checkpoint seeds each Stage 2 configuration in Table 2.
4. Add a FLOPs-per-step comparison or an iso-compute experiment to address the capacity confound.
5. Show that all baselines in Table 1 actually converge to loss 3.20, or justify the target differently.

## Score and Decision

Let me calibrate via anchor comparison.

**Calibration round 1 — Bracketing:**
- Low band (<3.5): Papers at 2.50–3.33 on similar RNN/memory topics — these are clearly weaker (poorly validated, unclear contributions).
- Middle band (3.5–7.5): Anchors at 4.50–5.60 on closely related topics (MoM 5.50, TTT-Done-Right 5.60, Smooth Reading 5.00, MeSH 4.50, Memory Caching 4.67).
- High band (>7.5): Anchors at 8.00 on unrelated topics.

**Round-1 bracket:** 4.5–6.5.

**Calibration round 2 — Narrowing:**

Topically closest anchors read in full:

| Anchor | Avg Score | Topic Comparison |
|---|---|---|
| MoM: Mixture-of-Memories | 5.50 | Linear sequence modeling with multiple memory states. Cleaner evaluation but less novel mechanism. TNT has stronger architectural novelty but weaker cross-architecture validation. Comparable. |
| Test-Time Training Done Right (LaCT) | 5.60 | Large-chunk TTT. Multi-modal evaluation, custom kernels not required. TNT has more architectural innovation (resets + hierarchy) but less evaluation breadth. Comparable. |
| MesaNet | 6.50 | Optimal test-time training with CG solver. More thorough experiments (up to 1B params), cleaner narrative, but solves an easier problem (linear modules). TNT is slightly below in polish and validation breadth. |
| MeSH: Memory-as-State-Highways | 4.50 | Memory buffer for recursive transformers. Mixed reviews (0,4,6,8). Less clean validation. TNT is clearly stronger. |
| Memory Caching | 4.67 | Caching states for RNNs. Rejected paper. TNT has stronger novelty and results. |

**Round-2 narrowing:** TNT is clearly above the MeSH (4.50) and Memory Caching (4.67) anchors. It is comparable to MoM (5.50) and TTT-Done-Right (5.60)—similar quality level but with different trade-offs. It is below MesaNet (6.50), which had better-controlled experiments and a cleaner narrative. The overclaiming in the abstract and the lack of cross-architecture validation are real weaknesses that prevent a higher score.

**Final score:** 5.5. The paper has genuine contributions (periodic resets enabling deep memory parallelism, Q-K projection, well-identified challenges) that are supported by strong speedup results and a clean ablation study. However, the abstract overclaims about TTT evaluation, the model-agnostic claim is unsubstantiated, S_L is never ablated, and the Stage 2 presentation needs clarification. These are fixable issues, and with revisions this could reach 6.0–6.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>