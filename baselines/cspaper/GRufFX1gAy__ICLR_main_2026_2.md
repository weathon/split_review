---
job_id: 6778bf10-cc24-4c77-b78f-be116b011298
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GRufFX1gAy.pdf
paper: InnoGym: Benchmarking the Innovation Potential of AI Agents
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The submission is clearly within ICLR scope as a machine learning benchmark and infrastructure paper for evaluating AI agents, with direct relevance to datasets/benchmarks, agent evaluation, and ML systems.

## Minimum Quality
Pass ✅. The paper includes the expected scientific structure for a benchmark paper, namely abstract, introduction, methodological framework, experiments with quantitative results, related work, and conclusion; despite notable methodological and empirical weaknesses, it clears the minimum bar for non-desk-reject review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions or manipulative text targeting automated reviewers; the prompt text in Appendix H/I appears to be part of the benchmark methodology rather than an attempt to influence peer review.

# Expected Review Outcome:
## Summary
This paper introduces InnoGym, a benchmark and evaluation framework intended to measure the innovation potential of AI agents rather than only their final-task correctness. The core proposal formalizes tasks as quadruples \((P,S,V,D)\), defines two evaluation axes, performance gain \(G\) over known solutions and novelty \(N\) relative to known solutions, and instantiates the benchmark with 18 curated engineering/scientific tasks plus a unified execution environment, iGym. The paper also reports experiments with three existing agent scaffolds on a 10-task subset, concluding that current agents sometimes produce methodologically different solutions but still fail to translate novelty into strong performance.

## Strengths
The paper tackles a meaningful and underexplored evaluation question. Many existing agent benchmarks indeed collapse everything into correctness or leaderboard score, and this submission makes a serious attempt to separate “better” from “different.” That framing is useful, even if the present instantiation is imperfect.

The benchmark construction effort appears substantial. The task curation pipeline in **Figure 2** is one of the stronger parts of the paper because it makes the benchmark-building process concrete rather than hand-wavy. In particular, the progression from 197 source tasks to 18 retained tasks, together with evaluator validation, solution collection, and visible/hidden partitioning, gives the work more credibility than papers that simply aggregate a handful of existing datasets with minimal normalization. I also appreciated that **Table 3** reports the number of reference solutions per task and a diversity statistic, which at least signals awareness that novelty depends strongly on coverage of \(S_{\mathrm{known}}\).

The paper’s formalization is simple and easy to understand at a high level. The decomposition \(V(s)=C(s)\cdot R(s)\) in **Section 2.1** is intuitive for benchmark design, and **Equations (2) and (3)** make the intended evaluation axes explicit. Even though I have concerns about the details, the authors deserve credit for articulating the measurement problem clearly enough that one can disagree with it precisely.

The unified execution environment is potentially useful for the community. **Figure 4** presents iGym as more than a thin wrapper, with support for tool dispatch, recovery, concurrency, and common abstractions across agent systems. Benchmark papers often underestimate how much engineering inconsistency pollutes comparisons; centralizing execution infrastructure is a practical strength.

The experiments, while limited, are directionally informative. **Table 2** supports the core empirical narrative that current agents are far from human SOTA on these tasks, and that novelty scores do not automatically align with performance. Even negative results can be valuable when the benchmark is genuinely difficult, and the broad pattern in Table 2 is at least consistent with the paper’s claim that robustness is the bottleneck.

## Weaknesses
1. **The central novelty metric is not yet convincing enough to support the paper’s strongest claims.**  
   This is the main issue. In the main paper, **Section 2.1** defines \(D\) as a task-appropriate dissimilarity function, but in practice the entire benchmark hinges on a very specific LLM-as-judge pipeline that extracts a structured summary with one model and then scores dissimilarity with another model. In **Section 4.1**, novelty is computed by prompting Codex for extraction and GPT-5 for six rubric scores, then taking the minimum over known solutions. This is a very fragile measurement stack for such a central quantity. The problem is not merely that the judge is learned or approximate; it is that the benchmark’s headline contribution is “benchmarking innovation,” while the operationalization of innovation relies on a subjective, prompt-dependent, model-dependent comparator with limited validation in the main paper.  
   Why this matters: if \(N(s)\) is unstable, biased, or insensitive to implementation-level distinctions that matter for actual innovation, then the benchmark may be measuring “how different a judge model thinks two writeups look” more than methodological novelty. Since the paper’s main scientific claim is the importance of evaluating novelty alongside performance, this is not a side detail, it is the load-bearing beam.

