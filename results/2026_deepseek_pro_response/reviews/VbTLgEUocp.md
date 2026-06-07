Now I have solid anchors for comparison. Let me finalize my assessment.

**Round 2 anchor comparison:**

- **Hidden in Plain Text (5.00, rejected)**: Directly comparable LLM steganography paper with thorough experiments but novelty questioned. Calgacus has a more genuinely novel protocol and richer discussion, but thinner empirical evaluation. Calgacus is slightly stronger.

- **Semantic Invariant Watermark (5.50, accepted)**: Another novel LLM security protocol. Has broader experimental coverage (multiple datasets, baseline comparisons) but also has gaps. Calgacus has a more elegant core idea and philosophical depth but notably thinner evaluation and no comparisons to prior methods. Calgacus is slightly weaker.

- **Concept Bottleneck LLMs (5.75, accepted)**: Novel interpretability architecture with experiments on multiple tasks and human evaluation. Calgacus has a cleaner protocol and deeper philosophical contribution but lacks the experimental breadth.

- **Plausibly Deniable Encryption (4.80, rejected)**: Very similar in spirit — clever LLM-based security protocol. Calgacus avoids that paper's pitfall of overclaiming security guarantees and has a more elegant protocol.

**Final score: 5.0.** The paper presents a genuinely novel, elegant protocol with thought-provoking implications. However, the empirical evaluation (3 source texts, no human study, no comparison to prior LLM steganography methods) is too thin to support the paper's quality claims, and the paper's hybrid method/position-paper structure creates some tension. These are addressable issues but substantial enough that the paper falls below the acceptance threshold while clearly surpassing the weak-band papers. The core ideas are strong enough to merit eventual publication after revisions.

Now let me write the final review.

---

## Summary
The paper presents Calgacus, a simple and elegant steganographic protocol that uses LLMs to hide an arbitrary text within another coherent, plausible text of the same token length. The method records token ranks when the LLM processes a secret message, then uses those ranks (rather than sampling) to generate cover text from a different prompt. The paper uses this protocol as a springboard for philosophical discussion about intent, hallucination, and knowledge in LLMs.

## Strengths
- **Simple, novel protocol achieving full (1:1) steganographic capacity.** The Calgacus method achieves the counterintuitive property of hiding text within another of identical token length using only standard autoregressive generation repurposed as a deterministic encoding scheme. The recipe format (Section 3) makes the method immediately clear and reproducible.
- **Crisp "low entropy token choices" analysis.** The analysis (Figure 5) provides a non-obvious, quantitative explanation for why stegotexts are systematically less probable than originals despite rank preservation: rank-1 tokens are "wasted" on high-entropy positions where they don't deliver their full probability mass. This is the paper's strongest technical contribution.
- **Cross-model verification.** Using Phi-3 3.8B (a different model from the Llama 3 8B used for generation) confirms the probability gap between real and stegotexts is not an artifact of using the same model for both generation and evaluation.
- **Novel philosophical reframing of hallucination.** Section 4 redefines hallucination as lack of intention rather than factual error, using the Tacitus/Calgacus historical analogy (line 232) to argue that text without attributable intent becomes hallucination regardless of factual content. This insight is genuinely novel within the ML literature and directly motivated by the protocol.

## Weaknesses

### Fatal
None.

### Major
- **Empirical evaluation too thin to support broad quality claims.** The entire quantitative evaluation uses only 3 base texts (chosen at μ, μ−2σ, μ+2σ from 1000 Reddit posts) to generate 300 stegotexts total. This is insufficient to support claims that the method produces consistently "coherent and plausible" output across arbitrary topics (line 9) or that stegotexts are "opaque to humans" (line 43). Three hand-picked source texts cannot establish generalizability. A broader evaluation across diverse source texts, or a human fluency study, would be needed to substantiate these claims.
- **No comparison to existing LLM-based steganography methods.** The related work (line 67) names Meteor (Kaptchuk et al., 2021), Wu et al. (2024), and Zamir (2024) as directly relevant prior methods with different trade-offs (entropy-adaptive encoding, black-box access, distribution-preserving). The paper claims full capacity as Calgacus's distinctive contribution but provides no empirical or systematic qualitative comparison along dimensions of capacity, output quality, key length, or model access requirements. Without this, the reader cannot assess whether Calgacus is a genuine advance or simply a different operating point in a trade-off space.

### Minor
- **"Unaligned chatbot" framing overstates the protocol.** The abstract claims "a company could covertly deploy an unfiltered LLM by encoding its answers within the compliant responses of a safe model" (line 9), but the actual protocol (Section 4, Acts 1-5) requires the user to actively run a decoding procedure using the provided reasoning trace as a key. This is a covert channel requiring user-side cooperation, not fully passive covert deployment. The AI safety concern is genuine but the abstract's framing promises more than the protocol delivers.
- **Deterministic-logit requirement understated.** The paper notes (line 148) that sender and receiver must run identical LLM configurations, but the practical severity is significant: different GPU architectures, quantization, or minor version updates would break the protocol, substantially limiting real-world applicability.
- **Security claim about random key padding lacks analysis.** The claim that "inserting a simple random string in k is enough to nip [search-space reduction attacks] in the bud" (line 164) is stated without any analysis of required string length, impact on stegotext quality (since k now contains non-semantic content), or the attack model being considered.
- **No human evaluation for "plausible to humans" claim.** The paper asserts stegotexts are "opaque to humans" (line 43) and that "for a human both the original and fake texts are plausible" (line 132), but provides only LLM log-probability evidence. A modest human study would significantly strengthen this central claim.

