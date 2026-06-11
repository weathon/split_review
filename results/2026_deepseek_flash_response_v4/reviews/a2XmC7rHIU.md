## Summary

The paper presents the Open Proof Corpus (OPC), a human-validated dataset of 5,062 LLM-generated proofs across 1,010 competition-level mathematics problems (IMO, USAMO, Putnam, etc.), graded by 13 expert judges (former IMO participants) with 90.4% inter-annotator agreement. Using the OPC, the paper answers three open questions: (1) informal proof generation solves roughly 4× more problems than formal proof generation on the same benchmark, (2) final-answer accuracy is a poor proxy for proof correctness (e.g., o3 drops ~30% when proof correctness is required), and (3) ranking-based best-of-n selection significantly outperforms simpler selection methods. The paper also fine-tunes an open 8B judge model (OPC-R1-8B) that reaches 88.1% accuracy, matching Gemini-2.5-Pro.

## Strengths

1. **Scale and quality of human annotation**: 5,062 human-evaluated proofs across 1,010 problems, graded by 13 expert former-IMO judges with 90.4% inter-annotator agreement. This is a genuine step change relative to prior work (Petrov et al. 2025: 6 problems; Mahdavi et al. 2025: <5% accuracy ceiling). The double-grading protocol, pilot phase, coordinator oversight, and abstention option (lines 113–131) together produce unusually high-quality labels for this difficult task.

2. **Controlled best-of-n experimental design**: The best-of-n evaluation (Fig. 6a) uses 60 problems where all 8 generations have independent human judgments, avoiding circular evaluation (same LLM selecting and evaluating). This cleanly supports the non-obvious finding that ranking-based methods (Rank/Swiss) continue improving beyond n=5 while simpler methods plateau (lines 316–320).

3. **Empirical contamination diagnostic for judging**: Table 4 provides ground-truth solutions alongside proofs to be judged and measures accuracy changes. The shifts are small and non-significant (GPT-5: 89.3%→89.0%, Δ = -0.3), providing a well-designed empirical check that most dataset papers omit.

4. **Systematic documentation of the self-evaluation deficit**: Table 3 shows across four models that each performs worst when judging its own proofs (e.g., Gemini judges Gemini at 79.4% vs. Gemini judges o4 at 87.1%). This is a specific, quantified finding about a practical limitation of LLM self-assessment that goes beyond aggregate accuracy reporting.

5. **Validation that LLM-issued summaries did not bias judges**: The paper compares agreement rates between O4-MINI and human graders before and after introducing O4-MINI-generated issue summaries, finding no significant difference (lines 115–116). This methodological check addresses a plausible confound in the annotation pipeline that comparable efforts rarely evaluate.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Human baseline measured on a different sample than LLM evaluations**: The human baseline of 90.4% (Table 2) is inter-annotator agreement on the ~500 double-graded proofs, while LLM judging accuracy is measured on a separate 293-proof test set. The paper's defense — "test samples are uniformly drawn from the OPC" (line 246) — is reasonable, and the double-graded set is described as a consistency-monitoring mechanism, not a biased sample. However, the headline claim that GPT-5 is "on-par with human performance" would be more rigorous if humans were evaluated on the exact same test set. The concern is modest (both sets come from the same distribution), but it should be either addressed or explicitly caveated.

2. **OPC-R1-8B evaluation partially confounded by train-test distribution overlap**: The paper acknowledges that OPC-R1-8B's training set shares the same distribution as its test set, which may inflate its reported 88.1% accuracy (line 248). The paper refers to §C (stripped appendix) for OOD analysis showing the improvement persists. Since the paper is transparent about this and claims the issue is addressed, this is a limitation rather than a flaw, but the headline comparison with Gemini-2.5-Pro would benefit from presenting the OOD results more prominently.

3. **MathArena proof correctness is conditional, and the presentation could be clearer**: The paper reports proof correctness on the MathArena subset using only solutions with correct final answers, retrying generation if necessary (line 103). This means the "Pcorrect proof" in Fig. 5 is conditional on having a correct final answer. The methodology states this clearly, and the finding — that proof quality varies across models even when all get the right answer — is valid. However, the figure could be more explicit about the conditional nature, and the retrying strategy means the conditional rate may be higher than under single-attempt settings.

4. **Statistical power of the LLM-summary bias check not reported**: The paper reports "no significant difference in agreement" before and after introducing O4-MINI-generated issue summaries (line 115), but does not report the sample sizes or effect sizes used for this comparison. A null result with a small sample is not strong evidence of no bias.

5. **Self-evaluation analysis would benefit from column-normalized presentation**: Table 3 shows each model performs worst on its own proofs. The reviewer suggests comparing against column averages to separate self-evaluation difficulty from baseline judging difficulty. This is a reasonable suggestion for strengthening the analysis but does not invalidate the current findings.

### Trivial

1. The model name "GEMINI-PRO" appears in Table 1 and Fig. 3 while "GEMINI-2.5-PRO" is used everywhere else. These should be unified.
2. The bug in Rank (Swiss) affecting 18 questions (line 353) is mentioned in a footnote but the nature of the bug is not described.

## Nice-to-Haves

