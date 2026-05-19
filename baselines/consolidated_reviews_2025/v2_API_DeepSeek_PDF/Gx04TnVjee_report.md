## Summary
# Final Review Report

## Summary

This paper presents **3DTrajMaster**, a video generation framework that controls multi-entity 3D motions by conditioning on user-specified 6DoF pose sequences (translation + rotation) for each entity. The core technical contribution is a plug-and-play 3D-motion grounded object injector: it uses a frozen text encoder and a learnable pose encoder to project entity descriptions and 3D trajectories into a joint latent space, combines them via entity-wise addition, and fuses them into the video diffusion transformer through gated self-attention with zero-initialized residual scaling to preserve pretrained priors.

To overcome the lack of suitable training data with paired 3D trajectories, the authors construct a **360°-Motion Dataset** — 54,000 synthetic videos rendered from Unreal Engine using 70 3D assets, GPT-generated trajectories, and 12 surround cameras. A LoRA-based domain adaptor and an annealed sampling strategy are introduced to mitigate the synthetic-to-real domain gap.

Quantitative evaluation (limited to human entities due to pose estimation constraints) shows 3DTrajMaster achieves substantially lower trajectory error (TransErr: 0.398m, RotErr: 0.277°) compared to 2D baselines (MotionCtrl, Direct-a-Video, Tora). Qualitative results demonstrate control over diverse entity types and fine-grained attribute editing.

**Overall assessment:** The paper tackles a timely and well-motivated problem — 3D-aware multi-entity motion control in video generation. The proposed object injector architecture is technically sound and the synthetic dataset construction is a practical contribution. However, the evaluation has significant limitations: quantitative results cover only human entities, comparisons lack a 3D-aware baseline to isolate representation gain from architectural gain, novelty claims rely on "first" language that requires literature verification, and several methodological details (dimensional alignment in entity-trajectory fusion, domain adaptor mechanism) are underspecified. The paper would benefit from stronger empirical rigor, broader baselines, and tempered contribution claims.

## Strengths
1. **Well-motivated problem formulation.** The paper identifies a genuine limitation of existing 2D control signals for video generation — they cannot represent 3D rotation, depth ordering, or multi-entity binding. Moving from 2D control to 6DoF multi-entity 3D motion control is a natural and important research direction that aligns with downstream applications (virtual cinematography, interactive games, embodied AI).

2. **Clean architectural design.** The plug-and-play object injector with entity-wise addition and gated self-attention is conceptually simple and principled. The zero-initialized residual scaling (trainable β) is a practical design choice that preserves the pretrained video diffusion prior during early training, which is crucial for generalization. The entity-wise correspondence enforced by explicit per-entity embedding addition is a clear improvement over 2D methods that merge all trajectories into a single feature map.

3. **Comprehensive synthetic data pipeline.** The 360°-Motion dataset construction pipeline (3D assets → GPT-generated trajectories → UE rendering → multi-view capture) is a significant engineering contribution. The use of 12 evenly-surrounding cameras to capture 360° views, 96 trajectory templates, and integration of diverse 3D scenes provides a scalable template for future 4D motion dataset construction.

4. **Practical domain adaptation strategy.** The combination of a LoRA-based domain adaptor (to mitigate UE-style artifacts) and annealed sampling (to drop trajectory conditioning in later denoising steps) demonstrates awareness of the synthetic-to-real gap and provides a workable solution, even if the mechanisms require further clarification.

5. **Strong quantitative results on human motion.** The trajectory accuracy metrics (TransErr: 0.398m, RotErr: 0.277°) represent a large improvement over 2D baselines (e.g., Tora: TransErr 1.848, RotErr 1.471). Even accounting for the inherent advantage of 3D input, the decoupled entity-wise design demonstrably produces more accurate multi-entity motion control.

## Weaknesses
### W1. Quantitative evaluation limited to human entities only (Major, validity-critical)
The paper's central claim — controlling "multi-entity" 3D motions — is quantitatively evaluated only on human entities because "Due to the absence of a pose estimator for open-world 4D objects, we limit our evaluation to only human objectives" (Page 7, Sec. 4.3). This means all results for non-human entities (animals, cars, robots, natural forces shown in Figures 1, 4, 6) are purely qualitative. The quantitative superiority claimed in the abstract and conclusion is technically valid only for humans. Moreover, the human pose estimator (GVHMR) itself may introduce systematic errors on generated (potentially distorted) human figures, and these errors are not quantified.

