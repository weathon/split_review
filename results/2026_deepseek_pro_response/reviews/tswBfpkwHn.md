Now I have a clear picture. Let me compare:

- **"One Step of GD is Optimal for One-Layer Linear Self-Attention" (6.00, Accept):** Similar scope (one-layer linear attention, ICL theory), but limited novelty (incremental on prior GD-as-ICL work) and lacks experiments. Our paper is clearly stronger — first Mamba ICL training analysis, richer contributions, well-aligned experiments.

- **"Toward Understanding In-context vs. In-weight Learning" (6.50, Accept):** Theory paper with gating mechanism, but reviewers flagged theory-experiment gaps and restrictive modeling. Our paper has cleaner theory-experiment alignment and a more complete story (training → generalization → mechanism).

- **"When can transformers reason with abstract symbols?" (7.60, Accept):** Strong theory with practical architectural modifications validated on real LLMs. Our paper lacks this practical innovation and real-model validation; it's a step below.

Our paper lands between 6.50 and 7.60 — I'd place it at **6.5**. Now let me write the final review.

## Summary
This paper presents the first theoretical analysis of training dynamics and ICL generalization for one-layer Mamba models, with a focus on robustness to outliers in prompts. The key technical move is reducing one-layer Mamba with A = −I_m to an equivalent architecture of linear attention followed by a product-of-sigmoids nonlinear gating mechanism (Equation 3). This enables a direct apples-to-apples comparison with linear Transformers by simply removing the gating. The central findings are: (1) Mamba can tolerate test-time outlier fractions up to min(1, p_a·l_tr/l_ts) — potentially approaching 1 — while linear Transformers provably fail beyond α = 1/2 (Theorems 2, 4); (2) this robustness advantage comes at the cost of harder optimization (more iterations, larger batch sizes); and (3) a mechanistic decomposition (Corollaries 1–2) shows that the linear attention selects context examples sharing the query's relevant pattern while the gating suppresses outliers and induces exponential recency bias. Synthetic experiments on both one-layer and three-layer models validate these theoretical predictions.

## Strengths
- **Clean architectural reduction (Equation 3):** The derivation showing that one-layer Mamba with A = −I_m simplifies to linear attention followed by product-of-sigmoids gating is elegant and directly enables the comparison with linear Transformers. This structural decomposition underpins all subsequent theoretical results.

- **Sharp, non-trivial theoretical distinction in outlier tolerance:** The comparison reveals a qualitative gap — Mamba's outlier tolerance can approach 1 (Theorem 2) while linear Transformers fail at α > 1/2 (Theorem 4). This is corroborated by Figure 2, where Mamba maintains error below 10⁻² at α = 0.8 while the linear Transformer degrades sharply past α = 0.5 across three labeling corruption types.

- **Mechanistic decomposition of Mamba's ICL (Corollaries 1–2):** Corollary 1 shows the attention concentrates weight on examples sharing the query's relevant pattern, while Corollary 2 shows the gating suppresses outlier examples and imposes exponential decay by distance from the query. Together they provide a complete mechanistic account — not just convergence bounds — of why Mamba achieves robust ICL. The multi-layer experiments (Figures 3–4) qualitatively validate these predictions even beyond the one-layer theory.

- **Honest comparison of trade-offs (Remark 4):** Rather than declaring Mamba uniformly superior, the paper acknowledges that linear Transformers require smaller batch sizes, fewer iterations (Θ(l_tr) gap), and less restrictive conditions on outlier magnitude. The finding that robustness is "bought" with harder optimization is both credible and informative.

- **Multi-layer experiments validate single-layer theory (Section 4.2):** Despite the theory being restricted to one layer, the three-layer Mamba experiments replicate the same qualitative behavior — attention score concentration on same-pattern examples (Figure 3) and gating-based outlier suppression with exponential decay (Figure 4). Table 1 reveals a practically important position-sensitivity failure mode (CQ setting) that follows directly from Corollary 2's exponential decay property.

