# Continual Memorization of Factoids in Large Language Models

- Decision: Reject
- Scores: 5, 8, 3, 5

## Abstract
Large language models (LLMs) can absorb a massive amount of knowledge through pretraining, but pretraining is inefficient for acquiring long-tailed or specialized facts. Therefore, fine-tuning on specialized or new knowledge that reflects changes in the world has become popular, though it risks disrupting the model’s original capabilities. 
We study this fragility in the context of \emph{continual memorization}, where the model is trained on a small set of long-tail factoids (subject-relation-object associations) and must retain these factoids after multiple stages of subsequent training on other datasets.
Continual memorization focuses on the specific challenge of retaining long-tail factoids, whereas general continual learning aims to maintain the LLM’s capabilities across a wide range of generic tasks (e.g., reasoning, commonsense knowledge). 
Through extensive experiments, we show that LLMs suffer from forgetting across a wide range of subsequent tasks, and simple replay techniques do not fully prevent forgetting, especially when the factoid datasets are trained in the later stages.
We posit that there are two ways to alleviate forgetting: 1) protect the memorization process as the model learns the factoids, or 2) reduce interference from training in later stages. 
With this insight, we develop an effective mitigation strategy: \ours{} (\underline{R}andom and G\underline{e}neric Data \underline{Mix}ing).
\ours{}  prevents forgetting by mixing generic data sampled from pretraining corpora or even randomly generated word sequences during each stage, despite being unrelated to the memorized factoids in the first stage.
\ours{} can recover performance from severe forgetting, often outperforming replay-based methods that have access to the factoids from the first stage.
We then analyze how \ours{} alters the learning process and find that successful forgetting prevention is associated with a pattern: the model stores factoids in earlier layers than usual and diversifies the set of layers that store these factoids. 
The efficacy of \ours{} invites further investigation into the underlying dynamics of memorization and forgetting, opening exciting possibilities for future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studied the forgetting issues when finetuning a LLM in multi-stage datasets. They focus the setting of continual memorizing of factoid facts - Stage 1 is factoid fact datasets and Stage 2 finetune with fact/non-fact datasets. The authors find non-fact datasets will cause smaller drop. Based on this intuition, the authors proposed a data mixing strategy (introducing some unrelated datasets) in multi-stage fine-tuning to reduce the forgetting.

### Strengths
The papers present problems and solution pretty clear and easy to follows.
The authors proposed a simple yet effect way to reduce the interference among the different fine-tuning datasets.

### Weaknesses
There are some other method to reduce the interference among the datasets of stage 1 and stage 2.  For example, the method needs to compare with another baseline, i.e. "mixing of Data A and Data B"



### Questions
Table 1, the degradation is more severe for Stage 2 is also a factoid dataset. Do you have any explanation? Also, there is big drop when using GSK8k. It will be very insightful to understand the interplays of the datasets.

For the Replay approach, what if we use a ratio = 1.0?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work focuses on the continual memorization setting in LLMs, a subsetting of continual learning in which a model is first fine-tuned on a factoid dataset, then successively fine-tuned on other datasets (multiple training stages) and must retain knowledge learned during the first stage. The authors first demonstrate that catastrophic forgetting occurs in a 2-stage training process, especially if the dataset from the second stage is a factoid one, and that usual replay methods used in continual learning do not satisfactorily mitigate the issue.

The authors then introduce REMIX, a strategy for preventing forgetting in the multi-stage learning process. In this strategy, additional training data is added to one or both of the training stages. This data takes the form of either generic of random data. The authors show that this new method produces significantly better result than the basic training process on LLaMa-3 and Mistral-7B, which they show to be linked to a more diversified and larger set of layers in which factoids are stored.

Finally, the authors perform a large number of validation experiments, proving that this method is effective with different mixing datasets, and investigate the effect of several other hyperparameters such as the mixing sequence length, the mixing ratio and the number of training stages.

### Strengths
- The paper is very well-written and clear. The section order feels natural, and the reasoning and intuition for each idea are given clearly. The tables and charts summarize the data well, and while informative, the text flows well and is not overly complicated. As a result, this is a very pleasant paper to read. In addition, the references are recent and seem relevant.

