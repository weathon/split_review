## Summary

This paper proposes Quantized Zeroth-order Optimization (QZO), which enables fine-tuning of post-training quantized LLMs by perturbing continuous quantization scales (rather than discrete weights) during zeroth-order gradient estimation. It pairs this with Directional Derivative Clipping (DDC) to stabilize training. The central result is an 18× memory reduction over 16-bit SGD fine-tuning and competitive performance with MeZO (16-bit ZO baseline) at 3× lower memory, demonstrated across three 7B model families and five NLP tasks.

---

## Strengths

- **Concrete and large memory reduction**: Figure 1 and Table 1 show QZO at 4-bit achieves 4.8–6.3 GB peak memory versus 14.8–20.5 GB for MeZO and 26–31.9 GB for SGD fine-tuning, directly validating the headline 18× claim.
- **Consistent improvement over quantized zero-shot baseline**: Table 1 shows large gains on all tasks across all three model families, e.g., Llama-2-7B SST-2 from 58.5 (Zero-Shot-Q) to 90.0 (QZO), and SQuAD F1 from 53.6 to 85.5 — confirming that QZO genuinely fine-tunes quantized LLMs.
- **Effective under extreme 2-bit quantization**: Table 3 shows QZO improves Llama-2-13B (AQLM, 2-bit) across all five tasks, e.g., SST-2 from 57.6 to 80.5, within a single 24 GB GPU, demonstrating practical applicability to aggressive compression.
- **Empirically grounded DDC**: Figure 2 provides causal evidence — without DDC, training collapses to NaN loss at step 22 due to exploding directional derivatives; with DDC both quantities remain stable. Figure 3 shows robustness for thresholds C ≥ 75.
- **Compatibility with scalar and codebook quantization**: QZO is tested with GPTQ (scalar, 4-bit) and AQLM (codebook, 2-bit), demonstrating genuine orthogonality to PTQ method choice.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing QLoRA baseline** — QLoRA (Dettmers et al., 2023) is cited in the reference list but absent from Table 1. It is the most widely adopted approach for fine-tuning quantized LLMs (via LoRA adapters over 4-bit weights) and is a direct practical competitor to QZO. The paper never explains why it is excluded. A reader comparing the two paradigms (ZO vs. adapter-based) in a constrained memory budget cannot make that decision from this paper. Even a memory-footprint comparison (without full performance results) would substantially strengthen the paper's practical positioning.

- **Unexplained FLOP inconsistency in Table 2** — The paper claims "QZO uses only about 1% of the FLOPs of MeZO" but the ratio in Table 2 varies wildly across models: ~12,000× for OPT-6.7B (MeZO: 9.91×10¹⁷ vs QZO: 8.19×10¹³), ~50× for Llama-2-7B, and ~14× for Llama-3.1-8B. The 1% claim applies approximately to Llama models but is wildly off for OPT-6.7B. Both methods perform two full forward passes per step through the same-size network; a 12,000× FLOP gap at the same step count is mechanistically implausible without an explanation. The paper does not clarify whether different step counts, batch sizes, or FLOP counting methodologies are used for different models. This undermines the computation-efficiency narrative for OPT-6.7B specifically.

### Minor

- **"On par with MeZO" is overstated in specific cases** — The main results section claims "QZO performs on par with MeZO on most datasets" (Section 4.2), but Table 1 shows a 21.5-point gap on CB for Llama-3.1-8B (QZO: 69.6 vs MeZO: 91.1) and a 5.2-point gap on BoolQ for the same model (78.2 vs 83.4). The paper acknowledges some gaps ("the gap is still huge on some tasks") but does not reconcile this with the "on par" characterization. A more precise qualifier — e.g., "competitive on classification and generation tasks, with notable exceptions for tasks requiring richer reasoning" — would be more accurate.

