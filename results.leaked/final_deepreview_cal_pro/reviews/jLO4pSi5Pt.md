Now I have enough information to write the final review. Let me synthesize everything.

**Bracket summary:**
- Round 1 bracket: paper sits between 6.5–8.0
- Round 2 narrowing: compared to DeYO (7.00), Concept Drift (7.00), RLCF (6.67), DynaPrompt (6.25)
- L-TTA is comparable to or slightly stronger than DeYO (7.00), clearly stronger than the 6.25–6.67 anchors, but has some gaps the 8.00 READ paper didn't have
- Final score: 7.0

Now let me write the final consolidated review.

Let me also verify the specific claims from critics against the paper text:

1. "Reliance on pseudo-label priors without robustness analysis" - Verified. Eq 9 states priors are "continually updated based on the current predicted pseudo-labels." No study of estimation error. This is a real but minor gap.

2. "Missing simple long-tailed baselines" - Verified. No baseline combining TPT/TDA with logit adjustment exists. However, paper does provide theoretical argument and β ablation. Major concern.

3. "Theoretical claims disconnected from empirical validation" - REMOVE. The propositions are mathematical statements with stated assumptions. They don't need "empirical verification" of assumptions. This is a misunderstanding.

4. "Failure modes not operationalized as quantitative metrics" - Verified. Figure 1 shows visualizations but no quantitative metrics for "Text-induced Tail Erosion" or "Modality-bias Amplification." Minor.

5. "EP update φ_c explanation lacking" - Partially true but the text does explain the mechanism. Minor.

6. "Visual encoder frozen - should be stated explicitly" - It IS stated. REMOVE.

7. "No standard deviations" - Verified. Minor.

8. "Table 4 memory entry ambiguous" - Verified. Trivial.

9. "β=0 not tested" - Verified but β=0.1 is close. Minor.

10. "Only CLIP-based models" - Verified. Minor scope limitation.

11. "No limitations section" - Verified. Minor.

Now let me write the review.## Summary

This paper introduces L-TTA, the first test-time adaptation framework for vision-language models (VLMs) designed for long-tailed test distributions. L-TTA combines three components: Synergistic Prototypes (DPs + EPs) that enrich tail classes with inter-class knowledge, learnable Rebalancing Shortcuts with a class re-allocation loss for dynamic adaptation, and Balanced Entropy Minimization (BEM) — a theoretically motivated variant of entropy minimization that penalizes overconfident head-class predictions. Extensive experiments across 15 datasets, three benchmarks, and multiple imbalance ratios (10–50) demonstrate consistent improvements over 12 baselines in both accuracy and macro-F1, with strong cross-backbone robustness and practical efficiency.

## Strengths

- **First systematic study of long-tailed TTA for VLMs.** The paper identifies two specific failure modes (Text-induced Tail Erosion and Modality-bias Amplification, Fig. 1) unique to the VLM-based long-tailed TTA setting, providing clear motivation for the proposed designs.

- **Synergistic prototype design is effective and well-ablated.** Table 6 shows that removing either Deterministic Prototypes or Exclusionary Prototypes reduces macro-F1 by over 3%, confirming their complementary contributions. The Exclusionary Prototypes mechanism — updating all classes from every sample's predictions — is a clever way to ensure tail classes accumulate representations throughout the stream.

- **BEM is a genuinely tailored objective for long-tailed TTA.** Unlike standard entropy minimization which the paper formally shows amplifies head-tail gradient disparity (Proposition 1), BEM's confidence-dependent penalty term shortens this gap (Proposition 2). The β ablation (Fig. 4d) empirically validates that BEM outperforms both near-uniform penalty (β=0.1) and near-standard logit adjustment (β=8).

- **Comprehensive empirical validation across diverse settings.** Gains are consistent across the OOD Benchmark (Table 1, +1.47% Acc / +1.70% macro-F1 at imb=10), Cross-Domain Benchmark (Table 2, 10/11 datasets best), and Corruption Benchmark (Table 3). L-TTA's macro-F1 drops only 1.29% from imb=10 to imb=50 while competing methods degrade by 3.6–4.9% — the central claim of robustness to worsening imbalance is well-supported.

- **Practical efficiency and cross-backbone robustness.** Table 4 shows L-TTA achieves strong accuracy/macro-F1 trade-offs with moderate GPU memory (1.89G) and runtime (1.45h). Table 5 demonstrates the method maintains its lead across ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG.

## Weaknesses

### Fatal
None.

### Major
- **Missing direct baseline combining standard TTA with class balancing.** The paper argues (Section 3.2, before Eq. 9) that naively combining class priors with entropy minimization can amplify head-class bias, and Proposition 2 provides theoretical justification. However, no experiment directly compares against, e.g., TPT or TDA augmented with a running-average class prior and balanced softmax. The β=8 point in Fig. 4d offers indirect evidence that simple logit adjustment underperforms BEM, but this tests only the BEM variant of L-TTA, not whether a simple balancing heuristic on an existing TTA method would close much of the observed gap. A direct baseline comparison would cleanly separate the contributions of the SyPs, RS, and BEM components from simpler rebalancing strategies.

### Minor
- **No variance reporting across runs.** All tables report averages over 5 runs but include no standard deviations or confidence intervals. Since datasets are artificially subsampled for long-tailed distributions, variability across random seeds could be substantial, and statistical significance of the reported gains cannot be assessed.

