## Summary

MoE-F proposes a stochastic-filtering-based gating mechanism for dynamically combining pre-trained LLMs in online time-series prediction. The key idea is to frame expert selection as a finite-state continuous-time HMM and use the Wonham-Shiryaev filter to derive per-expert optimal estimates (in the L² sense) of which expert is best at each time step, then aggregate these estimates via a Gibbs/smooth-softmin weighting and heuristically update the HMM's transition rate matrix. Experiments on a financial market movement dataset (NIFTY, 317 test samples) show a 17% absolute F1 improvement over the best individual LLM.

## Strengths

- **Novel framing of MoE gating as a stochastic filtering problem.** Casting online expert combination as a finite-state HMM and applying the Wonham-Shiryaev filter is a fresh perspective that differs from static learned routing (Switch Transformer, Mixtral) and from static Gibbs-posterior aggregation in the Bayesian MoE literature. The paper correctly identifies that closed-form finite-dimensional filters exist for this discrete-state, univariate-observation structure (Sec. 3, Related Work), making the approach computationally attractive.

- **Theorem 1 provides genuinely optimal per-expert belief updates.** Theorem 1 derives the exact SDE for each expert's conditional distribution of the masking process \(w_t\), given only that expert's running loss. The L² optimality claim for this step is standard filtering theory correctly applied, not an overstatement. The closed-form nature of the filter (no Monte Carlo sampling needed per expert) is a meaningful practical advantage.

- **The perturbation scheme (Propositions 1–2) is cleanly justified.** The trick of perturbing the rank-1 transition matrix \(P_t\) to \(P_t^\alpha = (1-\alpha)P_t + \alpha I_N\) to ensure invertibility and thus a well-defined matrix logarithm is mathematically sound, and Proposition 2's KL-bound quantifies the cost of this perturbation. This provides formal support for Step 3's mathematical validity, even if its predictive benefit is not established.

- **Consistent outperformance over individual experts across two expert pools.** MoE-F beats every single expert in Tables 1 and 2 (main set of 7 SOTA LLMs; Llama-2/3 family with LoRA variants). Table 3's class-wise breakdown provides granular evidence that the dynamic gating leverages complementary per-label strengths (e.g., boosting Neutral-class F1 from 0.49→0.56 in the Llama-3 pool).

## Weaknesses

### Fatal
None. The paper's core theoretical contribution (Theorem 1) is mathematically sound, and the central idea of filtering-based gating is not invalidated by any single error.

### Major

- **No ensemble or simple-aggregation baselines — the filtering mechanism's contribution is unidentifiable.** The only comparisons are against individual LLM experts. No uniform-weight ensemble, no exponential weighted average (EWA), no Hedge, no simple Bayesian update baseline is tested. Because the final MoE-F prediction (Step 2) is a softmin over recent scores — itself a standard aggregation method — the 17% absolute F1 gain could plausibly arise entirely from that ensembling step, with the parallel filters (Step 1) and the Q-update (Step 3) contributing little or nothing. This is a fundamental experimental design gap. An ablation replacing Steps 1 and 3 with e.g. uniform weights or an exponentially weighted average over expert scores is needed to isolate the filtering mechanism's value.

- **Evaluation is limited to one dataset (NIFTY, 317 test samples) without variance reporting.** The main results (Table 1) report means over 3 runs but no standard deviations, confidence intervals, or significance tests. With 317 samples and a "mean over 3 seeds," the stability of the 17% improvement is unclear. The ablation (Table 2) uses the same test split. The paper's claims about general applicability to other time-series tasks (regression, other asset classes, general LLM benchmarks) are unsupported by evidence.

- **The claim that Theorem 1 "optimizes a lower bound for the expected performance" of the Q-update (line 68) is inconsistent with the paper's content.** Theorem 1 provides the filtering SDE and says nothing about Q-updates or lower bounds. The paper contains no theorem establishing such a bound. This is not a minor cross-reference error — it overstates what is actually proven.

### Minor

- **Step 3 (Q-update) is heuristic and not ablated.** The "follow-the-leader" transition-matrix update is acknowledged as heuristic, and Propositions 1–2 only guarantee the perturbation is mathematically well-behaved (invertible, KL-bounded). There is no evidence that this step improves predictive performance over fixing \(Q\) (e.g., to the identity). An ablation comparing MoE-F with and without adaptive Q would clarify whether this complexity is warranted.

