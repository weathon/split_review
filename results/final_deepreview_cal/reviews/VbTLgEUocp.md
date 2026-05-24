Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper presents *Calgacus*, a simple generative-steganography protocol that uses an LLM to encode an arbitrary secret text into a coherent cover text of the same length. The method works by computing the token ranks of the secret text under the LLM and then generating a new text using a different secret prompt, choosing at each step the token at the prescribed rank rather than sampling. The stegotext can be steered in topic/style by the prompt, and the original message is exactly recoverable by anyone who knows both the prompt and the LLM. The paper provides a modest quantitative evaluation (log-probability comparisons against 1000 Reddit posts) and an extended discussion of philosophical implications around authorial intent, hallucinations, and AI safety.

## Strengths

- **Elegant, well-explained protocol**: The three-step recipe (tokenize, compute ranks, generate by rank-selection) is clearly described, intuitive, and illustrated with a concrete worked example (Figure 3). The method is a genuinely counterintuitive use of LLM autoregressive generation.

- **Quantitative plausibility evidence (Figure 4)**: The paper shows that 300 stegotexts generated from three source texts at different percentiles of the real-text distribution all fall within the log-probability range of 1000 real Reddit posts, while random ASCII and random-English-word baselines fall far outside. This is direct, distribution-level evidence that the protocol produces cover texts indistinguishable from real text by this metric.

- **Mechanistic analysis of the probability gap (Figure 5)**: The paper identifies *why* stegotexts are on average less probable than their originals — rank-1 tokens are "wasted" on low-entropy positions — and provides empirical analysis of rank frequency and associated probabilities. This deepens understanding of the protocol's behavior.

- **Concrete, recoverable end-to-end examples (Figure 1)**: The Caesar-critique hidden inside a recipe and a speech is a compelling demonstration that the protocol works as described and supports the paper's conceptual claims.

- **Reproducibility and practicality**: The method is described as a simple recipe using open-source models (Llama 3 8B), code is publicly released, and the paper claims encoding/decoding in seconds on commodity hardware.

## Weaknesses

### Fatal

None.

### Major

- **Evaluation is too thin to support claims about output quality.** The only quantitative evaluation uses three source texts (each expanded into 100 stegotexts with different prompts) and measures only log-probability under the generating LLM. The paper provides no human evaluation of fluency, coherence, or topic relevance, no test of how often stegotexts become gibberish with "difficult" hidden texts (though one hash example is given qualitatively), and no systematic measurement of whether stegotexts actually stay on the intended topic. The paper itself acknowledges that log-probability is "a defective measure of meaningfulness." For a method that claims to produce "well-formed and plausible" text carrying arbitrary hidden messages, 300 stegotexts from three source texts with a single automated metric is insufficient evidence.

- **Practical significance of "full capacity" over existing methods is not established.** The paper positions equal-length encoding as Calgacus's distinguishing property and "main interest," but provides no quantitative comparison with prior LLM-based steganography (Meteor, Wu et al., Zamir) on hiding capacity, output quality per bit, or security. The claim that equal length "prevents one from establishing at first sight which text is authentic when we have one next to the other" addresses a narrow scenario — in typical steganography, only the stegotext is transmitted, not the hidden message alongside it. The paper would benefit from clarifying what practical situations this property enables that prior methods cannot address.

### Minor

- **Security discussion is informal.** Section 3.1 provides an upper bound on brute-force attacks and discusses deniability, but the claim that inserting a random string in the key "nips [a brute-force attack] in the bud" is stated without quantitative analysis. The paper explicitly disclaims formal treatment ("we will avoid building a palace on the sand"), which mitigates this concern, but the security claims made in the text still lack supporting analysis.

- **The philosophical discussion overreaches the technical results.** Section 4 proposes redefining hallucinations as a "void of intention" and challenges what it means for an LLM to "know" something. While engaging and well-written, these arguments are presented as commentary rather than conclusions grounded in empirical evidence from the protocol. The paper straddles two genres (method paper and position paper) without fully satisfying the standards of either.

- **The unaligned-chatbot scenario is illustrative but has limited standalone force.** The "Shibbolethian Theatre" scenario (Section 4) uses the protocol to embed unfiltered LLM answers within compliant responses. While it demonstrates an application of the method, the scenario requires a cooperative company that both deploys the protocol and sends the secret key alongside the response — a setup whose practical motivation is not fully argued. The paper acknowledges this is "described for research purposes," which appropriately scopes the claim.

### Trivial

None.

## Nice-to-Haves

