- Decision: Accept
- Scores: 6, 8, 6, 6

## Merged Review

### Summary
The reviewers generally find the proposed Scalable Language Model (SLM) method for continual learning to be novel, well-motivated, and empirically strong, with clear presentation. Reviewer 2 (score 8, confidence 4) is notably more positive, highlighting originality, significance, and the elimination of replay/regularization/task-ID requirements. Reviewers 1, 3, and 4 (scores 6, confidence 3, 4, 2 respectively) also acknowledge the contributions but raise several concerns: missing baselines, storage comparisons, computational complexity, lack of clarity about key initialization and inference procedures, and missing analyses (similarity across tasks, zero-shot evaluation, data imbalance in retrieval). All reviewers agree on the method’s effectiveness and the value of its first use of LLaMA2‑7B in this setting.

### Strengths
1. Strong experimental results on diverse backbones and benchmarks, achieving state-of-the-art performance (Reviewers 1, 2, 4).
2. Novel continual learning paradigm that eliminates regularization constraints, data replay, and inference task‑ID via vector space retrieval; does not append parameters to the model, enabling selective knowledge transfer (Reviewers 2, 4).
3. Clear presentation, well‑structured, and detailed mathematical formulation that is easy to follow (Reviewers 2, 3).
4. First application of a large language model (LLaMA2‑7B) to continual learning at scale, advancing the field (Reviewer 4).
5. Method simplicity and no additional overhead (Reviewer 1).
6. Connection to model soup (Wortsman et al., ICML 2022) and meta‑learning linear interpolation (Triantafillou et al., ICML 2021); worth discussing (Reviewer 3).
7. Well‑founded motivation and sound claims (Reviewer 2).
8. Goes beyond single task type, explores diverse domains and task types (Reviewer 2).

### Weaknesses
1. **Method description confusion.** The description is convoluted, making it hard to grasp the benefits fully (Reviewer 1). Several clarifications are missing: (a) Is the preparation phase done collectively for all tasks or sequentially per task? (b) During each task, are keys and low-rank weights updated using task‑specific examples, and are they frozen for new tasks? (c) What is the initial number of keys, and is it dependent on unknown future tasks? (d) How is aggregation across groups achieved when queries and keys are of reduced size? (Reviewer 1 questions)
2. **Missing baseline.** A basic baseline using an average feature extractor as a key and training a single low‑rank weight per task with Top‑1 or Top‑k retrieval is absent (Reviewer 1).
3. **Zero‑shot evaluation.** The advantage of retaining performance on trained tasks is limited; the main benefit is zero‑shot evaluation. Table 6 is unconvincing because the baseline LLAMA already has decent performance. A more robust experiment would involve learning a sequence of tasks and evaluating zero‑shot performance after each new task, e.g., using T0 Held‑in from arXiv:2110.08207 (Reviewer 1).
4. **Storage comparison needed.** The claim that replay‑based methods require additional storage is disputed because the proposed method also saves low‑rank parameters and keys. Text datasets do not require much storage. A storage comparison is needed (Reviewer 3).
5. **Upper bound comparison.** Comparing with an upper bound by assuming ideal similarity (D(p,p_i)=0 for non‑relevant tasks, 1 for current task) would be interesting, though not a strict upper bound due to forward transfer benefits (Reviewer 3).
6. **Triviality of baseline comparisons.** Outperforming replay‑based and regularization methods (e.g., EWC) may be trivial given that the proposed method and task‑ID methods assume additional parameters. Also, the method requires an extra model (sentence‑BERT) (Reviewer 3).
7. **More replay baselines.** Since data replay is not a big issue, additional replay‑based baselines (e.g., online SGD, other replay approaches) should be included (Reviewer 3).
8. **Data imbalance in retrieval.** The number of data points per task should be considered when using weight increments from that task in retrieval. Otherwise, a task with 100 data points has the same importance as one with 10,000. A weighted averaging strategy (like FedAvg in federated learning) could be used (Reviewer 2).
9. **High computational complexity.** Training appears computationally expensive due to per‑instance processing with top‑K vector space retrieval. A comparison of training time versus baselines, along with a breakdown (retrieval, re‑parameterization, backpropagation), is needed (Reviewer 2).
10. **Missing inference algorithm.** An algorithm for the inference phase, detailing retrieval and application of weight increments, should be provided (Reviewer 2).
11. **Unclear initialization.** The initialization of (key, value) pairs for each task is unclear. The mathematical formulation (distributions or techniques) should be specified to enable reproducibility (Reviewer 2).
12. **Similarity analysis and redundancy.** When the pretrained model is frozen and initialized with the same weights, keys of tasks with similar distributions can overlap. An analysis of similarity between (key, value) pairs across tasks is needed. Additionally, if DTKR provides similar pairs from different tasks during inference, is there a mechanism to avoid redundant information? (Reviewer 2 questions)
13. **Typo.** "researchs have" in Section 3.1, Line 1 (Reviewer 2).
14. **Reproducibility concerns.** The method may be harder to reproduce compared to prior methods due to its departure from existing approaches (Reviewer 4).