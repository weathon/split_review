Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes treating the full network parameters of individually trained signed distance functions (SDFs) — "level-set parameters" — as a continuous data modality for 3D shape analysis. To handle the non-Euclidean nature of these parameters, the paper formulates them as a pseudo-normal distribution θ = μ + Δθ with a learned shared prior μ, and introduces a hypernetwork (HyperSE3-SDF) that generates pose-dependent first-layer parameters from SE(3) inputs. The representation is evaluated on shape classification (ShapeNet, Manifold40), retrieval, and 6D object pose estimation, demonstrating that analysis from continuous parameters can match or exceed point-cloud-based methods under arbitrary rotations.

## Strengths

1. **First systematic demonstration that full SDF network parameters can serve as a data modality for pose-related shape analysis.** The paper constructs level-set parameter datasets for 17,656 ShapeNet shapes and 10,859 Manifold40 shapes and shows they encode discriminative semantic information. Under the challenging z/SO(3) setup on ShapeNet (Table 2), the proposed method achieves 87.7% classification accuracy, outperforming rotation-equivariant point-cloud networks (best prior: 87.1%, VR-Net). This directly supports the claim that continuous representations enable semantic analysis in arbitrary poses.

2. **HyperSE3-SDF, a hypernetwork architecture that generates pose-dependent first-layer SDF parameters from SE(3) inputs.** The architecture is described in §3.1 with specific dimensions and the latent matrix mechanism. Table 1 shows that HyperSE3-SDF (85.9% under z/SO(3)) substantially outperforms a plain SDF with Euclidean weight transformations (79.8%), confirming that the dedicated hypernetwork is necessary for pose-related analysis of continuous representations.

3. **A correspondence-free 6D pose estimation method that requires only the SDF reconstruction loss and a multi-initialization strategy (§4.2, Algorithm 2).** Table 4 shows it achieves 2.94° RRE on clean partial point clouds and degrades gracefully to 4.93° RRE under 3 cm noise + 30% outliers, where ICP and FGR fail entirely and TEASER++ degrades to 42.92° RRE. This demonstrates the feasibility of using level-set parameters for robust pose estimation from partial views.

4. **Encoder architecture that processes the full tensor structure of level-set parameters and achieves state-of-the-art shape retrieval on Manifold40 under arbitrary rotations.** The three-branch encoder (Figure 2) processes all SDF layers. Table 3 shows 70.7% mAP under SO(3)/SO(3), surpassing point-cloud baselines (best: 66.5%, MVCNN), supporting the claim that continuous representations capture discriminative features without resolution discretization issues.

5. **Ablation validating the learned shared prior μ (§5.1, Table 1, Figure 3).** The t-SNE plots show that learned μ yields clearly separated semantic clusters while random μ produces entangled embeddings. Quantitatively, learned μ improves classification from 55.4% (random μ) to 85.9% under HyperSE3-SDF, providing strong evidence that aligning shapes in parameter space via a shared prior is critical.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison to other neural-field-based continuous representations weakens the "novel data modality" claim.** The paper claims level-set parameters are a "novel data modality" but compares only against point-cloud methods. The most natural baselines for a continuous neural-field representation are alternative continuous representations from the same family — specifically, DeepSDF latent codes (Park et al., 2019) or the modulation vectors of Dupont et al. (2022). These are also continuous numerical shape representations, are more compact, and are already known to support classification. The paper cites Dupont et al. (2022) but does not compare quantitatively. Without this comparison, the reader cannot tell whether the advantage comes from using full network parameters rather than latent/modulation vectors, or from the specific encoder+hypernetwork pipeline. This gap undermines the paper's central contribution claim. (Sections 2.3, 5.2, 5.3)

2. **The pose estimation evaluation (§5.3, Table 4) compares across fundamentally different information regimes.** The proposed method assumes access to the complete level-set parameters of the reference shape — i.e., a full continuous SDF model defining the entire surface. The baselines (ICP, FGR, TEASER++) receive only the reference point cloud — discrete samples with no underlying model. An implicit representation naturally helps with partial views and noise. A more controlled comparison would give the baselines the same implicit prior (e.g., registering to a DeepSDF) or restrict the proposed method to point-cloud-only inputs. As presented, the experimental design conflates the benefit of the implicit representation with the benefit of the method itself, making the claimed superiority unsurprising.

### Minor

3. **The paper oversells the "inherent separation" of pose-dependent and pose-independent subsets.** The introduction states that "the inherent separation of pose-dependent and pose-independent subsets in level-set parameters enables classification... to be simple and outperform equivariant networks." However, the paper itself shows that a simple Euclidean transformation of the first-layer weights (Eq. 4) does not produce comparable results (Table 1: 79.8% vs. 85.9%). This means the effective separation is *engineered* through the hypernetwork and the pseudo-normal decomposition, not inherent to the representation itself. The claim should be rephrased to reflect that the pipeline jointly achieves this separation. (§1, §3.1, Table 1)

4. **No ablation isolates the contribution of the level-set representation from the contribution of the tailor-made encoder.** The semantic learning pipeline combines (a) the level-set representation, (b) a specifically designed three-branch encoder, (c) a transformer, and (d) the μ normalization. Table 1 isolates the effect of μ and the hypernetwork, but there is no control experiment where a simpler encoder (e.g., an MLP on concatenated parameters) is used, or where the same three-branch encoder processes point coordinates. This makes it difficult to determine whether the performance advantage over point-cloud methods is due to the continuous representation or the encoder architecture. (§4.1, Table 2)

