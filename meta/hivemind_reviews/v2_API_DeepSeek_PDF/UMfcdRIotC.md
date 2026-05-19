## Summary
This paper proposes two model-agnostic approaches for explaining black-box NLP model predictions via counterfactual (CF) approximation. The first approach uses LLMs (ChatGPT, T5) to directly generate CFs by rewriting text while holding confounders fixed. The second approach learns a causally-informed embedding space via contrastive learning, using LLM-generated CFs only at training time; at test time it matches query examples to pre-existing candidates. The paper also introduces Order-faithfulness, a theoretical criterion for explanation methods, and proves that CF-based methods satisfy it while non-causal methods can fail.

The main empirical results on the CEBaB benchmark with five explained models show: (1) generative CF methods achieve the lowest explanation error among tested approaches, (2) the proposed causal representation model outperforms all matching baselines, and (3) Top-K aggregation improves all methods. A new stance detection benchmark (using GPT-4-generated CFs as ground truth) validates these findings under distribution shift. The paper includes thorough ablation studies, latency comparisons, and a theoretical appendix.

Overall, the paper addresses an important problem (faithful, model-agnostic NLP explanation) with sound motivation and solid methodology. However, several claims (SOTA for generative methods, universal Top-K benefit) are stronger than the single-benchmark evidence supports, and the lack of statistical significance testing weakens the empirical ranking claims. The theoretical contribution is well-structured but relies on assumptions that merit more critical discussion. The matching approach is a practical contribution with clear efficiency advantages, though it remains outperformed by generative methods.

## Strengths
1. **Important problem with practical motivation.** The paper tackles the critical challenge of faithful, model-agnostic explanation for black-box NLP models. The connection between causality and faithfulness is well-motivated, and the practical efficiency advantages of matching over generation are clearly articulated.

2. **Clean theoretical contribution.** The Order-faithfulness criterion is a well-defined, intuitive concept. Theorem 1 cleanly separates CF-based methods (always order-faithful under zero-mean approximation error) from non-causal methods (which can fail). The proof is rigorous and provided in full in the appendix.

3. **Novel technical approach for matching.** The causal representation learning method with four contrastive training sets (XCF, XM, X¬CF, X¬M) is technically innovative. The six-component contrastive objective is well-motivated and ablation studies (Table 4, Appendix C) convincingly show that each component contributes to robustness.

4. **Comprehensive evaluation across model scales.** The paper explains five different models (DistilBERT, BERT, RoBERTa, Llama2-7B, Llama2-13B), demonstrating that the explanation methods work across model families and sizes. This strengthens the model-agnostic claims.

5. **Strong ablation and efficiency analysis.** Appendix C provides thorough ablation across candidate set variations, backbone encoders, and objective component removal. Table 3 clearly quantifies the inference-time efficiency gains of matching over generation (up to 1000x in batch mode).

6. **New benchmark construction demonstration.** The paper demonstrates how LLMs can be used to construct explanation benchmarks (stance detection). While this raises circularity concerns, it is a forward-looking contribution that may reduce annotation costs for future work.

7. **Top-K analysis with clear visualizations.** Figures 2 and 3 provide intuitive visualization of how match rank relates to explanation quality, with the desirable ✓-shaped curve of the causal model clearly distinguished from baselines.

## Weaknesses
1. **Missing statistical significance and variance reporting.** All experimental results in Table 2 are point estimates without standard deviations, confidence intervals, or significance tests. The core empirical claim — ranking explanation methods by accuracy — cannot be statistically verified. Differences as large as 0.02-0.05 L2 between methods could be within noise range, and the conclusion that "all matching baselines are competitive and perform similarly" is not testable without variance estimates.

2. **SOTA claims exceed evidence scope.** The paper asserts LLM-generated CFs are "SOTA model-agnostic explainers" based on a single benchmark (CEBaB, N=1688 test). Most non-matching baselines from prior work (LIME, integrated gradients, CPM) are excluded by citing Abraham et al. (2022)'s result that Approx outperforms them. Without direct comparison, the SOTA claim is unverifiable. Additionally, the paper uses "SOTA" to describe generative methods that are themselves slower and more expensive than the matching alternative — a nuanced positioning is needed.

