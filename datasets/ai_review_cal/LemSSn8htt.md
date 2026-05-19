- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8
## Summary

This paper proposes Δ-AI, a training objective for amortized inference in sparse probabilistic graphical models. The key idea is to match conditional distributions of a learned Bayesian network sampler to those of a target Markov network using local constraints that involve only a single variable and its Markov blanket. This avoids instantiating all variables per gradient update, yielding a local loss (in the style of GFlowNets) with stronger per-step credit assignment. The method is theoretically grounded (Proposition 1) and evaluated on synthetic PGMs and latent-variable modeling of MNIST, showing substantial wall-clock speedups over GFlowNet baselines and competitive performance with MCMC and wake-sleep methods.

---

## Strengths

1. **Principled local objective with theoretical guarantee.** Proposition 1 proves that enforcing the local constraint (9) — which involves only a variable and its Markov blanket — for all single-variable perturbations is equivalent to global equality of the full joint distributions \(p = q\). This provides a clean theoretical foundation for the Δ-AI loss (Eq. 10), which contrasts with GFlowNet objectives that require a fully instantiated terminal reward.

2. **Dramatic wall-clock speedup over GFlowNets and MCMC on synthetic models.** Figure 4 shows Δ-AI converging orders of magnitude faster in wall-clock time than TB, DB, and FL-DB on the Ising ladder, Ising lattice, and factor lattice. Figure 5 demonstrates that after a short warm-up period, Δ-AI achieves substantially lower MMD than long-run Gibbs sampling and Gibbs-With-Gradients on peaky energy landscapes — a clear amortization benefit that training-free MCMC cannot match.

3. **Amortization over multiple DAG orders enabling partial inference.** Δ-AI simultaneously learns a single parametric model \(q_\theta\) to match conditionals from multiple I-maps (Figure 2). This allows inference over arbitrary subsets of variables without retraining, a capability not present in standard GFlowNets or variational methods. Figure F.2 (appendix) shows that amortizing over orders does not slow convergence relative to a single DAG.

4. **Effective on a real-world latent-variable modeling task.** In the MNIST variational EM experiment (Section 5), Δ-AI achieves faster wall-clock convergence in test NLL than all baselines (TB, DB, FL-DB, mean-field, wake-sleep, Gibbs) as shown in Figure 7, and generates high-quality unconditional samples with low classifier entropy.

---

## Weaknesses

### Fatal
None.

### Major

1. **Scalability claim is incompletely stress-tested.** The paper claims (line 14) that Δ-AI "scales well with respect to the dimension of variables." However, the method's efficiency depends critically on the chordal completion \(\overline{G}\) remaining sparse: the local loss (10) involves the Markov blanket in \(\overline{G}\), which can be much larger than the neighborhood in the original \(G\) if the graph has many immoralities. The paper acknowledges this limitation in §6. The experiments use graphs where chordalization adds few edges — the Ising ladder (chordal by design), the Ising lattice, and the factor lattice (both nearly chordal). The MNIST pyramid is custom-designed with small cliques. The paper does not demonstrate performance on graphs where chordalization significantly densifies the Markov blanket (e.g., a large grid with many immoralities or a random factor graph with controlled chordalization complexity). While the experiments are consistent with the claimed scalability, they do not probe the limiting case the authors themselves identify, leaving uncertainty about the method's practical range of applicability.

### Minor

1. **Advantage over IW wake-sleep on MNIST may be marginal.** Figure 7(b) shows that Δ-AI and importance-weighted wake-sleep (IW) converge to similar final NLL values. The paper claims Δ-AI "converges quicker than all other baselines" (line 250), but IW appears within one standard deviation at many time points. The mean prediction entropy (Fig. 7(c)) shows a more convincing separation, which is encouraging. Given that IW wake-sleep is simpler (no chordalization, no I-map requirement) and already uses local importance weights, the practical advantage of Δ-AI over IW in this particular setting is not as decisive as the synthetic results would suggest.

2. **GFlowNet baselines with multiple DAG orders are underdescribed.** The paper states (line 205) that "All algorithms amortize over multiple DAG orders." It is not standard for GFlowNets to operate over multiple DAG orders, and the paper does not describe how the TB, DB, and FL-DB baselines handle this — e.g., whether the ordering is randomly sampled per trajectory, how the flow function adapts, or whether the forward-looking parametrization (FL-DB) was given access to the same factor decomposition used by Δ-AI. The comparability of the baselines would be clearer with these details.

