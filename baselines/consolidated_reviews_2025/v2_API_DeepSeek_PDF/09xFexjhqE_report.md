## Summary
# Final Review Report

## Summary

This paper tackles the problem of robust fine-tuning (RFT) for pre-trained feature extractors. The authors identify that existing RFT methods (vanilla RFT and TWINS) suffer from divergent gradient directions when jointly optimizing natural and adversarial objectives through the same feature extractor. To address this, they propose AutoLoRa, which disentangles the optimization by routing natural objectives through a low-rank (LoRa) branch and adversarial objectives through the feature extractor. Additionally, they introduce heuristic automated schedulers for the learning rate and loss-term scalars.

The paper is published at ICLR 2024 and presents experiments on six downstream image classification datasets using tasks with ResNet-18, ResNet-50, and Vision Transformer backbones. The results show consistent improvements in robust accuracy (PGD-10 and AutoAttack) over two baselines (vanilla RFT and TWINS), with gains of up to +3.03% on DOG-120 with ResNet-50. Statistical significance is validated through t-tests.

**Core contributions (C1-C3):**
- **C1**: Empirical identification of divergent gradient directions in existing RFT methods.
- **C2**: Disentangled RFT via a LoRa branch separating natural and adversarial optimization.
- **C3**: Heuristic automated scheduling of learning rate and loss scalars (λ1, λ2).

**Novelty verdict: Deferred.** External literature verification was unavailable in this run (Retrieval-Disabled Mode). The core technical idea — using a low-rank branch to separate optimization bypass to separate conflicting objectives — is a reasonable contribution to the RFT literature, but the extent of overlap with existing methods (e.g., other forms of parameter-efficient adversarial fine-tuning, dual-optimizer approaches) requires manual verification.

## Strengths
1. **Clear problem diagnosis.** The paper identifies a concrete and well-motivated issue — divergent gradient directions in multi-objective RFT — and provides empirical evidence (gradient similarity plots in Figures 1a and 2a) to support the diagnosis. The visualization of cosine similarity between natural and adversarial gradients is informative and gives readers immediate insight into the optimization conflict.

2. **Simple and elegant solution.** The proposed disentanglement via a LoRa branch is conceptually clean: natural objectives update the LoRa branch, adversarial objectives update the FE. This architectural separation directly addresses the diagnosed issue without requiring complex training schedules or multi-stage optimization. The use of LoRA (parameter-efficient fine-tuning) ensures the overhead remains modest (<5% extra parameters) and does not affect inference latency.

3. **Comprehensive empirical evaluation.** The experiments cover 6 diverse downstream datasets (low-resolution CIFAR-10/100, high-resolution DTD-57/DOG-120/CUB-200/Caltech-256), two backbone architectures (ResNet-18, ResNet-50), Vision Transformers (ViT, DeiT), and multiple pre-training budgets. Statistical significance is validated via t-tests with 3 random seeds. The ablation studies explore rank sensitivity, pre-training budget effects, and scheduler components.

4. **Practical automation value.** The automated LR scheduler and graduated-optimization-inspired λ1/λ2 scheduler reduce the need for per-task hyperparameter search, which is a meaningful practical contribution given that TWINS required extensive grid search for each dataset.

## Weaknesses
1. **Causal overclaim without causal evidence.** The paper asserts that divergent gradient directions *cause* poor robustness, and that resolving this divergence *causes* gains. However, the evidence is correlational (low gradient similarity → low robust accuracy), and the proposed method introduces multiple confounding factors (extra LoRa parameters, KL distillation, changed optimization landscape) that are not isolated. The robustness gains could equally be explained by increased model capacity or regularization from the low-rank constraint.

2. **Insufficient baseline comparisons.** Only two baselines are compared (vanilla RFT and TWINS). Standard adversarial training, other robust fine-tuning variants, and alternative parameter-efficient approaches are omitted. Claiming "state-of-the-art" with only two comparators is not justified.

3. **Evaluation bias from test-set checkpoint selection.** The best checkpoint is selected based on PGD-10 test accuracy rather than a held-out validation accuracy. This leaks test-set information into model selection and likely inflates the reported numbers, particularly problematic when gains are small (e.g., +0.03% PGD-10 on Caltech-256 with ResNet-50).

