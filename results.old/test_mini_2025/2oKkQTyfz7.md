Now I have enough information for calibration. Let me synthesize the final review.

**Calibration Summary:**

**Round 1 Bracketing:** I performed three queries for VLN/dataset/benchmark papers across low (<3.5), middle (3.5-7.5), and high (>7.5) bands. The paper sits clearly above the low band (all <3.5 anchors are non-VLN papers with withdrawn/reject decisions) and clearly below the high band (7.5+ anchors are oral/spotlight papers with more thorough evaluations). Initial bracket: **4.0–6.5**.

**Round 2 Narrowing:** I retrieved anchors with scores 4.5–6.5 and 5.0–7.0 on VLN and embodied navigation topics:
- SRDF (6.5, accepted) — VLN data flywheel. Stronger controlled experiments; GSA is below.
- HAZARD (6.75, accepted) — Embodied benchmark for dynamic environments. More thorough evaluation with learning curves; GSA is below.
- ThinkBot (5.75, accepted) — Embodied instruction following. Comparable tier but better-controlled.
- SPARTUN3D (5.75, accepted) — 3D situated understanding dataset. Comparable tier.
- LoTa-Bench (6.0, accepted) — Embodied task planning benchmark. GSA slightly below.
- PARSE-Ego4D (5.5, rejected) — Action recommendation dataset. GSA is similar or slightly better.
- OBSER (5.5, rejected) — Sub-environment recognition. GSA is better.

The GSA paper has a genuine dataset contribution that surpasses PARSE-Ego4D and OBSER, but its evaluation gaps (missing learning curves for the core "adaptation over time" claim, uncontrolled baselines) are more significant than what ThinkBot or SPARTUN3D faced. I place it at **5.5** — borderline, leaning toward rejection given the gaps.

Now let me write the complete review.

## Summary
2-3 sentence summary

## Strengths

Let me list only concrete, well-evidenced strengths.

1. **GSA-R2R dataset provides substantially greater scene and instruction diversity than prior VLN benchmarks.** Table 1 shows 150 evaluation scenes across 20 building types (vs. 29 scenes from only MP3D in R2R/R4R/RxR), 90,000 paths each with up to 7 instruction types, and the largest unseen vocabulary. Figure 2 confirms that non-residential building types (cinemas, shops, laboratories) are entirely absent from prior evaluation splits, making this a valuable resource for evaluating OOD generalization.

2. **The three-stage LLM-based instruction pipeline produces stylistically diverse instructions.** Section 3.3.2 describes a pipeline where speaker-generated instructions are VLM-refined with path visualizations, then role-play rephrased into Scene and User styles. The t-SNE analysis (Figure 4) shows that User and Scene instructions occupy distinctly different embedding regions from the training distribution, while the human evaluation (Table 2) confirms ~80% path-matching accuracy and 96% style distinctiveness for Scene instructions — direct evidence of stylistic diversity.

3. **GR-DUET achieves large and consistent improvements over all baselines.** In Table 4, GR-DUET improves SR over vanilla DUET by +11.6 (57.7→69.3) on Test-R-Basic and +8.5 (48.1→56.6) on Test-N-Basic. Tables 5–6 show similar gains across User and Scene instructions. The contrast with TourHAMT (14.9 SR) and OVER-NAV (22.3 SR) is striking, and the ablation in Table 7 confirms that the benefit is not solely from extra pretraining (without pretraining and augmentation, GR-DUET still achieves 56.8 SR, far above memory-based baselines).

4. **Ablation studies cleanly isolate key design choices.** Table 7 separates the contributions of pretraining with ground-truth graphs and PREVALENT augmentation. Table 8 tests buffer size and comparison strategies for graph construction, showing memory-based buffer methods outperform proportion-based alternatives, with optimal performance at α=50.

5. **Comprehensive benchmarking of diverse adaptation methods.** Tables 3–6 benchmark 5 VLN architectures, 5 optimization-based methods (TENT, SAR, BT, MLM, MRC), and 2 memory-based methods (TourHAMT, OVER-NAV). The non-obvious failures — TENT/SAR harming performance, TourHAMT collapsing to ~15% SR, BT helping only on Basic instructions — provide useful diagnostics for the community.

