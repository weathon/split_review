# 3D-Prover: Diversity Driven Theorem Proving With Determinantal Point Processes

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
A key challenge in automated formal reasoning is the
        intractable search space, which grows exponentially with the depth of the proof.
        This branching is caused by
        the large number of candidate proof tactics which can be applied to a given goal.
        Nonetheless, many of these tactics are semantically similar or lead to an execution error, wasting valuable resources in both cases.
        We address the problem of effectively pruning this search, using only synthetic data generated from
        previous proof attempts.
        We first demonstrate that it is possible to generate semantically aware tactic representations
        which capture the effect on the proving environment, likelihood of success, and execution time.
        We then propose a novel filtering mechanism which leverages these
        representations to select semantically diverse and high quality tactics,
        using Determinantal Point Processes.
        Our approach, \sysname{}, is designed to be general, and to augment any underlying tactic generator.
        We demonstrate the effectiveness of \sysname{} on the miniF2F-valid and miniF2F-test benchmarks by augmenting the ReProver LLM.
        We show that our approach leads to an increase in the overall proof rate, as well as a significant improvement in the tactic success rate, execution time
        and diversity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The search space of proofs grows exponentially with the depth of the proof but a number of branches in this space capture sequences that could be semantically similar or lead to errors. Pruning this search space is, thus, critical. The paper looks at using synthetic data from proof attempts to accomplish this pruning. Semantically-aware tactic representations are generated to capture the effect on proving environment and likelihood of success. DPPs are used to select semantically diverse and high quality tactics using these representations.  The developed approach is called Diversity Driven Determinantal Point Process Prover (3D-Prover). The approach is evaluated on miniF2F-valid and miniF2f-test benchmarks by augmenting reProver LLM.

### Strengths
Many generated proof paths are equivalent modulo variable renaming and other semantics-preserving transformations (such as variable renaming). Authors have found that 75% of the proof paths lead to execution error and thus, it is critical to factor them into exploration. Past work has considered sparse binary signal from the proof status of a goal, intrinsic reward for exploration for new nodes, etc but these do not factor in error likelihood, error messages and execution time. Further, addition of new nodes does not factor in node similarity. 

3D-Prover can augment proof search by filtering candidate tactics to generate diverse and high quality subsets. It is able to filter tactics based on their likely outcome. 

The utility of the transition model representations is demonstrated using ablation study where the transition model Encoder is replaced by an Autoencoder of the same size. Augmenting the ReProver LLM on the standard miniF2F benchmark, the paper reports an improvement in the overall proof success rate.

### Weaknesses
For representing the transitions, the paper adopts a specific architecture - encode the goal and tactics followed by a decoder to get the outcome (next goals or error) and a predictor to determine whether the transition led to an error and the time taken. There is no intuition provided to why this is a better architecture. Why note just have a decoder predict the entire tuple? What other architectures were considered and why is the current one most promising? Even if there is no experimental evaluation of other baseline, it would be good to include discussion based on whatever experimentation was done to select this architecture. 

When splitting the 500K transitions into train and test, how did the authors ensure that it is not the case that the same goal, tactics, next-goal triplet in the test set does not show up in another proof and has been included in the training set. Since the transitions are being collected across several proofs, how is the train/test partitioning ensured to be non-overlapping? 

Could you include not just top-4 but also top-k (k= 1 to 4 or 5) in the Table 1?

### Questions
For representing the transitions, the paper adopts a specific architecture - encode the goal and tactics followed by a decoder to get the outcome (next goals or error) and a predictor to determine whether the transition led to an error and the time taken. There is no intuition provided to why this is a better architecture. Why note just have a decoder predict the entire tuple? What other architectures were considered and why is the current one most promising? Even if there is no experimental evaluation of other baseline, it would be good to include discussion based on whatever experimentation was done to select this architecture. 

When splitting the 500K transitions into train and test, how did the authors ensure that it is not the case that the same goal, tactics, next-goal triplet in the test set does not show up in another proof and has been included in the training set. Since the transitions are being collected across several proofs, how is the train/test partitioning ensured to be non-overlapping? 

Could you include not just top-4 but also top-k (k= 1 to 4 or 5) in the Table 1?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method to address a key issue in automated theorem proving: the vast search space that grows exponentially with proof depth due to numerous potential tactics. To manage this complexity, the authors introduce 3D-Prover, a filtering mechanism for proof tactics that prioritizes diversity and quality using Determinantal Point Processes (DPPs). The method involves two parts:
  - Tactic Representation Learning: The authors generate semantic representations of tactics to predict their impact on the proving environment, likelihood of success, and execution time. This prediction model uses past proof attempts (synthetic data) to form representations of tactics based on their effect rather than mere syntactic similarity.
  - Filtering Mechanism: Using DPPs, 3D-Prover filters the tactic pool, selecting those that are both high quality and semantically diverse. This selection optimizes proof success while minimizing redundant tactic exploration.

