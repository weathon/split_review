## Summary
This paper addresses the challenge of low-bit (<4-bit) weight-only quantization for large language models (LLMs), where large-magnitude activation outliers amplify quantization errors and degrade model quality. The authors propose two interconnected contributions: (1) **per-input-channel (per-IC) quantization**, a grouping strategy that creates quantization groups along the input-channel dimension rather than the conventional output-channel dimension, isolating outlier effects within individual groups; and (2) **Adaptive Dimensions (AdaDim)**, a lightweight framework that automatically selects per-IC or per-OC quantization per layer by minimizing reconstruction error through only two forward passes. The method is applied to Round-To-Nearest (RTN) and GPTQ, showing consistent improvements across LLaMA and instruction-tuned models (Vicuna, WizardLM) on MMLU (+4.7%), perplexity, and code/math benchmarks (+10% on HumanEval). A per-IC kernel implementation achieves latency speedups over cuBLAS.

**Core strength:** The key insight—rethinking the grouping dimension in per-channel quantization—is simple, well-motivated, and practically effective. The adaptive selection framework elegantly handles the observation that the optimal grouping dimension varies across layers and models.

**Core weaknesses:** (1) No statistical variance or significance testing is reported, making it unclear whether small improvements (0.5-2%) are meaningful. (2) The comparison against AWQ is asymmetric (AWQ is never combined with AdaDim for compatible per-OC layers). (3) The SpQR comparison in the appendix shows that a more sophisticated method outperforms AdaDim at equal bit precision, which is not transparently discussed in the main text. (4) The reconstruction-error-based selection (Eq. 1) uses an unsubscripted norm and has missing dimensionality definitions.

**Novelty verdict:** Novelty claims are deferred for manual verification (external paper search unavailable in this run). The core idea of per-IC grouping appears well-motivated and non-trivial, but a thorough literature comparison against channel-dimension exploration methods is needed.

## Strengths
1. **Well-motivated and intuitive idea.** The core insight—shifting the quantization grouping from output-channel to input-channel to isolate activation outliers—is clearly explained and visually supported (Figure 1). The observation that existing per-OC quantization spreads outlier effects across all groups, while per-IC localizes them, is both simple and compelling. This conceptual clarity is a genuine strength.

2. **Lightweight adaptive framework.** AdaDim requires only two forward passes per layer to determine the optimal quantization dimension, compared to AWQ's 40 forward passes per layer (as noted in Appendix A.3). This minimal overhead makes it practical for real deployment scenarios.

3. **Consistent empirical improvements.** Across multiple model families (LLaMA V1/V2, Vicuna, WizardLM), model scales (7B to 70B), and tasks (perplexity, MMLU, CSR, GSM8k, HumanEval), applying AdaDim consistently improves RTN and GPTQ baselines. The improvement is especially notable for RTN-ada, which can match or exceed GPTQ in several settings despite RTN's simplicity.

4. **Thorough GPTQ ablation.** Table 2 provides a detailed ablation of GPTQ variants (default, reorder, reorder+static) for both per-OC and per-IC dimensions across heuristic and optimization-based selection. This systematic exploration strengthens the paper's empirical foundation.

5. **Open-sourced code and reproducibility consideration.** The authors provide a GitHub repository with the implementation, and Appendix B includes pseudocode for both RTN-ada and GPTQ-ada, which improves reproducibility.

6. **Honest limitation disclosure (partial).** The paper acknowledges that the per-IC kernel is not fully optimized (Section 4.5), that AWQ compatibility is limited (Appendix A.2), and that SpQR can outperform at equal bit precision (Appendix C). This transparency is commendable, though some limitations should be moved to the main text.

## Weaknesses
1. **Missing statistical variance and significance testing.** All experimental results are reported as point estimates without standard deviations, confidence intervals, or significance tests. Given that many reported improvements are small (0.5–2% on MMLU, 1–3 perplexity points), the reader cannot assess whether these gains are statistically reliable or could arise from random seed variation. This is a major methodological gap for a conference paper.

2. **Asymmetric comparison with AWQ.** The paper claims that RTN-ada "surpasses both AWQ and GPTQ" (Section 4.2), but AWQ is tested only in its default configuration. As the authors acknowledge in Appendix A.2, AWQ can be applied to layers where AdaDim selects per-OC quantization. A combined AWQ+AdaDim evaluation is missing, making the comparison incomplete.

