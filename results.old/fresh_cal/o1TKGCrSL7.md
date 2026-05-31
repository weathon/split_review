Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes L-DRO, a method that uses natural language descriptions of sub-populations (e.g., "male"/"female", "old"/"young") to debias CLIP image feature representations via entropy maximization over subgroup descriptions, combined with a similarity constraint to preserve general performance. The goal is to improve worst-case accuracy under sub-population shifts without requiring instance-wise sub-population labels during training. The method trains a lightweight feature adapter using only the debiasing objective, and extensive experiments on CelebA and Waterbirds across multiple CLIP architectures (RN50, ViT-B/32, ViT-L/14) show consistent worst-case accuracy improvements over zero-shot CLIP and existing DRO baselines, along with notable training stability.

## Strengths

- **Consistent worst-case accuracy improvements across diverse settings**: Table 8 (lines 387–414) shows L-DRO achieves the highest worst-case accuracy on both CelebA and Waterbirds under both RN50 and ViT-B/32, outperforming ERM, CVaR-DRO, χ²-DRO, JTT, and OrthCali. On CelebA with ViT-B/32, L-DRO reaches 79.2% vs. 72.0% for the next best method (χ²-DRO), with substantially lower standard deviation. On Waterbirds ViT-B/32, L-DRO achieves 64.8% vs. 59.7% for ERM.

- **Training stability across epochs**: Figure 2 (lines 425–432) demonstrates that L-DRO maintains nearly flat worst-case accuracy over training epochs, while CVaR-DRO, χ²-DRO, and JTT exhibit large fluctuations. This is a genuine practical advantage that reduces reliance on careful early stopping with a validation set.

- **Robustness to prompt variation**: Table 3 (lines 196–232) shows L-DRO improves worst-case accuracy over zero-shot across six different classification/debiasing prompt pairs on CelebA (e.g., worst-case improving from 70.6→79.2, 61.1→69.7, 75.0→75.9 under ViT-B/32), indicating the method is not brittle to arbitrary phrasing.

- **Data efficiency**: Table 9 (lines 443–467) shows L-DRO improves worst-case accuracy over zero-shot with as few as 512 training examples on Waterbirds and 2048 on CelebA, demonstrating practical utility in low-data regimes while training only a lightweight adapter.

- **Compatibility with existing DRO methods**: Table 7 (lines 558–586) shows that applying L-DRO before CVaR-DRO or χ²-DRO improves both mean worst-case accuracy and reduces standard deviation (e.g., CVaR-DRO: 67.1±10.4 → 71.0±8.1 on CelebA), suggesting debiased features stabilize loss-based DRO methods.

## Weaknesses

### Fatal
None.

### Major

- **Weak theoretical connection to DRO despite the name "L-DRO"**: Equation (4) (line 171) states a proportionality $\sup_{Q\in\mathcal{Q}}\mathbb{E}_{Z\sim Q}[\ell(\theta, Z)] \propto -\ell_{\text{ent}}(\mathcal{P}(F|\rvx), \mathcal{P}(M|\rvx))$ without any rigorous derivation. The reasoning from lines 163–173 is heuristic — it argues that sub-population performance is proportional to sub-population proportion, then equates entropy balancing to DRO minimization. The actual objective (Eq. 5, lines 183–192) is entropy regularization with a cosine similarity constraint; it is not derived from the DRO dual formulation (e.g., the Cressie-Read family discussed in Section 3.2) and does not minimize a formally defined DRO risk. Calling the method "L-DRO" overpromises on theoretical foundations that the paper does not supply. The method stands on its own as an effective debiasing approach; the DRO framing adds confusion rather than rigor.

### Minor

- **Framing of "domain-oblivious" is imprecise**: The paper defines "domain-oblivious setting" as "wherein the sub-population membership of individual instances remains unknown during the training phase" (line 41). This is accurate as stated, but the framing can mislead because the method requires (a) explicit knowledge of which attributes define the sub-populations (e.g., "male/female") to construct debiasing prompts, and (b) a domain-aware validation dataset for hyperparameter selection (explicitly acknowledged in Table 8 footnote, line 417). While both requirements are standard in the sub-population shift literature, the paper would benefit from a clearer discussion of what knowledge is vs. is not assumed, to avoid inflating reader expectations about the degree of obliviousness.

