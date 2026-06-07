## Summary

This paper proposes **Copy-Paste**, a generation paradigm for RAG that directly reuses lexical fragments from the provided context to mitigate faithfulness hallucinations. It is instantiated through a two-stage pipeline: (1) three Copy-Paste prompting strategies (CP-Order, CP-Link, CP-Refine) generate high-copying responses, and (2) **CopyPasteLLM** internalizes a preference for contextual trust via DPO training on only 365 automatically constructed preference pairs. On FaithEval, CopyPasteLLM achieves 12.2–24.5 percentage point improvements over baselines, with a peak accuracy of 92.8%. The paper also proposes a **Context-Parameter Copying Capturing** algorithm for token-level analysis of knowledge source usage during generation.

## Strengths

- **Genuinely novel paradigm with strong empirical results**: The core idea of explicitly maximizing lexical copying from context as a faithfulness mechanism is intuitive and well-motivated. CopyPasteLLM achieves 12.2–24.5 percentage point improvements on FaithEval over strong baselines (Table 1) using only 365 query-context pairs—50× fewer than Context-DPO's 18,000 samples. These gains hold across three model families (Llama-3-8B, Mistral-7B-v0.2, Llama-3.1-8B).

- **Non-obvious mechanistic finding**: The Context-Parameter Copying Capturing analysis (Section 3.3, Figure 4) reveals via UMAP that CopyPasteLLM works by *suppressing parametric knowledge confidence* rather than enhancing contextual processing — contextual representations remain nearly co-distributed with the base model while parametric distributions shift substantially. This extends token-level analysis (KTC, Bi et al., 2024) from short answers to full CoT trajectories and provides genuine insight.

- **Dual-setting validation**: The method improves accuracy on both counterfactual settings (Table 1) and non-counterfactual settings (Table 3), with particularly strong gains on the challenging ConFiQA-MR/MC subsets (average improvement from 84.49% to 94.37%, with a 20.67% gain on Mistral-7B-v0.2 MR). This shows the method does not simply overfit to counterfactual patterns.

- **Fully automated preference construction pipeline**: The pipeline (Section 3.2) generates preference pairs from raw query-context pairs without manual annotation, using multi-criteria filtering (AlignScore, MiniCheck, embedding similarity, perplexity), an Elo-style LLM-as-Judge tournament targeting two hallucination modes (Twist and Causal), and gold-answer stamping. This addresses a practical bottleneck for DPO in faithfulness tasks.

## Weaknesses

### Major

- **Answer-stamping confound in preference construction**: During DPO data construction (Section 3.2), the paper *appends the gold answer to the top Copy-Paste candidate* and wrong answers to other candidates. This means the chosen response contains both (a) a high-copying reasoning pattern and (b) the verbatim correct answer text. The rejected response contains (c) a different generation pattern and (d) an incorrect answer. The model therefore simultaneously learns to prefer high-copying *and* learns to reproduce the specific gold answer. In counterfactual settings, the gold answer is exactly the answer consistent with the fabricated context. Without an ablation that isolates copying preference from answer supervision (e.g., comparing DPO on pairs [high-copying response] vs. [low-copying response] both *without* answer-stamping), the reported gains cannot be confidently attributed to internalized copying preference rather than direct answer memorization. This is the single most consequential unresolved issue in the paper.

- **Title/abstract overstate the scope**: The paper presents itself as mitigating "LLM hallucinations" broadly, but the primary evaluation is on *contextual faithfulness* in RAG settings — specifically, whether the model follows a provided (potentially counterfactual) context. Following incorrect context and producing factually wrong content is itself a form of hallucination under standard definitions. The paper clearly defines its scope as "contextual faithfulness hallucinations" in RAG, but the title and framing ("Mitigate Large Language Model Hallucinations") create a mismatch between what readers expect and what is actually evaluated. The contribution should be framed honestly as "improving contextual faithfulness in RAG."

### Minor

- **No variance or significance measures**: No standard deviations, confidence intervals, or multi-seed results are reported for any main result (Tables 1–3). DPO training can exhibit variability across seeds and hyperparameter choices. While single-run evaluation is common practice in this area, the absence of any uncertainty quantification makes it impossible to assess whether the reported 12–24% improvements are stable or reflect favorable runs.

- **Numerical discrepancy in reported improvement**: The paper claims a 24.5 percentage point improvement on FaithEval for Llama-3.1-8B, but Table 1 shows CopyPasteLLM at 92.6 and the best baseline (Attributed) at 65.5, yielding a difference of 27.1 points. The source of this ~2.6 point discrepancy should be clarified and corrected.

- **Hard-to-interpret hallucination metric in Table 2**: The "Twist" and "Causal" hallucination scores are reported as raw values ranging from ~1300 to ~1600 without normalization, making it impossible to assess whether a difference of, say, 1518.9 vs. 1472.5 (Table 2, Mistral) is meaningful.

- **Labeling confound in Context-Parameter Copying Capturing**: The algorithm (Section 3.3) classifies tokens that appear in the context as "contextual knowledge" and tokens preferred in a context-free run as "parametric knowledge." When a token appears in both (coincidence), it is always classified as contextual regardless of its actual generation source. This limits the precision of the mechanistic analysis but does not invalidate the main experimental results.

