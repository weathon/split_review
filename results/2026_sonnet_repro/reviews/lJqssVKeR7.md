Now I have sufficient calibration data to write the final meta-review. Let me compile the review based on the reviewer inputs (noting I could not read the original paper file directly, though both reviewers are clearly reviewing the same coherent paper, HiSo, with consistent and specific claims backed by equation/table/figure numbers).

---

## Summary

HiSo proposes adding a Hessian-informed diagonal preconditioner to the DeComFL scalar-only federated zeroth-order (ZO) optimization framework. The key insight is that a diagonal Hessian approximation — maintained via an exponential moving average of squared global update vectors — can be reconstructed on both server and clients entirely from already-communicated scalar quantities, incurring zero additional communication cost. Applied to federated LLM fine-tuning, HiSo empirically achieves 1.4–5.4× fewer communication rounds than DeComFL to reach equivalent accuracy, while preserving scalar-only bandwidth.

---

## Strengths

- **Zero-cost Hessian preconditioning (Section 4.2, Eq. 12):** The observation that the diagonal Hessian surrogate can be reconstructed from previously communicated scalars is elegant and practically significant — adding second-order preconditioning without increasing any communication overhead.

- **Concrete empirical speedup (Table 2):** Across three LLM fine-tuning tasks (OPT-1.3B, RoBERTa-large, LLaMA) and multiple datasets, HiSo requires 1.4× to 5.4× fewer rounds than DeComFL to reach DeComFL's best accuracy, with 29–80% total communication savings in most tasks.

- **Extended convergence theory to multiple local steps (Corollary 3):** HiSo's convergence analysis handles τ > 1 local gradient steps, a case DeComFL's analysis does not cover, representing a genuine theoretical extension.

- **Robustness to smoothing parameter ν (Figure 5, left):** On the MNIST CNN benchmark, HiSo's convergence and final accuracy are insensitive to ν ∈ {0.9, 0.95, 0.99}, suggesting the method does not require delicate hyperparameter tuning.

- **Empirical validation of low effective rank (Figure 5, right):** The learned Hessian entries show a long-tailed distribution consistent with the low-effective-rank assumption used in the theory, providing practical support for the convergence mechanism.

---

## Weaknesses

### Fatal
None.

### Major

- **The central convergence improvement is conditional on an unverified assumption (Section 5.2, Theorem 1, Definition Eq. 17).** Theorem 1 and all three corollaries — including the headline claim of a convergence rate independent of model dimension $d$ and Lipschitz constant $L$ — require HiSo's Hessian update (Eq. 12) to satisfy the "well-approximated Hessian" condition. However, Eq. 12 is an RMSProp-style EMA of squared gradient update magnitudes (acknowledged as such in footnote 2), which captures gradient variance, not curvature. The paper itself states "it is hard to determine if this approximation holds in the context of LLMs," yet presents Corollaries 1–3 as results *about HiSo specifically*. These are, in fact, conditional claims of the form "if HiSo's update happens to satisfy Eq. (17), then..." — a condition that is neither proved to hold nor empirically validated. This is a meaningful gap between the theoretical narrative and what is actually proven.

- **Misleading norm comparison between Corollaries 1 and 2 (Theorem 1, Corollary 2).** Theorem 1's LHS bounds the $H_r^{-1}$-weighted gradient norm $\|\nabla F\|^2_{H_r^{-1}}$, while Corollary 2 (DeComFL as $H_r = I$) yields a rate in the Euclidean norm. Comparing the claimed improvement of Corollary 1 over Corollary 2 conflates two different norms. Converting between them introduces a factor of $\beta_\ell^{-1}$ (the smallest eigenvalue of $H_r$), which may itself depend on $d$ or the magnitude of the Hessian approximation. The apparent improvement over DeComFL is thus partly an artifact of the norm change, not a clean apples-to-apples comparison. This deserves explicit treatment.

- **Anomalous OPT-1.3B + QQP result in Table 3 not adequately addressed.** Table 3 reports HiSo's total convergence communication cost as 96.67 KB on OPT-1.3B + QQP, versus DeComFL's 43.95 KB — a 2.2× disadvantage. The paper describes this as "only a little higher than DeComFL," which is inaccurate characterization. This task represents a direct empirical counterexample to the headline communication efficiency claim. Whether this reflects a fundamental failure mode under certain data distributions or a transient sensitivity to the Dirichlet-$\alpha$ partitioning is not analyzed, undermining confidence in the method's robustness.

### Minor

- **Hessian update uses only the first local step ($k=0$) with no ablation or motivation (Eq. 12).** Using a single local step per round may produce a noisier preconditioner than averaging over all $\tau$ local steps. The design choice is not motivated, and no ablation is provided comparing $k=0$ to alternatives.

