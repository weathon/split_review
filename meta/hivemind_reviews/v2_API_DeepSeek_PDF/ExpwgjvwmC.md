## Summary
# Final Review Report

## Summary

This paper introduces OMNIINPUT, a model-centric evaluation framework that uses output-distribution sampling (via the Gradient Wang-Landau algorithm) to construct representative inputs from a trained model, then estimates precision and recall across all output thresholds through selective human annotation. The core idea — using the output distribution as a bridge between sparse annotations and the full input space — is conceptually interesting and addresses a real gap in model evaluation.

The paper demonstrates OMNIINPUT on binary MNIST classification, revealing precision-recall differences between models with near-identical held-out accuracy that standard data-centric AUPR rankings cannot distinguish. It also reports qualitative findings about how different architectures (CNN vs. MLP) learn different classification criteria, and how training with noise augmentation affects output-space behavior. Additional experiments on CIFAR-10 and SST2 sentiment classification using DistilBERT extend the demonstration to other modalities.

However, the paper has several significant weaknesses that limit its current impact. (1) The uniform-prior assumption over the entire input space is philosophically and operationally problematic — the vast majority of inputs are noise, and weighting them equally with meaningful inputs may produce evaluation results that have little relation to practical model quality. (2) The precision/recall definitions use continuous human scores rather than binary labels, producing metrics that are not directly comparable to standard definitions. (3) Scalability is deferred entirely to future samplers, with the CIFAR-10 experiment producing a near-zero precision result that may be an artifact of the uniform prior rather than a meaningful diagnosis. (4) The novelty claim about being "first to leverage the output distribution" is not adequately distinguished from the prior GWL work that introduced output-distribution sampling for neural networks. (5) Related work is presented as a flat reference list rather than a structured comparison.

The paper presents an interesting proof-of-concept on a toy problem (28×28 grayscale binary MNIST), but the path to practical deployment on realistic-scale problems is unclear. The strengths lie in the conceptual framework and the qualitative insights from representative input inspection. With substantial revision to address the foundational assumptions, metric definitions, scalability analysis, and claim bounding, the paper could become a more solid contribution to the evaluation methodology literature.

## Strengths
**S1 — Novel conceptual framing.** The idea of using the output distribution (the frequency of each logit value over the entire input space) as the foundation for discriminative model evaluation is genuinely creative. It reframes evaluation from "how does the model perform on this test set?" to "how does the model partition the input space across output values?" This shift in perspective could be valuable for understanding model behavior in open-world settings.

**S2 — Addresses a real limitation of data-centric evaluation.** The paper correctly identifies that models with nearly identical held-out accuracy can have qualitatively different behavior over the broader input space. Table 1 convincingly shows that AUPR rankings depend heavily on which OOD dataset is used as the negative set, making data-centric rankings inconsistent. OMNIINPUT's ability to produce a single precision-recall curve over the entire input space is a principled response to this inconsistency.

**S3 — Useful qualitative insights from representative inputs.** The analysis of representative inputs (Appendix D) revealing that CNN classifiers associate "digit 1" with dark-background patterns while MLP classifiers associate it with inverted-digit patterns is an interesting finding. While causal interpretations need more support, these observations demonstrate that OMNIINPUT can generate hypotheses about model behavior that go beyond what test-set metrics provide.

**S4 — Human annotation effort is modest.** Figure 4 shows that the precision-recall curve converges with roughly 40-50 annotations per bin, which is a practical annotation budget. The paper correctly notes that this is far less than annotating a full test set like MNIST (60,000 samples).

**S5 — Honest limitation disclosure in the Introduction.** The paper explicitly states (Page 2) that the findings are "specific to the models we trained" and that this is "not a conclusive study" but a demonstration. This transparency is commendable and should be preserved.

## Weaknesses
**W1 — Unsupported "first to leverage output distribution" claim (Major).** The paper claims (Page 2) to be "the first to leverage the output distribution as a unique quantity to generalize model evaluation." This claim is not adequately distinguished from the GWL sampler (Liu et al., 2023), which already introduced output-distribution sampling for neural networks. The novelty of OMNIINPUT lies in using the output distribution for *precision-recall estimation*, not in leveraging the output distribution per se. The wording should be revised to make the specific contribution clear.

