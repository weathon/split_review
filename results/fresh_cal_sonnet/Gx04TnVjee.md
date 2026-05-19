Now let me run the calibration searches to determine an appropriate score.Let me read a couple of anchors to calibrate better.Initial bracket: **5–7**. The paper has clear novelty (first 6DoF multi-entity 3D motion control in video generation), a complete pipeline with dataset, architecture, and ablation — more substantial than score-4 papers. But evaluation gaps (human-only trajectory accuracy, information-asymmetric baselines) pull it below the 8+ tier. Let me narrow.Now I have enough data for calibration. Let me write the final review.

**Round 1 bracket: 5–7.** 3DTrajMaster is more ambitious (multi-entity object motion + dataset) than score-4 papers like Ctrl-V/MOTIONFLOW but clearly below the 8+ tier.  
**Round 2 narrowing:** VD3D (6.2) and CameraCtrl/I2VControl-Camera (6.5) are the closest anchors — all address 3D control in video generation, propose plug-and-play adapters on diffusion models, and have comparable evaluation rigor. 3DTrajMaster tackles a harder problem (multi-entity object vs. single camera) and makes a dataset contribution, but has notable evaluation gaps. This positions it at **6.5**, comparable to CameraCtrl and I2VControl-Camera.

---

## Summary

3DTrajMaster introduces the first framework for fine-grained 6DoF multi-entity 3D motion control in text-to-video generation. The core contribution is a plug-and-play object injector using gated self-attention that creates entity-wise correspondences between detailed text descriptions and per-entity 3D pose sequences. To overcome the absence of suitable training data, the authors construct the 360°-Motion Dataset (54,000 synthetic videos from 70 3D assets in UE environments), supplemented by a LoRA-based domain adaptor and an annealed sampling inference strategy to preserve video quality.

---

## Strengths

- **Novel task definition with concrete architectural novelty.** The paper is the first to control per-entity 6DoF (location + rotation) for multiple objects simultaneously in video generation. Table 1 makes the gap explicit: all prior methods (MotionCtrl, Tora, Direct-a-Video) operate on 2D projections and lack per-entity correspondence. The gated self-attention injector (Eq. 2) explicitly concatenates entity-trajectory bonded embeddings with video tokens and uses truncated attention, preserving the diffusion prior while grounding each entity to its trajectory.

- **Practical two-stage quality recovery.** The LoRA domain adaptor (Section 3.3) and annealed sampling (Algorithm 1, Section 3.4) are not just engineering flourishes — Table 3 shows removing either component degrades FVD (from 146 to 160/163), and Figure 5 shows clear UE-style bleed-through without the adaptor. This is a well-validated practical contribution.

- **Complete ablation study.** Table 3 compares gated self-attention vs. cross-attention fusion vs. placement after 3D self-attention, with domain adaptor on/off and annealed sampling on/off. The ablation structure is thorough and the dominant factors (domain adaptor, annealed sampling) are clearly identified.

- **Meaningful dataset contribution.** The 360°-Motion Dataset construction pipeline (70 3D assets × GPT-generated spline trajectories × 12 surrounding cameras × 4 UE platforms) directly addresses two known gaps: low entity diversity and the absence of reliable 6D pose estimation for non-rigid objects. The 54,000-video dataset at 384×672 resolution is a resource the community lacks.

- **Fine-grained entity editing capability.** Figure 4 demonstrates that 3DTrajMaster can modify human attributes (hair, clothing, gender, figure size) while preserving the same trajectory — a qualitative capability not achievable with prior 2D methods that fold entity descriptions into a single shared feature.

---

## Weaknesses

### Fatal
None.

### Major

- **Information-asymmetric baseline comparison.** Section 4.4 explicitly states: "we project the 3D pose trajectories onto 2D space" for baselines, and simplifies entity descriptions ("a man with messy black hair, tall frame, a red shirt" → "a man in red") because baselines "may fail to generate videos with detailed descriptions." The paper itself acknowledges "It is not surprising that ours significantly outperforms all baselines." The reported gains in Table 2 (e.g., RotErr 0.265 vs. 0.485 for Tora) reflect an information advantage, not solely an architectural advantage. Since the baselines architecturally cannot consume 3D input, a proper isolation of what the *3D signal itself* contributes (vs. the 3DTrajMaster architecture) is absent. The missing ablation would be a variant of 3DTrajMaster trained on projected 2D trajectories only, compared to the full 3D version and to the baselines — but this is not provided. Without it, the performance gap is structurally over-attributed to architectural innovation.

