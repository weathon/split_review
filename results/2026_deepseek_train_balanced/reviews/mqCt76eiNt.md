## Summary

This paper proposes Advantage-Aware Policy Optimization (A2PO), an offline RL method that addresses the constraint-conflict problem in mixed-quality datasets. The key idea is to use a CVAE conditioned on (state, advantage) to model action distributions from all behavior policies, then freeze the CVAE decoder as an explicit advantage-aware constraint during actor-critic optimization. This avoids discarding low-advantage transitions (a limitation of prior advantage-weighted methods like LAPO) while still steering the policy toward high-advantage behavior.

---

## Strengths

1. **Concrete diagnosis of the overfitting problem in Advantage-Weighted methods.** The didactic experiment (Figure 1) shows that LAPO accurately estimates advantage for only a small subset of high-return pairs while systematically underestimating it for many effective pairs. This visual, empirical grounding goes beyond generic "overfitting" claims and directly motivates why explicit advantage-conditioning is worth exploring.

2. **Architectural novelty that avoids data-discarding.** Unlike AW methods that prioritize/reweight samples and inevitably exclude low-advantage transitions, the CVAE-based design (Section 4.1, Equations 3–5) models action distributions of *all* behavior policies simultaneously by conditioning on advantage. The frozen decoder then serves as an explicit constraint during actor optimization (Section 4.2, Equation 7). This turns the multi-modal structure of mixed-quality data from a problem into a structured representation.

3. **Strong empirical results on the most challenging mixed-quality benchmarks.** On newly constructed datasets (random-medium, random-expert, random-medium-expert) where all baselines including LAPO and BPPO show sharp performance drops and increased variance, A2PO achieves best results on the majority of tasks. The total score improvement over LAPO (the next-best AW method) by over 33% (line 152) across all locomotion tasks is substantial, and the hardest tasks are precisely those the method was designed for.

4. **Informative ablations that isolate the advantage-conditioning mechanism.** The comparison of continuous vs. discrete vs. fixed advantage conditions (Figure 3) cleanly separates the paper's contribution from the underlying CVAE/actor-critic infrastructure. The fixed condition (ξ=1) causes severe degradation, confirming that advantage-awareness—not the CVAE presence alone—drives the gains.

5. **Test-time conditioning validation.** Figure 4 shows that fixing different discrete ξ values at test time produces returns that partition cleanly by the designated condition. The gap grows as the dataset includes more diverse behavior policies, providing evidence that the learned policy has internalized distinct behavioral modes tied to advantage levels.

---

## Weaknesses

### Fatal
None.

### Major

1. **CVAE training step (K) sensitivity with no principled selection criterion.** The ablation (Figure 5, Section 5.3) shows that K=10⁵ underperforms, K=2×10⁵ is optimal, and K=10⁶ causes performance collapse. The paper's Conclusion (line 191) honestly states the method "heavily relies on the specified step number" — but offers no heuristic, early-stopping criterion, or guidance for selecting K on a new domain. Since the optimal K likely depends on dataset size, composition, and behavior-policy complexity, applying A2PO to a new problem requires extensive tuning. This is a structural limitation of the method, not a minor hyperparameter nuisance.

2. **Non-stationary advantage labels create a moving target for the CVAE.** The CVAE is trained on advantage estimates from critic networks that are themselves being trained simultaneously (Section 4.1, line 90). The paper's mitigation (halting CVAE training after K steps while the critic continues to improve; Section 4.2, line 119) is acknowledged as a limitation in the Conclusion. The ablation confirms the severity: training the CVAE too long (K=10⁶) causes collapse. While the empirical results show the method works *despite* this issue, the two-stage procedure introduces a misalignment between the frozen CVAE (trained on early, evolving advantage estimates) and the continually improving critic. The paper would be stronger with a stabilized advantage estimation procedure or evidence that the early estimates are sufficiently accurate for the CVAE's purpose.

