- Decision: Accept
- Scores: 8, 5, 5, 6

## Merged Review

### Summary
The paper proposes OpenPRM, a method to construct sentence-level process reward data for open-domain instruction-following tasks. It uses an existing outcome-based reward model (ORM) to evaluate sampled trajectories, merges trajectories with similar prefixes (by edit distance) into a tree, and backpropagates outcome-level rewards to obtain weak process supervision. The resulting PRM is trained jointly with the ORM under pairwise ranking objectives. Experiments on RewardBench and other benchmarks show improved performance over ORMs and specialized PRMs, and inference-time scaling experiments (Best-of-N, beam search) suggest better scalability than ORMs.

### Strengths
- The paper addresses a significant gap by extending PRMs from specialized domains (math, coding) to open-domain instruction-following, and provides an open-accessible dataset and model, which is valuable for the RLHF community (Reviewers 1, 2, 3).
- The preference tree construction using existing ORMs is a creative and cost-effective solution for generating process-level supervision without manual annotation (Reviewers 1, 3).
- The inference-time scaling experiments (Best-of-N, beam search) are valuable, especially given the growing importance of inference-time compute (Reviewer 2, 3).
- The paper provides a detailed analysis of ORM limitations, particularly cumulative error, and shows how OpenPRM mitigates this by identifying key divergent steps. It also addresses concerns like length bias and process aggregation rationality (Reviewer 3).
- The writing is clear and the methodology is easy to follow (Reviewer 4). Some reviewers find the presentation lacking details (Reviewers 2, 3) – this is noted as a weakness below.

### Weaknesses
- **Novelty and prior work**: The approach is similar to prior MCTS-based methods (Math-Shepherd, OmegaPRM). One reviewer considers the novelty limited and the contribution an incremental improvement (Reviewer 4). Another notes that novelty is missing but not a major concern given the value to the community (Reviewer 1). A third points out that the key innovation (merging solutions into a tree based on step similarity) is not thoroughly discussed (Reviewer 3). The rebuttal experiments showed MCTS remains a strong baseline; the authors claim 10x efficiency over MCTS but both methods process 3.84M examples in 24 hours, which appears contradictory (Reviewer 4).
- **Missing details on tree building**:
  - How data merging works is not fully described; e.g., the edit distance threshold (stated as 0.88) and why it was chosen are not explained, nor is its impact on data quality and results ablated (Reviewers 2, 3).
  - Steps are separated by “.\n”, and sampling temperature is 0.5. It is unclear why this temperature was chosen; typical practice uses higher temperatures for diversity. The low temperature may limit solution diversity needed for accurate reward calculation (Reviewer 3).
  - Only one example is given in the appendix, and it is not clear. Reviewers would like a concrete example showing original solutions and the resulting tree (Reviewer 3).
- **Missing details on PRM training and inference**:
  - How the process supervision data is formatted into training examples and what loss function is used is not clearly stated (Reviewers 2, 3). The paper mentions MSE loss for ORM training; one reviewer notes that training a reward model with MSE loss for probability labels is inappropriate (this is not a regression problem) (Reviewer 2).
  - At inference, how step-level rewards are predicted and aggregated into a final reward is not described (Reviewer 3).
  - Table 2 does not specify the metric (e.g., per-step accuracy?) and how PRMs are evaluated on RewardBench (which is typically for ORMs) – this needs clarification (Reviewer 2).
  - Table 3 lacks results from the outcome reward model; reviewers request inclusion to allow direct comparison (Reviewer 4).
- **Performance analysis gaps**: OpenPRM consistently underperforms on the Chat subset of RewardBench; no analysis explains this discrepancy (Reviewer 1). Figure 3 (Best-of-N scaling) has overlapping lines making it hard to interpret, and no analysis for PBM (Process-Based Model) scaling is provided (Reviewer 1).
- **Baseline comparisons**: The improved outcome-level reward performance may simply come from better training data (UltraFeedback, HS2, added math/coding data) rather than the method itself. A baseline with the same data but only outcome-level supervision would isolate the method’s impact (Reviewer 1). For Table 2, it is unclear how comparisons across different backbones and training data are “apple-to-apple” (Reviewer 4).
- **Potential errors in related work review**: The statement that reward models are trained with MSE loss is incorrect (step-level probability is not a regression target). The Step-DPO paper did not train a reward model (Reviewer 2).
- **Compute efficiency claim**: The paper motivates the method by saving compute for process label generation, but the sampling cost appears the same regardless of the labeling method; this requires clarification (Reviewer 2).
- **Missing evaluation**: The authors might consider evaluating on the OffsetBias dataset for a more fine-grained assessment of model bias (Reviewer 1).