- A comparison with a baseline that generates text from the prompt *without* the rank constraint, to quantify how much coherence is lost by following prescribed ranks.
- Analysis of how topic alignment and prompt steering interact with the hidden text across a wider range of inputs.
- Larger-scale evaluation with diverse hidden texts (news, reviews, poems, tweets) and multiple LLM sizes to support the claim that "even modest 8B models are sufficient."

## Removed Points

These points from the input reviews were considered but removed:

- *"The description of hiding 'the first page of the unreleased 8th Harry Potter book' is misleading"* — This is a vivid illustrative example, not a claim of universal applicability. The paper explicitly discusses when the protocol fails (the hash example in §3).

- *"The unaligned chatbot scenario is contrived / could be done with any steganographic channel"* — The scenario makes specific use of Calgacus's properties (same-length encoding, prompt-based steering) and is scoped as a research illustration. This criticism demands the paper solve problems outside its stated scope.

- *"Missing comparison with random rank selection to demonstrate necessity of hidden text structure"* — This is a nice-to-have ablation, not a flaw in the existing evaluation.

- *"The examples in the figures are cherry-picked"* — The paper provides quantitative evaluation in Figure 4 alongside illustrative examples. Using well-chosen examples for illustration is standard practice.

- *"The philosophical claims constitute a separate paper"* — Discussion sections are the appropriate place for broader implications. The concern is folded into the Minor weakness about overreach.

- *"Model availability / reproducibility concerns"* — The paper cites open-source models (Llama 3 8B) and releases code. Per review policy, cited models exist.

- *"Missing appendix sections (A.1, A.2, A.5, Figure 13, etc.)"* — The appendix is stripped by the parser; these exist in the original submission.

- *"No comparison with a baseline that generates text from the prompt without the rank constraint"* — Moved to Nice-to-Haves.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an interesting tension: the paper's most compelling contribution is the protocol itself — a simple, counterintuitive demonstration of what LLMs enable — while the quantitative evaluation that would normally anchor such a method paper remains thin. The strength of the idea and the clarity of the exposition carry the paper further than the empirical evidence alone would justify. This suggests that the paper's primary value is conceptual and demonstrative rather than empirical, which is unusual but not invalid for a venue that accepts position-adjacent work. The protocol's connection to Oulipo-style constraint literature (raised in the paper's discussion) is genuinely fresh and underexplored in the ML literature.

## Suggestions

- Expand the evaluation to include at minimum 10–20 diverse source texts (news, social media, fiction, technical writing) with 20+ prompts each, and report both automatic metrics (log-probability, perplexity, coherence scores) and a small human evaluation of fluency and topic relevance.
- Provide a quantitative comparison with at least one prior LLM-based steganography method (e.g., Meteor) on encoding capacity and output quality, to substantiate the claimed advantage of "full capacity."
- Either strengthen the philosophical claims by grounding them in additional empirical evidence from the protocol, or narrow the discussion section to focus on the technical implications that the current results actually support.

## Score and Decision

**Calibration anchors consulted:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | R1 | Calgacus is stronger: more novel protocol, clearer contribution |
| urQi0TgXFY (Steganographic Collusion) | 5.00 | R1,R2 | Comparable: similar creative core idea, but Calgacus is simpler and more accessible while having thinner evaluation |
| 7suavRDxe8 (Deniable Encryption w/ LLMs) | 4.80 | R1,R2 | Calgacus slightly stronger: cleaner protocol, clearer exposition, comparable evaluation rigor |
| 6p8lpe4MNf (Semantic Invariant Watermark) | 5.50 | R2 | Calgacus is weaker: the watermark paper has more rigorous experiments and formal analysis |
| W48CPXEpXR (Hallucinating LLM Could Be Creative) | 5.00 | R2 | Calgacus is stronger: more concrete technical contribution |

**Round 1 bracket:** 4.0–6.0, based on comparison with the deniable encryption paper (4.80) and the steganographic collusion paper (5.00) on the lower end and the semantic watermark paper (5.50) on the upper end.

**Round 2 narrowing:** Calgacus sits between the deniable encryption paper (4.80) and the semantic watermark paper (5.50). The protocol is more elegant and accessible than the deniable encryption paper, but the evaluation is thinner than the watermark paper. The paper's primary strength is conceptual clarity and a genuinely novel idea; its primary weakness is insufficient empirical grounding for its claims.

Final score: **5.0**. The paper makes a real technical contribution — a clever, well-explained protocol that works — and opens interesting directions for discussion. However, the evaluation is too thin to fully support the paper's claims about output quality, and the paper does not convincingly establish the practical significance of its "full capacity" property over prior work. These are addressable issues that would require a significantly expanded evaluation to resolve. At this level the paper is borderline, with the weaknesses outweighing the strengths for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>