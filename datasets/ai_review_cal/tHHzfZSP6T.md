- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 3, 8
Now I have all the information I need. Let me construct the final review.

---

## Summary

This paper studies whether Transformers can compositionally generalize — i.e., learn to apply unseen combinations of simple functions after training on only a small subset of compositions. Using a synthetic domain of bijections and permutations on a small vocabulary, the authors show that Transformers trained with a "step-by-step" prompt format (where intermediate outputs are provided during training) can generalize to exponentially many unseen compositions from as few as 30–100 training examples. They characterize conditions for in-order vs. out-of-order generalization, compare step-by-step vs. direct prompting, and provide mechanistic analysis via linear probes and attention visualization. The core contributions are a clean empirical demonstration and a formal framework (displacement) for analyzing compositional generalization failures.

---

## Strengths

1. **Clean empirical demonstration of exponential/combinatorial generalization (Fig. 4).** The paper shows that a Transformer trained on only 30–100 in-order compositions in the step-by-step format achieves near-perfect accuracy on all 3125 possible compositions — all of which are unseen during training. This is a striking result, clearly presented, and directly supports the paper's central claim.

2. **Sharp contrast between step-by-step and direct prompting (Fig. 6, Left).** The paper shows that with direct prompting (no intermediate outputs), the same architecture fails to generalize even when trained on 2000 of the 3125 compositions. This contrast provides concrete evidence that generating intermediate outputs is the key enabler, and it is a well-controlled ablation.

3. **Displacement analysis for out-of-order generalization (Fig. 5).** The formalization of "displacement" (Hamming distance between the order of functions in a composition and the in-order baseline) is a useful analytical tool. The paper systematically varies displacement in the training data and shows that out-of-order generalization degrades with increasing displacement unless the training data includes out-of-order examples. This is a precise characterization of a failure mode.

4. **Mechanistic analysis via linear probes and attention visualization (Fig. 7).** Using a well-established probing technique (unembedding layer as probe), the paper shows that accuracy increases sharply in the latter layers, localizing compositionality to later attention/MLP blocks. The attention maps for a 1-layer model further show that tokens attend to their relevant task and data tokens. This provides converging evidence for the mechanism.

5. **Training dynamics analysis (Fig. 8).** The paper shows that models trained on the 21-base condition generalize to fewer-function compositions first, while models trained on random in-order compositions generalize to more-function compositions first. This nuanced finding reveals how training data composition shapes the order in which capabilities emerge.

---

## Weaknesses

### Fatal
None. The core experiments are sound and support the stated claims within the synthetic domain. No verified flaw invalidates the paper's contributions.

### Major

1. **The paper overclaims the scope of its findings relative to the evidence.** The language throughout — "explosion of capabilities," "this could explain why language models show signatures of compositionality" — implicitly extends the results to large-scale LLMs. But the experimental setup uses a vocabulary of 10 tokens, simple bijections and permutations (effectively lookup tables), a maximum composition length of 5, and a step-by-step format that provides full intermediate supervision during training. The gap between this regime and real LLMs performing multi-step reasoning on open-domain text with ambiguous tasks is enormous. The paper acknowledges the synthetic nature of its setup in the introduction ("we choose to limit the purview... to a well-defined synthetic domain") but nevertheless repeatedly uses broad language that invites exactly the extrapolation the evidence cannot support. The claims would be more appropriate if scoped precisely to "Transformers in this synthetic, fully-observed setting can generalize compositionally under these conditions."

2. **No variance or statistical significance reported.** All figures appear to report results from a single run. Given the randomness in training data selection (e.g., "30 random compositions"), the choice of random seeds, and the inherent variance in Transformer training, reporting accuracy without error bars, confidence intervals, or replication across seeds makes it impossible to assess the robustness of the results. This is a standard expectation even in synthetic/interpretability work, where a mean ± std over 3–5 seeds is the norm. The critic who pointed this out is correct.

### Minor

1. **The step-by-step format provides strong intermediate supervision that fundamentally simplifies the problem.** The paper acknowledges this and contrasts it with direct prompting, which is good. However, the framing throughout treats the step-by-step format as a benign "recursive processing" mechanism. In reality, training with step-by-step targets means the model only ever needs to apply a single function per autoregressive step — it never has to learn to compose multiple operations in a single forward pass, which is what genuine compositionality would require. A fairer test of whether the model can *internally* compose would be to train on step-by-step but test on direct prompts (forcing the model to generate the full composition without intermediate targets), or to train on direct prompts and test whether internal representations encode compositional structure. Neither experiment is performed.

