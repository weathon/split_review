## Summary
# Final Review Report

## Summary

This paper, accepted at ICLR 2024, proposes three composition methods built on a fixed pretrained Motion Diffusion Model (MDM) to overcome data scarcity in human motion generation: (1) **DoubleTake** for zero-shot long-sequence generation through batched handshake and soft-masked transition refinement, (2) **ComMDM** for few-shot two-person interaction via a slim communication block between two frozen MDM priors, and (3) **DiffusionBlending** for fine-grained joint/trajectory control by generalizing classifier-free guidance to blend multiple fine-tuned models. The paper is technically solid, well-motivated by a genuine data bottleneck, and the three-method composition framework is conceptually appealing. The experiments cover multiple datasets (HumanML3D, BABEL, CMU-Mocap, 3DPW) with user studies supporting the proposed methods over baselines (TEACH, MRT). However, several issues reduce the paper's overall rigor: (1) the "first" claim for text-driven two-person generation is unverifiable without external literature (deferred), (2) the DiffusionBlending formula has theoretical gaps around the "alignment" assumption, (3) Algorithm 2 contains a critical notation error preventing reproducibility, (4) the inference cost vs. training efficiency trade-off is not discussed, and (5) the two-person text-to-motion experiment lacks quantitative evaluation. The paper's research value lies in demonstrating that a single pretrained diffusion model can be compositionally extended to multiple out-of-domain tasks with minimal additional data — a practical paradigm for data-scarce motion generation.

## Strengths
1. **Strong conceptual framing.** The paper's core idea — using a pretrained motion diffusion model as a generative prior for composition — is well-conceived and clearly communicated. The three-axis taxonomy (sequential, parallel, model composition) provides a principled organization that helps readers understand the design space.

2. **Zero-shot and few-shot practicality.** DoubleTake's ability to generate long coherent motion sequences without any training on long sequences, and ComMDM's ability to learn two-person interaction from as few as 10 training examples, demonstrate genuine practical value. The paper convincingly shows that composition at the diffusion sampling level can circumvent data scarcity.

3. **Comprehensive evaluation with user studies.** The paper includes multiple quantitative metrics (R-precision, FID, Diversity, MultiModal-Dist) across multiple datasets, plus user studies with 20-30 participants for both long-sequence (82-85% preference) and two-person tasks (64-79% preference over baselines). This is more thorough than typical for the field.

4. **Open and reproducible.** Code and trained models are publicly released, which is commendable and essential for the community to build upon this work.

5. **Applicability to multiple tasks.** Unlike most papers that address a single task, this paper tackles three distinct challenges (long sequences, multi-person interaction, fine-grained control) within a unified framework, increasing its potential impact.

## Weaknesses
1. **Algorithm 2 is not reproducible.** The sampling algorithm (Page 14, Appendix B) contains a critical notation error: `x(T)_0 = 0` sets the initial state to zero instead of sampling from N(0,I), and the loop variable `x(t)_0` conflates noise step and clean prediction notation. As written, the algorithm cannot be correctly implemented.

2. **Inference-time cost is high but unacknowledged.** DoubleTake's inference time is 78s for a 10s motion vs. TEACH's 5.7s (13.7x slower) and 15.7 minutes for a 5-minute motion (6.3x slower). The paper frames the method as "inexpensive" but the cost is in training data, not inference. This trade-off is not discussed in the main text (only in Appendix D).

3. **Two-person text-to-motion lacks quantitative evaluation.** Unlike the prefix completion task (with L2 error in Table 4 and user study in Figure 6), the text-to-motion experiment has no quantitative results — only qualitative figures and an admission that "generalization is fairly limited." The 5 textual annotations per sample lack quality control details.

4. **DiffusionBlending's alignment assumption is undertested.** The method generalizes classifier-free guidance but requires models to be "aligned" (architecture, noise schedule, data distribution). Fine-tuning for different joints likely breaks alignment, yet no diagnostic test is provided. The N-model formula also has a dimension mismatch (uses G_a for all n).

