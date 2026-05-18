Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper introduces DecompDPO, which adapts Direct Preference Optimization (DPO) for structure-based drug design by incorporating decomposition into preference alignment. The key ideas are: (1) classifying optimization objectives as decomposable or non-decomposable, (2) applying GlobalDPO (molecule-level DPO) to non-decomposable objectives and LocalDPO (substructure-level DPO) to decomposable ones, (3) a physics-informed energy penalty to maintain reasonable molecular conformations, and (4) a linear beta schedule for efficiency. Empirically, DecompDPO achieves strong results on CrossDocked2020 — 95.2% High Affinity (vs 85.5% for the next-best generative model IPDiff) and 36.2% success rate for generation, and 100% High Affinity / 52.1% success rate for molecular optimization.

## Strengths

- **Strong and consistent empirical gains.** The method substantially outperforms all generative baselines on multiple affinity and property metrics (Table 2). The 95.2% High Affinity and 36.2% success rate represent large, practically meaningful improvements over prior methods (IPDiff: 85.5%/25.6%). These gains hold across both generation and optimization settings. The ablation (Table 5) further shows that the full DecompDPO outperforms the molecule-level DPO variant on most metrics, supporting the value of decomposition.

- **Well-motivated and clearly scoped problem framing.** The paper identifies that different pharmaceutical objectives (Vina Min Score vs. QED/SA) have different decomposability properties, validates this empirically (Figure "decomp_prop" showing proportional relationship for Vina Min), and designs separate alignment mechanisms (GlobalDPO vs. LocalDPO) accordingly. This nuanced treatment is principled and practically relevant.

- **Multi-faceted evaluation including molecular conformation quality.** Beyond standard binding affinity and drug-likeness metrics, the paper evaluates whether generated molecules maintain physically reasonable conformations (JSD of atom distance distributions, MMFF energy differences, RMSD). This is often neglected in SBDD preference alignment work and strengthens the claim that the physics-informed penalty serves its purpose — DecompDPO achieves the lowest JSD among generative models.

- **Clear ablation isolating the two main algorithmic contributions.** The ablation in Table 5 separately compares DecompDPO vs. molecule-level DPO (isolating decomposition) and DecompDPO vs. constant beta (isolating the beta schedule). Each variant shows measurable improvements, supporting both claimed contributions.

## Weaknesses

### Fatal
None.

### Major

