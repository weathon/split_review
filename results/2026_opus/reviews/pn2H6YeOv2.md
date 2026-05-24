Now I have a solid understanding of the paper. Let me do the calibration searches.Round-1 bracket: The paper sits between 4.5 and 7.0. It's more methodologically sophisticated than the rejected anchors (e.g., LVLM-CL at 2.5, MCIL at 2.33) and closer to the C-CLIP / PROOF / Vision-Language Synergy band. Let me narrow.## Summary
The paper introduces Pi-CCA, a replay-free continual learning method for vision-language models that summarizes pre-continual image-text alignment via a compact certificate consisting of the top-k canonical correlations and sketched canonical subspaces, and regularizes LoRA updates to preserve these invariants while averaging over prompt perturbations. Across MTIL, X-TAIL, VLCL, and ConStruct-VL, Pi-CCA reports state-of-the-art results among replay-free methods, with ablations targeting both spectral and subspace terms and a prompt-invariance loss.

## Strengths
- **Novel canonical-correlation regularizer for VL-CL.** Pi-CCA targets the *whitened* cross-covariance spectrum and subspaces directly, rather than proxy quantities like contrastive off-diagonals or distilled logits (Eqs. 2–11). Removing the spectral term (λ₁=0) drops MTIL Avg by 2.5 pp and the subspace term (λ₂=0) by 2.2 pp (Table 3), so the geometry-targeted terms are doing real work in the ablations.
- **Breadth of empirical evaluation.** SOTA among replay-free methods across four heterogeneous benchmarks (classification: MTIL/X-TAIL; retrieval: VLCL; structured-VL: ConStruct-VL), and surpasses one synthetic-replay method (GIFT) on VLCL retrieval (Tables 1–2).
- **Constant-memory certificate with explicit Pareto study.** The sketching scheme stores only h×k matrices, independent of feature dimension (Eq. 4). Fig. 2 sweeps (k,h) over a wide grid and identifies a broad Pareto ridge around (64, 256), supporting the "small yet sufficient" claim.
- **Task-order robustness.** Twenty independently shuffled MTIL orders (Fig. 5) show narrow IQRs in Avg/Last/AF, providing more order-robustness evidence than most VL-CL papers report.
- **Prompt-invariance is operationalized and stress-tested.** Eq. 11 aligns the *mean* sketched text projector across perturbations and contracts dispersion; Fig. 4 shows the invariance loss flattens decay slopes (+2.44 / +2.51 pp R@1 at s=1.0, ID/OOD) and lowers AF.

## Weaknesses

### Fatal
None.

### Major
- **The "pre-continual" certificate is EMA-refreshed from the current model.** §3.2 frames ρ*, U*, V* as the *reference, pre-continual* CCA quantities, but Eq. 13 explicitly updates ρ*, S_v*, S̄_t* each step from sketches of the *current* model with rate α. Once α>0, the certificate is a low-pass-filtered version of the model's own trajectory, not the invariant the prose advertises. Worse, Table 3 shows that turning the EMA off (α=0, i.e., literally anchoring on the original geometry) *degrades* MTIL Avg (76.8→75.6) — so the geometry-preservation framing is in tension with its own ablation. The method may still be useful, but the explanatory story ("retention works because Pi-CCA pins a pre-continual invariant") is not what the implementation does.
- **Fig. 3 reports Pearson 0.99–1.00 and Spearman = 1.00 in all four panels.** Across realistic sweeps over LoRA capacity, LR, sketch type, EMAs, invariance strength, etc., obtaining ρ = 1.00 in four independent panels is implausible. The most plausible reading is that the geometry drifts and the performance deltas are computed from the same checkpoints, making the correlation largely a self-consistency check rather than independent mechanistic evidence. The paper itself flags this as its key piece of evidence linking "alignment-geometry stability" to retention, so the implausibility weakens a central claim.
- **Initial-certificate construction is under-specified.** §3.2 says the global certificate is "constructed from a diverse anchor prompt set," but the whitened cross-covariance Σ_vt (Eq. 1) requires *paired* (image, text) embeddings — prompts alone are insufficient. The paper never specifies what images are paired with anchor prompts, how many pairs are used, or whether those images are seen at any point during the stream. Since the paper's own taxonomy criticizes prior work for relying on "reference corpora" (§2), the boundary that defines "replay-free" for Pi-CCA itself needs to be made precise.
- **Inconsistent variance reporting on the headline tables.** Table 1 (MTIL, X-TAIL) is reported as single numbers without SDs or seed counts, while Table 2 reports mean ± SD with values around 1–1.5 pp. The Pi-CCA→C-CLIP gap on MTIL Avg is 76.8→75.2 (1.6 pp) — well within the SD ranges reported elsewhere in the paper. Without seed counts and variance on the *largest* tracks, the SOTA claim is not statistically supported.

