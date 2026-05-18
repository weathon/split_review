Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper studies the underexplored problem of "parameter imbalance" — the bias inherited from imbalanced pre-training data of foundation models — and its interaction with downstream "data imbalance" in long-tailed learning. Through controlled experiments (Figs. 2–3, Tables 2–4), the paper shows that while data imbalance can be effectively corrected by re-balancing methods like Logit Adjustment (LA), parameter imbalance persists and dominates performance. The paper further models this via a causal graph where "incomplete semantic factors" act as confounders between inputs and labels, and proposes a backdoor adjustment (Eq. 7) implemented by fusing predictions from multiple foundation models (CLIP, OpenCLIP, MetaCLIP) fine-tuned with LA. Experiments on ImageNet-LT, Places365-LT, and iNaturalist2018 show consistent gains, especially on tail classes.

## Strengths

1. **Demonstrates the dominance and persistence of parameter imbalance.** Through controlled experiments with CE and LA criteria (Figs. 2–3), the paper convincingly shows that re-balancing methods correct downstream data imbalance but leave pre-training-derived parameter imbalance largely intact. Tables 2–3 quantify this gap across CLIP, OpenCLIP, and MetaCLIP, establishing parameter imbalance as a distinct and practically important challenge.

2. **Feature vs. classifier diagnosis.** Table 4 uses KNN accuracy to show that re-balancing methods like LA improve tail-class performance mainly through the classifier head, not the representation. This clean experiment explains why logit-based re-balancing cannot fix parameter imbalance (which is baked into the backbone parameters), motivating representation-level intervention.

3. **Detailed combined-imbalance analysis.** Splitting classes into 9 groups along both parameter and data imbalance dimensions (Fig. 2) provides fine-grained insight — "Tail-Tail" (D-Few & P-Few) classes suffer most, and LA actually hurts P-Few classes within D-Many groups. This granular analysis clarifies the compounding nature of the two biases.

4. **Consistent improvements on tail classes across three benchmarks.** On ImageNet-LT (+3.49% on D-Few over LIFT), Places365-LT (+2.91% overall over VL-LTR), and iNaturalist2018 (+1.91% overall over RAC), the proposed method delivers practically meaningful gains, with the largest improvements consistently on tail classes.

## Weaknesses

### Major

1. **Missing control baseline prevents attribution of improvement to the causal mechanism.** The backdoor adjustment (Eq. 7) averages predictions from 3 foundation models, each fine-tuned with LA — this is structurally a multi-model ensemble. The paper compares against single-model baselines (LIFT, VL-LTR, etc.) but against itself only compares M=1 vs. M=3 (Table 8), which any ensemble would trivially satisfy. The critical missing experiment is: compare the proposed fusion against a **simple logit average of the same 3 models fine-tuned without the causal framing** (e.g., each fine-tuned with CE and their outputs averaged). Without this, the claimed benefit of the "causal adjustment" over "generic ensemble" is unsubstantiated. The paper also compares against methods using a single CLIP backbone while using 3 backbones itself, further confounding the source of gains. These are not fatal flaws — the method may still be practically useful — but they mean the paper cannot claim its improvement validates the causal model.

2. **Causal graph assumptions are abstract and unverifiable.** The confounder C (incomplete semantic factor) is never directly measured. The backdoor adjustment assumes C blocks all backdoor paths between X and Y, which is untestable with an unmeasured C. The paper approximates different C values using different foundation models and assumes P(c)=1/M without justification. The Grad-CAM visualizations (Fig. 4) showing different models attend to different image regions are suggestive but do not demonstrate that these regions constitute "incomplete semantic factors" in the causal sense, nor that they are caused by parameter imbalance. The causal framing is an interesting perspective, but the paper does not validate that it is the causal mechanism (rather than generic ensemble diversity) driving the empirical gains.

### Minor

3. **Ablation on M (Table 8) does not validate the causal story.** M=3 outperforming M=1 is expected from any model ensemble. The paper does not test whether different random seeds of the *same* architecture (which would have the same pre-training distribution, hence the same parameter imbalance) also yield gains — this would be necessary to attribute improvement to diverse "semantic factors" rather than generic ensemble diversity.

4. **Pre-training prior estimate unvalidated.** The analysis of parameter imbalance (splitting classes into P-Many/Medium/Few) relies on the GLA-estimated prior (Eq. 3). The paper does not assess the reliability of this estimate, e.g., by verifying against a known prior in a synthetic setting or checking consistency across methods. While GLA is published prior work, the paper's core argument about the primacy of parameter imbalance depends on this estimate being accurate.

