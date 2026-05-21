---
job_id: 330f7844-d7d2-465b-ae3e-be940d5e83c7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: c339hUw3cy.pdf
paper: Concurrence of the First Model Trained on a Current Data Collection
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through LLM post-training, dataset curation, benchmarking, and ML systems-oriented evaluation for code generation.

## Minimum Quality
Pass ✅. The submission includes an abstract, introduction, related work, methodology/data curation, experiments, quantitative results, discussion, and conclusion; while I have substantial technical concerns, the paper clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies supervised fine-tuning for CUDA kernel generation under limited high-quality data. The authors propose a two-stage synthesis and curation pipeline that generates PyTorch, reasoning trace, and CUDA kernel triples, then filters them using kernel correctness, speedup, reasoning length, and task balancing to build the ConCuR dataset of 4,892 examples. Fine-tuning QwQ-32B on this dataset yields KernelCoder, which is evaluated on KernelBench and compared against frontier and open-source baselines; the paper also argues that average reasoning length may serve as a proxy for kernel-generation task difficulty.

## Strengths
1. The paper tackles a real bottleneck in this area, namely the lack of open high-quality training data for kernel generation. Framing the contribution around data curation rather than yet another inference-time search stack is a reasonable and useful angle.

2. The overall pipeline is easy to understand. **Figure 1** gives a clear high-level overview of the two-stage process, from synthesis and unit testing to curation and final dataset construction. Even though some design choices are under-justified, the presentation of the pipeline itself is straightforward and reproducible at a conceptual level.

3. The empirical gains over the chosen base model are substantial. In **Table 1**, KernelCoder improves over QwQ-32B from 18.0 to 58.0 Exec on Level 1 and from 17.0 to 59.0 Exec on Level 2, with corresponding fast$_1$ gains from 7.0 to 17.0 and from 11.0 to 39.0. Whatever the caveats about broader comparison, this is a large within-family improvement and does support the claim that the curated SFT data is useful.

4. The ablation section is directionally helpful. **Table 4** compares several alternative selection strategies, including random, max-length, min-length, and speedup-only. KernelCoder is consistently better than these alternatives on both pass@1 and pass@10, especially on Level 2 fast$_1$, where it reaches 39.0 / 68.0 compared to 21.0 to 27.0 / 50.0 to 56.0 for the baselines. This does provide evidence that the exact curation recipe matters, not just the existence of any 5K-example dataset.

5. The paper is willing to test transfer across base models. **Table 5** shows improvements after fine-tuning for Qwen3-8B, Qwen3-32B, and QwQ-32B, which is useful because it suggests ConCuR is not purely overfit to one base model.

6. The efficiency comparison is appealing from a practical perspective. **Table 3** suggests a relatively small curated dataset and modest SFT budget can be competitive with substantially more expensive methods. This is a reasonable systems-oriented message for the community.

## Weaknesses
1. **The central claim about reasoning length is much weaker than the paper suggests, and the main figures do not fully support the stronger conclusions.**  
   The paper repeatedly argues that “concise yet informative reasoning traces” are crucial for robust kernel generation, and later uses reasoning length as both a curation signal and a task-difficulty proxy. However, the evidence in the main paper is largely correlational and partially inconsistent with the strength of the claims. In **Figure 2** on Page 4, the reported Pearson correlation between reasoning length and speedup is \(r=-0.047\) with \(p<0.01\), which is statistically significant only because the sample size is large; practically, this is near zero. That figure supports “little relationship with speedup,” not a strong positive case for short reasoning as a core quality signal. **Figure 3(a,b)** does show that incorrect generations tend to be longer on average, but this is still an aggregate association and does not isolate whether long reasoning causes errors, whether hard tasks induce both longer reasoning and more failures, or whether model-specific verbosity patterns are the real driver. The paper gestures at “for the same task” on Page 4, but no controlled within-task analysis is shown in the main paper.

2. **The proposed curation method in Section 3.5 is ad hoc, and several key choices are not justified or stress-tested.**  
   The dataset is assembled from three parts: (a) taking the shortest-reasoning sample if it also has the highest speedup, (b) adding kernels with speedup \(>5\), and (c) adding 544 single-operator samples to balance task types. These are consequential design choices, but the paper does not explain why this precise rule is preferable to more principled scoring or Pareto-style selection. Why require “shortest and fastest” jointly rather than optimize a continuous criterion over correctness, speedup, and length? Why is the threshold exactly 5 for part (b)? Why 544 additional single-operator tasks, and how sensitive is performance to that number? The paper says in Section 5 that combining these parts is crucial, but **Table 4** does not ablate the three parts of ConCuR directly; it mostly compares against alternative one-criterion datasets. That is not enough to validate the exact recipe advocated in Section 3.5.

