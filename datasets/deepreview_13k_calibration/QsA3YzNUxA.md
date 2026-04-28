# Is Your Multimodal Language Model Oversensitive to Safe Queries?

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Humans are prone to cognitive distortions — biased thinking patterns that lead to exaggerated responses to specific stimuli, albeit in very different contexts.
This paper demonstrates that advanced Multimodal Large Language Models (MLLMs) exhibit similar tendencies.
While these models are designed to respond queries under safety mechanism, they sometimes reject harmless queries in the presence of certain visual stimuli, disregarding the benign nature of their contexts.
As the initial step in investigating this behavior, we identify three types of stimuli that trigger the oversensitivity of existing MLLMs: \textbf{\textit{Exaggerated Risk}}, \textbf{\textit{Negated Harm}}, and \textbf{\textit{Counterintuitive Interpretation}}.
To systematically evaluate MLLMs' oversensitivity to these stimuli, we propose the \textbf{M}ultimodal \textbf{O}ver\textbf{S}en\textbf{S}itivity \textbf{Bench}mark (MOSSBench).
This toolkit consists of 300 manually collected benign multimodal queries, cross-verified by third-party reviewers (AMT).
Empirical studies using MOSSBench on 20 MLLMs reveal several insights:
(1). Oversensitivity is prevalent among SOTA MLLMs, with refusal rates reaching up to \textbf{76\%} for harmless queries.
(2). Safer models are more oversensitive: increasing safety may inadvertently raise caution and conservatism in the model’s responses.
(3). Different types of stimuli tend to cause errors at specific stages — perception, intent reasoning, and safety judgement — in the response process of MLLMs.
These findings highlight the need for refined safety mechanisms that balance caution with contextually appropriate responses, improving the reliability of MLLMs in real-world applications.
We make our project available at~\href{https://turningpoint-ai.io/MOSSBench/}{https://turningpoint-ai.io/MOSSBench/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a benchmark, MOSSBench, to systematically evaluate the propensity of multimodal LLMs to refuse to answer harmless queries. The authors find that safer models also tend to refuse more benign queries, that web-based models are more “oversensitive” than API versions, and that particular types of safe queries (i.e. “negated harm” and “counterintuitive interpretation”) engender more refusal than others. The authors perform a deeper analysis of the refusal behavior in a subset of examples, finding that perceptual errors often cause oversensitive behavior.

### Strengths
This work tackles a persistent problem in safety-tuned models: their poor ability to properly discern harmless queries from harmful ones. The dataset curation process seems thorough and careful, and the empirical results are compelling

### Weaknesses
The primary weakness in this work lies in its rhetorical framing around cognitive distortions. It appears that this comparison is a bit superficial, and does not add much to the scientific contributions of the paper. On the contrary, this framing invites either 1) potentially harmful anthropomorphizing of LLMs, or 2) analogizing people with mental health disorders to LLMs. Though this work does not attempt to use LLMs as models of people with mental health disorders, the current framing may inspire such misguided work in the future. 

Additionally, there appears to be an important element of refusal behavior that is absent in the current analysis: the model’s conception of the user submitting the “harmless” query. Prior work [1, 2] has demonstrated that a model’s perception of a user’s attributes importantly modifies their refusal behavior. Understanding person effects seems crucial for understanding the model’s reasons for refusing queries such as those shown in Figs 20, 25, and 30. In all of these cases, the “harmless” query might be rendered harmful if a certain user (i.e., a white supremacist for Fig. 25) is submitting them. In the absence of a user model, perhaps the LLM is merely assuming the worst and responding as such? Including a preliminary investigation of these effects would strengthen the empirical results.

Additionally, some of the most interesting analyses in the paper (Section 6) are performed on a very small number (10) of examples. More examples should be included in the final version of the work.

### Questions
How were these three categories of visual stimuli determined?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces a Multimodal Oversensitivity Benchmark (MOSSBench) to evaluate the oversensitivity of multimodal language models (MLLMs) based on Refusal Rate. The authors categorize the main "stimuli" of oversensitivity into three types: Exaggerated Risk, Negated Harm, and Counterintuitive Interpretation, each explained by an illustrative example. They conduct a thorough and detailed analysis, testing 20 popular MLLMs including both proprietary and open-source models on MOSSBench. They also provide several interesting findings.

