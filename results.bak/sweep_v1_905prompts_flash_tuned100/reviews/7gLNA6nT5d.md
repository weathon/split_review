Now I have all the information I need. Let me write the final consolidated review.

**Round 1 bracket:** After inspecting anchors in the weak (avg 2.5–3.4), middle (avg 5.5–6.67), and strong (avg 7.75+) bands, I place this paper in the **4.5–6.0 range** — clearly above papers with fundamental flaws (e.g. "Actions Speak Louder Than States" at 4.75 had a wrong problem formulation) but below clearly acceptable papers (e.g. DICP at 6.67 had more rigorous experiments).

**Round 2 narrowing:** Reading anchors in the 4.5–6.5 band:
- Memory-Efficient AD (5.50, Reject): similar AD-modification paper. This paper has a more novel idea but more methodological gaps → slightly weaker.
- ICPL (6.00, Reject): stronger experimental validation in a different area → this paper is weaker.

**Final score:** 5.0. The contribution is real but the causal masking gap, undersupported 27× claim, and missing experimental details prevent acceptance.

---

## Summary

This paper integrates n-gram induction heads (from Akyürek et al. 2024) into transformers for in-context reinforcement learning, specifically Algorithm Distillation (AD). The authors modify the transformer architecture to hardcode n-gram attention patterns, which they show improves data efficiency and reduces hyperparameter sensitivity. They extend the approach to pixel-based environments via vector quantization. Experiments on Dark Room, Key-to-Door, and Miniworld environments provide evidence that the n-gram model matches or outperforms AD, especially in low-data regimes.

## Strengths

- **First application of n-gram induction heads to ICRL** — This is a sensible and novel adaptation of an architectural idea from language modeling to the decision-making setting. The paper correctly identifies that n-gram patterns can help overcome the simplicity bias in transformers that hinders in-context RL.

- **Clear evidence of improved hyperparameter search efficiency** — Figure 2 and the accompanying text show that with 1K histories, the n-gram model finds optimal hyperparameters in ~20 assignments versus >400 for the baseline. This is a concrete, well-visualized demonstration of reduced training instability.

- **Extension to visual observations via VQ is a practical contribution** — Section 2.3's use of vector quantization to enable n-gram matching on pixel observations, combined with the Miniworld results in Figure 5, shows the method can leave the discrete-state setting where prior n-gram work was confined.

- **The permutation experiment (Table 1c) is well-designed** — Shuffling the n-gram attention matrix produces no degradation relative to the baseline (0.51 vs 0.52), which supports the claim that the n-gram layer does not harm performance even when the matching is flawed, and partially addresses the concern that extra parameters alone drive the gains.

- **Ablation on n-gram hyperparameters shows robustness** — Tables 1(a,b) demonstrate that EMP is stable across n-gram lengths (0.67–0.76) and layer positions (0.67–0.69), indicating minimal overhead from the new hyperparameters.

## Weaknesses

### Major

- **The n-gram attention formula does not discuss causal masking, creating a methodological ambiguity.** The attention pattern is defined as \(A(n)_{ij} \propto \mathbb{1}[\bigwedge_{k=1}^n x_{i-k} = x_{j-k-1}]\) without any restriction that \(j \le i\). In an autoregressive transformer used for RL sequences, attending to future positions would leak information and invalidate the method. The paper briefly mentions "train both causal and n-gram attention layers simultaneously" (Section 2.3) but never clarifies whether causal masking is applied to the n-gram attention pattern itself, or only to the standard attention layers. This is not a speculative gap — the paper is actually silent on a critical implementation detail that could affect correctness. The authors must either confirm that standard causal masking applies (and if so, how the pattern is restricted to \(j < i\)) or revise the architecture accordingly.

- **The 27× data reduction claim is not adequately supported by the evidence presented in the main text.** The paper states in Section 4.2 that "our method needs 27x less data comparing to baseline" and directs readers to Appendix B (stripped by the parser) for justification. Figure 4 does show the n-gram method achieving near-optimal return with 100 goals and ~1K histories while the baseline plateaus at suboptimal performance. However, the 27× factor depends on an indirect comparison: the paper asserts that the baseline "needs 2048 goals and 2048 learning histories [17]" (citing the original AD paper), but does not run its own baseline at that data scale in the same experimental setup. The comparison is against a published result from a different paper, not a controlled experiment. The claim could be true, but the paper does not provide the direct evidence that such a strong quantitative claim requires.

- **Missing experimental details that affect reproducibility and interpretation.** The hyperparameter search space is not listed in the main text (Appendix C is stripped). The number of random assignments used to compute EMP curves is not consistently reported. Most EMP figures lack error bars or confidence intervals (Figure 6 has them but Figures 2, 4, 5 do not). VQ codebook size and training details are not reported. The data generation procedure for the baseline is a departure from the original AD setup (decaying noise schedule from Zisman et al.), which is fine for within-paper comparisons but weakens external comparisons to AD-published numbers.

### Minor

- **No parameter-count-controlled baseline.** The n-gram layer adds two learned projection matrices (\(W_1, W_2\)) per head. The permutation experiment (Table 1c) rules out a naive "extra parameters cause gains" story, but a proper control — adding an equivalent number of parameters to the baseline (e.g., an extra linear layer or widened MLP) — would cleanly isolate the benefit of the n-gram inductive bias. This is standard practice for architectural papers.

