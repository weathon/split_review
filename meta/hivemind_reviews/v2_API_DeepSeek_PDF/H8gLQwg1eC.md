## Summary
# Final Review Report

## Summary

This paper provides a theoretical analysis of generalization guarantees for preference optimization (DPO, IPO, SLiC) under noisy human feedback, within the generalized preference optimization (GPO) framework. Unlike classical convergence-based generalization bounds, the authors analyze finite-step optimization—a setting more aligned with practical LLM fine-tuning. Key results include: (1) generalization bounds showing population risk grows as $1/(1-c\epsilon)^2$ for noise rate $\epsilon$ below $1/2$, transitioning to linear decay near $\epsilon=1/2$; (2) a theoretical model where risk degradation slows with stronger class separation (angle $\theta$) and concentration ($\gamma$); (3) empirical validation on synthetic vMF data and HH-RLHF with Llama-2-7B. The paper makes a meaningful step toward bridging theory and practice in noisy preference learning. However, several technical concerns limit the current contribution: a mathematical inconsistency in the $R_0$ formula between the main theorem and appendix, strong assumptions (fixed encoder, vMF-distributed embeddings, symmetric noise) that are not fully bridged to practice, and a gap between the proven bounds and the empirically-fitted functional form.

## Strengths
1. **Novel theoretical framing.** The paper provides what is, to the best of our knowledge, the first generalization analysis for preference optimization under noisy feedback in a finite-step training regime. Departing from the convergence-based framework of classical learning theory is a practical and timely contribution.

2. **Unified GPO analysis.** The analysis covers the entire GPO family (DPO, IPO, SLiC) under a single framework, showing that the functional form of the risk bound is loss-agnostic. This generality increases the paper's impact.

3. **Theory-practice bridge.** The use of vMF-distributed embeddings to model post-RMSNorm LLM representations is empirically grounded (Appendix C shows high cosine concentrations). The theoretical predictions (risk grows as $1/(1-c\epsilon)^2$ with linear transition at $\epsilon=0.5$) are qualitatively validated on both synthetic and real-world data.

4. **Clear and well-structured exposition.** The paper is generally well written, with clear definitions, a logical flow from preliminaries to theory to experiments, and helpful "Key takeaways" summaries at the end of Section 3.

5. **Honest limitation statement.** The paper acknowledges the offline-only setting as a limitation, which demonstrates scientific transparency.

## Weaknesses
1. **Critical mathematical inconsistency in $R_0$ (Annotation 9).** Theorem 3.1 (Eq. 15) defines the clean risk bound as $R_0 = \frac{4}{\gamma}(1 - \frac{1}{\gamma} - \frac{\cos\theta}{3})^2$, while Lemma B.4 (Eq. 49) and Theorem B.1 (Eq. 64) both use $R_0 = \frac{8}{\gamma}(1 - \frac{1}{\gamma} - \frac{\cos\theta}{3})^2$. This factor-of-2 discrepancy propagates into the main bound and must be resolved.

2. **Fixed-encoder vs. full fine-tuning gap (Annotation 8).** The main theoretical results (Theorems 3.1, 3.2) are proven for a fixed encoder (last-layer fine-tuning only). The paper claims the theory holds "when performing full fine-tuning" based on empirical observations, but no theoretical extension is provided. The empirical agreement may not imply theoretical validity for the full fine-tuning case.

3. **Empirical validation validates functional form, not specific bound coefficients (Annotations 11, 13).** The controlled experiments fit a free parameter $c$ in the model $E_D[R(P)]/(1-c\epsilon)^2$. Since $c$ subsumes all distributional properties ($\gamma$, $\theta$, $N$), the experiments validate the functional form rather than the specific coefficient predictions of Theorem 3.1. The bound coefficients are never quantitatively instantiated.

4. **Strong assumptions limit practical applicability.** The analysis assumes (a) symmetric label-flipping noise (not realistic for human annotation), (b) vMF-distributed embeddings with known $\mu_+, \mu_-, \kappa$, (c) a fixed encoder, and (d) known separation angle $\theta$ and concentration $\gamma$. These parameters are never estimated from real data in the empirical validation.

5. **Related Work lacks structural organization (Annotation 15).** The "Alignment of LLMs" paragraph is a dense 35-citation list without grouping by approach family or stating differences from the current work. This weakens the novelty positioning.

6. **Limitations section is incomplete (Annotation 12).** Only the offline setting is mentioned as a limitation. The fixed-encoder assumption, symmetric noise model, lack of statistical significance reporting, and uncharacterized bound tightness are not discussed.