3. **SpQR comparison undermines precision parity claims.** Appendix C shows that SpQR outperforms RTN-ada at comparable average bit-precision (Table 9). This is acknowledged but relegated to the appendix, while the main text focuses on improvements over RTN and GPTQ without contextualizing against similarly recent methods.

4. **Contribution C3 is performance-only.** The third contribution bullet ("Augmenting... results in significant boost") describes an empirical outcome rather than a distinct conceptual contribution. Per the review guidelines, performance-only claims without novel intervention should not be standalone contributions.

5. **Equation (1) lacks notational rigor.** The reconstruction error norm lacks an L2 subscript (stated only in text), and the dimensionality of `Xℓ` is not formally defined. The quantization parameter computation (scale, zero-point) is not specified to be independent or shared across the two dimension choices, which could affect fairness of the comparison.

6. **Generic conclusion without bounded limitations.** The conclusion ends with a vague "step forward in the practicality and accessibility of LLMs in real-world applications" without discussing concrete limitations (unoptimized kernel, missing variance, untested architectures, calibration sensitivity).

7. **Per-IC kernel not fully optimized.** The kernel implementation is acknowledged as suboptimal, and its latency is slower than per-OC kernels (LUT-GEMM, OPTQ) in Table 10. The paper claims "measurable speedups" over cuBLAS, but cuBLAS is not a quantization-aware baseline—comparison against OPTQ or LUT-GEMM would be more informative.

8. **Fragmented sentence in critical paragraph.** The sentence "it does not rely on specialized INT8 GEMM kernels impose the per-OC grouping constraint" (Page 1, Introduction) is grammatically broken, impairing readability at the exact point where the core proposal is introduced.

## Key Issues
### Issue 1: Missing Statistical Variance (Severity: Major)
All results are point estimates without variance or significance testing. Improvements of 0.5–2% on MMLU may be within noise range. This undermines confidence in the claim that AdaDim "strictly improves" baselines. **Fix:** Report mean±std over ≥3 seeds for all main experiments; add bootstrap confidence intervals for MMLU.

### Issue 2: Asymmetric Baseline Comparison with AWQ (Severity: Major)
AWQ is tested in its default per-OC configuration only, while AdaDim methods benefit from per-IC on selected layers. Per Appendix A.2, AWQ *can* be applied to per-OC layers selected by AdaDim. The missing AWQ+AdaDim hybrid evaluation means the "surpassing AWQ" claim is not fully validated. **Fix:** Add a combined AWQ+AdaDim experiment for per-OC layers; or explicitly frame the comparison as "AdaDim-augmented RTN/GPTQ vs. default AWQ."

### Issue 3: SpQR Comparison Undermines Bit-Precision Claims (Severity: Major)
The appendix shows SpQR outperforms RTN-ada at comparable bit precision. This is correctly acknowledged but relegated to the appendix. The main text claims of "significant improvements" should be contextualized against similarly recent methods. **Fix:** Move a brief SpQR discussion to the main text; avoid implying precision-competitive SOTA without explicit comparison.

### Issue 4: Contribution C3 is Not a Standalone Scientific Claim (Severity: Minor)
The third contribution bullet is a performance outcome ("augmenting... results in significant boost"), not a conceptual contribution. Per extraction rules, performance-only claims without novel intervention should not be standalone contributions. **Fix:** Merge C3 into experimental framing ("We demonstrate consistent gains across...") rather than listing as a separate contribution.

### Issue 5: Equation Notational Ambiguity (Severity: Minor)
Equation (1) omits the L2 subscript and leaves the dimensionality of Xℓ undefined. Without knowing whether Xℓ is a vector or matrix, the reconstruction error computation is ambiguous. **Fix:** Add `||·||_2` and define `Xℓ ∈ R^{d_in × N}`.

### Issue 6: Generic Conclusion (Severity: Minor)
The conclusion introduces unsupported "real-world applications" framing and lacks concrete limitations and future directions. **Fix:** Replace with validated-findings summary, bounded limitations, and prioritized next steps.

## Actionable Suggestions
### S1: Add Statistical Variance to All Main Results (Must-fix)
Add mean±std over ≥3 random seeds for Tables 1, 3, 4 and Figure 3, 4. For MMLU (57 tasks), report bootstrap 95% confidence intervals by resampling tasks. Add a sentence in Section 4.1 explaining the seeding protocol and significance testing approach. This single change would substantially increase the paper's credibility.

