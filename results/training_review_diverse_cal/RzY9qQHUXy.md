I now have a complete picture of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper identifies an important problem in long-tailed learning: conventional class-independent data augmentation (DA) can harm tail classes while improving average accuracy, creating an "extrinsic augmentation-wise imbalance" on top of the inherent data-wise imbalance. To address this, the authors propose Dynamic Optional Data Augmentation (DODA), which maintains per-class probability distributions over augmentations ("preference lists") and updates them dynamically based on positive sample counts. Experiments on CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018 show consistent improvements across multiple long-tailed learning baselines.

## Strengths

- **Important problem identification**: The paper clearly identifies and empirically demonstrates (Figure 2) that class-independent DA sacrifices specific classes — especially tail classes — while boosting average performance. This observation is well-motivated and validated across multiple DA types (Cutout, CUDA, hybrid).

- **Clean, flexible method**: DODA's core idea — per-class DA selection via preference lists — is intuitive and the method integrates orthogonally with six different long-tailed learning algorithms (CE, CE-DRW, LDAM-DRW, BS, RIDE, BCL) in Table 1, with every integration showing accuracy gains. This flexibility is a genuine strength.

- **Consistent empirical improvements**: DODA shows positive gains across three datasets (CIFAR-100-LT at IR={10,50,100}, ImageNet-LT, iNaturalist 2018) and six baselines, plus outperforms five DA methods (AutoAugment, Fast AutoAugment, DADA, RandAugment, CUDA) in Figure 7. The consistency across diverse settings suggests the method captures a real effect.

- **Quantified reduction in class sacrifice**: Figure 4 reports that DODA reduces the sacrifice rate by 31% and 24% relative to CUDA, directly supporting the paper's central claim about protecting tail classes.

## Weaknesses

### Major

- **Missing comparison with the most closely related prior work (FSR).** The paper cites FSR (Wang et al. 2023, ICCV) in the introduction as "a pioneer [that] first proposed an adaptive augmentation to rebalance the potential temporal feature space" — yet FSR is absent from all experimental tables. This is the most directly comparable method in the literature (also learning class-dependent augmentation policies for long-tailed data). Without this comparison, the paper's claim of "state-of-the-art performance" (Contributions, line 28) is unsubstantiated against its closest competitor. The authors must add FSR as a baseline or explain why the comparison is not feasible.

- **Theoretical analysis is presented as formal theory but is heuristic illustration.** Theorems 1–4 are stated with equations and natural-language assertions but no formal proofs. Theorem 1 restates a standard observation (augmented samples deviate from the ideal level-set, citing Balestriero et al. 2022). Theorem 3's derivation depends on the critical, unsubstantiated assumption that Δ_{c_h} = Δ_{c_t} (same distribution radius increase under DA for all classes). The "distribution span" analysis (Section 2.2) is explicitly a 2D toy model — the paper acknowledges it approximates high-dimensional space as "regular hyperspace" and uses "two-dimensional space to illustrate this" — yet it is presented under the heading of formal theoretical analysis. The core insight (DA disproportionately impacts tail classes) is genuinely valuable and empirically supported, but the paper inflates its intellectual contribution by framing this intuition as rigorous theory.

- **Potential BCL baseline discrepancy needs clarification.** The harsh reviewer reports that BCL is listed at 49.7% on ImageNet-LT (Table 2), while the published BCL paper (Zhu et al. 2022, NeurIPS) reports 57.2% under standard protocols — a 7.5-point gap. Different backbones, training schedules, or data preprocessing could explain this, but the paper does not disclose any such deviation. If the comparison is not apples-to-apples, the entire BCL row in Table 2 is misleading. The authors must disclose their BCL reproduction protocol and, if it differs from the standard, re-run the comparison fairly.

- **No error bars, confidence intervals, or significance tests.** The paper states "average results of three random trials" for CIFAR-100-LT but reports only single numbers without variance in Tables 1–2. DODA's improvements are often modest (per the reviewer, 0.3–1.5 percentage points on many settings), and the method introduces additional stochasticity through random DA selection per sample. Without error bars, the reader cannot assess whether the observed gains are reliable or within training noise. This is especially concerning for the smallest improvements (e.g., +0.3 on BS at IR=10).

### Minor

