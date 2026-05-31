## Human Reviewer 1

### Summary
This paper presents three significant contributions to the field of multimodal reasoning. First, it introduces VisualPRM400K, a large-scale dataset of approximately 400,000 samples with step-by-step process supervision, created using an automated data pipeline based on Monte Carlo sampling. Second, leveraging this dataset, the authors train VisualPRM, an 8B parameter Process Reward Model (PRM) designed to evaluate each step of a multimodal reasoning chain. Third, to facilitate the evaluation of such critic models, the paper proposes VisualProcessBench, a new human-annotated benchmark for identifying all incorrect steps within a reasoning process. The authors demonstrate that using VisualPRM as a critic in a Best-of-N (BoN) inference setting consistently improves the performance of various Multimodal Large Language Models (MLLMs) across seven reasoning benchmarks, outperforming Outcome Reward Models (ORMs) and Self-Consistency.

### Strengths
1. Significant and High-Quality Data Contribution: The primary strength of this work lies in the creation and release of two valuable resources: the large-scale VisualPRM400K training dataset and the high-quality, human-annotated VisualProcessBench. Constructing such resources is a laborious but crucial endeavor for the community. VisualPRM400K is, to my knowledge, the first large-scale dataset for training multimodal PRMs, and VisualProcessBench provides a much-needed, fine-grained benchmark for evaluating them. These resources will undoubtedly catalyze future research in multimodal reward modeling and reasoning.
2. Thorough and Rigorous Experimentation: The authors have conducted an extensive set of experiments to validate their contributions. They demonstrate the effectiveness of VisualPRM across multiple model families (MiniCPM, Qwen, InternVL) and scales (from 8B to 78B). The ablation studies are comprehensive, comparing PRM with ORM and Self-Consistency, and analyzing the impact of various hyperparameters. The evaluation on VisualProcessBench, which shows that VisualPRM is competitive with powerful proprietary models like Gemini-2.0-Flash, further solidifies the quality of the trained reward model.
3. Well-Written and Clearly Presented: The paper is exceptionally well-organized and clearly written. The motivation, methodology, and results are presented in a logical and easy-to-follow manner, making the paper's contributions accessible and understandable.

### Weaknesses
1. Performance Gains Comparison: The central application of VisualPRM is to improve MLLM reasoning via Best-of-N (BoN) inference. While the reported gains are consistent (e.g., +5.9 points for InternVL2.5-78B), the final performance often falls short of what has been achieved by other contemporary methods that focus on improving the policy model itself through advanced training techniques.
2. In contrast, the approach in this paper is purely an inference-time strategy. While it successfully lifts the performance of existing models, it does not fundamentally enhance the models' intrinsic reasoning capabilities. The resulting performance, while improved, does not appear to push the state-of-the-art boundary as significantly as these training-focused methods.
3. High and Under-discussed Inference Cost: The Best-of-N strategy is notoriously expensive. Using BoN with N=8, as is the default in this paper, multiplies the inference cost (both latency and compute) by at least a factor of 8, plus the overhead of running the VisualPRM critic. This makes the method impractical for many real-world applications. While the authors demonstrate performance scaling up to N=128, they do not provide a thorough discussion on the cost-performance trade-off. A more complete analysis would be necessary to assess the practical viability of this approach. The reported performance gains, while notable, may not be sufficient to justify such a substantial increase in inference cost for many use cases.

### Questions
1. Could you provide a more direct comparison of your final BoN results with other state-of-the-art methods on the same benchmarks? How does the performance of, for example, "InternVL2.5-78B + VisualPRM" compare to models that have been fine-tuned with advanced RL or self-improvement techniques? This would help contextualize the significance of the improvements you've achieved.
2. Could you elaborate on the inference latency and computational cost of using VisualPRM in a BoN setting? For instance, what is the wall-clock time required to evaluate a single instance with N=8 compared to a single pass from the base model? A cost-benefit analysis would be extremely valuable for readers to understand the practical implications of your method.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper introduces VisualPRM400K, a ~400K multimodal process-supervision dataset built via Monte-Carlo (MC) completion to estimate step-wise correctness; an 8B VisualPRM trained on it; and VisualProcessBench, a PRM/MLLM benchmark with 2,866 samples and 26,950 human-annotated step labels. With Best-of-N (BoN) test-time scaling, VisualPRM substantially improves multiple MLLMs (e.g., +8.4 for InternVL2.5-8B; +5.9 for InternVL2.5-78B) and outperforms outcome reward models and self-consistency as the critic.

### Strengths
Timely, practical contribution: A large multimodal process dataset plus a purpose-built benchmark for PRMs addresses a clear gap and enables systematic progress on multimodal TTS. 

Solid empirical evidence: Consistent BoN gains across model scales; clear comparisons vs. ORM and self-consistency; ablations on value- vs advantage-based PRMs and score aggregation. 

Clear PRM formulation: Step-wise discretized targets, single-pass scoring efficiency, and supervising all steps rather than stopping at first error are well motivated and validated.

### Weaknesses
Potential generator-bias in labels: Process rewards are derived from continuations sampled with InternVL-2.5 models. This may bias the PRM toward InternVL-style reasoning and limit transfer to other families (e.g., GPT-5, Qwen-VL). 

MC estimation only: The paper uses MC to estimate expected accuracy per step but does not compare with alternative credit assignment/judging strategies (e.g., MCTS, LLM-as-a-Judge).

