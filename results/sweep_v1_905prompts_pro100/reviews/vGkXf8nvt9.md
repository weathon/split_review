Now I have a clear picture of the calibration landscape. Let me finalize the review.

**Round 1 bracket:** The paper falls between the weak domain-adaptation papers (~3.0–3.5) and the strong theoretical+empirical papers (~8.0–9.0). Compared to UnSTAR (5.50) and Deep Unlearning (5.33), this paper has broader evaluation and a more original framing. Compared to the 8.0+ papers, it lacks methodological rigor. **Bracket: 5.5–7.0.**

**Round 2 narrowing:** Compared to "Training Mice" (6.00, accepted), this paper has a more novel idea and broader model coverage, but more significant methodological gaps (missing key baseline, no variance). Compared to "Dissecting learning and forgetting" (5.75, accepted), both have interesting empirical insights but this paper's missing controls are more damaging to its central claims. Compared to "Lawma" (7.00, accepted), this paper lacks the same level of evaluation rigor (260 tasks vs. ~10 benchmarks across 3 domains, but Lawma's evaluation is intrinsically more thorough). **Final score: 5.5 — Reject.**

The fatal gap is the missing retain-only baseline, which prevents the paper from conclusively demonstrating that *forgetting* (rather than just additional domain-relevant training) causes the improvements. Combined with no variance reporting and an unsubstantiated calibration claim, the paper overstates its conclusions.

---

## Summary

This paper proposes Forget-to-Focus (F2F), a two-stage protocol that first applies machine unlearning on a general-domain "forget set" (with an optional retain set for stability) before fine-tuning on a target domain. The central claim is that removing interfering pre-training priors via unlearning causes more effective domain specialization. The paper evaluates F2F across 5 models (0.6B–72B), 3 domains (coding, medical, math), and against several baselines (SFT, DAPT, LoRA, CurlLoRA), consistently showing gains. Representation analysis via CKA and SVCCA provides additional evidence of representational change.

## Strengths

- **Novel framing of unlearning for domain specialization.** Rather than using unlearning for privacy, the paper repurposes it as a deliberate preparatory stage to enhance fine-tuning — a genuinely fresh perspective supported by the consistent empirical trend that F2F+SFT outperforms standard SFT across models and domains (Table 1, Table 3).

- **Broad empirical scope.** The evaluation spans 5 model families (Qwen, LLaMA, Gemma), sizes from 0.6B to 72B, and three distinct domains (coding, medical, mathematics). Table 3 alone provides a rich comparison of forget-set quality effects across domains. This scope is a real strength relative to typical unlearning papers that evaluate on one dataset.

- **Meaningful ablation of forget-set quality and unlearning variants.** Table 3 systematically compares curated (BC-Select), auto-selected (BC-Cosine), and mixed (BC-Mixed) forget sets, confirming that cleaner forget sets yield better downstream results. Figure 3 shows GA+GD consistently outperforms GA-only, NPO, and GA+KL, validating the importance of the retain term.

- **Representational analysis complements the performance story.** The CKA (Figure 4) and SVCCA (Figure 5) analyses provide converging evidence that F2F induces larger representational changes than standard fine-tuning. While correlational, these analyses go beyond raw accuracy numbers and support the paper's narrative about representational reorganization.

## Weaknesses

### Fatal

None that are verifiable from the paper as written without speculation. The paper's core empirical pattern (F2F > SFT) is consistent and not in question.

### Major

- **Missing retain-only baseline (GD on retain set, no forgetting).** The GA+GD unlearning variant uses a retain set that is "a small subset of the fine-tuning data" (Section 3.3). Thus, during the unlearning phase, the model is already exposed to a portion of the target domain. The observed improvement over standard fine-tuning could arise from this extra domain-specific warm-up rather than from the act of forgetting itself. The paper includes GA-only (σ=0, forgetting without stability) but not the symmetric control: GD-only on the retain set for the same number of steps, followed by the same fine-tuning. Without this ablation, the central causal claim — that gains are *caused* by removing spurious pre-training knowledge — is not isolated. The gains could simply reflect two separate phases of domain training (a multi-stage fine-tuning recipe). This directly undermines the paper's thesis and the framing of unlearning as the causal mechanism.

- **No variance, error bars, or statistical significance reported.** All results in Tables 1–3 and Figure 3 are single-point estimates with no standard deviations, confidence intervals, or seed replications. Given that many absolute improvements are modest (e.g., 3–4 percentage points on larger models, such as LLaMA-8B HumanEval 56.71→60.37), it is impossible to assess whether the differences are reliable or could be due to training stochasticity or hyperparameter sensitivity. For an empirical paper making comparative claims, this is a significant methodological gap.

### Minor

- **Calibration claim is unsubstantiated in the main text.** The abstract and introduction (Section 1) prominently claim that F2F "helps improved calibration on medical QA tasks, reducing overconfidence." No calibration metrics, reliability diagrams, or ECE scores appear anywhere in the body of the paper. While the appendix may contain these results (it was stripped by the parser), such a central claimed contribution must be supported in the main paper. As it stands, the claim is an overstatement.

- **CKA/SVCCA analysis is correlational, not causal.** Section 4.5 shows that F2F causes larger representational drift than standard fine-tuning and states the shift is "toward domain-useful structure." However, greater deviation from the base model does not by itself imply beneficial specialization — a model could drift further while becoming worse. The paper does not provide evidence linking specific representational changes to downstream performance improvements (e.g., correlation between layer-wise CKA and task accuracy). The analysis is consistent with the paper's story but does not prove it.

