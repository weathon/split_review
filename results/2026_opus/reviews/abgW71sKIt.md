## Summary

This paper studies 1-bit post-training quantization (PTQ) for LLMs and argues that naive layer-wise output matching (as in ARB-X) fails in three identifiable ways: it does not guarantee block-level loss reduction, it diverges from the true full-precision target as quantization errors accumulate, and it can distort token-similarity structure relevant to attention. The proposed method (i) replaces the activation-conditioned error with a true output error that conditions on full-precision X, (ii) introduces an "Attention Matrix Preservation" (AMP) masking mechanism, and (iii) applies output matching only to the last FC layer of each block while using ARB-RC for the rest, yielding consistent perplexity improvements across OPT (1.3B–30B), LLaMA-2 (7B/13B), and LLaMA-3-8B.

## Strengths
- **Empirical gains over the strongest prior baseline (ARB-RC) on most settings.** Table 1 shows OPT-1.3B C4 PPL drops from 27.70 → 24.69 and WikiText2 from 26.40 → 24.30; LLaMA-2-7B C4 drops 20.4 → 19.25 and WikiText2 16.25 → 15.42 (Table 2). The gains are largest where 1-bit PTQ is hardest (small OPT models and LLaMA).
- **The preliminary analysis (Section 3) surfaces a non-obvious negative result and motivates the design.** Figure 1 documents that layer-wise output matching can yield *higher* block-level loss than weight matching at multiple layers — a real, useful observation about the limits of ARB-X. Figure 2 supports the "error accumulation" claim quantitatively across 32 blocks.
- **AMP is grounded in a concrete architectural observation.** The ablation in Table 3 shows removing AMP doubles LLaMA-2-7B C4 PPL (19.25 → 29.12) but barely changes OPT-6.7B (16.22 → 16.35); Section 5.3 ties this asymmetry to RMSNorm vs LayerNorm. This is a substantive, evidence-backed claim, not generic ablation table padding.
- **Closed-form updates make the modified objective tractable.** Eqs. 5–8 give analytic optima for α_c, B, α_r (the latter via `torch.linalg.lstsq`), so the new objective does not impose a heavy iterative cost.

## Weaknesses

### Fatal
None. The technical concerns below are real but localized; the empirical kernel still stands.

### Major
- **The PTB-on-LLaMA-2-7B result is a real failure that is dismissed rather than diagnosed.** In Table 2, the proposed method posts PTB PPL = 3166 on LLaMA-2-7B vs. 763 (ARB-RC), 681 (ARB-X), 657 (PB-LLM) — roughly 4–5× worse than every baseline. The paper writes "the large perplexity indicates that the metric cannot provide a meaningful evaluation," but the same column reports 657/681/763 as if meaningful. If PTB on LLaMA-2-7B is degenerate, the entire cell should be marked as such for all methods; otherwise this is a setting where the method catastrophically underperforms, and the paper offers no hypothesis (AMP-induced? objective-induced?) or diagnostic ablation. This directly contradicts the "consistently outperforms" framing.
- **The selective-layer scheme — one of three claimed contributions — is asserted, not ablated.** Section 4.2 picks "the last fully connected layer of each block" because it "has the most direct impact on the block loss." Figure 1 shows that ARB-X helps on some layers and hurts on others, but never breaks the comparison down by intra-block layer position. The obvious ablation — output matching on first FC only / last FC only / all layers / a learned selection — is absent, and the existing ablations (Tables 3, 4) hold the selective scheme fixed. Since this design choice is what protects most of the network from the failure modes identified in Section 3, leaving it unsupported is a methodological gap.
- **The AMP derivation contains an ambiguous/incorrect equality that the paper never resolves.** Eq. 9 writes
  ‖(X̂Ŵ Ŵᵀ X̂ᵀ) ⊙ (XWWᵀXᵀ)‖ = Tr[X̂Ŵ Ŵᵀ X̂ᵀ · XWWᵀXᵀ] = Tr[ŴᵀMŴ].
  The middle equality only holds if "‖A ⊙ B‖" is interpreted as the sum of entries of A ⊙ B (= Frobenius inner product ⟨A,B⟩, which equals Tr[AB] for symmetric A, B). Under the standard reading "‖·‖ = Frobenius norm," ‖A ⊙ B‖²_F = Σᵢⱼ A²ᵢⱼ B²ᵢⱼ ≠ Tr[AB]. The objective Tr[ŴᵀMŴ] is reasonable on its own as a cosine-style alignment of token-similarity matrices, but the paper presents it as if it were derived from a Hadamard norm and never declares which object is actually being optimized. The trace-form objective should be motivated directly.
