# ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain.
This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT.
To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation.
We first present \ourdata, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect $16,464$ real-world RESTful APIs spanning $49$ categories from RapidAPI Hub; (ii) instruction generation: we prompt \turbo to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use \turbo to search for a valid solution path (chain of API calls) for each instruction.
To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space.
Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval.
Based on \ourdata, we fine-tune LLaMA to obtain an LLM \ourmodel, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that \ourmodel demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. 
Our \ourmodel also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces ToolLLM, a whole pipeline for creating and evaluating instruction-tuned language models that can use tools.

The authors created ToolBench, an instruction-tuning dataset by i) collecting a large number of real-world APIs from multiple categories; ii) creating instructions with seed demonstrations and tool sets; iii) annotate the api call solution paths with ChatGPT.

They fine-tuned several baselines on ToolBench and evaluated them with the proposed ToolEval pipeline, which also uses ChatGPT to evaluate whether the solution path is successful and whether the solution path is better than the one annotated by ChatGPT.

Additionally, they also propose to use an API retriever and a tree-search algorithm (DFSDT) during inference.

### Strengths
1. The scale of ToolBench is unprecedented compared to previous tool learning datasets. It has more APIs, more tools, more task instances. This makes ToolBench much closer to real-world settings of tool-augmented language models.
2. The authors conducted extensive experiments to show that their instruction-tuning pipeline enables language models to generalize to new tools and new domains without seeing them in the fine-tuning dataset.

### Weaknesses
### 1. The current annotation/evaluation pipeline is not rigorous and may lead to false impressions about model’s performance.

ToolBench is entirely annotated by ChatGPT. I understand that the annotations of the instruction-tuning data don’t have to be perfect, but I think as a benchmark for evaluation, it should be held to higher standards.

ToolEval solely relies on ChatGPT to evaluate whether a solution path “passes” and whether it “wins” the solution path from ChatGPT.

While I appreciate the authors’ efforts in comparing ChatGPT’s evaluation with human subjects’, I think the current evaluation pipeline is problematic because of the following reasons:

- Many tool-related tasks can have a definite set of correct answers or correct solution paths. For these tasks, the real correct answers should be used to judge the correctness of generated answers. Relying on ChatGPT’s annotation of win rates and pass rates can lead to over-confidence about wrong answers that look satisfactory.
- ChatGPT (and other language models) as an evaluator is known to have order bias (gives preference to an option based on their order), egocentric bias (prefers its own outputs), length bias [1], selection bias [2]. It also chooses style over substance [3]. I would expect more discussion on if and how ToolEval mitigates these biases.
- The evaluation rules for pass rates and win rates seem too complex even for human annotators to follow, which severely undermines my confidence in your human evaluation results. According to Appendix A.5, the rules to determine whether a solution path gets a “pass” form a 3-layer decision tree with as many as 10 leaves and each decision in the tree requires some non-trivial and thorough examination of the instructions, the available APIs and the solution path. I would really love to learn more about your human evaluation process. For example, did the annotators only submit the final flag of pass/fail/unsure or did they also submit all the decisions they made to get to the final results? Is there any evidence that can show that human annotators were faithfully following your rules instead of relying on human cognitive biases? If the human annotations themselves were not reliable, nor would the correlation between human and ChatGPT be good enough.
- Win rates are computed by comparing model generation with annotations from ChatGPT+ReAct. Could inference algorithms that are more similar to the annotation pipeline (instead of better) lead to better results?

**Reference**

[1] Koo, Ryan, et al. "Benchmarking Cognitive Biases in Large Language Models as Evaluators." *arXiv preprint arXiv:2309.17012* (2023).

[2] Zheng, Chujie, et al. "On Large Language Models' Selection Bias in Multi-Choice Questions." *arXiv preprint arXiv:2309.03882* (2023).

[3] Wu, Minghao, and Alham Fikri Aji. "Style over substance: Evaluation biases for large language models." *arXiv preprint arXiv:2307.03025* (2023).

### 2. The evaluation results are constantly changing over time, making it very expensive and difficult to compare new methods and older baselines. This also ruins the reproducibility of the evaluation pipeline.

