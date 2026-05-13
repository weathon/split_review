# No more hard-prompts: SoftSRV prompting for synthetic data generation

- Decision: Reject
- Scores: 5, 6, 5, 5, 3

## Abstract
We present a novel soft prompt based framework, SoftSRV, that leverages a frozen pre-trained large language model (LLM) to generate targeted synthetic text sequences. Given a sample from the target distribution, our proposed framework uses data-driven loss minimization to train a parameterized ``contextual'' soft prompt. This soft prompt is then used to steer the frozen LLM to generate synthetic sequences that are similar to the target distribution. We argue that SoftSRV provides a practical improvement over common hard-prompting approaches that rely on human-curated prompt-templates, which can be idiosyncratic, labor-intensive to craft, and may need to be specialized per domain. We empirically evaluate SoftSRV and hard-prompting baselines by generating synthetic data to fine-tune a small Gemma model on three different domains (coding, math, reasoning). To stress the generality of SoftSRV, we perform these evaluations without any particular specialization of the framework to each domain. We find that SoftSRV significantly improves upon hard-prompting baselines, generating data with superior fine-tuning performance and that better matches the target distribution according to the {\sc mauve} similarity metric.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SoftSRV, a novel framework that uses soft prompts to generate synthetic training data using frozen large language models (LLMs). Rather than relying on manually crafted hard prompts, SoftSRV learns parameterized "contextual" soft prompts through data-driven optimization. The authors evaluate three variants of their approach (SSNSP, SSMPk, SSMC) across different domains (coding, math, reasoning) and show superior performance compared to hard-prompting baselines when using the generated data to fine-tune smaller models.

### Strengths
- Requires minimal human intervention
- Introduces contextual conditioning for better distribution matching
- Outperforms hard-prompting baselines across multiple domains
- Shows better distribution matching (MAUVE scores)
- Supports different soft prompt architectures
- Demonstrates practical alternative to manual prompt engineering

### Weaknesses
1. Domain-Agnostic Parameters: Assumes fixed hyperparameters (prompt length=128, 20K training steps, learning rate=5e-6) work across domains

2. Sufficiency of Context Vector: Assumes the context vector derived from an example sequence captures enough information to generate meaningful variations

3. Small Training Sample Sensitivity: For datasets with small training sets (like MBPP with only 384 examples), more complex SoftSRV variants perform worse than simpler ones, suggesting the approach may be sensitive to training sample size.

4. Task Complexity Impact: The approach appears less effective for more complex tasks like BoolQ that require generating longer passages and more diverse content. The authors note this is "perhaps the most difficult task to generate synthetic data for."

5. No Direct Performance Indicator: The authors note that the MAUVE similarity score they use to measure distribution matching is "not a direct indicator of downstream fine-tuning performance," suggesting a lack of clear metrics to predict effectiveness.

6. Problem Setup Limitations:
- Assumes fixed maximum sequence length m (Section 2, pg 2)
- Restricts to scenarios where input and output sequences have equal length

7. Methodological Concerns:
- Relies heavily on a "lossy" sequence embedder without strong justification
- No clear guidance on how to select the degree of "lossiness"

8. Validation Gaps:
- Initial results focused on only three domains (coding, math, reasoning)
- No clear guidelines for choosing between different variants (SSNSP, SSMPk, SSMC)

9. Heavy reliance on MAUVE score which is acknowledged to not directly indicate downstream performance

10. Comparison Scope:
- Primarily compares against hard-prompting baselines
- Limited comparison with other synthetic data generation approaches
- No comparison with other parameter-efficient tuning methods

### Questions
1. How sensitive is the approach to the quality and diversity of the initial sample data from the target distribution?
2. What is the minimal sample size needed for effective training across different domains?
3. How does the choice of sequence embedder affect performance? 
4. How well does the approach handle very specific or niche domains not well-represented in the LLM's training data?
5. Why choose MLPs for the SSMC variant?
6. How was the number of basis prompts (k=2) chosen for SSMPk? What's the tradeoff between k and performance?
7. How robust is the approach to different random seeds and initialization?
9. How does it compare to other synthetic data generation approaches beyond hard prompting?

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
3