- **Prescriptive training-inference scaling relationship:** The bound α < min(1, p_a·l_tr/l_ts) links training-time outlier exposure and prompt lengths to test-time robustness, offering practical guidance for noise-aware ICL training.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **A = −I_m simplification limits claims about full Mamba:** The paper sets A = −I_m citing Gu & Dao (2023) Theorem 1. Under this choice, the gating function G_{i,l+1}(w) takes the clean product-of-sigmoids form in Equation (3) that makes the entire analysis tractable. However, in practical Mamba, A is learned and input-dependent through the Δ parameterization. The paper never discusses what properties of the full Mamba architecture are lost under this simplification. The gating structure in (3) — a product of independent sigmoids — is a direct consequence of the diagonal negative-identity A and may not faithfully represent gating behavior when A is learned. At minimum, the paper should discuss what the analysis can and cannot claim about full Mamba models.

- **Experimental results exceed Theorem 2's sufficient condition without discussion:** With p_a = 0.6 and l_tr = l_ts = 20, Theorem 2 guarantees generalization only when α < min(1, 0.6·20/20) = 0.6. Yet Figure 2 reports Mamba classification error below 10⁻² at α up to 0.8 — a setting where the theory provides no guarantee. The paper states (line 245) that "Mamba can tolerate a fraction of outliers close to that seen during training, which can be close to 1," but with these parameters the training fraction is 0.6, not close to 1. Sufficient conditions are not necessary conditions, so this does not invalidate the theory, but the gap is large enough to warrant explicit discussion of whether the bound is loose or the experiments benefit from additional structure.

- **The positive-cone condition on test outliers is a non-trivial restriction:** Theorem 2, Condition (a), requires test outliers to contain a positive linear combination of training outlier patterns (∑λ_i ≥ L > 0), though they may also include an arbitrary orthogonal component u. The paper frames this as capturing "a wide range of possible outlier patterns" (Remark 3), which is partially true — the orthogonal component provides meaningful flexibility. However, the positive-cone requirement still excludes scenarios where test outliers use entirely different directions from training patterns. In security-motivated settings (data poisoning, prompt hijacking), attackers are not constrained to use positive combinations of previously seen patterns. The paper should be more precise about what "unseen" means and acknowledge this structural limitation.

- **The claim that α tolerance "goes to 1" needs stronger qualification in the main text:** Remark 3 notes that α → 1 requires p_a·l_tr/l_ts ≥ 1. In the natural setting l_tr = l_ts, this means p_a must approach 1 (i.e., almost all training examples are outliers). The abstract and Section 3.1 frame the α → 1 possibility without discussing this requirement. The qualifier in Remark 3 is present but easy to miss.

### Trivial

- The paper's framing in places overclaims relative to the theoretical bounds (e.g., "can be close to 1" in Section 4.1 when the experimental parameters give a bound of 0.6).

## Nice-to-Haves
- Characterize what happens when test outliers violate the positive-cone condition (e.g., orthogonal to training outlier subspace). This would transform a proof-technique limitation into a testable prediction.
- Discuss what properties of practical Mamba (with learned, input-dependent A) are captured vs. lost under the A = −I_m simplification.
- A brief discussion of how softmax attention would change the comparison with linear Transformers would contextualize the results for practitioners.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "(200) is a parser artifact"** — REMOVED. The "(200)" on line 61 is clearly a parser artifact (should reference equation (2)), not an author error. Per the hard rules, formatting artifacts are removed.

- **Harsh Critic: "The unseen outlier claim excludes genuinely novel directions orthogonal to training outlier span"** — REMOVED as incorrect. Equation (11) explicitly allows an orthogonal component u: v = ∑λ_i v_i^* + u where u ⟂ {v_r^*} ∪ {μ_j} ∪ {ν_k}. The test outlier can contain genuinely novel orthogonal directions. Only the positive-cone component is restricted. (The softened version about the positive-cone restriction being non-trivial is retained as Minor.)

