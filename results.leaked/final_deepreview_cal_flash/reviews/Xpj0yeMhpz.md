Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper introduces a new problem formulation for class-wise machine unlearning where the target concept is decoupled from the class label, creating mismatch scenarios (target-mismatch, model-mismatch, data-mismatch) beyond the conventional all-matched setting. The authors propose TARF, a framework that combines annealed gradient ascent on forgetting data with target-aware gradient descent on hard-to-affect retaining data, guided by a theoretical analysis linking representation distance to forgetting dynamics ("gravity effect"). Experiments on CIFAR-10/100, ImageNet-1k, and case studies on Stable Diffusion and LLM unlearning show TARF consistently achieves the smallest gap with the retrained reference across all mismatch settings, often by large margins.

## Strengths

1. **Novel and well-motivated problem formulation.** The four-scenario taxonomy (all-matched, target-mismatch, model-mismatch, data-mismatch) based on decoupling the class label from the target concept is a genuine conceptual contribution. It expands the scope of class-wise unlearning to practically relevant situations where the pre-training taxonomy does not align with the forgetting request (Section 3.1, Figure 1, Table 1). This reframing is likely to influence future work in the area.

2. **Theoretical grounding connecting representation distance to forgetting dynamics.** Theorem 3.2 provides a formal bound showing that the loss-update gap during gradient ascent is proportional to representation distance between data subsets. This "gravity effect" explains why entangled representations cause spill-over forgetting and under-entangled representations cause incomplete forgetting, giving principled insight into why mismatch scenarios are challenging (Section 3.2, Eq. 2). The remarks mapping this theory to each mismatch scenario (Remarks 3.1–3.3) are concretely useful.

3. **TARF framework is well-designed to address the identified challenges.** The dynamic objective (Eq. 3) with annealed forgetting weight \(k(t)\) and selective retaining weight \(\tau(x,y,t)\) organically produces three phases (target identification, separation, retraining approximation) that directly respond to the two identified failure modes: insufficient representation and lack of decomposition (Section 3.3, Figure 4). The design is not ad-hoc but follows from the theoretical analysis.

4. **Comprehensive and convincing empirical evaluation.** TARF is evaluated across CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1k (Tables 3, 4), with multiple architectures (ResNet-18, VGG-16bn, WideResNet-50 - Figure 7). In the novel mismatch settings (target, model, data), TARF achieves the lowest Gap with the retrained reference by substantial margins (e.g., CIFAR-100 target-mismatch: TARF Gap=0.21 vs. next-best GA Gap=8.86). All individual metrics (UA, RA, TA, MIA) are reported alongside the composite Gap, enabling fine-grained assessment. Ablation studies (Figure 7) validate each design choice.

5. **Code released and practical grounding.** The code is publicly available at github.com/tmlr-group/TARF, and the paper demonstrates applicability beyond classification (Stable Diffusion concept removal, TOFU LLM unlearning), showing the framework's generality.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Model-mismatch evaluation framing needs sharper clarification.** In the model-mismatch scenario, the retrained model achieves high UA (~88% on CIFAR-10) because the superclass remains in the retaining set. The paper states this (line 260: "UA of Retrained (Ref.) in the model mismatch scenario is not equal to 0 since it is evaluated with superclass label") and defines the overall goal as approximating the retrained model. However, readers could still misinterpret "forgetting" as requiring low UA. The paper would benefit from an explicit statement that in this setting, forgetting means removing the *influence of specific training examples* (not degrading superclass accuracy), and from providing auxiliary evidence (e.g., linear-probe accuracy on subclasses, or representation similarity analysis) that the finer-grained concept is genuinely forgotten. The fine-grained Table 2 (UA-F vs UA-R) partially addresses this, but the reasoning could be foregrounded.

2. **The identification mechanism (Phase I) is heuristic and its sensitivity is not fully characterized in the main text.** TARF uses the accuracy drop from a few gradient ascent steps with a threshold \(\beta\) (e.g., top-10%) to identify false-retaining data. While the paper mentions broader explorations in the appendix and provides some ablation on \(k\) (initialized strength), the main text does not present a sensitivity analysis of \(\beta\) across datasets, model capacities, or noise levels. The robustness of this identification step — how precise/recall varies, and how much the final performance depends on getting \(\beta\) right — would help users judge the method's reliability. The paper's own open challenges section acknowledges that the gravity signal can be weaker in long-tailed or multi-attribute scenarios, which reinforces this concern.

