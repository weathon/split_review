Now I have sufficient calibration data. Let me produce the final consolidated review.

## Summary

This paper provides the first absolute (as opposed to relative) utility guarantees for differentially private set union, by reframing the problem in terms of missing mass rather than cardinality. The core theoretical contribution proves that the Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass under Zipfian data (Theorem 3.3 with matching lower bound Theorem 3.5), plus a distribution-free ℓ∞ missing mass guarantee (Theorem 3.6). These results are then leveraged to obtain the first utility guarantees for unknown-domain variants of top-k selection (Theorem 4.3) and k-hitting set (Theorem 4.5) via a simple two-stage pipeline. Experiments on six real datasets demonstrate that the WGM-based methods are empirically competitive with existing approaches.

## Strengths

- **First absolute utility guarantees for DP set union:** Section 1.1 correctly notes that all prior utility results for set union are stated relative to other algorithms. The paper delivers on this claim with concrete, high-probability bounds on missing mass.

- **Near-optimal ℓ₁ missing mass on Zipfian data:** Theorem 3.3 (upper bound) and Theorem 3.5 (lower bound) match in their ε and N dependence (up to logarithmic factors), establishing near-optimality of the WGM for this problem class. The lower-bound proof exploiting Assumption 1 is technically clean.

- **Novel utility guarantees for unknown-domain top-k and k-hitting set:** Theorems 4.3 and 4.5 give the first utility bounds for these problems in the unknown-domain setting. The approach of running WGM as a domain-discovery precursor and then composing with a known-domain algorithm is simple, practical, and yields nontrivial guarantees.

- **Distribution-free ℓ∞ bound enables broad applicability:** Theorem 3.6 does not require any Zipfian assumption, which allows the downstream top-k and k-hitting set guarantees to apply to arbitrary datasets. This clean separation of the domain-discovery step from the selection/hitting step is architecturally nice.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theorem 3.6 uses an undefined symbol s:** The theorem statement reads "$T = \hat{\Theta}_{\Delta_0, s}(\max\{\sigma, 1\})$", but $s$ is never defined in Theorem 3.6 (which is explicitly distribution-free and does not assume Zipfian parameters). This appears to be a copy-paste artifact from Theorem 3.3. The $s$ subscript should be removed or replaced with the relevant parameters ($\Delta_0$, $\delta$). While the asymptotic meaning is clear (the threshold scales as $\tilde{\Theta}(\max\{\sigma,1\})$), the formal statement as written is technically incorrect.

- **Set union experiments compare against baselines optimized for cardinality, not missing mass:** The Policy Gaussian (Gopi et al., 2020) and Policy Greedy (Carvalho et al., 2022) baselines were explicitly designed to maximize the *number* of recovered items (cardinality), not to minimize missing mass. The paper acknowledges this contrast ("previous empirical results for cardinality") but does not tune or adapt the baselines to the missing-mass objective. The claim "WGM obtains MM within 5% of that of the policy mechanisms" is an empirical observation — it adds texture but does not constitute a strong experimental endorsement, since the baselines may be far from optimal for missing mass. This does not threaten the theoretical claims, but the experimental framing could be more precise.

- **Experimental variance reporting is uneven:** Figure 1 reports only averages over 5 trials without any variance indication. Figure 3 does report standard error, but Figure 1 (the main set union result) lacks this. Adding standard error bars or confidence intervals to Figure 1 would improve interpretability.

### Trivial

- **Corollary 4.6 notation is unconventional:** The inequality $\mathbb{E}[\text{Hits}] \geq \text{Opt} - \tilde{\Omega}(k/\epsilon)$ is mathematically valid as a lower-bound statement about additive error, but the $\tilde{\Omega}$ inside a subtracted term on the RHS can be confusing. A clearer formulation would be $\text{Opt} - \mathbb{E}[\text{Hits}] \geq \tilde{\Omega}(k/\epsilon)$. This is a notational preference, not an error.

## Nice-to-Haves

- A brief ablation study showing the effect of $\Delta_0$ on top-k and k-hitting set performance would strengthen the empirical section (the set union experiments vary $\Delta_0$, but the downstream experiments fix it at 100).
- Providing a self-contained privacy proof sketch for Algorithm 1 would make the paper more self-contained, though citing Theorem 5.1 of Gopi et al. (2020) is standard and sufficient for a conference paper.

## Removed Points

These points were removed from the input reviews; they are flagged here for transparency but should be treated with caution:

