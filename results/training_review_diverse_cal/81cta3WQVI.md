Now I have all the evidence I need. Let me construct the final review.

---

## Summary

This paper proposes EdgeRunner, an auto-regressive auto-encoder (ArAE) pipeline for mesh generation. The key ideas are: (1) a novel EdgeBreaker-based mesh tokenization that achieves ~50% compression (4–5 tokens per face vs. 9 in prior methods), enabling support for up to 4,000 faces; (2) an ArAE that compresses variable-length tokenized meshes into fixed-length latent codes; and (3) a latent diffusion model (DiT) trained on these latent codes for image-conditioned mesh generation, with coarse-grained face-count control. The approach aims to overcome limitations of prior auto-regressive mesh generators in face count, resolution, and cross-modal generalization.

## Strengths

1. **Compact mesh tokenization with measurable 50% compression.** The EdgeBreaker-based traversal shares edges between adjacent faces, achieving 4–5 tokens per face vs. the 9 tokens used by prior methods (MeshAnything, MeshXL). The paper provides a quantitative comparison (Table 1) with the AMT tokenizer from MeshAnythingV2, showing similar amortized compression but fewer sub-sequences due to bidirectional traversal. This is the paper's strongest validated contribution and directly enables the increase to 4,000-face generation.

2. **ArAE converts variable-length meshes to fixed-length latent codes, enabling latent diffusion for cross-modal conditioning.** The architecture (lightweight point-cloud encoder with cross-attention outputs a fixed-size latent Z ∈ ℝ^{M×L}; an auto-regressive decoder reconstructs the mesh) is well-motivated and unlocks image-conditioned generation that prior auto-regressive mesh methods cannot directly handle. The ablation (Figure 5, right) provides preliminary evidence that this two-stage approach outperforms direct auto-regressive image conditioning.

3. **Coarse-grained face-count control through a learnable conditioning token.** Bucketing face counts into ranges and appending a corresponding token (Section 3.2) is a simple but practical contribution, demonstrated qualitatively in Figure 6. This feature is absent in prior auto-regressive mesh generators and addresses a real user need (low-poly vs. high-poly control).

4. **Qualitative generalization to out-of-domain inputs.** Figure 4 shows the model producing plausible meshes from 2D-style artwork and realistic photographs despite training on rendered 3D views, while the optimization-based baseline (Unique3D) produces artifacts on the same inputs. This provides visual evidence of robustness.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of generation quality, despite strong comparative claims.** The paper asserts "superior quality, diversity, and generalization capabilities" (abstract) but provides no standard generation-quality metrics: no FID on rendered views, no Coverage/MMD on point-cloud representations, no Chamfer distance against ground truth, no user study. The section titled "Quantitative Results" (Section 4.2) only compares the tokenization algorithm (Table 1) and reports inference speed — it contains zero numbers about the quality of generated meshes. Every comparative claim against MeshAnything, MeshAnythingV2, Unique3D, CLAY, and CraftsMan rests entirely on 3–4 cherry-picked qualitative examples per figure. In a field where quantitative evaluation on held-out test sets is standard practice (MeshGPT, MeshXL, MeshAnythingV2 all report metrics), this gap prevents rigorous assessment of whether ArAE actually improves over prior methods. The paper reads as a promising technical report rather than a validated method.

2. **Very limited ablation studies.** Section 4.3 contains exactly two ablations (quantization resolution 128³ vs. 512³; direct image conditioning vs. ArAE + latent diffusion), both shown qualitatively on one or two examples. Key design choices central to the paper's contribution are not ablated: the tokenization algorithm itself (bidirectional traversal vs. fixed-side traversal; number of sub-sequences; N vs. P token design choices), the latent size M and dimension L, the point-cloud sampling density N, the regularization loss weight, and the face-count bucket design. Without systematic ablation, it is impossible to attribute observed (qualitative) improvements to specific components or to know whether simpler alternatives would work as well.

### Minor

1. **Incomplete baseline comparisons.** For point-cloud-conditioned generation, only MeshAnything (v1/v2) is compared; MeshGPT (unconditional) and MeshXL are discussed in related work but not compared, even for unconditional generation where they are applicable. For image-conditioned generation, the sole baseline is Unique3D (an optimization-based method), with the explanation that "other auto-regressive methods cannot directly condition on images" — this is reasonable but still leaves the reader unable to situate the method relative to the broader field of feed-forward image-to-mesh methods (e.g., CRM, MeshLRM). Expanding the comparison set (even qualitatively for more samples) would substantially strengthen the evaluation.

2. **ArAE generalization claim is under-supported.** The paper claims that ArAE + latent diffusion offers "better generalization" than direct auto-regressive conditioning (a central motivation). The evidence is Figure 5 (right): one qualitative example. No systematic evaluation on a held-out test set with varied input styles, no distribution-shift robustness metrics, and no ablation of latent size or diffusion model parameters is provided. The claim may be correct but is not convincingly demonstrated.

