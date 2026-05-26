Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes LoLoRA, a method that updates LoRA's A matrix using local Hebbian-like rules (HPCA) during the forward pass instead of backpropagation, thereby avoiding the need to store activations for A's backward pass. The method is motivated by a theoretical analysis showing that optimal A initializations span the top eigenspace of the input covariance matrix. The paper evaluates LoLoRA on GLUE with RoBERTa-large, math reasoning with LLaMA-3.1-8B, multimodal fine-tuning with LLaVA-v1.5-7B, and ablations on TinyLlama.

## Strengths

1. **Theorem 4.4 provides a formal characterization of optimal A.** Under a random linear regression model, the theorem proves that an optimal A must span the top-eigenspace of the input covariance matrix, and any nonsingular linear transformation of those eigenvectors is optimal. This generalizes and formalizes the EVA initialization insight and directly motivates the HPCA-based local update rules.

2. **The ablation study (Tables 5–6) clearly shows that HPCA-based local updates match EVA initialization without a separate pre-processing pass.** On TinyLlama/Alpaca, LoLoRA HPCA (uniform, r=4) achieves perplexity 2.545±0.011 vs LoRA-FA (EVA) 2.546±0.011 — essentially identical — while not requiring the initial SVD of training data. This is a practical advantage for deployment scenarios where a separate data-dependent initialization step is inconvenient.

3. **The evaluation covers diverse tasks across NLU (GLUE), mathematical reasoning (LLaMA), and multimodal (LLaVA) settings**, demonstrating the general applicability of the approach. The 13% extra-memory reduction vs standard LoRA on LLaMA-3.1-8B (26 GB vs 30 GB) is a genuine memory saving, and the method maintains comparable accuracy.

## Weaknesses

### Major

1. **LoLoRA does not clearly outperform the simpler LoRA-FA baseline, undermining the paper's central claim.** The paper claims to "mitigate the trade-off" between memory savings and performance introduced by freezing A. Yet across all experiments:
   - **GLUE (Tables 1–2):** LoLoRA HPCA is never the best method on any of 8 tasks. It is comparable to or slightly worse than LoRA-FA (uniform) on every task (e.g., CoLA 66.3 vs 67.9, RTE 84.6 vs 86.4), and even LoRA-FA (EVA) — which the paper frames as "underperforming" — ties or beats LoLoRA on several tasks.
   - **LLaMA math (Table 3):** LoLoRA HPCA (82.9%) matches LoRA-FA (EVA) (82.9%) and is within 0.3% of LoRA-FA (uniform) (82.6%). The local updates provide no measurable benefit.
   - **LLaVA multimodal (Table 4):** LoLoRA HPCA (perp 2.93) is slightly worse than LoRA-FA (EVA) (2.92). The "LoLoRA HPCA (EVA)" variant achieves 2.93/1.074 — no better than LoLoRA without EVA (2.93/1.075), confirming the HPCA updates are essentially neutral.
   
   The novel component (local updates of A) does not provide a clear benefit over a *frozen* A with a good static initialization (EVA), yet the method adds complexity and optimizer state.

2. **LoLoRA uses strictly more GPU memory than LoRA-FA while not outperforming it.** On LLaVA (Table 4), LoLoRA uses 24.1 GB extra memory vs LoRA-FA's 23.9 GB — a small but *negative* saving. The only memory advantage LoLoRA has over standard LoRA comes from *not storing A's input activations*, which LoRA-FA achieves at zero extra cost. LoLoRA adds a local optimizer state for A (Algorithm 1, lines 3–4), making its memory footprint strictly larger than LoRA-FA. The paper acknowledges this in the conclusion, but it directly undercuts the motivation: LoLoRA is less memory-efficient than LoRA-FA while not being clearly better in quality.

3. **The claimed advantage of "adapting to input distribution shifts" is never tested or demonstrated.** The abstract and Section 3 motivate LoLoRA by stating that local updates allow it to "adapt to input distribution shifts without storing activations for the backward pass." However, all experiments are single-task, single-epoch (except GLUE which runs multiple epochs but shows no advantage for the adaptive method), with no distribution shift within training. There is no experiment comparing LoLoRA against LoRA-FA (EVA) under conditions where the input covariance actually changes over time (e.g., multi-task sequential fine-tuning, domain adaptation, or longer training runs). Without such evidence, the "adaptation" justification remains an untested hypothesis.

### Minor

4. **The theoretical analysis assumes a setting far removed from practice.** Theorem 4.4 assumes a random linear regression model with i.i.d. Gaussian weight change targets, isolated submodules with stationary input distributions, and known optimal B. In reality, deep transformers are nonlinear, all layers are coupled through backpropagation, and the optimal B is never found by SGD in finite steps. The paper acknowledges this limitation in a single sentence in the conclusion, but Section 4 is framed as "rationale" and "theoretical justification" without making the gap clear to the reader.

5. **The GLUE results are systematically weaker than standard LoRA.** While the paper correctly reports these results, the narrative (e.g., "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups") glosses over the fact that on GLUE (the most comprehensive benchmark), LoLoRA is never the top method and is often statistically tied with or worse than even the simplest baseline (LoRA-FA uniform). The claim "achieves slightly better results than LoRA-FA (EVA)" on GLUE is accurate but the comparison to LoRA-FA (uniform) — the simpler baseline that the method should improve upon — shows no clear advantage.