- **Unsupported factorization claim in the LocalDPO derivation (Section 3.2, line 116).** The paper states "the probability of a molecule is equivalent to the product of the probabilities of its decomposed substructures" without justification or citation. In DecompDiff, atoms are generated jointly; the model does not factorize into independent substructure probabilities. Substructure decomposition is a structural annotation, not a probabilistic factorization of the joint density. The derivation of Eq. 6 from the Diffusion-DPO loss relies on this claim. Without it, LocalDPO is not a "reformulation" of Diffusion-DPO but rather a heuristic training loss. **However, this is not fatal** — the empirical results would stand if LocalDPO were reframed as an empirically motivated loss that provides finer-grained preference signals, and the ablation already supports its effectiveness over molecule-level DPO. The paper should either provide rigorous justification (e.g., showing that the model's generative process approximately factorizes), or explicitly reframe LocalDPO as a heuristic.

### Minor

- **Linear beta schedule lacks theoretical grounding (Section 3.4).** The paper introduces $\beta_t = (t/T)\beta_T$ without modifying the DPO derivation, which in Diffusion-DPO assumes a constant $\beta$. The schedule is presented as an empirical improvement and validated in the ablation. This is a reasonable heuristic, but the paper should acknowledge that it is not derived from the standard DPO objective and briefly discuss whether it preserves the preference-alignment interpretation (e.g., as a time-dependent KL penalty in a multi-step MDP).

- **Novelty claim about being "first" is slightly overstated given concurrent work.** The paper acknowledges Gu et al. (2024, AliDiff) as "independent concurrent work that also uses preference alignment methods to fine-tune diffusion models for SBDD" but still claims to be "first to introduce preference alignment to structure-based drug design" (contributions list and conclusion). This is a common convention in ML, but the wording is contradictory given the acknowledgement. The authors should qualify this more precisely (e.g., "first to formulate multi-objective preference alignment with decomposition for SBDD").

- **Physics-informed energy term is not directly ablated.** The paper compares DecompDPO against molecule-level DPO and against constant beta, but does not include a variant that removes only the $r_{\text{constraint}}$ penalty. Without this ablation, the claim that the energy term "maintains reasonable molecular conformations" is only indirectly supported by comparing DecompDPO's conformation metrics against other generative models (not against itself without the penalty). Adding this ablation would strengthen the claim.

- **AliDiff comparison appears only in single-objective ablation, not the main table.** AliDiff is the most directly related method. While its omission from the multi-objective main table (Table 2) is defensible — AliDiff is a single-objective method that optimizes only Vina Minimize — the paper should explicitly state this rationale. Currently it is left implicit.

- **Iterative optimization procedure is underspecified.** For molecular optimization, the paper says "we perform iterative DPO" but does not report the number of iterations, early stopping criteria, or how many rounds were used for the results in Table 4. This hurts reproducibility.

- **Results are reported as point estimates without confidence intervals.** This is standard practice in the SBDD generation literature (the critic acknowledges this), but given the stochasticity of diffusion models and the non-deterministic optimization process, error bars or significance tests would strengthen the claims — particularly in Table 4 where differences between methods are smaller.

### Trivial
- The paper does not report computational cost (GPU-hours, convergence speed) of fine-tuning, which would be useful for practitioners.
- The decomposability validation (Figure "decomp_prop") is shown for the training set only; the paper does not discuss whether the proportional relationship holds for test proteins.

## Nice-to-Haves
- A cross-validation analysis of the decomposability assumption for Vina Min across diverse test proteins would increase confidence.
- Reporting the number of DPO iterations used for molecular optimization.
- An ablation removing only the physics constraint to isolate its effect.

## Removed Points

- **Criticism about the ablation "conflating" decomposition with the beta schedule and physics constraint.** The ablation table includes a separate "w/o linear beta" row, demonstrating that both DecompDPO and Molecule-level DPO use the beta schedule. The physics constraint applies to the reward function and would affect both variants equally. So the comparison does isolate the decomposition effect. This criticism is inaccurate.

- **Criticism that AliDiff omission from the main table constitutes "selective reporting."** AliDiff is a single-objective method; the main results table evaluates multi-objective generation. Including AliDiff in that table would require adapting it to a setting it was not designed for. The paper reasonably places it in the single-objective ablation. The omission is defensible.

- **Strength about adapting bond-first noise schedule to DecompDiff.** This is an implementation detail, not a core contribution, and is generic (following prior work). Moved here.

- **Generic strength about "addressing an important problem."** Too generic to carry weight.

## Novel Insights

The review process surfaces one genuinely novel observation beyond the paper's own contributions: The relationship between the factorization claim and the actual LocalDPO loss is more nuanced than either the paper or the critic fully articulates. The paper's Eq. 6 (the "reformulated" Diffusion-DPO with substructure log-ratio sum) would require the factorization to hold, but the actual LocalDPO loss in Eq. 7 departs from it further by introducing the sign function, which is a heuristic intervention that cannot be derived from any factorization. In other words, even if the factorization were rigorously justified, Eq. 7 would still be an additional heuristic modification. This means the factorization issue is somewhat less central than the critic suggests — LocalDPO is already a heuristic at the level of the sign function, so the paper could cleanly reframe both Eq. 6 as an approximation and Eq. 7 as a heuristic without changing the empirical claims.

## Suggestions

1. **Reframe LocalDPO explicitly.** Replace the unsupported factorization claim with a clear statement: "We approximate the substructure-level log-ratios... as a heuristic training loss that provides finer-grained preference signals." This admits the approximation honestly and preserves all empirical results.

2. **Add an ablation removing only the physics constraint.** This would directly validate the claim that it helps maintain reasonable conformations.

3. **Specify the iterative DPO procedure.** Report the number of iterations used for the molecular optimization results in Table 4.

4. **Clarify the novelty claim.** Replace "first to introduce preference alignment to SBDD" with something like "first to formulate multi-objective preference alignment with decomposition for SBDD" to avoid contradiction with acknowledged concurrent work.

5. **Acknowledge the heuristic nature of the linear beta schedule.** Add a sentence noting that it is not derived from the DPO objective but works well empirically.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>