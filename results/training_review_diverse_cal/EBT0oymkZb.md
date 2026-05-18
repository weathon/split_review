I now have all the information needed. Let me synthesize the final consolidated review.

---

## Summary

This paper studies zero-shot generalization (ZSG) in offline reinforcement learning — training on data from multiple environments and deploying on unseen ones without interaction. It proposes two meta-algorithms, PERM (model-based) and PPPO (model-free), each with a theoretical suboptimality bound that cleanly decomposes into a supervised learning error (controlled by the number of training environments) and a reinforcement learning error (controlled by dataset coverage). The paper also proves (Proposition 4) that without context information, merged offline data from multiple MDPs is indistinguishable from a single average MDP, explaining why naive offline RL fails to generalize. Experiments on Procgen use IQL with multiple value networks (IQL-nV) as a practical approximation, showing improved generalization over single-network baselines.

## Strengths

- **First theoretical framework for ZSG in offline RL.** The paper provides the first finite-sample guarantees (Theorems 9 and 14) that bound the zero-shot generalization gap in offline RL, explicitly separating the suboptimality into SL error (scaling with the number of environments) and RL error (scaling with dataset coverage). Proposition 4 formally characterizes why ignoring context information leads to failure — a useful impossibility result.

- **Principled use of pessimism for multi-environment generalization.** Unlike standard offline RL where pessimism guards against distribution shift within a single MDP, the paper introduces pessimistic policy evaluation (PPE) as a subroutine that constructs reliable Q-functions *per environment*, which collectively support generalization. Both PERM and PPPO leverage this design, and Theorems 9 and 14 show the RL error term is controlled by coverage relative to the optimal policy.

- **PPPO's action-space-dependent SL error.** PPPO (Algorithm 3) achieves an SL error depending only on \(\log|\mathcal{A}|H^2/n\), avoiding the covering number of the full policy class. This is a meaningful advantage over the model-based PERM, as PPPO maintains \(n\) policies rather than \(n\) critics/models.

- **Empirical demonstration of multi-value-network benefit.** Experiments on Procgen show that IQL-nV (using multiple value networks per environment) outperforms IQL baselines, especially on games where IQL performs worst. The ablation study (Table 3) confirms that increasing the number of value networks monotonically improves performance on the Miner game.

## Weaknesses

### Major

- **Experiment-theory gap: experiments do not faithfully implement the proposed algorithms.** The paper's headline algorithmic contributions are PERM and PPPO, yet the experiments replace PERM with IQL-nV, which uses implicit Q-learning with multiple value networks — a different optimization objective. The paper acknowledges this ("this isn't exactly the same optimization objective as we proposed... but nonetheless a first-order approximation"), but the gap is structural: PERM's theoretical bound (Theorem 9) depends on an uncertainty quantifier Γ and a pessimism step that IQL-nV does not implement, and PPPO is not tested at all. As a result, the experiments do not provide direct evidence that the *proposed algorithms* work. They provide evidence that the *high-level idea* (multiple per-environment critics) helps, but this weakens the paper's claim that "our framework demonstrates the ability to enhance the performance" based on the specific methods proposed. This disconnect reduces the overall impact.

### Minor

- **PPPO's probability guarantee is weak without discussion of amplification.** Theorem 14 holds "w.p. at least 2/3" (with δ = 1/8), which is a constant probability far below the standard high-probability bounds (1−δ for user-specified δ) typical in RL theory. The paper does not discuss whether or how this can be amplified (e.g., via multiple runs and median selection) to a high-confidence bound, nor does it explain why the analysis cannot be tightened. While constant-probability bounds do appear in the RL theory literature, the omission of any amplification discussion leaves the practical meaning of the guarantee unclear.

- **The oracle framework is presented abstractly with limited concrete instantiation in the main text.** The entire theoretical analysis (Definition 5, Theorems 9 and 14) is built on an oracle \(\mathbb{O}\) that returns an empirical Bellman operator and uncertainty quantifier with high probability. Remark 7 mentions bootstrapping, and line 205 states that linear MDPs are treated in the appendix (Algorithm 5, Section D). However, the main text would benefit from at least a brief sketch of a concrete bound (e.g., for linear MDPs) to make the theory tangible for readers. As it stands, the bounds remain at the meta-algorithm level in the main text, making it harder for readers to judge feasibility.

