- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

Self-Pruner introduces a framework where a large language model (LLM) drives an evolutionary search to find layer-wise pruning rates for post-training structured pruning of LLMs. The LLM generates the initial population, selects parent solutions, and performs crossover/mutation — all without human-designed importance metrics or retraining. The method is evaluated on LLaMA models (7B–70B) against LLM-Pruner and Wanda-sp, showing improved perplexity and zero-shot accuracy.

## Strengths

1. **Strong empirical results against existing post-training pruning baselines.** The paper reports consistent improvements over LLM-Pruner and Wanda-sp across multiple model scales (7B to 70B) and pruning rates (20%–50%). For instance, on LLaMA-2-7B at 30% pruning, Self-Pruner outperforms Wanda-sp by 3.13% and LLM-Pruner by 14.59% in mean zero-shot accuracy across seven commonsense reasoning tasks (Section 4.3). On LLaMA-2-70B at 30% pruning, perplexity increases by only 1.88 over the original model (Section 4.2).

2. **Useful ablation and sensitivity analysis.** The paper ablates the LLM-based initialization (replaced with random) and the LLM-driven mutation/crossover operations, showing both contribute to accuracy (Table 3). It also compares GPT-3.5, GPT-4, and GPT-4o as the search LLM (Table 4), and compares against the manually-designed heuristic OWL for layer-wise pruning rates (Table 5), consistently outperforming it.

3. **Demonstrated practical deployment benefits.** Table 7 reports inference speedups (up to 1.82×) and GPU memory reductions on A100 GPUs using the vLLM engine, with specific throughput numbers for LLaMA-2-70B pruned to 49B and 35B levels. This validates the practical motivation for structured pruning.

