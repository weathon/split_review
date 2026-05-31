## Summary

MVLight proposes a light-conditioned multi-view diffusion model that takes explicit HDR lighting as input, alongside text prompts and camera poses, and generates consistent multi-view RGB, albedo, and normal maps. Using this model within a Score Distillation Sampling (SDS) pipeline — where the same HDR map drives both the diffusion prior and the PBR material optimization — the method enables "non-blind" PBR estimation, aiming to produce relightable 3D assets with cleanly decomposed light-dependent and light-independent components. The core architectural novelty is the light cross-attention mechanism with high/low-frequency HDR encoding, and the two-stage SDS pipeline jointly supervising normal, albedo, and RGB.

---

## Strengths

1. **First light-conditioned multi-view diffusion model.** The paper introduces a novel architectural design (Sec. 3.1, Fig. 1) that integrates HDR lighting via high/low-frequency decomposition, VAE encoding, and a dedicated light cross-attention module. This goes beyond prior multi-view models (MVDream, RichDreamer, UniDream) that do not condition on lighting at all, enabling the model to generate multi-view images that explicitly reflect specified lighting environments.

2. **Multi-modal SDS with joint normal, albedo, and RGB supervision.** The SDS loss (Eq. 2) simultaneously optimizes three modalities under light-conditioned diffusion guidance. The ablation (Fig. 6, "Effectiveness of multi-modal SDS") shows that this produces smoother normal maps and more accurate, deshadowed albedo compared to single-modal SDS used in prior work, directly supporting the claim of improved geometric fidelity and material decomposition.

3. **Light-aware (non-blind) PBR fine-tuning.** The method uses the same HDR map for both the diffusion model in SDS and the PBR material optimization (Sec. 3.2, Fig. 2). The ablation in Fig. 7 ("Light-aware vs blind PBR estimation") demonstrates that this alignment avoids baking lighting into albedo — a key limitation of Fantasia3D and RichDreamer — yielding albedo maps that are substantially cleaner, and significantly better relighting under unseen HDR environments.

4. **Large-scale multi-view multi-light training dataset.** The custom Objaverse-based dataset (8.6M images, ~90K objects, 450 HDR environments, 4 random lights per object, Sec. 4.1) is a significant data-engineering effort that underlies the model's ability to learn lighting-aware generation. This scale of multi-light, multi-view data is novel relative to prior relightable 3D methods.

5. **User study with clear preference.** A 24-participant user study evaluating 40 prompts (Fig. 5) shows MVLight preferred 63% of the time over DreamFusion, Fantasia3D, MVDream, and RichDreamer, validating that the improvements translate to perceptible quality gains.

---

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of relighting quality or material decomposition accuracy.** The paper's central claim is that explicit lighting conditioning enables "more accurate PBR material estimation and improved relighting performance" (Sec. 4.2, Fig. 3). Yet the metrics reported — CLIP score (Table 1, text–image alignment) and user study (overall visual quality) — do not directly measure relighting fidelity or material decomposition. The ablations (Figs. 6, 7) are qualitative only. The training dataset contains ground-truth albedo, normal, and HDR-lit renders for ~90K Objaverse objects, which could have been used to compute quantitative metrics (e.g., PSNR/SSIM/LPIPS between predicted and ground-truth renders under novel lighting, albedo MSE). Without this, the core technical claim — that lighting conditioning improves disentanglement of light-dependent/independent components — rests on visual inspection alone. This is the most consequential gap in the paper.

2. **Potential mismatch between the simplified Stage-1 renderer and the diffusion model's training data is not discussed.** In Stage 1 of SDS (geometry and appearance optimization), MVLight uses a simplified PBR model where "the lighting intensity is assumed to be uniform across the object's surface for each lighting environment" and final RGB = ambient light × albedo (Sec. 3.2). This is a Lambertian assumption with no specular or roughness effects. Meanwhile, the diffusion model was trained on Objaverse renders under HDR environment maps that likely produce complex shading (specular highlights, reflections, environment-dependent effects). The SDS loss (Eq. 2) directly penalizes the difference between the NeRF render (simplified) and the diffusion prediction (trained on potentially full-PBR renders). If the diffusion predicts a specular highlight that the simplified renderer cannot produce, the optimization could bake that into albedo or distort geometry — the very failure mode the method claims to avoid. The paper does not discuss this mismatch or justify why the simplified model is sufficient.

