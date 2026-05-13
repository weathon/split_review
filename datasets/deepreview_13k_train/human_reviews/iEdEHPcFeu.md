# AuPair: Golden Example Pairs for Code Repair

- Decision: Reject
- Scores: 6, 5, 5, 1

## Abstract
Scaling up inference-time compute has proven to be a valuable strategy in improving the performance of Large Language Models (LLMs) on several tasks without involving any fine-tuning. An example of such a task that can benefit from additional inference-time compute is self-repair: given an initial flawed response produced by the LLM, it is supposed to correct its own mistake and produce an improved response. We propose leveraging the in-context learning capability exhibited by LLMs to aid with self-repair. The key contribution of this paper is an approach to synthesise and select a golden set of pairs, each of which contains a problem, the initial guess produced by the LLM, and the consequent fix generated. Each golden example pair, or AuPair is then provided as an in-context example at inference time to generate a candidate repaired solution with 1-shot prompting; in line with best-of-$N$ the highest scoring response is selected. Given an inference-time compute budget of $N$ LLM calls, our algorithm selects $N$ AuPairs in a manner that maximises complementarity and usefulness. We demonstrate the results of our algorithm on the coding domain for code repair on 4 LLMs across 7 competitive programming datasets. The AuPairs produced by our approach provide a significant boost in performance compared to best-of-$N$, and also exhibit strong generalisation across datasets and models. Moreover, our approach shows strong performance as the inference-time compute budget $N$ is scaled up.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper deals with the problem of self-repairing the answers to an LLM’s responses. The authors claim the proposal of a general-purpose, domain-independent algorithm (according to lines 079--081) for improving an LLM’s responses.

### Strengths
The paper conducts an interesting empirical comparison of the proposed technique for self-repair in code repairing.

### Weaknesses
 - In line 079, the authors claim that they propose a general-purpose, domain-independent algorithm for self-repairing LLMs. However, later, in line 082, the authors state that they focus on code repairing. I find this very confusing. The authors must either give a second use case to support the claim about domain-independence, or remove the claim made in lines 079—081 and exclusively present code repairing as their aim.
- Continuing with my previous questions, the unit tests are an essential part of the pipeline – according to line 072, the fixes are evaluated on the unit tests. However, unit tests or other kinds of assertion statements are, in general, missing in the setting of detecting hallucinations (e.g., factual mistakes) in the responses of an LLM (e.g., as it is the case when asking a VLM questions on a specific image). Hence, I do not see how the proposed framework can be applied to other domains. Can the authors please clarify?
- In line 143, the authors state that a set \mathcal{C} of candidate guess-fix pairs is extracted using the methodology described in Figure 1. However, Figure 1 is high-level, giving no concrete details. Can the authors please be more specific of how the extraction algorithm works?  
- In line 072, it is unclear how the (optional) examples are used during the sampling process and in general, what is the purpose of these optional examples in the overall pipeline. Can the authors please provide further details? 
- In line 160, the authors state that a validation set is needed during the AuPair extraction process. However, in lines 082—083, this part is missing. Can the authors be very specific on what is exactly is needed as an input to their algorithm?  

The above issues make it difficult to the reader understand the paper and its contributions. However, I am happy to revise my score if the authors address/answer my concerns/questions.

### Questions
Please see my comments/questions in the above field. In addition: 
- Please provide a concrete running example, potentially extending/giving more information on the example in Figure 2. Please clarify how the unit tests look like, how the examples look like, how the candidate guess-fix pairs look like, how the validation set looks like. Even a toy example that demonstrates these notions would enhance readability a lot.      
- Please discuss how the method might be adapted or generalized to work in domains without clear unit tests or ground truth evaluations.
- Please provide a more detailed algorithmic description or pseudocode for the extraction process, in addition to the high-level overview in Figure 1.
- Please provide a clear list of all inputs required by the algorithm, including the validation set, and explain how each input is used in the process.
- Please position your work against SOTA on detecting/mitigating hallucinations in LLMs and VLMs. One indicative reference is "HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding", ICML 2024, which studies the problem of detecting hallucinations in VLMs.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper tackles the self-repair task in coding, by synthesizing a set of golden (problem initial guess, fix) pairs, to augment inference-time context when solving test examples. The proposed method shows to be effective across different programming tasks while having the computation overhead controlled.

### Strengths
Strengths
1. The paper tackles an interesting problem – coding repairs – and experiment on a wide range of datasets to provide its comphrensiveness and effectiveness.

2. The proposed method shows to be effective on a series of in-domain and out-of-domain, on weaker Gemma and stronger Gemini models, partially demonstrating its effectiveness.

3. The controlled compute budget (N LLM calls) alleviate worries in gaining increase with more compute.

