Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me produce the consolidated review.

## Summary

DELIFT introduces a pairwise utility metric (UF_{ij}) that measures how much one data sample improves the model's prediction of another in an ICL setting, then combines this metric with submodular functions (Facility Location, FLMI, FLCG) to select informative, diverse data subsets for LLM fine-tuning. The framework is evaluated across three stages (instruction tuning, task-specific fine-tuning, continual fine-tuning) on six dataset pairs, two model scales (3.8B, 72B), and both ICL and QLoRA settings, consistently selecting 30% of data while achieving performance within ~1–5% of the full dataset and often outperforming baselines (SelectIT, LESS, Random).

## Strengths

- **Unified framework across three distinct fine-tuning stages**: The paper is one of the first to propose a single data-selection algorithm (same utility metric + different submodular functions) that works across instruction tuning, task-specific adaptation, and continual fine-tuning, with experiments on six dataset pairs demonstrating consistent gains over stage-specific baselines.

- **Empirical performance with 70% data reduction is well-supported**: In most settings, DELIFT's 30% subset achieves performance within 1–5% of the full dataset. In the HotpotQA→MMLU task (Table 5), DELIFT even exceeds full-data accuracy by 3.34% (Qwen2) and 4.20% (Phi-3), suggesting the utility-based selection effectively filters noisy/harmful data.

- **Utility kernel ablation confirms its value**: The comparison between "Util. Feat." (full DELIFT) and "SE Feat." (DELIFT with sentence embeddings instead of the utility kernel) consistently favors the utility kernel across nearly all settings (e.g., MixInstruct Qwen2 ICL: ROUGE 48.46 vs. 47.43), providing direct evidence that the novel pairwise utility metric—not just the submodular optimization framework—drives the improvement.

- **Evaluation across two model scales and both ICL/QLoRA**: Testing on Phi-3 (3.8B) and Qwen2 (72B) with both ICL and QLoRA yields 12 combinations per use case, demonstrating the method's robustness.

## Weaknesses

### Fatal

None.

### Major

- **Missing specification of how UF_{ij} becomes the similarity s_{ij} used in submodular functions**: The paper defines UF_{ij} (Eq. 1) as a non-symmetric utility value, then defines the submodular functions (FL, FLMI, FLCG) over a similarity measure s_{ij} (Eqs. 3–5). However, it never explicitly states the relationship between UF_{ij} and s_{ij}. While the submodular functions can technically operate on asymmetric values (the max-over-selected-set formulation works with any real-valued matrix), the paper should state this unambiguously—e.g., "we set s_{ij} = UF_{ij}" or specify a symmetrization/transformation. Without this, the method is incompletely specified and cannot be reproduced as stated. This is a genuine clarity gap, not a fatal flaw, but it must be resolved.

- **Computational efficiency claim is entirely unsupported and contradicts the apparent cost**: The paper claims "at least 70% reduction in computational time compared to gradient-based methods" (Contribution 3) but presents zero runtime measurements, wall-clock comparisons, or complexity analysis. Computing UF_{ij} for all pairs (i,j) in a dataset of 21,000 samples would require ~441M conditional forward passes (each with an ICL prefix), which is orders of magnitude more expensive than gradient-based methods like LESS (which requires O(N) LoRA forward-backward passes). The paper does not clarify whether the full N×N kernel is computed or a subsample is used, and provides no analysis of practical scalability. Without this information, the efficiency claim is unsubstantiated.

- **Empty table for a main experimental result**: The MixInstruct→MT-Bench table in the \small-formatted set (lines 371–390) has **all data cells empty**—every method row (Initial, Random, SelectIT, LESS, SE Feat., Util. Feat., Full Data) contains blank cells with no numeric values. This makes one of the three use-case results completely unreadable. The earlier \scriptsize version of this table (lines 239–259) has valid data, suggesting a compilation error where an incomplete revision replaced the correct version.

- **Duplicated tables and inconsistent formatting**: The paper contains two complete sets of essentially identical tables (one in \scriptsize format with \sysn{} naming, another in \small format with "Util. Feat."/"SE Feat." naming). The SQuAD+HotpotQA table appears three times (lines 286–305, 433–452, 454–473). The naming inconsistency (\sysn{} vs. Util. Feat.) across table sets, while semantically clear, creates an unprofessional presentation and raises concerns about which version reflects the intended final results.

### Minor

- **"Performance percentage drop" metric is poorly defined**: The paper reports aggregated "performance percentage drop" (e.g., "10.44% performance percentage drop from Full Data to \sysn{}") without specifying how this is computed across metrics on different scales (ROUGE ~0–100, BGE ~0–100, LAJ 1–5). Averaging raw scores across these scales is not meaningful. The paper should clarify (e.g., normalize each metric or report per-metric drops).

