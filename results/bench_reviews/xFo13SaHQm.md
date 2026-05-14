Now I have all the information needed to write the final consolidated review.

## Summary

This paper identifies and formalizes the "copy-paste artifact" in identity-consistent image generation—where models replicate the reference face instead of synthesizing the identity across natural variations—and proposes three contributions: (1) **MultiID-2M**, a large-scale dataset of 500k paired multi-person images with reference banks for ~3k identities; (2) **MultiID-Bench**, a benchmark with a Copy-Paste (MCP) metric that quantifies over-similarity to the reference; and (3) **WithAnyone**, a FLUX-based model trained with a GT-aligned ID loss and an InfoNCE contrastive loss using extended negatives. Experiments show WithAnyone reduces copy-paste while maintaining high identity similarity, breaking the trade-off observed in prior methods.

## Strengths

- **Clear and well-motivated problem formulation.** The copy-paste artifact is convincingly motivated (Fig. 2) by contrasting model behavior with natural variation in real photographs. The paper identifies a genuine failure mode that prior metrics (SimRef) inadvertently reward.

- **MultiID-2M is a significant dataset contribution.** At 500k paired multi-person images with ~400 reference images per identity (plus 1.5M unpaired images), this is the first large-scale open-source dataset providing multiple reference images per identity in group photos, enabling paired training and contrastive losses that are central to mitigating copy-paste. The construction pipeline (clustering, retrieval, filtering) is practical and well-documented.

- **MultiID-Bench with the Copy-Paste metric (MCP) is a principled evaluation innovation.** The benchmark uses SimGT (similarity to ground-truth) as the primary metric rather than SimRef, and the copy-paste score MCP = (θ_gt − θ_gr)/max(θ_tr, ε) captures relative bias toward reference vs. ground truth. Fig. 5 reveals a clear trade-off that prior evaluations obscured. The user study (Table 7) shows moderate positive correlation between MCP and human judgments (Pearson r=0.44, p<1e-47), validating the metric's perceptual relevance.

- **WithAnyone achieves compelling qualitative results.** The generated images (Fig. 6) demonstrably produce more natural variation (smiles, pose changes, expression changes) than strong baselines while preserving identity. The model also generalizes to low-quality and non-celebrity references (Figs. 15, 16), demonstrating practical robustness.

- **Systematic ablation study validates each component.** Table 3 shows that removing paired training (Phase 3) increases CP from 0.161 to 0.239, removing GT alignment reduces SimGT from 0.405 to 0.385, and removing extended negatives drops SimGT from 0.405 to 0.368. These ablations isolate the contribution of each design choice.

## Weaknesses

### Major

- **Distributional advantage in the primary evaluation.** MultiID-Bench samples test cases from the long tail of MultiID-2M (disjoint identities, but same source distribution—celebrity event photos, lighting, backgrounds, face poses). All baselines were trained on different data distributions (LAION, CelebA, etc.), so the main quantitative comparison (Table 1, Fig. 5) cannot fully separate genuine algorithmic improvement from familiarity with the data distribution. The OmniContext evaluation partially addresses this (WithAnyone achieves best among face customization models), but it is presented as secondary. The headline claim of "breaking the trade-off" relies primarily on MultiID-Bench results. A cross-dataset evaluation (e.g., training a strong baseline on MultiID-2M or testing on an independently collected set) would be needed to fully substantiate the claim.

### Minor

- **The SimGT/MCP metric depends on the specific ground-truth image.** MCP = (θ_gt − θ_gr)/max(θ_tr, ε) measures whether the generated face is closer to the reference or to the *specific* ground-truth image. If a prompt admits multiple valid interpretations (different plausible poses, expressions, or lighting of the same identity), a model producing a plausible but different face is penalized. This is a conceptual limitation of the metric design, though the user study's moderate correlation with human judgments provides some validation.

- **Ablation of the FFHQ-only baseline does not isolate which property of MultiID-2M drives improvement.** The FFHQ-only ablation (SimGT 0.224) shows drastic deterioration, but this conflates multiple factors: scale, paired supervision, data diversity, and domain alignment. An ablation controlling for these factors individually would strengthen the analysis.

- **The toy experiment for InfoNCE (Fig. 17) uses only 1000 training samples.** While the results are directionally informative, it is unclear how representative this small-scale experiment is of full training dynamics with the complete dataset.

