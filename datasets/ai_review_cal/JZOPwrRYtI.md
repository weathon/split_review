- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5, 5
Now I have enough information to write the final consolidated review. Let me compose it.

## Summary
The paper identifies "temporal clustering" — a pattern where node interactions occur in bursts — as a prevalent property across real-world temporal graphs. Building on this observation, the authors propose TG-Mixer, a lightweight model that (1) samples the most recent 1-hop historical links to preserve recent interaction rhythm patterns, and (2) introduces a silence decay mechanism that penalizes nodes' long-term inactivity. Extensive experiments on 7 datasets against 9 baselines show TG-Mixer achieves state-of-the-art performance with faster convergence and significantly lower computational cost. The paper also demonstrates that the silence decay mechanism can be plugged into existing sequential TGNs to boost their performance.

## Strengths
1. **Empirical discovery of temporal clustering as a prevalent pattern**: Section 3 provides both macro-level (across the entire timeline, Figure 3a) and micro-level (over individual timestamps, Figure 3b) analyses across multiple real-world temporal graphs, convincingly showing that truly existing interaction nodes consistently have smaller inter-event times than randomly sampled pairs. This data-driven observation is well-motivated and provides a clear inductive bias for model design.

2. **Silence decay mechanism is novel, interpretable, and effective**: Equation (9) defines a clean decay mechanism based on inter-event times, and Figure 6 visualizes that the resulting decay coefficients are highly discriminative between positive and negative links. The ablation study (Table 5, row 6) confirms that removing this component causes substantial performance degradation across all datasets.

3. **State-of-the-art performance with strong efficiency advantages**: Tables 1 and 8 show TG-Mixer outperforms all nine baselines on all seven datasets in both transductive and inductive settings. Table 2 and Figure 5 further demonstrate that it achieves this with significantly less training time, faster convergence, and fewer parameters — supporting the claim that explicit temporal clustering modeling yields both effectiveness and efficiency.

4. **Temporal clustering boosts existing TGNs**: Table 3 demonstrates that adding the silence decay mechanism to three existing sequential TGNs (TCL, GraphMixer, DyGFormer) improves their performance, especially on datasets with strong temporal clustering (LastFM, Flights). This shows the finding's general utility beyond the proposed architecture.

5. **Solid ablation study**: Table 5 systematically ablates the token mixer, temporal mixer, information mixer, and silence decay mechanism, providing clear evidence for each component's necessity.

## Weaknesses

### Fatal
None.

### Major
1. **Absence of variance/uncertainty reporting across all main results**: All reported results in Tables 1, 8, 9, 10 are single AP or AUC-ROC values with no standard deviations, confidence intervals, or statistical significance tests. On Wikipedia, TG-Mixer achieves 98.53% AP versus 98.33% for the second-best baseline — a difference of 0.2 percentage points. Without any measure of variance, the reader cannot assess whether these improvements are reliable or due to random seed/run variation. Given that the paper claims state-of-the-art performance, this is a significant evidential gap. The paper mentions "a single run" for training time (Table 2 caption), suggesting only one run may have been performed for main results. Reporting mean and standard deviation over multiple random seeds (at least 3–5) is a non-negotiable standard for a paper making a strong SOTA claim.

2. **Incomplete specification of the rhythm vector update mechanism in the main text**: The paper states that the temporal mixer fulfills two objectives, one of which is "updating the rhythm vector for the following timestamp t'" (lines 108–110). However, Equation (9) only shows the computation of a per-node decayed version (C_u,decay^t), not how the global C_rhythm^t is actually updated to C_rhythm^(t+1). The "information mixer" is mentioned as handling part of this (line 113), but no equations or algorithm are provided in the main text for how it combines the rhythm vector and token-mixed output to produce the updated global vector or the final node representation. While these details may reside in the stripped appendix (Section C is referenced multiple times), the main text as presented is incomplete on a core component of the method. This gap makes it difficult for readers to fully understand or reproduce the method from the paper alone.

### Minor
3. **Negative sampling construction in empirical analyses may inflate the observed clustering difference**: In Section 3, negative links for the empirical analysis are constructed by substituting *both* interaction nodes with randomly sampled nodes (line 57). This means the negative pair consists of two nodes that have no direct connection at that time and may not have interacted recently with *anyone*. A standard practice in temporal link prediction evaluation is to keep one node real and swap the other. The current construction likely amplifies the inter-event time difference between positive and negative pairs, making the temporal clustering signal appear stronger than it would be under a fairer baseline. This does not affect the TG-Mixer model itself (which uses standard negative sampling during training), but it weakens the empirical motivation in Section 3.

