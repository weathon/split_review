Now I have a thorough understanding of the paper. Let me compile the final review, carefully verifying every claim against the actual text.

---

## Summary

This paper extends the infinite-width Neural Network Gaussian Process (NNGP) limit to a broader class of weight distributions called "pseudo-iid," which relaxes the standard i.i.d. assumption to allow exchangeable, uncorrelated entries with controlled moment conditions. The authors prove (Theorem 1) that deep fully-connected networks under the pseudo-iid regime converge to a GP, and extend this result to convolutional networks (Theorem 2, Definition 3). Three example families are presented — low-rank (via random orthonormal basis + i.i.d. factors), structured sparse (via randomly permuted masked matrices), and orthogonal CNN filters — as concrete instantiations. Numerical simulations for the fully-connected case validate finite-width convergence, and the paper discusses implications for Bayesian inference and Edge-of-Chaos analysis.

## Strengths

- **Unified theoretical framework for GP limits under non-i.i.d. weights.** The pseudo-iid definition (Definition 2) cleanly captures a broad class of dependent weight distributions via exchangeability, variance scaling, an eighth-moment bound, and a vanishing cross-correlation condition. Theorems 1 and 2 prove GP convergence for both fully-connected and convolutional architectures under these conditions. This generalizes prior work (Matthews+18, Lee+17, Huang+21) under a single, well-structured formalism.

- **Extension to convolutional networks with a novel filter construction.** Definition 3 provides the first pseudo-iid conditions for convolutional kernels, and Theorem 2 derives the corresponding GP limit. The orthogonal CNN filter construction (Equation 4, Section 3.1) via matricization of the kernel and imposing \(\widetilde{\mathbf{U}}^\top\widetilde{\mathbf{U}} = (1/k^2)I\) is a novel approach that is meaningfully different from prior orthogonal CNN definitions (Xiao+18, Wang+20, Qi+20). The verification of conditions (i), (ii), and (iv) for this example (lines 447–458) is reasonably explicit, referencing Lemma 3 of Huang+21 for the four-cross expectation.

- **Empirical validation of finite-width convergence.** Numerical experiments (Figures 2 and 3) for fully-connected networks with widths \(n=3, 30, 300\) show that the empirical distribution of preactivations matches the predicted GP for low-rank, structured sparse, and orthogonal weight distributions. The convergence is clearest for the orthogonal case, but all cases show good agreement by \(n=300\). The code is provided.

- **Careful treatment of the first-layer restriction.** The paper explicitly notes (lines 66–68 and footnote) that the first layer requires i.i.d. rows (or Gaussian i.i.d. entries) because its scaling dimension does not permit the dependencies that deeper layers can accommodate. This technical limitation is honestly stated rather than glossed over.

## Weaknesses

### Fatal
None.

### Major

