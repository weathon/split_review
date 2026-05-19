- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces SPACE, a benchmark for evaluating spatial cognition in LLMs and VLMs, grounded in decades of cognitive science research. It covers both large-scale (environment-level navigation and mapping) and small-scale (object-level shape/space reasoning) tasks, with parallel text and image presentations enabling evaluation of both model types. The authors evaluate a range of frontier models and find systematic failure: near-chance performance on large-scale tasks, and strong performance only on text-based working memory tasks. The benchmark itself is the paper's core contribution.

## Strengths

- **Systematic adaptation of established cognitive-science tasks into an AI benchmark.** The benchmark draws directly on classic protocols — Tolman's novel-shortcut discovery, Vandenberg & Kuse's mental rotation, the Corsi block-tapping test, the Cambridge Spatial Working Memory test — grounding the evaluation in decades of construct-validated spatial cognition research. This provides far stronger construct validity than ad-hoc spatial VQA benchmarks.

- **Matched dual-modality design.** For nearly every task, the paper provides both an image-based multimodal presentation and a purely textual character-array presentation. This enables direct cross-modal comparison of the same underlying spatial ability — a capability absent from most prior benchmarks, which test only one modality.

- **Compelling evidence of systematic failure.** Across all models and tasks, the results are striking and clear. With egocentric multimodal presentation (the closest counterpart to animal navigation experiments), GPT-4o averages 23.0% (chance 15.0%). Even with an allocentric BEV-image view, the best model reaches only 28.8%. On image-based mental rotation, perspective taking, maze completion, and the Minnesota Paper Form Board Test, all models are near chance. These results are clean, systematic, and directly support the paper's central claim.

- **Rigorous evaluation design.** The use of multiple trials with standard deviations, three observation spaces for large-scale tasks (ego image, BEV image, BEV text), the SPL metric for interactive navigation tasks, and the inclusion of chance baselines all demonstrate careful experimental methodology.

- **Inclusion of clinical neuropsychological tests.** Tasks like the Corsi block-tapping test, Spatial Addition (WMS-IV), and Cambridge Spatial Working Memory test are standard clinical measures of visuospatial working memory, rarely used in AI benchmarks, broadening the evaluation's diagnostic scope.

## Weaknesses

### Fatal
None.

### Major

- **Human performance baselines lack methodological documentation.** The paper reports human accuracy numbers in every table (e.g., 78.5% on MRT, 82.8% on direction estimation) and uses these to contextualize model results — even coloring model results relative to "50% of human performance." However, the paper provides no description whatsoever of how these human data were collected: no participant demographics, no administration procedure (online/lab?), no number of trials per condition, and no statement on whether the data come from the authors' own experiments on the exact benchmark items or from the cognitive science literature using different stimuli. This is a significant documentation gap in a benchmark paper that explicitly draws human-model comparisons. The core claim ("models fall short of spatial intelligence in animals") is supported primarily by near-chance performance and does not collapse without human baselines, but the prominence given to these numbers demands methodological transparency. A rigorous human evaluation on the actual benchmark items — even on a representative subset — would significantly strengthen the paper.

### Minor

- **Multimodal large-scale evaluation is limited to two closed-source models.** On the ego-image and BEV-image observation spaces, only GPT-4v and GPT-4o are evaluated. The paper notes this is because they "support video understanding (via a succession of images)." While the interactive tasks (route retracing, novel shortcuts) genuinely require sequential input, the non-interactive large-scale tasks (direction/distance estimation, map sketching) could be evaluated with static images from the walkthrough — allowing evaluation of more VLMs. The generality of the large-scale multimodal results rests on just two API-access models from the same provider.

- **No statistical significance testing.** The paper reports means and standard deviations but does not test whether model performance is statistically significantly above chance or whether differences between models are reliable. For example, GPT-4o at 32.0% on direction estimation (ego image) with σ=4.1 is within ~1.7σ of the 25% chance baseline — is this reliably above chance? A t-test, bootstrap, or confidence interval would clarify.

