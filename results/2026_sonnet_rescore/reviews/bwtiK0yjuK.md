## Summary

This paper proposes the first offline change point localization and inference framework for dynamic multilayer random dot product graphs (D-MRDPGs). The two-stage algorithm combines seeded binary segmentation with CUSUM statistics (Stage I) and TH-PCA-based local refinement (Stage II), yielding consistency guarantees (Theorem 1) and the first limiting distributions for change point estimators in the network data setting (Theorem 2). A fully data-driven confidence interval procedure is derived and evaluated on simulations and real agricultural trade data.

---

## Strengths

- **First consistency result for offline CP localization in D-MRDPGs (Theorem 1):** The bound $|\tilde{\eta}_k - \eta_k| \leq C_c \log(T)/\kappa_k^2$ with high probability, combined with the consistency of $\tilde{K} = K$, constitutes a concrete and non-trivial advance over prior work (Wang et al., 2021 in single-layer; Wang et al., 2025 in online multilayer). The sharper localization rate ($\kappa^{-2}\log T$ vs. $\kappa^{-2}(d^2 m_{\max} + nd + Lm_{\max})\log(\Delta/\alpha)$ for the online setting) is quantified precisely in Remark 1.

- **First limiting distributions for change point estimators in network data (Theorem 2):** The two-sided Brownian motion limit $\kappa_k^2(\hat{\eta}_k - \eta_k) \xrightarrow{\mathcal{D}} \arg\min_{r} \mathcal{P}_k(r)$, distinguishing vanishing and non-vanishing jump regimes, is a genuinely novel result that enables the data-driven CI procedure in Section 3.1.

- **Strong simulation performance across diverse scenarios (Table 1):** CPDmrdpg achieves near-perfect detection and localization across all four scenarios—including two that deliberately violate Model 1—substantially outperforming gSeg and kerSeg on all metrics. For example, Scenario 4 ($n=100$): $|\hat{K}-K|=0.00$, Hausdorff distances $=0.00$, coverage $=100\%$, versus gSeg (frob.) coverage of 68.57%.

- **CI procedure with near-nominal coverage in three of four simulation scenarios (Table 2):** Scenarios 1, 2, and 4 achieve 100% coverage at nominal 95% for both $n=100$ and $n=150$, with tight average interval lengths (e.g., 0.003 for Scenario 1, $n=100$). This validates the asymptotic approximation in the well-specified settings.

- **Principled integration of Tucker decomposition and tensor PCA:** The Tucker low-rank structure of CUSUM-transformed adjacency tensors (Section 2.3) provides the key justification for applying TH-PCA in Stage II, bridging scalar change point methods and multilayer tensor estimation in a theoretically grounded way.

---

## Weaknesses

### Fatal
None.

### Major

- **Real-data confidence intervals are implausibly narrow given the asymptotic nature of the theory.** Table 4 reports 95% CIs for the agricultural trade network ($T=35$) of width 0.06 (e.g., the 1991 change point: $(5.97, 6.03)$) and 0.08 (the 2005 change point: $(17.97, 18.05)$). The CI procedure in Section 3.1 is explicitly asymptotic — it relies on Theorem 2 as $T \to \infty$ — and all simulation validation in Table 2 uses $T=200$. Whether the limiting distribution approximation is reliable at $T=35$ is not discussed anywhere in the paper. While the large number of observed edges per time point ($n=75$, $L=4$) may compensate somewhat, the paper neither justifies this extrapolation nor flags any caveat, and intervals narrower than the data's annual resolution by a factor of ~15 warrant explicit discussion.

- **The theory-to-practice gap from odd-even splitting is acknowledged but not analyzed.** Algorithm 1 formally requires four mutually independent network sequence copies. Section 2.2 states: "In practice (and in our numerical experiments in Section 4), Stage I and Stage II are implemented using the same two split tensor sequences via the odd-even splitting approach." This halves the effective time resolution and induces correlations the theory does not account for. Because Theorem 2 establishes a precise limiting distribution (not just a rate), even mild residual correlation from temporal splitting could perturb the distributional limit. The CI results in Table 2 are all generated under this splitting, not the four-copy input of the theory, so the formal validity of the CI coverage guarantees is left as an assertion. At minimum, the paper should note this gap explicitly and characterize conditions under which the approximation is expected to hold.

### Minor

- **CI coverage failure in Scenario 3 is under-diagnosed.** Table 2 reports 76.67% coverage at nominal 95% ($n=100$) in Scenario 3. The paper's explanation (Section 4.1) is a single sentence: "Coverage is lower in Scenario 3, where violations of Model 1 and relatively small, layer-specific changes pose greater challenges." Yet Scenario 3 — a change confined to community sizes in a single layer — is a realistic partial-violation case, precisely where multilayer aggregation should help. The failure could stem from biased variance estimation in Step 2 of Section 3.1 (since the variance formula assumes Model 1 holds), from the limiting distribution approximation being inaccurate at $T=200$ under misspecification, or from an identifiability issue when the signal is sparse across layers. Diagnosing which mechanism is responsible would materially strengthen the paper's practical claims.

- **Most relevant online baseline (Wang et al., 2025) is relegated to Appendix G.1.** The paper correctly notes in Section 4.1 that this comparison exists, and addresses the same underlying model. Moving at least a summary of that comparison into the main text (even as a condensed table) would directly quantify what the offline formulation contributes over online detection on common scenarios, grounding the rate comparison in Remark 1 with empirical evidence.

