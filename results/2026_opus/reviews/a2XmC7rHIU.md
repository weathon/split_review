Now I have enough understanding of the paper. Let me run calibration searches.Based on initial bracketing, the paper appears stronger than Putnam-AXIOM (5.8) and roughly comparable to MathGAP (7.0) or better. Let me narrow further.Based on calibration, I have a clear sense of where to anchor this paper. Let me write the final review.

## Summary
The Open Proof Corpus (OPC) is a 5,062-proof, human-graded dataset across 1,010 problems from prestigious math competitions (IMO, USAMO, Putnam, etc.), graded by 13 expert judges (former IMO participants) with 90.4% inter-judge agreement. The authors use it to (a) quantify the informal vs. formal proof gap, (b) characterize the misalignment between final-answer and proof correctness, (c) compare best-of-n selection strategies, and (d) fine-tune an 8B judge model (OPC-R1-8B) that matches GEMINI-2.5-PRO and approaches GPT-5 in judging accuracy.

## Strengths
- **Large-scale, expertly-graded resource**: 5,062 proofs across 1,010 problems, double-graded at ~10%, with 90.4% inter-judge agreement — the largest expert-graded LLM proof corpus to date, and the judges (former IMO participants) are unusually qualified for this domain (§3.1, §4).
- **Open release of dataset and judge model**: The OPC and OPC-R1-8B are publicly released, distinguishing this work from prior closed efforts (Mahdavi et al., Guo et al. cited in §2).
- **Quantification of the informal/formal proof gap**: On the PutnamBench subset, GEMINI-2.5-PRO (82.7%) vs. GOEDEL-PROVER-V2 (<19%) gives the first large-scale, human-graded comparison of natural-language vs. formal proof generation (§5.3, Fig. 4).
- **Final-answer vs. proof correctness divergence**: The MathArena subset documents that, e.g., o3 drops from 87.6% final-answer correctness to 59.5% proof correctness while GEMINI-2.5-PRO drops only ~8%, providing concrete evidence that final-answer benchmarks misrepresent proof ability (§5.4, Fig. 5).
- **8B judge model competitive with frontier closed models**: OPC-R1-8B achieves 88.1% maj@5, matching GEMINI-2.5-PRO and within ~2.7 pts of GPT-5 at substantially lower cost (Table 2).
- **Contamination-control experiment**: Providing ground-truth solutions alongside proofs to be judged yields small/non-significant ∆ on top models (e.g., GPT-5: 89.3→89.0), strengthening the judge-side robustness claim (§5.6, Table 4).

## Weaknesses

### Fatal
None.

### Major
- **Best-of-n headline (§5.5) excludes 18/134 problems from the winning method.** Footnote 1 (p. 9) admits "a small bug in the *Rank (Swiss)* method caused incorrect selections for 18 questions. These are excluded from the analysis." Since *Rank (Swiss)* (improving accuracy by 17%, Fig. 6(b)) is the section's headline result, dropping 18/134 questions for that method but not others is a post-hoc filter that favors the winning method. The qualitative ordering may still be right, but the section needs to be re-run including those 18 (either re-graded under the corrected selection, or carrying the buggy selection through honestly) before the 17% number can be claimed with confidence.
- **Generic-subset "capability" numbers reflect an adaptively curated mix, not a fixed distribution.** §3.1 states "the difficulty level of the competition aligns with our target of roughly 50% model accuracy" and "more problems from international competitions were added when initial results indicated that models were performing very well … prioritization was adjusted based on ongoing performance metrics." The abstract and §1's "43% correct proofs" and the per-model bars in Fig. 3 inherit this confound. Cross-model comparisons should be restricted to the externally-anchored subsets (MathArena, PutnamBench, IMO Shortlist) for capability claims; the Generic subset is better framed as a training resource. The limitations section (§6) does not acknowledge this.

