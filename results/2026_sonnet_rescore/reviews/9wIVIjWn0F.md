Now I have enough context to write the final review. Let me synthesize the findings.

---

## Summary

This paper proposes **Regression-based Test-Time Adaptation (RTA)** for CLIP-based image classification. The core idea is to train a lightweight decision tree (LightGBM) offline to predict pseudo cross-entropy loss from CLIP logit vectors, then use this predictor at test time to select the most reliable augmented views for ensemble inference. The method avoids gradient updates and memory banks. Experiments on single-label ImageNet variants, 10 cross-domain datasets, and three multi-label benchmarks demonstrate consistent improvements over entropy-based TTA competitors.

---

## Strengths

1. **Compelling ceiling TTA experiment.** Tables 1 and 2 rigorously show that ground-truth CE loss ($H_{LCE}$) dramatically outperforms Shannon entropy for view selection (e.g., ViT-B/16 on ImageNet-A: 90.2% vs 64.3% with 64 views), providing a clear empirical motivation and establishing a meaningful upper bound for the proposed approach.

2. **Consistent empirical improvements across diverse benchmarks.** RTA outperforms Zero, BCA, TDA and other recent methods on the majority of settings in Tables 3–6. For RN50 on ImageNet-A, the improvement over the best competitor is 6.44% (36.79% vs 30.35% BCA). For multi-label, RTA surpasses ML-TTA on all six dataset/backbone combinations — the pattern holds across convolution-based and transformer-based backbones.

3. **Computationally efficient design.** Training requires only 1,000 pseudo-labeled samples from ImageVal-12k and 100 rounds of LightGBM with no gradient computation. At test time there are no parameter updates or memory bank maintenance, making the approach notably lighter than TPT, DiffTPT, or RLCF.

---

## Weaknesses

### Fatal
None — no single flaw, as written in the paper, fully invalidates the reported empirical results.

### Major

- **Missing trivial baseline: max-confidence view selection.** The pseudo-label CE loss (Eq. 4) is derived from high-confidence CLIP predictions (confidence ≥ 0.8 filter, §5.1). For such a sample, Eq. 4 reduces to $-\log(\max_j \text{softmax}_j(s))$ — a deterministic, closed-form function of the input logit vector $s$. A well-trained decision tree fitting this target will therefore approximate the negative log of the maximum softmax probability. Consequently, selecting top-$k$ views by smallest predicted loss may be functionally equivalent to selecting views by highest max-confidence — a single-line computation requiring no regression model at all. The paper contains no experiment comparing RTA against direct max-confidence view selection, which is the one experiment needed to determine whether the regression contributes something beyond a roundabout approximation of an existing closed-form statistic. Until this baseline is tested, it is impossible to verify the paper's core claimed mechanism. This does not nullify the empirical improvements but does seriously undermine the explanatory framing of the contribution.

- **Unexplained dimensionality mismatch for cross-domain generalization.** The regression model is trained on ImageNet logit vectors with 1000 dimensions ($j = 1, \ldots, L=1000$ in Eq. 3 / Algorithm 1). At test time, the target domain's class set varies widely: VOC2007 has 20 classes, UCF has 101, Aircraft has 100, Cars has 196. A LightGBM model trained on 1000-dimensional feature vectors cannot accept 20- or 196-dimensional inputs without an unreported adaptation step. The paper's central claim — "the regression mapping only needs to be trained once in the initial stage, and then it can directly adapt to test instances with arbitrary distributions" (§1) — is contradicted by this mismatch. Table 4 reports results on all 10 cross-domain datasets without any explanation of how the dimensionality difference is resolved. This is a reproducibility-critical methodological gap; readers cannot replicate these experiments from what is written.

