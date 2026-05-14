## Summary

This paper presents *Calgacus*, a simple protocol that uses an LLM's token-probability ranks to encode an arbitrary text into another same-length, coherent-looking text, with the original exactly recoverable given a secret prompt key. The key idea is to record the ranks of each token in the original text under the LLM, then generate the cover text by forcing the LLM to select tokens at those same ranks after a different steering prompt. The paper discusses philosophical implications (decoupling text from authorial intent, reframing hallucinations) and sketches an AI-safety scenario where an unfiltered model's answers are smuggled inside a compliant model's responses.

## Strengths

- **Elegant, genuinely novel core protocol.** The idea of using token ranks to achieve "full capacity" steganography (same-length encoding) is simple, clearly described, and implementable in a few lines of code. It reveals a deep tension in LLM text generation between following a probability distribution and encoding external intent. This is the paper's central contribution and it is well-motivated.

- **Empirical plausibility check, though limited in scope.** Figure 4 shows that 100 stegotexts generated per original (three originals, selected at μ, μ−2σ, and μ+2σ of the Reddit log-prob distribution) fall within the log-probability range of 1000 real Reddit posts as judged by Llama 3 8B. This provides baseline evidence that the method can produce texts within the plausibility range of natural text.

- **Principled explanation of the probability gap.** Section 3's "Low entropy token choices" analysis and Figure 5 provide a clear explanation for why stegotexts are systematically less probable than originals: rank-1 tokens occupy a smaller fraction of real-text tokens (~40%) than their per-token probability (~95%) would suggest, so many rank-1 opportunities are "wasted" on low-entropy positions where virtually any continuation looks wrong. This is a nice, self-contained insight.

- **Philosophical discussion of unusual depth and originality.** Section 4 reframes hallucinations as a failure of ascribable intent rather than mere factual inaccuracy, draws connections to the Oulipo literary movement, and uses the protocol to question what it means for an LLM to "know" something. This elevates the paper beyond a pure methods contribution and makes it genuinely thought-provoking.

## Weaknesses

### Fatal
None.

### Major

- **Claims of human indistinguishability are asserted without evidence.** The paper repeatedly states that stegotexts are "opaque to humans" (Abstract, Section 1, Section 3). The sole quantitative evaluation is a univariate log-probability histogram (Figure 4). Overlap in a 1-D log-probability distribution is a weak proxy for human-perceived naturalness — two texts can have similar aggregate log-probability while differing dramatically in local coherence, factual consistency, or stylistic naturalness. No human evaluation, no expert annotation, and no systematic qualitative analysis of failure modes are provided. This is the paper's most significant evidentiary gap, since the core narrative depends on the reader believing the stegotexts are convincingly natural to human readers.

- **Experimental evaluation is narrow for a paper making broad claims.** The quantitative evaluation uses only three original texts of exactly 85 tokens each, all drawn from Reddit. While the selection strategy (μ, μ±2σ) is principled, this sample cannot support the paper's narrative about diverse use cases (political critique, secret manuscripts, product reviews). The paper also analyzes a 1.3k-token Economist article in Figure 5, but only for the rank-frequency analysis, not for stegotext quality evaluation. Broader sampling across text types, lengths, and domains would substantially strengthen the paper.

### Minor

- **Security and deniability claims are qualitatively argued but not quantified.** The deniability argument (Section 3.1) rests on observing that "for some prompts the stegotexts can attain probabilities in the same ballpark as the original" (Figure 4) and references an appendix example (Figure 15). This is a qualitative observation, not a quantitative analysis. There is no estimate of how often a random prompt yields a plausible-looking decryption, no formal deniability model, and the "random string in k" countermeasure against language-model-aided key search is mentioned but never evaluated. Since the paper invokes these security properties explicitly, they should either be supported or appropriately hedged.

- **No comparison with prior LLM-based steganography at comparable capacity.** The paper positions "full capacity" (same-length encoding) as its distinguishing contribution relative to Ziegler et al. (2019), Wu et al. (2024), and Zamir (2024). However, it provides no head-to-head comparison of text quality at comparable payload sizes. While full capacity is a unique property that makes equal-capacity comparison impossible by definition, comparing quality at, say, 50% or 80% of capacity would help readers assess whether the full-capacity property comes at a catastrophic quality cost relative to existing schemes.

- **The "unaligned chatbot" scenario rests on exact model matching.** The scenario (Section 4) requires the user to run precisely the same oLLM under identical conditions as the company. The paper acknowledges this limitation (line 153) but does not discuss how realistic it is for a company to distribute or specify a model whose logits match exactly on the user's commodity hardware. This does not invalidate the scenario as an existence proof, but it limits its practical threat credibility.

### Trivial

- The paper occasionally overstates what the log-probability evidence shows. For example, "fake texts built with our procedure are plausible" (Figure 4 caption) and "Fake texts built with our procedure remain within the plausibility of real texts" conflate log-probability overlap with genuine plausibility. More precise language ("within the log-probability range of real texts") would avoid overclaiming.
- The evaluation uses Llama 3 8B for both generation and log-probability scoring (with Phi-3 as a cross-check in appendix Figure 14). Using the same model to both generate and evaluate risks circularity; the cross-model check with Phi-3 is noted but deserves more prominence.

## Nice-to-Haves

