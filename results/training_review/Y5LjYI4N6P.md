Now I have thoroughly read and analyzed the paper and all reviewer inputs. Let me produce the consolidated review.

## Summary

The paper introduces progressive subnetwork training, a stagewise framework where increasingly larger random subnetworks of a model are trained over time, culminating in full-model training. The instantiation, Random Part Training (RaPT), selects random depth-wise or width-wise subnetworks and progressively increases their size across stages. The paper provides a polynomial toy analysis to motivate why subnetwork complexity should increase (not decrease) over time, offers theoretical stability analysis for stage transitions in dropping-based training, and presents BERT and UL2 experiments showing 1.2–1.33× FLOPs reduction with competitive or better quality.

## Strengths

- **First theoretical framework for dropping-based stagewise training stability**: Section 4 provides a formal analysis of loss behavior at stage transitions for dropping-based methods, showing that residual connections and layer normalization are important for stability. Theorem 1 upper-bounds the loss gap between stages in terms of a stability measure, and Lemma~1 illustrates this concretely for linear networks. This goes beyond existing work on stacking (which only studies loss preservation) by identifying conditions under which dropping-based stagewise training yields smooth transitions.

- **Principled polynomial analysis identifies why prior dropping methods underperform**: Through a controlled polynomial regression setting, the paper shows theoretically and empirically that progressive layer dropping (PLD) — which *decreases* network capacity over time — cannot learn high-order correlations in data, while RaPT's increasing-capacity schedule can. This provides a clean conceptual justification for the paper's core design choice and is a genuine conceptual contribution independent of the RaPT instantiation.

- **Empirical demonstration of real FLOPs reductions with competitive quality**: On BERT-Base, RaPT achieves 1.33× FLOPs reduction while matching or exceeding baseline quality, and is competitive with stacking approaches. On UL2-1.6B, RaPT matches baseline perplexity with 1.2× fewer FLOPs and shows improved downstream performance on QA and SuperGLUE (+1.5%). These results provide credible evidence that dropping strategies, when properly designed, can be practically useful.

- **Intriguing downstream improvement beyond perplexity**: The UL2 result — better downstream performance despite matching perplexity — suggests RaPT may induce a qualitatively beneficial training dynamic. While under-analyzed in the current paper, this observation is non-obvious and could motivate future research.

## Weaknesses

### Fatal

None.

### Major

1. **Missing comparison with stochastic depth at constant probability**: The paper's central claimed distinction from stochastic depth (Related Work, lines 201–202) is the *progressive increase* in subnetwork size. Yet no experiment compares RaPT against stochastic depth with a constant keep probability matched to RaPT's average subnetwork size at the same total FLOPs budget. Without this control, it is impossible to attribute any observed benefit to the progressive schedule specifically, as opposed to training on random subnetworks generically. This gap directly undermines the paper's core narrative that "increasing complexity" is the key innovation — the results may simply reflect the benefit of stochastic training at any fixed rate, a known technique since Huang et al. (2016). The paper compares against PLD (which *decreases* capacity) but omits the more natural constant-probability baseline.

2. **Theoretical analysis does not match the full algorithm**: Section 4 (lines 141, 150–155) analyzes a simplified two-stage variant where the first stage trains subnetworks of exactly *L*−1 layers (dropping one random layer) and the second trains the full model. The actual RaPT algorithm (lines 108–111) uses *K* stages with varying probabilities *p*ₛ, and subnetworks can be much smaller than *L*−1 in early stages — precisely where most FLOPs savings occur. The theory provides no insight into the small-*p* regime. The paper's claim that this "provides a theoretical basis" for the framework (abstract, contribution list) is overstated given the gap between what is analyzed and what is executed.

### Minor

3. **No wall-clock speedup measurements**: The paper repeatedly highlights efficiency as a motivation, claims "a novel implementation strategy that translates FLOPs improvements to wall-clock speedups" (contribution 4, line 56), and the abstract states training is sped up "up to 33%." However, all efficiency results are reported in FLOPs, not wall-clock time. For distributed training — which the paper explicitly discusses — FLOPs savings do not automatically translate to wall-clock speedup because devices must synchronize on the slowest worker. Without actual timing measurements, the practical efficiency claims remain unvalidated. This gap could be filled straightforwardly.

4. **UL2 downstream gains lack statistical rigor**: The reported 1.5% improvement on QA tasks and SuperGLUE (abstract, line 6) is presented without error bars, significance tests, per-task breakdown, or multiple seeds. The paper's own limitations section (lines 219–220) acknowledges not explaining this phenomenon. As presented, these results could reflect noise from a single baseline run or uncontrolled confounds (e.g., compute-matched comparison vs. step-matched comparison). A claim of "better inductive bias" requires stronger statistical support.