- **Near-ceiling results on non-counterfactual benchmarks**: On PubMedQA and ConFiQA-QA (non-counterfactual), the method achieves only 1.01% average improvement (from 96.04% to 97.05%, Table 3). These ceiling-level results provide limited evidence of added value.

### Trivial

- None beyond the numerical discrepancy noted above.

## Nice-to-Haves

- A head-to-head comparison of total computational cost (LLM calls, tokens processed) alongside the "365 samples" claim would allow fairer comparison with baselines.
- Evaluating the method on a standard factuality benchmark (e.g., Natural Questions) where context is reliable but parametric knowledge could correct gaps would clarify whether the method truly reduces hallucinations or merely increases context obedience.
- Ablations isolating the Elo tournament, multi-criteria filtering, and answer-stamping within the preference construction pipeline.

## Removed Points

These points from the inputs are flagged to be removed — treat with caution:

- **"Correlation is not causation" (§2.2)**: The inverse correlation between copying degree and hallucination is presented as motivation, not as a proven causal claim. The phrasing "suggesting" is appropriately hedged for a motivating observation in a preliminary analysis.
- **"365 training samples claim is misleading"**: The paper unambiguously compares training data quantity (365 vs 18,000 pairs), not total compute cost. The pipeline is transparently described; there is no deception.
- **"Baseline comparisons are selectively reported"**: Table 1 is clearly organized with seen/unseen markers (`<sup>T</sup>`). Comparisons across models are clearly separated. The numerical error (24.5 vs 27.1) is retained as a Minor weakness above.
- **"Section-by-Section Notes"** about missing appendix content, citation framing, and formatting: These reflect parser artifacts or scope-creep suggestions.
- **Various points about missing related work**: Not verifiable without external sources.
- **Strengths from the Strength Finder that were generic** (e.g., "addressed an important problem," "well-written"): These lack specific concrete content.

## Novel Insights

Beyond the paper's own contributions: The merged review surfaces a tension between the paper's mechanistic claims and its experimental design. The answer-stamping confound means the mechanistic analysis (Figure 4) may characterize a model trained to memorize specific answers rather than one that learned to "trust context" per se. If the gains can be replicated *without* answer-stamping, the paper's interpretation stands; if not, the core contribution reduces to "data-efficient DPO with automated preference construction" — still useful, but a substantially weaker claim. The fact that the paper evaluates almost exclusively on counterfactual benchmarks (where the correct answer is defined by the context, not by external factuality) further compounds this issue: the method could be learning "output what looks like the last answer in the context" rather than genuine contextual reasoning.

## Suggestions

1. **Ablate answer-stamping**: Run DPO on preference pairs constructed from copying behavior alone (e.g., compare CP-high-copying response vs. Base/Attributed response without appending any gold/wrong answer). Report whether the accuracy gains persist.
2. **Reframe the contribution**: Change the title and framing to precisely target "contextual faithfulness in RAG" rather than the broader "hallucination mitigation."
3. **Report variance**: Run DPO training over at least 3 seeds and report mean ± std for all main results.
4. **Correct the numerical discrepancy** for the Llama-3.1-8B FaithEval improvement (stated as 24.5, actual value appears to be 27.1).
5. **Normalize hallucination metrics** in Table 2 or provide interpretable scales.
6. **Add a factuality benchmark**: Evaluate on a dataset where context is reliable and the correct answer requires selectively applying contextual knowledge (not just copying it).

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing)**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RuY1r1PDdQ.md` | 3.00 | R1 (weak) | Weaker paper — narrower scope, poorly received |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Iyrtb9EJBp.md` | 8.00 | R1 (strong) | Stronger paper — comprehensive metric + alignment method, cleaner experimental design |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/asGQQc7gNo.md` | 6.67 | R1 (middle) | Stronger paper — cleaner analysis of context-faithfulness trade-offs, fewer confounds |

**Round 1 bracket**: 4.0–7.0

**Round 2 (Narrowing within bracket)**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/d2H1oTNITn.md` (Mask-DPO) | 6.40 | R2 | Stronger — cleaner methodology, more rigorous evaluation; similar topic area |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Pnktu2PBXD.md` (RAG-DDR) | 6.00 | R2 | Comparable — both have interesting ideas but methodological concerns; RAG-DDR is cleaner |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WPZ2yPag4K.md` (Fine-Tuning for Factuality) | 5.75 | R2 | Slightly stronger — cleaner DPO application despite limited novelty; fewer confounds |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/hPk92D2GJV.md` (BALCONI) | 5.25 | R2 | Slightly weaker — less novel contribution; copy-paste paper has a more original paradigm |

**Final score rationale**: The paper's core idea (copy-paste as a faithfulness mechanism) is genuinely novel and the empirical results on FaithEval are impressive. However, the answer-stamping confound is a significant unresolved concern that undermines attribution of the gains to copying preference per se, and the framing overreaches. Relative to the round-2 anchors, the paper is stronger than BALCONI (5.25) due to greater novelty but weaker than Mask-DPO (6.40) and RAG-DDR (6.00) whose experimental designs are cleaner. It is most comparable to the Fine-Tuning for Factuality paper (5.75) in overall quality, but with a more novel idea balanced by a more serious confound. I place it at 5.5.

### Final Score

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>