I've now thoroughly verified every claim against the paper. Let me write the consolidated review.

## Summary

This paper proposes IC-Light, a method for scaling diffusion-based illumination editing training by enforcing a "light transport consistency" constraint. The constraint is motivated by the physical linearity of light transport (appearance under merged illumination = sum of appearances under individual illuminations). The authors translate this into a diffusion training loss by constraining noise predictions under different illumination conditions to be related via a learned MLP. They train on >10M images from three data sources (in-the-wild augmented images, 3D renders, light stage captures) using strong backbones (SD1.5, SDXL, Flux), and demonstrate applications including background-conditioned relighting and normal map extraction.

## Strengths

- **Large-scale, multi-source data pipeline**: The paper systematically combines three qualitatively different data sources (in-the-wild augmented images — 6M, 3D renders — 4M, light stage captures) into a unified training format. The ablation in Figure 4 shows that removing in-the-wild augmentation data degrades generalization (e.g., hat color changes on portraits), providing concrete evidence that data diversity improves model robustness. This is a genuine engineering contribution.

- **IC-Light consistency constraint empirically helps**: The ablation study (Figure 4) directly demonstrates that removing the light transport consistency term causes visible color saturation artifacts and loss of red/blue albedo distinction, while the full model preserves intrinsic properties. This provides clear empirical evidence that the constraint is effective for its intended purpose, regardless of the exactness of its theoretical derivation.

- **Scaling to strong backbones**: The method is demonstrated to work with SD1.5, SDXL, and Flux.1.0-dev, showing that the constraint scales to state-of-the-art generative backbones. Table 1 shows competitive LPIPS scores against SwitchLight and DiLightNet on a quantitative test set.

- **Emergent capabilities**: The ability to extract normal maps from multiple consistent inferences (Section 4.3, Eq. 7–10) without explicit normal supervision is an interesting byproduct that evidences the model's learning of consistent light transport behavior.

- **Background-conditioned relighting**: The model handles illumination harmonization using only a background image as condition (Figure 5), demonstrating generalization beyond the paired-illumination setup.

## Weaknesses

### Fatal
None.

### Major

- **Derivation of the consistency loss is mathematically incomplete, overstating the physical grounding**: The paper claims (line 78) that from the estimated clean appearance Î_L = (I_{σ_t} − ε_L)/σ_t and the light transport identity Î_{L1+L2} = Î_{L1} + Î_{L2}, it follows that ε_{L1+L2} = ε_{L1} + ε_{L2}. However, the correct algebra yields ε_{L1+L2} = ε_{L1} + ε_{L2} − I_{σ_t} — the paper drops the −I_{σ_t} term. Furthermore, the derivation assumes a single shared noisy latent I_{σ_t} for all three conditions, while the actual training (Eq. 5) uses three different noisy latents derived from three different clean images ε(I_{L1})_t, ε(I_{L2})_t, ε(I_{L1+L2})_t. The practical implementation introduces a learnable MLP φ that can absorb these discrepancies, which means the loss is a **heuristic consistency constraint** rather than a direct consequence of light transport physics as claimed. This does not invalidate the empirical contribution — the ablation shows the constraint helps — but it significantly weakens the paper's central rhetorical claim of being "physically grounded," "rooted in the physical principle," and "imposing consistent light transport." The paper should either fix the derivation or honestly characterize the loss as a physics-inspired heuristic.

- **Narrow quantitative evaluation**: Quantitative results (Table 1) are reported only on a synthetic test set of 50,000 unseen 3D renders from Objaverse. This shares the same rendering pipeline as one of the training data sources, so it is not a meaningful measure of generalization to real in-the-wild images. No quantitative evaluation is performed on standard relighting benchmarks (e.g., Multi-Illumination dataset, light-stage portraits with ground-truth lighting, or real photographs). The paper's claims of in-the-wild generalization are supported only by qualitative visual comparisons (Figure 6).

- **No scaling studies for the >10M image claim**: The paper repeatedly claims that the method enables "scalable" training on >10M images, but provides no scaling curves, no study of how performance changes with dataset size or composition, and no analysis of which data sources contribute what. Without this evidence, the scalability claim is unsubstantiated — we only know the method was trained with the full dataset, not that scaling was necessary or beneficial.

- **Ablation results are almost entirely qualitative with limited examples**: Figure 4 shows only two examples per ablation condition. The text describes changes ("red and blue differences vanished") without any quantitative metric such as albedo consistency error, color constancy error, or Frechet Inception Distance on held-out data. The paper mentions "more results in the supplementary materials" but these are absent from the submitted manuscript.

