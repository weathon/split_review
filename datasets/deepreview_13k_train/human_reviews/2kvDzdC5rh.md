# IntentGPT: Few-Shot Intent Discovery with Large Language Models

- Decision: Reject
- Scores: 5, 3, 6, 3, 5

## Abstract
In today's digitally driven world, dialogue systems play a pivotal role in enhancing user interactions, from customer service to virtual assistants. In these dialogues, it is important to identify user's goals automatically to resolve their needs promptly. This has necessitated the integration of models that perform Intent Detection. However, users' intents are diverse and dynamic, making it challenging to maintain a fixed set of predefined intents. As a result, a more practical approach is to develop a model capable of identifying new intents as they emerge. We address the challenge of Intent Discovery, an area that has drawn significant attention in recent research efforts. Existing methods need to train on a substantial amount of data for correctly identifying new intents, demanding significant human effort. To overcome this, we introduce IntentGPT, a novel training-free method that effectively prompts Large Language Models (LLMs) such as GPT-4 to discover new intents with minimal labeled data. IntentGPT comprises an \textit{In-Context Prompt Generator}, which generates informative prompts for In-Context Learning, an \textit{Intent Predictor} for classifying and discovering user intents from utterances, and a \textit{Semantic Few-Shot Sampler} that selects relevant few-shot examples and a set of known intents to be injected into the prompt. Our experiments show that IntentGPT outperforms previous methods that require extensive domain-specific data and fine-tuning, in popular benchmarks, including CLINC and BANKING, among others.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of intent classification/clustering and discovery using in-context learning and LLMs. It proposes 1) A method to discover useful prompts for the problem using an LLM 2) Use those prompts with few shot examples (based on semantic similarity) to classify utterances and discover new intents. The latter step is executed iteratively which leads to a growing database of novel intents.

### Strengths
1. The paper is written well and cites the relevant literature
2. Intent classification and discovery is an interesting problem on its own
3. It also has many potential useful downstream applications 
4. The results improve upon prior baselines

### Weaknesses
While studying LLMs and their performance is an important endeavour, I am not convinced by the novelty of the proposed method or the efficacy of the individual components. For instance,

1. The first part of the pipeline (ICP) seems to add little value. From row 3 vs row 5 in bottom panel of Table 2, it seems that on average ICP led to no performance boost.
2. The semantic few shot sampling (SFS) also seems to add limited value (row 3 vs row 4)
3. Intutitively "Feedback" should help, but I am not sure how is performance affected (see question below).
4. Is row 1 (i.e. no tickmarks) of Table 2 (top and bottom panels) the right baseline to compare with? Based on the appendix it seems that for row 1, the KIR ratio is 0 (since the prompt contains no information about the space of labels) while the remaining rows presumably have a KIR of 0.75.
5. How does 50-shot vanilla GPT4 with KIR = 0.75 perform? Is that closer to row 3 of table 2 or row 0? 

As mentioned in the appendix, GPT4 was trained on an unknown data distribution. The authors point out, that it clearly knows about the dataset. The arguments presented in the appendix about GPT4 not having seen the test/train split are unconvincing. I am not sure what a Frechet distance of 0.54 means without a control, but Table 5 seems to suggest that for 5 out of 12 categories, the predicted intent exactly matches the ground intent. Is that evidence that GPT4 knows a lot more than just the name of the datasets?

Is the fact the the optimal clusters (155 and 88) are so close to the ground truth numbers (150 and 70) an indication of dataset leakage or is it just an inevitable side effect of the evaluation criteria?

### Questions
1. How does performance change if only the feedback part is ablated (i.e. the database of intents is constant) from the entire pipeline?
2. It would be nice to have a longer version on Appendix A.7 with more examples and details about the statistics of discovered intents. How close are they semantically/syntactically to the ground truth labels?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper demonstrates the power of pre-trained LLM like GPT to both detect known dialogue intents and more importantly discover intents not previously known. The paper shows how the in-context prompt of an LLM can be crafted using examples from known intents, and how certain prompt design decisions affect the performance.

### Strengths
1.	This is a well-written paper, well-organized, and clear to read and follow.
2.	There is a substantive literature review which is well presented, clearly comparing each work to the paper.
3.	There are substantive appendices that are very helpful to the reader.
4.	Throughout all of it, there is obvious diligence, attention to detail, and care for the presentation.
5.	This work could be useful to anyone new to the area of Intent Discovery, and in particular applying LLMs to this problem. 
a.	This is not in conflict with the low contribution score above since the contribution question relates to research innovation value and the ICLR audience expectations - see below for more on this point.

