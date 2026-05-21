---
job_id: 2f85c41c-ceb8-4764-9c5b-6d713b3d9209
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: RDAhLHEHDm.pdf
paper: Lost in Tokenization: Context as the Key to Unlocking Biomolecular Understanding in Scientific LLMs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies how scientific LLMs represent and reason over biomolecular inputs, which is directly relevant to representation learning, multimodal/hybrid AI systems, and ML applications in biology.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, related work, methodological framing, experiments, quantitative/qualitative results, and conclusion/limitations; while I have several concerns about overclaiming and evaluation design, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other obvious attempts to manipulate automated or human review in the provided paper content.

# Expected Review Outcome:
## Summary
This paper argues that current Sci-LLMs struggle with a “tokenization dilemma” when biomolecular sequences are provided directly, either as tokenized text or as a separate modality aligned to language models. The authors propose a context-driven alternative in which standard bioinformatics tools, such as InterProScan, BLASTp, and ProTrek, are used to convert a raw protein sequence into structured textual context, and they compare sequence-only, sequence+context, and context-only inputs across several Sci-LLMs and general LLMs. The main empirical claim is that context-only consistently performs best on their protein QA benchmark, while adding the raw sequence often hurts performance.

## Strengths
The paper has a clear and provocative central thesis. The framing around “sequence-as-language,” “sequence-as-modality,” and “context-driven” inputs is easy to follow, and **Figure 1** on Pages 2-3 is genuinely useful in conveying the conceptual distinction between the three paradigms. Even though I have concerns about how strong the resulting conclusions should be, the problem formulation is memorable and likely to spark discussion.

The empirical comparison in **Table 1** on Page 6 is broad enough to be interesting. The authors evaluate multiple specialized Sci-LLMs and multiple general-purpose LLMs under three input configurations. That breadth is valuable, and the table does make a real point: sequence-only performance is weak on this benchmark for most tested models, while adding structured biological context dramatically helps. Regardless of whether one agrees with the stronger interpretation, the raw observation is important.

I also appreciated that the paper does more than report top-line scores. The representation analyses in **Figure 2** and **Figure 3** attempt to open the black box a bit. In particular, **Figure 3** offers a concrete mechanistic hypothesis for why a sequence-as-modality model may lose useful structure during alignment, and this is more informative than simply stating “alignment is hard.”

The ablation in **Table 3** in the appendix is also a useful sanity check on the proposed pipeline. It shows that not all context sources are equally helpful, and that a naive “throw everything in” strategy can hurt. That is a more credible story than claiming every external knowledge source monotonically improves performance.

The paper is generally readable. The experimental story is coherent, the limitations section does acknowledge a major blind spot around mutation sensitivity, and the work is positioned as an empirical challenge to a prevailing design choice rather than a new large model.

## Weaknesses
My main concern is that the paper repeatedly overstates what has actually been demonstrated. The comparison is framed as evidence that “raw biomolecular sequences act as informational noise” and that current sequence-centric paradigms are “fundamentally handicapped,” but the actual setup mostly shows that **retrieved high-level annotations from mature bioinformatics systems are extremely useful for answering annotation-like questions**. Those are not the same claim. On Page 5, the context is built using InterProScan, BLASTp against Swiss-Prot, and a fallback retrieval model. This means the “context-only” input is not just a different representation of the same information, it is a tool-augmented pipeline that injects curated external knowledge and homology-derived annotations. In contrast, the sequence-only baseline asks the LLM to infer function from sequence alone. That is an inherently asymmetric comparison. The result is still interesting, but the paper sometimes sells it as a verdict on sequence modeling, when it is at least equally a verdict on the power of retrieval from curated biological databases.

This asymmetry matters directly for interpreting **Table 1** on Page 6. The table is the centerpiece of the paper, and the gains are indeed large, but the task itself is tightly coupled to the sources used in context construction. The benchmark asks about function, pathway, and subcellular localization, and the context pipeline explicitly supplies GO terms, Pfam domains, and homolog-derived evidence, which are already close to the answer space. In that light, the most defensible conclusion from **Table 1** is not that tokenization is the central bottleneck, but that expert-derived contextualization is a very strong tool-augmented baseline for these QA tasks. The paper would be much stronger if it were more disciplined about this distinction.

