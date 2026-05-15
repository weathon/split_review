Now I have thoroughly verified the claims against the paper. Let me produce the consolidated review.

## Summary

This paper introduces S3E, a pipeline that translates symbolic predicates from PDDL task domains into natural language questions and uses a pre-trained Vision-Language Model (LLaVA OV) to answer them via VQA, enabling zero-shot symbolic state estimation without hand-coded sensing functions. The authors analyze S3E as a multi-label classifier, identify two types of uncertainty (model uncertainty and task ambiguity), and propose low-effort mitigations through environment design (home pose) and natural-language instructions. Experiments in simulated and real-world pick-and-place settings show that a 72B model can achieve over 90% average precision.

## Strengths

- **First zero-shot symbolic state estimator using VLMs, eliminating hand-crafted functions.** The paper introduces a clean pipeline (predicate translation → natural-language questioning → VQA) that requires no task-specific coding, exploration, or training beyond the pre-trained VLM. Prior VLM-based approaches (Chen et al., 2024a; Duan et al., 2024b) require external success indicators or task-specific scene representations; S3E distinguishes itself as a general-purpose replacement that interfaces directly with symbolic domain descriptions (Section 4, Section 2).

- **Novel identification and mitigation of two distinct uncertainty types.** The paper distinguishes model uncertainty (training distribution mismatches) from task uncertainty (ambiguous predicate definitions) and demonstrates concrete, low-overhead mitigation strategies — a robot "home pose" to disambiguate gripping, and natural-language instructions describing object appearance. These improve macro AP by up to 22% for the 72B model (Table 1), providing actionable guidance for deploying VLMs in state estimation.

- **Rigorous multi-scale comparison across model sizes (0.5B, 7B, 72B) and modifications.** Table 1 systematically evaluates accuracy at three thresholds, micro/macro AP, and the impact of home-pose and instruction modifications across three model scales. This provides clear insight into how model capacity and prompt/environment design interact, showing that smaller models (0.5B, 7B) degrade with additional instructions while the 72B model substantially benefits.

- **Detailed per-predicate failure analysis.** Figure 7 breaks down AP for each grip predicate, revealing which objects the VLM struggles with (e.g., bread due to unrealistic 3D modeling) and how modifications differentially affect individual predicates. Figure 6 provides precision-recall curves, adding granularity beyond aggregate metrics.

- **Practical focus on open-source models and real-world deployment.** The use of LLaMA 3 and LLaVA OV (both freely available) and explicit discussion of GPU memory constraints (Section 6.1) ensure the method is accessible to the robotics community. The real-world experiment with a physical robot and single camera demonstrates applicability beyond simulation.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against any alternative state estimation baseline.** All experiments compare S3E only with itself (different model sizes, with/without modifications). The paper never benchmarks against even simple alternatives such as an object-detection + rule-based approach (e.g., YOLO + spatial heuristics), a directly prompted VLM like GPT-4V, or prior integrated pipelines (Duan et al., 2024b). The trivial "predict-all-false" baseline (Section 6.2) does not represent a real state estimator. Without this comparison, readers cannot assess whether S3E's framework-level contribution — the two-stage predicate translation pipeline — actually improves over simpler approaches, or whether a direct VQA prompt would perform as well. This gap substantially weakens the empirical support for the paper's central contribution claim.

- **Real-world evaluation lacks objective ground truth and is not reproducible.** The real-world experiment (Experiment 2, Section 6) determines ground truth by "manually check[ing] the results for each frame" (line 105). There is no inter-rater reliability measure, no precise localization system (motion capture, fiducial markers, QR codes), and no discussion of how ambiguous frames were resolved. The resulting AP scores (>99% for Mid-poses with 72B) are suspiciously high — higher than in simulation — and the paper acknowledges these are "approximate performance" measurements. This evaluation cannot independently validate the claim that S3E works reliably in practice; it is at best a qualitative demonstration. Given that the paper explicitly targets real-world applicability, this is a significant methodological gap.

### Minor

- **Translation stage (LLM predicate-to-question conversion) is not ablated.** The paper uses an LLM to convert grounded predicates to natural-language questions (Section 4) but never compares against manually written question templates. It is unclear whether this stage adds value over a simple deterministic template — the primary contribution of S3E could potentially be achieved without the LLM translation step.

- **Uncertainty classification is non-standard.** The paper classifies model uncertainty as aleatoric (Section 5, line 81), whereas standard ML terminology treats model uncertainty caused by limited training data as epistemic. While the paper acknowledges this ambiguity ("can be viewed as aleatoric... yet it can also be epistemic"), the chosen convention is somewhat confused. This does not invalidate the practical mitigation strategies but weakens the theoretical framing.

