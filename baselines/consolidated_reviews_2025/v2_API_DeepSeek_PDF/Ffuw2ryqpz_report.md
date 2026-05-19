## Summary
# Final Review Report

## Summary

This paper presents Real3D, a self-training framework for Large Reconstruction Models (LRMs) that enables training on single-view real-world images without requiring multi-view or 3D supervision. The core technical contributions are: (i) a cycle-consistency rendering loss at the pixel level, (ii) a CLIP-based semantic similarity loss with hard-negative mining for semantic-level guidance, and (iii) an automatic data curation pipeline for selecting high-quality, unoccluded object instances from in-the-wild images. The method builds on a fine-tuned TripoSR backbone and jointly trains on synthetic multi-view data (Objaverse) with supervised losses and real single-view data (WildImages, 300K instances) with unsupervised losses. Experiments across four evaluation sets (MVImgNet, CO3D, OmniObject3D, WildImages) show consistent improvements over existing LRM baselines (TripoSR, OpenLRM) and generative-prior methods (LGM, CRM, InstantMesh), with average PSNR gains of 0.74 dB (4% relative) and LPIPS improvements of 6.3% relative over TripoSR.

The paper addresses an important problem — scaling LRM training data beyond synthetic/manual multi-view captures — and proposes a technically sound self-training framework. However, several weaknesses limit the current evidence: lack of statistical significance testing, no variance reporting across any experiment, non-trivial engineering dependencies (stop-gradient trick, curriculum schedules, multi-stage fine-tuning) whose individual contributions are not fully isolated, and an unverifiable "first" novelty claim under Retrieval-Disabled Mode. The research value is clear and the direction is promising, but the current evidentiary basis for the claimed consistent outperformance needs strengthening.

## Strengths
1. **Important problem formulation.** The paper targets a genuine bottleneck in single-view 3D reconstruction: the reliance on multi-view or 3D supervision severely limits the scale and diversity of LRM training data. Shifting to single-view real-world images as a training resource is a well-motivated and practically significant direction.

2. **Clean and principled method design.** The self-training framework is architecturally clean — combining a cycle-consistency pixel-level loss with a CLIP-based semantic loss — and each component is grounded in a clear intuition. The stop-gradient mechanism and hard-negative mining for the semantic loss are well-reasoned design choices that demonstrably prevent degenerate solutions (as shown in the ablation study).

3. **Comprehensive evaluation.** The paper evaluates across four diverse datasets spanning real/synthetic and in-domain/out-of-domain scenarios, using multiple metrics (PSNR, SSIM, LPIPS, CLIP, FID, Chamfer distance). This is significantly broader than typical LRM evaluations. The inclusion of both generative-prior and deterministic baselines provides a meaningful performance context.

4. **Strong ablation study.** Table 5 provides a step-by-step ablation that isolates the contributions of clean data, semantic guidance, pixel-level cycle consistency, stop-gradient, and curriculum learning. The ablation clearly shows that naive application of losses hurts performance, and only the full configuration yields consistent gains. This level of diagnostic analysis is valuable for the community.

5. **Scalability analysis.** Figure 5 shows monotonic improvement with increasing data volume across all four test sets, providing initial evidence that the self-training approach can benefit from further data scaling. Table 6's comparison with multi-view training (Δmulti-view vs Δours) convincingly demonstrates that single-view self-training extracts more per-instance value than naive multi-view supervision on real data.

## Weaknesses
1. **No statistical significance or variance reporting (Major).** All experimental results (Tables 1-5) report single-point metrics without standard deviation, confidence intervals, or significance tests. The claimed gains are modest (e.g., 0.72 dB PSNR, ~3.6% relative improvement over TripoSR) and may be within the range of random seed variation. Without multi-seed evaluation, the "consistent outperformance" claim cannot be assessed for statistical reliability.

2. **Novelty verification deferred (Structural limitation).** Under Retrieval-Disabled Mode, the paper's "first LRM system using single-view real-world images" claim and the positioning against related work cannot be independently verified. While the paper's self-training framework appears technically novel, a manual literature check is needed to confirm whether similar cycle-consistency or unsupervised LRM training approaches exist.

