## Summary
The paper introduces PbP, a simulated embodied benchmark for preference-based planning, where agents observe a few demonstrations and must infer a user preference to plan in a new setup. Its main concrete contribution is a structured dataset/environment with 290 manually defined preference primitives across action-, option-, and sequence-level preferences, 15,000 egocentric video instances, and 50 simulated scenes, together with evaluations of video/multimodal and symbolic/LLM baselines.

## Strengths
- **Concrete benchmark scale and structure.** The paper defines a three-level preference hierarchy—action, option, and sequence level—and reports 290 unique preferences: 75 action-level, 135 option-level, and 80 sequence-level, with 15,000 egocentric video instances across 50 OmniGibson scenes. This is a specific and potentially useful dataset contribution.
- **Broader scope than narrow rearrangement-only personalization.** Section 3.1 includes preferences over fine-grained actions, alternatives among subtasks/objects, and temporal ordering, which gives the benchmark broader coverage than only object placement or rearrangement.
- **Demonstration/test construction attempts to test contextual transfer.** Section 3.2 states that demonstrations paired with a task “share the high-level preference but not exactly the same trajectory in terms of the objects selected or the scene used,” and Section 5.4 further compares same-room/same-object “direct” cases with generalized cases. This is a valuable diagnostic direction.
- **The paper evaluates both perceptual and symbolic inputs.** Section 4.2 includes video/multimodal models such as ViViT, LLaVA-NeXT, EILEV, and GPT-4V, as well as action-sequence/symbolic models such as DAG-Opt, Llama3-8B, and GPT-4. Even though the comparisons are confounded, the range of tested model classes is useful for identifying perception versus high-level reasoning bottlenecks.
- **The results identify a plausible bottleneck.** The contrast between poor end-to-end performance and much better performance when explicit preference labels are available suggests that current models struggle to infer the latent preference from demonstrations, while planning from an explicit semantic preference is easier.

## Weaknesses

### Fatal
None. The paper is a real benchmark contribution, but its claims and evaluation are substantially stronger than what the current evidence supports.

### Major
- **The paper overstates “human preference” evidence given that PbP uses manually defined labels and rule-generated demonstrations rather than observed human preferences.** Section 3.2 explicitly says, “Instead of recruiting human subjects,” the authors sample preference primitives and generate demonstrations with a manually designed rule-based planner. The limitation section also acknowledges that “human-defined preference labels may not fully encapsulate the intricacies and diversity of human preferences.” This is acceptable for a synthetic latent-preference benchmark, but it does not justify repeated claims that the benchmark demonstrates learning human behaviors, individual user needs, user satisfaction, or real personalized assistance. The central contribution should be framed as synthetic preference-rule inference/planning, not as validated human preference learning.
- **The two-stage results do not clearly establish that learned preferences improve planning.** Section 4.1 says the two-stage setting trains models to predict preference labels and then uses predicted labels for action prediction, while Section 5.3 says that in the second stage models generate actions using “the current preference label” and that “preference tokens are semantic enough to be translated into primitive actions.” Figure 5 states that models are provided with predicted preference labels, but the text also describes explicit preference labels. This ambiguity matters: if ground-truth labels are used, the second-stage result is an oracle-label planning experiment; if predicted labels are used, the near-zero planning distance for GPT-4V/GPT-4 is hard to reconcile with the much lower preference-prediction accuracies reported in Table 2. The paper needs a clear cascaded evaluation showing preference prediction followed by planning under prediction errors.
- **The main planning metric measures imitation of one simulator-generated trace rather than preference satisfaction or task success.** Section 5.2 uses Levenshtein distance between generated and ground-truth action sequences, treating each action as a token. This is a reasonable diagnostic for sequence imitation, but preference-conditioned embodied tasks often admit multiple valid action orders or equivalent plans. A model could satisfy the preference while receiving a poor edit-distance score, or match the script while not demonstrating robust preference understanding. Since the main planning claims rely on this metric, the evaluation does not fully measure the stated goal.
- **The modality comparisons conflate perception difficulty with reasoning/planning ability.** The paper compares video-based models using egocentric observations with symbolic/LLM models using action sequences. Section 4.2 explicitly notes that action input is a “high-level abstraction of the egocentric video, reducing the complexity associated with visual data.” Therefore, conclusions such as “symbol-based approaches show promise” and “symbol-based reasoning demonstrates robustness across diverse environments and objects” are partly expected from the easier input representation. This does not invalidate the symbolic results, but it weakens claims that symbolic methods are intrinsically more effective or generalizable.
- **The few-shot preference-learning claim is under-specified in the main text.** The paper frames PbP as few-shot learning from demonstrations, but the described setup appears to involve prediction over a fixed vocabulary of 290 predefined labels. The main text does not make clear whether preferences themselves are held out, whether train/test splits share the same preference labels, how many examples per preference are available, or whether evaluation is closed-vocabulary classification over seen primitives. If the latter, the task is weaker than inferring a new user’s previously unseen preference from a few examples.