Model size choice and scaling law: VisualPRM is fixed at 8B; the paper lacks justification for this size and a scaling curve (e.g., 1B/3B/8B/14B) to reveal accuracy–latency–cost trade-offs.

### Questions
On process reward generation: You estimate step values via MC sampling. Have you tried other strategies such as MCTS rollouts or LLM-as-a-Judge?

On PRM capacity: Why 8B? Have tried other PRM size (e.g., 1B/2B/9B/14B)? 

Related work coverage (multimodal PRMs): The Related Work section focuses primarily on text-only PRMs. It should discuss recent multimodal PRM papers such as DreamPRM [1], AR-MCTS [2].

[1] DreamPRM: Domain-Reweighted Process Reward Model for Multimodal Reasoning (NeurIPS 2025)   
[2] Progressive Multimodal Reasoning via Active Retrieval (ACL 2025)

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper introduces VisualPRM400K, a ~400K-sample multimodal process-supervision dataset with step-wise expected-accuracy labels, and VisualProcessBench, a 2,866-sample benchmark with 26,950 human step-correctness annotations, to enable and evaluate process reward models (PRMs) as critics for Best-of-N test-time scaling in MLLMs. Trained as an 8B PRM that scores each reasoning step in a single forward pass, VisualPRM achieved great improvement across seven multimodal reasoning benchmarks.

### Strengths
1. The paper is generally well-written and easy to follow, with a clear description of the method.
2. The paper provides intuitive visual demonstrations to help better understand the paper.

### Weaknesses
1. Label quality & construction pipeline clarity. The Monte-Carlo step-correctness (`Eq. (2)`) relies on continuations sampled from an unspecified model $M$; this risks systematic bias/noise if $M$ shares failure modes with the policy models later evaluated. In addition, merging solutions to a maximum of 12 steps may distort error localization and the temporal dynamics of “first error vs. downstream errors.” Please quantify label noise (e.g., step-level inter-rater agreement on a subset), report sensitivity to the number of sampled continuations, and analyze the effect of step-merging on PRM accuracy.

2. Fairness of comparisons. Please clarify whether the reported gains in `Tab.2` are measured only against each policy model’s base (“Pass@1”) or also against strong critic baselines. To more comprehensively validate the effectiveness of the proposed approach, include outcome-based reward (ORM) and additional PRM baselines under identical Best-of-N settings (same candidate pool, N, decoding, and compute). Also expand `Tab.3` with more PRM variants and report matched-compute results.

3. Generalization beyond the current suite. Beyond the seven benchmarks used (six math, one multidisciplinary), consider evaluating on more general-purpose multimodal benchmarks and on broader text-only reasoning benchmarks to substantiate cross-domain robustness.

4. Limited technical novelty; strengthen the case for multimodality. The paper’s primary contributions appear to be `VISUALPRM400K` and `VisualProcessBench`, while methodological novelty is modest. To demonstrate that the *multimodal* aspect is indispensable (rather than a text-dominant signal), please add modality ablations and analyses showing performance drops when visual evidence is removed or corrupted. Such results would clarify the unique value of multimodal supervision/assessment relative to single-modal PRMs.

### Questions
See the `Weaknesses` part.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper introduces a new dataset to train multimodal Process Reward Models, a new benchmark to evaluate MM PRMs and an 8B-parameter PRM that consistently, across different model series and sizes, improves performance over MM reasoning benchmarks. The PRM is shown to outperform other TTS algorithms like Outcome Reward Models, Self-Consistency and MLLMs as critic models.

### Strengths
1.	TTS and using PRMs as reward functions in RL are under explored in multimodal modeling. The work here pledges to open source a large 400k sample dataset to train MM-PRMs, a benchmark to evaluate MM-PRMs and a trained MM-PRM. These contributions can be valuable for the community and foster further research.
2.	Effectiveness of PRMs used for TTS in improving MM reasoning across multiple model series and sizes are clearly demonstrated along with improvements compared to other TTS methods.
3.	Design of the PRM benchmark  is sound with the main standouts being, considering all the erroneous reasoning steps as opposed to stopping at the first occurrence, using macro F1 scores to account for class imbalance and multiple math and reasoning datasets.

### Weaknesses
1.	PRMs are well studied in the language modeling space. This work repurposes those studies and algorithms to the multimodal space with limited algorithmic novelty.
2.	An automated Monte Carlo sampling-based pipeline is used to generate the PRM400k dataset. There are no discussions on the quality of this dataset and alignment with human judgement. How the authors ensure incorrect demonstrations are filtered out and how this could affect the trained PRM’s abilities as a critic are not discussed. 10% of the reasoning steps are negative demonstrations. Effect of PRM modeling with more balanced positive and negative demonstrations, using weaker models and models from other series to introduce diverse thinking styles is not explored.
3.	The task categories in VisualProcessBench are mostly centered around math and logic. Extensibility of this methodology for other vision applications like chart, table, GUI reasoning among others will be helpful.
4.	While PRM is shown to outperform other Best-of-N strategies, a discussion about latency and throughput tradeoffs compared to other light-weight strategies can strengthen the claim.

### Questions
1.	Can the authors quantify FP and FN rates for a sub-sample of the VisualPRM400k dataset and explain if they have any filtering steps to identify and remove such demonstrations?
2.	Can the authors provide accuracy-vs-latency plots at multiple N comparing different BoN techniques?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3