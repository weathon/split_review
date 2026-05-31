## Summary
This paper introduces a weight-based read-write (RW) analysis framework for gated MLP neurons in transformer LLMs, classifying neurons by the cosine similarities among their gate, input, and output weight vectors (w_gate, w_in, w_out). The core discovery is a small but highly influential class of *weakening* neurons that activate very frequently, concentrate in late layers, and have outsized effects on attribute rate and output entropy—while early-middle layers are dominated by *conditional strengthening* neurons. A further surprising finding is that negative gate values (x_gate < 0) in weakening neurons contribute meaningfully to model behavior, contradicting the common assumption that the gated activation function behaves essentially like ReLU.

---

## Strengths

- **Universal cross-model patterns:** The structural finding—early-middle layers dominated by conditional strengthening, late layers trending toward weakening—is validated on 12 different LLMs (Llama, Gemma, OLMo, Mistral, Qwen, Yi), across 0.5B–9B parameters. This breadth is unusual for a mechanistic interpretability paper and strongly supports the generality of the finding.

- **Negative gate values as a new mechanistic phenomenon:** Section 6.2 uses conditional ablations (stratified by sign of x_gate) to show that the surprising entropy-sharpening behavior of weakening neurons is largely driven by the x_gate < 0 regime. This is a concrete, falsifiable, and genuinely novel mechanistic claim. Figure 3(b) makes it legible: ablating only gate-negative activations (case iii) recapitulates the entropy effect of the full ablation, whereas the three other sign combinations do not. This challenges the prevailing assumption that Swish ≈ ReLU for interpretability purposes.

- **Simple, scalable method with striking results:** The cosine-similarity taxonomy requires no forward passes and is applicable to any model with gated activations. Despite its simplicity, it predicts activation frequency (r = −0.97 in layer 15 of OLMo-7B; Figure 4) and produces a clean, consistent picture across layers and models. This is an appealing property for a mechanistic tool.

- **Conditional ablation as a reusable contribution:** The method of partitioning a neuron's activations by the sign of x_gate and x_in and ablating each partition separately is a transferable diagnostic, applicable to any analysis of gated neurons beyond this paper's scope.

- **Empirical effect sizes are striking:** Ablating only 243 weakening neurons (out of tens of thousands) substantially alters attribute rate from layer ~10 onward (Figure 3a), while ablating the same number of random neurons from the same layers has no discernible effect. The disproportion between neuron count and functional influence is well-illustrated.

---

## Weaknesses

### Fatal
None.

### Major

1. **Functional impact is demonstrated on a single model.** The ablation experiments establishing that weakening neurons are functionally influential are run only on OLMo-7B. The authors justify this by citing compute constraints and the public availability of OLMo's training set, but this creates an asymmetry: structural patterns are shown to be universal across 12 models, while the causal claim—that weakening neurons have *outsized influence*—is demonstrated for only one. It is unclear whether the disproportionate impact is equally universal or specific to OLMo-7B. Even ablations on a second smaller model (e.g., Llama-3.2-3B) would substantially strengthen the functional claims.

2. **The mechanistic explanation of *why* weakening neurons have outsized influence remains incomplete.** The paper shows *that* ablating them affects metrics but does not provide a satisfying account of the underlying circuit. Section 8's case study of neuron 31.9634 is described by the authors themselves as "much harder to interpret," and the text acknowledges that the Omicron example cannot be attributed to any single neuron's w_out. The claim in the title ("outsize influence") is empirically supported but mechanistically ungrounded, which limits the interpretability contribution.

3. **The τ = 0.5 threshold choice is under-justified.** The paper presents random baselines (Section 4.3) for significance testing but does not show how sensitive the category counts or layer distributions are to the choice of threshold. Since the main structural finding (conditional strengthening in early-middle layers, weakening in late layers) is illustrated with threshold-based bar charts (Figure 1b), the robustness of this finding to threshold variation should be checked. The continuous scatter plots (Figure 2) partially address this, but no sensitivity analysis is reported.

### Minor

1. The weight preprocessing step (multiplying w_in and w_out by the sign of cos(w_gate, w_in), Section 3.2) directly affects which neurons are classified as weakening versus strengthening. Deferring this entirely to Appendix C makes the taxonomy hard to interpret without reading the appendix; at least an intuitive justification should appear in the main text.

2. Activation frequency is presented as a correlate of RW class but the direction of causality is unclear. It may be that weakening neurons activate often *because* they encode broadly applicable suppression (e.g., suppressing high-entropy directions), not because of any intrinsic property of the weakening class. The paper notes the correlation but does not attempt to distinguish these accounts.

3. The single case study per class (one strengthening, one weakening neuron) is thin as qualitative evidence. Given the claim that weakening neurons are "much harder to interpret," several case studies would be needed to establish whether that complexity is a property of the class or the specific neuron chosen.

### Trivial
- The code URL in footnote 1 is empty (parser issue or placeholder).

---

## Nice-to-Haves

- Ablation experiments on at least one additional model to test whether weakening neurons' functional dominance is as universal as their structural prevalence.
- A brief sensitivity analysis of the τ = 0.5 threshold, even just showing that the layer distribution pattern (Figure 1b) is qualitatively stable under τ ∈ {0.3, 0.5, 0.7}.
- More case studies of weakening neurons with interpretable examples (e.g., from the conditional ablation framework) to begin building a systematic picture of what these neurons do.
- A discussion of whether the strengthening-to-weakening transition across layers might reflect a known functional decomposition such as early feature construction → late output refinement.

---

## Novel Insights

The most genuinely novel insight is that negative gate values in gated activation functions are not mechanistically inert—they contribute to model behavior through a sign-flip mechanism: when x_gate < 0, a weakening neuron (which normally subtracts a direction from the residual stream) instead adds it, effectively acting as a strengthening neuron. This is not predicted by treating Swish as a smooth ReLU substitute and has concrete consequences for interpretability methodology: analyses that ignore the x_gate < 0 regime (or that discretize to "active" vs "inactive" based on a threshold of zero) will miss a functionally important portion of weakening neuron behavior. The conditional ablation framework introduced here is the right tool for exposing such sign-dependent effects and is likely to have value beyond this specific class of neurons.

---

## Suggestions

- Run at least one ablation experiment (attribute rate or entropy) on a second model (e.g., Llama-3.2-3B) to test cross-model generalization of the functional dominance claim.
- Show a threshold sensitivity figure (fraction of neurons per class vs. τ for a representative layer) to validate robustness of the structural taxonomy.
- In Section 6.3, quantify how often the x_gate < 0 effect (case iii) is the dominant contributor to entropy reduction across the full evaluation set, not just the single most extreme example—this would strengthen the statistical case.
- Clarify the preprocessing sign convention (Section 3.2) with an inline example in the main text, as it is essential for interpreting the sign of cos(w_in, w_out).

---

## Score and Decision

The paper makes a clear, well-executed contribution to mechanistic interpretability with a novel taxonomy, strong cross-model structural evidence, and a genuinely surprising finding about negative gate values. The main gaps—functional analysis on only one model, incomplete mechanistic explanation—are significant but do not invalidate the claims made; they limit the depth of the contribution. The work is a solid step forward for the subfield and the conditional ablation methodology is independently useful.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>