Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper presents 3DTrajMaster, a framework for controlling multi-entity 3D motion in video generation using 6DoF pose sequences (translation + rotation) as user-specified inputs. The key technical contributions are a plug-and-play object injector with gated self-attention that establishes entity-trajectory correspondences, a synthetic 360°-Motion Dataset with 54K videos, and domain adaptor + annealed sampling techniques to mitigate quality degradation from training on synthetic data.

## Strengths
1. **First to formulate and tackle multi-entity 6DoF motion control in video generation**: The paper provides a clear articulation of the limitations of 2D control signals (no z-dimension, no rotation) and demonstrates that no existing baseline (MotionCtrl, Tora, Direct-a-Video) offers 3D location + 3D orientation + entity-trajectory correspondence (Table 1). This is a genuine step forward in controllable video generation.

2. **Well-designed gated self-attention architecture with entity-wise addition**: The proposed object injector (Section 3.2) uses entity-wise addition of frozen text embeddings and learned pose embeddings, then fuses them via a gated self-attention layer initialized from 2D spatial self-attention. The ablation (Table 3) shows this design improves over cross-attention fusion (TransErr 0.398 vs. 0.453) and 3D self-attention placement (TransErr 0.398 vs. 0.427), providing concrete evidence for the design choices.

3. **Novel dataset construction pipeline that fills a critical data gap**: The 360°-Motion Dataset (Section 3.3) uses GPT-generated trajectory templates, 70 animated 3D assets, and 12 surrounding cameras on diverse UE platforms to produce 54K videos with ground-truth 6DoF. This directly addresses the data scarcity problem the paper identifies, and Table 3 shows training without domain mitigation ("w/o Domain Adaptor," FVD 2379.89 vs. 1546.15) leads to severe quality degradation, confirming the dataset's importance — and the need for the mitigation techniques.

4. **Effective domain adaptor + annealed sampling for synthetic-to-real quality**: The combination of a LoRA-based domain adaptor (trained to absorb UE style, then reduced via scalar α at inference) and annealed sampling (trajectory injection only in early steps) is shown to improve FVD substantially (Table 3: Full Model 1546.15 vs. w/o Annealed 1841.64 vs. w/o Domain Adaptor 2379.89). The approach is pragmatic and empirically validated.

5. **Fine-grained entity editing capability**: Figure 5 demonstrates that the entity-wise addition design decouples appearance from motion, enabling attribute editing (hair, clothing, accessories) within the same generated motion — a capability not shown in prior motion-control methods.

## Weaknesses

### Fatal
None.

### Major

1. **Quantitative trajectory accuracy is only measured on human entities, leaving the multi-entity claim partially unverified**: The paper explicitly states (Section 4.3) that "due to the absence of a pose estimator for open-world 4D objects, we limit our evaluation to only human objectives." The evaluation set (Section 4.4) consists of 100 pairs where "each pair has one human entity," meaning the quantitative results in Table 2 only reflect performance on the human entity within each multi-entity video. While qualitative examples (Fig. 4, Fig. 6) show non-human entities (animals, cars, fire) following trajectories, this is not sufficient to confirm precise 3D trajectory following for non-human categories — which is a central claim of the paper ("multi-entity" in the title, diverse entity categories in the contributions). The paper acknowledges this limitation but does not provide a proxy evaluation (e.g., 2D keypoint tracking, bounding box overlap) to bridge the gap.

2. **Uncontrolled backbone comparison with baselines**: The paper trains 3DTrajMaster on an "internal video diffusion model" (Section 4.1) while comparing against open-source methods (MotionCtrl, Tora, Direct-a-Video) that use different, likely weaker, base models. Table 2 shows dramatic improvements (TransErr 0.398 vs. 1.420, RotErr 0.277 vs. 1.057), but without controlling for the backbone, the magnitude of improvement cannot be cleanly attributed to the proposed components. The internal "Base T2V" row provides some control (showing the backbone alone fails at trajectory following), but it is not a trajectory-conditioned baseline. The paper also simplifies entity descriptions for baselines (Section 4.5) to prevent failures, which, while practical, raises further concerns about comparison fairness. An internal control study (proposed components vs. a trajectory-conditioned baseline on the same backbone) would substantially strengthen the claims.

