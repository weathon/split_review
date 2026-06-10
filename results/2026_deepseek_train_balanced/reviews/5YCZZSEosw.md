Now I'll write the final consolidated review.

## Summary

This paper proposes ACTIVE DATA SEARCH (ADS), a framework where an LLM-based optimizer model autonomously generates API call trajectories to collect data from external sources (information retrieval, demonstration generation, question answering) to improve a policy model. The optimizer is iteratively refined via DPO using reward signals that balance task performance gains against API costs. Experiments across 1,000 in-house test tasks and three public benchmarks (AlpacaEval 2.0, Arena-Hard, MT-Bench) demonstrate consistent improvements.

## Strengths

- **Framework design for automated data discovery is well-conceptualized.** The idea of encapsulating data collection and synthesis methods into APIs and training an optimizer via DPO to select optimal trajectories is a clean formulation that could generalize beyond the current prototype. The three-API design (retrieval, generation, QA) covers distinct data acquisition strategies.

- **Comprehensive evaluation across diverse tasks and benchmarks.** The paper evaluates on 1,000 in-house test tasks spanning multiple categories and difficulty levels, plus three public benchmarks, using both RM and GPT-4 judgments. The held-out instruction split (3 observed, 97 held-out for test tasks) is a methodologically careful design that prevents instance-level overfitting.

- **Fine-grained analysis reveals meaningful patterns.** The analysis by task category (Figure 3, left) shows ADS substantially improves information-seeking, reasoning, and planning tasks while yielding only slight improvements on editing/creative writing — an honest disaggregation that strengthens credibility. The finding that relative improvement scales with task difficulty (+14.2% on very easy to +76.5% on very hard, Figure 3 right) provides evidence that the optimizer learns task-specific strategies rather than applying uniform augmentation.

- **DPO clearly outperforms rejection sampling as optimizer training algorithm.** The ablation (Section 6.1, Figure 4) shows DPO improves average win rate from 49.1% to 84.3% on in-house tasks and from 28.6% to 32.8% on public benchmarks — a large-margin result that isolates the algorithmic contribution.

## Weaknesses

### Major

- **Claim-evidence gap: the paper claims autonomous *training* but demonstrates *in-context learning*.** The title, abstract, introduction, and method description (Section 3.2, Algorithm 1) consistently use language about "retraining," "updating the policy model," and "training on the tailored dataset." Yet Section 4.4 reveals the implementation uses ICL: *"Considering the frequent policy model updating for each target task, we use in-context learning to maintain computational efficiency."* In-context learning does not change model parameters and provides no persistent improvement — the gains vanish when context is removed. This means the paper's headline contribution — that an LLM can find data to *train itself* — is not demonstrated anywhere in the experiments. The paper acknowledges it *could* use fine-tuning but chose ICL for efficiency, citing claims of comparable effectiveness (Mosbach et al., 2023; Agarwal et al.). However, this does not bridge the gap: the claims in the title and abstract are framed around training/retraining, and the experiments simply do not validate that framing. A paper about autonomous data discovery for *training* must at minimum show a small-scale fine-tuning experiment to validate that the discovered data produces persistent parameter-level improvements. Without this, the central claim is unsubstantiated.

- **Missing critical baselines.** The in-house evaluation (Figure 2) compares the final ADS model against the original policy model with no context and against the initial "prompting" optimizer (no DPO training). The paper does not compare against simpler baselines such as: (a) standard retrieval-augmented generation (embedding-based similarity retrieval of demonstrations), (b) random API trajectory selection, or (c) a fixed heuristic policy (e.g., always use Information Retrieval with the task query). The ablation in Section 6.2 compares against a QA-only baseline, but this still leaves the most natural baselines unaddressed. Without these comparisons, it is impossible to determine how much of the gain comes from the RL-trained optimizer versus the basic fact that providing task-relevant context helps performance.

### Minor

- **Comparison to larger models is incomplete and asymmetric.** The paper claims Qwen-2-7B-Instruct + ADS achieves a 38.8% RM win rate on AlpacaEval 2.0, "almost equivalent to" Qwen-2-72B-Instruct, and that Gemma-2-9B + ADS (37.0% GPT-4) "matches" Gemma-2-27B-Instruct. However, the actual scores of these larger models are not reported in the paper, making the claim unverifiable from the paper alone. Moreover, the comparison is asymmetric: the smaller model benefits from ICL augmentation while the larger models do not. A 72B model provided with the same discovered context might perform even better.