### W2. Missing 3D-aware ablation baseline (Major, validity-critical)
The paper compares only against 2D methods (MotionCtrl, Direct-a-Video, Tora). There is no ablation that isolates the benefit of 3D trajectory input from the object injector architecture. For example, a simple baseline could extend a 2D method with depth-aware conditioning or add 3D location maps as extra input channels. Without this, readers cannot determine whether the large gains come from the richer 3D input representation or from the proposed injection architecture.

### W3. Unqualified novelty claims (Major, objectivity)
Contribution 1 states "We are the first to customize 6DoF multi-entity motion in 3D space for controllable video generation" (Page 3). This "first" claim requires broader literature verification (concurrent works like FreeTraj, object-level 3D control in gaming/rendering contexts). The claim should be qualified with "to our knowledge" and a specific scope boundary.

### W4. Synthetic dataset generalization gap (Major, robustness)
The 360°-Motion dataset contains only 70 assets in 2 categories (human, animal). The claimed generalization to cars, robots, and natural forces (Figure 4, Figure S11) relies on the base T2V model's prior, not on the proposed method's training. The surround camera setup introduces a confound between camera motion and object motion that is not discussed.

### W5. No variance or significance statistics (Moderate, reproducibility)
All metrics in Tables 2 and 3 are reported as point estimates without standard deviations, confidence intervals, or significance tests. The large FVD/FID values (>1500 FVD) are unusual and not contextualized. With multi-seed generation variance unknown, the statistical reliability of rankings is unverifiable.

### W6. Underspecified technical details (Moderate, reproducibility)
Key implementation details are ambiguous: (1) how entity embeddings (L_max×D) and trajectory embeddings (F̃×D) are aligned for "entity-wise addition" given different shapes; (2) how Z^{Pe} ∈ ℝ^{F̃×N×L_max×D} is concatenated with video tokens x_t; (3) the "domain adaptor" is just a LoRA fine-tuning with α adjustment, not a proper domain adaptation method.

### W7. Limitations section uses speculative solutions (Moderate, rigor)
The limitations paragraph (Page 10) states problems can be solved by "constructing more diverse 3D assets" or "more powerful video foundation models" — these are future aspirations, not honest assessments of current boundaries. Missing specific failure cases and reproducibility limitations (proprietary base model, synthetic-only training data).

### W8. Related work lacks analytical depth (Minor)
Both related work subsections (2D Guidance, 3D-aware Synthesis) read as paper lists rather than organized comparisons. Missing analytical axes that would clarify the paper's position. The 3D-aware section dismisses prior work too briefly without explaining why camera control cannot be adapted to object control.

## Key Issues
### Issue 1: Human-only quantitative evaluation undermines "multi-entity" claims (P0 Critical)
**Location:** Page 7 - Sec 4.3 Evaluation Metric; Page 10 - Table 2; Page 1 - Abstract  
**Root cause:** No open-world 6D pose estimator exists for non-human entities, forcing evaluation to humans only.  
**Risk:** The paper's central claim ("controlling multi-entity 3D motions") is quantitatively validated only for one entity type.  
**Fix:** (a) Add a tracking-by-matching metric for non-human entities (e.g., using optical flow + depth to verify trajectory alignment). (b) Run a human-annotation study on a subset evaluating perceived trajectory accuracy for non-human entities. (c) Explicitly acknowledge this as a scope limitation in abstract and conclusion.

### Issue 2: No 3D-aware baseline for controlled ablation (P0 Critical)
**Location:** Page 7 - Sec 4.2 Baselines; Table 2  
**Root cause:** All baselines are 2D methods; no ablation separates 3D representation benefit from injection architecture benefit.  
**Risk:** The large gains could be primarily from using 3D input rather than the proposed architecture.  
**Fix:** Add a simple 3D-aware baseline (e.g., project 3D trajectories into 2D+depth maps and condition a 2D method on depth). This isolates the contribution of the object injector.

### Issue 3: Unsupported "first" and "SOTA" claims (P0 Critical)
**Location:** Page 3 - Contributions; Page 1 - Abstract  
**Root cause:** Retrieval-Disabled Mode prevents literature verification.  
**Risk:** Claims may be rejected by reviewers who know relevant prior work.  
**Fix:** Qualify "first" as "to our knowledge, the first method to jointly control multi-entity 6DoF motion in video generation with explicit entity-trajectory binding." Replace "SOTA" with bounded wording: "substantially outperforms selected 2D baselines on the proposed evaluation benchmark."