### Minor
- **The preference hierarchy is useful but not fully formalized.** Some examples, such as desired water amount or bookshelf level, can be interpreted as task parameters or hidden instructions rather than “preferences” in a stronger psychological/personalization sense. This does not undermine the benchmark, but it contributes to the overclaiming problem and should be clarified.
- **The ablation in Table 3 is informative but somewhat hard to interpret.** The ablation removes demonstrations and supplies the test sequence to predict the preference. That may test post-hoc recognition of a preference from the target trajectory rather than the intended watch-and-help setting of observing prior demonstrations and planning in a new context.
- **Generalization analysis is suggestive but not deeply diagnostic.** Section 5.4’s direct-vs-generalized comparison is useful, but the analysis remains broad. It does not clearly separate failures due to object recognition, scene layout, action ambiguity, preference type, visual grounding, or planner artifacts.
- **The societal impact discussion is too dismissive.** The paper says it does not foresee negative societal impacts, while also discussing preference modeling in private domestic scenarios and future collection using head-worn devices. Privacy and surveillance concerns should be acknowledged.

### Trivial
None.

## Nice-to-Haves
- Add a small human-validation study to check whether the predefined primitives are perceived as plausible human preferences and whether generated demonstrations visibly convey the intended preference.
- Report repeated trials or uncertainty over demonstration sampling, since three-shot performance may depend strongly on which demonstrations are selected.
- Add preference-satisfaction or task-success evaluators based on final states, object states, temporal constraints, and preference-specific predicates, in addition to Levenshtein distance.
- Evaluate symbolic models under noisy or automatically extracted action annotations to see whether their advantage survives perception errors.
- Provide confusion matrices and per-level/per-type breakdowns to identify whether errors are semantically close, hierarchy-confused, or random.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Generic “important problem” strength.** The problem is indeed relevant, but generic importance alone is not a paper-specific strength, so I did not count it as a core strength.
- **Strength Finder claim that PbP “explicitly tests few-shot preference generalization rather than trajectory imitation.”** The construction encourages transfer across scenes/objects, but the evaluation still relies heavily on Levenshtein distance to a generated trajectory, so the stronger claim conflicts with a verified weakness.
- **Strength Finder claim that the two-stage evaluation directly proves preference is a useful learned intermediate abstraction.** The results do show that explicit semantic labels help planning, but ambiguity about predicted versus ground-truth labels prevents treating this as strong evidence for a complete learned preference pipeline.
- **Detailed complaints about missing implementation details such as complete prompt design, action vocabulary, or generation parameters.** These may be useful for reproducibility, but they may also be in omitted appendix material and are not central enough to weigh heavily.
- **Criticism of DAG-Opt as poorly motivated.** DAG-Opt may be a weak or imperfect baseline, but the paper does not rely solely on it, and the more important issue is the broader representation confound between symbolic and visual inputs.
- **Formatting, typo, or grammar issues.** Any such artifacts are ignored because the provided paper text is extracted from PDF and parser artifacts should not be penalized.

## Novel Insights
The main tension is that PbP is potentially valuable precisely because it provides a controllable synthetic latent-preference benchmark, but the paper weakens itself by presenting simulator-defined labels and rule-based traces as evidence about human preference learning. The strongest version of the paper would not claim to validate human personalization; it would instead argue that PbP isolates a key subproblem—inferring reusable latent task parameters from a few demonstrations—and then provide evaluation metrics that separate preference recognition, plan validity, and exact script imitation.

## Suggestions
- Reframe the contribution as a **synthetic latent-preference planning benchmark** unless real human demonstrations or human validation are added.
- Clearly state whether second-stage planning uses **ground-truth preference labels, predicted preference labels, or both**, and report cascaded two-stage performance with prediction errors propagated.
- Add metrics for **preference satisfaction and task completion**, not only Levenshtein distance to a single generated trajectory.
- Control modality comparisons by giving models matched abstractions: e.g., video models with extracted action captions, language models with noisy predicted action sequences, and symbolic models with perception-derived rather than oracle action inputs.
- Clarify train/test splits: whether preference labels are held out, whether scenes/objects are disjoint, how demonstrations are sampled, and whether the task is closed-vocabulary classification over the 290 primitives.
- Analyze failures by preference level, object/scene changes, and visual versus symbolic input to better explain where current models fail.

## Score and Decision

