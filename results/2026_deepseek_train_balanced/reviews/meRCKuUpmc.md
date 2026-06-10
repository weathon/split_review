## Summary

This paper introduces Seer, an end-to-end Predictive Inverse Dynamics Model (PIDM) that jointly optimizes conditional visual foresight (predicting future RGB frames) and inverse dynamics prediction (inferring actions) within a single Transformer architecture. Pre-trained on large-scale robot datasets like DROID and fine-tuned on downstream tasks, Seer is evaluated on LIBERO-LONG, CALVIN ABC-D, and four real-world tasks, showing consistent improvements over several baselines. The key architectural contribution is a unidirectional attention mask that enables the action token [INV] to attend to the foresight token [FRS], allowing end-to-end training of vision and action.

## Strengths

- **End-to-end PIDM outperforms two-stage PIDM on a direct comparison**: The paper explicitly compares Seer against Susie (a two-stage PIDM) on CALVIN ABC-D and reports that Seer surpasses it "by a large margin" (Table 2, Section 4.2). This provides direct empirical evidence that the paper's central architectural innovation—closing the vision-action loop end-to-end—yields better performance than the two-stage pipeline.

- **Large and consistent gains across three distinct evaluation settings**: The pre-trained Seer shows strong results on LIBERO-LONG (outperforming OpenVLA while using only 4% of its parameters), on CALVIN ABC-D (achieving the highest average task completion length), and on four real-world tasks (78.4% average success vs. the next-best baseline at 45.0%). The margin is consistent across simulation and reality.

- **Quantified data efficiency with clear baselines**: Section 4.3 (Figure 3) shows that with only 10% of fine-tuning data, Seer achieves a 187% relative improvement on LIBERO-LONG and a 150% relative improvement on CALVIN ABC-D compared to training from scratch. It requires only 70% of LIBERO-LONG data and 40% of CALVIN data to surpass prior SOTA baselines.

- **Ablation studies isolate the contribution of each loss component**: Table 3a ablates fine-tuning objectives and Table 3b ablates pre-training objectives, showing that neither conditional visual foresight nor inverse dynamics alone matches the combination, and the synergy holds in both phases.

- **Systematic robustness evaluation across four categories of visual disturbance**: Section 5.3 (Figure 5) tests Seer under novel object colors, novel objects with different physical properties, strong artificial lighting, and natural cluttered backgrounds. The pre-trained policy consistently improves over the from-scratch version in all four scenarios.

- **Parameter efficiency relative to VLM-based policies**: Seer (316M parameters) uses only 4% of OpenVLA's 7B parameters yet achieves a 62% relative improvement on LIBERO-LONG, a practical advantage for real-world deployment.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent reporting of headline quantitative improvements across abstract, introduction, and body**: The abstract claims "improvements of 13% on the LIBERO-LONG benchmark, 22% on CALVIN ABC-D, and 43% in real-world tasks." The introduction (line 16) states a "10.4% improvement in success rate and a 0.71 increase in average task completion length" without specifying which benchmark. Section 4.2 reports a 9% improvement from pre-training on LIBERO-LONG. Section 5.2 reports that Seer improves "from 60.0% to 78.4%" on real-world tasks — an absolute improvement of 18.4pp or a relative improvement of ~30.7%, neither matching the abstract's 43%. It appears the abstract uses different comparison bases (perhaps relative to different baselines) than the body, but this is never clarified. A reader cannot determine which numbers to trust or how they are computed. This is a transparency issue that undermines confidence in the paper's headline results. The authors should state the basis (absolute vs. relative, versus which baseline) for every percentage consistently across the entire paper.

### Minor

- **Missing strong contemporary baseline**: The paper does not compare against **Diffusion Policy** (Chi et al., 2023), one of the most widely-used strong baselines for both simulation and real-world robot manipulation. While OpenVLA, GR-1, and Susie are included, the absence of Diffusion Policy weakens the claim to state-of-the-art performance. This is a notable gap but not fatal given the other strong baselines.

