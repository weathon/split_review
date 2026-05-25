Now let me write the comprehensive final review, integrating all findings.

## Summary

This paper proposes two aggregation methods for multi-LLM decision-making: **Optimal Weight (OW)**, which is Bayesian-optimal when each model's accuracy is known, and **Inverse Surprising Popularity (ISP)**, which uses second-order information (pairwise answer correlations) to improve over majority voting without needing ground-truth labels. The paper provides theoretical analysis (OW optimality, ISP advantage ordering, finite-sample guarantees) and experiments on simulated data, UltraFeedback, MMLU, and the ARMMAN healthcare dataset.

## Strengths

1. **Clean Bayesian-optimality proof for OW (Theorem 1)**. The paper proves that under conditional independence and random label shuffling, a linear weight of the form \(w_i = \sigma_K^{-1}(x_i)\) (with \(\sigma_K(x)=e^x/(K-1+e^x)\)) achieves the maximum expected accuracy among all possible aggregators. This is a genuine theoretical contribution that goes well beyond ad-hoc majority voting and is correctly derived from first principles.

2. **Novel ISP algorithm connecting second-order information to aggregation**. The ISP rule is a thoughtful adaptation of the surprisingly popular (SP) mechanism, swapping the conditioning to create a controlled amplification of prediction bias. The paper shows (Theorem 2) that the expected *advantage* of the true label is ordered ISP > MV > SP, with closed-form expressions for the gap. The connection between the derived expressions and the intuition about LLM agents having smaller systematic biases than human crowds is insightful.

3. **Consistent empirical outperformance across multiple benchmarks**. In simulations (Table 2), ISP beats MV for all \(K \in \{2,4,6,8,10\}\). On real datasets (Table 3), all three proposed methods (OW-L, OW-I, ISP) outperform MV on UltraFeedback, MMLU, and ARMMAN. The per-question comparison (Table 4) and t-tests confirm the gains are statistically significant. The improvement on the disagreement subset (up to 3.36% absolute on MMLU) demonstrates practical value.

4. **Finite-sample guarantee for ISP (Theorem 3)**. The paper provides a high-probability bound showing that, with \(M\) questions to estimate second-order information, the empirical advantage gap over MV remains positive up to a \(\tilde{O}(1/\sqrt{M})\) error. This gives practical confidence when only limited data are available.

5. **Real-world healthcare application (ARMMAN)**. Testing on a maternal-health dropout prediction task demonstrates the methods' relevance in a critical domain, moving beyond standard NLP benchmarks.

## Weaknesses

### Major

1. **Theoretical claim for ISP is overstated — Theorem 2 proves expected advantage, not accuracy.** The paper repeatedly states that ISP "outperforms" MV and that the theoretical analysis "provably mitigates inherent limitations of majority voting" (abstract, introduction, conclusion). However, Theorem 2 only proves that the *expected advantage* of the true label is larger for ISP than for MV (\(\mathbb{E}[\mathrm{Adv}_{\mathrm{ISP}}(s^*)] \geq \mathbb{E}[\mathrm{Adv}_{\mathrm{MV}}(s^*)]\)). Each method selects the label with the *maximum advantage*, so a larger expected advantage for the true label does **not** directly imply a higher probability of selecting it — that depends on the full joint distribution of advantages across all labels. The gap between the proved result and the claimed conclusion is not addressed. This is not a fatal error — the empirical evidence independently supports ISP's accuracy gains — but it misrepresents what the theory establishes. The paper would be stronger if it clearly delineated what is proven (advantage ordering) and what is only observed empirically (accuracy improvement). *[Grounded in: Abstract line 9, Theorem 2 statement line 207, and repeated "outperform" claims throughout.]*

2. **Identical OW‑L and OW‑I results across all three datasets are unexplained and undermine experimental credibility.** In Table 3, OW‑L and OW‑I have identical accuracies (73.66%, 90.37%, 85.78%) on UltraFeedback, MMLU, and ARMMAN. In Table 4, the per-question discrepancy counts are identical (UltraFeedback: 2545/1727, MMLU: 1821/659, ARMMAN: 264/195). OW‑L solves an optimization problem (Eq. 7) to learn accuracies from second-order information, while OW‑I uses ISP pseudo-labels to estimate accuracies. These are methodologically distinct, so exact identity across all three datasets is highly improbable. This raises a serious concern about the experimental pipeline — whether a coding error, unintended information leakage, or some other artifact produced the duplication. The paper provides no explanation. This does not invalidate the ISP results (which differ from OW-L/OW-I on two of three datasets), but it directly undermines the credibility of the OW-L/OW-I experiments. *[Grounded in: Table 3, Table 4, Section 5.2 describing OW-L and OW-I as distinct methods.]*

### Minor

