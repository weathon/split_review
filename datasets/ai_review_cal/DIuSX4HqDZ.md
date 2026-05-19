- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 6, 6, 3
Now I have all the information I need to verify each reviewer claim against the paper. Let me produce the final consolidated review.

## Summary

This paper formally introduces a new task—abductive logical reasoning over knowledge graphs—where the goal is to infer a logical hypothesis whose conclusion set (entities satisfying the hypothesis on the full KG) best matches a given observed entity set. The authors propose a generative approach (transformer seq2seq and decoder-only) combined with Reinforcement Learning from Knowledge Graph Feedback (RLF-KG), which uses PPO to optimize the Jaccard similarity between the observation and the conclusion of the generated hypothesis on the observed training graph. Experiments on FB15k-237, WN18RR, and DBpedia50 show that RLF-KG consistently improves Jaccard over supervised-only training, and the generative approach is orders of magnitude faster than brute-force search.

## Strengths

1. **Clear and novel problem formalization**: Section 2 provides a precise mathematical definition of abductive logical reasoning over KGs, including the logical hypothesis form (disjunctive normal form with existential quantifiers, conjunction, disjunction, negation), the conclusion set definition in Equation (2), and the Jaccard-based objective in Equation (4). This formalization is a necessary foundation and more explicit than prior related KG reasoning problems.

2. **RLF-KG consistently improves over supervised baselines**: Table 3 shows that on all three datasets (FB15k-237, WN18RR, DBpedia50) and for both encoder-decoder and decoder-only architectures, the RLF-KG variant achieves higher Jaccard scores than the corresponding supervised-only model. This directly supports the claim that incorporating KG feedback via PPO yields hypotheses with better explanatory power.

3. **Generative methods are orders of magnitude faster than search**: Table 5 reports inference runtime with generation-based models requiring 1.2–1.5 seconds versus 246 seconds for brute-force search (and ~61,000 seconds for the full search procedure). This supports the claim that generative approaches overcome the combinatorial complexity of symbolic search.

4. **Ablation on reward design validates design choices**: Section 4.5 (Table 4) shows that adding SMATCH structural similarity to the reward does not improve Jaccard, and sometimes worsens it, while the original RLF-KG reward (Jaccard alone) achieves the best overall Jaccard. This ablation strengthens the paper's design decisions.

5. **Architectural comparison provides practical insight**: The paper shows that encoder-decoder benefits more from RLF-KG than decoder-only, attributing this to the encoder's ability to handle unordered observation sets. This comparison provides insight into the task's nature.

## Weaknesses

### Fatal
None.

### Major

- **Modest Jaccard improvement over the search baseline**: While Table 6 shows the generative model outperforms brute-force search, the Jaccard margins are small in some cases (e.g., the paper itself states the model "only slightly overperforms the search-based method in Jaccard performance"). The claim of superiority therefore rests heavily on the SMATCH metric (structural similarity to ground-truth hypotheses) and on speed, rather than on large gains in the primary task objective. The paper would benefit from demonstrating that the small Jaccard advantage is robust and not an artifact of the specific search implementation.

### Minor

- **No confidence intervals or significance tests**: Results are reported as point estimates without variance or significance measures (e.g., Table 3 reports per-type Jaccard scores without confidence intervals). Given that some improvement margins are small, it is unclear whether the observed gains are statistically reliable. Running the RL training multiple times or using bootstrap would strengthen the evidence.

- **No analysis of training-graph vs. test-graph reward correlation**: RLF-KG uses the training graph's Jaccard as a reward, but the evaluation uses the test graph's Jaccard. The paper does not analyze how well the training-graph reward correlates with the test-graph metric, leaving open the question of whether the model may overfit to the training graph's incompleteness. Figure 6 shows the training reward increasing, but does not show whether test Jaccard tracks it.

- **No qualitative analysis of generated hypotheses**: The paper reports quantitative metrics (Jaccard, SMATCH) but does not show examples of generated hypotheses for test observations. Qualitative examples would help assess whether the Jaccard improvements correspond to semantically plausible explanations, and would bridge the gap between the motivating examples and the experimental results.