**W2 — Uniform-prior assumption is not adequately defended (Major).** The assumption that all inputs in $\Omega = \{0,\ldots,N\}^D$ are equally important (Page 3, Section 2.1) is presented as a principle but has severe consequences: the evaluation is dominated by noise inputs that constitute >99.999% of the space. The paper does not discuss alternative reference measures (e.g., weighting by distance to training data) or provide an argument that uniform-prior evaluation correlates with practical model quality. This is a foundational issue that affects the interpretation of all experimental results.

**W3 — Precision/recall definitions are non-standard (Major).** The paper defines $r(z)$ as the average continuous human score (0 to 1) per bin, then treats $\sum r(z)\rho(z)$ as the "true positive" count. This only matches standard precision if scores are binary. Using continuous scores as TP counts biases the precision upward — a sample rated 0.3 contributes partially to "positive" even though a human considered it mostly negative. The metrics should be renamed (e.g., "soft precision") or binarized with a threshold sensitivity analysis (Page 4, Section 2.2).

**W4 — Scalability is not demonstrated (Major).** The paper acknowledges that scaling requires more efficient samplers (Page 5, "Scalability" paragraph) and defers this to future work. The CIFAR-10 experiment (Page 7) produces near-zero precision — effectively a negative result that may reflect the uniform-prior artifact in high-dimensional spaces rather than a meaningful model diagnosis. Without demonstrating usefulness on at least one moderately scaled problem, the framework's value remains a proof-of-concept on toy problems.

**W5 — FID comparison is technically flawed (Major).** Table 2 compares FID scores between RES-AUG-MNIST-0/1 (logits 40-43) and CNN-MNIST-0/1 (logits 9-12) — models with completely different output ranges. The conclusion that FID is "completely misleading" conflates the fact that FID correctly measures distance to MNIST digit-1 features for both sets (which are far from digit-1 features for different reasons). The analysis does not control for logit range or provide a meaningful comparison protocol (Page 8, Section 5).

**W6 — Related work is unstructured (Minor).** The "Performance Characterization" subsection (Page 9) is a flat list of ~15 references without grouping by approach family. The paper does not provide a structured comparison with the most relevant baselines: generative precision-recall frameworks (Sajjadi et al., 2018; Naeem et al., 2020; Cheema & Urner, 2023) and test-set-free diagnosis methods (Qiu et al., 2020; Lang et al., 2021; Luo et al., 2023; Prabhu et al., 2023).

**W7 — Contribution list is imprecise (Minor).** The three-bullet contribution list (Page 3) mixes a philosophical stance (C1), a framework description (C2), and application results (C3). A crisper separation into methodological innovation versus empirical demonstration would strengthen the paper.

**W8 — Conclusion does not bound findings (Minor).** The Conclusion (Page 9) focuses almost entirely on future sampler requirements without summarizing what was actually validated. The claim about automatic scalability is speculative. Missing limitations include the uniform-prior assumption and human annotation quality dependency.

## Key Issues
### Issue 1: Foundational assumption of uniform prior over the input space (W2)
**Severity:** Major | **Risk:** Invalidity of the evaluation framework's core premise

The uniform-prior assumption ($p(x) = \text{uniform over } \Omega$) is presented as a principle but has not been validated as a useful basis for evaluation. In a $28 \times 28$ grayscale input space with $256^{784}$ possibilities, the vast majority of inputs are meaningless noise. Weighting these equally with digit-like images means the precision-recall curve is dominated by the model's behavior on noise. The paper does not address whether a model that performs well under this metric also performs well in practical deployment scenarios. A sensitivity analysis with alternative reference measures (e.g., weighting by distance to training distribution) is needed.

**Fix path (Must):** (a) Explicitly characterize the uniform prior as a *design choice* rather than a universal principle. (b) Add a discussion of alternative measures and show that key results are robust or explain differences. (c) Provide at least one experiment with a non-uniform reference measure (e.g., sampling from a neighborhood around the training distribution).

