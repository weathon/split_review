Now I have read the full paper. Let me write the consolidated meta-review.

---

## Summary

HiSo (Hessian-informed Scalar-only communication) proposes a federated zeroth-order optimization method for LLM fine-tuning that incorporates a globally learned diagonal Hessian preconditioner while strictly preserving scalar-only (dimension-free) communication. The key insight is that the aggregated ZO update vector $\Delta x_r$, already transmitted for model reconstruction, can be reused to maintain an exponential moving average of squared updates as a free diagonal preconditioner—adding zero communication overhead. Theoretically, under a "well-approximated Hessian" condition, HiSo achieves a convergence rate independent of model dimension $d$ and Lipschitz constant $L$; empirically, it achieves 1.4–5.4× faster convergence than DeComFL across three LLM fine-tuning tasks.

---

## Strengths

- **Zero-overhead Hessian preconditioning (Section 4.2, Eq. 12):** The paper's central technical insight is that $\Delta x_{r,0}$ is already reconstructed by all participants for model synchronization; squaring its entries and exponentially averaging them yields a diagonal preconditioner with exactly zero additional communication cost. This is a clean and genuine contribution.

- **Generalized scalar-only FL framework (Section 3.3, Algorithm 1):** The paper decouples the scalar-only communication property from the specific choice of ZO-SGD, enabling a broader class of update rules within the dimension-free paradigm. This generalization is clearly formulated and opens the door to future extensions.

- **Strong empirical results across multiple LLM settings (Tables 2–3):** HiSo consistently achieves 1.4–5.4× speedup to reach DeComFL's best accuracy with 29–80% communication savings across three tasks (SST-2, QQP, SQuAD) and three model sizes (OPT-125M/350M/1.3B/2.7B), while also achieving strictly higher final test accuracy than all ZO baselines.

- **Extension of DeComFL theory to $\tau > 1$ (Corollary 3):** The paper's analysis covers multiple local update steps, resolving an open problem in DeComFL's convergence analysis. This is a concrete theoretical advance.

- **Robustness to smoothing parameter $\nu$ (Figure 5 left):** Across $\nu \in \{0.9, 0.95, 0.99\}$, HiSo's convergence and final accuracy are stable, indicating no sensitive hyperparameter tuning is required.

- **Empirical Hessian structure validation (Figure 5 right):** The learned diagonal Hessian entries exhibit a long-tailed distribution consistent with the low-effective rank assumption, lending practical support to the theoretical mechanism.

---

## Weaknesses

### Fatal
None.

### Major

- **Convergence rate comparison uses mismatched norms.** Theorem 1's LHS bounds $\mathbb{E}[\|\nabla F(\bar{x}_{r,k})\|^2_{H_r^{-1}}]$, the $H_r^{-1}$-weighted gradient norm. Corollary 1 then derives a rate of $\mathcal{O}(\sqrt{\zeta/mR})$ in this weighted norm. Corollary 2 (DeComFL as $H_r \equiv I$) recovers $\mathcal{O}(\sqrt{L\kappa/mR})$ in the standard Euclidean norm. These are not directly comparable quantities. Converting the HiSo rate from $H_r^{-1}$-norm to Euclidean norm requires multiplying by $\beta_\ell^{-1}$ (Assumption 4), introducing a dependence on the smallest eigenvalue of $H_r$ that may itself depend on model scale. The paper presents Corollaries 1 and 2 as directly establishing HiSo's advantage over DeComFL without addressing this norm discrepancy, making the stated theoretical comparison less clean than it appears.

### Minor

- **Headline convergence claim is conditional but presented as definitive in the abstract and introduction.** The abstract states HiSo "can achieve an accelerated convergence rate that is independent of the Lipschitz constant $L$ and model dimension $d$," and the introduction lists this as a bullet-point contribution. However, this rate requires the "well-approximated condition" (Definition, Eq. 17), which is neither proved to hold for HiSo's RMSProp-style update (Eq. 12) nor directly verified empirically in LLM fine-tuning. The paper itself notes in the Remarks section of Section 5.2: "it is hard to determine if this approximation holds in the context of LLMs." The conditional nature is disclosed—but only deep in the paper. A more honest abstract framing (e.g., "under a well-approximated Hessian condition") would align the narrative with what can actually be proved about HiSo specifically.

- **OPT-1.3B + QQP total convergence cost.** Table 3 shows HiSo's total communication until convergence is 96.67 KB versus DeComFL's 43.95 KB for OPT-1.3B+QQP—a 2.2× excess. The paper dismisses this as "only a little higher," which significantly understates the gap. The correct explanation is that HiSo converges to a higher final accuracy (64.20% vs 63.25%) and therefore runs longer; Table 2 shows HiSo reaches DeComFL's best accuracy at 750 rounds (29.30 KB). The paper should present this as an explicit Pareto tradeoff (higher cost for higher accuracy on this task) rather than a minor discrepancy.

- **Small and homogeneous FL setup; missing non-IID details.** The LLM fine-tuning experiments use only 6 clients with 2 sampled per round. The Dirichlet non-IID parameter $\alpha$ is stated for MNIST ($\alpha=1$) but not reported for any of the LLM tasks. Whether the data partitioning is heterogeneous at all in the LLM experiments is unclear, which matters for assessing how HiSo performs under the client drift it aims to handle.

### Trivial

- Corollary 3 claims the $\tau>1$ rate is "still independent of model dimension $d$," but the drift term includes $\kappa = \text{Tr}(\Sigma/L)$, which can scale with $d$ in the worst case. The independence holds only under the low-effective rank assumption and should be stated explicitly in Corollary 3 rather than only in the associated remarks.