### Weaknesses
The first LLM does not appear to contribute any value to the model, as discussed below. If this criticism is correct, then this work becomes more of an application paper, a study of applying off-the-shelf LLM to a known problem, showing how readily available new technology outperforms previous methods while significantly increasing simplicity and flexibility. While valuable, it is probably not a good match for this conference/track.

The role of the first LLM (LLM1) in the model is to create the prompt for the second LLM (LLM2). LLM1 is given an original prompt created by a human and asked to craft an optimized prompt to be used with LLM2. This can be an effective method to optimize LLM performance, chaining LLMs like this. (The reviewer uses this technique quite a bit). However, LLM1 would usually use its intelligence to create something better, with a clear added value, compared to the original input. Often, LLM1 considers specialized data in this process that is later not observed by LLM2. None of this seems to be the case in the proposed model. The list below shows a complete generated prompt by LLM1 (from Appendix 2), and the original prompt given to LLM1 that was the basis for its generation. It is obvious that the generated prompt is at most a slight rewording of the original. Next, the auxiliary data (few shot examples, known intents) given to LLM1 are basically just passed to LLM2, i.e. they could just as well be given directly to it. In other words, nothing suggests that the performance would not be equivalent if the model just used one LLM, with the original prompt and the auxiliary data (few shot examples, known intents) added to it. At the very least, the paper should compare to this scenario. The ablation study result for ICP, if I understand it correctly, compares to using a “simple prompt” like Prompt 5.E. in Appendix 2 – which lacks the key addition of the auxiliary data (which are very informative to an LLM like GPT), and is therefore not a true comparison of using one vs two LLMs. 

LLM1 Generated Prompt: “As an AI language model, your task is to assign the correct intent to a given textual utterance.”	
Original Prompt: “You are a helpful assistant and …  You specialize in … the task of assigning textual utterances to specific intents”

LLM1 Generated Prompt: “The intent can be one of the pre-defined intents or a new one that you create based on the context and knowledge about the problem and specific data domain.”	
Original Prompt: “… some of which are pre-defined and others are not and have to be created”… “sufficient context and knowledge about the problem and specific data domain.”

LLM1 Generated Prompt: “You should never assign an utterance to ’unknown’.”	
Original Prompt: “never assign a utterance to ’unknown’”

LLM1 Generated Prompt: “For each utterance, analyze the context and the specific request or action implied.”	
Original Prompt: “…acquire sufficient context…”

LLM1 Generated Prompt: “If the utterance matches a known intent, assign it to that intent. If it doesn’t match any known intent, create a new intent that accurately represents the request or action implied by the utterance.”	
Original Prompt: “you need to be aware of the known intents and reuse them as much as possible, but need to create new intents when there are not known intents that fit the given utterance”

LLM1 Generated Prompt: “Remember, the goal is to understand the user’s intent as accurately as possible.”	
Original Prompt: “maximizing the model’s performance in the task”

LLM1 Generated Prompt: “Be aware of the known intents and reuse them as much as possible, but don’t hesitate to create new intents when necessary.”	
Original Prompt: “be aware of the known intents and reuse them as much as possible, but need to create new intents”

The other generated prompt example in Appendix 2 (Prompt 3.C) is basically equal to the original as above, with the exception of the following fragment: “The utterances can be questions, statements, or requests related to banking services like card transactions, account top-ups, refunds, identity verification, card delivery, transfer fees, and more.” – But this is just a summary of the auxiliary example data and a single GPT would have it by default by having the auxiliary example data itself.

A couple of smaller points:
1.	For the “Semantic Few-Shot Sampling” the proposed model uses SentenceBERT to do the embeddings, which is a strange choice given that better quality embeddings can be attained with OpenAI’s GPT3+ models, which are already used in this work in other ways.
2.	On page 8, “that while SKIF” should probably be “that SKIF”

### Questions
Would you be able to run a comparison to a one-LLM setup as described above, i.e. by using the “Original Prompt” and adding the auxiliary data directly to it?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a system of GPTs, called IntentGPT, in order to discover new intents in an open-world recognition system. The method of the paper consists of an LLM (or two) with a prompt to design an in-context learning prompt to do intent identification from utterances, with a special provision for labeling new intents that it has not seen before. This prompt is then augmented by including semantically relevant examples of labeled utterances to the test utterances and a list of possible intents and then handed to an LLM to perform the intent identification. The paper evaluates its method on two different benchmarks, with three different LLMs, and shows competitive, and often better, performance as compared to both semi-supervised and full unsupervised techniques for intent discovery.

