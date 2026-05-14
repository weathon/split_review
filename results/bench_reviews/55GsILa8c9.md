## Summary
CausalNovo proposes a model-agnostic add-on for de novo peptide sequencing that frames the task with a Structural Causal Model and extracts "causal" peak representations via (a) a contrastive independence objective between original and perturbed spectra, (b) sufficiency/purification cross-entropy losses on causal/non-causal sub-representations, and (c) a label-guided causal intervention that replaces noise peaks (identified by m/z distance to the theoretical spectrum) and injects theoretical b/y/a ions. Plugged into CasaNovo, AdaNovo, and π‑HelixNovo on three NovoBench datasets, it produces consistent AA/peptide/PTM gains and improved stability under non-causal peak perturbations.

## Strengths
- **Model-agnostic, repeatedly validated**: The framework is integrated into three different baselines (CasaNovo, AdaNovo, π-HelixNovo) and yields directionally consistent gains across Nine‑species, Seven‑species, and HC‑PT (Tables 1–2), with leave‑one‑species‑out cross‑species evaluation (Table 3) and NSR‑stratified analysis (Fig. 4).
- **Useful inductive bias for spectra**: Identifying non‑causal peaks via theoretical b/y/a ion spectra and replacing them with other-batch noise peaks is a sensible and realistic augmentation strategy; the 18-ion-type robustness check (Table 6) shows the strategy is not overly sensitive to ion-type choice.
- **Component-level ablations and interpretability evidence**: Tables 4–5 separate the contribution of independence, purification, symmetric training, replace, enhance, and drop, and Table 7 shows a measurable shift in attention toward causal peaks (19.26% → 32.87% fully-causal attention) — concrete evidence that the auxiliary objectives change model behavior.
- **Acknowledged costs**: §5 reports the ~2.3× training overhead and <1% inference overhead honestly.

## Weaknesses

### Fatal
None — the empirical contribution is real even after stripping the causal framing.

### Major
- **Robustness evaluation is largely circular with training signal.** The headline "vulnerability" results (Figs. 1, 3; Table 6) define noise peaks via m/z distance to the theoretical spectrum — exactly the same definition used to construct training-time interventions (Eq. 4). The 18-ion-type variant in Table 6 partially mitigates this, but the perturbation distribution and the training-time augmentation distribution are not independent. The paper's motivating story (matrix effects, co‑elution, contaminants in §1) is not actually tested with any independently-defined real perturbation (cross-instrument, contaminant-spiked, OOD lab). This weakens the "causal generalization" framing of the central claim.
- **The "purification" objective `max I(z_s; Y)` is conceptually backwards relative to its variable naming.** §3.3 defines `z_s = (1−M) ⊙ z` as the *non‑causal* representation, then trains it to predict Y by CE (Eq. 6). The justification ("indirectly leads to purification of z_c", citing Chen et al. 2022) is a single sentence with no derivation, and Table 4 attributes a real chunk of gain (+0.8% AA prec.) to this component. Either the variable semantics or the loss direction is mis‑labeled in the manuscript; the reader cannot reconcile the two without external context. Empirically demonstrating that trained `z_s` does *not* in fact predict Y (or rederiving the objective) would resolve this.
- **Retrained baselines diverge from published numbers in both directions and no variance is reported anywhere.** †AdaNovo on Nine‑species drops from 0.698 → 0.681; †π‑HelixNovo HC‑PT drops 0.588 → 0.532; †CasaNovo Seven‑species jumps 0.322 → 0.357. With ablation deltas as small as +0.4% in Table 4 and a sizable π‑HelixNovo retrain regression, the cleanly reported "+12% / +14.2%" improvement numbers are difficult to interpret. No seeds, no CIs, no significance tests on any of Tables 1–7.

