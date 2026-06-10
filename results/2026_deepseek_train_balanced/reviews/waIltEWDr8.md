## Summary

WASUP combines B-cos weight-input alignment with case-based reasoning via class-support vectors to create an inherently interpretable classifier that provides both local (pixel-level contribution maps via B-cos) and global (prototypical support-vector) explanations. The paper provides axiomatic faithfulness proofs and evaluates on three tasks (Pascal VOC, Stanford Dogs, RSNA) with three backbone architectures (DenseNet121, ResNet50, Hybrid ViT).

## Strengths

1. **Theoretical faithfulness guarantee via axiom satisfaction**: WASUP's explanations are proven to satisfy all six Sundararajan et al. (2017) axioms (Completeness, Sensitivity, Implementation Invariance, Dummy, Linearity, Symmetry-Preserving), with proofs provided in the appendix. This directly counters a known failure of prior prototypical networks — Wolf et al. (2024) showed ProtoPNet explanations are generally unfaithful due to the spatial disconnect between input and latent space (line 32). The B-cos transform's property of summarizing any forward pass as a single input-dependent linear transformation (Eqs. 4–7) is the technical foundation that makes this possible.

2. **Multi-label classification capability**: By replacing the Nadaraya-Watson head's softmax normalization (which sums to one, line 56) with sigmoid + binary cross-entropy loss (Section 3.2), WASUP structurally overcomes a key limitation of its predecessor, enabling simultaneous multi-class predictions under a standard threshold of 0.5. This is validated on Pascal VOC (multi-label, line 159).

3. **Architecture-agnostic design validated across three backbone families**: Experiments span an order of magnitude in parameters — DenseNet121 (~8M), ResNet50 (~26M), and Hybrid Vision Transformer (~81M) — including both CNNs and transformer-based architectures (line 159). This supports the claim that the method does not constrain backbone capacity.

4. **Quantitative debugging mechanism**: The Silhouette score (0.655, line 174) and t-SNE analysis of support vectors provide a concrete, quantitative approach to identifying weak latent representations, going beyond purely qualitative explanation visualization.

## Weaknesses

### Fatal
None.

### Major

1. **The similarity measure sim() is never defined** (lines 108–114, Eq. 5). The core classification mechanism computes logits as μ_c = b + Σ sim(f⁺, vᵢᶜ)/τ, but the function sim() is never specified. Is it cosine similarity? Dot product? Negative L2 distance? B-cos similarity? A bespoke formulation? This is not a minor implementation detail — it is the central operation that converts latent representations into class logits. Without knowing what sim() is, the method cannot be reproduced, and the faithfulness proofs in the appendix cannot be verified against the actual implementation. The paper later claims (line 150) that "The B-cos properties of WASUP allow us to faithfully compute the RGBA explanations in terms of the similarity measure," which cannot be evaluated without knowing what the similarity measure is.

2. **No comparison against any inherently interpretable baseline**. The introduction (lines 32–33) positions WASUP as superior to ProtoPNet, ProtoTree, Pip-Net, XProtoNet by criticizing their unfaithful explanations and spatial misalignment. Yet the experiments (line 161) compare WASUP only to *black-box* versions of the backbones. There is no accuracy comparison against ProtoPNet, Pip-Net, or the Nadaraya-Watson head on any dataset. There is no explanation-quality comparison (pointing game, insertion/deletion, ROAR, or any other metric) against any interpretable baseline. The paper's core thesis — that WASUP improves upon existing interpretable models — is asserted but never empirically tested.

3. **No quantitative evaluation of explanation faithfulness**. The RSNA dataset has bounding boxes for lung opacities that could be used for a quantitative pointing-game or IoU evaluation of whether explanation mass falls inside medically relevant regions. The paper only states qualitatively "we observe a high degree of intersection between significant test sample contributions and bounding boxes" (line 172). The axiomatic proofs establish mathematical consistency but do not substitute for empirical measurement — especially since the B-cos mapping from latent space to input space depends on learned representations that may be imperfect.

4. **The ⊕ function used is never specified** (line 114). The paper lists "exponential function, absolute value, and ReLU" as examples but never states which was actually used in the experiments. This choice affects whether the non-negative constraint is strict, whether gradients vanish, and the range of resulting similarity scores. The method cannot be reproduced without this information.

### Minor

1. **Minimal quantitative accuracy reporting in the main text**. The only accuracy numbers appear in a single sentence (line 161) referencing an appendix table, without naming the metric for Pascal VOC (is it mAP?), and without standard errors or confidence intervals. A main-text table with accuracy/mAP across datasets and backbones would be standard for a claims paper.

2. **No ablation studies**. Several design choices — the number of support vectors N_s, temperature τ, the ⊕ function choice, BCE vs. CE loss, k-means vs. random support vector selection — are never ablated. The paper builds on the Nadaraya-Watson head (Wang & Sabuncu, 2022) but never compares directly against this simpler baseline. Without isolating which components drive performance or explanation quality, the reader cannot tell whether WASUP's complexity is justified.

3. **Key hyperparameters not reported**. Neither N_s (number of support vectors per class) nor τ (temperature) values are given for any of the three datasets or three backbones.

4. **Overstated generality claim about backbones**. Line 33 states WASUP "can implement any neural network architecture (e.g., ResNets, Transformers, Mamba) in its feature extractor without limiting their computational capacity," but the backbone requires B-cos modifications (removing biases, replacing standard linear layers with B-cos transformations). The experiments use "B-cos versions" of backbones (line 159). The claim should clarify that the backbone must be a B-cos variant, rather than implying any off-the-shelf architecture works directly.

### Trivial
None.

## Nice-to-Haves
- Adding a main-text accuracy table comparing WASUP to both black-box backbones AND interpretable baselines (ProtoPNet, Pip-Net, Nadaraya-Watson head).
- Conducting a quantitative faithfulness evaluation on RSNA using the available bounding boxes (e.g., percentage of explanation mass inside bounding boxes).
- Performing ablation studies on N_s, τ, ⊕ function, and BCE vs. CE loss.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **"No quantitative accuracy results in the main paper"** — Removed because line 161 DOES contain quantitative accuracy numbers (≥ +0.29% on Pascal VOC, −3.7% on Stanford Dogs, −0.65% on RSNA). The paper has minimal quantitative reporting but not "none." Replaced with a more accurate Minor weakness.
- **"The debugging section raises concern about weak latent representation"** — The paper deliberately identifies a weak latent representation as a *demonstration of debugging capability*, not as a flaw in the method. This is a feature of the approach.
- **"k-means scaling claim is unsupported"** — The paper's observation about decision-critical fields having fewer classes is a discussion point, not a core empirical claim.
- **"Standard error not reported"** — Single-run evaluation is standard for large-scale image classification benchmarks.
- **"Analysis of wrong predictions is purely speculative"** — This is subsumed by Major weakness #3 (no quantitative faithfulness evaluation).
- **"B-cos requiring architectural modifications overstates generality"** — Already captured in weakened form as Minor weakness #4.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Specify the similarity measure sim() explicitly (e.g., "we use cosine similarity" or "we use the B-cos transformation as the similarity measure").
2. Add a main-text table reporting accuracy/mAP across all methods, including at least one interpretable baseline (ProtoPNet or the original Nadaraya-Watson head).
3. Report N_s and τ values for each experimental configuration.
4. Specify which ⊕ function was used and why.
5. Add a quantitative faithfulness evaluation on RSNA using the bounding boxes.
6. Clarify that the backbone requires B-cos modifications rather than claiming compatibility with any architecture out of the box.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>