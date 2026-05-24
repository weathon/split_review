Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). It proposes a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation, establishes consistency guarantees, derives limiting distributions for refined change point estimators (the first such results in the network literature), and develops a data-driven confidence interval procedure. Empirical results show strong performance across diverse simulation scenarios and a real-world agricultural trade network analysis.

## Strengths

1. **First study of offline change point detection in dynamic multilayer networks with consistency guarantees.** The paper proposes a novel two-stage procedure (seeded binary segmentation + tensor-based refinement) that is genuinely new for this setting, and Theorem 1 establishes that the algorithm correctly estimates both the number and locations of change points with high probability.

2. **First limiting distributions for change point estimators in network data.** Theorem 2 derives the limiting distribution of the refined estimator under vanishing jumps, involving a two-sided Brownian motion process. This is a nontrivial theoretical contribution that goes well beyond the consistency bounds typical in this literature.

3. **Improved localization rate compared to prior work.** Remark 1 explicitly documents that the achievable rate is $\kappa_k^{-2}\log(T)$, which is substantially sharper than the rate from the online setting of Wang et al. (2025) because it removes dependence on $n$, $d$, $L$, and $m_{\max}$.

4. **Strong empirical performance across diverse scenarios.** Table 1 shows that CPDmrdpg achieves near-perfect metrics (e.g., $C(\hat{G},G)=100\%$) in Scenarios 1, 2, and 4, and outperforms both gSeg and kerSeg by wide margins. The method also shows robustness when Model 1 is violated (Scenario 3, $C(\hat{G},G)=99.98\%$ at $n=100$).

5. **Data-driven confidence interval construction with good empirical coverage.** Section 3.1 provides a fully specified CI procedure, and Table 2 shows 95–100% coverage for $n=150$ across all four scenarios, with narrow average lengths.

## Weaknesses

### Fatal
None.

### Major

1. **Confidence interval procedure lacks a formal theoretical coverage guarantee.** Theorem 2 gives the limiting distribution of $\hat\eta_k$ under two critical idealizations: (i) "oracle" intervals $(\tilde s_k,\tilde e_k)$ are assumed to contain the true change point with correct segment boundaries, and (ii) the jump tensor is known. The procedure in Section 3.1 then plugs in estimates of the jump size, normalized jump tensor, and variances — all obtained from the same data and preliminary estimators — without any theorem stating that these plug-in estimates yield asymptotically valid coverage. While the empirical results in Table 2 are encouraging, the paper's inference claim (one of its headline contributions) is not fully supported by theory. The suspiciously narrow confidence intervals in the real-data example (Table 4: $(5.97,6.03)$ for time index 6, with $T=35$ and $n=75$) further suggest the variance estimators may be underestimating uncertainty in practice, underscoring the need for a formal justification.

### Minor

2. **Low-rank assumption is acknowledged but not characterized.** Assumptions 1(ii)–(iii) impose low-rank conditions on the CUSUM and average $Q$ matrices that are necessary for the theory. The paper traces these to constraints on $\{Q(\eta_k)\}$ and notes that "such ambiguity is common in tensor-based models" (page 5), but it does not characterize what natural classes of weight matrices satisfy this condition or how a practitioner might verify it. The theory therefore applies to an uncharacterized subclass of D-MRDPGs. This limits the practical scope of the guarantees.

3. **Limited baseline set in the main text.** The main experimental section only compares against gSeg and kerSeg. The paper mentions additional comparisons (Wang et al., 2025; Li et al., 2024) in Appendix G.1, but relegating these to the appendix weakens the claim of "substantially outperforming existing state-of-the-art algorithms" in the main narrative.

### Trivial

4. **Algorithm notation ambiguity.** Algorithm 1 uses notation $|(\tilde{\mathbf{A}}^{\alpha,\beta}(t), \tilde{\mathbf{B}}^{\alpha,\beta}(t))|$ without explicitly defining the inner product $(\cdot,\cdot)$. The Frobenius inner product $\langle\cdot,\cdot\rangle$ is defined in Section 1.2 for tensors, so $(\cdot,\cdot)$ can be inferred, but the paper should be explicit. Similarly, it should state that $\tilde{\mathbf{A}}^{\alpha,\beta}(t)$ and $\tilde{\mathbf{B}}^{\alpha,\beta}(t)$ are computed via Definition 4 on sequences $\{\mathbf{A}(t)\}$ and $\{\mathbf{B}(t)\}$, respectively.

5. **Suboptimal real-data confidence intervals labeled as "confidence" without qualification.** Table 4 reports 95% CIs of width ~0.06–0.08 time units (roughly 3–4 weeks on annual data). The paper should explicitly note that these intervals are constructed under the assumption that the plug-in procedure is valid, since the theoretical coverage guarantee has not been established.

## Nice-to-Haves

- Provide guidance on tuning $\tau$ and input ranks beyond the one heuristic ($c_{\tau,1}=0.1$). A brief sensitivity summary in the main text would be helpful.
- Mention the non-vanishing jump regime result (Appendix A) briefly in the main text for completeness.
- Include a short discussion in Section 5 or the introduction about when $Q(t)$ matrices might be expected to be low-rank (e.g., shared latent factors across layers, factor model structure).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper never discusses when such weight matrices would be low-rank"** — The paper does discuss this on pages 4–5, tracing the low-rank condition to $\text{rank}(Q(\eta_k)) + \text{rank}(Q(\eta_{k+1}))$ and acknowledging the ambiguity. The characterization is admittedly shallow, but the claim that it is "never discussed" is inaccurate.

