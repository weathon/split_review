Now I have a good picture. Let me finalize the review with a score of **5.5**.

**Bracket summary:**
- Round 1 anchors: IQafqgqDzF (3.50) — clearly below Calgacus; urQi0TgXFY (5.00) — Calgacus is better; KRnsX5Em3W (6.50) and 567BjxgaTp (6.75) — clearly above Calgacus. Bracket: 5.0–6.5.
- Round 2 narrows: RC5FPYVQaH (5.75) — Calgacus is slightly weaker empirically but comparable in novelty; aS1IhKdLPP (4.75) — Calgacus is better. Calgacus lands at **5.5** — a borderline accept with genuine intellectual contributions offset by empirical gaps.

---

## Summary

This paper presents *Calgacus*, a steganographic protocol that uses an LLM to encode an arbitrary text into another coherent text of exactly the same token length. The method is simple: tokenize the secret message, record the rank of each token under the LLM's probability distribution, then generate a new text from a secret prompt by selecting the rank-prescribed token at each step. The paper leverages this "full capacity" protocol to discuss LLM intentionality, to reframe hallucination as a failure of attributed intent rather than factuality, and to present a concrete AI-safety scenario involving covertly deployed unfiltered models.

## Strengths

- **Full capacity (1:1 token ratio) via an elegant, simple mechanism.** The encoding procedure consists of only three steps (lines 102-108): tokenize, record ranks, regenerate from a secret prompt by selecting the rank-prescribed token. This contrasts with prior LLM-based steganography (e.g., Meteor, Wu et al., Zamir) which do not achieve same-length encoding. The paper correctly positions this "full capacity" property as its novel technical contribution (line 67).

- **Empirical evidence that stegotexts fall within the plausibility distribution of real text.** Using 1000 Reddit posts as baselines and 100 stegotext variants across three source texts (chosen at μ, μ−2σ, and μ+2σ), Figure 4 demonstrates that stegotext log-probabilities fall within the real-text distribution, cleanly separated from random baselines. This is a falsifiable empirical claim supporting the protocol's ability to produce plausible output.

- **Insightful diagnosis of why stegotexts are systematically less probable than originals.** The "Low entropy token choices" analysis (lines 134-146, Figure 5) explains the mechanism: rank-1 tokens constitute ~40% of tokens in real text, but in stegotexts those rank-1s are applied indiscriminately across both low-entropy and high-entropy positions, "wasting" high-probability tokens. Figure 5 (right) quantifies the resulting probability gap. This is a genuinely non-obvious finding that goes beyond merely reporting results.

- **Concrete, well-specified AI safety demonstration.** The "Shipping unfiltered LLMs without really shipping them" scenario (Section 4, lines 174-206) provides a detailed five-act protocol with specific inputs and outputs, referenced to a real worked example.

- **Discussion grounds philosophical claims in technical results.** The reframing of hallucination as a failure of *intentionality* rather than factuality (lines 226-236) follows naturally from the protocol's decoupling of surface text from underlying message. The Oulipo analogy and the "constraint of chance" argument (lines 244-246) productively connect the method to broader questions about LLM text generation.

## Weaknesses

### Fatal

None.

### Major

- **Human imperceptibility is claimed but not evaluated.** The paper states that stegotexts are "opaque to humans" (line 43) and asserts real-world applications such as "crafting anti-government content disguised as pro-government messages" (line 21). The only evidence for plausibility is that stegotexts fall within the log-probability distribution of real Reddit texts under a single LLM (Figure 4). The paper acknowledges that log-probability is a proxy (line 124: "we adopt soundness as a practical proxy for meaningfulness") and that measuring meaningfulness is "an ill-posed problem." However, an LLM's aggregate log-probability can mask local incoherencies — odd word choices, tonal shifts — that a human reader might notice, especially given that ~60% of tokens are not the model's top choice (Figure 5). A human evaluation study would substantiate the paper's most important claims about societal impact and trust erosion. Without it, those claims remain speculative.

- **Experimental scope in the main text is limited.** The empirical evaluation rests on three source texts, one LLM (Llama 3 8B), one dataset (Reddit, 1000 samples), and one metric (log-probability). Three source texts — even carefully chosen at distributional extremes — cannot establish robustness across diverse text types and styles. Broader empirical validation would substantially strengthen the paper's generality claims.

### Minor

- **The Shibbolethian Theatre scenario has an unaddressed tension.** In Act 4, the reasoning trace *t* (which serves as the secret key *k*) is transmitted in the clear as part of the chatbot response. This means a third party who knows the Calgacus protocol, has the user's original query *c*, and possesses the exact oLLM could also decode the hidden unfiltered answer *u*. The paper's deniability argument (Section 3.1) addresses the company's legal position but not third-party decodability. The scenario remains interesting and valuable, but this limitation should be acknowledged.