- **The DODA update rule is heuristic with known confounds.** The rule compares the current epoch's positive sample count per class to the previous epoch's count: if it rises, the DA used in the current epoch is up-weighted; if it falls, down-weighted. The positive count depends on the entire model state (not just the augmentation), and the comparison can mix across different DAs if different augmentations were used in successive epochs. Theorem 4 (more dominant DA → less biased level-set) is essentially a restatement of the premise rather than independent justification. The method works empirically, but the paper should be transparent that this is an intuitive heuristic, not a theoretically grounded procedure.

- **Incomplete specification of the augmentation pool.** The paper mentions "10 common DAs" (Section 4.3) and gives examples (Gaussian blur, rotation, horizontal flip, line 105) but does not list the full set of K augmentations. This makes exact reproduction difficult. The authors should specify all augmentations, their strengths/parameters, and how K was chosen.

- **No ablation on augmentation probability p_aug.** The hyperparameter p_aug (probability that a sample is augmented) is fixed at 0.5 for all experiments without any sensitivity analysis. It is plausible that optimal p_aug differs across datasets, imbalance ratios, or even classes, potentially offering further gains.

- **No analysis of computational overhead.** DODA evaluates K augmentations per sample during training (by sampling one of K), which adds training cost relative to single-DA baselines. The paper should report wall-clock training time or FLOPs relative to baselines to help practitioners assess the trade-off.

- **The 50-epoch random warm-up strategy is not ablated or justified beyond "cold-boot issues."** The paper switches from a random strategy to the proposed update at epoch 50 for CIFAR-100-LT (200 total epochs). No analysis examines whether the method works without warm-up, with a shorter warm-up, or with a different initialization.

### Trivial

- Figure 2 plots per-class accuracy for 100 classes, making it hard to visually assess the "sacrifice" pattern. A histogram of per-class accuracy changes or a summary statistic would be more directly informative.
- The "birds/hypocritical/bullying" metaphor is colorful but can substitute for precise technical description (e.g., Section 2.2's title "DA favors long-tailed learning through 'bullying'") rather than providing a formal link between the metaphor and the toy model.

## Nice-to-Haves

- A more principled update rule (e.g., a bandit algorithm like Exp3 with regret guarantees) could strengthen the method's theoretical grounding without changing the core idea.
- Per-class ablation of p_aug or the warm-up duration would clarify design choices.
- Reporting standard deviations for all main results would establish reliability.

## Removed Points

- **Criticism about BCL being "misreported" at the level of questioning its existence as a cited method**: Not applicable; the criticism is about numerical values, not existence.
- **"The paper does not discuss how many augmentations K"**: The paper does mention K (line 105) and "10 common DAs" in the CIFAR-100-LT experiments (line 204), so this criticism was partially inaccurate. Retained the specific concern about listing the full set of DAs.
- **Criticisms about "no code release" and "Algorithm 1 is truncated"**: The parser strips figures and algorithms; Algorithm 1 exists in the original submission. Moved to this section per the missing appendix rule.
- **Strength Finder's claim of "Formal theoretical analysis"**: Conflicts with verified weakness #2 (theoretical analysis is heuristic). Per the rule "when a strength and weakness disagree, the weakness wins," this claimed strength is removed.
- **Suggestion to use validation accuracy for updating preference lists**: This is a reasonable idea but the current design is defensible, and the paper presents a working method. Demoting to nice-to-have does not misrepresent the paper.

## Novel Insights

The most useful insight across the reviews is that the paper's claimed formal theory is better understood as an illustrative toy model. The core empirical finding — that class-independent DA disproportionately penalizes tail classes — and the DODA method itself are the real contributions. A revision that honestly re-frames the theoretical section, adds FSR and fixes the BCL comparison, and reports error bars would turn a borderline paper into a strong one. The contrast between the intuition and the overclaimed formalism is the key tension the authors need to resolve.

## Suggestions

1. **Add FSR as an experimental baseline** — this is essential to substantiate the SOTA claim.
2. **Clarify the BCL baseline**: disclose the exact protocol used for ImageNet-LT and reconcile with the published BCL numbers. If different backbones or schedules were used, state this explicitly and re-run comparisons under matched conditions.
3. **Reframe Section 2 honestly**: present Theorems 1–4 as intuitive motivations and observations (not formal theorems with proofs), and describe the 2D toy model as illustrative rather than rigorous. This aligns the claims with what the paper actually delivers.
4. **Report standard deviations** for all main results (Tables 1–2), or at minimum for the CIFAR-100-LT experiments where "three random trials" are already conducted.
5. **List the full set of K augmentations** used in experiments, including their parameters/strength settings.
6. **Ablate p_aug** and the 50-epoch warm-up to show sensitivity, or justify the chosen values with evidence.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>