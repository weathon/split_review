Now I have sufficient comparison data. Let me synthesize the final review.

## Summary

CALM proposes a framework for automatic heuristic design that co-evolves the LLM alongside heuristics through GRPO-based reinforcement learning. Unlike prior LLM-based AHD methods that keep the LLM frozen and rely solely on prompt manipulation ("verbal gradients"), CALM fine-tunes the LLM on-the-fly using the heuristic evaluation signal as a reward, introducing "numerical gradients." The framework includes fine-granularity mutation operators (injection, replacement), a diversity-aware crossover, a collapse mechanism to escape local optima, and a carefully designed progressive reward function. Running on a single 24GB GPU with a quantized 7B model, CALM outperforms SOTA API-based baselines across four optimization problems (OBP, TSP, CVRP, OP). 

## Strengths

- **Novel co-evolution paradigm**: CALM is the first AHD framework to jointly optimize both prompt generation and LLM parameters through RL. This distinguishes it from all prior work, which kept the LLM frozen. The paper provides a clear conceptual argument for why co-evolution matters (lines 42–44: "the evolutionary loop naturally produces abundant prompt-response-performance triplets… By using this signal as feedback for reinforcement learning, we can fine-tune the LLM") and validates it through ablation (Table 4: removing GRPO increases OBP gap from 0.71% to 1.78%).

- **Comprehensive empirical validation**: The evaluation spans four distinct optimization problems (OBP, TSP, CVRP, OP) across multiple scales including out-of-domain instances, with comparison against 8+ baselines covering hand-crafted heuristics, NCO methods, and LLM-based AHD approaches including the concurrent EvoTune. CALM consistently achieves SOTA or near-SOTA results — e.g., on CVRP at N=200, it reduces the gap from 4.70% (MCTS-AHD) to 3.95% (Table 3).

- **Thorough ablation study**: Table 4 systematically isolates the contribution of each component — RL fine-tuning, collapse mechanism (with multiple hyperparameter configurations), and individual operators (diversity-aware crossover, injection, replacement, simplification). This provides strong evidence that each design choice is justified.

- **Verbal gradient alone is competitive**: CALM without GRPO but using GPT-4o-mini API achieves results competitive with or better than MCTS-AHD across all tasks (Tables 1–3), demonstrating that the prompt-generation operators and sampling strategies are highly effective independently of RL (Section 5.2, lines 229–234).

- **Practical resource efficiency**: The framework runs on a single 24GB GPU with an INT4-quantized Qwen2.5-7B model fine-tuning only 1.15% of weights (lines 144–148), making it accessible without costly API calls while still surpassing API-based methods.

- **Reproducibility**: Code is publicly released, complete algorithms and prompts are provided in the appendix, and hyperparameters are specified.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Training cost not reported in main text**: The paper emphasizes resource efficiency (single 24GB GPU, INT4 quantization, no API costs) but does not report wall-clock time or GPU-hours in the main body. This information is deferred to Appendix I (line 276), but the efficiency claim would be more convincing with at least high-level numbers in the main evaluation. Without this, readers cannot assess the practical tradeoff between local fine-tuning cost and simply calling a stronger API model.

- **Mild overstatement on TSP results**: The abstract and conclusion state that CALM "outperforms" or "outmatches" SOTA API-based baselines. On TSP at the in-domain scale (N=50), CALM's 10.04% gap is slightly behind MCTS-AHD's 9.69% (Table 2). The body text correctly qualifies this (line 177: "achieve the second-best LLM-based result on the in-domain set"), but the abstract/conclusion should be tempered to reflect this domain-specific result.

- **Inaccurate table header label**: In Tables 2 and 3, the row grouping "LLM-based AHD: Qwen2.5-7B-Instruct-INT4 (w/. GRPO)" includes EvoTune, which uses DPO rather than GRPO (as acknowledged in Section 2, line 56). The label should use "w/. fine-tuning" to avoid misleading readers about EvoTune's training method.

### Trivial

- **Reward terminology inconsistency**: Section 4.3 describes the duplicate-heuristic case as receiving "a small but consistent reward (α₁ r_invalid)" (line 140). Since r_invalid ∈ (−1, 0) and α₁ ∈ (0, 1), the resulting value is negative, making "reward" technically a misnomer. The intent is clear but the wording could be tightened.

## Nice-to-Haves

- Reporting the rate of invalid LLM responses and whether this rate changes under fine-tuning would strengthen the evaluation of the reward design and learning dynamics.
- A brief sensitivity analysis of the reward-function hyperparameters (r_invalid, α₁, α₂) in the main text (currently in Appendix I per line 276) would reassure readers that results are not artifacts of careful tuning.
- Quantifying the fraction of generated heuristics that are valid, novel, and superior to their parents over the course of training would make the learning dynamics more transparent.

## Removed Points

These points were flagged in input reviews but removed from the final assessment:

- **"Training cost is not reported" originally framed as a potentially fatal evidential gap** — demoted to Minor because: (1) the paper does include this information in Appendix I (line 276), so the gap is one of presentation (main text vs. appendix), not omission; (2) the paper already provides substantial evidence for resource efficiency (24GB GPU, INT4 quantization, 1.15% weights, no API costs).

- **"The comparison on TSP does not fully support the claim of outmatching all SOTA API-based baselines" originally framed as a major concern** — demoted to Minor because the body text already correctly qualifies the TSP results. The overstatement is limited to the abstract/conclusion and affects only one sub-result across four tasks.

