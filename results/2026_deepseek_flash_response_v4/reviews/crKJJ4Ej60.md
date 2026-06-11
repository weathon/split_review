Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

This paper proposes **Copy-Paste**, a generation paradigm for RAG that directly embeds contextual fragments into responses to mitigate hallucinations. It instantiates this through (1) three prompting methods (CP-Order, CP-Link, CP-Refine) that generate high-copying responses, and (2) CopyPasteLLM, a DPO-trained model that internalizes the preference for context-grounded generation using only 365 training samples. The paper also introduces **Context-Parameter Copying Capturing**, a token-level probing algorithm for analyzing knowledge-source reliance. CopyPasteLLM achieves strong results on FaithEval, ConFiQA, and PubMedQA, and the mechanistic analysis reveals that the model works by suppressing parametric knowledge confidence rather than enhancing contextual representations.

## Strengths

1. **Well-motivated, intuitive idea backed by empirical evidence.** The paper grounds the copy-paste approach in a clear empirical observation: an inverse correlation between copying degree and hallucination density on RAGTruth (Section 2.2, Figure 1). This provides a principled foundation before introducing the methodology.

2. **Strong experimental results on multiple datasets, including clean held-out settings.** On ConFiQA counterfactual subsets where CopyPasteLLM was *not* trained (no <sup>T</sup> marks in Table 1), it outperforms Context-DPO (which *was* trained on ConFiQA) on several configurations. On PubMedQA (20K samples, none used for training), CopyPasteLLM improves over base models. These results provide clean evidence of generalization that is not confounded by data distribution overlap.

3. **Non-obvious mechanistic finding.** The Context-Parameter Copying Capturing analysis (Figure 4) reveals that CopyPasteLLM *suppresses parametric knowledge* rather than enhancing contextual representations — the contextual knowledge hidden states remain nearly co-distributed with the base model's, while parametric knowledge distributions shift substantially. This is a genuine insight backed by a concrete token-level probing algorithm extending beyond short-answer analysis in prior work (KTC).

4. **Systematic design space exploration.** The three prompting variants (CP-Order, CP-Link, CP-Refine) are independently evaluated across faithfulness, hallucination, and fluency metrics (Table 2), showing distinct trade-offs: CP-Order leads on faithfulness, CP-Refine on hallucination reduction, CP-Link on modest improvements. This gives readers a clear understanding of each design choice.

5. **Multi-dataset evaluation across counterfactual and original contexts.** The paper tests on FaithEval, ConFiQA (three subsets), PubMedQA, and RAGTruth, measuring both accuracy under counterfactual contexts (Table 1) and accuracy under original/faithful contexts (Table 3). Table 3 demonstrates the method does not trade off broad accuracy for adversarial robustness — CopyPasteLLM improves over base models in non-counterfactual settings too (e.g., +20.67% on ConFiQA-MR for Mistral-7B).

## Weaknesses

### Fatal

None.

### Major

1. **FaithEval evaluation is partially confounded by training distribution overlap.** The paper states (line 109): "We removed 241 samples used for training CopyPasteLLM from FaithEval, with the remaining samples used for testing." This means ~66% of CopyPasteLLM's 365 training samples are drawn from FaithEval. The baselines in Table 1 (Context-DPO, Canoe, ParamMute) were trained on entirely different data distributions. Consequently, the headline 12.2%–24.5% improvement on FaithEval — featured in the abstract, introduction, and conclusion — reflects not only method quality but also in-distribution advantage. The ConFiQA results are methodologically clean and partially mitigate this concern, but the most prominently advertised numbers should be interpreted with caution.

2. **No extractive-only baseline.** The paper's thesis is that copying directly from context improves faithfulness, yet Table 2 compares only against generation-with-attribution baselines (Attributed, Citations). A pure extractive baseline (sentence selection + reordering without any generative model) would establish the value added by the prompting methods and DPO training beyond what trivial extraction achieves. Without this, it is difficult to separate the contribution of the DPO training from that of the prompting methods.

### Minor

