# Knapsack Schema Linking Agent for LLM-Based Text-to-SQL Generation

- Decision: Reject
- Scores: 3, 6, 5, 5, 6

## Abstract
Generating SQLs according to user queries (text-to-SQL) is a long-standing sequential challenge, where the accuracy of the initial schema linking significantly impacts the subsequent SQL generation performance. However, existing models often focus more on SQL generation and less on the schema linking task, leading to potential missing or redundant schema linking and suboptimal SQL generation performance. The underlying reason is that schema linking is not a simple selection problem but a \textbf{Knapsack problem}, which should consider both the \textit{value} of the schema linking in terms of missing important information and the \textit{weight} of the schema linking in terms of providing redundant information. Motivated by this, we provide two tailored SL benchmarks and two tailored metrics to train SL agents and to evaluate the missing and redundant schema linking. In this paper, we propose the \textbf{\underline{K}n\underline{a}psack \underline{S}chema \underline{L}inking \underline{A}gent (KaSLA)}, which can link the most valuable and least redundant schema element subsets for both tables and columns. KaSLA introduces an importance score function to predict each schema element's importance score, and then utilizes the importance score to estimate the value and the weight of each schema. Then, by estimating the capacity, the maximum weight the knapsack can hold, of a given user query from historical SQL records, KaSLA employs efficient dynamic programming to select the most valuable schema element set within the estimated capacity. Extensive experiments on two benchmark datasets demonstrate the superior performance of KaSLA over 12 state-of-the-art baselines. Especially on the popular and challenging BIRD benchmark, KaSLA can outperform the baselines by over 5.72\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper formulates the schema linking for text2sql as a knapsack problem. It defines many concepts, like redundancy, schema missing rate, score functions, as well as the weight, value and the capacity for the knapsack formulation. The paper is hard to read, in general. Some definitions are intuitive, such as redundancy. Models are fine-tuned for the scoring functions, and most formulas are per query. The paper does not convince me that schema linking is a knapsack problem; as the weight and value are both defined in terms of the importance of the schema element, and capacity is a forced parameter that is introduced. The experimental results look promising, but there are various concerns about them, which are explained below.

### Strengths
1. The paper provides extensive experiments.
2.

### Weaknesses
 1. Knapsack formulation is not intuitive, as the capacity constraints is superfluous. If the capacity was formulated depending on the context size limitations, it might have made sense. 
 2. The scoring model is fine-tuning with ground-truth. This requires having a ground truth set, training models, which will only work for benchmark datasets like BIRD and Spider, but is not solution in practice. 
 3. Experiments compare multiple things at the same time, so it is difficult to judge whether the accuracy savings are fully attributable to the schema linking process introduced in this paper.
 4. Why introduce new metrics like missing schema and redundancy, while precision and recall of schema linking can fully cover these concepts?
 5. The experiments do not include two of the SOTA schema linking works, E-SQL and CHESS, both are on the BIRD leadership. Especially, E-SQL focuses mainly on schema linking and does not use many of the other techniques, like self-consistency, to achieve high accuracy. Experiments should have included at least E-SQL.
A. CHESS: Contextual Harnessing for Efficient SQL Synthesis:  Shayan Talaei, Mohammadreza Pourreza, Yu-Chen Chang, Azalia Mirhoseini, Amin Saberi
B. E-SQL: Direct Schema Linking via Question Enrichment in Text-to-SQL: Hasan Alp Caferoğlu, Özgür Ulusoy