3. **Missing training details compromise reproducibility.** The paper does not specify the dataset (Objaverse is cited in related work but not stated as the training source), the number of GPUs or training steps, learning rate, batch size, or the exact number of layers/dimensions in the encoder and decoder. The latent diffusion model's architecture (depth, FLOPs, number of diffusion steps, noise schedule, classifier-free guidance) is not described. While some details may be in a stripped appendix, the main paper should at minimum state the training dataset and key hyperparameters for a practical generation method.

4. **"Artistic" is used as an unexplained normative label.** The title and framing emphasize "artistic mesh generation," but the term is never defined or operationalized. It appears to refer to meshes with clean topology and regular face structures (in contrast to post-processed meshes from implicit representations), but the paper does not establish this connection explicitly.

### Trivial

- **Inference speed reported without comparison.** The paper states ~45s for 1K faces and ~3min for 4K faces on an A100, but provides no speed comparison to prior auto-regressive methods (MeshAnything, MeshXL, MeshGPT), so the reader cannot assess whether this is fast or slow relative to baselines.

## Nice-to-Haves

- A discussion of failure cases and limitations (e.g., intricate topology, non-manifold meshes, arbitrary genus, very large face counts) would strengthen the paper by showing honest scoping.
- An evaluation of face-count control accuracy (e.g., a histogram of actual face counts per bucket over a test set) would quantitatively validate an advertised feature.
- A per-face token count distribution on the training dataset (compared to AMT and a naive baseline) would strengthen the tokenization efficiency claim beyond averages.
- Comparing against feed-forward image-to-mesh methods (CRM, MeshLRM) for the image-conditioned setting, even if only qualitatively on a set of 10+ test samples, would help situate the method.

## Removed Points

These points were flagged by reviewers but are removed for the reasons stated below:
- **"Point-cloud sampling strategy is unclear"** — The paper explicitly states "sample N random points" (line 185). This is clear. Removed as factually wrong.
- **"Lossless face compression is misleading"** — "Face compression" in mesh compression terminology refers to connectivity/topology, which is indeed losslessly compressed via EdgeBreaker traversal. Vertex quantization is a separate, explicitly disclosed step. Removed as it misunderstands the paper's claim.
- **"Notation is dense and uses non-standard symbols"** — Pure formatting/style nitpick. The notation is specific to the method, which is normal. Removed per hard rules.
- **"Missing related works"** — The paper fully cites MeshGPT, MeshXL, PivotMesh, and MeshAnything in Section 2.4 (Auto-regressive Mesh Generation). The critic's concern is about experimental comparison, not citation. Not a related-work omission.

## Novel Insights

The reviews reveal a tension that the paper does not adequately address: the core technical contributions (tokenization, ArAE architecture) are promising and partially validated, but the evaluation is structurally disconnected from the claims. The tokenization efficiency is quantified but treated as an end in itself, while the downstream generation quality — which is what "EdgeRunner" is ultimately selling — is left to qualitative judgment. This mismatch between the rigor of the technical development and the looseness of the experimental validation is the paper's central weakness, and it is fixable without changing the method.

## Suggestions

1. **Add quantitative generation metrics immediately.** Compute FID/KID on rendered views, Coverage/MMD on point-cloud representations, and Chamfer distance against ground truth for a held-out test set. Compare against MeshAnythingV2, MeshGPT (unconditional), and a representative image-to-mesh method. Even a single table with these numbers would transform the paper from "interesting proposal" to "validated method."
2. **Add systematic ablations of the tokenization algorithm** (compare to fixed-side traversal; vary trajectory direction choices), the latent dimension M/L, and the point-cloud sampling density N. Show these with quantitative metrics, not just visuals.
3. **State the training dataset, key hyperparameters, and compute budget** — even briefly — to establish reproducibility. If details are in an appendix, reference it explicitly.
4. **Test the generalization claim explicitly** by evaluating on a deliberately out-of-domain subset (e.g., stylized images, non-watertight inputs) with quantitative metrics, rather than relying on one qualitative example.
5. **Expand the baseline comparison** to at least include qualitative side-by-sides for MeshGPT (unconditional generation on held-out shapes) and one feed-forward image-to-mesh method.

## Score and Decision

The paper introduces genuinely useful ideas (compact EdgeBreaker-based tokenization, ArAE for mesh-to-latent compression, face-count control) that address real limitations in auto-regressive mesh generation. The technical development is sensible. However, the evaluation is fundamentally incomplete: the paper makes strong comparative claims ("superior quality, better generalization") but provides no quantitative evidence to support them, relying entirely on a handful of cherry-pickable qualitative examples. The ablation studies are too few and also qualitative. In the current state, the paper does not meet the evidentiary standard required to validate its central claims. A major revision adding quantitative metrics, more baselines, and systematic ablations could make this a strong paper, but as presented the contribution cannot be properly assessed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>