- **Simulation data generation details underspecified.** The paper states that "actions are implemented imperfectly" (line 99) to produce realistic states but does not specify the type, degree, or distribution of imperfections. This makes it difficult to assess whether the simulated evaluation reflects realistic failure modes or is biased toward certain kinds of errors.

- **Claim of "over 90% state estimation precision" conflates multiple metrics.** The abstract's "over 90% precision" combines results from different settings: the simulated result (91.1% micro AP with both modifications for 72B) and the real-world result (>99% AP for Mid-poses). The term "precision" is ambiguous — the paper uses Average Precision (AP), not standard precision, and the real-world >99% figure is on a subset of frames. A more precise framing would clarify these distinctions.

### Trivial

- The paper does not report the number of frames or data points used in the real-world experiment, making it difficult to assess statistical reliability.
- The "degree of imperfection" in simulated actions is not quantified.
- $\theta=0.5$ is used as the primary threshold without discussion; however, AP is threshold-agnostic and the paper does report accuracy at multiple thresholds, so this is a minor presentational concern.

## Nice-to-Haves

- Comparison against a directly-prompted VLM (e.g., GPT-4V with the same yes/no questions) would help isolate the value of S3E's predicate-translation pipeline from the VLM's raw capabilities.
- Calibration analysis (expected calibration error) for VLM output probabilities, since the paper treats them as confidence scores.
- A closed-loop planning experiment demonstrating that S3E's state estimates are reliable enough to trigger correct replanning.
- Domain generalization to at least one additional task (e.g., block-world from CLEVR, mentioned but not evaluated).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about "no task-specific coding" vs. task-specific design** (from Harsh Critic #3 Discussion/Conclusion): The paper explicitly distinguishes between *coding* (writing software) and *environment/prompt design* (home pose, instructions). The limitations section (line 169) acknowledges the need for visual input setup. This criticism misreads the paper's claims.
- **Criticism about contribution being overstated relative to prior work** (Harsh Critic #3): The paper's related work section (Section 2) provides clear distinctions — prior VLM-based approaches require external action success indicators (Chen et al., 2024a), task-specific scene representations (Duan et al., 2024b), or focus on action failure reasoning rather than state estimation (Duan et al., 2024a; Liu et al., 2023c). The claim of "first zero-shot symbolic state estimator" is adequately qualified and defensible.
- **Criticism about the "Instruct" modification hurting smaller models not being framed as a limitation**: The paper explicitly discusses this (lines 121-122: "Adding natural language instructions negatively impacts the 0.5B and 7B models, likely due to confusion from the additional context"). It is already documented.
- **Strength Finder strength #6** ("Detailed per-predicate analysis revealing failure modes and improvement") is kept — it is genuine and supported by Fig. 7/Fig. 6.

## Novel Insights

The most interesting observation across the reviews is the *asymmetric effect of instructions across model scales*: the "Instruct" modification consistently *hurts* the 0.5B and 7B models while *helping* the 72B model, sometimes substantially (macro AP gain of ~9% with Pose). This suggests that smaller VLMs are not merely less capable but are actively confused by additional context that larger models can leverage — a finding with implications for how practitioners should match prompt complexity to model capacity. The reviews do not surface any other insight that goes substantially beyond the paper's own discussion.

## Suggestions

1. **Add baselines.** At minimum, compare against: (a) a detection + spatial-heuristic state estimator using YOLO or similar, and (b) directly prompting the same VLM with a single prompt containing all predicate questions (removing the translation stage) to isolate S3E's pipeline contribution.
2. **Strengthen real-world evaluation.** Use objective ground truth (e.g., fiducial markers, motion capture, or a second human annotator with inter-rater reliability) for the real-world experiment. Report the number of frames and per-predicate breakdown as in the simulated experiment.
3. **Ablate the LLM translation stage.** Compare LLM-generated questions against hand-written templates to justify this component.
4. **Quantify simulation imperfections.** Specify the type and distribution of action imperfections used for data generation.
5. **Discuss calibration.** Report expected calibration error for VLM output probabilities, or at minimum acknowledge that treating VLM logits as calibrated probabilities requires validation.

## Score and Decision

**Originality**: 7/10 — First zero-shot VLM-based symbolic state estimator; the pipeline is clean and well-motivated.  
**Importance of research question**: 8/10 — Replacing hand-crafted state estimation is a real bottleneck in task planning.  
**Claims support**: 5/10 — Core claims are partially supported by simulation but undermined by missing baselines and weak real-world validation.  
**Soundness of experiments**: 5/10 — Simulated experiments are reasonably thorough internally; real-world experiment is not reproducible.  
**Clarity of writing**: 7/10 — Well-structured and readable; some abstraction/conflation issues.  
**Value to community**: 6/10 — The idea is practically useful and timely, but the empirical evidence needs strengthening before it becomes a reliable reference.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>