- **Multi-label extension is methodologically undefined.** The regression model is trained to predict single-label CE loss (Eq. 4), which assumes a single correct class index $l$. For multi-label tasks (MSCOCO, VOC2007, NUSWIDE), images may have multiple positive labels. The paper reports mAP results in Tables 5–6 and states the method achieves competitive performance, but never defines what CE loss the regression is trained to predict in a multi-label setting, how pseudo-labels are assigned when multiple classes are valid, or how view selection interacts with mAP computation. This is a structural gap, not a missing ablation: the method as specified does not cover the multi-label setting it is evaluated on.

### Minor

- **Large ceiling gap is unacknowledged.** Table 2 shows $H_{LCE}$ with ViT-B/16 and 64 views achieves 89.0% on ImageNet and 90.2% on ImageNet-A. Table 3 shows RTA achieves 71.13% and 65.65% respectively — gaps of ~18% and ~25%. If the regression were a meaningful approximation of the label CE loss signal, we would expect RTA to substantially narrow the gap to the ceiling. The paper presents the ceiling as motivating the method, then never discusses why the approximation is so distant from what it is approximating. This narrative inconsistency is worth addressing in the text.

- **Notation inconsistency in §4.3.** Equations 8, 9, and 10, along with Algorithm 2, use the superscript $x_i^{reg}$ for test-time inference (e.g., $s_{ij}^{x_i^{reg}}$ in Eq. 8, $V_{conf} = \{\mathbf{x}_i^{reg} \mid ...\}$ in Eq. 10), when the intended quantity is $x_i^{test}$. The training-stage notation leaks into the test-time algorithm, making Algorithm 2 harder to follow.

- **No statistical significance reporting.** Several headline improvements in Table 3 are below 1% for ViT-B/16 (OOD average: RTA 65.84% vs Zero 65.03%; IN-1k: RTA 71.13% vs Zero 70.89%). With no variance estimates or confidence intervals, it is difficult to assess whether these margins are reliable, especially given that single-run evaluation is reported. This is non-standard only in that the margins are unusually small; some indication of reliability would strengthen the claims.

### Trivial

- Y-axis truncation in Figure 5 (IN-1k range 70.6–71.2; Invariant Acc range 65.2–66.0) visually amplifies the sensitivity to sample pool size; the absolute improvement from 1k to 50k samples is ~0.6% and ~0.8%.

---

## Nice-to-Haves

- **Feature importance analysis for the LightGBM model.** A permutation-importance or SHAP analysis of the trained tree would clarify whether the tree's decisions hinge primarily on the top-1 logit (equivalent to max confidence) or encode richer multi-class relationships. This is a cheap experiment that would directly illuminate the mechanism and is the highest-leverage improvement the paper could make.
- **Explicitly report the EuroSAT exception.** In Table 4 (ViT-B/16), BCA outperforms RTA on EuroSAT by ~3% (56.63 vs 53.65). Discussing this exception, even briefly, would improve the paper's intellectual honesty and might point to an interesting domain-specific limitation.
- A brief ablation replacing the regression with direct max-confidence selection would conclusively settle the mechanistic question and strengthen (or importantly clarify) the contribution.

---

## Removed Points

*These points were evaluated and removed — treat with caution.*

- **"Free lunch" claim is overstatement (Harsh Critic §Abstract).** This is a valid minor point but the paper uses "free lunch" as a rhetorical device referring to the absence of gradient updates and label access, not a literal absence of computational cost. The actual training cost (1000 samples + 100 LightGBM rounds) is genuinely negligible relative to the inference cost, so this is too minor to retain as a weakness.

- **Eq. 8 cross-entropy loss for pseudo-label CE is "not well-supported" (implied).** The harsh critic's analysis of the Spearman / t-SNE visualizations "proving less than claimed" is not an error per se; the paper uses them as secondary supporting evidence for a regression-learnable structure, not as proof of a novel non-trivial mapping. The visualization evidence is consistent with the paper's framing; removing this sub-point.

- **Harsh Critic's claim that "equal-interval sampling" is unmotivated.** The paper says "sampling by logit-based equal-interval from 5,000 samples" (§5.1). This is a standard diversity-preservation sampling heuristic. The critic asks for further motivation, which is a preference, not a flaw.