- **"Privacy guarantee of WGM may depend on subsampling scheme not fully verified"** (Harsh Critic #2): The paper states Theorem 3.2, which is Theorem 5.1 of Gopi et al. (2020), and Algorithm 1 is exactly the WGM described in that work. Citing a published privacy theorem for one's exact algorithm is standard practice. The concern is unwarranted.
- **"Corollary 4.6 inequality direction is wrong"** (Harsh Critic, last bullet): The inequality $\mathbb{E}[\text{Hits}] \geq \text{Opt} - \tilde{\Omega}(k/\epsilon)$ is a conventional way to express a lower bound on additive error in the DP literature. The critic's claim that it should be $\leq$ reflects a misunderstanding of the $\tilde{\Omega}$ notation in this context.
- **"Error bars not defined"** (Harsh Critic): The paper explicitly states "along with its standard error across 5 trials" for Figure 3 (line 321). For Figure 1, the paper reports averages without error bars — this is noted as a minor weakness above, but the critic's blanket claim that error bars are undefined is incorrect.
- **"Asymmetric baseline settings are confusing and should be justified"** (Harsh Critic on top-k experiments): The paper explains the asymmetric $\Delta_0$ settings come from Durfee & Rogers (2019) recommendations. Setting $\Delta_0=\infty$ (no truncation) helps the baseline, so any advantage WGM shows is despite this concession. This is correctly handled.
- **Strength Finder claims about experiments "outperform or compete with existing baselines"**: This is verified as an accurate summary of Section 5, so it is retained in the Strengths section.

## Novel Insights

Beyond the paper's own contributions, the most striking structural insight is that missing mass — an ℓ₁-weighted metric — is the "right" language for DP set union guarantees, while prior work focused on cardinality (ℓ₀). The Zipfian assumption elegantly sidesteps the well-known hardness example (all-unique items) while capturing realistic data distributions, and the matching lower bound confirms this is not a free lunch: the dependence on $s$ (Zipfian exponent) in the bound is genuine. The two-stage decomposition (WGM for domain discovery + known-domain algorithm) is methodologically clean: it separates the information-theoretic difficulty of *finding the domain* from the combinatorial difficulty of *selecting within it*, with the ℓ∞ bound on missing mass serving as the bridge.

## Suggestions

- Fix the undefined $s$ in Theorem 3.6's threshold expression.
- Add standard error bars to Figure 1 (or at minimum note the variance).
- For the set union experiments, add a brief discussion acknowledging that the baselines were designed for cardinality, not missing mass, explaining why the comparison remains informative.

## Score and Decision

**Calibration summary.**

*Round 1 (bracketing, 3 queries):*
| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| WhIuLQWCWS — DP Federated K-Means | weak | 3.00 | R1 | Much weaker; vague contributions, no real theory |
| uxFme785fq — Nonlinear Inference Learning DP | weak | 2.50 | R1 | Much weaker; poorly motivated |
| nM2kuesKpC — D2P2-SGD | weak | 3.00 | R1 | Much weaker; incremental |
| TbOcySs6g8 — Synthetic Dataset Alignment DP | weak | 2.50 | R1 | Much weaker; empirical, no substance |
| S6Dn3uyM2p — DP One Permutation Hashing | middle | 4.60 | R1 | Weaker; narrower contribution, less theory |
| hVTaXJ0I5M — Privately Counting Partially Ordered Data | middle | **6.75** | R1 | Comparable; solid theory paper, similar DP depth |
| FZS5m1cbFU — DP Range Subgraph Counting | middle | 5.67 | R1 | Weaker; good algorithm but less tight bounds |
| yLhJYvkKA0 — DP Hierarchical Clustering | middle | **6.67** | R1 | Comparable; similar structure (upper/lower bounds + experiments) |
| EUSkm2sVJ6 — Dataset Usage Cardinality Inference | strong | 7.60 | R1 | Stronger; more polished, broader impact case |
| oZtt0pRnOl — DP Few-Shot Generation | strong | 8.00 | R1 | Stronger; different subfield, very polished |
| A3YUPeJTNR — Hidden Cost of Waiting | strong | 8.00 | R1 | Stronger; different area, excellent exposition |
| fMTPkDEhLQ — Tight Lower Bounds Hölder | strong | 8.00 | R1 | Stronger; pure optimization theory, very tight analysis |

*Round 2 (narrowing within bracket 5.5–7.5):*
| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| fbqOEOqurU — Optimality of Matrix Mechanism ℓₚᵖ | 7.00 | R2 | Slightly stronger; tighter lower bounds, more technical depth |
| txV4dNeusx — Near-Exact Privacy Amplification for Matrix Mechanisms | 6.25 | R2 | Weaker; narrower scope, more applied |
| uqWM9hBDAE — Missing Mass Estimation (no DP) | 7.33 | R2 | Stronger but on a different problem; polished empirical paper |
| E60SIDItyT — Learning from Aggregate Responses | 6.00 | R2 | Weaker; less technical depth |

*Round 1 bracket:* [5.5, 7.5]. The paper clearly sits above the 3.0–4.6 anchors and below the 7.6–8.0 strongest anchors.

*Round 2 narrowing:* The paper is most similar to the 6.67 (hierarchical clustering DP) and 6.75 (partially ordered data) anchors — all are theory-first DP papers with matching upper/lower bounds and supporting experiments. The paper under review has a broader scope (three problems vs. one) and fills a clearer gap (first absolute guarantees for set union), but its experiments are less polished than the 7.00–7.33 anchors. The paper is stronger than the 6.25 and 6.00 anchors. This places it at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>