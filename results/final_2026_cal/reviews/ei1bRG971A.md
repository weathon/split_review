Now I have all the verification needed. Let me compile the final review.

## Calibration Report

**Round 1 bracket:** 5.0 – 7.0 (after comparing against weak anchors scoring <3.5, middle anchors scoring 3.5–7.5, and strong anchors scoring >7.5 on different topics)

**Anchors retrieved:**
- ZNWpUfwisS (0.67, Withdrawn) — Poor-quality paper on adaptive test-time compute. DND is vastly stronger.
- d1KbcYaWaE (2.67, Reject) — Dynamic memory for LLM adaptation. DND is stronger.
- RKHtowV9Yc (2.50, Withdrawn) — Test-time context extension. DND is stronger.
- eZRPb52ccA (3.33, Reject) — Dynamic-depth speculative decoding. DND is stronger.
- wZ4UoRKDNa (5.60, Accept Poster) — ssToken: token-level data selection for SFT. DND's architectural novelty is greater, validated on full-parameter SFT (not LoRA-only), but both have similar methodological gaps (no variance reporting). DND slightly stronger.
- LoPF9Zl7ic (4.00, Reject) — TokenTune: data selection. DND is stronger.
- z8Smdfn8FF (5.00, Reject) — CFT: critical token fine-tuning. Criticized for single-seed runs, no error bars, expensive counterfactual computation. DND is stronger.
- k7ytptAaDN (5.50, Accept Poster) — Token-level data selection for safe LLM fine-tuning. Different focus, comparable quality.
- kkBOIsrCXh (8.00, Accept Poster) — Embodied navigation. Different topic, not a useful comparison.
- VKGTGGcwl6 (8.00, Accept Oral) — Multi-turn conversation analysis. Different topic.
- qOyF214xmg (8.00, Accept Poster) — Transducing language models. Different topic.
- oBXfPyi47m (8.00, Accept Poster) — RL with world models. Different topic.
- 3ow7tq0O3l (5.00, Accept Poster) — Dr.LLM: dynamic layer routing. Most comparable topic. Criticized for no wall-clock evaluation, unclear batching. DND is stronger (has throughput measurements, simpler method).
- SdnkB5pGbq (6.00, Accept Poster) — Dynamic-dLLM: cache-budget for diffusion LLMs. Different architecture.
- aiP6XfaYZR (6.00, Accept Poster) — GateSkip: token-wise layer skipping via residual gates. Strong paper with solid compute-accuracy trade-offs, criticized for single-seed runs and backbone fine-tuning confounds. DND is slightly weaker due to fewer baselines.
- yAC56BJXmE (4.67, Reject) — Cross-layer attention aggregation for prefill acceleration. DND is stronger.
- cvztBvlglK (6.50, Accept Poster) — Limited memory language models. Different topic.
- dTWfCLSoyl (7.33, Accept Oral) — In-Place TTT. Different topic (test-time training).
- 3gM6HwHvnc (6.50, Accept Poster) — RL makes MLLMs see better. Different topic.
- yKUbw7q1IA (6.80, Accept Poster) — Data-efficient LLM pre-training. Different topic.

**Round 2 narrowing:** Compared directly against Dr.LLM (5.00), ssToken (5.60), GateSkip (6.00), and CFT (5.00). DND is clearly stronger than Dr.LLM and CFT, comparable to ssToken, and slightly weaker than GateSkip. Placing at **5.5**.

---

## Summary

This paper introduces Dynamic Nested Depth (DND), a post-training method that selects a subset of "critical" tokens at each transformer layer and feeds them back through the same layer for an extra round of processing. A lightweight linear router determines which tokens to reprocess based on a learned threshold, and a normalized fusion strategy combines the original and reprocessed representations. Two complementary training strategies—a router controlling loss (score dispersion + distribution preservation) and a threshold control scheme (buffer proportional control + EMA synchronization)—stabilize the selection process. Experiments on Qwen3-1.7B, Llama3.2-1B, Gemma3-1B, and Qwen3-30B-A3B show consistent gains of +1.88 to +2.61 points on the 1B models and +0.87 on the 30B MoE model across diverse benchmarks, with ~6% extra FLOPs and 91–93% throughput relative to vanilla inference.

## Strengths

- **Consistent gains across multiple architectures with minimal overhead.** Tables 1 and 2 show that DND improves performance on four different models (three dense 1B and one 30B MoE) with only 0.03M additional parameters and ~6% extra FLOPs. The gains are particularly pronounced on reasoning-heavy benchmarks (BBH, GPQA), which aligns with the paper's motivation. Throughput measurements in Table 3 confirm 91.6–93.1% of vanilla speed in realistic settings.

- **Post-training plug-and-play design validated on existing open-source models.** DND is applied via standard SFT on Qwen3-1.7B, Llama3.2-1B, Gemma3-1B, and Qwen3-30B-A3B without pretraining from scratch. This is explicitly contrasted with MOR (Bae et al., 2025), which requires training on 200B tokens, and ITT (Chen et al., 2025), which is compared under the same compute budget and underperforms DND (+0.05 vs. +1.88 on Qwen3-1.7B).

- **Ablation study and token selection analysis that validate the core design.** Table 4 systematically ablates the router controlling loss, threshold control, selection ratio, and layer range, showing that the full training strategy (+1.88) outperforms simpler controls (+1.01 with z-loss only). Figures 4a–4b provide compelling evidence that the router preferentially selects high-entropy tokens (r=0.34) and that the nested pass reduces their entropy (r=-0.58). Figures 5, 6a–6b demonstrate that the threshold control scheme stabilizes selection within a tight 5% band.

