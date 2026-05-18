Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper proposes FC-GFlowNet, a one-shot federated learning framework for GFlowNets where the global reward is a product of local rewards and clients are unwilling to share their reward functions directly. Each client trains a local GFlowNet; the server aggregates their policies using a new *federated balance* (FB) condition. Along the way, the paper introduces *contrastive balance* (CB), a new training criterion for conventional (non-federated) GFlowNets that avoids parameterizing the partition function. Experiments on grid-world, multiset, sequence, and phylogenetic inference tasks show that FC-GFlowNet closely matches the performance of a centralized GFlowNet (with direct reward access) and vastly outperforms a naive product-of-categoricals baseline.

## Strengths

1. **Novel federated balance condition with provable guarantees.** Theorem 1 provides a necessary and sufficient condition (federated balance) for correctly aggregating locally trained GFlowNets to sample from the product of their rewards. This is the first principled approach for federated learning of GFlowNets, extending GFlowNet theory to a setting with no prior work.

2. **Contrastive balance (CB) as a simpler training criterion.** Lemma 1 and Corollary 2 establish a necessary and sufficient condition for GFlowNet correctness that requires no parameterization of the partition function or state flows — only forward and backward policies. This reduces model complexity relative to TB and DB, and experiments in Section 4.5 show it can lead to faster convergence in some settings (multiset generation, phylogeny).

3. **Theoretical characterization of imperfect local models.** Theorem 2 provides an upper bound on the Jeffrey divergence between the aggregated distribution and the true product distribution in terms of local errors (\(\alpha_n, \beta_n\)), quantifying how local inaccuracies propagate. Remark 1 connects this to the known "catastrophic failure" phenomenon in parallel inference.

4. **Solid empirical validation across four diverse tasks.** Experiments on grid world, multiset generation, sequence design, and Bayesian phylogenetic inference show FC-GFlowNet achieving L1 distances within one standard deviation of the centralized model (which has direct reward access), and substantially outperforming the PCVI baseline. The phylogenetic inference task (Section 4.4) demonstrates a novel application of federated GFlowNets to distributed Bayesian inference over discrete structures.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theorem 3 (VI-CB connection) proof sketch is insufficiently justified.** The proof defines \(\xi_{\text{TB}}(\tau;\phi_F,Z) = \log\frac{Z p_F(\tau)}{p_B(\tau|x)R(x)}\) and notes that \(\mathcal{L}_{CB}(\tau,\tau') = (\xi_{\text{TB}}(\tau)-\xi_{\text{TB}}(\tau'))^2\) (which is correct because \(Z\) cancels). It then invokes Prop. 1 of Malkin et al. (2023) for \(\mathbb{E}[\nabla_{\phi_F}\xi_{\text{TB}}]=0\) and \(\mathbb{E}[\nabla_{\phi_F}\xi_{\text{TB}}^2] = 2 D_{\text{KL}}[p_F\|p_B]\). While the first identity is unproblematic (log-derivative trick, independent of \(Z\)), the second requires more careful justification — Malkin et al.'s TB result was derived under joint optimization of \(p_F\) and the learned \(Z\), whereas CB has no learned \(Z\). The claimed gradient equality may still be true, but the provided 6-line proof sketch does not establish it convincingly. The paper would benefit from a self-contained derivation or a clear statement of the needed assumptions.

2. **Privacy implications are not discussed.** The protocol requires clients to share their forward and backward policies \(p_F^{(n)}, p_B^{(n)}\) with the server. These policies encode information about high-reward regions and could leak information about the local reward functions or data. The paper does not acknowledge this limitation or discuss potential mitigations (e.g., differential privacy). This is a substantive omission for a paper framed around settings with "possibly sensitive" rewards.

3. **The sampling distribution \(\nu\) over trajectory pairs is underspecified.** Corollaries 1 and 2 require a "full-support probability distribution over pairs of terminal trajectories" but do not specify how \(\nu\) is chosen in practice, nor discuss how different choices affect variance or convergence of the FB/CB losses. In practice, one likely uses on-policy sampling, but this should be stated and justified.

