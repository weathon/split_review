## Summary
# Final Review Report

## Summary

This paper addresses the problem of improving group fairness in classification when sensitive attributes (e.g., race, gender) are unavailable due to privacy regulations. The authors propose **Reckoner**, a confidence-based dual-VAE framework with two key components: (1) learnable noise that modifies input features to suppress spurious correlations, and (2) a dual-model knowledge-sharing mechanism between a High-Confidence generator (trained on high-confidence predictions) and a Low-Confidence generator (trained on low-confidence predictions). The motivation comes from an exploratory analysis on COMPAS showing that low-confidence data regions exhibit better fairness but lower accuracy, while high-confidence regions show the opposite pattern.

**Strengths:** The paper tackles a practically important problem (fairness without sensitive attributes) with a novel confidence-based perspective. The exploratory analysis in Section 3 provides useful empirical observations connecting prediction confidence to fairness. The dual-model design is conceptually interesting, and the ablation study attempts to isolate the contributions of the two main components.

**Core Weaknesses:** (1) The learnable noise mechanism lacks an explicit fairness regularization objective, making its debiasing effect indirect and difficult to guarantee. (2) The experimental evaluation has reproducibility gaps (missing hyperparameters, data splits, statistical significance tests, confidence threshold sensitivity analysis). (3) Several claims are overstated relative to the evidence (generalization to images/audio, "relative improvement" wording, "state-of-the-art" without proper comparison scope). (4) The novelty positioning is unclear without external literature verification (deferred to manual check per Retrieval-Disabled Mode). (5) The knowledge-sharing mechanism has underspecified with notation inconsistencies and underspecified loss terms.

External literature verification was unavailable in this run (Retrieval-Disabled Mode active). Novelty/comparison conclusions are intentionally deferred for manual verification.

## Strengths
**S1 — Practically relevant problem setting.** The paper addresses the realistic scenario where sensitive attributes (race, gender) are unavailable due to privacy regulations. This is a timely and important problem in fair ML, and the motivation is clearly established with reference to GDPR and real-world deployment constraints.

**S2 — Interesting confidence-based exploratory analysis.** Section 3 provides a novel empirical observation: data subsets with low predictive confidence exhibit better fairness (Equalised Odds 8.10% vs 25.10% for high-confidence subsets on COMPAS). The distribution analysis of age across racial groups in different confidence intervals is genuinely insightful and well-illustrated in Figure 1. This analysis provides a compelling motivation for the dual-model architecture.

**S3 — Clean ablation design.** The ablation study (Section 5.2) cleanly separates the two components: learnable noise only vs. pseudo-learning only vs. full Reckoner. This allows readers to attribute effects to each component. The reconstruction distance analysis in Figure 3 provides an interesting diagnostic that goes beyond simple metric comparisons.

**S4 — Competitive fairness results.** On COMPAS, Reckoner achieves the best Equalised Odds (17.10%) with a 3.21 percentage point improvement over the best baseline. On New Adult, the improvement is more substantial: 5.01 percentage points over the best baseline for Equalised Odds. These results demonstrate that the confidence-based approach is a promising direction for fairness without sensitive attributes.

**S5 — Reasonable narrative structure.** The paper follows a clear logical flow: empirical observation (Section 3) -> method design (Section 4) -> experimental validation (Section 5). The motivation section (4.1) explicitly connects back to the analysis findings, creating a coherent story.

## Weaknesses
**W1 — Underspecified learnable noise mechanism (Major).** The formulation ($\tilde{x}_i = x_i + g_\omega(\eta)$, Eq. 1) lacks specification of noise dimensionality, initial variance, and optimization objective for $\omega$. Most critically, the noise wrapper $g_\omega$ is optimized jointly with the VAE through the classification + ELBO losses, which contain no explicit fairness regularization. Without a debiasing signal, it is unclear why the noise should learn to suppress bias rather than task-irrelevant noise or nothing at all. This mechanism needs either theoretical justification or an explicit fairness objective.

**W2 — Missing reproducibility details (Major).** The experimental section does not report: data split ratios, learning rate, batch size, training epochs, VAE latent dimension, MLP hidden dimension, feature hashing dimension, or number of random seeds. Baseline methods (DRO, ARL) are not confirmed to be re-tuned under the same conditions. This makes it impossible for readers to reproduce or verify the results independently.

**W3 — Overclaimed results interpretation (Major).** Several claims in the Results section (Page 8) use imprecise language: 
- "Relative improvement of about 3.21%" actually refers to absolute percentage points (3.21 pp), which is a critical factual precision issue.
- "Significant edge" is used without statistical significance tests. Overlapping confidence intervals (e.g., Reckoner Equalised Odds 17.10$\pm$2.01 vs ARL 20.95$\pm$1.01) suggest the improvement may not be statistically significant.
- Reckoner achieves only third-highest accuracy on New Adult (84.02% vs ARL 85.32%, a 1.30% gap), but this trade-off is understated.