### Minor

1. **No ablation isolating lighting conditioning in the diffusion model from other changes.** The method introduces two novel components: (a) lighting-conditioned diffusion, and (b) multi-modal SDS. The ablation in Fig. 6 tests multi-modal SDS vs. single-modal SDS, and Fig. 7 tests light-aware vs. blind PBR. But neither ablation isolates *whether the diffusion model's ability to condition on lighting* helps independently of the multi-modal supervision and data scale. A controlled comparison — same architecture with vs. without light conditioning, holding other factors equal — would strengthen the attribution. The current comparisons against MVDream and RichDreamer change multiple variables simultaneously.

2. **No comparison against UniDream.** UniDream (cited in Sec. 2) is a directly relevant baseline that also generates albedo and normal maps via a multi-view diffusion model for relightable 3D. The paper compares against DreamFusion, Fantasia3D, MVDream, and RichDreamer but omits UniDream. The stated criterion is "available code and checkpoints," but UniDream's relevance to the paper's contribution makes its omission a gap worth addressing.

3. **Dataset rendering pipeline details are not specified.** The paper does not state which renderer, material model (e.g., Disney BSDF, Lambertian+depth), or BRDF integration method was used to create the training dataset. Since the method's core logic depends on the type of shading present in the training renders, this information affects reproducibility and the assessment of the simplified-vs-full-PBR concern.

### Trivial
None.

---

## Nice-to-Haves

- **Confidence intervals for CLIP scores.** CLIP scores in Table 1 are reported as point estimates from a single run; providing variance (e.g., across multiple seeds or bootstrapped over prompts) would strengthen the quantitative claim.
- **Sanity-check evaluation of the diffusion model's HDR fidelity.** A simple metric (PSNR between the diffusion model's predicted output under a given HDR and a ground-truth render from the same HDR) would calibrate trust in the model's ability to faithfully reflect input lighting.

---

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the reasons stated.

- **"Normal maps for MVLight appear blurrier than competitors (e.g., the owl figure). This is not discussed."** — Removed. This is an unverifiable qualitative observation about figures not accessible to the reviewer without the actual visual output. The paper's figures cannot be judged from text description alone.
- **"No statistical significance for any metric"** — Demoted to Nice-to-Have. Single-run evaluation is standard practice in this subfield (text-to-3D with SDS is computationally expensive). Not a weakness per se, but an improvement opportunity.
- **"Code is not cited in the main text"** — Removed per policy: appendix-stripped content (project webpage is mentioned in the paper).
- **"No evaluation of the diffusion model's ability to faithfully reflect input HDR"** — Demoted to Nice-to-Have. This would be a useful sanity check but is not central to the paper's core contribution about the full 3D generation pipeline.
- **"The paper needs major revisions" assertion in the critique's overall assessment** — Removed as a judgment call rather than a specific, grounded weakness. The assessment is incorporated into the evaluation above.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the strengths (novel architecture, multi-modal SDS, clear ablation for light-aware PBR) and converge on the primary weakness (lack of quantitative relighting metrics). The harsh critic's concern about the simplified-vs-full-PBR mismatch is a genuinely useful methodological observation that goes beyond what the paper discusses and could inform a productive direction for the authors to address.

---

## Suggestions

1. **Add quantitative relighting evaluation on held-out Objaverse objects.** Render 3D models under multiple unseen HDR environments; compare the pipeline's output to ground-truth renders using PSNR, SSIM, and LPIPS. Report albedo MSE against ground-truth albedo. This directly validates the central claim.
2. **Ablate the lighting conditioning variable.** Train a version of the model with the same architecture but where the light embedding is either constant or randomized (not corresponding to the input HDR). Compare against the full model on the same quantitative metrics to isolate the effect of lighting conditioning.
3. **Discuss the simplified-vs-full-PBR mismatch explicitly.** Either (a) clarify the rendering equation used for training data to show the mismatch is minimal, (b) justify that Stage 1's simplified model is sufficient because it is only used for coarse geometry and albedo, with fine-grained shading deferred to Stage 2, or (c) provide empirical evidence (e.g., visual examples) that the mismatch does not cause the artifacts it theoretically could.
4. **Include UniDream** in comparisons if its code/checkpoint is available, given its direct relevance.

---

## Score and Decision
MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>