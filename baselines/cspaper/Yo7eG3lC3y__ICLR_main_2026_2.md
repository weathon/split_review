---
job_id: 5e728826-eeac-48a1-869b-c0cb6ce32b7a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Yo7eG3lC3y.pdf
paper: LEGO-EVAL: Towards Fine-Grained Evaluation on Synthesizing 3D Embodied Environments with Tool Augmentation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies evaluation and benchmarking for text-guided 3D scene synthesis in embodied AI, using tool-augmented multimodal models and releasing a benchmark.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, method, experiments, quantitative results, analysis, and conclusion; despite several weaknesses, it clears the minimum bar for scientific completeness and readability.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden or reviewer-targeted manipulation attempts; the many prompt blocks appear to be part of the method description rather than attempts to influence the review process.

# Expected Review Outcome:
## Summary
This paper proposes LEGO-EVAL, a tool-augmented evaluation framework for checking whether generated 3D indoor scenes satisfy fine-grained natural-language instructions. It also introduces LEGO-BENCH, a benchmark of 130 instructions with manually aligned scenes and annotated constraints, and reports that LEGO-EVAL agrees with human judgments substantially better than CLIPScore, SceneEval, and VLM-as-a-judge baselines, while current scene generation systems perform poorly on the benchmark.

## Strengths
The paper tackles an important and fairly underexplored bottleneck. A lot of recent work focuses on generating 3D scenes, but evaluation is often reduced to CLIP-style similarity or generic VLM judging, which is not enough for detailed spatial and attribute constraints. Framing evaluation as explicit constraint satisfaction is sensible and useful for embodied AI settings.

The overall system design is intuitive. **Figure 2** gives a clear high-level view of the pipeline, from constraint identification to tool planning, argument selection, execution, and final validation. That decomposition makes the proposed evaluator more interpretable than a monolithic VLM judge, and the explanation traces are a practical advantage if the framework is used as a debugging or refinement signal.

The tool inventory is broad enough to cover multiple evidence types. The combination of environment interaction tools, textual metadata tools, and multimodal reasoning tools is a reasonable way to address multi-hop grounding in 3D scenes, especially for constraints involving both object identity and spatial relations.

The empirical gain over the reported baselines is large. In **Table 1**, the main result is not a tiny bump but a substantial jump: the reported holistic F1 rises from roughly 0.40 for the strongest VLM-as-a-judge baseline to 0.81 for LEGO-EVAL with GPT-4.1, and Cohen’s \(\kappa\) rises from 0.05 to 0.63. Even allowing for baseline caveats, that is a meaningful improvement on the presented benchmark.

The benchmark itself has value. **Figure 4** suggests that LEGO-BENCH is not just a bag of object-count prompts; it includes constraints spanning floor layout, material selection, object selection, and object placement, with a nontrivial fraction involving architectural elements. That broader coverage is a nice step beyond evaluations that only check objects and pairwise relations.

The generation benchmark is also informative. **Table 3** shows a striking gap between partial success and holistic success, with holistic SR topping out at only \(10.0\%\). This is a useful result for the community because it highlights that seemingly decent per-constraint performance does not translate into complete instruction following.

The analysis section is directionally useful. **Table 5** connects tool-planning quality, graph similarity, and argument selection to end evaluation performance, which is more informative than only reporting end-to-end numbers.

## Weaknesses
1. **The claimed evaluation framework is much less general than the paper’s framing suggests, because it depends heavily on simulator-specific privileged access and handcrafted tools.**  
   The title, abstract, and introduction present LEGO-EVAL as a framework for evaluating synthesized 3D embodied environments broadly, but the actual implementation in **Section 3.2** and **Appendix C.3** relies on direct access to structured scene representations and simulator rendering utilities: `get room info`, `get wall info`, `get object info`, `get window info`, `get spatial relation`, etc. This is not a minor implementation detail. It means the system is evaluating scenes with access to metadata such as exact IDs, positions, rotations, room membership, and geometry, rather than purely from the rendered outputs that most generic evaluators would have.  
   Why this matters: this makes LEGO-EVAL closer to a simulator-instrumented checker for AI2-THOR-style environments than a generally applicable evaluation metric for text-to-3D scene synthesis. If another generator outputs meshes, NeRFs, Gaussian splats, or a different simulator format without the same APIs, the evaluator is not immediately applicable. The paper should narrow its claims or more clearly state that the method assumes privileged programmatic scene access.

2. **The experimental comparison may overstate the advantage because the baselines are relatively weak and not matched to the tool-access setting.**  
   In **Table 1**, CLIPScore is evaluated with thresholds 15/20/25, and VLM-as-a-judge gets four scene images plus self-consistency over three samples. That is a reasonable starting point, but it is not obviously a strong upper bound. There is no stronger agentic VLM baseline with decomposition, retrieval, or external memory, even though the core claim is that tool-based multi-hop grounding is better than VLM judging. Likewise, SceneEval is handicapped by construction because, as the authors note, it cannot evaluate \(41\%\) of the constraints.  
   Why this matters: the reported \(+0.41\) holistic F1 gain over VLM-as-a-judge is impressive, but the comparison is not apples-to-apples with respect to available evidence and reasoning structure. A stronger comparison would include a generic tool-using multimodal agent without bespoke tools or a stronger multi-view judge with explicit decomposition. As is, the result supports “this particular tool pipeline beats these baselines on this benchmark,” but not yet the broader paradigm claim.

