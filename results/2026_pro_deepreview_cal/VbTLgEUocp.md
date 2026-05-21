Now I have a good calibration picture. Let me synthesize the final review.

**Bracket assessment after Round 1**: The paper sits somewhere between the middle anchors (4.75–5.5), where evaluation-driven steganography/watermarking papers cluster, and the strong anchors (7.0–8.0), which demand thorough empirical grounding. The "Plausibly Deniable Encryption with LLMs" (4.80) is closest in spirit — clever LLM-based encoding idea with weak crypto formalism — but Calgacus is clearly stronger in method clarity and quantitative evidence. The "Hidden in Plain Text" (5.00) shares the steganography topic but has weaker novelty and more evaluation gaps. At the upper end, "Managing Diffuse Risks" (7.00) has formal problem definition plus strong empirical results that Calgacus lacks. My initial bracket: **5.5–7.0**.

**Round 2 narrowing**: Reading "Safety-Tuned LLaMAs" (6.00), which has solid but expected results plus comprehensive evaluation — Calgacus has a more novel idea but thinner evaluation. Reading "Plausibly Deniable Encryption" (4.80) confirms Calgacus is clearly better. Reading "Managing Diffuse Risks" (7.00) confirms Calgacus is clearly below it on evaluation rigor. Reading the middle steganography paper "Hidden in Plain Text" (5.00) confirms Calgacus is above it on novelty and clarity.

**Final calibration**: The paper is closest in overall quality to "Safety-Tuned LLaMAs" (6.00) — both have clear contributions with some evaluation limitations, but Calgacus compensates with higher originality and thought-provoking discussion. Score: **6.0**, Accept.

---

## Summary

This paper presents Calgacus, a simple protocol that uses an LLM's token probability ranks to encode an arbitrary text into a different, coherent text of the same token length. The receiver who knows the secret prompt key can perfectly recover the hidden message. The paper explores implications for AI safety, including a scenario where an aligned chatbot covertly transmits unfiltered answers, and offers a philosophical reframing of LLM hallucinations as a "void of intention" rather than factual error.

## Strengths

- **Novel full-capacity steganography.** The protocol achieves equal token length between stegotext and hidden message — a "full capacity" property that distinguishes it from prior generative steganography methods which typically expand message length. The method is cleanly described (Section 3) and immediately reproducible from the recipe given.

- **Demonstrated practical feasibility on modest hardware.** The paper shows that Llama 3 8B — an open-source, modestly-sized model — suffices to encode and decode messages in seconds on consumer hardware. Figure 4 provides quantitative evidence that stegotexts fall within the log-probability distribution of real Reddit texts, separating cleanly from random baselines.

- **Thought-provoking implications for AI safety and trust.** The "Shipping unfiltered LLMs without really shipping them" scenario (Section 4) is a concrete, step-by-step illustration of how the protocol could undermine safety alignment. The philosophical discussion redefining hallucinations as a lack of trust in authorial intent (rather than factual error) is genuinely insightful and directly grounded in the protocol's mechanics.

- **Well-written and engaging.** The paper is clear about its method, candid about limitations (e.g., the hash example on p. 4 showing when the method produces gibberish), and the prose effectively draws connections between the technical contribution and broader questions about LLM knowledge, intention, and trust.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient empirical support for the "plausible to humans" claim.** The central empirical claim is that stegotexts are "plausible" and that "for a human both the original and fake texts are plausible." This is supported by (a) three curated examples in figures and (b) a log-probability comparison of three Reddit posts (each encoded 100 times) against a reference distribution of 1000 real texts (Figure 4). Log-probability under a single LLM is an acknowledged proxy (the paper itself notes its defects, line 133), and three secrets — deliberately chosen at μ, μ−2σ, and μ+2σ of the real distribution — is a narrow test. There is no human evaluation, no perplexity assessment under a different model family, and no systematic exploration of how stegotext quality degrades as secret entropy increases. The conclusion may be correct, but the present data do not fully warrant the strength of the claim in the abstract ("high-quality results").

- **Qualitative-only security and deniability analysis.** The deniability argument — that a sender can present a bogus key yielding a plausible alternative message — is central to the "Trojan horse" framing and the erosion-of-trust thesis. However, it is supported by only a single example (Figure 15, referenced from the appendix) and aggregate observation that some stegotexts have probability comparable to originals. No systematic experiment is provided to quantify how often such decoy messages exist or what probability gap can be expected. While the paper does not claim formal security (it explicitly notes the attack feasibility is "an open research question," line 169), the deniability discussion in Section 3.1 asserts conclusions ("this observation evidences that our method provides deniability") that the evidence does not fully support.

### Minor

- **The equal-length symmetry claim needs tighter qualification.** The paper highlights that the stegotext and hidden message share the same token length and calls this "full capacity," using it to argue that "this symmetry prevents one from establishing at first sight which text is authentic." While the paper does qualify this by showing failure cases (hashes, high-entropy secrets), the symmetry argument conflates token-count equality with semantic parity. Two texts of equal token length can carry vastly different amounts of information, and the stegotext's style is controlled by an arbitrary prompt k, making side-by-side comparison a somewhat contrived scenario. The discussion of when equal-length matters and when it does not could be sharper.

