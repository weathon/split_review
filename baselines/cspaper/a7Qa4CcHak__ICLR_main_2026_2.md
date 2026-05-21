---
job_id: 8e980528-77bb-4cd1-8951-b50d21811b01
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: a7Qa4CcHak.pdf
paper: Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. This submission is clearly in scope for ICLR as a datasets-and-benchmarks paper on evaluating ML agents in realistic terminal environments, with direct relevance to agentic LLMs, tool use, autonomy, and benchmark design.

## Minimum Quality
Pass ✅. The paper has the expected structure for a benchmark paper, including abstract, introduction, benchmark/task formulation, dataset construction, verification methodology, experiments, results, limitations, related work, and conclusion. While I have substantive concerns about parts of the evaluation methodology and reporting, these are not fatal flaws warranting desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any evidence in the provided paper text of hidden prompts, manipulative instructions to reviewers, or other prompt-injection style content.

# Expected Review Outcome:
## Summary
This paper introduces Terminal-Bench 2.0, a benchmark of 89 containerized command-line tasks intended to evaluate long-horizon AI agents on realistic terminal workflows. Each task includes instructions, an environment, oracle solution, and tests, and the paper reports results for a large set of frontier models and agent scaffolds, along with task verification procedures and trajectory-level error analyses.

## Strengths
The paper tackles an important and timely evaluation problem. There is a clear need for benchmarks that go beyond toy tool-use or narrow software-fix tasks, and the proposed setting, real terminal environments with outcome-based verification, is practically relevant.

The benchmark construction effort is substantial. The task pipeline described in Section 2.3 is more rigorous than what many benchmark papers offer: oracle solvability checks, contributor checklists, LLM-backed auditing, adversarial exploit attempts, and multiple human reviews. **Figure 3** is particularly helpful here, because it makes the review and post-merge audit pipeline concrete rather than merely asserted. That figure supports the authors’ claim that task curation was not a lightweight crowdsourcing exercise, but a multi-stage verification process with explicit anti-cheating checks.

I also appreciate the benchmark design choice in Section 2.1 to evaluate final container state rather than exact trajectories. That choice is defensible for an outcome-driven benchmark and avoids overfitting to one “correct” sequence of commands. **Figure 2** does a good job of visually explaining this task structure, including the separation between agent execution and test execution.

The task set appears genuinely difficult for current systems. **Figure 1** makes the main empirical message immediately clear: even the top system is only around 63% resolution, and there is a meaningful spread across models. This is exactly what a useful frontier benchmark should show, namely headroom at the top and non-trivial stratification across capability levels.

The paper includes a broad empirical sweep. Running 32,155 trials across many model-agent combinations is nontrivial, and the authors do not only report a single leaderboard. The inclusion of cost-performance tradeoffs in **Figure 5** is useful for practitioners, and the per-task heatmap in **Figure 11** is one of the more informative figures in the paper. It reveals that there is both a persistent “hard core” of unsolved tasks and a rough diagonal of tasks that become solvable as model quality improves, which suggests the benchmark is not saturated and has some resolution power beyond one aggregate number.

The benchmark is diverse in subject matter. **Table 1** and **Figure 4** support that claim reasonably well. Table 1, although based on author estimates, does at least show that many tasks are intended to be substantially beyond quick scripting exercises, especially for junior engineers. Figure 4 also indicates that the benchmark is not purely a SWE-Bench clone; there is some spread across scientific computing, security, data processing, systems, and other categories.

The authors go beyond leaderboard reporting and attempt failure analysis. **Figure 7** and **Figure 8** provide a useful first pass at understanding where terminal agents fail, especially the prominence of execution failures and command-level issues like missing tools or shell mistakes. Even if I have reservations about the judge methodology, I still view this as a meaningful strength relative to many benchmark papers that stop at aggregate pass rates.

Finally, the release of an open harness and standardized task format appears valuable for the community. The adapter architecture in Appendix E also suggests the framework may be useful beyond this exact task set.

## Weaknesses
My main concerns are not about whether the benchmark effort is real, it clearly is, but about how strongly the paper’s claims are supported by the evidence presented in the main paper.

