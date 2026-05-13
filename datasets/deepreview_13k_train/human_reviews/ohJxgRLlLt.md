# Large (Vision) Language Models are Unsupervised In-Context Learners

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Recent advancements in large language and vision-language models have made it possible to solve new tasks via zero-shot inference without task-specific training. Various adaptation techniques, such as In-Context Learning (ICL), supervised fine-tuning, and prompt engineering, can further enhance the model’s performance on a given task. However, these methods require either labeled examples or substantial manual effort to construct effective prompts. In this work, we introduce a joint inference framework extending the standard zero-shot inference. In contrast to independent zero-shot predictions, joint inference makes predictions simultaneously for all inputs for a given task. Since direct joint inference involves a computationally expensive optimization, we develop efficient approximation techniques resulting in two unsupervised adaptation methods that are compatible with language and vision-language models: unsupervised fine-tuning and unsupervised ICL. We demonstrate the effectiveness of both approaches across a broad range of tasks and models, including language-only Llama 3.1, vision-language Open-Flamingo and API-only access GPT-4o models. Our experiments reveal substantial improvements over the standard zero-shot approach. Furthermore, our approach, although unsupervised, often performs on par with supervised approaches that use ground truth labels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a joint inference framework for large language and vision-language models, with an optimized and efficient approximation techniques to enable unsupervised adaptation to new tasks through two main methods: unsupervised fine-tuning and unsupervised in-context learning (ICL). This approach makes predictions jointly across multiple inputs, and shows significant improvements over zero-shot inference, sometimes achieving results close to supervised approaches without needing labeled data.

### Strengths
1) A big strength of this method is that it provides a framework to effectively allows unsupervised fine-tuning and ICL, reducing the need for labeled examples which is usually expansive in practice.
2) It also demonstrates considerable accuracy and generalization improvements across a range of language and vision tasks, even comparing with supervised fine-tuning methods. The experiments performed on multiple datasets, models, and tasks, demonstrating the framework’s effectiveness in both text and vision-language scenarios.
3) It generally works for various model types such as open-weight models (e.g., Llama-3.1, OpenFlamingo) and close-weight models (e.g., GPT-4), showing flexibility and robustness in application.

### Weaknesses
1) The effectiveness of unsupervised ICL seems to rely on the model’s inherent in-context learning abilities. This may restrict its applicability to models lacking strong ICL capabilities. It is unclear how does the same method work for other models with relative weak capability.
2) While the experimental results are promising, a deeper theoretical analysis of the joint inference framework’s optimization behavior and potential limitations or failures would strengthen the contribution.

### Questions
Q1: Do you have any evaluations on how the joint inference framework affects model robustness, especially when inputs are noisy or out-of-distribution?

Q2: It is also very interesting to see if there are any common failure cases/scenarios of the proposed method?

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
3

### Summary
The paper proposes an 'unsupervised joint inference' framework to improve the performance of large language / vision-language models on tasks without using labeled data. The proposed approach predicts output sequences simultaneously for multiple inputs, leveraging inter-sample dependencies. There are two variants in the proposed approach: 1. use the model's own predictions to finetune its parameters. 2. Use in-context learning to refine predictions iteratively. The paper conducts experiments on some nlp and vision-language datasets and claim substantial improvements to vanilla zero-shot approach and often on-par performance with supervised approaches.

### Strengths
1. The paper proposes an novel framework to adapt llm or vlm for unseen tasks. 
2. The paper intents to build solid theoretical foundation for the proposed approach. It establishes a theoretical connection between the proposed unsupervised ICL method and the joint inference objective, showing how the former approximates the latter.
3. The experiments conducted are diverse on different tasks: text classification, image classification, question answering, visual question answering, natural language inference, common-sense reasoning, and math problem-solving.
4. Experiments show that the proposed approach is effective and outperform the baselines by a large margin.

### Weaknesses
1. The paper overclaims it's contribution and effectiveness of its approach. In abstract, the paper claims that 'our approach, although unsupervised, often performs on par with supervised approaches that use ground truth labels.' However, its an overclaim for the following reasons: (1) In the results shown in the paper, most of the time supervised approach is better than the proposed approach. (2) Supervised approach uses LoRA instead of full model training. 
2. The experiments are not solid. Some of the experiments in the paper use non-standard (potentially easy/small/old/deprecated) datasets. Most notably - CIFAR 10/100 for image classification and COCO-colar and COCO-number for VQA. The results are much less convincing compared to ImageNet for classification and VQA v2 for VQA.

### Questions
Is there a reason for picking these datasets for experiments? Is it possible to perform the same experiments on more recent and broadly adopted datasets?

### Soundness
2

### Presentation
2

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
The paper introduces an unsupervised joint inference framework to improve the performance of LLMs and VLMs by considering the entire set of questions for a given task instead of making predictions on each question independently. They utilize the shared context of these questions to improve model accuracy It includes a self-improvement loop where the model iteratively refines its predictions by using its own prior answers as in-context examples to guide the next round of predictions. This self-refinement continues over multiple iterations, allowing the model to gradually improve and make more consistent predictions without needing labeled data. The authors show that this

### Strengths
- the motivation of utilizing the entire corpus of the task to improve overall performance is compelling, as there is often shared context that is underutilized
- this method is versatile and applies to both open and closed source models as well as across modalities
- the results indicate that this can provide substancial improvements over zero shot methods

