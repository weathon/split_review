## Summary

This paper formalizes the **Program-to-Geometry** task, where models interpret procedural drawing code (Asymptote/matplotlib) to construct geometric representations and solve problems. The authors present **GeoGramBench**, a 500-problem benchmark with a three-level taxonomy (Primitive Recognition → Local Relation Composition → Global Abstract Integration) based on geometric complexity rather than reasoning-step difficulty. A key methodological contribution is the identification and mitigation of answer leakage (direct and indirect) in geometry code. Evaluation of 19 LLMs shows that even the strongest models (GPT-5 at 75.01% overall) fall below 50% on the Abstract level, revealing a pronounced gap in program-driven spatial reasoning.

## Strengths

- **Novel task formalization with genuine practical grounding.** The Program-to-Geometry task is a well-motivated and underexplored evaluation axis. The paper correctly identifies that existing benchmarks treat geometry code as an incidental subset rather than a systematic test of spatial abstraction from symbolic code. The distinction between text-only and text+code performance (Figure 1) provides a clear initial demonstration that models struggle with procedural code.

- **Answer leakage mitigation is a thoughtful and specific contribution.** The paper identifies a subtle vulnerability unique to geometry-code benchmarks: answers can leak through coordinate values (direct) or code parameters (indirect) in the procedural drawing code. The targeted countermeasures—coordinate rescaling and parameter masking (Section 4.1, Figure 3)—are principled and cleanly demonstrated. No prior geometry benchmark has addressed this, and it meaningfully improves the benchmark's integrity.

