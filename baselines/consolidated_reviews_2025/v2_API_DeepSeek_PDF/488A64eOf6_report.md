## Summary
# Final Review Report

## Summary

This paper (DAEMON) proposes a novel decoding-time framework for open-ended text generation from language models. The core idea is to formulate decoding as a constrained optimization problem: find the distribution q that minimizes reverse KL divergence from the base LM distribution pθ while matching expected evaluation metric scores with human text. The solution takes the form of an Energy-Based Model (EBM) pθ,µ(x) ∝ pθ(x)·exp(−µᵀf(x)). The paper proves that the optimal solution guarantees improved perplexity over the base LM (Proposition 2) and adopts Sampling-Importance-Resampling (SIR) for tractable sampling from the globally-normalized distribution. Experiments on Wikipedia and News domains with GPT-2 XL (1.5B) and OPT-6.7B show improved alignment with human texts across repetition, coherence, diversity, and information metrics compared to strong baselines (nucleus sampling, top-k, typical decoding, contrastive decoding/search).

**Key Strengths**: The optimization-based framing is principled and theoretically grounded (analytical EBM solution, perplexity guarantee). The SIR-based sampling approach provides a practical pathway for handling the globally-normalized EBM. Empirical results are consistent across two model families and two domains. The ablation study (Table 4) convincingly demonstrates the contribution of each metric group.

**Key Weaknesses**: (1) Automatic evaluation metrics overlap directly with DAEMON's constraint set, creating a circular evaluation advantage. (2) No variance/confidence intervals are reported for any metric in Table 1, preventing statistical significance assessment. (3) The theoretical perplexity guarantee (Proposition 2) applies to the exact optimization solution, not the practical SIR approximation with temperature modulation—this gap is not adequately discussed. (4) The SIR convergence rate O(M⁻¹) assumes sampling from pθ, but the implementation uses temperature-modulated pτ_θ (τ<1), breaking the theoretical guarantee. (5) The WIS-based µ estimation may suffer from importance weight degeneracy, which is not analyzed.

**Novelty Assessment (Deferred)**: External literature verification is unavailable in this run (Retrieval-Disabled Mode). Novelty claims relative to energy-based decoding methods (e.g., Deng et al. 2020, Khalifa et al. 2021, Parshakova et al. 2019ab) cannot be independently verified here and require manual literature verification.

## Strengths
1. **Principled optimization-based framing**: The formulation of decoding as constrained reverse-KL minimization with expectation-matching constraints is novel and well-motivated. The analytical solution (Proposition 1) as an EBM that scales the base LM distribution by exp(−µᵀf(x)) is elegant and provides a clear information-geometric interpretation (information projection).

2. **Theoretical perplexity guarantee**: Proposition 2 provides a non-trivial theoretical result: the optimal decoding distribution strictly improves perplexity over the original LM. This is a stronger theoretical foundation than existing heuristic decoding methods, which typically lack distribution-level guarantees.

3. **Practical SIR-based sampling**: The use of Sampling-Importance-Resampling to approximate the globally-normalized EBM is well-chosen. The parallel candidate generation and the O(M⁻¹) convergence rate (under ideal conditions) provide a practical pathway from the theoretical solution to implementable decoding.

4. **Comprehensive empirical evaluation**: Experiments span two domains (Wikipedia, News), two model families (GPT-2 XL 1.5B, OPT-6.7B), multiple sampling-based and search-based baselines, and both automatic and human evaluation. The ablation study (Table 4) convincingly demonstrates the individual contribution of each metric group.

5. **Human evaluation validation**: The pairwise human evaluation (Table 3) shows statistically significant improvements (p<0.005) across fluency, coherence, and informativeness, providing evidence beyond automatic metrics.

6. **Clear exposition**: The paper is generally well-written with clear problem motivation, rigorous mathematical derivations, and thorough appendices covering proofs, runtime analysis, convergence analysis, and qualitative examples.

## Weaknesses
1. **Circular evaluation (Major)**: The automatic evaluation metrics (SR-N, TR-L, COH, DIV, eENT) are identical to the constraint set used by DAEMON. This gives DAEMON an inherent advantage over baselines that do not explicitly optimize these objectives. The paper partially addresses this with MAUVE and human evaluation, but the main narrative emphasis is on the same-metric comparison.

2. **Missing variance/statistical significance (Major)**: Table 1 reports only point estimates without standard deviations, confidence intervals, or significance tests. Many metric differences are small (e.g., SR-4: 0.42 vs 0.48 reference), and without variance information, the reader cannot assess whether improvements are statistically reliable.

