Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes replacing WFST-based contextual biasing in ASR with an algorithm based on the Knuth-Morris-Pratt (KMP) string matching algorithm. The key idea is to track partial matches of biasing phrases during beam search by maintaining a matching state per phrase, computing a per-token biasing bonus from the difference in matching potentials. The method is designed to be TPU-friendly through vectorization of the matching operations. Experiments on a large 870M-parameter RNN-T model (voice search domain) show substantial WER reductions over no biasing (50–70% relative on With-Prefix sets) and additional gains when combined with Neural Associative Memory (NAM) model-based biasing.

## Strengths

1. **Novel and principled adaptation of KMP to ASR biasing.** The paper gives a clean, self-contained algorithmic exposition (Algorithms 1–3) showing how the KMP failure function and forward function can maintain per-phrase matching state during beam search. The equivalence to a deterministic epsilon-free FSA is noted (Section 2.1, citing CLRS), providing a principled foundation. This is a genuinely new connection between string matching and ASR inference-time biasing.

2. **Large and consistent WER reductions.** Table 1 shows KMP biasing alone reduces WER on the With-Prefix set from 9.6% to 2.4% at B=150 (75% relative) and from 20.9% to 4.8% on Without-Prefix (77% relative) — without introducing any model parameters. These gains are substantial and hold across multiple dataset configurations (B=150, 600, 3000) and both shallow fusion and OTF rescoring modes.

3. **Complementarity with model-based biasing (NAM) is convincingly demonstrated.** Table 2 shows that adding KMP biasing to NAM yields 20–40% additional relative WER reduction on biasing sets (e.g., With-Prefix B=3000: NAM 2.8% → NAM+KMP 2.1%) and 21% relative on Contact-Tag (3.8% → 3.0% with prefix boosting). This supports the claim that inference-time and model-based biasing are additive.

4. **Efficient prefix-boosting mechanism.** The extension in Section 2.4 handles carrier phrases (e.g., "call", "open", "play") with only O(C+B) additional state cost, avoiding the O(B·C) combinatorial explosion of naive prefix-phrase concatenation. Table 2 shows further consistent gains (e.g., With-Prefix B=3000: 2.1% → 1.7%).

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against a WFST-based biasing baseline.** The paper is motivated throughout by the claim that KMP biasing "simulates the classical approaches often implemented in the weighted finite state transducer framework" (Abstract) and that FST-based biasing is "not efficient to use on TPUs" (Section 3). Yet the experiments include no WFST baseline — neither for WER accuracy nor for efficiency. The only baselines are "without-biasing" and NAM. Since WFST shallow fusion (Zhao et al., 2019) is the standard inference-time biasing method for E2E ASR and is cited extensively, the reader cannot assess whether KMP biasing achieves comparable, better, or worse biasing accuracy. A comparison on the same test sets, at minimum reporting WER, is needed to validate that the method is a viable replacement rather than just a working biasing method.

2. **No empirical efficiency measurements despite central TPU-efficiency claims.** The paper repeatedly asserts TPU-friendliness, vectorization, and careful memory considerations (Abstract, Section 1, Section 3). However, zero runtime measurements are provided — no wall-clock time per utterance, no real-time factor (RTF), no memory footprint, no latency comparisons. The only "evidence" is asymptotic complexity analysis (O(γ̄KFB)). Since TPU-friendliness is a primary selling point and distinguishes this work from existing WFST approaches, the complete absence of any efficiency experiment is a structural gap. The reader cannot evaluate whether the method solves the efficiency problem it claims to address.

3. **Generality claims are unsupported.** The paper states the method "can be incorporated into the beam search of any ASR system" (Section 1), but all experiments use a single RNN-T architecture (870M parameters) with one specific 4096-token word-piece vocabulary, on one domain (English voice search). The method's dependence on subword tokenization — particularly whether biasing phrase tokens align with vocabulary boundaries — is not investigated. Only one ASR architecture is tested.

### Minor

4. **Limited analysis of out-of-domain/anti-biasing degradation mechanism.** Table 1 shows Anti-Biasing WER degrades from 1.7% (no biasing) to up to 2.3% (B=3000 with fusion F=4096). While small, this degradation is not analyzed (e.g., what fraction of errors are insertions of biasing entities vs. unrelated errors). Understanding this degradation mode is important for deployment.

