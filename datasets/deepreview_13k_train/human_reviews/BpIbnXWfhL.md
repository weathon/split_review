# RuAG: Learned-rule-augmented Generation for Large Language Models

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
In-context learning (ICL) and Retrieval-Augmented Generation (RAG) have gained attention for their ability to enhance LLMs' reasoning by incorporating external knowledge but suffer from limited contextual window size, leading to insufficient information injection. To this end, we propose a novel framework $\ourmethod$ to automatically distill large volumes of offline data into interpretable first-order logic rules, which are injected into LLMs to boost their reasoning capabilities. Our method begins by formulating the search process relying on LLMs' commonsense, where LLMs automatically define head and body predicates. Then, $\ourmethod$ applies Monte Carlo Tree Search (MCTS)  to address the combinational searching space and efficiently discover logic rules from data. The resulting logic rules are translated into natural language, allowing targeted knowledge injection and seamless integration into LLM prompts for LLM's downstream task reasoning. We evaluate our framework on public and private industrial tasks, including natural language processing, time-series, decision-making, and industrial tasks, demonstrating its effectiveness in enhancing LLM's capability over diverse tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a rule-augmented generation approach, where rules are learned from the training dataset using Monte Carlo Tree Search (MCTS).
It shows that leveraging rules can outperform retrieved passages or even other supervised trained models.

### Strengths
The paper contributes by integrating rule-based augmentation with generation models, leveraging rules learned from data.

### Weaknesses
There are several areas of concern:

1. Clarity in Section 3.1 (LLM-based Logic Rule Search): This section is difficult to understand. Here are some follow-up questions for clarification:

    1.1. What do the initial predicates look like across the three different datasets?

    1.2. How does the LLM eliminate impossible predicates? Could you provide prompt examples?

    1.3. How does the LLM propose new target predicates? Any prompt examples for this?

2. Performance of Rules Alone: It appears that in cases where the rules generalize well to the test set, predictions might be straightforward using only the rules. However, this may not extend to more complex or varied test cases. The paper does not adequately address the limitations of relying solely on rules, especially in scenarios where the rules might be brittle or incomplete.

3. Applicability of Rules: The rules generated in this paper may not directly translate to real-world retrieval-augmented generation (RAG) settings, which often require "external knowledge" represented in both body and target predicates. For instance, the example in Figure 2 does not reflect how real-world decisions about weather predictions are made. The rules discussed here seem applicable primarily to scenarios with deterministic target predicates (e.g., classification tasks). How might this approach be extended to real-world scenarios, as suggested in the conclusion?

### Questions
1. Did you use only the "train" split to construct the rules, testing them exclusively on the "test" split?
2. How did you partition the data for the cooperative game into train, validation, and test sets?
3. Given the reliance on deterministic predicates, how do you anticipate this approach adapting to real-world RAG scenarios requiring dynamic, knowledge-based decision-making?

### Soundness
2

### Presentation
2

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
This paper proposes to use LLM to create abstract rules that can be provided in context for better decision making when using LLM. The method contains a few steps where first the LM is used to define the features and labels for which we would like to forumlate rules over. Then MCTS is used to find the rules that explain the data best, and last the rules are provided in-context for prediction. The idea of using LLM to create features to search over given data is very nice. The method is evaluated on tasks of relation extraction, anomaly detection and a multi-agent game. Using GPT-4 is much better than weaker models (unsurprisingly) and using the rules is better than some prior work termed HtT (which needs more explanation). In the game experiment there is advantage over ICL and RAG.

### Strengths
* The idea of using large language models for "feature extraction" is very interesting. It is related to https://arxiv.org/abs/2409.08466 (which I don't expect to be in the paper since it's very recent)

* The empirical results show that for some use cases abstract rules can be leveraged to improve performance.

### Weaknesses
 * The paper needs better **scoping** -- when is this method likely to be useful and when not? For example, the point of machine learning is that some things are hard to express by rules -- for example, what makes a face a face or a cat a cat? We learn machine learning models for cases where rules are hard to formulate. Is this method restricted to things that can be defined by rules or not? I think it's important to discuss this. Second - the method assumes an input of N features with some feature description. Often nowadays we work with more raw data like a sequence of words etc. Is this restricted to such cases? The tasks chosen are diverse but rare and it is not clear how general the method is and when we should expect it to work? Overall the generality of the method remains unclear and needs further discussion.

* Line 188: it is not clear if the LM looks at the actual data. The authors talk about using the LLM to look at the data and find patterns, but it seems maybe the LLM is only used to look at the schema, or the featuer descriptions to define what are the body and target predicates and it does not use the actual values of these features in the data at all? Choosing the rules is done with MCTS where it is not clear if the LM is used - it seems like rules are applied on the data to see if they work well. So if the LLM is not used to find patterns in the data this might be a bit limited.

* The paper has many clarity issues:
** Clarity - I don't understand figure 3 well enough - it seems important but is a mix of using text and emoji without proper explanation I can kind of squint at it and guess but it seems really difficult to understand what are the details of each step.

** Clarity: line 190: “initial the features as the body predicates” - what are the features exactly? can you give some examples and intuition at this point already?

** The paper talks about "impossible body predicates". What are those? Why are they impossible? What is exactly the input provided to the LLM to perform this task (please don't send me to the appendix in author response). Similarly "suggesting new target predicates" how? What is the task given to the LLM to do that? All those seem like crucial aspects that are not explained. I can imagine the LM doing an OK job in these things with some prompt but they don't seem necessarily like something that is well defined that even humans can do with reasonable agreement.

** HtT -- this seems like a key baseline that is not explained properly.

** Line 285: During the rule extraction process, we leveraged the LLM to filter out 15% of the relationships that were unlikely to serve as valid predicates. Unclear;

** Experimental details: There is very little detail in the paper on what are the featuers/labels/target and body predicates in each of the experiments, this makes it hard to understand the task. There are a few examples in a table but this is insufficient for understanding.

* Experimental evaluation: a lot of the comparisons in the experiment are between models that have very different abilities. Comparing GPT-4 to some CNN or BiLSTM or BERT is not a fair comparison at all. Baselines should be between the same model that uses different methods for providing in-context information and this is missing.

* Experimental evaluation: The main claim in the abstract and introduction is that using rules in context is a better alternative to in-context learning and RAG - but I don't see any RAG or ICL baselines in section 4.1 or section 4.2 so how can this claim be made? Did the author try ICL and RAG in 4.1 and 4.2? or only in 4.3? It would also be good to have much more detail on what the ICL and RAG baselines look like in Section 4.3.

* Minor: lines 189 and onwards have the same few sentences twice.

### Questions
** Table 4 -- where do confidences come from?

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
This work introduces the RuAG framework that automatically distills large volumes of offline data into logical rules , which are then included in LLM prompts to enhance their reasoning capabilities.

### Strengths
1. RuAG offers a scalable solution for integrating extensive domain knowledge into LLMs that improves upon RAG or SFT.
2. Model performance is tested on a wide array of tasks and show improvement on strong baselines
3. RuAG is more computationally efficient than other methods that summarize external dataset as knowledge storage, as the calls to API models only happen once during logic rule constructions.

### Weaknesses
1. Ablation studies in Table 5 could include RAG or SFT on open-source LLMs, as the current baselines only include COT which does not include external knowledge.
2. How do LLMs suggest new rules to explore and detect impossible body predicates? These parts seem unclear to me.

### Questions
1. L190-195 probably has some copy-pasting errors?

### Soundness
3

### Presentation
3

### Contribution
3
