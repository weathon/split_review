**What did the low-band anchors fail at, and does the paper under review share any of those failures?**

The low-band topic anchors (scores 3.0–3.4) were papers with unclear contributions, weak evaluations, or fundamental misunderstandings in their causal reasoning — the ZNet paper does not share those failures: it has a clear architecture, well-defined loss functions, and an extensive empirical evaluation. The weakness-anchored hits with theoretical errors (e.g., `F7XPZnIUHh`, 4.20) did share a key failure mode with this paper: an error in a theoretical proof that undermines a claimed advantage. That similarity is relevant and prevents the paper from being scored in the 5+ range.

---

## Anchor List

| Anchor | Avg Score | Round & Query | Comparison to Paper Under Review |
|--------|-----------|---------------|----------------------------------|
| `qDhq1icpO8` — Conditional IV Regression with Representation Learning for Causal Inference | 6.75 | R1-topic-mid | More rigorous theory (proven identification), similar topic. Paper under review is less theoretically sound. |
| `F7XPZnIUHh` — Adversarial Learning of Decomposed Representations | 4.20 | R1-topic-mid, R2-narrow, R1-weakness | Shares theoretical error in proof and comparison concerns. Paper under review has more comprehensive evaluation. |
| `Q2bJ2qgcP1` — Do Contemporary CATE Models Capture Real-World Heterogeneity? | 6.00 | R1-weakness | Large-scale benchmark with rigorous evaluation. Paper under review has tighter focus but less rigorous variance reporting. |
| `Oc4ji1iCjQ` — Catch the Shadow | 6.75 | R2-narrow | Better theory, some evaluation concerns. Paper under review has weaker theory. |
| `TC9r8gsaoh` — Nuisance-Robust Weighting Network | 6.00 | R2-narrow | Better theoretical grounding. Paper under review has more comprehensive IV-specific evaluation. |
| `4u0ruVk749` — DFITE: Diffusion Model for ITE | 3.00 | R1-topic-low | Weak evaluation and unclear contribution. Paper under review is substantially stronger. |
| `5AJ8R4z5g0` — Potential Outcomes Under Hidden Confounders | 3.25 | R1-topic-low | Unclear scope. Paper under review is clearer and better motivated. |
| `0sO2euxhUQ` — Learning Latent Structural Causal Models | 4.00 | R1-topic-mid | Ambitious but incomplete. Paper under review has more concrete empirical results. |
| `sSWGqY2qNJ` — Indeterminate Probability Theory | 3.33 | R1-weakness | Different topic; theoretical issues. Not directly comparable. |
| `OXIIFZqiiN` — Dual-Modal Framework | 1.50 | R1-weakness | Unrelated topic, very weak. Not comparable. |
| `MqEQbvPvkE` — Causal Estimation of Exposure Shifts | 5.00 | R2-narrow | Applied causal paper, accepted. Paper under review is more method-focused. |
| `qsAckNdySL` — Causality is Invariance Across Heterogeneous Units | 4.25 | R2-narrow | Abstract theory, unclear evaluation. Paper under review has stronger empirical work. |

**Round-1 bracket:** 3.5–6.5. **Round-2 narrowing:** confirmed the paper sits between 4.0 and 5.5, closest in profile to `F7XPZnIUHh` (4.20) but with stronger empirical evaluation.

---

## Summary

This paper proposes ZNet, a deep learning architecture that learns instrument and confounder representations \(Z = g(X), C = f(X)\) from observed covariates \(X\) by enforcing moment constraints (covariance/variance conditions) derived from standard IV assumptions: relevance, exclusion restriction, and unconfoundedness. The learned representations can then be fed into downstream IV estimators (TSLS, DeepIV, DFIV) for causal effect estimation. The paper evaluates ZNet across ten semi-synthetic data settings with varying instrument availability and demonstrates competitive ATE estimation.

## Strengths

1. **Clear architectural design with well-motivated loss constraints.** The ZNet architecture directly encodes the three IV conditions (relevance, exclusion restriction, unconfoundedness) as differentiable loss terms, providing a transparent and principled framework for learning instrument representations. The staged training procedure and use of both Pearson correlation and mutual information losses are sensible.

2. **Demonstrated ability to recover ground-truth instruments.** Figure 4 shows perfect recovery of a latent categorical instrument (diagonal confusion matrix = 1.0), and Figure 5 shows strong correlation between learned \(Z\) and the true instrument variables in the Mixed Candidate setting. The ablation study (Figure 5c) confirms each constraint contributes to recovery.

