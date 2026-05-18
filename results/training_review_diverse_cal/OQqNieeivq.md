Now I have all the evidence I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes KaSA (Knowledge-aware Singular-value Adaptation), a PEFT method that first performs SVD-based truncation to remove minor/noisy singular components from the base model weights, then learns a low-rank additive update parameterized directly in SVD form (with learned singular values and orthogonal singular vectors). The intuition is that knowledge-aware singular values dynamically activate task-relevant parametric knowledge while suppressing irrelevant information. Experiments cover NLU (GLUE with RoBERTa/DeBERTaV3), NLG (E2E with GPT-2), instruction following (LLaMA3, Mistral, Gemma, LLaMA2 on synthetic datasets and MT-Bench), and commonsense reasoning (LLaMA2/LLaMA3 on Commonsense170K), showing consistent improvements over LoRA, PiSSA, and MiLoRA across nearly all settings.

## Strengths

1. **Novel and well-motivated SVD-based adaptation design.** KaSA's two-stage approach—knowledge-based SVD truncation to remove noisy components, followed by SVD-structured additive updates with learnable singular values—is a clean architectural contribution. Unlike PiSSA (which fine-tunes principal components) and MiLoRA (which fine-tunes minor components), KaSA learns which singular dimensions to activate, providing a principled mechanism to handle knowledge relevance. This design is validated by the ablation study (Figure 3), where the full KaSA outperforms partial variants by 2.05–3.25%, confirming each component's contribution.

2. **Consistent superiority over SVD-based PEFT baselines (LoRA, PiSSA, MiLoRA) across diverse settings.** The paper demonstrates this across 4 model scales, 4 task categories, and multiple benchmarks. Representative results: on commonsense reasoning (Table 5), KaSA achieves 81.5% on LLaMA2 7B vs. 79.2% for MiLoRA and 84.6% on LLaMA3 8B vs. 81.9% for MiLoRA; on GLUE (Table 1), KaSA beats FFT across nearly all tasks with only 0.24% trainable parameters.

3. **Rigorous experimental scope with multiple models, seeds, and tasks.** Experiments use 4 model families (RoBERTa, DeBERTaV3, GPT-2, LLaMA/Mistral/Gemma), multiple model sizes (125M to 13B), 5-run averages for GLUE, 3-run averages for NLG, and p-values for instruction-following results. The budget parameter scalability study (Figure 4) shows KaSA's advantage holds across ranks 1–128.

4. **Practical advantage of zero inference overhead.** KaSA's linear SVD structure allows merging the adaptation module back into the base model, preserving the original inference architecture—a significant practical benefit over adapter-based methods.

5. **Public release of 4 synthetic instruction-following datasets (128K each).** This provides a reusable resource for the community.

## Weaknesses

### Fatal
None.

### Major

1. **The claim "consistently outperforms FFT" is contradicted by the paper's own Table 4.** The abstract and introduction state KaSA "consistently outperforms FFT," but the instruction-following results show clear counterexamples:
   - **Mistral 7B**: FFT beats KaSA on all 4 synthetic tasks (Classification: 6.73 vs. 5.72; Summarization: 7.18 vs. 6.82; Coding: 7.53 vs. 6.74; Closed QA: 8.75 vs. 7.75).
   - **LLaMA3 8B Closed QA**: FFT = 8.90, KaSA = 6.81 (2.09-point gap against KaSA).
   - **LLaMA2 13B Closed QA**: FFT = 8.97, KaSA = 7.12 (1.85-point gap against KaSA).
   - **Gemma 7B Closed QA**: FFT = 8.88, KaSA = 8.69.
   - **LLaMA2 13B Summarization**: FFT = 7.93, KaSA = 7.92 (essentially tied).

   On the synthetic instruction-following tasks across all 4 models, KaSA wins in only 10/16 comparisons, loses in 5, and ties in 1. The claim is only defensible for MT-Bench (where KaSA wins on all 4 models) and GLUE (where KaSA wins in 13/14 scenarios). The paper must either remove the "consistently outperforms FFT" language from the abstract and introduction, or precisely specify the conditions under which it holds, and acknowledge the counterexamples. This is the most significant flaw in the paper as written.

