Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper investigates whether example selection for in-context learning (ICL) amplifies social biases in LLMs. It constructs EEC-paraphrase (a paraphrased sentiment classification dataset for bias evaluation), evaluates 8 LLMs × 4 selection methods, and reports three findings: (1) high accuracy does not imply low bias, (2) example selection amplifies *maximum* bias relative to zero-shot, and (3) example selection contributes to spurious correlations. The paper then proposes ReBE, a prompt-tuning method that learns bias-aware embeddings guided by a contrastive loss designed to make representations invariant to demographic attributes within the same label.

## Strengths

- **First systematic evidence that ICL example selection amplifies worst-case bias**: Figure 2 shows that across 8 LLMs (LLaMA-2, OPT, GPT-J, GPT-neo families), random-based example selection consistently increases the *maximum* bias (AvgGF, MaxTG, MaxFG) relative to zero-shot, while decreasing mean bias. This nuanced finding — that selection improves average fairness but worsens the worst case — goes beyond prior work on ICL bias and is actionable for practitioners.

- **Null-prompt analysis isolates the contribution of example selection to spurious correlations**: Using content-free prompts to measure parameter-level (native) bias, Figure 4 shows that fear-label tendency is nearly identical for female and male groups, yet Figure 3 reveals a large disparity (male sadness→fear misclassification at 0.54 vs. female at 0.08) in the ICL setting. This provides plausible evidence that the spurious correlation originates from the selected examples, not pre-training.

- **ReBE's bias-contrastive loss demonstrably reduces maximum bias in 7/8 tested configurations**: Comparing absolute values in Table 3 (post-debiasing) against Table 2 (pre-debiasing), the maximum AvgGF decreases for 7 out of 8 model×selection combinations (e.g., DPP+ReBE reduces OPT-6.7B's max AvgGF from 0.110 to 0.073). The ablation study (Table 4) cleanly establishes that L_bias is responsible for bias reduction.

- **Compatibility across four existing example selection methods**: ReBE is evaluated on top of Random, Perplexity, Similarity, and DPP selection, consistently reducing max bias, demonstrating general applicability.

## Weaknesses

### Major

- **The debiasing method is compared only against weak baselines, making it difficult to assess relative effectiveness**: Table 5 compares ReBE against only two context-augmentation strategies (counterfactual context and gender-balanced context). No existing debiasing techniques adapted for ICL are used as baselines — not fairness-prompts ("be fair"), not adversarial debiasing, not instruction-based methods, and not the methods from Ma et al. (2023) which the paper cites as related work. While the paper notes that "no other debiasing methods specifically for ICL" exist, this does not excuse the absence of adapted versions of general debiasing approaches. The claim that ReBE "effectively mitigates biases" would be substantially stronger if it outperformed an explicit fairness instruction baseline.

### Minor

- **The subscripts in Table 3 are confusing and potentially contradictory with the reported absolute values**: The caption states "Red subscript indicates that the metric increases after debiasing, and blue subscript indicates that the metric decreases after debiasing." However, for the "Max" rows, the subscripts are almost all red (positive), suggesting an increase, while the absolute post-debiasing maximum values in Table 3 are lower than the pre-debiasing maximum values in Table 2 for 7/8 cases. For example, Random/GPT-neo-2.7B: max AvgGF goes from 0.13 (Table 2) to 0.083 (Table 3) — a decrease — yet the subscript is red (+0.044). The paper does not specify what baseline the subscripts compare against, making it impossible to interpret them. The absolute values support the paper's claim, but the subscripts as presented are misleading and should be clarified or removed.

- **GPT-3.5-Turbo paraphrasing of EEC introduces a potential confound for bias measurement**: The dataset EEC-paraphrase is constructed by having GPT-3.5-Turbo paraphrase the original EEC templates. If GPT-3.5-Turbo has its own systematic biases, it could introduce correlations between demographic groups and sentence structures or vocabulary that are unrelated to sentiment. The paper mentions quality validation in Appendix A (not visible in the main text) but does not discuss this confound or provide a control experiment comparing bias scores on the original EEC vs. EEC-paraphrase. This does not invalidate the findings but weakens their interpretability.

- **The spurious correlation claim (Finding 3) is correlational, not causal**: The analysis in Section 3.4 demonstrates a *correlation* between example selection and the presence of spurious group disparities, but does not manipulate the examples to show that the spurious correlation moves with selection. The paper appropriately uses hedging language ("we believe the disparity... occurs because...") in places, but the contribution list states "example selection contributes to spurious correlations" as a definitive finding. A causal experiment (e.g., swapping demographic attributes in selected examples and showing the disparity shifts accordingly) would strengthen this claim.

### Trivial

