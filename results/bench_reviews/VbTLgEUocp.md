Now I have a thorough understanding of the paper and anchor papers. Let me synthesize the final review.

---

## Summary

This paper presents *Calgacus*, a simple steganographic protocol that hides an arbitrary text *e* inside a different text *s* of equal token length. The method works by: (1) tokenizing *e* and recording each token's rank in the LLM's probability distribution given prior context, then (2) generating *s* from a secret prompt *k* by selecting the *r_i*-th most probable token at each step. The stegotext can be steered by choice of *k*, and decoding requires knowledge of *k* and the same LLM. The protocol runs on consumer hardware with 8B-parameter open-source models, encoding messages the length of the paper's abstract in seconds. The paper uses token log-probability under the generating LLM (and cross-validated with Phi-3) to argue stegotexts fall within the distribution of real Reddit texts, and discusses deniability, security, and a provocative AI-safety scenario where aligned chatbot responses conceal unfiltered answers.

## Strengths

- **Elegant, genuinely novel protocol.** The idea of using token ranks to achieve full-capacity steganography (hiding *n* tokens inside *n* tokens) is remarkably simple and constitutes a clear conceptual advance over prior generative steganography methods that typically achieve sub-capacity rates. The protocol is described with a clear, reproducible recipe (Section 3, Figure 3).

- **Demonstrated to work in practice.** Figures 1, 7, 8, and 13 provide concrete, compelling examples across multiple domains (political text, chess games, Python code, book passages) and multiple models (Llama 3 8B, Gemma 3 27B, Phi-4 14B, Qwen3 8B), showing that the protocol produces coherent steerable stegotexts on commodity hardware (e.g., 5.0/4.6s encoding/decoding on Llama 3 8B).

- **Cross-model validation of stegotext plausibility.** Figure 4 shows stegotexts fall within the log-probability distribution of real Reddit texts, and Figure 14 replicates this gap with a *different* LLM (Phi-3 3.8B), providing non-circular evidence that stegotexts occupy a plausibility range comparable to real text.

- **Thoughtful engagement with broader implications.** The discussion (Section 4) raises substantive questions about LLM knowledge, hallucinations re-conceptualized as absence of intent, and the erosion of trust in written communication. These are not merely hand-waving—they connect to concrete protocol properties demonstrated in the paper.

## Weaknesses

### Fatal

None.

### Major

- **Plausibility evaluation relies solely on token log-probability; stronger evidence for human-perceived quality is absent.** The paper's central qualitative claim is that stegotexts are "coherent" and "plausible." The quantitative evidence is restricted to token log-probability under the generating model (Figure 4), which the paper itself acknowledges is a "practical proxy" with "a clear defect" (lines 249-271). While Figure 14 provides cross-model validation with Phi-3, log-probability under *any* LLM is not a validated measure of human-perceived text quality. A human evaluation or at minimum an evaluation using established text-quality metrics (e.g., MAUVE, perplexity under a held-out model, or LLM-as-judge with an independent model) would substantially strengthen the paper's core claim.

- **No empirical comparison with prior generative steganography methods.** The paper claims full capacity as its distinguishing contribution, yet provides no comparison with prior LLM-based steganography schemes (e.g., Meteor, Zamir 2024, Wu et al. 2024) on any shared axis: capacity, cover-text quality, encoding/decoding speed, or detectability. This makes it difficult to assess the practical tradeoffs Calgacus makes to achieve full capacity, or to verify that full capacity does not come at a prohibitive cost to other desiderata.

### Minor

- **Security and deniability analysis is preliminary.** The deniability argument (Section 3.1, Figure 15) is demonstrated with a single hand-crafted example. No systematic measurement is provided for how often bogus keys can be found that yield messages with comparable log-probability, nor whether an attacker with access to probability distributions could distinguish true keys from bogus ones. The paper is upfront about avoiding formal steganographic models (lines 123-125), so the absence of formal security proofs is not itself a weakness—but the empirical analysis of deniability would benefit from a larger-scale study.

- **The Shibbolethian Theatre scenario is illustrative but not systematically validated.** The scenario in Section 4 (Figures 11-12) is presented as a single worked example. The paper does not analyze when the condition holds that oLLM assigns low ranks to uLLM's unfiltered answer, nor provide statistics on success rates. This is presented in the Discussion section as an application illustration rather than a main empirical claim, so it does not undermine the paper's core contributions, but readers should treat the scenario as a conceptual demonstration rather than a validated capability.

### Trivial

- The paper could benefit from reporting statistics (e.g., mean rank, fraction of rank-1 tokens) across the 100-stegotext sample in Figure 4, rather than only reporting distributional overlap.

## Nice-to-Haves

- A large-scale failure-case gallery complementing the cherry-picked examples, to help readers understand the method's practical reliability across different *e* domains and *k* lengths.
- A detectability study: training a simple classifier (e.g., based on rank-frequency distortions noted in the "Low entropy token choices" analysis) to distinguish stegotexts from real texts, which would clarify the practical concealment properties.
- Extending the application scenario to multimodal domains (as sketched in Appendix A.3) with concrete examples would add richness.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"The claimed plausibility is not adequately supported — log-probability under the generating model is fundamentally circular."** The paper does cross-validate with a different model (Phi-3, Figure 14), explicitly acknowledges log-probability is a "practical proxy" with defects, and does not claim human indistinguishability. The core concern is retained as a major weakness but softened to reflect what the paper actually demonstrates and claims.

