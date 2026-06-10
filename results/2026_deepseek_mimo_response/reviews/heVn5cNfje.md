## Summary
This paper proposes High-Entropy Sum (HES), a training-free metric that sums entropy of the top 0.5% highest-entropy tokens to quantify reasoning quality in long-CoT samples. HES is applied as a unified data selection criterion across SFT, RFT, and RL training paradigms, with the key finding that pruning the lowest 20% by HES consistently outperforms full-dataset training, and that HES-guided RL sampling surpasses full-batch baselines using half the data.

## Strengths
- **Consistent improvement from pruning low-HES data across models, datasets, and domains**: In Table 1 (Qwen3-8B on Open-Math-Reasoning), Highest-HES-80% achieves 35.36% avg vs Full-Dataset's 32.61% (+2.75 points). In Table 2 (DeepSeek-R1-Distilled-7B on OpenR1-Math-220k), Highest-HES-20% at 34.61% beats Full-Dataset at 30.22% (+4.39 points). Tables 3-4 extend this to code (codeforces-cots) and STEM (Llama-Nemotron) domains. This counter-intuitive finding — less data yields better performance — is the paper's most impactful and replicable result.
- **HES uniquely identifies harmful data**: Lowest-HES-20% yields 14.90% in Table 1 (vs 25.89% for Random-20%), and 13.39% in Table 5 global pool k=2 (vs 27.83% for Random). This extreme degradation confirms the metric reliably identifies harmful samples, not merely noisy ones.
- **Effective discriminative ability demonstrated in Figure 1**: HES separates correct (0.29 norm mean) from incorrect (0.68) samples far better than AvgE (0.52 vs 0.53), AvgHE (0.82 vs 0.82), and ES (0.28 vs 0.58). This demonstrates that both the top-p focus and the sum formulation are essential.
- **Cross-model transfer with cost savings**: Using a 0.6B proxy model for HES yields 32.12% on the 8B model (Table 1), comparable to self-selection at 31.14%, reducing inference cost by over an order of magnitude.
- **Comprehensive baseline design**: 12 SFT selection strategies (difficulty, length, multiple entropy variants, forking-only, random controls) thoroughly isolate HES's specific contribution.
- **Cross-paradigm validation is genuinely novel**: No prior work validates a single quality metric across SFT, RFT, and RL, making this a valuable contribution to the data-centric LLM training literature.
- **RL ablation reveals actionable insight**: Table 6 shows curating negative samples hurts (Pos-Rand Neg-Low at 19.76% vs Pos-Rand Neg-Rand at 19.88%), supporting the claim that negative diversity matters in RL training.

## Weaknesses

### Fatal
None

### Major
- **No multi-seed training variance reported**: All experiments report single-run results. Key margins are small: Table 1 Highest-HES-20% vs Highest-ES-20% is 31.14% vs 30.92% (0.22 points); Table 5 RFT gains average 1–1.7 points; Table 6 RL gain is 21.30% vs 20.63% (0.67 points). Without at least 3-seed variance, it is difficult to distinguish signal from noise for these margins. This is the most important gap — it affects the credibility of all quantitative claims, particularly the RL and RFT results where margins are smallest.
- **RL experiments limited to single small model (1.5B)**: Table 6 trains only DeepSeek-R1-Distilled-Qwen-1.5B on DeepScaleR. The SFT section is far more thorough (two models at 8B and 7B, two math datasets, code and STEM domains). This asymmetry weakens the "unified framework" claim — the RL contribution reads as a pilot study rather than a validated result comparable to the SFT evidence.

### Minor
- **Mechanism remains correlational**: The argument flows from discriminative ability (Figure 1: HES separates correct from incorrect) to training value (experiments show HES-selected data trains better). These are distinct properties — a sample could have high HES due to genuine complex reasoning or model confusion. Direct evidence (gradient norm analysis, qualitative examples of high-vs-low HES reasoning traces) would strengthen the causal story.
- **No explicit quantification of HES computation overhead**: The paper claims HES is "training-free" and the proxy model result (0.6B for 8B selection) partially addresses cost, but no quantification of inference cost on the full training set (FLOPs, wall-clock time relative to training duration) is provided. For practitioners considering adoption, this matters.
- **The 0.5% percentile lacks theoretical motivation**: Sensitivity analysis confirms p=0.005 consistently works best (Figures 3-4), but no intuition connects this threshold to structural properties of reasoning chains. It remains an empirical hyperparameter.
- **RFT gains are modest and inconsistent across individual benchmarks**: In Table 5 per-query k=2, HES beats Random on 6/8 benchmarks but ties or loses on GPQA (40.30 vs 40.50) and HMMT24 (28.13 vs 28.54). The global-pool results are more convincing (HES is the only method beating random where length and difficulty fail), but per-query gains average only +1.01 points.

