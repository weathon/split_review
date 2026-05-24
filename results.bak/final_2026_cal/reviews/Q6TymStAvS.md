Now let me write the final consolidated review.

## Summary

This paper introduces ShadowFM, a framework that applies geometric flow matching to generate classical shadows conditioned on Hamiltonian parameters. Two methods are proposed: (1) **Spherical Flow**, which embeds shadows on the 2-sphere (via the Bloch sphere mapping) and applies Riemannian Flow Matching, and (2) **Anisotropic Dirichlet Flow**, a generalization of discrete flow matching that introduces a target-anti-target pairing mechanism reflecting the (X⁺,X⁻), (Y⁺,Y⁻), (Z⁺,Z⁻) structure of Pauli-6 shadows. The core insight—that respecting the Bloch sphere geometry of shadows improves generative modeling—is supported by a clean toy experiment showing spin errors (across the sphere) are far more harmful than basis errors (within the sphere). Across extensive evaluations on TFIM, Heisenberg (1D & 2D), and time dynamics, the geometric methods consistently outperform non-geometric flow matching baselines, often by substantial margins.

## Strengths

- **Principled incorporation of Bloch sphere geometry into generative modeling for shadows.** The paper provides a clear theoretical motivation (the Fubini–Study metric on ℂℙ¹ is isometric to the round metric on S²) and translates this into two well-specified generative frameworks. The toy experiment (Figure 2) concretely demonstrates that spin errors are more detrimental than basis errors for observable estimation, justifying the geometric design choices. No prior work on generative models for shadows has used this geometric structure.

- **Consistent and often large empirical gains over non-geometric flow matching baselines.** Across all settings — TFIM L=10/30, Heisenberg 1D/2D, time evolution, tetrahedral POVM — at least one of the two proposed methods achieves the lowest RMSE among generative models. The gains are substantial in many cases: on TFIM L=10 (Table 1) at 100k inferred shadows, AD achieves correlation RMSE 0.021 vs. the best prior generative model (StatisticalFM) at 0.126—roughly a 6× improvement. On Heisenberg L=10 (Table 3), Spherical Flow at 100k gives correlation RMSE 0.042 vs. StatisticalFM at 0.054. These improvements are not marginal but systematically observed across system sizes, observable types, and Hamiltonians.

- **Clean demonstration of scaling with training data.** Section 4.4 (Figure 5c) shows that ShadowFM methods scale nearly monotonically with training sample size, matching the slope of the exact CS oracle, while baselines plateau. This indicates the geometric inductive bias reduces model bias effectively.

- **Generality to multiple measurement protocols and system sizes.** Experiments cover 1D chains (L=10, L=30), 2D systems (4×4), time dynamics extrapolation, and tetrahedral POVM shadows (Table 7), showing the geometric principles are not tied to Pauli-6 POVM specifically.

## Weaknesses

### Major

- **Anisotropic Dirichlet flow underperforms severely on dynamics entropy estimation, without discussion.** In Table 5 (time evolution extrapolation), AD achieves a competitive correlation RMSE of 0.099 (best among generative methods at 1k) but a catastrophic entropy RMSE of 0.389—roughly 2× worse than the next-worst baseline (0.224) and ~6× worse than Spherical Flow (0.195). The paper does not discuss this failure or hypothesize why the anti-target repulsion mechanism harms entropy estimation specifically. Since AD is presented as a general-purpose method, this inconsistency weakens the claim of broad applicability and requires either an explanation, a modification, or a clear delineation of regimes where each variant is appropriate.

- **Unclear whether the main experiments evaluate generalization to unseen Hamiltonians or interpolation.** The paper states in the abstract and introduction that the method can "infer the ground state of both seen and unseen Hamiltonians" and the experiments report RMSE "averaged over a test set of 100 ground states." However, the paper does not specify whether these test Hamiltonians use coupling constants not seen during training (true generalization) or are a held-out subset drawn from the same parameter grid (interpolation). Section 4.4 explicitly refers to "seen Hamiltonians" in one experiment, but the main TFIM/Heisenberg experiments (Tables 1–4) do not state this split. The strength of the reported results cannot be properly assessed without knowing whether they reflect extrapolation to genuinely new parameter regimes. (The appendix may contain these details, but they are not in the main text and are stripped.)

