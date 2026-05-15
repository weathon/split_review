Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

**Key findings from cross-checking:**

1. **Critical Issue 1 (Eq. 6→7)**: The reviewer's claim about "max and average not commuting" is **mathematically incorrect**. The inequality \(\max_{||\Delta||<\gamma} \sum p_i f_i(\Delta) \le \sum p_i \max_{||\Delta_i||<\gamma} f_i(\Delta_i)\) always holds. The valid concern is different: extending Assumption 1 from the actual local models \(\theta_i\) to perturbed versions \(\theta_i + \Delta\) isn't justified by the assumption as stated. But the reviewer's specific argument is wrong.

2. **Critical Issue 2 (Theorem 2's assumption)**: The paper explicitly acknowledges this is an idealized assumption ("theoretical value"). Standard practice in ML theory papers.

3. **Empirical validation of Assumption 1**: The reviewer correctly notes it only validates regular risk, not robust risk.

Now producing the consolidated review:

Let me think about the scoring.

The paper makes a genuine contribution: it identifies the gap between local and global flatness in FedDG, and proposes a practical method combining constrained adversarial augmentation with SAM. The empirical evidence (flatness measurements, loss surfaces, ablation) strongly supports the core claim that GFM finds flatter global minima.

The theoretical story is somewhat rough: the derivation from Assumption 1 to Eq. (7) has a subtle gap (extending to perturbed models), and Theorem 2 relies on an idealized assumption. However, the paper is not primarily a theory paper — it's an empirical method paper with theoretical motivation. The weaknesses are genuine but not fatal.

I'll rate this as a solid paper with minor-to-moderate theoretical gaps that don't undermine the empirical contribution.

Score: 6.5/10 — good paper with clear contributions and generally solid experiments, but theoretical framing is somewhat loose and some experimental details (variance, baseline reproduction) are lacking.

## Summary

This paper proposes GFM (Global Flat Minima), a federated domain generalization algorithm that seeks globally flat minima by combining (i) global-model-constrained adversarial data augmentation (GCA) to create a local surrogate for global data, and (ii) sharpness-aware minimization (SAM) for local flatness. The core idea—decomposing the search for global flatness into local flatness plus global-local consistency via augmentation—is well-motivated and novel. The paper provides theoretical bounds (Theorem 2) connecting the robust risk on augmented local data to unseen-domain generalization, and validates the method on four FedDG benchmarks with consistent improvements over baselines.

## Strengths

- **Novel and well-motivated approach to global flatness in FedDG.** The paper correctly identifies that prior FedDG methods (FedSAM, FedGAMMA, FedSMOO) only seek local flatness on each client, which is suboptimal for the global model. The decomposition into local flatness + global-local consistency via constrained augmentation is a genuine algorithmic contribution. The design is modular and can be combined with other aggregation methods (e.g., GA), as demonstrated.

- **Direct empirical evidence that GFM finds flatter global minima.** The flatness metric \(F_\gamma(\theta)\) in Fig. 1 provides quantitative evidence that GFM consistently achieves lower (flatter) values than both FedAvg and FedSAM across all unseen domains. The loss surface visualizations in Fig. 2 further confirm this qualitatively. This evidence directly supports the paper's core claim and does not depend on baseline reproduction or statistical significance testing.

- **Consistent accuracy improvements across diverse benchmarks.** GFM (FedAvg) achieves the best or second-best average accuracy on all four benchmarks (Digits-DG, PACS, OfficeHome, TerraInc) in Table 1. The ablation study (Table 2) cleanly separates the contributions of GCA and SAM, showing that neither component alone is sufficient—both are necessary for the best performance.

- **Careful ablation and parameter analysis.** Table 2 isolates four conditions (FedAvg, FedSAM, GCA alone, full GFM), showing that GCA alone can even hurt on harder datasets (OfficeHome, TerraInc) while the full GFM consistently helps. Fig. 4 shows GFM is less sensitive to the perturbation radius \(\gamma\) than FedSAM, and more frequent augmentation updates improve performance—providing practical guidance.

## Weaknesses

### Fatal

None.

### Major

None that threaten the paper's core empirical contribution. The weaknesses below are significant but addressable.

### Minor

1. **The theoretical derivation from Assumption 1 (regular risk) to Eq. (7) (robust risk) has a subtle gap.** The paper states "With Assumption 1, we derive the following upper bound" and writes \(\hat{\mathcal{E}}_D^\gamma(\theta) \le \sum_i p_i \hat{\mathcal{E}}_D^\gamma(\theta_i)\). This requires applying Assumption 1 to shifted models \(\theta_i + \Delta\) rather than the actual local models \(\theta_i\). While the inequality \(\max_{||\Delta||<\gamma} \sum p_i f_i(\Delta) \le \sum p_i \max_{||\Delta_i||<\gamma} f_i(\Delta_i)\) always holds (contrary to the reviewer's claim about max/avg not commuting), the real gap is that Assumption 1 as stated only covers the actual local models, not arbitrarily perturbed versions. The paper does not discuss this extension, and the empirical validation (Sec. 4.4) tests only the regular-risk version, not the robust-risk version. This weakens the theoretical grounding but does not invalidate the algorithm, which is motivated more by intuition and empirical validation than by formal proof.

2. **Theorem 2 relies on an idealized assumption about the augmentation model.** The theorem assumes there exists \(\hat{\phi}_i\) such that \(a(D_i;\hat{\phi}_i) \overset{d}{=} D\) (the global data distribution). The paper acknowledges this ("theoretical value"), but the bound is on a quantity that cannot be realized by the practical augmentation network (a simple CNN applying color/geometry transforms). The gap between the idealized bound and the practical algorithm is not quantified or discussed beyond a brief note. This is common in ML theory papers that use idealizing assumptions for motivation, but it means the theorem should be interpreted as a conceptual justification rather than a rigorous guarantee for the implemented method.

3. **Baseline comparisons lack variance and are not clearly documented as reproduced under identical conditions.** The paper reports point estimates for baselines like FedSR, GA, StableFDG, and FedIIR without standard deviations or confidence intervals. It does not explicitly state whether these results were reproduced under the same backbone, optimizer, data splits, and training rounds, or cited from original papers. In federated DG, minor implementation differences can shift rankings. The paper's strongest empirical evidence (flatness measurements in Fig. 1, loss surface visualizations in Fig. 2) does not depend on baseline reproduction, but the accuracy claims in Table 1 would be stronger with controlled reproduction and variance reporting.

4. **Missing ablation for the global model constraint specifically.** The ablation (Table 2) compares "with GCA" vs. "without GCA," but GCA includes both the adversarial augmentation term AND the global model constraint term. An appropriate control would compare the full GCA objective (Eq. 9) against an unconstrained version that maximizes only the local risk term \(\ell(f(a(x;\phi_i);\theta_i+\Delta_i), y)\) without the global model penalty \(-\ell(f(a(x;\phi_i);\theta), y)\). This would isolate whether the global model constraint itself is responsible for the improvement, which is central to the paper's narrative.

5. **"Previous SOTA" not explicitly identified.** The claim that "GFM (GA) surpasses the previous SOTA method by 1.7 percent on average" does not name which method is the previous SOTA. This should be clear from context (likely the best non-GFM baseline in the table) but should be stated explicitly.

### Trivial

- The informal statement of Proposition 1 is presented without a formal proof or reference. The paper states the proof is deferred (presumably to an appendix that was stripped by the parser), which is acceptable for the main text.

## Nice-to-Haves

- Reproduce key baselines (at least FedAvg, FedSAM, and one representative FedDG method) under identical conditions with multiple seeds and report mean ± std.
- Add an ablation comparing the full GCA objective (Eq. 9) against unconstrained adversarial augmentation (maximizing only the local risk term). This would directly test whether the global model constraint is necessary.
- Validate Assumption 1 for robust risk (\(\hat{\mathcal{E}}_D^\gamma\)) on at least one dataset, not just regular risk. Even a limited check would strengthen the theoretical motivation for Eq. (7).
- Include augmented image examples from the GCA network to illustrate what kind of global-data surrogate is being generated.
- Quantify the computational overhead (wall-clock time or FLOPs) of GFM vs. FedAvg and FedSAM to help practitioners assess the practical cost.

## Removed Points

- **Criticism about max/avg not commuting in Eq. (7):** The reviewer claimed the step "treats the max and the average as interchangeable" and that it "generally does *not* hold." This is mathematically incorrect: the inequality \(\max_{||\Delta||<\gamma} \sum_i p_i f_i(\Delta) \le \sum_i p_i \max_{||\Delta_i||<\gamma} f_i(\Delta_i)\) always holds. The valid concern (extending Assumption 1 to perturbed models) is different and is preserved in Minor Weakness 1 above.

- **Criticism about Theorem 2 being "vacuous":** The paper explicitly labels this as having "theoretical value" and acknowledges the idealization. The bound serves as conceptual motivation, which is a standard and acceptable use of idealized assumptions in ML theory papers. The weakness is kept but softened to Minor Weakness 2.

- **Formatting/style nitpicks:** references to garbled table text, missing appendix proofs, broken characters, missing symbols. These are parser artifacts, not author errors.

- **Criticism about Proposition 1 proof being missing:** Rule states to remove weaknesses about missing appendix content, as the parser strips those sections.

- **Criticism about "unfair comparison" favoring baselines:** The reviewer did not raise this specific concern in a way that matches the rule's condition, so no removal needed on this basis.

- **Generic strengths from Strength Finder:** Several claimed strengths (e.g., "careful ablation" is already covered by the paper's own claims) are duplicates. The strength about "theoretical connection" is weakened by the idealized assumptions but still valid as a conceptual contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the derivation from Eq. (6) to Eq. (7).** Add a brief explanation: applying Assumption 1 to models \(\theta_i + \Delta\) for any fixed \(\Delta\), then using the fact that \(\max_{||\Delta||<\gamma} \sum_i p_i \hat{\mathcal{E}}_D(\theta_i + \Delta) \le \sum_i p_i \max_{||\Delta_i||<\gamma} \hat{\mathcal{E}}_D(\theta_i + \Delta_i)\). Acknowledge that this extends Assumption 1 beyond its literal statement.

2. **Validate Assumption 1 for robust risk** on at least one dataset (e.g., PACS) by computing \(\hat{\mathcal{E}}_D^\gamma(\sum p_i \theta_i)\) and \(\sum p_i \hat{\mathcal{E}}_D^\gamma(\theta_i)\) and showing the inequality holds. This would directly support Eq. (7).

3. **Run the missing ablation** comparing full GCA vs. unconstrained adversarial augmentation (remove the \(-\ell(f(a(x;\phi_i);\theta), y)\) term). This would confirm whether the global model constraint is responsible for the improvement or whether simple adversarial augmentation suffices.

4. **Reproduce key baselines under identical conditions** and report means and standard deviations over at least 3 seeds. At minimum, reproduce FedAvg, FedSAM, and one top FedDG method (e.g., FedSR or GA) with the same backbone, optimizer, local epochs, and data splits.

5. **Explicitly name the previous SOTA** when claiming the 1.7% improvement. Add a row or footnote to Table 1 identifying the best prior method.

## Score and Decision

This paper makes a genuine and well-motivated contribution to federated domain generalization. The core idea—seeking global rather than local flatness via constrained adversarial augmentation—is novel, the algorithmic design is clean and modular, and the empirical evidence (flatness measurements, loss surface visualizations, accuracy improvements, ablation study) consistently supports the method's effectiveness. The theoretical framing has gaps (extending Assumption 1 to perturbed models, idealized augmentation in Theorem 2) but these are standard weaknesses in empirically-driven ML papers and do not undermine the core contribution. The experimental evaluation would benefit from controlled baseline reproduction and variance reporting. Overall, the paper presents a solid, well-evaluated algorithm with clear empirical advantages over existing approaches.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>