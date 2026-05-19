## Summary
# Final Review Report

## Summary

This paper presents FTP (Fine-grained Token-wise Pruner), a dynamic token-skipping framework for accelerating LLM inference. The key idea is to train a lightweight 2-layer MLP router that takes four low-dimensional features (token position, attention score, attention rank, and block-wise sparsity requirement) as input and predicts which tokens in each transformer block can be safely skipped without computation. The router is trained via a three-stage pipeline: (1) GA-based sparsity scheduler search using a static router, (2) dynamic router training with guide loss, sparsity constraint loss, and distillation loss, and (3) sparsity scheduler fine-tuning. Experiments on LLaMA2-7B/13B, LLaMA3-8B, and Qwen1.5-7B across five benchmarks show that FTP retains 96-99% of dense-model accuracy at 22-30% token sparsity, outperforming BlockPruner and ShortGPT by approximately 10-15 percentage points.

**Strengths:** The problem is well-motivated (token-level redundancy in LLMs). The proposed three-stage decoupling of sparsity allocation and router training is a practical contribution. The router design using low-dimensional handcrafted features instead of high-dimensional hidden states is clever and achieves strong empirical results. The evaluation covers multiple model families and sparsity levels.

**Weaknesses (major):** (1) No variance/statistical significance reported across any experiment, making it impossible to assess reliability of the reported rankings; (2) The conclusion lacks any discussion of limitations, failure cases, or actionable future work; (3) The Token Redundancy analysis uses a narrow sample (50 sequences of 64 tokens) without justification of the similarity threshold or sensitivity analysis; (4) The KV-cache threshold is tuned on a single dataset and the significant perplexity gap (5.47 to 11.12) is underreported as a limitation; (5) SOTA claims in Abstract/Introduction use imprecise language and absolute qualifiers that would benefit from tighter scope bounding.

**Novelty:** Due to Retrieval-Disabled Mode in this run, external literature verification was not available. The core technical novelties (designed low-dimensional input factors, three-stage pipeline, GA-based sparsity scheduler) appear to be reasonable contributions over the closest known baseline Mixture-of-Depths (MoD, Raposo et al., 2024), but a definitive novelty judgment requires manual literature verification.

## Strengths
1. **Well-motivated problem and practical framing.** The paper identifies a real bottleneck in LLM deployment—the computational cost of processing every token through every block—and proposes a solution that is practically grounded (no LLM retraining, lightweight router, easy to integrate with existing models). The argument that block-level depth pruning (ShortGPT, BlockPruner) is too coarse-grained is well-supported by the token redundancy analysis in Section 3.1.

2. **Clean three-stage pipeline design.** Decoupling the sparsity scheduler search (GA-based), dynamic router training, and scheduler fine-tuning into separate steps is a sensible approach to a hard joint optimization problem. Each stage has a clear objective and the pipeline can be iterated (though the authors use one iteration for simplicity). This modular design makes the method easier to understand, implement, and extend.

3. **Clever low-dimensional input design.** Instead of feeding high-dimensional hidden states to the router (as done in MoD), the authors propose four handcrafted features: token position, absolute attention score, relative attention rank, and block-wise sparsity requirement. This 4D input makes the router (a 2-layer MLP with hidden size 64) extremely lightweight and sample-efficient to train. The ablation study (Table 5) convincingly demonstrates that this designed input substantially outperforms hidden-state-based alternatives (98.03% vs 86.02% accuracy retention), including combinations that add hidden states on top (87.01%), suggesting the designed features already capture the relevant information.

4. **Comprehensive evaluation scope.** The method is evaluated on four model families (LLaMA2-7B/13B, LLaMA3-8B, Qwen1.5-7B) across five diverse benchmarks (ARC-c, ARC-e, HellaSwag, MMLU, WinoGrande) and at multiple sparsity levels (22%/25%/30%/40%). The consistent trend—FTP outperforms BlockPruner and ShortGPT by substantial margins across all settings—is compelling evidence that the method works as intended.

5. **Honest KV-cache discussion.** The paper explicitly acknowledges the tension between token-wise skipping and KV-cache efficiency (Section 4.4), which is an important practical consideration that many pruning papers overlook. The proposed threshold-based and strict-constraint variants for KV-cache compatibility show thoughtful engineering.

