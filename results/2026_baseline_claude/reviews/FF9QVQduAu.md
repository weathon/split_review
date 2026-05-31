## Summary

CrowdFM introduces a foundation model paradigm for crowdsourced label aggregation. Rather than fitting dataset-specific parameters (as all existing methods do), it pre-trains a bipartite GNN on a large, diverse synthetic corpus generated via a three-parameter logistic (3PL) IRT model, then deploys the fixed model zero-shot on any new crowdsourcing dataset. The key technical ingredients are (i) a domain-randomized synthetic data generator that faithfully mimics real-world annotation statistics, and (ii) a size-invariant initialization scheme that lets the same model adapt to varying numbers of workers, tasks, and label options. Experiments on 22 benchmarks show CrowdFM wins on 21/22 datasets over MV, is statistically competitive with the best dataset-specific methods, and runs in 0.53 s—all without any dataset-specific training.

---

## Strengths

- **Well-motivated and practically impactful problem.** The tension between majority voting's scalability and advanced methods' accuracy is clearly articulated. A retraining-free model that ships once and generalises everywhere has obvious value for production pipelines. The foundation-model framing is appropriate and principled.

- **Principled synthetic data generation.** Using the 3PL IRT model to generate annotations is not an ad-hoc choice; it is grounded in decades of psychometric theory and properly captures the interplay of worker ability, task difficulty, task discrimination, and guessing probability. Randomizing the distribution hyperparameters per dataset (domain randomization) is a well-established sim-to-real transfer technique applied appropriately here.

- **Size-invariant initialization.** Initialising all worker nodes to the same shared learnable vector and all task nodes to another, then differentiating them only through annotation-graph message passing, is an elegant solution to the variable-size problem. It cleanly avoids dataset-specific embeddings and makes the model directly deployable on unseen graphs of arbitrary scale.

- **Comprehensive experimental evaluation.** 22 real-world benchmarks covering a wide range of domains, sizes, and annotation densities, paired with 11 baselines, a Wilcoxon signed-ranks significance test, and per-dataset runtime reporting—this is a thorough empirical study. The ablation on attention vs. mean aggregation and on the synthetic generator shows the contribution of each component clearly.

- **Multiple downstream applications.** Worker/task assessment and task assignment experiments demonstrate that the learned representations transfer beyond label aggregation, validating the "foundation model" branding and expanding the practical scope of the contribution.

---

## Weaknesses

### Fatal
None.

### Major

1. **EBCC still leads on average accuracy (84.08% vs. 83.41%).** Although the difference is not statistically significant (p = 0.90), and CrowdFM leads on win count (21 vs. 17), the headline claim that CrowdFM "matches or surpasses" dataset-specific methods is oversold. EBCC is consistently better on average accuracy even though it is 5× slower; reviewers who care primarily about accuracy can reasonably argue CrowdFM is not yet superior—only competitive. The paper should present the comparison with more precision rather than claiming broad superiority.

2. **Option embedding randomness at inference.** Option nodes are initialised from $\mathcal{N}(0, I_d)$ at every new inference call (Eq. 4). This introduces stochasticity in predictions for the same input. The paper does not discuss variance across random seeds for inference or report averaged results. In practice this raises reproducibility concerns, and edge cases (e.g., two label options receiving very similar random initializations) could degrade performance silently.

3. **Attention formulation computes self-similarity, not cross-annotation comparison.** In Eq. 7, both query $q_{ij}$ and key $k_{ij}$ are derived from the same triple $h_{ij}^{(l)}$, so the pre-softmax score is a bilinear form on the same vector: $\langle W_q h_{ij}, W_k h_{ij}\rangle$. This yields a scalar importance weight per annotation, which is then softmax-normalised over a node's neighbourhood. While valid as a learned reweighting, it is not standard attention—no annotation is "attending to" other annotations; each annotation simply receives a content-based scalar score. The gain over mean aggregation (seen in ablation) may reflect learned filtering of high-quality annotations rather than genuine attention dynamics. The description as "attention-based message passing" should be clarified, and a version that computes cross-annotation comparisons (query from one annotation, keys from others) would be a natural and potentially stronger alternative to explore.

### Minor

1. **Task assignment experiment limited to a single dataset (Web).** Whilst the trend is clear and Figure 5 is informative, generalizability of the compatibility-predictor benefit across multiple datasets would strengthen this claim significantly.

2. **Worker ability prediction on real-world data is only moderately correlated (Pearson = 0.449, Spearman = 0.506).** These values are meaningful but modest; practitioners would need to calibrate their expectations before relying on these ability estimates. The paper presents this more positively than the numbers warrant.

3. **Compatibility head for task assignment requires ground-truth labels during training.** This creates a bootstrapping dependency: to train the compatibility head, you need labels from the current dataset. The paper does not clearly state how this interacts with the "retraining-free" claim for this downstream application.

### Trivial
None worth enumerating.

---

## Nice-to-Haves

- Report variance over multiple inference seeds to characterise the effect of random option initialisation.
- A cross-annotation attention variant (standard transformer attention among annotation triples at each node) as an ablation baseline would clarify the mechanism's effectiveness.
- Task assignment and worker assessment experiments on more than one real-world dataset to substantiate generalizability claims.
- A brief discussion of settings where the 3PL model is a poor fit (e.g., adversarial annotators, class-conditioned biases, sequential/ordinal annotations) to help users gauge when CrowdFM may fail.

---

## Novel Insights

The key insight synthesised here is the *sim-to-real foundation model* for structured probabilistic label aggregation: by committing to a principled generative family (3PL IRT) for synthetic pre-training and designing a graph architecture that is agnostic to dataset size via shared initialisation, one can escape the per-dataset parameter estimation bottleneck entirely. This is analogous to meta-learning over tasks, but the "task distribution" is itself designed from domain knowledge of human annotation behaviour rather than scraped from existing datasets. The combination of IRT-based domain randomisation and size-invariant GNN pre-training is a reusable blueprint that could be applied to other structured prediction problems where the "graph" varies in size at deployment time.

---

## Suggestions

- Run inference on each benchmark at least 5 times with different option-initialization seeds and report mean ± std to address the stochasticity concern.
- Re-examine Equation 7 and either rename the mechanism (e.g., "content-based weighted aggregation") or implement and ablate a true cross-annotation attention variant.
- Expand the task assignment experiment to 3–5 datasets; even a low-effort evaluation on Bird or ZC_all would substantially strengthen the claim.
- Add a synthetic–real distributional analysis for the datasets where CrowdFM trails EBCC to understand systematic failure modes.

---

## Score and Decision

CrowdFM is a solid, clearly motivated contribution that substantially advances the practical utility of crowdsourcing aggregation. The evaluation is among the most comprehensive in the literature on this topic. The main performance claim is slightly overstated (EBCC still leads on average accuracy), the attention mechanism deserves clarification, and the inference-time stochasticity is unaddressed—but none of these invalidate the core contribution. The retraining-free paradigm genuinely adds value to the community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>