Now I have thoroughly verified all claims against the actual paper. Let me produce the consolidated review.

## Summary

This paper proposes UPV, the first watermarking framework for LLMs that separates watermark generation and detection into two distinct neural networks, enabling public verifiability without exposing the generation key. The key technical innovation is sharing the token embedding layer between the generator and detector, which bootstraps the detector to near-oracle accuracy. The paper claims unforgeability on the basis of computational asymmetry: constructing a generator from the detector is argued to be much harder than the reverse.

## Strengths

- **Novel framework enabling public verifiability without key exposure.** The idea of using separate neural networks for generation and detection, rather than a shared secret key, directly addresses a fundamental limitation of prior watermarking work (Kirchenbauer et al., Zhao et al., etc.) and opens the door to third-party detection scenarios. This is a genuine architectural contribution, not an incremental tweak.

- **Shared token embedding dramatically improves detection accuracy (Table 2).** The ablation study shows that removing the shared embedding causes F1 to collapse—from ~99% to as low as 0.5% for GPT-2 on C4—and fine-tuning the shared embeddings hurts performance (dropping F1 by ~11%). This clean ablation convincingly demonstrates that the shared embedding is the critical design choice, not an incidental detail.

- **High detection accuracy nearly matching the key-based upper bound.** Across three LLMs (GPT-2, OPT 1.3B, LLaMA 7B), two datasets (C4, Dbpedia), and two decoding methods, network-based detection achieves F1 scores of 97.5–99.8% with false positive rates below 1.2% (Table 1). The gap to the key-based oracle is small (~1–2% FNR), which is impressive for a detector that does not have access to the watermark generation rule.

- **Minimal computational overhead.** The generation network has only 43k parameters (~1ms added per token), making the approach practical.

- **Comprehensive evaluation across diverse settings.** Experiments cover three scales of LLM (124M to 7B), two datasets, two decoding methods, and both key-based and network-based detection, which supports generality.

## Weaknesses

### Fatal
None.

### Major

- **The forgery attack experiment does not report the attack success rate at the default operating point (window size w=5).** The paper's main experiments (Table 1) and hyperparameter configuration (Section 5.1) use w=5 as default. Figure 2(a) shows attack success as a function of window size, and the text states the trend that the reverse-training attack "decreases gradually as the window size increases until it drops to 0.5." But without reporting the numerical attack success rate at w=5 — the actual setting used throughout the paper's own evaluation — a reader cannot determine whether the watermark is forgeable at the system's default operating point. If attack success at w=5 is high (e.g., F1 > 0.8), the central claim of unforgeability is undermined at the exact configuration the authors chose. This is a missing experiment that directly impacts the paper's headline contribution. The authors should provide attack success rates at w=5 and at several larger window sizes (e.g., 10, 20) to establish the security margin.

- **The threat model defines removal attacks as a condition for the watermark being "broken," but the paper explicitly excludes removal robustness from evaluation.** Section 3 states: "If a user can consistently remove the watermark (over 90%) using a rewriting algorithm, then the watermark is considered broken." Yet the Conclusion (Section 6) says "robustness in the face of multiple rewrites or more intense attack scenarios remains unexplored" and places this "beyond the scope of our current work." This is a direct contradiction: the paper defines a criterion for the watermark being "broken" and then declines to test or argue about it. The issue is not that the paper lacks robustness experiments — robustness is legitimately separable from unforgeability — but that the threat model should be scoped to match what the paper actually evaluates. The fix is straightforward: remove or rewrite the removal-attack discussion from the threat model, or explicitly test minimal robustness.

### Minor

- **The claim that training the detector on randomly generated token sequences "theoretically avoids out-of-domain issues" (Section 4.4) is not justified.** Random token sequences have radically different statistical structure (uniform token distribution, no co-occurrence patterns) from natural language. While the detector empirically works well on real text (Table 1), which is the important result, the paper offers no analysis of *why* it generalizes — e.g., whether the detector's outputs correlate with ground-truth z-scores, or whether it is learning some other heuristic. The empirical success is the result that matters, and the paper should either remove the unsupported "theoretically avoids" claim or provide supporting analysis.

- **The description of the embedding mechanism is ambiguous.** Section 4.2 states: "The embedding network accepts the binary representation of token IDs as input... requiring 16 bits for its binary representation." This could mean (a) token IDs are converted to their 16-bit binary form and fed through a learned linear layer, or (b) the paper is simply describing the bit-width of standard integer token IDs used as indices into an embedding lookup table. The latter is standard practice; the former would be unusual and needs clarification. Reproducibility requires knowing the actual input representation to the embedding network.

