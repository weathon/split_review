- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes PerPO (Perceptual Preference Optimization), a method that uses discriminative rewards (e.g., IoU for object grounding, edit distance for OCR) to construct listwise preference data, then optimizes MLLMs with a margin-weighted ranking loss. The key idea is to use the discriminative reward difference between responses as a weight in the LiPO-style listwise preference optimization loss, bridging preference optimization and empirical risk minimization. Experiments on object grounding (RefCOCO/+/g) and dense OCR show consistent gains over SFT and DPO, with thorough ablations validating the design choices.

## Strengths

- **Consistent and substantial gains on visual discrimination tasks**: Tables 1 and 2 show PerPO outperforms SFT and DPO on object grounding (e.g., RefCOCO+ with LLaVA-v1.5-7B: 68.73 vs 60.55 SFT, 63.55 DPO) and dense OCR (edit distance reduction of 14.3% on LLaVA-Next-50k-7B). These gains are the central empirical contribution and are convincingly demonstrated across two model backbones and two task families.

- **Evidence of reduced image-unconditional reward hacking**: Figure 1c compares DPO and PerPO with and without image input. PerPO shows a substantially larger performance gap when the image is present versus absent, indicating its optimization depends more on genuine visual input — a clean diagnostic for this known MLLM alignment failure mode.

- **Thorough ablation of key design choices**: Section 4.3 and Section 5 systematically ablate data margin threshold (Figure 2a), data size (Figure 2b), hyperparameter β (Figure 2c), LoRA rank/alpha (Table 3), reward margin weight γ (Figure 4a), and sample size N (Table 4). This provides strong empirical validation of each component and allows readers to assess sensitivity.

- **Positive transfer to general image understanding**: Tables 1 and 2 show PerPO also improves LLaVAW and reduces hallucination (MMHalBench, POPE), indicating that alignment on discriminative rewards does not harm — and modestly improves — broader visual cognition. This directly supports the claim of maintaining generative quality.

- **Human evaluation confirms alignment quality**: Figure 3 shows that PerPO-aligned models achieve higher win rates judged by both GPT-4o and human users across 500 sampled questions, covering accuracy, instruction adherence, and hallucination. This provides qualitative validation beyond automated metrics.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (PerPO improves visual discrimination via discriminative-reward-weighted listwise optimization) are well-supported by the experiments. The issues below are addressable in revision and do not threaten the main findings.

### Minor

- **Overclaimed theoretical framing.** The paper asserts that "the deterministic nature of discriminative rewards ensures that we can guide an optimization space **perfectly isomorphic** to the discrimination space" (line 95) and that PerPO "theoretically proves [its] capability to model both visual discrimination and language generation abilities concurrently" (lines 122–123). The derivation in Eqs. 7–8 is a rearrangement that treats a normalizing constant ${\sum_{\hat{R}_i > \hat{R}_j} (\hat{R}_i - \hat{R}_j)^\gamma}$ as constant and assumes $\gamma=1$ — the paper acknowledges this is a "simplified scenario" but does not caveat the strong subsequent conclusions. This is a framing issue, not a methodological flaw: the insight that discriminative margins naturally reweight the preference gradient is useful and well-motivated. The "isomorphic" and "proves" language should be toned down to avoid overclaiming.

- **LiPO baseline only appears in the $\gamma$ ablation, not in main results.** The paper correctly notes that $\gamma=0$ in Eq. 6 recovers LiPO (line 198), and Figure 4a compares $\gamma=0$ (LiPO) vs. $\gamma=0.5$ (PerPO) on RefCOCO+. This shows the discriminative margin weighting adds value over uniform listwise ranking. However, this comparison is absent from the main results tables (Tables 1 and 2), which compare only SFT, DPO, and PerPO. Including LiPO in the main tables would allow readers to assess the contribution of the margin weight across all benchmarks, cleanly separating the benefit of "going listwise" (DPO→LiPO) from the benefit of "adding discriminative weights" (LiPO→PerPO). The paper's central claim is about the latter, and isolating it fully would strengthen the evidence.

- **Data filtering statistics are incomplete.** The training data is filtered by requiring a minimum margin between best and worst rewards (0.8 for grounding, 0.04 for OCR), retaining 3k and 1.8k samples respectively (line 132). The paper does not report how many total samples were generated before filtering, nor the fraction discarded at each threshold. Figure 2a provides a useful ablation showing performance declines at lower margins, which partially addresses this concern, but the method's applicability to low-margin (more ambiguous) cases is not discussed. A brief statement of the filtering ratio and a note on this limitation would improve completeness.

### Trivial

- **Unverifiable "first" claims.** The introduction states "We highlight, for the first time, the capability dilemma" and proposes "the first method to align with the human perception process" (line 35). These framing claims are hard to verify and add no technical substance. They should be removed or softened.

## Nice-to-Haves

- **Comparison with MLLM-specific alignment methods on hallucination benchmarks.** The paper cites mDPO, HA-DPO, and LLaVA-RLHF in related work and reports hallucination improvements (MMHalBench, POPE) as a secondary finding. Comparing against one of these methods on hallucination metrics — even if they are not designed for visual discrimination — would situate PerPO more clearly in the MLLM alignment landscape. This is scope-adjacent rather than central to the paper's contribution.
- **Report per-task win rates and inter-annotator agreement for the human evaluation** (currently only a single overall win rate is reported).
- **Include a brief comparison of training time/memory** between PerPO and DPO, since PerPO processes all $N$ samples per instance.

## Removed Points

These points were flagged in the inputs but are removed from the main review with brief justification:

1. **Missing MLLM alignment baselines treated as a Major issue** — The harsh critic framed the absence of mDPO/HA-DPO/LLaVA-RLHF comparisons as a critical gap. These methods target hallucination reduction, which is a secondary finding in this paper; the primary contribution (visual discrimination improvement via discriminative rewards) is well-supported within its stated scope. Demanding these baselines is scope creep. Moved to Nice-to-Haves.

2. **Criticism that "the paper does not discuss computational cost relative to DPO"** — This is a valid point but belongs in Nice-to-Haves, not as a significant weakness. Moved.

3. **Criticism that "the human evaluation uses a single overall win rate"** — A reasonable suggestion for improvement but not a weakness. Moved to Nice-to-Haves.

4. **Criticism about "first to highlight" / "first method" overclaims** — While valid as an observation, this is a trivial presentation issue, not an evidential gap. Moved to Trivial.

5. **Strength Finder claim that "the theoretical bridge between PO and ERM directly supports the claim"** — This is partly accurate (the paper does connect the two) but the connection is heuristic, not a rigorous derivation. The strength is retained but implicitly qualified in the weaknesses section above. The energy from the Strength Finder on this point is softened.

## Novel Insights

None beyond the paper's own contributions. The observation that PerPO's advantage emerges only after SFT has established basic capability (Figure 4b) is an original insight in the paper itself but is not additionally surfaced by the reviewer inputs.

## Suggestions

1. **Add LiPO as a row in Tables 1 and 2** (or include a direct LiPO-vs-PerPO comparison table). This would cleanly isolate the contribution of the discriminative margin weighting from the shift from pairwise to listwise optimization.
2. **Tone down the theoretical language** — replace "perfectly isomorphic" and "proves" with "provides a perspective" or "can be interpreted as"; acknowledge the simplifying assumptions in the derivation.
3. **Report the number of samples filtered out** at each margin threshold to clarify data construction statistics, and briefly discuss the limitation that the method is applied only to sufficiently discriminable cases.
4. **Remove or soften the "first" claims** in the introduction (line 35).
