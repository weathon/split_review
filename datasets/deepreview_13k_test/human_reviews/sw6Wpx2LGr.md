# Mitigating Dialogue Hallucination for Large Vision Language Models via Adversarial Instruction Tuning

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Mitigating hallucinations of Large Vision Language Models\,(LVLMs) is crucial to enhance their reliability for general-purpose assistants.
This paper shows that such hallucinations of LVLMs can be significantly exacerbated by preceding user-system dialogues.
To precisely measure this, we first present an evaluation benchmark by extending popular multi-modal benchmark datasets with prepended hallucinatory dialogues powered by our novel Adversarial Question Generator (\algname{}), which can automatically generate image-related yet adversarial dialogues by adopting adversarial attacks on LVLMs. On our benchmark, the zero-shot performance of state-of-the-art LVLMs drops significantly for both the VQA and Captioning tasks.
Next, we further reveal this hallucination is mainly due to the prediction bias toward preceding dialogues rather than visual content.
To reduce this bias, we propose Adversarial Instruction Tuning (\algnameB{}) that robustly fine-tunes LVLMs against hallucinatory dialogues.
Extensive experiments show our proposed approach successfully reduces dialogue hallucination while maintaining performance.
\vspace{-0cm}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the issue of dialogue hallucination in LVLMs, where preceding dialogues can lead to unreliable outputs. 

It introduces a benchmark dataset, EvalDial, using the Adversarial Question Generator from VQA and image captioning datasets. Then, it proposes the Adversarial Instruction Tuning method, which fine-tunes LVLMs against hallucinatory dialogues.

The results suggest most of the well-performing LVLM failed on the EvalDial benchmark, in which AIT successfully reduced dialogue hallucination while maintaining performance.

Overall, this work aims at an important research problem, presents a reasonable and effective approach, and contains insightful discussions. The implementation is reproducible.

### Strengths
- The AQG is a reasonable and scalable algorithm for data generation. 
- The experiment design is comprehensive, and the results show the AIT approach effectively mitigates dialogue hallucination.
- There is a potential that both AQG algorithm and AIT strategy can be extended to more tasks and modalities.

### Weaknesses
An important contribution of the work is to propose AIT as a method to mitigate dialogue hallucination. However, the evaluation only focuses on the EvalDial benchmark, which includes synthetic dialogue augmented from non-dialogue data. This is insufficient to justify AIT's real-world value in countering the visual dialogue hallucination problem.

### Questions
Does AQG-generated data somehow reflect the real distribution of LVLM's hallucination behaviors? Or is it just a way to create fake adversarial dialogue that serves AIT's finetuning purpose?

### Soundness
3

### Presentation
4

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
This paper tackles the problem of hallucinations in Large Vision-Language Models (LVLMs), particularly how biases from prior dialogue contexts can lead to incorrect or "hallucinated" responses. To measure and address this, the authors introduce EvalDial, a benchmark created by adding adversarial dialogue sequences to existing multimodal datasets, using a novel Adversarial Question Generator (AQG). Their findings show that these adversarial dialogues significantly impact model accuracy. As a solution, they propose Adversarial Instruction Tuning (AIT), which fine-tunes LVLMs by masking dialogue tokens to reduce the bias from previous conversations. Experimental results demonstrate that AIT successfully minimizes hallucinations across multiple tasks while preserving overall model performance.

### Strengths
The introduction of EvalDial and AQG provides a structured and novel approach to testing model robustness against adversarial dialogue contexts, successfully inducing dialogue hallucinations across multiple models and confirming AQG's effectiveness. Notably, AIT demonstrates superior performance over other models in handling adversarial rounds, highlighting its potential as a reliable technique for mitigating dialogue-induced biases in broader LVLM applications where robustness is essential.

### Weaknesses
(1) The paper’s focus on hallucinated dialogue scenarios limits the ability to gauge the model’s general performance in non-hallucinated contexts. A broader evaluation that includes non-adversarial scenarios would provide a more comprehensive view of the model’s robustness and applicability.

(2) The study relies heavily on the CIDEr metric for evaluating image captioning, limiting insights into overall performance. Results using additional metrics such as BLEU, ROUGE, METEOR, or GPT-aided evaluation (accuracy) would provide a more balanced view of the model’s capabilities.

(3) While the Adversarial Dialogue is designed to be image-related and likely to induce hallucination in response to the original test question, it introduces content that is largely independent of the question itself. This raises the question: if the adversarial content is unrelated to the core test question, would simply resetting the chat between exchanges be a more straightforward solution?

### Questions
(1) The adversarial dialogue sequences used for prepending contain intentionally misleading answers, which likely disrupt baseline models due to their lack of exposure to such cases. Would AIT still demonstrate superior performance if prepend responses were correct, non-hallucinatory answers?

(2) Does the Masked Instruction Tuning approach risk overly discouraging reference to preceding dialogues? The relatively stable performance in Table 6, even as dialogue rounds increase, suggests this possibility. Could this approach prevent the model from effectively using relevant context from previous interactions, which is crucial in real dialogue scenarios where preceding exchanges often contain meaningful information?

(3) It would be valuable to understand how the model’s performance in captioning tasks changes as the length of dialogue rounds increases, particularly for AIT in handling longer, potentially more complex dialogue contexts.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper discovers that LVLMs can exhibit hallucination phenomena during user-system dialogues and presents a EvalDial benchmark for validation. Experimental results indicate that the performance of existing LVLMs significantly declines on this hallucination dataset. Furthermore, to mitigate the hallucination issue, the paper proposes an Adversarial Instruction Tuning method, which has been shown through experiments to reduce the occurrence of hallucinations effectively.