### Minor

- **MLP φ is introduced but never analyzed**: The MLP φ is described as handling domain adaptation between LDR/HDR/latent spaces, but its behavior is never examined. Does φ converge to approximately linear behavior (supporting the physical intuition) or does it learn a complex nonlinear mapping (suggesting the constraint is essentially arbitrary)? Without this analysis, the physical interpretation of the loss remains unclear.

- **Normal map extraction is presented but not validated**: The paper's own text calls this method "empirical" and notes the model is "not optimized to approximate light stage ground truths or 3D normal maps." However, it then qualitatively claims superiority over GeoWizard and DSINE. Ground-truth normal maps from synthetic data could easily validate this claim quantitatively; the absence of such validation makes this a weak piece of evidence.

- **Training schedule for data sources is described but not ablated**: The scheduled probabilities for different data sources (Section 4.1) are an important design choice that is not empirically investigated. It is unclear how much the light-stage data contributes versus the synthetic augmentations.

### Trivial
- The bracket structure in Eq. (5) appears to contain a formatting error (mismatched parentheses).
- The text mentions "supplementary material" extensively without including it.

## Nice-to-Haves

- A corrected derivation (or honest reframing) of the consistency loss that accounts for the I_{σ_t} term and the use of different noisy latents, so readers can understand what exactly the loss enforces and why.
- Ablation with quantitative metrics (albedo consistency, color constancy) to substantiate the claim that the constraint preserves intrinsic properties.
- A scaling study showing how model performance varies with dataset size (e.g., 1M, 5M, 10M).
- Evaluation on at least one real-image relighting benchmark.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The evaluation is too narrow to support the paper's ambitious claims"** (from Harsh Critic) — This is kept in the Major section above but the critic's framing as "fatal" or structural is removed. The evaluation is narrow but the paper does provide visual comparisons on real images (Figure 6) and acknowledges the synthetic evaluation bias ("this is likely due to evaluation bias towards the rendering data").

- **"The authors state this is 'empirical' which undercuts its value as evidence"** (about normal maps) — The paper's own caveat is reasonable. The normal map extraction is presented as an interesting emergent application, not core evidence. Reclassified as Minor.

- **Strength Finder's claim that the loss is "physically grounded"** — Overridden by the verified derivation issue. The constraint empirically helps but the physical grounding claim is overstated. The empirical effectiveness remains a genuine strength.

- **"No runtime comparisons, no user study"** — These are not standard requirements for this type of paper. Removed.

- **Generic strengths about "addressing an important problem"** — Removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The two independent reviews do not surface a novel observation not already present in the paper.

## Suggestions

1. **Fix the derivation in Section 3.2.** Either present a corrected derivation showing exactly what relationship the loss enforces, or honestly characterize the constraint as a physics-inspired heuristic consistency loss rather than a direct consequence of light transport. This would not diminish the paper's empirical contribution and would significantly strengthen its intellectual honesty.

2. **Add a real-image quantitative benchmark.** Even a small set of real photographs with approximately known lighting conditions (e.g., Multi-Illumination dataset or light-stage portraits) would substantially strengthen the generalization claims.

3. **Provide scaling curves.** Show how at least one metric (e.g., LPIPS on the synthetic test set) changes when training with subsets of the data (e.g., 1M, 5M, 10M images) to substantiate the scalability claim.

4. **Add quantitative ablation metrics.** Measure albedo consistency (e.g., using the in-the-wild augmentation pipeline's albedo estimates as pseudo-ground-truth) to quantify the "red and blue differences vanished" observation.

5. **Analyze the learned MLP φ.** Report whether φ converges to a near-linear function or a complex nonlinear one, to clarify how much of the physical motivation survives in practice.

## Score and Decision

The paper makes a worthwhile empirical contribution — a constraint that demonstrably helps stabilize diffusion-based illumination training across diverse data and strong backbones, supported by a large-scale data pipeline. These are the kind of practical contributions that move the field forward. However, the paper's central claim of being "physically grounded" is undermined by a genuine mathematical error in the derivation (the ε_{L1+L2} = ε_{L1} + ε_{L2} identity does not follow from light transport linearity as claimed). Additionally, the quantitative evaluation is limited to synthetic data and the scalability claims lack supporting evidence. These are serious enough to prevent acceptance in the current form but are addressable with revisions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>