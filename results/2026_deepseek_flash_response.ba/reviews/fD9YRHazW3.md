Now let me write the final consolidated review.

## Summary

The paper introduces In-Context Watermarking (ICW), a paradigm for LLM watermarking that operates entirely through prompt engineering — requiring no access to model weights, logits, or the decoding process. Four strategies are proposed (Unicode, Initials, Lexical, Acrostics) across two settings: Direct Text Stamp (DTS) and Indirect Prompt Injection (IPI). Experiments on GPT-4o-mini and GPT-o3-mini show that with capable models, ICW achieves ROC-AUC ≥ 0.995 in DTS and ≥ 0.997 in IPI, while maintaining robustness against paraphrasing attacks and preserving text quality better than post-hoc baselines.

## Strengths

- **Eliminates decoding-process dependency**: ICW achieves strong detection (AUC ≥ 0.995 with GPT-o3-mini across all four strategies in DTS, Table 2) while requiring no access to model weights, logits, or sampling — a fundamentally different operational paradigm from all prior in-process methods that require logit perturbation or pseudo-random sampling control. This is validated with concrete numbers.

- **Enables watermarking in the IPI setting where no prior method can operate**: Post-hoc methods (PostMark, YCZ+23) are explicitly inapplicable in the IPI setting because a dishonest reviewer has no incentive to watermark their own text (Section 5.1). ICW achieves ROC-AUC of 0.997–1.000 in IPI with GPT-o3-mini (Table 2), demonstrating that a third party (e.g., conference organizer) can covertly embed and detect watermarks without the user's cooperation.

- **Superior paraphrasing robustness**: Under LLM paraphrasing, Initials (0.887), Lexical (0.924), and Acrostics (0.922) ICW all surpass PostMark (0.841) and vastly exceed YCZ+23 (0.557) (Figure 3). This is the strongest evidence in the paper that prompt-level watermarking survives semantic reformulation that destroys some baselines.

- **Text quality preservation**: Lexical ICW (Overall=4.808) and Acrostics ICW (4.813) on the LLM-as-a-Judge evaluation (Table 3) are close to unwatermarked text (4.992) and far surpass PostMark (2.997) and YCZ+23 (3.865). This is quantitative evidence that prompt-based watermarking degrades output quality much less than post-processing approaches.

- **Systematic exploration of trade-offs**: The paper provides a clear analysis of four strategies across LLM requirements, detectability, robustness, and text quality (Table 1), giving practitioners a principled basis for choosing among methods, and the discussion honestly acknowledges limitations of each approach.

## Weaknesses

### Major

- **IPI ecological validity is untested in realistic conditions**: The paper's headline application (detecting AI-written peer reviews) depends on hidden watermarking instructions surviving realistic PDF-to-text pipelines. The paper mentions using "white text" or "zero-font-size text" (lines 89, 95) as obfuscation but provides no experiment testing whether instructions embedded this way survive standard PDF viewer copy-paste operations or LLM API processing. If the instruction doesn't survive the pipeline, the IPI case study collapses. The paper acknowledges this is left for future work (lines 99–102), but given that this is the paper's central motivating scenario, the gap is significant.

- **ICW currently only works with the most capable (and expensive) models**: With GPT-4o-mini, three of four ICW methods perform at or near chance in DTS: Initials (AUC 0.572), Acrostics (AUC 0.590), and to a lesser degree Lexical (AUC 0.910). Only the trivial Unicode ICW works across both models. This means the method is currently viable only with models at the GPT-o3-mini level — expensive, not universally available, and not under the control of the entity trying to detect watermarks. In the paper's own motivating scenario, the reviewer could use weaker open-weight models that will not follow the watermarking instructions. The paper acknowledges this, but frames it optimistically as "ICW will improve as models advance" rather than treating it as a central constraint on current applicability.

- **GPTZero listed as baseline but absent from results**: Section 5.1 lists GPTZero (Tian & Cui, 2023) as a baseline alongside PostMark and YCZ+23, but Table 2 does not include GPTZero results with any explanation for its absence. If it was evaluated, results should be shown; if not, it should be removed from the baseline list.

### Minor

- **No confidence intervals or statistical significance testing**: The paper reports ROC-AUC and T@FPR values but does not report confidence intervals. With 500 samples per condition, confidence intervals would allow readers to assess whether differences between methods (e.g., Initials AUC 0.999 vs. Lexical AUC 0.995) are meaningful.

- **Detection threshold selection not discussed**: The paper reports ROC-AUC (threshold-independent) alongside T@1%F and T@10%F, but does not discuss how a detector would choose an operating point in practice, or what the implications of false positives would be in the peer review scenario (falsely accusing a reviewer of AI use has serious consequences).

- **Lexical ICW green word list not fully characterized**: The paper reports the vocabulary is "restricted to adjectives, adverbs, and verbs" (line 152) but does not report the size of the green list, how it was sampled from the vocabulary, or whether the full list was provided in-context or via truncation. These details matter for reproducibility.

- **LLM-as-a-Judge confound**: The evaluation uses Gemini 2.0 Flash to judge GPT-generated text. The near-perfect scores for unwatermarked GPT-o3-mini text (Relevance 4.982, Quality 5.000, Clarity 4.994, Table 3) suggest potential judge bias toward GPT outputs, which could inflate relative quality scores for ICW methods. The perplexity numbers (in appendix) would be a more trustworthy comparison.

### Trivial

None.

## Nice-to-Haves

