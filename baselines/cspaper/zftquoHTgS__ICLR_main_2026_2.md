---
job_id: 1717b886-a794-4990-83f1-e67c7615a1fe
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zftquoHTgS.pdf
paper: SmartSwitch: Advancing LLM Reasoning by Overcoming Underthinking via Promoting Deeper Thought Exploration
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on inference-time control for LLM reasoning, evaluation of reasoning behavior, and benchmark-based study of long chain-of-thought behavior.

## Minimum Quality
Pass ✅. The submission contains the core scientific sections, namely Abstract, Introduction, Related Work, Methodology, Experiments, Results/Analysis, and Discussion/Conclusion, and it presents a concrete method with empirical evaluation. While I have serious concerns about novelty, methodology, and evaluation rigor, these issues do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies the "underthinking" phenomenon in long chain-of-thought reasoning, defined as models switching away from a thought too early, and proposes SmartSwitch, a test-time framework that detects thought-switch cues, scores the preceding thought with an external process reward model, and, when the score exceeds a threshold, backtracks and injects a prompt encouraging deeper exploration. The method is evaluated on several math reasoning benchmarks using DeepSeek-R1-Distill-Qwen models and QwQ-32B, with reported improvements in pass@1 accuracy, reductions in underthinking frequency, and in many cases shorter responses and lower wall-clock inference time.

## Strengths
The paper tackles a real and timely issue in long-reasoning models. The central intuition, that some failures come not from inability to reason but from abandoning a promising path too early, is plausible and operationally useful. I appreciate that the paper frames this as an inference-time intervention problem rather than requiring retraining.

The method is simple and easy to understand. The pipeline in **Figure 3** is one of the stronger aspects of the paper: it clearly conveys the perception-intervention cycle, the role of thought-switch detection, PRM-based evaluation, and the backtracking plus prompt injection step. This makes the proposed framework reasonably accessible and likely reproducible from the main text.

The empirical gains reported in **Table 1** are substantial across several model sizes and datasets. In particular, the improvements on AIME24 and AIME25 are large enough to be interesting, especially for smaller models. The paper also includes comparisons beyond raw accuracy, such as response length (**Table 2**) and inference time (**Table 3**), which is useful because the claimed motivation is partly about avoiding wasted exploration.

The paper includes ablations on several components, including the PRM choice (**Table 4**), comparison with a thought-switching penalty baseline and standard prompting (**Table 5**), segmentation strategies (**Table 6**), score aggregation (**Table 7**), and threshold sensitivity (**Table 8**). Even though I have concerns about how to interpret some of these, the attempt to unpack the system is appreciated.

The qualitative case studies are helpful for intuition. In **Figures 6, 7, and 8** and the associated case descriptions, the authors show concrete examples where the vanilla model repeatedly says variants of "Alternatively" and seems to thrash across many short thoughts, while SmartSwitch re-focuses the trajectory. These examples are not proof, but they do illustrate the intended failure mode and the intended mechanism in a way that is easier to inspect than the aggregate tables alone.

## Weaknesses
1. **The paper's central metric for "underthinking" is too weakly justified, and may not measure what the paper claims it measures.**  
   In **Section 3.2, Page 4**, the Underthinking Frequency metric is defined in **Equation (1)** as
   \[
   \mathrm{UF}_L = \sum_{i=1}^M \lambda_i(L), \quad \lambda_i(L)=\mathbf{1}[|T_i|<L].
   \]
   So "underthinking" is operationalized almost entirely as "a thought segment shorter than a threshold." This is a very blunt proxy. Short thoughts are not necessarily prematurely abandoned thoughts; they can be legitimate quick eliminations, sanity checks, or concise but correct sub-arguments. Conversely, long thoughts can still be low-quality flailing. The paper does acknowledge this is heuristic, but then builds a large part of its empirical narrative on this metric, including prevalence claims in **Figure 1(b)** and difficulty correlations in **Figure 2**. Without stronger validation, the paper risks relabeling "frequent short segments" as "underthinking" without showing that the metric aligns with actual premature abandonment judged by humans or by outcome-sensitive annotations. This matters because the paper's framing, motivation, and intervention logic all rest on the claim that the measured phenomenon is real and distinct, not just an artifact of segmentation or verbosity.