- Evaluate human judges on the exact same 293-proof test set used for LLM evaluation to ground the "human-level" claim more rigorously.
- Present the OPC-R1-8B out-of-distribution analysis in the main paper rather than deferring to the appendix.
- Add a derived quantity in Fig. 5 showing the unconditional proof correctness rate (final-answer accuracy × conditional proof correctness) for clarity.
- Report sample sizes for the bias check on LLM-generated issue summaries.

## Removed Points

Removed from the Harsh Critic's review (with justifications):

- **"Human baseline not measured on same instances" framed as critical/evidential concern**: Demoted to Minor. The paper acknowledges the difference and provides a reasonable justification (uniform sampling from OPC). The reviewer's claim that the double-graded set was "strategically selected" to be harder is speculative — the paper describes it as a monitoring mechanism, not a biased sample. The comparison is imperfect but not invalid.

- **"OPC-R1-8B evaluation confounded" framed as critical concern**: Demoted to Minor. The paper explicitly acknowledges the issue and claims to address it in the appendix. The paper is transparent about this limitation.

- **"MathArena conditional probability issue" framed as methodological gap**: Demoted to Minor. The paper clearly states its methodology in §3.1. The comparison is about the gap between two metrics, which is valid. The figure could be clearer but is not misleading.

- **Independence assumption in error rate estimation**: Removed. The reviewer acknowledges "This does not invalidate the estimate." The assumption is standard and acknowledged.

- **O4-MINI as its own best-of-n selector**: Removed. O4-MINI's self-evaluation accuracy (81.3%, from Table 3) is still reasonable, and the pass@n baseline provides a proper comparison. This is a missed analysis opportunity at most.

- **Contamination analysis ambiguity (models may already "know" solutions)**: Removed. This is a speculative alternative interpretation that does not undermine the main conclusion.

- **Short limitations section**: Removed. This is a generic suggestion; the paper lists the two most important limitations. The reviewer's own concerns are already in the weakness list.

No strengths were removed from the Strength Finder — all identified strengths are concrete, specific, and well-supported by evidence.

## Novel Insights

The calibration across reviewers reveals an interesting tension: the paper's most exciting claims (human-level judging, OPC-R1-8B matching frontier models) are slightly ahead of the evidence presented in the main paper, not because of flawed methodology but because the underlying comparisons rely on slightly different samples or distribution assumptions. This pattern is common in dataset papers where downstream experiments naturally use the same distribution. The self-evaluation deficit finding (each model performs worst on its own proofs) is genuinely insightful and less anticipated. The contamination diagnostic (providing ground-truth solutions does not improve judging accuracy) is a clever, well-executed check that the review correctly highlights.

## Suggestions

1. Run a small additional annotation effort to evaluate human judges on the exact 293-proof test set used for LLM evaluation, enabling a properly grounded comparison for the "human-level judging" claim.
2. Move the OPC-R1-8B out-of-distribution analysis from the appendix to the main paper (or at least a prominent supplementary figure) since it directly supports a headline claim.
3. Clarify in Fig. 5 that "Pcorrect proof" is conditional on a correct final answer, and optionally add the unconditional rate as a derived bar.
4. Report sample sizes and effect sizes for the LLM-summary bias check.
5. Unify model naming ("GEMINI-PRO" → "GEMINI-2.5-PRO") and briefly describe the Swiss-system bug that affected 18 questions.

## Score and Decision

**Calibration anchors used (across 2 rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Putnam-AXIOM (WrBqgoseGL.md) | 5.80 | R1 bracketing | Weaker — smaller dataset, automated evaluation only, no proof-level judgments |
| StepProof (EXaKfdsw04.md) | 3.25 | R1 bracketing | Much weaker — lacks novelty, inappropriate benchmarks |
| U-MATH (xlxGsX1pc7.md) | 5.25 | R1 bracketing | Weaker — smaller, uses LLM-as-judge, less rigorous methodology |
| Omni-MATH (yaqPf0KAlN.md) | 6.75 | R1 bracketing | Comparable — larger dataset but uses GPT-4o-as-judge vs. OPC's expert humans; OPC focuses on harder task (proofs) and shows fine-tuning utility |
| MUSTARD (8xliOUg9EW.md) | 7.33 | R2 narrowing | Stronger on methodology novelty (automated generation + formal verification) but different category |
| MathGAP (5ck9PIrTpH.md) | 7.00 | R2 narrowing | Comparable — synthetic data limitations vs. OPC's real competition problems with real human evaluation |
| LEGO-Prover (3f5PALef5B.md) | 7.50 | R2 narrowing | Stronger — more novel methodology for theorem proving |

**Round 1 bracket:** 6.0–7.5 (the paper is clearly above U-MATH/Putnam-AXIOM and below LEGO-Prover/MUSTARD).

**Round 2 narrowing:** The paper is slightly stronger than Omni-MATH (6.75) in methodological rigor (expert human judges vs. LLM-as-judge, proof evaluation vs. final-answer evaluation) and comparable to MathGAP (7.00). It is not as methodologically novel as MUSTARD (7.33) or LEGO-Prover (7.50) but makes a strong contribution as a dataset with rigorous human annotation.

**Final score:** 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>