3. **Real-world application demonstrations are too thin in the main text.** The Stable Diffusion concept removal (Figure 6) is presented with only qualitative image comparisons — no metric (e.g., CLIP score, detection rate, FID) is provided to quantify removal success or utility preservation. The TOFU results (Table 5) are dense and difficult to parse without stronger visual organization. While these are case studies rather than core contributions, strengthening them with quantitative metrics would meaningfully increase impact and help validate that the framework transfers beyond controlled classification benchmarks.

4. **The theoretical result (Theorem 3.2) is presented as a sketch.** The proof is deferred to the appendix (which is stripped), and the assumptions (Assumption 3.1: Lipschitz smoothness of \(\ell_h\)) are stated but their implications are not discussed. The bound's dependence on \(\lambda_{\max}(J_\theta)\) (largest eigenvalue of the Jacobian) is not empirically examined. While the theorem's intuitive content ("gravity" = representation distance drives forgetting spill-over) is clear and well-supported by the empirical dynamics in Figures 3 and 5(a), the formal result as presented in the main text is more suggestive than rigorous.

5. **Discussion could more explicitly acknowledge where TARF's advantage is marginal.** On the ImageNet-1k all-matched and target-mismatch settings (Table 4), TARF's Gap (3.66 and 3.97) is only marginally better than FT (3.82 and 4.02) and L1-sparse (4.48 and 5.05). This is acceptable — the paper's primary novelty is the mismatch settings — but the text could be more upfront about this rather than implying uniform improvement.

6. **Assumption about known number of false-retaining classes.** The paper assumes (line 73) that "the number of classes in \(\mathcal{D}_{un}\) belonging to the target concept is known in target mismatch forgetting." A sensitivity study where this count is mis-specified would clarify practical applicability when this information is not perfectly available.

### Trivial

- The table caption lists "RL (Toneva et al., 2018)" where RL stands for random labeling — a standard unlearning baseline — but the citation is to a paper about forgetting dynamics during training, not about random-label unlearning. This is a minor citation mismatch.
- Some notation switches between \(\mathcal{D}_{un}\) and \(\mathcal{D}_R\) without explicit reconciliation (e.g., the text defines \(\mathcal{D}_{un}\) as remaining data but then uses \(\mathcal{D}_R\) for the identified subset in Phase I).

## Nice-to-Haves

- **Quantitative metrics for the real-world demonstrations.** Adding CLIP-score-based concept removal success and FID for the Stable Diffusion experiment, and clearer structured tables for the TOFU results, would strengthen the case studies without much additional work.
- **A simple representational baseline for comparison.** Comparing the gradient-based "gravity" identification with a static k-NN or clustering baseline on penultimate-layer embeddings would clarify whether the dynamic signal is necessary or whether static distances suffice.
- **Radar plots or small multiples** showing the per-metric gaps (UA-gap, RA-gap, TA-gap, MIA-gap) separately for each method, in addition to the composite Gap, would give readers an immediate visual of where deviations are largest.

## Removed Points

The following points from the inputs were considered and removed or demoted based on the filtering rules:

- **Composite Gap metric is misleading** — *Removed.* The paper reports all four component metrics (UA, RA, TA, MIA) separately in every table (Tables 2, 3, 4). The Gap is only a summary statistic, and readers can see the full decomposition. This is a standard practice and not a flaw.
- **"The appendix may address this" criticisms about sensitivity analysis** — *Weakened to Minor.* The paper mentions robustness analysis in the appendix (which is stripped by the parser). The main-text criticism about lack of sensitivity characterization stands as Minor.
- **Formatting/style nitpicks** (notation jumps, small typo about RL) — *Demoted to Trivial or Removed.* These are at most presentation issues and do not affect the paper's contribution.
- **Missing related works** — *Removed.* Per rule: do not mention missing related works as I cannot verify their existence.
- **Criticisms questioning the existence/release status of code, datasets, or models** — *Removed.* The paper states code is publicly available at github.com/tmlr-group/TARF (line 20). All cited datasets and tools are assumed to exist.
- **"One-size-fits-all" demands for more models/datasets** — *Demoted to Nice-to-Have.* The current model zoo (ResNet-18, VGG-16bn, WideResNet-50) and dataset scale (up to ImageNet-1k) are already adequate.

