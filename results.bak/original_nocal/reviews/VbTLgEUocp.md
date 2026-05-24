Now I have a complete understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper presents *Calgacus*, a simple steganographic protocol that uses an LLM to hide a secret text within another plausible text of exactly the same token length. The method works by recording the token-level ranks of the secret message under an LLM, then generating a "stegotext" by selecting tokens at those same ranks conditioned on a different key prompt. The paper demonstrates that stegotext log-probabilities fall within the distribution of real Reddit posts, discusses security considerations qualitatively, and explores implications for AI safety and the nature of authorship. A public demo is released.

## Strengths

- **Simple, accessible, and well-described protocol.** The method requires no training or fine-tuning — only access to LLM logits — and is explained clearly with a concrete example (Figure 3). The efficiency claim (encoding/decoding in seconds on a laptop with an 8B model) is substantiated by the released demo and is a genuine practical advantage.

- **Quantitative evidence of stegotext plausibility.** Figure 4 shows that 100 stegotexts (generated from three different source texts at different points in the real-text distribution) all fall within the log-probability distribution of 1000 real Reddit posts, while random ASCII strings and random English-word strings do not. A cross-model check using Phi-3 (Figure 14, appendix) reproduces the same qualitative pattern, partially mitigating circularity concerns.

- **Notable same-length property.** Unlike prior generative steganography methods (Meteor, Wu et al.) that encode variable-length bit streams, Calgacus preserves exact token-length parity between the hidden and cover texts — a conceptually clean and practically useful property.

- **Analysis of the probability gap.** The "Low entropy token choices" paragraph (Section 3) provides a clear, concrete explanation (using the "Gaius Julius → Caesar" example and Figure 5) of why stegotexts are systematically less probable than their originals despite preserving token ranks. This analysis reveals a genuine behavioral property of the method.

- **Provocative discussion with broader implications.** The framing of hallucination as "lack of intention" rather than factual inaccuracy, and the identification of a concrete AI safety scenario (covertly shipping unfiltered answers inside compliant responses), are thoughtful and conceptually novel contributions that extend beyond the technical protocol itself.

## Weaknesses

### Fatal
None.

### Major

- **Limited stegotext quality evaluation.** The paper's central claim of "high-quality results" rests almost entirely on log-probability from the *same LLM* used to generate the stegotexts. While a cross-model check with Phi-3 is mentioned (appendix Figure 14), no human evaluation study, no alternative fluency metrics (e.g., perplexity from a held-out model, readability scores, topic-consistency measures), and no comparison against prior steganographic methods on quality are provided. The paper acknowledges the difficulty of measuring "meaningfulness" and adopts log-probability as a pragmatic proxy, but this proxy alone does not adequately support the claim that stegotexts are "coherent and plausible" in a practical or human-perceptible sense. The reader cannot assess whether the stegotexts would actually fool or appear natural to a human observer.

- **No empirical security evaluation.** The security analysis (Section 3.1) is entirely theoretical and qualitative. No steganalysis experiments are performed (e.g., training a classifier to distinguish stegotexts from natural text, attempting key-recovery attacks, measuring false-positive rates for deniability). The AI safety scenario ("Shipping unfiltered LLMs without really shipping them") is described as a play and claimed to "open a new challenge" but is not validated empirically — the referenced Figures 11–12 are in the stripped appendix, leaving the reader with only the textual description. The paper is honest about these being open questions, but the security discussion is presented assertively enough to create an impression of practical applicability that the evidence does not support.

- **No quantitative comparison with prior steganographic methods.** The related work section mentions Meteor (Kaptchuk et al., 2021), Wu et al. (2024), and Zamir (2024) but makes no quantitative comparison on metrics such as information rate (bits per token, accounting for key length), stegotext quality, computational overhead, or detection resistance. Without such comparison, the "full capacity" claim is stated but not contextualized against existing trade-offs in the literature.

### Minor

- **Limited experimental scope.** The main experiment uses only three source texts (each 85 tokens) embedded into 100 stegotexts each. Testing on longer texts (500+ tokens) or a more diverse set of source texts would help assess whether quality degrades with length or varies by content type. The paper notes this is a proof of concept, but the narrow scope weakens the generality of the findings.

