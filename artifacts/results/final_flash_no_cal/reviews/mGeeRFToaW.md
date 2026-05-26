Here is the final consolidated review.

---

## Summary

This paper introduces QZO (Quantized Zeroth-order Optimization), a method that combines model quantization with zeroth-order optimization to minimize GPU memory consumption across weights, gradients, and optimizer states. The core idea is to apply SPSA-style gradient estimation to the continuous quantization scale parameters rather than to the discrete quantized weights, thereby avoiding dequantization/re-quantization overhead. A directional derivative clipping (DDC) mechanism is introduced to stabilize training. Experiments on OPT-6.7B, Llama-2-7B, Llama-3.1-8B, and Llama-2-13B across five NLP benchmarks show that QZO achieves performance on par with MeZO (which operates on 16-bit models) while using significantly less memory and enabling fine-tuning of a 2-bit 13B model on a single 24GB GPU.

---

## Strengths

1. **Clever and novel technical approach.** Perturbing quantization scales rather than discrete weights is a simple but insightful way to bridge the gap between discrete quantized weights and the continuous perturbations required by zeroth-order optimization. This idea cleanly avoids the dequantization/re-quantization loop that would otherwise be necessary. The method is also demonstrated to be orthogonal to both scalar-based (GPTQ) and codebook-based (AQLM) quantization (Table 1 and Table 3).

2. **Competitive empirical performance despite 4-bit weights.** On several benchmarks, QZO matches or exceeds MeZO (which operates on 16-bit models). For example, on Llama-2-7B SQuAD, QZO achieves 85.5 F1 vs. MeZO's 80.7 (Table 1). This convincingly shows that the memory savings do not come at a catastrophic accuracy cost.

3. **Extreme parameter and FLOP efficiency.** QZO fine-tunes only ~5×10⁷ quantization-scale parameters rather than all ~6.7×10⁹ weights, resulting in roughly 1% of the trainable parameters and, in some cases, orders of magnitude fewer FLOPs compared to MeZO (Table 2). This is a concrete computational advantage beyond memory.

4. **DDC empirically prevents training collapse.** Figure 2 shows that without DDC, training hits NaN within 22 steps, whereas with DDC it remains stable for 1,000 steps. Figure 3 further demonstrates robust performance across a range of clipping thresholds (C ≥ 75). The ablation study is well-designed and provides strong empirical support for the stabilization component.

5. **Extreme quantization scenario works.** QZO successfully fine-tunes a 2-bit Llama-2-13B using only 5.78 GB of memory (Table 3), beating the zero-shot baseline by large margins (e.g., SST-2: 80.5 vs. 57.6). This demonstrates practical viability for on-device learning settings with severe memory constraints.

---

## Weaknesses

### Major

1. **Misleading 18× memory reduction claim.** The paper's headline claim — an "18× reduction in total memory cost" (Abstract, Introduction, Figure 1) — is presented without the necessary context to be properly interpreted. The 87.6 GB figure for "Fine-tune w/ AdamW (16-bit)" is obtained using fully-sharded data parallel (FSDP), while QZO's 4.8 GB is measured on a single GPU. The paper does not specify how many GPUs were used for the AdamW/FSDP run, nor does it clarify whether 87.6 GB is a per-device measurement, an aggregate across devices, or a theoretical calculation. Under the standard reading (per-device peak memory), the comparison is invalid because FSDP explicitly distributes memory across devices. Against the SGD baseline actually used in the paper's performance comparisons (26 GB, single-GPU), the savings are ~5–6× — still practically meaningful but far less dramatic than 18×. **Why it matters:** The 18× factor is the paper's most prominent quantitative claim and appears in the abstract. If it conflates single-GPU and multi-GPU measurements, it misleads readers about the magnitude of QZO's advantage. The paper should either report per-device memory for all methods consistently or clearly state the conditions under which the 18× figure is computed.

