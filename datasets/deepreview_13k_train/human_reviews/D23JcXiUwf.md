# Formal Theorem Proving by Rewarding LLMs to Decompose Proofs Hierarchically

- Decision: Reject
- Scores: 8, 8, 3, 3

## Abstract
\noindent Mathematical theorem proving is an important testbed for large language models’ deep and abstract reasoning capability. This paper focuses on improving LLMs’ ability to write proofs in formal languages that permit automated proof verification/evaluation. Most previous results provide human-written lemmas to the theorem prover, which is an arguably oversimplified setting that does not sufficiently test the provers' planning and decomposition capabilities. Instead, we work in a more natural setup where the lemmas that are directly relevant to the theorem are not given to the theorem prover at test time. We design an RL-based training algorithm that encourages the model to decompose a theorem into lemmas, prove the lemmas, and then prove the theorem by using the lemmas. Our reward mechanism is inspired by how mathematicians train themselves: even if a theorem is too challenging to be proved by the current model, a positive reward is still given to the model for any correct and novel lemmas that are proposed and proved in this process. 
		During training, our model proposes and proves lemmas that are not in the training dataset. In fact, these newly-proposed correct lemmas consist of 37.7\% of the training replay buffer when we train on the dataset extracted from Archive of Formal Proofs (AFP). The model trained by our RL algorithm outperforms that trained by supervised finetuning, improving the pass rate from 40.8\% to 45.5\% on AFP test set, and from 36.5\% to 39.5\% on an out-of-distribution test set.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
According to my understanding, this paper has the following two main contributions:

1. **A Setting for Theorem Proving without the Help of Human-Written Lemmas**

- **Contribution**: This paper introduces a new, more challenging evaluation setting in theorem proving, focusing on the use of human-written code libraries but with minimal reliance on human-proven lemmas. 

- **Motivation**: This setting arises from the observation that proofs in human-written projects display strong modularity: proofs are often broken down into lemmas, making final theorems relatively easy to prove by combining these intermediate steps. While efficient, this approach may obscure a prover's ability to handle full-scale proofs of original theorems independently, limiting evaluation of the prover's core capabilities.

- **Method**: To address this, lemmas referenced in the proof of each selected theorem are excluded from the evaluation (however, the authors describe this as removing those "not referred to in the remaining file contents," which seems intended to remove only redundancies). Additionally, the test set is split by dependency—ensuring that no theorem in the test set is refered by any theorem in the training set.

- **Soundness**: Experiments show that the pass rate under the "without lemma proposal" setting is lower than in the "with lemmas  proposal" setting, demonstrating the increased difficulty of this approach.

2. **An Interface for Actively Proposing Lemmas during Proof Generation**

- **Contribution**: This work offers a solution for language models to comply with the above lemma minimalism setting (in my words), enabling models to actively propose lemmas during theorem proving while relying minimally on human-written lemmas.

- **Method**: The theorem proving process is structured as a hierarchical tree search. During proof generation for a specific statement, the model actively proposes lemmas and leverages them in subsequent proof steps, with the proofs of these lemmas deferred to a lower hierarchical level. For model training, reinforcement learning is applied to the supervised-fine-tuned model. By distinguishing between global and local rewards, the model is optimized both to propose provable lemmas that help solve the original theorem and to complete the proofs of proposed lemmas. Special tokens are used to guide the model in deciding when to propose lemmas, effectively controlling exploration.

- **Soundness**: Experimental results indicate that the RL-trained model achieves a higher pass rate than the SFT model, with a 4.7% absolute improvement. Additionally, some proposed lemmas are successfully proved. Experiments over multiple rounds of RL further demonstrate the effectiveness of this approach.