### Minor
- **Subspace surrogate is acknowledged but not bounded.** §3.3(ii) admits the sketched Gram operators Q̂_v, Q̂_t are *not* projectors of the original-space subspaces and uses ‖Q̂−Q*‖²_F as "a surrogate that preserves order/angles under near-isometric sketches." With d_v,d_t≈512–768 and h=256, JL/SRHT distortion is not vanishingly small; a small experiment verifying that ‖Q̂_v − Q*_v‖_F is monotone in ∑sin²θ_i on representative pairs would convert a heuristic into a justified design choice.
- **Spectral clipping non-differentiability is left unstated.** §3.3(ii) applies eigenvalue clipping to [0,1] and re-symmetrization after forming each Q, which can be non-differentiable at clipped eigenvalues. Whether stop-gradient is used at the clip points (vs. a relaxed surrogate) is not stated, and the choice between Newton–Schulz and eigendecomposition for Σ^(−1/2) (§3.4) is offered as "either … or …" without disclosing which produced the reported numbers.
- **Asymmetric prompt-invariance with no image-side counterpart.** The certificate averages projectors over text-side perturbations only. The paper frames prompt invariance as central, but provides no parallel mechanism for image-side augmentation invariance; given image-side augmentations are standard in VLM training, the asymmetry deserves justification.
- **Ky-Fan-k sum term overlaps with sorted L2 term.** In Eq. 8, the Ky-Fan-k sum is determined by the sorted spectrum, so its contribution beyond the sorted L2 term is mostly aggregate. The ablation (no spectral moments J=0 → 76.1, Hungarian pairing → 76.7) supports that these enrichments add at most ~0.7 pp; presenting them as principled invariances slightly oversells.

### Trivial
- None retained.

## Nice-to-Haves
- Add a *certificate-frozen* ablation (literally freeze ρ*, S_v*, S̄_t* at t=0) and a *refresh-only-at-task-boundaries* variant, and show curves of certificate-to-current drift over the stream. This is the highest-leverage experiment to defend the geometry-preservation thesis.
- Replace Fig. 3's in-trajectory scatter with a *predictive* setup: compute geometry drift *ex ante* on a held-out perturbation set and predict the subsequent performance drop. Even Pearson 0.7 there would be more informative than 1.00 in the current setting.
- Report SDs and seed counts on Table 1 (MTIL, X-TAIL) to match Table 2's variance reporting, given gaps to baselines are comparable to the SDs elsewhere.
- Add the best baseline (e.g., C-CLIP or RAIL) under the same 20 task orders in Fig. 5 to show order-robustness is a Pi-CCA property, not an MTIL property.