5. **Quality gap to ground truth is large but undiscussed.** Table 2 shows R-precision of 0.59 vs. ground truth 0.80 (26% gap) and MultiModal-Dist of 5.61 vs. 2.96 (89% gap) on HumanML3D. These gaps receive no analysis in the text.

6. **Related Work is organized as a list rather than a positioned comparison.** The section reads as three siloed literature surveys rather than an argument about why composition is needed and how this paper differs from prior work on each dimension.

7. **"First" claim for text-driven two-person motion is unverifiable.** The claim (Page 2) conflicts with acknowledged concurrent work (InterGen). Without external literature verification (currently unavailable), this claim should be downgraded.

8. **Conclusion overreaches.** The final paragraph introduces an untested claim about domain-agnostic applicability. The scaling expectation ("expect this approach to scale with larger datasets") is unsupported speculation.

## Key Issues
### Issue 1: Algorithm 2 Sampling Method is Not Reproducible (Critical)
- **Page 14 - Appendix B, Algorithm 2**
- **Severity:** Critical — blocks reproducibility
- **Evidence:** `x(T)_0 = 0` is an incorrect initialization (should be N(0,I)). The notation `x(t)_0` conflates the diffusion step index t with the clean prediction subscript 0, making the loop body ambiguous. The step `x(t-1)_0 = ε_θ(...)` does not match the standard DDPM posterior sampling.
- **Impact:** A reader cannot correctly implement the sampling procedure from the paper alone.
- **Fix:** Rewrite in standard DDPM notation (see annotation on Page 14 for corrected pseudocode).

### Issue 2: Two-Person Text-to-Motion Lacks Quantitative Validation (Major)
- **Page 9 - Section 4.2, "Text-to-Motion" paragraph
- **Severity:** Major — weakens the parallel composition contribution
- **Evidence:** The text-to-motion experiment for ComMDM reports no quantitative metrics — only qualitative figures and the caveat "generalization is fairly limited." Five textual annotations per sample were created without quality control details. The user study (Figure 6) covers prefix completion only.
- **Impact:** The parallel composition claim for text-to-motion is not empirically supported.
- **Fix:** Add quantitative evaluation using HumanML3D metrics (R-precision, FID, Diversity); report annotation quality metrics; perform systematic failure analysis.

### Issue 3: DiffusionBlending Theoretical Gap (Major)
- **Page 6 - Section 3.3, "DiffusionBlending" paragraph
- **Severity:** Major — threatens the validity of the model composition contribution
- **Evidence:** The method relies on "aligned" models (Wu et al., 2021) but provides no diagnostic test. The N-model formula uses G_a for all terms instead of G_n. The scale parameter s has no sensitivity analysis.
- **Impact:** Without alignment verification, readers cannot know whether blending degrades motion quality.
- **Fix:** Add alignment diagnostic, correct the N-model formula, and include s-sensitivity analysis.

### Issue 4: Inference Efficiency Trade-off Undiscussed (Major)
- **Page 7 - Section 4.1; Page 17 - Appendix D
- **Severity:** Major — framing mismatch
- **Evidence:** DoubleTake inference: 78s for 10s motion (13.7x slower than TEACH). This is only reported in Appendix D, not discussed in the main text.
- **Impact:** The claim of "inexpensive composition methods" is misleading without this context.
- **Fix:** Move the efficiency table to the main paper and add discussion of the training-vs-inference trade-off.

### Issue 5: Ground-Truth Quality Gap Unanalyzed (Minor)
- **Page 8 - Table 2
- **Severity:** Minor — transparency issue
- **Evidence:** R-precision 0.59 vs. GT 0.80 (26% gap), MultiModal-Dist 5.61 vs. GT 2.96 (89% gap).
- **Impact:** Readers may overestimate the quality of DoubleTake relative to ground truth.
- **Fix:** Add paragraph discussing the gap, including when it is most severe and potential mitigations.

