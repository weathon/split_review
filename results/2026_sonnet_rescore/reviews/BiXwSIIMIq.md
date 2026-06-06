Now I have enough information to write the final authoritative review. Let me carefully filter the reviewer claims against what the paper actually says.

---

## Summary

This paper proposes ADMM Plug-and-Play (ADMM-PnP) with the AC-DC denoiser for solving inverse problems using score-based generative priors. The method addresses manifold mismatch in ADMM via a three-stage denoiser: Auto-Correction (AC) via additive Gaussian noise, Directional Correction (DC) via conditional Langevin dynamics, and a final score-based denoising step. The paper establishes convergence guarantees — ball convergence under strong convexity (Theorem 1–2) and bounded convergence under an adaptive step-size schedule (Theorem 3) — and demonstrates state-of-the-art performance across six inverse problems on FFHQ and ImageNet.

---

## Strengths

- **Novel convergence analysis for score-based ADMM-PnP**: Theorem 2 establishes that the AC-DC denoiser is weakly nonexpansive with high probability (under Assumptions 1–3), and together with Theorem 1 this provides ball-convergence guarantees for strongly-convex losses. Theorem 3 extends this to the non-convex regime under an adaptive ρ-schedule. These are concrete theoretical advances over prior PnP convergence analyses (e.g., Chan et al. 2016; Ryu et al. 2019) that did not apply to diffusion-score denoisers.

- **Strong empirical results across a diverse evaluation suite**: Table 1 reports PSNR, SSIM, and LPIPS across six tasks (4× super-resolution, random/box inpainting, Gaussian/motion deblurring, phase retrieval) on FFHQ and ImageNet (100 test images each). Both Ours-tweedie and Ours-ode achieve best or second-best across most settings against seven baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DCDP, PMC). On phase retrieval — the hardest task — the proposed method leads by a clear margin: FFHQ PSNR 27.944 vs. DAPS 26.707.

- **Well-motivated three-stage design**: The decomposition of the manifold alignment problem into AC (global noise injection) and DC (conditional Langevin refinement) is clearly motivated theoretically in Section 3, and the qualitative ablation in Figure 5 shows that DC steps (J=10, J=20) progressively remove reconstruction artifacts compared to AC-only (J=0) on phase retrieval.

---

## Weaknesses

### Fatal
None.

### Major

- **No NFE or runtime comparison with baselines**: The paper's own Limitations section acknowledges that "each iteration of AC-DC denoiser needs multiple score evaluations," and Figures 3–4 explicitly compare against "DAPS-4K" (implying a 4,000-NFE budget for DAPS). Yet no NFE count or wall-clock time is reported for the proposed method. Given that the AC-DC denoiser stacks up to 1,000 Adam steps for the x-subproblem, J=10 DC score evaluations, and 1 or 10 final denoising evaluations per outer ADMM iteration, the total compute could be comparable to or exceed DAPS-4K. Without this, readers cannot determine whether gains over DAPS and DiffPIR are due to the AC-DC design or simply due to greater compute budget. This is the most significant evidential gap in the paper.

- **DC contribution supported only qualitatively**: Figure 5 — the main ablation for the DC step — shows only visual comparisons (J=0 vs. J=10 vs. J=20 on two phase retrieval examples) with no quantitative PSNR/SSIM/LPIPS numbers. Since DC is the paper's central algorithmic novelty over prior noise-injection methods (DiffPIR, SNORE), a quantitative table isolating (AC-only + Tweedie) vs. (AC+DC + Tweedie) across all six tasks is needed to establish that DC provides independent, measurable benefit. The current evidence is insufficient to separate the contribution of DC from the ADMM structure and AC step.

- **Theory-practice gap for non-convex tasks**: Theorem 1 requires μ-strong convexity of ℓ, which the paper (Section 4.3) explicitly acknowledges fails for super-resolution, inpainting, and phase retrieval — the majority of tested tasks. Theorem 3 covers the non-convex case but requires an adaptive ρ-schedule; the Limitations section itself calls this "arguably less appealing in practice" and confirms that all experiments use constant ρ. The result is that the practically-relevant regime (non-convex loss, constant ρ) lacks a convergence guarantee, and the existing guarantees apply either to tasks not tested (strongly convex) or to a schedule not used (adaptive ρ). This gap is acknowledged but understated.

### Minor

- **Multiple unexplained PMC rows in Table 1**: PMC appears with two different numeric rows for Superresolution (e.g., FFHQ: 27.761/0.639/0.332 and 23.774/0.421/0.407) and has blank entries for several other tasks. No explanation is given for what distinguishes the two configurations, nor is it clear whether the blank entries represent failed runs or omitted evaluations. This undermines the completeness of the baseline comparison.

- **Box inpainting: DCDP outperforms both proposed variants on PSNR by 1.2 dB** (25.230 vs. 24.025 for Ours-tweedie on FFHQ). The claim that the method achieves "best or second-best performance in almost all inverse problems" is technically accurate but elides this specific case where the proposed method is noticeably outperformed. A brief discussion of why box inpainting is harder for the proposed approach would be informative.

