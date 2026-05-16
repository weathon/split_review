Now I have a thorough understanding of the paper. Let me construct the final consolidated review, carefully verifying each claim against the paper text.

---

## Summary

This paper studies how the bias of foundation models' pre-training data ("parameter imbalance") combines with downstream long-tailed data ("data imbalance") to hurt fine-tuned model performance. Through careful analysis, the authors show parameter imbalance is more persistent and cannot be fixed by logit-adjustment style re-balancing. They then propose a method that fine-tunes multiple foundation models (CLIP, OpenCLIP, MetaCLIP) with Logit Adjustment and averages their predictions, framed as a causal backdoor adjustment over "incomplete semantic factors."

## Strengths

- **Clear empirical distinction between parameter imbalance and data imbalance** – The paper formally defines parameter imbalance (from pre-training) and data imbalance (from downstream), then shows experimentally (Figures 2, 3, Table 2) that parameter imbalance more strongly affects tail-class performance after fine-tuning, and that classes both "D-Few" and "P-Few" are the worst affected. This is a well-supported, nontrivial finding.

- **Demonstration that logit-adjustment re-balancing fails to fix parameter imbalance in representations** – Tables 3 and 4 show that GLA-Train (extending logit adjustment into training) gives minimal benefit over LA, and that KNN accuracy—a representation-quality metric—is barely improved by re-balancing methods. This establishes that parameter imbalance operates at the representation level, not just the classifier, which is a meaningful insight.

- **Causal perspective provides principled motivation for using diverse foundation models** – The paper constructs a causal graph (Figure 5) identifying the "incomplete semantic factor" as a confounder, providing a principled reason for why predictions from models with different pre-training distributions should be combined. This framing connects an observed practical phenomenon (ensemble helps) to a formal causal model.

- **Consistent empirical gains on three benchmarks** – On Places365-LT, ImageNet-LT, and iNaturalist2018, the proposed method (M=3) outperforms strong single-model baselines, with the largest gains on tail classes (e.g., +3.49% on ImageNet-LT D-Few). The ablation study (Table 8) further shows increasing M consistently improves performance.

- **Detailed group-wise analysis revealing the "Tail-Tail" problem** – Figure 2 splits classes into 9 groups by both data- and parameter-imbalance quartiles, showing that LA actually hurts "P-Few" classes within "D-Many", revealing a nuanced failure mode of re-balancing.

## Weaknesses

### Fatal

None.

### Major

- **The "backdoor adjustment" method is an ensemble of fine-tuned models with uniform averaging; the causal framing does not introduce a technically novel adjustment mechanism.** The core operational step (Section 5.2, Eq. 7) reduces to averaging predictions from M models fine-tuned with a re-balancing loss, each from a different foundation model. The derivation assumes P(c)=1/M (uniform), makes the simplifying assumption that the mapping X→B is injective and deterministic, and does not estimate any causal structure from data. No intervention is performed; no new training mechanism is derived. The paper's claimed contribution of a "novel backdoor adjustment method" is overstated—the actual technique is model averaging with causal motivation. This is a structural issue that undermines the paper's central claim of technical novelty.

- **The experimental comparison is asymmetric and a key control is missing.** The main results (Tables 5–7) compare the proposed method—which uses **three** different foundation models (CLIP, OpenCLIP, MetaCLIP)—against baselines that use **one** foundation model (typically CLIP). The ablation (Table 8) shows that using three models outperforms using one, but this comparison is only within the proposed method. The paper does not include a control where baselines (e.g., LIFT, VL-LTR) are also applied to multiple foundation models and their predictions ensembled. Without such a control, the reported gains cannot be confidently attributed to the backdoor adjustment; they could simply reflect the benefit of using multiple diverse backbones. This is an evidential issue: the central claim of method superiority is not fully supported.

### Minor

- **The strong claim that parameter imbalance "cannot be effectively addressed" by re-balancing rests primarily on one attempted method.** Section 4.2 shows that GLA-Train (a specific extension of logit adjustment to the training phase) fails to improve performance, and the paper concludes that "parameter imbalance is fundamentally different from data imbalance and cannot be resolved through simple adjustment alone." While the KNN analysis (Table 4) provides supporting evidence that re-balancing doesn't improve representations, this is still a broad claim to rest on one implementation. Other re-balancing strategies (e.g., decoupled training with balanced classifier re-training, balanced contrastive losses) are not tested. The paper would be more persuasive with a more measured conclusion, e.g., "the specific GLA-Train adjustment we attempted did not work; this motivates a different approach."