3. **Evaluation test set is in-domain with training data**: Both training and evaluation use Unreal Engine-rendered scenes from the same platform types (city/MatrixCity, desert, forest, HDRI — Section 3.3, training; the evaluation uses GPT-generated locations of similar types — Section 4.4). The paper does not specify whether the evaluation uses held-out 3D scenes distinct from training, nor does it test on real-world video data. Given the paper's emphasis on "generalization ability" (abstract, introduction), the lack of any out-of-domain or real-world evaluation limits support for this claim.

4. **Domain adaptor training objective is not clearly specified**: Equation (4) uses the notation \(\hat{\epsilon}_{\theta_1}\) for the domain adaptor training objective, where \(\theta_1\) is defined as the object injector. However, the domain adaptor is trained first (50K steps, then frozen; Section 4.1), before the object injector \(\theta_1\) exists. The intended meaning is likely that the base model (without injector) is used during domain adaptor training, but the notation conflates \(\theta_1\) as both "base model" (during Step 1) and "base model + injector" (during Step 2). This ambiguity, combined with the garbled formatting of the expectation in Eq. (4), makes the exact training objective harder to reproduce.

### Minor

1. **Rotation accuracy decrease with annealed sampling is dismissed without sufficient analysis**: Table 3 shows that "w/o Annealed Sampl." yields _better_ RotErr (0.265 vs. 0.277 with the full model). The paper attributes this to "pose estimation errors" (Section 4.6), but this is an evident trade-off between quality and accuracy that deserves more thorough discussion or analysis, especially since trajectory accuracy is the paper's primary claimed contribution.

2. **Pose encoder downsampler is underspecified**: The pose encoder uses "interval sampling" along the temporal dimension (Section 3.2), described as resembling the VAE's causal encoding, but "interval sampling" of tensors is not a standard learned operation. The paper notes that 1D convolution layers gave "similar results" without quantification. This detail is important for reproducibility.

3. **Entity cap of ≤3 and lack of inter-entity interaction modeling**: The paper notes (Conclusion) that the model supports at most 3 entities and only global motions (no dancing, waving, or entity-entity interactions like "a man picking up a dog"). These are honestly stated but significantly limit the practical scope of the "multi-entity" framing.

### Trivial
None.

## Nice-to-Haves
- A proxy metric for non-human trajectory accuracy (e.g., projecting 3D trajectories to 2D and measuring alignment via a tracker or bounding box overlap) would directly address the most significant evidential gap.
- An internal control experiment — comparing a trajectory-conditioned baseline on the same backbone, keeping entity descriptions identical — would disentangle architecture effects from backbone effects.
- A small-scale real-world generalization study (e.g., applying 3D trajectories to a real video scene via inpainting or compositing) would strengthen the generalization claim.
- Ablation on the LoRA scalar α and annealed timestep Tc sensitivity, which the paper references to the appendix but would benefit from a main-text summary.

## Removed Points
- **"Comparison with baselines is fundamentally unfair" framed as a fatal flaw**: The harsh critic characterized this as a "methodological gap that undermines the validity of the quantitative claims." This is softened because (a) the "Base T2V" row provides an internal control showing the backbone alone fails at trajectory control, (b) the ablations in Table 3 are all on the same backbone, and (c) comparing against open-source baselines with their native backbones is standard practice in the generation literature. The criticism is valid but not fatal — it's retained as Major issue #2.
- **"Negative static trajectory conditioning" request**: The paper mentions this as an observation from the appendix. The harsh critic suggests it be explored further; this is a nice-to-have rather than a weakness.
- **"Statistical significance" complaint**: The test set has 100 pairs. Requesting confidence intervals is a reasonable suggestion but not standard for this type of generative benchmark evaluation. Downgraded to Nice-to-Have.
- **Criticisms about missing appendix content**: The appendix is stripped by the parser; these cannot be verified.
- **Generic formatting/style nitpicks from critics**: Removed per instructions.
- **Strength Finder claims about "importance of the problem"**: Generic; removed.
- **Strength Finder claim #3 about "large quantitative margin"**: Kept but qualified in the final review to reflect the backbone fairness concern.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a quantitative proxy evaluation for non-human entities (2D projection of 3D trajectories measured via object tracking or bounding box alignment) to support the multi-entity claim.
2. Re-implement one baseline on the same backbone (or add an internal controlled comparison where all methods share the same base model) to disentangle architecture from backbone effects.
3. Clarify the domain adaptor training objective notation in Eq. (4) — specifically, what model parameters θ₁ refers to during domain adaptor training versus object injector training.
4. Test at least one real-world out-of-domain scenario to support the generalization claim, or weaken the claim to match the evidence.
5. Provide more analysis of the rotation accuracy trade-off caused by annealed sampling.

