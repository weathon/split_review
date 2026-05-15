Below is my consolidated review, after cross-checking every claim against the paper.

---

## Summary

The paper studies zero-shot generalization (ZSG) in offline RL when training data comes from multiple environments / contexts. It proves a negative result (Proposition 4): without access to context information, offline RL with Markovian policies fails to generalize. It then proposes two meta-algorithms—PERM (model-based) and PPPO (model-free)—that use per-environment pessimistic value functions, and derives suboptimality bounds that decompose into a supervised learning term (shrinking with the number of environments $n$) and an RL term (controlled by dataset coverage). Experiments on Procgen show that an approximate instantiation (IQL with multiple value networks, called IQL-$n$V) outperforms single-network IQL.

---

## Strengths

- **First provable bounds for ZSG in offline RL (Theorems 9, 14).** The paper provides the first theoretical guarantees showing that an offline RL algorithm can output a near-optimal policy with zero-shot generalization. The decomposition into a supervised learning error (controlled by $n$) and an offline RL error (controlled by coverage) is conceptually clean and captures the essential trade-off.

- **Negative result establishing the necessity of context information (Proposition 4, Figure 1).** The paper proves that without context labels, the pooled offline dataset is indistinguishable from data from an average MDP, and constructs a simple 2-context example where the average-MDP-optimal policy achieves 0 expected return while the true ZSG-optimal policy achieves 0.5. This cleanly explains prior empirical failures and motivates the algorithmic approach.

- **Dual algorithmic frameworks (model-based PERM and model-free PPPO).** Covering both paradigms with a unified pessimistic evaluation subroutine (PPE) gives the work architectural breadth, and the differences in the SL-error terms between the two theorems (covering number vs. $|\mathcal{A}|$) are interesting.

---

## Weaknesses

### Fatal
None.

### Major

- **Theory–experiment gap: the experiments test IQL-$n$V, not PERM or PPPO.** The paper explicitly states that IQL-$n$V is "not exactly the same optimization objective" as PERM and calls it a "first-order approximation." However, no justification is given that IQL-$n$V inherits any of the theoretical guarantees of PERM/PPPO (the pessimism principle that produces the $\Gamma_{i,h}$ uncertainty quantifier in the bounds). IQL uses expectile regression, not a pessimistic penalty derived from uncertainty quantification. The empirical results therefore cannot be used to validate the central claim that PERM/PPPO "demonstrate effectiveness." The paper's strongest empirical claims ("our algorithm outperforms the vanilla RL baselines") refer to IQL-$n$V, leaving a disconnect between what is proved and what is tested.

- **PPPO's theoretical guarantee is fundamentally weak.** Theorem 14 holds with probability at least $2/3$, which is an unusually low confidence level for a theoretical result in RL. The algorithm selects $\delta=1/8$ to achieve this, and the bound's SL error $O(\sqrt{\log|\mathcal{A}|\,H^2/n})$ does not depend on the policy class complexity. The *random selection* of one policy from $n$ sequentially trained policies as the final output, combined with the sequential dependence structure, makes the result hard to interpret. Without verifying the proof (deferred to appendix), the stated guarantee as presented in the main text inspires limited confidence.

- **Empirical evaluation is too narrow to support the paper's claims.** (a) Only two baselines are compared: IQL and BC, both from the same data pipeline (Mediratta et al., 2023). No existing offline RL generalization method (e.g., from Mazoure et al., 2022, or other methods discussed in the Related Work) is included. (b) The 200 training levels are grouped into 4 contexts of 50 levels each—a practical choice that may violate the theoretical i.i.d. assumption if levels within a group share structure. (c) The ablation (Table 3) increases the number of value networks but does not control for total parameter count (e.g., a single larger IQL with 4× the width), so the improvement could partly reflect increased capacity rather than the benefit of per-environment value functions.

### Minor

- **Uncertainty quantifier $\Gamma_{i,h}$ is not instantiated for any concrete MDP class in the main text.** The bounds remain abstract: they hold for *any* oracle $\mathbb{O}$ that returns an uncertainty quantifier, but the main text does not show that $\Gamma_{i,h}$ can be small for a tractable class (e.g., linear MDPs), or discuss how to construct it in practice beyond a brief remark about bootstrapped DQN. (Concrete instantiations appear in the appendix.) While this is standard for meta-algorithms, the main text's theoretical contribution would be stronger with at least one concrete instantiation and discussion of when the bounds are non-vacuous.

- **Remark 10 notes the covering number is exponential in $|S|$ for tabular representations, but the practical implications are not discussed.** The bound may be vacuous in large state spaces without additional structure, yet the paper does not address this limitation.

