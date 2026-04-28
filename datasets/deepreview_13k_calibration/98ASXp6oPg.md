# Self-Explained Keywords Empower Large Language Models for Code Generation

- Decision: Reject
- Avg Score: 4.67
- Scores: 8, 3, 3

## Abstract
Large language models (LLMs) have achieved impressive performance in code generation. 
However, due to the long-tail distribution of LLMs' training data, low-frequency terms are typically underrepresented in the training process. Consequently, LLMs often misunderstand or overlook problem-specific, low-frequency keywords during code generation, compromising the accuracy of the generated code.
To address this, we propose a novel technique named \SEK(\textbf{S}elf-\textbf{E}xplained \textbf{K}eywords), which empowers an LLM for better code generation by extracting and explaining the key terms in the problem description with the LLM itself and ranking them based on frequency.
Comprehensive experiments across three benchmarks, i.e., HumanEval(+), MBPP(+), and APPS, with five representative LLMs, show that \SEK can significantly improve LLMs in code generation, yielding substantial and consistent gains. For instance, \SEK improves the Pass@1 of DeepSeek-Coder-V2-Instruct from 85.4\% to 93.3\% on the Humaneval benchmark. Further analysis confirms that \SEK enables the LLMs to shift their attention from low-frequency keywords to their corresponding high-frequency counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a two-stage prompting technique called “Self-Explained Keywords”, that improves the quality of code generated from a variety of LLMs. The technique primarily works by first inducing the model to produce descriptions of select keywords, then ranking these descriptions and finally appending them to the original context before proceeding with code generation. The paper suggests that the ideal keywords to select are low-frequency terms in the model training corpus that the model may have more difficulty understanding. The authors evaluate their method on 5 different LLMs across 3 major code generation benchmarks (and an additional variant of the HumanEval and MBPP benchmarks) and find that performance increases across various models.

### Strengths
- The paper presents a structured and domain-motivated approach to think about prompt refinement that I think also could be useful in other non-code domains as well. Particularly ones where there is some shared structure between instances or in the general process of solving the task that we can identify apriori.
- It seems possible that one could use this general approach to combine models that are specialized towards explanations with models specialized towards solving tasks in the target domain.
- I think the results point to the fact that many problems may be 'underspecified' and that models are capable of (self) improvement of the specification before solving the problem. The general approach proposed is elegant, simple and targeted.

Overall I think this is an interesting paper, there were a few things that made my score a bit lower that might be addressable by the authors during the discussion.

**Post-discussion update**

I've increased my score based on the updates to the papers from the authors.

### Weaknesses
 - **No evaluation of zero-shot CoT**: From what I can tell there is no evaluation of zero-shot CoT [Kojima et al, 2022], (aka "lets think step by step"). The proposed method seems similar in spirit to zero-shot CoT albeit more structured and tailored to code generation. The paper would be stronger if it benchmarked against that method, as it would provide a condition that is not dependent on the effect of demonstrations in the original CoT formulation and would allow readers to understand how much problem refinement models are able to do without the use of a specialized prompt.

- **Selecting number of beams=2 because SEK calls the model twice doesn't seem all that well motivated.** Beam search is significantly less costly than full generation so if the goal is to match compute it doesn't seem necessary to limit to just two beams. Since the beam search results are somewhat competititive with other methods, it would be helpful to readers to understand how this saturates as the number of beams increases. The  Wiseman & Rush 2016 citation for beam search experiemnts with beams=5 and beams=10. Could the authors shed some more light on their seelction and why?

- **Results bounds**
	- Table 1 does not show any result bounds like standard deviation or confidence intervals. The authors do present the ranges for the different sampled APPS sets in Table 6 in the appendix, but this should be brought into the main table to allow readers to see the variability of scores for that benchmark. 
	- Alternatively the paper would be stronger if it also presented with pass@k (where k > 1) to capture some of the variablity that may be present in each of the methods.
	- In particular the results in Table 4 would benefit from repeated sampling and error bounds to better understand the importance of the ranking step as the scores are somewhat close.

- **Low frequency assumption**
	- One area of the paper that I did not find particularly convincing was the assertion that the keywords worth explaining are low-frequency tokens *in the training corpus*. I couldn't really find any evidence for this presented in the paper, if I missed this then I'd certainly appreciate clarification. If not then I think the paper would be better served if this were framed as a motivating assumption. While I think the intuition that rarity may play a role is not unreasonable, it seems somewhat overstated as causative. To give an example, L043 "The term even digits rarely appears in code datasets, causing LLMs to misinterpret it as even numbers." — how do we know that **"even digits"** occurs rarely in training datasets (presumably compared to "even numbers")?
	- The prompt used to select "keywords" wouldn't necessarily bias towards selecting low frquency terms in the training corpus. It mainly tries to select and expand on key terms for the problem at hand and for generating correct functions