### S2: Add AWQ+AdaDim Hybrid Comparison (Should-fix)
Since AWQ can be applied to per-OC layers selected by AdaDim (Appendix A.2), add a single experiment combining AWQ scaling on per-OC AdaDim layers with RTN or GPTQ-ada on per-IC layers. This would provide a fairer comparison and potentially show further gains. Report this in Table 2 or as a supplementary row in Figure 3.

### S3: Move SpQR Comparison to Main Text (Should-fix)
Add a paragraph in Section 4.4 or Section 5 discussing the SpQR comparison from Appendix C. Frame AdaDim's contribution as simplicity and compatibility ("AdaDim requires no sparse kernel or FP16 outlier storage, unlike SpQR") rather than raw accuracy. This transforms a weakness into a clearer value proposition.

### S4: Restructure Contribution Statements (Nice-to-have)
Merge the three bullet contributions into two conceptual claims (per-IC quantization + AdaDim framework) plus one experimental summary. Remove or rephrase C3 as an empirical finding rather than a standalone contribution.

### S5: Fix Equation (1) Notation (Nice-to-have)
- Add L2 subscript: `||·||_2`
- Define `Xℓ ∈ R^{d_in × N}` as a matrix of N calibration activation vectors
- Clarify that quantization parameters (scale, zero-point) are computed independently for each dimension

### S6: Rewrite Conclusion (Nice-to-have)
Replace the generic conclusion with a structured format: (a) validated findings with scope bounds, (b) concrete limitations (3-4 bullet points), (c) prioritized future work items.

### S7: Repair Fragmented Sentence in Introduction (Must-fix)
Page 1, Introduction paragraph 2: "it does not rely on specialized INT8 GEMM kernels impose the per-OC grouping constraint" → "it does not rely on specialized INT8 GEMM kernels that impose the per-OC grouping constraint."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current narrative flows as: LLMs are successful but memory-bound → weight quantization helps but sub-4-bit is hard due to outliers → per-IC quantization isolates outliers → AdaDim adapts dimension selection → experiments show improvements. This is functional but could be significantly sharpened.

**Problem alignment check:** The stated challenge (activation outliers) directly matches the proposed solution (per-IC grouping). **Pass.**

**Variable alignment check:** Core concepts (IC, OC, grouping dimension, outlier isolation) introduced early appear consistently through method and experiments. **Pass.**

**Contribution-evidence alignment check:** Abstract claims "up to +4.7% on MMLU" and "+10% on HumanEval" are supported by Tables 3/4 and Figure 3. However, the causal mechanism linking per-IC grouping to these gains is only qualitatively shown (Figure 6). **Partial pass.**

---

### Abstract Outline (Complete)

**S1 (Problem & Domain):** "Large Language Models (LLMs) achieve strong performance but face a memory bottleneck in small-batch inference settings, where each generated token requires reading the full weight matrix from VRAM."

**S2 (Prior Gap):** "Weight-only quantization reduces memory by packing low-bit weights, but sub-4-bit precision degrades accuracy because activation outliers amplify quantization errors across all output-channel groups."

**S3 (Proposed Method):** "We propose per-input-channel (per-IC) quantization, which creates quantization groups along the input dimension, isolating outlier effects within individual groups. Building on this, we introduce Adaptive Dimensions (AdaDim), a lightweight framework that automatically selects between per-IC and per-OC quantization per layer by minimizing reconstruction error."

**S4 (Key Result + Scope):** "Augmenting RTN and GPTQ with AdaDim consistently improves perplexity and task accuracy across LLaMA and instruction-tuned models. Under INT3 precision, AdaDim yields gains of up to +4.7% on MMLU and +10% on HumanEval compared to per-OC baselines."

**S5 (Code/data):** "Code is available at https://github.com/johnheo/adadim-llm."

---

### Introduction Outline (Complete)

**P1 — Establish stakes and gap.** Role: State the deployment problem (memory bandwidth), explain why weight-only quantization is promising, and identify the specific obstacle (activation outliers make sub-4-bit difficult). Explicitly state why existing methods (mixed-precision, scaling) are insufficient—they require specialized kernels or hardware modifications that limit adoption.

