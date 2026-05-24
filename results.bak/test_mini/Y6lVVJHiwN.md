## Summary

FEDSGM introduces a unified algorithmic framework for federated constrained optimization that simultaneously addresses functional constraints, bidirectional compression with error feedback, multiple local updates, and partial client participation. The paper provides convergence guarantees for both hard and soft switching variants, demonstrating that the averaged iterate achieves the canonical $\mathcal{O}(1/\sqrt{T})$ rate while explicitly accounting for drift, compression, and sampling noise. The analysis recovers known rates as special cases.

---

## Strengths

- **First unified convergence analysis combining all four challenges.** Theorem 1 provides explicit convergence rates for FEDSGM that simultaneously account for functional constraints, bidirectional compression with error feedback ($\Gamma(q,q_0)$), multiple local updates ($\sqrt{E}$ factor), and partial client participation (high-probability bounds with $\sigma\sqrt{2\log(6T/\delta)/m}$). Prior work (e.g., Islamov et al. 2025) required full participation and $E=1$. This is a genuine theoretical contribution.

- **Recovery of known rates as special cases.** Section 3.1 shows that Theorem 1 reduces to the optimal $\mathcal{O}(DG/\sqrt{T})$ rate for centralized no-compression, to $\mathcal{O}(DG\sqrt{E}/\sqrt{T})$ for FedSGM without compression, and to $\mathcal{O}(DG/\sqrt{q_0 q T})$ for full participation with single-step updates. Each reduction matches existing results, confirming the framework's generality and internal consistency.

- **Soft switching analysis with geometric insight.** Theorem 2 proves that soft switching with $\beta \geq 2/\epsilon$ achieves the same $\mathcal{O}(1/\sqrt{T})$ rate as hard switching, while Section 3.2 provides a geometric explanation for oscillations via skew-symmetric matrices $K_{\text{glob}}$ and $K_{\text{loc}}$. Remark 1 identifies that even when global gradients align, client-level heterogeneity induces rotational drift — a novel insight absent from prior SGM works.

- **Ablation study confirming theoretical predictions.** Figure 2 systematically varies local steps ($E$), participation ratio ($m/n$), and compression ratio ($K/d$), showing that the empirical trends (diminishing returns from larger $E$, improved convergence from higher participation, slower convergence with aggressive compression) match the theoretical predictions.

---

## Weaknesses

### Fatal
None.

### Major

- **Complete absence of baseline comparisons.** The experiments compare only different configurations of FEDSGM against itself. There is no comparison to any existing method — not constrained FedAvg with projection, not FedADMM, not a centralized switching gradient method without FL complications, not even a simple Lagrangian approach. The "Centralized" entry in Table 1 is not a proper constrained baseline (it exceeds the safety margin at 33.2 cost vs. the 30 safety budget). Without external baselines, the paper cannot demonstrate that the unification provides any practical benefit over simpler alternatives. The paper's own framing ("To our knowledge, FEDSGM is the first...") is a novelty claim that the experiments do not test — they show the method works, not that it works better or comparably. For a paper proposing a new algorithmic framework, this is a critical gap.

- **Experiments on extremely small-scale problems.** The NP classification uses the breast cancer dataset (569 total samples) partitioned across 20 clients, yielding roughly 28 samples per client. The results are necessarily high-variance and the conclusions are not portable to realistic FL settings. The CMDP experiments use Cartpole, a simple control environment. Neither task provides evidence that FEDSGM scales or offers practical advantages in realistic federated settings.

- **"Centralized" baseline in CMDP is not a proper constrained method.** Table 1 compares FEDSGM variants against a "Centralized" method that exceeds the safety budget (33.2* cost at 500 rounds). The paper does not specify what this baseline is (centralized PPO? TRPO without constraints?), making it an inappropriate comparator. A proper baseline would be a centralized constrained RL method (e.g., CPO, constrained PPO). Comparison against a method that is not designed to satisfy constraints is misleading.

