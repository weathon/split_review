Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes ResearchTown, a multi-agent framework for simulating human research communities. The key idea is to model researchers as agent nodes and papers as data nodes in an "agent-data graph," and to define research activities (paper reading, writing, reviewing) as text-based message-passing operations (TextGNN) on this graph. The paper also introduces ResearchBench, a benchmark using masked node prediction to evaluate simulation quality via similarity to ground-truth papers. Experiments on 100 ML papers and 20 interdisciplinary papers show ResearchTown outperforms several baselines on embedding-based similarity metrics, and case studies suggest potential for interdisciplinary idea generation.

## Strengths

- **Novel framework bridging multi-agent LLMs with graph-structured reasoning.** The agent-data graph formulation (Section 3) and TextGNN message-passing framework (Section 4) provide a principled abstraction that unifies heterogeneous entities (researchers, papers) and diverse activities (reading, writing, reviewing) under a single graph-based paradigm. Equations 3–7 formally define how each research stage maps to a specific GNN-like layer, which is a cleaner and more general formulation than typical ad-hoc multi-agent prompting.

- **Graph-derived evaluation paradigm (ResearchBench) that is scalable and objective.** Rather than relying on expensive human evaluation or subjective LLM-as-a-judge, the paper leverages its own graph framing to define a masked node prediction task (Section 6). This is an elegant consequence of the modeling choice — if you model the community as a graph, you get evaluation for free via a standard graph learning paradigm. This allows repeatable, automatic assessment.

- **Quantitative advantage over baselines on the 100-paper subset.** On the ML-bench subset tested, ResearchTown achieves a best@10 similarity score of 0.664 (text-embedding-3-large) and 0.670 (voyage-3) for paper writing, consistently outperforming all four baselines (zero-shot, swarm, AI Scientist, paper-only) by a clear margin (Table 1). The improvement is systematic across both embedding models and all sampling sizes (k=1, 5, 10).

- **Honest self-critique in qualitative analysis.** Section 10 includes a mature discussion of failure modes ("ideas end up being little more than a combination of terms without substantial meaning") and acknowledges that the most "similar" papers aren't always the most valuable. The paper also provides concrete examples of both successes (interdisciplinary ideas) and failures (vague research questions), giving readers a realistic picture of the framework's capabilities and limitations.

## Weaknesses

### Major

- **Evaluation on only ~3.7% of the benchmark's stated size.** The paper builds ResearchBench with 2,737 paper-writing tasks and 1,452 review-writing tasks (Section 7.1), but reports quantitative results on just 100 ML papers (Section 7.2), citing "limited time and cost budget." This is a severe disconnect — a paper cannot claim to validate a framework and benchmark while testing such a tiny fraction of the data. The trends may be real, but at this sample size, the paper draws conclusions ("effective simulation of collaborative research activities") that far outrun the evidence. The authors should either (a) complete the full evaluation or (b) honestly resize the benchmark claim to match what was actually tested.

- **Review-writing evaluation defined but never reported.** The paper carefully defines review evaluation in Equations 7 and 10, and ResearchBench includes 1,452 review-writing tasks. Yet no review evaluation results appear anywhere in the experiments (Table 1 only shows paper writing). This is a significant omission — the paper cannot claim to validate "the research lifecycle including three stages" if one of those stages is never quantitatively evaluated.

- **Baseline comparison conflates the framework's contribution with an information advantage.** ResearchTown conditions generation on the full community graph — author profiles, citation relationships, and reviewer identities. The baselines (zero-shot, paper-only, swarm) do not receive author profile information. For example, "paper-only" inserts cited papers into the prompt but does not model which authors wrote them or their expertise. This means the performance gap could partly reflect the extra information rather than the graph-based multi-agent pipeline. A controlled ablation that gives baselines the same information (author names, profiles, etc.) in unstructured form would isolate the benefit of the framework itself.

- **TextGNN complexity vs. benefit is unclear.** The ablation on aggregation functions (combining two agent functions into one) shows only a 0.4–0.6 drop in text-embedding-3-large and 0.1 drop in voyage-3 — the paper itself says "such a light drop indicates the potential to simplify the aggregation function further." While this is an honest finding, it undercuts the paper's architectural claims. More importantly, the paper does not compare TextGNN against a simpler baseline that directly prompts the LLM with concatenated neighbor text and author profiles (no message-passing, no multi-turn interaction). Without this comparison, it is unclear whether the elaborate GNN framing is the source of improvement or a post-hoc formalization of a straightforward multi-agent strategy.

### Minor

- **Similarity-to-existing-papers metric partially misaligned with the broader goals.** The paper's abstract promises insights into "research idea generation" and "automatic discovery of novel scientific insights," but the main metric rewards papers that are *similar* to existing ones. The paper does acknowledge this tension (Section 10: "valuable ideas that differ from the ground truth") and includes qualitative analysis of non-similar outputs. However, the quantitative backbone remains focused on fidelity over novelty. Adding a diversity or plausibility metric (e.g., distinctiveness from cited papers, LLM-judged coherence) would better match the stated ambitions.