- **Fairness of baseline hyperparameter tuning is uncertain.** The paper specifies hyperparameters for F2F's unlearning and fine-tuning stages (Section 3.4), but provides no comparable tuning report for DAPT, LoRA, CurlLoRA, or SFT baselines. Additionally, for larger models (LLaMA-8B, LLaMA-13B, Qwen-72B), the "SFT" baseline is actually performed via LoRA (Section 3.4), while a separate "LoRA" row in Table 1 shows different (often weaker) performance, suggesting configuration sensitivity. Ensuring all baselines received a comparable tuning budget would strengthen the comparative evidence.

### Trivial

- The distinction between the "SFT" and "LoRA" rows in Table 1 is ambiguous for larger models, where both use LoRA under the hood. Clarifying exact configurations (rank, target modules, full-parameter vs. LoRA) for each baseline row would prevent reader confusion.

## Nice-to-Haves

- The convex-surrogate proposition (Section 2) provides helpful intuition, but its assumptions (orthogonal decomposition, bounded retain gradient) are not linked to any property of the actual Transformer unlearning procedure. Explicitly discussing which assumptions are violated in practice would help readers calibrate the theory's role as motivation rather than analysis.
- Including a "GD-only on retain set" baseline would transform the paper from suggestive to conclusive regarding the causal role of forgetting.

## Removed Points

*These points were flagged from reviewer inputs but removed from the final review.*

- **"Theory does not guide hyperparameter choices"** — The paper presents the theory as motivation/intuition, not as a practical guide. This is not a weakness of the paper but a misreading of its intent. Removed.

- **"Batch sizes are unusually small"** — The paper reports per-device batch sizes of 2–8 with gradient accumulation to an effective batch size of 128, which is standard practice for large-model training on limited GPU memory. The harsh critic's concern about gradient noise from small per-device batches is speculative and not anchored to any observed problem in results. Removed.

- **"Table 2 does not include F2F results"** — Table 2 is explicitly about comparing fine-tuning variants (SFT, LoRA, CurlLoRA, DAPT) on medical tasks without unlearning, to establish which fine-tuning method is strongest. F2F results are shown separately in Figure 3 and Table 3. This is a presentation choice, not a weakness. Removed.

- **Strength Finder: "Theoretical grounding"** — The convex-surrogate proposition is motivation, not rigorous theory. While it provides helpful intuition, calling it "theoretical grounding" overstates its role. Demoted to a Nice-to-Have note.

## Novel Insights

The paper's core insight — that unlearning can be repurposed from a privacy mechanism to a domain-specialization tool — is genuinely novel and opens an interesting research direction. The finding that forget-set quality (curated vs. mixed) significantly modulates downstream performance (Table 3) is also a practical insight that could inform future work in this space. However, the causal mechanism (forgetting vs. multi-stage training) remains unresolved, which limits the depth of the insight.

## Suggestions

- Add a **retain-only baseline** (gradient descent on the retain set for the same number of unlearning steps, followed by the same fine-tuning). This is the single most important experiment to isolate the effect of forgetting. If F2F still outperforms this baseline, the causal role of unlearning is supported. If not, the contribution should be reframed as a multi-stage fine-tuning recipe.
- Report **per-seed averages with standard deviations** for at least one model/domain pair. Even 3 seeds would substantially increase confidence in the comparisons.
- Either provide **calibration metrics in the main text** or remove the calibration claim from the abstract and introduction.

## Score and Decision

**Anchor comparisons across rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DST (ijwYWoChN9) | 3.00 | R1 | Our paper has much stronger evaluation and clearer motivation |
| Deep Unlearning (CIN2VRxPKU) | 5.33 | R1 | Our paper proposes and validates a method; that paper only analyzes problems |
| UnSTAR (J9Ofr1PmvX) | 5.50 | R1 | Similar novelty level; our paper has broader evaluation but similar methodological gaps |
| Domain-Specific Embeddings (powufeT93G) | 5.25 | R2 | Our paper is more novel and broader in scope |
| Dissecting learning/forgetting (tmsqb6WpLz) | 5.75 | R2 | Both have interesting empirical findings; our missing controls are more damaging to central claims |
| Training Mice (eENHKMTOfW) | 6.00 | R2 | Our paper is more novel but has more significant methodological gaps |
| Lawma (7El7K1DoyX) | 7.00 | R2 | Lawma has more thorough evaluation rigor; our paper's missing controls prevent reaching this tier |
| Probabilistic Unlearning (51WraMid8K) | 8.00 | R1 | Substantially more theoretical rigor; not comparable |

**Round 1 bracket:** 5.5–7.0. **Round 2 narrowed:** the paper sits below the 6.0–7.0 cluster due to the missing retain-only baseline and absence of variance reporting. The closest comparable anchors are UnSTAR (5.50) and Dissecting learning/forgetting (5.75). This paper is stronger than UnSTAR in evaluation breadth but shares its pattern of an interesting idea with methodological gaps that prevent full conviction. The paper is slightly below Dissecting (5.75) because the missing control directly threatens the central causal claim.

**Final score: 5.5. Decision: Reject.** The paper presents a genuinely interesting idea with comprehensive empirical coverage. However, the missing retain-only baseline prevents it from demonstrating that *forgetting* — rather than multi-stage domain training — drives the observed improvements. Combined with no variance reporting and an unsubstantiated calibration claim, the evidence does not yet support the paper's central thesis. These issues are addressable in a revision, and the paper would become substantially stronger with the suggested experiments.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>