### Strengths
1. While the concept of splitting test sets based on file dependencies has been explored in the LeanDojo project ([arXiv:2306.15626](https://arxiv.org/abs/2306.15626)), the minimalist lemma approach introduced here is novel, with comparative experiments validating its challenges.

2. The RL training framework designed to enhance lemma-proposing capabilities is both innovative and practical. The global and local reward design can be generalized to other tree search tasks. Notably, the use of special tokens to control lemma exploration is an exceptional feature.

### Weaknesses
1. Although the test set split is restricted by file dependencies, the risk of lemma proposal leakage has not been fully addressed. It is possible that some theorems in the training and test sets rely on the same lemmas, which may have been learned during the supervised-finetuning phase. Furthermore, splitting the test set based on file dependencies might introduce bias. These isolated AFP files could be separated precisely because they are experimental or less widely used, which may not accurately represent the average difficulty of the AFP. The challenges observed in dependency-splitting experiments might instead arise from unfamiliar or unseen knowledge and proving skills specific to these isolated files. An alternative approach would be to train and test on an out-of-domain benchmark, such as miniF2F, which has fewer dependencies and reduces the risk of lemma proposal leakage.

2. The comparison between the SFT and RL models, though straightforward, might be insufficient. It seems that the RL model’s advantages arise from additional exploration and feedback on successful lemma proposals during the online training. A more fair comparison might involve comparing the RL model with an SFT model trained with additional expert iterations, where the SFT model also attempts lemma proposals while without the hierarchical reward.

3. The comparison between proving with and without lemma proposals might also be unfair. In lemma proposal mode, the difficulty of proving theorems is deferred to lemma proving, which has more computational resources than direct theorem proving.

4. *Figure 4* demonstrates that extra lemma proposals may not benefit proofs of higher difficulty. Instead of highlighting the hierarchical approach’s advantages for difficult problems, this approach may exacerbate concerns that its benefits stem from unequal computational budgets.

### Questions
1. Regarding *Weakness 4*, the advantages of lemma proposal for more challenging proofs are not immediately clear in *Figure 4*, as the data only presents absolute counts, and the relative advantage is not obvious. Could it be that the relative advantage for proofs with at least 5 steps is indeed more significant?

2. It appears that the tree search depth is limited to 2 or 3. Why have deeper experiments not been conducted? Would increasing the depth help tackle more difficult proofs by allowing finer-grained decomposition, thereby making each lemma more manageable for the model?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel paradigm in neural theorem proving. Previous methods assume pre-provided lemmas during the proving stage. In contrast, this paper encourages the model to decompose the theorem into lemmas, prove the lemmas, and then use these lemmas to prove the theorem. This approach more closely resembles a real-world theorem-proving process. And the effectiveness of the proposed framework is demonstrated by the experiments.

### Strengths
- The motivation for this work is strong, addressing a critical problem in the domain of neural theorem proving. The proposed framework is highly useful for this task.
- The experimental results demonstrate its effectiveness in creating lemmas during the theorem-proving process.
- The paper is well-written and easy to follow.

### Weaknesses
 - The primary concern with the proposed method is its performance. While effective, the enhancement offered by the framework is marginal when compared to the baseline scenario, with a modest 2.1% increase in the AFP test and a negligible 0.1% improvement in the AFP 2023 set.
- One drawback of the lemma proposal mechanism is that the model’s performance can be hindered by meaningless proposed lemmas. This issue is evident in the case study section. The key challenge lies in the ability to refine the proposed method to be able to generate lemmas that are genuinely beneficial.

### Questions
- Why does the performance of `RL w/o lemma proposal` fare worse than `SFT w/o lemma proposal`? Does the RL loop function as an alternative to expert iteration, serving as an advanced version of it? If so, expert iteration has been shown to be effective for neural theorem proving in previous works such as GPT-f and PACT. Why does the current proposed RL loop fail to improve upon these results?
- Why has the miniF2F result been removed in this submission, despite being presented in the previous NeurIPS submission?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces ProD-RL, an RL method to enhance LLM’s theorem-proving capabilities by encouraging them to decompose proofs into lemmas. It avoids oversimplifying the task by removing direct lemma support from the training setup, requiring the model to independently propose intermediate steps in the proof process. The paper evaluates the model’s performance on the Isabelle AFP dataset and shows 45.5%/39.5% accuracy on AFP-test/AFP-2023, which outperforms SFT baselines.

### Strengths
1. This work proposes an RL-driven approach to proof decomposition without lemma reliance, an original contribution that aligns with similar ideas in [3], [4]
2. ProD-RL’s methodology yields improvements over SFT, highlighting the model’s capability to generalize beyond pre-existing lemmas, and trains on a more realistic dataset, splitting by dependency rather than at random.
3. The work contributes to LLM for theorem proving, an important direction for mathematical reasoning research.

### Weaknesses
1. Clarity and Readability: The paper is a little bit difficult to follow, especially in algorithmic explanations and conditional proof notation. The baseline and proposed methods are not clearly differentiated in the results. Improved organization, clearer definitions, and visuals would make the methodology more accessible. Specifically, the description of the RL training loop lacks detail, making it hard to understand how the reward signal is constructed and applied. The conditional proof notation, which is central to the method, is not introduced with sufficient clarity, leaving the reader struggling to grasp the nuances of the proof decomposition process. Furthermore, the results section does not clearly delineate the performance of the baseline SFT model from the ProD-RL model, making it difficult to assess the actual improvement gained by the proposed method.
2.  Generalization and Complexity: There is limited exploration of scalability to higher-complexity proofs. It's better to address whether ProD-RL is viable for deeper proof trees. The paper does not provide any analysis on how the performance of ProD-RL degrades as the depth of the proof tree increases. This is a critical aspect for assessing the practical applicability of the method, as real-world theorem proving often involves complex proofs with multiple levels of sub-goals. The lack of experiments on theorems requiring deeper proof trees leaves a significant gap in understanding the limitations of the proposed approach.
3.  Comparative Benchmarks and Dataset Exclusion: The absence of benchmarks like minif2f in experiments raises questions, given its mention in the license section. Also, there could be more comparisons with other theorem-proving techniques in the experiment section. The paper's failure to include MiniF2F, a standard benchmark for theorem proving, is a significant oversight. This omission makes it difficult to compare the performance of ProD-RL with other state-of-the-art methods. Furthermore, the experimental section lacks a comprehensive comparison with other theorem-proving techniques, limiting the ability to assess the relative strengths and weaknesses of the proposed approach.

### Questions
1. Could the authors address the large experimental difference between ProD-RL (45.5%) and MagnusHammer’s 71% on the PISA benchmark [2]? A direct comparison/discussion of scalability/ablation study could strengthen the work. 

2. Why is “MiniF2F” only in the licensing section without experiment inclusion? This benchmark is a robust test for theorem-proving tasks.
it could be better to add the evaluation PutnamBench [1] which assesses the methods on hard competition level problems.



[1] Tsoukalas, George, et al. "PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition." arXiv preprint arXiv:2407.11214 (2024).
[2] Mikuła, Maciej, et al. "Magnushammer: A transformer-based approach to premise selection." arXiv preprint arXiv:2303.04488 (2023).
[3] Wang, Haiming, et al. "Lego-prover: Neural theorem proving with growing libraries." arXiv preprint arXiv:2310.00656 (2023).
[4] Aygün, Eser, et al. "Proving theorems using incremental learning and hindsight experience replay." International Conference on Machine Learning. PMLR, 2022.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores neural theorem proving in a setting where existing lemmas cannot be used and proposes a RL-based approach that encourages the model to decompose proofs into multiple subgoals and propose new lemmas to prove. The authors demonstrate that their approach, which combines supervised fine-tuning with reinforcement learning, achieves superior performance on the AFP dataset compared to baseline methods, including those that do not propose new lemmas or rely solely on supervised fine-tuning.

### Strengths
* The paper is well-written, clearly structured, and easy to follow.

* The proposed method is well-motivated. Experiments on the AFP dataset effectively demonstrate the advantages of lemma proposal with reinforcement learning.

### Weaknesses
 * The idea of decomposing proofs into subgoals and proposing new lemmas is not entirely novel, as it has been explored in previous work. For instance, LEGO-Prover [1] uses informal proofs to break down proofs into manageable subgoals and leverages language models to either propose new lemmas or retrieve existing ones from a growing library. While the proposed setting of excluding relevant premises is indeed challenging, I believe it does not always reflect practical scenarios. Incorporating both lemma selection and lemma proposal would present a more generalized and realistic approach.

* The experiments are conducted exclusively on the AFP dataset, which may not provide a thorough evaluation of the method's robustness, particularly in out-of-distribution scenarios like the miniF2F dataset, a more commonly used benchmark. As a result, it is unclear how well the proposed approach generalizes beyond the training set. Additionally, in Case 2, there seems to be evidence that the model may be memorizing lemmas from the training data rather than proposing genuinely novel ones, which raises concerns about its ability to generate useful new lemmas in unseen contexts.

* Minor Points: There are some missing references to works that share similar ideas or components with this paper [2,3,4]. For instance, POETRY [4] introduces a recursive approach that decomposes proofs into subgoals and generates lemmas in a hierarchical, level-by-level manner. A broader overview of related work can be found in [5]. Additionally, the statement in Line 80 ("the best method along this line of research requires more than 1k GPU days with A100s to train a model with 600M parameters") may not be entirely accurate. More recent methods, such as InternLM-Step Prover [6], appear to have surpassed HTPS in both efficiency and requiring less computational resources.

### Questions
* Could you evaluate the proposed method on the miniF2F benchmark? This dataset is more commonly used and would help assess the generalization of your approach beyond AFP.

* The paragraph starting at Line 270 suggests that the reward in the RL setting is based on the conditional proof, with its weight influenced by the conditional proof as well. However, in practice (as described in Line 277), it appears that the proposed method uses a language model as a value network to predict True/False, and the probability is used as the reward score, without incorporating any information from the conditional proof. Could you clarify why the conditional proof is discarded for the value function? Additionally, in the RL w/o lemma proposal, what rewards or weights are used in the absence of lemmas?

* Why does RL w/o lemma proposal underperform SFT w/o lemma proposal? For ProD-RL, you first apply SFT, followed by RL, which (almost) ensures that ProD-RL always outperforms ProD-SFT. Does RL w/o lemma proposal also involve an initial SFT stage? If so, it seems that RL w/o lemma proposal negatively impacts performance, and I would like more details on why this happens (since there are no details provided). If not, the comparison between RL w/o lemma proposal and ProD-RL may not be entirely fair.

### Soundness
2

### Presentation
3

### Contribution
1