- **The task is evaluated on 13 pre-defined logical patterns**: Following prior work on KG queries (Ren & Leskovec, 2020; Ren et al., 2020), the experiments are restricted to 13 patterns. While this is standard practice in the KG reasoning literature, it limits the generality of the approach. Real-world observations may not conform to these patterns, and the paper does not discuss how to extend to arbitrary first-order hypotheses or evaluate on out-of-pattern observations. This limitation is acknowledged but could be discussed more explicitly.

- **Observation size restricted to ≤32 entities**: The paper sub-samples observation sets to at most 32 entities, but does not report how performance varies as a function of observation size. This makes it difficult to understand when the model breaks.

### Trivial
None.

## Nice-to-Haves
- **Multiple hypotheses**: Abduction often yields several plausible explanations. Beam search or diverse decoding to produce multiple hypotheses would strengthen the practical applicability.
- **Pattern-frequency baseline**: A baseline predicting the most common hypothesis type given observation size would help contextualize the improvement over supervised-only training.
- **Impact of KG incompleteness**: An ablation varying train/validation/test split ratios would illuminate how sensitive the method is to graph incompleteness.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The task is not abductive reasoning in any meaningful sense"** — REMOVED. The paper explicitly defines abduction via the standard syllogism (P ∧ H → O) in Section 2 and formalizes it for KGs: finding a hypothesis whose conclusion set (entities satisfying H on the hidden KG) best matches the observation. This is a reasonable operationalization of abduction in a KG setting. The critic's characterization ("query reconstruction from answer sets") is an uncharitable reframing that ignores the paper's clear formalization of the explanatory relation. The set-matching objective directly follows from the P ∧ H → O formulation given the KG context.

2. **"The medical diagnosis example cannot be handled by the 13 patterns"** — REMOVED. The medical example (H₃: HaveSymptom(V_?, V_₁) ∧ RelievedBy(V_₁, Panadol)) is a 2p pattern (a path of two relations with one existential variable), which IS among the 13 patterns. The critic's factual claim is incorrect.

3. **"Evaluation metric does not measure explanatory quality" (framed as a fatal flaw)** — REMOVED as a fatal/structural issue, demoted to task context. The Jaccard index is the formal objective of the task as defined: hypotheses are better explanations precisely when their conclusion sets better match the observation set under the hidden KG. The critic's example of "a long disjunction enumerating observed entities" is prevented by the 13-pattern restriction. SMATCH is appropriately used as a secondary metric for structural similarity to ground-truth hypotheses, and the paper is transparent about this.

4. **"KL penalty copied from RLHF without justification"** — REMOVED. The paper cites Ziegler et al. (2020) and states "Again following (Ziegler et al., 2020)," which is the justification. The KL penalty is standard practice in RL fine-tuning of generative models.

5. **"Weak baseline comparison — no comparison with rule miners (AMIE, NeuralLP, AnyBURL)"** — REMOVED. Rule mining methods perform inductive reasoning (learning rules from repeated patterns), not abductive reasoning (finding hypotheses to explain a given entity set). Adapting them to this fundamentally different task is non-trivial and not a standard baseline. The brute-force search is the natural baseline for a newly proposed task.

6. **"Unknown entities not handled"** — DEMOTED to minor scope note. The paper assumes O ⊂ ν (observation entities are in the KG), which is a reasonable assumption for the task formulation. Discussing this limitation would be nice but is not a weakness of the current formulation.

7. **"The search baseline's astronomical runtime is a weakness" framing** — REMOVED. The runtime advantage is correctly presented as a strength of the generative approach (Table 5). The critic's framing that "the main practical benefit is speed, not reasoning quality" ignores that both speed AND Jaccard are better (even if Jaccard by a small margin).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel synthesis or insight that the paper does not already contain.

## Suggestions

1. **Add confidence intervals or significance tests** for the main Jaccard results to establish that the improvements over supervised-only training and search are statistically reliable.
2. **Provide a correlation analysis** between training-graph Jaccard (the RL reward) and test-graph Jaccard during RL training to verify that the model does not overfit to the training graph's incompleteness.
3. **Include qualitative examples** of generated hypotheses alongside their Jaccard scores, demonstrating that higher Jaccard does correspond to semantically plausible explanations.
4. **Report performance broken down by observation size** to understand when the model breaks and whether the ≤32 restriction is limiting.
5. **Explicitly discuss the 13-pattern limitation** and outline potential extensions to arbitrary first-order hypotheses, rather than relying on the reader to know this is standard practice from prior KG query work.
