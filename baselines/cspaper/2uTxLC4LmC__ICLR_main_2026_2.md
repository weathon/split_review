---
job_id: a90b4c2a-dc2a-413d-bfe9-00f6e68714e2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2uTxLC4LmC.pdf
paper: Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on safety alignment for large reasoning models, process supervision, preference optimization, and empirical evaluation on reasoning and safety benchmarks.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments, results, and conclusion; it presents a coherent method with substantial empirical evaluation. I do see several methodological and clarity issues, but none rises to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper argues that safety alignment for large reasoning models should target the reasoning process itself, not only the final response. The authors study safety dynamics in chain-of-thought, identify what they call safety triggers and compliance cues, and propose Intervened Preference Optimization (IPO), which constructs preference pairs by replacing compliance cues with safety triggers and then performs DPO-style training from the divergence point. Experiments on three reasoning models and several safety benchmarks suggest improved reasoning-level and response-level safety, with limited degradation, and sometimes gains, on standard reasoning benchmarks.

## Strengths
1. The paper focuses on an important and under-addressed problem, namely the mismatch between safe final responses and unsafe intermediate reasoning. This framing is convincing and practically relevant for open models and settings where reasoning traces may be exposed or used downstream.

2. The core idea is intuitive and reasonably well motivated: instead of waiting for sparse end-of-trajectory safety signals, intervene locally at safety-critical points and turn the resulting corrected continuations into preference data. This is a sensible design choice, and it is more targeted than simply doing another round of safety SFT.

3. The empirical story is generally coherent from diagnosis to method. The progression from Figure 2 and Figure 3, which document the gap between reasoning safety and response safety, to Figure 4, which motivates why vanilla GRPO may struggle due to low rollout diversity, to Figure 5 and Figure 6, which motivate the intervention mechanism, makes for a fairly convincing pipeline. In particular, Figure 5(a) gives a useful operational picture of where safety “locks in,” and Figure 6 provides an intuitive sanity check that replacing early compliance cues can substantially reduce harmful continuation rates.

4. The main benchmark table is fairly strong. In Table 2, IPO improves average reasoning harmfulness across all three backbones, often by a noticeable margin over prior baselines. For example, on DS-8B, IPO reduces reasoning harmfulness on WildJailbreak to 23.4%, compared with 36.3% for GRPO and 37.8% for STAR; on Qwen3-8B, the gap between IPO and GRPO on reasoning harmfulness is also substantial, 13.9% vs. 23.3%. This is not a tiny win hidden in one corner of the table.

5. The paper also does a decent job of checking that the method is not merely collapsing into universal refusal. Table 2 includes XsTest and several reasoning benchmarks, and IPO does not look like the most conservative model in the comparison. The trade-off is not perfect, but the authors at least engage with it rather than quietly ignoring it.

6. The ablation in Table 3 is useful. The comparison between SFT, DPO on full trajectories, and DPO on the intervened suffixes helps support the specific design choice of optimizing from the divergence point. Likewise, Figure 7 aligns with the paper’s intended mechanism by showing larger divergence near compliance-related positions for IPO than for broader SFT-style baselines.

7. The paper is generally well organized, and the central method is understandable from the main text without requiring appendix-dependent reconstruction.

## Weaknesses
1. The method depends heavily on external GPT-4o judgments at multiple critical points, and this dependence is more central than the paper’s framing suggests. On Page 3, GPT-4o is the primary safety evaluator for both reasoning and response. On Page 6 to 7, GPT-4o is also used to detect the first compliance cue, which directly determines the divergence index \(h\) used in dataset construction and the training loss in Equation (4). In other words, the paper is not just using an external judge for evaluation, it is using one to define the supervision structure. This matters scientifically because the claimed gains may partly reflect transfer from GPT-4o’s own safety heuristics into the trained model, rather than a model-agnostic property of “safe reasoning.” The detector robustness check in Table 3 is helpful, but it is limited to StrongReject and only compares alternative detectors during construction, not alternative evaluators at test time. If the method’s success is tightly coupled to one proprietary judge, the broader claim of a general process-supervision mechanism becomes weaker.

2. The definition of the Continuation Safety Ratio in Equation (1) is mathematically awkward and under-specified. The paper defines
\[
S_i(x,z_s)=\mathbb{E}_{z_c \sim \pi_\theta(\cdot \mid x, z_s^{\le i})}\left[\mathbb{I}(z_s^{\le i} \| z_c \text{ is safe})\right].
\]
This mixes token-level prefixing and full-trajectory safety in a way that is not fully formalized. It is unclear whether “safe” is judged on the concatenated reasoning only, on reasoning plus response, or on reasoning continuation alone, especially since the paper later says it neglects the response \(y\) in the remaining notation. Also, the notation \(z_s^{\le i}\| z_c\) suggests the continuation may include the already-fixed token \(i\), but \(z_c\) is sampled conditioned on \(z_s^{\le i}\), so one must be careful not to double count or ambiguously define continuation boundaries. This may sound fussy, but here it matters because the whole trigger/compliance analysis in Figure 5 and the reward-shaping interpretation later depend on CSR being a precise quantity rather than a hand-wavy proxy.