6. **Strong ablation studies.** Tables 3, 4, and 5 systematically validate the contribution of each design choice (sparsity scheduler vs uniform/BI-score allocation, global vs local/recurrent router, each input factor vs ablated versions). This level of ablation significantly strengthens confidence in the method's components.

## Weaknesses
1. **[Major] Missing variance and statistical significance in all experiments.** Every result in Tables 1-6 is reported as a single point estimate without standard deviation, confidence intervals, or significance tests. The GA search involves randomness (initialization, mutation), the router training involves stochastic optimization (batch size 1), and Appendix A.4 shows 5-fold cross-validation for the static router, confirming that variance exists. Without dispersion measures, the reader cannot assess whether the reported improvements (e.g., FTP 99.21% vs FTP static 98.30%, a 0.91 pp gap) are statistically meaningful or within noise range. This is below the standard for ICLR-level empirical work. *(Related annotation: Page 9 - Experiment section)*

2. **[Major] Conclusion lacks scientific completeness.** The Conclusion (Section 5) is only 6 lines long, recaps results with generic SOTA claims, and omits any discussion of limitations, failure cases, or actionable future work. No mention is made of: the perplexity gap (5.47 dense vs 11.12 pruned), the threshold sensitivity for KV-cache, the narrow sample size of the redundancy analysis, or the need for OOD generalization tests. A conclusion that does not bound its own claims reduces the paper's scientific credibility. *(Related annotation: Page 10 - Conclusion)*

3. **[Major] Token redundancy analysis has limited scope and missing sensitivity checks.** The motivating analysis in Section 3.1 uses only 50 sequences of 64 tokens from an unspecified training dataset. This is a very narrow sample for models that routinely process thousands of tokens. The similarity threshold of 0.8 is presented without justification, and there is no sensitivity analysis across thresholds or sequence lengths. The specific dataset used is not named, hindering reproducibility. While the qualitative pattern is likely robust, the quantitative claims ("89.94% of tokens exhibit similarity >0.8") would benefit from broader sampling and explicit variance reporting. *(Related annotation: Page 4 - Token Redundancy)*

4. **[Major] KV-cache threshold tuned on a single dataset and perplexity gap underreported.** The threshold of 0.5 for the last token's sparsity constraint is determined through evaluations on WinoGrande only—no cross-dataset validation is provided. Additionally, the claim of "virtually no performance loss" (Page 10) is misleading: accuracy retention is high (>99%), but perplexity increases from 5.47 (dense) to 11.12 (threshold variant), more than doubling. This distributional shift is not discussed as a limitation. *(Related annotation: Page 10 - KV Cache)*

5. **[Major] SOTA and overclaim language throughout.** The Abstract states "these always introduce additional training costs" despite the paper citing one-shot pruning methods (SparseGPT, Wanda) that do not require retraining. The Introduction uses "tremendously maintaining the accuracies" and "fully demonstrates the superiority"—promotional language that undermines scientific objectivity. Contribution 1 uses "proving" for correlational evidence. These issues are fixable with tighter wording but currently weaken the paper's tone. *(Related annotations: Page 1 - Abstract, Page 1-2 - Introduction)*

6. **[Moderate] Comparison fairness in Table 1.** Sparsity ratios vary across baselines (e.g., BlockPruner at 20.99%, FTP at 22% and 30%). While the magnitude of FTP's advantage makes this unlikely to change the ranking, the term "comparable" in the caption is imprecise. A FLOPs-matched comparison or adding an explicit FLOPs/speedup column would strengthen the comparison. *(Related annotation: Page 8 - Table 1)*

7. **[Moderate] Related Work reads as a list rather than structured positioning.** The LLM Pruning paragraph (Page 2) enumerates methods chronologically without organizing them by comparison axes (e.g., static vs dynamic, weight-level vs token-level, retraining required vs one-shot). This makes it harder for readers to quickly understand where FTP fits in the landscape. *(Related annotation: Page 2 - Related Work)*

8. **[Minor] Static router notation ambiguity.** The ranking notation `{x^i_0, x^i_{L-1}, x^i_{L-2}, ..., x^i_1}` leaves the ordering of intermediate tokens (indices 2 through L-3) underspecified. While the general idea is understandable, explicit documentation would aid reproducibility. *(Related annotation: Page 6 - Static Router)*