### Questions
1. Redundancy is a confusing term; do you include the same table/column multiple times in the context? I understand that you do not. This is supposed to capture irrelevant schema elements; i.e. precision. How is this different?
2. Similarly, how is missing schemas different than recall?
3. In the paper, when you say schema it is confusing whether you mean table or column or both. It is not until 4.3 that it gets some clarification. Do you mix schema errors or solve two separate knapsack problems, one for tables and one for columns? The models in the score function, are they trained for tables and columns separately? Column selection is conditional, you choose columns from the selected tables; how does that impact the score functions?
4. How are the scoring functions trained? Ground truth for which dataset? Dev or train?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes the famous schema linking problem in the field of LLM-based text-to-SQL. The main contribution is to formulate the selection of relevant tables/columns into a Knapsack problem. Each schema item is assigned a value, and the objective is to maximize the total value with the constraint that the total cost of all selected schema items should be less than a capacity. This idea is novel and interesting to me. And the authors present sound math proof (except minor issues, discussed below) in the main paper. The experiment results demonstrate that this pre-processing is useful on the dev sets of two well-known benchmarks, BIRD and Spider. Besides, this work also formally defines two intuitive metrics to evaluate/explain the "precision" and "recall" of schema linking from another perspective, namely, missing rate and redundancy rate.

### Strengths
1. The paper is well-written and easy to follow.

2. The experimental results verify the motivation.

3. The new formulation of schema linking problem sounds interesting and novel to me.

### Weaknesses
 **[Updated]: Part of my major concern is resolved, and the minor concern is totally addressed. Thus, I am willing to raise my scores of both Soundness and Rating to the next level. About the Confidence score, I accidently choose 2 in the first round, while I originally intended to choose 4.**

1. Major concern: Although in Figure 1, the authors demonstrate the importance of schema linking (given the oracle set, there is still large margin), the problem that whether pre-extracting relevant schema items is a promising direction is still doubtful, especially considering the high cost of individually determining the scores/weights of each table/column. To the best of my knowledge, the majority of existing benchmarks have a relatively smaller database schema size, which can mostly afford to the prompt length. See the work below (also one missing reference):

_The Death of Schema Linking? Text-to-SQL in the Age of Well-Reasoned Language Models._

link: https://arxiv.org/pdf/2408.07702v2

It proves that, if the schema items can be fully inserted into the prompt, schema linking is not a necessity considering efficiency. In other words, this work circumvents this significant issue on the inference delay (including nomination model StarCoder2, guaranteed scorer RoBERTa-Large, extra statistics calculation and dynamic programming). I even did not see one limitation section discussing it. And a quantitive comparison on the inference time w/ and w/o your method is inevitable to trade-off the benefits and disadvantages.

2. Minor issue: some technical design or math is really confusing. Here are some questions:

a. in Eq.(4), you use two scores (both binary $I_{nomi}$ and float $I_{guar}$). How about directly use the soft score $I_{guar}$ as $I_{s,q}$? What is the performance difference? This is important that if a simpler calculation of $I_{s,q}$ can achieve similar expectations, we should always follow the Occam's Razor.

b. About Eq.(8) and (10), the authors define a little complicated equations to estimate the weight and capacity, respectively. I’m curious if there was any mathematical basis behind the design of these formulas, or you just come up with them all from intuition. If the answer is true, please cite them to make the equations more sound. Otherwise, it would be better to prove that this design is empirical and preferred by comparing multiple variants.

c. There are many hyper-parameters in the calculation, e.g., $\tau,\alpha,\gamma$. Could you explain in detail why each of them is needed? Introducing too many tunable parameters may lead readers to suspect that the experimental performance was achieved through careful hyperparameter tuning, which could indicate poor generalizability.

3. Other issues: (not affecting my final judgement at all, just kind suggestions)

i. Be more careful about the notation details, e.g., in Eq.(8), $f_V(s)$, $f_V(s, q)$, and $E_{I\ge \tau}(S)$, if the result is related to concrete input question $q$, please add the symbol $q$. Otherwise, the reviewers will wonder whether this is a benchmark-level statistics or instance-level score.

ii. Try to simplify some equations to avoid over-complicating the introduction. For example, the value estimation $V_{s,q}$ re-uses the importance score in Eq.(7), why not merge them into one? This will also alleviate issue i).

### Questions
All questions are introduced in the Weaknesses section.

### Soundness
4

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
5

### Summary
The paper introduces a table (and column) retrieval/schema linking method for RAG-base text-to-SQL systems. The proposed approach called Knapsack Schema Linking Agent employ metrics for missing and redundant schema linkages explicitly optimizing the retrieval recall and precision. To constrain the redundancy in the table retrieval process, the paper proposes a capacity estimation method to limit the selection. The paper also proposes two benchmarks for training and evaluating the table retrieval model and task. Experimental evaluation demonstrates its superior performance on benchmarks.

