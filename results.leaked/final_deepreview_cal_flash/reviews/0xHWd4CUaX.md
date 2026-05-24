## Summary

This paper proposes a reinforcement learning framework for automated code refactoring that combines contrastive pre-training on code graphs with a composite reward function and a graph-attention policy. The central idea—learning refactoring-aware representations via self-supervised contrastive objectives and using them in an RL loop—is interesting and addresses a real problem in automated refactoring. The paper reports strong results across multiple metrics, includes an ablation study, and demonstrates cross-language transfer. However, the paper has several significant issues in technical clarity, methodological rigor, and evaluation consistency that prevent it from being accepted in its current form.

## Strengths

- **Novel combination of contrastive pre-training with RL for code refactoring.** The idea of learning refactoring-aware representations through self-supervised contrastive objectives and then feeding them into an RL policy is well-motivated and distinct from prior work that relies on handcrafted rewards or expert demonstrations.

- **Comprehensive evaluation with strong results across multiple metrics.** Table 1 shows the proposed method achieving the highest scores on SI (83.7%), SP (93.8%), MG (27.9%), and GS (72.4%), outperforming rule-based, learning-based, RL-based, and hybrid baselines across the board.

- **Clean ablation study isolating component contributions.** Table 2 systematically ablates each component (contrastive pre-training, embedding rewards, semantic tests) and shows that contrastive pre-training causes the largest performance drop (−7.5% SI), confirming it is central to the method's success.

- **Faster convergence demonstrated.** Figure 1 shows the proposed method reaches near-maximum reward by ~15k episodes versus ~25k for GraphRL, supporting the claim that pre-trained embeddings accelerate RL training.

- **Cross-language generalization evidence.** Table 3 shows a model pre-trained solely on Java maintains reasonable SI (68.7% on Python, 63.5% on C++) without fine-tuning, outperforming language-specific rule-based tools.

- **Qualitative examples of non-trivial refactorings.** Section 5.5 provides concrete cases (pattern consolidation, dataflow optimization, architectural hints) showing the method discovers transformations beyond simple rule-based fixes.

## Weaknesses

### Fatal

None. The core idea and experimental results have merit, though several issues need major revision.

### Major

- **Equation 6 (exploration strategy) is not a valid action distribution.** The expression π_explore(a|s) ∝ exp(−½(h_s − h*)ᵀΣ⁻¹(h_s − h*)) does not depend on the action *a*. It is a scalar function of the state only and therefore cannot define action probabilities. This appears to be an exploration bonus or state-valuation term misrepresented as a policy distribution. Without resolving this, the exploration mechanism cannot be understood or reproduced.

- **Equation 7 (policy network) conflates graph-level and node-level representations.** The state representation is defined as [h_t; q_t] where h_t is a *graph-level* embedding from mean pooling. Yet Eq. 7 uses h_j (node-level indices) and describes attention weights "deciding how nodes aggregate information from their syntactic neighbors," which describes message passing, not action selection. The connection between this equation and concrete refactoring action probabilities is not established.

