---
job_id: a1d60cc1-3026-4a13-927e-7a52bf35fefd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: YuxgSGFaqb.pdf
paper: SwingArena: Adversarial Programming Arena for Long-Context GitHub Issue Solving
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This submission is clearly within ICLR scope as a benchmark and evaluation framework for ML systems, specifically LLMs for repository-level software engineering, with emphasis on long-context reasoning, adversarial evaluation, and benchmarking infrastructure.

## Minimum Quality
Pass ✅ The paper contains the expected components for a benchmark paper, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While I have substantive concerns about metric design, experimental controls, and clarity of some methodological details, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect hidden instructions, prompt injection attempts, or suspicious manipulative text in the paper content.

# Expected Review Outcome:
## Summary
This paper introduces SwingArena, a benchmark and evaluation framework for GitHub issue solving that simulates an adversarial software engineering workflow between two LLM agents, a submitter that proposes patches and a reviewer that generates tests. The framework executes repository-native CI pipelines on real multi-language repositories and includes a retrieval-augmented code generation module, RACG, to provide bounded relevant context from large codebases. The empirical study covers 400 curated issue instances across C++, Python, Rust, and Go, with analyses of model matchups, language-specific performance, and retrieval ablations.

## Strengths
The problem setting is timely and important. Moving beyond static unit-test benchmarks toward repo-level, CI-grounded, interactive evaluation is a meaningful direction, and the paper makes a reasonable case in Sections 1 and 3 that current one-shot code benchmarks under-measure real software engineering behavior.

The benchmark scope is broader than many prior issue-solving setups. The paper covers four languages, uses real repositories and linked issue/PR pairs, and incorporates repository-native CI workflows rather than only hidden unit tests. That makes the setting more operationally realistic than many existing evaluations.

The overall framework is easy to understand. **Figure 2** is particularly useful here: it clearly communicates the data flow among retrieval, patch generation, test generation, patch verification, test verification, and final verification, as well as the role-switching battle structure. Even though several protocol details still need tightening, the diagram helps the reader see what the authors are trying to operationalize.

The paper does a decent job of framing RACG as supportive infrastructure rather than overselling it as a major algorithmic advance. That positioning is appropriate. The modular decomposition into file retrieval, chunking, reranking, and token-budget-aware packing in Section 3.3 is also sensible for a benchmark paper.

There is some evidence that retrieval matters in this setting. **Table 3** shows consistent gains from using RACG over the no-RACG setup across all four languages, with especially visible win-rate gains in Python, C++, and Go. Even if the gains are not massive and the comparison space is limited, this at least supports the claim that long-context handling is not incidental.

The paper is also commendably concrete about implementation aspects that often get hand-waved in benchmark papers, including Dockerized CI execution, role alternation, fixed prompting, pinned evaluation recipes, and deterministic decoding in primary experiments.

## Weaknesses
1. **The core evaluation metrics are not yet well aligned with the paper’s stated scientific goal, and in places they are actively misleading.**  
   The central promise is to evaluate realistic software engineering ability under adversarial review and CI. However, the reported headline outcome in **Table 1** is dominated by a very high “Win Rate,” often between 0.89 and 1.00, while the corresponding submitter and reviewer CI pass rates are much lower, typically around 0.54 to 0.71. That mismatch is hard to reconcile. If SPR and RPR are only around the mid-0.5 to mid-0.6 range, win rates approaching 1.00 suggest the win criterion is too weak, too aggregated, or too forgiving. The paper briefly notes on **Page 7** that Win Rate is adversarial and should be interpreted together with SPR/RPR, but this caveat is not enough. As written, the main results table creates an overly optimistic impression of model capability. This matters because the paper’s main empirical message, namely that the arena reveals nuanced model trade-offs, depends heavily on how “winning” is defined. A metric that saturates near 1.0 for almost every matchup weakens the benchmark’s discriminative power.

2. **The battle protocol remains underspecified in several places, which makes it difficult to understand exactly what is measured.**  
   There are multiple descriptions of the protocol in Sections 3.2, 3.3, 4.1, and **Algorithm 1** on **Page 18**, and they do not fully line up. For example, the main text says the reviewer receives \(+1\) if their test fails the submitter’s patch and \(-1\) if it fails the golden patch, while the algorithm says “if Test fails to expose meaningful flaw then Test Agent loses 1 point,” but “meaningful flaw” is not formally defined. Likewise, the paper says models alternate roles across multiple rounds and the battle terminates after 10 rounds, yet the formal metrics in Section 4.1, including Win Rate, are defined at the task level without clearly specifying whether the unit of aggregation is per round, per role assignment, per battle, or per task after all rounds. This is not a cosmetic issue. In an adversarial multi-round setting, small changes in aggregation can materially change rankings.

