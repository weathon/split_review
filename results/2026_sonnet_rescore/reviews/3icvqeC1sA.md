## Summary

ChaosNexus is a foundation model for universal chaotic system forecasting built on the ScaleFormer, a U-Net-inspired hierarchical Transformer architecture that applies patch merging/expansion at multiple temporal resolutions. It couples Mixture-of-Experts (MoE) layers with a wavelet scattering–derived frequency fingerprint, and is pretrained on ~20,000 synthetic ODE systems. The paper evaluates zero-shot generalization on ~9,300 held-out synthetic chaotic systems and on 5-day global weather forecasting using WEATHER-5K.

---

## Strengths

- **Multi-scale U-Net backbone with architectural novelty**: The ScaleFormer's progressive patch merging (halving temporal resolution, doubling feature dimension at each level) with symmetric decoder and skip connections is a concrete and well-specified architectural innovation over the flat single-resolution Transformer used by Panda and the RNN mixture used by DynaMix. Equations (1)–(6) specify each component clearly.

- **Real, statistically significant sMAPE improvement**: Figure 2 shows ChaosNexus achieves sMAPE@128 ≈ 69 vs. Panda ≈ 75 — a gap the paper tests with Wilcoxon signed-rank tests and marks as statistically significant (p < 0.01). This point-wise improvement over the closest prior chaotic foundation model is the clearest and best-supported result.

- **Wavelet scattering frequency fingerprint**: Conditioning the forecast head on wavelet scattering coefficients (Equation 7) is a distinct departure from Panda's linear embeddings and DynaMix's sinusoidal embeddings. It provides a theoretically motivated, deformation-stable spectral signature at inference time with no additional training overhead.

- **Scaling analysis (diversity > volume)**: Figure 4(b,c) clearly shows that increasing per-system trajectory count brings negligible zero-shot sMAPE gain, while increasing corpus diversity systematically improves generalization across all prediction horizons. This replicated and extended prior observations from Panda in a controlled manner, providing a concrete design principle for future work.

- **Dual axial attention for variable coupling**: Variable attention (Section 3.2, Equation 1) explicitly models inter-variable coupling at O(V²) complexity, which is relevant for coupled chaotic ODEs where joint state-space geometry matters.

---

## Weaknesses

### Fatal
None.

### Major

- **Weather experiment structural weakness: pretraining vs. no pretraining, not ChaosNexus vs. Panda**. Figure 3's central comparison pits ChaosNexus (zero-shot, pretrained on chaotic ODE corpus) against FEDFormer, CrossFormer, PatchTST, Koopa, and vanilla Transformer trained from scratch on 85K–473K samples — a regime where such models cannot meaningfully fit the weather distribution. The paper itself acknowledges in Section 4.2 that "ChaosNexus, Panda, and Chronos-S-SFT perform significantly better than those trained on general time series" (with Panda and Chronos-S-SFT results deferred to Table 9 in the appendix). The main-text Figure 3 does not show Panda's weather performance. Since the comparison in Figure 3 only establishes that pretraining on chaotic systems helps — not that ChaosNexus specifically outperforms other chaotic-domain foundation models — the headline result ("zero-shot MAE strictly below 1°C") cannot be attributed to ChaosNexus's specific architectural contributions without an explicit Panda vs. ChaosNexus comparison under the same weather protocol in the main text.

- **Attractor fidelity evidence misaligns with the paper's core framing**. The introduction explicitly motivates the multi-scale design as necessary for preserving "system-specific attractor geometries" and states that single-resolution models "degrad[e] long-horizon stability." The paper selects D_frac, D_step, D_lyap, and ME_LRW precisely to measure this. Yet Figure 2 — the paper's primary empirical figure for this claim — shows ChaosNexus D_step ≈ 1.2 and Panda D_step ≈ 1.2 (virtually identical, per the figure description), and an inset mean D_frac for ChaosNexus ≈ 0.225 vs. Panda ≈ 0.200, where lower is better (ChaosNexus is potentially *worse* on mean D_frac). The paper does claim improvement on D_lyap and ME_LRW in Table 2 (appendix), but the metrics most prominently shown in Figure 2 do not support the framing. The clear actual improvement — sMAPE (69 vs. 75) — is on the point-wise metric that the paper simultaneously argues is "ultimately unreliable" for chaotic forecasting. This inversion between the stated primary criterion and what is actually better is a coherence gap running through the paper.

- **No contextualization for the weather MAE claim**. The paper presents "zero-shot mean error strictly below 1°C" for 5-day global temperature as a headline result. However, there is no persistence baseline, climatological mean, NWP reference, or established ML weather model (FourCastNet, GraphCast, Pangu-Weather etc.) to situate this number. Temperature MAE varies enormously by location, season, forecast horizon, and normalization convention. Without at least one anchor, the claim "competitive zero-shot mean error below 1°C" is scientifically uninterpretable: it is impossible for the reader to assess whether this is impressive, mediocre, or trivially achievable at the evaluated horizons.

### Minor

- **Notation ambiguity in Equation (5)**: The patch merging equation uses H_enc^(i) on both the left-hand side and the right-hand side (as input to the concatenation). The surrounding text clarifies the intended semantics (input to level i is output of level i−1, etc.), but the equation in isolation is ambiguous about whether the LHS represents the pre-merge or post-merge tensor.

