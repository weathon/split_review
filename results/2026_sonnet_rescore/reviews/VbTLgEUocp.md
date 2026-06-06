## Summary

*Calgacus* introduces a simple steganographic protocol using Large Language Models: given a text **e** to hide and a secret prompt **k**, the sender records the rank of each token of **e** in the LLM's probability distribution, then generates the stegotext **s** by always selecting the token at that prescribed rank when prompted with **k**. The result is a stegotext of *exactly the same token length* as the hidden message, exactly recoverable by anyone who knows **k** and the LLM. The paper evaluates plausibility via log-probability comparisons against Reddit texts and closes with an original philosophical discussion connecting the protocol to hallucination theory and LLM intentionality.

---

## Strengths

1. **Full-capacity same-length steganography is a genuinely new property.** The protocol deterministically guarantees that the stegotext is exactly as long (in tokens) as the hidden message. As noted in Section 2, prior work (Meteor, Ziegler et al.) does not by design guarantee this symmetry; the paper's claim of novelty on this axis is anchored in the protocol description and Figure 3.

2. **Quantitative plausibility evidence in Figure 4.** The paper compares log-probabilities of 300 stegotexts (100 per three originals) against 1000 real Reddit posts using Llama 3 8b and replicates the key comparison with Phi-3 3.8B (Figure 14 referenced in text). The stegotexts fall within the real-text distribution in every case, concretely supporting the central "plausibility" claim rather than relying on anecdote alone.

3. **Insightful mechanistic explanation of the probability gap.** Section 3 ("Low entropy token choices") identifies and quantifies *why* stegotexts are less probable than originals: rank-1 tokens are "wasted" in high-entropy positions, reducing overall log-probability even though the rank sequence is preserved. Figure 5 operationalizes this with a 1.3k-token Economist article. This explanatory step—not just documenting the gap but accounting for it—strengthens the evaluation.

4. **Concrete deniability argument.** Section 3.1 provides a sender-deniability property with a worked example (Figure 15): a bogus key yields a plausible but different message with log-probability comparable to the original, grounded in the statistical observation from Figure 4 that some stegotexts land near the original's probability.

5. **Original philosophical contribution on hallucinations and intent.** The "Hallucinations as lack of intention" framing in Section 4—hallucination as the reader's inability to ascribe authorial intent rather than mere factual error—is a genuinely novel and well-argued idea that goes beyond protocol description. The Oulipo/Perec analogy is apt and precise.

6. **Steerability demonstrated.** Figure 1 shows that the same hidden message (Roman Republic critique) can be embedded in a culinary recipe or a Caesar eulogy via different **k**, validating the steerability claim.

---

## Weaknesses

### Fatal

None.

### Major

- **Evaluation breadth is too narrow to support the paper's generalization language.** The core empirical evaluation uses three original texts at 85 tokens with one primary model (Llama 3 8b). The abstract states "a message as long as this abstract can be encoded... in seconds" and Introduction mentions "an entire article can be encoded," yet no results at longer lengths appear in the main paper. The claim that stegotexts "fall within the real text distribution" (Section 3) may hold at 85 tokens but whether it holds at 200–500 tokens—the regime actually motivating the paper—is untested in the main text. Three originals is a very thin empirical base for the strong distributional claim.

- **Positioning relative to Zamir (2024) is unresolved.** Section 2 notes that Zamir (2024) "encode[s] the secret message without modifying the response distribution of the LLM"—a strictly stronger security guarantee than Calgacus, which *does* produce a detectably shifted distribution (Figure 4 explicitly shows stegotexts are on average less probable than originals and that LLMs can distinguish them). Calgacus's claimed advantage is the same-length property, but the paper never explains what use case requires same-length encoding but not distribution-preservation, nor does it include any comparison against Zamir on quality, speed, or detection rate. The result is that the most directly competitive prior work—the one most challenging to the novelty claim—goes uncontested experimentally.

### Minor

- **Security analysis remains qualitative where quantitative evidence is feasible.** Section 3.1 establishes that the original text is typically more probable than its stegotexts (Figure 4) and acknowledges that "LLMs can uncover a distinction between original texts and most of their encoded counterparts." But no detection AUC, ROC, or threshold-based accuracy is reported. Since the paper already has log-probability evaluations on two models (Llama 3 8b and Phi-3), deriving a simple threshold classifier accuracy would concretely support or qualify the deniability claims, rather than leaving them at "for some prompts the stegotexts can attain probabilities in the same ballpark."

- **"Full capacity" terminology carries information-theoretic baggage not resolved in the paper.** Section 2 defines "full capacity" as "stegotext and secret message being of the same length." This is explicit, so it is not a fatal overclaim. However, the actual bits-per-token conveyed varies wildly with the entropy of **e** (the hash example in Section 3 shows this clearly), and the paper never quantifies the typical information content of the rank sequence for real texts. A single sentence noting this distinction—or a brief rank-entropy estimate for the Reddit corpus—would prevent readers from over-interpreting "full capacity."

- **The AI safety scenario's threat model has a structural transparency issue.** As described, Act 4 requires the reasoning trace **t** to be transmitted alongside **s** to the user. Since **t** functions as the decryption key, it is sent in the open. The paper presents this as a covert channel, but the company is simultaneously transmitting both the ciphertext (**s**) and the key (**t**) to the user (and by extension, to any monitor inspecting the chatbot's output). A monitor who knows the protocol would have everything needed to decode **u**. The paper does not acknowledge this structural transparency, which somewhat weakens the framing as a "formidable application... with immediate consequences for AI safety." (Note: reasoning traces are sometimes publicly exposed in modern systems, so the scenario is not impossible—but the threat model as written assumes monitors are not aware of the protocol, which is a strong assumption the paper does not state.)