4. **Automation overclaim.** Despite claiming "no need for searching hyperparameters," the method still requires configuring λmax2, α, rank rnat, initial LR, checkpoint interval M, and the validation set proportion. These are hyperparameters that may need adjustment across tasks.

5. **Missing limitation discussion.** The conclusion provides no discussion of when or why AutoLoRa might underperform, what types of tasks it has not been validated on, or what computational overheads exist during training.

6. **Limited hyperparameter sensitivity evidence.** The sensitivity analysis (Appendix B.2) tests only the initial learning rate on one dataset (CIFAR-100), yet the paper makes broad claims about reduced hyperparameter sensitivity.

7. **Weak theoretical foundation for LR scheduler.** The analogy between adversarial attack step size scheduling and LR scheduling is insufficiently justified. The scheduler design (halving LR on validation plateau) is reasonable, but the claimed connection to AutoAttack is misleading.

8. **Cross-input KL distillation not clearly motivated.** The KL loss in Eq. 5 compares adversarial logits with natural soft labels from different inputs, which is not standard knowledge distillation. The paper does not analyze or justify this design choice.

## Key Issues
### Issue 1 (Critical): Causal claim for gradient divergence is unsubstantiated — confounding factors not addressed
**Location:** Page 1 - Abstract, Page 2 - Introduction (lines 56-62), Page 5 - Section 4.1
**Evidence:** The paper states "the issue of divergent optimization direction could prevent gaining adversarial robustness" and claims that disentanglement via LoRa "solves the issue." However, no experiment isolates gradient separation from other changes (extra capacity, regularization, distillation). The gradient similarity plots (Figures 1a, 2a, 3) show correlation, not robust accuracy confounds.
**Impact:** The core mechanistic claim of the paper may be incorrect. Gains could be driven by increased model capacity or the regularization effect of low-rank constraints rather than gradient separation.
**Fix:** Add ablation experiments isolating the gradient-separation mechanism from capacity and regularization confounds.

### Issue 2 (Major): SOTA claim overreach with only 2 baselines
**Location:** Page 1 - Abstract (lines 22-23), Page 3 - Introduction (lines 9-10)
**Evidence:** Experiments compare only vanilla RFT and TWINS. No comparison with standard adversarial training, other PEFT-based robust fine-tuning, or concurrent methods.
**Impact:** The SOTA claim is not empirically justified and may mislead readers about the method's standing in the field.
**Fix:** Replace "new state-of-the-art" with "outperforms vanilla RFT and TWINS." Expand baseline comparisons in revision.

### Issue 3 (Major): Test-set leakage in checkpoint selection
**Location:** Page 7 - Section 5 (lines 49-50)
**Evidence:** "We select the checkpoint that has the best PGD-10 test accuracy as the best checkpoint and report the performance."
**Impact:** Using the test set for both selection and evaluation violates standard practice and inflates reported numbers, especially problematic for small gains.
**Fix:** Use held-out validation set for checkpoint selection, or report last-epoch performance.

### Issue 4 (Major): Missing limitation discussion
**Location:** Page 9 - Conclusion
**Evidence:** The conclusion contains zero sentences discussing limitations, failure cases, or conditions where AutoLoRa may underperform.
**Impact:** Readers cannot make informed decisions about when to adopt the method. Scientific completeness is compromised.
**Fix:** Add a 2-3 sentence Limitations paragraph covering unvalidated modalities, remaining hyperparameters, and computational cost.

### Issue 5 (Major): Hyperparameter automation claim overstated
**Location:** Page 1 - Abstract (lines 24-26), Page 9 - Conclusion
**Evidence:** The method still requires configuring λmax2, α, rank rnat, initial LR, M (checkpoint interval), and validation set proportion.
**Impact:** Practitioners may expect a fully turnkey solution and be disappointed when tuning is still needed.
**Fix:** Acknowledge remaining hyperparameters explicitly. Provide guidance on setting defaults across tasks.

## Actionable Suggestions
### S1 (Must) — Add confounding-factor ablation experiments
Design three ablation variants to isolate the gradient-separation mechanism:
- **Ablation A (Separation only, no LoRa):** Freeze FE for natural data as in AutoLoRa, but use a separate copy of the classifier head (not a LoRa branch) for natural data. This tests whether gradient separation alone (without extra capacity) drives gains.
- **Ablation B (LoRa capacity, no separation):** Add the LoRa branch but allow gradients from both objectives to update the FE (remove the gradient stopping on natural data). This tests whether the extra LoRa parameters alone explain gains.
- **Ablation C (No KL distillation):** Remove the KL loss term from Eq. 5 and only use λ1·CE + (1-λ1)·CE. This tests the value of the distillation signal.
- **Expected outcome:** If gradient separation is the true mechanism, Ablation A should match AutoLoRa's performance; if capacity is the driver, Ablation B should match it.