### Calibration anchors retrieved and comparison
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/T5QLRRHyL1.md` — avg score 7.00, Accept. PARTNR is a stronger embodied benchmark anchor: broader scale, clearer benchmark positioning, and more convincing validation, so PbP is below it.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pk4YjZeevI.md` — avg score 5.50, Reject. PREDICT is a close preference-inference anchor with synthetic/simplified environments and concerns about realism and baselines; PbP is similar in ambition but has stronger dataset scale and weaker metric/claim alignment.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/blwWIKpwpL.md` — avg score 5.50, Reject. Similar embodied preference-learning topic; PbP has a broader benchmark but comparable concerns around evaluation support.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CTlUHIKF71.md` — avg score 5.25, Accept. Preference-alignment robotics work; PbP is comparable in relevance but less convincing on human validation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NQTrARs2pz.md` — avg score 4.00, Reject. Embodied benchmark/system with limited evaluation and analysis; PbP is more coherent and broader, so it should score above this low anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/UiLtbLsiPU.md` — avg score 4.50, Reject. Embodied planning benchmark with concerns about evaluation; PbP is somewhat stronger due to its structured preference hierarchy but shares benchmark-validity issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2R7498e2Tx.md` — avg score 6.00, Accept. PersonalLLM is a stronger personalization benchmark anchor; PbP is below it because its “human preference” claims are less directly validated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nkCWKkSLyb.md` — avg score 5.50, Reject. Strong benchmark with overclaiming about automated preference metrics; similar pattern to PbP’s metric/claim mismatch.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9RLC0J2N9n.md` — avg score 4.50, Reject. Synthetic benchmark with broad claims from proxy tasks; PbP is similar but somewhat more useful and grounded in embodied simulation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Kz3yckpCN5.md` — avg score 7.00, Accept. Human preference/crowd evaluation anchor; PbP lacks comparable human validation, so it is well below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EwRxk3Ho1V.md` — avg score 4.25, Reject. Metric benchmark criticized for overclaiming and simplistic metric design; PbP’s Levenshtein evaluation weakness resembles this, but PbP has a stronger dataset contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1JgWwOW3EN.md` — avg score 2.50, Reject. Confounded multimodal benchmark with severe validity issues; PbP is substantially better.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/j0ZvKSNZiP.md` — avg score 6.00, Accept. Benchmark aligned to human ratings despite some overclaim concerns; PbP lacks human preference validation, so it is below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/n6mLhaBahJ.md` — avg score 6.75, Accept. Strong embodied decision-making benchmark; PbP is below due to less convincing evaluation validity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1bbPQShCT2.md` — avg score 6.50, Accept. Interactive physical reasoning benchmark; stronger benchmark validity than PbP.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1kFDrYCuSu.md` — avg score 6.67, Accept. Personalized reward modeling anchor; stronger empirical support for personalization than PbP.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iX1RjVQODj.md` — avg score 7.00, Accept. Human preference learning anchor; PbP is less direct and less validated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8NlUL0Cv1L.md` — avg score 6.25, Accept. Embodied planning under partial observation; PbP is below because its metric and modality comparisons are less controlled.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pRIPRDALBV.md` — avg score 5.50, Reject. Embodied open-world planning with moderate concerns; PbP is in a similar borderline-reject range.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Y4iaDU4yMi.md` — avg score 3.67, Reject. Weak embodied planning/preference RL anchor; PbP is better due to clearer benchmark contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pwKokorglv.md` — avg score 4.00, Reject. Embodied instruction-following/planning anchor with weak evaluation; PbP is above it.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Z1Va3Ue4GF.md` — avg score 4.00, Reject. Embodied long-horizon planning with memory/CoT; PbP is above it but still flawed.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/y15LAM4u0A.md` — avg score 3.50, Reject. Weak embodied benchmarking platform; PbP is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/o3jgyJIhnv.md` — avg score 4.00, Reject. Personalized decision-making benchmark anchor; PbP is somewhat stronger but shares concerns about personalization validity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3ZDMQGQgkE.md` — avg score 4.00, Reject. Personalized preference benchmark in recommendation; PbP is stronger in embodied scope but has similar validation concerns.

Relative to these anchors, PbP is clearly stronger than the low-scoring embodied benchmark papers around 3.5–4.0 because it has a coherent dataset design, multiple preference levels, and a reasonable set of baseline evaluations. However, it is below the accepted 6–7 benchmark papers because its central claims are overextended, the main metric is not aligned with preference satisfaction, and the two-stage evidence is ambiguous. It is closest to the 5–5.5 range of synthetic/preference benchmark papers with useful ideas but significant evaluation and framing issues.

**Final score: 5.0 / 10. Decision: Reject.**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>