I appreciate the authors’ consideration about the temporal variability on RapidAI.

> *Considering the API’s temporal variability on RapidAPI and the infinite potential solution*
*paths for an instruction, it is infeasible to annotate a fixed ground-truth solution path for each test instruction. Moreover, when comparing different models, it is crucial to ensure they employ the same version of APIs during evaluation.*
> 

I think this is also part of the reason why they used ChatGPT as an evaluator instead of using ground truth annotation.

However, I still think it’s problematic.

First, people are not able to know roughly how good a method is by looking at the reported pass rates and win rates, because the reported results can only be compared with the results evaluated during the same time period.

Second, it makes evaluation much more difficult. As the authors pointed out, each evaluation run needs to use the same version of APIs to ensure fair comparison. This means every new method that needs evaluation on ToolEval must also run every baseline they compare to in a very short period of time. If some highly variable API were used (for example, APIs that query the availability of restaurants or realtime weather), this period could be as short as a few hours. This creates an extremely heavy burden for developers and researchers, because not only do they need to run all evaluation experiments multiple times, they also have to run them in parallel.

Therefore, at the very least, I would expect some qualitative analysis of the tool set that can point out how many task instances involve these temporally variable tools and how much temporal variability impacts the evaluation results over time.

I think a better solution to this problem might be creating a “snapshot” of the API call results at a certain time and release this snapshot with the evaluation suite. This way, it’s much easier to get reproducible results.

### 3. The comparison between DFSDT and ReAct.

Why isn’t DFSDT always better than ReAct? According to your description, it seems that ReAct is a special case of DFSDT where the branching factor is 1. Therefore, I expected DFSDT to be better than ReAct in most cases. In other words, the win rate for ChatGPT+DFSDT against ChatGPT+ReAct should be close to 100%. According to the first two rows in Table 4, that is clearly not the case. Is there some explanation on why that happened?

### Questions
How were ToolBench split into tuning and evaluation subsets? Could you explain more about this part?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper collected a new instruction-tuning dataset (called ToolBench) for improving LLM's tool-use capability. To construct ToolBench, the author collected more than 16k REST APIs from RapidAPI and constructed synthesized instructions based on these APIs. To automatically obtain the desired behavior of the LLM, the author prompted prompt gpt-3.5-turbo-16k. By finetuning LLaMA on ToolBench, the author showed that ToolLLaMA achieves higher score according to a ChatGPT evaluator than Text-davinci-003 and Claude-2 in ToolBench.

### Strengths
The paper is valuable to those who are trying to build LLMs that can use tools. ToolBench is a well-engineered dataset and is shown to be more diverse than prior datasets in Table 1.

### Weaknesses
1. There are lots of papers that studied how to instruction-tune an LLM for tool-use, like GPT4Tools (in NeurIPS 2023), Gorilla, ToolAlpaca, etc. The techniques adopted in ToolLLM, such as constructing instruction-tuning samples by prompting ChatGPT, is very standard and has limited novelty. The paper is mainly about applying a popular synthetic instruction generation pipeline to distill knowledge from gpt-3.5 and has almost no research value.

2. The author proposed "Depth First Search-based Decision Tree" (DFSDT) that seems to outperform ReAct prompting. However, the technique is closely related to self-consistency + CoT and Tree-of-thoughts. It is also unclear how DFSDT will perform for other types of LLMs not in the category of LLaMA / GPT / Claude.

3. The evaluation metrics are based on ChatGPT, which is highly unreliable and may favor models tuned with ChatGPT-prompted datasets. The author mentioned in Appendix A.5 (Paragraph "Comparing Human Evaluation and ToolEval") that `Our ChatGPT evaluator demonstrates a high agreement of 87.1% in pass rate and 80.3% in win rate with human annotators. `. This shows that there is **close to 20% disagreement** between human evaluation and ChatGPT evaluation. This is a large discrepancy and should not be ignored.

