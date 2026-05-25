Now I have a thorough understanding of the paper and can vet each reviewer claim against the actual text. Let me compose the consolidated review.

## Summary

This paper presents *Calgacus*, a steganographic protocol that uses an autoregressive LLM to encode an arbitrary secret message into a different, coherent cover text of exactly the same token length. The method is simple: record the rank of each token of the secret message in the LLM's probability distribution, then generate a new text from a separate prompt by selecting tokens at those same ranks. The paper demonstrates that the resulting stegotexts fall within the log-probability distribution of real human-written texts (1000 Reddit posts), shows why they are systematically less probable than originals despite preserving ranks ("Low entropy token choices"), discusses a security model based on key secrecy with deniability, and explores philosophical implications about authorial intent, hallucination, and LLM knowledge.

---

## Strengths

1. **Full-capacity (same-length) steganography is a genuinely novel property.** Prior LLM-based steganography methods (Ziegler 2019, Kaptchuk/Meteor 2021, Zamir 2024) encode bits at variable rates or alter the token distribution. Calgacus is the first protocol to produce a stegotext exactly as long as the hidden message — a crisp and non-obvious property directly following from the rank-preservation mechanism (Section 3, Figure 3). This makes the hiding and revealed texts symmetrical, which the paper rightly identifies as qualitatively different from prior work.

2. **Quantitative evidence that stegotexts fall within the real-text plausibility distribution.** Figure 4 plots the LLM-assigned log-probabilities of 1000 real Reddit posts (85 tokens), 3×100 stegotexts fitted to the same length, and random baselines. The stegotexts lie entirely inside the distribution of real texts, while random strings do not. This is concrete, reproducible evidence that the protocol can generate cover texts indistinguishable by an LLM-based plausibility measure.

3. **Clear explanation of the probability gap between originals and stegotexts.** The "Low entropy token choices" analysis (Section 3, Figure 5) is an insightful technical contribution. It explains why stegotexts are systematically less probable than originals despite preserving ranks: low-entropy tokens (e.g., "Caesar" after "…Gaius Julius") have near-certain probability in normal generation, but rank-1 tokens in the stegotext occur at the frequency of rank-1 tokens in the secret message (~40%), which is far lower. This deepens understanding of the protocol's behavior and limitations.

4. **Concrete AI-safety threat scenario.** The "Shipping unfiltered LLMs without really shipping them" scenario (Section 4, Figures 11–12) provides a concrete, step-by-step play showing how an aligned open-source LLM could serve as a carrier for an unaligned model's output. This connects the technical protocol to pressing safety concerns and grounds the discussion in a tangible use case.

5. **Elegant simplicity and accessibility.** The method is described as a short recipe requiring only access to LLM logits, a secret key, and a single forward pass per token. It works with open-source 8B models on consumer hardware — no fine-tuning, no auxiliary model, no complex sampling scheme.

---

## Weaknesses

### Fatal

None. The core protocol is sound, the demonstration works, and no verified error invalidates the central technical contribution.

### Major

1. **The identical-logit requirement is a critical practical barrier for the paper's main application scenario, and it is not evaluated.** The paper acknowledges (Limitations, Section 3) that "sender and receiver must run the chosen LLM under identical conditions, performing the same approximations and obtaining identical logits" and notes this "may be a challenge when using different GPU architectures." For the "shipping unfiltered LLMs" scenario — arguably the paper's most impactful use case — the user must decode on their own machine, where logits will differ across GPU architectures, CUDA versions, inference engines, and floating-point precision. A single diverging token rank causes the entire tail of the decoded message to become garbage (autoregressive error propagation). The paper provides no evaluation of this sensitivity, no mitigation strategy (e.g., deterministic inference, logit quantization, error-correcting codes), and no feasibility argument. This substantially weakens the showcased application, though it does not invalidate the protocol as an idealized construction.

2. **Experimental evaluation is narrow relative to the breadth of the claims.** The paper states sweeping consequences — "radical decoupling of text from authorial intent," "further eroding trust in written communication," raising "urgent questions for AI safety" — but the experiments are a proof-of-concept on a single scale:
   - **Three original texts** (each 85 tokens), drawn from one Reddit dataset (1000 posts).
   - **One LLM** (Llama 3 8B) for the main experiment, with a cross-validation check on Phi-3 3.8B (Figure 14).
   - **No human evaluation.** The paper asserts stegotexts are "opaque to humans" (Section 1 outline) but provides no human study — the plausibility evidence is entirely an LLM-based proxy, which raises a circularity concern given that the method itself uses an LLM.
   - **Single text length** (85 tokens). The paper claims "an entire article can be encoded" but gives no evidence for longer texts where the probability product decays and rank-error accumulation compounds.
   
   The core claim that Calgacus produces plausible cover texts *is* supported by Figure 4, but the gap between this evidence and the paper's rhetorical framing is substantial.

3. **No empirical comparison against prior LLM steganography methods.** The Related Work section explicitly cites Ziegler et al. (2019), Kaptchuk et al. (2021, Meteor), and Zamir (2024) and characterizes the contribution as "full capacity." Yet there is zero empirical comparison — no table of capacity (bits/token), no comparison of stegotext quality under comparable conditions, no decoding-error analysis. Without this, it is impossible for a reader to assess whether Calgacus is better, worse, or merely different from the state of the art.

### Minor

1. **The claim that stegotexts are "opaque to humans" is unsupported.** The paper states this as a fact (Section 1 outline, "While remaining opaque to humans…") but provides no human study. The LLM-based plausibility measure (Figure 4) is a useful proxy but does not establish human indistinguishability. A small user study would directly strengthen the paper's central argument.

