Now I have a thorough understanding of the paper and can verify each claim directly against the text.

---

## Summary

This paper provides the first finite-time global convergence analysis of policy gradient for infinite-horizon average-reward tabular MDPs, removing the smoothness assumption that prior work took as given. The key technical innovation is proving that the average reward is smooth (without assuming it) using a projection technique that resolves the non-uniqueness of the relative value function. The paper establishes sublinear convergence \(O(1/k)\) with regret \(O(\log T)\) in Theorem 1, identifies conditions for exponential convergence on "simple" MDPs, and extends the analysis to discounted MDPs with complexity-dependent bounds.

## Strengths

- **Elimination of the unverified smoothness assumption**: Prior work (Bai et al., 2023; Ganesh et al., 2024) assumed the average reward is smooth without verification. This paper proves smoothness via a projection technique (Lemma 1, the \(\Phi\) matrix) that handles the non-uniqueness of the value function, and then derives explicit smoothness constants in Lemmas 2–4. This is a genuine theoretical advance that validates the foundation on which downstream convergence results rest.

- **First finite-time global convergence bounds for average-reward policy gradient without smoothness assumptions**: Theorem 1 gives \(O(1/k)\) optimality-gap convergence with \(O(\log T)\) regret, improving over Bai et al. (2023)'s \(O(T^{1/4})\) regret bound which required the unverified smoothness assumption. The bound also identifies exponential convergence for MDPs where \(32|\mathcal{S}| L_2^\Pi C_{PL}^2 < 1\).

- **Explicit MDP-complexity constants in bounds**: Unlike discounted-reward bounds that depend only on \((1-\gamma)^{-5}\) and state/action cardinalities, the paper's constants \(C_m, C_p, C_r, \kappa_r\) capture the structure of the transition kernel and reward function. This makes the bounds predictive — MDPs with lower complexity converge faster — as illustrated in the simulations.

- **Extension to discounted MDPs with improved complexity dependence**: Section 3.2 shows how the analysis applies to discounted MDPs, yielding \(O(|\mathcal{S}| L_2^\Pi / \epsilon)\) iteration complexity, and demonstrates a concrete example (trivial MDP with \(C_p = 0\)) where the bound reduces to \(O(|\mathcal{S}| / \epsilon)\) versus the prior \(O(|\mathcal{S}||\mathcal{A}| / \epsilon)\).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The constants \(C_m, C_p, C_r, \kappa_r\) are not defined in the main text.** Lemmas 2–4 express the core smoothness and Lipschitz results in terms of these constants, stating only that they are "determined by the underlying MDP." The paper refers to Table 1 for definitions, but the table is an image that does not survive text parsing. Even in the original submission, the main text should provide at least a one-sentence description of what each constant represents (e.g., \(C_p\) is the maximum spectral norm of the Jacobian of \(\mathbb{P}^\pi\) w.r.t. \(\pi\); \(C_r\) scales with reward variance; \(C_m\) bounds the norm of \((I - \Phi \mathbb{P}^\pi)^{-1}\); \(\kappa_r\) relates to mixing). Without this, a reader of the main text cannot assess what the smoothness result actually depends on. The simulation section gives some intuition (lines 279–281) but not formal definitions.

- **Lemma 8 is stated without proof or derivation in the main text.** Lemma 8 claims \(\langle \partial\rho_{\pi_{k+1}}/\partial\pi_{k+1}, \pi' - \pi_{k+1} \rangle \leq 4\sqrt{|\mathcal{S}|} L_2^\Pi \|\pi_{k+1} - \pi_k\|\), a key ingredient for Theorem 1. No proof sketch is provided — the paper simply says "Lemmas 5,7 and 8 are combined to prove the result in Theorem 1." For a theory paper, a brief justification (even a one-sentence intuition) would help the reader assess plausibility. The proof is presumably in the appendix (which was stripped), but the main text should not rely entirely on deferred proofs for central lemmas.

- **Lemma 5's derivation from smoothness is not shown.** The lemma states \(\rho^{\pi_{k+1}} - \rho^{\pi_k} \geq (L_2^\Pi/2) \|\pi_{k+1} - \pi_k\|^2\). This follows from the standard smoothness inequality combined with the gradient ascent update and the step-size condition \(\eta < 1/L_2^\Pi\) (the standard bound gives \((1/\eta - L_2^\Pi/2)\|\cdot\|^2\), and since \(1/\eta > L_2^\Pi\), the coefficient exceeds \(L_2^\Pi/2\), making the paper's bound valid but looser). The paper should make this connection explicit.