6. **Missing ablation comparison: LoLoRA vs LoRA-FA (EVA) using identical initialization.** Table 5 compares LoRA-FA variants with different initializations (uniform, orthogonal, PiSSA, EVA). Table 6 compares LoLoRA variants with different local rules. But the critical comparison — LoLoRA HPCA vs LoRA-FA (EVA) with the same initialization and rank — is not shown in the controlled ablation setting where it would be cleanest. The comparison exists in Table 4 (LLaVA) but the controlled ablation on TinyLlama would better isolate the effect of the local updates.

7. **Missing runtime and throughput analysis.** Algorithm 1 performs a forward-pass update of A (lines 1–4) before computing the output, adding computation. LLaVA run times are reported (LoLoRA HPCA 2h52m vs LoRA-FA (uniform) 2h46m, ~3% slowdown), but GLUE and LLaMA run times are not. A systematic comparison of throughput (tokens/second) and training wall time across methods is absent.

### Trivial

8. The memory consumption figures are reported as single "Extra Memory (GB)" numbers without a breakdown into base model, adapter parameters, optimizer states, and activations. A breakdown would clarify whether the local A optimizer state is a meaningful cost.

## Nice-to-Haves

- A direct measurement of the "subspace distance" between the learned A and the PCA of current-layer activations during training, demonstrating that HPCA tracks shifting distributions while frozen EVA does not.
- Experiments under non-stationary conditions (e.g., sequential fine-tuning, multi-task, or longer training) where the adaptivity claim could be validated.
- Comparison against VeRA (Kopiczko et al., 2024) and Local LoRA (Key et al., 2023) as additional memory-efficient baselines.

## Removed Points

These points were considered but removed for the reasons given:

1. **"LoRA-FA already achieves the same memory savings"** — Retained in Weakness 1 and 2 above. The harsh critic raises this, and it is a real issue. Kept.
2. **"The paper claims 20% memory savings without evidence"** — This is referenced to Appendix D which is not present in the extracted text. Without being able to verify, I treat the paper's claim as stated. However, the memory data in Tables 3–4 is available and shows 13% on LLaMA and 2% on LLaVA. The claim of "up to 20%" on GLUE cannot be verified but is not central to the critique. Removed because the core memory concern (LoLoRA vs LoRA-FA) is already covered in Weakness 2.
3. **"Statistical rigor concerns"** (more seeds needed) — The paper reports mean ± std over 3 seeds, which is standard for this area. Not a genuine weakness. Removed.
4. **"Hyperparameters not tuned per method"** — The paper states hyperparameters are "same for all scenarios." This is common practice when comparing methods and is only a concern if there's evidence of systematic disadvantage. Speculative. Removed.
5. **Strength Finder: "Theorem 4.5 provides theoretical justification for asymmetry"** — This is already known from prior work (Zhu et al., 2024; Paischer et al., 2024). Not a novel contribution of this paper. Removed.

## Novel Insights

None beyond the paper's own contributions. The core tension confirmed by this review is a general one: methods that add complexity to avoid a perceived limitation of a simpler baseline (here, LoRA-FA) must demonstrate a clear advantage; when the advantage is marginal or absent, the contribution collapses regardless of theoretical motivation.

## Suggestions

1. **Reframe the contribution.** The paper's strongest finding is that online HPCA matches EVA initialization without requiring a separate data-dependent pre-processing pass. This is a practical convenience, not a performance improvement. The paper should be scoped accordingly, removing the unsubstantiated "adaptation to distribution shifts" claim or providing experiments that directly test it.

2. **Add controlled experiments under non-stationary distributions.** If the adaptive advantage of local updates is to be claimed, the paper must show a setting where the input covariance structure evolves during training (e.g., curriculum learning, multi-task sequential fine-tuning, or domain adaptation) and LoLoRA tracks it better than frozen EVA.

3. **Report memory breakdowns.** Provide a decomposition of peak memory into (a) base model weights, (b) adapter parameters, (c) adapter optimizer states, (d) local A optimizer state (if any), and (e) stored activations. This would clarify the cost-benefit trade-off of the local optimizer state LoLoRA adds.

## Score and Decision

After comparing against the calibration anchors:

| Anchor | Avg Score | Query Bucket | Comparison to this paper |
|--------|-----------|-------------|-------------------------|
| LoRA-FA (RbKThNNFxr) | 5.33, Reject | Topic-mid | Direct predecessor. Was rejected for incremental novelty. LoLoRA has more theoretical depth but weaker empirical case vs its own baselines. |
| ALLoRA (7X65yoKl3Y) | 3.33, Reject | Topic-low | Similar profile: claims not well-supported, marginal improvements. LoLoRA has stronger theory but comparable empirical weakness. |
| VeRA (NjNfLdxr3A) | 7.25, Accept | Topic-high | Strong, well-evaluated method with clear advantages. LoLoRA doesn't approach this level of empirical support. |
| ReLoRA (DLJznSp6X3) | 5.75, Accept | Topic-mid | Accepted despite some concerns. LoLoRA's empirical evidence is notably weaker. |
| HoLoRA (igGeaxOiFM) | 3.00, Reject | Topic-low | Limited novelty, insufficient experiments. LoLoRA has better theory and more experiments but similar fundamental weakness in demonstrating improvement. |

The low-band topic anchors (ALLoRA, HoLoRA) were rejected because their claimed improvements were marginal or unsupported, their evaluation was incomplete relative to their claims, and they didn't convincingly outperform simpler baselines. This paper shares those failure modes: LoLoRA does not clearly outperform LoRA-FA (EVA), its central "mitigation of trade-off" claim is not supported by the evidence, and the claimed adaptivity advantage is untested. Unlike those low-band papers, LoLoRA has a cleaner theoretical motivation and a more thorough ablation study, placing it slightly above them but well below papers that convincingly demonstrate improvement.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>