### Trivial
None.

## Nice-to-Haves
- A comparison table across Calgacus, Meteor, Wu et al., and Zamir along capacity, quality, key-length, and model-access axes.
- Reframing the empirical section honestly as a sanity-check existence proof rather than a comprehensive evaluation would better align the paper's structure with its actual contribution.
- Discussion of the edge case where prescribed rank exceeds vocabulary size at a generation step.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic: "The discussion section is a standalone philosophical essay."** This is a genre/structure preference, not a scientific weakness. The hybrid method+position paper format is intentional and valid at ICLR.
- **Harsh Critic: "LLM introduction is too tutorial for ICLR."** Pure style nitpick; the tutorial content (lines 65-66) is brief and accessible, not a substantive flaw.
- **Harsh Critic: Log-probability circularity concern.** The paper partially addresses this with cross-model verification using Phi-3 (Figure 14), weakening this criticism. The retained point about lacking human evaluation captures the remaining concern more precisely.
- **Harsh Critic: "Introduction reads like a position paper; method section reads like a technical note."** Structural preference, not a weakness. The paper's hybrid nature is a feature, not a bug.
- **Strength Finder: "Unaligned chatbot scenario concretizes AI safety implications."** Partially valid but conflicts with the verified overselling weakness; the scenario is interesting and worth keeping as illustrative but the framing is imprecise.

## Novel Insights
The most genuinely novel insight emerging from this paper is the recognition that standard LLM text generation is itself a form of constrained generation — forced to adapt at every step to the outcome of an external random source. Calgacus makes this constraint explicit by replacing random sampling with deterministic rank-following. The fact that the resulting stegotexts remain plausible reveals that LLMs already operate under an extreme constraint satisfaction regime. This observation — that Calgacus's success is unsurprising precisely because standard generation is already a variant of the same constrained process (articulated in "The constraint of chance," line 246) — connects the technical method to the philosophical discussion in a genuinely deep way. The Oulipo/La Disparition analogy (line 244) crystallizes this insight: literature produced under arbitrary constraints suffers from the same difficulty of attributing intent.

## Suggestions
- Expand the text corpus for evaluation beyond 3 source texts, or explicitly reframe the empirical section as a sanity-check existence proof rather than a comprehensive evaluation.
- Add a qualitative or quantitative comparison to at least one existing LLM steganography method (e.g., Meteor) to contextualize the full-capacity contribution.
- Consider a small human study (even 10-20 raters) to validate the "plausible to humans" claim.
- Either provide analysis of the random-key-padding security claim (required length, quality impact) or qualify it more cautiously.

## Score and Decision

**Calibration anchors used across rounds:**

Round 1 (bracketing):
- Sparse Watermarking in LLMs (3.00, rejected) — weaker paper; Calgacus clearly superior
- TrojanRAG (3.40, rejected) — weaker; Calgacus clearly superior
- Hidden in Plain Text (5.00, rejected) — most directly comparable LLM steganography paper; Calgacus has a more novel protocol and richer discussion but thinner evaluation
- Plausibly Deniable Encryption with LLMs (4.80, rejected) — similar spirit; Calgacus avoids overclaiming security and has a more elegant protocol
- Scaling Laws for Associative Memories (7.60, accepted) — rigorous theory paper; Calgacus clearly below in rigor

Round 2 (narrowing):
- Hidden in Plain Text (5.00) — Calgacus slightly stronger due to more novel protocol and philosophical depth
- Semantic Invariant Robust Watermark (5.50, accepted) — another novel LLM security protocol; Calgacus has a more elegant core idea and richer discussion but thinner empirical evaluation; Calgacus slightly weaker
- Concept Bottleneck LLMs (5.75, accepted) — broader experiments with human evaluation; Calgacus has cleaner protocol but weaker empirical support
- Plausibly Deniable Encryption (4.80) — Calgacus clearly stronger
- Representation Geometry (6.75, accepted) — rigorous theory; Calgacus clearly below

**Round 1 bracket: 5.0–6.5. Round 2 narrows to 5.0–5.5.** Calgacus sits between Hidden in Plain Text (5.00, rejected, more experiments but less novelty) and Semantic Invariant Watermark (5.50, accepted, more experiments but also gaps). The thin empirical evaluation (3 source texts) and lack of comparison to prior steganography methods pull it below 5.50. The genuine protocol novelty and philosophical depth keep it above 4.80. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>