- **Trajectory accuracy limited to human entities, leaving the core multi-entity claim partially unsupported.** Section 4.3 explicitly states: "we limit our evaluation to only human objectives" because GVHMR is the only available estimator. Yet the evaluation dataset is designed with 72 two-entity and 16 three-entity pairs, and the paper's core claim is multi-entity control. The motion accuracy of the non-human entity in every multi-entity pair — animals, cars, robots — is never quantitatively verified. Given that the bulk of the paper's novelty is precisely the multi-entity dimension, this gap means the headline accuracy numbers (RotErr/TransErr) measure only the easiest and most-studied sub-task. A coarse proxy such as 2D projection error or video-based depth consistency for non-human entities would substantially strengthen the quantitative case.

### Minor

- **Generalization to unseen categories (cars, robots, natural forces) is demonstrated only qualitatively and its attribution is unclear.** The 360°-Motion Dataset covers only humans and animals (70 assets). Yet Figure 3 and the teaser show 3DTrajMaster controlling cars, robots, and abstract forces. These capabilities plausibly come from the base T2V model's priors rather than the injector training — the plug-and-play architecture "preserves the video diffusion prior" by design. The paper does not distinguish between what the injector learned and what transfers zero-shot from the 1B-parameter base model. Acknowledging this attribution would improve scientific precision.

- **Gated self-attention design choice is weakly validated by ablation.** Table 3 shows RotErr 0.265 (gated self-attn.) vs. 0.278 (cross-attention) and TransErr 0.121 vs. 0.119 — differences that are within the acknowledged noise margin of the GVHMR estimator (Section 4.5: "there exist errors in evaluating open-world human poses"). The FVD difference (146 vs. 160) is more meaningful. The ablation supports a modest qualitative advantage but does not strongly validate the specific architectural design choice.

- **Domain adaptor scaling parameter α is not specified in the main text.** Section 3.3 states it is set to "a small value" during inference, with the hyperparameter study deferred to the supplementary. Given that α directly controls the UE-style trade-off, the main text should state the chosen value.

### Trivial

- The evaluation set size is 100 pairs. While this follows conventions in the field, reporting results by entity count stratum (12 single, 72 two-entity, 16 three-entity) would show whether accuracy degrades with more entities — the most novel regime.

---

## Nice-to-Haves

- Train a 2D-only variant of 3DTrajMaster (dropping z from the pose encoder) and include it in Table 2 as an ablation row. This would directly quantify the value of the 3D representation over 2D within the same architecture, providing a cleaner argument than the current baseline comparison.
- Even a rough multi-entity trajectory accuracy metric (e.g., 2D projection error averaged over all entity types) applied uniformly across all 100 test pairs would substantially strengthen the multi-entity claim.
- A small out-of-distribution evaluation on real-world pose sequences (e.g., from mocap data) would substantiate the generalization claim beyond in-distribution GPT-generated trajectories.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic §Intro: "First to customize 6DoF multi-entity motion is not supported by survey of concurrent work."** The paper's related work does survey TC4D and SynCamMaster and distinguishes them (TC4D handles 4D generation from an object perspective; SynCamMaster handles camera synchronization, not object motion). The claim is adequately argued given the related work scope. **Removed** as insufficiently grounded.

- **Harsh critic: Entity-wise addition mechanism "not clearly justified."** The ablation in Table 3 compares the gated self-attention placement and fusion type. The entity-wise addition itself is described in Section 3.2 as forming "bonded entity-motion correspondences" — the mechanism is architecturally coherent, even if not formally proven. The weakness is real as a minor architectural clarity note, but has been retained above as part of the weak ablation finding; the standalone version is excessive. **Removed** as redundant.

- **Harsh critic: Dataset asset overlap means "effective diversity is substantially lower."** While true (70 assets → 54,000 videos), the dataset's purpose is to provide varied trajectory-entity combinations for training the injector, not to represent natural video diversity. Asset reuse is inherent to any synthetic dataset. **Demoted** — acknowledged as a minor note, not a standalone weakness.

- **Strength Finder: "Quantitative SOTA on trajectory accuracy"** as a standalone strength is retained only with the caveat of the information asymmetry noted above. The numbers are real but the interpretation is limited; this is reflected in the Major weakness rather than a pure strength.

