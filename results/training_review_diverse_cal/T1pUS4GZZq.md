## Summary

This paper introduces a Large Recurrent Action Model (LRAM) with an xLSTM core for offline multi-task RL, trained via behavior cloning on 894M transitions from 432 tasks across 6 domains. The central hypothesis is that modern recurrent architectures (xLSTM, Mamba) are better suited as backbones for large action models than Transformers, along two dimensions: final performance and inference efficiency. The paper demonstrates that xLSTM/Mamba achieve competitive or better normalized scores than a GPT-2-style Decision Transformer across four model scales, and provides clear empirical evidence that xLSTM maintains constant per-step latency regardless of context length while the Transformer runs out of memory at long sequences—a result with direct practical relevance for real-time robotics.

## Strengths

- **Clear inference speed advantage demonstrated under realistic conditions.** The latency and throughput experiments (Figures 4–6) are the paper's strongest contribution. They show that xLSTM maintains constant per-step latency independent of context length, while a matched-parameter Transformer with KV-caching goes out-of-memory at ~16K timesteps (45K tokens) for batch size 64 and at even shorter contexts for larger batches. This directly validates the practical motivation (real-time control at 100–1000Hz requiring <10ms inference) and is a convincing, well-designed comparison.

- **Large-scale, multi-domain empirical study.** Training on 894M transitions from 432 tasks spanning vision-based (Atari, Procgen) and state-based continuous control (DMControl, Meta-World, Mimicgen, Composuite) is a substantial effort that provides breadth of evidence. The consistent trend—recurrent architectures matching or exceeding the Transformer across model sizes and domains—strengthens the claim that the finding is not domain-specific.

- **Practical design insight: removing actions from the input representation.** The ablation showing that omitting actions from the input sequence improves performance on continuous-control robotics domains (by preventing shortcut learning via oversmooth action predictions) is a concrete, actionable finding validated across multiple backbones. This refines the standard Decision Transformer formulation for robotics and is the kind of empirical contribution that saves future practitioners significant trial-and-error.

- **Performance advantage across scales is present but should be read with the caveat in Weaknesses.** The scaling plots (Figure 1) show recurrent architectures outperforming the Transformer in both validation perplexity and normalized evaluation scores at 16M–206M parameters, with the gap widening at larger scales. While the lack of error bars tempers confidence, the consistency of the trend across all four sizes is suggestive.

## Weaknesses

### Major

1. **No measure of variability in the core performance comparison.** The scaling results in Figure 1 (validation perplexity and normalized evaluation scores) are presented as single curves with no error bars, confidence intervals, or multiple seeds. Given that the gaps between architectures at smaller scales (16M–48M) are modest, and the evaluation aggregates normalized scores across 432 diverse tasks with different reward scales, it is impossible to assess whether the observed differences are systematic or within the noise of a single run. This is the most significant methodological weakness because it directly affects the paper's central claim about performance. The paper does not discuss this limitation or justify single-run evaluation.

2. **Fine-tuning and ICL experiments do not support the claimed scope of the contributions.** The paper's contribution list includes assessing architecture choice for fine-tuning and ICL, but:
   - **Fine-tuning** (§4.2): Only compares a *pretrained* xLSTM to a *randomly initialized* xLSTM on held-out tasks. This shows that pretraining helps, which is expected, but says nothing about whether the *choice of backbone* (recurrent vs. Transformer) affects fine-tuning quality. The claim that "fine-tuning performance is not negatively affected by switching the backbone" (§4.2) does not follow from an experiment that never switches the backbone.
   - **ICL** (§4.2): Only compares recurrent architectures (xLSTM variants and Mamba) against each other on a single small grid-world (Dark-Room), with no Transformer baseline. The conclusion that xLSTM "may enable applications that require long context lengths, such as in-context RL" is not supported by the ICL experiment as presented.
   
   These experiments are not worthless—they provide sanity checks—but they are positioned as supporting a broader claim than the data warrants. The Limitations section does partially acknowledge this (§5: "we only consider a limited grid-world setting"), but the paper's introduction and abstract do not convey the narrow scope of these results.

### Minor

