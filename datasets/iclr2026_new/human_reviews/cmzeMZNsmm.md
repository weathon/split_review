## Human Reviewer 1

### Summary
* **Research Problem**:
  Investigates whether Large Reasoning Models (LRMs), despite their strong inherent reasoning capabilities, still benefit from prompt optimization, and whether they can serve as effective prompt optimizers—using event extraction as a structured testbed.

* **Experimental Method**:
  Evaluates two LRMs (DeepSeek-R1, OpenAI o1) and two LLMs (GPT-4.5, GPT-4o) in both task-model and prompt-optimizer roles within a Monte Carlo Tree Search (MCTS) framework; experiments are conducted on event extraction (ACE05), symbolic reasoning, and biomedical NER tasks.

* **Main Findings**:

  1. LRMs significantly benefit from prompt optimization, with greater performance gains than LLMs.
  2. LRMs (especially DeepSeek-R1) outperform LLMs as prompt optimizers, producing higher-quality, more stable, and more concise prompts.
  3. These benefits generalize beyond event extraction to other domains, including symbolic and biomedical tasks.

### Strengths
1. The paper revisits prompt optimization in the context of Large Reasoning Models (LRMs) which is a meanful topic. It challenges the prevailing assumption that strong reasoning models no longer require prompt optimization, offering a novel empirical perspective.


2. The main insight of the experiment are constructive: the performance of LRM can be further improved by optimizing prompts.

### Weaknesses
1. Although the authors have conducted meaningful empirical research, this paper does not make any original theoretical or experimental contributions.

2. The overall experimental focus of this paper remains primarily on event extraction. Evaluation on a wider range of NLP tasks would enhance the significance of the paper's conclusions.

3. The conclusions of this paper are highly dependent on the test model and test task. LLMs are highly dependent on training data, and LRMs are primarily optimized for complex reasoning tasks. Do similar conclusions hold for the recent SOTA models o3 and o4? For datasets that are already saturated, optimizing prompt words will obviously not bring any improvement. For extremely difficult problems, such FrontierMath or ARC-AGI, can optimizing prompt also bring improvement?

### Questions
1. Can the authors generalize the evaluation task to a wider range of NLP tasks, not just event extraction?
2. Do similar conclusions hold for the recent SOTA LRMs?
3.  Do similar conclusions hold for extremely difficult problems, such FrontierMath or ARC-AGI?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper presents a timely and systematic empirical study investigating whether the advanced reasoning capabilities of Large Reasoning Models (LRMs) like DeepSeek-R1 and o1 diminish the need for prompt optimization, using the complex task of event extraction as a primary case study; the authors claim that LRMs still benefit significantly from optimization, that they serve as more effective prompt optimizers than general-purpose LLMs, and that these findings generalize to other tasks like symbolic reasoning and biomedical NER.

### Strengths
(1) Clear motivation and timely question: The paper addresses a relevant and open question in the era of advanced reasoning models: whether prompt engineering remains necessary. This is especially valuable as the community increasingly adopts LRMs without fully understanding their interaction with prompting strategies.

(2) Rigorous experimental design: The use of a unified MCTS-based prompt optimization framework allows fair comparison across models as both task solvers and optimizers. The inclusion of low- and medium-resource settings, depth-controlled MCTS rollouts, and cross-task generalization strengthens the empirical foundation.

(3) Comprehensive analysis: The paper includes convergence curves, survival plots, error categorization, and qualitative prompt comparisons, offering multiple lenses to interpret results. The observation that DeepSeek-R1 achieves high performance with shorter prompts is insightful.

### Weaknesses
(1) Limited Methodological Novelty: The core optimization algorithm (MCTS) is adopted from prior work (e.g., PromptAgent). The primary novelty lies in its application to LRMs rather than in a fundamental advancement of the optimization technique itself. The paper is more of a thorough empirical benchmark than a methodological contribution.

(2) Task selection bias: Event extraction is a highly structured, schema-constrained task. While the authors test generalization on two other tasks, the main conclusions are anchored in a setting where explicit guidelines and code-based prompting play an outsized role. It remains unclear whether the observed LRM advantages would hold in more open-ended reasoning tasks (e.g., mathematical proof, planning).

