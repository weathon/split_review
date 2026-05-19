## Summary
# Final Review Report

## Summary

This paper proposes FTA (Flexible Trigger Attack), a generator-assisted backdoor attack against federated learning (FL) that aims to achieve stealthiness across three dimensions: imperceptible triggers (P3), undetectable feature representations (P1), and minimal parameter-level anomalies (P2). Instead of using universal patch-based triggers common in prior work, FTA trains a generative trigger network (autoencoder or U-Net) that produces sample-specific imperceptible perturbations. The generator is optimized to make poisoned samples share similar hidden features with benign samples of the target label, enabling the backdoor to reuse benign routing paths in the classifier.

The paper formulates the attack as a constrained bilevel optimization problem and solves it through a sequential two-phase procedure: first training the trigger generator with the classifier fixed, then training the malicious classifier with the generator fixed. The generator is continuously updated across FL rounds to adapt to changes in the global model.

Experiments on four benchmark datasets (Fashion-MNIST, FEMNIST, CIFAR-10, Tiny-ImageNet) with eight FL defenses demonstrate that FTA achieves high backdoor accuracy (>98% in many settings) while maintaining better stealthiness than baseline attacks, DBA, Neurotoxin, and Edge-case, as measured by SSIM/LPIPS and similarity metrics between malicious and benign updates.

**Bottom line:** The paper presents a technically sound and empirically well-supported attack framework with a clearly motivated design. However, significant concerns include: (1) unverifiable "first" and "SOTA" claims due to the unavailability of external literature verification in this review; (2) a non-standard norm clipping defense variant that may unfairly favor FTA; (3) missing variance reporting for key results; (4) an optimization formulation that is not truly solved as claimed; (5) a factual error in the claimed FC layer parameter fraction for ResNet18; and (6) a privacy contradiction in the multi-agent collusion solution. The novelty positioning against centralized generator-based attacks is the strongest conceptual contribution, but direct empirical comparisons are missing.

## Strengths
1. **Clear problem decomposition (P1-P3).** The paper systematically identifies three distinct stealthiness problems—feature extraction anomaly, backdoor routing anomaly, and perceptible trigger anomaly—that are well-motivated and provide a structured basis for the proposed solution. This three-axis framing is a genuine improvement over prior work that focuses on only one aspect of stealthiness.

2. **Conceptually sound mechanism design.** The core idea—using a generator to produce sample-specific triggers that align poisoned-sample features with target-class features—is well-grounded in representation learning principles. The t-SNE visualization (Figure 5) convincingly demonstrates that FTA achieves feature-space overlap between poisoned and target-label samples, supporting the claimed mechanism.

3. **Extensive defense evaluation.** The evaluation against 8 FL defenses (norm clipping, FLAME, Multi-Krum, Trimmed-mean, RFA, SignSGD, Foolsgold, SparseFed) plus RLR and Pruning on 4 datasets is comprehensive. This breadth helps demonstrate that FTA's stealthiness advantage is not limited to a specific defense type.

4. **Computational efficiency analysis.** Table 5 provides a clear comparison of time and memory costs, showing that FTA adds less than 30% overhead over benign training and is substantially cheaper than Neurotoxin (~2× overhead). This practical analysis strengthens the claim that the attack is deployable.

5. **Ablation studies on key hyperparameters.** The appendix includes systematic ablation of trigger size, poison fraction, and generator dataset size (Figure 13), providing practical guidance for deploying the attack and demonstrating robustness to these choices.

6. **Clean differentiation from centralized generator attacks. The paper. The "v.s. Trigger generators in centralized setting" subsection (Page 4) provides a clear conceptual distinction—centralized generators constrain only input/feature similarity to benign samples, while FTA constrains similarity to target-label samples—which is the paper's most original conceptual contribution.

## Weaknesses
1. **Factual error in ResNet18 FC layer parameter fraction.** Page 2, P2 claims "62% in ResNet18" for the last FC layer's parameter share. Standard ResNet18 (512×1000 = 512K parameters out of ~11M total) yields ~4.7%, not 62%. This error undermines the quantitative support for the P2 argument and raises concerns about the reliability of other numerical claims.

2. **Non-standard norm clipping defense may unfairly favor FTA.** Page 8 uses an adaptive variant of norm clipping where the threshold is dynamically computed from benign updates. This differs from standard norm clipping (fixed threshold). The authors do not justify why this variant is used or analyze whether prior attacks would perform better under standard clipping. An adaptive threshold that follows benign update norms may inadvertently give FTA—which produces small-norm updates by design—an unfair advantage.

