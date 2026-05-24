Now I have sufficient calibration data. Let me write the consolidated review.

## Summary
This paper proposes SmartSwitch, a training-free, plug-and-play inference framework that detects and mitigates "underthinking" in Long Chain-of-Thought (LongCoT) reasoning. It monitors LLM generation for thought switches, evaluates abandoned thoughts using an off-the-shelf Process Reward Model (PRM), and backtracks to inject a deepening prompt when a promising thought was prematurely abandoned. Experiments across five models (1.5B–32B) and five math benchmarks show consistent accuracy improvements, with gains up to 23.3 points on AIME25.

## Strengths
- **Clear problem characterization with empirical evidence.** The paper defines a measurable Underthinking Frequency metric (Eq. 1) and provides extensive evidence of underthinking across six LongCoT LLMs (Figure 1b), with correlation to problem difficulty and incorrect answers (Figure 2). This establishes a well-justified motivation for the method.

- **Significant and consistent accuracy gains across models and benchmarks.** SmartSwitch improves pass@1 accuracy for all five tested models across all five benchmarks (Table 1), including competition-level datasets AIME24, AIME25, AMC23, and MATH-500. Gains are particularly large for smaller models (e.g., +23.3 points for DeepSeek-R1-Distill-Qwen-7B on AIME25) and persist even for strong models like QwQ-32B (+7.2 on AIME24, reaching 86.7%).

- **Thorough ablation study validates design choices.** The "Always Intervene" baseline degrades performance below vanilla (Table 4, 18.9% vs 20.0%), confirming selective PRM-guided intervention is essential. Process division strategy (Table 6), score mapping (Table 7), and PRM choice (Table 4) are all systematically ablated. Comparison against standard prompting and TIP (Table 5) shows SmartSwitch substantially outperforms alternative mitigation methods.

- **Method is simple, training-free, and model-agnostic.** SmartSwitch requires no fine-tuning and works as a drop-in with any LLM, making it practical for immediate deployment across diverse model families and sizes.

## Weaknesses

### Fatal
None.

### Major
- **Key hyperparameters tuned directly on test benchmarks, partially compromising reported gains.** The potential score threshold (Table 8) and process-to-thought score mapping (Table 7) were selected based on AIME24 performance, and the process division strategy (Table 6) was selected based on AIME25 performance — the same benchmarks used for reporting main results in Table 1. No held-out validation set is used. This means AIME24 and AIME25 accuracy numbers are partly in-sample. The extreme sensitivity to the threshold (e.g., DeepSeek-R1-Distill-Qwen-7B drops from 66.7% to 43.3% between thresholds 0.70 and 0.71, Table 8) further suggests brittleness. However, gains remain positive on benchmarks not used for any tuning (AMC23, MATH-500, GaoKao2023en), indicating the method does provide genuine improvement beyond overfitting. The paper would be substantially strengthened by fixing hyperparameters on a held-out validation set and reporting test-set results only once.

### Minor
- **Efficiency claims are insufficiently explained.** Table 2 reports modest token-count reductions (e.g., 2.8% for the 7B model on AIME24), yet Table 3 reports inference-time reductions up to 35.3% for the same model. The large gap between token savings and time savings is not analyzed. Since SmartSwitch introduces extra computation (PRM scoring, backtracking), a speedup of this magnitude requires a breakdown of where the time is saved — e.g., reduced number of thought switches lowering per-step overhead, or shorter context lengths. Without this, the efficiency numbers are difficult to interpret.

- **Underthinking Frequency metric is partly circular for evaluating the method.** UF (Eq. 1) counts thoughts shorter than a token threshold. Since SmartSwitch works by forcibly lengthening promising thoughts, a reduction in UF is an almost inevitable side effect regardless of reasoning quality improvement. This doesn't invalidate the accuracy gains, but weakens the narrative that UF reduction independently demonstrates mitigation of underthinking. The reduction in thought-switching count (Figure 4b) is a less circular supporting metric.

### Trivial
- The TIP baseline comparison (Table 5) does not describe how TIP's penalty coefficient was chosen; if TIP was not tuned with comparable effort, the comparison may be somewhat unbalanced.
- The paper acknowledges that thought-switch detection relies on explicit linguistic cues (e.g., "Alternatively"), which may miss implicit switches (Section 6, Limitations). This is acknowledged by the authors and appropriate for the scope.