### Questions
- Could the authors provide more detail (and an example) on the construction of the full CoT prompts presented to the models (including demonstrations). One surprising result in Table 5 was the large drop in human-eval performance for GPT-3.5-turbo for CoT relative to the default setup. It would be helpful to readers to understand how the demonstrations used might impact quality of generation.
- Table 4 shows results for experiments for 4 different combination orders in order to determine the best one. But shouldn't there be 6? Abs_Func_Gen and Func_Gen_Abs seem to be missing. Why weren't these other combinations evaluated?
	- As an aside it would help to put "SEK (Abs_Gen_Func)" in the table to help the reader compare.
- How many keywords are extracted and how many explanations are generated? The motivation for ranking the keyword descriptions based on locality bias in LLMs is a factor I wouldn't have expected to be relavant over the short token spans of the examples shown so was surprising to see.
- Fig 5 case study. I may have misunderstood something, but I couldn't understand the description of the case study associated with figure 5. It suggests that the CoT result searches for the string "boredom" rather than "I", but I couldn't identify that bug. I transcribed all 3 solutions and found the default and CoT ones were correct and the SEK one was wrong (not correctly capturing the sentences). I've included the code I used below for the authors to examine and point out if i missed something. 

```py
def is_bored_default(S):
    # Split the string into sentences based on delimiters '. ', '?', and '!' 
    sentences = S.split('.') 
    sentences += S.split('?') 
    sentences += S.split('!') 
    # Remove empty strings from the list 
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()] 
    # Count the number of sentences that start with "I" 
    boredom_count = 0 
    for sentence in sentences: 
        words = sentence.split()
        if words and words[0].lower() == "i":
            boredom_count += 1 
    return boredom_count


def is_bored_cot(S):
    # Step 1: Initialize 
    count = 0 
    sentences = S.split('.') # Split by '.' first 
    # Step 2: Further split by '?' and '!'
    sentences = [sentence for sublist in [sentence.split('? ') for sentence in sentences] for sentence in sublist]
    sentences = [sentence for sublist in [sentence.split('! ') for sentence in sentences] for sentence in sublist] 
    # Step 3: Check each sentence 
    for sentence in sentences: 
        # Step 4: Strip leading/trailing whitespace and ch eck if it starts with "I" 
        if sentence.strip().startswith("I"): 
            count += 1 
    # Step 5: Return the count 
    return count


def is_bored_sek(S):
    # Split the string into sentences based on '.', '?', or '!' 
    sentences = [] 
    start = 0
    for i, char in enumerate(S): 
        if char in '.?!': 
            print("Appending", S[start:i+1].strip())
            sentences.append(S[start:i+1].strip()) 
            start = i + 1 
    # Count the number of boredoms 
    boredom_count = 0 
    print("Se", sentences)
    for sentence in sentences:
        # Check if the sentence starts with the word "I" 
        if sentence.startswith("I ") or sentence == "I": 
            boredom_count += 1 
    return boredom_count


print("is_bored_default")
print(is_bored_default("Hello world"))
print(is_bored_default("The sky is blue. The sun is shining. I love this weather"))
print(is_bored_default("The sky is blue. I think The sun is shining. I love this weather"))

print("is_bored_cot")
print(is_bored_cot("Hello world"))
print(is_bored_cot("The sky is blue. The sun is shining. I love this weather"))
print(is_bored_cot("The sky is blue. I think The sun is shining. I love this weather"))

print("is_bored_sek")
# Outputs 0
print(is_bored_sek("Hello world"))
# Outputs 0 instead of 1
print(is_bored_sek("The sky is blue. The sun is shining. I love this weather"))
# Outputs 1 instead of 2
print(is_bored_sek("The sky is blue. I think The sun is shining. I love this weather"))
```

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents SEK (Self-Explained Keywords), a straightforward approach designed to enhance the code generation capabilities of large language models (LLMs). SEK utilizes the LLM to identify and elucidate keywords from problem descriptions and ranks them based on frequency. The authors conduct extensive experiments to show that SEK aids LLMs in recognizing and clarifying essential concepts within problems, thereby improving the accuracy of generated code solutions.


I concur with the paper's motivation, recognizing that due to the long tail of training data, LLMs often misinterpret or miss problem-specific, low-frequency keywords during code generation, which compromises the accuracy of the generated code. The method outlined in the paper involves three steps: keyword extraction and explanation via prompt-based LLMs, rule-based keyword ranking, and enriched prompt input for the final code generation step. 


