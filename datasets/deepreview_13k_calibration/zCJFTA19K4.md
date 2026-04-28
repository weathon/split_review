# Token Alignment via Character Matching for Subword Completion

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Generative models, widely utilized in various applications, can often struggle with prompts corresponding to partial tokens. This struggle stems from tokenization, where partial tokens fall out of distribution during inference, leading to incorrect or nonsensical outputs. This paper examines a technique to alleviate the tokenization artifact on text completion in generative models, maintaining performance even in regular non-subword cases. The method, termed \emph{token alignment}, involves backtracking to the last complete tokens and ensuring the model's generation aligns with the prompt. This approach showcases marked improvement across many partial token scenarios, including nuanced cases like space-prefix and partial indentation, with only a minor time increase. The technique and analysis detailed in this paper contribute to the continuous advancement of generative models in handling partial inputs, bearing relevance for applications like code completion and text autocompletion.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a token alignment model to apply in auto-completion task. The proposed method is described well and tested in the code generation task. There are some improvements recommended due to connection to literature and showing evidence that there is a problem that the paper addresses beyond the application of the LMs in code generation. The authors are referred to decoding literature in LM and sequence models in previous tasks for a fair comparison.

### Strengths
Interesting approach to improve efficiency in code generation.

### Weaknesses
The main problem of this paper is that there is no evidence or support that this problem exists, and caused by subword misalignment. 
Related work do not exactly align with the problem studied and there is no discussion why authors do not find evidence on the problem they choose to address.
Novelty of the proposed model is not clear.

### Questions
Can the authors find or add in their study evidence through actual experiments on the problem they propose to solve?
There are many variants of beam search that could do hierarchical subword/word generation. How do this approach differ from the existing methods?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method for text completion in large language models (LLM) from incomplete tokens in prompts. The method uses an algorithm to backtrack generated tokens for the completion of sub-words.  The main contributions are: i) method for identification and processing of incomplete tokens, and ii) comparison of the proposed method with byte-pair-encoding (BPE) baselines on code and natural language processing (NLP) benchmarks. The proposed method shows competitive results compared to the baseline.

### Strengths
- The proposed method  tackles issues with the text completion in LLM with a small latency overhead.
- Clear description of the proposed approach.  
- The authors perform a comparison of the proposed approach on code and NLP benchmarks.

### Weaknesses
 - It is not clearly described the background knowledge needed to motivate and position the proposed method in the literature.
- It is not clearly described the alignment task and the relation to code and NLP.
- A possible extra contribution can be the addition of a statistical significant test of the results.

### Questions
Please address the following questions during the rebuttal:

- Please elaborate in the background used to develop the proposed method.
- Is the alignment task based on fine-tuning a model or in-context-learning? Could you elaborate more on differences and benefits, compared to your method. 
- Could you elaborate on the selection and importance of hyper-parameters? such as backtracking B.
Is the selected baseline a strong proposal compared to other related work on fine/instruction tuning or character-based models? 

Extra:

Please add related-work/literature context to the introduction and methodology sections

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with problems arising from LLM prompts ending with incomplete subword tokens. This is an issue for use cases involving autocompletion, such as code generation. The authors propose a new decoding algorithm to handle partial tokens. The algorithm backtracks to a previous full token, then decodes the subsequent token while limited to only generating tokens that start with the partial token. This enables the model to use next-token predictions for complete tokens within its vocabulary, while ensuring that the resulting model output still aligns with the partially generated user input. The authors outline several classes of common partial token occurrences (e.g. natural language subwords, space prefixes, contiguous spaces in code) and construct evaluation data for testing generation from partial tokens for each class. They show that their backtracking algorithm improves performance across natural language and code generation datasets, with limited increased latency during decoding.

### Strengths
**-- 1. The problem of partial tokens is important and neglected –**

The authors have highlighted an important issue with this work. The effect of tokenisation on recent LLMs has not been sufficiently studied, and partial tokens might well be an issue for common LLM use cases like code generation. 

**-- 2. Method is simple and effective –**

The token alignment algorithm is an intuitive solution to the studied problem. It is easy to implement for existing LLMs, so it could realistically be used and adapted by practitioners. The reported results also look very good (large gains on some of the datasets), so I do see this work being useful for future research.

**-- 3. Useful categorisation of partial token scenarios –**

The authors outline a categorisation of the different types of common partial token errors. This in itself is a useful contribution, as it highlights the real-world use cases that cause problems.

### Weaknesses
 **-- 1. Uncertainty around backtracking steps --**

The paper is somewhat unclear about the method of backtracking multiple tokens (B in Algorithm 1), so I would ask the authors to clarify this. The introduction mentions “Our approach involves backtracking to the last complete tokens”, which is how I understood the method initially. But later it is suggested that the method backtracks multiple tokens (B = 3 tokens), and not just one token back.