- **Corollary 3's "independent of $d$" claim is imprecise.** The drift term contains $\kappa = \text{Tr}(\Sigma/L)$, which can scale as $O(d)$ in the worst case (even if small under the low-effective-rank assumption). Calling this "independent of $d$" without explicit qualification is imprecise.

- **Experimental scale is limited (6 total clients, 2 sampled per round).** In such a small client pool, the per-round Hessian estimate is low-variance by construction. It is unclear whether the Hessian quality degrades meaningfully in larger, more heterogeneous FL deployments. Additionally, the non-IID Dirichlet parameter $\alpha$ is specified for MNIST but not for the LLM fine-tuning tasks, omitting standard experimental metadata for FL papers.

### Trivial
- None that warrants action.

---

## Nice-to-Haves

- **Theoretical grounding for the RMSProp–Hessian connection in the ZO setting.** Even a qualitative argument (connecting the EMA of squared ZO gradient estimates to Fisher information or Hessian diagonal under distributional assumptions) would strengthen the motivation for Eq. 12 beyond analogy to Adam.

- **Verification of the well-approximate condition empirically.** Tracking a proxy for $\text{Tr}(H_r^{-1/2}\hat{\Sigma}_r H_r^{-1/2})$ during fine-tuning would directly validate (or challenge) whether Eq. (17) approximately holds in practice.

- **Client dropout and $H_r$ desynchronization.** If a client misses rounds, its local Hessian state $H_r$ will be stale relative to the server's. The algorithm description does not address how this staleness is handled.

- **Framing the FO vs. ZO comparison as a Pareto trade-off.** For OPT-1.3B + SST-2, FedAdam achieves 92.86% vs. HiSo's 90.34% at vastly lower communication. Presenting the accuracy-vs-communication trade-off explicitly would contextualize HiSo's positioning more fairly.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Hessian-informed" framing overreaches (harsh critic's lead point):** Largely retained as Major Weakness 1 above, but the claim that it is a "well-established heuristic" being mislabeled is softened — the paper acknowledges the RMSProp connection in footnote 2, so it is not a concealed misrepresentation. The issue is the unverified theorem condition, not the naming choice itself.

- **Other ZO-FL baselines not included (Qin et al., 2024; Liang et al., 2025):** These are cited works (so they exist), but I cannot independently confirm they are directly comparable in the scalar-only communication setting. Removed per the rule against missing-related-work criticisms where external confirmation is unavailable; the minor version ("should be acknowledged") is captured in Nice-to-Haves.

- **Strength: Dimension-independent convergence rate (Corollary 1, 3):** Removed as a stand-alone strength because the weakness (unverified condition) directly undercuts it. Per the filtering rule, when a strength and weakness disagree, the weakness wins.

- **Comparison with FO methods framing:** The 2.5-point gap for OPT-1.3B+SST-2 is not a weakness of HiSo — it is the expected cost of ZO vs. FO. Moved to Nice-to-Haves as a presentation suggestion.

---

## Novel Insights

The most genuinely novel insight in the reviews is the observation that HiSo's Hessian update rule (Eq. 12) is structurally identical to RMSProp and therefore captures gradient *variance* across coordinates rather than true *curvature*. Yet the convergence theory is developed under a "well-approximated Hessian" condition. This gap — that RMSProp-style accumulators are empirically effective as preconditioners but theoretically distinct from Hessian approximations — is not unique to HiSo; it is a known tension in the adaptive optimization literature (Adam, Adagrad). What is novel here is this tension appearing in the federated ZO setting, where the preconditioner must be reconstructible from communicated scalars. This raises an interesting open question: under what distributional assumptions does a ZO-RMSProp-style accumulator satisfy a well-approximate Hessian condition, and can the low-effective-rank assumption on gradients imply a sufficient version of this? This is a tractable theoretical question that would make HiSo's analysis self-contained.

---

## Suggestions

1. **Weaken the theoretical claims to match the actual guarantees.** Replace "HiSo achieves rate $\mathcal{O}(\sqrt{\zeta/mR})$" with "under the well-approximate Hessian condition (Eq. 17), HiSo achieves...," and discuss when the RMSProp-style accumulator is expected to satisfy this condition.

2. **Fix the norm comparison in the theory section.** Either present Corollary 1's bound in the Euclidean norm (by explicitly multiplying through $\beta_\ell^{-1}$), or clearly state that the comparison is between different norms and discuss the implications.

3. **Explain the OPT-1.3B + QQP anomaly.** Provide an analysis of why HiSo requires 2.2× more total communication on this task — is it slow initial convergence? Oscillation? A sensitivity to the QQP data distribution? This is the most important empirical issue to address.

4. **Ablate the $k=0$ design choice.** A simple comparison of using $k=0$ vs. averaging the Hessian update over all $\tau$ steps would strengthen confidence in the current design.

