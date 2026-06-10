## Summary

This paper introduces FoldFlow, a family of three flow-matching generative models over SE(3) for protein backbone generation: FoldFlow-Base (deterministic CFM), FoldFlow-OT (accelerated via Riemannian optimal transport), and FoldFlow-SFM (stochastic flow matching). The key technical contributions include a closed-form conditional vector field for SO(3) that avoids autograd, a proof of Monge map existence on the translation-invariant subgroup SE(3)⁰_N enabling Riemannian OT, and a simulation-free SDE formulation on SE(3). Empirically, FoldFlow-OT achieves 0.820 designability (vs. 0.612 for retrained FrameDiff) and FoldFlow-SFM approaches RFDiffusion-level novelty at 1/180th the compute.

---

## Strengths

- **Closed-form conditional vector field for SO(3) avoiding autograd (Eq. 4, §3.1 lines 184–199).** The paper derives $u_t(r_t|r_0,r_1) = \log_{r_t}(r_0)/t$ using an axis-angle trick and parallel transport, circumventing expensive matrix logarithm approximations and autograd differentiation. This is a concrete implementation improvement over prior Riemannian CFM (Chen et al., 2023) that directly increases training speed and numerical stability, as reflected in the 2× iteration speed over FrameDiff (Table 1).

- **Riemannian OT with proven Monge map on SE(3)⁰_N (Proposition 1, §3.2 lines 216–221).** The paper proves existence and uniqueness of a Monge map on the translation-invariant subgroup, establishing $\Psi(x) = \exp_x(\nabla\phi(x))$. This theoretical grounding enables FoldFlow-OT to construct straighter conditional probability paths via optimal transport — a capability absent in prior diffusion-based backbone models (RFDiffusion, FrameDiff, Genie) and in previous Riemannian FM work.

- **Strong designability gains over non-pretrained baselines (Table 1, lines 327–343).** FoldFlow-OT achieves 0.820 designability fraction vs. FrameDiff-Improved (0.555) and FrameDiff-Retrained (0.612). The gap is large and supported by reported standard errors. All three FoldFlow variants outperform all FrameDiff variants on designability.

- **FoldFlow-SFM achieves competitive novelty vs. RFDiffusion at dramatically lower cost (Table 1, line 342, line 354).** SFM achieves novelty fraction 0.544 (avg. max TM-score 0.411) vs. RFDiffusion's 0.708 (0.449), while using ~10 vs. 1800 GPU days and 17M vs. 60M parameters. This orders-of-magnitude resource disparity makes the competitive novelty notable.

- **Equilibrium conformation generation from an informed prior (§4.2, Table 2).** FoldFlow with an informed prior (OmegaFold/ESMFold predictions) achieves $\mathcal{W}_2$ of 4.379 vs. 4.844 for FrameDiff on the BPTI trajectory, demonstrating a capability unique among compared methods — diffusion approaches cannot start from an arbitrary source distribution. This cleanly validates the "any source" advantage claimed in Figure 1.

---

## Weaknesses

### Fatal
None.

### Major

- **Inference annealing is critical but uncharacterized, creating a gap between the theoretical framework and deployed method (§4.1, lines 368–369, Table ablation).** The paper discloses that inference annealing (multiplying the rotation velocity by $i(t)=ct$ with $c\approx 10$) "greatly improves designability." The ablation table shows this is not a minor refinement but the dominant factor: bare flow matching (no OT, no aux, no annealing) achieves 0.228 designability — *worse* than FrameDiff-ICML (0.402), FrameDiff-Improved (0.555), and FrameDiff-Retrained (0.612). Adding annealing alone (still no OT, no aux) jumps to 0.648. The paper never reports the non-annealed performance of FoldFlow-OT (the best model), so we cannot assess whether the OT contribution itself is effective, or whether annealing is carrying all the weight. Critically, the paper does not characterize what distribution the annealed process actually samples, nor analyze why the learned vector field systematically requires this correction. This does not invalidate the empirical results (the full system works), but it means the paper's core claim — "flow matching on SE(3) is a strong alternative to diffusion" — is supported empirically only when a non-justified inference modification is applied, and the contribution of the flow-matching framework itself is confounded with this trick.

### Minor

