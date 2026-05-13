# Reliable and Efficient Amortized Model-based Evaluation

- Decision: Reject
- Scores: 6, 8, 6, 8, 6, 5

## Abstract
Current generative model evaluation procedures are costly and sensitive to test set selection, making continuous monitoring impractical. In this paper, we employ a model-based evaluation framework using Item Response Theory (IRT), which decouples model performance from the test subset selection, ensuring reliable and efficient evaluation. We propose two innovations: amortized calibration to reduce the cost of estimating item parameters of the IRT model and an item generator based on a large language model to automate diverse question generation. Our experiments on 25 common natural language processing benchmarks and 184 language models show that this approach is more reliable and resource-efficient compared to traditional evaluation methods, offering a scalable solution to evaluate generative models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel model-based evaluation framework using Item Response Theory (IRT) to efficiently and reliably evaluate generative models. The key innovations include amortized calibration to reduce the cost of estimating item parameters and a conditional item generator to automate diverse question generation. The approach is validated on 24 benchmarks and 180 language models.

### Strengths
1. The application of IRT in generative model evaluation addresses the limitations of classical test theory (CTT) in machine learning.
2. Amortized calibration significantly reduces the cost and complexity of item parameter estimation, making continuous evaluation feasible.
3. The item generator automates question creation, which is crucial for maintaining a diverse and up-to-date item bank.
4. Experiments are very thorough.

### Weaknesses
1. The introduction of IRT and amortized calibration adds complexity to the evaluation process, which might be challenging for practitioners without a background in psychometrics.
2. Details on the practical implementation of the item generator and its integration into existing workflows are limited.
3. The integration of Item Response Theory (IRT) with machine learning evaluations assumes a level of prior knowledge (e.g., psychometric concepts) that could limit accessibility.
4. The experiments predominantly rely on synthetic setups or controlled environments. Real-world case studies or collaborations with industry practitioners would strengthen the empirical validation.

### Questions
1. The paper mentions missing values in the response matrix. How are these handled during calibration and scoring to ensure accurate ability estimation?
2. Is the IRT model effective for non-text data, such as images or multimodal datasets? What adjustments are necessary?
3. How does the automated question generation avoid introducing bias, ensuring fair and objective evaluations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors tackle the problem of reducing the cost of models in the context of generative models and LLMs. The authors propose to evaluate models by modeling evaluation using Item Response Theory - framing evaluation as predicting the abilities of a learner exposed to questions/items. While this can already reduce evaluation cost, the authors propose two methods to further reduce cost/improve the reliability of the evaluation (i) parameterizing evaluation questions with an item model and (ii) adaptively testing learners by generating questions from item parameters using a generative model.

### Strengths
This manuscript considers an important but often neglected cost for developing models - the compute required for extensive evaluation.

Drawing on item response theory is a refreshing way of reframing the problem to yield new insights.

Adaptive testing with conditional item generation is a particularly interesting idea, as the evaluation is tailored to the model. This idea also partially addresses another potential problem for model evaluation - overfitting/evaluation leakage.

### Weaknesses
No major weaknesses, however see my question below.

### Questions
Generating questions for adaptive testing is clearly useful, but what do the the generated questions look like? How does the underlying generative model affect the results? How can we automatically verify the generated questions are valid/correct?

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
4

### Summary
The paper proposes a new way of evaluating generative models that leverages Item Response Theory (IRT) to form a more cost efficient and robust evaluation framework. The authors design both an amortized calibration algorithm as well as train a conditional item generator to aid in this process. The amortized calibration reduces the cost of estimating item parameters and reduces the cost complexity from linear to constant assuming a fixed question bank size. The item generator network uses a fine-tuned language model to generate test questions which can be conditioned on difficulty level.

### Strengths
This work has many strengths. First, the paper presents a novel approach to evaluating generative models that addresses the high cost and potential pitfalls of  current evaluation techniques. As far as I know, this is the first work to propose a fine-tuned language model to generate novel evaluation questions. The authors present a strong knowledge of the underlying IRT theory and write the math for the method behind it clearly and concisely.

### Weaknesses
The most glaring weakness of the paper is that they claim to test 180 models and don’t show the results of all of them anywhere in the paper or an appendix. The closest I could see of all of the models evaluated was in Figure 1, but it is truncated to fit in the paper; a table or chart at least demonstrating the model performance on the conditionally generated dataset and comparing it to the subsets of HELM would have been useful. Some further justification for assumptions behind the method of their IRT formulation would have been useful as well. (addressed further in the questions section below)

Some formatting concerns: 
 - the references aren’t linked
 - the figures aren’t linked 
 - some of the graphs are hard to read when printed due to small text

### Questions
- How do you make sure that the amortized calibration processed doesn’t worsen the bias present in the training data?
- What motivated the choice of Rasch’s model over other IRT models like 2PL or 3PL? Was it a simplification made to make the model tractable? 
- How do you validate the quality and correctness of the generated questions? Specifically, how do you deal with questions that might match the desired difficulty but be semantically invalid, without human oversight?
- Did you compare the amount of compute needed to create the amortized model with the compute needed to evaluate a single model? How many models do you need to evaluate to have the amortized model be more efficient?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a framework for adopting language models into Item Response Theory evaluation. The model is used in two ways: first, to predict the item parameter, and second, to generate examples of a designated difficulty level.

### Strengths
* Innovative ideas of leveraging LLM to improve IRT evaluation, especially using item difficulty to guide RLHF.
* The experiments are through and careful.

### Weaknesses
 * Some concerns about experiment setting and base model selection.

* This work mainly develops techniques to improve IRT-based evaluation. However, it doesn't use it to run systematic evaluations of current models, so readers can not cross-validate with other evaluation methodologies or their own experience.

