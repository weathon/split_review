Now I have all the information needed. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects instruction hierarchy (IH) signals into every decoder layer of an LLM via small per-layer trainable embedding tables, rather than confining IH signals to the input layer as prior work does. The authors argue that input-only IH signals degrade as they propagate through the model, and they provide evidence (cosine similarity trends across layers, linear probing) that AIR maintains better privilege-level separation throughout the network. Experiments across three model families (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B) and two training paradigms (SFT, DPO) show AIR reduces white-box GCG attack success rates by 1.6× to 9.2× over prior defenses while preserving utility on AlpacaEval and MMLU.

## Strengths

- **Clear empirical demonstration of the input-only signal degradation problem.** Figure 3 shows that cosine similarity between same-privilege tokens increases across layers for Delimiters and ISE but stays low for AIR. The linear probing experiment (Appendix E, Fig. 10) confirms that ISE's near-perfect separability in early layers drops to 91% by the final layer, while AIR maintains near-perfect accuracy throughout. These two complementary analyses provide concrete motivation for the layer-wise approach.

- **Lightweight, practical design.** AIR adds only 0.4M parameters (~0.005%) for a Llama-3.1-8B model and negligible inference overhead, making it genuinely practical. The method is architecturally simple: per-layer embedding tables indexed by privilege level, summed with intermediate representations.

- **Strong and consistent robustness gains across diverse settings.** Table 1 shows AIR reduces GCG ASR substantially across all three model sizes and both training methods (e.g., Llama-3.2-3B/SFT: 4.1% vs. 38% Delim and 48.1% ISE; Qwen-2.5-7B/DPO: 1.6% vs. 7.7% ISE). The adversarial loss curves (Figures 7, 9) independently corroborate that AIR consistently imposes higher optimization loss on gradient-based attackers. Static attack results (Table 1 top rows) and BIPIA results (Table 2) further confirm broad robustness.

- **Utility is well-preserved.** AlpacaEval win rates (Figure 6) show <2% degradation. MMLU scores (Figure 11) remain comparable across all defenses. The SEP benchmark (Figure 8) shows AIR achieves the best utility×separation trade-off, particularly with DPO training.

## Weaknesses

### Fatal

None.

### Major

- **White-box ASR metric is insufficiently specified, weakening the headline quantitative claims.** Section 5.4 states that for gradient-based attacks, "ASR is measured using the likelihood (from model's logits) of generating the target phrase hacked!" No threshold, decision rule, or validation against actual generated strings is reported. The headline 1.6×–9.2× reduction claims depend on this metric. The adversarial loss curves (Figures 7, 9) provide independent, more reliable evidence that AIR makes attacks harder to optimize, but the precise ASR percentages cannot be fully verified from the paper. Clarifying whether this uses argmax generation, a probability threshold, or another binary rule — and validating it against actual output strings — would substantially strengthen confidence.

### Minor

- **No capacity-controlled ablation isolates layer-wise injection from parameter budget.** AIR adds K×d parameters per layer (plus final), yielding ~33× more IH-dedicated trainable parameters than ISE (input-only). While the absolute increase is tiny (0.4M for an 8B model), the paper does not rule out the possibility that the gains partly stem from having more capacity to encode privilege information rather than from *where* it is injected. An experiment equalizing the total IH parameter budget (e.g., expanding ISE's embedding dimension, or reducing AIR's layer coverage) would sharpen the central attribution claim.

### Trivial

- The analogy to Rotary Position Embeddings (RoPE) in Section 4 ("inset") is loosely drawn and adds little explanatory value — RoPE modifies attention computations, whereas AIR adds a bias vector to representations before each block. This does not affect the technical contribution but could mislead readers.

## Nice-to-Haves

- An adaptive white-box attack evaluation where the attacker is aware of AIR's per-layer embeddings and jointly optimizes to cancel or circumvent them would provide stronger security evidence, though this is acknowledged as beyond the scope of the current evaluation.
- A per-layer ablation (training AIR with embeddings in only a subset of layers) would reveal whether all layers are necessary or a few critical positions suffice, and would help address the capacity confound.
- Qualitative examples of attack trajectories — concrete prompts where the same adversarial prefix succeeds against Delim/ISE but fails against AIR — would give intuition for *how* AIR changes model behavior.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The white-box ASR metric is undefined, making all quantitative results untrustworthy"** (from Harsh Critic point 1, escalated severity). The harsh critic claims the metric is completely undefined and that results "cannot be taken at face value." While the ASR definition is indeed insufficiently precise (retained as a Major weakness above), the paper does report the loss curves (Figures 7, 9) which independently demonstrate AIR's superior robustness against gradient-based attacks across all models and training methods. The static attack results use exact-match ("contains the literal phrase hacked!") and also favor AIR. The core finding does not rest solely on the likelihood-based ASR. The removed claim overstates the severity.

2. **"Potential mismatch between adversarial training and test-time attacks"** (Harsh Critic point 3). This criticism argues that training with Naive/Ignore attacks while testing with GCG/Astra is a methodological gap. However, all compared defenses receive identical training, making this a fair comparison. The gap between training and test attacks affects all methods equally; the fact that AIR outperforms under these conditions is evidence *for* AIR's architectural advantage, not against it. This is removed as a strawman.

