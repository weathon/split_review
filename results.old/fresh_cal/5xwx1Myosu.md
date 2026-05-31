I have now thoroughly read the paper and cross-checked every claim from both reviewers against the actual text. Let me produce the consolidated review.

---

## Summary

This paper provides theoretical and empirical evidence that feedforward and recurrent neural networks with fixed random weights can achieve universal function approximation when only hidden-layer biases are learned. The authors introduce formal definitions of *parameter-bounding* and *bias-learning* activations (satisfied by ReLU), prove Theorem 1 (FFN universal approximation via bias learning) and Theorem 2 (extension to RNNs for finite-time trajectory approximation), and support these with experiments on multi-task classification, mask-learning comparisons, and dynamical system forecasting.

## Strengths

- **Theorem 1 provides the first theoretical guarantee** that a single-hidden-layer FFN with *fixed random weights and only learned biases* can approximate any continuous function with arbitrarily high probability, establishing a previously absent theoretical foundation for bias-only optimization. (Section 2.1, Theorem 1)

- **Theorem 2 extends the result to RNNs**, proving that fixed-random-weight RNNs with learned biases can approximate finite-time trajectories from smooth dynamical systems — a first proof of the unit-masking-style SLTH for RNNs. (Section 2.2, Theorem 2; Section 1, line 39 also flags this contribution explicitly)

- **The definitions of γ-parameter-bounding and γ-bias-learning activations** (Definitions 2 and 3) formalize a novel sufficient condition for universal approximation under fixed bounded weights, and the paper proves that ReLU satisfies this condition — directly enabling both main theorems. (Section 2.1, Proposition 1)

- **Multi-task validation across seven image-classification datasets** shows that a single fixed-weight network with task-specific learned biases matches or nearly matches the accuracy of a fully-trained network of the same architecture, despite having roughly 800× fewer trainable parameters (32K vs. 25M). (Section 3.1, Fig. 1B)

- **Task-variance clustering analysis** provides a clear mechanistic insight: bias learning creates task-specialized hidden-unit clusters, consistent with the theoretical intuition that bias learning works by selectively activating/deactivating units per task. (Section 3.1, Fig. 1C)

- **Jacobian eigenvalue analysis in RNNs** reveals a concrete mechanism — bias learning changes the effective connectivity (Jacobian) to generate target oscillations even while the recurrent weight matrix remains random and fixed — offering dynamical-systems insight not present in prior SLTH work. (Section 3.3, Fig. 3B)

- **The paper openly acknowledges its limitations**: pointwise (not L¹) convergence for RNNs, finite-time trajectories, the soft-mask confound in bias-mask comparisons, and the gap between existence guarantees and learnability. This candor strengthens rather than weakens the contribution.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core theoretical claims are plausible, well-scoped, and the full proofs (for what is verifiable only as a main-text sketch) are deferred to the appendix — standard practice for conference submissions.

### Minor

- **The RNN proof sketch in the main text is too brief to evaluate independently.** The paper states the RNN proof is "analogous to Theorem 1" (line 124) in a single paragraph, without addressing how the embedding argument handles the recurrent weight matrix — for which the required matching involves ~N² entries per candidate subnetwork, a qualitatively harder combinatorial problem than the FFN case. While the full proof may reside in the appendix, a reader of the main text cannot assess whether the extension is sound. This is the paper's most significant presentational gap.

- **The pointwise (rather than L¹) convergence for the RNN theorem is a genuine weakening** for which the paper provides no proof that strengthening is possible — only a conjecture. This limits the theorem's practical force and the parallel with the FFN result. The authors acknowledge this, which is good, but the conjecture remains unsupported.

- **The experiments do not directly test the theory's asymptotic predictions.** The theory guarantees existence of a width (possibly enormous) achieving error < ε with probability > 1−δ. The experiments demonstrate that bias learning *works* at fixed moderate widths on specific tasks, which is a welcome sanity check, but they do not probe the scaling relationship (error vs. width) for the continuous function approximation setting the theory addresses. The MNIST scaling curve (Fig. 1A) is the closest proxy, but classification accuracy is not a clean function-approximation metric. The paper would be stronger with an explicit synthetic-function experiment showing error decreasing with width.

