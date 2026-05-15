Now I have all the information I need. Let me construct the final review, carefully applying the rules about what to keep, remove, or weaken.

Here is my analysis of each criticism against the paper:

**Critical Issue 1 (batch-dependence / Markov chain):** The paper uses the modeling abstraction Y→X→Z1→Z2→R which is standard in information-theoretic analyses of contrastive learning (e.g., Tian et al., 2020). R represents the self-supervised target — in standard theory, this is the positive-pair relationship determined by the data generation process, not a batch-dependent variable. The paper does not discuss this as a simplification, which is a minor oversight, but declaring the bounds "invalid" misreads standard practice in the field.

**Critical Issue 2 (surrogate MI):** The paper transparently discloses using surrogates (line 96: "Due to the difficulty in computing mutual information with high precision...") and cites Tan et al. (2023). The InfoNCE loss used for I(Z1;R) is a known lower bound on MI (Oord et al., 2018). These are reasonable practical choices, though a formal connection would strengthen the paper.

**Critical Issue 3 (methods don't implement IB):** The training regularization (Eq. 4, line 148) explicitly combines the contrastive loss (maximizing task-relevant info I(Z2;R)) with the MI penalty (minimizing I(Z1;Z2)). This IS an IB-like objective. The architectural methods (discretization, sparse autoencoder) preserve "top-activated" features. However, the paper doesn't directly measure whether task-relevant info is preserved, which is a valid limitation.

Now the full review:

---

## Summary

This paper studies why discarding the projection head improves downstream performance in contrastive learning. It provides an information-theoretic analysis deriving lower and upper bounds on downstream performance (I(Y;Z1)) in terms of I(Z1;Z2) and I(Z1;R), revealing that an effective projector should act as an information bottleneck — filtering information irrelevant to the contrastive objective. Based on this principle, the paper proposes training regularization (mutual information penalty), discretized projectors (FSQ), and sparse autoencoder projectors, showing consistent improvements on CIFAR-10, CIFAR-100, and ImageNet-100 with SimCLR and Barlow Twins.

## Strengths

- **Novel theoretical bounds linking encoder-feature performance to measurable quantities.** The paper derives lower and upper bounds on I(Y;Z1) (Theorems 3.1, 3.2) that express downstream performance in terms of I(Z1;Z2) and I(Z1;R) — quantities that can be estimated during training. This goes beyond prior work (Tian et al., 2020; Xue et al., 2024) that primarily analyzed projector-feature guarantees, addressing a genuine gap in the literature.

- **Empirical validation that estimated bounds correlate with real accuracy.** Figure 3 shows strong correlations between the estimated bounds and actual linear-evaluation accuracy across diverse projector architectures and hyperparameters. Figure 2 shows the bounds track accuracy trends during training. These experiments provide evidence that the theoretical framework is not merely formal but operationally meaningful.

- **Consistent empirical gains across frameworks and datasets.** All three proposed methods improve linear-evaluation accuracy on CIFAR-10, CIFAR-100, and ImageNet-100 under both SimCLR and Barlow Twins (Tables 1–3), with gains up to 3.99%. The ablation study (Figure 4c–e) reveals a U-shaped curve where moderate information reduction helps but too much hurts, consistent with the bottleneck principle.

- **Clean theory-to-practice pipeline.** The same matrix-based mutual information surrogate used to verify the bounds in Section 3.3 is repurposed as the regularization loss in Section 4.1, creating a unified theoretical-to-practical workflow.

## Weaknesses

### Fatal
None.

### Major

- **The Markov chain assumption Y→X→Z<sub>1</sub>→Z<sub>2</sub>→R is presented without discussion of its limitations.** The contrastive objective (e.g., InfoNCE) compares samples within a batch, so the self-supervised target R for a given sample depends on features of other samples in the batch. While treating R as a per-sample abstraction is a standard modeling simplification (used widely in this literature), the paper neither acknowledges this simplification nor discusses conditions under which the bounds approximately hold. The bounds derived under this assumption should be interpreted as a formalization of the bottleneck intuition rather than rigorous guarantees for the actual contrastive objective. This does not invalidate the paper's core insight — the empirical correlations (Figures 2–3) and downstream gains (Tables 1–3) stand independently — but it does weaken the theoretical claims as stated.

- **The empirical validation uses a surrogate mutual information (matrix-based Rényi) without establishing a connection to the Shannon quantities in the theorems.** The paper defines Theorem 3.1 and 3.2 in terms of Shannon I(·;·), then validates them using the Rényi-based surrogate from Tan et al. (2023). No formal relationship or error bound is provided between these two information measures for the feature distributions in contrastive learning. While the strong correlations in Figure 3 are encouraging, they do not constitute a direct validation of the theoretical bounds — they show correlation between a Rényi-based surrogate and accuracy, not between the Shannon bound and accuracy. The paper would benefit from either (a) re-deriving the bounds using the same Rényi-based framework, or (b) providing empirical evidence that the surrogate approximates Shannon MI in this setting.

- **The proposed methods do not directly verify that task-relevant information is preserved while irrelevant information is filtered.** The paper reduces I(Z<sub>1</sub>;Z<sub>2</sub>) across all three methods and shows improved accuracy, but never measures whether I(Z<sub>1</sub>;R) or I(Z<sub>1</sub>;Y) is retained while irrelevant information is removed. The U-shaped ablation curves (Figure 4c–e) are consistent with the IB interpretation, but they are also consistent with any regularizer that prevents overfitting (e.g., weight decay, dropout). Without direct measurements of information preservation, the IB explanation remains one of several plausible hypotheses, not a uniquely supported mechanism.

### Minor

- **No comparison against simpler baselines for projector design.** The paper does not compare the proposed methods (regularization, discretization, sparse autoencoder) against the simple baseline of varying the projector's MLP depth or width. Standard practice in contrastive learning includes tuning these architectural parameters, and it is unclear whether the proposed methods outperform such tuning. The modest gains (0.26%–0.69% on CIFAR-10) could plausibly be matched or exceeded by simple architecture search.

- **No statistical significance reported** Despite relying on single-run comparisons with modest gains (as small as 0.26% on CIFAR-10), the paper reports no error bars, confidence intervals, or multiple-run statistics. This makes it difficult to assess whether the improvements are meaningful or within run-to-run variance.

- **I(Z<sub>1</sub>;R) is estimated via contrastive loss on encoder features, not a proper MI estimator.** While the InfoNCE loss is known to bound MI (Oord et al., 2018), the paper does not justify why the encoder-feature contrastive loss specifically serves as a surrogate for I(Z<sub>1</sub>;R). The contrastive loss conflates alignment and uniformity effects, making this a rough approximation.

### Trivial
None.

## Nice-to-Haves

- Derive an explicit information bottleneck objective (e.g., βI(Z<sub>1</sub>;Z<sub>2</sub>) − I(Z<sub>2</sub>;R)) and compare it against the ad-hoc regularizations used here. This would directly validate whether the IB framework is the right explanation.
- Provide qualitative visualizations (e.g., reconstruction from encoder vs. projector features) to illustrate what information is discarded by the bottleneck.
- Report results on full ImageNet to demonstrate scalability beyond ImageNet-100.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Theoretical bounds rely on an unjustified Markov assumption that ignores batch-dependent nature"** — The critic's claim that this "invalidates" the bounds overstates the issue. The Markov chain is a standard modeling simplification in this literature (cf. Tian et al., 2020; Tishby et al., 2000). The critic's stricter reading would invalidate a large body of work in information-theoretic ML. The appropriate response is to acknowledge the assumption (which I do in Major Weakness 1), not to dismiss the theory entirely.

2. **"Missing steps in derivations" / "I(Z1;R) ≤ I(Z1;Z2) is not proven"** — The proof is presented as a sketch (explicitly labeled "Proof Sketch"). The inequality I(Z1;R) ≤ I(Z1;Z2) follows directly from the Data Processing Inequality under the assumed Markov chain Z1→Z2→R. The critic's demand for a complete derivation misunderstands what a proof sketch is in this context.

3. **"Framing overstates the gap" regarding prior work** — The paper explicitly distinguishes its contribution from prior work (e.g., Jing et al., 2021; Xue et al., 2024) by noting that previous analyses focus on projector features while this paper studies encoder features (lines 33–34). The framing is reasonable.

4. **"U-shaped curve is consistent with any regularizer"** — While true as a caveat, this is acknowledged in the Minor Weaknesses. The paper does not claim exclusivity for the IB interpretation; it claims consistency. The reviewer's point is a generic criticism applicable to most regularizers in ML.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Acknowledge and discuss the Markov chain simplification.** Add a paragraph to Section 3.1 noting that the chain Y→X→Z1→Z2→R abstracts away batch-level dependencies common in contrastive objectives, and discuss when the approximation is reasonable (e.g., large batch sizes, expectations over data distribution).

2. **Either re-derive bounds using the Rényi-based surrogate framework, or validate empirically that the surrogate correlates with Shannon MI estimates** (e.g., using binning or KSG estimators on small-scale data). This would close the gap between the theory (Shannon) and the experiments (Rényi).

3. **Add direct measurements of I(Z1;R) and/or I(Z1;Y) under the proposed methods** to verify that the IB mechanism (preserving relevant info while removing irrelevant info) is actually at work, as opposed to generic regularization effects.

4. **Compare against simple baselines** (varying MLP depth/width, adding dropout/BatchNorm before projector) to demonstrate that the proposed methods outperform straightforward architecture tuning.

5. **Report results with error bars** (at least 3 runs) for the main tables, particularly on CIFAR-10 where gains are smallest.

## Score and Decision

This paper presents a novel theoretical framing of the projection head in contrastive learning as an information bottleneck, supported by consistent if modest empirical improvements. The core insight — that the projector should reduce I(Z1;Z2) while preserving I(Z1;R) — is valuable and likely to influence future design. However, the theoretical foundation relies on an unexamined modeling simplification, the empirical validation uses a surrogate MI without formal connection to the theorems, and the proposed methods lack verification of the hypothesized mechanism. These weaknesses are addressable but nontrivial.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>