---

## Summary

UniHM is a three-stage framework for language-conditioned dexterous hand manipulation sequence generation. It proposes: (1) a morphology-agnostic VQ-VAE tokenizer with a shared codebook and cross-hand distillation that maps heterogeneous dexterous hand kinematics into one discrete action space; (2) a Qwen3-0.6B–based VLM with a progressive masking curriculum for instruction-guided token generation; and (3) a physics-guided Gauss–Newton refinement module with contact, generative, and temporal priors. The system is evaluated quantitatively on DexYCB and OakInk and qualitatively in real-world trials across four task types.

---

## Strengths

- **Physics refinement is demonstrably effective.** Table 4 ablation directly shows: removing the physical refinement module worsens MPJPE from 61.40 → 65.78, FPL from 12.15 → 15.35, and FID from 31.24 → 33.57 on DexYCB (seen). The effect is consistent across seen/unseen splits and both datasets. The Gauss–Newton formulation (Eqs. 11–18) with asymmetric contact penalty, generative prior, and temporal prior is well-motivated and cleanly derived.

- **Progressive masked training provides meaningful improvement.** The ablation "w/o Masked Training" (Table 4) confirms higher MPJPE (73.41 vs. 61.40) and FPL (14.42 vs. 12.15) on DexYCB seen, validating the curriculum's contribution to reducing exposure bias and improving sequential stability. The masking schedule (Eq. 10) is clearly described.

- **Real-world execution shows substantial gains over baselines.** Table 3 reports UniHM at 65%/60% Grab success on seen/unseen vs. 30%/45% for the best baseline (MotionGPT3+Dex-Retargeting), and notably 60%/55% on Pull&Push, which requires contact-rich sequential control. This independent real-world validation demonstrates that the generated sequences are physically executable.

- **Depth input ablation confirms concrete component value.** Removing depth input degrades MPJPE from 61.40 → 85.47 (seen) and FID from 31.24 → 56.36, supporting the claim that RGB-D perception is essential for scene trajectory estimation.

- **Training without teleoperation data is a genuine and useful contribution.** Leveraging MANO-derived HOI sequences and retargeted dexterous trajectories, rather than expensive real-robot demonstrations, is a meaningful reduction in data cost that the real-world results validate.

---

## Weaknesses

### Fatal
None.

### Major

- **Baselines in Tables 1–2 are out-of-domain body motion models, not dexterous hand manipulation methods.** Every baseline in the main comparison — TM2T, MDM, FlowMDM, MotionGPT3 — is a general full-body skeleton motion generation model designed for tasks like "a person walks." None are intended for or adapted to dexterous finger-level grasping. Meanwhile, the paper's own Section 2.2 identifies domain-relevant methods (HOIGPT: "long 3D hand-object interaction," "bidirectional mapping between text and HOI sequences"; Multi-GraspLLM: "language-guided grasp poses across multiple robotic hands"), yet none appear in the quantitative tables. Outperforming body motion models on a dexterous hand dataset is nearly guaranteed; it provides no evidence of state-of-the-art performance within the actual field of language-conditioned dexterous manipulation.

- **Applying the authors' physics refinement to baselines does not create a fair comparison; it conflates contributions.** Section 4.3 states: "we post-process their outputs with our physics-guided refinement to ensure a fair comparison." However, the refinement was co-designed with the UniHM generation model — its contact energy queries the object point cloud via CLIPort's perception output, and its generative prior $\mathcal{E}_{\text{gen}}$ anchors to the generated trajectory $q_t^{\text{gen}}$. Applying this to outputs from body motion models (with different kinematic parameterizations) is not a controlled condition. Furthermore, the real-world experiments (Table 3) use "Dex-Retargeting" for baselines instead of the physics refinement, which is directly inconsistent with the rationale given in Section 4.3. This inconsistency means neither the quantitative nor the real-world comparison baseline treatment is coherent.

- **The morphology-agnostic tokenizer — a stated headline contribution — has no dedicated evaluation.** The paper introduces Eq. (6) for cross-hand pose translation and claims the shared codebook enables "direct token reuse and transfer across robotic and anthropomorphic hands." Yet Table 4's ablation contains only three conditions (w/o Depth Input, w/o Masked Training, w/o Physical Refinement) and no "w/o Unified Tokenizer" or "per-hand tokenizers" condition. There is no measurement of codebook utilization, per-hand reconstruction quality, or cross-morphology transfer fidelity. Given that this is one of the four listed contributions in the Introduction, the complete absence of supporting evidence for the cross-morphology claim is a significant gap.

### Minor

- **Real-world success rates in Table 3 are uninterpretable without trial counts.** The 65%, 60%, etc. values are reported without stating how many trials per cell were attempted. Typical small-scale robot experiments with n=10 would give ±16% confidence intervals that overlap most reported differences. This does not invalidate the result but prevents readers from assessing statistical reliability.

- **FID feature extractor is unspecified, yet FID values differ by an order of magnitude across datasets.** Section 4.2 introduces FID as a metric but does not identify the pretrained feature extractor used. DexYCB FID values range 31–56 while OakInk values range 204–337; this gap likely reflects different feature spaces or normalization, making cross-dataset FID comparisons and threshold judgments not reproducible.

- **The diversity–accuracy tradeoff from masked training is unreported.** Table 4 shows that removing masked training produces Diversity of 73.09 (seen) and 74.88 (unseen), both substantially closer to GT Diversity of 125.53 than the full model (39.62 and 42.70). This indicates that the masking curriculum trades diversity for accuracy, which is a significant characteristic of the system that practitioners would need to know. The paper provides no discussion of this tradeoff.