1. **The benchmark’s “realism” and “economic value” claims are argued more by assertion and anecdotes than by systematic evidence.**  
   The Introduction and Related Work repeatedly frame Terminal-Bench as measuring “the kind of high-skill work that professionals are paid to do” and emphasize realism and economic value. But in the main paper, the strongest evidence for this is a collection of example tasks and author-estimated completion times. **Table 1** reports author estimates for expert and junior completion time, not actual human completion data. That is a useful descriptive statistic, but it is not enough to validate the benchmark as a measure of real-world professional capability. This matters because the paper is not just introducing a dataset, it is making a positioning claim that this dataset is a better proxy for valuable work than prior benchmarks. Without actual human baselines, inter-rater difficulty calibration, or even limited user studies showing professionals agree these tasks reflect realistic workflows, the realism argument remains under-validated.

2. **The selection process from 229 contributed tasks to 89 final tasks is insufficiently quantified, which leaves benchmark composition bias underexplored.**  
   On Page 3, the authors state that 229 tasks were collected and 89 were selected “based on the author’s difficulty assessment and a quality assessment by three experienced human reviewers.” That is plausible, but the paper does not show enough about which tasks were excluded and why. Were some categories disproportionately rejected? Were easier tasks removed to keep the benchmark hard? Were certain contributors or domains overrepresented in the accepted subset? **Figure 4** shows final category counts, but not the before/after distribution. This matters scientifically because benchmark curation is itself an intervention: if the final set was tuned for frontier-model difficulty, the resulting leaderboard may be less a neutral measurement of terminal capability and more a filtered stress test for a particular notion of “hardness.”

3. **The comparison between models and agents is not fully apples-to-apples, yet some conclusions are phrased too strongly.**  
   **Figure 1** reports “the agent scaffold used to report each model was chosen to maximize performance,” and the text on Pages 6-7 argues that “model selection is usually more important than agent scaffold when optimizing for performance.” I do not think the main-paper evidence is sufficient for that statement. The paper gives a few examples, such as GPT-5.2 vs GPT-5-Nano under Codex CLI and Gemini 2.5 Pro under Terminus 2 vs OpenHands, but these are selective pairwise contrasts rather than a systematic factorial analysis. Because scaffold compatibility is constrained by vendor ecosystem and supported agents, the best-scaffold-per-model comparison conflates model quality, tool affordances, and ecosystem engineering. **Table 2** actually illustrates how large these scaffold effects can be for some models, yet the paper does not quantify them systematically in the main text. This matters because a benchmark paper should be especially careful not to over-interpret leaderboard rank differences when the evaluation protocol itself varies by system.

4. **Terminus 2 is presented as a “neutral” testbed, but its own design choices are consequential and under-ablated in the main paper.**  
   Section 3.1 motivates Terminus 2 as a simple Bash-only scaffold. However, Appendix G reveals that Terminus 2 includes context summarization using additional model calls once the context limit is reached. That is not an innocuous implementation detail. A summarization strategy can materially alter agent behavior, especially on long-horizon tasks. Similarly, restricting the agent to a single terminal tool may improve comparability but also creates a particular capability profile that may understate models that are better when given structured edit/search tools. The paper leans heavily on Terminus 2 for empirical difficulty (Section 4.2), trajectory error analysis (Section 4.3), and command error analysis (Section 4.4), so this is not a side issue. I would have liked at least one main-paper ablation showing how much of the observed ranking and difficulty structure is stable across scaffolds versus specific to Terminus 2.

5. **The error analyses depend heavily on LLM-as-judge pipelines, and the validation presented is helpful but still limited for the claims being made.**  
   In Section 4.3, GPT-5 high-reasoning mode is used as a primary judge for trajectory-level failure modes, with 90% agreement against 120 human-labeled traces. In Section 4.4, GPT-5 is also used for command failure identification and taxonomy assignment, with smaller human validation subsets. These are decent sanity checks, but the paper then draws interpretive conclusions from **Figure 7** and **Figure 8** about model-specific failure signatures and dominant command failure categories. I am not convinced the paper shows enough uncertainty quantification for those conclusions. There are no confidence intervals on the class proportions in Figures 7-8, no sensitivity analysis to the chosen judge model, and no evidence that the taxonomy assignments are robust across alternative judges or annotator pools. This matters because the paper positions the error analyses as guidance for future model development; if the judge pipeline itself is biased, the guidance may be misleading.

