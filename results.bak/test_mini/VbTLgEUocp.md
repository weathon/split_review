Now let me synthesize the final review.

## Summary

I've carefully read the paper and verified all reviewer claims. Here is my analysis:

**Verified weaknesses (keep):**
1. No quantitative comparison to prior LLM steganography methods (the paper cites Ziegler et al., Kaptchuk et al., Wu et al., Zamir but provides zero comparative experiments)
2. Plausibility evaluation relies primarily on LLM log-probabilities from the same model used for generation (Llama 3 8B); no human evaluation of stegotext plausibility
3. Empirical scope is limited to one LLM, one dataset (Reddit), one length (85 tokens), three source texts
4. Runtime claim ("seconds on a laptop" in the abstract) is unsubstantiated by any timing measurements

**Removed/softened weaknesses:**
- The security analysis complaint: the paper explicitly disclaims formal security modeling ("we will avoid building a palace on the sand"), so informal treatment is consistent with the paper's own stance
- Appendix-related criticisms: removed per hard rules (missing appendix is a parser artifact)
- Statistical rigor (KS test): demoted to Nice-to-Have since visual overlap in Figure 4 is clear
- Missing runtime data: kept as Minor since the claim is central to the "efficient" framing

**Verified strengths:**
1. Genuinely novel protocol achieving full-capacity (same-length) steganography
2. Figure 4 convincingly shows stegotext log-probabilities fall within real text distribution for the tested setting
3. Clear explanation of why stegotexts are systematically less probable ("Low entropy token choices")
4. Concrete application scenario (Shibbolethian Theatre) that grounds the capability in AI safety concerns

Now I'll write the review.

- Round 1 bracket: I initially placed this between ~3.5 and ~7.5 based on the calibration. The weak-band papers (avg 1.5-3.0) are clearly worse — they lack novel methods or are off-topic. The strong-band papers (avg 8.0) are on different topics and have far more rigorous evaluation. So the bracket is (3.5, 7.5).

- Round 2 narrowing: Reading the closest anchors — "Early Signs of Steganographic Capabilities" (6.00, Accept Poster) is more rigorous empirically but less novel. "Invisible Safety Threat" (6.00, Accept Oral) also has stronger empirical support. "Subversion Strategy Eval" (4.50, Reject) has mixed reviews. "The Telephone Game" (5.33, Reject) has split opinions. The Calgacus paper is more novel than all of these but empirically weaker than the accepted ones. The novel idea is strong but the evaluation is thin. I'd place this at ~5.0, which is in the reject range.

Let me write the review now.## Summary

This paper presents Calgacus, a protocol for LLM-based steganography that encodes a secret message into a generated "stegotext" of exactly the same token length. The method is strikingly simple: record the ranks of tokens of the secret message under an LLM, then generate the stegotext from a secret prompt by selecting the token at each recorded rank. The paper demonstrates the protocol on Reddit posts using Llama 3 8B, provides an informal security analysis, and devotes substantial space to philosophical discussion about LLM knowledge, hallucination, and authorial intent.

---

## Strengths

- **Full-capacity (same-length) steganography.** The paper delivers on its central claim: a protocol that hides a message in a stegotext of identical token length. This property is explicitly stated as the paper's addition to prior work (Section 3: "the stegotext and the secret message being of the same length") and is genuinely novel relative to existing LLM steganography methods.

- **Figure 4 provides clear evidence of plausibility in one setting.** 100 stegotexts generated from each of three original Reddit posts fall within the log-probability distribution of 1000 real Reddit texts, while random ASCII and random English-word strings lie far outside. This demonstrates, for the tested configuration, that the stegotexts are plausible under an LLM's own plausibility measure.

- **Principled explanation of the probability gap.** The "Low entropy token choices" paragraph (Section 3) and Figure 5 give a clear, correct explanation of why stegotexts are systematically less probable than originals: rank-1 tokens in the secret message correspond to ~40% of positions, and those rank-1 tokens in the stegotext have lower probability than their counterparts in real text, because the same rank doesn't imply the same contextual certainty.

