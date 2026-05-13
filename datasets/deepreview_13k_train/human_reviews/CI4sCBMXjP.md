# ELICIT: LLM Augmentation Via External In-context Capability

- Decision: Accept
- Scores: 8, 8, 3, 8

## Abstract
Enhancing the adaptive capabilities of large language models is a critical pursuit in both research and application.
    Traditional fine-tuning methods require substantial data and computational resources, especially for enhancing specific capabilities, while in-context learning is limited by the need for appropriate demonstrations and efficient token usage.
    Inspired by the expression of in-context learned capabilities through task vectors and the concept of modularization, we propose \alg, a framework consisting of two modules designed to effectively store and reuse task vectors to elicit the diverse  capabilities of models without additional training or inference tokens.
    Our comprehensive experiments and analysis demonstrate that our pipeline is highly transferable across different input formats, tasks, and model architectures.
    \alg serves as a plug-and-play performance booster to enable adaptive elicitation of model capabilities.
    By externally storing and reusing vectors that represent in-context learned capabilities, \alg not only demonstrates the potential to operate modular capabilities but also significantly enhances the performance, versatility, adaptability, and scalability of large language models.
    \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes ELICIT, a framework that stores the task vectors corresponding to different in-context-learning (ICL) prompts and dynamically augments the given question with retrieved task vectors to provide ICL abilities without explicitly forwarding the long ICL prompts. ELICIT shows comparable or better performance than ICL baselines on diverse tasks while being significantly more efficient.

### Strengths
1. The writing is clear and easy to follow. The motivation and design of each component is straightforward to understand.
2. Dynamically augmenting task vectors is significantly more efficient than in-context learning while showing competitive or even better performance.
3. The proposed approach can be applied to existing LLMs in a plug-and-play manner, making ELICIT easy to deploy.

### Weaknesses
1. Some details regarding the experiment setup need to be included. For example, the paper does not describe how the ICL prompts $p_i^{t}$ are chosen.


### Questions
1. How are the ICL prompt $p_i^{t}$ chosen? (e.g., Are they a group of randomly selected examples?) If there is a technique to maximize the diversity of the prompts in a given library, would it also boost the model performance?
2. Figure 5 shows that ELICIT boosts performance on relevant tasks while minimally compromising performance on non-related tasks. Is this because task vectors are not applied for unrelated tasks, or does the model perform well even when unrelated task vectors are given?
3. The current framework augments (at most) a single task vector at a single layer. Could this be extended to multiple vectors or layers to improve performance? (e.g., in cases where a given query is highly relevant to two different task vectors)
4. Tables 2 and 3 show that ELICIT performs significantly better than the ICL baselines for Pythia and Mamba. What would be the reason for this? For example, can ELICIT be more beneficial for models with weaker capabilities? Or could this be related to a specific training recipe, as Pythia and Mamba are trained under the same setup?

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
3

### Summary
This paper proposes ELICIT. It's a framework aims at improving LLMs capabilities by introducing an external ICL capacity library. This library stores task vectors, which represent in-context learned abilities, enabling models to retrieve relevant skills dynamically without additional training tokens or fine-tuning. The approach allows LLMs to handle diverse tasks by selectively activating specific capabilities when needed, thus improving both versatility and computational efficiency.

### Strengths
1. The paper comes up with an interesting and intuitive solution to improve LLMs' abilities using the task vectors.
2. Extensive experiments over various models and tasks.
3. Exprimental results show great advantage of the method over others.
4. This novel plug-and-play framework could benefit other methods on the same task.

### Weaknesses
1. I would expect the proposed ELICIT method to be integrated into more existing strategies such as few-shot learning.
2. Have you tried using the capacity bank with other creation method other than ICL?

### Questions
See weakness above

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
The article introduces ELICIT, a novel framework to enhance the adaptive capabilities of large language models (LLMs) without the need for extensive fine-tuning or in-context learning demonstrations. ELICIT consists of two key modules: a capability library that stores task vectors representing various in-context learned capabilities, and a dynamic retrieval module that selectively activates these vectors based on input queries. Experimental results demonstrate the effectiveness of the model.

### Strengths
1. The new framework with the use of task vector demonstrates effectiveness in improving zero-shot performance.
2. The paper is generally well written and easy for readers to understand.

### Weaknesses
1. The novelty is limited in some aspects, including the use of task vector and the retrieval module. 
2. Experiments on different models of different sizes should be conducted as the study would better demonstrate that this method is also effective for large models.
3. More comprehensive experiments on more datasets are expected, such as MMLU, GSM8K, HumanEval, etc.