### Questions
How does the models in Table 4 compare with each other if we adopt human evaluation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
- The paper introduces ToolLLM, a framework to facilitate tool use capabilities in open-source large language models (LLMs). It includes data construction, model training, and evaluation components.
- A new instruction tuning dataset called ToolBench is constructed using ChatGPT. It contains over 16,000 real-world APIs from RapidAPI spanning 49 categories. The dataset covers both single-tool and multi-tool instructions.
- An automatic evaluator ToolEval is developed to assess tool use capabilities. It incorporates pass rate to measure executability and win rate to compare solution quality.
- By fine-tuning LLaMA on ToolBench, ToolLLaMA is obtained. Experiments show it matches ChatGPT's performance and generalizes well to unseen APIs. An API retriever is also trained to automatically recommend relevant APIs. ToolLLaMA demonstrates strong generalization on the out-of-distribution APIBench dataset, despite not being trained on it. This validates its capabilities on new domains.

### Strengths
Leveraging existing techniques in the literature, authors build a framework for developing models capable of tool use. This framework encompasses dataset building, model training, and model evaluation. The scope is comprehensive, and the execution is generally solid. 

The authors do a good job documenting and elaborating design decisions such as dataset filtering and issues with prompting with a limited context window. 

The authors make their artifacts (ToolBench, ToolEval, and model artifacts) publicly available so others can build on their work.

### Weaknesses
Most of the technical ideas in this work are from past works, with the exception of DFSDT, which is a simple application of DFS to prompting. In this sense, the current work's technical contribution is low.

### Questions
NA

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Tool utilization is an important capability of LLMs to extend their task scope. Although closed-source LLMs have achieved powerful performance by calling external tools, it is still important for open-source LLMs to enhance their capability in tool use. In this paper, the authors proposed ToolLLM to facilitate the large language model to master 16,000+ tools. Moreover, the contributions of this paper can be summarized in three parts: 1) ToolBench, a benchmark which generate instructions involving different tool utilization; 2) a depth-first search-based decision tree algorithm is introduced to enhance the capability of LLMs in tool utilization; 3) an evaluation platform called TaskEval. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. Although tool utilization has received much attention in LLM applications, building a standard benchmark is still challenging. To address this, this paper releases a high-quality instruction tuning dataset, called ToolBench, which covers many different tools.
2. Based on the constructed ToolBench, this paper also designs a strategy for solution path annotation, which uses a depth-first search-based decision tree to search for a possible valid path.
3. Experimental results validate that tuning LLMs with generated samples can effectively improve performance. 
4. The writing of this paper is good and easy to follow.

### Weaknesses
1. This paper introduces TaskEval, which encompasses two metrics, *Pass Rate* and *Win Rate*. Specifically, *Pass Rate* detects whether LLM can successfully execute user instructions, and *Win Rate* is designed to judge which solution path is better for a given instruction. However, to some degree, I think these metrics still have some deficiencies and cannot efficiently the capability of LLMs in tool utilization. For example, *Pass Rate* can only reflect LLM whether can execute user instruction. Sometimes, powerful LLMs (e.g., ChatGPT) can always generate answers for any user instructions without any tool use, and besides, the hallucination of LLMs can also let it generate some executed but counterfactual answers. Besides, *Win Rate* can only reflect the capability of different LLMs, not their ability of tool utilization. Even two LLMs without tool utilization (e.g., ChatGPT v.s. LLaMA-7b), will also demonstrate differences in performance. Therefore, I think the proposed metrics can only reflect the capability of LLMs but not their tool-use ability. Of course, I also admit that it is challenging to build such a metric since there have been no metrics in this area before.
2. I appreciate that the paper releases a high-quality dataset in this area. However, it will be better to provide a detailed statistical of this dataset (e.g., distribution in domain, error analysis).

### Questions
1. In the design of solution path annotation, authors prefer to use DFS instead of BFS. However, DFS could also possibly backtrack and search multiple answers if it does not obtain a valid path. So, any experiments to prove the cost of DFS to find a valid path when compared with BFS?
2. This paper mainly uses RapidAPIs for training. So is the fine-tuned ToolLLaMa suitable or adapted for APIs in other sources/formats (e.g., Pytorch/Tensorflow/HuggingFace in Gorilla, ChatGPT plugins)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
