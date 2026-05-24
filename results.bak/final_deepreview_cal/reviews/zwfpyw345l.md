Now let me write the final consolidated review.

## Summary

This paper proposes a hierarchical code embedding system for reinforcement learning state representation. The method processes code at three levels — token-level (transformer), function-level (GAT on AST), and module-level (attention with CDG) — and optimizes the embeddings end-to-end via policy gradient. The model is evaluated on three code-related RL tasks: code completion (PY150), program repair (ManySStuBs4J), and algorithmic problem solving (APPS), achieving improvements of +4.5 BLEU, +5.7% success rate, and +6.2% pass rate over the best baselines.

## Strengths

- **Clear architectural concept with formally specified attention mechanisms at three abstraction levels.** Equations (1)–(3) define distinct attention formulations for token-, function-, and module-level processing, and the ablation study (Table 2) quantifies that removing each level degrades performance (e.g., −6.2% for token-level, −3.6% for function-level), confirming that each hierarchical component contributes. This provides concrete evidence for the multi-level design.

- **Performance gains across three diverse code-related RL tasks.** Table 1 shows that the proposed model outperforms five baselines (Sequence Transformer, Tree-LSTM, CodeBERT, GNN-CDG, Flat-GAT) on all three tasks, with improvements of 4.5 BLEU (code completion), 5.7 percentage points (program repair success rate), and 6.2 percentage points (algorithmic solving pass rate) over the best baseline (CodeBERT). The consistency across tasks strengthens the claim that the hierarchical representation is broadly useful.

- **Ablation study that isolates the contribution of each architectural component.** Table 2 systematically removes token-level attention, function-level attention, module-level attention, and CDG edges, showing that all components make a positive contribution. The "Uniform Attention" variant (−4.5%) provides some evidence that hierarchical organization matters beyond flat attention with comparable capacity.

- **End-to-end RL-aware optimization of the embeddings.** Equation (6) specifies that the policy gradient propagates through all attention layers, which contrasts with prior approaches that learn code representations in isolation from the RL objective (as noted in the related work comparison to Stooke et al., 2021).

## Weaknesses

### Major

- **Writing quality and clarity impair method understanding.** While individual typos and formatting artifacts are not the concern, several key sentences describing the architecture are genuinely hard to parse. For example, Section 4.2 states: "The transformer part processes token GAT sequences while the one longer the GAT depends on AST AND code dependency graph (CDG) structures." The abstract and introduction contain similarly garbled constructions (e.g., "Sequential or Tele-centric analysis yet, usually these techniques are restricted to either sequential or structural aspects"). The paper credits LLM polishing (Section 9), but the resulting prose remains below the clarity standard required for a conference submission. This is not a minor style issue — it affects a reader's ability to determine what was actually implemented.

- **Critical method details are underspecified.** The paper does not concretely define how token-level representations are aggregated into AST nodes or function embeddings. Section 4.1 says "Function level attention is affected on abstract syntax tree (AST) structure, aggregating token's representation into function embeddings" but provides no mechanism. What constitutes a "module" is never defined. The Code Dependency Graph (CDG) is introduced in Section 4.4 as capturing "semantic connections between modules," but how the CDG is constructed from raw source code is not described. The equations (1)–(8) are individually standard (transformer self-attention, GAT, multi-head attention, MLP); the novelty lies entirely in how they are arranged hierarchically, and that arrangement is not described with sufficient precision to reproduce.

- **No error bars, confidence intervals, or standard deviations in any result table.** Tables 1 and 2 report only point estimates. Section 5.4 mentions that "statistical significance was tested via paired t-tests (p < 0.01)," but no p-values, confidence intervals, or variance measures are reported anywhere. Figure 2 (learning curves) shows a single trajectory per method with no indication of variability across seeds. This is a basic gap in experimental reporting, and it makes it impossible to assess whether the reported improvements are reliable.

- **MDP definitions are absent despite the paper's central RL framing.** The title and contributions center on RL state representation, but Section 5.1 describes each task only at the dataset level: "Each task was implemented as a Markov Decision Process (MDP) where states represent the current program state and actions correspond to valid code modifications or additions." The state space, action space, and reward function are not formally specified for any of the three tasks. Without these definitions, a reader cannot evaluate whether the RL formulation is sound or whether the reported task metrics (BLEU, success rate, pass rate) actually reflect the quality of the learned state representation.

- **"Prediction Error" in the scalability analysis (Figure 3) is undefined.** Section 6.6 says "we tested the model's performance on programs of varying sizes" and reports "prediction error" as a function of code complexity. Neither the quantity being predicted nor the error metric is defined. The figure also shows baselines terminating at 100–125 functions while the proposed model continues to 175; this pattern is not explained (e.g., whether baselines failed due to memory constraints or some other threshold).

### Minor

- **Ablation study is performed on only one task (program repair).** While the results are informative, generalizing the component importance to the other two tasks would strengthen the paper.

- **Attention pattern analysis (Section 6.3) is qualitative and lacks rigorous quantitative backing.** The claims about mean attention distance (2.1 edges for completion vs. 3.8 for repair) are presented without a clear methodology for computation.

- **Limitations section (7.1) is a placeholder heading with no substantive content.** The paper acknowledges limitations exist but does not discuss them.