---

## Nice-to-Haves

- Tracking how well HiSo's learned $H_r$ satisfies the well-approximated condition (Eq. 17) during actual LLM fine-tuning—e.g., computing $\text{Tr}(H_r^{-1/2} \hat{\Sigma}_r H_r^{-1/2})$ with a held-out Hessian estimate at periodic checkpoints—would directly validate the theoretical premise and substantially strengthen the story.
- A brief derivation or intuition connecting the RMSProp-style accumulator (Eq. 12) to Hessian diagonal approximation in the ZO setting (e.g., via the Fisher-information / gradient-covariance connection) would make Section 4.2 more self-contained.
- Scaling experiments with larger client pools (e.g., 20–50 clients) would address whether the Hessian estimate degrades when fewer clients are sampled relative to total pool size.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Hessian-informed framing overreaches" (Harsh Critic):** The paper explicitly acknowledges in footnote 2 that "our method resembles RMSProp." The terminology "Hessian-informed" is disclosed as an approximation and is consistent with how it is used in cited prior work (Ye et al., 2018; Zhao et al., 2025). This criticism has no traction given the paper's own transparency on this point.

- **"First-order baselines are partially misleading" (Harsh Critic):** The comparison between HiSo (90.34% on OPT-1.3B+SST-2) and FedAdam (92.86%) is asymmetric against the author's method. Under the hard rule, comparisons that favor the baseline are not a weakness of the proposed method and should not be flagged.

- **"Hessian update uses only step k=0" (Harsh Critic):** This misreads the paper. The simplified algorithm in Section 4.3 writes $\Delta x_{r,0}$ referring to the global aggregated update in the $\tau=1$ case (where "0" is the step index). The full algorithm (Appendix D) handles $\tau>1$. This is not an evidenced design flaw.

- **Criticism of missing related works (Qin et al., 2024; Liang et al., 2025):** Per the hard rules, absent related-work comparisons cannot be verified from external sources and should not be cited as weaknesses.

- **"$\kappa$ can be $O(d)$ in the worst case in Corollary 3" as a major issue:** This is speculative in the context of the paper's assumptions; under the low-effective rank assumption $\kappa \ll d$ by premise. Demoted to Trivial rather than Major.

- **"Stale Hessian across missed rounds" concern (Harsh Critic):** This is a speculative gap—"whether this desynchronization causes problems is not addressed"—rooted in an assumption about the appendix. The paper's reconstruction mechanism (Algorithm 1, lines 6–8) handles missed rounds; the critic provides no concrete example of failure. Per the filtering rules, speculative-fatal claims without paper-grounded evidence are removed.

- **Low effective rank strength (Strength Finder - Corollary 3 claim about independence from d):** This is retained as a qualified strength but partially contradicted by the trivial weakness above regarding $\kappa$.

---

## Novel Insights

The most genuinely novel observation in the paper—and one that extends beyond the contribution itself—is the realization that scalar quantities already communicated for model reconstruction constitute a "free" channel for maintaining global second-order information. This suggests a broader principle: any quantity derivable from already-communicated scalars can be incorporated into the optimization state without violating the dimension-free communication budget. This could motivate exploration of momentum, gradient skewness estimates, or other statistics derived from the ZO scalar stream, all at zero additional communication cost.

---

## Suggestions

1. **Fix the norm comparison in Section 5.2:** Either (a) derive a bound on HiSo's rate in Euclidean norm (noting the $\beta_\ell^{-1}$ factor explicitly) so it is directly comparable to Corollary 2, or (b) add a remark clarifying that Corollaries 1 and 2 are not directly comparable due to the norm difference.

2. **Rewrite the abstract** to qualify the $d$- and $L$-independent rate as holding "under a well-approximated Hessian condition" to match what is actually provable about HiSo.

3. **Clarify Table 3's OPT-1.3B+QQP entry** by noting explicitly that HiSo's higher total cost (96.67 KB vs 43.95 KB) reflects convergence to a higher final accuracy, and frame it as a Pareto tradeoff point.

4. **Report the non-IID Dirichlet parameter** for all LLM fine-tuning tasks, not just MNIST; this is standard metadata in FL papers.

---

## Assessment

**Originality:** High. The core idea—reusing already-communicated scalars as a free Hessian approximation channel—is genuinely novel within the ZO-FL setting. The generalized framework and extended $\tau>1$ theory also represent real advances.

**Importance:** High. Communication cost is a dominant bottleneck in federated LLM fine-tuning; a method that substantially accelerates convergence without increasing per-round cost addresses a meaningful practical problem.

**Claims Supported:** Mostly well-supported empirically. The theoretical claims are partially overstated in the abstract and introduction (conditional rate presented as unconditional); the cross-norm comparison is a genuine gap. However, the empirical results cleanly and consistently support the paper's practical claims.

**Soundness:** Good. The algorithm is carefully designed, the theoretical framework is internally consistent, and the empirical evaluation covers multiple models and tasks. The theoretical gaps (norm mismatch, conditional rate) are real but do not invalidate the core contribution.

**Clarity:** Good overall. Section 5.2's Remarks section is commendably honest about limitations; the mismatch between the abstract's confident framing and those remarks is the primary clarity issue.

**Value to the research community:** Solid. The paper offers a practical, deployable method with clear gains over state-of-the-art ZO-FL baselines, an extensible framework, and a principled (if conditional) theoretical explanation.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>