- **Comparison with retrained FrameDiff is confounded by shared architecture and hyperparameter tuning (line 350).** FrameDiff-Retrained uses "the majority of the hyperparameters of FoldFlow" — i.e., hyperparameters tuned for FoldFlow, not FrameDiff. Since FoldFlow and FrameDiff share the same AF2 structure module architecture and auxiliary losses (borrowed from Yim et al., 2023), the key difference reduces to the training objective (CFM vs. score matching) plus inference annealing (which FrameDiff does not use). The base FoldFlow-Base with annealing (0.657) vs. FrameDiff-Retrained (0.612) gap is modest (0.045). It is unknown whether applying inference annealing to FrameDiff would close or reverse this gap.

- **Diversity metric is evaluated only on designable proteins, producing incomparable effective sample sizes across models (lines 361).** Since FrameDiff-ICML has 0.402 designability and FoldFlow-OT has 0.820, diversity is computed on very different numbers of samples per model. This makes the diversity column in Table 1 difficult to interpret as a fair comparison.

- **The OT transport plan computation is not described (§3.2, line 225).** The paper states "we rely on the optimal transport plan $\pi$" and "draw two samples from $\pi$" without specifying whether Sinkhorn, minibatch OT, or another algorithm is used, what cost function is discretized, or how the coupling scales with protein length and batch size. This is a standard implementation detail in Euclidean CFM-OT work (Tong et al., 2023; Pooladian et al., 2023) and should be specified.

- **Informative prior advantage is demonstrated on only one small-scale task (BPTI, 58 residues), while the main protein backbone experiment uses an uninformed uniform prior.** The paper frames "ability to start from an informative prior" as a key advantage (line 79), but this is leveraged in only one experiment. The equilibrium experiment also shows FoldFlow with a *random* prior outperforming FrameDiff (W₂ 4.446 vs. 4.844), which is unexplained — if flow matching alone (without informed prior) already beats diffusion, the narrative about the informative prior advantage is somewhat weakened.

### Trivial
- The number of sampling steps and specific temperature parameters for generation are not reported in the main text.

---

## Nice-to-Haves
- Report non-annealed FoldFlow-OT performance to isolate the OT contribution from the annealing trick.
- Apply inference annealing to FrameDiff to test whether this closes the gap with FoldFlow.
- Standard errors for the diversity metric in Table 1.
- Describe the OT coupling algorithm and its computational overhead.

---

## Removed Points

These points were identified in the reviews but removed after cross-checking against the paper:

- **FoldFlow-SFM method description missing from main body (line 256 `\input{se3_schrodinger_bridge}`).** *Removed per instruction: parser-stripped content from the original submission is assumed to exist. The weakness is about a missing section caused by the extraction pipeline, not a paper flaw.*
- **"The claim that avoiding autograd is misleading."** *Removed: the paper's description of the closed-form velocity avoiding matrix logarithm approximation and autograd is accurate and well-grounded (lines 184–199). The critic's suggestion that "the paper could have used autograd" does not constitute a weakness — avoiding autograd is a genuine implementation improvement.*
- **"Iterations/second advantage not discussed."** *Removed: the paper reports iters/sec in Table 1. Whether the speed advantage comes from flow matching vs. implementation details is a minor question unanswerable from the paper alone; it does not constitute a concrete weakness.*
- **"Missing related works."** *Removed per instruction: I cannot confirm existence of missing related works and should not fabricate such weaknesses.*
- **Various formatting/presentation nitpicks.** *Removed per instruction.*

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions
1. Report FoldFlow-OT designability **without** inference annealing. This is the single most important missing ablation to validate the flow-matching + OT contribution independently of the sampling trick.
2. Characterize the effect of inference annealing: what distribution does the annealed process sample? Is the learned vector field systematically incorrect in a way that linear velocity scaling compensates for? Even a simple empirical analysis of flow norms over time would be informative.
3. Specify how the OT transport plan $\pi$ is computed (algorithm, cost function, batch size scaling).

---

## Score and Decision

Based on my review, the paper has genuine and nontrivial contributions: the closed-form SO(3) velocity, the Riemannian OT extension with Monge map proof, and strong empirical results. However, the inference annealing issue is a significant concern — the paper's central empirical claims depend heavily on a procedure that contradicts the theoretical framework, and the contribution of the flow-matching approach itself is not cleanly isolated from this post-hoc fix. The paper would benefit from substantial revision to address this gap. At a top venue like ICLR, this level of ambiguity between the stated method and the deployed procedure is problematic.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>