3. **The "disentangling" framing overstates what the CVAE achieves.** The paper repeatedly claims the CVAE "disentangles the action distributions of different behavior policies" (Abstract, Section 4.1, Conclusion). What the CVAE actually does is condition on (state, advantage) — it has no access to which behavior policy generated a given transition. A low-advantage action could come from a random policy, an expert policy making a cautious move, or a medium policy at a hard state. The CVAE learns a mapping from (state, advantage-value) to plausible actions, which is useful but is *advantage-conditioned action modeling*, not policy-identity disentangling. The gap between the claimed framing and what is technically implemented is significant, and the paper would be more credible using more precise language.

### Minor

1. **Navigation experiments do not test the paper's central claim.** The paper's main contribution is addressing the constraint-conflict issue in mixed-quality datasets. Yet the navigation experiments (Table 2) are evaluated only on single-quality (expert) datasets (Section 5.1, line 133). The results show A2PO works on navigation, which is positive for general applicability, but this portion of the evaluation does not bear on the paper's core thesis. Constructing mixed-quality navigation datasets or qualifying this limitation would improve the paper.

2. **Hyperparameter α (KL-divergence coefficient) is never specified or ablated.** α appears in the CVAE loss (Equation 5) and again in the λ normalization coefficient for the actor loss (line 117). Its value is never stated, and no ablation study examines its effect. Given the central role of both the CVAE and the actor-critic trade-off, this is a gap in experimental reporting.

3. **The advantage estimation quality is not quantitatively evaluated.** The paper claims A2PO produces better advantage estimates than LAPO (Figure 1c), but provides only a visual comparison. Quantitative metrics (e.g., MSE of advantage estimates against Monte Carlo returns) would substantiate this claim and strengthen the connection between the method's design and its empirical success.

### Trivial
None.

---

## Nice-to-Haves
- A heuristic or validation-based criterion for selecting K (rather than exhaustive search) would significantly improve the method's usability.
- Reporting navigation results on mixed-quality datasets would strengthen the evaluation.
- Ablation or specification of α would complete the experimental picture.

---

## Removed Points
These points were flagged in the reviews but removed after verification against the paper:

- *"33% improvement claim is unverifiable because Table 1 is an image."* — REMOVED (parser artifact; the table existed in the original PDF submission).
- *"No statistical significance testing."* — REMOVED (mean/std over 5 seeds is the field standard for D4RL evaluations; requesting formal hypothesis testing is not standard practice).
- *"CVAE training details not in main text."* — REMOVED (these are appendix details, and the hard rules prohibit marking missing appendix content as a weakness).
- *"The critic loss is complex / could benefit from clearer exposition."* — REMOVED (subjective presentation opinion, not a concrete weakness).
- *"The description of results is imprecise/hedged."* — REMOVED (the claim about A2PO "consistently outperforms most other baselines on the majority of these datasets" is appropriately qualified for empirical RL papers).
- *"MOPO claim about samples from behavior policies is strange."* — REMOVED (the paper's claim is interpretable: MOPO benefits from more data to model dynamics; this is not a factual error).

---

## Novel Insights
The reviews surface a genuine tension at the heart of the paper: the method's central mechanism — conditioning a generative model on advantage estimates — both enables its success (by preserving all data while steering toward high-advantage behavior) and creates its main vulnerability (non-stationary labels from a simultaneously-trained critic). The paper's response (early halting of CVAE training) is a pragmatic band-aid that works empirically but does not resolve the underlying instability. This tension between architectural innovation and training instability is common in multi-stage learned systems, and A2PO's strong empirical results despite this flaw suggest the idea has genuine merit — but the paper would be significantly stronger if it either fixed the non-stationarity or provided a principled understanding of when and why the early-halting strategy succeeds.

---

## Suggestions
1. **Stabilize the advantage labels** by pre-training the critic to convergence *before* training the CVAE, so the CVAE conditions on stable estimates. This would directly address the core non-stationarity problem and make the "disentangling" claim more plausible.
2. **Re-frame the contribution.** Replace "behavior policy disentangling" with "advantage-conditioned action modeling" or similar precise language throughout. The method's value does not depend on this overclaimed framing.
3. **Provide a heuristic for K.** Even a simple validation-based early-stopping rule (e.g., monitor CVAE reconstruction loss on a held-out set) would substantially improve practical usability.
4. **Report single-quality vs. mixed-quality totals separately** and include navigation results on constructed mixed-quality datasets.
5. **State and ablate α** in the main text or appendix.

---

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>