5. **No hyperparameter sensitivity analysis.** The method has tunable hyperparameters (δ and, when applicable, λ), and the paper notes these were tuned based on a development set, but no plots or tables showing WER as a function of δ/λ are provided. This would help readers understand robustness.

6. **No ablation of the determinization loop vs. full forward table.** Section 2.1 discusses storing the O(m × |V|) forward table as an alternative to the failure-function-based approach, with a memory-accuracy trade-off. This trade-off is not empirically investigated — the paper only uses the memory-efficient failure function approach.

### Trivial

7. The introduction's phrasing "enables learning with the discrete structure of ASR biasing" (Section 1) is forward-looking (it refers to future potential for end-to-end training, as clarified in the conclusion), but could mislead readers into thinking the current method involves learned components. The current method uses only tuned scalar hyperparameters.

## Nice-to-Haves

- Comparison against a simple token-level biasing baseline (e.g., boosting any token appearing in any biasing phrase, without the KMP structure tracking) to ablate whether the partial-match tracking mechanism itself drives the gains.
- A hyperparameter sensitivity plot (WER vs. δ for a fixed configuration).
- Analysis of whether the method generalizes to other architectures (e.g., LAS, Transformer Transducer) and tokenization schemes.

## Removed Points

- **Criticism about the failure function algorithm being in the appendix:** The parser strips appendix content. The algorithm exists in the original submission. Removed per hard rule.
- **Criticism that simple scoring function is a major weakness:** The paper explicitly acknowledges this as future work (line 169) and frames it as a design choice. Kept as a minor point about limited analysis but downgraded from the critic's framing.
- **Criticism about "learning" claim being a major overstatement:** The paper's conclusion (line 408) clarifies this refers to future work. The intro claim is mildly overstated but trivial in impact.
- **Strength claiming "theoretical equivalence to deterministic FSA" as a major strength:** This is a standard known property of KMP (cited to CLRS). It's a supporting observation, not a novel contribution.
- **Demand for error type breakdown on Anti-Biasing:** Useful but not essential. Moved to Minor.
- **Demand for details of vectorized implementation:** The paper does mention the use of tf.while, tf.gather/tf.einsum (line 232). The critic may have missed this.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's two claimed contributions. The WER reductions (50–75% relative vs. no biasing) and complementarity with NAM are well-supported and significant. However, the efficiency story (TPU-friendliness as a replacement for WFST) is entirely theoretical, resting only on complexity analysis and architectural arguments about vectorization vs. sparse FST operations. This creates an asymmetric evaluation: the paper provides strong evidence for one claim (biasing works) while providing no evidence for its other core claim (it is a practical TPU-efficient alternative). The two claims could be decoupled — the KMP biasing method might be valuable even on GPU/CPU as a simpler alternative to WFST — but the paper does not explore this framing.

## Suggestions

1. **Most impactful single addition:** Add a WFST shallow fusion baseline (Zhao et al., 2019 style) comparing WER on the same test sets. This is the single missing piece that would validate or invalidate the paper's central positioning. If the WFST baseline achieves similar WER, the contribution shifts from "replacement" to "equivalent but more TPU-friendly algorithm." If KMP outperforms, the contribution is stronger still.

2. **Add at least one efficiency measurement** — e.g., real-time factor or wall-clock time per utterance on TPU, even for a single configuration. This would directly support the TPU-friendliness claim and distinguish the work from a purely algorithmic proposal.

3. **Add a second ASR architecture** (or at minimum acknowledge the limited scope explicitly) to support the generality claim, or temper the generality claim in the paper.

4. **Include a simple ablation** comparing KMP biasing to a naive token-level biasing bonus to demonstrate that the KMP structure-sensitive matching is necessary for the observed gains.

## Score and Decision

The paper presents a clever algorithmic contribution with solid WER improvements. However, the two major gaps — no comparison against WFST biasing and no efficiency measurements — mean the paper's core positioning as a TPU-friendly WFST replacement is unvalidated. The contribution stands as a novel biasing method that works well (proven) but not yet as the claimed alternative to WFST-based approaches (unproven). The paper would benefit substantially from a round of revision to address these gaps.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>