- The paper touches upon the issue of catastrophic forgetting of factoids in LLMs, which is a relevant and unsolved issue, especially in the current context where many pre-trained LLMs showcase good reasoning capabilities but cannot easily be updated afterward to store novel world knowledge.

- The paper contains a large number of experiments, that give clear motivation for introducing REMIX, and then show its efficacy over many settings.

- The ideas found in this work are not revolutionary per se (which is not to say that they lack originality; see my next point), but the execution is straightforward and good. The authors carefully checked for important details such as dataset overlap.

- The idea of mixing generic/random data with the training dataset is quite creative and original. Despite being counterintuitive, the authors justify this idea mathematically.

As a result, I recommend this paper for publication with no major point of criticism.

### Weaknesses
Many of the points of criticism I had while reading this paper were answered later on, or in the appendices. The other points that I have mainly consist of questions (see section below).

- In section 4.2, the word "Figure" is used several times instead of "Table".
- Section 3.2 (on replay) is lacking detail in comparison to other sections, especially as it justifies the use of REMIX compared to other replay methods. In particular, I could not find which of the two LLMs was used to measure the effect of replay methods.

### Questions
- The authors show that their method causes the model to store factoids in more layers of the model, which presumably means that the factoids overwrite previous data in these shallower layers. It would have been interesting to investigate whether this results in any significant degradation of other model capabilities (e.g. fluency) compared to the basic two-stage training process. I understand that this paper specifically focuses on factoid memorization and contains many experiments already, but this could be mentioned as future work.

- Another interesting experiment would be to vary either the model or the dataset's size, to evaluate the link between model capacity and the efficacy of REMIX/replay techniques. Do the authors have any insight or early intuition regarding this?

- Have the authors considered/tried combining REMIX with classic replay techniques? This seems like a natural next step to know whether the use of both methods leads to even better results.

### Soundness
4

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
4

### Summary
The paper tackles the issue of continual memorization of factoids in large language models (LLMs), focusing on retaining specific, rare knowledge (factoids) as the model undergoes further training on unrelated datasets. Typical replay techniques fail to prevent forgetting of such factoids in LLMs, leading the authors to propose REMIX, a data-mixing approach that interleaves random or generic data during training stages to reduce forgetting. The paper demonstrates that REMIX helps preserve factoid knowledge across various datasets and training scenarios, with results analyzed using tools like Logit Lens.

### Strengths
Originality: The paper draws attention to the issue of continual memorization of long-tail information through factoid memorization.
Quality: The experiments are conducted rigorously, covering a range of datasets and demonstrating REMIX’s impact across several configurations.
Clarity: Explanations are mostly clear, and the figures help illustrate key points. 
Significance: The method has some practical relevance for fact retention.

### Weaknesses
Unclear Problem Motivation: The paper does not convincingly explain why memorizing long-tail knowledge in the form of factoids is important in practical applications. Without a clear motivation, the relevance of the problem formulation is uncertain, which diminishes the contribution’s significance. If we are only concerned about factoids, why use LLMs in the first place? Why not just use traditional knowledge-based systems? The authors should show how memorizing factoids leads to downstream applications, such as utilizing the information from the factoids on tasks that specifically require LLMs. The paper lacks a clear explanation of how factoid memorization, as opposed to general knowledge retention, benefits specific downstream tasks that leverage the capabilities of LLMs, such as complex reasoning or question answering requiring integration of multiple facts.
Lack of Novelty: REMIX lacks sufficient originality; the idea of mixing generic data into training is not groundbreaking and does not specifically address the unique challenges of factoid memorization. The method appears to be a straightforward application of data mixing, and the paper does not provide sufficient justification for why this particular approach is uniquely suited to the problem of factoid retention compared to other data mixing strategies or more sophisticated continual learning techniques.
Lack of Baselines: The authors only explore experience replay as the baseline approaches, whereas there exists other methods in literature that can mitigate forgetting during continued pretraining (parameter expansion-based methods, regularization methods, etc.) The evaluation is limited by the choice of baselines, failing to compare against other established continual learning methods that address catastrophic forgetting, such as regularization-based approaches or parameter isolation techniques, which could provide a more comprehensive understanding of REMIX's effectiveness.