- Test the IPI setting more realistically: embed hidden instructions as white text in real PDFs and verify they survive standard copy-paste pipelines into LLM APIs.
- Evaluate on a range of open-weight models (LLaMA-3 variants, Qwen, Mistral) to empirically map the capability threshold where ICW becomes effective. This would tell readers which models are "ICW-capable."
- Provide a discussion of operating point selection for the peer review scenario, including false-positive cost analysis.

## Removed Points

- **"Baseline comparison conflates fundamentally different use cases"** (Harsh Critic): REMOVED. The paper explicitly acknowledges the asymmetry: "Unlike PostMark and YCZ+23, which rely on post-processing and cannot be used in the IPI setting, ICW methods are well-suited for IPI" (lines 222–223). The comparison in DTS is fair since both are applicable there.

- **"Unicode ICW inflates the contribution"** (Harsh Critic): REMOVED. Including a simple baseline strategy is standard practice. Table 1 clearly shows Unicode ICW has lower robustness, and the discussion acknowledges its fragility. It serves as a contrast, not a claimed core contribution.

- **"Security evaluation does not test informed adversaries"** (Harsh Critic): PARTIALLY REMOVED. The critic claimed the paper does not evaluate an adversary who "prepends 'ignore previous formatting instructions'" — but the paper explicitly does evaluate this in Appendix D.1: "the other evaluates detection performance when an adversary prepends the instruction 'ignore prior prompts'" (line 286). This specific criticism is factually incorrect and removed. The broader point about limited adversarial evaluation is partially valid but scoped out by the paper as future work.

- **"Instruction appears twice in IPI setting (ambiguity)"** (Harsh Critic): REMOVED. Equation 2 (line 93) shows `y ← M(𝜏̃ ⊕ Instruction(k, τ) ⊕ Q)` — the instruction is embedded in the stamped text AND explicitly provided. This is by design: the stamped text contains the hidden instruction, and the explicit concatenation ensures the LLM sees it regardless of whether the hidden text survives formatting.

- **"Statistical testing missing"** (Harsh Critic): Demoted to Minor (from an implied stronger criticism). While confidence intervals would strengthen the paper, the AUC differences are large enough (e.g., 0.995 vs 0.572) that statistical significance is unlikely to change conclusions.

- **Generic strengths from Strength Finder** (e.g., "timely topic", "addresses important problem"): REMOVED as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The key insight — that watermarking can be achieved purely through prompt engineering without any model-internal access, and that this approach can survive paraphrasing better than some post-hoc baselines — is the paper's own contribution.

## Suggestions

- Run a single sanity-check experiment: embed a hidden instruction as white/zero-font text in a PDF, copy-paste it through a standard pipeline, and verify the LLM follows it. This would either validate the IPI case study or reveal its brittleness.
- Include confidence intervals for all reported metrics.
- Add GPTZero results to Table 2 or remove it from the baseline list.
- Disclose the green word list size, sampling procedure, and prompt format for Lexical ICW.
- Test ICW on open-weight models (LLaMA-3, Qwen, Mistral) to characterize required capability thresholds.

## Calibration Anchors

**Round 1 (bracketing, scores <3.5, 3.5–7.5, >7.5):** 
- Weak anchors (avg ≤3.3): "Sparse Watermarking in LLMs" (3.00, Reject), prompt engineering papers (~3.00) — ICW paper is clearly stronger.
- Middle anchors (3.5–7.5): "A Semantic Invariant Robust Watermark for LLMs" (5.50, Accept), "Can Watermarks be Used to Detect LLM IP Infringement For Free?" (5.80, Accept), "WASA" (5.50, Reject), "Learning to Watermark via RL" (4.75, Reject).
- Strong anchors (≥7.5): "Black-Box Detection of Language Model Watermarks" (7.00, Accept) — ICW paper is not at this level of rigor or breadth.

**Round 2 (narrowing, 4.5–6.5 and 5.0–7.5):**
- "A Semantic Invariant Robust Watermark" (5.50, Accept, scores: 8,5,6,3): Novel core idea with practical limitations (needs logit access during detection). ICW has similar structural novelty and limitation severity — comparable. 
- "Can Watermarks be Used to Detect LLM IP Infringement For Free?" (5.80, Accept, scores: 6,6,5,6,6): Cleaner evaluation but narrower scope. ICW has broader scope but weaker evaluation on some dimensions.
- "A Watermark for Low-entropy and Unbiased Generation" (5.50, Reject, scores: 6,5,5,6): Weak results vs baselines led to rejection. ICW shows clearer improvements over baselines.
- "Black-Box Detection of Language Model Watermarks" (7.00, Accept, scores: 8,6,6,8): More rigorous statistically and broader model coverage. ICW does not reach this bar.

**Bracket:** Round 1 → 4–6.5. Round 2 → 5.0–6.0. Final score: **5.5** — comparable to the Semantic Invariant watermark paper (5.50, accepted) in terms of novelty/limitation trade-off, though the evaluation is less thorough than the strongest mid-band anchors.

## Score and Decision

**Score:** 5.5  
**Decision:** Accept

The paper introduces a genuinely novel approach to LLM watermarking (prompt-only, no model internals required) and systematically explores four strategies across two settings, with the strongest evidence being the paraphrasing robustness of Initials, Lexical, and Acrostics ICW with GPT-o3-mini. However, the practical limitations — IPI ecological validity untested, dependence on top-tier models, missing GPTZero results, and no confidence intervals — prevent this from being a stronger paper. The core idea is compelling enough for acceptance at a top venue, with expectation that the IPI validation and broader model evaluation will be addressed in the final version.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>