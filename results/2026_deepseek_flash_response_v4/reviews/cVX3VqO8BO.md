Now I have sufficient calibration data. Let me synthesize my findings.

**Round 1 bracket:** The paper clearly sits in the middle band (3.5–7.5). It is substantially stronger than the low-band papers (2.5–3.33) and does not approach the completeness of high-band papers (8.0).

**Round 2 narrowing:** The most comparable anchors are:
- Cross-Embodiment Dexterous Grasping (5.00, Accept): tests its core cross-embodiment claim, but limited real-world evaluation
- HandsOnVLM (6.33, Reject): similar VLM+hand interaction but with weak baselines
- CrayonRobo (5.20, Reject): solid method but concerns about evaluation completeness
- LAPA (5.83, Accept): better evaluated, stronger methodology

UniHM is comparable to the ~5.0 anchors — it has a coherent pipeline and real-world validation, but the untested cross-morphology claim, underspecified real-world evaluation, and missing HOIGPT comparison are significant gaps that prevent a strong recommendation for acceptance without major revisions.

Here is the final consolidated review:

## Summary

UniHM proposes a framework for generating sequential dexterous hand manipulation sequences conditioned on open-vocabulary language instructions. It combines three components: (1) a shared VQ-VAE codebook designed to work across multiple hand morphologies, (2) a VLM (Qwen3-0.6B) for instruction-conditioned token sequence generation, and (3) a physics-guided trajectory refinement optimization. The method is trained on existing HOI datasets (DexYCB, OakInk) and evaluated in both simulation and real-world settings.

## Strengths

1. **Well-specified physics-guided dynamic refinement** (Section 3.4, Eq. 11–18): The paper develops a principled Gauss-Newton optimization with contact energy, generative HOI prior, and temporal smoothness prior. The ablation study (Table 4) confirms that removing this refinement degrades MPJPE from 61.40→65.78 (seen) and FPL from 12.15→15.35, showing it provides measurable benefit.

2. **Real-world success rate improvements over baselines** (Table 3): UniHM achieves substantially higher success rates than the compared baselines across all four task types (e.g., 65% vs. 30% on seen Grab, 55% vs. 15% on unseen Pull&Push). This provides direct evidence that the generated sequences are physically executable.

3. **Progressive masking curriculum for sequence generation** (Section 4.4): The training strategy that gradually increases the masking ratio from 0 to 1 reduces exposure bias. The ablation shows it improves MPJPE from 73.41→61.40 on seen and 74.63→63.56 on unseen DexYCB, validating the design.

4. **Decoupled architecture for data efficiency** (Section 3.3): The separation of scene perception (CLIPort) from HOI sequence generation (VLM) means only the perception module needs adaptation when the scene distribution changes. This is a practical design choice that addresses the data-scarcity challenge.

## Weaknesses

### Fatal
None.

### Major

1. **Cross-morphology tokenizer is claimed as a central contribution but never evaluated for cross-morphology transfer.** Section 3.2 introduces a cross-morphology codebook with distillation-based encoder alignment and hand pose translation (Eq. 6), presented as enabling "direct token reuse and transfer across robotic and anthropomorphic hands." However, all quantitative experiments (Tables 1, 2, 4) evaluate only on DexYCB and OakInk, which use MANO hand annotations. The real-world experiments (Table 3) use a single unspecified dexterous hand. There is no experiment showing translation between different hand morphologies (e.g., MANO→Shadow Hand, Shadow→Allegro). Since the cross-morphology codebook is arguably the paper's most distinctive technical contribution, this evaluation gap is significant.

2. **Real-world evaluation is critically underspecified.** Table 3 reports success rates but omits: the specific dexterous hand used, the number of trials per condition, confidence intervals, the objects tested, and how success is adjudicated. Without these details, it is impossible to assess whether the reported numbers reflect a genuine advance or could be within the noise of small trial counts against weak baselines.

3. **Missing comparison against HOIGPT (Huang et al., 2025).** The Related Work section cites HOIGPT as a method that "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences" — this is directly relevant to UniHM's stated task of language-conditioned sequential hand-object interaction. The paper dismisses it alongside other methods as targeting "Digital Hand, low-DoF grippers, or static grasp poses" but provides no evidence for this characterization. A comparison against HOIGPT (or a clear explanation of why it cannot be compared) is needed to substantiate the paper's claims relative to the closest prior work.

### Minor

4. **Diversity scores are substantially below ground truth without discussion.** On DexYCB, GT Diversity is 125.53 while UniHM achieves only 39.62 (seen) and 42.70 (unseen). The paper notes "Diversity closer to the ground truth indicates a more reasonable generation" but does not discuss why its generations are far less diverse than the training data, or whether this indicates mode collapse.

5. **"First" claim requires qualification.** The paper repeatedly claims to be "the first" framework for dynamic language-guided dexterous manipulation, but HOIGPT — cited in the paper's own Related Work — performs text-conditioned HOI sequence generation. While UniHM differs in targeting robot hand morphologies and incorporating physics refinement, the "first" framing should be more carefully scoped.

6. **Key hyperparameters are missing.** The paper specifies codebook size K and latent dimension d_z in the formulation but never states their values. Other missing details include: encoder/decoder architectures, training hyperparameters, the masking schedule, Gauss-Newton solver parameters, and energy weight values.

7. **Seen/unseen split tests limited generalization.** The 80/20 split on DexYCB and OakInk separates different object instances from the same categories, testing category-level generalization rather than true open-world generalization to novel categories. The claim of "strong generalization" should be tempered accordingly.

