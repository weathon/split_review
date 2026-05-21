---
job_id: 1e652dc6-c493-45f5-8b6b-ee3e1dd18fac
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: dIOYpj9K8P.pdf
paper: Reformulation for Pretraining Data Augmentation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on large-scale language model pretraining, synthetic data generation, data augmentation, and data-constrained scaling.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, discussion, and conclusion. While I have substantial concerns about evaluation rigor, positioning, and some underspecified methodological choices, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other apparent manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes MGA, a two-stage genre-audience reformulation pipeline for synthetic pretraining data augmentation. Starting from FineWeb-Edu within SmolLM-Corpus, the authors generate a 770B-token MGACorpus by first producing multiple genre-audience pairs per document and then reformulating the source text under those directives using smaller finetuned tool models. The paper evaluates MGA against repetition and upsampling baselines across model sizes up to 13B and reports improved benchmark performance and better scaling behavior in data-constrained regimes, while also providing analyses of prompt design, validation loss behavior, and complementarity with other synthetic data sources.

## Strengths
1. The paper tackles an important practical problem for LLM pretraining, namely what to do when high-quality unique data is limited and naive repetition starts to hurt. This is a real bottleneck, and the paper is asking a useful question rather than inventing a benchmark-shaped toy problem.

2. The overall pipeline is reasonably clear at a high level. **Figure 1** on Page 2 does a good job of communicating the two-stage design, namely adaptive genre-audience generation followed by controlled reformulation and cleaning. Even though some implementation details remain underspecified, the core idea is easy to understand from the diagram and surrounding text.

3. The empirical section is broad in model scale and training regime. The scaling experiments in **Figure 3** on Pages 6-7 are the most convincing part of the paper. In both the entire-set repetition and subset-repetition settings, the MGA curves appear consistently above repetition or upsampling baselines, and the gap generally widens with model size. This is stronger evidence than a single fixed-budget table.

4. **Table 2** on Page 6 shows consistent average improvements from replacing a large portion of fineweb-edu-dedup with MGACorpus at fixed token budgets. The gains are modest for 134M and 377M, but they become more meaningful at 1.7B, where the average rises from 41.15 to 43.4 relative to the authors’ reproduced baseline. This size-dependent improvement is at least directionally consistent with the paper’s claim that reformulation helps more as models scale.

5. The paper does not overclaim MGA as a universal replacement for all synthetic data. The discussion in Section 4.3.1 and **Figure 4** positions MGA as complementary to other synthetic corpora. That is a more credible framing than pretending one recipe wins everywhere.

6. The attempt to distill the generation process into smaller “Tool SLMs” is practically relevant. **Table 1** suggests the tool model tracks the LLM teacher reasonably closely on the authors’ 1-5 scoring setup, with only about a 1-point absolute drop in the rate of outputs scoring at least 3. For a web-scale pipeline, that efficiency angle matters.

7. The prompt-design ablation is useful in spirit. **Figure 2** and **Table 3** jointly support the claim that an overly relaxed reformulation policy is harmful, while an overly strict one may reduce diversity too much. Even if I am not fully convinced by the exact analysis tools, the paper is at least trying to isolate why the method works rather than only reporting one best setting.

## Weaknesses
1. The main empirical comparisons do not cleanly isolate whether the gains come from “reformulation” or simply from changing the data mixture toward more synthetic, lower-repetition content. This is my biggest issue. In **Table 7** on Page 17, the baseline uses fineweb-edu-dedup at \(195 \times 4.15\) epochs, whereas MGA-Expansion uses both fineweb-edu-dedup and MGACorpus at \(0.84\) epochs each. That means the comparison changes at least three things at once: repetition count, source distribution, and synthetic-vs-real composition. The paper argues this is the point, but scientifically it weakens the causal claim that genre-audience reformulation itself is the operative factor. A stronger design would include matched controls where the repetition count is equalized and the only difference is whether the extra tokens are MGA rewrites versus other rewrite styles or alternative synthetic expansions of the same source.

2. The evaluation suite is heavily benchmark-centric and does not directly measure the paper’s central factual-faithfulness claim. The stated principle in Section 3.1 is “Limited Consistency”, balancing variance and invariance, but there is no direct quantitative evaluation of factual preservation at corpus scale in the main paper. **Table 3** on Page 8 reports teacher-judged quality scores, but these scores are generated under a permissive rubric that explicitly states omitted information and substantial deviation do not reduce the score unless the text becomes unrecognizable as a rewrite. That is a very weak definition of factual fidelity. Since the core claim is that MGA preserves “core factual information” while expanding style and structure, I expected a more direct measure of factual consistency, entity retention, contradiction rate, or even human evaluation focused on content preservation rather than broad acceptability.

