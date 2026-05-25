I now have a thorough understanding of the paper, the reviews, and the calibration anchors. Let me produce the final consolidated review.

## Summary

The paper presents *Calgacus*, a protocol for LLM-based generative steganography with the novel property of "full capacity": the stegotext and the secret message are exactly the same token length. The method is elegantly simple — encode a message by recording the rank of each of its tokens in the LLM's probability distribution, then generate the stegotext by following those same ranks under a secret prompt. The paper provides quantitative evidence (Figure 4) that the resulting stegotexts fall within the log-probability distribution of real Reddit posts, discusses the method's security and deniability properties, and explores philosophical implications for AI safety, LLM knowledge, and the nature of hallucination.

## Strengths

1. **Full-capacity (same-length) property is genuinely novel.** The paper correctly identifies that prior LLM steganography methods (Meteor, Zamir 2024, etc.) do not provide this property, and *Calgacus* is the first protocol achieving it. This is cleanly demonstrated through examples (Figure 1) and the method description (Section 3).

2. **Quantitative evidence that stegotexts overlap with real texts.** Figure 4 shows that stegotexts produced from three different source texts (at μ, μ−2σ, μ+2σ of the real distribution) fall within the log-probability envelope of 1000 genuine Reddit posts, while random ASCII and random English words fall far outside. This is replicated with a different LLM (Phi-3, Figure 14), providing evidence that the result is not model-specific.

3. **Deniability is substantiated.** The paper provides a concrete argument (Section 3.1) supported by Figure 4's evidence that some stegotexts attain probabilities in the same range as originals, meaning a coerced sender can plausibly present an alternative key producing a different "secret" message. A concrete example is referenced (Figure 15).

4. **Efficiency and accessibility.** The protocol works with an 8B open-source LLM on consumer hardware and can encode/decode an abstract-length message in seconds, making it immediately practical. This is clearly stated and supported by the method's simplicity.

5. **Theoretical analysis of the probability gap.** Section 3's "Low entropy token choices" paragraph insightfully explains *why* stegotexts are slightly less probable than originals despite identical token ranks — a genuine analytical contribution that distinguishes the method from simple re-ranking.

## Weaknesses

### Major

- **No human evaluation for the claim that stegotexts are "opaque to humans" / plausible to human readers.** The paper states "This symmetry prevents one from establishing at first sight which text is authentic" (p.1) and "while for a human both the original and fake texts are plausible" (p.5). These are direct empirical claims about human perception, yet the only supporting evidence is Figure 4, which measures LLM log-probability. While LLM log-probability is a reasonable proxy for text fluency, it does not directly test whether a human reader would find the stegotexts indistinguishable from authentic texts or detect the subtle oddities that an LLM's probability gap reveals. A forced-choice human evaluation (e.g., comparing stegotexts to genuine texts of the same style/length) is needed to substantiate this central framing claim. This gap is especially consequential because the paper's broader narrative about eroding trust in written communication depends on the premise that these texts are convincing to human readers.

- **No experimental comparison to existing LLM steganography baselines.** The paper correctly surveys prior methods (Ziegler et al., 2019; Kaptchuk et al., 2021; Wu et al., 2024; Zamir, 2024) and identifies "full capacity" as its distinguishing property. However, it provides no experimental comparison on any common ground — not on stegotext quality (perplexity under a held-out evaluator), not on detectability under steganalysis, and not on capacity-distortion trade-off. Without such comparison, the reader cannot assess whether the same-length property constitutes a meaningful advance or merely a different point in the capacity–distortion Pareto front. Given that the paper's technical contribution *is* this property, the lack of comparison is a significant evidential gap.

### Minor

- **Security analysis is entirely qualitative.** Section 3.1 acknowledges the limits ("we will avoid building a palace on the sand") and the analysis is explicitly heuristic. The brute-force bound $O(d^{|k|})$ is stated but the paper itself notes the attacker could reduce the search space using semantic information from the stegotext. No empirical attack attempts are made (e.g., model-based steganalysis, key-recovery with a surrogate LLM, minimum key-length analysis). Given that the paper invokes "urgent questions for AI safety," the qualitative security treatment feels disproportionately low-effort relative to the stakes claimed.