**P2 — Core idea and mechanism.** Role: Introduce per-IC quantization with the geometric intuition (Figure 1). Clearly explain *why* grouping along the input dimension isolates outliers (1:1 mapping between hidden dimension and quantization group) while per-OC spreads outlier effects across all groups. End with the insight that the optimal grouping dimension varies per layer.

**P3 — AdaDim framework.** Role: Introduce AdaDim as the adaptive selection mechanism. Explain the reconstruction-error minimization objective. Emphasize the minimal cost (2 forward passes per layer). State that AdaDim is a plugin that can augment existing methods (RTN, GPTQ).

**P4 — Contribution summary and roadmap.** Role: List contributions clearly (per-IC quantization concept, AdaDim framework, empirical validation). End with a one-sentence paper roadmap.

---

### Alternative Storyline Candidates

**Candidate A (Mechanism-First):** Start with weight sensitivity analysis (Section 3.1, Figure 2) and use it to motivate why a *variable* grouping dimension is needed. Then introduce per-IC as the tool to handle outlier-driven sensitivity. *Advantage:* Stronger logical foundation for why OC→IC switching helps. *Disadvantage:* Delays the simple intuitive idea (isolate outliers) to after a data-driven analysis.

**Candidate B (Problem-Focused):** Start with a concrete deployment scenario (e.g., serving LLaMA-70B on a single GPU) and calculate the memory savings from INT3 vs INT4 vs FP16. Use this to motivate why every bit matters, then introduce the outlier problem. *Advantage:* More engaging for practitioners. *Disadvantage:* Requires numeric example that may date quickly.

**Recommended: Current structure with Candidate A's sensitivity analysis moved earlier.** Move the weight sensitivity observation (Figure 2) to the introduction's second paragraph to immediately establish *why* per-OC quantization is suboptimal, before presenting per-IC as the solution. This would create a clear: Problem (outliers affect per-OC) → Evidence (sensitivity varies across layers) → Solution (per-IC + AdaDim) narrative arc.

## Priority Revision Plan
### P0 — Critical (must fix before acceptance)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|----------------|
| P0 | Missing statistical variance | Add mean±std ≥3 seeds for all main results; bootstrap CI for MMLU | Prevents dismissal of small gains as noise; establishes reliability |
| P0 | Asymmetric AWQ comparison | Add AWQ+AdaDim hybrid experiment for per-OC layers | Fairer comparison; potentially stronger results |
| P0 | Fragmented sentence (p1 intro) | Fix grammar: "kernels impose" → "kernels that impose" | Core proposal readability |

### P1 — High priority (should fix before submission)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|----------------|
| P1 | SpQR comparison buried | Move comparison to main text (Section 4.4 or 5); reframe AdaDim value as simplicity | Honest positioning; clearer value proposition |
| P1 | Contribution C3 inflation | Merge C3 into experimental framing | Cleaner contribution structure |
| P1 | Equation (1) notation | Add L2 subscript; define Xℓ dimensionality | Improved reproducibility |

### P2 — Quality improvement (nice to have)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|----------------|
| P2 | Conclusion generic | Replace with structured findings + limitations + future work | Stronger closure |
| P2 | Related work list structure | Reorganize Section 2.1 by comparison axes (regime, granularity) | Better positioning |
| P2 | Abstract secondary finding | Move "activation outliers do not dictate difficulty" to main text | Focused abstract |
| P2 | "Strictly improves" wording | Replace with "consistently improves" | Factual precision |

### Revision Effort Estimate

