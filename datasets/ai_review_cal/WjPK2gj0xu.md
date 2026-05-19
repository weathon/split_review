- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes MMER, a training-free approach for composing multiple MLLMs (image, audio, video, point cloud) into a unified model. MMER merges the LLM parameters via TIES and then constructs modality-specific binary masks that decouple the merged parameters back into approximately modality-private subspaces. This enables dynamic parameter routing during inference. The method is evaluated across multimodal expansion (Table 1), retention of original MLLM performance (Table 2), and catastrophic forgetting mitigation (Tables 3–4). The core idea—using masks derived from comparing original vs. merged task vectors to recover modality-specific parameters without additional training—is novel and empirically effective.

## Strengths

1. **Significant and clean empirical improvement over training-free baselines on multi-modality benchmarks (Table 1).** MMER achieves 59.6% average accuracy on MCUB, outperforming the best training-free baseline (TIES-DARE, 55.4%) by over 4 points, with similar margins on MUSIC-AVQA and ModelNet40+image. This directly demonstrates that the mask-based decoupling (Eq. 4–6) reduces cross-modal interference without training.

2. **Near-perfect retention of original MLLM performance across 14 dual-modal benchmarks covering four modalities (Table 2).** MMER retains 99.6% (trimmed average) of original zero-shot performance, while the strongest training-free baseline (NaiveMC-DARE) retains only 63.9%. The individual per-task results are reported, giving transparency. This is the paper's most striking result.

3. **Effective catastrophic forgetting mitigation in both single-task and cross-modal multi-task settings (Tables 3, 4).** MMER retains ~98% of previous-task performance while matching fine-tuned MLLMs on new tasks (e.g., 81.8% on Flickr30k vs. 82.0%). It outperforms the dedicated MLLM forgetting-mitigation method Model Tailor in both single-task (98.3% vs. 91.69% retention) and multi-task settings (97.9% vs. 91.60%), all without training on old tasks.

4. **Principled analysis of mask sparsity and hyperparameters (Figure 4).** Figure 4a shows the audio mask selects only 2.2% of parameters yet retains performance, consistent with prior findings on task-vector redundancy. Figure 4b systematically maps the interaction between Top-K% sparsity and the λ scaling factor, providing practical guidance.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison with DAMC weakens the central "bypassing the trade-off" narrative.** The paper motivates MMER by describing a trade-off between NaiveMC (training-free but low performance) and DAMC (training-required but better results), then claims MMER "bypasses" this trade-off (Introduction, lines 25–27; Section 2.2, line 52). Yet the paper explicitly excludes DAMC from all comparisons (Section 4.2, line 160: "We excluded the comparison with DAMC framework ... as its reliance on additional training introduces variables that could compromise the fairness of our experimental evaluation"). The paper's justification confuses the issue: the central claim is precisely *about* the relationship to DAMC. If DAMC still outperforms MMER on expansion benchmarks, the paper has not bypassed the trade-off—it offers a different operating point (training-free with moderate performance vs. training-required with potentially higher performance). If MMER matches or exceeds DAMC, that would strongly support the contribution. Either outcome is informative, and the omission prevents readers from verifying the paper's most distinctive positioning claim. This does not invalidate MMER's other demonstrated strengths (retention, forgetting mitigation, outperforming training-free baselines), but it leaves a gap in the evidence for a claim the paper itself foregrounds.

### Minor

- **The "Trimmed Avg" in Table 2 excludes three point-cloud and audio classification tasks without adequate justification.** The caption states "Trimmed Avg represents the average result obtained after excluding three point or audio classification tasks" (line 180), and the same exclusion appears in the ablation study (Table 5, line 213). The paper does not explain why these particular tasks are excluded from the aggregate. Since individual per-task results are reported, the full average could be computed by readers, but the presentation gives the appearance of selective reporting. A brief justification (e.g., "these are classification rather than QA tasks, making their metrics not directly comparable") would resolve this.

