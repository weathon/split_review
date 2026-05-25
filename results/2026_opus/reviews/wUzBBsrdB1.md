I have enough calibration data. Let me write the final review.

## Summary
This paper argues that L0 (the sparsity hyperparameter in SAEs) is not a free design choice but has a "correct" value: setting it too low (or too high) causes the SAE decoder to mix correlated features rather than recover the underlying monosemantic ones. The paper shows in toy models that MSE loss *actively rewards* this mixing — so the ubiquitous sparsity-reconstruction tradeoff plot can prefer a corrupted SAE over the ground-truth SAE — and proposes a decoder pairwise cosine similarity metric (c_dec) as a proxy for finding the right L0, validated in toy models and partially on Gemma-2-2b / Llama-3.2-1b SAEs.

## Strengths
- **Clean toy-model causal demonstration** (§3.1, Figs. 2–3): Initializing the L0=1.8 SAE at the ground-truth solution and showing that gradient pressure moves it *away* from those features is a well-controlled experiment that isolates the mechanism rather than relying on correlation.
- **Direct, falsifiable indictment of sparsity-reconstruction plots** (§3.3–§3.4, Fig. 4): The trained SAE at L0=5 achieves MSE 2.73 while the ground-truth SAE forced to L0=5 achieves 4.88, and the variance-explained curve shows the ground-truth SAE being *rejected* by the standard evaluation plot. This is a structural critique of how the field has been ranking SAE methods, supported by concrete numerical evidence.
- **Sparse-probing alignment in LLMs** (§4, Fig. 8): The c_dec "elbow" coincides with peak k=16 sparse-probing F1 across both Gemma-2-2b layer 5 and Llama-3.2-1b layer 7 SAEs, providing real-LLM evidence that the toy-model intuition transfers — at least at the elbow.
- **Honest reporting of limitations** (§4, §4.2): The authors openly note that c_dec has a shallow region at Gemma-2-2b layer 5, that JumpReLU and BatchTopK have different c_dec minima, and that L0 may be too high and too low simultaneously per latent.

## Weaknesses

### Fatal
None.

### Major
- **The c_dec proxy is cleaner in toys than in LLMs, and the LLM "elbow" is identified post-hoc.** Fig. 8 (Gemma-2-2b layer 5) is described as having "a long shallow region with the global minimum actually appearing in that shallow region," and Fig. 9 shows the BatchTopK minimum near L0≈200 but JumpReLU's at 250–300 *on the same activations*. The headline claim that c_dec finds a single correct L0 is therefore weaker in the LLM regime than the abstract suggests: the "elbow" interpretation requires squinting and is anchored against sparse-probing peaks rather than independently identified. This matters because the practical deliverable of the paper — a metric to pick L0 without ground truth — is what generalizes least well.

- **Architecture-dependent c_dec minima undermine the "there is a correct L0" framing.** A property of the activations should not depend on the SAE architecture used to estimate it. The paper notes (§4.1) the JumpReLU vs. BatchTopK discrepancy without resolving it, and §4.2 acknowledges that "L0 can be both too low and too high simultaneously" for different latents. Combined, these point to the right framing being per-latent firing rates rather than a global L0 — which would weaken (without invalidating) the "most SAEs have L0 too low" headline conclusion.

### Minor
- **The §3.4 result is undersold.** The demonstration that a ground-truth SAE *loses* the sparsity-reconstruction comparison to a feature-mixing SAE is the paper's strongest and most actionable contribution, with implications for how prior comparisons (Gao et al., Rajamanoharan et al.) have ranked SAE methods. As written it occupies a single section and could be elevated and pushed harder.

- **The choice of c_dec form is asserted rather than justified in the main text.** §3.5 motivates pairwise absolute cosine similarity intuitively, but the projection-histogram formalization used in §4.2 (which seems more directly tied to the claimed mixing mechanism) is introduced later without an explicit comparison to c_dec. Appendix A.9 is referenced for alternatives, but the main text would benefit from explaining why this specific functional form was chosen.

- **The too-high-L0 mechanism is less developed than the too-low-L0 case.** §3.1's gradient-pressure control is for the low-L0 case; the paper claims "degenerate solutions" at high L0 but provides less analogous mechanistic evidence. Given that §4.2 leans on the high-L0 side of the asymmetry, this asymmetric depth of analysis is noticeable.

- **The k=16 sparse probing F1 dynamic range is small (0.78–0.82, 3 seeds).** Claims about "peak performance" rest on differences that, while consistent across the two models, are not heavily contextualized with respect to seed-level variance.

### Trivial
- The "long shallow region" phrasing for Gemma-2-2b layer 5 (§4) is informal — a quantitative criterion for the elbow would help.