I am not sure why backtracking 3 tokens would work better than 1, as found in the ablation study. Wouldn’t that give the model less context unnecessarily, given that 1 token back is all we need to get to a complete token?

**-- 2. More details on increased latency --**

The paper would be improved by a more detailed explanation of the increased computational complexity introduced by token alignment. I appreciate that the authors have included a whole subsection on this topic, but I would suggest shifting the focus of the subsection to matters that are practically informative. What is the average added latency, in ms and percentage? This is mentioned, but the authors should include the relevant hardware details for reference as well. Increased latency would be a primary real world concern for practitioners.

**-- 3. Framing of the problem --**

The problem of partial tokens could be presented more accurately in some instances. For example, at the end of page 3 the authors suggest that subword tokens of linguistic words like “banana” (“banan” or “bana”) could lead to issues. I think it would be best to cite work on this, or prove this experimentally? Linguistically unsound subword tokenisations are present in every LLM, yet they work well in most cases, presumably because there is enough data for models to learn how these subwords combine to form words (e.g. on https://platform.openai.com/tokenizer the word “bananas” is segmented “ban-anas”.)

The reported results could be viewed as proof that this is an issue, but for that it would be useful to include more examples of where token alignment helps e.g. can models autocomplete “bana” as “bananas” given sufficient context? Does token alignment allow them to do this?

The same holds for the other partial token categories.

### Questions
**-- Questions --**

1. How does your work differ from this paper? https://aclanthology.org/D19-1507.pdf It seems like they are using the same backtracking algorithm (see Section 4), but testing it with different models and datasets.
2. Will you release your evaluation datasets publicly?
3. Section 2, end of paragraph 1. How does subword regularisation increase inference latency?
4. What model’s tokeniser was used for the examples in Figures 1-3? If these examples were constructed by hand, this should be mentioned.

**-- Typos: --**

1. Tables 1-3 have incorrectly boldfaced results that are lower than comparable results (e.g. Table 1, all 3 baselines results for LLaMA with token alignment are incorrectly bold).
2. Section 1, paragraph 3: ’incomplete token “sys” in Figure 2’ -> ’incomplete token “re” in Figure 2’ 
3. Section 1, paragraph 4 fix unclear wording: “with an average increase of only 3-7 ms for using token alignment, in addition to the number of backtracked tokens”.
4. Section 3, paragraph 2: fix notation “where N is the number of tokens we need to backtrack” -> “where B is the number of tokens we need to backtrack”.
5. Section 3, paragraph 4: “to avoid unnecessary the trie lookup” -> “by avoiding unnecessary trie lookups”.
6. Section 4, paragraph 3: “it is general quite hard” -> “it is generally quite hard”.
7. Fix last sentence on page 4: “the model always obvious contiguous”.
8. Section 5, paragraph 1: fix “for each case described in Section 4 show”
9. Section 5, paragraph 1: “handles the constrain due to all such cases” -> “handles the constraint…”
10. Section 5, paragraph 2: fix unclear wording “processing publicly available datasets to their corresponding variants”.
11. Section 5.2.1, paragraph 3: “token alignment can be use in all cases” -> “t token alignment can be used in all cases”.
12. Section 6.2, paragraph 2: fix unclear wording “opportunities to mark some token as beginning of pretoken as building time”.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explored handling partially labeled complex tasks in generative models. Through token alignment, improvements in various scenarios were demonstrated.

### Strengths
The proposed token alignment method could be combined with multiple techniques, such as subword regularization. 

The method presented was meaningful for code completion and text output directions.

### Weaknesses
In terms of prefix-indentation splitting, the results of the proposed method still lagged behind the baseline. 

The method introduced a certain time delay. 

Prompts affected the results.

### Questions
1. The outputs of LLMs were uncertain. Even a minor change in a prompt could lead to variations in the output. During the use of prompts in the paper, was the specific impact of the prompt considered?

2. Given the powerful In-Context Learning capabilities of large language models, it would be worth exploring whether adding relevant knowledge to the prompt could further enhance the proposed method.

3. Was there any consideration that an excessive amount of code data in the dataset might dilute the pre-trained knowledge in LLMs, impairing code generation capabilities?

4. How did the proposed method perform in multilingual or cross-lingual scenarios?

5. The paper mentioned "token healing." Could there be a detailed comparison between "token alignment" and "token healing" in terms of performance across different datasets and application scenarios? What were the pros and cons of these two methods when dealing with partially labeled issues?

6. In which areas did "token alignment" excel? Were there scenarios or applications where other methods might be more appropriate?

7. For long texts or texts exceeding the model's maximum input length, did the "token alignment" method maintain its effectiveness? In such cases, was there a need to adjust or optimize the method?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
