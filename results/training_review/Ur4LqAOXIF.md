Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces SODA, an online framework for out-of-distribution (OOD) detection that continuously adapts an OOD detector as data streams in from a deployed environment. The environment is modeled as a time-varying mixture of ID and OOD distributions. The proposed algorithm updates the model via online gradient descent using feedback (ID/OOD labels and class labels) provided at each timestep. The paper proves a sub-linear regret bound of \(O(\sqrt{T})\) against the best fixed model in hindsight and reports empirical gains over offline OOD detection methods on CIFAR-10 and ImageNet-1k.

## Strengths

- **Formal definition of online OOD detection with a non-stationary environment model.** The paper introduces a rigorous mixture distribution (Equation 1) that allows the OOD distribution to change over time, generalizing prior stationary "in-the-wild" formulations. This formalization provides a principled basis for the framework and is a clear conceptual advance over static OOD detection.

- **Provable sub-linear regret bound with theoretical decomposition.** Theorem 3.1 proves that SODA achieves regret bounded by \(\tilde{O}(\sqrt{T})\), and the bound is decomposed into ID and OOD components (Equation 6). While the bound is standard in online convex optimization, it provides a theoretical foundation for the online OOD setting and offers insight into how the mixture ratio and data complexity affect convergence.

- **Flexible instantiation with different OOD scoring functions.** Section 4.3 demonstrates that SODA can be instantiated with MSP, ODIN, and Energy scoring functions, each requiring only appropriate modification of the ID and OOD loss terms. This shows the framework is general and can accommodate various existing OOD detection techniques.

- **Empirical validation of regret behavior under non-stationary OOD shifts.** Figure 1b shows that SODA recovers sub-linear convergence after OOD distribution changes, with the regret plot providing some insight into the learning dynamics under distribution shifts.

## Weaknesses

### Fatal

None. The paper's core idea (formalizing an online OOD setting) is legitimate and the algorithmic framework is coherent within its stated assumptions. However, the severity of the issues below means the paper would need substantial revision before acceptance.

### Major

- **Oracle feedback assumption is incompatible with the OOD detection problem framing.** The framework (Algorithm 1) requires the environment to provide the true ID/OOD label *and* the class label for ID samples at every timestep during deployment. The loss computation directly depends on knowing whether \(\mathbf{x}_t\) is ID or OOD (lines 7–11 of Algorithm 1). This assumes away the very problem OOD detection is designed to solve — namely, distinguishing ID from OOD without access to such labels at test time. The paper claims "practicality" as a benefit (Section 1, bullet 2: "offering a pragmatic approach to real-world OOD detection"), yet the framework applies only to settings where one already knows the answer the detector is supposed to provide. The "unsupervised extension" is mentioned exactly once (line 18) but is never defined, formalized, or evaluated, so it cannot salvage the practicality claim.

- **Unfair comparison with offline methods invalidates headline empirical results.** SODA receives oracle ID/OOD labels and class labels at every streaming timestep. Offline baselines (MSP, ODIN, Energy, Mahalanobis, etc.) are trained only on labeled ID data and receive no OOD exposure during training. WOODS (Katz-Samuels et al., 2022) uses an unlabeled wild mixture dataset without per-instance OOD feedback. The claimed improvements — e.g., 18.54% FPR95 reduction over WOODS — are a reflection of the radically different supervision levels rather than algorithmic superiority. The paper acknowledges differences with WOODS (line 143: "performance comparisons between these two methods should be interpreted with these differences in mind") but then proceeds to draw the unjustified conclusion that SODA "significantly outperforms" offline methods (line 20, line 141). Comparing methods under fundamentally different information constraints and claiming victory is not informative. At minimum, a version of SODA that does *not* receive oracle feedback (the promised "unsupervised extension") would be needed for a meaningful comparison.

### Minor

