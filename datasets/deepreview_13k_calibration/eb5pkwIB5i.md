# Looking Inward: Language Models Can Learn About Themselves by Introspection

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Humans acquire knowledge by observing the external world, but also by \textit{introspection}. Introspection gives a person privileged access to their current state of mind (e.g., thoughts and feelings) that is not accessible to external observers. Can LLMs introspect? 
We define introspection as acquiring knowledge that is not contained in or derived from training data but instead originates from internal states. 
Such a capability could enhance model interpretability. Instead of painstakingly analyzing a model's internal workings, we could simply ask the model about its beliefs, world models, and goals.

More speculatively, an introspective model might self-report on whether it possesses certain internal states—such as subjective feelings or desires—and this could inform us about the moral status of these states. Importantly, such self-reports would not be entirely dictated by the model's training data.

We study introspection by finetuning LLMs to predict properties of their own behavior in hypothetical scenarios.
For example, ``\textit{Given the input $P$, would your output favor the short- or long-term option?}''
If a model \selfpredictionmodel{} can introspect, it should outperform a different model \crosspredictionmodel{} in predicting \selfpredictionmodel{}'s behavior---even if \crosspredictionmodel{} is trained on \selfpredictionmodel{}'s ground-truth behavior.
The idea is that \selfpredictionmodel{} has privileged access to its own behavioral tendencies, and this enables it to predict itself better than \crosspredictionmodel{} (even if \crosspredictionmodel{} is generally stronger).

In experiments with GPT-4, GPT-4o, and Llama-3 models (each finetuned to predict itself), we find that the model \selfpredictionmodel{} outperforms \crosspredictionmodel{} in predicting itself, providing evidence for introspection.
Notably, \selfpredictionmodel{} continues to predict its behavior accurately even after we intentionally modify its ground-truth behavior.  
However, while we successfully elicit introspection on simple tasks, we are unsuccessful on more complex tasks or those requiring out-of-distribution generalization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors investigate whether LLMs can gain insights about their own behavior in ways similar to human introspection, which typically involves accessing their own thoughts and states of mind. In this paper, the authors define “introspection” as “the ability to access facts about themselves that cannot be derived (logically or inductively) from their training data alone.” 

Based on this definition, the authors set up experiments with two models, where one model (M1) is trained to predict its own responses to hypothetical situations, while another model (M2) is trained on M1's behaviors to see if it can match M1’s self-prediction accuracy. The experiments are done on simple toy tasks, such as “What is the second character of your output?” and “Was your response an even or odd number?”. Their experiments show that M1 consistently outperforms M2, suggesting that M1 has "privileged access" to its behavioral tendencies beyond mere training data. However, this did not hold for more complex setups such as guessing the characters’ name in generated stories.

### Strengths
- The paper explores introspection in AI, a relatively underexplored area. By testing a model’s ability to predict its own behavior, the authors contribute to a novel line of inquiry that could have broad implications for model transparency and accountability.
- The authors also run an extensive set of experiments to back up their claim.

### Weaknesses
 - I’m not fully convinced that the current experiment design supports the claims the author is making.
    - The need for fine-tuning to improve a model's accuracy in predicting its own behavior raises questions about whether this is true introspection or just better alignment of the model to the hypothetical task. Specifically, it's unclear if the fine-tuning process is simply optimizing the model to better predict a specific type of output (e.g., the second character of its response) rather than genuinely accessing an internal representation of its own thought process. The fact that a separate model (M2) trained on M1's behavior does not achieve the same level of accuracy could be due to the difficulty of distribution matching, but it could also indicate that M1 is not truly introspecting but rather exploiting a shortcut learned during fine-tuning.
    - The tasks tested in the paper are relatively simple and somewhat random, so it’s unclear whether the results would generalize or if they are merely noise. The authors also find tasks that were not able to see this capability in tasks with similar complexity (e.g., ethical stance prediction & sentiment prediction). If similar results cannot be achieved even after further training, what implications does this give? The lack of a clear pattern of which tasks show this capability and which do not raises concerns about the robustness of the findings. The fact that models succeed on ethical stance prediction but fail on review sentiment prediction, despite both being complex tasks, suggests that the observed introspection might be task-dependent rather than a general capability.
- Please see the questions below.

