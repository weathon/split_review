Now I have all the information I need. Let me write the final consolidated review.

**Round 1 Bracket:** 4.5–6.5 (SeaKR is clearly stronger than TARG at 4.0, but not at the level of 8.0 papers about fundamental LLM mechanisms)

**Round 2 Narrowing:** Compared against Interact-RAG (5.5), FrugalRAG (5.0), and SelfReflect (5.5), SeaKR sits slightly higher due to its cleaner experimental design, more principled uncertainty signal, and more comprehensive evaluation spanning both complex and simple QA. Final score: **6.0**.

---

## Summary

This paper proposes SeaKR, an adaptive RAG method that uses the Gram determinant of hidden-state representations of the `<EOS>` token across multiple generations as a self-aware uncertainty signal. This signal drives three components: (1) self-aware retrieval (triggering retrieval when uncertainty exceeds a threshold), (2) self-aware re-ranking (selecting the knowledge snippet that minimizes uncertainty), and (3) self-aware reasoning (choosing between answer-generation strategies based on uncertainty). Experiments on complex multi-hop QA (2Wiki, HotpotQA, IIRC) and simple QA (NQ, TriviaQA, SQuAD) show consistent improvements over prior adaptive RAG methods.

## Strengths

- **Novel and coherent unification of retrieval decisions, knowledge selection, and reasoning strategy choice under a single internal-state signal.** Prior adaptive RAG methods rely on output-level signals (e.g., token probability, prompting) for retrieval decisions and largely neglect adaptive knowledge integration. SeaKR's use of the Gram determinant of hidden-state representations across multiple generations—adopted from INSIDE but repurposed for the RAG context—provides a principled, tuning-free signal that the paper demonstrates works for all three decision points. The related work section (Sec. 2) properly articulates the limitations of output-level approaches (self-bias, information loss during decoding).

