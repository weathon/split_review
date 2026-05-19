## Summary
This paper proposes LICO (Large Language Models for In-Context Optimization), a method that adapts pretrained LLMs for black-box optimization in non-language domains, specifically molecular optimization. LICO augments a frozen LLM (Llama-2-7B) with three learnable components: an embedding layer for molecular fingerprints (x), an embedding layer for property scores (y), and a prediction head. The model is trained on a mixture of 47 intrinsic molecular properties and Gaussian Process-generated synthetic functions to perform in-context score prediction. At test time, LICO serves as a surrogate model within a standard evolutionary optimization loop (crossover + mutation + UCB acquisition), predicting scores of candidate molecules conditioned on past observations without any task-specific finetuning.

The paper evaluates LICO on the PMO benchmark (23 molecular optimization objectives) under two budgets: PMO-1K (1000 oracle calls) and full PMO (10000 calls). On PMO-1K, LICO achieves the highest aggregate score (11.71) among 7 methods, outperforming GP BO (11.27) and MOLLEO (11.65). On full PMO, LICO scores 14.708 (4th place), behind Genetic GFN (15.678) and Augmented Memory (15.002). Ablation studies confirm the importance of language instructions, semi-synthetic training (intrinsic + synthetic), and pretrained LLM initialization.

The core strengths are the novel architecture for cross-modal in-context learning, the semi-synthetic training strategy, and strong low-budget results. The main weaknesses are overclaiming in the conclusion (SOTA claim inconsistent with full-PMO results), unsupported speculation about baselines, several under-specified architectural details, and a related-work section organized as a list rather than structured comparison.

## Strengths
**S1. Novel cross-modal adapter architecture for in-context BBO.** LICO's design of adding learnable embedding layers (x and y) plus a prediction head to a frozen LLM is a clean, generalizable solution for extending LLMs to non-language scientific domains. The insight of using natural language prompts ("Each x is a molecule... Predict y given x") to guide the LLM's in-context reasoning within the embedding space is creative and well-motivated by the ablation study (Table 3, Page 9), which shows that removing language instructions degrades performance from 3.099 to 2.927.

**S2. Semi-synthetic training strategy combining intrinsic and synthetic functions.** The paper identifies a key challenge in surrogate pretraining — the trade-off between task proximity and diversity — and proposes a practical solution: intrinsic molecular properties provide domain-relevant signal while GP-generated functions prevent overfitting. The ablation study (Table 4, Page 9) empirically shows that either component alone underperforms the combination (pure synthetic: 2.936, pure intrinsic: 3.010, mixed: 3.099), validating the design choice.

**S3. Strong empirical results on the low-budget PMO-1K benchmark.** LICO achieves the highest aggregate score (11.71) under the 1000-call budget, outperforming 6 strong baselines including GP BO (+0.44), Genetic GFN (+0.15), and MOLLEO (+0.06). The 5-seed reporting with standard deviations follows best practices recommended by PMO.

**S4. Thorough ablation and analysis.** The paper provides systematic ablations on language instructions (Table 3), synthetic data ratio (Table 4), pretrained vs scratch initialization (Table 5), and LLM scaling (Figure 3), plus additional comparisons with molecule-specific LLMs (Appendix C.2) and GPT-4 (Appendix C.3). This depth of analysis is valuable for understanding LICO's design decisions.

**S5. Publicly available benchmark and evaluation protocol.** Using the established PMO benchmark with standardized AUC Top-10 metrics and 5-seed aggregation enables direct comparison with future work and supports reproducibility.

