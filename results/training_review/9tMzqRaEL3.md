Now I have all the information needed to write my consolidated review. Let me carefully verify each claim.

**Verification of key reviewer claims against the paper:**

1. **12.3% claim**: Paper says "achieves a $12.3\%$ accuracy improvement" (line 24) and "showing an improvement of $12\%$ over baseline methods" (line 202). No computation method is given. The table is embedded as an image, so I cannot directly verify the reviewer's computed averages of 39.5 vs 41.1, but the paper's text acknowledges mixed results (worse on CaseHOLD and Plato - line 171). The 12.3% claim is indeed unexplained. **KEEP (verified)**

2. **Routing baseline as oracle**: The paper's "Domain fine-tuned" baseline uses ground-truth domain labels to map to the best fine-tuned model (line 154-157). The paper does acknowledge this mapping. This is a reasonable reference but the reviewer's characterization as "conceptually flawed" is too strong — the paper actually discusses why the hidden states classifier might beat it (lines 169-170). **WEAKEN to minor**

3. **No clustering metrics**: Search confirms "silhouette," "NMI," and "clustering metric" do not appear in the paper. The clustering claims rest entirely on visual inspection of Figures 1-3. **KEEP (verified)**

4. **Meng et al. ignoring claim**: Paper cites Meng et al. (2022, 2023, 2024) multiple times (lines 12, 33, 144). The reviewer's claim that the paper ignores generation-focused works by Meng et al. is **factually wrong**. **REMOVE**

5. **DeBERTa methodology**: Paper acknowledges DeBERTa's bidirectional encoding (line 122) and discusses why the same procedure may yield different patterns. The reviewer's claim that this is "methodologically unsound" is overstated given the paper's own caveats. **WEAKEN**

6. **Semantic Layer not explained**: The paper describes the Semantic Layer baseline (line 92). The reviewer's claim that "critical details are missing" is not entirely accurate; the description gives configuration details. **REMOVE this specific sub-point**

Let me now write the consolidated review.

---

**Note to self**: The "Emotional" fine-tuning domain (line 154) is odd — the routing domains are Maths, Biomedical, Law, Humanities, but one fine-tuned model is on "Emotional" data. This is a genuine inconsistency worth noting, though the harsh critic didn't catch it.

---

Now let me write the review.Now I have thoroughly verified all claims. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether LLMs encode domain-specific information in their hidden states (mean/std of activations across layers). The authors show qualitative evidence that autoregressive LLMs (Gemma, Phi, Llama2, Mistral) exhibit clustering of hidden-state traces by domain, and leverage this signal for model selection: an MLP trained on hidden states routes queries to domain-specific fine-tuned models, outperforming semantic similarity and encoder-based routing on several held-out tasks.

## Strengths

- **Consistent domain clustering across diverse LLM architectures**: The paper demonstrates that hidden-state traces (standard deviation across layers) visibly separate by domain for four different autoregressive LLMs (Gemma-2B, Phi-3-mini-3.8B, Llama2-7B, Mistral-7B), as shown in Figure 2. This clustering persists even when samples from non-MMLU datasets are introduced, suggesting the effect is not merely due to dataset-specific formatting. The use of multiple model families (trained by different organizations with different recipes) strengthens the generalizability claim.

- **Extension to open-ended generative tasks**: Unlike prior work that focused on closed-ended probing, the paper evaluates routing on GSM8K and MATH (free-form reasoning). The LLM Hidden States Classifier shows large absolute gains on these tasks (e.g., ~17 points on GSM8K), demonstrating that the approach is not limited to multiple-choice classification.

- **Systematic layer-depth ablation**: Figure 4 analyzes how routing performance varies as a function of the number of layers fed to the MLP classifier, identifying layer 26 as a turning point. This provides practical guidance for accuracy-efficiency tradeoffs and corroborates the finding that deeper layers carry more domain-specific information.

- **Comparison against multiple baselines**: The paper includes semantic routing (MiniLM embeddings), a fine-tuned DeBERTa classifier, and an LLM Sequence Classifier (full prefill+generation), providing a reasonable reference frame for the hidden-states approach.

## Weaknesses

### Fatal
None.

### Major

- **The headline "12.3% accuracy improvement" is unexplained and appears inconsistent with the reported data.** The abstract claims a "12.3% accuracy improvement over domain fine-tuned models" (line 24), and Section 7 states "an improvement of 12%" (line 202). The paper never defines whether this is an absolute or relative improvement, which tasks it is averaged over, or how it is computed. The routing results in Table 2 show improvements on GSM8K, MATH, and MEDMCQA but *decreases* on CaseHOLD and Plato, making an overall 12.3% figure puzzling without further clarification. This undermines the paper's central quantitative claim. The authors must either explain the computation or correct the number.

### Minor

- **Domain clustering evidence is purely qualitative.** The paper's central claim—that LLM hidden states "capture fundamental domain characteristics" and exhibit "latent domain-related trajectories"—rests entirely on visual inspection of Figures 1–3. No clustering metrics (silhouette score, NMI, domain classification accuracy on raw hidden states) are reported, and no negative controls (e.g., random domain labels) are conducted. While the visual patterns are suggestive, the paper overstates the certainty of this finding. The routing experiments provide indirect quantitative support, but the core interpretability claim needs direct quantification.