- **Table 1 caption error for Edit Distance.** The caption states "higher is better" for all metrics, but the proposed method achieves ED=0.36 versus baseline values of 0.38–0.52. If lower ED indicates less code change (which is the standard interpretation for normalized Levenshtein distance and is consistent with the paper's claim that the method is better), then the caption is wrong. If "higher is better" were correct, the proposed method would be the *worst* on this metric. This inconsistency needs to be resolved.

- **No error bars, standard deviations, or replication information.** The paper reports all results as point estimates with no indication of variability across runs. Every table and figure lacks error bars, confidence intervals, or information about how many random seeds were used. For an empirical paper reporting numerical comparisons, this is a significant omission that makes it impossible to assess the reliability of the claimed improvements.

- **The r=0.72 correlation (Figure 2) is not independent validation of the embedding-dynamics reward.** This correlation is computed from the same model trained *with* this reward term, so it reflects what the model learned to do under that reward, not evidence that embedding dynamics is a generally meaningful signal. A proper validation would need to show the correlation holds in an independent setting (e.g., with fixed policy parameters while varying the presence of the reward term, or on a held-out dataset).

### Minor

- **The symbolic execution component (Section 4.5) is described without any discussion of computational cost.** Invoking symbolic execution at every RL step across 1M environment steps would be prohibitively expensive for realistically sized codebases. The paper provides no details about what tool was used, the time overhead per step, or whether this was actually performed in the reported experiments. This makes it difficult to assess the method's practicality.

- **Several writing issues obscure meaning.** Examples include: "something that necessarily requires the existing RL approaches to accomplish and that most often do last year because of the handcrafted nature of their metrics" (Abstract); "our approach is excellent in reducing the necessity of expert demonstration based learning" (Introduction) — while outperforming the demonstration-based baseline GraphRL, the paper does not conduct a controlled experiment isolating the effect of removing expert demonstrations.

- **The cross-language evaluation (Table 3) compares only against rule-based tools (PyLint, Cppcheck).** While outperforming these shows basic transferability, the paper does not compare against other learning-based methods that could also transfer (e.g., fine-tuning a pre-trained code encoder). The claim of "reasonable performance despite the domain shift" is supported, but the advantage over alternative transferable approaches is not established.

### Trivial

- The reward weight vector w_q = [0.4, 0.3, 0.3] is stated to correspond to "Cyclomatic complexity, coupling metrics, and style violations" but it is not explained how three scalar weights capture potentially multiple metrics within each category.

## Nice-to-Haves

- Replacing symbolic execution with a feasible proxy (existing test cases, random input testing, or lightweight equivalence checks) would strengthen practical applicability.
- Comparing the contrastive pre-trained encoder against alternative code encoders (GraphCodeBERT, CodeBERT, or a randomly initialized encoder) while keeping the RL pipeline identical.
- Reporting results with standard deviations over multiple random seeds (≥5).
- Adding a comparison with LLM-based code transformation approaches would help position the contribution.

## Removed Points

These points were raised but removed from the main evaluation for the reasons given:

- **Criticism that references (Marvellous et al., 2025; Polu, 2025; Prasad & Srivenkatesh, 2025) have implausible author names/patterns.** Removed per the hard rule that reviewing cannot question the existence or validity of cited references.
- **Claim that Figure 3's table appears "hand-crafted" because proportions change in clean increments.** This is speculative; without evidence of fabrication, this criticism cannot be sustained. However, the lack of error bars and replication remains a valid concern.
- **Criticism about missing comparison with LLM-based methods as a weakness.** This is scope-creep; the paper focuses on RL+GNN for refactoring and does not claim to benchmark against LLMs. It is listed as a nice-to-have suggestion instead.
- **Claim that the method's superiority on SI "is not trustworthy" because SI overlaps with the reward.** The reward includes style violations as one component (weight 0.3) of one term in a composite function; SI measures percentage reduction in violations. There is partial overlap but the claim of "circularity" overstates the issue, especially given that the method also excels on metrics not in the reward (SP, MG, GS). This is noted as a minor transparency concern rather than a structural flaw.
- **Strength #3 from Strength Finder ("Learned embeddings encode meaningful refactoring signals" with r=0.72).** Removed because the weakness about the correlation being endogenous is valid—the correlation is computed from the model trained with that reward, so it is not independent validation.

## Novel Insights

None beyond the paper's own contributions. The idea of using contrastive pre-trained graph embeddings as state representations for RL-based refactoring is itself the novel element. The reviews surface that this idea is promising but the current execution does not yet deliver a convincing or reproducible demonstration of its value.

## Suggestions

1. **Fix Equations 6 and 7.** Clarify how the exploration strategy actually produces action probabilities (Eq. 6 needs to depend on the action). For Eq. 7, clearly define whether the policy operates on graph-level or node-level representations and how attention weights translate into action selection over refactoring operations.
2. **Correct the Table 1 caption** to accurately describe whether higher or lower is better for ED.
3. **Add error bars and standard deviations** to all reported results (tables and figures), with clear information about the number of seeds and runs.
4. **Reformulate Figure 2's analysis** either as a validation on held-out data or remove the causal claim, since the correlation is endogenous.
5. **Provide details on the symbolic execution implementation** or replace it with a feasible proxy, and discuss the computational overhead.
6. **Add a controlled comparison** where the same RL pipeline is run with different code encoders (contrastive pre-trained vs. GraphCodeBERT vs. randomly initialized) to isolate the benefit of the contrastive objective versus pre-training in general.

## Score and Decision

**Calibration Protocol**

**Round 1 (Bracketing):** Three queries covering low (score<3.5), middle (3.5–7.5), and high (>7.5) regions on topics related to the paper.

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| FALCON | N18Z2MkMEa | 3.00 | 1 | More serious clarity issues than our paper; our results are stronger |
| GEPCode | DgGdQo3iIR | 4.33 | 1 | Similar evaluation scope but GEPCode has clearer methodology |
| Code Repr. Learning | vfzRRjumpX | 5.75 | 1 | Much stronger methodology and clarity; our paper fares worse |
| CoRNStack | iyJOUELYir | 6.25 | 1 | Strong empirical contribution with rigorous evaluation; not directly comparable |
| RLEF | zPPy79qKWe | 4.50 | 2 | Similar level of methodological concerns; slightly clearer writing |
| Coarse-Tuning | vLqkCvjHRD | 4.75 | 2 | Clearer method description; our paper has more technical ambiguities |
| MetroGNN | VeFmnRmoaW | 5.00 | 2 | Clear problem formulation and method; our paper less clear |

**Round 1 bracket:** Between 3.0 and 5.75. The paper is clearly stronger than the low anchors (FALCON at 3.00, which has severe clarity issues) but weaker than the high anchors (Code Repr. Learning at 5.75, which has strong methodology and clarity).

**Round 2 (Narrowing):** Targeted searches within the 3.0–5.75 bracket returned anchors at 4.50–5.00. Comparing against these: *Coarse-Tuning* (4.75) and *RLEF* (4.50) have comparable scope and ambition but significantly clearer method descriptions. The present paper has more technical ambiguities (invalid equations, metric inconsistency) and less statistical rigor. Among the middle-band anchors, *MetroGNN* (5.00) has a clearer problem formulation and method but a more modest contribution. *GEPCode* (4.33) has similar evaluation breadth with clearer writing. Our paper sits below these anchors because the technical description issues (Eq. 6 and 7 being invalid as written) are more severe than typical clarity concerns.

**Final Score: 4.0** — The paper has a worthwhile idea and promising results, but the combination of technically incoherent equations, a clear metric inconsistency, absent statistical rigor, and insufficient methodological detail means the contribution is not reliably established. This is below the acceptance threshold.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>