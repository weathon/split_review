Now I have sufficient information to write the final review. Let me synthesize everything.

---

## Summary

This paper proposes three one-step diffusion-based solvers (CMILP, SCMILP, MFILP) for integer linear programming, extending prior diffusion-based ILP solvers in two key ways: (1) dramatically reducing inference time from hours/minutes to seconds via consistency, shortcut, and meanflow training paradigms, and (2) handling non-binary integer variables through a novel Iterative Integer Projection (IIP) layer that avoids costly binarization. A momentum mechanism is added to objective-guided sampling. Experiments span binary ILP benchmarks and two types of non-binary problems (inventory management, synthetic random ILPs), demonstrating 10-1000× speedups over prior diffusion solvers while maintaining competitive feasibility.

## Strengths

- **IIP layer enables non-binary ILP without binarization.** The differentiable integer projection in Eq. (3) converges to integer rounding within a few iterations (Fig. 2), and Table 4 convincingly demonstrates that binarization collapses feasibility for prior methods (0% sample feasibility for IP Guided DDPM/DDIM on binarized instances) while the proposed methods with IIP retain 69-71% sample feasibility on the same problems. This is a genuine architectural contribution.

- **Dramatic inference-time reduction with one-step diffusion.** Across all problem classes, the proposed solvers reduce inference time by orders of magnitude: CMILP finishes in 21.7s vs. 11h for DDPM and 65min for DDIM on set cover (Table 1); MFILP takes 3.6s vs. 1.2h for DDPM on Random-(500,20,2) (Table 6). This makes neural ILP solving practically competitive with traditional solvers for the first time.

- **Extensive and diverse experimental evaluation.** The paper evaluates on classic binary ILP benchmarks (SC, CF, CA), non-binary inventory management at multiple scales (Tables 2-3), synthetic non-binary ILP at three scales up to 2000 variables (Table 6), binarization comparisons (Table 4), and momentum ablations (Table 5). Comparisons include traditional solvers (Gurobi, SCIP, COPT), heuristics (rins, feaspump), and multiple neural baselines.

- **Momentum-guided sampling provides consistent, low-cost improvement.** Table 5 shows that adding momentum to objective-guided sampling reduces the optimality gap (e.g., 99.8% → 95.8% on IM-(50,5,10) with 20 steps) and improves dataset feasibility (87% → 88%) with negligible time overhead. The connection between diffusion guidance and gradient-based optimization (Section 3.3) is a useful conceptual reframing.

## Weaknesses

### Fatal

None.

### Major

