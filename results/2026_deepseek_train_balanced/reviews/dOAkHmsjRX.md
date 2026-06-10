## Summary

This paper argues that online continual learning (CL) evaluations are misleading because they control for epoch count and episodic memory size without accounting for actual per-iteration computation (FLOPs) or total storage (models, logits, replay). The authors propose a total-budget evaluation protocol (fixed FLOPs and total bytes) and contribute a method—aL-SAR—with two components: (1) adaptive layer freezing that selects which layers to freeze per batch by maximizing Fisher Information per computation, and (2) similarity-aware retrieval that biases training toward under-used samples via discounted use-frequency and class-wise gradient similarity. Experiments on CIFAR-10/100, CLEAR-10/100, and ImageNet-1K show that many high-profile methods trail behind simple Experience Replay under fair budgets, while aL-SAR consistently outperforms baselines.

## Strengths

- **The total-budget evaluation framework is a genuine and overdue contribution.** The paper identifies concretely that "same epoch" and "same episodic memory size" do not constitute fair comparisons when methods differ substantially in per-iteration FLOPs (e.g., MIR requires ~4× the computation of ER) and in auxiliary storage (logits, model copies). The teaser (Fig. 1) and the comprehensive Table 1 demonstrate that rankings reverse under fixed FLOPs+bytes, which should meaningfully affect how the community designs and evaluates CL methods. This contribution stands independently of the proposed method.

- **Similarity-Aware Retrieval (SAR) provides a computationally efficient alternative to expensive retrieval strategies.** Unlike MIR (4× computation) and ASER (3×) which require multiple additional forward/backward passes, SAR uses discounted use-frequency and class-wise gradient similarity obtained for free from training gradients (Section 3.2). The ablation (Table 5) shows SAR alone boosts Vanilla from 60.76→64.60 AUC on CIFAR-10 (+3.84 points) with negligible extra FLOPs (163.74→171.94). This directly supports the claim that SAR accelerates per-iteration learning without nullifying computational savings.

- **Adaptive layer freezing (aL) achieves substantial FLOPs reduction with minimal accuracy loss.** Table 3 shows aL achieves 14.6% (CIFAR-10) and 17.0% (CIFAR-100) FLOPs savings with accuracy statistically indistinguishable from the no-freezing baseline, while prior freezing methods (REMIND, PTLF, EGERIA) either degrade accuracy significantly or freeze negligibly. The MLLM application (Table 4) demonstrates transferability beyond CL, with ~12% FLOPs savings on LLaVA-1.5-7B without degradation.

- **The ablation study cleanly separates the contributions of each component.** Table 5 shows that SAR is the primary accuracy driver while aL provides FLOPs savings with negligible accuracy cost. The paper honestly reports that adding aL to SAR slightly reduces accuracy (64.60→64.38) while substantially reducing FLOPs (171.94→146.80)—exactly the expected computation–accuracy trade-off, not a "free lunch." This transparency strengthens the paper.

## Weaknesses

### Major

- **ImageNet-1K results for the Disjoint setup lack reported variance, making the small margins uninterpretable.** The paper reports (line 275) that ImageNet uses a single run ("due to computational cost") and provides no standard deviations. In the Disjoint setup, aL-SAR achieves A_AUC=45.08 vs. EWC at 44.17 and ER at 44.13—margins under 1 percentage point. Without any measure of variance, the reader cannot assess whether this difference is meaningful or noise. The paper states it conducts a Welch's t-test (line 276), but the absence of any reported uncertainty for these numbers undercuts the claim that aL-SAR "outperforms" baselines on this specific setup. The Gaussian setup on ImageNet has larger margins (33.94 vs. next best 27.65) and is more persuasive; this weakness is specific to the Disjoint claim.

- **The Fisher Information framing as "information gained per computation" has theoretical gaps that the paper does not address.** The paper defines information (I) via trace of the diagonal empirical Fisher Information (Eq. 3) and treats FI as a measure of "information that each layer gains from data." However, the Fisher Information at the current parameters measures expected curvature (or gradient variance), not information *gained* in a batch—these are related but not identical concepts. More critically: (a) the diagonal empirical Fisher approximation is known to have pathologies (Kunstner et al., 2019) that the paper does not discuss despite citing closely related FI approximations; (b) the two terms in the Batch Freezing Criterion (Eq. 7)—batch-specific FI loss and expected future FI gain scaled by saved FLOPs—are measured on different scales (batch vs. global expectation), and the paper gives no argument that they are commensurable; (c) the conversion from global FI to batch-specific FI (line 193) is referenced to the appendix but not justified in the main text. The method works empirically, which is sufficient, but the paper over-claims a principled information-theoretic foundation where a heuristic framing would be more accurate.