3. **There is a potentially serious train/eval contamination concern that the paper does not resolve clearly enough.**  
   On Page 4, the data synthesis starts from KernelBook tasks, while evaluation is on KernelBench. The paper never states explicitly whether there is any overlap, near-duplicate problem structure, or templated leakage between KernelBook and KernelBench. In this domain, many tasks are small operator kernels or common fusion patterns, so overlap in implementation motifs could materially inflate performance. This matters even more because **Table 3** explicitly notes that Kevin used 180 KernelBench problems for training, which shows that benchmark contamination is a live issue in this literature. The paper should state unambiguously, in the main text, whether ConCuR excludes all KernelBench tasks and any near-duplicates. Without that clarification, the headline benchmark gains are harder to interpret.

4. **Some comparison claims are overstated relative to the actual tables.**  
   The paper says KernelCoder “surpasses all frontier models” and emphasizes improvement in both correctness and performance. That is not uniformly true. In **Table 1**, on Level 1 fast$_1$, KernelCoder gets 17.0, which is below DeepSeek-R1-0528 (CUDA) at 18.0 and far below Qwen3-Coder-Plus at 35.0. In **Table 2**, KernelCoder is best on Level 1 Exec at 91.0, but not on Level 2 Exec, where DeepSeek-R1-0528 reaches 97.0 versus KernelCoder’s 95.0; it also trails Qwen3-Coder-Plus on Level 2 fast$_1$ (68.0 vs 76.0). So the paper can credibly claim strong overall performance and excellent gains for a 32B SFT model, but not clean dominance over all frontier models across metrics. The wording should be made more precise.

5. **The evaluation protocol is not rigorous enough for the correctness claims.**  
   Section 3.2 states that correctness is checked by giving “a random input” to both the PyTorch implementation and the generated kernel, and if outputs match in dimension and values, the kernel is considered correct. For generated CUDA kernels, a single random test is not a reliable correctness criterion. It can miss indexing bugs, dtype issues, shape corner cases, boundary-condition failures, and numerically unstable behavior. This is especially concerning because correctness then directly gates the speedup metric in **Equation (1)**. If the kernel validation is weak, both the training set quality and benchmark metrics are noisy. At minimum, the paper should specify how many test cases, which tolerances, what input ranges, what seeds, and whether edge cases are used.

6. **The mathematical definitions are underspecified or somewhat inconsistent in ways that matter for interpretation.**  
   In **Equation (1)**, speedup is defined as
   \[
   \text{speedup}=\frac{T_{\text{Torch}}}{T_{\text{kernel}}}\cdot\mathbf{1}_{\text{correct}}[\text{kernel}].
   \]
   Then **Equation (2)** defines
   \[
   \operatorname{fast}_p = \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}_{\text{correct}}[\text{speedup}_i > p].
   \]
   This notation is awkward because correctness is already folded into speedup via Equation (1). If \(\text{speedup}_i=0\) for incorrect kernels, then \(\mathbf{1}[\text{speedup}_i>p]\) is already sufficient, and the extra correctness notation is redundant or ambiguous. Also, the subscripted indicator \(\mathbf{1}_{\text{correct}}[\cdot]\) is not standard notation and makes the definition harder to parse.  
   A second issue appears in **Equation (3)** for ARL:
   \[
   \text{ARL}=\frac{1}{NM}\sum_{i=1}^{N}\sum_{j=1}^{M}L[i,j].
   \]
   This averages raw reasoning lengths over all generations, regardless of whether generations are correct or incorrect. But the paper then interprets ARL as a proxy for intrinsic task difficulty in Section 6. That interpretation is not justified, because ARL may also reflect model verbosity, failed reasoning trajectories, prompt sensitivity, or systematic overthinking. If ARL is meant as a difficulty estimate, the paper should justify why averaging over all attempts, rather than e.g. only correct ones or calibrated conditional statistics, is valid.

7. **The benchmark scope is too narrow for the breadth of the paper’s claims.**  
   Section 4.2 evaluates only KernelBench Levels 1 and 2, excluding Levels 3 and 4 because “they exceed the capabilities of current LLMs.” That is understandable pragmatically, but the resulting claims should be narrowed. The paper is really showing strength on relatively simple operator and fusion tasks, not on kernel generation in general. This is especially important because the paper positions itself as a general solution to the lack of data for kernel generation, and because the proposed reasoning-length difficulty metric is partly motivated as a broader benchmark construction tool.