- **The CMILP loss (Eq. 6) does not implement the self-consistency property it claims to.** The paper states that the consistency function should satisfy \(f_\theta(\mathbf{x}_t, t) = f_\theta(\mathbf{x}_{t'}, t')\) for all \(t, t'\) (lines 236-237), but the loss in Eq. (6) penalizes the distance between the model output and the ground-truth solution \(\mathbf{x}^*\) at two timesteps — it never compares \(f_\theta(\mathbf{x}_t, t)\) against \(f_\theta(\mathbf{x}_{t'}, t')\). What is actually trained is supervised regression of noisy inputs to \(\mathbf{x}^*\). While this indirectly forces outputs at all timesteps toward the same target and thus *implicitly* satisfies consistency, the theoretical framing is incorrect: the paper describes a self-consistency training protocol but implements direct regression to \(\mathbf{x}^*\). The boundary condition \(f_\theta(\mathbf{x}_\epsilon, \epsilon) = \mathbf{x}_\epsilon\) (line 236) is also not enforced — the model is trained to map even near-clean inputs to \(\mathbf{x}^*\), not to themselves. In practice this likely does not harm one-step generation from pure noise, but the mismatch between the claimed theoretical foundation and the actual training objective should be corrected. The authors should either acknowledge that their loss is a supervised regression simplification of consistency training, or adopt a genuine self-consistency loss.

### Minor

- **Abstract overstatement on binary ILP.** The abstract claims the method "outperforms existing learning-based methods on both binary and non-binary instances." On binary ILP (Table 1), IP Guided DDIM achieves better optimality gaps (68.5%, 54.6%, 25.4%) than the proposed methods (79-91%, 76-85%, 79-85%). The proposed methods win on speed and sample feasibility, but "outperforms" without qualification is misleading.

- **Two SCMILP rows in non-binary tables are unlabeled.** Tables 2-4 contain two rows both labeled "SCMILP (Ours)" with different numbers (e.g., Gap 16.5% vs. 12.2% in Table 2), while CMILP is absent from these tables. This is almost certainly a labeling error — one row likely corresponds to CMILP or to SCMILP with a different configuration. This makes the non-binary results difficult to interpret at a glance and should be corrected.

- **Missing ablations on key components.** No ablation is provided for the feasibility penalty \(\mathcal{L}_{\text{penalty}}\) or the CLIP-style contrastive pretraining. Given that constraint satisfaction and representation learning are central to the approach, readers cannot assess how much each component contributes. Similarly, while the paper notes that IIP uses one iteration during training and multiple during inference (line 186-187), no ablation over the number of IIP iterations is provided to justify this design choice or characterize the train-test mismatch.

- **No variance or distributional information.** All tables report single-point estimates without error bars, standard deviations, or box plots. Given that 30 samples are drawn per instance for generative methods, the variance of these samples is directly computable and its absence weakens confidence in the reported differences, particularly for metrics with small absolute gaps (e.g., Table 6).

### Trivial

- The two "SCMILP (Ours)" rows that should be disambiguated, as noted above.

## Nice-to-Haves

- A controlled study of the trade-off between number of inference steps, solution quality, and feasibility on representative instances would directly support the claimed speed-accuracy flexibility (mentioned but not systematically characterized).
- The synthetic instances where the proposed methods achieve 0.0% gap (Table 6) are also solved quickly by Gurobi. Identifying problem sizes where Gurobi's time explodes but the neural solver remains fast and yields acceptable gaps would substantially strengthen the practical value proposition.
- A discussion of how the consistency loss simplification (direct regression to \(\mathbf{x}^*\)) relates to standard consistency training, and why the simplification is valid in the ILP setting where \(\mathbf{x}^*\) is known during training.

## Removed Points

*These points were flagged for removal during cross-checking against the paper. Treat with caution.*

1. **"Training and inference procedures are under-specified to the point of irreproducibility."** REMOVED — The paper states that SCMILP and MFILP details are in the appendix (line 220: "The detailed introduction of shortcut and mean flow models are put in the appendix"). Per review policy, stripped appendix content is assumed to exist. The core CMILP procedure is described in the main text (Eqs. 4-6), and the noising process, reparameterization, and denoising process are all specified.

2. **"DiffILO comparison is unfair / misconfigured."** REMOVED — The paper includes DiffILO as a baseline and reports its results as obtained. If DiffILO performs poorly (512.3% gap on CF), that is an informative result, not evidence of unfair comparison. The claim that "the evaluation protocol is incompatible with that method's intended use" is speculative and unverifiable from the paper.

3. **"The 0.0% gap on binarized instances is suspicious."** REMOVED — The paper states that the gap metric is "only calculated among problems to which the solvers can get a feasible solution" (Section 4.1). Binarized instances have very low dataset feasibility (3-9%, Table 4), so the gap is computed over a tiny subset of instances. A 0.0% gap on those few feasible solutions is an expected artifact, not suspicious.

4. **"Best-of-30 vs. single-run comparison is unfair."** DEMOTED — This is standard practice in generative model evaluation for optimization. The paper transparently reports the sampling budget. Removed as a standalone weakness; folded into the broader missing-variance observation.

5. **"Optimality gap reference may not be globally optimal."** DEMOTED — Gurobi with a 100-second time limit is standard practice in ML-for-ILP literature. Multiple solvers (SCIP, COPT) confirm 0.00% gap on the synthetic datasets (Table 6), indicating the reference is indeed optimal for those problems. This concern carries minimal weight.

6. **"Neural Diving applied to non-binary without explanation."** REMOVED — The paper's point is precisely that binary-only methods fail on non-binary problems, motivating the IIP approach. The 0% feasibility is an informative baseline result, not a misconfiguration.

7. **"Missing hyperparameters, network sizes, noise schedules."** REMOVED — Per review policy, undisclosed hyperparameters and trivial implementation details are not grounds for criticism. These are expected to be in the appendix or code release.

## Novel Insights

The reframing of diffusion guidance for ILP as gradient-based optimization (Section 3.3) — where prior objective-guided sampling is recognized as a single gradient descent step — is a genuinely useful conceptual bridge between the diffusion and optimization literatures. It cleanly motivates the momentum extension and opens the door to importing other optimization techniques (adaptive step sizes, second-order methods) into the diffusion sampling process. This insight, while simple, connects two communities that rarely interact at this level of mechanism.

## Suggestions

- Correct the theoretical framing of CMILP: either rename the approach to clarify it uses supervised regression to \(\mathbf{x}^*\) rather than self-consistency training, or implement a proper consistency loss between pairs of timesteps and report whether it changes results.
- Fix the table labeling: disambiguate the two "SCMILP (Ours)" rows across Tables 2-4 by specifying which is CMILP and which is SCMILP, or what configuration differs between them.
- Add variance estimates (standard deviation of gaps across the 30 samples) to strengthen confidence in comparative claims, particularly for cases with small gap differences.
- Qualify the abstract's "outperforms" claim to reflect that DDIM achieves better optimality gaps on binary problems, while the proposed methods lead on speed and sample feasibility.

---

**Evaluation dimensions:**

- **Originality:** Moderate. The IIP layer is a genuinely novel contribution for non-binary ILP. The one-step diffusion adaptation and momentum guidance are solid but incremental extensions of existing techniques (consistency models, shortcut models, meanflow) to the ILP domain.

- **Importance:** High. Enabling neural solvers to handle non-binary ILP and achieve practical inference speeds addresses two major bottlenecks that have limited the real-world adoption of learning-based ILP solvers.

- **Claim support:** Moderately well-supported. The speed advantages and non-binary feasibility are convincingly demonstrated. However, the theoretical framing of the consistency loss is imprecise, and missing ablations leave some architectural contributions (feasibility penalty, contrastive pretraining) unvalidated.

- **Soundness:** Generally sound with one notable imprecision (the consistency loss formulation). The experimental methodology is reasonable for the domain, though the absence of variance information is a gap.

- **Clarity:** Adequate but with presentation issues. The two SCMILP rows and the mismatch between the described consistency properties and the actual loss create confusion. The writing is otherwise clear.

- **Community value:** Good. The IIP layer and the one-step diffusion speedup are practical contributions that can benefit follow-up work in neural combinatorial optimization.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>