## Summary

This paper proposes "hot PATE," a modification of the PATE framework for generative models where preserving the diversity of teacher response distributions is essential. The core technical contribution is **coordinated ensembles**: using shared randomness (exponential random variables in Gumbel-max sampling) to produce highly correlated samples across teachers. This allows tokens that individually have low per-teacher probability to nevertheless achieve high ensemble frequency, circumventing the diversity-privacy tradeoff that plagues independent sampling. The paper formalizes a definition of diversity-preserving aggregation, proves that coordinated ensembles satisfy it, provides DP aggregation schemes for both homogeneous and heterogeneous ensembles, and demonstrates order-of-magnitude improvements in coverage vs. threshold on a controlled Planet Z task with Llama 3 8B.

## Strengths

- **Formal definition of diversity-preserving aggregation (Definition 1).** The paper introduces a rigorous two-part definition — a *transfer requirement* (tokens with probability ≥ q across ≥ τ teachers must appear in the aggregate at some minimum rate) and a *relevance requirement* (no token's aggregate probability far exceeds its average teacher probability). This cleanly separates the "good case" (low probability across many teachers, safe to transfer) from the "bad case" (high probability in few teachers, identifying). The definition is a genuine conceptual contribution that prior work on diversity in PATE lacked.

- **Lemma 4.1 (diverse transfer guarantee).** The proof shows that for any token j with per-teacher probability ≥ q across m teachers, Pr[frequency ≥ floor(p·m)] ≥ ½·ln(1/p)·q. Crucially, this bound depends on q (per-teacher probability) but *not* on the total number of diverse tokens or the vocabulary size. This is the theoretical basis for the claim that coordinated ensembles avoid the diversity-privacy tradeoff — the probability of achieving high frequency depends on how strongly each teacher supports the token, not on how many other plausible tokens exist.

- **Order-of-magnitude empirical improvements (Section 5, Figures 6–7).** On Llama 3 8B with n=10⁴ teachers and a 128k-token vocabulary, coordinated ensembles achieve 20% vote coverage at threshold T=2000 where independent ensembles require T≤250 (8× worse) and hit 0% at T≥400. The coverage vs. sparsity plots show coordinated ensembles produce an order-of-magnitude more diverse tokens at the same coverage level. These are real quantitative results from actual teacher distributions, not toy simulations.

- **Two DP aggregation schemes with formal diversity-preservation proofs (Section 7, Algorithms 2–3, Lemmas 7.1–7.2).** The paper provides meta-schemes for both homogeneous ensembles (noisy argmax, τ > n/2) and heterogeneous ensembles (weighted sampling, lower τ), with end-to-end proofs connecting the coordinated sampling to the formal definition. Lemma 7.1 establishes β = ln(μ)/2, γ = 2 for the homogeneous case; Lemma 7.2 establishes β = (1/(2μ))·ln(μ), γ = 1 for the heterogeneous case. These are non-trivial end-to-end guarantees.

- **Conceptual distinction between within-teacher and across-teacher diversity (Figure 2, Remarks).** The paper identifies that in in-context learning, diversity is largely "within" teachers (the base model's entropy is present in every teacher's distribution), which is precisely where coordinated ensembles excel. This contrasts with "across" diversity where each teacher has unique data. The discussion of how the two settings affect the choice of τ and how methods could be combined with semantic-clustering approaches (Wu et al.) shows nuanced thinking about scope.

## Weaknesses

### Major

- **The experiments use a threshold T as a proxy for privacy noise but never instantiate a concrete (ε, δ) DP mechanism end-to-end.** The paper evaluates histogram statistics (coverage, sparsity) under frequency thresholds, and treats T as if it corresponds to a privacy noise scale. However, the mapping from T to (ε, δ) depends on the specific noise distribution, composition accounting, and data-dependent analysis that are deferred to Sections (datadependent:sec, heteromethods:sec) that are absent from the available text. The "yield probability" numbers cited (≈10% at σ≈0.3n for k=100) are qualitative illustrations, not measured privacy losses. The central claim — that the method preserves privacy with no penalty from diversity — is supported by theory (Lemma 4.1) and histogram evidence, but the experiments stop short of validating it through an actual DP pipeline with concrete privacy parameters. A reader can believe the coordinated sampling is clever without having evidence that the full DP workflow works as claimed.

### Minor

- **The "no penalty" claim is stated more boldly than what the evidence validates.** The paper claims "no penalty to privacy or efficiency" from diversity. The theoretical basis is sound: Lemma 4.1's bound does not depend on the number of diverse tokens. However, the *probability* of a token achieving high frequency does depend on its per-teacher probability q (the bound is ½·ln(1/p)·q), which can be very small when q is small. The paper acknowledges ≈10% per-sample yield probability for k=100; the claim that this is "no penalty" depends on the data-dependent privacy analysis (in the stripped appendix) showing that failed attempts consume negligible privacy budget. As presented in the main text, the claim is a prediction supported by theory and qualitative reasoning, not a validated result.

- **The Planet Z task, while cleanly controlled, is narrow relative to the paper's motivational claims about open-ended generation.** The task evaluates whether the method can identify correct 3-digit numbers from a known set C (size 20 or 100). The output space is effectively a subset of 900 tokens where ground truth is known. This is closer to multi-label classification than to the "open ended, diverse tasks with multiple valid responses" that the paper motivates (generating synthetic privacy-preserving data records, constructing few-shot prompts). The GPT3.5 experiments that might demonstrate broader applicability are referenced but in the stripped appendix.

- **No evaluation of the downstream student model.** The paper's stated motivation involves "privacy-preserving knowledge transfer to a student model" and "constructing a privacy-preserving student prompts for downstream tasks." While the histogram-level evaluation is appropriate for validating the core mechanism, the paper does not demonstrate that the preserved diversity actually translates to better student performance, better synthetic data quality, or more useful prompts. This limits the practical significance that can be inferred.

- **No comparison with other PATE variants for text generation.** The paper compares coordinated vs. independent ensembles, which is the natural ablation. But there are no comparisons with other approaches such as SeqPATE or the semantic-clustering method of Wu et al., even to discuss qualitatively (e.g., what kinds of outputs each would produce on the same task). The paper argues why these alternatives are limited, but does not benchmark against them.

## Nice-to-Haves

- Run the experiments with a concrete DP mechanism (e.g., Gaussian or Laplace) and report actual (ε, δ) values, to close the gap between the threshold-T experiments and the privacy claims.
- Add one simple student-model task (e.g., train a classifier on privacy-preserving synthetic records from hot PATE vs. cold PATE vs. non-private data) to demonstrate that the preserved diversity matters for downstream utility.
- Evaluate on a more open-ended task (e.g., diverse synthetic text generation) to better match the paper's motivational scope.

## Removed Points

These points were flagged by the reviewers but are removed or demoted per the filtering criteria:

- **"Data-dependent privacy analysis is entirely absent from the available text."** — The parser strips appendix sections from all papers; the analysis exists in the original submission. Removed per hard rule.
- **"No discussion of limitations."** — The paper includes Remarks on failures (Remark 1, allowing ⊥ return) and setting of τ (Remark 2, homogeneous vs. heterogeneous). The implicit limitations discussion is adequate for a methods paper.
- **"Missing related works."** — Removed per hard rule (cannot confirm missing works exist).
- **"Student model training is a structural gap that invalidates the paper."** — The paper's primary contribution is the aggregation method; the student model is downstream. Demoted from fatal to minor; the histogram-level evaluation validates the core mechanism.
- **"No comparison with DP-SGD."** — Comparing PATE with DP-SGD (different paradigms) is outside the paper's stated scope. Removed.
- **Several generic formatting/style criticisms.** — Removed per hard rules on formatting artifacts.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is the tension between the paper's elegant theoretical framing (the formal definition cleanly separates safe-to-transfer from unsafe-to-transfer diversity) and the practical difficulty of validating that the aggregate distribution actually serves downstream tasks. The formal definition is a *necessary condition* for useful privacy-preserving knowledge transfer, but the paper does not establish it as *sufficient*. This gap — between formal diversity preservation and actual student utility — points to an open question in the PATE literature that the hot PATE framework enables but does not resolve.

## Suggestions

1. Implement at least one concrete DP instantiation (e.g., Gaussian-based Confident-GNMax with a standard composition method, or Laplace with the data-dependent approach discussed) and report the (ε, δ) values actually achieved, to replace the threshold-T proxy with real privacy accounting.
2. Add a simple downstream experiment — even a classifier trained on the resulting synthetic records — to demonstrate that the diversity quantified by coverage/sparsity actually matters for task performance.
3. Include a side-by-side comparison with the semantic-clustering method of Wu et al. on the Planet Z task, or at minimum a qualitative discussion of what outputs each method would produce and why coordinated ensembles are preferable for the within-teacher diversity regime.
4. Clarify what "no penalty" means: the paper's claim is that diversity does not worsen the privacy-utility tradeoff (supported by Lemma 4.1), not that the mechanism has zero privacy cost. The abstract and introduction should be more precise.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>