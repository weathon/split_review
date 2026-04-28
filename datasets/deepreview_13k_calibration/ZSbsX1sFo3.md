# UNA: Unifying Alignments of RLHF/PPO, DPO and KTO by a Generalized Implicit Reward Function

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
An LLM is pretrained on trillions of tokens, but the pretrained LLM may still generate undesired responses. To solve this problem, alignment techniques such as RLHF, DPO and KTO are proposed. However, these alignment techniques have limitations. For example, RLHF requires training the reward model and policy separately, which is complex, time-consuming, memory intensive and unstable during training processes. DPO proposes a mapping between an optimal policy and a reward, greatly simplifying the training process of RLHF. However, it can not take full advantages of a reward model and it is limited to pairwise preference data. 

In this paper, we propose \textbf{UN}ified \textbf{A}lignment (UNA) which unifies RLHF/PPO, DPO and KTO. Firstly, we mathematically prove that given the classical RLHF objective, the optimal policy is induced by a generalize implicit reward function. With this novel mapping between a reward model and an optimal policy, UNA can 1. unify RLHF/PPO, DPO and KTO into a supervised learning of minimizing the difference between an implicit reward and an explicit reward; 2. outperform RLHF/PPO while simplify, stabilize, speed up and reduce memory burden of RL fine-tuning process; 3. accommodate different feedback types including pairwise, binary and scalar feedback. Downstream experiments show UNA outperforms DPO, KTO and RLHF.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the UNA framework, which integrates three prominent alignment techniques for LLMs: RLHF/PPO, DPO, and KTO. The UNA framework seeks to unify these methods by using a generalized implicit reward function to align language model policies through supervised learning. UNA also accommodates diverse feedback types (pairwise, binary, and score-based) and aims to outperform each technique on downstream tasks, simplifying the RLHF fine-tuning process.

### Strengths
1. By combining RLHF, DPO, and KTO, UNA supports a range of feedback types (pairwise, binary, and score-based), which enhances its versatility.
2. UNA replaces RLHF’s unstable, memory-heavy RL process with supervised learning, making the alignment process more straightforward and efficient. 
3. The paper provides a mathematical proof linking the RLHF objective to a generalized implicit reward function.

### Weaknesses
1. Evaluation of the experiments is relatively small-scale. The authors only evaluate UNA over DPO & KTO when fine-tuning with LoRA and evaluate online RLHF using a 1.5B model. It may be difficult to prove whether UNA can take advantage when using large-scale models. I suggest the authors to try larger models like ~8B models since they claim that they use 8 x 80G A100 GPUs. Specifically, the use of a 1.5B parameter model for the online RLHF experiments raises concerns about the generalizability of the findings to larger models, which are more commonly used in practice. The performance of models at this scale can be significantly different, and the observed benefits of UNA might not hold for larger models. Furthermore, the absence of results on larger models makes it difficult to assess the scalability of the proposed method.
2. The improvement of UNA over three baselines are not significant, which is considerate since they are somewhat equivalent. However, I think the authors should show the advantages of UNA, e.g., the time and computational cost, compared to baselines. The lack of a detailed analysis of computational costs and training time is a significant oversight. While the paper claims that UNA simplifies the RLHF fine-tuning process, it does not provide concrete evidence to support this claim. A comparison of training time, GPU memory usage, and overall computational cost between UNA and the baselines (RLHF, DPO, and KTO) is essential to validate the efficiency claims. Without this, it is difficult to assess the practical advantages of UNA.
3. The paper seems written in a rush with several clarity issues. For example, some references (Line 215 and 352) are missing.

### Questions
1. The paper states that $f(x)=0$ when implicit and explicit reward models are exactly the same. However, when we optimize a model using UNA with the simplified implicit reward $f(x)=c=0$, will it guarantee that it will lead to the convergence?
2. DPO also use log pi / pi_ref as an indicator of the reward. However, this implicit reward cannot well reflect the training status. Can the UNA framework better stabilize the training process in the DPO manner?
3. In Table 3, maybe you can try other reference models rather than GPT in Alpaca-eval? The win rates against GPT-4 is to low and difficult to compare among different models.
4. Can you include the results of the original DPO?

### Soundness
2

### Presentation
2

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
This paper provides a unifying framework for value alignment that has:
(i) explicit and implicit reward functions
(ii) can handle different types of preferences (pairwise, binary, score etc.)
and seems to provide better performance than state of the art approaches, RLHF, DPO, KTO.

### Strengths
1. The unified framework does seem to have significant advantages.
2. The paper's ideas are strong.
3. Experimental results are detailed and strong.

### Weaknesses
1. The biggest concern I have is that presentation is extremely poor, with many typos in notation, proofs, text and references. 
2. There are notational inconsistencies in proofs as well.
3. There is no intuitive explanation for why such a unified approach would provide better performance than any of the individual approaches. 