## Actionable Suggestions
### S1. Fix Algorithm 2 for Reproducibility (Must)

**Problem:** Algorithm 2 (Page 14) uses incorrect initialization `x(T)_0 = 0` and conflates notation between clean prediction and noised state.

**Action:** Replace Algorithm 2 with the following corrected version:

```
Algorithm 2 Sampling with trajectory control
Input: Fine-tuned model ε_θ, trajectory τ, text condition c, noise schedule α_t
  x_T ~ N(0, I)                        ▷ Sample pure noise
  for t = T down to 1 do
    x̂_0 = ε_θ(x_t, t, c)               ▷ Predict clean motion
    x̂_0[trajectory] = τ                ▷ Inject control features
    ϵ ~ N(0, I)
    ϵ[trajectory] = 0                  ▷ Mask noise on control features
    x_{t-1} = √(α_{t-1}) · x̂_0 + √(1 - α_{t-1}) · ϵ   ▷ Forward step with noise masking
  end for
  return x_0
```

**Expected benefit:** Readers can implement the method without guessing the missing details.

### S2. Add Quantitative Results for Two-Person Text-to-Motion (Must)

**Problem:** The text-to-motion ComMDM experiment has only qualitative results and a generalization caveat.

**Action:** 
1. Run the HumanML3D evaluator on generated two-person motions (even if using a modified protocol).
2. Report at minimum: R-precision, FID, Diversity.
3. Add a "Failure Analysis" table categorizing interactions by whether ComMDM generates plausible motion (e.g., "same type as training" vs. "novel interaction type").
4. Report inter-annotator agreement for the 5 textual annotations per sample.

**Expected benefit:** Provides empirical ground for assessing the parallel composition claim.

### S3. Revise DiffusionBlending with Corrected Formula and Alignment Test (Must)

**Problem:** The N-model formula is wrong (uses G_a for all n), and alignment is untested.

**Actions:**
1. Correct the general formula to: `G^{[N]}(X_t, t, {c_n}) = Σ_{n=1}^{N} s_n · G_n(X_t, t, c_n)` with `Σ s_n = 1`.
2. Add an alignment verification experiment: measure feature cosine similarity between original MDM and each fine-tuned model at the layer where blending is applied.
3. Include a sensitivity analysis for the scale parameter s (try s ∈ {0.1, 0.3, 0.5, 0.7, 1.0}) and report control accuracy vs. motion naturalness.

**Expected benefit:** Validates that blending preserves motion quality and control accuracy.

### S4. Discuss Inference Cost vs. Training Efficiency (Must)

**Problem:** DoubleTake is 13.7x slower than TEACH at inference but the paper calls methods "inexpensive."

**Actions:**
1. Move Table 5 (Page 17) to the main paper (Section 4.1).
2. Add a paragraph explicitly comparing training cost (DoubleTake: zero training; TEACH: dedicated training) vs. inference cost.
3. Replace "inexpensive composition methods" with "training-efficient composition methods" throughout.
4. Report inference time as a function of key parameters: handshake length h, second take steps T', number of intervals.

**Expected benefit:** Prevents readers from misinterpreting the efficiency claims.

### S5. Acknowledge Quality Gap to Ground Truth (Nice-to-have)

**Action:** In Section 4.1, add: "While DoubleTake outperforms TEACH on transition FID, the overall motion quality still lags behind ground truth (e.g., R-precision: 0.59 vs. 0.80). This gap is most pronounced for fast or highly articulated motions, and narrowing it is an open challenge."

### S6. Restructure Related Work by Composition Type (Nice-to-have)

**Action:** Reorganize Section 2 into three subsections: (2.1) Sequential/autoregressive methods, (2.2) Multi-person coordination methods, (2.3) Controllable generation methods. Within each, explicitly state: (a) what prior work does, (b) its limitation, (c) how this paper's approach differs. See the annotation on Page 3 for a detailed outline.

### S7. Tighten Conclusion Scope (Nice-to-have)