2. **The "21 base" negative result is under-discussed.** The paper shows that training exclusively on primitive functions plus identity yields zero compositional generalization. This is presented as a null baseline, but its implications deserve deeper treatment: it demonstrates that learning primitive capabilities is not sufficient — the model must see explicit compositions during training. This directly constrains the paper's motivating question about LLMs (if pretraining data lacks many explicit multi-step chains, can compositionality emerge?). The paper mentions the result but does not grapple with its implications.

3. **No per-composition breakdown of generalization accuracy.** Accuracy is reported as an average over all 3125 compositions. It is possible (even likely) that the model generalizes perfectly to compositions that differ trivially from training examples while failing on those that are genuinely novel in some structural sense (e.g., high displacement, unusual function combinations). Reporting per-composition accuracy distributions or failure analysis would substantially strengthen the claims.

4. **Limited comparison of architecture generalization.** The paper states that "the inductive bias of the architecture contributes to compositional generalization and any autoregressive model is not guaranteed to succeed" but provides no comparison to other architectures (e.g., LSTMs, state-space models, MLPs). Given the controlled setting, such comparisons would be straightforward and would contextualize the Transformer's performance. (Note: the Strength Finder's claim that "LSTMs fail to generalize" is not present in the paper — the paper does not mention LSTMs.)

### Trivial
- The paper's figures are clean and readable. No significant formatting issues are present in the submission content (garbled characters in the extracted text are parser artifacts, not author errors).

---

## Nice-to-Haves

- **Add error bars** across multiple random seeds (at least 3–5) for all main results.
- **Test generalization under chain length variation**: all experiments use L=5. Varying L from 1 to 10 would test whether compositionality degrades with chain length.
- **Add a per-composition error analysis**: identify which types of compositions the model systematically fails on (e.g., those requiring high displacement, those involving rare functions).
- **Train on step-by-step, test on direct prompts**: this would test whether internal representations learned under step-by-step supervision enable zero-shot composition without intermediate targets.
- **Test on function families outside the training set**: e.g., compositions involving functions not seen during training. This would test whether the model composes or merely interpolates among known functions.
- **Ablate the number of positions L** to test scalability of the compositional generalization result.

---

## Removed Points

These points were flagged by the reviewers but are removed for the reasons stated:

- **"LSTMs fail to generalize" (Strength Finder, claim #5):** The paper does not mention LSTMs at all. This strength is factually incorrect and is removed.
- **"Neither is done" about testing direct prompts (Harsh Critic, Issue 1):** The paper *does* test direct prompting (Section 4.3, Fig. 6 Left) and shows it fails. The critic's specific suggestion of "train on step-by-step, test on direct" is a separate experiment that is not done, but the claim that "neither is done" is inaccurate.
- **"The 21 base failure is buried in a figure caption":** The paper discusses the 21 base result in the main text of Section 4.1 ("We also observe that 21 base... does not compositionally generalize") and in Section 4.2. It is not buried.
- **Various speculative concerns:** "It is possible that the model generalizes perfectly to compositions that differ trivially" (speculative without evidence); "The paper does not discuss variance across random seeds or runs" (the core point is kept as a major weakness, but multiple speculative sub-claims about what "might" be happening are removed).
- **Formatting nitpicks, missing appendix references, missing related works:** These are parser artifacts or outside the scope of verification.
- **Criticisms about "comparison to simpler baselines" beyond the paper's stated scope:** The paper is explicitly scoped as an interpretability study, not a methods comparison paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper that the paper does not already contain or directly imply.

---

## Suggestions

1. **Recalibrate the language** to match the evidence. Replace phrases like "explosion of capabilities" with more precise descriptions such as "generalization to exponentially many unseen compositions." Scope the LLM implications explicitly as speculation rather than implication.
2. **Add error bars** over multiple random seeds for all main figures (Figs. 4, 5, 6).
3. **Add a per-composition failure analysis** to Fig. 4, showing whether errors concentrate on specific composition types.
4. **Expand discussion of the 21-base null result**: why does learning primitive functions fail to yield compositionality, and what does this imply about the need for compositional data in training?
5. **Consider a cross-evaluation experiment**: train on step-by-step, test on direct prompts to assess whether the model has learned internal composition ability.

---