This paper augments the ReProver LLM (proposed in an earlier paper) by introducing a tactic filtering mechanism (3D-Prover) at each step of the proof search, whereby the tactic space is reduced. The authors use Best-first Search for proof search where nodes are expanded in order of their cumulative log probability. Specifically, for each tactic state, the ReProver LLM is used to sample 64 candidate tactics. From the 64 tactics, the proposed tactic-filtering mechanism is used to select a subset of K (set at 8, 16 or 32) tactics. A lower value of K indicates a strong filtering and is aimed to cut down the proof search even more. The authors compared their filtering (from 64 tactics to K = 8, 16 or 32 tactics) with two baselines viz., Top-K (selects top K tactics from 64 candidate tactics, based on their log probabilities) and Random (selects K tactics at random from the 64 candidate tactics). 

3D-Prover is tested on the miniF2F-test and miniF2F-valid benchmark, where the basic prover framework is the same as the ReProver LLM, and 3D-Prover is used as a tactic filtering step at each state. The authors claim that filtering tactics results in an increased proof success rates due to reduced execution time, and more diverse tactic sets. The approach demonstrates scalability and effectiveness for deeper, complex proofs, addressing challenges faced by other models like DeepSeek-Prover-V1.5 and contributing to proof success beyond the generator's baseline. The experiments indicate that 3D-Prover outperforms traditional Top-K or Random tactic selection, when 3D-Prover filtering is applied. 

Notably, from Table 2, it is evident that for the Top-K baseline, the pass@1 metric i.e., the number of proofs found by ReProver after one attempt is 22.4%. And by incorporating filtering by 3D-Prover with K=8 (i.e., a stricter tactic filtering), pass@1 increases to 24.4%. However for K=32, the pass@1 metric increases minutely from 27.8% to 28.2% because of tactic filtering. A Random filtering, as expected, performs worse than Top-K baseline or the proposed 3D-Prover filtering. The authors also perform ablation study to demonstrate that the filtered tactics are indeed diverse. 

The authors claim that 3D-Prover's design, which layers a diversity-driven tactic filter atop conventional LLMs, points to a promising direction for automated theorem proving, enabling faster, deeper proofs while controlling for computational resources.

### Strengths
- The paper introduces a novel approach to tactic filtering that emphasizes both diversity and quality. The concepts of transition-aware tactic embeddings and the use of Determinantal Point Processes (DPPs) are innovative in the context of theorem proving, although DPPs themselves are a well-established probabilistic method and not a new contribution of this paper.

- With diversity-driven tactic filtering, the Best-First Search can explore deeper proofs, leading to a faster proof search overall. This is impressive. However, I did not find a comparison of execution times with and without filtering. Table 7 compares execution times with other baselines, but the paper does not clarify the improvement in proof search time specifically due to filtering.

- The tactic filtering method discards a significant portion (87.5%) of sampled tactics from the ReProver LLM for each tactic state, with the proposed 3D-Prover filtering approach outperforming baseline methods like Top-K and Random filtering. By effectively reducing the tactic space, this filtering approach enables more efficient proof searches with fewer resources. While this is a strong result, it would be even more compelling if the paper included a comparison against a no-filtering setup (i.e., considering all 64 tactics).

### Weaknesses
 - The preliminaries and transition models presented in Section 1.2 and 2.1 could have been written in a simplified manner. Some notations are hard to follow and expressed in a circuitous way.

- Why is the decoder taking as input a concatenation of e and g, when e is already an encoded and pooled version of t and g? What is the motive of having g twice?
Also, e is an encoded version. How is concatenating an encoded string to a non-encoded string g, meaningful?

- The authors use metrics like BLEU, ROUGE-L-F1 and top-4 accuracy (proportion of samples which have one beam identical to the ground truth) to evaluate the "Output" in Figure 2. BLEU and ROUGE are similarity metrics. How is checking similarity with the ground-truth "Output" relevant? Because even if the generated "Output" and the ground-truth "Output" are very close according to these similarity scores, they may not be a syntactically and semantically correct next tactic state.

- In lines 408-418, I do not see the quoted values in the referred tables: "∼36% relative improvement (Table 1)" and "∼6–9% relative improvements (Table 7)". It is not clear if these refer to the tables in the respective papers.

- I have concerns about the training dataset used for the Transition Model. Specifically, in lines 220-222, it is mentioned that "We obtain the dataset D from a vanilla ReProver attempt on miniF2F-valid, which results in 498,236 transitions, which we split randomly into 95% training, 5% testing." i.e., 3D-Prover uses a transition model trained from miniF2F-valid transitions. In that case, doesn't that mean that in Table 2, the proof search results for miniF2F-valid, are trained and evaluated on the same dataset? And for this reason, the results for miniF2F-valid in Table 2 are significantly better than those for miniF2F-test? 
Further, the improvement in pass@1 values on the miniF2F-test is not that significant. For K=8, there is a 22.4% to 24.4% i.e. a 2% increase in the number of proofs found. And this improvement goes down to 0.4% (27.8% to 28.2%) for K=32.
Also, the paper does not provide the results without any kind of filtering.