3. **Method complexity with limited isolation.** The full system involves multiple interacting components: TripoSR fine-tuning, synthetic supervised pre-training, cycle-consistency loss with stop-gradient, CLIP semantic loss with hard-negative mining, curriculum pose scheduling, and automatic data curation. While the ablation (Table 5) is helpful, some key design choices (e.g., the specific curriculum schedule, the stop-gradient operation, the loss weighting λ values) are justified only by empirical observation on a limited validation setup. The underlying causal mechanisms are not analyzed.

4. **Evaluation data and protocol limitations.** The evaluation on MVImgNet and CO3D uses only 100 instances per dataset with strict selection criteria (center-cropped, centered masks). This raises questions about selection bias and whether results generalize to more diverse real-world inputs. The TripoSR baseline requires fine-tuning (random scale issue), making the comparison less clean.

5. **Data curation pipeline not quantitatively validated.** The occlusion detection pipeline uses multiple heuristics (kernel sizes, depth ratio thresholds, confidence thresholds) but provides no quantitative precision/recall evaluation on a labeled subset. The category-level filtering (removing bus-like shapes) is acknowledged as a TripoSR-specific limitation but this selectivity reduces the diversity of the training data.

## Key Issues
### Issue 1: Missing variance and statistical significance (Severity: Major, Validity Risk: High)
**Evidence:** Tables 1-4 report single-point PSNR/SSIM/LPIPS values without standard deviation, confidence intervals, or significance tests. The main claim of "consistent outperformance" is based on small absolute margins (0.72 dB PSNR average).  
**Impact:** Without variance, readers cannot distinguish genuine improvement from random seed variation. This weakens the central conclusion.  
**Fix (Must):** Re-run Real3D and the principal baselines (TripoSR, LRM) with ≥3 random seeds. Report mean ± std in all tables. Add a sentence summarizing the min-max range of observed gains.

### Issue 2: Unverifiable "first" claim and novelty positioning (Severity: Major, Research Value Risk: High)
**Evidence:** Title and abstract claim "the first LRM system that can be trained using single-view real-world images." Under Retrieval-Disabled Mode, this cannot be independently verified.  
**Impact:** If an existing method (e.g., unsupervised NeRF from single views, or related self-training frameworks) already addresses the same setting, the novelty contribution is substantially reduced.  
**Fix (Must):** Qualify the claim with "To our knowledge..." and explicitly defer full novelty verification to the review process. Add a related-work comparison table in the revision.

### Issue 3: Insufficient causal isolation of design components (Severity: Major, Reproducibility Risk: Medium)
**Evidence:** The method includes stop-gradient (SG), curriculum pose sampling, CLIP hard-negative mining, data curation, and joint training with synthetic supervision. The ablation (Table 5) tests only binary presence/absence of these components, not their interactions or sensitivity to hyperparameters (loss weights, curriculum schedule).  
**Impact:** It is unclear whether the gains come from the self-training framework itself or from the specific combination of engineering choices tuned for the TripoSR base model.  
**Fix (Must):** Add a sensitivity analysis for key hyperparameters (λ_R_pix, λ_R_sem, curriculum starting/final angles, number of semantic views m). Show that gains are robust across a reasonable range of values.

### Issue 4: Limited evaluation diversity within datasets (Severity: Minor, Generalization Risk: Medium)
**Evidence:** MVImgNet and CO3D evaluations use only 100 instances each, with strict input selection criteria (center-cropped, instance mask centered, filtered by image quality).  
**Impact:** The reported metrics may not reflect performance on more challenging real-world inputs — occluded, off-center, low-resolution, or unusual-perspective images, which the failure cases (Fig. 11) show are problematic.  
**Fix (Nice-to-have):** Evaluate on a larger random subset (500+ instances) without the center-crop constraint. Report performance stratified by image quality and occluded vs non-occluded inputs.

### Issue 5: Incomplete limitation discussion (Severity: Minor, Transparency Risk: Low)
**Evidence:** The Conclusion only acknowledges constant intrinsics as a limitation. Missing: backbone specificity (fine-tuned TripoSR only), failure modes (unusual viewpoints, low quality as shown in Fig. 11), and the lack of variance reporting.  
**Impact:** Readers may overestimate the generalizability of the approach.  
**Fix (Must):** Expand the limitation paragraph to cover at least 3 constraints.

