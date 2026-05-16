Now I have thoroughly verified the claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper extends the Gaussian Process (GP) limit for infinitely-wide neural networks from i.i.d. weight distributions to a broader class called "pseudo-iid" that only requires exchangeability, uncorrelatedness, and moment conditions. It proves GP convergence for fully connected networks (Theorem 1) and convolutional networks (Theorem 2) under this relaxed regime, with examples including low-rank, structured sparse, and orthogonal CNN initializations. The paper also discusses implications for Bayesian inference and Edge-of-Chaos analysis.

## Strengths

- **Unifies GP limits under a single, relaxed condition that subsumes prior cases.** The pseudo-iid definition (Definition 1) requires only exchangeability, uncorrelatedness, and four moment conditions rather than full independence. This explicitly includes the established i.i.d. and orthogonal cases while also covering low-rank and structured sparse initializations — settings where the GP limit could not previously be derived. The paper clearly states: "extend the seminal proof of [Matthews_2018] to a larger class of initial weight distributions (which we call \pseudoiid), including the established cases of \iid\ and orthogonal weights, as well as the emerging low-rank and structured sparse settings."

- **First theoretical result establishing GP limits for CNNs with non-i.i.d. convolutional filters.** Theorem 2 proves convergence to a GP for CNNs whose convolutional kernels satisfy the pseudo-iid conditions (Definition 3). The paper provides a concrete construction of orthogonal CNN filters via matricization of the kernel (Section 3.1) and checks the pseudo-iid conditions for this construction.

- **Provides explicit constructions for each new distribution class.** Section 3.1 gives concrete generating procedures: low-rank weights via $A = CP$ with random orthonormal $C$ and i.i.d. $P$; structured sparse weights via random row/column permutations of a sparse mask; and orthogonal CNN filters via reshaping an orthogonal matrix. These constructions demonstrate that the pseudo-iid framework is not vacuous.

- **Code is provided for reproducibility.** The paper includes a footnote with a URL to code for reproducing all figures.

## Weaknesses

### Fatal

None that invalidate the core mathematical possibility of the claim. However, see the Major weaknesses below.

### Major

- **The proof sketch for both main theorems is not present in the visible manuscript.** The section titled "Sketch of the proof of Theorem 1" (lines 100–124) is enclosed in a `\begin{comment}...\end{comment}` block, which means it does not appear in the compiled PDF. The reader therefore has no way to assess the validity of the paper's central theoretical claim. Theorems 1 and 2 are the core contributions; without at minimum a self-contained proof sketch in the main text — explaining how the pseudo-iid conditions (i)–(iv) replace the i.i.d. assumption in the Matthews et al. argument, how the Blum–DeHardt CLT for exchangeable arrays is applied, and how the induction proceeds — the paper's central result is unsubstantiated. This is a **structural** flaw, not a presentation nitpick. (Note: this is not about a parser-stripped appendix; the proof sketch is in the main body but deliberately commented out by the authors.)

- **Verification of the pseudo-iid conditions for the examples is incomplete in parts, and some steps rely on unsubstantiated claims.**
  - **Low-rank weights (Section 3.1):** The paper derives a four-point expectation and then states "Using the expression in Lemma 3 of [Huang 2021] we can calculate the above expectation and deduce condition (iv) when r is linearly proportional to m." The calculation is not performed, the resulting limit is not stated, and the dependence on the rank scaling ratio is not made explicit. The reader must take the claim on faith.
  - **Structured sparse weights (Section 3.1):** The paper says "for suitable choices of underlying distribution D, it satisfies the moment conditions." No specific distribution D is given, no verification of conditions (iii) or (iv) is attempted, and the reader is left to guess whether any realistic D works. This is too vague to constitute a valid example.
  - **Orthogonal CNN filters (Section 3.1):** The verification of condition (iv) relies on Lemma 3 of [Huang 2021], which was derived for random orthogonal matrices drawn uniformly from the Stiefel manifold. The paper's construction (reshaping a matrix with $\mathbf{\Tilde{U}}^\top \mathbf{\Tilde{U}} = (1/k^2)I$) does not guarantee a uniform draw. The paper acknowledges this ("we do not claim the generated orthogonal convolutional kernel U is uniformly distributed over the set of all such kernels"), but does not address whether Lemma 3's result still applies under the paper's non-uniform construction. This gap needs to be resolved or at least discussed.

- **Experimental validation covers only fully connected networks and lacks quantitative convergence measures.** Theorem 2 (the CNN limit) receives no experimental verification whatsoever — all simulations use fully connected architectures. Even for the fully connected case, the evidence is purely visual (histograms and scatter plots with overlaid level curves). No Wasserstein distance, Kolmogorov–Smirnov statistic, or any other quantitative metric is reported, despite the paper mentioning a Wasserstein-distance figure that is itself commented out (lines 461–468). The histogram at width $n=3$ is barely Gaussian, and no error bars or repeated-seed variability is shown. For a paper whose main contribution is theoretical, the experiments are supportive but too thin to rigorously confirm the convergence.

### Minor

- **The first-layer weights must be i.i.d. Gaussian (not pseudo-iid).** The paper acknowledges this (Definition 1: "When $W^{(1)}$ has i.i.d. Gaussian entries and the other weight matrices... are drawn from a pseudo-iid distribution"). The title "Beyond IID weights" is therefore slightly overstated — the relaxation to pseudo-iid applies only from layer 2 onward. The paper explains why (the first layer has only one dimension scaling up), but the limitation is real and somewhat undermines the generality implied by the title.

