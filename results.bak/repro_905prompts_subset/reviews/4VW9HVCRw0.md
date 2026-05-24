Now let me write the final consolidated review.

## Summary

This paper introduces the task of **free-form hand-object interaction (HOI) generation** — moving beyond the grasp-centric paradigm that has dominated prior work. The authors contribute **(1) WildO2**, a large-scale in-the-wild 3D HOI dataset (4,414 interactions across 92 intents, 610 object categories) built from internet videos via an automated O2HOI frame-pairing pipeline, and **(2) TOUCH**, a three-stage framework combining contact map prediction (separate CVAEs for hand and object), a multi-level conditioned diffusion model with coarse-to-fine semantic and geometric conditioning, and a physical refinement stage with cycle-consistency loss. Experiments show TOUCH outperforms adapted baselines (ContactGen, Text2HOI) on contact accuracy, physical plausibility, diversity, and semantic consistency.

## Strengths

- **First large-scale 3D HOI dataset for non-grasping interactions.** WildO2 covers actions like pushing, poking, and rotating — fundamentally beyond the grasp-centric datasets (GRAB, HO4D, OakInk) that have constrained prior work. With 92 intents and 610 object categories, this is a meaningful resource for the community (Section 3, Figure 3).

- **Clear quantitative outperformance on all metrics.** In Table 1, TOUCH improves over the best baseline (Text2HOI) on contact accuracy (P-IoU 0.776 vs. 0.711), penetration depth (PD 0.932 vs. 1.239), diversity (Entropy 2.93 vs. 2.85), and semantic consistency (P-FID 4.13 vs. 15.72, VLM score 7.1 vs. 6.5). These gains are consistent across the board.

- **Comprehensive ablation study that validates each design choice.** Table 2 systematically ablates the contact prediction modules (✗ hoc.: P-IoU drops from 0.728 to 0.492), the multi-level conditioning (✗ mul.: 0.728→0.525), the refiner (✗ refiner: 0.728→0.513), the cycle loss (✗ L_cycle: 0.728→0.702), and each text level (✗ T_DSC: 0.728→0.698; ✗ T_SSC: 0.728→0.687). The ablations are cleaner evidence of contribution than the baseline comparisons.

- **Semantic controllability is convincingly demonstrated.** Figure 8 shows diverse poses for the same object under different textual intents ("push" vs. "lift"). Figure 9 shows the model correctly associates "firm" prompts with larger contact areas (22–25% larger, quantified) and "gentle" prompts with sparser contact — a nuanced behavior that was not explicitly programmed.

- **O2HOI frame-pairing pipeline is a practical contribution.** The mask transfer strategy (SAM2 on unoccluded frame → dense matching to interaction frame) avoids geometric inconsistencies from diffusion-based inpainting while being more scalable than manual completion (Section 3.1). This enables automated 3D dataset construction from 2D video at reasonable scale.

- **Out-of-domain generalization is shown on Objaverse objects** (Figure 7) with verbs like "tip", "roll", "pinch" not in the primary annotation set, suggesting the method generalizes beyond the WildO2 distribution.

## Weaknesses

### Major

- **Dataset reconstruction accuracy is not quantitatively validated.** The WildO2 pipeline produces a 55% automatic success rate, with the remaining 45% failing and the final 4,414 samples undergoing manual inspection. However, no quantitative validation of reconstruction fidelity is presented — no Chamfer distances to any held-out reference, no silhouette consistency check against the original frames, no inter-annotator agreement for the manual refinement step, and no comparison against any ground-truth (e.g., from lab capture of similar interactions). Since this dataset is used for both training and evaluation, uncertainty about reconstruction accuracy propagates into uncertainty about the method's quantitative results. A small validation study (e.g., 50 random samples judged for geometric plausibility against the source video) would substantially strengthen the evidence.

### Minor

- **Baseline comparison is weak but does not undermine the contribution.** ContactGen and Text2HOI were designed for grasping contexts and lack key components of TOUCH (contact prediction, multi-level conditioning, refinement). That TOUCH outperforms them is largely expected. This is mitigated by the strong ablations, which are the more important internal validation. The paper would benefit from stating explicitly that for this new task, existing methods are necessarily adapted baselines, and the ablations serve as the primary evidence for design choices.

- **P-FID and VLM score are underspecified.** The paper cites Nichol et al. 2022 for P-FID, but does not describe the exact feature space or protocol. The VLM-assisted evaluation is mentioned only as "VLM assisted evaluation" — no VLM model name, prompt, or scoring mechanism is given. The perceptual score from 10 users (PS in Table 1) lacks any description of the task, scale, or number of comparisons per user. These metrics are central to the claim of semantic consistency and should be clearly specified (in the main text or appendix).

- **No confidence intervals or variance reported.** Tables 1 and 2 report point estimates only. Given the modest test set size (677 samples), variance reporting would help assess the statistical significance of the observed improvements, particularly for metrics where gains are smaller (e.g., Entropy: 2.93 vs. 2.85).