- **The "unsupervised extension" is mentioned but never delivered.** The introduction promises "a straightforward unsupervised extension for SODA, enabling SODA to tackle the online setting without necessitating any environment feedback" (line 18). This extension is never defined, formalized, or evaluated anywhere in the paper. Given that the core weakness of the framework is its reliance on oracle feedback, the absence of this extension is a significant gap that prevents the paper from bridging the framing to the actual contribution.

- **The regret bound does not support the claims about non-stationary adaptation.** Theorem 3.1 provides a regret bound against the best *fixed* model in hindsight — this is a standard result in online convex optimization. The paper claims "SODA is sub-linear in regret with no assumption on the stationarity of the environment OOD" and interprets this as "converging to the optimal OOD detector" (line 101). However, in a non-stationary environment, the best fixed model in hindsight may be very poor, and achieving sub-linear regret against it does not imply good tracking of changing OOD distributions. The bound itself depends on \(\sup_{\mathbf{x}\sim\mathcal{P}^{\text{out}}}\|\mathbf{x}\|_2\) and \(\tilde{\pi}\), both of which involve unknown quantities about the OOD distribution. Dynamic regret or interval regret would be more appropriate for the claimed setting.

### Trivial

None.

## Nice-to-Haves

- An evaluation of SODA *without* oracle feedback (the promised unsupervised extension) compared against offline methods under identical information constraints would transform this paper from an upper-bound analysis into a practical solution.
- A dynamic regret analysis (or at least discussion of why the static comparator is meaningful under distribution shift) would strengthen the theoretical framing.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that Algorithm 2 and loss function details are missing from the paper.** The extracted text cuts off at "At every round" (line 76) and the Algorithm 2 reference points to content not captured by the parser. This is a parser/formatting artifact — the original PDF likely contains these details (equations, algorithm boxes). Per the formatting-artifact rule, this criticism is removed.
- **Criticism about table extraction and incomplete figures.** Same parser-artifact basis.
- **Criticism about the regret bound symbols lacking derivation.** The paper defines \(\tilde{\pi}\), \(\beta\), and the norm terms (lines 99–100). Proof details are standard for the appendix (which was stripped by the parser). Removed per the missing-appendix rule.
- **Strengths about "significant empirical gains over offline methods" and "large-scale evaluation on ImageNet-1k."** These strengths conflict with the verified weakness about unfair comparison (different supervision levels), and per the conflict-resolution rule, the weakness prevails. The empirical results *as presented* are not informative for a fair comparison.

## Novel Insights

None beyond the paper's own contributions. The formalization of an online OOD setting with a non-stationary mixture model is the main novel element. The algorithmic and theoretical contributions (online gradient descent with a regret bound) are standard machinery from online convex optimization applied to a new problem. The feedback assumption is the central tension the paper never resolves.

## Suggestions

1. **Evaluate the unsupervised extension.** The most impactful revision would be to implement and evaluate the promised unsupervised variant of SODA. Without this, the paper remains a best-case analysis under idealized conditions, which does not translate to practical guidance.
2. **Compare SODA against a version of offline methods that process the same streaming data without updating** (i.e., a static model evaluated on the stream). This would at least control for the evaluation protocol.
3. **Be more precise about the scope of the theoretical claims.** Clarify that the regret bound is against a fixed comparator and does not directly address tracking ability in non-stationary environments. Either adopt dynamic regret or temper the claims about non-stationary adaptation.
4. **Characterize when the oracle feedback assumption might hold approximately** (e.g., human-in-the-loop settings, domains with delayed verification) and discuss the degradation with partial/noisy feedback.

## Score and Decision

The paper identifies a meaningful direction — moving OOD detection from static to online settings — and provides a clean formalization. However, the core assumption (oracle feedback at every timestep) undermines both the practicality claims and the empirical comparisons with offline methods. The promised unsupervised extension, which could address this gap, is never implemented. The theoretical analysis is standard OCO repackaged with a misleading claim about non-stationary environments. In its current form, the paper's contribution is an upper-bound analysis whose main empirical result (outperforming offline methods) is a trivial consequence of receiving vastly more supervision rather than evidence of a superior algorithmic approach.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>