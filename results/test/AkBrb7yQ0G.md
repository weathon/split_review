Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper proposes TGDMat, a text-guided joint diffusion model for 3D periodic crystal generation. It is the first work to condition crystal structure generation (atom types, coordinates, lattice) on natural language descriptions, using a periodic-E(3)-equivariant GNN denoising network fused with a frozen MatSciBERT text encoder. The paper shows (1) that text guidance improves existing SOTA unconditional models (CDVAE, SyMat, DiffCSP) across both Gen and CSP tasks, and (2) that TGDMat's joint diffusion framework outperforms text-guided variants of those baselines.

## Strengths

- **First text-guided diffusion framework for periodic materials.** The paper genuinely opens a new direction by bridging natural language understanding with crystal structure generation. This claim is clearly supported by the experimental setup and the paper's positioning.

- **Joint diffusion over lattice, coordinates, and atom types is a meaningful architectural contribution.** Unlike prior work (DiffCSP treats atom types as given; CDVAE/SyMat use separate VAE + score network), TGDMat diffuses all three components in a single end-to-end equivariant framework. Table 4 shows that TGDMat (both Long and Short prompt variants) achieves superior or competitive results on the Gen task, especially on Perov-5 and MP-20 where it outperforms all text-guided baselines across all metrics.

- **Text guidance consistently and substantially improves baselines.** Tables 2 and 3 provide extensive evidence on three datasets that *every* text-guided variant (CDVAE+, SyMat+, DiffCSP+) outperforms its unconditional counterpart across all metrics. For the CSP task, text guidance raises the k=1 match rate dramatically (e.g., DiffCSP+ 62.48% vs. DiffCSP 40.97% on MP-20). This demonstrates that the text-conditioning idea is robust and model-agnostic, not a quirk of the proposed architecture.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaiming about "real-world custom text prompts by experts" — not tested.** The abstract, contribution list, and conclusion all claim that TGDMat "demonstrates rich generative capability under general textual conditions" when "applied to real-world custom text prompts by experts." But every experiment conditions on text that was *derived from the same crystal structure it is evaluated against* — either long Robocrystallographer descriptions or template prompts encoding the ground-truth formula, space group, and crystal system. The correctness check in Section 5.4 (Table 5) measures whether generated materials match properties stated *in the prompt they were conditioned on*, which is essentially a reconstruction/consistency test. There is no experiment where the model is given a novel textual description (e.g., "a perovskite with band gap > 2 eV and negative formation energy") that does not correspond to an existing training-set structure, and then evaluated on whether it generates a material satisfying those properties. The claimed real-world utility is therefore unsubstantiated, and this is a central gap because the paper's main motivation is that "users specify the desired characteristics."

2. **Computational cost comparison is misleading — compares against *unconditional* baselines.** Section 5.5 claims that text guidance reduces training/sampling overhead, but the comparison is TGDMat (text-conditioned) against *unconditional* CDVAE and DiffCSP. Conditioning on text provides direct information about the target structure, so faster convergence is expected — this is not a fair test of TGDMat's efficiency advantage. The paper never reports how many training epochs or sampling steps the text-conditioned baselines (CDVAE+, DiffCSP+) would require. Figure 3 plots match rate vs. GPU hours only for TGDMat variants, DiffCSP, and CDVAE, not for the text-conditioned baselines. The claimed efficiency advantage could simply be due to conditioning itself, not the proposed architecture.

3. **Joint diffusion advantage is confounded with the switch to discrete diffusion (D3PM).** TGDMat uses discrete diffusion (D3PM with absorbing state) for atom types, while baselines CDVAE, SyMat, and DiffCSP use continuous DDPM on atom-type probabilities. The paper explicitly acknowledges this (Section 3: "we enhance DiffCSP by integrating discrete diffusion over atom types in our proposed TGDMat") but then attributes TGDMat's gains to "joint diffusion" and "text guidance" without isolating the effect of the discrete diffusion choice. The D3PM paper (Austin et al., 2021) already shows that discrete diffusion is more appropriate for categorical data — so some of TGDMat's improvement could stem from this design choice alone, independent of both text guidance and the joint framework. An ablation replacing D3PM with continuous DDPM (or vice versa on baselines) is needed to attribute the gains to joint diffusion specifically.

### Minor

