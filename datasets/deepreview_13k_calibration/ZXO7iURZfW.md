# Automated Feature Engineering by Prompting

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Automated feature engineering (AutoFE) liberates data scientists from the burden
of manual feature construction, a critical step for tabular data prediction. While the
semantic information of datasets provides valuable context for feature engineering,
it has been underutilized in most existing works. In this paper, we introduce
AutoFE by Prompting (FEBP), a novel AutoFE algorithm that leverages large language
models (LLMs) to process dataset descriptions and automatically generate
features. Incorporating domain knowledge, the LLM iteratively refines feature
construction through in-context learning of top-performing example features and
provides semantic explanations. Our experiments on real-world datasets demonstrate
the superior performance of FEBP over state-of-the-art AuoFE methods. We
also conduct ablation study to verify the impact of dataset semantic information
and examine the behavior of our LLM-based feature search process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an automated feature engineering solution by exploiting the data description to automatically generate new features. The idea is to leverage LLM and provide it with descriptive information of the dataset in the prompt to guide the search for effective features. The paper proposes a compact feature representation in the prompt and instructs the LLM to iteratively generate feature augmentation code that perform data transformation based on a set of pre-defined operators. Experimental evaluation demonstrates it effectiveness by comparing against the baselines.

### Strengths
S1. The problem of automated feature engineering is an important problem to solve given the significant effort a data scientist/analyst has to spend in a typical life cycle of data science workflow. The idea of leveraging LLM to interpret the descriptive information about the dataset and performing the appropriate data engineering operations can speed up the cycle.

S2. The paper is written with running examples. The core technical part is clear and easy to follow.

S3. The experimental evaluation includes comparison against the state-of-the-art technique. It demonstrates superior performance in some of the cases.

### Weaknesses
W1. While acknowledging the importance of the problem and the high level idea, the paper does not provide enough justification/discussion on its difference to CAAFE. CAAFE which is an existing work shares the same vision and solves the same problem by using LLM to iteratively augment the dataset to achieve better accuracy. What are the unique research challenges?

W2. The experimental evaluation does not show significant improvement against CAAFE.

W3. Adding some ablation studies will be appreciated. There lacks of experimental evaluations to support the design choice, e.g. cRPN.

### Questions
Q1. How is the vision and high level idea different from CAAFE? What are the unique research challenges undressed by CAAFE and are tackled here?

### Soundness
2

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
The paper investigates the application of prompting LLM for automatic feature engineering over structured (tabular) data. It proposes an iterative in context learning approach (FEBP), which derives new features from raw tabular data. The iteration first leverages metadata and examples to generate new features, which are subsequently evaluated and added to the prompt, if they perform well. The approach stops if the model performance does not improve. FEBP is based on GPT-[3.5,4]. It is evaluated on 3 classification and 4 regression datasets against three automatic feature engineering methods.

### Strengths
The paper presents a sound approach for encoding tabular data for prompting and deriving new features. The approach is easy to replicate and can be reused quickly to train downstream models. Compared to deep embedding based approaches, the feature and their interactions are still explainable to a certain extent (with some effort and post processing of course).

### Weaknesses
 **Evaluation**
 - The significance of some results is unclear: Does the number of features in the initial prompt really have a significant effect on the performance, if the mean lies between [0.6823, 0.684] (Table 5). The same holds for the temperature metric in Table 4 [0.8169, 0.8197]. 
 - The approach is not compared against modern automatic feature interaction learning approaches. This could provide a upper bound on the performance:
    - DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems
    - AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks

### Questions
- How many responses on average are necessary to train a downstream model for classification and/or regression?
 - Did you consider using reflection and providing previous prompts as input to the model apart from in context examples?

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
This paper propose a novel AutoFE algorithm that leverage LLMs to automatically process dataset descriptions and generate new features. Specifically, LLM produce some feature with the semantic information of dataset and then iteratively refines feature construction with new output example features. This method of using LLMs not only reduces manual effort, but also proves in experiments that its effect reaches SOTA in AutoFE.

### Strengths
1. Experiments are tested on multiple real-world datasets (or tasks)
  
2. The writing of the paper is complete and clear, making it easy to read.

### Weaknesses
1. The new feature space generated by this method is limited, and it can only generate new features based on given operators.
  
2. The experimental conclusions in Table 2 are not consistent. The results of GPT3.5 are better than those of GPT4, which is counterintuitive. I think an additional experiment is needed to reveal the reason for this, and the speculation in line 320 does not explain the reason for this phenomenon.
  
3. Innovation is limited. In my opinion, this method is a prompting method designed based on LLMs. The entire framework implements automated FE through LLM simulation experts but lacks more detailed analysis and module design. For example, I think the analysis of temperature is redundant.

### Questions
See above.

### Soundness
3

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
Automated feature engineering (AutoFE) uses high-level algorithms and models to automate the FE
process such that the performance is comparable to domain experts. Existing AutoFE methods compute
and evaluate a large number of features in a trial-and-error manner. The authors propose a method that
leverages LLMs to do 'effective, efficient, and interpretable feature engineering.' Their main contributions
are to generate features in string representations while providing semantic explanations, to benchmark
the performance of the approach against state-of-the-art baselines using both GPT-3.5 and GPT-
4, and to investigate the impact of semantic context on this approach.

### Strengths
--The problem is obviously an interesting one, and the authors write it up with sufficient clarity. The paper is very readable. 
--There is some attempt at formalism, which I do appreciate. Far too many papers only describe a problem 'intuitively', and this is usually not adequate for a scientific venue in my opinion. 
--In some cases, the experimental improvements are decent, and I am particularly appreciative that the authors put in significance results.

### Weaknesses
There are two main weaknesses. The first is simply the nature of the contribution: I am not convinced that there is anything significantly novel or surprising here. As the authors state, LLMs have a lot of background knowledge that can be used to generate useful features, and the second 'self-correction' mechanism that subsets constructed features based on performance evaluation is not new either. It has been used a lot in other such LLM-related works, such as in the text2sql problem. I took a close look at the algorithm that the authors put on page 5 but it turns out that it's just a long way of expressions the rather simple formulation in figure 1. 

A much more significant weakness is in the experimental section. In carefully looking at the results, I am seeing hardly any difference between the authors' approach and baselines when using classifiers like Light-GBM and random forests. The only real difference seems to be in linear models, and I don't see why on the basis of this one model we should give the authors' approach too much credit.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
2
