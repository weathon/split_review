Now I have all the evidence I need. Let me construct the final review.

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for watermarking LLM-generated text entirely through prompt engineering, requiring no access to model internals, logits, or decoding. Four strategies are proposed across linguistic granularities (Unicode, Initials, Lexical, Acrostics), each with tailored detection methods. The paper evaluates ICW in a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) case study motivated by detecting AI-generated peer reviews. Experiments on GPT-4o-mini and GPT-o3-mini show that with sufficiently capable models, ICW achieves strong detection accuracy, robustness to paraphrasing, and high text quality — while opening up watermarking scenarios previously inaccessible to existing methods.

## Strengths

1. **Genuinely novel paradigm for LLM watermarking.** ICW embeds watermarks solely through prompt engineering, bypassing the need for model access (weights, logits, or sampling). This is conceptually distinct from both in-process methods (which require decoding control) and post-hoc methods (which modify existing text), filling a real gap for scenarios like peer-review detection where the watermarking party has zero visibility into the model used. The paper's core idea — that instruction-following capability can be repurposed for watermarking — is original and timely.

2. **Strong results on capable models in both settings.** Table 2 shows that on GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in the DTS setting and ≥ 0.997 in the IPI setting. Acrostics and Unicode ICW reach perfect or near-perfect T@1%F scores. The IPI results (full papers as context) demonstrate that ICW instructions can be followed even in long-context scenarios, which is non-trivial.

3. **Demonstrated robustness to paraphrasing.** Figure 3 shows that on GPT-o3-mini, Initials, Lexical, and Acrostics ICW maintain AUCs of 0.887, 0.924, and 0.922 respectively under LLM paraphrasing, outperforming PostMark (0.841) and YCZ+23 (0.557). This is non-trivial — paraphrasing is the most challenging attack for most watermarks.

4. **High text quality with minimal degradation.** Table 3 reports that Lexical and Acrostics ICW achieve overall LLM-as-a-Judge scores of 4.808 and 4.813 (near the unwatermarked baseline of 4.992), far exceeding PostMark (2.997) and YCZ+23 (3.865). ICW methods do not sacrifice output quality, a critical requirement for deployment.

5. **Systematic exploration and trade-off analysis.** The four strategies span Unicode (character-level), Initials (letter-level), Lexical (word-level), and Acrostics (sentence-level). Table 1 provides a concise qualitative summary of trade-offs, and each method's discussion identifies its specific failure modes — giving practitioners a clear decision framework.

## Weaknesses

### Major

1. **"Model-agnostic" claim is misleading given the extreme model-dependence of results.** The abstract calls ICW "model-agnostic," but Table 2 tells a different story: Initials ICW goes from 0.572 AUC (GPT-4o-mini) to 0.999 (GPT-o3-mini); Acrostics goes from 0.590 to 1.000. On GPT-4o-mini — the more accessible and widely-used model — only the trivial Unicode method works reliably. ICW is better described as "model-access-agnostic" but critically dependent on model capability. The paper acknowledges this in text (Table 2 caption, Section 5.2.1) but the abstract overclaims. Since the practical relevance of any watermarking method depends on when it works today, not on speculative future capability, this significantly tempers the claimed impact.

2. **IPI setting lacks realistic deployment validation.** The paper's marquee application (detecting AI-generated peer reviews) hinges on covertly embedding watermarking instructions in papers via "white text" or zero-font characters, and assumes the reviewer uploads the full PDF as-is to an LLM. The experiments simply concatenate the instruction with the paper text — a synthetic test. The paper does not test whether hidden text survives common PDF→text conversion pipelines (pdftotext, OCR, copy-paste from PDF viewers), nor does it address that a dishonest reviewer aware of this mechanism could easily strip hidden text or use a screen reader. The paper flags this as future work, but since the IPI case study is central to the paper's motivation (Section 1, Figure 2, Table 2 IPI columns), the absent validation substantially weakens the claimed practical significance.

### Minor

3. **No adaptive adversary evaluation.** The robustness evaluation (Figure 3) tests only random word deletion, synonym replacement, and LLM paraphrasing. The paper itself acknowledges (Section 4.2.2) that Initials ICW's green letter set "can be easily inferred, making the method vulnerable to spoofing attacks." A knowledgeable adversary could recover the green set from a handful of samples and replace those tokens. For Acrostics ICW, an adversary aware of the scheme could rephrase sentences to break the acrostic pattern. The paper does not evaluate against any informed adversary, leaving the claimed robustness unsubstantiated against motivated attackers.

4. **Null distribution mismatch for detection statistics.** Initials and Lexical ICW estimate the null distribution of green proportions from the Canterbury Corpus, not from the evaluation domain (ELI5 or academic reviews). Domain-specific letter/word frequency shifts could inflate or deflate false positive rates in practice. For Acrostics ICW, the null distribution is estimated by resampling sentence-initial letters from the suspect text itself, which is circular when the text may be watermarked. The paper provides theoretical false-alarm guarantees (Appendix B), but no empirical validation on domain-matched human text.

5. **Unicode ICW — the only method that works on GPT-4o-mini — is trivially fragile.** Unicode ICW achieves perfect AUC on both models but is admitted to be "highly fragile to transformations like LLM paraphrasing" (Section 4.2.1). Any paraphrase, format conversion, or text re-rendering would strip zero-width spaces. This is essentially known steganography (Sato et al., 2023), not a novel contribution to robustness.

