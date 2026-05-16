Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper provides theoretical upper and lower bounds on the number of tunable weights required for ResNet with bottleneck blocks (b-ResNet) to approximate monomials, polynomials, smooth functions, and a KST-based function class. The main result is that b-ResNet achieves a factor-of-\(d\) reduction in tunable weights compared to the best known ReLU FNN constructions, with approximation guarantees that are order-optimal in \(\varepsilon\). The paper also shows that ResNet can circumvent the curse of dimensionality for a dense subclass of continuous functions via the Kolmogorov Superposition Theorem.

## Strengths

- **Factor-of-\(d\) reduction in tunable weights for monomial approximation (Theorem 3).** The paper shows that b-ResNet approximates any monomial of degree \(p\) on \([0,1]^d\) with \(\mathcal{O}(dp\log(p/\varepsilon))\) total weights, of which only \(\mathcal{O}(p\log(p/\varepsilon))\) are non-zero (tunable). This is a clear \(d\)-factor improvement over the best known ReLU FNN upper bound of \(\mathcal{O}(d^2 p\log(p/\varepsilon))\) total weights / \(\mathcal{O}(dp\log(p/\varepsilon))\) tunable weights (DeVore et al., 2021). The paper explicitly states and discusses this comparison (lines 149), making the contribution concrete.

- **Order-optimal \(\varepsilon\)-dependence for polynomial approximation.** Theorem 2 gives a lower bound of \(\Theta_d(\log 1/\varepsilon)\) neurons for any ReLU FNN (and thus any ResNet via Proposition 1) approximating polynomials. Theorem 3's upper bound matches this \(\varepsilon\)-dependence, and the paper explicitly notes this optimality (lines 149, 173). This tightness is a strong theoretical contribution.

- **Circumventing the curse of dimensionality for a dense function class (Theorem 8).** For the class \(K_C\) (dense in \(C([0,1]^d)\)), the paper establishes that b-ResNet achieves \(\varepsilon\)-approximation with \(\mathcal{O}(d^4\varepsilon^{-1})\) tunable weights — polynomial in \(d\), directly avoiding the exponential dependence typical of uniform approximation in high dimensions. This is a noteworthy theoretical result.

- **Mechanistic explanation of how identity mappings enable efficiency ("Root of reduction," lines 151–152).** The paper provides a clear verbal argument explaining why identity mappings allow a bottleneck block with constant width to maintain linear independence across layers, turning what would be an additive reduction into a multiplicative factor-\(d\) reduction. This gives conceptual insight into why the construction works.

- **Exact representation of CPwL functions with narrow ResNets (Theorem 6).** The result showing that ResNet with only one neuron per activation layer can exactly represent any continuous piecewise linear function extends prior step-function results and demonstrates the expressive power of very narrow ResNets.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The central bottleneck-block construction for approximating \(x^2\) and \(xy\) is not sketched in the main text.** The paper states that it constructs b-ResNet blocks for these primitives (lines 84–91) and provides the "Root of reduction" analysis explaining *why* identity mappings help (lines 151–152), but no concrete block-level example, weight assignment, or schematic is given in the body. The paper relies on "as shown in our constructive proof" (line 145), deferring all detail to the appendix. While this is common practice for theory papers, including a brief concrete illustration (e.g., a 2-dimensional case with explicit weight values) would make the core claim immediately verifiable by the reader and is the single highest-leverage improvement. It does not undermine the validity of the results — the construction exists in the full submission — but it does reduce the self-containedness of the main text.

- **Experimental section (Section 6) is too minimal to be informative.** The experiments describe a test function, mention comparing b-ResNet with fully connected networks, and show MSE/MAX loss curves in figures that are not present in the parsed text. No architecture details, hyperparameters, dataset sizes, number of runs, or statistical significance are reported. The paper is primarily theoretical, so experiments are not required to support the core contribution; but if included, they should be presented with sufficient methodological detail to be interpretable. As they stand, they provide no evidentiary value and should either be expanded or removed.