3. **New benchmark circularity concern.** The stance detection benchmark (Section 6) uses GPT-4 to generate both the training data modifications and the "golden CFs" used as evaluation ground truth. Since the generative explanation methods also use models from the same family (ChatGPT, GPT-4), there is a risk of inflated agreement due to shared model biases. The paper acknowledges this implicitly but does not conduct a control experiment with human-written CFs for validation.

4. **Theoretical assumption boundary conditions.** The Order-faithfulness theorem assumes (Definition 1) that approximated CFs have zero-mean approximation error (E[ϵ]=0). In practice, LLM-generated CFs may exhibit systematic bias (e.g., tendency toward shorter texts, avoidance of certain constructions, mode collapse). If E[ϵ]≠0, the unbiasedness of SCF and hence its guaranteed order-faithfulness may not hold. The paper does not empirically assess the bias of LLM-generated CFs.

5. **Top-K hyperparameter selection is post-hoc.** The paper states K=10 was "arbitrarily opted" even though K=20 would be "more advantageous" for the causal model. Selecting K based on test-set performance constitutes data leakage. A principled validation-based selection is needed.

6. **Limited task and domain diversity.** All main experiments are on a single task (5-class sentiment analysis of restaurant reviews). The stance detection experiment uses the same causal graph structure. Generalizability to other NLP tasks (e.g., summarization, question answering, natural language inference) or other causal graph structures is unexplored.

7. **Matching method's dependency pipeline.** The causal representation model depends on accurate LLM-generated CFs (ChatGPT) and concept predictors (RoBERTa). Errors in either component can propagate through the contrastive learning pipeline, but this error amplification is not analyzed.

## Key Issues
### Issue 1 (Major): Missing statistical significance and variance reporting
**Location:** Page 7-8 - Results section and Table 2
**Severity:** Major | **Type:** Issue

All Err scores in Table 2 are reported as point estimates without variance, confidence intervals, or significance tests. This is critical because:
- The paper's central empirical claim — ranking explanation methods by accuracy — has no statistical grounding.
- The claim that "all matching baselines are competitive and perform similarly" cannot be verified without knowing whether differences (e.g., Causal Model L2=0.66 vs PT RoBERTa L2=0.75) are significant.
- The claim that "Fine-tune Generative is the best generative model" (L2=0.38 vs 0.42 zero-shot) may not be reliable.
- The Top-K benefit analysis (Figure 3) is presented deterministically without uncertainty quantification.

**Required action:** Report mean ± std over ≥3 random seeds for all experiments in Table 2. Add paired significance tests (e.g., Wilcoxon signed-rank) comparing the best generative method against the best matching method for each explained model.

### Issue 2 (Major): SOTA claim unsupported by direct comparison with prior SOTA methods
**Location:** Page 1-2 - Abstract, Introduction; Page 7 - Results
**Severity:** Major | **Type:** Issue

The paper claims "LLM-generated CFs are the SOTA model-agnostic explainers" but:
- Only compares against matching baselines and excludes most non-matching explanation methods (LIME, integrated gradients, Causal Proxy Model, SHAP, etc.) by citing Abraham et al. (2022)'s result that Approx outperforms them. This indirect comparison is insufficient to support a SOTA claim.
- CPM (Wu et al. 2023a) is discussed in Related Work but not compared empirically.
- The stance detection experiment (Table 6) compares only against matching baselines, not against other explanation methods.

**Required action:** Either (a) include at least 2-3 representative non-matching explanation methods in the CEBaB comparison, or (b) downgrade the claim from "SOTA" to "achieves low explanation error relative to matching-based alternatives."

### Issue 3 (Major): GPT-4-generated CFs as ground truth create circular evaluation risk
**Location:** Page 9 - Section 6; Page 23-24 - Appendix D
**Severity:** Major | **Type:** Issue

The new stance detection benchmark uses GPT-4 to generate both the text modifications and the "golden CFs" used as evaluation targets. The generative explanation methods (ChatGPT-based, T5 fine-tuned) belong to the same model family as GPT-4. If GPT-4's counterfactuals share systematic biases with the explanation methods' outputs, the evaluation may overestimate explanation quality. The paper's validation of main conclusions on this benchmark is thus potentially weaker than claimed.

