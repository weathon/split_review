Now let me carefully verify the key claims from the reviewers against the actual paper content.Now I have all the information I need. The duplication in Table 3 is fully confirmed. Let me write the final consolidated review.

---

## Summary

HFPrune proposes replacing the one-hot cross-entropy (CE) loss with the information entropy (IE) of the model's full output distribution as the criterion for first-order Taylor-based neuron importance scoring in structured LLM pruning. The paper argues that CE ignores all non-label token predictions, while IE provides a holistic, label-free signal that better preserves global prediction fidelity. Additionally, the paper identifies a zero-gradient initialization flaw in self-distillation-based pruning (SDMP-Prune) that makes its importance ranking effectively random at initialization. Results on LLaMA-2-7B, LLaMA-3.2, and Qwen series are presented, with ablations isolating the criterion effect and characterizing distribution-preservation quality.

---

## Strengths

- **Entropy criterion outperforms CE and SD baselines in a clean, fine-tuning-free ablation (Table 6).** On LLaMA-2-7B, IE achieves 53.1% average vs. CE's 52.6% and SD's 51.9% at 20% pruning (no fine-tuning), and 47.3% vs. 46.8%/45.2% at 30% pruning. This provides direct, controlled evidence that the proposed criterion produces better importance estimates independent of downstream fine-tuning.

- **The zero-gradient critique of SD-based pruning is mathematically correct and well-argued.** Section 1 and Section 4.2 correctly identify that at pruning initialization the student and teacher are identical, the KL divergence is zero, and gradients of the KL w.r.t. neuron activations vanish — making initial SDMP-Prune rankings effectively random. This is a genuine flaw identified in a competing method.

- **Substantially better computational efficiency over SDMPrune (Table 5).** HFPrune is ~3× faster and uses 31% less peak GPU memory than SDMPrune when pruning LLaMA2-7B (508.9s vs. 1539.8s; 35.3 GB vs. 51.2 GB), because it avoids the teacher forward pass entirely. The advantage scales consistently across model sizes (1.2B, 3.2B, 7B).

- **Distribution preservation is quantitatively confirmed (Table 7).** Over 5,000 C4 prompts on LLaMA-2-7B, IE achieves lower JS Distance (0.241 vs. 0.243 at 20%; 0.353 vs. 0.362 at 30%) and higher Top-15 Jaccard Similarity (0.445 vs. 0.439; 0.595 vs. 0.588) than CE, with the advantage growing at higher compression. This directly validates the theoretical motivation.

- **Consistent gains on LLaMA models across scales (Tables 1 and 2).** HFPrune outperforms LLM-Pruner, LoRAPrune, and SDMPrune at both 20% and 30% pruning on LLaMA-2-7B, LLaMA3.2-3.2B, and LLaMA3.2-1.2B, with a clear performance ordering maintained.

- **MLP-only pruning justification via ablation (Table 8).** Pruning only MLP modules consistently outperforms pruning attention + MLP at both 20% (61.9% vs. 60.3% with fine-tuning) and 30% (60.0% vs. 58.0%), supporting the design decision to focus on MLP modules.

---

## Weaknesses

### Fatal

- **Table 3 contains systematic copy-paste duplication that invalidates key Qwen results.** A direct element-by-element comparison reveals:
  - The Qwen2.5-1.5B@20% rows (both SDMPrune and HFPrune) are identical to the Qwen2.5-7B@40% rows, value-for-value across all 10 benchmarks and the average.
  - The Qwen3-1.7B@20% rows (both methods) are identical to the Qwen2.5-1.5B@40% rows, value-for-value.

  Concretely: Qwen2.5-1.5B@20% SDMPrune = 32.3, 59.2, 72.1, 56.2, 35.2, 72.0, 37.7, 43.6, 44.7, 58.2 (avg 51.1), which is character-for-character identical to Qwen2.5-7B@40% SDMPrune. The same exact duplication holds for all four affected rows. This is not coincidence — the probability of two different models at different pruning ratios producing the same ten benchmark scores is negligible. The paper uses Table 3 to support the claim of "consistent outperformance across the LLaMA and **Qwen** series models" (abstract). With the Qwen2.5-1.5B@20% and Qwen3-1.7B@20% data provably duplicated, the "20%" Qwen results for those two models do not reflect actual experiments, and the claim of broad Qwen generalization is partially unsupported. The rest of Table 3 (Qwen2.5-7B rows and 30% rows for smaller models) may be correct, but the systematic pattern of duplication casts doubt on data-entry discipline throughout the table.