- **Attention visualization uses three cherry-picked systems without cross-validation**. Section 4.4 interprets attention maps for three hand-selected systems (CircadianRhythm-GuckenheimerHolmes, Lorenz84-OscillatingFlow, BickleyJet-HindmarchRose) and makes interpretive claims ("anticipating future dynamics," "model concentrates on specific temporal segments"). These are plausible but not cross-validated on held-out systems or quantified. The analysis is presented as interpretive evidence for architecture design rather than as a formal ablation.

### Trivial

- The repeated "REVISE" / "ADD" markers in the paper text are leftover editorial placeholders; Section 4.2 in particular contains an "ADD" marker mid-results, suggesting the camera-ready still requires cleanup.

---

## Nice-to-Haves

- **Direct zero-shot and few-shot Panda vs. ChaosNexus comparison on WEATHER-5K in the main text**: Table 9 (appendix) reportedly contains this; promoting it to Figure 3 or adding it as a panel would directly address the major weather experiment concern.
- **A persistence baseline and at least one NWP reference line on Figure 3**: Even a single reference (e.g., ERA5 forecast or 24h persistence) would allow readers to calibrate whether sub-1°C is strong or expected at 24h horizons.
- **Ablation summary table in the main text**: Since MoE, U-Net hierarchy, and wavelet fingerprint are each claimed as essential contributions, a brief result table showing ablations of each in the main text (vs. deferred entirely to appendix) would substantially strengthen the contribution claim.
- **Stratified analysis of D_step / D_lyap by system frequency band**: If the multi-scale architecture is hypothesized to help systems with widely separated frequency content, showing that the improvement is concentrated in high-bandwidth systems would directly validate the core motivation with evidence.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Calling the scaling insight a 'guiding principle' is inflated"** — Removed as a scope-creep criticism. The paper explicitly acknowledges that the system-diversity scaling law was previously established by Panda and Lai et al. (2025), and correctly frames Figure 4(b) as a complementary refinement. Labeling a confirmed and extended result a "guiding principle" is routine academic framing and not a factual overclaim.

- **Strength Finder: "MoE layers contribute to consistently lower variance compared to Panda (Figure 2 inset)"** — Removed as delusional/unsupported. The figure description does not indicate that ChaosNexus has meaningfully lower variance than Panda; variance comparison from inset plots is not explicitly stated in the paper text.

- **Strength Finder: "Strong zero-shot accuracy on 5-day global weather forecasting"** — Partially retained only as far as the raw result is real; removed the blanket framing of it as a strong standalone strength given the structural weakness of the comparison (no Panda baseline in Figure 3, no contextualization).

- **Strength Finder: "Dual axial attention improves attractor statistics (low D_step)"** — Removed. The paper provides no ablation isolating the contribution of dual axial attention to D_step, and D_step is indistinguishable from Panda's anyway.

---

## Novel Insights

The observation from Section 4.4 that shallow encoder layers develop Toeplitz-like attention patterns for highly regular chaotic systems — suggesting the network learns to apply fixed convolutional-style filters for periodic dynamics — while deep encoder layers generalize to global dependency synthesis is a genuinely interesting mechanistic finding. If validated beyond the three illustrated systems, this would provide interpretive evidence that the multi-scale hierarchy partitions regularity-processing across depth in a principled way, potentially informing architectural choices for other PDE and dynamical-system foundation models.

---

## Suggestions

1. **Promote the Panda weather comparison from Table 9 (appendix) to Figure 3 (main text)** — with both zero-shot and identical fine-tuning budgets. This is the single most important fix for the paper's credibility.
2. **Add a persistence or climatological baseline to Figure 3** to contextualize the 1°C MAE claim.
3. **Reconcile the attractor fidelity claims with the main-text evidence**: Either show D_lyap and ME_LRW improvements directly in Figure 2, or revise the framing to acknowledge that the primary demonstrated improvement is in sMAPE and ground the multi-scale motivation accordingly.
4. **Fix Equation (5) notation** by renaming the LHS tensor (e.g., H_enc^(i+1)) to eliminate the self-referential ambiguity.
5. **Include a one-sentence ablation summary** (e.g., "removing each of U-Net, MoE, and wavelet fingerprint individually increases sMAPE@128 by X, Y, Z, per Table A.X") in the main text.

---

**Evaluation on key axes:**

- **Originality**: Moderate. The ScaleFormer combines known components (U-Net, MoE, wavelet scattering) in a new configuration for chaotic forecasting. No single component is novel in isolation, but the combination and application are genuinely new.
- **Importance of research question**: High. Zero-shot forecasting of diverse chaotic systems has clear scientific value, and data efficiency on real-world chaotic systems (weather) is practically important.
- **Claims supported by experiments**: Low-to-moderate. sMAPE improvement is clearly supported; attractor fidelity improvement (D_step in particular) is not evident from the main text; weather superiority is confounded by baseline asymmetry.
- **Soundness of experiments**: Moderate. Benchmark and metrics are appropriate, Wilcoxon tests are used correctly, but the weather experiment design is structurally problematic and key ablations are appendix-only.
- **Clarity of writing**: Moderate. Generally well-structured, but the framing-evidence gap creates confusion, and leftover editorial markers suggest incomplete revision.
- **Value to research community**: Moderate. The scaling analysis and architecture are worth knowing about; the sample-efficiency result for weather, if properly contextualized, could be compelling.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>