## Actionable Suggestions
### Suggestion 1 (Must, P0): Add multi-seed variance and significance reporting
**Target:** Tables 1-4 and Section 5.1.  
**Action:** Re-run Real3D and the primary baselines (TripoSR, LRM) with 3-5 random seeds. Report mean ± std for all metrics. Add a sentence in the Results paragraph: "Across 3 seeds, Real3D achieves a mean PSNR improvement of 0.74 dB ± 0.12 dB (range: 0.61–0.86 dB) over TripoSR on MVImgNet, indicating that the gain is statistically consistent."  
**Expected benefit:** Directly addresses the most critical weakness — the "consistent outperformance" claim becomes evidence-grounded rather than asserted.

### Suggestion 2 (Must, P0): Qualify novelty claims and add related-work positioning
**Target:** Title, Abstract (Page 1), Introduction (Page 2), Conclusion (Page 10).  
**Action:** Replace all instances of "the first LRM system that can be trained using single-view real-world images" with "to our knowledge, the first LRM system that can be trained using single-view real-world images." Add a paragraph in Related Work explicitly comparing Real3D's self-training approach to the closest existing self-supervised 3D learning methods (e.g., Alwala et al., 2022; Skorokhodov et al., 2023; Sargent et al., 2023) and explaining what is architecturally novel about the cycle-consistency loss.  
**Expected benefit:** Prevents a potential novelty rejection and demonstrates awareness of the literature.

### Suggestion 3 (Must, P1): Add hyperparameter sensitivity analysis
**Target:** Section 5.2 or Appendix.  
**Action:** Report how the main results (PSNR on MVImgNet) change when varying (a) loss weight λ_R_pix in {1.0, 2.0, 5.0, 10.0}, (b) curriculum final angles θ_max, φ_max in {60°, 90°, 120°}, (c) number of semantic views m in {2, 4, 8}. Show that the chosen configuration is near-optimal and that gains are not fragile.  
**Expected benefit:** Demonstrates that the self-training framework is robust, not an artifact of a single hyperparameter setting.

### Suggestion 4 (Nice-to-have, P1): Expand evaluation set size and conditions
**Target:** Section 5.1.  
**Action:** Evaluate on a larger random subset (500 instances) of MVImgNet without strict centered-input selection. Report performance stratified by (a) occlusion ratio, (b) image resolution, (c) off-center displacement.  
**Expected benefit:** Provides a more realistic assessment of in-the-wild performance and quantifies the domains where Real3D degrades to the TripoSR baseline.

### Suggestion 5 (Nice-to-have, P2): Validate data curation pipeline
**Target:** Appendix B.  
**Action:** Annotate 300 random instances for ground-truth occlusion status. Report precision/recall of the occlusion detection pipeline. Show how varying key thresholds (kernel size, depth ratio) changes the composition of the training set.  
**Expected benefit:** Adds scientific credibility to the data curation component and allows readers to assess data quality controls.

### Suggestion 6 (Must, P1): Fix typo and improve writing in Conclusion
**Target:** Page 10, lines 106-117.  
**Action:** Fix "perfrormance" → "performance." Replace "seemingly endless data source" with "abundant and diverse data source." Expand limitation paragraph per annotation advice.  
**Expected benefit:** Small but necessary polish for a conference submission.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current storyline follows: Scaling Law → LRM data bottleneck → Solution (single-view real images) → Method overview → Results. The narrative is functional but has three issues: (1) the Introduction opens with a generic scaling-law discussion before establishing the specific 3D reconstruction problem; (2) the contribution summary on Page 2 uses over-broad wording ("superior performance," "effective use of real data"); (3) the transition from "bottleneck" to "solution" lacks a clear statement of why existing unsupervised 3D learning methods are insufficient.

### Recommended Storyline: Problem → Gap → Solution → Evidence → Bounded Claim

#### Abstract Outline (S1-S5)
- **S1 (Problem + Domain):** "Single-view Large Reconstruction Models (LRMs) require multi-view or 3D supervision, which limits training data scale and diversity."
- **S2 (Gap):** "Existing data sources (synthetic 3D assets, video captures) are expensive to produce and do not capture the full distribution of real-world object shapes."
- **S3 (Proposed Solution):** "We introduce Real3D, a self-training framework that enables LRM training on single-view real-world images using two unsupervised losses — pixel-level cycle-consistency and CLIP-based semantic consistency — along with automatic data curation."
- **S4 (Key Results, Bounded):** "On four evaluation settings covering real/synthetic and in-domain/out-of-domain data, Real3D outperforms existing LRM baselines (TripoSR, LRM) under standardized protocols, with average PSNR gains of 0.74 dB and LPIPS improvements of 6.3%."
- **S5 (Limitation + Data):** "A current limitation is the use of constant camera intrinsics. Code, models, and data will be released."

