Now I have sufficient calibration. Let me construct the final review.

**Calibration Summary:**

Round 1 bracket: (4, 7) — narrowed after reading X-ALMA (7.33), XTransplant (4.75), TransLLM (6.25), Babel Tower (5.25)

Round 2 anchors read in full: Tool Decoding (6.00), UniDetox (6.25), The Same but Different (6.60)

LCG is stronger than Tool Decoding (6.00) — both are plug-and-play decoding interventions but LCG's norm-adjusted self-distillation is a genuinely novel contribution backed by mechanistic evidence, whereas Tool Decoding's constrained decoding is more straightforward. LCG is comparable to UniDetox (6.25) and The Same but Different (6.60). LCG is clearly above XTransplant (4.75), TransLLM (6.25), and Babel Tower (5.25) in terms of novelty and practical impact, but below X-ALMA (7.33) in experimental rigor and completeness. I anchor LCG at **6.5**.

---

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight two-layer MLP that filters tokens during decoding to reduce language confusion in multilingual LLMs. LCG takes the model's hidden state, predicts which of four language families (CJ, Latin, Symbols, Low-Res) are permissible at each step, and masks disallowed logits. It is trained via norm-adjusted self-distillation, where pseudo-targets are derived from the model's own norm-debiased top-k/p predictions. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS on translation (FLORES) and code generation (Humaneval-XL), LCG reduces confusion by an order of magnitude (e.g., Qwen3-30B CJ confusion 1.0%→0.0%, Latin 4.4%→0.4%) with 0.4% latency overhead while preserving legitimate code-switching.

## Strengths

1. **Novel and well-motivated approach grounded in mechanistic evidence**: The paper's core insight — that output token embedding norms are imbalanced across language families and that adjusting logits by these norms produces cleaner distillation targets — is original and supported by quantitative analysis (Table 1, Figure 2). Norm-adjusted self-distillation outperforms the unadjusted variant consistently (Table 3, e.g., Llama3.1-8B Latin confusion drops from 5.7% to 2.9%), confirming the geometric insight translates into a genuine algorithmic improvement.

2. **Empirically motivated intervention logic**: Section 3.1's finding that at confusion points, correct-language tokens appear within top-3 in 99.29% of cases while confusion tokens are top-1 56.74% of the time directly motivates masking over retraining. This is concrete, quantitative evidence that the model "knows" the right answer but samples wrong — a finding with implications beyond this paper.

3. **Comprehensive multi-model evaluation with consistent gains**: LCG is evaluated on five models spanning different architectures, scales (8B–30B), and modes (no-think and thinking). The pattern of confusion reduction holds across all (Tables 3, 4), including on Gemma3-12B and GPT-OSS where training was on different model families than the base Qwen3-8B used for gate training. The INCLUDE accuracy metric shows no degradation, unlike ORPO which drops accuracy (Figure 3).

4. **Practical overhead is quantified and negligible**: Section 6 reports a benchmark with 0.4% latency increase (15.95ms → 15.99ms per step) at 8-way concurrency. Combined with the 0.33–0.38% intervention rate (523/139,354 tokens for Qwen3-8B), this establishes that LCG is deployable in production settings.

5. **Code-switching preservation is demonstrated with two complementary analyses**: The token-level analysis (86.7% permission at human-validated code-switch points) and the response-level analysis (Table 5, post-intervention rates above Claude Sonnet 4 baseline) provide converging evidence that LCG does not suppress legitimate mixing. The comparison against a strong commercial model (Claude Sonnet 4) as an anchor is a useful reference.

## Weaknesses

### Major

1. **Potential training/evaluation data overlap is not addressed**: The training data for LCG includes the FLORES+ Dataset (Section 5.1, "aggregated from several sources, including…FLORES+ Dataset"), while the primary evaluation benchmark FLORES-NO-LATIN is explicitly a subset of FLORES+. The paper does not state whether evaluation sentences were excluded from training. Because the gate is trained on the frozen model's hidden states collected from training samples, overlap could inflate results — the gate might have learned to recognize the correct language family for specific inputs it saw during training. This concern is partially mitigated by (a) the gate's training objective (predicting language families from norm-adjusted logits, not memorizing translations), (b) the evaluation metric (character-level confusion rate, different from the BCE training loss), and (c) generalization across model families. However, the paper must clarify whether training and evaluation sets are disjoint, or provide results on a held-out subset. Without this clarification, a core claim — that LCG generalizes to unseen confusion points — rests on an unverified assumption.

2. **Gate training details are underspecified**: The paper does not report the hidden dimension, activation function, learning rate, batch size, number of training epochs, optimizer, or the procedure for collecting the 78,000 training samples (e.g., how confusion points were located for training). The binarization threshold for converting the gate's sigmoid outputs to binary language-family predictions at inference is also not specified. These omissions hurt reproducibility and make it difficult for other researchers to adopt or compare against the method. While the 2-layer MLP architecture is stated, a paper introducing a trained component should provide sufficient detail for independent reimplementation.

### Minor

3. **Limited task diversity**: Evaluation is restricted to translation (FLORES) and code generation (Humaneval-XL). For a method claiming to mitigate language confusion "generically," testing on additional tasks (e.g., multilingual summarization, instruction following, open-ended QA) would strengthen the findings. The paper acknowledges this implicitly by testing only tasks where confusion is measurable, but the scope of claims (e.g., "LCG decreases language confusion significantly" in the abstract) suggests broader applicability than what is tested.