### Trivial

- The Sankey diagram in Figure 3(b) is too small to read in the paper layout, limiting its utility.
- The phrase "manual inspection and refinement" (Section 3.2) is mentioned without describing the number of annotators, criteria, or process.

## Nice-to-Haves

- A discussion of failure cases (e.g., thin or deformable objects, ambiguous contact regions) would provide a more complete picture of the method's limitations.
- A small-scale quantitative evaluation on the Objaverse out-of-domain examples (Figure 7) would strengthen the generalization claim beyond visual inspection.

## Removed Points

- *"The paper does not establish whether these baselines were retrained on WildO2 or merely evaluated in an adapted form."* — The paper states "adapt it for our setting" and reports 1,000 epochs of training with a 4:1 train-test split, which implies retraining. This criticism is based on speculation rather than the paper's content.
- *"The FiLM and cross-attention injection is not novel per se."* — This is a general architecture criticism that could apply to most conditional diffusion models, not a specific weakness of this paper. The novelty lies in the overall multi-level conditioning framework, not individual building blocks.
- *"Missing related works."* — Cannot verify without external sources; not appropriate to include.
- Several formatting/typo nitpicks from the harsh critic regarding parser artifacts.
- Speculation about dataset licensing or tool availability.

## Novel Insights

None beyond the paper's own contributions, but the observation that the paper treats *contact maps as the spatial interface* between semantic intent and hand-object geometry — predicted by separate CVAEs and then consumed by the diffusion model and refiner — is an interesting design principle. The cycle-consistency loss for bidirectional contact mapping (hand↔object) is a particularly clean idea that avoids the ambiguity of unidirectional nearest-neighbor contact losses.

## Suggestions

1. Add a small-scale dataset validation study: take 50 random WildO2 samples, project the reconstructed 3D into the source video frames, and have 2–3 annotators judge silhouette consistency and contact plausibility. Report an agreement score.
2. Clearly specify P-FID (which point-cloud features, which reference distribution), the VLM evaluation protocol (model name, prompt template, score aggregation), and the perceptual study design (task, scale, number of judgments per user).
3. Report standard deviations across multiple random seeds or test-set bootstraps for all metrics in Tables 1 and 2.

## Score and Decision

I performed calibration in three rounds. Round 1 (bracketing) retrieved anchors spanning 2.5–10.0. The paper clearly sits above the weak anchors (~3.0, mostly dataset description papers with minimal method) and well below the strong anchors (7.5–10.0, breakthrough method papers with rigorous multi-benchmark evaluation). Round 2 (narrowing into 5.0–7.5) retrieved HOI-Diff (avg 5.25, rejected — similar weak-baseline problem but neglected hand contact modeling entirely and had no dataset contribution), IHDiff (avg 5.50, rejected — considered a trivial diffusion adaptation with weak baselines), and SignAvatars (avg 6.25, rejected — dataset-heavy with derivative data, spread thin over multiple subproblems). Relative to these, TOUCH is stronger than HOI-Diff and IHDiff: it contributes an original dataset (not derivative), has a more elaborate method with thorough ablations, and addresses a genuinely new task. It is comparable to SignAvatars in
ambition but has a tighter focus and cleaner ablation story. However, the dataset validation gap and metric underspecification prevent it from reaching the 6.5–7.0 range. The paper sits just below the strongest mid-range anchors and above the clearly weaker ones.

**Calibration anchors used:**
- xcHIiZr3DT (2.50), U6UPhLBTcv (3.00), TCSaLeANpN (3.00), zQXX3ZV2HE (3.00) — Round 1 weak bracket; all are either unrelated task papers or simple dataset collection papers without generative modeling.
- nTNElfN4O5 (5.50, IHDiff) — Round 1/2; similar HOI generative modeling but for two hands, not HOI; considered trivial architecture adaptation; TOUCH is stronger.
- ZYwLfi50GI (5.25, HOI-Diff) — Round 1/2; text-driven HOI with weak baselines and neglected hand contact; TOUCH is stronger with better ablations and dataset contribution.
- J4D5WVoc5g (4.50) — Round 1; reconstruction-focused, no generation; less relevant.
- otoggKnn0A (4.00) — Round 1; action recognition dataset, not generative.
- L2kbdthX5M (6.25, SignAvatars) — Round 2; large-scale dataset + method, but derivative data and spread thin; TOUCH is comparably strong with tighter focus.
- TEkoMEjf7E (6.20, Phidias) — Round 2; 3D generation with reference augmentation; less relevant domain.
- 96jZFqM5E0 (6.67) — Round 2; hand pose pretraining; less relevant domain.

Round-1 bracket: [4.5, 6.5]. Round-2 narrowing placed the paper near the upper end of this bracket.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>