### Questions
1. What is the intuitive explanation for why a unified approach provides better results? DPO provides better results than RLHF as it does direct optimization of preferences, rather than first creating a reward function and then optimizing. In a similar vein, is there an intuitive explanation. 
2. There are errors in the main proof in Appendix B. While I seem to follow the broad outline, I am not entirely sure and would request the authors to provide more explanation and a corrected version. "y" is present on the left hand side, there is a "y" used in expectation. I am not sure how the expectation over "y" makes sense?
3. Are the experimental improvements significant? The improvements are there, but are they significant? How can it be quantified?

### Soundness
3

### Presentation
1

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
This paper presents an algorithm which they call UNified Alignment (UNA), by utilizing a simplified DPO implicit reward. UNA's loss minimizes the difference between the implicit reward and the explicit reward (provided by an existing reward model), hence can be generalized to different modes of feedback: pairwise, binary or scalar. Empirical results are presented to compare UNA with several baselines.

### Strengths
1. There are math derivations for the proposed method.
2. The reward distillation loss is  general for different modes of feedback.

### Weaknesses
The paper is not solid enough for me and the contribution is limited. The reasons are concluded as follow:

First, It is not clear to me why the proposed method differs from DPO, thus the first contribution claimed is not novel at all. In my understanding, the DPO has already proved the equivalent between the optimal policy and the reward model's objective (under the BT model setting). Besides, it is also very confusing why the authors introduce f(x) and c.

Second, for the claimed contribution 2, the author used a objective introduced by DPO model to conduct a supervised learning, which is also confusing. What is the difference between using the proposed method to train an additional model and directly using a well-trained DPO model? And what if the DPO model is not well-trained, then the label would be very noisy? It is a very confusing step and I am open to more discussion.

Third, the proposed method is compared to some baselines and is claimed to be better, however I believe the comparisons are not fair and the experimental results are suspicious.  In Table 1, the authors use 4 UNA variants and only use KTO and Mistral as the baselines, and the best scores in each benchmark are distributed to all 4 variants, so which one is the best? The authors also claim UNA perform better than RLHF while they didn't provide the experimental detail about RLHF. The proposed method is not even a RL algorithm since it doesn't shown any potential in exploration but more like a distillation process, it is meaningless to announce that it perform better than PPO regarding speeds or hardware consuming.

The presentation of the paper needs to be largely improved. There are many compile Errors such as line 215 in the 4th page. Given all these reasons, I will not recommend the paper to be accepted.

### Questions
It seems to me UNA also needs a reward model to learn the policy, which is not too different from RLHF. But in your abstract, "RLHF requires training the reward model and policy separately, which is complex, time-consuming, memory intensive and unstable during training processes." Can you clarify the advantage of UNA compared to standard RLHF? For example, it could be that UNA saves some computation, or converges faster, etc.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method called Unified Alignment (UNA), which aims to unify existing alignment techniques like RLHF, DPO, and KTO. The authors argue that RLHF, though effective, suffers from high complexity and instability, while DPO simplifies the process but is limited in certain aspects, such as not fully leveraging the reward model and being constrained to pairwise preference data. The proposed UNA framework claims to generalize and improve upon these methods by creating a novel mapping between reward models and optimal policies, allowing it to handle different feedback types and improve performance across downstream tasks. The paper suggests that UNA can simplify, stabilize, and speed up fine-tuning processes while reducing memory requirements, and it reports outperforming RLHF, DPO, and KTO in experiments.

### Strengths
It is of interest that the authors try to narrow the gap between the RM-based and RM-free alignment methods.

### Weaknesses
The paper is not solid enough for me and the contribution is limited. The reasons are concluded as follow:

First, It is not clear to me why the proposed method differs from DPO, thus the first contribution claimed is not novel at all. In my understanding, the DPO has already proved the equivalent between the optimal policy and the reward model's objective (under the BT model setting). Besides, it is also very confusing why the authors introduce f(x) and c.

Second, for the claimed contribution 2, the author used a objective introduced by DPO model to conduct a supervised learning, which is also confusing. What is the difference between using the proposed method to train an additional model and directly using a well-trained DPO model? And what if the DPO model is not well-trained, then the label would be very noisy? It is a very confusing step and I am open to more discussion.

Third, the proposed method is compared to some baselines and is claimed to be better, however I believe the comparisons are not fair and the experimental results are suspicious.  In Table 1, the authors use 4 UNA variants and only use KTO and Mistral as the baselines, and the best scores in each benchmark are distributed to all 4 variants, so which one is the best? The authors also claim UNA perform better than RLHF while they didn't provide the experimental detail about RLHF. The proposed method is not even a RL algorithm since it doesn't shown any potential in exploration but more like a distillation process, it is meaningless to announce that it perform better than PPO regarding speeds or hardware consuming.

The presentation of the paper needs to be largely improved. There are many compile Errors such as line 215 in the 4th page. Given all these reasons, I will not recommend the paper to be accepted.

### Questions
Please refer to weakness part.

### Soundness
2

### Presentation
1

### Contribution
2
