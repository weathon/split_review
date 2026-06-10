Now let me write the final consolidated review.

---

## Summary

DeCoRe proposes a training-free decoding strategy that integrates mechanistic interpretability findings (retrieval heads) with contrastive decoding. The idea is to mask pre-identified retrieval heads to create a hallucination-prone model variant, then contrast the base and masked models' next-token distributions — with dynamic weighting controlled by the conditional entropy of the base model's predictions — to suppress hallucinated outputs. The method is evaluated on Llama3-8B and 70B across faithfulness, factuality, and reasoning benchmarks.

## Strengths

- **Novel and well-motivated integration of mechanistic interpretability with decoding.** The paper directly leverages the discovery of retrieval heads (Wu et al., 2024) — attention heads responsible for extracting contextual information — to construct an expert/amateur contrast. This bridges two previously separate lines of work (mechanistic interpretability and contrastive decoding) in a way that is both principled and practical.

- **Large, verifiable gains on faithfulness tasks.** DeCoRe-Entropy achieves an 18.6% improvement on XSum summarisation (abstract, line 9) and 74.14% Macro Accuracy on MemoTrap (line 209), substantially outperforming all six baselines on several faithfulness metrics. These are not marginal gains and are reported with concrete numbers tied to specific datasets.

- **Training-free while competitive with trained baselines.** DeCoRe is competitive with ITI on TruthfulQA (53.00% intersection of truthfulness and informativeness, line 224) despite ITI requiring supervised training on TruthfulQA data (line 177). This is a meaningful practical advantage.

- **Well-designed ablation with three controlled variants.** The decomposition into DeCoRe-Static, DeCoRe-Entropy, and DeCoRe-Entropy-Lite (Section 4.5) cleanly isolates the contribution of the entropy-based dynamic weighting from the core contrastive mechanism.

- **Systematic correlation analysis varying the number of masked retrieval heads N.** Section 4 (lines 252–270) analyzes how varying N affects performance across task types, revealing nuanced patterns (positive correlation for XSum/MemoTrap, negative for IFEval and factual recall tasks). This provides mechanistic insight and honestly surfaces where the method's assumptions hold or break.

- **Evaluation across two model scales (8B and 70B) and extension to multi-hop reasoning.** Results on both Llama3-8B-Instruct and Llama3-70B-Instruct show the method's benefits hold at both sizes, and the MuSiQue results in the open-book CoT setting (74.47% EM, line 244) demonstrate applicability beyond simple QA.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims (improved faithfulness) are supported by strong empirical evidence. The issues below are real but do not threaten the paper's main contribution.

### Minor

- **Framing–evidence mismatch on marginal results.** The paper uses language like "significantly improves" (lines 38, 321) for results that are genuinely strong on faithfulness tasks, but the same phrasing is applied to very marginal improvements. On MuSiQue closed-book CoT, DeCoRe improves EM from 14.61% to 14.69% for Llama3-8B and from 20.15% to 20.60% for Llama3-70B (lines 243–245) — ~0.08 and ~0.45 percentage points, respectively. These are negligible in practical terms. The paper partially acknowledges this in the limitations (line 326: "only marginal enhancements in factual recall tasks"), but the body text describing those same results uses enthusiastic framing that is not calibrated to the effect sizes. The paper would be stronger if it directly stated which tasks see substantial improvements (faithfulness) and which see only marginal gains (closed-book factuality, some reasoning settings) rather than promoting all results with equal force.

- **The core assumption about contrastive selectivity is not directly validated.** The paper's mechanism assumes that masking retrieval heads creates a "hallucinating" model whose distribution differs from the base model's in a *selective* way — i.e., the masked model assigns disproportionately higher probability to hallucinated tokens. The paper validates that the masked model is worse on average (app:res_baseline_masked) and provides one illustrative example (Figure 2), but does not present a per-token analysis showing that the *differences* between p_base and p_masked are concentrated on incorrect/hallucinated tokens as opposed to being a diffuse shift. A direct analysis — e.g., comparing p_base / p_masked ratios for correct vs. incorrect tokens — would either confirm or refute this assumption and would be more informative than an additional benchmark. This is a gap in the paper's theoretical grounding, though it does not invalidate the empirical results (contrastive decoding can work even without strict selectivity, as the field's standard practice shows).