Now let me assign the score using my calibration analysis.

**Round 1 bracketing**: I identified this paper sits between weak anchors (~3.25-3.4) and strong anchors (~7.6-8.5). The plausible range is 4.0-6.5.

**Round 2 narrowing**: Most relevant anchors:
- FreeTraj (5.5, Reject) — tuning-free 2D trajectory control. 3DTrajMaster has stronger novelty but weaker evaluation.
- PuppetMaster (5.33, Reject) — part-level dynamics with synthetic data. Similar data construction approach. Comparable.
- CamTrol (5.8, Accept/Poster) — training-free camera control. Stronger paper overall.
- Boosting Camera Motion Control (5.5, Reject) — analysis paper with limited novelty. 3DTrajMaster has stronger novelty.
- Ctrl-V (4.0, Withdrawn) — clearly weaker than 3DTrajMaster.

3DTrajMaster is stronger than Ctrl-V (4.0), comparable to FreeTraj (5.5) and PuppetMaster (5.33), and weaker than CamTrol (5.8, Accept). The evaluation gaps (human-only, in-domain, backbone fairness) prevent this from being an accept-level paper despite its genuine novelty. I place it at 5.0.

Score: 5.0 — borderline, with significant merits but evaluation gaps that need addressing before acceptance.

Decision: Reject (with a clear path to acceptance if the evidential gaps are addressed).

Wait, actually let me reconsider. At 5.0, should the decision be Reject or Accept? Given that similar-scored papers (FreeTraj at 5.5, PuppetMaster at 5.33, Boosting Camera Motion at 5.5) were all Reject, and CamTrol at 5.8 was Accept — 5.0 seems like Reject territory. The paper has real contributions but significant evaluation gaps that prevent acceptance in its current form.## Summary

This paper introduces 3DTrajMaster, a framework for controlling multi-entity 3D motion in video generation using 6DoF (translation + rotation) pose sequences per entity. The core technical contributions are: (1) a plug-and-play object injector with gated self-attention that establishes entity-trajectory correspondences while preserving the base model's prior, (2) a synthetic 360°-Motion Dataset with 54K videos from UE-rendered scenes, and (3) domain adaptor + annealed sampling to mitigate quality degradation from synthetic training data.

## Strengths

1. **First to formulate and tackle multi-entity 6DoF motion control in video generation.** Table 1 clearly shows that no existing baseline (MotionCtrl, Tora, Direct-a-Video) offers 3D location + 3D orientation + entity-trajectory correspondence — they all operate in 2D and cannot express the full 3D nature of motion. This is a genuine, well-scoped step forward in controllable video generation.

2. **Well-designed gated self-attention with entity-wise addition is empirically validated.** The object injector (Section 3.2) fuses frozen text embeddings and learned pose embeddings via entity-wise addition into a gated self-attention layer. The ablation (Table 3) shows this design outperforms cross-attention fusion (TransErr 0.398 vs. 0.453) and 3D self-attention placement (0.398 vs. 0.427), with measurable improvements in both accuracy and video quality.

3. **Novel dataset construction pipeline addressing a real data gap.** The 360°-Motion Dataset (Section 3.3) uses GPT-generated 3D trajectory templates, 70 animated assets, and 12 surrounding cameras on diverse UE scenes to produce 54K videos with ground-truth 6DoF. The severe degradation when training without the domain adaptor (FVD 2379.89 vs. 1546.15 in Table 3) confirms both the dataset's necessity and the importance of the mitigation techniques.

4. **Domain adaptor + annealed sampling effectively mitigates synthetic-domain degradation.** The LoRA-based domain adaptor (trained to absorb UE style, then reduced via scalar α at inference) combined with annealed sampling (trajectories dropped in later denoising steps) improves FVD substantially: Full Model 1546.15 vs. w/o Annealed 1841.64 vs. w/o Domain Adaptor 2379.89 (Table 3). This is a pragmatic, empirically validated solution to a known problem in synthetic-data training.

