Now I have a thorough understanding of the paper and can verify all claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces SPaR, a self-play framework that uses tree-search refinement to construct preference pairs for improving instruction-following in LLMs. The key insight is that independently sampling multiple responses for DPO training introduces irrelevant content variation (e.g., different stories) that distracts from learning what matters — whether the instruction is followed correctly. SPaR instead refines a model's own failed responses via tree search, producing preference pairs that differ minimally except for instruction-following correctness. Experiments on LLaMA3-8B/70B, GLM-4-9B, and Mistral-7B show consistent gains over self-rewarding, meta-rewarding, SELF, and AutoIF baselines. After three iterations, the LLaMA3-8B model surpasses GPT-4-Turbo on IFEval.

---

## Strengths

- **Synthetic experiments causally isolate the benefit of refinement pairs (Figure 4).** On two controlled tasks (character sequence generation and start/end story generation), refinement pairs (minimal variation) substantially outperform interfering pairs (independent sampling). In the story task, interfering pairs even underperform the original model, while refinement pairs improve steadily. This directly supports the paper's central causal claim: minimizing irrelevant variation is critical for effective preference learning in instruction-following.

- **Ablation studies confirm the necessity of each component (Tables 4, 5).** Removing tree-search refinement drops SPAR-8B-DPO-iter3 on IFEval from 81.3% to 77.4%, and skipping iterative training degrades both actor and refiner. These ablations isolate the contribution of the proposed framework cleanly.

- **Strong empirical gains across multiple backbones and iterations (Table 1, Figure 3).** SPAR-8B consistently outperforms established self-improvement baselines (Self-Rewarding, Meta-Rewarding, SELF, AutoIF) across every iteration. The improvements hold across LLaMA3-8B, LLaMA3-70B, GLM-4-9B, and Mistral-7B, and general capabilities (GSM8k, TriviaQA, MMLU, HumanEval) are maintained or improved.

- **Test-time compute scaling analysis (Figure 5).** Tree-search refinement at inference time yields better returns than best-of-N generation at similar compute budgets, showing that refinement is a more effective use of additional computation for instruction-following — a practically useful finding beyond the core training contribution.

- **Iterative self-improvement of the refiner (Tables 2, 3).** After three iterations, SPAR-8B-RFT-iter3 matches GPT-4o-Mini on refinement accuracy (79.0% under GPT-4o evaluation) and surpasses it on adversarial judgment subsets of LLMBar (66.0% vs. 56.8%). This demonstrates that the refiner can self-evolve beyond its initial bootstrapping data.

---

## Weaknesses

### Fatal
None.

### Major

- **The headline claim of surpassing GPT-4-Turbo on IFEval rests on a comparison that may not be controlled.** The paper reports that SPAR-8B-DPO-iter3 "surpasses GPT-4-Turbo (81.3% average accuracy)" on IFEval, but it is unclear whether GPT-4-Turbo was evaluated under the exact same protocol by the authors. Scores marked with † in Table 1 are acknowledged as sourced from original papers. If the GPT-4-Turbo number is an external result, differences in IFEval evaluation setup (strict vs. loose, prompt-level vs. instruction-level, verifier version) could affect comparability. The gap appears narrow, and no confidence intervals or significance tests are provided. This does not undermine the framework's value — the comparisons against Self-Rewarding, Meta-Rewarding, SELF, and AutoIF are clean and favorable — but the paper's strongest advertised result lacks the evidential rigor it deserves. The authors should directly evaluate GPT-4-Turbo under identical conditions or qualify the claim more carefully.

### Minor

- **Data contamination risk between training prompts and test sets is unaddressed.** The 43K training prompts are derived from Infinity-Instruct (a large Internet corpus) with constraints added by a strong LLM. The paper reports no n-gram overlap analysis or filtering against IFEval, FollowBench, or LLMBar test sets. Given that the method's gains are concentrated on these benchmarks, this is a missing rigor check. An exact-match overlap analysis would meaningfully raise confidence (and likely find no issues, which would be good to report).

- **Self-evaluation bias in the refiner is acknowledged but its impact on training data quality is not assessed.** Table 3 shows that when the refiner self-evaluates, it reports 90.5% refinement accuracy vs. 79.0% when GPT-4o evaluates. The paper notes this discrepancy but does not analyze whether the preference pairs used for DPO training contain systematic errors from an overconfident refiner. The self-consistency mechanism (majority voting) addresses random noise but not systematic bias. Sampling a few hundred training pairs for external evaluation (e.g., by GPT-4o) would address this gap.