- One of the most concerning weaknesses of this paper is that it does not compare the ReProver (for tactic prediction) + 3D-Prover (for tactic filtering) framework against any state-of-the-art method like DeepSeek-Prover, InternLM-Math, etc. The filtering method is only compared with two baseline tactic filtering mechanisms i.e., Random filtering and top-k filtering. But the paper does not show whether the effect of this filtering is significant enough, such that it outperforms other state-of-the-arts that do not use filtering or use some kind of state-of-the-art filtering.

Although the 3D-Prover introduces a novel design by layering a diversity-driven tactic filter on top of conventional LLMs, the paper falls short in evaluating and demonstrating its superiority over state-of-the-art theorem provers. Additionally, the results show only minimal improvement compared to baseline tactic filtering methods, such as Top-K and Random filtering.

### Questions
Please address the issues raised in the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This paper proposes a method to filter tactics generated by sampling a tree search policy based on diversity in formal theorem proving. To capture tactic diversity, it uses an encoder to embed both the tactic and the goal it is applied to, followed by Determinantal Point Processes (DPP) to select tactics based on these embeddings.
- The encoder used for embedding is trained on two tasks: (a) an auxiliary decoder that applies cross-attention on the embedding to predict the environment’s response after applying the tactic (yielding the next goal if successful, or error messages if unsuccessful); (b) a single-layer MLP that predicts both the success of the tactic and the time required by the Lean prover to verify it. In the final tactic selection step, embeddings are also weighted according to predictions from the MLP regarding tactic success and Lean prover verification time.
- Experimental results show that the tactics selected by 3D-Prover achieve a significantly higher pass rate compared to the baseline.

### Strengths
1. This paper introduces an additional filtering mechanism within language model-based tactic tree search, providing a fresh perspective for research on tree search in theorem proving.
2. Experimental results demonstrate noticeable performance improvements even with a relatively small number of filtered tactics, suggesting that the diversity-based screening method is effective for scenarios with limited computational resources.

### Weaknesses
1. The paper filters tactics only after they have been sampled by a language model, so the computational cost of model sampling remains unchanged. While the paper tries to reduce Lean prover calls with a specialized filtering algorithm, it does not provide a comparative analysis on this aspect. Does 3D-Prover achieve better results than the case that these computational resources were used to apply the Lean prover to all tactics the language model generated?

2. The paper emphasizes balancing quantity and diversity in tactic selection from the sampled tactics. However, given limitations in the language model’s capability, it may not generate tactics diverse enough to meet the problem’s requirements. This suggests that the proposed method may not fundamentally improve the success rate beyond the language model’s own capacity, limiting 3D-Prover’s primary advantage to efficiency (though this, as noted in *Weakness 1*, requires further estimation).

### Questions
Please refer to the first point in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces 3D Prover, a framework that combines a representation learning algorithm to generate semantically aware encodings of proof states and tactics with a filtering algorithm for enhancing semantic diversity in LLM-generated tactics for proof synthesis. The proposed method was tested on top of ReProver, demonstrating its effectiveness. Additionally, ablation studies validate the contribution of each component in the design.

### Strengths
- The proposed algorithm, 3D Prover, is well-motivated and practical. The paper presents an approach to augmenting proof search history using an existing LLM to enhance tactic selection, resulting in more efficient navigation within the search space.
- The semantic-aware representation learning of proof states and tactics is well-established and analyzed. The representations learned from proof history are useful for downstream tasks, including proof synthesis. The experimental design and results demonstrate the impact of each component of the proposed learning framework.
- The proposed filtering framework is straightforward and effective, with results outperforming ReProver without modifying the underlying model. This approach is thus beneficial for advancing proof synthesis in large language models.

### Weaknesses
 - Section 3.1 could benefit from greater clarity. Specifically, the motivation behind using this method could be expanded upon - why was DPP chosen over other sampling algorithms for balancing quality and exploration in this context? It would be beneficial to understand the specific advantages of DPP over alternatives like simple random sampling or more sophisticated methods such as those based on Markov Chain Monte Carlo, especially given the computational cost associated with DPP.
- In the experiments, both $\lambda_s$ and $\lambda_{\tau}$ are set to zero. Additionally, Section A.2’s hyperparameter sweep further suggests that these terms (or at least $\tau_i$) do not significantly contribute to filtering performance. Although this result is not unexpected, it should be explicitly discussed in the experiments section to enhance the clarity of the findings. The lack of impact from these parameters raises questions about their inclusion in the proposed framework, and a discussion of why they were initially considered and why they ultimately did not contribute would be valuable.


### Questions
I wonder what the intuition is for preferring shorter execution time for tactic. Tactic execution time can vary based on factors like the goal state; for example, `linarith` may require different durations depending on the complexity of the arithmetic expressions involved. Moreover, while tactics like `linarith` can take longer for more complex arithmetic, they are often the very effective in reducing the theorem down to its underlying logic.

### Soundness
4

### Presentation
3

### Contribution
3
