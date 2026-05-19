- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5
I have all the information I need. Now let me compose the final consolidated review.

---

## Summary

This paper introduces NeuralFuse, an input transformation module that learns to generate error-resistant data representations to mitigate accuracy loss from low-voltage-induced SRAM bit errors in DNN inference. The key idea is model-agnostic: rather than retraining the deployed model, NeuralFuse plugs in as a preprocessing DNN. Two access scenarios are considered: relaxed (gradients available via backprop) and restricted (transfer from a surrogate model). Experiments on multiple architectures (ResNet, VGG) and datasets (CIFAR, GTSRB, ImageNet-10) report up to 57% accuracy recovery and up to 24% SRAM memory access energy savings at a 1% bit error rate.

## Strengths

1. **First model-agnostic approach to low-voltage bit-error mitigation.** The paper's central claim—that NeuralFuse operates without retraining the deployed model—is well-supported by the design. Unlike prior work (ErrorAwareTraining, Matic, Eden) that requires model-specific retraining, NeuralFuse is an add-on module on the input side (Section 1, Figure 1, Eq. 1). This is a genuinely novel framing of the problem.

2. **Quantified accuracy recovery and energy savings from realistic SRAM simulations.** The up-to-57% recovery and up-to-24% energy savings at 1% BER are supported by experiments across 5 base models and 4 datasets (Section 4.2, Figure 3), with energy calculations based on SCALE-SIM simulations and Cadence Spectre SRAM characterization (Section 4.1, Eq. 6). The multi-model/generator sweep provides credible evidence that the effect is not an artifact of one specific architecture.

3. **Demonstrated transferability under restricted (black-box) access.** Table 1 (Section 4.3) shows that generators trained on a white-box surrogate (e.g., VGG19) transfer to other architectures (ResNet18, VGG11) with accuracy that sometimes exceeds the relaxed-access case. This validates the practical claim for the more realistic restricted-access setting and is a clear differentiator from prior work that requires model-specific retraining.

4. **Emergent robustness to low-precision quantization.** Section 4.5 shows that NeuralFuse, trained only on random bit errors, also recovers accuracy lost from uniform quantization down to 4-bit weights. This provides evidence that the learned input transformations capture general error-resistant representations, not just overfitting to the specific error model used in training.

5. **EOPM optimizer provides a principled training procedure.** The Expectation Over Perturbed Models (EOPM) algorithm (Section 3.2, Eqs. 4–5) adapts the EOT attack framework to handle the combinatorial explosion of possible bit-error patterns, with a practical approximation using N=10 perturbed models per iteration.

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison against prior error-mitigation methods.** The paper claims "state-of-the-art performance" (line 33) and discusses methods like ErrorAwareTraining, Matic, and Eden in related work (Section 2), but provides zero experimental comparison against them. Without this, the relative contribution of NeuralFuse is unestablished. A reader cannot determine whether the 57% recovery is better, worse, or comparable to what error-aware training achieves under the same BER and model settings. This is the single most significant gap in the evaluation.

2. **"Recover percentage" metric is ambiguous and baseline perturbed accuracy is not explicitly reported in the text.** The paper reports that NeuralFuse "increase[s] the perturbed accuracy... by up to 57%" (line 31) and that generators "recover the perturbed accuracy in the range of 41% to 63%" (line 133), but never defines what "recover percentage" means. It is unclear whether this is an absolute accuracy improvement (e.g., 10% → 67%), a percentage of lost accuracy recovered, or a relative improvement over the baseline. The baseline perturbed accuracy (model accuracy under bit errors without NeuralFuse) is not stated numerically in the text; the "Extended Analysis" subsection (line 170–171) merely says "the baseline is much worse than NeuralFuse" without providing concrete numbers. While the figures may show baselines, the text should be self-contained enough for a reader to interpret the key quantitative claim.

### Minor

