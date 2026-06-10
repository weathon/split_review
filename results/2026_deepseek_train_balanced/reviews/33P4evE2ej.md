## Summary

The paper introduces DynaMer Adapter, an architecture that dynamically merges tokens from a frozen general-domain ViT (DINOv2) and a frozen medical-domain ViT (pre-trained on cell images) for medical image analysis. It uses a shared Gated Mixture-of-Experts (MoE) adapter for token-level integration plus a layer-wise skipping router to reduce computation. Evaluated on Med-VTAB across 23 datasets spanning color, X-ray, OCT/CT/MRI modalities, the method shows consistent accuracy improvements over baselines while using fewer tunable parameters than the closest two-model counterpart (GMoE).

## Strengths

- **Consistent accuracy gains across diverse medical modalities**: Tables 1–3 report that DynaMer outperforms single-model methods (VPT, GaPT, LSPT) and the two-model GMoE baseline on color, X-ray, OCT, CT, and MRI datasets, showing the benefit of merging two frozen pre-trained models via a learned fusion mechanism. The shared MoE adapter achieves this with markedly fewer parameters than GMoE (Figure 1a), which uses separate per-domain adapters.

- **Gating mechanism addresses a concrete training instability problem**: Section 3.2 identifies value distribution shift from inserting randomly initialized adapters and proposes a learnable sigmoid-gated residual connection (Eq. 4) to balance original and adapter-processed tokens. Table 4 provides ablation evidence that this gating improves results over a no-gating baseline.

- **Layer-wise skipping router enables a tunable accuracy-efficiency trade-off**: Table 7 tests token retention ratios (100% down to 10%) and shows that inference time can be substantially reduced without proportionate accuracy loss. This mechanism is absent from VPT/GaPT/LSPT baselines and is relevant for the paper's stated goal of real-time medical deployment.

- **Strong quantitative gains on patient-level OOD evaluation**: Tables 8–9 show DynaMer outperforming prior methods in scenarios where training and test patient splits differ, supporting a key claim in the abstract.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reported anywhere**: The paper contains zero mention of random seeds, multiple runs, standard deviations, or confidence intervals. This was verified via grep across the full text. For a top venue, single-run results on small medical datasets (where variance is known to be high) prevent readers from assessing whether reported gains exceed run-to-run noise. This is a structural evidential gap that would need to be addressed before acceptance.

- **Training procedure is under-specified and internally contradictory**: Line 99 states: "They are optimized end-to-end with the objective in adaptation tasks." Line 129 states: "Each expert within the MoE architecture was optimized individually before the gating mechanism was trained to dynamically combine their outputs." These descriptions are in direct tension. The paper does not explain what "optimized individually" means (separate data subsets? separate task objectives?), whether the pre-trained ViTs remain frozen during this stage, whether the staged procedure is necessary, or whether results are sensitive to this design choice. Without clarification, the claimed "end-to-end dynamic adaptation" cannot be verified.

- **Insufficient ablation isolating the contribution of each pre-trained model**: The "medical" pre-trained ViT (Nguyen et al., 2023) is trained specifically on 1.6 million *cell images* (line 129), yet the paper tests on modalities ranging from X-rays to OCT to MRI — many far from cellular pathology. The paper does not ablate whether DynaMer with *only* the general model, *only* the medical model, or *two general models* would achieve similar results. Since single-model baselines (VPT, GaPT, LSPT) use only one model, they do not isolate whether the medical model specifically contributes beyond having a second frozen model. This ablation is necessary to support the claim that the method successfully combines complementary *general and medical* knowledge.

- **Data-efficiency claims lack dedicated experimental support**: The abstract and introduction claim DynaMer excels "in tasks with only few samples" and Figure 1c is described as showing data efficiency, but there is no tabular few-shot experiment (e.g., k-shot results with k=1,5,10) reported in the paper. A quantitative few-shot study is needed to substantiate these claims.

### Minor

- **Overstated novelty distinction from GMoE**: Section 2 (line 36) claims GMoE operates "at the feature or layer level" while DynaMer performs "token-level integration." However, the GMoE formulation shown in Eq. 1 already operates per-token: `Adapter^l([x_gen,i, x_med,i])`. The genuine differences (shared vs. separate adapters, gating, token skipping) are contribution enough and should be presented accurately without mischaracterizing the baseline.

