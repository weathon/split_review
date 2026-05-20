Now I have sufficient calibration data. Let me write the final review.

**Calibration Summary:**

Round 1 bracket: between 5 and 7.5.

Round 2 anchors read in full:
- **ASIDE** (avg 4.67, Accept Poster) — architectural defense against prompt injection. AIR has much stronger empirical results (ASR an order of magnitude lower) but requires adversarial training. AIR is clearly stronger.
- **HieraSuite** (avg 4.67, Reject) — instruction hierarchy toolkit. Criticized for limited originality. AIR scores higher on novelty.
- **Sysformer** (avg 5.00, Accept Poster) — adaptive system prompt defense. More limited baseline comparisons and evaluation scope. AIR is stronger.
- **"The Attacker Moves Second"** (avg 6.00, Reject) — attack evaluation, very mixed reviews (2,6,8,8). AIR is more self-contained and less controversial.

The paper under review is stronger than the 4.67–5.00 anchors and comparable in quality to the 6.00 anchor (but on a different topic). The evaluation is thorough, the method is simple and effective, and the weaknesses are minor. Score: **6.0**, Decision: **Accept**.

---

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks. The core idea is to inject instruction hierarchy (IH) signals not only at the input layer (as in prior work) but at every decoder layer via small, per-layer trainable embeddings. The authors evaluate AIR across three model sizes (3B–8B), two training procedures (SFT and DPO), static and gradient-based attacks, and two benchmarks. They report 1.6×–9.2× reduction in ASR on gradient-based attacks with minimal utility loss and negligible parameter overhead (0.005\%).

## Strengths

1. **Strong and consistent empirical results.** Table 1 shows AIR outperforms prior IH injection methods (Delim, ISE) across nearly all configurations. Representative numbers: on Llama-3.2-3B SFT, GCG ASR is 4.1% for AIR vs. 38% for Delim (9.2× reduction); Astra ASR is 0.1% for AIR vs. 14.5% for Delim. The improvement is consistent across all three model sizes and both SFT and DPO.

2. **Utility is maintained.** Figure 6 shows AIR's AlpacaEval win rate is within ~2 percentage points of a non-adversarially trained baseline, and in several configurations AIR actually improves utility. This demonstrates the robustness gain does not come at a significant utility cost.

3. **Thorough evaluation scope.** The paper evaluates 3 model families (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B), 2 training methods (SFT, DPO), 2 gradient-based attacks (momentum-GCG, Astra), 4 static attacks, and 2 benchmarks (AlpacaFarm, SEP). This provides strong evidence for the method's generalizability.

4. **Negligible parameter overhead.** AIR adds only 0.4M parameters for an 8B model (0.005% increase) — the per-layer embedding tables are extremely lightweight, making the method practical for deployment.

5. **Well-motivated design.** The paper identifies a concrete limitation of the ISE method (input-only IH signal degrades across layers, shown by increasing cosine similarity in Figure 3), and directly addresses it with multi-layer injection. The analogy to how RoPE distributes positional information across layers rather than only at the input provides intuitive grounding.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The cosine similarity analysis in Figure 3 is partially misleading for the delimiter method.** The paper computes cosine similarity between token representations of different privilege levels. For the delimiter method, privilege is signaled by *special tokens* placed at segment boundaries, not by modifying the embedding of every token. The representation of a regular token in a privileged segment does not carry an explicit privilege signal in its individual embedding — the model must infer privilege from context. Computing cosine similarity between representations of regular tokens measures a quantity the delimiter method was never designed to control, yet the figure treats all three methods uniformly. The comparison between ISE (which adds segment embeddings per token) and AIR is valid and supports the paper's motivation. The delimiter curve creates a false impression that *all* prior methods suffer from the same degradation, when delimiters work through a different mechanism. The authors should either remove the delimiter curve or add a discussion clarifying why the metric is not meaningful for that method. This does not invalidate the paper's core contribution but weakens the framing.