- **Gaussian likelihood approximation unvalidated**: The DC step is derived by approximating p(z_ac^(k) | z_σ^(k)) as Gaussian, valid when Var(s^(k))^{1/2} ≪ σ^(k) (Section 3). The correctness of this approximation — which determines whether DC targets the correct conditional distribution and hence whether the manifold-alignment argument holds — is never checked empirically for the actual schedules used. At minimum, an informal verification (e.g., showing that Var(s^(k)) and σ^(k) satisfy this ordering along the practical schedule) would strengthen the method's theoretical grounding.

- **Practical schedule not verified against Theorem 3(b) limit conditions**: The practical schedules σ^(k) = max(0.1, 10 − (10−0.1)·k/W) and σ_s^(k) = 0.1/√σ^(k) are described as "guided by empirical heuristics" (Limitations). Whether these satisfy the limit conditions in Theorem 3(b) — in particular lim_{k→∞} σ_s^(k)² / (1 − Mσ_s^(k)²) · log(2/ν_k) = 0 — is never verified. The theory and practice are therefore somewhat disconnected.

### Trivial

- The notation around Eq. (9) in Section 3 uses z_σ^(k) in overlapping roles (as both the noisy target and the AC output), which makes the mathematical exposition harder to follow than needed.

---

## Nice-to-Haves

- A single quantitative ablation table — (AC only), (AC+DC), (full method) across all six tasks — would sharply justify the DC contribution and is the most impactful addition the authors could make.
- Providing explicit verification that the practical schedule satisfies the Theorem 3(b) limit conditions (or noting where it falls short) would close the theory-practice gap in a transparent way.
- An NFE/runtime table alongside Table 1 would allow readers to judge efficiency-accuracy tradeoffs directly.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Appendix E.2 unverifiable**: The harsh critic notes that "Appendix E.2 is stripped from the submitted version." Per hard rules, appendix content exists in the original submission; this criticism is removed.

- **Section 4.3, Theorem 3(a) — c_k growth via log²(ν_k)**: This is a highly technical sub-concern ultimately about whether the practical schedule satisfies Theorem 3(b), which is already captured as a Minor weakness. The standalone criticism depends on detailed symbolic analysis without a clear anchor in the paper text as-is; demoted and merged into the Minor weakness on schedule verification.

- **DC stationarity assumption — "J=10 almost certainly insufficient"**: The harsh critic speculates that J=10 Langevin steps cannot reach stationarity in high-dimensional image space. This is plausible but not demonstrated from the paper; the paper explicitly defers to Appendix E.2 for the finite-step analysis (Footnote 1). Per hard rules on appendix content, the concern about Appendix E.2 being unverifiable is removed. The residual concern (finite J vs. ideal stationarity) is real and acknowledged by the paper in Limitations, but it is a known theoretical approximation rather than a flaw; demoted to an acknowledged limitation rather than a counted weakness.

- **Strength Finder – "well-motivated design with ablation" (as a full strength)**: The ablation is qualitative only (Figure 5), so claiming "necessity of DC is validated" overstates the evidence. Demoted; the qualitative result remains cited but the claim of validation is weakened in the Strengths section above.

---

## Novel Insights

The paper's most under-emphasized insight is that the two-stage noise manipulation (AC + DC) is necessary precisely because ADMM's dual variable perturbs iterates away from the score's training manifold in a structured way that simple noise injection does not fully correct. The DC step's conditional Langevin dynamics provides a data-driven "correction" that depends on the current ADMM state, making it fundamentally different from noise injection used in DiffPIR or SNORE. This distinction — that the correction must be *directional* and *state-dependent* — is the conceptual contribution that the paper would do well to foreground more explicitly, as it explains both why prior noise-injection methods fall short and why DC provides incremental benefit even when AC already reduces manifold mismatch.

---

## Suggestions

1. **Report NFE for all methods** in Table 1 (or a companion table). If Ours-tweedie/ode requires significantly more NFE than DAPS-4K, acknowledge it and frame the gains accordingly; if comparable, this becomes a selling point.
2. **Add one quantitative ablation row** in Table 1 for "AC only (J=0)" to quantify what DC adds beyond noise injection across all six tasks.
3. **Verify the practical schedule** against Theorem 3(b) conditions, or state explicitly in the text that the current schedule is heuristic and may not satisfy the theoretical requirements.
4. **Explain the PMC rows**: clarify in Table 1's caption what the two PMC configurations represent.
5. **Discuss the box inpainting result**: acknowledge and explain the 1.2 dB PSNR gap relative to DCDP.

---

## Evaluation on Key Axes

- **Originality**: The AC-DC denoiser design is novel; the convergence theory for score-based ADMM-PnP extends existing frameworks in a non-trivial way. High originality.
- **Importance**: Inverse problems with diffusion priors is an active and important area; principled convergence guarantees are practically and theoretically valuable.
- **Claims well-supported**: Empirical claims are broadly supported by Table 1, but the central novelty (DC benefit) lacks quantitative isolation, and the compute comparison is absent. The theoretical claims are sound but have a noted gap for the main experimental regime.
- **Soundness of experiments**: The multi-task, multi-dataset, multi-metric evaluation is well-designed, but the missing NFE data and qualitative-only ablation leave the most important questions unanswered.
- **Clarity of writing**: Generally clear, but notation in Section 3 around Eq. (9) and the unexplained PMC rows detract from reproducibility and readability.
- **Value to research community**: The combination of convergence theory and empirical breadth is valuable. The paper would be significantly more impactful with a quantitative DC ablation and NFE table.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>