5. **Fine-grained entity editing is demonstrated.** Figure 5 shows that modifying human attributes (hair, clothing, accessories) works within the same generated motion, enabled by the decoupled entity-wise addition design — a capability not shown in prior motion-control methods.

## Weaknesses

### Fatal
None.

### Major

1. **Quantitative trajectory accuracy is measured only on human entities, leaving the multi-entity claim partially unverified.** The paper states (Section 4.3): "Due to the absence of a pose estimator for open-world 4D objects, we limit our evaluation to only human objectives." Each test pair contains one human entity (Section 4.4), so the quantitative results in Table 2 only reflect performance on the human entity within multi-entity videos. Qualitative examples (Fig. 4, Fig. 6) show non-human entities visually following trajectories, but this does not confirm precise 3D trajectory following for animals, cars, or natural forces — which is a central claim of the paper. The paper honestly acknowledges this limitation but provides no proxy evaluation (e.g., 2D trajectory projection measured via tracking or bounding box alignment) to bridge the gap.

2. **The comparison against baselines uses an internal backbone versus different open-source backbones.** The paper trains on an "internal video diffusion model" (Section 4.1, ~1B parameters) while comparing against MotionCtrl, Tora, and Direct-a-Video using their own native backbones. Table 2 shows dramatic margins (TransErr 0.398 vs. 1.420), but without controlling for the backbone, the magnitude of improvement cannot be cleanly attributed to the proposed components alone. The "Base T2V" row provides an internal control showing the backbone cannot do trajectory control, but it is not a trajectory-conditioned baseline. The paper also simplifies entity descriptions for baselines (Section 4.5) to prevent failures — a reasonable practice but one that further complicates fair comparison. An internal controlled study (comparing all trajectory-conditioned methods on the same backbone) would substantially strengthen the evidence.

3. **The evaluation test set is in-domain with the training data.** Both training and evaluation use the same UE platform types (city/MatrixCity, desert, forest, HDRI — Section 3.3). The evaluation uses "novel" pose templates and GPT-generated descriptions (Section 4.4), but does not specify whether it uses held-out 3D scenes distinct from training or tests on real-world video. Given that the paper emphasizes "generalization ability" (abstract, introduction), the lack of any out-of-domain or real-world evaluation limits support for this claim.

4. **The domain adaptor training objective notation is ambiguous.** Equation (4) uses \(\hat{\epsilon}_{\theta_1}\) for the domain adaptor loss, where \(\theta_1\) is defined as the object injector. However, Section 4.1 states the domain adaptor is trained first (50K steps) before the object injector (36K steps). The intended meaning is likely that the base model (without injector) is used during domain adaptor training, but the notation conflates \(\theta_1\) as "base model" and later as "base model + injector" without clarification. The expectation in Eq. (4) also appears garbled in the PDF extraction, further hindering reproducibility.

### Minor

1. **Rotation accuracy decreases with annealed sampling but is dismissed.** Table 3 shows "w/o Annealed Sampl." achieves *better* RotErr (0.265 vs. 0.277 with the full model). The paper attributes this to "pose estimation errors" without further analysis, but this is an evident quality-accuracy trade-off that deserves more discussion given that trajectory accuracy is a primary claim.

2. **The pose encoder's "interval sampling" is underspecified.** The downsampler (Section 3.2) is described as "interval sampling of tensors" — not a standard learned operation. The paper notes that 1D convolutions gave "similar results" without quantification. This detail matters for reproducibility.

3. **Entity cap of ≤3 and no inter-entity interactions.** The model supports at most 3 entities and only global motions (no dancing, waving, or entity-entity interactions like "a man picking up a dog" — Conclusion). These are honestly stated but significantly limit the practical scope.

### Trivial
None.

## Nice-to-Haves
- A proxy metric for non-human trajectory accuracy (e.g., projecting 3D trajectories to 2D and measuring alignment via a tracker) would directly address the primary evidential gap.
- An internal controlled experiment — a trajectory-conditioned baseline on the same backbone with identical entity descriptions — would disentangle architecture from backbone effects.
- A small-scale real-world generalization test would strengthen the generalization claim.
- Ablation on the LoRA scalar α and annealed timestep T_c sensitivity — referenced to appendix but would benefit from a main-text summary.