- **P0 items:** ~2-3 days (running multi-seed experiments + writing AWQ hybrid)
- **P1 items:** ~1 day (reorganizing text, fixing notation, moving appendix content)
- **P2 items:** ~0.5 day (writing improvements)
- **Total estimated effort:** ~3-5 person-days

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Validate per-IC outlier isolation (Table 1) | LLaMA-V2 7B/13B, INT4 g128, RTN, selective per-IC on QKV/DOWN | Wiki-2 PPL, MMLU 5-shot | Per-IC on outlier modules improves over per-OC baseline | C1 (per-IC isolates outliers) | No variance; only 2 model sizes |
| E2 | Compare heuristic vs. adaptive selection (Table 2) | LLaMA-V2-13B, INT3 g128 | MMLU 5-shot | Adaptive selection (AdaDim) outperforms fixed heuristic | C2 (AdaDim adaptivity) | Single model; single metric |
| E3 | Base model comparison (Figure 3) | LLaMA V2 7B/13B/70B, V1 33B; INT3 g128 | MMLU 5-shot, CSR 0-shot | AdaDim improves RTN/GPTQ; RTN-ada surpasses AWQ in some settings | C3 (empirical gains) | No variance; AWQ compared at default only |
| E4 | Instruction-tuned evaluation (Table 3) | Vicuna-V1.5 7B/13B, V1.3 33B; INT3 g128 | MMLU Avg, CSR Avg | AdaDim brings consistent gains; notable at 33B scale (~2% degradation bridged) | C3 | Small gains (0.1-2%); no significance test |
| E5 | Task-specific quantization (Table 4) | WizardMath 7B/13B, WizardCoder 7B/13B; base vs. target calibration | GSM8k pass@1, HumanEval pass@1 | Target calibration improves; AdaDim adds further gains up to +10% | C3 | Calibration sample variability not studied |
| E6 | Precision sweep (Figure 4) | LLaMA-V2-7B; INT3/INT4 × g256/128/64 | Wiki-2 PPL, MMLU | AdaDim strictly improves PPL across all configs | C2 (generality) | "Strictly" overclaim without variance |
| E7 | Reconstruction error analysis (Figure 5) | LLaMA-V2 7B; RTN-ada decisions | Reconstruction error (L2) | Per-IC reduces error up to 6×; decisions vary by layer/model/task | C2 | Single metric; no comparison with other selection methods |
| E8 | GPTQ update analysis (Figure 6) | LLaMA-V2-7B attn.v layer | Weight update magnitude | Per-IC uses larger localized updates | C1 (mechanism) | Qualitative; no quantitative perturbation metric |
| E9 | Per-IC kernel latency (Figure 7, Table 10) | OPT-175B FFN; INT3/INT4 × g128-2048 | Latency (ms) | Per-IC faster than cuBLAS but slower than LUT-GEMM | Feasibility | Suboptimal kernel; comparison against cuBLAS not quantization-aware |
| E10 | Calibration size ablation (Table 5, Appendix C) | LLaMA-V2 7B/13B, INT3 g128; samples 32-512 | MMLU, CSR | 256 samples is optimal | Robustness | No theoretical analysis of sample complexity |
| E11 | SpQR comparison (Tables 8-9, Appendix C) | LLaMA-V1 7B/33B/65B; various bit-widths | Wiki-2 PPL, C4 PPL | At equal avg bits, SpQR outperforms RTN-ada | Honest comparison | RTN-ada has higher avg bits in Table 8 |

### Research-Theme Gap Diagnosis

**New knowledge:** The paper introduces a novel conceptual contribution (per-IC grouping as a design parameter). However, the *causal mechanism* linking per-IC grouping to improved quantization is supported only by qualitative visualization (Figure 6), not quantitative perturbation measures. The key insight is plausible but not rigorously verified.

**Reproducibility/reusability:** Code is provided and pseudocode is included (Appendix B), which supports reproducibility. However, the unreported variance and undefined calibration sample selection protocol (beyond "randomly sampling") create uncertainty.

**Impact on practice/understanding:** The finding that quantization difficulty is jointly determined by activation outliers *and* inherent weight sensitivity (not outliers alone) is an important insight that could influence future quantization design. However, this insight is not sufficiently foregrounded in the narrative.

### Proposed Research Experiments (P0/P1/P2)

#### Experiment P0a: Seed Variance and Significance (Must-fix)
- **Target Claim:** All main results (AdaDim improves RTN/GPTQ)
- **Hypothesis:** Observed gains are statistically significant
- **Minimal Design:** Run RTN, RTN-ada, GPTQ, GPTQ-ada with 5 random seeds on LLaMA-V2-7B with INT3 g128. Compute mean±std for MMLU and CSR. Report paired bootstrap p-values for RTN-ada vs. RTN and GPTQ-ada vs. GPTQ.
- **Controls/Baselines:** Same seed order, same calibration samples
- **Metrics:** MMLU 5-shot, CSR 0-shot, Wiki-2 PPL
- **Success Criterion:** All comparisons show p<0.05 or non-overlapping 95% CIs
- **Estimated Cost/Time:** ~2 days (5 seeds × 4 methods × 1 model)
- **Expected Quality Gain:** Converts core claims from "suggestive" to "statistically validated"

