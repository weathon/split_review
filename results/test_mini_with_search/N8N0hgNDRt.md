Now I have enough calibration context. Let me compose the final review.

**Round 1 Bracket:** Based on the initial calibration search, the paper sits between the weak anchors (scores 2-3 for flawed papers) and the middle anchors (scores 4-7). Papers scoring 8+ are not comparable in topic. The plausible range is 5.0-7.0.

**Round 2 Narrowing:** Comparing MetaMath to the 6.00-scoring papers (MathFimer, QuestA), MetaMath is comparably strong or stronger: it tests at 3 scales (not 1), has cleaner ablations, and more comprehensive analysis (diversity, perplexity, backward evaluation, error analysis, negative result). It is clearly above WarriorMath (4.50) and EFAGen (4.40). The narrowing settles on 6.0-7.0.

**Final Score:** 6.5 — The paper is a solid, well-executed contribution with a clean idea and thorough evaluation, positioned above comparable accepted papers.

---

## Summary

This paper proposes MetaMath, a family of LLaMA-2 models fine-tuned on bootstrapped mathematical questions. The key idea is "question bootstrapping": generating diverse training examples from original math problems through forward rephrasing (LLM rephrasing) and backward reasoning (Self-Verification and FOBAR templates), combined with answer augmentation via rejection sampling. The resulting MetaMathQA dataset (395K samples) is used to fine-tune LLaMA-2-7B, 13B, and 70B. MetaMath-7B achieves 66.5% on GSM8K and 19.8% on MATH — exceeding prior open-source 7B models by 11.5% and 8.7% respectively — and MetaMath-70B (82.3% on GSM8K) slightly surpasses GPT-3.5-Turbo, the model that generated the training data.

## Strengths

- **Substantial and cleanly-demonstrated accuracy gains across three model scales.** MetaMath-7B improves over WizardMath-7B by 11.6% on GSM8K and 9.1% on MATH (Table 2). The 13B and 70B results show consistent improvements. These gains are not marginal — they represent a clear advance over prior open-source math models.

- **Well-controlled ablation isolating the contribution of each augmentation component.** Table 3 shows the stepwise benefit: AnsAug+Rephrasing → 60.6% GSM8K, adding SV+FOBAR → 64.4%. This cleanly quantifies the specific value of backward question bootstrapping beyond forward-direction augmentation.

- **Quantified positive correlation between question diversity and accuracy.** The Pearson coefficient of 0.972 (Section 4.4) between diversity gain and accuracy gain provides concrete evidence for the paper's central thesis — that the diversity introduced by question bootstrapping, not just data quantity, drives improvement. This is supported by the negative result (Figure 3) where adding RFT data to MetaMathQA hurts performance.

- **Targeted measurement and remediation of backward reasoning deficits.** The paper constructs GSM8K-Backward (1,270 backward questions) and shows that existing models (SFT, RFT, WizardMath) have a large accuracy gap on backward questions, while MetaMath nearly closes this gap (Figure 4). This provides direct evidence that the backward bootstrapping addresses a specific, measurable weakness.

- **Outperforms the teacher model.** MetaMath-70B achieves 82.3% on GSM8K, surpassing GPT-3.5-Turbo (80.8%) which generated the augmented data, demonstrating that bootstrapping can distill knowledge beyond the teacher's own forward-direction performance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Backward reasoning examples filtered only by answer correctness, not reasoning-path validity.** For SV and FOBAR bootstrapped questions (Section 3.3), the filtering criterion is simply that the generated masked-value matches the original ground-truth number. As the reviewer notes, a correct numeric answer could theoretically arise from a flawed chain (e.g., compensating arithmetic errors). The paper's ablation shows the net effect is positive, so this does not threaten the core contribution. However, a small-scale manual check of reasoning-path quality for backward examples would have been a straightforward addition and would strengthen the claim that these examples teach genuine backward reasoning.

- **No statistical significance or variance reported for main results (Table 2).** All accuracies are point estimates without confidence intervals, standard deviations, or multi-seed runs. For the 70B results in particular (MetaMath 82.3% vs. WizardMath 81.6%, Δ ≈ 9 correct answers out of 1,319), the reader cannot assess whether the difference is statistically significant. This is a common practice in the literature (WizardMath, RFT, MAmmoTH also report point estimates), but it limits the precision of the paper's comparative claims.

- **Limited training hyperparameter details in the paper.** The paper does not report learning rate, batch size, number of epochs, or optimizer settings for any model size. The code is released, which fills this gap for reproducibility, but summarizing key settings in the paper would aid readers.

### Trivial