## Key Issues
### Ranked Core Defect Board (by severity, research-value impact, validity risk)

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|---------------|------------|------------|
| P0 | Missing variance/statistical significance in all experiments | Major | High — reader cannot assess reliability of rankings | Easy — report std over 3 runs | High |
| P1 | No limitations discussion in Conclusion | Major | Medium — misleading completeness | Easy — add 3-4 sentences | High |
| P2 | KV-cache perplexity gap underreported as "virtually no loss" | Major | Medium — overclaim | Easy — add qualifier | High |
| P3 | Token redundancy analysis narrow scope (50×64-token samples) | Major | Medium — weakens motivational claim | Moderate — add more sequences, threshold sensitivity | Medium |
| P4 | Promotional/hype language in Abstract and Contributions | Major | Low — tone issue, not validity | Easy — replace with precise wording | High |
| P5 | SOTA claim incomparable sparsity ratios in Table 1 | Moderate | Low — unlikely to change ranking | Easy — add FLOPs column or explicit ratio ranges | High |
| P6 | Related Work is a list instead of structured positioning | Minor | Low — readability | Easy — reorganize by axes | High |
| P7 | Static router notation ambiguity | Minor | Low — reproducibility nuance | Easy — expand notation | High |

### Evidence-Sufficiency Assessment

| Core Claim | Evidence Level | Assessment |
|------------|---------------|------------|
| Token-level redundancy exists in LLM blocks (C1) | Level 2 (quasi-experimental: similarity analysis on 50 sequences) | Partially supported; sample size and threshold need strengthening |
| FTP achieves higher accuracy retention than BlockPruner/ShortGPT (C2/C3) | Level 1-2 (descriptive benchmark results, no variance) | Supported in trend but statistical reliability unverifiable |
| Designed 4D input outperforms hidden-state router | Level 2 (ablation with point estimates) | Supported; ablation is clean but needs variance |
| Three-stage pipeline is effective | Level 2 (ablation: SS w/ vs w/o finetune) | Supported |

### Overclaim Audit

| Statement | Location | Verdict | Fix |
|-----------|----------|---------|-----|
| "these always introduce additional training costs" | Page 1 - Abstract | Unsupported (contradicts SparseGPT, Wanda cited in paper) | Replace "always" with "many" |
| "tremendously maintaining the accuracies" | Page 2 - Introduction | Hype language | Replace with "maintains 96-99% accuracy retention" |
| "fully demonstrates the superiority" | Page 2 - Contribution 3 | Hype language | Replace with "results show consistent improvements over baselines" |
| "proving there is much room" | Page 2 - Contribution 1 | Overclaim (correlation ≠ proof) | Replace "proving" with "indicating" |
| "virtually no performance loss" | Page 10 - KV Cache | Misleading (PPL 5.47→11.12) | Add qualifier: "accuracy retention remains >99%" |

## Actionable Suggestions
### S1 (Must) — Add variance reporting for all main results
**Target:** Tables 1-6, all benchmarks. **Effort:** Low (re-run each configuration 3 times with different seeds). **Impact:** High.

Report all results as `mean ± std` over 3 independent runs. For Table 1, also add a footnote: "Results are averaged over 3 runs with different random seeds for GA search and router training. Standard deviations are reported in parentheses." This is the single most impactful change for improving the paper's rigor.

### S2 (Must) — Rewrite Conclusion to include limitations
**Target:** Page 10, Section 5. **Effort:** Low. **Impact:** High.

Add 4-6 sentences covering: (a) the perplexity gap between dense and pruned models, (b) the KV-cache threshold sensitivity, (c) the limited scope of the redundancy analysis, (d) the need for OOD generalization tests, and (e) actionable future work. See the Mentor Revised Version in the Conclusion annotation for a copy-ready rewrite.

### S3 (Must) — Fix overclaim and imprecise language throughout
**Target:** Abstract (Page 1), Introduction contributions (Page 2), KV-cache paragraph (Page 10). **Effort:** Low. **Impact:** Medium.

Replace:
- "always introduce additional training costs" → "many methods introduce additional training costs"
- "tremendously maintaining the accuracies" → "maintains 96-99% of dense accuracy"
- "fully demonstrates the superiority" → "consistently outperforms baselines"
- "proving there is much room" → "indicating substantial pruning potential"
- "virtually no performance loss" → "accuracy retention remains above 99%, though perplexity increases from 5.47 to 11.12"

