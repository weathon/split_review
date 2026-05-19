## Summary
# Final Review Report

## Summary

This paper proposes an encoder-decoder framework that unifies four mechanistic interpretability methods — sparse autoencoders, logit lens, tuned lens, and probing — under a common intervention-centric evaluation paradigm. The authors define explicit forward and inverse mappings for each method, enabling principled intervention on human-interpretable features to steer model outputs. They introduce two evaluation metrics — intervention success rate and coherence-intervention tradeoff — along with a dataset of 210 open-ended prompts. Experiments on GPT2-sm, Gemma2-2b, and Llama2-7b compare these methods against steering vectors and prompting baselines on 10 word-level intervention topics (e.g., 'coffee', 'yoga', 'dogs').

The paper tackles a timely and important problem: the lack of standardized evaluation for mechanistic interpretability methods, particularly regarding their practical utility for model control. The key findings — that lens-based methods outperform for simple concrete features, that all methods degrade output coherence under intervention, and that prompting outperforms interpretability-based methods — are practically relevant for the interpretability community.

However, the paper has several significant weaknesses: (1) The evaluation is limited to 10 word-level features, making broad claims about "interpretability methods" premature; (2) The coherence metric relies on an unvalidated LLM-as-judge approach; (3) The appendix contains complex-feature results that directly contradict the main paper's headline finding, but this contradiction goes unaddressed; (4) The mathematical formalism uses notation (D^{-1}) that is misleading for overcomplete dictionaries and breaks for probing; and (5) The diagnostic claim about SAE label noise is supported only by anecdotal evidence. The novelty of the contribution cannot be fully assessed without external literature comparison, which is deferred due to retrieval unavailability in this run.

## Strengths
1. **Timely and well-motivated problem.** The paper addresses a genuine gap in mechanistic interpretability: the lack of standardized evaluation for whether interpretability methods can actually control model behavior. The threefold diagnosis (disparate feature spaces, predict/control discrepancy, no benchmarks) is well-articulated and practically relevant.

2. **Unifying encoder-decoder framework.** The abstract framework that treats SAEs, Logit Lens, Tuned Lens, and probing as instances of a common encoder-decoder paradigm is a useful conceptual contribution. It enables principled comparison across methods that were previously evaluated in isolation, and it provides a clean mathematical interface for defining interventions on interpretable features.

3. **Two new standardized metrics.** Intervention success rate and coherence-intervention tradeoff are sensible, practical metrics that go beyond reconstruction error or qualitative inspection. They directly measure what practitioners care about: whether intervening on an identified feature causes the desired output change, and at what cost to model quality.

4. **Multi-model evaluation.** The experiments span three model families (GPT2-sm, Gemma2-2b, Llama2-7b) with very different scales, providing some evidence about how method rankings change with model capability. The inclusion of both lens-based methods and SAEs allows direct comparison that most prior work lacks.

5. **Open dataset and code release.** The 210-prompt evaluation dataset and the accompanying code are valuable community resources that can be extended and reused for future benchmarking.

6. **Honest limitation acknowledgment.** The paper explicitly acknowledges that intervention degrades coherence, that prompting outperforms interpretability methods, and that α must be tuned per method/model/feature — a level of transparency that is rare in the interpretability literature.

7. **Rebutal experiments (Appendix B).** The addition of Llama3-8b experiments, grammar-checker coherence metrics, and complex features (French, Yelling) in the appendix shows responsiveness to potential criticism and enriches the empirical picture, even though these results partially contradict the main paper's headline findings.

## Weaknesses
1. **Evaluation limited to word-level features (major).** All 10 intervention topics are simple word/phrase references (e.g., 'coffee', 'pink', 'yoga'). The paper then generalizes to claims about "interpretability methods" broadly. Since lens-based methods are token-level by construction and SAEs/probes aim at higher-level abstractions, the evaluation setup inherently favors lens methods. Appendix B.3 partially addresses this but contradicts the main finding, creating internal inconsistency.