- **The "state matching only vs. full transition matching" distinction is interesting but underexplored.** Figures 2 and 4 show that matching on states alone outperforms matching on full \((s,a,r)\) transitions in some settings. The paper does not analyze *why* this pattern holds, which would strengthen the understanding of when n-gram heads help in RL.

### Trivial

- "Transitivity of the in-context ability" (Conclusion, line 230) appears to be a typo for "transience" — the cited reference [27] is titled "The transient nature of emergent in-context learning in transformers."

## Nice-to-Haves

- The computational cost of the n-gram attention (O(T²) pattern matching per layer) is not discussed. A brief complexity comparison against standard attention would be useful for practitioners.
- A sensitivity analysis on VQ codebook size for the Miniworld experiments would strengthen the image-based results.
- Reporting whether the same random hyperparameter order was used for both the n-gram and baseline methods (to ensure fair EMP comparisons).

## Removed Points

The following points were raised by reviewers but are removed for the reasons stated:

- **"27× claim is unverifiable because the appendix is stripped"** — Partially inaccurate. Figure 4 in the main text does provide visible evidence of data efficiency (n-gram with 100 goals vs baseline plateauing). The precise numerical derivation is in the appendix, but the qualitative claim of improved data efficiency is supported. The weakness is retained at Major status, but rephrased as "insufficiently supported by direct experimental evidence" rather than "unverifiable."
- **"Figure reference error: Section 4.3 references Figure 6 for image-based results"** — Not an error. Figure 6 is correctly about hyperparameter sensitivity in Miniworld (pixel-based) environments. The reference is accurate.
- **"The (Room, omitted for brevity) text is confusing"** — This is a minor parenthetical note; it is clear in context that it refers to the Miniworld-Dark variant being analogous to the Dark Room environment.
- **"Strawman about hyperparameter search space not described"** — Partially valid; folded into the "missing experimental details" Major weakness.

## Novel Insights

The most interesting observation to emerge from the reviews is the asymmetry between the two matching strategies (states-only vs. full transitions). Figures 2 and 4 consistently show that matching on states alone outperforms matching on the full \((s,a,r)\) transition. This is non-obvious: one might expect the richer signal in full transitions to be more informative. A plausible explanation is that action and reward tokens introduce noise into the n-gram matching because the same state can be paired with different actions (due to exploration) or different rewards (due to partial observability in Key-to-Door). The paper does not develop this point, but it is the kind of insight that could guide future work on n-gram heads in sequential decision-making.

## Suggestions

1. **Clarify causal masking** — Add an explicit statement about whether and how the autoregressive causal mask is applied to the n-gram attention pattern. A simple modification: restrict the indicator function to \(j < i\) (or equivalently, apply the standard causal mask after computing the n-gram attention weights).

2. **Run the direct data-efficiency experiment** — Train the baseline AD on 2048 goals × 2048 histories in the same environment (Key-to-Door) and compare directly against the n-gram model on 100 goals × ~1K histories. This would allow the 27× claim to be either substantiated or appropriately qualified.

3. **Add a parameter-count-controlled baseline** — Add either an extra linear layer or a wider MLP to the baseline AD to match the n-gram model's parameter count. Show that the n-gram method still outperforms this augmented baseline.

4. **Report error bars on all EMP figures** and list the number of random hyperparameter assignments used. Describe the hyperparameter search space in the main text (or ensure Appendix C is available).

## Score and Decision

**Score: 5.0**  
**Decision: Reject**

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Y8DClN5ODu (Demonstration Distillation) | 3.40 | 1 | Significantly weaker — paper had a flawed problem setup. This paper is better. |
| 7ienVkNf83 (EReLELA) | 3.00 | 1 | Much weaker — emergent language for RL exploration with limited validation. |
| cb4etlGvOY (Towards Autonomous Agents) | 2.50 | 1 | Much weaker — limited results on text games. |
| to4PdiiILF (Honesty to Subterfuge) | 3.00 | 1 | Weaker — different setting (LLM safety). |
| 5iWim8KqBR (Memory-Efficient AD) | 5.50 | 1,2 | Similar space — both modify AD architecture. This paper has a more novel idea but more methodological gaps. Slightly weaker overall. |
| BfUugGfBE5 (DICP) | 6.67 | 1 | Stronger — more comprehensive experiments, cleaner methodology. This paper is clearly weaker. |
| 2Y5kBPtU0o (MEND) | 6.25 | 1 | Different domain (LLM demonstrations), stronger validation. |
| XnX7xRoroC (Distilling RL into Single-Batch) | 6.25 | 1 | Different setting, comparable rigor. |
| b5MCteb3w7 (Actions Speak Louder) | 4.75 | 2 | Had fundamental problem formulation issues. This paper is stronger. |
| w9tS6NRmxX (ICPL) | 6.00 | 2 | Stronger experimental validation in a different (LLM+RL) area. |
| qH8ADnIVII (Dynamic Demonstrations Controller) | 5.75 | 2 | ICL for NLP, comparable rigor. |

**Round 1 bracket:** 4.5–6.0  
**Round 2 narrowing:** Comparing against the Memory-Efficient AD (5.50) and Actions Speak Louder (4.75) anchors, this paper sits between them — above the fundamentally flawed paper but below the cleaner AD-modification paper due to its methodological gaps.  
**Final score:** 5.0 — The core idea has genuine merit and the experiments show promise, but the causal masking ambiguity, undersupported 27× claim, and missing experimental details collectively prevent acceptance. A revised version addressing these issues could be a solid incremental contribution.

MY FINAL SCORE: 5.0
MY FINAL DECISION: Reject