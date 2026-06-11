Now I will write the final consolidated review.

## Summary

This paper introduces a weight-based method for classifying gated neurons in transformers by computing cosine similarities between their input, gate, and output weight vectors — producing a taxonomy of six read-write (RW) functionalities. Applying this method to 12 LLMs, the paper discovers a universal pattern: early-middle layers are dominated by "conditional strengthening" neurons while late layers shift toward "weakening" neurons. Through ablation experiments on OLMo-7B, the paper finds that the small class of weakening neurons has outsized influence on model behavior (attribute rate, entropy), and introduces "conditional ablation" to trace part of this effect to activations where the gate value is negative — a finding that challenges the assumption that negative Swish gate values are functionally irrelevant.

## Strengths

1. **Cross-model universality convincingly demonstrated across 12 LLMs.** The strengthening-then-weakening pattern across layers is shown for Gemma-2-2B/9B, Llama-2/3.1/3.2 variants, OLMo-1B/7B, Mistral-7B, Qwen2.5 variants, and Yi-6B. Figure 1(a) plots nine larger models and all show the same qualitative trend from positive median cos(w_in, w_out) in early layers to negative in late layers. This consistency from a simple weight-only measure is genuinely striking.

2. **Controlled ablation cleanly isolates weakening neurons' specific impact.** Section 6 zero-ablates all 243 weakening neurons and compares against 243 random neurons from the same layers. The weakening ablation produces a visible effect on attribute rate from layer ~10 onward, while the layer-matched random baseline is indistinguishable from clean (Figure 3a). Other RW classes likewise show no effect. This design cleanly separates the effect of RW class from layer position — a strong experimental control.

3. **Conditional ablation method and the negative gate value finding.** Section 6.2 partitions each neuron's activations by signs of (x_gate, x_in) into four cases. Case (iii) — x_gate < 0, x_in < 0 — reproduces most of the entropy-sharpening effect of full ablations. This is a genuinely novel methodological contribution and provides the first mechanistic evidence (concurrent with Kong et al., 2025) that negative Swish gate values have functional relevance, contradicting the common view that they only matter for training dynamics (line 227: "This shows that, for mechanistic interpretability research, Swish is not reducible to ReLU").

4. **Strong quantitative link between weight-based classification and activation behavior.** Figure 4 shows a -0.97 correlation (p < 0.01) between cos(w_in, w_out) and activation frequency for Layer 15 of OLMo-7B, with correlations at least -0.71 across most layers. This empirically connects the purely weight-based taxonomy to actual neuron behavior during inference.

5. **Weight preprocessing step for gated activations.** Section 3.2's sign-correction of w_in and w_out by sign(cos(w_gate, w_in)) resolves a sign ambiguity specific to gated neurons. This is a reusable methodological contribution for future work on gated architectures.

## Weaknesses

### Major

- **Functional importance claims validated on only one model.** The paper's headline claims — that weakening neurons have "outsize influence" on model behavior and that negative gate values play a functional role — rest entirely on ablation experiments with OLMo-7B. The weight-based taxonomy (Section 5) is impressively broad (12 models), but the functional validation (Sections 6-8) uses a single model. The paper justifies this by resource constraints (line 188), but the conclusion (line 281) presents these as general findings about weakening neurons without adequately caveating the single-model evidence. Since the weight analysis itself shows variation across models (Figure 1a), we cannot confidently assume the functional importance generalizes. The single case study (Section 6.3) and single qualitative neuron analysis (Section 8) further limit the generality of the functional claims.

### Minor

- **"First to observe" claim slightly outruns the evidence.** The conclusion states "we are the first to observe such a mechanism" (line 281) without the concurrent-work qualifier that appears in Section 6.2 (line 227: "for the first time (concurrently with Kong et al. (2025)"). The finding is genuinely interesting but demonstrated for weakening neurons of one model on one metric (entropy). The unqualified claim in the conclusion overstates the evidence.

- **Unclear whether "243 weakening neurons" includes conditional weakening.** Table 1 defines "weakening" and "conditional weakening" as distinct RW classes (separated by cos(w_gate, w_out) above/below 0.5), but the paper does not explicitly state whether the ablation count of 243 covers both classes or just the "weakening" class. This should be clarified for precision.

- **Minor counting inconsistency.** The abstract and introduction consistently state "nine different LLMs" while Section 5 lists 12. The discrepancy arises because Figure 1(a) shows the 9 larger models (3 smaller ones analyzed separately), but the framing is imprecise and could confuse readers.

### Trivial

None beyond the minor points above.

## Nice-to-Haves