- **The mask construction derivation is presented as a rigorous optimization but is heuristic.** The paper introduces the mask condition via an ℓ₁ minimization (Eq. 2) and derives the 50% threshold from |τᵢ| ≥ |τ_∗ – τᵢ| (line 81). The derivation is sound in the special case where signs agree and |τ_∗| ≥ |τᵢ|, but the introduction of the λ hyperparameter (line 81–84) is a post-hoc relaxation not justified by the optimization problem. This is standard practice for an empirical paper, but the presentation over-claims mathematical rigor. Reframing as "we approximate the optimal mask by …" would avoid misleading readers.

- **The text-mask averaging strategy in §3.2.1 (using the average mask m̄ for text tokens) is a design choice without ablation.** The paper uses the average of all modality-specific masks for processing text, without comparing to alternatives (union of masks, original merged weights, task-vector only). While the overall ablation in Table 5 validates parameter decoupling as a whole, this specific design choice is unexamined. Adding one row to the ablation would clarify its importance.

### Trivial
- The λ values used for each modality are not reported, making replication harder (only aggregate hyperparameter analysis in Figure 4b is given).

## Nice-to-Haves
- A discussion of how mask construction cost scales with the number of MLLMs being merged.
- Reporting the full untrimmed average for Table 2 alongside the trimmed average.
- Error bars or variance estimates on key results, since fine-tuning and validation-set choices introduce variability.

## Removed Points

These points were flagged but are removed because they are either: (a) unsupported by the paper, (b) speculative, (c) about information stripped by the PDF parser, (d) misreadings, or (e) generic nitpicks.

- **"The paper does not specify fine-tuning details"** — Removed because the paper states it "follow[s] prior works" (line 153). Any further details are in the appendix, which is stripped by the parser. Per review guidelines, missing-appendix criticisms are not admissible.
- **"No comparison with continual learning baselines (EWC, replay)"** — Removed because the paper compares against Model Tailor, the closest MLLM-specific prior work (line 193). General continual learning methods are outside the paper's scope; the paper frames its contribution in the MLLM composition setting.
- **"Strength Finder claim that MMER is 'competitive with or superior to DAMC'"** — Removed because the paper never makes this claim. The Strength Finder fabricated this assertion; the paper only says it "bypasses the trade-off" without providing a DAMC comparison.
- **"λ hyperparameter tuning conflicts with 'training-free' claim"** — Removed because "training-free" in the model merging literature means no gradient-based optimization, not "no hyperparameters." Validation-set tuning of hyperparameters (α, λ, K) is standard in this line of work and is explicitly disclosed (lines 67, 81).
- **Mask derivation "gap" beyond what is noted above** — The harsh critic asserted the 50% threshold "ignores the scaling factor λ." This is incorrect: λ is introduced *after* the 50% derivation as a separate refinement, which the paper clearly states ("we introduce a scaling factor λ_i to refine the selection process"). The 50% stands on its own from the inequality |τᵢ| ≥ |τ_∗ – τᵢ| under same-sign conditions; λ is an empirical adjustment layered on top. The retained minor weakness (above) captures the real issue: the presentation over-claims rigor, not that the math is wrong.
- **"Reproducibility concern about DAMC not being available"** — Removed per hard rule: if the paper cites it, it exists.
- **Pure formatting/style nitpicks** — Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the work that the authors themselves do not identify.

## Suggestions

1. **Compare with DAMC** on the same expansion benchmarks (Table 1). Even if DAMC uses training, the results are essential to evaluate the "bypassing the trade-off" claim. Report the gap and discuss the practical implications of being training-free even if DAMC outperforms MMER.

2. **Justify the trimmed average** in Table 2 explicitly, or report the full untrimmed average alongside it. The individual task results are fine; the concern is only about how the headline number is presented.

3. **Report the λ values used for each modality** and the specific validation tasks used for tuning, to improve reproducibility.

4. **Add an ablation comparing text-mask averaging** (m̄) against alternatives (union of masks, no mask, etc.) to show this design choice's impact.

5. **Re-frame the mask derivation** (§3.1) to clarify that the 50% condition is derived from the exact ℓ₁ solution but λ is a heuristic relaxation, rather than implying the whole formula follows from optimization.
