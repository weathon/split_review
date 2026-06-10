Now I have enough data to calibrate. Let me finalize the review.

**Round 1 bracket: 5.0–7.0** — clearly above the rejected steganography papers (~4.5–5.0), in the range of accepted papers with mixed reviews.

**Round 2: 5.5–6.5** — comparable to the accepted 6.0 "Predicting Emergent Abilities" paper (novel idea, limited evaluation) and clearly above the rejected 4.8 "Plausibly Deniable Encryption" paper (similar topic but weaker execution). The philosophical contribution pushes it up, while lack of baseline comparisons holds it back.

Let me now write the final review.

---

## Summary

This paper presents *Calgacus*, a steganographic protocol that hides an arbitrary text within a coherent, plausible text of identical token length using an LLM's probability rank structure. The method records the rank of each secret-message token in the LLM's distribution, then generates a stegotext from a different prompt by selecting tokens at those recorded ranks. The paper evaluates plausibility on Reddit posts, discusses security properties including deniability, and offers philosophical arguments about hallucination reframed as "lack of intention," a concrete AI safety threat scenario (unaligned chatbots disguised as aligned ones), and the nature of LLM knowledge.

## Strengths

- **Elegant, minimal protocol with a genuinely novel equal-length property**: The method (lines 96–108) achieves full capacity — stegotext and secret message of identical token length — through a minimal modification of standard autoregressive generation. Prior methods like Meteor use entropy-adaptive bit allocation, Wu et al. require black-box access, and Zamir preserves response distribution but does not achieve equal-length encoding (line 67). The simplicity itself is a contribution: it makes the method practical on 8B-parameter models in seconds on consumer hardware.

- **Well-designed empirical validation with proper controls**: Figure 4 compares log-probabilities of 1000 real Reddit posts against stegotexts, random ASCII strings, and random English word strings at identical token length (85 tokens). The Reddit texts are more recent than Llama 3's training cutoff (line 130), ruling out data contamination. Three source texts at μ, μ−2σ, and μ+2σ each generate 100 stegotexts with varied prompts, demonstrating robustness across the quality spectrum. Cross-model validation with Phi-3 3.8B (Figure 14) shows the distinguishing signal generalizes.

- **Clear mechanistic explanation for the probability gap**: The "Low entropy token choices" analysis (lines 134–146) provides a falsifiable explanation for why stegotexts are systematically less probable than originals despite preserved rank sequences. The Caesar example shows how rank-1 tokens (>95% probability) appear only ~40% of the time in stegotexts (Figure 5), with distributions demonstrably shifted between real and fake texts.

- **Concrete AI safety threat scenario**: The "unaligned chatbot" scenario (lines 174–206) specifies a five-act protocol where a company covertly serves unfiltered LLM responses inside compliant ones, with a worked example (gas meter tampering, Figures 11–12). The observation that "a better alignment of the surface LLM only helps in disguising better unaligned answers" (line 174) is a novel and consequential safety insight.

- **Substantive philosophical contribution grounded in the technical work**: The reconceptualization of hallucinations from "failure of factuality" to "void of intention" (lines 226–236) is argued with specific literary and historical references (Tacitus/Calgacus, Oulipo/Perec's *La Disparition*, Dennett's intentional stance). The observation that standard LLM generation is itself a constrained process ("the constraint of chance," line 246) links the philosophical argument back to the technical method.

## Weaknesses

### Fatal
None.

### Major

- **No comparison with prior steganographic methods on any metric**: The related work (Section 2) discusses Meteor, Wu et al., and Zamir, describing their distinguishing properties. Yet the experimental section contains zero comparisons with any of these methods on plausibility, detection resistance, encoding speed, or capacity. The paper claims Calgacus has "the notable property of having full capacity" (line 67) as its distinguishing contribution, but provides no evidence that prior methods lack this property or that Calgacus is better on any measurable axis. For a methods paper, the absence of any baseline comparison makes it impossible to assess the contribution's relative significance.

- **Security/indistinguishability claims are undermined by the paper's own evidence, and the deniability counterargument is underanalyzed**: The paper acknowledges that "generally the original text can be discerned from its stegotexts by picking the most probable one according to a LLM" (line 132). This directly weakens the steganographic security claim. The paper offers a "deniability" argument (line 166) — that some prompt choices yield stegotexts with probabilities "in the same ballpark" as the original — but this is a narrow statistical observation, not a security guarantee. The paper does not quantify how often deniability holds, does not consider more sophisticated detection strategies (perplexity classifiers, rank-distribution analysis, adversarial LLMs), and the deniability argument rests on visual overlap in Figure 4 and a single example in Figure 15. For a steganography paper, the security analysis is surprisingly informal.

### Minor

- **Limited evaluation scope**: The evaluation is restricted to 85-token Reddit posts evaluated by a single LLM (Llama 3 8b) using only three source texts. Varying text length, domain, and evaluation model would substantially strengthen generalizability claims. The paper acknowledges some limitations (line 148) and delegates analysis to appendices.

- **"Full capacity" claim lacks information-theoretic grounding**: While equal token length is a clear structural property, the paper provides no analysis of actual information throughput (bits per token). When the LLM assigns high confidence to the correct token (rank 1), one position transmits zero bits; when rank is high, more bits are transmitted. An information-theoretic comparison with Meteor's entropy-adaptive allocation would substantiate the "full capacity" claim as a meaningful advantage rather than a structural consequence of the design.

- **No human evaluation of stegotext plausibility**: The claim that stegotexts are "opaque to humans" (line 43) is stated without any human study. The LLM-based log-probability evaluation is informative but does not directly test human perception. Even a small-scale Turing-style test would strengthen this central claim.

