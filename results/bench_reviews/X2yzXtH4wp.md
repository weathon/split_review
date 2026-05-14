Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces Ambig-SWE, a benchmark that creates underspecified variants of 500 SWE-Bench Verified GitHub issues by using GPT-4o to remove critical details, producing paired well-specified/underspecified instances. The authors decompose the capability to handle underspecification into three components — detection (whether models recognize missing information), clarification (question quality), and integration (whether interaction improves task completion) — and evaluate six proprietary and open-weight LLM agents across all three dimensions. Key findings include: interaction can recover up to 74% of performance lost to underspecification for some models; Claude Sonnet 4 achieves 89% detection accuracy while Qwen 3 Coder never interacts (100% FNR even with strong prompting); and exploration-first questioning strategies (Claude Sonnet models) achieve comparable information gain with ~50% fewer questions than immediate-question strategies (Qwen 3 Coder).

## Strengths

- **Novel benchmark with rigorous paired design (Ambig-SWE).** By generating underspecified variants of SWE-Bench Verified issues and preserving their full-specification ground truth, the paper enables causal attribution of performance changes to interaction — a clear methodological advance over prior work on underspecification that either lacks paired ground truth or focuses on single missing details (Chen et al., 2025; Kim et al., 2024). The 500-instance scale and use of SWE-Bench Verified's automated evaluation harness give the benchmark practical utility.

- **Principled three-part decomposition of interaction capability.** Separating detection (RQ2), question quality (RQ3), and integration (RQ1) allows more targeted diagnosis than monolithic resolution metrics. The paper designs distinct experiments for each component, and the decomposition itself provides a framework the community can adopt for finer-grained agent evaluation.

- **Rich comparative findings across six diverse models.** The paper evaluates two proprietary families (Claude Sonnet 3.5/4, Haiku 3.5) and three open-weight models (Llama 3.1 70B, Deepseek-v2, Qwen 3 Coder 480B), spanning different scales and training paradigms. The finding that Qwen 3 Coder achieves coding performance comparable to Claude Sonnet 4 yet rigidly refuses to interact (100% FNR) is striking and actionable. The qualitative analysis of question strategies (Table 7, Section 5.3) revealing exploration-first vs. immediate-question behaviors is genuinely insightful.

- **Demonstration that interaction recovers substantial lost performance (RQ1).** The resolve-rate improvements from Hidden to Interaction settings are statistically significant across all models (Wilcoxon signed-rank, Table 4), with proprietary models recovering up to 80% of Full-setting performance. This quantifies the practical value of interaction in a controlled setting.

## Weaknesses

### Major

