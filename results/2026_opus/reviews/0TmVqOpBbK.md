Now I have enough calibration to write the final review.

## Summary
The paper proposes a "conditional scaling law" that augments Chinchilla with two architectural axes — hidden size $d_{\text{model}}$ and the MLP-to-attention ratio $r_{\text{mlp/attn}}$ — using a multiplicative calibration of a reference loss $L_{\text{opt}}(N,D)$. The authors train >200 models from 80M to 3B parameters, use the fit to design "Panda" and "Surefire" architectures, and report up to 2.1% accuracy and 42% throughput improvements over LLaMA-3.2 architectures under matched 100B-token training. The most striking empirical observation is that LLaMA-style models are MLP-heavy (r≈5) and a more balanced r≈1 with larger $d_{\text{model}}$ Pareto-dominates on both loss and inference throughput.

## Strengths
- **Substantial empirical scope.** Training >200 models up to 3B parameters and validating throughput across both vLLM/A100 and SGLang/H200 (§5.1, Appendix G) is genuine, expensive work and a meaningful empirical contribution.
- **A useful and unexpectedly clean architectural finding.** Figures 4 and 5 show that loss exhibits a consistent U-shape in both $d_{\text{model}}/\sqrt{N}$ and $r_{\text{mlp/attn}}$ at 80M, 145M, and 297M, with stable optima — a clean qualitative result that motivates the search.
- **Concrete, end-to-end validation at the 1B scale.** Panda-1B at 57.0% avg vs LLaMA-3.2-1B-arch at 54.9% (Table 1) is a credible +2.1% gap supported by the lowest training loss among the exhaustive 1B sweep (Figure 7 left).
- **Controlled inference-throughput ablations.** Figure 3 varies one architectural factor at a time under fixed $N_{\text{non-embed}}$, isolating throughput effects cleanly enough to justify the search-space design.

## Weaknesses

### Fatal
None.

### Major
- **The paper's own ablation undermines its "scaling law" framing.** Figure 8 / Table 2 / §5.1 show that fitting on (80M, 145M, 297M, 1B) and extrapolating to 3B gives Spearman = 0.50, while fitting on 1B alone gives Spearman = 1.0. The paper concludes "it is often sufficient, and sometimes preferable, to fit the law using models within a closer size range to the target, such as about one third of its scale." This is structural: a scaling law's value is extrapolation from substantially smaller experiments. The functional form in Eq. (3) is also separable — the only $(N,D)$ dependence is through $L_{\text{opt}}$, and the coefficients $a_i,b_i$ are claimed to be "shared across all $N, D$" yet shift materially between the (80M–297M) fit ($a_0=2.697,\ldots$) and the 1B fit ($a_0=2.319,\ldots$). The paper acknowledges the drift only as a "fitting-data strategy" issue and does not engage with what it implies for the functional form. Either modeling the $N$-dependence of the coefficients (e.g., $a_i(N) = a_i^0 + a_i^1 \log N$) or reframing the contribution as architecture optimization within a fixed scale band would resolve this, but as written the framing oversells what the apparatus delivers.

- **$L_{\text{opt}}(N,D)$ is "empirically searched," not predicted.** §4 explicitly states "instead of fitting the Chinchilla scaling law, we empirically searched over architecture variants to find the optimal loss $L_{\text{opt}}(N, D)$ for $N_{\text{non-embed}} < 1\text{B}$ scale." This means the multiplicative anchor is the minimum observed loss in the existing sweep, so (i) the calibration absorbs whatever optimization noise drove that minimum, and (ii) the framework cannot be applied at any $N$ without already running a saturated sweep at that $N$. This makes the "scaling-law abstraction" weaker than presented; it is closer to within-scale curve fitting plus an empirical reference.

- **Headline gains rest on single training runs without variance estimates.** Table 1 reports Panda-3B at avg 62.5 vs LLaMA-3.2-3B-arch at 61.9 — a 0.6-point gap with a loss difference of only 0.006 (2.625 vs 2.619). At 100B-token pretraining, this is within the range where seed noise can plausibly explain the gap. No seeds or confidence intervals are reported. A small-scale seed study at 297M for the final architectures would substantially raise confidence that the 3B gain is signal, not noise. The 1B gap (0.021 loss, 2.1% avg) is much more credible, but is still a single run.