6. **There are several numerical and reporting inconsistencies that undermine confidence in the presentation.**  
   The most obvious one is **Table 2** on Page 81, whose caption says token counts are “for running all 74 tasks in Terminal-Bench 2.0,” while the main paper repeatedly states the benchmark contains 89 tasks. That is not a tiny typo, because it directly affects interpretation of aggregate token usage and cost. Similarly, Section 3 says the paper evaluates “16 frontier models,” but the model list on Page 6 includes substantially more than 16 entries. These inconsistencies do not invalidate the benchmark, but they do signal that the manuscript needs a careful pass. For a paper whose contribution is an evaluation framework, sloppy accounting is especially unfortunate.

7. **The statistical treatment of some derived benchmark properties is weaker than it should be.**  
   Section 4.2 defines “empirical difficulty” by thresholding the fraction of frontier models that solve a task: easy if resolution is at least \(66.7\%\), medium if between \(33.3\%\) and \(66.7\%\), hard otherwise. These cutoffs are arbitrary and no sensitivity analysis is provided. A task near the threshold can flip category with small perturbations. Likewise, the reported correlation in **Figure 6**, \(r = 0.436\), is used to claim a “positive correlation” between predicted and empirical difficulty, but the paper does not discuss uncertainty around the empirical difficulty labels themselves, which are estimated through noisy finite trials and scaffold/model choices. In other words, the benchmark turns repeated Bernoulli outcomes into a categorical task label with hard thresholds, then correlates that label with another subjective label. The direction is reasonable, but the quantitative interpretation is looser than the prose suggests.

8. **The benchmark’s reproducibility story is mixed, and the paper does not quantify how much that affects results.**  
   The authors are commendably candid in Section 5 that tasks may depend on internet access, package registries, APIs, hardware differences, and runtime enforcement. However, the main paper gives no measurement of run-to-run or platform-to-platform instability beyond confidence intervals on average resolution rate. Since the benchmark explicitly allows internet access, even small changes in external resources can alter both solvability and cost. This matters because a benchmark intended for long-term community use needs more than an acknowledgment of possible drift; it needs some evidence on how stable the benchmark is under realistic reruns.

9. **The absence of actual human or non-LLM operational baselines limits interpretation of the reported scores.**  
   The paper repeatedly mentions “expert” and “junior engineer” time estimates, but that is not the same as human benchmark performance. The reader still does not know whether the tasks are mostly straightforward for experts, frequently ambiguous even for humans, or bottlenecked by setup friction. A benchmark can be valuable without human baselines, but here the paper’s central framing is about professional work. That framing would be much stronger if even a small subset had measured human completion rates or time-to-solve. Without that, 63% may sound either impressive or underwhelming depending on one’s assumptions.

10. **Some results are interesting descriptively but are not connected back to concrete benchmark-design lessons strongly enough.**  
   For example, **Figure 11** is one of the most informative visualizations in the paper, showing both universally hard tasks and tasks along a rough ability frontier. But the paper does not capitalize on it. Are the universally unsolved tasks unsolved because they are too open-ended, too brittle, too compute-heavy, or because the benchmark contains a few pathological outliers? Likewise, **Figure 5** shows a broad cost-performance tradeoff, but the paper does not discuss whether cost-normalized ranking is stable or whether some systems sit off the Pareto frontier because of avoidable scaffold inefficiencies. These are missed opportunities for a benchmark paper to say something deeper than “leaderboard plus diagnostics.”

11. **The paper would benefit from sharper positioning relative to adjacent benchmark paradigms.**  
   The Related Work section is broad, but the main paper still leaves somewhat vague what exactly Terminal-Bench should replace versus complement. Is the principal novelty the realism of containerized CLI tasks, the manual verification process, the long-horizon nature, the diversity of domains, or the open harness? Different comparisons matter depending on which of those is primary. Right now the paper sometimes reads as if it is advancing all of them at once.

12. **There is no mathematical flaw in the usual theorem-proof sense, but some formal definitions are underspecified given how much they are used.**  
   Since this is a benchmark paper, I am not asking for theory for theory’s sake. Still, when the paper operationalizes benchmark quantities, the definitions should be more rigorous. For instance, in Section 4.2 the empirical difficulty label is effectively a function
   \[
   d_{\text{emp}}(t) \in \{\text{easy}, \text{medium}, \text{hard}\}
   \]
   of the mean pass rate of task \(t\) across a selected set of frontier models under Terminus 2, with thresholds at \(1/3\) and \(2/3\). But the paper does not specify whether the per-model pass rate is estimated by averaging over all trials equally, whether each model is weighted equally regardless of variance, or how missing model-task runs would be handled. Similarly, the confidence intervals in **Figure 1** and **Table 2** are reported, but the paper does not say clearly whether these are task-level bootstrap intervals, trial-level binomial intervals, or something else. Because each task is attempted multiple times and trials within a task-model-agent cell are not independent in the same sense as i.i.d. data points, the uncertainty construction matters. This is fixable, but the current manuscript is looser than it should be on its core evaluation statistics.

