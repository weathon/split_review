## Summary
This paper proposes CAUSE (CAusal Unsupervised Semantic sEgmentation), a framework that applies causal inference (frontdoor adjustment) to unsupervised semantic segmentation (USS). The key idea is to decompose USS into two subproblems: (Step 1) constructing a discretized "concept clusterbook" as a mediator via modularity maximization, and (Step 2) using concept-wise self-supervised learning to consolidate or separate concept prototypes into target semantic groups. The method is evaluated on COCO-Stuff, Cityscapes, and Pascal VOC, demonstrating competitive performance against recent USS methods.

**Core claims (C1-C3):**
- **C1:** Novel application of causal inference (frontdoor adjustment) to USS, addressing the ambiguity of "what and how to cluster."
- **C2:** A two-step framework: (a) discretized concept clusterbook construction via modularity maximization, and (b) concept-wise self-supervised learning using a distance-based positive/negative selection mechanism and a concept bank.
- **C3:** State-of-the-art USS performance across multiple datasets without external information.

The paper has a clear technical contribution in framing USS through causal lens, and the two-step decomposition is architecturally novel. However, several issues need attention: the causal justification has conceptual gaps (incorrect collider reasoning, unverified assumptions), the "state-of-the-art" claim requires qualification, and several design choices (tanh approximation, positive/negative thresholds, bank update ratio) lack sufficient sensitivity analysis.

## Strengths
1. **Novel problem framing through causal lens.** The paper is the first to explicitly formulate the granularity ambiguity in USS as a causal inference problem. The frontdoor adjustment framing (T→M→Y) provides a principled decomposition that cleanly separates the construction of a concept representation from the consolidation into semantic groups. This is a genuine conceptual contribution that opens a new direction for USS research.

2. **Technically sound two-step architecture.** The two-step design (modularity-based concept clusterbook + concept-wise self-supervised learning) is internally consistent and each component has a clear role in the causal framework. The use of vector quantization to create discrete concept prototypes, and the concept bank for out-batch accumulation, are well-motivated engineering choices.

3. **Strong empirical results.** CAUSE achieves substantial improvements over prior USS methods (STEGO, HP) across multiple backbones. For example, on COCO-Stuff with ViT-B/8, CAUSE-TR reaches 41.9 mIoU vs. 28.2 for STEGO. The linear probing results (Table 2) show even larger gains, suggesting that CAUSE learns higher-quality dense representations. The generalization experiments across different self-supervised backbones (DINOv2, iBOT, MSN, MAE) demonstrate the framework's adaptability.

4. **Thorough ablation studies.** The paper provides comprehensive ablation on six factors (positive/negative relaxation, concept count k, concept bank, CRF, discretization method). Table 4 is particularly informative, showing that each component contributes positively and that modularity maximization outperforms alternative clustering methods (K-Means++, Spectral, Agglomerative, Ward).

5. **Honest failure case discussion.** Appendix C.2 and D provide a candid discussion of failure modes, including noisy segmentation in complex scenes and the trade-off with concept count k. The identification of the "heuristic static hyperparameter" issue in Appendix D shows awareness of practical limitations, which improves the paper's credibility.

## Weaknesses
1. **Causal reasoning has conceptual gaps.** The paper claims frontdoor adjustment as the theoretical foundation, but the causal diagram and justification contain inaccuracies. Specifically, the footnote on Page 2 incorrectly identifies Y as a "collider variable" in the path T→Y through U, which is not consistent with the stated diagram T←U→Y. The assumption that the unobserved confounder U affects both pre-trained features T (which are frozen) and semantic groups Y is also questionable. These issues weaken the paper's core theoretical narrative.

2. **Unverifiable novelty claims under Retrieval-Disabled Mode.** The paper claims "for the first time" applying causality to USS and "state-of-the-art" performance. Due to Retrieval-Disabled Mode (external paper search unavailable), these novelty claims cannot be independently verified. The paper does cite Zhang et al. (2020a) for causal intervention in weakly-supervised segmentation, acknowledging that causal ideas have been applied to segmentation before, which partially undercuts the "first" claim.

