---
job_id: 1c67f377-2b8d-42ac-a80b-d2b6a27e5dc2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: rRB1bYErbL.pdf
paper: R-HORIZON: How Far Can Your Large Reasoning Model Really Go in Breadth and Depth?
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on reasoning benchmarks, reinforcement learning with verified rewards, and evaluation/training of large reasoning models.

## Minimum Quality
Pass ✅. The paper includes the expected scientific components, namely abstract, introduction, related work, method, experiments, results/analysis, and conclusion, and it presents a complete empirical study with benchmark construction plus RL training experiments. While I have several concerns about methodology and positioning, none rise to the level of a desk-reject flaw.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative reviewer-targeted instructions, or suspicious concealed text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper introduces R-HORIZON, a query-composition framework for constructing long-horizon reasoning tasks from existing single-problem datasets. The authors use it to build a benchmark spanning math, code, and web-search tasks, evaluate a large set of reasoning models under increasing composition depth, and study reinforcement learning with verified rewards on composed training data. The central empirical claim is that current large reasoning models degrade substantially on multi-step composed tasks, and that RL training on R-HORIZON data improves both composed-task performance and some standard reasoning benchmarks.

## Strengths
The paper tackles a timely and important question, namely whether current large reasoning models can sustain reasoning quality across multiple interdependent subproblems rather than isolated single-shot tasks. This is a useful benchmark direction, and it is more informative than yet another single-problem leaderboard.

The benchmark construction idea is simple and operational. In particular, **Figure 2** does a good job of making the composition pipeline concrete: it distinguishes seed questions, composed questions, and expanded questions, and clarifies the difference between directly composed, sequentially composed, and graphically composed settings. That figure materially improves understanding of what the benchmark is actually testing.

The empirical coverage is broad. Evaluating many models across math, code, and agentic tasks is valuable, and **Figure 3** is one of the stronger parts of the paper because it shows the degradation trend consistently across datasets rather than relying on a single cherry-picked benchmark. Even from the summarized heatmap, one can see that the drop with increasing query count is not limited to one model family.

The paper goes beyond raw accuracy and offers a reasonably interesting diagnostic suite. **Figures 5, 6, 7, and 8** provide analyses of error types, error positions, reflection behavior, and token-budget allocation. I particularly appreciated that **Figure 5** separates "problem reasoning error" from "dependency reasoning error" and "early stop", because this helps distinguish whether the benchmark is merely punishing arithmetic propagation mistakes or exposing broader long-horizon failures.

The RL section is not just an afterthought. The authors train on composed data and show improvements over single-problem RL training. **Table 1** is useful here: it suggests that composed-query training improves not only multi-problem performance but often also the original single-problem performance, and that reward choice matters. The comparison between \(R_{\text{last}}\) and \(R_{\text{all}}\) is especially relevant for the paper's long-horizon thesis.

The work is mostly well motivated and clearly written at the high level. The main message is easy to follow, and the benchmark/training contributions are reasonably aligned.

## Weaknesses
1. **The main benchmark signal is confounded by multiplicative error accumulation and strict all-or-nothing scoring, and the paper does not sufficiently disentangle this from genuinely new long-horizon reasoning failure.**  
   The core evaluation in **Equation (3)** defines success only if all subproblems are correct. This is a very harsh metric. The expected baseline in **Equation (4)** is then computed as \(\prod_i p_i\), which implicitly assumes independence across subproblems and also assumes that the only source of degradation should be simple multiplicative compounding of atomic error rates. That is a very strong assumption in a setting where the prompt format changes, answer extraction changes, output length changes, and earlier mistakes alter later problem statements through dependencies. Put differently, the benchmark is simultaneously varying horizon length, prompt complexity, response formatting burden, and sequential error propagation.  
   This matters because the paper's headline claim, that LRMs have "limited effective reasoning length", is stronger than what the current evaluation design cleanly supports. A gap between actual accuracy and \(\prod_i p_i\) could arise from many factors other than an intrinsic horizon boundary. The authors do show an ablation on dependent vs independent composition in Appendix D.1, but in the main paper they do not sufficiently isolate which fraction of the drop comes from horizon length itself versus evaluation protocol artifacts. This is especially important because **Figure 1** and **Figure 6** are presented almost as evidence of a principled reasoning-length law, while the benchmark itself changes several variables at once.

2. **The composition mechanism for math tasks is quite synthetic, and the paper overstates its connection to "real-world long-horizon reasoning".**  
   In **Algorithm 1** and the surrounding text on **Page 4**, the dependency function is defined as
   \[
   f_i(x) = x + (m_{i+1} - a_i),
   \]
   which ensures that plugging in the previous answer recovers the original integer \(m_{i+1}\). This is clever for controllability, but it also makes the dependency structure rather artificial. The model is often solving a sequence of otherwise standard benchmark questions with a templated variable substitution layer inserted on top. That is meaningfully different from authentic long-horizon reasoning tasks in which later subproblems emerge naturally from earlier deductions, plans, or world-state changes.  
   Why this matters: the paper repeatedly motivates the work with language about planning and acting over "thousands or even millions" of steps on **Page 2**, but the benchmark is mostly a controlled composition test of short standard tasks. That is still useful, but the framing should be more modest. As written, the paper risks selling synthetic dependency chaining as a stronger proxy for real agentic long-horizon reasoning than the evidence warrants.

