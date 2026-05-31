## Summary

*Calgacus* is a steganographic protocol that uses LLMs to embed an arbitrary text *e* inside a different, plausible text *s* of exactly the same token length. The method is elegantly simple: tokenize *e*, record each token's rank in the LLM's probability distribution conditioned on the preceding context, then generate *s* by prompting the LLM with a secret key *k* and selecting tokens according to those recorded ranks instead of sampling. Decoding is the exact reverse. The paper argues this "full capacity" property (stegotext = same length as secret message) is novel, demonstrates it works with 8B open-source models on consumer hardware, evaluates plausibility against 1000 Reddit posts, sketches a security analysis, and discusses philosophical and AI-safety implications—particularly the possibility of hiding unaligned LLM responses inside aligned ones.

---

## Strengths

- **Elegant, genuinely novel protocol with the full-capacity property.** Prior LLM steganography work (e.g., Meteor, Zamir 2024) encodes a small secret payload inside a longer covertext. Calgacus achieves a 1:1 ratio between secret message length and stegotext length, which is a qualitatively different and stronger guarantee. The mechanism is also notably simpler than many competitors.

- **The AI-safety application is concrete and original.** The "unaligned chatbot disguised as aligned chatbot" scenario is described as a complete, step-by-step protocol and illustrated with a real example (gas-meter tampering, Figures 11–12). This makes the stakes tangible in a way that elevates the paper beyond a technical curiosity.

- **Plausibility evaluation is principled.** Comparing the log-probabilities of 300 stegotexts against 1000 Reddit posts under two independent LLMs (Llama 3 8B and Phi-3 3.8B) provides a concrete and reproducible quality signal. The finding that stegotexts land within the real-text distribution, even though they are systematically less probable than their originals, is both useful and well-explained mechanistically (the "low-entropy token choices" paragraph).

- **Deniability result.** The observation that some outlier secret prompts produce stegotexts with log-probabilities in the same ballpark as the original—enabling plausible false keys under coercion—is a non-obvious security feature that is demonstrated concretely (Figure 15).

- **The philosophical discussion on hallucinations and authorial intent is a genuine intellectual contribution.** Reframing hallucination as *lack of ascribable intent* rather than *factual falsehood* is novel and actionable for the ML community's self-understanding.

---

## Weaknesses

### Fatal
None.

### Major

1. **The LLM-detectability problem is a serious security gap that the paper underaddresses.** The paper itself shows that an LLM can reliably rank the original text as more probable than its stegotexts in aggregate (Figure 4). This means an automated detector running candidate stegotexts against a set of candidate originals can distinguish real from fake with better than chance accuracy. The security claim effectively reduces to "humans cannot detect it and automated LLM-based detection is imperfect," but no quantitative detection accuracy is reported, no ROC curves are shown, and no adversarial-detector experiments are run. For a paper whose primary value proposition includes *security*, this is insufficient. The deniability argument partially mitigates this, but relies on a subset of outlier prompts rather than a systematic defense.

2. **Empirical evaluation scope is narrow.** The full-capacity claim is the headline result, yet the evaluation is conducted on only 3 original texts (chosen at μ, μ±2σ), restricted to exactly 85 tokens, using only Reddit posts as the "real text" distribution. Texts from other domains (news articles, academic prose, social media in other languages), and a range of lengths beyond 85 tokens, are not tested. The appendix apparently includes more examples, but the main paper relies on a single length and domain for all quantitative claims. It is unclear whether the protocol degrades for longer messages, for lower-entropy source texts, or for non-English inputs.

3. **The "unaligned chatbot" scenario has an unaddressed covert-channel bootstrapping problem.** In Act 3–5 of the play, the user must already know the secret key *k* = *t* (the reasoning trace), must know the exact LLM version being used, and must know to apply the protocol. The paper does not describe how *k* is transmitted to the user covertly, which is itself a steganographic problem. Without solving this bootstrapping problem, the scenario is incomplete as an AI-safety threat model. The authors acknowledge the identical-GPU-conditions requirement (Shanmugavelu et al., 2024) as a practical challenge but do not assess how brittle this constraint is in practice.

### Minor

1. **No quantitative comparison with prior work.** The claim that full capacity is novel is argued informally. A direct comparison with the encoding efficiency of Meteor or Zamir (2024) on equal-length benchmarks would substantiate this claim.

2. **The plausibility metric is evaluated only on one side.** Log-probability measures how the generating LLM itself rates the text, not how well the stegotext *satisfies the key prompt k*. A stegotext that is "in distribution" overall may still fail to coherently follow the key's style or topic instructions. Human or LLM-judge evaluation of prompt adherence is absent.

3. **Security analysis is informal.** The key-space argument (O(d^|k|)) assumes a random key, but natural-language keys have far lower entropy. No bound on the information revealed about *k* by observing *s* is provided.

### Trivial

- The paper notes that identical GPU hardware is required for matching logits, but does not quantify how often rank mismatches occur across common GPU families in practice.

---

## Nice-to-Haves

- An automated detection experiment with a threshold-based LLM detector (e.g., run a Neyman-Pearson test using log-probability ratios) would quantify the security gap precisely.
- Evaluating at multiple text lengths (e.g., 50, 85, 200, 500 tokens) would establish scalability of the quality guarantee.
- A brief comparison of encoding throughput and per-token quality against Meteor and Zamir 2024 would contextualize Calgacus in the prior art.

---

## Novel Insights

The central insight—that token *ranks* in one LLM generation context are a lossless, portable representation of the text, and can be used as a code to drive generation in a completely different context—is a clean and underexplored observation about the structure of autoregressive language models. The paper's mechanistic explanation for why stegotexts are systematically less probable than originals (the "wasted rank-1" problem at low-entropy positions) is a concrete and generalizable insight into the relationship between token-rank distributions and LLM log-probability. The reframing of hallucinations as a *failure to attribute intent* rather than a *failure of factual accuracy* may prove useful to the alignment and interpretability community as a conceptual tool.

---

## Suggestions

- Add a detection experiment to quantify how reliably an automated LLM-based steganalyzer can identify stegotexts, and compare against human detection rates.
- Evaluate text quality beyond 85-token Reddit posts: include at least two additional domains and at least two additional lengths to support the full-capacity claim.
- Clarify the key-transmission mechanism in the unaligned chatbot scenario or scope the threat model more carefully to avoid overstating the attack's practicality.

---

## Score and Decision

Calgacus is a clean, honest, and genuinely novel contribution. The protocol is simple enough to be immediately reproducible, the full-capacity property is a real advance over prior work, and the AI-safety application is concretely described and thought-provoking. The main weaknesses—an incomplete security evaluation and a narrow empirical scope—are real but do not invalidate the core technical claim, which is well-supported by the experiments that are present. The philosophical discussion, while unusual for a top ML venue, is substantive rather than decorative. The paper brings clear value to the ICLR community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>