- **The "unaligned chatbot" scenario is a thought experiment, not an empirical demonstration.** The paper presents this as "a real example" but the core claim — that the oLLM can assign sufficiently low ranks to the uncensored answer u — is not systematically tested. Whether an aligned model consistently produces low ranks for harmful content it was trained NOT to generate is an important empirical question that remains open.

### Trivial

- None.

## Nice-to-Haves

- A modest human evaluation (e.g., showing raters a mix of original texts, stegotexts, and standard LLM continuations, asking them to rate coherence) would directly strengthen the plausibility claim.
- A scatter plot of stegotext quality vs. secret entropy across a more diverse set of secrets (news articles, code, lyrics, technical docs) would clarify the method's practical limits.
- A simple heuristic experiment for deniability (e.g., searching for bogus keys via random perturbation and reporting the fraction where a decoy with comparable probability is found) would sharpen the security analysis.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Harsh Critic's "no comparison with existing methods on embedding rate or output quality"**: The paper clearly states its contribution relative to prior work (Section 2, line 72) and the full-capacity property is a qualitative differentiator. Quantitative comparison with methods that do not share this property would be apples-to-oranges. REMOVED.

- **Harsh Critic's "the writing occasionally overreaches and could be trimmed"**: This is a stylistic preference, not a substantive weakness. The paper's essayistic style is a feature of its position-paper nature, not a bug. REMOVED.

- **Harsh Critic's "the reader must take on faith that this works for arbitrary political statements"**: The paper demonstrates the method with concrete examples and explicitly discusses limitations and failure cases. No method paper demonstrates operation on "arbitrary" inputs. REMOVED as scope creep.

- **Strength Finder's "security analysis in Section 3.1 demonstrates deniability"**: Overstates the evidence — only one example is shown. This was moved to a weakness instead. REMOVED as a strength.

- **Strength Finder's generic framing around "important problem" / "interesting question"**: These are not concrete strengths grounded in paper content. REMOVED.

## Novel Insights

The most original synthesis to emerge from the reviews is the recognition that Calgacus is simultaneously a technical contribution and a philosophical intervention. The protocol's simplicity — it is essentially the standard autoregressive generation algorithm with rank-based token selection instead of sampling — means it speaks to the nature of LLMs at large, not just to steganography. The paper's strongest insight is that the distinction between "generating text that conveys intent" and "generating text that satisfies an external constraint" collapses under this protocol, since every token in standard LLM generation is already constrained by the outcome of sampling from the distribution. This reframes LLM text as inherently a "constraint satisfaction problem" rather than an "intention transmission" problem, which genuinely advances our understanding of what LLM-generated text is.

## Suggestions

- Add even a small-scale human evaluation (50–100 ratings) to directly support the claim that stegotexts are plausible to humans. This is the single highest-leverage improvement.
- Expand the secret text diversity beyond Reddit posts and produce a figure showing how stegotext log-probability varies with secret entropy — this would give readers a practical map of when the method works.
- Either strengthen the deniability analysis with a systematic experiment or temper the deniability claims in Section 3.1 to match the current evidence level.
- Consider repositioning the paper slightly: the method and its implications are strong enough to carry the paper even if the plausibility and security claims are more modestly stated.

## Score and Decision

**Anchor comparison summary:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jbfDg4DgAk.md` (Round 1, score 3.00): Sparse Watermarking — much weaker contribution, rejected. Calgacus is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/urQi0TgXFY.md` (Rounds 1+2, score 5.00): Hidden in Plain Text (steganographic collusion) — closest topical match. Calgacus has a cleaner, more novel method but similarly thin evaluation. Calgacus is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7suavRDxe8.md` (Round 2, score 4.80): Plausibly Deniable Encryption with LLMs — similar "clever LLM encoding idea, weak formalism" profile. Calgacus has better evaluation and clearer contribution. Calgacus is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gT5hALch9z.md` (Round 2, score 6.00): Safety-Tuned LLaMAs — solid empirical paper, somewhat expected results. Calgacus has higher originality but weaker evaluation. Comparable quality for different reasons.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/keu6sxrPWn.md` (Round 2, score 7.00): Managing Diffuse Risks — stronger on formalism and empirical results. Calgacus is clearly below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Bo62NeU6VF.md` (Round 1, score 8.00): Backtracking — excellent method with comprehensive evaluation. Calgacus is clearly below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/syThiTmWWm.md` (Round 1, score 7.75): Cheating Benchmarks — clever finding with thorough evaluation. Calgacus is below this.

**Round 1 bracket**: 5.5–7.0. **Round 2 narrowed**: the paper lands closest to the Safety-Tuned LLaMAs anchor at 6.00 — comparable overall quality with a different strength/weakness profile (higher originality, thinner evaluation). Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>