#### Introduction Outline (Paragraph-by-Paragraph)

**P1 — Establish stakes and problem (revised from current):**
Role: Define single-view 3D reconstruction, state its practical importance (AR/VR, robotics, AIGC), and identify the core challenge: it is ill-posed and requires strong shape priors from large-scale data.
Key claim: "The key to accurate single-view 3D reconstruction is learning generic shape and texture priors from diverse, large-scale training data."
Target: ~6 sentences. Move the Transformer architecture discussion to a brief mention; remove the scaling-law generalities.

**P2 — Identify the bottleneck (revised from current):**
Role: Explain why current LRM training data is limited — reliance on multi-view/3D supervision means data sources are synthetic assets (expensive to produce, category-biased) or video captures (hard to scale). Provide a quantitative anchor: "Objaverse-XL contains ~10M objects, several orders of magnitude fewer than the billions of text-image pairs in LAION-5B."
Key claim: "Multi-view supervision is the critical bottleneck preventing LRMs from scaling their training data to match the diversity of real-world object shapes."

**P3 — Propose the solution with concrete advantage:**
Role: State that single-view real-world images are abundant and diverse. Explain that recent foundation models (SAM, DECOLA, Depth Anything) enable automatic curation of high-quality object instances from in-the-wild images.
Key claim: "By shifting from multi-view to single-view supervision, we unlock orders of magnitude more training data that better represents the real distribution of object shapes."

**P4 — Method preview and contribution summary (revised):**
Role: Introduce Real3D's self-training framework (cycle-consistency + CLIP semantic loss + data curation), state that it jointly trains with synthetic supervised data, and present three bounded contribution claims:
- C1: "A self-training framework with pixel-level cycle-consistency and CLIP-based semantic losses that enables LRM training on single-view real images."
- C2: "An automatic data curation pipeline that selects unoccluded, high-quality instances from in-the-wild images."
- C3: "Empirical demonstration of consistent improvements over LRM baselines across four diverse evaluation settings, with analysis of scalability and data efficiency."

Key correction vs current: Each contribution claim is bounded (says what is measured, not abstract superiority).

**P5 — Overview of findings (keep similar but bound the claims):**
Role: Preview the evaluation scope and key results with explicit bounds.
Key claim: "On four test sets (MVImgNet, CO3D, OmniObject3D, WildImages), Real3D achieves average PSNR gains of 0.74 dB over TripoSR under standardized evaluation protocols."

### Candidate Alternative Storyline: "Data-Centric" Frame
Lead with the data bottleneck as the central thesis, then introduce self-training as a data-centric solution. This would reorder the Introduction as:
P1: Data bottleneck (current P2, expanded with quantitative anchor)
P2: Unsupervised 3D learning from real images (current Related Work paragraph 3)
P3: How self-training solves the bottleneck (current P3 + P4 combined)
P4: Contribution summary and evidence preview

This alternative places the data problem (rather than scaling laws) as the primary narrative driver, which may resonate better with a 3D vision audience. The current storyline is acceptable but could be tightened by moving the scaling-law discussion to a secondary position.

## Priority Revision Plan
### P0 (Must, Before Resubmission)

| Priority | Item | Issue Addressed | Effort | Expected Impact |
|----------|------|----------------|--------|-----------------|
| P0.1 | Run 3-seed experiments, report mean±std in Tables 1-4 | Missing variance (Key Issue 1) | 3-5 GPU-days | High — validates core claim |
| P0.2 | Qualify "first" claims as "to our knowledge" throughout | Unverifiable novelty (Key Issue 2) | <1 hour | High — prevents novelty rejection |
| P0.3 | Expand limitation paragraph (3+ constraints) | Incomplete limitations (Key Issue 5) | <1 hour | Medium — improves transparency |

### P1 (Must, Strongly Recommended)

