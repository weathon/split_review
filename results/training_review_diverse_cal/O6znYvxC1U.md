Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies Bayesian neural networks (BNNs) in asymptotic linear-width (P/N→α, P/N₀→α₀) and sublinear-width (P/(N·N₀)→γ) regimes. Its contributions are: (1) Theorem 3.4, integral formulas for BNN predictor mean and variance expressed in terms of the limiting spectral measure of the empirical kernel matrix and the spectral universality assumption (SUA); (2) Theorem 3.5, which argues that the renormalisation theory (previously known for linear BNNs) extends to nonlinear BNNs iff the SUA holds; and (3) a numerical estimation technique for the sublinear-width regime where renormalisation theory breaks down.

## Strengths

- **Novel bridge between kernel spectral theory and BNN predictor statistics.** Theorem 3.4 provides explicit integral expressions for the mean and variance of a trained BNN's predictor using only the limiting spectral measure and the SUA, offering a unified way to compute predictor statistics without posterior sampling (Theorem 3.4, equations 2–3). This connection between random matrix theory (Marchenko–Pastur maps) and BNN inference is genuinely new.

- **Connection between renormalisation theory and the SUA.** Theorem 3.5 reframes the correctness of the SUA in terms of whether the random feature map can realize arbitrary orthogonal decompositions of the kernel matrix. This gives a conceptual criterion for when renormalisation should hold in nonlinear networks, and it provides a mathematical explanation for empirical observations that renormalisation often works with ReLU activations (Theorem 3.5, Section 3.3).

- **Honest treatment of limitations.** The paper explicitly acknowledges that the sublinear-width regime lacks a proven nonrandom limiting spectral measure (Section 3.4: "precisely characterising the asymptotic behavior…is an interesting avenue for further research"), that the technique is a heuristic in this regime, and that the SUA may not be accurate in certain configurations (Section 4). This intellectual honesty is commendable.

- **Experimental consistency check in the linear-width regime.** Figure 1 shows that the integral estimates agree with the predictions of renormalisation theory for both linear and ReLU networks in the linear-width limit, confirming internal consistency of the theoretical framework.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 3.5's "if and only if" claim is not rigorously proven.** The necessity direction is merely asserted ("Conversely, if the SUA does not hold, the integral with respect to Φ does not span the space of orthogonal matrices…") without establishing the logical chain from "the SUA approximation is inaccurate" to "no weight configuration exists for each orthogonal Φ" to "the marginal likelihood deviates from the Gaussian form." The sufficiency direction's "free interchange" argument — constructing a new training dataset with the same covariance structure as K_NNGP — is sketchy and not developed into a rigorous proof. For a theoretical paper, a theorem labeled "if and only if" needs proper proof of both directions; the necessity half is essentially unsubstantiated. This weakens the paper's central claim about extending renormalisation theory.

- **The proof of Theorem 3.5 conflates the SUA as a numerical approximation with the covering property of the feature map.** The theorem's condition ("for any orthogonal Φ, there exists Θ such that φ(Θ,X)^T φ(Θ,X) = ΦΛΦ^T") is a property of the architecture and data, whereas the SUA is a distributional approximation for eigenfunctions. The paper asserts without rigorous justification that failure of the SUA (an approximation whose accuracy varies continuously) is equivalent to failure of this covering property (a binary condition). This conflation undermines the claimed "if and only if" characterization.

### Minor

- **The claimed spectral measure ρ_{MP}^α ⊠^L ρ_{NNGP}^{α₀} for multi-layer nonlinear networks is not adequately justified.** The paper states this follows "by immediate induction…as a direct corollary of Theorem 2 in El Harzli et al. (2024)" (Section 3.1). However, after the first hidden layer, the effective input to subsequent layers consists of pre-activations with a different distribution and covariance structure than the original data. The induction step — composing Marchenko–Pastur maps with the layer-wise NNGP covariance recursion — is not trivial and requires explicit justification. The paper does not explain how the linear-width scaling of hidden layers interacts with the infinite-width limits of other layers.

- **The sublinear-width "technique" lacks theoretical grounding that the paper partially acknowledges but still presents as a contribution.** The method of numerically computing the strictly positive support of the empirical kernel spectrum and using the integral formulas under the SUA is presented as a "novel technique" (abstract). Yet the paper concedes that whether the relevant random kernel matrix even has a nonrandom limiting spectral measure under this scaling is unresolved. The experiments compare against variational inference (itself an approximation), so the validation does not establish ground truth. The paper's honest framing mitigates this issue but does not change the fact that the sublinear-width contribution is a heuristic with unknown domain of validity.

