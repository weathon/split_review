Now I'll produce the final consolidated review.

---

## Summary

The paper proposes COMBO, a framework for embodied multi-agent cooperation that factorizes joint actions into per-agent components via a compositional video diffusion model, then combines this world model with VLM-based planning sub-modules (Action Proposer, Intent Tracker, Outcome Evaluator) in a tree search procedure for online cooperative planning. The core idea — compositional score composition for multi-agent video prediction — is conceptually clean and addresses a genuine gap in prior single-agent video prediction work. Experiments are conducted on two new TDW-based tasks (TDW-Game and TDW-Cook) with 2–4 agents.

## Strengths

- **Compositional factorization is a well-motivated technical contribution.** The two-stage training procedure (first single-agent action conditioning, then fine-tuning on composed actions) is principled, and the 4→3 agent generalization result (Table 3: 100% success rate, 15.0 avg steps vs Oracle 13.5) provides concrete evidence that composable score functions enable handling unseen agent counts — a capability no prior baseline offers.

- **ADLS (Agent-Dependent Loss Scaling) yields demonstrable accuracy gains.** Table 2 shows COMBO w/o ADLS drops from 95%→70% (Single) and 75%→55% (Multiple) on TDW-Game video prediction — a large, meaningful margin that validates the technique.

- **Intent Tracker module provides measurable cooperation improvements.** Table 1 shows removing it reduces success rate from 1.0 to 0.7–0.9 in several settings and increases average steps, confirming that explicit intent inference aids cooperative planning.

- **Thoughtful evaluation design against opposing cooperator policies.** Testing each agent against two deliberately contrasting partner policies (clockwise/counter-clockwise in TDW-Game, selfish/altruism in TDW-Cook) demonstrates robustness beyond a single interaction pattern.

## Weaknesses

### Fatal
None.

### Major
- **Evaluation scale is too small to support the quantitative claims.** All main results (Tables 1, 3) are reported over only **10 episodes** per condition. With binary success/failure outcomes, a 10/10 success rate has a 95% CI extending as low as ~69%. Observed differences such as COMBO (100%) vs. CoELA (80%) or LLaVA (90%) are not statistically meaningful. The average-steps metric is computed on an even smaller subsample (successful episodes only). Tellingly, COMBO *outperforms the Oracle* on TDW-Cook Agent 1 (21.3 vs 23.4 steps) — with 10 episodes this is readily explained by noise, yet presented uncritically. **No confidence intervals, standard deviations, or significance tests are reported anywhere.** This significantly undermines the strength of the paper's empirical foundation.

- **Missing critical ablation: compositional vs. non-compositional multi-agent world model.** The paper's central claim is that *compositional factorization* of joint actions enables accurate multi-agent video prediction. Yet Table 2 compares COMBO's CWM only against AVDC, which is a single-agent video diffusion model not designed for multi-agent prediction (achieving 20–25% on the "Multiple" metric by construction). The informative comparison would be against a multi-agent video diffusion model trained on full joint-action conditions *without* compositional factorization, keeping architecture and training data identical. Without this ablation, the observed gains cannot be attributed to the compositional factorization — they could arise from any architectural difference or the two-stage training procedure itself.

- **Several system components are not individually ablated.** The system has multiple modules (world state inpainting, tree search with three parameters, Outcome Evaluator) whose individual contributions are not assessed. The compute-budget experiment (Table 3 with 5 episodes) confounds P, B, and D simultaneously, so we cannot tell which dimension matters most or whether the tree search outperforms greedy single-step planning.

### Minor
- **"Arbitrary number of agents" claim overreaches the evidence.** This phrase appears in the abstract, contributions list, and conclusion, but the only supporting experiment is generalization from 4→3 agents (decrement of 1 in one direction). Extrapolating to *arbitrary* counts is not justified by this evidence. The demonstration is interesting and non-trivial, but the claim should be qualified.

- **Zero-performance baselines are not informative.** MAPPO and Recurrent World Models achieve 0% across all conditions. While the paper attributes this to task difficulty, well-known methods flatlining entirely suggests a mismatch (observation encoding, hyperparameter tuning) that should be investigated or acknowledged more directly. These baselines provide no useful signal.

- **ADLS reachable-region computation is underspecified.** The paper states the loss coefficient matrix is "set based on each agent's reachable region in the image" (Sec. 4.2) without describing how this region is determined. If this requires ground-truth agent positions or kinematics, it is a non-trivial supervision requirement that should be discussed.

- **Human evaluation lacks methodological detail.** The video quality evaluation (Table 2, 20 samples per condition) does not report number of evaluators, blinding condition, or inter-rater agreement.

### Trivial
- The Outcome Evaluator's exploitation-mitigation threshold (Sec. 5) is described without detail on how it is set or how sensitive results are to its value.

## Nice-to-Haves
- Report wall-clock planning time, as the paper identifies slow inference as a limitation.
- Provide confidence intervals or bootstrapped standard errors for all quantitative results.
- Include an ablation of the world state inpainting module.

## Removed Points

These points from the source reviews were removed or demoted based on the filtering rules:

- **"AVDC comparison is staged"** — The observation that AVDC is a single-agent model is factually correct, but this criticism is fully subsumed by the missing-ablation weakness above (compositional vs. non-compositional multi-agent model). Kept as a merged concern.
- **Strength #5 (artifact exploitation mitigation)** — Described in one sentence without evaluation; insufficient evidence to count as a strength.
- **Generic strength claims about problem importance** from the Strength Finder — removed as not specific to this paper's content.
- **"Strengthening the Paper on Its Own Terms" items** (scale to 50–100 episodes, tune baselines) — These are reasonable but covered by the weaknesses above.
- **Vague criticisms about "the evaluation lacks rigor"** without concrete anchors — removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The compositional factorization idea is the paper's genuine novelty; the reviews do not surface an insight the paper itself does not already articulate.

## Suggestions

1. **Add the critical ablation**: Train a multi-agent video diffusion model on full joint-action conditions *without* compositional factorization (same architecture, same data) and compare on both video-prediction accuracy (Table 2 metrics) and downstream planning (Table 1). This directly tests whether the compositional factorization specifically causes the observed improvement.
2. **Scale evaluation to at least 50 episodes per condition** and report confidence intervals or bootstrapped standard errors for all metrics.
3. **Qualify the "arbitrary number of agents" claim** to match the evidence, and ideally add experiments with 5+ agents or provide a formal compositional argument.
4. **Provide details on ADLS reachable-region computation** and whether it requires privileged information.
5. **Ablate tree search parameters independently** rather than confounding P, B, and D.
6. **Report human evaluation methodology** (number of evaluators, blinding, inter-rater agreement).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>