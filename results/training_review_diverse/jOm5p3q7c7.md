I now have a complete understanding of the paper and all reviewer claims. Let me write the final consolidated review.

---

## Summary

This paper resolves an open question in RL theory by providing the first optimal sample complexity bound $\widetilde\Theta(|S||A|\tmix\epsilon^{-2})$ for learning an $\epsilon$-optimal policy in uniformly ergodic average-reward MDPs (AMDPs) under a generative model, matching the lower bound of Jin & Sidford (2021). The approach combines two ideas: (1) an improved analysis of the perturbed model-based planning algorithm (Li et al., 2020) that achieves optimal $\widetilde\Theta(|S||A|\tminor(1-\gamma)^{-2}\epsilon^{-2})$ sample complexity for uniformly ergodic discounted MDPs (DMDPs) — contributing Theorem 3.1 — and (2) a reduction from AMDP to DMDP (Jin & Sidford, 2021) that translates this DMDP result into the optimal AMDP guarantee via suitable parameter choices.

---

## Strengths

- **First optimal sample complexity for uniformly ergodic AMDPs.** The paper achieves $\widetilde\Theta(|S||A|\tmix\epsilon^{-2})$, matching the lower bound. This is a genuine advance over prior work that had a $\tmix$ gap (upper bound $\widetilde O(|S||A|\tmix^2\epsilon^{-2})$) or an $\epsilon^{-3}$ dependence, as clearly shown in Table 1.

- **Improved DMDP analysis of independent interest.** Theorem 3.1 provides an error bound for perturbed model-based planning (Li et al., 2020) that replaces the worst-case $(1-\gamma)^{-3}$ dependence with an optimal $\tminor(1-\gamma)^{-2}$ dependence for uniformly ergodic DMDPs, while maintaining a low minimum sample size $\widetilde\Omega(|S||A|(1-\gamma)^{-1})$. This improves over Wang et al. (2023), which required $\widetilde\Omega(|S||A|(1-\gamma)^{-3})$ minimum samples — a critical difference for the AMDP reduction.

- **Clear exposition of the gap and motivation.** The paper effectively explains (Section 1.2, Table 2) why prior reduction-based methods obtained suboptimal $\epsilon^{-3}$ dependence — they used worst-case DMDP results that ignore mixing — and why the low minimum sample size of Li et al. (2020) is essential for the AMDP application.

- **Numerical validation.** Experiments on the hard instance from Wang et al. (2023) separately verify the $\epsilon^{-2}$ rate (slope $-0.5$, Figure 1a) and the linear $\tminor$ dependence (slope near $0$, Figure 1b), providing supporting evidence for the theoretical claims.

---

## Weaknesses

### Fatal
None.

### Major

None.

### Minor

1. **The reduction lemma connecting DMDP error to AMDP error is not stated.** The paper cites Jin & Sidford (2021) for the reduction procedure, but the key error bound — which translates the DMDP value-function error $(v^*_\gamma - v^{\hat\pi_0}_\gamma)$ into the AMDP average-reward error $(\bar\alpha - \alpha^{\hat\pi_0})$ with the specific $(1-\gamma)$ scaling — is never written out. The parameter settings in Algorithm 4.1 ($\gamma = 1-\epsilon/(19\tminor)$, $\zeta = \frac14(1-\gamma)\tminor$, and especially the constant 19) appear without derivation. An explicit statement of the reduction lemma (even as a proposition citing Jin & Sidford 2021) showing how the constants arise would significantly improve verifiability and self-containedness. This is the single most important presentation gap.

2. **Confusing reuse of $\epsilon$ across Theorem 3.1 and Algorithm 4.1.** In Theorem 3.1, $\epsilon$ is the DMDP target error, and $\zeta$ is set to $(1-\gamma)\epsilon/4$. In Algorithm 4.1, $\epsilon$ is the AMDP target error, and $\zeta$ is set to $(1/4)(1-\gamma)\tminor$ — which *implicitly* corresponds to a DMDP target error of $\tminor$. The paper does not explain this correspondence, making it seem like the $\zeta$ formula changes arbitrarily. A brief remark that in Algorithm 4.1 the DMDP error tolerance is effectively $\tminor$ (since $\zeta = \frac14(1-\gamma)\tminor$ and the reduction scales this by $(1-\gamma)$) would resolve the confusion.

3. **The condition $\epsilon \leq \sqrt{\tminor/(1-\gamma)}$ in Theorem 3.1 is stated without intuition or justification.** While such technical conditions are common, a brief explanation of why it arises (e.g., to ensure the two terms in the error bound are balanced) would help readers.

### Trivial

- The function $\beta_\delta(\eta)$ has $\eta$ as a dummy parameter, and $\eta_\delta^*$ is a specific value inserted into it. This is standard notation but could be briefly remarked for clarity.
- The paper alternates between $\tminor$ and $\tmix$ but does explicitly state their equivalence up to constants (line 169) and notes that bounds expressed in $\tminor$ can be re-expressed in $\tmix$. This is adequate.