- **Harsh critic: No confidence intervals.** Standard evaluation practice in video generation is single-run; this is not a meaningful departure. **Removed** per community standards.

- **Harsh critic: Base model opacity ("internal video diffusion model").** The paper provides that it is a ~1B parameter DiT-based T2V model. Opaqueness of internal research models is routine in industry-academic papers. This is not a scientific weakness. **Removed** as a reproducibility nitpick.

---

## Novel Insights

The paper's most underappreciated insight is the entity-wise addition operation as a binding mechanism: rather than jointly encoding all entity-trajectory pairs through shared cross-attention (which produces entanglement), the entity-trajectory binding is enforced *before* the attention operation, so each entity's text embedding and pose sequence are already fused into a single token stream that the gated self-attention then jointly attends to. This structural choice is what allows multi-entity occlusion handling (a man walking in front of a zebra) without requiring entity-specific masking — the positional disambiguation is handled by the binding step, not by the attention mechanism itself. This design principle may generalize to other multi-agent conditioning tasks.

---

## Suggestions

1. Add a 2D-only ablation row to Table 2 (drop z from pose encoder inputs, retrain); this is the single change that would most immediately clarify the paper's contribution.
2. Report TransErr and RotErr broken down by entity count (1-entity vs. 2-entity vs. 3-entity) to show whether accuracy degrades with multi-entity complexity.
3. Explicitly state the domain adaptor scaling value α in the main text, and note which capabilities come from the base T2V model vs. the trained injector (especially for cars/robots).
4. Consider adding even a single out-of-distribution evaluation example with real-world mocap trajectories to strengthen the generalization narrative.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| CCM-DiT (15lk4nBXYb) | 3.0 | R1 low | Much weaker — simple LoRA-based camera control on OpenSora, no dataset, limited scope |
| Mask-Guided Video (9GNTtaIZh6) | 3.0 | R1 low | Much weaker — single GPU, limited 2D mask guidance |
| MOTIONFLOW (OBTmkKBmQW) | 4.0 | R1 mid | Weaker — camera trajectory via implicit pixel flow, no 3D entity control |
| Ctrl-V (n6To2wAOKL) | 4.0 | R1 mid | Weaker — 2D bounding box object control only, single entity focus |
| Training-free Camera (KI1zldOFz9) | 5.8 | R1 mid | Weaker scope — training-free single-camera only, no object motion |
| I2VControl-Camera (AcAD4VEgCX) | 6.5 | R1 mid | Comparable — camera+subject motion control, plug-and-play, similar evaluation rigor |
| VD3D (0n4bS0R5MM) | 6.2 | R2 | Comparable — 3D camera control for DiT, novel application but limited technical novelty per reviewers |
| CameraCtrl (Z4evOUYrk7) | 6.5 | R2 | Comparable — first camera pose control for T2V, plug-and-play module, dataset study, similar structure |
| HOI-Diff (ZYwLfi50GI) | 5.25 | R2 | Weaker — 3D human-object interaction synthesis but no video generation, limited evaluation |
| TANGO (LbEWwJOufy) | 8.5 | R1 high | Stronger — mature framework, multiple novel components, thorough evaluation with real datasets |
| MovingParts (QQ6RgKYiQq) | 8.0 | R1 high | Stronger — NeRF-based 4D reconstruction, fundamentally different task, rigorous evaluation |

**Bracket reasoning:** R1 placed the paper 5–7. R2 anchors (VD3D 6.2, CameraCtrl 6.5, I2VControl-Camera 6.5) provide sharp comparisons. 3DTrajMaster addresses a harder problem (multi-entity object vs. single camera), makes a dataset contribution, and includes a more complete pipeline — but the evaluation design is weaker than CameraCtrl (which had clean SfM-based camera accuracy, not information-asymmetric baselines). On balance, the contributions are roughly equal to CameraCtrl/VD3D in maturity. The novelty of the task and dataset slightly favors the upper end of the comparable cluster.

**Final score: 6.5 — Accept.**

The paper makes a genuine, novel contribution to a hard and understudied problem, with a complete technical pipeline and an honest dataset contribution. The evaluation gaps (information-asymmetric baselines, human-only trajectory accuracy) are real weaknesses but do not invalidate the contribution — they limit interpretability of the quantitative claims. For a new task where no direct comparators can accept the same signal, some degree of asymmetry is unavoidable; the paper's own hedging ("it is not surprising...") shows awareness. The core architectural insights and qualitative results support the paper's claims even absent a cleaner ablation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>