- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces a unified definition called *pseudo-iid* that characterizes weight distributions for which deep neural networks converge to Gaussian Processes in the infinite-width limit. The definition covers i.i.d. and orthogonal weights as special cases and is claimed to extend to low-rank and structured sparse fully connected networks, as well as convolutional networks with orthogonal filters. The paper provides numerical simulations for the fully connected case showing finite-width agreement with the predicted GP limit.

## Strengths

- **Unified definition that captures dependent weight structures (Def. 1).** The pseudo-iid conditions (row/column exchangeability, uncorrelatedness with proper variance scaling, 8th moment bound, and vanishing cross-correlation) are clearly stated and motivated. As argued in §1 and §2, this is the first definition that encompasses i.i.d., orthogonal, low-rank, and structured sparse weights within a single framework.

- **Novel construction for orthogonal CNN filters (§3.1).** The paper provides a concrete method for generating orthogonal convolutional filters by matricizing the signal rather than the filter, yielding a construction where the kernel's four-point cross-product expectation can be expressed in closed form using Lemma 3 of Huang et al. (2021). This is a practical contribution independent of the proof details.

- **Numerical validation at finite widths for multiple pseudo-iid families (Figs. 1–2).** The simulations show that for widths as small as 30, the empirical histograms and joint distributions of preactivations closely match the limiting GP prediction for i.i.d., dropout, low-rank, structured sparse, and orthogonal fully connected networks. 10,000 runs are used, and the visual agreement is clear.

- **Explicit treatment of the first-layer restriction.** The paper honestly acknowledges (§2) that the first layer must have i.i.d. Gaussian (or row-i.i.d.) weights because only one dimension scales with width, and footnotes possible relaxations. This shows technical awareness.

## Weaknesses

### Fatal
None.

### Major

- **The proof of the main theoretical result (Theorem 1) is absent from the compiled paper.** The paper contains a four-step proof sketch in a `\begin{comment}` block (lines 100–124), which would not appear in the submitted PDF. Even within that sketch, the critical verification that conditions (iii)–(iv) of Definition 1 suffice for the exchangeable CLT is merely asserted ("proceed by induction...sequentially verifying the moment assumptions...hold") without showing *how* the verification works. For a paper whose primary contribution is a theoretical extension of the GP limit, this omission means the core claim cannot be evaluated from the manuscript as presented. The proof needs to be included (or at minimum a rigorous sketch in the main text) for the paper to be publishable as a theoretical contribution.

### Minor

- **Verification of the pseudo-iid conditions for the examples is incomplete in key places.**
  - *Low-rank weights (§3.1):* The paper computes the four-entry expectation up to a point and then invokes "Lemma 3 of [Huang+2021]" without justifying its applicability to the rectangular orthonormal basis $C \in \mathbb{R}^{m \times r}$ (a matrix on the Stiefel manifold, not a square orthogonal matrix). The condition "when $r$ is linearly proportional to $m$" is stated but the connection to the lemma is not explained.
  - *Structured sparse weights (§3.1):* The paper states that for "suitable choices of $\mathcal{D}$" the moment conditions hold, but provides **no verification** of condition (iv) (the limiting cross-correlation condition). The sparsifying mask combined with random permutations may produce dependencies that do not vanish at the required rate; this needs explicit analysis.
  - *Orthogonal CNN filters (§3.1, lines 447–458):* The paper applies Lemma 3 of Huang et al. (2021) — a result for square orthogonal matrices — to the tall matrix $\widetilde{\mathbf{U}} \in \mathbb{R}^{c_{out} \times k^2 c_{in}}$ with orthogonal columns. The extension of the entry-wise moment formula to this setting is technically non-trivial and is not justified.

- **No experimental validation for the CNN result (Theorem 2).** All simulations are for fully connected networks. While the paper is primarily theoretical, including even a small-scale CNN experiment would substantially strengthen confidence in the separate convolutional definition and theorem.

### Trivial

- The simulations test only one activation (tanh) and one depth (7 layers). Testing additional activations or shallower depths would be a minor improvement.
- Condition (iii) in Definition 1 involves an unspecified constant $K$ that appears to depend on the distribution; the paper does not discuss whether such a constant exists for all examples or how one would verify it.

## Nice-to-Haves

- Include a concrete worked verification of condition (iv) for the structured sparse example, at least in a simplified setting (e.g., a specific $\mathcal{D}$ and block size).
- Provide a brief remark on how one would check the existence of the constant $K$ in condition (iii) for a given distribution.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The claim that the proof 'strictly generalizes' previous approaches is overstated."** — The paper's claim on line 30 is about presenting *a unified proof* that encompasses prior cases, which is accurate; the first-layer restriction is separately acknowledged. The criticism conflates "unified" with "less restrictive."
- **"The sentence 'The importance of condition (iii) is' appears to be cut off."** — This is likely a parser artifact; the paper as submitted would not have this formatting issue.
- **"The caption mentions Wasserstein distance but the corresponding figure is commented out."** — The Wasserstein figure is in a comment block with its own caption; this is a draft artifact, not a flaw in the paper's argument.
- **"No standard deviation or confidence intervals."** — Reporting CIs over 10,000 runs for histogram visualizations is not standard practice; the visual evidence is sufficient.
- **"Pure formatting/style nitpicks"** and **"typos/spelling/grammar" criticisms** — Per instructions, these are parser artifacts and not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same picture: the pseudo-iid definition is novel and practically motivated, but the paper's central theoretical claim cannot be assessed because the proof is absent from the compiled manuscript and the example verifications are incomplete in ways that are fixable but non-trivial.

## Suggestions

1. **Include the proof (or a rigorous sketch) in the main text.** At minimum, show how conditions (iii)–(iv) of Definition 1 are used to verify the assumptions of the exchangeable CLT (Blum et al., 1956). The induction step should be clearly demonstrated.
2. **Complete the verification of the examples.** For the low-rank and orthogonal CNN cases, either prove that Lemma 3 extends to the rectangular setting or provide a self-contained calculation. For the structured sparse example, verify condition (iv) explicitly.
3. **Add a small CNN experiment.** Even a single setting (e.g., one convolutional layer with orthogonal filters, small input size) would demonstrate that the CNN theorem is empirically plausible.
