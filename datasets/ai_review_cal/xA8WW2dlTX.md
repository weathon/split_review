- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 5, 3, 5, 3
Here is my consolidated review.

---

## Summary

This paper proposes ICDA, an LLM-based agent for interactive causal graph refinement. The method maintains uncertainty estimates for every potential edge, selects the most uncertain edges for binary feedback ("interventions"), and then uses the LLM to locally update edge predictions and confidences for edges adjacent to each intervened edge. Experiments on eight real-world causal graphs (8–30 variables) show ICDA outperforms random selection by up to 0.5 F1 score, and ablations isolate the contributions of uncertainty-based selection and local prompting.

---

## Strengths

1. **Consistent empirical advantage across diverse graphs.** Figures 2–3 show ICDA outperforming all baselines on seven of eight graphs, achieving average rank 0 (best) across all timesteps. The advantage holds on both acyclic and cyclic graphs, including the highly cyclic Arctic sea ice and transcription factor graphs (lines 132–141, 185).

2. **Thorough ablations isolate each component's contribution.** Figure 4 decomposes improvements into those from direct intervention feedback vs. local LLM updates, showing updates dominate early and interventions sustain later gains. Figure 5 confirms that removing either confidence-based selection or local prompting degrades performance to near-random (lines 150–169).

3. **Memorization control via a post-training-cutoff graph.** The paper tests on a graph published July 2024 (Zhu et al., 2024), after Llama-3-70B's training cutoff, and shows ICDA still outperforms baselines (Figure 8, lines 174–185). This is a genuine effort to address contamination concerns.

4. **Robust recovery from poor initial predictions.** On graphs where zero-shot LLM F1 < 0.2 (Asphyxia, Neuropathic pain), the method still converges to correct structure (line 132), demonstrating the pipeline does not depend on good initial domain knowledge.

5. **No DAG/acyclicity assumption required.** The method operates on general directed graphs, avoiding a common restriction in classical causal discovery (lines 28, 43, 185), which is validated by strong results on cyclic graphs.

6. **Local vs. global prompting insight.** The ablation showing global updates (full graph in context) fail while local updates succeed (lines 164–169) is a practical finding about LLM limitations that the paper acknowledges and builds on.

---

## Weaknesses

### Fatal

None. The core claims (ICDA improves graph predictions via uncertainty-driven selection and local updates) are supported by the experimental evidence within the paper's defined setting.

### Major

1. **Misaligned "intervention" model.** The paper defines an intervention on edge \((X_i,X_j)\) as "an operation revealing the ground truth label \(l_{i,j}\)" (line 45). This is an oracle query that returns a binary yes/no answer about edge existence, not a causal intervention in any standard sense. In real causal discovery, intervening on a variable sets its value and requires statistical inference to determine edge presence from observed downstream effects. The paper claims this abstraction "could correspond to" do-operations or instrumental variables (line 45), but this is a stretch — no standard intervention directly reveals edge labels. The experimental setup therefore evaluates *active learning for binary edge classification under an oracle*, not *interactive causal discovery under realistic interventions*. While the method itself may be sound, the framing overclaims the contribution to causal discovery.

### Minor

2. **Baselines are too narrow to establish significance.** The only nontrivial baselines are random selection, a "Direct LLM" variant, and a static-confidence variant — all are ablated versions of the proposed method. No comparison is made to simple active-learning heuristics (e.g., uncertainty sampling with a logistic regression on variable-embedding features) that would test whether the LLM's confidence estimates drive the improvement or whether any uncertainty-based policy would work. (A comparison to causal-structure-learning intervention-selection methods such as Hauser & Bühlmann (2014) or Squires et al. (2020) would be even stronger, though those methods operate on a different input modality — observational data — making direct comparison non-trivial.)

3. **Memorization analysis is not fully conclusive.** The paper claims the 2024 graph is "guaranteed to be memorization free" because the model finished training in 2023 (line 174). However, individual edges in the transcription factor graph correspond to well-documented biological relationships (e.g., a specific TF→target-gene regulation) that are likely present in the pre-training corpus. The graph *structure* is novel, but *edge-level* knowledge could be memorized from the scientific literature. A definitive test would require synthetic graphs with fictional variable names.

