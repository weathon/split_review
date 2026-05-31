## Summary
The paper introduces the Open Proof Corpus (OPC), a dataset of 5,062 human-evaluated LLM-generated mathematical proofs across 1,010 problems from prestigious competitions such as the USAMO, IMO, and Putnam. Using 13 expert judges (former IMO participants) with a rigorous annotation pipeline, the authors address three open questions: the gap between natural language and formal proof generation, the relationship between final-answer accuracy and proof correctness, and the effectiveness of best-of-n selection strategies. They also fine-tune an 8B-parameter model on the OPC that matches GEMINI-2.5-PRO in judging proof correctness.

## Strengths

- **Genuine gap-filling dataset**: The OPC is the first large-scale, open-source dataset of human-evaluated LLM-generated proofs from top-tier competitions. The 90.4% inter-annotator agreement with IMO-level judges, a pilot phase, and double-grading ~10% of proofs validate data quality rigorously.

- **Empirically surprising findings with clear implications**: The O3 result is particularly striking — O3 achieves 87.6% final-answer accuracy but only 59.5% proof correctness, a ~28-point gap, while GEMINI-2.5-PRO loses only ~7 points. This directly challenges the assumption that strong final-answer performance reflects proof-generation capability, and the quantification is novel.

- **Strong informal vs. formal gap**: GEMINI-2.5-PRO achieves 82.7% on PutnamBench (natural language) versus GOEDEL-PROVER-V2's <19% (formal), a 4× gap. This is a well-controlled comparison and the magnitude is informative for the field.

- **Pairwise ranking finding in best-of-n**: The result that pairwise ranking strategies (especially Swiss tournament with Bradley-Terry) continue to scale with n while discrete/continuous methods plateau is actionable and not merely incremental — it offers a practical recipe for improving proof quality without new training.

- **Open-source fine-tuned model**: OPC-R1-8B, an 8B model fine-tuned with GRPO on the OPC, matches GEMINI-2.5-PRO at majority voting (88.1%) for proof judgement. Providing this to the community alongside the dataset adds practical value beyond the dataset itself.

- **Contamination analysis**: The authors treat contamination seriously, including a worst-case experiment showing that providing ground-truth solutions to judge models results in only small, non-significant accuracy changes, supporting the robustness of the judging evaluation.

## Weaknesses

### Fatal
None.

### Major
- **Small best-of-n evaluation set**: The core best-of-n analysis with all 8 proofs human-evaluated is conducted on only 60 problems. The larger confirmation uses 134 problems (minus 18 excluded due to a bug), and the authors themselves acknowledge "relatively large confidence intervals." The conclusion that pairwise ranking "continues to scale" while others plateau is visually appealing in Figure 6(a) but rests on a very small empirical base. An error bar analysis on the scaling curves would strengthen this claim considerably.

- **Swiss ranking bug**: A footnote reveals a "small bug in the Rank (Swiss) method caused incorrect selections for 18 questions," which are simply excluded. This is concerning because the exclusions may be non-random — if the bug triggered in harder or easier cases, this biases the reported accuracy for Rank (Swiss). The authors provide no analysis of whether excluded problems are representative, leaving a potential confound in their most novel best-of-n result.

- **Training/test distribution overlap for OPC-R1-8B**: The fine-tuned model is trained on the generic subset and tested on a held-out split of the same generic subset. The authors note this limitation and report out-of-distribution results in an appendix, but the main Table 2 is the headline result and is presented with the headline claim. Without surfacing the OOD numbers in the main text, the comparison to frontier models may be overstated for readers who do not read the appendix.

### Minor
- **Adaptive problem selection introduces potential dataset bias**: Problem selection was dynamically adjusted based on observed model accuracy (e.g., adding harder IMO problems when models scored ~65% on national-level problems). While this keeps the dataset balanced in terms of correctness rate, it also means the dataset is specifically tailored to current frontier model capabilities, which limits generalizability and may introduce implicit difficulty stratification.

- **Informal advantage from final-answer injection**: For PutnamBench comparison, informal models received the final answer appended to the problem statement "to mirror the setup for formal models." This design choice is not fully justified — formal models may or may not receive equivalent information — and could inflate the informal advantage. A sensitivity analysis without answer injection would help.

- **Uncertainty acknowledgment finding is underanalyzed**: The observation that models almost never acknowledge inability to solve a problem (only 114/1700+ incorrect proofs do so, nearly all from o3) is an interesting behavioral finding, but it receives only a brief paragraph without analysis of whether this varies by problem difficulty, domain, or has implications for calibration.

### Trivial
- The footnote about the Swiss bug would be better served with a direct explanation in the main text alongside confidence intervals rather than appearing only in a footnote.

## Nice-to-Haves
- Error bars or confidence intervals on the scaling curves in Figure 6(a) would help readers interpret whether the plateau of discrete/continuous methods and the continued scaling of ranking methods are statistically robust at each value of n.
- An ablation on the GRPO training set size for OPC-R1-8B would clarify how much of the gain comes from dataset quality versus quantity.
- Including GPT-5 and GROK-4 as provers, even on a smaller held-out subset evaluated after dataset construction, would complete the picture for the strongest frontier models.

## Novel Insights
The most genuinely novel insight is the model-specific dissociation between final-answer accuracy and proof correctness: O3's 28-point gap versus GEMINI-2.5-PRO's 7-point gap suggests these models have structurally different failure modes — O3 may rely more heavily on "guess-and-check" heuristics that arrive at correct answers through flawed reasoning, while GEMINI's answers more faithfully reflect proof-level understanding. Paired with the self-evaluation finding (most models are worse at judging their own outputs than others'), this paints a coherent picture: models that produce confident but structurally unsound proofs also fail to detect their own errors. This has implications beyond proof generation for any domain requiring chain-of-thought faithfulness.

## Suggestions
- Provide an analysis of the 18 excluded Swiss ranking problems to show they do not differ systematically from included ones (e.g., compare difficulty distributions or model correctness rates).
- Report OOD judgment accuracy for OPC-R1-8B in the main text alongside the in-distribution numbers in Table 2.
- Add a comparison of informal performance without the final-answer hint on PutnamBench to quantify how much the injection contributes to the informal advantage.
- Expand the self-evaluation analysis (Table 3) with statistical tests or a more systematic breakdown by problem difficulty to understand when self-evaluation fails most severely.

## Score and Decision
This is a solid dataset and empirical study paper. The OPC fills a genuine need in the field, the annotation methodology is commendable, and the key empirical findings — particularly the model-specific proof-vs-answer gap and the scaling behavior of pairwise ranking — are meaningful contributions. The weaknesses are real (small best-of-n set, Swiss ranking bug, training/test overlap for the fine-tuned model) but do not invalidate the core contributions. The dataset alone, if released and adopted by the community, provides lasting value.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>