3. **Inconsistent definition of \(\sigma_K\) between abstract and main text.** The abstract defines \(\sigma_K(x) = \frac{x^2}{K-1+x^2}\), while Section 3 (where the theory is developed) uses \(\sigma_K(x) = \frac{e^x}{K-1+e^x}\). Only the latter yields the log-odds weight correctly derived from Bayesian optimality. The abstract definition produces \(\sigma_K^{-1}(x_i) = \sqrt{(K-1)x_i/(1-x_i)}\) instead of the correct \(\ln((K-1)x_i/(1-x_i))\). This appears to be a typo in the abstract but is confusing and suggests a presentational lapse. *[Grounded in: Abstract line 25 vs. Section 3 line 73.]*

4. **Limited baselines.** The experimental comparison is restricted to MV, SP, and a clairvoyant "Single Best" oracle. Several natural alternatives from the same problem setting are absent: confidence-weighted voting (mentioned in related work as Chen et al. 2023a; Fu et al. 2025), self-consistency with temperature sampling, and other unsupervised aggregation methods. While the paper's claims about beating MV are independent of these baselines, including them would substantially strengthen the evaluation. *[Grounded in: Table 3 baseline list; Section 1.1 related work mentions confidence-based methods without comparison.]*

5. **No variance estimates or confidence intervals on main results.** Table 3 and Table 4 report only point estimates without standard errors or confidence intervals. The t-statistics provided are a useful addition, but with large sample sizes even tiny differences become "significant." Reporting mean ± standard error or confidence intervals would give readers a clearer picture of the effect sizes and their reliability. *[Grounded in: Table 3, Table 4, Section 5.4.]*

### Trivial

- The abstract states that OW uses weight \(w_i\) as the "inverse function value of the sigmoid-like function \(\sigma_K(x) = \frac{x^2}{K-1+x^2}\)" — this is inconsistent with the body of the paper (see Weakness 3 above). Fix the abstract to match the main text.

## Nice-to-Haves

- A discussion of when ISP might fail — e.g., when estimated second-order information is noisy due to few samples, or when some models are close to random (the \((Kx_i-1)\) factor in Theorem 2 turns negative).
- Sensitivity analysis on the number of questions \(M\) used to estimate second-order information, complementing the finite-sample bound of Theorem 3.
- Release of anonymized code and data splits to improve reproducibility.

## Removed Points

These points were flagged by reviewers but are removed from the main weakness list with brief justification:

- **"The paper would benefit from replication code"** — Removing per Hard Rule (reproducibility nitpick about code release; the paper presumably intends to release code upon acceptance).
- **"Missing related works"** — Removing per Hard Rules (the paper has a dedicated related work section and Appendix A.1; the instruction forbids mentioning missing references).
- **"Typos and formatting issues"** — Removing per Hard Rules (parser artifacts, not author errors).
- **"The paper has no limitations section"** — Removing; the paper discusses future work and limitations are partially covered. The critic's concern about the conditional independence assumption is addressed by the paper's claim to extend results beyond this assumption in Appendix C.
- **"The author should use confidence intervals where large M makes tiny differences significant"** — Demoted to Minor weakness #5 above; the t-statistics are provided but variance estimates would strengthen the presentation.
- **Strength Finder's claims that ISP "strictly outperforms" MV and that Theorem 2 "provides a principled reason to prefer ISP"** — Partially removed because the theoretical claim is overbroad (see Weakness 1). The empirical outperformance is retained as Strength 3.
- **Strength Finder's claim that "the most compelling piece of evidence is Theorem 2"** — Removed; given Weakness 1, Theorem 2 is not the strongest evidence (the empirical results are).
- **Strength Finder's generic praise about addressing "an important and timely problem"** — Removed per Filtering rules (generic motivation praise with no specific evidence).
- **"Missing experimental details (prompts, tie-breaking)"** — Partially kept; these are reasonable reproducibility concerns but are minor. The paper's ISP algorithm explicitly uses the argmax of the advantage function, which has a built-in tie-breaking mechanism. Deferred to Nice-to-Haves.

## Novel Insights

The paper's core insight — that second-order information (pairwise answer correlations) can recover accuracy information without ground-truth labels, and that this can be exploited through a counterfactual twist on the surprisingly popular rule — is genuinely novel. The Bayesian-optimality result for OW under conditional independence is a well-executed application of standard information aggregation theory to the LLM setting; its connection to the Bradley-Terry model (Corollary 1) is a nice observation. None of the reviews surface any genuinely novel observation beyond what the paper itself claims.

## Suggestions

1. **Clarify the scope of Theorem 2.** Either prove that the advantage ordering implies accuracy ordering under the model, or explicitly state that the theoretical result concerns the expected advantage score and that accuracy improvements are empirically observed but not theoretically guaranteed. Revise the abstract, introduction, and conclusion accordingly.

2. **Explain or correct the OW‑L / OW‑I duplication.** If the identity is expected (e.g., because the two estimation methods converge to the same weights), provide theoretical or empirical justification. If it is an error, correct the tables and report the correct results. This is the single most important fix for restoring experimental credibility.

3. **Harmonize the \(\sigma_K\) definition.** Ensure the abstract uses the same function as the main text (\(e^x/(K-1+e^x)\)) to avoid confusion.

4. **Add at least one additional baseline** — confidence-weighted voting (weighting by LLM-reported confidence) would be straightforward and would better situate the paper within the broader ensemble literature.

