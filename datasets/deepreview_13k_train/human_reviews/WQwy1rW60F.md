# LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
State-of-the-art large language models (LLMs) are now claiming remarkable supported context lengths of $256k$ or even more. In contrast, the average context lengths of mainstream benchmarks are insufficient ($5k$-$21k$), and they suffer from potential knowledge leakage and inaccurate metrics, resulting in biased evaluation. This paper introduces \nameshort, a challenging long-context benchmark with five length levels ($16k$, $32k$, $64k$, $128k$, and $256k$) reaching up to $256k$ words.
\nameshort features two main tasks, single-hop QA and multi-hop QA, comprising 11 bilingual datasets. The design of \nameshort has incorporated three key techniques, namely confusing facts insertion (CFI), keyword and phrase replacement (KPR), and keyword-recall-based metric design. 
The advantages of \nameshort include controllable evaluation across context lengths, challenging test instances with confusing facts, mitigated knowledge leakage, and more objective evaluation. 
We evaluate 15 LLMs on \nameshort and conduct ablation studies on the benchmarking techniques. The results reveal that:
(i) Moonshot-v1 and recent large-scale open-source models, such as Qwen-2.5-72B and Llama-3.1-70B, achieve the highest performance on \nameshort, particularly at lengths below $64k$.
(ii) Models exhibit distinct score trends. For example, GLM-4-9B-128k, Yi-6B-200k, and Llama3-8B-1M exhibit a relatively gentle degradation of performance, but their absolute performances may not necessarily be higher than those of LLMs with shorter context lengths. (iii) LLMs' performances can significantly degrade in the presence of confusing information, especially in the pressure test of ``needle in a haystack''. (iv) Issues related to knowledge leakage and inaccurate metrics introduce bias in evaluation, and these concerns are alleviated in \nameshort.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new LLM eval benchmark called LV-Eval to assess LLMs longer-context QA capability up to 256k words. LV-Eval incorporates a few techniques (e.g., confusing facts insertion, keyword manipulation) and adopts a new eval metric, which provides better/more reliable LLM evaluation. Authors conduct experiments on 15 different LLMs and demonstrate how performance can vary significantly in different testing scenarios.

### Strengths
1. A new dataset that could potentially benefit the community
2. Paper presentation is overall clear
3. The proposed benchmark construction method is overall reasonable

### Weaknesses
The quality (and usefulness) of proposed benchmark is not fully evaluated. How do state-of-the-art LLMs and human (both domain experts and lay people) perform on this dataset? Does this benchmark capture LLM's full capability (other than knowledge extraction/manipulation capabilities for the QA tasks)? In multiple places in the paper, the authors mention human interventions (e.g.,  Line 269, “ask human annotators to resolve any conflicts in generated facts”), more analysis/discussions on the human annotation qualities are needed. 

The second limitation is its construction process is not very clearly discussed. For example, around line 254, the authors mention that “For each length level, we sample distracting documents one by one until the cumulative word count meets the desired length level“, how does the distracting document sampling work exactly? Furthermore, as mentioned in the previous limitation, for each place where human annotation/intervention is involved, more discussions (e.g., # of annotator, annotation guideline, human annotation agreement numbers, etc) are needed. I would recommend authors moving some part of current Appendix section B details to the main text. 

Finally, as mentioned by the authors in the limitation section, the current benchmark only include QA tasks. As a result, the proposed new evaluation metric also only targets short-form answers (compared to long-text generation). A natural question is that what if we use another LLM auto-rater to judge if two answer strings match semantically (instead of the lexical based methods).

### Questions
Please refer to the questions in the above weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors propose a long-context benchmark dataset for Large Language Models, with 5 gradually increasing length levels - 16k, 32k, 64k, 128k, and 256k tokens. The datasets consists of single-hop and multi-hop QA examples. The dataset was constructed using techniques such as content mixing up, keyword and phrase replacement and confusing facrs insertion. Authors have also conducted evaluation of 15 LLMs on the proposed benchmark. The insights from this evaluation includes: 1) Moonshot-1 and Qwen2.5-72B and LLaMA-3.1-70B achieved top performance; 2) Within the group of LLMs with 6-9B parameters, GLM-4-9B achieves the best results; 3) Score trends on various length levels differs substantialy between LLMs.

### Strengths
1. The dataset design approach with 3 options for confusing evaluated LLMs allows to take a broader look on LLM capabilities in dealing with potentially out-of-distribution content. This could be a substantiall addition to the set of benchmarks for thorough examination of LLMs in the context of their generalization.
2. 5 different length levels allows to precisely point out how model is able (or unable) to recall information from different parts of the context.
3. The inclusion of bilingual datasets helps assess the efficacy of long-context recall and understanding in two vastly different languages,
4. Authors evaluated multiple open-source LLMs with various context window sizes. This helps to assess the efficacy of different approaches to increasing the context window size for different models.