### Issue 4: Missing statistical rigor (P1 Major)
**Location:** Table 2, Table 3  
**Root cause:** Point estimates without variance across seeds or inference runs.  
**Risk:** Rankings may not be statistically significant; reproducibility unverifiable.  
**Fix:** Report mean ± std over ≥3 seeds for all metrics. Add paired significance test (e.g., permutation test) between best baseline and proposed method.

### Issue 5: Domain adaptor and annealed sampling synergy unexplained (P1 Major)
**Location:** Page 6 - Sec 3.3, Page 7 - Algorithm 1  
**Root cause:** The domain adaptor (LoRA) and annealed sampling (drop trajectory condition late in inference) serve overlapping purposes but their interaction is not analyzed.  
**Risk:** It is unclear whether both components are necessary or if one suffices.  
**Fix:** Add ablation: (a) domain adaptor only, (b) annealed sampling only, (c) both. Report both quality metrics and trajectory accuracy for each.

### Issue 6: Entity-trajectory embedding fusion lacks dimensional specification (P1 Major)
**Location:** Page 5 - Matching Entity-Trajectory Pair paragraph  
**Root cause:** The paper says entity and trajectory embeddings are "expanded and combined through entity-wise addition" without specifying how tensors of different shapes (L_max×D vs F̃×D) are aligned.  
**Risk:** The method cannot be reproduced from the paper description alone.  
**Fix:** Provide explicit tensor shapes for each operation: "Z^e_n ∈ ℝ^{L_max×D} is broadcast along temporal axis to ℝ^{F̃×L_max×D}, then added to Z^P_n ∈ ℝ^{F̃×1×D}..."

### Issue 7: Proprietary base model limits reproducibility (P1 Major)
**Location:** Page 7 - Sec 4.1 Implementation Details  
**Root cause:** The method is trained on "our internal video diffusion model for research purposes (see Sec. A for more details)."  
**Risk:** Results cannot be independently verified or built upon.  
**Fix:** Release the base model weights or retrain on an open-source model (e.g., VideoCrafter2, AnimateDiff, or an open DiT-based video model). At minimum, state the exact base model architecture, training data, and license terms.

## Actionable Suggestions
### S1. Revise the title for clarity and scope
**Current:** "3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation"  
**Issue:** The title names the method but does not communicate the problem framing or contribution scope.  
**Suggested:** "3DTrajMaster: Controlling Multi-Entity 6DoF Motion in Video Generation with 3D Trajectory Conditioning"  
This title states the task (multi-entity 6DoF motion control), the input modality (3D trajectory conditioning), and the domain (video generation).

### S2. Add a non-human trajectory accuracy metric
**Location:** Page 7 - Sec 4.3  
**Action:** Instead of relying solely on 6D pose estimation (which fails for non-rigid entities), add a proxy metric: compute optical flow from generated video, back-project to 3D using estimated depth, and compare trajectory curvature/direction against the input trajectory using cosine similarity on displacement vectors. This provides quantitative evidence for non-human entity control.

### S3. Restructure Related Work around decision axes
**Location:** Page 3-4 - Sec 2  
**Action:** Replace paper-by-paper listing with three analytical axes: (a) **Control representation:** 2D vs 3D (sketches, boxes, points, pose, camera, object 6DoF), (b) **Entity binding:** single-entity vs multi-entity with explicit correspondence, (c) **Learning paradigm:** training-based vs training-free. This structure would make the gap immediately visible.

### S4. Clarify the "gated" mechanism
**Location:** Page 5 - Eq. (2)  
**Action:** Rename "gated self-attention" to "residual self-attention with learnable scale" unless a gating function (e.g., sigmoid-activated projection) is actually used. If β is just a learnable scalar, the term "gated" is misleading.

### S5. Provide reproducible implementation details
**Location:** Page 5 - Matching Entity-Trajectory Pair  
**Action:** Add explicit tensor shape transformations:
- Text encoder: e_n → Z^e_n ∈ ℝ^{L_max×D} (zero-padded, L_max=77 or similar)
- Pose encoder: P_n ∈ ℝ^{F×12} → Linear → ℝ^{F×D} → TemporalAvgPool(stride=4) → Z^P_n ∈ ℝ^{F̃×D}
- Entity-wise addition: broadcast Z^e_n along time → ℝ^{F̃×L_max×D}, add Z^P_n → ℝ^{F̃×L_max×D}
- Stack N entities → Z^{Pe} ∈ ℝ^{F̃×N×L_max×D}

