- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary
This paper proposes DiST, a decomposition-incorporation framework for Few-Shot Action Recognition (FSAR) that leverages Large Language Models to generate decoupled spatial and temporal attribute descriptions for action categories. These attributes are injected into visual features via two novel modules: a Spatial Knowledge Compensator (SKC) that learns compact object-level prototypes through patch aggregation, and a Temporal Knowledge Compensator (TKC) that enriches frame-level features with temporal attribute information. The approach achieves state-of-the-art results across four standard FSAR benchmarks (HMDB51, UCF101, Kinetics, SSv2-small) with gains of 1.7%–6.8% accuracy under the 5-way 1-shot setting.

## Strengths
1. **Novel decoupled spatio-temporal attribute generation (Section 3.3):** The paper systematically generates both spatial (object/environment) and temporal (action steps) attributes from LLMs, with concrete prompt templates and examples (e.g., "drink" → spatial: "container; mouth; hand"; temporal: "Hold container; Bring container to mouth; Put container"). This decoupling is novel for FSAR and provides complementary semantic context that coarse class names cannot.

2. **Principled compensator design (Sections 3.4–3.5):** SKC learns object-level prototypes via learnable patch aggregation (Eq. 1) followed by cross-attention with spatial attribute features (Eq. 2). TKC integrates a global temporal semantic vector into frame features (Eq. 3) and performs cross-attention with temporal attributes through a temporal transformer (Eq. 4). These modules are tailored to incorporate prior knowledge at different granularities, rather than simply concatenating LLM text with visual features.

3. **Convincing empirical validation (Section 4.3, Tables 1–3):** DiST outperforms prior FSAR methods across all four datasets and both 1-shot and 5-shot settings. The most compelling evidence is Table 5c, which shows that simply replacing class names with LLM prompts in the CLIP-FSAR framework yields negligible gains, while DiST's full compensator design produces large improvements — confirming that the compensator architecture, not just the richer prompts, drives the performance gain.

4. **Comprehensive ablation study (Section 4.4, Tables 4, 5a–5e):** The paper systematically ablates each component (TKC alone: +5.2% on HMDB51; SKC: +1.8%; combined: +6.1%), different injection manners, attribute content, matching metrics, and the fusion parameter α. This provides strong evidence that both compensators contribute complementary value.

5. **Qualitative analysis (Section 4.5):** Class-wise performance breakdown (Fig. 4 right, gains on all 31 HMDB51 classes), feature distribution visualization (Fig. 5, improved intra-class compactness), and attention visualization (Fig. 6, temporally-aware frame weighting) support the quantitative results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Undefined ablation baseline (Table 4, Section 4.4):** The paper reports that TKC and SKC add gains of +5.2%, +1.8%, etc. "compared to the baseline" but never states what this baseline includes (e.g., whether it uses CLIP ViT-B features with OTAM matching and no semantic injection). The relative improvements are still informative because they are large and the paper separately compares against CLIP-FSAR, but the missing definition is a reproducibility gap that should be filled.

- **No sensitivity analysis of LLM-generated attributes (Section 3.3):** The number of spatial attributes G=6 and temporal attributes L=3 are set empirically without ablation, and the paper does not test sensitivity to prompt wording or different LLM versions. Since the method's effectiveness depends on the quality of these generated attributes, the absence of any robustness analysis is a limitation. The contribution would be strengthened by showing that performance is stable across reasonable variations in these choices.

- **Missing variance or confidence intervals (Section 4.1):** Results are averaged over 10,000 random test tasks, but no standard deviations or confidence intervals are reported. This is standard practice in the FSAR literature, and including them would improve the ability to assess the significance of the reported gains.

- **Fusion parameter α only validated on HMDB51 (Section 4.4, Fig. 4 left):** The sensitivity analysis of the spatial/temporal fusion weight α is shown only for HMDB51. While α=0.5 is a reasonable default, the paper does not verify whether this value is near-optimal on other datasets where the relative importance of spatial and temporal cues may differ.

### Trivial
- Computational cost (training/inference time, parameter count) is not discussed. Not critical for a method paper, but would help readers assess practical overhead.

## Nice-to-Haves
- Provide the exact LLM prompts and generated attribute lists (as a supplementary table) to ensure full reproducibility.
- Ablate the number of spatial (G) and temporal (L) attributes to show robustness to these hyperparameters.
- Include a brief analysis of attribute quality (e.g., manual inspection of a subset of generated attributes across classes).

## Removed Points
The following points from the inputs were removed with justification:
- "The paper does not discuss other works that use LLMs for action recognition beyond FSAR context" — Not a flaw given the paper's stated scope; removed per Soft Rules about scope creep.
- Any formatting, typo, or language nitpicks — These are parser artifacts, not author errors.
- Any speculation about missing appendix content — The appendix content may have been stripped by the PDF parser.
- Strength Finder's generic praise about "addressing an important problem" or similar — Removed as generic/superficial; only concrete, evidence-anchored strengths were retained.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Explicitly define the ablation baseline** in Section 4.4 (e.g., "Baseline uses CLIP ViT-B visual features with OTAM temporal matching and no semantic attribute injection").
2. **Add variance or confidence intervals** to the main results (Tables 1–3) and ablation results.
3. **Include an ablation of G and L** (number of spatial/temporal attributes) to demonstrate robustness to these choices.
4. **Provide the exact prompts and generated attributes** as a supplementary table.
5. **Briefly discuss computational cost** — training time per episode or total training time, and inference overhead of the two compensators.
6. **Show α sensitivity on at least one additional dataset** (e.g., SSv2-small) to verify that α=0.5 generalizes.