5. **Polynomial analysis to real Transformers is a conceptual step, not a validated bridge**: The polynomial setting (Section 3) cleanly illustrates why PLD fails on synthetic data. However, no experiment validates that the same mechanism (learning higher-order correlations) explains RaPT's benefits in BERT or UL2 training. The paper's claim that this "provides a strong justification" for the approach (line 49) goes beyond what the evidence supports, as the dynamics of multi-layer Transformers on natural language differ substantially from linearized polynomial regression.

### Trivial

6. The paper's framing language — "fixes their key issues" (abstract), "fundamentally addresses" (line 33) — is overly assertive for the level of evidence presented. The results show RaPT is competitive (not strictly better) and the theoretical analysis covers a simplified setting.

## Nice-to-Haves

- An ablation comparing RaPT against stochastic depth with constant *p* matched to RaPT's average subnetwork size (same total FLOPs) would directly isolate the contribution of the progressive schedule.
- Wall-clock timing measurements, particularly for the distributed training scenario discussed in the implementation section.
- Per-task breakdown, confidence intervals, and multi-seed results for the UL2 downstream evaluation.
- A bridging experiment examining whether RaPT-trained Transformers exhibit different feature learning dynamics compared to constant-probability stochastic depth training (e.g., via probing or CKA analysis).

## Removed Points

- **"Systematic misrepresentation" of stochastic depth**: The harsh critic claimed the paper "systematically misrepresents" its relationship to stochastic depth. The paper explicitly states the similarity ("RaPT is similar to stochastic depth," line 202) and identifies a factual distinction (fixed vs. increasing probability). This is appropriate scholarly practice, not misrepresentation. Removed.  
- **"Two-line change" dismissal**: The claim that RaPT is merely "a two-line change to stochastic depth" is a reductive opinion that dismisses the broader framework (multiple stages, varying fixed-sets, theoretical motivation, schedule design) without justification. Removed.  
- **Section-by-section notes about "missing the main practical challenge"**: The paper defers implementation details to a designated section (sec:efficient_raptr_impl), which is standard practice. Removed as a scope-creep complaint.  
- **Lemma 1 critique about random initialization**: The critic noted Lemma 1 analyzes random initialization, not trained networks. The lemma is explicitly presented as an illustrative example for *linear networks at initialization*, and the paper separately provides empirical verification *with trained BERT* (lines 157, Figure behavior). This is not a weakness but a deliberate structure. Removed.

## Novel Insights

The harshest critic's observation about the mismatch between the theory (two-stage, one-layer-drop) and the algorithm (K stages, small-*p* regime) is more consequential than the paper's own limitations section suggests. Most discussion focuses on the theory's strengths, but the gap means the paper essentially has *two* contributions that are not well-integrated: (a) a general polynomial argument for increasing capacity (which is clear and principled but not linked to the stability theory), and (b) a stability theory that only covers the narrowest transition (L→L, not small-p→L). The paper would be stronger if it either extended the theory or explicitly scoped the claim. This also suggests the polynomial analysis, not the stability theory, is the paper's most robust conceptual contribution.

## Suggestions

1. **Run the missing baseline**: Compare RaPT against stochastic depth at constant *p* matched to RaPT's average subnetwork size at the same FLOPs budget. This single experiment would either validate or refute the paper's central narrative.
2. **Provide wall-clock times** for the distributed training setup described in the implementation section, even as a supplementary table.
3. **Strengthen statistical reporting**: Report UL2 downstream results with standard deviations across ≥3 seeds, per-task breakdown, and significance tests.
4. **Bridge the theory-practice gap**: Either extend the stability analysis to general *p* (not just L−1 subnetworks) or clearly scope the theoretical claims to the two-stage dropping-one-layer setting.
5. **Tone down overclaims**: Replace "fixes their key issues" with "addresses limitations of" and "provides a theoretical basis" with "provides theoretical analysis for a simplified setting."

## Score and Decision

The paper presents a conceptually interesting framework and has genuine analytical contributions (polynomial analysis, stability theory). However, the experimental validation has a critical gap: the central claimed innovation — progressive increase in subnetwork size — is never isolated from the simpler alternative of constant-probability stochastic depth. Combined with missing wall-clock validation and under-supported downstream claims, the evidence does not currently support the paper's strong narrative. A revised version that runs the missing baseline, provides wall-clock measurements, and strengthens statistical reporting could be competitive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>