- **Convexity assumption versus non-convex experiments.** The entire theoretical analysis (Theorem 1, Theorem 2) relies on convexity of both $f_j$ and $g_j$ (Assumption 1). Yet the CMDP experiments involve deep RL with neural network policies — a highly non-convex setting. The paper acknowledges this limitation but does not bridge the gap. The RL experiments therefore cannot be considered validation of the theory; they are empirical exploration of a different regime without theoretical backing.

### Minor

- **Soft switching advantage is not rigorously quantified.** Figures 1 and 3 show qualitative differences between hard and soft switching, but the paper provides no numerical quantification (e.g., "soft switching reduces constraint oscillation amplitude by X%"). The theoretical rates for both variants are identical (Theorems 1 and 2), so the claimed practical advantage of soft switching rests entirely on qualitative visual evidence.

- **The constraint threshold $\epsilon$ serves dual roles.** The same parameter $\epsilon$ is used both as the target accuracy for the optimization problem and as the switching threshold in Algorithm 1. This conflates two distinct concepts and may cause the feasibility set $\mathcal{A}$ to be empty if $\epsilon$ is too small relative to optimization error. The theorem guarantees nonemptiness only under a specific $\epsilon$ choice that depends on unknown constants.

- **Assumption 4 (sub-Gaussian constraint evaluation gap) does not address temporal dependence.** The analysis uses concentration inequalities that typically require independent samples, but the iterates $w_t$ depend on previous samples, making the constraint evaluation process non-i.i.d. The paper mentions a union bound but does not address this dependence carefully.

- **No ablation isolating error feedback versus compression.** The paper compares compressed vs. uncompressed variants but does not isolate the effect of error feedback specifically (e.g., compression without EF). Given that EF is a core claimed contribution, this would strengthen the validation.

### Trivial
- The sketch on page 5 writes $\epsilon \gtrsim \text{optimization error} + \sigma\sqrt{2\log(6T/\delta)}/m^2$, while the theorem uses $\sqrt{2/m}$ — this appears to be a minor inconsistency in the informal discussion.

---

## Nice-to-Haves
- Compare against a constrained FedAvg (with projection after each round) and a FedADMM variant on the same tasks.
- Validate the $\sqrt{E}$ scaling prediction by plotting final objective/constraint as a function of $E$ for fixed $T$.
- Ablate the soft switching parameter $\beta$ over several orders of magnitude to characterize when soft switching truly differs from hard switching.
- Report wall-clock time or communication cost to contextualize speed-accuracy trade-offs.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"No experiment isolates the effect of bidirectional compression with EF"** — The paper does compare "No comp. (float32)" against compressed variants in Table 1 and Figure 2 (bottom row), providing an aggregate view of compression+EF effects. While a separate EF on/off ablation would be stronger, the claim that no isolation exists is too strong.

2. **"Reproducibility: insufficient specification of details"** — The paper provides code as supplementary material and references Appendix F for experimental details. The appendix is stripped by the parser; these details exist in the original submission.

3. **"The theory is a combination of known techniques... The bounds are complex but not surprising"** — This is a subjective opinion, not a specific verifiable weakness. It does not identify an error or gap in the paper.

4. **"The rates degrade with many practical factors"** — This is true for all convergence analyses with explicit constants. It is a generic critique of the entire convergence-rate genre, not a specific flaw of this paper.

5. **"No error bars for Table 1"** — The table reports results without standard deviations, but the text states results are "averaged over 5 runs with different random seeds" and Figure 3 shows 0.2 standard deviation bands. The table format is standard for such comparisons.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension (strong unified theory vs. severely incomplete experiments) but do not identify a contradiction or flaw in the theoretical reasoning itself. The harsh critic correctly identifies the experimental gaps but overstates some as fatal; the strengths are genuine but the weakness of no baselines is the binding constraint on the paper's impact.

---

## Suggestions

1. **Add baseline comparisons as a minimum requirement for publication.** Compare FEDSGM against: (a) a constrained FedAvg with projection after each round, (b) a centralized SGM without FL complications, (c) an ADMM-type method adapted for FL. Without these, the paper cannot demonstrate that the unification is practically meaningful.

