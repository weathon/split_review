# Dynamic Demonstrations Controller for In-Context Learning

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
In-Context Learning (ICL) is a new paradigm for natural language processing (NLP), where a large language model (LLM) observes a small number of demonstrations and a test instance as its input, and directly makes predictions without updating model parameters. Previous studies have revealed that ICL is sensitive to the selection and the ordering of demonstrations. However, there are few studies regarding the impact of the demonstration number on the ICL performance within a limited input length of LLM, because it is commonly believed that the number of demonstrations is positively correlated with model performance. In this paper, we found this conclusion does not always hold true. Through pilot experiments, we discover that increasing the number of demonstrations does not necessarily lead to improved performance. Building upon this insight, we propose a \textit{\textbf{D}ynamic \textbf{D}emonstrations \textbf{Controller}} (\textit{\textbf{D$^2$Controller}}), which can improve the ICL performance by adjusting the number of demonstrations dynamically. The experimental results show that D$^2$Controller yields a 5.4\% relative improvement on eight different sizes of LLMs across ten datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an algorithm to select the right number k of examples per class to compose an in-context learning prompt. The proposed Dynamic Demonstration Controller (D2Controller) algorithm chooses k based on a series of experiments with N different in-context learning example selections. In each experiment a validation set is chosen in a special way from the remaining training data that did not make it into the prompt. The k is chosen to maximize the average validation set performance over the N in-context learning support sets. 

The paper’s novelty is in the selection of the validation set for each of the N in-context learning support sets. For each of the C classes, the paper chooses an example out of the remaining training data by maximizing a score called IICScore. I did not fully understand the intuition behind the score, but it involves balancing the example’s similarities to the class of interest and to the other classes. 

The paper key points are that:
- D2Controller selects k better than the typical settings from the prior work
- D2Controller selects k better than taking as many examples as possible
- D2Controller selects the validation sets better than taking *the same number of validation examples* at random
- D2Controller is also helpful when it is combined with other demonstration selection or ordering methods

### Strengths
The paper is most clearly written and methodologically sound. The research question makes sense, the set of baselines is large and appropriate. But there may be one crucial baseline that's missing (see Weaknesses Section).

### Weaknesses
This is basically a hyperparameter selection paper, and as such it is missing a key baseline: what if one uses as many examples as possible for selecting k? That would correspond to the classic setting of having your dataset split into training, validation and test sets. While it would be more computationally expensive at the hyperparameter selection time, the key concern in practical applications of LLMs is the inference speed at test time, which would not be affected by using more validation examples to select k.

I imagine that one justification for using fewer validation examples could be that there might be not that many examples available overall. The paper does not discuss this possible constraint though. The set of examples available for selection with IICScore would have to also be restricted.

Some aspects of the paper were difficult to understand, see the next section of the review. I found Figure 5 very dense and difficult to understand. I did not find the motivation for IICScore clearly explained and compelling.

### Questions
- “To measure similarities, we transform each sentence x to a vector representation x, which essentially is a language modeling distribution, by querying LLMs with x and obtaining the output” - what does this mean exactly?
- Is your Oracle baseline using the test set examples? If it is, your explanation as to why it is not practical on Page 7 is a bit confusing. Because Oracle would not be a possible practical method, it’s just a hypothetical baseline from above. 
- What set of in-context examples is used at the test time? Is it one the N sets you used to select k, or is it another one?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors study in-context learning and how different numbers of in-context examples affect an LLM's performance on a classification task. Specifically, the authors design and conduct some pilot experiments and report that a large number of in-context examples does not always guarantee the best model performance. Motivated by this, the authors propose the $D^2$ Controller, a method that dynamically determines an optimal number $k$ for $k$-shot ICL given a dataset. 

In the $D^2$ Controller algorithm, for a given $k$ value, 
- first, $N_s$ groups of in-context examples are sampled; 
- second, for each group, a set of evaluation data points is selected, according to the proposed IICScore, which measures the similarity between a evaluation data point and the in-context examples in the group;
- third, the accuracy of an LLM on the selected evaluation data, using the corresponding in-context examples, is obtained; 
- averaging all the above accuracy scores over the $N_s$ groups resulting an overall score for $k$;
- finally, the optimal $k$ is selected according to the setting produces the highest averaged accuracy.

