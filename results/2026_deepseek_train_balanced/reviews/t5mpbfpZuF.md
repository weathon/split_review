## Summary

The paper proposes DEAL, which applies Wasserstein Distance Guided Representation Learning (WDGRL)—an existing domain adaptation algorithm—to the final embedding layer of an LLM reward model. The goal is to transfer supervision from a labeled source distribution to an unlabeled target distribution across four low-data scenarios: cross-lingual transfer, clean-to-noisy generalization, few-shot alignment, and easy-to-hard (short-to-long) transfer. The paper evaluates this approach on SHP, CValues, and essay-scoring benchmarks.

---

## Strengths

- **Well-motivated problem framing.** The four scenarios (cross-lingual, noise-robust, few-shot, easy-to-hard) are genuinely practical challenges in LLM alignment where labeled target data is scarce. The paper provides concrete examples (e.g., translating Reddit preferences to Korean/Thai/Chinese, transferring from argument fragments to full essays) that make the motivation clear.

- **Diagnostic analysis provides mechanistic insight.** The odd-one-out toy experiment (Section 4) shows that domain adaptation can prevent shortcut learning (e.g., "reject anything that isn't a fruit" vs. learning the general "odd one out" logic). The two-moons 2D visualization (Figure 3) and PCA embedding analysis on the safety task (Figure 4) geometrically demonstrate that DEAL clusters unlabeled target points around the few-shot labeled examples—a visualization that goes beyond reporting accuracy numbers.

- **The short-to-long essay transfer experiment is a creative and practically motivated setup.** Translating supervision from ~10–100 word argument fragments to ~200–600 word full essays (Section 5.4) is a genuinely non-trivial transfer scenario where labeling short fragments is cheaper, and the paper attempts to quantify this transfer.

- **Results are reported as mean ± standard error over 3 random seeds** (all table captions), and the paper states the snapshot selection criterion (maximum validation performance, line 105), providing a minimal floor of empirical rigor.

---

## Weaknesses

### Fatal
None.

### Major

1. **The method is standard WDGRL applied as-is, not a novel proposal.** The paper presents DEAL as a proposed method ("we propose Data Efficient Alignment for Language..."), but Section 3 describes standard WDGRL (Shen et al., 2018) without any modification for the LLM reward-modeling setting. The loss functions in equations 66–75 are the standard WDGRL critic loss, gradient penalty, and task loss. There is no algorithmic change, no architectural adaptation, and no justification for why WDGRL specifically is suited to LLM reward model embeddings over alternatives. The paper must either reframe itself as an empirical study of applying domain adaptation to LLM alignment (with correspondingly rigorous experiments) or contribute some methodological novelty. Currently it does neither.

2. **The experimental design cannot attribute gains to domain adaptation.** The paper compares DEAL against exactly one baseline: "train on source" (training only on labeled source data without any unlabeled data). This is insufficient to support the claims. Several critical missing comparisons:
   - **No comparison to other domain adaptation methods** (DANN, MMD, DeepJDot are all discussed in Related Work but never compared against). Without this, we cannot tell whether WDGRL's Wasserstein distance is beneficial or whether any form of distribution matching works.
   - **No ablation of the domain adaptation component** (e.g., training on source + unlabeled data *without* the domain critic/loss; varying λ in Equation 74). The observed gains could come from the simple presence of more data during training (semi-supervised learning) rather than distribution alignment specifically.
   - **No semi-supervised learning baseline** (e.g., self-training with pseudo-labels on target data), which is a simpler and more standard NLP approach to using unlabeled data.
   
   Without these controls, the paper's central claim—that domain adaptation/distribution alignment causes the improvements—is unsupported by the evidence presented.

3. **Critical implementation details are missing, making the work irreproducible.** The paper never specifies:
   - **Which LLM is used as the base reward model.** The only model mentioned is Gemma-2-9b-it, which was used *to generate data* in the noise experiment, not as the reward model. Line 54 says "the LLM" without identification.
   - **Hyperparameters:** learning rate, batch size, optimizer, λ and γ trade-off parameters, number of training epochs, critic architecture, gradient penalty coefficient.
   - **How unlabeled target data is used at test time** in the translation and noise scenarios.
   - **The definition of "accuracy"** on preference data. For a preference dataset, accuracy presumably means the fraction of pairs where the model assigns a higher score to the preferred response, but this is never stated.

   These omissions are not minor formatting issues—they prevent independent verification of the results.

4. **All quantitative results are in unreadable image tables.** Tables 1–5 are embedded as images (lines 94, 114, 124, 154, 189). The paper provides no prose summary of the key figures (e.g., "DEAL improved accuracy from X% to Y% on average across language splits"). This means the reader cannot evaluate the magnitude, consistency, or statistical significance of the reported improvements from the text alone. At a top-tier venue, key results must be represented in reader-accessible form.

