Now I have a thorough understanding of the paper and anchors. Let me write the consolidated review.

## Summary
This paper proposes the Language Confusion Gate (LCG), a lightweight plug-in MLP that dynamically masks token logits during decoding to prevent unintended language mixing in LLMs, without modifying base model parameters. The method is motivated by three observations: confusion is rare, correct-language tokens are typically among the top predictions, and high-resource language tokens have systematically larger output embedding norms. The gate is trained via norm-adjusted self-distillation using the frozen model's own debiased predictions as pseudo-targets. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS in both thinking and no-think modes, LCG reduces language confusion by an order of magnitude while preserving task performance and legitimate code-switching.

## Strengths
- **Novel mechanistic insight into norm imbalance (Section 3.2, Table 1):** The paper demonstrates that output token embedding norms are systematically larger for high-resource languages (e.g., CJ and Latin tokens dominate the top-5% norm group, while Low-Res tokens are heavily underrepresented). This provides a concrete, testable explanation for why models are biased toward high-resource language tokens, and directly motivates the norm-adjustment technique.

- **Comprehensive and convincing evaluation across diverse settings:** The evaluation spans four model families (Qwen3, Llama3.1, Gemma3, GPT-OSS), both thinking and no-think modes, translation benchmarks (FLORES+), knowledge benchmarks (INCLUDE), and code generation (Humaneval-XL). Table 3 shows consistent, large reductions in confusion (e.g., Qwen3-8B Latin confusion from 12.1% to 2.0%, CJ from 4.5% to 0.1%) with stable BLEU and accuracy. This breadth strengthens the generality claim.

- **Norm-adjusted self-distillation consistently outperforms unadjusted (Table 3):** Across all models, LCG-adjusted achieves lower confusion than LCG-unadjusted (e.g., Llama3.1-8B Latin% 2.9 vs. 5.7, Qwen3-30B Latin% 0.4 vs. 0.7), validating that the norm debiasing derived from the mechanistic analysis is crucial for gate accuracy.

- **The intervention is sparse and efficient:** Intervention occurs on only 0.38% of tokens for Qwen3-8B (Section 5.3), and the production benchmark shows a 0.4% increase in generation time (Section 6), supporting the claim of a truly lightweight, practical plug-in.

- **Preservation of legitimate code-switching is empirically demonstrated:** Human evaluation found that 86.7% of human-validated code-switch tokens were permitted by LCG, and Table 5 shows post-intervention code-switch rates remain above the Claude Sonnet 4 baseline, indicating the gate suppresses confusion without breaking necessary multilingual blending.

- **Honest about limitations:** The paper explicitly acknowledges the script-level granularity limitation (Section 6) and includes failure cases (Appendix J), which demonstrates intellectual honesty.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by the evidence presented.

### Minor
- **FLORES-NO-LATIN metric is a heuristic proxy for Latin confusion:** The paper defines Latin confusion in FLORES-NO-LATIN as any Latin character in output when the reference contains none (Section 5.2). While the paper acknowledges the challenge of distinguishing erroneous mixing from legitimate code-switching (Section 1), valid translations could contain Latin loanwords, proper names, or acronyms absent from the reference, inflating the measured confusion rate. The paper partially mitigates this through the separate code-switching evaluation (Table 5, human validation), and the CJ confusion metric is unambiguous. The Latin metric should be interpreted as an upper bound rather than a precise confusion rate; this nuance should be discussed more explicitly.

- **Pseudo-target training signal lacks direct validation (Section 4.2):** The gate is trained to match multi-label targets derived from norm-adjusted top-k/p logits, but the paper provides no direct evidence (e.g., oracle comparison, human annotation, correlation with ground-truth language appropriateness) that these pseudo-targets accurately reflect which language families are truly permissible. The norm-adjusted vs. unadjusted ablation in Table 3 provides indirect evidence that norm adjustment improves the training signal, but the absolute quality of the pseudo-targets remains uncharacterized.