### S6. Conduct multi-seed evaluation
**Location:** Page 10 - Table 2  
**Action:** Run all methods with 3 different random seeds. Report mean ± std for all metrics. Add a note on whether the relative ranking is consistent across seeds. This is standard practice for diffusion-based generation papers.

### S7. Add failure case analysis
**Location:** Page 10 - Conclusion/Limitations  
**Action:** Include a dedicated failure analysis paragraph discussing: (a) what happens when >3 entities are requested, (b) how the model handles entities with rapidly changing trajectories, (c) edge cases where the domain adaptor + annealed sampling fails (e.g., complex backgrounds, extreme motion).

### S8. Bound the generalization claims
**Location:** Page 1 - Abstract, Page 3 - Contributions  
**Action:** Replace "sets a new state-of-the-art in both accuracy and generalization" with "achieves substantial improvements in trajectory accuracy over 2D baselines on the proposed evaluation benchmark, with generalization to diverse entity types demonstrated qualitatively."

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction follows: [Broad controllable video generation context] -> [2D methods + their limitations] -> [Our focus: multi-entity 3D motion] -> [Three core questions] -> [Method summary] -> [Data challenge] -> [Contributions]. This is functional but the three core questions appear before the method is motivated, making the narrative somewhat disjointed.

### Option A (Recommended): Problem-Gap-Solution-Evidence
**Paragraph 1 (Stakes):** Open with the concrete limitation of 2D control for multi-entity scenarios, using a vivid example (e.g., "generating a video where a person walks past a turning car requires specifying 3D positions and rotations, which 2D sketches cannot capture").
**Paragraph 2 (Gap):** Review existing methods across two dimensions: 2D control (what they can do) and 3D-aware methods (what they focus on — mostly camera control). Identify the missing capability: multi-entity object-level 3D motion with entity binding.
**Paragraph 3 (Solution):** Present 3DTrajMaster — use 6DoF trajectories per entity, inject via gated self-attention with zero-init residual. Explain the intuition: explicit entity-wise correspondence preserves identity-motion binding.
**Paragraph 4 (Evidence + Contributions):** Preview quantitative (humans) and qualitative (diverse entities) results. List 3 contributions (not 4): (1) first 6DoF multi-entity control, (2) object injector architecture, (3) dataset + domain adaptation pipeline.

### Option B: Application-Driven (for broader impact venues)
Start with an application vignette (film post-production, game design), then identify the missing technical capability, then method, then results. This trades some technical depth for accessibility.

### Abstract Outline (Complete, 5 sentences)
- **S1 (Problem):** Controlling multi-entity motion in video generation is currently limited to 2D signals, which cannot represent 3D rotation, depth ordering, or entity-specific trajectories.
- **S2 (Gap):** Existing 2D methods collapse all motions into a single feature map, losing entity identity and 3D spatial relations.
- **S3 (Method):** We introduce 3DTrajMaster, which conditions on per-entity 6DoF pose sequences through a plug-and-play object injector with entity-wise embedding addition and gated self-attention, preserving the video diffusion prior via zero-initialized residual scaling.
- **S4 (Dataset):** To train this model, we construct the 360°-Motion dataset (54k synthetic videos) and introduce a domain adaptor with annealed sampling to mitigate synthetic-to-real quality degradation.
- **S5 (Result):** On human trajectory evaluation, 3DTrajMaster reduces translation error by 76% and rotation error by 81% relative to 2D baselines, while qualitative results demonstrate generalization to diverse entity categories.

### Introduction Outline (Complete, 4 paragraphs)
- **P1 (Motivation via limitation):** Open with concrete limitation — 2D signals cannot represent 3D rotation, depth, or multi-entity binding. Use a specific illustrative scenario. Close with: "This paper addresses the problem of controlling multi-entity 3D motions in video generation."
- **P2 (Gap analysis):** Briefly review 2D control methods → their success and limitation. Review 3D-aware methods → they focus on camera, not object. Identify the missing capability: entity-specific 3D motion with explicit binding. Pose the three research questions (representation, binding, generalization).
- **P3 (Proposed method):** Introduce 3DTrajMaster. Explain core ideas in plain language: (1) 6DoF trajectories per entity as input, (2) entity-wise addition to create joint embeddings, (3) gated self-attention with zero-init β to preserve prior. Mention dataset challenge and the two mitigation techniques.
- **P4 (Contributions):** List 3 scoped contributions: task formulation + benchmark, object injector architecture, synthetic dataset pipeline + mitigation techniques. Preview key results.