### Issue 2: Non-standard precision/recall definitions (W3)
**Severity:** Major | **Risk:** Reproducibility and comparability

The use of continuous human scores (0-1) as if they were binary true/false counts in the precision formula is metric-mismatched. Define $\text{precision}_\lambda = \frac{\sum_{z\geq\lambda} r(z)\rho(z)}{\sum_{z\geq\lambda} \rho(z)}$ where $r(z) \in [0,1]$. If $r(z) = 0.3$ for a bin, it contributes 0.3 "true positives" even though 70% of samples are considered non-positive by the human annotator. This inflates precision relative to standard definitions and makes OMNIINPUT's metrics not directly comparable with any literature baselines.

**Fix path (Must):** (a) Binarize human scores with an explicit threshold (e.g., $\tau = 0.5$) and report both hard and soft precision. (b) Provide a sensitivity analysis over $\tau \in \{0.3, 0.5, 0.7\}$. (c) Rename the metric to "soft precision" when using continuous scores.

### Issue 3: Scalability not demonstrated (W4)
**Severity:** Major | **Risk:** Research value limited to toy problems

The framework is demonstrated only on $28 \times 28$ MNIST and 66-token SST2 — both very low-dimensional input spaces. The CIFAR-10 experiment produces a trivial result (near-zero precision). The paper defers scaling to "future samplers" without analyzing the practical barriers (sampler convergence, bin count explosion, annotation budget). Without a concrete path to scaling, the contribution remains a proof-of-concept.

**Fix path (Must):** (a) Provide a theoretical analysis of computational complexity as a function of $D$ (input dimension), $B$ (number of bins), and $N$ (samples per bin). (b) Add a controlled downsampling experiment (e.g., CIFAR-10 at $8 \times 8$, $16 \times 16$, $32 \times 32$) to show how precision discrimination degrades with dimensionality. (c) Be explicit about the current practical upper bound.

### Issue 4: Unsubstantiated "first" claim (W1)
**Severity:** Major | **Risk:** Novelty perception

The claim of being "first to leverage the output distribution" is not adequately bounded against prior work [Liu et al., 2023] which introduced output-distribution sampling for neural networks.

**Fix path (Must):** Replace with a bounded novelty statement: "This is the first framework to use the output distribution — already estimable via GWL — as the backbone for computing precision-recall curves for discriminative models via selective annotation."

### Issue 5: CIFAR-10 near-zero precision interpretation (W4 extension)
**Severity:** Major | **Risk:** Misleading conclusions about model quality

The near-zero precision on CIFAR-10 (Page 7) is presented as evidence of overconfident prediction. However, it may equally reflect that the uniform prior in a $32 \times 32 \times 3$ space makes informative samples astronomically rare, so *any* model would show near-zero precision — including a perfectly calibrated one.

**Fix path (Must):** (a) Add sampler convergence diagnostics for the CIFAR-10 experiment. (b) Provide a controlled comparison: compute OMNIINPUT precision for a deliberately broken model (e.g., random labels) vs. the trained model to verify that the metric can distinguish them. (c) If both show near-zero precision, acknowledge that the metric lacks discriminative power at this scale.

## Actionable Suggestions
### Suggestion 1: Revise the uniform-prior assumption (Must — Publication-critical)
**Problem:** Section 2.1 presents the uniform-prior assumption without justification or alternatives.
**Fix:** Replace the current phrasing with an explicit design-choice characterization:

*Mentor Revised Version (for Section 2.1, Page 3):*
"We adopt the uniform distribution over $\Omega = \{0,\dots,N\}^D$ as the reference measure for evaluation. This choice is motivated by two practical considerations: (a) it provides a reproducible, normalization-independent basis for comparing models, since the total number of inputs $(N+1)^D$ is identical across all models; and (b) it aligns with the sampling mechanism of Wang-Landau algorithms, which are designed to produce a uniform histogram over the output space. We note that this uniform measure assigns equal weight to every input, including the vast majority that are semantically meaningless noise. While alternative measures (e.g., weighting by distance to training data or by a reference prior) are possible, the uniform prior provides a model-agnostic baseline. We provide a sensitivity analysis with alternative measures in Appendix G."