- **Real-world evaluation protocol inflates absolute numbers**: Section 5.1 states "Each method is allowed three executions per trial, with the mean performance reported." This protocol gives each method three attempts per trial (45 attempts per task per method). While all methods are evaluated under the same protocol (so relative comparisons are valid), the absolute success rates are not comparable to the broader literature where single-attempt success is standard. The paper should report first-attempt success rates separately.

- **Overstated "first" claim**: The paper states (line 14) "our approach is the first to optimize vision and action in an end-to-end manner." This is questionable given that GR-1 (Wu et al., 2024), which the paper cites and compares against, uses generative video pre-training jointly with action prediction. The paper's distinction between two-stage and end-to-end PIDM is valid, but the "first" claim needs more careful qualification.

- **Design choice for handling missing language instructions is not ablated**: Section 3.4 mentions that when language instructions are missing during pre-training, "the robot state token at the future time step t+n+1 acts as a goal." This design choice is described briefly and its effectiveness is not validated through any ablation. A reader cannot tell whether this mechanism meaningfully contributes to the results or is a neutral design detail.

- **CALVIN generalization claims are overstated**: The CALVIN ABC-D setup pre-trains on play data from environments A, B, C and evaluates in environment D. While the visual appearance differs, all four environments share the same simulator, objects, task semantics, and action space. The paper frames this as evidence of handling "visual appearance variation," but it does not demonstrate genuine cross-domain or cross-robot generalization. The real-world DROID experiments partially address this, but the CALVIN results should be contextualized more carefully.

### Trivial

- **"6 downstream tasks" vs. 4 real-world tasks mismatch**: The conclusion (line 179) states "we only evaluate 6 downstream tasks," but the paper evaluates only 4 real-world tasks. If "6" includes the 2 simulation benchmarks, those are multi-task benchmarks (10 and 34 tasks respectively), not single tasks. This imprecision in describing the evaluation scope is confusing.

## Nice-to-Haves

- Report first-attempt success rates in addition to the three-attempt protocol for real-world experiments, to improve comparability with the broader literature.
- Report inference speed / latency numbers, which are important for real-time robotic control.
- Ablate the design choice of using future robot states as a goal when language is missing, to validate whether this mechanism matters.
- Add Diffusion Policy as a baseline to strengthen the SOTA claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Asymmetric camera advantage for Seer**: The critic claimed Seer's two-camera setup gives it an unfair advantage over baselines. The paper describes a single unified experimental hardware setup; all methods use the same cameras. Only OpenVLA is noted as being limited to a single camera, and the paper acknowledges this (line 160–161). This is not a design flaw in the paper's evaluation.
- **Questions about "mean performance" computation for binary success**: The paper defines Success Rate as "100% only upon successful completion of the entire task," making each execution binary. The mean across 3 executions per trial is therefore clearly a fraction (0%, 33.3%, 66.7%, or 100%). No ambiguity.
- **Reproducibility complaints about missing hyperparameters**: These (learning rate, batch size, etc.) would be in the appendix, which is stripped by the parser.
- **Speculation that baselines are differentially affected by the three-attempt protocol**: This is pure conjecture with no evidence from the paper and does not constitute a verifiable weakness.
- **Request for cross-embodiment evaluation**: The paper explicitly acknowledges this as a limitation in the conclusion. Criticizing an acknowledged limitation is a generic requirement that goes beyond the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Harmonize all reported percentage gains**: State the comparison basis (absolute vs. relative, versus which baseline/metric) for every number in the abstract, introduction, and results sections so they are mutually consistent and unambiguous.
2. **Add Diffusion Policy as a baseline** to the LIBERO-LONG and/or real-world comparisons to strengthen the SOTA claim.
3. **Report first-attempt success rates** for the real-world experiments alongside the three-attempt metric.
4. **Add an ablation** validating the design choice of using future robot states as a goal when language instructions are missing.
5. **Soften the "first" claim** (line 14) to acknowledge prior end-to-end vision-and-action training approaches such as GR-1.
6. **Fix the "6 downstream tasks" language** in the conclusion to accurately reflect the evaluation scope.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>