- **Human evaluation of stegotext naturalness.** Even a small-scale study (e.g., 10 raters judging 20 stegotext/real-text pairs on a Likert scale) would substantially ground the "opaque to humans" claim and address the paper's most significant evidentiary gap.
- **A "sanity filter" variant** that rejects stegotexts below a log-probability threshold and retries with a different key. The paper mentions failure modes (the hash example), and this simple extension would improve practical reliability. Discussing or benchmarking it would be valuable.
- **Robustness quantification.** A small experiment measuring decoding error rate under model version mismatch (e.g., Llama 3 vs. Llama 3.1) or precision mismatch (bf16 vs. int8) would calibrate the fragility limitation that the paper already acknowledges.
- **Examples of failure modes** in the main text. The hash example is good, but showing additional cases where stegotexts degrade would give a more honest picture of the method's reliability envelope.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim: "LLMs can uncover a distinction" is unsupported.** REMOVED — the paper explicitly states that LLMs *can* distinguish original from stegotext via probability comparison (Section 3, lines 137-138: "while for a human both the original and fake texts are plausible, generally the original text can be discerned from its stegotexts by picking the most probable one according to a LLM"), and Figure 4 shows exactly this. The harsh critic misread the paper's claim direction.

- **Harsh Critic claim: the fragility issue makes the unaligned chatbot scenario "speculative" and results irreproducible.** REMOVED as framed — the paper explicitly lists identical model conditions as a limitation (line 153) and references prior work on the GPU architecture challenge. The scenario is presented as an existence proof / thought experiment, not as a deployed system. Kept in softened form as a minor weakness.

- **Strength Finder claim: "Deniability is substantiated by the observation in Figure 4."** REMOVED — the deniability evidence is qualitatively argued from Figure 4 overlap, not quantitatively substantiated. This does not rise to the level of a verified strength. The deniability argument is thin (see Minor weakness above).

- **Strength Finder's generic claims about importance.** REMOVED — several strength-finder outputs were generic ("this paper addressed an important problem," "the method is practical") without concrete grounding. Only strengths backed by specific evidence from the paper were retained.

- **Formatting nitpicks from Harsh Critic's section-by-section notes.** REMOVED — the comment about the "iawundemè string example being glib" is a stylistic judgment, not a substantive weakness. The comment about the brute-force attack analysis being "misleading" is partially valid but the paper already notes language-model-aided search (line 160) and proposes the random string countermeasure (line 169); the paper's treatment is thin but not misleading.

- **Harsh Critic: missing references, missing appendix content.** REMOVED per hard rules — appendix stripping is a parser artifact, not an author error.

## Novel Insights

The reviewers' synthesis surfaces an interesting tension: the paper's strongest contribution is conceptual — a simple protocol that demonstrates a deep property of LLMs (the radical decoupling of coherent text from authorial intent) — yet its empirical validation is calibrated for a methods-contribution paper without meeting that bar. The philosophical discussion in Section 4 is unusually rich for an ML venue and arguably represents the paper's real center of gravity. A useful reframing would be to treat this as a "concept paper with empirical demonstration" rather than a "methods paper with philosophical discussion," which would realign reader expectations and make the thin experimental section feel like adequate existence-proof rather than insufficient validation.

## Suggestions

- **Reframe the contribution.** Position the paper as introducing a concept/protocol and exploring its implications, with experiments serving as proof-of-concept rather than comprehensive validation. Tone down "opaque to humans" to "within the log-probability range of real texts" unless human evaluation is added.
- **Add even minimal human evaluation.** A small Mechanical Turk or colleague study (e.g., 5 raters, 20 pairs) would dramatically strengthen the paper's central claim at modest cost.
- **Expand text diversity.** Include stegotexts from at least one non-Reddit domain (e.g., news, product reviews) and one longer-form text to demonstrate generality.
- **Add a failure-mode gallery.** Showing 3-5 examples where stegotexts degrade (alongside the hash example) would improve transparency and help readers understand the method's reliability envelope.
- **Discuss the sanity-filter extension.** Even a paragraph discussing the threshold-and-retry variant would demonstrate awareness of practical deployment considerations.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| `gdZ6J5hZzF` — Sequences of Logits Reveal Low Rank Structure | 7.33 | Accept (Oral) | Much stronger: rigorous theory + extensive experiments + surprising application. Our paper is not at this level. |
| `q4qxtaKVAU` — Early Signs of Steganographic Capabilities | 6.00 | Accept (Poster) | Stronger empirically: systematic multi-model evaluation with error bars and sensitivity analysis. Our paper has a more novel core idea but thinner evaluation. |
| `0kHbD6ad07` — Language Models are Injective | 5.00 | Accept (Poster) | Most similar profile: novel theoretical/conceptual contribution with interesting implications, some experimental validation, but thin spots in evaluation. Comparable level. |
| `YHz6PybFqK` — Hidden Cost of Modeling P(X) | 5.00 | Reject | Different topic but similar score band; our paper's core idea is more novel and elegant. |
| `qF6TyKhc7S` — Majority Bit-aware Watermarking | 4.00 | Reject | Our paper has a stronger conceptual contribution than this methods paper with incremental improvements. |
| `ZujfJpD6as` — Steganographic Jailbreaks | 3.50 | Reject | More experiments but weaker core idea. Our paper's protocol is more elegant and its implications more profound. |
| `X5YiG1YXVT` — Accidental Vulnerability | 2.00 | Reject | Our paper is substantially stronger in originality, clarity, and contribution. |

The paper presents a genuinely elegant and novel protocol with thought-provoking philosophical implications. The central idea is simple enough to be memorable and deep enough to sustain discussion. The evaluation, while adequate as existence-proof, is too thin to support the paper's strongest claims about human indistinguishability, and security claims are argued qualitatively rather than quantified. These weaknesses are addressable but real. The paper lands near the `0kHbD6ad07` (5.00, Accept Poster) anchor — a conceptually novel contribution with interesting implications that would benefit from stronger empirical grounding.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>