- **Intervention rules ablated only as a bundle (Section 4.3, Figure 3):** The paper evaluates the three inference rules together in a "No Rule" vs. "LCG-adjusted" comparison (Figure 3), showing the gate still works without rules. However, Rule 2 (contradiction check against high-confidence model output) acts as a strong sanity check and could be doing substantial work. Without per-rule ablation, the relative contribution of the learned MLP versus the heuristic rules is not fully characterized. This does not invalidate the results but limits understanding of the method's components.

- **Section 3.1 confusion point analysis is from a single model on a single dataset:** The finding that language-consistent tokens appear in the top-3 at 99.29% of confusion points is derived from Qwen3-8B on FLORES-NO-LATIN only. While this is sufficient to motivate the masking approach, the generality of this observation across models and tasks is not established.

- **Human evaluation of code-switching lacks methodological detail (Section 5.3):** The 86.7% figure for human-validated code-switch tokens is reported without specifying the number of examples evaluated, annotator instructions, inter-annotator agreement, or annotator qualifications. This makes it difficult to assess the reliability of this finding.

### Trivial
- The specific top-k and top-p values used for pseudo-target construction during training (Section 4.2) are not reported, which is a minor reproducibility gap.
- The exact language pairs, split sizes, and filtering criteria for FLORES-NO-LATIN construction are described only at a high level (Section 5.2).

## Nice-to-Haves
- Confidence intervals or significance tests for BLEU and accuracy differences in Tables 3-4 would strengthen the claim that task performance is preserved.
- A sensitivity analysis of LCG's effectiveness under different sampling parameters (temperature, top-k, top-p) would help practitioners.
- Diagnostic case studies showing where the gate incorrectly blocks legitimate mixing and where it fails to block actual confusion, with analysis of the gate's internal predictions, would enrich the qualitative analysis beyond the existing success cases in Appendix I-J.
- Expanding the confusion point analysis (Section 3.1) to additional models and datasets would strengthen the generality of the motivating observations.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **Criticism about the FLORES-NO-LATIN metric being "unsalvageable" or that the "headline result" is undermined:** The paper uses multiple evaluation strategies (CJ confusion, Latin confusion as upper bound, code-switching preservation, human evaluation), and the core claim of confusion reduction is supported across all of them. The FLORES-NO-LATIN heuristic has limitations the paper itself acknowledges, but these do not invalidate the central empirical narrative. The metric is a reasonable practical compromise for a setting where perfect automatic detection is impossible. Removed as overstatement.

- **Criticism that "the connection to Large Reasoning Models is speculative":** The paper cites Guo et al. (2025) and Wang et al. (2025) to contextualize the problem, and separately evaluates LCG on thinking models (Table 4) with positive results. The connection is empirically demonstrated, not merely speculative. Removed as misunderstanding.

- **Criticism about token classification noise (ASCII punctuation/numbers classified as Latin):** The paper's classification heuristic (Section 4.1) first checks for CJ characters, then checks if characters consist only of Latin script AND symbols. Tokens that decode exclusively to symbols are classified as Symbols, not Latin. The remaining Latin tokens may include mixed alphanumeric tokens, but this is a reasonable classification for the purpose of norm analysis. Removed as factually incorrect.

- **Criticism about "no oracle study" for self-distillation and "the entire training procedure rests on a heuristic whose accuracy is unknown":** The norm-adjusted vs. unadjusted ablation directly validates that norm adjustment improves gate performance. The paper also provides mechanistic justification (Figure 2) showing that norm-adjusted logits remove confusion tokens from top ranks. While direct pseudo-target validation would strengthen the paper, the existing evidence is sufficient to support the method. Removed as overstatement.

- **Criticism that the paper should have used LCB instead of FLORES+:** The paper explicitly explains (Section 5.2, lines 509-514) why LCB was not used: some LCB queries require natural code-switching, and its language detector produces false positives. The authors designed a more controlled evaluation. Removed as the paper already addresses this.