- **The exponential convergence expression in Theorem 1 (second bullet) is unusually formatted.** The expression \(\rho^* - \rho^{\pi_k} \leq c^{-k/2} (\rho^* - \rho^{\pi_0})^{1/2^k}\) is mathematically correct — the \((\rho^* - \rho^{\pi_0})^{1/2^k}\) factor approaches 1, so the bound is dominated by \(c^{-k/2}\) giving exponential convergence. However, the form is non-standard and could confuse readers; a cleaner expression (e.g., \(\rho^* - \rho^{\pi_k} \leq (\rho^* - \rho^{\pi_0}) \cdot c^{-k/2}\)) would be preferable.

### Trivial

- The notation in Lemma 5 has a garbled reference ("equation $\theta,$" instead of "equation 6").

## Nice-to-Haves

- Add brief definitions of \(C_m, C_p, C_r, \kappa_r\) in the main text (not just in Table 1) so that the smoothness lemmas are self-contained.
- Provide a short proof sketch for Lemma 8 in the main text.
- Clarify the relationship between the step-size condition \(\eta < 1/L_2^\Pi\) and the bound in Lemma 5.
- Reformulate the exponential convergence expression in a more standard form.

## Removed Points

These points were flagged by the reviewers but are not valid weaknesses of the paper:

1. **"Lemma 5 is inconsistent with standard smoothness analysis"** (Harsh Critic Point 1). This is incorrect. For an \(L\)-smooth function under projected gradient ascent with \(\eta < 1/L\), the standard descent/ascent lemma gives \(f(x_{k+1}) - f(x_k) \geq (1/\eta - L/2)\|x_{k+1} - x_k\|^2\). Since \(\eta < 1/L_2^\Pi\) implies \(1/\eta - L_2^\Pi/2 > L_2^\Pi/2\), the bound \((L_2^\Pi/2)\|\cdot\|^2\) is a valid (weaker) lower bound. The lemma is correct.

2. **"Abstract and Theorem 1 give conflicting convergence rates"** (Harsh Critic Point 4). The abstract says \(O(1/T)\), Theorem 1 gives \(O(1/k)\), and the remark states regret \(O(\log T)\). These are consistent: \(O(1/k)\) optimality gap summed over \(k\) yields \(O(\log T)\) regret. There is no conflict.

3. **"Condition \(L_2^\Pi \ll 1\) is vague"** (part of Harsh Critic Point 4). The paper immediately states the precise mathematical condition: \(\frac{1}{c} = 32|\mathcal{S}| L_2^\Pi C_{PL}^2 < 1\). The informal "\(\ll 1\)" is just a high-level gloss; the formal condition is explicit.

4. **"Simulations claim to 'empirically validate the result'"** (Harsh Critic). The simulations are qualitative and illustrative — this is standard for theory papers. The phrase "empirically validate" is not uncommon for qualitative demonstrations of predicted trends. Not a meaningful weakness.

5. **Strength Finder's claim that simulations "validate the theory"** is somewhat overstated (they show qualitative alignment, not rigorous validation), but this is a strength-framing issue, not a weakness. The simulations do illustrate the predicted dependence on MDP complexity, which is a positive.

## Novel Insights

None beyond the paper's own contributions. The reviews largely confirm the paper's own framing: the key novelty is proving smoothness (Lemmas 1–4) rather than assuming it, and the convergence rates follow from standard smooth-analysis machinery once that property is established. The unresolved question from the reviews — whether Lemma 8's bound with \(\sqrt{|\mathcal{S}|}\) is tight or can be improved — is a technical detail the paper should address, not a new insight.

## Suggestions

1. **Define the MDP-complexity constants in the main text.** Add a one-sentence description for each of \(C_m, C_p, C_r, \kappa_r\) (or integrate Table 1 as text) so that Lemmas 2–4 are interpretable without cross-referencing a figure.

2. **Provide proof sketches for Lemma 5 and Lemma 8.** Even 2–3 sentences showing how Lemma 5 follows from the standard ascent lemma with the step-size condition, and how Lemma 8 uses smoothness to bound the gradient after one step, would significantly improve verifiability.

3. **Reformat the exponential convergence expression** to a cleaner form such as \(\rho^* - \rho^{\pi_k} \leq (\rho^* - \rho^{\pi_0}) \cdot c^{-k/2}\) or state it as linear convergence directly.

4. **Acknowledge the role of the appendix more clearly.** Since key proofs are deferred, a note at each lemma saying "Proof deferred to Appendix" would set reader expectations properly.

## Score and Decision

The paper tackles an important open problem — proving smoothness of the average reward (rather than assuming it) and deriving finite-time convergence guarantees for policy gradient. The core technical contribution (the projection technique in Lemma 1 and the smoothness analysis in Lemmas 2–4) is novel and significant. The main weaknesses are presentation issues: undefined constants in the main text, missing proof sketches for central lemmas, and minor formatting quirks. None of these threaten the validity of the contribution. The paper is ready for acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>