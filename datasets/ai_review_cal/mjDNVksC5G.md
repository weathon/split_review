- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 3, 5
Now I have all the information needed. Here is the final consolidated review.

---

## Summary

This paper theoretically and empirically investigates whether transformers can learn to perform PCA through a supervised pre-training procedure. Theoretically, it constructs a transformer architecture whose forward pass approximates the power method for computing top-\(k\) eigenvectors, and provides generalization bounds (Proposition 1 gives an \(n^{-1/2}\) rate; the abstract additionally claims an \(n^{-1/5}\) rate). Empirically, it trains a GPT-2-style ReLU-attention transformer on synthetic Gaussian data to predict eigenvectors and eigenvalues, and tests transfer to MNIST and Fashion-MNIST. The paper identifies a genuine connection between the iterative structure of the power method and the layered structure of transformers, but the theoretical construction and empirical evaluation are only loosely coupled.

## Strengths

1. **Explicit approximation bounds linking transformers to the power method.**  
   Theorem 3.1 constructs a transformer (with \(L = 2\tau + 4k + 1\) layers) whose forward pass provably approximates \(\tau\) iterations of the power method for extracting top-\(k\) eigenvectors. The error decomposes into an approximation error (from replacing matrix multiplication with attention/MLP layers) and a finite-iteration error, which is a non-trivial theoretical contribution.

2. **Generalization bounds for the supervised pre-training setup.**  
   Proposition 1 provides a finite-sample generalization bound for the empirical risk minimizer with a \(\sqrt{(\dots)/n}\) rate, using the Rademacher complexity of the transformer class. Corollary 3.1.1 combines this with the approximation error to give an end-to-end bound. These results go beyond pure universal approximation and address learning from finite data.

3. **Empirical validation across synthetic and real data with controlled ablations.**  
   The experiments systematically vary dimension \(D\), number of layers \(L\), and number of predicted eigenvectors \(k\). Results show relative MSE below 2% for eigenvalues and cosine similarity near 1 for eigenvectors at small \(D\). The transfer experiments from synthetic Gaussian training to MNIST/Fashion-MNIST (Figure 4) demonstrate that the learned mapping generalizes beyond the training distribution.

