Now I'll synthesize the final consolidated review. Let me go through the harsh critic's points systematically against the paper, then write the review.

---

## Summary

This paper presents *Calgacus*, a protocol that encodes a text into another text of identical token length using an LLM's token probability ranks. The method records the rank of each token in the hidden text under the LLM's own probability distribution, then generates a new text from a secret prompt by selecting tokens at those same ranks. This achieves full capacity (1:1 length ratio) in generative steganography, with steerable cover text. The paper demonstrates that stegotexts fall within the real-text log-probability distribution (Figure 4), provides a mechanistic explanation for the probability gap between originals and stegotexts (Figure 5), and illustrates a concrete AI-safety scenario where an aligned chatbot's responses encode uncensored answers from an unfiltered model (Figures 11-12).

---

## Strengths

- **Novel full-capacity steganographic protocol**: The core mechanism — repurposing token ranks from one generation context to constrain generation under another — is genuinely elegant and, to the authors' and reviewers' knowledge, novel. Achieving 1:1 length ratio between hidden message and stegotext is a notable property not attained by prior generative text steganography methods (Section 2).

- **Quantitative evidence of stegotext plausibility**: The evaluation in Figure 4 shows that stegotexts constructed from three diverse source texts (chosen at μ, μ−2σ, μ+2σ of the real-text distribution) fall within the log-probability range of 1000 real Reddit posts. This is further corroborated using a different LLM (Phi-3, Figure 14), directly supporting the claim that stegotexts are not obviously fake by LLM standards.

- **Mechanistic insight into the probability gap**: The "Low entropy token choices" analysis (Figure 5) provides a clear, non-obvious explanation for why stegotexts are systematically less probable than their originals: rank-1 tokens (which carry the bulk of probability mass) are "wasted" on low-entropy contexts because their availability is determined by the hidden text's rank distribution, not by the generating context's entropy.

- **Practical and reproducible**: The method works on consumer hardware (RTX 4070 laptop) with quantized 8B-parameter models, with encoding/decoding in seconds. A working demo and implementation are provided. The appendices contain useful practical findings including rank inversion (Figure 9), model quality ablation (Figure 8), and domain-dependence analysis (Figure 7).

- **Concrete and thought-provoking AI-safety scenario**: The "Shipping unfiltered LLMs without really shipping them" play (Section 4, Figures 11-12) demonstrates how an aligned, lightweight open-source LLM can deliver uncensored answers from a powerful unfiltered private model while exposing only compliant surface text. This is a genuinely novel concern distinct from standard jailbreak or alignment-failure modes.

---

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed scope in the abstract and introduction vs. acknowledged limitations**: The abstract claims the protocol can hide "a meaningful text" and Section 1 says "arbitrary meaningful text" can be encoded. However, the method's mechanism (Section 3, "When the stegotext *s* sounds like a real text") and Appendix A.1 make clear that stegotext quality depends on the LLM's ability to predict the hidden text: when *e* is out-of-distribution (Romanesco dialect, cryptographic hashes), the output is garbled. The paper *does* acknowledge this dependency (e.g., "If *e* is difficult to guess for the LLM, ranks will be high and *s* will be gibberish"), but the abstract and introduction frame the capability in unqualified terms. The class of text that works is genuinely broad (English prose, code, chess notation, Spanish) but the headline framing should be tempered. This matters because readers may take away a stronger capability claim than the method delivers.

- **Security and deniability claims lack systematic evidence**: The deniability argument rests on a single hand-constructed example (Figure 15). While this demonstrates *existence* of a bogus key yielding a plausible alternate message, there is no quantification of how reliably this property holds — what fraction of stegotexts admit such a key, at what computational cost, and whether an adversary who knows the protocol could distinguish real from bogus keys by other means (e.g., checking whether the revealed *e* is itself predictable by the LLM). Similarly, the security analysis (Section 3.1) is informal and does not quantify the effective key space after accounting for the natural-language constraint on *k*. The paper acknowledges some of these gaps ("the feasibility of such an approach is unclear and remains an open research question") but then draws conclusions ("this observation evidences that our method provides deniability") that outpace the evidence. These claims underpin the paper's most attention-grabbing applications (the aligned/unfiltered LLM scenario, political censorship use-case).