4. **No confidence intervals or significance tests**: BLEU differences in Table 3 are often less than 1 point (e.g., 13.2→13.4 for Qwen3-30B). Without confidence intervals or significance tests, it is unclear whether these differences are meaningful given the noise in LLM generation. This is common for systems papers at this scale, but the paper should at minimum acknowledge the lack of statistical rigor.

5. **Human evaluation protocol for code-switching analysis is underspecified**: The paper states that human annotators judged code-switch cases as "natural, appropriate" but does not report the number of annotators, inter-annotator agreement, or selection criteria. While this analysis is secondary (measuring gate behavior on pre-selected examples, not the annotators' judgment as a metric), the lack of detail prevents assessment of the 86.7% figure's reliability.

6. **No held-out gate accuracy metric**: The paper reports intervention frequency (0.38%) but never directly evaluates the gate's own classification accuracy, precision, or recall on a held-out set of confusion points. How often does the gate correctly predict the allowed language family? How often does it incorrectly mask a permissible token? Without this, the gate is a black box whose behavior is only indirectly observed through downstream confusion rates.

### Trivial

7. Naming inconsistency: The introduction refers to "Qwen3-235B-A22B-Instruct-2507" but Table 2 lists "Qwen3-235B-Instruct."

8. The heuristic thresholds for intervention rules (top-k=5/p=0.999 and top-k=20/p=0.95 in Section 4.3) are stated without justification or sensitivity analysis. A brief note on how these were chosen would improve clarity.

## Nice-to-Haves

- A "rules-only" ablation (intervention rules without the gate) would clarify how much of the confusion reduction comes from the learned gate versus the safety rules. The "No Rule" ablation in Figure 3 shows the gate without rules; the reverse (rules without gate) would complete the picture.
- Extending the confusion point analysis (Section 3.1) beyond Qwen3-8B to at least one other model would strengthen the claim that the 99.29% top-3 finding generalizes.
- A sensitivity analysis of the binarization threshold (if one is used) showing the trade-off between confusion reduction and code-switch preservation would be informative.

## Removed Points

- **Criticism about FLORES-NO-LATIN being a filtered subset of FLORES+ making Latin confusion evaluation unreliable**: This is factually wrong. The paper explicitly designed FLORES-NO-LATIN to filter out translations where Latin characters are legitimate, which is a careful and correct methodological decision. The subset is used precisely to avoid false positives, not to cause them.
- **Criticism that the paper claims "generalization to unseen confusion points" without evidence**: The paper's confusion point analysis (Section 3.1) is on Qwen3-8B, but LCG is evaluated on other models (Llama3.1, Gemma3, GPT-OSS) that were not used for confusion point analysis, which does demonstrate cross-model generalization.
- **Critique of token-level 86.7% figure as "unverifiable"**: The paper describes the procedure (human annotators selected natural code-switch cases, then gate was applied). While more detail on annotator count and agreement would be welcome, the figure is clearly described as a behavioral test of the gate, not a human evaluation of output quality.
- **"Missing related work"** type criticism.
- **Formatting/style nitpicks** (parser artifacts).

## Novel Insights

The reviews surface one point that the paper does not fully explore: the norm-adjusted self-distillation approach could be viewed more broadly as a method for distilling a classifier from the geometric properties of a frozen LM's output embeddings. The fact that the 2-layer MLP gate trained on one model (Qwen3-8B) generalizes to other model families (Llama3.1, Gemma3) suggests that the mapping from hidden states to permissible language families is partly model-agnostic — a finding that, if pursued, could lead to a universal language-confusion gate trained once and applied to any LLM. The paper's current framing focuses on the specific application, but the method's cross-model transferability is arguably its most surprising and potentially impactful property.

## Suggestions

1. **Clarify the train/eval split**: Add a sentence specifying whether any FLORES+ sentences used for evaluation were excluded from the 78k training samples. If they were not excluded, re-evaluate on a truly held-out subset (e.g., languages or sentences not in the training data) and report whether confusion reductions hold.

2. **Add training details**: Specify the gate's hidden dimension, activation, optimizer, learning rate, batch size, epochs, and the binarization threshold (or decision rule) for gate predictions at inference. Even a brief paragraph would substantially improve reproducibility.

3. **Report gate accuracy metrics**: Add precision, recall, and F1 for the gate's language-family predictions on a held-out set of confusion points. This would help readers calibrate trust in the gate's outputs independently of downstream confusion rates.

4. **Add confidence intervals**: For the main confusion-rate comparisons (Table 3), report bootstrap confidence intervals or note the number of independent generations used to estimate variance.

## Score and Decision

I assign a score of **6.5**. The paper makes a genuinely novel contribution — norm-adjusted self-distillation for language-aware decoding is a clever and principled idea backed by mechanistic evidence and solid empirical results across diverse models. The method is practical (0.4% overhead, sparse intervention) and addresses a real problem. The weaknesses are real but not fatal: the data-overlap concern needs clarification (not correction — the mitigated factors suggest results would hold), and the missing training details hurt reproducibility but can be addressed in a revision. Relative to calibration anchors, this paper sits above Tool Decoding (6.00) and TransLLM (6.25) due to its stronger originality, and below top-tier papers like X-ALMA (7.33) due to evaluation gaps. **Decision: Accept**, contingent on the authors clarifying the train/eval data split.

<score>6.5</score>
<decision>Accept</decision>