- **Inference cost is not discussed.** DeCoRe requires a forward pass through both the base model and the masked model (which is architecturally identical to the base model). This doubles the inference cost relative to greedy decoding and is a strictly higher cost than methods like DoLa that only require one forward pass. The paper should explicitly discuss this trade-off, especially when comparing to single-forward-pass baselines. This is a practical concern for deployment decisions.

### Trivial

- None.

## Nice-to-Haves

- **Selectivity analysis.** As noted above, a direct per-token analysis of p_base / p_masked ratios across correct and incorrect tokens would strengthen the theoretical grounding of the method.
- **Entropy trajectory analysis.** A comparison of H(x_t) trajectories across generation steps for DeCoRe-Static vs. DeCoRe-Entropy vs. baseline would clarify whether the dynamic mechanism is stabilizing uncertainty or introducing oscillations.
- **Statistical significance.** Some reported improvements are very small (0.08 EM points). Including confidence intervals or significance tests across multiple runs would help readers assess which improvements are reliable.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- **"The contrastive mechanism relies on an unverified assumption about selectivity — the masked model might just be uniformly more uncertain."** The specific claim about "uniform uncertainty" is mathematically incorrect: if p_masked is uniform across the vocabulary, log p_masked is constant, and Eq. (5) reduces to a constant rescaling of p_base, preserving token rankings. The broader selectivity point is retained as a Minor weakness (above), but the "uniform noise" framing is removed.

- **"The entropy-controlled dynamic mechanism has a circularity problem."** The paper provides empirical validation through ablation studies (DeCoRe-Static vs. DeCoRe-Entropy, Section 4.5) and entropy analysis showing DeCoRe reduces entropy over time (Section 4, line 272–287). The concern about feedback instability is speculative and unsupported by the evidence on the page. Removed.

- **"The number of masked retrieval heads N is underspecified for main experiments."** N may be specified in the stripped appendix (app:implementation_details). Per the review guidelines, weaknesses about missing appendix content are removed as they reflect parser issues, not author errors.

- **"NQ-Swap task definition is unclear."** The paper states (line 149): "NQ-Swap is a version of NQ where the answer entity in the context was replaced with another entity and is used to evaluate the faithfulness of the model to the modified context." This description is sufficiently clear — the ground truth is the swapped entity in the modified context.

- **"Related works missing."** The paper's related work coverage is adequate for its scope. No removal needed as this was not raised, but noted for completeness.

- **Strength Finder claim about "training-free while competitive with trained baselines."** Kept — this is accurate and well-supported by the paper.

## Novel Insights

None beyond the paper's own contributions. The key insight — that retrieval heads identified through mechanistic interpretability can be masked to construct an informative amateur model for contrastive decoding, with entropy-based dynamic weighting — is the paper's contribution, not a synthesis from the reviews.

## Suggestions

1. **Calibrate the claims in the results section.** Replace "significantly improves" with more measured language for settings where improvements are marginal (e.g., closed-book CoT on MuSiQue). The limitations section already acknowledges this honestly; the body text should match.

2. **Add a per-token selectivity analysis.** Compute p_base / p_masked ratios for correct vs. incorrect tokens on a sample of generations to directly validate that the contrastive signal is selective.

3. **Discuss inference cost explicitly.** State that DeCoRe requires two forward passes and explain the practical trade-off relative to single-pass baselines.

4. **Report the specific N value used for main experiments** (if not already in the appendix, include it in the main paper's experimental setup section).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>