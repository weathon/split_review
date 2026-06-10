## Summary

This paper proposes VQ-TR, a Transformer architecture for probabilistic time series forecasting that incorporates Vector Quantization (VQ) into the encoder's attention mechanism. By quantizing C query vectors down to J ≪ C codebook vectors before cross-attending to keys/values, the method achieves O(CJ + LJ²) per-encoder-layer complexity instead of O(C²). The paper also claims to provide the first systematic comparison of transformer-based methods for probabilistic (as opposed to point) forecasting across 6 datasets with 7 metrics. Results indicate VQ-TR is competitive or best on most metrics for 5/6 datasets while using substantially less memory than comparable efficient-transformer baselines.

---

## Strengths

- **Novel and architecturally sound integration of VQ into transformer attention for time series.** The core design — quantizing query vectors, cross-attending codebook vectors to keys/values, then gathering back to the original sequence dimension (lines 112–128) — is clearly described and non-trivially extends the Perceiver-style latent transformer paradigm to the time-series forecasting setting. The complexity analysis (O(CJ + LJ²) vs O(C²)) is correctly reasoned.

- **Theoretical motivation connecting attention error bounds to VQ's K-means objective.** Theorem 3.1 (lines 96–102) bounds the attention output error under query-vector perturbations, and the derivation (lines 104–110) connects minimizing that bound to a weighted K-means objective that VQ naturally optimizes. While the connection is conceptual rather than fully rigorous, it provides genuine motivation beyond a purely heuristic application of VQ.

- **Clear architectural differentiation from closest related methods.** Section 5 (lines 233–237) correctly identifies why Perceiver-AR (decoder-only, requiring P passes of cross-attention for probabilistic forecasting) and VQ-AR (applies VQ after an RNN, not within attention) are architecturally distinct from VQ-TR, and why those differences matter for the probabilistic forecasting use case.

- **Joint end-to-end training of VQ and forecasting losses** (line 144). Unlike the common two-stage paradigm of unsupervised VQ pretraining followed by downstream fine-tuning (e.g., DALL·E), VQ-TR jointly minimizes the negative log-likelihood together with VQ latent and commitment losses, which is a sensible design choice for this setting.

---

## Weaknesses

### Major

- **Critical experimental details are entirely absent from the paper.** The paper defines symbols C (context window length), P (prediction horizon), J (codebook size), N/M (encoder/decoder layers), F (embedding dimension), L (latent self-attention layers), and the commitment loss weight β, but never reports their numerical values for any dataset or experiment. No learning rate, optimizer, batch size, number of training steps/epochs, or number of random seeds is provided anywhere in the visible text. This level of underspecification makes it impossible to reproduce the results, evaluate the fairness of comparisons, or assess whether hyperparameter differences (rather than architectural ones) drive the reported outcomes. For a paper making SOTA-adjacent empirical claims, this is a fundamental omission that prevents the experimental section from meeting the reproducibility bar of a top venue.

- **No statistical significance or variance reporting.** All results (Table 1) are reported as single numbers per metric per dataset with no standard deviations, confidence intervals, or indication of how many independent runs were performed. With 6 datasets, ~7 metrics, and 11+ baselines, the central claim that VQ-TR "performs best on almost all metrics on 5 out of 6 datasets" cannot be evaluated for statistical reliability. Some proportion of these wins could arise from random variation, and without variance estimates the reader has no way to assess this.

- **The ablation study is effectively absent.** The paper claims to "provide some positive evidence for this in our vector quantization ablation" (line 215) and then devotes three sentences to codebook-size sensitivity (line 219), reporting qualitative observations (no quantitative table or figure). There is no comparison of VQ-TR against: (a) the same architecture without VQ (i.e., standard cross-attention over C tokens), (b) alternative compression methods (random projections, pooling, linear projections), or (c) different codebook sizes shown systematically. The claim that VQ provides "a natural regularizing effect" (line 18) is therefore an untested hypothesis. Given that the paper's dual thesis is that VQ yields both *efficiency and regularization* benefits, the regularization claim is entirely unsupported.

### Minor

- **The theoretical motivation is conceptually suggestive but not rigorous.** Theorem 3.1 is stated without proof, and the derivation connecting it to VQ's K-means objective (lines 104–110) involves a chain of approximations (Jensen's inequality, expectation over keys to obtain Σ_k + μ_kμ_k^T, appeal to properties of optimal VQ codes) that is presented as a sketch rather than a formal argument. The paper does not empirically verify whether the δ_t bound from Theorem 3.1 is actually satisfied by VQ-quantized queries during training. The theorem serves as useful motivation, not as a rigorous guarantee that VQ minimizes attention error — a distinction the paper does not clearly draw.

