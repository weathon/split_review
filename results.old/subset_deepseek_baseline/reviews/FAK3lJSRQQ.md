## Summary

The paper introduces ExLLM, an LLM-as-optimizer framework for molecular design and large discrete optimization problems. ExLLM combines three components: (1) an evolving experience snippet that distills non-redundant cues from past evaluations to guide search without memory bloat; (2) a k-offspring scheme that generates multiple candidates per LLM call to broaden exploration; and (3) a feedback adapter that normalizes multi-objective signals, formats constraints and expert hints. The framework requires no training—only a task template and evaluation functions—and is demonstrated across molecular optimization (PMO benchmark), circle packing, stellarator design, combinatorial routing, peptide design, and GPU kernel optimization, achieving state-of-the-art or record-level results in several domains.

## Strengths

- **Strong empirical results on PMO**: ExLLM achieves a total score of 19.165 on the PMO benchmark, ranking first on 17/23 tasks and improving over the previous SOTA (MOLLEO) by +7.3%. Even without the experience module, ExLLM (18.165) outperforms prior methods, indicating the underlying approach is robust.
- **Novel evolving experience mechanism**: The paper identifies a critical failure mode of retrieval-style memory (exploration collapse, prompt bloat) in large discrete optimization and proposes a compact, updated single experience with probabilistic injection. Table 1 provides direct evidence that this design outperforms both retrieval-style memory and no memory on hypervolume, uniqueness, and cost.
- **Generalizable k-offspring scheme**: Exploiting the autoregressive factorization to sample multiple offspring per call is simple yet effective, increasing exploration breadth under a fixed budget with low overhead. This is shown to generalize across domains.
- **Broad cross-domain validation**: The framework is tested on problems ranging from molecular design to physics (stellarator), engineering (offshore jacket), combinatorics (MOCPOP), and code generation (GCU operator), all with the same hyperparameters. This demonstrates practical transferability.
- **Ablation and analysis**: The paper includes ablations on experience injection probability (cited) and the k-offspring trade-off, and provides runtime/cost comparisons, supporting the design choices.
- **Practical impact**: The GCU operator results (top-10 in a competition, second prize) show real-world applicability in a challenging, low-resource code generation setting.

## Weaknesses

### Major
- **Unclear LLM model and budget for PMO experiments**: The paper does not explicitly state the LLM model used for the PMO benchmark (Table 3) or confirm that the same LLM was used for both ExLLM and the reproduced baseline (MOLLEO) on these tasks. The five-objective experiment controls for this by using GPT-4o-2024-05-13 for both methods, but PMO results appear to rely on published MOLLEO scores (which may have used a different LLM). The evaluation budget (oracle calls) for PMO is also not stated. This is a significant fairness concern that could affect the SOTA claim.
- **Weak baselines in several cross-domain experiments**: For stellarator design, only one feasible baseline (ALM-NGOpt) is available; for circle packing, the previous records are not established through a systematic comparison of optimization algorithms (they are known best-known values). For offshore jacket, the baselines (GA, MOEAD, RS) are basic and not necessarily competitive. These results are interesting but do not constitute rigorous SOTA comparisons.
- **Marginal improvements on circle packing**: The reported new records for n=26 and n=32 differ from previous best by less than 0.001% (e.g., 2.635983 vs 2.635977), which could be within numerical noise. The paper does not report multiple runs or error bars for these results, making it difficult to assess reliability.
- **Lack of statistical rigor on PMO**: The PMO results are reported as mean ± std, but the paper does not specify the number of seeds for the PMO evaluation. The five-objective experiments use 5 seeds, but for PMO it is unclear.

### Minor
- **Lower diversity and validity in some settings**: ExLLM achieves lower diversity and slightly lower validity compared to some baselines (e.g., 0.494 diversity on random-init vs 0.581 for DyMol; 0.79 validity on best-init vs 1.0 for many baselines). The paper acknowledges a fitness-diversity trade-off, but this could be a limitation for applications where exploration of chemically diverse space is critical.
- **No comparison to recent LLM-optimizer baselines**: While the paper compares to MOLLEO, it does not compare to other recent LLM-based optimizers such as OPRO, ReEvo, or AlphaEvolve on the PMO benchmark (these are only compared on MOCPOP or circle packing). A direct PMO comparison would strengthen the empirical positioning.

### Trivial
- Table ordering in the paper is non-sequential (Table 7 appears before Table 4 in the text). This is likely a formatting artifact from compilation and does not affect technical correctness.

## Nice-to-Haves

- Provide the exact LLM model, evaluation budget, and number of seeds used for the PMO benchmark for both ExLLM and the reproduced baseline (MOLLEO). If possible, rerun MOLLEO under the same conditions to ensure a fair comparison.
- Include error bars or multiple trials for the circle packing and stellarator results to confirm statistical significance.
- Compare ExLLM to additional LLM-optimizer methods (e.g., OPRO, ReEvo) on PMO tasks to further validate the SOTA claim.
- Consider using a high-quality open-source LLM (e.g., Llama-3) for a subset of experiments to demonstrate reproducibility independent of proprietary APIs.

## Novel Insights

The paper provides a clear empirical demonstration that retrieval-style memory (append per-step summaries and re-inject) causes exploration collapse in large discrete optimization, whereas a compact, continuously updated single experience with probabilistic injection avoids bloat and maintains diversity. This insight is backed by controlled experiments (Table 1) and is relevant to the growing body of work on LLM-as-optimizer. Additionally, the probabilistic injection mechanism (Bernoulli sampling with p_exp) offers a simple knob to balance exploitation and exploration in iterative LLM-based search.

## Suggestions

- Clarify the LLM model and evaluation budget used for the PMO benchmark. If the same GPT-4o model was used for both ExLLM and the MOLLEO reproduction, state this explicitly. If not, consider reproducing MOLLEO on PMO with the same model to enable a fair comparison.
- Add a brief discussion on how the evolving experience synthesis prompt S_θ is designed and how it avoids simply memorizing high-performing candidates, to further justify the mechanism.
- For the cross-domain results, include a table showing the number of evaluations/LLM calls used for each domain to help readers gauge sample efficiency.

## Score and Decision

Score: 7 (accept)

The paper presents a well-motivated, technically sound framework with strong empirical evidence across multiple domains. The PMO results are particularly impressive and represent a clear advance over prior LLM-based molecular optimization methods. The main concerns—clarity of LLM model and budget for PMO, and weak baselines in some extended experiments—are addressable and do not invalidate the core contribution. The evolving experience mechanism is a novel and effective design for large discrete optimization. I recommend acceptance with the expectation that the authors will carefully clarify the experimental setup for PMO and possibly strengthen the cross-domain comparisons.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>