- **Theorem 1 lacks intuition in the main text** — Theorem 1 asserts that the clipped directional derivative estimate d′ · z is unbiased for ∇_Δ L, and the variance reduction proof in Eq. 8 depends on this via the equality E[||∇'||]² = (∇L)². This is counterintuitive: standard mean estimation shows that clipping introduces bias. The proof is deferred entirely to Appendix A (which exists per the reproducibility statement). The main text offers no sketch of why clipping a scalar d = f(z) before multiplying by z preserves unbiasedness. For a theoretical claim that the whole variance-reduction argument rests on, even one explanatory sentence (e.g., symmetry of d under negation of z in SPSA) would substantially strengthen the presentation.

- **SGD as fine-tuning upper bound** — Footnote 2 discloses that fine-tuning experiments use SGD, not AdamW. For tasks where AdamW substantially outperforms SGD, the "upper bound" is artificially lower, which makes QZO's gap to fine-tuning appear smaller than it is. This is acknowledged but only in a footnote rather than in the discussion of results.

### Trivial

- The paper states QZO is applied to Stable Diffusion 3.5 Large in Appendix F but mentions it only in passing in Section 5. A brief numerical summary in the main text would justify the generality claim more concretely.

---

## Nice-to-Haves

- **Wall-clock training time comparison**: The FLOP analysis in Table 2 is important but confusing. Actual per-step and total training time on a single RTX 4090 would be more actionable for practitioners and would clarify the practical speedup story.
- **Analysis of when scale-only optimization succeeds vs. fails**: The observation that updating ~0.75% of parameters (quantization scales) can match full-parameter ZO on many tasks is arguably the most scientifically interesting finding in the paper, but is treated as an engineering observation. Even a brief analysis of whether task type, model size, or quantization quality predicts the scale-vs-full-parameter performance gap would elevate the paper significantly.
- **Performance ceiling for Table 3 (2-bit)**: Table 3 only compares QZO against Zero-Shot-Q; including MeZO at 16-bit as a reference ceiling (even without memory constraints) would let readers assess how far 2-bit QZO falls short of ZO at higher precision.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh Critic — CB coincidence as evidence of convergence to the same optimum**: The observation that QZO and MeZO both report 67.9 on CB for OPT-6.7B and Llama-2-7B is not in itself an error — it may reflect the small test set or task saturation. Removed as it conflates coincidence with a methodological problem.
- **Harsh Critic — "de-quantization" concern for scale updates**: The critic asks whether updating Δ means the quantized weights θ̄ remain in int4. Algorithm 1 (lines 148–168) makes clear that θ̃ (integer weights) are fixed throughout and Δ is updated as a continuous variable; the model runs via dequantization w = Δ ⊙ θ̃ during forward passes. The method is exactly as described; this is a strawman.
- **Strength Finder — "about 10¹⁴ FLOPs"**: The Strength Finder characterizes QZO's FLOPs as "~10¹⁴" but Table 2 shows 8.19×10¹³ for OPT-6.7B, 2.26×10¹⁶ for Llama-2-7B, and 7.9×10¹⁶ for Llama-3.1-8B. This characterization is inaccurate for Llama models and is removed as a generic strength that conflicts with actual data.
- **Strength Finder — "performance on par with MeZO" as a strength without qualification**: Given the 21.5-point CB gap for Llama-3-8B, retaining "performance on par" as an unqualified strength conflicts with a verified weakness; the qualified form is maintained in the Strengths section.

---

## Novel Insights

QZO's most intellectually interesting finding — that optimizing ~50M continuous quantization scales (0.75% of total weights) can match full-parameter ZO optimization over 6.7–8B parameters on most NLP tasks — is underexplored by the authors. This suggests that quantization scale parameters are disproportionately influential for task adaptation, a phenomenon with potential implications for understanding what information in LLM weights is most task-relevant. The paper establishes this empirically but does not pursue it analytically. The DDC mechanism also raises a non-trivial theoretical question: under what conditions does clipping a scalar estimator before multiplication by its generating random vector preserve unbiasedness? This is counterintuitive from standard statistics and may have broader applicability in ZO optimization beyond this paper's specific setting.

---

## Suggestions

1. Add QLoRA to Table 1, even for a subset of models/tasks, or provide an explicit memory-footprint comparison explaining why QLoRA is out of scope.
2. Clarify FLOP counting in Table 2: specify training steps and batch sizes per method, and explain the anomalous 12,000× ratio for OPT-6.7B versus the 14–50× ratios for Llama models.
3. Replace the unqualified "on par with MeZO" characterization with one that acknowledges the CB gap for Llama-3.1-8B and explains it (e.g., harder reasoning tasks where scale-only updates are insufficient).
4. Add one sentence in Section 3.2.2 providing intuition for why DDC preserves unbiasedness — even a symmetry argument (d is odd in z under SPSA perturbation) would make Theorem 1 much less mysterious.
5. Promote the Stable Diffusion 3.5 results from Appendix F to a small Table in Section 5 to support the generality claim.

---

## Score and Decision

**Originality**: The core idea of perturbing quantization scales for ZO gradient estimation is clean and novel. (4/5)
**Importance**: Memory-constrained fine-tuning is a real and growing need; enabling 13B fine-tuning on a 24 GB GPU is practically significant. (4/5)
**Claims supported**: Memory reduction claims are robustly demonstrated; the "on par with MeZO" claim is partially supported but overstated in specific cases; the FLOP claim has an unexplained anomaly. (3/5)
**Soundness**: Method is principled; DDC has empirical support; but FLOP accounting inconsistency and missing QLoRA comparison leave gaps. (3/5)
**Clarity**: Generally clear writing and good algorithmic presentation; Table 2 confusion and missing justification for QLoRA exclusion reduce clarity. (3/5)
**Community value**: Strong practical value for resource-constrained settings; directly useful for practitioner deployment. (4/5)

The paper makes a real and useful contribution with clearly demonstrated memory reduction. The major weaknesses (missing QLoRA, FLOP inconsistency) are addressable in revision and do not invalidate the core results. The method is sound and the experiments are extensive enough to support the main claims for most tasks.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>