## Weaknesses

### Fatal
None.

### Major

**1. The paper does not measure whether agents actually improve over time within an environment — the core phenomenon the task is designed to study.**

The GSA-VLN task is defined as enabling "agents to continuously improve as they execute instructions in previously unseen environments" (Section 3.2, line 69). The paper states "agents are required to maintain long-term memory and continuously update their model parameters to improve performance over time" (Section 1, line 37). Yet the experimental protocol (Section 4.2) shuffles episode order and reports only means and standard errors across three random permutations. No results show how SR/SPL changes as a function of episode index within a single environment. A baseline that achieves 69.3 SR with no upward trend is not "adapting" — it is just performing at a static level. The GR-DUET's global graph may help at every step equally, not progressively. The buffer-size ablation (Table 8) provides indirect evidence consistent with adaptation (bigger buffers help up to a point), but this is not a substitute for direct learning-curve measurements. This gap undermines the paper's motivating narrative.

**2. The comparison between GR-DUET and adaptation baselines is not controlled for training pipeline differences.**

GR-DUET modifies both training and inference: it uses pretraining with full ground-truth topological maps and environment-specific fine-tuning with PREVALENT augmentation (Section 4.1). In contrast, the optimization-based methods (TENT, SAR, BT, MLM, MRC) and memory-based methods (TourHAMT, OVER-NAV) are applied as plug-in modifications to vanilla DUET — with no equivalent pretraining or fine-tuning. The catastrophic gap (TourHAMT 14.9 SR vs. GR-DUET 69.3 SR on Test-R-Basic) conflates the effect of the graph-retention mechanism with the effect of better pretraining and more training data. The ablation in Table 7 partially addresses this (GR-DUET without pretraining/agumentation = 56.8 SR, still well above TourHAMT's 14.9), suggesting the graph mechanism itself helps. However, a controlled comparison where TourHAMT or OVER-NAV is applied on the same pretrained backbone would be needed to fairly assess GR-DUET's specific architectural contribution. Without this, the paper overclaims the effectiveness of the graph-retention mechanism versus the training pipeline.

**3. Dataset validation is thin for a primary dataset contribution.**

The human evaluation (Section 3.3.4) uses 15 participants judging 20 instructions each — 300 judgments total for 90,000 instruction-path pairs across 150 environments. The *Matching* score for Basic instructions is only 80% (1 in 5 instructions may not accurately describe the path). The *Style* score for User instructions is 57.6% — barely above the 20% random baseline for distinguishing 5 characters and well below the 96% for Scene instructions. The paper's explanation ("word-level changes are less noticeable when viewed individually") is speculative and does not address whether the LLM role-playing actually produces consistent, detectable stylistic patterns. For a dataset that is the paper's primary contribution (submitted to the datasets and benchmarks track), stronger validation — larger annotation samples, inter-annotator agreement, automatic alignment metrics, or linguistic analysis of User styles — would be expected to certify the dataset as a reliable community resource.

### Minor

**4. The explanations for optimization-based method failures are plausible but unsupported by evidence.**

The paper explains TENT/SAR failures by stating "entropy measures become meaningless after an incorrect step" (Section 4.3.2) and attributes MLM's marginal improvement to not being "optimized together with action prediction." These are reasonable hypotheses but are stated without supporting evidence (e.g., entropy distributions over correct vs. incorrect steps, or comparisons of MLM representations with vs. without action-prediction training). Quantitative diagnostics would strengthen these claims.

**5. Missing analysis of why memory-based baselines collapse.**

TourHAMT achieves only 14.9 SR on Test-R-Basic (vs. 48 SR for vanilla HAMT). OVER-NAV achieves 22.3 SR. The paper attributes this to "excessively long history embeddings as input" (Section 4.3.2). This explanation is plausible but a diagnostic analysis — e.g., performance vs. history length, attention pattern visualization, or trajectory length statistics — would make the paper's critique of these methods more informative and actionable for future research.

### Trivial
None.

## Nice-to-Haves
- Showing SR/SPL curves binned by episode index (early/middle/late) would directly support the task framing and could reveal whether GR-DUET genuinely improves with experience or merely benefits from graph-based representation at all episodes equally.
- A controlled experiment applying TourHAMT or OVER-NAV on a pretrained backbone similar to GR-DUET's would cleanly isolate the contribution of the graph-retention mechanism from training pipeline effects.
- A larger human evaluation with multiple annotators per instruction and reported inter-annotator agreement would strengthen the dataset's certification.
- Reporting the fraction of speaker-generated instructions retained vs. regenerated at each pipeline stage would help the community assess the dataset's provenance.

## Removed Points

**Harsh Critic points removed:**
1. *"Section 3.2 distinction from lifelong learning and TTA is superficial"* — The paper explicitly distinguishes GSA-VLN from lifelong learning (repeated application of same skill vs. acquiring new skills) and TTA (TTA has no memory bank; GSA-VLN integrates one). The distinction is adequate.
2. *"Section 3.3.2: doesn't report fraction of instructions retained/regenerated"* — This is an implementation detail about generation statistics, not a methodological weakness.
3. *"Section 3.3.4: t-SNE needs quantitative measures of distribution shift"* — The t-SNE is presented as a diversity visualization, not a quantitative metric. Requesting additional metrics is a nice-to-have, not a weakness. The paper also notes that traditional linguistic metrics like BLEU/ROUGE are inappropriate for OOD instructions.
4. *"Section 4.2: doesn't specify update frequency for TTA methods"* — This is a minor implementation detail that would typically be in the appendix (which is stripped).
5. *"Comparison with LLM-based VLN agents absent"* — These methods use different training pipelines and action spaces; their inclusion would expand scope beyond what is reasonable.
6. *"Ethical considerations about TV character role-playing"* — Scope creep; this is not standard practice for VLN papers.

**Strength Finder points removed:**
7. *Strength about "substantially greater scene and instruction diversity"* — Retained as Strength #1.
8. *Strength about "human evaluation provides direct evidence"* — Re-framed as part of the dataset contribution (Strength #2) rather than a separate strength, since the sample size limits the strength of the evidence.
9. *Strength about "comprehensive benchmarking reveals non-obvious failures"* — This is descriptive rather than a core strength; merged into benchmarking point (Strength #5).

## Novel Insights
None beyond the paper's own contributions. The harsh critic's observation that the missing learning curves contradict the task's motivating narrative is a useful critical insight, but the reviews do not surface a novel positive observation about the paper that the authors themselves did not make.

## Suggestions
1. **Add learning curves**: Plot SR/SPL vs. episode index (or bin into early/middle/late groups) for at least the Test-R-Basic and Test-N-Basic splits. This is the single most impactful addition because it directly tests the paper's central claim about adaptation over time.
2. **Controlled baseline comparison**: Evaluate TourHAMT and OVER-NAV with the same pretraining and fine-tuning recipe as GR-DUET, or alternatively, ablate GR-DUET down to a minimal memory-augmented DUET that does not use extra pretraining, to isolate the contribution of the graph-retention mechanism.
3. **Expand dataset validation**: Conduct a larger human study (100+ instructions per type) with multiple annotators and report inter-annotator agreement. For User instructions, provide linguistic analysis (n-gram distributions, syntactic patterns) to demonstrate that the five characters genuinely differ in detectable ways.
4. **Diagnose baseline failures**: For TourHAMT and OVER-NAV, analyze performance as a function of history length to confirm that long history embeddings cause the collapse, rather than other confounds (e.g., action space mismatch, step limit issues).

## Score and Decision

**Anchor table (all papers retrieved across rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| LVLM-CL | JIlIYIHMuv.md | 2.50 | R1 | Non-VLN continual learning; much weaker |
| VideoGPT+ | YGWxpOI6Y0.md | 3.40 | R1 | Non-VLN video understanding; weaker |
| MCTBench | BVACdtrPsh.md | 3.00 | R1 | Non-VLN benchmark; weaker |
| Industrial Benchmarking | JQbqaQjV7D.md | 3.00 | R1 | Non-VLN; weaker |
| MCIL Benchmark | gNoqEdT2wO.md | 2.33 | R1 | Non-VLN continual learning; weaker |
| Domain-specific Benchmarking | 1CeIRl147S.md | 4.33 | R1 | VLM benchmarking; comparable in contribution scope |
| SRDF (VLN Data Flywheel) | OUuhwVsk9Z.md | 6.50 | R1/R2 | VLN data generation, accepted poster; better-controlled experiments |
| ReForm-Eval | ZuYvrjh2od.md | 5.00 | R1 | VLM benchmark, rejected; similar tier |
| Dysca | bU1JOvdXXK.md | 6.00 | R1 | LVLM benchmark, accepted; more thorough |
| Inherent 3D Reasoning | uBhqll8pw1.md | 4.00 | R1 | Non-VLN; weaker |
| EQA-MX | 7gUrYE50Rb.md | 8.00 | R1/R3 | Embodied QA, spotlight; much stronger |
| GUI Agents | kxnoqaisCT.md | 7.75 | R1/R3 | GUI agents, oral; much stronger |
| R2C (Chessboard) | ysAX5ORQoX.md | 4.25 | R2 | Non-VLN; weaker |
| Embodied Instruction Following | pwKokorglv.md | 4.00 | R2 | Non-VLN; weaker |
| SnapMem | mz8unSsSsB.md | 4.25 | R2 | 3D scene memory; different domain, weaker |
| Octopus | VUA9LSmC2r.md | 4.00 | R2 | Non-VLN; weaker |
| EF-VLA | KBSHR4h8XV.md | 3.33 | R2 | Non-VLN; weaker |
| Task Planning Visual Room | jJvXNpvOdM.md | 6.67 | R2 | Embodied task planning, accepted; stronger |
| ThinkBot | tFDTHA3odg.md | 5.75 | R2 | Embodied instruction following, accepted; comparable |
| GROOT-2 | S9GyQUXzee.md | 5.50 | R2 | Multimodal instruction following, accepted; comparable |
| LLaRA | iVxxgZlXh6.md | 5.25 | R2 | Robot learning data; comparable |
| BALROG | fp6t3F669F.md | 6.25 | R2 | Game-based benchmark, accepted; more thorough |
| SPARTUN3D | FGMkSL8NR0.md | 5.75 | R2/R3 | 3D dataset, accepted poster; comparable |
| VisualAgentBench | 2snKOc7TVp.md | 5.75 | R2 | LMM benchmark, accepted; more thorough |
| Learning with a Mole | 8HCARN2hhw.md | 6.67 | R2 | Navigation representations, accepted; stronger |
| SnapMem (again) | mz8unSsSsB.md | 4.25 | R3 | 3D scene memory; weaker |
| FlightBench | vrCT5uCdYp.md | 4.75 | R3 | Non-VLN navigation; weaker |
| OBSER | BUEQlOwGMY.md | 5.50 | R3 | Sub-environment recognition, rejected; GSA is stronger |
| UnrealCV Zoo | vQ1y086Kn2.md | 5.00 | R3 | Embodied env dataset, rejected; similar tier |
| 3D-GRAND | i7hXOqzUcK.md | 5.00 | R3 | 3D-LLM dataset, withdrawn; GSA is stronger |
| HAZARD | n6mLhaBahJ.md | 6.75 | R3 | Embodied dynamic benchmark, accepted poster; more thorough evaluation |
| LoTa-Bench | ADSxCpCu9s.md | 6.00 | R3 | Embodied task planning benchmark, accepted; more thorough |
| PARSE-Ego4D | Kh5OS3oNlg.md | 5.50 | R3 | Ego action dataset, rejected; GSA is stronger |
| Incremental VLM | EKfcngSxwD.md | 4.67 | R3 | Non-VLN; weaker |
| Stylized Offline RL | rnHNDihrIT.md | 6.50 | R3 | Non-navigation; not comparable |

**Round 1 bracket:** 4.0–6.5.

**Round 2 narrowing:** The paper sits near the lower end of the 5.0–6.5 band. It is stronger than PARSE-Ego4D (5.5, rejected) and OBSER (5.5, rejected), comparable to ThinkBot (5.75, accepted) and SPARTUN3D (5.75, accepted), but notably weaker than SRDF (6.5, accepted) and HAZARD (6.75, accepted) in terms of evaluation thoroughness and evidence for core claims. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>