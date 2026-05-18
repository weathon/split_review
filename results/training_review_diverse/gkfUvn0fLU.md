Now I have thoroughly verified the paper content against all reviewer claims. Let me compile the final review.

---

## Summary

This paper studies reward model overoptimization in *composite* reward functions (e.g., METEOR + intent score), where the interaction between component RMs shifts the points at which each ceases to be a useful proxy. It proposes identifying these "proxy points" and then using constrained RL (CMDPs with Lagrangian relaxation) to keep each component RM at or below its proxy point, with dynamic weights emerging naturally from Lagrange multipliers. A derivative-free variant (NM-PPO) allows threshold identification within a single training run. Experiments on DailyDialog with GPT-2 and two component RMs show that the constrained methods (μ-PPO, ξ-PPO) outperform fixed-weight PPO baselines and are more robust to extended training.

---

## Strengths

- **First systematic analysis of overoptimization in composite RMs.** The paper explicitly studies how correlation between component RMs (METEOR and intent) shifts the joint proxy point relative to independent optimization (Figure 3/Fig:correlated). This is a genuine contribution — prior work focused on single-RM overoptimization (Gao et al., 2022).

- **Principled constrained RL formulation with dynamic weights.** Using CMDPs and Lagrangian relaxation elegantly avoids manual hyperparameter tuning of fixed component weights. The Lagrange multipliers automatically adjust the influence of each RM during training. The paper shows that μ-PPO and ξ-PPO achieve higher evaluation scores than PPO with optimally tuned fixed weights (Figure 4/Fig:eval_all, left), and that robustness to longer training is improved (Figure 4, right).

- **Empirical verification of constraint satisfaction.** Figure 5 (Fig:constraint_satisfaction) separately validates that μ-PPO reaches/exceeds thresholds, All-PPO stays below them, and ξ-PPO hits them approximately — confirming the algorithms enforce the intended constraints, not just that evaluation scores improve.

- **NM-PPO for single-run threshold search.** The Nelder-Mead variant dynamically updates proxy point candidates during a single run, reducing compute compared to the multi-run surface-fitting approach. Figure 7 (Fig:nm) shows NM-PPO achieves strong evaluation performance, and the simplex trajectories converge to a local maximum of the evaluation surface.

- **Practical modifications with clear rationale.** The sigmoid bounding of Lagrange multipliers (keeping them in [0,1]), low-momentum SGD updates, and using return-to-go instead of early value estimates are motivated by specific instability issues. These are transparent engineering choices that address known problems in primal-dual RL.

---

## Weaknesses

### Fatal
None.

### Major

1. **Proxy point identification procedure is insufficiently specified for the multi-run approach.** The paper's main experiments (Figure 4) use proxy points identified by "fitting a surface" to data from multiple runs and taking its maximum. However, the paper never specifies: (a) what type of surface was fitted (quadratic? spline? local regression?), (b) how many data points were used, (c) any measure of fit quality, or (d) how the maximum of the fitted surface is algorithmically located. These are not minor implementation details — the entire constrained method uses these thresholds as constraints. Without a clear, repeatable procedure, the results from the multi-run approach cannot be reproduced, and the method cannot be confidently applied to new domains. The NM-PPO variant avoids this issue, but the central experimental results (Figure 4) depend on the underspecified surface fitting.

2. **No empirical comparison against early stopping as a baseline for overoptimization avoidance.** The paper mentions early stopping (Section 1, "Worse, early stopping to avoid overoptimization in composite RMs is problematic") but never compares against it experimentally. Early stopping, monitored via the ground-truth evaluation metric, is the most straightforward baseline for avoiding overoptimization. The paper's constrained methods claim to be "more robust to longer training time" (Figure 4, right), but early stopping is by definition robust to training duration because it stops. Without this comparison, it is difficult to assess whether the constrained approach offers a practical advantage over simply monitoring the gold standard and stopping at the right point — especially since both approaches require periodic access to ground-truth evaluation.

### Minor

1. **NM-PPO computational savings are not fully substantiated.** The paper allows NM-PPO "twice as many training steps for a single run" (256,000) compared to baselines, and each threshold update triggers a new ξ-PPO run from scratch. Meanwhile, ξ-PPO itself required 10 runs to find proxy points via surface fitting. The total environment interactions for NM-PPO versus the full pipeline (10 runs of PPO + ξ-PPO runs) are not clearly accounted for. The caveat that the feasible region for thresholds is "relatively small" (Section 5.1) also tempers how much the result generalizes.

2. **Practical modifications are not ablated.** The paper describes sigmoid-bounded multipliers, low-momentum SGD updates, and return-to-go value estimates as important for stability, even calling them "hacks" (Section 4). However, no ablation study disambiguates which modifications are essential. This makes it unclear whether the "vanilla" constrained formulation would work without these additions, weakening the claim of a clean theoretical framing.

