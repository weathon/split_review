Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper proposes GenZSL, an inductive variational autoencoder for generative zero-shot learning that synthesizes unseen class visual features by "inducing" from similar seen classes (using seen samples as starting points) rather than "imagining" from Gaussian noise. The method introduces class diversity promotion (CDP) via removing the first singular vector from CLIP text embeddings to improve class discriminability, and a target class-guided information boosting loss. Experiments on CUB, SUN, and AWA2 show strong results, with large margins over prior generative ZSL methods and substantial training speedups.

## Strengths

- **Novel inductive paradigm for generative ZSL**: The paper introduces a genuinely different approach to generative ZSL — using seen samples as referent starting points rather than generating from scratch. This is conceptually motivated by human inductive learning (Section 3.3, Figure 1). The training procedure (cross-class generation within seen classes) is distinct from standard conditional VAEs/GANs.

- **Strong empirical results with weak semantic vectors**: GenZSL achieves 92.2% CZSL accuracy on AWA2 and 47.0% harmonic mean on CUB (GZSL) using only CLIP text embeddings of class names — no expert-annotated attributes. Table 4 shows a 22.1% absolute harmonic mean improvement over f-VAEGAN when both use the same weak CLIP vectors on CUB, demonstrating the approach's advantage in the weak-semantic setting.

- **Efficiency gains are substantial**: Figure 5 reports ≥60× training speedup over f-VAEGAN on AWA2 with 24.7% performance gains. This is not just a hardware/implementation artifact — the IVAE is architecturally simpler (MLP-based) than typical VAEGAN stacks.

- **Ablation study confirms component contributions**: Table 3 shows that removing the target class reconstruction loss (ℒ<sub>TR</sub>) drops harmonic mean by 30.8% on CUB and 33.5% on AWA2, and removing CDP causes notable degradation. These ablations validate that both criteria are functionally important.

## Weaknesses

### Major

- **CDP undermines the semantically similar sample selection mechanism it is supposed to enable**: The paper states that after CDP, the mean cosine similarity among refined class vectors drops to 1.825×10⁻⁵ on CUB (Section 3.1, line 126) — effectively near-zero for all pairs. Yet the semantically similar sample selection (Section 3.2, Eq. 4) explicitly uses cosine similarity on these *refined* vectors (̃z) to pick top-k referent classes. If all pairwise cosine similarities are near-zero, the ranking degenerates into an essentially arbitrary choice. The paper claims CDP "keep[s] the original class relationships" but provides no evidence that meaningful variance remains at the 10⁻⁵ scale. Since this selection is the gateway to the entire induction pipeline, the paper must clarify: (a) whether selection actually uses the refined vectors or the original ones, and (b) if refined vectors are used, demonstrate that the cosine similarity ranking is not noise-dominated. The ablation confirms CDP helps overall, but whether it helps through better conditioning or through meaningful selection is unclear.

- **The central claim — that induction outperforms imagination — is not tested with a properly controlled baseline**: Tables 1 and 2 compare GenZSL (using CLIP visual features and weak CLIP text embeddings) against methods using different visual backbones (e.g., ResNet) and expert-annotated attribute vectors. These confound differences in backbone strength, semantic information, and paradigm. Table 4 controls for semantic vectors by re-implementing f-VAEGAN and TF-VAEGAN with weak CLIP embeddings, but the CZSL results for these baselines are missing entirely ("N/A" entries), and the paper acknowledges these methods were "designed for rich attribute vectors" and are "likely poorly adapted to weak embeddings." The key missing control is a method that uses the *same* CLIP visual features *and* weak semantic vectors as GenZSL but generates from scratch (imagination) rather than induction. Without this, the observed gains could partially or largely reflect the stronger visual backbone (CLIP vs. ResNet) rather than the induction paradigm itself.

### Minor

- **ℒ<sub>Boost</sub> denominator sums only over seen classes (Eq. 5)**: During training, the contrastive loss encourages the generated sample to be close to the target unseen class semantic vector relative to *seen* classes. It does not promote separation among unseen classes. Since the generated unseen features are later used to train a classifier that must discriminate among unseen classes as well, this could cause intra-unseen-class confusion. The paper does not analyze this. (The strong GZSL harmonic means on AWA2, 87.4%, suggest the practical impact may be limited, but the analysis is absent.)

- **Mixup fusion weights (0.8 and 0.2) are not ablated**: The referent sample is a fixed convex combination of the top-2 seen classes. This is a non-trivial design choice — a different weighting changes what "reference sample" the model sees. The hyperparameter analysis (Figure 6) varies λ, k, and N<sub>syn</sub>, but not the mixup weights.

