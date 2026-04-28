# SparsePO: Controlling Preference Alignment of LLMs via Sparse Token Masks

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Preference Optimization (PO) has proven an effective step for aligning language models to human-desired behaviors. Current variants, following the offline Direct Preference Optimization objective, have focused on a strict setting where all tokens are contributing signals of KL divergence and rewards to the loss function. However, human preference is not affected by each word in a sequence equally but is often dependent on specific words or phrases, e.g. existence of toxic terms leads to non-preferred responses. 
Based on this observation, we argue that not all tokens should be weighted equally during PO and propose a flexible objective termed SparsePO, that aims to automatically learn to weight the KL divergence and reward corresponding to each token during PO training. We propose two different variants of weight-masks that can either be derived from the reference model itself or learned on the fly. 
Notably, our method induces sparsity in the learned masks, allowing the model to learn how to best weight reward and KL divergence contributions at the token level, learning an optimal level of mask sparsity.
Extensive experiments on multiple domains, including sentiment control, dialogue, text summarization and text-to-code generation, illustrate that our approach assigns meaningful weights to tokens according to the target task, generates more responses with the desired preference and improves reasoning tasks by up to 2 percentage points  compared to other token- and response-level PO methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes SparsePO, a new approach for Preference Optimization (PO) with a token-level focus. Specifically, SparsePO uses sparse token masks to assign different weights to specific tokens, allowing flexible optimization. SparsePO uses dynamic or model-derived masking strategies.
Quantitative and qualitative experiments on a few varied tasks show that SparsePO works well and provides improvements in some of the cases.

### Strengths
1. The paper is clear and well-written.
2. The method seems novel, has a clear and well-established motivation, and is mathematically rigorous.
3. The paper performs experiments on a varied set of tasks.
4. The sentiment control experiments show good trade-offs between KL divergence and reward. The "Sparsity and Token-level KL divergence" experiment is insightful.
5. Nice improvements on IFEVAL and BBH with H&H training.

