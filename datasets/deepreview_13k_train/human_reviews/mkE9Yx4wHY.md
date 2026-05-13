# Anchored Alignment for Self-Explanations Enhancement

- Decision: Reject
- Scores: 5, 6, 3, 8

## Abstract
In this work, we introduce a methodology for alignment designed to enhance the ability of large language models (LLMs) to articulate their reasoning—\textit{self-explanation}—even in the absence of annotated rationale explanations. Our alignment methodology comprises three key components: explanation quality assessment, self-instruction dataset generation, and model alignment. Additionally, we present a novel technique called \textit{Alignment with Anchor Preference Pairs}, which improves the selection of preference pairs by categorizing model outputs into three groups: consistently correct, consistently incorrect, and variable. By applying tailored strategies to each category, we enhance the effectiveness of Direct Preference Optimization (DPO). Our experimental results demonstrate that this approach significantly improves explanation quality while maintaining accuracy compared to other fine-tuning strategies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new self-explanation alignment method, called Alignment with Anchor Preference Pairs, to improve both exact answer prediction and explanation quality in response to given questions. The main idea is to categorize preference pairs into three types: consistently correct prompts, consistently incorrect prompts, and a mixed category. The authors also propose a new evaluation framework for explanations, measuring five aspects - logical coherence, clarity, relevance, depth of argumentation, and factual accuracy - using other large language models (LLMs). Experiments on four different datasets show that the proposed method outperforms existing self-alignment techniques in generating better explanations, as assessed by the new evaluation framework. Although answer accuracy was somewhat higher than baseline methods, the difference was not statistically significant. The authors further analyze the effect of preference pair category distribution and find that selecting preference pairs from consistently incorrect prompts and the mixed set improves performance over baselines.

### Strengths
The main strength of this paper lies in its introduction of a novel and well-executed modeling of self-explanation alignment. The concept is both sound and straightforward, making it applicable to other QA tasks and LLM models. In terms of clarity, the paper is generally well-written, though certain aspects could benefit from further elaboration.

### Weaknesses
One main concern is the effectiveness of the proposed method in answer accuracy and explanation quality. While M_{Anchor} outperforms M_{Rank}, the differences shown in Table 1 are not statistically significant. Are the reported ± values standard deviations or standard errors? Regarding explanation quality, it would strengthen the paper to validate the new evaluation framework by measuring its correlation with human judgments. Even if LLMs perform similarly to human raters, the reliability of a new evaluation metric needs to be confirmed.

### Questions
- It would be helpful to test the proposed method with one or two more LLMs to demonstrate its robustness and applicability.
- Can the lambda in line 423 be optimized as a hyperparameter? In the current setup, lambda is chosen from the dataset, but controlling lambda as a hyperparameter (by adding a condition after line 18 in Algorithm 1) might improve model performance, especially given Figure 2’s positive correlation between lambda and model performance.
- Why does the performance of M_{Anchor} vary across the four datasets? While lambda partially explains these variations, understanding other influencing factors could reveal ways to further improve performance.
- Are the symbols “s” in lines 113 and 193 referring to the same concept?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a framework for evaluating the quality of self-explanations from language models using criteria like coherence, clarity, and accuracy, with an LLM acting as the judge. It introduces the "Alignment with Anchor Points" method to create reliable preference pairs and uses an alignment strategy that boosts performance while maintaining explanation quality, without needing human annotations.

### Strengths
**S1**. The paper presents a framework for assessing the quality of self-explanations based on various criteria, including logical coherence, clarity, depth of argumentation, and factual accuracy, using an LLM as the evaluator.

**S2**. The authors provide an analysis of the relationship between alignment methods and self-explanation quality, based on their evaluation framework.

**S3**. They introduce the "Alignment with Anchor Points" method to create high-quality preference pairs by grouping them according to the consistency of their accuracy, along with an end-to-end alignment strategy that enhances downstream performance while preserving self-explanation quality, without requiring human rationale annotations.

**S4**. The paper is well-written and easy to read.

### Weaknesses
 **W1**. Although the authors state in Line 69 that their approach differs from faithfulness, they should be more precise when articulating the aim of their approach. The phrase "effectively conveying the model's reasoning" is broad and can be interpreted as faithfulness. A more suitable term might be "improving the plausibility of explanations," as this study aims to replace human-annotated preference pairs with LLM annotations, and the criteria selected resemble those that make explanations plausible to humans. An explicit discussion of where these criteria fit within the distinction between faithfulness and plausibility would be beneficial [1]. Additionally, while this alignment scheme might incidentally improve the faithfulness of explanations, it is not necessarily required to do so. It would be interesting to examine the correlation between each criterion dimension and faithfulness. References [2, 3] could be used for evaluating the faithfulness of explanations.