3. **The benchmark is small, and the paper does not adequately quantify annotation reliability.**  
   **Section 3.3** states that LEGO-BENCH contains 130 instructions and 1,250 constraints; **Section 4.1.1** adds 130 intentionally misaligned scenes, yielding 260 instruction-scene pairs. For a benchmark intended to support broad claims about evaluation reliability for fine-grained 3D scene synthesis, this is not a large dataset. More importantly, the paper does not report inter-annotator agreement for constraint identification, constraint typing, or the human judgments used as ground truth in **Table 1**. The appendix describes mutual review and two iterations, but not quantitative agreement.  
   Why this matters: when the main headline is agreement with human judgments, the reliability of those judgments is central. Without annotator agreement, it is hard to know whether the evaluation problem is itself well-posed at the claimed granularity.

4. **The paper’s formalization is too thin for a method paper built around multi-stage planning and validation.**  
   The only explicit mathematical formalization in the main method is **Equation (1)**,
   \[
   J, E \leftarrow \mathrm{Eval}(I \mid S),
   \]
   which is essentially just notation for input-output behavior. It does not formalize the decomposition over constraints, the graph-structured tool plan, or how per-constraint judgments are aggregated into the final decision. Since **Section 3.1** says the scene is valid only if it fulfills all constraints \(C=(c_1,\dots,c_k)\), the paper should define something like
   \[
   J = \bigwedge_{i=1}^{k} J_i,
   \]
   with a precise definition of each \(J_i\), including what happens for missing entities, ambiguous grounding, or constraints that are conditionally phrased after rewriting.  
   Why this matters: these details affect both correctness and reproducibility. For example, the benchmark construction explicitly rewrites dependent constraints into contextualized forms in the appendix. But the main paper never clarifies how “partial” metrics are computed when constraints are merged, conditioned, or rephrased. A framework paper does not need a theorem, but it does need a precise operational definition.

5. **Some evidence in the paper directly undermines the authors’ own qualitative claims.**  
   The most glaring example is **Figure 8** on **Page 9**. The figure labels LEGO-EVAL’s judgment as **“Valid”**, but the accompanying explanation says: “Since neither object is present, there is no way to assess whether the flashlight and the laptop are facing the same way. This means the constraint cannot be satisfied.” That explanation corresponds to an invalid judgment, not a valid one. This is not a tiny typo in a caption, it is a contradiction in the showcased case study.  
   Why this matters: the figure is supposed to build trust in the framework’s reasoning. Instead, it creates confusion about whether the system is judging constraint validity, reasoning validity, or explanation quality. The text below the figure even says all methods achieve accurate judgments, which makes the inconsistency more problematic, not less.

6. **The ablation study is weaker than the prose claims, and one of its own numbers cuts against the “all tools are indispensable” narrative.**  
   In **Section 4.1.3** and **Table 2**, the authors conclude that all three tool types are indispensable. But the reported drop for removing multimodal reasoning is tiny at the holistic level, only \(-0.04\%\), and \(-1.02\%\) partial F1. That is not what “indispensable” usually looks like. **Figure 5** shows all tool types are used, but tool usage is not the same as tool necessity.  
   Why this matters: the paper currently over-interprets its own ablation. The data support that environment interaction and textual reasoning matter substantially, especially the very large degradation without environment interaction, but they do not convincingly show that multimodal reasoning is essential in the same sense. A more honest reading would separate “frequently used” from “critical for performance.”

7. **The generation benchmark in Table 3 is partially confounded by hybridization with Holodeck, which blurs what is actually being compared.**  
   In **Section 4.2.1**, the authors state that LayoutGPT, LayoutVLM, and I-Design are augmented with Holodeck to produce full scenes for fair comparison. This means the systems in **Table 3** are not simply the original methods, but method-plus-Holodeck hybrids with a shared scene completion component.  
   Why this matters: the conclusion that “existing methods achieve success rates of at most 10%” is directionally interesting, but it is not a clean head-to-head comparison among original generators. Once multiple methods share a downstream completion engine, attribution becomes murky. This should be stated more carefully.

8. **The presentation is serviceable but noticeably rough, with multiple inconsistencies and errors that obstruct careful reading.**  
   Examples include inconsistent model naming, such as “GPT-o4-mini” in **Table 1** versus “GPT-4o mini” in the text; fragmented prose around **Table 2** on **Page 7** where the paragraph is visibly cut (“such as the color of small ob...jects”); duplicated and misnumbered figures in the appendix; and a clearly corrupted prompt block on **Page 47** with garbled tokens. These issues do not make the paper unreadable, but they do weaken confidence in the polish and in some of the qualitative examples.  
   Why this matters: for a systems-and-benchmark paper, clarity of protocol and exact reporting are a big part of the contribution.