- **The causal derivation contains several logical leaps that are not fully justified.** (a) The assumption that the mapping X→B is injective (each sample uniquely maps to a balanced representation) is stated without justification. (b) The step from ∑_b ∑_c P(Y=y|b,c)P(c)P(b|x) to ∑_c P(Y=y|b,c)P(c) relies on P(b|x)=1 for a single b, which assumes determinism that contradicts the probabilistic framing used elsewhere. (c) The uniform prior P(c)=1/M is arbitrary and not justified in terms of the causal model. These do not invalidate the practical method but weaken the claimed rigor of the causal derivation.

- **No variance or statistical significance is reported.** All main results are reported as single numbers without standard deviations or confidence intervals. Given the method involves multiple models and training runs, this makes it difficult to assess whether observed improvements are statistically significant.

- **The "P-Few" group analysis after the method (Figure 6)** compares the proposed method and LA, but does not include comparisons with other baselines (e.g., LIFT, GLA) over the same grouped analysis. This would strengthen the claim that the method specifically helps "P-Few" classes.

- **The paper does not specify precisely which re-balancing loss is used for each model in the ensemble.** Line 239 says "utilize a re-balancing method, such as Logit Adjustment (LA)" but does not explicitly confirm LA is used in the main experiments. The ablation (Table 8) suggests LA, but this should be stated explicitly.

### Trivial

None.

## Nice-to-Haves

- A control experiment where the same backbone (e.g., CLIP) is fine-tuned multiple times with different random seeds or learning schedules and then ensembled. This would help isolate whether the improvement comes from backbone diversity (different pre-training distributions → different incomplete semantic factors) or simply from the benefits of any model ensemble.
- A comparison where baselines (LIFT, VL-LTR) are also given multiple backbones and ensembled, to make the comparison symmetric.
- Grad-CAM visualizations comparing the proposed method against baselines, not just CE and LA.
- A learned (non-uniform) weighting scheme for fusing predictions instead of uniform 1/M, to test whether the uniform weights are actually optimal or just a simplifying choice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The harsh critic's criticism that "GLA's prior estimation procedure is borrowed from Zhu et al. (2024) and not independently justified" — This is standard practice; the paper properly cites the source and uses the method as intended. Not a weakness.
- The criticism that the paper "does not discuss why GLA-Train fails (only that it does)" is a "wishlist" item — The paper's analysis of the failure (that parameter imbalance is fundamentally different and operates at the representation level) is discussed through the KNN analysis and the paper's overall argument. The reviewer's demand for per-class logit statistics is excessive for this scope.
- Various formatting/style nitpicks from the Section-by-Section notes — These are parser artifacts or presentation preferences.

## Novel Insights

The reviews collectively surface one genuinely novel observation beyond the paper's own contributions: **the causal framing of "incomplete semantic factor as confounder" provides a testable hypothesis about why diverse pre-training distributions help** — it's not just about having more models, but about models that capture different partial features. This is more specific than the generic "ensemble helps" observation, and the Grad-CAM visualizations (Figure 4) provide initial supporting evidence. However, this insight would be much stronger with the missing control (same backbone, different seeds) to confirm that backbone diversity specifically (not just ensemble size) drives the improvement.

## Suggestions

1. **Reframe the contribution honestly.** Present the method as a causally-motivated ensemble of PEFT models from diverse foundation models, not as a novel "backdoor adjustment algorithm." The causal framing remains valuable as motivation and explanation.
2. **Add the missing control.** Report what happens when you give a strong baseline (e.g., LIFT) the same three backbones and ensemble the predictions. If the proposed method still outperforms this control, the claim of causal adjustment value is much stronger.
3. **Tone down the claim about re-balancing failing.** Replace "cannot be effectively addressed by current re-balancing techniques" with "GLA-Train, a natural extension of logit adjustment into training, did not fix parameter imbalance; this suggests the problem operates differently from data imbalance."
4. **Report standard deviations** over at least 3 runs for the main tables.
5. **Explicitly state which re-balancing loss is used** for fine-tuning each model in the ensemble.

## Score and Decision

The paper identifies a genuine and underexplored problem — parameter imbalance from pre-training — and provides a clear empirical analysis showing its persistence. The analysis contribution (Section 4) is solid and informative. However, the claimed method contribution is substantially overstated: the "backdoor adjustment" is an ensemble of fine-tuned models with uniform averaging, and the experimental evaluation does not control for the asymmetric advantage of using three backbones versus the baselines' one. The core empirical claim — that the proposed method is a superior approach — is not adequately supported by the evidence as presented. The paper could be strengthened with the suggested controls and a more measured framing, but in its current form, the central claim of methodological novelty and the evidence for superiority are insufficient.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>