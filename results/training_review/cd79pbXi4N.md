Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces LipsLev, the first method for **deterministic** (non-probabilistic) certification of convolutional text classifiers under bounded Levenshtein distance. The key idea is to use the ERP distance — an edit-distance-like metric on sequences of real vectors — to connect discrete Levenshtein distance to Lipschitz analysis of neural network layers, compute a Lipschitz constant upper bound for the classifier, and train 1-Lipschitz models by normalizing each layer by its Lipschitz constant. This allows single-forward-pass certification for any radius *k*. Experiments on AG-News, SST-2, Fake-News, and IMDB show non-trivial verified accuracy at *k* = 1 and *k* = 2 with large speedups over brute-force and IBP baselines.

## Strengths

- **First deterministic certification method for Levenshtein distance.** The paper correctly identifies a gap: existing NLP verification handles only substitutions (synonym/character) or uses probabilistic randomized smoothing (Huang et al., 2023). LipsLev is the first to provide **deterministic** certificates against insertions, deletions, and replacements jointly (Table 1, Section 1).

- **Certification for *k* > 1, where no other practical method exists.** Table 2 shows LipsLev certifies non-trivial accuracy at both *k* = 1 and *k* = 2 (e.g., 38.80% and 13.93% on AG-News; 75.33% at *k* = 2 on Fake-News). The IBP baseline cannot handle *k* > 1 for Levenshtein distance, and brute-force enumeration is computationally intractable. This is a genuine practical advance.

- **Novel connection between Levenshtein distance and Lipschitz analysis via ERP distance.** The use of ERP distance (Definition 4.1) to bridge discrete text sequences and continuous vector outputs is theoretically motivated and opens the door for Lipschitz-based verification in NLP. Lemma S4 (referenced) establishes that ERP with *p* = ∞ recovers Levenshtein distance for one-hot sequences.

- **Clean, hyperparameter-free 1-Lipschitz training.** The training strategy (Eq. 7) enforces 1-Lipschitzness by dividing each layer's output by its Lipschitz constant, avoiding expensive hyperparameter tuning. Table 3 shows this outperforms standard Lipschitz regularization, which converges to near-constant classifiers or near-zero verified accuracy.

- **Empirical validation across four datasets** with multiple *p*-norms, showing interesting sensitivity. The analysis of sentence length vs. verifiability (Figure 1) provides actionable insight: longer sentences are easier to verify.

## Weaknesses

### Fatal

1. **The central quantity *M*(·) is never defined.** Theorem 4.3, which states the core Lipschitz constant bound, and Corollary 4.4 depend on *M*(**K**^(i)) (for each convolutional layer) and *M*(**E**) (for the embedding layer), yet **neither quantity is defined anywhere in the main text**. *M*(**W**) is finally defined in Section 4.3 (line 190), and *M*(**E**, *P*) is locally defined in Remark 4.5, but *M*(**K**^(i)) and *M*(**E**) appear without formula or explanation. The training procedure (Eq. 7) divides by *M*(**K**^(j)) and *M*(**E**), making the training scheme underspecified. Line 198 states "*M*(**E**) is defined as in Theorem 4.3" — but Theorem 4.3 merely uses the symbol without defining it. **Without this definition, the paper's central theoretical claim is unverifiable, the method is unreproducible, and the training algorithm cannot be implemented.** This is not a missing-appendix issue (which would be filtered); it is an undefined notation in the main body of a result the paper bills as its core contribution. *Severity: fatal — it invalidates evaluation of the paper's core claim.*

### Major

2. **No comparison to the only existing Levenshtein-distance certification method.** The paper cites Huang et al. (2023) for probabilistic Levenshtein certification via randomized smoothing but never compares against it — not in verified accuracy, runtime, or certificate tightness. The experimental evaluation (Table 2) compares LipsLev only against brute-force enumeration and a modified IBP baseline that does not scale (and is known not to). The paper's speed claims ("4 orders of magnitude faster") are against brute-force, which is an exponential method; the relevant practical baseline is the probabilistic single-forward-pass method. Without this comparison, the practical advantage over the state of the art for Levenshtein certification is unestablished.

### Minor

3. **Experiments only test a single convolutional layer.** The theory (Theorem 4.3) supports *l* layers, but all experiments use a single convolutional layer (Section 5.1: "we train models with a single convolutional layer"). While this follows prior work (Huang et al., 2019), the paper's title and abstract claim "certified robustness under bounded Levenshtein distance" without qualification on depth. The paper does not demonstrate that the approach extends to deeper architectures, even though the bound in Theorem 4.3 multiplies per-layer Lipschitz constants. *This limits the empirical scope but does not invalidate the contribution.*