## Removed Points
These points are flagged to be removed; treat them with caution.
- "Time-continual study on TiC-YFCC/RedCaps announced but absent from the main text." — The paper says it is *additionally reported*; relegating it to the appendix is a reasonable presentation choice for a paper already covering four tracks.
- "Mod-X is dismissed but L_sub on Q̂ is operationally similar to a whitened, top-k variant of the same idea." — This is rhetorical positioning, not a concrete error; whitened, top-k canonical alignment is meaningfully different from contrastive off-diagonal matching.
- "Eq. 12 has an OCR artifact with Σ_v appearing twice." — Per instructions, formatting/parsing artifacts are not author errors.
- (Strength dropped) "Pearson/Spearman of 1.00 across 20+ configurations supports a causal link" (Strength Finder #3 supporting strengths) — This is the same Fig. 3 the harsh critic flags as a self-consistency artifact. The weakness wins.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a useful diagnostic tension — that "preservation" methods often end up tracking moving targets when implemented with EMAs — but this is a well-known concern in the broader stability/plasticity literature rather than a novel observation. The most interesting *new* lens the reviews offer is that the α=0 ablation, when read against the geometry-preservation framing, suggests the gain may come from a slow regularizer that smooths trajectory rather than from preserving a fixed alignment skeleton; the authors could either lean into that or counter it with a frozen-certificate experiment.

## Suggestions
- Run a literal-anchor experiment: freeze (ρ*, S_v*, S̄_t*) at the start of the stream and report accuracy curves; if Pi-CCA still wins, the geometry thesis is supported. If not, retitle the contribution as "a slow EMA regularizer over the canonical spectrum/subspace."
- Convert Fig. 3 into a predictive experiment with a clear train/test split between configurations used to fit the relationship and configurations used to evaluate it. Report the correlation drop and treat the residual as the true mechanistic signal.
- Specify the anchor set (number and source of image–prompt pairs) and add a sensitivity sweep over anchor-set size; if the method works with O(100) unlabeled images, make that claim explicit.
- Add SDs over ≥3 seeds for MTIL/X-TAIL in Table 1 to match the reporting standard of Table 2.
- Add an image-side counterpart to L_pi (or explicitly justify the text-only asymmetry).

---

## Calibration Trace

**Round 1 anchors (bracketing):**
- `JIlIYIHMuv.md` (avg 2.50, Reject) — LVLM-CL continual learning; clearly weaker than Pi-CCA in scope and rigor.
- `gNoqEdT2wO.md` (avg 2.33, Reject) — MCIL benchmark; weaker.
- `WM5G2NWSYC.md` (avg 2.00, Reject) — Projected Subnetworks; weaker.
- `A1JdcLawSu.md` (avg 3.00, Reject) — Hyperspherical replay; weaker.
- `G9Ea7mlqGO.md` (avg 3.80, Reject) — CLIP online continual learner; weaker but topically similar.
- `sb7qHFYwBc.md` (avg 6.50, Accept) — **C-CLIP**, the direct competitor Pi-CCA beats; Pi-CCA has more benchmarks but weaker mechanistic-evidence chain.
- `9aZ2ixiYGd.md` (avg 5.00, Accept) — Vision-language synergy, rehearsal-free.
- `k9NYnsC4Mq.md` (avg 5.67, Reject) — PROOF for VLM-CIL; similar scope, similar weaknesses around evidence.
- `gc8QAQfXv6.md` (avg 9.00, Accept) — Function vectors / CF in instruction tuning; significantly stronger.
- `WyEdX2R4er.md`, `1aF2D2CPHi.md`, `3i13Gev2hV.md` (avg 8.00, Accept) — Different topics, stronger.

Initial bracket: **4.5–7.0** (Pi-CCA clearly above the 2–3 cluster, below the 8–9 strong-VLM cluster, sitting near C-CLIP / PROOF / Proxy-FDA).

**Round 2 anchors (narrowing 4.5–6.5 / 5.5–7.5):**
- `Hcb2cgPbMg.md` (avg 6.25, Accept) — **Spectral Regularization for CL**; conceptually parallel (regularize singular values), accepted on cleaner motivation though less ambitious. Pi-CCA is broader in scope but weaker on mechanistic evidence; roughly comparable.
- `1TXDtnDIsV.md` (avg 4.67, Reject) — MambaCL; weaker.
- `7sASqAmGaO.md` (avg 5.33, Reject) — AugNeg; comparable middle-band.
- `u3dHl287oB.md` (avg 5.67, Accept) — Joint task similarity / overparam; comparable.
- `SIZWiya7FE.md` (avg 6.00, Accept) — Label-agnostic forgetting; comparable.
- `pUOesbrlw4.md` (avg 5.25, Reject) — Deep unlearning; weaker comparison.
- `eIFHoPsIkw.md` (avg 5.75, Reject) — **Proxy-FDA**; closest analog — feature-distribution preservation for foundation-model fine-tuning with SOTA results but reviewer complaints about justification/ablation, leading to Reject.
- `ScI7IlKGdI.md` (avg 6.33, Accept) — Spurious forgetting in LLMs; comparable.
- `V6uxd8MEqw.md` (avg 6.50, Accept) — Prompt-based replay-independent GCL.
- `pB9XVRGVu0.md` (avg 5.75, Reject) — GeRA geometric regularization for alignment; comparable.

**Final placement.** Pi-CCA's empirical breadth and SOTA-across-4-tracks are slightly stronger than Proxy-FDA's case, but the verifiable evidential issues (self-referential certificate framing vs. Eq. 13, Fig. 3 correlation = 1.00, missing SDs on Table 1, under-specified anchor data) collectively pull the paper down. It sits closer to Proxy-FDA (5.75, Reject) and PROOF (5.67, Reject) than to C-CLIP (6.5, Accept) or Spectral Regularization (6.25, Accept), because in the latter two, the central evidence holds up. Score lands at **5.0** — slightly below the borderline-accept band; the contribution is real but the mechanistic narrative is not yet supported by the evidence offered.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>