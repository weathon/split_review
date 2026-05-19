Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes SeaKR, an adaptive RAG method that extracts "self-aware uncertainty" from the internal states (hidden representations of the EOS token) of LLMs using Gram determinant consistency across multiple generations. This uncertainty signal is used for three purposes: (1) deciding when to trigger retrieval (by thresholding), (2) re-ranking retrieved knowledge pieces (selecting the one that minimizes uncertainty), and (3) choosing between two reasoning strategies (direct generation vs. comprehensive reasoning). The method is tuning-free and evaluated on both complex and simple QA benchmarks.

## Strengths

1. **Strong empirical gains on complex QA benchmarks.** Table 1 shows SeaKR outperforms all baselines by 5.5–6.0 F1 points on 2WikiMultiHop and HotpotQA (36.0 vs. 30.0 and 39.7 vs. 34.2, respectively). These margins are substantial and directly support the paper's central claim that internal-state uncertainty benefits adaptive RAG.

2. **Informative ablation study decomposes contributions.** The ablation (Table 3) shows that each of the three self-aware components contributes positively, and that the integration strategies (re-ranking and reasoning) yield larger gains than the retrieval decision itself. The comparison against alternative uncertainty estimators (perplexity, LN-Entropy, energy score, prompting) also provides concrete evidence that the Gram-determinant internal-state estimator is the best choice.

3. **Systematic hyperparameter analysis.** Figure 1 shows parameter sweeps for recall size N, Gram dimension k, layer index l, and threshold δ, with optimal ranges identified (e.g., k∈[10,25], l=16). This grounds the reported configurations empirically rather than relying on arbitrary choices.

4. **Tuning-free design generalizes across distributions.** SeaKR (which requires no training) outperforms Self-RAG (fine-tuned on GPT-4 generated NQ data) on all complex QA datasets, demonstrating that intrinsic self-awareness generalizes better than supervised adaptation when domains shift.

## Weaknesses

### Fatal
None.

### Major

1. **The core uncertainty estimator is adopted directly from prior work (INSIDE) and applied in a straightforward manner.** The paper explicitly states "we follow INSIDE" (line 237) for the Gram determinant of EOS-token hidden states. The three uses of this score — threshold-based retrieval triggering, selecting the knowledge piece with minimal uncertainty, and picking the reasoning strategy with lower uncertainty — are conceptually straightforward applications of the same signal. While combining these into a complete system is non-trivial engineering, the paper does not introduce modifications to the uncertainty estimator itself or propose fundamentally new ways of using it. The methodological novelty is thinner than the framing suggests, and the paper's positioning as "the first to leverage self-awareness from internal states" (line 46) should be tempered — previous work (e.g., INSIDE for hallucination detection, and output-probability-based adaptive methods like FLARE and DRAGIN) laid significant groundwork that makes this step natural.

### Minor

2. **No computational cost analysis despite the method's high inference overhead.** The method requires k=20 parallel generations per retrieval decision (line 299), and with N=3 candidates for re-ranking, this can multiply to 60+ generations per reasoning step. While vLLM parallel inference is mentioned, the paper does not report runtime, total LLM calls per question, or generated tokens — making it impossible to assess whether the accuracy gains justify the cost. A fair comparison with baselines that also considers efficiency (e.g., IRCoT retrieves at every step but generates only one answer per step) is missing.

3. **No confidence intervals, error bars, or significance tests on any reported results.** With k=20 generations introducing variance into the uncertainty estimates themselves, and analysis experiments using only 500 sampled questions (line 343), the reported numbers could be noisy. The lack of statistical rigor makes it impossible to assess whether small gaps (e.g., 0.3% on TriviaQA) are robust.

4. **Underspecified implementation details affecting reproducibility.** (a) The temperature for the k=20 generations is not specified, yet it is critical for ensuring diverse but not random generations. (b) The pseudo-generation token selection ("tokens ... with low probability" — line 185) does not specify thresholds or selection criteria. (c) The termination condition "So the final answer is" (line 215) is noted as fragile — its recall is not evaluated, so unanswered questions may silently hit the maximum iteration limit without analysis of how often this occurs.