3. The turning-point definitions in Equations (2) and (3) are heuristic and somewhat brittle, while the paper leans on them as if they reveal a stable structural property of safe reasoning. The thresholds \(\mu=0.9\), \(\eta=0.1\), and the window \(K=15\) are fixed choices, but the main text provides no sensitivity analysis in the main paper. Since the identification of safety triggers and unsafe turning points depends directly on these values, it is hard to tell whether the reported pattern in Figure 5 is robust or partially an artifact of thresholding. This matters because IPO’s conceptual selling point is that safety is concentrated around a few critical steps. If those steps move around substantially under small perturbations of \(\mu,\eta,K\), then the intervention narrative becomes less solid.

4. The “safety trigger pool” looks surprisingly narrow and hand-crafted relative to the generality of the claims. Table 4 in the appendix lists six trigger sentences, many of which are generic refusals such as “I shouldn’t be helping someone do that.” In the main paper, the authors describe triggers as if they capture an underlying safety-critical structure of reasoning, but operationally the method may be learning to insert a small number of highly stereotyped refusal phrases and continue from there. This raises a concern that the method is closer to targeted refusal templating than to genuine reasoning-level alignment. Figure 1 is visually effective in illustrating the idea, but it also exposes the risk: the intervention is literally lexical substitution of one sentence with another. That can work, but it is a more local and potentially less general contribution than the broader rhetoric about aligning reasoning processes suggests.

5. The comparison to GRPO in Section 2.3 and Table 1 is suggestive, but not fully conclusive as evidence that RL is inherently limited for this problem. Table 1 reports large gains from GRPO already, especially on JailbreakBench, and Section 2.3 attributes the remaining gap to low rollout diversity based mainly on Figure 4. However, Figure 4 is only a histogram over the number of safe reasonings in grouped rollouts from DS-8B, and it does not isolate whether the issue is GRPO specifically, the reward design, rollout budget, prompt set, or hyperparameter choices. Since GRPO is known to be sensitive to reward shaping and sampling schemes, the argument “RL is insufficient, therefore intervention-based DPO is needed” feels a bit overplayed given the evidence presented here. A fairer claim would be that this particular RL instantiation is sample-inefficient or less effective under the tested setup.

6. The empirical evaluation is strong on the chosen benchmarks, but the evidence for generality is still narrower than the paper’s claims. The main text uses three backbones, all in the 7B to 8B class in Section 4, and all safety benchmarks are single-turn prompt-response settings. Yet the Introduction and Conclusion repeatedly motivate risks for agentic systems and more realistic deployments. The paper itself acknowledges, on Page 10, that extension to multi-turn dialogue and agentic systems is future work. That is fine, but then the practical claims should be toned down. Right now the paper reads as if it has demonstrated a broadly deployable path to safer LRMs, when in fact it has shown a promising intervention strategy in fairly controlled single-turn settings.

7. The utility story is mixed, and the paper occasionally spins it a bit too hard. In Table 2, IPO preserves average benchmark performance reasonably well, but “preserves and even enhances” is somewhat selective. For DS-8B, the average utility improves from 66.7% to 68.5%, which is good, but MATH drops from 91.8% to 91.6% and HumanEval stays flat at 79.5%; for Qwen3-8B, average utility increases with GRPO more than with IPO, 80.8% vs. 80.2%. On XsTest, IPO’s compliance is noticeably below the base models and also below some stronger utility baselines. So the paper’s core safety contribution is credible, but the broader “best balance” claim should be stated with a bit more restraint.

8. The partial-DPO objective in Equation (4) is plausible, but some implementation details remain underspecified in the main text. The objective compares suffix likelihoods starting from \(h\), but because language models are autoregressive, the exact masking and normalization matter. Is the loss computed over all tokens in \(z^{\ge h}\) and \(\tilde z^{\ge h}\), including potentially different lengths, with standard summed token log-probabilities? Are sequences length-normalized? How is EOS handled? These details can materially affect DPO behavior, especially when comparing a short refusal-like trigger continuation against a longer unsafe completion. Since the whole point is to enforce preference at divergence steps, the training objective should be stated more explicitly.

