Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

The paper introduces the Open Proof Corpus (OPC), a dataset of 5,062 human-evaluated LLM-generated mathematical proofs across 1,010 competition problems (IMO Shortlist, Putnam, USAMO, MathArena, etc.) with rigorous annotation procedures (former IMO participants as judges, 10% double-grading, 90.4% inter-judge agreement). Using the OPC, the paper studies three questions: (1) the gap between informal and formal proof generation, (2) the relationship between final-answer accuracy and full proof correctness, and (3) the effectiveness of best-of-n selection for improving proof quality. The paper also fine-tunes an 8B model (OPC-R1-8B) on the OPC that achieves 88.1% judgment accuracy, close to the best frontier models.

## Strengths

- **Large-scale, human-validated dataset of genuine research utility.** The OPC is the first large dataset of human-evaluated LLM-generated solutions to prestigious competition problems. With 5,062 proofs across 1,010 problems, rigorous judge selection (former IMO participants), pilot phase, 10% double-grading, and detailed annotation guidelines (Sections 3–4), the dataset fills a real gap and is designed for downstream training and evaluation. This is the paper's strongest and most solid contribution.

- **OPC-R1-8B demonstrates the dataset's practical value for training proof judges.** Fine-tuning R1-QWEN3-8B on the OPC using GRPO yields an 8B model achieving 88.1% maj@5 judgment accuracy, matching GEMINI-2.5-PRO and approaching GPT-5's 90.8% (Table 2). This provides direct evidence that the OPC enables meaningful improvement in automated proof evaluation.

- **Self-evaluation bias finding is well-supported and insightful.** Table 3 systematically shows that for GEMINI-2.5-PRO, o4-MINI, and o3, judges perform worst when evaluating their own proofs, while the pattern reverses for QWEN3-235B-A22B (Section 5.2). This is a concrete, non-obvious finding about a key limitation for self-assessment in mathematical reasoning.

- **Uncertainty acknowledgment analysis provides a clear negative result.** Of over 1,700 incorrect solutions, only 114 (6.7%) contain an explicit acknowledgment of inability to solve the problem, with nearly all from o3 (Section 5.1). This cleanly quantifies LLMs' reluctance to admit failure, an important trustworthiness issue.

- **Dataset is structured for broad applicability.** The four subsets (MathArena, PutnamBench, best-of-n, generic) are intentionally designed to support different analyses and training setups (Section 4), making the resource reusable beyond the paper's own experiments.

- **Contamination robustness experiment provides supporting evidence.** Table 4 shows that providing ground-truth solutions alongside proofs changes judge accuracy by at most ±3.1% for most models (and non-significantly), suggesting limited contamination impact on judging results (Section 5.6).

## Weaknesses

### Fatal
None.

### Major

1. **The gap analysis in Section 5.4 conditions on the wrong variable, systematically understating the true gap between final-answer accuracy and proof correctness.** The paper first filters to solutions with correct final answers, then evaluates proofs only on that subset, and presents the resulting conditional probability P(correct proof | correct answer) as the "proof correctness rate" in Figure 5 alongside unconditional final-answer accuracy. Because P(correct proof) = P(correct answer) × P(correct proof | correct answer), the gap actually reported — P(correct answer) – P(correct proof | correct answer) — is systematically smaller than the true gap P(correct answer) – P(correct proof). For example, the paper claims GEMINI-2.5-PRO "loses only 8% of its final-answer accuracy when proof correctness is required" (84.9% → 77.6%). Recomputing unconditionally: true P(correct proof) = 84.9% × 77.6% = 65.9%, yielding a true gap of ≈19%. Similarly, o3's reported "drop of almost 30%" (87.6% → 59.5%) should be ≈35.5%. The qualitative conclusion that a gap exists is preserved, but the specific magnitudes and the comparative narrative (e.g., "loses only 8%") are materially misleading. The paper's own text in the introduction ("GEMINI-2.5-PRO loses only 8%") and throughout Section 5.4 needs correction.

2. **The human judging baseline is miscalibrated, overstating the claim that LLMs are "on par with human performance."** The paper reports 90.4% as the human accuracy in Table 2 — the *inter-annotator agreement* rate from double-graded samples. The paper itself derives that this agreement rate implies a single-judge error rate of ~5% (solving 0.904 = (1-p)² + p²), which corresponds to individual judge accuracy of ~95%, not 90.4%. Using the agreement rate as the human baseline in the "pass@1" column inflates the apparent human performance relative to individual LLM judges (which are evaluated against the human-generated gold standard, not against each other). The claim that GPT-5 (89.3% pass@1, 90.8% maj@5) is "approaching the 90.4% human baseline" and "on-par with human performance" (Figure 1, Section 5.2, Abstract) is substantially overstated. A properly calibrated human baseline (~95%) would leave a materially larger gap. The paper should either use the implied individual accuracy or provide a clear justification for why the agreement rate is the appropriate comparator.

3. **Post-hoc data exclusion in the best-of-n analysis (Section 5.5) violates transparency norms.** A footnote states: "A small bug in the Rank (Swiss) method caused incorrect selections for 18 questions. These are excluded from the analysis." Excluding 18 questions (≈12% of the 152-problem best-of-n subset) because the method produced "incorrect selections" discards potentially negative results. It is impossible for the reader to assess whether the bug biased the method upward or downward or how the results would change if the 18 questions were included. At minimum, the results must be reported with and without the excluded questions, and the nature of the bug must be fully documented. As presented, this undermines the credibility of the best-of-n comparison — a core empirical claim of the paper.