5. **FLARE and DRAGIN re-implementations for complex QA are not validated against original results.** The paper adapts these methods to the complex QA setting (line 289: "We re-implement FLARE with IRCoT strategy") but does not verify that the re-implementations match or approximate the original methods' performance on their original settings. This introduces potential implementation bias that could favor the proposed method.

6. **No discussion of limitations or failure modes.** The conclusion (Section 5) does not address the computational overhead, the sensitivity to hyperparameters (δ tuned on NQ only, used across all datasets), or the fragility of the termination condition. An honest assessment of when the method might underperform or fail would strengthen the paper.

### Trivial

- None significant enough to list.

## Nice-to-Haves

- Provide an efficiency comparison (total LLM calls or generated tokens per question) to contextualize the accuracy gains.
- Validate FLARE/DRAGIN re-implementations against any available original results to rule out implementation bias.
- Analyze the sensitivity of δ across datasets with different uncertainty distributions.
- Evaluate cheaper approximations of the uncertainty (e.g., fewer generations, single-pass estimator) to explore the accuracy-efficiency trade-off.
- Report the average number of retrieval steps per dataset to quantify how "adaptive" the method is in practice.

## Removed Points

- **"DRAGIN already uses internal attention weights… diminishing the paper's novelty"** — DRAGIN uses attention weights for *query reformulation* after deciding to retrieve, not for the retrieval decision itself or for knowledge integration. The paper's claim (line 46) is about using internal states for "when to retrieve and effectively integrate knowledge," which DRAGIN does not do. Removed as the criticism conflates different uses of internal states.

- **"Self-RAG comparison is not apples-to-apples"** — The paper explicitly acknowledges this distribution shift (lines 318–321) and uses the comparison to demonstrate the benefit of tuning-free generalization. The criticism restates an acknowledged limitation rather than identifying a blind spot. Demoted.

- **"The paper overstates how much knowledge integration is neglected by prior work"** — FLARE and DRAGIN do append retrieved knowledge to context, but they do not *adaptively* select among knowledge candidates or choose between reasoning strategies. The paper's phrasing ("largely neglected") refers to these specific adaptive integration mechanisms, not to any knowledge integration at all. Removed.

- **Generic concern about δ sensitivity across datasets** — This is speculative; the paper demonstrates strong empirical results across datasets with a single δ. The concern is reasonable but unsupported by evidence in the review. Demoted to nice-to-have.

- **"The conclusion does not mention limitations"** — While true, this is a presentation issue rather than a substantive weakness. Noted above as a minor omission but not weighted significantly.

## Novel Insights

None beyond the paper's own contributions. The finding from the ablation that *integration* strategies (re-ranking and reasoning) contribute more to performance than the *retrieval decision* itself is a useful insight that somewhat reframes the paper's emphasis, but it is already stated explicitly by the authors (line 61: "dynamically integrating retrieved knowledge brings even more performance gain than self-aware retrieval").

## Suggestions

1. **Provide a cost analysis table** reporting average LLM calls and/or total generated tokens per question for SeaKR and all baselines. This would contextualize whether the accuracy gains justify the computational overhead and address the most significant practical concern about the method.

2. **Add confidence intervals** via bootstrapping or multiple runs for at least the main results (Tables 1 and 2) and the ablation study (Table 3). With k=20 generations introducing variance, this is particularly important.

3. **Specify generation temperature** and the exact token-selection criterion for pseudo-generation. These are needed for reproducibility.

4. **Tone down the novelty framing** in the introduction and related work to more accurately reflect that the core uncertainty estimator is adopted from INSIDE, and that the contribution lies in its application to three adaptive RAG components.

5. **Add a limitations paragraph** to the conclusion discussing computational cost, sensitivity to δ, and the termination condition's potential failure cases.

## Score and Decision

The paper makes a solid empirical contribution: it demonstrates convincingly that internal-state uncertainty (Gram determinant of EOS hidden states) provides a better signal for adaptive RAG than output-level alternatives, and achieves strong results on complex QA. However, the methodological novelty is incremental — the core estimator is adopted directly from prior work and applied in conceptually straightforward ways. The lack of computational cost analysis and statistical significance testing weakens the evidence. On balance, the paper has real contributions and the main results are credible, but the weaknesses prevent it from being a strong paper.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**