3. **Comprehensive and systematic evaluation.** The paper constructs ten distinct semi-synthetic settings varying linearity (linear/nonlinear), instrument existence (Disjoint/Mixed/Latent/No Candidate), and unobserved confounding presence. Three downstream IV estimators are tested, and 50 bootstrap replicates are used. This is the most thorough evaluation of learned IV methods among existing work.

4. **Competitive ATE estimation in the hardest settings.** In "No Candidate" settings (no explicit instrument exists), ZNet achieves the lowest ATE error in 4 of 8 estimator-dataset combinations and is second-best in another 3, demonstrating that the method can construct useful proxy instruments when none are pre-specified.

## Weaknesses

### Major

1. **Lemma 1 proof is mathematically incorrect, undermining the claim of relaxing the U→X assumption.** The proof of Lemma 1 (page 3) contains a basic error. The step  
   \(\mathbb{E}[Z \cdot (e_Y - \mathbb{E}[e_Y|X, T])] = \mathbb{E}[Z \cdot e_Y] - \mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X, T]\)  
   incorrectly replaces \(\mathbb{E}[Z \cdot \mathbb{E}[e_Y|X, T]]\) with \(\mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X, T]\). Since \(\mathbb{E}[e_Y|X, T]\) is a random variable (a function of \(X, T\)) and \(Z = g(X)\) is also a function of \(X\), the product \(\mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X, T]\) does not equal \(\mathbb{E}[Z \cdot \mathbb{E}[e_Y|X, T]]\) in general; the former is identically zero (since \(\mathbb{E}[Z]=0\)) while the latter need not be. The lemma's conclusion may still hold under additional conditions, but the provided proof does not establish it.  

   This error is consequential because Lemma 1 is the theoretical basis for Constraint 1 (unconfoundedness) and for the paper's central and repeatedly stated claim that ZNet *relaxes the standard assumption that unobserved confounders do not influence the observed data* (stated in Sections 3, 7, and the abstract). Without a correct lemma, this claimed advantage over prior variational methods (AutoIV, VIV, DVAE.CIV) is unsupported. The method remains a reasonable heuristic approach under the standard assumption (shared with prior work), but the paper oversells its theoretical contribution.

2. **Missing variance estimates in the main ATE results.** Table 1 reports ATE errors across 50 bootstrap resamples but shows only mean errors without standard deviations or confidence intervals. This omission is significant for a paper that makes comparative superiority claims: the reader cannot assess whether ZNet's performance is stable or erratic, nor whether observed differences between methods are meaningful relative to sampling variability. The non-standard significance notation (**, *) is not a substitute for proper variance reporting. Standard deviations must be reported or at minimum stated in the table.

### Minor

3. **Overstated performance claims.** The paper describes ZNet as achieving "superior performance" (Section 7) and "on average the highest performing among IV generation methods" (Section 6.3). Table 1 tells a more nuanced story: ZNet is bolded (best) in roughly 11 of 30 estimator-dataset combinations, often trading wins with AutoIV, VIV, or TrueIV. Missing standard deviations make it impossible to determine how often ZNet is actually significantly better rather than trivially different. The claims should be calibrated to "competitive" or "frequently among the best."

4. **Conflation of moment constraints with causal identification.** The paper states (Section 7) that "solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument since IV constraints are explicitly embedded in the loss function." This is a tautology that redefines "instrument" to mean "satisfies specified covariance constraints." In causal inference, instrument validity requires structural conditions (exclusion restriction and unconfoundedness in the data-generating process), not just finite-sample moment conditions. A learned representation may satisfy \(\text{Cov}(Z, C) \approx 0\) and \(\text{Cov}(Z, Y-\hat{Y}) \approx 0\) while still being correlated with \(U\) nonlinearly or violating exclusion through a confounded pathway. The paper does not characterize the gap between its covariance conditions and true causal identification, nor the bias when those conditions are insufficient.

5. **Tuning pipeline asymmetry.** Hyperparameters for ZNet and all baselines are tuned via Bayesian optimization on criteria (F-statistic for relevance, C-Z correlation) that directly align with ZNet's loss function. Downstream estimators are tuned to minimize ATE error against a nearest-neighbor ATE estimator, which itself is biased under unobserved confounding. This complex multi-stage pipeline makes it difficult to separate method performance from tuning artifacts. While all methods were tuned using the same procedure, ZNet's inductive bias aligns more closely with the tuning criteria.

