Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper formalizes the task of abductive logical reasoning over knowledge graphs — given an observation set of entities, find a logical hypothesis (in disjunctive normal form) that best explains them by maximizing Jaccard similarity between the observation and the hypothesis's conclusion on the KG. The authors propose a generative approach: (1) sample hypothesis-observation pairs from the KG, (2) train a transformer (encoder-decoder or decoder-only) via supervised learning to generate hypotheses from observations, and (3) refine the model using Reinforcement Learning from Knowledge Graph feedback (RLF-KG), where the reward is the Jaccard between the observation and the generated hypothesis's conclusion on the training KG. Experiments on FB15k-237, WN18RR, and DBpedia50 show that RLF-KG consistently improves Jaccard over supervised-only training, and the generative models are orders of magnitude faster than brute-force search.

## Strengths

1. **First principled formalization of abductive logical reasoning on KGs.** Section 2 provides a rigorous problem definition: hypotheses in disjunctive normal form with existential quantifiers, conjunction, disjunction, and negation; conclusions drawn on a KG; and the Jaccard objective. This carves out a clear and underexplored research direction distinct from deductive query answering and rule mining.

2. **Generative approach bypasses the combinatorial explosion of search.** By framing hypothesis search as conditional generation, the method avoids enumerating the exponential hypothesis space. Table 5 validates this concretely: inference takes <1 second for generative models versus ~2.2×10^5 seconds (≈2.5 days) for brute-force search on FB15k-237.

3. **RLF-KG consistently improves hypothesis quality over supervised training alone.** Table 3 shows that RLF-KG boosts Jaccard across all three datasets and both architectures — e.g., on FB15k-237, from 0.445 to 0.526 (encoder-decoder) and from 0.351 to 0.478 (decoder-only). This is the paper's strongest empirical result and directly supports the central claim that KG feedback improves abductive reasoning.

4. **Ablation on structural reward (Table 4) informs reward design.** Adding a SMATCH-based structural reward to RLF-KG yields comparable or slightly worse Jaccard than using KG-feedback alone, supporting the paper's motivation that structural similarity to a reference hypothesis is not the right objective for abductive reasoning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The search baseline is underspecified.** Section 4.6 says "we introduce a brute-force search algorithm" but never describes it — how the search space is defined, whether it enumerates all 13 hypothesis types, what graph it searches over, or how many candidates it considers per observation. This makes the comparison in Tables 5–6 difficult to interpret. The paper should document the search procedure so readers can assess whether the comparison is fair and what assumptions the baseline makes.

2. **"State-of-the-art" is an overclaim given the evaluation setup.** The abstract claims "state-of-the-art results" but the only competitor is a single brute-force search algorithm. Since this is a new task, there are no prior methods to be "state-of-the-art" relative to. The claim should be removed or qualified (e.g., "outperforms the search-based baseline").

3. **The detokenization process is not described.** Section 3.2 mentions "we recover the corresponding hypothesis H through the de-tokenization process" but never explains how the token sequence is mapped back to a valid logical expression. This is needed for reproducibility.

4. **No discussion of hypothesis validity or filtering.** The paper does not state whether generated token sequences can produce invalid logical expressions (e.g., unbalanced parentheses, out-of-vocabulary relations/entities), how often this occurs, or how such cases are handled in the metrics. This is a relevant concern for a generative approach to logical form generation.

5. **Several RL hyperparameters are unreported.** The paper mentions using PPO with dynamic KL penalty adjustment (Ouyang et al., 2022) but does not report the number of PPO steps, rollout batch size, learning rate for the RL stage, or the target KL divergence. These affect reproducibility.

### Trivial

1. **No error bars or variance reporting.** All metrics in Tables 3, 4, and 6 are point estimates. Given the sample sizes, confidence intervals or standard deviations would help assess reliability.

2. **The pre-defined ordering of observation tokens is not specified.** Section 3.1 says tokens are "sorted ... in a pre-defined order" but does not state what that order is (alphabetical? by frequency?). This is a minor implementation detail.

3. **Figure 6 caption is ambiguous.** It says "the curve of the reward values of RLF-KG training over three different datasets" but does not specify which architecture the curves belong to.

## Nice-to-Haves

