# UOE: Unlearning One Expert is Enough for Mixture-of-Experts LLMs

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Recent advancements in large language model (LLM) unlearning have shown remarkable success in removing unwanted data-model influences while preserving the model's utility for legitimate knowledge. However, despite these strides, sparse Mixture-of-Experts (MoE) LLMs--a key subset of the LLM family--have received little attention and remain largely unexplored in the context of unlearning. As MoE LLMs are celebrated for their exceptional performance and highly efficient inference processes, we ask: How can unlearning be performed effectively and efficiently on MoE LLMs? And will traditional unlearning methods be applicable to MoE architectures? Our pilot study shows that the dynamic routing nature of MoE LLMs introduces unique challenges, leading to substantial utility drops when existing unlearning methods are applied. Specifically, unlearning disrupts the router's expert selection, causing significant selection shift from the most unlearning target-related experts to irrelevant ones. As a result, more experts than necessary are affected, leading to excessive forgetting and loss of control over which knowledge is erased. To address this, we propose a novel single-expert unlearning framework, referred to as {\ours}, for MoE LLMs. Through expert attribution, unlearning is concentrated on the most actively engaged expert for the specified knowledge. Concurrently, an anchor loss is applied to the router to stabilize the active state of this targeted expert, ensuring focused and controlled unlearning that preserves model utility. The proposed {\ours} framework is also compatible with various unlearning algorithms. Extensive experiments demonstrate that {\ours} enhances both forget quality up to $5\%$ and model utility by $35\%$ on MoE LLMs across various benchmarks, LLM architectures, while only unlearning $0.06\%$ of the model parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addresses the challenge of unlearning in Mixture-of-Experts (MoE) LLMs. When naively applying traditional unlearning methods to MoE models, the authors discovered that MoE's dynamic routing mechanism leads to unintended expert selection shifts, causing excessive forgetting and reduced model utility. To solve this, they propose UOE (Unlearning on One Expert), a framework that: 1) identifies the most relevant expert for the target knowledge using affinity scores, and 2) implements a router anchor loss to maintain that expert's activation during unlearning. By concentrating unlearning on a single expert, UOE + baseline methods improve both forgetting quality and model utility significantly compared to baseline methods alone.

### Strengths
1. Novel and well-motivated solution that specifically addresses MoE architecture challenges in unlearning, filling an important gap in the literature 
2. Thorough follow-up studies that justify key design choices, particularly: the effectiveness of single-expert versus multi-expert unlearning, and the impact of single/multi-layer selection on forgetting performance. 
3. Strong empirical validation with comprehensive experiments across different: unlearning algorithms, model architectures, benchmarks 4. Resource-efficient approach, requiring modifications to only 0.06% of model parameters while achieving superior performance.

### Weaknesses
1. **Notation Clarity**: Several key mathematical notations (particularly $g(l)$ in the router anchor loss formulation) would benefit from more explicit definitions. The relationship between different mathematical terms could be better explained.
2. **Implementation Details**: Training hyperparameters are insufficiently documented for reproducibility; the $Unlearn()$ subroutine in Algorithm 1 lacks specific implementation details; more comprehensive experimental setup information would facilitate replication.

### Questions
1. The method relies on selecting the expert with the highest affinity score. However, how robust is this approach when there are experts with closely competing scores? 
2. The robustness to attack of the proposed method: if we keep the model frozen and use soft prompt learning, can the soft prompt uncover the knowledge from other experts? If so, this suggests that the knowledge still resides within these experts and can be accessed through carefully crafted input prompts.

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
To address the issue of unlearning disrupting the router's expert selection, the authors propose a novel single-expert unlearning framework that focuses unlearning on the most actively engaged expert for the specified knowledge.

### Strengths
1、The authors present an innovative and parameter-efficient unlearning framework that effectively identifies, targets, and unlearns the expert most relevant to the forget set.
2、The paper provides numerous experiments that convincingly illustrate the motivation behind this work.
3、Extensive experiments demonstrate that UOE improves both the quality of forgetting and model utility in MoE-based large language models across various benchmarks.

### Weaknesses
1、The novelty of this work lacks a compelling impact.

2、The explanation of the router anchor loss is unclear. Specifically, Equation (3) is confusing because it does not define the meaning of g(l).

3、I am unclear about the authors' statement: “we propose the router anchor loss, which encourages the previously identified target expert to remain consistently activated throughout unlearning.” This raises the question of whether the previously identified target expert can reliably be the true target expert. If this cannot be ensured, the process may simply stabilize routing choices, inadvertently activating less relevant experts and undermining the effectiveness of the unlearning process.

4、In Algorithm 1, it is unclear what Ll represents.

5、The authors have not sufficiently emphasized the unique advantages of UOE compared to other MoE frameworks. For instance, while UOE leverages expert attribution to calculate affinity scores for expert selection, other MoE frameworks also compute affinity scores between inputs and experts. Why is UOE more advantageous in this regard? Additionally, when the authors state that "it overlooks finer details that are important for precise comparisons," it would be helpful to clarify what "precise" entails in this context and which additional factors might be considered more significant than precision.

