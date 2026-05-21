Now let me write the consolidated review.

## Summary

MoEP (Modular Expert Paths) proposes a sparse decoder-only architecture that interleaves two dense GPT-2 layers with a parallel block stack operating at reduced dimension, connected by MoE shrink/grow projections with top-k routing. The method adds sparsity without increasing the total parameter count (all models use 28M parameters). Evaluated on the BabyLM strict-small track (<100M training tokens), MoEP achieves a macro average of 49.00 (excluding AoA) compared to the official GPT-2 baseline at 46.60 and the authors' own GPT-2 at 48.10, while the GPT-BERT baselines score 52–54. The paper also provides training dynamics analysis showing faster early pattern discovery.

## Strengths

- **Fixed parameter count with added sparsity.** Table 2 confirms that MoEP and the GPT-2 baseline both have 28M total parameters, demonstrating that MoEP introduces MoE-style sparsity without the typical parameter explosion of standard MoE. This is a clean architectural property worth investigating.

- **Faster early pattern discovery evidenced by checkpoint analysis.** Appendix A.3 (described in Section 5.1) shows that MoEP reaches its peak evaluation performance at 30M words (after only ~3 epochs), whereas the GPT-2 baseline's best scores are scattered across different checkpoints. The paper documents that "MoEP extracted useful patterns earlier during training," supporting the claim that modular sparse routing can improve sample efficiency even if final scores converge. This is potentially the most interesting finding.

- **Honest discussion of overfitting and scope.** The appendix provides a clear account that after the 30M-word peak, MoEP's performance degrades with continued training (e.g., Entity Tracking stabilizes below the mean), and Section 6 acknowledges the uncertainty about scaling to larger, more complex data. The authors also candidly compare linear vs. SwiGLU experts and find that lightweight linear projections outperform the more complex SwiGLU variant at this scale (28M-param MoEP beats 38M-param MoEP-SwiGLU).

- **Systematic positioning within MoE placement literature.** Section 2.2.2 organizes prior work by expert placement strategy (FFN-level, attention-level, attention+FFN, layer-level) and correctly identifies layer-level MoE as relatively unexplored in pre-training settings, providing clear context for MoEP's novelty.

## Weaknesses

### Fatal
None. The paper makes a coherent architectural proposal, and no verified error invalidates its core claims entirely.

### Major

- **The claim of "outperforming all BabyLM strict-small baseline models" in the abstract and introduction is misleading.** Table 1 shows that GPT-BERT variants achieve substantially higher macro averages excluding AoA (54.10, 53.65, 52.40) than MoEP (49.00). Lines 35–36 in the introduction state "MoEP was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well" without qualification. The body text (Section 5.1) does clarify that this holds "when the AoA task score was included in the Macro Average," but the abstract and introduction do not carry this qualification. A reader skimming the high-level statements takes away an unsupported claim of dominance. The authors must either report the comparison honestly in the abstract/intro or drop the claim.

- **Improvement over the primary baseline (GPT-2) is marginal without statistical evidence.** MoEP's macro average excluding AoA is 49.00 against the authors' own GPT-2 at 48.10 — a gap of 0.9 points. The authors note that their GPT-2 "slightly outperformed the BabyLM GPT-2 baseline... reaching performance near comparable to MoEP," confirming the margin is thin. No confidence intervals, error bars, or multi-seed experiments are reported. For a paper proposing a novel architecture, a 0.9-point gap from a single run is insufficient to demonstrate practical benefit.

- **No ablation study isolates the contribution of individual components.** MoEP differs from the GPT-2 baseline in multiple ways simultaneously: parallel blocks, MoE shrink/grow projections, reduced hidden dimension, top-k routing at two levels (parallel blocks and MoE experts), and a load-balancing auxiliary loss. The only variant tested (MoEP-SwiGLU) changes expert type and increases parameters from 28M to 38M, which confounds the comparison. Without ablations, it is impossible to determine whether the gains come from the parallel architecture, the routing, the dimension reduction, or simply better training of a comparable-size dense model.