### Trivial

- The claim that encoding/decoding runs "in seconds" on a laptop (lines 9, 19) is not supported by wall-clock measurements in the main text.
- The practical requirement of identical LLM conditions for sender and receiver (line 148) — including floating-point determinism across GPU architectures — is noted but merits more discussion given its practical significance.

## Nice-to-Haves

- A human evaluation study pitting stegotexts against real texts would dramatically strengthen the central claims, whatever the outcome.
- Deeper analysis of where stegotexts fail (at which ranks, in which syntactic positions) would sharpen the paper's contribution to understanding LLM generation constraints.
- Quantitative comparison of Calgacus's bits-per-token capacity against prior LLM steganography methods would help readers assess the tradeoff.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **HC: "The claim conflates two different distributions" (regarding line 112-113).** REMOVED — The paper's claim that low ranks in *e* lead to high-probability tokens after *k* is straightforward: the protocol uses the same rank values in a different context, and low ranks correspond by definition to high-probability positions in the sorted distribution. There is no conflation; the criticism misunderstands the mechanism.

- **HC: "The brute-force bound O(d^|k|) is misleading."** REMOVED — The paper explicitly acknowledges (lines 154-164) that natural-language keys have lower effective entropy and that an attacker could exploit this, and proposes inserting random strings as mitigation. The criticism ignores the text that immediately follows the bound.

- **HC: "Deniability evidence is only in stripped appendix (Figure 15)" and "Cross-model check with Phi-3 is in the stripped appendix."** REMOVED — The parser strips appendices from all papers; these exist in the original submission. The deniability argument in the main text (lines 166-167) is adequately motivated by the variance visible in Figure 4, and the paper references Figure 14 (Phi-3) at line 133.

- **HC: "The chatbot scenario does not hold up under scrutiny" (overstated version).** DEMOTED to Minor — The scenario's core claim (encoding unfiltered answers within aligned responses) remains valid; the third-party decodability concern is a limitation worth noting but does not invalidate the scenario. The HC's framing as "structural" or fatal was excessive.

- **SF: Generic framing strengths (e.g., "problem is important," "targets an interesting question").** REMOVED — These lack specific evidentiary anchors and are superficial.

## Novel Insights

The paper's most genuinely novel insight is its reframing of standard LLM text generation as already being a form of constrained optimization — that Calgacus merely makes explicit a constraint (arbitrary rank selection) that is already implicit in standard sampling (the "constraint of chance" argument, lines 244-246). This lens, combined with the observation that LLMs can serve as conduits for information they are "supposedly incapable of expressing," productively challenges how the field thinks about LLM knowledge and hallucination. The redefinition of hallucination as a failure of attributed *intent* rather than factual error is thought-provoking and well-supported by the protocol's mechanics.

## Suggestions

- Conduct even a modest human evaluation study (e.g., 50-100 raters asked to distinguish stegotexts from real texts). If humans perform at or near chance, the paper's central implications are validated; if they perform above chance, the paper gains an honest and interesting limitation.
- Acknowledge the third-party decodability tension in the chatbot scenario explicitly and discuss its implications for the threat model.
- Add analysis showing how stegotext log-probability varies with source text properties (e.g., entropy/perplexity) to help readers understand when the method works well versus when it produces gibberish like the hash example.

## Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IQafqgqDzF (OD-Stega) | 3.50 | R1 | Calgacus has a more novel property (full capacity), more elegant method, and more ambitious discussion |
| urQi0TgXFY (Hidden in Plain Text) | 5.00 | R1 | Calgacus is more novel and intellectually interesting; steganographic collusion paper had originality concerns |
| KRnsX5Em3W (LLMs Know More Than They Show) | 6.50 | R1 | Calgacus has thinner empirical evaluation and weaker evidence for its central claims |
| 567BjxgaTp (How to Catch an AI Liar) | 6.75 | R1 | Calgacus has similarly clever simplicity but far less thorough empirical validation |
| RC5FPYVQaH (CB-LLM) | 5.75 | R2 | Comparable novelty; CB-LLM has stronger experiments across tasks; Calgacus has deeper philosophical implications |
| aS1IhKdLPP (Reflection Window) | 4.75 | R2 | Calgacus is more novel and engaging |

Round 1 bracket: 5.0–6.5. Round 2 narrowed to **5.5**: Calgacus sits between the 5.00 steganographic collusion paper (better) and the 5.75 CB-LLM paper (slightly weaker empirically, comparable in conceptual contribution). The score reflects genuine intellectual contributions offset by significant but addressable empirical gaps.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>