### Minor

1. **The formal vs. informal comparison (Section 5.3) has a caveat that should be acknowledged more explicitly.** The paper appends the final answer to the problem statement for both formal and informal models "to mirror the setup for formal models." Contrary to the reviewer suggestion, the informal models are not at an informational disadvantage — both conditions receive the answer. However, appending the answer likely benefits informal proof generation more than formal proof generation, because an LLM can reverse-engineer a natural-language proof from a known answer more flexibly than a formal prover can. This asymmetry should be explicitly discussed as a limitation of the comparison rather than left implicit. The headline claim that informal proof generation "solves 4× more problems" is directionally correct but the magnitude should be understood as conditional on this design choice.

2. **The dataset curation for ~50% model accuracy (Section 3.1) limits what the aggregate statistics in Section 5.1 describe.** The paper states that problem selection was "actively monitored to ensure that the selected problems remained appropriately challenging" with a target of "roughly 50% model accuracy." This means the dataset-level numbers (e.g., 43% overall correctness) are descriptive of the *curated dataset*, not of the models' general capability on competition problems. While model-to-model comparisons on the same problems remain valid, the paper should more prominently acknowledge that the aggregate correctness rates are influenced by deliberate curation rather than reflecting a natural sample. This is partially covered but could be clearer.

3. **The contamination analysis (Section 5.6) relies partially on rhetorical arguments.** The claim that the informal-formal gap is "too large to be affected by small changes" is an assertion rather than a quantitative bound. The main supporting evidence is the Appendix C experiment, which is appropriately referenced but should be summarized in the main text for readers. This is a minor presentation issue rather than a substantive flaw, especially since Table 4 does provide some empirical evidence on the judging side.

### Trivial
None.

## Nice-to-Haves

- Show best-of-n results both with and without the 18 excluded questions, and fully document the bug in Rank (Swiss).
- Recompute the gap analysis in Section 5.4 using unconditional proof correctness rates (or clearly label Figure 5 as conditional and adjust claims accordingly).
- Recalibrate the human baseline in Table 2 to the implied ~95% individual accuracy (or provide a detailed justification for using the agreement rate).
- Include a brief summary of the Appendix C contamination experiment in the main text of Section 5.6.

## Removed Points

These points from the input reviews are removed or downgraded with justification:

- **Harsh critic's claim about Table 3 self-evaluation misreading:** The critic states the paper misreads Table 3 (that "all models except QWEN3-235B-A22B perform worse when judging their own proofs" is incorrect because QWEN3's lowest accuracy is on GEMINI's proofs). **Removed.** The paper's claim is *exactly* that QWEN3 is the exception — which the critic's own numbers confirm. The paper correctly states the finding. This is a misreading by the reviewer.

- **Harsh critic's claim about formal vs. informal answer asymmetry:** The critic states "The formal model is given the problem *and* the answer... The informal model is given only the problem." **Removed.** The paper explicitly states it "appended the informal final answer... to the problem statement to mirror the setup for formal models" — both conditions receive the answer. The factual premise is incorrect. The weakened version (that giving the answer may help informal models more) is retained as a Minor caveat.

- **Harsh critic's claim that the contamination experiment "is not described in the main text":** **Removed.** The paper says "In §C, we present a small experiment..." in the main text (Section 5.6), which is a correct reference. The description is deferred to the appendix as is standard.

- **Strength Finder's more generic strengths** (e.g., "addressed an important problem," "targeted a interesting question"): **Removed** due to lack of concrete evidence specific to this paper. The retained strengths are specific and grounded.

## Novel Insights

The most novel observation that emerges from triangulating the reviews is that the OPC dataset is a genuinely useful resource whose value is largely independent of the paper's empirical analyses. The three headline empirical findings — the formal/informal gap, the final-answer vs. proof correctness gap, and best-of-n improvements — all have methodological issues that weaken specific quantitative claims, but the dataset itself is well-constructed, has clear documentation, and enables an 8B model to reach frontier-level judging performance. This suggests the OPC could be more impactful as a community resource than as a vehicle for the paper's own conclusions, and the paper would benefit from reframing the empirical sections as exploratory analyses grounded in a valuable resource rather than as definitive answers.

## Suggestions

1. **Fix the gap analysis.** Either (a) compute unconditional proof correctness by multiplying the reported conditional rates by the final-answer accuracy (P(correct proof) = P(correct answer) × P(correct proof | correct answer)), or (b) clearly relabel Figure 5 as showing P(correct proof | correct answer) and revise all associated claims about the size of the gap. The introduction's statement about GEMINI-2.5-PRO "losing only 8%" must be corrected.

2. **Recalibrate the human judging baseline.** Either compute and report the implied individual accuracy (~95%) using the paper's own error-independence model, or provide a clear justification for why the inter-annotator agreement rate is the appropriate comparator for single LLM judges.

3. **Restore the excluded best-of-n data.** Include the 18 excluded questions in at least a supplementary analysis, document the bug precisely, and report results with and without these questions so readers can assess the impact.

4. **Acknowledge the formal/informal caveat explicitly.** Add a sentence noting that providing the answer likely benefits informal models more because they can construct natural-language proofs backward from a known answer, and that the 4× gap should be interpreted with this in mind.

5. **Make the dataset curation's effect on aggregate statistics more prominent.** Add a limitation note that the ~50% accuracy target during problem selection means the dataset-level averages reflect curation choices, not unconditional model capability on competition problems.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>