9. The paper’s theoretical discussion around reward shaping is more analogy than justification, and it overreaches slightly. On Page 7, the paper says CSR is “exactly the value function” at state \(s_t=(x,z^{\le t})\), then suggests IPO can be analogized to potential-based shaping. This is not wrong at a very informal level, but it does not establish that the proposed DPO objective is equivalent to, or inherits guarantees from, reward shaping. There is no theorem, no policy invariance argument, and no demonstration that the shaping interpretation predicts the observed gains. I would strongly suggest the authors either formalize this connection properly or present it more modestly as intuition.

10. The literature positioning is good overall, but the paper could do more to distinguish itself from other process-level safety interventions that edit or backtrack reasoning trajectories. The related work on Page 10 mentions backtracking, step-level supervision, and critics, but the main paper does not sharply articulate where IPO is materially different beyond using preference optimization on intervened suffixes. Given how visually similar Figure 1 is to a generic “detect unsafe step, replace with safe step, continue” pipeline, the paper would benefit from a clearer statement of what exactly is new algorithmically and empirically relative to closely related reasoning-intervention and process-supervision lines.

## Questions
1. Could the authors clarify Equation (1) more formally? In particular, what exact object is judged by the safety evaluator when computing \(S_i(x,z)\): the reasoning trace only, the reasoning-plus-response completion, or only the continuation after prefix \(z^{\le i}\)? A precise definition would improve confidence in the trigger analysis.

2. How sensitive are the trigger/compliance statistics in Section 3.1 and 3.2 to the hyperparameters \(\mu\), \(\eta\), and \(K\) in Equations (2) and (3)? A small sensitivity table or plot in the rebuttal would be useful, because the central “critical step” claim depends on those thresholds.

3. How much of IPO’s gain comes from the intervention mechanism itself versus from GPT-4o-based cue localization and safety judgments? In rebuttal, it would strengthen the paper to report at least one cross-evaluator sanity check, for example using a different judge at test time, or a manual evaluation on a subset beyond the one consistency number already mentioned.

4. In Equation (4), how exactly are suffix log-probabilities computed for different-length continuations? Are they summed or length-normalized, and how is EOS treated? This is important because the model may otherwise be rewarded partly for shortening continuations rather than making them safer.

5. The paper states that safe reasoning naturally induces safer responses, partly motivated by Figure 3. Could the authors quantify this conditional relationship more carefully? For example, what is \(P(\text{safe response} \mid \text{safe reasoning})\) versus \(P(\text{safe response} \mid \text{unsafe reasoning})\) across all three models and datasets? That would make the “prioritize reasoning safety” claim much tighter.

6. Table 2 is promising, but the comparison against GRPO leaves room for alternate interpretations. Can the authors clarify whether GRPO was tuned with comparable care, and whether alternative reward formulations or larger rollout groups were attempted? I am not asking for a massive new experiment, but some detail here would help support the paper’s RL critique.

7. The trigger pool seems fairly small and lexicalized. Did the authors observe degradation when using paraphrased or semantically broader trigger templates? A brief analysis of trigger diversity would help distinguish “learning generic refusal phrases” from “learning safer reasoning transitions.”

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper studies harmful prompts, jailbreak benchmarks, and interventions on unsafe reasoning traces. Although the goal is defensive, the paper explicitly analyzes compliance cues and demonstrates how certain intermediate reasoning patterns correlate with unsafe continuations, especially in Section 3.2 and Figure 5(b). The manuscript is generally responsible, but any method that localizes safety-critical failure points in reasoning may also inform more adaptive jailbreak design. I do not see this as disqualifying, but it is worth an ethics check given the dual-use nature of the topic.

## Soundness Rating
3: good. The method is technically plausible and supported by fairly extensive experiments, but several central pieces, especially the CSR formalization, threshold-based trigger identification, and dependence on external judges, are not tight enough for a higher score.

## Presentation Rating
3: good. The paper is readable and well structured, with effective figures and a coherent narrative, though some mathematical definitions and implementation details need sharper exposition.

## Contribution Rating
3: good. The paper makes a meaningful contribution by pushing safety alignment toward reasoning-level supervision with a concrete intervention-based preference-learning scheme. I do not view it as a top-tier conceptual leap, but it is a useful and empirically relevant step.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a clear problem statement, a sensible intervention-based method, and solid empirical evidence that it improves reasoning safety. My hesitation comes from the heavy reliance on external GPT-4o judgments, heuristic trigger definitions, and somewhat overstated claims about mechanism and generality. On balance I lean positive, but this is not a slam dunk.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I carefully checked the main paper’s method, equations, figures, and tables, but some implementation-specific details would still benefit from clarification in rebuttal.