- **The "Domain fine-tuned" baseline uses ground-truth domain labels, while the hidden-states classifier does not.** The baseline maps each query to a fine-tuned model based on its true domain label (Maths → Phi-3-MATHS, etc.). This is an oracle that has access to information the hidden-states classifier must infer. The paper discusses this and offers plausible explanations for when the hidden-states classifier beats the oracle (lines 169–170), but additional baselines would contextualize the results: e.g., a single best model across all data, random routing, or a text-based domain classifier (using the same MLP on DeBERTa embeddings) trained on the same 4,000 samples. The comparison as-is is not flawed, but it would be strengthened by these references.

- **The DeBERTa comparison uses an architecture-mismatched procedure.** The paper applies the same per-layer mean/std extraction to DeBERTa, a bidirectional encoder with fundamentally different layer semantics. Finding "no clear pattern" in DeBERTa (line 122) may partly reflect the inappropriateness of the procedure rather than a genuine absence of domain encoding. A fairer comparison would use DeBERTa's sequence-level representations (e.g., CLS token or pooled output) as features. The paper acknowledges architectural differences, but the conclusion that autoregressive models are "better suited for capturing domain-related trajectories" (line 171) would be stronger with an architecture-appropriate comparison.

- **Fine-tuning domains mismatch routing domains.** The fine-tuned models are described as trained on "Emotional, Mathematical thinking and Medical Data" (line 154), but the routing taxonomy uses "Maths, Biomedical, Law, Humanities." It is unclear what "Emotional" corresponds to in this taxonomy, or how "Law and Humanities" were handled (they use the pretrained model). This inconsistency is not discussed.

### Trivial
None.

## Nice-to-Haves

- Report standard deviations or confidence intervals for the routing accuracy numbers in Table 2. Single-run evaluations make it impossible to assess whether the observed differences are statistically significant.
- Add a confusion matrix for the MLP domain classifier to reveal which domains are most confusable.
- Test on larger models (e.g., 13B, 70B) to assess scalability, as the paper acknowledges this limitation.
- Add example queries from different domains with their hidden-state traces superimposed to illustrate what "latent domain-related trajectories" look like at the sample level.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Ignores works like Meng et al. that also study generation"** — Factually wrong. The paper cites Meng et al. (2022, 2023, 2024) in multiple locations (lines 12, 33, 144). This criticism is based on a misreading and is removed.
- **"Semantic Layer baseline not explained"** — The paper provides configuration details (line 92): four routes, 1,000 utterances each, MiniLM encoder with 0.5 threshold. While concise, this is adequate for reproduction given the cited reference.
- **"Contrast with prior work is overstated"** — Subjective opinion without specific evidence; not a concrete weakness.
- **"The paper's motivation conflates two distinct goals"** — The two goals (understanding domain representations and using them for routing) are connected through the experimental pipeline. This is feature, not a bug.

## Novel Insights

None beyond the paper's own contributions. The reviews highlight a tension that the paper itself does not fully address: the routing results show that hidden-state representations can sometimes outperform domain-label-based routing, which suggests that the hidden states capture information that is *more nuanced* than domain identity. However, the paper frames its contribution primarily as confirming that hidden states encode "domain-specific knowledge" — a framing that undersells the more interesting possibility that they encode something task-relevant that cuts across domain boundaries. Exploring *when* and *why* the hidden-states classifier beats the oracle would be more insightful than further confirming the clustering observation.

## Suggestions

1. **Clarify or correct the 12.3% claim.** State explicitly whether it is an absolute or relative improvement, which datasets it covers, and show the computation. If it is not representative of the full evaluation, replace it with a more accurate summary statistic (e.g., average improvement across tasks where the method helps, or weighted average).

2. **Add quantitative clustering metrics.** Report silhouette scores, domain classification accuracy via k-NN on raw hidden states, or similar measures for Figures 1–3. Include a negative control (randomly permuted domain labels) to demonstrate that the clustering is not an artifact of the visualization.

3. **Add a "single best model" baseline** to the routing comparison (i.e., the single Phi-3 checkpoint with the highest average accuracy across all held-out data). This would help disentangle whether the hidden-states classifier's advantage comes from smart routing or from simply avoiding the worst fine-tuned model for each task.

4. **Extend the fine-tuning descriptions** to clarify the "Emotional" fine-tuning domain and how it maps to the four routing domains (Maths, Biomedical, Law, Humanities).

## Score and Decision

This paper tackles a timely and relevant question—whether LLM internal representations encode domain information useful for model routing—and provides a reasonable experimental pipeline across multiple architectures and task types. However, the paper has a significant presentation issue: the headline accuracy improvement (12.3%) is not explained and appears inconsistent with the mixed results reported in Table 2 (improvements on some tasks, regressions on others). This makes the central quantitative claim unverifiable. The qualitative clustering evidence, while suggestive, lacks the quantification needed to fully support the interpretability claims. These issues are addressable with revisions but weaken the paper in its current form.

**Originality**: Good — using hidden-state traces for model routing is a reasonable extension of prior probing work to generative settings.  
**Importance**: Moderate — domain-aware routing is practically relevant, but the paper's contribution is incremental.  
**Claims**: Partially supported — the routing results show promise, but the 12.3% headline is unexplained and the clustering claims lack quantification.  
**Soundness**: Adequate — the experimental design is reasonable but missing some baselines and statistical rigor.  
**Clarity**: OK — the paper is generally readable but the 12.3% computation is opaque.  
**Value to community**: Moderate — the finding that hidden-state-based routing can outperform label-based routing is interesting and could inspire follow-up work.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>