3. **The mathematical formalization is too thin for a paper whose contribution is primarily an evaluation protocol.**  
   The paper does provide formulas for \(\mathrm{Best@}k\), \(\mathrm{SPR}\), and \(\mathrm{RPR}\) on **Page 7**, but crucial pieces are missing:
   - For Win Rate, the text defines it as “the fraction of battles whose final outcome is that the submitter’s patch passes all CI checks and agrees with the golden fix.” The phrase “agrees with the golden fix” is not mathematically defined. Does this mean exact diff equality, semantic equivalence as judged by an LLM, equal tests passed, or something else?
   - The scoring rule for the reviewer is partly binary, partly CI-based, and partly dependent on the golden patch, but there is no formal joint objective over rounds.
   - The reviewer is said on **Page 6-7** to receive “contextual hints including which parts of the code were most changed by the patch.” This is a powerful asymmetry that effectively leaks patch-localization information. Yet the paper does not formalize this information channel, nor quantify how much it contributes.  
   Because the contribution is the protocol itself, not just a model benchmark, the lack of precise formalization matters more than usual. Right now the equations describe some surface metrics, but not the actual game being played.

4. **The empirical comparison space is narrower than the claims suggest, especially regarding baselines against non-adversarial evaluation.**  
   The paper repeatedly argues that static benchmarks miss important behavior, but it never directly demonstrates that SwingArena changes model ranking or reveals errors that a standard non-adversarial repo-level setup would miss in a controlled comparison. A very natural baseline would be the same tasks with the same retrieval pipeline and same patch generation budget, but without reviewer-generated tests or without multi-round interaction. As is, the paper asserts that adversarial CI evaluation surfaces overlooked limitations, but the evidence is indirect. **Table 1** compares models within the arena, not the arena against a carefully matched non-arena evaluation protocol. This weakens the causal claim that the adversarial setup itself is responsible for the extra diagnostic value.

5. **The RACG study is useful but still methodologically limited, making it hard to isolate what component actually helps.**  
   Section 3.3 presents RACG as a combination of BM25 file retrieval, syntax-aware chunking, CodeBERT reranking, and token packing, yet **Table 3** only compares “w/ RACG” vs “w/o RACG” and a few retrieval-only variants such as BM25 and Top-k related retrievals. This leaves several unanswered questions: Is the gain coming from chunk granularity, dense reranking, packing policy, or simply from retrieving more relevant files? The file hit rate results in **Table 5/Table 6** are informative, but they also reveal some odd behavior, for example BM25 Top-20 hit rate being lower than Top-10, and chunk-based methods also slightly decreasing from Top-10 to Top-20. That can happen depending on metric definition, but then the definition should be clarified because “Top-20” should not intuitively underperform “Top-10” if it means inclusion within a larger set. This suggests either a reporting issue or a nonstandard measurement setup. Since RACG is presented as an important enabling component, the ablation needs tighter design and clearer metrics.

6. **Some of the strongest claims are more interpretive than supported.**  
   For instance, the text around **Table 1** claims “GPT-4o's aggressive patching advantage” and that DeepSeek and Gemini “prioritize correctness and CI stability.” But the evidence for psychological or strategic model tendencies is fairly thin. The table shows differences in SPR, RPR, and win rate, but these metrics conflate many factors, including reviewer quality, retrieval adequacy, prompt fit, and CI policy strictness. Similar over-interpretation appears in the failure typology in Appendix C, where correlations and model-specific error profiles are described in a way that sounds stronger than the paper’s sample size and methodology warrant. The paper would be stronger if it stayed closer to the observable facts and framed these as hypotheses rather than stable model “behaviors.”

7. **The dataset curation process raises concerns about selection bias and benchmark representativeness.**  
   On **Page 4**, the authors mine repositories by popularity, filter by CI pass success, use an LLM judge for clarity and difficulty, and then apply expert filtering. This may produce a cleaner benchmark, but it also risks selecting issues that are unusually well-specified, tractable, and aligned with the authors’ preferred evaluation style. The paper releases 2,300 issue-PR pairs but evaluates on 400 selected samples and a 100-sample ablation split. The main text does not sufficiently characterize how much the filtering changes the distribution of issue types, repository sizes, patch complexity, or CI strictness. **Figure 1** shows the construction pipeline clearly, which is good for transparency, but it also makes the amount of filtering visually obvious. That is precisely why the paper should quantify the attrition more carefully in the main text. Without that, external validity remains uncertain.

8. **Presentation is decent overall, but there are several inconsistencies and signs of rushed assembly that reduce confidence.**  
   The paper has repeated “Battle Protocol” descriptions in Sections 3.2 and 3.3, and some appendix references are inconsistent, for example “Table 6” is discussed on **Page 9** while the actual table later appears duplicated as **Table 5** and **Table 6** with identical contents. There are also some obvious wording issues, such as “morbidity” being used where “complexity” seems intended on **Page 15**, and the open-source results in **Table 4** appear mislabeled in the self-play rows, for example “Qwen2.5-7B vs Qwen2.5-7B” has reviewer listed as Seed-8B. These are not fatal, but for a benchmark paper, sloppy bookkeeping is more damaging than usual because readers need to trust the protocol details.