### Minor

- **Limited evaluation diversity**: The main quantitative evaluation (Figure 4) uses only 3 original texts (chosen at μ, μ−2σ, μ+2σ from the Reddit distribution) to produce 100 stegotexts each. While the selection strategy is thoughtful, 3 source texts cannot fully characterize the method's behavior across different hidden-text types. The appendix provides qualitative examples across domains (Figure 7: chess, code, Romanesco) but no quantitative diversity evaluation. The paper would be strengthened by measuring stegotext quality across a wider range of hidden-text types with varying predictability.

- **Probability gap and its steganalysis implications not fully explored**: The paper notes that stegotexts are consistently less probable than originals (Figure 4, Figure 14) and explains the mechanism (Figure 5), but does not analyze whether this gap is exploitable for steganalysis — i.e., whether an observer who only sees the stegotext (without the original for comparison) could detect it as steganographic. The "Low entropy token choices" analysis itself suggests a potential signature (systematic underuse of top-rank tokens), but the paper does not discuss whether this creates a detectable statistical pattern against a baseline of natural cover text.

### Trivial
None.

---

## Nice-to-Haves

- A quantitative characterization of the relationship between the hidden text's average rank and the stegotext's log-probability would help practitioners predict whether their message will produce acceptable output.
- Comparison with other generative steganography methods (e.g., Meteor, Zamir 2024) on capacity-distortion trade-offs would help contextualize when full capacity is worth the quality cost.
- Discussion of potential defenses against the unfiltered-LLM scenario — e.g., could a platform detect that a response doubles as a rank sequence for generating harmful content?

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The method does not actually hide arbitrary meaningful text — it hides only text the LLM can predict well. This invalidates the paper's core claim."** — REMOVED. The paper explicitly acknowledges this limitation in Section 3 ("When the stegotext *s* sounds like a real text") and Appendix A.1. The tension between the abstract's "meaningful text" claim and the acknowledged limitation is real, but the paper does not hide it; moving this to a softened major weakness about overclaiming rather than a fatal flaw.

2. **Various demands for formal security models and missing experiments on detectability by a steganalysis-aware observer** — MOVED TO NICE-TO-HAVE. The paper explicitly declines to adopt a formal steganographic model (Section 2: "we will avoid building a palace on the sand, and not frame our method in a formal model of steganography"). Demanding formal security analysis contradicts the paper's stated scope. The suggestion about steganalysis evaluation is reasonable but is a nice-to-have, not a core requirement for a paper introducing a novel protocol.

3. **Complaints about Reddit posts as "real text" being potentially LLM-generated** — REMOVED. This is speculative and generic; most steganography papers use publicly available text corpora as cover-text proxies without exhaustive provenance verification. The dataset is cited (Trimness8, 2025) and the paper notes the texts are "more recent than Llama 3 and therefore cannot appear in its training corpus."

4. **Demand for larger-scale experiments and more models** — WEAKENED (partially moved to Minor). The paper provides ablations across 6 model sizes (Appendix A.2, Figure 8) and evaluates cross-model generalization (Phi-3, Figure 14). The core evaluation is adequate as a proof-of-concept for the protocol.

5. **"The philosophical discussion is largely disconnected from empirical grounding"** — REMOVED. The discussion section (Section 4) is explicitly a discussion and does not claim empirical support. It engages with conceptual questions about intentionality, hallucination, and LLM knowledge that the protocol naturally raises. Creative philosophical discussion is a legitimate component of a paper, particularly one that explicitly positions itself as raising questions about the nature of LLM-generated text.

6. **"The connection to hallucinations as 'lack of intention' is interesting but the argument's validity does not depend on the protocol"** — REMOVED. This is a matter of taste; the paper uses the protocol to *motivate* and *illustrate* a conceptual reframing of hallucinations. It does not claim the protocol is necessary for the argument.