9. **The paper does not sufficiently separate evaluation reliability from benchmark-specific engineering.**  
   **Table 4** shows that automatically identified constraints lead to results close to annotated constraints, which is useful, but it is still within the same benchmark, same taxonomy, and same overall data construction process. The benchmark’s four-way taxonomy in **Section 3.1** mirrors the same decomposition used by the evaluator, and the paper even notes this is “similar to the modules in Holodeck.”  
   Why this matters: a reviewer wants to know whether LEGO-EVAL discovered a generally effective way to evaluate fine-grained scene alignment, or whether it works especially well because the benchmark and evaluator were designed in tandem. The current experiments do not really disentangle those possibilities.

10. **The main claim about supporting “a broad range of relationships expressed in natural language” is only partially substantiated.**  
   The related-work comparison on **Page 3** emphasizes that LEGO-EVAL can handle more diverse spatial expressions than predefined relation taxonomies, including examples like “The table is closer to the chair than bed.” That is a strong claim. However, the experiments mainly report aggregate metrics and broad constraint categories, not breakdowns by challenging relation subtype, compositional depth, or comparative relations.  
   Why this matters: if the paper wants to claim robust handling of open-ended spatial language, it should show where performance holds up and where it breaks. Right now, the evidence is too coarse.

## Questions
1. **Can the authors clarify the exact operating assumptions of LEGO-EVAL?**  
   In particular, is the intended setting “evaluation with privileged simulator access,” or do the authors view it as a general metric for text-guided 3D scene synthesis? A concise statement of the required inputs, such as structured scene graph, object IDs, controller access, renderable assets, would help a lot.

2. **Please provide annotation-quality statistics for LEGO-BENCH and for the human judgments used in Table 1.**  
   Inter-annotator agreement for constraint extraction, type classification, and scene-instruction alignment judgments would materially increase my confidence in the benchmark and in the reported evaluator agreement.

3. **Can the authors add or at least discuss stronger judge baselines?**  
   I would especially like to see either a decomposition-based VLM judge, a generic multimodal agent with access to the same images but without handcrafted environment tools, or a stronger multi-view judge that explicitly reasons over sub-constraints. Even a carefully argued ablation of why these are infeasible would help.

4. **Please clarify the aggregation rule mathematically.**  
   If each instruction yields constraints \(c_1,\dots,c_k\), what exactly is the final judgment function? Is it simply \(J=\bigwedge_i J_i\)? How are missing entities, ambiguity, and conditionally rewritten constraints handled in partial scoring?

5. **What explains the contradiction in Figure 8?**  
   The LEGO-EVAL panel is marked “Valid,” but the text says the constraint cannot be satisfied because the relevant objects are absent. This needs correction, and if it is a labeling mistake, please confirm that it does not reflect a deeper issue in the evaluator logic.

6. **Can the authors better justify the “all three tools are indispensable” statement in light of Table 2?**  
   The multimodal-removal result seems very small. Is that number correct? If so, I would recommend toning down the claim or providing a more targeted analysis of where multimodal tools matter.

7. **How sensitive are the results to the underlying model backbone and prompting?**  
   Table 1 already shows notable variation across GPT-4.1, GPT-4.1-mini, and Qwen2.5VL-32B. A clearer discussion of variance across prompts or repeated runs would help separate the framework contribution from base-model effects.

8. **For the scene-generation benchmark in Table 3, can the authors clarify what exactly is attributed to each method after augmenting with Holodeck?**  
   A decomposition of errors into object-selection versus placement versus scene-completion failures would make the comparison much more interpretable.

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper involves manual data collection and annotation, and the appendix also describes a survey where people were asked to describe room images. However, I could not find details about annotator compensation, consent procedures, participant recruitment, or whether any ethics/IRB-style review was considered. Since the benchmark may be released and used by others, these human-data collection details should be documented more clearly.

## Soundness Rating
2: fair. The core empirical findings are plausible and reasonably supported on the presented benchmark, but the evidence is not yet strong enough to justify the broader claims of general evaluation superiority, and several methodological details remain underspecified.

## Presentation Rating
2: fair. The main idea is understandable and some figures, especially Figure 2, help, but the paper has enough inconsistencies, rough writing, and reporting issues to materially affect clarity.

## Contribution Rating
2: fair. The benchmark and tool-based evaluation framing are useful, but the current evidence leaves open important questions about generality, benchmark coupling, and the strength of the comparative baselines.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper addresses a real problem and has some genuinely interesting ingredients, especially the explicit grounding-based evaluation framing and the benchmark. However, the current version over-claims generality relative to what is actually demonstrated, relies on a small benchmark without enough annotation-reliability reporting, and compares against baselines that do not fully stress-test the central claim. I see promise here, but I do not think the present evidence quite clears the ICLR bar.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. I am familiar with the evaluation/benchmarking side of multimodal and 3D embodied AI, and I carefully checked the core methodology and experimental claims, though some implementation details remain underspecified in the main paper.