8. **There is little information about variance, decoding settings, and statistical reliability of the reported gains.**  
   For pass@1 and pass@10, the paper does not report confidence intervals, multiple-run variance, or sensitivity to decoding temperature and sampling parameters. In a stochastic code-generation setting, especially with pass@10, these details matter a lot. For example, were all models run with the same sampling budget, prompt wrapper, stop criteria, max tokens, and compilation timeout? The paper notes that all evaluations are run on 8 RTX 5090 GPUs, but hardware alone is not the crucial missing detail. Without tighter reporting, some of the comparisons in **Tables 1 and 2** are hard to audit.

9. **The ablation evidence does not cleanly establish the “reasoning quality” mechanism claimed in the discussion.**  
   **Table 4** shows that KernelCoder outperforms several alternative selection schemes, but the ARL column does not strongly support the claimed mechanism. KernelCoder’s ARL is 7035.9 on Level 1, which is actually very close to 5K-random at 7065.3 and 5K-speedup at 7119.3. On Level 2 it is 6410.8 versus 6447.2 and 6435.0. So the explanation that ConCuR teaches “better reasoning length calibration” is not strongly evidenced by these numbers. The better interpretation may simply be that the curated dataset has better examples overall, but then the paper should say that more modestly instead of over-reading ARL.

10. **The paper is reasonably written overall, but several places overstate causality or importance from limited evidence.**  
   For example, the discussion around DeepSeek-V3.1-Think in **Table 2** attributes its worse performance to “highly compressed” CoTs and says that this “decreases the quality of CoTs.” That is speculation, not an experimentally established causal finding here. Similarly, Section 6 presents ARL-based difficulty division as successful, but **Table 7** includes somewhat irregular geometric speedup behavior, for example Qwen3-8B has higher Gspeedup on Hard than on Medium, which complicates the narrative. The paper would benefit from a more careful distinction between observations, hypotheses, and validated conclusions.

## Questions
1. Please clarify the relationship between KernelBook and KernelBench. Is there any exact overlap, near-duplicate overlap, or templated overlap between the training tasks used to construct ConCuR and the KernelBench evaluation tasks? A precise contamination analysis would substantially increase my confidence.

2. How exactly is correctness checked during both data curation and benchmark evaluation? How many random inputs are used per task, what numerical tolerances are applied, are multiple shapes tested when applicable, and are edge cases included? If this was stronger than the main paper suggests, please spell it out.

3. Can you provide a controlled within-task analysis supporting the “shorter reasoning is better” claim? For example, for each task, compare correctness rates across bins of reasoning length after normalizing within that task, rather than only aggregating across all tasks as in **Figure 3**.

4. Why is the curation threshold in Section 3.5 part (b) set to speedup \(>5\)? Did you test nearby thresholds such as \(>2\), \(>3\), or \(>10\)? Likewise, how was the additional set of 544 single-operator tasks chosen? A sensitivity analysis would help.

5. The paper’s strongest empirical point is the large gain over QwQ-32B. Can you provide a cleaner apples-to-apples comparison between ConCuR and a same-size uncurated or lightly curated dataset generated from the same source model, with matched sample count and training recipe? **Table 4** goes in this direction, but more detail on exact data distributions would help.

6. For **Equations (1)–(3)**, please clarify the metric definitions and notation. In particular, is fast$_p$ effectively just \(\frac{1}{N}\sum_i \mathbf{1}[\text{speedup}_i>p]\) given Equation (1)? And why is ARL over all generations an appropriate estimator for task difficulty rather than a model-dependent verbosity statistic?

7. Please report the full decoding protocol for pass@1 and pass@10, including sampling temperature, top-\(p\), max new tokens, compile/runtime timeouts, and whether all models receive identical prompting and number of retries. This would make the results in **Tables 1 and 2** much more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the main paper. The work is about model training and benchmarking for GPU kernel generation, and the submission does not appear to involve sensitive personal data, human subjects, or deployment claims that would independently trigger ethics review.

## Soundness Rating
2: fair. The empirical signal is interesting and there are clear gains over the base model, but the main causal claims about reasoning length, the curation mechanism, and benchmark validity are not supported as rigorously as the paper suggests.

## Presentation Rating
3: good. The paper is readable, the high-level story is easy to follow, and the figures/tables are generally informative, but some claims are overstated and several definitions and evaluation details need tightening.

## Contribution Rating
2: fair. The dataset-and-curation angle is relevant and potentially useful, but the novelty is moderate and the scientific contribution is weakened by under-justified heuristics, limited validation, and over-claimed conclusions.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a useful practical idea and strong improvements over its base model, but too many core claims are currently supported by suggestive correlations and heuristic choices rather than careful validation. With a cleaner contamination analysis, stronger correctness evaluation, and tighter evidence around the reasoning-length hypothesis, I could see this becoming publishable, but in its current form I lean negative.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details that were only briefly described in the main paper.