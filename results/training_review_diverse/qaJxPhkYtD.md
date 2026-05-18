Now I have enough information to write the final consolidated review. Let me compose it.

## Summary

This paper studies the expressivity of message-passing GNNs for counting graph substructures (cycles, cliques, quasi-cliques, connected components). The key idea is to analyze GNNs receiving i.i.d. random node inputs and show that suitable activation/normalization functions make the output correspond to statistical moments of the node representation distribution. From the closed-form expressions of these moments (e.g., \(\mathbb{E}[z^2], \mathbb{E}[z^3], \mathbb{E}[z^4]\)), the paper proves existence theorems that GNNs can count cycles of length 3–8, 4-cliques, quasi-cliques, and connected components. The analysis is constructive and yields Moment-GNN, an architecture that computes these moment-based features in closed form and achieves strong empirical results on cycle detection, cycle counting (ZINC), logP prediction, and graph classification (REDDIT).

## Strengths

- **Theoretical existence proofs for counting nontrivial substructures.** The paper proves that message-passing GNNs can count cycles of lengths 3–8, 4-node cliques, quasi-cliques, and connected components (Theorems 4.1–4.5, 6.1–6.3). These results go beyond what was previously known about GNN expressivity and are derived from closed-form expressions of statistical moments (Equations 6, 10, 12, 13). This is a genuine theoretical contribution.

- **Novel analysis using random node inputs to produce moment-based features.** Studying GNNs with i.i.d. random inputs (Section 3) and showing that elementwise power activations + expectation normalization yield representations corresponding to high-order moments of \(z = H(S)x\) is a fresh perspective. It connects GNN expressivity to tensor algebra (CPD models, Hadamard products of powers of S) in a way that is analytically tractable.

- **Constructive architecture with strong empirical validation.** The theoretical analysis directly motivates Moment-GNN (Proposition 5.1, Figure 1b), which computes moment features in closed form. The architecture is evaluated on four tasks: cycle detection (Table 1: >90% accuracy for lengths 4,6,8), cycle counting on ZINC (Table 3a: MAE ~10⁻³ for pentagons and hexagons), logP prediction (Table 4: MAE 0.373/0.328, state-of-the-art), and graph classification on REDDIT (Table 5: 94.58% accuracy). These results validate that the framework yields practically useful representations.

- **Favorable computational profile.** The paper notes that Moment-GNN has lower computational and memory complexity than RP, PPGN, Ring-GNN, and SMP (Section 7.2), yet matches or exceeds their performance, making the contribution practically relevant.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Main text lacks proof sketches for the central existence claims.** The paper's core contribution is a set of theoretical existence theorems (4.1–4.5, 6.1–6.3), yet the main text provides only the algebraic expressions (Equations 6, 9, 10, 12, 13) and the theorem statements. There is no sketch of *why* these expressions yield counts of specific substructures, how overlapping walks are resolved, or how polynomial coefficients \(h_k\) are chosen. All proofs are deferred to appendices. While deferring proofs is standard, the absence of even a brief intuition for at least one nontrivial case (e.g., how \(\mathbb{E}[z^3]\) counts 6-cycles) makes it difficult for readers to assess the plausibility of the claims from the main text alone. Adding a short proof sketch (1–2 paragraphs) for a representative theorem would significantly strengthen the paper.

- **The "counts" notion is ambiguous between per-node and per-graph.** The derived outputs are node-level vectors (e.g., \(\boldsymbol{y} \in \mathbb{R}^N\) in Equation 6, \(\boldsymbol{y}_1\) in Equation 9). The theorems say the GNN "counts the number of [substructure]" without clarifying whether this is the per-node count (how many substructures each node participates in) or a graph-level total (requiring aggregation such as summation over nodes). The downstream experiments clearly use graph-level predictions (binary classification for cycle detection, regression for cycle counting), implying a readout step, but the theoretical statements should explicitly specify this.