## Questions
1. Can the authors provide a more systematic breakdown of the 229 submitted tasks versus the final 89, ideally by category and rejection reason? That would substantially increase my confidence that the benchmark is not unintentionally skewed by curation choices.

2. For the confidence intervals shown in **Figure 1** and reported in **Table 2**, what exactly is the sampling unit? Are these computed across trials, across tasks, via bootstrap over tasks, or by another method? Please define this explicitly, since repeated trials within a task are not interchangeable with independent task samples.

3. Relatedly, can the authors correct the apparent inconsistency in **Table 2**, whose caption states token counts are for “all 74 tasks” although the benchmark is otherwise described as 89 tasks? If some subset was used for token accounting, please explain why.

4. How sensitive are the empirical-difficulty categories in Section 4.2 to the \(33.3\%\) and \(66.7\%\) thresholds? A simple sensitivity analysis, or reporting the raw continuous pass-rate values alongside categories, would make **Figure 6** more convincing.

5. Since so much of the deeper analysis uses Terminus 2, can the authors provide a main-text ablation or at least a compact summary of how stable task ordering and model ordering are across scaffolds? This would help justify Terminus 2 as a neutral analysis scaffold rather than just one particular agent design.

6. Could the authors provide at least a small measured human baseline, perhaps on a subset of tasks? Even a 10-15 task sample with expert completion rates or time-to-solve would materially strengthen the realism and difficulty claims that are currently supported mostly by author estimates in **Table 1**.

7. For **Figure 7** and **Figure 8**, can the authors report uncertainty bars or judge-sensitivity analyses? Given that these plots support prescriptive conclusions about failure modes, it would help to know how stable the distributions are across alternative judge models or annotation samples.

8. In Section 4, the text states that model selection is “usually more important” than agent scaffold. Can the authors back this with a systematic variance decomposition or paired analysis rather than anecdotal examples? Right now that conclusion feels somewhat ahead of the evidence.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The benchmark includes a non-trivial number of security-oriented tasks, including password recovery, archive cracking, secret extraction, XSS filter bypasses, repository secret recovery, and vulnerability fixing or exploitation, see the task list in Appendix I, for example **crack-7z-hash**, **break-filter-js-from-html**, **vulnerable-secret**, **password-recovery**, and **git-leak-recovery**. Publishing realistic terminal tasks of this kind is scientifically defensible, but it also lowers friction for evaluating and improving offensive agent capabilities.

A second concern is deployment risk. Section 5 explicitly allows internet access during evaluation, and the benchmark centers autonomous agents operating in command-line environments with file, process, and package-management capabilities. That is realistic, but also close to the operational setting in which unsafe autonomous behavior could have real consequences. I do not view this as a reason to reject the paper, but I do think the paper should foreground responsible-use considerations a bit more clearly.

## Soundness Rating
3: good. The core benchmark construction and headline empirical findings are credible, but several claims are somewhat over-interpreted relative to the main-paper evidence, and the statistical/reporting details around uncertainty and derived difficulty labels need tightening.

## Presentation Rating
3: good. The paper is generally readable and well organized, with informative figures such as **Figure 1**, **Figure 3**, **Figure 5**, and **Figure 11**. However, there are enough inconsistencies and underspecified evaluation details, especially around **Table 2** and some statistical definitions, that I cannot rate the presentation higher.

## Contribution Rating
3: good. The benchmark is meaningful, difficult, and likely useful to the community, especially because it covers realistic terminal workflows with containerized verification. I stop short of a higher score because the paper does not yet fully substantiate some of its stronger realism and interpretability claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a valuable benchmark paper with clear practical relevance and a substantial engineering and curation effort behind it. My hesitation comes from benchmark-science issues rather than lack of effort: insufficiently quantified curation bias, no actual human baselines, over-strong conclusions about model vs scaffold effects, heavy dependence on LLM judges for deeper analyses, and some avoidable inconsistencies in reporting.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with benchmark design and agent evaluation, and I checked the main-paper methodology and reporting carefully, but some implementation specifics live outside the main text.