3. **Theory-practice gap in convergence guarantees (Major)**: The O(M⁻¹) SIR convergence guarantee assumes sampling from pθ, but the implementation uses temperature-modulated pτ_θ (τ_θ (τ<1). The perplexity guarantee (Proposition 2) applies to the exact optimization solution, not the practical approximation. These gaps are not adequately discussed.

4. **WIS degeneracy risk (Major)**: The Weighted Importance Sampling estimation of µ (Algorithm 1) can suffer from importance weight degeneracy when the target EBM distribution differs substantially from the proposal. No diagnostic (e.g., effective sample size) is reported.

5. **Limited domain/task diversity (Moderate)**: Experiments are limited to open-ended generation on Wikipedia and News. The summarization experiment (Appendix I) is a useful addition but uses a different model (Pegasus). Broader validation on dialogue, story generation, or instruction-following tasks would strengthen generalizability claims.

6. **Human evaluation scope (Moderate)**: Human evaluation uses only 100 prefixes with 3 annotators per comparison. While acceptable for a conference paper, the sample size is modest, and only pairwise comparisons (not absolute ratings) are reported.

7. **Computational cost (Moderate)**: DAEMON with M=25 candidates has 1.35× latency vs greedy decoding. While the paper provides runtime analysis, the memory cost of generating M parallel candidates is not discussed. For larger models (e.g., OPT-6.7B), this could be prohibitive.

8. **Conclusion overclaim (Minor)**: The conclusion states DAEMON "outperforms strong decoding baselines" without bounding the claim to evaluated settings. The final sentence ("paves the way") is promotional without scientific content.

## Key Issues
### Issue 1 (Major): Circular Evaluation — Automatic Metrics Overlap with Constraint Set
- **Location**: Page 6 - §3.2 Evaluation Metric Settings; Page 7 - Table 1
- **Evidence**: Metrics in §3.2 (SR-2/3/4, TR-8/16/32, COH, DIV, eENT) are the same metrics used as DAEMON's constraints (§3.3). 
- **Impact**: DAEMON is explicitly optimized to match human text on these exact metrics, giving it an inherent and expected advantage. The primary novelty claim (better text quality) rests partly on a circular evaluation.
- **Fix required**: Add held-out metrics not in constraint set; reweight discussion to emphasize MAUVE and human evaluation as primary evidence.

### Issue 2 (Major): Missing Statistical Significance Reporting
- **Location**: Page 7 - Table 1
- **Evidence**: All metrics reported as point estimates without standard deviation, confidence intervals, or significance tests. No multi-seed results reported.
- **Impact**: Readers cannot assess whether DAEMON's improvements are statistically reliable, especially for small-margin gains.
- **Fix required**: Report mean±std over ≥3 seeds; add significance tests for key comparisons.

### Issue 3 (Major): Theory-Practice Gap in Convergence Guarantees
- **Location**: Page 5 - §2.3.2 (SIR sampling); Page 8 - §3.6 (ablation with τ<1)
- **Evidence**: SIR O(M⁻¹) guarantee (citing Skare et al. 2003) assumes sampling from pθ, but Algorithm 2 uses temperature-modulated pτ_θ with τ=0.97/0.99. The perplexity guarantee (Proposition 2) applies to exact qopt, not the approximated ˆpM_θ,µ.
- **Impact**: The paper implies stronger theoretical backing than the implemented method actually provides.
- **Fix required**: Explicitly acknowledge the τ≠1 issue; provide empirical analysis of the approximation gap.

### Issue 4 (Major): WIS Degeneracy Risk Without Diagnostic
- **Location**: Page 5 - Algorithm 1 and surrounding text
- **Evidence**: The µ estimation relies on importance sampling weights w_i = exp(-Eµ(ˆx_i)). When Eµ produces large positive values, weights collapse, increasing estimator variance.
- **Impact**: No diagnostic (effective sample size) is reported, so the reliability of µ estimation is unknown.
- **Fix required**: Report ESS for µ estimation; consider defensive importance sampling.

### Issue 5 (Moderate): Reverse KL Mode-Seeking Trade-off Not Acknowledged
- **Location**: Page 2-3 - §2.1; Appendix C
- **Evidence**: The paper motivates reverse KL via mode-seeking but does not acknowledge that this can reduce distributional diversity (a key evaluation aspect).
- **Impact**: The framework may inherently limit diversity despite including diversity metrics as constraints.
- **Fix required**: Add explicit discussion of this trade-off and empirical evidence that it is managed.

## Actionable Suggestions
### S1 (Must): Add Variance Reporting and Significance Tests
**Location**: Page 7 - Table 1 and surrounding text
**Action**: Report all metrics as mean±std over ≥3 random seeds. Add a paired bootstrap test or Wilcoxon signed-rank test comparing DAEMON against the best baseline for each metric-domain combination.
**Expected benefit**: Allows readers to assess statistical reliability of reported improvements. Current point estimates alone are insufficient for confidence.
**Effort**: Low-to-medium (requires re-running experiments with different seeds).

### S2 (Must): Add Held-Out Evaluation Metrics
**Location**: Page 6 - §3.2
**Action**: Include at least 1) Add at least one metric NOT in the constraint set to Table 1. Candidates: perplexity from a different LM (e.g., OPT-175B), factual consistency (e.g., FactCC), or sentiment/toxicity metrics. 2) Explicitly note which metrics were optimized and which are held-out.
**Expected benefit**: Provides unbiased evaluation of DAEMON's text quality improvements. Without this, the primary evaluation is circular.
**Effort**: Low (computing additional metrics from existing generations).