### Minor

- **Single small-scale evaluation with unclear relevance to the motivating scale.** The paper trains on <100M tokens with 28M-parameter models, while the motivation (Llama 4, DeepSeek, GPT-OSS) describes large-scale MoE systems. The authors acknowledge this limitation in the conclusion but do not provide any evidence or argument that the approach would scale. The gap between the framing (efficiency at scale) and the evidence (small-scale benchmark where dense models match or exceed MoEP) weakens the significance of the contribution.

- **Training dynamics analysis is relegated to the appendix.** The claim of "faster early pattern discovery" (contribution 3) is potentially the paper's most interesting finding, but the main text contains only a qualitative summary. The actual figures and quantitative analysis are in Appendix A.3. This evidence should be in the main body to support the claimed contribution.

- **No computational cost comparison despite an efficiency framing.** The paper motivates MoEP through efficiency and sparsity but never reports FLOPs, inference speed, throughput, or memory usage. The parallel blocks and MoE routing introduce overhead that is not measured. Efficiency claims are untestable without such data.

- **Routing behavior analysis is absent.** Contribution (3) is listed as "analyze expert networks routing behavior," yet the paper contains no load histograms, no specialist/expert-utilization patterns, and no discussion of whether routing learns meaningful specialization. The analysis in Appendix A.3 covers training dynamics (checkpoint-wise task scores), not routing behavior.

### Trivial

