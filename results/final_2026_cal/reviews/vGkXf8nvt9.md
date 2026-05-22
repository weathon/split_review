## Summary

This paper proposes **Forget-to-Focus (F2F)**, a two-stage protocol that first performs machine unlearning (via gradient ascent on a "forget set" of general-domain data, optionally combined with gradient descent on a "retain set" for stability) followed by standard fine-tuning on a domain-specific dataset. The central idea is that actively suppressing irrelevant pretraining knowledge before adaptation can mitigate negative transfer and improve downstream specialization. Experiments span coding (HumanEval, MBPP), medical (PubMedQA, MedMCQA), and math (Hendrycks-MATH, GSM8K) domains, across models from 0.6B to 72B parameters (Qwen, LLaMA, Gemma), and include representational analyses (CKA, SVCCA). The paper reports consistent gains over standard fine-tuning and parameter-efficient baselines.

## Strengths

- **Novel and well-motivated framing of unlearning as a mechanism for domain specialization, not privacy.** The core idea — that selectively forgetting irrelevant pretraining knowledge can create a cleaner optimization landscape for fine-tuning — is original and timely. The paper convincingly argues that not all pretraining knowledge is useful for downstream tasks, and the proposed two-stage pipeline is a clean way to test this hypothesis.

- **Broad and systematic empirical evaluation.** Experiments span five model families (Qwen-0.6B, Gemma-2B, LLaMA-8B/13B, Qwen-72B), three domains (code, medical, math), multiple unlearning variants (GA+GD, GA-only, GA+KL, NPO), and multiple fine-tuning methods (SFT, LoRA, DAPT, CurlLoRA). This breadth provides reasonable evidence that the F2F benefit is not an artifact of a single model or domain. For example, on Qwen-0.6B, HumanEval pass@1 improves from 31.71 (SFT) to 42.07 (F2F+SFT); on Qwen-72B, from 71.12 to 78.50.

- **Representation-level analysis (CKA and SVCCA)** provides mechanistic insight beyond surface accuracy. The observation that F2F induces more pronounced representational drift than standard fine-tuning, and that this drift correlates with downstream gains, adds a useful interpretability dimension.

- **Systematic ablation of forget-set quality** across three constructions (BC-Select, BC-Mixed, BC-Cosine) shows that the composition of the forget set is a controllable and impactful design choice, with curated sets (BC-Select) consistently outperforming mixed sets.

## Weaknesses

### Major

1. **Inconsistency between Table 2 and Table 3 undermines experimental trustworthiness.**  
   For LLaMA 8B-Instruct, Table 2 reports SFT (standard fine-tuning without unlearning) as 45.31 (PubMedQA) and 13.06 (MedMCQA). Table 3 reports the same baseline condition — standard fine-tuning without unlearning, labeled "(3) + Tuning" under BC-Cosine — as 85.31 and 64.20. These are 40-point and 50-point discrepancies, respectively, on the same benchmarks. For Qwen 0.6B, Table 2 SFT gives MedMCQA 11.8, whereas Table 3's BC-Select F2F result (which should match if Table 2 shows F2F variants) gives MedMCQA 45.31. The paper provides no explanation for these differences. Whether this is a mislabeling, a data-split mismatch, or a genuine reporting error, the numbers cannot be reconciled as presented, and the experimental record is not trustworthy until clarified.

2. **Retain-set confound prevents isolation of the forgetting effect.**  
   The paper states that "the retain set is a small subset of the fine-tuning data" (Section 3.3). During the unlearning phase, the model performs gradient descent on this retain set — i.e., it receives *additional exposure* to target-domain examples before fine-tuning begins. The observed gains could therefore arise from this warm-up effect rather than from forgetting per se. To isolate the role of forgetting, a control experiment performing *only gradient descent* on the same retain set (without gradient ascent on the forget set) is needed. Without this control, the central causal claim — that *forgetting* itself drives improvement — is not properly supported. This is a standard and expected confound in this type of design, not a fatal flaw, but it must be addressed.

### Minor

3. **No variance or significance estimates.** All reported numbers in Tables 1–3 are single-shot accuracies with no error bars, confidence intervals, or multiple-run standard deviations. Given the small forget-set sizes (100–1000 samples) and the known sensitivity of gradient ascent to initialization and learning rate, observed improvements (e.g., +10 points on HumanEval) could fall within noise ranges. This limits the reader's ability to assess robustness.

4. **Theoretical analysis (Proposition and Corollary in Section 2) is ornamental.** The analysis assumes a convex linear surrogate with orthogonal decompositions, which the paper acknowledges does not apply to non-convex LLM optimization. The bounds are not used to derive empirically testable predictions, and they do not guide any design choices in the experiments. This section does not add explanatory value to the empirical results.

5. **No evaluation on general-purpose benchmarks.** The paper focuses entirely on domain-specific metrics and does not report whether F2F degrades general capabilities (e.g., MMLU, HellaSwag, or other broad reasoning tasks). The appendix is mentioned as containing such analysis but was stripped during the review process. Given that the method deliberately removes pretraining knowledge, the risk of collateral damage to general competence should be explicitly quantified.

### Trivial

- Figure 3 (unlearning variants comparison) is described only via the figure caption's fallback text; the y-axis label is not clearly stated in the main text.
- The "BC-Select" forget set curation ("manually excluded texts overlapping with the target domain") is described only qualitatively; the overlap detection procedure is not specified.

## Nice-to-Haves

- Adding the suggested control experiment (GD-only on the retain set → fine-tune) would cleanly separate the warm-up confound from the forgetting effect.
- Reporting at least 3 runs with standard deviations for the main comparisons would substantially strengthen the paper.
- A quantitative link between the CKA/SVCCA representational drift measures and downstream accuracy (e.g., a scatter plot or correlation) would make the representation analysis more than an intriguing observation.