- **Concrete, compelling application scenario.** The "Shibbolethian Theatre" (Section 4) describes a detailed, plausible protocol for a company covertly deploying an unfiltered LLM by encoding uncensored answers within compliant responses of a safe model, with accompanying real examples (Figures 11–12). This grounds the capability in an immediate AI-safety concern.

---

## Weaknesses

### Fatal

None.

### Major

- **No quantitative comparison to prior LLM steganography methods.** The paper acknowledges prior work (Ziegler et al., 2019; Kaptchuk et al., 2021; Wu et al., 2024; Zamir, 2024), correctly identifies each method's distinguishing feature, and claims that the novel contribution is full capacity. Yet it provides **zero comparative experiments** — no comparison of stegotext quality, bit-per-token efficiency, computational cost, or detectability against any of these methods. The core claim that same-length steganography is a meaningful advance cannot be assessed without understanding the quality/efficiency trade-off. For example, Meteor (Kaptchuk et al.) encodes a variable number of bits per token depending on entropy; Calgacus encodes exactly 1 token per token. A comparison showing how much stegotext quality Calgacus sacrifices for this property is needed to establish the contribution's significance within the field the paper itself invokes.

- **Plausibility evaluation is insufficient for the strength of the claims.** The primary evidence that stegotexts are "plausible" is that Llama 3 8B — the **same model** used to generate the stegotexts — assigns them log-probabilities within the range of real Reddit texts. This is circular: a model's probability estimate is not independent evidence of human-perceived plausibility. The paper mentions cross-model verification with Phi-3 (Figure 14, in appendix) but this still uses the same LLM-as-plausibility-proxy approach. No human evaluation is conducted (e.g., A/B forced-choice between real and stegotext, detection experiment, or rating study). Since the paper's broader claims reach "a radical decoupling of text from authorial intent" and practical applications in censorship circumvention, the evidence that stegotexts are actually *believable to human readers* is the core empirical pillar — and it is missing.

- **Empirical scope is very narrow.** The main experiment uses: one LLM (Llama 3 8B), one dataset (1000 Reddit posts), one fixed length (85 tokens), and three source texts to generate stegotexts from. This is a thin basis for a paper whose title claims "LLMs Can Hide Text in Other Text of the Same Length" as a general capability. The evaluation does not vary: text length (e.g., 50, 200, 500 tokens), text domain (news, dialogue, code), or model (smaller or larger models). The appendices are said to contain some further analysis (A.1, A.2, A.5), but the central evidence should stand on its own. As presented, the results support the claim that *some stegotexts from this method fall within the LLM-estimated probability range of real texts for one model and one dataset at one length* — a much weaker statement than the title and abstract imply.

### Minor

- **Runtime claim is unsubstantiated.** The abstract states that "a message as long as this abstract can be encoded and decoded locally on a laptop in seconds," and the introduction repeats that the method is "efficient." No timing measurements, throughput figures, or wall-clock data are reported anywhere in the paper. Given that the protocol requires one forward pass per token for both encoding and decoding, the runtime is non-trivial and should be quantified, especially for the claimed "laptop" scenario.

- **Failure cases are not quantified.** The paper mentions that stegotext quality depends on $e$, $k$, and the LLM, and gives an example of a hash producing broken output. But there is no systematic analysis of how often the protocol produces incoherent stegotexts, under what conditions, or the distribution of failure modes. For a practical protocol, the frequency of usable vs. unusable outputs matters.

### Trivial

None.

---

## Nice-to-Haves

- **Statistical comparison of distributions** (e.g., KS test or overlap coefficient) between real and stegotext log-probabilities would be a small but welcome addition beyond the visual inspection of Figure 4.
- **A simple comparative experiment** against at least one prior method (e.g., Meteor) showing the quality/length trade-off would clarify the nature of the contribution without requiring extensive benchmarking.
- **Systematic variation** of text length and model would strengthen generalizability claims without requiring a human study.

---

## Removed Points