- **AI safety scenario is presented as a theatrical script, not a validated demonstration.** The "Shibbolethian Theatre" play (Section 4) is an evocative framing device, but the paper does not provide an end-to-end implementation or success-rate measurement of the described protocol. The reference to a "real example" in Figures 11–12 (appendix) cannot be evaluated from the available content. For a scenario that the abstract frames as raising "urgent questions for AI safety," the absence of a concrete working demonstration weakens the impact.

- **Evaluation scope is narrow.** The quantitative evaluation uses 85-token texts from a single dataset (Reddit) with only 3 source texts generating 100 stegotexts each. There is no analysis of: (a) scaling to very short (<20 tokens) or very long (>500 tokens) messages, (b) performance on non-English or highly domain-specific texts, (c) variation across different underlying LLMs beyond Llama 3 8B and Phi-3, or (d) effect of the secret prompt's length/style on output quality. The evaluation is sufficient as a proof-of-concept but not as a characterization of the method's generality.

### Trivial

- The play format in Section 4, while engaging, sits in tension with the paper's repeated appeals to seriousness about AI safety. This is a presentation choice, not a substantive flaw.

## Nice-to-Haves

- A human evaluation study (even a small-scale MTurk experiment) would directly test the paper's central aesthetic claim and is the single highest-impact addition.
- An empirical comparison to at least one prior LLM steganography method on perplexity and simple steganalysis would contextualize the contribution.
- An end-to-end working prototype of the unfiltered LLM scenario, even as a demonstration on a single example, would substantially strengthen the safety discussion.
- An analysis of minimum key length / entropy needed to resist simple key-recovery attacks.

## Removed Points

These points were raised by the reviewers but are removed from the main weakness list with justification:

1. **"Figures 11 and 12 are in the appendix that cannot be evaluated"** → The appendix was stripped by the parser, not missing from the original submission. The paper's claim about a "real example" in those figures cannot be verified from the parsed text but the reference itself is valid. This is a parser artifact, not an author error.

2. **"The paper lacks a formal security model"** → The paper explicitly scopes this out ("we will avoid building a palace on the sand, and not frame our method in a formal model of steganography"). Criticizing this absence is scope creep — the paper sets modest expectations for security formality, which the heuristic treatment meets.

3. **"The secret key may disrupt the LLM's ability to produce coherent output"** → The paper acknowledges this limitation ("the quality of the result depends on e, k, and the LLM used") and discusses it in Appendix A.5. This is a known and acknowledged limitation, not an unaddressed problem.

4. **"The hash counterexample shows the method can fail"** → The paper explicitly acknowledges this: "For instance the hash ... produces the broken s" and discusses it as a limitation. This transparency is a strength, not a weakness.

5. **"The 'same length' property may reduce practical applicability"** → This is a speculation, not a grounded criticism. The paper characterizes this as a novel property without claiming universal superiority.

6. **Various formatting/style nitpicks and questions about reproducibility of trivial artifacts** → Removed per filtering rules.

## Novel Insights

The merger of the two reviews surfaces an interesting tension that neither reviewer explicitly articulates: the paper simultaneously claims two things that pull in opposite directions. On one hand, it asserts the stegotexts are "opaque to humans" and plausible; on the other hand, it demonstrates that LLMs *can* distinguish them via a probability gap, and provides a detailed analytical explanation for why this gap exists. The paper's honest treatment of the probability gap (Section 3, "Low entropy token choices") actually undermines its own opacity claim more than it acknowledges — if LLMs consistently catch the difference, and the mechanism is well-understood, the claim that humans cannot is less reassuring and demands direct testing. The paper would be more coherent if it reframed its central claim from "humans cannot tell" to "these texts are plausible enough that suspicion of steganography would not arise in ordinary reading" — a weaker but more defensible position.

## Suggestions

1. **Conduct a human evaluation** — even a modest one (50 raters, forced-choice between stegotext and original, or a Likert-scale plausibility rating) would provide crucial evidence for or against the framing claim. The results would either strengthen the paper significantly or reveal an honest limitation.

2. **Add at least one baseline comparison** — generate stegotexts using a prior method (e.g., Meteor/Kaptchuk 2021) on the same source texts and compare perplexity from a held-out evaluator LLM. This would contextualize whether the same-length property trades off against text quality.

