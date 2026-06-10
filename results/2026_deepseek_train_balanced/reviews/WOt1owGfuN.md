## Summary

This paper proposes Probe Pruning (PP), a framework for online dynamic structured pruning of LLMs. The key idea is to run a small subset of each batch's hidden states (a "probe") through a few layers ahead to obtain intermediate representations, then use those to make per-batch pruning decisions. PP operates without fine-tuning or additional network modules, achieving speedups comparable to static pruning methods while maintaining significantly better perplexity and downstream task accuracy.

## Strengths

- **Novel and well-motivated dynamic probing concept**: The core idea — running a small subset of each batch forward to obtain intermediate hidden states for per-batch pruning decisions — is genuinely novel. The motivation is grounded in a verified phenomenon: batch-dependent outlier features in LLMs that static calibration-dataset-based pruning cannot capture. The paper provides concrete evidence of this calibration bias (FLAP achieves 18.5 PPL when calibrated on WikiText2 vs 38.9 when calibrated on C4, lines 20–21).

- **Low computational overhead, verified through two complementary measures**: The paper reports both formal complexity analysis (Section 4.1, line 84) and empirical FLOPs measurement using DeepSpeed (Table 4, lines 177–178), confirming probing uses ~1.5% of dense inference FLOPs. Importantly, the paper also reports actual wall-clock speedups (Table 5), showing PP achieves 1.46× speedup in attention and 1.30× in MLP blocks — comparable to static methods — demonstrating the overhead is practically manageable.

- **Consistent empirical superiority over static pruning baselines**: PP outperforms Wanda-sp and FLAP across LLaMA-2-7B/13B, LLaMA-3-8B, and OPT-13B at multiple pruning ratios on both WikiText2 perplexity and commonsense reasoning accuracy (Tables 2, 3). For instance, PP achieves 16.8 PPL vs FLAP's reported range on LLaMA-2-7B at 40% pruning (lines 95–96).

- **Component ablation partially disentangles contributions**: Table 7 (line 201) demonstrates that the PPsp metric alone, used in a static pruning setting (no dynamic probing), achieves 29.7 PPL on LLaMA-2-7B, substantially outperforming FLAP (38.2) and Wanda-sp (43.8). This cleanly isolates the metric's contribution from the dynamic mechanism. Figure 3 further ablates probe sizes, showing even a minimal probe (batch=1, 5% tokens) yields large gains (29.8→21.7 PPL).

- **Mechanistic validation via Jaccard analysis**: Figure 2 (lines 107–109) shows that PP's selected channels have consistently higher Jaccard similarity with Full-Batch Probing (the theoretical upper bound) than a fix-pruned model, providing direct evidence that the dynamic probing mechanism captures information relevant to optimal pruning decisions.

## Weaknesses

### Fatal
None.

### Major

- **Numerical inconsistency in baseline results for the paper's headline comparison**: Lines 95–96 report that on LLaMA-2-13B at 40% pruning, PP achieves 61.0% average accuracy versus 52.0% for LLM-Pruner and 48.1% for LoRAPrune. However, lines 193–194 report PP achieves 61 while "LoRAPrune achieves 55.5 and LLM-Pruner achieves 54.7" for the same model and pruning ratio. The two descriptions give substantially different baseline numbers (52.0 vs 54.7 for LLM-Pruner; 48.1 vs 55.5 for LoRAPrune), with no explanation for the discrepancy. Since the tables are rendered as images, the correct values cannot be verified from the extracted text. This inconsistency undermines confidence in the reported results and needs clarification.

- **Unsupported claim about fine-tuning harming generalizability**: Line 31 states "we have found that fine-tuning might cause LLMs to lose their generalizability; for example, they may perform worse on certain downstream tasks, such as commonsense reasoning tasks." This claim is presented without any supporting citation or experimental evidence anywhere in the paper. It is used rhetorically to motivate PP's "no fine-tuning" advantage but remains unsubstantiated. If the authors believe this, they should directly demonstrate it (e.g., showing that LLM-Pruner's fine-tuned model performs worse on some tasks than the non-fine-tuned version).