### Weaknesses
1. The conducted evaluation of LLMs on the LV-Eval benchmark included only 3 closed-source models. It is even more confusing that among those 3 models 2 are very outdated versions of GPT-3.5 and GPT-4. This paper would immensely benefit from inclusion of at least relatively recent closed-source LLMs, such as GPT-4 with 128k context window (which was released almost a year ago to this date), along with Anthropic Claude, which shows remarkable performance in long-context recall. The argumentation of high-cost is slightly confusing - particualrly most recent closed LLMs have been much less expensive compared to their previous versions. This might not apply to some models from Anthropic, but it certainly does apply to GPT-4. The price of GPT-3.5 with 16k context window was 3$ per 1m tokens, for GPT-4 is was 30-60$ per 1m tokens, while most recent GPT-4o pricing is 2.5$ per 1m tokens.
2. Confusing Facts Insertion relies entirely on GPT-4 internal concept of a "confusing fact". This yields a problem of data leakage - GPT-4 may have an unfair benefit to other models on this benchmark.

### Questions
1. Do you believe that using GPT-4 in confusing fact generation *will not* result in GPT-4 having an unfair advantage on this benchmark? If so, why?

2.1. Have you measured an inter-annotator agreement during annotation for CFI and KPR? 

2.2. How many annotators have seen each example? 

2.3. Have you rejected any annotations due to disagreement between annotators?

### Soundness
3

### Presentation
4

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
The paper's about LV-Eval, a fresh test to see how well big language models get long contexts. It's got five levels of length and covers two types of question-answering in 11 different languages. They mixed in some tricky stuff like made-up facts and swapped out keywords to make it harder. They tried it on 15 models and saw how they did, especially when things got confusing.

### Strengths
1. It's got a good range of lengths, which is key for seeing how models handle long texts.
2. It's not just English—it's got Chinese too, so it's more useful for different models.
3. They tried new things to make the test harder and stop models from cheating with common knowledge.
4. The scoring is more focused on the important bits of the answer, which makes it more accurate.
5. They shared all the data and code, which is cool for transparency and building on their work.

### Weaknesses
1. It's mostly about question-answering, which might not cover everything we need for understanding long texts. The focus on question-answering, while important, neglects other crucial aspects of long-context understanding, such as summarization, coherent text generation, and complex reasoning tasks that go beyond simple fact retrieval.
2. Testing some models is pricey, so they couldn't check out all the new ones. The computational cost of evaluating large language models on long contexts is a significant barrier, limiting the breadth of models that can be assessed, potentially missing important insights from newer architectures or fine-tuned models.
3. They're still relying a lot on people to check the tricky parts, which takes time and can be off. The reliance on human annotators for tasks like verifying counterfactual information and key-phrase replacements introduces subjectivity and potential inconsistencies, which could affect the reliability and reproducibility of the benchmark.
4. There's a chance models could just learn the test, not actually get better at understanding. The risk of models overfitting to the specific structure and content of the benchmark is a valid concern, potentially leading to inflated performance scores that do not reflect genuine improvements in long-context understanding.
5. Models had a hard time with the confusing stuff, so maybe the test needs more of that. The observation that models struggle with counterfactual information and key-phrase replacements suggests that the benchmark could be further enhanced by incorporating more challenging instances of these types of confusing information.

### Questions
1. How do these results compare to other tests, and does that tell us something about how well they do in the real world?
2. Can the authors walk us through how they checked the tricky parts and if there's a way to do it by machine?
3. What does it mean if models use common knowledge instead of the text, and how can we fix that for future tests?
4. Do models do as well on LV-Eval as they do on real-world tasks like summarizing or chatting?
5. Are there certain types of long-text jobs where LV-Eval is really good or bad, and how could that change future tests?

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
4

### Summary
The paper introduces LV-Eval, a long-context benchmark specifically designed to evaluate language models across a range of text lengths, reaching a maximum of 256k words. This benchmark encompasses two primary tasks: single-hop and multi-hop question answering (QA), and it utilizes a total of 11 bilingual datasets to enhance its robustness. To effectively assess model performance, LV-Eval incorporates three key techniques: confusing fact insertion, keyword and phrase replacement, and a keyword-recall-based metric design. The experiments conducted on this proposed long-context benchmark yield several significant findings, providing valuable insights into the capabilities and limitations of various LLMs in handling extended contexts.

### Strengths
1. The structure of this paper is coherent and well-organized, facilitating ease of reading and comprehension.
2. This paper presents the LV-Eval benchmark, which has the potential to foster further research in the area of long-context modeling.
3. The thorough experiments conducted in this paper provide valuable insights that assist readers in selecting the most suitable LLMs for various real-life applications and scenarios.

### Weaknesses
1. The contributions of this paper are somewhat limited in scope. While the techniques of confusing fact insertion and keyword/phrase replacement for data augmentation may be useful, they are relatively straightforward and lack significant innovation. The confusing fact insertion, for instance, seems to rely on a simple substitution of facts, which may not effectively challenge the model's reasoning capabilities in complex scenarios. Similarly, keyword/phrase replacement, while useful for surface-level variations, might not capture the nuances of semantic understanding required for long-context tasks.
2. To emphasize the contributions of the proposed benchmark, it would be beneficial to compare LV-Eval with more recent long-context benchmarks, such as “XLBench: A Benchmark for Extremely Long Context Understanding with Long-Range Dependencies” and “Loong: Benchmarking Long-Context LLMs with Extended Multi-Doc QA.” Such comparisons would provide a clearer context for evaluating the effectiveness and relevance of LV-Eval within the current landscape of long-context modeling. Without a detailed comparison, it's difficult to ascertain the unique advantages of LV-Eval over existing benchmarks, particularly in terms of the types of reasoning and understanding it assesses.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
