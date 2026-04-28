# Adaptive Tool Use in Large Language Models with Meta-Cognition Trigger

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Large language models (LLMs) have demonstrated remarkable emergent capabilities, reshaping the landscape of functional tasks by leveraging external tools to tackle complex problems, such as those requiring real-time data or specialized input/output processing. Existing research primarily focuses on equipping LLMs with a broader array of diverse external tools (e.g., program interpreters, search engines, weather/map applications) but overlooks the necessity of tool usage, invoking external tools indiscriminately without assessing their actual need. This naive strategy leads to two significant issues: 1) increased latency due to prolonged processing times, and 2) potential errors arising from communication between LLMs and external tools, resulting in faulty outputs. In this paper, we introduce a concept we term meta-cognition as a proxy for LLM self-capability, and we propose an adaptive decision-making strategy for invoking external tools, referred to as MeCo. Specifically, MeCo focuses on representation space to capture emergent representations of high-level cognitive phenomena that quantify the LLM's meta-cognitive scores, thereby guiding decisions on when to use external tools. Notably, MeCo is fine-tuning-free, incurring minimal cost, and our experiments demonstrate that MeCo accurately detects the model's internal cognitive signals. More importantly, our approach significantly enhances decision-making accuracy in tool use for multiple base models across various benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses a practical problem in LLM tool use - when should models actually call external tools versus use internal knowledge. Current approaches tend to call tools indiscriminately, leading to increased latency and errors. The authors propose MeCo, which uses representation engineering (RepE) to detect "meta-cognition" signals that indicate whether a model needs external tools.

### Strengths
The problem identification and motivation are excellent. The authors clearly articulate why indiscriminate tool use is problematic and provide compelling examples. The empirical results are strong, showing an 11% improvement in accuracy across various benchmarks. The approach is also practical - it requires no fine-tuning and can be easily integrated into existing systems.

### Weaknesses
I am unsure of any new technical details beyond just applying an existing RePe research to tool use. While the authors frame this as detecting "meta-cognition", it's functionally very similar to previous work on detecting other concepts like honesty or confidence. The main innovation seems to be in the framing rather than the technical approach. 

The decision mechanism is overly simplistic, using basic thresholds on the meta-cognition scores without any principled way to set these thresholds. There's no consideration of different tools having different costs or risks, or of the model's confidence in its decisions--which seems quite relevant here.

### Questions
Que: How does detecting "meta-cognition" differ technically from detecting these other concepts? The paper shows strong empirical results - is this because meta-cognition is particularly well-suited to RepE detection compared to other concepts? Are there any such insights in the results?

### Soundness
3

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
This paper introduces "MeCo," a meta-cognitive mechanism designed for large language models (LLMs) to adaptively determine when to invoke external tools or rely on internal knowledge. The framework centers on "meta-cognition" to gauge LLMs' self-assessed capability to handle queries, with the goal of minimizing unnecessary tool usage, which may increase latency and errors. Through the representation of high-level cognitive phenomena, MeCo detects internal cognitive signals without fine-tuning, using a meta-cognition probe trained on contrastive instructions to determine when tool engagement is needed. Experimentally, MeCo improves decision-making accuracy in adaptive tool use and retrieval-augmented generation tasks, surpassing baseline approaches.

### Strengths
Meta-Cognition Trigger Mechanism: The paper introduces a meta-cognition-oriented trigger mechanism for large language models (LLMs), which enables models to assess their own capabilities and invoke external tools only when needed. This approach optimizes efficiency by minimizing unnecessary tool usage​.

Policy Utilization Effectiveness: By integrating meta-cognition evaluations into decision-making policies, the approach improves decision accuracy, proving more effective than prior methods in guiding when and how tools are engaged​.

Generability: The model demonstrates strong empirical adaptability across varied scenarios, confirming the robustness and wide applicability of its meta-cognitive strategy in different environments​.

Benchmark Introduction: The paper establishes a new benchmark, MeCa, to evaluate meta-cognitive strategies in LLMs, setting a valuable standard for future research in adaptive tool use and Retrieval-Augmented Generation (RAG) processes​

### Weaknesses
Simplified Benchmarks: The paper primarily evaluates its approach on benchmarks that may not fully reflect real-world complexity. This can limit the broader applicability and relevance of its findings in practical scenarios.

Underexplored Limitations of Meta-Cognition Scoring: While the meta-cognition approach is promising, the paper does not deeply address cases where this scoring might fail or where it could lead to suboptimal decisions, particularly with ambiguous or highly nuanced queries.

Lack of Robust Comparative Analysis: The analysis lacks a detailed comparison against alternative adaptive approaches. Without this, it’s challenging to assess how the proposed model's efficiency and accuracy improvements stand relative to other recent innovations in adaptive retrieval or tool use.

Scalability Concerns in Diverse Operational Environments: The paper suggests that the model generalizes well but does not provide sufficient evidence to validate this across varied and complex environments, where scalability might be affected.