### Strengths
1. While there is prior work on oversensitivity in language models, this paper is novel as the first to assess oversensitivity specifically in multimodal LLMs.

2. The evaluation is both comprehensive and in-depth, and covering a wide range of MLLMs. The authors provide insightful analyses, such as identifying discrepancies between web and API versions of proprietary models. The design of how different stimuli impact different reasoning stages in MLLMs indicates the novelty of the work and results in several valuable findings.

3. The authors conducted multiple rounds of rigorous controls and reviews on the proposed benchmark, suggesting MOSSBench is in a high quality.

### Weaknesses
The dataset is relatively small, with only 300 test cases, which may affect the statistical significance of the findings and limit the impact of this work. A small benchmark size could make it easier for MLLMs to overfit to this evaluation.

### Questions
1. Are the ARR results for open-source models (and API versions of proprietary MLLMs) reported after running randomness tests with repeated experiments, such as changing the random seed or decoding strategy?
2. How was the human annotation team? Could you provide details on their occupations or expertise, such as in cognitive science or psychology?

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
The paper presents a benchmark dataset for testing the possible oversensitivity of Multimodal Large Language Models (Vision + Language), i.e., rejection of harmless queries due to the safety mechanism of MLLM. The authors focused on visual stimuli that can  potentially trigger such systems.
Visual stimuli that cause oversensitivity of MLLM were categorized in three main categories: 

1. exaggerated risk, i.e. potential dangerous elements but harmless in the given context; 
2. negated harm, i.e. the harmful content is present with a message of discouraging the harm (e.g. a visual negation); 
3. counterintuitive interpretation, i.e. elements in benign intentions are misinterpreted.

Authors address two main research questions: 
1. how prevalent is oversensitivity in MLLM? 
2. what specific failure in MLLM ‘s response process contributes to such behaviors? 

To these aims, they developed Multimodal OverSenSitivity Benchmark (MOSSBench), a benchmark of 544 image-text pairs formatted for Visual Question answering (VQA). It utilizes an hybrid method that combine LLM and human inputs for different scenarios and meticulous filtering, then annotated by an AMT annotator. They tested the benchmark on an array of 20 models from 3 categories: proprietary, proprietary from web versions and open sources. They also perform a failure analysis to test at which stage of reasoning the MLLM refuses a query. The results highlight three main findings:

1. Oversensitivity is prevalent on most of the current MLLMs.
2. Safer models are also more oversensitive.
3. Precise type of stimuli triggers more precise stages of the reasoning process.

MOSSBench is collected by a two-step sample generation: 
1. candidate generation: using several LLMs (to reduce biases in data) for generating the candidate texts and DALL-E 3 or looking up the web for the images. 
2. candidate filtering: human annotators filter the generations to delete possible real harmful content;  9% of the candidates were found to be actually harmful.

Finally, they construct a complementary set of harmful samples by introducing explicit malice into their scenario.

Authors perform both human and automatic evaluation (via GPT4-V), finding a 97.8% agreement among the human annotators.

From the results of such analysis, they highlight 5 main findings:
1. Open source models are less sensitive than proprietary models, except for the models from the GPT-series.
2. Web version of proprietary models shows greater sensitivity with respect to the API version
3. The refusal rate is higher for stimuli of Negated Harm or Counterintuitive interpretation
4. The safer the model, the more oversensitive it is.
5. System prompts influence oversensitive behavior.

For the final analysis about the stage that causes incorrect refusal in MLLMs, the authors divide the response process in three main stages: 
1. perception: the model must describe in the correct way the image; 
2. intent reasoning: the model formulated hypothesis about the user’s actual intent; 
3. safety judgement: the model decide to accept or reject the query, based on the other two stages. 

The authors find that most errors occur in the perception stage and different stimuli challenge different stages, i.e. exaggerated risk challenge more the perception stage. Conversely, negated harm and counterintuitive interpretation have most of the errors in intent reasoning and final decision stages.

### Strengths
The paper extends a debated topic on LLMs (sometimes called extra safety) to MLLM, clearly focusing on the visual component of such models. 