- **The soft-mask comparison uses a non-standard proxy for binary masking** (steepened sigmoid) with a learning schedule. The authors acknowledge this confound in the Discussion, but it means the comparison with mask learning is not definitive. Whether bias learning is systematically different from or better than hard-mask training remains an open question.

### Trivial
- The term "suitable activation" (Definition 1) is non-standard; the well-known equivalent condition "non-polynomial" (already cited) could be used directly to avoid introducing new jargon for a known concept.

## Nice-to-Haves

- A coarse asymptotic bound on how width must scale with ε, δ, din, and dout for the FFN theorem would turn the "exceedingly massive" qualitative statement into a more informative result. This is not required for correctness but would strengthen the contribution.
- An explicit formal definition of the pointwise convergence notion used in Theorem 2 would help the reader.
- For the RNN theorem, stating whether the subnetwork selection is per-time-step or global (it should be global, as biases are fixed) would clarify the argument.

## Removed Points

These points from the inputs are removed with justification:

1. **"The parameter-bounding property is insufficiently justified; Proposition 1 is stated without proof"** — The paper states Proposition 1 as a `restatable` (proved in appendix). Criticisms about missing appendix proofs are explicitly excluded by the review rules. The main text's intuition (norms grow with width even though individual entries stay bounded, differentiating this from band-limited parameter settings) is present and reasonable.

2. **"The li2023powerful citation appears to argue against the possibility the paper needs"** — The paper directly addresses this: "a bound on individual, scalar, parameters... as a network grows in width the bias vector and weight matrix norms will still grow accordingly" (line 76). The critic's reading is factually incorrect — the paper explains why band-limited results do not apply.

3. **"Missing related works"** — Excluded per instruction: do not mention missing related works without external sources.

4. **"Code repository not linked, hyperparameters not stated"** — Reproducibility nitpick of the kind excluded by the review rules. The paper states "all other hyper-parameters can be found in the codebase" (line 155).

5. **"The paper does not discuss whether there exist activation functions that are not bias-learning activations"** — The paper explicitly says "We leave it to future work to determine which other activations are parameter bounding" (line 76). This is scope-appropriate, not an omission.

6. **"The paper could mention that the theoretical results are existence results and do not guarantee gradient descent will find the required biases"** — This is a suggestion, not a weakness, and is implicit in any existence result.

7. **"The paper would be made significantly stronger by making the parameter-bounding property rigorous"** — This and other suggestions from the "Strengthening the Paper on Its Own Terms" section of the harsh critique are methodological suggestions already deferred to the appendix. They do not identify actual weaknesses in the presented work.

8. **"Formatting/style nitpicks"** — Removed per rules. The paper is well-structured and clearly written.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate the paper's stated claims but offer no synthetic insight that the paper itself does not already articulate.

## Suggestions

1. For the RNN theorem, expand the main-text proof sketch to at least outline how the subnetwork selection handles the recurrent weight matrix and state the required width scaling (even as "see appendix for details" with a qualitative roadmap).
2. Add a synthetic function-approximation experiment (e.g., a target function with known Fourier decay) showing bias-learning error decreasing with width, to directly illustrate the scaling predicted by Theorem 1.
3. Consider replacing "suitable activation" with the standard "non-polynomial" terminology for clarity.
4. For the mask comparison, either use a hard-mask training method (e.g., straight-through estimator) or explicitly note the non-definitive nature of the soft-mask proxy earlier in the section.

## Score and Decision

This paper makes a clear, novel, and well-motivated theoretical contribution: first universal approximation guarantees for bias-only learning in both FFNs and RNNs. The theoretical framing is clean, the connection to neuroscience is compelling, and the experiments provide meaningful qualitative validation and mechanistic insight. The main weaknesses — the brief RNN proof sketch in the main text and the experiments' limited direct engagement with asymptotic predictions — are addressable and do not undermine the core claims. The paper's honest and thorough discussion of its limitations is a further strength.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>