9. **The Best@k analysis is underdeveloped relative to the claimed importance of test-time scaling.**  
   **Figure 3** plots Best@k win rate, but it only appears to use Qwen2.5-Coder-7B self-play at temperature 0.25. This is too narrow to support broader conclusions about scaling behavior in the arena. If the point is that the arena supports stochastic search and test-time scaling, then the analysis should either include multiple models or be presented as a very limited case study. As currently placed, the figure feels more like a teaser than a substantive result.

10. **The role of the golden patch is potentially problematic and insufficiently discussed.**  
    The paper relies on the golden human patch for validation references and for rejecting reviewer tests that fail on the golden patch. This is pragmatic, but real GitHub issues often admit multiple acceptable fixes. If “agreement with the golden fix” is interpreted too strictly, the benchmark may penalize valid alternative repairs. If it is interpreted loosely through functional equivalence, then the exact judging mechanism needs to be specified. The paper mentions a “Golden Patch Comparison Prompt” later in the appendix, which suggests an LLM may be involved in some equivalence judgments, but the main text does not make this explicit enough. This matters because the scientific meaning of “solved” depends on it.

## Questions
1. Please define the unit of evaluation much more precisely. Is Win Rate computed per round, per battle after 10 rounds, per role pair, or per task aggregated across rounds? A compact formal definition would help a lot. Right now the text and Algorithm 1 leave room for multiple interpretations.

2. How exactly is “agrees with the golden fix” operationalized in the Win Rate definition on **Page 7**? Is this exact patch matching, CI-based functional equivalence, or an LLM judgment against the golden patch? A concrete definition here could materially increase my confidence.

3. Can you provide a matched non-adversarial control, using the same 400 tasks, same retrieval setup, and same models, but without reviewer-generated tests or role interaction? This would directly test whether the adversarial arena adds discriminative value beyond ordinary repo-level CI evaluation.

4. Reviewer assistance seems asymmetric because the reviewer is given hints about which parts of the code were changed by the patch in Section 3.3. How much does this help? A simple ablation with and without patch-localization hints would clarify whether the reviewer is truly “reasoning adversarially” versus being steered to the answer region.

5. In **Table 1**, why are Win Rates so close to 1.0 even when SPR and RPR are much lower? Please provide the exact aggregation logic, and ideally a decomposition of battle outcomes into categories such as patch fails base CI, reviewer test rejected, reviewer test passes golden patch but fails candidate patch, and so on.

6. In **Table 3** and **Table 5/Table 6**, can you clarify why Top-20 hit rates are lower than Top-10 hit rates? If the metric is “correct file appears within Top-k,” monotonicity would normally be expected. If the reported values use a different definition, please state it explicitly.

7. The paper says all evaluations use deterministic decoding in the main setup, with higher-temperature sampling only in the scaling-law study. Given the adversarial and iterative nature of the framework, do the model rankings remain stable across a few random seeds or mild prompt perturbations? The appendix mentions modest variance, but a short main-text summary with actual model ranking stability would make the benchmark more convincing.

8. Please clarify the curation funnel in the main text, not only the appendix. Starting from mined repositories and PRs, how many candidates are filtered out at each step in **Figure 1**, and for what dominant reasons? This would help assess how representative the final 400 tasks are.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper evaluates and potentially improves LLMs for repository-level code modification and test generation. As acknowledged in the broader impact section, this capability can be dual-use, including for vulnerability discovery, exploit development, or malware-adjacent automation. That alone does not make the work unethical, but it does raise a mild safety concern.

There is also a legal/compliance angle because the benchmark mines and redistributes artifacts from GitHub repositories. The main text says the release is “license-aware” on **Page 4**, which is good, but the exact redistribution policy, especially for patches, tests, and repository snippets, should be clearly documented to ensure compatibility with repository licenses and terms of use.

I do not see a reason to block the paper on ethics grounds, but these issues deserve explicit handling.

## Soundness Rating
3: good. The paper presents a substantial benchmark and the main empirical claims are partly supported, but important protocol details, metric definitions, and controls are still insufficiently specified for me to call the evidence fully airtight.

## Presentation Rating
3: good. The overall story is readable and figures like **Figure 1** and **Figure 2** help, but there are repeated sections, table inconsistencies, and several ambiguities that should have been cleaned up.

## Contribution Rating
3: good. A CI-grounded, adversarial, multi-language issue-solving arena is a worthwhile contribution for the community, even though the current version does not yet isolate all factors or fully validate its claimed diagnostic advantages.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I see a real contribution here, especially in pushing evaluation closer to realistic repository workflows, and I think the benchmark direction is important for ICLR. At the same time, the paper is trying to sell both a benchmark and an evaluation philosophy, and the current version does not fully nail the protocol definition, metric design, or the causal evidence that adversarial interaction is what drives the extra insight. So this is a cautious positive from me, not an enthusiastic one.

## Reviewer Confidence
4: confident. I am confident in my assessment and familiar with the benchmarking and repo-level code evaluation landscape, though some implementation-specific details remain ambiguous because the main text does not pin them down tightly enough.