2. **The definition of a "thought" is itself unstable, and the paper uses inconsistent segmentation mechanisms across analysis and method.**  
   In **Section 3.2, Page 4**, the paper says the full reasoning process is segmented into thoughts using "a capable LLM" such as DeepSeek-V3. But in the actual SmartSwitch framework in **Section 4.2, Pages 5-6**, thought boundaries are detected online via hand-written linguistic cues such as "Alternatively." These are very different operationalizations. One is post hoc LLM-based segmentation, the other is a sparse trigger-list heuristic. This inconsistency makes the underthinking analysis less tightly connected to the deployed system than the paper implies. In other words, the paper diagnoses the problem using one segmentation regime and fixes it using another. The ablation in **Table 6** partly touches process division strategy, but it still does not resolve the deeper issue that the object "thought" is not consistently defined throughout the paper. This matters scientifically because the diagnosis and intervention should be aligned if the paper wants to claim it is correcting the measured failure mode.

3. **The method description is underspecified in several places, especially around scoring and aggregation, which makes it hard to assess what is really being optimized or intervened on.**  
   In **Section 4.2**, the PRM scores a preceding thought \(T_{\text{prev}}\), but in **Page 9**, the paper later says a thought may consist of multiple processes, and then process-level scores are aggregated with strategies such as max, min, mean, weighted average, or last, with "last" selected in **Table 7**. This creates ambiguity about what the PRM actually consumes in the main experiments: is the unit of scoring the whole thought, multiple sub-processes within a thought, or some adaptive subdivision? If multiple segments are scored, the exact aggregation should be part of the main method statement rather than appearing later as an ablation detail. Similar underspecification appears in the pseudocode in **Figure 5 / Algorithm 1 (Page 14)**, where `Score(Steps(O_prefix))` is abstract and does not spell out how the "steps" are produced online, how the threshold is calibrated, or what happens if repeated interventions revisit nearly identical contexts. This matters for reproducibility and for understanding whether the gains come from a principled mechanism or from one very specific prompt-plus-threshold recipe.

4. **The threshold sensitivity is severe, and the paper does not convincingly show robustness.**  
   **Table 8 (Page 9)** is actually quite alarming. Moving the threshold from \(0.70\) to \(0.69\) or \(0.71\) often causes very large drops. For example, R1-Distill-Qwen-1.5B goes from 40.0 at \(0.70\) to 30.0 at both neighboring thresholds; QwQ-32B goes from 86.7 at \(0.70\) to 73.3 at \(0.69\) and \(0.71\). That is a very sharp optimum for a single scalar hyperparameter, especially given the small benchmark sizes. Yet the paper's main text says the chosen setting is "effective across various models" and presents the threshold as if it were relatively stable. The evidence shown suggests the opposite: the method may be highly tuned to a narrow threshold region. This matters because a plug-and-play inference framework should ideally be robust, not brittle to one decimal place in the PRM score cutoff.

5. **There is a serious risk of test-set tuning or, at minimum, insufficiently controlled hyperparameter selection.**  
   The threshold in **Table 8** is evaluated directly on AIME24, and the implementation section on **Page 6** then states that the authors set the promising score threshold to 0.7 for the main system. The paper never clearly states what separate validation set was used to choose this threshold, the intervention cap, the 200-token subdivision threshold, the cue list, or the score aggregation rule. Since benchmark sizes are small, especially AIME24 and AIME25 with 30 questions each, tuning on the reported test benchmark would materially inflate conclusions. The paper does mention reproducibility and fixed seeds in the appendix, but that is not the issue. The issue is model selection protocol. For an ICLR paper, this is not a minor bookkeeping detail. If the same benchmarks are used both to pick hyperparameters and to report final gains, then the empirical support becomes much less convincing.

