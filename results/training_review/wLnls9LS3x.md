Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes a new structural model (Assumption A) for Gaussian kernel matrices — that the total sum of entries is O(n) rather than the worst-case O(n²) — and presents the first subquadratic-time algorithm (Õ(d n^{1.89}/ε²)) for approximate kernel matrix-vector multiplication under this assumption that works for arbitrary (possibly signed) input vectors. This removes the non-negativity restriction of the prior state-of-the-art (Backurs et al., 2021). The paper validates the assumption empirically on attention-derived Gaussian kernel matrices from BERT on SQuAD, showing a maximum head-to-tail ratio of 4.6.

## Strengths

1. **Removal of the non-negativity restriction on the input vector, with a stronger error guarantee.** The paper proves an error bound of ‖Kx−y‖₂ ≤ ε‖x‖₂ (Theorem 1.1), which works for any vector x ∈ ℝⁿ. This is a genuine advance over Backurs et al. (2021), whose error guarantee ε‖Kx‖₂ can vanish (forcing exact computation) and whose algorithm requires non-negative x. The paper also shows (Section 1.2) that even for non-negative x, its algorithm can be subquadratic where Backurs et al. would require Ω(n²) time.

2. **A new ℓ₁-based structural assumption with empirical grounding.** Rather than assuming a uniform ℓ∞ bound on tail entries (which Experiment (ii), Section 4, shows does not hold — the n-th and (n+1)-th largest entries have median ratio ≈1), the paper proposes Assumption A: the tail sum (excluding the largest n entries) is at most a constant times the head sum. This is a plausible modeling direction for attention-like matrices. The empirical validation on BERT-derived Gaussian matrices (144 head/layer combinations) finds the maximum ratio is 4.6, supporting the assumption.

3. **First subquadratic algorithm for this problem in the high-dimensional regime for unrestricted vectors.** The paper correctly identifies that prior work (Backurs et al., 2021) has an inherent non-negativity limitation, and Theorem 1.1 genuinely establishes a new capability — subquadratic approximate Gaussian kernel matrix-vector multiplication for arbitrary x under Assumption A. The algorithm combines LSH for heavy-key recovery, sampling for light-key estimation, and KDE for variance control into a coherent pipeline.

4. **Attention-to-Gaussian reduction with improved properties.** Lemma 4.1 provides a reduction from softmax attention matrices to Gaussian kernel matrices that is independent of the input vector x (so the reduction is done once per matrix, not once per matrix-vector pair), improving over Zandieh et al. (2023). This is clearly stated and makes the algorithm applicable to fast attention computation.

## Weaknesses

### Fatal
None.

### Major

1. **Empirical validation of Assumption A is too narrow to support the paper's practical motivation.** The main text's experiments are conducted exclusively on BERT-base with max context length 512 and the SQuAD dataset. The paper repeatedly invokes "modern LLMs" with "context lengths 2048–8192" as the motivating application, but provides no empirical evidence at these scales in the main paper. While the paper mentions additional experiments on RoBERTa and GPT (presumably in the appendix, which was stripped by the parser), the main text should include or at least summarize these results, because the entire algorithmic contribution is conditional on Assumption A holding in practice. A reader cannot evaluate whether the assumption actually holds for the attention matrices of GPT-2, LLaMA, or similar models at realistic sequence lengths.

2. **Main text lacks proof sketches for the key lemmas, making the runtime claims difficult to assess.** Lemmas 3.4 (heavy-keys detection in Õ(d n^{1+2α})) and 3.5 (light-key estimation in Õ(d(n^{2+γ−α} + n^{1.78+γ}/ε²))) are stated without any high-level justification. The parameter choices in Algorithm 2 — the KDE error parameter n^{−0.218}, the threshold μ = ε²/(n log² n (1+ε)^m |B_m|), the construction s_i = t_i − Σ_{j∈S_i} x_j² k² + n^{−0.218}t_i — are presented without explanation of how they interact with the runtime exponent derivation. The final parameter balancing (γ=0.109, α=1/3) that yields the claimed n^{1.89} exponent is mentioned only in the proof of Theorem 1.1 without any rationale for the optimal trade-off. While full proofs may exist in the appendix, the main text should include even brief proof sketches so a reader can follow the argument.