- **"BCA average comparison is only 0.11% gap."** The margin 68.70% vs 68.59% is small, but (a) this is above BCA for most tasks, and (b) the paper already notes it carefully as "edging out." Not a misrepresentation.

- **Reproducibility nitpick on hyperparameters** (max depth 5, 16 leaves, lr 0.01): these are explicitly stated in §5.1 and are more than sufficient for reproducing the LightGBM setup.

- **Strength Finder: "visual and correlation analyses corroborate the regression assumption."** Retained as a supporting observation but demoted: as the harsh critic correctly notes, these analyses are consistent with the regression simply fitting a deterministic function of the inputs. The strength is valid but weaker than framed.

---

## Novel Insights

The most substantive insight emerging from this review — beyond the paper's own framing — is the equivalence hypothesis: because the regression targets (pseudo-label CE loss) are deterministic functions of the regression inputs (logit vectors) for high-confidence samples, the proposed method may reduce to max-confidence view selection implemented via an unnecessary regression intermediary. If confirmed, this would reframe the paper's contribution as demonstrating that maximum softmax confidence is a superior view-selection criterion to Shannon entropy — itself a publishable and interesting finding, but one requiring much simpler exposition. Conversely, if the regression provably outperforms max-confidence selection, the paper would have demonstrated that the tree captures multi-class logit structure beyond the top-1 probability, which would be a genuinely novel and mechanistically interesting result. Either outcome is worth reporting; the current paper reports neither.

---

## Suggestions

1. **Add a direct max-confidence baseline** ($\arg\max_j p_j$ as view-selection score, no regression). This single experiment determines whether the regression contributes anything beyond a deterministic approximation.
2. **Explain the dimensionality handling** for cross-domain evaluation. Specify whether logits are sorted, truncated, padded, or re-computed against target domain class names (which would imply domain-specific retraining that contradicts the "train once" claim). If target-domain logits are used at test time, clarify whether the tree can generalize to different logit dimensions and by what mechanism.
3. **Define the multi-label adaptation** in a dedicated subsection: what CE loss target is used for multi-label pseudo-labeling, and how multi-label pseudo-labels are assigned given CLIP's single-class softmax output.
4. **Conduct a LightGBM feature importance analysis** (SHAP values or gain-based importance) to determine whether the tree's decisions primarily use the top-1 logit or a richer multi-class signature.
5. **Acknowledge and explain the ceiling gap** in §4.1 or §5.2: why does RTA achieve only 65.65% on ImageNet-A when the ceiling is 90.2%, and what this implies about the quality of the regression approximation.

---

## Score and Decision

**Originality:** The idea of using an offline-trained regression to predict CE loss for view selection is genuinely novel in the TTA context. The ceiling TTA experiment is a clean and insightful design. Score: 3/5 (novel framing, but the core mechanism may reduce to a well-known heuristic).

**Importance:** TTA for CLIP is an active and practically relevant problem; a lightweight offline-trained method is valuable. Score: 3/5.

**Claims supported:** The empirical claims (outperforming competitors) are supported. The mechanistic claims ("regression mapping captures view quality beyond what entropy measures") are inadequately supported due to the missing max-confidence baseline and unexplained cross-domain applicability. Score: 2/5.

**Soundness of experiments:** Broad coverage across architectures and benchmark types is a plus. However, the cross-domain method is underspecified, multi-label adaptation is undefined, and no statistical significance is reported for small margins. Score: 2/5.

**Clarity:** Good overall structure and readable prose. Notation errors in §4.3 and incomplete method description for key settings detract. Score: 3/5.

**Value to the research community:** If the max-confidence baseline shows RTA does better, or if the method is properly specified for cross-domain use, the contribution would be solid. As written, the reproducibility gaps and unverified mechanism limit immediate value. Score: 3/5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>