### Strengths
S1. Table retrieval/schema linking is an important problem often overlooked or over simplified by the existing text-to-SQL systems. Real life  text-to-SQL use cases often deal with hundreds, thousands and even over hundreds of thousands tables (extreme case in data lake scenarios). The prompt can only contain a small amount of tables requiring high recall and high precision table retrieval/ranking method. This paper addresses this important problem although not at scale.

S2. The idea of explicitly measuring and trading off potential missing and redundant tables is interesting.

S3. The experimental evaluation demonstrates its superior performance against baselines on the proposed benchmarks and BIRD.

### Weaknesses
W1. As mentioned in S1, as the number of tables in a database where the text-to-SQL is performed against is growing, the problem of table retrieval becomes increasingly challenging. To really assess the impact of this work, it will be great if the paper can discuss and address the size of full schema |S| being realistically large.

W2. The proposed method requires a fair amount of fine-tuning efforts. The application scenario is unclear. Such an approach can be valid for competing in benchmark like BIRD where the dev and holdout test has similar distribution. It works when the type of questions and the schema design in the database is fairly stable over time. In the event of significant schema changes, does the training/fine-tuning need to happen again? The paper lacks of discussion on the exact text-to-SQL usecase.

W3. Text-to-SQL generation often deals with SQLs involving multiple tables (e.g. JOIN). Join keys can be semantically meaningless to the question (arbitrary id columns) but very important to the generation. It is unclear how is this taken into consideration when the proposed approach is performing column retrieval/selection.

W4. The paper lacks of details on the table representation. How is cell values considered?

W5. In real life application, table names and/or column names can be explicitly mentioned in the question. This motivates the use of sparse index such as inverted index. Can inverted index be used as a part of this approach to improve the recall/precision?

### Questions
Please respond to/comment on W1-W5.

### Soundness
2

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
4

### Summary
The authors point out, with supporting evidence, that inability to link to a high-recall and high-precision set of schema elements (such as tables and their columns) is a significant contributor to text2sql system errors.  This set of schema elements are provided to the (usually LLM-based) SQL generator/decoder, along with the natural language question/utterance. Loss of recall will generally result in hallucination (where the generated SQL mentions fictitious tables and columns), and loss of precision shows up as interference (leading to existent but incorrect tables and columns being used). The authors then propose a schema retrival method in which recall and precision are deliberately balanced using a knapsack paradigm.  Limited knapsack capacity encourages high precision.  Item (schema element) profits encourage high recall.  The profit of an item is an additive combination of two parts: one is the probability of generation by a fine-tuned LLM, and the other is a late-interaction comparison between the query embedding and a suitable encoding of schema elements.  Meanwhile, the weight of an item is inversely related to an "importance score".  Finally, the knapsack capacity is determined via in-context demonstrations.

### Strengths
Strengths:
* Identifies schema retrieval failure as a significant reason for text2sql failures.
* Proposes a schema subset selection problem as a cost-benefit driven knapsack instance.
* Shows consistent end-to-end text2sql improvements on BIRD and Spider.
* Shows a more mixed improvement at schema selection.

### Weaknesses
Weaknesses:
* Proposed method has too many moving parts and lacks clarity in its development.
* Writeup quality can be greatly improved (see below).  Nonstandard and unfamiliar terminology is frequently used.
* Instead of inventing new retrieval measures, why not not stick to classic ones like recall and precision?  I do not quite buy that you have to "propose two metrics that evaluate the missing rate and the redundancy rate that directly impact the SQL generation performance, rather than indirect metrics like AUC and F1"  Recall and precision directly impact SQL generation as much as the measures you propose.
* While some improvements result, Knapsack may not be technically the correct paradigm to model schema selection.
* (L364-L373) are confusing.  Why should the SQL generator get access to "ground truth schema $S$" at all?  You would not be able to use it in a real deployment, would you?

### Questions
Questions/comments