### Major

- **The headline claim of "exceeding the original dense model" is confounded by asymmetric fine-tuning.** Section 5.2.1 and the abstract state that at 20% pruning HFPrune (59.0%) outperforms the original LLaMA-2-7B (58.3%). However, the pruned model was fine-tuned for 2 epochs on LaMini, while the original unpruned model was not fine-tuned at all. This comparison conflates the effect of pruning with the effect of fine-tuning on LaMini. If the unpruned model were fine-tuned on the same dataset under the same protocol, its accuracy would almost certainly improve further. The comparison as framed overstates the benefit of the pruning criterion itself. Note that Table 8's "mlp w/ tune" achieves 61.9% at 20% pruning — substantially above the unpruned baseline — further suggesting that fine-tuning is the dominant factor in exceeding the original model.

- **Fine-tuning conditions for baselines in Table 1 are not verified to be controlled.** The paper states it uses LaMini-instruction "across all experiments for fair comparison" (Section 5.1), but does not explicitly state whether all compared methods (LLM-Pruner, LoRAPrune, SDMPrune) were re-run by the authors under identical fine-tuning hyperparameters, or whether their results were taken from the original papers. Since fine-tuning hyperparameters (learning rate, LoRA rank, number of epochs) strongly affect final performance, uncontrolled fine-tuning would mean the performance gaps in Table 1 are not attributable solely to the importance criterion.

### Minor

- **Table 4 text–table discrepancy.** Section 5.2.2 states "pruning 30% of the MLP layers results in a 1.47× speedup in prefill latency," but Table 4 clearly shows 57.5 ms → 42.1 ms = 1.35×. The stated figure of 1.47× does not match the reported table entry.

- **Table 8 and Table 6 use inconsistent benchmark sets without disclosure.** Table 6 reports averages over 10 benchmarks (including TruthfulQA, column labeled "TrQA"), while Table 8 reports averages over 9 benchmarks (TruthfulQA column is absent). The same configuration — MLP-only, no fine-tuning, 20% pruning — yields different-looking numbers in the two tables: "IE (ours)" in Table 6 averages 53.1% and "mlp w/o tune" in Table 8 averages 54.8%. The paper does not flag this distinction, making cross-table comparison misleading.

- **The criterion effect in the clean ablation is modest.** IE outperforms CE by 0.5 pp at both pruning ratios in Table 6. This is a real but small improvement. The paper's characterization of "clear superiority" is somewhat overstated; the actual margin is within the noise range of zero-shot benchmark evaluation. This does not invalidate the contribution but warrants more careful language.

### Trivial

- None beyond the numerical inconsistency noted under Minor.

---

## Nice-to-Haves

- **Extend the no-fine-tuning ablation (Table 6) to Qwen models and LLaMA-3.2.** The 0.5 pp advantage of IE over CE is shown only on LLaMA-2-7B. Demonstrating a consistent advantage across architectures in a controlled, fine-tuning-free setting would substantially strengthen the central claim and distinguish it from architecture-specific noise.

- **Characterize which neurons each criterion selects differently.** Table 7 measures output-behavior similarity, but a ranking correlation analysis or visualization of score distributions between IE and CE importance scores would provide mechanistic insight into *why* IE produces better estimates. This would transform the paper from "IE works better empirically" to "IE works better because it selects structurally different neurons."

