Now I have all the data I need. Let me write the final consolidated review.

## Summary

The paper introduces Insertion Language Models (ILMs), which generate sequences by inserting one token at a time at arbitrary positions. The authors propose a denoising training objective (Eq. 2) that trains a transformer to predict the distribution of dropped tokens across all gaps given a random subsequence, alongside a learned stop classifier. Experiments on star-graph planning (Table 1) show ILMs dramatically outperforming ARMs (23%→99.1% on Star_hard) and MDMs (21%→99.1%), demonstrating genuine advantages for variable-length constraint-satisfaction problems. On text (LM1B, TinyStories), ILMs outperform MDMs in NLL and LLM-judge scores and are competitive with ARMs on Stories (2.14 vs 2.11 NLL) while lagging more on LM1B (4.67 vs 3.94). Infilling results (Table 3) show consistent improvements over MDMs.

## Strengths

- **Planning-task results demonstrate a clear success mode for insertion-based generation.** Table 1 shows ILM achieving 100% (Star_easy), 100% (Star_medium), and 99.1% (Star_hard) exact-match accuracy, far exceeding ARM (23% on hard) and MDM (21% on hard). The ablation with Insertion Transformer (IT) on the same tasks (35.2% on easy, 17.5% on hard) confirms the dedicated stop classifier is essential. These experiments directly validate the motivation that out-of-order insertion with relative-position modeling solves constraint-satisfaction problems that neither left-to-right generation nor masked diffusion can handle.

- **Variable-length infilling without fixed-mask constraints.** As argued in Sections 1–2, MDMs require a predetermined number of mask tokens and cannot infill arbitrarily long segments. ILM's iterative insertion with learned stop prediction (Algorithm 2) avoids this constraint, and Table 3 shows ILM obtaining better ΔNLL than MDM on both single- and multi-segment infilling across two datasets.

- **Favorable inference-time quality vs. compute trade-off compared to MDM.** Figure 6 shows that for the same per-token generation time on Stories, ILM achieves substantially lower NLL than MDM, and increasing MDM sampling steps (128→1024) does not close the gap.

## Weaknesses

### Major

1. **Biased training objective vs. inference procedure — uncharacterized.** The training objective (Eq. 2) trains the model to predict the *aggregate* distribution of all dropped tokens between each pair of visible tokens, given a uniformly random subsequence. During inference the model inserts one token at a time on sequences built incrementally by its own choices. The paper acknowledges this objective is "biased" (Section 3) but provides no analysis of how the bias affects the model's predictions on the partial sequences encountered during inference, nor any bound on the distribution shift between training (uniform random subsets) and inference (model-dependent trajectories). While similar gaps exist in MDMs and ARMs (exposure bias), the paper's specific formulation — training on the full count-normalized insertion distribution and then sampling single insertions — merits analysis. This is a structural concern about the methodological justification for the training procedure.

2. **Missing Insertion Transformer baseline on text tasks.** The paper compares against IT on star graphs (where it performs poorly) but does not evaluate it on LM1B or TinyStories. Since IT (Stern et al., 2019) is the most direct insertion-based baseline, a side-by-side comparison on at least one text task is needed to assess whether the proposed training objective and stop classifier offer practical benefits for language generation beyond the synthetic planning setting. Without this, the contribution's novelty for language modeling is harder to evaluate.

3. **Abstract overstates text generation results.** The abstract claims ILMs "perform on par with ARMs" in unconditional text generation, but the body acknowledges ILMs "perform slightly worse than ARMs trained for the same number of gradient steps." On LM1B, the NLL gap is substantial (4.67 vs 3.94, corresponding to roughly 2× perplexity difference). The body language ("competitive with ARMs") is more appropriate. The abstract should be revised to match the nuance in the paper.

4. **MDM baseline uses only the vanilla τ-leaping sampler.** The paper evaluates MDMs with simultaneous unmasking (τ-leaping) but discusses improved inference techniques (greedy selection, top‑k unmasking; Gong et al. 2024, Zheng et al. 2024, Campbell et al. 2024) in Section 4 without including them in comparisons. While Figure 6 does ablate MDM sampling steps up to 1024, it does not test these improved sequential-unmasking strategies that directly address the simultaneous-unmasking critique that motivates ILM. Including at least one such variant would strengthen the comparison.