- **Pseudo-label prior robustness unexamined.** BEM (Eq. 9) uses class priors that are continually updated from the model's own predicted pseudo-labels. Early-stage predictions on tail classes are likely noisy, yet no analysis tracks prior estimation quality over the stream or its impact on BEM effectiveness.

- **Failure modes not quantified.** "Text-induced Tail Erosion" and "Modality-bias Amplification" are illustrated qualitatively in Figure 1 but never operationalized as quantitative metrics in the main experiments. As a result, it is unclear whether L-TTA specifically remedies these modes or simply improves overall long-tailed performance through its components.

- **Scope limited to CLIP with hand-crafted prompts.** All experiments use frozen CLIP backbones with fixed template-based prompts. Transferability to other VLM architectures or prompt-learning setups is unexamined and should be acknowledged as a scope limitation.

- **No limitations section.** The paper would benefit from discussing reliance on a fixed, known set of class names, the assumption of stationary class priors, and potential failure modes when the imbalance pattern shifts over time.

### Trivial
- Table 4 lists WATT memory as "1.54<×n" which is ambiguous and should be clarified.
- The notion of "rich classes" is used informally in the motivation and never measured or ablated.

## Nice-to-Haves
- Sensitivity analysis for the number of augmented views Q and the entropy threshold θ for DP updates, which are implementation choices that could affect performance.
- Analysis tracking pseudo-label prior deviation from ground-truth priors over the stream, to complement the BEM robustness concern.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Theoretical claims are disconnected from empirical validation"** — Removed. Propositions 1 and 2 are mathematical statements with stated assumptions (class cardinality ordering, head/tail split). The assumptions are reasonable and explicitly stated; mathematical propositions do not require "empirical verification" of their premises. The paper provides proofs in the appendix. This criticism reflects a misunderstanding of the role of theoretical analysis.

- **"Visual encoder frozen — should be stated explicitly when prototypes are introduced"** — Removed. The paper does state this in the Rebalancing Shortcuts section: "Considering that prompts in existing TTA methods bring extra gradient flow across the text encoder, we keep the prompts frozen (Zhang et al., 2024a), then introduce learnable Rebalancing Shortcuts (RSs)..."

- **"EP update rationale for subtracting φ_c is not explained"** — Removed. The paper explains: φ_c measures how far a class's probability is from the max probability; when a class is improbable, φ_c is large, making the EMA more plastic. The rationale is present in the text following Eq. 5.

- **Generic formatting/presentation nitpicks about typos, grammar, figure resolution** — Removed per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's framing of concerns largely restates gaps the paper already acknowledges implicitly (e.g., the pseudo-label prior dependency) or proposes additional analyses that would extend rather than alter the core findings.

## Suggestions
- The most impactful addition would be a baseline combining TPT or TDA with a running-average class prior and balanced softmax. This directly tests whether the elaborate SyPs/RS/BEM designs are genuinely necessary or whether a simpler class-balancing heuristic on top of existing TTA could close much of the gap. Even if this baseline underperforms (as the theory predicts), including it would substantially strengthen the contribution narrative.
- Report standard deviations across the 5 runs to allow assessment of statistical significance, particularly important given the subsampled long-tailed distributions.
- Add a brief limitations paragraph discussing the fixed-class-name assumption, stationary prior assumption, and scope.

## Score and Decision

**Round 1 bracket:** Based on calibration anchors, the paper sits between 6.5 and 8.0.

**Round 1 anchors:**
- `pdzHpQbGrn` (avg 2.50): Active test-time prompt learning — rejected, much weaker
- `b20VK2GnSs` (avg 7.00): Concept drift in MLLMs, long-tailed — accepted, similar domain, L-TTA is stronger
- `BUDxvMRkc4` (avg 4.67): BLG long-tailed vision classification — rejected, L-TTA clearly stronger
- `TPZRq4FALB` (avg 8.00): READ multi-modal TTA reliability bias — accepted, slightly stronger than L-TTA but comparable domain

**Round 2 anchors:**
- `9w3iw8wDuE` (avg 7.00): DeYO, TTA with disentangled factors — accepted, comparable quality; L-TTA has broader experiments but DeYO has fewer identified weaknesses
- `kIP0duasBb` (avg 6.67): RLCF, TTA with CLIP reward — accepted, L-TTA is clearly stronger
- `EFZEdHB3Mp` (avg 6.25): DynaPrompt — accepted, L-TTA is clearly stronger

**Comparison:** L-TTA is comparable to DeYO (7.00) in overall quality — both propose novel TTA approaches with theoretical backing and strong empirical results, but each has addressable gaps. L-TTA's experiments are broader (15 datasets vs DeYO's ImageNet-C/R focus), but DeYO had fewer concerns about missing baselines. L-TTA is clearly stronger than the 6.25–6.67 anchors. It falls short of READ (8.00), which introduced new benchmarks, had near-universal reviewer enthusiasm, and had only minor presentation-level weaknesses.

**Final score: 7.0.** The paper addresses an underexplored problem with a well-motivated multi-component method. The empirical campaign is broad and consistent. The key limitation — no direct comparison against a simple TTA + class-balancing baseline — prevents a higher score but does not invalidate the contribution. With that baseline added and variance reported, this would be a clear 7.5–8.0 paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>