5. **No comparison to prior level-set parameter works (Luigi et al., 2023; Erkoç et al., 2023).** The paper convincingly argues (§2.3) that these methods have limitations (random initialization, small networks, dependence on traditional data), but never provides quantitative evidence that the proposed approach improves upon them. Even a simple classification comparison on the same data would substantiate the claimed improvements. (§2.3)

6. **Hypernetwork design choices are under-ablated.** Only the first-layer parameters are generated, but there is no analysis of whether generating multiple layers would improve performance, or whether smaller latent matrices Y^{mn} could suffice. The paper reports only the chosen configuration without exploring the design space. (§3.1)

7. **No statistical variance reported for main results.** Tables 1–4 report single numbers with no error bars, confidence intervals, or runs with different random seeds. Given the randomness in transformations, initialization, and training, variance estimates would meaningfully strengthen confidence in the reported improvements.

8. **Pose estimation runtime (~50s) is slow, and no breakdown is provided.** The paper acknowledges this but does not break down the cost (SDF fitting, hypernetwork inference, optimization iterations). This makes it hard to assess practical feasibility.

### Trivial

- The plane example (n_x, n_y, n_z, d) in the introduction suggests a trivial Euclidean structure that the full SDF network parameters do not possess. Removing or qualifying this example would avoid confusion.
- The paper states "hundreds of training iterations" for stage two fitting (§3.2) without giving a precise range. A concrete number would aid reproducibility.

## Nice-to-Haves

- A comparison to DeepSDF latent codes or Dupont et al.'s modulation vectors under the same encoder and tasks would be the single highest-leverage addition for substantiating the core claim.
- An analysis of how many shapes are discarded by the Chamfer filter (§5) and whether filtering biases the dataset toward simpler shapes.
- A discussion of the relationship between network size, parameter count, and reconstruction quality — how does the 8-layer/256-neuron architecture constrain the representable shapes?
- An exploration of whether the hypernetwork approach generalizes to other SDF architectures (e.g., SIREN, occupancy networks).

## Removed Points
- *"Algorithm 1 box is not fully transcribed"* — This is a PDF parsing artifact. The algorithm exists in the original submission.
- *"Several details are unclear (e.g., how many shapes used to train μ)"* — The paper explicitly states "20 shapes from each class in ShapeNet and 7 shapes per class in Manifold40" (line 166).
- *"Section 5.1 should show whether level-set parameters with random μ preserve shape identity"* — This is exactly what Table 1 and Figure 3 show: random μ yields 55.4% accuracy, indicating poor shape identity preservation.
- *"Limitations section understates the local feature issue"* — The paper clearly states: "they are not suitable for learning local features of 3D shapes, as there is no correspondence between the local structures of the shape and subsets of the level-set parameters" (line 235). This is appropriately candid.
- *"Point cloud baselines are too old (2017–2021)"* — The comparison includes VR-Net (2022), which is recent. Equivariant network methods are a well-defined subfield, and claiming newer methods would be stronger is speculative and not constructive as a criticism.
- *"The paper should also cover Y / domain Z"* beyond its scope — e.g., deep learning registration methods (GeoTransformer) are mentioned but not evaluated; the paper explains this is due to absence of training data, which is a reasonable scope choice.

## Novel Insights

The reviews surface one genuinely insightful observation that goes beyond the paper's own framing: the paper's contributions are not primarily about a "new data modality" but rather about showing that the full weight space of SDF networks — when properly aligned via a learned shared prior — encodes geometric structure in a way that supports semantic and geometric analysis. The hypernetwork is the mechanism that makes this practical for pose-varying analysis, but the real insight is the alignment itself (μ + Δθ decomposition). A revision that reframes the contribution around this alignment mechanism rather than the "novel data modality" would better match the evidence and be harder to attack. The reviews also correctly note that the paper's strongest evidence is the z/SO(3) classification result — but this could be driven by the encoder architecture just as much as the representation, and the paper does not disentangle these factors.

## Suggestions

1. **Add comparisons to DeepSDF latent codes and/or Dupont et al.'s modulation vectors** under the same classifier encoder (or a simplified version). If level-set parameters outperform them, the "novel data modality" claim is strongly supported. If not, reframe the contribution around the hypernetwork-enabled pose-dependent analysis rather than the representation itself.

2. **Add a control experiment** applying a neural network to point cloud inputs with a similar (or the same) encoder architecture, to estimate how much of the performance gap is due to the representation vs. the architecture.

3. **For pose estimation, add a baseline where the reference is represented by a DeepSDF** (or occupancy network) to control for the advantage of having an implicit representation. This would isolate whether the hypernetwork-based transformation adds value beyond the implicit prior.

4. **Rephrase "inherent separation"** to "learned/engineered separation" or "the hypernetwork achieves a separation of pose-dependent and pose-independent parameters, which enables..." to avoid overclaiming.

5. **Report standard deviations** for all main results (Tables 1–4) across multiple runs or seeds, and provide a runtime breakdown for the pose estimation pipeline.

## Score and Decision

This paper tackles a genuinely novel direction — using the full weight space of learned SDFs as a representation for downstream 3D analysis. The technical contributions (HyperSE3-SDF, the μ + Δθ decomposition, the encoder, the pose estimation method) are solid and the experiments are reasonably extensive. However, the paper's central claim — that level-set parameters are a "novel data modality" — is inadequately supported by the missing comparison to other continuous neural-field representations (DeepSDF latent codes, modulation vectors). The pose estimation evaluation is also confounded by asymmetric information access. These are substantive gaps, but they are addressable. The paper would benefit from a major revision to add the missing comparisons and control experiments, and to reframe its claims to match its evidence more precisely. In its current form, the contribution is promising but incompletely validated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>