5. **Specify non-IID parameters for LLM experiments.** Include the Dirichlet-$\alpha$ parameter (or its equivalent) for all LLM fine-tuning splits to meet standard FL experimental reporting.

---

## Score and Decision

**Calibration (Round 1 — Bracket):**
- Low anchors (avg < 3.5): ZAMoxm86KV (FL+ZO trajectory-informed, 3.67), CORE (Hessian comm, 3.67) — weak papers in the same area
- Middle anchors (3.5 < avg < 7.5): DeComFL/omrLHFzC37 (ZO FL scalar comm, **6.25, Accept**); DJRd4IQHGQ/FeedSign (FL+ZO+LLM, **5.25, Reject**); Ferret/9H1uctBWgF (FL LLM, **4.67, Reject**); kndxjyKxX2 (ZO+LLM+edge, **4.50, Reject**)
- Strong anchors (avg > 7.5): None found in this topic area

*Round 1 bracket: 5.0–6.5*

**Calibration (Round 2 — Narrowing):**
Within 5.0–6.5, additional anchors:
- 4Kw4KAoVnx / Sparse MeZO (ZO LLM FT incremental, **5.50, Reject**) — similar incremental-extension-with-unresolved-assumptions profile
- 2OegVbwvY2 / ZIP (ZO optimization for large models, **5.75, Accept**) — clean contribution with comparable novelty bar
- NvbeD9Ttkx / FOSI (hybrid 2nd-order optimization, **6.25, Accept**) — second-order acceleration, clean theory + strong empirics
- BdPvGRvoBC (FL convergence theory, **6.00, Accept**) — FL theory paper with internally consistent (if somewhat unclear) analysis

**Comparison against Round 2 anchors:**
- *Better than Sparse MeZO (5.50):* HiSo's zero-cost Hessian insight is genuinely more novel than sparsity masking; empirics are stronger.
- *Comparable to ZIP (5.75):* Both make a clever ZO algorithmic contribution; HiSo's is arguably more impactful, but HiSo has the anomalous result and the norm comparison issue that ZIP does not have.
- *Weaker than FOSI (6.25):* FOSI has clean, internally consistent theory + strong empirics. HiSo's theory has the unverified condition AND the norm comparison gap.
- *Weaker than BdPvGRvoBC (6.00):* BdPvGRvoBC's theory is internally sound even if some comparisons are unclear. HiSo has an actively unverified central condition plus an unexplained experimental anomaly.

HiSo sits just below ZIP (5.75), because the norm comparison issue and the OPT-1.3B+QQP anomaly are both concerns that ZIP doesn't have, while HiSo's algorithmic novelty is somewhat stronger than ZIP's. Final score: **5.5**.

**All Anchors Across Rounds:**

| Path | Avg Score | Round | Comparison to HiSo |
|---|---|---|---|
| omrLHFzC37.md (DeComFL) | 6.25 | R1/R2 | Direct baseline; HiSo is incremental on this, with weaker theory soundness |
| NvbeD9Ttkx.md (FOSI) | 6.25 | R2 | Second-order hybrid; cleaner theory; HiSo falls short |
| BdPvGRvoBC.md (FL clipping) | 6.00 | R2 | FL theory, internally sound; HiSo's unverified condition is more fundamental |
| 2OegVbwvY2.md (ZIP) | 5.75 | R2 | ZO optimization; similar novelty bar; HiSo slightly weaker due to anomalous result |
| 4Kw4KAoVnx.md (Sparse MeZO) | 5.50 | R2 | ZO LLM incremental, rejected; HiSo is more novel than this |
| DJRd4IQHGQ.md (FeedSign) | 5.25 | R1 | FL+ZO+LLM, rejected for insufficient novelty; HiSo clearly more novel |
| 9H1uctBWgF.md (Ferret) | 4.67 | R1 | FL LLM compression, rejected; HiSo clearly stronger |
| kndxjyKxX2.md (Grey-box) | 4.50 | R1 | ZO+LLM, rejected; HiSo clearly stronger |
| ZAMoxm86KV.md (FZOOS) | 3.67 | R1 | FL+ZO, rejected; HiSo clearly stronger |
| ER1VDuwWvB.md (CORE) | 3.67 | R1 | Hessian+comm theory only; HiSo clearly stronger empirically |

**Final Score: 5.5 — Reject.** Three unresolved major issues — the unverified "well-approximate Hessian" condition underpinning the headline convergence claim, the misleading norm comparison between Corollaries 1 and 2, and the unexplained 2.2× communication excess on OPT-1.3B+QQP — collectively prevent acceptance in this cycle. The empirical contribution and algorithmic insight are genuine and the paper is revisable; a revision that weakens the theoretical claims to match what is proven and explains the anomalous QQP result would substantially strengthen the submission.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>