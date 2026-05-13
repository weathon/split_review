# Teaching LLMs to Decode Activations Into Natural Language

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Interpretability methods seek to understand language model representations, yet the outputs of most such methods---circuits, vectors, scalars---are uninterpretable, requiring further effort to interpret. In contrast, we propose to study LatentQA, the task of answering open-ended questions about model activations in natural language. Towards solving LatentQA, we propose Latent Interpretation Tuning (LIT), which finetunes a decoder LLM on a dataset of activations and associated question-answer pairs, similar to how visual instruction tuning trains on question-answer pairs associated with images. We use the decoder for diverse reading applications, such as extracting relational knowledge from representations or uncovering system prompts governing model behavior. Our decoder also specifies a differentiable loss that we use to control models, such as debiasing models on stereotyped sentences and controlling the sentiment of generations. Finally, we extend LatentQA to reveal harmful model capabilities, such as generating recipes for bioweapons and code for hacking.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new task LatentQA. It aims at improving interpretability and control in language models (LLMs) by transforming latent activations into language responses. To facilitate this, the authors propose Latent Interpretation Tuning (LIT), which fine-tunes a decoder model to answer open-ended questions about model activations. By doing so, the decoder can provide insights into latent model tendencies, biases, and behavioral control. Authors provide comprehensive and various tasks for the experimental setting and showcase the advanced model performance.

### Strengths
1. This paper propose a new dataset, LatentQA, aiming to improve interpretability and control in language models (LLMs) by transforming activations into language responses.
2. This paper includes comprehensive experiments and anlysis
3. This paper provides some insights from explaining activations in LLM.

### Weaknesses
1. This paper is hard to follow at the first glance. The term 'activation' should be explained clearer at the beginning.
2. When comparing with Patchscope, it would be fair and convincing to use the same LLaMA3.1-8b in your method for Patchscope.
3. In the controllable generation, control refers to persona, I would like to see other types of control in the experiment, e.g., topics
4. Methods like DExpert and Patchscope are training-free methods, while your LIT needs finetuning LLMs. The comparison seems to be unfair. At least you should compare the training/inference latency between different strategies.
5. There's only one LLM employed for the task, I would expect to see more LLMs to be tested.

### Questions
1. What is LoRRA finetuning?

### Soundness
2

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
3

### Summary
In this work, the authors explore an interesting problem of LLMs to interpret their own latent representations (activations). They curated a dataset called LATENTQA with over 1M QA pairs and used it to train a decoder specifically designed for this purpose. The authors demonstrate a range of valuable applications for their proposed model, including reading model latent representations and controlling model behavior. Compared to existing methods, the trained decoder achieves a significant performance improvement.

### Strengths
1. The studied problem, directly decoding activations into natural language,  is interesting and unique. 

2. They contribute a unique large-scale dataset with 1.2 million data points specifically designed for this task, which is a valuable resource for the community.

3. The authors investigate a diverse range of applications for their approach, demonstrating its effectiveness across several tasks. These include extracting relational information from latent representations, decoding personas embedded in system prompts, controllable sentiment generation, debiasing, and eliciting harmful capabilities. 

4. The proposed method shows promising results across these applications.

### Weaknesses
1. For the experiments, there’s a concern about fairness in comparison. Since the proposed model is trained on a large-scale dataset, many of the baselines used are training-free methods. Comparing these directly may not be entirely fair, and it may lead to overclaiming the observed performance improvements. Specifically, the advantage of the proposed method may be overstated if the baselines are not given the opportunity to adapt to the specific tasks, such as through fine-tuning or task-specific training. The comparison should include baselines that are trained on the same task or a similar scale of data, to provide a more balanced evaluation of the proposed method's true capabilities.

2. Another concern is the generalization capability of the model. Specifically, it would be insightful to test whether it’s possible to achieve cross-model understanding, such as using activations from one model (e.g., LLaMA) to interpret the behavior of a different model (e.g., Mistral). This is crucial to understand the robustness of the learned representations and whether they are model-specific or capture more generalizable features of language understanding. Without this, it is unclear if the decoder is truly learning to interpret latent representations or simply overfitting to the specific model it was trained on.

3. The authors frequently mention "interpretability," but the connection between this approach and interpretability is not entirely clear. It’s challenging to see how the studied applications, such as decoding latent information or controlling behaviors, directly contribute to a deeper understanding of the model’s internal workings. The current applications demonstrate the ability to manipulate the model's behavior, but not necessarily to understand the underlying mechanisms that lead to such behavior. A more direct link to interpretability would involve explaining the specific features or patterns in the latent space that are being decoded.

### Questions
Here is a list of questions for the authors:

1. **Practical Use of Predicting Future Model Behavior**: What are the practical applications of predicting future model behavior based on latent representations, and why is this an important problem to investigate?

2. **Contextualization Using WikiText-103**: 
   - (a) Since WikiText-103 is used to extract phrases containing the subjects, these phrases may also include objects. Could this lead to potential data leakage?
   - (b) Do other baselines also use WikiText-103 for contextualization? If not, could this create an unfair comparison?