2. **Incorrect theoretical justification for Directional Derivative Clipping.** Theorem 1 claims that the clipped gradient estimate \(\hat{\nabla}_{\Delta} \mathcal{L}'\) is an *unbiased* estimate of the true gradient. This is incorrect: clipping the scalar directional derivative \(d\) to \([-C, C]\) is a non-linear operation that introduces bias whenever \(|d| > C\). The subsequent variance analysis (Eq. 7–8) relies on this unbiasedness claim (via the substitution \(\mathbb{E}[\|\hat{\nabla}'\|| = \|\nabla\mathcal{L}\|\)). Without unbiasedness, the variance inequality does not follow as stated. The empirical ablation (Figures 2–3) convincingly demonstrates that DDC stabilizes training, so the method itself is not in doubt. **Why it matters:** The paper explicitly presents the DDC theory as formal justification for a core algorithmic component. Publishing a known-to-be-incorrect mathematical claim (the unbiasedness of a clipped estimator) would be irresponsible. The theoretical framing should be corrected to a bias-variance trade-off analysis, an MSE argument, or simply removed in favor of the empirical evidence.

### Minor

3. **No comparison to LoRA/QLoRA.** QZO targets memory-efficient fine-tuning of quantized models, a domain where LoRA and QLoRA are the de facto standard baselines. While QZO operates in a different paradigm (ZO on scale parameters vs. backprop on low-rank adapters), the complete absence of any comparison makes it difficult for readers to situate QZO's practical significance relative to established methods. Even a brief discussion or a single comparison point would substantially strengthen the evaluation. **Why it matters:** Without this context, the paper's claim of advancing memory-efficient fine-tuning is only partially supported.

4. **SGD as the fine-tuning upper-bound.** The paper uses SGD rather than AdamW for the fine-tuning performance baseline (Section 4.1), with the justification of limited computational budget. Since AdamW typically outperforms SGD in LLM fine-tuning, this choice sets a lower upper-bound and may inflate QZO's relative performance. The paper acknowledges this limitation, but it still weakens the comparison. **Why it matters:** A reader cannot tell how QZO's performance would compare against a more standard AdamW-tuned model.

5. **Limited training data and lack of scaling analysis.** Following the MeZO protocol, the paper uses only 1,000 training samples. While this is consistent with prior work, QZO's expressivity is fundamentally limited because it only tunes scaling parameters. An experiment varying the training set size (e.g., 500, 1K, full dataset) would help assess whether the scale-only parameterization provides enough capacity for larger-scale adaptation tasks. **Why it matters:** Without this analysis, the applicability of QZO beyond the small-data regime is unclear.

### Trivial

6. **Notation mismatch between theory and implementation.** The mathematical formulation (Eq. 5) uses element-wise scaling (\(\theta = \Delta \odot \bar{\theta}\)), while the experiments use group-wise quantization with group size 128, where one \(\Delta\) scales many integers. The notation should clarify that the \(\odot\) product implicitly broadcasts over groups. This does not affect the validity of the method but creates unnecessary confusion for readers familiar with standard quantization conventions.

7. **Terminological imprecision.** The paper states that the variance inequality "holds almost surely" (line after Eq. 8), but what is intended is "holds in expectation under the assumption of unbiasedness." This is a minor technical imprecision.

---

## Nice-to-Haves

- **Report wall-clock time.** ZO methods require two forward passes per step, making training slower than backprop-based methods. Reporting training time per step or total fine-tuning duration would greatly help practitioners assess the practical trade-off.
- **Naïve weight-space ZO baseline.** The paper dismisses "dequantize + perturb + requantize" as infeasible but provides no experiment showing how it compares to QZO. A small ablation isolating the benefit of the scale-perturbation design would strengthen the motivation.
- **LoRA/QLoRA comparison.** As noted above, even a single model/dataset comparison against LoRA or QLoRA would anchor QZO in the broader landscape.