### Trivial
- The claim to be "the first framework" for language-conditioned dynamic dexterous manipulation is not precisely differentiated from HOIGPT (described in Section 2.2 as generating "long 3D hand-object interaction" from text). The distinction is asserted but not argued rigorously.

---

## Nice-to-Haves

- Replace or augment Tables 1–2 with at least one domain-relevant baseline (HOIGPT, Multi-GraspLLM, or SemGrasp adapted to sequence prediction). Even a single such comparison would ground the quantitative claims.
- Add a "w/o Unified Tokenizer" ablation or a cross-morphology transfer experiment: encode a MANO sequence, decode with Shadow and Leap decoders, and measure the output against a direct Dex-Retargeting baseline. This would directly validate the tokenizer's core claim.
- Report trial counts and confidence intervals for Table 3, and clarify whether baselines in Table 3 and Tables 1–2 receive the same post-processing.
- Specify the FID feature extractor used and normalize across datasets to make FID values interpretable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Training/inference mismatch (CLIPort estimation vs. ground truth)**: The harsh critic raises this as a concern, but the paper explicitly acknowledges and justifies this design in Section 3.3: "Our training and inference pipelines differ by design. During training, we condition the model on ground-truth target trajectories... At inference, a separate CLIPort module estimates these quantities from RGB-D observations, decoupling spatial perception from hand-object interaction." This is an intentional modular design with stated advantages. Removed as a weakness since the paper directly addresses it.

- **Strength: "State-of-the-art generation accuracy on standard benchmarks"** (Strength Finder, core strength 1): The baselines in Tables 1–2 are out-of-domain general motion models (confirmed by Section 2), not domain-appropriate dexterous manipulation baselines. This framing as "standard benchmarks" for the dexterous manipulation field is misleading. The strength is weakened by a verified weakness; removed as a standalone strength.

- **Strength: "Unified tokenizer enables morphology-agnostic pose translation"** (Strength Finder, supporting strength 1): This strength conflicts with the verified weakness that no cross-morphology transfer experiment exists in the paper. The claim is architectural, not evidential. Removed per the rule that strengths conflicting with verified weaknesses are dropped.

- **Strength: "Scalable language data annotation via GPT-4o"**: This is a supporting methodological detail (Section 3.1) rather than a novel demonstrated contribution. It is a reasonable engineering choice but not a substantiated strength beyond the description given. Removed as generic/superficial.

---

## Novel Insights

The paper's most technically interesting observation — not explicitly discussed by the authors — is the diversity–accuracy tradeoff revealed by the masked training ablation. The full model's diversity (39.62 on DexYCB seen) is considerably farther from GT diversity (125.53) than the w/o Masked Training variant (73.09). This suggests that the progressive masking curriculum, while improving positional accuracy (lower MPJPE, FPL), constrains the output distribution toward a narrower mode. For deployment applications where varied grasping strategies are desirable (e.g., multi-trial manipulation or grasp planning under uncertainty), this compression could be limiting. Understanding what diversity ceiling is achievable without sacrificing accuracy, and whether the tradeoff is tunable, would be a valuable direction.

---

## Suggestions

1. **Replace or add one domain-relevant baseline in Tables 1–2.** HOIGPT, Multi-GraspLLM, or SemGrasp (extended to sequences) are already cited in the related work. Adding even one such comparison would transform the evaluation from a demonstration against weak out-of-domain methods into an informative state-of-the-art comparison.

2. **Add a "w/o Unified Tokenizer" ablation row to Table 4.** Train five separate per-hand VQ-VAEs with the same codebook size, run the same evaluation, and show whether the shared codebook provides measurable benefit. This is the minimum evidence needed to support the morphology-agnostic tokenizer contribution.

3. **Report trial counts and confidence intervals for Table 3.** Given the magnitude of differences reported (e.g., 65% vs. 30%), confidence intervals are likely favorable to the authors' method — reporting them strengthens rather than weakens the result.

4. **Specify the FID feature extractor in Section 4.2.** This is a one-sentence addition and makes the results reproducible.

5. **Discuss the diversity tradeoff explicitly** in the ablation section. Acknowledging that masked training narrows diversity while improving accuracy, and how practitioners might tune $p_t$, would improve the paper's practical utility.

---

## Evaluation on Core Axes

- **Originality**: Moderate. The combination of a morphology-agnostic VQ-VAE, a small VLM (0.6B), and physics-based Gauss–Newton refinement for dexterous manipulation is a novel integration, though each component individually draws on established methods. The cross-hand distillation approach is the most original element.

- **Importance of research question**: High. Language-conditioned sequential dexterous manipulation without teleoperation data is a meaningful and underserved problem with clear relevance to robotics and embodied AI.

- **Claims well supported**: Weak. The ablation results do support the contribution of individual components. However, the central claim of "state-of-the-art" performance is tested only against out-of-domain baselines, and the headline tokenizer contribution lacks any direct experimental support.

- **Soundness of experiments**: Weak. The baseline comparison design is methodologically problematic (out-of-domain methods, applying authors' refinement to baselines). The tokenizer is not ablated. Trial counts are absent from real-world experiments.

- **Clarity of writing**: Adequate. The method sections are clear and mathematically precise. The evaluation section understates the limitations of the baseline selection.

- **Value to research community**: Moderate. The physics refinement formulation, the masked training curriculum, and the real-world results on multiple task types are genuine contributions. The paper's value would be substantially higher if the evaluation were grounded in domain-appropriate comparisons.

---

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>