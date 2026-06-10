Now let me produce the final consolidated review.

## Summary

This paper introduces QK-score and Attention-score — two methods that extract answer predictions from specific "select-and-copy" attention heads in LLMs rather than from the final output logits. The method is evaluated across LLaMA2 and LLaMA3 models (7B–70B) on several MCQA benchmarks (MMLU, CosmosQA, HellaSwag, HaluDialogue) and a synthetic dataset (SSD), showing consistent improvements over the standard logit-based baseline, particularly for smaller models in zero-shot settings.

## Strengths

- **Large-scale empirical validation across model scales (7B–70B):** Table 1 (lines 209–240) reports 80+ accuracy comparisons across LLaMA2-7B/13B/70B and LLaMA3-8B/70B, including chat/instruct variants. The breadth directly supports the claim that select-and-copy heads exist universally, not just at one model size.

- **Causal evidence via zero-ablation (Figure 4, lines 252–254):** Ablating the top 10 select-and-copy heads causes accuracy drops "sometimes below random performance." This goes beyond correlation — it demonstrates that these heads play a causal role in the model's MCQA output.

- **Robustness to option permutation:** The PA (Permutation Accuracy) metric (defined lines 176–179) measures stability under option shuffling. Across all datasets in Figures 3 and Table 1, QK-score's PA consistently exceeds the baseline PA, often by wide margins (e.g., HellaSwag QA with LLaMA2-13B: 38.8 vs. 17.1).

- **Systematic token analysis (Figure 2b, lines 249–250):** The paper compares five different option-representative token types (label, period after label, end-of-line, period after content, mean aggregation), showing that the end-of-line token works best in zero-shot. This empiricism strengthens the design decisions.

- **Synthetic dataset cleanly isolates format-following difficulty:** SSD (lines 149–151) uses trivial word-matching questions where the model explicitly "knows" the right answer, disentangling knowledge from format-following. The paper frames this as "mitigating MCQA format limitations" (Abstract), not as knowledge extraction — a clear and appropriate framing.

## Weaknesses

### Fatal
None.

### Major

- **The QK-score definition is technically ambiguous regarding RoPE, and the paper's claim about what it measures is unclear.**  
  The paper states (line 117): "In QK-score we do not apply positional transformation, therefore it is not equal to the attention scores before softmax." However, in all LLaMA-family models tested (which use Rotary Position Embedding), RoPE is applied *inside* the computation of the query and key vectors themselves. If the paper extracts q_N and k_{t_i} from the model as-is, these vectors already encode positional information through the RoPE rotation. In that case, the QK-score (q_N^T k_{t_i}) is proportional to the pre-softmax attention logit, contradicting the claimed distinction. If the paper instead modifies the forward pass to extract unrotated vectors, this is a significant implementation detail that is not disclosed. Either way, the claimed ability to measure "semantic rather than positional alignment" is not grounded in a clear technical mechanism. This affects the paper's central explanatory narrative, though the *empirical* finding that certain heads' q-k dot products outperform the final logit baseline stands independently.

### Minor

- **Few-shot demonstration selection is not reproducible (line 184):** The demonstrations are "chosen from the first fifteen entries of the validation set, and their choice was mostly arbitrary, but we tried to filter out questions that we considered suboptimal from the perspective of an English-speaking human expert." This introduces uncontrolled subjectivity. For a small number of demonstrations (≤5), this could meaningfully affect results. A fixed reproducible procedure (e.g., first K entries or random sampling with reported variance) would be preferable.

- **Unsupervised head selection is under-validated (lines 291–294):** The paper proposes an unsupervised heuristic (high attention weight on options + high variance across options) but only reports that the heads "get into top-20" when scored across real datasets and "top-10" on the synthetic dataset. No quantitative accuracy comparison between unsupervised and supervised head selection is reported, making it unclear whether the unsupervised approach is practically useful.