- **Security analysis is informal/incomplete** (raised by Harsh Critic). The paper explicitly states in Section 2: "we will avoid building a palace on the sand, and not frame our method in a formal model of steganography, limiting our discussion to how meaningful our fake texts look, with some quantitative arguments." Section 3.1's security discussion is informal by design. Criticizing it for lacking formal security guarantees holds the paper to a standard it disclaims.
- **Missing appendix content / missing proofs / missing reproducibility details** (raised by Harsh Critic). Per hard rules: the parser strips appendix sections from all papers; they exist in the original submission. Similarly, formatting nitpicks about typos, spacing, and garbled characters are parser artifacts, not author errors.
- **Insufficient related work coverage** (raised by Harsh Critic, implicit). Per hard rules: I cannot verify missing citations without external knowledge.
- **Generic strength about "importance of the problem"** (raised by Strength Finder). Per hard rules: strengths that are generic or sycophantic without concrete evidence are removed.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add a human evaluation** — even a small-scale study (e.g., 100 examples judged by crowdworkers on a 3-point plausibility scale) would substantially strengthen the core claim that stegotexts are "plausible." Alternatively, a detection experiment using a *different* LLM as a discriminator trained on the task would be a meaningful step.
2. **Include a comparison to at least one prior method** — the simplest path would be to implement a basic version of the Kaptchuk et al. (2021) approach and compare stegotext quality (via the same log-probability measure) for fixed secret messages of the same content, showing the length-quality trade-off explicitly.
3. **Report runtime measurements** for encoding and decoding on a specific hardware setup, supporting the "seconds on a laptop" claim.
4. **Broaden the empirical scope** in one additional dimension (e.g., a second model or a second text length) in the main paper to support the generality of the claims.

---

## Score and Decision

**Calibration anchors used:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| "Early Signs of Steganographic Capabilities" (q4qxtaKVAU) | 6.00 | 1,2 | More rigorous empirically, multiple models, systematic evaluation; less novel conceptually. The Calgacus paper is less empirically thorough. |
| "Invisible Safety Threat" (6cEPDGaShH) | 6.00 | 1,2 | Clear attack demonstration, quantitative results on AdvBench, tested on multiple models. More rigorous. |
| "The Telephone Game" (TbWQJI5OIn) | 5.33 | 1,2 | Rejected paper. Split reviews (4,4,8). Interesting idea but weak execution. Comparable in being a conceptually interesting paper with insufficient empirical support. |
| "Subversion Strategy Eval" (4tlbxaPiXy) | 4.50 | 2 | Rejected. Novel benchmark but mixed reviews questioning practical value. Calgacus is more novel but similarly limited in scope. |
| "Detecting Benchmark Contamination" (WFGxFzFDmQ) | 5.00 | 2 | Rejected. Clean idea with some experiments but insufficient for acceptance. |
| "Majority Bit-aware Watermarking" (qF6TyKhc7S) | 4.00 | 1 | Rejected. Practical contribution but limited novelty. |

**Round 1 bracket:** I initially placed the paper between ~3.5 and ~7.5 based on broad calibration. The weak-band (1.5–3.0) papers are clearly worse (off-topic or lacking novel methodology). The strong-band (7.5+) papers are on different topics with far more rigorous evaluation.

**Round 2 narrowing:** Reading the closest topical anchors narrowed the bracket. The accepted papers at 6.0 have stronger empirical execution (multiple models, quantitative baselines, systematic evaluation). The rejected papers at 4.5–5.3 share a pattern: interesting, novel ideas with insufficient support. The Calgacus paper is more conceptually novel than most of these but empirically weaker than all accepted anchors.

**Final position:** The paper is more novel than the rejected anchors (4.5–5.3) but less empirically rigorous than the accepted ones (6.0). It occupies a space between them — a genuinely interesting idea presented as a proof-of-concept rather than a complete scientific investigation. It is comparable to papers scoring ~5 that were rejected due to insufficient evidence for the scope of their claims.

**MY FINAL SCORE: 5.0**
**MY FINAL DECISION: Reject**