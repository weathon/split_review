Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces **codebook features**: a method that inserts trainable vector-quantization bottlenecks into each layer of a neural network during finetuning, forcing hidden states into sparse, discrete combinations of codebook vectors. The authors show that Transformers can operate under this bottleneck with limited performance degradation, that the resulting codes correspond to interpretable features (especially in a synthetic FSM setting where 100 hidden states map to distinct codes despite only 128 neurons per layer), and that activating identified topic codes during generation steers outputs toward desired topics (e.g., "dragon" topic frequency rising from 2.5% to 65.0%). The TokFSM experiments span the TokFSM algorithmic dataset and language models up to 410M parameters on TinyStories and WikiText-103.

---

## Strengths

1. **Novel and well-motivated method.** The idea of imposing a structural sparse-discrete bottleneck via vector quantization during finetuning, rather than training a post-hoc sparse autoencoder on frozen activations, is a clean conceptual contribution. The paper clearly motivates why sparsity and discreteness are desirable properties for interpretability (lines 24-27) and the method section (Section 2) is clearly written.

2. **Strong causal evidence in a controlled synthetic setting.** The TokFSM experiment (Section 3) is the paper's cleanest result. With 128 neurons per layer, codes achieve 97.1% average precision for state classification vs. 70.5% for the best neuron at matching recall (Figure 3 left, lines 129). The interchange intervention — replacing MLP state codes with those of another state — shifts the next-token distribution almost entirely to the target state (Figure 2). This constitutes genuine causal evidence, not just correlation.

3. **Scaling demonstrates feasibility.** The paper trains codebook models up to 410M parameters (24 layers) with attention-only codebooks (k=8), achieving loss of 2.74 vs. a finetuned baseline of 2.41 (Table 2). This shows the approach does not break at scale, a non-trivial finding for a structural bottleneck.

4. **Steering methodology is intuitive and practical.** The two-phase procedure (hypothesis generation by inspecting activating tokens → steering by substituting codes) is clearly described and works measurably: e.g., "Fire" topic frequency from 2.5% to 100% on TinyStories (Table 5), and "Football" from 7.5% to 95% on WikiText-103. This contrasts with activation addition methods that require tuning steering magnitudes per layer.

---

## Weaknesses

### Fatal

None. The paper has real contributions and does not contain a fundamentally flawed methodology-level error that invalidates its core claims.

### Major

1. **No comparison to sparse autoencoders (SAEs), the dominant baseline for the same goals.** The paper claims to "minimize the superposition problem" (line 129) and provide interpretable sparse features, but never benchmarks against SAEs (Bricken et al. 2023, Cunningham et al. 2023, etc.), even though these are cited in related work (line 315). The paper distinguishes itself on the structural-vs-post-hoc axis, but this distinction does not excuse the absence of a direct comparison. Without showing that codebook features discover more monosemantic features, support better steering, or achieve higher reconstruction fidelity at comparable sparsity, the paper's novelty relative to a well-known alternative is unestablished. This is the single most important missing experiment.

2. **Interpretability evaluation is narrow and potentially biased.** The paper evaluates code interpretability by manually selecting codes with "simple, interpretable activation patterns" (line 241), defining regular expressions after seeing the activations (creating a confirmation loop), and measuring precision only on that cherry-picked set. This says nothing about the thousands of other codes that may be noisy or uninterpretable. The neuron baseline — picking the best neuron at the code's recall — is also a generous-to-neurons comparison, yet the evaluation only covers a handful of hand-selected features (years beginning with "2", months, state codes). A systematic interpretability evaluation over all codes (e.g., automated interpretability scoring as in Bills et al. 2023, or a broad-coverage benchmark) is needed to support the claim that codes are generally more interpretable.

3. **Steering experiments lack baseline comparisons and coarse evaluation.** The paper does not compare to simpler steering methods like activation addition (Turner et al. 2023, Merullo et al. 2023) or latent steering vectors. Since the paper claims codebooks "make it easier to localize behaviors and perform interventions" (line 319-320), showing that the same intervention could not be done at least as well with cheaper methods is essential. Additionally, the evaluation uses keyword-based classifiers (e.g., "dragon" → dragon topic) that cannot distinguish fluent topic incorporation from generation collapse. No perplexity, diversity, or coherence metrics are reported for steered generations.

### Minor

1. **Performance degradation in language models is non-trivial.** The 410M attention k=8 model has a loss of 2.74 vs. 2.41 (13.7% increase). The MLP k=100 model loss is 3.03 (25.7% increase). The paper characterizes this as "strong" performance (line 216), which overstates the case. For the MLP codebooks specifically, degradation is substantial, and the paper focuses analysis primarily on the better-performing attention codebooks without adequately discussing this limitation.

2. **Claim about "modest degradation" for TokFSM is imprecise.** The attention+MLP k=1 model attains 63.65% state accuracy vs. 96.77% original (Table 1) — a 34% absolute drop. While the attention-only k=1 model is near-perfect (96.39%), the paper's broad statement that "networks can operate under this extreme bottleneck with only modest degradation" (line 100) applies cleanly only to the attention-only variant.

3. **No quantitative characterization of codebook utilization or monosemanticity at scale.** The paper does not report what fraction of codes are ever activated, whether "dead" codes exist (a known VQ-VAE issue), or what proportion of codes are monosemantic vs. polysemantic. These are standard analyses for this type of work.

4. **No analysis of failure cases for steering.** All steering examples shown are successes (Tables 3-4). The paper does not discuss when or why steering fails or produces incoherent outputs.

---

### Trivial

None.

---

## Nice-to-Haves

