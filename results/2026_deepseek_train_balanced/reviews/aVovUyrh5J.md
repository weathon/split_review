## Summary

This paper proposes IBCircuit, a circuit discovery method that uses learnable noise injection into intermediate activations, guided by an Information Bottleneck (IB) objective, to identify task-relevant subgraphs (circuits) in Transformer-based models. The key claimed advantages are (1) a principled information-theoretic formulation, (2) not requiring task-specific corrupted inputs for training, and (3) joint optimization of all component weights rather than independent interventions. Experiments on GPT-2 Small for IOI and Greater-Than tasks show competitive or superior performance on IOI compared to ACDC, attribution patching, and subnetwork probing, though underperformance on Greater-Than is acknowledged.

## Strengths

- **Novel formulation of circuit discovery as an IB optimization.** Casting circuit identification as an explicit trade-off between task-relevance and compression (Eq. 7: min\_C –I(Y;C) + αI(G;C)) is a fresh perspective that differs from prior heuristic approaches. The IB framing provides a clean conceptual motivation for why a circuit should be both informative about the task and compressed.

- **No task-specific corrupted activations required during training.** The method uses Gaussian noise sampled from dataset activation statistics (mean and variance of intermediate activations) to perturb model components, avoiding the need to design per-task corrupted inputs during the discovery phase. This is a genuine practical advantage over activation patching methods.

- **Ablation study validates the dual-loss design on IOI.** The ablation (RQ2) on the IOI task shows that removing either the CE loss or the MI loss degrades performance, empirically confirming that both terms contribute in that setting. This provides some support for the IB-inspired two-term objective.

## Weaknesses

### Major

- **Unsupported claim about "factual recall" and "earlier layers."** The abstract and contribution list (lines 4, 22) state that "the results from IBCircuit suggest that the earlier layers in Transformer-based models are crucial in capturing factual information." The conclusion (line 228) further mentions "Factual Recall Localization tasks" as if they were a separate experiment. **No experiment in Section 5 tests factual recall or provides a layer-wise importance analysis.** The only tasks evaluated are IOI (indirect object identification) and Greater-Than (numeric ordering), and the paper presents no evidence about which layers are most important. This is a factual overclaim in the paper's advertised findings.

- **Theoretical derivation does not connect to the practical method.** The paper claims an IB foundation, but the link between the formal IB objective (Eq. 7: min\_C –I(Y;C) + αI(G;C)) and the noise-injection optimization (Eq. 8: min\_Ĝ –I(Y;Ĝ) + αI(G;Ĝ)) is not rigorously established. The inequality chain in lines 125–131 is presented without adequate justification: how G\_s (a subset independent of Y) is identified, why I(G\_s;C) ≤ I(G\_s;Ĝ) holds, and why I(G\_s;Ĝ) ≤ I(G;Ĝ) – I(Y;Ĝ) follows, are all asserted without proof. Critically, the bound on I(G\_s;C) is stated to require α=1 (line 131), yet α is treated as a tunable hyperparameter (line 155, α "used to adjust the weights of the loss"). The theoretical guarantee therefore does not apply to the actual method used unless α=1, which is never confirmed. The paper would be better served by describing the method as a heuristic noise-regularization approach rather than claiming rigorous IB grounding.

- **CE loss contributes nothing on Greater-Than, undermining generality.** The paper's own results (line 204, 210) show that on the Greater-Than task, IBCircuit and IBCircuit-woCE (MI loss only) perform similarly, meaning the CE loss is irrelevant — the method reduces to optimizing only the MI loss. The paper attributes this to "insufficient training from CE loss" because "the Greater-Than task input lacks a unique next token output label" (line 204). This is a significant limitation: the method's success depends on the task having a near-deterministic next-token label, which many tasks do not satisfy. Combined with the underperformance against ACDC on this task (line 204), this substantially narrows the claimed generality.

### Minor

- **Insufficient experimental details for reproducibility.** The paper does not report the selection threshold δ, the hyperparameter α value(s), learning rate, optimizer, batch size, number of training epochs/steps, dataset size, or whether results are averaged over multiple random seeds with error bars. These omissions make it impossible to reproduce the results or assess their statistical reliability.