6. **LLM-as-a-Judge evaluation uses gemini-2.0-flash, which may have its own biases.** The text quality assessment (Table 3) relies on a single LLM judge. Perplexity is measured with LLaMA-3.1-70B, but watermarked text might have artificially low perplexity due to constrained vocabulary rather than genuinely better fluency. No human evaluation is provided.

### Trivial

- The term "model-agnostic" in the abstract should be qualified (discussed above under Major).
- Figures referenced in the main text (Table 6 for IPI robustness, Figure 4 for perplexity) are deferred to the appendix, making inline reading harder.

## Nice-to-Haves

- Perform a realistic IPI survivability test: embed watermarking instructions via white-text/zero-font in a PDF, run through standard PDF→text converters, and verify instruction survival before LLM querying.
- Implement a simple adaptive adversary that infers the green set from watermarked samples and replaces matching tokens — this would either validate robustness or reveal a clear failure mode.
- Validate false positive rates empirically on domain-matched human text (e.g., human-written ELI5 answers or real peer reviews) rather than relying solely on Canterbury Corpus estimates.
- Vary watermark strength (green set size, frequency requirement) and show the detectability vs. quality trade-off curve.
- Test on at least one open-source model (e.g., LLaMA-3.1-70B) to demonstrate model-independence and enable community reproducibility.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **Claim that Table 1 contradicts itself for Unicode ICW's robustness.** The critic states Unicode is "rated high on Detectability and Robustness" in Table 1, but the table clearly shows ○ (lowest) for Robustness, consistent with the text that calls it "highly fragile." This is a misreading. **Removed.**

- **Claim that the paper doesn't highlight the asymmetry between GPT-4o-mini and GPT-o3-mini results.** Section 5.2.1 explicitly states: "Initials and Acrostics ICWs require substantially higher model capabilities... exhibit very low detection performance when used with GPT-4o-mini." The asymmetry is discussed. **Removed.**

- **Criticism of baseline selection (PostMark, YCZ+23) as unfair.** The paper clearly explains why these post-hoc baselines are chosen (they are the few open-source black-box methods) and why in-process methods requiring model access are inapplicable. The critic acknowledges there is no in-process black-box baseline — this is not a weakness but the paper's premise. **Removed.**

- **Criticism about missing related works.** The instruction prohibits this. **Removed per protocol.**

- **Criticism about missing appendix content, proofs, references.** The parser strips these; they exist in the original submission. **Removed per protocol.**

- **Formatting/style nitpicks and typos.** **Removed per protocol.**

## Novel Insights

A genuinely interesting observation emerging from the review process is that ICW inverts the standard watermarking trust model: instead of the *model provider* embedding watermarks during generation, ICW empowers *third-party input controllers* (e.g., conference organizers) to watermark through the input channel. This reframes watermarking as a prompt-security problem rather than a decoding-probability problem. However, this inversion also introduces new attack surfaces — the same prompt injection techniques used to embed watermarks can be used to remove or spoof them — that the paper does not yet address. The finding that ICW's effectiveness scales sharply with model capability (from AUC ~0.6 on GPT-4o-mini to ~1.0 on GPT-o3-mini for Initials/Acrostics) provides a concrete empirical anchor for discussions about when prompt-based watermarking becomes viable.

## Suggestions

1. **Revise the abstract's "model-agnostic" claim** to "model-access-agnostic" or clarify that ICW does not require model internals access but its effectiveness depends strongly on the model's instruction-following capability.  
2. **Add a single experiment validating the IPI deployment channel** — take a PDF with white-text or zero-font instructions, convert it with a standard tool (e.g., `pdftotext`), and show the instruction reaches the LLM. If this fails, at minimum the paper should discuss this limitation honestly rather than deferring entirely to future work.  
3. **Add one adaptive attack experiment** — even a simple one where the adversary infers the green letter set from watermarked samples and removes matching words — to bound the claimed robustness.  
4. **Empirically validate false positive rates** on domain-matched human text (e.g., human-written ELI5 or real review text) for Initials and Lexical ICW.

## Score and Decision

I calibrate against the following anchor papers retrieved from the corpus:

- **WASA: Watermark-based Source Attribution** (avg 5.50, Reject) — Similar watermarking paper with moderate novelty. ICW has a more novel paradigm (prompt-based vs. Unicode-based) but its evaluation is similarly incomplete. ICW is slightly stronger.

- **Can Watermarked LLMs be Identified by Users via Crafted Prompts?** (avg 7.50, Accept) — Well-executed paper with comprehensive evaluation. ICW has higher conceptual novelty but weaker empirical completeness. ICW is notably weaker.

- **A Watermark for Black-Box Language Models** (avg 4.60, Reject) — Also addresses black-box watermarking but requires API sampling access. ICW's prompt-only approach is more novel and more practical (no repeated sampling needed), and ICW has clearer experiments. ICW is significantly stronger.

- **Optimizing Adaptive Attacks against Content Watermarks** (avg 5.50, Reject) — Different contribution type (attack methodology), well-executed. ICW has comparable quality but its contribution type (new method) has higher potential impact.

- **WAPITI: A Watermark for Finetuned Open-Source LLMs** (avg 3.75, Reject) — Parameter-based method with limited evaluation. ICW is clearly stronger in both novelty and evaluation.

The paper introduces a genuinely novel paradigm and the core experiments are clean and well-designed. However, the overclaimed "model-agnostic" framing, the unvalidated IPI deployment mechanism, the absence of adaptive adversary evaluation, and the fact that on today's widely-deployed models (GPT-4o-mini) only the trivial Unicode method works, collectively mean the evidence does not yet support the paper's strongest claims. The contribution is promising but incomplete.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>