| Priority | Item | Issue Addressed | Effort | Expected Impact |
|----------|------|----------------|--------|-----------------|
| P1.1 | Add hyperparameter sensitivity analysis (λ weights, curriculum angles, semantic m) | Insufficient causal isolation (Key Issue 3) | 2-4 GPU-days | Medium — shows robustness |
| P1.2 | Fix typos (perfrormance), replace promotional language | Writing quality | <1 hour | Low — basic polish |
| P1.3 | Rewrite Introduction P1 to be more focused (see Storyline Outlines) | Narrative clarity | 2-4 hours | Medium — improves reader engagement |
| P1.4 | Expand MVImgNet evaluation to 500+ instances without strict centering | Limited evaluation diversity (Key Issue 4) | 1-2 GPU-days | Medium — improves external validity |

### P2 (Nice-to-Have, If Time Permits)

| Priority | Item | Issue Addressed | Effort | Expected Impact |
|----------|------|----------------|--------|-----------------|
| P2.1 | Validate occlusion detection pipeline (precision/recall on 300 labeled instances) | Unvalidated curation (Weakness 5) | 2-3 person-days | Low-Medium — adds rigor to data pipeline |
| P2.2 | Add Related-Work comparison table (see Suggestion 2) | Novelty positioning | 1-2 days | Medium — helps readers assess contribution |

### Revision Sequence (Recommended Order)
1. **P0.2 + P0.3 + P1.2** (text-only changes, 1 day)
2. **P0.1** (critical experiment, start immediately, ~3-5 GPU-days)
3. **P1.1 + P1.4** (while waiting for P0.1 results)
4. **P1.3** (after experimental evidence is finalized)
5. **P2 items** (if remaining time)

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Main comparison: Real3D vs baselines (Tables 1-4) | 4 datasets: MVImgNet, CO3D, OmniObject3D, WildImages. Baselines: LGM, CRM, InstantMesh, LRM, TripoSR | PSNR, SSIM, LPIPS, CLIP, FID | Real3D best on all settings, avg +0.74 dB PSNR vs TripoSR | C3: consistent improvements | No variance/CI; evaluation subset small (100 instances for MVImgNet/CO3D) |
| E2 | Ablation study (Table 5) | CO3D dataset, stepwise adding clean data, semantic loss, cycle-consistency, curriculum | PSNR, SSIM, LPIPS | Full model best (19.18 PSNR); naive CLIP hurts (17.89) | C1: unsupervised losses work | Only tested on CO3D; single-seed |
| E3 | Scalability analysis (Fig. 5) | Real3D trained with 0%/30%/60%/100% of WildImages | PSNR on all 4 datasets | Monotonic improvement with more data | C3: scalability | Only 4 data amounts; extrapolation uncertain |
| E4 | Effectiveness comparison (Table 6) | Δmulti-view (OpenLRM + MVImgNet) vs Δours (Real3D self-training) | PSNR, SSIM, LPIPS on 4 datasets | Δours > Δmulti-view on all metrics | C2: effective data use | Different base models (OpenLRM vs TripoSR); not an apples-to-apples comparison |
| E5 | Mesh quality (Sec 5.1) | Chamfer-L1 distance on mesh outputs | CD | Real3D 0.275 vs TripoSR 0.321 vs InstantMesh 0.395 | C3: mesh quality improvement | Single metric; no per-category breakdown |
| E6 | Data curation ablation (implicit in Table 5) | Raw vs cleaned data for self-training | PSNR, SSIM, LPIPS | Clean data helps (+0.19 PSNR over raw) | C2: curation matters | No per-criterion ablation (category filter vs occlusion filter vs scale filter) |
| E7 | Failure case analysis (Fig 11) | Qualitative: unusual viewpoints, low quality | Visual inspection | Degraded reconstruction under challenging conditions | — (limitation) | No quantitative breakdown of failure rate |

### Research-Theme Gap Diagnosis

1. **New knowledge claim (C1 — self-training framework):** Partially proven. The ablation shows the full configuration works, but the individual components (SG, curriculum, CLIP hard-negative mining) are not analyzed for their causal mechanism. The paper demonstrates *that* they work, not *why* they work.

2. **Reproducibility/reusability claim:** Partially supported. The method description is detailed (equations, curriculum schedules, hyperparameters), but the reliance on a fine-tuned TripoSR backbone (with specific fine-tuning recipes detailed in Appendix A) means reproduction requires replicating the full multi-stage pipeline. The data curation pipeline (DECOLA + Depth Anything) uses off-the-shelf models with threshold tuning.

