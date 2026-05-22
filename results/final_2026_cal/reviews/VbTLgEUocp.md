Now I have all the information I need to produce the final consolidated review.

## Summary of Calibration

**Round 1 bracket**: The paper falls in (3.5, 7.5) — clearly above the weak band (scores 2-3) of rejected/withdrawn papers, and clearly below the strong band (8.0) of papers with thorough evaluation and rigorous methodology.

**Narrowing (Round 2)**: I compared the paper against accepted posters at 5.33 and 5.50 (both with interesting ideas but thin evaluation or limited technical contribution) and against steganography papers at 6.0 (more rigorous evaluation). The paper under review has a stronger method contribution than the 6.0 steganography papers (which mainly evaluate existing models) but weaker evaluation. It sits closest to the 5.33-5.50 range.

**Final score**: 5.5 — reflecting a genuinely novel and creative contribution with clear exposition, but with an empirical evaluation too narrow to fully support the scope of the claims.

Now for the review itself. Let me compile and filter all the points.

Let me carefully check the harsh critic's points against the paper once more before writing:

**Critic #1: Empirical evidence insufficient** — VERIFIED. 3 source texts, 85 tokens, one LLM. The paper itself acknowledges limitations (hash example, termination). But the critic says "the title constitutes an overclaim." The title says "LLMs Can Hide Text in Other Text of the Same Length" — this is actually supported; the paper shows it *can* be done. What's not shown is *how often* it works. The broader claim is in the abstract: "A meaningful text can be hidden inside another..." — this is strictly true as demonstrated. So the critic overstates slightly. But the thinness of the evaluation is a real concern.

**Critic #2: Full capacity framing misleading** — The paper's claim is about same token length between secret message and stegotext. The key is a pre-shared secret, which is standard in steganography. The paper mentions this and variations. This is a minor point at best.

**Critic #3: Security claims speculative** — The paper explicitly says it won't use a formal model. The security analysis is brief and honest about its limitations. The critic's point is valid but the paper doesn't claim provable security.

**Critic #4: Steerability not assessed** — VALID. The paper shows examples but no quantitative measure.

Now let me draft the review.

I need to be careful about:
1. The critic's claim about "The main text provides no evidence that the plausibility transfers across model families" — the paper actually mentions Phi-3 verification in the main text (line 137), but Figure 14 is in the appendix. Since the appendix was stripped by the parser, I should note this.
2. The critic's claim about "3 hand-picked examples" — they were selected at μ, μ−2σ, μ+2σ which is principled, not ad-hoc.

Let me now write the final review.**Calibration Anchors Used:**

| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| QJku1vSXrJ | 2.50 | R1 | Withdrawn; copyright detection paper — much weaker |
| US1UwMHHtS | 3.00 | R1 | Withdrawn; watermarking paper — much weaker |
| nDSTDq0uDK | 2.00 | R1 | Withdrawn; watermarking paper — much weaker |
| q4qxtaKVAU | 6.00 | R1/R2 | "Early Signs of Steganographic Capabilities" — more thorough evaluation but method is empirical-evaluation, not novel protocol |
| 6cEPDGaShH | 6.00 | R1/R2 | "Invisible Safety Threat" — thorough evaluation, strong baselines, concrete attack demonstrated |
| neE8pqIqyR | 5.00 | R2 | Rejected; watermarking paper with more evaluation but less novelty |
| WFGxFzFDmQ | 5.00 | R2 | Rejected; watermarking with thorough eval but novelty concerns |
| Fllp8l6Puy | 5.33 | R2 | Accepted Poster; good experimental design but limited technical contribution |
| zzTQISAGUp | 5.50 | R2 | Accepted Poster; novel framework but narrow evaluation, some concerns |
| t38nZqqi3Z | 6.50 | R2 | Accepted Oral; fingerprinting paper with thorough evaluation |

**Round 1 bracket:** (3.5, 7.5) — clearly above weak band, clearly below very strong papers.