### Suggestion 2: Binarize the precision/recall definition (Must — Publication-critical)
**Problem:** The precision formula uses continuous human scores as TP counts.
**Fix:** Add a binarization step and report both soft and hard metrics.

*Mentor Revised Version (for Section 2.2, Page 4):*
"We define the per-bin precision $r(z)$ as the proportion of samples in bin $z$ whose human-assigned score exceeds a threshold $\tau$ (we set $\tau=0.5$ by default). Then:
$$\text{precision}_\lambda = \frac{\sum_{z \ge \lambda} r(z)\rho(z)}{\sum_{z \ge \lambda} \rho(z)}$$
where $r(z)\rho(z)$ equals the number of positively-rated samples in bin $z$ (under the binary threshold). We provide a sensitivity analysis over $\tau \in \{0.3, 0.5, 0.7\}$ in Appendix G. For completeness, we also report 'soft precision' using raw continuous scores."

### Suggestion 3: Down-scope the novelty claims (Must — Publication-critical)
**Problem:** The "first to leverage output distribution" claim is not adequately bounded.
**Fix:** Replace the sentence in the Introduction (Page 2, lines 7-9).

*Mentor Revised Version:*
"While existing generative model evaluation frameworks also adopt a model-centric perspective, OMNIINPUT is distinguished by using the output distribution — already estimable via methods such as GWL — as the carrier for aggregating per-bin human annotations into precision-recall curves for discriminative models. This contrasts with generative metrics (FID, IS, Precision-Recall Cover) that compare feature distributions via pre-trained feature extractors."

### Suggestion 4: Restructure Related Work into comparison axes (Nice-to-have — Quality improvement)
Restructure "Performance Characterization" (Page 9) into three themed paragraphs with sub-headings: (a) Black-box performance characterization, (b) Generative model evaluation metrics, (c) Test-set-free model diagnosis. For each, explicitly state the difference from OMNIINPUT.

### Suggestion 5: Revise the CIFAR-10 analysis (Must — Experiment robustness)
Add sampler convergence diagnostics, a controlled experiment with a deliberately broken model (random labels), and a downsampled-resolution analysis. If near-zero precision persists across all conditions, acknowledge this as a limitation of the uniform-prior measure in high-dimensional spaces rather than a meaningful model diagnosis.

### Suggestion 6: Add an alternative-reference-measure sensitivity experiment (Nice-to-have — Research value)
Run OMNIINPUT with a truncated reference measure that samples only from a neighborhood of the training distribution (e.g., $\ell_\infty$ ball of radius $\epsilon$ around training samples). Compare the resulting precision-recall curves with the uniform-prior results to assess the impact of the reference measure.

### Suggestion 7: Strengthen the Conclusion (Must — Publication-critical)
Restructure the Conclusion into three parts: (a) validated findings (what OMNIINPUT demonstrated empirically), (b) bounded limitations (uniform prior, scaling, annotation quality), (c) prioritized future work. Remove the unsupported claim about automatic scalability.