### Strengths
1. Benchmark on which the performance of existing LVLMs significantly declines. 
2. Adversarial Instruction Tuning method, which has been shown through experiments to reduce the occurrence of hallucinations effectively.

### Weaknesses
Insufficient in-depth analysis of the experiment resulted in the inability to determine whether the dataset was meaningful. The benchmark data analysis is also insufficient. If the following issues in the QUESTIONS are solved, we will consider modifying the score.

1. Regarding the impact of prepended dialogues: Is the hallucination caused by an incorrect prediction made by the LVLM when the user asks a prepended question, which then leads to hallucinations in subsequent questions? Or is the hallucination triggered because the user's prepended question conflicts with the current question (i.e., unrelated to the answer)? Could you provide a detailed analysis of how the information in the preceding dialogues leads to hallucinations in the model?  It is essential to understand the mechanisms behind the mentioned hallucinations in LVLMs. Specifically, there are several following possible assumptions. (1)If the LVLM makes an incorrect prediction when interpreting a prepended question, this could indeed set off a chain reaction of hallucinations. The model might latch onto incorrect information, which it then carries forward into subsequent interactions. This could happen if the model's prediction is misled by the phrasing or context of the prepended question, causing it to deviate from the correct path of reasoning. Hallucinations occur when the model generates responses that are not grounded in the actual experiments. (2)Another hypothesis is that the model can not handle the long text of the prepended question. (3)A prepended question that is unrelated to the current question can also cause hallucinations. This is because the LVLM might struggle to recognize different segments of the dialogue. When the model encounters a question that seems to diverge significantly from the previous context, it may attempt to reconcile the two by creating a fabricated connection. This process can lead to the generation of wrong responses.
You may add specific experiments. For example, you could compare hallucination rates when prepended dialogues contain (1) incorrect information vs (2) unrelated information vs (3) correct, long, and related information.

2. In the benchmark, is a hallucinated prepended dialogue added before each question? If multiple rounds of dialogue are added before the current question, and the hallucinated dialogues are positioned differently within these rounds (e.g., at the beginning or just before the current question), or if the number of hallucinated dialogues varies, how would the model's performance change? You conduct ablation studies with different numbers of hallucinated dialogues and positions.

3. It is suggested to add a statistical table to analyze the benchmark, such as the distribution of dialogue types, and average dialogue length.

4. In Table 1, the mean DTAR values for hallucinated cases are 0.37 or 0.25, which are not particularly high. How does this prove that the hallucinations are caused by prepended dialogues? Furthermore, should the impact of the distance of the prepended dialogues from the current answer (whether closer or farther) also be considered in evaluating the influence on the answer? You may consider significance tests comparing hallucinated vs non-hallucinated cases. At the same time, it is suggested that the author test whether the DTAR value is affected by the relative position of the prepended hallucination dialogue and the current question.

### Questions
1. Regarding the impact of prepended dialogues: Is the hallucination caused by an incorrect prediction made by the LVLM when the user asks a prepended question, which then leads to hallucinations in subsequent questions? Or is the hallucination triggered because the user's prepended question conflicts with the current question (i.e., unrelated to the answer)? Could you provide a detailed analysis of how the information in the preceding dialogues leads to hallucinations in the model?

2. In the benchmark, is a hallucinated prepended dialogue added before each question? If multiple rounds of dialogue are added before the current question, and the hallucinated dialogues are positioned differently within these rounds (e.g., at the beginning or just before the current question), or if the number of hallucinated dialogues varies, how would the model's performance change?

3. It is suggested to add a statistical table to analysis the benchmark.

4. In Table 1, the mean DTAR values for hallucinated cases are 0.37 or 0.25, which are not particularly high. How does this prove that the hallucinations are caused by prepended dialogues? Furthermore, should the impact of the distance of the prepended dialogues from the current answer (whether closer or farther) also be considered in evaluating the influence on the answer?

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
3

### Summary
The paper introduces a new benchmark designed to evaluate vision-language models (VLM)  when dialogues are corrupted by adversarial questions. While this aims to address dialogue hallucination, such issues appear rare in real-world applications. Additionally, the benchmark is not tested on models known to hallucinate less, which raises concerns about its general applicability. There are also some contradictory statements about hallucinations and examples provided.

### Strengths
1. The paper presents a novel benchmark that specifically evaluates vision-language models when conversations are corrupted by adversarial questions from previous rounds. This benchmark is powered by the Adversarial Question Generator (AQG), which generates adversarial questions to test model robustness. 

2. The paper proposes a solution, Adversarial Instruction Tuning (AIT), to mitigate the performance drop in VLMs caused by these adversarial dialogues, which is an important contribution to improving the robustness of these models.

### Weaknesses
1. The real-world applicability of adversarial questions, as demonstrated in the examples provided, seems limited. The likelihood of such adversarial scenarios occurring in practical use cases appears low, and hence, this might not be a widespread issue. 

2. The hallucinated dialogues presented in Figure 2 may indicate that the underlying model itself is not robust enough. Many recent works, such as ShareGPT4V, have tackled hallucination issues with better training data. The paper does not evaluate its methods on models that are known to hallucinate less, leaving the effectiveness of the proposed method for stronger models unclear. 

3. Section 3.1: Even by the paper’s own definition of hallucination (line 155: “the generated content that is nonsensical or unfaithful to the given source content”), the examples provided don’t clearly qualify as hallucinations. For instance, the responses in Figure 1 and Figure 2 make sense given the incorrect text from the previous dialogue. For example, in Figure 2 (mid-column), the answer "Antarctica" makes sense in relation to the mention of penguins from the prior round.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
3