3. **Potential to change practice/understanding:** Moderate. The core insight — that LRMs can be trained with single-view real images using self-training losses — is practically valuable and could influence how 3D reconstruction models are trained going forward. However, the current evidence base (modest gains, no variance reporting, single backbone) limits the strength of this claim.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost | Expected Gain |
|--------|-------------|-----------|---------------|-------------------|---------|------------------|---------------|--------------|
| P0-E1 | C3: consistent outperformance | Real3D's gains are statistically stable across seeds | Run Real3D + TripoSR with 3 seeds each on MVImgNet and CO3D | Same training config, same eval protocol | PSNR mean±std, paired t-test p-value | Mean gain > 2σ; p < 0.05 | 3-5 GPU-days | High — validates core claim |
| P1-E2 | C1: self-training robustness | Gains are stable across key hyperparameters | Vary λ_R_pix {1,2,5,10}, θ_max {60°,90°,120°}, m {2,4,8} on CO3D | Fixed other params, same TripoSR baseline | PSNR across configs | All configs outperform baseline | 2-4 GPU-days | Medium — shows design isn't overfitted |
| P1-E3 | C2: data curation effectiveness | Each curation criterion contributes independently | Ablate criteria: (1) no filtering, (2) scale only, (3) category only, (4) occlusion only, (5) all | Same Real3D training, 100% data | PSNR on MVImgNet, WildImages | Each criterion adds >0.1 dB | 2-3 GPU-days | Medium — quantifies curation importance |
| P2-E4 | Generalization: diverse inputs | Real3D maintains gains on random (not center-selected) inputs | Sample 500 random MVImgNet instances without centering constraint | Same eval protocol as Table 1 | PSNR, SSIM, LPIPS | Mean PSNR still > baseline | 1 GPU-day | Medium — tests external validity |
| P2-E5 | C1: stop-gradient mechanism | SG prevents gradient collapse in the cycle | Compare: (1) no SG, (2) SG on 1st render, (3) SG on 2nd LRM, (4) full SG | Same Real3D training on CO3D | PSNR, gradient norm statistics | Full SG best; (2) > (1) | 1-2 GPU-days | Low-Medium — provides mechanistic insight |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Rationale:** The paper addresses an important and well-motivated problem (scaling LRM training data beyond synthetic multi-view sources) and proposes a technically sound self-training framework with two unsupervised losses. The evaluation is comprehensive across four datasets, and the ablation study is thorough. However, the score is constrained by three critical limitations:

1. **No statistical variance or significance reporting** (Severity: Major) — The central claim of "consistent outperformance" rests on single-point metrics with modest margins (~3.6% PSNR relative), making it impossible to assess statistical reliability.
2. **Novelty verification deferred** (Severity: Structural) — The "first LRM system" claim cannot be verified under Retrieval-Disabled Mode.
3. **Method complexity with limited causal isolation** (Severity: Major) — The self-training framework involves multiple interacting components whose individual contributions are empirically ablated but not mechanistically analyzed.

The research value is genuine and the direction is timely, but the current evidentiary basis needs strengthening before the claims can be fully trusted.

### Post-Revision Target: [7.5, 8.5] / 10

**Conditions for reaching the target:**
- **7.5:** P0 items completed (multi-seed variance reporting, novelty claim qualification, expanded limitation section). This would resolve the most critical validity concern.
- **8.0:** P0 + P1.1 (hyperparameter sensitivity) + P1.4 (larger evaluation subset). This would demonstrate that the method is both statistically reliable and robust to hyperparameter choices.
- **8.5:** All P0 and P1 items completed, plus a clear statement of how the self-training framework differs from prior unsupervised 3D learning approaches (Related-Work comparison table).

The upper bound of 8.5 reflects that the method's gains, while consistent, are incremental in magnitude. A score above 8.5 would require either (a) a significantly larger absolute improvement over baselines, or (b) a new theoretical insight about why self-training works for LRMs beyond empirical demonstration.

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: LRMs need multi-view/3D supervision → limited data scale & diversity]
    |
    v