### Minor
- **Abstract overclaims the cross-scale reliability.** The abstract states "the conditional scaling law reliably predicts optimal architectural choices," but the Spearman drops monotonically across Tasks 1–3 (0.89 → 0.79 → 0.75) and to 0.50 by the 3B extrapolation in Figure 8. The body acknowledges this; the abstract should too.
- **Comparison framing.** The text says "outperforms LLaMA-3.2-3B" and "outperform the open-weight LLaMA-3.2-3B baseline configs." A reader scanning the abstract would naturally read this as comparison to the public LLaMA-3.2 checkpoint, when in fact it is the LLaMA-3.2 *architecture* retrained under the paper's 100B-token setup. This is correct experimental practice but should be stated explicitly.
- **Fixing $m_{\text{layer}}$.** §3.1 fixes the number of layers because "varying $m_{\text{layer}}$ under a fixed $N_{\text{non-embed}}$ substantially impacts both inference cost and accuracy." This is the kind of factor a scaling law over architecture should ideally handle, not exclude — especially since the cited prior work (Bian et al. 2025) covers depth via aspect ratio. The choice to fix it is defensible but in tension with the "general framework for incorporating broader architectural factors" framing.
- **Functional-form choice is under-justified.** §3.3 introduces $c_0 + c_1\log x + c_2/x$ as "effectively models the U-shaped behavior." Other U-shaped forms (quadratic in $\log x$, etc.) are not compared; this is acknowledged but the choice isn't motivated beyond convenience.
- **Optimum trajectory across $N$ is not plotted directly.** Both Panda-1B and Panda-3B land near $d/\sqrt{N}\approx 0.08, r\approx 1$, but the paper does not plot the optimum's trajectory across 80M/145M/297M/1B/3B — which would be the most informative diagnostic for whether the architectural optimum actually stabilizes.

### Trivial
- The monotone Spearman degradation 0.89 → 0.79 → 0.75 → 0.50 from Task 1 to the 3B extrapolation could be visualized in a single figure rather than scattered across Figures 6 and 8.

## Nice-to-Haves
- A phenomenological fit of how $a_i, b_i$ depend on $N$ (even just $a_i(N) = a_i^0 + a_i^1 \log N$) would let the paper either recover its scaling-law claim or demonstrate, as a finding, that the architectural optimum drifts with $N$.
- A 3-seed study at 297M (and ideally one seed pair at 1B) for the chosen architectures would convert the 3B 0.6-point gap from suggestive to credible.
- A sharper relationship to Bian et al. (2025) — how much of the Panda gain would already be captured by an aspect-ratio search at fixed $m_{\text{layer}}$? — would strengthen the contribution claim.

## Removed Points

These points are flagged to be removed, treat them with caution.

- *(Harsh critic)* "GQA handled as a discrete local search after the continuous optimization reveals the law really only covers two of the three architectural variables." The paper explicitly motivates this in §3.4 ("GQA does not exhibit a consistent continuous relationship with loss (Figure 24, Appendix I)"), and presents the discrete search as a deliberate engineering decision. This is a reasonable scoping choice rather than a flaw.
- *(Harsh critic)* "Throughput analysis is hardware- and serving-stack-specific." The paper validates on both vLLM/A100 and SGLang/H200 (Appendix G, Table 6) — this concern is largely addressed.
- *(Strength finder)* "Addresses an important problem of inference-efficient LLMs." Too generic; importance of the topic is a framing claim, not a strength.
- *(Strength finder)* "U-shaped relationship consistent across three model sizes." Already counted in Strengths above; not separately retained.

## Novel Insights
The paper's most novel observation — that LLaMA-style architectures with $r\approx 5$ are notably MLP-heavy and that $r\approx 1$ with larger $d_{\text{model}}$ Pareto-dominates on both loss and inference throughput — is genuinely useful and goes against current open-weight design trends. This finding stands on its own even if the scaling-law apparatus is read as a search heuristic rather than as a predictive law. Nothing beyond the paper's own contributions emerges from the reviews.

## Suggestions
- Either (a) make $a_i(N), b_i(N)$ explicit functions of $N$ and show stabilization, or (b) reframe the contribution as an architecture-search procedure at a target scale class with an empirical reference loss.
- Report seed variance for at least one of the 1B or 3B comparisons; without it, the 3B 0.6-point gap is not convincing.
- Tighten the abstract: the law's cross-scale reliability is much weaker than "reliably predicts" suggests, and the LLaMA-3.2 comparison is architecture-only.
- Plot the optimal $(d/\sqrt{N}, r)$ as a function of $N$ across 80M–3B; this is the most informative diagnostic and the paper currently leaves it implicit.
- Add a direct comparison to Bian et al. (2025)'s aspect-ratio search to clarify the marginal value of jointly searching $d_{\text{model}}$ and $r$.

