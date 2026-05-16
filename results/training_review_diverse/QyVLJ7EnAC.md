Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces a double-pessimism principle for model-free offline robust reinforcement learning. The core idea is to combine two penalty terms — one for dataset coverage (standard pessimism) and one for model mismatch (a new pessimism) — to obtain a conservative estimate of the robust value function without requiring a transition model. The paper provides the first theoretical sample-complexity guarantees for a model-free offline robust RL algorithm under the \(l_\alpha\)-norm uncertainty set, with bounds that match model-based robust RL in key terms. Experiments on Garnet and Classic Control problems show the double-pessimism algorithm outperforms a single-pessimism (non-robust) baseline.

## Strengths

- **Novel double-pessimism principle enabling model-free offline robust RL.** The paper constructs a principled combination of two pessimism terms (Definition 1) and provides a concrete construction of the model-mismatch penalty \(\kappa\) for \(l_\alpha\)-norm uncertainty sets (Lemma 1). The resulting update rule (Equation 15) avoids storing or computing a transition model, which is a genuine conceptual innovation for this setting.

- **First theoretical sample-complexity guarantees for model-free offline robust RL.** Theorems 2 and 3 give finite-sample bounds of \(\tilde{\mathcal{O}}\bigl(\frac{H^6 S C^*}{\epsilon^2}\bigr)\) (finite-horizon) and \(\tilde{\mathcal{O}}\bigl(\frac{S C^*}{(1-\gamma)^5\epsilon^2}\bigr)\) (infinite-horizon). As the paper honestly notes, these match non-robust model-free Q-learning without variance reduction and are competitive with model-based robust RL in \(S\) and \(C^*\). This is a significant theoretical contribution that opens up a new direction for model-free algorithms in robust offline RL.

- **Substantially improved memory and computational efficiency compared to model-based alternatives.** Section 7.1 and Table 1 convincingly argue that the model-free approach reduces memory from \(\mathcal{O}(S^2A)\) (storing the transition model) to \(\mathcal{O}(SA)\) (storing visitation counts), and avoids the \(\hat{P}_{s,a}V\) inner product required by model-based methods. This scalability advantage is inherent in the algorithm design and does not depend on any particular experiment.

- **Use of partial coverage assumptions (Assumptions 1 and 2), which are standard in modern offline RL.** The paper adopts the robust single-policy concentrability condition, which is much less restrictive than global coverage and ties into a well-established literature.

## Weaknesses

### Fatal
None.

### Major

- **Experiments do not compare against existing robust offline RL methods, despite claiming improved robustness "over existing methods."** The abstract and contribution list claim the approach "significantly improves robustness in a more scalable manner than existing methods" and "consistently outperforms existing methods in handling model uncertainty." Yet the experiments exclusively compare against a single-pessimism (non-robust) baseline (Yan et al., 2022). The prior robust works cited — Shi & Chi (2022) and Blanchet et al. (2023) — are discussed theoretically but never benchmarked. Outperforming a non-robust baseline is expected and does not demonstrate advancement over *existing robust* approaches. Similarly, the claim that model-based methods are "ineffective" for Classic Control problems is stated without any attempted implementation, even in a simplified discretized form. This mismatch between the strength of the empirical claims and the evidence provided is the paper's most significant weakness. The theoretical contribution is not harmed, but the empirical narrative overreaches.

### Minor

- **Missing implementation details for Classic Control experiments.** The paper is set in tabular MDPs, but CartPole and MountainCar have continuous state spaces. The paper does not specify how states were discretized, the resulting size of the state-action space, how the \(l_\alpha\)-norm uncertainty set or penalty radius \(R_{h,s,a}\) was constructed for these environments, or how the dataset penalty \(b\) was computed beyond saying it is based on "visitation counts." These omissions prevent independent reproduction of the results and undercut the claim that scalability to "large problems" has been concretely demonstrated.

- **How the perturbation radius \(R_{h,s,a}\) is set in practice is not discussed.** Lemma 1 and the algorithm depend on this radius. For the Garnet experiments, the paper states \(R_{s,a} \in [0.1, 0.5]\) (chosen randomly), but there is no discussion of how a practitioner would set this parameter in a new problem — e.g., via domain knowledge, cross-validation, or sensitivity analysis. This limits the practical guidance the paper offers.