4. **Probabilistic guarantee for the initialization condition.**  
   Lemma 3.1 shows that the alignment condition required by Theorem 3.1 (\(\tilde{p}_i^\top v_i \ge \delta\)) holds with high probability when initial vectors are sampled from an isotropic Gaussian, making the existence theorem's assumptions realizable.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-experiment disconnect limits the paper's explanatory power.**  
   The theoretical construction (Theorem 3.1) requires: (a) a specialized context matrix \(P\) containing identity blocks, random initial vectors, and zero placeholders; (b) up to \(M \le \lambda_1^d C/\epsilon^2\) attention heads (exponential in \(d\)). The experiments use a standard GPT-2 architecture, *without* the \(P\) matrix, and with only 2–8 heads. The paper acknowledges (Section 5) that \(P\) is "verified removable from our empirical results" and conjectured unnecessary in theory, but this acknowledgment does not bridge the gap. The paper presents theory and experiments as mutually reinforcing, but the theory constructs a specific, high-complexity model while the experiments train a completely different model via SGD. There is no evidence (e.g., probing intermediate representations, comparing the trained model's activations to power-method iterates) that the trained model implements anything resembling the constructed algorithm. This disconnect means the theory does not *explain* the empirical results, and the empirical results do not *validate* the theoretical construction.

2. **No baselines against other architectures.**  
   The experiments train only a transformer. Without comparisons to MLPs of comparable parameter count, linear models, or the actual power method, it is impossible to assess whether the transformer architecture is especially suited to this task or whether any sufficiently expressive model would reach similar accuracy. The paper's core question ("Can Transformers Perform PCA?") is implicitly comparative, yet no comparison is made.

### Minor

3. **Supervised regression vs. unsupervised discovery.**  
   The paper trains on ground-truth eigenvectors as labels (Eq. 1). The model learns to *regress* onto known eigenvectors, not to *discover* low-dimensional structure without supervision. The paper is transparent about this setup (Section 2.3: "The standard PCA problem is unsupervised... we need to perform supervised pre-training"), but the title and framing ("transformers can perform PCA") imply a capability that is narrower than what is actually demonstrated — the model performs eigenvector regression given supervised targets.

4. **Abstract claims an \(n^{-1/5}\) rate not derived in the main text.**  
   The abstract states "the generalization error of transformers decays by \(n^{-1/5}\) in \(L_2\)." Proposition 1 in the main text gives an explicit \(n^{-1/2}\) bound; Corollary 3.1.1 adds complexity without obvious simplification to \(n^{-1/5}\). While the derivation may appear in the appendix (which was stripped by the parser), the main text does not even sketch how this rate emerges from balancing approximation and estimation errors. The future work section (line 240) mentions certifying whether the rate is sharp, which suggests the rate is obtained somewhere, but the main text should be self-contained on a headline quantitative claim.

5. **Exponential dependence on dimension in the theoretical construction is understated.**  
   Theorem 3.1 requires \(M \le \lambda_1^d C/\epsilon^2\) heads, which is exponential in dimension \(d\) unless \(\lambda_1\) is very small. Remark 3 merely notes that "dimension significantly affects the approximation properties," which understates the severity: for \(d=100\) with \(\lambda_1 \ge 1\), the bound is vacuous. The experiments use \(d\) up to 40 with only 2–8 heads, operating in a regime far from what the theory requires.

6. **Eigenvector sign ambiguity not discussed.**  
   Eigenvectors are defined only up to sign. The cosine-similarity loss penalizes sign flips (predicting \(-\mathbf{v}_1\) gives \(\cos = -1\), loss = 2). Since `numpy.linalg.eigh` returns eigenvectors with arbitrary sign, the training labels may have inconsistent signs across examples. The paper does not address how this is handled or whether it affects the reported cosine similarities.

7. **ERM vs. SGD gap acknowledged but unaddressed.**  
   The theory guarantees performance of the empirical risk minimizer, but experiments use SGD. The paper notes this limitation (Section 5) but does not attempt to measure the gap (e.g., by comparing against a model explicitly trained to ERM).

### Trivial
None.

## Nice-to-Haves

- An ablation comparing ReLU vs. softmax attention on the PCA task would strengthen the connection to the theory (which assumes ReLU).
- A systematic exploration of how the number of attention heads affects performance would help contextualize the exponential head-count bound.
- Reporting absolute error (not just relative MSE) for eigenvalue prediction would clarify whether small eigenvalues are predicted accurately in absolute terms.

## Removed Points

The following points from the reviewers are removed with brief justification:

- **"The saturation of prediction improvement with layers is not discussed."** — Removed because the paper *does* discuss this: Section 4.2 notes "the rate of improvement diminishes as the number of layers becomes larger" and attributes it to the bias-variance tradeoff (Figure 3, middle).
- **"Transfer to MNIST could simply indicate smoothness of the function space."** — Removed as speculative; the reviewer provides no evidence that this is the case rather than the transformer learning the PCA mapping.
- **"Missing related works."** — Removed per instruction: the reviewer cannot verify missing citations without external knowledge.
- **"The Lipschitz bound may not transfer to practical settings."** — Removed as a generic theory-practice concern without a specific, verifiable flaw in the paper.
- **"The abstract's \(n^{-1/5}\) claim is unsupported."** — Downgraded from a fatal/major discrepancy to Minor (point 4 above) because the derivation may reside in the appendix, which is stripped by the parser. The remaining concern is about main-text presentation, not a missing proof.

## Novel Insights

The harsh critic's observation that the theoretical construction (requiring \(P\) matrix, exponential heads) and the empirical evaluation (standard GPT-2, no \(P\), few heads) are *structurally disconnected* — not merely partially aligned — is a genuinely insightful frame. The paper treats these as complementary, but they are better understood as two separate contributions: an existence proof that *some* transformer can approximate PCA, and an empirical demonstration that *training* a transformer via SGD on supervised labels yields PCA-like predictions. Whether the trained model actually implements the constructed algorithm is an open question the paper does not address. This disconnect is the most significant limitation and should be the primary focus of any revision.

## Suggestions

1. **Add baselines.** At minimum, compare against an MLP with similar parameter count and the actual power method on the same supervised regression task. This would clarify whether the transformer's depth or attention mechanism is essential.
2. **Bridge theory and experiments.** Either (a) implement the constructed architecture (with \(P\) matrix) and verify the theoretical predictions, or (b) adapt the theory to cover the standard architecture used in experiments (remove reliance on \(P\) and reduce head-count dependence). Alternatively, probe the trained model's intermediate representations to test whether they resemble power-method iterates.
3. **Derive the \(n^{-1/5}\) rate in the main text or correct the abstract.** Show the trade-off optimization between approximation error (in \(\epsilon, \epsilon_0\)) and estimation error (\(\sqrt{1/n}\)) that yields the claimed rate.
4. **Address the sign ambiguity.** Either describe how the training procedure handles arbitrary eigenvector signs (e.g., flipping to a canonical sign), or modify the loss/metric to be sign-invariant (e.g., using absolute cosine similarity).
5. **Acknowledge the exponential head-count limitation more prominently** and discuss whether the bound is loose or whether alternative constructions could avoid this dependence.
