## Summary
This paper investigates whether generative (decoder-based) approaches to visual perception are necessary for compositional generalization — the ability to recognize unseen combinations of known concepts. Building on Brady et al. (2025), the authors formalize the constraints required for compositional generalization in both generative and non-generative paradigms, prove that constraining a decoder to the required function class ℱ_int is straightforward while constraining an encoder to 𝒢_int is impractical (the constraints depend on the unknown geometry of OOD regions of the data manifold), and demonstrate empirically on the PUG dataset that augmenting autoencoders with generative replay and gradient-based search improves OOD compositional generalization across a range of pretrained base encoders.

## Strengths
- **Formal characterization of the asymmetry between generator and inverse generator function classes (Theorem 3.2, Lemma 3.1, Sec. 3):** The paper proves that when d_x ≥ d_z³, the Jacobian and Hessian of inverse generators g ∈ 𝒢_int can be essentially arbitrary at any point, in stark contrast to the structured block-diagonal derivatives characterizing forward generators f ∈ ℱ_int (Eq. 3.1). This provides a precise formal explanation for why decoder constraints are straightforward while encoder constraints are data-manifold-dependent. Lemma 3.1 further shows clean structure does exist when d_x = d_z, making the dimensionality argument sharp and falsifiable.

- **The n=0 ablation as a natural control experiment (Sec. 3.1, Figure 5C):** The paper identifies that when concepts do not interact (n=0, PUG-Object split), 𝒢_int becomes more structured, and predicts non-generative methods should succeed. The empirical result — near-perfect OOD accuracy for all methods on PUG-Object — validates this prediction. This bidirectional confirmation (failure when n≥1, success when n=0) substantially strengthens the theory's explanatory power.

- **Controlled empirical evaluation across a spectrum of pretrained encoders (Figures 5–6, Sec. 5):** The experiments systematically test five distinct base encoder families (from-scratch ViT, DINOv1, I-JEPA, DINOv2, CLIP, SigLIP2) spanning a wide range of pretraining scales on three carefully constructed PUG splits. The consistent pattern — OOD accuracy correlates with pretraining scale for non-generative methods, while generative methods improve OOD performance across all base encoders without additional data — is coherent with the theoretical predictions.

- **Practical instantiation of gradient-based search with encoder initialization (Sec. 4.1):** Using the ID-trained encoder as a "System 1" initialization for gradient-based "System 2" optimization of the decoder is principled and pragmatic. Empirical results show non-trivial gains from search on top of replay alone.

- **Connection to causality literature (Sec. 6):** The paper situates its findings within the causal/anti-causal learning framework, bridging representation learning and causality research in a substantive way.

## Weaknesses

### Fatal
None.

### Major
- **Overclaimed framing relative to evidence:** The title and abstract assert that "generation is required" for data-efficient perception. However, what the paper establishes is narrower: for the specific function class ℱ_int, constraining a decoder to guarantee compositional generalization is tractable while constraining an encoder is not, and on one controlled dataset, generative methods improve OOD performance over non-generative autoencoder baselines. The paper's own experiments show SigLIP2 (a non-generative method) achieving ~80% OOD accuracy on PUG-Background without any generative mechanisms, and the Discussion (line 231) acknowledges the theory is limited to ℱ_int and "may, in principle, fail to generalize to function classes associated with other settings." The paper would be considerably stronger if the claims were calibrated to match what is actually shown — namely, that generative approaches provide principled guarantees for compositional generalization that non-generative approaches lack — rather than asserting generation is categorically required.

### Minor
- **Theorem 3.2 is pointwise, weakening the infeasibility argument:** Theorem 3.2 guarantees that Dg and D²g can be arbitrary at any single point x₀, but does not establish that this lack of structure holds globally across the manifold. The paper acknowledges persistent structure on the tangent space (Eq. 3.4), but the leap from "pointwise arbitrary" to "infeasible to constrain" needs more careful qualification. The core argument — that encoder constraints are manifold-dependent and thus impractical — still holds, but the theorem's actual scope is narrower than the surrounding prose suggests.