2. **The mathematical definition of novelty is too underspecified relative to how strongly it is used.**  
   In **Equation (3)**, novelty is defined as
   \[
   N(s)=C(s)\cdot \min_{h\in S_{\mathrm{known}}}D(s,h),
   \]
   which means novelty is entirely determined by the single closest known solution. This choice is intuitive but also quite brittle. If \(S_{\mathrm{known}}\) is sparse, unrepresentative, or uneven across tasks, then a solution can appear highly novel merely because the reference set is incomplete. The paper acknowledges this limitation in Appendix B, but the main text still treats \(N\) as if it were a stable cross-task quantity. There is also no discussion in the main paper of whether \(D\) is symmetric, calibrated across domains, or comparable across tasks with very different solution modalities.  
   The use of the minimum operator is especially consequential. If two tasks differ greatly in the density of collected reference solutions, then the same candidate methodology can receive very different novelty scores for reasons unrelated to actual innovation. **Table 3** partly exposes this issue by showing some tasks have only 2 or 3 reference solutions, and several ROADEF tasks have only 1. That is an alarm bell, not a minor caveat. A benchmark that compares novelty across tasks needs a much deeper treatment of reference-set coverage.

3. **The main experiments cover only a subset of the benchmark, which weakens the empirical case.**  
   The benchmark claims 18 tasks, but **Section 4.1** states that only 10 are used in the main evaluation subset due to computing and engineering constraints. That is understandable operationally, but scientifically it reduces confidence in the benchmark’s representativeness. The omitted tasks are not random; they are likely among the hardest or most cumbersome, which means the reported conclusions may reflect a filtered view of benchmark difficulty and agent behavior.  
   Why this matters: benchmark papers live or die by breadth and coverage. If nearly half the benchmark is absent from the core experiments, then the paper is partly asking readers to trust the benchmark design without demonstrating how it behaves at full scope.

4. **The empirical evaluation of agents is too narrow to support broad conclusions about “AI agents” writ large.**  
   The paper evaluates only three scaffolds, MLAB, CODEACT, and AIDE, with one main backbone in the core experiments and a small model ablation later. This is a rather limited slice of the rapidly moving agent landscape. The claims in **Section 4.2** are phrased broadly, for example about “current agents” being limited by robustness, but the experimental evidence is from three systems under one standardized environment with only three runs per configuration.  
   **Table 2** is informative, but the sample is small and heavily censored by failures, denoted as “/”. This makes the conclusions directionally plausible rather than strongly established. A benchmark paper is more convincing when it stress-tests a wider variety of agent designs, including at least one stronger innovation-oriented search system if the paper is explicitly about innovation potential.

5. **The result reporting in Table 2 is awkward and can be misleading.**  
   **Table 2** reports “Gain,” “Ratio,” and “Novelty,” with many missing entries and no dispersion. The paper says it reports the best score over three runs, restricted to runs yielding a valid submission. This choice introduces an optimistic selection effect for successful runs while also silently dropping failed runs from the mean in the main table. The appendix later adds pessimistic imputation in **Tables 4–6**, which is more honest, but this should not be buried outside the main paper.  
   Why this matters: benchmark comparisons are highly sensitive to aggregation choices. Reporting best-of-three valid runs inflates performance relative to average-case robustness, exactly the property the paper claims is central. In other words, the paper’s aggregation protocol partially undercuts its own stated thesis about robustness.