- The Figure 3 "More Data is Not Always Better" experiment tests only one mixing ratio and one training schedule. The paper's cautious phrasing ("may not be beneficial") is appropriate, but a sensitivity analysis across ratios would strengthen the claim.

## Nice-to-Haves

- **Ablation with a different generator model.** All augmented data is generated by GPT-3.5-Turbo. Testing whether the bootstrapping method works when the generator is a weaker open-source model (e.g., LLaMA-2-70B) would strengthen the claim that the method itself — not just distillation from a stronger model — drives improvements.
- **Discussion of potential selection bias from rephrasing filtering.** The paper reports that GPT-3.5-Turbo accuracy is 76.30% on rephrased questions vs. 80.74% on originals, meaning ~24% of rephrasings are discarded. A brief discussion of whether this selects only "easy" rephrasings would be informative.

## Removed Points

The following points raised by reviewers were removed with justification:
- *"Perplexity is not a direct measure of pedagogical value"* — The paper already acknowledges this is speculative language ("we speculate," "may serve"), and the perplexity analysis is presented as suggestive correlation, not causal evidence.
- *"Rephrasing filtering might introduce bias"* — Speculative framing of a concern the paper partially addresses by reporting the accuracy gap (76.30% vs 80.74%). Moved to Nice-to-Haves.
- *"Clarify combined training setup (balanced sampling, ratio)"* — The paper states data is merged as D_MetaMathQA = D_AnsAug ∪ D_rephrase ∪ D_SV ∪ D_FOBAR, and Table 1 shows exact sizes per component. This is sufficient for a research paper.
- *"Ablation with ChatGPT vs. LLaMA-2 generation"* — An interesting follow-up study but outside the stated scope of the paper. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The review input surfaces a useful tension: the backward-reasoning path-quality concern is real but self-limiting — if flawed backward chains were common, the ablation would show degradation, not the observed improvement. The reviews do not identify any contradiction or unstated assumption in the paper's internal logic that the paper itself does not already address.

## Suggestions

1. **For revision:** Add a small-sample manual evaluation (e.g., 100 SV and 100 FOBAR examples) of reasoning-path quality for backward bootstrapped data. This directly addresses the main reviewer concern and is straightforward.
2. **For revision:** Add bootstrap confidence intervals for the main results in Table 2, or report means over 3-4 seeds for the 7B model. Even a single additional run would substantially strengthen the comparative claims.
3. **For revision:** Report key training hyperparameters (learning rate, batch size, epochs, optimizer) in the experimental setup section.
4. **For the camera-ready:** The "More Data is Not Always Better" claim would benefit from a sensitivity analysis across mixing ratios (e.g., 25%, 50%, 75% RFT data mixed with MetaMathQA).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| TabularGSM | PoUdJ8bMDQ.md | 2.67 | R1 | Much weaker; flawed methodology and narrow scope |
| AgenticMath | 2aA6YwZYOJ.md | 3.00 | R1 | Much weaker; limited results |
| WarriorMath | JPZoLWYo82.md | 4.50 | R2 | Weaker; confusing methodology, missing baselines, high computational cost |
| ExecFuncAbst | Wrte87s2Bs.md | 4.40 | R1/R2 | Weaker; small gains (+2-3%), limited novelty |
| F1-Reasoner | BejA1KL8cA.md | 4.40 | R1 | Weaker; narrower contribution |
| ProofRM | ZZAIF9fjlU.md | 4.50 | R1 | Weaker; different task (proof verification) |
| ScaleDiff | dbcXNwfgsI.md | 4.00 | R2 | Weaker; withdrawn paper |
| Rewriting Pretrain | 45btPYgSSX.md | 4.50 | R2 | Weaker; different focus (code+math pre-training data) |
| MathFimer | 14i2wzPPfn.md | 6.00 | R1/R2 | Comparable; similar strength, clean ablations, accepted as Poster |
| QuestA | 3MifB0f7qR.md | 6.00 | R2 | Slightly weaker; limited to 1.5B models, less comprehensive ablation |
| Quantization+Reasoning | So3hbnEGYV.md | 5.00 | R2 | Weaker; different topic (quantization degradation) |
| RIDE | PPkzchpdNK.md | 5.00 | R2 | Weaker; evaluation/perturbation paper, not training method |

MetaMath is clearly stronger than the 4.0-5.0 papers (WarriorMath, EFAGen, ScaleDiff, etc.) and at least comparable to the 6.00-level papers (MathFimer, QuestA). It has a cleaner method, more comprehensive evaluation across 3 model scales, better ablation studies, and stronger results than these accepted papers. The score of 6.5 positions it above the typical Poster-acceptance papers while reflecting that the work is a solid contribution rather than a paradigm-shifting advance (which would warrant 8+).