### S4 (Must) — Strengthen token redundancy analysis
**Target:** Page 4, Section 3.1. **Effort:** Moderate. **Impact:** Medium.

- Specify which dataset was used (presumably Alpaca).
- Add results with longer sequences (e.g., 256, 512 tokens).
- Show sensitivity of the 0.8 threshold (e.g., a table of percentages at thresholds 0.7, 0.8, 0.9).
- Report variance across the 50 sampled sequences.

### S5 (Nice-to-have) — Add KV-cache threshold sensitivity analysis
**Target:** Page 10, Section 4.4. **Effort:** Low. **Impact:** Medium.

Report accuracy retention and PPL for threshold values {0.3, 0.4, 0.5, 0.6, 0.7} across at least 2 datasets (WinoGrande and ARC-c). This demonstrates that 0.5 is not an overfitted choice.

### S6 (Nice-to-have) — Restructure Related Work by comparison axes
**Target:** Page 2-3, Section 2. **Effort:** Low. **Impact:** Medium.

Reorganize the LLM Pruning paragraph into three functional groups: (1) weight-level one-shot pruning (SparseGPT, Wanda), (2) structured/depth pruning requiring retraining (LLM-Pruner, SliceGPT, ShortGPT, BlockPruner), (3) token-level prompt pruning (LLMLingua, Selective Context). End each group with the specific gap that FTP fills. See the Mentor Revised Version in the Related Work annotation.

### S7 (Nice-to-have) — Add FLOPs comparison column to Table 1
**Target:** Page 8, Table 1. **Effort:** Low. **Impact:** Medium.

Since width-pruning (SliceGPT, LLM-Pruner) and token-skipping have different hardware-efficiency profiles even at the same theoretical sparsity, add a column showing actual FLOPs reduction or measured speedup for each method. This makes the comparison more informative and fair.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current Introduction (Page 1-2) follows this paragraph sequence:
- P1: Generic background on LLMs + enumeration of compression techniques
- P2: Garbage paragraph on quantization, distillation, conditional computing (survey-like)
- P3: Depth redundancy argument + transition to token-wise approach
- P4: Method overview + contribution list

**Problems:** P1 and P2 are generic survey paragraphs that delay the paper's core argument. The reader must wait until P3 to understand what is specifically missing in prior work. P2 is particularly problematic because it reads like a textbook rather than a targeted motivation.

### Alternative Storyline Candidates

**Candidate A (Recommended) — Problem-First Arc:**
1. **Opening hook:** LLM inference is dominated by the cost of processing every token through every transformer block.
2. **Specific gap:** Existing pruning methods are either too coarse (block removal) or require retraining; token-level dynamic skipping could bridge this gap but existing routing methods (MoD) need full retraining.
3. **Key insight:** Token redundancy is highly uneven—most tokens change little in middle blocks—and can be predicted from simple attention-derived features.
4. **Solution:** FTP's three-stage pipeline with a lightweight router trained without LLM retraining.
5. **Evidence preview:** 96-99% accuracy retention at 22-30% sparsity, 10-15pp over BlockPruner/ShortGPT.

**Candidate B — Method-First Arc:**
1. **Problem:** Coarse-grained pruning wastes computation on important tokens while skipping computation that matters.
2. **Idea:** What if each block dynamically decides which tokens to process based on a learned importance score?
3. **Challenge:** Hidden-state routers are expensive and need retraining.
4. **Solution:** Low-dimensional features + GA-based sparsity allocation + three-stage training.
5. **Evidence:** Ablations validating each design choice + benchmark results.

**Candidate C — Challenge-Then-Solution Arc (for more technical audiences):**
Same as Candidate A but front-loading the technical challenge: "Simultaneously allocating sparsity ratios across blocks and routing tokens within blocks is a hard joint optimization problem. We decouple it into three tractable steps."

### Selected Storyline: Candidate A

This best aligns the three checks:
- **(a) Problem alignment:** The opening hook directly matches what the method solves (per-token computation per block).
- **(b) Variable alignment:** "Token redundancy", "sparsity scheduler", "dynamic router" introduced in the gap discussion are the paper's key method variables.
- **(c) Contribution-evidence alignment:** The evidence preview directly supports the three stated contributions.

### Abstract Outline (Complete)

