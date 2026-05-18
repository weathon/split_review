Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper provides theoretical upper and lower bounds on the number of tunable weights needed for ResNet with bottleneck blocks (b-ResNet) to approximate various function classes. The key result is that b-ResNet can approximate monomials of degree $p$ to accuracy $\varepsilon$ using $\mathcal{O}(p\log(p/\varepsilon))$ tunable weights—a factor of $d$ fewer than the corresponding bound for ReLU feedforward networks from DeVore et al. (2021). The paper extends this to polynomials, smooth functions in Sobolev space, continuous piecewise-linear functions, and a KST-based function class where it achieves $\mathcal{O}(d^4\varepsilon^{-1})$ tunable parameters, avoiding the curse of dimensionality.

## Strengths

- **Factor-of-$d$ reduction in tunable weights for monomial approximation (Theorem 3).** The paper shows that b-ResNet with constant width $N=4$ approximates any monomial with $\mathcal{O}(p\log(p/\varepsilon))$ tunable weights, compared to $\mathcal{O}(dp\log(p/\varepsilon))$ tunable weights for the ReLU FNN construction from DeVore et al. (2021). This is clearly stated and directly supported in Section 4.1 ("ResNet vs FNNs" paragraph).

- **Order-optimal $\varepsilon$-dependence for polynomial approximation.** Theorem 2 provides a $\Theta_d(\log 1/\varepsilon)$ lower bound on the neuron count for approximating polynomials, and the upper bounds in Theorems 3–4 match this dependence in $\varepsilon$. The paper explicitly notes this optimality (Section 4.1, end of "ResNet vs FNNs" paragraph; Section 4.2 after Theorem 4).

- **Curse-of-dimensionality avoidance for a dense function class via KST (Theorem 8).** The paper constructs a ResNet approximating any function in $K_C$ (a dense subset of $C([0,1]^d)$) with $\mathcal{O}(d^4\varepsilon^{-1})$ tunable parameters, avoiding exponential dependence on $d$. This is a novel application of KST within the ResNet framework, presented in Section 5.

- **Insightful mechanistic explanation of identity mappings' role.** The "Root of reduction" paragraph in Section 4.1 provides a clear intuition: identity mappings restore linear independence in the identity layer after a bottleneck, enabling constant-width b-ResNet to match the expressiveness of wider FNNs. This goes beyond a complexity bound to explain why skip connections enable the weight reduction.

- **Comprehensive coverage of multiple function classes with a unified framework.** The paper establishes results for monomials, polynomials, Sobolev-space smooth functions, CPwL functions, continuous functions, and a KST-based class. Lower bounds are systematically linked to FNN results via Proposition 1, creating a coherent theoretical framework.

- **Extension of ResNet's universal approximation to CPwL functions (Theorem 6).** The paper shows ResNet with one neuron per activation layer can exactly represent any CPwL function, improving on Lin & Jegelka (2018) which covered only step functions. This provides a constructive bridge to approximating continuous functions via spline methods.

## Weaknesses

### Fatal

None.

### Major

- **The factor-$d$ reduction claim rests on a comparison against a single FNN construction.** The paper compares its b-ResNet bound against the specific construction from DeVore et al. (2021), which yields $\mathcal{O}(dp\log(p/\varepsilon))$ tunable weights for monomial approximation. However, the paper does not argue that this is the best possible FNN bound or survey alternative FNN constructions (e.g., Yarotsky 2017, Shen et al. 2022b) that might achieve different rates. The lower bound in Theorem 2 only addresses $\varepsilon$-dependence and says nothing about the $d$ dependence. As a result, the headline claim of a "factor of $d$ reduction" is only demonstrated against one baseline, not established as a general separation between ResNet and all ReLU FNNs. The paper would be strengthened by stating the best known FNN bounds for each function class and showing how the ResNet result improves upon them.

### Minor

- **The experimental validation (Section 6) is too vague to be evaluable.** The paper states that b-ResNet is compared against a fully connected NN, but provides no network sizes, no training hyperparameters (learning rate, optimizer, epochs, batch size, data splits), and no explicit numerical error values in the text. The figures are embedded images that cannot be assessed from the text alone. For a theory paper, experiments are secondary, but if included they should contain enough detail to be interpreted. The claims that "b-ResNet outperforms fully connected NN" and "reduces training parameters" are unsupported as presented.

- **The sparsity mechanism for tunable weights is not explained.** Theorem 3 states that total weights are $\mathcal{O}(dp\log(p/\varepsilon))$ while tunable weights are $\mathcal{O}(p\log(p/\varepsilon))$, achieved because "in each constructive residual block, there are only absolute constant non-zero weights." The paper does not explain how this sparsity pattern is enforced in the construction—whether weights are initialized to zero and frozen, or learned with a sparsity-inducing regularizer. This is important for understanding the practical applicability of the bound.