- **The non-hierarchical multi-modal baseline is missing.** As the paper's contribution is hierarchical attention combining sequential and graph information, a baseline that uses both modalities without hierarchical organization (e.g., a transformer that concatenates graph features) would provide a sharper test of whether the hierarchy itself, rather than the presence of both modalities, drives the gains.

### Trivial

- None that remain after filtering.

## Nice-to-Haves

- An additional baseline combining sequential and graph features without hierarchical structure would help isolate whether the *hierarchy* or merely the *multi-modality* is responsible for the gains.
- RL-specific metrics such as sample efficiency curves and policy entropy over training would strengthen the connection to the RL framing.
- t-SNE visualizations (mentioned in Section 6.4) would benefit from quantitative cluster quality measures (purity, silhouette score).
- A discussion of computational cost beyond memory scaling (e.g., training time, inference latency) would aid practitioners.

## Removed Points

These points were flagged by reviewers but removed from the main review for the following reasons:

- *"Impossible to evaluate the method with confidence"* — Overstated. While the writing quality is poor, the equations (1)–(8) and Figure 1 convey the architecture. The method is partially evaluable even if underspecified in places.
- *"RL claims not supported — no RL-specific quantities"* — Partially inaccurate. Table 1 includes an "Avg. Reward" column and Figure 2 shows cumulative reward curves. The missing MDP definitions are real (kept as major), but the claim that no RL evidence exists is wrong.
- *"Cherry-picked data / suspicious baseline termination in Figure 3"* — Speculation. Baseline termination could reflect memory limits or a 20% error threshold; there is no evidence of deliberate cherry-picking.
- *Grammar/typo/style nitpicks about specific sentences* — Per the review guidelines, individual formatting and grammar issues that may be parser artifacts are removed. The overall writing quality concern is retained as a major weakness.
- *"Section 5.4 metrics listed but not reported"* — The paper lists RL metrics (cumulative reward, sample efficiency) but only partially reports them (cumulative reward in Figure 2, Avg. Reward in Table 1). This is noted but is less severe than the major issues above.
- *"No comparison with GPT models"* — The paper's baselines (CodeBERT, Tree-LSTM, GNN-CDG, etc.) are appropriate for this setting. GPT models are not designed for the RL state representation framing used here.

## Novel Insights

None beyond the paper's own contributions. The reviews largely surface standard concerns about clarity, evaluation rigor, and method specificity that the paper itself would need to address.

## Suggestions

1. **Rewrite the paper for clarity.** Many sentences describing the core method are grammatically broken or structurally confusing. This is the single highest-leverage fix: a clear description of the hierarchical aggregation pipeline is a prerequisite for any evaluation of the work.

2. **Define the MDPs formally.** For each task, specify the state representation, action space, and reward function. This is essential given the paper's RL framing.

3. **Report error bars.** Run each experiment over multiple seeds and report standard deviations or confidence intervals for all metrics.

4. **Specify the hierarchical aggregation mechanism.** Explain concretely how token representations are aggregated into function embeddings, what constitutes a module, and how the CDG is constructed from raw code.

5. **Define "Prediction Error" in the scalability analysis** and explain why baseline curves terminate earlier than the proposed model's curve.

6. **Add a non-hierarchical multi-modal baseline** (e.g., transformer + graph features concatenated, without hierarchical levels) to isolate the effect of hierarchical organization.

7. **Replace the placeholder Limitations section** with a substantive discussion of failure cases, scope constraints, and known weaknesses.

## Calibration

**Round 1 (Bracketing):** Three queries covering <3.5 (weak anchors), 3.5–7.5 (middle anchors), and >7.5 (strong anchors).

- Weak anchors (avg ~3.0): FALCON (3.0), Improve Code Generation with Feedback (3.0), D2Coder (1.67) — papers with clear writing/method deficits.
- Middle anchors (avg 4.3–5.8): CodeSage (5.75), Nova (5.60), AST-T5 (5.67), GEPCode (4.33), Coarse-Tuning (4.75).
- Strong anchors (avg 8.0): Retrieval Head (8.0), Compositional Entailment (8.0), Hölder Stability (8.0) — papers with strong clarity, theory, and evaluation.

Initial bracket: 3.0–5.0, as the paper sits between the weak rejected papers and the stronger mid-range accept/reject boundary.

**Round 2 (Narrowing):** Queries targeting 2.5–4.0 and 3.5–5.0.

- FALCON (3.0), CodeUnlearn (3.8), Interchangeable Token Embeddings (3.75) — comparable writing and method issues.
- GEPCode (4.33), AuPair (4.25), FILI (4.75), Coarse-Tuning (4.75) — papers with cleaner writing and more rigorous evaluation.

The current paper is worse than GEPCode (4.33) and Coarse-Tuning (4.75) in both writing clarity and evaluation rigor. It is comparable to or slightly better than FALCON (3.0) — the architectural idea is more concrete (equations, diagram, ablation), but the writing quality is similarly poor and the evaluation gaps are similar. The paper sits closer to 3.0–3.75 anchors than to the 4.33+ anchors.

**Final score: 3.5** — below the publication bar due to poor writing quality, underspecified method, absent error bars, undefined metrics, and missing MDP definitions. The core idea has merit, but the execution is too weak to support the paper's claims in its current form.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>