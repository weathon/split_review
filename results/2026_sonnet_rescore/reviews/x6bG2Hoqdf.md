## Summary

CALM proposes a hybrid framework for Automatic Heuristic Design (AHD) that combines evolutionary prompt-level ("verbal") guidance with online reinforcement learning fine-tuning ("numerical") of the underlying LLM. Using GRPO with a carefully designed reward function, CALM co-evolves both the heuristic population and the 7B INT4-quantized model itself, enabling a locally run, single-GPU system to discover heuristics that compete with and often surpass those produced by API-based (GPT-4o-mini) AHD baselines across OBP, TSP, CVRP, and OP tasks. The proposed framework introduces new fine-granularity mutation operators (injection, replacement), a diversity-aware crossover operator, and a probabilistic collapse mechanism to escape local optima.

---

## Strengths

- **RL fine-tuning is the dominant factor, confirmed by ablation.** Table 4 is unambiguous: removing GRPO causes the single largest performance drop across all ablation settings—OBP gap rises from 0.71% to 1.78%, and OP gap from 17.41% to 19.89%. This cleanly validates the paper's central claim that numerical gradient updating is the critical new ingredient over prior verbal-only frameworks.

- **Cleanest comparison—CALM vs. EvoTune—is consistently won by CALM.** Both use Qwen2.5-7B-Instruct-INT4 with GRPO-based fine-tuning. CALM outperforms EvoTune on all four tasks and all test scales (Tables 1–3: OBP 0.71% vs. 2.40%, CVRP N=200 3.95% vs. 6.13%, OP N=100 15.43% vs. 18.27%). This comparison isolates the contribution of CALM's design choices—operators, collapse, reward—from confounds of model quality or API access.

- **Reward function design is empirically validated.** Table 4 shows that neither alternative reward scheme (performance-based or binary improvement) matches the proposed relative-improvement reward. The performance-based reward underperforms even the no-RL baseline on OP (21.30% vs. 19.89%), making the design choice non-trivial and well-motivated.

- **Novel operators each contribute measurably.** Table 4 ablation confirms that injection, replacement, diversity-aware crossover, and simplification each contribute independently—removing any one consistently degrades performance. The diversity-aware crossover result is particularly notable: crossover without diversity-based selection performs *worse than no crossover at all* on OBP (1.05% vs. 0.88%), highlighting the importance of the specific design choice.

- **Practical scope is genuinely attractive.** Running GRPO on a 7B INT4-quantized model with only 1.15% of parameters fine-tuned, on a single 24 GB GPU, is a concrete and reproducible resource claim. The ability to do this locally, without API dependency, is a real practical advantage over prior work.

---

## Weaknesses

### Fatal
None.

### Major

- **G (GRPO group size) is not disclosed in the main text, making the evaluation budget comparison ambiguous.** Section 4 states "G responses are sampled from the local LLM π_θ" but never specifies G's numeric value in the main text. The paper reports CALM's budget as "2,000 LLM queries" and baselines' as "1,000 heuristic evaluations." If "LLM queries" means individual response generations (as would be natural), and G > 1, then the number of GRPO rounds is 2000/G while the total heuristic evaluations remain 2,000. This is 2× the baselines' 1,000, independently of G. The problem is compounded because it is unclear whether "2,000 LLM queries" means 2,000 prompt submissions (each yielding G responses, potentially 2,000 × G total evaluations) or 2,000 total response generations. Section 5.2 confirms G=1 for the API ablation, implying G > 1 for the main CALM experiments, but the actual value is deferred to Appendix H. Without knowing G, readers cannot determine whether CALM's margins over MCTS-AHD on TSP (10.04% vs. 9.69%), CVRP N=50 (3.83% vs. 5.44%), and OP N=50 (24.22% vs. 25.27%) reflect a better method or a larger evaluation budget. The cross-model EvoTune comparison avoids this issue (both use the same G), but the primary claim against GPT-4o-mini baselines does not. The authors should state G explicitly in Section 5 and clarify what "LLM queries" counts.

- **Abstract and introduction overclaim on "outperforms SOTA."** Table 3 shows two HSEvo rows under GPT-4o-mini for OP—both achieve lower in-domain gaps (23.98% and 24.08%) than CALM (24.22%) at N=50. CALM's own Section 5.1 partially acknowledges this: "As for the in-domain scale, it still outperforms EoH and the most recent approach, MCTS-AHD and EvoTune"—notably omitting HSEvo. The abstract's unqualified claim that CALM "outperforms state-of-the-art baselines across various optimization tasks" is not uniformly supported. Moreover, the two HSEvo rows with differing values (e.g., CVRP N=50: 7.54% vs. 6.11%) are never explained in the text, making it unclear whether these represent distinct HSEvo configurations, different runs, or a table layout issue. This ambiguity affects interpretation of several results and should be resolved.

### Minor

- **Collapse mechanism is sensitive to hyperparameters in a practically significant way.** Table 4 shows δ₀=0.005, C=15 yields OP gap of 27.22% vs. the chosen setting's 17.41%—a near 10-percentage-point degradation. The paper addresses this in Section 5.2, attributing it to premature collapse, but does not give practical guidance on how to choose δ₀ and C without running multiple ablations. The analytical approximation (Eq. 2) is stated as a "design aid" but the method for mapping desired patience to (δ₀, C) is not worked through. This brittleness is worth flagging as a practical limitation.

