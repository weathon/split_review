## Summary

This paper presents *Calgacus*, a steganographic protocol that uses an LLM to hide a secret text *e* inside another coherent text *s* of the same length (in tokens). The method tokenizes *e*, records each token's rank in the LLM's probability distribution, then generates *s* by following those same ranks from a secret prompt *k*. Decoding reverses the process. The paper provides experimental evidence (LLM-assigned log-probability) that the stegotexts fall within the distribution of real texts, analyzes why stegotexts are systematically less probable than originals, and includes a philosophical discussion about intentionality, hallucination, and LLM knowledge.

## Strengths

1. **Clean, simple protocol with exact encoding/decoding symmetry.** The method is described in a few lines and achieves the notable property that stegotext and secret message have the same token length. This simplicity contrasts with prior generative steganography methods (Meteor, Wu et al., Zamir 2024) and is the paper's clearest differentiator.

2. **Quantitative evidence that stegotexts fall within the log-probability distribution of real texts (Figure 4).** The paper generates 300 stegotexts (100 each from 3 source texts selected at μ, μ−2σ, μ+2σ of the Reddit distribution) and shows their log-probabilities lie within the range of 1000 real Reddit posts as measured by Llama 3 8B. The paper further verifies this pattern using a different LLM (Phi-3 3.8B, Figure 14), partially addressing circularity concerns.

3. **Insightful analysis of the systematic probability gap ("low-entropy token choices," Section 3, Figure 5).** The paper identifies why stegotexts are typically less probable than originals: rank-1 tokens are "wasted" in positions where the LLM would assign them lower probability than the natural high-probability continuations. This mechanistic insight goes beyond simply observing a performance gap.

4. **Plausible deniability argument (Section 3.1).** The paper shows that some prompts produce stegotexts with log-probabilities comparable to originals, providing a concrete basis for deniability even under coercion.

5. **Concrete AI safety scenario ("Shibbolethian Theatre," Section 4).** The multi-act play illustrates how the protocol could ship unfiltered LLM capabilities under the guise of aligned responses, making the abstract implications tangible.

6. **Honest treatment of limitations.** The paper explicitly shows a failure case (encoding a hash produces broken stegotext), discusses the need for identical LLM conditions, and acknowledges that key-search-space reduction is an open question.

## Weaknesses

### Fatal
None.

### Major

1. **No human evaluation of stegotext plausibility, despite this being the paper's central empirical claim.** The paper asserts that stegotexts are "plausible," "coherent," and "meaningful." The quantitative evidence relies entirely on LLM-assigned log-probability as a proxy. While the paper acknowledges limitations of this metric and uses a held-out LLM (Phi-3) for verification, a log-probability score conflates grammar, topic-appropriateness, stylistic coherence, and factual accuracy — two texts with identical aggregate log-probability can differ dramatically in perceived naturalness. A human evaluation study (e.g., naturalness ratings comparing stegotexts against real texts) is the standard way to substantiate such claims and is conspicuously absent. Without it, the paper's strongest claims about text quality rest on an unvalidated proxy that is known to have limited correlation with human judgment.

### Minor

1. **Limited source text diversity.** The paper generates stegotexts from only 3 source texts (selected at μ, μ−2σ, μ+2σ from the Reddit distribution). This makes it difficult to assess how output quality varies across content types (dialogue, domain-specific jargon, poetry, formulaic text, etc.). The paper acknowledges this dependency in principle but does not investigate it systematically.

2. **No quantitative capacity analysis (bits per token).** The paper claims "full capacity" (same token length) as its distinguishing property but does not report the empirical information density achieved. Since each token rank encodes a variable number of bits (rank r encodes log₂(r) bits on average), reporting the empirical rank distribution and resulting bits-per-token would help quantify the method's efficiency relative to the theoretical maximum (the entropy of the LLM's distribution).

3. **"Same length" qualification could be clearer.** "Same length" means *token count*, not character or word count, which can diverge significantly from human-perceived length. The paper states this on line 19 ("in terms of LLMs tokens") but it is easy to miss in the abstract and introduction where the headline claim appears without qualification.

### Trivial
None.

## Nice-to-Haves

- Comparison against prior LLM steganography methods (Meteor, Wu et al., Zamir 2024) on at least one dimension (text quality or capacity) to help readers situate the contribution. The paper scopes itself as a conceptual contribution, so this is not a requirement but would strengthen the empirical picture.
- Experimentation with more diverse source text genres (news, poetry, dialogue, technical writing).
- Analysis of how inference parameters (temperature, top-p, float precision) affect decoding reliability.

## Removed Points

These points were flagged by the reviewers but are removed from the main evaluation:

- **"Log-probability as sole metric conflates multiple properties of text"** — This concern is subsumed by Major weakness #1 (no human evaluation). The paper also acknowledges the metric's limitations explicitly (lines 124-128). The criticism adds no new information beyond what is already factored into the human evaluation gap.
- **"Security analysis is trivial (O(d^|k|) bound)"** — The paper itself states this is a naive bound and discusses how the search space could be reduced. The criticism does not identify a flaw the paper hides.
- **"Random ASCII/English words baselines are strawman comparisons"** — The paper uses these as negative controls to validate that log-probability can distinguish text from noise. This is standard experimental practice, not a strawman.
- **"Philosophical discussion goes beyond experimental results"** — This reflects the paper's stated ambition as a conceptual/positional contribution. The paper is transparent about this framing from the abstract.
- **"Example texts in Figure 1 do not inspire confidence"** — Subjective judgment about illustrative examples, not experimental evidence.
- **"No comparison to existing LLM steganography methods"** — Weakened to Nice-to-Have because the paper explicitly scopes itself as a conceptual contribution focused on the same-length property and its implications, not as a benchmark-driven comparison.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Conduct a human evaluation study (e.g., 50+ participants rating "how natural does this text look?" for stegotexts vs. real texts vs. originals) to substantiate the plausibility claim.
2. Expand to at least 10–15 source texts across diverse genres (news, dialogue, technical writing, social media) to establish generality.
3. Report the empirical distribution of ranks and the resulting bits-per-token capacity of the method.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>