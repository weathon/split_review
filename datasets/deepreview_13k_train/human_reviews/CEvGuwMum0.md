# JudgeRail: Harnessing Open-Source LLMs for Fast Harmful Text Detection with Judicial Prompting and Logit Rectification

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
Large language models (LLMs) simultaneously facilitate the generation and detection of harmful text. Leading LLM developers, such as OpenAI, Meta, and Google, are driving a paradigm shift in the detection of harmful text, moving from conventional detectors to fine-tuned LLMs. However, these newly released models, which require substantial computational and data resources, have not yet been thoroughly investigated for their effectiveness in this new paradigm. In this work, we propose JudgeRail, a novel and generic framework that guides open-source LLMs to adhere to judicial principles during text moderation. Additionally, we introduce a new logit rectification method that accurately interprets an LLM's classification intent, rigorously controls its output format, and significantly accelerates detection. By integrating several top-performing open-source LLMs into JudgeRail without any fine-tuning and evaluating them against OpenAI Moderation API, LlamaGuard3, ShieldGemma, and other conventional moderation solutions across various datasets, including those specifically designed for jailbreaking LLMs, we demonstrate that JudgeRail can adapt these LLMs to be competitive with fine-tuned moderation models and significantly outperform conventional solutions. Moreover, we evaluate all models for detection latency, a critical yet rarely examined practical aspect, and show that LLMs with JudgeRail require only 46% to 55% of the time needed by LlamaGuard3 and ShieldGemma. The generic nature and competitive performance of JudgeRail highlight its potential for promoting the practicality of LLM-based harmful text detectors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces JudgeRail, a framework designed to guide open-source language models in detecting harmful text through judicial prompting and a novel logit rectification technique. The study compares JudgeRail’s effectiveness and efficiency against existing moderation tools, showing that JudgeRail enhances detection accuracy and latency without requiring fine-tuning.

### Strengths
1. Significance: The paper tackles a critical issue, harmful text detection, which is increasingly urgent as LLMs are deployed widely in real-world applications.

2. Comprehensive Evaluation: The paper includes comparisons with state-of-the-art models and examines latency, a rarely explored aspect in text moderation studies, providing practical insights for real-world applications.

### Weaknesses
1. Insufficient Justification: The paper does not adequately justify the specific harmful categories used in the label system, which could limit the generalizability of its results. What are P1, P2, etc., and S1, S2, etc? 

2. Lack of Novelty in Core Concept: Judge framework in content moderation is not new. There are some missed literature already explored this concept and implemented. Such as:

Mitchell L. Gordon, Michelle S. Lam, Joon Sung Park, Kayur Patel, Jeff Hancock, Tatsunori Hashimoto, and Michael S. Bernstein. 2022. Jury Learning: Integrating Dissenting Voices into Machine Learning Models. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems (CHI '22). Association for Computing Machinery, New York, NY, USA, Article 115, 1–19. https://doi.org/10.1145/3491102.3502004
 
It would be important for the authors to justify their approach's novelty and difference with previous relevant work.


### Questions
It is not clear why the paper claims that "These findings suggest that text moderation tasks have lower requirements for high-precision computing compared to text generation tasks." Low precision is the results, how could it explain the requirement? 
However, achieving acceptable results with lower precision does not inherently justify that text moderation has lower precision requirements. 
Instead, it simply indicates that this particular framework, JudgeRail, was effective in the given tests. The paper would benefit from clarifying the distinction between observed outcomes and actual task requirements, and ideally, providing evidence or reasoning that explains why moderation tasks inherently need less precision compared to generation tasks.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a moderation framework for harmful text detection using open-source LLMs. First, the framework  uses prompting based on jurisdictal principles (assigning a judge role, using chain-of-thought prompting) and secondly, restrictis the logit output to a predetermined few-shot learned set of labels that are based on PerpepeciveAI, the OpenAI Moderation API and LlamaGuard3. The authors claim this is more efficient while performing almost on par with the closed models’ APIs.

### Strengths
The paper introduces a simple and low-cost approach using prompting as a content moderation technique, along with controlled decoding. By adapting the prompting strategy of open LLMs models to the schema of the baseline APIs also including LlamaGuard3 and ShieldGemma, along with controlled decoding the authors achieve competitive performance without extra fine-tuning. This is interesting in spite of its simplicity. They provide a multi-faceted evaluation of false-positive classification.

The paper is generally well-written.

### Weaknesses
While multiple aspect of the false-positive ratio are evaluated, I have several concerns regarding the evaluation.

1. The reated work section mentions two recent approaches, SplineLLM and RigorLLM, which JudgeLLM is not compared to (only what the authors call conventional models based on BERT (martin-ha, toxberta, s-nlp, all bert-based); I find this comparison important. How does this approach differ from those two?

2. Label set and constrained decoding:
- Lines 305-310: E.,g, “For Perspective API, we converted its multi-label detection results into binary classification ”: how does it perform using multi-label output?
- How much does the approach depend on the decoding vocabulary?
    - I find a more detailed evaluation of the logit distribution important:
	 - different decoding vocabulary sizes
	 - a comparison to the performance using the overall logit distribution, without restrictions
- The authors used only 100 samples to create the decoding vocabulary (logit distribution): how much does performance depend on the sample size and does it change with more/less samples?

Writing:
The phrasing in some parts is unneccessarily strong, e.g.: Lines 20-22: "accurately interprets an LLM’s classification intent, rigorously controls its output format, and significantly accelerates detection"

### Questions
A more general question:
Interestingly, this simple approach performs on par with closed models' APIs and also fine-tuned ones such as  LlamaGuard3, while also being much more cost-efficient. What is your intuition on that? E.g, how much is it depending much on the task/datsets?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents JudgeRail, a framework designed to adapt LLMs for detecting harmful content. The authors conduct extensive experiments comparing the performance of open-source LLMs with JudgeRail, against traditional harmful content detection models and commercial APIs. They introduce a logit rectification method to refine LLM outputs, ensuring more valid classifications and reducing latency. Results show that open-source LLMs equipped with JudgeRail perform comparably to commercial APIs and outperform conventional detection methods.

### Strengths
- The research question is well-motivated, emphasizing the importance of detecting harmful content and preventing prompt jailbreaking in publicly deployed models. This paper effectively explores how to adapt open-source LLMs for better harmful content detection. In a landscape dominated by commercial APIs, it is crucial to investigate scalable and effective methods for open-source models. The results show that while open-source LLMs may not surpass commercial solutions in all respects, they can perform comparably, highlighting their value in content moderation efforts.

- They conduct extensive experiments to provide a robust comparison between open-source LLMs and both traditional and commercial detection models. Also, they explore the validity of their design choices very meticulously.

### Weaknesses
 - The novel logit rectification method has shown effectiveness on a limited set of examples. However, it is difficult to assess its overall impact on the framework's performance. The paper is missingcomparisons using simple prompts on the LLMs and ablation studies that evaluate performance with and without the logit rectification method, as these analyses could provide clearer insights into its contribution. Specifically, the paper lacks a detailed analysis of how the logit rectification affects different types of harmful content, and whether it introduces any biases or unintended consequences. The absence of a controlled comparison against standard prompting techniques makes it difficult to isolate the specific benefits of the proposed method.

- While the paper is generally easy to understand, the experiments section is densely written, making it challenging to follow all the observations. For example, Section 4.3 would benefit from the inclusion of small headings or bolded paragraphs headings to better organize and group the observations, which would significantly enhance readability.

Minor comment:
- You use "a LLM" in many places (lines 183, 192 etc.), but I think it should be "an LLM". Please check with a native speaker and make correction if required

### Questions
- Do you have any insights on how these open-source models operate without the JudgeRail framework? Are the LLMs capable enough with simple prompts, and does JudgeRail generally enhance their performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces JudgeRail, a framework designed to enhance harmful text detection using open-source large language models (LLMs) without requiring extensive fine-tuning. By leveraging "judicial prompting" and a novel "logit rectification" technique, JudgeRail ensures accurate text classification and significantly reduces detection latency. Evaluated against established tools like OpenAI’s Moderation API and specialized models like LlamaGuard3 and ShieldGemma, JudgeRail-equipped LLMs demonstrated competitive performance while achieving faster processing times (only 46-55% of the time required by other advanced models).

### Strengths
1) Introducing label systems, novel logit rectification method and calibration is really interesting and found to be helpful.

2) The evaluation and baselines includes the state of the art models.

3) The latency seems be a strength of the proposed model.

### Weaknesses
1) No limitations section

2) No comparison with prompt detection techniques. Prompt detectors are simple and easy to integrate as well as latency is quite low.

3) Lack of enough baselines. Readers and researchers will be interested in comparison with prompting techniques which are much simpler to execute like baselines with only chain of thought prompting and other advanced prompting techniques.

4) The datsets implemented looks irrelevant hateful prompts differ from hate speech and hatexplain. please refer[1],[2] and it would be great if you can implement those.

5) The novel method cannot be implemented on the GPT models which is the model used by most. This makes the model cannot be utilised by many who are dependent on GPT models.

### Questions
1) Can you implement the proposed model on the GPT models.

2) Can this be applicable for vison models as well like text to image generation. please write a section in appendix.

3) Is the proposed method much faster than prompt detection techniques?

4) Why there is no evaluation comparison with prompting techniques? Though they might look simple readers wouldlike to their evaluation metrics as well.

### Soundness
3

### Presentation
2

### Contribution
3
