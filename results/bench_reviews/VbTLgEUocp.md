Now I have read the paper and the calibration anchors thoroughly. Let me synthesize the final review.

---

## Summary

Calgacus is a simple LLM-based protocol that hides a text $e$ inside another text $s$ of the same token length. The method records the ranks of $e$'s tokens under an LLM's probability distribution, then generates $s$ by prompting the same LLM with a secret key $k$ and choosing the $r_i$-th most probable token at each step. The hidden text can be exactly recovered by anyone who knows $k$. The paper discusses implications for AI safety (encoding unfiltered LLM answers within aligned responses) and offers a philosophical reframing of hallucinations as a void of intention rather than mere falsehood.

## Strengths

- **Elegant protocol with a genuinely novel property.** The method achieves full-capacity steganography — the stegotext and hidden message have the same token length — which prior LLM-based steganography methods (Meteor, Wu et al., Zamir) do not offer. The recipe is simple, deterministic, and requires only access to output logits. The correctness of encoding/decoding is straightforward.

- **Practical and lightweight.** The method works with an 8B-parameter open-source model on consumer hardware, with encoding/decoding reportedly taking seconds for a message as long as the paper's abstract. The linked demo code supports reproducibility.

- **Insightful analysis of the probability gap between real and stegotexts.** The low-entropy token choice analysis (Figure 5, Section 3) explains why stegotexts are slightly less probable than originals despite preserving token ranks: rank-1 tokens are "wasted" on high-entropy positions, creating an identifiable but not necessarily detectable gap. This deepens understanding of the protocol's behavior.

- **Thought-provoking discussion connecting the protocol to broader questions about LLM intentionality.** The reframing of hallucinations as a failure of ascribed intent (rather than factual error), the Oulipo analogy, and the "unaligned chatbot disguised as aligned" scenario are genuinely interesting contributions to the discourse on trust in machine-generated text.

## Weaknesses

### Fatal

None.

### Major

- **Empirical validation is too narrow to support the central claim about steerable, coherent stegotexts.** The paper claims Calgacus can hide a meaningful text inside another meaningful text of the same length, with the stegotext's topic steerable via $k$. However, the quantitative evaluation uses only three source texts (85 tokens each) × 100 prompts = 300 stegotexts, all assessed solely by cumulative log-probability under a single LLM (Llama 3 8B). Log-probability measures token-level plausibility but says nothing about global coherence, semantic relevance to the prompt $k$, or whether the stegotext actually follows the intended topic. The paper itself acknowledges that log-probability is an imperfect proxy for meaningfulness ("Measuring the meaningfulness of a text is a longstanding linguistic challenge"), yet provides no systematic human evaluation, automated coherence metric, or prompt-relevance measure. The qualitative examples (Figures 1, 13) are compelling but anecdotal; they do not establish that steerability holds in general across diverse $e$ and $k$. Without this evidence, the paper's core contribution — hiding one meaningful text inside another steerable, meaningful text — is partly unsubstantiated.

- **No comparison with existing generative steganography methods.** The paper explicitly positions Calgacus relative to Meteor, Wu et al., and Zamir in the Related Work, and correctly identifies full capacity as its distinguishing property. But it does not benchmark against any of these methods on capacity, undetectability, or output quality. Without such comparison, it remains unclear whether full capacity comes at a cost in other dimensions (e.g., coherence, detectability) that prior methods handle better. This makes the claimed advantage over prior work difficult to assess.

### Minor

- **Security and deniability analysis is informal and sparse.** The security section (3.1) provides a brute-force complexity argument and notes that a random string in $k$ defeats search, which is reasonable. However, there is no steganalysis test against even a simple classifier trained to distinguish real texts from Calgacus stegotexts, and deniability is supported by a single example (Figure 15, appendix). The paper is honest about not framing itself in a formal steganography model, but the security claims (e.g., "our method provides deniability") remain under-supported. This does not invalidate the protocol's value but limits confidence in the claimed security properties.

