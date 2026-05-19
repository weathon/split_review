Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper diagnoses poor fine-grained visual recognition (FGVR) in MLLMs as a misalignment between visual object representations and category name representations in the LLM embedding space. To address this, the authors propose Finedefics, built on Idefics2, which uses contrastive learning on object-attribute-category triples (with hard negatives) and a two-stage training paradigm (attribute-augmented contrastive learning followed by classification-centered instruction tuning). Experiments on six FGVR datasets show substantial improvements over the base model and other MLLMs.

## Strengths

1. **Evidence-based diagnosis of the root cause**: Section 2 systematically decomposes FGVR underperformance into three capabilities (object information extraction, category knowledge, object-category alignment) and provides empirical evidence — t-SNE visualizations (Figure 2) and linear probing (Table 1) — that the bottleneck is alignment, not information extraction or knowledge. This decomposition goes beyond prior work that attempted improvements without such analysis.

2. **Attribute-augmented contrastive learning improves both alignment and accuracy**: Table 3b shows that adding attribute descriptions to contrastive learning substantially boosts performance (e.g., Caltech-Bird 200: 69.71% vs. 65.23% without attributes). Figure 4c further visualizes that the gap between object and category representations shrinks when attribute descriptions are used, directly confirming the claimed alignment improvement.

3. **Two-stage training paradigm empirically justified**: Table 3c demonstrates that single-stage training (combining contrastive loss with instruction tuning) degrades performance compared to the two-stage paradigm, providing empirical evidence for a non-obvious design choice (e.g., Caltech-Bird 200: 67.63% vs. 69.71%).

4. **Hard negative mining targets the FGVR-specific difficulty**: The contrastive losses (Equations 5–12) incorporate hard negatives mined from similar but incorrect categories via CLIP, directly addressing the challenge that distinguishes FGVR from standard classification where categories are highly visually similar.

5. **Consistent improvements across multiple datasets**: Finedefics shows large and consistent gains over Idefics2 (+10.89% average) and Qwen-VL-Chat (+9.43%) across all six FGVR datasets, and the ablation (Table 3a) confirms that naive fine-tuning on the same data actually hurts performance, suggesting the gains are attributable to the alignment method rather than just exposure to FGVR training data.

## Weaknesses

### Fatal
None.

### Major

1. **Main comparison (Table 2) does not control for training data**. Finedefics is trained on the training sets of the FGVR datasets while the baselines (LLaVA, InstructBLIP, Qwen-VL-Chat, etc.) are evaluated in their original, untuned state. The paper does not state or imply that any baseline was fine-tuned on the same FGVR data. This means the headline "outperforms existing MLLMs" conflates two effects: (a) the benefit of training on the target dataset vs. (b) the benefit of the proposed attribute alignment method. The paper partially mitigates this with Table 3a, which shows that naive fine-tuning of Idefics2 on the same FGVR data *deteriorates* performance, establishing that Finedefics > naive fine-tuning. However, this only covers one base model (Idefics2) and does not control for the full set of baselines in Table 2. The claim that Finedefics generally "outperforms existing MLLMs" requires a controlled comparison against baselines also fine-tuned on the same FGVR training data. *Evidence:* Table 2 lists Finedefics vs. untuned baselines; Section 4.1 states "Several recent MLLMs...are evaluated" without mentioning fine-tuning them. Section 4.3/Table 3a provides the only controlled comparison but only for Idefics2.

### Minor

1. **Root cause analysis is limited in scale and conclusiveness**. The t-SNE visualizations (Figure 2a,d) use only 3 categories from a single dataset (Dog-120), and the linear probing (Table 1) uses only one dataset (Pet-37). The conclusion that category knowledge is "relatively sufficient" is based on probing LLM-generated *descriptions* (Table 1b), which measures description quality rather than the LLM's *internal category name embeddings* directly — though the paper separately discusses category name discriminability via t-SNE (Figure 2b,e). The analysis is a reasonable motivation but is presented in the abstract as definitive ("position of the root cause"), which overstates its rigor. *Evidence:* Section 2.1 uses Dog-120 with 3 categories; Section 2.2 uses Pet-37 only.

2. **Asymmetry in hard negative usage across loss terms is not discussed**. L_OAC^{hn} (Equation 6) averages L_OA^{hn} (object→attribute with hard negatives in the attribute dimension) and L_AO (attribute→object *without* hard negatives). This asymmetry is not explained or justified. Similarly, L_ACC^{hn} averages L_AC^{hn} and L_CA^{hn} (both with hard negatives), while CCC loss (Equation 11) uses only hard negatives. Given the many loss terms, the paper would benefit from explaining why certain directions use hard negatives and others do not. *Evidence:* Equations (5)–(7), (8)–(10), (11).

3. **No statistical significance or variance reported**. The paper states "All seeds are fixed across the training procedures for fairness" — meaning a single fixed seed with no repeated runs. For a comparison where some margins are small (e.g., +1.1% on Car-196 over Pali-Gemma), variance estimates are necessary to assess whether differences are meaningful. *Evidence:* Section 4.1 (Training Settings).