### S2 (Must) — Fix checkpoint selection protocol
Replace test-set selection with validation-set selection:
- Use the 5% held-out validation set (already used for LR scheduling) for checkpoint selection.
- Report test-set performance of the best validation checkpoint.
- Add mean±std across seeds for all metrics in the main tables (not just p-values in appendix).

### S3 (Must) — Add limitation section
Insert a 2-3 sentence paragraph before the future work sentence:
- Acknowledge remaining hyperparameters (λmax2, α, rnat).
- Note that the method is only validated on image classification; other modalities (text, audio, LLM fine-tuning) remain open.
- State that the computational overhead of adversarial example generation during training is not reduced.

### S4 (Should) — Strengthen baseline comparisons
Expand the related work comparison to include:
- Standard adversarial training on downstream tasks (without pre-training).
- Other PEFT-based robust fine-tuning approaches (adapter-based, prefix-tuning variants).
- If space permits, add empirical comparison on at least one additional high-resolution dataset.

### S5 (Should) — Clarify the LR scheduler's motivation
Reframe the LR scheduler as a validation-plateau-based halving strategy rather than claiming inspiration from AutoAttack. The current analogy is weak and may distract readers from the practical value of the scheduler.

### S6 (Should) — Discuss the SA-robustness tradeoff
AutoLoRa consistently shows lower SA than TWINS (by 0.5-1.1%). Add a brief discussion acknowledging this tradeoff and explaining why the robustness improvement is worth the SA drop in safety-critical applications.

### S7 (Nice-to-have) — Report λ1/λ2 dynamics
Add a figure showing how λ1, λ2, and LoRa SA evolve over training epochs to demonstrate the graduated optimization behavior and verify that the adversarial objective receives non-negligible weight early enough.

### S8 (Nice-to-have) — Expand sensitivity analysis
Test hyperparameter sensitivity (initial LR, weight decay, batch size) on at least 2 datasets (e.g., CIFAR-100 and DTD-57) with 3 seeds each, and report mean±std.

## Storyline Options + Writing Outlines
### Abstract Outline (4-5 sentence plan)

**S1 (Problem & Domain):** "Robust fine-tuning (RFT) adapts pre-trained models to downstream tasks while maintaining adversarial robustness, but existing RFT methods suffer from a fundamental optimization conflict."

**S2 (Gap):** "We identify that jointly optimizing natural and adversarial objectives through the same feature extractor produces significantly divergent gradient directions, which destabilizes training and limits robustness gains."

**S3 (Proposed Solution):** "To resolve this, we propose AutoLoRa, which disentangles the optimization by routing natural objectives through a low-rank (LoRa) branch and adversarial objectives through the feature extractor, supplemented by automated learning rate and loss-weight schedulers."

**S4 (Key Results):** "Across six diverse image classification datasets with ResNet and Vision Transformer backbones, AutoLoRa consistently improves robust accuracy over vanilla RFT and TWINS, with gains of up to +3.03% under AutoAttack."

**S5 (Bounded Implication):** "AutoLoRa offers a practical, low-overhead approach to obtaining adversarial robustness in downstream tasks while reducing the burden of hyperparameter tuning."

### Introduction Outline (Paragraph-by-Paragraph Plan)

**Current Storyline Issues:** The current introduction (Page 1-3) jumps between foundation models, GPT-3, PEFT, adversarial attacks, and RFT without a clear narrative arc. The motivation for the LoRa branch is introduced abruptly.

**Proposed Storyline (Revised):**

**P1 — Establish stakes and motivation (1 paragraph):**
Role: Define the practical importance of robust fine-tuning.
Target claim: Pre-trained models need downstream robustness for safety-critical deployment.
Transition: "However, existing RFT methods face a subtle but critical optimization challenge."
Evidence anchor: Reference to Madry et al. (2018), Hendrycks et al. (2019).

