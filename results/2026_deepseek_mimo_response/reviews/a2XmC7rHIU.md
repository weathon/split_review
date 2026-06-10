Now I have enough information to write the final review. Let me compile it.

## Summary
This paper introduces the Open Proof Corpus (OPC), a dataset of 5,062 human-evaluated LLM-generated mathematical proofs across 1,010 competition problems, graded by 13 former IMO-participant judges. Using the OPC, the paper investigates three questions: the gap between formal and informal proof generation, the relationship between final-answer accuracy and proof correctness, and the effectiveness of best-of-n selection strategies. The paper also fine-tunes an 8B model (OPC-R1-8B) achieving 88.1% proof-judging accuracy.

## Strengths
- **Large-scale, high-quality dataset with expert human evaluation**: 5,062 proofs across 1,010 problems, graded by 13 former IMO participants, achieving 90.4% inter-agreement rate (corresponding to ~5% individual judge error rate) (Section 4). This substantially exceeds prior proof evaluation efforts in scale and rigor — e.g., Petrov et al. (2025) evaluated only 6 USAMO problems; Mahdavi et al. (2025) evaluated IMO Shortlist without open-sourcing data.
- **Novel per-model quantification of the proof correctness gap**: Figure 5 shows o3 drops from 87.6% final-answer accuracy to 59.5% proof correctness on MathArena (28-point drop), while GEMINI-2.5-PRO drops only from 84.9% to 77.6% (7-point drop). This model-specific decomposition of the gap has not been reported at this scale and granularity in prior work.
- **Ranking-based best-of-n methods outperform standard selection and continue to scale**: Figure 6(a) shows Rank (Swiss) achieves ~47% accuracy versus ~34–36% for discrete/continuous methods, and continues to improve with n while standard methods plateau after n=5. This is a practically useful finding for proof generation pipelines.
- **Practical downstream utility**: OPC-R1-8B (8B parameters) achieves 88.1% judgment accuracy, matching GEMINI-2.5-PRO and approaching GPT-5, demonstrating the dataset enables tangible model improvements (Table 2).

## Weaknesses

### Fatal
None

### Major
- **Asymmetric comparison inflates the "human-level judge" headline claim**: The section title ("5.2 LLMs Are Human Level Judges"), abstract, and Figure 1 all foreground the claim that GPT-5 achieves 90.8% accuracy "on-par with human performance." However, the 90.8% is majority-of-5 judgments (maj@5) while the 90.4% human baseline is the pairwise inter-annotator agreement rate (Table 2). GPT-5's actual single-pass accuracy is 89.3%, which is below the 90.4% baseline. If human judges were similarly ensembled via majority vote, their accuracy would be substantially higher — the estimated individual judge error rate is p ≈ 5%, so human maj@5 would exceed 99%. The paper does present pass@1 honestly in Table 2 and the text (line 248: "89.3% with a single evaluation pass, approaching the 90.4% human baseline"), but the most prominent framings (abstract, Figure 1 caption, section title) compare an ensemble against individuals and declare parity.

- **PutnamBench formal/informal comparison uses different test sets, and the abstract presents the 4× gap as a direct comparison**: Informal evaluation uses 114 problems (the subset with available informal final answers, per lines 103, 178), while GOEDEL-PROVER-V2's <19% accuracy is on the full PutnamBench (~498 problems). The abstract states "GEMINI-2.5-PRO solves 4 times more problems than the best formal model" (line 62), and Figure 1 caption reads "Informal solves 4× more problems in the PutnamBench." The body text in Section 5.3 is more careful ("reaches almost 83% accuracy on the evaluated subset"), but the headline claims in the abstract and figures do not flag this subset asymmetry. The 4× figure is not well-supported as a direct comparison without establishing that the 114-problem subset is representative of the full benchmark's difficulty.

### Minor
- **Double-grading selection mechanism undocumented**: The 90.4% inter-judge agreement rate — which anchors the human baseline — comes from "approximately 10% of the proofs" that were double-graded (line 131). The paper does not specify whether this sample was randomly selected or chosen through some other mechanism. The surrounding quality-monitoring context ("disagreements were reviewed by the coordinator," "if the coordinator identified a significant number of discrepancies for a specific judge, they would discuss the issue") suggests the selection may have been targeted rather than random, which could affect the representativeness of the 90.4% figure.

- **Self-evaluation penalty claim is weaker than stated for QWEN3**: The paper claims "all models except QWEN3-235B-A22B perform worse when judging their own proofs" (line 252), but Table 3 shows QWEN judging QWEN at 84.4% — the highest of all judges for QWEN proofs. This undermines the universality of the "LLMs struggle to recognize their own mistakes" claim. The effect is real but modest for the other three models (e.g., o3 drops to 76.9% vs. ~83% from others).

- **MathArena retry mechanism undocumented**: The paper retains only proofs with correct final answers, "retrying generation if necessary" (line 103), but does not report retry counts per model. If a model needed multiple attempts to produce a correct answer, the evaluated proof may not be representative of single-shot proof-generation capability.

### Trivial
None

## Nice-to-Haves
- Include confidence intervals in Tables 3 and 4 in the main text (currently deferred entirely to appendix) to help readers assess statistical significance of self-evaluation and contamination effects.
- Report key prompt design choices in the main body, given that prompt quality is emphasized as critical to judging performance (line 250: "we put considerable effort into crafting clear and comprehensible prompts").

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's concern about LLM issue summaries potentially anchoring human judges: the paper already addresses this by testing agreement before/after introduction and omitting summaries from best-of-n experiments. The proposed anchoring bias is speculative.
- Strength about "contamination robustness analysis": this is a negative result (small effects) included for completeness rather than a positive contribution; it supports the paper's other findings but is not a standalone strength.

