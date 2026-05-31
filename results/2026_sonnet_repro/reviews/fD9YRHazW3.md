Now let me do calibration searches to score the paper.Now I have enough information to write the final review.

---

## Summary

This paper introduces **In-Context Watermarking (ICW)**, a model-agnostic approach that embeds watermarks into LLM-generated text purely through prompt engineering, without any access to the model's decoding process. Four strategies are proposed—Unicode, Initials, Lexical, and Acrostics—evaluated in both a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) setting targeting AI-generated peer review detection. With GPT-o3-mini, all four methods achieve near-perfect detection AUC (0.995–1.000 in DTS), and the IPI results demonstrate that capable LLMs can follow hidden watermarking instructions embedded in full academic papers.

---

## Strengths

- **Novel and well-motivated paradigm.** ICW fills a genuine gap: most watermarking requires model access, but in many real scenarios (e.g., dishonest peer reviewers using third-party LLMs) the deployer has no such access. The IPI peer review case study is a creative, practically motivated application of the idea.

- **Effective with capable models.** With GPT-o3-mini, all four ICW methods achieve ROC-AUC of 0.995–1.000 in the DTS setting (Table 2), matching or exceeding post-hoc baselines (YCZ+23: 0.998, PostMark: 0.977). The IPI results are similarly strong (Lexical: 0.997, Acrostics: 0.997), demonstrating that LLMs can reliably follow watermarking instructions embedded within long documents.

- **Systematic trade-off characterization.** The paper evaluates all four strategies across detectability, robustness, text quality, and LLM requirement dimensions (Table 1), providing a useful comparative map. For example, Initials ICW shows AUC of 0.999 under word deletion and replacement attacks (Figure 3), while Acrostics ICW achieves AUC 1.000 under replacement—both outperforming baselines in these conditions.

- **Preserved text quality.** LLM-as-a-Judge evaluation (Table 3) shows ICW methods achieve relevance scores of 4.918–4.960 versus 4.982 for unwatermarked text with o3-mini, confirming the watermarking instructions cause minimal degradation to content accuracy.

---

## Weaknesses

### Fatal
None.

### Major

- **Evaluation restricted to two models from a single provider undermines the "model-agnostic" claim.** The entire experimental evaluation uses only GPT-4o-mini and GPT-o3-mini (Section 5.1). No open-weight models (e.g., LLaMA-3, Mistral, Qwen) or other providers are tested. The paper's central framing—that ICW is "model-agnostic" and practical across "wider scenarios"—is not supported by evidence from a single provider. A more honest framing would acknowledge this as a single-provider preliminary study. This limitation also means the paper cannot characterize *what model capability threshold enables reliable ICW*, which would be its most practically useful claim.

- **Performance collapses on the weaker model, yet the paper's forward-looking framing obscures this.** Table 2 shows Initials ICW at AUC 0.572 and Acrostics ICW at 0.590 with GPT-4o-mini—both barely above chance. The paper frames this as "as LLMs continue to advance, ICWs will become correspondingly more powerful," which is speculative and circular. Three of four proposed methods essentially fail at the capability level of GPT-4o-mini, meaning the practical method today is largely restricted to frontier models (o3-mini-level). The paper's headline contribution is not as broadly practical as presented.

- **IPI mechanism rests on an untested practical assumption about PDF text extraction.** The IPI scenario depends on hidden text (zero-font or white-color instructions in a PDF) surviving conversion and being followed by the LLM. The paper describes this as established via "prompt injection attacks" but does not test whether actual PDF-to-text pipelines preserve invisible characters, nor whether LLM APIs process them. Many document ingestion pipelines strip invisible or unusual characters. The paper does not present a single end-to-end IPI demonstration with a real PDF—experiments appear to treat IPI as simply prepending a long text to the watermarking instruction (Section 3.2, Equation 2). This is a feasibility question central to the paper's application claim.

### Minor

- **Acrostics detection has a potential statistical circularity.** The z-statistic for Acrostics ICW (Section 4.2.4) estimates the null-distribution mean µ and standard deviation σ by resampling sentence initial letter sequences *from the suspect text itself*. If the text is already watermarked, these resamples are drawn from a distribution already biased toward the key ζ, potentially inflating the z-score artificially. Unlike Initials and Lexical ICW (which reference an external corpus and provide formal guarantees cited to Appendix B), no theoretical guarantee for Type I error control is cited for Acrostics ICW. This undermines the reliability of the false-positive-rate control claims for this method.

- **Canterbury Corpus calibration may be miscalibrated for test genres.** Section 4.2.2 estimates γ (the baseline initial-letter distribution) from the Canterbury Corpus—general English prose. The evaluation is on ELI5 (long-form QA) and ICLR paper reviews, which may have different first-letter distributions. Systematic genre mismatch would miscalibrate the z-statistic and compromise false positive rate control without being apparent in AUC results.

- **GPTZero appears in the baselines section but not in the main results.** Section 5.1 lists GPTZero as a baseline in the DTS setting, but it does not appear in Table 2 or Figure 3. The reason for its exclusion is not stated.

### Trivial
- Section 5.2.1 refers to the "ignore prior prompts" attack being evaluated in the appendix without reporting summary findings in the main text—a missed opportunity to directly address one of the most natural adversarial strategies against IPI.

---

## Nice-to-Haves