### Strengths
The paper has good empirical validation is clear in its explanations and figures and is attacking a difficult and significant problem.  The paper does a thorough empirical validation by comparing the multiple LLM models, including an open-source, one. This highlights that the proposed methodology is actually what is working for the task at hand. The paper also shows its proposed methods' performance relative to state-of-the-art methods which thoroughly validates the methods' effectiveness. Overall, given the context and high levels of linguistics understanding required for such a task as open-world intent discovery, the use of LLMs is a solid approach.

The paper also proactively attempts to answer questions that arise when using a GPT model, such as whether the model has seen the training data before in its pre-training.

### Weaknesses
The paper is missing some grounding in previous literature and it's not clear what the value of all of the components of its proposed methodology is. First, the whole component of Semantic Few-shot Sampling (SFS) reads to me as just being Retrieval Augmented Generation or RAG. See https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/ for a description. The SFS component then is not a novel contribution and should be cited as RAG. 

Second, it's not clear from the write-up what the value of the in-context prompt generator (ICPG) step is. The authors mention  that they do an ablation study with this module but do not provide what the alternative prompt is besides “Utilizing the automatically generated In-Context Prompt (ICP) by IntentGPT proves superior to using a \textit{simple prompt description}.” From looking at the examples provided in the appendix, the crafted prompt looks like what I would have given the LLM as a base prompt for this task, so I am not convinced that the ICPG step is producing better prompts than what a human would give.

Third, and this is more of a minor criticism and possibly something for future work, but why not test other prompting schemes? For example, especially given the ICPG step, why not tree a Chain of Thought style of prompt for this task? Doing such a prompting scheme combined with the ICL might deliver even better results.

### Questions
There are a couple of questions about the manuscript, some of which have already been detailed earlier in this review.

-	What is the “simple prompt description” that was done in the ablation study of the ICPG module?
-	When doing empirical testing, since this is meant to be used in an open-world setting, was the inclusion of test examples that express no intent or multiple intents considered? If so, how did this method handle those cases?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes IntentGPT, a framework for few-shot intent discovery using large language models (LLMs) like GPT-3.5, GPT-4, and Llama-2.

### Strengths
1. Eliminates the need for training and extensive domain-specific data by leveraging the knowledge and generalization capabilities of LLMs through in-context learning. 

2. Introduces an automatic prompt generation module that leverages examples from the training set to create high-quality prompts tailored for intent discovery.

3. Proposes techniques like Semantic Few-Shot Sampling to retrieve relevant examples and Known Intent Feedback to reuse discovered intents. 

4. Shows competitive performance compared to prior state-of-the-art semi-supervised methods on intent discovery benchmarks like CLINC and BANKING.

5. Provides comprehensive analysis on the influence of various hyperparameters for few-shot in-context learning using frozen LLMs.

### Weaknesses
1. The core idea of using LLMs for few-shot learning, while powerful, is not highly creative or novel at this point given extensive prior work on leveraging LLMs. The techniques like prompt engineering and few-shot sampling, while optimized for intent discovery, mostly draw from existing approaches for adapting LLMs.

2. Is there a suspicion of cheating in the KIF mechanism? Is there any unfairness compared to traditional deep learning paradigms?

3. The research is limited to English datasets, however, large language models can be easily extended to other languages, so it is necessary to test the performance of IntentGPT in other languages. I think the author may lack this necessary comparison.

### Questions
See Above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a framework for Intent Discovery by utilizing pre-trained LLM s like GPT 4 for few shot in context learning. The authors performed prompt engineering to guide LLMs to produce the desired generations. Experimental results show improvement over existing approaches.

### Strengths
Good prompt engineering to guide GPT-4 to produce intents.

Incorporation of few shot examples to improve performance.

Improving performance without training overhead.

### Weaknesses
Tested on only 2 datasets; difficult to not judge robustness of the proposed method without seeing results on different datasets.

Prompt and few shot example usage might change depending on the data.

Known intent feedback might not be usable for zero shot context.

### Questions
Please perform experiments on more datasets that have diverse input structure. (Many datasets are out there: https://paperswithcode.com/task/intent-detection)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