- **PPPO's sequential dependence structure.** The algorithm processes MDPs sequentially, using Q-functions from environment $i-1$ to update the policy for environment $i$. This breaks the i.i.d. data assumption underlying the theory, and the main text does not explain why this is valid. (The proof is in the appendix.)

### Trivial
- Figure 2 shows performance gaps as point estimates across 5 seeds without visible error bars. The paper would benefit from showing variability in the figure.

---

## Nice-to-Haves

- A proper implementation of PERM or PPPO (or a rigorous justification of why IQL-nV approximates PERM) would close the theory-experiment gap.
- Including comparisons against other offline RL ZSG methods from the literature (not just IQL and BC) would strengthen the empirical claims.
- A parameter-count-controlled ablation (single wide network vs. multiple narrow networks) would isolate the benefit of per-environment value functions from increased capacity.

---

## Removed Points

These points were removed per the review guidelines; they are listed for transparency but should not be considered in the evaluation:

1. **"Proof is omitted" for PPPO / "missing appendix" criticisms.** The paper's proofs and concrete instantiations (Algorithm 5, Section D) are in the appendix, which the parser stripped. All papers read via this interface have stripped appendices; the content exists in the original submission.
2. **Claim that BC statement is an "overstatement."** The paper states BC "converges to the teacher policy that is independent of the specific MDP." This is factually correct—BC on pooled data learns a context-independent policy—and the broader point about BC vs. offline RL generalization is supported by the paper's analysis.
3. **Criticism about "theoretical bounds left uninstantiated" as a structural flaw.** Concrete instantiations for linear MDPs exist in the appendix (referenced on line 205). The main text presents the meta-level result, which is standard practice for theory papers.
4. **Criticism about the SL error's covering number being "exponential."** The paper acknowledges this in Remark 10. The fact that the bound depends on policy class complexity is expected; the paper does not hide this.

---

## Novel Insights

The most interesting observation emerging from this review is the asymmetry between the two theoretical bounds: PERM's SL error depends on a covering number of the policy class, while PPPO's SL error depends only on $|\mathcal{A}|$. This difference is attributed to PPPO outputting a randomly selected policy from $n$ candidate policies (each optimized for a specific environment) rather than a single ERM-style policy. This suggests a fundamental trade-off: model-based approaches (PERM) may achieve better per-environment optimality at the cost of policy-class-dependent generalization, while model-free approaches (PPPO) trade away individual optimality for action-space-dependent (and thus potentially tighter) generalization. Neither bound dominates the other, and unifying them—or showing a fundamental limit—would be a valuable contribution.

---

## Suggestions

1. **Align theory and experiment.** Either implement PERM or PPPO with an explicit pessimistic penalty (e.g., using CQL or PEVI as the base algorithm with per-environment critics) on Procgen or a smaller benchmark, or alternatively, provide a theoretical argument that IQL-$n$V's expectile regression objective is a valid instantiation of the pessimistic evaluation framework, and derive a bound for it.
2. **Strengthen the PPPO guarantee.** Raise the confidence probability to a standard level (e.g., $1-\delta$ with $\delta=0.1$) or provide a clear explanation of why $2/3$ is acceptable in this setting.
3. **Include additional baselines** from related offline RL generalization work (e.g., those discussed in the paper's own Related Work section).
4. **Add a capacity-controlled ablation** to separate the effect of more parameters from the effect of per-environment value functions.
5. **Provide an explicit instantiation of $\Gamma_{i,h}$** in the main text for a tractable MDP class (e.g., linear or tabular MDPs) and discuss when the SL error is non-vacuous.

---

## Score and Decision

**Originality:** High — first provable bounds for ZSG in offline RL.  
**Importance:** High — ZSG is practically important and theoretically understudied.  
**Claims supported:** Moderate — theoretical claims are backed by proofs (appendix), but empirical claims about "effectiveness of our methods" conflate PERM/PPPO with IQL-$n$V.  
**Soundness of experiments:** Low — experiments test an approximation with no justification of theoretical inheritance, limited baselines, and no capacity-controlled ablation.  
**Clarity of writing:** Good — the paper is well-structured and the motivation is clear.  
**Value to community:** Moderate — the theoretical framework is a useful starting point, but the empirical validation is too weak to fully support the contributions.

The paper has a genuine theoretical contribution (first provable ZSG bounds for offline RL) and a clean negative result. However, the experiments do not actually test the proposed algorithms, the PPPO guarantee is unusually weak, and the empirical evaluation is too narrow. These issues are substantial enough that the paper's main claims are not fully supported by the evidence presented.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>