Now I have enough calibration data. Let me construct the final review.

## Comparative calibration summary

**Round 1 — Bracketing:**
- Weak anchors (avg ≤ 3.5): Chess SAE (2.5, reject), RLHF reward model SAE (3.0, withdrawn), Sparling (3.0, reject) — papers with major novelty/presentation issues. The current paper is substantially stronger.
- Middle anchors (avg 3.5–7.5): Scaling Sparse Feature Circuits (5.0, reject), In-Context RL Suboptimal (5.75, reject), Rethinking SAE Eval (5.75, accept), Residual Stream MLSAE (6.5, accept), Principled SAE Eval (7.0, accept) — range of quality, from borderline to solid accepts.
- Strong anchors (avg ≥ 7.5): Sparse Feature Circuits (8.0, oral), Scaling SAEs (8.2, oral) — landmark interpretability papers.

**Round 1 bracket:** 5.0–7.0

**Round 2 — Narrowing:** Compared within (4.5, 6.5) and (5.5, 7.5):
- Current paper is clearly stronger than Scaling Sparse Feature Circuits (5.0, reject) — better experimental design, clearer causal evidence, multiple tasks
- Comparable to or slightly stronger than In-Context RL Suboptimal (5.75, reject) — more novel finding
- Comparable to Rethinking SAE Eval (5.75, accept) — similar quality but different contribution type
- Weaker than Residual Stream MLSAE (6.5, accept) — that paper had cleaner statistical practices; the current paper lacks CIs on several figures
- Weaker than Towards Principled SAE Eval (7.0, accept) — more rigorous evaluation framework

**Final score: 6.0.** The paper is a solid, well-executed empirical contribution with genuine novelty (TD learning from next-token prediction). The main limiting factor is the lack of statistical reporting on some results — confidence intervals and significance tests would push this higher. But the core finding is well-supported across multiple tasks with both correlational and causal evidence.

Here is the final consolidated review:

## Summary

This paper investigates whether Llama 3 70B implements temporal difference (TD) learning in-context when solving reinforcement learning problems. Across three tasks — a two-step MDP, a 5×5 grid world, and a graph structure learning task — the authors show that SAE features in the residual stream correlate with TD errors from external Q-learning and successor representation models. Crucially, lesioning (zero-ablating) these features causally impairs task performance and reduces the alignment of subsequent representations. The finding that a next-token-prediction model spontaneously learns a classic RL learning rule is genuinely interesting, and the paper establishes a useful methodology for studying in-context learning mechanisms with sparse autoencoders.

## Strengths

1. **Causal evidence from SAE feature lesioning.** In the Two-Step Task, deactivating a single SAE latent that correlates with TD error (r=0.58 in block 34) significantly reduces task returns and makes behavior less consistent with Q-learning, while lesioning the lowest-correlation feature does not (Fig 2E,F). Similar causal effects are shown in both the Grid World and Graph Learning tasks (Figs 4D, 6A). This goes beyond correlation to demonstrate functional necessity.

2. **Extension to reward-free structure learning via the Successor Representation.** The Graph Learning task (Section 5) is the most novel experiment: SAE features correlate more strongly with the Successor Representation (max r=0.62) and its TD errors (max r=0.60) than with the transition matrix (max r=0.49) or a log-likelihood surprise signal (max r=0.18). Lesioning a single TD latent in block 64 impairs next-state prediction accuracy (24.3% → 18.9%) and distorts the learned community structure. This shows the TD-like computation extends beyond reward prediction to general structure learning.

3. **Multiple control analyses confirm specificity.** The paper includes careful controls: (a) myopic (γ=0) Q-learning fits worse than full Q-learning (NLL 2864 vs 2729), (b) random-reward baselines in the Grid World isolate the role of reward integration (Fig 4A), and (c) control lesions (lowest-correlation features) produce minimal behavioral effects (Figs 2F, 4D). These controls substantially strengthen confidence that the discovered features are genuinely involved in TD computations.

4. **Scale dependence.** Llama 70B learns near-optimal policies while the 8B variant performs at chance (Fig 2A). This provides a concrete observation about when TD-like computations emerge with scale.

## Weaknesses

### Fatal

None.

### Major

1. **Missing statistical inference on key results.** The paper reports correlation values (e.g., r=0.58 in block 34) and behavioral differences (e.g., 24.3% → 18.9% in the graph task) without p-values, confidence intervals, or effect sizes. Figures 2C/D and 4B/C show line plots without any uncertainty estimates, making it impossible to assess whether the correlation peaks are significant relative to nearby blocks. Given that the central claims depend on these comparisons, this is a notable methodological gap. (Verified: Figs 2C/D show no error bars; cf. Fig 5 which does show 95% CIs — the inconsistency is itself a weakness.)

2. **Number of SAE features per block not reported; multiple comparisons unaddressed.** The paper does not state how many SAE latents were evaluated per block. If thousands of features were tested, a peak correlation of r=0.58 could arise by chance. Without this information, or correction for multiple comparisons, the significance of the reported correlations is unclear. (Verified by searching paper — not mentioned.)

### Minor

3. **Task-specific SAEs limit generality.** The SAEs are trained on activations from the same tasks they are evaluated on, so the discovered features may partly reflect the training distribution. The authors explicitly acknowledge this limitation ("our SAEs are task-specific and are not suitable for identifying RL-related variables for arbitrary tasks") but do not test whether similar TD features appear in general-purpose SAEs or across tasks. This does not invalidate the in-task findings but bounds the generality of the claim.