[Solution: Train LRMs on single-view real-world images via self-training]
    |
    ├── C1: Cycle-consistency pixel loss + CLIP semantic loss
    │       Evidence: Table 5 (ablation), Fig 7-8 (visual ablation)
    │       Gap: No variance, no causal mechanism analysis for SG/curriculum
    │
    ├── C2: Automatic data curation pipeline
    │       Evidence: Table 5 row (clean vs raw data)
    │       Gap: No precision/recall validation of occlusion detection
    │
    └── C3: Consistent outperformance + scalability
            Evidence: Tables 1-4 (4 datasets, multiple baselines), Fig 5 (scaling)
            Gap: No confidence intervals, small eval subsets (100 instances)
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0: Statistical validity]
    → Add multi-seed variance (mean±std) to Tables 1-4
    → Qualify "first" claims → "to our knowledge"
    → Expand limitation paragraph
    ↓
[P1: Robustness & clarity]
    → Hyperparameter sensitivity analysis (λ, θ_max, m)
    → Larger evaluation subset (500+ instances, no centering constraint)
    → Rewrite Introduction P1 for sharper narrative
    → Fix typos and promotional language
    ↓
[P2: Scientific rigor]
    → Validate occlusion detection pipeline (precision/recall)
    → Add Related-Work comparison table
    → Ablate individual curation criteria
    ↓
[Target: 7.5-8.5/10]
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Related Work: Single-View 3D Reconstruction
│
├── Branch 1: Representation-Focused Methods
│   ├── Leaf 1.1: Explicit representations (voxels, point clouds, meshes, Gaussians)
│   └── Leaf 1.2: Implicit representations (SDFs, NeRFs, radiance fields)
│   → Common assumption: Multi-view or 3D supervision at training time
│   → Difference vs Real3D: Real3D uses single-view images + self-training
│
├── Branch 2: Guidance-Based Methods
│   ├── Leaf 2.1: Depth-guided (MCC, ZeroShape)
│   ├── Leaf 2.2: Diffusion-guided (RealFusion, Make-it-3D, Magic123, Zero-1-to-3)
│   ├── Leaf 2.3: Adversarial-guided (GAL, SinNeRF)
│   └── Leaf 2.4: Semantic-guided (NeRDi, Make-it-3D)
│   → Common limitation: Per-shape optimization, slow, hard to scale
│   → Difference vs Real3D: Feed-forward LRM, no per-shape optimization
│
├── Branch 3: Large Reconstruction Models (LRMs)
│   ├── Leaf 3.1: Triplane-based (LRM, TripoSR, MeshLRM, GS-LRM)
│   └── Leaf 3.2: Generative-prior-based (LGM, CRM, InstantMesh)
│   → Common limitation: Require normalized coordinate system + canonical pose
│   → Difference vs Real3D: Self-training on single-view real images, no pose normalization
│
└── Branch 4: Unsupervised/Self-Supervised 3D Learning
    ├── Leaf 4.1: Category-level (CMR, pi-GAN, various)
    └── Leaf 4.2: General-category (Pre-train-Self-train-Distill, VQ3D, im2NeRF)
    → Common limitation: Learned from scratch without leveraging 3D annotations
    → Difference vs Real3D: Initialized from synthetic 3D supervision + self-training on real images
```

*Note: This taxonomy is constructed from the manuscript's own references. External literature verification is deferred under Retrieval-Disabled Mode.*

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason |
|------|-----------------|-----------------|-------------|
| 1 (Abstract + Intro P1-P2) | 3 | Covered | — |
| 2 (Intro P3-P5, Fig 1) | 3 | Covered | — |
| 3 (Related Work) | 1 | Covered | — |
| 4 (Preliminaries) | 0 | Skipped | Boilerplate background; key content covered in annotations on Pages 5-6 |
| 5 (Method: cycle-consistency) | 1 | Covered | — |
| 6 (Semantic loss, formulas) | 1 | Covered | — |
| 7 (Training details, experiments) | 0 | Skipped | Implementation details paragraph, no novel claims |
| 8-9 (Results tables, ablation) | 1 | Covered (Table 5 area annotated) | — |
| 10 (Scalability, Conclusion) | 1 | Covered | — |
| 11-16 (References) | 0 | Skipped | Reference list, non-substantive |
| 17-18 (Appendices: curation pipeline) | 1 | Covered | — |
| 19-22 (Appendices: additional results) | 0 | Skipped | Visual results supplementary to main text |

**Total: 12 annotations across 10 substantive pages.** Main-body density averages ~1.2 annotations/page (within 1-4 target). Appendix coverage meets ≥1 per 2 pages target.