### Questions
How does MeCo handle real-world scenarios with complex or ambiguous questions? Were any experiments conducted in more open-ended, unstructured environments, and if so, what were the results?

Can the meta-cognition scoring approach manage ambiguous or nuanced queries that may require partial or iterative tool engagement? If not, how does the system handle such edge cases?

Have the authors tested MeCo’s scalability in more diverse and high-stakes environments where model latency or tool usage frequency could impact outcomes significantly?

How does MeCo compare to other adaptive approaches like reinforcement learning-based or rule-based systems? Were any such methods considered for direct comparison, especially for efficiency or accuracy?

Could the authors clarify any limitations they see in the MeCa benchmark? Are there aspects of meta-cognitive performance that the benchmark doesn’t capture, and are there plans to address them?

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
The paper focuses on the decision making whether an LLM should use an external tool to answer a user query. The authors design a metric to help an LLM recognize its own limits, when answering such queries and if a request is beyond its abilities to decide to use an external tool or RAG. The mechanism for the metric is based on PCA. The authors fine-tune various models to improve the use of that metric with the help of an existing benchmark/dataset (Metatool) as well as two self-created datasets. All three datasets are used to evaluate the resulting models.

### Strengths
* proposition of a new metric to help an LLM judge its own capabilities
* two new datasets for judging whether the use of external resources in the forms of tools or RAG is necessary

### Weaknesses
The paper lacks focus and flow. The components are only sometimes clearly described and the text contains several contradictions (no fine-tuning according to abstract, but is actually used), for example the decision process shown in the motivation figure is never discussed (and might be wrong) or some discussion seems to lack details like the determination of thresholds. This makes it hard to follow and to clearly grasp, what the contributions are.

* the decision making process presented in Figure 1 is not discussed in the text itself
* section 6: abstracts states that no fine-tuning is used, but apparently fine-tuning is used to improve the generation of the meta-cognition score
* Figure 5: I think the use of different x axis ranges for original model and the fine-tuned model is not great for the comparison of the two.
* size of both self-generated datasets seems kind of small
* number of evaluated models seems kind of small, with the used models having small sizes, which makes me question whether the results would generalize
* table 2: methods does not always perform better (usually one highlights the best performing entries):
  * llama3 with fine-tuning, with context: P_Yes 70%
  * fine-tuned Llama3 model shows not much differences between the three methods
  * llama3 with fine-tuning, without context: Naive 80% (same as MeCo)
* section 6: no discussion on deriving the thresholds for the differentiation
* no ablation studies

additional issues:
* line 142: PCA is never explained nor written out. No reference is provided either.
* Figure 2 is never referenced in the text
* section 4, discussion of MeCa-Tool dataset should use past tense, since it was already assembled, and it does not seem to be a synthetic dataset generator
* section 5, line 332: no reference for CoT
* line 343: "performance references" - apparently those references are missing
  * maybe the whole paragraph was included by accident, since it rephrases the same argument from the previous paragraph
* table 3: placement is not great, since the surrounding text is unrelated
* section 6: "This discrepancy occurs because the meta-cognition score for Yes/No tokens depends not only on the meta-cognition score itself but also on the token embedding."
  * sentence does not make much sense: the score depends on itself as well a token embedding
* prompt examples on pages 19 to 21 should be explained or at least given some context