### Questions
- Inconsistency in the results also strengthens my concerns. For example, why do models succeed on ethical stance prediction, but fail on review sentiment prediction?
- Are there any performance results available for the validation sets? Ideally, both M1 and M2 should exhibit the same performance on the validation data.
- What would the result look like if we make the complex tasks resemble the simpler ones? For example, set the main character’s name to be the next work for a story continuation and prompt the model to guess the first or second letter?
- It would have been much better if the authors included the CoT results. Shouldn’t CoT be dependent on the introspection capability?
- Which task is Figure 6 based on? Did you use 1000 random prompts sampled from all tasks?
- Why are the experiment models not consistent through out the paper? The calibration experiment is done on GPT-4o and Llama-3 70B, whereas the behavioral change experiment is done on GPT-4, GPT-4o, and GPT-3.5.
- What does this imply for mixture-of-experts models?

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
This paper discusses introspection in LLMs.
The claimed contributions include 1) a framework for measuring introspection, 2) evidence for introspection and 3) unveil the limitations in introspective ability.

### Strengths
The experimental setting to justify the claim for introspection in LLM is novel to the best of my knowledge. 
The paper is overall well structured and not hard to follow. 
The experimental set up as well as the models to be fine-tuned and compared are clearly illustrated. 
Introspection in LLM is indeed a relatively new concept for the research in LLMs. Therefore the topic has the potential to contribute to the community.

### Weaknesses
This paper is written in a way that it first introduces the concept of "introspection in LLMs", if I am not mistaken.
However, there are existing literature discussing introspection in LLMs but are not mentioned throughout the paper, e.g. [1,2,3].
Although the first contribution still holds, including the related work of introspection in LLMs might help readers to better understand the contribution of this paper.

Though I agree advantages from introspection, it is still not clear to me where/how it can be employed right now. It would consolidate the contribution of the paper if more examples of use case or applications of introspection are introduced or discussed.

It remains unclear how the specific definition of introspection used in this paper relates to the broader concept as it is used in other machine learning literature. The paper should more clearly distinguish its definition of introspection from other uses of the term, particularly in the context of self-improvement and feedback loops, as this distinction is not clearly made in Section 2 where the term is introduced.

### Questions
1) Is introspection for LLMs first introduced in this paper? if not, why the existing literature are not mentioned?

2) Could you provide some examples of application/ use case of introspection in LLM? i.e., in which cases would users use the model M1?

3) Is it a limitation of the proposed framework, that it only takes hypothetical questions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the ability of LLMs to forms of self-prediction. They propose an evaluation setup for this and provide several experimental evaluations on several current LLMs.

### Strengths
The paper is generally well written and the experimental section showcase an in depth analysis.

### Weaknesses
I have concerns about the conclusions drawn in this work, particularly regarding the handling of “introspection.” Specifically, I am skeptical about the experimental setup and assumptions leading to the authors' conclusion that LLMs exhibit introspective abilities.

The results do not definitively support the notion of "introspection" as traditionally understood in cognitive science, where introspection entails self-awareness and access to one’s own mental states. Instead, the authors describe an experimental setup in which a model trained on its own outputs (M1) outperforms a second model (M2)—fine-tuned on M1’s outputs—in predicting M1’s behavior. This advantage is presented as evidence that the model has "privileged access" to its own behavior, which the authors relate to introspective ability.

However, this outcome can likely be attributed to the specifics of M1’s internal learned representations and operational dynamics rather than introspection. The observed advantage probably reflects M1’s better alignment with internal statistical correlations or patterns in its responses rather than a genuine introspective process akin to self-reflective thinking. In the absence of evidence against this alternative explanation (which I find lacking in the current setup), I consider it incorrect to conclude introspective abilities in any LLM. Therefore, while the results indicate an advantage for M1, interpreting this as introspection overstates the implications, especially as the task lacks the depth typically required to infer cognitive introspection.

In particular, the issues with more complex hypothetical questions (as the authors themselves remark on) indicate this interpretation. Specifically, the model’s limitations with complex questions provide evidence that its self-prediction advantage is bound to specific learned patterns rather than a flexible, introspective ability.

That said, I do recognize valuable insights in this work regarding LLM behavior that could be of interest to the research community. However, I find the conclusions drawn about introspection incorrect and potentially misleading. I recommend reframing the paper to remove conclusions involving “introspection” or “introspective” and replace them with more accurate terms. For example:

    - Self-Alignment: This term suggests the model’s responses align with patterns it has developed internally based on its training, without implying self-awareness.
    - Self-Predictive Consistency: This highlights that the model’s advantage arises from its capacity to predict properties of its responses based on embedded patterns, not metacognitive processes.
    - Behavioral Consistency: This straightforward term underscores the repeatability and stability in the model’s response patterns, which is what the tests measure.