- **No statistical significance or variance reported**: All results are reported as single numbers. Given the often small margins (1–3%), it is not possible to assess whether DELIFT's improvements are reliable.

- **GT_i description is ambiguous**: The paper describes GT_i as "modeled as a vector of ones for each token to signify perfect prediction." This could be read as a uniform distribution, which would be incorrect; it should read "one-hot vector" (with a 1 at the correct token index). The intended interpretation (one-hot) is inferable from context, but the wording should be corrected.

- **Ablation on subset size is described only in text**: Section 4.4 states that DELIFT outperforms all baselines at every subset size from 5% to 100%, but no table or figure with actual numerical results is provided. This weakens an otherwise useful ablation.

### Trivial

- Minor: The naming inconsistency (\sysn{} vs. "Util. Feat.", \sysn{} (SE) vs. "SE Feat.") across the two table sets should be resolved.

## Nice-to-Haves

- Include wall-clock runtime comparisons with gradient-based baselines (LESS) to substantiate the efficiency claim.
- Clarify the computational protocol for the utility kernel: is the full N×N matrix computed, or is a subsampling strategy used? If subsampling, describe the procedure.
- Add confidence intervals or error bars from multiple runs or seeds.
- Provide the subset-size ablation results as a table or figure with actual numbers, not just text.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Full Data is sometimes worse — this misinterprets what Full Data represents"** — This criticism suggests that DELIFT's outperformance of Full Data in HotpotQA→MMLU is misleading because Full Data causes catastrophic forgetting. However, DELIFT's ability to select data that avoids catastrophic forgetting is a *feature* of the method, not a bug. The baselines LESS and SelectIT also select subsets and do not achieve the same performance. Removed because this is a misinterpretation of the result.

2. **"The flattened probability vector has N×V dimensions which is computationally infeasible"** — The distance metric can be computed token-by-token without ever materializing the full N×V vector (it reduces to computing per-token cross-entropy-like terms). The reviewer's specific concern about dimensionality is overblown; the paper's teacher-forcing setup naturally computes this incrementally. However, the broader concern about O(N²) forward passes (not the distance computation itself) remains valid and is retained above.

3. **Strawman criticism about sentence-embedding comparison being unfair to baselines** — Not found in the reviewer's comments; no action needed.

4. **Generic criticisms about "could add more models/datasets"** — Not found in a form that fits this category.

5. **Pure formatting nitpicks** — The naming inconsistency (\sysn{} vs. Util. Feat.) is a real issue but the reviewer's framing as "raises concerns about whether the results are reliably reproduced" is overblown. The data values are identical across table versions where both have content.

## Novel Insights

The reviews reveal an interesting tension: the pairwise utility metric (UF_{ij}) is the paper's core novelty, yet its computational cost is essentially unexamined. The metric requires comparing every pair of data points through conditional forward passes—a process that is, on its face, far more expensive than gradient-based alternatives. If the authors are computing the full N×N kernel, the method is likely impractical for any dataset larger than a few thousand samples. If they are subsampling (e.g., computing UF for only a random subset of pairs), this needs to be disclosed and its impact on selection quality analyzed. This blind spot is the single most important missing analysis in the paper—more consequential than the missing s_{ij} specification, because it directly determines whether the method has any practical value.

## Suggestions

1. **Explicitly state the relationship between UF_{ij} and s_{ij}** — even if it is simply "s_{ij} = UF_{ij} (we use the raw utility values as similarities in the submodular functions, which is valid since Facility Location functions operate on arbitrary real-valued matrices)."

2. **Provide a runtime analysis** comparing DELIFT's kernel computation time (wall-clock) against LESS's LoRA gradient computation for the same datasets. Report total preprocessing time (including the kernel) and per-epoch training time for the selected subset.

3. **Clarify the computational protocol**: is the full N×N kernel computed? If not, describe the subsampling strategy (if any) and its impact.

4. **Fix the empty table** — the MixInstruct→MT-Bench table in the \small-formatted set is missing all data.

5. **Remove the duplicate table set** — the paper should contain one complete, consistent set of tables (preferably the \small-formatted version with Util. Feat. naming, which includes proper underlining).

6. **Define the "performance percentage drop" metric clearly** — specify which normalization/averaging formula is used across metrics with different scales.

## Score and Decision

**Overall assessment**: The paper tackles a worthwhile problem with a genuinely novel approach (pairwise ICL-derived utility for data selection), and the empirical results are substantively strong across a broad experimental sweep. However, the submission has three significant problems that prevent acceptance in its current form: (1) a methodology gap where the mapping from UF_{ij} to the submodular similarity s_{ij} is never stated; (2) a completely empty table for one of the three main use cases; and (3) an efficiency claim that is not just unsubstantiated but contradicted by the method's apparent computational profile. These are fixable (the first requires one sentence, the second is a compilation fix, the third requires honest runtime reporting), but as presented the paper does not meet the bar for acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>