### Minor

1. **The reduction Lemma 4.1 introduces a per-row scaling factor e^{‖q_i‖²} that is not constant across rows, but the paper does not discuss how this affects the applicability of Assumption A.** The paper validates Assumption A on the Gaussian kernel matrix K (after reduction), and the scaling is applied as a post-processing step when converting Kx to Ax. So the criticism does not directly threaten the algorithm's correctness. However, the paper should explicitly discuss why the row-dependent scaling does not affect the validity of the assumption on K itself, and whether the empirical validation (which tests K) is sufficient.

2. **The paper does not analyze or discuss graceful degradation when Assumption A is violated.** The conclusion acknowledges that "no assumption will model such matrices perfectly," but does not provide any theoretical or empirical analysis of how the algorithm's runtime or accuracy behaves when the head-to-tail ratio c grows with n (e.g., c = O(log n) or c = O(n^δ)). Since the runtime exponents depend critically on the assumption, some discussion of robustness would strengthen the paper.

3. **The dependence on the bandwidth parameter σ is not made explicit.** The LSH parameters (Lemma 2.1) and KDE thresholds depend on σ (e.g., r_near = √(2σ²α ln n)), but the paper never states how σ affects the overall runtime or whether it is absorbed into polylogarithmic factors. Since σ is a free parameter of the kernel, this omission makes the algorithm's guarantees incomplete.

4. **The empirical evaluation uses prefix submatrices K[:i,:i] rather than independent sequences of varying lengths.** This means all prefix matrices share the same underlying data distribution, so the scaling behavior observed may not generalize to independently sampled sequences of different lengths. This is a minor methodological caveat that the paper does not discuss.

### Trivial

1. Line 49 cites "Backurs et al. (2017)" where the context (and the rest of the surrounding paragraphs) clearly intends "Backurs et al. (2021)." This is a citation inconsistency.

2. The paper uses the squared kernel k²(·,·) for KDE in Algorithm 2 (step 5) without explicitly noting that k² for a Gaussian kernel with bandwidth σ is a Gaussian with bandwidth σ/√2, which is a standard observation but should be stated for clarity.

## Nice-to-Haves

- An experiment showing the empirical distribution of heavy keys per query across layers/heads would help illustrate whether the average-case bound from Assumption A is reflected in practice.
- A controlled synthetic experiment comparing the empirical runtime and error of the proposed algorithm against Backurs et al. (2021) on non-negative x would demonstrate the practical advantage.
- A brief discussion of how the algorithm degrades when c grows (e.g., subquadratic for c = O(log n), quadratic for c = Ω(n^δ)) would give readers a sense of the algorithm's robustness.

## Removed Points

The following points from the reviews were removed for the reasons indicated:

- **"Validation aggregates across matrices and may hide that some matrices violate it"** — Factually wrong. The paper computes the *maximum* ratio over all prefixes and sentences for each head/layer, so violations would be revealed, not hidden. (from Harsh Critic)
- **"Reference formatting is erratic throughout"** — Pure formatting/style nitpick, removed per hard rules. (from Harsh Critic)
- **"The claim that 'additional experiments … are in the supplementary material' is not verifiable from the main paper"** — Removal per hard rule about questioning existence of appendix/supplementary material; the parser strips these sections. (from Harsh Critic)
- **"The paper does not bound the total preprocessing time across all buckets"** — This is a detail that would appear in the appendix proofs, which were stripped by the parser. (from Harsh Critic)
- **"The contrived example (one row of all ones) may not be realistic"** — The example is a valid theoretical illustration of a runtime exponent gap, not an empirical claim. (from Harsh Critic)
- **"It is not trivial that they extend to squared kernel"** — The squared Gaussian kernel is a Gaussian with bandwidth σ/√2; this is standard. The paper's omission of this note is addressed in Trivial weaknesses above. (from Harsh Critic)
- **Strength Finder's generic strengths about "addressing an important problem"** — Removed as generic/superficial; the remaining strengths are concrete. (from Strength Finder)