3. **No separation of wall-clock advantage from statistical efficiency.** The paper plots NLL vs. wall-clock time (appropriate for the speed claim), but does not report NLL vs. gradient steps or vs. number of energy function evaluations. This makes it difficult to disentangle whether Δ-AI's benefit comes from i) lower per-step cost (fewer variables to sample per update), ii) better credit assignment (stronger local signal per sample), or a combination of both. Reporting sample efficiency would strengthen the claim about the local objective itself, not just its computational cheapness.

4. **Hyperparameter sensitivity not reported.** The paper does not discuss sensitivity to the off-policy exploration rate, the choice of chordal completion algorithm, or the relative frequency of \(q_\theta\) and \(p_\psi\) updates in the EM loop. These are relevant for reproducibility and for understanding whether the reported advantages are robust across settings.

### Trivial

1. **Non-uniqueness of chordal completion not flagged early.** The paper notes in §2.1 that "any graph \(G\) can be made into a chordal graph \(\overline{G}\) by adding edges" (line 72) without mentioning that chordal completions are not unique and that their quality directly affects efficiency. This is acknowledged later in §6 but stating it early would help the reader.

2. **Loss enumeration assumes binary variables.** The loss (10) requires enumerating all possible perturbations \(x_u'\) of a variable, which is combinatorial for multi-valued discrete variables. The paper assumes binary variables (line 37) and could state this limitation more explicitly before the loss is introduced.

---

## Nice-to-Haves

- An experiment on synthetic graphs where chordalization adds a controlled number of edges (e.g., random factor graphs with varying immorality count) would sharpen the paper's contribution by either confirming the method's robustness or delineating clear applicability boundaries.
- A comparison against IW wake-sleep on synthetic posteriors with known ground truth would help isolate whether Δ-AI's local constraint yields a genuinely better approximation or converges to similar solutions at similar sample-efficiency rates.
- An evaluation of the stochastic estimator (described in §E of the appendix) on a synthetic graph with a large Markov blanket would address the chordalization scalability concern directly.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Missing comparison to contrastive divergence / persistent CD.* **Reason for removal:** Scope creep. CD is an MCMC-based negative-phase method for maximum-likelihood training of energy-based models, not an amortized inference method. The paper's experiments focus on amortized sampling from known PGMs and variational EM for latent-variable models — settings where CD is not a direct competitor. The paper already compares against MCMC (Gibbs, GWG) as the standard non-amortized sampling baseline.
- *Stochastic estimator not evaluated.* **Reason for removal:** The stochastic estimator is described in §E of the appendix, which is stripped from the parsed PDF. Per instructions, missing appendix content should not be counted as a weakness.
- *The description of \(q_\theta\) edges in §5 is unclear.* **Reason for removal:** On re-reading, the paper's phrasing is sufficiently clear: "has all edges from latent to hidden variables oriented upward" means edges from observed \(V \setminus H\) (below) to latent \(H\) (above), which is standard for a variational posterior that conditions on observations.
- *The statement about "real-world data" in §6 feels generic.* **Reason for removal:** This is a presentation nitpick about a single sentence in the discussion section and has no bearing on the paper's technical contributions.

---

## Novel Insights

The convergence of insight across the two reviews centers on a gap between the paper's framing and its evidence: the local objective is convincingly faster and better-credited on models where chordalization keeps Markov blankets small, but the experiments do not probe situations where chordalization breaks down. The strength finder rightly emphasizes the synthetic speedups (Fig. 4, Fig. 5) as the strongest evidence, while the harsh critic correctly notes that the MNIST experiment tells a more nuanced story — Δ-AI is faster but not dramatically better than a well-tuned IW wake-sleep. This pattern suggests that the paper's core contribution is strongest at what it explicitly targets: amortized sampling from known sparse PGMs, where the local constraint provides a clear computational and credit-assignment advantage over global GFlowNet objectives. The variational-EM setting inherits these benefits but is less decisive because wake-sleep methods can also exploit some structure via importance weighting.

---

## Suggestions

1. Add a controlled experiment varying the density of edges added by chordalization (e.g., by randomly removing edges from a chordal base graph to create immoralities) and plot convergence time vs. chordal Markov blanket size. This would directly address the main scalability concern and either confirm robustness or provide actionable guidance for practitioners.
2. In Figure 7(b), explicitly state whether the NLL gap between Δ-AI and IW is statistically significant at convergence (e.g., report a confidence interval or paired test), or tone down the "quicker than all baselines" claim to reflect the overlapping error bars.
3. Add a plot of NLL vs. gradient steps (or vs. number of energy evaluations) for the synthetic experiments to disentangle the effect of cheaper per-step cost from better credit assignment per sample.
4. Provide a brief description of how the GFlowNet baselines (TB, DB, FL-DB) were adapted to handle multiple DAG orders, to strengthen the fairness of the comparison.

---
