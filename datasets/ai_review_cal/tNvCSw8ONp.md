- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper investigates selection bias in LLMs answering multiple-choice questions and proposes two mitigation methods: **Bias Node Pruning (BNP)**, which removes parameters from the final linear layer that contribute to bias, and **Auxiliary Option Injection (AOI)**, a simple prompting tactic that adds an "I don't know" option. The paper also introduces **Choice Kullback-Leibler Divergence (CKLD)** as a bias evaluation metric that addresses insensitivity to label imbalance. Experiments on three datasets (ARC-Challenge, MMLU-Redux, CommonsenseQA) across three 7-8B models show that both methods improve accuracy and can be combined with existing techniques like CoT, ICL, and DoLa.

**Important note on paper availability:** The extracted text is heavily truncated — the method details, full experiments, result tables, and analysis sections are all in unresolved `\input{}` commands. This review evaluates only what is present (abstract, introduction, problem statement overview, methods overview, related works, conclusion). Claims about content in the truncated sections cannot be verified from the extracted text alone.

---

## Strengths

1. **First parameter-level debiasing approach for selection bias.** Prior work on selection bias modifies input format or calibrates output probabilities (lines 27, 133). BNP directly modifies model parameters by pruning nodes in the final linear layer, a genuinely different intervention level. The paper explicitly contrasts this with output calibration methods (line 27: "no embedding or parameter-level investigation has been performed").

2. **BNP is remarkably efficient.** The paper reports dropping as few as 32 out of 4096 nodes in the final layer significantly reduces selection bias (line 33). This suggests the bias signal is concentrated in a small number of parameters, which is a non-trivial finding.

3. **Black-box applicability of AOI.** AOI requires only input modification and works with black-box models where parameter access is unavailable (lines 34–35). This complements BNP (which requires white-box access) and broadens practical applicability.

4. **Demonstrated compatibility with existing methods.** The paper explicitly shows BNP and AOI can be combined with Chain-of-Thought, In-Context Learning, and Decoding by Contrasting Layers to further improve performance (line 45, line 149).

5. **Clear problem framing and motivation.** The paper provides a well-structured definition of selection bias, distinguishes its approach from prior input/output-level work, and motivates why parameter-level investigation is needed.

---

## Weaknesses

### Fatal

None.

### Major

1. **Framing of BNP as "internal representation" investigation is somewhat overstated.** The paper repeatedly claims it "investigates the model's internal representation" and scrutinizes "embedding-level discrepancies" (lines 6, 28, 30, 148). However, BNP only prunes nodes in the **final linear layer** — the layer that directly produces logits. While this is genuinely parameter-level intervention (distinct from prior output-calibration methods), calling it an investigation of "internal representation" overstates what pruning the output projection layer reveals about the model's deeper internal computations. The paper would be more accurate to frame BNP as identifying and removing parameter-level sources of bias at the output stage, without the "internal representation" rhetoric. That said, this is a framing issue, not a methodological one — the method itself is sound and distinct from prior work.

2. **Two different performance improvement numbers without sufficient contextualization.** The contributions list states "improve accuracy by up to 24.9%" (line 51), while the conclusion states "improve the base performance of Llama-3 by up to 33.8% on the ARC-Challenge dataset" (line 149). It appears these refer to different experimental conditions (24.9% for BNP+AOI; 33.8% when combined with other methods), but the paper does not explicitly clarify this distinction in either location, which invites confusion.

### Minor

1. **Limited model scale.** Experiments use three models (Llama-3-8B, Mistral-7B, Bloomz-7b1), all in the 7-8B parameter range. While this is a reasonable scope, the paper's claims of "broad applicability" would be strengthened by at least one larger model (e.g., 70B) or a model from a different family (e.g., Qwen, Gemma) to demonstrate that the localization of bias in the final layer's nodes generalizes across scales and architectures.

2. **AOI's novelty is modest.** The paper itself frames AOI as "a simple prompting tactic" and acknowledges that survey science has studied "I don't know" options (lines 139–141). This is appropriate and honest framing. However, the paper should not be evaluated as if AOI is a major technical contribution — its value is as a practical, lightweight method, particularly for black-box settings.