**Action:** Remove the unsupported paragraph about domain-agnostic applicability. Keep only: validated findings, specific limitations with improvement directions, and concrete next steps. See the Mentor Revised Version in the annotation on Page 9.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: (P1) Big picture — diffusion + language models for motion, (P2) Data limitation, (P3) Our approach — using pretrained models as priors, (P4-P7) MDM choice and three composition methods, (P8) Summary claim. This arc is functional but has two weaknesses: (a) the problem statement (data scarcity) is introduced in P2 but the connection to composition is delayed until P3-P4, and (b) the three methods are enumerated rather than motivated by a unifying principle.

### Recommended Storyline: "Composition via Manifold Prior"

**Rationale:** This storyline foregrounds the core insight — a diffusion model trained on short single-person motion learns a manifold that can be reused for out-of-domain tasks via composition — and uses it to motivate each method as a natural consequence.

**Arc:** Big Picture (one sentence) → Data scarcity is structural, not incidental → Key insight: pretrained diffusion = manifold prior → Composition along three axes (time, agents, control) naturally extends the prior → Each axis solves a specific data-scarce task → Evidence preview → Contribution summary.

### Abstract Outline (Complete)

**S1 (Problem):** "Denoising diffusion models achieve high-quality text-driven human motion generation but are restricted to short, single-person sequences due to the expense and scarcity of annotated motion data."

**S2 (Gap):** "Tasks requiring long-horizon motion, multi-person interaction, or fine-grained joint control remain out of reach for existing data-driven approaches."

**S3 (Approach):** "We show that a pretrained motion diffusion model can serve as a generative prior for three forms of composition that overcome these data barriers: sequential (DoubleTake), parallel (ComMDM), and model composition (DiffusionBlending)."

**S4 (Key Results):** "DoubleTake generates arbitrarily long multi-action sequences with smooth transitions in a zero-shot manner, outperforming the trained baseline TEACH on transition FID (0.79 vs. 1.12). ComMDM learns two-person coordination from as few as 10 training examples and is preferred over MRT in 77-79% of user comparisons. DiffusionBlending enables fine-grained per-joint and trajectory control, reducing FID from 0.98 (inpainting baseline) to 0.54."

**S5 (Implication):** "Our results demonstrate that diffusion-based motion priors can be compositionally extended to multiple out-of-domain tasks without task-specific training, offering a practical paradigm for data-scarce motion generation."

### Introduction Outline (Complete)

**P1 (Stakes + Gap):** "State-of-the-art text-to-motion models produce high-quality short clips but are fundamentally limited by the data they are trained on. Motion capture is expensive, producing datasets that are small, homogeneous, and dominated by single-person sequences of 10 seconds or less. Long animations, multi-person interactions, and joint-level control cannot be addressed by scaling these models alone — the required annotated data does not exist at sufficient scale."

**P2 (Key Insight):** "This paper is based on a different premise: rather than collecting more data, we can reuse a pretrained motion diffusion model as a generative prior. A diffusion model trained on short single-person motion implicitly learns the human motion manifold. If we can compose this prior — by concatenating clips, coordinating multiple instances, or blending control signals — the manifold constraint keeps each component realistic without task-specific retraining."

**P3 (Method 1 — Sequential):** "Along the time axis, we introduce DoubleTake, a zero-shot method that generates arbitrarily long multi-interval sequences. Two diffusion samples with overlapping 'handshake' regions are generated simultaneously and blended at each denoising step, with a second soft-masking pass refining transitions. This achieves smooth transitions between semantically different actions without any training on transition data."

**P4 (Method 2 — Parallel):** "Along the agent axis, we introduce ComMDM for two-person interaction. Two frozen MDM instances are coordinated by a lightweight communication block that passes correction signals through intermediate transformer activations. This preserves each person's motion distribution while learning to synchronize, requiring as few as 10 interaction examples."

