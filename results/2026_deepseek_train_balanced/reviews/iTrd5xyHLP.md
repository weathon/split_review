## Summary

LLMatic proposes a Neural Architecture Search algorithm that uses a code-generating LLM (CodeGen-6.1B) as mutation and crossover operators within a dual-archive MAP-Elites Quality-Diversity framework. One archive stores neural architectures (behavioral descriptors: FLOPS, width-to-depth ratio) with test accuracy as fitness, while a second co-evolves prompts and temperatures with curiosity-driven fitness. The method is evaluated on CIFAR-10 (ablation study) and NAS-bench-201 (CIFAR-10, CIFAR-100, ImageNet16-120), claiming competitive results with 2,000 candidate evaluations.

## Strengths

- **Competitive NAS-bench-201 results using a smaller LLM than GPT-4.** Table 1 shows LLMatic (94.26±0.13 on CIFAR-10) outperforms the GPT-4-based GENIUS (93.79±0.09) on all three NAS-bench-201 datasets, using the smaller CodeGen-6.1B model. It reaches within 0.21–2.55 points of the known optimum on each dataset, which is the paper's strongest quantitative evidence.

- **The dual-archive QD design is methodologically novel.** Co-evolving prompts alongside architectures in separate MAP-Elites archives, with curiosity-driven prompt selection that rewards prompt-niche combinations leading to archive insertions, is a creative approach to leveraging LLMs as informed search operators rather than static generators.

- **Ablation study with 30 seeds is thorough.** The paper ablates five variants (network-archive-only, prompt-archive-only, mutation-only, crossover-only, random generation) and examines crossover/mutation probability settings, all with 30 runs — good statistical practice.

- **Demonstrates diversity of discovered architectures.** The network archive contains more than 20 competitive networks across different FLOPS and width-to-depth ratios (Section 4.2), confirming that the QD objective is genuinely satisfied beyond finding a single best architecture.

## Weaknesses

### Major

- **CIFAR-10 test accuracy from the direct ablation study is not reported numerically.** The paper conducts its primary ablation study by training networks from scratch on CIFAR-10 (Section 4), compares variants to each other and references EfficientNet-B0, yet never states the actual test accuracy LLMatic achieves in this setup. Results are shown only in Figure 3 as a curve. The NAS-bench-201 CIFAR-10 numbers (94.26±0.13 in Table 1) *are* reported, but those come from a different, heavily constrained experimental setup (cell-based search space, table-lookup evaluation). For the paper's main evaluation setting, the reader cannot verify what accuracy was actually achieved.

- **The 2,000-vs-8,000 efficiency comparison with EfficientNet-B0 is invalid as presented.** The paper compares its 2,000 evaluations on CIFAR-10 to EfficientNet-B0's 8,000 evaluations, but those 8,000 evaluations were conducted on **ImageNet** during the NAS that discovered EfficientNet-B0, not on CIFAR-10. The paper acknowledges this distinction (line 239: "EfficientNet-B0 was first trained on the ImageNet dataset and then on CIFAR-10 via transfer learning") yet still presents the figures as a head-to-head efficiency comparison. Search budgets across different datasets with different difficulty, input sizes, and training protocols are not commensurable. This comparison should either be removed or clearly labeled as non-comparable.

- **The "2,000 evaluations" metric excludes LLM compute cost, making the efficiency argument incomplete.** The 2,000 figure counts only neural network training runs. Each candidate architecture requires a forward pass through a 6.1B-parameter CodeGen model, which has a non-trivial GPU cost. Traditional NAS baselines (DARTS, Λ-DARTS, random search) do not require an LLM inference per candidate. Without accounting for this cost, the efficiency comparison is not apples-to-apples, and the paper's claim of sample efficiency does not necessarily translate to computational efficiency.

- **The ablation study undermines the claimed necessity of the dual-archive design.** The paper states (line 235): "Mutation-Only-LLMatic and Network-Archive-LLMatic are the closest to LLMatic." Network-Archive-LLMatic removes the prompt archive entirely, and Mutation-Only-LLMatic removes crossover. Both perform nearly as well as the full method. This means (a) the prompt archive — one of the two central architectural contributions — adds only marginal value over the network archive alone, and (b) crossover adds even less. The paper claims the dual-archive cooperative design is essential, but the evidence shows a single-archive variant with mutation achieves comparable results.

### Minor

- **No statistical significance tests on NAS-bench-201 comparisons.** The performance gaps between LLMatic (94.26±0.13), GENIUS (93.79±0.09), and Random Search (93.70±0.36) on CIFAR-10 are within one standard deviation. Without significance testing, it is unclear whether these differences are reliable or simply noise. This is especially important for the ImageNet16-120 results, where LLMatic's rank drops to 11th.

- **Key implementation details deferred to supplementary material.** The 16 system prompts, prompt design methodology, mutation and crossover prompts, and NAS-bench-201 cell generation details are all referenced only in supplementary material absent from the main text. Given that LLM-based methods are highly sensitive to prompt phrasing, the main text should contain at least illustrative examples.

- **No sensitivity analysis for critical hyperparameters.** The curiosity score weights (+1.0, -0.5, -1.0), temperature mutation schedule (increase/decrease by 0.05), archive bounds (set "after experimentation"), and the 0.7/0.3 mutation/crossover probability are all presented without any sensitivity study.

### Trivial

None.

## Nice-to-Haves

- Include at least one example mutation prompt and one crossover prompt in the main paper body.
- Add a cost-aware comparison that acknowledges or accounts for LLM inference overhead.
- Add statistical significance tests (bootstrap or Mann-Whitney U) on the NAS-bench-201 comparisons.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that DARTS (54.30%) is "misleading" as a baseline in NAS-bench-201 comparison.** DARTS is included as a standard baseline in virtually all NAS-bench-201 comparison tables. Including it is standard practice and not misleading. → REMOVED (misunderstands standard practice in the NAS literature)
- **Criticism about "no prior knowledge" claim being undercut by CodeGen's training data.** All LLMs used in NAS are trained on code corpora that may contain architecture patterns; this is an inherent property of any LLM-based NAS approach and not specific to this paper. → REMOVED (not a substantive weakness specific to this paper)
- **Strength claiming "sample efficiency vs. a prior method" (2,000 vs 8,000 evaluations).** As documented under weaknesses, this comparison is invalid because the search budgets were on different datasets. The paper itself acknowledges the issue. → REMOVED (weakness contradicts this claimed strength)
- **Strength claiming "ablation confirms both archives and both operators are necessary."** The paper's own results show the prompt archive adds marginal value and the contribution is narrower than claimed. → REMOVED (weakness contradicts this claimed strength)

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report the numerical CIFAR-10 accuracy from the direct (non-NAS-bench) ablation study** — this is the single most impactful fix. Include a table with mean and standard deviation across 30 seeds.
2. **Restructure or remove the EfficientNet-B0 efficiency comparison.** Either clearly label it as a non-comparable reference point or replace it with a cost-matched comparison on CIFAR-10 against a traditional NAS method.
3. **Acknowledge and account for LLM inference cost** in any efficiency or computational budget discussion.
4. **Add statistical significance tests** on the NAS-bench-201 results to establish whether the modest performance advantages over GENIUS and Random Search are reliable.
5. **Calibrate the contribution claims to match the ablation evidence** — explicitly discuss that the prompt archive adds limited value and reposition the contribution around the network archive + LLM mutation rather than the dual-archive cooperative design.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>