- **The AI safety scenario is not validated.** Section 4 describes a scenario where a company covertly delivers uncensored answers via Calgacus-encoded compliant responses. While thought-provoking, the scenario is presented without any empirical demonstration that it works end-to-end (e.g., generating a concrete unsafe query, producing a compliant stegotext, and recovering the full unsafe answer on a local open model). This weakens the claim that the scenario "opens a new challenge in AI safety" — it remains a hypothetical.

### Trivial
None worth listing.

## Nice-to-Haves

- A human evaluation study (e.g., 100+ samples rated by 5+ annotators for coherence, naturalness, style consistency) would substantially strengthen the claim of "high-quality" stegotexts.
- Steganalysis experiments (e.g., training a classifier on perplexity or other features to distinguish stegotexts from natural text) would ground the security discussion.
- End-to-end empirical validation of the AI safety scenario with concrete examples.
- Quantitative comparison with Meteor, Wu et al., and Zamir on capacity (bits per token), quality (log-probability or human ratings), and detection resistance.
- Testing on longer texts and with varied secret-message types (e.g., high-entropy random content) to characterize failure modes more systematically.

## Removed Points

These points from the harsh critic were examined against the paper and found to be inapplicable or misleading:

1. **"Full capacity" property is misleading because the key must also be transmitted.** In steganography, the key is shared out-of-band and is not part of the transmitted material. The paper correctly states that the stegotext and secret message are the same length — this is a valid claim about the transmitted payload, not about the pre-shared key.

2. **"Stegotexts are systematically more 'surprising' which could be a detectable signal."** The paper explicitly discusses this in the "Low entropy token choices" section and the "How to distinguish" section. The paper acknowledges stegotexts are less probable and that LLMs can distinguish them. This is not a hidden weakness; it is a known property the paper already addresses.

3. **The evaluation is "circular" because the same LLM is used.** The paper uses the generating LLM as a plausibility metric AND validates with a different model (Phi-3, Figure 14). Using log-probability as a proxy is a stated design choice with acknowledged limitations. The true weakness is that the *type* of evidence (same-model log-probability) is insufficient to support the strength of the claim, not that it is logically circular.

4. General-area sweep concerns from the critic's section-by-section notes that lack specific anchors in the paper (e.g., "the evaluation lacks rigor" without pointing to a specific missing element) were removed as noise.

## Novel Insights

The harsh and strength reviews converge on similar observations but sometimes disagree on their severity. The key insight that emerges from synthesizing them is that this paper's contribution is split very unevenly between its technical core and its framing. The technical core — a dead-simple, same-length LLM steganographic protocol — is clean, novel, and well-presented. But the paper's framing ("high-quality results," "opens a new challenge in AI safety," security analysis) consistently over-reaches what the evidence supports. The strength finder correctly identifies the protocol's elegance and accessibility; the harsh critic correctly identifies that the evaluation is too thin to carry the weight of those claims. The genuine novelty is in the protocol's conceptual simplicity and the same-length property; the paper would be stronger if it scoped its claims more narrowly around these contributions and flagged the evaluation as a preliminary proof-of-concept rather than asserting "high-quality results."

## Suggestions

1. **Tone down the quality claim** or back it with a human evaluation. Replace "high-quality results" with something like "results that are plausible according to the generating model's own probability distribution" unless human judgments are added.
2. **Add a quantitative comparison with Meteor and Wu et al.** on at least one dimension (e.g., bits per token, or stegotext log-probability) to contextualize the "full capacity" property.
3. **Add steganalysis experiments** (even a simple logistic classifier on perplexity features) to ground the security discussion. This would significantly strengthen the paper's empirical contribution.
4. **Empirically validate the AI safety scenario** with at least one concrete end-to-end example, or else present it as a hypothetical risk rather than a demonstrated vulnerability.
5. **Expand the evaluation** to longer texts and more diverse source content to assess whether the method generalizes beyond the 85-token setting.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>