**Required action:** Validate the stance detection benchmark's ground-truth CFs with human annotators on a subset (N=100). Report agreement rates and recompute Err scores using human-validated CFs to confirm the relative method rankings are preserved.

### Issue 4 (Major): Unbounded Top-K hyperparameter selection
**Location:** Page 8 - Results / Top-K analysis
**Severity:** Major | **Type:** Issue

K=10 was "arbitrarily opted" even though K=20 would be "more advantageous" for the causal model. Selecting K post-hoc based on test-set observations constitutes a form of data leakage. The paper also does not provide a principled method for choosing K in practice.

**Required action:** (a) Select K using a held-out validation set and report performance at the selected K on the test set. (b) Add a sensitivity analysis showing Err as a function of K for K=1,5,10,20,50 across all explained models.

### Issue 5 (Major): Zero-mean approximation error assumption in Theorem
**Location:** Page 4 - Section 3.1; Page 18 - Appendix A, Definition 1
**Severity:** Major | **Type:** Verification

Definition 1 assumes E[ϵ]=0 for approximated CFs. This is a strong assumption: LLM-generated CFs may have systematic biases. The paper does not empirically test whether this assumption holds for ChatGPT/T5-generated CFs. If violated, the guaranteed order-faithfulness of CF-based methods may not hold in practice.

**Required action:** (a) Add an empirical analysis of CF generation bias: compute the mean of f(\tilde{x}_{t'}) - f(x_{t'}^{gold}) across test examples. If significantly non-zero, the bias violates the assumption. (b) Discuss the practical implications of assumption violations in the limitations section.

## Actionable Suggestions
### Must-do (Publication-Critical)