7. **Real-world experiment conflates two noise sources (Annotation 10).** HH-RLHF has ~30% pre-existing annotator noise (Wang et al., 2024), and the experiment adds synthetic label-flipping on top. The theoretical model assumes clean oracle data with symmetric label flipping, so the pre-existing noise creates a confound that is addressed only via a footnote calculation.

## Key Issues
### Issue 1 (Critical): $R_0$ Formula Inconsistency [Annotation 9]
- **Location:** Page 6 - Theorem 3.1 Eq. (15) vs Page 21 - Lemma B.4 Eq. (49)  
- **Root cause:** Theorem 3.1 uses $R_0 = \frac{4}{\gamma}(1 - \frac{1}{\gamma} - \frac{\cos\theta}{3})^2$, while both Lemma B.4 and Theorem B.1 use $\frac{8}{\gamma}$ instead of $\frac{4}{\gamma}$.  
- **Risk:** The factor-of-2 propagates into the main bound (Eq. 14) through both the numerator and the $\sqrt{R_0\gamma}$ denominator term, changing the bound's quantitative predictions.  
- **Fix:** Authors must re-derive the variance bound in Lemma B.1, determine the correct factor, and ensure all instances of $R_0$ are consistent throughout the paper and appendix.  
- **Severity:** Critical — directly affects mathematical correctness of the main theorem.

### Issue 2 (Major): Fixed-Encoder Theory vs. Full Fine-Tuning Claims [Annotation 8]
- **Location:** Page 4 - "Analyze GPO behavior under practical considerations" paragraph  
- **Root cause:** Theorem 3.1/3.2 are proven only for a fixed encoder, but Section 4 claims the theory "holds on real-world dataset with full fine-tuning" without a theoretical extension.  
- **Risk:** Readers may overestimate the rigor of the full fine-tuning claims.  
- **Fix:** Add explicit scope statement: Theorems hold for fixed encoder; full fine-tuning experiments show empirical consistency but lack formal proof.

### Issue 3 (Major): Empirical Validation Validates Functional Form, Not Bound Coefficients [Annotations 11, 13]
- **Location:** Page 5 - vMF assumption paragraph; Page 7 - Controlled experiment setup  
- **Root cause:** The model $E_D[R(P)]/(1-c\epsilon)^2$ has a free parameter $c$ fitted from data. The fit validates the functional family, not the specific theoretical coefficients.  
- **Risk:** The paper's claim of "close match between theoretical analysis and empirical observation" overstates what is demonstrated.  
- **Fix:** Clarify that $c$ is empirically fitted; report fitted $c$ values and compare with theoretical prediction $c = \sqrt{R_0\gamma}$ if possible.

### Issue 4 (Major): Incomplete Limitations [Annotation 12]
- **Location:** Page 10 - Limitation paragraph  
- **Root cause:** Only the offline setting is listed as a limitation. Missing: fixed-encoder assumption, symmetric noise model, no variance/statistical significance in experiments, bound tightness uncharacterized.  
- **Risk:** Reduces scientific transparency and may erode reviewer trust.  
- **Fix:** Expand limitations to cover all key assumptions and unaddressed gaps.

### Issue 5 (Major): Related Work is a Dense Citation List [Annotation 15]
- **Location:** Page 10 - "Alignment of LLMs" paragraph  
- **Root cause:** ~35 references in a single paragraph without thematic grouping or explicit comparison to the current work.  
- **Risk:** Weakens the paper's novelty positioning; reviewers may question whether the analysis is truly the first in this direction.  
- **Fix:** Restructure into 2-3 sub-paragraphs: theoretical works on preference optimization, empirical noise studies, robust DPO methods.

## Actionable Suggestions
### P0 — Must fix before publication

**S1. Resolve the $R_0$ inconsistency [Issue 1].** Re-derive the variance upper bound in Lemma B.1 (Eq. 36) to verify whether the factor is $4/\gamma$ or $8/\gamma$. If the true variance bound is $4/\gamma$, then Lemma B.4 and Theorem B.1 must be corrected to match Theorem 3.1. If $8/\gamma$ is correct (as the appendix suggests), Theorem 3.1 Eq. (15) must be corrected. Then verify that all downstream equations (Eqs. 14, 16) and the bound derivations in Theorem B.1 use the corrected $R_0$ consistently.