## Removed Points

These points were raised by the reviewers but are removed or demoted for the reasons stated:

- *"No evaluation on general benchmarks"*: The paper states this is in Appendix A, which was stripped by the parser. This is a parser artifact, not an author omission. Moved to Minor as a fair request for the main paper.
- *"The first comprehensive study claim ignores prior work"*: The paper cites Chen et al. (2023a) and the claim is qualified ("systematically study across multiple domains and model scales"). The criticism is somewhat valid but minor and scope-dependent.
- *"Missing related works"*: Cannot be verified without external sources. Removed per policy.
- *"t-SNE only for mixed set, not medical/math"*: This is a genuinely secondary visualization request; the coding-domain t-SNE suffices to illustrate the concept.
- *"BookCorpus is odd as a general source"*: The choice is reasonable (common benchmark), and the ablation across three forget-set constructions addresses concerns about sensitivity to the specific source.
- *"CurlLoRA is from a non-peer-reviewed source"*: Acceptable as a practical baseline; does not invalidate results.
- *"Gemma-2B failure case should be discussed more honestly"*: The paper does discuss it (Section 4.1 point 3). The discussion is adequate.
- *"No comparison to warm-up fine-tuning"*: This is the same as the retain-set confound (Weakness 2), already included above.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from the review process is that the representational analyses (CKA, SVCCA) — which are often used to verify that forgetting has occurred in privacy-focused unlearning — can serve a forward-looking role in *measuring preparedness for downstream learning*. The observation that F2F consistently pushes representations further from the base model than standard fine-tuning does, and that this correlates with improved accuracy, suggests that representation-level distances could be developed into a *predictive* signal for whether a given unlearning intervention will benefit fine-tuning. This reframes the role of representation analysis from post-hoc verification to a proactive optimization signal.

## Suggestions

1. **Resolve the Table 2 / Table 3 discrepancy immediately.** Clarify whether Table 2 shows baseline fine-tuning (no unlearning) or F2F results. If the former, ensure numbers match Table 3's baseline rows. If the latter, ensure the column labels and conditions are clearly specified. Provide a corrected table or an explanation of why the numbers differ.
2. **Add the proposed GD-only control experiment.** Run the unlearning phase with *only gradient descent on the retain set* (remove the GA term) followed by fine-tuning, and compare to the full F2F protocol. This is the cleanest way to demonstrate that forgetting — not just data exposure — drives the improvement.
3. **Add variance estimates** for the main comparisons (at least 3 seeds for the core claims in Tables 1 and 3).
4. **Include general-benchmark results** (e.g., MMLU, HellaSwag, or an appropriate subset) in the main paper to assess whether F2F preserves broad linguistic competence.

## Score and Decision

**Calibration report.** All anchors retrieved across rounds:

*Round 1 — Bracketing:*
| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| 6zcXThQIoR | 1.33 | R1 | Privacy unlearning paper; much narrower scope and lower quality than F2F |
| 7bW5ECLy8q | 2.50 | R1 | Unlearning method paper; similar topic area but weaker on experiments |
| qZPIyCf5ke | 3.33 | R1 | JensUn unlearning; strong on utility-preservation but different goal |
| 4LcAY5Q3z5 | 2.50 | R1 | UniErase; similar topic area, lower quality |
| 7cEMkTu7Lf | 4.00 | R1 | Unlearning reversibility; representation analysis focus, similar CKA methods |
| iKqQGEOeej | 5.50 | R1 | Memorize-to-Forget; different unlearning paradigm, similar topic, mixed reviews |
| BcjZCertEk | 4.67 | R1 | Learning-time encoding for unlearning; controlled experiments, similar quality level |
| jROUUKq51K | 4.00 | R1 | MaGA unlearning; narrower scope |
| VKGTGGcwl6 | 8.00 | R1 | Unrelated topic (multi-turn conversation) |
| oBXfPyi47m | 8.00 | R1 | Unrelated topic (RL) |
| qOyF214xmg | 8.00 | R1 | Unrelated topic (transducing LMs) |
| DM0Y0oL33T | 8.00 | R1 | Unrelated topic (multimodal verification) |

*Round 1 bracket:* 4.0–6.0 (based on topically similar middle-band anchors).

*Round 2 — Narrowing:*
| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| 7SnsUnuBEB | 4.50 | R2 | Domain-specialization fine-tuning (DBA); similar topic, comparable quality, cleaner experiments |
| qd9fA4LzVN | 4.50 | R2 | Label smoothing for GA unlearning; narrower focus |
| ru93xpQFi1 | 5.00 | R2 | SFT domain specialization (TALR); similar topic, Accept Poster, cleaner experiments, less novelty |
| cvztBvlglK | 6.50 | R2 | Unrelated (limited memory LMs) |
| kpjb0kbaW6 | 5.50 | R2 | ERASER subspace unlearning; strong method but Reject decision |
| Qi1rZa4zzl | 5.50 | R2 | Safety unlearning for VLMs; different modality |
| uMq2N8hJK4 | 5.50 | R2 | Knowledge localization for capability removal; different approach |
| K4pQPqibC3 | 4.00 | R2 | Jailbreak unlearning ripple effect; different application |

*Final score determination:* The F2F paper is more novel than the 5.00 "SFT Doesn't Always Hurt" anchor (which received Accept Poster) but has messier empirical reporting. Compared to the 5.50 ERASER anchor (Reject), F2F has broader cross-domain validation but a clear reporting inconsistency. I place it at **4.5**, reflecting that the core idea is strong and the experimental scope is broad, but the Table 2/Table 3 discrepancy and the unresolved retain-set confound are significant weaknesses that must be resolved before the contribution can be fully assessed.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>