## Summary
Forgedit is a single-image, text-guided editing method built on Stable Diffusion. It combines (i) a joint vision–language fine-tuning of UNet and a BLIP-generated source-prompt embedding, (ii) a vector-projection decomposition of the target text embedding into identity and edit components, and (iii) a "forgetting" mechanism at sampling time that resets fine-tuned UNet encoder or decoder blocks based on an observed encoder=structure / decoder=appearance property. The authors report new SOTA on TEdBench (CLIP 0.771, LPIPS 0.534, FID 7.071) vs. Imagic+Imagen, with 30 s fine-tuning on an A100.

## Strengths
- **14× fine-tuning speedup with a cleaner pipeline.** Joint optimization of the UNet (encoder 0–2, decoder 1–3) and the BLIP source-prompt embedding with separate learning rates collapses Imagic's two stages into one and converges in ~30 s vs. Imagic's 7 min (Sec. 3.2, Eq. 4). This is a useful, concrete practical gain.
- **Vector projection is a sensible mechanism.** Decomposing e_tgt into a component along e_src and an orthogonal e_edit, then summing with separate coefficients α and β (Eqs. for r, e_edit, e), gives two interpretable knobs for identity vs. edit strength. Fig. \ref{reasonablation} shows it complements vector subtraction (projection preserves identity; subtraction handles replacement).
- **BLIP-generated source prompt empirically reduces overfitting.** The comparison in Fig. \ref{blip}, with forgetting disabled to isolate the effect, supports the claim that using a captioning model rather than the target prompt as source prompt is a meaningful change from Imagic.

## Weaknesses

### Fatal
None — the method's qualitative contributions and speedup are concrete and at least partially supported.