### Weaknesses
 - the main weakness of this paper is clarity: sections 3 and 4 are hard to follow and it would have been significantly clearer to provide a methods figure which outlines the iterations and IC examples used. If I understand this method correctly, it uses responses to questions from previous iterations as in context examples for questions in the current iteration, optimizing for the joint likelyhood over all the examples in the batch. If this is the case, then it should have been stated clearly in prose in section 4. I find the entirety of section 3 to be unnecessary as it is explaining commonly known procedures for model training and inference, and much of section 4 to use unnecessary notation in explaining a relatively straightforward method. Again, I have no major concerns about the method itself, but I urge the authors to remove or significantly shorten section 3, add a methods figure, and rewrite section 4. A methods figure could be in the form of showing the inputs to the LLM at each iteration for the no weight-update option to indicate the change in in context examples. 
- I am not fully convinced that adding iterations helps for the no weight update setting. if the authors added a 1-iteration baseline to their results this would resolve my concern
- all the benchmarks used in the results section are out of date and focus on easy tasks. The results would be much more compelling if the authors included a benchmark like MMLU. That being said, given the short rebuttal period I would put this experiment as a lower priority than the two above concerns 

### Questions
- how does your method answer multiple questions with one model call? What is the exact prompt used and how are the in context examples formatted? This should be in the appendix, table C1 does not indicate where in context examples are placed nor does is show how multiple questions are answered in a single pass. If the authors could give a template of the prompt used in the iteration steps for a benchmark that would be sufficient
- are the in context examples used different than the questions the LLM is tasked to answer in a given call?

### Soundness
3

### Presentation
1

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
This paper aims to enhance the zero-shot inference capabilities of existing open- and closed-weight models. To achieve this, it introduces a joint inference framework that processes and makes predictions for all task-related inputs simultaneously, rather than handling each input individually. The paper presents two efficient approximations—unsupervised fine-tuning and unsupervised in-context learning (ICL)—to reduce the computational complexity of joint inference. The results demonstrate the effectiveness of the proposed method across NLP and vision tasks, using two large language models (LLaMA-3 and GPT-4o) and one vision-language model (OpenFlamingo).

### Strengths
- I believe the idea of self-refinement using model predictions is solid, as is the approach of zero-shot evaluation without a labeled support set, which contrasts with the traditional definition of supervised in-context learning (ICL). In my view, the paper aligns well with the concept of inference-time compute scaling, as evidenced by the O1 model by OpenAI, where generating the final answer requires multiple steps (turns) by the model. Hence, the problem definition is quite sound. 

- The paper presents two distinct approximations for the joint inference task, which appear to outperform all baselines. The authors demonstrate this rigorously across several NLP and vision tasks.

### Weaknesses
In the following, I will provide a list of weaknesses and a follow-up question for each in case the authors want to reply.

1. **Model Cacapcity and ICL Abilities**: The proposed method assumes that the pretrained model already possesses few-shot in-context learning (ICL) abilities, which are typically found in large-scale models (those with over 8 billion parameters). What about models that don't have these ICL capabilities? Can they leverage their context more effectively during joint inference? To be more specific, if the authors use the Phi-1.5 model and conduct unsupervised fine-tuning or unsupervised ICL again, what would be the outcome?

2. **Reliance on Task Encoder Approximation**: I think the design of the Task Encoder has not been explored properly in the paper. The authors only did not mention why the same pre-trained model + LoRA can be a good approximation for the task encoder approximation tasks. Why is this case? Based on which ablation in the paper? What are the other alternatives? It’s important to note that, as shown in other research, LoRA often tends to underfit a task, which can lead to suboptimal or inconsistent improvements. This raises concerns that the proposed task inference model may not accurately reflect the tasks that the model is intended to predict.

3. **Limited Applicability to Open-Ended Tasks**: Aside from the single open-ended experiment mentioned in line 395 for the GSM8K benchmark, I do not see any other experiments demonstrating the effectiveness of the proposed method for open-ended generation. With just one experiment, it is not convincing that the method is effectively generalizable for both unimodal and multimodal open-ended generation. Do the authors have any additional ablations or experiments to support the strengths of their proposed method?

4. **Missing Compute-related Ablations**: In multi-turn inference settings, it is crucial to provide the number of FLOPs used to arrive at the final answer. Do the authors have any experiments that demonstrate the scaling curve, with FLOPs on the x-axis and performance on the y-axis?

5. **Lack of Proper Evaluation in Multi-modal Setting**: In the paper, the authors used OpenFlamingo and demonstrated that the proposed method shows some effectiveness. However, I'm curious about their design choice and why they opted for OpenFlamingo. What about other alternatives that may be more powerful and capable of handling larger contexts? For example, LLaVA-Next-Interleaved is a suitable candidate, as it is trained with the in-context learning (ICL) objective function. Could the proposed method work properly if LLaVA-Next-Interleaved were used instead of OpenFlamingo? Additionally, regarding multimodal evaluation, assessing a model using COCO-color and COCO-count might not provide an accurate reflection of the proposed method's performance. Have the authors considered evaluation on the MMMU Benchmark? This benchmark is recognized as a legitimate evaluation tool for multimodal large language models, and LLaVA-Next-Interleaved has reported strong results on it.

### Questions
Asked above.

### Soundness
2

### Presentation
3

### Contribution
3