### Questions
1. Why isn't the experiment conducted on instruction-tuned models but base models?
2. Did you compute the decrease in inference efficiency caused by the introduction of a new module?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces ELICIT, a novel framework for adapting Large Language Models (LLMs) to diverse tasks, using task vectors and in-context learning (ICL). Inspired by the concept of modularization, ELICIT comprises two core components—Build Capability Library and Dynamic Capability Elicitation. By building a library of task vectors, each representing one in-context capability, ELICIT dynamically leverages this library to selectively retrieve and activate capabilities based on any given query, ensuring efficient and flexible elicitation of the model’s capabilities. 

To build the capability library, task vectors are stored across layers for each task, along with prompts for future reuse, and the position of the optimal layer, which is determined based on the hold-out validation set and zero-shot inferences with task vector interventions to the model. Interventions within the model can be as direct replacement or a linear combination, with the latter shown to perform better. Later, task vectors are retrieved with the Dynamic Capability Elicitation module that employs a SimCSE RoBERTa model for relevant task vector selection and a threshold-based filtering approach based on AUC scores from the validation set.

ELICIT shows good performance across 20 ICL tasks and four models, outperforming other baselines across tasks, models and query formats, while also showing good generalization on unseen tasks.

### Strengths
- **S1:** Paper explores a novel and promising direction for in-context learning by leveraging task vectors with an external modular concept which is really interesting and aligns well with the recent work in the field of in-context learning and task-vectors.
- **S2:** Proposed method ELICIT demonstrates strong performance and generalization across diverse tasks and models.
- **S3:** This paper has a clear mathematical presentation with good explanations of ICL and task vectors.

### Weaknesses
 - **W1:** The paper lacks specifics on dataset curation regarding the train-val-test splits and sizes, as well as the sample sizes used to calculate the performance. Can you please clarify how many examples were used for the task calculation? 
- **W2:** ELICIT selects the optimal layer for task vectors for each given task and prompt, but assuming that the whole task encoding is stored just within a single layer may not be optimal. Have the authors tested multi-layer interventions, and if so, how did they compare? Moreover, could grouping and averaging task vectors per task simplify optimization steps and yield efficient task vector retrieval without extra steps?
- **W3:** The paper does not compare with previous task vector approaches mentioned in the related work (Hendel et al., Todd et al., Liu et al., Yan et al.), as well as with other parameter-efficient fine-tuning methods based on modularity (also mentioned in the related work like Hu et al.) with 16 shots. I believe such comparisons should be performed and included in the paper. Additionally, the paper does not mention task vector work for visual ICL and multi-modal ICL [1, 2] and including these would provide a comprehensive context and overview of the field. 
- **W4:** Figure 3 illustrates the trade-off between stronger interventions and language modeling performance on WikiText, which is an expected observation since ICL and general language modeling operate with different circuits [3, 4, 5]. Having stronger interventions steers the activations further from the pretrained task, thus resulting in the worse performance, which is what previous works also showed. Authors do not analyze or explain this observation, but just comment how the strength of interventions affects the ICL and language modeling performances. I believe further discussion and explanation should be included.
- **W5:** The proposed method relies heavily on validation data to select optimal hyperparameters and determine the filtering threshold. And the similarity-based model for task vector retrieval is further trained. Does relying on the validation tuning affects the scalability and efficiency? Can you please explain how this similarity model was trained, and with what data?
- **W6:** Tables 1 and 2 contain additional bolded entries, and captions are not descriptive enough, missing information about the sample size for the BM25 and evaluation in general. Further, figure 6 does not have a clear explanation of components labeled a, b, and c, while also missing a description in general. Finally, there is a typo in the appendix in the title for the Similarity based retrieval methods.

### Questions
While the paper presents an interesting direction within ICL with modular task vectors and shows better performance than zero-shot and classical ICL, further improvement of clarity, related work comparison, and validation dependency could strengthen the paper even more. I would recommend acceptance if the authors address these points and the questions within the weakness section and the following one:
- Have you tried aggregating task vectors by task, and if so, what were the results?
- Have you considered using multiple layers to represent task vectors instead of relying on a single optimal layer? If yes, how did this affect performance?
- Can you please clarify if only the most similar task vector is used for intervention in the end? If so, does this mean many task vectors remain unused?
- Can you include comparisons to related task vector approaches from previous ICL research you mentioned in the related work? Can you also compare your method against PEFT modular methods with a few-shot regime?
- How well does your approach scale to larger LLMs?
- Can ELICIT be extended for multi-modal applications or other, more complex tasks?
- Does ELICIT support compositionality, such that combining different task vectors can represent new tasks?

### Soundness
3

### Presentation
3

### Contribution
3
