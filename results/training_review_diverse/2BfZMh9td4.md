Now I have all the information needed. Let me produce the final review.

---

## Summary

This paper introduces Multi-Objective Direct Preference Optimization (MODPO), an RL-free algorithm that extends DPO to handle multiple alignment objectives (e.g., helpfulness vs. harmlessness). The key idea is to integrate linear scalarization into the reward modeling stage itself — training LMs to implicitly represent different weighted combinations of objectives through a simple cross-entropy loss — rather than using multi-objective RL. The paper provides a theoretical derivation showing that under known other-objective rewards, MODPO recovers the same optimal policy as MORLHF, and presents experiments on safety alignment and long-form QA demonstrating competitive or superior Pareto fronts with roughly 3× reduction in per-LM training GPU hours.

## Strengths

- **Theoretically grounded extension of DPO to multiple objectives.** The derivation (Section 3.1) provides a clean analytic mapping from the collective reward objective (Eq. 7) to a cross-entropy loss (Eq. 14) by leveraging the preference dataset \(\mathcal{D}_k\) to cancel the partition function. This gives MODPO a principled foundation that existing ad-hoc multi-objective DPO extensions (DPO soups, DPO loss weighting) lack.

- **Empirically competitive Pareto fronts with substantially lower computational cost.** In synthetic safety alignment (Figure 2, ground-truth rewards used), MODPO matches or outperforms MORLHF. In real safety alignment evaluated by GPT-3&4 (Figure 4), MODPO shows a comparable or marginally better front. Crucially, Table 1 demonstrates that training one LM with MODPO requires 7 GPU hours vs. 24 GPU hours for MORLHF — a ~3× reduction in per-LM training cost. The efficiency advantage is well-supported and significant.

- **Versatility across tasks and feedback types.** The method works with preference-only datasets (safety alignment on BEAVERTAILS), datasets combining preferences with multi-dimensional meta-labels (long-form QA on QA-FEEDBACK), and can leverage off-the-shelf feedback pipelines by repurposing existing meta-labels. This demonstrates broad applicability to real-world alignment scenarios.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Division by zero at boundary preference weights is not addressed.** The MODPO loss (Eq. 14) divides by \(w_k\), the weight on the preference dataset \(\mathcal{D}_k\) used in the loss. In the safety alignment experiments, the paper uses \(\mathcal{D}_2\) (helpfulness) as the preference dataset and sweeps \(w \in \{0.0, 0.2, 0.4, 0.6, 0.8, 1.0\}\) with \(\mathbf{w}=[1-w,w]^\top\). At \(w=0.0\), \(w_k = 0\), making the loss undefined. The paper provides no explanation of how this boundary case is handled (e.g., using standard DPO on \(\mathcal{D}_1\) at \(w=0\), or adding an epsilon). While this is unlikely to affect the central results — the interior weights carry the evidential weight and the boundary is trivially handled by single-objective DPO — it is a clarity gap that makes the experimental protocol incompletely specified. The authors should explicitly state the handling procedure.

- **Long-form QA evaluation uses the same reward models for computing training margins and for evaluation.** For long-form QA (Section 4.1, Figure 3), the reward models \(\mathbf{r}_\phi\) trained on the feedback datasets are used both for computing the margin in the MODPO loss and as the evaluation proxy for the ground-truth rewards \(\mathbf{r}^*\). The paper honestly acknowledges this and uses a higher KL penalty (\(\beta=0.5\)) as mitigation, but the mitigation does not remove the bias — only limits over-optimization. The observed advantage of MODPO over MORLHF in Figure 3 could partly reflect differential exploitation of the evaluation proxy rather than genuine superiority in aligning with true human preferences. The synthetic safety alignment experiments (Figure 2) do not share this issue, so the paper's core claims remain supported, but the long-form QA conclusions are weakened.

- **The theoretical "exact equivalence" claim in the abstract is stated without acknowledging the practical need to estimate other-objective rewards.** The abstract states MODPO produces "analytically the exact solutions of the original MORLHF objective." The derivation in Section 3.1 properly qualifies this ("under the true collective rewards," line 158) and notes that in practice \(r_{-k}^*\) must be replaced with estimated counterparts \(r_{\phi,-k}\) (line 148). The abstract's unqualified phrasing could mislead a reader about the approximation inherent in the practical method. This is a presentation issue rather than a methodological flaw, since every practical instantiation involves estimation.