2. **Missing ablation on whether per-layer IH embeddings must be layer-specific.** The paper's claim that per-layer customization is the reason AIR outperforms input-only methods would be strengthened by testing whether sharing the same embedding table across all layers (or using a smaller set of shared tables) yields comparable results. If a single shared embedding works almost as well, the paper's explanation would need revision. This is a natural ablation that would deepen the contribution.

3. **Single attack budget for all defenses.** The paper uses fixed optimization steps (200 for DPO, 50 for SFT) and a 100-token prefix for all defenses. While Figure 7 shows AIR's loss remains substantially higher and the gap does not appear to be closing, some ASR numbers (e.g., Qwen-2.5-7B SFT: AIR 22.6% vs. ISE 36.6% for GCG) could shift with more aggressive optimization. A robustness saturation test (ASR vs. optimization steps beyond the current budget) would increase confidence that the ranking is stable.

### Trivial

4. **The initialization of AIR's IH embeddings is not specified.** The paper states the embeddings are added to the residual stream but does not state whether they are zero-initialized (the sensible choice to avoid disrupting the pre-trained model) or randomly initialized. This should be stated.

## Nice-to-Haves

- **Statistical significance of ASR differences.** The ASR numbers in Table 1 are point estimates from single runs. Given the variance in GCG (which depends on random initialization), reporting standard errors or running attacks with multiple seeds would increase confidence. This is standard practice in the adversarial examples literature.
- **Analysis of why AIR makes gradient-based attacks harder.** For example, comparing gradient norms with respect to the adversarial prefix across defenses, or measuring how the per-layer IH embeddings change during training and correlate with robustness. Such analysis would deepen the paper beyond "it works."
- **Clarity on the cosine similarity measurement.** The paper should specify exactly which tokens are included in the cosine similarity computation, whether the delimiter tokens themselves are included for the Delim method, and whether the similarity is averaged over prompts or over tokens.

## Removed Points

- **"The paper identifies a concrete limitation of prior defenses" (Strength Finder #4).** Retained in a qualified form because the ISE-vs-AIR comparison in Figure 3 is valid; only the delimiter curve is misleading.
- **"Analogy to RoPE strengthens plausibility" (Strength Finder #8).** Removed as a generic rhetorical point, not a core strength.
- **"Adaptive attacks clarity" (Harsh Critic).** The paper's "white-box" description is adequate; no additional clarification needed.
- **Formatting/typographical nitpicks.** Parser artifacts, not author errors.
- **Missing appendix content and references.** These are stripped by the PDF parser and exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The observation that input-level IH signals degrade across layers (for ISE) and that injecting per-layer trainable embeddings substantially improves robustness is the paper's core finding.

## Suggestions

1. Address the Figure 3 issue: either remove the delimiter curve or add a clear discussion of why the cosine similarity measure is not directly applicable to the delimiter mechanism.
2. Add a shared-vs-per-layer IH embedding ablation to strengthen the causal claim.
3. Report ASR with standard errors (multiple seeds).
4. Specify the initialization scheme for AIR's embedding tables.
5. Add a saturation plot for attack steps on one representative configuration.

## Score and Decision

**Round 1 bracket:** The paper is clearly above the weak anchors (scores ~2–3, rejected papers on LLM safety) and below the very strong anchors (scores ~8, broader-scope papers). Initial bracket: 5–7.5.

**Round 2 narrowing:** Compared against four closely related anchors read in full:
- ASIDE (avg 4.67, Accept Poster) — similar defense topic; AIR has stronger empirical results.
- HieraSuite (avg 4.67, Reject) — instruction hierarchy toolkit; AIR has more originality.
- Sysformer (avg 5.00, Accept Poster) — defense through adaptive prompts; AIR has more thorough evaluation.
- "The Attacker Moves Second" (avg 6.00, Reject) — attack evaluation paper, very mixed reviews.

The paper is stronger than the 4.67–5.00 anchors in terms of empirical thoroughness and strength of results, and comparable in quality to the 6.00 anchor. The main weakness (cosmetic issue with Figure 3 framing) is minor and does not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>