5. **Report variance estimates** (standard errors or confidence intervals) for the main accuracy results, especially given that t-tests with large \(M\) can be misleading.

## Score and Decision

**Round 1 bracket**: Topic-anchored queries placed this paper between the weak band (< 3.5, containing clearly deficient papers) and the strong band (> 7.5, containing thorough papers with complete evaluation), in the mid band (3.5–7.5). Weakness-anchored queries for papers with overclaimed theory or methodological anomalies clustered around 4.5–5.75. **Initial bracket: 4.5–6.5**.

**Round 2 narrowing**: Direct comparison with anchors in the 4.5–6.0 range:
- *EnsemW2S* (5.50, Reject): similar quality tier — has genuine contributions but overclaimed results and methodological concerns.
- *SpecFuse* (5.33, Reject): comparable — genuine empirical gains but limited baselines and methodological concerns.
- *Balancing Act* (6.25, Accept): stronger empirical package but also has theory-evidence gaps; our paper has stronger theory but weaker experimental credibility (OW-L/OW-I issue).
- *Model aggregation: minimizing empirical variance* (6.00, Accept): solid theory and experiments, but also limited baselines.

**Final score**: The paper sits between the 5.5–6.0 anchors on theoretical merit but is pulled downward by the unexplained OW-L/OW-I duplication (which the 5.5–6.0 anchors do not have). Score **5.5** — the paper has genuine contributions (Bayesian-optimal OW, novel ISP, strong ISP empirical results) but the overclaimed ISP theory and the unexplained experimental duplication are significant issues that prevent it from being a clear accept.

**Anchor list** (all papers retrieved across calibration rounds):

| Anchor ID | Avg Score | Round/Query | Comparison |
|-----------|-----------|-------------|------------|
| ujNe7sybJu | 2.50 | R1-topic-low | Much weaker — lacks any theoretical grounding |
| E2CR6hmV1I | 3.00 | R1-topic-low | Much weaker — limited scope |
| 56mg1JFd3n | 3.00 | R1-topic-low | Weaker — different domain (long-context retrieval) |
| cSnbM9SIJJ | 3.00 | R1-topic-low | Much weaker — multi-agent simulation platform |
| SO0manOwUF | 5.50 | R1-topic-mid | Comparable — MLLM merging, has methodological gaps |
| **Dl6nkKKvlX** | **6.25** | **R1-topic-mid** | **Stronger empirically, weaker theory; similar genre (LLM ensemble)** |
| lhLQpS33YL | 5.33 | R1-topic-mid | Comparable — SpecFuse, has baseline & cost concerns |
| grM2Yv49cI | 6.00 | R1-topic-mid | Stronger — model aggregation with cleaner evaluation |
| Iyrtb9EJBp | 8.00 | R1-topic-high | Much stronger — thorough evaluation, complete |
| WbWtOYIzIK | 8.00 | R1-topic-high | Much stronger |
| GGlpykXDCa | 8.00 | R1-topic-high | Much stronger |
| rfdblE10qm | 8.00 | R1-topic-high | Much stronger |
| KX5hd1RhYP | 4.67 | R1-weakness (overclaimed metric) | Weaker — different domain, similar "metric vs. claim" gap |
| 28U5Olm32r | 5.75 | R1-weakness (ensemble theory) | Comparable — ensemble theory paper, similar theory-evidence gap |
| G3OCarOfxx | 4.80 | R1-weakness | Less relevant |
| PCXvcULwiI | 5.50 | R1-weakness (suspicious results) | Different domain, similar data integrity concern |
| tqHgSxRwiK | 3.00 | R1-weakness | Much weaker |
| UkLSvLqiO7 | 5.50 | R1-weakness | Different domain |
| HvkXPQhQvv | 6.00 | R1-weakness (Bayesian aggregation) | Comparable — Bayesian aggregation without labels, cleaner eval |
| W6hzM9DMMU | 6.00 | R1-weakness | Less relevant |
| wHgu98u8Sc | 4.40 | R1-weakness | Weaker — small-data ensemble |
| **OIEczoib6t** | **5.50** | **R2** | **Most comparable — EnsemW2S, similar quality tier and issues** |
| 7rzA6aEASo | 5.60 | R2 | Less relevant — random feature ensembles |
| ueqTjOcuLc | 5.00 | R2 | Weaker — multi-agent collaboration paper |
| WVWZ6SnM4t | 4.75 | R2 | Weaker — group decision-making |
| obYDlJN0oU | 4.25 | R2 | Weaker — value understanding |
| Bp2axGAs18 | 5.20 | R2 | Weaker — multi-agent resilience |

**What the low-band anchors failed at**: Papers scoring 3.0 or below had either no meaningful theoretical contribution, severely flawed evaluation, or contributions too narrow for the venue. The paper under review does not share these failures — it has a genuine theoretical result (OW optimality) and generally sound empirical methodology (with the caveat of the OW-L/OW-I issue). The score reflects that the paper has genuine contributions but is held back by the overclaimed ISP theory and the unexplained experimental duplication.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>