4. **Attribute construction pipeline details are underspecified for reproducibility**. The prompts for attribute discovery, extraction, and summarization are referenced to (Liu et al., 2024c) rather than provided. The specific model versions (e.g., which GPT-4 variant, which BLIP-2/LLaVA checkpoint) are not specified. While referencing prior work is acceptable, the exact prompts and model configurations should be included for full reproducibility. *Evidence:* Section 3.1 repeatedly references prompts in (Liu et al., 2024c) (e.g., "$P^{\mathrm{dis}}$ is the How-to LLM-prompt in (Liu et al., 2024c)").

5. **Missing discussion of limitations beyond continual learning**. The Future Work section only discusses challenges in continual learning of new categories, but does not acknowledge: (a) dependency on external models (GPT-4, BLIP-2, LLaVA) for attribute construction, which may introduce noise, hallucination, and computational cost; (b) evaluation limited to six natural-image datasets, leaving out domains such as medical, synthetic, or satellite imagery; (c) whether the method improves zero-shot FGVR or only fine-tuned performance. *Evidence:* Section 6 (Conclusion and Future Work).

### Trivial
None.

## Nice-to-Haves
- **Ablate the quality of attribute descriptions**: The current ablation (Table 3b) compares contrastive learning with vs. without attribute descriptions. A stronger isolation would compare GPT-4-generated descriptions against simpler alternatives (e.g., "This is a {category}" or automatically extracted attribute lists from smaller models) to test whether the complex multi-model pipeline is necessary.
- **Ablate individual loss components**: The method has four loss terms (OAC, ACC, CCC, attribute generation). Ablating each would clarify which components drive the improvement.
- **Quantify alignment directly**: Figure 4 shows t-SNE visualizations; reporting a quantitative alignment metric (e.g., average cosine similarity between matched object-category pairs) would strengthen the alignment claim.
- **Fine-tune additional baselines on the same FGVR data**: Extending the controlled comparison in Table 3a to one or two additional base models (e.g., Qwen-VL-Chat, LLaVA) would substantially strengthen the evaluation.
- **Test transfer to downstream tasks**: The motivation mentions object-centric VQA and reasoning; showing that improved FGVR transfers to such tasks would broaden the contribution.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Section 2.2 probing on descriptions confounds description quality with category name discriminability"**: The paper actually discusses both separately — Table 1b probes description features (showing knowledge reserve), while Figure 2b/e shows category name (non-)discriminability via t-SNE. The paper does not conflate the two. *Justification:* The criticism misunderstands the paper's two-part argument.

2. **"Related work is generic"**: This is a one-size-fits-all criticism without a specific actionable observation. *Justification:* Generic criticism, not a specific identified problem.

3. **"Strengthening the Paper on Its Own Terms" items 4 and 5** (quantitative alignment measure, impact on advanced tasks): These are additive suggestions, not weaknesses. *Justification:* Nice-to-have extensions, not flaws in the existing paper.

4. **"No comparison with traditional FGVR methods"**: The paper's scope is improving FGVR *for MLLMs*, not competing with traditional FGVR classifiers. *Justification:* Scope creep — the paper evaluates against other MLLMs, which is appropriate for its stated contribution.

5. **"No analysis of where Finedefics fails (per-category analysis)"**: This is a useful addition but not a missing requirement for a paper of this scope. *Justification:* Nice-to-have, not a core weakness.

## Novel Insights

The structural pattern that emerges across the reviews is that the paper's empirical strengths lie more in its carefully controlled ablations (Table 3a–c, which isolate the method from naive fine-tuning, attribute ablation, and two-stage necessity) than in its main comparison table (Table 2, which is confounded by training data). This creates an unusual situation where the paper's internal evidence is stronger than its external evidence. The reviewers converge on the method being sound and the ablations being informative, but diverge on how much weight to give the uncontrolled main comparison. The deepest insight from combining the reviews is that the paper would be most convincing if it reframed its central claim from "outperforms existing MLLMs" (which requires a controlled comparison) to "improves FGVR for Idefics2 through attribute-augmented alignment" (which its ablations already support well).

## Suggestions
1. **Add controlled baselines**: Fine-tune 2–3 base MLLMs (Qwen-VL-Chat, LLaVA) on the same FGVR training data (without attribute alignment) and compare against Finedefics. This is the single most impactful fix.
2. **Provide exact prompts and model versions** used in the attribute construction pipeline in the appendix or supplement.
3. **Report variance across seeds** or at minimum state whether results are stable across multiple runs.
4. **Explain the asymmetry in hard negative usage** across the contrastive loss terms (L_OA^{hn} vs. L_AO) to clarify design rationale.
5. **Tone down the conclusiveness of the root cause analysis** claims in the abstract and introduction — present it as motivated diagnosis rather than definitive proof.

## Score and Decision

This paper identifies a genuine problem, proposes a novel and well-motivated solution (attribute-augmented contrastive learning with hard negatives), provides informative ablations, and demonstrates consistent improvements. The main weakness — the uncontrolled comparison in Table 2 — is significant but partially mitigated by the controlled ablation in Table 3a. The remaining issues (reproducibility details, variance reporting, loss asymmetry discussion) are addressable. The core contribution is solid and the empirical evidence, when viewed through the ablations, supports the method's effectiveness.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>