### Questions
* Line 196, should it be $Y_{M+1}$ instead?

* In the subset evaluation experiment, the setting of having 50 hard subsets and 50 easy subsets feels artificially against CTT and in favor of IRT. I guess the differentiation of hard and easy is also based on IRT parameters, right? Then, although we can see IRT achieving consistent results in this setting, we can only infer that IRT can handle the differences in difficulty that it can capture. Because the IRT parameter is monotonic w.r.t., the correctness of each test taker, the notion of hard and simple will correlate with average accuracy. The fact that CTT shows a bimodal distribution is also largely expected. If we don't deliberately sample 50 hard and 50 simple but uniformly sample 100 subsets without any intervention, is the IRT evaluation still significantly better than CTT?

* Generating items and controlling their difficulty with RL is a clever idea. But, since we need to take some model to generate it, we ought to inspect if this asymmetry causes any unfair advantage or disadvantage to the models close to the item generation model. Suppose we have one item generation model trained from LLAMA3, another trained from GPT, and another trained from Mistral. Will the IRT scores calculated from these three item pools agree on which model is better? (A similar argument can be made about the embedding model)

* Related works: https://arxiv.org/pdf/2106.00840 https://aclanthology.org/D19-1434.pdf https://aclanthology.org/D18-1500.pdf

* Wait a second, where are the 180 language models you talked about in the abstract? Are you really human?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduce new method (amortized model-based evaluation) for evaluating generative models using Item Response Theory (IRT) framework. The main contributions include: 1). Using IRT to decouple model performance from test set selection, making evaluation more reliable 2). Propose "amortized calibration" technique to reduce cost of estimating item parameters 3). Develop LLM-based item generator to automatically create diverse test questions 4). Experiments with 24 NLP benchmarks and 180 language models show the proposed method is more efficient and reliable, the methodology uses Rasch's model for IRT implementation and can reduce required test samples by up to 82% compared to traditional methods. While the paper claims that it is model-based evolution and decoupled model performance from the test subset selection, it still needs to test models on some example

### Strengths
- Strong theoretical foundation using established IRT framework but applying in an interesting way for generative model evaluation
- Clear empirical validation with extensive experiments (24 datasets, 180 models)
- Technical details are well explained - for example, equations for Fisher information I(θ) = ∑pi(1-pi) and reliability metrics
- Good visualization and quantitative results (Figure 4 showing goodness of fit metrics)

### Weaknesses
 - Some limitation in generated questions quality not fully addressed. Need more discussion about potential risks of automated question generation such as bias towards model-generated questions
- Empirical results focus mainly on English language tasks - multilingual evaluation missing
- No ablation studies comparing different IRT model choices
- Need more baseline comparisons with other evaluation methods (like Elo scores of LLM arena)
- While the paper claims that it is model-based evolution and decoupled model performance from the test subset selection, it still needs to test models on some examples, which is a major concern of mine

### Questions
No.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the impracticality of current methods for evaluating generative models, as traditional approaches (e.g., classical test theory) are resource-intensive and unreliable when using subsets of benchmarks. To solve this, the authors propose leveraging Item Response Theory (IRT) , which decouples model ability estimation from test set selection, enhancing evaluation reliability and reducing query complexity by up to 82%. The main contriobutions are 3 fold: 1) A large-scale study showing that IRT is more efficient and reliable than traditional methods. 2) Amortized calibration, which predicts question difficulty from content, reducing calibration costs. 3) A conditional item generator that automates question creation based on difficulty, ensuring scalable item bank construction. In experiments, the authors demonstrate that the involvment of IRT can indeed reduce the cost of large scale evaluation.

### Strengths
1. The authors offer a solid theoretical analysis based on Item Response Theory (IRT), which effectively decouples the selection of test samples from the test taker's ability.
2. The applied IRT demonstrates greater robustness against test set selection in reflecting the model’s actual ability, as shown in Figure 3. This robustness becomes increasingly valuable as models grow larger and more resource-intensive in terms of inference costs.
3. The proposal for generating new questions using a Conditional Item Generator is promising, as discussed in Section 4.2. It introduces the possibility of automatically constructing new test datasets, which could streamline and enhance evaluation processes.

### Weaknesses
1. While using Item Response Theory (IRT) to model the evaluation process is valuable, it also introduces an additional understanding barrier for those unfamiliar with these concepts. For example, the term "item parameters" could be simplified to "difficulty," giving readers a more intuitive sense of what the modeling aims to capture.
2. One of the main claims made in the paper is the emphasis on "long-term, adaptive monitoring as models evolve, going beyond static benchmarking" (Line 157). However, the paper does not provide sufficient experimental evidence to support this claim. For example, it does not introduce new models to demonstrate adaptive monitoring and instead relies on conventional approaches like train/test splits. Additionally, the conditional item generator is only tested on a single dataset, which limits the generalizability and persuasiveness of the results. The lack of diversity in the test data for the conditional item generator makes it difficult to assess its robustness and practical utility across different types of evaluation tasks.
3. Another critical issue is the practicality of the proposed system. Traditionally, NLP benchmarks included large datasets, making them easier to encode for analysis. However, recent evaluation trends are shifting toward more challenging tasks with relatively smaller datasets (e.g., using AIME data for testing). This work does not convincingly demonstrate its relevance or necessity in light of this trend. The paper needs to address how the proposed IRT-based evaluation framework can be effectively applied to these smaller, more complex datasets, and how it offers advantages over existing methods in such scenarios.

### Questions
1. Why is it important to provide the dataset context for each question by prepending a brief description before embedding them using LLaMA-3 (as shown on lines 388-389) when fitting two models to predict item parameters?
2. What do the blue and yellow dashed lines represent in Figure 5?

### Soundness
2

### Presentation
2

### Contribution
2
