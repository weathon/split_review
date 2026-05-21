---
job_id: 46a833d3-6ead-47e0-bc82-e5a4651f2c86
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: bhPaXhWVKG.pdf
paper: MermaidFlow: Redefining Agentic Workflow Generation via Safety-Constrained Evolutionary Programming
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, touching agentic workflow optimization, graph-based/neurosymbolic representations, safety constraints, and LLM-based planning/search.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments/results, and conclusion, and it provides enough technical and empirical content to warrant full review, even though several claims are overstated and some methodological details remain insufficiently justified.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes MermaidFlow, a framework for agentic workflow generation that represents workflows as Mermaid graphs and optimizes them using constrained evolutionary programming. The core idea is to move from directly generating Python/code-like workflows to a typed, declarative intermediate representation that can be statically checked, then evolved via operators such as substitution, addition, rewiring, deletion, subgraph mutation, and crossover. Experiments on GSM8K, MATH, HumanEval, and MBPP show consistent improvements over several non-agentic, hand-crafted multi-agent, and automated workflow baselines.

## Strengths
The paper addresses a real and increasingly important pain point in agentic systems, namely that workflow search in raw code space is brittle, hard to verify, and often produces unusable candidates. Recasting workflow generation into a structured intermediate representation is a sensible design choice, and the separation between planning representation and executable realization is one of the more convincing parts of the paper.

I found the high-level framework intuitive and reasonably compelling. In particular, **Figure 2** does a good job of communicating the advocated shift from imperative code generation to a declarative graph substrate. The left half makes the representation argument concrete, and the right half gives a clear picture of the population-based search loop. Even though the formal guarantees are narrower than the paper sometimes suggests, the figure helps explain why graph-level edits are likely to be more stable than textual Python edits.

The empirical results are broadly positive. **Table 1** shows that MermaidFlow is consistently best across all four benchmarks, and the gains over the strongest automated baselines are not confined to a single dataset. The improvement on MATH is especially notable relative to AFlow and MaAS, and the cross-domain coverage, math plus code, is better than many papers in this area that only show one task family.

The efficiency argument is also directionally supported. **Figure 3** suggests that MermaidFlow reaches stronger train/test solve rates than AFlow over search iterations, and the accompanying discussion claims substantial token savings to reach comparable MATH performance. Even though the evidence could be more rigorous, this is an important dimension because workflow search methods can otherwise become too expensive to matter in practice.

The case study is useful. **Figure 4** makes the crossover operator less abstract by showing how structural pieces from two parent workflows are recombined into a child workflow. This helps the reader understand what “graph evolution” means operationally, rather than leaving it at the level of generic EP terminology.

The paper also does a decent job in providing concrete artifacts: examples of Mermaid workflows, pseudo-code for the optimization loop, and dataset-level benchmark results. For an area where many papers remain vague about the actual workflow objects being optimized, this level of concreteness is appreciated.

## Weaknesses
1. **The central “safety” and “correctness” claims are overstated relative to what is actually verified.**  
   The paper repeatedly uses strong language such as “valid and executable by construction” and “guarantee static graph-level correctness across the entire generation process” in the abstract, Section 1, Section 3.2, and Section 4.1. However, the validator described in the paper checks mostly structural properties: existence of required interface nodes, connectivity, allowed node types, and ensemble in-degree constraints. This is explicit in Appendix A.2 with checks W1-W5. That is useful, but it is much weaker than semantic correctness, executable correctness of the translated Python, or task-level safety. In fact, the paper itself later acknowledges that Mermaid-to-Python translation still relies on an LLM and can suffer from code-generation issues, with examples in Appendix C and future work in Appendix E. So there is a mismatch between the headline claims and the actual guarantee. This matters because the representation is the main contribution; if the guarantee is only syntactic well-formedness plus a few schema constraints, the paper should say that plainly rather than implying stronger safety properties than it delivers.

