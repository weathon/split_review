Now I have a clear picture. Let me write the consolidated review.

## Summary

This paper presents *Calgacus*, a protocol that uses an LLM's token-rank ordering to hide a secret message within a plausible cover text of exactly the same length. The method is simple: tokenize the secret message, record each token's rank in the LLM's distribution given its prefix, then generate the cover text by selecting tokens at the same ranks from the distribution conditioned on a secret key prompt. The paper's contributions are (1) the protocol itself, notable for achieving full capacity (same-length hiding) while producing coherent steerable cover texts, and (2) a philosophical discussion connecting the method to authorial intent, hallucination, and knowledge in LLMs.

## Strengths

- **Full-capacity encoding.** The protocol produces a stegotext exactly as long as the secret message. This is a genuine advance over prior generative steganography methods (e.g., Meteor, which encodes a variable number of bits per token). The paper states this clearly: "What we add to the field is *Calgacus*, a protocol with the notable property of having full capacity, that is, the stegotext and the secret message being of the same length" (Section 2).

- **Simple, elegant, and directly implementable protocol.** The method requires only access to token-level logits from an LLM and a standard autoregressive generation loop. The description in Section 3 is clear, the diagram (Figure 3) is helpful, and the low-entropy token analysis (Section "Low entropy token choices") explains why stegotexts are less probable than originals — one of the more rigorous parts of the paper. The paper explicitly notes that a hash fails as a secret message, showing awareness of limitations. A GitHub demo is linked for reproducibility.

- **Quantitative plausibility check against real texts.** Figure 4 compares the cumulative log-probability of 1000 real Reddit posts (85 tokens), random ASCII strings, random English-word strings, and 300 stegotexts (100 for each of 3 original texts). All stegotexts fall within the real-text distribution, providing empirical evidence that the outputs are not trivially distinguishable from human writing under this measure. The three original texts are chosen at μ, μ−2σ, and μ+2σ of the real-text distribution, showing some coverage of the plausibility spectrum.

- **Thought-provoking philosophical discussion.** Section 4 connects the protocol to a re-framing of hallucination (lack of intention rather than factual falsehood), a challenge to what it means for an LLM to "know" something, and the Oulipo connection. This discussion is genuinely original, well-written, and goes beyond what a pure steganography paper would offer. The "Shipping unfiltered LLMs without really shipping them" scenario grounds the technical idea in a concrete safety concern.

## Weaknesses

### Major

- **Limited empirical validation of stegotext quality.** The evaluation relies on three original texts, one main LLM (Llama 3 8B), and log-probability as the sole proxy for "plausibility." No human evaluation is conducted — the paper infers that "while for a human both the original and fake texts are plausible" without testing this directly. The abstract claims "high-quality results" and "even modest 8-billion-parameter open-source LLMs are sufficient," but these claims outrun the evidence, which is a single scatter-plot distribution. The paper explicitly says it will "avoid building a palace on the sand" regarding formal models, yet leans heavily on the log-probability measure without cross-validation against human judgment. This gap matters because the method's core value proposition — concealing meaning within natural-looking text — is undermined if the stegotexts are detectably unnatural to human readers, even if they pass an LLM-based check.

- **No comparison against baseline steganography methods.** The related work section mentions several prior LLM steganography methods (Ziegler et al., 2019; Kaptchuk et al., 2021; Wu et al., 2024; Zamir, 2024) but provides no quantitative comparison on capacity, text plausibility, or detection resistance. While the paper's stated focus is on the full-capacity property and its implications, readers have no way to gauge whether the trade-off (e.g., lower text quality for higher capacity) is favorable. Even a simple comparison of perplexity or human-likeness between Calgacus stegotexts and those from a prior method would substantially strengthen the paper.

### Minor

- **Security analysis is informal and incomplete.** The security discussion (Section 3.1) provides an upper bound O(d^{|k|}) for brute-force key search and mentions the possibility of more efficient attacks, but it is transparently informal — the paper states that "the feasibility of such an approach is unclear and remains an open research question." The deniability argument rests on one observation (some stegotexts attain probabilities comparable to originals) and a reference to Figure 15 (not visible in the excerpt). The countermeasure of inserting a random string into k is proposed but not analyzed. These gaps matter for a paper that raises "urgent questions for AI safety," but the paper is candid about the analysis being limited, and the protocol itself does not hinge on security guarantees.

- **The "shipping unfiltered LLMs" scenario is presented as a thought experiment, not a demonstrated attack.** The play (Section 4) is engaging but no implementation or experimental validation is reported. The claimed example (Figures 11–12, referenced but not visible in the excerpt) could ground the discussion, but the paper does not quantify success rates, stegotext quality in this setting, or practical obstacles. This weakens the "urgent questions for AI safety" framing relative to what would be needed to support actionable concern.

