Now I have all the information I need. Let me produce the final review.

## Summary

This paper proposes L-DRO, a method that uses natural language descriptions of sub-populations (e.g., "male"/"female") to debias CLIP image representations. The key idea is to train a lightweight feature adapter that maximizes the entropy of sub-population membership predictions (making features uninformative about the spurious attribute) while maintaining consistency with the original CLIP embedding. Experiments on CelebA and Waterbirds show that L-DRO improves worst-group accuracy over zero-shot CLIP and several DRO baselines (CVaR-DRO, χ²-DRO, JTT), with notably more stable training curves.

## Strengths

- **Consistent worst-case accuracy improvement across diverse settings**: L-DRO improves worst-group accuracy over zero-shot CLIP across multiple prompts, two architectures (RN50, ViT-B/32), and two datasets. For instance, on CelebA with ViT-B/32, worst-case accuracy rises from 70.6% (zero-shot) to 79.2%±1.3% (L-DRO). On Waterbirds with RN50, worst-case jumps from 34.0% to 62.7%±2.8%.

- **Dramatically improved training stability**: Figure 1 shows L-DRO maintains nearly constant average and worst-case accuracy across training epochs, while CVaR-DRO, χ²-DRO, and JTT exhibit large fluctuations (10–20% swings). This directly addresses the known instability of DRO methods and reduces reliance on domain-aware validation for early stopping — a practical advantage.

- **Data efficiency**: L-DRO achieves competitive worst-case accuracy with a fraction of the training data. On Waterbirds, worst-case accuracy reaches 57.9%±3.1% with just 512 examples — surpassing zero-shot (43.6%) — and near-full-data performance (65.1%) with 2048 examples.

- **Flexibility for multiple and semantically-related sub-populations**: L-DRO can debias against multiple simultaneous attributes (e.g., {male, female} + {old, young}) with modest degradation, and generalizes to semantically related descriptions (e.g., "man/woman" for "male/female") with graceful degradation, showing robustness to imperfect prompt selection.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous description of training objective.** The paper claims in multiple places (abstract, Sec. 4, conclusion) that L-DRO operates "without instance-wise label information," and the L-DRO loss in Eq. (4) uses only entropy over sub-population prompts and a cosine-similarity consistency term — no labels. However, line 193 states: "The corresponding training and inference of L-DRO follow the procedures of Eqs. (1) and (2)," where Eq. (1) explicitly defines training using cross-entropy loss with ground-truth labels. While the intended meaning is likely that L-DRO uses the same *architecture* (I→A→T) as Eqs. (1)–(2) but with the *loss* from Eq. (4), the wording creates genuine ambiguity about whether labels are used during the debiasing phase. The reader cannot determine whether L-DRO is label-free or uses labels for a secondary classification task. This needs a precise clarification (e.g., a dedicated Algorithm box showing the exact forward pass and loss).

- **Confusing presentation of the η sensitivity experiment.** Table 6 is captioned "with varying η" but shows columns labeled 512, 1024, 2048, 4096, 8192. These same labels appear in the immediately following data-efficiency table (Table 7) but with completely different numerical values (confirming Table 6 is *not* a duplicate data-efficiency table). The default η is 0.2, so values of 512–8192 are unexplained and non-standard for a balancing parameter. The table may genuinely show robustness across some range, but the choice and meaning of these values are not justified. A proper ablation over interpretable η values (e.g., {0.01, 0.1, 0.2, 0.5, 1.0, 5.0}) is needed to substantiate the claim of η-robustness.

- **Weak theoretical connection to DRO / overclaimed framing.** The derivation in Eq. (3) (lines 163–172) attempts to connect sub-population shift to entropy maximization via an informal proportionality argument: it reasons that sub-population performance is proportional to the sub-population's proportion in the data, then jumps to entropy as a measure, concluding sup E[ℓ] ∝ −ℓ_ent. This reasoning is heuristic, not a formal DRO derivation. The resulting method — maximizing entropy over sub-population logits — is better described as *language-guided adversarial debiasing at the feature level* (related to fair representation learning) rather than a DRO method in the standard sense (uncertainty sets, worst-case loss minimization). The "DRO" label overclaims the theoretical grounding and may confuse readers.