- Extending ablation experiments to at least one additional model (e.g., Llama-3.2-3B) would substantially strengthen the generality of the functional claims. This is the single highest-leverage improvement.
- Reporting confidence intervals or variance for the ablation results in Figure 3(a) would help quantify uncertainty around the observed effects.
- Per-layer correlation plots for activation frequency (beyond the single striking layer in Figure 4) would be a useful supplement to the reported correlation range in the text.
- A brief check showing that weight norms do not systematically differ between RW classes would address a natural reader concern about confounds.

## Removed Points

These were removed from the reviewer inputs with justification:

- **Preprocessing justification in appendix (Harsh Critic):** The critic notes that the preprocessing step's justification is deferred to the appendix. Per the rules, appendix content was stripped by the PDF parser; the original submission contains this justification. Not a weakness.
- **Weight norm confound (Harsh Critic):** The critic speculates that weakening neurons might have larger weight norms confounding ablation results. This is an area-of-concern sweep without evidence that the confound actually exists. The paper already controls for layer position by sampling random neurons from the same layers.
- **Activation frequency conflating correlation with causation (Harsh Critic):** The paper explicitly acknowledges that "activation frequencies do not fully explain their effect" (line 247). This concern is already addressed by the authors.
- **Figure 4 only shows one layer (Harsh Critic):** The paper reports the correlation range across all layers in the text (-0.71 or stronger in most layers). Showing one representative layer in the main figure is standard presentation practice.
- **Case study is a single example (Harsh Critic):** Presented as a case study; its inherent scope limitation is acknowledged by the format.
- **Various generic/false strengths from Strength Finder:** None applicable — all enumerated strengths were concrete and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The contrast between the paper's broad cross-model weight analysis (12 models) and narrow single-model functional validation is the central tension that future work could address.

## Suggestions

1. Extend ablation experiments to at least one additional model (e.g., Llama-3.2-3B or a Gemma variant) to test whether the functional importance of weakening neurons generalizes beyond OLMo-7B.
2. Clarify the "243 weakening neurons" count — specify whether this includes or excludes "conditional weakening" neurons.
3. Add a sentence in the conclusion caveating that the functional validation rests on one model (while the weight-based taxonomy covers 12).
4. Keep the concurrent-work qualifier consistent throughout when making "first to observe" claims.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| EytBpUGB1Z (Retrieval Head) | 8.00 | R1 | Stronger — causal validation on multiple model families; cleaner detection method |
| SUc1UOWndp (Attn Head Specialization) | 7.00 | R2 | Stronger — more rigorous theoretical grounding; limited to 2-layer model |
| GPDcvoFGOL (Second-Order Neurons CLIP) | 6.75 | R2 | Comparable — similar quality of findings, limited to CLIP; our paper has broader model coverage |
| GdbQyFOUlJ (NeurFlow) | 6.50 | R2 | Comparable — similar methodology quality; our paper has cleaner experimental controls |
| 41HlN8XYM5 (Automated Circuit Discovery) | 6.33 | R2 | Comparable — similar contribution level |
| WQQyJbr5Lh (Influential Neuron Path ViT) | 6.00 | R1 | Comparable — similar scope of findings and limitations |
| Hf17y6u9BC (Best Practices Activation Patching) | 6.67 | R2 | Comparable — well-executed methods paper |
| Ebt7JgMHv1 (Interpretability Illusion) | 6.33 | R2 | Comparable — well-executed but different focus |
| rIx1YXVWZb (Understanding Addition) | 5.50 | R2 | Weaker — limited to toy one-layer transformer |
| v675Iyu0ta (Interpretability Illusions) | 5.60 | R2 | Weaker — narrower scope and contribution |
| nUGFpDCu3W (GPT MLP Weights) | 4.00 | R1 | Weaker — single model, single task, less surprising findings |
| 89wVrywsIy (Sparse Circuits) | 3.40 | R1 | Weaker — no baseline comparisons, limited experimental scope |
| fM1ETm3ssl (Meta-Models Auto Interpretability) | 3.00 | R1 | Weaker — proof-of-concept without strong empirical validation |

**Round 1 bracket:** 5.0 to 6.5.

**Round 2 narrowing:** The lower anchor (5.50, Understanding Addition) is clearly weaker than this paper (toy model, single task). The upper anchors (6.75 Second-Order Neurons, 7.00 Attn Head Specialization) have either more rigorous methodology or broader validation. Our paper sits between these — it has genuinely novel findings (weakening neurons, conditional ablation, negative gate values) and impressively broad weight-analysis across 12 LLMs, but the single-model functional validation prevents it from reaching the 6.5-7.0 range. The paper is best compared to NeurFlow (6.50) and the ViT Neuron Path paper (6.00) — it is comparable in overall contribution quality.

**Final score: 6.0.** The paper makes a solid empirical contribution with novel findings, clean experimental design where it matters (layer-matched ablation controls), and impressive cross-model breadth. The main limitation — single-model functional validation — is real but not fatal, and appropriately scoped claims plus a straightforward extension would substantially strengthen the paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>