- **Demand for confidence intervals, statistical tests, and larger-scale validation** (general sweep concerns from the harsh critic template) — removed because the paper reports results averaged over three runs with standard deviation (Figure 2), and p-values/statistical significance are addressed in Appendix I (line 276). The evaluation across 4 problems at multiple scales already exceeds the norm for this subfield.

- **Concerns about "missing appendix" or "missing proofs"** — removed per hard rules; appendices are stripped by the parser and exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, this review process surfaces an interesting pattern: the combination of verbal guidance (prompt-level operators) and numerical guidance (RL fine-tuning) appears to be synergistic rather than merely additive. The fact that CALM without GRPO using GPT-4o-mini API already matches or exceeds MCTS-AHD, while adding GRPO on a weaker quantized model pushes performance substantially further, suggests that these two guidance modalities operate on complementary dimensions of the search process — verbal guidance explores the heuristic space structurally, while numerical guidance adapts the generator's inductive biases. This dual-gradient paradigm may generalize beyond AHD to other LLM-based search and optimization problems.

## Suggestions

- Move the key training-cost numbers (GPU-hours, wall-clock time for a full run) from Appendix I into Section 5 to directly support the resource-efficiency claim.
- Temper the abstract's TSP claim to "matches or surpasses" rather than "outperforms," or add a brief qualifier about the in-domain result.
- Change the table header "w/. GRPO" to "w/. fine-tuning" to accurately describe EvoTune.

## Score and Decision

### Round 1 — Bracketing

I queried for LLM-based automatic heuristic design papers across three bands:

- **Weak band (<3.5)**: LLM4Solver (3.40), MHRE (2.50), Starjob (3.00), Symbolic/Black-box (3.00). CALM is substantially stronger than all of these — these papers have fundamental gaps (missing baselines, weak evaluation, incremental contributions). None are close comparators.

- **Middle band (3.5–7.5)**: Hercules (5.25), LLM-LNS (5.25), HeurAgenix (3.80), CADO (5.75). CALM is clearly stronger than Hercules and LLM-LNS, which reviewers criticized for incremental novelty and missing ablations. CADO (5.75) introduces RL fine-tuning for diffusion models in CO but reviewers noted marginal improvements and simplicity. CALM offers a more novel paradigm (co-evolution), broader evaluation, and more thorough ablations.

- **Strong band (>7.5)**: MaestroMotif (7.75), LLAMBO (8.00), LLM-SR (8.00), WizardMath (8.00). These are polished, high-impact papers. CALM is comparable in execution quality but has minor presentation weaknesses (training cost in appendix, slight overstatement) that place it slightly below the 8.00 tier.

**Initial bracket**: Between 6.5 and 8.0.

### Round 2 — Narrowing

I pulled anchors inside (5.5, 7.0) and (6.5, 8.5):

- **EvoPrompt (6.50, Accept)**: LLM + EA for prompt optimization. CALM is stronger: harder problem domain (heuristic design vs. prompt engineering), more novel contribution (RL co-evolution vs. LLM-as-operator), better ablation, and stronger results relative to baselines.

- **LASeR (6.25, Accept)**: LLM-aided evolutionary search for robot design. CALM is stronger: broader evaluation (4 problems vs. single-domain voxel robots), more significant gains over baselines, more thorough ablation.

- **Learning Performance-Improving Code Edits (7.25)**: Different domain (code optimization via dataset curation), well-executed. CALM shows comparable execution quality but with a more novel algorithmic contribution.

- **OctoPack (7.33)**: Instruction tuning for code LLMs. Well-executed but different paradigm. CALM's contribution is comparably significant.

CALM sits above EvoPrompt (6.50) and LASeR (6.25), and at a level comparable to or slightly above the 7.25 anchor. It does not quite reach the polish and impact of LLAMBO/LLM-SR (8.00), which are cleaner contributions with no presentation gaps. Score: **7.5**.

### Anchor Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LLM4Solver (XTxdDEFR6D) | 3.40 | R1 | CALM is far stronger — broader evaluation, better novelty, more thorough ablation |
| MHRE (sUywd7UhFT) | 2.50 | R1 | CALM is far stronger — single vs. multi-objective different scope but CALM's execution is superior |
| Hercules (0fwJMANq9P) | 5.25 | R1 | CALM stronger — RL co-evolution is more novel than core abstraction prompting, broader ablation |
| LLM-LNS (Usk4KzBxLW) | 5.25 | R1 | CALM stronger — LLM-LNS lacks ablation studies, narrower evaluation |
| CADO (pbDqZBn2X2) | 5.75 | R1 | CALM stronger — more novel paradigm, broader problem coverage |
| EvoPrompt (ZG3RaNIsO8) | 6.50 | R2 | CALM stronger — harder problem, RL innovation beyond LLM-as-operator |
| LASeR (7mlvOHL6qJ) | 6.25 | R2 | CALM stronger — broader evaluation, more significant gains |
| Code Edits (ix7rLVHXyY) | 7.25 | R2 | CALM comparable in execution quality, more novel algorithmic contribution |
| OctoPack (mw1PWNSWZP) | 7.33 | R2 | Different domain but CALM's contribution is comparably significant |
| MaestroMotif (or8mMhmyRV) | 7.75 | R1 | CALM slightly below — MaestroMotif has cleaner presentation |
| LLAMBO (OOxotBmGol) | 8.00 | R1 | CALM below — LLAMBO is more polished, no presentation gaps |
| LLM-SR (m2nmp8P5in) | 8.00 | R1 | CALM below — LLM-SR is a cleaner contribution |

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>