## Summary

MIMOSA extends concept embedding models (CEM) to multimodal settings by fusing representations from image and text encoders *before* the concept layer (early fusion), creating a single shared concept embedding space. It also attaches modality-specific decoders that generate prototypical visualizations from concept embeddings alone. The paper's central empirical finding is that this shared representation eliminates discordant concept predictions — on CUB, the late-fusion baseline SHARCS exhibits 54.13% per-concept discordancy, while MIMOSA has zero by design.

---

## Strengths

- **Shared concept representation demonstrably eliminates discordant concept predictions.** Section 4.2 reports that SHARCS (late fusion) produces mismatched concept predictions 54.13% of the time on CUB, 2.44% on MNIST+, and 4.10% on cdSprites+ (rising to 26.49% and 8.88% under noise injection). MIMOSA has zero discordancy by architectural design. This is a concrete, measurable advantage over the closest prior work and is the paper's strongest piece of evidence.

- **Best task accuracy among concept-based models on the complex CUB dataset.** MIMOSA achieves a +0.1588 accuracy improvement over SHARCS, the runner-up concept-based model, on a real-world fine-grained classification task (Section 4.1). This is a meaningful result for an interpretable model on a challenging dataset.

- **Highest concept accuracy on two of three datasets with substantially lower variance.** Table 2 (Section 4.1) shows MIMOSA achieves the best concept accuracy on MNIST+ and CUB, and is within 0.0001 of the leader on cdSprites+. On CUB, SHARCS has a standard deviation of 0.3 for image-derived concepts, while MIMOSA's standard deviations are all below 0.0001 — indicating the unified representation stabilizes concept learning.

- **Explicit concept decoding from embeddings is a novel architectural contribution.** Rather than relying on post-hoc attribution (saliency maps, attention), MIMOSA trains decoders to generate prototypical concept visualizations directly from concept embeddings (Section 3.2). The approach is conceptually clean and goes beyond what prior unimodal concept visualization methods offer.

---

## Weaknesses

### Major

- **The missing late-fusion CEM baseline confounds the central accuracy comparison.** MIMOSA (early fusion, CEM-style embeddings) is compared against SHARCS (late fusion, unsupervised concept bottleneck). These differ in *both* fusion strategy *and* architecture (embedding-based vs. bottleneck-based). A late-fusion CEM — where each modality independently produces CEM-style concept embeddings fused only at the task predictor — would control for architecture while isolating the fusion strategy. Without it, the paper cannot fully distinguish whether MIMOSA's accuracy advantage on CUB comes from early fusion or from CEM's embedding-based representation. This gap does **not** affect the discordancy analysis (Section 4.2), which relies on a structural property of late fusion, but it weakens the accuracy-based argument for early fusion.

### Minor

- **Headline accuracy claims are overstated relative to the evidence.** The abstract states MIMOSA "achieves comparable accuracy with multimodal black-box models," and Contribution 1 claims "accuracy greater or close to black-box models." However, the paper's own results (Section 4.1) acknowledge that on CUB "the multimodal black-box E2E model outperforms all concept-based models." MIMOSA never exceeds the black-box on any dataset. The supported claim is "best among concept-based models on CUB," which is a meaningfully weaker statement. The framing should be corrected to match the evidence.

- **Concept decoder evaluation is entirely qualitative.** The decoder evaluation (Section 4.4, Figures 5–7) relies solely on hand-picked examples, with no human evaluation, no quantitative concept-fidelity metric, and no controlled concept-manipulation experiment. The paper candidly acknowledges "potential information leakage" for the CUB Stable Diffusion decoder (line 145), noting that reconstructed images "show a noticeable resemblance to the input image." This undercuts the claim that these visualizations reveal "what the model has internalized as the concept" (line 135). Since decoder-based visualization is listed as a contribution, this evaluation gap is nontrivial.

- **The joint training objective is not fully specified.** The paper defines the decoder loss $\mathcal{L}_{dec}$ (line 64) but never states the complete training loss — specifically, how concept prediction loss, task loss, and decoder loss are weighted and combined. This is needed for reproducibility.

- **The φ aggregation stage in the architecture is underspecified.** Equation (1) describes a two-stage process: ⊕ (pooling encoder outputs) followed by ϕ (producing concept embeddings). The paper says ϕ is "modeled as a simple sum operator" (line 55), but it is unclear what is being summed — the pooled representation itself? If ϕ is also a sum, the two-stage description is redundant. The paper defers to "implemented as described in Espinosa Zarlenga et al. (2022)," but CEM is a unimodal architecture and it is unclear how it is adapted to the pooled multimodal input.

### Trivial

- The intervention results on CUB are described qualitatively ("most significant impact," line 119) without providing numerical accuracy figures in text. Figure 3 plots the results but the text should include at least the key numbers.

---

## Nice-to-Haves

- **A pooling-strategy ablation** (sum vs. mean vs. attention for both ⊕ and ϕ) would strengthen confidence in the architectural choices, especially since the current method uses sum-then-sum with no alternatives tested.
- **A controlled concept manipulation experiment for the decoders** (e.g., intervene on a specific concept embedding and measure whether decoder output changes in the expected direction) would move the decoder evaluation from anecdotal to evidential.
- Quantitative intervention results (final accuracy after correction, improvement over baseline) should be reported in the text alongside Figure 3.

---

## Removed Points

The following points from the inputs were removed under the filtering rules:

1. **"All tables are embedded as images and no numerical results appear in text"** — This is a PDF-parsing artifact; the original submission has proper tables. Removed per the rule about formatting artifacts.
2. **Strength: "Concept interventions improve task accuracy on all three datasets"** — Partially retained in spirit but the lack of numerical support in text makes it too vague to keep as a standalone strength. Moved here.
3. **Criticism about "no full objective function" being fatal** — Demoted from the harsh critic's framing to Minor; this is a reproducibility gap but not a fatal flaw.
4. **Criticism that the "method specification is underspecified for reproducibility" framed as a structural issue** — The underspecification is real but addresses only one aspect (the ϕ module). Demoted from the critic's "Critical Issues" framing to Minor.

---

## Novel Insights

The harsh critic's strongest insight is distinguishing between two confounded claims in the paper: (a) early fusion of concept representations avoids discordancy, and (b) CEM-style embedding-based concept representations improve accuracy. The paper's evidence cleanly supports (a) but only partially supports (b), because no late-fusion CEM baseline exists to decouple the two variables. This distinction is not drawn in the paper itself and could usefully inform future work.

The discordancy analysis under distribution shift (noise injection magnifying discordancy from 2.44% to 26.49% on MNIST+) is a methodological contribution that the paper treats as a supporting experiment but that is actually its strongest and most novel finding. Future work on multimodal concept models should adopt this as a standard diagnostic.

---

## Suggestions

1. Add a late-fusion CEM baseline (each modality produces independent CEM-style embeddings, fused just before the task predictor). This is the single highest-leverage improvement.
2. Correct the abstract and contribution list: replace "accuracy greater or close to black-box models" with "best accuracy among concept-based multimodal models."
3. State the full training objective function explicitly, including loss weights.
4. Clarify the ϕ aggregation stage: what is summed, and how the CEM module is adapted from unimodal to multimodal input.
5. For the decoder evaluation, add a quantitative metric (e.g., concept-fidelity score from controlled interventions on individual concept embeddings).

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>