## Removed Points
- **"Comparison with baselines is fundamentally unfair" characterized as a fatal methodological gap**: This is softened because (a) the "Base T2V" row provides an internal control, (b) ablations in Table 3 use the same backbone, and (c) comparing across backbones is standard practice in the generation literature. Retained as Major issue #2 (weaker frame).
- **"Statistical significance not reported"**: Requesting confidence intervals for a 100-pair generative benchmark is reasonable but not standard practice for this setting. Moved to Nice-to-Have.
- **"Negative static trajectory conditioning should be explored"**: The paper mentions this as an appendix observation; it is a curiosity, not a weakness. Removed.
- **Generic Strength Finder claims about "importance of the problem"**: Removed per instructions — dropped strengths must lack specific content.
- **Missing appendix content criticisms**: The appendix is stripped by the parser; these cannot be verified.
- **Formatting/style nitpicks**: Removed per instructions (parser artifacts, not author errors).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a quantitative proxy evaluation for non-human entities — project 3D trajectories to 2D and measure alignment via a visual tracker or bounding box overlap.
2. Run a controlled comparison where all methods share the same backbone, or at minimum add a trajectory-conditioned baseline on the internal backbone.
3. Clarify the notation in Eq. (4): specify what θ₁ refers to during domain adaptor training (the base model before injector insertion) vs. during injector training.
4. Test at least one real-world or out-of-domain scenario, or temper the generalization claims to match the evidence.
5. Provide a brief analysis of the RotErr increase from annealed sampling rather than dismissing it via pose estimation error.

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/lvgsPjRtLM.md | 2.50 | R1 (weak) | VideoDiT — different task, clearly weaker paper |
| /home/wg25r/review_agent/human_reviews/w73feIekdO.md | 3.25 | R1 (weak) | Unrelated motion-vector tracking paper |
| /home/wg25r/review_agent/human_reviews/XYuWS3nrw3.md | 3.00 | R1 (weak) | Video diffusion timestep approach, limited novelty |
| /home/wg25r/review_agent/human_reviews/n6To2wAOKL.md | 4.00 | R2 (bracket) | Ctrl-V — bounding-box video gen for driving. Weaker novelty, no video results, simpler approach. 3DTrajMaster is clearly stronger in novelty and scope. |
| /home/wg25r/review_agent/human_reviews/KI1zldOFz9.md | 5.80 | R2 (bracket) | CamTrol — training-free camera control, accepted at poster. Better-evaluated (real data, multiple backbones) but addresses a different (camera, not object) problem. 3DTrajMaster has a harder problem setting but weaker evaluation. |
| /home/wg25r/review_agent/human_reviews/rDRCIvTppL.md | 5.50 | R2 (bracket) | Boosting Camera Motion Control — camera control analysis, rejected. Limited novelty. 3DTrajMaster has stronger novelty. |
| /home/wg25r/review_agent/human_reviews/CU7QfWJ6nC.md | 5.50 | R2 (bracket) | FreeTraj — tuning-free 2D trajectory control, rejected. Simpler (no training), but only 2D, no multi-entity. 3DTrajMaster has stronger novelty but weaker evaluation. Comparable overall. |
| /home/wg25r/review_agent/human_reviews/HCUksccuFx.md | 5.33 | R2 (bracket) | PuppetMaster — drag-based control with synthetic data, rejected. Similar in having a synthetic dataset. 3DTrajMaster is comparable. |
| /home/wg25r/review_agent/human_reviews/5a79AqFr0c.md | 5.50 | R2 (bracket) | ControlVideo — training-free controllable video gen, accepted poster. Better evaluated. |
| /home/wg25r/review_agent/human_reviews/0uFTqvQhML.md | 5.00 | R1 (middle) | MagicDrive3D — 3D street scene generation, withdrawn. |

**Round 1 bracket**: Between weak anchors (~3.0–3.4) and strong anchors (~7.6–8.5) → plausible range 4.0–6.5.

**Round 2 narrowing**: Compared against FreeTraj (5.5, Reject), PuppetMaster (5.33, Reject), CamTrol (5.8, Accept). 3DTrajMaster is clearly stronger than Ctrl-V (4.0), comparable to FreeTraj and PuppetMaster in overall quality, and weaker than CamTrol (which was accepted despite other issues). The evaluation gaps (human-only trajectory metrics, in-domain test set, uncontrolled backbone) prevent acceptance at the level of CamTrol, placing this paper among the borderline-reject papers with genuine contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>