3. **"Figure 3 and linear probing results merely confirm that the injection works as designed"** (Harsh Critic, Introduction notes). The harsh critic argues these results are tautological. While AIR's design does trivially force representations of different privilege levels to differ by a constant vector, the ISE and Delim results are not tautological — they independently demonstrate that input-only signals degrade (ISE drops from 100% to 91% separability). The comparison validates the core hypothesis. This critique is removed as a misunderstanding.

4. **"RoPE analogy is not actually executed — claimed conceptual connection is weak"** (Harsh Critic, Section 4 notes). This is a presentation nitpick. The analogy is clearly presented as conceptual: "Our proposal shares an interesting similarity with the research on positional embedding... Our proposal applies the same underlying principle — distributing critical privilege information across all layers." The paper does not claim to modify attention mechanisms. Removed as a minor presentation quibble.

5. **"The SEP formulas are garbled in the text"** (Harsh Critic, Section 5). This is a parser artifact — the original PDF does not have garbled formulas. Removed per formatting artifact rule.

6. **Strength Finder: "The design is lightweight and clearly motivated"** — Retained in main review as a strength with concrete numbers.

7. **Strength Finder: "Ablation-style evidence supports the benefit of pervasive IH injection"** — This is essentially the same as the progressive improvement argument already captured in the robustness gains strength. Not dropped but merged.

8. **"Sensitivity to embedding initialization suggests the method is brittle"** (Harsh Critic, Deeper Analysis). The paper documents that Qwen needed a different initialization scale (σ=0.1 vs. 0.02 for Llama) and provides practical guidelines for porting to new models (Appendix B.2). This is transparent reporting, not a weakness — and the same adjustment was applied to ISE for fair comparison. Removed.

9. **"Missing comparison to ASIDE or other beyond-input-layer injection strategies"** (Harsh Critic, Related Work). ASIDE is discussed in Appendix D as concurrent work. The paper identifies its novelty relative to existing methods. Removed as a missing-reference nitpick.

## Novel Insights

The paper makes a clean, testable observation that is genuinely instructive: input-level instruction hierarchy signals (whether delimiter tokens or additive embeddings) lose discriminative power as representations propagate through decoder layers, and this degradation correlates with reduced robustness to prompt injection attacks. The linear probing experiment showing ISE dropping from near-perfect to 91% separability is a crisp demonstration that could inform future defense design beyond this particular method.

## Suggestions

- **Clarify the white-box ASR metric.** Specify the exact binary decision rule (e.g., argmax decoding followed by substring match, or a probability threshold) and validate it on a subset of examples against actual generated outputs. This is the single most important fix.
- **Add a capacity-controlled baseline.** Train an ISE variant with expanded embedding dimensions matching AIR's total IH parameter budget, or an AIR variant with embeddings in only a subset of layers at equal capacity. This would cleanly disentangle the "where" vs. "how much" question.
- **Show qualitative examples.** Pick 2-3 cases where the same GCG-optimized prefix succeeds against ISE/Delim but fails against AIR, and show the generated outputs. This would make the results more tangible.

## Score and Decision

**Anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/7B9mTg7z25.md` (avg 6.00, Reject): "The Attacker Moves Second" — Broader methodological contribution (breaking 12 defenses, introducing adaptive evaluation framework). AIR has a narrower but cleaner architectural contribution. AIR is slightly below this.

- `/home/wg25r/review_agent/human_reviews_2026/gMajoi2xsq.md` (avg 4.67, Reject): "HieraSuite" — Toolkit/benchmark paper criticized for limited originality. AIR has a more novel architectural contribution and cleaner evaluation. AIR is above this.

- `/home/wg25r/review_agent/human_reviews_2026/RgOHRYHX5L.md` (avg 4.50, Reject): "Inoculation Prompting" — Simple technique with thorough empirical validation across 4 settings. Comparable in spirit (simple idea, solid evaluation), but AIR addresses a more concrete security problem with practical implications. AIR is comparable.

- `/home/wg25r/review_agent/human_reviews_2026/IeNXtofK6T.md` (avg 3.50, Reject): "PromptArmor" — Simple baseline paper with limited novelty. AIR is clearly above this.

- `/home/wg25r/review_agent/human_reviews_2026/fF9alVesJ0.md` (avg 3.50, Reject): "IntentGuard" — Novel defense idea but limited benchmarks and baselines. AIR has broader empirical coverage. AIR is above this.

- `/home/wg25r/review_agent/human_reviews_2026/k5Sc3ageMW.md` (avg 2.50, Reject): "Reasoning Up the Instruction Ladder" — Similar IH topic but incremental, synthetic data limitations. AIR is clearly above this.

The paper makes a real contribution: a simple, lightweight architectural modification that consistently improves robustness against prompt injection attacks, with good empirical coverage and well-preserved utility. The core weakness is the imprecisely specified white-box ASR metric, which makes the headline quantitative claims somewhat less trustworthy than they should be, though the loss curves and static attack results independently support the core finding. This weakness is addressable in a rebuttal. Compared to the anchors, the paper falls above the 4.5–4.67 rejected papers in originality and empirical quality, and slightly below the 6.0 paper in breadth of contribution. A score of 5.5 reflects a solid contribution with one significant but addressable methodological gap.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>