### Weaknesses
1. The experimented setting somewhat already “reveals the answer”: as described in the paper “given a coding problem, its test cases, and …”, the test cases serve as a canonical correctness checker for model generations – one only need to execute model-generated code over the test cases to know if it’s correct or not. AFAIK the test cases should be assumed unknown at any point during the generation. This setup, where test cases are available for evaluating generated code during the repair process, significantly simplifies the task, potentially leading to inflated performance metrics. The model can effectively perform a form of test-driven development, iteratively refining its code based on immediate feedback from the test cases, which is not realistic in real-world scenarios where test cases are often unavailable during code generation.

2. Incomprehensive model selection: this paper experiments with Gemma and Gemini models in various sizes. However, neither Gemma nor Gemini are known to perform the best on coding tasks, their coding alternatives (e.g., CodeGemma) and better alternatives (CodeLlama, DeepseekCoder) should be considered to prove the effectiveness of the method. Otherwise, the paper should clearly state that the proposed method only applies to text-oriented LMs or weak coding LMs. The lack of evaluation on state-of-the-art coding models raises concerns about the generalizability of the proposed method. It is crucial to demonstrate that the method is effective across a wide range of models, including those specifically designed for code generation, to establish its robustness and practical applicability. Without this, the results may be limited to a specific subset of models and not be broadly relevant to the field.

3. It is unclear (from section 3) what evaluation metric is used in this paper, especially given that rigorous evaluation is important for coding tasks. From the description, it seems that “the number of unit tests passed” is the main metric. First, writing-wise, it’d be good to highlight (e.g., bold) the metric name to clearly inform the readers. Second, design choice wise, the “number of tests passed” do not correlate with the correctness extent of a program. A program should pass all test cases to prove its correctness; and “number of tests passed” will be more affect by the distribution/sufficiency of test cases (which analysis is not available in the paper) than the actual correctness of the model-generated program. The paper does not provide any analysis on the distribution and sufficiency of the test cases, which is critical for interpreting the results. The metric of “number of tests passed” is highly sensitive to the quality and coverage of the test suite, and without a detailed analysis, it is difficult to assess the true effectiveness of the proposed method.

### Questions
1. Could you explain how the method control the N LLM call compute budget? Because the experiments seem to control the sampling baseline to sample only N responses; but for the proposed method, it involves N AuPairs and then N fixes, so that would cause the compute to be 2N?

2. It is unclear what the green and blue blocks mean in Figure 1; similarly, what the purple block mean in Figure 3. Thus I’m not sure if I fully understand the figures.

2. I am curious on the types of fixes model learn to perform, have you observed any major catefogories, e.g., “fixing variable name copy errors”, “fixing logical computing errors”, etc.

4. As mentioned in the paper, AuPair is created on a held-out validation set. How would the proposed method apply when no held-out validations are available?

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
4

### Summary
This paper introduces AuPairs, which is designed to enhance the performance of LLMs on auto program repair (APR). The authors utilize each pair of _guess, fix_ in AuPairs as an in-context examplar to improve performance through in-context learning when providing more inference-time compute. The _guess_ is the initial solution generated by the LLM for a coding problem, while the _fix_ is a repaired code for the aforementioned _guess_. 

The process of AuPairs is as follows: 
First, the initial solution, or _guess_, for all problems in the training set is collected; then, a random sample of $k$ pairs from the candidate pairs (which are initially empty) is used as in-context exemplars to create the _fix_ based on each guess. Subsequently, if the test case pass rate (also defined as score) of the _fix_ exceeds that of the _guess_, the pair _<guess, fix>_ is added to the candidate pairs. Furthermore, if the _fix_ does not pass all cases, it is also converted into a _guess_. 

Ultimately, scores for each pair in the candidate pairs are calculated as a one-shot examplar on all guesses in the validation set, and the pairs are selected from high to low based on the average scores. Subsequently, the scores of all remaining pairs' guesses are reduced by the score of the selected pair (with any negative values being set to zero). This method allows for the selection of complementary AuPairs. During testing, each pair in AuPairs is used as a one-shot examplar on the test set. 

The contributions of this paper are as follows:
1. AuPairs have outperformed the performance of best of N in multiple scenarios.
2. With an increase in the inference budget, there is an improvement in performance.
3. Good results are achieved across different models and datasets.

### Strengths
1. The focal point of AuPairs is well-chosen. By leveraging in-context learning, the method enhances performance without the need for additional training.

2. The approach is ingeniously designed. In the PAIR GENERATION stage, the method creatively reuses imperfect _fix_ by transforming them into _guess_. Additionally, the AuPair EXTRACTION process, which identifies complementary AuPairs by subtracting the scores of selected pairs from those of unselected pairs, is particularly innovative.

3. The method’s effectiveness is validated across multiple models, with comprehensive experimental analysis.