5. **The method description contains a technical inconsistency.** Line 69 states: "A gradient reversal layer is placed in between the feature extractor and critic head." This is a component from DANN (Ganin et al., 2015), not standard WDGRL (Shen et al., 2018). In WDGRL, the critic is trained to maximize the Wasserstein distance and the feature extractor to minimize it through alternating optimization/sign flips in the loss, not via a gradient reversal layer. If the implementation used a gradient reversal layer, the training dynamics differ from standard WDGRL. The paper never clarifies whether this is intentional (a hybrid method) or an error in the description. Either way, the method as described is ambiguous.

### Minor

- **The few-shot PCA visualization uses unequal training epochs.** Line 161: the "train on source" baseline is evaluated after 10 epochs while DEAL is evaluated after 1 epoch for the PCA embedding analysis (Figure 4). This confounds the comparison: the baseline may have overfit at 10 epochs, making the embeddings look worse. The comparison should use equivalent training steps (e.g., early stopping at similar validation performance).

- **No downstream RLHF evaluation.** The paper evaluates reward model accuracy but never runs RLHF or evaluates a downstream aligned LLM. While the paper scopes itself to reward model training (line 54–57), the title and abstract ("Aligning Large Language Models") imply a broader claim. A brief experiment showing that DEAL-trained reward models improve best-of-N sampling or RLHF outcomes would substantially strengthen the connection.

- **No analysis of failure cases or negative results.** The paper notes one case where domain adaptation "slightly decreases performance" (Section 5.1) and attributes it to high zero-shot performance, but provides no systematic analysis of when domain adaptation helps vs. hurts. Understanding the boundary conditions of the method is valuable.

### Trivial

- "Tne critic head" (line 61) → "The critic head" (typo).

---

## Nice-to-Haves

- A comparison of computational cost (DEAD adds a critic network and requires processing unlabeled data); the paper does not discuss whether the gains justify the additional training overhead.
- Varying the weighting hyperparameter λ in Equation 74 would help characterize the trade-off between task accuracy and distribution alignment.
- For the noise scenario (Section 5.2), characterizing what kind of noise exists in the original SHP data and verifying that the LLM rewriting actually removed it would strengthen the experimental construct validity.

---

## Removed Points

These points from the input reviews were flagged for removal or are treated with caution:

- *"Missing related work on semi-supervised learning for LLMs"* — Removed per instructions (no external sources to confirm specific omissions).
- *"The paper would benefit from a larger dataset"* — Generic, not a concrete weakness.
- *"No comparison of computational cost"* — Moved to Nice-to-Haves; demanding cost analysis for a conference paper is not standard.
- *Strength Finder's specific numbers* (e.g., "+7.3 points on legaladvice Korean," "+15.9 points on askscience Thai," "8.3 points / 5.7 points on short-to-long") — These exact numbers do not appear in the paper text; the tables are images that cannot be read. The general claim of "consistent improvement" is retained; specific unverifiable numbers are dropped.
- *"WDGRL with gradient penalty as a non-trivial engineering contribution"* — This overstates the contribution; the method is standard WDGRL.
- *"Reproducibility practices" as a standalone strength* — Partially retained in strengths (mean±SE reporting), but the missing base LLM and hyperparameters severely undermine this.
- *Harsh critic's claim "the leap from reward model accuracy to LLM alignment is substantial and unsupported"* — Weakened to Minor, as the paper explicitly scopes itself to reward model training (line 54: "We focus on training reward models..."). The title claim is broader than the experiments, but this is a scope mismatch, not a fatal error.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' main insights (that the method is standard WDGRL, that the experimental design lacks the baselines needed to attribute gains to domain adaptation, that the gradient reversal layer description is inconsistent with standard WDGRL) serve as critical evaluation of the paper's evidence rather than novel observations about the field.

---

## Suggestions

1. **Rebaseline the experiments against at least one other domain adaptation method** (DANN is the natural choice—it is the closest alternative and would isolate whether the Wasserstein distance matters) and a semi-supervised learning baseline (e.g., self-training with pseudo-labels). Without these, the core claim is not supported.
2. **Add an ablation without the domain critic** (train on source + unlabeled data with only the task loss). This would control for the effect of simply seeing more data.
3. **Specify the base LLM backbone, all hyperparameters, and the accuracy metric definition.** Without these, the work is irreproducible.
4. **Report key numerical results in prose** (in addition to tables), so readers can assess the magnitude and statistical significance of improvements without reading images.
5. **Clarify the technical inconsistency about the gradient reversal layer:** is the method standard WDGRL, DANN, or a hybrid? Correct the description or justify the deviation.
6. **Add a downstream experiment** (e.g., best-of-N sampling with the trained reward models on a generation task) to connect reward model accuracy to actual LLM alignment quality.
7. **Equalize training epochs** for the few-shot PCA comparison (Figure 4) so the visualization is not confounded by overfitting in the baseline.

---

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>