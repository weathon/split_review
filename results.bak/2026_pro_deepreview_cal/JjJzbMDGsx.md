Now I have sufficient calibration data. Let me synthesize everything and write the final review.

---

## Summary

The paper introduces the Language Confusion Gate (LCG), a lightweight plug-in decoding filter that suppresses unintended language mixing in multilingual LLMs without altering base model parameters. LCG is a small two-layer MLP trained via norm-adjusted self-distillation: it uses the frozen model's own debiased (norm-adjusted) predictions as pseudo-labels, then at inference predicts which language families are permissible and masks disallowed tokens. The method is grounded in a novel mechanistic analysis showing that output token embedding norms are systematically larger for high-resource languages (Table 1), creating a sampling bias that contributes to confusion. Across Qwen3, Llama3.1, Gemma3, and GPT-OSS models, LCG reduces language confusion by an order of magnitude while preserving task performance, with only ~0.4% latency overhead.

## Strengths

- **Strong empirical results across diverse models and tasks.** Table 3 shows LCG reduces confusion by an order of magnitude across four no-think models on FLORES-NO-LATIN and INCLUDE (e.g., Qwen3-30B CJ%: 1.0→0.0, Latin%: 4.4→0.4; Qwen3-8B Latin%: 12.1→2.0), while BLEU and accuracy remain stable or slightly improve. Table 4 shows similar benefits for thinking models on Humaneval-XL without degrading Pass@k. These results are consistent and convincing.

- **Novel mechanistic insight into token embedding norm imbalance.** The decomposition logit_i = ‖h‖·‖e_i‖·cos_sim (Section 3.2) and the data in Table 1 (e.g., Qwen3-8B: 10.74% of CJ tokens vs. 0.14% of Low-Res tokens in the top-5% norm) provide a clear, measurable explanation for why high-resource languages dominate sampling. Figure 2 demonstrates concretely how norm adjustment reorders logits at a confusion point, showing the debiased signal can identify the correct language family.

- **Norm-adjusted self-distillation is critical and well-ablated.** Table 3 shows LCG-adjusted consistently outperforms LCG-unadjusted (e.g., Llama3.1-8B Latin%: 5.7%→2.9%), confirming that the norm-adjustment mechanism translates into practical gains, not just a theoretical observation.

- **Thoughtful evaluation design.** The FLORES-NO-LATIN/WITH-LATIN partitioning (Section 5.2) is a sensible way to handle the Latin confusion measurement challenge. The rationale for not using LCB (natural code-switching in queries, detector false positives) is well-argued.

## Weaknesses

### Fatal

None.

### Major

- **Evidence for preserving legitimate code-switching is insufficient for the strength of the claim.** The paper motivates LCG in part by its ability to distinguish confusion from natural code-switching, but the evaluation supporting this claim has two gaps. First, the token-level experiment (86.7% of English tokens allowed at "human-validated" code-switch points) does not report the sample size, selection criteria, or annotator agreement, and—critically—does not measure false rejections (how often LCG blocks natural code-switches in the full FLORES-WITH-LATIN set). Second, the response-level code-switch rate experiment (Table 5) shows post-intervention rates (e.g., Qwen3-8B: 25.9%) dropping below the ground-truth reference rate (38.4%), which could indicate over-suppression of legitimate mixing. The paper argues the rate remains above the Claude Sonnet 4 baseline (23.3%), but this is a weak defense since that baseline may itself suppress code-switching. A precision/recall-style evaluation on code-switching would substantially strengthen this claim.

### Minor

- **The "open-source datasets" contribution is overstated (Section 1).** The paper claims to "collect and open-source specialized training and evaluation datasets." The training data is aggregated from existing public corpora (Aya, FLORES+, DeepSeek Distill, Alpaca), and evaluation uses standard benchmarks. The FLORES-NO-LATIN/WITH-LATIN partitioning is a useful methodological contribution but does not constitute a new dataset in the sense the claim implies. The claim should be recalibrated.

- **ORPO baseline comparison lacks implementation detail (Section 5.3).** The paper reports ORPO results in Figure 3 but provides only a high-level description ("synthesize samples with language confusion as rejected samples similar as Lee et al. (2025)"). Data size, hyperparameters, and the mixture of rejected samples are not specified, making it difficult to assess whether the comparison is fair.