### Questions
Suggestions
- I would like to suggest the authors the strengthen the motivation of needing to memorize long-tail knowledge through the form of factoids, but showing that it transfers the knowledge itself to downstream NLP tasks that require integrating those long-tail information. Simply getting a high score in the factoid task itself is insufficient to motivate the problem formulation.
- I would suggest that the authors include more baselines from the continual learning literature that can mitigate the forgetting of previously learned knowledge.

### Soundness
3

### Presentation
3

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
This paper examines the problem of forgetting in large language models (LLMs) during continual learning, particularly when training on a small set of long-tail factoids (subject-relation-object triples). The authors identify two primary challenges in retaining these long-tail facts over successive training stages: the limitations of standard replay techniques and the interference from training on unrelated datasets. To address these challenges, the authors propose REMIX (Random and Generic Data Mixing), which combines unrelated, generic data with the factoid data to prevent forgetting. Through comprehensive experiments, REMIX is shown to outperform replay-based methods and recover performance from severe forgetting. The authors further analyze how REMIX influences the learning process, noting that it shifts the storage of factoids to earlier layers and diversifies the layers used for storing these facts, thus reducing interference from later training stages.

### Strengths
Novel Approach to Memory Retention: REMIX introduces a unique approach to mitigate forgetting by mixing random and generic data during training, achieving substantial performance improvement compared to replay-based methods.
Thorough Experimental Analysis: The authors conduct extensive experiments across multiple datasets, providing empirical evidence of REMIX’s effectiveness. They also analyze layer-specific behavior, offering insights into how REMIX modifies the model’s memory dynamics.
Generalizable Insight for Continual Learning: By demonstrating the limitations of replay techniques and proposing alternative strategies, this paper offers valuable insights for both continual memory retention and general continual learning in LLMs.

### Weaknesses
1 Lack of Comparison with Other Forgetting Mitigation Techniques:
Although the authors discuss the limitations of replay-based methods, the paper lacks a systematic comparison with other common forgetting mitigation techniques, such as Elastic Weight Consolidation (EWC) or Knowledge Distillation. For instance, EWC is frequently used in continual learning to reduce interference by regularizing key weights, while Knowledge Distillation selectively retains critical information. Comparing REMIX with these methods would help clarify REMIX’s unique advantages and performance under similar conditions.
2 Synthetic and Specific Dataset Selection:
The datasets used in this paper, such as Key-Value Recall and PopQA, are primarily synthetic and consist of isolated factoids, which may not fully reflect the complexity of real-world data. For example, in practical scenarios, knowledge is often presented in overlapping or nested forms (e.g., “The author of Hamlet is Shakespeare” and “Shakespeare wrote Hamlet”) rather than as isolated facts. Testing REMIX on more commonly used datasets, such as Wikipedia or open-domain QA datasets (e.g., Natural Questions), could provide a more realistic evaluation of its effectiveness and generalizability.
3 Unclear Justification for Types of Data Mixing:
The paper employs both random word sequences and knowledge-rich text (e.g., Knowledge Pile) as mixed data to prevent forgetting, but it does not provide a clear explanation of why these two disparate types would produce similar effects. For example, random word sequences contain no factual content, while Knowledge Pile includes a substantial amount of knowledge and contextual information. The authors could further analyze why both random and knowledge-rich data help prevent forgetting or test the specific impacts of each type in different scenarios.
4 Impact on Performance in New Tasks:
While REMIX performs well in retaining early-stage knowledge, the paper does not explore its impact on subsequent new tasks. For instance, it would be useful to know whether REMIX might limit the model's ability to learn these new tasks when introduced for fine-tuning. Evaluating REMIX’s impact on new tasks could provide insights into potential trade-offs between memory retention and generalization to new tasks.
5 Limited Evaluation on Extended Stages:
The experiments primarily focus on two-stage continual learning, with limited testing of multi-stage scenarios. In real-world applications, models may undergo multiple updates, such as continual fine-tuning in legal or medical domains. Testing REMIX in a three-stage or four-stage setting could provide better insight into its stability and effectiveness over longer training cycles.
6 Resource and Scalability Concerns:
REMIX relies on incorporating additional mixed data during training, which may increase computational costs, especially for large models such as Llama-3-8B. Expanding this method to resource-intensive domains like finance or healthcare could present challenges. If the authors could discuss the trade-offs between added data usage and computational demands or provide a rough estimate of the resources required to implement REMIX in a real-world setting, it would help assess its feasibility and scalability in high-resource environments.