- **Performance on Waterbirds is more modest and prompt-dependent**: On Waterbirds, several prompt configurations in Table 2 show gains within overlapping standard deviations (e.g., "a {landbird, waterbird}" with ViT-B/32: zero-shot 56.8% vs. L-DRO 56.6±2.6%, line 247), and on ViT-B/32 only two of six prompt configurations show L-DRO outperforming zero-shot (lines 246–263). Although Table 8 shows L-DRO with the best overall Waterbirds performance (64.8±0.8%), the method's effectiveness is clearly sensitive to prompt selection, which the paper acknowledges in its limitations but should weigh more explicitly when summarizing the contribution.

### Trivial

- **Line 602 states** "even though we can eliminate the need for a domain-oblivious validation dataset during training," which appears to contradict the Table 8 footnote stating L-DRO requires a domain-aware validation dataset for hyperparameter selection. Clarify what "domain-oblivious validation dataset" means in this context.

## Nice-to-Haves

- The unaligned debiasing results (Table 5, lines 473–508) show that debiasing for unrelated attributes (e.g., "old/young" while evaluating on "male/female") gives near-baseline performance. This is interesting and correctly interpreted, but a brief discussion of when attributes are likely to be "influential" vs. "independent" would help practitioners apply the method.

- The paper could explicitly compare the required degree of attribute knowledge for L-DRO vs. the group-label requirements of methods like CVaR-DRO or JTT to better clarify the practical trade-offs.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder's claim #3 about "Theoretical grounding of the debiasing objective: Equation (4) establishes a principled link..."** — Removed because the theoretical connection is heuristic rather than principled (see Major weakness above). The paper's strength lies in its empirical results, not in formal theoretical grounding.

- **Harsh critic's statement: "The paper contains a significant disconnect between its claims and what the method actually delivers"** — Removed as overblown. The paper defines "domain-oblivious" explicitly (line 41) as not using instance-wise labels, which is factually correct. The method does not require instance-wise sub-population labels during training. The critic's framing as a "significant disconnect" inflates a reasonable presentation concern into a structural flaw.

- **Harsh critic's statement: "the magnitude of improvement is sometimes modest relative to standard deviations (e.g., Table 2, first row, ViT-B/32)"** — Removed as cherry-picking. The main comparison table (Table 8) shows clear, non-overlapping improvements on both datasets across both architectures. The critic selects the weakest prompt configuration while ignoring the best and most standard configurations.

- **Strength Finder's strength about "generalization to semantically related prompts"** — Kept in modified form; actually this is genuinely interesting. Let me re-check... I'll keep this as part of the robustness analysis.

## Novel Insights

The most interesting observation emerging from the reviews is that the paper's key advantage — training stability across epochs — is a structural property of its entropy-based objective, not an accident. Unlike loss-based DRO methods that amplify gradients for hard examples and cause oscillatory behavior, L-DRO's debiasing objective saturates naturally once features become uninformative about the target sub-population. This insight is implicit in the paper (Figure 2 and Section 5.1) but could be stated more explicitly as a design principle: entropy maximization over subgroup logits provides a natural regularizer that makes training dynamics independent of the loss landscape's worst-case fluctuations. The combination results in Table 7 further suggest that this stability can be *transferred* — debiased features stabilize downstream DRO methods — which is a noteworthy system-building property.

## Suggestions

1. **Rename or reframe the DRO connection**: Either rename the method (e.g., "Language-Guided Debiasing") or explicitly state in Section 4 that the connection to DRO is motivational/intuitive, not a formal instantiation of the DRO dual formulation. The current framing invites scrutiny the method does not need to withstand.

2. **Clarify the domain-oblivious framing**: Add a sentence in the introduction that the method assumes knowledge of which attributes define sub-populations but not which examples belong to which subgroup — contrasting with methods that require per-instance group labels. This would preempt the misunderstanding the harsh critic raised.

3. **Fix the apparent contradiction about validation data**: Line 602 says L-DRO eliminates the need for a "domain-oblivious validation dataset," but the Table 8 footnote says L-DRO requires a domain-aware validation dataset for hyperparameter selection. Harmonize this language.

## Score and Decision

The paper makes a genuine, empirically well-supported contribution: using natural language prompts to debias CLIP features at training time improves worst-case accuracy under sub-population shifts with notable training stability. The theoretical DRO framing is weak and should be scaled back, and the presentation can be sharpened, but these are addressable issues that do not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>