4. **Small models (8B) underperform random baseline** (Figure 6, lines 171–172). The paper notes this but does not seriously discuss the limitation: the method requires strong reasoning capabilities available only in large (70B) models, which limits practical applicability. This is particularly relevant because the local update procedure calls the LLM repeatedly per round.

### Trivial

5. **F1 is the sole evaluation metric** (line 51–57). For edge-classification tasks with imbalanced edge ratios, precision-recall curves or AUROC would provide a more complete picture.

6. **No error bars or confidence intervals** on any plot. The paper states results are averaged over five independent runs (line 130) but does not show variance, making it impossible to assess statistical significance of the reported improvements.

7. **The specific values of \(R\) (rounds) and \(I\) (interventions per round)** used in experiments are not stated in the main text. The x-axis is "% of edges intervened" which conflates different combinations of rounds and per-round interventions.

8. **Ethics statement is generic** (line 194) and does not address domain-specific risks, e.g., how biased edge predictions in a scientific domain could mislead downstream causal inferences.

---

## Nice-to-Haves

- A reframing of the contribution as "active learning for LLM-based edge prediction with an oracle query model" rather than "interactive causal discovery" would better align the paper's language with its actual experimental setup.
- A more rigorous memorization test using synthetic graphs with invented variable names.
- Cost/feasibility analysis for graphs >30 variables: the quadratic cost of local prompting per round is mentioned (line 169) but never quantified.
- Simple non-LLM uncertainty-sampling baseline (e.g., logistic regression on variable-name embeddings) to isolate whether the LLM's confidence estimates are the real driver of gains.

---

## Removed Points

*These points were flagged in reviews but are removed here with justification:*

- **"Seven vs. eight graphs inconsistency"** — Removed. The abstract says "eight" (7 main + 1 memorization test graph, total 8). The Results section says "seven" for the main experiments (line 124), then separately introduces the 8th memorization graph (line 174). This is consistent, not an error.
- **"Sharma & Kiciman 2020 reference missing"** — Removed. The reference section is stripped by the parser; the reference exists in the original submission.
- **"Missing prompt structures (Appendix B)"** — Removed. The appendix is stripped by the parser; it exists in the original submission.
- **"No comparison to Hauser & Bühlmann 2014, Squires et al. 2020" as a required baseline** — Weakened to a nice-to-have. These methods require observational data, a different input modality from LLM semantic metadata, so direct comparison is not straightforward.
- **"Global updates failing is a practical failing"** — Removed. The paper already acknowledges this (line 169) and uses it to motivate the local update strategy.
- **"The LLM cannot handle full graph in context"** — Already stated by the paper (line 169) as the motivation for local prompting. Not a weakness.
- **"Pure formatting/style nitpicks"** — Removed per rules.

---

## Novel Insights

The reviews surface a point that the paper itself does not fully engage with: the local update strategy depends on the LLM's ability to reason about *local graph structure* (edges incident to a single variable), which is a fundamentally different capability from reasoning about the full graph. The fact that 8B models fail at this local reasoning (Figure 6) suggests that the required capability — using a single edge label to infer neighboring edges — is not trivial and emerges mostly at larger scales. This creates a tension: the method is designed to be scalable (local updates avoid context limits), but the LLM capability required for those local updates may not scale down to smaller, cheaper models. This observation parallels findings in other LLM-agent settings where local reasoning seems easy but actually demands substantial model capacity.

---

## Suggestions

1. **Reframe the "intervention" as "edge query" or "oracle query"** throughout the paper to accurately reflect what the method does. This would eliminate the most significant framing gap without changing any experiments.
2. **Add a simple non-LLM uncertainty baseline** (e.g., logistic regression or random forest on variable-name embeddings/descriptions predicting edge existence, selecting by predictive uncertainty) to test whether the LLM's confidence calibration is the real driver of improvement.
3. **Add error bars** (std. deviation over 5 runs) to Figures 2, 4–8 to support significance claims.
4. **State \(R\) and \(I\) values explicitly** in the experimental setup section.
5. **Discuss the limitation** that 8B models underperform random, and reflect on what capability this implies is necessary for the local update strategy.

---