**W4 — Unsupported generalization claim (Major).** The claim that the framework "exhibits greater generalisability, particularly when dealing with data where proxy identification is challenging, such as images and audio" (Page 3) is entirely unsupported by experiments, which are limited to two tabular datasets (COMPAS, New Adult). No image or audio data is evaluated.

**W5 — Pseudo-learning mechanism is underspecified (Major).** The rollback operation (reset to initialization after every 3 iterations) prevents the Low-Conf generator from accumulating knowledge, which contradicts the notion of "knowledge sharing." The loss terms $L_\mu$ and $L_{\sigma^2}$ in Eq. (2) are not explicitly defined (MSE? direction of regression?). Notation inconsistency between $\Theta_H$ (Eq.  and $\theta_i^H$ (Eq. 3 vs Eq. 4) creates confusion.

**W6 — Lack of novelty verification (Deferred).** Without external literature retrieval (Retrieval-Disabled Mode), novelty claims cannot be independently verified. The paper's claim of being the first to use confidence-based splitting with learnable noise + dual VAE for fairness without sensitive attributes requires manual comparison against related methods (e.g., Grari et al. 2022's causal VAE, Chai et al. 2022's knowledge distillation for fairness without demographics).

**W7 — Ablation interpretation is speculative (Minor).** The reconstruction distance metric (Figure 3) is used as a proxy for "information removal," but there is no evidence that the removed information is bias-related rather than task-relevant. The interpretation that "learnable noise changes the distribution of certain features" is post-hoc without direct causal evidence.

**W8 — Confidence threshold not justified (Minor).** The 0.6 threshold is adopted from Lakkaraju et al. (2017) which addresses a different problem (unknown unknowns). No sensitivity analysis is provided to show that results are robust to the choice of threshold.

## Key Issues
### Issue 1: Learnable noise lacks explicit fairness signal (Severity: Major)
The noise wrapper $g_\omega$ is trained end-to-end with only classification and VAE reconstruction losses. There is no adversarial discriminator, no fairness regularizer, and no constraint that forces the noise to remove bias. The paper's claim that noise "neutralises embedded unfairness" (Page 5, Section 4.3.1) is thus a hypothesis, not a demonstrated property. The ablation study's reconstruction distance metric does not establish that removed information is bias-related. **Fix:** Add an explicit fairness regularization to the noise training, or at minimum provide a correlation analysis showing that noise-augmented features have lower correlation with the (unobserved) sensitive attribute proxy.

### Issue 2: Reproducibility gaps threaten validity (Severity: Major)
Several critical experimental details are missing: data split ratios (only "same split as Chai et al. 2022" is mentioned for COMPAS, and nothing for New Adult), hyperparameters (learning rate, batch size, epochs, latent dimension, hash dimension), and random seed count. The unusually small accuracy standard deviation for Reckoner on New Adult (0.06% vs 0.26-0.86% for baselines) raises questions about evaluation protocol consistency. **Fix:** Provide a complete hyperparameter table and reproducibility appendix.

### Issue 3: Results interpretation includes factual imprecision (Severity: Major)
The phrase "relative improvement of about 3.21%" conflates absolute percentage points with relative improvement. The word "significant" is used without statistical testing. Given overlapping confidence intervals for several key comparisons, the claimed advantages may not be statistically reliable. **Fix:** Reword all improvement claims to "X percentage points" (absolute) or compute proper relative percentages. Add statistical significance tests (paired bootstrap over seeds) for all main comparisons.

### Issue 4: Pseudo-learning mechanism is not fully specified (Severity: Major)
The training loop involves: (a) Low-Conf generator trained for 3 iterations on pseudo-distribution, (b) rollback to initialization, (c) parameter averaging via Eq. (3), (d) gradient update on averaged parameters via Eq. (4). The loss terms $L_\mu$ and $L_{\sigma^2}$ in Eq. (2) are not explicitly defined. The notation inconsistency between $\Theta_H$ (Eq. 3) and $\theta_i^H$ (Eq. 4) creates confusion. **Fix:** Define all loss terms explicitly, use consistent notation, and provide a pseudocode algorithm in the appendix.

### Issue 5: Issue 5: Unsupported generalization claim (Severity: Major)
The claim about "greater generalisability... such as images and audio" (Page 3) has zero experimental support. All evaluations are on tabular data (COMPAS, New Adult). **Fix:** Remove the claim or relegate it to future work, and add at least one proof-of-concept experiment on a non-tabular fairness benchmark.

### Issue 6: Confidence threshold sensitivity unexamined (Severity: Minor)
The threshold of 0.6 determines the 65%/35% data split, which directly controls the amount of training data available for each generator and the proportion of data considered "high-confidence." The paper provides no analysis of how results change with different thresholds. **Fix:** Add a sensitivity analysis sweeping the threshold from 0.5 to 0.8, reporting accuracy and fairness for each setting.

### Issue 7: Novelty positioning deferred (Deferred)
Due to Retrieval-Disabled Mode, external literature verification was not performed. The paper's relationship to the closest related works (Grari et al. 2022 causal VAE, Chai et al. 2022 knowledge distillation, Chai & Wang 2022 contrastive learning, Gupta et al. 2018 proxy fairness) cannot be fully assessed in this review. Manual verification is required before publication.

## Actionable Suggestions
### Suggestion 1: Strengthen the learnable noise mechanism (Must)

**Problem:** The noise formulation lacks both specification and explicit fairness guidance.

**Action:**
1. **Specify details:** State the dimension of $\eta$ (should match $x_i$), the initial distribution $\mathcal{N}(0, \sigma^2 I)$ with $\sigma$ reported, and whether $\sigma$ is fixed or learned.
2. **Add explicit fairness regularization:** Augment $L_H$ with a term that penalizes correlation between noise-augmented features and proxy attributes (e.g., a discriminator loss or mutual information minimization). Alternatively, replace the regressor with an adversarial classifier that tries to predict sensitive group membership from noise-augmented representations.
3. **Add diagnostic experiment:** After training, measure the correlation between each input feature and the (excluded) sensitive attribute, both before and after noise perturbation. Show that learnable noise reduces these correlations.

**Expected benefit:** Makes the debiasing mechanism theoretically grounded and empirically verifiable.

### Suggestion 2: Fix results reporting precision (Must)

**Problem:** The "relative improvement" wording and lack of significance tests undermine scientific credibility.

**Action:**
1. Replace all occurrences of "X% improvement" with "X percentage point improvement" when referring to absolute differences in fairness metrics.
2. If relative improvement is intended (e.g., (20.31-17.10)/20.31 = 15.8%), compute and report it correctly.
3. Add statistical significance tests: for each main comparison (Reckoner vs. best baseline per metric, per dataset), report a paired bootstrap p-value or confidence interval of the difference.
4. Report the number of random seeds used (minimum 5) and ensure all methods use the same seeds.

**Expected benefit:** Removes factual ambiguity and strengthens the reliability claims.

### Suggestion 3: Add reproducibility details (Must)

**Action:**
In a new appendix, provide:
- Complete hyperparameter table: learning rate, batch size, optimizer (Adam $\beta_1, \beta_2$), training epochs, VAE latent dimension, MLP hidden dimension(s), feature hashing dimension, number of seeds.
- Data split ratios for both datasets (specify training/validation/test percentages and whether stratified by label and/or sensitive attribute).
- Confidence threshold sensitivity analysis: sweep threshold from 0.5 to 0.8 in 0.05 increments, report accuracy and both fairness metrics for each setting.
- Baseline tuning: state whether DRO, ARL, FairRF, and Chai et al. were re-tuned under identical conditions or numbers taken from prior work.

**Expected benefit:** Enables independent verification and improves review trust.

### Suggestion 4: Clarify pseudo-learning algorithm (Must)

**Action:**
1. Define $L_\mu$ and $L_{\sigma^2}$ explicitly: e.g., $L_\mu = \|\mu_L - \mu_H\|_2^2$, $L_{\sigma^2} = \|\sigma^2_L - \sigma^2_H\|_2^2$ (MSE).
2. Clarify whether $\mu_H$ and $\sigma^2_H$ are detached from the computational graph (stop-gradient) or allow gradients to flow into the High-Conf generator.
3. Use consistent notation: keep $\theta$ (lowercase) throughout.
4. Provide a pseudocode algorithm for the Refinement Stage training loop, clearly showing:
   - When the High-Conf generator generates pseudo-distributions.
   - When the Low-Conf generator trains (3 iterations) and resets.
   - When the parameter averaging (Eq. 3/4) occurs.
   - When backpropagation through the averaged parameters happens.

**Expected benefit:** Eliminates ambiguity that currently prevents reproducibility of the core mechanism.

### Suggestion 5: Remove or weaken unsupported generalization claim (Must)

**Action:** Replace the sentence "Hence, our proposed framework exhibits greater generalisability, particularly when dealing with data where proxy identification is challenging, such as images and audio" with: "Hence, our proposed framework avoids manual proxy selection, which is a conceptual advantage for settings where proxy identification is difficult. Demonstrating this advantage on non-tabular data (e.g., images) is left for future work."

**Expected benefit:** Removes a claim that invites immediate reviewer rejection.

### Suggestion 6: Add confidence threshold analysis (Nice-to-have)

**Action:** Add a figure showing accuracy, Equalised Odds, and Demographic Parity as functions of the confidence threshold (0.5-0.8). Include the resulting split proportions (e.g., threshold=0.5 → 80%/20% split). Discuss the trade-off: a lower threshold gives the Low-Conf generator more data but may dilute its fairness signal.

**Expected benefit:** Demonstrates the robustness/limitations of the key design choice.

### Suggestion 7: Improve conclusion with limitations (Nice-to-have)

**Action:** Expand the conclusion to include:
- Explicit limitations: binary classification only, tabular data only, two datasets, single sensitive attribute (race).
- Accuracy-fairness trade-off observed.
- Concrete future directions: multi-class extension, image/audio modalities, adversarial debiasing integration, confidence threshold learning.

**Expected benefit:** Improves scientific honesty and provides clear next steps for the community.

### Suggestion 8: Add related-work comparison table (Nice-to-have)

**Action:** Create a table comparing methods for fairness without sensitive attributes across dimensions: need for proxy identification, need for sensitive attributes, applicable data types, training complexity, fairness metric used, and whether theoretical guarantees exist. Position Reckoner in this table.

**Expected benefit:** Makes the novelty positioning explicit and helps readers quickly understand the contribution.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current introduction (Page 1-2) follows this structure:
- P1: Broad applications -> privacy regulations -> two categories of prior work -> critique
- P2: Two challenges (proxy unreliability and accuracy-fairness trade-off)
- P3: Proposed method overview
- P4: Contributions list

**Issues:** P1 tries to cover too much ground (context, literature review, critique) in one paragraph. P2 introduces two challenges but the second one (accuracy-fairness trade-off) is not developed further in the paper. The method overview in P3 appears before the contributions list, which is an unusual order.

### Candidate Storyline 1 (Recommended — "Gap-First" Arc)

**Abstract Outline (S1-S5):**
- **S1 (Problem + Domain):** "Automated decision systems in high-stakes domains require fairness, but growing privacy regulations increasingly restrict access to sensitive demographic attributes such as race or gender."
- **S2 (Prior Gap):** "Existing fairness methods either require sensitive attributes or rely on manually selected proxy features, which is unreliable because bias can be embedded in overlooked attributes and the approach does not generalize to unstructured data."
- **S3 (Proposed Method):** "We propose Reckoner, a confidence-based dual-VAE framework that introduces learnable noise to suppress spurious correlations and enables knowledge sharing between high-confidence and low-confidence generators to learn fairer representations."
- **S4 (Key Result):** "On COMPAS and New Adult benchmarks, Reckoner reduces Equalised Odds by 3.2-5.0 percentage points over competing methods while maintaining competitive accuracy."
- **S5 (Bounded Conclusion):** "Ablation studies validate that both components contribute to the fairness improvement. Limitations include evaluation on binary classification and tabular data only."

**Introduction Outline (P1-P4):**

**P1 — Establish Territory:**
Role: Define the practical stakes and the core problem.
"High-stakes automated decisions in criminal justice, lending, and hiring increasingly rely on machine learning models. These models can propagate societal biases against demographic groups, creating demand for algorithmic fairness. However, regulations such as the GDPR increasingly restrict access to sensitive attributes (race, gender), creating a tension: how can we ensure fairness without the very information needed to measure it?"

**P2 — Identify Gap:**
Role: Explain why existing solutions fall short.
"Prior approaches for fairness without sensitive attributes fall into two paradigms. The first uses proxy features — observed attributes correlated with the sensitive attribute — to approximate group membership [Gupta et al. 2018, Zhao et al. 2022, Yan et al. 2020]. The second uses distributionally robust optimization to improve worst-group utility from observed features [Hashimoto et al. 2018, Lahoti et al. 2020]. Both approaches share a fundamental limitation: they require identifying which observed attributes carry bias information. This is unreliable because bias can be embedded in features that are not selected as proxies (e.g., our analysis on COMPAS reveals that age, rarely used as a proxy, shows distributional differences across racial groups that correlate with prediction bias). Manual proxy selection also fails on unstructured data where feature-level correlation analysis is impractical."

**P3 — Present Solution:**
Role: Introduce Reckoner's intuition and key components.
"In this paper, we propose Reckoner, a confidence-based framework that avoids explicit proxy selection. Our key insight, derived from an exploratory analysis on COMPAS, is that data points near the decision boundary (low confidence) exhibit better fairness but lower accuracy, while high-confidence points have higher accuracy but reduced fairness. Reckoner exploits this by: (1) splitting training data into high- and low-confidence subsets using a logistic regressor, (2) introducing learnable noise to suppress feature-level biases, and (3) enabling a dual-VAE system where the low-confidence generator's fairer representations are transferred to the high-confidence generator."

**P4 — Summary and Contributions:**
Role: State contributions with concrete evidence anchors.
"Our contributions are threefold: (i) we demonstrate through empirical analysis that prediction confidence reveals systematic fairness disparities in non-sensitive attribute distributions across demographic groups, (ii) we introduce Reckoner, which combines learnable noise and dual-model knowledge sharing to improve fairness without sensitive attributes, and (iii) we provide experimental evidence that Reckoner reduces Equalised Odds by 3.2-5.0 percentage points over prior methods on COMPAS and New Adult, with ablation studies validating both components."

### Candidate Storyline 2 — "Empirical Discovery First" Arc

Alternative structure: Start with the COMPAS analysis (Section 3 material) in the introduction, then explain the method as a direct response to this discovery.

P1: Brief motivation (privacy-fairness tension) -> immediately present Figure 1b/1c findings.
P2: "This observation suggests that confidence carries information about where bias lives. We design a method around this insight."
P3: Method overview.
P4: Contributions.

**Comparison with Candidate 1:** Storyline 2 is more original but risks losing readers who are not yet convinced of the problem importance. Storyline 1 is more conventional and easier to follow.

### Recommendation

Select **Candidate Storyline 1**. It provides a clear problem-gap-solution arc, aligns with standard ML paper expectations, and directly answers the three required questions: what is missing in prior work (reliable fairness without manual proxy selection), what this paper solves (confidence-based framework avoiding explicit proxies), and why the approach is better (learnable noise + dual-model knowledge sharing).

## Priority Revision Plan
Ranked by severity and expected impact on paper quality.

### P0 — Must fix before acceptance

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | Fix results interpretation wording | Replace "relative improvement X%" with "X percentage point improvement" throughout results section. | Removes factual imprecision that could lead to rejection. | Low (text edit) |
| P0.2 | Specify learnable noise details and add explicit fairness signal | Define noise dimension/variance, clarify optimization path, and add either adversarial discriminator or correlation analysis. | Makes core mechanism reproducible and theoretically grounded. | Medium (experiment) |
| P0.3 | Add reproducibility appendix | Report all hyperparameters, data splits, seed counts, baseline tuning status. | Enables independent verification; required for any ICLR publication. | Medium (documentation) |
| P0.4 | Remove unsupported generalization claim | Replace "images and audio" claim with bounded future-work statement. | Removes a statement that invites immediate rejection. | Low (text edit) |
| P0.5 | Clarify pseudo-learning loss and algorithm | Define $L_\mu$ and $L_{\sigma^2}$ explicitly; provide pseudocode; fix notation. | Makes the core technical contribution reproducible. | Low (text edit + appendix) |

### P1 — Should fix for strong revision

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Add statistical significance tests | Bootstrap p-values or confidence intervals for key comparisons (Reckoner vs. best baseline per metric/dataset). | Strengthens reliability claims; may reveal which differences are robust. | Medium (experiment) |
| P1.2 | Add confidence threshold sensitivity analysis | Sweep threshold 0.5-0.8, plot accuracy and fairness metrics. | Validates robustness of key design choice. | Medium (experiment) |
| P1.3 | Expand conclusion with limitations | Add explicit limitations and future work directions. | Improves scientific honesty. | Low (text edit) |
| P1.4 | Add related-work comparison table | Table comparing methods across dimensions (proxy need, data type, fairness metric). | Clarifies novelty positioning. | Low (text + table) |

### P2 — Nice-to-have improvements

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | Add OOD evaluation | Evaluate Reckoner on a third dataset (e.g., Law School, German Credit) to demonstrate generalizability. | Broadens empirical scope beyond two datasets. | Medium (experiment) |
| P2.2 | Add fairness-accuracy Pareto plot | Plot accuracy vs. fairness for all methods, showing frontier. | Visualizes the trade-off more honestly. | Low (figure) |
| P2.3 | Add proof-of-concept on non-tabular data | Evaluate on a simple image fairness benchmark (e.g., CelebA with protected attribute). | Supports generalization claim or refutes it. | High (experiment) |

### Execution Order

```
Week 1: P0.1 (text), P0.4 (text), P0.5 (text + pseudocode) → low-effort, high-impact
Week 2: P0.2 (experiment design + correlation analysis) → medium-effort, high-impact
Week 3: P0.3 (documentation appendix) → medium-effort, high-impact
Week 4: P1.1 (significance tests), P1.2 (threshold sweep) → medium-effort, medium-impact
Week 5: P1.3 (conclusion rewrite), P1.4 (comparison table) → low-effort, medium-impact
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Compare Reckoner vs DRO, ARL, FairRF, Chai et al. on COMPAS | Binary classification, race excluded, 6150 samples | Accuracy, Equalised Odds, Demographic Parity | Reckoner achieves best Equalised Odds (17.10%), third-highest accuracy (64.00%) | Reckoner improves fairness over baselines | No significance test; overlapping CIs with best baseline |
| E2 | Same as E1 on New Adult | Binary classification, race excluded, 49531 samples | Same as E1 | Reckoner achieves best fairness (Equalised Odds 5.33%, Demographic Parity 8.28%), third-highest accuracy (84.02%) | Reckoner improves fairness; accuracy trade-off exists | Accuracy gap of 1.30% vs ARL is understated |
| E3 | Ablation: Reckoner without learnable noise | Same as E1, noise removed | Same as E1 + reconstruction distance | Fairness improves (Equalised Odds 16.91%) but accuracy drops to 62.68% | Learnable noise contributes to accuracy preservation | Distance metric does not measure bias removal |
| E4 | Ablation: Reckoner without pseudo-learning | Same as E1, knowledge sharing removed | Same as E1 + reconstruction distance | Accuracy highest (64.17%) but fairness worse (Equalised Odds 18.38%) | Pseudo-learning contributes to fairness | Effect size may not be statistically significant |
| E5 | Subset analysis (Section 3) | COMPAS split by confidence (threshold 0.6) | Equalised Odds, Demographic Parity | Low-confidence subset: EO 8.10%, DP 8.50%; High-confidence: EO 25.10%, DP 32.90% | Low-confidence data is fairer but less accurate | No accuracy reported for subsets; no statistical distribution test |
| E6 | Reconstruction distance analysis (Figure 3) | COMPAS, compare full Reckoner vs ablations | L2 distance (reconstructed - original) | Full: 61.35; w/o noise: 49.47; w/o pseudo-learning: 55.24 | Learnable noise increases reconstruction distance | No error bars; single/unreported number of runs |

### Research-Theme Gap Diagnosis

| Research-Value Claim | Supported? | Gap | Required Evidence |
|--------------------|-----------|-----|-----------------|
| **New Knowledge:** Confidence-based splitting reveals fairness-accuracy relationship | Partially proven | Qualitative analysis only; no statistical tests for distribution differences | KS tests on age distributions; accuracy values for subsets |
| **New Knowledge:** Learnable noise suppresses bias | Unsupported | No causal evidence linking noise to bias reduction to bias reduction | Correlation analysis between noise-augmented features and proxy attribute |
| **Methodological Novelty:** Dual-model knowledge sharing improves fairness | Partially proven | Ablation shows it helps but mechanism is vague | Pseudocode, explicit loss definitions, standalone verification of Low-Conf fairness |
| **Practical Impact:** Reckoner generalizes beyond tabular data | Unsupported | No non-tabular experiments | At least one proof-of-concept on image/audio fairness benchmark |
| **Reproducibility:** Results can be independently verified | Partially proven | Many hyperparameters and data splits unreported | Complete reproducibility appendix |

### Proposed Research Experiments (P0/P1/P2)

**Experiment P0.1: Learnable Noise Correlation Analysis**correlation analysis (Must)
- **Target Claim:** Learnable noise reduces spurious correlations between features and sensitive attributes.
- **Hypothesis:** The correlation between noise-augmented features $\tilde{x}_i$ and the excluded sensitive attribute $s_i$ is lower than the correlation between original features $x_i$ and $s_i$.
- **Minimal Design:** Train Reckoner on COMPAS; for each feature dimension, compute Pearson correlation with race (the excluded sensitive attribute) before and after noise augmentation. Report mean absolute correlation reduction.
- **Controls/Baselines:** Compare against the "w/o noise" ablation and a random noise baseline (non-learnable Gaussian noise).
- **Metrics:** Mean absolute correlation reduction, feature-level correlation scatter plot.
- **Success Criterion:** Statistic:** Learnable noise reduces mean absolute correlation by at least 20% compared to original features.
- **Estimated Cost:** Low (2 GPU hours, existing model).
- **Expected Paper-Quality Gain:** Provides direct evidence for the debiasing mechanism.

**Experiment P0.2: Significance testing for main results (Must)**
- **Target Claim:** Reckoner significantly outperforms baselines in fairness.
- **Hypothesis:** The fairness improvement is statistically significant at $p < 0.05$.
- **Minimal Design:** Run Reckoner and the best baseline on each dataset with 10 different random seeds. Compute paired bootstrap p-values for the difference in Equalised Odds and Demographic Parity.
- **Controls/Baselines:** All baselines from Tables 2-3 with same seeds.
- **Metrics:** p-value, 95% CI of difference, effect size (Cohen's d).
- **Success Statistic:** p < 0.05 for at least one fairness metric on each dataset.
- **Estimated Cost:** Low (same experiment setup, more seeds).
- **Expected Paper-Quality Gain:** Transforms qualitative "improvement" claim into statistically grounded finding.

**Experiment P0.3: Confidence threshold sensitivity (Must)**
- **Target Claim:** Results are robust to the choice of confidence threshold.
- **Hypothesis:** Reckoner's fairness improvement persists across a range of thresholds (0.5-0.8).
- **Minimal Design:** Sweep threshold from 0.5 to 0.8 in 0.05 increments; for each value, run Reckoner and report accuracy and both fairness metrics on both datasets.
- **Controls/Baselines:** Include the 0.6 setting as reference point.
- **Metrics:** Accuracy, Equalised Odds, Demographic Parity as functions of threshold.
- **Success Statistic:** Fairness improvement over best baseline is maintained (within 1 pp) for thresholds 0.55-0.7.
- **Estimated Cost:** Medium (5 x 2 = 10 additional training runs).
- **Expected Paper-Quality Gain:** Validates the central design choice.

**Experiment P1.1: OOD evaluation on third dataset (Should)**
- **Target Claim:** Reckoner is effective across different tabular fairness datasets.
- **Hypothesis:** Reckoner improves fairness on Law School or German Credit dataset.
- **Minimal Design:** Apply same binary classification setup with race/gender as sensitive attribute. Compare against at least 3 baselines.
- **Controls/Baselines:** DRO, ARL, Chai et al.
- **Metrics:** Accuracy, Equalised Odds, Demographic Parity.
- **Success Statistic:** Reckoner achieves best or second-best Equalised Odds.
- **Estimated Cost:** Low-Medium (reuse existing code, new dataset).
- **Expected Paper-Quality Gain:** Broadens empirical scope beyond two datasets.

**Experiment P2.1: Proof-of-concept on image data (Nice-to-have)**
- **Target Claim:** Reckoner framework can be applied to image classification.
- **Hypothesis:** With CNN encoder replacing linear features, Reckoner improves fairness on CelebA (binary attribute prediction).
- **Minimal Design:** Replace VAE with convolutional VAE; use "Attractive" prediction with "Gender" as sensitive attribute. Compare against a vanilla CNN baseline.
- **Controls/Baselines:** Vanilla CNN, CNN with adversarial debiasing.
- **Metrics:** Accuracy, Equalised Odds, Demographic Parity.
- **Success Statistic:** Reckoner improves Equalised Odds by at least 2 pp over vanilla CNN.
- **Estimated Cost:** High (significant code changes).
- **Expected Paper-Quality Gain:** Supports or refutes the generalization claim; major novelty boost if successful.

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0 — Must fix, before resubmission)
  ├── P0.1: Correlation analysis for learnable noise (proves mechanism)
  ├── P0.2: Statistical significance tests (strengthens claims)  
  ├── P0.3: Confidence threshold sensitivity (validates design)
  └── P0.4: Reproducibility appendix (enables verification)

Stage 2 (P1 — Should fix, strong revision)
  ├── P1.1: OOD evaluation on Law School dataset (broadens scope)
  ├── P1.2: Fairness-accuracy Pareto frontier (honest visualization)
  └── P1.3: Related-work comparison table (positions novelty)

Stage 3 (P2 — Nice-to-have, future work)
  └── P2.1: Proof-of-concept on image data (tests generalization)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: **5.5 / 10**

**Scoring rationale:**
- **Research Value (5/10):** The problem is practically important and timely. The confidence-based exploratory analysis provides a novel perspective. However, the lack of explicit fairness regularization in the learnable noise mechanism and the absence of statistical significance tests limit the scientific contribution's depth.
- **Novelty (4/10):** The confidence-based dual-VAE approach is conceptually interesting, but similar ideas (knowledge distillation for fairness without demographics [Chai et al. 2022], causal VAE for fairness without sensitive attributes [Grari et al. 2022]) exist in the literature. External verification is needed for a definitive assessment (deferred due to Retrieval-Disabled Mode). The claim of generalization to images/audio is unsupported.
- **Validity/Soundness (5/10):** Reproducibility gaps (missing hyperparameters, data splits, seed counts) prevent full verification of results. The "relative improvement" wording is factually imprecise. Overlapping confidence intervals suggest some results may not be statistically significant.
- **Presentation (6/10):** The paper is generally well-written and follows a clear narrative structure. However, the Related Work section reads as a chronological list rather than analytical comparison. Notation inconsistencies (Eq. 3 vs Eq. 4) reduce clarity.

### Post-Revision Target: **[6.5, 7.5] / 10**

**Conditions for reaching target:**
- Fix all P0 issues (results wording, learnable noise specification, reproducibility appendix, unsupported claim removal, pseudo-learning pseudocode).
- Add statistical significance tests and confidence threshold sensitivity analysis (P1 issues).
- If external literature verification confirms sufficient novelty gap over Grari et al. 2022 and Chai et al. 2022, the upper bound of 7.5 is achievable.
- The lower bound (6.5) assumes P0 fixes but no additional experiments beyond significance testing and threshold sensitivity.

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current Score: 5.5/10]
    │
    ├── P0 Fixes (Must)
    │   ├── Fix results wording → +0.5 (factual precision)
    │   ├── Specify noise mechanism → +0.3 (method clarity)
    │   ├── Reproducibility appendix → +0.5 (trust/verifiability)
    │   ├── Remove unsupported claim → +0.2 (scientific honesty)
    │   └── Clarify pseudo-learning → +0.3 (method clarity)
    │
    ├── P1 Fixes (Should)
    │   ├── Significance tests → +0.5 (statistical rigor)
    │   ├── Threshold sensitivity → +0.3 (robustness)
    │   └── Conclusion + comparison table → +0.2 (positioning)
    │
    └── P2 (Nice-to-have)
        └── OOD evaluation → +0.5 (generality)
        
[Target: 6.5-7.5/10 after P0+P1]
```

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Fairness without sensitive attributes]
    │
    ├── [Analysis (Section 3): Confidence reveals fairness disparities]
    │   └── Evidence: Figure 1, Table 1 (descriptive stats)
    │       ⚠ Gap: No statistical distribution tests, no accuracy per subset
    │
    ├── [Method (Section 4): Reckoner]
    │   ├── Learnable noise (Eq. 1)
    │   │   ⚠ Gap: No explicit fairness objective
    │   ├── Identification (Sec 4.2): LR → threshold 0.6 split
    │   │   ⚠ Gap: Threshold choice not justified
    │   └── Dual-model knowledge sharing (Eq. 2-5)
    │       ⚠ Gap: Loss terms underspecified, notation inconsistency
    │
    └── [Experiments (Section 5)]
        ├── Main results (Tables 2-3)
        │   ⚠ Gap: No significance tests, overclaimed wording
        ├── Ablation (Figure 3)
        │   ⚠ Gap: Distance metric not causally linked to fairness
        └── Conclusion
            ⚠ Gap: No limitations stated
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