- The load-balancing loss (Eq. 2) is the negative entropy of the routing distribution, which encourages uniform routing indirectly. This differs from the standard auxiliary load-balancing loss used in most MoE papers (e.g., Switch Transformers' importance + load terms). A brief clarification would help.

- Table 2 shows a typo: "Liner" instead of "Linear" for the MoE FF type.

## Nice-to-Haves

- **Ablations**: Running a baseline that removes the parallel architecture (single MoE layer at full dimension) or removes the routing (all parallel blocks always active) would clarify which design choices drive performance.
- **Multi-seed runs**: Reporting results with 3–5 seeds would establish whether the 0.9-point gap over the authors' GPT-2 is reproducible.
- **FLOPs/throughput measurement**: Providing wall-clock or FLOPs comparison would substantiate the efficiency motivation.
- **Routing specialization analysis**: Visualizing which experts/blocks different token types are routed to would strengthen contribution (3).

## Removed Points

These points were flagged by the reviewers but are removed or demoted for the reasons stated:

- *"Fragmented sentence about recent works"* and *"hasty writing"*: The apparent sentence fragment on line 19 is a PDF-extraction artifact, not an author error. Removed per the formatting-artifact rule.

- *"Model parallelism not defined"*: The paper's usage ("model parallelism with MoE-style linear projections" in the abstract) is clear enough in context — it refers to the parallel blocks, not distributed training parallelism. Removed as insubstantial.

- *"Load-balancing loss is not the standard one"*: While technically correct (the entropy regularizer differs from the Switch Transformers auxiliary loss), entropy-based balancing is a valid alternative and the equations are clearly presented. Demoted from a claimed critical issue to a trivial clarification.

- *"Checkpoint selection criterion unspecified"*: The paper states the final checkpoint had "best evaluation performance." While more detail would help, the core logic is understandable. Demoted from a reported weakness to a minor clarity point.

- *"Reproducibility flagged due to placeholder URLs"*: The paper contains generic github.com and huggingface.co URLs. Per the rules, reproducibility concerns that question code release status should not be treated as author errors when the paper states the code will be released. Removed.

- *"Strength Finder claim that MoEP outperforms all BabyLM baselines"*: This strength conflicts with verified weakness #1 (the claim is misleading for GPT-BERT models). Removed and replaced by the honest characterization above.

- *"Strength Finder claim that the paper addresses an important problem"*: Generic and lacking specific evidence. Removed.

## Novel Insights

The most interesting observation that emerges from combining the reviews is that MoEP's apparent advantage is not in final accuracy (where it beats GPT-2 by ≤1 point and trails GPT-BERT by 3–5 points) but in training dynamics: the architecture reaches peak evaluation performance at 30M words versus the staggered, task-dependent convergence of GPT-2. This faster early learning could be valuable in data-constrained regimes, but the paper does not isolate whether this stems from the parallel architecture, the routing, or simply the reduced dimensionality. The fact that MoEP-SwiGLU (more complex experts) underperforms MoEP (linear experts) despite having 10M more parameters is also a noteworthy result that challenges the intuition that more expressive experts are always better at small scales. However, both observations need controlled ablations to become more than speculation.

## Suggestions

1. **Fix the misleading claim in the abstract and introduction.** State honestly that MoEP outperforms the GPT-2 baseline and achieves competitive results with GPT-BERT on AoA-weighted metrics, or restrict the claim to GPT-2 comparison only.

2. **Add at minimum two controlled baselines**: (a) a single MoE layer at full dimension with the same number of experts/total parameters (isolates the parallel-block design), and (b) a dense GPT-2 with the same reduced hidden dimension (isolates whether the gains come from sparsity or simply from operating at a smaller dimension).

3. **Report results over multiple seeds (3–5)** for MoEP and the authors' GPT-2, with mean and standard deviation, to establish whether the 0.9-point gap is meaningful.

4. **Move the training dynamics analysis (Figure 3/4) from the appendix to the main paper** if faster learning is claimed as a contribution.

5. **Report a computational cost comparison** — even a simple throughput (tokens/second) measurement would support the efficiency motivation.

6. **Add routing behavior analysis**: Show expert/block utilization histograms or per-token-type routing patterns to substantiate contribution (3).

## Score and Decision

**Calibration report:**

*Round 1 (bracketing):* Queried papers on small-scale MoE and BabyLM benchmarks:
- **Weak band (<3.5):** NanoMoE (3.0, Reject), TinyStories (3.0, Withdrawn), MOEfication (3.4, Withdrawn), EfficientSkip (2.5, Withdrawn)
- **Middle band (3.5–7.5):** SMALLTALK LM (7.33, Spotlight), MoE+Instruction Tuning (6.75, Poster), Compressing LLMs (6.75, Poster), Scaling Laws (6.67, Poster)
- **Strong band (>7.5):** OLMoE (8.67, Oral), Sparse Autoencoders (8.20, Oral), Small-scale Proxies (8.00, Oral), DEPT (8.00, Oral)
- **Initial bracket:** 3.5–5.5

*Round 2 (narrowing):* 
- NanoMoE (3.0, Reject): Replaces FFN layers with low-rank MoE blocks, only compares to low-rank baselines. MoEP is stronger — it uses proper benchmarks (BabyLM) and has clearer architecture description.
- MoIN (4.5, Reject): Semantic routing with LoRA adapters, weak baseline comparisons, insufficient experimentation. MoEP is roughly comparable.
- Free-MoE (3.5, Reject): Tuning-free MoE approach with unclear method description and notation issues. MoEP is stronger — methodology is clearer, evaluation is more systematic.
- Dense Backpropagation (5.5, Reject): Novel routing gradient approximation, evaluated at 2B params/200B tokens. MoEP is weaker — smaller scale, no ablation studies, misleading claims.
- ReMoE (6.6, Accept Poster): ReLU-based differentiable router, strong experimentation across model sizes. MoEP is substantially weaker — lacks the experimental rigor and breadth.
- MOEfication (3.4, Withdrawn): Sparsification via masks, compared against single baseline. MoEP is stronger.

*Final score determination:* The paper has a genuinely interesting architectural idea and a credible evaluation pipeline, but it is undermined by a misleading claim in the abstract/intro, a marginal improvement over the primary baseline with no significance testing, and a complete lack of ablations. It is clearly stronger than the 3.0/3.5 rejected papers (NanoMoE, Free-MoE) but weaker than the 5.5 rejected Dense Backpropagation paper and far below the 6.6 accepted ReMoE paper. The score is set at 4.0.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>