- **Large discrepancy between RM and GPT-4 evaluation is not discussed.** For Qwen-2-7B-Instruct, RM judgment gives an 84.3% win rate while GPT-4 gives only 46.0% (Figure 2). This ~38-point gap is substantial and deserves analysis. Potential explanations (e.g., RM evaluation favoring ADS outputs due to distributional similarity) are not explored.

- **Question Answering API implementation is underspecified.** The paper describes it as "resorting to the wisdom of human experts" and costing 3 "as it requires a more powerful model or manual efforts." It is unclear whether this API actually uses human annotators, a more powerful LLM (e.g., GPT-4), or some other mechanism. This ambiguity matters for interpreting both the API's capabilities and its true cost.

- **No variance/confidence estimates reported.** Win rates are reported as point estimates without error bars, confidence intervals, or significance tests. Given that evaluation samples five API trajectories per task, some measure of variability is expected. The small improvement from cost-control (81.9% → 84.3%) in particular would benefit from variance estimates.

### Trivial

None.

## Nice-to-Haves

- A qualitative analysis of what the optimizer actually learns (e.g., does it favor different APIs for different task categories? What kinds of trajectories does it discover?)
- An analysis of whether ADS gains are complementary to standard fine-tuning — i.e., would a model actually fine-tuned on the discovered data benefit further?
- Comparison to the larger models' actual scores on the same evaluation setup, to substantiate the "rivaling" claim.

## Removed Points

These points from the inputs are removed or demoted from the main review for the following reasons:

- **"Reward signal is circular under ICL"** (Harsh Critic point 2): This is an interpretation issue rather than a factual error. The optimizer demonstrably learns to select trajectories that improve held-out task performance. Whether this constitutes "self-knowledge" is a framing choice, not a correctness issue. Removed to avoid overloading on interpretive critiques.

- **"Cost-control is standard Pareto front selection"**: This is an accurate description but the method is still validated and shows clear improvements. The paper's claim of novelty on this point is slightly overstated but the contribution is real. Demoted to nice-to-have.

- **"Strengthening the Paper on Its Own Terms" section suggestions**: Some suggestions (running actual fine-tuning, adding RAG baselines) are already covered in the major weaknesses. Others (variance estimates, qualitative analysis) appear in minor/nice-to-have. Redundant suggestions removed.

- **Strength Finder points about "ADS enables 7B/9B to rival 72B/27B"**: This strength is partially undermined by the lack of reported comparison numbers (discussed in Minor weaknesses). The core empirical result remains valid but the "rivaling" framing is weakened. Retained as a minor point rather than a core strength.

- **"Held-out instruction split prevents instance-level overfitting"**: This is correctly identified but the paper does not analyze whether cross-task generalization actually occurs — the held-out instructions are from the same task cluster as observed instructions. Kept as a supporting but limited strength.

- **Generic strengths from Strength Finder** such as "the paper addressed an important problem" removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews largely surface the same points: a well-designed framework with a fundamental mismatch between its training-centric claims and its ICL-based implementation, compounded by absent baselines.

## Suggestions

1. **Either run an actual fine-tuning experiment or reframe the paper.** The single highest-leverage change is to conduct a small-scale fine-tuning experiment (e.g., on 10-20 target tasks) to validate that the discovered data produces persistent parameter-level improvements. If this is computationally infeasible, the paper should be reframed as a method for automatic demonstration selection for in-context learning, with the title, abstract, and introduction revised to match the actual contribution. This is the most critical issue and should be addressed first.

2. **Add standard retrieval and random baselines.** Compare against at least embedding-based RAG and random trajectory selection to isolate the optimizer's contribution.

3. **Report the actual comparison scores for larger models** (Qwen-2-72B-Instruct, Gemma-2-27B-Instruct) when making comparative claims, and discuss the asymmetry of the comparison.

4. **Analyze the RM vs. GPT-4 judgment gap** — this large discrepancy raises questions about evaluation reliability.

5. **Include variance/confidence estimates** for the main reported win rates.

## Score and Decision

<score>5.0</score>
<decision>Reject</decision>