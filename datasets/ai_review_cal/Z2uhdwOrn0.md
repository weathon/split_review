- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have full verification of the paper content. Let me construct the final review.

## Summary

This paper proposes SpARQ, which replaces standard attention softmax with a Softmax₁ activation (adding 1 to the denominator) plus a max-shift stabilization module to reduce outliers when adapting pretrained LLMs (OPT models) to multimodal speech-text tasks via LoRA and post-training quantization. On OPT-1.3b, SpARQ reports 41% relative improvement under LoRA, 45% under PTQ, and 1.33× training speedup.

## Strengths

- **Consistent and substantial PTQ improvements across all model sizes and quantization methods (Table 1).** Under AffineQuant W4A4 on OPT-1.3b, the vanilla framework's average performance drop is 165.33% while SpARQ reduces this to 90.68% — a gap too large to attribute to noise. The pattern holds across SmoothQuant, AffineQuant, and OmniQuant, and across all three model sizes (125M, 350M, 1.3B).

- **Quantitative evidence of outlier reduction (Figure 3).** SpARQ produces lower kurtosis and lower max infinity norms than the vanilla framework across text, speech, and cross-modal (ASR) inputs. This provides a mechanistic link between the architectural change and the claimed benefit, beyond just task metric improvements.

- **Well-executed ablation isolating the stabilization method (Table 4).** The paper shows that L₁ normalization and mean-centering both lead to NaN losses, while max-shift uniquely enables stable training. This empirically justifies the design choice and goes beyond simply copying prior work.

- **Evaluation across three model sizes (125M, 350M, 1.3B) and two LoRA variants (LoRA, QLoRA).** The pattern of smaller performance drops for SpARQ is consistent, not a single lucky configuration.

## Weaknesses

### Major

- **The vanilla LoRA baseline degrades catastrophically, making the headline 41% relative improvement claims hard to interpret.** The paper reports (line 157) that vanilla ASR WER goes from 8.00% (full rank) to 46.92% under LoRA — a ~486% relative increase. Such a dramatic collapse is atypical of standard LoRA on well-tuned architectures and raises the possibility that the vanilla baseline was not properly optimized for the multimodal setting. The paper provides rank (128) and alpha (256) but no learning rate, optimizer, convergence curves, or evidence that the vanilla LoRA training was stable. If the vanilla model is essentially failing on ASR/TTS under LoRA, then SpARQ's relative advantage may stem more from making a poorly-tuned system work than from solving a fundamental outlier problem. This concern applies primarily to the LoRA experiments (Tables 2); the PTQ experiments (Table 1) are less susceptible since both frameworks use the same frozen weights and only differ in quantization behavior.

- **Only one model family (OPT) is evaluated, limiting generalizability.** The paper acknowledges this in its limitations (not testing LLaMA or 6.7B models) but the claims about SpeechLM broadly would be significantly stronger with at least one additional architecture. Without it, the reader cannot tell whether the benefit is specific to OPT's pretraining or general.

### Minor

- **Core methodological novelty is modest.** The central architectural change (Softmax₁) is taken directly from Hu et al. (2024a). The paper's original contribution is the stabilization module (max-shift) that enables transferring pretrained vanilla LLM weights into the outlier-free architecture without retraining from scratch — a practical engineering contribution but not a new principle. The paper would benefit from a clearer statement of what is new vs. what is adapted.

- **Theoretical propositions (3.1, 3.2) are informal restatements of prior results and not connected to the experiments.** Proposition 3.2 invokes sub-quadratic training efficiency, but the actual measured speedup (1.33×) is modest and could arise from engineering factors. The theory section adds rhetorical weight without providing testable predictions or insight specific to the SpeechLM setting.

- **Missing optimization hyperparameters for reproducibility.** The paper does not report learning rates, optimizer choice, batch size, number of epochs, or learning rate schedule for any of the experiments. While the training procedure "follows (Hu et al., 2024a)" for full-rank fine-tuning, the LoRA-specific training setup is underspecified. This makes independent verification difficult.

- **No comparison to alternative attention stabilization approaches.** Baselines such as attention clipping, learned temperature scaling, or increasing dropout would contextualize whether Softmax₁ is uniquely beneficial or one of several viable options.

### Trivial

None.

## Nice-to-Haves

- Add convergence curves for the vanilla and SpARQ LoRA training runs to demonstrate both frameworks reached a stable minimum.
- Report standard deviations for key configurations (the paper states they are <2% but omits them).
- Include qualitative examples (e.g., generated speech samples or attention maps) to illustrate differences.
- Ablate the Softmax₁ contribution separately from the stabilization module (softmax+max-shift vs. Softmax₁+max-shift).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Lack of error bars and significance tests"** — The paper explicitly states (line 139) that each experiment was run 3 times and standard deviations were <2%, but omitted from tables for brevity. This is a reasonable presentation choice, not a missing analysis.
- **"Appendix theorems unavailable"** — The appendix is stripped by the PDF parser; the original submission contains it. Not a valid criticism.
- **"Introduction claims without evidence that outliers from LoRA/PTQ are distinct"** — The paper cites Crabbé et al. (2024) for multimodal outliers and does not need to prove the outliers are "distinct" from those in plain LLMs; it only needs to show SpARQ mitigates them, which it does empirically.
- **"The stabilization module is just standard max-shift"** — While max-shift is a standard numerical technique, the paper's contribution is showing it is *necessary* for stable training with Softmax₁ in this setting (Table 4 shows alternatives fail). This is a valid engineering finding.
- **"Methodology motivational example rehashes known findings"** — Setting up the problem with known context is standard practice; not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews raise a genuine tension: the paper has convincing PTQ results and clear outlier reduction evidence, but the LoRA experiments are undermined by a baseline that likely underperforms standard practice. This distinction between the two experimental settings (PTQ vs. LoRA) is the most important takeaway for evaluating the paper.

## Suggestions

1. **Tune the vanilla LoRA baseline properly and report the process.** Run a learning rate sweep, show convergence, and ensure the vanilla model achieves a reasonable ASR/TTS WER under LoRA (below 15-20%) before claiming improvement. If the vanilla model is indeed unstable for SpeechLM under standard LoRA — which would itself be a novel finding — document that clearly and make it part of the contribution.

2. **Add validation on at least one other architecture** (e.g., LLaMA-7B or a smaller LLaMA variant) to demonstrate the method is not OPT-specific.

3. **Separate the Softmax₁ effect from the stabilization effect** with an ablation that compares (a) softmax + max-shift, (b) Softmax₁ alone (no max-shift), and (c) Softmax₁ + max-shift, to attribute the gains precisely.

4. **Provide full training hyperparameters** (learning rate, optimizer, batch size, epochs, scheduler) in a table for reproducibility.