**S1: Add statistical significance and variance to all experiments (Key Issues 1, 5)**
Run all explanation methods with 3 random seeds on the CEBaB benchmark. Report mean ± std for all Err metrics in Table 2. Add a paired significance test (e.g., Wilcoxon signed-rank or McNemar's test) comparing each method against the best-performing one for each explained model. This is the single most important revision — without it, the empirical ranking claims are unverifiable.

**S2: Bound SOTA claims to available evidence (Key Issue 2)**
Replace "SOTA model-agnostic explainers" with "achieves the lowest explanation error among tested matching and generative baselines on the CEBaB benchmark." Remove or qualify the "SOTA" label in the abstract and introduction unless direct comparison with at least 2-3 prior explanation methods (e.g., LIME, Causal Proxy Model, Integrated Gradients) is added.

**S3: Validate stance detection benchmark with human-annotated CFs (Key Issue 3)**
Sample 100 test examples from the stance detection dataset and have 3 annotators write counterfactuals or verify LLM-generated CFs. Report the agreement rate between GPT-4 CFs and human CFs, and recompute Table 6 Err scores on the human-validated subset. If the relative method rankings are preserved, this strengthens the paper's conclusions substantially.

**S4: Principled K selection for Top-K (Key Issue 4)**
Split the CEBaB development set into a validation split (N=800) and a test split (N=872). Select K as the value minimizing Err on the validation split. Report test-set results at the validation-selected K alongside a sensitivity analysis (K=1,5,10,20,50). Remove the phrase "arbitrarily opted."

**S5: Assess zero-mean approximation error (Key Issue 5)**
Compute the empirical bias E[f(\tilde{x}_{t'}) - f(x_{t'}^{gold})] for each generative method and each intervention type. If the bias is significantly non-zero, (a) discuss how this affects the order-faithfulness guarantee, and (b) consider a bias-corrected estimator.

### Nice-to-have (Quality Improvement)

**S6: Expand the range of explained models and tasks (Weakness 6)**
Add at least one non-sentiment NLP task (e.g., natural language inference on SNLI, or toxicity detection on Jigsaw). This would significantly strengthen the generalizability claims.

**S7: Include non-matching baselines in comparison (Key Issue 2)**
Add LIME and at least one other feature-attribution method to Table 2. While these are not CF-based, including them contextualizes the absolute error values and supports the claim that CF-based methods are more effective.

**S8: Analyze error propagation in the matching pipeline (Weakness 7)**
Add a simulation study where concept predictor accuracy and CF generation quality are systematically degraded to measure how the causal model's matching performance degrades. This would help practitioners understand when the matching approach is reliable.

**S9: Clarify the \hat{CaCE} estimator notation (Annotation on Page 3)**
Simplify or remove the third term in the \hat{CaCE} estimator (Eq. 2), which involves ambiguous cross-pairing. Provide a clearer estimator with properly defined sampling sets.

**S10: Restructure Related Work by comparison axes (Annotation on Page 2-3)**
Organize the Related Work section by decision-relevant axes (model access required, CF generation method, evaluation protocol) rather than paper-by-paper chronological summaries.

## Storyline Options + Writing Outlines
### Current Storyline Map

The current introduction uses a compressed structure:
- P1: Faithfulness requires causality → we propose theory + two methods (too compressed)
- P2: Order-faithfulness criterion + model-agnostic benefits
- P3: CF acquisition limitations → LLM generation → matching
- P4: Matching details + empirical preview + new benchmark
- P5: Related Work (two static paragraphs)

The main issue is that P1 tries to introduce theoretical framework AND two methods in one sentence, while P4 introduces matching BEFORE the reader has seen the method details. The narrative jumps between theory, methods, and results too quickly.

### Best Storyline Candidate: "Problem → Gap → Theory → Method1 → Method2 → Evidence"

This structure separates theoretical and methodological contributions into a logical progression:

- **P1 (Big Picture):** Faithful explanation is critical for NLP safety. Current methods struggle because faithfulness requires causality, but causal estimation is difficult without access to the data-generating process.
- **P2 (Gap):** Prior CF-based methods are limited to simple manipulations or expensive manual annotation. Model-agnostic methods are needed for model selection and debugging across multiple black-box models.
- **P3 (Theory):** We introduce Order-faithfulness — a necessary condition for faithful explanation — and prove that CF-based methods satisfy it while non-causal methods can fail (Theorem 1).
- **P4 (Solution — Generation):** We propose LLM-based CF generation: prompt an LLM to intervene on a concept while holding confounders fixed. This achieves low explanation error but is costly at inference time.
- **P5 (Solution — Matching):** We propose an efficient alternative: learn a causally-informed embedding space using contrastive learning with LLM-generated supervision at training time. At test time, matching to pre-existing candidates is up to 1000x faster than generation.
- **P6 (Evidence Preview):** On the CEBaB benchmark across 5 models (including Llama2-13B), we show: (1) generative CFs achieve low explanation error, (2) our matching method outperforms all matching baselines, (3) Top-K improves all methods.

### Abstract Outline (4-sentence structure)

**S1 (Problem & Significance):** "Faithful explanations of black-box NLP model predictions are essential for safety and trust, but existing methods are often model-specific, costly, or inefficient."
**S2 (Gap & Proposed Solution):** "We propose two model-agnostic approaches based on counterfactual (CF) approximation: CF generation using LLMs, and a matching method that learns a causally-informed embedding space from LLM-generated supervision."
**S3 (Key Result — Empirical):** "On the CEBaB benchmark across five explained models (including Llama2-13B), generative CFs achieve the lowest explanation error, while matching reduces inference latency by up to 1000x and outperforms all matching baselines."
**S4 (Additional Findings):** "Top-K aggregation consistently improves all methods, and we demonstrate that LLMs can help construct new explanation benchmarks for stance detection."
**S5 (Bounded Implication):** "Our findings establish causal CF-based methods as a practical and principled approach to model-agnostic NLP explanation, with a clear accuracy-efficiency trade-off."

### Introduction Outline (5-paragraph structure)

**P1 — Establish Territory:** "Faithful explanations are critical for safe NLP deployment. Explainability without causality cannot guarantee faithfulness because spurious correlations can mislead interpretations. Prior work [citations] has established this connection, but practical causal explanation methods remain limited."
*→ Transitions to: gap in existing methods*

**P2 — Identify Gap:** "Existing model-agnostic explanation methods are either restricted to simple input manipulations or rely on expensive manual annotation. Model-specific methods (e.g., Causal Proxy Model) require separate training per explained model, limiting their scalability."
*→ Transitions to: our theoretical criterion*

**P3 — Our Theory:** "We formalize a necessary condition — Order-faithfulness: an explanation method's ranking of concept importance must match the true causal ordering. We prove that CF-based methods always satisfy this criterion under mild assumptions, while non-causal methods can fail (Theorem 1)."
*→ Transitions to: our first practical method*

**P4 — Method 1 (Generation):** "Our first approach directly generates CFs by prompting an LLM to intervene on a target concept while holding confounders fixed. This achieves low explanation error on the CEBaB benchmark but requires LLM inference at test time."
*→ Transitions to: efficient alternative*

**P5 — Method 2 (Matching) + Evidence Preview:** "To address efficiency, we propose a matching method that learns a causal embedding space via contrastive learning, using LLM-generated CFs only at training time. We benchmark both approaches across 5 explained models, demonstrating effectiveness of generation and efficiency of matching, with Top-K universally beneficial."
*→ Ends with contribution summary*

## Priority Revision Plan
### Ranked Error Board

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Effort |
|------|-------|----------|--------------|------------|------------|--------|
| 1 | Missing variance/significance in Table 2 | Major | High | Easy (re-run with 3 seeds) | High | 1-2 weeks |
| 2 | SOTA claims unsupported | Major | High | Easy (rephrase claims) | High | 1 day |
| 3 | Stance benchmark CF circularity | Major | Medium | Medium (human annotation on subset) | Medium | 2-3 weeks |
| 4 | Unbounded Top-K selection | Major | Medium | Easy (validation split) | High | 1 week |
| 5 | Zero-mean approximation error assumption | Major | Medium | Easy (empirical bias analysis) | Medium | 1 week |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Priority 0: Fix Empirical Core]
    -> Problem: No variance/significance in Table 2
    -> Action: Run 3 seeds, report mean±std, add significance tests
    -> Expected Impact: All empirical rankings become statistically grounded
    -> Dependencies: None (compute only)