### Trivial
None

## Nice-to-Haves
- Qualitative examples of 2–3 high-HES vs low-HES reasoning traces with annotated entropy values would make the paper more intuitive.
- A limitations section acknowledging (a) need for inference-time logit access, (b) focus on reasoning-heavy domains, (c) correlational mechanism.
- A second RL model size (e.g., 7B) to strengthen the unified claim.
- Brief analysis of what fraction of total training compute HES scoring adds.

## Removed Points
These points are flagged to be removed, treat them with caution:
- KL divergence argument ordering in Section 2.1 — likely a parser artifact; notation is internally consistent.
- Missing related works — cannot verify external references; removed per rules.
- Missing appendix/proofs — parser strips appendices; they exist in the original submission.

## Novel Insights
A notable observation from the synthesis: HES is dramatically better at identifying *harmful* data (Lowest-HES-20% at 14.90%, massively below random's 25.89%) than at identifying the *best* data (Highest-HES-20% at 31.14%, only modestly above random in many benchmarks). This asymmetry — HES excels as a quality filter but is weaker as a top-k selector — is under-discussed in the paper but has practical implications: the most reliable use of HES is pruning the bottom 20%, and the paper's strongest results (Highest-HES-80% beating Full-Dataset) are consistent with this interpretation. The paper would benefit from explicitly framing HES primarily as a noise-removal tool rather than a best-sample selector.

## Suggestions
- Add 3-seed training runs for key conditions (Full-Dataset, Random-20%, Highest-HES-20%, Lowest-HES-20%) on at least one model/dataset pair. This single addition would substantially strengthen all claims.
- Add 2–3 qualitative examples of high-vs-low HES reasoning traces with entropy annotations.
- Strengthen RL with at least a 7B-scale experiment or multi-seed variance on the 1.5B model.
- Add a brief limitations paragraph.

## Calibration Anchors

**Round 1 (bracketing, range 6.0–7.0):**
- EOPLy80bBm (3.00, Reject): Data pruning disentanglement — purely analytical, no practical metric. HES paper is clearly stronger.
- qUJsX3XMBH (4.40, Reject): "Random Selection is Almost All You Need" — shows most methods fail to beat random at scale. HES paper demonstrates consistent improvements, clearly stronger.
- SpTzsQjgxF (5.75, Reject): Rule-based rating with DPP — more complex framework but weaker empirical results and missing baselines. HES paper is simpler and stronger.
- f4gF6AIHRy (8.00, Accept): DiSF — stronger theoretical grounding (submodular optimization), comprehensive ablations, 98.5% data savings. Clearly above HES paper.

**Round 2 (narrowing):**
- Fty0wTcemV (6.00, Accept): DELIFT — data selection across fine-tuning stages, scores 6/6/6. HES paper has broader paradigm coverage and stronger SFT evidence; somewhat better.
- BTKAeLqLMw (6.33, Accept): DEITA — data selection for alignment, scores 8/6/5. Limited evaluation on AlpacaEval/MT-Bench; HES paper has more rigorous benchmark evaluation. Comparable overall.
- 3OyaXFQuDl (7.00, Accept): "Smaller, Weaker, Yet Better" — compute-optimal reasoning data, scores 8/8/6/6. More theoretical grounding and more thorough methodology; slightly above HES paper.
- 3NnfJnbJT2 (7.00, Accept): GIO — gradient information optimization for data selection. Different methodology but comparable contribution level.

**Final score rationale:** The HES paper sits between the 6.0–6.3 anchors (DELIFT, DEITA — which it slightly exceeds in empirical breadth and practical impact) and the 7.0 anchors (which have stronger theoretical grounding). The consistent cross-paradigm SFT results and the practical proxy-model transfer are genuine strengths. The lack of variance and the weak RL section prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>