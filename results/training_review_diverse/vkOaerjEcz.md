Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

---

## Summary

This paper introduces MTMC (Maximum Token Manifold Capacity), a simple auxiliary loss for Generalized Category Discovery (GCD) that maximizes the nuclear norm of the class-token matrix from unlabeled samples in a batch. The core idea is to prevent dimensional collapse and promote richer intra-class representations, thereby improving clustering accuracy and category-number estimation. MTMC is designed as a lightweight plug-in for existing GCD methods (SimGCD, CMS) and is evaluated on six benchmarks, showing consistent improvements — most notably +4.7% on ImageNet100 with SimGCD and ~4% on CUB/Stanford Cars with CMS.

## Strengths

- **Consistent empirical improvements across multiple GCD backbones and benchmarks.** MTMC boosts SimGCD by 4.7% on ImageNet100 (All column) and CMS by ~4% on CUB and Stanford Cars without `K`. Improvements are consistent across coarse-grained and fine-grained datasets, though magnitude varies. [Verified: Table 1 and Section 4.2, lines 152.]

- **Exceptionally simple and practical contribution.** The core loss is implementable in three lines of code (Section 3.2 code snippet) and integrates with any existing GCD framework via a single scalar hyperparameter λ. [Verified: code snippet in Section 3.2, line 103-105.]

- **Empirical evidence that MTMC counteracts dimensional collapse.** Figures 2, 4, and 5 show that MTMC increases von Neumann entropy, reduces the Frobenius norm of the autocorrelation matrix, and produces more uniform eigenvalue distributions compared to baselines. These measurements directly support the claim that MTMC produces richer, less-collapsed representations. [Verified: Section 4.3, lines 168-173, and Figures 2, 4, 5.]

- **Accurate category-number estimation.** CMS+MTMC achieves 100% correct `K` estimation on ImageNet100 and sharply reduces error rates on other datasets (Table 2). This demonstrates a practical benefit beyond clustering accuracy. [Verified: Table 2, Section 4.2, line 154.]

- **Hyperparameter robustness.** The method is stable across a range of λ values and feature dimensionalities D (Figure 3), making it easy to use without extensive tuning. [Verified: Section 4.2, lines 159.]

## Weaknesses

### Major

- **The theoretical link between the batch-level nuclear norm loss and per-sample manifold capacity is not adequately established.** The paper defines CTME = ||[cls]||_* for a single sample (Equation 3) but the actual loss L_MTMC = –||[cls]^u||_* operates on a *batch-level matrix* of class tokens from *different samples* (Equation 4). The paper invokes the MMCR literature (which operates on sample views) and Theorem 1 (which relates rank to von Neumann entropy of an autocorrelation matrix), but never bridges the gap between (a) maximizing the sum of singular values of a batch×dim matrix and (b) the claimed per-sample or intra-class benefits. The nuclear norm is not the rank — maximizing the sum of singular values does not necessarily produce more uniform eigenvalue distributions without additional constraints on the singular vector structure. The paper's claim (line 4, abstract) that MTMC's "efficacy is fundamentally rooted in its ability to leverage the nuclear norm... as a quantitative measure of manifold capacity" is asserted rather than derived or rigorously argued. This does not invalidate the empirical results, but the theoretical framing is overclaimed relative to what is actually shown. [Verified: compare Eqs 3-4 with Theorem 1 and accompanying discussion; the chain from L_MTMC → uniform eigenvalues → higher entropy is empirically observed (Figures 2, 4, 5) but not theoretically justified.]

### Minor

- **No error bars or statistical significance tests are reported.** Given that several gains are small (CIFAR-100 +0.6%, Herbarium19 +0.4%), single-run results make it impossible to assess whether these improvements are systematic or noise. While this is common practice in the GCD literature, the paper would be strengthened by reporting results over multiple seeds with standard deviations. [Verified: No matches for "standard deviat", "random seed", or "multiple run".]

- **The decision to apply MTMC only to unlabeled samples is not ablated.** The paper states that labeled samples are excluded because supervised signals already shape their manifolds (line 83). This is a reasonable design choice, but it is never tested — the reader cannot tell whether applying MTMC to all samples would work equally well or better. An ablation comparing "MTMC on unlabeled only" vs. "MTMC on all samples" would clarify whether the restriction is necessary or a missed opportunity. [Verified: The ablation study (line 159) covers only λ and D; no ablation of this design choice exists.]

- **The hyperparameter sensitivity analysis (Figure 3) does not specify which dataset is used.** This makes it difficult to assess how general the claimed stability is across different data distributions. [Verified: Figure 3 caption (line 157) — no dataset specified.]