### Minor
- **The "causal intervention" depends on label-derived theoretical spectra at training time.** §3.4.1 explicitly defines `x_intervene = x_replace ∪ x_theory`, i.e., the encoder sees the theoretical peaks (a strong label-derived signal) during training. The paper does not analyze how much of the gain is attributable to this leak vs. the contrastive/purification objectives. A control training the encoder *only* with label-derived theoretical peaks added (without the contrastive or purification losses) would tighten the attribution; Table 5 only partially isolates this.
- **The link from Eq. (5) (InfoNCE over augmented views) to `P(C|S) = P(C|do(S))` is asserted, not shown.** This is contrastive augmentation; the identification claim hinges on the assumption that the label-derived noise mask isolates `S`, which is not formalized.
- **§3.2 SCM omits the precursor `t`** that decoding explicitly conditions on in Eq. (1) and again in §3.3. The structural equation `Y = g(C)` implies `Y` is a deterministic function of `C` alone, which is not what the model implements. This is a presentation issue but matters because the SCM is what motivates the design.
- **Cross‑species (Table 3) is only run with CasaNovo.** The "model‑agnostic" claim under distribution shift is therefore not fully tested.
- **Percentage vs. absolute confusion in §4.3.** Improvements stated as "+12%" / "+14.2%" are absolute precision differences, not relative percentages, which inflates perceived magnitude.

### Trivial
- Table 4/5 checkmark formatting makes it ambiguous which row enables which component (likely a parsing artifact, but worth verifying in the camera-ready).