- **Hyperparameter analysis is limited to CUB**: While the paper analyzes λ, k, and N<sub>syn</sub> on CUB (Figure 6), the chosen hyperparameters for SUN and AWA2 are simply stated (line 255) without comparable sensitivity analysis. Given that SUN has very different characteristics (717 scene classes, 645/72 split), the absence of analysis there weakens the robustness claim.

- **The training-to-test generalization gap is not analyzed**: The model is trained on (seen reference, seen target) pairs and tested on (seen reference, unseen target) pairs. The paper asserts but does not analyze why the learned transformation should transfer across the seen/unseen boundary. While this is a standard ZSL assumption, the paper's specific claim that the model "induces" rather than "imagines" would be strengthened by analysis showing that the reconstruction loss on held-out seen pairs correlates with generation quality on unseen classes.

### Trivial

- The notation Ψ<sub>acc</sub> for CZSL and S, U, H for GZSL is introduced in the evaluation protocols (Section 4) but Table 1 uses the simpler column header "acc" without the subscript, and Table 2 does not consistently label which columns correspond to S, U, H.

## Nice-to-Haves

- A controlled experiment comparing GenZSL against a lightweight conditional VAE that uses the same CLIP visual features, same weak CLIP text embeddings, but generates from Gaussian noise (imagination) rather than from seen samples. This would directly test induction vs. imagination.
- Ablation of the selection mechanism itself: randomly chosen referent classes vs. cosine-similarity selection on original (non-refined) embeddings vs. refined embeddings. This would clarify whether CDP helps through selection or through conditioning.
- Analysis of intra-unseen-class separability of generated features (e.g., average pairwise distance or silhouette score among generated features of different unseen classes).
- Ablation of the mixup fusion weight parameter.

## Removed Points

- **Critical Issue #4 (Harsh Critic): "Induction concept not well-defined / training-test gap"** — This is a restatement of a standard ZSL assumption (learned mappings from semantic to visual space generalize across the seen/unseen boundary). The paper's training procedure follows the same logic as all ZSL methods. The criticism is too generic to constitute a specific weakness of this paper; included above in Minor as a suggestion for strengthening.
- **Strength Finder's "CDP elegantly solves the weak semantic vector problem"** — Inflated. While CDP does improve discriminability (ablation confirms this), it also creates the selection-arbitrariness problem identified above. The weakness partially negates this claimed strength. Moved here for balance.
- **"Human finder" comments** (none provided in the inputs).
- **Formatting/style nitpicks** (none surfaced by reviewers that aren't parser artifacts).

## Novel Insights

The most interesting tension the reviews surface is that CDP simultaneously enables and potentially undermines the method: it makes class vectors more discriminable (which the ablation confirms is necessary) but at the cost of destroying the relative similarity structure needed for semantically meaningful reference class selection. This suggests the reported performance may come from a combination of (a) better-conditioned semantic inputs to the decoder, and (b) the inductive architecture itself, rather than from selecting *semantically similar* referent classes specifically. A useful follow-up study would disentangle these factors by comparing random selection, original-embedding selection, and CDP-embedding selection.

## Suggestions

1. **Clarify the CDP/selection inconsistency**: Explicitly state whether selection uses refined vectors (̃z) or original vectors (z). If refined vectors are used, report the variance/range of pairwise cosine similarities (not just the mean) to demonstrate the ranking is meaningful. Alternatively, apply CDP only to the conditioning input to the decoder/encoder and use original vectors for selection.
2. **Add the missing controlled baseline**: A version of GenZSL that replaces the referent sample with Gaussian noise (while keeping everything else identical, including CLIP features and weak semantic vectors) would directly isolate the benefit of induction over imagination in a way the current comparisons do not.
3. **Complete Table 4**: Report CZSL results for the weak-vector f-VAEGAN and TF-VAEGAN baselines.
4. **Ablate the mixup fusion weight** and the selection source (random vs. original-embedding cosine vs. refined-embedding cosine).
5. **Extend hyperparameter analysis to SUN** where the setting is very different (scene classification, 717 classes, different λ=0.001).

## Score and Decision

The paper introduces a genuinely novel generative paradigm for ZSL and backs it with strong benchmark results and useful ablations. However, two structural issues prevent acceptance: (1) the CDP mechanism as described appears to make the reference class selection unworkable (near-zero cosine similarities across the board), yet the paper's narrative depends on selecting *semantically similar* seen classes — this contradiction must be resolved; (2) the core claim of induction > imagination is not tested with a controlled comparison that holds visual features and semantic vectors constant. These are not fatal — the method clearly works — but they weaken the paper's central argument substantially. A revision that clarifies the selection mechanism and provides the missing controlled baseline could make this a strong contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>