5. **Equal-weighting assumption P(c)=1/M underexplored.** The paper assumes all M foundation models contribute equally without ablation or justification. Unequal weighting based on per-model calibration or tail-class bias could potentially improve results.

6. **Unclear whether the method works with a single backbone.** The proposed backdoor adjustment inherently requires multiple models to approximate different C values. This raises the practical question of whether the framework can be applied when only one foundation model is available (e.g., by treating different attention heads or feature clusters as different C values, as the reviewer suggests). The paper currently does not address single-backbone applicability.

### Trivial

- Some implementation details could be clarified (exact LA integration procedure for each backbone, fusion at test time beyond "merging").
- The paper uses "incomplete semantic factor" and "partial semantic factor" interchangeably — consistent terminology would help.

## Nice-to-Haves

- **Simple ensemble baseline:** Adding an ablation where the three foundation models are fine-tuned with CE (or the same loss) and their logits are simply averaged would directly test whether the causal framing adds value beyond ensemble diversity.
- **Correlation test for parameter imbalance relief:** Computing the correlation between class performance and estimated pre-training prior before/after the backdoor adjustment would provide direct evidence that the method reduces parameter imbalance.
- **Different-seed control:** Testing whether multiple seeds of the same OpenCLIP architecture (same pre-training distribution) yield similar gains when fused would disentangle "different pre-training distributions" from "generic ensemble diversity."
- **Cost comparison:** The computational overhead is honestly reported but not compared against the alternative of using a larger single backbone or full fine-tuning.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the filtering rules:

- *"The paper reuses GLA but criticizes it"* — The paper does not criticize GLA; it analyzes its limitations (GLA-Train doesn't work during training), which is a fair empirical finding. Removed as factually inaccurate.
- *"KNN analysis is consistent with existing literature"* — The reviewer acknowledges this as a useful observation; it is not a weakness. Removed.
- *"Generic strengths" from Strength Finder* — The claim that the causal-graph formulation is a "core strength" is retained but weakened given the unvalidated assumptions. Generic phrasing without specific evidence was dropped.
- *Demands for broader scope experiments* — Requests to test on additional tasks/domains beyond the paper's stated scope were removed as scope creep.

## Novel Insights

Beyond the paper's own contributions, the most interesting synthesis from the reviews is the contrast between the paper's analytical contributions (which are solid) and its methodological claims (which are overclaimed). The paper convincingly identifies parameter imbalance as a real and persistent problem and provides clean diagnostics (feature vs. classifier, 9-group analysis). However, the proposed solution is essentially a simple ensemble given a causal justification, and the experiments do not isolate the claimed mechanism. This suggests the paper's most durable contribution may be the problem analysis and diagnosis rather than the specific method. A stronger paper would either (a) replace the causal apparatus with a simpler "ensemble of diverse foundation models mitigates parameter imbalance" story, or (b) operationalize C more concretely to make the causal claims testable.

## Suggestions

1. **Add the simple ensemble control baseline** (average-logit fusion of 3 CE-fine-tuned models) to distinguish the effect of having multiple backbones from the effect of the causal adjustment.
2. **Temper the causal claims** or provide direct validation (e.g., show that the correlation between class accuracy and estimated pre-training prior decreases after the backdoor adjustment).
3. **Report a single-best-model comparison** on equal footing — compare the best individual model (CLIP, OpenCLIP, or MetaCLIP) fine-tuned with the same PEFT + LA recipe against the 3-model fusion, to clarify the marginal benefit of the ensemble.
4. **Justify or ablate the equal-weighting assumption** P(c)=1/M.
5. **Move the causal framing to a justification** and describe the method honestly as "an ensemble of foundation models with diverse pre-training distributions" rather than implying the backdoor adjustment is a distinct algorithmic operation beyond averaging.

## Score and Decision

The paper makes a genuinely useful contribution by identifying and diagnosing parameter imbalance — a real, underappreciated problem in long-tailed fine-tuning. The analysis (Figs. 2–3, Tables 2–4) is clean and the method produces consistent empirical gains. However, the methodological novelty is weakened by (a) the absence of a simple ensemble control baseline, which makes it impossible to attribute the gains to the causal mechanism rather than generic ensemble effects, and (b) the abstract, unverifiable causal graph assumptions. These issues do not invalidate the paper but do reduce the strength of its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>