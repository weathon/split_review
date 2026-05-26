Now I have a comprehensive view of both the paper and the calibration anchors. Let me assemble the final review.

---

## Summary

This paper presents *Calgacus*, a steganographic protocol that uses an LLM's token ranks to encode an arbitrary secret text inside a different, coherent text of exactly the same length. The method records the rank of each token in the secret text under the LLM's probability distribution, then generates a stegotext from a secret prompt by selecting the token at that rank at each step. The paper argues this demonstrates a radical decoupling of text from authorial intent and discusses implications for AI safety, including a concrete scenario where an unfiltered LLM's answers are hidden inside a compliant chatbot's responses.

## Strengths

- **Elegant and genuinely novel protocol.** The method is strikingly simple — just record token ranks and replay them under a different prompt — yet achieves the notable "full capacity" property (stegotext same length as secret) that existing LLM-based steganographic schemes lack. The step-by-step recipe in Section 3 (Figure 3) is clear and immediately replicable.

- **Insightful explanation of the probability gap.** The "low entropy token choices" analysis (Section 3, Figure 5) provides a mechanistic account of why stegotexts are less probable than originals — rank-1 tokens are "wasted" in high-entropy contexts — which is a genuinely illuminating observation about the method's behavior.

- **Compelling real-world scenario.** The "Shibbolethian Theatre" play in Section 4 — where a company hides uncensored LLM answers inside a compliant model's responses — is a concretely worked-through application that grounds the abstract protocol in a timely AI safety concern.

- **Clear, accessible writing and thoughtful discussion.** The paper is well-written and the philosophical exploration of hallucination as "lack of intention" (Section 4) is stimulating, connecting the technical contribution to broader questions about trust in written communication.

## Weaknesses

### Fatal

None.

### Major

- **The empirical evaluation is too narrow to support the headline claims.** The abstract asserts "high-quality results" and the introduction promises that "even modest 8-billion-parameter open-source LLMs are sufficient." Yet the quantitative evaluation (Figure 4) uses only three original texts, each encoded with 100 different prompts, measured solely by the log-probability assigned by the same Llama 3 8B model used for generation. This is a reasonable metric but it is only one metric — log-probability is a necessary but not sufficient condition for human-level coherence and plausibility. No human evaluation is performed, and there is no systematic characterization of how often the method produces incoherent output (the hash example is offered anecdotally but not quantified). The gap between "falls within the log-probability distribution of real texts" and "produces coherent, plausible text that a human cannot distinguish from natural writing" is substantial.

- **No empirical comparison with existing LLM-based steganographic methods.** The paper positions full capacity (same token length) as its main novelty over Meteor (Kaptchuk et al., 2021), Wu et al. (2024), and Zamir (2024), all of which are discussed in Section 2. Yet there is no head-to-head comparison on any shared metric. Without this, the reader cannot assess the quality–capacity tradeoff: does full capacity come at a significant cost in text quality, security, or reliability compared to lossy-capacity schemes? A small controlled comparison would substantially strengthen the contribution.

### Minor

- **The security analysis is informal while still making concrete claims.** Section 3.1 discusses brute-force bounds and deniability, but the treatment remains qualitative. The paper explicitly states it will not adopt a formal model (Section 2: "we will avoid building a palace on the sand"), which is reasonable, but then proceeds to claim that the method "provides deniability" based on the existence of outlier prompts. The deniability argument would be more persuasive with a clearer threat model specifying what an adversary can and cannot do.

- **The "low entropy token choices" analysis rests on a single text.** The explanation in Figure 5 is insightful, but it is performed on a single Economist article. A broader analysis across multiple text types would strengthen confidence that the observed mechanism generalizes.

- **The prompt dataset is opaque.** The paper states that prompts are "a random subsample of the prompts in (Akn, 2025)" without characterizing the distribution of prompts (length, topic diversity, etc.), making it difficult to assess how representative the results are.

### Trivial

- The runtime claim ("in seconds on a laptop") is stated without any measurement or specification of hardware.
- The references "Akn, 2025" and "Trimness8, 2025" are non-standard citation forms.

## Nice-to-Haves

- A human evaluation study where raters judge the coherence and plausibility of stegotexts against real texts would directly test the core claim of human-level opacity.
- A systematic failure analysis mapping how output quality varies with the entropy/domain of the secret text, the length and specificity of the prompt key `k`, and the choice of LLM.
- A small controlled comparison with at least one existing LLM-based steganographic scheme (e.g., Meteor) on a shared quality metric to illustrate the quality–capacity tradeoff.
- A runtime benchmark to substantiate the "seconds on a laptop" claim.

## Removed Points

These points from the reviewer inputs were considered but removed or weakened:

- **"Three hand-picked Reddit posts" / cherry-picking.** The paper selects texts at μ, μ−2σ, and μ+2σ of the real-text distribution — this is systematic stratified sampling, not cherry-picking. Removed.
- **"The appendix was not available for review."** The appendix exists in the original submission; its absence is a parser artifact. Removed.
- **Demand for a formal Cachin-style security model.** The paper explicitly states (Section 2) that it will not adopt a formal model of steganography given the unrealistic assumptions required. Criticizing its absence is scope creep. Demoted from major to minor (the informal security claims that the paper *does* make are still worth flagging).
- **"The only argument against steganalysis is that stegotexts fall within the log-probability range."** The paper does not claim steganalysis is impossible — it explicitly shows (Figure 4, Figure 14) that stegotexts are less probable than originals and can often be distinguished by an LLM. The paper's claim is about *human* indistinguishability, not LLM-based steganalysis. The critic's framing is inaccurate. Removed.
- **Conditional praise from the Strength Finder rephrased as "rigorous, data-driven validation."** The log-probability evaluation is useful but calling it "rigorous" overstates what was done. Moderated.

## Novel Insights

The paper surfaces an interesting connection between standard LLM text generation and constrained writing: both involve satisfying a sequence of token-level constraints that are orthogonal to communicative intent. The observation that stegotext generation (forced rank choices) and standard nucleus sampling (forced random choices) are structurally similar — both are "tyrannical noise" that the LLM must work around — is a genuinely novel framing that reframes the trustworthiness problem for all LLM-generated text, not just steganographic text alone.

## Suggestions

- The paper's strongest contribution is the protocol itself and the philosophical implications. Consider reframing the evaluation section as a preliminary validation rather than a definitive demonstration, which would better align the claims with the evidence provided.
- If full human evaluation is infeasible, an LLM-as-judge evaluation (e.g., having GPT-4 or Claude rate the coherence of stegotexts vs. originals in a blinded setup) would provide a stronger signal than log-probability alone while being significantly cheaper to run.
- The "Shibbolethian Theatre" scenario (Section 4) is compelling enough to deserve its own small empirical demonstration within the paper — the figures referenced in the appendix (Figures 11–12) already exist and could be foregrounded.

## Score and Decision

### Calibration anchor comparison

| Anchor | Score | Source | Comparison |
|--------|-------|--------|------------|
| IQafqgqDzF (OD-Stega) | 3.50 | R1-topic-mid + R1-weakness | LLM steganography with more formalism and metrics but weaker novelty. Calgacus has a cleaner idea but thinner eval. |
| urQi0TgXFY (Hidden in Plain Text) | 5.00 | R1-topic-mid + R2 | Steganographic collusion; much more comprehensive evaluation. Calgacus is weaker empirically. |
| 7suavRDxe8 (Plausibly Deniable Encryption) | 4.80 | R2 | LLM-based deniable encryption; similar "clever LLM application" profile with more evaluation. Calgacus is simpler but less validated. |
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | R1-topic-low | Rejected for lack of novelty and missing baselines. Calgacus is more novel. |
| BXMoS69LLR (Blind Baselines) | 4.50 | R1-weakness | Methodological critique paper; different genre. |

**Round 1 bracket:** 3.0–5.0 based on topic-band and weakness-anchored queries. The topic-low band (2.33–3.00) contains papers rejected for lack of novelty or fundamentally flawed evaluation — Calgacus clears that bar on novelty. The topic-mid band (3.67–5.50) contains papers with stronger evaluation or mixed reception. The weakness-anchored queries show that papers with "no comparison with baselines" or "informal security" in steganography typically score 3.50–5.50.

**Round 2 narrowing:** Within the 3.0–5.5 bracket, OD-Stega (3.50) and Plausibly Deniable Encryption (4.80) are the closest comparators. Calgacus is more novel and elegant than OD-Stega but has thinner evaluation. It is less empirically rigorous than PDE but simpler and more accessible.

**What low-band anchors failed at, and does Calgacus share those failures?** The low-band anchor (Sparse Watermarking, 3.00) was rejected primarily for lack of novelty. Calgacus does not share this failure — the full-capacity protocol is genuinely novel. However, the weakness-anchored papers at 2.50 share the pattern of thin evaluation with unsupported claims — Calgacus partially shares this pattern, though its evaluation is not absent, just insufficient. The paper's core contribution (the protocol idea) survives independent of the evaluation quality, which distinguishes it from papers where both idea and evidence are weak.

**Final score: 4.0.** The paper presents a genuinely novel and elegantly simple protocol with a thought-provoking discussion. However, the empirical validation is too narrow for the strength of the claims made. The evaluation uses only 3 texts, one metric, and one LLM, with no human judgment, no comparison with existing methods, and no systematic failure characterization. The paper would benefit substantially from stronger evaluation but the core idea has clear merit.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>