4. **Large gap between verified accuracy and adversarial accuracy.** At *k* = 2, the Charmer adversarial accuracy far exceeds LipsLev's verified accuracy on AG-News (40.13% vs. 13.93%), SST-2, and IMDB. The paper notes this gap but does not analyze its cause — whether the Lipschitz bound is loose, or whether the training sacrifices clean accuracy. On SST-2 at *k* = 1, IBP achieves 28.96% verified accuracy vs. LipsLev's 13.13%, which also warrants discussion.

### Trivial

5. Minor notation inconsistency: In the proof line of Theorem 4.3, the text reads only "Proof" with no content — this is a formatting artifact from the PDF extraction.

## Nice-to-Haves

- Comparing runtime against the randomized smoothing approach of Huang et al. (2023) would provide a more informative practical baseline.
- Analyzing the tightness of the Lipschitz bound (e.g., showing the actual Lipschitz constant vs. the bound or the distribution of *g*_{*y*,*ŷ*} / *G*_{*y*,*ŷ*}) would help readers understand the gap between verified and adversarial accuracy.
- Testing on a 2- or 3-layer convolutional classifier would strengthen claims of generality.

## Removed Points

- **Criticism about missing appendix/proofs**: The parser strips appendix content from all papers. The missing proof text under Theorem 4.3 is almost certainly present in the original appendix. However, the undefined notation *M*(·) in the main body is *not* an appendix issue — it is a main-text definition problem that persists regardless of the appendix. Kept as Fatal #1.
- **Criticism about "4 orders of magnitude faster" being misleading**: The comparison is against brute-force enumeration and IBP, both of which are enumerated approaches with combinatorial cost. While a comparison to randomized smoothing would be more informative, the claim is factually correct for the baselines presented and does not misrepresent those specific comparisons. The omission of Huang et al. (2023) is already captured as Major #2.
- **Complaint about single-conv-layer architecture being "too narrow to support claimed generality"** — weakened to Minor. The paper follows prior work's architecture choice and the conclusion acknowledges limited coverage of modern architectures. The claim is about being the first deterministic method, which holds even for one layer.
- **Strength Finder's "Empirical demonstration of non-trivial verified accuracy"** — kept (genuine, supported by Table 2).
- **Strength Finder's "Orders of magnitude faster"** — kept but contextualized (genuine for the baselines compared).
- **Formatting/style nitpicks** (typos, capitalization, whitespace) — removed as parser artifacts.
- **Request for confidence intervals** — not standard for this setting, moved to nice-to-have implicitly.

## Novel Insights

The review reveals that the paper's most critical flaw is not experimental but theoretical/presentational: the central quantity *M*(·) is never defined. The reviewers correctly identified this from reading the main text independently. The fact that *M*(**K**) and *M*(**E**) are used in every major claim (Theorem 4.3, Corollary 4.4, Eq. 7) yet lack formulas means the paper is effectively incomplete as submitted. The second-order issue — omitting the Huang et al. (2023) baseline — is serious but addressable. The single-layer architecture limitation is real but consistent with prior work in this specific sub-area. The paper's core idea (ERP distance for Lipschitz analysis of text classifiers) is genuinely novel and the experimental results at *k* = 2 are impressive, but the theoretical presentation must be completed before the contribution can be assessed.

## Suggestions

1. **Define *M*(**K**) and *M*(**E**) explicitly** with formulas in the main text. Clearly state their dependence on the norm *p* and whether they represent spectral norms, maximum singular values, or operator norms induced by the ERP distance.
2. **Add a comparison to Huang et al. (2023)** (randomized smoothing for Levenshtein distance) on at least one dataset, reporting both certified accuracy and runtime.
3. **Add an experiment with 2–3 convolutional layers** to demonstrate that the bound scales beyond a single layer.
4. **Discuss the verified vs. adversarial accuracy gap.** Show the distribution of the margin-to-Lipschitz ratio to indicate bound tightness.

## Score and Decision

The paper introduces a novel and principled approach to a real problem. However, the failure to define *M*(·) — the central quantity in every theoretical claim and the training procedure — makes the paper unreproducible and the core contribution unverifiable in its current form. Combined with the omission of the relevant baseline (Huang et al., 2023), the paper requires major revision before it can be assessed for acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>