Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper presents Calgacus, a protocol that uses an off-the-shelf LLM to hide a secret text inside a different, coherent cover text of the *same token length*. Encoding is straightforward: record the rank of each token of the secret message under the LLM, then generate the stegotext by selecting tokens at those same ranks from the LLM's distribution conditioned on a secret prompt key. Decoding reverses the process. The paper demonstrates the method with several examples (e.g., hiding a political critique inside a boar recipe), shows that generated stegotexts fall within the log-probability distribution of real Reddit posts, discusses a deniability property, and presents a concrete AI-safety scenario (an "Shibbolethian Theatre" for covertly deploying an unfiltered LLM). A substantial portion of the paper philosophically reflects on how this protocol challenges notions of authorship, intention, and hallucination in LLMs.

## Strengths

- **Simple, working, and reproducible protocol.** The method requires no fine-tuning — it uses an off-the-shelf LLM with logit access. The paper provides concrete encoding/decoding timing (e.g., 5.0s encode / 4.6s decode on Llama 3 8B with an RTX 4070), a publicly available demo, and clear step-by-step instructions. The protocol is trivially verifiable.

- **Steerability of the cover text.** The secret prompt key \(k\) controls the topic, tone, and style of the stegotext. The paper demonstrates diverse steering (culinary recipes, VR game reviews, Python code) with concrete examples, and shows that the method works across multiple LLMs (Llama 3 8B, Gemma 3 27B, Qwen 3 8B, Phi-4 14B, Phi-3 3.8B).

- **Quantitative plausibility evidence.** Figure 4 shows that 300 stegotexts (from 3 original Reddit posts at different points in the distribution) fall within the log-probability distribution of 1000 real Reddit posts under Llama 3 8B. Figure 14 confirms the same ranking holds under a different LLM (Phi-3 3.8B). This provides reasonable evidence that the method produces text that is *statistically* similar to human-written text according to LLM probability estimates.

- **Engaging philosophical framing.** The discussion of hallucinations as a failure of intention rather than factuality (drawn from Tacitus and Oulipo parallels), and the questioning of what it means for an LLM to "know" something when it can serve as a conduit for information it is supposedly incapable of expressing, is genuinely thought-provoking. The Shibbolethian Theatre scenario (Figures 11–12) is a novel and alarming application that concretely illustrates AI safety implications.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative comparison to prior LLM steganography methods.** The paper mentions Meteor (Kaptchuk et al., 2021), Wu et al. (2024), and Zamir (2024) in Section 2, but never benchmarks Calgacus against any of them on standard metrics: bit rate, stegotext perplexity, human detection rate, or throughput. The paper claims the "notable property of having full capacity" (same-length stegotext and secret), but without any quantitative baseline comparison, it is impossible to assess whether this property translates into any practical advantage over existing methods, or whether the trade-offs (e.g., inability to choose high-rank tokens freely, detectable probability shifts) make it less useful. This is not a missing ablation — it is a fundamental failure to situate the claimed contribution in the literature.

- **No human evaluation of stegotext detectability despite explicit claims.** The paper states that stegotexts are "opaque to humans" (line 85) and that "for a human both the original and fake texts are plausible" (line 290), yet provides zero human evaluation. For a steganography protocol whose central goal is undetectability, this gap is severe. A Turing-like test or even a small-scale human rating study is essential to support these claims. All evidence is based on LLM-assigned log-probability, which is partially circular (the same model family used to generate stegotexts is used as the judge; Figure 14 partially addresses this with a different model, but still relies on an LLM rather than human judgment).

### Minor

- **The scale of the main experiment is small.** Only 3 original texts (chosen at \(\mu, \mu-2\sigma, \mu+2\sigma\) of the Reddit distribution) and 100 stegotexts each are evaluated. While the results are consistent, a larger and more diverse set of original texts would substantially strengthen confidence in the method's generality. The paper does not systematically study how the capacity-quality trade-off varies with different secret message domains, lengths, or perplexities.

- **Security analysis is informal and lacks threat modeling.** The paper explicitly states it will not frame the method in a formal security model (lines 123–125), which is a reasonable scope choice. However, given that the paper claims safety and security implications (e.g., "nips [attacks] in the bud" line 377), the security discussion is overly informal. There is no treatment of stronger threat models (known-plaintext, chosen-message attacks), no empirical steganalysis, and the deniability claim rests on a single cherry-picked example (Figure 15). A systematic search for plausible bogus keys across many secret messages would be needed to substantiate the deniability claim.

- **The novelty of "full capacity" requires clearer articulation.** The paper defines "full capacity" as equal-length stegotext and secret, which is a direct consequence of rank-based encoding. Prior variable-length steganography methods can encode messages of arbitrary length by adjusting bits per token; they do not guarantee same *token length* because they do not attempt to. The paper would benefit from a more precise discussion of what "full capacity" enables that prior methods cannot do, rather than presenting it as an uncontested advantage.