**P2 — Identify the gap (1 paragraph):**
Role: Explain the gradient conflict problem clearly before proposing the solution.
Target claim: Joint optimization of natural and adversarial objectives through the FE leads to divergent gradients.
Transition: "This paper shows that the conflict arises not from the objectives themselves but from sharing the same optimization path."
Evidence anchor: Refer to Figure 1a (gradient similarity plot) and Table 6 (sensitivity to LR).

**P3 — Solution intuition (1 paragraph):**
Role: High-level explanation of the disentanglement idea before technical details.
Target claim: Separating the optimization paths via a LoRa branch eliminates the gradient conflict.
Transition: "Our key insight is that natural and adversarial objectives can pursue different parameter subspaces."
Evidence anchor: Refer to Figure 1c (right panel).

**P4 — Technical overview and contributions (1 paragraph):**
Role: Summarize the method components and state explicit contributions.
Target claim: AutoLoRa combines LoRa-based disentanglement with automated hyperparameter scheduling.
Transition: (none — this is the closing paragraph).
Evidence anchor: Reference to Algorithm 1 and experimental results preview.

**Three Alignment Checks for the Proposed Storyline:**
(a) Problem alignment: The gradient conflict problem directly motivates the need for optimization separation.
(b) Variable alignment: "LoRa branch," "gradient similarity," "FE," "λ1/λ2" appear as the key method variables.
(c) Contribution-evidence alignment: Each claimed contribution (gradient divergence identification, LoRa disentanglement, automated scheduling) has direct empirical support in the results section.

## Priority Revision Plan
### P0 Items (Publication-Critical — Must Fix Before Resubmission)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | Causal overclaim without confounding isolation | Add Ablation A/B/C (separation-only, capacity-only, no-distillation) | Establishes the true mechanism behind gains; fixes the paper's core scientific claim |
| P0.2 | Test-set leakage in checkpoint selection | Switch to validation-set-based selection; report mean±std | Restores evaluation integrity; prevents criticism of result inflation |
| P0.3 | Missing limitation discussion | Add 2-3 sentence Limitations paragraph to Conclusion | Shows scientific maturity; helps practitioners understand scope |

### P1 Items (High Priority — Should Fix)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | SOTA overclaim with only 2 baselines | Replace "SOTA" with "outperforms vanilla RFT and TWINS"; add at least 1-2 more baseline comparisons | Strengthens empirical rigor; avoids overclaim criticism |
| P1.2 | Automation overclaim | Explicitly list remaining configurable hyperparameters and provide default guidelines | Manages reader expectations accurately |
| P1.3 | Weak LR scheduler analogy | Reframe as plateau-detection scheduler; remove AutoAttack analogy | Improves scientific accuracy of motivation |