### Minor

- **Length mismatch in text evaluation is discussed but not controlled.** Table 2 shows ILM generates shorter sequences than the data average (119 vs 205 on Stories; 21 vs 28 on LM1B), while MDM overgenerates (985, 85). The paper correctly attributes MDM's high entropy to over-generation but does not control for ILM's under-generation when interpreting NLL or judge scores. Although the evidence does not consistently show that shorter sequences get unfairly favorable NLL (on LM1B, ILM's shorter text has *worse* NLL than ARM's longer text), a controlled analysis (e.g., matching length distributions or reporting length-KL divergence) would address the concern cleanly.

- **No error bars or confidence intervals.** Tables 1–3 and Figure 5 report point estimates without variance, making it impossible to assess the reliability of comparisons. LLM judge scores (Prometheus) in particular are known to be noisy; standard errors across multiple generations or evaluation runs are needed.

- **No ablation of the stop loss or stop threshold.** The learned stop classifier governs the generated length, but its behavior is unexamined — e.g., how sensitive is length to the weight of ℒ_stop, or to adjusting the stop threshold at inference time? This would help understand and potentially correct the under-generation issue.

- **No analysis of the training bias.** The paper motivates the biased objective by citing high variance in the unbiased estimator (Appendix D) but provides no empirical or theoretical analysis (e.g., how large is the bias on real data, does it diminish with sequence length). This is a gap given that the bias is the central design justification.

### Trivial

None.

## Nice-to-Haves

- Compare against Insertion Transformer on at least one text infilling or generation task.
- Include MDM baselines with greedy or top‑k unmasking at comparable compute budgets.
- Ablate the stop loss weight and threshold; report length-KL divergence between generated and data distributions.
- Provide confidence intervals or error bars for the main text evaluation tables.

## Removed Points

*Weaknesses that were flagged by reviewers but removed after verification against the paper:*

- **"Training objective mismatch is a fatal structural issue"** (Harsh Critic Point 1): Downgraded from Fatal to Major. The paper acknowledges the bias and the high-variance justification is standard in generative modeling. The concern is real but not fatal — similar gaps exist in MDMs and ARMs, and the planning results suggest the training does transfer to inference. The paper should analyze this gap, but it does not invalidate the approach.

- **"Length mismatch confounds text evaluation entirely"** (Harsh Critic Point 2, strong framing): The critic claimed shorter texts are "often easier to predict." However, on LM1B the ILM generates shorter text (21 vs 30 tokens) but has *worse* NLL (4.67 vs 3.94), directly contradicting a simple "shorter = easier" story. The concern is valid but the claimed damage is not supported by the paper's own numbers. Downgraded to Minor.

- **"MDM baseline deliberately weak"** (Harsh Critic Point 3, strong framing): The standard τ-leaping sampler is the canonical MDM evaluation approach from the cited literature. The paper additionally compares MDM at multiple step counts in Figure 6. The omission of improved MDM samplers is a real gap but calling the baseline "deliberately weak" overstates the issue. Downgraded to Major (point 4 above).

- **"Omission of IT on text is a methodological gap"** (Harsh Critic Point 4): Kept as Major (point 2 above). The critic's strong claim that this makes it "impossible to determine whether the proposed training objective improves" is slightly overstated — the ILM vs ARM/MDM comparisons are still informative — but the gap is real.

- **"Unconditional generation procedure not specified clearly"**: The paper states in Section 3.1 that the initial sequence contains `<stp>` and `<s>` tokens, and Algorithm 2 (in the appendix, stripped by parser) specifies the procedure. Main-text description is adequate for a conference paper.

- **Strength Finder: "Competitive text generation quality"**: Weakened — kept but with the caveat that the LM1B gap (4.67 vs 3.94) is substantial and the evaluation has length confounds.