- **Harsh Critic: "Abstract does not mention positive-cone condition"** — REMOVED. Abstracts are necessarily condensed; the condition is stated clearly in Section 3.1 (line 94). This is a scope of communication issue, not an error.

- **Harsh Critic: "Orthogonality assumption makes outlier detection analytically simple"** — REMOVED. The orthogonality assumption is a standard modeling device inherited from Li et al. (2024a) and Huang et al. (2023). It is explicitly stated and the paper operates within this framework. Criticizing it as "never justified beyond being a modeling convenience" applies equally to the entire line of work — this is scope creep, not a specific flaw of this paper.

- **Strength Finder: "Realistic outlier modeling with distribution-shifted test-time generalization captures practical concerns"** — REMOVED. This is too generic and overlaps with kept strengths about the theoretical framework. The positive-cone restriction (kept as Minor) also partially undercuts the "realistic" framing.

- **Strength Finder: "Explicit training-to-inference scaling relationship has practical implications"** — REMOVED as a standalone strength. It is subsumed by the kept strength about the sharp theoretical distinction.

## Novel Insights

The mechanistic decomposition in Corollaries 1–2 goes beyond typical generalization-bound papers by explaining *how* Mamba achieves robustness, not just *that* it does. The finding that robustness arises from a division of labor — linear attention handles pattern matching while nonlinear gating handles outlier suppression and recency — is genuinely novel and not obvious from the architecture alone. The corollary that this same mechanism creates a failure mode (CQ positioning, Table 1) where Mamba performs worse than the simpler linear Transformer is a crisp, falsifiable prediction that the paper validates. This bidirectional insight (why it works + when it fails) is rare in theory papers and substantially strengthens the contribution.

## Suggestions

- Add a paragraph in Section 4.1 explicitly noting the gap between the Theorem 2 sufficient condition (α < 0.6) and the experimental results (α up to 0.8), and discuss whether the bound is loose or the experimental outlier patterns satisfy additional structure beyond the positive-cone condition.
- Add a brief discussion (even one paragraph) on what properties of full Mamba (with learned, input-dependent A) are captured vs. lost under A = −I_m.
- In Section 3.1, qualify the "α goes to 1" claim by noting that in the natural l_tr = l_ts setting this requires p_a → 1 (almost all training examples being outliers).

## Score and Decision

**Calibration anchors used:**

| Round | Paper | Avg Score | Comparison |
|-------|-------|-----------|------------|
| R1 | "State-space models can learn in-context by gradient descent" | 4.00 | Our paper is clearly stronger — provides training dynamics (not just construction), generalization bounds with outliers, mechanistic decomposition, cleaner experiments |
| R1 | "Mamba SSMs are Lyapunov-Stable Learners" | 4.67 | Different focus (fine-tuning stability vs. ICL theory); our paper is more theoretically substantive |
| R1 | "When can transformers reason with abstract symbols?" | 7.60 | Strong theory paper with practical architectural modifications + real-LLM validation. Our paper is below this one — lacks practical innovations and real-model experiments |
| R2 | "One Step of GD is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention" | 6.00 | Similar scope (one-layer, ICL theory). Our paper is stronger — broader contributions (Mamba + outlier analysis + mechanistic decomposition), better experiments |
| R2 | "Toward Understanding In-context vs. In-weight Learning" | 6.50 | Theory paper with gating mechanism. Our paper has cleaner theory-experiment alignment, more complete story (training → generalization → mechanism) |

**Round 1 bracket:** 5.5–7.5

**Round 2 narrowing:** The paper is clearly above the 6.00 anchor and comparable to or slightly above the 6.50 anchor, but below the 7.60 anchor. The paper's contributions — first Mamba ICL training dynamics analysis, clean architectural reduction, sharp theoretical distinction with mechanistic decomposition, and well-aligned experiments — are genuinely novel and well-executed. The scope limitations (A = −I_m, positive-cone condition) are real but well-understood and do not undermine the core contributions. Settling at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>