I maintain reservations about the first step, which depends on the LLM's capability to extract and understand keywords. This reliance on the LLM’s inherent abilities seems contradictory to the paper’s motivation. As noted in the paper, LLMs exhibit biases toward low-frequency text comprehension. Therefore, I remain my concerns for this step. The method needs a more generalized or innovative strategies to mitigate this issue, making it challenging to achieve broad applicability solely with constructed prompts. Have the authors investigated the performance of the LLMs specifically in extracting low-frequency keywords? Is there any observed bias? Given the known instability of LLM results, have the authors performed any experimental analyses or discussions on this issue? For instance, running the LLM multiple times, analyzing variations, and conducting separate experiments on low-frequency words to assess the LLM's effectiveness. I suggest that the authors consider using pre-defined keyword extraction dictionaries or tools alongside LLMs for more robust keyword extraction.


In the second and third steps (keyword ranking and prompt enrichment), the ranking method based on heuristic rules is not very flexible or portable and may become unreliable with updates. The concepts of these steps seem akin to Retrieval Augmented Generation (RAG). I recommend that the author consider enhancing these steps by integrating RAG principles. Using heuristic rules and external low-frequency dictionaries as knowledge sources within RAG could allow for a recombination of LLM and RAG to improve the ranking algorithm. Ultimately, this could enrich the prompt with more relevant retrieved context. I think using RAG may be more effective than relying solely on rule-based ranking because it is closer to current technology trends and makes the paper's approach more flexible.


Overall, although it seems that numerous experiments validate the method's effectiveness, the approach remains fundamentally simple, centered primarily around prompt engineering. It lacks substantial theoretical depth and appears to reiterate existing methods rather than presenting innovative solutions. I recommend that the author consider replacing heuristic rules with RAG and integrating existing keyword extraction tools or custom low-frequency keyword dictionaries to create a more adaptable system. Relying excessively on heuristic rules to enhance prompts could render the method cumbersome and challenging to apply to different datasets or application contexts.

### Strengths
a practical motivation for this paper and a good writing in the introduction section.
Extensive experiments in this paper.

### Weaknesses
Dependence on LLM's Existing Capabilities: The method heavily relies on the LLM's existing keyword extraction and comprehension abilities, which could perpetuate inherent biases, particularly with low-frequency text. The method proposed, such as prompt engineering and rule-based ranking, are not fundamentally novel and rely heavily on existing techniques, which may limit their impact in advancing the field.

### Questions
1. Did you explore the integration of RAG or similar methods into your approach?
2. Have you considered developing more advanced methodologies or theoretical frameworks at a higher level to enhance your proposed solution?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces **SEK** (Self-Explained Keywords), a pipeline to improve large language model (LLM) code generation by translating low-frequency keywords in the problem description into high-frequency natural language descriptions. The authors evaluate the effectiveness of SEK on three code generation benchmarks and claim that SEK provides substantial and consistent performance improvements.

### Strengths
- This paper presents a well-designed pipeline to address the issue of overlooking low-frequency terms in program descriptions due to the long-tail distribution present in LLM training data. The experimental results demonstrate that SEK effectively enhances code generation performance.

- The authors have conducted a wide spectrum of experiments, encompassing five leading LLMs, four baseline models, and three established code generation benchmarks. This extensive evaluation adds robustness and credibility to the findings.

### Weaknesses
 - **Simplistic Benchmarks:** The selected benchmarks seem relatively simple and may not adequately capture the real-world effectiveness of the proposed approach. To enhance the rigor and applicability of this study, incorporating more recent and realistic benchmarks [1,2] would be beneficial. This would strengthen the overall soundness and relevance of the paper. The benchmarks used, while established, do not inherently require the type of keyword-focused explanation that the proposed method provides. This raises concerns about whether the observed improvements are truly due to the method's ability to address low-frequency keyword issues or if they are simply a result of the method's overall approach to code generation. The benchmarks lack the complexity to fully test the method's ability to handle nuanced, real-world scenarios where low-frequency keywords are critical for understanding the problem.

- **Similarity to One-step CoT or One-shot Learning:** The SEK approach exhibits similarities with one-step chain-of-thought (CoT) and one-shot learning strategies. To better elucidate and highlight the advantages of SEK, I suggest conducting a simple experiment, which could ask a language model to rephrase the problem description using precise language. The rephrased description would then be fed back into the language model to determine if this simple rephrasing enhances performance as well as SEK does. The current evaluation does not sufficiently isolate the specific contribution of the keyword explanation component of SEK from the general benefits of rephrasing or additional context. The fact that the rephrased descriptions, when used directly for code generation, do not improve performance as much as SEK suggests that the method's strength may not be in the rephrasing itself, but in how the explanations are integrated.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