- **Limited diversity of evaluation texts.** Only three source texts (all Reddit posts, all 85 tokens, selected at μ, μ−2σ, μ+2σ of the real-text distribution) are used. Dependence of output quality on the entropy of $e$, the match between $e$'s rank distribution and $k$'s context, and text length is discussed only qualitatively or deferred to appendices. A broader evaluation with longer texts and more diverse $e$/$k$ pairs would strengthen confidence in the method's generality.

### Trivial

- The discussion section's AI-safety scenario (Section 4) is presented as a concrete demonstration, but the paper does not evaluate whether the resulting stegotexts would survive content-based filters or appear distinguishable from ordinary aligned responses. This is a scope limitation rather than a flaw — the scenario serves as an illustration, not a rigorous security evaluation.

## Nice-to-Haves

- A human study or LLM-as-judge evaluation of stegotext coherence and prompt-relevance would substantially strengthen the paper's central claims. Even a small-scale study (e.g., 50 annotators rating 20 stegotexts) would go a long way.
- A simple steganalysis experiment (e.g., training a logistic regression classifier on token-logit statistics to distinguish real from Calgacus-generated texts) would add empirical weight to the undetectability claims.
- Benchmarking against at least one existing generative steganography method on capacity and quality would clarify the trade-offs of full-capacity encoding.
- A theoretical bound on when the rank-transfer procedure preserves coherence (e.g., relating output quality to KL divergence between $e$'s and $k$'s token distributions) would strengthen the contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The three anecdotal examples in Figure 1 and the additional examples in Figure 13 provide no systematic demonstration" (from Harsh Critic #1):** The examples are indeed qualitative and not systematic, but the core concern — lack of systematic coherence/steerability evaluation — is already captured in the Major weakness above. The dismissive "anecdotal" framing is removed.