3. **The Lagrange multiplier bounds assume optimal weighting is a convex combination.** Constraining Lagrange multipliers to [0,1] via sigmoid (Section 4) implicitly assumes the optimal weighting of task vs. constraint rewards lies in [0,1] — i.e., the optimal Lagrange multipliers form a convex combination. The paper does not discuss whether this assumption could be violated or what would happen if the optimal multipliers fell outside this range.

### Trivial

- The paper uses "proxy point" for both the value at which a single RM peaks (Figure 1) and the joint maximum of the fitted surface (Figure 2). These are related but distinct quantities; a terminological distinction (e.g., "independent proxy point" vs. "joint proxy point") would improve clarity.

---

## Nice-to-Haves

- An ablation study isolating the effects of sigmoid bounding, low momentum, and return-to-go would help practitioners understand which modifications are essential.
- A finer-grained sensitivity analysis around proxy point thresholds (e.g., ±5%) beyond the ±10% test in Figure 5 would strengthen claims about the method's robustness to threshold misspecification.

---

## Removed Points

These points were removed from the harsh critic's review for the reasons below:

- **"Missing adaptive KL control baseline"** — REMOVED (factually wrong). The paper's PPO baseline already uses adaptive KL control (Section 2, line 63: "The coefficient α_t^KL effectively acts as a Lagrange multiplier, increasing if the KL exceeds some threshold and decreasing otherwise"). This is the standard adaptive KL baseline from the RLHF literature.
- **"Proxy points found without KL may not transfer to constrained training regime"** — DOWNGRADED to Nice-to-Have. The paper explicitly tests this concern in Figure 5 (right) by comparing correlated (from the surface fit, which accounts for interaction effects) vs. independent proxy points, showing correlated ones work better. The main experiments use the correlated points, so this is partially addressed.
- **"Theoretical guarantees section notes only averaged iterates converge, raising questions about neural policies"** — DOWNGRADED. The paper is honest about this limitation in Section 4 ("Formal Guarantees") and describes what existing theory provides. This is a known property of primal-dual policy optimization; holding it against the paper as a weakness would be penalizing it for a limitation it transparently acknowledges. The paper is primarily empirical.
- **"Surface-fitting approach only used to produce thresholds but details are absent"** — Already captured in Major Weakness #1 above (merged for conciseness).
- **"The paper does not ablate these modifications"** — Already captured in Minor Weakness #2 above.
- **"Paper's practical improvements presented as hacks suggests fragility"** — The paper uses the word "hack" once informally (line 147). This is transparent reporting, not a confession of fragility. The concern about missing ablation is already captured in Minor Weakness #2.

---

## Novel Insights

The reviews collectively surface an important tension: the paper's core conceptual contribution (using proxy points as CMDP constraints with learned Lagrange multipliers) is elegant and well-motivated, but the empirical instantiation relies on a proxy point identification step whose details remain opaque. The harsh critic rightly identifies this as the method's linchpin, but undercounts how the NM-PPO variant side-steps the issue by finding thresholds online. The more subtle insight from cross-referencing the two reviews is that the paper actually offers *two* contributions — (1) the constrained RLHF formulation and (2) a method for finding thresholds — and the strength of evidence for each is asymmetric: (1) is well-supported experimentally, while (2) is well-described only for NM-PPO but not for the multi-run surface fitting it replaces. A revised version that either specifies the surface fitting or relies entirely on the NM-PPO approach would be significantly stronger.

---

## Suggestions

1. **Specify the surface fitting procedure in full.** Provide the model class (e.g., quadratic, RBF, local regression), the loss function, the number of data points, the number of runs used, and any cross-validation. Alternatively, if the surface fitting is not central to the contribution, consider pivoting the main experiments to use NM-PPO thresholds, which are described in detail.
2. **Add an early stopping baseline.** For each fixed-weight PPO run, identify the evaluation peak and report both the peak value and the steps required. Compare against the constrained methods' performance and training length.
3. **Add an ablation study** of the sigmoid bounding, low momentum, and return-to-go modifications to clarify which are essential.
4. **Introduce distinct terminology** for independent vs. joint proxy points to avoid confusion.

---

## Score and Decision

**Originality:** Good — this is the first study of overoptimization in composite RMs and the constrained RLHF formulation is novel.  
**Importance of question:** High — composite RMs are increasingly standard in LLM alignment.  
**Claims supported:** Partially. The constrained methods outperform fixed-weight PPO, but the proxy point identification procedure is underspecified, weakening reproducibility.  
**Soundness of experiments:** Adequate within the single domain tested, but missing an early stopping baseline.  
**Clarity of writing:** Clear, well-structured, with a helpful table summarizing methods.  
**Value to community:** Real. The conceptual framework (proxy points + CMDP constraints) is likely to influence future work on multi-faceted alignment.

The paper has a real and timely contribution, and its main experimental results are plausible and well-presented. However, the insufficiently specified proxy point identification procedure is a genuine reproducibility gap for the multi-run approach that underpins the central results. With the surface fitting details clarified or the main experiments pivoted to NM-PPO, and with an early stopping baseline added, the paper would be significantly stronger.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>