- **The KST result (Theorem 8) targets a function class $K_C$ that the paper itself acknowledges is "not easy to characterize" and difficult to judge membership in.** The paper is transparent about this limitation (Section 5), which is commendable, but it does narrow the practical relevance of the result.

### Trivial

- The notation "$^b$-ResNet" in Theorem 3 is awkward and undefined (presumably meaning b-ResNet, which is defined earlier).
- The paper says results are shown in "Fig. 6 and 2" but only Figure 2 exists in the paper (Figure 6 likely a numbering error).

## Nice-to-Haves

- Adding a brief construction sketch of how a bottleneck ResNet block with constant width 4 approximates $x^2$ or $x\cdot y$ in the main text would help readers assess the factor-$d$ claim without needing to consult the proofs.
- Including explicit numerical error tables for the experiments would make the experimental validation self-contained.
- A discussion of the best known FNN bounds across multiple sources (Yarotsky 2017, Shen et al. 2022b, etc.) for each function class would strengthen the comparison.

## Removed Points

The following points from the harsh critic are removed per the filtering guidelines:

- **Missing constructions/proofs for the upper bounds (Theorems 3–6, 8) in the main text:** The parser strips appendix sections from all papers. Detailed constructions and proofs would be in the appendix, which existed in the original submission. The main text provides proof ideas (Section 2.2) and high-level intuition (Section 4.1 "Root of reduction"), which is standard for a theory paper.
- **Missing proof of Theorem 2:** Same rationale—the proof would be in the appendix.
- **Proposition 1 has no proof/reference:** Same rationale.
- **"Total vs tunable weights discrepancy never explained":** The paper does explain this in the note after Theorem 3: non-zero weights are constant per block, so the total tunable weights are $\mathcal{O}(p\log(p/\varepsilon))$ while total weights are $\mathcal{O}(dp\log(p/\varepsilon))$. The explanation is present, though the mechanism for enforcing sparsity is deferred to the appendix.
- **Claim that the paper doesn't even sketch construction ideas:** The paper provides proof ideas in Section 2.2, the "Root of reduction" intuition in Section 4.1, and states the constructions exist. For a theory paper of this length, this level of main-text exposition is standard.

## Novel Insights

The most insightful observation from the reviews is the recognition that the factor-$d$ reduction in tunable weights is claimed relative to a single FNN construction rather than established as a fundamental separation between ResNet and all ReLU FNNs. This reframes the contribution: the paper demonstrates that b-ResNet can match the approximation power of a *specific* FNN construction with fewer tunable weights, which is a meaningful but narrower result than a provable architectural advantage over *all* FNNs of comparable size. The "Root of reduction" explanation (identity mappings restoring linear independence after a bottleneck) is itself a genuinely insightful mechanism that goes beyond what most approximation-theory papers provide and is worth preserving.

## Suggestions

1. Broaden the comparison to include the best known FNN bounds for each function class (e.g., from Yarotsky 2017, 2018; Shen et al. 2022b), not just DeVore et al. (2021). This would place the factor-$d$ claim on firmer footing.
2. Add explicit numerical results and training details to the experiments section, even if brief, so that the empirical validation is evaluable.
3. Include a short construction sketch for at least one primitive (approximating $x^2$ with b-ResNet) in the main text to illustrate how skip connections enable the weight reduction.
4. Clarify how the sparsity pattern for "tunable weights" (non-zero parameters) is realized—whether by a training procedure or by architectural design.

## Score and Decision

The paper makes solid theoretical contributions to understanding ResNet's approximation capability, with clear theorem statements and an insightful explanation of how identity mappings enable weight reduction. The factor-$d$ reduction is demonstrated against a specific FNN construction, and the $\varepsilon$-optimality is established. The weaknesses are real but manageable: the comparison baseline is narrow, and the experiments are too sparse to evaluate. These do not threaten the core theoretical contribution.

**Originality:** Good. The paper provides the first explicit characterization of the number of tunable weights needed for ResNet approximation of several function classes.

**Importance of research question:** High. Understanding why ResNet is efficient in practice is an important theoretical question.

**Claims support:** The theoretical claims are well-stated. The factor-$d$ reduction is correctly caveated as a comparison against a specific construction.

**Soundness:** The theoretical framework (Proposition 1 linking ResNet to FNN for lower bounds, constructions for upper bounds) is reasonable. The experiments are too sparse to fully validate.

**Clarity:** The writing is clear, with good intuition provided for the key mechanism.

**Value to community:** The paper contributes useful theoretical bounds and a framework for analyzing ResNet approximation.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>