### Summary
This paper suggests an alternative to hand engineering/crafting prompts for designing synthetic data, which is based on soft prompting to learn soft tokens or embedding strategies that minimize NLL on the small amount of human data available, and then generating conditioned on those soft tokens.

### Strengths
This paper addresses a very real problem (the generation of synthetic data) in a novel way.  Their approach is fairly rigorous and the experimental sections contain lots of information; for instance, they report on three variations of their idea (SS_{NSP}, SS_{MPK}, SS_{MC}) and compare performance on a diverse number of metrics (including both downstream task performance after finetuning on the dataset and the human baseline coverage.  

The experiments demonstrate quite convincingly that the approach does better than hand-engineering prompts to generate this synthetic data **when enough human examples are available to tune the prompts**.  Furthermore, it is clear that this is a more "sustainable" approach, as it is not feasible to generate hand-engineered prompts for every domain if you have many domains you are perhaps interested in.

### Weaknesses
I could be wrong, but it seemed to me like they only applied this in domains where it was possible to learn an entire neural network to maximize the likelihood of the "real" data without overfitting, which I imagine is only the case when you have a lot of human data.  To me, this seems like the least likely instance where you'd need to do synthetic generation.  Thus, while I'm convinced the application is real and the empirical results are valid, I would imagine (but would be happy to be proven wrong) that the intersection of problems where you **could** apply this approach and problems where you'd **need** to apply this approach is fairly limited.


Furthermore, I see no novel algorithms or mathematical foundations in this paper.  It is a very straightforward application of an approach developed by Lester et al and Li and Liang, just to this novel task.  And, since, as I pointed out earlier, there may not be many use cases for this task, it may be that the only reason no one has done this yet is that it isn't a very useful thing to do in practice.  However, again, I'd be happy to be proven wrong.

### Questions
What is the minimum amount of human data you need to make this approach not overfit?

How would you generalize this approach to when you only have `k` examples of human data?  (This is asking a bit much, but I'm curious if you've thought about it)
?
Do you see your paper as having novel mathematical contributions, and, if so, what are they?

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
The paper introduces SoftSRV, a prompt-tuning framework designed to synthesize data with frozen LLMs. Unlike standard prefix-tuning prepending a soft prompt to an existing hard prompt, SoftSRV uses only the soft prompt as input context for the LLM. The paper presents three structures of SoftSRV: $SS_{NSP}, SS_{MPk}, SS_{MC}$. The authors then fine-tune SoftSRV on coding, mathematics, and reasoning domains to synthesize data. Experiments show that fine-tuning Gemma-2B on SoftSRV synthesized data outperforms zero-shot synthesized data on those domains.

### Strengths
- The target problem is practical and useful.
- The proposed method is simple and intuitive. 
- Experiments show the promise of the proposed method and the improvements are also very intuitive.

### Weaknesses
 - The method shows limited novelty. It is evident that generating data using a PEFT fine-tuned model on specific domains improves domain alignment, outperforming zero-shot data generation. A model fine-tuned on ~20K samples is naturally better aligned with these domains than zero-shot, which relies on only 0 sample.
- Given this, the approach appears straightforward. Rather than fine-tuning a model for data generation, why not simply PEFT fine-tune the model directly on these tasks? As shown in Table 1, the "train" column demonstrates superior performance compared to the "HP" columns.
- Testing with out-of-distribution (OOD) data instead of MBPP, GSM8K, and BoolQ could further validate the method’s robustness.
- The paper evaluates only one LM; assessing additional LMs could strengthen its claims.
- Current comparisons are unfair. More baselines that incorporate training-based data generation methods are needed.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, authors want to introduce a data synthetic generation method by using a soft-prompt based framework. It aims to train a parameterized soft-prompt by using data-driven loss minimization, and thus synthesize sequences to satisfy the target distribution $D$. Specifically, they found that the parameterized families of soft prompt can be conditioned on an input context and can fit the target distribution. Experimental results indicate that the proposed method can improve the fine-tuned model to achieve better performance based on the synthetic data.

### Strengths
**Strengths**

1. This paper introduces how to train soft prompts to build a data synthetic generation to fit target distribution.
2. Experimental results demonstrate the effectiveness of the proposed method can fit the target distribution.

### Weaknesses
 **Weaknesses**

1. To build such a data synthetic generation, the proposed method first needs to obtain a lot of samples from the target distributions to train the soft prompt. So, which is advantage to use the proposed method as directly use hard prompt does not require any target samples for training? Specifically, the method requires a substantial amount of data from the target distribution to effectively train the soft prompt, which seems to negate the advantage of synthetic data generation, as one might as well use the original data directly for fine-tuning. The necessity of having a large dataset to train the soft prompt raises questions about the practical applicability of this method in low-resource scenarios.
2. The generalization of the proposed method is also a concern. It seems if we want to use a different LLM (e.g., LLama-70B) for data generation, we also need to train a corresponding model. Therefore, the proposed method (i.e., the trained soft prompt) cannot be adapted to different LLMs, while hard prompt does not have such a concern. The soft prompt is intrinsically tied to the specific architecture and parameters of the LLM it was trained on. This lack of transferability significantly limits the method's versatility and necessitates retraining for each new LLM, which is computationally expensive and time-consuming. This is a major drawback compared to hard prompts, which can be more easily adapted across different models.
3. Experiments on more LLMs are required. In this paper, authors only use Gemma-2B as a backbone network. The evaluation of the proposed method is limited to a single LLM, Gemma-2B. This raises concerns about the generalizability of the findings to other LLMs with different architectures and parameter sizes. It is crucial to validate the method's effectiveness on a broader range of models to ensure its robustness and practical relevance.
4. In authors' setting, training SoftSRV also require some training (e.g., 20K steps). So what happened if our downstream tasks do not have enough data for training? The requirement of 20K training steps for SoftSRV poses a challenge, particularly in scenarios where downstream tasks have limited data. This raises questions about the method's applicability in low-data regimes, where the training of the soft prompt might be unstable or ineffective.
5. In this paper, authors only choose three standard datasets (i.e., Code, Math and Reasoning) for generation. Do you try some other open-domain scenarios, like some datasets which are not in question-answer format (e.g., Chat)? The evaluation is limited to question-answer formatted datasets, which does not fully demonstrate the method's capability in more diverse and open-ended scenarios. Exploring the method's performance on datasets with different formats, such as chat or text generation, would be crucial to assess its broader applicability.

### Questions
Please see my comments on Weaknesses. I am willing to increase my score if authors can address my concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes SoftSRV, which trains and adapts soft prompt in synthetic data generation, while previous works mainly generate pseudo data by manually hard prompts. Empirical results on diverse tasks show that the models trained by SoftSRV-generated data performs better than those trained on data generated by baseline hard-prompting approaches. Besides, softSRV always generates data with better matches the target distribution.

### Strengths
* This paper well written and the analysis of distribution matching is clear.
* The experimental results compared with hard prompt baselines are promising.

### Weaknesses
 * SoftSRV is only applied on synthetic data generation, actually the application can be more diverse and broader. What about the performance on some specific downstream tasks if we can train soft prompts on these tasks? Will it perform better than other soft prompts like Prefix-tuning[1], RLPrompt[2], P-tuning[3,4]? 
* The paper mentioned SoftSRV is different from previous soft prompt methods, rather than prepending parameters, it instead uses the soft prompt alone as input context to the LLM. But it does not give some comparisons between SoftRSV and these soft prompt methods. What if those soft prompt methods be used in synthetic data generation? 
* To some extent, this paper only adapts soft prompts in pseudo data generation, rather than propose a brand new, novel method. The contribution might not meet the level of substantial novelty expected at a conference like ICLR. So if SoftSRV performs better than other soft prompt baselines on other downstream tasks instead of only data generation, I'll consider increasing my score. 

### Questions
* What about the performance on some specific downstream tasks of SoftSRV compared with other soft prompt methods?
* This paper only compares SoftSRV with hard prompt baselines on synthetic data generation. More comparisons with previous soft prompt methods applied in this data generation area are necessary.

### Soundness
2

### Presentation
3

### Contribution
2