6. **The empirical comparisons are not yet strong enough to isolate what actually causes the gains.**  
   SmartSwitch bundles together several elements: cue-based switch detection, backtracking, PRM scoring, a deepening prompt, a cap on interventions, and a specific score aggregation rule. The "Always Intervene" ablation in **Table 4** is helpful but not sufficient. What is missing is a cleaner decomposition such as: backtracking + prompt without PRM filtering, PRM filtering without backtracking, prompting at random switch points with matched frequency, or prompting based on thought length only. Without these controls, it is hard to tell whether the improvement comes from accurately identifying abandoned promising thoughts, or simply from giving the model another chance and an encouraging meta-prompt at strategic moments. This matters because the paper claims a specific causal story, namely that PRM-guided detection of prematurely abandoned high-potential thoughts is the key mechanism. The current experiments do not convincingly separate that story from simpler explanations.

7. **The reported efficiency gains are interesting but not fully persuasive, and in places the interpretation feels overconfident.**  
   The paper claims improved efficiency despite extra PRM scoring and intervention overhead. **Table 3 (Page 6)** indeed reports lower wall-clock time for SmartSwitch across listed competition benchmarks, and **Table 2** often shows shorter generations. But the reductions are uneven, and one row in **Table 2** even shows *longer* responses for R1-Distill-Qwen-14B on "All" tokens, \(14128.90 \to 14480.20\), despite the efficiency narrative. Also, the formatting in **Table 2** is suspicious in at least one case: for the 1.5B model, the value changes from 14973.97 to 13486.80, yet the table reports "↓0.95%"; that percentage appears inconsistent with the raw numbers. If the summary statistics themselves contain such mismatches, it weakens confidence in the efficiency claims. More importantly, the computational cost of running a separate 7B PRM online is only partially reflected in the high-level wall-clock measurement. The paper does not characterize memory overhead, batching assumptions, hardware contention, or whether the timing includes realistic serving conditions. Since the method is pitched as plug-and-play, deployment cost matters.

8. **The comparison set is too narrow relative to the breadth of the claims.**  
   The experiments are exclusively on mathematical reasoning benchmarks. Yet the paper repeatedly uses broader language such as improving "LLM reasoning" and being broadly compatible with "any large language model" as a plug-and-play solution. The actual evidence supports a narrower claim: the method may help on a family of math-oriented long-CoT models, especially those that visibly emit cue words like "Alternatively." That is still potentially useful, but the paper overshoots the evidence. This matters because SmartSwitch depends on assumptions that may fail outside math, for example explicit verbalized switching cues, availability of a strong math-oriented PRM, and long deliberative traces.

9. **The literature positioning is incomplete for a paper that claims to identify and address a distinct reasoning pathology.**  
   The paper cites Wang et al. (2025) on underthinking and compares against TIP in **Table 5**, which is good. However, the broader positioning around length-control, reasoning-depth control, and underthinking/overthinking tradeoffs is still thin. The paper repeatedly presents SmartSwitch as addressing a general gap between overthinking and underthinking, but the related work section on **Pages 2-3** stays rather high level and does not adequately situate this method among recent test-time reasoning control approaches and more systematic studies of reasoning length versus correctness. As written, the framing risks sounding more differentiated than the evidence currently shows.

10. **Some parts of the exposition are sloppy enough to hinder confidence in technical details.**  
   There are repeated wording and notation issues, for example "Under-thinking" vs "underthinking", "process" vs "thought", "T_pre" vs "T_prev", and awkward or broken pseudocode in **Algorithm 1 / Figure 5 (Page 14)**, which is even labeled "Simplified Ff Framework" rather than SmartSwitch. The pseudocode variables are inconsistent, several lines are incomplete, and control flow is only partly specified. There are also odd textual glitches in the qualitative examples and prompts. None of these individually is fatal, but collectively they create the impression that the paper has not yet been polished to the level expected for a main-track ICLR paper. Presentation quality matters more here because the method is relatively simple; if the writing and algorithm box are imprecise, reviewers are left guessing about important implementation choices.