### Minor

- **The paper lacks a limitations discussion.** Neither the conclusion (Section 5) nor any other section discusses limitations or boundary conditions of the approach. Given that the paper proposes both a new evaluation paradigm and a new method, this is a notable omission. Examples of limitations worth acknowledging: (a) the quadratic scaling of class-wise similarity tracking with the number of classes (the paper notes the ~10¹² sample-pair problem in line 235 but does not report actual overhead); (b) reliance on gradient access, which may not be available in all settings; (c) the fact that baseline methods were designed and hyperparameter-tuned under the conventional (non-FLOPs-constrained) regime, which could disadvantage them under the new evaluation.

- **The MLLM experiment only tests aL, not SAR or the full aL-SAR, in a non-CL setting.** Table 4 shows that aL saves ~12% FLOPs on LLaVA-1.5-7B fine-tuning without accuracy degradation. This is a useful demonstration of generality, but it does not directly support the CL claims. The paper should clarify this more explicitly.

### Trivial

None.

## Nice-to-Haves

- Clarify whether any baseline hyperparameters were re-tuned under the total-budget regime. Even a brief statement acknowledging this limitation would strengthen the benchmarking contribution.
- Report at least the range across seeds for ImageNet-1K, even if full standard deviations are costly to compute, to make the Disjoint setup claim evaluable.
- Discuss the known limitations of the diagonal empirical Fisher approximation (Kunstner et al., 2019) and justify why it is still a useful signal for the freezing criterion despite these limitations.

## Removed Points

Several criticisms from the harsh reviewer were removed or downgraded after verification against the paper:

- **"FI is not a measure of information gained"** — The paper cites literature (durant2021determining, desjardins2015natural, ollivier2015riemannian) that uses FI as an information measure. While the mapping is imperfect, it is not the paper's invention and is standard in certain contexts. The remaining concern (commensurability of BFC terms) is kept as a Major weakness.
- **"Baselines were not re-tuned for the new budget regime"** — The paper's core contribution is to show that rankings change under equal total budgets. The paper does not claim baselines were optimized for the new regime, and re-tuning baselines for a new objective would introduce its own confounds. The concern is acknowledged in Minor weaknesses as a limitation the paper should discuss, not a fatal flaw.
- **"Batch-specific FI conversion not explained in main text"** — The paper references the appendix (Sec. 3.1, line 195), which exists in the original submission but was stripped by the PDF parser. This is not an author error.
- **"Temperature sensitivity only in appendix"** — The appendix exists in the original submission; the parser strips all such content. Not an author error.
- **Strength Finder's claim that BFC "formally maximizes information gained per computation"** — Partially conflicts with the verified FI-theoretical weakness. Kept as a strength because the formal derivation follows from the paper's definitions; the weakness concerns whether the proxy (FI) is the right measure, not whether the derivation is internally consistent.

## Novel Insights

The most insightful observation from the reviews is how the ablation cleanly reveals that the two components of aL-SAR serve fundamentally different roles: SAR drives accuracy (Vanilla 60.76 → +SAR 64.60), while aL reduces FLOPs (Vanilla 163.74 → +aL 142.23) at minor accuracy cost. When combined (+aL & SAR), aL-SAR achieves 64.38 AUC with 146.80 TFLOPs—slightly lower accuracy than SAR alone but far fewer FLOPs. This decomposition suggests the method's total-budget advantage comes primarily from SAR making better use of each iteration, while aL converts saved FLOPs into additional training iterations within the budget. The paper's contribution is thus more about intelligent retrieval (SAR) than about principled freezing (aL), which the FI-based framing somewhat obscures.

## Suggestions

1. Add a limitations paragraph discussing the diagonal empirical Fisher approximation, the class-wise similarity scaling, and the baseline tuning issue.
2. Report at least the seed range (min–max) for the ImageNet-1K Disjoint results, or explicitly state the Welch's t-test outcome for those comparisons.
3. Consider reframing the FI-based freezing criterion as an empirically motivated heuristic rather than a theoretically principled information-maximization scheme. The empirical support in Table 3 is strong enough to stand on its own.
4. Disambiguate the MLLM experiment: explicitly note that only aL (not SAR) was tested, and that it is not a CL setting but a demonstration of transferability.

## Score and Decision

This paper makes a genuine contribution: the total-budget evaluation framework addresses a real and overlooked gap in online CL evaluation, and the aL-SAR method is empirically effective across multiple datasets and setups. The weaknesses—particularly the missing error bars for ImageNet-1K Disjoint and the loose theoretical justification of the FI-based freezing—are real but neither fatal nor structural. They are addressable in a revision. I recommend acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>