- **User study is small-scale.** Ten participants for 230 groups is modest, and no inter-annotator agreement is reported. The correlation analysis (Table 7) is supportive but not definitive.

### Trivial

- **The fitted curve in Fig. 5** is described informally ("fitted curve") without specifying the fitting procedure. A polynomial fit through other methods is not a theoretical bound.

## Nice-to-Haves

- A cross-dataset evaluation (e.g., on an independently collected set of in-the-wild group photos) would address the distributional concern and substantially strengthen the paper.
- An ablation that trains a strong baseline (e.g., PuLID or UniPortrait) on MultiID-2M would isolate dataset-driven vs. architecture-driven improvement.
- Sensitivity analysis of SimGT to which ground-truth image is selected for a given identity would calibrate the metric's reliability.

## Removed Points

These points were flagged for removal; treat them with caution:

- **Harsh Critic's claim that "w/o Ext. Neg." removes InfoNCE entirely.** The paper explicitly states "By ablating extended negatives, leaving only 63 negative samples from the batch (originally extended to 4096)" — the ablation keeps InfoNCE with batch-only negatives. The criticism is factually incorrect.

- **Harsh Critic's claim that providing GT pose to ID-Patch is an unfair advantage for WithAnyone.** The paper states "ID-Patch requires pose condition, and we use the ground-truth pose for it." This favors the *baseline* (ID-Patch), not the proposed method, so it is not a valid weakness.

- **Strength Finder's claim that "large-scale ablation studies validate each component"** — this is kept in Strengths above as it is well-supported.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated contributions and identified limitations, without introducing new cross-cutting observations.

## Suggestions

1. Add a cross-dataset evaluation on an independently collected set of group photos (e.g., from Celebrity Together or a newly curated set) to address the distributional concern. Even a smaller-scale experiment would substantially improve confidence in the quantitative claims.
2. Ablate the negative pool scale more granularly (batch-only 63, then 512, 1024, 2048, 4096) to better attribute the gain to pool size vs. the InfoNCE loss itself.
3. Add inter-annotator agreement metrics for the user study and consider expanding the participant pool if possible.
4. Clarify the curve-fitting procedure in Fig. 5 (what polynomial order, data points included/excluded) to avoid the appearance of ad-hoc fitting.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| **IC-Custom** (`gv2cr8kABL.md`) | 6.00 | Both contribute dataset+model+benchmark for image customization. WithAnyone has a larger dataset and more novel metric, but IC-Custom's evaluation is cleaner (less distribution concern). WithAnyone is slightly weaker overall. |
| **EditedID** (`ohpsnceMSb.md`) | 6.00 | Both address face ID issues in generation/editing. WithAnyone has more substantial dataset and training contributions but EditedID is training-free with cleaner evaluation. Comparable quality. |
| **OmniPortrait** (`DVmR3Ij0ap.md`) | 5.50 | Both target face ID customization with evaluation concerns. WithAnyone has stronger dataset and benchmark contributions but similar evaluation caveats. Slightly stronger than OmniPortrait but comparable. |
| **ContextGen** (`wEuWyQnLY5.md`) | 5.00 | Both have evaluation confounds (baselines on different data). WithAnyone has better problem isolation and more novel metrics. Stronger than ContextGen. |
| **CoDi** (`8pDcEIvmcP.md`) | 4.67 | Both deal with subject consistency. WithAnyone has more substantial contributions (dataset, benchmark, trained model vs. training-free method). Clearly stronger. |
| **InstantCharacter** (`iPiEllQhsn.md`) | 4.50 | Both propose customization models with datasets. InstantCharacter had poor quantitative results; WithAnyone's quantitative evidence is much stronger. |
| **FaceID-6M** (`yTq81RcKaw.md`) | 3.50 | Pure dataset paper with minimal novelty beyond curation. WithAnyone has model, benchmark, and a more novel dataset. Significantly stronger. |
| **Turn That Frown** (`XJ3T70nELl.md`) | 2.67 | Dataset paper with legal/ethical concerns and small scale. WithAnyone is substantially more rigorous and novel. |

The paper makes genuine contributions (dataset, benchmark with novel metric, model with clear qualitative improvements). The primary weakness—distributional advantage in evaluation—is real but not fatal: the qualitative results, user study, and OmniContext evaluation provide converging evidence. The paper is stronger than the mid-4 to low-5 papers and comparable to or slightly above the 5.5-6.0 papers in its domain. I position it at 5.5.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>