2. **Unvalidated LLM-as-judge for coherence (major).** The coherence metric uses a single Llama3.1-8b model with a single prompting template, with no calibration against human judgments, no inter-rater reliability checks, and no sensitivity analysis. The paper's central practical conclusion — that all methods degrade coherence — rests entirely on this unvalidated metric.

3. **Unaddressed internal contradiction (critical).** Appendix B.3 shows that for complex features (French, Yelling), steering vectors and probes outperform lens-based methods — directly contradicting the main paper's headline claim that "lens-based methods outperform all other methods." This contradiction is not acknowledged or discussed in the main text.

4. **Misleading mathematical formalism (major).** The notation $D^{-1}$ for the decoder suggests $D$ is square and invertible, which is false for SAEs (overcomplete dictionaries) and Logit Lens (non-square unembedding matrix). The probing "inverse" ($\hat{x}' = x + \theta$) does not follow from the encoder-decoder formalism at all.

5. **Unsupported diagnostic claim about SAE label noise (major).** The claim that SAE underperformance is "due to heavy noise in the labels of features" is supported only by a single anecdotal coffee/beans example. No systematic label-quality audit is provided.

6. **Weak contribution framing.** The three bullet-point contributions are procedural ("In Section X, we present...") rather than claiming concrete scientific advances. This makes it harder to assess what is genuinely new.

7. **Novelty assessment deferred.** Due to the Retrieval-Disabled Mode in this run, no external literature comparison was possible. Claims about the novelty of the encoder-decoder framework relative to Patchscopes (Ghandeharioun et al., 2024a) and other unifying frameworks cannot be independently verified.

8. **Prompting baseline comparison is incomplete.** Prompting was only feasible for Llama2-7b (instruction-tuned); it was "less successful" for Gemma2-2b and "infeasible" for GPT2-sm. The headline claim that "prompting performs best overall" should be nuanced to reflect this limited comparison scope.

9. **Section 4.6 high-level comparison is insightful but insufficiently tied to evidence.** The characterization of each method's strengths/weaknesses is largely based on author opinion rather than directly linked to experimental quantities. For example, the claim that SAEs "ideally 'cover' all the true underlying features" is speculation, not a finding from this paper's experiments.

10. **Related Work section does not differentiate from Patchscopes.** Both Patchscopes (Ghandeharioun et al., 2024a) and this paper propose unifying frameworks for interpretability methods. The paper mentions Patchscopes but does not explain what its framework adds beyond Patchscopes, weakening the novelty claim for Contribution 1.

## Key Issues
### Issue 1 (Critical): Appendix-Main Contradiction — Complex features reverse method rankings
**Location:** Page 7, Section 4.3 vs Page 19, Appendix B.3  
**Evidence:** Main paper claims "Logit lens and Tuned lens have the highest intervention success rate" (Page 7). Appendix B.3 shows for French and Yelling features, "Steering vectors and Probes generally perform the best... Logit Lens does not perform well" (Page 19).  
**Impact:** This is the paper's most serious flaw. A reader who reads only the main paper receives a conclusion that is contradicted by the paper's own supplementary experiments. The contradiction is not acknowledged, discussed, or reconciled anywhere in the main text.  
**Required fix (Must):** Restructure the paper to present the feature-type dependence as a key finding rather than a buried appendix. Revise the abstract, introduction, and conclusion to state that method rankings depend on feature complexity. Move the Appendix B.3 results (or equivalent broader evaluation) into the main paper.

### Issue 2 (Major): Coherence metric lacks validation
**Location:** Page 5, Section 3.2 (Usefulness of Intervention Methods)  
**Evidence:** Coherence is measured by Llama3.1-8b with a single prompt template. No human correlation, no alternative judge, no calibration.  
**Impact:** The paper's central practical finding — that all interpretability methods degrade coherence under intervention — rests entirely on an unvalidated metric. If the LLM judge has systematic biases (e.g., favoring topic-focused outputs regardless of grammar), the coherence-intervention tradeoff curves could shift significantly.  
**Required fix (Must):** Report human correlation on a 50-sample subset. Add at least one alternative judge. Provide calibration statistics and explicitly acknowledge limitations.

### Issue 3 (Major): Word-level evaluation limits generality
**Location:** Page 6, Section 4.1 (Intervention Topics)  
**Evidence:** All 10 interventions are "simple, low-level features" — single words or phrases. The paper explicitly acknowledges this is an "upper bound" evaluation. Yet the conclusion generalizes to "interpretability approaches" broadly.  
**Impact:** The headline findings (lens > SAE > probing; prompting > all) may be artifacts of the word-level evaluation design. SAEs are designed for abstract features; probes and steering vectors can capture higher-level concepts. The narrow feature scope prevents fair assessment.  
**Required fix (Must):** Reframe all conclusions as specific to word-level features. Add at least 3-5 higher-level features (e.g., sentiment, formality, factual accuracy) to the main evaluation.

### Issue 4 (Major): Misleading mathematical formalism
**Location:** Page 4, Section 3.1  
**Evidence:** The framework uses $z = \sigma(x \cdot D)$ and $\hat{x} = z \cdot D^{-1}$, where $D$ is simultaneously used as a matrix and an index set, and $D^{-1}$ suggests invertibility.  
**Impact:** SAEs use overcomplete dictionaries ($m \gg d$) that have no inverse. The probing "inverse" is additive ($\hat{x}' = x + \theta$) and does not follow from $z = f(x)$. This notation overstates the mathematical unity of the framework.  
**Required fix (Must):** Replace $D^{-1}$ with per-method decoder notation. Clearly specify which operations are true inverses, pseudoinverses, or ad-hoc constructions.

### Issue 5 (Major): SAE label noise claim is anecdotal
**Location:** Page 7, Section 4.3  
**Evidence:** "We believe the lower performance of Sparse Autoencoders is due to heavy noise in the labels of features... For example, a feature labelled 'references to coffee'..." Only one example given.  
**Impact:** Without systematic evidence, alternative explanations (reconstruction error, layer selection, feature-type mismatch) remain equally plausible. The paper should present multiple hypotheses rather than a single unsupported assertion.  
**Required fix (Must):** Either provide a systematic label-quality audit across all 10 topics, or present the claim as one of several hypotheses.

## Actionable Suggestions
### S1 (Must): Resolve the Appendix-Main Contradiction
**Problem:** The main paper claims lens-based methods outperform, but Appendix B.3 shows the opposite for complex features.  
**Action:** Move the complex-feature experiments (French, Yelling) from the appendix into the main evaluation. Add 2-3 more complex features (e.g., sentiment polarity, factual accuracy, formality). Rewrite the abstract, introduction, and conclusion to state that method rankings depend on feature type, not as a buried caveat but as a central finding.  
**Location:** Abstract, Page 7 Section 4.3, Page 10 Section 5, Page 19 Appendix B.3.

### S2 (Must): Validate the Coherence Metric
**Problem:** The LLM-as-judge coherence metric has no human correlation.  
**Action:** (a) Have 2 human annotators rate 50 randomly sampled outputs from each method. Report Spearman correlation between human scores and Llama3.1-8b scores. (b) Add a second LLM judge (GPT-4o) and report rank-order consistency. (c) Report mean, std, and distribution statistics for clean outputs as calibration. (d) Add a limitations paragraph acknowledging the metric's unvalidated nature.  
**Location:** Page 5, Section 3.2 (Usefulness of Intervention Methods).

### S3 (Must): Fix the Mathematical Notation
**Problem:** $D^{-1}$ is misleading for overcomplete dictionaries and probing.  
**Action:** Replace the unified equation block with per-method definitions: For SAEs: $\hat{x} = z D_{\text{dec}}$ where $D_{\text{dec}} \in \mathbb{R}^{m \times d}$. For Logit Lens: $\hat{x} = z W_{\text{unembed}}^+$ (pseudoinverse). For Tuned Lens: $\hat{x} = z (A W_{\text{unembed}})^+$. For probing: $\hat{x}' = x + \theta$ (additive edit, not an inverse). Explicitly note that the framework is conceptual — it unifies the *goal* of interpretability (mapping to human-interpretable features and back), not the specific mathematical operator.  
**Location:** Page 4, Section 3.1.

### S4 (Must): Provide Systematic SAE Label-Quality Evidence
**Problem:** The SAE label noise claim is anecdotal.  
**Action:** For each of the 10 intervention topics, have 2-3 annotators rate the top-3 SAE features as "correct," "partially correct," or "incorrect" relative to the target concept. Report the distribution and its correlation with intervention success rate. Alternatively, present the claim as one of several hypotheses and test the reconstruction-error hypothesis by comparing SAEs with better reconstruction (e.g., GPT2-sm with a larger dictionary).  
**Location:** Page 7, Section 4.3.

### S5 (Nice-to-have): Reframe Contribution Statements
**Problem:** Contributions are procedural ("In Section X we present...") rather than substantive.  
**Action:** Rewrite each bullet to state what scientific advance was made. For example: "We introduce an encoder-decoder framework that enables, for the first time, principled intervention across four previously incompatible interpretability methods." Avoid section references in contribution statements.  
**Location:** Page 3, contribution list.

### S6 (Nice-to-have): Differentiate from Patchscopes
**Problem:** The Patchscopes framework (Ghandeharioun et al., 2024a) also unifies interpretability methods, but the paper does not explain what its framework adds.  
**Action:** Add 2-3 sentences in Related Work explaining: Patchscopes focuses on *inspection* (patching representations into contexts). This paper focuses on *control* (defining explicit inverse mappings for intervention). The two are complementary: Patchscopes for understanding, this paper's framework for steering.  
**Location:** Page 3, Section 2 (Related Work — Mechanistic Interpretability).

### S7 (Must): Expand the Prompting Baseline Comparison
**Problem:** Prompting was tested only on one model (Llama2-7b, instruction-tuned).  
**Action:** Include at least one additional instruction-tuned model (e.g., Gemma2-2b-it or Llama3-8b-it) where prompting is feasible, to make the "prompting performs best" claim more robust. The Llama3-8b experiments in Appendix B.1 partially address this, but the main text should reference them more prominently.  
**Location:** Page 8, Section 4.4.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**Current analysis:** The abstract contains most necessary elements but is overloaded with qualification clauses and lists three findings without prioritization.

**Revised Abstract Plan (5 sentences):**
- **S1 (Problem):** "As large language models (LLMs) grow in capability, understanding and controlling their internal reasoning is critical for safety and alignment."
- **S2 (Gap):** "Existing interpretability methods are typically designed for either understanding or control, seldom both, and there are no standardized benchmarks to evaluate their practical utility for intervention."
- **S3 (Solution):** "We propose intervention as a fundamental goal of interpretability and introduce an encoder-decoder framework that unifies sparse autoencoders, logit lens, tuned lens, and probing, enabling structured interventions on human-interpretable features to control model outputs."
- **S4 (Key Results):** "Using two new metrics — intervention success rate and coherence-intervention tradeoff — we find that lens-based methods outperform for word-level features but supervised methods excel for abstract concepts, and all methods degrade output coherence, underperforming simple prompting baselines."
- **S5 (Implication):** "These results reveal that the choice of interpretability method for control depends critically on feature type, and that no current method achieves both high intervention success and output coherence — highlighting a key open challenge for the field."

### Introduction Outline (Complete)

**Current storyline:** P1: Motivation + threefold gap (dense). P2: Framework + results preview + diagnostics (overloaded). P3: Contribution list (procedural).

**Weaknesses:** Two paragraphs dump all motivation, gaps, framework, and detailed results into dense blocks. The reader doesn't see a clear gap-solution-evidence arc.

**Candidate Storyline A (Recommended): Problem → Gap → Solution → Evidence → Contribution**
- **P1 (Motivation + Specific Gap):** Open with the practical need for controlling LLMs. State the specific gap: interpretability methods claim intervention capability but lack standardized evaluation. Highlight the predict/control discrepancy (Wattenberg & Viégas, 2024) as the most important barrier.
- **P2 (Solution Intuition):** Present the encoder-decoder framework at a high level: any method that maps latents to interpretable features and back can be used for intervention. Name the four methods unified. State that this framework enables systematic comparison.
- **P3 (Evaluation Metrics + Dataset):** Introduce the two metrics (intervention success rate, coherence-intervention tradeoff) and the open-ended dataset. Explain why these metrics matter for practical control.
- **P4 (Evidence Preview):** Give a high-level summary of key findings, structured as three takeaways without diagnostic speculation: (1) lens methods do best on word features, (2) method rankings depend on feature type, (3) prompting beats all interpretability methods on instruction-tuned models.
- **P5 (Contributions):** Three substantive bullet-point claims about what scientific advance was made, without section references.

**Candidate Storyline B (Practice-Oriented):** Starting from the practitioner's question "Which interpretability method should I use to steer my model?" — organize the introduction around this concrete decision problem. Each paragraph addresses one dimension of the answer: feature type, model type, and coherence constraints.

**Selected: Candidate A** — It preserves the paper's scientific framing while fixing the main structural issues (overloaded paragraphs, buried findings, procedural contributions).

### Key Paragraph Rewrites

**Current P1 (Page 1, Introduction):** Three gaps listed in a single paragraph.  
**Mentor Revised Version (split into two paragraphs):**  
Paragraph 1a: "As large language models grow more capable and complex, understanding and controlling their internal reasoning has become critical for ensuring safe, human-aligned outputs. Many interpretability methods aim to address this by analyzing model representations, yet the link between interpretation and intervention remains tenuous in practice. While compelling qualitative demonstrations exist — such as Anthropic's Golden Gate Claude — most methods are designed either for understanding or for control, not both, and they are rarely evaluated systematically for their ability to steer model outputs."  
Paragraph 1b: "We identify three structural barriers that prevent current interpretability methods from achieving reliable control. First, methods produce explanations in disparate feature spaces (token vocabulary, probe predictions, learned SAE features), hindering direct comparison. Second, there is a 'predict/control discrepancy' — the features that best predict model behavior are not necessarily the same as those needed to steer it. Third, there are no standardized benchmarks to measure intervention success. This paper directly addresses all three barriers by proposing an intervention-centric evaluation framework."

**Current Contribution List (Page 3):** Procedural.  
**Mentor Revised Version:**  
"Our contributions are threefold:  
(1) A unifying encoder-decoder framework that extends four mechanistic interpretability methods — sparse autoencoders, logit lens, tuned lens, and probing — to support principled intervention on human-interpretable features with explicit forward and inverse mappings.  
(2) Two standardized evaluation metrics — intervention success rate and coherence-intervention tradeoff — that jointly measure the causal correctness of explanations and their practical utility for steering model outputs, along with an open-source benchmark dataset of 210 prompts.  
(3) A systematic empirical comparison of all four methods (plus steering vectors and prompting baselines) on GPT2-sm, Gemma2-2b, and Llama2-7b, producing actionable recommendations for method selection based on feature type, model size, and coherence constraints."

## Priority Revision Plan
### P0 — Must Fix (Publication-Critical)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P0.1 | Appendix-main contradiction (complex features reverse rankings) | Move B.3 to main paper, rewrite abstract/conclusion to reflect feature-type dependence | Resolves the most damaging inconsistency; corrects misleading headline | 1-2 days |
| P0.2 | Coherence metric validation | Add human correlation study (50 samples), second LLM judge, calibration stats | Validates the central practical finding | 2-3 days |
| P0.3 | Expand feature scope beyond 10 word-level concepts | Add 3-5 higher-level features (sentiment, formality, factual accuracy) | Strengthens generality of findings; may change method rankings | 3-5 days |
| P0.4 | Fix misleading $D^{-1}$ notation | Replace with per-method decoder definitions; remove pretense of unified inverse | Eliminates mathematical inaccuracy | 0.5 days |

### P1 — Should Fix (High Impact on Quality)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P1.1 | SAE label noise claim | Add systematic label-quality audit or present as hypothesis with alternatives | Strengthens diagnostic rigor | 2-3 days |
| P1.2 | Contribution framing | Rewrite as substantive scientific claims | Improves first impression for reviewers | 0.5 days |
| P1.3 | Introduction narrative | Split overloaded first paragraph; restructure results preview | Improves readability and argument clarity | 1 day |
| P1.4 | Patchscopes differentiation | Add 2-3 sentences explaining what this framework adds beyond Patchscopes | Strengthens C1 novelty claim | 0.5 days |

### P2 — Nice to Have (Quality Polish)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P2.1 | Prompting baseline | Add explicit cross-reference to Llama3-8b experiments (Appendix B.1) in main text | Makes comparison more robust | 0.5 days |
| P2.2 | Coherence contradiction (Page 8) | Add bridging sentence reconciling the two views of coherence (edit distance vs success rate) | Eliminates reader confusion | 0.5 days |
| P2.3 | Consistency of reviewer-applicable experiments | Ensure all methods have comparable hyperparameter search budgets | Improves fairness perception | 1 day |

### Revision Order

```
Week 1: P0.4 (notation fix, 0.5d) → P1.3 (intro rewrite, 1d) → P1.2 (contributions, 0.5d) → P1.4 (Patchscopes, 0.5d)
Week 2: P1.1 (SAE audit, 2d) + P0.2 (coherence validation, 2d)
Week 3: P0.1 (rewrite abstract/conclusion + move B.3 to main, 2d) 
Week 4: P0.3 (higher-level features, 3-5d) → P2.1-2.3 (polish, 1d)
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Current: Contradictory Findings]
    ├── Main paper: "Lens methods outperform"
    └── Appendix B.3: "Steering/probes outperform"
            │
            ▼
[P0.1: Resolve Contradiction]
    └── Move B.3 to main + rewrite claims to be feature-type dependent
            │
            ▼
[P0.2: Validate Central Metric]
    └── Human correlation + second judge for coherence scores
            │
            ▼
[P0.3: Broaden Feature Scope]
    └── Add 3-5 higher-level features to main evaluation
            │
            ▼
[P0.4: Fix Notation]
    └── Replace D^{-1} with per-method decoders
            │
            ▼
[Expected Outcome: Honest, Defensible Paper]
    ├── Claim: "Method rankings depend on feature type"
    ├── Metric: Coherence validated against humans
    ├── Scope: Word-level AND abstract features
    └── Math: Accurate notation
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|-------------|----------------|-------------------|
| E1 (4.2) | Measure latent reconstruction error without intervention | GPT2-sm, Gemma2-2b, Llama2-7b; Logit Lens, Tuned Lens, SAEs | Normalized $\|\hat{x} - x\|/\|x\|$ | Error varies: Logit Lens 0.52 (Gemma) → 5e-5 (Llama); SAEs 1.64 (GPT2) | SAEs have high reconstruction error | Only 3 methods (not probes/steering); no error bound analysis |
| E2 (4.2) | Measure coherence of reconstructed outputs | Same as E1 | Coherence via Llama3.1-8b (score 1-10) | Reconstructed outputs match clean model coherence | Encoder-decoder cycle preserves coherence | Unvalidated LLM judge; small sample |
| E3 (4.3) | Intervention Success Rate across methods | 10 word features; 210 prompts; 3 models; 5 methods + 2 baselines | Binary intervention success; normalized edit distance | Logit/Tuned Lens > SAE > Probing > Steering | Lens methods have highest ISR | Only word-level features; α tuned per method |
| E4 (4.3) | Intervened Token Probability | Same as E3 | Token-level probability for target words | All methods increase target token probability; SAEs at $10^{-5}$ vs others $10^{-4}$-$0.5$ | All methods change output probability | Does not measure output-level success |
| E5 (4.4) | Coherence-Intervention Tradeoff | Same as E3 + prompting baseline | Coherence vs edit distance; coherence vs ISR | Prompting > Lens methods > others for coherence | All methods degrade coherence | Only 30-token generation; prompting tested only on Llama2-7b |
| E6 (4.5) | Intervention Direction Similarity | Same as E3 | Cosine similarity between $\hat{x}' - x$ vectors | Logit↔Tuned: 0.8-1.0; Steering↔Probing: 0.68-0.75; SAE↔Logit: near orthogonal | Methods cluster into two groups | Interpretation of near-orthogonality is speculative |
| E7 (A.6) | Layer-wise Intervention Efficacy | GPT2-sm all layers; 3 features (beauty, coffee, dogs) | ISR, coherence, edit distance per layer | Logit/Tuned: higher ISR at later layers; others: layer-invariant | Layer depth matters for lens methods | Only GPT2-sm; only 3 features |
| E8 (B.1) | Intervention on Llama3-8b | Same prompts + features as E3/E5 | ISR, coherence | Consistent with Llama2-7b results | Results generalize to larger model | One additional model only |
| E9 (B.3) | Complex features (French, Yelling) | Gemma2-2b; 2 features | ISR, coherence | Steering/Probes > SAEs > Logit Lens | Method ranking flips for complex features | Only 2 features; only 1 model |

### Research-Theme Gap Diagnosis

1. **Feature-type dependence is underexplored.** The paper's main experiments use only word-level features, yet the appendix shows dramatically different rankings for complex features. The central unresolved question is: *which methods work for which feature types?* Without a systematic investigation across a feature-type spectrum (word-level → phrase-level → abstract concept → behavioral property), the paper cannot provide reliable practitioner guidance.

2. **Causal mechanism of intervention is not tested.** The paper measures whether intervention *succeeds* but not *why* it succeeds for some methods and not others. Understanding the causal mechanism — e.g., whether Logit Lens succeeds because of the token-level feature space or because of lower reconstruction error — would require controlled ablation experiments.

3. **Coherence metric validity is unestablished.** The entire coherence-intervention tradeoff analysis rests on a single unvalidated LLM judge. This is a critical gap that must be closed before the practical conclusions can be trusted.

4. **Reproducibility of the intervention framework is unverified.** The paper defines the encoder-decoder framework theoretically but does not demonstrate that another research group could implement it from the description alone. More implementation details (pseudocode, hyperparameter sensitivity, edge cases) are needed.

### Proposed Research Experiments (P0/P1/P2)

| Priority | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|----------|-------------|------------|---------------|-------------------|---------|------------------|---------------|--------------|
| **P0** | C2: "Lens methods outperform for simple features" but B.3 shows opposite for complex features | Method ranking is feature-type-dependent | Add 5 hierarchy levels of features: word (existing), phrase (e.g., "machine learning"), concept (e.g., "technology"), behavior (e.g., "politeness"), meta (e.g., "French") | Same 3 models, same α tuning protocol | ISR, coherence, edit distance | Significant interaction effect (feature type × method) in ANOVA | 1-2 weeks | Resolves main contradiction; enables grounded practitioner guidance |
| **P0** | All claims using coherence metric | Human-Llama3.1-8b agreement on coherence scoring | 50 outputs × 5 methods × 2 human raters; compare scores | Random selection stratified by ISR success/failure | Spearman ρ between human avg and LLM score | ρ > 0.7 | 2-3 days | Validates or invalidates all coherence-related conclusions |
| **P0** | C1: Encoder-decoder framework enables principled intervention | Framework can be applied to a new method not in the original four | Implement intervention for a 5th method (e.g., activation patching) within the framework | Existing 4 methods as reference | Framework adoption cost (hours), ISR comparison | New method is < 20 lines of code to integrate | 1 week | Demonstrates framework generality beyond chosen methods |
| **P1** | C2: SAE label noise causes poor performance | SAEs with human-verified labels achieve higher ISR than auto-interpreted SAEs | For 5 topics, have 3 annotators select the best SAE feature, then compare ISR | Auto-interpreted SAE features (current) vs human-selected | ISR improvement | ISR increase > 0.1 | 1 week | Confirms or refutes the label noise hypothesis |
| **P1** | C3: Prompting outperforms all interpretability methods | Prompting maintains coherence because it doesn't perturb latent representations | Compare latent perturbation norms between prompting and intervention methods | Same prompt content, same model | Norm $\|x' - x\|$, coherence, ISR | Prompting has > 10× smaller perturbation | 3-5 days | Explains *why* prompting outperforms; could inspire better methods |
| **P2** | Generalization of findings to larger models | Method rankings hold for models > 10B parameters | Add Llama3-70b (if SAEs available) or Mixtral | Same protocol as Section 4 | ISR, coherence | Ranking correlation > 0.8 with current results | 2-3 weeks | Strengthens external validity of findings |

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2 Sequencing)

Week 1-2: P0 Experiments
┌─────────────────────────────────────────────────────┐
│ P0.1: Feature-type hierarchy (5 levels × 3 models)  │
│   → Resolves appendix-main contradiction             │
├─────────────────────────────────────────────────────┤
│ P0.2: Human coherence validation (50 samples × 2     │
│   raters × Llama3.1-8b comparison)                   │
│   → Validates central metric                          │
├─────────────────────────────────────────────────────┤
│ P0.3: 5th method integration test                    │
│   → Demonstrates framework generality                 │
└─────────────────────────────────────────────────────┘
                        ▼
Week 3: P1 Experiments
┌─────────────────────────────────────────────────────┐
│ P1.1: SAE label quality audit                        │
│   → Confirms or refutes diagnostic speculation        │
├─────────────────────────────────────────────────────┤
│ P1.2: Perturbation norm analysis (prompting vs        │
│   interpretability methods)                           │
│   → Explains why prompting outperforms                │
└─────────────────────────────────────────────────────┘
                        ▼
Week 4+: P2 Experiments
┌─────────────────────────────────────────────────────┐
│ P2.1: Larger model validation (>10B parameters)      │
│   → Strengthens external validity                     │
└─────────────────────────────────────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

The paper addresses a genuine and timely problem with a clean conceptual framework and useful evaluation metrics. However, the score is limited by three major weaknesses:

1. **Internal contradiction (critical):** The main paper's headline finding that "lens-based methods outperform" is directly contradicted by Appendix B.3, which shows the opposite ranking for complex features. This contradiction is unaddressed, making the paper's central claim unreliable as written.

2. **Narrow evaluation scope:** The 10 word-level features provide a thin empirical basis for broad claims about "interpretability methods." The meaningful results are in the appendix (complex features), but they are not integrated into the main narrative.

3. **Unvalidated core metric:** The coherence metric — on which the paper's most important practical conclusion rests — has no human validation, no calibration, and no sensitivity analysis.

**Research value assessment:** The framework and metrics are genuinely useful contributions that could influence how the interpretability community evaluates methods. However, the current empirical execution does not match the scope of the claims. With substantial revision, this paper could be a valuable benchmark contribution.

**Reasoning:** Following the scoring policy of prioritizing research value + novelty as primary dimensions: the framework contribution (C1) is conceptually valuable but its novelty relative to Patchscopes is unclear. The metrics contribution (C2) is solid. The empirical contribution (C3) is weakened by the narrow feature scope and internal contradiction. Validity concerns about the coherence metric further reduce confidence.

---

**Post-Revision Target: [7.0, 7.5]/10**

This target assumes all P0 and P1 items are addressed: (1) the appendix-main contradiction is resolved by reframing findings as feature-type-dependent, (2) the coherence metric is validated against human judgments, (3) the feature scope is broadened to include abstract concepts, and (4) the mathematical notation is corrected. Given the solid conceptual core (framework + metrics), a score in this range is achievable after major revision. The upper bound is limited by the inherent difficulty of assessing novelty without extensive external literature comparison, which remains deferred.