- **S1 (Problem & Domain):** "Large language models (LLMs) incur high inference costs because every token is processed through every transformer block, even though many tokens change little in middle blocks."
- **S2 (Challenge):** "Existing pruning methods either remove weights or blocks permanently—risking accuracy loss—or require costly retraining to restore performance."
- **S3 (Gap):** "A fine-grained approach that dynamically skips unimportant tokens per block without retraining the LLM remains underexplored."
- **S4 (Method):** "We propose FTP, which uses a lightweight router trained on four low-dimensional features (token position, attention score, attention rank, block sparsity) to skip less important tokens in each block, guided by a GA-based sparsity scheduler and three auxiliary losses."
- **S5 (Result & Scope):** "On LLaMA2/3 and Qwen1.5 models, FTP retains 96-99% of dense accuracy at 22-30% token sparsity, outperforming BlockPruner and ShortGPT by 10-15 percentage points, without retraining the LLM."

### Introduction Outline (Complete)

- **P1 (Stakes & Problem):** "LLM inference cost grows with model depth and sequence length. The standard approach of computing every token through every block is wasteful because token representations converge gradually."
- **P2 (Prior Work Gap):** "Weight-level pruning methods (SparseGPT, Wanda) avoid retraining but can degrade at high sparsity. Depth-pruning methods (ShortGPT, BlockPruner) remove entire blocks but are too coarse. Conditional computing (MoD) dynamically skips tokens but requires training from scratch. A method that combines fine-grained token skipping with no LLM retraining is missing."
- **P3 (Our Approach):** "We present FTP, a three-stage token-wise pruning framework. First, a GA-based sparsity scheduler allocates pruning ratios per block using a static router. Second, a dynamic router is trained with three losses and four low-dimensional input features. Third, the scheduler is fine-tuned. Crucially, the LLM weights are never updated."
- **P4 (Key Intuition):** "The router's input—token position, attention scores, attention rank, and block sparsity—is designed to capture token importance without relying on high-dimensional hidden states, making the router lightweight and sample-efficient."
- **P5 (Results Preview):** "Across five benchmarks and four LLM families, FTP achieves 96-99% accuracy retention at 22-30% sparsity, surpassing BlockPruner and ShortGPT by substantial margins. Ablations validate each design component."
- **P6 (Contributions):** Listed as in the current paper but with tightened wording (see suggestion S3).

## Priority Revision Plan
### P0 Items (Must fix before resubmission)

| Order | Task | Location | Effort | Impact | Suggested By |
|-------|------|----------|--------|--------|-------------|
| 1 | Add variance/std over 3 runs to all tables | Tables 1-6 | 2-3 GPU-days | High (rigor) | Annotation #12 |
| 2 | Rewrite Conclusion with limitations & future work | Page 10 | 30 min | High (completeness) | Annotation #11 |
| 3 | Replace hype/overclaim language (6 instances) | Abstract, Intro, KV-cache | 20 min | Medium (tone) | Annotations #1, #3, #10 |
| 4 | Strengthen token redundancy analysis (more sequences, threshold sweep, dataset name) | Section 3.1 | 1 day | Medium (motivation) | Annotation #6 |

### P1 Items (Should fix before resubmission)

| Order | Task | Location | Effort | Impact |
|-------|------|----------|--------|--------|
| 5 | Add KV-cache threshold sensitivity analysis | Section 4.4 | 0.5 day | Medium |
| 6 | Restructure Related Work by comparison axes | Section 2 | 1 hour | Medium |
| 7 | Explain asymmetric sparsity constraint loss rationale | Section 3.2 (Eq. 5) | 15 min | Medium |
| 8 | Clarify static router ordering notation | Section 3.2 | 10 min | Low |

### P2 Items (Nice-to-have for quality improvement)

| Order | Task | Location | Effort | Impact |
|-------|------|----------|--------|--------|
| 9 | Add FLOPs/speedup column to Table 1 | Section 4.2 | 0.5 day | Medium |
| 10 | Report distribution of achieved vs target sparsity per block | Appendix | 1 day | Low-medium |
| 11 | Evaluate OOD generalization (e.g., domain-shifted datasets) | New experiment | 2 days | Medium |
| 12 | Ablation on symmetric sparsity constraint vs asymmetric | Appendix | 0.5 day | Low-medium |

### Expected Impact After P0 Fixes