6. **The claims around Figure 5 and Figure 6 overreach relative to the evidence shown.**  
   The analysis section is visually appealing, but it often feels more like post hoc storytelling than rigorous evaluation. In **Figure 5(a)**, the “solution space tree” for CirclePacking is based on a single development trajectory, and in **Figure 5(b)** the complex-plane representation uses performance magnitude and novelty angle. This is interesting as a visualization device, but the paper presents it as showing a “richer, multidimensional representation of the innovation process.” I am not convinced this goes beyond a descriptive re-encoding of two scalars.  
   Similarly, **Figure 6(a-c)** provides limited-sample trends on execution time, base model, and sampling temperature, apparently with only 3 runs each. The text then makes fairly strong claims about diminishing returns, stable monotonic improvement, and a “sweet spot” around temperature \(0.5\) to \(0.75\). With such small \(n\), these are better framed as anecdotal observations than as reliable benchmark insights. The figures are useful for intuition, but the prose oversells them.

7. **The benchmark’s novelty pipeline may conflate methodology with presentation artifacts.**  
   The comparison prompt in **Appendix H.2** includes dimensions such as “Model Architecture & Implementation,” “Experiment Design & Validation Methods,” and “Data Processing & Feature Engineering.” Some of these are reasonable, but others risk rewarding differences in tooling, formatting, or implementation environment rather than actual conceptual innovation. The main text in **Section 4.1** says novelty captures “methodological dissimilarity,” but the rubric explicitly includes implementation choices. That is not a harmless detail, because for competition tasks, two solutions may be methodologically identical yet differ in software stack or packaging.  
   Why this matters: if novelty includes implementation heterogeneity, then the benchmark may systematically overestimate innovation for superficial engineering changes.

8. **There is a serious benchmarking confound around prior exposure and possible contamination, but the paper barely discusses it.**  
   Many tasks come from public competitions from 2018 to 2024, and some associated solutions, writeups, and repositories are public. The paper does partition visible and hidden task artifacts, but that does not address whether the foundation models used by the agents have seen these competitions, solutions, or related discussions during pretraining. Since the benchmark’s notion of innovation is partly “departure from known human methods,” pretraining exposure to those methods is a direct threat to validity.  
   This is especially important because novelty is measured against a finite curated set \(S_{\mathrm{known}}\), not the model’s latent knowledge. If the agent reproduces a known but uncollected method, it could receive artificial novelty credit. The paper should confront this issue directly in the main text.

9. **The formalization of performance gain and ratio has avoidable inconsistencies and unclear notation.**  
   In **Equation (2)**, \(G(s)=V(s)-V_{\mathrm{known}}^*\) is clean enough. But in **Section 4.1**, the paper then defines a normalized ratio as \(\mathrm{Ratio}(s)=G(s)/V^{*}(s)\). This notation is suspicious because \(V^*\) was previously defined in **Equation (1)** as the optimal feasible value for the task, not a function of \(s\). Writing \(V^{*}(s)\) suggests dependence on the candidate solution, which is mathematically inconsistent with the earlier definition. I assume the intended denominator is the task optimum or best-known score, but the paper should not be sloppy here because the ratio is used throughout **Table 2** and the appendix.  
   Also, if the true optimum \(V^*\) is generally unknown for improvable tasks, as the paper itself says in **Section 2.1**, then normalizing by \(V^*\) is conceptually odd. Perhaps the implementation actually uses the best-known score; if so, the notation should be corrected explicitly.

10. **The benchmark’s “innovation” concept is narrower than the framing suggests.**  
    The paper repeatedly motivates innovation in broad terms, but the operational definition boils down to performance improvement and judge-scored methodological difference relative to known solutions. The benchmark excludes efficiency, interpretability, reproducibility quality, resource use, and downstream scientific value from the main metric, although these are often central to what practitioners mean by innovation in real engineering and science. Appendix B admits some of this, but the main paper still adopts grand framing.  
    This matters because the title and narrative promise “benchmarking the innovation potential of AI agents,” while the actual object being measured is closer to “benchmarking performance improvements plus judged methodological dissimilarity on a curated set of optimization/competition tasks.”

11. **Presentation quality is uneven, and there are several exposition issues in the main paper.**  
    There are a number of minor but cumulative issues: repeated text in **Section 2**, awkward phrasing, inconsistent capitalization of iGym/igym, and some confusing figure references. In **Section 2.3**, the text says “As shown in Fig. 1(c)” for multiple categories, even though the categories are supposed to correspond to **Fig. 1(c-e)**. On **Page 9**, the captioning/layout around **Figure 6** is messy enough that it momentarily interrupts understanding. **Table 1** also has formatting artifacts such as “Easy Hard” and awkward source/domain strings. None of these is fatal, but for a benchmark paper, clarity really matters because readers need to trust the protocol details.