3. **CKLD cannot be evaluated from the extracted text.** The definition and formalization of CKLD are in the truncated `\input{}` sections. While this is a parser issue rather than an author error, it means the reader (and this review) cannot verify whether CKLD actually addresses the claimed limitations of RStd/RSD.

4. **BNP sample selection details are unclear in the available text.** The paper mentions using "a separate set of out-of-bag samples" (line 98) to compute average bias vectors, but the number of samples required and the selection procedure are not specified in the extracted portion. (These details may exist in the truncated sections.)

### Trivial

None.

---

## Nice-to-Haves

- An ablation pruning nodes from intermediate (non-final) layers would help substantiate the claim that bias is specifically concentrated at the output layer.
- A direct comparison between BNP and logit-adjustment calibration methods (e.g., Zheng et al. 2024) would sharpen the distinction between parameter-level and output-level approaches.
- A per-category analysis showing that BNP does not degrade performance on unbiased questions would address a natural concern about pruning.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic's claim that BNP is "output-level intervention" and "not fundamentally different from existing calibration methods."** REMOVED — This is factually incorrect. The paper explicitly contrasts BNP with output-calibration methods (lines 27, 133), and pruning parameters from the final linear layer is a parameter-level modification, not a post-hoc output adjustment. Prior calibration methods (Zheng et al., Reif et al.) adjust output probabilities without modifying model weights. BNP modifies the model itself.
- **Harsh Critic's claim of "inconsistent performance claims" as a structural issue.** REMOVED — The 24.9% (contributions list) and 33.8% (conclusion, line 149) refer to different experimental conditions: 33.8% explicitly states "BNP and AOI work alongside other debiasing/decoding methods." This is not inconsistency but different reporting contexts.
- **Harsh Critic's concern about BNP sample selection and data leakage.** REMOVED — The paper explicitly states "a separate set of out-of-bag samples" (line 98), indicating the pruning samples are disjoint from the test set.
- **Strength Finder's point about "in-depth mechanism analysis."** This may be valid but refers to truncated sections and cannot be verified from the available text. Moved here for caution.
- **Harsh Critic's missing related works criticism.** REMOVED per instructions: the reviewer lacks external sources to confirm existence of missing references.
- **Strength Finder's generic/superficial strengths removed:** "The problem is important and well-motivated" (generic), "The paper is clearly written" (formatting/superficial). These add no specific evidence.

---

## Novel Insights

The most interesting observation from the synthesis of the two reviews is the tension between the paper's framing and its actual intervention. Both reviewers agree that trimming reliance on the "internal representation" framing would make the paper stronger, but neither reviewer elaborated on what would be gained: the paper's genuine contribution — demonstrating that selection bias can be localized to and corrected by modifying a very small number of parameters (32/4096) in the final layer — is actually *more* striking if framed straightforwardly as parameter-level bias localization rather than as "internal representation investigation." The 32/4096 ratio is the paper's most compelling quantitative finding, but it is buried under the broader framing rather than elevated as the headline result. The harsh critic's error was to dismiss this as "output-level intervention," missing that modifying parameters (even at the final layer) is categorically different from post-hoc output calibration and that the sparsity of the fix (32 nodes) is itself a non-trivial discovery about where bias concentrates.

---

## Suggestions

1. **Reframe the contribution more precisely.** Replace "investigates the model's internal representation of selection bias" with language about identifying and pruning parameter-level bias sources at the output layer. This would be more accurate and actually strengthen the paper by avoiding over-claim.
2. **Clarify the 24.9% vs 33.8% numbers.** Add a short sentence in the contributions section noting that the 33.8% figure includes gains from combining with other methods.
3. **Add at least one larger model (e.g., 70B scale) or a different architecture family** to strengthen generality claims.
4. **Include a direct comparison experiment** between BNP and a representative output-calibration method (e.g., Zheng et al. 2024) to make the distinction concrete.

---