**S2. Scope the fixed-encoder vs. full fine-tuning claim [Issue 2].** Add an explicit sentence after Theorem 3.2: "We note that Theorems 3.1 and 3.2 are proven under the fixed-encoder setting with vMF-distributed embeddings. The experiments in Section 4 extend to full fine-tuning on Llama-2-7B; the observed qualitative agreement suggests the theoretical insights may generalize, but a formal proof for the full fine-tuning case is left for future work."

**S3. Clarify the empirical validation scope [Issue 3].** In Section 4.1, after reporting the theoretical fit, add: "The parameter $c$ in Eq. (18) is fitted from the data and subsumes the distributional properties ($\gamma$, $\theta$) and training configuration. This validates the $1/(1-c\epsilon)^2$ functional form predicted by the theory; the specific coefficient predictions of Theorem 3.1 would require computing $c = \sqrt{R_0\gamma}$ from estimated $\gamma$ and $\theta$."

### P1 — Strongly recommended

**S4. Expand limitations [Issue 4].** Replace the current one-sentence limitation with: "Several limitations should be noted. First, our analysis assumes a fixed encoder and vMF-distributed embeddings; extending the bounds to full fine-tuning is open. Second, we model noise as symmetric label flipping, but real human annotation noise is asymmetric. Third, the bounds are upper bounds whose tightness is not characterized. Finally, experiments report mean accuracy without variance or significance tests."

**S5. Restructure Related Work [Issue 5].** Split the "Alignment of LLMs" paragraph into three sub-topics: (a) theoretical analyses of preference optimization (Azar et al., Im & Li, Tang et al., Rafailov et al.) — explain why their clean-label analyses do not cover noise; (b) empirical noise studies (Gao et al., Fisch et al.) — summarize key empirical findings; (c) robust DPO methods (rDPO, cDPO, ROPO) — explain how they modify the objective and how the current analysis complements them.

**S6. Report goodness-of-fit metrics.** Add $R^2$ or RMSE values for each fitted curve in Figures 1 and 3. Example sentence: "Across all configurations, the fitted model achieves an average $R^2$ of 0.97 (min 0.94), confirming the close match."

### P2 — Quality improvements

**S7. Restructure the abstract [Annotation 1].** The abstract should follow a tighter 4-5 sentence logic. See Mentor Revised Version in Annotation 1 for a concrete proposal.

**S8. Add variance/error bars to real-world experiment [Annotation 10].** Report test accuracy across multiple training seeds (at least 3) with standard deviation in Figure 2.

**S9. Add a quantitative theory-practice comparison.** Estimate $\gamma$ and $\theta$ from real LLM embeddings on HH-RLHF and compute the predicted $R_0$. Compare this predicted bound with the observed test accuracy to provide a direct test of the bound coefficients (not just the functional form).

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: (P1) LLM alignment context + method list -> (P2) noise-free assumption is unrealistic + empirical study by Gao et al. -> (P3) we provide first finite-step generalization guarantees -> (P4) technical preview + contributions.

**Problem:** P1 and P2 are reasonably structured, but the transition from "noise matters" to "our theory" (P2->P3) lacks a concrete explanation of why existing theory (Im & Li 2024a) does not cover noise, and why finite-step analysis is needed. The contribution preview in P4 uses $\gamma$ before it is defined.

### Proposed Storyline (Recommended)

**Paragraph 1 - Big Picture & Problem:** Open with the practical gap between noise-free assumptions in preference optimization and the noisy reality of human annotation. Define noise concretely (label-flipping rate $\epsilon$). Mention empirical evidence that noise degrades alignment (Gao et al.).

**Paragraph 2 - Prior Work Gap:** Explain that existing theoretical analyses (Im & Li, Azar et al.) either assume clean labels or analyze convergence, not finite-step generalization under noise. Contrast with robust methods (rDPO, cDPO) that modify the objective but do not analyze the generalization behavior of the unmodified GPO family.

**Paragraph 3 - Our Approach:** Introduce the finite-step analysis as the key methodological departure. State the main result compactly: risk grows as $1/(1-c\epsilon)^2$ for $\epsilon<1/2$, with slower degradation for more separable data.

**Paragraph 4 - Contributions:** List contributions with explicit scoping qualifiers.

### Abstract Outline (Complete)

**S1 (Problem):** "Preference optimization aligns LLMs with human preferences, but human feedback is inherently noisy."

**S2 (Challenge):** "Existing theoretical analyses assume noise-free labels, leaving the generalization behavior under noisy feedback uncharacterized."

**S3 (Prior gap):** "We provide the first finite-step generalization guarantees for the GPO family (DPO, IPO, SLiC) under symmetric label-flipping noise."