4. **Global rhythm vector design choice lacks justification and ablation**: The rhythm vector C_rhythm^t is a single vector shared globally across all nodes (line 106–108), implicitly assuming that interaction rhythms are coherent across the entire graph. However, the paper's own Figure 3 shows that different nodes in the same dataset exhibit varying burstiness patterns. The paper does not compare this global design against per-node rhythm vectors (initialized per node, updated at their interaction timestamps), nor does it provide justification for why a shared vector would suffice. If the global version matches or outperforms per-node, that would be a notable finding; if per-node is better, the paper should adopt it. This is a non-trivial design decision that should be ablated.

5. **Framing overstates the gap relative to prior work**: The paper claims existing TGNs "overlook the potentially heuristic, realistic patterns inherent in the temporal correlations between interactions" (line 18) and fail to capture "interaction rhythms." However, many existing methods (e.g., TGN, JODIE, TGAT, attention-based models) do capture recency and temporal dynamics through time encoding, memory mechanisms, and temporal attention. The novelty is not that temporal patterns were entirely overlooked, but that the paper explicitly models temporal clustering with a dedicated, lightweight mechanism and demonstrates its sufficiency. The framing should be more precisely scoped.

6. **Sensitivity of the decay function and T_max is not analyzed**: The decay function g(s_u^t) = 1 - exp(-2·s_u^t / T_max) uses T_max as the maximum inter-event time over the entire dataset. This makes the decay scale sensitive to the dataset's time span and potentially to outlier nodes with very long inactivity periods. The paper does not analyze how the performance changes with different decay functions (e.g., linear decay) or with different normalizations of T_max.

### Trivial
None.

## Nice-to-Haves
- **Analytical complexity analysis**: The paper claims efficiency but only reports wall-clock time and parameter count. An O-notation complexity analysis for a single prediction would strengthen this claim.
- **Limitations discussion**: The conclusion mentions extending to other tasks but does not discuss when TG-Mixer might fail (e.g., datasets where temporal clustering is weak, or where long-range historical dependencies matter).
- **Comparison against a per-node rhythm vector variant** in the ablation study would deepen the paper's own analysis.

## Removed Points
These points from the reviewers are flagged to be removed — treat them with caution:

1. **Token mixer/MLP-Mixer architecture mismatch** (Harsh Critic, "token mixer" note): The criticism that the paper lacks channel mixing from the original MLP-Mixer misunderstands the paper. The paper says "we follow Tolstikhin et al. (2021) and **apply a token mixer**" — it does not claim to implement the full MLP-Mixer architecture. It implements token mixing specifically, which is clearly described in Equation (8). This is a strawman.

2. **"Section 5.4 neighbor selection finding is expected"** (Harsh Critic): The paper is not claiming this as a novel discovery; it is an ablation validating that its specific design choice (recent sampling) is sound. Criticizing it as "not novel" is applying the wrong standard to an ablation analysis.

3. **"Section 5.3 boosting method is unclear from main text"** (Harsh Critic): The paper explicitly states "detailed implementations can be found in Section C" (line 265). Since the appendix was stripped by the parser, this is not a valid criticism of the paper as submitted.

4. **Strength Finder's generic/superficial claims**: All identified strengths were verified against the paper and found to be specific and evidence-supported. None were removed.

## Novel Insights
The reviews surface one notable observation beyond the paper's own contributions: the paper's central inductive bias — that temporal clustering is globally coherent enough to be captured by a single shared rhythm vector — is simultaneously its most interesting design hypothesis and its least tested assumption. The global rhythm vector is a clever way to minimize parameter count and enforce regularization, but it runs counter to the paper's own empirical evidence of heterogeneous node burstiness. Testing this assumption (global vs. per-node rhythm vectors) would either validate a genuinely novel finding (that temporal clustering patterns are graph-level rather than node-level) or reveal a clear path to improvement. This tension is worth highlighting but does not undermine the paper's core contribution.

## Suggestions
1. **Report mean and standard deviation over multiple runs** (at least 3–5 random seeds) for all main results, and include a statistical significance test (e.g., paired bootstrap) for the comparison against the strongest baseline.
2. **Provide the full specification of the rhythm vector update** — either move it from the appendix to the main text or add an algorithm box in Section 4 showing how C_rhythm^t transitions to C_rhythm^(t+1) through the information mixer.
3. **Add an ablation comparing global vs. per-node rhythm vectors** to justify or modify this design choice.
4. **Rerun the empirical analysis in Section 3 with a fairer negative construction** (one node fixed, one swapped) to verify that the temporal clustering signal remains strong and quantify the difference.
5. **Add a brief limitations section** discussing scenarios where temporal clustering might be weak and TG-Mixer may underperform.