The authors introduce a  useful resource (MOSSBench), identifying a variable dimension about the type of visual stimuli divided in 3 possible categories. They also correlate the Refusal Rate with the actual safetiness of the models, computed by mean of a complement set  of real harmful examples, which is an important comparison to perform. 

Also, the post-experiment analysis about the refusal stage is important, in order to understand what the model finds challenging, and the authors show some similarity across the models (same visual stimuli tends to fail for the same “failed” stage). 

The evaluation pipeline can be potentially useful for future analysis of safety vs oversensitivity of the models and diagnose the cause of errors.

### Weaknesses
In the paper there is a continuous parallelism with human cognition and behavioral disturb that causes similar errors in the humans of what is seen in MLLM. As written, it seems that authors give the MLLM “human cognition” capabilities and similar possible illnesses/disturb. All these could be avoided since they don’t give any contribution to the message of the paper and again, give the hint that MLLMs have something close to human cognition. Instead, a bigger focus on the technical aspects that lead to failures might strenghten the paper.

For instance, example 2 is misleading since the MLLM oversensitivity, in that case, seems totally an error of miscomprehension of the MLLM, and I don’t see any similarity with human cognition.

Moreover, the MLLMs use a non-stochastic decoding (I saw also the impact of temperature on the results). To this matter, results on a single run limit the generalization of the claim. Since the main point of the paper is the resource, a reader would expect to see multiple runs of the experiments on the 3-4 most meaningful models to verify the generalization of the claims, reporting average and standard deviation. This should be done also on the analysis about the error stage.

I am also not totally convinced by the usage of GPT4-V for automatic evaluation (GPT4-V is one of the models used in the experiments), and the paper is missing a comparison between human annotation and LLM annotation

Some minor typos:
- Line 48: “Concretely” 🡪 “concretely”
- Line 84: “scenariosand” 🡪 “scenarios and”
- Check the capitalization of the first letter in the item lists.

### Questions
- Have you tried to perform multiple runs on the same model (with fixed hyperparameters)? How much are they coherent with the results reported?

- Can you add a general description of the type of subjects in the images? Can you provide any categorization of the images? I would expect that some categories, due to embedded biases in the model, lead to higher ARR than others (i.e. image with predatory animals vs image of cities).

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel benchmark for evaluating the issue of oversensitivity in MLLMs, aiming to balance safety and efficiency. It contributes a dataset in which the image-text inputs are benign but may be mistakenly recognized by MLLMs as violating safety guidelines, leading to a refusal to respond. It provides extensive empirical evaluations and presents several findings. In addition, it designs clever ablation experiments to verify the components that lead to oversensitivity.

### Strengths
1. The paper is well-structured with rigorous writing logic, and the experimental design is tightly interconnected. The idea behind the ablation experiments designed at the end is particularly clever.
2. The paper provides intuitive insights into balancing the safety of MLLMs and user efficiency.

### Weaknesses
1. First, it is mentioned in the limitations that the dataset size is too small, in terms of cost and resource requirements due to the need for human intervention in the filtering and selection processes. The comprehensiveness and generalizability of the benchmark need improvement. 
2. The experimental section only evaluates the rejection rate, which is crucial; however, it lacks an assessment of the balance between safety in question answering and the efficiency of the answers. When using this benchmark to evaluate MLLMs, focusing only on the rejection rate would be too one-sided. The goal is to balance, it would be appropriate to include experiments that assess the correct rejection of harmful queries, the incorrect rejection of harmless queries, the correct response to harmless queries, and the incorrect response to harmful queries. 
3. I observed that the prohibitions for some examples related to “Negated Harm” seem somewhat forced subjectively (e.g., figure 20, figure 25).

### Questions
1. Regarding the division of the processing steps and the design of the ablation study, I would like to know if these are original contributions of this paper. If so, I would consider giving a higher score.
2. Some typo: It covers a variety of scenariosand serves as a diagnostic suite for assessing oversensitive behaviors. (line84-85); (3). Safety Judgement (line430-431)
3. I believe it is quite necessary, rather than solely focusing on the rejection rate. I will consider increasing the score if you add a set of small experiments during the rebuttal period (weakness two).

### Soundness
3

### Presentation
4

### Contribution
3