2. **"Sub-unit-width interval on an integer-indexed time axis is mechanically unsound"** — This misinterprets the nature of the parameter. Change point locations are modeled as continuous parameters in the theory; fractional CIs are standard in change point inference (the limiting distribution in Theorem 2 involves Brownian motion on $\mathbb{R}$). The narrowness is a legitimate concern about potential underestimation, but it is not "mechanically unsound."

3. **"Confidence interval procedure... The paper does not discuss the impact of the non-vanishing jump regime on the interval construction"** — This is a scope point: the CI procedure is explicitly designed for the vanishing regime, and the non-vanishing regime is deferred to Appendix A. Criticizing this is scope creep.

4. **Generic strength from Strength Finder (#6):** "Interpretable real-data results aligned with known events" — While true, this is a demonstration, not a core strength of the paper's contribution. Moved here.

5. **Strength Finder claims about "superior performance and practical utility" being a core strength** — These are supported by evidence but are standard claims; they are folded into strengths 4 and 5 above rather than listed separately.

## Novel Insights

The reviews surface an important tension in this paper: the theoretical contribution (limiting distributions for change point estimators in networks) is genuinely novel and technically challenging, but the inference procedure built on top of it lacks a formal coverage guarantee — and the real-data CIs appear suspiciously tight. This gap between the sophistication of the theory and the validation of its downstream use is the paper's central unresolved issue. The low-rank assumption, while acknowledged, is another instance where the theoretical framing is clean but the practical connection unexamined. Neither issue is fatal on its own, but together they suggest the paper's contributions are strongest on the point-estimation side (detection/localization consistency) and weaker on the inference side (uncertainty quantification).

## Suggestions

1. **Prove asymptotic validity of the plug-in CI procedure** or provide a heuristic derivation showing that the plug-in estimates of $\kappa_k$, $\Psi_k$, and $\sigma_{k,k'}^2$ converge fast enough that the limiting distribution in Theorem 2 still applies. If a full theorem is not possible, add a bootstrap-based CI procedure (e.g., Cho and Kirch, 2022) as an alternative.
2. **Characterize when the low-rank assumption holds** — e.g., when layers share a low-dimensional factor structure. A brief proposition or even a simulation demonstrating that the method degrades gracefully as rank increases would substantially strengthen the paper.
3. **Move or summarize the additional baseline comparisons** (Wang et al., 2025; Li et al., 2024) from Appendix G.1 into the main experimental table.
4. **Resolve the algorithm notation ambiguity** by explicitly defining $(\cdot,\cdot)$ as the Frobenius inner product and clarifying that $\tilde{\mathbf{A}}^{\alpha,\beta}(t)$ is computed via Definition 4 on $\{\mathbf{A}(t)\}$.

## Score and Decision

Based on calibration against human-reviewed anchors:

**Round 1 (bracketing):** Weak-anchor papers (avg 2.33–3.33, unrelated topics) are clearly below this paper. Middle-anchor papers (avg 4.80–6.00, graph/network topics) are the relevant comparison set. Strong-anchor papers (avg 7.60–8.00) are clearly above. Initial bracket: [4.5, 6.5].

**Round 2 (narrowing):** Within the bracket, key anchors include:
- *Node Similarities under Random Projections* (avg 5.80, accepted poster): Solid graph theory paper with clear contributions; presentation issues noted by one reviewer. This paper's theoretical contribution is at least as novel, but its CI coverage gap is a more serious weakness than the Node Similarities paper's presentation issues. Comparable but slightly weaker.
- *Exploring Edge Probability Graph Models* (avg 5.75, rejected): Graph model paper with limited validation and missing comparisons. This paper has stronger theory and more complete experiments, placing it above this anchor.
- *Online Detection for Black-Box LLMs* (avg 5.25, rejected): Change point detection paper with weak baselines and questionable problem framing. This paper has stronger theory, clearer motivation, and more complete evaluation. Clearly above.
- *γ-Orthogonalized Tensor Deflation* (avg 5.25, rejected): Narrow theoretical scope, poor presentation. This paper is stronger in both scope and experimental validation.

**Final calibration:** The paper sits around the 5.0–5.5 mark. Its theoretical contributions are genuine and well-supported by consistency proofs. However, the CI coverage gap is a significant omission for one of the paper's headline claims, and the narrow real-data CIs suggest the inference procedure needs further validation. The paper is above the rejected anchors (4.25–5.25) but below the accepted graph paper (5.80) due to the unresolved inference gap.

**Score: 5.0** — Marginally below the acceptance threshold. The paper addresses a novel and important problem with real theoretical contributions, but the lack of a formal coverage guarantee for the CI procedure and the uncharacterized low-rank assumption prevent acceptance in current form. With substantial revision — particularly a theoretical or bootstrap-based coverage guarantee — the paper could be a strong candidate for resubmission.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>