### Weaknesses
1. The paper lacks comparisons with alternative baseline methods, as the authors compare only with the simple "best of N" approach. Prior work, such as Self-Repair[1], explores how varying the balance between feedback and repair affects performance under fixed inference attempts. Additionally, it would be valuable to compare AuPairs to methods that provide execution results before resampling fixes. Comparing with other methods that also use a fixed number of inferences would better demonstrate the strengths of the proposed approach.

2. The presentation of the experimental datasets appears overstated. While the authors mention the use of seven datasets, six of these are extracted from CodeContest[2]. While grouping by website categories may be suitable for analysis, I question whether this categorization should be emphasized as a primary contribution. Furthermore, all experiments focus on code generation benchmarks, lacking evaluations on code repair benchmarks like the self-repair section in Livecodebench[3] or the APR section in xCodeEval[4].

3. The conclusions regarding diversity are not sufficiently substantiated. The authors claim that AuPairs provide diversity without a trade-off in performance. However, in Figure 7(b), while diversity scores increase from Gemini-1.5-flash to Gemma-9B to Gemma-27B, performance scores of AuPairs show a decline, suggesting that the improvement in diversity may indeed come at a performance cost too.

4. The figures in the paper could be optimized for information density relative to their visual footprint.

### Questions
1. Why did you choose not to include the execution results of guesses directly within the prompts? Including these results could potentially provide more context and improve the model's performance by refining subsequent guesses.

2. Could you clarify the setup of your baseline method, "best of N"? Specifically, what information is provided during sampling, and what prompt is used? Understanding these details would allow for a clearer comparison with your proposed approach.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes an approach to self-repair the generation of LLMs for text-to-code tasks. The idea is to pre-compute an example bank of incorrect LLM attempts and its fixes (called AuPairs) from a dataset, then at inference time, select N AuPairs that best match the given utterance to form N 1-shot prompts for the LLMs. The paper shows that its approach out-performs the best-of-N approach on 7 competitive programming datasets using 4 variants of Gemini models. It also demonstrates that the approach generalizes across datasets and variants of Gemini models and scales with inference-time compute budget.

### Strengths
+ The paper addresses an important problem 

+ The paper is easy to follow

### Weaknesses
 - The title is confusing. The paper tries to solve text-to-code problems, where the model is given a task description and some test cases. The paper did not solve code repair problems, where the model is typically given a broken program and some test cases to generate the fixed program.  

- The evaluation is questionable. The paper did not report results using standard metrics (e.g., pass@k for varies k) and did not provide any comparison with other popular RAG-based approaches. The baseline best-of-N is weak, and its configuration is not clear (zero-shot?). 

- The approach may not be practical. To solve each task, it needs to make |C| LLM calls to rank all the candidates in C. 

- The paper overclaims that AuPair is a general and domain-agnostic algorithm. It is only evaluated on one domain. 

- The paper did not specify several parameters in the algorithms. The claim about composability is not clear. 

- The evaluation only shows the results for Gemini variants and missing results for other models.

### Questions
1. What is the definition of the score function? Is it the percentage of passing tests? 

2. In section 2.1, the discussion is vague. When do you stop generating the candidate pairs (i.e., what do you mean by “large”)? What is the size of C compared to the original training dataset D? What is the value k (the number of randomly sampled examples)? Did you try to control the generation so that each problem in D has a similar representation in C, or did you just do it randomly? 

3. In Section 2.2, for each problem in D_{val}, we need to make |C| calls for all the pairs in the candidate list C. This is extremely expensive. Can we use other ways to rank the candidates (e.g., sequence similarity)? 

4. In Section 2.2 step 3, why subtracting M by M_k ensures that complementary pairs are generated? Each element in M_k is simply the score of evaluating the pair c_k on D_{val}. The score did not specify which tests passed, so subtracting them did not make sense to me. 

5. In Section 2.2, why did you limit to 1-shot in the final prompt? Can’t we use a larger k? 

6. I don’t understand the reasons behind picking best-of-N as the baseline. How does your approach perform in standard pass@k metrics? How does your approach compare with other RAG-based techniques? 

7. In section 3, can you explain why we may have less than 32 AuPairs given that all datasets are quite large? 

8. In Section 3.1, can you provide more details on the best-of-N baseline. Did you use zero-shot? 

9. In Section 3.2, I think it is not fair to compare with random 1-shot. Can we compare your approach with other RAG techniques? Also, can you extend your evaluation beyond 1-shot prompts? 

10. Can you expand your evaluation to other open source and close source models?  

Other minor suggestions: In Figure 1, annotate the diagram with numbers and reference them in the caption. In Figure 2, explain why the score is 0.67 and 1.

### Soundness
1

### Presentation
2

### Contribution
1