* minor issues:
  * oversights:
    * line 45: "Lu et al. (2024); Wu et al. (2024)" - remove brackets around the year, and add brackets around the whole citation; should be fixed by using the correct cite command
    * Figure 1, Query: "reviews form the" - it should probably be "from"
    * line 106: "Bricken et al. (2023); Levinstein & Herrmann (2024)" - remove brackets around the year, and add brackets around the whole citation; should be fixed by using the correct cite command
    * line 107: "(Zou et al., 2023; Liu et al., 2023a)" - wrong cite command, here it should actually be "those by Zou et al. (2023) and Liu et al. (2023a) have"
    * line 162: "provided in Section C." - You probably mean "Appendix C".
      * similar for lines 191, 252, 329, 334 and 340
    * lines 234/238: "where LLM assistant" - "an" or "the" is missing before LLM
    * line 253: "To curate MeCa-Tool dataset" - missing "the" before MeCa-Tool
    * Figure 5, caption: "Llama-3-8b-ft" - missing s
    * section 5, Backbone LLMs, line 325: "Llama-3-8b-sft" is referred to as llama-3-sft in Figure 5, please correct the denotation
      * alternatively you could also remove the titles inside the subfigures
    * line 488: "Similar to the LLMs function-calling" - I believe it should LLMs'
    * line 500: "Zou et al. (2023)" - remove brackets around the year, and add brackets around the whole citation; should be fixed by using the correct cite command
    * line 504: "Probing use" - I believe it should be "uses"
    * Figure 6:
      * "Llama-3-8b-ft" should be "Llama-3-8b-sft"
      * additional the title inside the subfigures uses "llama3-8b-inst-sft"
      * "train data" - probably "training data"
    * Figure 7: inconsistent use of "llama3-8b-inst" and "llama3" in the titles of the subfigures
    * Figure 8: "train data" - probably "training data"
    * C.2, title: "train data" - probably "training data"
    * Figure 9: "train data" - probably "training data"
  * references:
    * Bricken et al. 2023: url not clickable
    * Drozdov et al. 2022: cited differently than the other arXiv papers
    * Hao et al. 2024: cited differently than other NeurIPS proceedings
    * He et al. 2021: cited differently than the other arXiv papers
    * He-Yueya et al. 2023: cited differently than the other arXiv papers
    * Huang et al. 2023: cited differently than the other arXiv papers
    * Komeili 2021: cited differently than the other arXiv papers
    * Li et al. 2023: cited differently than the other arXiv papers
    * Liu et al. 2024a/b and 2023a/b/c: cited differently than the other arXiv papers
    * Lu et al. 2024: cited differently than other NeurIPS proceedings
    * Patil et al. 2023: cited differently than the other arXiv papers
    * Qin et al. 2023: cited differently than the other arXiv papers
    * Qu et al. 2024: cited differently than the other arXiv papers
    * Schick et al. 2024: cited differently than other NeurIPS proceedings
    * Shen et al. 2024: cited differently than other NeurIPS proceedings
    * Tang et al. 2023: cited differently than the other arXiv papers
    * Wu et al. 2024: cited differently than the other arXiv papers
    * Yang et al. 2023: cited differently than the other arXiv papers
    * Zou et al. 2023: cited differently than the other arXiv papers

### Questions
* Figure 1: Why not use a tool, if the initial decision is to not use a tool, but it also beyond the ability of the LLM?
* section 3.2: The discussion about the probe selection seems rather fuzzy, since detailed results are not shown. How does the selection process generalizes to other models?
* section 5, baselines: Where do P(Yes | Prompt) and P(No | Prompt) come from? Token probabalities of the respective model?
* Will the source code be publicly released?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce a method called MeCo, which can enhance the ability of LLM to use external tools.
Unlike existing strategies, the proposed method captures emergent representations within the representation space that quantify the LLM's self-capability, guiding the decision-making process regarding such tools. The method is fine-tuning-free, minimizing additional costs.

### Strengths
1. The proposed method is fine-tune-free.

2. A benchmark MeCa is proposed for evaluating the ability of adaptive tool use

### Weaknesses
## 1. Meta-cognition is not clear enough and it is easy to confuse readers.
For a self-defined concept, a clear definition and examples should be given. However, the definition in the paper (the sentence below) is vague and lacks clear indicators.

> "We define meta-cognition as the model’s ability to recognize its own capabilities and limitations, discerning whether it can address a user’s query independently or if it needs to utilize external tools."

I don’t know if my understanding is correct, but the meta-cognition in the article is actually self-knowledge. However, the extensive use of meta-cognition in the article confuses this point.
A more detailed definition of Meta-cognition should be put it in a more prominent position. And it would be better if you could provide examples and quantitative indicators.

## 2. The proposed method has limited effectiveness
Table 1 shows that the score improvement brought by fine-tuning is much greater than the method proposed in the paper. Especially on the fine-tuned model, the improvement brought by the proposed method is limited.

Although this method does not require fine-tuning, it does require obtaining the output of the intermediate layer of the model to train the probe. The paper does not compare the overhead of fine-tuning and training probes
In addition, the intermediate layer output is also necessary during inference, which will continue to incur additional overhead.
This results in the actual cost being no lower than fine-tune.

## 3. Insufficient experiments
Only the 7B scale model was tested. The effects on larger models (e.g. 70B) need to be supplemented.
And it is unreasonable to use only the first token of the model to judge correctness, especially for a 7B scale model.

In addition, I have doubts about the prompt in Appendix B.1.
> “Our findings indicate that instructing the model to first provide a “Yes” or “No” response followed by an explanation yields better results than other strategies, including the CoT approach.”

When using the COT method, if still let the model answer “Yes” or “No” first and explain it later, then COT will not produce any effect, because the "Yes" or "No" is not based on the explanation, which is a classic incorrect use of COT. The reason for the results in Table 6 is probably that there is a problem with the prompt itself, but the prompt is not given in the paper. The authors should provide the COT prompt used in the experiment and the method of how to get "Yes" or "No" from LLM's output.

### Questions
1. Please give a more detailed definition of Meta-cognition and put it in a more prominent position. It would be best if you could provide examples and quantitative indicators.
2. Please provide experiments on larger models (e.g. 70B level)
3. Please provide the COT prompt used in the experiment and the method of how to get "Yes" or "No" from LLM's output.

### Soundness
2

### Presentation
2

### Contribution
2