## Nice-to-Haves
- Introducing a proper held-out validation set (e.g., a separate competition year) and reporting all results with hyperparameters fixed from that validation set would substantially improve credibility.
- A detailed breakdown of inference time (generation vs. PRM scoring vs. backtracking overhead) would resolve the unexplained gap between token and time efficiency.
- Demonstrating that the score threshold maintains reasonable performance across a broader range (e.g., 0.65–0.75) rather than requiring precise tuning at 0.70 would make the method more practically appealing.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The thought segmentation uses an LLM (DeepSeek-V3) whose own segmentation quality is not analysed"** — This concerns the UF metric analysis in Section 3, not the main SmartSwitch method. The main method uses linguistic cues for switch detection, not DeepSeek-V3. The claim about UF segmentation quality is valid as a minor observation but doesn't affect the core contribution. Removed as it applies to a preliminary analysis tool, not the method itself.

- **"The claim that SmartSwitch 'maintains 100% accuracy on all previously correct answers' could be a consequence of the threshold being tuned to avoid disturbing already correct solution paths"** — This is speculative. The paper reports this as an observation for one specific model-benchmark pair (DeepSeek-R1-Distill-Qwen-14B on AIME24). Without evidence that the threshold was specifically tuned to achieve this property, this remains speculation. Removed as an unsupported inference.

- **"No details are given about how TIP's penalty coefficient was chosen"** — Already captured in Trivial weaknesses above at appropriate severity.

- **Strength Finder claim about "100% accuracy on AMC23" being a core strength** — This is a single data point from one model-benchmark pair. While impressive, it's not independently a core strength beyond what the general accuracy gains already demonstrate. Merged into the broader accuracy strength.

## Novel Insights
The paper's characterization of underthinking via the UF metric provides a useful empirical lens, but the most practically valuable insight is that selective, PRM-guided backtracking at inference time can recover reasoning performance without any training — and that naive "always intervene" strategies actually hurt. The finding that a properly-calibrated PRM score threshold is critical (with performance collapsing just 0.01 away from optimal) is both a strength (the method works when tuned) and a concern (it may be brittle), and this tension itself is a genuine empirical finding worth noting.

## Suggestions
- The highest-impact improvement would be to designate one benchmark year (e.g., AIME24) as a validation set for all hyperparameter selection, and report final results only on AIME25, AMC23, MATH-500, and GaoKao2023en. This alone would address the major weakness.
- Provide a cost model: report PRM inference time per call, average number of PRM calls per problem, and explain the token-to-time efficiency gap quantitatively.
- Consider evaluating with multiple PRM score thresholds fixed a priori (e.g., 0.65, 0.70, 0.75) and report all results, to demonstrate robustness rather than peak performance at a single tuned value.

## Score and Decision

**Calibration Anchor Summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| pXIbcRPxWR (Supervised CoT) | 2.50 | R1 | Significantly weaker — limited evaluation, less developed method |
| sdpVfWOUQA (MCTS Planning) | 3.00 | R1 | Significantly weaker — narrower scope, less convincing results |
| rpbzBXdo4x (CoT Reduces Performance) | 5.00 | R1 | Weaker — fundamental design concerns, poorly substantiated claims |
| 8WQ7VTfPTl (SADI) | 6.40 | R2 | Slightly weaker — SmartSwitch has broader evaluation, but SADI has fewer methodological concerns |
| W6yIKliMot (FAI Attention Intervention) | 6.50 | R1/R2 | Comparable — similar inference-time intervention for reasoning; SmartSwitch has better evaluation scale but has the test-set tuning issue |
| Ze4aPP0tIn (TSMC Verification) | 6.60 | R2 | Comparable — both are verification/PRM-guided math reasoning methods; TSMC has theory, SmartSwitch has broader eval |
| IssPhpUsKt (Rep Engineering) | 6.80 | R1/R2 | Slightly stronger — more principled approach, but SmartSwitch has broader evaluation |
| 3bq3jsvcQ1 (Step-Back Prompting) | 8.00 | R1 | Stronger — cleaner contribution, no methodological issues, but narrower model evaluation |

**Round 1 Bracket:** 6.0–7.5  
**Round 2 Narrowing:** The paper is most comparable to FAI (6.50) and TSMC (6.60). SmartSwitch has better evaluation breadth than both but suffers from the test-set tuning issue which neither of those papers shares to the same degree. I place it at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>