### Trivial

- The "Proof." label on page 3 suggests the lemma has been proven, when the derivation is actually invalid.
- KL divergence to enforce \(Z \sim \mathcal{N}(0, \sigma^2)\) is mentioned but the specific form of the KL loss is not given.

## Nice-to-Haves

- Report standard deviations or 95% confidence intervals alongside the mean ATE errors in Table 1.
- Provide a corrected version of Lemma 1 or, if it cannot be fixed, explicitly remove the claim of relaxing the U→X assumption and position ZNet as operating under the standard assumption shared with prior work.
- Include an analysis of failure modes: the "No Candidate" setting with TSLS produces wildly inflated errors for ZNet in some configurations (e.g., 2.718 in linear, -25.181 in nonlinear for AutoIV), and understanding why would sharpen the paper's practical guidance.
- Move CATE results currently in the appendix into the main paper, since CATE estimation is listed as a contribution.

## Removed Points

- **Criticism that the method is purely heuristic without any theoretical justification** — Removed because this overstates the case. The exclusion restriction and relevance constraints are well-motivated by standard IV conditions even if the unconfoundedness lemma is flawed. The paper has partial theoretical grounding.
- **Criticism about missing related work** — Removed per instruction: I cannot verify existence of unmentioned related work.
- **Claim that ZNet's loss does not guarantee the right kind of correlation for \(C \rightarrow Y\)** — Removed because the paper is clear that \(C\) should capture *observed* variation in \(Y\), which is a reasonable approximation; claiming it must guarantee structural correctness is too strict for a learned representation approach.
- **Formatting nitpicks** — Removed per instruction.
- **Strength about "relaxing the U→X assumption"** — Removed because it depends on the flawed Lemma 1.
- **Strength about "theoretical grounding for the unconfoundedness loss"** — Removed because the lemma is flawed.
- **Strength about "staged training with gradient surgery"** — Removed as an implementation detail, not a research strength.

## Novel Insights

None beyond the paper's own contributions. The core observation is that moment constraints derived from IV assumptions (relevance, exclusion restriction, unconfoundedness) can be encoded as differentiable losses for learning instrument representations, and this can be effective empirically. The review process did not surface a deeper insight beyond what the paper presents.

## Suggestions

1. **Fix or remove Lemma 1.** Either provide a correct proof under properly stated assumptions, or remove the lemma and the claim that ZNet relaxes the U→X assumption. If the method is presented honestly as operating under the standard assumption (shared with AutoIV, VIV, etc.), the architecture and empirical evaluation still constitute a solid contribution.
2. **Report standard deviations in Table 1.** This is essential for a comparative evaluation with 50 bootstrap replicates.
3. **Calibrate the performance claims.** Replace "superior" with "competitive" and present ZNet's head-to-head record transparently.
4. **Add a formal discussion of identification.** Clarify what the moment constraints do and do not guarantee about the validity of the learned instrument for causal inference.
5. **Discuss the failure cases.** The catastrophic performance of ZNet's representations with TSLS in some No Candidate settings (e.g., ATE error 2.718 in Linear No Candidate) is informative and should be analyzed rather than omitted from discussion.

## Score and Decision

**Round-1 bracket:** 3.5–6.5. The paper exceeds low-band anchors (3.0–3.4) by having a clear architecture and much stronger evaluation, but falls short of mid/high-band anchors (5.5+) due to the flawed Lemma 1 and unsupported theoretical claim. The weakness-anchored query (theoretical error in proofs) returns a paper scored 4.20 with a closely matching failure profile.

**Round-2 narrowing:** Queries within (4.0, 5.5) and (5.5, 7.0) confirm that the closest score-anchors with matched failure modes sit in the 4.20–5.00 range (rejected papers). Papers at 5.5+ generally have sounder theory or stronger novelty justification.

**Final score rationale:** The paper has clear empirical strengths and a well-engineered architecture, but is held back by a genuine mathematical error in Lemma 1 that invalidates its signature theoretical claim. The missing variance estimates and overstated performance claims further weaken the case. At 4.5, the paper is above a pure reject (it has substantial merit and useful empirical contributions) but below the threshold for acceptance in its current form.

MY FINAL SCORE: 4.5
MY FINAL DECISION: Reject