- **Average accuracy cost is acknowledged but underexplored.** In Table 4, L-DRO improves worst-case accuracy on CelebA (79.2% vs. 72.0% for χ²-DRO) but at a substantial average accuracy cost (83.6% vs. 95.3% for ERM and ~87–90% for DRO methods). The paper acknowledges L-DRO does not use labels, which partly explains the gap, but practitioners need clearer discussion of this trade-off. A plot or table showing (average accuracy, worst-case accuracy) across η values or prompt choices would help.

- **Missing training implementation details.** The paper does not specify the optimizer, learning rate, batch size, number of training epochs, or learning rate schedule for L-DRO. While some details may follow the cited CoOp paper (Gao et al. 2021), the method description should be self-contained for reproducibility.

- **Evaluation on only two datasets.** CelebA and Waterbirds are standard subgroup-shift benchmarks, but evaluating on one additional dataset (e.g., CivilComments-WILDS or MultiNLI) would strengthen generalizability claims. This is noted as a scope limitation.

- **No ablation of the adapter architecture.** The adapter is a two-layer MLP. It would be informative to test whether a linear layer suffices, or whether more capacity changes the debiasing behavior.

### Trivial
- The column labels in Table 6 (η sweep) use the same numeric values as Table 7 (data efficiency), creating unnecessary confusion. Rename or annotate clearly.

## Nice-to-Haves
- Provide an Algorithm box with the exact training loop for L-DRO (forward pass, loss computation, backward pass) to eliminate the ambiguity about the training objective.
- Add an ablation comparing L-DRO with only the entropy term, only the consistency term, and both.
- Discuss why the combination of L-DRO with DRO methods fails on Waterbirds (Table 8). The paper mentions it "does not show any advantages" but does not analyze why.

## Removed Points
*These points are flagged to be removed, treat them with caution:*
- **η table is "clearly the data efficiency result"** — The reviewer claimed Table 6 (η sweep) is actually the data-efficiency table. This is factually incorrect: the values in Table 6 (Avg 83.6–84.5, W.C. 76.3–79.2) are completely different from Table 7 (data efficiency: e.g., 512 samples: Avg 77.1, W.C. 57.2). The criticism is removed because it is based on a misreading of the data.
- **Missing related works** — Removed per policy (no external sources to confirm).
- **Pure formatting/style nitpicks** (e.g., "W.C.Acc." vs "Worst-case Acc." standardization) — Removed per hard rule.
- **Unfair comparison to zero-shot CLIP framed as a structural flaw** — L-DRO's primary value is improving subgroup robustness over the label-free zero-shot baseline, which is an appropriate comparison for a method designed to operate without instance-level labels. The paper *also* compares to training-based methods (ERM, DRO, JTT). The zero-shot comparison is legitimate and expected for a CLIP-based method.

## Novel Insights
The reviews converge on the core strength of the paper: the language-guided feature-debiasing approach is intuitive, practically motivated, and delivers on its promises (worst-case improvement, training stability, data efficiency). The most novel observation from the reviews is the identification of an unresolved ambiguity about the training objective — the paper simultaneously claims "no instance-wise labels" and references a training equation that uses cross-entropy. This is the single issue that needs most urgent clarification, as it affects the fundamental interpretation of what L-DRO does. The reviews also surface that the DRO framing is more decorative than substantive; the method is essentially an entropy-based debiasing technique, which is a cleaner and more accurate description.

## Suggestions
1. **Clarify the training objective.** State explicitly that L-DRO trains the adapter *only* with Eq. (4) (entropy + consistency), without cross-entropy on class labels. If labels are used for a secondary task, remove the "without instance-wise label information" claim.
2. **Fix the η sweep.** Replace the current table with a proper ablation over interpretable η values. Explain the range and show that worst-case accuracy is stable across it.
3. **Reframe the method.** Drop the stretched DRO theoretical framing. Describe L-DRO as language-guided feature debiasing (maximizing entropy over sub-population logits to achieve invariance to spurious attributes).
4. **Add training details.** Specify optimizer, learning rate, batch size, epochs, and hardware.
5. **Discuss the average-accuracy trade-off explicitly.** Include a brief discussion or visualization of how much average accuracy is sacrificed for worst-case gains.

## Score and Decision

The paper makes a genuine contribution: using natural language to guide feature-level debiasing for subgroup robustness is a clean and effective idea, supported by consistent empirical gains and a practically important stability advantage. The weaknesses are real but addressable — none is fatal. The training-objective ambiguity and the confusing η table need clarification before publication.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>