**S4 (Method + Key Result):** "Our bounds show that population risk grows as $1/(1-c\epsilon)^2$ for noise rate $\epsilon<1/2$, transitioning to linear decay near $\epsilon=1/2$, with stronger class separation and concentration slowing degradation."

**S5 (Evidence):** "Experiments on synthetic vMF data and HH-RLHF with Llama-2-7B confirm the predicted functional form."

### Introduction Outline (Complete)

**P1 (Role: Motivation and Problem):** State the practical importance of preference optimization for LLM alignment. Acknowledge that human feedback is noisy. State the core question: how does label noise affect generalization? (Backed by Gao et al. empirical findings.)

**P2 (Role: Prior Work Gap):** Explain why existing analyses (convergence-based, clean-label) do not answer this question. Cite Im & Li (2024a) as the closest theoretical work and explain the clean-label limitation. Briefly note robust DPO variants (rDPO, cDPO) as complementary but different.

**P3 (Role: Our Solution):** Present the finite-step analysis approach. State that the paper provides generalization bounds for the entire GPO family under noisy feedback. Preview the key functional form $1/(1-c\epsilon)^2$ without using undefined notation.

**P4 (Role: Contributions):** List three contributions with scope qualifiers: (1) first generalization guarantees for noisy GPO (fixed-encoder setting), (2) comprehensive analysis of noise rate impact in finite-step setting, (3) empirical validation on synthetic and real data.

## Priority Revision Plan
| Priority | Action | Effort | Expected Impact | Annotation Ref |
|----------|--------|--------|----------------|----------------|
| P0 | Resolve $R_0$ inconsistency: re-derive variance bound, correct Eq. (15) or Eq. (49) | 1-2 days | Eliminates mathematical error in main theorem | #9 |
| P0 | Scope fixed-encoder vs. full fine-tuning claims in Theorem statements | <1 day | Prevents overclaiming; improves scientific precision | #8 |
| P0 | Clarify that empirical validation fits free parameter $c$, not bound coefficients | <1 day | Aligns claims with evidence; reduces overclaim risk | #11, #13 |
| P1 | Expand limitations section to cover all key assumptions | <1 day | Improves transparency and reviewer trust | #12 |
| P1 | Restructure Related Work into thematic sub-paragraphs | 1-2 days | Strengthens novelty positioning | #15 |
| P1 | Report goodness-of-fit metrics ($R^2$) for Figures 1 and 3 | <1 day | Quantifies the "close match" claim | #14 |
| P2 | Add variance/error bars to HH-RLHF experiment (multi-seed) | 1-2 days | Improves statistical reliability of experimental claims | #10 |
| P2 | Estimate $\gamma$ and $\theta$ from real LLM embeddings and compute predicted $R_0$ | 2-3 days | Directly tests bound coefficients, not just functional form | #11 |
| P2 | Restructure abstract to 4-5 sentence compact format | <1 day | Improves first-impression clarity | #1 |

### Revision Dependencies
- P0 items must be completed before resubmission.
- P1 items should be completed for a strong revision.
- P2 items are quality improvements that would strengthen the paper but are not blocking.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Test effect of noise rate $\epsilon$ and concentration $\gamma$ on test accuracy | Synthetic vMF data, d=512, DPO loss, 10 epochs, 20 trials | Test accuracy | Accuracy decreases with $\epsilon$; slower degradation for larger $\gamma$ | Functional form $1/(1-c\epsilon)^2$ validated | $c$ is fitted, not computed from theory; no $R^2$ reported |
| E2 | Test effect of class separation $\theta$ on noise sensitivity | Same as E1, varying $\theta$ | Test accuracy | Larger $\theta$ (more separable) yields slower accuracy degradation | Distributional parameters affect noise sensitivity as predicted | Same as E1 |
| E3 | Real-world validation with full fine-tuning | HH-RLHF, Llama-2-7B, DPO loss, 1 epoch, $\epsilon$ in [0,0.5] | Test accuracy | Near-linear decline; theory-based model closely fits | Functional form holds under full fine-tuning | 30% pre-existing noise confounds the clean-oracle assumption |
| E4 | Extension to IPO loss | Same setup as E1 with IPO loss | Test accuracy | Same functional pattern as DPO | GPO family shows loss-agnostic behavior | Same limitations as E1 |

### Research-Theme Gap Diagnosis

1. **Bound coefficient verification gap.** The theory predicts specific values for $R_0$ and the rate constant $c = \sqrt{R_0\gamma}$, but the experiments only fit $c$ as a free parameter. The quantitative predictions of Theorem 3.1 are never tested against real data.