### Minor

- **No autoregressive baseline, though the motivation cites autoregressive limitations.** The paper's introduction identifies "sequential bottlenecks of auto-regressiveness" as a limitation of prior work. While the core contribution is geometric, the framing implicitly promises a comparison point. The authors acknowledge this gap in the conclusion, but including one autoregressive baseline (e.g., from Yao & You 2024) would directly substantiate the claimed advantage over non-geometric autoregressive methods and is the single most impactful experiment the authors could add.

- **Experimental details deferred to stripped appendix.** The number of training Hamiltonians, how coupling constants are sampled (grid vs. random), network architectures, and training hyperparameters are referenced as in Sections C and D (presumably in the appendix), which is not available in the parser output. These are standard details needed for reproducibility. (This is noted as a weakness only to the extent that these details should be in the main text or a reliably available appendix.)

- **Kernel baselines solve a different task than generative baselines.** RBFK and NTK are regressors that predict observables directly from Hamiltonian parameters, not generative models that learn shadow distributions. The paper is transparent about this (the table separates "Classical" from "CFM"/"CS-DFM" categories), but the comparison is asymmetric: RBFK on L=10 TFIM achieves correlation RMSE 0.028 (close to CS's 0.027 at 10k), lower than any generative method. The paper does not discuss what conclusions should be drawn from this comparison. A brief discussion of when direct regression is preferable vs. when generative modeling adds value would strengthen the evaluation.

### Trivial

- The y-axis in Figure 2 is labeled "Relative Error (%)" but the text says the metric is "RMSE of XX and ZZ correlation" — it is unclear whether "relative" refers to percentage of the true value or some normalization. A clarifying note in the caption would help.

## Nice-to-Haves

- Ablate the anisotropic parameter γ for AD flow more explicitly. The paper mentions evaluating γ ∈ {0, 0.05, 0.1} and reporting the best, but a dedicated table would clarify sensitivity.
- For the phase transition plots (Figure 5a,b), a quantitative measure (e.g., error in critical point location) would complement the qualitative visual comparison.
- Report approximate training/inference times, especially given the pre-computation overhead acknowledged for AD flow.
- Visualize generated shadow distributions (e.g., histogram of outcomes for a given Hamiltonian) to qualitatively show what the model learns beyond RMSE-aggregated metrics.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing comparison to autoregressive baselines is a decisive gap that invalidates core claims."** — The paper's core claim is that respecting geometry improves shadow generation. This is tested against non-geometric FM baselines. The autoregressive mention is motivational context, not a central claim that undermines the paper if untested. The authors also acknowledge this limitation in the conclusion. Demoted from "decisive" to Minor.
- **"Baseline comparison fairness for kernel methods — the kernel rows are a distraction."** — The paper clearly separates kernel baselines in a different category ("Classical" vs generative), and the comparison is informative even if asymmetric. The asymmetry favors the baselines, not the proposed method. Removed per the rule about asymmetry favoring baselines.
- **Criticisms about missing appendix content, missing proofs in appendix, or absent references.** — These are parser artifacts; the appendix exists in the original submission.
- **"Toy experiment effect sizes not reported numerically"** — The figure provides relative error values visually; this is standard practice for figures.
- **"Domain and codomain dimensions of the pushforward map π are not explicitly stated"** — The paper states "C³ ≡ {x ∈ ℝ³ | ‖x‖₁ = 1}" and "S² is the unit sphere in ℝ³", making the dimensions clear.

## Novel Insights

The paper's key insight—that the Bloch sphere geometry can be leveraged to design better generative models for classical shadows—is genuinely novel and well-motivated. Beyond the empirical results, the anisotropic Dirichlet flow formulation (Equation 6) is a nontrivial generalization that introduces a mathematically principled way to encode the (target, anti-target) structure of shadows through a pull-away term in the probability path. This framework extends beyond quantum shadows to any discrete data with paired oppositional structure. The finding that geometric approaches can match the exact CS scaling behavior with training data (Figure 5c) while baselines plateau is also notable and suggests the geometric inductive bias fundamentally reduces sample complexity.

## Suggestions

1. **Add one autoregressive baseline** (e.g., a transformer-based shadow generator following Yao & You 2024) for at least one setting (e.g., TFIM L=10). Even if the baseline is competitive or better, the comparison would clarify where geometric FM stands relative to the broader state of the art.
2. **Explicitly state the train/test split of coupling constants** for every experiment — whether c values are held out or interpolated — and ideally add an explicit out-of-distribution test (e.g., train on c ∈ [0, 0.6], test on c ∈ [0.6, 1.0]).
3. **Analyze the AD failure on dynamics entropy.** This is the single most important missing analysis. Show whether tuning γ per task, adjusting the pairing structure, or using a different inference strategy resolves the issue. If not, clearly delineate the regimes where each method is recommended.
4. **Include the key experimental details** (number of training Hamiltonians, coupling constant sampling strategy, architecture details) in the main text, not solely the appendix.
5. **Improve Figure 2 caption** to clarify the metric used on the y-axis.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak anchors (<3.5): mq1kHw6IUX (2.67, Lie group flow matching, reject); nnRB90w2kv (2.50, PDE flow matching, reject); lZfaGbAAGe (2.00, fermionic MCMC, reject); 9E0ioSxB7s (2.50, quantum neural networks, reject). These papers have fundamental experimental or methodological flaws that ShadowFM does not share.
- Middle anchors (3.5–7.5): a1MteiJJ6g (4.00, GenKSR, reject — generative models underperform CS baseline); wJTD7wQh40 (4.80, quantum generative modeling, reject); x79tGDQd7Z (4.00, quantum GANs, reject); DbimAFDxZA (5.50, IQP-QCBM, reject — strong theory, limited experiments). ShadowFM is stronger than GenKSR (where the AI methods underperformed baselines) and roughly comparable to the IQP-QCBM paper (5.5) in overall quality, with stronger experiments but weaker theory.
- Strong anchors (>7.5): VaS6xcDrTb (8.50, rotation estimation); DTQIjngDta (8.00, permutation-equivariant geometry); RDerF20JYT (8.00, protein generation); kI27Niy4xY (8.00, text-to-3D). These papers have tighter, more complete evaluations and cleaner contributions than ShadowFM.

**Round 1 bracket:** [5.0, 6.5]

**Round 2 — Narrowing:**
- Flow matching discrete data (4.5–6.5): 4EGjzT6w80 (5.00, SD-FM, accept poster — limited benchmarks but solid contribution); awEvtKliMC (6.00, PairFlow, accept poster — clean theory, broad experiments); p56ZAQUCUr (5.50, SGFM, accept poster); eoEmoKoQpJ (6.00, flow matching policy gradients, accept poster).
- Classical shadow / ML quantum estimation (5.0–7.0): on2lie43Kl (6.00, quantum ML advantages, accept poster); 0zIcPe4CtY (5.50, quantum attention, accept poster); cS0L2kj0lj (6.00, Bayesian VQE, accept poster); QcRto0GjxC (5.50, quantum neural nets, accept poster).

ShadowFM's experimental breadth (5 Hamiltonians × 2 system sizes × multiple tasks + POVM variants) exceeds SD-FM (5.00, limited to two small benchmarks). ShadowFM's empirical evidence is stronger than the IQP-QCBM paper (5.50, limited to synthetic parity-check data). However, ShadowFM's theoretical contribution is less clean than PairFlow (6.00), which had closed-form derivations validated across molecular and image domains. ShadowFM's AD-failure-on-dynamics issue is an unexplained anomaly that PairFlow and SD-FM do not have.

**Final score:** 5.5. This reflects a paper with genuine contributions (geometric flow matching for shadows, strong empirical evidence in most settings, broad evaluation) that is held back by (a) an undiscussed failure mode of the AD method on dynamics, (b) unclear generalization setup for the main experiments, and (c) the absence of an autoregressive baseline when the motivation mentions autoregressive limitations. The paper is publishable after addressing these concerns but needs the missing analysis and clarifications.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>