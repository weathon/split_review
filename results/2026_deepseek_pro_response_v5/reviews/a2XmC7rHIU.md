Now I have sufficient calibration data. Let me finalize the review.

**Calibration summary across all rounds:**

| Anchor | Score | Round | Comparison to OPC |
|--------|-------|-------|-------------------|
| JNZ3Om6NPS (GPT limitations theory) | 2.00 | R1 | Much weaker — OPC is a real empirical contribution |
| koza5fePTs (Planning benchmark) | 2.00 | R1 | Much weaker |
| v3DwQlyGbv (Paramanu-Ganita) | 2.33 | R1 | Much weaker |
| EXaKfdsw04 (StepProof) | 3.25 | R1 | Weaker — significant methodological flaws, limited novelty |
| mb2rHLcKN5 (SubgoalXL) | 3.75 | R1 | Weaker — different focus |
| DexGnh0EcB (MathEval) | 4.20 | R1 | Weaker — benchmark aggregation with limited novelty |
| uDZ9d4UAUh (Math mistakes) | 4.75 | R1 | Weaker — narrower scope |
| xlxGsX1pc7 (U-MATH) | 5.25 | R1 | Weaker — LLM-judge based, less rigorous human eval |
| u6jbcaCHqO (SciBench) | 5.60 | R1 | Weaker |
| WrBqgoseGL (Putnam-AXIOM) | 5.80 | R1 | Weaker — smaller scale, no proof evaluation |
| jKHmjlpViu (OpenWebMath) | 6.00 | R2 | Different type — web corpus, not human-annotated |
| AjXkZIvjB (GSM-Symbolic) | 6.00 | R2 | Different — synthetic benchmark, narrower |
| nDvgHIBRxQ (MathCheck) | 6.25 | R2 | Comparable but OPC has richer analyses |
| yaqPf0KAlN (Omni-MATH) | 6.75 | R1/R2 | OPC is slightly stronger — human proof evaluation vs. final-answer + LLM judge |
| 5ck9PIrTpH (MathGAP) | 7.00 | R1 | Comparable — different approach, both strong |
| Se6MgCtRhz (Herald) | 7.00 | R2 | Stronger — novel pipeline + dataset + translator model |
| KUNzEQMWU7 (MathVista) | 7.25 | R1 | Stronger — multimodal math benchmark |
| 8xliOUg9EW (MUSTARD) | 7.33 | R2 | Stronger — novel data generation framework |
| yLClGs770I (MAmmoTH) | 7.20 | R2 | Stronger — training methodology paper |
| mMPMHWOdOy (WizardMath) | 8.00 | R1 | Much stronger — training method with large gains |

**Bracket:** 6.0–7.0. The paper is clearly above Putnam-AXIOM (5.80) and above Omni-MATH (6.75) on methodology rigor, but below Herald (7.00) and MUSTARD (7.33) on novelty and impact.

The OPC's rigorous human evaluation (13 IMO judges, double-grading, pilot phase) and genuinely novel empirical findings (differential final-answer/proof gap, ranking-based best-of-n) place it in the strong dataset paper category. However, two major framing overclaims (human-level judging conflates inter-judge agreement with accuracy; PutnamBench comparison provides answer hints to informal but not formal models) and minor methodological issues (retry counts unreported, Rank Swiss bug underdescribed) bring it below the 7.0 threshold.

**Final score: 6.5**

Decision: This is borderline Accept/Reject territory. Given the calibration, 6.0 papers were accepted (OpenWebMath, GSM-Symbolic got Accept decisions) and Omni-MATH at 6.75 was Accept. The OPC at 6.5 would likely be Accept with the expectation that the major framing issues are addressed.## Summary
This paper introduces the Open Proof Corpus (OPC), a human-validated dataset of 5,062 LLM-generated mathematical proofs across 1,010 competition problems, graded by 13 former IMO participants with 10% double-grading. Using the OPC, the authors address three open questions: the gap between formal and informal proof generation, the relationship between final-answer accuracy and proof correctness, and best-of-n selection strategies. They also fine-tune an 8B model that approaches GPT-5 in proof judging accuracy. The dataset and pipeline represent a genuine community resource.

## Strengths
- **Rigorous annotation pipeline at unprecedented scale:** 13 former IMO participants graded 5,062 proofs with a pilot phase (300 proofs, 35% double-graded, §3.3), iterative instruction refinement with judges, coordinator-mediated discrepancy resolution, and LLM issue-summary validation showing no introduced bias (§3.2). This substantially exceeds prior proof-evaluation efforts in both scale and quality control.
- **Model-specific differential gap between final-answer accuracy and proof correctness:** Figure 5 demonstrates that while GEMINI-2.5-PRO, o4-mini, and o3 all achieve 85–88% final-answer accuracy on MathArena, proof correctness diverges dramatically (77.6%, 80.3%, and 59.5% respectively). The finding that o3 fabricates convincing but incorrect proofs far more often than competitors is novel and evidence-backed.
- **Well-controlled best-of-n experiment revealing ranking advantage:** The 60-problem subset with all 8 generations human-evaluated (§5.5, Fig. 6a) enables clean comparison of four selection strategies. Rank (Swiss) reaches 47% vs. Discrete's 34% at n=8, and ranking methods continue scaling while pointwise methods plateau after n=5 — a genuinely actionable insight.
- **Honest self-evaluation analysis:** Table 3 shows models consistently perform worse judging their own proofs (diagonal entries are lowest or near-lowest for all models except QWEN3), validating the judging methodology (no self-preference bias) and revealing an interesting limitation in LLM self-assessment.
- **Contamination robustness experiment:** Table 4 shows that providing ground-truth solutions to judge models yields negligible accuracy changes (GPT-5: -0.3%), directly testing whether training data contamination inflates judging results — a clever and well-executed ablation.