**P5 (Method 3 — Model Composition):** "Along the control axis, we introduce DiffusionBlending, which generalizes classifier-free guidance to combine multiple models fine-tuned for different joint-control tasks. This enables flexible combinations of trajectory and end-effector control without training a model for every joint combination."

**P6 (Contributions):** "We demonstrate, on BABEL, HumanML3D, CMU-Mocap, and 3DPW, that these composition methods outperform dedicated prior work. DoubleTake achieves 82-85% user preference over TEACH on long-sequence generation, ComMDM reduces prefix-completion error by 15-34% over MRT, and DiffusionBlending cuts FID by 2-4× compared to motion inpainting. Code and models are publicly available."

## Priority Revision Plan
### P0 — Must Fix (Publication-Critical)

| Order | Issue | Action | Effort | Impact |
|-------|-------|--------|--------|--------|
| 1 | Algorithm 2 sampling pseudocode incorrect | Rewrite with correct DDPM notation (see S1 in Actionable Suggestions) | Low | Critical — blocks reproducibility |
| 2 | DiffusionBlending N-model formula wrong | Correct to use G_n per model; add alignment diagnostic | Low | Major — fixes theoretical error |
| 3 | Two-person text-to-motion lacks quantitative results | Add HumanML3D evaluator metrics; report annotation quality | Medium | Major — validates parallel composition claim |
| 4 | Inference cost not discussed in main text | Move Table 5 to main paper; add trade-off paragraph | Low | Major — corrects framing |

### P1 — High Priority (Strongly Recommended)

| Order | Issue | Action | Effort | Impact |
|-------|-------|--------|--------|--------|
| 5 | "First" claim for two-person text-to-motion | Replace with bounded wording | Low | High — removes vulnerability |
| 6 | DiffusionBlending scale parameter untested | Add s-sensitivity analysis | Medium | Medium — validates blending |
| 7 | Quality gap to ground truth unanalyzed | Add analysis paragraph to Sec 4.1 | Low | Medium — improves transparency |
| 8 | Related Work is list-like | Restructure by composition type | Medium | High — improves positioning |

### P2 — Nice-to-Have (Quality Improvement)

| Order | Issue | Action | Effort | Impact |
|-------|-------|--------|--------|--------|
| 9 | Abstract lacks quantitative anchor | Incorporate key numbers from Storyline outline S4 | Low | Medium |
| 10 | Conclusion overreaches | Remove domain-agnostic claim; tighten limitations | Low | Medium |
| 11 | Handshake formula asymmetry not discussed | Add one-sentence explanation in Sec 3.1 | Low | Low |
| 12 | Introduction narrative can be tighter | Adopt recommended storyline (see Section 6) | Medium | Medium |

### Revision Cost-Benefit Analysis

The P0 fixes require approximately 2-3 days of work (rewriting Algorithm 2, correcting the formula, running evaluators on text-to-motion data, and adding the efficiency discussion). These directly address the most significant validity and reproducibility concerns. The P1 fixes add another 3-5 days but substantially improve the paper's scientific rigor and defensibility. All P0 and P1 items are feasible within a standard revision cycle.