### Trivial

- The paper acknowledges (Limitations, Section 3) that GPU non-determinism may prevent identical logit computation across hardware. This is correctly flagged but worth noting once more in the safety scenario, since the scenario assumes user and company obtain identical logits from the same open-source model on potentially different hardware.

---

## Nice-to-Haves

- **Empirical results at longer text lengths** (200–500 tokens) in the main paper, matching the abstract's motivating claims.
- **A brief quantitative rank-entropy analysis** of the Reddit corpus (average bits-per-token of the rank sequence for typical human-written text at 85 tokens), which would sharpen the "full capacity" claim from a token-count observation into a more principled statement.
- **A minimal head-to-head comparison against Meteor or Zamir** on stegotext quality (log-prob) and speed for the same inputs, to concretely establish where Calgacus sits in the landscape.
- **AUC or accuracy of a log-probability threshold detector** at a fixed false-positive rate, transforming the qualitative security discussion into a quantitative one.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic, Issue 1 (partial): Meteor achieves comparable results.** Removed because Meteor uses arithmetic coding and does not by design produce stegotexts of the same token length as the hidden message—the same-length property is a genuine differentiator not shared by Meteor. The critique that "for a sufficiently long message, Meteor can in principle produce stegotexts of comparable token length" is speculative and asymptotic; it does not undermine the precise same-length guarantee of Calgacus.

- **Harsh Critic, Issue 2 (in part): "Full capacity is an overclaim."** Partially removed. The paper explicitly defines "full capacity" as same-length (Section 2), so it is not an outright overclaim; the term is used by stipulative definition. The legitimate residual concern (information-theoretic content is not quantified) is retained as a Minor weakness.

- **Strength Finder, "Practical AI-safety scenario with worked example" as a primary strength.** Moved here because the threat model has the structural transparency issue noted above (key transmitted openly alongside ciphertext), which prevents this from being an unqualified strength. The scenario is thought-provoking and correctly noted as research-purposes illustration, but the "formidable" and "immediate" framing overstates it.

- **Harsh Critic: "Single most important omission is comparison against prior methods."** Retained in Major but the specific demand for "Meteor or Zamir experimental comparison" is downgraded from "most important omission" to a "nice-to-have," since the paper's scope is explicitly to describe Calgacus and discuss its implications, not to benchmark against all prior methods. The Zamir gap remains Major because Zamir's distribution-preserving property directly challenges the paper's implicit security positioning.

- **Harsh Critic: GPU non-determinism as "serious practical obstacle."** The paper already acknowledges this in Limitations, Section 3: "sender and receiver must run the chosen LLM under identical conditions... This may be a challenge when using different GPU architectures (Shanmugavelu et al., 2024)." Repeated framing as a structural flaw is a strawman against a point the paper explicitly addresses.

---

## Novel Insights

The most genuinely novel intellectual contribution is the proposed reconceptualization of LLM hallucination: not as factual error but as *void of intention*—the reader's inability to trust that what is stated reflects authorial intent affecting reality. The protocol demonstrates this philosophically: a coherent, factually plausible text (the boar recipe) can be the purely mechanical byproduct of encoding a completely unrelated political critique, meaning the recipe's "author" never intended any of its content. This connects steganographic capability to a fundamental question about what reading means in an era of machine-generated text, and is more conceptually original than most technical contributions in the steganography literature.

---

## Suggestions

1. Add one experiment at 200+ token length in the main paper (even a single example with log-probability evaluation), matching the abstract's motivating claim.
2. Report a threshold-detection accuracy (e.g., "at 5% false positive rate, a log-probability classifier distinguishes stegotexts from real texts with X% true positive rate") to make Section 3.1's security claims precise.
3. Clarify in the AI safety play that **t** (the decryption key) is transmitted openly to the user, and briefly discuss whether a monitor who observes both **s** and **t** could trivially decode **u** if they know the protocol—this is an honest limitation that the current text sidesteps.
4. Add a one-paragraph comparison to Zamir (2024): acknowledge the distribution-preservation tradeoff explicitly, and argue what use-cases specifically benefit from same-length encoding even at the cost of detectability.
5. Rename or qualify "full capacity" to avoid importing information-theoretic connotations—e.g., "length-preserving" or "same-length"—or add a single sentence noting that the information content of the rank sequence (not just its token count) varies with source entropy.

---

**Evaluation on axes:**

- **Originality**: The same-length steganographic property is new and cleanly demonstrated. The hallucination-as-void-of-intention framing is original philosophical work. High.
- **Importance of research question**: Covert LLM communication has genuine safety implications; the philosophical contribution on intent and hallucination is broader still. High.
- **Claims well supported**: Main plausibility claim (Figure 4) is supported, but generalizability beyond 85-token single-model regime is asserted more than shown. Moderate.
- **Soundness of experiments**: Correct methodology (same-length constraint for log-prob comparison; multi-model check; ablation on rank distributions), but thin sample (3 originals). Moderate.
- **Clarity of writing**: Excellent—the protocol is described clearly, the discussion is well-structured, the humor and literary references land without obscuring content.
- **Value to research community**: The protocol is simple enough to reproduce and the philosophical framing is thought-provoking for the broader AI safety and NLP communities.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>5</clarity>
<community_value>4</community_value>
</subscores>