2. **The "14 PEFT baselines" claim overstates the actual breadth of comparison.** The paper lists 14 PEFT baselines in §4.1, but no single experiment includes more than a fraction of them:
   - GLUE tables compare only LoRA, AdaLoRA, DyLoRA, PiSSA, MiLoRA, and select Adapters—**DoRA, VeRA, SARA, and CorDA are absent**.
   - E2E NLG includes SARA and VeRA but not DoRA, CorDA, PiSSA, or MiLoRA.
   - Instruction following (Table 4) and commonsense reasoning (Table 5) compare only LoRA, PiSSA, and MiLoRA.
   - **CorDA and DoRA never appear in any results table**, despite being listed as baselines.
   
   While it is common for PEFT papers to compare subsets across experiments, claiming "outperform[s] 14 popular PEFT baselines" implies broader coverage than the paper delivers. The authors should either include the missing baselines in at least one main experiment, or explicitly scope the claim to the subset actually compared.

### Minor

1. **The mathematical presentation in §3 uses non-standard and ambiguous notation.** Writing the task-specific update as Δ(UΣV^T) and Δ(u_i σ_i v_i^T) is not standard for an additive low-rank update, since the SVD factors of W^(0) are fixed. The subsequent expansion into sums of Δ(u_i σ_i v_i^T) and the approximation that drops ΔW_noise without justification obscure the actual parametrization. The paper would benefit from a cleaner exposition: state directly that W^(0) is replaced by W_world (top m−r singular triplets), and the additive update is parametrized as ηΔU ΔΣ ΔV^T with orthogonality constraints. The conceptual contribution is understandable despite this, but the presentation could be significantly improved.

2. **Hyperparameter r conflates truncation rank and adaptation rank.** In the methodology (§3), r denotes both the number of singular components truncated and the rank of the additive update. The experiments mention tuning a truncation rank k separately (line 275) while setting r=8 for adaptation, but the relationship between the two is never discussed. Whether these ranks should be equal or decoupled is a design choice worth justifying or ablating.

3. **The statistical test used to compute p-values is not specified.** Table 4 reports p-values next to baseline comparisons, and the caption states "Significance is tested at the α=0.05 level," but the test itself (e.g., paired t-test, bootstrap, Wilcoxon) is never described. The p-values are uniformly small across all models and baselines, which raises the question of whether the test is appropriately sensitive. This should be clarified.

4. **Optimization dynamics of the orthogonality penalty are not analyzed.** The paper enforces orthogonality of ΔU and ΔV through a soft penalty (L3) rather than a hard constraint, but never reports how well orthogonality is maintained during training, how sensitive results are to the β and γ hyperparameters, or whether the penalty gradients dominate the task loss gradients. The ablation shows L3 contributes to gains, but it is unclear whether this is because it enforces SVD structure or simply acts as an additional regularizer. A brief analysis of orthogonality drift or sensitivity would strengthen the paper.

5. **The knowledge-aware singular value visualization (Figure 5) is purely qualitative.** The heatmap shows that different layers learn different singular value patterns, which is consistent with the claim of dynamic activation, but this is essentially a sanity check. A more compelling analysis would relate learned singular values to task performance (e.g., by ablating specific layers or singular components) or demonstrate correlation with task-relevant properties.

### Trivial
- The notation for truncation rank switches between r (§3 methodology) and k (line 275 in experiments), causing minor confusion.
- SARA is correctly included in Table 3 (E2E NLG), contrary to the reviewer's claim—CorDA is indeed absent from all tables.

