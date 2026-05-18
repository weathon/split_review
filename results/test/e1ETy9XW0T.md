Now I have a thorough understanding of the paper and all claims. Let me write the consolidated review.

## Summary

This paper introduces a new metric — "unfair regret" — to study context length generalization in sequence prediction. The metric measures the performance gap between an online learner with limited context length \(L'\) and a benchmark predictor using longer context \(L\). The authors prove that spectral filtering algorithms can achieve \(\tilde{O}(\sqrt{T})\) unfair regret when trained with context as short as \(T^q\) and compared against a full-context (\(T\)) spectral filter, for noiseless linear dynamical systems under eigenvalue conditions. A two-autoregressive variant (Algorithm 2) relaxes these conditions when \(q \ge 1/3\). Experiments on synthetic LDS data validate the theory, and proof-of-concept experiments on induction heads and copy tasks suggest STU neural architectures built on spectral filtering exhibit length generalization empirically.

## Strengths

1. **Novel formal metric for context-length generalization.** The unfair regret (Definition 1) formalizes asymmetric-context comparison in a principled online learning framework, which is a clean conceptual contribution applicable beyond this paper. (Section 2.1)

2. **First provable sublinear unfair regret for spectral filtering.** Theorem 1 (and its detailed version, Theorem 3) shows \(\tilde{O}(\sqrt{T})\) unfair regret when training on \(T^q\) context vs. the best full-context spectral filter, for noiseless LDS under explicit eigenvalue and input-conditioning assumptions. This is a nontrivial theoretical result extending known properties of spectral filtering. (Section 3)

3. **Two-autoregressive variant removes the spectral assumption asymptotically.** Algorithm 2 and Theorem 2 (detailed as Theorem 5) prove that adding a second autoregressive term (\(y_{t-2}\)) enables length generalization for *all* marginally-stable LDS (nonnegative eigenvalues) when the context is at least \(T^{1/3}\), without case-by-case eigenvalue restrictions. (Section 3, Algorithm 2)

4. **Tensorized spectral filters are provably more expressive.** Theorem 4 (expressivity) shows tensorized spectral filters can represent certain time-varying systems that vanilla spectral filtering cannot, and the companion Theorem 6 extends the unfair regret guarantee to this richer class. (Section 4)

5. **Experimental validation of eigenvalue-dependent behavior.** LDS experiments (Figures 3–6) confirm the theory's prediction: vanilla spectral filtering fails in the "bad" eigenvalue region (Region B) and succeeds in Region A, while the two-autoregressive variant overcomes the limitation. (Section 5.1–5.2)

6. **Proof-of-concept length generalization in STU networks.** The induction heads and copy-task experiments show that STU (a neural architecture incorporating spectral filtering) exhibits nontrivial length generalization without task-specific modifications, with tensorization improving performance on nonlinear tasks. (Section 5.3–5.4)

## Weaknesses

### Fatal
None.

### Major
1. **The narrative conflates two distinct settings of "length generalization."** The theoretical results bound *unfair regret* within a fixed horizon \(T\): the learner trains *during* the sequence with context \(T^q\) and competes against a full-context predictor over the *same* \(T\) steps. The induction heads and copy experiments test a different setting: train on short sequences and evaluate on longer ones (beyond the training horizon). The paper calls both "length generalization," but the theory directly supports only the first. The second is presented as "proof-of-concept," which is honest but the overall framing — title, abstract, and introduction — risks misleading readers into thinking the theorems guarantee train-short-test-long transfer. This does not invalidate the theory, but the paper would be significantly stronger if it explicitly distinguished these two notions and clarified that the theoretical guarantees apply to the unfair-regret setting, not to generalization beyond the training horizon.

### Minor
2. **The claim that the two-autoregressive variant covers \([0,1]\) "for any \(T>0\)" is not technically correct for finite \(T\).** Line 59 states that for \(q \ge 1/3\), \([0, 1 - \log(T)/(8T^q)] \cup [1-1/T^{1/4}, 1] = [0,1]\) for any \(T>0\). The theorem itself assumes "sufficiently large \(T\)," and the union only equals \([0,1]\) in the asymptotic limit. For moderate \(T\) (e.g., \(T=10^4\)), a gap exists — the gap only closes when \(\log(T) \le 4T^{q-1/4}\), which for \(q=1/3\) requires \(T \gtrsim 10^8\). This is a standard asymptotic-vs-finite discrepancy, but the unconditional phrasing is over-optimistic.

3. **Input conditioning assumption receives insufficient scrutiny.** All theorems require \(\sum_{t=0}^{T-1} (T-t) u_t u_t^\top \succeq (2\|C\|\|B\|/\sqrt{T}) I\). The paper does not discuss when this holds (e.g., does it hold with high probability for random inputs? for what input distributions?), nor does it verify it empirically in the LDS experiments. If this condition fails, the theoretical guarantees collapse. Adding a brief discussion or empirical check would substantially strengthen reader confidence.

4. **The core experimental validation on LDS is limited to a single \(T\) and two values of \(q\).** The LDS experiments (Section 5.1) use \(T=2^{14}\) and test only \(q=7/8\) and \(q=1/2\). Since the theory predicts a *gradual* dependence on \(q\), a sweep over more values (e.g., \(q = 0.25, 0.5, 0.75, 0.875, 1\)) would be far more convincing. The selected \(q=7/8\) is suspiciously close to 1, making one wonder whether the result reduces to "use almost full context." The experiments on nonlinear tasks test more \(q\) values, but the core theoretical validation remains sparse.

5. **The theory requires autoregressive components; the nonlinear experiments do not use them.** The two-autoregressive and tensorized algorithms (Algorithms 2 and 3) rely on \(y_{t-1}\) and \(y_{t-2}\) for their theoretical guarantees. The induction heads experiments (line 377) explicitly use **no autoregressive components** ("Following prior STU architecture implementations we use **no autoregressive components**"). The theory therefore does not directly apply to these experiments. The paper presents these as "proof-of-concept" and the results are still interesting empirically, but the gap should be acknowledged more clearly.

6. **Notation inconsistency: \(|C|,|B|\) vs \(\|C\|,\|B\|\).** Theorem statements use \(|C||B|\) (line 38: \(\frac{2 |C| |B|}{\sqrt{T}}\)) while the bounds use \(\|C\|\|B\|\) (line 185). These presumably denote the same quantity (spectral norms), but the dual notation is confusing.

### Trivial
- The initial definition of unfair regret (line 32) omits the inner sum \(\sum_{t=1}^T\) inside the \(\min\) compared to the corrected version in Definition 1 (line 118). This appears to be a formatting/LaTeX issue but should be made consistent.
- The scaling \(\sigma_i^{1/4} \phi_i\) used in Algorithm 1 (line 170) differs from the standard spectral filtering prediction. A brief justification or citation for this design choice would help.

## Nice-to-Haves
- A systematic sweep over \(q\) in the LDS experiments (e.g., \(q = 0.25, 0.5, 0.75, 0.875\)) with unfair regret reported as a function of \(q\).
- A figure or table showing the actual eigenvalue-gap size for representative \(T\) and \(q\) values for both Algorithm 1 and Algorithm 2, to make the asymptotic-vs-finite behavior concrete.
- An empirical check of the input conditioning assumption on the experimental LDS inputs.
- Reporting the number of random seeds and error bars/confidence intervals for the LDS experiments.

## Removed Points
These points from the reviewers are flagged for removal — treat with caution:
- **"The paper does not provide a lower bound showing the excluded eigenvalue region is necessary."** The paper speculatively calls its empirical finding a "partial converse" (line 338–339) and never claims a proven lower bound. This is a strawman criticism.
- **"LLM motivation feels tacked on."** This is a preference about framing/scope, not a technical weakness. The LLM motivation is one paragraph in a theory paper and is standard positioning.
- **"The tensorized section has no theory supporting its length generalization advantage."** The paper explicitly states this is "not yet explained by theory" (line 413). The reviewer's observation is factually correct but the paper is transparent about the limitation.

## Novel Insights
Beyond the paper's own contributions, the most interesting observation from the reviews is the **structural tension between the theoretical setting (unfair regret within a fixed horizon) and the empirical setting (train-short-test-long)**. The fact that spectral filtering works in both settings suggests the unfair-regret framework may be a useful proxy for the harder train-short-test-long problem, but the paper does not make this connection explicit. A careful reader might ask whether unfair regret subsumes train-short-test-long generalization under certain conditions (e.g., when the LDS is time-invariant and the optimal predictor is stationary), which would be a valuable direction for follow-up work.

## Suggestions
1. **Reframe the narrative to separate two notions of length generalization.** Clearly label the theoretical results as "context-length generalization within a fixed horizon via unfair regret" and the nonlinear experiments as "preliminary evidence of train-short-test-long transfer." This prevents reader confusion without changing the technical content.
2. **Correct the overstatement on line 59** ("for any \(T>0\)") to "for sufficiently large \(T\)" to be consistent with the theorem's own assumption.
3. **Add a paragraph discussing the input conditioning assumption:** when it holds (e.g., sub-Gaussian inputs with bounded covariance), whether it's verifiable, and that it's an assumption the analysis requires rather than a fundamental limitation.
4. **Expand the experimental sweep over \(q\)** in the LDS experiment to at least 4–5 values to demonstrate the gradual dependence predicted by theory.
5. **Acknowledge the theory-experiment gap** for nonlinear tasks more explicitly: note that Algorithms 2–3 use autoregressive terms in their theory, while the STU experiments do not, so the theoretical explanation for the nonlinear results is only suggestive.

## Score and Decision

**Originality:** Good — the unfair regret metric is novel, and extending spectral filtering theory to context-length asymmetry is a fresh contribution.  
**Importance:** Moderate-high — length generalization is an active problem, and provable guarantees for any nontrivial predictor class are rare.  
**Claims:** Mostly well-supported, though the framing overreaches slightly by conflating two settings.  
**Soundness:** The theoretical results appear sound (the proof sketch is coherent). The experiments support the theory for what they test.  
**Clarity:** Good in the technical sections; could be improved by more precise framing of what kind of "length generalization" is being proven.  
**Value:** Positive — the paper provides a rigorous framework and a nontrivial guarantee for a practically relevant predictor class.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>