Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proposes a mutual information estimator based on the difference-of-entropies (DoE) formulation, using a single block autoregressive normalizing flow (B-NAF) to jointly estimate both \(H(X)\) and \(H(X \mid Y)\). The key idea is to "deactivate" off-diagonal weight blocks in the autoregressive architecture to switch between marginal and conditional density estimation within the same network. Experiments on correlated Gaussian, cubic-transformed Gaussian, and sparse Gaussian data (20–100 dimensions, 32K–128K samples) show lower bias than discriminative methods (MINE, SMILE, InfoNCE, NWJ) and in some settings improvement over separately trained flows.

## Strengths

- **Novel application of B-NAF to joint entropy estimation.** Exploiting the block autoregressive structure to switch between marginal and conditional estimation within a single architecture is a clever design choice. The paper correctly identifies that the B-NAF's block-diagonal weight structure enables a natural "deactivation" operation (lines 197, 216–217, 232) that separate-flow approaches cannot offer, and this is well-motivated.

- **Consistently lower bias than discriminative methods on tested settings.** On correlated Gaussian, cubic Gaussian, and sparse Gaussian benchmarks across 20-, 50-, and 100-d data, the proposed NDoE (B-NAF) estimator shows smaller estimation errors than MINE, SMILE, InfoNCE, NWJ, and DoE with simple parameterizations (Section 4.1, results paragraph). The underestimation pathology of discriminative methods is documented and the proposed method avoids it in the Gaussian case and mitigates it in the cubic case.

- **Joint architecture reduces bias compared to separately trained flows in some regimes.** The paper compares against BNAF (two separate flows for each entropy) and finds that NDoE (B-NAF) exhibits less bias for smaller sample sizes and for cubic cases near zero MI (lines 248–249). This supports the claim that joint estimation helps, though the advantage is not universal (BNAF outperforms on sparse Gaussian for larger MI).

## Weaknesses

### Major

- **Joint estimation procedure is underspecified, undermining the core claim.** The paper's central contribution is a single network that estimates both \(H(X)\) and \(H(X \mid Y)\) via a "deactivation" mechanism. However, the paper does not clearly specify:
  - Whether the two entropy estimates come from independently trained parameter subsets or a single network with shared parameters that are updated under both objectives.
  - How the deactivation mask is applied (hard zero during both forward and backward passes, or during inference only?).
  - Whether training is sequential (train for \(H(X)\) first, then for \(H(X \mid Y)\) keeping diagonal weights fixed) or interleaved.
  
  The text hints at a sequential approach: "one can begin with a network that approximates \(H(X)\) and then optimize the off-diagonal weights to obtain an approximation of \(H(X|Y)\)" (line 216–217). But this is not formalized in the algorithm description. Since the DoE formula \(I = \inf_{q_X} Q(p_X, q_X) - \inf_{q_{X|Y}} Q(p, q_{X|Y})\) requires **separately optimized** infima, it is unclear whether the paper's shared-parameter approach actually yields a valid DoE estimator. Without this clarification, the theoretical grounding (unbiasedness, consistency) of the method is unverifiable.