- **No ablation study disentangling the two penalty terms.** The paper compares double-pessimism against single-pessimism, but does not compare against (a) no penalty, (b) only model-mismatch penalty (no dataset penalty), or (c) only dataset penalty (the baseline). This would help isolate the contribution of each term.

- **The practical implications of the robust single-policy concentrability coefficient \(C^*\) are not discussed.** As the paper defines it (Assumptions 1 and 2), \(C^*\) requires coverage under *any* worst-case kernel in the uncertainty set, which can be substantially more restrictive than standard non-robust concentrability when the uncertainty set is large. This is a practical limitation worth acknowledging.

### Trivial

- The word "universal" in the abstract ("propose a universal, model-free algorithm") slightly overstates the scope, since the theoretical analysis and concrete penalty construction are only provided for \(l_\alpha\)-norm sets. However, the paper does hedge in Remark 2, so this is a minor framing issue.

## Nice-to-Haves

- A comparison against a simplified/discretized version of at least one model-based robust offline RL method on the Garnet problems, even if the comparison favors the proposed method (the hard rules note this is acceptable when the asymmetry favors the baseline).
- A brief table of wall-clock runtime to ground the claimed computational advantages.
- Statistical significance tests or confidence intervals for the experimental results.
- Discussion of how \(R_{h,s,a}\) could be selected in practice.

## Removed Points

The following points raised by reviewers are removed or downgraded per the instructions:

1. **"Proof of Lemma 1 missing due to appendix stripping"** — Removed per hard rule: the parser strips appendices; the proofs exist in the original submission.
2. **"Comparison of sample complexity rates across different uncertainty sets is not meaningful"** — The paper explicitly notes that the comparison with Blanchet et al. uses different uncertainty sets (Table 1 caption: "(Shi & Chi, 2022) is for the KL-divergence set") and qualifies the comparison. The critic's concern is already addressed.
3. **"No code release"** — Removed per hard rule: criticisms questioning the availability of artifacts not cited in the paper should not be treated as weaknesses.
4. **"The uncertainty set formulation assumes P is known"** — The paper's model-free approach avoids estimating P, and the formulation is standard in the robust RL literature. This criticism misunderstands the role of the nominal kernel in the theoretical setup.
5. **"Only two Classic Control environments"** — Two environments are sufficient for a demonstration in a primarily theoretical paper. This is scope creep.
6. **"10 random seeds is small"** — 10 seeds is standard for tabular experiments. This is a generic nitpick.
7. **Strength "Empirical validation of enhanced robustness"** — Downgraded/moved because the strength claims conflict with the verified weakness (no comparison to robust baselines), per the conflict resolution rule.

## Novel Insights

The reviews surface one genuinely useful observation beyond the paper's own contributions: the robust single-policy concentrability coefficient \(C^*\) (Assumptions 1 and 2) is potentially much more restrictive than standard non-robust concentrability, because it requires coverage of state-action pairs under *any* worst-case kernel within the uncertainty set. For large uncertainty sets, this could grow significantly, and the paper does not discuss this practical limitation. This is a point worth the authors' attention when positioning their theoretical results.

## Suggestions

1. **Tone down the empirical claims in the abstract and contributions** to match what is actually shown: the method improves over a non-robust baseline. If the authors wish to keep the stronger claim, experiments against at least one model-based robust offline RL method (e.g., on the Garnet problems) are essential.
2. **Add implementation details for the Classic Control experiments:** discretization scheme, resulting state-action space dimensions, how the uncertainty set and penalty radii were constructed, and how \(b\) and \(\kappa\) were computed.
3. **Discuss the practical implications of the robust concentrability coefficient** and how it compares to standard non-robust concentrability.
4. **Add an ablation study** comparing double-pessimism against (no penalty), (dataset penalty only), and (mismatch penalty only).

## Score and Decision

The paper's core contribution — the double-pessimism principle and the first theoretical guarantees for model-free offline robust RL — is novel, technically sound, and valuable. The theoretical results are the main event, and they are not undermined by the experiment-level overclaims. However, the paper's own framing ("significantly improves robustness in a more scalable manner than existing methods") invites scrutiny that the experiments do not withstand. The mismatch between the empirical claims and the evidence is a real weakness, but it is not fatal to the paper's primary (theoretical) contribution.

This is a borderline paper: strong theory, weak experiments relative to claims. Given that the theoretical contribution is genuinely novel and the experimental overreach is correctable, the paper is worth accepting with the expectation that the authors adjust their empirical framing or add robust baselines in the camera-ready.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>