1. **The Context-Parameter Copying Capturing algorithm uses surface-form matching rather than causal attribution.** Tokens are classified as "contextual knowledge" if they appear in the provided context, and "parametric knowledge" if preferred in a context-free run. For a model explicitly trained to copy context tokens, this conflates lexical overlap with genuine knowledge-source reliance — a token could be generated from parametric knowledge while coincidentally matching the context. The analysis in Figures 3-4 is suggestive but not definitive. A cleaner approach (e.g., activation patching, logit lens) would strengthen the mechanistic claims.

2. **The hallucination metrics (Twist, Causal) are not defined in the main text.** Table 2 reports these values (in the 1400–1600 range) without specifying what they measure. The paper says they diagnose "two major hallucination modes" (line 83), but readers cannot interpret whether higher or lower values are better, or what these scores represent. The appendix presumably contains details, but the main text should be self-contained on this point.

3. **The copy detection algorithm may flag spurious overlaps.** The "answer w/o context" baseline in Figure 1 has κ=0.44, which is surprisingly high for a method that should produce minimal lexical overlap with the context. This suggests the algorithm (described in Appendix I) may capture common function words or other coincidental overlaps, inflating apparent copying degrees for all methods. This does not invalidate the results but makes the κ/δ thresholds in the filtering pipeline harder to interpret.

### Trivial

None.

## Nice-to-Haves