- **"The unaligned chatbot scenario is never validated / remains speculative."** The scenario is in the Discussion section and is presented as an application illustration. The paper includes a concrete reproducible example (Figures 11-12). The absence of large-scale validation is retained as a minor weakness but the claim that it constitutes a fatal gap is inflated relative to the paper's framing.

- **"Missing related works" critiques.** Per instructions, these are removed.

- **"GPU reproducibility is mentioned only in passing."** This is a limitation the paper explicitly acknowledges (lines 338-340) and is standard in the field. Not a substantive weakness.

## Novel Insights

The paper's most genuinely novel observation is the "low entropy token choice" analysis (lines 297-331, Figure 5): the systematic probability gap between stegotexts and originals arises because rank-1 tokens occur at ~40% frequency in real text but are "wasted" on high-entropy positions where they would have been selected anyway, while high-entropy positions in stegotexts receive lower-rank tokens that the model finds less probable. This explains *why* stegotexts are less probable than originals and why the gap is detectable, without relying on any property of the hidden message content. It is a clean, mechanistic explanation that could inform future work on both steganography and detection.

## Suggestions

- Add a human evaluation (e.g., a simple forced-choice Turing test where annotators distinguish stegotexts from human-written texts of the same length) or at minimum an LLM-as-judge evaluation using an independent model family. This would directly address the core plausibility claim.
- Include at least one comparison with a prior generative steganography method (e.g., Meteor) on a shared set of messages, reporting capacity, text quality, and encoding time. This would ground the full-capacity claim in the broader literature.
- For the deniability claim, run a modest-scale experiment: for a sample of 50-100 stegotext/message pairs, search for bogus keys that yield messages within 1-2 standard deviations of the true message's log-probability, and report the success rate.

## Anchor Comparison

- **`/home/wg25r/review_agent/human_reviews_2026/q4qxtaKVAU.md` (avg 6.0, Accept Poster):** "Early Signs of Steganographic Capabilities in Frontier LLMs." More systematic evaluation across multiple models and tasks, but less novel as a method contribution. Calgacus has a stronger conceptual idea but thinner evaluation.
- **`/home/wg25r/review_agent/human_reviews_2026/6cEPDGaShH.md` (avg 6.0, Accept Oral):** "Invisible Safety Threat: Malicious Finetuning for LLM via Steganography." Thorough evaluation with multiple models and safety classifiers. Requires finetuning; Calgacus is training-free and simpler, but lacks comparable evaluation rigor.
- **`/home/wg25r/review_agent/human_reviews_2026/t38nZqqi3Z.md` (avg 6.5, Accept Oral):** "LLM Fingerprinting via Semantically Conditioned Watermarks." Strong technical contribution with thorough evaluation. More polished than Calgacus.
- **`/home/wg25r/review_agent/human_reviews_2026/EhDgP69DJG.md` (avg 7.0, Accept Poster):** "PMark: Semantic-level Watermarking." Strong theoretical framework, thorough experiments, clear baselines. Significantly more rigorous evaluation than Calgacus.
- **`/home/wg25r/review_agent/human_reviews_2026/ZujfJpD6as.md` (avg 3.5, Withdrawn/Reject):** "Hiding in Plain Sight: Steganographic Jailbreaks." Rejected for insufficient novelty (fusion of prior methods), replication failures, and weak evaluation. Calgacus is substantially stronger—its method is genuinely novel and works as claimed.
- **`/home/wg25r/review_agent/human_reviews_2026/rgzzE3Ypsq.md` (avg 3.0, Withdrawn/Reject):** "Task Overload Jailbreak." Rejected for speculative claims, weak threat model, insufficient evidence. Calgacus is clearly superior—its protocol has a concrete, reproducible mechanism.
- **`/home/wg25r/review_agent/human_reviews_2026/YHz6PybFqK.md` (avg 5.0, Reject):** "The Hidden Cost of Modeling P(X): Membership Inference Attacks." Similar evaluation-level concerns. Calgacus is comparable in evaluation depth but has a more novel core idea.
- **`/home/wg25r/review_agent/human_reviews_2026/TVSPV6D0co.md` (avg 4.67, Reject):** "Fast, Secure, High-Capacity Image Watermarking." Mixed reviews. Calgacus has a cleaner, more focused contribution.
- **`/home/wg25r/review_agent/human_reviews_2026/dZY5t9ZrUB.md` (avg 4.50, Reject):** "LLM Watermark Evasion via Bias Inversion." Mixed reviews. Calgacus has a stronger conceptual contribution.

**Positioning:** Calgacus has a more novel and elegant core idea than most anchors, but its evaluation is noticeably thinner than the 6.0+ accepted papers. It is clearly stronger than the 3.0-3.5 rejected papers. It sits in a borderline region—the idea is strong enough to warrant acceptance with revision, but the evaluation gaps are real and substantive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>