3. **The mathematical specification is under-explained in several places, and some notation/objective choices are sloppy enough to affect reproducibility.**  
   The definition of the key-variable verifier in **Equation (2)** is underspecified. The paper says \(M(q,m)=1\) if removing \(m\) renders the problem unsolvable, but does not explain how this is operationally determined in the main paper. Is \(M\) a prompted LLM classifier, a heuristic, or a manually validated detector? The benchmark quality depends heavily on this step, because a poor key-variable detector will create weak or spurious dependencies. Since the main method rests on identifying "critical" integers, this should not be punted away.  
   There is also a mismatch in the RL objective exposition. In **Equation (5)**, the paper writes a GRPO token-level objective with a KL term \(-\beta D_{\mathrm{KL}}[\pi_\theta \| \pi_{\mathrm{ref}}]\), but **Appendix F.1** later states, "Notably, we do not apply any KL loss in our training process." If \(\beta = 0\) in all experiments, that should be stated explicitly in the main paper rather than presenting a generic objective that was not actually used. Otherwise the exposition is misleading, because the formal training objective in the paper is not the implemented one.  
   More broadly, \(\pi_{\theta_{\text{idf}}}\) in **Section 3.3** seems likely intended to be the old or behavior policy, but the notation is unconventional and unexplained. That alone is minor, but together with the KL inconsistency it gives the RL section a somewhat boilerplate feel rather than a carefully paper-specific formulation.

4. **The extraction-based evaluation introduces another potentially important source of noise, but the main paper does not quantify its effect enough.**  
   On **Page 5**, the authors note they use model-based extraction to obtain all answers from free-form responses, with details deferred to Appendix E.2. Then in **Appendix E.2 / Table 3**, they show that rule-based vs model-based extraction disagree increasingly as the number of composed problems grows, with consistency dropping to 91.04% at 16 problems. That is not negligible. Since the main headline of the paper is that performance degrades with horizon length, an evaluator whose reliability worsens with horizon length is a nontrivial confound.  
   This matters because some of the reported gap may partly reflect format-following and extraction issues rather than pure reasoning. The paper itself notes that many models fail to follow the output format as composition grows. That is still a real usability issue, but it is not identical to long-horizon reasoning failure. The main paper should report either human verification on a subset, extraction error estimates stratified by \(n\), or sensitivity analyses showing that the central conclusions survive evaluator noise.

5. **The code and agent settings are not methodologically symmetric with the math setting, weakening the claim of a unified long-horizon benchmark.**  
   For math, the core setup is sequentially dependent composition. For code, **Appendix A** says the authors use "directly composed concatenation" without explicit dependencies between problems. For WebShaper, they construct sub-questions from DAGs, but the final benchmark size is quite small, only 50 composed questions according to **Table 2** on **Page 20**. These are materially different task constructions.  
   This matters because the paper's central framing suggests a general benchmark for breadth and depth, but in practice the three domains test different stressors: dependency propagation in math, multi-task packing in code, and tool-use/decomposition in web tasks. The large degradation in **Figure 3** is therefore harder to interpret as evidence of one coherent phenomenon. A more precise claim would be that R-HORIZON is a family of composition-based stress tests, not a single unified measure of long-horizon reasoning.

6. **The RL evidence is promising but still too narrow to support broad training claims.**  
   Most of the RL study centers on a single base model, R1-Qwen-7B, as described in **Section 4.3**. That is fine for a first pass, but the paper's conclusion speaks much more generally about R-HORIZON as a scalable paradigm for improving long-horizon capabilities. A single-model RL study makes it hard to know whether the gains are robust across architectures or whether they depend on this particular starting point and recipe.  
   **Figure 4** shows cleaner training curves for composed data than for original data, and **Table 1** reports substantial gains. But there are still missing controls: for example, a matched-token or matched-compute comparison, a curriculum baseline, or a baseline that simply concatenates independent tasks during RL without dependencies. Without those, it is difficult to know whether the gains come from long-horizon supervision specifically, from increased task diversity per sample, from denser reward opportunities, or from better difficulty shaping.

7. **The "effective reasoning length" analysis is suggestive, not yet convincing as a scientific construct.**  
   In **Figure 6**, the authors plot actual vs expected accuracy and an "error position" range, then infer model-specific reasoning boundaries such as 4-6k tokens for 7B and 8-10k for 32B on Math500. This is an interesting observation, but the notion of error position is not formalized carefully enough in the main paper to justify boundary-style claims. Is the "error position" the token index where the first wrong step occurs, where the first wrong final answer becomes inevitable, or where the model shifts to another problem? These are different objects.  
   This matters because the paper repeatedly interprets these plots mechanistically, but the evidence is largely correlational. If the goal is to argue for model-specific effective reasoning lengths, the paper needs more controlled interventions, for example fixing total output budget, varying only the order of problems, or comparing with a segmented prompting baseline where each solved answer is fed back into the next problem externally. Without such controls, "effective reasoning length" remains a plausible but not well-isolated interpretation.