### Trivial
None.

## Nice-to-Haves

- A systematic study of how often high-rank tokens degrade stegotext quality, with quantitative coherence scores across varied secret messages.
- An empirical steganalysis experiment (e.g., token-rank distribution divergence, autoencoder-based detection) to complement the log-probability analysis.
- A larger-scale deniability experiment (systematic search for plausible bogus keys across many secret messages).

## Removed Points

- **Criticism about "full capacity" being inaccurate / prior methods having same capability.** The reviewer claimed prior methods can achieve "arbitrary compression ratios" and that same-length encoding is not a lacking capability. However, prior methods embed bits into tokens and produce stegotexts whose length depends on the bit-to-token encoding ratio, not the token-length of the secret. Same-length is a genuine property of rank-based encoding that prior methods do not guarantee. The criticism is not factually wrong per se, but overstates the capability of prior methods. *Kept as a weakened point in Minor section.*

- **Criticism about missing appendices / proofs.** The parser strips appendices from all papers; they exist in the original submission. *Removed per hard rule.*

- **Nitpicks about formatting, typos, broken characters.** These are parser artifacts. *Removed per hard rule.*

- **Strength about "improving on prior methods that embed fewer bits per token."** The strength finder claimed Calgacus improves on prior methods, but the paper provides no quantitative comparison to support this. This strength conflicts with the verified major weakness (no baseline comparison). *Moved here — the weakness wins.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper that the paper does not already articulate itself.

## Suggestions

1. **Add baseline comparisons.** Evaluate Calgacus against Meteor, Zamir, and Wu et al. on a common set of secret messages. Report bit rate (bits per token), stegotext perplexity (under a held-out LLM), and a human detection rate study. This is the single most important revision.
2. **Conduct a human evaluation.** At minimum, a small-scale Turing-like study where raters distinguish stegotexts from real texts of comparable topic/length. Report detection rates and confidence intervals.
3. **Expand the empirical evaluation.** Test on more original texts (e.g., 30+ rather than 3), more domains, and more varied lengths. Quantify the frequency of incoherent stegotexts.
4. **Strengthen the security discussion.** Even without a formal model, provide a threat model (adversary capabilities, goals), a systematic deniability experiment (search for bogus keys across many messages), and at least one simple steganalysis baseline (e.g., rank-distribution divergence).

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/q4qxtaKVAU.md` | 6.00 | *Early Signs of Steganographic Capabilities* — thorough empirical evaluation of LLM steganography with multiple models, metrics, and threat models. The current paper has much weaker evaluation but offers a novel protocol + philosophical discussion absent from this anchor. |
| `/home/wg25r/review_agent/human_reviews_2026/6cEPDGaShH.md` | 6.00 | *Invisible Safety Threat* — rigorous steganographic attack evaluation with AdvBench, multiple models, and LlamaGuard classification. Much stronger experimental methodology. Current paper is less rigorous. |
| `/home/wg25r/review_agent/human_reviews_2026/ZujfJpD6as.md` | 3.50 | *Hiding in Plain Sight: StegoAttack* — steganographic jailbreak with missing baselines and overclaimed results. Current paper has a cleaner protocol but similarly lacks thorough evaluation and baseline comparisons. |
| `/home/wg25r/review_agent/human_reviews_2026/nrinbZTy26.md` | 3.50 | *Eliciting Secret Knowledge* — empirical benchmark with limited novelty. Current paper has more novel conceptual contribution but similar evaluation limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/nDSTDq0uDK.md` | 2.00 | *Watermarks via Probabilistic Automata* — fundamentally flawed theoretical claims. Current paper has no such theoretical flaws. |
| `/home/wg25r/review_agent/human_reviews_2026/a195V8Qp4Z.md` | 2.50 | *Low-frequency Image Information Hiding* — image steganography paper with weak evaluation. Current paper is clearer and more reproducible. |
| `/home/wg25r/review_agent/human_reviews_2026/TVSPV6D0co.md` | 4.67 | *Fast, Secure Image Watermarking* — image-domain steganography with solid evaluation. Current paper has a more novel protocol but less rigorous evaluation. |

The paper presents a genuinely interesting protocol and a thought-provoking philosophical discussion. However, for a venue like ICLR, the experimental evaluation is insufficient to support the strong claims made. The lack of any comparison to prior LLM steganography methods, the absence of human evaluation despite explicit claims about human undetectability, and the very small scale of the main experiment (3 original texts, 300 stegotexts) are significant gaps. The paper is positioned between the clearly flawed papers (score 2–3) and the well-evaluated papers (score 6) in the calibration set. It has a real contribution in the protocol itself and the philosophical framing, but the evaluation falls short of what is needed.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>