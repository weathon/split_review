Now I have a complete picture of the paper and can verify specific claims against the text. Let me produce the final consolidated review.

## Summary

This paper proposes Mixture-of-Instructions (MoI), a method for multi-task supervised fine-tuning of LLMs that combines three components: (1) domain-specific system prompts, (2) balanced sampling to pack instructions from different domains, and (3) chunk-based attention masking to prevent cross-contamination between packed examples. The method is applied to Qwen-7B-chat and evaluated across seven benchmarks covering code, math, tool use, and dialogue. The strongest evidence in the paper is that MoI's combination of system prompts + balanced sampling clearly outperforms naive packing and sequential training strategies. However, the paper's most novel component—the chunk-based attention mask—shows only a small average improvement over the already-strong balanced sampling baseline, with no statistical significance or variance reporting.

## Strengths

- **Systematic ablation isolates each design choice.** Table 2 compares Sequence, Packing, Balanced, and MoI strategies across all seven benchmarks, and Table 3 varies system prompts for code tasks. This controlled design lets readers attribute improvements to specific MoI components. The ablation shows that balanced sampling + system prompts accounts for most of the gain.

- **Demonstrates generalizability across model families and sizes.** Table 6 shows MoI improves Llama2-7B (+1.7 avg) and Llama3-8B (+2.0 avg) beyond their SFT baselines, and Table 7 shows gains on Qwen1.5-1.8B and Qwen1.5-4B, indicating the method scales down without losing effectiveness.

- **Concrete case study and attention visualization motivate the system prompt component.** Figure 2 and the Boyer-Moore example (Section 2.1) provide an intuitive, testable demonstration that changing the system prompt from a generic one to "You are a programmer" shifts the model's attention and improves code generation, as further validated in Table 3.

- **Principled loss formulation for chunk-based packing.** Equations (6)–(10) formally specify the MoI training objective with chunk-based attention masking, treating each instruction group independently to avoid attention cross-contamination—a clean technical specification that distinguishes the approach from ad-hoc packing.

## Weaknesses

### Fatal
None.

### Major

- **The key novel component (chunk-based attention masking) is not convincingly shown to provide a meaningful improvement over balanced sampling alone.** Per Table 2, the MoI strategy (balanced sampling + chunk mask) yields an average gain of roughly 0.7 points over the Balanced variant (which uses the same data, same system prompts, but no chunk mask). The individual deltas are small (e.g., ~+0.6 HumanEval, ~+0.5 GSM8K, ~+1.1 MATH, ~+0.05 MT-Bench). The paper reports zero variance or statistical significance measures—no multiple runs, no confidence intervals. Given that these benchmarks exhibit non-trivial variance under greedy decoding, the observed differences may fall within noise. This is the paper's central methodological novelty, and the evidence for it is not commensurate with the claim that MoI "achieves substantial improvements across all tasks" (line 279). The authors should either (a) demonstrate statistical significance via repeated runs, or (b) reframe the contribution to center on the well-supported system-prompt + balanced-sampling combination, presenting the chunk mask as a secondary, exploratory finding.

- **The weight replacement analysis (Table 9) lacks proper experimental controls, making its interpretation speculative.** The paper replaces the chat model's attention weights with MoI's and observes a performance drop, concluding that "MoI's attention mechanisms are unable to extract the most relevant knowledge from the original chat MLP." A proper control would require the complementary swap (MoI MLP with chat attention) to isolate whether the effect comes from the attention distribution specifically. Without this, the experiment does not convincingly support the claim that MoI's attention distribution is "fundamentally different." This experiment should either be redesigned or de-emphasized.

### Minor

- **The paper's framing overstates the contribution by emphasizing comparisons to the base Qwen-7B-chat model.** The abstract and conclusion highlight how Qwen-SFT-MoI improves over Qwen-7B-chat (which is expected, since MoI adds substantial additional training data). The more relevant and controlled comparison (MoI vs. Balance, which uses the same data) shows a much smaller advantage. The paper should clearly separate "the method works" from "more data helps."

- **Table 1 does not report per-domain training example counts or mixture ratios.** Given that balanced sampling is a critical component, the exact ratios used and how they vary across domains should be stated in the main text, not deferred to the appendix.

- **Figure 5 (training curves) compares Balanced vs. Concat but omits the full MoI (with chunk mask) curves.** Since the contribution of the chunk mask is the paper's most debated component, showing its training dynamics across the same benchmarks would directly address whether the mask adds value during training.

- **The attention map analysis in Figure 2 is based on a single question.** While illustrative, this limits the generality of the mechanistic claim that system prompts "resolve knowledge conflicts" by shifting attention. A more systematic analysis (e.g., attention entropy across the validation set) would strengthen the motivation.

### Trivial

- Section 2.3 claims the chunk mask "enhances" reasoning ability; however, Table 8 shows it improves T-Eval but slightly reduces GSM8K and MATH relative to the no-mask baseline. The claim would be more precise as "balances task performance" rather than "enhances."