## Novel Insights

Across the critiques, the most pointed insight is that the paper's theoretical and empirical contributions are somewhat mismatched in their scope. The algorithm is a sophisticated theoretical construction with carefully balanced runtime exponents (derived from Assumption A), yet the empirical validation — which alone justifies the practical relevance — is limited to one architecture (BERT) at moderate context lengths (≤512). This asymmetry means that a reader cannot evaluate whether the theory's O(n) sum-of-entries assumption actually holds for the kinds of models the paper claims to motivate (GPT-class models at 2048+ token contexts). Additionally, the reviewers collectively highlight that the paper would be substantially stronger if it included proof sketches in the main text, rather than deferring all technical justification to an appendix that readers cannot inspect.

## Suggestions

1. **Strengthen the empirical section.** Include results from at least one modern autoregressive model (e.g., GPT-2, LLaMA) at longer context lengths (1024+) in the main paper. Even a summary table showing that the maximum ratio c stays bounded across models and lengths would significantly increase confidence in Assumption A's generality.

2. **Add proof sketches for Lemmas 3.4 and 3.5.** Each lemma needs 3–5 sentences explaining (a) why the claimed runtime is achievable, (b) how the parameter choices (α, γ, n^{−0.218}, μ, etc.) interact, and (c) why the balancing yields the n^{1.89} exponent. Without this, the main text is opaque.

3. **Make the σ dependence explicit.** State how the LSH parameters and KDE thresholds depend on σ, and whether σ is absorbed into the Õ(·) notation. Even a remark that σ is treated as a fixed constant (or that its effect is polylogarithmic) would clarify the guarantees.

4. **Discuss robustness to assumption violation.** Add a brief paragraph analyzing or conjecturing how the algorithm degrades when the head-to-tail ratio c grows with n, or whether the algorithm remains subquadratic for c = O(log n) or c = O(n^δ).

## Score and Decision

**Originality:** 7/10 — The ℓ₁-based structural assumption is a plausible new direction, and the algorithm is a non-trivial synthesis of LSH, sampling, and KDE techniques. However, the building blocks are all from prior work.

**Importance of research question:** 7/10 — Fast kernel matrix-vector multiplication is a well-motivated problem with clear applications to attention computation and KDE. The removal of the non-negativity restriction is a genuine advance.

**Claims supported:** 5/10 — The theoretical claims are likely sound (subject to the assumption), but the empirical validation of the central assumption is too narrow, and the main text lacks proof sketches to let a reader assess the runtime guarantees.

**Soundness of experiments:** 4/10 — The experiments are correctly conducted on BERT/SQuAD, but they cover only one model family at one scale. The validation methodology (prefix submatrices) has a caveat that is not discussed. The main paper does not present the claimed RoBERTa/GPT experiments.

**Clarity of writing:** 5/10 — The high-level overview is clear, but the algorithmic sections are dense and opaque without proof sketches. The parameter choices appear ad-hoc without explanation.

**Value to the research community:** 6/10 — The algorithm and reduction are potentially useful. The ℓ₁-based assumption is worth further investigation. But the narrow empirical validation limits immediate impact.

The paper has a solid theoretical core and addresses a genuine limitation of prior work. However, the empirical validation of the central assumption is too narrow to convincingly support the claimed practical motivation, and the main text is missing proof sketches that would allow readers to assess the algorithmic claims. These are addressable weaknesses, not fatal flaws.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>