- **CSWM chance baseline calculation is not explained.** The chance baseline for the Cambridge Spatial Working Memory test is listed at 33.0–33.8% across conditions, but the task has varying numbers of boxes (N=3–7) and an interactive search process. The paper only states that "the chance baseline samples an action at random in each step," which does not transparently yield the stated numbers. The calculation should be explicitly shown for reproducibility.

- **SPL metric without separate success rate.** The interactive navigation tasks (route retracing, novel shortcuts) are evaluated using SPL, which conflates success and path efficiency. Without a reported success rate, it is impossible to tell whether low SPL values (e.g., GPT-4o at 6.6 on ego-image route retracing) reflect failure to reach the goal, or reaching it via long detours. Reporting success rate alongside SPL would improve interpretability.

- **Framing overstates the animal-cognition connection.** The abstract describes the tasks as "classic tests of animal cognition," but the actual implementations are multiple-choice QA on rendered 2D images or text arrays — far removed from the original embodied navigation experiments with rats, chimpanzees, or wolves. The paper is better described as evaluating spatial cognition *inspired by* cognitive science (including human cognitive tests), rather than directly administering "tests of animal cognition." The claim is not false, but the rhetorical framing could mislead readers about the construct being measured.

### Trivial
- The caption of Table 2 uses "textural" instead of "textual" ("purely textural presentations").

## Nice-to-Haves
- **Qualitative error analysis.** Understanding *how* models fail on tasks like mental rotation (e.g., mirror-image confusions vs. rotation-magnitude errors) or perspective taking would make the benchmark more diagnostic and is a natural next step.
- **Reliability analysis.** Reporting internal consistency (e.g., split-half reliability) across items within each task would demonstrate that the benchmark produces stable measurements.
- **Cross-modal fairness discussion.** The text-only implementations of some tasks (e.g., MRT using 2D arrays instead of 3D rotations) are qualitatively different from their visual counterparts. The paper acknowledges this but does not discuss how it affects the fairness of cross-modal comparisons.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **OOM marking issue** (from Harsh Critic): The critic claimed models that ran out of memory "should be clearly marked as 'OOM'" — but this IS already done (OOM is shown in the table cells and the caption explains the treatment). Factually inaccurate criticism.
- **Released materials** (from Harsh Critic): Requesting that the paper state it will release the benchmark. Hard rule: do not question release status of cited artifacts.
- **Maze completion and CSWM OOM averaging** (from Harsh Critic): The paper's caption already states "their accuracy is taken to be 0 for the calculation of average performance" and marks averages with asterisks. Already addressed.
- **Missing appendix content** (from Harsh Critic and Section-by-Section Notes): The parser strips appendix sections from all papers. Do not penalize content that exists in the original submission.
- **Generic concerns about "could be a proxy" / "confounders may exist"** (from Harsh Critic's area sweep): Speculative without concrete anchor in the paper.
- **Strength Finder generic strengths** — e.g., "this paper addressed an important problem" — removed as superficial.

## Novel Insights
None beyond the paper's own contributions. Both reviews largely converge on the same observations: the benchmark is well-designed and grounded, the results are impactful, and the main weakness is the lack of documented human baseline methodology. The most interesting emergent point from the reviewers is that the paper's central claim does not strictly depend on the human baselines (the near-chance performance alone suffices), but the paper itself foregrounds the human comparison, making the documentation gap more consequential than it might otherwise be.

## Suggestions

1. **Document human baseline methodology** — or better, conduct a proper human evaluation on a representative subset of the benchmark tasks (e.g., all multiple-choice QA tasks) and report participants, procedure, and per-task results transparently.
2. **Expand multimodal large-scale evaluation** by evaluating additional VLMs on the non-interactive large-scale tasks (direction/distance estimation, map sketching) using static images from the walkthrough familiarization, for which sequential video understanding is not strictly necessary.
3. **Add statistical significance tests** comparing model performance to chance and to human performance where applicable.
4. **Report success rate alongside SPL** for interactive navigation tasks.
5. **Calibrate the animal-cognition framing** — describe the tasks as "inspired by cognitive science including animal and human studies" rather than "classic tests of animal cognition."
6. **Explain the CSWM chance baseline calculation** explicitly to aid reproducibility.