- **"The method's novelty and advantage over existing generative steganography are neither articulated" (from Harsh Critic #2):** The paper *does* articulate the novelty (full capacity, same-length encoding). The valid concern — no benchmarking — is kept as a Major weakness.

- **"The discussion of attack scenarios rests on brute-force complexity heuristics and hand-waving about natural-language constraints on k" (from Harsh Critic #3):** The security analysis is indeed informal, but the paper is upfront about avoiding formal steganography models. The valid concern is kept as a Minor weakness. Inflammatory language ("hand-waving," "vacuous") removed.

- **"The claim that inserting a random string in k 'nips [search] in the bud' is unsupported" (from Section-by-Section Notes):** The paper shows an example in Figure 13. The basic argument (random strings expand the search space combinatorially) is sound. This is not a genuine weakness.

- **"The AI-safety alarm depends on the method working reliably and stealthily. The paper never investigates whether the resulting stegotext would be flagged by simple content-based filters" (from Section-by-Section Notes):** The AI-safety scenario is presented as a demonstration/thought experiment, not as a claim of proven stealth. Moved to Trivial as a scope note.

- **"Thorough treatment of security and deniability" (from Strength Finder):** Overstated. The security section is 2 paragraphs and deniability rests on one example. Moved to Removed Points.

- **"Convincing demonstration that stegotexts are plausible real-world texts" (from Strength Finder):** Partially kept but qualified. The log-probability evidence is real but limited to 3 source texts and one LLM, so "convincing" is too strong. The qualified version appears under Strengths.

- **"The framing about radical decoupling of text from intent... is put forward before the method's core properties have been established by evidence" (from Section-by-Section Notes):** This is a presentation preference, not a substantive weakness. Removed.

- **"The statement 'If e is sound, we expect ranks to be low, making tokens chosen after k highly probable, ensuring s is coherent' is an intuition, not a proven guarantee" (from Section-by-Section Notes):** The paper presents this as a consideration/expectation, not a theorem. Not a genuine weakness. Removed.

## Novel Insights

The paper's most original observation is the low-entropy token choice analysis: stegotexts are less probable than originals because rank-1 tokens are "wasted" on high-entropy positions where they would have been selected anyway by normal sampling, while at low-entropy positions (where the model is nearly certain), the protocol often fails to select rank 1. This creates a systematic, identifiable probability gap that does not, however, push stegotexts outside the real-text distribution. This insight about *where* the capacity cost is paid is genuinely novel and could inform future steganography designs.

## Suggestions

- The strongest path to strengthening the paper is a systematic evaluation of steerability and coherence. Even 2–3 source texts with 5–10 prompts each, rated by human annotators or an LLM judge for topic alignment and coherence, would substantially address the main weakness.
- Adding a simple steganalysis baseline (e.g., classifier on token probability features) would transform the security section from speculative to empirically grounded with minimal effort.
- The discussion section is the paper's most distinctive contribution and should be preserved, but it would land harder if preceded by stronger empirical evidence.

## Score and Decision

### Anchor comparison:

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| q4qxtaKVAU | Early Signs of Steganographic Capabilities in Frontier LLMs | 6.00 | Stronger empirical evaluation (multiple models, systematic methodology) but narrower conceptual contribution. Our paper has a more novel protocol but thinner validation. Below this anchor. |
| 6cEPDGaShH | Invisible Safety Threat: Malicious Finetuning for LLM via Steganography | 6.00 | Strong empirical validation on multiple models including GPT-4.1 API, quantitative safety evaluation. Our paper has more elegant core idea but substantially weaker evaluation. Below this anchor. |
| gdZ6J5hZzF | Sequences of Logits Reveal the Low Rank Structure of Language Models | 7.33 | Both empirical and theoretical contributions, thorough validation. Our paper is clearly below this level. |
| t38nZqqi3Z | LLM Fingerprinting via Semantically Conditioned Watermarks | 6.50 | Strong empirical evaluation with clear methodology. Our paper is below this level. |
| EhDgP69DJG | PMark: Robust and Distortion-free Semantic-level Watermarking | 7.00 | Solid theory + experiments. Our paper is below this level. |
| ZujfJpD6as | Hiding in Plain Sight: Steganographic Approach to Stealthy LLM Jailbreaks | 3.50 | Limited novelty, replication concerns, evaluation issues. Our paper has a more genuinely novel protocol and is clearly stronger. |
| d1fVTnq3c8 | Bypassing Prompt Guards in Production | 2.50 | Insufficient novelty, extremely narrow evaluation. Our paper is clearly stronger. |
| qF6TyKhc7S | Majority Bit-aware Watermarking for LLMs | 4.00 | Technical refinement with limitations. Our paper has more conceptual novelty but similarly thin evaluation. Slightly above this anchor. |
| HhXOVhO3ia | Be Careful When Fine-tuning On Open-Source LLMs | 4.50 | Novel risk demonstrated with experiments. Comparable in evaluation breadth. Our paper has a more elegant core idea. |
| dZY5t9ZrUB | LLM Watermark Evasion via Bias Inversion | 4.50 | Theoretically motivated attack with evaluation. Comparable level. |

The paper introduces a genuinely novel and elegant protocol with a clear contribution (full-capacity steganography). The core method is correct and the implications discussed are thought-provoking. However, the empirical validation is thin: only 3 source texts, no systematic coherence/steerability evaluation, no comparison with prior methods, and an informal security analysis. These weaknesses are significant but not fatal — the method works as described, and the paper is honest about its scope limitations. Relative to the anchors, the paper sits above the 3.50–4.00 rejects (which had limited novelty or replication issues) but below the 6.00+ accepts (which had thorough empirical grounding). The paper is strongest where it is most original (the protocol itself, the probability-gap analysis, the philosophical discussion) and weakest where it is most conventional (empirical benchmarking, formal security analysis).

Each kept strength: the elegant full-capacity protocol is a genuine advance that distinguishes this work from prior methods; the practical lightweight implementation on open models makes the contribution accessible; the probability-gap analysis provides real insight into the protocol's behavior. These strengths lift the paper above a reject. But the thin empirical validation and lack of baselines prevent it from reaching the level of the 6.00 anchors. A score of 5.0 reflects a borderline-accept paper with a clear novel contribution that would benefit substantially from stronger validation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>