## Weaknesses

### Fatal
None.

### Major
- **The "human baseline" is inter-judge agreement, not accuracy:** Section 4 defines the 90.4% figure explicitly as inter-judge agreement on double-graded proofs, and the paper estimates individual judge error rate at p=5%, implying ~95% human accuracy. Yet §5.2 places this 90.4% agreement rate as the "HUMAN" baseline in Table 2 and claims GPT-5's 90.8% maj@5 makes LLMs "on-par with human performance" (abstract). These are different quantities: inter-judge agreement vs. accuracy measured against resolved labels. The section title "LLMs Are Human Level Judges" is overstated given this mismatch. The LLM judging results remain impressive and the comparison is not meaningless, but the framing must be substantially revised.
- **PutnamBench comparison confounded by providing final answer to informal models:** Section 3.1 states that for PutnamBench, the authors "appended the informal final answer (if present) to the problem statement to mirror the setup for formal models." Formal provers on PutnamBench receive the theorem statement, not a pre-computed answer for computational problems. Providing the answer changes the task from "prove this" to "verify this answer and produce a proof," which is easier. The headline claim that informal models "solve 4x more problems" compares models under different task conditions. The qualitative gap is clearly real given its magnitude, but the numerical framing is misleading.

### Minor
- **Retry-generation for MathArena subset lacks quantification:** Section 3.1 states proofs were only retained with correct final answers, "retrying generation if necessary." The number of retries per model is never reported. If o3 required substantially more retries than GEMINI-2.5-PRO to hit correct answers, the proofs accompanying those answers may differ qualitatively from single-pass samples. This affects the precision of Figure 5's proof-correctness estimates, though not the existence of the differential gap.
- **Rank (Swiss) bug affects a non-trivial fraction of data without analysis:** Footnote 1 states a bug caused incorrect selections for 18 questions, excluded from the 134-problem best-of-n subset (13.4%). The bug's nature is undescribed, and no analysis shows whether excluded problems differ from retained ones. However, the ranking advantage is independently validated on the 60-problem fully-evaluated subset (Fig. 6a).

### Trivial
- Non-English problem translations were verified only by the coordinator (§3.1), whereas the rest of the pipeline features rigorous double-checking.

## Nice-to-Haves
- Report retry counts per model for the MathArena subset to contextualize Figure 5's proof-correctness numbers.
- Discuss whether the best-of-n ranking advantage found with O4-MINI is expected to generalize to other models.
- Provide details on the Rank (Swiss) bug and analyze whether excluded problems differ from retained ones.
- Compute judge accuracy against coordinator-resolved labels to establish a proper human ceiling rather than using inter-judge agreement as a baseline.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Harsh Critic claimed contamination experiment results are "noisy" and warrant more discussion:** This is a matter of interpretive emphasis, not a verifiable flaw. Table 4 clearly presents the results and the paper discusses them straightforwardly.
- **Harsh Critic questioned whether the PutnamBench subset is representative of full benchmark difficulty:** Speculation without evidence in the paper.
- **Harsh Critic noted model distribution is skewed (O4-MINI 1,615 vs. R1 326):** The paper explicitly addresses this with its two-partition design in Figure 3. Not a weakness.
- **Harsh Critic noted best-of-n method description references stripped appendix:** Per hard rule, criticisms about missing appendices are removed.
- **Strength Finder "quantified formal-to-informal gap" as unqualified strength:** The gap is real but the numerical comparison is confounded (see Major Weakness 2). The strength is retained with the caveat noted.
- **Strength Finder "LLMs can judge proofs at near-human level" as unqualified strength:** The judging capability is real but the "human-level" framing is overstated (see Major Weakness 1).

## Novel Insights
The paper's most novel empirical insight is the model-dependent dissociation between final-answer accuracy and proof correctness: o3 matches GEMINI-2.5-PRO on final answers (~87%) but produces far fewer correct proofs (59.5% vs. 77.6%), suggesting that reasoning-heavy models may learn to optimize for final-answer benchmarks without developing robust proof-generation capabilities. The self-evaluation finding — that LLMs are consistently worse at judging their own proofs — is also a clean, counterintuitive result with implications for self-improvement and self-verification approaches.

## Suggestions
- Reframe the "human level" claim in §5.2 to properly distinguish inter-judge agreement from accuracy. Compute human accuracy against coordinator-resolved labels as the proper ceiling, and update the section title.
- For the PutnamBench comparison, either re-run informal evaluation without answer hints or explicitly reframe as "informal proof generation with answer hints vs. formal proof generation without hints" with a discussion of effect size.
- Report retry counts per model for MathArena and consider evaluating a single-pass subset to bound the retry effect on Figure 5 estimates.

## Score and Decision

**Bracketing (Round 1):** OPC clearly exceeds weak-reject anchors (StepProof 3.25, MathEval 4.20) and the middle band (Putnam-AXIOM 5.80, U-MATH 5.25). It is comparable to or stronger than Omni-MATH (6.75) and roughly comparable to MathGAP (7.00). It sits below MUSTARD (7.33) and Herald (7.00), which offer stronger technical novelty.

**Narrowing (Round 2):** Within the 6.0–7.0 bracket, OPC is stronger than Omni-MATH (6.75) on evaluation rigor (human proof grading vs. LLM-as-judge for final answers) but weaker than Herald (7.00) on technical novelty (dataset paper vs. novel pipeline + translator). The two major overclaims and minor methodological gaps bring it below the 7.0 threshold.

**Final score: 6.5**, reflecting a strong dataset paper with real empirical contributions and a rigorous annotation pipeline, held back by framing overclaims that require correction.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>