3. **Determining the Appropriate Layer for Activations**: In the footnote, it mentions "during execution replace the activations of ??? with [ACT] at the appropriate layer." How is the “appropriate layer” determined for replacing activations? Section 4 notes that the activations of the 15th layer in the target model are used as input, based on early experiments. Could you provide more detail on how these early experiments guided the choice of layer? 

4. **Choice of Layer for Replacement**: Why do you consistently replace activations at layer 0, rather than other layers? Is this choice shown to be optimal, or were other layers considered as well? Has any analysis been conducted to evaluate whether this layer is indeed the most effective for achieving the desired outcomes?

These clarifications would help in understanding the setup and methodology more thoroughly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose the task and dataset for LatentQA -- a set of ([ACT], question, answer), where [ACT] is the model activation when prompted with the question and answer. This question and answer is attributed with stimuli -- something like a persona, or style to answer the question. For example, given an original question "What should I have for dinner?" the authors add a stimuli like "Answer as if you were a billionaire living on a private island", and get the model's answer by: original_question + stimuli. Next, the authors ask GPT-4 to generate QA pairs to describe the properties of the model's answer.

This LatentQA dataset is then used to train a decoder to produce the answer given the question, and patching [ACT] to the decoder.

Next, this decoder can be used to read/control LLM behavior. The experimental result is based on this read and control task

### Strengths
- An important and novel problem: how to interpret LLM activation in natural language
- Clever way to materialize this motivation into an idea
- I like that the resulting decoder can be used to both interpret activation and control LLM behavior

### Weaknesses
Execution of a great idea that falls short. For several reasons:
1. I find patching activation from layer 15 to layer 0 weird. Wouldn't the model just completely fail? When you get layer 15's activation, it is already accumulating outputs from layers 0-14, and thus numerically will be very different from the original distribution of the model's layer 0 activation. I also fail to understand the reasoning behind doing this.
2. The method is model specific -- so each time a person wants to do this for a different model, they need to collect 1.2 data points from that model? they can probably still use the same QA provided by the original LatentQA dataset, but it is still a heavy price.
3. Some crucial writing needs to be made more clear (check Questions)
4. On 5.1 results: I do not find this evaluation fair (comparing training-free method with training-based method); are there other training-based methods you can compare to?
5. On 5.1: There is a debiasing specific activation steering method: https://arxiv.org/pdf/2406.03631 have you tried to compare debiasing results with this method?
6. On 5.2: LIT seems to perform the worst on 'Generate Positive'.

### Questions
1. Is dialog = control + control response? (lines 214-215) 
2. What do you mean by repeatedly calling STEER(ACT, "control")? (lines 258-259)
3. Is STEER(ACT, "control") the gradient computed when doing LoRA fine-tuning on the "control" question-answer string, and patching the activation with [ACT]?
4. Why do you need to sample activations from prompts from he Databricks Dolly dataset on top of the stuffs you already have on LatentQA?
5. In my understanding, RepE is a fully training free, representation engineering method. Why did you use LoRRA fine-tuning with RepE?

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
3

### Summary
This paper introduces **LatentQA**, a novel interpretability task designed to translate large language model (LLM) activations into natural language, making model internals more accessible and understandable for humans. Unlike traditional interpretability techniques that yield abstract outputs (e.g., vectors or circuits), LatentQA enables direct, human-readable interpretations of model behavior. To achieve this, the authors constructed a comprehensive LatentQA dataset, created with the aid of GPT-4 to generate question-answer pairs that describe qualitative attributes of model activations. They further developed a method called **Latent Interpretation Tuning (LIT)** to fine-tune an LLM to perform LatentQA, effectively enabling it to "caption" model activations with descriptive language. This approach not only advances interpretability but also offers a means to control model behaviors, such as reducing biases and steering sentiment, through its differentiable, language-based output.

### Strengths
1. The proposed LatentQA task introduces a groundbreaking method for interpreting LLM activations by translating them directly into natural language. This approach is more user-friendly and accessible compared to existing interpretability techniques, which often rely on complex, abstract outputs.

2. LIT uniquely combines interpretability with control, enabling it not only to decode and explain LLM activations but also to steer model outputs in desired directions, such as adjusting biases or modifying response tones.

3. LIT offers a powerful approach for identifying and revealing potentially harmful model behaviors, making it a valuable tool for safety auditing and alignment.

### Weaknesses
1. The paper would benefit from an improved pipeline diagram to clarify the process flow.

2. LatentQA heavily relies on extensive data and faces challenges in scaling efficiently. The model’s interpretative ability is limited to the specific personas and activations it was trained on, which restricts its generalizability. For example, it can only interpret personas included in its training dataset. It would be valuable to assess whether LatentQA can perform well in a zero-shot setting, such as on tasks similar to those in [1].

3. The paper states that LatentQA selects the 15th layer's activations as input for the decoder, supported by early experimental results. However, intuitively, activations from later layers in large language models may be better learned and thus more effective. An ablation study analyzing the impact of different layers’ activations as input would enhance the robustness of the findings.

4. The dataset used is synthetically generated, which could introduce biases or noise. A more detailed description of the dataset construction process, along with an analysis of its diversity, would strengthen the paper's validity.

### Questions
Will the data used in this study be publicly accessible?

### Soundness
3

### Presentation
2

### Contribution
3
