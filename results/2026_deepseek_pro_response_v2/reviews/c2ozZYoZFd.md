Now I have a clear picture from the calibration. Let me finalize the review.

**Round 1 Bracket:** 7.5–8.5, anchored against `jOmk0uS1hl` (8.00, accepted — methodological critique about evaluation).

**Round 2 Narrowing:** Compared against `m2NVG4Htxs` (6.75 — narrower scope, limited novelty), `tfyHbvFZ0K` (7.50 — re-examines existing theory, solid but less comprehensive), and `jOmk0uS1hl` (8.00 — most similar, clean reception). The paper under review is stronger than `m2NVG4Htxs`, comparable to or slightly stronger than `tfyHbvFZ0K`, and comparable to `jOmk0uS1hl`. **Final score: 8.0.**

---

## Summary
This paper conducts a forensic re-examination of Nguyen et al. (2024), an ICLR 2025 Oral paper that introduced "min-p" sampling and claimed it achieves superior quality and diversity over established methods. Through systematic re-analysis of the original paper's four lines of evidence (human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, community adoption claims), the authors demonstrate that the evidence does not support min-p's claimed superiority. Key findings include: (1) one-third of human evaluation data was omitted, and correct statistical testing shows no consistent advantage; (2) a novel Best-of-N hyperparameter-control methodology on GSM8K shows min-p is indistinguishable from baselines when hyperparameter tuning volume is equalized; (3) LLM-as-a-Judge evaluations had methodological issues and apparent selective reporting; and (4) community adoption claims of 54K repos and 1.1M stars were retracted. The paper derives six methodological lessons for rigorous ML research.

## Strengths

- **Novel Best-of-N methodology for fair hyperparameter comparison (Section 3.1, Figures 4–5):** The paper introduces a principled method to control for hyperparameter tuning volume when comparing samplers — subsampling equal numbers of hyperparameters per sampler and computing expected best performance as a function of budget. The sweep is unusually thorough: 9 models × 2 training stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds, totalling ~6000 A100-hours. Both analyses (Figures 4 and 5) converge to show min-p is indistinguishable from baselines when hyperparameter volume is equalized. This methodology is operationalizable and broadly applicable beyond this case study.

- **Rigorous multi-level statistical re-analysis of human evaluations (Section 2.2, Table 1):** The paper conducts 12 one-sided paired t-tests across all metric/temperature/baseline combinations, then transparently layers three increasingly stringent criteria: uncorrected p-values (5/12 significant), Bonferroni correction (1/12 significant), and an Intersection-Union Test appropriate for the original claim of "consistently" outperforming (p=0.378, failing to reject). This stepwise presentation makes the statistical reasoning accessible and demonstrates exactly how the original paper's pooling into a single t-test was misleading.

- **Documented data omission with confirmed impact (Section 2.1):** The paper discovers that one-third of the original human evaluation data (scores for basic sampling) was excluded from the methodology, analysis, and results without justification — a finding publicly confirmed by the original authors. The inclusion of this data demonstrably changes the paper's conclusions.

- **Specific, falsifiable identification of asymmetric score reporting (Section 4.3):** The paper documents a precise instance of selective reporting in the original Table 3(b): the higher of two min-p scores was reported (52.01 at p=0.05 vs. 50.14 at p=0.01) while the lower of two top-p scores was reported (50.07 at p=0.9 vs. 50.43 at p=0.98). The specific numbers are concrete and checkable.

- **Documented retraction of community adoption claims (Section 5):** The paper establishes that the original claims of 54,000 GitHub repositories and 1.1 million stars were unsubstantiated (major LM repositories total only ~453K stars) and documents that the original authors retracted both numbers. It further notes that 3 of 4 ICLR reviewers and the Area Chair cited these retracted numbers as justification for endorsement, strengthening the paper's argument about consequences of unverified claims on peer review.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **GPQA evaluation mentioned but not conducted (Section 3):** Section 3's opening sentence describes the original paper's NLP benchmark evaluations as covering both GSM8K and GPQA, but the actual re-analysis sweep is restricted to GSM8K only. The paper is transparent about this (citing ~6000 A100-hour compute budget), and GSM8K alone provides substantial evidence. However, GPQA is a qualitatively different benchmark (graduate-level QA vs. grade-school math), so the conclusions about NLP benchmarks are limited to one domain. A scoping clarification in the section's opening would prevent overpromising relative to the actual analysis.

- **Qualitative annotation methodology underspecified (Section 2.3):** The paper states "we manually annotated the qualitative responses" and visualizes results in Fig. 2, but provides no description of who performed the annotation, whether multiple annotators were used, whether there was an annotation protocol or inter-annotator reliability check, or how ambiguous responses were resolved. For a paper that criticizes the original work's handling of qualitative data, documenting this process would strengthen credibility.