## Nice-to-Haves

- Including MoI curves in Figure 5 alongside Balanced and Concat to directly visualize the attention mask's effect during training.
- Reporting training efficiency metrics (throughput, GPU memory) to help practitioners assess the practical cost of chunk-based masking.
- A brief comparison to loss-weighting approaches for multi-task learning (e.g., uncertainty weighting) to situate the method relative to complementary paradigms.

## Removed Points

These points from the inputs were removed for the following reasons:

- **Criticism that Section 2.2 (balanced sampling) is underspecified due to missing text.** The reviewer acknowledges this is caused by parser truncation. The hard rule on missing appendix/content stripped by the parser applies analogously — this content exists in the original submission. *Removed.*
- **Criticism about missing comparison to GradNorm, uncertainty weighting, or domain-specific adapters.** These are alternative research paradigms (loss weighting vs. data mixing), and the paper already compares against three relevant data-mixing baselines (sequence, packing, balanced). Demanding coverage of a different family of methods is scope creep. *Removed.*
- **Criticism that the "leap" from the Boyer-Moore anecdote to MoI is not clearly motivated.** This is a subjective preference about exposition; the paper explicitly states (Section 2) that the system prompt observation motivated the use of diverse prompts, and balanced sampling addresses a separately identified problem (dataset bias). The logical connection is present, if not elegantly woven. Downgraded to minor clarity preference above. *Removed as standalone weakness.*
- **"No analysis of training efficiency."** Moved to Nice-to-Haves — useful but not a weakness.
- **Pure formatting/style nitpicks and speculation about missing appendix content.** *Removed per hard rules.*

## Novel Insights

The two reviews, when read against each other, surface an interesting tension: the Strengths Finder highlights the thoroughness of the ablation and the breadth of generalization experiments (Llama2, Llama3, small Qwen models), while the Harsh Critic's deepest concern is not about the evaluation's breadth but about its *precision* — specifically, the lack of repeated-run statistics makes it impossible to know whether the chunk mask's effect is real. This tension reveals that the paper's empirical strategy is wide but shallow: it covers many models and benchmarks (a strength), but for its central novelty it provides no within-cell variance estimate (a weakness). The paper would be meaningfully stronger if it invested some of its breadth budget into precision on the key comparison (MoI vs. Balance with 3–5 seeds).

## Suggestions

1. **Run the core comparison (MoI vs. Balance) with 3–5 random seeds and report means + standard deviations.** If the 0.7-point advantage is robust, this transforms the paper's central claim from plausible to demonstrated. If not, reframe the contribution around the system-prompt + balanced-sampling combination (which is well-supported) and present the chunk mask as an exploratory finding.

2. **Redesign the weight replacement experiment (Table 9) with proper controls**, specifically swapping MoI's attention weights into a model with MoI's MLP and vice versa. If the experiment cannot be made interpretable, move it to the appendix.

3. **Add per-domain training example counts and mixture ratios to Table 1** in the main paper. This is essential for reproducibility of the balanced sampling procedure.

4. **Qualify the framing throughout**: separate "MoI outperforms the original Qwen-7B-chat (due to more data + better mixing)" from "MoI outperforms balanced sampling with the same data (due to the chunk mask)." These are different claims with different evidence strengths.

## Score and Decision

**Originality:** The individual components (system prompts, balanced sampling, attention masking) are known, but their combination in a unified SFT pipeline for multi-task alignment is moderately novel. The chunk-mask design (intra-chunk visibility, inter-chunk isolation) has some specificity.

**Importance of research question:** High. Multi-task alignment during SFT is practically important, and the paper addresses a real problem (dataset bias, attention cross-contamination).

**Claims well-supported:** Partially. The overall MoI framework's advantage over naive packing is well-supported. However, the paper's central novel component (chunk mask) has marginal, non-significance-tested evidence. The weight replacement analysis is undercontrolled.

**Soundness of experiments:** The ablation structure is sound and the benchmark coverage is broad. The primary weakness is the absence of statistical rigor on the key comparison.

**Clarity of writing:** Generally clear, though Section 2.2's content is absent in the parsed version (likely a parser issue), and some descriptions (chunk construction, weight replacement) could be more precise.

**Value to community:** Moderate. The method is practical and reproducible (open-source models, open data), and the ablation provides useful empirical guidance for practitioners doing multi-task SFT.

**Overall assessment:** The paper makes a reasonable contribution with solid empirical breadth, but the evidence for its most novel component is thin. The overall framework (system prompts + balanced sampling) is demonstrably useful, which is valuable, but the paper's presentation overclaims by centering the chunk mask as the key innovation when the data only weakly support its incremental benefit.

**Score:** The paper is between "marginally above acceptance threshold" and "clear accept" — the method works, the experiments are broad, but the core novelty claim is underpowered. I assign a score of **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>