3. **Mamba parameter mismatch is acknowledged but not addressed.** The paper notes (line 271) that "Mamba has a significantly higher number of parameters than competitors" in the scaling comparison, but provides no analysis of how this affects interpretation. If Mamba is larger, its comparable-or-worse performance relative to xLSTM actually strengthens the case for xLSTM's efficiency, but a reader cannot verify this without knowing the exact parameter counts at each "size" tier. This is a methodological gap that the paper could easily close by reporting parameter counts for each architecture at each tier and briefly discussing the implications.

4. **Normalization scheme lacks transparency.** The paper reports "data-normalized scores" for most domains and "human-normalized scores" for Atari, but does not specify which policies/returns were used as the min and max references, whether the normalization is consistent across domains, or how the domain averages in Figure 2 are computed. This makes the absolute scale of reported numbers opaque and hinders reproducibility and comparison with future work.

### Trivial

5. **Embedding space analysis (Figure 5) is purely qualitative.** The claim that xLSTM exhibits "more refined domain separation" is based on visual inspection of UMAP plots. This could be quantified with silhouette scores or similar metrics. As presented, it is suggestive but not evidence.

6. **The DT baseline input modification could be stated more prominently.** The paper modifies the standard Decision Transformer input representation by removing actions from the sequence (Section 3.2). All backbones use this same representation, so the comparison is fair across methods. However, a reader skimming the experiments section could miss this and assume the paper uses the *exact* DT setup. A brief explicit statement in Section 4 ("All backbones use the modified sequence representation described in Section 3.2") would prevent confusion.

## Nice-to-Haves

- Per-domain results (Figure 2) would benefit from some measure of variance across tasks within each domain, even if multi-seed training runs are infeasible.
- The ICL experiment would be more informative if it included a Transformer baseline, even if trained at a smaller scale, to calibrate the absolute performance of the recurrent models.
- Reporting exact parameter counts for Mamba alongside the stated "model size" tiers would address the parameter mismatch concern without requiring re-runs.

## Removed Points

- **Criticism that "the DT baseline is not the standard Decision Transformer" as a weakness:** The paper clearly describes the input modification in Section 3.2 (line 160: "We omit actions in our sequence formulation"), and all backbones use the same modified representation. The comparison is fair across methods; the concern about potential misinterpretation is a presentation preference, not a substantive weakness. Moved to Trivial (#6).
- **Strength Finder's claim about "In-context learning improvement via state-tracking":** The ICL experiment only compares recurrent architectures to each other, lacks a Transformer baseline, and is on a single small grid-world. Calling this a core strength overstates the evidence. Dropped.
- **Strength Finder's claim about "Embedding space analysis revealing domain separation":** The analysis is qualitative (UMAP visual inspection) and conflicts with the verified weakness that it could be quantified. Dropped as a core strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tensions (error bars vs. computational cost; scope of claims vs. experimental coverage) that are standard for large-scale empirical papers in this space.

## Suggestions

1. Add a brief discussion of statistical uncertainty to the paper, even if multi-seed runs are infeasible. State the expected variance based on related work and acknowledge single-run evaluation as a limitation.
2. Either add cross-architecture comparisons to the fine-tuning and ICL experiments, or explicitly reframe the contributions to match the narrower scope (e.g., "we verify that recurrent backbones support fine-tuning and ICL" rather than "we assess the effect of backbone choice on fine-tuning/ICL").
3. Report the exact parameter counts for all architectures at each size tier, and explain whether the "model size" labels refer to matched hidden-dim/layers or matched total parameters.
4. Document the normalization reference policies (min/max) for all domains in an appendix or repository README.
5. Add silhouette scores or cluster purity metrics to support the embedding space analysis, or remove the qualitative claim.

## Score and Decision

This is a solid empirical paper with a clear practical contribution: the inference-speed experiments convincingly show that recurrent architectures enable real-time deployment where Transformers fail under realistic robotics constraints. The scaling comparison is directionally informative, though the lack of error bars tempers confidence in the precise performance advantage. The fine-tuning and ICL sections are the weakest parts and do not support the breadth implied by the contribution list.

The paper is well-motivated, the primary experiments (scaling + inference) are conducted at an unusually large scale, and the core finding—that xLSTM enables fast inference without sacrificing task performance—has genuine practical value for robotics. The weaknesses are addressable and do not invalidate the main contributions.

**Decision: Accept** (with recommendations for the above revisions, particularly addressing the error bars/uncertainty discussion and tightening the scope of the fine-tuning/ICL claims).

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>