8. **The paper misses some relevant recent benchmark positioning, making the literature framing feel incomplete.**  
   The related work discusses test-time scaling, effective reasoning length, NEST/REST-style concatenation, and GSM-Infinite, which is a good start. But for a paper centered on long-chain or long-horizon reasoning evaluation, the positioning would be stronger with broader discussion of adjacent benchmark efforts focused on long-form reasoning, reflection quality, and thinking efficiency. As it stands, the paper mainly positions itself against single-horizon reasoning benchmarks and a small number of multi-problem stress tests.  
   This matters less than the methodological issues above, but it still affects how clearly readers can distinguish the paper's specific niche: is the main contribution dependency-aware composition, long-output stress testing, reflection analysis, or RL training on composed tasks? A sharper literature comparison would help.

9. **Some claims in the presentation are stronger than the evidence and occasionally drift into over-interpretation.**  
   A concrete example is the statement on **Page 2** that LRMs "often reflect within the current problem, failing to identify errors from previous questions." **Figure 7** does support the claim that long-range reflection is limited, but the operational definition of "reflection" is based on lexical cues such as "wait" or "but..." according to the text in **Section 5.1**, which is at best a rough proxy for self-correction. Models can revise reasoning without these markers, and they can emit these markers performatively without genuine reflection.  
   Similarly, the conclusion that R-HORIZON training "alleviates the overthinking phenomenon" is too strong based on **Figure 9(b,d)** alone. Shorter responses and different token allocation patterns are compatible with better efficiency, but they do not by themselves demonstrate reduction of overthinking in the stronger sense used in the cited literature.

10. **There are several writing and presentation issues that, while not fatal, reduce polish.**  
   Examples include repeated capitalization inconsistency between "R-Horizon" and "R-HORIZON", several typos such as "interger" in **Page 3**, "CONLUSION" in **Page 10**, and somewhat rough phrasing in the RL section. The paper is readable overall, but these issues contribute to the impression that some parts, especially the formal method/RL exposition, could have been tightened.

## Questions
1. The biggest issue for me is disentangling genuine long-horizon reasoning failure from artifacts of the evaluation protocol. Could the authors provide, in rebuttal, results for at least one decomposition where each subproblem is scored individually and the next subproblem is fed the gold previous answer externally? This would help separate sequential error propagation from within-context long-horizon reasoning limits.

2. For **Equation (4)**, what exactly justifies the independence-style expected accuracy estimate \(\prod_i p_i\) once the problems are embedded in a single longer prompt with changed formatting and dependency structure? I would like the authors to clarify whether this is intended as a strict probabilistic baseline or merely a rough heuristic, and ideally provide confidence intervals or a calibration analysis.

3. Please clarify the implementation of the key-variable detector \(M\) in **Equation (2)**. What model is used, how often does it fail, and was any human validation performed? Since dependency quality hinges on \(K(q)\), this is not a minor detail.

4. In **Equation (5)** versus **Appendix F.1**, is the KL term actually used in any experiment? If not, please restate the objective in the main paper with \(\beta=0\) or otherwise make the implemented optimization objective explicit.

5. For the RL results in **Table 1**, can the authors comment on whether improvements hold under compute-matched or token-matched training budgets? Right now it is hard to tell whether composed data is better because it teaches horizon handling, because it changes reward density, or because it exposes more useful difficulty structure per rollout.

6. Since **Table 3** shows evaluator consistency deteriorating as the number of composed problems increases, can the authors provide a manual audit of a subset of extracted answers for large \(n\)? That would materially increase confidence in the benchmark conclusions.

7. For **Figure 8**, have the authors considered a normalized budget-allocation metric that controls for per-problem difficulty, rather than raw token distribution by order? Otherwise, "bad allocation" may partly reflect later problems being easier or harder in a particular ordering.

8. The math setting is the only one with explicit sequential dependencies. Could the authors clarify how strongly the main conclusions depend on this setting, versus the more loosely composed code and WebShaper settings?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work is a benchmark and training-data construction study on existing reasoning datasets and model evaluations.

## Soundness Rating
2: fair. The empirical trends are interesting and likely directionally real, but several central claims, especially around effective reasoning length and long-horizon causality, are not fully isolated from confounds in the benchmark design and evaluation protocol.

## Presentation Rating
3: good. The paper is generally readable and the figures are informative, but some mathematical definitions, implementation details, and claim calibration need tightening.

## Contribution Rating
3: good. The benchmark direction is valuable and the RL experiments make the paper more than just a stress-test note, but the methodological limitations and synthetic task construction reduce how strongly I view the contribution.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper asks an important question and provides a useful empirical benchmark plus promising RL evidence, and I do think the community would learn something from it. That said, I am not fully convinced that the benchmark cleanly isolates long-horizon reasoning as opposed to a mixture of error compounding, prompt packing, extraction noise, and synthetic dependency artifacts. So I land slightly positive, but not comfortably so.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main methodological concerns, though some uncertainty remains because several implementation details are only partially specified in the main paper.