Overall, I am concerned about labeling the behavior showcased here as “introspection,” a term with a well-defined, established literature and test designs from psychology. If the authors wish to call this a form of introspection different from that recognized in psychology, it is risky to attribute similar cognitive abilities based on a single type of evaluation. In light of these concerns, I recommend two changes: first, a reframing or rewording of the paper, which would be a crucial and achievable adjustment. Additionally, further experiments could be designed to challenge the intuition I’ve provided about potential underlying processes; however, I do not have specific suggestions at this time.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to show that Large Language Models have the capability to introspect, challenging the previous observation that these models merely imitate their training data. 
In order to show this, the authors record the behavior of various models across a plethora of tasks as the ground truth, and fine-tune these models on the property-level behavior of a given target model. They then perform self-prediction, where the model is tasked to predict its own behavior, and cross-prediction, where the model is tasked to predict another model's behavior. The experiments show that the models are able to consistently outperform other, stronger models when predicting their own behavior.

In addition, further experiments show that the models calibrate towards their behavior distribution, even in cases where the fine-tuning data does not reflect this distribution. Finally, when fine-tuned on property-level tasks, the models can generalize to novel fine-tuning data, changing their behavior to match that of the fine-tuned model rather than the original one.

Overall, I believe this is a very interesting paper that sheds further light on LLM behavior. However, additional observations as well as analysis are required to cement the correctness of the experiments.

### Strengths
- The idea behind the possible introspection capabilities of Large Language Models is very interesting. However, I would be cautious regarding its framing as a non-data phenomenon as the introspective knowledge can arise from the training process and how the model was penalized with respect to next-token prediction during training for example.
- The paper is very well written, ample with examples and figures to bolster the claims, making it an enjoyable read.
- The experimental process is unbiased and comprehensive enough to showcase the behavior's truthfulness across models.
- The calibration analysis is especially interesting, and shows that significant behavioral distributions can be effectively learned by large language models.

### Weaknesses
 - The definition of introspection (line 110) should be better defined. The fact that a better language model (I presume with respect to evaluation criteria) is not able to infer $F$ might not necessarily mean that $F$ can't be derived at all.  It is crucial to clarify whether the inability to infer $F$ is a limitation of current models or an inherent property of $F$ itself. The current definition leaves room for the possibility that a more sophisticated model or a different training paradigm could indeed infer $F$, thus weakening the claim of introspection.
- When fine-tuning the $M_2$ model, does the training corpora exactly match that of $M_1$? If that is the case, isn't it possible that the prompt is eliciting a self-simulation even through fine-tuning in $M_2$? In other words, $M_2$ is generating answers based on its own behavior rather than those of $M_1$. I believe a further look into this would be valuable. The potential for $M_2$ to learn to mimic $M_1$'s behavior through the fine-tuning process, rather than truly understanding it, needs to be addressed. This could be investigated by varying the fine-tuning data and observing how it affects the cross-prediction accuracy.
- Following the point above, a distinct advantage that $M_1$ has over $M_2$ is its knowledge of the introspection process, while $M_2$ is not provided with the knowledge that it is predicting another model's behavior during the training process. Do you think a significant change will be observed if we provide this knowledge to $M_2$ either through in-context knowledge or via fine-tuning with strings such as "Another model has predicted $X$ on $P$" where $P$ is the question prompt and $X$ is the generated answer? This lack of explicit knowledge about the task could be a confounding factor in the cross-prediction experiments. It's important to determine if providing this information would improve $M_2$'s ability to predict $M_1$'s behavior.
- Although I agree that introspection is a valid explanation, I also disagree with your position in lines 357 to 363 where it is stated that it is not possible for introspection to partially arise from memorization. Can't it be that the fine-tuning process also allows the model to better align the question representation with that of the previously generated response? The argument against memorization needs to be more robust, as the fine-tuning process could enable the model to learn associations between prompts and responses, which could be misinterpreted as introspection. The possibility that the model is simply recalling patterns learned during fine-tuning should be further investigated.
- A further exploration of possible explanations would increase the work's merit. While the current explanation is appreciated, I think it would be good to expand upon this section. The current discussion is somewhat limited, and exploring alternative explanations, such as the model learning to predict statistical patterns in the data rather than engaging in true introspection, would strengthen the paper.
- Consider condensing the figure captions to increase the available space in order to report more results in the paper itself rather than the appendix.

### Questions
- What do you think is the relation between the performance in the introspection task and the overall model performance? For instance, if a much stronger model is tested against a weak model (imagine GPT-4o versus Llama2 7B), can we expect the stronger model to infer the behaviors of the weaker model better than itself?
- How is the "mode" of output distribution is calculated as the baseline? Is this the mode with respect to the entire dataset under a single model?
- Why is it the case that a variant of COT can't improve this task on all levels? For example, prompting the model with something like "First generate the response that you would give to this question, and then choose the second character of your response" and then comparing to the ground truth. In other words, manually triggering the self-simulation.
- I suggest a better articulation for the phrases "property level" and "object level" prompts.

### Soundness
3

### Presentation
4

### Contribution
3