4. **Causal evidence is sparse.** The Two-Step Task lesions a single feature in one block (block 34); the Grid World lesions four features; the Graph Task lesions one feature. While sufficient to demonstrate that these specific features are causally involved, the evidence does not establish how many such features exist, whether they collectively form a circuit, or whether other features at similar correlation levels would be equally causal.

5. **Q-learning fitted parameters not reported.** The paper says Q-learning models were fitted to Llama's behavior but does not report the fitted parameters (discount factor γ, learning rate α). This makes it difficult to interpret the resulting TD error signals used for correlation analysis or to assess parameter sensitivity. (Verified: Section 3 mentions fitting but no parameters reported.)

6. **Scaling intervention is uncalibrated.** The negative scaling intervention (×-10) in Section 3 is described as "similar to Templeton et al. (2024)" but the choice of magnitude is not justified for this specific setting. A sweep over scaling factors would be more informative about the feature's functional form.

### Trivial

None.

## Nice-to-Haves

- **Circuit-level understanding.** The paper identifies TD-like features in the residual stream but does not trace how they are computed through attention heads or MLPs. Methods like path patching could reveal the circuits that produce these representations. (Acknowledged in Limitations.)
- **Cross-task generalization of SAE features.** Training SAEs on one task and testing whether the same features correlate with TD errors in another task would strongly support the claim that the model implements TD learning generally rather than learning task-specific representations.
- **Fitted Q-learning parameter reporting.** Reporting γ and α from the behavioral fits would improve reproducibility and allow readers to assess the sensitivity of the correlation results to parameter choices.

## Removed Points

These points were flagged for removal; treat them with caution if referenced elsewhere.

- **"Accuracy ceiling in graph task is low (25%)"** — Removed because the paper defines and shows the ceiling (solid horizontal line in Fig 5B) corresponding to the maximum achievable accuracy given the stochastic transitions of the random walk on the graph. This is not a flaw.
- **"No analysis of whether the model computes TD errors or merely represents them"** — Removed as a weakness because the lesion experiments demonstrate causal involvement (establishing functional necessity), and the authors explicitly acknowledge circuit-level understanding as future work.
- **"The control lesion in Section 3 is only one feature"** — Removed as a substantive weakness. The control is the lowest-correlation feature, which is a standard and valid control establishing specificity. The suggestion to lesion random features at the same correlation level is a reasonable extension but not a required control for the claims made.
- **"Choice of blocks (40 onwards) is post hoc"** — Removed as a weakness. Selecting blocks with high correlation peaks for intervention is standard practice in SAE interpretability work; the correlation peaks provide principled selection criteria.
- **"SAE features could be artifacts of training distribution"** — Weakened to Minor (weakness #3) because the paper acknowledges this limitation explicitly and proposes future directions for addressing it.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely reinforce the paper's framing rather than providing new analytical angles. The key tension in the reviews — between genuine appreciation for the causal methodology and concern about statistical rigor — is already internal to the paper's own presentation choices.

## Suggestions

1. Add error bars (bootstrap CIs or standard errors) to Figures 2C/D and 4B/C to allow readers to assess the reliability of the reported correlation peaks.
2. Report the total number of SAE features evaluated per block and discuss whether the maximum correlations survive multiple-testing correction.
3. Report the fitted Q-learning parameters (γ, α) for the behavioral model comparisons so readers can assess the sensitivity of the TD error signals used in correlation analyses.
4. Include a sweep over scaling magnitudes (e.g., −1, −5, −10) in the lesion experiments to better characterize how feature activity relates to behavior.

## Score and Decision

Based on calibration against human-reviewed anchors:

| Anchor paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Chess SAE | Wxl0JMgDoU.md | 2.5 | 1 | Much weaker — limited novelty, poor presentation |
| RLHF Reward Model SAE | bIb1xhSCVY.md | 3.0 | 1 | Much weaker — limited scope |
| Sparling | zgHamUBuuO.md | 3.0 | 1 | Much weaker — less relevant |
| Scaling Sparse Feature Circuits | Pa1vr1Prww.md | 5.0 | 1 | Weaker — narrower scope, less clean causal evidence |
| In-Context RL Suboptimal | FXJm5r17Q7.md | 5.75 | 2 | Comparable quality, current paper has more surprising finding |
| Rethinking SAE Eval | HpUs2EXjOl.md | 5.75 | 2 | Comparable quality, different contribution type |
| From Context to Concept | 0ULf242ApE.md | 6.0 | 3 | Similar quality, current paper has stronger causal evidence |
| Residual Stream MLSAE | XAjfjizaKs.md | 6.5 | 1 | Slightly stronger — cleaner statistical practices |
| Towards Principled SAE Eval | 1Njl73JKjB.md | 7.0 | 1 | Stronger — more rigorous evaluation framework |
| Efficient Dictionary Learning | k2ZVAzVeMP.md | 7.0 | 2 | Stronger — well-executed method paper |
| Sparse Feature Circuits | I4e82CIDxv.md | 8.0 | 1 | Significantly stronger — landmark paper |
| Scaling SAEs | tcsZt9ZNKD.md | 8.2 | 1 | Significantly stronger — landmark paper |

**Round 1 bracket:** 5.0–7.0.  
**Round 2 narrowing:** Compared to anchors in (4.5, 6.5) and (5.5, 7.5). The paper sits near the upper end of the middle band — better executed and with a more interesting finding than typical 5.x papers, but held back from 6.5+ by the statistical reporting gaps.

The paper is a genuinely interesting empirical contribution that delivers on its stated goals. The weaknesses are real but bounded: they concern presentation rigor rather than fatal methodological flaws. The core finding — that Llama 3 70B implements TD-like computations in-context, supported by both correlational and causal evidence across three tasks — is well-supported and should be of broad interest to the interpretability and in-context learning communities.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>