[Priority 1: Tighten Claims]
    -> Problem: SOTA claims exceed evidence (single benchmark, no direct SOTA comparison)
    -> Action: Rephrase to "lowest error among tested methods on CEBaB"
    -> Expected Impact: Claims match evidence scope, reviewer trust improves
    -> Dependencies: Priority 0 (need statistical basis for ranking statements)

[Priority 2: Validate New Benchmark]
    -> Problem: GPT-4 CFs as ground truth → circular evaluation risk
    -> Action: Human-annotate 100 CFs, verify ranking consistency
    -> Expected Impact: Stance detection experiment becomes a valid second benchmark
    -> Dependencies: Priority 0 (recomputation uses same seed policy)

[Priority 3: Methodological Rigor]
    -> Problem: Top-K selection post-hoc, zero-mean assumption untested
    -> Actions: (a) validation-based K selection, (b) empirical bias analysis of CFs
    -> Expected Impact: Stronger reproducibility and theoretical grounding
    -> Dependencies: None
```

### Revision Sequence

**Week 1-2 (P0):** Re-run all CEBaB experiments (Table 2, ablation Table 4) with 3 seeds. Add std and significance tests. Update all claims to match evidence scope.

**Week 2-3 (P1):** Add human validation for 100 stance detection CFs. Select K via validation split. Implement empirical bias analysis.

**Week 3-4 (P2):** Add 2 non-matching baselines (LIME, CPM) to Table 2 if feasible. Restructure Related Work. Revise abstract and introduction narrative.

**Week 4 (Polish):** Clarify CaCE estimator notation. Add error propagation analysis. Final proofreading of claims.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Compare CF generation vs matching explanation methods | CEBaB, 5 models, 24 interventions | L2, Cos, ND (Err) | Generative methods have lower Err than matching | C1: CF generation is effective | Single benchmark, no variance reported |
| E2 | Compare causal model vs matching baselines | CEBaB, 5 models, K=1 and K=10 | L2, Cos, ND (Err) | Causal model outperforms all matching baselines | C2: Matching method is best among matching approaches | No comparison with non-matching baselines |
| E3 | Evaluate Top-K effect on all methods | CEBaB, DistilBERT focus | L2 Err vs K | Top-K reduces Err for all methods | C3: Top-K universally improves explanations | K=10 chosen arbitrarily, no validation-based selection |
| E4 | Ablation: objective components | CEBaB, original/+GT CFs/+misspecified CFs | L2, Cos, ND | Six-component objective is robust to candidate set variations | Method design choice validated | Small candidate set may mask differences |
| E5 | Ablation: backbone encoder | CEBaB | L2, Cos, ND | S-Transformer and RoBERTa both competitive | Architecture robustness | — |
| E6 | Ablation: unsupervised concept prediction | CEBaB, LLM-predicted labels | L2, Cos, ND | Performance on par with human-annotated labels | Practical applicability without human annotation | LLM prediction quality not directly measured |
| E7 | Ablation: no LLM-generated CFs | CEBaB, w/o XCF | L2, Cos, ND | Good performance, less precise | Feasibility without LLM | — |
| E8 | Inference time comparison | Single/batch, 250/1000 candidates | Latency (sec) | Matching 30-1000x faster than generation | Efficiency advantage of matching | Only one hardware configuration tested |
| E9 | Cross-domain generalization | Stance detection, OOD candidate set | L2, Cos, ND | Main findings replicated under distribution shift | Robustness of conclusions | GPT-4 CFs as ground truth create circularity risk |
| E10 | CF generation for complex causal graphs | Health consultation scenario | Qualitative | GPT-4 can handle mediators in CF generation | Method applicability beyond CEBaB | No quantitative evaluation |

### Research-Theme Gap Diagnosis

Three core research-value claims have weak empirical support:

1. **New knowledge (Order-faithfulness as a framework):** The theoretical contribution is sound but its practical significance is untested — the paper does not empirically demonstrate that non-causal methods fail in realistic scenarios in the way the theorem predicts.

2. **Reproducibility:** The missing variance reporting (no standard deviations, no seeds) and deferred prompt details make independent reproduction challenging. The code is available but key hyperparameters (concept predictor accuracy, ChatGPT CF generation parameters) are only partially reported.

3. **Potential to change practice:** The paper claims matching could replace generation for efficient explanation, but the gap between generative Err (~0.24-0.36 at K=10) and matching Err (~0.38-0.63 at K=10) means the matching method is substantially less accurate. Without error bars, it is unclear whether this gap can be narrowed via better candidate sets.

### Proposed Research Experiments (P0/P1/P2)

#### Experiment P0.1: Statistical Variance Quantification
- **Target Claim:** C1 (generative methods are SOTA), C2 (causal model beats matching baselines)
- **Hypothesis:** Observed Err differences are statistically significant
- **Minimal Design:** Run all methods in Table 2 with 3 random seeds. Report mean ± std for each metric.
- **Controls:** Fixed data splits, fixed seeds across methods
- **Metrics:** L2, Cos, ND (same as current); paired Wilcoxon signed-rank test
- **Success Criterion:** Reported std deviations < 0.05 L2 (i.e., differences > 0.05 can be considered significant)
- **Estimated Cost:** 1-2 weeks (compute-limited)
- **Expected Quality Gain:** High — all empirical ranking claims become statistically grounded

#### Experiment P0.2: Human Validation of Stance Detection CFs
- **Target Claim:** C1, C3 (generalizability to new benchmark)
- **Hypothesis:** GPT-4 CFs and human-written CFs produce similar method rankings
- **Minimal Design:** Sample 100 test examples. Three annotators write CFs for 6 interventions each. Compute inter-annotator agreement and GPT-4 vs human agreement. Recompute Table 6 on human-validated subset.
- **Controls:** Use same prompt structure as GPT-4 generation
- **Metrics:** Agreement rate (Cohen's κ), Err scores on human-validated subset
- **Success Criterion:** Relative method rankings preserved on human-validated subset
- **Estimated Cost:** 2-3 weeks (annotator effort, ~600 CFs)
- **Expected Quality Gain:** High — removes circularity concern, validates new benchmark utility

#### Experiment P1.1: CF Generation Bias Analysis
- **Target Claim:** Theorem applicability (zero-mean approximation error assumption)
- **Hypothesis:** LLM-generated CFs have small but non-zero systematic bias
- **Minimal Design:** For each generative method, compute Δ = f(\tilde{x}_{t'}) - f(x_{t'}^{gold}) for all test examples. Test whether E[Δ] ≠ 0 via one-sample t-test.
- **Controls:** None (descriptive analysis)
- **Metrics:** Mean bias, 95% CI of bias, proportion of predictions where bias direction reverses ranking
- **Success Criterion:** If |E[Δ]| < 0.05 L2, assumption is practically satisfied
- **Estimated Cost:** 1 week (compute-only)
- **Expected Quality Gain:** Medium — strengthens theoretical-practical connection

#### Experiment P1.2: Validation-Based K Selection
- **Target Claim:** C3 (Top-K improves all methods)
- **Hypothesis:** Validation-selected K yields similar or better Err than K=10
- **Minimal Design:** Split dev set into validation (N=800) and test (N=872). Select K ∈ {1,5,10,20,50} minimizing Err on validation. Report test-set Err at selected K.
- **Controls:** Compare with fixed K=10
- **Metrics:** L2 Err, selected K values by method
- **Success Criterion:** Validation-selected K yields ≤10% worse Err than oracle K
- **Estimated Cost:** 1 week
- **Expected Quality Gain:** Medium — methodological rigor improvement

#### Experiment P2.1: Non-Matching Baselines
- **Target Claim:** C1 (generative methods are SOTA)
- **Hypothesis:** Generative CF methods outperform LIME and CPM
- **Minimal Design:** Add LIME (using text perturbations) and Causal Proxy Model to Table 2 for DistilBERT and RoBERTa.
- **Controls:** Same data splits, same metrics
- **Metrics:** L2, Cos, ND
- **Success Criterion:** Generative CF methods achieve lower Err than both baselines
- **Estimated Cost:** 2-3 weeks
- **Expected Quality Gain:** High — directly supports SOTA claim or forces claim downgrade

### ASCII Diagram — Experiment Upgrade Plan

```text
P0.1: Variance Quantification (Week 1-2)
  -> Add 3 seeds to all Table 2 experiments
  -> Report mean±std + significance tests
  -> [Gate: std < 0.05 L2]