## Weaknesses

### Fatal

None.

### Major

- **Missing control baseline to isolate the effect of the selection mechanism.** The paper compares DND against vanilla SFT and ITT, but does not include a baseline that reprocesses the same number of tokens *without* the router's selection — e.g., selecting 20% of tokens at random from each layer. Without this, it is unclear whether the gains come from the router identifying truly critical tokens, or simply from adding a modest amount of extra computation to any subset of tokens (which the model can then learn to exploit during fine-tuning). The paper mentions "Instead of uniformly applying extra recurrent depth to all tokens" (line 28) as motivation but never tests the converse: a uniform-but-targeted-depth baseline that isolates the selection decision itself.

- **Training cost not quantified.** The paper carefully measures inference throughput (Table 3) but reports no training FLOPs, wall-clock time, or number of gradient steps relative to the vanilla SFT baseline. During fine-tuning, each DND layer incurs an additional forward (and backward) pass for selected tokens, meaning the DND model sees more gradient updates per step. Unless the baseline is run for a comparable number of total gradient updates (or comparable FLOPs), there is a confound: the gains could partly reflect additional optimization rather than the architectural design. This should be acknowledged and, ideally, quantified.

### Minor

- **No variance or statistical significance estimates for main results.** Tables 1 and 2 report point estimates from single evaluation runs. Several sub-benchmark improvements are small (e.g., +0.13 on BBH, +0.15 on MATH for Qwen3-30B-A3B), and without any measure of variance it is impossible to assess whether these are robust or within evaluation noise. While multi-run SFT on the 30B model is expensive, reporting variance over evaluation seeds or over multiple fine-tuning runs for the 1B models would substantially strengthen the evidence.

- **Training dataset description lacks detail on domain balance and potential overlap with evaluation benchmarks.** The paper states that training data consists of "1-2 million synthetic instances curated from human annotations and open-source materials" but does not describe the domain composition or whether any evaluation benchmarks were used as training material. This information is critical for assessing whether the reported gains might be inflated by data leakage.

- **Router initialization not specified.** The paper does not state whether the linear router weights are initialized randomly or from existing components (e.g., the MoE router for Qwen3-30B-A3B). This matters for training stability and reproducibility, especially since the router is trained from scratch during SFT.

### Trivial

None.

## Nice-to-Haves

- A random-selection ablation (selecting ~20% of tokens per layer uniformly at random) would cleanly isolate whether the router's selection mechanism or simply the extra computation drives the gains.
- Extending to a larger dense model (e.g., Llama-3-8B) would strengthen the claim that DND scales beyond 1B parameters for non-MoE architectures.

## Removed Points

The following points from the harsh critic review were removed or demoted per the filtering guidelines:

- **Missing hyperparameters (λ_sd, λ_dp, buffer size N_b, EMA factor γ, step size α, τ_0).** The paper explicitly states "Detailed hyperparameters and training settings are provided in Appendix Sec.B." Since the appendix was stripped by the PDF parser, these values are present in the original submission. *Removed per rule: "REMOVE weaknesses about missing appendix."*

- **Request for a uniform-depth baseline that processes all tokens through the same layer twice.** This baseline would use ~2× the FLOPs of the vanilla model, while DND uses ~1.06×. It is not a controlled comparison. The relevant control is a same-compute-budget baseline (e.g., random 20% selection), which is retained above as a major weakness. *Demoted and reframed.*

- **Criticism about missing limitations section.** This is a formatting expectation, not a substantive weakness about the method or results. *Removed per rule: "REMOVE pure formatting/style nitpicks."*

- **Request for more models (larger dense model).** The paper already tests on 4 models across 2 architectures. Adding more is a nice-to-have, not a weakness. *Moved to Nice-to-Haves.*

## Novel Insights

None beyond the paper's own contributions. The key observation from the reviews is that the token-selection analysis (Figures 4a–4b, 7b) provides unusually direct evidence for the method's internal mechanism — most papers in this area stop at aggregate benchmark numbers. The correlation between selection frequency and logit entropy (r=0.34) and the negative correlation with entropy reduction (r=-0.58) are the strongest pieces of evidence that the router is doing what the authors claim.

## Suggestions

1. **Add a random-selection control baseline** on at least one model (Qwen3-1.7B). Select 20% of tokens uniformly at random per DND layer and reprocess them with the same architecture. If DND's router-based selection outperforms random selection, the selection mechanism is validated. If random selection matches DND, the gains are from extra computation, not routing.

2. **Report training FLOPs or wall-clock time** for the SFT and SFT+DND conditions, or at least acknowledge the training cost asymmetry and discuss why it does not affect the conclusions.

3. **Add variance estimates** for the 1B-model results (at least 3 fine-tuning seeds or evaluation seeds with bootstrap CIs) to demonstrate that the reported gains are robust.

4. **Describe the training dataset composition** (domain breakdown, whether any evaluation benchmarks were used as training data) to rule out data leakage concerns.

## Score and Decision

**Score:** 5.5 — The paper presents a well-motivated, novel architectural method for dynamic computation allocation in LLMs. The core idea is sound, the ablation is thorough, and the token-selection analysis provides unusually direct evidence for the claimed mechanism. The main gaps are the absence of a random-selection baseline (which would validate that the router drives the gains), unquantified training costs, and lack of variance estimates. These are addressable and do not undermine the paper's central contribution.

**Decision:** Accept

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>