- **The paper's language overclaims optimality of the overall algorithm.** The abstract says "theoretical optimality guarantees of the proposed filtering-based gating algorithm" and the conclusion says "the components of our algorithm satisfy several optimality guarantees." In reality, only the per-expert filtering equations (Theorem 1) have an optimality guarantee; the softmin aggregation (Step 2) and the Q-update (Step 3) are standard heuristics. This mismatch between what is claimed and what is proved should be corrected.

- **Hyperparameter sensitivity unreported.** The algorithm has at least three hyperparameters (\(\lambda\) for the Gibbs temperature, \(\alpha\) for the perturbation, discretization step size \(\Delta\)) whose impact on results is not analyzed. Given the small test set, sensitivity to these choices matters.

### Trivial
None of substance — the paper's presentation is adequate.

## Nice-to-Haves

- An ablation testing MoE-F with only Steps 1+2 (skip the Q-update, keep \(Q\) fixed) to isolate Step 3's contribution.
- An error analysis comparing the Euler-Maruyama discretization of the filter to a finer discretization, to confirm discretization error is negligible.
- Reporting standard deviations or confidence intervals for the 3-run means.

## Removed Points

These points were flagged by reviewers but are removed or weakened:

- **"Theorem 1's SDE uses terms that depend on π itself, so it is not closed-form."** This reflects a misunderstanding of stochastic filtering. The innovation term \(\bar{A}\) depends on the filter's own estimate — this is standard in the Wonham-Shiryaev filter and does not break the closed-form property. The SDE is an explicit function of \(\pi_t^{(n)}\) and the observations, which is what "closed-form" means in the filtering literature.
- **"The 'innovations process' is defined using the filter's own prediction — self-referential."** Same point as above. This is how all continuous-time filters work; it is not a weakness.
- **"No proof of Theorem 1."** Theorem 1 is a direct application of the Wonham-Shiryaev filter to the specific observation model. A full proof would reproduce standard textbook material (cited in the paper). Missing a dedicated proof section is acceptable for a conference paper.
- **"Missing related work on online expert aggregation."** The reviewer's claim cannot be independently verified. The paper cites relevant references for Gibbs aggregation (Andrychowicz et al., Rothfuss et al.).
- **"Missing appendix / missing proofs."** The parser strips appendix material. This is not an author error.
- **"Cannot attribute reported gains to filtering mechanism."** This is kept as a Major weakness above, but note that the critic's phrasing that gains "could be entirely due to that step" is framed as an attack on attribution, not as factual error — this concern is genuine and is retained.
- **Strength Finder's generic strengths removed.** Several strengths from the Strength Finder ("addressed an important problem," "well-motivated," "plug-and-play harness") are too generic or conflict with verified weaknesses and are not included.

## Novel Insights

A genuinely novel observation emerges by reading across the critic's critique and the paper together: the MoE-F algorithm has a theoretically elegant core (the Wonham-Shiryaev filter giving L²-optimal per-expert beliefs) encased in two layers of heuristic (Gibbs aggregation + ad-hoc Q-update) that are themselves standard tools from separate literatures. The paper never cleanly separates "what the theory guarantees" from "what the heuristics add." The most valuable contribution may not be the overall empirical results (which are confounded) but rather the formal demonstration that the expert-selection-as-HMM framing yields tractable filtering equations — a conceptual contribution that could inspire theoretically cleaner aggregation schemes. Conversely, the weakest part of the paper is the experimental evaluation, which treats the entire pipeline as a black box and thus cannot speak to whether the filtering step — the paper's advertised novelty — actually helps.

## Suggestions

1. **Run the ablations that actually isolate the filtering component.** Add two baselines: (a) a uniform-weighted ensemble of expert predictions, (b) an exponentially weighted average of recent expert scores (EWA) with the same softmin structure but without the parallel filters. If MoE-F beats these, the filtering step's contribution is substantiated. If not, the novelty rests entirely on the conceptual framing.
2. **Fix the mismatch between Theorem 1 and the claimed lower-bound guarantee.** Either add the missing theorem that establishes the bound, or correct the contribution statement.
3. **Ablate Step 3** by fixing \(Q\) (e.g., to identity or constant transition rates) and comparing to the full MoE-F.
4. **Report variance** for the 3-run means in Tables 1–3, or run more seeds.
5. **Test on at least one additional dataset** (e.g., a regression task or a different asset class) to support the generalizability claim.
6. **Tone down the optimality language** for the overall algorithm; reserve "optimal" for Theorem 1 and describe Steps 2–3 as heuristic or standard subroutines.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>