**W2**. The paper lacks details about the dataset used. A section, either in the main text or the appendix, should briefly summarize the tasks involved.

**W3**. Since the study relies solely on one base model, LLama-3-8B-Instruct, it is unclear if the proposed method's improvements are consistent across different model families or sizes. For example, the marginal improvement may be reduced in larger models.

**W4**. As mentioned in the limitations, using the base model as the judge during the creation of the self-instruct dataset may fail to capture certain nuances as the model evolves. However, the authors did not provide evidence to show whether this is a practical concern. An analysis comparing how often the M_{base}, M_{Anchor} and the evaluation judge agree on evaluation scores would be helpful.

**W5**. The paper lacks an ablation study that uses a different LLM as the judge for evaluation.

**W6**. The method is limited to classification tasks, as mentioned in the limitations section. However, it could potentially be extended to generation tasks using a similar approach, where outputs are grouped based on their similarity to ground-truth answers. Although this may be more complex than for classification tasks, discussing such possibilities could strengthen the paper.

**W7**. Figure 1 should not use radar charts, as they are difficult to interpret and can be misleading. Replacing each radar chart with a bar plot would make the data much easier to interpret.

### Questions
**Q1**. Why does SFT result in a degradation in explanation quality?

**Q2**. In Figure 2, Section 4.2.4, how is $\lambda$ calculated? Is it  the raw number of preference pairs selected under the consistently-incorrect or variable strategies? How do you scale $\lambda$? Does the total dataset size increase as $\lambda$ increases, or is it kept constant? Could the relative improvement be solely due to a decrease in by decrease in M_{Rank} performance?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces Alignment with Anchor Preference Pairs, a method to improve an LLM's reasoning capability when there is no CoT rationale available. The key idea is to employ the LM as both a judge and response generator. By dividing into three cases, the authors empirically show that their method is effective compared to naively constructing the preference dataset based on the judge model's prediction

### Strengths
* For employing LLM-as-a-Judge, the authors use 5 evaluation criteria and include an ablation experiment in Figure 1 to compare which one was effective. This is very insightful.

* The methodology is clear and very intuitive.

### Weaknesses
 * If the main point is exploring how to utilize CoT rationales when they are not available, I think there should also be a upper-bound score, which is curating CoT rationales from a stronger teacher model (for instance, Llama-3.1-70B-Instruct, which was used as the evaluator). Without that, it is hard to tell how effective the method is compared to a strong baseline which is distillation.

* There isn't enough ablation experiments to support the design choices in Section 3.3. For example: 
   * When M_sft consistently produces correct answers, preference pairs are constructed based on the quality of the explanations. What if we remove these instances?
   * When there are a mix of correct and incorrect predictions, the explanations with the highest scores assigned by the judge model is employed. What are the trends like if counterfactually choosing instances where the judge model provides slightly lower scores?

* The evaluation is done with pairwise ranking (O(N^2)), making it computationally expensive to employ in diverse settings.

* The explanation in line 355 - 358 regarding how M_anchor could outperform M_rank lacks insight or details. Could you further elaborate on this?

* The algorithm still requires ground-truth annotations of the datasets (even if it doesn't require a CoT rationale).

### Questions
* In Section 3.2, why did you use the name "Self-Instruction Creation"? Aren't the inputs fixed? Perhaps it should be called "Self-Preference Data Creation" instead?

* I'm not sure how the method differs a lot from the "Self-rewarding LM" paper. Could you elaborate on this?

* Please see the questions in weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a pipeline to generate self-explanation without gold explanations. The process is divided into three main steps: i) explanation evaluation, ii) creating a self-instruct dataset, and iii) aligning the model with Anchor Preference Pairs which are "better" pairs that are refined by categorizing the model's output in three different categories and are then utilized in DPO for model alignment. The main achievement of this research is mitigating the effect of fine-tuning which causes degradation in explanation quality without harming the task accuracy.

### Strengths
- The paper targets a common yet important problem in the field of explanations.
- A comprehensive evaluation of the explanations through the introduced metrics.
- Using LLM as a judge to evaluate self-explanations w.r.t. the given metrics.

### Weaknesses
N/A

### Questions
- How do you choose between two or more explanations with the same score when calling min/max to generate Preference Pairs? My question is regarding line 225.

### Soundness
4

### Presentation
4

### Contribution
3
