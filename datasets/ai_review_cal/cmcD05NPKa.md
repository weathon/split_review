- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5
Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

This paper is an empirical study of small transformers trained to compute the GCD of two positive integers. The central contribution is a complete behavioral characterization: during training, the model learns a set of integers (products of base divisors and, after grokking, small primes) and outputs the largest element of that set dividing both inputs. The paper documents how training distribution (uniform vs. log-uniform operands, natural vs. balanced outcomes) affects both performance and explainability, showing that log-uniform distributions dramatically improve results (up to 91/100 GCD correctly predicted) while perfectly uniform outcome distributions break full explainability.

## Strengths

1. **Deterministic prediction rules (R1–R3) validated across many bases and settings**: The paper derives three simple rules that fully characterize model outputs from input-output behavior alone. Predictions are deterministic per GCD, correct predictions are products of primes dividing the base, and the model always predicts the largest learned divisor that divides both inputs. These rules are substantiated by Table 1 (correct GCD counts across 20 bases) and Table 2 (full prediction tables for bases 2 and 10), with frequencies near 100% throughout.

2. **Grokking of small primes discovered and documented with the same rule structure**: The paper shows that after long training plateaus, models suddenly learn non-divisor primes (e.g., 3 for base 1000) and then all their multiples — following the same extended rule structure (G1–G3). Section 4 and Table 3 report the exact grokking epoch and results for 16 large bases, providing clean evidence of a phenomenon that parallels grokking in a setting where memorization cannot occur (on-the-fly data generation).

3. **Training distribution controls both performance and explainability, with a clear mechanism**: The paper demonstrates that a log-uniform outcome distribution (favoring large GCD) boosts performance to 87–91 correct GCD, while a perfectly uniform distribution causes the model to cluster inputs into the same classes but predict an arbitrary class representative that changes every epoch — breaking explainability. This is supported by Section 6 (Table 5 showing best results) and Section 7 (detailed epoch-by-epoch prediction tables showing volatile classes).

4. **Systematic study of encoding base reveals a principled explanation**: Composite bases divisible by many small primes (e.g., 420: 38 correct GCD) dramatically outperform prime bases (e.g., 31: only 2 correct GCD). Table 1 and the surrounding text in Section 3 tie performance to simple divisibility tests based on the last digit(s) of the representation, providing an interpretable mechanism grounded in number theory.

5. **Log-uniform operand distribution boosts performance across all bases**: Training with log-uniform operands (many small examples) raises accuracy to 94–99% and correct GCD counts to 48–73 (e.g., base 10 from 13 to 48). Table 4 reports these results for 27 bases, and the paper notes accelerated learning (e.g., prime 3 learned by epoch 25 instead of requiring grokking).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented.

### Minor

1. **The "sieve algorithm" interpretation is presented as an indicated finding, not a proven mechanism.** The paper states in the Discussion that "Experiments indicate that transformers learn a sieve algorithm for computing GCD" (Section 7, line 429), but the evidence is entirely based on input-output prediction patterns and learning timing — not on attention analysis, weight inspection, or probing of internal representations. The sieve analogy fits the data well, but the paper never verifies that the model internally performs sieve-like operations (e.g., testing divisibility by checking last digits, splitting classes based on prime divisibility). This does not weaken the empirical characterization (which is the paper's main contribution), but the mechanistic interpretation remains speculative.

2. **Limited architectural generality.** The vast majority of experiments use a single architecture (4-layer, 512-dim, 8-head transformer). The paper briefly checks that a 1-layer 32-dim model and a 24-layer 1024-dim model achieve similar accuracy for base 30 (Section 3, line 104), but this is a single data point. The core observations about clustering and rule-following likely hold for small-to-moderate transformers, but the paper provides insufficient evidence to assert generality across model scales, depths, or architectural families.

3. **The "full explainability" framing is slightly imprecise for the uniform-outcomes case.** The abstract states that predictions "can be fully characterized" and bullet 5 notes that "explainability partially fails" under uniform outcomes. Section 7 shows that the uniform-outcomes case is still characterized by rules U1–U3 (deterministic per epoch, same classes, arbitrary class representative), but the mapping from class to output changes unpredictably across epochs. The paper is honest about this, but the phrase "fully characterized" in the abstract could be read as implying a stronger degree of explainability than what actually holds for the uniform-outcomes setting — namely, we cannot predict *which* element of the class will be output without checking each epoch. This is a minor framing issue, not a flaw in the science.

### Trivial

1. Table 3 (grokking) contains a duplicate row for base 2401 (lines 214–215), which appears twice with different results (10 GCD vs 14 GCD). This likely reflects multiple random seeds but is not clarified in the caption.

2. Line 438: "classifiers" is misspelled as "calssifiers."

## Nice-to-Haves

- **Reporting variance across seeds.** Many tables report "best of 3" or "best of 6" experiments. Providing mean and variance across seeds would give a better sense of reliability, especially for the "breakiness" observed under uniform outcomes.
- **Attention analysis.** A few targeted experiments — e.g., measuring whether the model attends to the final digit(s) for divisibility by powers of the base — would transform the behavioral characterization into a genuine mechanistic explanation and strengthen the sieve algorithm interpretation.
- **Testing on larger operands and GCD values.** The paper tests numbers up to 10⁶ and evaluates only GCD ≤ 100. It would be informative to report how performance degrades for larger operands or more GCD values.
- **Reporting computational cost.** Mentioning total training time per epoch and total parameters for the main 4-layer model would help practitioners assess the approach.

## Removed Points

- **The harsh critic's suggestion about "Alternative representations"** — The paper's stated scope is digit sequences in a given base; the base variation already partially covers representation effects. This is scope creep.
- **The harsh critic's "error bars and seed variance" concern** — Moved to Nice-to-Haves; the paper's patterns are strong enough without variance reporting, and best-of-N reporting is standard for this type of exploratory work.
- **The harsh critic's "scalability" point about larger GCD values** — Moved to Nice-to-Haves; this is an incremental extension, not a core weakness.
- **The harsh critic's suggestion about "Computational cost"** — Moved to Nice-to-Haves; not a weakness of the paper's claims.
- **Strength Finder strengths #1–6** — All retained as they are concrete, specific, and evidence-backed; none are generic or conflict with verified weaknesses.

## Novel Insights

The two review sources together highlight a compelling tension at the heart of the paper: the model's behavior can be *fully characterized* by simple rules even while the *mechanism* by which it implements those rules remains opaque. This distinction — between behavioral explainability (what the model does) and mechanistic explainability (how it does it) — is not explicitly drawn in the paper but emerges clearly from the reviews. The uniform-outcomes results (Section 7) push this tension further: the model demonstrably *learns the correct clustering* but cannot be trained to output the correct cluster representative because the training signal is uniform — suggesting that what we call "explainability" in neural models may be as much a property of the training distribution as of the model itself. This observation, implicit in the paper's data, is worth making explicit.

## Suggestions

- Add a brief discussion distinguishing behavioral characterization (what the paper does) from mechanistic interpretability (what it does not do), to set reader expectations more precisely.
- Add a small number of targeted attention-map analyses (e.g., checking whether the model attends to the final digit for base-2 divisibility) to support the sieve-algorithm interpretation without requiring a full mechanistic account.
- Clarify the duplicate base-2401 row in Table 3.
- Add mean/variance alongside best-of-N for the main results tables.
- Explicitly define "explainability" (behavioral vs. mechanistic) in the introduction or discussion to sharpen the uniform-outcomes analysis.