#### Experiment P0b: AWQ+AdaDim Hybrid (Should-fix)
- **Target Claim:** "Surpassing AWQ" comparison fairness
- **Hypothesis:** AWQ scaling on per-OC AdaDim layers + baseline on per-IC layers provides further gains
- **Minimal Design:** For LLaMA-V2-7B/13B, apply AWQ scaling factors only to layers where AdaDim selects per-OC, then run RTN-ada/GPTQ-ada
- **Controls:** Default AWQ (all layers per-OC), default AdaDim (no AWQ)
- **Metrics:** MMLU 5-shot, CSR 0-shot
- **Success Criterion:** AWQ+AdaDim hybrid matches or exceeds AdaDim alone
- **Estimated Cost/Time:** ~1 day
- **Expected Quality Gain:** Fairer comparison; potentially stronger headline numbers

#### Experiment P1a: Quantitative Perturbation Analysis (Should-fix)
- **Target Claim:** "Per-IC minimally perturbs the weight distribution" (Section 4.4)
- **Hypothesis:** Per-IC induces lower total weight perturbation than per-OC
- **Minimal Design:** Compute ||W_quantized - W_fp16||_F (Frobenius norm) per layer for per-IC vs. per-OC quantization under GPTQ. Also report fraction of weights changed by >1%. Violin plot of per-weight update magnitudes.
- **Controls:** Same layer, same quantization method, only dimension differs
- **Metrics:** Frobenius norm ratio (per-IC / per-OC), % weights changed >threshold
- **Success Criterion:** Per-IC shows significantly lower total perturbation
- **Estimated Cost/Time:** ~0.5 day (computational; runs already exist)
- **Expected Quality Gain:** Transforms qualitative visual analysis into quantitative evidence

#### Experiment P2a: Non-LLaMA Architecture Validation (Nice-to-have)
- **Target Claim:** Generality of AdaDim across architectures
- **Hypothesis:** AdaDim also benefits GPT-2, OPT, or Falcon quantization
- **Minimal Design:** Apply RTN-ada and GPTQ-ada to GPT-2 (1.5B) or OPT-6.7B with INT3 g128; report PPL and task accuracy
- **Controls:** Standard per-OC RTN/GPTQ baselines
- **Metrics:** Wiki-2 PPL
- **Success Criterion:** Consistent PPL improvement over per-OC baseline
- **Estimated Cost/Time:** ~1 day
- **Expected Quality Gain:** Demonstrates broader applicability beyond LLaMA family

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Scoring rationale:**
- **Research value (7/10):** The core insight (per-IC grouping as a design parameter) is well-motivated and practically useful. The lightweight nature of AdaDim (2 forward passes) is a genuine advantage. However, the value is somewhat diminished by the missing variance analysis (cannot confirm small gains are real) and the SpQR comparison showing that more sophisticated methods outperform at equal bit precision.
- **Novelty (6/10):** The per-IC grouping idea appears non-trivial and well-justified. However, external literature verification is deferred (Retrieval-Disabled Mode). The conceptual contribution is incremental rather than groundbreaking—it repurposes an existing grouping strategy (per-channel quantization) along a different axis rather than introducing a fundamentally new quantization paradigm.
- **Methodological soundness (6/10):** The method is clearly described and the adaptive selection is elegant. However, the missing statistical rigor (no variance, no significance tests), the asymmetric AWQ comparison, and the uncontrolled bit-precision in the SpQR comparison reduce confidence in the reported results.
- **Reproducibility (7/10):** Code is provided, pseudocode is included, and the calibration/data setup is described. The main reproducibility gaps are the undefined calibration sampling protocol and unreported seed values.

**Post-Revision Target: [7.5, 8.0] / 10**

If the authors address the P0 items (add statistical variance, fix AWQ comparison, repair fragmented sentence) and P1 items (move SpQR discussion to main text, fix equation notation, restructure contributions), the paper would be significantly strengthened. The core idea is sound and the experimental trend is consistent—what is needed is rigorous statistical backing and fairer comparisons. Achieving this target would require:
- Adding seed variance and significance tests to all main results
- Adding AWQ+AdaDim hybrid experiments
- Repositioning the contribution narrative to be more precise about comparison scope
- Including a quantitative perturbation metric for the mechanism analysis

These changes are feasible within a standard revision cycle (estimated 3-5 person-days).