### Trivial

8. **VLM model scale is not ablated.** The paper uses Qwen3-0.6B with the motivation that larger models are "data-inefficient," but no experiment tests whether a larger VLM would improve results.

## Nice-to-Haves
- Failure analysis of real-world attempts (35–65% fail; understanding why would strengthen the contribution)
- Ablation of the shared codebook (train separate per-hand models and compare)
- Runtime/computational cost analysis for practical applicability

## Removed Points

These points were identified in the source reviews but filtered per the merger guidelines:

- **Criticism about baselines being unfair because of asymmetric physics post-processing**: The paper applies physics-guided refinement to baseline outputs as well, which if anything favors the baselines (not the author's method). The core concern — that the baselines are human motion methods rather than dexterous grasping methods — is retained in Major #3 (specific to HOIGPT). The sweeping claim that "SemGrasp, AffordDexGrasp, Multi-GraspLLM should be baselines" is removed; these methods produce static grasps, not sequences, so comparing against them for a sequential task would not be informative.

- **Criticism about "learning from video" framing being misleading**: Minor overstatement about training data source. The paper trains on 3D-annotated HOI datasets (not raw video), but the claim about "eliminating teleoperation data" is accurate since these are existing public datasets. Does not affect core claims.

- **Criticism about MPJPE/FOL/FPL metrics being poorly motivated**: Generic criticism applicable to much of this research area. The paper also uses Success Rate as a complementary metric. Removed as not specific enough to this paper.

- **Strength about morphology-agnostic codebook being "confirmed by ablation"**: The ablation does not evaluate cross-morphology transfer, so this strength overclaims. The formulation remains a valid contribution but is weakened by the evaluation gap noted in Major #1.

## Novel Insights

None beyond the paper's own contributions. The reviews surface legitimate concerns about evaluation completeness but do not generate new conceptual understanding of the problem.

## Suggestions

1. Add a cross-morphology transfer experiment: train on MANO data and evaluate reconstruction/task success on Shadow Hand, Allegro Hand, etc.
2. Provide full details of the real-world evaluation: hand type, number of trials, confidence intervals, objects list, and success criteria.
3. Compare against HOIGPT (or justify its exclusion clearly) and qualify the "first" claim.
4. Report all missing hyperparameters for reproducibility.
5. Discuss the low Diversity scores and whether they indicate a limitation of the approach.

## Score and Decision

**Calibration Anchors:**

| Anchor | Avg Score | Round | Comparison to UniHM |
|--------|-----------|-------|---------------------|
| Vision-Based Pseudo-Tactile (xcHIiZr3DT) | 2.50 | R1 | Much weaker; narrow scope, no real-world validation |
| Vision-Based Grasping (sXF5P4N7e8) | 3.00 | R1 | Much weaker; basic RL method |
| GRAIL (oyXoGJQlUf) | 3.00 | R1 | Much weaker; different problem (PDDL planning) |
| Early Fusion VLA (KBSHR4h8XV) | 3.33 | R1 | Weaker; limited evaluation |
| DTP (VaoeAi5CW8) | 4.25 | R1/R2 | Weaker; simulation-only evaluation |
| Mani-WM (aVyJwS1fqQ) | 4.67 | R2 | Comparable; both have real-world eval but limitations |
| Cross-Embodiment Dex Grasping (twIPSx9qHn) | 5.00 | R1 | Comparable; both tackle cross-embodiment but that paper actually tests it; UniHM has better real-world eval |
| Instruct2Act (JWrl5pJCnl) | 5.00 | R2 | Comparable; both use VLMs for manipulation |
| CrayonRobo (Aqfwhna1D7) | 5.20 | R1/R2 | Comparable; both have evaluation limitations |
| Visual Robot Manipulation - GR1 (NxoFmGgWC9) | 5.50 | R1/R2 | Stronger; better benchmark results, more comprehensive |
| LAPA (VYOe2eBQeh) | 5.83 | R2 | Stronger; more rigorous evaluation, stronger novelty |
| GEVRM (hPWWXpCaJ7) | 6.00 | R2 | Stronger; more comprehensive experiments |
| HandsOnVLM (AJQuTFd9es) | 6.33 | R2 | Stronger; new benchmarks, but similar baseline weaknesses |
| GenSim (OI3RoHoWAN) | 8.00 | R1 | Much stronger; comprehensive evaluation, clear contribution |
| Geometry-aware RL (7BLXhmWvwF) | 8.00 | R1 | Much stronger; rigorous benchmark and experiments |

**Round 1 bracket:** Narrowest plausible range is 4.0–6.0 (clearly above the 2.5–3.33 low band, clearly below the 8.0 high band).

**Round 2 narrowing:** The paper is slightly weaker than LAPA (5.83) and HandsOnVLM (6.33) which both have more complete evaluations of their core claims. It is comparable to Cross-Embodiment Dex Grasping (5.00) and CrayonRobo (5.20). The paper has a coherent pipeline and real-world validation that puts it above DTP (4.25) and Mani-WM (4.67). The central weakness — the untested cross-morphology claim — prevents a stronger score.

**Final score:** 5.0. The paper presents a reasonable pipeline for a genuine problem and provides some evidence of effectiveness, but the evaluation gaps (particularly the untested cross-morphology tokenizer and underspecified real-world experiments) are significant enough that the paper in its current form does not meet the bar for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>