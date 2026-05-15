Now I have a thorough understanding of the paper and can compose the final consolidated review.

---

## Summary

This paper argues that large language models possess intrinsic self-correction (SC) ability, contrary to recent claims (Huang et al., 2024) that LLMs degrade after self-correction. The paper re-frames intrinsic SC as functionally similar to chain-of-thought and self-verification, then identifies two factors critical for successful SC: **zero temperature** and **fair (unbiased) prompts**. Through theoretical analysis (variance of binary decisions under temperature scaling, effect of biased prompts) and experiments on 4 LLMs across 2 benchmarks, the authors show that under zero temperature and fair prompts, all tested models improve accuracy after SC — whereas biased prompts or non-zero temperature can cause degradation.

---

## Strengths

- **Principled decomposition of self-correction into a three-stage conditional probability process (Eq. 5) and four operational cases (Section 2.2):** The paper formally models SC as $p(A'|\tau) = p(A'|\tau_3,D,R_2,\tau_2,A,R_1,\tau_1) \cdot p(D,R_2|\tau_2,A,R_1,\tau_1) \cdot p(A|R_1,\tau_1)p(R_1|\tau_1)$ and identifies how different orderings of decision/rationale in Stage 2 map onto CoT and self-verification. This provides a clear theoretical grounding for why SC can improve accuracy.

- **Empirical demonstration that prompt fairness and zero temperature jointly enable SC across models:** Using three progressively unbiased prompt sets (Problem Sets 1–3) and testing GPT-3.5, GPT-4, Mistral-7B, and Phi-3 on CommonSenseQA and GSM8K, the paper shows that under zero temperature and the fairest prompt set, all four models exhibit accuracy gains after SC (Table 5). This directly addresses the debate with Huang et al. (2024) by showing that the reported degradation is not fundamental but contingent on experimental conditions.

- **Mathematically sound derivation linking temperature to decision variance:** The paper proves $\partial Var(D)/\partial T \geq 0$ for the binary decision in Stage 2, showing that higher temperature increases the randomness of the "correct/incorrect" judgment, which can cause accuracy degradation. The ablation fixing Stage 1 responses (Fig. 2b) cleanly isolates this effect.

- **Actionable guidelines for constructing fair prompts:** The paper provides a concrete methodology (Section 5.2) for removing biased language from SC prompts — e.g., avoiding negative phrases like "find the problem" and balancing words like "correct/incorrect" — which is practically useful for the community.

---

## Weaknesses

### Fatal
None.

### Major

- **The paper never demonstrates that the model actually detects and corrects specific errors in its own output, as opposed to simply generating a better answer from scratch using more reasoning context.** The title claims LLMs "have Intrinsic Self-Correction Ability," which implies the model can identify its own mistakes and fix them. But the evidence is only aggregate accuracy deltas. The paper explicitly frames SC as similar to CoT/self-verification (Section 2.2), which weakens the distinctiveness of the claim, and never analyzes whether the final answer differs from the initial answer because the model spotted an error or because the additional reasoning simply produced a better answer independently. Without a per-example breakdown (e.g., accuracy change conditioned on whether the initial answer was correct vs. incorrect), the "self-correction" framing overpromises relative to what is actually measured.

### Minor

- **Lemma 1 is tautological and adds no theoretical insight.** "LLMs are generally under-performing compared to their true ability because hallucination will cause the overall accuracy to decrease" simply restates the observation that models make errors. It does not explain *why* the model cannot arrive at the correct answer initially. The paper would be cleaner without this lemma, since the real theoretical content is in Sections 4–5.

- **Temperature experiments are conducted on only one dataset (CommonSenseQA) and the main temperature effect is observed for only one model (GPT-3.5).** The paper explains this via different decomposition orderings (Order 1 vs. Order 2), but this explanation is post-hoc: the paper does not directly verify the ordering for each model by constraining or probing the generation (e.g., by forcing Order 2 in GPT-3.5). The "universal" claim in the conclusion is not well-supported by the temperature evidence.

- **No error bars or significance tests are reported.** The paper honestly acknowledges this in the Limitations section, but it remains a weakness: the variance in results across queries at different temperatures could affect the conclusions, and the reader cannot assess the reliability of the reported accuracy differences (especially the smaller deltas).

- **The theoretical analysis of biased prompts (Section 5.1) is hand-wavy.** The $\gamma\%$ random-change model is not grounded in actual model behavior. The paper assumes that a biased prompt causes a fixed percentage of answers to flip randomly, but this is an oversimplification — biased prompts likely have asymmetric effects (e.g., more likely to flip correct answers to incorrect than vice versa, or vice versa) that depend on the specific model, task, and prompt wording.