3. **Energy savings calculation may overstate system-level benefit.** The energy formula (Eq. 6) accounts for SRAM memory access energy of both the base model and NeuralFuse, but does not include the computation energy of NeuralFuse's own forward pass (MAC operations). The paper acknowledges this as a "tradeoff" (Section 4.4, paragraph on latency) but does not quantify its impact on the claimed 24% savings figure. If NeuralFuse' compute energy is non-trivial relative to the SRAM savings, the net benefit could be lower than reported.

4. **Training hyperparameters not reported.** The paper states 150 training epochs and GPU hours (Section 4.1) but omits learning rate, batch size, optimizer choice, weight decay, and learning rate schedule. This limits reproducibility.

5. **"Extended Analysis" subsection (Section 4.5) is near-empty.** It contains only three lines stating "the baseline is much worse than NeuralFuse" without adding quantitative or qualitative substance. This section should either be fleshed out meaningfully or removed.

### Trivial

6. The claim that error-aware training was "found ineffective for large DNNs with millions of bits" (line 44) is asserted via a citation without any quantification or supporting evidence from this paper's own experiments. The paper would benefit from being more precise about the conditions under which this is known to hold.

## Nice-to-Haves

- An ablation study showing sensitivity of NeuralFuse performance to the number of perturbed models N during training (the paper states N=10 is sufficient but shows no data backing this claim).
- A discussion of whether the relaxed-access setting (backprop through API) exists in practice, and what approaches could handle fully black-box models beyond the surrogate transfer already considered.
- Testing against a correlated bit-error model (e.g., row/column clustering) to assess whether the independence assumption affects generalization.

## Removed Points

These points were raised by reviewers but are excluded from the main review for the reasons noted. They should be treated with caution if consulted.

- **"Unacknowledged assumption about bit error distribution"** — Removed because the paper *does* explicitly acknowledge the assumption: "It has been observed that bit cell failures for a given memory array are randomly distributed and independent of each other" (line 50–51), with citation. The criticism is factually incorrect about the paper.
- **"Gradient calculation requires backprop through base model in relaxed access setting"** — Removed because the paper *defines* relaxed access precisely as a scenario where backpropagation through the model is possible (line 21). The restricted-access setting separately handles the no-backprop case. The criticism misreads the paper's scoping rather than identifying a flaw.
- **"Missing related works"** — Removed per policy: this cannot be verified without external sources. The paper's related work section is present and discusses relevant literature (Section 2).
- **Style/formatting nitpicks** — Removed per policy (parser artifacts, not author errors).
- **Generic reproducibility concerns (e.g., "cannot be independently verified")** — Removed per policy (speculative, not grounded in a concrete missing element).

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface an observation about NeuralFuse that the authors themselves do not already articulate. Two points worth noting, however: (1) the finding that transfer from a surrogate sometimes *outperforms* direct training (Section 4.3) is an interesting phenomenon that the paper correctly flags but could explore more deeply; (2) the emergent robustness to quantization (Section 4.5) hints that input transformations learned for one error source may generalize to others, which could be a broader principle worth investigating.

## Suggestions

1. **Add an experimental comparison against at least one prior error-aware training method** (e.g., ErrorAwareTraining or Matic) under identical BER and model settings. Even if the comparison is not perfectly apples-to-apples (since NeuralFuse is a fundamentally different approach), it establishes where the method sits in the landscape and substantiates the "state-of-the-art" claim.
2. **Explicitly define "recover percentage"** and report baseline perturbed accuracy values (without NeuralFuse) in the text itself, not only in figures.
3. **Report all training hyperparameters** needed to reproduce results (learning rate, batch size, optimizer, weight decay, schedule).
4. **Quantify the compute energy of NeuralFuse's forward pass** and include it in the energy savings analysis, or explicitly bound the worst-case impact on the reported 24% savings figure.
5. **Fill or remove the "Extended Analysis" subsection** — either add meaningful quantitative analysis (e.g., per-class breakdown, sensitivity to model capacity) or delete it.

---