- **Simulations test only a special case (bias-free) of Theorem 1.** The footnote for the experiments states they used "weight variance σ_w=2 and without bias." Theorem 1 includes biases with variance σ_b². The bias-free setting is a valid special case, but the paper does not test the full claim.

- **Implications section (Section 3.3) is expository and does not contain new calculations or experiments.** The Bayesian NNGP and Edge-of-Chaos discussions describe what *could* be done with the results rather than demonstrating anything new. The paper states "our main contributions … allow similar calculations to be made" but does not make them. This does not weaken the theoretical contribution but means the "implications" are prospective, not demonstrated.

### Trivial

- Line 65–66 has a cut-off sentence: "The importance of condition (iii) is" with no continuation — a drafting error.
- The proof sketch section (§sec:fcn_proof_sketch) is referenced in the paper but exists only in the commented-out block, creating a dead reference in the visible text.

## Nice-to-Haves

- Provide a rigorous verification of at least one non-trivial example. For low-rank weights, carry out the full computation of conditions (iii) and (iv) explicitly, stating the scaling assumptions (rank proportional to width, scaling constant). For structured sparse, specify a concrete distribution D (e.g., Gaussian entries) and verify the moment conditions.
- Add quantitative convergence experiments for the fully connected case (e.g., Wasserstein distance vs. width, QQ plots) and include at least one CNN simulation (e.g., a single convolutional layer with random filters).
- Clarify whether condition (iv) in Definition 1 is required for all index choices or only for distinct rows/columns, and whether the notation assumes distinctness of $i_a, i_b, i_c, i_d$.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's concern about the structured sparse example "no explicit distribution is given"** → Kept as Major weakness because it is factually correct and substantive. The paper genuinely does not specify D.
- **Harsh critic's concern about Lemma 3 [Huang 2021] requiring uniform draws** → Kept as a Major weakness because it raises a genuine technical gap.
- **Strength Finder's claim that "Numerical validation directly supports the theory"** → Weakened (not removed) because the experiments are real but limited to visual evidence and FC-only architectures. The strength is partial.
- **Harsh critic's claim that "the paper as currently written provides the reader with no way to assess the validity of the central theoretical claim"** → Kept as Major weakness; it is factually accurate and fundamental.
- **Criticism that experiments use bias-free setting while theorem includes biases** → Kept as Minor weakness; it is factually correct.
- **Criticism about Implications section being purely expository** → Kept as Minor weakness; it is factually correct but not a fatal flaw.
- **Criticism about the cut-off sentence "The importance of condition (iii) is"** → Kept as Trivial; it is a drafting error.

## Novel Insights

The reviews do not surface any genuinely novel insight beyond the paper's own contributions. The central observation — that exchangeability plus moment conditions suffice for GP convergence — is the paper's own idea, and the reviewers primarily identify gaps in its execution rather than adding new perspective.

## Suggestions

1. **Uncomment the proof sketch (or include a self-contained one) in the main text.** The sketch currently in the `\begin{comment}` block is a reasonable outline (reduction to finite-dimensional vectors → linear projections → exchangeable CLT → induction). Restore it and ensure it is self-contained enough for a reader to follow the logic. This is essential — without it, the paper is a collection of claims with no argument.
2. **Complete the verification of the low-rank example.** Carry out the full calculation of condition (iv) for $A = CP$ when $r = \alpha m$, showing that the limit equals $\delta_{i_a,i_b}\delta_{i_c,i_d}$ and stating the required scaling constant explicitly.
3. **Specify a concrete distribution for the structured sparse example.** Show that e.g. Gaussian entries with a block-sparse mask and random permutations satisfy conditions (iii) and (iv), or at minimum give a plausible D and sketch why the moments converge.
4. **Address the uniformity concern for orthogonal CNN filters.** Either argue that Lemma 3 of [Huang 2021] holds for the specific non-uniform distribution generated by the paper's construction, or provide an alternative verification of condition (iv).
5. **Add quantitative metrics to the experiments** (e.g., Wasserstein distance between the empirical preactivation distribution and the limiting Gaussian, as a function of width) and include at least one CNN simulation to validate Theorem 2.
6. **Fix the cut-off sentence** at line 65–66 and remove or properly include the commented-out proof sketch and Wasserstein figure.

## Score and Decision

The paper proposes an interesting and well-motivated extension of GP limits to a broader class of weight distributions. The pseudo-iid definition is clean, the theorem statements are precise, and the practical motivation (low-rank, structured sparse, orthogonal CNNs) is timely. However, the paper in its current form has a structural problem that prevents evaluation of its central contribution: the proof sketch for both theorems is commented out and invisible to the reader, meaning the theoretical claim — which is the entire contribution — cannot be assessed. Additionally, the verification of the central examples is incomplete, and the experimental validation is thin and does not cover CNNs. These are not minor presentation issues; they are gaps in the substance of the paper.

The paper could become a solid contribution if the proof sketch (or a full proof) is restored, the example verification is completed, and the experiments are strengthened. In its present state, the paper does not meet the standard for acceptance because its core claim is unverifiable without the missing proof argument.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>