---

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"18× memory reduction" listed as a strength by the Strength Finder.** This conflicts with the verified weakness that the comparison is between single-GPU (QZO) and multi-GPU/aggregate (AdamW with FSDP) setups. Per the merge instructions, when a strength and weakness disagree on a specific claim, the weakness wins. The strength is demoted here; the actual strength (significant memory reduction of ~5–6× against SGD) is captured implicitly in Strengths #2–3.

- **Criticism about the paper not being reproducible due to missing artifacts.** The parser strips appendices and supplementary material from all papers. Claims about "missing proofs" or "missing appendix content" cannot be verified from the parsed text and are removed per the hard rules.

- **Criticism about missing related work on LoRA/QLoRA.** The paper cites QLoRA in its references (Dettmers et al., 2023). The criticism about not *comparing* to LoRA/QLoRA is retained as a Minor weakness (point #3 above), but any claim that the paper ignores this line of work is inaccurate.

- **Speculation that the AdamW memory number might be theoretical rather than measured.** While this is a genuine concern, the review does not need to assert it as a proven fact. The weakness is sufficiently supported by the undisputed facts: (a) the caption states FSDP was used, (b) the number of GPUs is not reported, and (c) 87.6 GB exceeds a single A100's capacity. These facts alone make the comparison ambiguous and potentially misleading. No further speculation is needed.

- **Generic "evaluation lacks rigor" framing from the Harsh Critic.** This is an area-of-concern sweep without a specific concrete anchor. The specific, verifiable concerns (memory comparison ambiguity, missing baseline comparison) are preserved in the Major/Minor sections above.

---

## Novel Insights

None beyond the paper's own contributions. The observation that perturbing quantization scales (rather than discrete weights) makes ZO compatible with quantized models is itself the novel insight, and the reviews do not surface a deeper, cross-paper synthesis beyond what the authors already articulate.

---

## Suggestions

1. **Clarify the memory comparison.** Report per-device peak memory for all methods, including AdamW with FSDP (specify the number of GPUs). Alternatively, clearly label the 87.6 GB figure as "total memory across all devices" or "theoretical single-GPU equivalent" and present the single-GPU SGD comparison (5–6× savings) as the primary memory-efficiency claim in the abstract and introduction.

2. **Fix or remove the DDC theory.** Theorem 1 is incorrect as stated because clipping introduces bias. Either (a) replace the unbiasedness claim with a proper bias-variance or MSE analysis that correctly handles the clipping operation, or (b) drop the theoretical framing entirely and present DDC as a well-motivated heuristic with strong empirical support (Figures 2–3 already provide this). Option (b) is simpler and does not detract from the contribution.

3. **Add at least one LoRA/QLoRA comparison point.** Even a single-model, single-dataset comparison (e.g., Llama-2-7B on SST-2) would dramatically improve the paper's positioning. QZO targets a different point in the design space, but readers need to see how this point compares to what they would actually use in practice.

4. **Include wall-clock training time.** This is essential information for any ZO method, as the two-forward-pass cost is a well-known practical limitation.

5. **Report the number of GPUs used for the AdamW/FSDP memory profiling.** This is necessary for the reader to interpret the 87.6 GB figure.

---

## Score and Decision

The paper presents a genuinely novel and interesting approach to memory-efficient fine-tuning. The core idea (ZO on quantization scales) is clever, the empirical results are solid, and the ablation study convincingly demonstrates that DDC stabilizes training. However, the paper in its current form has two major issues that prevent acceptance: (1) the headline 18× memory reduction claim is based on a comparison that mixes single-GPU and multi-GPU setups without sufficient transparency, and (2) the theoretical justification for DDC (Theorem 1) is mathematically incorrect. These issues are fixable — the empirical contributions are sound — but they require significant revision of the paper's framing and theoretical claims.

**MY FINAL SCORE:** <score>5.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>