### S3 (Must): Acknowledge and Bound Theory-Practice Gap
**Location**: Page 5 - §2.3.2; Page 9 - Conclusion
**Action**: 1) Add a paragraph acknowledging that the O(M⁻¹) convergence guarantee assumes τ=1, and that τ<1 is a practical heuristic. 2) Note that the perplexity guarantee (Proposition 2) applies to the exact qopt, and empirical results represent the approximation quality. 3) Provide a bound or empirical estimate of the approximation gap (e.g., by comparing τ=1 vs τ=0.97 results in ablation).
**Expected benefit**: Aligns theoretical claims with practical implementation, improving scientific credibility.
**Effort**: Low (text revision + one additional experiment variant).

### S4 (Should): Report WIS Diagnostics
**Location**: Page 5 - Algorithm 1 description
**Action**: Report effective sample size (ESS) during µ estimation. Add a note on conditions where WIS may become unreliable.
**Expected benefit**: Ensures reproducibility and helps other researchers apply the method correctly.
**Effort**: Low (computing ESS from existing weight values).

### S5 (Should): Add Temperature-Only Ablation for Perplexity
**Location**: Page 8 - Table 2
**Action**: Add a column showing perplexity of pτ_θ alone (temperature-modulated proposal without EBM reweighting).
**Expected benefit**: Isolates the contribution of the energy function from temperature sharpening.
**Effort**: Low (one additional perplexity computation).