- **The AMP update rule (Eq. 11) is incoherent given the mask definition (Eq. 10).** The masks Mʳ, Mᶜ, Mᴮ are defined as sign(·) of a gradient, so entries are in {−1, 0, +1}. The update in Eq. 11 has the form α ← α·(1 − M) + α*·M, which is a convex combination only if M ∈ {0,1}. With M = −1 the rule becomes α ← 2α − α*, which is reflection, not the "convex selection" the surrounding prose describes ("once we obtain the AMP mask… we update them with…"). Either the masks should be {0,1} indicators on positive gradient sign or the update is wrong. Whichever resolution is intended, the implementation in Table 3 measures whatever the code does, not what the paper specifies; the most novel component is under-specified.
- **The framing/labelling versus what the method does is inconsistent.** Tables 1–2 categorize the proposed method as "OA" (output alignment), but Section 4.2 makes clear that only the last FC layer per block uses the modified output-error objective and AMP — the remaining layers use ARB-RC, the exact weight-matching the paper argues against. A more honest label is "hybrid (WA + selective OA)," and the ablations should disentangle how much of the gain over ARB-RC comes from (a) the modified objective on one layer per block, (b) AMP, and (c) the ARB-RC substrate. Table 4 only varies the activation-conditioned vs output error at the selected layer; the selectivity itself is not toggled.

### Minor
- **Improvements shrink on larger / more modern models with no variance reported.** OPT-13B C4 gain over ARB-RC is 0.36 PPL (15.07 → 14.71); OPT-30B is 0.19 (13.34 → 13.15); LLaMA-3-8B is 0.9 (36.04 → 35.14). No multi-seed numbers, calibration-set variance, or significance tests are reported. At the scale most relevant for deployment, the headline "consistently outperforms" rests on differences within plausible calibration-noise range.
- **Section 3.2 conflates ARB-X's objective with an observed side effect.** The text states that "ARB-X maximizes the cosine similarity between the layer outputs before and after the quantization." ARB-X minimizes a Frobenius MSE; the cosine similarity behavior is an empirical byproduct, as the paper actually shows in Figure 2. As written, this confuses the optimization target with a side observation.
- **Eq. 6 contains the undefined notation "N_{F,BK}".** The symbol appears once, with no definition; from context it looks like the product N_F · B · K, but it should be spelled out since this expression defines the closed-form update for B, a central optimization variable.
- **Table 3 / Table 4 do not include PTB.** Given the PTB failure on LLaMA-2-7B, running the AMP ablation and the objective ablation on PTB would either localize the failure or rule out one of the components, and is a small, well-targeted experiment that would address the most consequential remaining doubt.

### Trivial
None retained (see Removed Points).