- **Duplicate-reward edge case on small training sets.** Equation (4) applies a small penalty (α₁·r_invalid) when a new heuristic's training-set performance equals that of any heuristic in the prompt context H. On small training sets (e.g., 10 CVRP instances), two structurally distinct heuristics can achieve identical training performance by chance. This case is not discussed, and on CVRP (10-instance training set), such coincidental matches are plausible and would incorrectly penalize genuinely novel heuristics.

### Trivial

- The CALM-API comparison (Section 5.2) states that T=2,000 for non-OBP tasks "matches the query budgets of prior LLM-based AHD methods," but the baselines section states those methods use 1,000 heuristic evaluations. This inconsistency (2,000 vs. 1,000) is never reconciled and creates confusion about whether CALM-API's competitive performance is at parity or at double the budget.

---

## Nice-to-Haves

- **Budget-equalized comparison.** Running MCTS-AHD and EvoTune at 2,000 heuristic evaluations (matching CALM's stated budget) would definitively separate "better method" from "larger budget." If CALM still wins, the claim is airtight. If the gap closes, the contribution can be reframed as equal performance at lower cost—also valuable.

- **Cross-problem transfer experiment.** CALM fine-tunes from scratch on each problem. Initializing CVRP fine-tuning from an OBP-fine-tuned checkpoint would test whether GRPO induces generalizable heuristic priors or only task-specific adaptation. Either outcome—positive transfer strengthening the "co-evolution" framing, or null transfer clarifying the contribution—would meaningfully inform the community.

- **G sensitivity analysis.** A sweep of G (e.g., 4, 8, 16) in the main paper or an accessible section would show how performance and training efficiency trade off, and would clarify the effective budget more transparently.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Wall-clock efficiency not substantiated in main body" (Harsh Critic):** The critic notes that Appendix I contains wall-clock comparison. Per review rules, weaknesses about content in the stripped appendix are removed.

- **"Missing appendix proofs for Eq. 2" (implied):** Appendix G is referenced for the collapse derivation. Since the appendix is stripped by the parser, any criticism of its absence is removed.

- **"The abstract claims surpass API-based models, but model quality and budget are confounded—this is fatal/structural" (Harsh Critic, framing):** The cross-model comparison does conflate model quality and fine-tuning, but the EvoTune comparison clearly separates the effect of CALM's design choices. The confound is real but does not constitute a structural flaw; it is retained as a Major weakness (budget ambiguity), not a Fatal one.

- **"Strength: addresses an important problem"** (Strength Finder): Generic statement about problem importance removed per filtering rules. Retained only concrete, evidence-backed strengths.

---

## Novel Insights

The most novel insight surfaced by this review is the interaction between fine-granularity mutation operators and GRPO's token-level advantage attribution. CALM's operators—injection and replacement—are explicitly motivated by the observation that GRPO rewards/penalizes entire responses but heuristic performance can shift with a single sub-component. By designing operators that hold most of the heuristic fixed and vary targeted components, CALM creates a training signal where GRPO's advantage estimate is more likely to reflect the contribution of the varied part rather than the whole heuristic. This is an underappreciated design principle: the evolutionary search structure can be deliberately shaped to improve the credit assignment quality of the RL algorithm, not just to improve search efficiency. The ablation showing that diversity-less crossover is strictly worse than no crossover at all (Table 4: OBP 1.05% vs. 0.88%) further illustrates how the verbal and numerical gradient mechanisms can actively interfere when poorly coupled.

---

## Suggestions

1. **State G explicitly in Section 5** and clarify whether "2,000 LLM queries" counts prompt submissions or individual response generations. Add the resulting total heuristic evaluations per CALM run so readers can directly compare to the baselines' 1,000-evaluation budget.

2. **Explain the two HSEvo rows in Table 3.** Label them HSEvo (config A) and HSEvo (config B), or clarify their origin. The current unexplained duplication undermines confidence in the table.

3. **Soften the abstract's "outperforms SOTA"** to acknowledge the in-domain OP N=50 result (CALM at 24.22% vs. HSEvo at 23.98%), or explicitly scope the claim to out-of-domain generalization where CALM's advantage is consistent.

4. **Provide a worked example** for selecting (δ₀, C) given a desired expected patience horizon using Eq. 2, so practitioners can configure the collapse mechanism without running a full ablation.

5. **Report G and the number of GRPO rounds** in the reproducibility statement alongside the "1.15% of weights fine-tuned" detail already provided.

---

**Evaluation on key axes:**

- **Originality:** High. First to apply online GRPO fine-tuning within an evolutionary AHD loop; the co-evolution paradigm and credit-assignment-aware operators are genuinely novel.
- **Importance:** High. Enabling AHD on a local GPU without API dependency addresses a real barrier to adoption, and the research question (can RL fine-tuning improve AHD?) is well-motivated.
- **Claims well-supported:** Moderate. Core claim (RL fine-tuning helps) is strongly supported by ablation and EvoTune comparison. Cross-model claims against GPT-4o-mini are muddied by undisclosed G and budget asymmetry.
- **Soundness of experiments:** Moderate-high. Three-run averaging, systematic ablation, and multiple task domains are solid. The budget accounting issue is the primary gap.
- **Clarity:** Good. Method description is clear; GRPO setup (especially G) and budget counting are the main opaque points.
- **Community value:** High. Practical system running on a single consumer GPU, open-source code released, and clear improvement over direct competitor EvoTune.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>