A second serious issue is the evaluation methodology. The main protein QA results in Section 5.1 rely on an LLM-based judge, “LLM-Score,” whose details are deferred to Appendix C. On Pages 18-19, the judge is described as DeepSeek-V3 scoring generations against database excerpts. This is a weak point for two reasons. First, the paper does not report any human evaluation or agreement analysis to justify that this metric is reliable for nuanced biological answers. Second, one of the evaluated systems in **Table 1** is itself Deepseek-v3. Even if the judge is used in a separate role, this setup raises avoidable concerns about evaluator bias or affinity to the response style of one family of models. A paper making such sweeping claims about the failure of sequence-centric Sci-LLMs should not rest so heavily on a single LLM-as-judge metric without stronger validation.

Third, the paper does not sufficiently address possible knowledge leakage or memorization routes. The authors state on Page 6 that when using BLASTp they read GO annotations from homologous sequences rather than the query protein’s own record, which is good, but this does not resolve the broader issue. The context generation pipeline retrieves from Swiss-Prot and related curated resources, and the questions themselves are derived from explicit annotation fields. For many test proteins, especially older ones, the contextual evidence may be extremely close to a paraphrase of the ground truth. This is not necessarily invalid, but then the paper is benchmarking a retrieval-and-synthesis system rather than isolating biological reasoning capacity. The problem becomes even more pronounced in the time-split analysis of **Figure 4** on Pages 8-9, where performance for older proteins is partly explained by richer database support. That undermines the sweeping interpretation that the superiority is due primarily to native alignment with language, rather than simply more available external evidence.

Fourth, several of the paper’s mathematical formulations are too loose to support the conceptual claims attached to them. In Section 3 and Section 4, **Equations (1)-(6)** are presented as if they formalize the three paradigms, but the notation is more rhetorical than rigorous. The most obvious issue is **Equation (6)** on Page 5,
\[
P(a \mid s,q) \approx P(a \mid c,q),
\]
where \(c = \mathcal{C}(s)\). This approximation is exactly the core empirical claim of the paper, not a justified modeling identity. No conditions are stated for when this approximation should hold, how much information loss is tolerated, or how it depends on the task. Similarly, **Equation (5)** defines the input as \([T_{\text{text}}(q); T_{\text{text}}(c)]\), which is fine operationally, but then the paper slides from “we feed the model context” to “we circumvent the tokenization dilemma entirely.” That jump is not established mathematically or experimentally. If the equations are meant to be conceptual, they should be presented more carefully as abstractions, not as if they formalize a theorem-like argument.

Fifth, the representation analysis is suggestive but not as probative as the paper implies. In **Figure 2** on Page 7, the authors compare ARI scores after clustering embeddings against homolog-based ground-truth clusters. The problem is that the “Ours” representation is derived from textual context that already contains functionally meaningful descriptors extracted by tools such as Pfam/GO. It is therefore unsurprising that this representation separates proteins in a way aligned with homology or function. This does not cleanly prove that sequence representations are intrinsically weak; it may simply show that explicit functional annotations are easier to cluster than downstream LLM outputs conditioned on raw sequences. Likewise, **Figure 3** is visually consistent with the claim that Evolla loses structure through alignment, but there is no statistical analysis showing robustness across proteins, seeds, or alternative metrics. These figures are interesting diagnostics, not decisive evidence.

Sixth, the “sequence + context hurts” claim is overstated. There are cases where the drop is meaningful, for example Intern-S1 and Evolla in **Table 1**, but for some models the difference is tiny. For **Gemini2.5 Pro**, context-only is 87.19 versus 86.98 for sequence+context, which is effectively negligible absent variance estimates. For **GPT-5**, the difference between 76.45 and 75.76 is also small. Yet the text on Pages 6-7 repeatedly uses language such as “consistently act as informational noise” and presents the effect as a general law. Without confidence intervals, repeated trials, or significance tests, the paper should be much more cautious here.

Seventh, the efficiency claims in **Table 2** on Page 9 are not fully convincing as presented. The comparison mixes very different resources and assumptions, including CPU tool execution plus API calls for the proposed method, versus a GPU-only baseline for Evolla. The batch-mode result claiming approximately \(0.13\) seconds per sequence for the context-driven pipeline is especially striking, but the main paper does not explain how database access, tool startup costs, indexing overhead, or engineering amortization are handled. Since the claimed practical advantage is part of the paper’s pitch, this section needs a more transparent apples-to-apples accounting in the main text, not just a pointer to Appendix M.