### Trivial

- **The filtering of evaluation points not on any Pareto front** (line 207) is standard practice for visualizing fronts, but the paper does not report how many points were filtered. A brief note on the proportion of retained points would improve transparency.

- **The "3× less computational resources" claim** in the abstract refers specifically to per-LM training costs after amortizing reward model training. Table 1's caption clarifies this, but the abstract's phrasing could be read as a total-cost advantage. Clarifying "per-LM training cost" in the abstract would prevent misunderstanding.

## Nice-to-Haves

- Add a limitations section explicitly discussing the reliance on estimated other-objective rewards, the evaluation bias in long-form QA, and the boundary-case handling for \(w_k=0\).
- Include a small-scale independent evaluation (e.g., human evaluation or held-out reward models) for the long-form QA setting to strengthen the evidence.
- Add an empirical sensitivity analysis varying the quality of the margin reward model (e.g., trained on different amounts of data) to show robustness to approximation error.
- Report the number of evaluation points filtered during Pareto front construction.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Stability claim references Figure 3 for learning dynamics but Figure 3 shows reward fronts"**: The paper's reference (line 169, ".3") points to an appendix figure showing training accuracy curves. Appendix content was stripped by the parser — the original submission contains this evidence. (Rule: REMOVE weaknesses about missing appendix content.)
- **"Missing related works"**: Not confirmed — the paper adequately reviews RLHF, MORLHF, and RL-free alignment in Section 5. (Rule: DO NOT mention missing related works.)
- **"No scaling to more than two objectives"**: The paper states (line 185) that it explores more than two objectives and notes the results are in the appendix (stripped by parser). (Rule: REMOVE weaknesses about missing appendix content.)
- **"The 3× claim could be misleading about total cost"**: The paper explicitly qualifies this in Table 1's caption and Section 3.2 ("per-LM training costs"). The claim is clear in context. (Rule: REMOVE criticisms where the paper already addresses the concern.)
- **"Preference weights ambiguity about which objective corresponds to which w"**: The paper specifies that for safety alignment, \(\mathcal{D}_1 = \mathcal{D}_{\mathrm{harmless}}, \mathcal{D}_2 = \mathcal{D}_{\mathrm{helpful}}\) and uses \(\mathcal{L}_{\mathrm{MODPO}}\) on \(\mathcal{D}_2\) — this is sufficiently clear for readers familiar with the notation. (Rule: WEAKEN criticisms that reflect reading effort rather than genuine ambiguity.)

## Novel Insights

None beyond the paper's own contributions. The key insight — integrating linear scalarization into the DPO framework by expressing one objective's reward as a function of the policy and the other estimated rewards, then using a preference dataset to cancel the partition function — is the paper's own novel contribution, and the reviews do not surface an independent novel perspective beyond what the authors already provide.

## Suggestions

- Explicitly state in Section 4.1 how the boundary weights \(w=0\) and \(w=1\) are handled (e.g., using standard DPO on the single objective, or a small epsilon in the denominator). This single clarification would resolve the most substantive ambiguity in the experimental section.
- Qualify the abstract's "exact solutions" language with a brief caveat (e.g., "under known other-objective rewards") to match the precision of Section 3.1.
- Add an independent evaluation signal for the long-form QA experiments (even a small-scale human evaluation or held-out reward models trained on separate data) or clearly delineate the long-form QA results as supplementary evidence subject to the noted bias.

## Score and Decision

The paper presents a well-motivated, theoretically grounded, and practically efficient method for multi-objective alignment. The core contribution — extending DPO to multiple objectives via scalarization-integrated reward modeling — is novel and the efficiency advantage is clearly demonstrated. The weaknesses are all addressable: the division-by-zero ambiguity is a clarity gap, the evaluation bias in long-form QA is acknowledged and does not affect the synthetic experiments, and the abstract's over-precise phrasing is easily corrected. None of these issues threaten the paper's central claims.

**Score: 7.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>