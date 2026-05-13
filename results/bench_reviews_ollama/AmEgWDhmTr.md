Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper investigates why Chain-of-Thought (CoT) improves Transformer reasoning by arguing that the benefit lies in sample efficiency rather than expressiveness. Using a parity-learning testbed, the authors show that: (1) a 1-layer transformer can represent parity without CoT (Theorem 1), yet learning it without CoT requires exponentially many samples under bounded-memory one-pass SGD (Theorem 2); (2) with CoT data introducing sparse sequential dependencies, a 1-layer transformer can learn parity with near-linear samples and the learned attention becomes one-hot on the relevant secret indices (Theorem 3). Experiments on both synthetic parity problems and GSM8K support the sparsity mechanism hypothesis.

## Strengths

- **Formal separation of expressiveness from learnability.** Theorems 1 and 2 together establish that parity is representable but exponentially hard to learn (under specific conditions), directly challenging the common assumption that CoT's benefit is primarily about expressiveness. This is a clean and valuable framing contribution.

- **Concrete mechanistic account with interpretable attention guarantee.** Theorem 3 not only proves learnability with CoT but also establishes that the learned attention pattern becomes one-hot on the secret indices (error < 1/n⁸). The three-phase training dynamics (FFN configuration → sparse attention learning → output mapping) provides a testable mechanistic story for how CoT structures gradient signal, which is more detailed than most theoretical accounts of CoT.

- **Honest presentation of complicating results.** The paper explicitly reports that multi-pass training without CoT can succeed on parity (Section 5.2, Figures 4–5) and notes this complements rather than contradicts the one-pass lower bound. The observation that 50K samples succeed with multi-pass while 1M samples fail is intriguing and the paper does not hide it.

- **Parity as a clean testbed.** The problem isolates the "identifying which inputs matter" aspect of reasoning, and the CoT structure (sequential XOR accumulation) is a natural decomposition, making the mechanism transparent.

## Weaknesses

### Fatal
None.

### Major

- **Regime mismatch between the two main theorems undermines the headline comparison.** Theorem 2 provides an exponential lower bound without CoT that holds for *all* k, while Theorem 3 provides a polynomial upper bound with CoT that holds only when k ∈ [n/log⁵(n/δ), n/log⁴(n/δ)] — meaning the secret set must comprise nearly all input tokens. In this regime, CoT steps involve nearly the entire input, which is the opposite of the setting where identifying a small secret set among distractors is the core challenge. The motivating experiments use k = 1,2,3,4 (n = 30), which fall far outside Theorem 3's regime. This means the central claim — "exponential without CoT, polynomial with CoT" — compares bounds in mismatched parameter regimes, and the theory does not directly justify the empirical observations. This significantly weakens the paper's core theoretical argument.

- **Theorem 2's scope (constant-pass, bounded-memory SGD) is narrower than the paper's framing suggests.** The abstract states flatly that "without CoT, the required sample size is exponential" (line 6) and the introduction claims the function requires "exponentially more samples" without CoT (line 21), but Theorem 2 only proves this for constant-pass SGD with O((d²+dm)log n) memory. The paper's own multi-pass experiments demonstrate that this hardness can be circumvented. While Section 5.2 acknowledges this, the abstract and introduction do not properly qualify the result, making the headline claim misleading relative to what the theorem actually proves. The real contribution is that CoT restructures the *optimization landscape* by introducing sparse dependencies, not that it fundamentally changes the statistical complexity of parity.

### Minor

- **GSM8K experiments are correlational and cannot establish the claimed causal mechanism.** Section 5.3 shows that attention entropy is lower on CoT data and that Qwen2-Math-7B has lower entropy than Qwen2-7B. However, these observations have clear confounders: (a) the Math model differs in training data and procedure beyond just CoT exposure; (b) lower entropy could reflect positional or structural artifacts of longer sequences rather than meaningful sparsity; (c) no intervention (e.g., enforcing sparse attention and measuring downstream performance) is conducted. The paper uses hedging language ("suggesting," "indicating") but the claim that "CoT induces sparsity on real-world data" (Section 5.3 heading) overstates what these experiments show.