## Weaknesses
**W1. SOTA claim is inconsistent with full-PMO results.** The conclusion states LICO "achieves state-of-the-art performance on PMO," but Table 2 shows LICO ranks 4th out of 7 methods on the full PMO benchmark (sum 14.708 vs Genetic GFN's 15.678). The SOTA claim is only valid for the low-budget PMO-1K setting. This inconsistency reduces the paper's factual credibility and will be flagged by reviewers.

**W2. Unsubstantiated speculation about baseline (MOLLEO) data contamination.** On Page 8, the paper speculates that MOLLEO "possibly has data contamination issues" without providing any evidence. This is a serious allegation that should either be supported with concrete evidence or removed. Speculative criticism weakens the paper's objectivity and scientific tone.

**W3. Overclaiming causal attribution ("proves").** The phrase "proves the effectiveness of LICO for surrogate modeling" (Page 8) is too strong for evidence from only 3 tasks, especially since on troglitazone_rediscovery the correlation between surrogate quality and optimization performance breaks down. The evidence is consistent with but does not prove the claim.

**W4. Prediction layer architecture is underspecified.** The paper states the prediction layer outputs "mean and standard deviation" (Page 5) but does not describe how σ is parameterized (linear head? softplus? log-variance?). This makes the UCB acquisition function (§4.3) unreproducible. The uncertainty estimate is central to LICO's surrogate-guided optimization, yet its architecture is a black box.

**W5. Related work reads as an annotated bibliography rather than structured comparison.** The two sub-sections list papers by category without explicit comparison axes (input representation, training data, surrogate vs generation). Optformer is mentioned but not directly compared to LICO despite both training transformers for in-context function prediction.

**W6. Limited evaluation of surrogate quality-optimization correlation.** The claim that surrogate model quality predicts optimization performance is tested on only 3 out of 23 tasks. While consistent with the hypothesis, this limited sample size weakens the generalizability of the finding. Additional comparisons across more tasks with controlled candidate generation would strengthen the claim.

**W7. Constrained LLM scaling analysis.** The scaling experiment (Figure 3) compares only 4 LLM sizes (1.8B-7B) on 8 tasks. The observed trend is suggestive but limited in both model size range and task coverage. The conclusion that "larger LLMs obtain stronger pattern-matching capabilities" for BBO is based on a narrow sweep.

**W8. Intrinsic-bioactivity correlation claim is unsupported.** Page 2 states intrinsic properties "are closely related to the actual objective functions we want to optimize such as bioactivities." This is asserted without citation or empirical evidence. Simple molecular weight is only weakly correlated with most target bioactivities.

## Key Issues
### Issue 1 (Severity: Major): SOTA Claim Contradicts Full-PMO Results
- **Location:** Page 10 - Conclusion
- **Evidence:** Conclusion states "LICO achieves state-of-the-art performance on PMO." Table 2 (Page 8) shows LICO sum score 14.708 (4th place) on full PMO, behind Genetic GFN (15.678), Augmented Memory (15.002), and MOLLEO (14.682).
- **Impact:** Factual inconsistency undermines paper credibility; reviewers will detect this mismatch.
- **Fix:** Revise to: "LICO achieves state-of-the-art performance on the low-budget PMO-1K setting and competitive results on the full PMO benchmark."

### Issue 2 (Severity: Major): Unsubstantiated Speculation About Baseline Data Contamination
- **Location:** Page 8 - Results Discussion
- **Evidence:** "MOLLEO ... which possibly has data contamination issues, since the finetuning data may have included similar tasks."
- **Impact:** Violates scientific objectivity; could be seen as unsupported competitor disparagement.
- **Fix:** Remove the speculation. Instead, acknowledge MOLLEO uses BioT5 (chemistry-aware) while LICO uses general Llama-2-7B, making LICO's result more generalizable.

### Issue 3 (Severity: Major): Overclaiming "Proves" for Surrogate-Optimization Correlation
- **Location:** Page 8 - Surrogate Comparison Paragraph
- **Evidence:** "This verifies our hypothesis and proves the effectiveness of LICO for surrogate modeling."
- **Impact:** Overstatement; tested on only 3/23 tasks, and troglitazone_rediscovery shows reverse correlation.
- **Fix:** Replace "proves" with "is consistent with" or "supports." Add caveat about limited task coverage.

### Issue 4 (Severity: Minor): Prediction Layer Architecture Underspecified
- **Location:** Page 5 - Model Architecture
- **Evidence:** "Each prediction consists of a mean and a standard deviation value" — no description of σ parameterization.
- **Impact:** Harms reproducibility of UCB acquisition function; central component is a black box.
- **Fix:** Specify: "The prediction layer outputs (μ, log σ²), with σ² = exp(log σ²) via a linear projection + softplus."

### Issue 5 (Severity: Minor): Intrinsic Property Correlation Claim Unsupported
- **Location:** Page 2 - Introduction / Page 5 - Semi-synthetic Training
- **Evidence:** "Intrinsic functions are closely related to the actual objective functions we want to optimize such as bioactivities."
- **Impact:** Plausible but unverified; molecular weight alone does not predict target bioactivity.
- **Fix:** Soften to "provide coarse structural priors" or add correlation analysis in appendix.

## Actionable Suggestions
### Suggestion 1: Revise Conclusion SOTA Claim (Must)
**Location:** Page 10 - Conclusion
**Action:** Replace "LICO achieves state-of-the-art performance on PMO" with a precise, bounded claim.
**Revised text:** "LICO achieves state-of-the-art performance on the low-budget PMO-1K setting (sum 11.71, highest among 7 methods) and competitive results on the full PMO benchmark (sum 14.708, 4th of 7)—the only method in the top 4 that does not update its model on downstream data during optimization."

### Suggestion 2: Remove Data Contamination Speculation (Must)
**Location:** Page 8 - Results Discussion
**Action:** Delete the sentence "which possibly has data contamination issues, since the finetuning data may have included similar tasks." Replace with objective comparison: "MOLLEO uses BioT5, a chemistry-aware LLM finetuned on molecular data, while LICO uses Llama-2-7B, a general-purpose LLM. This makes LICO's competitive result noteworthy for demonstrating that general LLMs can succeed in molecular BBO without domain-specific pretraining."

### Suggestion 3: Replace "Proves" with Evidence-Consistent Language (Must)
**Location:** Page 8 - Surrogate Comparison
**Action:** Change "This verifies our hypothesis and proves the effectiveness of LICO for surrogate modeling" to "These results on three objectives are consistent with the hypothesis that surrogate model quality translates to optimization performance, motivating further analysis across additional tasks."

### Suggestion 4: Specify Prediction Layer Architecture (Nice-to-have)
**Location:** Page 5 - Model Architecture §4.1
**Action:** Add after "Each prediction consists of a mean and a standard deviation value": "The prediction layer is a linear projection that outputs (μ, log σ²). We apply softplus to obtain σ = √(exp(log σ²)), ensuring positivity. The predictive distribution is pθ(y | x, Dobs) = N(μ, σ²)."

### Suggestion 5: Restructure Related Work into Comparison Axes (Nice-to-have)
**Location:** Page 3-4 - Related Work
**Action:** Reorganize "LLMs for Optimization" and "LLMs for Molecular Optimization" sub-sections around 3 axes: (1) Input representation — prompt-based vs learned embeddings, (2) Role — surrogate prediction vs candidate generation, (3) Training data — text corpora vs molecular data vs synthetic.
**Add a paragraph:** "The closest precursor to LICO is Optformer [Chen et al., 2022], which also trains a transformer for in-context function prediction. However, Optformer trains from scratch on synthetic functions, whereas LICO leverages a pretrained LLM with language guidance, enabling transfer from language pretraining to molecular domains."

### Suggestion 6: Add Numerical Stability Note for Tanimoto Kernel (Nice-to-have)
**Location:** Page 6 - Equation 4
**Action:** Add "ε = 1e-8" to denominator to prevent division by zero for zero-fingerprint inputs.

### Suggestion 7: Add Quantitative Correlation Analysis for Intrinsic Properties (Nice-to-have)
**Location:** Page 2 or Appendix
**Action:** Add a small table or figure in the appendix showing Spearman correlation between the 47 intrinsic properties and each PMO objective. This would validate the claim that intrinsic properties are "closely related" to target objectives.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current narrative follows: BBO problem → LLM capabilities → Prior LLM optimization (text-based) → Limitations → LICO method → Experiments → Conclusion. This structure is logical but could be strengthened.

**Key weakness in current storyline:** The domain-specific motivation (molecular optimization) is introduced late. The abstract mentions "molecular domain" but the first two introduction paragraphs discuss BBO and LLMs generically. The reader does not learn *why molecules are hard* until mid-way through page 2.

### Recommended Storyline: "Domain-First" Approach
**Arc:** Molecular optimization challenge → Why existing methods (GP BO, text-LLM) fall short → Key insight (embedding space ICL with language guidance) → LICO architecture → Semi-synthetic training → Results.

### Complete Abstract Outline (4 sentences)
- **S1 (Problem):** "Optimizing molecular properties such as drug bioactivity is a critical black-box optimization problem where each evaluation requires expensive experiments, making sample-efficient surrogate modeling essential."
- **S2 (Gap):** "Existing LLM-based optimization methods rely on natural language descriptions, limiting their applicability to scientific domains like molecular design where inputs are structural objects that lose information when verbalized."
- **S3 (Method):** "We propose LICO, which equips a frozen LLM with learnable embedding layers for molecular fingerprints and property scores, plus a prediction head, enabling in-context surrogate modeling in the LLM's hidden space rather than text space."
- **S4 (Result):** "Trained on a mixture of 47 intrinsic molecular properties and GP-generated synthetic functions, LICO achieves state-of-the-art performance on the low-budget PMO-1K benchmark (sum 11.71, best among 7 methods) and competitive results on the full PMO benchmark without any task-specific finetuning."

### Complete Introduction Outline (5 paragraphs)

**P1 — Molecular BBO as a critical scientific challenge**
- Role: Establish the concrete domain (molecular optimization) and why it matters (drug discovery).
- Key claim: "Designing molecules with desired properties is a black-box optimization problem where each evaluation requires costly wet-lab experiments, making sample efficiency paramount."
- Evidence: Cite PMO, ZINC, and the practical importance of molecular optimization.
- Transition: "A central bottleneck is learning an accurate surrogate model from sparse observations."

**P2 — Why existing surrogates and text-based LLM methods are insufficient**
- Role: Identify the gap — GP surrogates have limited capacity, text-based LLM optimization requires natural language.
- Key claim: "GP-based surrogates struggle with high-dimensional molecular fingerprints, while LLM methods that require natural language descriptions face two issues: molecules cannot be faithfully encoded as text, and verbose tokenization limits context length."
- Evidence: Cite GP BO limitations, cite LLM optimization works [Yang, Chen, Zhang, Liu].
- Transition: "This motivates a method that leverages LLM pattern-matching without requiring natural language input."

**P3 — LICO: cross-modal in-context learning via embedding adapters**
- Role: Present the high-level method intuition.
- Key claim: "We propose to extend LLMs to molecular domains by learning separate embedding layers that map fingerprints and scores to the LLM's existing hidden space, allowing in-context learning without text tokenization."
- Evidence: Contrast with FPT (no language guidance).
- Transition: "However, the model needs training data — which brings us to semi-synthetic training."

**P4 — Semi-synthetic training bridges intrinsic priors and function diversity**
- Role: Explain the training strategy.
- Key claim: "Training on 47 intrinsic molecular properties provides domain-relevant priors, while GP-generated synthetic functions prevent overfitting and encourage generalization."
- Evidence: Preview ablation results (Table 4).
- Transition: "With this training, LICO generalizes to unseen objectives via in-context prompting alone."

**P5 — Contributions summary**
- Role: Explicit bulleted contributions.
- Key claim: Three contributions: (1) embedding-adapter architecture for LLM-based molecular surrogate, (2) semi-synthetic training, (3) SOTA low-budget PMO results.
- Evidence: Brief performance preview.
- Transition: "We now describe the method in detail."

### Alternative Storyline Option 2: "BBO-General" Approach
Lead with the general BBO framing but embed molecular examples immediately. This would suit a broader audience but risks dilution. Not recommended unless targeting a general ML conference.

### Alternative Storyline Option 3: "Method-First" Approach
Start with the technical challenge (how to make LLMs work for non-text domains) and use molecular optimization as a case study. This would better highlight the technical novelty but may underweight domain significance.

## Priority Revision Plan
### P0 — Must Fix (Before Resubmission)

| Priority | Item | Effort | Impact | Acceptance Criteria |
|----------|------|--------|--------|---------------------|
| P0.1 | Revise conclusion SOTA claim to match full-PMO results (4th place) | Low (5 min) | High | Claim is bounded to PMO-1K; full-PMO described as "competitive" |
| P0.2 | Remove MOLLEO data contamination speculation | Low (5 min) | High | Replaced with objective cross-method comparison |
| P0.3 | Replace "proves" with "is consistent with" | Low (5 min) | Medium | Causal language downgraded to evidence-consistent wording |

### P1 — Strongly Recommended

| Priority | Item | Effort | Impact | Acceptance Criteria |
|----------|------|--------|--------|---------------------|
| P1.1 | Specify prediction layer architecture (μ, log σ², softplus) | Low (15 min) | High | Reproducibility of UCB acquisition is ensured |
| P1.2 | Add numerical stability epsilon to Tanimoto kernel | Low (5 min) | Low | Division-by-zero risk documented |
| P1.3 | Restructure related work around comparison axes | Medium (2 hrs) | Medium | Clear differentiation from Optformer and other LLM-based methods |
| P1.4 | Add intrinsic-property correlation analysis in appendix | Medium (4 hrs) | Medium | Validates the "closely related" claim with empirical data |

### P2 — If Time Permits

| Priority | Item | Effort | Impact | Acceptance Criteria |
|----------|------|--------|--------|---------------------|
| P2.1 | Expand surrogate quality-optimization correlation test to >10 tasks | High (days) | Medium | Strengthens the surrogate-efficacy claim |
| P2.2 | Add LLM scaling experiment with 13B+ model | Medium (2 days) | Medium | Stronger scaling evidence |
| P2.3 | Add matched-capacity ablation to isolate LLM pretraining benefit | Medium (1 day) | Medium | Separates architecture from pretraining effects |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | PMO-1K optimization (1000 calls) | 23 PMO objectives, 5 seeds, 7 methods | AUC Top-10 (min-max scaled) | LICO sum 11.71 (best) | LICO achieves SOTA on low-budget setting | MOLLEO sum 11.65 is close; some tasks LICO underperforms |
| E2 | Full PMO optimization (10000 calls) | 23 PMO objectives, 5 seeds, 7 methods | AUC Top-10 | LICO sum 14.708 (4th) | LICO is competitive without task finetuning | Behind Genetic GFN (15.68) and Augmented Memory (15.00) |
| E3 | Language instruction ablation | 5 PMO tasks, 3 variants | AUC Top-10 | Full LICO 3.099 > w/o prompt 3.060 > w/o language 2.927 | Language guidance helps in-context learning | Only 5 tasks tested |
| E4 | Synthetic ratio ablation | 5 PMO tasks, 4 ratios (0, 0.1, 0.5, 1.0) | AUC Top-10 | Mix (0.1) 3.099 > intrinsic-only 3.010 > synthetic-only 2.936 | Semi-synthetic training outperforms either alone | Only 5 tasks; optimal ratio may vary per task |
| E5 | Pretrained vs scratch LLM | 5 PMO tasks, same 7B size | AUC Top-10 | Pretrained 3.099 > Scratch 2.898 | LLM pretraining provides transferable pattern matching | Scratch transformer uses different architecture (Garg et al.) |
| E6 | LLM size scaling | 8 PMO tasks, 4 models (1.8B-7B) | Sum performance | Llama-2-7B best; monotonic improvement with size | Larger LLMs transfer better to BBO | Only up to 7B; limited task count |
| E7 | Surrogate quality comparison (LICO vs GP) | 3 objectives, 32-512 context | NLL, MSE, RMS Cal | LICO better on 2/3; GP better on 1/3 | Surrogate quality correlates with optimization | Only 3 tasks; causal link not isolated from candidate generation |
| E8 | GPT-4 comparison (Appendix C.3) | 3 objectives, 32-512 context | MSE | LICO significantly outperforms GPT-4o | Text-based prompting is insufficient for molecular property prediction | Only 3 tasks; expensive API calls |
| E9 | LLM embedding baselines (Appendix C.4) | 23 PMO tasks, MLP+GP on LLM embeddings | AUC Top-10 | LICO best on 14/23 tasks | In-context learning beats embedding+regressor approach | — |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper's core contribution is a method (LLM + embedding adapters + semi-synthetic training) that is conceptually novel. However, the novelty boundaries are not clearly delineated from Optformer and FPT. Without external literature verification, the degree of incremental advance cannot be fully assessed.

**Reproducibility:** Partially supported. Training details (hyperparameters, LoRA rank, batch size) are reported. However, the prediction layer architecture (how σ is computed), Tanimoto kernel stability, and exact prompt format (including tokenizer behavior for <x> and <y>) are underspecified.

**Practical Impact:** The PMO-1K result is practically meaningful (high sample efficiency), but the full-PMO ranking (4th) tempers the claim of dominance. The practical advantage is clearest in low-budget settings.

### Proposed Research Experiments

**P0 Experiment: Surrogate-Quality Correlation Expansion**
- **Target Claim:** Surrogate model quality predicts optimization performance.
- **Hypothesis:** LICO's prediction advantage over GP on more tasks will correlate with optimization advantage.
- **Minimal Design:** Replicate the surrogate comparison (Figure 2) on 10 tasks instead of 3, using the same controlled candidate generation pipeline.
- **Controls/Baselines:** Same GP baseline; same candidate pool; same acquisition function.
- **Metrics:** NLL, MSE, RMS Cal for prediction; AUC Top-10 for optimization.
- **Success Criterion:** Spearman ρ > 0.6 between prediction NLL improvement and optimization AUC improvement.
- **Estimated Cost/Time:** 2-3 GPU-days.
- **Expected Gain:** Strong evidence for the central causal claim of the paper.

**P1 Experiment: Matched-Capacity Ablation for Pretraining Benefit**
- **Target Claim:** LLM pretraining provides benefits beyond architecture scale.
- **Hypothesis:** A scratch-trained transformer of equal parameter count and training FLOPs will underperform.
- **Minimal Design:** Train a scratch transformer with the same number of parameters, training steps, and data as LICO's total trained parameters (base LLM frozen + LoRA + embeddings).
- **Controls/Baselines:** Same architecture family; same data; same optimization pipeline.
- **Metrics:** AUC Top-10 on 10 PMO tasks.
- **Success Criterion:** Pretrained LICO > scratch LICO across >8/10 tasks.
- **Estimated Cost/Time:** 3-5 GPU-days.
- **Expected Gain:** Stronger evidence for the pretraining transfer claim.

**P1 Experiment: Cross-Domain Transfer Test**
- **Target Claim:** LICO generalizes to non-molecular scientific domains.
- **Hypothesis:** LICO's architecture (embedding layers + language prompt) can be applied to protein optimization with minimal changes.
- **Minimal Design:** Replace molecular fingerprints with protein sequence embeddings (one-hot or ESM); train intrinsic+GP semi-synthetic data for protein properties; evaluate on 1-2 protein optimization benchmarks.
- **Controls/Baselines:** GP BO with sequence kernel; random search.
- **Metrics:** AUC Top-10, top-1 best value.
- **Success Criterion:** LICO outperforms GP BO and random search.
- **Estimated Cost/Time:** 5-7 GPU-days.
- **Expected Gain:** Demonstrates generality claims and broadens contribution scope.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper presents a technically sound and empirically evaluated method with clear strengths: the cross-modal adapter architecture is novel, the semi-synthetic training strategy is well-motivated, and the PMO-1K results are strong. However, the score is tempered by three concerns: (1) the conclusion's SOTA claim is factually inconsistent with full-PMO results (4th place), which raises credibility concerns; (2) the paper contains speculative criticism of baselines and overclaiming language ("proves"); (3) without external literature verification (Retrieval-Disabled Mode), the novelty relative to Optformer, FPT, and Kristiadi et al. cannot be fully assessed. On research value, LICO's contribution — enabling LLMs for non-text scientific BBO with embedding adapters and semi-synthetic training — is practically relevant and likely to be influential. The primary scoring dimensions (research value + novelty) support a mid-range score, as the method is solid but incremental novelty and factual precision issues prevent a higher rating.

**Post-Revision Target: [7.0, 8.0] / 10**

**Rationale for target:** After the P0 fixes (correcting SOTA claim, removing speculation, softening causal language), the paper would have consistent evidence-claim alignment and objective tone. Adding the P1 architectural specification would improve reproducibility. The upper bound (8.0) assumes the authors also address the related-work restructuring and add the intrinsic property correlation analysis. The lower bound (7.0) reflects a minimal fix scenario where only the three P0 items are addressed. External literature verification (currently deferred) could further adjust this range — if strong overlap with Optformer or Kristiadi et al. is found, the target should shift downward; if distinct novelty is confirmed, it could shift upward.