Eighth, the wet-lab validation in Section 5.6 is potentially interesting but underdeveloped in the main paper. **Figure 5** and **Figure 6** on Page 10 show sample-level outcomes for Rhodopsin and PETase classification, but the paper does not state the sample sizes in the main text, does not clarify how “absence from major databases” was verified in a way relevant to LLM pretraining, and does not explain how context was generated for truly unpublished proteins if the standard homology/domain tools still rely on existing databases. This is exactly the kind of result that could strengthen the paper, but in its current form it reads more like an appealing anecdote than a rigorous validation.

Ninth, the paper’s novelty is somewhat narrower than the rhetoric suggests. The actual methodological contribution is a deliberately assembled tool-augmented prompting pipeline using standard biological databases and tools, plus an empirical comparison against sequence-centric prompting. That is useful, but it is not a new learning method, and the strongest contribution is really in the diagnosis and benchmark-style comparison. I do not object to that kind of paper in principle, but the manuscript would benefit from toning down statements such as “lays the foundation for a new class of hybrid scientific AI agents” unless the evaluation more directly supports such breadth.

Tenth, the scope of the conclusions is narrower than the title and abstract imply. Most main-text evidence is about proteins, mostly annotation-oriented tasks, and often cases where decades of biological prior knowledge can be surfaced by homology or domain searches. The paper does acknowledge on Page 10 and in Appendix J that mutation-sensitive settings are a weakness, and this is not a side issue. Many biologically important tasks turn on subtle sequence differences. If the context pipeline is insensitive to such differences, then the claimed reframing of Sci-LLMs as “reasoning engines over expert knowledge” may be appropriate for a subset of tasks, but not for biomolecular understanding broadly construed.

## Questions
1. The central empirical comparison in **Table 1** would be much more convincing if the authors could quantify how often the generated context contains near-paraphrases of the ground-truth annotation. Can the authors report an explicit leakage audit, for example lexical or semantic overlap between the context and the answer field, broken down by task?

2. Since the main metric is an LLM judge, can the authors provide stronger validation of the “LLM-Score”? Concretely, what is the agreement between the DeepSeek-V3 judge and human biologists on a representative subset, and does the model ranking remain stable under a different adjudicator LLM?

3. For the “sequence + context hurts” claim in **Table 1**, can the authors report variance estimates or repeated runs? The gaps for some models, especially Gemini2.5 Pro and GPT-5, look small enough that I am not comfortable interpreting them as robust evidence of informational noise without uncertainty bars.

4. Regarding the formulation in **Equation (6)**, under what assumptions do the authors believe
\[
P(a\mid s,q)\approx P(a\mid c,q)
\]
should hold? Is the claim task-dependent, and can the authors better delimit the regime where context is expected to preserve the relevant information?

5. For **Figure 2** and **Figure 3**, can the authors provide more methodological detail in the main paper: number of proteins used, whether the visualization is stable across random seeds and t-SNE hyperparameters, and whether the ARI conclusions hold under alternative embedding evaluations beyond clustering?

6. For **Table 2**, please clarify whether the reported cost and time include all practical overheads of running InterProScan/BLASTp at scale, including database setup, I/O, and failed or slow queries. The current presentation makes the proposed pipeline look extremely efficient, but the comparison is hard to assess fairly.

7. For the wet-lab experiments in Section 5.6, what are the sample sizes per family, how exactly was “unpublished and absent from major databases” verified, and what context was available for these sequences if they were truly novel? A precise answer here could materially increase my confidence.

8. More broadly, I would like the rebuttal to sharpen the paper’s claim. Is the intended conclusion “current Sci-LLMs are weak de novo sequence interpreters on annotation-style QA,” or the much stronger statement that raw sequences are generally a harmful representation for biomolecular reasoning? My opinion would improve if the authors narrowed the claim to what is directly supported.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
I did not identify a concrete ethics issue in the submission that requires separate ethics review based on the main paper.

## Soundness Rating
3: good. The experiments are substantial and the main empirical pattern is real, but the evaluation design, asymmetry of the comparison, and overinterpretation of the evidence prevent a higher soundness score.

## Presentation Rating
3: good. The paper is readable and well organized, and several figures/tables are helpful, but some claims are rhetorically stronger than what the evidence supports, and parts of the mathematical formalization are too loose.

## Contribution Rating
3: good. The paper offers an interesting and useful empirical reframing, especially for tool-augmented biological QA, but the contribution is more diagnostic and benchmark-like than the paper’s broader language suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper makes an interesting and potentially useful empirical point, and it will likely stimulate discussion in the community. However, the current version overclaims, and the main comparison conflates representation choice with access to curated external biological knowledge.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main technical concerns, particularly around evaluation design, interpretation of the comparisons, and the strength of the conclusions.