- **Efficiency evaluation is limited to a single dataset.** Figure 2 compares training time and memory on Traffic only, with a single context length. The efficiency benefits depend on the ratio C/J, which varies across datasets. Results on one dataset do not establish the generality of the efficiency claims, and the paper does not report whether the efficiency comparison controlled for comparable forecast quality across methods (a model using less memory but producing worse forecasts is not an apples-to-apples comparison).

- **The "systematic benchmark" contribution is overclaimed relative to what is actually presented.** The paper lists 6 non-transformer baselines (Section 4.3) but Table 1 only compares VQ-TR against transformer-based methods (line 215 states this directly; the table caption confirms). The non-transformer baselines are listed but not empirically compared. While comparing 11 transformer methods on 6 datasets with 7 metrics is legitimate and valuable work, the framing implies a broader comparison than is delivered, and the experimental underspecification prevents the results from functioning as a reproducible benchmark that others could build on.

### Trivial

- "Elecricity" (line 181) appears to be a typo for "Electricity."
- The reference footnotes 3–6 in the datasets section appear as empty superscripts in the parsed text.

---

## Nice-to-Haves

- A properly controlled ablation comparing VQ-TR against (a) the same architecture without any compression and (b) the same architecture with an alternative compression method (e.g., learned linear projection to J dimensions, or average pooling to J tokens) would isolate whether the VQ mechanism itself drives the gains, or whether reduced dimensionality alone is responsible.
- Reporting standard deviations over at least 3–5 seeds for the primary metrics would substantially strengthen the empirical claims.
- Extending the efficiency analysis to multiple datasets with different C/J ratios would better establish the generality of the memory/compute advantage.
- A brief table reporting C, P, J, N, M, and the emission head distribution used per dataset would resolve the reproducibility issue.

---

## Removed Points

- **"Theorem 3.1... errors in the denominator of the softmax are not accounted for"** — This is a speculative mathematical claim about a theorem stated without proof. The bound is a standard softmax perturbation analysis; whether the specific inequality chain works as claimed is unverifiable without the proof (likely deferred to the now-stripped appendix). Removed as unverifiable speculation.

- **"Garbled equations in the derivation"** — The equations (lines 104–108) contain OCR artifacts from the parsing process, not errors in the original submission. Removed per parser-artifact rule.

- **"Section-by-section notes"** and **"Missing Parts and Places to Improve"** — Many of these are general observations or suggestions rather than specific, verified weaknesses. Relevant concrete points (e.g., unclear decoder conditioning, missing codebook sensitivity figure) are subsumed into weaknesses above.

- **Strength Finder points removed:** The claim about "first systematic probabilistic-forecasting benchmark" is retained but weakened (see Minor weaknesses). Generic or overstated framing was trimmed; concrete strengths (theoretical motivation, architectural differentiation, joint training) are kept.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Restructure the experiments section** to include a dedicated table reporting all hyperparameters (C, P, J, N, M, F, L, β, optimizer, learning rate, batch size, epochs, number of seeds) for every dataset before presenting results.
2. **Add a proper ablation** comparing VQ-TR against a version that replaces VQ with a learned linear projection to J dimensions (same reduction ratio, no discretization), plus a version with no compression at all. Report the results in a dedicated table.
3. **Report standard deviations** over at least 3 independent runs for all main metrics, and flag whether the "best on 5/6 datasets" claim holds under statistical testing.
4. **Extend the efficiency benchmark** to at least 2–3 datasets with different (C, J) ratios, and include a column showing each method's metric scores in the efficiency comparison so the trade-off between quality and efficiency is transparent.
5. **Clarify the scope** of the benchmark contribution upfront: state explicitly that the comparison covers transformer-based methods (the non-transformer baselines are listed for context but not quantitatively compared in this work).

---

## Score and Decision

The core idea — integrating VQ into the attention mechanism for time series — is novel, the architecture is clearly described, and the theoretical motivation (Theorem 3.1 → weighted K-means) is a genuine contribution beyond purely heuristic applications. However, the experimental evaluation as presented is critically incomplete for a top venue: no implementation details are reported, no variance or statistical significance is provided, the ablation study that would validate the central regularization claim is absent, and the efficiency analysis covers only one dataset. These omissions prevent reproducibility and make it impossible to assess the reliability of the core empirical claims. The contribution is real but insufficiently validated.

**Score: 4.5 — Decision: Reject**

The paper would benefit substantially from adding a full experimental specification, proper ablations, and statistical significance reporting. With those additions it could be a strong submission.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>