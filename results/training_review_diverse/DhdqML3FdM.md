I've now verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper provides a theoretical and empirical investigation into limitations of Structured State Space Models (SSMs) for function composition and complex reasoning. The authors prove three main theoretical results: (1) one-layer SSMs require state size scaling with domain size to solve function composition (Theorem 1), (2) SSMs need polynomially many Chain-of-Thought steps for iterated composition (Theorem thm-CoT), and (3) multi-layer SSMs are in the complexity class **L** (logarithmic space), implying they cannot solve **NL**-complete problems unless **L** = **NL** (Theorems thm:ssm_log_space, thm-LogSpace). The paper claims empirical validation on multiplication, dynamic programming, and logic puzzles, but the experiments section contains no actual results.

## Strengths

- **First formal lower bound for one-layer SSMs on function composition (Theorem 1):** The paper extends the communication-complexity reduction of Peng et al. (2024) from Transformers to SSMs, proving that a one-layer SSM needs state size satisfying (d²+d)p = Ω(n log n) to solve function composition with high probability. This is a genuine theoretical contribution that identifies a concrete architectural bottleneck.

- **CoT step lower bound for SSMs (Theorem thm-CoT):** Through a reduction from pointer chasing, the paper shows SSMs require Ω(√(n log n)/(dp)) CoT steps for iterated composition. This result extends the known Transformer CoT bound to SSMs and demonstrates that CoT prompting cannot circumvent the fundamental communication bottleneck.

- **Unified complexity-theoretic framing:** The paper ties together results on SSMs, Transformers, and the complexity class **TC⁰** ⊆ **L**, reinforcing the observation that these sequence-modeling architectures share inherent computational limitations that explain their struggles with multi-step reasoning tasks.

## Weaknesses

### Major

- **Experiments section contains no results.** Section 8 (Experiments) describes the evaluation setup (GPT-4 API, Jamba v1, 500 samples, three runs) but presents zero accuracy numbers, tables, figures, or analyses. The abstract and introduction claim specific values (GPT-4 27%, Jamba 17% on 4×3-digit multiplication) and the conclusion states "our empirical evaluations confirm these findings," yet no empirical evidence is provided in the body. There are no \begin{table}, \begin{figure}, \includegraphics, or \caption commands anywhere in the extracted text. A paper that claims "theoretical and empirical investigation" and asserts "our experiments corroborate these theoretical findings" cannot be evaluated without presenting the experimental results. This is the single most significant problem with the submission.

- **Overclaimed rhetoric in the conclusion.** The conclusion (line 295) states that the results show "overcoming these limitations would require exponentially large hidden dimensions or computational precision." However, Theorem 1 gives a *polynomial* bound: (d²+d)p must be at least roughly n log n, which is polynomial in n, not exponential. The contrast between the polynomial bound proved and the "exponential" language in the conclusion misrepresents the paper's own contribution and sets unrealistic expectations.

### Minor

- **Algebraic slip in Theorem 1 proof (line 116).** The proof defines q as the probability the SSM answers *correctly*, then states "By Lemma 1, it follows that q ≤ R/(3n log n)." Lemma 1 gives a lower bound on *error* probability (≥ R/(3n log n)). The correct conclusion should be 1 − q ≥ R/(3n log n), i.e., q ≤ 1 − R/(3n log n). The theorem statement itself is correctly formulated in terms of error probability. This is a proof-writing error, not a fatal flaw, but it needs correction.

- **CoT lower bound proof (Theorem thm-CoT) is under-specified.** The reduction from pointer chasing to iterated composition with CoT is sketched in a few paragraphs. Key steps — how Alice and Bob can independently compute their respective hidden states using only local data, how the round structure maps to CoT steps, and the derivation of k = (1/100)√(n/log n) + 1 — receive minimal justification. While the proof follows the template of Peng et al. (2024), the presentation is too terse for a self-contained verification.

- **Log-space theorem (Theorem thm:ssm_log_space) is a known result with a sketchy proof.** The paper acknowledges that Merrill et al. (2024) already established SSMs are in **TC⁰** ⊆ **L**, so the theorem's classification is not new. The self-contained proof offered for multi-layer SSMs hand-waves the critical issue: computing layer ℓ+1 requires the outputs of layer ℓ for all N time steps, but the proof asserts "we can recompute any needed values when required" without explaining how this avoids storing O(N) values or why the total space remains O(L log N) rather than O(N).