3. **Tone down the "opaque to humans" phrasing** — replace it with language that accurately reflects the evidence: "LLM-based plausibility proxy suggests these texts are within the distribution of human-written texts" rather than "prevents one from establishing at first sight which text is authentic."

4. **Include an end-to-end demonstration of the AI safety scenario** — even a single annotated example (which the paper already references in Figures 11–12) would make the scenario concrete. A success-rate measurement would be stronger still.

5. **Broaden the evaluation** — at minimum, test with different message lengths (20, 200 tokens), different LLMs (Mistral 7B, Gemma 7B), and different text domains (news, technical writing). This would demonstrate generality without requiring a massive effort.

## Score and Decision

### Calibration

**Anchor list (all rounds):**

| Anchor | Score | Round/Query | Comparison |
|--------|-------|-------------|-----------|
| `IQafqgqDzF` (OD-Stega) | 3.50 | R1-topic-low, R1-weakness-missing-baseline, R2-novel-LLM | Closest comparator — LLM steganography paper with similar weaknesses (no baseline comparison, weak security evaluation, no human evaluation). Our paper has a cleaner novel contribution (same-length) and better writing, placing it above. |
| `jbfDg4DgAk` (Sparse Watermarking) | 3.00 | R1-topic-low | Watermarking paper with missing baselines and unclear novelty. Our paper has stronger originality. |
| `BeOEmnmyFu` (Playing Language Game) | 2.50 | R1-topic-low | Jailbreaking paper, less relevant. |
| `urQi0TgXFY` (Hidden in Plain Text) | 5.00 | R1-topic-mid, R1-weakness-missing-baseline, R1-weakness-no-human-eval, R2-generative-steg | Emergent LLM steganography with thorough evaluation (active defenses, multiple experiments). Rejected despite more evaluation than our paper. Our paper has a cleaner method contribution but weaker evaluation. |
| `kRJNV8RCE3` (Hiding Images in Diffusion) | 4.75 | R1-topic-mid, R2-generative-steg | Image steganography, weaker topical match. |
| `7suavRDxe8` (Plausibly Deniable Encryption) | 4.80 | R2-novel-LLM, R2-generative-steg | Strong thematic overlap (LLM-based deniable communication), similar evaluation gaps (heuristic security analysis, claims outrun evidence). Our paper is comparable in ambition and evidence level. |
| `eKGEsFdpin` (I Know You Did Not Write That) | 3.67 | R1-topic-mid, R1-weakness-no-human-eval | Watermarking paper, moderate topical match. |
| `6p8lpe4MNf` (Semantic Invariant Robust Watermark) | 5.50 | R1-topic-mid, R2-generative-steg | Accepted watermarking paper with thorough evaluation. Stronger than our paper on every evaluation dimension. |
| `NvSwR4IvLO` (Can AI-Generated Text be Reliably Detected) | 4.67 | R1-weakness-no-human-eval | AI text detection, moderate topical match. |

**Round 1 bracket:** 3.5–5.5

**Narrowing:** Low-band anchors (OD-Stega at 3.50, Sparse Watermarking at 3.00) failed at providing sufficient evaluation evidence — missing baseline comparisons, weak security/steganalysis, no human evaluation for plausibility claims. **Does our paper share these failures? Yes:** the paper makes a central claim about human opacity without testing it, provides no baseline comparison, and the security analysis is heuristic. The low-band failures apply directly.

However, our paper is lifted above OD-Stega (3.50) by: (a) a cleaner and more demonstrable novel property (same-length), (b) genuine quantitative evidence (Figure 4) that is more directly tied to the main claim than OD-Stega's evaluation was, (c) stronger writing and framing. It sits below the 4.75–5.00 anchors because those papers provided more thorough evaluation (even when still insufficient for acceptance).

**Round 2 anchors** (4.80 "Plausibly Deniable Encryption", 5.00 "Hidden in Plain Text") do not relocate the bracket upward because our paper shares the same class of evaluation failures as the low-band anchors but lacks the evaluation breadth of those mid-band papers.

**Final score:** 4.0. The paper has a genuine, clean novel contribution and is well-written, but the evaluation is too thin to support the ambitious claims about human opacity and AI safety implications. The gap between the paper's rhetorical ambition and its evidential support is the central weakness.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>