### Questions
1 Comparison with Other Forgetting Mitigation Techniques:
How does REMIX compare with other established forgetting mitigation methods across different tasks? A systematic comparison would strengthen the case for REMIX’s advantages.
2 Exploration of Bidirectional Relational Memory with Atomic Fact Datasets:
The datasets used appear to consist mainly of isolated factoids or "atomic" facts, without directly exploring bidirectional or inverse relational memory. For example, if the model learns that "Bob’s dad is Sam," it would be valuable to evaluate whether the model can infer the inverse relationship, such as "Who is Sam's son?" This type of associative memory is essential for comprehensive fact retention, as it reflects a more integrated understanding of relationships. Could the authors clarify whether such tests were conducted, or suggest if REMIX could potentially extend to this type of bidirectional memorization?
3 Why Forgetting is More Pronounced with Factoid Datasets:
The paper reports that models experience significant forgetting when fine-tuned on factoid datasets in the second stage, but not on non-factoid datasets. Could the authors elaborate on why forgetting is more pronounced with factoids compared to non-factoids, as well as any observed differences in how REMIX performs on these types? This could provide further insight into the underlying mechanisms of forgetting and the strengths of REMIX.
4 Rationale Behind Data Mixing Types:
The paper employs various data sources (e.g., Knowledge Pile, random word sequences) as mixed data in REMIX. However, the choice of these sources appears empirical, lacking theoretical justification or detailed explanation. It remains unclear why certain data sources yield better performance on specific tasks, and this potential variation across tasks is not fully explored. There is no clear guideline for selecting mixed data types, nor an analysis of how different types of mixed data impact task performance. A more thorough theoretical or empirical examination of these differences could enhance understanding of REMIX’s applicability and effectiveness across various contexts.
5 Impact of REMIX on New Task Performance:
The paper focuses on preventing forgetting in prior tasks, but it does not discuss the potential impact of REMIX on performance for new tasks introduced in later stages. While REMIX seems effective at preserving knowledge from earlier stages, it remains unclear whether this approach might inadvertently reduce performance on new tasks due to constraints placed on the model’s capacity or flexibility. An analysis of how REMIX affects the model's performance on new tasks would provide a more balanced understanding of its effectiveness in continual learning contexts.
6 Effectiveness of Random vs. Generic Text Mixing:
The paper explores both random word sequence mixing and generic pretraining text mixing in REMIX. However, it is not entirely clear whether these two approaches yield similar or differing effects on knowledge retention. Could the authors provide more details on any observed differences in effectiveness between random and generic data mixing? Understanding how each type impacts forgetting could offer valuable insights into the dynamics of memory retention in large language models.
7 Combined Mixing Effectiveness:
The results indicate that combining random word sequence mixing with generic data mixing produces the best outcomes, but it is not fully explained why this combination is most effective. Is there a theoretical or empirical rationale for why mixing both types of data provides better retention compared to using either one alone? Additional explanation of this combined effect would enhance understanding of REMIX’s underlying mechanisms and may help guide future applications.
8 100% Accuracy in Table 1:
In Table 1, it is stated that all Stage 1 datasets are trained to 100% accuracy before Stage 2 training. Could the authors clarify how this 100% accuracy is achieved and guaranteed across different datasets? Specifically, were there particular training techniques or criteria used to ensure full memorization of Stage 1 data? Additional details on this process would help in understanding the baseline setup for evaluating forgetting.
9 Suitability Across Task Types:
Has REMIX been tested on other types of tasks, such as generative or dialogue-based tasks? Additional testing on these tasks would clarify REMIX’s versatility and applicability beyond factoid retention.

### Soundness
2

### Presentation
3

### Contribution
2