In experiments, the authors include a wide range of LLMs, including open-sourced LLMs and ones that can only be accessed via online APIs. The author also include 10 classification datasets. Results suggest that their method can indeed determine a better $k$ value than default settings used in prior works.

### Strengths
1. Useful topic: As the authors describe, there are few work studying how the number of demonstrations impacts an LLM's performance in the ICL setting. I agree this is an important topic because empirically the study could benefit millions of LLM practitioners. 

2. Neat idea: I think the method is well designed, I especially like the IICScore part, where it takes both inter- and intra-class similarity into consideration. 

3. Experiments and results: The authors study their methods on a wide range of LLMs and ten datasets. The authors run five seeds and report average / standard deviation. Results show that the proposed method outperforms baselines. The authors also provide a list of ablation study to help understand their method.

### Weaknesses
Please see my questions and concerns below.

### Questions and concerns
Q1. How does $D^2$ Controller compare to a simple baseline where $k$ is optimized as a hyperparameter using a validation set?

Q2. How does $D^2$ Controller work with `classification` tasks where options have no consistent meanings? For instance, below is a datapoint taken from the BigBenchHard dataset:
  ```
  Jane quited her job on Mar 20, 2020. 176 days have passed since then. What is the date today in MM/DD/YYYY?
  (A) 09/12/2020
  (B) 11/12/2020
  (C) 12/12/2020
  (D) 09/12/1961
  (E) 09/17/2020
  ```
In this case, computing IICScore per class makes less sense. Could the author provide more insights on this?

Q3. How does $D^2$ Controller work when $k < |c|$?

Q4. $D^2$ Controller measures data similarity in representation space. Did the authors compare different text encoders and see whether / how they affect $D^2$ Controller?

Q5. In my opinion, adding GPT-3 in Section 5.4 could make the analysis stronger.

Q6. The authors report a setting where they combine KATE and $D^2$ Controller, this is interesting. Now, KATE is selecting $k$ different IC examples per test data point, where $k$ is determined by $D^2$ Controller at a dataset level. While I understand the setting, could the authors provide some insights on, is it necessary, or is there a way to dynamically determine the $k$ for every test data point? 

Q7. Could the authors provide some insights on why sometimes LLMs fail to benefit from more IC examples? Do stronger LLMs (e.g., gpt-4) suffer less from this?

### Typos and minor stuff
1. There is an extra quotation mark in the 3rd line of Section 5.1, Datasets.
2. DBPedia does not seem to be a good dataset to include in this work, because the longer text, there can be at most one example per class and thus it is not helpful to demonstrate the $D^2$ Controller. 
3. In Section 5.4.4, the authors mention that they get better performance with fewer demonstrations. Maybe a more straightforward way to present this is to report (on average) how many tokens their method queries an LLM, and how does that compare to prior work (default $k$).

### Questions
### Questions and concerns
Q1. How does $D^2$ Controller compare to a simple baseline where $k$ is optimized as a hyperparameter using a validation set?

Q2. How does $D^2$ Controller work with `classification` tasks where options have no consistent meanings? For instance, below is a datapoint taken from the BigBenchHard dataset:
  ```
  Jane quited her job on Mar 20, 2020. 176 days have passed since then. What is the date today in MM/DD/YYYY?
  (A) 09/12/2020
  (B) 11/12/2020
  (C) 12/12/2020
  (D) 09/12/1961
  (E) 09/17/2020
  ```
In this case, computing IICScore per class makes less sense. Could the author provide more insights on this?

Q3. How does $D^2$ Controller work when $k < |c|$?

Q4. $D^2$ Controller measures data similarity in representation space. Did the authors compare different text encoders and see whether / how they affect $D^2$ Controller?

Q5. In my opinion, adding GPT-3 in Section 5.4 could make the analysis stronger. 