- An automated, large-scale interpretability evaluation (e.g., automated feature description scoring over all codes).
- Steering evaluation with perplexity, diversity, and coherence metrics.
- Codebook utilization statistics and analysis of dead codes.
- A study of whether codebook features from early layers are more or less interpretable than those from later layers.

---

## Removed Points

The following points raised by the harsh critic are flagged for removal and should be treated with caution:

- **"No real baseline comparison" framing as fatal.** The reviewer calls the lack of SAE comparison fatal to the paper's contribution. This is an overstatement — the paper's TokFSM results and the structural method are self-contained contributions. I re-classified this as a Major weakness (not fatal) because the paper's core claims do not collapse without an SAE baseline; the experiments still demonstrate that codebooks assign states to distinct codes and enable causal intervention, independent of any SAE comparison.
  
- **Criticism about the MLP-attention model's state accuracy drop (33%).** The reviewer claims this contradicts the "modest degradation" claim, but the paper's analysis focuses on the attention-only k=1 model (96.39% accuracy, genuinely modest degradation) and discusses the attention+MLP model separately. I re-classified this as a Minor weakness to note the imprecision, not a major contradiction.

- **"The paper does not discuss whether codebook inherits features from pretraining or learns them anew."** This is a fair curiosity but not a weakness — the paper's method is finetuning-based; the codebooks are randomly initialized and learned during finetuning. This is clear from the method description.

- **Criticism about the steering intervention being "extreme" and "possibly model-breaking."** The paper already acknowledges this by including both a "single code" condition and an "all codes" condition (lines 285-287), transparently showing both. The results report both conditions.

- **Criticism about regularization being defined "after seeing activations."** The paper is transparent about this methodology (lines 241-242) — it is a standard interpretability practice to generate hypotheses from data and then test them. The criticism implies a fatal methodological flaw when in fact the procedure is clearly described and acknowledged as "preliminary" (line 241).

---

## Novel Insights

The reviews surface a substantive tension that the paper does not fully resolve: codebook features are *structural* (imposed during finetuning, baked into the model's computation) while SAEs are *post-hoc* (trained on frozen activations). The paper argues this structural nature is advantageous (it makes codes "an appealing unit of analysis"), but it also means the codebook fundamentally alters the model, unlike SAEs which leave the original model untouched. This tradeoff — interpretability by design vs. interpretability by decomposition — is never squarely addressed. The paper would benefit from clarifying when one would prefer a structurally interpretable model over a post-hoc decomposable one, and vice versa.

---

## Suggestions

1. **Add an SAE comparison on at least the TokFSM dataset** (where ground-truth features are known) and one language model setting. Train SAEs on the baseline model's activations at comparable sparsity levels (same number of active features per token) and compare: feature precision on known probes, steering effectiveness, and monosemanticity.

2. **Add a steering baseline comparison** using activation addition (Turner et al. 2023) on the same topics. Report not just keyword frequency but also perplexity and diversity of steered outputs.

3. **Broaden the interpretability evaluation.** Instead of hand-picking codes, either (a) compute automated interpretability scores (e.g., transcription-based scoring) over all codes, or (b) sample codes randomly and have independent annotators label them, reporting the fraction of interpretable codes.

4. **Report code utilization rates** (fraction of codes that activate at least once in the training set) and monosemanticity histograms over all codes.

5. **Qualify performance claims more precisely.** Distinguish "modest" (attention-only TokFSM, TinyStories) from "notable" degradation (410M attention k=8, MLP codebooks) rather than using a single descriptor.

---

## Score and Decision

**Calibration anchors consulted (all returned by batch search):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I4e82CIDxv.md` (Sparse Feature Circuits) | 8.00 | Much stronger evaluation: comprehensive circuits, faithfulness metrics, causal interventions at scale. Codebook paper has weaker LM evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PBjCTeDL6o.md` (Unlearning-based Interpretations) | 8.00 | Much more rigorous: comprehensive experiments, theoretical analysis, multiple datasets. Codebook paper is less thorough. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9ca9eHNrdH.md` (SAEs Not Canonical) | 7.00 | Stronger: well-designed experiments with principled metrics, clear research question. Codebook paper has cleaner synthetic results but weaker evaluation at scale. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fmWVPbRGC4.md` (Local vs Distributed) | 5.67 | Both have limited scope. Local/Distributed has rigorous psychophysics; codebook paper has cleaner causal evidence but cherry-picked interpretability evaluation. Roughly comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F76bwRSLeK.md` (SAEs Find Features) | 4.80 | Both introduce a method for interpretable features with limited evaluation. SAE paper has automated interpretability scoring; codebook paper has stronger causal evidence (TokFSM). Comparable overall. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9L9j5bQPIY.md` (Metanetwork) | 2.50 | Much weaker: unclear methodology, no meaningful experiments. Codebook paper is substantially better. |

The paper introduces a genuinely novel structural approach to interpretability with clean causal evidence in a synthetic setting, but the evaluation in the primary domain of interest (language models) has significant gaps: no comparison to the dominant baseline (SAEs), a narrow and potentially biased interpretability assessment, and no steering baseline comparisons. These weaknesses are fixable but material.

**Score: 5.0** — The paper has solid contributions (novel method, convincing TokFSM experiments) but is incomplete in its current form for the natural language claims. The missing experiments (particularly SAE comparison and broader interpretability evaluation) would substantially strengthen the paper.

**Decision: Reject** — not because the idea is unsound, but because the evaluation as presented does not adequately support the paper's central claims about interpretability improvement and superposition mitigation in language models. The paper would benefit from a major revision adding the missing comparisons and a more rigorous evaluation, after which it could become acceptable.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>