### P2 Items (Nice-to-Have — Quality Improvements)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Limited sensitivity analysis | Expand to 2+ datasets, test weight decay and batch size | Strengthens robustness claims |
| P2.2 | Missing λ1/λ2 dynamics | Add figure showing scheduler behavior over epochs | Improves transparency and reproducibility |
| P2.3 | Cross-input KL not justified | Add analysis/comparison with standard distillation baseline | Clarifies design rationale |
| P2.4 | SA-robustness tradeoff not discussed | Add one sentence acknowledging the slight SA drop | Completes the accuracy-robustness picture |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Core Problem: Causal overclaim without confounding isolation]
    |
    ├──> [Fix P0.1: Add Ablation A (separation only)]
    │       -> Isolates gradient-conflict mechanism
    ├──> [Fix P0.1: Add Ablation B (LoRa capacity only)]
    │       -> Checks if extra params drive gains
    └──> [Fix P0.1: Add Ablation C (no KL)]
            -> Checks distillation contribution
    |
    [Evaluation Integrity Issue: Test-set leakage]
    |
    ├──> [Fix P0.2: Validation-based checkpoint selection]
    │       -> Removes selection bias
    └──> [Fix P0.2: Report mean±std]
            -> Adds statistical context
    |
    [Scope/Claim Precision Issues]
    |
    ├──> [Fix P0.3: Add Limitations paragraph]
    ├──> [Fix P1.1: Replace SOTA claim]
    └──> [Fix P1.2: Acknowledge remaining hyperparameters]
    |
    [Expected Outcome after P0+P1 fixes]
    -> Scientifically defensible mechanism claim
    -> Fair and reproducible evaluation
    -> Realistic and bounded contribution claims
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Robustness benchmark (ResNet-18) | 6 datasets, PGD-10 attack, ϵ=8/255 | SA, PGD-10, AA | AutoLoRa > vanilla RFT and TWINS | C2 (LoRa disentanglement) | Only 2 baselines; test-set checkpoint selection |
| E2 | Robustness benchmark (ResNet-50) | Same as E1 with larger backbone | SA, PGD-10, AA | Consistent gains, smaller margins | C2 | Same limitations as E1 |
| E3 | Vision Transformer compatibility | CIFAR-10, ViT-S/16, ViT-B/16, DeiT-tiny, DeiT-small | SA, PGD-10 | AutoLoRa > vanilla RFT | C2 | Only CIFAR-10; no AA evaluation |
| E4 | Rank rnat sensitivity | rnat ∈ {2,4,8,16} on 4 datasets | SA, RA | rnat=8 sufficient, marginal gains beyond | C2 | No analysis of rank vs dataset complexity |
| E5 | Pre-training budget ϵpt sensitivity | ϵpt ∈ {0,1/255,2/255,4/255,8/255} on CIFAR-100 and DTD-57 | SA, RA | Larger ϵpt beneficial; AutoLoRa consistently better | C2 | Limited to 2 datasets |
| E6 | Automated LR scheduler on TWINS | Apply scheduler to TWINS | SA, RA | Comparable to tuned TWINS | C3 | RA slightly lower on some tasks |
| E7 | α sharpening sensitivity | α ∈ {0.2,0.5,0.8,1.0,2.0,3.0,5.0} on CIFAR-10/100 | SA, RA | α=1.0 best | C3 | Only tested on 2 low-res datasets |
| E8 | Gradient similarity measurement | CIFAR-10, DTD-57, CUB-200 | Cosine similarity | AutoLoRa >> vanilla RFT/TWINS | C1 | Correlation, not causal |
| E9 | LR sensitivity | Initial LR ∈ {0.001,0.01,0.03} on CIFAR-100 | SA, AA | AutoLoRa robust to LR changes | C1+C3 | Only 1 dataset; only LR |

### Research-Theme Gap Diagnosis

| Theme | Current Status | Gap |
|-------|---------------|-----|
| New Knowledge (C1 — gradient divergence) | Empirical observation only | No causal evidence; no theoretical analysis of when/why divergence occurs |
| New Knowledge (C2 — LoRa disentanglement) | Method works empirically | Competing mechanisms (capacity, regularization, distillation) not separated |
| Reproducibility | Code available; hyperparameters reported | Selection bias in evaluation; no training curves; no per-seed variance in main tables |
| Practical Impact | Automation reduces tuning | Still requires λmax2, α, rnat selection; not validated on LLM fine-tuning |

### Proposed Research Experiments

**Exp P0.1 (P0 — Causal Isolation Ablation)**
- Target Claim: C2 (disentanglement drives robustness gains, not capacity/regularization)
- Hypothesis: Gradient separation without extra capacity will match AutoLoRa performance
- Minimal Design: Three ablation variants (A: separation only via dual classifier heads; B: LoRa capacity without gradient stopping; C: no KL loss)
- Controls/Baselines: Same optimizer, epochs, attack budget as main experiments
- Metrics: SA, PGD-10, AA; gradient similarity
- Success Criterion: Ablation A ≈ AutoLoRa; Ablation B < AutoLoRa; or any pattern that isolates mechanism
- Estimated Cost/Time: ~2 GPU-days per variant (using ResNet-18, CIFAR-100 and DTD-57)
- Expected Paper-Quality Gain: Transforms the paper from correlational claim to causal understanding

**Exp P0.2 (P0 — Validation-Based Evaluation)**
- Target Claim: All robustness claims
- Hypothesis: Gains hold under proper evaluation protocol
- Minimal Design: Re-run all experiments with checkpoint selected on 5% validation set (not test set)
- Controls/Baselines: Compare validation-selected vs test-selected results
- Metrics: Mean±std SA, PGD-10, AA across 3 seeds
- Success Criterion: Gains direction and significance are preserved
- Estimated Cost/Time: Reuse existing checkpoints if stored; otherwise ~5 GPU-days
- Expected Paper-Quality Gain: Removes evaluation bias concern; adds statistical rigor