## Nice-to-Haves
- A small layer-position grid (output matching on layer 0 / layer 1 / … / last only / all layers) on a single block, reporting block loss, would directly test the "last FC has the most direct impact" claim.
- Multi-seed / multi-calibration-subset error bars on at least the OPT-13B/30B and LLaMA-3-8B numbers, where the gains are sub-PPL.
- Move the overhead measurement out of the appendix into the main text — the abstract claims "minimal overhead," but the method involves alternating closed-form updates with lstsq solves.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"STB-LLM is missing as a baseline."** STB-LLM operates in a sub-1-bit regime (with sparsity + binarization), whereas all compared baselines and the proposed method sit at ≈1.06–1.11 bits with no sparsity. Comparing across regimes is not strictly required; the criticism is fair as a nice-to-have but not a Major issue. Removed from the main weakness list.
- **"Inconsistent bolding in Table 2 PTB row for LLaMA-2-7B."** Re-checking the row: PB-LLM 657.24 is in fact the lowest among all five methods listed for that cell (PB-LLM 657, ARB-X 681, ARB-RC 763, BiLLM 5243, Ours 3166), so bolding the best value is consistent with the table's convention. The harsh critic's reading was wrong.
- **"Eq. 2 typo ‖X̂Ŵ − X̂Ŵ‖²_F = 0."** This is almost certainly a parser/OCR artifact rather than a substantive error in the submission; under the parsing policy, removed.
- **Strength: "The paper addresses an important problem of LLM compression."** Generic; removed.
- **Strength: "Comprehensive ablations."** Tables 3 and 4 are useful but the selective-layer ablation is *missing*, which directly conflicts with this claim; the more specific AMP/RMSNorm strength supersedes it.

## Novel Insights
The paper's most genuinely novel observation is the asymmetric impact of output alignment on architectures with RMSNorm (LLaMA) versus LayerNorm (OPT): because RMSNorm strips magnitude information and leaves the model dependent on representation direction, naive output matching distorts token-similarity matrices in deeper layers, and this distortion is what AMP is designed to address. The supporting empirical pattern — AMP nearly doubles LLaMA-2-7B PPL when removed but barely moves OPT-6.7B — is concrete and not obviously a priori. Beyond this, the findings (block-level vs layer-level loss mismatch, error accumulation under X̂-conditioned objectives) re-express known phenomena from BRECQ-style work in the 1-bit LLM setting.

## Suggestions
- Re-derive AMP starting from Tr[ŴᵀMŴ] as the alignment objective directly, motivating it as preservation of the token-similarity Gram matrix; drop the Hadamard-norm step that the paper does not actually use.
- Define the AMP masks as {0,1} indicators on positive gradient sign and state the update as a selection, not a convex combination — or, if reflection is genuinely intended, motivate it. Make sure Table 3 is run against the version the paper describes.
- Add a per-layer-position ablation (which FC inside a block receives output matching) on at least one model.
- Report PTB results for the AMP and objective ablations on LLaMA-2-7B, and either diagnose the 3166-PPL failure or remove PTB-LLaMA-2-7B from the main table with a footnote applied uniformly across methods.
- Re-label the method as a hybrid in Tables 1–2 (e.g., "OA (last FC) + WA") to avoid overstating the framing.
- Provide variance numbers for the sub-PPL gaps at OPT-13B/30B and LLaMA-3-8B.

## Axis Assessment

- **Originality:** Modest. The paper is an incremental extension of ARB-LLM with one genuinely novel component (AMP). The framing of the three failure modes is useful but largely re-expresses BRECQ-style observations in a 1-bit LLM context.
- **Importance of research question:** Real but well-trodden. 1-bit PTQ for LLMs is an active sub-area with clear practical motivation.
- **Claims well supported:** Partially. "Consistently outperforms" is supported on most cells but contradicted by the LLaMA-2-7B PTB result and is not statistically backed at the larger scales where gains are small.
- **Soundness of experiments:** Mixed. The AMP ablation is convincing; the selective-layer claim is not ablated; the PTB failure is dismissed rather than investigated.
- **Clarity of writing:** Adequate at the analysis level. The AMP derivation (Eqs. 9–11) is the weakest section — the central novel mechanism is the one the paper specifies most ambiguously.
- **Value to research community:** Moderate. The RMSNorm-sensitivity observation and the modified objective are reusable insights even if AMP itself needs to be re-derived.

