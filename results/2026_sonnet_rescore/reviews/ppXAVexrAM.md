## Summary

ARSS proposes the first decoder-only, GPT-style causal autoregressive framework for novel view synthesis from a single image conditioned on a camera trajectory. The method combines a causal video tokenizer (VidTok/FSQ), a geometry-constrained camera autoencoder that maps Plücker raymaps to latent tokens, and a spatial-only token permutation strategy that preserves temporal causality while handling bi-directional spatial context. The system is trained from scratch on RealEstate10K and ACID, achieving competitive metrics—particularly best LPIPS and FVD—against stronger diffusion-based baselines including SEVA.

---

## Strengths

1. **Genuine novelty as first decoder-only AR model for camera-controlled NVS.** The paper claims ARSS is the first GPT-style causal transformer applied to novel view generation with explicit camera control. The framing is well-motivated and technically distinctive from all diffusion-based baselines compared.

2. **Best perceptual quality and temporal coherence across all three evaluated benchmarks.** Table 1 shows ARSS achieves the lowest LPIPS on Re10K (0.269 vs. SEVA's 0.349, a 21% improvement), ACID (0.265 vs. 0.326), and DL3DV (0.347 vs. 0.400 for next-best LVSM), and the lowest FVD on Re10K and DL3DV. These are consistent and non-trivial margins in perceptual and video-consistency quality.

3. **Hybrid token permutation ablation is principled and well-validated.** Table 2 shows that spatial-only random permutation (PSNR 19.22 dB) clearly outperforms both raster order (16.29 dB) and full spatial+temporal permutation (18.76 dB). The result cleanly validates the design decision to preserve temporal causality while randomizing spatial order. Figure 7 provides supporting qualitative evidence.

4. **Camera autoencoder with geometry-aware constraints is a sound design.** The pre-training loss (Eq. 5) enforces Plücker ray unit-length and orthogonality constraints, grounding the positional encoding in 3D geometry rather than purely learned features. This provides principled 3D positional guidance interleaved with visual tokens.

5. **Error accumulation analysis demonstrates slower long-horizon quality degradation.** Figure 6 shows ARSS's per-frame PSNR, SSIM, and LPIPS curves are flatter across 17 frames than all included baselines (LVSM, MotionCtrl, RayZer, ViewCrafter), consistent with the causal sequential generation hypothesis.

---

## Weaknesses

### Fatal
None.

### Major

- **SEVA is excluded from the error accumulation analysis (Figure 6) without justification, weakening the paper's central claim about causal sequential advantages.** SEVA is the only competitor close to ARSS in Table 1 (winning SSIM and FID on Re10K), yet it is absent from Figure 6. The paper excludes SEVA from DL3DV on legitimate grounds (training data overlap), but that reason does not apply to RealEstate10K, where Figure 6 is presumably evaluated. The claim from Section 4.2 that ARSS "maintains consistently highest or near-highest PSNR/SSIM" is far more compelling if demonstrated against SEVA. As presented, Figure 6 compares ARSS only against baselines it already beats decisively in Table 1, and the analysis that should be the paper's strongest argument for AR-specific long-horizon advantages is assembled to sidestep the most relevant comparison.

- **The tokenizer ablation (Table 3) confounds two independent variables, preventing clean isolation of the claimed contribution.** The comparison switches simultaneously from (a) an image-only VQ tokenizer to a causal video tokenizer, and (b) from VQ to FSQ quantization. FSQ is independently known to improve training stability relative to VQ codebook learning. The 62% FVD improvement (137.68 → 52.56) is attributed to temporal consistency from the video tokenizer architecture, but the VQ→FSQ change could independently account for a substantial fraction of this improvement. A VQ-based video tokenizer as an intermediate ablation condition would cleanly isolate the temporal architecture contribution.

### Minor

- **The quantitative framing is inconsistent with the actual results against SEVA.** The abstract states ARSS achieves "overall comparable to state-of-the-art view synthesis approaches," and Section 4.2 claims ARSS is superior (+1.1% PSNR, −21% LPIPS). However, Table 1 shows SEVA wins on SSIM (0.670 vs. 0.624, −6.6%) and FID (46.98 vs. 47.60, +1.3%) on Re10K. The mixed result is not dishonest, but the framing in the body text reads as if ARSS wins outright. A direct acknowledgment that results are mixed against SEVA would be more accurate and would not diminish the genuine contribution.

- **Ablation tables (Tables 2 and 3) do not specify which dataset the reported numbers correspond to.** Given that ARSS is trained on Re10K and ACID and tested on three datasets, it is unclear whether these are in-domain or full test set numbers. This makes direct comparison with Table 1 entries difficult.

- **The paper does not test the most distinctive claimed advantage of AR models — adaptability when the trajectory changes.** The introduction states that diffusion-based methods make it "less straightforward to incrementally extend and reuse existing generations when the trajectory changes" and that AR models operate "in a sequential and causal manner." Figure 6 provides indirect evidence of sequential quality, but no experiment shows trajectory extension beyond training horizon, variable-length trajectory handling, or online trajectory adaptation. This is not required for the paper's core NVS claim, but the gap between the framing and the experiments is noticeable.

### Trivial

- **Notation inconsistency in Eq. 5 description.** The accompanying text reads "where **d** is the normalized camera ray direction, **d** is the momentum term," using the same variable name for two quantities. The equation itself correctly uses distinct hat-variables. The text likely intends **m** for the momentum term.

- **Equation 7 appears to be missing the target sequence argument of the cross-entropy loss** (likely a parser formatting artifact; Eq. 3 in the same section provides the complete formulation).

---

## Nice-to-Haves

- Including inference time and relative compute cost versus SEVA would let readers calibrate the resource-normalized significance of ARSS's competitive performance, given that the paper trains from scratch at 256×256 versus SEVA's pretrained, higher-resolution regime.
- A brief analysis or discussion of how much of the SSIM/FID gap relative to SEVA is attributable to the resolution difference (256×256 vs. higher) rather than method design would sharpen the interpretation of Table 1.
- At least one experiment specifically exploiting the causal AR property — e.g., extending a 17-frame trajectory to 34 frames by conditioning on previously generated frames, or evaluating on variable-length trajectories — would substantiate the motivation more directly and make for a compelling additional result.

---

## Removed Points

*These points are flagged for removal — treat them with caution.*

- **Harsh critic's "structural coherence failure" for the missing trajectory-change experiment.** The critic frames this as a fatal problem, but the paper does provide partial evidence via Figure 6. The gap between motivation and experiment is real, but "Fatal" is too strong; demoted to Minor / Nice-to-Have.

- **Harsh critic's concern about unfair resource/training comparison.** The paper itself acknowledges the resource gap in Section 5 ("our method is trained from scratch using limited public datasets with relatively low resolution"), and the results are presented in a way that makes this context available to the reader. Demanding an explicit compute comparison table exceeds field-standard practice for a systems paper of this type.

- **Harsh critic's request for training and inference timing.** Per filtering rules, this is a reproducibility nitpick for an empirical systems paper.

- **Harsh critic's assertion about the abstract "overstating" the result.** The abstract uses "comparable," not "superior," which is defensible given ARSS's LPIPS/PSNR/FVD wins against SEVA. The body text framing is more problematic (retained as Minor above), but the abstract claim itself is within acceptable bounds.

- **Strength Finder's claim that Figure 6 "demonstrates that the strictly causal generation structure leads to reduced error accumulation."** This claim is too strong: the causal structure is one potential explanation, but the video tokenizer, training data, and architectural differences also plausibly contribute. Retained as a supporting strength but weakened to reflect this ambiguity.

---

## Novel Insights

The most genuinely novel observation to emerge from the synthesis is the design tension between spatial bi-directionality and temporal causality in multi-view generation — a tension that does not arise in single-image AR generation. ARSS's hybrid permutation strategy (spatially random, temporally ordered) is a principled solution to this tension and is cleanly supported by the ablation. This insight generalizes beyond NVS: any AR generative task over sequences of 2D spatial data faces the same bi-directional/causal conflict, and the hybrid ordering principle may apply broadly (e.g., video prediction, embodied navigation). The camera token interleaving — where each visual token is paired with its 3D positional instruction from the camera autoencoder rather than relying on a global condition — is also a clean design pattern for geometry-aware AR generation that could be adopted in other settings.

---

## Suggestions

1. Include SEVA in Figure 6 on the Re10K split. If ARSS degrades more slowly than SEVA, this is a compelling and honest demonstration of the sequential AR advantage; if degradation is similar, that is still informative and does not undermine the rest of the paper.
2. Add a VQ-based video tokenizer condition to Table 3 to isolate the temporal architecture contribution from the VQ→FSQ quantization change.
3. Specify the dataset source for Tables 2 and 3 ablation numbers.
4. Correct the notation in the Eq. 5 description (replace second **d** with **m**) and complete Eq. 7 to include the CE target sequence.
5. Revise the language in Section 4.2 to accurately reflect the mixed result vs. SEVA: ARSS wins on PSNR, LPIPS, and FVD; SEVA wins on SSIM and FID.

---

**Axis Assessment:**
- *Originality:* High — first AR NVS framework; hybrid permutation is novel and principled.
- *Importance of research question:* Medium-high — AR for world modeling is a live research direction; NVS is an important sub-problem.
- *Claims supported:* Medium — core NVS quality claims are supported; the sequential/causal advantage claim is partially but not fully demonstrated.
- *Soundness of experiments:* Medium — main table is broadly sound; error accumulation analysis has a notable gap (SEVA absent); tokenizer ablation conflates two variables.
- *Clarity of writing:* Medium — method section is clear; results section overclaims; ablations are under-specified.
- *Value to research community:* Medium-high — establishes AR as a viable NVS paradigm with a usable design pattern; competitive results under constrained training.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>