---

## Nice-to-Haves

- Stating the reduction lemma (from Jin & Sidford 2021) as a self-contained proposition, even in a short form, with the specific constants.
- Briefly tracing the origin of the constant 19 (e.g., "19 = 2 + 2×8 + something" if it comes from combining constants in the reduction bound and Theorem 3.1).
- Including an ablation varying both $\epsilon$ and $\tminor$ simultaneously (though this is not necessary for a theory paper).

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Fatal internal inconsistency between Theorem 1 and Algorithm 2":** The reviewer computes the DMDP error bound with Algorithm 4.1's parameters, obtains DMDP error ≤ $\tminor$, and concludes this is fatal because "the total error is therefore at least $\tminor$, a fixed constant." **This is factually wrong.** The DMDP error $(v^*_\gamma - v^{\hat\pi_0}_\gamma)$ is not the AMDP error $(\bar\alpha - \alpha^{\hat\pi_0})$. The reduction lemma (Jin & Sidford 2021) relates the two with a $(1-\gamma)$ scaling factor. With $1-\gamma = \epsilon/(19\tminor)$, the DMDP error of $\tminor$ translates to $(1-\gamma)\cdot\tminor = \epsilon/19$ in the AMDP, which is $O(\epsilon)$, not a constant. The reviewer's algebra for the DMDP bound is correct, but the conclusion ignores the reduction step. Removed per: *REMOVE criticisms that are factually wrong or misunderstand the paper.*

- **"The definition of $\eta_\delta^*$ involves a term $\eta$ that appears in the log factor $\beta_\delta(\eta)$ but is never defined":** $\eta$ is the argument of the function $\beta_\delta$, and $\eta_\delta^*$ is a specific value. This is standard mathematical notation. Removed as a non-issue.

- **"Numerical experiments on a single instance family cannot verify the scaling":** This confuses the role of experiments in a theory paper. The primary evidence is the proof; experiments are illustrative sanity checks. Removed as a genre-inappropriate expectation (benchmark paper standards applied to a theory paper).

- **"The constant 19 appears without derivation" and "The constant 486 is never derived":** These are presentation issues (which are kept in Minor #1 above in aggregate form), but the reviewer's framing as separate major flaws is disproportionate. Consolidated into the single clarity concern about the missing reduction lemma statement.

- **"The experiments are measuring an algorithm whose theoretical guarantee has not been established":** This follows from the "fatal inconsistency" claim which is factually wrong. Removed.

- **"The paper lacks a clear statement of how the DMDP error bound translates into the AMDP error bound":** Kept in spirit as Minor #1; the removed framing implied a fatal gap rather than a presentation issue.

- **"The mismatch between $\tmix$ and $\tminor$ in naming creates confusion":** The paper explicitly states the equivalence relationship (lines 167-171) and notes all bounds can be expressed in either. This is adequately clarified.

---

## Novel Insights

The harsh reviewer's algebra reveals an interesting pedagogical point: the paper's compact presentation style places a heavy burden on readers who are not intimately familiar with the Jin & Sidford (2021) reduction lemma. The DMDP error bound in Theorem 3.1, when evaluated at Algorithm 4.1's parameters, indeed yields a DMDP error of $\tminor$ — which looks alarmingly like a constant. What rescues the result is the $(1-\gamma)$ scaling in the reduction: the AMDP error is bounded by $C\cdot(1-\gamma)\cdot\text{(DMDP error)}$, and since $1-\gamma = \epsilon/(19\tminor)$, this becomes $C\epsilon/19$. The paper's reliance on an external lemma without restating it creates a verifiability gap that is real even though the underlying mathematics is sound. A 3-line lemma stating the reduction bound would eliminate the confusion entirely.

---

## Suggestions

1. **Add a short, self-contained reduction lemma** (or proposition, citing Jin & Sidford 2021) that explicitly states the error bound connecting the DMDP value-function error to the AMDP average-reward error for uniformly ergodic MDPs, including the $(1-\gamma)$ scaling factor. This would resolve the main clarity concern.
2. **Derive the parameter settings in Algorithm 4.1 from this lemma**, showing step-by-step how $\gamma = 1 - \epsilon/(19\tminor)$, $\zeta = \frac14(1-\gamma)\tminor$, and $n = 4\cdot486^2\beta/((1-\gamma)^2\tminor)$ are chosen to make the total AMDP error ≤ $\epsilon$.
3. **Add a remark** clarifying that the $\epsilon$ in Theorem 3.1 (DMDP error tolerance) and the $\epsilon$ in Algorithm 4.1 (AMDP error tolerance) are different quantities, and how one is set in terms of the other via the reduction.

---

## Score and Decision

The paper makes a genuine contribution: it is the first to achieve the optimal sample complexity for uniformly ergodic AMDPs, matching the lower bound. The improved DMDP analysis (Theorem 3.1) is technically sound and independently interesting. The main presentation issues — the missing explicit reduction lemma and the opaque constant choices — are real but addressable in a revision, and they do not undermine the core mathematical claims. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>