- Evaluate at least one capable open-weight model (e.g., LLaMA-3-70B or Qwen-72B) and one model from a different provider (e.g., Claude Sonnet or Gemini Pro) to bound the capability threshold for reliable ICW, rather than leaving it implicit.
- Provide an actual end-to-end IPI demonstration: create a PDF with hidden watermarking instructions, convert it through a realistic reviewer workflow (drag-and-drop or API submission), and show whether the instruction survives and is followed.
- Supplement the Acrostics detection with an empirical calibration study showing that the bootstrap z-statistic achieves nominal Type I error control at the claimed levels.
- Report some summary statistics from the "ignore prior prompts" attack in the main text, as it is among the most natural adversarial strategies.

---

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **"Baseline comparison is structurally misleading"** (harsh critic §4): The critic argues the paper misrepresents ICW as "competitive" with baselines. However, the paper's own text (Section 5.2.1) qualifies this as "comparable to that of the two baselines... when used with high-capability LLMs." The baselines' exclusion from IPI is correct (they require post-hoc access to the reviewer's text), and the paper is transparent about GPT-4o-mini failures. **Removed as strawman** — the paper does not overclaim.

- **"Conclusion is asymmetric about capability dependence"** (harsh critic §6): The critic flags that the conclusion does not discuss adversarial prompting against capable LLMs. This is a nice-to-have for future work, not a weakness that undermines the paper's claims. **Removed as scope creep.**

- **"Strength: Effective demonstration of capability-dependent success"** (strength finder §1): This was rephrased and partly subsumed into the Weaknesses section — the capability dependency cuts both ways. The strength observation is valid but should not be separated from its flip side (failure on weaker models). **Kept in weaknesses for balance.**

---

## Novel Insights

The most genuinely novel insight surfaced by the reviewers (and present in the paper itself) is that the *gap between what a capable LLM can do and what a weaker one can do* is itself a watermark signal — the same capability differential that makes o3-mini reliable makes GPT-4o-mini unreliable. The practical implication is an interesting inversion: ICW is easiest to deploy when the adversary uses the most capable models, and weakest when the adversary uses cheaper models. This adversarial dynamic is not fully discussed in the paper but is directly visible in Table 2 and deserves more explicit treatment.

---

## Suggestions

1. **Model breadth (most important):** Add experiments on at least one open-weight model and one non-OpenAI API model. Report capability-dependent detection curves so readers can characterize the approximate threshold.
2. **IPI end-to-end validation:** Create a real PDF with hidden text, convert it using a standard API flow, and report whether the watermark instruction is followed. Even a single such demonstration would substantially change the confidence level of the IPI claims.
3. **Acrostics calibration:** Include a small empirical study showing that the bootstrap z-statistic in Section 4.2.4 produces calibrated Type I error (e.g., 1% threshold → 1% empirical false positive rate on unwatermarked text). This is a targeted fix, not a major redesign.
4. **Clarify the "model-agnostic" framing:** The paper's framing should either (a) demonstrate model-agnosticism with broader coverage, or (b) reframe as a "capability-gated" approach and characterize the capability threshold — which is a valid and interesting contribution in its own right.

---

## Score and Decision

**Calibration summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| FDfq0RRkuz.md (WASA) | 5.50 | R1 | Watermarking paper with unclear threat model, poorer organization; ICW is better |
| 0KHW6yXdiZ.md (E2E logits) | 5.25 | R1 | Technically rigorous but requires model internals; ICW more novel but narrower eval |
| 0koPj0cJV6.md (Black-box watermark) | 4.60 | R2 | Requires API-level access; rejected partly for underdiscussed practicality — very similar issue to ICW |
| DEJIDCmWOz.md (Reliability of watermarks) | 6.00 | R2 | Accepted; studies existing watermark robustness, well-executed. ICW is more novel but has larger evaluation gaps |
| 3fEKavFsnv.md (MGT detection via MMD) | 6.50 | R2 | Accepted; theoretically grounded, multi-model evaluation. ICW weaker on evaluation breadth |
| rWjZWHYPcz.md (PaLD) | 6.25 | R2 | Accepted; detection of mixed-text. ICW comparable in novelty but narrower evaluation |
| eKGEsFdpin.md (Sampling-based WM) | 3.67 | R1 | Straightforward adaptation; ICW is significantly more novel |

**Round 1 bracket:** 5.0 – 7.0

**Round 2 narrowing:** The most directly comparable paper is 0koPj0cJV6 (4.60, Rejected), which was rejected partly because of an underdiscussed gap between the paper's "black-box" framing and its actual demonstration — exactly the same structural issue as ICW's "model-agnostic" claim vs. two-OpenAI-model evaluation. ICW is more novel (no model access whatsoever, vs. still requiring API sampling control), which pushes it above 4.6. The accepted papers at 6.0–6.5 have more comprehensive evaluations and/or stronger theoretical footing. ICW sits between these groups: genuinely novel and well-executed on a capable model, but with a significant evaluation gap. The lack of multi-model evidence for the core claim, combined with the unvalidated IPI PDF mechanism, places this below the 6.0 acceptance threshold but clearly above the 4.6 rejected paper.

**Final score:** 5.5 — positioned above 0koPj0cJV6 for higher novelty, but below DEJIDCmWOz because the evaluation breadth doesn't support the scope of the paper's claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>