**Exp P1.1 (P1 — Expanded Baseline Comparison)**
- Target Claim: "State-of-the-art" → "stronger than vanilla RFT and TWINS"
- Hypothesis: AutoLoRa is competitive with or better than additional baselines
- Minimal Design: Add 2-3 baselines (standard adversarial training from scratch, adapter-based robust fine-tuning, full fine-tuning with gradient clipping)
- Controls/Baselines: Same attack budget (ϵ=8/255), optimizer, epochs
- Metrics: SA, PGD-10, AA; training time
- Success Criterion: AutoLoRa shows competitive or better performance
- Estimated Cost/Time: ~3-5 GPU-days depending on baseline complexity
- Expected Paper-Quality Gain: Substantially strengthens empirical positioning

**Exp P2.1 (P2 — λ1/λ2 Dynamics Visualization)**
- Target Claim: C3 (automated scheduler improves optimization)
- Hypothesis: λ1 decreases and λ2 increases smoothly as training progresses
- Minimal Design: Log λ1, λ2, and LoRa SA at each epoch for CIFAR-100 and DTD-57
- Metrics: Plot λ1, λ2, SA_LoRa vs epochs
- Success Criterion: Smooth transition with λ2 > 0.5 within first 10 epochs
- Estimated Cost/Time: Minimal (logging only)
- Expected Paper-Quality Gain: Increases transparency and reproducibility of scheduler behavior

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Experiments (Publication-Critical)
├── P0.1: Causal Ablation (3 variants)
│   ├── Ablation A: Separation-only (no LoRa)
│   ├── Ablation B: LoRa capacity-only (no separation)
│   └── Ablation C: No KL distillation
│   └── Expected: Identifies true mechanism
│
└── P0.2: Fix Evaluation Protocol
    ├── Validation-set checkpoint selection
    ├── Report mean±std across 3 seeds
    └── Expected: Removes bias, adds rigor

P1 Experiments (High Priority)
├── P1.1: Expand Baselines
│   ├── Standard adversarial training
│   ├── Adapter-based robust fine-tuning
│   └── Full fine-tuning (with gradient clipping)
│   └── Expected: Strengthens empirical positioning
│
└── [Already covered by writing fixes]

P2 Experiments (Nice-to-Have)
├── P2.1: λ1/λ2 dynamics visualization
└── [Other minor improvements]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale:** The paper presents a clearly motivated and technically sound method for improving robust fine-tuning through gradient separation via a LoRa branch. The empirical evaluation is reasonably comprehensive (6 datasets, 2+ backbones, VT ablation). However, several factors cap the score at 6.5:

1. **Causal overclaim (severity: major):** The paper's core argument — that gradient divergence causes poor robustness and its resolution drives gains — is supported only by correlational evidence with unaddressed confounds. This undermines the primary scientific claim.

2. **Evaluation bias (severity: major):** Test-set-based checkpoint selection likely inflates reported numbers.

3. **Limited baselines (severity: major):** With only two comparators, the empirical positioning is weak.

4. **Missing limitation section (severity: major):** Scientific completeness requires honest discussion of scope and honest scope boundaries.

5. **Novelty is plausible but unverifiable in this run (verification deferred):** The core idea (LoRa-based optimization separation) is a reasonable contribution to RFT, but without external literature verification, a firm novelty judgment cannot be made.

**Post-Revision Target: [7.5, 8.0]/10**

**Rationale:** If the authors address the P0 items (causal ablation experiments, fix evaluation protocol, add limitation section), replace SOTA claims, and acknowledge remaining hyperparameters, the paper would become a solid 7.5-8.0. The core technical idea is sound, the experiments are extensive, and the problem is well-motivated. The main barriers are causal evidence and evaluation rigor, which are fixable with targeted experiments and writing revisions. Adding 2-3 baseline comparisons (P1.1) would further strengthen the position.

**Scoring Breakdown (current):**
- Research Value/Contribution: 6/10 (good motivation, but mechanistic claim not yet proven)
- Novelty: 6/10 (plausible; deferred verification)
- Validity/Soundness: 5/10 (causal overclaim + evaluation bias)
- Reproducibility: 7/10 (code available, most details reported)
- Clarity/Presentation: 7/10 (well-structured, but overclaims and missing limitations)
- Practical Utility: 7/10 (automation value is real, but limited by remaining hyperparameters)