- **Systematic ablation with controlled alternatives for the uncertainty estimator.** Table 2 (referenced in Sec. 5.1) compares six alternative uncertainty estimation methods (prompting, perplexity, multi-perplexity, LN-Entropy, energy score, and SeaKR's Gram determinant), showing that the chosen method yields the best F1 on both 2Wiki (36.0% vs. next-best 34.1%) and NQ. This provides rigorous evidence that the specific internal-state consistency measure is well-motivated, not just an arbitrary choice.

- **Consistent and nontrivial gains on complex multi-hop QA**, where adaptive RAG is most needed. SeaKR outperforms the best baselines by 6.0% F1 on 2Wiki, 5.5% on HotpotQA, and 0.6% on IIRC (Sec. 4.2). On complex QA, it also outperforms the fine-tuned Self-RAG by 6.2% and 6.3% F1 on 2Wiki and HotpotQA respectively, demonstrating the advantage of a tuning-free intrinsic signal over training-based approaches that suffer from distribution shift.

- **Ablation study showing self-aware re-ranking contributes more than self-aware retrieval** (Sec. 5.1). This is a non-obvious finding: "ablating self-aware re-ranking reduces the performance of SeaKR more than removing self-aware retrieval." It directly supports the paper's claim that *how* knowledge is integrated is at least as important as *when* to retrieve—a novel insight for the adaptive RAG literature.

- **Hyperparameter analysis identifies reproducible operating ranges** (Sec. 5.3): k=10–25 generations, middle layer (l=16), threshold δ > -6. Backbone scaling study (Table 5) confirms the method benefits from stronger LLMs (LLaMA-3-8B improves over LLaMA-2-7B by ~5% F1).

## Weaknesses

### Fatal
None.

### Major

- **No variance or significance reporting for any result.** All metrics are reported as point estimates. The analysis experiments deliberately sample only 500 questions (Sec. 5, line 343), which is *more* reliant on statistical stability, yet no confidence intervals or significance tests (even bootstrap) are provided. While single-run evaluation on full test sets is common in this sub-area, the paper would benefit from at least bootstrapped CIs on the 500-sample analysis experiments and key main results. This is a standard expectation for empirical NLP papers and reduces confidence that the smaller gains (e.g., 0.6% F1 on IIRC) are reliable.

- **No discussion of computational cost.** The method requires generating k=20 completions and extracting hidden states for every retrieval decision and re-ranking step. While the paper mentions vLLM for parallel inference (line 300), it provides no analysis of wall-clock time, FLOP overhead, or cost relative to baselines. This is a significant omission—practitioners cannot assess the practical trade-off without this information, especially since some baselines (CoT, IRCoT) require only a single forward pass per step.

- **The validation of the central selection mechanism is indirect.** The paper shows that (a) the full system outperforms baselines, (b) removing each component hurts, and (c) the Gram-determinant estimator outperforms 6 alternatives. However, there is no direct analysis of whether the specific *selection rule* (choosing the knowledge snippet with lowest Gram-determinant uncertainty) actually picks the correct supporting fact more often than alternatives (e.g., the top-ranked snippet by BM25). For the reasoning component, there is no analysis of whether the chosen reasoning strategy yields the correct answer more often. A direct per-decision analysis—tracking selection accuracy against ground-truth supporting facts—would close this gap. As presented, the evidence that the mechanism itself is responsible for the gains is circumstantial.

### Minor

- **FLARE is re-implemented with the IRCoT strategy for complex QA** (line 288–289). The original FLARE does not support multi-hop reasoning, and the paper's adaptation is a nontrivial modification. The paper acknowledges this but does not discuss whether the re-implementation is faithful to FLARE's spirit. This is a minor concern since the primary comparisons are with methods designed for complex QA (IRCoT, DRAGIN, Self-RAG), and the FLARE comparison is supplementary.

- **The case study (Sec. 5.4) is illustrative but thin.** It shows one example from HotpotQA where SeaKR retrieved the correct knowledge. It does not demonstrate that the chosen snippet was *necessary* for the correct answer, or that the first-ranked snippet would have led to an error. A quantitative breakdown across multiple examples would strengthen the qualitative support.

### Trivial
None.

## Nice-to-Haves

- A direct analysis of the self-aware selection criterion: tracking how often the Gram-determinant-chosen snippet is the gold supporting fact vs. the top-ranked BM25 snippet.
- A brief discussion of inference cost (relative wall-clock time or number of LLM calls per question) to help readers evaluate practical viability.
- The "first" claim in the abstract/introduction ("SeaKR is the first to leverage self-awareness from the internal states of LLMs") could be softened slightly—INSIDE already used internal-state uncertainty for hallucination detection—though the paper's specific combination for adaptive RAG is genuinely novel.

## Removed Points

These points were flagged for removal, treated with caution:

- **"The paper's central claim is supported only indirectly"** from the harsh critic — This was rephrased and retained as a Major weakness but the original framing ("only indirectly") overstates. The paper *does* provide substantial indirect evidence: ablation, comparison of 6 uncertainty estimators, full-system wins over baselines, and a case study. The criticism is real (direct selection accuracy analysis would be stronger) but the paper is not *only* indirect.

- **"FLARE re-implementation may not be faithful to the original method's spirit"** — This was retained as a Minor weakness but softened. The paper acknowledged the modification, and the main comparisons are with other methods designed for complex QA.

- **"The hyper-parameter analysis uses a held-out sample from NQ training, then applies the same δ across datasets... not ideal"** — This is standard practice for tuning-free methods; cross-dataset fixed thresholds are common in the literature. Removed as overly nitpicky.

- **Generic strengths from the Strength Finder about "important problem" and "well-written"** — Removed as they lack specific anchors in paper content.

- **Strength Finder strength about "tuning-free generalization" vs. Self-RAG** — Retained and rephrased under Strengths, as it's specifically supported by the F1 numbers mentioned in the text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add confidence intervals (bootstrapped 95% CI) to the main results, especially for the 500-sample analysis experiments where sampling noise is a real concern.
2. Add a direct validation experiment: on a sample of retrieval steps, track whether the snippet selected by the Gram-determinant criterion is the gold supporting fact more often than the top-ranked BM25 snippet or random selection.
3. Report approximate inference cost: wall-clock time per question or relative FLOP overhead compared to baselines.
4. Expand the case study to show quantitative patterns across multiple examples (e.g., what fraction of the time does each reasoning strategy get selected, and is that the better strategy?).

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| TARG (bMDdjg75NS) | 4.00 | R1 | Weaker: simple-QA-only, output-level signals, less comprehensive evaluation |
| ConfRAG (1OLTJL1wHG) | 3.00 | R1 | Weaker: requires fine-tuning, largely incremental |
| UnSAF (ohedxNATR9) | 4.00 | R1 | Different paper type (evaluation framework, not method); hard direct comparison |
| Interact-RAG (yHUjWb6eMe) | 5.50 | R2 | Comparable: similar contribution level and thoroughness; Interact-RAG has broader benchmark coverage but SeaKR has cleaner ablation and more principled signal |
| SelfReflect (hOErnDsehG) | 5.50 | R2 | Different paper type (uncertainty metric); comparable rigor |
| FrugalRAG (uQKtwdJN0o) | 5.00 | R2 | Comparable domain but more technical issues (reward inconsistencies, missing ablations) |
| Uncertainty as Feature Gaps (OWvvdl27CE) | 6.00 | R2 | Different paper type (UQ theory); SeaKR comparable in rigor to this anchor |
| Q-RAG (MS9nWFY7LG) | 6.00 | R2 | Different methodology (RL for embedding); comparable evaluation thoroughness |

SeaKR is a well-designed adaptive RAG method with a coherent, principled approach. Its key weaknesses (no variance reporting, no cost analysis, indirect mechanism validation) are real but not fatal—they are addressable in revision and are typical of accepted papers at venues comparable to the anchors surveyed. The paper's contributions—particularly the unification of retrieval triggering, knowledge selection, and reasoning under a single internal-state signal, and the finding that adaptive knowledge integration matters more than adaptive retrieval timing—are novel and well-supported by the experiments presented.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>