- An extractive-only baseline for Tables 2 and 3 would sharpen the attribution of improvement to the DPO training vs. the prompting methods.
- Error analysis or failure cases (e.g., where copy-heavy responses are incoherent, miss the query point, or reproduce irrelevant context) would improve practical understanding.
- A corrected FaithEval evaluation where CopyPasteLLM is trained without any FaithEval samples (or baselines are also fine-tuned on the same 241 FaithEval samples) would clean up the headline claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that the "answer w/o context" baseline having κ=0.44 suggests the copy detection algorithm is fundamentally broken.** While the elevated baseline is worth noting, the paper's comparisons are across methods using the *same* detection algorithm, so any systematic bias affects all methods equally. This is a minor methodological observation, not a structural flaw.
- **Harsh Critic's claim that Stage 1 evaluation is "partially tautological."** The purpose of the prompting methods is explicitly to maximize faithfulness by copying from context. Evaluating them with faithfulness metrics is not tautological — it is measuring whether they achieve their stated goal. The correlation between copying and faithfulness metrics is by design, not a circularity. The *absence* of an extractive baseline (addressed above) is the real gap.
- **Harsh Critic's claim about the "365 samples" understating computational cost.** The pipeline's complexity is a design choice, not a flaw. The paper is transparent about the pipeline (Section 3.2). The "365 training samples" refers to query-context pairs, which is the standard way to measure training data size.
- **Harsh Critic's criticism about FaithEval training split being "insufficiently documented in the main paper."** The paper references Appendix Table 4 for details. Appendix sections are standard for such documentation and cannot be verified as absent since they are stripped by the parser.
- **Several claims from the Harsh Critic that the paper should address problems outside its stated scope** (e.g., demanding a "cleaner approach" using activation patching without acknowledging the paper's stated goal of a first-approximation method). These have been demoted to minor weaknesses where applicable.

## Novel Insights

The most interesting observation from the reviews is the contrast between the mechanistic finding (parametric knowledge suppression, not contextual knowledge enhancement) and what one might naively expect — namely, that training to copy from context would strengthen context-processing circuitry. The paper's UMAP analysis (Figure 4) showing that CopyPasteLLM's contextual representations are nearly identical to the base model's, while parametric representations shift substantially, is a genuinely non-obvious result. This finding suggests that contextual faithfulness failures in LLMs may stem less from *inability to process context* and more from *overconfidence in parametric priors*, which has implications for how future faithfulness methods should be designed. That said, as noted in the weaknesses, this result depends on the validity of the surface-form matching approach used to separate "contextual" from "parametric" tokens, so the finding should be interpreted as suggestive rather than definitive.

## Suggestions

1. **Correct the FaithEval comparison.** Either (a) train CopyPasteLLM on a dataset that excludes FaithEval entirely and report zero-shot FaithEval results, or (b) fine-tune the strongest baselines (Context-DPO, Canoe) on the same 241 FaithEval samples to enable a fair comparison. Option (a) is cleaner. If neither is feasible, clearly state the limitation and de-emphasize FaithEval in the headline claims.

2. **Add an extractive-only baseline** (sentence selection + reordering without generation) to Tables 2 and 3 to quantify the value added by the generative components.

3. **Clarify the Twist and Causal hallucination metrics** in the main text — what they measure, how they are computed, and whether higher or lower values indicate better performance (currently, the 1400–1600 range is presented without interpretation).

4. **Strengthen the mechanistic analysis** by supplementing the surface-form matching with a control: show that the "contextual knowledge" tokens truly depend on context-processing mechanisms (e.g., by ablating context-related attention heads and checking whether these tokens' probabilities drop).

## Score and Decision

**Calibration results (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| EDU-RAG (`a2rSx6t4EV`) | 2.33 | R1 Low | Much weaker — simple RAG benchmark paper with limited novelty |
| Reward-RAG (`oqRe1KvD17`) | 3.00 | R1 Low | Much weaker — simple RAG pipeline paper |
| Factuality Enhancement (`asGQQc7gNo`) | 6.67 | R1 Mid | Comparable — both address context-faithfulness; Copy-Paste has method contribution, FaithEval overlap is a concern |
| BALCONI (`hPk92D2GJV`) | 5.25 | R1 Mid | Somewhat weaker — unsurprising findings, missing baselines; Copy-Paste has stronger methodology |
| Faithfulness CoT (`1OyE9IK0kx`) | 5.00 | R1 Mid | Somewhat weaker — analysis paper on CoT faithfulness |
| SCOPE (`dTkqaCKLPp`) | 5.80 | R1 Mid/R2 Weak | Weaker — Copy-Paste has broader evaluation, mechanistic analysis, and cleaner experimental design |
| Mask-DPO (`d2H1oTNITn`) | 6.40 | R2 Strong | Slightly stronger — cleaner evaluation (no distribution overlap), but Copy-Paste has more novel paradigm and mechanistic analysis |
| Fine-Tuning for Factuality (`WPZ2yPag4K`) | 5.75 | R2 Weak | Weaker — small test sets, limited novelty; Copy-Paste has broader evaluation |
| 3D-Properties DPO (`9Hxdixed7p`) | 6.25 | R2 Mid | Different focus (DPO analysis), comparable quality |
| Non-Adversarial Reproduction (`590yfqz1LE`) | 6.75 | R2 Mid | Different focus (memorization), similar quality |
| True Counterfactual Generation (`TUC0ZT2zIQ`) | 6.50 | R2 Mid | Different focus (counterfactual generation), similar quality |
| Backtracking Safety (`Bo62NeU6VF`) | 8.00 | R1 High | Stronger — top-tier submission on safety |
| Synthetic Continued Pretraining (`07yvxWDSla`) | 8.00 | R1 High | Stronger — top-tier submission on data augmentation |

**Round 1 bracket:** The paper clearly sits above the weak band (2–3) and below the strong band (8). Initial plausible range: 5.0–7.0.

**Round 2 narrowing:** The paper is stronger than SCOPE (5.80) and Fine-Tuning for Factuality (5.75), and comparable to but slightly below Mask-DPO (6.40) due to the FaithEval distribution overlap concern. The core contribution (copy-paste paradigm + mechanistic analysis) is solid, and the ConFiQA results provide independent support. Score: **6.0**.

**Decision:** Accept. The paper proposes a well-motivated paradigm, supports it with experiments across multiple datasets (including clean held-out evaluations on ConFiQA and PubMedQA), and provides an interesting mechanistic analysis. The FaithEval comparison issue is significant enough to temper the headline claims but does not invalidate the core contribution, which is independently supported by other experiments. The weaknesses are addressable in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>