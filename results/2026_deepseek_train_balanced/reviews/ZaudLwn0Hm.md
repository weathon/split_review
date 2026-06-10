## Summary

The paper proposes Prototypical Evolutionary Adaptation (PEA), a method for few-shot CLIP adaptation that adds learnable shift vectors Δ_c to class-mean visual prototypes (computed from frozen CLIP features) and combines them with text prototypes for classification. The key idea is to calibrate biased prototype estimates caused by limited few-shot samples, rather than editing representations through prompts or adapters. The method reports strong average accuracy (75.15% across 12 datasets with RN-50 at 16 shots) and is evaluated across multiple datasets, shot settings, backbone architectures, and OOD generalization.

## Strengths

- **Operates on visual prototypes rather than textual ones, providing a different calibration axis from prior work.** The paper explicitly contrasts with TaskRes (Yu et al., 2023) and Sui et al. (2024), noting those methods "focus on the textual feature space" while PEA directly calibrates visual-class prototypes. This is a concretely different mechanism from the textual-residual baselines (lines 115–117).

- **Addresses a demonstrated failure mode of existing methods.** Figure 2 (line 39–40) provides evidence that visual features from the same class exhibit low similarity with both simple prompt templates and LLM-generated descriptions. This observation motivates the need for visual prototype calibration rather than further text-side engineering.

- **Minimal parameter overhead with a clean formulation.** The method learns only N shift vectors (one per class, of dimension D) and a scalar α, keeping the entire CLIP backbone frozen (Section 4.2, lines 93–98). This is substantially fewer trainable parameters than prompt-tuning or adapter-based approaches.

## Weaknesses

### Major

- **The training objective for the learnable shift vectors Δ_c is never stated.** Section 4.2 introduces the shifted prototype formulation (Eq. 5, line 98) and the classification probability (Eq. 6, line 110), but the loss function used to optimize Δ_c is absent from the paper. Cross-entropy is mentioned only in the description of Linear Probing as background (Section 3, line 54), not for PEA itself. Without this, the method is not reproducible, and it is impossible to determine whether any regularization, temperature scaling, or auxiliary loss differentiates PEA from a standard linear probe with text-initialized weights. This is not a minor omission; it is the core of the algorithm.

- **The claimed mechanism ("regulates intra-class variance," "reduces overfitting") is asserted without any direct evidence.** The abstract (line 4), introduction (lines 14, 19), and conclusion (line 148) repeatedly state that PEA "regulates intra-class feature variance" and "mitigates excessive feature variance within the same class caused by selective bias." However, the paper provides zero analysis of actual feature variance — no measurements, no visualizations of prototype trajectories, no quantification of how the shift vectors change the classifier geometry. The only evidence presented is final accuracy numbers on held-out test sets. The mechanistic claim is unsupported.

- **No component ablation isolating each term's contribution.** The classifier combines three components: text prototype t_y, mean visual prototype \bar{c}_y, and learnable shift Δ_c. The paper never ablates to show what each term contributes. For example: (a) classifier = t_y only (standard LP with text init); (b) classifier = \bar{c}_y + t_y with no learnable shifts; (c) fully PEA with Δ_c. Without this, it is unclear whether the reported gains come from the visual prototype initialization, the learnable shift, or simply the combination of text + visual features. The only ablation reported is on the scalar α (line 143), which does not address this.

### Minor

- **The initialization and dimensionality of Δ_c are unspecified.** The paper