2. **Scale up experiments.** Use a larger dataset (e.g., CIFAR-10 with a constrained fairness objective) to demonstrate that the method works beyond toy-scale problems.

3. **Replace or clarify the "Centralized" CMDP baseline.** Use a proper constrained RL method (CPO, constrained PPO) as a baseline, or clearly state that "Centralized" is an unconstrained optimizer and remove it from the primary comparison.

4. **Quantify the soft switching advantage numerically.** Report metrics such as oscillation magnitude, rounds to reach feasibility, or constraint violation frequency for both hard and soft switching.

5. **Provide a tighter connection between theory and experiments.** Validate the $\sqrt{E}$ scaling prediction by plotting convergence as a function of $E$. Report the empirical $q$ (compression accuracy) to connect with the $\Gamma$ terms in the theory.

---

## Score and Decision

**Calibration anchor summary:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| UJYhBfKuBE.md (WingsFL) | 3.00 | R1, weak | Weaker: inferior theory, topic (compression optimization) less central |
| DVfaLBUc2s.md (Dynamic Compression) | 2.40 | R1, weak | Weaker: limited contribution, not on constrained optimization |
| cUrshXsWYK.md (MARINA-P) | 3.00 | R1, weak | Weaker: narrower scope, no constraints or partial participation |
| zOWljZMbCm.md (ADI weighting) | 4.67 | R1, mid | Similar: combined known techniques, theory + limited experiments; accepted despite limited baselines |
| PSmakC4sw5.md (Composite EF) | 6.00 | R1, mid | Stronger: cleaner theory contribution (first EF in composite), has baselines in experiments |
| FnaDv6SMd9.md (Non-convex FL) | 5.50 | R1, mid | Stronger: stronger theory contribution with SOTA bounds, more thorough evaluation |
| hB8r4cdFTh.md (Cohort Squeeze) | 4.00 | R1, mid | Similar novelty level but has empirical baselines; rejected |
| aR7jXICvcL.md (SA-PEF) | 5.50 | R2 | Stronger: has extensive baselines and experiments, cleaner theory; still rejected |
| rex7s82Iav.md (EF21-Muon) | 6.00 | R2 | Stronger: broader theoretical scope (non-Euclidean), has baselines in experiments |
| 6PgOtwaEF8.md (FedSUM) | 4.50 | R3 | Similar: unified framework for arbitrary participation, limited experiments; rejected |
| 0KXI6lDM9C.md (Limited Scalability) | 5.50 | R3 | Stronger: clean lower-bound theoretical contribution, no experiments needed |

**Round 1 bracket:** The paper sits between the weak band (scores 2–3.33, papers with fundamental flaws) and the middle band (scores 4–6, papers with genuine contributions but varying experimental quality). The theory is real and non-trivial, placing it clearly above the weak band. The closest comparable anchors in the middle band are the ADI weighting paper (4.67, accepted despite limited experiments) and the FedSUM paper (4.50, rejected due to limited experiments).

**Round 2 narrowing:** Comparing against the ADI weighting paper (accepted at 4.67) — FEDSGM has stronger theoretical scope (unifying four challenges vs. two) but weaker experiments (ADI at least had CIFAR-10 with DIANA baselines; FEDSGM has no baselines at all). Comparing against SA-PEF (rejected at 5.50) — SA-PEF had extensive baselines and stronger experiments but was rejected for being incremental; FEDSGM is less incremental but has far weaker experiments. The FedSUM paper (4.50, rejected) is closest in profile: unified theory but limited experimental validation.

**Final score:** The paper's theoretical contribution is genuine and non-trivial — combining all four challenges in a single analysis is a clear advance over prior work that handles them only in pairs or triples. However, the experimental evaluation is critically incomplete: no baseline comparisons, extremely small-scale problems, and a strawman "Centralized" baseline. For a venue like ICLR, a theory paper with weak experiments can be acceptable if the theory is deep and the experiments at minimum validate feasibility against existing methods. Here, the experiments validate only that FEDSGM runs, not that it is useful. The paper would need substantial additional experimental work (baselines, larger-scale tasks) to be acceptable.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>