### Trivial

None.

## Nice-to-Haves

- Add a brief discussion of how to amplify the 2/3 probability in Theorem 14 to a standard high-confidence bound (e.g., by running multiple independent copies and taking the median), and at what cost.
- Include a short corollary or concrete bound sketch for linear MDPs (or another standard class) in the main text to make the oracle-based guarantees more tangible.
- If the experiment-theory gap cannot be closed, consider reframing the empirical section explicitly as a *practical heuristic inspired by the framework* rather than as validation of the proposed algorithms. The claim "our framework demonstrates the ability to enhance performance" is reasonable for the core idea, but the connection to the specific algorithms PERM/PPPO should be softened.

## Removed Points

These points were raised by reviewers but are either factually inaccurate, nitpicks, or apply the wrong evaluative standard:

- **"Notation in Algorithms 2 and 3 is occasionally unclear"** — The notation in Algorithm 3 (softmax update) is standard for meta-algorithms in RL theory. For a theoretical paper describing meta-algorithms, this level of abstraction is expected, and function-approximation specifics are a separate concern.
- **"The impossibility result (Proposition 4) overstates its novelty"** — While the intuition may implicitly exist in the multitask RL literature, a formal proof that merged data is indistinguishable from an average MDP is a novel contribution of this paper. The reviewer's assessment is an opinion, not a factual weakness.
- **"The experiments provide no evidence that the proposed methods work"** — This is overstated. The experiments do test the core idea (per-environment critics for generalization), even if they do not implement PERM or PPPO exactly. The underlying concern (the gap) is real and is kept as a Major weakness; the stronger claim that they provide "no evidence" is removed as inaccurate.

## Novel Insights

The most novel insight emerging from the reviews is the tension between the paper's theoretical rigor (which relies on oracle abstractions standard in the PEVI lineage) and the practical heuristic used in experiments (IQL-nV). This gap is not just a presentational issue — it highlights a genuine difficulty in instantiating provable pessimism for deep-RL-like settings. The fact that even the authors fall back on a different objective suggests either that PERM's pessimism step is hard to implement with function approximation, or that the theoretical framework is better understood as a *template* for algorithm design rather than a directly deployable method. Clarifying this distinction — perhaps by separating the theoretical meta-framework from a "practical instantiation" section — would substantially strengthen the paper.

## Suggestions

1. **Restructure the empirical section.** Either (a) implement a faithful version of PERM (or PPPO) with a concrete uncertainty quantifier (e.g., via bootstrapped ensembles as suggested in Remark 7), or (b) explicitly reframe IQL-nV as a *practical heuristic inspired by* — but not validating — PERM, and adjust all claims accordingly (e.g., replace "our algorithm outperforms" with "a heuristic instantiation of our framework outperforms").

2. **Add a concrete bound in the main text.** Even a brief corollary for linear MDPs (with the bound stated and a sketch of the uncertainty quantifier construction) would substantially increase the accessibility and credibility of the theory.

3. **Discuss amplification of PPPO's guarantee.** A few sentences on how the 2/3 probability can be boosted to 1−δ (e.g., by repeating the algorithm and taking the median) — and what cost this would incur — would address a significant theoretical concern.

## Score and Decision

This paper tackles an important and underexplored problem (ZSG in offline RL) and provides the first theoretical framework with clean suboptimality decomposition. The theoretical contributions are solid and novel. However, the empirical validation is weakened by a significant gap between the proposed algorithms (PERM, PPPO) and what was actually tested (IQL-nV). Additionally, the oracle abstraction and PPPO's weak probability guarantee leave parts of the theory feeling incomplete in the main text. The paper would benefit from either closing the experiment-theory gap or being more circumspect about what the experiments validate. On balance, the theoretical contribution is substantial enough to recommend acceptance, but the empirical disconnect prevents a stronger rating.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>