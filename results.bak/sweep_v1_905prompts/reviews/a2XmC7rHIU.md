Now I have a solid calibration. Let me organize my final review.

The paper is a dataset + analysis paper. Key anchors: MUSTARD (7.33, Accept), MathGAP (7.00, Accept), Omni-MATH (6.75, Accept), MathCheck (6.25, Accept). The paper under review is comparable to or slightly stronger than these — it has genuine expensive human evaluation (not synthetic), multiple novel empirical findings, a fine-tuning demonstration, and open-source release. Score: 7.0, Decision: Accept.

---

## Summary

This paper introduces the Open Proof Corpus (OPC), a dataset of 5,062 human-evaluated LLM-generated proofs across 1,010 competition-level problems (IMO, USAMO, Putnam, etc.), annotated by 13 expert judges (former IMO participants). The paper uses this dataset to answer three open questions about LLM proof generation: (1) quantifying the gap between informal and formal proof generation (≈4×, informal leads on PutnamBench), (2) measuring the discrepancy between final-answer accuracy and full proof correctness (especially large for o3: 87.6% → 59.5%), and (3) evaluating best-of-n selection strategies (ranking methods significantly outperform discrete/continuous scoring). It also fine-tunes an 8B model (OPC-R1-8B) on the OPC to 88.1% judging accuracy, matching Gemini-2.5-Pro.

## Strengths

- **Large-scale, high-quality human annotation of LLM proofs.** The OPC contains 5,062 proofs labeled by 13 expert judges, with ~10% double-graded (90.4% agreement). The methodology is rigorous: pilot phase, explicit grading guidelines, LLM-issue summaries verified as unbiased, and a coordinator resolving disagreements. This is the first dataset at this scale pairing LLM-generated proofs with human correctness labels.

- **Concrete resolution of three open questions.** The paper provides clear empirical answers on (i) the informal-formal proof gap (Gemini-2.5-Pro at 82.7% vs. Goedel-Prover-V2 at <19% on PutnamBench), (ii) the gap between final-answer and proof correctness (o3 drops 28 percentage points, Gemini-Pro drops only 7), and (iii) the effectiveness of ranking-based best-of-n strategies (improving from 22.7% pass@1 to 40.0% with Rank Swiss). These findings are novel, timely, and directly actionable.

- **Fine-tuned model demonstrates dataset utility.** OPC-R1-8B reaches 88.1% judgment accuracy (maj@5), matching Gemini-2.5-Pro and outperforming its base model by 17 points. This directly validates the dataset's value for training and provides a concrete open-source artifact for the community.

- **Thorough contamination analysis.** The paper provides a worst-case experiment (providing ground-truth solutions alongside proofs) showing small, non-significant accuracy changes (max Δ = +4.7% for the weakest base model). For the judging task, this is a strong argument that performance is not driven by solution memorization.

- **Self-evaluation bias finding.** Table 3 shows that all models except Qwen3-235B-A22B perform worse when judging their own proofs (e.g., o3 drops from 83–91% to 76.9%). This is a specific, actionable insight for practitioners.

- **Open-source release.** The dataset, code, and fine-tuned model are publicly released, enabling reproducibility and downstream use.

## Weaknesses

### Major

None. No issue fundamentally threatens the paper's core claims.

### Minor

- **The "human baseline" presentation conflates inter-annotator agreement with accuracy.** The paper reports 90.4% (inter-annotator agreement) as the "human" row in Table 2 and states GPT-5 is "on-par with human performance." Inter-annotator agreement is a quality metric for the annotation process, not a directly measured human accuracy on the judging task. The derived 5% per-judge error rate is a reasonable estimate under standard independence assumptions, but the presentation implies a precision that the measurement does not support. The paper's core comparisons between models are unaffected, but the "human-level" claim should be softened or re-framed as "approaching human inter-annotator agreement."

- **Best-of-n analysis on a modest sample.** The detailed head-to-head comparison (Figure 6a) uses only 60 problems where all 8 generations were human-evaluated. The larger sample (134 problems, Figure 6b) is better but still modest. The paper acknowledges the wide confidence intervals and argues that paired comparisons make relative differences significant. The findings are suggestive and internally consistent, but the small N limits the precision of the quantitative claims.

- **Fine-tuned model evaluation shares distribution with training data.** The paper transparently acknowledges this and references an OOD experiment in §C (stripped in this excerpt). Without seeing §C, the extent of the mitigation cannot be fully evaluated. The main results (Table 2) are based on the in-distribution test set, so the comparison of OPC-R1-8B to other models is not exactly apples-to-apples. The OOD persistence claim would need to be verified from the appendix.

- **Formal vs. informal comparison could be more nuanced.** The paper compares the best informal model (Gemini-2.5-Pro) against the best *non-agentic* formal model (Goedel-Prover-V2) on PutnamBench. The recently reported agentic Seed-Prover (50%) is noted but excluded from the headline comparison because it uses "agentic techniques." This framing is defensible but the "4×" gap in the abstract and Figure 1(b) would be smaller if Seed-Prover were included, and the paper does not clearly justify why agentic techniques are a meaningful exclusion axis for this particular comparison.

### Trivial

- The paper says "the relative performance differences significant" (end of §5.5) — missing "are" before "significant."
- A bug in the Rank (Swiss) implementation excluded 18 questions from the larger subset analysis; this is disclosed but suggests the implementation may need careful review.

## Nice-to-Haves