3. **Missing variance/statistical rigor in main results.** The attack effectiveness results (Figure 3, Page 7) are reported as single curves without error bars, confidence intervals, or significance tests. The text makes strong comparative claims ("60% higher," "at least 25% advantage") that cannot be assessed for statistical reliability. This is especially concerning for results where different attacks show overlapping trajectories (e.g., FEMNIST).

4. **Unverifiable "first" and "SOTA" claims.** The abstract and contributions make unqualified "for the first time" and "state-of-the-art" claims that cannot be verified in this review due to Retrieval-Disabled Mode. Even with external literature, such claims require careful scope bounding.

5. **Optimization claim vs. actual procedure mismatch.** The paper formulates a bilevel optimization (Equation 1) but solves it with a sequential two-phase heuristic (Section 3.3) that does not alternate or guarantee convergence to a bilevel optimum. The text calls this a "simple but practical optimization process" without acknowledging the gap between the formulation and the approximation.

6. **Privacy contradiction in multi-agent collusion.** Appendix A.2 solves the multi-agent non-i.i.d. problem by having malicious agents "share a portion of their local datasets." This directly contradicts the privacy premise of FL, where agents cannot share raw data. The paper does not discuss this trade-off.

7. **Missing limitations section.** The conclusion (Page 9) does not acknowledge any limitations of FTA. The attack is only evaluated on computer vision tasks; its effectiveness on NLP or RL tasks is unknown. The paper also does not discuss potential adaptive defenses that could detect generator-based backdoors.

8. **Confounded dataset scaling.** Table 1 shows different total agent counts (1000-3000) across datasets without explanation. Since larger agent pools mean the malicious agent is selected less frequently, this confounds cross-dataset comparison of convergence speed.</｜DSML｜parameter.

## Key Issues
### Issue 1 (Critical): Factual Error in ResNet18 Parameter Fraction Claim
- **Location:** Page 2 - P2 paragraph (backdoor routing abnormality)
- **Problem:** The paper states that the last FC layer contains "62% in ResNet18" of total parameters. For standard ResNet18, the FC layer has 512×1000≈512K parameters out of ~11M total, yielding ~4.7%, not 62%. This ~13× discrepancy is not a typographical error but a substantive misrepresentation of architectural importance.
- **Risk:** Undermines the quantitative foundation of the P2 argument. If the FC parameter fraction claim is corrected, the argument that FC-layer abnormality is the primary stealthiness challenge is weakened.
- **Fix:** Correct the number or clarify if a non-standard ResNet18 variant was used. If the authors used a wider classifier head, specify the exact architecture.

### Issue 2 (Major): Unverifiable Novelty and SOTA Claims
- **Location:** Page 1 (Abstract), Page 3 (Contributions)
- **Problem:** The abstract claims "we for the first time consider the natural stealthiness of triggers during global inference," and contribution 3 claims "state-of-the-art effectiveness and stealthiness." These claims cannot be verified without controlled literature comparison, which is unavailable in this review. Even with literature, "first" claims in a mature field like backdoor attacks require extremely careful scoping.
- **Risk:** If prior work exists that already achieves similar stealthiness properties (e.g., centralized generator-based attacks adapted to FL), the core novelty claim collapses.
- **Fix:** Remove unqualified "first" and "SOTA" wording. Use scoped claims: "To our knowledge, no prior FL backdoor attack simultaneously addresses feature-space stealthiness, parameter-level stealthiness, and trigger imperceptibility. Our experiments on eight defenses demonstrate competitive or superior stealthiness under the evaluated settings."

### Issue 3 (Major): Bilevel Optimization Formulation vs. Sequential Approximation Gap
- **Location:** Page 5 (Equation 1), Page 6 (Section 3.3)
- **Problem:** Equation (1) presents a bilevel optimization problem where ξ* is defined as the argmin of the inner problem given θ, while simultaneously θ is optimized given ξ*(θ). The sequential two-phase procedure (fix θ→optimize ξ, then fix ξ→optimize θ) does not solve this coupled problem—it approximates it with a one-pass sequential approach. The paper does not acknowledge this gap or analyze its impact.
- **Risk:** A mathematically informed reader will recognize that the proposed algorithm does not solve the stated optimization problem. This weakens the paper's technical rigor.
- **Fix:** Reframe the formulation as a constrained optimization that is approximately solved via sequential two-phase training. Add an analysis of the approximation error or convergence properties of the sequential procedure.