(3) Incremental Nature of Key Finding: The central finding that more capable models benefit from optimized prompts is intuitively plausible and, to some extent, expected. While the quantitative demonstration is valuable, it may not be sufficiently surprising or groundbreaking for a top-tier venue.

### Questions
(1) Beyond the application of an existing MCTS framework to a new model class (LRMs), what is the core conceptual or methodological novelty of this work that distinguishes it from prior prompt optimization research?

(2) How confident are you that the observed advantages of LRMs would hold on the full ACE05 dataset with all 33 event types? Did you run any preliminary experiments that suggested context length would become a major bottleneck?

(3) In the Geometric Shapes and NCBI tasks, did you use the same code-based prompting format? If not, how was the prompt structure adapted, and could that influence the observed generalization?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper studies whether Large Reasoning Models (LRMs; DeepSeek-R1, OpenAI o1) still benefit from prompt optimization and whether they are good optimizers themselves, using event extraction (ACE05) as a case study within an MCTS framework. The main finding is that optimization helps all models but LRMs benefit most, both as task models and as optimizers. The claim is probed further with convergence/quality analyses and two non-EE tasks.

### Strengths
S1 - Clear problem framing and technically sound MCTS setup with explicit four-step loop.

S2 - 2. Strong, easy-to-grasp headline result that LRMs both benefit more from optimization and optimize better than LLMs.

S3 - 1. Sensible experimental design with two data regimes (ACElow/ACEmed) and two evaluation depths (depth 1 vs depth 5), enabling controlled comparison/

### Weaknesses
W1 - Metric mismatch in optimization v reporting -- The reward aggregates averaged F1 across TI/TC/AI/AC (s. 3.2), yet the analysis "primarily reports AC" (I understand the authors provide a citation for this choice but I find it unsatisfactory), creating a potential objective-reporting mismatch. Clarify why not optimize AC directly. 

W2 - Downsampling schema may bias conclusions -- To avoid (presumably) long prompts, the paper downsamples ACE05 to 10 event types and leaves long-contextg processing to future work (L236-245). This choice may favor models preferring concise prompts and limits external validity to full-schema EE. 

W3 - Depth-5 gains are modest, at best. Paper does note "non-dramatic" improvements from full-depth over d-1 (RQ2) and tab 1 shows small deltas. This sort of raises questions about the practical alue of deeper search. 

W4 - No statistical uncertainty reported. Main tables/figures lack confidence intervals or sig tests, making it hard to judge robustness of improvements.

### Questions
Q1. Why optimize the average of TI/TC/AI/AC instead of AC directly, given AC is your primary metric? Any evidence that the averaged reward improves AC more than AC-only reward?

Q2. How were the 10 ACE05 event types chosen, and do conclusions hold on the full 33-type schema (or with long-context methods)?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper studies the interaction of prompt optimization for Large Reasoning Models (LRMs). They identify that this is a gap in existing literature which has only studied prompt optimization for Large Language Models (LLMs). In this work, DeepSeek-R1 and o1 are representative LRMs while GPT-4.5 and GPT4o are representative LLMs.

In particular, the paper focuses on structured prediction tasks since performance on these tasks is not yet saturated even with LRMs. The core analysis is conducted on the ACE05 Event Extraction task with supplementary analysis on Geometric Shapes and NCBI Disease NER tasks to show the generality of the findings. The paper uses a MCTS-based discrete prompt optimization algorithm with different LLMs/LRMs plugged in as the optimizer.

The core finding is that LRMs benefit from prompt optimization in both low and medium data regimes. Prompt optimized LRMs out-perform and have out-sized gains compared to prompt optimized LLMs. Moreover, they serve as effective optimizers for other LRMs/LLMs. This finding generalizes to 3 different structured prediction tasks.

Further qualitative analysis of remaining error types and optimized prompts is presented. E.g. DeepSeek-R1 produces effective prompts that are shorter than the other models considered.

### Strengths
1. The paper is very clearly written and includes qualitative examples where appropriate.
2. The findings fill-in an important gap in the literature (prompt optimization has mostly been studied int he context of LLMs)

### Weaknesses
I did not find anything lacking in the presentation and content. While the finding is not ground-breaking, the analysis is well done.

### Questions
Suggestion
---
Certain prompt optimization techniques such as GEPA, Mipro, etc seem relevant to discuss in the related work. GEPA may be concurrent with this work so the missing citation is understandable.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
3