## Nice-to-Haves
- A comparison of training time and memory overhead between KaSA and standard LoRA/PiSSA would help practitioners assess the computational cost of the orthogonality penalty.
- A brief discussion of how the synthetic instruction-following datasets were generated (prompts, filtering, quality control) would improve reproducibility despite the datasets being released.
- The heatmap analysis (Figure 5) could be strengthened by relating singular value patterns to downstream task performance, e.g., via layer-wise or component-wise ablation.

## Removed Points
- **Criticism that the mathematical derivation is "potentially flawed":** The notation Δ(UΣV^T) is indeed non-standard and somewhat ambiguous, but the underlying method is clear: truncate small singular components, learn an SVD-structured update. The presentation is suboptimal but not flawed. This is downgraded to Minor weakness #1 above.
- **Claim that "the orthogonality penalty contributions are relatively small (2–3% absolute)":** 2–3% absolute improvement on NLU benchmarks is actually substantial evidence that the regularization terms are meaningful, not a sign they are weak. This characterization is misleading and is removed.
- **Complaint that "SARA... never appear[s] in any table":** SARA appears in Table 3 (E2E NLG, GPT-2 Medium). This is factually incorrect and removed.
- **General reproducibility complaints about undisclosed hyperparameters:** The paper provides extensive implementation details, learning rate ranges, rank ranges, and loss coefficient ranges for GLUE. The level of detail is standard for the field.
- **Complaint that Figure 5 is purely qualitative/sanity check:** This is a standard use of visualization in ML papers—qualitative sanity checks are acceptable as supporting evidence. Downgraded to Minor weakness #5.

## Novel Insights
The reviews surface an interesting tension: the same SVD design that makes KaSA principled also introduces complexities (rank conflation, soft orthogonality constraints, ambiguous notation) that weaken the paper's clarity. This trade-off between methodological elegance and expository clarity is common in papers that bridge linear algebra techniques with deep learning, but it is particularly acute here because the core innovation *is* the parametrization choice. Additionally, the gap between the paper's strongest evidence (GLUE, commonsense reasoning, MT-Bench) and its weakest (synthetic instruction-following) suggests the method's advantage over FFT may be task-dependent—stronger on discriminative/classification-style tasks and weaker on generative tasks with Mistral 7B. This pattern is worth examining in future work.

## Suggestions
1. **Tone down the FFT comparison.** Replace "consistently outperforms FFT" with precise language: e.g., "KaSA achieves competitive or superior performance to FFT across most tasks while using only 0.24% of the parameters" or "KaSA consistently outperforms FFT on NLU benchmarks and MT-Bench, and matches or exceeds it on most instruction-following tasks."
2. **Clarify §3 notation.** Replace Δ(UΣV^T) and Δ(u_i σ_i v_i^T) with a direct statement: truncate W^(0) to W_world (top m−r triplets), then learn ΔW = η ΔU diag(Δσ) ΔV^T with orthogonal ΔU, ΔV.
3. **Disentangle truncation and adaptation ranks** notationally and provide an ablation or discussion of whether they can/should differ.
4. **Specify the statistical test** used for p-values in Table 4 and justify the small p-values.
5. **Add at least a brief analysis** of orthogonality maintenance during training (e.g., plot ‖ΔU^T ΔU − I‖ over steps) to demonstrate the soft constraint is working.
6. **Include DoRA and CorDA in at least one main experiment** or remove them from the baseline list.

## Score and Decision

The paper presents a solid, well-motivated PEFT method with thorough experiments and consistent improvements over the most relevant baselines (LoRA, PiSSA, MiLoRA). The main flaw is the overclaimed FFT comparison in the abstract, which is contradicted by the paper's own Table 4. This is a fixable problem: the contribution does not depend on outperforming FFT in every setting—it is already strong enough as a PEFT method that often matches or exceeds FFT with a tiny fraction of parameters. The other issues (notation clarity, rank conflation, missing test specification) are addressable in a revision. I recommend acceptance conditioned on addressing the major FFT overclaim and the missing baseline issue.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>