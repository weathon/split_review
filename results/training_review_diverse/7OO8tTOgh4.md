Now I have all the information needed to produce the consolidated review. Let me write it.

## Summary

This paper proposes Maximizing Information Entropy (MIE), a non-targeted white-box adversarial attack on vision-language models (VLMs). Unlike prior methods that require ground-truth captions, MIE maximizes entropy across three decoder components — logits, attention weights, and hidden states — to degrade the model's image understanding. Experiments on five VLMs (BLIP, BLIP2, InstructBLIP, MiniGPT-4, LLaVA) show CLIP score drops from ~30 to ~20 and a 96.88% average attack success rate.

## Strengths

1. **First non-targeted attack operating without ground-truth captions**: The paper is the first to show that a VLM can be attacked in a non-targeted manner using only the model's own outputs, without requiring authentic image descriptions (Section 2.2, Section 3). Prior work (Schlarmann & Hein, 2023) required ground-truth captions as supervisory signals. This is a meaningful practical difference for open-world scenarios.

2. **High effectiveness across diverse VLM architectures**: MIE achieves consistent results across both "Image as Key-Value" models (BLIP) and "Image as Token" models (LLaVA, MiniGPT-4), with CLIP score reductions substantially exceeding comparison methods (Carlini et al., Schlarmann & Hein, Aafaq et al.) by more than 2 points on multiple models (Table 1). The method is architecture-agnostic by design.

3. **Mechanistic insight via internal state visualization**: Figure 4 directly validates the entropy maximization rationale by showing attention heatmaps and hidden state distributions transitioning from concentrated to dispersed as the attack progresses. This goes beyond reporting aggregate metrics and provides evidence that the attack works as intended.

4. **Systematic ablation study**: Figure 3 investigates loss coefficients, perturbation size, and iteration count, identifying an optimal λ₁:λ₂:λ₃ ratio of ~8:1:1 and showing that attack effectiveness plateaus at ε ≥ 8. These results offer practical guidance for applying the method.

## Weaknesses

### Fatal
None.

### Major
- **Ablation only on one model (BLIP)**: The ablation study (Figure 3) is conducted exclusively on BLIP. Given the architectural differences across models (Image-as-Key-Value vs. Image-as-Token), the optimal coefficients and component contributions may vary. The paper acknowledges this briefly ("For different models, additional coefficient settings may generate better results") but does not provide ablation data for any second model. This limits the generality of the design choices.

- **Logit-only baseline absent from main results table**: The ablation shows that the logit term dominates (optimal λ₁:λ₂:λ₃ ≈ 8:1:1), but the main comparison table (Table 1) does not include a logit-only ablation baseline. Without seeing whether the full joint attack significantly outperforms λ₁-only across multiple models, the paper's central claim that all three components are necessary is incompletely supported. The current evidence only shows this on BLIP (Figure 3a).

### Minor
- **Manual evaluation details underspecified**: The paper reports a 96.88% attack success rate from "manual evaluation" (Table 2 caption, line 219) but does not state the sample size used for human inspection, the number of annotators, or inter-annotator agreement. If all 1000 images were manually judged, that should be explicit; if only a subset, the sampling procedure is needed. This does not invalidate the results but weakens reproducibility.

- **Attack success rate metric lacks granularity**: The binary "factually inaccurate" criterion (line 200) counts both fluent-but-wrong outputs and incoherent gibberish as successful attacks. The paper acknowledges that outputs can be "illogical and incoherent" (Figure 5). Reporting auxiliary metrics (e.g., perplexity of outputs, proportion of outputs that are fluent-yet-false, BLEU against plausible descriptions) would better distinguish meaningful degradation from trivial gibberish and strengthen the claim of practical security risk.

- **Gradient flow through autoregressive generation underspecified**: The paper states that "gradients of the target can be obtained through backpropagation" (line 121) but does not clarify how the autoregressive generation loop handles the discrete token selection. In standard implementations this is straightforward — the entropy is computed on differentiable probability distributions (softmax of logits), and the argmax-selected tokens from previous steps are treated as constants (detached) during backpropagation, so gradients flow to the image via cross-attention. However, the paper should state this explicitly for reproducibility. (This is a clarity issue, not a foundational flaw; the approach is standard and implementable.)