- **Validity:** Adding variance reporting would make the empirical claims statistically verifiable, removing the single largest methodological weakness.
- **Completeness:** A proper Conclusion with limitations closes the scientific loop and protects against reviewer criticism about missing self-critique.
- **Tone:** Replacing hype language with precise, bounded claims would significantly improve reviewer perception of scientific maturity.
- **Motivation:** The redundancy analysis upgrade would make the core motivation more defensible.

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current issues identified]
    |
    +-- P0: Rigor & Completeness
    |       |
    |       +-- Add variance/std (Tables 1-6)
    |       +-- Rewrite Conclusion with limitations
    |       +-- Replace hype/overclaim language
    |       +-- Strengthen redundancy analysis
    |       |
    |       v
    |   [Paper becomes statistically credible]
    |
    +-- P1: Clarity & Positioning
    |       |
    |       +-- KV-cache threshold sensitivity
    |       +-- Restructure Related Work
    |       +-- Explain asymmetric loss rationale
    |       |
    |       v
    |   [Paper becomes easier to read and evaluate]
    |
    +-- P2: Depth & Robustness
            |
            +-- FLOPs column, OOD tests, sparsity distribution
            |
            v
        [Paper achieves ICLR-level completeness]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Main comparison: FTP vs SOTA pruning methods | LLaMA2-7B/13B, LLaMA3-8B, Qwen1.5-7B; 5 benchmarks (ARC-c, ARC-e, HellaSwag, MMLU, WinoGrande); sparsity 22-30% | Accuracy, Avg. Percentage | FTP 96-99% retention, +10-15pp over BlockPruner/ShortGPT | C2, C3 | No variance reported; sparsity ratios not exactly matched across methods |
| E2 | Higher sparsity (40%) evaluation | Same models, 40% sparsity | Accuracy, Avg. Percentage | 85-93% retention across models | C3 | No other method evaluated at 40% for direct comparison |
| E3 | Sparsity scheduler ablation | LLaMA2-7B at 30% sparsity; Uniform, BI-score, SS w/o finetune, SS w/ finetune | ARC-c, MMLU, Avg. Percentage | SS w/ finetune: 98.03% vs Uniform: 72.80%; validates scheduler | C2 | Single model, single sparsity level |
| E4 | Router design ablation | Global vs Recurrent vs Local router | ARC-c, MMLU, Avg. Percentage | Global router 98.03% best | C2 | Single model, single sparsity |
| E5 | Input design ablation | 8 variants: hidden states, DI, DI w/o each factor | ARC-c, MMLU, Avg. Percentage | DI (full): 98.03% vs Hidden states: 86.02% | C2 | Single model, single sparsity |
| E6 | Inference speedup | LLaMA2-7B, Alpaca prompts, token lengths 1000/2000 | Infer Speedup | 1.28-1.61× speedup | Practical impact | Only one model; no comparison to other methods' speedup |
| E7 | KV-cache compatibility | LLaMA2-7B; threshold + strict constraint | ARC-c, MMLU, PPL | Accuracy ~99.9%; PPL 11.12 vs 5.47 (dense) | Practical impact | Threshold tuned on single dataset; PPL gap not discussed as limitation |
| E8 | Static router vs random | LLaMA2-7B at 30%; random selection, priority token experiments | ARC-c, MMLU, Avg. Percentage | Static FTP 97.63% >> Random 68.96% | C2 | Additional model verification missing |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Status | Gap |
|-------------------------|---------------|-----|
| **New Knowledge** | Token redundancy analysis provides empirical evidence but limited in scope | Narrow sample (50×64 tokens); threshold sensitivity unchecked |
| **Reproducibility** | Method description is detailed; code release planned | Missing variance reporting prevents statistical verification; dataset for redundancy analysis not named |
| **Impact on Practice** | Speedup results are promising but limited to one model and two sequence lengths | No latency breakdown (router overhead vs compute saved); no comparison to other methods' actual speedup |

### Proposed Research Experiments

**P0 Experiment: Variance & Statistical Reliability**
- **Target Claim:** All empirical claims (C2, C3)
- **Hypothesis:** FTP's advantage over baselines is statistically significant
- **Minimal Design:** Run all Table 1 configurations with 3 different seeds for GA search + router training; report `mean ± std`
- **Controls/Baselines:** Same seed changes applied to dense model evaluation
- **Metrics:** Accuracy, Avg. Percentage, standard deviation
- **Success Criterion:** FTP's advantage over BlockPruner is >1 std
- **Estimated Cost/Time:** ~2-3 GPU-days (AMD MI250)
- **Expected Paper-Quality Gain:** High — single biggest rigor improvement