3. **Unexamined simplifying assumptions in the causal-to-USS mapping.** The derivation from Eq. (1) (frontdoor adjustment) to Eq. (2) (USS approximation) relies on several implicit assumptions: (a) uniform distribution of pixel-level features p(t'), (b) hard assignment (p(m|t) ∈ {0,1}) via sharpening, (c) independence of pixel-wise likelihoods. These assumptions are not justified, and violations could break the claimed causal interpretation.

4. **Heuristic hyperparameter sensitivity.** The positive/negative relaxation thresholds (ϕ+=0.3, ϕ-=0.1) are selected via grid search (0.1-0.7) and vary across datasets (e.g., ϕ+=0.55 for COCO-171). The gap between ϕ+ and ϕ- creates a neutral zone whose effect is unanalyzed. The concept bank replacement ratio (50%) is also chosen without sensitivity analysis. This makes the method harder to apply to new datasets without extensive tuning.

5. **Overclaimed "state-of-the-art" without qualification.** The strongest results are on COCO-Stuff with ViT-B/8. On Cityscapes, the margins are smaller (CAUSE-TR 28.0 vs. STEGO 21.0 with ViT-B/8, but HSG achieves 32.5 with ResNet50). On Pascal VOC, CAUSE-TR (53.3) is close to COMUS (50.0). The claim should be bounded to the specific comparison scope (DINO-backbone methods without external data).

6. **Missing variance and significance reporting.** All results are reported as single numbers without standard deviations or confidence intervals. Given that performance differences are sometimes small (1-3 mIoU points), readers cannot assess whether improvements are statistically significant.

7. **CRF post-processing confound.** The inference pipeline uses CRF refinement, which can substantially improve results. While ablation in Table 4 shows that CRF contributes positively (+2.4 mIoU for CAUSE-TR on COCO-Stuff), the paper does not report whether comparable CRF gains apply to baselines. This makes it difficult to attribute the reported gains solely to the CAUSE framework.

## Key Issues
### Ranked Error Board (Top-7 by severity and research-value impact)

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|---------------|------------|------------|
| **1** | Incorrect collider reasoning in causal footnote (Page 2) | Major | High — undermines theoretical credibility | Easy — remove or correct the collider statement | High |
| **2** | Unjustified assumptions in USS→frontdoor mapping (Page 4) | Major | Medium-High — causal claim weakened if assumptions fail | Medium — add explicit assumption discussion and justification | High |
| **3** | Unqualified "state-of-the-art" and "first" claims | Major | Medium — reviewer confidence reduced | Easy — add scope boundaries and hedging | High |
| **4** | Missing variance/significance for all results | Major | Medium — single-point comparisons may be unreliable | Medium — add multi-seed std and significance tests | High |
| **5** | Heuristic ϕ+/ϕ- thresholds without analysis of neutral zone | Major | Medium — reproducibility on new datasets | Medium — add sensitivity analysis | High |
| **6** | CRF post-processing confound not analyzed for baselines | Major | Medium — gain attribution between method and post-processing unclear | Medium — report all methods with/without CRF | High |
| **7** | Tanh approximation to modularity changes optimization landscape | Major | Medium-Low — practical effect may be small | Medium — add τ ablation and gradient saturation analysis | Medium |

### Detailed Issue Breakdown

**Issue #1 — Collider reasoning error (Page 2, footnote)**
The paper states "In Step 1, Y is a collider variable in the path of T→Y through U, and it blocks backdoor path." This is incorrect. In the stated diagram (T←U→Y), U is a common cause of T and Y. Y is an outcome, not a collider (a collider would be →X←). This misstatement of basic causal concepts can erode reviewer trust in the paper's theoretical contributions. *Fix: Remove the collider claim and simply state that the frontdoor adjustment conditions are satisfied because M is constructed from T alone, making it independent of U given T.*

**Issue #2 — Unjustified assumptions (Page 4-5)**
The transition from Eq.(1) to Eq.(2) implicitly assumes: (a) E_t[p(Y|do(t))] is a valid approximation, (b) hard assignment p(m|t) ∈ {0,1}, (c) uniform p(t'), and (d) independent pixel-wise likelihoods. The uniform p(t') assumption is particularly problematic — in natural images, background pixel features dominate, so the expectation E_t is biased toward background concepts. *Fix: Explicitly list all assumptions, justify each one, and discuss how violations would affect results.*

**Issue #3 — Overclaiming (Page 1-3, 8-9)**
"State-of-the-art" appears 4 times (abstract, intro, contributions, conclusion) without scope qualification. "For the first time" in causal USS (Page 2) is an unverifiable claim. *Fix: Replace with bounded claims and add "to the best of our knowledge" qualifiers.*

**Issue #4 — No statistical reliability evidence (Page 7-8)**
All Table 1-4 results are single-point estimates. Without variance, the 1-3 mIoU improvements over HP/STEGO in several settings may not be statistically significant. *Fix: Report mean±std over 3-5 seeds for the main results.*

**Issue #5 — ϕ+/ϕ- threshold selection (Page 6)**
The positive bound ϕ+=0.3 and negative bound ϕ-=0.1 create a [0.1, 0.3] neutral zone. The number of selected positives/negatives and the effect of this zone are unanalyzed. *Fix: Report average positive/negative counts per anchor, show DM value distribution, and vary thresholds systematically.*

**Issue #6 — CRF as confound (Page 7)**
CRF improves CAUSE-TR by +2.4 mIoU (Table 4). If CRF helps STEGO or HP proportionally more, the method gain would shrink. *Fix: Add a table showing all methods with and without CRF.*

**Issue #7 — Tanh temperature τ (Page 5, Appendix B.1)**
The tanh approximation with τ=0.1 changes the modularity objective. No ablation on τ is provided. *Fix: Ablate τ ∈ {0.01, 0.05, 0.1, 0.5, 1.0} and report impact on concept clusterbook quality.*

## Actionable Suggestions
### Must-fix (publication-critical)

**S1. Correct the collider error and clarify causal justification (Page 2 footnote)**
Replace the incorrect collider statement with a correct causal justification. The frontdoor adjustment conditions are satisfied because M is constructed solely from T, making it conditionally independent of U. No collider reasoning is needed.
```
Current: "In Step 1, Y is a collider variable in the path of T→Y through U, and it blocks backdoor path."
Revised: "Because M is constructed entirely from the pre-trained features T, the path U→M is blocked. 
The two-step decomposition isolates the causal path T→M→Y, satisfying the frontdoor adjustment conditions."
```

**S2. Add explicit assumption catalog for the USS→frontdoor mapping (Page 4-5)**
Add a paragraph after Eq. (2) listing the four assumptions (uniform p(t'), hard assignment, independent pixel likelihoods, expectation approximation). Justify each one with theoretical or empirical evidence. Acknowledge that uniform p(t') is a simplifying approximation and discuss how non-uniform feature distributions (e.g., background-dominated scenes) might affect results.

**S3. Qualify "state-of-the-art" and "first" claims (Pages 1, 3, 8, 9)**
Replace all instances of "state-of-the-art" with bounded qualifiers. Replace "for the first time" with "to the best of our knowledge" or remove it.
```
Abstract: "achieve state-of-the-art performance" → "achieve competitive or superior results on standard USS benchmarks"
Contributions: "for the first time, treat USS within the context of causality" → "we propose a causal lens for USS, a direction not previously explored in this formulation"
```

**S4. Report variance for all main results (Page 7-8, Tables 1-3)**
Add standard deviations from at least 3 random seeds for the main method and the closest baselines. If full re-running is expensive, at minimum add 3-seed variance for the COCO-Stuff ViT-B/8 results where the largest gains are reported.

**S5. Analyze the ϕ+/ϕ- neutral zone (Page 6)**
Report: (a) the average number of positive and negative concept features selected per anchor, (b) the distribution of DM values across all concept prototypes, (c) how varying ϕ- between 0.05-0.3 and ϕ+ between 0.2-0.5 affects performance on COCO-Stuff.

### Nice-to-have (quality improvements)

**S6. Report CRF-free results for all baselines (Page 7)**
Add a supplementary table showing mIoU for all compared methods with and without CRF post-processing. This clarifies how much of the reported gain is from the method vs. CRF.

**S7. Ablate tanh temperature τ in modularity maximization (Appendix B.1)**
Report the impact of τ ∈ {0.01, 0.05, 0.1, 0.5, 1.0} on clusterbook quality and downstream mIoU on COCO-Stuff.

**S8. Add concept bank sensitivity analysis (Page 6)**
Vary replacement ratio (25%, 50%, 75%) and capacity b (50, 100, 200) on COCO-Stuff with CAUSE-TR.

**S9. Restructure Related Work by comparison axes (Page 3)**
Reorganize into thematic paragraphs: (a) USS with pre-trained features (limitation: no granularity control), (b) USS with external priors (difference: no external data needed), (c) Causal inference in CV (difference: frontdoor vs. backdoor approaches).

**S10. Strengthen conclusion with limitations and roadmap (Page 9)**
Add 2-3 concrete limitations and a prioritized future work item to the conclusion.

## Storyline Options + Writing Outlines
### Abstract Outline (complete)

The current abstract is 5 sentences but mixes problem, method, and result without clear role separation. Recommended structure:

- **S1 (Problem + Domain):** Unsupervised semantic segmentation (USS) aims to group pixels semantically without human labels, but a fundamental challenge is the unknown target granularity — the model does not know whether to cluster fine-grained parts (head, torso) or broad categories (person).
- **S2 (Prior Work Gap):** Existing USS methods using pre-trained features lack a principled mechanism to define the clustering target, leading to inconsistent granularity across images.
- **S3 (Proposed Method):** We propose CAUSE, which draws on causal inference (frontdoor adjustment) to decompose USS into two well-defined subproblems: (a) constructing a discrete concept clusterbook via modularity maximization to capture multiple granularity levels, and (b) concept-wise self-supervised learning to consolidate prototypes into target semantic groups.
- **S4 (Key Results):** On COCO-Stuff, Cityscapes, and Pascal VOC, CAUSE achieves competitive or superior results compared to existing USS methods that use no external data.
- **S5 (Bounded Implication):** Our results suggest that causal decomposition can provide a principled framework for unsupervised dense prediction, though sensitivity to heuristic thresholds remains a practical limitation.

### Introduction Outline (complete)

The current introduction has 4 paragraph-like segments on Page 1-2. Recommended restructuring into 6 focused paragraphs:

**P1 — Motivation and stakes (replacing current P1)**
Role: Establish why USS is distinctively hard.
Transition: Broad segmentation context → annotation cost → USS challenge → specific granularity problem.
Key sentence: "The central difficulty in USS is not merely the absence of labels, but the absence of a defined clustering target — should pixels of a person's head, torso, and leg be grouped separately or as one 'person' cluster?"
Evidence anchor: Concrete example (head/torso/leg → person) clarifies the granularity problem.
Link to P2: "Prior methods have made progress but leave this granularity question unresolved."

**P2 — Prior USS methods and their limitation (replacing current P2)**
Role: Survey USS methods critically, not chronologically.
Transition: Early USS (IIC, PiCIE) → Pre-trained feature methods (STEGO, HP) → Common limitation.
Key sentence: "While these methods have improved segmentation quality, they share a common limitation: the clustering objective operates at a fixed granularity determined implicitly by the feature space, without an explicit mechanism to control or adapt the grouping level."
Evidence anchor: Cite Fig. 1 showing STEGO/HP failing to merge person parts.

**P3 — The granularity gap (new)**
Role: Define the specific gap that the paper addresses.
Key sentence: "We identify that the granularity ambiguity can be modeled as an unobserved confounder U that distorts the mapping from pre-trained features T to semantic groups Y."
Link to P4: "This causal perspective offers a new path forward."

**P4 — Causal insight and proposed solution (expanding current P3 ideas)**
Role: Explain the core idea in accessible terms before technical details.
Key sentence: "The frontdoor adjustment decomposes the problem: first build a fine-grained concept clusterbook M from T alone, then consolidate M into target-level groups Y through concept-wise contrastive learning."
Link to P5: "This two-step design leads to our framework, CAUSE."

**P5 — CAUSE framework overview (new, from Page 2-3)**
Role: Briefly describe the architecture and two steps.
Key sentence: "CAUSE comprises (Step 1) modularity-based clustering to create M as a discrete concept mediator, and (Step 2) distance-based positive/negative selection to drive concept-wise self-supervised learning."

**P6 — Contributions (current contribution list, reworded)**
Role: Explicit contribution statements.
Key claim 1: Causal formulation of USS granularity problem.
Key claim 2: Two-step CAUSE framework with concept clusterbook + self-supervised learning.
Key claim 3: Empirical results demonstrating competitive performance.

### Storyline Alternatives Considered

**Alternative A (Problem-first):** Start directly with the granularity question (K* question in current P3) as the first sentence of the introduction. This is more engaging but might skip necessary context for non-specialist readers.

**Alternative B (Causal-first):** Open with the causal diagram (Fig. 2) and the frontdoor adjustment intuition, then explain why USS is a natural fit. This emphasizes the paper's most distinctive contribution but may alienate readers unfamiliar with causal inference.

**Alternative C (Empirical-motivation-first):** Lead with Fig. 1 showing STEGO/HP failures on COCO-Stuff, then explain why this happens, then propose the causal solution. This is the most intuitive path but risks appearing as a patch rather than a principled framework.

**Recommended: Current storyline with the structured 6-paragraph revision above (introduction P1-P6).** This balances accessibility with technical depth and provides clear logical progression from problem → gap → insight → solution → evidence → contribution.

## Priority Revision Plan
### P0 — Submission-critical (must complete before resubmission)

| Priority | Task | Effort | Impact | Affected Section |
|----------|------|--------|--------|-----------------|
| P0.1 | Correct collider error in causal footnote | 1 hour | High (validity) | Page 2 footnote |
| P0.2 | Add explicit assumption catalog for USS→frontdoor mapping | 4 hours | High (validity) | Page 4-5, Section 3.1 |
| P0.3 | Qualify SOTA/novelty claims throughout | 1 hour | High (reviewer perception) | Abstract, Intro, Experiments, Conclusion |
| P0.4 | Add variance (≥3 seeds) for main results | 1-2 days | High (reliability) | Tables 1-3, Page 7-8 |
| P0.5 | Analyze ϕ+/ϕ- threshold sensitivity and neutral zone | 1 day | High (reproducibility) | Page 6, Section 3.3 |
| P0.6 | Report CRF-free results for all baselines | 1 day | High (fair comparison) | Page 7, Table 4 |
| P0.7 | Add τ ablation for modularity tanh approximation | 1 day | High (method rigor) | Appendix B.1 |

### P1 — Major improvement (recommended)

| Priority | Task | Effort | Impact | Affected Section |
|----------|------|--------|--------|-----------------|
| P1.1 | Add concept bank sensitivity analysis | 1-2 days | Medium | Page 6 |
| P1.2 | Restructure Related Work by comparison axes | 2-3 days | Medium | Page 3, Section 2 |
| P1.3 | Strengthen conclusion with limitations | 2 hours | Medium | Page 9, Section 5 |
| P1.4 | Restructure introduction per 6-paragraph plan | 1 day | Medium | Page 1-2, Section 1 |

### P2 — Polish (nice-to-have)

| Priority | Task | Effort | Impact | Affected Section |
|----------|------|--------|--------|-----------------|
| P2.1 | Add quantitative analysis of concept bank retrieval (Fig. 11) | 1-2 days | Low-Medium | Appendix C.3 |
| P2.2 | Quantify k trade-off between complex/simple scenes | 1 day | Low-Medium | Appendix C.2 |
| P2.3 | Expand linear probing analysis with per-class results | 1 day | Low | Page 8 |
| P2.4 | Add failure case quantification (e.g., % of test images with noisy segmentation) | 1 day | Low | Appendix C.2 |

### Schematic Revision Roadmap

```text
Current Manuscript
    │
    ├── P0 fixes (∼5 days total)
    │   ├── Causal corrections (collider + assumptions)
    │   ├── Claim qualifications (SOTA, first)
    │   ├── Statistical rigor (variance, thresholds)
    │   └── Fair comparison (CRF-free baselines)
    │
    ├── P1 improvements (∼4 days)
    │   ├── Sensitivity analysis (bank, τ)
    │   ├── Structure (Related Work, Intro, Conclusion)
    │   └── Limitation discussion
    │
    └── P2 polish (∼3 days)
        ├── Quantitative failure analysis
        ├── Concept bank retrieval analysis
        └── Per-class linear probing
            │
            ▼
    Revised Manuscript (estimated +2-3 weeks)
    Expected improvements: 
    - Theoretical clarity: high
    - Reproducibility: high
    - Reviewer confidence: high
    - Position in field: clear and defensible
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | USS on COCO-Stuff (27 classes) | DINO ViT-S/16, S/8, B/8; CAUSE-MLP & CAUSE-TR | mIoU, pAcc | CAUSE-TR B/8: 41.9 mIoU, +13.7 over STEGO | C3 (SOTA) | Single-seed; CRF confounded |
| E2 | USS on Cityscapes (27 classes) | Same as E1 | mIoU, pAcc | CAUSE-TR B/8: 28.0 mIoU, +7.0 over STEGO | C3 (SOTA) | HSG (32.5) not directly compared due to different backbone |
| E3 | USS on Pascal VOC (21 classes) | Same as E1 | mIoU | CAUSE-TR B/8: 53.3 mIoU, +3.3 over COMUS | C3 (SOTA) | Object-centric setting; COMUS uses different pipeline |
| E4 | Linear probing | DINO + CAUSE features, linear classifier | mIoU, pAcc | CAUSE-TR B/8: 52.3 mIoU on COCO-Stuff | Dense representation quality | Linear probing ≠ USS performance |
| E5 | Generalization to other SSL backbones | DINOv2, iBOT, MSN, MAE with CAUSE-TR | mIoU, pAcc | DINOv2 B/14: 45.3 mIoU on COCO-Stuff | Method generality | Only CAUSE-TR tested |
| E6 | Larger category sets (COCO-81, COCO-171) | CAUSE-MLP & TR with adjusted ϕ+ | mIoU, pAcc | CAUSE-TR: 21.2 mIoU on COCO-81 | Scalability | mIoU low on COCO-171 (15.2) |
| E7 | Ablation: Bank & CRF | Variants with/without bank/CRF (Table 4) | mIoU, pAcc | Bank + CRF: 41.9 mIoU; No bank + no CRF: 27.8 | Component contribution | No baseline CRF analysis |
| E8 | Ablation: Discretization method | K-Means, Spectral, Agglomerative, Ward vs Modularity | mIoU, pAcc | Modularity best (41.9 vs 33.7 for K-Means++) | Modularity advantages | No analysis of why modularity works better |
| E9 | Ablation: ϕ+ and ϕ- (Fig. 5) | ϕ+ varied 0.1->0.7, ϕ- varied 0.1->0.5 | mIoU, pAcc | Optimal ϕ+=0.3, ϕ-=0.1 | Threshold importance | No analysis of neutral zone |
| E10 | Ablation: k (Fig. 5) | k = 512, 1024, 2048, 4096 | mIoU, pAcc | Saturation at k=2048 | Sufficient capacity | k=4096 not tested on larger datasets |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Status | Gap |
|--------------------------|----------------|-----|
| New knowledge (causal USS framing) | Conceptual contribution present but causal justification has errors | Collider error and unexamined assumptions weaken the theoretical contribution |
| Reproducibility | Method described in detail; hyperparameters reported | Missing sensitivity analysis for key hyperparameters (bank ratio, τ, ϕ+/ϕ-) |
| Impact on practice/understanding | Strong empirical results, but limited to specific evaluation protocol | No OOD or domain-shift evaluation; unclear how method generalizes beyond IID benchmarks |

### Proposed Research Experiments (P0/P1/P2)

**P0-Exp1: Variance and significance testing**
- **Target Claim:** C3 (CAUSE achieves superior performance)
- **Hypothesis:** Reported gains are statistically significant
- **Minimal Design:** Run CAUSE-TR (ViT-B/8) on COCO-Stuff with 3 seeds
- **Controls:** Same seeds for STEGO and HP
- **Metrics:** mIoU (mean±std), paired t-test p-value
- **Success Criterion:** p < 0.05 for main comparison
- **Cost:** ~3 GPU-days
- **Expected Gain:** High — establishes statistical reliability

**P0-Exp2: CRF-free comparison**
- **Target Claim:** C3 (fair comparison)
- **Hypothesis:** CAUSE gains are not solely from CRF
- **Minimal Design:** Report mIoU for CAUSE, STEGO, HP without CRF post-processing
- **Controls:** Identical CRF settings for all methods
- **Metrics:** mIoU without CRF
- **Success Criterion:** CAUSE still outperforms baselines without CRF
- **Cost:** 1 GPU-day
- **Expected Gain:** High — clarifies gain attribution

**P0-Exp3: ϕ+ and ϕ- sensitivity sweep + neutral zone analysis**
- **Target Claim:** C2 (concept selection mechanism is effective)
- **Hypothesis:** Performance is stable within a reasonable ϕ+/ϕ- range
- **Minimal Design:** Sweep ϕ+ ∈ {0.2,0.3,0.4,0.5} × ϕ- ∈ {0.05,0.1,0.2} on COCO-Stuff with CAUSE-TR
- **Controls:** Fixed k=2048, bank ratio=50%
- **Metrics:** mIoU, avg #positives/negatives per anchor
- **Success Criterion:** mIoU variance < 2 points within [0.2,0.4]×[0.05,0.15]
- **Cost:** 2 GPU-days
- **Expected Gain:** High — establishes practical usability

**P1-Exp4: Tanh temperature τ ablation**
- **Target Claim:** C2 (modularity optimization is effective)
- **Hypothesis:** τ does not critically affect clusterbook quality
- **Minimal Design:** τ ∈ {0.01, 0.05, 0.1, 0.5, 1.0} on COCO-Stuff
- **Controls:** Fixed downstream SSL config
- **Metrics:** Downstream mIoU, cluster purity
- **Success Criterion:** mIoU variation < 1.5 points across τ values
- **Cost:** 1 GPU-day
- **Expected Gain:** Medium — fills methodological gap

**P1-Exp5: Concept bank replacement ratio and capacity**
- **Target Claim:** C2 (concept bank provides global views)
- **Hypothesis:** Performance is stable across bank configurations
- **Minimal Design:** Ratio ∈ {25%, 50%, 75%}, capacity b ∈ {50, 100, 200}
- **Controls:** Fixed k=2048, ϕ+=0.3, ϕ-=0.1
- **Metrics:** mIoU
- **Success Criterion:** mIoU variation < 1 point across configurations
- **Cost:** 1.5 GPU-days
- **Expected Gain:** Medium — improves reproducibility

**P2-Exp6: OOD generalization test**
- **Target Claim:** C3 (generalization capability)
- **Hypothesis:** CAUSE is robust to limited domain shift
- **Minimal Design:** Train on Cityscapes, evaluate on a different urban dataset without retraining
- **Controls:** STEGO and HP under same cross-dataset protocol
- **Metrics:** mIoU, relative performance drop
- **Success Criterion:** CAUSE shows smaller relative drop than baselines
- **Cost:** 1 GPU-day
- **Expected Gain:** Medium-Low — strengthens generalization claim but beyond current scope

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Must, ~6 GPU-days)          P1 (Should, ~4.5 GPU-days)       P2 (Nice, ~1 GPU-day)
│                                │                                │
├── Exp1: Variance (3 seeds)    ├── Exp4: τ ablation            └── Exp6: OOD test
├── Exp2: CRF-free comparison   ├── Exp5: Bank sensitivity       
├── Exp3: ϕ+/ϕ- sweep          │
│                                │
└── All P0 → revised Tables 1-4 └── All P1 → revised Appendix
    
Expected quality improvement if P0 completed:
  - Validity: from medium to high
  - Reproducibility: from medium-low to high  
  - Theoretical clarity: from medium to high
  - Overall score uplift: +1.5 to +2.0 points
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Reasoning:**
- **Research value (primary dimension): 6/10.** The causal framing of USS granularity is a genuine conceptual contribution, and the two-step decomposition is technically sound. However, the causal justification contains factual errors (collider misstatement) and relies on unverified assumptions, which reduces the theoretical contribution. The method is not fundamentally new in components (modularity clustering + contrastive learning are established), but their integration under a causal lens is novel.
- **Novelty: 7/10.** The causal approach to USS is novel in formulation. The paper presents a clean decomposition that prior USS methods lack. However, external verification is deferred in this run (Retrieval-Disabled Mode). The paper itself acknowledges related causal work in weakly-supervised segmentation (Zhang et al., 2020a), so the novelty is more in application domain than in causal methodology.
- **Validity/soundness: 6/10.** The empirical results are strong, but several validity concerns reduce the score: (a) no variance reporting, (b) CRF confound not controlled for baselines, (c) collider error in causal reasoning, (d) unexamined assumptions in the USS→frontdoor mapping. None of these are fatal, but collectively they reduce confidence.
- **Reproducibility: 7/10.** Method description is detailed with pseudocode and hyperparameters. Sensitivity to ϕ+/ϕ- and concept bank settings is a limitation, but the reported ablations provide some guidance.
- **Presentation: 6/10.** The paper is generally well-written but has structural issues (Related Work is chronological, Introduction could be more engaging, Conclusion lacks specificity). The causal diagram and architecture figure are clear.

**Post-Revision Target: [7.5, 8.0] / 10**

If all P0 items are addressed (collider correction, assumption catalog, claim qualification, variance reporting, ϕ+/ϕ- analysis, CRF-free comparison, τ ablation), the score would rise to approximately 7.5-8.0. The main uplift comes from fixing the theoretical errors and adding statistical rigor. If P1-P2 items are also addressed, the upper bound could reach 8.0.

**Scoring Breakdown:**

| Dimension | Weight | Current | Post-fix Target |
|-----------|--------|---------|-----------------|
| Research value / contribution | 30% | 6.0 | 7.5 |
| Novelty | 25% | 7.0 | 7.5 |
| Validity / soundness | 25% | 6.0 | 8.0 |
| Reproducibility | 10% | 7.0 | 8.0 |
| Presentation / clarity | 10% | 6.0 | 7.5 |
| **Weighted total** | **100%** | **6.4** | **7.7** |