- **No direct numerical comparison between generative and supervised non-generative methods:** Figure 5 reports supervised non-generative results and Figure 6 reports generative (unsupervised VAE + replay/search) results in separate figures. The paper never directly plots them together, making it difficult to assess whether VAE + replay/search outperforms the supervised baselines or merely improves over the unsupervised VAE baseline. The within-autoencoder comparison (w/o replay vs. w/ replay vs. w/ replay+search) is clean and valid, but the broader claim about generation being needed would benefit from a more explicit cross-paradigm comparison.

- **No error bars or variance estimates:** All results in Figures 5 and 6 are reported as single bar values without uncertainty estimates. Given the relatively small dataset (~20K images) and the use of gradient-based search (which may be sensitive to initialization), reporting variance across runs or data splits would strengthen confidence in the results.

### Trivial
- Gradient-based search hyperparameters (number of gradient steps, learning rate) are referenced to Appendix B but not reported in the main text.

## Nice-to-Haves
- Discuss the inference-time computational cost of gradient-based search relative to a single forward pass of an encoder, to give readers a complete picture of the trade-off between data efficiency and compute efficiency.
- Include a direct verification that the trained decoder approximately satisfies the cross-derivative constraints of ℱ_int (e.g., measuring ∥D²_{zk,zl} f̂(z)∥), to more tightly connect the theory to the empirical results.
- Report unstructured decoder results in the main text rather than only in Appendix C, as these help establish whether the regularized decoder architecture is responsible for the gains.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"SigLIP2 contradicts the 'generation is required' thesis"** — REMOVED. The paper's thesis is about data efficiency, not absolute impossibility. SigLIP2 achieves ~80% with web-scale pretraining, which is consistent with the claim that non-generative methods need massive data. The paper explicitly states that larger-scale pretrained models "improve OOD performance at the cost of data efficiency" (line 233-234).

- **"PUG-Object results contradict the thesis"** — REMOVED. The paper explicitly predicts and explains this result via the n=0 special case (Sec. 3.1), where 𝒢_int is more structured. This is a feature of the theory, not a contradiction.

- **"Generative methods also use pretrained encoders, so they don't prove data efficiency"** — REMOVED. The paper's claim is that generative methods improve OOD performance *without requiring additional training data*, not that they eliminate the need for any pretraining. The comparison is within-encoder: given the same base, adding replay/search improves OOD accuracy.

- **"The comparison is asymmetric because generative methods get extra compute at inference time and synthetic training data"** — PARTIALLY REMOVED. The extra compute (gradient-based search) is inherent to the generative approach being proposed; it's not an unfair advantage, it's the method. The clean ablation (VAE vs. VAE+replay vs. VAE+replay+search) makes this clear. The point about lacking comparison with supervised methods is retained as a minor weakness.

- **"Missing appendix and references"** — REMOVED per hard rules (parser strips these sections).

- **"Data contamination concerns for pretrained models"** — REMOVED per hard rules. The paper asserts PUG datasets were not in pretraining sets; we must accept this.

- **"The logical gap between G_int is hard to constrain and generation is required"** — PARTIALLY REMOVED. The paper does not claim G_int is the only route; it says that *if* guarantees are desired through the identifiability framework, generation is the practical path. The Discussion explicitly acknowledges limitations. The overclaim concern is captured in the Major weakness about framing.

- **"Lack of proofs in appendix"** — REMOVED per hard rules (appendix is stripped by parser).

- **Requesting related work additions** — REMOVED per hard rules (cannot verify existence of missing related work).

## Novel Insights
The paper's most novel insight is the formal characterization of *why* the non-generative path to compositional generalization is harder than the generative one: it is not merely an empirical accident but stems from a fundamental structural asymmetry in the function classes. For forward generators, the constraints for OOD identifiability are aligned with the global coordinate axes of the latent space and can be enforced universally; for inverse generators, the constraints must be projected onto the data manifold's tangent space, making them data-dependent and ill-posed for OOD regions. This geometric insight — illustrated in Figure 3 — provides a principled lens for understanding a pattern observed empirically across object-centric learning, causal representation learning, and compositional generalization.