- **Strength Finder: "Simpler architecture than MDM"**: Kept as a minor strength — it's a legitimate point but a secondary one.

## Novel Insights

None beyond the paper's own contributions. The paper correctly identifies that insertion-based generation with relative position encoding can solve variable-length constraint-satisfaction problems where ARMs (fixed order) and MDMs (fixed mask positions) fail. This is the paper's genuine contribution, and the planning experiments support it convincingly.

## Suggestions

1. Analyze the bias of the training objective — either theoretically (bound the bias) or empirically (compare predictions on uniform-random vs iteratively-built subsequences). This would significantly strengthen the paper's methodological foundation.

2. Add Insertion Transformer to the text experiments. Even a single dataset comparison would help benchmark ILM against the nearest prior work.

3. Control for length when reporting text generation NLL and judge scores — report length distributions, evaluate on length-matched subsets, or provide length-KL as a secondary metric.

4. Tone down the abstract to match the body's more measured characterization of the text results ("competitive with" rather than "on par with").

5. Report standard errors or confidence intervals for at least the main text evaluation metrics (Tables 2–3, Figure 5).

## Score and Decision

**Score: 5.0**

**Decision: Reject**

*Justification:* The paper has a genuine contribution — the planning experiments clearly demonstrate that insertion-based generation with relative position encoding solves problems where ARMs and MDMs fail. This is compelling evidence for the method's core advantage. However, the paper is held back by several issues that collectively prevent acceptance: (1) the central training-inference gap is acknowledged but uncharacterized, leaving the methodology on uncertain footing; (2) key baselines (Insertion Transformer on text, stronger MDM sampling strategies) are missing, making it difficult to assess the language modeling contribution relative to prior work; (3) the abstract overstates the text results; and (4) the text evaluation lacks error bars and does not control for systematic length differences. The paper would benefit from addressing these issues in a revision. At 5.0, the paper sits between the FiLM anchor (4.25, rejected — similar weaknesses in a closely related topic) and COrAL (5.75, rejected — order-agnostic modeling with similar methodological gaps) in quality.

### Calibration Anchors

| Anchor | Avg Score | Round & Query | Comparison |
|--------|-----------|---------------|-----------|
| FiLM: Fill-in Language Models (UbOzNf6hGq) | 4.25 | R1-any-order-gen | Similar topic, similar weaknesses (training/inference gap, length mismatch, missing baselines). ILM's planning results are stronger. |
| COrAL: Order-Agnostic LM (0JjsZC0w8x) | 5.75 | R2-biased-obj | Order-agnostic/denoising approach. Narrower scope of evaluation. ILM has stronger planning evidence but similar evaluation gaps. |
| SequenceMatch (FJWT0692hw) | 6.00 | R1-topic-mid | Addresses training-inference mismatch with theory+method. ILM is weaker in addressing its own training-inference gap. |
| Interpolating AR and DD Diffusion (tyEyYT267x) | 8.00 | R1-topic-high | SOTA results, strong theory. ILM is substantially weaker in theory and text results. |
| Item Language Model (QFaj7InstQ) | 3.75 | R1-topic-mid | Different domain. Lower scores due to novelty concerns. ILM is stronger. |

**Round-1 bracket:** 4.0–6.0 (based on FiLM at 4.25 and COrAL at 5.75 being the most topically relevant anchors).

**Round-2 narrowing:** The upper part of the bracket was anchored by SequenceMatch (6.0, accepted), which actually *solves* its training-inference mismatch — a bar the ILM paper does not meet. The lower part was anchored by FiLM (4.25, rejected), which has similar evaluation issues. ILM's stronger planning results lift it above FiLM, but the unanalyzed training gap and missing baselines prevent it from reaching the SequenceMatch level. Hence 5.0.

**What the low-band anchors failed at:** FiLM was rejected because of (a) unfair comparison confounded by length, (b) unanalyzed training/inference discrepancy, (c) missing baselines. The ILM paper shares all three issues in some form (Items 1, 2, 4 in Major above). The score reflects that while ILM has stronger planning evidence, the same structural evaluation weaknesses are present.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>