4. **PCVI baseline is extremely weak.** The PCVI baseline assumes local reward distributions are products of independent categoricals, which is a gross misspecification for the structured state spaces studied. It unsurprisingly fails. The centralized GFlowNet is the proper baseline, and FC-GFlowNet performs well against it, so this is not a fatal issue — but the paper's presentation of PCVI as a meaningful competitor inflates the apparent improvement.

### Trivial

1. **Lemma 1 / CB relationship to TB should be more explicit.** The proof notes that CB is equivalent to TB with a specific constant \(Z = c(\tau)\), but the main text calls CB a "novel concept." Explicitly stating that CB is a reparameterization of TB (without learned \(Z\)) would improve clarity and avoid overclaiming.

2. **No algorithm pseudocode.** Given the multi-stage procedure (local training, server aggregation), a pseudocode summary would aid reproducibility.

3. **The bound in Theorem 2 is not empirically validated.** An experiment measuring \(\alpha_n,\beta_n\) and comparing the observed Jeffrey divergence to the bound would strengthen the paper, though its absence is not a flaw.

## Nice-to-Haves

- Empirical validation of the Theorem 2 bound (measure \(\alpha_n,\beta_n\) and compare observed vs. predicted divergence).
- Ablation: evaluate CB as the local training loss in the federated pipeline (clients use CB instead of TB/DB) to test whether CB's advantages carry over to the federated setting.
- Wall-clock time or sample efficiency comparison (L1 error vs. number of trajectory samples).
- Discussion of when the state graphs differ across clients (the current analysis assumes a shared graph).

## Removed Points

These points were flagged by reviewers but are removed per filtering rules. Treat them with caution:

1. **"Corollary 1 equation is garbled"** — The displayed equation for \(\mathcal{L}_{\text{Fed}}\) appears to have identical terms inside and outside the sum (both lack \(p_F^{(i)}\) superscripts). This is a PDF-to-text parser artifact. The original submission is assumed to have the correct expression, and the high-level idea (matching ratios across clients) is clear from Theorem 1.

2. **"The bound in Theorem 2 is not tested"** — This is a nice-to-have, not a weakness. The paper never claims to test the bound.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging from these reviews is the potential tension between the federated balance condition's dependence on the *exact* product of local policies and the practical reality that local models are imperfect. Theorem 2's bound on Jeffrey divergence in terms of \((\alpha_n,\beta_n)\) is formally reassuring, but the "catastrophic failure" remark (Remark 1) honestly acknowledges that a single poorly trained client can corrupt the aggregated result. This echoes similar hard lessons from parallel MCMC and suggests that practical FC-GFlowNet deployments would need robust client-side quality assurance mechanisms — a direction the paper does not explore.

## Suggestions

1. Provide a self-contained proof or a more carefully referenced derivation for Theorem 3, clarifying how the Malkin et al. (2023) results apply when \(Z\) is not jointly optimized.
2. Add a paragraph on privacy limitations: discuss what information the shared policies might leak and whether techniques like differential privacy could mitigate this.
3. Specify the practical choice of \(\nu\) (sampling distribution over trajectory pairs) for both FB and CB losses, with justification.
4. Add an algorithm pseudocode box summarizing the client training and server aggregation steps.

## Score and Decision

**Originality:** High. First work on federated learning for GFlowNets. CB is a useful reparameterization of TB.

**Importance:** High. Federated settings for generative models over discrete structures are relevant to drug discovery, distributed Bayesian inference, and multi-objective optimization.

**Claims support:** Good for the core contribution (federated balance, Theorem 1). The CB→VI connection (Theorem 3) is less rigorously supported.

**Soundness of experiments:** Good. Four diverse tasks with sensible metrics. The main comparison (FC-GFlowNet vs. centralized GFlowNet) is fair and informative.

**Clarity:** Adequate. The paper is clearly written at a high level but missing important details (algorithm pseudocode, specification of \(\nu\), privacy discussion).

**Value to community:** Significant. Opens up a new direction for GFlowNet research and provides a theoretically grounded starting point.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>