- **"MoE experts are not trained" (line 37) is confusing given trainable AdapE**: The paper states "MoE experts are not trained" but then introduces trainable adaptation expert networks (AdapE) in Section 3.2. The intended meaning (the pre-trained ViTs are frozen) is clear from context, but the terminology conflates two different uses of "expert" and should be clarified.

- **Skipping router presented without reference to adaptive computation literature**: The layer-wise router selects which tokens pass through the adapter. While it serves a different purpose than token-pruning methods (skipped tokens still pass through the base ViT), it is related to adaptive computation / conditional computation in ViTs. The paper neither cites nor compares against any such methods, which limits the positioning of this component.

- **No Limitations section**: Given the domain-specificity of the medical pre-trained model, the absence of variance reporting, and the lack of direct few-shot experiments, a limitations section would substantially improve the paper's self-assessment and credibility.

- **Gating dimension ablation (Table 5) is unclear at the extreme**: A gating network with input dimension 1 is tested, but the paper does not explain what a single-dimensional input to the gating network represents or how this configuration functions. The interpretation of this ablation is not obvious.

### Trivial
- The phrase "fundamentally inferior capabilities" (abstract, line 4) to describe medical pre-trained models is imprecise — what is meant is inferior *general* capabilities, which is clarified later but could mislead on first reading.

## Nice-to-Haves

- A direct comparison against the specific GMoE / MoE Adapter from Mo et al. (2024a) as a dedicated row in the main results tables (Tables 1–3), along with a version of DynaMer without gating and without the skipping router, to quantify the marginal benefit of each component.
- Inference-time wall-clock measurements on actual hardware, rather than token-reduction ratios alone, to substantiate the efficiency claims.
- Testing DynaMer with different medical pre-trained models (e.g., a retina-specific model paired with the cell-image model) to explore whether the results generalize across medical sub-domains.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Criticism that "Patient ID OOD is not real OOD"**: Patient-level holdout IS a standard form of OOD evaluation in medical ML, and the paper follows prior work (Mo et al., 2024a) in using this setup. Removed as factually incorrect.
- **Criticism that Cambrian-1 comparison is "tangential"**: The paper mentions Cambrian-1 to draw contrast in scope. This is a reasonable citation to scope the contribution. Removed as a strawman.
- **Criticism that "medical model inferiority" contradicts the premise**: The paper's intended meaning (medical models have weaker *general* capabilities) is clear from context. Removed as a misreading.
- **"Gating mechanism is too simple"**: The paper presents it as a practical solution to a specific instability problem, not as a fundamental architectural innovation. The simplicity is not a flaw given the stated purpose. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring pattern: the paper proposes a reasonable approach (shared MoE adapter for fusing two frozen models) but systematically overstates its distinctiveness from prior work and under-supports its claims with insufficient experimental rigor (missing variance, missing ablations, contradictory training descriptions). This gap between claimed novelty and evidenced novelty is the central tension.

## Suggestions

1. **Report all results with standard deviations over at least 3–5 random seeds.** This is non-negotiable for a top venue, especially on small medical datasets.
2. **Clarify the training procedure.** Resolve the contradiction between lines 99 and 129. If there is a staged training phase, describe it fully (data used, objective, whether experts are frozen during gating training) and justify it with an ablation comparing staged vs. single-stage end-to-end training.
3. **Add ablations isolating each pre-trained model.** Show: DynaMer-with-general-only, DynaMer-with-medical-only, DynaMer-with-two-general-models, and DynaMer-with-both. This directly tests whether the medical model contributes or whether any second frozen model suffices.
4. **Add a dedicated few-shot experiment** (e.g., 1, 5, 10, 20 samples per class) to support the data-efficiency claim made in the abstract.
5. **Correct the characterization of GMoE** (it operates per-token in Eq. 1) and reframe the novelty claims around the actual differences: shared MoE adapter, gating, and token-level skipping.
6. **Discuss the skipping router in the context of adaptive computation / conditional computation in ViTs** and, if possible, compare against one standard token-pruning baseline.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>