- **Efficiency claim is unsubstantiated.** The paper repeatedly criticizes existing methods as "complicated and inefficient" (lines 12, 20) but provides no runtime, GPU hours, or memory comparison. Without this data, the efficiency advantage over baselines is asserted rather than demonstrated.

- **Conceptual ambiguity in the equivalence evaluation (RQ3).** The paper measures "equivalence" as the proportion of instances where the circuit *outperforms* or matches the full model (line 212). Reporting that IBCircuit's circuits outperform the full model on >50% of IOI instances (line 214) is framed as a positive result, but in circuit discovery the goal is to identify the subgraph that *explains the model's behavior*, not to find a better-performing one. If a proper subgraph systematically outperforms the full model, it may be following a different computational path, which raises questions about faithfulness. The evaluation should focus on output agreement with the original model, not comparative performance.

### Trivial

- None.

## Nice-to-Haves

- Clarifying the theoretical connection: either provide a rigorous derivation showing that optimizing Eq. 8 with the proposed bounds actually minimizes an upper bound on the circuit IB objective (Eq. 7), or reframe the method without the IB theoretical grounding and present it as a noise-regularized selection approach.
- Adding experiments that explicitly test the "earlier layers" claim (e.g., layer-wise ablation analysis, comparison of circuits found at different layers).
- Reporting computational cost (training time, GPU hours) to substantiate the efficiency advantage claimed over baselines.
- Adding error bars / variance across runs for all quantitative results, given the noise injection is stochastic.

## Removed Points

The following points from the inputs are excluded with justifications:

- **"Garbled equation" criticism (Eq. 10/line 147):** The harsh critic acknowledged this is "likely parser artifact." Per instructions, formatting/parser artifacts are removed.
- **"The method still requires corrupted datasets for evaluation":** The paper's contribution is about not needing corrupted inputs during the *training/discovery phase* (line 20: "without corrupted activation construction"). The evaluation protocol (line 195) uses activation patching with corrupted datasets, which is standard practice and not a limitation of the method itself.
- **"Selection mechanism (Section 4.3) is vague":** The paper provides concrete operational criteria: threshold δ for λ\_i values and identification of commonly occurring layers with larger λ. While not fully precise, this is comparable to standard practice and not a distinct weakness beyond the missing δ value (covered under missing experimental details).
- **"The method optimizes λ\_i but δ determines circuit size":** This is how threshold-based selection works — the threshold controls circuit size, and the learned λ\_i values determine which components pass the threshold. This is standard and not a flaw.
- **Strength Finder's claim about "theoretical justification that existing methods lack":** The derivation has verified gaps (see Major weakness 2), so overstating the theoretical contribution is removed. The IB *formulation* remains a strength, but the claim of rigorous theoretical justification is not supported.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments surface genuine problems (unsupported factual-recall claims, derivation gaps, limited generality) but do not offer new analytical insights into the circuit discovery problem that the paper itself does not discuss.

## Suggestions

1. **Remove or substantiate the factual-recall / earlier-layers claim.** Either add an experiment that tests this (e.g., layer-wise ablation, or evaluation on a factual recall benchmark) or remove the claim from the abstract and contributions.
2. **Either tighten the IB derivation or drop the theoretical framing.** If the method is fundamentally heuristic (learn noise-injection weights with a CE+regularization loss), present it as such. Claiming IB grounding requires a rigorous connection; the current sketch with unverified inequalities does not suffice.
3. **Report all experimental hyperparameters** (δ, α, learning rate, optimizer, batch size, epochs, dataset size) and include error bars or variance estimates over multiple runs.
4. **Reconsider the RQ3 "equivalence" metric.** Either reframe it as "task performance preservation" (not equivalence) or add a direct per-instance output-agreement metric (e.g., logit correlation between circuit and full model).
5. **Provide a computational cost comparison** (training time per task, GPU hours) to support the claimed efficiency advantage over baselines.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>