- **Experimental validation is limited in scope and reporting.** All experiments are on Gaussian-derived distributions (correlated Gaussian, cubic-transformed Gaussian, sparse Gaussian). True non-Gaussian benchmarks from Czyż et al. (2023) beyond the sparse Gaussian variant are not evaluated. The cubic transformation does create non-Gaussian data (the reviewer's claim that it "remains close to Gaussian in structure" is incorrect — applying \(y \to y^3\) to a Gaussian produces a heavily skewed distribution), so this limitation is partial. However, the absence of results on multimodal, discrete, or more complex synthetic benchmarks means the paper's claim of "better performance across different dimensionalities and sample sizes" is only supported within the Gaussian family. Additionally, results are reported only in figures (stripped in the provided text) without tables of mean and standard deviation, and no runtime comparison with baselines is provided.

- **Insufficient algorithmic detail for reproduction.** Algorithm 1 is referenced but its content is not described in sufficient text detail. Key specifics are missing: how the base distribution's parameters are set (fixed standard normal or learned), how the entropy of the base is incorporated into the final MI estimate, how the "deactivation" interacts with the optimizer (single optimizer or separate, how the two loss terms are balanced). These gaps make independent implementation and verification difficult.

### Minor

- **Claims of unbiasedness and consistency are stated without support.** The abstract and introduction claim "an unbiased and consistent mutual information estimator" (lines 4, 18). The DoE framework provides these properties asymptotically if the density models are sufficiently expressive, but the paper provides no analysis of how finite capacity, non-convex optimization, and the joint training procedure affect bias. A convergence plot (error vs. sample size) would substantiate the consistency claim but is absent.

- **No runtime or computational cost comparison.** Normalizing flows require Jacobian determinant computations, which are more expensive per iteration than discriminative methods. The paper gives no wall-clock time or FLOPs comparison, making it difficult for practitioners to assess the trade-off.

### Trivial

- The paper notes that Real NVP "failed to achieve realistic results" on sparse Gaussian data (line 249) but does not analyze why. A brief diagnostic would be helpful.
- The parameter count comparison between the flow and discriminative MLPs is described as "roughly the same" (line 247) without exact counts.

## Nice-to-Haves

- A convergence plot (estimation error vs. sample size) for a fixed dimension would help support the consistency claim.
- A controlled comparison isolating the benefit of joint architecture from the benefit of using normalizing flows: compare NDoE (B-NAF) against two separately trained B-NAF flows (already done as "BNAF") — this exists. The authors should explicitly discuss this comparison and its implications for the joint architecture's advantage.
- A brief analysis of the sign of the MI estimate: is the constraint \(I \ge 0\) (i.e., \(H(X) \ge H(X \mid Y)\)) enforced or checked? How often are violations observed?

## Removed Points

- **"Comparison to natural baselines is missing"**: The paper already includes BNAF (two separate flows) as a baseline (line 245, item 6), which directly tests the benefit of joint vs. separate estimation. The DoE baseline with simple parameterizations is standard from McAllester & Stratos (2018). This criticism is not factually supported.
- **"Proof of Lemma 2.1 contains unjustified steps"**: The proof (lines 87–93) is present and correct. The derivation from \(Q(p,q)\) to \(H(X|Y) + D_{\mathrm{KL}}(p \parallel \tilde{q})\) uses the identity \(Q(p, \tilde{q}) = H(X,Y) + D_{\mathrm{KL}}(p \parallel \tilde{q})\) for the joint density \(\tilde{q}(x,y) = q(x|y)p_Y(y)\), which follows from Equation 2. The steps are compact but valid.
- **"Choice of \(H(X)-H(X\mid Y)\) rather than \(H(Y)-H(Y\mid X)\) is not motivated"**: Either factorization is equally valid; this is not a weakness.
- **"Figures are not visible"**: This is a PDF parser artifact, not an author error. The original submission contains the figures.
- **"Cubic transformation does not change the distribution structure"**: This is incorrect — applying an element-wise cubic transformation to a Gaussian variable produces a heavily skewed, non-Gaussian distribution with substantially different tail behavior. The cubic experiment is a meaningful non-Gaussian test.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the paper itself does not already state or imply.

## Suggestions

1. **Specify the training procedure in full detail.** Clearly describe: (a) whether training is sequential (first diagonal-only for \(H(X)\), then full network for \(H(X \mid Y)\)) or joint; (b) whether the diagonal weights are frozen during the conditional training phase; (c) how the mask is applied (hard zero during forward/backward); (d) the exact form of the loss for each phase; (e) how the base distribution parameters are set and how base entropy is computed.
2. **Provide quantitative tables** with mean and standard deviation of estimation error across 10 runs for each configuration, and a convergence plot (error vs. sample size) for at least one dimension.
3. **Expand experimental validation** to at least one non-Gaussian benchmark from the Czyż et al. (2023) suite that does not derive from a Gaussian base distribution, to demonstrate the method works beyond the Gaussian family.
4. **Add a runtime comparison** (wall-clock time per epoch or total training time) against at least the discriminative baselines.
5. **Tone down the unbiasedness/consistency claims** or provide explicit analysis of the conditions under which they hold for the joint architecture.

## Score and Decision

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**