P0.2: Human CF Validation (Week 2-4, parallel with P0.1)
  -> 100 stance detection samples x 3 annotators
  -> Compute GPT-4 vs human agreement
  -> Recompute Table 6 Err on validated subset
  -> [Gate: rankings preserved]

P1.1: Bias Analysis (Week 3, after P0.1)
  -> Compute E[f(CF_LLM) - f(CF_gold)]
  -> t-test for zero mean
  -> [Gate: |bias| < 0.05 L2]

P1.2: K Selection (Week 3, after P0.1)
  -> Validation split for K selection
  -> Compare validation-selected K vs oracle
  -> [Gate: within 10% of oracle]

P2.1: Non-Matching Baselines (Week 4-5, after P0.1)
  -> Add LIME + CPM to Table 2
  -> Compare against generative methods
  -> [Gate: generative methods win OR claims downgraded]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper tackles an important problem with sound theoretical motivation and a novel technical approach (causal representation learning for matching). The theoretical framework (Order-faithfulness) is clean and well-proven. The empirical evaluation covers multiple explained models and includes thorough ablations.

However, the score is limited by:
- **Research value limitation:** The core empirical claims (SOTA for generative methods, universal Top-K benefit) are overstated relative to the evidence — a single benchmark, no variance reporting, and no direct comparison with prior SOTA explanation methods.
- **Novelty uncertainty:** Due to Retrieval-Disabled Mode in this run, external novelty verification is deferred. Without literature comparison, the novelty of the matching approach relative to existing causal representation learning methods cannot be confirmed.
- **Validity concerns:** Missing statistical significance testing, potential circularity in the new benchmark evaluation, and post-hoc hyperparameter selection (K=10) weaken the empirical conclusions.

**Post-Revision Target: [7.5, 8.0] / 10**

The target is achievable if the authors:
- Add statistical significance (3 seeds + std + tests) — addresses the most critical validity gap
- Add at least 2 non-matching baselines (LIME, CPM) for direct SOTA comparison
- Human-validate 100 CFs from the new stance detection benchmark
- Select K via validation split
- Tighten all claim language to match evidence scope
- Discuss the zero-mean approximation error assumption empirically

These revisions would increase confidence in the empirical rankings, validate the new benchmark, and align claims with evidence. The upper bound of 8.0 reflects the inherent limitation of single-benchmark evaluation; reaching above 8.0 would require additional task domains and a confirmed external novelty assessment.