```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Algorithm 2 fix] --> [Reproducibility restored]
[P0: DiffusionBlending formula] --> [Theoretical correctness]
[P0: Text-to-motion quant eval] --> [Parallel composition validated]
[P0: Inference cost discussion] --> [Honest efficiency framing]
        |
        v
[P1: "First" claim bounded] --> [Reduced vulnerability to rejection]
[P1: s-sensitivity analysis] --> [Blending mechanism validated]
[P1: GT gap analysis] --> [Transparent error characterization]
[P1: Related Work restructured] --> [Stronger positioning]
        |
        v
[P2: Tighten intro/conclusion] --> [Professional presentation]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 | DoubleTake long-sequence (BABEL) | 32-interval sequences, MDM trained on BABEL, compared to TEACH | R-precision, FID, Diversity, MultiModal-Dist (Table 1) | DoubleTake outperforms TEACH on transition FID (1.88 vs 3.86 at 70 frames) | C1 (Sequential composition) | R-precision (0.43-0.48) still below Ground Truth (0.62); DiffCollage not compared |
| E2 | DoubleTake long-sequence (HumanML3D) | Same parameters, HumanML3D evaluator | R-precision, FID, Diversity (Table 2) | DoubleTake best at FID 0.60, large GT gap unanalyzed | C1 | 26% R-precision gap to GT; ablation shows sensitivity to b and h |
| E3 | DoubleTake user study | 20 users, DoubleTake vs TEACH | Preference % (Figure 12) | 82-85% preference for DoubleTake | C1 | Limited to subjective quality |
| E4 | ComMDM prefix completion (CMU-Mocap) | 1-sec prefix, 3-sec completion, 55 training sequences | L2 root/joint error (Table 4) | ComMDM best at 0.24/0.32/0.43 m (1/2/3s root) | C2 (Parallel composition) | Small dataset (55 sequences); limited action types |
| E5 | ComMDM prefix completion user study (3DPW) | 30 users, ComMDM vs MRT vs MDM vs GT | Quality/Completion/Interaction preference (Figure 6) | ComMDM preferred 64-79% over MRT | C2 | 27 training sequences only; test set omitted as "noisy" |
| E6 | ComMDM text-to-motion | 100K steps, 5 annotations per sample | None (qualitative only) | "Fairly limited" generalization | C2 (text-driven variant) | **No quantitative evaluation** — critical gap |
| E7 | Single-joint control fine-tuning | HumanML3D, 80K steps, trajectory/left wrist | R-precision, FID, Diversity (Table 3) | Fine-tuned FID 0.54 (trajectory) vs MDM 0.98 | C3 (Model composition) | Only two joint types tested |
| E8 | DiffusionBlending composite control | Left wrist+trajectory, left wrist+right foot | R-precision, FID, Diversity (Table 3) | DiffusionBlending FID 0.22 vs MDM 1.18 | C3 | s=0.5 only; no sensitivity analysis; alignment untested |

### Research-Theme Gap Diagnosis

1. **New Knowledge (Weak):** The sequential and parallel composition methods are novel in their specific design, but the core insight (diffusion prior as manifold) is conceptually similar to prior inpainting and classifier-free guidance work. The two-person text-to-motion experiment is too preliminary to constitute robust new knowledge.

2. **Reproducibility (Weak):** Algorithm 2's notation error prevents exact reproduction. The 5 textual annotations per two-person sample are not detailed enough for independent replication. Code is released but the sampling algorithm as described is incorrect.

3. **Impact on Practice/Understanding (Moderate):** The demonstration that frozen diffusion priors can be composed for multiple tasks with few extra examples is practically valuable for the motion generation community. However, the high inference cost limits immediate deployment.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: DoubleTake Inference Cost Characterization

- **Target Claim:** C1 (DoubleTake is training-efficient)
- **Hypothesis:** DoubleTake's inference cost scales linearly with number of intervals and handshake length.
- **Minimal Design:** Measure inference time for N intervals ∈ {4, 8, 16, 32} with h ∈ {15, 30, 60} frames and T' ∈ {300, 500, 700}.
- **Controls:** Fix batch size, GPU model.
- **Metrics:** Wall-clock time, peak GPU memory.
- **Success Criterion:** Clear scaling trend enabling practitioners to predict cost.
- **Cost:** ~2 GPU-hours.
- **Expected Gain:** Replaces vague "inexpensive" claim with actionable efficiency characterization.

#### P0 Experiment: ComMDM Text-to-Motion Quantitative Evaluation

- **Target Claim:** C2 (text-driven two-person generation)
- **Hypothesis:** ComMDM achieves better-than-random text-motion alignment on seen interaction types.
- **Minimal Design:** Use HumanML3D evaluator (trained on single-person) on each person's motion separately; report per-person R-precision and FID.
- **Controls:** Compare to single MDM generating each person independently.
- **Metrics:** R-precision, FID, Diversity per person; interaction plausibility (new metric: joint contact distance < 10cm).
- **Success Criterion:** Per-person R-precision > 0.3 (random baseline) and FID < 2.0.
- **Cost:** ~5 GPU-hours including data preparation.
- **Expected Gain:** Transforms the text-to-motion claim from qualitative to quantitative.

#### P0 Experiment: DiffusionBlending Alignment Verification

- **Target Claim:** C3 (model composition via blending)
- **Hypothesis:** Fine-tuned models remain sufficiently aligned with the original MDM for blending to be effective.
- **Minimal Design:** Compute cosine similarity between original MDM and fine-tuned model activations at the output layer for 100 random noise inputs.
- **Controls:** Compare to two independently fine-tuned models on the same joint (expected low alignment).
- **Metrics:** Mean ± std cosine similarity.
- **Success Criterion:** Cosine similarity > 0.9 between original and fine-tuned; < 0.7 between different joint specializations.
- **Cost:** ~1 GPU-hour.
- **Expected Gain:** Provides empirical foundation for the blending method's theoretical assumption.

#### P1 Experiment: Handshake Length Sensitivity on Transition Quality

- **Target Claim:** C1 (robust to h)
- **Hypothesis:** h=30 (1 second) is near-optimal for most transitions.
- **Minimal Design:** Vary h ∈ {10, 20, 30, 40, 60} frames; compute transition FID for each.
- **Controls:** Same text prompts and random seeds across h values.
- **Success Criterion:** Non-monotonic relationship with optimal at h=30.
- **Cost:** ~3 GPU-hours.
- **Expected Gain:** Validates the claim that h=30 is robust.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Now):
  ├── E1: DoubleTake inference cost scaling
  ├── E2: ComMDM text-to-motion quant eval  
  └── E3: DiffusionBlending alignment test
        |
P1 (This week):
  ├── E4: Handshake length sensitivity
  ├── E5: Scale parameter s sensitivity
  └── E6: Ground-truth gap analysis
        |
P2 (Before submission):
  ├── E7: Failure-case analysis for ComMDM
  ├── E8: DoubleTake vs DiffCollage (theoretical)
  └── E9: User study for DiffusionBlending
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.0/10**

**Scoring rationale:**
- **Research Value & Novelty (5.5/10):** The compositional framework is conceptually appealing and practically relevant, but the individual components have prior-art overlap (diffusion inpainting, classifier-free guidance). The "first" claim for text-driven two-person motion is unverified without external literature access. The two-person text-to-motion experiment is too preliminary to constitute robust novelty.
- **Validity & Soundness (5.5/10):** Algorithm 2's notation error blocks reproducibility. DiffusionBlending's theoretical gap (alignment assumption) and incorrect N-model formula reduce confidence. The two-person text-to-motion lacks quantitative evaluation entirely.
- **Empirical Quality (6.5/10):** The prefix completion and long-sequence experiments are thorough with user studies. However, the quality gap to ground truth is undiscussed, and DiffCollage (closest concurrent work) is not compared.
- **Writing & Clarity (6.5/10):** The paper is generally well-written but the introduction could be tighter, the Related Work section is list-like, and the abstract lacks quantitative anchors.

The paper has genuine practical value and a strong conceptual core, but the reproducibility issue (Algorithm 2), the unaudited "first" claim, and the missing quantitative evaluation for the text-to-motion experiment prevent a higher score.

**Post-Revision Target: 7.5/10**

If all P0 fixes are completed (Algorithm 2 corrected, DiffusionBlending formula fixed and alignment tested, text-to-motion quantitative evaluation added, inference cost discussed), the paper would reach approximately 7.5/10. Full P0+P1 completion (including "first" claim bounded, Related Work restructured, GT gap analyzed) could bring it to 8.0/10. These targets assume that the corrected evaluations validate the core claims; if significant degradation is found, the score would be lower.