https://bird-bench.github.io/ shows systems with better performance, but perhaps the authors are interested in a more controlled comparison?  They should explain their position in this matter.

Many writing nits:

What is described as "schema" throughout the paper is more accurately called "schema element", which is usually a table (including views) or a (table, column) pair in case of text2sql. 

I do not find it appropriate or necessary to call the proposed method an "agent".

"Nomination-guaranteed" is not a thing.  You cannot use this in an abstract (or anywhere, actually).

Various other terms are used throughout in confusing manners:
redundancy, "semantically related schema", 

(L307-L315) Why is $\gamma$ needed as a hyperparameter?

L017 …but can be modeled as a Knapsack…
L019 "redundant" or "incorrect", "excessive"?
L023 "nomination-guaranteed" is non-standard.  Define or use a more self-contained expression.
L025 better to specify early that "capacity" is the maximum item weight the knapsack can support.  This is found on L139 "weight capacity".

Figure 2 What are the schema items $S_1,\ldots,S_4$?  Better to call them "schema items" or "schema elements" and give actual examples of tables and columns.

One can measure a large value of your redundancy measure, but it is not clear how much that damages SQL generation (compared to loss of schema recall).  This is worth a separate study.

Eqn (2) is a measurement of loss of recall.
"Redundancy rate" in eqn (3) is like one minus precision.
It is confusing that redundancy is forced to zero if the recall is not perfect.

The terminology in "nomination-guaranteed" gets even more confusing.

About $\mathcal{I}_ {nomi}(s|q,\mathcal{S})$:
while you have defined in eqn (5) the quantity $\mathcal{L}_ {nomi}$, I could not find an expression for $\mathcal{I}_ {nomi}(s|q,\mathcal{S})$ nearby.  It seems there is no use of this score downstream.  It is just an indicator for what schema elements StarCoder2 will generate.
Authors need to provide exact input and output specifications for finetuning StarCoder2.
Also in eqn (5) how do you deal with the fact that $\mathbf{S}$ may be output in any order?

And then, in L247, an _importance value_ assigned by RoBERTa to each (surviving?) schema element.

L271 "schemas with higher importance scores should be assigned higher values".  Then we see $I_{s,q}$ which comes from eqn (4), combining inclusion by StarCoder2 and scoring by RoBERTa.  This is confusing, because on the latter was called "imporance" earlier.

L281 "schemas with higher importance should be assigned lower weights than those with lower importance scores".  So the importance score figures twice: once in value, and again in weights.  This seems not-elegant.

L488 $\mathcal{R}_{correct}$ springs another surprise.  Given the relatedness to recall and precision, why not just use F1?

Success in Table 3 is more mixed.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work focuses on text-to-SQL query conversion. While current research primarily addresses SQL generation, this study is more inclined toward schema-linking tasks. This approach aims to prevent missing or redundant schema linking, resulting in more optimal SQL generation. The authors argue that schema selection is not a simple task but rather resembles a knapsack problem. Additionally, the authors note that the current state-of-the-art (SOTA) in Text-to-SQL relies on simplistic schema linking strategies.

### Strengths
This work introduces a novel approach by applying the Knapsack problem to schema linking, effectively addressing the generative versus recall methodologies. The authors highlight the lack of benchmarks and metrics for schema linking, emphasising the need for standard evaluation metrics to assess missing and redundant schemas. They clearly explain why previous metrics are not suitable for evaluating schema linking.

The authors design two tailored schema linking benchmarks and introduce two schema linking metrics: schema missing rate and schema redundancy rate to evaluate schema linking performance.

### Weaknesses
- Since this approach is based on dynamic programming, the computation time might be significant. It would be beneficial if the authors addressed this issue in the paper.

- The related work is severely lacking and is in the supplementary section instead of the main paper. The authors make it easy to understand what they have done but it is not clear what the previous approaches were and how exactly the proposed approach is better.

### Questions
- In the Guaranteed Scoring Model, the authors used the RoBERTa-Large model to obtain semantic embeddings. It would be helpful if they provided a rationale for choosing this specific model.

### Soundness
4

### Presentation
2

### Contribution
3