## Suggestions
- Narrow the title and framing to match the evidence: e.g., "Generative Approaches Enable Tractable Guarantees for Compositional Generalization" rather than "Generation Is Required for Data-Efficient Perception." The current framing invites readers to look for counterexamples rather than appreciate the subtle but real theoretical contribution.
- Add a combined figure or table directly comparing the best generative results against the best non-generative results (both supervised and unsupervised) on PUG-Background and PUG-Texture.
- Report error bars and key search hyperparameters in the main text.
- Acknowledge the computational cost of gradient-based search explicitly in the main text, framing it as a compute-vs-data trade-off.

## Calibration

### Round 1 — Bracketing
Queried anchors across the full score range:

| Anchor | Path | Avg Score | Decision | Comparison |
|---|---|---|---|---|
| Non-Parameterized Randomization for Environmental Generalization | fvTaoyH96Z | 2.33 | Reject | Significantly weaker; narrow RL focus, less theoretical depth |
| Zephyr GAN | f6GMwpxXHG | 2.20 | Reject | Much weaker; GAN loss function paper, no compositional generalization |
| On inherent limitations of GPT/LLM Architecture | JNZ3Om6NPS | 2.00 | Reject | Much weaker; limited theoretical scope |
| Learning Identifiable Concepts for Compositional Image Generation | 0BBzwpLVpm | 4.25 | Reject | Related topic but weaker theory and smaller experimental scope |
| Correcting Flaws in Common Disentanglement Metrics | hv8l922Ad7 | 3.40 | Reject | Different focus (metrics), less substantial |
| CLIP Exhibits Improved Compositional Generalization | UVSKuh9eK5 | 5.67 | Reject | Empirical study of CLIP; current paper has stronger theory |
| Feature Accompaniment | oKglS1cFdb | 5.67 | Reject | Theory-experiment disconnect; current paper has cleaner connection |
| Next state prediction gives rise to entangled, yet compositional representations | 7QGyDi9VsO | 5.00 | Reject | Empirical focus, no identifiability theory |
| Dynamics of Concept Learning and Compositional Generalization | s1zO0YBEF8 | 6.50 | Accept | Comparable theory scope but SIM task criticized as poor model; current paper's experiments more directly connected |
| Provable Compositional Generalization for Object-Centric Learning | 7VPTUWkiDQ | 7.33 | Accept | Direct predecessor; current paper extends this work with G_int analysis |
| Cross-Entropy Is All You Need To Invert the Data Generating Process | hrqNOxpItr | 8.00 | Accept | Stronger theory (global identifiability results), cleaner contributions |

**Round 1 Bracket: 5.5 – 7.0**

### Round 2 — Narrowing
Queried anchors inside the bracket:

| Anchor | Path | Avg Score | Decision | Comparison |
|---|---|---|---|---|
| On Provable Length and Compositional Generalization | Hxm0hOxph2 | 5.25 | Reject | Different domain (sequence models); current paper has cleaner experiments |
| On the Identifiability of Nonlinear Representation Learning | 7oT1X8xjIk | 5.80 | Reject | Theory-only identifiability paper; current paper more applied and empirical |
| Feature Accompaniment | oKglS1cFdb | 5.67 | Reject | Theory-experiment disconnect more severe than current paper |
| OCEBO: Object-Centric Pretraining | 7d2JwGbxhA | 6.50 | Accept | Method-focused; current paper has more theoretical depth |
| Cycle Consistency Driven Object Discovery | f1xnBr4WD6 | 6.75 | Accept | Well-executed method paper; current paper's experimental validation less clean |

The current paper sits above the 5.25–5.80 anchors (cleaner theory-experiment connection, more comprehensive evaluation) but below the 6.50–6.75 anchors (weaker experimental validation, overclaim issue, pointwise theorem limitation). It is closest in spirit to the Brady et al. predecessor (7.33) but is a less crisp contribution with acknowledged limitations.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>