- **Method advantage erodes or reverses on the largest models, but this pattern is under-discussed:** On LLaMA3-70B MMLU, QK-score accuracy is 74.5 vs. baseline 75.3; on LLaMA2-70B MMLU, 56.7 vs. 59.7. The paper acknowledges this briefly (line 193: "MMLU is the most difficult benchmark for our method") but does not discuss what this pattern implies about the method's mechanism — specifically, that it may be compensating for format-following weaknesses of smaller models rather than uncovering "hidden knowledge."

- **Computational cost and practical applicability are not discussed:** The method requires running a full forward pass, extracting per-head q/k vectors for all heads, and computing QK-scores for all options on a validation set to select the best head. This is substantially more expensive than the logit-based baseline. Additionally, the method requires white-box access to model internals, which is not available through standard API access. These practical limitations are not acknowledged.

- **Table 1 includes columns for "-30B" and "-65B" (original LLaMA v1) that are never introduced in the running text** (line 211). The text only mentions LLaMA2 and LLaMA3 families.

### Trivial

None beyond what is already captured above.

## Nice-to-Haves

- An error analysis or case study showing examples where QK-score selects the correct answer but the baseline chooses wrong, and vice versa, would help readers understand what kinds of errors the method corrects.
- Variance or confidence intervals on the reported accuracy numbers would strengthen the comparisons, though single-run evaluation is the norm for deterministic LLM benchmarks.
- Reporting PriDe performance on the standard (4-option, no E/F) version of the data, even as an additional comparison, would clarify whether the QK-score advantage extends to that setting.

## Removed Points

These points from the reviewers were found to be invalid or insufficiently grounded after checking against the paper:

- **"SSD results are dramatically overstated"** — *Removed.* The paper explicitly frames SSD as testing "format limitations" (line 149: "estimate the ability of the model deal with the bare task format"), not knowledge extraction. The Abstract separates "knowledge extraction" (real benchmarks) from "mitigating MCQA format limitations" (SSD). The critic's claim that the paper presents SSD as evidence of hidden knowledge extraction is a misreading.

- **"Baseline comparison is partially staged"** — *Removed.* The baseline (argmax of label token probabilities) is the standard approach used across the MCQA literature. PriDe is compared within the same experimental setup — the E/F options are added to *all* experiments (line 151: "in all five datasets we specially modified questions by adding two extra options"), so comparing PriDe in this same setup is fair, not cherry-picked.

- **"Head selection introduces a multiple-comparisons problem"** — *Weakened and moved.* The theoretical concern about selecting the best of hundreds of heads on 5% validation data is valid, but the paper provides mitigating evidence: the same heads (14,20) and (14,24) consistently emerge as best across multiple datasets and shot settings, and the ablation study confirms their causal role. Moved to Minor and folded into other observations.

- **"Last token is ambiguous"** — *Removed.* The method description and Figure 1 make it clear that q_N is the last token of the input sequence (the token after "Answer:"). This is sufficiently specified for reproducibility.

- **Strength Finder claims about "complementary bias patterns"** — *Moved here.* This is a minor observation (two heads have complementary A/D vs. B/C biases), reported in a single sentence with no further analysis. Interesting but too preliminary to count as a strength.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses primarily surface the paper's framing issues and technical ambiguities rather than generating wholly new observations about the work.

## Suggestions

1. **Clarify the QK-score computation with respect to RoPE.** State explicitly whether q and k vectors are extracted before or after the RoPE rotation. If before, disclose the implementation. If after, correct the claim that QK-score "does not use positional information" and reframe the explanation of why QK-score differs from attention logits.

2. **Replace the subjective few-shot demonstration selection** with a fixed procedure (e.g., first K entries from the validation set) and report whether results vary across different demonstration sets.

3. **Provide quantitative accuracy results for the unsupervised head selection** method, comparing it directly to supervised selection on the validation set, to substantiate the claim that labeled data is not required.

4. **Add a discussion of the eroding advantage on large models** (especially MMLU), and consider reframing the paper's claims from "extracting hidden knowledge" to "compensating for format-following weaknesses in smaller models," which is better supported by the data.

5. **Acknowledge the practical limitations** (white-box requirement, computational overhead) and discuss potential mitigations or use cases where these costs are justified.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>