## Nice-to-Haves
- A robustness evaluation defined *independently* of the training-time noise mask: contaminant-spiked spectra, cross-instrument data, or an OOD protocol like ContraNovo/RankNovo's.
- Multi-seed runs with CIs on at least the headline cross-baseline numbers and ablation deltas <1%.
- Either drop or formalize the "intervention/do" language. The method's contribution stands on its own as a principled label-guided augmentation + contrastive regularization; it does not need the do-calculus claim.
- Sensitivity curve over the m/z tolerance γ at training time (Table 6 only reports the evaluation-side sweep).

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- "The causal framing is purely decorative" — partially valid as critique but overstated as a fatal flaw. The paper does derive its losses from SCM-motivated principles (independence, sufficiency), and the disentangled representation + intervention machinery, while not a do-calculus identification result, is a legitimate operationalization of those principles. It is fairer to call the framing loose than empty.
- "Strawman strength: principled causal formulation is a strength of the paper" (Strength Finder #1) — already substantially undermined by the Major weakness above; the formulation is suggestive rather than identification-grounded.

## Novel Insights
None beyond the paper's own contributions. The label-guided augmentation idea (replace noise peaks with batch-sampled noise peaks; inject theoretical b/y/a peaks) is a genuinely useful inductive bias for spectra, but it is presented in causal vocabulary rather than as a novel methodological insight per se.

## Suggestions
1. Reconcile `max I(z_s; Y)` with the non-causal naming of `z_s` — either rederive, rename, or empirically check that trained `z_s` is not predictive of Y.
2. Add a label-leak ablation: train with the augmentation but disable contrastive + purification, and vice versa, to attribute gain.
3. Report multi-seed mean ± std on at least Tables 1, 4, 5.
4. Add at least one evaluation where the perturbation is *not* a function of `Y` (e.g., contaminant injection, cross-instrument, or an existing OOD split).
5. Either supply an identification argument tying Eqs. (3)–(6) to the do-operator, or soften the causal language to "causally-motivated regularization."

---

## Evaluation along requested axes
- **Originality**: Moderate. The SCM framing for de novo sequencing is new in this subfield, but operationally the method is contrastive augmentation + auxiliary CE on a label-derived mask — close in spirit to existing causal supervised learning works (Chen et al. 2022) and label-conditioned augmentation in mass spec literature.
- **Importance**: The problem (noise sensitivity in de novo sequencing) is real and well-motivated; gains, if they survive variance scrutiny, are practically meaningful.
- **Claim support**: The "consistent gains" claim is well-supported across three baselines and three datasets. The "causal generalization" claim is not well-supported — the robustness eval reuses the training-time noise definition.
- **Soundness**: Empirically reasonable; theoretically loose (purification objective vs. variable semantics; no identification argument; no variance reporting).
- **Clarity**: Generally clear; SCM/decoder-conditioning inconsistency and the purification rationale are the main rough spots.
- **Value**: Useful add-on recipe; the framing oversells a method that would stand fine as label-guided augmentation + contrastive regularization.

## Score and Decision

Anchors considered:
- `/home/wg25r/.../uQnvYP7yX9.md` (ReNovo, avg 6.50) — same domain, accepted. Comparable empirical breadth, less ambitious framing; CausalNovo's gains are comparable but the causal framing is the wobbly part. CausalNovo is in the same ballpark, slightly weaker in theoretical claim integrity.
- `/home/wg25r/.../87B3zDRMjv.md` (RankNovo, avg 5.50) — same domain, rejected. CausalNovo has somewhat broader integration (3 baselines plugged in directly) but shares the issue of framing not fully landing. CausalNovo ≈ RankNovo or slightly above.
- `/home/wg25r/.../I2ZYngkRW6.md` (NAT→AT distillation for de novo, avg 4.25) — same domain, rejected. CausalNovo is clearly stronger (broader empirical sweep, ablations).
- `/home/wg25r/.../78tc3EiUrN.md` (MADGEN, avg 6.00) — adjacent domain, accepted. CausalNovo not as cleanly motivated.
- `/home/wg25r/.../Mfnh1Sqdwf.md` (Seq2Exp, avg 7.50) — causal representation in genomics, accepted. Better identified causal pipeline than CausalNovo; CausalNovo is below.
- `/home/wg25r/.../F4IMiNhim1.md` (CRE design RL, avg 7.00) — bio-ML, accepted. Different topic; CausalNovo less novel methodologically.
- `/home/wg25r/.../AvXrppAS2o.md` (causal structure learning, avg 3.00) — rejected. CausalNovo clearly stronger empirically.
- `/home/wg25r/.../WpjehX0TM2.md` (causal RL point processes, avg 4.33) — rejected. CausalNovo stronger.
- `/home/wg25r/.../4QVgnxXVDB.md` (3CIL causality-inspired contrastive IL, avg 5.00) — rejected. Very similar critique pattern (causal framing decorative); CausalNovo has broader and more convincing empirics, so slightly above.
- `/home/wg25r/.../ozZG5FXuTV.md` (Causal Alignment Disease Diagnosis, avg 6.00) — accepted. CausalNovo less rigorous on causal mechanism.
- `/home/wg25r/.../aqvf3R48pl.md` (causality-guided CL, avg 4.40) — rejected. CausalNovo stronger empirically.
- `/home/wg25r/.../W0zgCR6FIE.md` (Spawrious, avg 5.75) — rejected. Different scope.
- `/home/wg25r/.../GF6UrrTWp1.md` (Invariance Starvation, avg 2.60) — rejected. CausalNovo well above.
- `/home/wg25r/.../2uQBSa2X4R.md` (Robust Gymnasium benchmark, avg 6.50) — accepted. Different scope.
- `/home/wg25r/.../Pa4hecILrt.md` / `/home/wg25r/.../lnVPfgRnIV.md` / `/home/wg25r/.../HCCkCjClO0.md` / `/home/wg25r/.../8QTpYC4smR.md` / `/home/wg25r/.../gENfMmUIkT.md` / `/home/wg25r/.../nSDOkm0SKo.md` — unrelated/low-quality, CausalNovo clearly above all.

CausalNovo sits between ReNovo (6.5, accept, same domain, cleaner framing) and RankNovo (5.5, reject, same domain, similar "frame oversells" issue) and 3CIL (5.0, "causality decorative"). Empirically richer than 3CIL/RankNovo but with a more strained theoretical story than ReNovo. Net: a borderline paper, slightly on the reject side because the central causal-generalization claim is propped up by a circular robustness eval.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>