- **Tree-search hyperparameters are underspecified for reproducibility.** The paper explains the BFS/DFS approach at a conceptual level but does not report concrete values for: branching factor (number of refinements generated per node), maximum search depth, or which search strategy (BFS vs. DFS) was used for the main experiments. These details are necessary for faithful reproduction and for interpreting ablation results (e.g., Table 7 comparing tree search to best-of-N refinement).

- **The "strong LLM" used for bootstrapping is not named until Table 3 (Section 3.4), despite being referenced repeatedly in Section 2.2.** The paper uses "a strong LLM" throughout the data construction methodology; only the refiner evaluation table reveals it is GPT-4o-Mini. Naming it earlier with exact version and API settings would improve clarity and reproducibility.

- **No confidence intervals or error bars on any main result.** While single-run evaluation is common for large-scale benchmarks, the narrow margins (e.g., the GPT-4-Turbo comparison) would benefit from some measure of variability (e.g., bootstrap resampling over IFEval instructions).

### Trivial

- The sentence "SPAR-8B-DPO-iter3 even surpasses GPT-4-Turbo $81.3\%$ average accuracy)" on line 154 has a minor formatting issue (missing opening parenthesis before "81.3%").

---

## Nice-to-Haves

- A breakdown of the string-level similarity claim (0.90 vs. 0.85 for refinement vs. independent pairs) by constraint type (formatting vs. content changes) would sharpen the mechanistic argument — higher similarity could also indicate trivial refinements that are easier to learn.
- Reporting the average number of LLM calls per successful refinement (compute cost) would help practitioners assess practical overhead.
- Reporting standard LLMBar pairwise scores alongside the adapted pointwise scores would provide full comparability with the literature.

---

## Removed Points

- **"Overstates novelty"** — Removed because this is a generic positioning critique without a concrete anchor in the paper. The paper clearly distinguishes its approach from independent sampling in prior self-rewarding work.
- **"Baseline comparison may be across different experimental conditions"** — Removed because the paper appears to compare against baseline methods using the same backbone (LLaMA3-8B-Instruct) in Figure 3, which is a within-setup comparison. The critic's concern about reproduce/re-implement is speculative.
- **"Adaptation from pairwise to pointwise on LLMBar may change difficulty"** — Removed because the paper clearly states the adaptation and the comparison is primarily against the same adapted setup across models, which is internally valid.
- **"Missing computational cost discussion"** — This is a nice-to-have, not a weakness that harms validity.
- **"Statistical significance missing"** — Moved to Minor but downgraded from the critic's framing because single-run evaluation is standard practice in this area.
- **"String-level similarity breakdown"** — Moved to Nice-to-Haves.

---

## Novel Insights

The reviews do not surface any genuinely novel insight beyond the paper's own contributions. The harsh critic's observation that the tree-search mechanism produces adversarially robust refiners (through exposure to similar responses with opposite labels during search) is already discussed in Section 3.4 of the paper. The synthetic experiment design (Figure 4) is the paper's own contribution and is correctly identified as compelling evidence by both reviewers.

---

## Suggestions

1. **Controlled GPT-4-Turbo evaluation**: Run GPT-4-Turbo through the exact same IFEval evaluation pipeline used for SPAR models and report the result side-by-side. If the number matches the cited 81.3%, this puts the comparison on solid ground. If it differs, report both.
2. **Report tree-search hyperparameters**: Specify branching factor, maximum depth, and whether BFS or DFS was used in each experiment.
3. **Add a contamination analysis**: Report exact-match and near-match n-gram overlap between the 43K training prompts and the IFEval/FollowBench/LLMBar test sets.
4. **Audit preference pair quality**: Have GPT-4o (or a human) label a 200-sample subset of the DPO training pairs to estimate the error rate from refiner self-evaluation bias, and show that the method is robust to this noise level.
5. **Name GPT-4o-Mini explicitly in Section 2.2** when describing bootstrapping.

---

## Score and Decision

**Originality**: Solid — the idea of constructing preference pairs by minimizing irrelevant variation through tree-search refinement is a genuine step beyond independent sampling approaches.  
**Importance of research question**: High — instruction-following with multiple constraints is practically critical.  
**Claims well supported**: Mostly yes, with the caveat that the GPT-4-Turbo comparison needs tighter controls.  
**Soundness of experiments**: Strong — multiple backbones, benchmarks, ablations, and a clean synthetic experiment.  
**Clarity of writing**: Clear and well-structured.  
**Value to community**: Clear contribution — the code/data release, the synthetic experiment design, and the test-time compute analysis are each independently useful.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>