- **No variability measures for Monte Carlo results in Table 1.** For a paper whose core contribution includes inference, reporting only means across 100 MC trials without standard deviations or confidence bands leaves certain near-ties unresolvable (e.g., Scenario 3, $n=50$: CPDmrdpg $|\hat{K}-K|=0.19$ vs. kerSeg (nets.) $0.16$).

### Trivial
None (formatting artifacts are parser issues, per instructions).

---

## Nice-to-Haves

- Empirical wall-clock timing comparison at representative parameter settings (e.g., $n=100$, $L=4$, $T=200$) to ground the asymptotic complexity $O(Tn^2 Lr \log^2(T \vee n))$ claim.
- A brief finite-sample discussion of when the asymptotic CI approximation is expected to be reliable (e.g., as a function of $T$, $n$, $L$), even heuristic, to guide practitioners.
- The high-frequency change point experiments in Appendix G.1 represent a non-trivial practical extension (relaxing $\Delta = \Theta(T)$); a short mention in the main text would better convey the method's practical scope.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Assumption 2 not verified in simulations/real data.** The critic argues that it would be informative to check whether the detected change points satisfy the SNR condition. This is a general area-of-concern sweep: no specific violation is identified, and verifying SNR post-hoc is nonstandard in the statistics literature. The condition is stated transparently and is analogous to prior work. **Removed: speculative, no specific failure identified.**

- **Harsh Critic: Theorem 2 non-vanishing regime deferred to appendix.** The paper explicitly states this in Section 3 and the CI construction is for the vanishing regime. The non-vanishing case is addressed theoretically in Appendix A. **Removed: appendix-stripping artifact; the paper addresses this.**

- **Harsh Critic: Beating gSeg/kerSeg says little because they're non-parametric.** While the argument has merit organizationally, beating these methods under the four scenarios (including misspecified ones) does carry information about practical robustness. The harder concern — that the Wang et al. (2025) comparison is in the appendix — is already captured as a Minor weakness above. **Removed as a standalone criticism; subsumed.**

- **Strength Finder: "Addressed an important problem / targeted an interesting question."** Generic and not evidence-backed on its own. **Removed as a standalone strength.**

---

## Novel Insights

The paper's most structurally interesting finding is that the Tucker low-rank representation of CUSUM-transformed adjacency tensors enables a separation of the multilayer inference problem into a consistent Stage I coarse detection (operating on raw tensor CUSUM statistics) and a Stage II refinement (using TH-PCA to recover the expected probability tensor), where the refinement achieves a $\log(T)$ improvement over the coarse stage in localization rate. The limiting distribution result — a two-sided Brownian motion with layer-aggregated variance parameters $\sigma_{k,k'}^2 = \mathrm{Var}(\langle \Psi_k, \mathbf{E}_{k'}(1)\rangle)$ — cleanly separates the jump geometry (captured by the normalized jump tensor $\Psi_k$) from the noise structure, which has the practical implication that variance estimation in the CI procedure only requires projecting observed noise onto the estimated jump direction.

---

## Suggestions

1. In Section 4.2, add a brief discussion of why the asymptotic CI approximation is expected (or not expected) to be reliable at $T=35$; if the large $n^2 L$ term effectively increases the asymptotic precision, explain this explicitly.
2. In Section 3.1, add a remark quantifying the effect of odd-even splitting on the theoretical guarantees, or citing what conditions would be needed for the limit to carry through; even an informal argument would close the stated gap.
3. Move a condensed version of the Wang et al. (2025) comparison from Appendix G.1 into Section 4.1, and provide a concrete scenario comparing online vs. offline performance to empirically substantiate Remark 1.
4. Add standard errors to Table 1 results, at least for the near-tie entries.
5. For Scenario 3, run a targeted diagnostic experiment varying the fraction of layers that change to characterize the boundary of CI validity under partial model misspecification.

---

## Score and Decision

**Originality:** High. First offline CP framework for D-MRDPGs; first limiting distributions in the network CP literature.

**Importance of research question:** Moderate-to-high. Dynamic multilayer networks are increasingly prevalent; offline localization with inference is practically valuable.

**Claims supported:** Moderate. The consistency and localization claims (Theorem 1) are well-supported theoretically and empirically. The inference claims (Theorem 2, CI procedure) are theoretically grounded but the empirical validation has notable gaps (Scenario 3 coverage failure, real-data CI validity at T=35, sample-splitting gap).

**Soundness of experiments:** Moderate. Four well-designed simulation scenarios, including two that test robustness to model violation. Real-data analysis is qualitatively compelling but inference validity is questionable at T=35.

**Clarity of writing:** Good. Problem setup, algorithm, and theoretical results are clearly presented.

**Value to research community:** Moderate-to-high. The theoretical tools (Tucker CUSUM, TH-PCA refinement, Brownian motion limit) and the data-driven CI procedure are reusable beyond this specific model.

The paper makes a genuine and technically sophisticated contribution to a specialized but active area of statistics. The theoretical results are novel and appear correct. The experimental weaknesses — particularly the narrow real-data CIs at T=35 and the unanalyzed sample-splitting gap — would benefit from revision but do not invalidate the core claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>