6、In the preliminaries section, the character N denotes the number of experts; however, in Equation (2), it is used to represent the size of the calibration dataset.

7、Sentences such as "Model utility (UT) comparison, at the same level of forget efficacy" in Table 5 and “UT is compared at a consistent level of forget efficacy”in Table 7 are unclear and need clarification. The authors should explain how adjusting model hyperparameters allows one experiment's performance to be maintained while enabling changes in another.

8、Figure 2 illustrates that multiple experts handle a substantial number of tokens, as shown in the long-tail distribution. The decision to unlearn only the top-1 expert requires further justification.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper looks into unlearning (UL) for Mixture-of-Experts LLMs, being a pilot study in this area. It is found that existent UL algorithms suffer from expert selection shifts and thus cannot efficiently eliminate certain knowledge. This paper offers a simple solution that is to unlearn the target expert in a single layer. Experiments support the effectiveness of the method.

### Strengths
- This paper identifies the unique challenge of unlearning MoE LLMs.

- The experiments are thoroughly conducted and ablate well on the design components of UoE such as the number of layers/experts to unlearn and sensitivity to expert ranking.

### Weaknesses
 - My primary concern is that both Qwen1.5 MoE [1] and DeepSeek MoE [2] have shared experts, meaning certain experts are always activated and are not subject to router choices. The paper does not mention how this issue is addressed. I believe these shared experts could retain the knowledge of the forget set. The paper lacks discussion on this point, and additional evidence is needed.

- The unlearning loss objective is unclear, is it a combination of (1) and (3)? What is the hyperparameter applied to the anchor loss, and how sensitive is model performance to this hyperparameter?


### Questions
- What does line 4 in Algorithm 1 mean? Only router parameters in the same selected layer are activated accordingly, or all router parameters?

- Related to what is pointed out in Weakness. The affinity score is only taken from router outputs and thus ignores shared experts. Is there a reason to ignore those shared experts? 

- For other MoE models (for example Mixtral) without such a shared expert setting, how does UoE work?



I believe further clarification is needed on these points, and I am open to adjusting my scores if my concerns are addressed.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigated a critical problem when applying machine unlearning in an MoE scenario. The author gives an insightful demonstration of the current challenge (e.g., Fig 1(a) and Fig 2), making this paper easy to follow. As the authors mentioned, the short-cut behavior when the MoE system is doing expert selection leads to unstable unlearning. To address this issue, the authors proposed an Unlearning One Expert system, which prevents the frequent switching of expert selection and ensures a focused, controlled, and stable unlearning. Although most of this paper is written clearly, I still have concerns about motivation, contribution, and technical quality.

### Strengths
S1. The research problem is well formalized and presented with some demonstration of current research limitation visualization. \
S2. The authors provided a detailed introduction to recent studies on MoE, MU, etc. \
S3. The methodology and most of the experiment parts are well-written.

### Weaknesses
W1. Regarding the motivation for applying MU tech to the MoE system. There could be a wild ground for application, but the technical challenge remains unclear. One key issue is raised due to the golden label of expert selection being decided during MoE system training. It could be more reasonable to directly apply this _decision + MU tech_ when unlearning on the MoE system remains unclear. The 'decision' here refers to the expert selection or weight score in dense routing, which is determined during the initial training of the MoE model. The challenge lies in how to effectively leverage this pre-existing routing decision during the unlearning process. Simply applying standard MU techniques might not be optimal, as the routing mechanism itself could be a source of instability during unlearning.

W2. Like some routing algorithms, the performance improvement result from whether to reduce the uncertainty or routing token to correct expert is unclear.  The author could provide more experimental detail to clarify the contribution of the UOE system. Specifically, it's unclear if the performance gains are due to a reduction in routing uncertainty or if the tokens are simply being routed to the 'correct' experts more consistently. The paper needs to disentangle these two effects through more detailed analysis.

W3. There are many routing algorithms proposed recently. However, UOE seems only to use TopK routing as the backbone. The versatility of UOE framework is not discussed well. It is unclear how UOE would perform with other routing mechanisms, such as those that use dense routing or different forms of sparse routing. The lack of discussion on the adaptability of UOE to various routing strategies limits the general applicability of the proposed method.

### Questions
Major Questions:

Q1. Is the rising **uncertainty** among routing algorithms causing ineffective MoE unlearning? If so, why not directly optimize (or maintain) the entropy?

Q2. As $\lambda$ (hyperparameter for retaining loss, eq.1) aims to directly optimize the strength of retain quality, there is no discussion on this setting. If $\lambda$ is set to $0$, what would happen? 

Q3-1. Is the affinity score unchanged (or as a golden label) during the unlearning progress? 

Q3-2. If the affinity score is the golden target, why not use it as a roadmap but an optimization target? Is it proper to refine the routing strategy during optimization?

Q4. Some case studies on generated unlearning data could be interesting. What will happen in the MoE system?

Minor Questions:

MQ1. In Fig. 3 (a-b), what is the difference between the settings for Routers+Experts, Routers Only, and Experts Only? Why do those settings matter?\
MQ2. Also, in Fig. 3 (a-b), will the deeper layers affect the routing overlap ratio?

### Soundness
2

### Presentation
3

### Contribution
2