## Calibration

**Anchors retrieved (all rounds):**

Round 1 (bracketing):
- `6Mdvq0bPyG.md` (EfficientQAT) — avg 3.00 — weak QAT paper; this paper is more substantive than this anchor.
- `vw0NurJ7UX.md` (PrefixQuant) — avg 3.00 — weak activation-quant paper; not directly comparable but a low-band anchor.
- `0T8vCKa7yu.md` (CVXQ) — avg 3.00 — weak quantization paper; this paper has more empirical kernel.
- `cywG53B2ZQ.md` (NEAT) — avg 2.50 — unrelated alignment paper.
- `BifeBRhikU.md` (PB-LLM) — avg 6.75 — accepted partial-binarization paper, more novel than this one.
- `ZU8OdDLTts.md` (ARB-LLM) — avg 7.00 — accepted; this is the direct predecessor and considerably more novel.
- `RdG7LVGnQi.md` (One QuantLLM for ALL) — avg 4.50 — rejected; comparable level of incremental contribution.
- `6XUSDvBFkV.md` (STBLLM) — avg 6.00 — accepted; comparable in scope but more substantial (CUDA kernel + sub-1-bit framework).
- `wg1PCg3CUP.md` (Scaling Laws for Precision) — avg 8.00 — strong scaling-laws paper, far above this one.
- `TJo6aQb7mK.md` (Spectra/TriLM) — avg 7.60 — strong; well above.
- `eW4yh6HKz4.md` (CBQ) — avg 7.60 — strong cross-block quantization paper; well above.
- `E4Fk3YuG56.md` (Cut Cross-Entropy) — avg 8.50 — unrelated, well above.

Round 1 bracket: **4.0 to 6.0** — clearly above the 3.0 cluster (which are broken papers), below STBLLM (6.0) and PB-LLM (6.75) which have more substantial contributions, comparable to FlexBCQ/One-QuantLLM territory.

Round 2 (narrowing inside 4.0–6.0):
- `dZ3cI69BE8.md` (FlexBCQ) — avg 5.00 — read in full. Rejected. Comparable: an incremental quantization technique with empirical gains, criticized for novelty, readability, and missing ablations. This paper has more meaningful empirical gains in its niche but has more serious technical issues in its central novel mechanism (AMP). Roughly comparable, slightly weaker.
- `44pbCtAdLx.md` (I-LLM) — avg 5.00 — rejected integer-only quantization; comparable score band, different topic.
- `tjlTczcnPz.md` (SliM-LLM) — avg 5.40 — rejected mixed-precision; consistent improvements but novelty concerns. Comparable.
- `sYGNCscE9M.md` (Nearly Lossless Bit Switching) — avg 5.75 — rejected; comparable.
- `6XUSDvBFkV.md` (STBLLM) — avg 6.00 — re-read. Accepted. Clearly more novel (first sub-1-bit structural binarization, CUDA kernel) than the paper under review.
- `BifeBRhikU.md` (PB-LLM) — avg 6.75 — re-read. Accepted. More foundational contribution.

This paper sits below STBLLM (6.0) because (a) STBLLM introduces a new compression regime with a working kernel, while this paper is an ARB-LLM extension with notation issues in its novel mechanism, and (b) STBLLM's empirical story is cleaner than the PTB-LLaMA-2-7B failure here. It sits at or just below FlexBCQ (5.0): the methods are at comparable levels of incremental contribution, but this paper's AMP derivation/update issues are more serious than FlexBCQ's "limited novelty + readability" complaints, partially offset by the more concrete RMSNorm insight and substantive empirical gains on smaller models.

Settling at **4.5**: weaker than STBLLM at 6.0, in the same band as FlexBCQ at 5.0 but pulled slightly down by the AMP specification problems and the unaddressed PTB failure; clearly above the 3.0 cluster.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>