- A larger best-of-n evaluation (e.g., n=16 or n=32) would strengthen the scaling claims for ranking methods.
- Qualitative error categorization (mentioned as §E, stripped) would enrich the paper; including it in the main text would be beneficial.
- A brief discussion of why o3 exhibits a much larger final-answer-to-proof gap than Gemini-Pro would be a useful addition.

## Removed Points

These points were flagged by reviewers but do not survive cross-verification:

- *"The formal vs. informal comparison is misleading because formal proof is harder"* — The paper is comparing approaches on the same benchmark; that formal proofs are harder *is* the finding. The comparison is valid and the paper acknowledges Seed-Prover.
- *"The LLM issue summaries may bias judges"* — The paper explicitly tests this (no significant agreement change before/after introduction) and mitigates by omitting summaries in best-of-n experiments.
- *"The best-of-n methods should control for compute/cost"* — The paper reports the complexity (O(n) vs O(n²)) and the cost is inherent to the methods being compared; this is not a flaw in the analysis.
- *"Missing discussion of why models fail to acknowledge uncertainty"* — The paper reports the finding as a striking observation; deeper analysis would be nice-to-have but is not missing given the paper's scope.
- *"Reproducibility concerns about undisclosed hyperparameters/training details"* — The paper provides prompts (§I) and methodology details. The appendix stripping is a parser issue, not an author omission.
- *"The dataset is limited to high-school problems"* — The paper explicitly discusses this in §6 (Limitations).

## Novel Insights

The most interesting finding goes beyond the paper's own framing: the discovery that ranking-based best-of-n methods (pairwise comparisons) continue to scale with n while discrete/continuous methods plateau suggests that LLMs are better at *relative* judgment (which proof is more correct?) than at *absolute* judgment (is this proof correct?). This is a structurally different failure mode — the models have useful discriminative information about proof quality even when their absolute scoring is unreliable — and it has direct practical implications for how to deploy LLMs as proof selectors. The self-evaluation bias finding (Table 3) reinforces this: models are asymmetric evaluators, better at spotting flaws in others' work than in their own.

## Suggestions

1. Reframe the human baseline: present the 90.4% as inter-annotator agreement with the derived 5% per-judge error rate, and avoid claiming "human-level" accuracy without explicitly noting the proxy nature of this measurement.
2. Include the OOD results from §C in the main text to strengthen the fine-tuned model evaluation.
3. More clearly justify why Seed-Prover's agentic approach is excluded from the headline informal-formal comparison, or include it with appropriate caveats.
4. Consider a follow-up study with larger n for best-of-n (e.g., n=16 or 32) to verify the scaling trend.

## Score and Decision

**Round 1 bracket:** between 5 and 8.  
**Round 2 narrowing:** anchors within that bracket include MUSTARD (7.33, Accept), MathGAP (7.00, Accept), Omni-MATH (6.75, Accept), MathCheck (6.25, Accept), Putnam-AXIOM (5.80, Reject), MathEval (4.20, Reject).  

The paper under review is clearly stronger than the rejected anchors. Compared to the accepted anchors: it has a more expensive and scarce annotation resource (expert human evaluation of proofs vs. synthetic generation or answer-only benchmarks) and provides multiple novel empirical findings from a single unified dataset. It is slightly below MUSTARD (7.33) in terms of methodological novelty but comparable in rigor; the dataset contribution is arguably more directly useful to the community. The paper is on par with MathGAP (7.00) and stronger than Omni-MATH (6.75) in terms of annotation depth and breadth of analysis. Final score: **7.0**.

All anchor papers used for calibration:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EXaKfdsw04 (StepProof) | 3.25 | 1 | Much weaker — small-scale, no human eval of LLM proofs |
| JNZ3Om6NPS (LLM Architecture Limits) | 2.00 | 1 | Unrelated/theoretical |
| E4hK8t7Fts (Math Fine-tuning) | 3.00 | 1 | Much weaker — standard fine-tuning study |
| v3DwQlyGbv (Paramanu-Ganita) | 2.33 | 1 | Much weaker — small model pretraining |
| DexGnh0EcB (MathEval) | 4.20 | 1 | Weaker — benchmark aggregation, no proof evaluation |
| WrBqgoseGL (Putnam-AXIOM) | 5.80 | 1/2 | Weaker — smaller dataset, final-answer only |
| M1CCA6UF0y (AI Math Questions) | 4.25 | 1 | Weaker — question generation, not proof evaluation |
| nDvgHIBRxQ (MathCheck) | 6.25 | 1 | Comparable — but smaller human eval component |
| UHPnqSTBPO (Trust or Escalate) | 8.00 | 1 | Stronger — provable guarantees for LLM judges |
| KIgaAqEFHW (miniCTX) | 8.00 | 1 | Stronger — formal theorem proving with context |
| GGlpykXDCa (MMQA) | 8.00 | 1 | Unrelated — multi-table QA |
| YrycTjllL0 (BigCodeBench) | 9.00 | 1 | Unrelated — code generation |
| 8xliOUg9EW (MUSTARD) | 7.33 | 2 | Slightly stronger — novel data synthesis pipeline |
| 5ck9PIrTpH (MathGAP) | 7.00 | 2 | Comparable — OOD evaluation framework |
| xLoxMvO695 (Subgoal Theorem Proving) | 6.33 | 2 | Weaker — formal theorem proving methodology |
| yaqPf0KAlN (Omni-MATH) | 6.75 | 2 | Comparable — Olympiad benchmark, answer-only |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>