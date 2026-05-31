Now let me perform the calibration searches to anchor the score.Let me read the most relevant anchors before narrowing.Round 1 bracket: **6.0 – 8.0**. C-CLIP (a direct baseline that PI-CCA outperforms) scored 6.5. The strong-band papers at 8.0 are on different CLIP-analysis topics. Let me narrow within 6–8.I have sufficient calibration data. Now I'll write the final consolidated review.

---

## Summary

PI-CCA (Prompt-Invariant CCA Certificates) recasts catastrophic forgetting in vision-language continual learning as *alignment-geometry drift* rather than proxy-level mismatch. The method preserves the top-*k* canonical correlations and subspaces of the whitened image-text cross-covariance via a compact, replay-free certificate; prompt robustness is induced by averaging projectors over perturbations. Across four benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), PI-CCA sets a new replay-free state of the art, outperforming recent methods and even a synthetic-replay competitor (GIFT) on retrieval and structured-concept tasks.

---

## Strengths

- **Consistent SOTA across all four benchmarks.** PI-CCA achieves the best replay-free results on MTIL (76.8 vs. 75.2 C-CLIP Avg), X-TAIL (68.1 vs. 67.4 RAIL Avg), VLCL (I2T R@1 48.6 ± 1.0 vs. 47.3 ± 1.2 GIFT†), and ConStruct-VL (FA 75.2 ± 1.3, AF 2.7 ± 0.2). Crucially, it surpasses GIFT, which employs a diffusion-based generative pipeline, while being fully replay-free—a meaningful result given the resource asymmetry (Tables 1–2).

- **Both geometric components shown to be necessary.** The ablation (Table 3) demonstrates that removing either the spectral term (λ₁=0, −2.5 pp MTIL Avg) or the subspace-angle term (λ₂=0, −2.2 pp) causes the largest individual drops across all benchmarks, directly supporting the claim that both the canonical spectrum and subspace directions must be preserved. The ablation also isolates the relative importance of streaming covariance EMA vs. certificate EMA, and explores sketch type and pairing scheme variants, providing unusually thorough component coverage.

- **Prompt-invariance component validated under stress.** Figure 4 shows that ℒ_pi flattens the performance decay curve as perturbation strength *s* increases: at *s* = 1.0, R@1 improves by +2.44 pp (ID) / +2.51 pp (OOD) vs. no ℒ_pi, with ≈1 pp lower Average Forgetting, confirming the projector-averaging mechanism adds genuine robustness beyond what the base alignment losses achieve.

- **Task-order robustness rigorously evaluated.** Figure 5 sweeps 20 independent MTIL orderings; the IQR on Avg accuracy spans ≈76.0–77.4%, and Last accuracy likewise stays narrow, demonstrating that the gains are not an artifact of a favorable task sequence. This analysis is often omitted in competing papers and adds meaningful credibility to the reported numbers.

- **Efficient Pareto frontier.** The (k=64, h=256) certificate sits near the knee of the performance-vs-memory curve (Figure 2), confirming that the "small yet sufficient" certificate hypothesis holds across a wide grid of capacity settings.

---

## Weaknesses

### Fatal
None.

### Major

- **The geometry→performance correlation analysis (Fig. 3) is self-referential.** The paper presents Pearson r=1.00 / Spearman ρ=1.00 correlations between geometry drift and performance drop as evidence that "preserving CCA geometry predicts retention rather than being a coincidental regularizer." However, per §4.3, the sweep that generates these scatter plots varies hyperparameters of PI-CCA itself (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type). Because PI-CCA's training objectives (ℒ_spec, ℒ_sub) *directly minimize* D_ang and D_ρ, configurations where the regularization operates more weakly will simultaneously exhibit larger geometry drift and lower performance—both as downstream consequences of the same underlying cause (weaker regularization). The near-perfect correlation is therefore a property of PI-CCA's own hyperparameter landscape, not an independent empirical law. To validate the causal claim, the paper would need to measure geometry drift across diverse *methods* (e.g., ZSCL, C-CLIP, Mod-X) under the same protocol and show that methods achieving lower drift also achieve higher performance regardless of their mechanism. As currently framed, Fig. 3 constitutes internal consistency evidence, which is weaker than the causal framing in the paper implies. This does not undermine the method's empirical gains, but the theoretical narrative overstates what the evidence demonstrates.