### Trivial

- None that are paper-specific and not parser artifacts.

## Nice-to-Haves

- Compare K-estimation performance against other GCD methods that can estimate category count (e.g., SimGCD's entropy-based estimation) rather than only CMS vs. CMS+MTMC. The current comparison is valid within scope (CMS does not require hyperparameters for K estimation), but a broader comparison would strengthen the claim.
- Discuss why a nuclear-norm-based loss is preferable to covariance regularization approaches (e.g., Zbontar et al., Cogswell et al.) cited in related work. The paper references these methods but does not situate MTMC relative to them conceptually.
- Include a brief discussion of what happens when the unlabeled batch size is smaller than the feature dimension D — the nuclear norm's behavior and gradient properties depend on the rank of the batch matrix.

## Removed Points

These points were removed per the filtering rules; they are listed here with brief justification in case they are useful:

1. **"Notation inconsistency and garbled equations (e.g., '3ttention')"** — This is a PDF parser artifact, not an author error. The original submission does not have this issue. [Rule: pure formatting/parser artifacts.]
2. **"Equation 2 omits multi-head nature of attention"** — Simplified exposition is standard; not a substantive weakness. [Rule: nitpick about implementation detail.]
3. **"The unlabeled-only justification is circular reasoning"** — The paper's justification (supervised signals already shape labeled-sample manifolds) is a reasonable design choice, not circular. The *absence of an ablation* is a separate valid point kept above, but the accusation of circularity is unwarranted. [Rule: strawman weakness.]
4. **"Missing comparison with SimGCD for K estimation"** — The paper specifically uses CMS because CMS estimates K without additional hyperparameters. Criticizing the absence of a comparison with a method that uses a different mechanism is scope creep. [Rule: evaluating against wrong class of expectations / scope creep.]
5. **"Related work on uniform eigenvalue distributions"** — The paper does cite whitening/decorrelation methods (Zbontar et al., Cogswell et al.) in Section 5.2 (line 192). The reviewer's claim that the paper does not compare "even conceptually" is inaccurate. [Rule: factually wrong.]

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's theoretical framing and its actual theoretical content, but this observation is implicit in the paper's structure — the authors claim theoretical analysis but deliver only Theorem 1 (a known bound) plus empirical eigenvalue plots. The reviewers correctly identify this mismatch but do not contribute a novel resolution.

## Suggestions

1. **Strengthen the theoretical justification** by either (a) deriving a bound that connects the nuclear norm of the batch class-token matrix to properties of per-sample representations, or (b) explicitly reframing the contribution as a well-motivated empirical method rather than a theoretically grounded one.
2. **Add multi-seed experiments** with standard deviations for the main results (Table 1), especially for datasets where gains are modest (CIFAR-100, Herbarium19).
3. **Ablate the unlabeled-only restriction** — compare "MTMC on unlabeled samples only" vs. "MTMC on all samples" to determine whether the restriction is necessary.
4. **Specify the dataset used in Figure 3** (hyperparameter sensitivity) in the caption.
5. **Add a brief discussion** of what happens when batch_size < D, since the nuclear norm's properties change when the matrix is not full-rank.

## Score and Decision

**Originality:** The nuclear-norm-based loss for intra-class representation in GCD is novel, though the connection to MMCR is clearly acknowledged.  
**Importance of research question:** GCD is a practically relevant problem, and improving intra-class representation completeness addresses a genuine limitation of existing methods.  
**Claims support:** The empirical claims of improved accuracy and K-estimation are supported by the experiments. The theoretical claim of "maximum manifold capacity" is only partially supported — the empirical evidence is there (eigenvalue distributions, entropy), but the theoretical derivation is incomplete.  
**Soundness:** The experimental setup follows standard GCD protocols. The main soundness concern is the gap between claimed theory and actual results.  
**Clarity:** The paper is understandable despite parser artifacts; Sections 3.1-3.2 are reasonably clear about the method.  
**Value to community:** The method's simplicity and consistent improvements make it practically useful. However, the overclaimed theory may mislead readers about what is established vs. conjectured.

The method is simple, empirically effective, and easy to adopt. However, the paper overstates its theoretical contribution — what is presented as a "theoretical analysis" is largely a known theorem (rank vs. entropy) plus empirical observations, without actually deriving why maximizing the nuclear norm of the batch class-token matrix produces the claimed benefits. This gap between framing and substance is the paper's central weakness. The empirical contribution is real but modest in scale (most gains are 1-4%, with several near-zero gains on challenging datasets), and the lack of error bars makes it hard to fully trust the small improvements.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>