- **Precision definition ambiguity.** The paper uses "computational precision p" as a central parameter in all theorems but only briefly defines it as "the number of bits used in each computation." It is unclear whether p is per scalar, per matrix element, or per arithmetic operation, which affects the interpretation of the bounds.

### Trivial

None.

## Nice-to-Haves

- The paper could strengthen its case by including a table of the claimed empirical results (GPT-4, Jamba on composition tasks, multiplication, DP, Einstein's puzzle) to substantiate the claims made in the abstract and conclusion.

- An ablation varying the number of SSM layers on a fixed composition task would test the conjecture that constant-depth SSMs cannot overcome one-layer limitations.

- A more precise account of how token embeddings encode discrete function values in the reduction would bridge the gap between the continuous SSM formulation and the discrete function composition setting.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The experiments section contains no actual results" — moved from Fatal to Major because the theoretical contributions stand independently, but the missing results are still a severe weakness given the paper's own claims.*
- *Strength Finder's "Empirical validation across multiple compositional tasks" — removed because this strength conflicts with the verified weakness that the experiments section contains no results. Per instructions: when a strength and weakness disagree, the weakness wins.*
- *Strength Finder's "Log-space characterization" being described as a fully novel contribution — weakened because the paper itself acknowledges prior work (Merrill et al. 2024) establishing SSMs ∈ **TC⁰** ⊆ **L**, so the novelty is in the self-contained proof, not the result itself.*
- *Harsh critic's point about "Theorem 1's proof contains a probability-direction error that invalidates the logical chain" — downgraded from fatal to minor because the error is an algebraic slip in one line (q ≤ R/(3n log n) should be q ≤ 1 − R/(3n log n)); the theorem statement is correctly formulated and the intended derivation is clear.*
- *Harsh critic's claim about missing related works and formatting/style nitpicks — removed per instructions (cannot verify missing related works; formatting issues are parser artifacts).*
- *Harsh critic's point that the log-space proof is "incomplete" and "essentially a known result" — the known-result point is kept as minor; the incompleteness is real but the result itself is already established by prior work, so it does not threaten the paper's overall validity.*
- *Various section-by-section nitpicks (e.g., "Section 2 adds little" — this is a background section, not expected to be novel; "definition of φ_k is ambiguous" — it is defined in the CoT definition block).*

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuine insight: this paper shows that the function-composition limitations previously proved for Transformers are *architecturally robust* — they transfer to SSMs, which have a fundamentally different state-update mechanism (linear recurrence vs. attention). This suggests the bottleneck is not in the specific computation (attention vs. recurrence) but in the bounded hidden state that both architectures share when constrained by fixed precision and dimension. This observation is implicit in the paper but worth highlighting as a direction for future work.

## Suggestions

1. **Fill the experiments section with actual results.** Add accuracy tables for each of the four task settings (function composition, multi-digit multiplication, dynamic programming, Einstein's puzzle) with error bars across the three evaluation runs. Without these data, the paper cannot claim empirical validation.

2. **Fix the algebraic error in the Theorem 1 proof.** Replace "q ≤ R/(3n log n)" with "1 − q ≥ R/(3n log n)" (or equivalently "q ≤ 1 − R/(3n log n)") to maintain consistency between the definition of q (correctness probability) and Lemma 1's error-bound framing.

3. **Calibrate the rhetoric in the conclusion.** Replace "exponentially large hidden dimensions" with "polynomially large hidden dimensions" or a more precise characterization matching Theorem 1's bound.

4. **Expand the CoT proof sketch** to explicitly address how each party computes their required hidden states from local data, making the reduction to pointer chasing fully transparent.

5. **Clarify the multi-layer log-space argument** by specifying the recomputation schedule that keeps space O(L log N) rather than O(N).

## Score and Decision

This paper addresses a worthwhile question and provides a theoretically sound (albeit incremental) extension of known Transformer limitations to SSMs. The core theoretical idea — using communication complexity to lower-bound SSM state requirements for function composition — is sensible and the reductions are on the right track. However, the submission in its current form has two critical problems: (1) the experiments section is a stub with no results despite the paper repeatedly claiming empirical validation, and (2) the conclusion overclaims with "exponential" language that the proved polynomial bound does not support. The proof-level issues (algebraic slip, terse CoT reduction, sketchy log-space argument) are fixable but nontrivial. Given that the paper cannot be evaluated on its claimed empirical evidence and that the theoretical novelty is incremental (extending established Transformer results), the submission falls short of the acceptance threshold.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>