### Issue 4 (Major): Non-Standard Norm Clipping Defense Variant
- **Location:** Page 8 (Section 4.3.1)
- **Problem:** The norm clipping variant uses an adaptive threshold computed by filtering extreme updates and averaging the rest. This differs from standard norm clipping (fixed threshold τ). Without justification or comparison to standard clipping, it is unclear whether FTA's advantage over prior attacks is due to the attack design or the defense variant.
- **Risk:** A reviewer could argue that standard norm clipping with properly tuned fixed threshold would reduce FTA's advantage, making the defense comparison misleading.
- **Fix:** Add experiments with standard norm clipping (fixed threshold) and discuss any differences.

### Issue 5 (Major): Missing Variance in Key Results
- **Location:** Page 7 (Section 4.2, Figure 3)
- **Problem: All BA curves in Figure 3 are single trajectories without error bars, standard deviations, or significance tests. Strong comparative statements ("60% higher," "at least 25% advantage") are made without statistical support.
- **Risk:** Without variance information, readers cannot assess whether the reported advantages are within natural random variation. This is especially concerning given the overlapping trajectories on FEMNIST.
- **Fix:** Report mean±std over ≥3 random seeds for all main results. Add a brief significance statement for the primary comparison on each dataset.

## Actionable Suggestions
### Suggestion 1 (Must): Correct the ResNet18 FC parameter fraction
- **Action:** Replace "62% in ResNet18" with the correct value (~4.7; if a non-standard ResNet18 variant was used, report the exact architecture and recompute the fraction.
- **Location:** Page 2, P2 paragraph
- **Rationale:** Correcting this factual error is essential for establishing technical credibility.

### Suggestion 2 (Must): Add standard norm clipping experiments
- **Action:** Run all attacks under standard norm clipping with a fixed threshold (e.g., τ = median of benign update norms from the first 5 rounds). Report results in the same figure format as Figure 4 (a)-(d).
- **Location:** Section 4.3.1
- **Rationale:** This ensures fair defense comparison and addresses the concern that the adaptive variant favors FTA.

### Suggestion 3 (Must): Report variance in all main results
- **Action:** Re-run all experiments in Figures 3 and 4 with ≥3 random seeds. Report mean BA ± std. Add a brief footnote stating which differences are statistically significant (e.g., via paired bootstrap test).
- **Location:** Section 4.2, Figures 3-4
- **Rationale:** Essential for statistical credibility.

### Suggestion 4 (Must): Acknowledge optimization approximation gap
- **Action:** In Section 3.3, add a paragraph explicitly stating that the sequential two-phase procedure is an approximation of the bilevel formulation in Equation (1), and discuss the conditions under which this approximation is reasonable (small e_T, e_f; stable f_θ across phases).
- **Location:** Page 5-6, transition from 3.1 to 3.3
- **Rationale:** Addresses the formulation-implementation mismatch.

### Suggestion 5 (Must): Add limitations section
- **Action:** In the conclusion (Page 9), add 2-3 sentences acknowledging: (a) evaluation is limited to computer vision; (b) adaptive defenses could potentially detect generator-based attacks; (c) the privacy trade-off in multi-agent collusion.
- **Rationale:** Improves scientific objectivity and helps the community understand the attack's boundaries.

### Suggestion 6 (Nice-to-have): Add direct comparison with centralized generator adapted to FL
- **Action:** Include an ablation where a centralized generator (e.g., from Doan et al. 2021b or Zhao et al. 2022b) is applied in the FL setting with the same threat model. Compare BA, SSIM/LPIPS, and cosine similarity of updates against FTA.
- **Location:** Section 2.2 or a new appendix subsection
- **Rationale:** This would directly validate the paper's central novelty claim that target-label feature alignment is necessary for FL stealthiness.

### Suggestion 7 (Nice-to-have): Explain NA entries in Table 4
- **Action:** Add a footnote to Table 4 explaining why LPIPS is NA for Fashion-MNIST (grayscale images; LPIPS requires 3-channel RGB input).
- **Location:** Appendix A.9, Table 4
- **Rationale:** Prevents reader confusion about missing data.

### Suggestion 8 (Nice-to-have): Add quantitative feature-space metrics
- **Action:** In addition to t-SNE visualization (Figure 5), report quantitative metrics such as Frechet Distance or cosine similarity between feature centroids of poisoned samples and target-label samples, with and without FTA.
- **Location:** Section 4.4
- **Rationale:** t-SNE visualization alone is insufficient for causal mechanism claims; quantitative metrics would strengthen the evidence.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current storyline follows: FL background → backdoor threat → three problems (P1-P3) → proposed solution → contributions. This structure is reasonable but has room for improvement in narrative clarity.

**Current weaknesses in narrative:**
- The introduction opens with FL applications rather than the core security problem
- P1-P3 are presented before the reader fully understands why stealthiness is the key challenge
- The solution description (Page 3) repeats the same argument multiple times ("reuse benign routing")

### Recommended Storyline (Option A: Problem-First)

**Structure:** Security Gap → Three Stealthiness Dimensions → Method → Evidence

**Abstract Outline (S1-S5):**
- S1 (Problem): Backdoor attacks on FL are detectable because universal triggers create feature-space and parameter-space anomalies.
- S2 (Challenge): Achieving stealthiness requires simultaneously addressing trigger perceptibility, feature-space separability, and parameter-level detectability.
- S3 (Prior Gap): Existing attacks focus on only one aspect; no prior work jointly addresses all three.
- S4 (Method): FTA uses a generative trigger network that produces sample-specific, imperceptible triggers aligned with target-label features, updated adaptively across FL rounds.
- S5 (Result): On four datasets and eight defenses, FTA achieves >98% ASR with higher SSIM/LPIPS and lower update dissimilarity than prior attacks.

### Introduction Outline (P1-P5)

**P1 (Big Picture & Threat):** 
"Federated learning enables collaborative training without sharing raw data, but this decentralized architecture is vulnerable to backdoor attacks where malicious agents inject poisoned updates. While FL defenses (norm clipping, clustering, trigger inversion) can detect many existing attacks, they do so by exploiting characteristic abnormalities in the attacker's model updates and trigger patterns."

**P2 (Problem Decomposition - Three Stealthiness Dimensions):**
"We identify three distinct stealthiness problems in existing FL backdoor attacks. First, universal patch-based triggers introduce separable feature representations in convolutional layers (P1). Second, the backdoor task creates a separate routing path in fully connected layers that produces parameter-level anomalies (P2). Third, perceptible triggers can be visually identified or inverted during inference (P3). These three problems are interconnected: visible triggers cause feature separability, which forces separate routing, which creates detectable parameters."

**P3 (Prior Work Limitations):**
"Prior attacks—including DBA, Neurotoxin prior work, Neurotoxin, and Edge-case—rely on universal trigger patterns or tail data. While effective under no defense, these approaches fail against robust FL aggregators because they do not address P1-P3. Centralized generator-based attacks (Doan et al., 2021b; Zhao et al., 2022b) produce imperceptible triggers but constrain only input-space similarity, not target-label feature alignment—leaving P1-P2 unresolved in FL settings."

**P4 (Proposed Solution & Intuition):**
"We propose FTA, a generator-assisted backdoor attack that addresses all three stealthiness dimensions. A generative trigger network produces sample-specific, ℓ2-bounded perturbations. The generator is trained to minimize the feature-space distance between poisoned samples and benign samples of the target label, enabling the backdoor to reuse benign routing paths. The generator is updated across FL rounds to adapt to global model changes."

**P5 (Contributions Summary):**
"• A generator-assisted attack framework addressing three stealthiness dimensions simultaneously. • An adaptive trigger generator with sequential two-phase optimization practical for FL. • Comprehensive evaluation against eight FL defenses on four datasets demonstrating improved stealthiness and effectiveness."

### Alternative Storyline (Option B: Defense-Focused)

Start with the defense perspective: "Current FL defenses detect backdoors by exploiting three signatures: anomalous feature activations, parameter outliers, and visible trigger patterns. We design an attack that systematically eliminates all three signatures." This framing positions the paper as a red-team analysis of FL defense assumptions, which may appeal to security-oriented venues.

## Priority Revision Plan
### P0 Items (Must-fix, publication-critical)

1. **Correct ResNet18 parameter fraction** (Issue 1)
   - Fix the 62% → ~4.7% (or report actual architecture used)
   - Effort: ~1 hour. Impact: Prevents factual rejection.

2. **Add variance reporting for main results** (Issue 5)
   - Re-run Figures 3-4 with ≥3 seeds, add error bars
   - Effort: ~2-3 GPU-days. Impact: Enables statistical verification of claims.

3. **Acknowledge optimization approximation** (Issue 3)
   - Add paragraph in Section 3.3 explaining the sequential procedure is an approximation
   - Effort: ~2 hours. Impact: Resolves formulation-implementation mismatch.

4. **Add standard norm clipping comparison** (Issue 4)
   - Run experiments with fixed-threshold norm clipping
   - Effort: ~1 GPU-day. Impact: Ensures defense evaluation fairness.

### P1 Items (High-impact low-effort: #1, #3 (can be done without new experiments)
High-impact medium-effort: #2, #4 (requires GPU time but directly addresses core validity concerns)

### P1 Items (Should-fix, quality improvement)

5. **Add limitations section in conclusion** (Suggestion 5)
   - Effort: ~1 hour. Impact: Improves scientific completeness and objectivity.

6. **Add quantitative feature-space metrics** (Suggestion 8)
   - Compute Frechet Distance / centroid cosine similarity for Figure 5
   - Effort: ~1 GPU-hour. Impact: Strengthens causal mechanism evidence.

7. **Address multi-agent privacy contradiction** (Issue 6)
   - Discuss the data sharing trade-off or propose a privacy-preserving alternative
   - Effort: ~1 day. Impact: Resolves tension with FL privacy assumptions.

### P2 Items (Nice-to-have)

8. **Direct comparison with centralized generator adapted to FL** (Suggestion 6)
   - Effort: ~2 GPU-days. Impact: Validates central novelty claim.

9. **Explain NA entries in Table 4** (Suggestion 7)
   - Effort: ~30 minutes. Impact: Prevents reader confusion.

10. **Justify dataset scaling confounds** (Weakness 8)
    - Add discussion of how total agent count affects attack difficulty
    - Effort: ~1 hour. Impact: Improves cross-dataset comparison clarity.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Attack effectiveness under no defense (fixed-frequency) | 4 datasets, FedAvg, compare vs Baseline, DBA, Neurotoxin, Edge-case | BA over FL rounds | FTA converges faster and reaches highest BA (98-100%) | C1, C2 | No variance reported; single-run curves |
| E2 | Attack durability (few-shot mode) | Same as E1, attack stops after 100 rounds | BA decay after attack stops | FTA decays slower than baseline, comparable to Neurotoxin | C1 (durability) | Durability is not the paper's claimed focus; Neurotoxin often outperforms |
| E3 | Stealthiness against norm clipping (defense) | Norm clipping variant, 4 datasets, fixed-frequency | BA | FTA maintains high BA, prior attacks suppressed | C3 | Non-standard clipping variant may be unfair |
| E4 | Stealthiness against FLAME (defense) | FLAME clustering, 4 datasets, fixed-frequency | BA | FTA >99% in CIFAR-10, Tiny-ImageNet | C3 | FEMNIST results show only marginal advantage |
| E5 | Stealthiness against Multi-Krum | Multi-Krum, 4 datasets | BA | FTA near 100% in CIFAR-10, Tiny-ImageNet; ~90% in FEMNIST | C3 | Fashion-MNIST convergence slow |
| E6 | Stealthiness against Trimmed-mean | Trimmed-mean, 4 datasets | BA | FTA 96-99.9% in CIFAR-10, Fashion-MNIST, FEMNIST | C3 | Tiny-ImageNet performance significantly degraded |
| E7 | Stealthiness against RFA, SignSGD, Foolsgold, SparseFed | Respective defenses, subset of datasets | BA | FTA outperforms baselines | C3 | Not all defenses tested on all datasets |
| E8 | Feature-space analysis (t-SNE) | CIFAR-10, baseline vs FTA | t-SNE visualization, Euclidean/cosine similarity | FTA achieves feature overlap with target label | C1 (mechanism) | Qualitative only; no quantitative metrics; single visualization |
| E9 | Natural stealthiness (SSIM/LPIPS) | 4 datasets, compare vs all baselines | SSIM↑, LPIPS↓ | FTA achieves highest SSIM (0.9967-0.9978) and lowest LPIPS | P3 (trigger stealthiness) | LPIPS NA for Fashion-MNIST; no statistical comparison |
| E10 | Computational cost | Time and memory per FL round | Mean±SD time, memory | FTA <30% overhead over benign; ~70% cheaper than Neurotoxin | Practical deployability | Statistical significance of differences not tested |
| E11 | Ablation: trigger size | Vary ϵ, all datasets | BA vs ϵ | Performance drops sharply below threshold size | Practical guidance | - |
| E12 | Ablation: poison fraction | Vary fraction 0.01-0.2, all datasets | BA vs fraction | FTA effective down to 0.05 fraction | Practical guidance | FEMNIST, Tiny-ImageNet degrade at 0.01 |
| E13 | Ablation: generator dataset size | Vary 32-1024, all datasets | BA vs dataset size | Effective even at 32 samples | Practical guidance | - |
| E14 | Post-training defense (Pruning) | FEMNIST, CIFAR-10 | BA vs prune ratio | FTA maintains 80% BA at 50% prune ratio | Robustness (C3) | Only tested on 2 datasets |

### Research-Theme Gap Diagnosis

The paper's core research-value claims are: (1) new knowledge about the three stealthiness dimensions and how to address them jointly, (2) a practical attack framework reproducible from the description, and (3) potential to change how FL defense research evaluates stealthiness.

**Gap 1 (New knowledge):** The central conceptual claim—that aligning poisoned features with target-label features (not just benign features) is necessary for FL stealthiness—is well-motivated but lacks direct empirical validation. No experiment compares FTA directly compares FTA against a centralized generator adapted to FL with the same threat model.

**Gap 2 (Reproducibility):** The main algorithm (Section 3.3, Algorithm 1) is described with sufficient detail. However, the non-standard norm clipping defense variant and ambiguous agent selection description reduce reproducibility confidence.

**Gap 3 (Impact on practice/understanding):** The paper could more strongly impact defense research by identifying which defenses are most vulnerable to FTA's approach and why, rather than presenting a broad comparison across eight defenses.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Effort | Paper-Quality Gain |
|-------------|-----------|---------------|-------------------|---------|------------------|--------|-------------------|
| C1 (cont (Centralized generator adaptation) | Centralized generator adapted to FL will have lower stealthiness than FTA under clustering defenses | Apply Doan et al. 2021b generator in FL setting with same threat model as FTA | FTA vs centralized-gen-FL vs baseline | BA under FLAME; cosine similarity of updates | Centralized-gen-FL BA < FTA BA by >20% under FLAME on CIFAR-10 | 2 GPU-days | Validates central novelty claim |
| C3 (Standard norm clipping) | FTA's advantage under standard fixed-threshold clipping will be smaller than under adaptive variant | All attacks under fixed-threshold norm clipping (τ = median of benign norms from warm-up) | Adaptive vs standard clipping, all attacks | BA over rounds | Demonstrate that FTA still outperforms baselines under standard clipping | 1 GPU-day | Ensures defense evaluation fairness |
| C1 (Variance) | Main results are stable across random seeds | Re-run Figures 3-4 with ≥3 seeds | Same attacks, same settings | Mean±std BA | Standard deviation <5% for FTA on each dataset | 2-3 GPU-days | Enables statistical claim verification |
| Mechanism (Quantitative feature metrics) | Feature-space overlap is quantifiable and correlates with attack success | Compute Frechet Distance / cosine centroid similarity between poisoned and target-label features | Baseline vs FTA, at multiple FL rounds | Frechet Distance; correlation with BA | Frechet Distance for FTA <50% of baseline distance | <1 GPU-hour | Strengthens causal mechanism evidence |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5 / 10

**Reasoning:** The paper presents a technically sound and well-motivated attack framework with extensive empirical evaluation. The core idea—aligning poisoned-sample features with target-label features via a generator—is conceptually interesting and the experimental results are largely consistent with the claimed mechanism. However, several significant issues reduce the overall score:

- **Research value/novelty (weighted heavily):** The central novelty claim (first to consider natural stealthiness in FL inference) cannot be verified externally in this review. The conceptual distinction from centralized generator-based attacks is the strongest novelty element, but it lacks direct empirical validation. Score: 5/10.

- **Validity/soundness:** A factual error in the ResNet18 parameter fraction (~4.7% vs claimed 62%), non-standard norm clipping defense that may unfairly favor FTA, and missing variance reporting raise concerns about the reliability of specific claims. The optimization formulation mismatch further weakens technical rigor. Score: 5/10.

- **Reproducibility:** Algorithm description is adequate. Experimental setup has ambiguous aspects (agent selection, defense variant), but the appendix provides sufficient detail for approximate reproduction. Score: 6/10.

**Post-Revision Target:** [6.5, 7.5] / 10

If the authors address P0 items (correct factual error, add variance reporting, acknowledge optimization approximation, add standard norm clipping experiments) and P1 items (add limitations section, quantitative feature metrics), the score could reach 6.5-7.5. The upper bound assumes that the corrected norm clipping experiments still show FTA's advantage and that the novelty claims hold under external verification.