- **Gap between the theoretical architecture (random inputs + expectation) and the practical implementation (closed-form expressions).** The theory posits a GNN with random node inputs and expectation as a normalization layer; the practical Moment-GNN bypasses randomness by directly evaluating the closed-form moment expressions (Equation 14). The paper correctly notes this equivalence (Remark 5.1, Figure 1), but the theoretical claim is about *representation power* (existence of weights that yield the count), not about *learnability* via gradient descent on finite data from random inputs. The paper would benefit from explicitly discussing this distinction and whether a standard GNN trained via backpropagation on finite samples could discover the counting functions.

- **Missing definition of "quasi-clique."** Theorem 4.4 mentions "4-node and 5-node quasi-cliques (chordal cycles)" without defining what a quasi-clique is or specifying which substructures it refers to. The parenthetical "chordal cycles" does not clarify whether this means chordal cycles, near-cliques, or something else. A formal definition is needed.

- **The OOD generalization experiment (Table 2) is not described in the main text.** The paper claims that the counting ability generalizes to "any graph" (Theorems 4.2–4.5) and includes Table 2 ("Cycle detection for in- and out-of-distribution graphs"). However, the text does not describe what constitutes in-distribution vs. out-of-distribution in this experiment, what graph families are used, or how the OOD condition is constructed. This makes the empirical support for the generalization claim difficult to evaluate.

### Trivial

- The paper uses the term "moment" to refer both to statistical moments of the distribution of \(z\) and to the closed-form algebraic expressions. While the equivalence is shown, the dual usage could confuse readers about whether randomness is involved in the practical architecture.

## Nice-to-Haves

- An ablation study examining the contribution of each moment order (2nd vs. 3rd vs. 4th vs. 5th) would help connect the theory to the architecture and show which moments are most important for different tasks.
- Testing exact counting (regression, not classification) for 7- and 8-node cycles on synthetic data would directly validate Theorems 4.5 and 6.3 beyond what ZINC's molecular graphs offer.

## Removed Points

- **"No experiment tests zero-shot transfer"** (HC #3) — **Removed.** The paper includes Table 2 explicitly titled "Cycle detection for in- and out-of-distribution graphs," contradicting this claim. The OOD experiment exists, though it is insufficiently described.
- **"Theorem 4.1 is not explained"** — **Removed as partially inaccurate.** The paper explicitly notes (line 107) that Theorem 4.1 is weaker and limited to observed training graphs, setting correct expectations.
- **Citation formatting issues (e.g., Vignac et al. 202O)** — **Removed.** These are parser artifacts, not author errors.
- **Several generic strength claims from Strength Finder** — **Removed.** Redundant with or subsumed by the retained strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a 1–2 paragraph proof sketch in the main text for at least one representative theorem (e.g., how \(\mathbb{E}[z^3]\) yields 6-cycle counts). This will make the theoretical contribution verifiable without requiring readers to reconstruct the argument from the appendix.
2. Clarify in each theorem whether the count is per-node or per-graph, and specify the readout/pooling operation used to obtain graph-level quantities.
3. Provide a formal definition of "quasi-clique" in the main text.
4. Describe the OOD experimental setup for Table 2 in the main text: what distinguishes in-distribution vs. out-of-distribution, which graph families are used, and what the results show.
5. Add a brief discussion in Section 5 or 8 distinguishing representation power (the existence claim of the theorems) from learnability (whether standard gradient-based training on finite data can discover the counting functions).

## Score and Decision

The paper makes a genuine theoretical contribution — proving that message-passing GNNs can count a range of substructures that were previously thought to be beyond their reach — and supports it with a constructive architecture that achieves strong empirical results. The weaknesses are primarily matters of presentation clarity (missing proof sketches in the main text, ambiguous counting semantics, insufficiently described OOD experiment) rather than fatal errors. With reasonable revision, these concerns are addressable.

**Score: 7.0 / 10**
**Decision: Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>