4. **Construction of text-guided baselines is insufficiently described.** The paper states that CDVAE+, SyMat+, and DiffCSP+ were built by "fus[ing] the contextual representation of (long detailed) text data into denoising network of those models using our proposed algorithm as described in 4.3.2." But Section 4.3.2 describes TGDMat's specific architecture (CSPNet-based periodic-E(3)-equivariant GNN with text injected into input atom features). CDVAE and SyMat have quite different architectures (VAE encoder + score network with separate decoders for lattice/atom types), so it is unclear how text was fused into each. The paper does not specify whether these variants were trained from scratch or fine-tuned, or what hyperparameters/schedulers were used. While the high-level idea is reasonable, the lack of detail makes it difficult to assess fairness of the main comparisons in Tables 2, 3, and 4.

5. **No uncertainty quantification.** All results in Tables 2–5 report single numbers with no error bars, and no mention of multiple independent runs. For a paper claiming to "surpass" baselines, the reader cannot tell whether margins are within noise. This is partially a field-convention issue, but given the stochastic nature of diffusion sampling, error bars would substantially strengthen confidence in the results.

### Trivial
None.

## Nice-to-Haves

- **Ablation: TGDMat without text conditioning (but still joint diffusion).** This would isolate the improvement from text guidance vs. the joint diffusion framework itself.
- **Ablation: TGDMat with continuous DDPM on atom types** (instead of D3PM) to measure the specific benefit of discrete diffusion.
- **Nearest-neighbor analysis** between generated and training-set structures to check for memorization (a genuine concern when prompts are derived from training structures).
- **Property-distribution analysis** to verify that text-conditioned generations actually align with the properties specified in the prompts (e.g., if prompt says "formation energy negative," does the model generate structures with negative formation energy more often?).
- **Fair computational comparison** against text-conditioned baselines (CDVAE+, DiffCSP+) to validate the efficiency claim.
- **Limitations section** discussing when text guidance might fail (vague/contradictory prompts, reliance on Robocrystallographer's accuracy).

## Removed Points

- **"Visualizations (Table ??) are not present"** — This is a parser artifact. The original submission contains these in the appendix. (Hard Rule: remove weaknesses about missing appendix content.)
- **"The paper does not discuss memorization"** — Moved to Nice-to-Haves as this is a reasonable suggestion but not a core flaw.
- **Weakness about lack of limitations section** — Moved to Nice-to-Haves, as this is standard good practice but not a structural flaw.
- **The "no error bars" criticism** — Downward-adjusted from Major to Minor because single-run reporting is standard practice in the crystal generation literature (CDVAE, DiffCSP, SyMat all report single numbers), but still worth noting.

## Novel Insights

The reviews reveal a tension between the paper's genuine novelty (first text-guided crystal generation, strong empirical improvements) and its overclaiming on two fronts: (1) the real-world custom-prompt claim is untested, and (2) the computational efficiency and joint-diffusion attributions are not cleanly separated from simpler explanations (conditioning itself, discrete diffusion). The paper's most robust finding — that text conditioning boosts unconditional models across the board — is well-supported, but the more specific claims about the proposed architecture require additional ablations and fairer baselines. This pattern (novel framing + strong but confounded experiments + overstated conclusions) is common in emerging application areas and suggests the paper needs tightening rather than fundamental rethinking.

## Suggestions

1. **Add a held-out novel-prompt experiment.** Generate textual descriptions that do not correspond to any training-set material (e.g., specifying only a space group, crystal system, and property ranges) and evaluate whether generated structures satisfy those constraints via property prediction or DFT relaxation. This directly validates the "real-world custom prompt" claim.
2. **Run ablations to disentangle contributions.** (a) TGDMat without text conditioning (joint diffusion only) vs. with text conditioning. (b) TGDMat with continuous DDPM on atom types (replacing D3PM).
3. **Report computational cost of text-conditioned baselines** (CDVAE+, DiffCSP+) alongside TGDMat, using the same step counts, to make the efficiency comparison fair.
4. **Report means and standard deviations over at least three random seeds** for all main results.
5. **Provide more detail** on how text conditioning was fused into each baseline architecture (CDVAE+, SyMat+, DiffCSP+), ideally in an appendix.

## Score and Decision

The paper makes a genuine contribution — it is the first to explore text-guided diffusion for crystal generation, and the core finding that text conditioning improves unconditional models is empirically solid. However, the paper overstates its claims in several ways that cannot be resolved by simple clarifications: the "real-world custom prompts" claim is untested, the computational efficiency comparison is unfair, and the joint-diffusion contribution is confounded. These are structural experimental gaps, not presentation issues.

**Score:** 5.0

**Decision:** Reject

The paper has real promise and a clear direction for improvement. With proper ablations, a real novel-prompt experiment, and fairer baselines, it could become a strong paper. In its current form, the evidence does not fully support the claimed contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>