- **Correlation analysis between training-graph and test-graph Jaccard.** The RLF-KG reward uses training-graph Jaccard as a proxy for the true objective on the hidden graph. The paper acknowledges this approximation but does not analyze how well the proxy correlates with the true objective (e.g., a scatter plot on validation data). Such analysis would strengthen the justification for RLF-KG.

- **Qualitative analysis of generated hypotheses.** Showing a few concrete examples with the gold hypothesis, supervised-only output, and RLF-KG output would give readers intuition about what "better explanation" means beyond aggregate Jaccard scores.

- **Discussion of why certain hypothesis types (2u, up, 3i) yield very low Jaccard scores.** Understanding whether the model fails to generate structurally correct hypotheses for these types or whether the hypotheses are correct but KG incompleteness hurts the metric would help target future improvements.

## Removed Points

- **"Cannot deal with complex hypotheses" claim not demonstrated** — REMOVED because Table 5 provides evidence: brute-force search takes 2.2×10^5 seconds (≈2.5 days) on FB15k-237, which directly supports the claim that search is impractical for complex hypotheses. The critic misread this.

- **RLF-KG reward proxy is a structural gap** — DOWNGRADED from "critical issue" to Nice-to-Have. The paper explicitly acknowledges this is an approximation ("serves as an approximation, with no information leakage"). The core claim (RLF-KG improves over supervised training) is validated on the test graph, which uses ground-truth hidden edges. The proxy concern is secondary.

- **Per-type sample imbalance** — MOVED to Nice-to-Have. The imbalance is reported in Table 2 and is an inherent property of the data; it does not invalidate the results.

- **Missing related works** — REMOVED per instructions (cannot confirm existence of external sources).

- **Formatting/style nitpicks** — REMOVED per instructions (parser artifacts).

## Novel Insights

The most useful insight emerging from this review is that the paper's main strength — the RLF-KG improvement over supervised training (Table 3) — and its main weakness — the underspecified search baseline — operate at different levels. The RLF-KG vs. supervised comparison is internally valid and well-controlled; it shows that optimizing for KG feedback (Jaccard on the training graph) produces better explanations than optimizing for structural similarity to a reference hypothesis. This finding stands independently of the search baseline comparison. The search baseline comparison, by contrast, is handicapped by unspecified enumeration details and the fact that generative methods use learned patterns while search is blind. A more informative comparison would be a beam-search variant constrained to the same 13 hypothesis patterns, which would isolate the benefit of neural generation from the effect of RL.

## Suggestions

1. **Remove or qualify the "state-of-the-art" claim** in the abstract and conclusion; replace with a factual description of what was compared (e.g., "outperforms the search-based baseline on three KGs").
2. **Document the brute-force search algorithm** in full: hypothesis enumeration space, search graph (training vs. test), candidate count, and the computational assumptions behind it.
3. **Describe the detokenization procedure** — how a sequence of tokens is deterministically mapped back to a logical expression, and how invalid sequences are handled.
4. **Report PPO hyperparameters** (number of steps, rollout batch size, RL learning rate, target KL).
5. **Add error bars** to the main result tables (standard deviations or confidence intervals over multiple seeds or bootstrap samples).

## Score and Decision

**Originality:** The task formulation is novel. The generative approach + RLF-KG pipeline is a sensible first solution, though each component individually follows existing methodology (supervised seq2seq + PPO with KL penalty). The contribution is in the combination and the task framing.

**Importance of research question:** Abductive reasoning on KGs is a meaningful and underexplored problem with practical applications. The paper opens a new direction.

**Claims support:** The central claim — RLF-KG improves over supervised training — is well-supported by Table 3. The "state-of-the-art" claim is overstated. The efficiency advantage over search is well-supported.

**Soundness of experiments:** Reasonable evaluation setup with standard KGs, clear metrics, and controlled data splits. However, the underspecified search baseline and missing RL hyperparameters reduce reproducibility somewhat.

**Clarity of writing:** Generally clear. The examples in Figures 1–2 are helpful. The tokenization and problem formulation are well explained.

**Value to the community:** Moderate to high. The task definition enables future work on KG abduction. The generative baseline and RLF-KG provide a starting point for comparison.

The paper makes a credible first contribution to a new task. The weaknesses are real but minor — they concern presentation, documentation, and overclaim rather than the validity of the core results. The primary evidence (RLF-KG consistently improves over supervised training) is sound.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>