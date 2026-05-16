I have now verified all the relevant claims. Let me produce the consolidated review.

---

## Summary

This paper identifies a systematic bias in GFlowNets for graph generation: when multiple distinct actions lead to isomorphic graphs (equivalent actions), standard training objectives do not account for this, biasing the sampling distribution. The paper provides a clean theoretical analysis proving that the bias is proportional to \(1/|\mathrm{Aut}(G)|\) (fewer symmetries oversampled in atom-based generation), and proposes a simple reward-scaling correction \((\tilde{R}(G) = |\mathrm{Aut}(G)| R(G))\) that requires only one automorphism computation per trajectory. The theory is validated definitively on small graphs with exact enumeration, and practical improvements are shown on molecule-generation tasks.

## Strengths

1. **Rigorous theoretical analysis of bias and its correction.** Theorem 1 and Corollary 1 formally prove that the ratio of forward-to-backward state-action probabilities equals the automorphism group size ratio, and that ignoring this biases the model by \(1/|\mathrm{Aut}(G_n)|\). The telescoping argument is clean, and the result is correctly derived for both Trajectory Balance and Detailed Balance objectives.

2. **Simple and efficient correction.** The correction requires only a single \(|\mathrm{Aut}(G)|\) computation per trajectory (terminal state), rather than per-step graph isomorphism tests. The paper explicitly contrasts this with the \(O(K \times T)\) complexity of per-step alternatives (Section 5, Computation paragraph), making the practical advantage concrete.

3. **Definitive experimental validation in a controlled setting.** The small-graph experiment (Figure 3) uses exact enumeration over \(|\mathcal{X}| = 2{,}999\) states. The target-to-model probability ratio exactly matches \(|\mathrm{Aut}(x)|\) for vanilla TB and is constant for TB+AC, directly confirming the predicted bias and the efficacy of correction.

4. **Demonstrated practical impact on realistic molecular generation tasks.** On both atom-based and fragment-based tasks (Table 2), TB+AC improves reward, diversity, and FCS over vanilla TB. The concrete example (cyclohexane count: 5220 vs. 1042) makes the bias tangible.

5. **Unbiased model-likelihood estimator.** Equation (3) provides an unbiased estimator for \(p_S^\top(x)\) using importance sampling and the automorphism correction, enabling proper evaluation on held-out data — a meaningful methodological addition.

6. **Consistency across multiple GFlowNet objectives.** Corollary 1 (TB) and Theorem 2 (DB) both reduce to the same reward-scaling correction, suggesting broad applicability.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by theory and experiment. The issues below are all addressable and do not undermine the central contribution.

### Minor

1. **The approximate correction method (TB+XC) is underspecified.** The paper describes it in three sentences: "assign a number to each fragment based on how many equivalent actions it is likely to incur during generation" and then divide the reward by the product of those numbers. No algorithm, heuristic, or formal definition is given for determining these numbers. While this is a *supplementary* method — the exact fragment correction (Theorem 3, Equation 2) is the main approach — the paper reports TB+XC results in Table 2 and claims computational benefits, which makes the lack of specification a reproducibility gap. **Severity**: minor (the exact method is specified; this only affects the approximate variant).

2. **The reward adjustment procedure for Table 2 is not explicitly stated.** The paper says "When reporting rewards, we adjust them to remove the effects of reward scaling and reward exponents" without showing the formula or the unadjusted values. Given that the paper uses \(\tilde{R}(G) = C(x)R(x)^\beta\) for training, the natural interpretation is that reported rewards are \(R(x)\) (raw proxy reward), but this should be stated explicitly to rule out any concern that the adjustment itself introduces bias. **Severity**: minor.

3. **Theorem 3 (Fragment correction) is stated without derivation or proof sketch in the main text.** The formula \(\tilde{R}(G) = |\mathrm{Aut}(G)|R(G) / \prod_i |\mathrm{Aut}(C_i)|\) is given with an intuitive explanation, but unlike Theorem 1, no derivation is attempted. Since this is a key result for the fragment-based experiments, a brief sketch would help the reader trust the claim without having to consult the appendix. **Severity**: minor.

4. **Theorem 2 (DB correction) would benefit from a brief intuition.** The paper states that reward scaling suffices for DB and draws an analogy to intermediate reward signals, but does not sketch why the graph-level detailed balance condition together with reward scaling yields the correct distribution. The core insight (telescoping works at the DB level too) is worth a sentence. **Severity**: minor/trivial.

### Trivial

1. The assumption underlying Lemma 1 (that permutation-equivariant networks assign equal probability to actions in the same orbit) is stated, but the paper could briefly note that this holds for standard GNN aggregators and could fail with positional encodings or other symmetry-breaking architectures. This is a minor clarification, not a flaw.

2. The paper references Appendix H for hyperparameters and architecture details; this appendix is missing from the reviewed manuscript (parser artifact) but stated to be present in the original submission — no weakness attaches to the paper for this.

## Nice-to-Haves

- A comparison to a GFlowNet that uses a canonical node ordering (or adjacency-matrix formulation) would further strengthen the claim that the correction brings sequence-based GFlowNets to parity with methods that inherently avoid the bias. The paper correctly notes this distinction in Related Work; an empirical demonstration would be a useful addition.
- Wall-clock timing comparisons between the automorphism computation and per-step alternatives would address a natural concern about scalability. The paper qualitatively discusses complexity but does not report actual times.
- Showing both raw and adjusted metrics in Table 2 (or a footnote) would fully resolve the reward-adjustment ambiguity.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Absence of FCS on the atom-based task"** (Harsh Critic). The paper states "This is also evidenced by FCS metric in the Table 2" for the atom-based task, so FCS was measured and reported. This criticism is factually incorrect.
- **"Missing appendix, missing proofs in appendix"** (Harsh Critic). The appendix was stripped by the parser; the original submission contains it. Per the hard rules, criticisms about absent appendix content are removed.
- **"Comparison to adjacency-matrix baseline would strengthen the claim"** — moved from weakness to nice-to-have, as the paper's scope is correcting sequence-based GFlowNets, not benchmarking every formulation.
- **"The authors should add X" wishlist items** — moved to Nice-to-Haves where they do not affect the accept/reject judgment.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that the paper itself does not articulate. The primary insight — that the ratio of forward-to-backward equivalent actions telescopes to \(|\mathrm{Aut}(G)|/|\mathrm{Aut}(G')|\) and that reward scaling at the terminal state suffices — is the paper's own contribution and is correctly presented.

## Suggestions

1. **Specify the approximate correction.** Provide a concrete algorithm or rule for how the "numbers" for TB+XC are assigned to fragments, or replace the approximate variant with the exact fragment correction (Equation 2) as the primary fragment-based method.
2. **State the reward-adjustment formula explicitly.** Add one sentence: "Reported rewards are the raw proxy reward \(R(x)\) before applying the automorphism correction or reward exponent \(\beta\)." Or show a brief example.
3. **Add a proof sketch for Theorem 3** (and optionally Theorem 2) in the main text, mirroring the clean presentation of Theorem 1 and Corollary 1.

## Score and Decision

This is a method paper with a strong theoretical component. The contribution is clearly scoped, the theoretical analysis is correct, and the experimental validation is well-designed (the small-graph experiment with exact enumeration is particularly convincing). The weaknesses are all minor and addressable — they concern presentation and specification of supplementary details, not the validity of the core claims. The paper represents a meaningful advance for the GFlowNet community and is ready for acceptance with minor revisions.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>