*Note: This taxonomy is constructed from the paper's self-cited references. External verification is deferred (Retrieval-Disabled Mode).*

```text
Fairness Improvement Approaches (Root)
│
├── Branch 1: Requires Sensitive Attributes
│   ├── Leaf 1.1: Fairness Regularization [Kamishima+2011, Beutel+2019]
│   └── Leaf 1.2: Constrained Optimization [Hardt+2016, Zafar+2019]
│
├── Branch 2: Fairness Without Sensitive Attributes
│   ├── Leaf 2.1: Proxy-based methods
│   │   ├── Gupta+2018 (proxy groups via clustering)
│   │   ├── Datta+2017 (zip code as proxy for race)
│   │   ├── Zhao+2022 (FairRF: reweighting correlated features)
│   │   └── Yan+2020 (fair class balancing)
│   ├── Leaf 2.2: DRO-based methods
│   │   ├── Hashimoto+2018 (DRO for worst-group utility)
│   │   ├── Lahoti+2020 (ARL: adversarial reweighting)
│   │   └── Jung+2023 (DRO + fairness constraints)
│   ├── Leaf 2.3: Knowledge distillation / VAE-based
│   │   ├── Chai+2022 (knowledge distillation for fairness)
│   │   ├── Chai&Wang 2022 (contrastive learning)
│   │   └── Grari+2022 (causal VAE)
│   └── Leaf 2.4: This paper — Reckoner
│       (confidence-based split + learnable noise + dual VAE)
│       ⚠ Novelty position vs Grari+2022 (causal VAE) and 
│         Chai+2022 (distillation) needs manual verification
│
└── Branch 3: Weak Proxy Estimation
    └── Leaf 3.1: Zhu+2023 (weak proxy calibration)
```