- **The relationship between the SUA condition in Theorem 3.5 and the "covering property" is circular.** The paper defines the correctness of the SUA in terms of whether the feature map can realize all orthogonal matrices. But the SUA is itself an assumption about the distribution of eigenfunctions, not a property of the feature map's range. The paper does not provide independent conditions under which the covering property holds for nonlinear architectures (beyond the linear case, where it is "easy to show"), so Theorem 3.5's criterion is not operationalizable without essentially assuming the conclusion.

### Trivial
None.

## Nice-to-Haves

- A discussion of how the SUA, as used in this paper, relates to — and differs in verifiability from — the Gaussian equivalence assumption (GEA) from statistical mechanics would strengthen the positioning. The paper mentions the distinction (Section 3.2) but does not argue why the SUA is easier to verify for BNNs than the GEA.
- Error bars or confidence intervals on the variance estimates in Figure 2 would help assess finite-size effects that the paper acknowledges.
- A description of how the Marchenko–Pastur maps were numerically computed (fixed-point solver details) would aid reproducibility.

## Removed Points

These points were removed per the meta-reviewer guidelines; they are listed here for transparency:

1. **"The derivations of the main results are not carried out in the paper; Theorem 3.4 is stated without proof."** — Removed because proofs likely reside in the appendix, which the parser strips. The text at line 102 references "Theorem 3.4 and its proof," confirming a proof existed in the original submission.

2. **"The integral formulas (equations 2 and 3) contain notation that does not parse."** — Removed as a parser-induced formatting artifact (garbled matrix expressions). The original submission presumably has correct typesetting.

3. **"The paper uses the term 'modified NNGP kernel' without ever defining it explicitly."** — Removed because the paper does define it at line 75: "The modified NNGP kernel is the random kernel K_Θ^{α,α₀} (respectively, K_Θ^γ) defined over R^N in the linear-width regime (respectively, the sublinear-width regime)."

4. **"The paper should supply the missing proofs…"** — Removed per the guideline that missing appendix content is a parser artifact.

5. **"The SUA is not shown to be satisfied in the intended regimes."** — Removed as a scope-creep demand: Theorem 3.4 explicitly assumes the SUA holds; the paper's contribution is the *consequence* of that assumption, not a proof that the SUA holds. The necessity of the SUA is discussed in Theorem 3.5.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface genuinely novel observations that the paper itself does not already articulate (e.g., the connection between the SUA and the uniform distribution over orthogonal matrices in the infinite-dimensional limit is already in Section 3.2).

## Suggestions

1. **Restate Theorem 3.5 as a sufficient condition**, dropping the unproven necessity direction. Replace "if and only if" with "if" (or at most "if and only if" for a properly proven version). This would honestly reflect what the paper actually establishes.

2. **Rigorously justify the induction** claiming ρ_{MP}^α ⊠^L ρ_{NNGP}^{α₀} for multi-layer networks. Either show the induction step explicitly or cite a theorem in El Harzli et al. (2024) that directly handles the multi-layer case, noting any additional assumptions required.

3. **Reframe the sublinear-width contribution** as "initial empirical findings" or "a heuristic inspired by the theoretical linear-width results" rather than a "novel technique," which overclaims given the acknowledged lack of asymptotic theory.

4. **Clarify the logical relationship** between the SUA (a distributional approximation) and the covering property of the feature map (whether all orthogonal Φ are realizable). Theorem 3.5 would be stronger if it explicitly verified this covering property for a concrete nonlinear architecture (e.g., ReLU with Gaussian weights) rather than leaving it abstract.

5. **Add a small-scale experiment** where the exact BNN posterior can be computed (e.g., via Hamiltonian Monte Carlo or closed-form for tiny networks) to validate the integral formulas against a ground truth, rather than relying solely on variational inference comparisons.

## Score and Decision

The paper presents a novel perspective and interesting connections, but the core theoretical claim (Theorem 3.5's "if and only if") is not properly proven, and the sublinear-width contribution is overclaimed relative to its theoretical support. For a theoretical paper, incomplete proof of a central theorem is a significant weakness that prevents acceptance in the current form. A thorough revision that addresses the proof gaps, clarifies the logical relationships, and honestly scopes the sublinear-width contribution would be needed.

**Originality:** Good — the spectral bridge between BNNs and kernel theory is novel.

**Importance of question:** Moderate — the generalisation properties of BNNs are an active area.

**Claims supported:** Partially — Theorem 3.5's stronger claim is not supported; Theorem 3.4 is conditional on the SUA.

**Soundness:** Moderate — the proof sketch for Theorem 3.5 has significant gaps.

**Clarity:** Generally clear despite theoretical complexity, though the notation in equations 2–3 is compromised by parser artifacts.

**Value to community:** Potentially high if the proof gaps can be closed, as the integral formulas and spectral perspective could inform future BNN theory.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>