Q6. The authors report a setting where they combine KATE and $D^2$ Controller, this is interesting. Now, KATE is selecting $k$ different IC examples per test data point, where $k$ is determined by $D^2$ Controller at a dataset level. While I understand the setting, could the authors provide some insights on, is it necessary, or is there a way to dynamically determine the $k$ for every test data point? 

Q7. Could the authors provide some insights on why sometimes LLMs fail to benefit from more IC examples? Do stronger LLMs (e.g., gpt-4) suffer less from this?

### Typos and minor stuff
1. There is an extra quotation mark in the 3rd line of Section 5.1, Datasets.
2. DBPedia does not seem to be a good dataset to include in this work, because the longer text, there can be at most one example per class and thus it is not helpful to demonstrate the $D^2$ Controller. 
3. In Section 5.4.4, the authors mention that they get better performance with fewer demonstrations. Maybe a more straightforward way to present this is to report (on average) how many tokens their method queries an LLM, and how does that compare to prior work (default $k$).


### Nov 21

I have read the authors response including those answering other reviewers' questions. I appreciate the authors' effort on clarifying things so I'm happy to raise my score a bit. **However, please note, I give 6 -> 8 only because there is no option of 7. I don't think the current version is as mature as 8.** (E.g., the authors have included quite a bit of new experiments during the rebutal period, mainly in the appendices. It may require some efforts to merge some into the main content, with some non-trivial rewriting.)

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to determine the optimal number of example demonstrations for in-context learning. The authors argue that the common belief that the number of demonstrations is positively correlated with model performance does not necessarily hold true. Therefore, it is critical to decide on the optimal number of example demonstrations. In this work, the authors propose a method to select representative in-context learning examples that minimize intra-class distance and maximize inter-class distance for each group of in-context examples from the training dataset. They then use these selected examples as a validation set to adjust the number of demonstrations dynamically. The authors perform experiments on a wide range of datasets and demonstrate the effectiveness of their proposed method.

### Strengths
1. The authors have done an excellent job of motivating the problem and providing a thorough description of their research. The paper is well-written in a high-standard and easy to understand.

2. The authors have conducted extensive experiments to demonstrate that the length of in-context learning examples is not necessarily better. Furthermore, the experimental evaluation shows that their proposed method has promising performance.

3. Validation set selection is critical to in-context learning. Compared to other works, the authors propose a method to carefully curate a representative validation set. It is meaningful and makes sense.

### Weaknesses
The novelty of this paper is my main concern. The idea of minimizing intra-class distance and maximizing inter-class distance has been widely used in previous machine learning works [1][2]. Similarly, the paradigm of using a validation set to choose in-context learning examples/tune in-context learning hyperparameters has also been well-explored in previous works [3][4]. If the author can provide more content to illustrate their unique contribution, I will consider improving my score.

### Questions
Could the authors provide more information on the cost of “Evaluation Examples Selection” and “Accuracy-based Evaluation” stages?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a dynamic demonstration controller to select the optimal number of demonstrations in the prompt. The proposed method can achieve similar performance with Oracle demonstration selection across different datasets and across different models. The proposed method can be integrated with existing prompt selection methods to achieve higher performance.

### Strengths
- The paper is clearly written and easy to follow.

 - The ablation study is comprehensive.

### Weaknesses
 - The evaluation and discussion can be further improved. 

    - It would be interesting to discuss what causes the observations in the pilot experiments. 

     - It is important to conduct experiments comparing demonstration number selection and demonstration selection. The original Table 2 shows that the proposed method can further improve based on the demonstration selection. However, it is still unclear which one is more effective among demonstration selection and dynamic demonstration number selection.


 - The limitation of the method is not fully discussed.

### Questions
- In terms of the limitations, when will the method fail, and when will the method have a good performance?

 - In Table 2, can you also show the performance of the “default” method, which is randomly sampling k-shot demonstrations? And also show the performance of “D2Contoller” along? It will be helpful to understand which one is more effective among demonstration selection and demonstration number selection.

 - What may cause the observations in Pilot experiments? For instance, in Figure 2, what aspects of the datasets cause the different optimal k for different datasets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