**P1 Experiment: KV-Cache Threshold Sensitivity**
- **Target Claim:** FTP is compatible with KV-cache with "virtually no performance loss"
- **Hypothesis:** Threshold 0.5 is robust across datasets
- **Minimal Design:** Evaluate threshold values {0.3, 0.4, 0.5, 0.6, 0.7} on WinoGrande AND ARC-c; report accuracy + PPL
- **Controls/Baselines:** Dense model; FTP without threshold
- **Metrics:** Accuracy, PPL
- **Success Criterion:** <1 pp accuracy variation across thresholds
- **Estimated Cost/Time:** 1 GPU-day
- **Expected Paper-Quality Gain:** Medium — validates KV-cache claim robustness

**P2 Experiment: OOD Generalization Test**
- **Target Claim:** FTP maintains accuracy across diverse tasks (implicit generalization claim)
- **Hypothesis:** FTP's accuracy retention pattern holds under distribution shift
- **Minimal Design:** Evaluate FTP at 22% sparsity on non-IID benchmarks (e.g., TyDiQA for cross-lingual, or a domain-shifted text classification dataset)
- **Controls/Baselines:** Dense model same evaluation
- **Metrics:** Accuracy retention, relative degradation vs dense
- **Success Criterion:** Accuracy retention >90% on at least 2 OOD datasets
- **Estimated Cost/Time:** 1 GPU-day
- **Expected Paper-Quality Gain:** Medium — fills generalization gap in current evaluation

### ASCII Diagram — Experiment Upgrade Plan

```text
                    +-- P0 (Must) --+
                    |               |
                    | Add variance  |---> Rigor foundation
                    | (3 runs, std) |
                    +---------------+
                            |
                            v
              [Claims become statistically verifiable]
                            |
          +-----------------+------------------+
          |                                    |
+-- P1 (Should) --+                +-- P2 (Nice-to-have) --+
| KV threshold     |                | OOD generalization    |
| sensitivity      |                | tests                 |
| sweep            |                |                       |
+------------------+                +-----------------------+
          |                                    |
          v                                    v
[KV-cache claim         [Generalization
 robustness verified]    boundaries established]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Scoring Rationale

The final score prioritizes research value + novelty as primary dimensions, consistent with the policy.

**Research Value (7/10):** The paper addresses a practically important problem (LLM inference acceleration) with a well-designed solution. The idea of using low-dimensional handcrafted features for token routing is clever and the empirical results are strong. However, the scientific completeness is weakened by the absence of variance reporting, limited limitations discussion, and narrow scope of the motivating analysis. The experimental scope is broad (4 models, 5 benchmarks) but lacks OOD validation.

**Novelty (5/10 — tentative, pending external verification):** The combination of GA-based sparsity scheduler, designed 4D input factors, and three-stage pipeline appears to be a non-trivial extension over Mixture-of-Depths (MoD) and depth-pruning methods. However, external literature verification was unavailable in this run, so the novelty assessment is provisional.

**Methodological Soundness (6/10):** The three-stage pipeline is well-motivated and clearly described. The ablation studies are systematic. The main weakness is the lack of statistical significance testing, which is a standard requirement for ICLR-level empirical work. The asymmetric sparsity constraint loss is an interesting design choice but needs justification.

**Reproducibility (6/10):** The method description is reasonably detailed (router architecture, GA parameters, loss functions, training details). Missing elements include: the specific dataset used for the redundancy analysis, the variance of reported results, and the exact attention score computation for the router input. Code is promised but not yet available.

### Final Scores

| Dimension | Score (out of 10) |
|-----------|------------------|
| Research Value & Significance | 7 |
| Novelty (provisional) | 5 |
| Methodological Soundness | 6 |
| Reproducibility | 6 |
| **Final Score** | **6/10** |

**Post-Revision Target:** [7, 8]/10

**Rationale for Post-Revision Target:** If all P0 and P1 items in the Priority Revision Plan are addressed (variance reporting, conclusion rewrite, language tightening, redundancy analysis upgrade, KV-cache sensitivity), the paper would be substantially stronger. The core technical contribution and empirical results are solid enough to support a score of 7-8 after these fixes. The uncertainty (lower bound 7) reflects the unresolved novelty question pending external literature verification.