### Trivial
- The paper's Section 3 mentions "C.5,7,8,9, respectively." at the end of line 105, which appears to be a stray reference number fragment.
- The comment block (lines 156–166) contains leftover editing notes with red-colored text that should be cleaned up before publication.

---

## Nice-to-Haves

- **Per-example analysis comparing initial answers, SC rationales, and final answers** to show whether the model actually identifies specific errors in its initial response — this would substantially strengthen the core claim.
- **Controlled comparison forcing Order 2 in GPT-3.5** (e.g., through constrained decoding or prompt engineering) to directly verify the decomposition-ordering explanation for temperature sensitivity, rather than relying on post-hoc attribution.
- **Temperature experiments on GSM8K** to broaden the evidence base beyond CommonSenseQA.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper does not directly refute the prior work it criticizes — it never replicates Huang et al.'s exact experiment"** — Factually incorrect. The paper uses Huang et al.'s exact prompts as Problem Set 1 (Section 5), stating "Case 1 has the same setting with huang2024large, with the only difference being the semantic bias of the prompt." Section 4.2 also explicitly tests temperature effects using Huang et al.'s prompts. The paper does perform controlled comparisons.

2. **"The derivation assumes α is independent of temperature, which is unlikely"** — Incorrect. The formulation $p(D=1) = \alpha^{1/T} / (\alpha^{1/T} + (1-\alpha)^{1/T})$ is standard softmax temperature scaling where α represents the base probability (at T=1 implicitly). α is defined as the "original positive decision probability" and is independent of T by construction.

3. **"Table 1 is not described in sufficient detail (the caption is missing)"** — Parser artifact. Tables are included via `\input{}` commands and are present in the original submission.

4. **"The classification feels post-hoc"** — Speculative; no evidence provided.

5. **"The results table (Table accuracy_temp0) is not actually shown in the provided text"** — Parser artifact. The table is included via `\input{tables/accuracy}`.

6. **"Missing appendix, missing proofs in appendix"** — Parser artifact; appendices exist in the original submission.

---

## Novel Insights

The reviews surface an important meta-point about the self-correction literature: the term "self-correction" implicitly promises error identification and targeted repair, but what most papers (including this one) actually measure is accuracy improvement from multi-stage prompting. The paper is more honest than most in framing SC as functionally equivalent to CoT/self-verification, yet retains the "self-correction" label in the title, creating a tension between the specific conceptual claim (models can fix their own mistakes) and the generic operational finding (more reasoning steps help). A crisp distinction between these interpretations could sharpen future work in this area.

---

## Suggestions

1. **Reclaim the "self-correction" claim** by adding a per-example analysis: condition accuracy changes on whether the initial answer was correct or incorrect. If SC primarily fixes incorrect answers without flipping correct ones, that directly supports the error-correction interpretation. This would not require running new models — just re-analyzing existing logs.

2. **Weaken the "universal" claim** in the conclusion. The temperature evidence is model-specific (GPT-3.5) and dataset-specific (CommonSenseQA). A more precise claim — e.g., "zero temperature is beneficial for SC in models that follow Order 1 decomposition" — would better match the evidence.

2. (minor) **Remove Lemma 1** — it adds no analytical value and the paper's substantive theoretical contributions (temperature variance, prompt bias analysis) stand without it.

4. (minor) **Add significance tests or bootstrapped confidence intervals** to the key accuracy comparisons (Table 5 results) so readers can assess reliability.

---

## Score and Decision

**Originality:** Moderate. The reframing of SC as CoT/self-verification is not entirely novel, but the systematic identification of temperature and prompt fairness as critical factors is useful.  
**Importance of research question:** High. The debate over whether LLMs can self-correct is active and practically relevant.  
**Claims support:** Partial. The paper's operational claims (temperature and prompt bias matter) are reasonably supported. The conceptual claim (models have intrinsic SC ability) is overclaimed relative to the evidence.  
**Soundness of experiments:** Adequate but limited. The experiments are well-designed for the scope, but the limited number of datasets, lack of error bars, and single-model temperature results weaken the conclusions.  
**Clarity of writing:** Good. The paper is well-structured and the theoretical reasoning is clearly presented.  
**Value to community:** Moderate. The guidelines for fair prompts are practically useful. The temperature analysis highlights an important experimental design consideration.

The paper makes a genuine but modest contribution. The core findings — that prompt fairness and zero temperature enable SC across models — are empirically supported and practically useful. However, the experimental scope is limited (2 datasets, no error bars, temperature results mainly for one model on one dataset) and the title overclaims relative to what is actually demonstrated. The paper would benefit from a more measured framing and additional analysis.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>