- **The "author contribution insight" is presented as a discovery but is well-known.** The finding that using only first+last authors yields higher similarity than using all authors (Table 2) is framed as "uncovers insights" and "aligned with real-world research communities." While it is defensible as *validation* of the simulation (the simulator mirrors reality), the paper should be clearer that this is a sanity check, not a novel scientific discovery about research communities.

- **Experimental setup limited to a single LLM backbone (GPT-4o-mini).** All experiments use the same backbone. While this is practical, it leaves open the question of whether the findings generalize to stronger or different models. A small-scale replication with GPT-4o or Claude would increase confidence.

- **No analysis of computational cost.** The framework uses multiple LLM calls per generated paper (one per agent per stage). The paper should report average calls, total tokens, and cost per paper so readers can assess practical feasibility.

### Trivial

- The ethical concerns are acknowledged in a single sentence in the introduction. For a system that generates plausible but potentially fabricated research, a more substantive discussion of misuse risks would strengthen the paper, though this is not unusual for a technical framework paper.

- Section numbering jumps from Section 7 to Section 10 (Sections 8–9 appear to be in the appendix that was stripped by the parser).

## Nice-to-Haves

- A controlled baseline that receives the same information as ResearchTown (author names, profiles, citations) in a flat prompt without graph-based message passing, to isolate the framework's contribution.
- A human evaluation (even small-scale, ~50 papers judged by domain experts) to validate that the similarity metric correlates with actual quality.
- A diversity/novelty metric (e.g., distinctiveness from cited works, LLM-judged coherence or plausibility) alongside the fidelity metric.
- Evaluation on the full ResearchBench, or at minimum a principled justification for the 100-paper subset size.
- Replication of the main results on a stronger LLM (e.g., GPT-4o) for a subset of the data.

## Removed Points

These points were flagged during review but are removed or downgraded per policy:

- **"Agent-data graph only instantiated for research communities"** — This is scope creep. The paper's stated domain is research community simulation; asking it to also demonstrate other domains (code repositories, social media) is outside the paper's scope and would turn it into a different paper.
- **"Evaluation does not match stated goals" (as a fatal issue)** — The evaluation (masked node prediction measuring similarity to ground-truth) is a natural consequence of the graph framing and is standard in graph learning. The paper does acknowledge the tension with novelty (Section 10). The mismatch is real but moderate, not fatal.
- **"The author contribution insight is questionable"** — The paper presents this as simulation validation (the simulator aligns with real-world patterns), not as a novel discovery about research communities. The phrasing "uncovers insights" is slightly strong but not misleading.
- **Aggregation ablation criticism as undermining the entire framework** — The ablation shows a specific sub-design choice (combining two agent functions) has little effect. This does not invalidate the broader framework; the paper itself notes the potential for simplification.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel perspective on the work that the authors themselves have not already addressed or acknowledged.

## Suggestions

1. **Prioritize full-scale evaluation.** The single most impactful improvement would be to report results on the full 2,737 papers rather than 100. If budget is truly limiting, provide a power analysis or error bars showing why 100 is sufficient, or downscale the benchmark claim to match what is tested.

2. **Add a controlled baseline.** Create a baseline that receives the same information as ResearchTown (author names + profiles + citations) in a single flat prompt, no GNN structure. This directly tests whether the graph-based multi-agent pipeline adds value beyond extra information.

3. **Report the review-writing results.** The paper defines review evaluation but never presents it. Even a single table with review results would fix this gap.

4. **Add a novelty or plausibility metric.** Complement the fidelity metric (similarity to ground-truth) with a measure of diversity (e.g., distinctiveness from cited papers) or LLM-judged plausibility, to better capture the "idea generation" aspect of the contribution.

5. **Add computational cost reporting.** Report average number of LLM calls, total tokens, and cost per generated paper so readers can assess practical feasibility.

6. **Clarify the "author contribution" finding.** Reframe it as simulation validation rather than discovery about research communities, to avoid overclaiming.

## Score and Decision

**Originality:** Good — the agent-data graph and TextGNN are a novel synthesis of multi-agent LLMs and graph-structured reasoning.

**Importance of research question:** High — simulating research communities is a timely and ambitious goal with potential impact on scientific discovery.

**Claims well-supported:** Partially. The quantitative results on 100 papers show promising trends, but the tiny sample size (3.7% of the benchmark), missing review evaluation, and uncontrolled baselines mean the central claims are only weakly supported.

**Soundness of experiments:** Weak to moderate. The evaluation design (masked node prediction, similarity metric) is reasonable but under-executed (too few samples, missing review results, uncontrolled baselines).

**Clarity of writing:** Good. The framework is clearly formalized with equations and algorithms. The qualitative discussion is honest and well-structured.

**Value to research community:** Moderate. The framework is conceptually interesting and could serve as a foundation for future work, but the evaluation in its current form is too thin to convince the community of its effectiveness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>