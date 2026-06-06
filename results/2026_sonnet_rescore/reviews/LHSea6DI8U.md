Now I have read the paper thoroughly. Let me write the consolidated final review.

---

## Summary

STBP proposes a continual spatio-temporal forecasting (CSTF) framework combining a frozen general-purpose backbone (a frequency-domain network FreNet + Dual-stream Linear Graph Attention DLGA) with an expandable per-node Contextual Pattern Bank (CPB). The backbone is trained once and frozen; during each subsequent incremental period, only newly appended CPB rows are fine-tuned. The CPB interacts with the frozen backbone via prompt-based gating and serves as dual-stream keys in a linear-complexity graph attention. STBP achieves large accuracy gains over the best CSTF competitor on two traffic streaming datasets and modest gains on an air-quality dataset.

---

## Strengths

1. **Large and consistent MAE improvements on traffic domains**: On PEMS-Stream and CA-Stream, STBP reduces average MAE by 21.44% and 21.93% respectively over the strongest CSTF competitor EAC (Table 1: PEMS-Stream STBP 12.31 vs. EAC 15.67; CA-Stream STBP 15.77 vs. EAC 20.20). The improvements are consistent across all three forecasting horizons (3, 6, 12) and all three metrics (MAE, RMSE, MAPE), with error bars that clearly separate STBP from EAC.

2. **Ablation supports the decoupling design**: Figure 4 shows that "Our" (frozen backbone + CPB) substantially outperforms both Retrain (no CPB, scratch each period) and Online (no CPB, full fine-tune). The w/o Backbone variant shows a clear performance drop, and w/o DLGA degrades substantially. This multi-variant ablation meaningfully validates the joint importance of the backbone design and the CPB.

3. **Strong few-shot performance demonstrating data efficiency**: Table 2 (10% training data for subsequent periods) shows STBP improves over EAC by 15.8% on PEMS-Stream MAE (13.58 vs 16.13) and 18.3% on CA-Stream MAE (17.11 vs 20.94), indicating that the CPB can effectively reuse prior knowledge with very limited data.

4. **Scalable linear-complexity spatial attention**: The toy dataset experiment in Figure 8 confirms that the linear-attention STBP O(N) uses substantially less GPU memory than the quadratic variant O(N²), validating the complexity claim and supporting the scalability argument.

5. **Meaningful CPB cluster visualization**: Figure 6 shows the pattern bank evolves from a chaotic initial distribution into well-defined clusters that match temporal behavioral patterns of nodes (Clusters 1–3 with visually distinguishable flow profiles), and new nodes from later periods correctly assimilate into existing clusters. This constitutes concrete evidence for the paper's node-relevance/heterogeneity hypothesis.

---

## Weaknesses

### Fatal
None.

### Major

- **AIR-Stream results are marginal and partially reversed, with no explanation**: On AIR-Stream (Table 1), STBP achieves only a 2.35% MAE improvement over EAC (23.64 vs 24.21) compared to 21.44%/21.93% on traffic datasets. More critically, on RMSE at horizons 6 and 12, EAC *outperforms* STBP (h=6: EAC 39.63 vs STBP 39.81; h=12: EAC 44.65 vs STBP 44.97), and the average RMSE improvement is a negligible 0.07 (STBP 37.76 vs EAC 37.83), well within uncertainty intervals (±0.30 vs ±0.60). MAPE is better (6.5% improvement), making the picture inconsistent across metrics. The paper acknowledges the 2.35% MAE figure but provides zero explanation for why FreNet's emphasis on periodicity/trend stability and DLGA's dynamic correlation modeling—both central claims for handling distributional drift—fail to generalize to the air quality domain. This limits the scope of the paper's generality claims beyond traffic data.

- **Forgetting mitigation is a central claim but never directly measured**: The abstract and all four "key challenges" enumerate catastrophic forgetting as a primary target, and the conclusion states STBP "efficiently mitigates catastrophic forgetting." Yet the evaluation metric (accuracy averaged over all periods) conflates within-period accuracy and cross-period retention. A model that simply performs well in later periods due to better architecture will appear to mitigate forgetting. The paper includes no backward transfer measurement (e.g., performance on Period-1 nodes at the end of training). The ablation's Retrain/Online comparison gives indirect support, but it doesn't isolate whether the backbone *freezing* prevents forgetting or whether the backbone simply achieves better accuracy overall. For a paper that claims forgetting mitigation as a core contribution, this is a methodological gap.

### Minor

- **No w/o FreNet ablation variant despite an explicit "notable contribution" claim**: Section 5.3 states "The FreNet module also makes a notable contribution by improving computational efficiency and enhancing the extraction of stable temporal components." However, the ablation contains no "w/o FreNet" variant (only w/o DLGA is ablated). This means the claim that FreNet specifically contributes to distributional drift mitigation is asserted, not demonstrated. Adding a variant that replaces FreNet with a standard linear embedding while keeping DLGA and CPB would directly validate this.

- **Linear attention description is confusing and potentially conflated**: Section 4.3 states: "The function φ(·) denotes a random feature mapping, with Softmax used for approximation in our implementation." Random feature mapping (Performer-style kernel approximation) and Softmax are distinct approximation strategies; this sentence appears to use two different things interchangeably. The O(N) complexity claim depends on which is actually implemented. The authors defer to the appendix, but the main text should resolve this ambiguity given that it is central to the efficiency claim.