**Narrowing (Round 2)**: Paper sits between the 5.33–5.50 accepted posters (novel ideas with evaluation gaps) and the 6.0 steganography papers (stronger evaluation). Score of 5.5 reflects a genuine method contribution held back by thin empirical validation relative to the scope of the claims.

---

## Summary

This paper presents *Calgacus*, a protocol that uses an LLM to encode an arbitrary secret text within a stegotext of the **same token length** — a property the paper terms "full capacity." The core idea is elegant and straightforward: tokenize the secret message, record the rank of each token in the LLM's probability distribution, then generate the stegotext by selecting tokens at those same ranks starting from a secret prompt *k*. Because the stegotext mimics the structural properties of real text (it is constructed from the LLM's high-probability token choices when the secret message is itself natural language), it falls within the distribution of genuine human-written text as measured by LLM log-probability. The paper includes a thoughtful philosophical discussion reframing hallucination as a failure of intention attribution and probing what it means for an LLM to "know" something.

---

## Strengths

- **Novel and elegant protocol with the full-capacity property.** The method achieves what the paper identifies as its key contribution: the stegotext and the secret message have the same token length. The protocol is described with admirable clarity (Fig. 3) and is immediately reproducible. The idea, once stated, feels almost self-evident — a hallmark of good research.

- **Quantitative evidence that stegotexts remain within the real-text distribution.** Figure 4 shows that stegotexts generated by Calgacus fall within the log-probability distribution of genuine Reddit posts of the same length, while random ASCII or English-word strings do not. This provides a concrete, measurable sense in which the generated texts are plausible.

- **Practical efficiency with modest hardware.** The paper demonstrates that the protocol runs on a laptop in seconds using an 8B-parameter open-source LLM (Llama 3 8B), and the provided demo runs even from a smartphone. This makes the contribution immediately accessible to practitioners.

- **Well-written and thought-provoking discussion.** The philosophical treatment of hallucination as a failure of intention attribution (Section 4), the Oulipo connection, and the question of what it means for an LLM to "know" something are intellectually rich and clearly articulated. The "shipping unfiltered LLMs" scenario provides a concrete and alarming application that connects the method to pressing AI safety concerns.

---

## Weaknesses

### Major

1. **Empirical evaluation is too narrow to support the breadth of the claims.** The quantitative experiments use only **3 source texts** (selected at μ, μ−2σ, μ+2σ of the real-text distribution), generate 100 stegotexts each, all at a fixed token length of **85 tokens**, with a **single LLM** (Llama 3 8B). The paper's title and abstract make sweeping claims ("a meaningful text can be hidden inside another... text of the same length"), but the evaluation does not characterize **how often** the protocol succeeds across a diverse range of source texts, topics, lengths, or LLMs. The 3 hand-picked texts (chosen at principled distribution points, but still only 3) are not a substitute for a systematic characterization. Without it, a reader cannot judge what fraction of natural-language texts are amenable to the protocol. The paper itself acknowledges limitations (the hash example, termination) but does not quantify the success-rate landscape.

2. **Steerability is claimed but never measured.** The paper asserts that the topic, tone, and style of the stegotext are steerable via the secret key *k*, and the examples in Figure 1 are indeed convincing. However, there is no quantitative evaluation of how well the stegotext actually adheres to the intended topic/style. Given that the protocol forces the LLM to choose from a restricted set of ranks, how often does the resulting text deviate from the intended topic? This gap matters because steerability is presented as a core capability of the method.

3. **No human evaluation of plausibility.** The paper states that the distinction between real and fake texts "remains opaque to humans" but provides no human-subject study to support this. Plausibility is measured exclusively via LLM log-probability (with a confirmatory check using Phi‑3, referenced as Figure 14 in the appendix). While log-probability is a reasonable proxy, a basic "detect the fake" experiment with human raters would directly support the paper's central claim that the generated texts are indistinguishable from real ones.

### Minor