- **Abstract makes an unsupported claim about "continuous-depth" networks.** The abstract states: *"Our results reveal that a continuous-depth network generated via a dynamical system possesses significant approximation capabilities even if its dynamics function is realized by a shallow ReLU network with absolute constant neurons."* The paper studies only discrete ResNet (as defined in Section 2.1) and contains no analysis of ODE-based continuous-depth models or dynamical systems. This claim in the abstract misrepresents the scope of the paper and is not justified by any result in the body. It should be removed or explicitly connected to the discrete ResNet studied.

### Trivial

None.

## Nice-to-Haves

- Include a brief (half-page) concrete example of a bottleneck block approximating \(x^2\), with explicit weight assignments, to make the central construction accessible in the main text.
- Clarify that the comparison in Theorem 3 is against *existing* FNN constructions (as the paper already does at line 149), not against a proven lower bound for FNNs — this is already handled but could be made more explicit.
- Remove the unsupported "continuous-depth" sentence from the abstract.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Critic's claim about "no discussion of the number of non-zero weights vs. total weights."** The paper explicitly discusses this distinction at lines 143–146: "Note that the number of total weights of \(R\) is \(\mathcal{O}(dp\log(p/\varepsilon))\) ... However, in each constructive residual block, there are only absolute constant non-zero weights ... Thus it is enough to adjust \(\mathcal{O}(p\log(p/\varepsilon))\) weights." This criticism is factually incorrect.

- **Critic's claim about "No analysis of the constant hidden in the \(\mathcal{O}\) for the smooth-function bound (Thm. 5)."** The paper provides explicit lower and upper bounds on \(c(d,r)\) at line 179: \((\frac{2^{(d+1)/r}d}{r})^d < c(d,r) < (\frac{2^{(d+1)/r}d}{r})^d d^{r+2}(d+r)r\). This criticism is factually incorrect.

- **Critic's claim that "The paper does not discuss how to know whether a given practical function belongs to \(K_C\)."** The paper acknowledges this limitation explicitly: "it is not easy to judge if a function belongs to \(K_C\). The outer function \(g\) can vary badly even though \(f\) is very smooth such as a linear polynomial" (line 223). The paper already addresses this.

- **Strength Finder's point about "Experimental validation of the theoretical bounds."** This conflicts with the verified weakness that the experimental section is too minimal to be informative. The experiments lack all methodological details (architecture, hyperparameters, number of runs, statistical significance), so claiming they "empirically confirm" the theory is not warranted from what is presented. This strength is dropped.

- **Critic's characterization of the missing construction sketch as a "structural flaw" and "impossible for the reader to evaluate."** The paper provides the high-level approach (lines 84–91) and the "Root of reduction" analysis (lines 151–152); the detailed construction is in the appendix, which is standard practice for theory papers. The characterization as a "structural flaw" is overstated for the genre.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel perspective that the paper itself does not already articulate. The key insight — that identity mappings in bottleneck blocks allow constant-width constructions to achieve a factor-\(d\) reduction in tunable weights — is already presented in the paper's "Root of reduction" paragraph.

## Suggestions

1. Add a concrete example (even one paragraph) of the bottleneck-block construction for \(x^2\) in Section 4.1. Show the weight values, how the identity connection is used, and why the number of non-zero weights per block is independent of \(d\). This single addition would address the most significant presentation gap.
2. Remove the "continuous-depth" sentence from the abstract, or replace it with a sentence that accurately reflects the paper's scope (discrete ResNet).
3. Either substantially expand the experimental section with full methodological details (architecture, hyperparameters, dataset generation, multiple runs with error bars) or remove it entirely, since the paper's contribution is theoretical and experiments are not required.

## Score and Decision

The paper makes a solid theoretical contribution: it provides the first comprehensive characterization of ResNet's approximation complexity, with clean upper and lower bounds and a genuine factor-\(d\) improvement over known FNN constructions. The weaknesses are all presentation issues (central construction deferred to appendix, unsupported abstract claim, uninformative experiments). None of these threaten the validity of the theoretical results, which are stated as theorems with proofs in the full submission. The paper would benefit from minor revisions but is publishable in its current intellectual form.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>