### Minor

- **The "fix-pruned model" baseline in the Jaccard analysis is under-specified**: In Figure 2 (lines 107–109), the comparison is between PP (dynamic) and a "fix-pruned model (without PP)" when measuring alignment with Full-Batch Probing. The paper states the PPsp metric is used consistently, but the calibration data, sample count, and procedure used to produce this fix-pruned model are not described. Since the Jaccard comparison is the paper's primary mechanistic argument for why dynamic probing works, this under-specification weakens the analysis. The improvement could partially reflect the fix-pruned model being configured suboptimally rather than the dynamic mechanism itself.

- **No variance or statistical significance reported for any result**: All perplexity and accuracy numbers throughout the paper are point estimates. Given PP involves probe selection (which may have stochastic elements across batches), reporting variance across multiple evaluation runs or random seeds would help assess the stability and reliability of the claimed improvements.

- **PRR framing is overwrought**: The Performance Runtime Ratio (Eq. 1, lines 187–191) is a reasonable metric, but as shown in Table 5, the speedups of PP, FLAP, and Wanda-sp are nearly identical (1.46× vs 1.45× for attention, 1.30× vs 1.28× for MLP). The PRR is therefore dominated by perplexity differences, making the "2.56× better" claim essentially a rescaling of the perplexity gap. The metric is not misleading, but emphasizing it as a novel evaluation insight is not well-justified — the raw perplexity table already tells the same story.

### Trivial

- None.

## Nice-to-Haves

- Compare PP against a static version of itself: same model, same PPsp metric, but pruning decisions made statically using the calibration dataset (no probing, no history-informed fusion). This would directly measure the value of the dynamic mechanism.
- Report a breakdown of end-to-end wall-clock time across the probing, decision, and inference stages to clarify where overhead arises.
- If the numerical inconsistency above is resolved by citing different columns/metrics (e.g., accuracy vs perplexity, or different evaluation subsets), make this explicit in the prose to avoid confusion.

## Removed Points

These points were considered but removed per the filtering rules. Treat them with caution if referenced elsewhere:

- **Harsh Critic: "Comparison with fine-tuned baselines is fundamentally unfair"** — REMOVED. Comparing complete systems (PP vs LLM-Pruner/LoRAPrune) is standard practice; the paper claims PP as a system outperforms other systems. The critic's demand for ablating the dynamic component is a reasonable suggestion (captured in Nice-to-Haves) but does not make the existing comparison invalid. The paper additionally provides a partial ablation (Table 7) showing PPsp alone beats prior metrics in a static setting.

- **Harsh Critic: "Computational overhead claim conflates FLOPs with latency"** — REMOVED. Factually incorrect: the paper reports both FLOPs overhead (Table 4, ~1.5%) AND actual wall-clock end-to-end speedups (Table 5, 1.46×/1.30×). PP's latency is shown to be comparable to static baselines, which is a strength, not a weakness.

- **Harsh Critic: "Evaluation setup incompletely specified (missing Section 5)"** — REMOVED. Per the instructions, missing sections are parser artifacts that exist in the original submission. Some specific questions about the fix-pruned model remain valid (captured in Minor weaknesses above).

- **Harsh Critic: "PRR metric is misleading"** — DEMOTED to Minor (see Minor weakness 3 above). The metric is reasonable; the critic's characterization as "misleading" and "self-serving" is overstated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the numerical discrepancy**: In the final version (or rebuttal), explain why lines 95–96 and lines 193–194 report different baseline numbers for LLM-Pruner and LoRAPrune on LLaMA-2-13B at 40% pruning. If they refer to different metrics or evaluation conditions, state this explicitly in the text.
2. **Substantiate or remove the fine-tuning generalizability claim**: Either provide evidence (even a small experiment or a citation) that fine-tuning can degrade downstream performance, or remove the claim as it currently lacks support.
3. **Specify the fix-pruned model configuration**: In the Jaccard analysis, state clearly what calibration data, sample size, and procedure were used to generate the fix-pruned model baseline.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>