7. **Strength Finder: "Thorough treatment of robustness factors"** — WEAKENED. While the appendices contain useful ablations, calling them "thorough" overstates the case given the small scale of some analyses.

---

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation emerging from the reviews is the tension between the protocol's steerability and its detectability. The method allows the cover text's topic and style to be freely chosen via the prompt *k*, which has significant practical benefits (e.g., tailoring the cover to a target platform). However, the very mechanism that enables this — decoupling the generating context from the text being encoded — also creates the probability gap that the paper documents. This is not just a bug but a structural feature: any protocol that preserves full capacity while decoupling surface text from hidden content will face the same tension, because the hidden text's token ranks are sampled from one distribution while the generating context imposes a different distribution. This suggests a fundamental capacity-stealth trade-off in generative steganography that the paper implicitly identifies but does not fully formalize.

---

## Suggestions

- Revise the abstract and introduction to accurately bound the method's capabilities: replace "arbitrary meaningful text" with phrasing that acknowledges the LLM-predictability requirement (e.g., "text within the LLM's modeling distribution").
- Add a brief quantitative analysis (even a scatter plot) relating the hidden text's average rank to the stegotext's log-probability, which would give readers a practical diagnostic tool.
- The deniability section should either be significantly strengthened with a systematic evaluation or its claims should be toned down to match the current evidence level (single example = existence proof, not established property).
- Consider discussing whether systematic underuse of rank-1 tokens (Figure 5) could serve as a steganalysis signal, even if only qualitatively.

---

## Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `q4qxtaKVAU` — "Early Signs of Steganographic Capabilities in Frontier LLMs" | 6.0 (Accept Poster) | More thorough evaluation across multiple models and settings; Calgacus has a more novel core mechanism but weaker empirical support. The 6.0 paper's evaluation is more systematic. |
| `6cEPDGaShH` — "Invisible Safety Threat: Malicious Finetuning for LLM via Steganography" | 6.0 (Accept Oral) | Strong practical demonstration with multiple models and a clear attack pipeline. Calgacus is comparably novel in concept but less thorough in evaluation and has overclaiming issues the 6.0 paper does not. |
| `ZujfJpD6as` — "Hiding in Plain Sight: A Steganographic Approach to Stealthy LLM Jailbreaks" | 3.50 (Reject) | Had fundamental problems: overclaimed results that a reviewer could not replicate, low-quality jailbreak outputs, and fusion of known techniques. Calgacus is clearly stronger — its method is genuinely novel and demonstrably works. |
| `9u8HFU6ioO` — "The Coding Limits of Robust Watermarking for Generative Models" | 3.50 (Reject) | Theoretical paper; not directly comparable. Calgacus has more practical novelty. |
| `YHz6PybFqK` — "The Hidden Cost of Modeling P(X): Membership Inference Attacks" | 5.0 (Reject) | Different topic area but similar in having a clear idea with somewhat limited evaluation scope. Calgacus has a more novel core contribution. |
| `TVSPV6D0co` — "Fast, Secure, And High-Capacity Image Watermarking" | 4.67 (Reject) | Image domain, not directly comparable. Had strong results but evaluation concerns. |
| `pAeEzS4LwS` — "Catch-22: Pareto Frontier for Detectability and Robustness in LLM Watermarking" | 2.67 (Reject) | Theoretical work with fundamental issues; Calgacus substantially stronger. |

**Calibration judgment**: The paper is clearly above the 3.50 StegoAttack paper (which had replicability issues and limited novelty) and below the two 6.0 steganography papers (which had more thorough evaluation). The core idea is genuinely novel and elegant, the method demonstrably works, and the AI-safety implications are thought-provoking. However, the overclaiming in the abstract/intro, the single-example deniability evidence, and the limited evaluation diversity pull the score down. Positioned at the high end of the marginal-accept range.

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>