- **Rigorous human curation pipeline.** The two-stage manual verification by four experts (master's level or above in mathematics) with three-pronged refinement (decontamination, answer leakage prevention, accuracy verification) is more thorough than typical for benchmark papers of this scale (Section 4.3). The reduction from 1,782 unique candidates to 392 curated problems reflects meaningful quality control.

- **Comprehensive evaluation across 19 models with fine-grained subtype breakdown.** The evaluation spans both closed-source (GPT-5, GPT-o1, Gemini-Pro) and open-source models (Qwen3, DeepSeek-R1, QwQ-32B, etc.) across six answer types per difficulty level (Table 1). The subtype analysis revealing that angle (in 2D) and volume/area (in 3D/Abstract) are the hardest subtypes provides actionable diagnostic information beyond aggregate accuracy.

## Weaknesses

### Major

- **Taxonomy validation is thin for the central claim it supports.** The paper argues that geometric complexity, not reasoning complexity, is the primary challenge in Program-to-Geometry. The validation for this claim (Section 3.2, Figure 2) relies on a single model (QwQ-32B) on only 42 problems from MATH-500. The data in Figure 2 shows irregular trends (accuracy by reasoning complexity on code problems goes 79.4% → 56.9% → 86.2%, rising at the highest level), which undermines the clean narrative about orthogonality. The paper reports no correlation coefficients or reasoning complexity labels. While the main evaluation across 19 models strongly supports the *difficulty ordering* of the three levels, the specific claim about orthogonality to reasoning complexity is under-validated. The authors should either (a) strengthen this analysis with multiple models and controlled experiments within GeoGramBench, or (b) soften the claim to reflect that the taxonomy's main empirical support comes from the difficulty ordering observed in the full evaluation.

- **Decontamination status of augmented problems is unclear.** The benchmark augments 392 curated problems with 5 from AIME24, 42 from MATH-500, and 61 from MathVerse (Section 4.4). The paper provides extensive detail about decontamination and answer leakage prevention for the 392 main problems, but does *not* state whether the same procedures were applied to the AIME24 and MATH-500 subsets. These are widely used benchmark problems—if added without modification, they could inflate performance on known items and compromise the benchmark's validity. The MathVerse subset was manually transcribed (mitigating direct copying, but not structural similarity). The paper must clarify what decontamination was applied to each source, or explain why these problems are considered safe.

### Minor

- **No uncertainty estimates in the main results.** Accuracy is reported as a point value from 8 samples per problem (Section 5.1), but no standard deviations, confidence intervals, or significance tests are provided. With 500 problems and per-model stochasticity, differences between models (e.g., GPT-5 at 75.01% vs. Qwen3-235B at 74.00%) could fall within noise. This is especially problematic for subtype breakdowns where sample sizes become very small (some subtypes may have only a handful of problems). Bootstrapped confidence intervals would substantially strengthen the reliability of model rankings.

- **Failure pattern analysis is qualitative and not quantified.** The behavioral analysis (Section 6) describes four failure patterns (algebraic bias, lack of auxiliary constructions, orientation confusion, symbolic mapping errors) that are intuitively plausible and supported by examples. However, the analysis is based on "manual review of a substantial number of failure cases" without specifying how many were reviewed, how they were sampled, or whether the patterns were quantified. The paper acknowledges the lack of "accurate automated assessment methods," but annotating a random subsample and reporting prevalence would turn insightful observations into reproducible findings.

- **No human performance baseline.** The paper reports that even the strongest models achieve <50% on the Abstract level, but without a human baseline it is difficult to calibrate whether this reflects inherent problem difficulty or a specific model limitation. A small human expert evaluation (e.g., 10–20 problems per level) would strengthen the claim that LLMs are specifically deficient.

### Trivial

- None beyond the formatting artifacts introduced by PDF parsing.

## Nice-to-Haves

- **Inter-annotator agreement for taxonomy categorization.** The taxonomy classification uses GPT-4o with human review (Section 4.5), but no agreement metric is reported. Reporting Cohen's κ on a subsample would strengthen trust in the categorization.

- **Release of model responses** (even for a subset of models) would facilitate follow-up analysis and improve reproducibility beyond the provided evaluation code.

- **Adapt the evaluation prompt to test whether CoT specifically helps or hinders** by also reporting results with a direct-answer prompt, to quantify the effect of the chosen prompt strategy.

## Removed Points

These points from the inputs were removed with justification:

- **"Boundaries between Compositional and Abstract are not sharply defined"** (Harsh Critic): The paper provides definitions with concrete examples in Figure 4. While no inter-annotator agreement is reported, the definitions are clear and the human expert review handles borderline cases. This is a standard level of precision for a benchmark taxonomy.

- **"GPT-4o filtering details not reported"** (Harsh Critic): The paper reports proceeding from 1,782 items to 1,247 geometry items through GPT-4o classification. While agreement with human labels is not reported, this is a minor preprocessing step and the subsequent two-stage human refinement corrects any misclassifications.

- **"Evaluation prompt may favor instruction-tuned models"** (Harsh Critic): The prompt is applied uniformly across all models, so comparisons are internally valid. The speculation about favoring specific model types is not supported by evidence.

- **Strength Finder's claim about taxonomy being "validated empirically"**: The strength is retained but caveated above as a weakness. The difficulty ordering is empirically supported; the stronger claim about orthogonality to reasoning complexity is not.

## Novel Insights

The most interesting finding to emerge from the reviews—beyond what the paper itself states—is the tension between the paper's strong claims about geometric complexity being orthogonal to reasoning complexity and the thin evidence base for that specific claim. The taxonomy itself is useful and well-motivated, but the *strongest* evidence for it is the consistent accuracy drop across all 19 models on the 500-problem benchmark, not the preliminary MATH-500 analysis. If the authors leaned on this empirical support rather than the weaker single-model validation, the paper would be more rigorous. The second novel angle is that answer leakage in geometry code is a subtle but real threat to benchmark validity that no prior work systematically addressed—this is a genuine contribution that other geometry benchmark builders should adopt.

## Suggestions

1. **Clarify decontamination for augmented problems.** Add a short paragraph (or table) in Section 4.4 specifying the decontamination status of each data source (AIME24, MATH-500, MathVerse). If no modifications were applied, explain why these sources are believed to be safe (e.g., the small number of problems, the manual transcription for MathVerse).

2. **Add confidence intervals to the main results.** Even bootstrapped 95% CIs for the overall and level-wise scores would greatly strengthen the evidence for model rankings. This is particularly important for the subtype analysis where sample sizes are small.

3. **Strengthen or soften the taxonomy validation claim.** Either (a) run the taxonomy validation on GeoGramBench's own data with multiple models to show that geometric complexity predicts accuracy better than a human-labeled reasoning difficulty measure, or (b) reframe the claim as "the taxonomy provides a difficulty ordering that is empirically confirmed by the main evaluation," acknowledging that the orthogonality-to-reasoning-complexity claim remains a conceptual motivation.

4. **Quantify the failure patterns.** Take a random sample of 50–100 failure cases per level for 2–3 representative models, have two annotators code the presence of the four identified failure patterns, and report frequencies. This would turn insightful qualitative observations into reproducible findings.

5. **Add a human baseline.** Even a small study (10–20 problems per level from a few math experts) would calibrate the benchmark and strengthen the claim that LLM performance at the Abstract level is genuinely deficient rather than reflecting inherent problem difficulty.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Queried three bands using geometry/code/spatial-reasoning topics:
- Low band (avg < 3.5): returned papers scoring 2.00–3.25 (traffic incident benchmark, programming challenges, structure-rich text benchmark, graph modification). These are clearly weaker than GeoGramBench.
- Middle band (3.5 < avg < 7.5): returned papers scoring 4.00–6.75 (GeomRel at 6.67, SPACE at 6.75, GeoMeter at 4.00, depth/height perception at 4.00). GeoGramBench fits in this range.
- High band (avg > 7.5): returned papers scoring 8.00–9.00 (BigCodeBench, PhysBench). GeoGramBench is not at this level.

Initial bracket: **4.0–6.75**.

**Round 2 — Narrowing.** Queried inside the bracket focusing on geometry benchmarks and LLM evaluation:
- Returned: Euclid/Geoperception (5.00), LiveCodeBench (6.25), Program Synthesis for Visual Programming (5.80), GeoILP (6.00), Putnam-AXIOM (5.80), MathVista (7.25).
- Read in full: Euclid/Geoperception (5.00), LiveCodeBench (6.25), GeomRel (6.67).

**Comparison against anchors:**
- *Euclid/Geoperception (5.00, reject)*: Had circular data filtering, small training set, overclaimed results. GeoGramBench is clearly stronger — cleaner construction, more novel task, no circularity.
- *LiveCodeBench (6.25, accept)*: Dynamic contamination-free coding benchmark. GeoGramBench is comparable — both have solid benchmarks with thorough evaluation, both have some methodological concerns. GeoGramBench's task formalization is arguably more novel, but LiveCodeBench has a more scalable design.
- *GeomRel (6.67, accept)*: Geometry relationship ID benchmark. GeoGramBench is slightly weaker in evaluation rigor (GeomRel proposes and evaluates a method) but has a more novel task and larger dataset.

The paper sits between LiveCodeBench and GeomRel in quality. Its strongest assets are the novel task formalization, answer leakage mitigation, and thorough human curation. Its main weaknesses are the thin taxonomy validation, unclear decontamination for augmented sources, and missing uncertainty estimates.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>