## Novel Insights

Beyond the paper's own contributions, a notable insight that emerges from the reviews is the **inherent tension between the evaluation standard and the interpretation of "forgetting" in mismatch settings.** The retrained model is the standard reference, but in model-mismatch the retrained model has high accuracy on the forgetting data because the superclass remains. This means the evaluation goal shifts from "make accuracy low" to "match retrained behavior" — and this shift is often implicit. Future work on mismatch unlearning would benefit from an explicit discussion of what "forgetting" means when the taxonomy changes, and possibly from developing metrics that specifically measure the removal of fine-grained concept influence (e.g., through representation probing or example-level influence estimation) rather than just predictive accuracy.

## Suggestions

1. **Clarify the model-mismatch forgetting objective.** Add a paragraph that explicitly states: "In model-mismatch, the goal is not to reduce accuracy on the forgetting data (since the superclass remains), but to remove the influence of the specific training examples so that predictions are based only on the superclass information shared with the retaining set. This is why the retrained model is the reference, not zero UA." Supplement with representation-level analysis (e.g., linear probing on subclasses).
2. **Add a sensitivity table for the identification threshold \(\beta\).** Show precision/recall of false-retaining data selection across different quantiles (e.g., 5%, 10%, 20%) on at least two datasets, and report how the final Gap varies. This would substantially increase confidence in the method's robustness.
3. **Quantify the real-world demonstrations.** For the Stable Diffusion experiment, report a metric such as CLIP-score drop on the target concept vs. unrelated concepts, or a classifier-based detection rate. Even a single quantitative number would move this from "illustrative" to "evidence."
4. **Acknowledge the marginal cases explicitly.** In the ImageNet discussion, note that "on all-matched and target-mismatch, TARF's advantage over FT and L1-sparse is modest; the main gains are in model-mismatch and data-mismatch, which are the novel settings this paper targets."

## Score and Decision

**Calibration report:**

I retrieved anchors across three bands:
- **Weak** (avg < 3.5): Xagys9QD3T (3.00), hwXUmwJAq5 (3.00), BJfIDS5LsS (2.50), 1gqR7yEqnP (2.20)
- **Middle** (3.5–7.5): OHOmpkGiYK (5.75, our paper), SIZWiya7FE (6.00, Accept), pUOesbrlw4 (5.25, Reject), TLBPjECC5D (5.25, Reject), 7tpMhoPXrL (4.80, Reject)
- **Strong** (>7.5): 51WraMid8K (8.00), PBjCTeDL6o (8.00), gc8QAQfXv6 (9.00), EUSkm2sVJ6 (7.60)

Round-1 bracket: between approximately 4.5 and 6.5.

Round-2 anchors inside bracket: OHOmpkGiYK (5.75), pUOesbrlw4 (5.25), TLBPjECC5D (5.25), 7tpMhoPXrL (4.80), fMNRYBvcQN (6.75), HVFMooKrHX (6.60), oe51Q5Uo37 (6.75). Compared to the 5.25-level papers, this paper is stronger — it has greater novelty (new problem formulation vs. incremental application of DKVB/sparsity) and more comprehensive evaluation. Compared to the 6.75-level papers (Jogging Memory, Scalable Exact), this paper has a broader scope but less sharply focused empirical validation in the real-world case studies and a more heuristic component in the identification phase. It is closest in quality to SIZWiya7FE (Label-Agnostic Forgetting, avg 6.00, Accept), which also combines a novel problem framing with extensive experiments and has similar presentation issues. I place this paper at 6.0: above the 5.25-level papers but below the 6.75-level papers, and comparable to the 6.00 paper that was accepted.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>