2. **Lemma 1 and the associated formalization are too weak and partially circular, and the notation around the search space is not fully coherent.**  
   In Section 4.1, **Lemma 1** states closure of the search space under “constraint-preserving operators.” But this is almost tautological as written: the operator set $\mathbb{O}$ is defined to preserve the constraints, and then the lemma states that applying operators in $\mathbb{O}$ preserves membership in $\mathcal{S}$. There is no real proof, and the statement does not establish anything beyond the way the operators were defined. More importantly, the definition of the validator in **Equation (5)** uses $Q(G)=1$ iff $G\in\mathcal{S}$, but $\mathcal{S}$ in **Equation (2)** itself is defined via satisfaction of static constraints $G \models \mathcal{C}_{\text{static}}$, which are said to be “automatically enforced by Mermaid’s parser and extended structural schema.” The paper never cleanly separates what Mermaid itself guarantees, what the authors’ custom checker guarantees, and what the operator definitions guarantee. That distinction matters because many of the claimed benefits hinge on this exact boundary.  
   There are also notation issues. **Equation (2)** defines
   \[
   \mathcal{S}=\left\{G(\mathcal{V}_{[\tau,\alpha]},\mathcal{E}_{[\rho]},\mathcal{C})\in\mathcal{G}_{\text{Mermaid}}\mid G\models \mathcal{C}_{\text{static}}\right\},
   \]
   but **Equation (1)** defines a workflow graph only as $G(\mathcal{V}_{[\tau,\alpha]},\mathcal{E}_{[\rho]})$, not with $\mathcal{C}$ as an argument. Then **Equation (3)** appears malformed:
   \[
   \mathcal{V}_{[\tau,\alpha]}=\left\{(m,p(\tau,\alpha),f(\tau)\mid m\in M,\ p\in P,\ f\in F\right\},
   \]
   where the tuple/conditioning syntax is unbalanced and the role of $\tau,\alpha$ versus free variables $p,f$ is unclear. This is not a cosmetic issue, because the paper is trying to formalize the exact search object and agent parameterization.

3. **The experimental protocol leaves an uncomfortable ambiguity around model selection and use of the test set.**  
   In Section 5.1 the paper says datasets are partitioned into training and test sets with a 1:4 ratio, and in Appendix A.5 the specific train/test sizes are given. However, **Table 1** reports test performance, while **Figure 3** shows train and test curves over optimization iterations, and **Table 3** reports “final selected workflow indices for each benchmark,” implying that some stopping point or selected round is chosen. The paper does not explain clearly whether the final workflow round is selected using a validation set, using the training split only, or by inspecting the test curve. Because the search itself optimizes workflows over repeated rounds, the selection protocol is not a minor detail. If the round index or best workflow is effectively chosen with access to test performance, that would inflate the reported results. The paper needs to specify the exact model-selection pipeline: what data are used for scoring in the search loop, what data are used for stopping, and whether test data are touched only once for final reporting. As written, this is too blurry for comfort.

4. **The reliance on LLM-as-Judge is under-analyzed, despite being central to the optimization loop.**  
   Section 4.2 says candidate selection is done by an LLM-as-Judge, and the prompt for this judge in Appendix A.3 shows it scores workflow coherence, innovation, complexity balance, prompt quality, and modification rationale. This means the search quality depends heavily on subjective, model-specific preferences rather than direct downstream evaluation over candidates. Yet the paper provides almost no robustness analysis of this choice. There is no comparison to simpler selectors, no sensitivity analysis across judge models, no estimate of disagreement/noise, and no evidence that the judge correlates reliably with actual validation performance. The paper does include **Table 2**, but that table studies stronger optimization LLMs for generation on only two datasets, not the stability of the judging mechanism itself. This matters because if the judge is poorly calibrated, the supposed gains may be due as much to hidden preference shaping as to the Mermaid representation.

5. **Some empirical comparisons are suggestive, but the evidence for the specific claimed mechanism is thinner than the paper implies.**  
   The paper’s main causal claim is not merely “we did better,” but “we did better because structured Mermaid representation plus safe graph operators create a better search space.” To support that claim, I would expect stronger ablations isolating: (i) Mermaid representation without EP constraints, (ii) EP over Mermaid but without custom checker, (iii) simpler graph-edit heuristics versus the full operator set, and (iv) direct comparison between one-parent and two-parent evolution. Instead, the empirical section mostly compares the full system against external baselines. **Figure 3** compares MermaidFlow against AFlow, which is useful, but that is a comparison of two whole systems, not a controlled decomposition of the paper’s own design choices. Likewise, **Table 3** on later stopping points is intriguing but not very convincing by itself, because “better workflows are found later” is at best an indirect signal of search stability. If the paper wants to claim that safety-constrained graph evolution, specifically, is the reason for improved search efficiency and robustness, it needs tighter ablations.

6. **The case study is helpful for intuition, but it sometimes overstates fidelity between representation and execution.**  
   In Section 5.4, the text around **Figure 4** says the generated Python code “perfectly resemble[s] Mermaid Workflow_8.” That is too strong given the actual pipeline still relies on LLM translation rather than a deterministic compiler. The appendix examples of translated code also contain obvious inconsistencies and typos, such as malformed syntax, naming mismatches, and variable errors. This does not by itself invalidate the method, but it does undercut the paper’s stronger presentation that Mermaid offers a reliable compilation path today. The paper would be stronger if it positioned Mermaid as a useful structured intermediate representation with partial static checking, not as something already close to a verified compiler pipeline.

7. **Presentation quality is uneven, with several writing and notation problems that make careful reading harder than necessary.**  
   There are numerous grammar issues, typographical mistakes, and inconsistencies throughout the main text and appendix, for example “threefold of agentic baselines,” “represent workflows,” “it can be easily understood by human,” “After sample two different parent workflows,” and several malformed code snippets and prompt templates. Some section titles are oddly capitalized, and the paper occasionally blurs Mermaid syntax, custom schema rules, and implementation prompts. The examples in the appendix are valuable, but several are visibly noisy or inconsistent with the text. This matters because the paper’s contribution is largely representational and methodological, so precision of exposition is especially important.

8. **The scope of evaluation is still fairly narrow relative to the paper’s broad framing.**  
   The introduction and conclusion frame MermaidFlow as a modular foundation for robust, interpretable, and scalable agentic reasoning systems. But the actual experiments cover only four benchmarks in two domains, math reasoning and code generation, under a relatively controlled setup with a single closed-source execution model in the main experiments. There is no evaluation on longer-horizon tool-use tasks, external API interactions, retrieval-heavy settings, or environments where workflow validity involves richer control flow than the current node types allow. The paper itself admits in Appendix E that MermaidFlow cannot yet express if-conditions or loops. That is an important limitation because it narrows how much one can infer from the benchmark wins about general agentic workflow generation.

## Questions
1. **Please clarify the exact search/model-selection pipeline to rule out test-set contamination.**  
   For each benchmark, what data are used for: (a) scoring workflows during search, (b) choosing the final workflow round or stopping point, and (c) reporting final numbers in **Table 1**? A concise step-by-step description would substantially increase my confidence.

2. **Can the authors precisely restate what is guaranteed by the representation and checker?**  
   Right now the paper mixes claims about syntactic validity, type safety, executability, and safety. I would like a crisp statement of the form: “our checker guarantees A, B, C; it does not guarantee D, E, F.” If this is only graph-schema validity plus basic interface constraints, please say so explicitly.

3. **Can the authors provide stronger evidence that the LLM-as-Judge is reliable?**  
   For example, a rebuttal could report the agreement between judge scores and actual downstream validation scores on a held-out set of candidates, or compare against a simpler selector such as random selection, score-only parent inheritance, or direct validation-based ranking on a small subset.

4. **Can the authors disentangle Mermaid representation from evolutionary operators more cleanly?**  
   A targeted ablation would help, such as Mermaid representation with simpler local search, or EP without the custom structural checker. This would clarify whether the improvement mainly comes from the DSL, the operator design, or the judge/translation prompts.

5. **Please clarify the formal layer in Section 3.2 and Section 4.1.**  
   In particular, can the authors revise **Equations (2), (3), (4), and (5)** to remove ambiguity and explicitly define the search object, the validator, and the conditions under which closure actually holds? As written, the lemma reads more definitional than substantive.

6. **How much of the reported gain survives if code translation is made deterministic or rule-based?**  
   Since Appendix E itself identifies rule-based Mermaid-to-Python conversion as future work, I am curious whether the current performance is bottlenecked more by workflow search or by the LLM translation step.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns require escalation based on the presented work. The paper studies workflow generation for reasoning tasks and does not present human subjects, sensitive private data, or clearly harmful deployment claims in the main paper.

## Soundness Rating
3: good. The core empirical claim, that a structured Mermaid-based workflow search can outperform several baselines on the chosen benchmarks, is reasonably supported. However, the formal guarantees are weaker than advertised, and the experimental methodology leaves important unanswered questions, especially around workflow selection and the judge-based optimization loop.

## Presentation Rating
2: fair. The main idea is understandable and several figures, especially **Figure 2** and **Figure 4**, help a lot, but the paper has many writing, notation, and precision issues that make the technical contribution harder to assess cleanly than it should be.

## Contribution Rating
3: good. The use of a declarative graph IR for agentic workflow search is a meaningful contribution, and the benchmark improvements are relevant to the ICLR community. That said, the contribution is moderated by overclaimed guarantees, limited mechanistic ablations, and a somewhat narrow evaluation scope relative to the framing.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a solid core idea and useful empirical evidence, and I do think the representational shift from direct code search to constrained graph search is worth sharing. Still, the paper oversells its safety guarantees, underspecifies some math and protocol details, and does not yet isolate the true source of the gains as cleanly as I would like.

## Reviewer Confidence
4: confident. I am confident in the main assessment and checked the paper carefully, including equations, figures, tables, and appendix examples, though some implementation-level ambiguities remain because the paper does not fully spell them out.