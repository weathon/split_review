Now I have sufficient information to produce the consolidated review. Let me compile it.

---

## Summary

This paper proposes MolJO, a gradient-guided framework for structure-based molecule optimization (SBMO) built on Bayesian Flow Networks (BFNs). The key technical contributions are: (1) joint gradient guidance over both continuous atom coordinates and discrete atom types within a unified BFN framework, preserving SE(3)-equivariance; and (2) a backward correction sampling strategy with a sliding window that re-optimizes past latent aggregates. Evaluated on CrossDocked2020, MolJO reports a Success Rate of 51.3%, Vina Dock of -9.05, and SA of 0.78, outperforming prior gradient-based and oracle-based methods.

## Strengths

- **Joint gradient guidance over continuous and discrete modalities is well-motivated and technically sound.** Proposition 4.1 derives guided sampling kernels for both atom coordinates (via continuous μ) and atom types (via discrete y through a Gaussian latent construction), avoiding the problematic approximations used in prior discrete guidance (e.g., DiGress's Gaussian classifier assumption). The ablation in Figure 5 confirms that joint guidance consistently outperforms single-modality guidance, with coordinate guidance improving affinity and type guidance improving drug-likeness — directly supporting the paper's rationale for why TAGMol (coordinate-only) underperforms on holistic metrics.

- **Backward correction with sliding window is a novel and effective sampling strategy.** Algorithm 1 and Section 4.2 formalize a method that corrects past latent aggregates using information from the current guided step. Table 4 shows this strategy improves both unguided sampling (Vina Dock from -8.40 to -8.72) and guided sampling (from -8.83 to -9.05). The framing as a sliding window (k=1 → Graves et al.; k=n → Qu et al.) provides a clear unifying perspective, and Figure 2's gradient similarity analysis offers insight into the explore-exploit trade-off.

- **State-of-the-art quantitative results on a standard benchmark.** Table 1 reports MolJO achieving the best Vina Dock, SA, and Success Rate among all baselines including oracle-based (DecompOpt), generative (MolCRAFT, TargetDiff), and gradient-based (TAGMol) methods. The extension to constrained tasks (R-group optimization, scaffold hopping) in Table 3 further demonstrates practical applicability, with validity exceeding diffusion baselines by a wide margin in the challenging scaffold hopping setting.

- **SE(3)-equivariance is formally established.** Proposition 4.4 provides a clean theoretical condition under which the guided sampling process preserves SE(3)-equivariance, which is important for physically meaningful 3D molecular optimization.

## Weaknesses

### Fatal
None.

### Major

- **The 4× Success Rate improvement over TAGMol cannot be attributed to joint guidance alone, because the comparison conflates guidance design with backbone choice.** MolJO uses BFN as the generative backbone while TAGMol uses continuous-discrete diffusion. The critic's demand for a controlled experiment — running coordinate-only guidance on the BFN backbone and/or running joint guidance on a diffusion backbone — is justified. Without this isolation, the paper's headline claim (abstract: "more than 4x improvement in Success Rate compared to the gradient-based counterpart") implicitly attributes the gains to the guidance method, but the gains could substantially arise from the BFN backbone's stronger generative quality rather than from joint guidance. The paper does not run the critical ablation that would disentangle these factors. This weakens the central claim that "joint gradient guidance" is the cause of the improvement.

### Minor

- **Gradient guidance without backward correction yields little or no improvement (Table 4), which undercuts the "gradient guidance" framing.** The paper acknowledges this: "for vanilla case, the gradient guidance does not work as much probably due to the suboptimal history." However, the paper's title ("Unlocking the Power of Gradient Guidance") and narrative frame gradient guidance as the central contribution, when in practice the improvement is almost entirely dependent on the backward correction sampling strategy. The contribution is more precisely a *combined* guidance + corrected-sampling recipe that works for BFN, rather than a generalizable gradient-guidance framework. The paper would benefit from reframing to give backward correction co-equal billing.

- **"Me-Better" ratio is referenced in the abstract, Figure 1B, and the contributions list but never formally defined in the main text.** The reader must infer its meaning from context. A clear formulaic definition (what constitutes "me-better" — any improvement? improvement above a threshold? improvement on a composite metric?) should be provided in Section 5.1.

- **Main experimental results (Table 1) are reported as point estimates without error bars or significance tests.** For generative models where sampling variance across runs is expected, this is a notable omission. At minimum, results from 3 random seeds with standard deviations should be reported.

- **Energy function training details are missing.** The energy function \(E(\theta, \mathbf{p}, t)\) is central to the method — it replaces expensive oracle simulations — yet the paper does not specify its architecture, what property(s) it predicts, what data it is trained on, the loss function, or its predictive accuracy relative to the actual oracle. While these details may be deferred to a supplementary document (which the parser may have stripped), the main text should at minimum summarize the training setup and provide evidence that the proxy is sufficiently accurate to be a reliable substitute for oracle calls.

### Trivial

- **The BFN preliminaries (Section 3) are notation-heavy and assume prior familiarity.** The connection between \(\theta\), \(y\), and the output \(\hat{\mathbf{x}}\) is under-explained for readers not already versed in Graves et al. (2023).

- **No limitations or failure-case discussion is present.** The paper concludes without addressing sensitivity to the guidance scale \(s\) and window size \(k\), cost of training the energy function, or scenarios where gradient guidance degrades properties.

## Nice-to-Haves

- A systematic hyperparameter sweep showing how Success Rate varies with guidance scale \(s\) and window size \(k\).
- Scatter plot or bar chart of "Me-Better" ratios with error bars to quantitatively confirm the claimed 2× improvement over 3D baselines.
- Correlation plot of energy function predictions vs. actual oracle (e.g., Vina score) on a held-out set to validate the proxy's reliability.

## Removed Points

These points were flagged by reviewers but are removed or weakened per the meta-review rules:

- **"No controlled comparison with TAGMol under the same base model"** → Kept as Major (the analysis above found it valid and substantive).
- **"Training details of energy function entirely absent"** → Retained as Minor (plausibly deferred to appendix, but the main text should still summarize).
- **"First gradient-based SBMO framework claim too strong"** → Removed. The qualifier "facilitates joint guidance signals across different modalities" accurately distinguishes from TAGMol, which uses coordinate-only guidance. The claim is precise as written.
- **"Sliding window unifies prior sampling strategies — contribution is incremental"** → Removed as a weakness. Unifying existing strategies under a tunable hyperparameter is a legitimate contribution; the paper does not claim the sliding window is a fundamentally new concept unrelated to prior work.
- **"Guidance over θ vs. y connection (Remarks 4.2, 4.3) unconvincing"** → Removed. Remark 4.3's one-hot example is illustrative, not meant to be a rigorous proof of superiority.
- **Pure style/formatting nitpicks** → Removed.
- **Criticisms about missing appendix content** → Removed per meta-review guidelines (parser strips appendices from all papers).

## Novel Insights

The reviews surface a tension in the paper's framing that is worth the authors' attention: the paper is titled and motivated around "gradient guidance," but the ablation reveals that guidance alone (without backward correction) contributes negligible improvement. This suggests the paper's actual contribution is a specific sampling recipe (backward correction + joint guidance) that works for BFN, rather than a general gradient-guidance framework that could be ported to other architectures. Reframing the contribution around the combined sampling procedure — and explicitly testing whether the guidance component adds value even in the presence of backward correction (e.g., compare B.C. without guidance vs. B.C. with guidance) — would both strengthen the paper and clarify what is actually novel. Additionally, the controlled-backbone comparison with TAGMol is the single experiment that would most directly validate whether the joint-guidance design itself (as opposed to the BFN backbone or backward correction) is what drives the reported gains.

## Suggestions

1. **Run a controlled backbone comparison**: Apply coordinate-only guidance (TAGMol's strategy) on the same BFN backbone, and apply MolJO-style joint guidance on a diffusion backbone (e.g., TargetDiff). This isolates whether the 4× improvement is due to joint guidance or the BFN backbone.
2. **Reframe the contribution**: Give backward correction equal prominence in the title and narrative, since the ablation shows guidance alone is ineffective without it. Alternatively, add an ablation showing that backward correction *with guidance* outperforms backward correction *without guidance* — this would demonstrate that both components contribute.
3. **Formally define "Me-Better"** in Section 5.1 with a clear formula and report it with error bars.
4. **Add error bars or standard deviations** to the main results (Table 1, Table 3).
5. **Include energy function details** — minimum: architecture, training data, loss function, and a correlation plot of predicted vs. actual oracle scores on a held-out set.
6. **Add a limitations paragraph** discussing sensitivity to \(s\) and \(k\), the cost/accuracy of the energy proxy, and failure cases.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>