### Trivial

- **"Seconds" runtime claim (Abstract, Introduction) is stated without measurement.** The claim that "a message as long as this abstract can be encoded and decoded locally on a laptop in seconds" is plausible given the method's simplicity, but no runtime benchmarks are reported. The linked GitHub demo provides a path for verification but the paper itself should contain this data.

- **Only one LLM model size (8B) is used for most results.** The cross-validation with Phi-3 3.8B (Figure 14) is a good addition, but the paper's claim about "modest 8-billion-parameter" models working well would be strengthened by testing across a wider range of model sizes and architectures.

## Nice-to-Haves

- A small-scale human evaluation (e.g., 20–30 participants judging whether texts look natural) would directly address the most significant evidential gap.
- Characterizing the failure regime more thoroughly — varying e's perplexity, topic mismatch with k, and different LLMs — would make the protocol's operating envelope clearer and more useful.
- Reporting per-text statistics and confidence intervals for the log-probability comparisons would improve the quantitative analysis.

## Removed Points

These points were considered but excluded from the main review:
- "The paper omits discussion of how Calgacus compares to other steganography methods on quality/capacity/detectability" — already addressed in the Major weaknesses; the paper does position itself differently (full capacity as the differentiator) and scopes out systematic comparison.
- "Reproducibility details about secret keys not being reported" — the paper provides a GitHub demo that enables reproduction, and specific keys for the examples are stated in the Figure 1 caption.
- "The paper doesn't analyze properties of e and k that determine success" — covered in Minor weaknesses; the paper's Limitations subsection explicitly acknowledges these dependencies and the hash failure example illustrates one boundary condition.
- "Security analysis ignores far more efficient strategies" — the paper acknowledges this ("remains an open research question"); the criticism overstates the omission.
- Various formatting and style nitpicks — removed per instructions.
- "Missing related works" — removed per instructions (cannot verify external omissions).

## Novel Insights

None beyond the paper's own contributions. The key conceptual insight — that choosing the k-th most probable token at each position is not qualitatively different from standard sampling, and that this creates a radical decoupling of text from intent — is already the paper's central thesis and is well-argued in Section 4.

## Suggestions

1. Add a human evaluation study (even modest in scale) to validate that stegotexts are perceived as natural — this is the single most impactful addition.
2. Include runtime measurements to support the "seconds" claim in the Abstract.
3. Provide a more systematic characterization of which types of secret texts (e, in terms of perplexity or rank distribution) and which keys (k) produce successful vs. failed stegotexts.
4. Add at least one quantitative comparison against a prior generative steganography baseline (e.g., Meteor) on a dimension the paper values, such as text plausibility under the same LLM-based measure.
5. Report per-text statistics (not just aggregate Figure 4) with variance across different secret texts and keys.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on LLM steganography topics. Weak anchors (avg < 3.5) came from Sparse Watermarking and similar papers (avg 3.00). Middle anchors (3.5–7.5) included "Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs" (avg 5.00), "A Semantic Invariant Robust Watermark" (avg 5.50), and "An End-to-End Model for Logits Based LLM Watermarking" (avg 5.25). Strong anchors (avg > 7.5) were high-quality ML papers on unrelated topics (avg 8.00). → Initial bracket: **4.0–6.0**.

**Round 2 (Narrowing):** Searched inside (3.5, 6.5) with a topical query. Retrieved the same papers plus "Plausibly Deniable Encryption with Large Language Models" (avg 4.80), which is topically similar (LLM-based concealment). Read all four in full.

- vs. "Plausibly Deniable Encryption" (4.80, reject): Calgacus is stronger — clearer writing, actual empirical evaluation with figures, deeper philosophical contribution.
- vs. "Hidden in Plain Text" (5.00, reject): Calgacus has a more novel protocol but weaker experiments. Comparable overall.
- vs. "Semantic Invariant Robust Watermark" (5.50, accept): Calgacus has weaker empirical rigor but greater conceptual novelty. Slightly lower overall.
- vs. "End-to-End Watermarking" (5.25, reject): Calgacus is less thorough empirically but more original. Comparable.

**Final score:** **5.0**. The paper's core idea is simple, novel, and clearly communicated. The philosophical discussion is a genuine strength. However, the empirical evaluation is too narrow to support the stronger claims in the abstract ("high-quality results" with only log-probability as evidence, no human evaluation), and the security analysis is too informal for the safety claims. The paper reads more as a provocative position paper with a proof-of-concept than as a fully validated method.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>