### Writing Style Notes
- Replace "we argue that" with direct statements (e.g., "2D control signals cannot fully express 3D motion because...").
- Replace "It is not surprising that ours significantly outperforms all baselines" (Page 10) with a more measured interpretation.
- Use concrete numbers in the abstract (e.g., "76% reduction in trajectory error" rather than "sets a new state-of-the-art").
- Remove "robust controller" from abstract unless robustness is directly tested.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[P0 Items - Must fix before resubmission]
    ├── Issue 1: Human-only evaluation → Add tracking-based metric for non-humans
    │   └── Expected: Quantitative evidence for multi-entity claim
    ├── Issue 2: No 3D baseline → Add depth-conditioned 2D baseline
    │   └── Expected: Isolate architecture benefit from representation benefit
    └── Issue 3: Unqualified "first"/"SOTA" → Temper language, add scope qualifiers
        └── Expected: Defensible claims, less reviewer pushback

[P1 Items - High impact, moderate effort]
    ├── Issue 4: Missing variance → Multi-seed evaluation with std reporting
    ├── Issue 5: Domain adaptor synergy ablation → 2x2 ablation experiment
    ├── Issue 6: Unspecified tensor shapes → Add explicit dimensional formulas
    └── Issue 7: Proprietary base model → State exact architecture or release weights

[P2 Items - Improvement but lower urgency]
    ├── W8: Related work restructuring → Organize by analytical axes
    ├── Limitations rewrite → Replace aspirational language with honest boundaries
    └── Abstract rewrite → Use concrete numbers, bounded claims
```

### Execution Order
1. **Week 1-2:** P0 items (metric for non-humans, 3D baseline, claim tempering). These directly affect acceptance criteria and require no new data collection.
2. **Week 3:** P1 experiment items (multi-seed evaluation, ablation studies). These require additional GPU compute but are parallelizable.
3. **Week 4:** P1 documentation items (tensor shapes, base model details). These require no experiments, only writing.
4. **Week 5:** P2 polish (related work, limitations, abstract). Integrate all changes into a clean manuscript version.

### Expected Impact After Fixes
- **Without fixes:** The paper's strong empirical claims may be rejected due to insufficient scope of evaluation and unverifiable novelty claims. Score potential: 4-5/10.
- **With all P0+P1 fixes:** The paper would have bounded but credible claims, quantitative support for non-human entities (via proxy metrics), statistical rigor, and full reproducibility specifications. Score potential: 7-8/10.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Single-entity trajectory accuracy | 44 pose templates, human-only eval via GVHMR | TransErr, RotErr | 3DTrajMaster: TransErr 0.456m, RotErr 0.319° | 3D trajectory conditioning improves accuracy | Human-only; no variance reported |
| E2 | Multi-entity trajectory accuracy | 72 two-entity + 16 three-entity pairs | TransErr, RotErr | 3DTrajMaster: TransErr 0.390m, RotErr 0.272° | Entity-wise design benefits multi-entity | Same limitation as E1 |
| E3 | Video quality comparison | Same test set | FVD, FID, CLIPSIM | FVD 1546.15, FID 96.75, CLIPSIM 33.77 | Acceptable quality with domain adaptor | FVD very high (>1500) without interpretation |
| E4 | Motion fusion design | Replace gated self-attn with cross-attn | Video quality + trajectory accuracy | Cross-attn fusion degrades both metrics | Gated self-attn is beneficial | Minimal degradation details |
| E5 | Domain adaptor effect | w/o domain adaptor | FVD, FID, CLIPSIM | FVD 2379.89 (worse) | Domain adaptor improves quality | Synthetic data reliance not eliminated |
| E6 | Annealed sampling effect | w/o annealed sampling | FVD, FID, CLIPSIM | FVD 1841.64 (worse) | Annealed sampling helps quality | Rotation accuracy slightly increases without it (0.265 vs 0.277) |

### Research-Theme Gap Diagnosis
- **New knowledge:** The paper demonstrates that 6DoF multi-entity control is feasible in video diffusion models. The key insight — entity-wise addition with gated self-attention — is novel but the evidence base is narrow (human-only quantitative).
- **Reproducibility:** Weakened by proprietary base model, lack of tensor shape details, and no public code release for the full pipeline.
- **Impact on practice:** Potentially significant for film/game content creation, but limited by ≤3 entities, synthetic-only training data, and no real-world video evaluation.

### Proposed Research Experiments

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Critical - Must do)
├── EX-A: Non-human trajectory accuracy proxy
│   ├── Hypothesis: Optical flow + depth back-projection can verify trajectory adherence
│   ├── Design: Extract RAFT flow + DepthAnything depth from generated video
│   ├── Metric: Cosine similarity between expected and observed 3D displacement
│   └── Cost: ~2 GPU-days for evaluation
│
├── EX-B: 3D-aware baseline for comparison
│   ├── Hypothesis: Adding depth as extra channel to 2D method partly bridges 3D gap
│   ├── Design: Project 3D trajectories to 2D+depth maps, condition e.g., ControlNet
│   ├── Metric: Same as Table 2
│   └── Cost: ~5 GPU-days for setup + evaluation
│
└── EX-C: Multi-seed variance reporting
    ├── Design: Run all methods × 3 seeds
    ├── Metric: mean±std for all Table 2/3 metrics
    └── Cost: ~3 GPU-days

P1 (High impact - Recommended)
├── EX-D: Entity ablation (N=1,2,3 with same compute budget)
│   ├── Goal: Verify scaling behavior of entity-wise injection
│   └── Cost: ~4 GPU-days
│
├── EX-E: Out-of-domain evaluation on real videos
│   ├── Gather real videos with tracked entities (e.g., MOT dataset)
│   ├── Use as background, overlay generated entities with 3D trajectories
│   └── Cost: ~5 GPU-days
│
└── EX-F: Prompt sensitivity test
    ├── Vary entity description detail (short vs long) and measure trajectory accuracy
    └── Cost: ~2 GPU-days

P2 (Nice-to-have)
└── EX-G: User study for perceptual trajectory accuracy
    ├── 50 users rate trajectory plausibility (1-5 Likert)
    └── Cost: ~$500 + 1 week
```

