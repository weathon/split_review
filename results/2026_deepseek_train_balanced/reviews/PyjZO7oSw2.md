Now I'll write the consolidated review.

## Summary

This paper proposes SuperCorrect, a two-stage framework for improving mathematical reasoning in small LLMs. Stage 1 (HSFT) uses a large teacher model (o1-mini/GPT-4o) to reformat ground-truth solutions into hierarchical thought templates with step-by-step XML annotations, key-step explanations, and high-level generalizations, which are then used for supervised fine-tuning. Stage 2 (Cross-model DPO) collects incorrect student solutions, has the teacher identify and correct the first erroneous step, and applies DPO to prefer the teacher's correction over the student's own attempted correction. On MATH/GSM8K, SuperCorrect-Qwen-7B achieves 70.2%/89.5%, outperforming the base Qwen2.5-Math-7B by 15.1/6.3 points.

## Strengths

- **Strong empirical results for a 7B model.** Table 1 shows SuperCorrect-Qwen-7B at 70.2% on MATH — a genuinely impressive number. The improvement over the base model (55.1→70.2) is substantial, and the method generalizes across three different base models (Qwen, DeepSeek, Llama-3.1).

- **The HSFT vs. SFT comparison is clean and well-controlled.** Table 2 shows HSFT (+5.0% on MATH over the Qwen base) clearly outperforms traditional SFT (+2.3%), with the same data sources. This provides solid evidence that the hierarchical thought format itself adds value beyond standard CoT-style SFT on the same problems.

- **Additional analyses strengthen the evaluation.** The topic-level breakdown (Figure 4) shows gains across all seven MATH categories, with larger improvements on topics where the base model was weakest. The stability analysis (256 repeated trials on level-5 problems, Figure 5) examines variance rather than relying on a single pass. The self-correction comparison (Figure 3) shows SuperCorrect gains 5–6% from revision while baselines stagnate or decline.

- **Method is clearly described and well-motivated.** The two-stage design, the error-localization procedure, and the thought-level DPO formulation (Equation 10) are communicated concretely with illustrative examples and a clear prompt template.

## Weaknesses

### Fatal
None.

### Major

- **The ablation for Cross-model DPO compares against Reflexion (inference-only prompting), not against standard DPO or Step-DPO, leaving a central claim unsubstantiated.** Table 2 shows Base-HSFT+Reflexion at 63.1% vs. Base-HSFT+Cross-DPO at 70.2%, a 7.1-point gap. Reflexion is a prompting-only method — it does not involve any training. The paper's core claim is that *cross-model* correction traces (teacher vs. student) are the key ingredient. But this comparison cannot distinguish between two hypotheses: (a) the cross-model asymmetry matters, versus (b) applying *any* DPO training — even standard DPO on the same correction data without cross-model pairing — would produce similar gains. The paper cites Step-DPO in related work and critiques it, yet does not include it (or standard DPO) as a baseline. This is not a fatal flaw — the overall system clearly works — but it is a significant evidential gap in the argument for the paper's most distinctive contribution.

### Minor

- **The "traditional SFT" baseline in the ablation is underspecified.** Table 2 reports "Base + SFT" at 57.4%, but the paper never states what data, format, or prompt this baseline uses. If it trains on the same 100k problems in plain CoT format, the 5% HSFT gain is fairly attributed to the hierarchical template. If data or quantity differ, the comparison is confounded. This should be clarified.

- **Dataset size figures are reported inconsistently.** The abstract (line 29) states 10k preference samples, while the experimental setup (line 377) describes collecting 20k incorrect reasoning results. These figures may be reconciled (e.g., 20k raw → filtering → 10k final pairs), but no explanation is given. Similarly, how ~15k unique problems (7,500 + 7,473 + 670 + sampled additions) produce 100k HSFT training samples is not explained — whether multiple templates are generated per problem or data augmentation is used.

- **No inference decoding parameters are reported.** Training hyperparameters are given (lines 380–381), but temperature, top-p, number of samples, and other inference settings are absent. This is especially needed for the stability analysis (256 repeated runs, Figure 5), where decoding configuration directly affects variance.

- **Error localization accuracy is claimed but not measured.** The paper states that Cross-DPO enables the student to "accurately locate the erroneous steps" (line 254, 435), but no metric — automated or human-evaluated — is reported for how often the student correctly identifies the error step vs. the teacher. This would strengthen the self-correction claim.

- **No limitations section.** The conclusion lacks a discussion of limitations. The most prominent are: the method requires access to a strong teacher LLM (API costs), ground-truth solutions for generating hierarchical thoughts, and the teacher's correction process has access to the ground truth while the student's does not — an asymmetry whose implications for what the student can realistically learn could be discussed more explicitly.

### Trivial

- None beyond the minor issues above.

## Nice-to-Haves

- Adding a standard DPO or Step-DPO baseline to the ablation would directly address the central evidential gap.
- A brief discussion of potential data contamination (teacher models may have seen MATH/GSM8K test sets during training) would strengthen reproducibility.
- Reporting decoding parameters for all evaluations.

## Removed Points

- **"Several recent math models are absent from the comparison table"** (Harsh Critic). No specific missing models were named. The table includes the most relevant baselines — Qwen2.5-Math-7B and DeepSeekMath-7B (the paper's own base models) — alongside 12 other 7B math-specific models. Removed as speculative.
- **"The teacher's role is primarily reformatting, not knowledge distillation"** (Harsh Critic). While the teacher is given ground-truth solutions, it also identifies which steps are "challenging and tricky" and provides generalized solution strategies. This goes beyond pure reformatting. Weakened to a minor observation about the asymmetry and folded into the limitations point above.
- **"The comparison set is not sufficiently current"** (Harsh Critic). Overlaps with the first removed point; no specific missing work was identified.
- **Strength Finder's claim that "the ablation study isolates the contribution of each stage"** (Strength Finder #2). This strength conflicts with the verified major weakness. The HSFT vs. SFT comparison is clean, but the Cross-DPO vs. Reflexion comparison does not isolate the cross-model contribution. The strength is partially correct about HSFT but overstates the evidence for the second stage.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface the same core tension: the method clearly works well, but the evidence for why it works (specifically, whether the cross-model DPO mechanism is the reason or any DPO on correction data would suffice) is incomplete. This is a useful observation for the authors but does not constitute a novel analytical insight.

## Suggestions

- **The single highest-priority revision:** Replace the Reflexion column in Table 2 with standard DPO (or Step-DPO) trained on the same pairwise correction data. If the gap between Cross-DPO and standard DPO remains large (~5%+), the cross-model claim is strongly supported. If the gap shrinks to 1–2%, the paper's contribution is better characterized as the HSFT stage plus DPO training on error-correction data, with the cross-model mechanism playing a smaller role.
- Clarify what "traditional SFT" means in the ablation — data source, format, and prompt.
- Explain the dataset construction pipeline: how 20k incorrect results become 10k preference pairs, and how ~15k problems become 100k HSFT samples.
- Report decoding parameters (temperature, top-p) for all evaluations.
- Add a limitations paragraph acknowledging the teacher dependency, ground-truth requirement, and the asymmetry in correction generation.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>