- **RQ2's detection experiment confounds detection with instruction-following and question-generation ability.** The experiment measures whether the model *interacts* when given underspecified vs. well-specified inputs, then labels this as "detection." But a model may detect underspecification yet fail to formulate a question (e.g., Qwen 3 Coder's 100% FNR could equally reflect inability to produce clarification questions as failure to detect), or may interact purely because the prompt instructs it to do so. The paper never directly probes the model's judgment (e.g., by asking it to explicitly rate completeness or explain its choice). While the varying encouragement levels (Neutral/Moderate/Strong) partially address this, the fundamental confound remains: the metrics in Table 2 (accuracy, FPR, FNR) are behavioral measures of *interaction propensity under task conditions*, not validated measures of *detection capability*. This undermines the paper's strongest claim about detection (Claude Sonnet 4's 89% "accuracy") and overstates the severity of Qwen's failure (it may be a question-generation failure rather than a detection failure).

### Minor

- **The "multiple, interdependent gaps" framing is stated but not empirically characterized.** The introduction and related work claim that prior work focuses on single missing details while this paper addresses "multiple, interdependent gaps." However, the paper never quantifies how many information gaps are present per issue, their types (architectural/locational/behavioral), or their interdependence. The underspecification is created via broad summarization (GPT-4o reducing detail), not by systematically introducing multiple interdependent gaps. This distinction between the paper's approach and prior work is asserted rather than demonstrated.

- **The Full setting includes developer discussion hints (Appendix A.2.1), making the "recovery" metric reflect recovery from a gap that includes more than just underspecification.** Specifically, the Full setting provides: (1) the original fully-specified issue, plus (2) "hints from the dataset, which contains the conversation between developers regarding the issue." The Interaction setting's user proxy also receives these hints plus file locations. Therefore, the Hidden-to-Full gap is not purely an underspecification gap — it also includes developer discussion content. The reported recovery rates (up to 80% of Full performance, Section 3.2) are relative to this augmented baseline. The paper discloses this in the appendix but doesn't discuss how it affects interpretation.

- **Question quality metrics (RQ3) are descriptively useful but lack validation against task performance.** The cosine distance and LLM-as-judge scores measure information extraction volume. The paper itself shows disconnects between these metrics and resolve rates (e.g., Claude Sonnet 3.5 and Haiku 3.5 achieve nearly identical cosine distance but differ by ~13 points in resolve rate), positioning this as a finding about integration rather than a metric flaw. However, the qualitative strategy analysis (exploration-first, answerability) remains speculative without causal evidence linking specific question features to performance gains. The LLM-as-judge scores converging near 4/5 for all capable models indicates limited discriminative power.

- **The user proxy (GPT-4o) is highly idealized.** It has complete knowledge of the full issue, developer discussion hints, and file locations, and responds with perfect non-hallucinated answers. The paper acknowledges this limitation (Section 7) but the headline recovery numbers (up to 74% improvement, 80% of Full) are upper bounds that would likely degrade with a realistic user who has imperfect knowledge.

### Trivial

- The cosine distance metric (Section 5.1) does not fully specify which messages are included in the "cumulative knowledge after interaction" embedding (all interaction turns or only the first question-answer pair), though this is a minor implementation detail.
- Table 4 uses Wilcoxon signed-rank tests for paired binary outcomes; McNemar's test would be more directly appropriate for matched-pair binary data, though the practical impact is negligible given the large samples and very low p-values.

## Nice-to-Haves

- A direct detection probe where the model is explicitly asked to judge whether the task description contains sufficient information before any generation would cleanly separate detection from interaction propensity.
- A human evaluation of question quality on a sample of interactions would validate the LLM-as-judge metric.
- An ablation study where the user proxy has incomplete knowledge (e.g., missing file locations) would help quantify how much the recovery rates depend on perfect user cooperation, making the results more realistic.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about SWE-Bench Verified comparison population being unclearly defined (Section 2.1):** The paper explicitly states that SWE-Bench Verified was pruned to remove underspecified issues and that naturally underspecified issues are from the *original* SWE-Bench. The comparison is clearly defined, and the paper explains why natural underspecified issues are not used in experiments (lack of paired ground truth). This criticism reflects a misreading.

- **Criticism about how "navigational information acquired" is determined (Section 3.3):** The paper states "we measure the resolve rates separately for instances where the model asks for navigational details" — the measurement is clearly whether the model asks for file paths. This is a straightforward behavioral trace analysis.

- **Criticism about the three-turn detection limitation undermining FNR/FPR (Section 7):** The paper acknowledges this limitation explicitly and justifies it ("models rarely recover if they fail to engage early"). This is a reasonable design choice, not a flaw the paper ignores.

- **Pure formatting/style nitpicks:** Removed per instructions.

- **Criticism about §5.3's qualitative analysis being "post-hoc speculation":** The paper presents the qualitative analysis as interpretive and suggestive, clearly labeling it as analysis of patterns rather than causal claims. The Strength Finder's identified pattern analysis is more accurate here.

## Novel Insights

Beyond the paper's own contributions, the most striking emergent insight from this review is the deep tension between *competence* and *interactivity* in current LLM agents. Qwen 3 Coder performs near Claude Sonnet 4 on standard SWE-Bench coding metrics, yet has a 100% failure rate to interact under any prompt condition — revealing that the training paradigm that produces strong coding performance may actively suppress interactive behavior. Claude Sonnet 4, by contrast, achieves both strong standalone coding and strong interaction. This suggests that interaction capability is not a natural byproduct of improving general task-solving ability; it may require explicit training interventions. The finding that Qwen 3 Coder's performance actually *worsens* after receiving navigational information (Table 1) — because it robotically re-discovers information the user already provided — further illustrates how "protocol following" can actively interfere with effective interaction, even when the model has the relevant information.

## Suggestions

- Reframe RQ2 explicitly as measuring "proactive clarification behavior" or "interaction propensity under underspecification" rather than "detection." Add a supplementary experiment where models are directly asked to rate task completeness to validate the behavioral measure.
- Acknowledge more prominently that the Full setting includes developer discussion hints (not just the original issue) and discuss how this affects interpretation of the recovery metric.
- Add a human baseline or human validation of question quality on a subset to ground the LLM-as-judge scores.
- Characterize the types and counts of information gaps per Ambig-SWE issue to substantiate the "multiple interdependent gaps" claim with evidence.

## Score and Decision

**Calibration anchors (all retrieved in batch search):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/.../0xpakqqTbe.md` (RExBench) | 3.00 | Weaker: only 12 tasks, loose evaluation metric; this paper has 500 instances and rigorous SWE-Bench evaluation |
| `/home/.../R40rS2afQ3.md` (SWE-Bench+) | 3.00 | Weaker: engineering contribution fixing existing benchmark without conceptual novelty; this paper has more novel problem formulation |
| `/home/.../dc8ebScygC.md` (Structured Uncertainty) | 3.50 | Weaker: three loosely-connected sub-papers with poor presentation; this paper is more coherent and better organized |
| `/home/.../GAh52Zncfk.md` (CLARA) | 3.00 | Weaker: small-scale evaluation (200-364 instances) with limited performance; this paper has larger scale and more thorough evaluation |
| `/home/.../IKnuyyPHCV.md` (RECODE-H) | 4.50 | Comparable: both propose interaction-focused benchmarks; this paper has larger scale (500 vs 102 tasks) but RECODE-H has more realistic feedback modeling |
| `/home/.../qBcHWGBnIb.md` (AutoExperiment) | 5.00 | Comparable: both propose coding-agent benchmarks; this paper has larger scale but AutoExperiment's masking design is cleaner. This paper scores slightly higher due to richer three-part analysis |
| `/home/.../ftLqH4tgrh.md` (Dialogue as Discovery) | 5.00 | Similar level: both study interaction under uncertainty. That paper has a trained method; this paper is more diagnostic. This paper has better empirical coverage |
| `/home/.../x54wwB6QvL.md` (Scaling Laws Revisited) | 6.00 | Stronger: more rigorous theoretical contribution with validated scaling law; this paper is more empirical/diagnostic |
| `/home/.../3YKeB9R1g9.md` (Scaling with Collapse) | 8.00 | Much stronger: theoretical contribution with elegant scaling law derivation and thorough experiments; this paper does not aim for this level of theoretical depth |

The paper has a genuine contribution — a controlled benchmark for studying interactive handling of underspecification, a clean three-part decomposition, and interesting comparative findings across six models — but the RQ2 detection experiment has a significant confound (interaction behavior ≠ detection capability) that affects one of the paper's central claims. The Full setting's inclusion of developer discussion hints also slightly inflates the recovery narrative. These issues are addressable in revision but need attention. Relative to the calibration anchors, the paper is clearly stronger than the 3.0–4.0 papers (which had fundamental flaws or minimal scale) and comparable to the ~5.0 accepted benchmarks, with the RQ2 confound being the primary factor preventing a higher score.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>