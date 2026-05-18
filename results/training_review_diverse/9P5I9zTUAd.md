## Summary

This paper proposes Mixture-of-Instructions (MoI), a multi-task SFT alignment method combining three components: (1) domain-specific system prompts tailored to each task, (2) balanced sampling to mitigate dataset bias when packing instructions from different domains, and (3) chunk-based attention masking to control attention cross-contamination across packed examples. The method is applied to Qwen-7B-chat and evaluated on seven benchmarks spanning math, code, tool use, and dialogue. The central empirical claim—that MoI produces consistent improvements across all evaluated tasks relative to baseline packing and naive SFT—is supported by the presented experiments.

## Strengths

- **Comprehensive multi-task improvement on a 7B model**: Table 2 reports that Qwen-SFT-MoI outperforms the base Qwen-7B-chat and several SFT baselines across all seven evaluation benchmarks (GSM8K, MATH, HumanEval, MBPP, MMLU, MT-Bench, T-EVAL), achieving the highest average score. This directly validates the paper's core claim.

- **Balanced sampling demonstrably reduces dataset bias**: The ablation in Figure 5 shows that balanced sampling yields faster gains on GSM8K and stabilizes code generation performance (HumanEval, MBPP) during training, while naive packing shows late-stage degradation. This is direct evidence that the method mitigates the dataset-bias problem identified in multi-task alignment.

- **Chunk-based attention masking strikes a measurable trade-off**: Table 8 shows that chunk-based attention simultaneously improves complex reasoning (T-EVAL) over a no-mask baseline while retaining the math/code performance gains that a fully isolated attention mask would lose. This demonstrates the design choice is empirically grounded rather than arbitrary.

- **Generalizability across model families and scales**: MoI improves performance on Qwen-1.5 models (1.8B, 4B), Llama2-7B, and Llama3-8B (Tables 6, 7), showing the method is not architecture- or scale-dependent.

## Weaknesses

### Fatal

None.

### Major

- **The loss function specification is notationally inconsistent and hard to follow.** The mathematical derivation in Section 2.4 has several problems that hinder reproducibility:
  - In $\mathcal{L}_{\text{packed}}$ (line 83), the denominator includes $|y_i|$ where $y_i$ indexes a single token. Since $|y|$ was defined as the number of tokens in the response (line 80), $|y_i|$ for a single token $i$ would always be 1, making this term either meaningless or a notational error.
  - The transition from $\mathcal{L}_{\text{masking\_out}}$ to $\mathcal{L}_{\text{MoI}}$ (lines 89–101) is not explained. The paper states "By combining $\mathcal{L}_{\text{packed}}$ and $\mathcal{L}_{\text{masking\_out}}$" but the MoI loss (line 101) introduces an entirely new indexing structure with $n_{\text{mix}}$ and windowed indices that does not obviously follow from the preceding equations.
  - The overall presentation obscures rather than clarifies the core idea. The method itself (chunk-based masking with per-chunk attention) is conceptually clear from Figure 4 and the prose, but the loss functions as written would not allow a reader to re-implement MoI from the equations alone. This is fixable with a clean, self-contained definition, but in its current form it is a genuine barrier to reproducibility.

### Minor

- **The motivating evidence for the system prompt insight is thin.** The paper's narrative begins with one example (Boyer-Moore question, Question ID 127, Figure 2) and attention maps for that single instance. While Table 3 shows aggregate code benchmark scores across system prompts (supporting the general claim), the paper generalizes from a single qualitative observation to argue that "altering prompts can resolve knowledge conflicts and improve task performance across tasks." This is acceptable as *motivation* for the method (the main evidence comes from the comprehensive experiments in Section 3), but the introductory framing oversells what one example can support.

- **The explanation for why chunk-based masking works is post-hoc and untested.** The paper notes that full attention cross-contamination hurts complex reasoning (T-EVAL) but helps math/code, and then proposes chunk-based masking as a middle ground. The explanation (citing Zhao et al.'s pre-training finding that packed examples should be similar) is invoked without testing whether the chunk structure actually increases within-chunk similarity in the claimed way. The mechanism is plausible but unvalidated.

- **The attention weight replacement experiment (Table 9) is logically muddled and does not support the claimed narrative.** The paper finds that replacing the chat model's attention weights with MoI's attention weights harms performance (more so than with other SFT models) and concludes "This suggests that the MoI model's attention mechanisms are unable to extract the most relevant knowledge from the original chat MLP." Presenting this under "Why is MoI effective?" is confusing—if anything, this shows that MoI's attention and MLP co-adapt, not that MoI specifically improves attention. The experiment is interesting but the interpretation needs substantial reframing or the experiment should be replaced with a more informative analysis (e.g., per-task attention entropy).

- **Training hyperparameters are absent from the main text.** Learning rate, batch size, number of training steps, warmup schedule, optimizer choice, and precision are not stated. While the appendix (stripped by parser) may contain them, they should be present or clearly referenced in the main text for reproducibility of a methods paper.

### Trivial

None.

## Nice-to-Haves

- Adding a controlled experiment quantifying the effect size and variance of task-specific system prompts across multiple code tasks (beyond the single Boyer-Moore example) would strengthen the motivation.
- A sensitivity study varying chunk size (e.g., 2, 4, 8) and composition order (fixed vs. random) would clarify whether the benefit comes from the mask structure, the fixed domain ordering, or the specific number of domains.
- Comparison to simpler multi-task alternatives such as linearly combining per-task LoRA adapters or weight interpolation from separate domain-specific SFT runs would help isolate whether the benefit comes from joint training or the attention masking.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

- **Criticism that the name "Mixture-of-Instructions" is misleadingly similar to "Mixture-of-Experts"**: This is a stylistic observation, not a substantive weakness. The paper clearly describes the method as a packing-and-masking scheme, and the name alone does not misrepresent the contribution.
- **Strength Finder's claim that the attention replacement experiment "suggests MoI specifically modifies attention to better leverage the original MLP knowledge"**: This interpretation contradicts the paper's own (admittedly confused) conclusion and is not supported. Removed.
- **Criticism about Table 3 being "not visible in the extracted text"**: This is a parser artifact common to PDF extraction. The table exists in the original submission.
- **Criticism about missing appendix content**: The appendix is stripped by the PDF parser. The paper's original submission contains it.

## Novel Insights

None beyond the paper's own contributions. The core insight—that combining per-task system prompts with chunk-based attention masking during packed multi-task SFT yields consistent improvements—is practical but not conceptually surprising given prior work on prompt engineering and attention masking in pre-training.

## Suggestions

1. **Rewrite the loss function section (2.4) cleanly.** Provide a single, self-contained equation for the MoI loss using clear notation. Define $K$ chunks per packed sequence, $M$ instructions per chunk, and show the attention mask structure explicitly. The build-up from $\mathcal{L}_{\text{seq}}$ to $\mathcal{L}_{\text{packed}}$ to $\mathcal{L}_{\text{masking\_out}}$ to $\mathcal{L}_{\text{MoI}}$ could be moved to an appendix; the main text needs one clear definition.

2. **Reframe or replace the attention replacement experiment (Table 9).** Either provide an analysis that directly tests whether MoI aligns attention with task-relevant features (e.g., per-task attention entropy, domain-specific token attribution) or remove the experiment if it cannot be cleanly interpreted.

3. **Add training hyperparameters** (learning rate, optimizer, scheduler, batch size, number of steps/epochs, warmup) to the main experimental setup section.

4. **Temper the motivational claims** about the system prompt discovery to accurately reflect that it is based on a single case study, and clarify that the main evidence for MoI's effectiveness comes from the controlled experiments in Section 3.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>