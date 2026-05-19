- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5
Now I have enough information to produce the consolidated review. Let me synthesize everything.

## Summary

This paper proposes Deep Restoration Priors (DRP), a method that extends the plug-and-play (PnP) framework from denoisers to general image restoration operators. DRP uses a pre-trained super-resolution SwinIR model as an implicit prior for solving inverse problems (deblurring and single-image super-resolution). The authors provide convergence theory (Theorems 1 and 2) under the assumption that the restoration operator is an MMSE estimator, and demonstrate competitive quantitative results against several denoiser-based baselines.

---

## Strengths

- **Genuine theoretical extension from denoisers to restoration operators.** Theorems 1 and 2 give fixed-point characterization and non-asymptotic convergence guarantees for DRP under a set of clearly stated assumptions. The theory allows nonsmooth data-fidelity terms and expansive restoration models, which is a notable generalization of existing denoiser-based PnP/RED theory (line 159: "major generalization of the existing theory"). This is verified in the paper's theoretical development (Sections 3–4).

- **Competitive quantitative results across most test configurations.** In the experiments (Tables 1 and 2), DRP achieves the highest PSNR in 23 of 24 test configurations across two inverse problems, four datasets, two blur kernels, and two super-resolution factors. For example, on Set3c deblurring (kernel 1.6), DRP (30.69 dB) outperforms the best denoiser-based method DPIR (29.53 dB) by 1.16 dB (line 192). On 2× SR with the same kernel, DRP (29.26 dB) beats DPIR (28.18 dB) by 1.08 dB (line 252). These margins are meaningful.

- **Prior-refinement strategy for adaptive use of restoration priors.** The paper demonstrates a practical schedule that gradually reduces the SR downsampling factor \(q\) during DRP iterations, yielding ~0.3 dB improvement over using a fixed \(q\) (Section 4.1, Figure 4). This is conceptually analogous to the denoiser sigma-schedule in DPIR and is a practically useful engineering contribution.

---

## Weaknesses

### Fatal
None.

### Major

1. **Directly related prior work (DPSR) not compared empirically.** The paper cites DPSR (Zhang et al. 2019) and RARE (Liu et al. 2020) as "the two most related methods that already use restoration operators instead of denoisers" (line 46) and distinguishes DRP by its statistical interpretation and theoretical analysis. Yet DPSR — a method specifically designed for super-resolution under arbitrary blur kernels using a pre-trained super-resolver — is not included as a baseline in any table. The paper's SISR experiments (Table 2) are the exact setting DPSR was designed for. Without this comparison, it is impossible to assess whether DRP's algorithmic framework provides meaningful practical improvement over this closely related approach, or whether the contribution is primarily theoretical. This weakens the experimental case for the paper's practical claims.

2. **Theory-practice gap: convergence theorem requires \(H^T H\) positive definite; experiments use rank-deficient bicubic downsampling.** Assumption 3 (line 146–147) requires \(\mu > 0\) in \(H^T H \succeq \mu I\). However, the bicubic downsampling operator \(H\) used throughout the experiments is rank-deficient (as is standard in SR), making \(H^T H\) positive semidefinite. The paper acknowledges the semidefinite case for the scaled proximal operator (line 82: "when \(H^T H\) is positive semidefinite, there might be multiple solutions") but does not reconcile this with the convergence theory's positive-definiteness requirement. Consequently, the convergence guarantees of Theorem 2 do not formally apply to the practical algorithm as run.

3. **Theory-practice gap: prior refinement strategy changes the operator during optimization, violating theory assumptions.** The convergence theory (Theorems 1 and 2) assumes a fixed restoration operator \(R\) (fixed \(H\) and \(\sigma\)). The prior refinement strategy (Section 4.1) progressively reduces the downsampling factor \(q\) of the SR prior, which changes \(H\) mid-optimization. The paper notes the analogy to DPIR's sigma-schedule (line 207) but provides no theoretical justification for why the convergence results remain valid when the prior is being varied. The theory and the practical algorithm operate under different premises.

4. **No ablation to separate architecture effect from restoration-operator effect.** DRP uses SwinIR (a large-capacity Transformer-based model) as the restoration operator, while baselines use DnCNN/DRUNet denoisers (smaller-capacity CNN-based models). If DRP outperforms the baselines, the gain could be attributable to SwinIR's more powerful architecture rather than to the use of a "restoration operator" per se. A controlled ablation — e.g., using a denoiser as the operator \(R\) (setting \(H = I\)) within the DRP framework — would isolate the contribution of the restoration-operator formulation. Without this, the paper's central claim that "restoration operators provide better priors than denoisers" is insufficiently supported by the evidence presented.