### Minor

- **Missing statistical uncertainty for MTIL and X-TAIL classification results (Tables 1).** VLCL and ConStruct-VL results include ±s.d. (Table 2), but the classification tracks report single numbers. Some margins over competitors are small (e.g., 0.7 pp over RAIL on X-TAIL Avg). Variance estimates or multi-seed ranges would allow proper comparison.

- **Memory cost of streaming covariance EMAs not surfaced in efficiency analysis.** For CLIP ViT-L/14 (d_v = d_t = 768), the three streaming covariance matrices (Σ_vv, Σ_tt, Σ_vt) together represent ≈ 14M float32 values (≈56 MB), which exceeds the footprint of the compact sketch certificate itself. The Pareto plot (Fig. 2) correctly reports peak memory in GB but does not distinguish certificate cost from covariance EMA cost. The "constant-memory" framing is accurate (memory does not grow with tasks), but acknowledging this dominant contributor would clarify the true memory profile for practitioners.

- **Prompt invariance stress test covers template variation, not genuine style shifts.** The abstract claims "resilience to prompt/style shifts," but the stress test in §4.3 uses token-level synonym swaps, back-translation, and template jitter—all within a narrow template style. Style shifts (e.g., medical captions vs. web captions, VQA-style descriptions vs. retrieval captions for the same images) are substantially harder and more application-relevant. The current stress test validates robustness to phrasing variation but not to distributional style variation. The abstract claim should be narrowed, or a single held-out domain with genuinely different language style should be added.

### Trivial

- The reproducibility note states that code cannot be released during review due to ongoing commercial use. This is a limitation for reviewers attempting to verify the multi-component implementation (differentiable SVD via block power iteration, EMA stop-gradients, sketch normalization), though it does not affect the validity of the reported results.

---

## Nice-to-Haves

- Measuring geometry drift (D_ang, D_ρ) on the *baselines* (ZSCL, C-CLIP, Mod-X) using the same protocol and plotting their (drift, performance) pairs on Figure 3 would transform the correlation analysis from an internal consistency check into genuine cross-method evidence for the geometry-prediction hypothesis. This requires only inference passes on saved checkpoints and would significantly strengthen the paper's theoretical narrative.

- A small-scale demonstration involving genuine style variation—e.g., CLIP-style captions vs. medical image reports, or web descriptions vs. VQA annotations for the same images—would substantiate the "style shifts" claim in the abstract more convincingly than the synonym-swap stress test.

- Statistical significance (multi-seed results) for MTIL and X-TAIL would make the classification comparison tables on par with the retrieval/structured-concept tables.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's "no baseline comparison for geometric framing"**: While the critic suggests comparing CCA-based certificates to e.g. CKA drift minimization, the paper's contribution is specifically the CCA certificate design, and the ablation already isolates both spectral and subspace terms. Demanding a different geometric alternative is scope creep; the method works and the components are validated. Moved to nice-to-have territory.

- **Harsh critic's distillation-vs-CCA distinction being overstated**: Critic notes that CTP and Mod-X are "related to" the cross-modal alignment geometry and the distinction is "a matter of degree, not kind." This is a nuanced framing point, not a substantive weakness. The paper's claim is that CCA directly preserves invariants of the *whitened* cross-covariance, whereas prior methods act on similarity distributions or logits—this distinction is genuine even if partial.