## Novel Insights
The paper's most novel empirical contribution is the per-model quantification of the final-answer-to-proof-correctness gap (Figure 5), revealing that the gap is highly model-dependent: o3 loses ~28 percentage points while GEMINI-2.5-PRO loses only ~7 points despite similar final-answer accuracy. This finding, enabled by the OPC's MathArena subset design of first verifying final answers then evaluating proofs, has not been reported in prior work at this scale and granularity, and it directly informs model selection for applications requiring verifiable reasoning.

## Suggestions
- Reframe the "human-level judge" comparison: either compare GPT-5 pass@1 vs. individual human accuracy (~95% based on the p=5% estimate) and describe it as "approaching" human performance, or compute a human majority-vote baseline for a fair maj@5 comparison. The current 89.3% vs. 90.4% comparison is close but not "on-par."
- For PutnamBench, either report GOEDEL-PROVER-V2's accuracy on the same 114-problem subset used for informal evaluation, or add a prominent caveat in the abstract noting the different test sets.
- Document the double-grading selection process (random vs. targeted) to strengthen confidence in the 90.4% human baseline.

## Calibration Report

**Round 1 anchors (bracketing):**
| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| StepProof | 3.25 | 1 | Narrow autoformalization paper, much smaller scale. OPC is clearly stronger. |
| JNZ3Om6NPS | 2.00 | 1 | Theoretical impossibility paper. Not comparable. |
| E4hK8t7Fts | 3.00 | 1 | Fine-tuning study on MATH, limited scope. OPC is stronger. |
| v3DwQlyGbv | 2.33 | 1 | Small pre-training study. OPC is stronger. |
| WrBqgoseGL (Putnam-AXIOM) | 5.80 | 1,3 | Math benchmark, 236 problems, no human proof evaluation. OPC is clearly stronger. |
| DexGnh0EcB (MathEval) | 4.20 | 1 | Comprehensive but aggregation benchmark, no human evaluation. OPC is stronger. |
| uDZ9d4UAUh | 4.75 | 1 | Mistake-detection dataset, smaller scale. OPC is stronger. |
| ToVvoHpk4L (CLR-Bench) | 4.33 | 1 | College-level reasoning benchmark. OPC is stronger. |
| mMPMHWOdOy (WizardMath) | 8.00 | 1 | SOTA training method with impressive results. Stronger than OPC. |
| GGlpykXDCa | 8.00 | 1 | Multi-table QA benchmark. Different domain, comparable quality. |
| KIgaAqEFHW | 8.00 | 1 | Formal theorem proving with contexts. Stronger in its niche. |
| HnhNRrLPwm | 8.00 | 1 | Multimodal benchmark. Different domain. |

**Round 2 anchors (narrowing):**
| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| C25SgeXWjE | 6.25 | 2 | FOL reasoning benchmark with LLM+symbolic prover. OPC has larger scale and more impactful findings. |
| QqdloE1QH2 | 5.50 | 2 | Multilingual autoformalization dataset. OPC is stronger. |
| 71kocBuhNO (LogicBench) | 5.40 | 2 | Logical reasoning benchmark. OPC is stronger. |
| dWsdJAXjQD (ImProver) | 6.75 | 2 | Proof optimization agent. OPC has larger dataset contribution and broader findings. |
| 5ck9PIrTpH (MathGAP) | 7.00 | 2 | Synthetic proof complexity framework. OPC has real-world data and human evaluation. |
| xLoxMvO695 | 6.33 | 2 | Subgoal learning for formal proving. OPC is stronger. |
| yaqPf0KAlN (Omni-MATH) | 6.75 | 2,3 | 4,428 Olympiad problems with human annotation. OPC has stronger analyses and proof-specific utility. |
| KUNzEQMWU7 (MathVista) | 7.25 | 3 | 6,141 visual math examples, comprehensive. Similar quality benchmark paper; comparable but OPC has more novel findings. |
| u6jbcaCHqO (SciBench) | 5.60 | 3 | College-level science benchmark. OPC is stronger. |

**Round 1 bracket:** Between 5.5 and 8.0, initially between 6.0 and 7.5 after reading anchors.

**Round 2 narrowing:** Between 6.0 and 7.5. The OPC is clearly stronger than the 5.5–6.25 anchors (Putnam-AXIOM, SciBench, C25SgeXWjE) and clearly weaker than the 8.0 anchors (WizardMath). Compared to Omni-MATH (6.75) and ImProver (6.75), the OPC has a more substantial dataset, more comprehensive analyses, and demonstrated downstream utility. Compared to MathGAP (7.0) and MathVista (7.25), the OPC's two major framing issues (the asymmetric human-level comparison and the PutnamBench subset mismatch) are more consequential than the weaknesses in those papers. This places the OPC slightly below MathGAP (7.0) but above Omni-MATH/ImProver (6.75), settling at 6.5.

## Score and Decision

The paper makes a strong, timely dataset contribution with several genuinely novel empirical findings. The OPC scale (5,062 proofs, 13 expert judges), the proof-answer gap quantification, the ranking-based best-of-n methods, and the downstream fine-tuned model all represent real, substantial contributions. However, two headline claims — "on-par with human performance" for GPT-5's judging (which compares maj@5 against individual humans) and the "4× more problems" PutnamBench comparison (which uses different test sets without flagging this in the abstract) — are overclaimed relative to the evidence presented. These are fixable framing issues, not fundamental methodological flaws, and the underlying results remain meaningful when properly characterized.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>