- Figure 2 caption refers to "gpt-cj-6b" instead of "gpt-j-6b" (visible in the parsed figure text).
- The footnote for Table 2 appears to have a formatting issue ("Avg<sub>C(Min)</sub> are the largest two values in AvgGF; Avg<sub>G(Min)</sub> are the largest two values in MaxTG and MaxFG" — the subscript notation is unclear).

## Nice-to-Haves

- A comparison against re-adapted general debiasing baselines such as fairness-instruction prompts or adversarial debiasing would substantially strengthen the method evaluation.
- A control experiment comparing bias scores on original EEC vs. EEC-paraphrase would help isolate the effect of the paraphrasing step on bias measurement.
- A causal experiment for the spurious correlation claim (e.g., swapping demographic terms in selected examples) would elevate the third finding from an association to a demonstrated mechanism.

## Removed Points

- **Harsh critic's claim that Table 3 is "critically flawed" and makes the method's success "unverifiable"**: Overstated. While the subscripts are confusing, the absolute values in Table 3 and Table 2 are directly comparable and support the paper's claims. The critic's assertion that "the method's reported success is unverifiable" is not justified — the core data is accessible and consistent with the claims.
- **Harsh critic's speculation about Appendix A content**: The paper explicitly states quality validation is in Appendix A, which was stripped by the parser. Criticizing absent appendix content is invalid.
- **Strength Finder's generic strengths about "important problem" and "first systematic identification" claim**: The "first" claim is retained but noted as slightly over-stated given Ma et al. (2023).
- **Strength Finder's strength about "construction of a more natural bias evaluation dataset"**: While technically true, this is a modest contribution (paraphrasing existing templates) and is not a core strength.

## Novel Insights

The reviews converge on an interesting tension: the paper's most valuable finding is that example selection amplifies worst-case bias while reducing mean bias — a nuanced observation that could influence how practitioners audit ICL deployments. Yet the paper's proposed solution (ReBE) is presented as the main contribution, whereas the evidence for it is weaker (confusing Table 3, weak baselines). This creates a mismatch between where the paper's genuine novelty lies (the empirical diagnosis) and where it invests its narrative weight (the prescription). A reframed version that foregrounds the three empirical findings as the primary contribution and positions ReBE as a preliminary mitigation attempt would be stronger.

## Suggestions

1. **Fix Table 3**: Either remove the confusing subscripts or clearly specify what they compare against. Better yet, add side-by-side columns showing pre- and post-debiasing values for both mean and max so readers can directly verify the claimed reduction.
2. **Add stronger baselines for ReBE**: At minimum, compare against an explicit fairness instruction prompt (e.g., "Please make your prediction without regard to gender") and/or an ICL-adapted version of a simple debiasing technique. This is essential to establish that ReBE offers advantages beyond simple prompting.
3. **Reframe the contributions**: Consider making the three empirical findings about bias amplification the primary contribution, with ReBE as a secondary demonstration of one possible mitigation approach.

## Score and Decision

**Calibration anchors:**
- *Round 1 (bracketing 4.0–6.0)*: Weak anchors (score <3.5): M7CblLwJB8 (2.60, bias finetuning, rejected), Y8DClN5ODu (3.40, demonstration distillation, rejected) — both weaker. Middle anchors (3.5–7.5): 7GKbQ1WT1C (5.25, Prompting Fairness, accepted poster), FEDnzAhIT4 (5.75, Test-Time Fairness, rejected), IHqlU2J5ia (4.25, Restyled ICL alignment, rejected). Strong anchors (>7.5): SPS6HzVzyt (8.00, oral) — much stronger.
- *Round 2 (narrowing 4.5–5.5)*: 0upMDCx8AA (3.67, bias injection, rejected) — weaker. XuQJ5a3sTb (4.75, fair representation, withdrawn) — comparable. 1XzTxtezgj (4.40, causal discrimination, rejected) — comparable. Spp2i1hKwV (6.00, ICL annotations, accepted poster) — stronger execution. pdf6MbXnAS (5.75, ICL shifts, rejected) — comparable. The paper sits between the weaker rejected papers (3.67–4.40) and the accepted posters (5.25–6.25), closest to the 4.40–5.75 range.

Compared to **Prompting Fairness** (5.25, accepted poster): that paper has a stronger causal theoretical framework and broader evaluation across multiple domains. This paper has a more novel empirical finding (bias amplification from example selection) but weaker method evaluation and presentation issues. Slightly weaker overall.

Compared to **Restyled ICL** (4.25, rejected): this paper has more convincing empirical evidence and a working debiasing method, making it clearly stronger.

The paper's genuine empirical contributions and clean Figure 2 evidence are merits, but the confusing Table 3 presentation, weak debiasing baselines, and correlational-only support for the spurious correlation finding prevent acceptance at a competitive venue. Score 5.0 — Reject.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>