12. **The validation of \(D_{\mathrm{AGENT}}\) is too small-scale to justify heavy reliance on it.**  
    Even granting the appendix at face value, the validation remains limited: 50 EquiBench triplets with only 8 human-annotated, and 3 human-collected method triplets across subfields. That is not enough to establish reliability across the much more heterogeneous benchmark tasks in the main paper. The paper needs stronger evidence for inter-judge consistency, prompt sensitivity, model sensitivity, and task-level calibration.  
    Put simply, the benchmark is only as solid as its novelty metric, and the validation provided for that metric is still thin.

## Questions
1. The most important issue for me is the reliability of the novelty metric. Can the authors provide, in the rebuttal, a stronger analysis of judge stability, for example agreement across multiple judge models, prompt variants, or repeated evaluations? I would be especially interested in task-level rank correlations of novelty scores under different judges, not only a few triplet sanity checks.

2. Please clarify the exact definition of the normalized ratio in **Section 4.1**. Is the denominator \(V^*\), \(V_{\mathrm{known}}^*\), or something else? As written, \(\mathrm{Ratio}(s)=G(s)/V^*(s)\) conflicts with the notation in **Equation (1)**. This should be corrected precisely.

3. Why is best-of-three-valid-runs the primary aggregation in **Table 2** rather than average performance over all runs with explicit failure accounting? Since the paper’s own message emphasizes robustness, average-case or pessimistically imputed results seem more aligned with the stated goals.

4. Can the authors explain how sensitive novelty is to the size and coverage of \(S_{\mathrm{known}}\)? For example, if one removes some known reference solutions, how much do the novelty rankings of candidate submissions change? This ablation would directly address a core benchmark validity concern.

5. The paper uses only 10 of 18 tasks in the main evaluation. Are the remaining 8 omitted solely because of computational constraints, or are there qualitative reasons they behave differently? A brief characterization of the held-out tasks would help readers understand how representative the reported subset is.

6. Can the authors clarify whether the novelty rubric intentionally includes implementation environment/tooling differences, or whether the intended target is only conceptual/methodological distinction? If the former, I worry the metric is broader than advertised; if the latter, the rubric should be tightened.

7. Regarding **Figure 6(c)**, how robust is the claimed temperature “sweet spot”? With only three runs, this seems noisy. Please provide either error bars or a more cautious interpretation.

8. Since many tasks are drawn from public competitions and published solutions, how do the authors assess contamination risk from model pretraining? Even a discussion of plausible failure modes and mitigations would improve confidence.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The benchmark aggregates tasks, datasets, leaderboard solutions, and code artifacts from multiple public competitions and repositories across different organizers and years, as described in **Section 3.1**, **Section 3.2**, and **Appendix G.1**. While this does not automatically imply an ethics violation, the paper does not clearly discuss licensing or reuse permissions for all collected solution artifacts, extracted summaries, or benchmark packaging. Since benchmark release and redistribution can interact with dataset licenses, competition terms, and code repository licenses, I would like the authors to explicitly document compliance and redistribution policy.

## Soundness Rating
2: fair. The paper has a sensible benchmark motivation and a nontrivial construction effort, but the central novelty metric remains insufficiently validated, and the empirical methodology is narrower and less rigorous than the paper’s claims suggest.

## Presentation Rating
2: fair. The paper is readable at a high level, but there are important notation, formatting, and exposition issues that reduce clarity, especially around metric definitions, figure interpretation, and result aggregation.

## Contribution Rating
2: fair. The problem being addressed is important and the benchmark-building effort is real, but the current evaluation methodology, especially the novelty measurement, is not yet strong enough for me to view the overall contribution as solidly above the bar.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The benchmark idea is timely and potentially useful, and the curation work is substantial, but the paper leans too heavily on a thinly validated LLM-judge novelty metric and a limited experimental evaluation to support broad claims about innovation in AI agents.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially about benchmark methodology, evaluation design, and the operationalization of novelty, though I have not independently reproduced the benchmark or appendix validations.