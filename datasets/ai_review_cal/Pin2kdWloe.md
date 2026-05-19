- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have verified all claims against the paper directly. Let me prepare the final consolidated review.

---

## Summary

This paper challenges the prevailing assumption in continual learning that the multitask objective (minimizing average loss over all seen tasks) is an optimal target. It formalizes the average lifelong error using concepts from online learning, proves for convex linear regression that a critical task duration exists beyond which a single-task (forgetful) agent outperforms a multitask agent, and validates these predictions empirically across supervised learning (CLEAR, MD5, Permuted-CIFAR) and reinforcement learning (ML10) benchmarks. The paper also demonstrates a Selective Replay method that switches objectives based on data-stream instability.

## Strengths

- **Theoretical proof of multitask suboptimality (Theorem 4):** The paper proves that for convex linear regression with positive instability, there exists a finite critical task duration \(\bar{h}\) beyond which the single-task agent achieves lower average lifelong error than the multitask agent. This formalizes the central claim that the multitask objective is not always optimal and is a clean, nontrivial theoretical contribution.

- **Empirical validation across diverse benchmarks (Table 1):** Results on CLEAR (smooth drift), MD5 (sharp semantic shifts), and ML10 (robotic RL) show that the best agent is data-dependent: ST outperforms MT on MD5 and ML10, while MT wins on CLEAR. This directly confirms the theory's prediction that optimality depends on the data stream's properties.

- **Controlled experiment isolating instability's effect (Figure 3):** The Permuted-CIFAR10 experiments demonstrate that increasing permutation size (higher instability) reduces the critical task duration, exactly as predicted. This provides causal evidence for the relationship between instability and the ST-vs-MT trade-off in a setting where the theory's assumptions are not strictly met, showing the framework's empirical reach.

- **Formalization of instability as an agent-independent measure:** The decomposition of \(\Delta_T\) into \(\Delta_T^{ST}\), \(\Delta_T^{MT}\), and \(\Delta_T^I\) (instability) provides a clean theoretical tool for analyzing non-stationarity in continual learning. The two proposed estimation options for non-convex settings, while coarse, are principled and yield consistent rankings across benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **The ML10 results (Table 2) do not follow the theoretical prediction that \(\Delta_T\) decreases with task duration \(h\).** The theory predicts that increasing \(h\) should monotonically reduce the gap between ST and MT. This holds on CLEAR but not on ML10. The paper attributes this to "the inherent noisiness of the reward signal" without any supporting analysis. This is a gap between theory and evidence that weakens the claim that the framework extends to reinforcement learning as cleanly as to supervised learning. While the main result (ST can beat MT, which is supported by the Table 1 ML10 results) is unaffected, a secondary but significant theoretical prediction is unconfirmed in the RL setting, and the offered explanation is an untested hypothesis rather than an analysis. This should be addressed with either additional experiments isolating the cause or a principled discussion of why the squared-loss theory may not transfer to reward-based metrics.

### Minor

- **The Selective Replay (SR) demonstration (Section 5.3) assumes a priori knowledge of when the instability regime changes.** The paper is transparent about this — it states that the switch point is known (permutation size increases from 16 to 32 at task 6) and explicitly frames online estimation as future work. However, the conclusion then says "we showed that one can easily modify a replay based method to take into account task similarity and be able to outperform the multitask agent." This slightly overstates the demonstration: what was shown is that *if* one knows the instability regime, one can switch to the better objective. The SR demo remains a useful illustration of the paper's thesis, but the "easily modify" phrasing should be tempered to reflect that an online instability estimator is still an open problem.

### Trivial
None.

## Nice-to-Haves

- **An online estimator of instability** would transform the SR demo from an illustration into a practical proof-of-concept. Even a simple heuristic based on gradient alignment or validation performance on a held-out subset would substantially strengthen the paper's constructive contribution.
- **A comparison of ST/MT agents against actual CL algorithms (e.g., EWC, ER, SI) on the same benchmarks** would help readers contextualize the magnitude of the observed effects relative to practical methods. This is not required for the core argument (the paper's contribution is analytical, not algorithmic), but it would broaden the paper's impact.
- **A deeper investigation of why ML10 diverges from theory** beyond a single hypothesis: e.g., whether the PPO optimization dynamics differ fundamentally from GD on squared loss, or whether the evaluation protocol (interleaving environment interaction with updates) introduces variance that masks the trend.

## Removed Points

These points were raised by reviewers but removed following the verification and filtering rules:

- **"Characterization of CL methods (dynamic architecture) as approximating the MT objective is overstated"** — The paper explicitly writes that dynamic architecture methods "do not seem to directly mimic the multitask objective" and says they are "akin to maximizing average performance under a fixed capacity constraint." This is a reasonable high-level characterization, not a strong claim the paper depends on. The critique misreads the qualified language.
- **Various formatting, typographical, and garbled-text complaints** — These are parser artifacts from the PDF-to-text extraction, not errors in the original submission.
- **"Missing comparison to CL algorithms"** — The paper's contribution is analytical (re-examining the multitask objective as an abstraction), not a new algorithmic state-of-the-art. Such a comparison is a nice-to-have extension, not a missing requirement.
- **"Missing related work"** — Cannot be verified without external sources.

## Novel Insights

Beyond the paper's own contributions, the most notable insight emerging from the reviews is that **the paper's core framework is subtly two-tiered**: it proves a strong formal result (Theorem 4, existence of \(\bar{h}\)) in the convex linear case, but the empirical story is more complex. The CLEAR and Permuted-CIFAR results neatly track the theory, while the ML10 results fail to confirm a secondary prediction yet still support the primary claim (ST beating MT on lifelong reward). This suggests that the theory's decomposition into \(\Delta_T^{ST}, \Delta_T^{MT}, \Delta_T^I\) may be a useful conceptual tool even in settings where its quantitative predictions do not all hold — a kind of "robustness to partial failure" that is worth highlighting as a meta-insight for the community.

## Suggestions

1. **Address the ML10 discrepancy directly** — either run a controlled experiment isolating why \(\Delta_T\) does not decay with \(h\) (e.g., is the metric itself too noisy? Does PPO's clipped objective break the convex-analysis assumptions?), or add a paragraph explicitly scoping the theory's applicability to RL settings with a clear argument for why the squared-loss analysis may not transfer.
2. **Temper the "easily modify" claim** in the conclusion (line 190) to better reflect that the SR demo assumed knowledge of instability and that online estimation remains open.
3. **Add a brief discussion** of why Option 1 for estimating instability can be negative and why this does not invalidate its use as a relative measure (currently only briefly mentioned).
4. **Consider adding an explicit scope statement** clarifying that the paper's critique of the MT objective is aimed at the *goal* of minimizing forgetting as a universal target, rather than at specific CL algorithms — this would sidestep the need to argue that all methods approximate the MT objective.