- **Assumption 1 in Theorem 3 is a highly engineered initialization.** The FFN weights are initialized to correlate with secret-index embeddings (line 182–184), which is strong structural information provided to the model. The paper does not discuss sensitivity to this assumption or whether the three-phase dynamics persist under standard random initialization, leaving it unclear how general the proof mechanism is.

- **The sample complexity metric — "first time achieving 100% validation accuracy" (line 59) — is noisy and non-standard.** Reaching 100% accuracy on a finite test set can occur due to variance, especially for small k. No error bars or confidence intervals are reported, and the exponential-vs-linear comparison in Figure 1a depends on these measurements.

### Trivial
None.

## Nice-to-Haves

- Testing whether artificially inducing sparse attention (e.g., via sparsity regularization or attention masking) during no-CoT training improves sample efficiency would provide causal evidence for the mechanism hypothesis.
- Extending Theorem 3 to cover small k (the regime where CoT is most practically useful) would bridge the theory-experiment gap and significantly strengthen the paper.
- A controlled ablation on GSM8K separating CoT structure from sequence length (e.g., padding no-CoT responses) would rule out the trivial explanation that longer sequences yield lower normalized entropy.

## Removed Points

- **Theorem 2 applies to "online learning algorithms" not transformers specifically.** The harsh critic notes the proof uses communication complexity arguments for bounded-memory streaming algorithms. However, the paper (line 163) explicitly states the bound is for SGD with specific memory constraints, and the result is a legitimate lower bound for a natural training regime. The restriction is clearly stated; calling it "not about transformers per se" overstates the issue.

- **The "expressiveness vs. sample efficiency" dichotomy is a false choice.** The harsh critic argues both could matter simultaneously. The paper does not claim expressiveness is irrelevant; it demonstrates a specific setting where expressiveness is *sufficient* but learnability fails, making the dichotomy a valid analytical device rather than a false one.

- **The "min over tokens" entropy measure is potentially sensitive to outliers.** While true, this is a measurement design choice that is clearly defined (line 280) and motivated by the fact that "attention heads may specialize in extracting information for specific tokens." This is reasonable for measuring sparsity of a specialized head.

## Novel Insights

The paper's most novel contribution is the identification of sparse sequential dependency as the key structural property that CoT injects into data, and the rigorous demonstration that this property enables a three-phase learning dynamic in which attention naturally becomes one-hot on the relevant tokens. This goes beyond the common "CoT increases expressiveness" narrative by providing a specific, testable mechanism. The observation from multi-pass experiments that more data can hurt (50K samples succeed, 1M samples fail) is an intriguing phenomenon suggesting memorization-driven generalization plays a role, and deserves further investigation.

## Suggestions

- Qualify the abstract and introduction claims about Theorem 2 to explicitly note the one-pass, bounded-memory constraint and acknowledge that the exponential lower bound does not hold for multi-pass training.
- Discuss the regime mismatch between Theorems 2 and 3 explicitly and either extend the theory or limit the scope of the claims accordingly.
- Report error bars or standard deviations across multiple runs for the empirical sample complexity measurements.

## Score and Decision

This paper makes a genuinely interesting contribution in identifying sparse sequential dependencies as the mechanism through which CoT improves sample efficiency, backed by the concrete three-phase training dynamics proof. However, the headline "exponential to polynomial" comparison is built on mismatched theoretical regimes (Theorem 2 covers all k while Theorem 3 covers only k ≈ n/polylog(n)), and the exponential lower bound applies only to one-pass bounded-memory SGD while being presented more broadly in the abstract. The core insight and mechanistic account are valuable, but the overclaiming from theory that does not cover the experimental setting significantly weakens the paper's central argument.

MY FINAL SCORE: <pineapple>6</pineapple>
MY FINAL DECISION: <orange>Accept</orange>