3. The paper’s main quality evaluation relies too heavily on self-judging by the same LLM family used in the pipeline, which is not very reassuring. In **Table 1** on Page 4, the “Labeler LLM” evaluates both itself and the Tool SLM, and the human check is described only as “alignment rate of over 90%” without details on sample size, protocol, annotator expertise, or what exactly was aligned. This matters because the training and filtering decisions in Section 3.2 are downstream of these judgments. If the judge is biased toward its own writing style or blind to factual distortions, then the curated set \(\mathcal{D}_{\text{SFT}}\) may optimize the wrong target.

4. The mathematical formulation in Section 3.2 is too thin to support some of the surrounding claims, and key pieces are underspecified. On Page 5, the filtered dataset is defined as
\[
\mathcal{D}_{\text{SFT}}=\{(D,G,D')\in\mathcal{D}_{\text{synth}} \mid S(D')\ge 3\},
\]
followed by a standard SFT loss
\[
\mathcal{L}_{\text{SFT}}(\theta)=\mathbb{E}_{(D,G,D')\sim\mathcal{D}_{\text{SFT}}}[-\log P_\theta(D' \mid D,G)].
\]
This is mathematically fine as far as it goes, but it does not formalize the central “Limited Consistency” tradeoff at all. There is no objective involving diversity, consistency, or any explicit balancing parameter. The actual mechanism is prompt engineering plus post-hoc filtering, which means the conceptual core of the method is only informally described. If the paper wants to present “Limited Consistency” as more than a slogan, it should be explicit about what quantities are being optimized or constrained, how quality filtering affects the induced training distribution, and why the threshold \(S(D') \ge 3\) is the right operating point rather than an arbitrary heuristic.

5. Several of the analyses use suggestive visualizations without enough methodological grounding. **Figure 2** on Page 4 uses t-SNE to argue that the base prompt “achieves a balanced expansion of the original data distribution,” while strict and relaxed variants are too conservative or too shifted. This is a very fragile claim to base on t-SNE plots, since those visualizations can change substantially with perplexity, initialization, embedding choice, and sample composition. The paper does not specify in the main text what embeddings were projected, how many points were used, or whether the observed separation is stable across runs. As written, the figure is visually appealing but not strong evidence of distributional balance.

6. Some of the strongest reported gains are on tasks whose improvements can plausibly come from task-format alignment rather than better general pretraining. In **Table 2**, the TriviaQA gain for 1.7B jumps from 4.95 to 20.42, which is enormous compared with the average gain of +2.25. The paper itself speculates that diverse phrasings improve reasoning, but that is not the only explanation. Because MGA explicitly generates varied genres such as tutorials, reports, pedagogical texts, and audience-targeted expositions, it may simply inject more QA-friendly or instruction-like formats. Without a more careful task-by-task attribution or controls against format matching, the reasoning narrative feels too convenient.

7. The complementarity experiment in Section 4.3.1 is interesting but not fully convincing as presented. **Figure 4** on Page 7 claims a hierarchy \( \text{Exp C} > \text{Exp A} > \text{Exp B} > \text{Baseline} \), but the main paper does not provide a table with exact benchmark numbers, variance, or even aggregate values for that figure. For a paper making a synergy claim, this is surprisingly underreported. The reader is asked to trust a plotted trend without the granular evidence needed to judge effect size consistency or significance.

8. The paper’s discussion of validation loss versus benchmark performance is intriguing, but the “different learning strategy” explanation remains speculative. In Section 4.3.3, **Figures 6 and 7** are used to argue that higher validation losses do not necessarily mean collapse, and that the model may prioritize more generalizable contextual patterns instead of memorization. That is possible, but the evidence shown is not yet sufficient to support this interpretation. The “first anomaly position” metric is introduced only later and depends on a thresholded window statistic over token-level loss differences. In the main paper, this feels post-hoc and somewhat hand-crafted. The examples in the supplement suggest boilerplate and noisy web tails may contribute, but in the main text the conclusion is stronger than the evidence.

9. The paper is not especially well positioned against closely adjacent recent work on synthetic pretraining under data constraints. The related work section cites several important papers on rewriting and synthetic corpora, but the positioning remains broad and somewhat vague. Given that the paper’s headline claim is about improved scaling in data-bound regimes, the comparison to recent systematic studies of synthetic-data scaling and controlled synthetic pretraining recipes is thinner than it should be. This matters because some of the contribution is empirical framing rather than a fundamentally new algorithm, so careful positioning is part of the scientific value.

10. There are a number of presentation issues that make the paper read more like an internal project report than a polished conference submission. A few examples: Section headings switch style awkwardly, several passages are grammatically rough, and some claims are phrased with more confidence than the evidence warrants. The qualitative examples in Appendix E are also a bit alarming: many reformulations contain clear fluency issues, repetitions, or nonsensical insertions like “Aneuploidy” and duplicated “Stress”. Since these examples are the closest look we get at actual generations, they undercut the paper’s narrative that the reformulations are broadly high quality.

## Questions
1. Can the authors provide a cleaner control experiment where the repetition count and token budget are matched, and the only difference is whether the added tokens come from MGA versus another rewrite strategy applied to the same source documents? This would substantially increase my confidence that the gains are due to the genre-audience mechanism rather than to reduced repetition or generic synthetic expansion.

2. What exactly is the embedding space and setup used for **Figure 2**? Please specify the encoder, sample size, preprocessing, t-SNE hyperparameters, and whether the pattern is stable across seeds. If there is a quantitative companion metric beyond the visualization, that would be much more convincing.

3. How much human evaluation was done for the filtering and teacher-judge validation process in **Table 1** and **Table 3**? I would like concrete numbers: annotator count, sample count, rubric, agreement, and whether factual inconsistency was separately annotated from style quality.

4. The threshold \(S(D') \ge 3\) in Equation filtering is central to dataset construction. Did the authors test \(S \ge 4\) or a soft weighting scheme such as
\[
\mathcal{L}(\theta)=\mathbb{E}_{(D,G,D')\sim \mathcal{D}_{\text{synth}}}\left[w(S(D')) \cdot -\log P_\theta(D' \mid D,G)\right]
\]
with \(w(\cdot)\) increasing in the score, instead of hard-thresholding at 3? This would help clarify whether the chosen cutoff is principled or just convenient.

5. For the large TriviaQA and GSM8K gains in **Table 2**, can the authors rule out task-format contamination or alignment effects? For example, how often do MGA outputs adopt QA-like, tutorial-like, or step-by-step pedagogical forms compared with the original corpus?

6. In **Figure 4**, please provide the exact benchmark numbers and preferably uncertainty estimates for Exp A/B/C. The current figure is suggestive, but the synergy claim would be much easier to evaluate with a full table.

7. The examples in Appendix E show notable fluency degradation in some reformulations. How frequent are such failures in the final corpus after cleaning, and what proportion of generated documents are discarded? Even a rough rejection rate would help.

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper expands web-derived text into a 770B-token synthetic corpus, and the source is based on FineWeb-Edu / SmolLM-Corpus. At this scale, synthetic rewriting can preserve or amplify source biases, stereotypes, copyrighted content patterns, and personally identifying information that may survive upstream filtering. Because MGA explicitly reformulates content for different audiences and styles, there is also some risk of laundering problematic source material into more fluent or more persuasive variants rather than removing it. The paper mentions broader impact only briefly in the limitations section on Page 15, mostly around hallucinations and bias, but does not give concrete auditing or mitigation procedures for bias propagation, privacy leakage, copyrighted material, or harmful content transformation. I do not see this as a reason to reject on its own, but it does warrant ethics review.

## Soundness Rating
3: good. The empirical results are substantial and mostly support the claim that this data recipe can outperform repetition and some alternative baselines, but the causal attribution to the specific MGA mechanism is not fully nailed down, and several analyses are more suggestive than rigorous.

## Presentation Rating
2: fair. The paper is understandable and the high-level narrative is clear, but there are notable writing issues, some underreported experimental details, and several places where the evidence shown is weaker than the confidence of the claims.

## Contribution Rating
3: good. The problem is important, the scale of experimentation is meaningful, and the paper offers a practically relevant synthetic-data recipe. However, the contribution feels more like a strong systems/data recipe plus empirical study than a sharply isolated methodological advance.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem and includes broad experiments that suggest the method is useful in practice, especially in data-constrained scaling settings. I remain unconvinced on several scientific points, particularly whether the gains are truly due to the proposed genre-audience reformulation mechanism, how faithfully content is preserved, and how strong the supporting analyses really are. Still, the empirical evidence is strong enough that I lean weakly positive.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the surrounding literature on LLM pretraining, synthetic data, and data-constrained scaling, though some implementation details are missing and prevent a fully definitive judgment.