### Major
- **Per-example human-in-the-loop hyperparameter selection invalidates the headline SOTA claim as stated.** Sec. 3.3 sweeps γ ∈ [0.8,1.6], α ∈ {0.8,1.1}, β ∈ [1.0,1.5]; Sec. 3.4/4.1 further has the user decide whether overfitting occurred and choose between encoderattn, decoderattn, or no forgetting; Sec. 3.5 describes the diamonds in the workflow as "user choices and preferences." Imagic+Imagen numbers in Table 1 are not produced this way. Combined with an LPIPS gap of only 0.003 (0.537 → 0.534) and no variance reported, the quantitative comparison is best-of-many vs. single-shot. The remark that "these user decisions can also be replaced by thresholds on metrics like CLIP score and LPIPS score" effectively concedes the metrics are being optimized at inference time. A fixed-protocol re-evaluation is needed before "new SOTA" can be claimed.
- **No same-backbone comparison.** The framing "Forgedit+SD 1.4 surpasses Imagic+Imagen" conflates method with backbone. Without Imagic+SD 1.4 (and ideally Forgedit on Imagen), one cannot attribute the gain to Forgedit. This is especially important given how small the LPIPS/FID gaps are.
- **The "general UNet property" (contribution #3) is asserted, not demonstrated.** It is supported only by a schematic (Fig. \ref{forget}) and cherry-picked qualitative ablations (Figs. \ref{forgetdecoder}, \ref{forgetencoder}). A claim phrased as a *general property of UNets in Diffusion Models* requires at least a quantitative probe across many images, and ideally across backbones — the paper provides neither. Since the forgetting mechanism depends entirely on this property, the third contribution is undersupported.

### Minor
- **Conceptual tension with σ = 0.** Sec. 3.4 states σ = 0 "works in general," i.e., entire fine-tuned encoder or decoder blocks are replaced with the pretrained weights. Sec. 3.2 motivated joint fine-tuning as necessary for identity preservation and semantic understanding. If half of the fine-tuned UNet can be discarded without losing identity, an ablation isolating what work the optimized e_src vs. UNet fine-tuning is doing (e.g., text-embedding-only optimization with no UNet update) would clarify the mechanism.
- **End-to-end editing wall-clock is not reported.** The 14× speedup measures the single fine-tuning pass, but the editing stage sweeps multiple γ/α/β values and forgetting strategies. Wall-clock per *successful* edit under the user-in-the-loop workflow is the relevant number for practitioners.
- **Vector projection geometry is ambiguous over tensor shape.** e_src and e_tgt are B×N×C, and the paper says "we conduct all vector operations on the C dimension," but does not show whether r is computed per-token or pooled across N. This affects exactly how the orthogonal decomposition is performed and is worth stating explicitly.
- **No success-rate metric for the user-in-the-loop workflow.** Given that the workflow expects users to detect overfitting and select forgetting strategy, a fixed-protocol success rate (or a small forced-choice human study) would substantiate the practical claims much more than the 0.003 LPIPS improvement does.
- **"Limitations" subsection (Sec. 3.5) contains no limitations,** only workflow text.

### Trivial
- The forgetting strategies "encoderattn" / "decoderattn" are defined in prose and via figure captions; a small table of which parameter groups are preserved vs. reset would help reproducibility.

## Nice-to-Haves
- Same-backbone same-prompt Imagic comparison on SD 1.4.
- A small human-evaluation forced-choice study on TEdBench under a fixed protocol.
- A quantitative probe (e.g., structural vs. appearance reconstruction error under encoder/decoder reset, aggregated across the benchmark) to substantiate the "general UNet property."
- Ablation isolating optimized e_src alone vs. e_src + UNet fine-tuning.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *Harsh critic: "SDXL is cited via the FID paper (HeuselRUNH17), which is almost certainly a citation error."* This is a citation-formatting / parser-level concern that the rules exclude.
- *Harsh critic's reproducibility ask for "Variance / seed reporting across at least 3 seeds per edit."* For TEdBench, single-run evaluation is the field norm; keeping this only as a nice-to-have rather than a weakness. (A weaker version remains under Major because the LPIPS gap is on the order of plausible noise — the substantive issue is the hyperparameter sweep, not the absence of seed averaging per se.)
- *Strength Finder: "New state-of-the-art on TEdBench."* In direct conflict with the verified Major weakness about asymmetric evaluation; weakness wins.
- *Strength Finder: "Forgetting strategy grounded in UNet encoder–decoder property."* Cannot be a strength when the underlying property is itself unsupported (see Major #3). Demoted.

## Novel Insights
None beyond the paper's own contributions. The decomposition of an edited embedding into identity-aligned and orthogonal components, and the encoder=structure/decoder=appearance heuristic for selectively resetting fine-tuned blocks, are the genuinely interesting observations, and both originate in the paper itself rather than in the reviews.

## Suggestions
- Re-run TEdBench under a fixed (γ, α, β, forgetting-strategy) protocol picked a priori or via a held-out tuning split, and also run Imagic on SD 1.4 as a same-backbone baseline. Without one or both of these, the SOTA claim should be removed or rephrased.
- Provide quantitative evidence for the UNet property: e.g., aggregate reconstruction-error metrics under encoder-only vs. decoder-only reset across all 100 TEdBench images, and ideally on a second backbone.
- Add a true Limitations subsection and a failure gallery with a success-rate number under a fixed protocol.
- Clarify whether vector projection is per-token or pooled over the N dimension and ablate.
- Run an ablation that fine-tunes only e_src (no UNet update) to clarify what the UNet fine-tuning contributes given that σ = 0 reset already "works in general."

---

**Axis-by-axis assessment.** *Originality:* moderate — the BLIP-source-prompt, orthogonal-embedding-decomposition, and selective-reset recipe is a coherent and reasonably fresh engineering combination. *Importance:* moderate — single-image text-guided editing is a well-trafficked problem. *Claims well supported:* partially — the speedup and the qualitative edits are credibly shown; the SOTA claim and the "general UNet property" are not, due to the hyperparameter-sweep evaluation, missing same-backbone baseline, and lack of any quantitative probe of the UNet property. *Soundness of experiments:* the central weakness — user-in-the-loop selection of γ/α/β and of forgetting strategy versus single-shot baselines, with no variance and a 0.003 LPIPS gap. *Clarity:* mostly clear but with notational ambiguities (per-token vs. pooled projection), a mis-titled Limitations section, and forgetting-strategy definitions buried in figure captions. *Value to community:* the practical recipe and the speed-up are useful; the empirical claims need tightening before others should rely on them.

## Score and Decision
The paper has real, useful contributions (fast joint fine-tuning, orthogonal embedding decomposition, a workable forgetting recipe) but the headline SOTA claim is undermined by per-example hyperparameter/strategy selection against single-shot baselines, no same-backbone comparison, and an undersupported "general UNet property." These are addressable in a substantial revision but not in a rebuttal.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>