### Traceability
- **EX-A** → supports C1 (multi-entity claim) by extending evaluation beyond humans.
- **EX-B** → strengthens C2 (architecture) by isolating representation vs architecture benefit.
- **EX-C** → improves reproducibility, addresses all validity concerns about statistical reliability.
- **EX-D/E** → strengthens C4 (generalization) by demonstrating robustness to entity count and domain.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.5 / 10

**Reasoning (research value + novelty prioritized):**
The paper addresses a timely and well-motivated problem — 3D-aware multi-entity motion control in video generation — and contributes a clean architectural design (object injector with entity-wise addition and gated self-attention). However, the score is tempered by several critical limitations:

1. **Quantitative evaluation scope (validity risk):** Only human entities are quantitatively evaluated, but the paper's core claim is "multi-entity" control encompassing diverse categories. Non-human results are purely qualitative.
2. **Novelty verification deferred (novelty risk):** Due to Retrieval-Disabled Mode, the "first" claim for 6DoF multi-entity motion control cannot be verified against concurrent literature. The claim must be treated as unverified.
3. **Missing 3D-aware baseline (validity risk):** Without a depth-conditioned 2D baseline, the advantage of the object injector architecture over simply using 3D input cannot be isolated.
4. **No statistical rigor (reproducibility risk):** Point estimates without variance prevent assessing reliability of reported improvements.
5. **Research value:** Moderate-high. The task formulation and dataset pipeline are valuable contributions, but the evidence base is too narrow to fully establish the claimed capabilities.

### Post-Revision Target: [7.0, 8.0] / 10

**If all P0 + P1 items are addressed:** (1) non-human proxy metrics, (2) 3D-aware baseline, (3) tempered "first"/"SOTA" language, (4) multi-seed variance reporting, (5) explicit tensor shape specifications, (6) domain adaptor synergy ablation, the paper would have credible bounded claims with adequate empirical support, placing it in the 7-8 range.

**Upper bound (8.0):** Requires also demonstrating generalization to real-world video backgrounds (not just UE synthetic scenes) and releasing either code or an open-source base model for reproducibility.

**Lower bound (7.0):** Achievable with just P0 items + variance reporting, making claims defensible even if broader generalization remains future work.