- **The key-based baseline's z-score formula is not explicitly stated.** The key-based baseline (Table 1) is described as the method of Kirchenbauer et al., which uses the simple z-score without the σ² correction. The paper's detection network is trained on the corrected z-score (Equation new-z). Since σ is measured to be <0.02, the practical difference is negligible, but the paper should state explicitly whether the key-based baseline uses the simple or corrected z-score to avoid any ambiguity about the comparison.

### Trivial
- None that affect evaluation.

## Nice-to-Haves

- **Additional attack vectors:** The paper tests two attack strategies (reverse training, frequency analysis). An attacker could also attempt direct optimization of token sequences against the detector (e.g., genetic algorithms or RL). While the paper's analysis of label-interdependency provides a general argument for difficulty, a brief discussion of why direct optimization would face similar or greater challenges would make the security argument more complete.

- **Correlation analysis between detector output and z-scores:** Showing that the detector's predictions correlate with ground-truth z-scores on real text would cleanly address the "random training data" concern without needing further theoretical justification.

- **Larger window size sweep in main detection experiments:** The paper uses w=5 throughout. Since unforgeability improves with larger w, reporting main detection results at w=10 or w=20 as well would demonstrate the detection F1 remains high at configurations where unforgeability is stronger.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's "Missing Parts" point about detection network training data generation (sequence length, sample count, threshold z):** These implementation details (how random sequences are generated, number of samples, z-threshold) are reasonably placed in the appendix. The paper explicitly references the appendix for training details (line 117: "see the appendi \ref{sec:detail}"). Since the parser strips appendix content from all papers, this criticism is an artifact of the review format, not an omission by the authors.

- **Harsh critic's "Other Observations" point about reverse-training attack (genetic algorithms/RL):** This is a suggestion for extending the threat analysis, not a weakness. The paper tests two specific attacks and provides a theoretical argument for why reverse training is hard. Suggesting additional attacks is reasonable future work but does not indicate a flaw in the paper as written.

- **Strength Finder's strength 3 ("Empirical demonstration of unforgeability against two attack strategies"):** Retained but implicitly qualified by the Major weakness about missing attack success at w=5. The existence of the experiment is a strength; the incompleteness at the default operating point is a weakness. These are not in direct contradiction — the experiment exists but is incomplete.

- **Harsh critic's suggestion about providing "numerical attack success rates... for several larger window sizes"** — this is already captured in the Major weakness above, not a separate point.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not articulate about its contributions or limitations. The key tension — that the unforgeability trend is demonstrated but the default operating point's security is not quantified — is a standard review observation rather than a novel synthesis.

## Suggestions

1. **Report attack success at the default w=5.** Run the reverse-training attack at w=5 and report the forged watermark's detection F1 alongside the genuine detection F1. If the attack succeeds at w=5, check whether larger window sizes (e.g., w=10, w=20) maintain high detection accuracy while blocking forgery, and adjust the operating point accordingly.

2. **Align the threat model with the evaluation.** Either (a) remove removal attacks from the threat model entirely (they are not evaluated and are explicitly scoped out), or (b) add a small experiment showing that the watermark survives simple synonym substitution at reasonable rates. The former is cleaner and avoids diluting the contribution.

3. **Clarify the embedding input format.** State explicitly whether the embedding network uses standard integer-indexed lookup or a learned transformation from a binary vector. If it is standard lookup, avoid the phrase "binary representation" which implies a different mechanism.

4. **Tone down the "theoretically avoids out-of-domain issues" claim.** The detector works empirically (Table 1), which is sufficient. The unsupported theoretical claim risks distracting readers; replace it with a more measured statement about empirical generalization.

5. **State explicitly which z-score formula the key-based baseline uses** and confirm that σ is small enough that the correction does not affect the comparison.

## Score and Decision

The paper introduces a genuinely novel architecture for publicly verifiable LLM watermarks, supported by strong detection accuracy results and a compelling ablation study. The shared-embedding design is clean and well-validated. However, the paper's central claim of *unforgeability* has an evidentiary gap: the attack success rate at the default window size (w=5) is not reported, so the security margin at the system's own operating point is unknown. Additionally, the threat model contains a scope inconsistency that should be resolved. These issues are structural in that they affect a core claim, but they are addressable in revision. The paper should not be accepted in its current form.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>