2. **No quantitative runtime measurements.** The abstract and introduction claim that "a message as long as this abstract can be encoded and decoded locally on a laptop in seconds." The method is indeed efficient in principle, but no wall-clock timings are reported. For a methods paper claiming efficiency, this is a straightforward gap.

3. **The security analysis is incomplete in several respects.** (a) The random-string mitigation for key-guessing attacks is presented as "enough to nip it in the bud," but the paper simultaneously calls the feasibility of key-reduction attacks "an open research question" — the mitigation claim would benefit from a concrete analysis (entropy of the random string, overhead on key length). (b) The deniability argument (Figure 15, some stegotexts match the original's probability) is interesting but rests on a small number of examples without a systematic characterization of how often this occurs across keys and texts.

4. **The hallucination and intentionality discussion, while thought-provoking, is loosely attached to the experimental core.** It reads as a philosophical essay that follows from the *existence* of the protocol rather than from the experiments. This creates a genre mismatch: methods readers will find the evaluation insufficient, while position-paper readers may find the arguments under-evidenced. The discussion could be strengthened by connecting it to the established hallucination literature and by providing empirical evidence (e.g., reader perception studies).

### Trivial

- The hash failure example demonstrates that the method can produce incoherent output for high-entropy secrets, but no systematic failure analysis (rate of failure across text types, entropy thresholds, LLM quality) is provided.
- The paper does not analyze robustness of stegotexts to perturbations (re-tokenization, minor editing), though this is outside the protocol's stated design goal of exact recovery.

---

## Nice-to-Haves

- A human plausibility study (e.g., "which text is real?" or "rate coherence") would directly substantiate the claim that stegotexts are opaque to humans.
- A comparison table showing capacity (bits/token), stegotext perplexity, and decoding error rate for Calgacus vs. Ziegler et al., Meteor (Kaptchuk et al.), and Zamir under comparable conditions.
- Scaling experiments across text lengths (50–500 tokens) to show the quality doesn't degrade.
- A systematic characterization of the condition under which the protocol produces fluent stegotexts vs. broken text (entropy of the secret message, quality of the LLM).

---

## Removed Points

These points raised by the reviewers were removed after cross-checking against the paper:

- **Perplexity normalization criticism** (Harsh Critic): The critic argues the paper's rejection of perplexity is "weak and potentially misleading." However, the paper only compares texts of equal length and explicitly acknowledges perplexity as "another possibility." The justification about first-token probability is technically grounded; the approach is methodologically sound for same-length comparisons. **Reason**: Factually incorrect characterization of the paper's argument.

- **Figure 6 (GEB collage) critique** (Harsh Critic): The critic says it "adds little substance." **Reason**: Pure stylistic/subjective preference; does not affect evaluation of technical merit.

- **"Editorializing" about trust in writing** (Harsh Critic): The critic says the abstract's claim about "eroding trust" is editorializing the paper doesn't need. **Reason**: Subjective framing preference. The paper is permitted to contextualize its contribution.

- **"Novel conceptual framing" strength** (Strength Finder): The hallucination-as-lack-of-intention framing was flagged as a strength. **Reason**: Conflicts with verified weakness — the discussion is recognized as loosely attached and not empirically supported. A strength must be grounded in evidence, not just interesting prose.

- **Security and deniability analysis as a core strength** (Strength Finder): The analysis exists but is incomplete; listing it as a core strength overstates its rigor. **Reason**: Weakness (Major #3) already covers this ground more honestly.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the protocol's key strengths (full capacity, simplicity, the rank-preservation gap) and its weaknesses (thin evaluation, the logit-determinism problem, lack of baselines) but do not produce a synthetic insight absent from the paper.

---

## Suggestions

1. **Foreground what the paper does best.** The elegant simplicity of the protocol and the "full capacity" property are the genuine contributions. Lead with these and let the implications emerge from the evidence, rather than front-loading maximal claims about societal impact.

2. **Add a human plausibility study and baseline comparisons before any final version.** A small user study and a comparison table against Ziegler/Meteor/Zamir would address the most significant evidential gaps without requiring a new method.

3. **Either solve or honestly bound the logit-determinism problem.** If the "shipping unfiltered LLMs" scenario is retained as a central contribution, provide at minimum a controlled experiment quantifying logit divergence across hardware setups, and discuss potential mitigations. If the scenario is de-emphasized as speculative, the paper should make this clear.

4. **Provide basic runtime measurements** (seconds per token on a laptop) to back the efficiency claim.

5. **Scale the central experiment** to at least a few length regimes (e.g., 50, 200, 500 tokens) to show the method does not degrade with longer messages.

---

## Score and Decision

The paper presents a genuinely clever and novel protocol with a clean technical idea. The core demonstration is valid, the key insight about rank preservation is well explained, and the "Low entropy token choices" analysis adds depth. However, the evaluation is thin — three texts at a single length, no human study, no comparison against prior work — relative to the paper's ambitious framing and claims. The most compelling application scenario is undermined by a practical (logit-determinism) barrier that is acknowledged but not engaged with. The paper is a thought-provoking demonstration rather than a rigorous empirical contribution, and its current form requires substantial strengthening or recalibration of claims.

**Score: 6.0**

**Decision: Accept** (borderline, with the caveat that the strengths are real and the core idea is publishable, but the authors should be strongly encouraged to address the major weaknesses — especially the logit-determinism evaluation and the empirical gaps — in a revision or extended version.)

<score>6.0</score>
<decision>Accept</decision>