2. **Full fine-tuning theory gap.** The core theoretical results are for a fixed encoder. The empirical extension to full fine-tuning lacks theoretical backing.

3. **Asymmetric noise gap.** All experiments use symmetric label-flipping noise. Real human annotation noise is likely asymmetric, and the theory's applicability to that setting is untested.

4. **Statistical reliability gap.** Experiments report mean accuracy over 20 trials (controlled) or a single run (real-world) without variance or significance tests.

### Proposed Research Experiments (P0/P1/P2)

**P1 — Experiment R1: Bound Coefficient Verification**
- **Target Claim:** $R_0$ bound from Theorem 3.1
- **Hypothesis:** Estimating $\gamma$ and $\theta$ from vMF-sampled data and computing $R_0$ yields a valid upper bound on the observed test error.
- **Minimal Design:** Use the synthetic setup from E1. For each ($\gamma$, $\theta$) configuration, compute the empirical sample estimates $\hat{\gamma}$, $\hat{\theta}$. Compute the predicted $R_0$ from Eq. (15). Compare with observed test error for $\epsilon=0$.
- **Controls/Baselines:** Use the theoretical bound value; check if the observed risk is below $R_0$ as guaranteed.
- **Metrics:** Fraction of configurations where $R_{\text{observed}} \leq R_0(\text{predicted})$.
- **Success Criterion:** At least 95% of configurations satisfy the bound.
- **Estimated Cost/Time:** 2-3 days (reuses existing code).
- **Expected Quality Gain:** Directly validates bound coefficients, not just functional form.

**P2 — Experiment R2: Asymmetric Noise Probe**
- **Target Claim:** The $1/(1-c\epsilon)^2$ functional form holds under asymmetric noise.
- **Hypothesis:** If label-flipping probability differs for positive→negative vs. negative→positive, the risk growth rate changes.
- **Minimal Design:** Modify the synthetic setup to use $\epsilon_+$ and $\epsilon_-$ with $\epsilon_+ \neq \epsilon_-$. Fit the same functional form and measure goodness-of-fit.
- **Metrics:** $R^2$ of the fitted model under asymmetric noise.
- **Success Criterion:** $R^2 \geq 0.9$ for moderate asymmetry ($|\epsilon_+ - \epsilon_-| \leq 0.2$).
- **Estimated Cost/Time:** 1-2 days.
- **Expected Quality Gain:** Tests robustness of the theory to a more realistic noise model.

**P2 — Experiment R3: Multi-Seed Variance for HH-RLHF**
- **Target Claim:** The test accuracy trend in Figure 2 is statistically reliable.
- **Hypothesis:** Results are consistent across seeds.
- **Minimal Design:** Repeat the HH-RLHF experiment (Section 4.2) with 3-5 random seeds for each noise level. Report mean $\pm$ std.
- **Metrics:** Standard deviation of test accuracy across seeds.
- **Success Criterion:** Standard deviation $\leq 0.01$ at each noise level.
- **Estimated Cost/Time:** 3-5 days (full fine-tuning of Llama-2-7B is compute-intensive).
- **Expected Quality Gain:** Enables statistical claims about the experimental results.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

The paper tackles an important and timely problem (generalization of preference optimization under noisy feedback) with a novel finite-step theoretical framework. The GPO-level analysis and the functional form $1/(1-c\epsilon)^2$ are valuable contributions. However, the score is constrained by:

- **Research Value (7/10):** The problem is important and the finite-step framing is practical. However, the strong assumptions (fixed encoder, vMF, symmetric noise) limit the direct applicability of the results.
- **Novelty (6/10):** The finite-step generalization analysis for noisy GPO is new. But the mathematical inconsistency in $R_0$ weakens confidence, and the empirical validation validates the functional form rather than specific bound coefficients. Deferred external verification needed for "first" claims.
- **Validity (6/10):** The $R_0$ inconsistency (4/$\gamma$ vs. 8/$\gamma$) is a correctness issue that must be resolved. The empirical fits use a free parameter, making the "close match" claim weaker than stated.
- **Reproducibility (7/10):** Experimental details are well documented (hyperparameters in Appendix A). Code availability is not stated.

**Post-Revision Target: [7.5, 8.0] / 10**

If the $R_0$ inconsistency is resolved (P0), the scope claims are properly bounded (P0), limitations are expanded (P1), and additional experiments validating the bound coefficients are added (P2), the paper could reach the 7.5-8.0 range, reflecting a solid theoretical contribution with well-scoped claims.