## Nice-to-Haves
- An overcomplete (h >> g) toy-model experiment, since LLM SAEs use h=32768 against an unknown but presumably large feature count. The current toys essentially have h≈g, leaving a gap that the LLM section is asked to bridge alone.
- A per-latent diagnostic operationalizing the §4.2 observation (e.g., per-latent firing rate vs. projection-histogram width) — this could resolve both the architecture-dependent c_dec minimum and the global vs. per-latent L0 question.
- A demonstration that c_dec (or a variant) can serve as a *training-time* regularizer rather than only a post-hoc selection criterion that still requires sweeping L0.
- One or two reproductions of published SAE-method comparisons where the ranking *flips* once viewed through the §3.4 lens, to make the indictment of sparsity-reconstruction plots concrete rather than abstract.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Toy models are undercomplete/stylized in ways that matter for the headline claim."* — The paper explicitly scopes the toy section as a controlled environment with ground truth and uses §4 for the LLM regime. The harsh critic's deeper concern (that "correct L0" may be per-latent in the overcomplete regime) is preserved above as a Major weakness; the generic "toy is too small" framing without a specific failure is removed as scope-creep.
- *"Most SAEs use L0 too low" is a strong claim leaning on weak inference.* — This is partially the harsh critic's own speculation about what "too low" means across activation distributions; the paper's claim is more modest (Appendix A.13 catalogs Neuronpedia L0<100 alongside elbow estimates ~200). The empirical correlation with sparse probing supports the qualitative claim adequately.
- *Strength: "MSE comparison (2.73 vs 4.88) directly supports the claim that reconstruction loss pushes the SAE away from the correct dictionary."* — Kept as a strength under §3.3/§3.4 in the main review; not duplicated separately.

## Novel Insights
The genuinely novel observation surfaced across the inputs (and from the paper itself) is that the sparsity-reconstruction tradeoff plot, treated as a near-universal evaluation protocol in the SAE literature, is incentive-misaligned in the regime where existing SAEs operate: an SAE with the *correct* dictionary can be systematically ranked below an SAE that mixes correlated features at low L0. This generalizes the existing feature-hedging story (Chanin et al., 2025) into a critique of how the field compares architectures, not just how individual SAEs learn. The architecture-dependent c_dec minima (JumpReLU vs. BatchTopK on identical activations) is a smaller but real new puzzle that the paper raises without fully resolving.

## Suggestions
- Elevate §3.4 — the indictment of sparsity-reconstruction plots — into a co-headline contribution, and add a worked example reproducing a published comparison whose ranking changes under correct evaluation.
- Tighten the c_dec story in the LLM regime: replace the post-hoc "elbow" with a pre-registered criterion (e.g., the first L0 at which c_dec falls below k% of its maximum), or move c_dec from "method" to "diagnostic" framing.
- Develop §4.2's per-latent observation into a proper diagnostic and discuss what it implies for the architecture-dependent minima.
- Add at least one overcomplete (h >> g) toy experiment to bridge the toy-to-LLM gap.
- Symmetrize the gradient-pressure control: re-run the §3.1 initialization experiment for the too-high-L0 case.

---

### Axis-by-axis assessment
- **Originality**: Genuinely novel structural critique of sparsity-reconstruction plots; c_dec is a fresh proxy though imperfect.
- **Importance**: High — L0 selection and SAE evaluation protocols are central to the mechanistic-interpretability community right now.
- **Claim support**: Toy claims are well supported; LLM claims are supported only at the elbow and the architecture-dependence is honestly noted.
- **Soundness of experiments**: Toy experiments are clean and well-controlled; LLM experiments are honestly reported, with the caveats discussed.
- **Clarity**: Good; figures convey the core mechanism well.
- **Value to the community**: High for practitioners selecting L0 and for the broader debate on how to rank SAE methods.

### Calibration trail

Round 1 anchors retrieved (bracketing):
- `89wVrywsIy.md` (3.40) — SAE/Transcoder circuits; weaker writeup than this paper.
- `LQdaXixB0g.md` (2.50) — applied SAE psychiatry paper; far below.
- `UbLvSPMvMA.md` (1.67) — sparsity loss novelty; far below.
- `Wxl0JMgDoU.md` (2.50) — applied SAE chess; far below.
- `F76bwRSLeK.md` (4.80) — foundational SAE paper (Cunningham et al.); comparable importance, different era.
- `ZtvRqm6oBu.md` (5.25) — SAE unlearning; similar empirical character, less structural.
- `1Njl73JKjB.md` (7.00) — principled SAE evaluation; comparable in ambition, broader framework.
- `9ca9eHNrdH.md` (7.00) — canonical units / meta-SAEs; closest sibling — critique of SAE assumption + new method.
- `tcsZt9ZNKD.md` (8.20) — scaling SAEs (Gao et al.); above this paper's scope.
- `I4e82CIDxv.md` (8.00) — sparse feature circuits; above.
- `EytBpUGB1Z.md`, `aWXnKanInf.md` (both 8.00) — off-topic.

Round 1 bracket: between 5.0 and 7.0, leaning toward the upper half because the structural critique (§3.4) is comparable to the "Canonical Units" paper.

Round 2 anchors retrieved (narrowing within 4.5–7.5):
- `ghH6YYDs15.md` (4.67) — SAE amortization gap; mostly theoretical, less impactful.
- `OeHSkJ58TG.md` (5.67) — incidental polysemanticity; clean toys, less clean LLM evidence, comparable structural insight but less prescriptive.
- `XAjfjizaKs.md` (6.50) — multi-layer SAEs; comparable empirical depth and honesty.
- `d63a4AM4hb.md` (7.00) — non-linear features; broader, more thoroughly validated.
- `1Njl73JKjB.md` (7.00), `9ca9eHNrdH.md` (7.00) — confirmed as nearest siblings.

Round-2 comparison: this paper is stronger than the 5.67/4.80 anchors (cleaner mechanism, real LLM validation), comparable to MLSAEs (6.50) in empirical character and honesty, and slightly below the 7.0 "Canonical Units" and "Principled Evaluations" papers because the c_dec metric is acknowledged as noisier and architecture-dependent in the LLM regime. Final score sits between MLSAEs (6.5) and the 7.0 cluster.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>