### Weaknesses
1. The  TL;DR dataset can be unfaithful and a small set of 120 prompts can hinder results further. Hence I tend to suspect the results. This is a more experimental design problem than a method problem. For faithfulness, AFAIK there are better methods like Q^2, True, GPM, and more.
2. Although the H&H shows some nice results, the size of the model combined with the difficulty of the benchmarks (OpenLLM-2 is designed to be much harder than 1) limit the ability to properly assess the method capabilities. Again this is more on the experimental design side. Running on the version may be better. Also, considering stronger models in the 1B range can also help (See Phi, SmolLM, Qwen2; see this blog reporting small LLMs results on OLLM-V.1 https://huggingface.co/blog/smollm).
3. The results on text-to-code are mixed or even negative raising questions regarding the versatility of the method.



### Questions
1. Although PPO is less used, many recent papers show that it is not inferior to DPO, so is it justified to exclude this from the evaluation?

Comments:
1. There are a few different terminology regarding SparsePO, including method, strategy, objective, and framework. This can be confusing to the reader.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Previous studies have shown that specific tokens play a key role in learning desired behaviors during pre-training and preference optimization, especially in domains where preference depends on certain aspects or subsequences. Consequently, the authors introduce SparsePO, a method for sparse token-level preference optimization. This approach aims to learn sparse masks over token-level rewards and KL divergences during training. SparsePO offers flexibility, does not rely on external models, and can be combined with different masking methods. The authors also analyze the sparsity of induced masks and their relation to KL divergence, and demonstrate quantitative and qualitative improvements when applying SparsePO in various domains with preference indicators.

### Strengths
1. The paper presents a technically sound approach. The motivation for proposing the objective function of SparsePO lies in the classic problem of token contribution allocation in reinforcement learning. The transformation is well-motivated and follows a logical progression.
 2. The use of masks to control the contribution of each token is a valid approach. The two proposed mask computation strategies, MAPO and SPARSEPO, are clearly described and seem feasible. The technical details provided in the methodology section, such as the equations for calculating the masks and the optimal policy, are sufficient to understand the implementation.
 3. In the experiments, the evaluation metrics used are appropriate for the tasks considered (sentiment control, dialogue, summarization, and text-to-code generation). The analysis of the trade-offs between reward and KL divergence, as well as the sparsity of the masks, provides a comprehensive understanding of the behavior of the proposed method.

### Weaknesses
1. Learned sparse masks do not necessarily match human preferences: In the learnable sparse mask, the author only illustrated in the paper how to adjust parameters to ensure the learned mask is sparse. However, it cannot be guaranteed that the crucial tokens are learned correctly. For example, in Figure 9(a), SparsePO-common rewards assigns almost equal rewards to all tokens. This raises concerns about the method's ability to truly identify and emphasize tokens that are semantically important for the desired preference, especially when the reward signal is not perfectly aligned with human judgment. The method's reliance on the preference optimization dataset to model token-level supervision signals might not be sufficient to capture the nuances of human preferences at the token level.
2. Inconsistent performance across metrics: Table 2 shows that SparsePO gains over pass@100 but has a slight decay in the remaining metrics. This indicates that while it may improve one aspect of code generation performance, it may not be uniformly beneficial across all evaluation criteria. The trade-off between different evaluation metrics suggests that the method might be optimizing for a specific aspect of performance, potentially at the expense of others. This raises questions about the general applicability of the method and whether it can consistently improve performance across all relevant metrics.
3. Difficulty in identifying important tokens across domains: In the code domain, especially for code execution, it is challenging to identify which particular tokens are more responsible for a program executing correctly. This is indicated by low mask sparsity levels, suggesting that the method may not be as effective in precisely weighting tokens for code generation as it could be for other domains. The low sparsity in code generation suggests that the method struggles to pinpoint the crucial tokens that determine the correctness of the generated code, which could be due to the complex interdependencies between tokens in code.

### Questions
1. Have you attempted to train the sparse mask using the Gumbel-Softmax function?
2. When the KL constraint is very small, a larger reward value obtained by the model usually implies a higher probability of reward hacking. Can you provide some case studies to illustrate the impact of SparsePO on preventing reward hacking?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Sparse Preference Optimization (SparsePO), a novel approach for controlling large language models' preference alignment through sparse token masks. The authors note that current preference optimization methods (like DPO) treat all token weights equally, whereas human preferences often depend on specific words or phrases. SparsePO introduces flexible weight masks, enabling models to automatically learn weights for KL divergence and rewards during training, thereby improving adaptation to human preferences.

### Strengths
1. SparsePO introduces dynamic token weighting, enhancing model adaptability and generation diversity across different preference criteria.
2. The method is evaluated across multiple datasets.

### Weaknesses
1. The core motivation - that human preferences depend on specific words rather than equally on all tokens - lacks empirical and theoretical validation. The paper does not provide sufficient evidence to support the claim that token-level weighting is inherently superior to uniform weighting for preference alignment. While the intuition is that certain words may carry more weight in determining preference, this needs to be rigorously demonstrated, especially given that current methods implicitly learn complex relationships between tokens and preferences.
2.  The introduction of m(y_t) in Equation 3 does not guarantee optimization equivalence with previous work (Zeng et al., 2024). The paper should clarify the precise conditions under which the proposed method converges to the same solution as existing methods, or explicitly acknowledge the potential for different convergence behavior. The lack of a formal proof of convergence or a detailed analysis of the optimization landscape raises concerns about the reliability of the method.
3.  The learnable sparse mask implementation using a single feed-forward network requires more theoretical justification. The paper does not adequately explain why a single FFN is sufficient to capture the complex relationships between tokens and preferences. Additionally, the method's sensitivity to model architecture and data distribution needs further examination, particularly for implicit alignment tokens. The paper should also explore the potential for overfitting when learning these masks, and how this might impact generalization.
4.  Section 3.3's evaluation focuses on reasoning tasks while omitting crucial assessments of helpfulness and harmlessness metrics, diminishing the significance of minimal performance degradation in reasoning. The paper should include a more comprehensive evaluation that considers a broader range of metrics relevant to real-world applications, including those related to safety and user satisfaction. The lack of these metrics makes it difficult to assess the overall impact of the method.
5.  Section 3.4's summarization task evaluation would benefit from GPT-4-based win rate metrics. The improvements are marginal, with some metrics underperforming existing baselines. The paper needs to demonstrate more substantial and consistent improvements over existing methods to justify the added complexity of the proposed approach. The marginal gains observed may not be worth the additional computational cost.
6.  Section 3.5's experiments suffer from insufficient training data and show inferior performance compared to standard DPO, potentially contradicting the paper's claims. The paper should provide a more robust evaluation with sufficient data to demonstrate the effectiveness of the proposed method, especially in scenarios where it is expected to excel.

### Questions
Please refer to the weakness part.

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
* This paper introduces token-level masking to the token-level DPO objective proposed by Zeng, et. a (2024)l. The motivation is that not all tokens should contribute to KL divergence and Reward computation equally. 
* They conduct experiments on standard tasks for preference optimization: Sentiment Control, Helpfulness & Harmlessness Control, TL;DR summarization, and Text-to-Code generation. 
* They analyze Sparisity level (i.e,. the amount of zero maskings) of the learned masks during training and discuss its implication.
* Their experimental results suggest that DPO remains a strong baseline. The proposed methods are marginally better, if at all than DPO, in terms of final performance or KL-Performance frontier,

### Strengths
* They select a broad set of experiments for investigating PO methods.
* The proposed token-level masking method is a natural extension of previous work on token-leval DPO.

### Weaknesses
 * **Lack of precision in discussing results**. The discussion heavily relies on imprecise statements such as “TDPOv1 exhibits moderate KL divergence”. It is not clear how an PO algorithm could exhibit a certain level of KL divergence. This results in serious issues in clarity as to what the paper tries to argue with its experimental results (See Questions Below).
* **Proposed methods show marginal or no performance gain compared to DPO**. There is little evidence for adopting the proposed methods in terms of performance. For example, in sentiment control, DPO shows the best KL-Reward frontier at low KL (<10). Experiments on Text-to-Code (Table 2) essentially shows DPO remains the most robust PO algorithm. It is difficult to justify the complicated modeling techniques introduced by token-level masking based on their experimental results. 
* **Inadequate experimental setups**. While the paper includes a good range of tasks, some experimental setups are inadequate for investigating PO. For example, Table 1 on Helpfulness & Harmlessness show all PO methods underperforming SFT policy by substantial margin in terms of average scores on Open LLM Leaderboard 2. It is inadequate to argue which PO algorithm is best on the ground that it induces less degradation than SFT compared to other methods. In addition, Helpfulness & Harmfulness and Text-to-Code are investigated with models with <2B parameters. The baseline performance of these small models is poor on these tasks.
* **Advantages from introducing token-level masking are unclear**.  It is not clear from the paper what theoretical/empirical advantages there are for the proposed token-leval masks.



### Questions
> Line 242: “TDPOv1 exhibits moderate KL divergence, which translates into higher reward than DPO and comparable to SimPO.” 
1. It looks to me that DPO attains substantially higher reward at KL <10 in Figure 2 than all other PO methods except MaPO. Could you explain?

2.  Could you explain what “TDPOv1 exhibits moderate KL divergence, which translates into higher reward than DPO ...” mean? Do you mean systems trained with TDPOv1 generally have KL < 20 at the end of TDPOv1 training? 

3. In stating “moderate KL translate into higher reward”, Are you suggesting a causal relationship between KL and reward? I understand KL and reward are two measures of system characteristics which could be correlated, but without causal relation.

> Line 302: “increasingly higher values of β induce higher levels of sparsity on the divergence mask (md), restricting the amount of tokens allowed to diverge in a sequence, which translates to lower token-level KL divergence throughout training.”

4. From Equation (3): high sparsity (i.e., more zero maskings) effectively drops out the KL term, allowing the policy to optimize the advantage function only. It seems like this increases the amount of tokens allowed to diverage in a sequence rather than restricting it. Could you help me understand how mask sparsity interferes with the policy objective? 

> Line 307: “we find that low values of β induce scenarios where reward sparsity is high and divergence sparsity is low, meaning that the loss is dominated by the masked divergence term, δ(x,y1,y2).”

5. Do you mean that the mask is restricting KL divergence at small beta? It seems like the mask is working against beta’s control of regularization. 
6. I am not sure what are the theoretical and emprical advantages of the proposed SPARSEPO methods. Could you provide a clear summary?

### Soundness
2

### Presentation
2

### Contribution
1