- **Harsh critic's concern about GIFT's additional access implying unfair comparison**: The critic notes that "the fair comparison here should clarify whether GIFT's diffusion pipeline adds parameters or access to out-of-distribution generated data." PI-CCA *outperforms* GIFT while being more constrained (replay-free). A comparison that favors the baseline does not constitute an unfair baseline; per the hard rules, this criticism is removed.

- **Strength Finder's claim of "geometry-performance correlation further shows strong positive linear relationships"**: This strength was downgraded because the harsh critic's major weakness (tautological correlation) is verified. The correlation is real but self-referential; it is not an independent validation of the CCA framing as a standalone strength.

---

## Novel Insights

The most genuine methodological insight in PI-CCA is the projector-averaging mechanism for prompt invariance: by constructing the certificate text basis as the top eigenvectors of the *mean* sketched projector across perturbations (Eq. 5–6), the method eliminates sign and rotation ambiguity in the canonical text subspace without requiring Procrustes alignment. This is a clean, practically motivated design that simultaneously addresses a longstanding brittleness in CLIP-based continual learning (prompt sensitivity) and makes the certificate compact and rotation-free. The observation that averaging projectors—not directions—achieves this is non-obvious and applicable beyond the specific PI-CCA setting.

---

## Suggestions

1. **Reframe or replace Fig. 3**: Either add geometry-drift measurements from baselines (ZSCL, C-CLIP, Mod-X) on the same scatter plots, or explicitly present Fig. 3 as "ablation consistency evidence" rather than "causal prediction of performance by geometry drift." The current Pearson r=1.00 framing will draw skepticism from readers who notice the data come exclusively from PI-CCA hyperparameter variants.

2. **Add multi-seed variance to Table 1** (MTIL, X-TAIL), or at minimum report the range across 3 seeds, to make the classification results comparable in rigor to Table 2.

3. **Separate memory accounting in Fig. 2**: Add a breakdown distinguishing (a) covariance EMA memory, (b) certificate memory, and (c) LoRA adapter memory in the efficiency analysis.

4. **Temper abstract language**: Replace "resilience to style shifts" with "resilience to prompt/phrasing variation" unless a genuine style-shift experiment is included.

---

## Score and Decision

**Calibration summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| sb7qHFYwBc (C-CLIP) | 6.50 | R1 | Direct baseline PI-CCA outperforms; PI-CCA is more principled and covers 4 benchmarks vs. fewer |
| Hcb2cgPbMg (Spectral CL) | 6.25 | R2 | Spectral regularization for CL but unimodal; less comprehensive than PI-CCA |
| Ll8PmgD0IB (Divide & Orthogonalize) | 6.00 | R2 | Gradient-projection CL; weaker contribution and evaluation |
| DJZDgMOLXQ (PEC) | 6.50 | R2 | Class-incremental learning; less direct topic |
| b20VK2GnSs (MLLM Concept Drift) | 7.00 | R2 | VL continual adaptation with comprehensive experiments; received 7.0 despite noted comparison fairness issues |
| X1OfiRYCLn (VLB) | 7.50 | R2 | Strong VL evaluation paper; different problem but similar comprehensiveness |

**Round 1 bracket: 6.0–8.0.**

**Round 2 narrowing:** PI-CCA is clearly better than C-CLIP (6.5)—it introduces a more principled geometric framework, evaluates on 4 benchmarks (vs. fewer for C-CLIP), and outperforms all competitors including a generative-replay method. The concept-drift MLLM paper (7.0) has more fundamental weaknesses (unfair comparison baselines, missing module evaluations) yet scored 7.0. PI-CCA's main weakness—the tautological geometry→performance correlation—is real and should be fixed, but does not invalidate the empirical contribution. Combined with the missing statistical uncertainty on classification tables and the slightly overstated abstract claims, the paper sits firmly above 6.5 but below 7.5. The paper is **comparable to the 7.0 anchor** (b20VK2GnSs) in overall contribution, with a cleaner methodology but a weaker theoretical validation component.

**Final score: 7.0 — Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>