1. **Proof sketch is inside a LaTeX `comment` environment in the main text and thus not visible to readers.** Lines 100–124 contain a bullet-point proof sketch (outlining the 4-step argument: reduction to finite-dim convergence, linear projections, exchangeable CLT, induction) entirely within `\begin{comment}...\end{comment}`. A reader of the rendered document sees no proof sketch at all. While the paper does describe its proof approach verbally (references to Matthews+18, the exchangeable CLT of Blum et al., and induction over layers), the visible main text lacks a self-contained outline. For a theoretical paper whose central contribution is a proof, this is a significant presentation gap. *(Note: The full proof is presumably in the appendix, which the parser stripped — that is not the authors' fault. But the commented-out sketch is an author-level decision and means the main text, as submitted, is incomplete.)*

2. **Verification of pseudo-iid conditions for the examples is uneven and incomplete in two of three cases.**  
   - **Structured sparse weights (line 185):** The paper states that "for suitable choices of underlying distribution \(\mathcal{D}\), it satisfies the moment conditions." No concrete \(\mathcal{D}\) is specified, and no computation or argument is given for conditions (iii) or (iv). This is effectively a placeholder rather than a verification.  
   - **Low-rank weights (lines 179–183):** The computation for condition (iv) is sketched and references Lemma 3 of Huang+21, but only when "\(r\) is linearly proportional to \(m\)." Condition (iii) (the eighth-moment bound) is not addressed at all — the paper merely notes it is "controlled by the choice of distribution \(\mathcal{D}\)" without any bound or concrete example.  
   - **Orthogonal CNN (lines 447–458):** This case is reasonably well-verified, with explicit checks of exchangeability and condition (iv) via the known four-cross expectation for Haar-orthogonal matrices.  
   The unevenness is a concern because the paper's practical claims depend on these examples being genuine instances of the pseudo-iid regime. The structured sparse case in particular lacks any real verification.

### Minor

3. **Title overstates the scope of the result.** The title "Beyond IID weights: sparse and low-rank deep Neural Networks are also Gaussian Processes" implies that *arbitrary* sparse or low-rank weight matrices (e.g., those arising from magnitude-based pruning, unstructured SVD, or the lottery ticket hypothesis) fall under the result. What the paper actually proves covers specific *constructed ensembles*: low-rank via a random orthonormal basis with i.i.d. factors, structured sparse via randomly permuted masked matrices, and orthogonal CNN filters under a specific matricization. The motivational discussion (Section 1, paragraph 3) tying the work to the lottery ticket hypothesis and pruning-at-initialization methods suggests wider applicability than is actually established. The paper would benefit from more precise language.

4. **No CNN simulations are shown.** Theorem 2 and the orthogonal CNN example are presented in Sections 2.2 and 3.1, yet all numerical experiments (Figures 2 and 3) are restricted to fully-connected networks. Given the non-trivial nature of the orthogonal CNN construction, empirical validation would substantially strengthen the paper's claims for the convolutional case.

5. **First-layer restriction limits practical applicability.** The paper requires the first layer to have i.i.d. rows (or Gaussian i.i.d. entries), so low-rank and structured sparse initializations cannot be applied to the first layer — which is often the largest layer in terms of parameters. This is acknowledged in a footnote but the practical implications (e.g., on the claimed computational speed-up from sparsity/low-rank at initialization) are not discussed.

### Trivial

None beyond the issues captured above.

## Nice-to-Haves

- A more complete verification of condition (iii) (the eighth-moment bound) for the low-rank example, or alternatively, specifying a concrete distribution \(\mathcal{D}\) that works.
- Numerical simulations for the CNN case (Theorem 2), even for a simple architecture.
- A brief discussion of known counterexamples or boundary cases where pseudo-iid conditions fail despite superficial similarity (e.g., unstructured magnitude-based sparsity), to clarify the regime's scope.

## Removed Points

- **"No proof exists at all" / "paper relies entirely on the appendix which was stripped"**: The hard rules require removing weaknesses about missing appendix content since the parser strips these sections. The full proof presumably exists in the appendix. The visible weakness is the *commented-out sketch*, which is genuine and retained above as Major #1.
- **"The Edge of Chaos and BNN sections are purely commentary"**: These are discussion/implication sections, not claimed as novel results. Faulting them for not deriving new results is an expectation mismatch — the paper's main contribution is the GP limit, and noting its implications is standard.
- **"The paper does not mention any counterexample"**: This is a nice-to-have, not a weakness.
- **"Missing related works"**: Hard rules prohibit mentioning missing related works.
- **Orthogonal CNN verification complaints** (ambiguous distribution, exchangeability complications): The paper's description ("drawn uniformly random with orthogonal columns") is standard language for the Stiefel manifold, and the exchangeability argument for row/column blocks is correctly reasoned. The reviewer's pedantry here is not justified by the actual text.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the paper itself does not make.

## Suggestions

1. **Uncomment and expand the proof sketch** in Section 2.1. Even a 4-bullet sketch (as exists in the commented-out lines) would make the main text self-contained for a reader who does not immediately dive into the appendix.
2. **Replace the placeholder verification for structured sparse weights** with a concrete example. Choose a specific \(\mathcal{D}\) (e.g., a centered distribution with finite eighth moment such as Gaussian or uniform), compute or bound the relevant moments, and show condition (iv) holds. This would take no more than a few lines.
3. **Add a qualifying phrase to the title** (e.g., "...are also Gaussian Processes under exchangeability conditions") or at minimum rephrase the abstract and introduction to clarify that specific *constructed ensembles* are covered, not all sparse/low-rank networks that arise in practice.
4. **Add at least one CNN simulation** validating Theorem 2 for the orthogonal CNN construction, even on a small-scale task like CIFAR-10 with a 2-layer CNN.
5. **Discuss the practical impact of the first-layer restriction** more explicitly — does the computational benefit of low-rank/sparse initialization survive when the largest layer cannot use it?

## Score and Decision

The paper introduces a genuinely useful theoretical framework (the pseudo-iid class) and proves meaningful generalizations of the NNGP limit. However, the main text's visible proof is essentially absent (commented out), and the example verifications that demonstrate the framework's applicability are incomplete for two of three cases. The title overclaims. These are fixable issues, but in their current form they prevent the paper from being a clean accept. 

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>