- **Explain the source of the 3× pruning efficiency gain more explicitly.** The paper attributes the efficiency advantage to not requiring a teacher model, but a brief calculation showing the time breakdown (teacher forward pass vs. entropy computation) would make the claim more concrete and reproducible.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[Harsh Critic — "gradient-space terms" request]:** The critic asked the paper to state the CE vs. IE comparison "in gradient-space terms." This is a presentation suggestion that does not constitute a weakness; Figure 1 and the conceptual description in Section 4.2 adequately convey the difference. Removed as a style nitpick.

- **[Strength Finder — "surpasses original dense model"]:** Removed as a standalone strength because the comparison is confounded by fine-tuning (see Major weakness above). The factual claim that 59.0% > 58.3% is not disputed; the interpretation that the pruning criterion is responsible for this is.

- **[Harsh Critic — "comparison scope in Table 3 (brevity justification)"]:** The criticism that only SDMPrune appears in Table 3 is secondary and speculative about intent; other methods may not have been applied to Qwen models by their authors. Removed as scope creep — the more serious issue (data duplication) already covers Table 3.

- **[Harsh Critic — "efficiency of entropy computation not explained"]:** The paper provides sufficient conceptual explanation (no teacher forward pass needed) to understand the advantage. The demand for a detailed breakdown is a nice-to-have rather than a weakness; downgraded accordingly.

---

## Novel Insights

The paper's identification of the zero-gradient initialization problem in self-distillation-based Taylor pruning is a genuine and precise methodological insight: at initialization, when student equals teacher, the KL divergence is zero and its gradient with respect to any neuron activation is zero (because the Jacobian of the softmax sums to zero), making the initial importance ranking effectively random. This is a concrete, verifiable flaw in SDMP-Prune that has not been articulated in prior work based on this review. The entropy criterion as a fix is elegant and efficient. However, the empirical evidence for this insight (the clean ablation showing SD loss performing *worse* than CE — 51.9% vs. 52.6% at 20% pruning in Table 6) supports the critique and is a notable finding in its own right.

---

## Suggestions

1. **Correct Table 3 immediately.** The Qwen2.5-1.5B@20% and Qwen3-1.7B@20% rows must be replaced with the actual experimental results. Audit all other rows in Table 3 for similar errors.

2. **Add a comparison to Table 1 where the original LLaMA-2-7B is also fine-tuned on LaMini**, or clearly present a fine-tuning-controlled comparison, to separate the effect of the entropy criterion from the effect of fine-tuning. Without this, the "exceeds original model" headline claim is misleading.

3. **State explicitly whether baselines in Table 1 were re-run or reproduced from their respective papers**, and if re-run, report the fine-tuning hyperparameters used for each method.

4. **Fix the text–table discrepancy in Section 5.2.2**: update "1.47×" to the correct "1.35×" speedup.

5. **Align benchmark counts between Tables 6 and 8**, or add a footnote explaining that Table 8 excludes TruthfulQA. The "Average" columns across tables must be computed over the same benchmark set, or the difference must be disclosed.

---

## Evaluation on Key Axes

- **Originality:** Moderate. Using information entropy instead of CE for Taylor importance scoring is a simple, well-motivated substitution. The zero-gradient critique of SDMP-Prune is the most original analytical contribution.
- **Importance:** The efficiency and memory savings over distillation-based methods are practically meaningful. The core idea is applicable beyond LLM pruning.
- **Claims supported:** The LLaMA claims (Tables 1, 2) and clean ablation claims (Tables 6, 7, 8) are well-supported. The Qwen generalization claims (Table 3) are partially invalidated by data duplication. The "exceeds original model" claim is not fairly supported.
- **Soundness of experiments:** LLaMA experiments and ablations appear sound. Table 3 has a serious data integrity failure.
- **Clarity:** Generally clear, but the text–table discrepancy and inconsistent benchmark counting reduce confidence in numerical reporting.
- **Community value:** Moderate. A corrected and verified version of this paper would be a clean incremental contribution suitable for publication. The current version requires significant correction.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>