- **Attribution of advantage to freezing strategy overstated**: Section 5.2 states "lightweight prompt-based adaptation on a frozen backbone yields higher average accuracy, highlighting the benefits of dynamically tuning only a small set of parameters." However, EAC also uses a frozen backbone with lightweight adaptation, yet STBP substantially outperforms EAC. The advantage is primarily architectural (FreNet + DLGA vs. CNN/GCN), not the freezing strategy per se. This framing conflates two distinct factors.

### Trivial

- The efficiency study (Figure 8) does not report whether the O(N) linear attention approximation achieves accuracy parity with the O(N²) full-attention variant on a held-out task. A brief accuracy comparison would confirm the approximation is lossless.

---

## Nice-to-Haves

- A backbone-unfrozen + CPB variant in the ablation would close the current gap in isolating whether gains come from backbone architecture, CPB design, or the freezing strategy itself. Currently the Online variant (no CPB, fine-tune entire backbone) cannot distinguish "freezing helps" from "CPB helps."
- Reporting total parameter count growth over incremental periods (P_τ grows as N_τ × d × 3) would sharpen scalability claims for large-scale or long-horizon deployments.
- A spectral analysis of AIR-Stream vs. traffic datasets (e.g., dominant frequency components, drift patterns) would transform the unexplained AIR-Stream gap into a principled characterization of when and why STBP's frequency-domain approach is advantageous.
- The few-shot experiment setting (10% training data) is presented without articulating why this particular ratio is representative of real deployment scenarios; a brief justification of the experimental design would help.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Baseline asymmetry (GWNet/STID retrained from scratch)**: The critic argues that retraining GWNet/STID from scratch at each period is a "weak protocol" that "inflates headline improvements." However, this is explicitly the standard adopted from prior CSTF work (Chen & Liang, 2025), and the paper is transparent about it (Section 5.2). Moreover, the primary headline comparison in the paper itself is against CSTF methods, not GWNet/STID. The paper does not misrepresent these baselines as "state of the field." **Removed: standard community protocol, no misrepresentation.**

- **Eq. 9 interpretive asymmetry**: The critic notes that K and P^(2) are treated symmetrically (additively combined before multiplying V), while the text claims this "assesses the relationship between evolving input patterns and stored knowledge," implying asymmetry. This is a minor imprecision in interpretive framing. The mechanism itself is well-defined and functional; the interpretive claim is a common soft overstatement. **Removed: too minor to weight in evaluation.**

- **Strength: "bridges an important research gap" (generic importance claim)**: Removed as too generic per instructions. Only concrete, evidence-backed strengths retained.

- **Missing backward transfer metrics (framed as "not in the appendix")**: The critic mentions "the appendix presumably clarifies." Since appendices are stripped, we cannot penalize for this. What is penalized is that the main text evaluation does not include any direct forgetting measurement — retained as a Major weakness on those grounds only.

---

## Novel Insights

The most genuinely insightful observation that cuts across both reviewer perspectives is the domain-specificity of STBP's advantages: the method performs dramatically better than all competitors on periodic, high-predictability traffic data, but only marginally (and inconsistently by metric) on air quality data. This pattern is not merely a weakness to criticize — it implicitly suggests that frequency-domain stability modeling is a better fit for domains with strong, recurring periodicity (traffic) than for domains with more irregular, meteorologically-driven variation (air quality). If confirmed analytically, this would be a principled and useful finding about the scope of applicability of frequency-domain spatio-temporal representations in continual learning.

---

## Suggestions

1. Add a direct forgetting measurement: report performance on the Period-1 node subset after all T incremental periods, comparing STBP to EAC and Online. Even a single table row would ground the forgetting-mitigation claim empirically.
2. Add a "w/o FreNet" ablation (replace FreNet with linear embedding, keep DLGA and CPB) to directly validate the stated contribution of the frequency-domain module.
3. Provide a spectral characterization of the three datasets to explain why STBP's advantages are domain-specific, converting an apparent inconsistency into a strength.
4. Clarify the linear attention implementation (Eq. 4.3): specify whether φ(·) is a random feature kernel approximation (e.g., Performer-style) or a Softmax approximation, and how these achieve O(N) complexity.

---

## Score and Decision

**Originality**: The core idea — pairing a frozen, frequency-domain + linear-attention backbone with an expandable per-node parameter bank for CSTF — is a sensible and incremental but novel combination within the CSTF literature. The dual-stream CPB gating and attention integration are architecturally novel relative to EAC/TrafficStream. Score: 3/5.

**Importance**: Continual spatio-temporal forecasting on expanding urban graphs is a practically important problem with real deployment implications. 4/5.

**Claims well supported**: Traffic domain claims are well supported by consistent multi-metric results. The forgetting-mitigation claim lacks direct measurement. The FreNet contribution lacks an ablation. The air quality claim is marginal and partially contradicted by RMSE at specific horizons. 3/5.

**Soundness of experiments**: Generally solid experimental design following CSTF protocols, multi-metric, multi-horizon evaluation, multiple seeds with uncertainty. The missing direct forgetting measurement is a notable gap. 3/5.

**Clarity of writing**: Generally clear, with the main exception being the linear attention description in Section 4.3 which conflates two distinct approximation strategies. 4/5.

**Value to research community**: The model is performant, the scalability analysis is concrete, and the CPB visualization is informative. This is a useful contribution to the CSTF community. 4/5.

Overall: A technically sound paper with compelling results on its primary domain (traffic) and a coherent architectural contribution, undermined by the unexplained domain specificity on AIR-Stream, the absence of any direct forgetting measurement despite claiming it as a core contribution, and an incomplete ablation for FreNet. These are fixable gaps that prevent a confident accept in the paper's current state, but the core contributions are real and substantive.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>