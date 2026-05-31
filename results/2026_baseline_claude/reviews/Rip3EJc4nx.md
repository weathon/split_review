## Summary

HFPrune proposes replacing the conventional one-hot cross-entropy criterion with information entropy of the model's full output distribution as the criterion for Taylor-based neuron importance scoring in structured MLP pruning of LLMs. The key motivation is that cross-entropy only assesses importance relative to a single ground-truth token, whereas information entropy captures the model's global predictive confidence. The method is label-free, avoids the zero-gradient initialization issue present in self-distillation approaches (SDMPrune), and requires no teacher model, achieving 2–3× faster importance scoring. Results are reported across LLaMA and Qwen model families at 20–40% pruning ratios using 10 zero-shot benchmarks.

---

## Strengths

- **Motivated identification of a real problem:** The zero-gradient flaw of SDMPrune at initialization (student and teacher are identical at start, so distillation loss = 0) is a genuine, underappreciated defect. The entropy criterion sidesteps it cleanly and elegantly.
- **Clean and reproducible formulation:** The substitution of C_H(x) for L_CE in Equation 4 is minimal, conceptually clear, and easy to implement without additional infrastructure.
- **Broad evaluation:** Experiments span six model variants (LLaMA2-7B, LLaMA3.2-3.2B, LLaMA3.2-1.2B, Qwen2.5-7B, Qwen2.5-1.5B, Qwen3-1.7B) across ten benchmarks and multiple pruning ratios.
- **Criterion-isolated ablation (Table 6):** The retraining-free comparison of CE, SD, and IE criteria directly validates the importance metric independent of fine-tuning effects, which is methodologically sound.
- **Practical efficiency gains:** Table 5 shows ~3× faster scoring and ~31% lower peak memory than SDMPrune, which is a meaningful engineering advantage.
- **Distribution-level validation (Table 7):** Reporting JS Distance and Top-15 Jaccard Similarity provides a principled sanity check that the entropy criterion indeed better preserves the output distribution, not merely downstream task accuracy.

---

## Weaknesses

### Fatal

None identified with full confidence, but see the Major section on Table 3 data integrity.

### Major

1. **Table 3 data integrity concern.** Multiple rows in Table 3 are byte-for-byte identical across different model families and pruning ratios. Specifically:
   - Qwen2.5-7B 40% SDMPrune = Qwen2.5-1.5B 20% SDMPrune (all 11 values)
   - Qwen2.5-7B 40% HFPrune = Qwen2.5-1.5B 20% HFPrune (all 11 values)
   - Qwen2.5-1.5B 40% SDMPrune = Qwen3-1.7B 20% SDMPrune (all 11 values)
   - Qwen2.5-1.5B 40% HFPrune = Qwen3-1.7B 20% HFPrune (all 11 values)
   The pattern is a systematic one-row downward shift between successive model sections, consistent with copy-paste error rather than parser damage (parser artifacts produce garbled values, not perfectly duplicated ones). This casts serious doubt on the validity of the Qwen-series results, which constitute a major portion of the paper's generalization claims.

2. **Theoretical justification is incomplete.** The paper argues that minimizing Δ(entropy) ≈ preserving the global predictive distribution. However, entropy is not a sufficient statistic for a distribution — two distributions with identical entropy can have arbitrarily different probability assignments. A neuron that causes zero change in entropy could still substantially shift probability mass between tokens. The empirical evidence in Table 7 supports the method's practical benefit, but the causal chain "minimize |Δ H| → preserve P" is not formally substantiated, and the paper does not address this gap.

3. **Narrow baseline comparison in later experiments.** Gradient-free methods (Wanda, FLAP) and reconstruction-based methods (SlimGPT) are cited in related work but never appear in any comparison table. Table 3 compares HFPrune only against SDMPrune, and even Table 1 only has four baselines. At aggressive sparsity (30–40%), omitting competitive baselines limits the reader's ability to judge the paper's standing.

### Minor

1. **Marginal absolute improvements.** The average accuracy gain over the best baseline is 0.8pp (Table 1, 20%) and 0.7pp (30%). The ablation in Table 6 shows 0.5pp over CE without fine-tuning. While consistent, these margins are narrow and may be within variance of the benchmark suite; no confidence intervals or repeated runs are reported.

2. **Uniform pruning ratio across layers.** All MLP layers are pruned at the same ratio ρ_mlp. The paper does not explore or justify this choice, even though later in the conclusion it identifies adaptive per-layer ratios as future work. Layer sensitivity analysis would directly support or challenge this design.

3. **Missing TrQA entry in Table 8.** The table omits TruthfulQA from the ablation of pruning different parts, making it inconsistent with Tables 1 and 6. Averages are therefore computed over 9 vs 10 benchmarks.

### Trivial

None that deserve attention beyond what is listed above.

---

## Nice-to-Haves

- A theoretical bound or informal argument connecting entropy-gradient-based importance to distribution fidelity (e.g., via a Taylor expansion of KL divergence) would significantly strengthen the method's story.
- Standard errors or confidence intervals on zero-shot accuracy would help assess whether 0.5–0.8pp gains are reliable.
- Including Wanda or FLAP as a baseline would show where gradient-free versus gradient-based methods stand at comparable compute budgets.

---

## Novel Insights

The observation that SDMPrune's self-distillation criterion degenerates at initialization—because the student and teacher are the same model, yielding zero loss and zero gradient—is a precise and practically important insight. The proposed resolution (using information entropy of the current model's own output rather than a distillation target) is elegant in that it both fixes the gradient issue and converts a two-model procedure into a single-model one at lower compute. The label-free property falls out naturally rather than being engineered. Whether or not the improvement margins are large, the diagnostic of the zero-gradient flaw and the principled repair represent genuine conceptual progress in criteria for Taylor-based pruning.

---

## Suggestions

- **Audit and correct Table 3.** Verify and re-run (or re-report) the Qwen experiments; provide separate, clearly labeled sub-tables for each model if the data was originally structured that way.
- **Add error bars.** Even single repeated runs would help validate consistency of the 0.5–0.8pp claimed gains.
- **Provide at least one gradient-free baseline** (e.g., Wanda) for context in Tables 1–3.
- **Include a formal or semi-formal argument** connecting entropy gradient to distributional fidelity to support the theoretical narrative.
- **Investigate adaptive per-layer pruning ratios** driven by layer-level entropy sensitivity, as hinted in the conclusion.

---

## Score and Decision

The entropy-criterion idea is clean, well-motivated, and practically useful (label-free, no teacher, no zero-gradient problem). Most experiments in Tables 1, 2, 4–8 are credible. However, the systematic identical-row duplication in Table 3 is a significant data integrity problem that undermines the generalization claims, the theoretical justification has a notable gap, and the empirical gains are modest. The paper requires substantial revision before it can be accepted.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>