- **Selective-reporting allegation relies on an informal source (Section 4.3):** The claim that the original authors reported asymmetric scores references a Telegram link shared by the first author. While the specific numbers (52.01 vs. 50.14; 50.07 vs. 50.43) are concrete and checkable, presenting this evidence through a more permanent or reproducible channel (e.g., a reconstructed table from publicly available data) would better match the paper's own standards for rigor. The appendix (stripped by the parser) may contain this documentation.

- **"Remains misleading" claim unsubstantiated (Section 5):** The paper states that the Camera Ready's replacement community adoption statement "remains misleading" (line 204-205) but does not argue or substantiate this claim. Either providing the reasoning or removing the unsupported assertion would improve the section.

- **"Blueprint" framing slightly overpromises relative to lessons delivered (Section 6):** The six general lessons are sensible but somewhat generic ("apply statistical tests rigorously," "ensure methodological clarity"). The genuinely novel methodological contribution is the Best-of-N hyperparameter-control analysis. The paper would be stronger if it foregrounded this contribution rather than packaging it within a broader "blueprint" framing.

### Trivial

- The paper adopts an adversarial tone in places (e.g., "invalidated by its own data" in the abstract) that may distract some readers from the substance of the findings.

## Nice-to-Haves

- Running the GPQA sweep would broaden the NLP benchmark evidence, though the ~6000 A100-hour GSM8K sweep already provides substantial evidence and the compute constraint is reasonable.

- Documenting the qualitative annotation protocol (number of annotators, whether blinded, how disagreements were resolved) would further strengthen Section 2.3.

- Presenting the Section 4.3 selective-reporting evidence through a reconstructed table from publicly available data rather than relying on a Telegram reference.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Reliance on private communication" (lines 64-65):** The harsh critic flagged that the paper relies on "private communication" with original authors. However, the paper explicitly says the authors "publicly told us" and "said publicly" — this was public communication, not private. Removed as factually incorrect.

- **Harsh Critic: "Ranked as 18th highest-scoring submission" is extraneous/score-settling:** This is a pure stylistic judgment about tone, not a substantive weakness. The information provides relevant context about the paper's visibility and review process. Removed as a style nitpick.

- **Strength Finder: Generic framing strengths:** Some claimed strengths were generic (e.g., "the paper addressed an important problem," "crisis of rigor context-setting"). These are presentation choices rather than concrete, evidenced contributions and were removed.

## Novel Insights
The Best-of-N methodology for controlling hyperparameter tuning volume is a genuinely novel contribution that extends beyond this specific case study. By subsampling equal hyperparameter counts and measuring expected best performance as a function of budget, it operationalizes "fair comparison" in a way that detects asymmetric tuning. The methodology's complementary analyses (Figures 4 and 5) — absolute best-of-N performance and relative min-p advantage — provide a template for detecting whether claimed improvements survive equalized tuning budgets. This is broadly applicable to any ML subfield where methods differ in the number of tunable knobs.

## Suggestions

- Clarify Section 3's opening to explicitly state that the re-analysis is restricted to GSM8K, rather than letting the sentence about the original paper's GPQA evaluation create an expectation of coverage that isn't met until the compute-budget caveat later.

- Either substantiate or remove the claim that the Camera Ready's replacement community adoption statement "remains misleading" (Section 5).

- Document the qualitative annotation process for Section 2.3 even briefly — number of annotators, whether they were aware of the paper's hypothesis, and how ambiguous responses were categorized.

- Consider restructuring the framing around the Best-of-N methodology as the headline contribution rather than the generic "blueprint" lessons, since the methodology is the most transferable and novel element.

## Score and Decision

**Calibration anchors referenced:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| `SaOxhcDCM3` (Self-Consuming Training) | 3.20 | R1 | Significantly weaker — methodological flaws, rejected |
| `ejvf3JrZuC` (Theory of LLM Sampling) | 4.25 | R1 | Weaker — unclear definitions, limited contribution, rejected |
| `0xUEBQV54B` (Large Language Monkeys) | 5.00 | R1 | Weaker — findings seen as narrow/trivial, rejected |
| `m2NVG4Htxs` (Data Contamination) | 6.75 | R2 | Weaker — narrower scope and limited novelty, accepted |
| `tfyHbvFZ0K` (Knowledge Localization) | 7.50 | R2 | Comparable — re-examines existing theory with extensive experiments, but less comprehensive evidence base |
| `jOmk0uS1hl` (Training on Test Task) | 8.00 | R1 | Most similar — methodological critique with novel methodology, clean reception, comparable rigor. The paper under review has comparable strengths (more evidence lines, documented retraction) and comparable minor weaknesses |

**Round 1 bracket:** 7.5–8.5. **Round 2 narrowed to:** 7.5–8.0. The paper is comparable to `tfyHbvFZ0K` (7.50) in its re-examination approach but more comprehensive, and comparable to `jOmk0uS1hl` (8.00) in its methodological critique framing and clarity. All weaknesses are genuinely minor and none threaten the core contribution. **Final score: 8.0.**

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>