- **Security analysis is informal and acknowledged as such.** The paper explicitly states it will not use a formal steganographic model. The attack scenarios in Section 3.1 are sketched rather than analyzed: the O(d^{|k|}) brute-force claim is immediately followed by the observation that the key space can be reduced by exploiting natural-language structure, with no analysis of the residual difficulty. The suggestion that a random string in *k* "nips [attacks] in the bud" is unsubstantiated. This is not a fatal flaw (the paper does not claim provable security), but it limits the practical applicability of the protocol in security-sensitive settings.

- **The "full capacity" framing glosses over key overhead.** The paper correctly notes that the stegotext and secret message are the same length in tokens. However, the secret key *k* is an additional piece of information that must be transmitted (or pre-shared). The paper's main rhetorical framing — "same length" — is technically true for the embedded payload but obscures the total communication overhead. This is a minor presentational concern; the paper already acknowledges variations (adding k' as context, appending random strings to k).

- **No analysis of how quality scales with text length or model size.** All experiments use 85-token texts and an 8B model. The paper mentions that encoding/decoding takes "seconds on a laptop" but does not provide time-per-token measurements or test smaller (e.g., 1B) models to find the threshold at which quality breaks down. These are natural ablations that would strengthen the paper.

### Trivial

None.

---

## Nice-to-Haves

- A systematic evaluation across, say, 100–500 source texts sampling the perplexity distribution, reporting the fraction that yield plausible stegotexts, would directly answer the most important question left open by the current work.
- A simple human evaluation (e.g., a Mechanical Turk "detect the fake" task) would strengthen the claim that stegotexts are opaque to humans.
- A plot of lexical diversity or topic-similarity (via embedding cosine similarity) between the key *k* and the stegotext would quantify steerability.

---

## Removed Points

These points from the reviews were removed with justification:

- *"The plausibility measure is circular because it uses the same LLM that generated the stegotexts"* — The paper explicitly verifies with Phi‑3 (a different LLM) in Figure 14 (appendix); this criticism is factually incorrect as stated.
- *"The paper does not demonstrate... varied source texts"* — While true as a weakness, the critic claimed this as a fatal issue undermining the title. The title's claim ("LLMs Can Hide Text in Other Text of the Same Length") is demonstrated: the paper successfully hides specific texts. What's missing is *how often* — a major concern but not a title-invalidating flaw.
- *"To strengthen the paper... replace the shipping unfiltered LLMs scenario with a real demonstration or remove it"* — This is a suggestion about scope, not a weakness. The scenario is presented as a thought-experiment application, consistent with the paper's position-paper elements.
- *"No discussion of computational cost"* — The paper states encoding/decoding takes "seconds on a laptop" and provides a smartphone demo. This is sufficient for the claimed efficiency.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that "the paper's core thesis is almost self-evident once stated — which is a hallmark of good ideas" is worth noting as an accurate characterization rather than a weakness.

---

## Suggestions

1. **Broaden the empirical evaluation to match the claims.** The single most impactful improvement would be to take 100–500 natural-language texts spanning the perplexity distribution and report: (a) the fraction that yield stegotexts with log-probability within the real-text distribution; (b) the fraction judged coherent by a second LLM; (c) variation across text lengths (e.g., 50, 100, 200 tokens) and across multiple LLMs (e.g., Llama‑3, Phi‑3, Mistral). This would directly answer "for what fraction of texts does the protocol work?"

2. **Add a human plausibility study.** A small-scale "detect the fake" experiment with human raters would directly validate the claim that stegotexts are indistinguishable from real text.

3. **Quantify steerability.** Report a topic- or style-consistency score (e.g., embedding similarity between the key *k* and the generated stegotext, or a topic-classification accuracy) to substantiate the claim that the protocol allows topic/style steering.

4. **Acknowledge the key overhead explicitly.** Adding a sentence or calculation of effective bitrate (bits per stegotext token, net of the key cost) would give readers a concrete trade-off.

---

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>