- **Criticism about missing appendices or "too few" case studies:** The paper includes Appendices A through J covering token classification, additional evaluations, compute resources, ICL prompts, commercial LLM rates, speculative decoding, training data analysis, code-switch examples, intervention examples, and failure cases. This is extensive. The parser strips appendices — the original submission includes them. Removed as parser artifact / incorrect.

- **Criticism about typos, formatting, or broken characters:** These are parser artifacts, not issues in the original submission. Removed per hard rules.

- **Criticism about speculative decoding compatibility being "argued in prose only":** The paper explicitly states this is a design note and does not claim empirical validation for speculative decoding. Appendix F provides a detailed technical argument. Removed as scope creep — the paper does not claim to have empirically validated speculative decoding.

## Novel Insights
The finding that output token embedding norms are systematically imbalanced across language families (Section 3.2, Table 1) — with high-resource language tokens having larger norms that give them an unfair advantage in the logit computation — is a genuinely novel mechanistic observation. It explains why models can "know" the correct language (correct tokens appear in the top predictions) yet still sample incorrectly, and it provides a clean, principled basis for the norm-adjustment technique. The additional analysis in Appendix G, showing that norm imbalance is shaped by training data composition (using Olmo 3 pretrain vs. SFT checkpoints), strengthens this insight. This finding has implications beyond the specific LCG method and could inform future work on multilingual model training and decoding.

## Suggestions
- Report the specific top-k and top-p values used for pseudo-target construction, along with any sensitivity to these choices.
- Add details for the human evaluation of code-switching: number of examples, annotator instructions, inter-annotator agreement.
- Consider discussing FLORES-NO-LATIN Latin confusion rates as an upper bound rather than an exact measure, and explicitly note the types of false positives the metric may produce.
- The per-rule ablation of intervention rules would clarify the relative contribution of the learned gate vs. heuristics. Even a brief analysis of Rule 2 alone would be informative.

## Calibration and Score

### Anchor comparison

- **vzlDdOzXAh** (avg 4.50, Accept Poster): LGCD — gated contrastive decoding for multilingual factuality. Similar plug-in decoding approach but limited to QA benchmarks, two model families, and mid/high-resource languages. LCG has broader evaluation, novel mechanistic insight, and more practical justification. **LCG is clearly stronger.**

- **r00UxTl8El** (avg 5.33, Accept Poster): LinguaMap — layer-wise analysis of language control with selective fine-tuning. Two model families, three benchmarks, novel interpretive analysis. LCG has broader model coverage (4+ families vs. 2) and a more practical method applicable to any model without fine-tuning. **Comparable, with LCG having a slight edge in evaluation breadth and practical applicability.**

- **A5YyXBg79E** (avg 5.00, Reject): Language-specific latent process — primarily an analysis paper with activation steering, limited to multiple-choice tasks and two model families. **LCG is stronger** with a more complete contribution (analysis + method + comprehensive evaluation).

- **IKJyRyHpHV** (avg 5.50, Reject): Multilingual data mixtures — training-from-scratch experiments at 1B-3B scale with 25-400 languages. Different type of contribution (pretraining science vs. inference-time method). **Comparable contribution level; LCG's method is more immediately practical.**

- **ysT0BCmZ3S** (avg 3.00, Reject/Withdrawn): Language Matters — surface-level analysis of reasoning language, limited experimental scope, writing issues. **LCG is substantially stronger.**

- **JaOSacdwmw** (avg 3.50, Reject): Cross-lingual collapse — identifies known phenomenon, limited to small models (≤3B) and 3 languages. **LCG is substantially stronger.**

- **aEuqVZVCdr** (avg 5.00, Accept Poster): Gumbel distillation for parallel decoding — different area, comparable contribution level. **LCG has similar strength with broader multilingual evaluation.**

LCG has a novel mechanistic insight, a practical well-validated method, comprehensive evaluation, and honest discussion of limitations. Its weaknesses (heuristic metric, unvalidated pseudo-targets, bundled rule ablation) are real but minor and do not threaten the core claims. Compared to the anchor papers, LCG sits above the 5.0-5.5 accept-poster range and merits a score of 6.0.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>