- **No computational cost analysis**: The attack requires 100 PGD iterations, each involving a full autoregressive forward pass through the decoder. Reporting average GPU time per image would help readers assess practicality (Table 2 caption mentions "considerable cost associated with human resources" but the computational cost of the attack itself is not discussed).

- **No discussion of perturbation perceptibility**: The paper uses L∞ ε=8, which is standard, but does not provide qualitative examples showing whether the resulting perturbations are visible to humans. For captioning tasks, human perceptibility matters more than for classification since the output is used by end users.

### Trivial
None.

## Nice-to-Haves
- Include the logit-only (λ₁) and the two individual component baselines (λ₂-only, λ₃-only) in Table 1 to directly demonstrate the value of the joint attack.
- Run the ablation study on at least one additional architecture (e.g., LLaVA as an Image-as-Token model).
- Report perplexity, coherent prefix length, or proportion of fluent-yet-wrong outputs alongside the attack success rate.
- Provide examples showing whether the L∞ ε=8 perturbations are visually perceptible.
- Report per-image GPU time for the 100-step PGD attack.

## Removed Points

- **"Missing specification of how gradients are computed through autoregressive generation (foundational flaw)"**: This criticism misunderstands the gradient computation. The entropy objective (Eq. 2–4) is computed on differentiable probability distributions (softmax of logits), not on the discrete token outputs. The token selection (argmax) determines which context is fed to the next step, but those tokens are treated as constants during backprop — the gradient flows to the image through the differentiable cross-attention and language model paths. This is standard practice in white-box attacks on autoregressive models and does not require Gumbel-Softmax or straight-through estimators. The approach is reproducible and the gradient flow is correct. The paper could be more explicit about this, but it is not a fatal or even major flaw — it is at most a minor clarity gap.

- **"Overclaimed novelty"**: The paper's claim of being "the first to evaluate the non-targeted adversarial robustness of VLMs without real supervisory signals" (line 21) is appropriately scoped. The acknowledged closest work (Schlarmann & Hein, 2023) uses ground-truth captions, which is a real supervisory signal. The reviewer's suggested alternatives (maximizing cross-entropy with a random caption, minimizing likelihood of the model's own clean caption) either reduce to targeted attacks with random targets (which the paper compares against via Carlini et al.) or still require some form of signal. The novelty claim is reasonable and measured.

- **"Non-targeted attack vs specific instantiation"**: Entropy maximization is a well-motivated choice for non-targeted attacks because it makes no assumptions about what constitutes a "wrong" output. The paper clearly explains this motivation (Section 2.3, Section 3). The fact that other instantiations exist does not weaken the paper's contribution.

- **Pure formatting/style nitpicks and missing appendix content**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
1. Clarify the gradient computation procedure in Section 3.5: state that during the autoregressive forward pass, the previously generated tokens are detached from the computation graph (treated as constants), and the entropy loss is computed on the differentiable output probability distributions. This will address the main reproducibility concern.
2. Add logit-only and single-component baselines to Table 1, or add a supplementary table showing per-component results across all models.
3. Extend the ablation study to at least one additional VLM architecture (e.g., LLaVA) to support the claim that the λ ratio generalizes.
4. Report the sample size and number of annotators for the manual evaluation of attack success rate (Table 2).

## Score and Decision

The paper proposes a well-motivated, novel attack method for VLMs that is the first to operate without ground-truth captions. The experimental results demonstrate clear effectiveness across diverse architectures. The weaknesses are primarily about presentation completeness (underspecified manual evaluation, ablation on one model only, missing individual-component baselines in the main table) rather than fundamental methodological flaws. The gradient concern raised by the reviewer is based on a misunderstanding and does not threaten the paper's validity. The paper would benefit from addressing the listed minor and major issues, but in its current form it represents a solid contribution to the field of VLM robustness evaluation.

**Originality**: Good — first non-targeted attack without ground-truth captions.  
**Importance**: Good — VLMs are widely deployed and their robustness is a timely concern.  
**Claims support**: Adequate — main results are clear but some evaluation details are underspecified.  
**Soundness**: Adequate — methodology is sound but would benefit from stronger ablation evidence across models.  
**Clarity**: Adequate — generally clear but could better specify implementation details (gradient handling, manual eval).  
**Value**: Moderate to good — provides a practical benchmark for evaluating VLM robustness.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>