### S6 (Nice-to-have): Expand Human Evaluation
**Location**: Page 7-8 - §3.4-3.5
**Action**: Increase prefix sample size, add inter-annotator agreement (Fleiss' κ), and report absolute Likert-scale ratings in addition to pairwise comparisons.
**Expected benefit**: Strengthens the human evaluation evidence base.
**Effort**: Medium (requires additional annotation budget).

### S7 (Nice-to-have): Broaden Task/Model Validation
**Location**: Page 6 - §3.1
**Action**: Add experiments on at least one additional task (e.g., dialogue generation, story generation) and one additional model family (e.g., LLaMA, GPT-J).
**Expected benefit**: Strengthens generalizability claims.
**Effort**: High (requires additional experiments with new datasets/models).

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: Problem setup (two mis-specifications of LM distribution) → existing methods address only one
- P2: Training-time approaches and their limitations (exposure bias, RL challenges)  
- P3: Proposed solution (DAEMON framework overview + theoretical guarantee + empirical preview)

**Strengths**: The problem framing is clear and technically accurate. The contrast between sampling-based and search-based methods is well-drawn.

**Weaknesses**: (1) No explicit "gap sentence" at end of P1 telling the reader what is missing. (2) P2 critiques training methods but doesn't justify why decoding-time correction is preferable. (3) The transition from P2 to P3 ("In this work, we focus on the decoding route...") is abrupt.

### Abstract Outline (Complete)

**S1 (Problem & Domain)**: "Despite advances in language modeling, current decoding methods fail to simultaneously align generated text with human text across multiple quality aspects such as repetition, coherence, diversity, and information content."

**S2 (Gap)**: "Sampling-based methods improve diversity at the cost of coherence, while search-based methods maintain coherence but increase repetition—no existing method achieves holistic multi-aspect alignment."

**S3 (Proposed Method)**: "We frame decoding as a constrained optimization problem that minimizes reverse KL divergence from the base LM while matching human text on expected metric scores, yielding an analytical EBM solution pθ,µ(x) ∝ pθ(x)·exp(−µᵀf(x))."

**S4 (Theoretical Result)**: "We prove this optimal solution strictly improves perplexity over the original LM and adopt Sampling-Importance-Resampling for tractable sampling from the resulting globally-normalized distribution."

**S5 (Empirical Summary)**: "Experiments on Wikipedia and News domains with GPT-2 XL and OPT-6.7B show improved alignment across all evaluated metrics, corroborated by human evaluation and MAUVE scores."

### Introduction Outline (Complete)

**P1 (Big Picture → Gap)**: Open with the two mis-specifications. End with explicit gap: "A principled framework that simultaneously controls multiple aspects under a unified distributional objective remains an open challenge."

**P2 (Why Decoding-Time)**: Explain why training approaches fall short. End with: "Decoding-time correction avoids retraining, applies to frozen LMs, and can adapt to different quality criteria without modifying model weights—offering a complementary alignment strategy."

**P3 (Solution Preview)**: Present DAEMON's optimization framework, analytical solution, theoretical guarantee, and empirical roadmap. Keep contribution statements explicit and bounded.

**P4 (Contributions)**: List contributions as numbered items for clarity.

### Alternative Storyline Candidates

**Option A (Current**: Problem → Failed Training Approaches → Our Solution → Results

**Option B (Theory-First)**: Information-Geometric Motivation → Constrained Optimization → Analytical EBM Solution → SIR Sampling → Empirical Validation

**Option C (Application-First)**: Decoding Quality Challenge → Multi-Aspect Alignment Failure → DAEMON Framework → Theoretical Guarantees → Experiments

**Recommended**: Blend of B and C. Lead with the practical problem (multi-aspect alignment failure), then motivate the principled optimization framework, then present theoretical results, then empirical validation.

## Priority Revision Plan
### P0 (Before Resubmission — Critical)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | Circular evaluation (Issue 1) | Add held-out metrics; reweight discussion | Removes primary validity concern |
| P0.2 | Missing variance (Issue 2) | Report mean±std over ≥3 seeds; add significance tests | Enables statistical assessment |
| P0.3 | Theory-practice gap (Issue 3) | Acknowledge τ≠1 issue; bound approximation error | Aligns claims with implementation |

### P1 (Before Resubmission — High)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | WIS degeneracy (Issue 4) | Report ESS; consider defensive sampling | Ensures reproducibility |
| P1.2 | Reverse KL trade-off (Issue 5) | Add discussion + empirical evidence | Clarifies framework scope |
| P1.3 | Temperature-perplexity ablation | Add pτ_θ-only column to Table 2 | Isolates EBM contribution |

### P2 (Future Work — Medium)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Human evaluation scope | Increase samples; add inter-annotator agreement | Strengthens evidence |
| P2.2 | Task diversity | Add dialogue/story generation experiments | Broadens generalizability |
| P2.3 | Computational cost analysis | Report peak memory; compare FLOPs | Informs deployment feasibility |

### Revision Sequence

1. **Week 1**: Text revisions (P0.3, P1.2, conclusion bounding) + compute held-out metrics + WIS diagnostics
2. **Week 2**: Multi-seed re-runs for variance reporting (P0.2) + temperature-perplexity ablation (P1.3)
3. **Week 3**: Additional experiments (P2.1, P2.2) if feasible
4. **Week 4**: Full manuscript revision incorporating all changes; update abstract/conclusion to reflect bounded claims

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|-------|---------|--------------|-----------------|------------|
| E1: Main Results (Table 1) | Compare DAEMON vs baselines on metrics alignment | Wikipedia + News; GPT-2 XL + OPT-6.7B | SR-2/3/4, TR-8/16/32, COH, DIV, eENT, MAUVE | DAEMON closest to human references on most metrics | C1: Optimization framework improves alignment | Same metrics as constraints; no variance |
| E2: Perplexity (Table 2) | Compute DAEMON's PPL improvement | Same as E1 | Perplexity of pθ,µ vs pθ | Consistent improvement (e.g., 23.1→22.0 GPT-2 XL Wiki) | C2: Theoretical PPL guarantee | No temperature-only control; PPL of pτ_θ alone not reported |
| E3: Human Eval (Table 3) | Pairwise comparison of DAEMON vs baselines | 100 Wikipedia prefixes; 3 annotators | Fluency, Coherence, Informativeness | DAEMON preferred on all criteria vs CD/CS/Nucleus/Typical | C1, C3 | 100 prefixes only; no inter-annotator agreement |
| E4: Ablation - Metrics (Table 4) | Remove each metric group from constraints | GPT-2 XL, Wikipedia | Same as E1 | Removing any metric degrades corresponding score | C1: Each metric contributes | Small interdependencies not fully analyzed |
| E5: Ablation - M (Figure 3) | Vary number of SIR candidates M | GPT-2 XL, Wikipedia, τ=1.0 | SR-4, TR-32, COH, DIV, eENT | Larger M improves alignment; M=25 chosen for efficiency | C3: SIR approximation quality | τ=1.0 only; main results use τ<1 |
| E6: Ablation - Temperature (Figure 2) | Vary proposal temperature τ | GPT-2 XL, Wikipedia | COH vs DIV trade-off | DAEMON dominates baselines on COH-DIV frontier | C1, C3 | Single domain only |
| E7: Robustness (Appendix H) | Optimize single metric, evaluate all | GPT-2 XL, Wikitext | All metrics | Small variance across optimization targets | C1: Robustness | Grid search only; limited M,τ combinations |
| E8: Summarization (Appendix I) | Apply DAEMON to summarization | CNN/DailyMail; Pegasus model | SR-3, TR-8, COH, DIV, eENT, ROUGE | Improved alignment vs baselines | Generalizability claim | Different model (Pegasus); not comparable with main results |

### Research-Theme Gap Diagnosis

1. **New Knowledge**: The optimization-based decoding framework is novel, but the novelty relative to existing energy-based decoding methods (Deng et al., 2020; Khalifa et al., 2021) cannot be fully assessed without literature retrieval.
2. **Reproducibility**: Partially limited by missing variance estimates and WIS diagnostics.
3. **Impact on Practice**: The framework is practical (1.35× latency) but demonstrated only on two domains and two model families.

### Proposed Research Experiments

| P0 | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Cost | Quality Gain |
|----|-------------|------|-------------|--------------|-------------------|---------|-------------------|------|--------------|
| P0-Exp1 | C1 (Circular Eval Fix) | DAEMON improves held-out metrics not in constraint set | Compute 2 held-out metrics (e.g., FactCC, sentiment) on existing generations | Same baselines as Table 1 | FactCC, sentiment score | DAEMON closest to human references on held-out metrics | Low (compute only) | Removes primary validity concern |
| P0-Exp2 | C1 (Statistical Reliability) | Improvements are stable across seeds | Re-run all experiments with 3 seeds | Same as Table 1 | Mean±std for all metrics | Majority of improvements remain significant at p<0.05 | Medium (3× compute) | Enables significance assessment |
| P0-Exp3 | C3 (τ≠1 gap) | Approximation error from τ<1 is small | Compare τ=1 vs τ=0.97 results on Wikipedia | Same M=25 | All metrics, PPL | τ=0.97 and τ=1 results within 5% of each other | Low (single run) | Quantifies theory-practice gap |
| P1-Exp4 | C2 (PPL source) | EBM contributes beyond temperature sharpening | Compute PPL of pτ_θ alone; compare with DAEMON's PPL | pτ_θ (same τ) vs pθ,µ | PPL | DAEMON PPL < pτ_θ PPL | Low (compute only) | Isolates EBM contribution |
| P2-Exp5 | Generalizability | DAEMON works on dialogue generation | Apply to Topical-Chat or Persona-Chat | Same baselines | Same metrics + BLEU, ROUGE-L | Consistent improvement | High (new task setup) | Broadens scope |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

Rating rationale (10-point scale, emphasizing research value + novelty):

- **Research Value (7/10)**: The optimization-based decoding framework addresses a genuine gap—principled multi-aspect alignment at decoding time without retraining. The theoretical analysis (Proposition 2) is valuable. However, the circular evaluation design weakens the empirical contribution.
- **Novelty (6/10)**: The constrained optimization framing with reverse KL and EBM solution is novel within the decoding literature. However, external literature verification is deferred due to Retrieval-Disabled Mode, so the novelty assessment against energy-based decoding methods (Deng et al., 2020; Khalifa et al., 2021) cannot be completed here and requires manual verification.
- **Validity/Soundness (6/10)**: Strong theoretical foundations but significant gaps between theory (exact solution, O(M⁻¹) convergence) and practice (temperature modulation, WIS approximation, finite M). Missing variance reporting prevents assessment of statistical reliability.
- **Reproducibility (5/10)**: Partially reproducible. Algorithms are clearly specified but missing variance estimates, WIS diagnostics (ESS), and seed information limit full reproducibility.

**Post-Revision Target: [7.0, 7.8]/10**

If all P0 and P1 items are addressed (held-out metrics, variance reporting, theory-practice gap acknowledgment, WIS diagnostics), the score is expected to rise to 7.0–7.8/10. Key uplift drivers: resolving circular evaluation concern (+0.8), adding statistical rigor (+0.5), aligning theoretical claims with practice (+0.3).