- **The connection between norm-adjustment and the trained gate's behavior could be more fully articulated (Section 3.2, 4.2).** The ablation confirms norm-adjusted training improves results, and Section 3.2 motivates why debiased pseudo-labels are better. However, the paper does not analyze whether the trained gate's predictions actually reflect the cosine-similarity signal or whether a simpler rule (e.g., always normalizing during inference) would suffice. A brief analysis of the gate's reliance on the norm-debiased signal versus other features would strengthen the mechanistic story.

- **Intervention rule hyperparameters are not analyzed (Section 4.3).** Rule (2) uses two candidate-set definitions ((k=5, p=0.999) and (k=20, p=0.95)) as a safeguard against incorrect gate predictions. The sensitivity of results to these specific thresholds is not examined.

- **Thinking model evaluation does not report Latin confusion (Table 4).** For code-generation tasks this is understandable (Latin characters are expected), but the decision should be explicitly justified in the text rather than left implicit.

- **The interaction between LCG and sampling parameters is not discussed.** The paper notes intervention only occurs when disallowed tokens are within the sampling set, but the effects of temperature, top-k, and top-p on intervention rate are not analyzed.

### Trivial

- Training data language coverage and dataset composition would benefit from a concise table rather than the current prose description.

- The 0.4% latency claim (Section 6) references a "production system" without specifying hardware, batch size, or measurement methodology.

## Nice-to-Haves

- A dedicated code-switching benchmark evaluation (e.g., LinCE) with precision/recall metrics for confusion suppression vs. code-switch preservation would directly address the central tension of the method.
- Analysis of LCG behavior on a language unseen during gate training would build confidence in generality.
- A few concrete error examples where the gate fails (wrong prediction, override rules insufficient) would help readers understand remaining limitations.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic's concern about "appendix F referenced but not verified" / "compatibility with speculative decoding cannot be verified from main text."** REMOVED per hard rule: the parser strips appendices; the original submission includes them. The main text does reference Appendix F, and the efficiency claim in the main text (0.4% latency) stands on its own.
- **Harsh critic's claim that evaluation metrics are "coarse."** The CJ% and Latin% metrics are standard and appropriate for the problem. The issue is not coarseness of metrics but the evaluation design for code-switching, which is already captured in the Major weakness.
- **Strength Finder's claim that the code-switching evaluation is "careful" without qualification.** The FLORES-NO-LATIN/WITH-LATIN split is indeed careful, but the actual code-switching preservation experiments have limitations. I've kept the strength for the split design while flagging the preservation evidence as a Major weakness.

## Novel Insights

Beyond the paper's own contributions, a notable tension emerges: the norm imbalance analysis (Section 3.2) is the paper's most original finding, yet the paper acknowledges it "cannot fully explain language confusion" and "can't be directly used for intervention." The solution—using it indirectly via norm-adjusted self-distillation to train a gate—is clever but creates an indirection that the paper does not fully close. Understanding exactly how the trained gate leverages (or does not leverage) the debiased signal—versus learning other features of the hidden state—would transform this from an insightful-but-partial mechanistic story into a complete causal account.

## Suggestions

- Report the sample size, selection criteria, and inter-annotator agreement for the human-validated code-switch experiment. Extend it to measure false rejection rate on the full FLORES-WITH-LATIN set.
- Either tone down the "open-source datasets" claim in the introduction or clarify that the contribution is the FLORES-NO-LATIN/WITH-LATIN partitioning and the aggregated training corpus, not de novo datasets.
- Add a brief analysis (even a paragraph) on whether the trained gate's predictions correlate with the norm-adjusted logit ranking versus the raw logit ranking, to connect the mechanistic motivation more tightly to the learned behavior.
- Justify the thinking-model evaluation's focus on CJ% only and absence of Latin% reporting.

This paper addresses a real, practical problem in multilingual LLM deployment with a well-motivated, lightweight solution grounded in a genuine mechanistic insight. The empirical results are strong and consistent across models and tasks. The primary weakness—thin evidence for code-switching preservation—is significant because it touches the method's core motivation, but it is addressable with additional evaluation and does not invalidate the demonstrated confusion reduction. The paper is original, well-executed, and practically valuable.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>