11. **The analysis figures support the narrative only partially, and some interpretations are overstated.**  
   **Figure 1(b)** shows rising \(\mathrm{UF}\langle L\rangle\) with the threshold \(L\), but that is mechanically expected from the definition in **Equation (1)**. As \(L\) increases, more segments will be counted as short. So the figure is not, by itself, strong evidence of widespread underthinking; it mainly illustrates threshold dependence. Likewise, **Figure 2(a)** showing higher UF on harder problems is suggestive but not causal. Harder problems can cause more exploratory branching, more failed starts, or simply more fragmented output, none of which uniquely implies the specific pathology the paper emphasizes. The paper draws quite strong conclusions from these plots, while the evidence is more correlational and proxy-dependent.

## Questions
1. **Hyperparameter selection protocol:** How were \(\tau_{\text{score}}=0.70\), the 200-token split threshold, the cue list, the "last" aggregation rule from **Table 7**, and the max intervention count of 3 selected? Please clarify whether any held-out validation set was used, and whether the reported test benchmarks were also used for tuning. A clean answer here would materially affect my confidence.

2. **Metric validation:** Can the authors provide evidence that \(\mathrm{UF}_L\) from **Equation (1)** correlates with genuine premature abandonment rather than just short segments? For example, even a small human annotation study on whether a short thought was actually promising and abandoned too early would help. Without this, the paper's diagnosis remains somewhat circular.

3. **Mechanism isolation:** Can the authors report additional ablations that disentangle the components of SmartSwitch? In particular, I would like to see:  
   - backtracking + deepen prompt without PRM filtering,  
   - PRM-triggered intervention without backtracking,  
   - intervention at random cue-triggered points with the same average number of interventions,  
   - intervention based on a simple heuristic such as short-thought length rather than PRM score.  
   These would clarify whether the improvement comes from the PRM-based "promising thought" detection or just from strategic re-prompting.

4. **Robustness of thresholding:** **Table 8** suggests strong brittleness around \(\tau=0.70\). Are these numbers stable across multiple random seeds, and do broader threshold sweeps or validation on a separate dataset show a robust plateau anywhere? If the method only works at one narrow threshold, that should be discussed more candidly.

5. **Scope of generality:** The method is advertised as plug-and-play and broadly compatible, but all evaluations are math benchmarks using math-capable LongCoT models and a math-oriented PRM. Do the authors have any evidence, even preliminary, that the cue-based switch detection and PRM scoring transfer to non-math reasoning tasks?

6. **Online scoring details:** In the main method on **Pages 5-6**, it sounds like the full preceding thought is scored, while later discussion implies subdivision into processes and score aggregation. Please give a precise definition of the online scoring unit used in the main experiments, ideally in one concise mathematical or algorithmic description.

7. **Efficiency accounting:** For **Tables 2 and 3**, please clarify exactly what was included in timing, whether PRM computation was serialized or batched, and whether the reported wall-clock times include all SmartSwitch overhead under the same serving setup as vanilla. Also please verify the percentage reductions in **Table 2**, since at least one percentage seems inconsistent with the raw values.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the paper itself. The work is an inference-time reasoning intervention on public math benchmarks and does not appear to introduce a direct fairness, privacy, or human-subjects issue in its current form.

## Soundness Rating
2: fair. The core idea is plausible and the experimental gains are interesting, but the main empirical claims rest on a weakly validated metric, there is insufficient clarity about tuning and component contributions, and the robustness evidence is not strong enough.

## Presentation Rating
2: fair. The high-level idea and **Figure 3** are clear, but the paper has important imprecision in notation, algorithm description, and methodological exposition, and some tables/pseudocode contain inconsistencies that reduce confidence.

## Contribution Rating
2: fair. The problem is important and the intervention is practically appealing, but the current paper does not yet establish the method as a sufficiently well-understood or convincingly validated contribution for ICLR main track.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and the empirical gains are hard to ignore, but there are too many unresolved issues around the validity of the "underthinking" measurement, hyperparameter/tuning protocol, mechanism attribution, and robustness for me to recommend acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main equations, figures, and tables carefully, but some implementation details remain ambiguous from the text alone.