### Suggestion 8: Add annotation inter-rater reliability statistics (Nice-to-have — Quality improvement)
The paper shows that different annotators produce different $r(z)$ values (Figure 3). Report a quantitative inter-rater reliability metric (e.g., Fleiss' kappa or ICC) and discuss how annotation ambiguity affects precision estimates.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction (Pages 1-2) follows this structure:
- P1: Safety motivation (backdoor attack example) + limitation of data-centric evaluation
- P2: Model-centric approach inspired by generative evaluation + four-step illustration
- P3: Fine-grained comparison claim + bullet-point insights
- P4: Additional experiments (DistilBERT, CIFAR) + caveat + contribution list

**Problem:** The backdoor attack example (P1) is too specific and does not justify the uniform-prior framework. The four-step illustration (P2) dives into technical details before the reader understands the core idea. The contribution list (P4) mixes philosophical claims with technical contributions.

### Proposed Storyline: "Evaluation Gap → Output Distribution Solution → Validation"
This storyline makes a cleaner narrative arc and aligns with the three alignment checks.

**Alignment Check:**
- (a) Problem alignment: YES — "data-centric evaluation cannot assess full input space behavior" directly motivates "we use output distribution to sample the full space."
- (b) Variable alignment: YES — "output distribution," "representative inputs," "precision per bin" all reappear as key objects in Section 2.
- (c) Contribution-evidence alignment: YES — "different models with same accuracy have different PR curves" is directly supported by Figure 2 and Table 1.

---

### Abstract Outline (Complete)
**S1 (Problem):** "Standard data-centric evaluation assesses model performance on pre-defined test sets, but cannot characterize behavior over the full input space — including out-of-distribution and adversarial inputs that arise in deployment."

**S2 (Gap):** "Existing model-centric evaluation metrics (e.g., FID, IS) require a separate generative model or feature extractor, and their applicability to discriminative models is unvalidated."

**S3 (Method):** "We propose OMNIINPUT, which uses an efficient Wang-Landau sampler to estimate the model's output distribution over the entire input space, then constructs representative inputs from each output bin, and estimates precision and recall via selective human annotation."

**S4 (Key Result):** "On binary MNIST classification, OMNIINPUT reveals precision-recall differences between models with near-identical held-out accuracy — a capability that data-centric AUPR rankings cannot provide. The framework also detects systematic overconfident predictions in CNN classifiers."

**S5 (Bounded Implication):** "OMNIINPUT provides a complementary tool for fine-grained model comparison and safety auditing, though scaling to larger input spaces requires more efficient samplers."

---

### Introduction Outline (Complete)

**P1 — Motivation and Gap (purpose: establish stakes)**
Role: Define the evaluation blind spot. 
Claim: Data-centric test sets cover only a tiny fraction of the input manifold; two models with identical test accuracy can have vastly different behavior on unseen inputs.
Evidence: Cite OOD detection and adversarial robustness literature.
Transition: "To address this blind spot, we argue that evaluation should consider the entire input space."

**P2 — Core Idea (purpose: introduce the solution at a high level)**
Role: Present the output distribution as the key enabler.
Claim: The output distribution — the frequency of each logit value over all inputs — provides a principled way to move from representative samples to full-space metrics.
Evidence: Reference WL sampling (Wang & Landau, 2001) and GWL (Liu et al., 2023) as the technical foundation.
Transition: "In this paper, we operationalize this idea through the OMNIINPUT framework."

**P3 — Framework Overview (purpose: give the reader a mental model before details)**
Role: Briefly describe the four steps (sample output distribution → annotate representative inputs → compute per-bin precision → construct PR curve) without deep technicalities.
Transition: "We illustrate this framework on binary MNIST classification."

**P4 — Empirical Preview + Contribution Summary (purpose: seed anticipation and state contribution)**
Role: State that OMNIINPUT reveals differences invisible to data-centric evaluation, list key findings, and present a crisp two-contribution list.
Transition to Section 2: "In the following section, we describe the framework in detail."

---

### Title Recommendation
Current: "OMNIINPUT: A Model-Centric Evaluation Framework Through Output Distribution"
Better: "OMNIINPUT: Evaluating AI Models over the Full Input Space via Output-Distribution Sampling"
Reason: The revised title explicitly states the problem (evaluating over the full input space) and method (output-distribution sampling), making it more informative to readers.

## Priority Revision Plan
### Overview
The revision plan is organized by priority (P0 = immediate, P1 = before next submission, P2 = ongoing improvement). Each item maps to specific sections and annotations.

```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Foundational Fixes]
  ├── Revise uniform-prior assumption (Section 2.1/Page 3)
  │   -> From principle to design choice + sensitivity plan
  │   -> Expected: removes foundational validity risk
  ├── Binarize precision/recall definitions (Section 2.2/Page 4)
  │   -> Add threshold + sensitivity analysis
  │   -> Expected: metrics become standard-comparable
  └── Down-scope novelty claims (Page 2, Introduction)
      -> Replace "first" with bounded claim
      -> Expected: novelty defense becomes credible
          
[P1: Experiment & Analysis]
  ├── CIFAR-10: add convergence diagnostics + random-label control
  ├── CIFAR-10: downsampled-resolution analysis (8×8, 16×16, 32×32)
  ├── MNIST: add threshold-sensitivity analysis (tau=0.3/0.5/0.7)
  └── MNIST: add alternative reference-measure experiment
      -> Expected: demonstrates metric robustness or reveals limitations

[P2: Writing & Structure]
  ├── Restructure Related Work (Section 6/Page 9)
  ├── Strengthen Conclusion (Section 7/Page 9)
  ├── Rewrite Introduction narrative (Pages 1-2)
  └── Revise FID analysis (Section 5/Page 8)
      -> Expected: paper becomes better positioned and more readable
```

### Detailed Priority Table

| Priority | Item | Issue Reference | Effort | Impact | Section Affected |
|----------|------|-----------------|--------|--------|------------------|
| **P0** | Revise uniform-prior assumption | W2, Issue 1 | Low (text edit) | High (foundational validity) | Section 2.1, Page 3 |
| **P0** | Binarize precision/recall | W3, Issue 2 | Low (text edit + re-analysis) | High (metric comparability) | Section 2.2, Page 4 |
| **P0** | Down-scope novelty claim | W1, Issue 4 | Low (text edit) | High (novelty perception) | Introduction, Page 2 |
| **P0** | Restructure Conclusion | W8 | Low (text edit) | Medium (paper closure) | Section 7, Page 9 |
| **P1** | CIFAR-10 convergence diag. + controls | W4, Issue 3, Issue 5 | Medium (experiment run) | High (scalability evidence) | Section 4, Page 7 |
| **P1** | CIFAR-10 downsampled analysis | W4, Issue 3 | Medium (experiment run) | Medium (scalability insight) | Section 4, Page 7 |
| **P1** | Threshold sensitivity analysis | W3, Issue 2 | Low (re-analysis of existing data) | Medium (metric robustness) | Section 2.2/Appendix |
| **P1** | Alternative reference measure exp. | W2, Issue 1 | Medium (new sampling) | High (assumption validation) | New appendix section |
| **P2** | Restructure Related Work | W6 | Low (text edit) | Medium (positioning) | Section 6, Page 9 |
| **P2** | Rewrite Introduction narrative | — | Medium (text edit) | Medium (readability) | Section 1, Pages 1-2 |
| **P2** | Fix FID comparison analysis | W5, Issue 5 | Low (text edit) | Low (secondary claim) | Section 5, Page 8 |

### Expected Outcome After All P0 Fixes
With P0 fixes (uniform-prior reframing, metric binarization, bounded novelty), the paper becomes defensible as a proof-of-concept methodology paper on toy problems. The remaining P1/P2 items would substantially strengthen the paper toward acceptance at a venue like ICLR or NeurIPS.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Compare models via data-centric AUPR | MNIST-0/1, 5 OOD test sets (Fashion, Kuzushiji, EMNIST, Q-MNIST) | AUPR | Rankings inconsistent across OOD sets | S1 (data-centric limitation) | Only binary MNIST; results may differ for multi-class |
| E2 | Compare models via OMNIINPUT PR curves | MNIST-0/1, 7 models (CNN, MLP, ResNet variants) | Full PR curve (Fig. 2) | RES-AUG best; CNN near-zero precision | C2 (framework capability) | Continuous scores used; PR curve not threshold-binarized |
| E3 | Inspect representative inputs | MNIST-0/1, all 7 models | Qualitative analysis (App. D) | Different models prefer different pattern types | C2 (qualitative insights) | No quantitative feature analysis |
| E4 | Human annotation convergence | MLP-MNIST-0/1, 10-50 samples/bin | PR curve convergence | Converges at 40-50 samples/bin | C2 (annotation efficiency) | Only tested on one model |
| E5 | Inter-annotator agreement | 3 annotators on same dataset | r(z) variance (Fig. 3) | Varying ambiguity across models | Robustness check | No quantitative reliability metric (ICC/kappa) |
| E6 | CIFAR-10 binary evaluation | ResNet, airplane vs automobile | PR curve | Near-zero precision | Framework demonstration | Negative result; no controls for dimensionality artifact |
| E7 | Sampler comparison | CIFAR-10, GWL vs Langevin sampler | Representative input agreement | Samplers produce similar samples | Sampler robustness | Qualitative comparison only |
| E8 | SST2 sentiment evaluation | DistilBERT, SST2 (len=10, 66) | Qualitative analysis | Model relies on keywords, not grammar | Framework demonstration | Very small bins (15); no quantitative precision |
| E9 | FID vs human comparison | RES-AUG vs CNN on select logit bins | Human score + FID (Table 2) | FID scores similar despite semantic difference | Model annotation critique | Logit ranges not matched between models |

### Research-Theme Gap Diagnosis

**Gap 1: Metric validity.** The core evaluation metrics (precision, recall) use non-standard definitions (continuous scores instead of binary thresholds). This means all E2 results need re-analysis under binarized definitions.

**Gap 2: Assumption validation.** The uniform-prior assumption (used in all experiments) is not validated against alternative reference measures. Any of the E2/E6/E8 results could change under a different measure.

**Gap 3: Scalability evidence.** Only low-dimensional experiments (E1-E5, E8) produce non-trivial results. The single higher-dimensional experiment (E6) produces a trivial result. The framework's practical utility remains unvalidated.

**Gap 4: Causal interpretation.** The qualitative insights from E3 are presented with causal language (e.g., "the model does not use shapes") but lack quantitative attribution analysis. The representative input inspection alone cannot establish what features the model uses.

### Proposed Research Experiments (P0/P1/P2)

**Experiment P0-A: Precision-recall binarization re-analysis**
- **Target Claim:** C2 (framework capability)
- **Hypothesis:** Binarizing human scores with τ=0.5 produces qualitatively similar PR rankings to the current continuous-score method.
- **Minimal Design:** Re-compute Fig. 2 using binary r(z) (score ≥0.5 = positive, else negative).
- **Controls:** Compare with τ=0.3 and τ=0.7.
- **Metrics:** Rank-order correlation of model PR curves across thresholds.
- **Success Criterion:** At least 3 of 4 top-ranked models remain in the same order.
- **Estimated Cost:** Low (re-analysis of existing annotation data).
- **Expected Gain:** Validates or challenges metric robustness; directly addresses Issue 2.

**Experiment P0-B: Alternative reference measure on MNIST**
- **Target Claim:** C1 (framework principle)
- **Hypothesis:** An evaluation measure that truncates the input space to a neighborhood of the training data produces different PR curves than the uniform prior.
- **Minimal Design:** Restrict the input space to $\ell_\infty$ balls of radius $\epsilon$ around MNIST training samples; run GWL sampler within this restricted space.
- **Controls:** Compare uniform-prior PR curves with truncated-space PR curves for the same models.
- **Metrics:** Spearman rank correlation of model rankings between the two measures.
- **Success Criterion:** Either high correlation (measure is robust) or low correlation with explanation of differences.
- **Estimated Cost:** Medium (new sampling runs).
- **Expected Gain:** Addresses Issue 1 by validating or bounding the uniform-prior assumption.

**Experiment P1-A: CIFAR-10 controlled diagnostics**
- **Target Claim:** C2 (scalability)
- **Hypothesis:** The near-zero precision on CIFAR-10 is partly an artifact of the uniform-prior measure in high dimensions, not purely a model defect.
- **Minimal Design:** (a) Run OMNIINPUT on a model trained with random labels (should show near-zero precision if metric works). (b) Run OMNIINPUT on the same model at downsampled resolutions: 8×8, 16×16, 32×32.
- **Controls:** Compare with the existing 32×32 result.
- **Metrics:** Precision at recall=0.5 for each resolution and condition.
- **Success Criterion:** Precision improves at lower resolutions, and the random-label model shows lower precision than the trained model.
- **Estimated Cost:** Medium (sampling at multiple resolutions).
- **Expected Gain:** Provides the first evidence (positive or negative) on how OMNIINPUT scales.

**Experiment P1-B: Feature-attribution analysis for representative inputs**
- **Target Claim:** Qualitative insights (E3)
- **Hypothesis:** Representative inputs with high logits have systematically different saliency patterns across CNN and MLP architectures.
- **Minimal Design:** Compute Grad-CAM or Integrated Gradients for representative inputs of CNN-MNIST-0/1 and MLP-MNIST-0/1.
- **Controls:** Compare with saliency maps on standard test-set samples.
- **Metrics:** Proportion of attribution weight on foreground vs. background pixels.
- **Success Criterion:** Statistically significant difference in foreground/background attribution between architectures.
- **Estimated Cost:** Low (existing models can be probed).
- **Expected Gain:** Transforms qualitative insights into quantitative, reproducible findings.

**Experiment P2-A: Synthetic controlled baseline**
- **Target Claim:** C2 (framework validity)
- **Hypothesis:** On a synthetic binary classification problem (e.g., Gaussian blobs in 2D), the OMNIINPUT precision-recall curve matches the analytically computed ground-truth precision-recall curve.
- **Minimal Design:** Create a 2D binary classification problem where the true data distribution is known; train a small neural network; compute OMNIINPUT PR curve; compare with analytically computed PR curve.
- **Success Criterion:** Mean absolute error < 0.05 between OMNIINPUT and ground-truth PR curves.
- **Estimated Cost:** Low (synthetic data, small model).
- **Expected Gain:** Provides a ground-truth validation of the framework's estimation procedure.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (this week): Re-analysis & Text Fixes
  ├── P0-A: Binarization sensitivity (re-use existing annotations)
  ├── P0-B: Restrict-space OMNIINPUT on MNIST (new sampling)
  └── P0-C: Add random-label control for CIFAR-10 (new sampling)

P1 (before next submission): Controlled Experiments
  ├── P1-A: CIFAR-10 multi-resolution + convergence diagnostics
  ├── P1-B: Feature-attribution for representative inputs
  └── P1-C: Synthetic ground-truth validation (2D Gaussian)

P2 (after acceptance): Extensions
  ├── P2-A: Alternative reference measures (beyond uniform)
  ├── P2-B: Inter-annotator reliability (kappa/ICC)
  └── P2-C: Multi-class extension
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

The paper has a conceptually interesting core idea (using output-distribution sampling for discriminative model evaluation) and demonstrates some useful qualitative insights on binary MNIST. However, it has several foundational weaknesses that prevent a higher score: the uniform-prior assumption is not adequately defended, the precision/recall definitions are non-standard, scalability is not demonstrated on realistic-scale problems, and the CIFAR-10 experiment produces a trivial result. The novelty claim about being "first to leverage the output distribution" is not adequately bounded against the prior GWL work. The paper reads as a promising proof-of-concept on a toy problem, but the path to practical applicability is unclear.

**Score breakdown (evidence-grounded):**
- **Research value (primary dimension): 5/10** — The conceptual framework is interesting, but the practical utility is unvalidated beyond 28×28 MNIST. The CIFAR-10 result (near-zero precision) raises questions about whether the framework produces meaningful evaluations at realistic scales.
- **Novelty (primary dimension): 5/10** — The core idea of output-distribution-based evaluation has merit, but the paper does not clearly separate what is inherited from GWL versus what is newly contributed. The "first" claim is overclaimed.
- **Validity/Soundness: 5/10** — The uniform-prior assumption and the non-standard metric definitions introduce validity concerns. The FID comparison is technically flawed.
- **Reproducibility: 6/10** — The method description is adequate for the MNIST experiments, but the sampling procedure depends on GWL convergence, which is not always verifiable from the text.
- **Presentation/Clarity: 5/10** — The abstract and introduction need restructuring. The related work section is a flat list. The conclusion does not bound findings.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors complete all P0 fixes (revise uniform-prior framing, binarize metrics, down-scope novelty claims, restructure conclusion) and at least P1-A (CIFAR-10 diagnostics with multi-resolution analysis + random-label control), the score could rise to 6.5-7.5. The paper would then be a solid methodology paper with clear scope boundaries and validated metric definitions, though the scalability limitation would remain a ceiling on research value until larger-scale demonstrations are provided.