### Minor

1. **Step-size condition from theory is not verifiably satisfied in practice.** Theorem 2 requires \(\gamma = \mu/(\alpha L)\) with \(\alpha > 1\), where \(L\) is the Lipschitz constant of \(\nabla h\) and \(\mu\) is the minimum eigenvalue of \(H^T H\). Neither \(L\) nor \(\mu\) is estimated or bounded for the SwinIR instance used experimentally. The experiments tune \(\gamma\) and \(\tau\) freely on Set5 (line 216) rather than setting them according to the theorem's prescription. This further widens the theory-practice gap.

2. **The assumption that the trained network is exactly the MMSE estimator is unverified.** The theory assumes \(R\) is exactly the MMSE estimator of problem (2) (line 98–101). In practice, SwinIR is trained with MSE loss under varying noise levels, which approximates the conditional mean but is not guaranteed to be the exact MMSE estimator. The impact of this approximation error on the theoretical conclusions (fixed-point characterization, convergence) is not discussed.

3. **Evaluation scope is limited to two inverse problems with Gaussian blurs.** Experiments cover only deblurring and SISR, both with Gaussian blurs (std 1.6 and 2.0) and low noise (2.55/255). Testing on other tasks (e.g., inpainting, compressed sensing) or non-Gaussian degradations (motion blur, measured PSFs) would strengthen claims of generality.

### Trivial
None.

---

## Nice-to-Haves

- Include DPSR as a baseline. This is the most impactful addition to the experimental evaluation.
- Add an ablation using a denoiser as \(R\) (i.e., \(H = I\)) within the DRP framework to separate architecture effects.
- Report the specific values of \(\gamma\), \(\tau\), and the \(q\)-schedule used in experiments to aid reproducibility.
- Extend evaluation to at least one non-Gaussian degradation (e.g., motion blur) and one additional task (e.g., inpainting).

---

## Removed Points

These points were flagged in the reviews but are removed for the reasons stated below. Treat them with caution if encountered elsewhere.

1. **"Paper highlights DRP as best on CBSD68 kernel 2.0 deblurring, but DPIR beats it."** — FACTUALLY INCORRECT. The table (line 198) correctly shows DPIR in **bold** (27.52, best) and DRP underlined (27.46, second best). The paper's labeling is accurate. **Removed.**

2. **"CG iterations per step are not stated."** — FACTUALLY INCORRECT. Line 216 explicitly states "we run three steps of a CG solver." **Removed.**

3. **"DPS results not in the main tables."** — The appendix (which contained these results by the paper's own reference at line 170) was stripped by the PDF parser. Per the hard rules, missing appendix content is not a valid weakness. **Removed.**

4. **"No error bars or confidence intervals."** — PSNR evaluation on fixed test benchmarks with a fixed pre-trained network is deterministic; this is not standard practice in the image restoration literature. **Removed.**

5. **"No evaluation on real-world or non-Gaussian blurs."** — This demands the paper address problems outside its stated scope. The method is demonstrated on standard benchmarks; extending to other degradations is future work, not a flaw. **Removed.**

6. **"Convergence analysis should show objective \(f = g + h\) decrease."** — The regularizer \(h\) is implicit and defined through the MMSE operator; computing it directly is intractable. Showing iterate distance and PSNR convergence (Figure 2) is a reasonable proxy. **Removed.**

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not synthesize any observation about the paper that is not already stated in the paper itself — the theory-practice gaps and missing DPSR comparison are standard reviewer observations, not novel insights.

---

## Suggestions

1. **Add DPSR as a baseline** in the SISR experiments (Table 2) to contextualize DRP against the most directly related prior work that also uses a restoration operator.

2. **Address the \(H^T H\) positive-definiteness issue** either by modifying the theory to handle the semidefinite case (e.g., by adding a damping term or restricting to subspaces where \(H\) is injective) or by explicitly stating that Theorem 2 applies to the restricted setting where the iterate subspace avoids the nullspace of \(H\).

3. **Provide a theoretical discussion** (or at minimum an empirical justification) for why the prior-refinement strategy does not break convergence — e.g., by showing that each phase with fixed \(q\) converges, and that switching acts as a warm-start.

4. **Run a controlled ablation** where DRP uses a denoiser as the operator \(R\) (\(H = I\)) to separate the effect of the restoration-operator formulation from the effect of the SwinIR architecture.

---