4. **Clean, automatable pipeline.** The method replaces human-designed importance metrics (e.g., OWL's activation outlier ratio) with an LLM-driven search, advancing the goal of minimal human intervention in LLM compression. The hyperparameters for the search are few and simple (κ=30, M=10, s=10, N=20).

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against a conventional evolutionary algorithm without LLM involvement.** The paper claims that "LLMs accelerate convergence" and that the approach is better than standard EAs, but the ablations only remove LLM components piecemeal (random init, no mutation/crossover) — never comparing against a standard EA with random population generation and conventional crossover/mutation operators under the same budget of fitness evaluations. Without this baseline, it is impossible to tell whether the LLM component is genuinely beneficial or whether the same search structure (population, selection, iterative refinement) alone accounts for the gains. This is the most consequential gap in the evaluation.

2. **Incomplete baseline set for post-training structured pruning.** The paper compares only against LLM-Pruner and Wanda-sp as post-training structured pruning baselines, and against OWL for layer-wise pruning rate heuristics. SliceGPT (Ashkboos et al., 2024) — a well-known post-training structured pruning method cited in the introduction — is not included in the experiments. While no paper can compare against every method, the omission of a directly relevant structured pruning method that is explicitly cited weakens the claim of "state-of-the-art" performance.

3. **No error bars or variance reporting.** The evolutionary search and LLM API calls are both stochastic, yet all reported results are single-point measurements. The paper does not report standard deviations or confidence intervals for any experiment (perplexity, zero-shot accuracy, speedup). Given the inherent randomness in both the search process and GPT-4o responses, it is unclear how stable the reported improvements are.

### Minor

1. **The "prior knowledge" hypothesis is asserted but not experimentally validated.** The paper states "we find that LLMs may have prior knowledge about their own redundancy" as a key insight (Abstract, Section 1), yet no experiment tests this claim. The ablation showing that LLM-generated initialization outperforms random initialization is consistent with this hypothesis, but it is equally consistent with the LLM simply following prompt instructions (e.g., to produce diverse, well-distributed numbers) or exploiting prompt structure. The paper would be stronger without over-interpreting this as inherent "knowledge of redundancy."

2. **Reproducibility depends on proprietary, non-deterministic API calls.** The method uses GPT-4o (proprietary, versioned, non-deterministic), and while the code is provided in the supplementary material and the prompt structure is described at a high level (Figure 2), several implementation details are underspecified in the main text: how the average pruning-rate constraint (Eq. 1) is enforced during LLM generation, how invalid or out-of-constraint solutions are handled, and how duplicate solutions are managed in the population. The evolutionary operators are described conceptually ("LLMs select parents and perform crossover/mutation") but the exact prompt instructions that realize these operations are not visible in the extracted text.

3. **Computational cost of the search is not reported.** For a 70B model, the search requires evaluating fitness (pruning + perplexity computation) for 30 initial individuals + 20 offspring per iteration × 20 iterations = 430 evaluations. The paper does not report the wall-clock time or total compute required, making it difficult to assess practical feasibility. Since each evaluation involves pruning a 70B model and measuring perplexity, the total cost could be substantial, yet this is not discussed.

### Trivial
- The term "pruning rate" (pᵢ) is defined as "the ratio of the remaining parameters after pruning to the original number of parameters" — this is actually a retention rate, not a pruning rate. Typically 30% pruning rate means 30% removed, but in the paper it appears to mean 30% retained. This creates potential for confusion.

## Nice-to-Haves

- Including SliceGPT as an additional baseline would strengthen the SOTA claim.
- Reporting wall-clock time and total API costs would help practitioners assess the trade-off between search cost and accuracy improvement.
- Analyzing whether LLM-generated pruning rates correlate with established importance metrics (e.g., activation outlier ratios, gradient magnitudes) would give insight into what the LLM is actually doing.

## Removed Points

- **"Reproducibility severely limited — prompts not shown in text."** The prompt is referenced as Figure 2, and the paper states "Code is available in the supplementary material." The parser strips figures and supplementary material from all papers; these exist in the original submission. Removed.
- **"FLAP not compared."** The paper's baseline Wanda-sp is cited as (An et al., 2024), which is the same author group as FLAP, and Wanda-sp is described as "the structured pruning extension of Wanda." The methods are either the same or from the same paper; this criticism is factually inaccurate. Removed.
- **"The comparison to OWL uses fixed hyperparameters that may disadvantage OWL."** This is speculation — the hyperparameters are taken from the original OWL paper (λ=0.08, M=5). The paper does not claim to have tuned them adversarially. Removed as speculative.
- **"LoRA fine-tuning experiment is tangential."** While not core to the contribution, it provides a useful practical datapoint and does not detract from the paper. Removed as subjective scope criticism.
- **"Budget of the evolutionary search not reported"** — kept in Minor with adjusted framing (more about computational cost than missing budget).
- Several generic claims from the Strength Finder about "automated evolutionary search driven by the LLM itself" were removed as they describe the method rather than providing evidence of strength. The "LLMs may have prior knowledge" strength claim is also removed since it conflicts with a verified weakness.

## Novel Insights

The reviewers' observations converge on a single core tension: the paper proposes an LLM-driven evolutionary search that is clever and empirically effective against human-designed baselines, but it never disentangles whether the LLM component or the evolutionary search structure is responsible for the gains. The "self-pruning" framing is appealing, but the missing conventional-EA baseline means the paper cannot support the central mechanistic claim that the LLM is providing unique value beyond the search structure itself. This is a common issue in the emerging "LLM for optimization" literature — methods that replace individual algorithm components with LLM calls need rigorous ablations that isolate the contribution of the LLM from that of the overall algorithm scaffolding.

## Suggestions

1. **Add a conventional EA baseline.** Use random population generation (respecting the average pruning rate constraint) with standard crossover (e.g., simulated binary crossover) and mutation (e.g., polynomial mutation), same population size and evaluation budget. If Self-Pruner outperforms it, the LLM contribution is clearly demonstrated.
2. **Report error bars.** Run the full search 3–5 times with different random seeds and GPT-4o API calls, and report mean ± std for the key metrics.
3. **Report the wall-clock time and approximate API cost** for the evolutionary search on at least one model size.
4. **Clarify how the average pruning-rate constraint is enforced** during LLM generation and how invalid/out-of-constraint solutions are post-processed.
5. **Tone down the "prior knowledge" claim** or provide correlational evidence linking LLM-generated pruning rates to standard importance metrics.