### Trivial
None.

## Nice-to-Haves
- A human evaluation study (even small-scale) testing whether people can distinguish real from fake texts.
- Information-theoretic bits-per-token analysis comparing Calgacus with Meteor and other methods.
- Analysis of how stegotext quality varies with text length beyond 85 tokens and across different domains/genres.
- Systematic security analysis: quantifying detection accuracy under various adversarial strategies (different LLMs, perplexity classifiers, rank-distribution analysis).

## Removed Points
These points are flagged to be removed, treat them with caution.
- The harsh critic's assertion that "full capacity" is "misleading" is too strong — the paper clearly defines what it means (equal token length, line 67) and never claims bits-per-token superiority. It is a legitimate design distinction, though incomplete without information-theoretic comparison.
- The critic's concern about the brute-force bound O(d^|k|) being "imprecise" is a minor wording issue — the paper acknowledges the attacker could prune the search space using the stegotext itself (lines 154–164).
- Generic strengths about the paper's writing quality and engaging prose were dropped as not constituting technical contributions for evaluation purposes.

## Novel Insights
The paper's most genuinely novel insight is the philosophical reframing of hallucination as "lack of intention" rather than factual error, grounded concretely in the steganographic protocol's demonstration that LLM text can simultaneously be coherent and free of authorial intent. The connection to Oulipo constrained writing and the observation that standard LLM generation is itself a constrained process ("the constraint of chance") are thought-provoking and well-argued. The AI safety scenario — that better alignment of the surface LLM only helps disguise unaligned content — is a consequential observation that extends beyond the specific protocol.

## Suggestions
- Add at least one baseline comparison with Meteor or another LLM-based steganographic method on plausibility and detection resistance using the same evaluation setup.
- Quantify the deniability property: what fraction of prompts yield stegotexts statistically indistinguishable from originals? How does this vary with prompt quality and LLM size?
- Add information-theoretic analysis of actual bits-per-token capacity to ground the "full capacity" claim.
- Expand evaluation to vary text length, domain, and LLM model.
- Consider a human evaluation study to support the "opaque to humans" claim.

## Calibration Report

**All retrieved anchors across rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Sparse Watermarking in LLMs | jbfDg4DgAk | 3.00 | 1 | Weaker method, less novelty, narrower contribution |
| TextEconomizer | DsMxVELk3K | 3.00 | 1 | Unrelated domain, weaker contribution |
| Jailbreaking with Language Games | BeOEmnmyFu | 2.50 | 1 | Unrelated, weaker paper |
| Mind Scramble | KBixkDNE8p | 3.00 | 1 | Unrelated, weaker contribution |
| Steganographic Collusion in LLMs | urQi0TgXFY | 5.00 | 1 | Similar topic but Calgacus has cleaner method and more original philosophical angle |
| Plausibly Deniable Encryption with LLMs | 7suavRDxe8 | 4.80 | 1 | Very similar topic; Calgacus is simpler, better validated, more compelling philosophically |
| End-to-End LLM Watermarking | 0KHW6yXdiZ | 5.25 | 1 | Related (watermarking); Calgacus is more novel in design |
| Semantic Invariant Robust Watermark | 6p8lpe4MNf | 5.50 | 1 | Watermarking paper; less topically similar |
| Lightweight Deep Watermarking | j7b4mm7Ec9 | 7.60 | 1 | Image watermarking; accepted with high scores but different domain |
| LLM-SR: Scientific Equation Discovery | m2nmp8P5in | 8.00 | 1 | Accepted paper with clear, well-validated contribution — Calgacus is below this |
| Alice in Wonderland | EJgxMsiAO9 | 5.20 | 2 | Well-executed but limited scope; Calgacus has more novelty |
| Predicting Emergent Abilities | lDbjooxLkD | 6.00 | 2 | Comparable novelty level, similar evaluation limitations — good anchor |
| Dynamic Demonstrations Controller | qH8ADnIVII | 5.75 | 2 | Moderate contribution; Calgacus has more depth |
| Multilingual Trolley Problems | VEqPDZIDAh | 7.25 | 2 | Large-scale evaluation with philosophical implications — Calgacus's philosophical contribution is more original but technical evaluation is weaker |
| Uncovering Gaps in Subjective Language | gye2U9uNXx | 7.50 | 2 | Well-validated paper with novel insights — above Calgacus |
| DailyDilemmas | PGhiPGBf47 | 7.25 | 2 | Large-scale evaluation — above Calgacus in rigor |

**Round 1 bracket: 5.0–7.0** — Calgacus is clearly above the rejected steganography/watermarking papers (3.0–5.25) and below well-accepted papers with strong evaluation (7.25+).

**Round 2 bracket: 5.5–6.5** — Calgacus is most comparable to the "Predicting Emergent Abilities" paper (6.0, accepted with mixed reviews): both have a novel core idea, limited evaluation, and genuine but incomplete contributions. Calgacus has a more original philosophical contribution but weaker experimental scope.

**Final score: 6.0** — The paper offers a genuinely novel and elegant method paired with thought-provoking philosophical insights and a concrete AI safety scenario. These real strengths push it above rejected papers in the same domain. However, the complete absence of baseline comparisons against prior steganographic methods, the informal security analysis partially contradicted by the paper's own detection results, and the limited evaluation scope (single domain, length, and model) prevent it from being a clear accept. The score reflects a borderline paper with a strong core idea that needs more rigorous technical evaluation to support its claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>