### Minor
- **"Informal solves 4× more problems in PutnamBench" mixes scaffolding regimes.** §5.3 itself notes that the agentic Seed-Prover reaches 50% on PutnamBench (much closer to GEMINI's 83%) and that "it is therefore not accurate to directly compare these numbers." But Fig. 1(b) and the abstract still report the 4× number without qualification. The conclusion (informal currently outperforms comparably-scaffolded formal systems) is plausible, but the multiplicative framing should be qualified everywhere it appears, not only in §5.3.
- **OPC-R1-8B's headline number is in-distribution.** §5.2 acknowledges that "the train set for OPC-R1-8B shares the same distribution as this test set, which may inflate its performance" and points to §C for OOD results. The contribution (an open 8B judge ported from larger judges) is real, but the abstract/contribution bullets stating it "matches GEMINI-2.5-PRO" should propagate the OOD caveat or report the OOD number as the headline.
- **Human-error estimate assumes independent judges.** §4 solves 0.904 = (1−p)² + p² for p ≈ 5%. For proofs, judge errors are plausibly correlated (both judges may miss the same subtle gap), so 5% is an underestimate, making the framing "GPT-5 is on-par with human performance" somewhat optimistic.
- **§5.4 conclusion rests on a 112-problem subset.** The "o3 suffers a ~30% drop" comparison is appropriately stated, but per-model confidence intervals belong in Fig. 5 (currently absent) given the sample size.
- **§3.2 bias check is confounded by problem difficulty.** Comparing O4-MINI-judge agreement with humans "before and after" introducing LLM issue summaries mixes the change in tool with a change in problem mix. A within-judge, within-problem A/B would be tighter — the authors themselves recognize the concern and disable summaries in best-of-n to "avoid compounding bias."
- **§5.6 contamination analysis covers judging well, but generation only qualitatively.** The cross-benchmark ordering argument is reasonable for relative comparisons but does not bound absolute inflation of, e.g., IMO Shortlist numbers in §5.1.

### Trivial
- The limitations section (§6) is brief and does not mention the curated Generic distribution, small best-of-n samples, or OPC-R1-8B in-distribution evaluation — these are precisely the limitations that most affect reader interpretation.

## Nice-to-Haves
- Lean into externally-anchored subsets (MathArena, PutnamBench, IMO Shortlist) as the canonical capability-reporting surfaces; treat Generic as a training/analysis resource.
- A taxonomy of error types derived from the per-sentence annotations and judge justifications (which the corpus uniquely supports) would be a distinctive contribution that no prior proof-evaluation paper could produce at this scale, and would sharpen both §5.1's "uncertainty acknowledgment" observation and §5.4's findings.
- Targeted evaluation of OPC-R1-8B on the <3% uncertain-flagged proofs (the regime where automated grading matters most) would be more informative about real-world utility than the overall test-split accuracy.
- Match scaffolding between formal and informal systems (or restrict the comparison to non-agentic formal systems) before claiming a multiplicative gap.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *Strength: "addressed an important problem"* — generic; the specific strengths above already capture the substantive contribution.
- *Strength: "best-of-n is the first systematic comparison of selection strategies for proof generation"* — kept implicitly in the major weakness about §5.5 evidence; the underlying methodological novelty is real but the strength as worded overstates given the post-hoc filtering issue.
- *Harsh critic's "OPC-R1-8B's headline number not yet released / cannot be verified"* — not raised; the model is released.

## Novel Insights
None beyond the paper's own contributions. The empirical findings (informal > formal, final-answer ≠ proof correctness, pairwise ranking > scalar scoring for best-of-n selection, models rarely admit uncertainty) are themselves the novel observations and would have been hard to establish without the corpus.

## Suggestions
- Re-run §5.5 with the 18 buggy-selection problems re-graded or accounted for; report the *Rank (Swiss)* number with the corrected sample.
- Replace abstract/Fig. 1(b) reports of "43% correct proofs" and "matches GEMINI-2.5-PRO" with either (a) the per-subset rates on externally-anchored splits, or (b) explicit notes that these numbers reflect a curated/in-distribution measurement.
- Add the agentic-formal qualifier to every appearance of the "4×" claim, not only §5.3 prose.
- Expand §6 to acknowledge curation of Generic, the small best-of-n samples, and the in-distribution OPC-R1-8B evaluation.
- Add per-model CIs to Fig. 5 and to Fig. 6(b).

## Evaluation along required axes
- **Originality**: High — first large-scale, expert-graded open corpus of LLM-generated competition proofs.
- **Importance of research question**: High — proof grading at scale is a real bottleneck for the field.
- **Claims supported**: Mostly yes. Headlines are mildly overclaimed (curation, in-distribution, post-hoc filter), but the underlying directions are credible.
- **Soundness of experiments**: Generally sound; the §5.5 exclusion is the one place where evidence does not match the framing.
- **Clarity of writing**: Clear and well-organized.
- **Value to the community**: High — open dataset + judge model + three well-targeted empirical analyses.

## Calibration

**Round 1 — Bracketing.**
Anchors retrieved:
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EXaKfdsw04.md` (StepProof, avg 3.25, round 1, low band) — far weaker, no human-graded corpus, OPC is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JNZ3Om6NPS.md` (GPT inherent limitations, avg 2.00, round 1, low) — irrelevant theoretical paper, much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/koza5fePTs.md` (Planning benchmark, avg 2.00, round 1, low) — much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/v3DwQlyGbv.md` (Paramanu-Ganita, avg 2.33, round 1, low) — much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WrBqgoseGL.md` (Putnam-AXIOM, avg 5.80, round 1, middle) — narrower scope (236 problems, final-answer only), OPC is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/C25SgeXWjE.md` (ProverGen, avg 6.25, round 1, middle) — synthetic FOL benchmark, more narrow than OPC.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5ck9PIrTpH.md` (MathGAP, avg 7.00, round 1, middle) — synthetic arithmetic-proof framework, similarly substantial; OPC complementary and arguably more impactful for real competition proofs.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Zix86UbMGh.md` (ProofNet, avg 4.50, round 1, middle) — much smaller (371 problems), OPC stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/owR9ofvkFQ.md` (MathOdyssey, avg 4.50, round 1, middle) — narrower scope, OPC stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KIgaAqEFHW.md` (miniCTX, avg 8.00, round 1, high) — strong specialized formal-theorem benchmark; comparable significance, OPC arguably broader.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oYjPk8mqAV.md` (Magnushammer, avg 8.00, round 1, high) — methodological premise-selection paper, different category.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mMPMHWOdOy.md` (WizardMath, avg 8.00, round 1, high) — training method paper, different category.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GGlpykXDCa.md` (MMQA, avg 8.00, round 1, high) — different domain.

Round-1 bracket: **6.5 to 7.5** — clearly stronger than Putnam-AXIOM/ProofNet/MathOdyssey, comparable to MathGAP/Omni-MATH, but with real evidential issues that keep it below the 8.0 anchors.

**Round 2 — Narrowing.**
Anchors:
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yaqPf0KAlN.md` (Omni-MATH, avg 6.75, round 2) — 4,428 olympiad problems with GPT-judge eval; OPC's grading is by IMO participants (more rigorous) and includes free-form proofs (not just final answers), making OPC arguably stronger on rigor and on the proof-generation question; OPC has more headline-overclaim issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/cfGpIcOIa5.md` (GeoILP, avg 6.00, round 2) — synthetic ILP dataset, different domain.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jKHmjlpViu.md` (OpenWebMath, avg 6.00, round 2) — pretraining-data resource, different category.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xsELpEPn4A.md` (JudgeLM, avg 7.50, round 2) — fine-tuned judge model with comprehensive analysis; very comparable to OPC-R1-8B + dataset story; OPC arguably has more substantive empirical findings (three open questions resolved) but JudgeLM's bias analysis is more developed.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7El7K1DoyX.md` (Lawma, avg 7.00, round 2) — domain specialization study, different domain but similar "fine-tune small model, beat large one" theme.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9OevMUdods.md` (Pinocchio, avg 6.75, round 2) — factual knowledge benchmark, different domain.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3GTtZFiajM.md` (LLM-judge bias quantification, avg 6.75, round 2) — adjacent topic, narrower.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8xliOUg9EW.md` (MUSTARD, avg 7.33, round 2) — theorem+proof data synthesis with quality controls; comparable significance for theorem/proof data.

OPC sits between Omni-MATH (6.75) and JudgeLM (7.50): stronger than Omni-MATH on grading rigor and breadth of findings, comparable to JudgeLM in overall package (dataset + judge + analyses) but with notable headline-overclaim issues (curation, 18-question exclusion, in-distribution OPC-R1 framing) that prevent it from clearly exceeding JudgeLM. Final score lands near MUSTARD/Lawma (7.0–7.33), closer to the upper end given the unusual scale and rigor of expert grading.

**Final score: 7.0** — solidly above Omni-MATH/MathGAP, comparable to MUSTARD/Lawma, just below JudgeLM, well below the round-1 high anchors at 8.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>