## Evaluation by axis
- **Originality:** Moderate. The architectural finding (MLP-heaviness of LLaMA) is novel and concrete; the formal "conditional scaling law" is a modest extension of Chinchilla.
- **Importance of research question:** High. Inference-aware architecture design under fixed parameter/token budgets is practically important.
- **Whether claims are well supported:** Mixed. The 1B-scale findings are well supported; the cross-scale "scaling law" claim is partially contradicted by Figure 8, and the 3B accuracy gap lacks variance evidence.
- **Soundness of experiments:** Reasonable scope (>200 models, 3B scale), but single-seed and the L_opt empirical-search choice weaken the formal apparatus.
- **Clarity of writing:** Generally clear; abstract overclaims relative to body.
- **Value to the research community:** A useful practical pointer (try r≈1, larger $d_{\text{model}}$, more GQA) backed by real training runs; the formal framework as presented is less reusable.

## Score and Decision

**Calibration anchors retrieved:**

Round 1 (bracketing):
- BjZP3fTlVg.md (3.00, Reject) — efficient LLM deployment, weaker than this paper
- 2DD4AXOAZ8.md (2.00, Reject) — MixAttention; less rigorous than this paper
- BmYzoPppij.md (3.33, Reject) — LLM carbon footprint; weaker than this paper
- ulGwcj1egv.md (3.00, Reject) — input-adaptive latency reduction; weaker than this paper
- BDisxnHzRL.md (4.25, Reject) — scaling laws for downstream perf; somewhat weaker
- VNckp7JEHn.md (5.75, Accept) — inference scaling laws; more rigorous question framing
- xGM5shdGJD.md (5.20, Reject) — scaling-law estimation best practices; comparable rigor
- iZeQBqJamf.md (6.50, Accept) — over-training scaling; cleaner methodology than this paper
- 6VhDQP7WGX.md (5.80, Accept) — VLM inference scaling; comparable scope
- wg1PCg3CUP.md (8.00, Accept) — precision scaling laws; substantially more principled
- TJo6aQb7mK.md (7.60, Accept) — ternary LM pretraining; substantially more rigorous
- Tzh6xAJSll.md (7.60, Accept) — associative memory scaling; cleaner theory
- E4Fk3YuG56.md (8.50, Accept) — cut cross-entropy; out of scope but strong

Round-1 bracket: between 4.5 and 6.

Round 2 (narrowing):
- xGM5shdGJD.md (5.20, Reject) — read in full; similar scale of empirical contribution, presentation issues; this paper sits comparably
- iZeQBqJamf.md (6.50, Accept) — read in full; substantially more rigorous extrapolation evidence than this paper
- mao3y822aM.md (5.50, Reject) — NanoLM; closely analogous (predict large-model loss from small-scale fits for architecture comparison) and lands at 5.5
- T2h2V7Rx7q.md (5.25, Reject) — multilingual scaling laws; comparable level of ambition vs. evidence
- zpBamnxyPm.md (5.75, Reject) — downstream-capability prediction; comparable
- UatDdAlr2x.md (5.75, Reject) — attention/feed-forward interplay; comparable
- 7JU8TwFXGC.md (5.00, Reject) — LLM PP for NAS; weaker
- VAwgL8kPvr.md (4.67, Reject) — structural pruning via NAS; weaker
- d4uL2MSe0z.md (4.50, Accept) — dynamic layer tying; not directly comparable
- o9YC0B6P2m.md (6.75, Reject) — LR annealing scaling; more elegant equation, comparable rigor

Reading NanoLM (mao3y822aM, 5.5) and Hitchhiker's Guide (xGM5shdGJD, 5.2) closely: this paper has comparable empirical scope to NanoLM (200+ models, scaling to 3B vs NanoLM's prediction up to 52B), but NanoLM's μP+μScaling apparatus actually extrapolates, whereas this paper's central ablation shows its extrapolation breaks down across scales (Spearman 0.50 at 3B). Conversely, this paper's architectural finding (r≈1 vs LLaMA's r≈5) is more directly actionable than either anchor. Against iZeQBqJamf (6.5, Accept), this paper is clearly weaker on extrapolation rigor and variance reporting.

The paper lands somewhat below NanoLM (5.5) due to the structural framing-vs-evidence mismatch — Panda-3B's small 0.6% gap without variance and the explicit Spearman 0.50 cross-scale breakdown — but somewhat above the (4–4.5) anchors because the architectural finding is concrete and the 1B-scale evidence is genuinely strong.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>