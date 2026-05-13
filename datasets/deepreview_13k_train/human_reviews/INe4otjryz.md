# Can In-context Learning Really Generalize to Out-of-distribution Tasks?

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
In this work, we explore the mechanism of in-context learning (ICL) on out-of-distribution (OOD) tasks that were not encountered during training. To achieve this, we conduct synthetic experiments where the objective is to learn OOD mathematical functions through ICL using a GPT-2 model. We reveal that Transformers may struggle to learn OOD task functions through ICL. Specifically, ICL performance resembles implementing a function within the pretraining hypothesis space and optimizing it with gradient descent based on the in-context examples. Additionally, we investigate ICL's well-documented ability to learn unseen abstract labels in context. We demonstrate that such ability only manifests in the scenarios without distributional shifts and, therefore, may not serve as evidence of new-task-learning ability. Furthermore, we assess ICL's performance on OOD tasks when the model is pretrained on multiple tasks. Both empirical and theoretical analyses demonstrate the existence of the \textbf{low-test-error preference} of ICL, where it tends to implement the pretraining function that yields low test error in the testing context. We validate this through numerical experiments. This new theoretical result, combined with our empirical findings, elucidates the mechanism of ICL in addressing OOD tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studied the limitations of in-context learning (ICL) on out-of-distribution (OOD) tasks through empirical experiments and theoretical analysis. They pointed out that ICL mainly implements functions from its pretraining distribution rather than learning new functions. Therefore, ICL cannot guarantee ideal performance when ICL data are from OOD distributions unseen during training. While ICL appears capable of handling tasks with abstract labels, the authors show this ability stems from learning retrieval mechanisms during training rather than true OOD generalization. They also provide theoretical insights into how ICL selects which pretraining function to implement when faced with OOD tasks.

### Strengths
1. Novel theoretical insights: The paper provides theoretical analysis of the "low-test-error preference" mechanism in ICL, explaining how models select which pretraining function to implement when handling OOD tasks. 
2. I found the experiments on the abstract label classification interesting. The paper provides a fresh perspective on how models handle abstract label classification, demonstrating it's more about retrieval capabilities than true OOD learning.
3. Besides GPT-2, they use Llama2-7b, a pre-trained language model for evaluation.

### Weaknesses
1. Presentation issues.

(a) In Eq.1, why the prediction is supervised by f(x_i)? Shouldn’t it be f(x_{I+1})

(b) In Fig.2, what is y_i id? Is it same as I_{y_i}? If yes, why not keep using the same notation? If no, please clarify.

(c)Please correct the way how you are using the quote. See examples in the caption of Fig.3.

2. Questions on the training set. The retrieval design in Sec.3.1 is interesting. When the training range is larger (say yi Id in [50, 455]), the test-time performance is better regardless that y_i in [50, 155] aligns better with the evaluation tasks. I wonder if you have same number of training tasks for different range.  If the answer is no, then is it  a fair comparison?  Is it possible that better performance simply comes more training data? Please clarify the number of training tasks for each range. Second, the setup is hard to understand, please improve the writing.


3. Questions about the experiment design. The first and last experiments in Sec.3 are following the same idea, which maps the index of an embedding to new indices based on some pre-specified rules.  I find it hard to understand the motivation here. Are previous works using similar design? If yes, please cite. If no, could you clarify why this setup?


4. Questions about the assumptions when evaluating pretrained models.In Sec.3.3, how is it possible to know an evaluation task is in-distribution or out-of-distribution for a pretrained llama-2-7b? In line 264, the authors said `To ensure the task is far from the pretraining distribution’, are there evidence supporting the assumption?


5. Limited evaluation setups. All conclusions are derived based on either curve fitting or rule-based mapping. The setups are too simple. They are not sufficient to derive convincing conclusions especially when evaluating the behaviors of models with high parameter size.

### Questions
See the comments in the weakness section.


Update:

Sorry for the late response. Most of my concerns were properly addressed. I have raised my score to 6.

### Soundness
2

### Presentation
2

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
This paper investigates the ability of transformer models to generalize to tasks that are OOD compared to its pre-training distribution through in-context learning. They do this through empirical analysis with controlled synthetic tasks and on a pretrained Llama-2-7B model as well as provide some theoretical justification. The core contributions are:
1. The performance of transformers on OOD tasks is similar to the performance of an estimator that learns the ICL examples through GD within the pretrianing function class.
2. The transformers ability to learn and classify abstract concepts in-context can be attributed to its ability to do retrieval and can be learned by doing retrieval on a pre-training distribution of many diverse labels. This fails if the testing function is OOD.
3. Provides theoretical and empirical evidence that when the pretraining distribution contains a mixture of function classes, when tested OOD, models select the pretraining function class that has the lowest test error and match between the train and test input distributions.

### Strengths
**Originality**: This paper adds to the literature on understanding ICL in transformers on synthetic tasks by empirically and theoretically characterizing their behavior on OOD tasks. To my knowledge, this behavior on OOD tasks has not been carefully demonstrated yet.

**Quality**: The paper does thorough, well thought out experiments and provides new theoretical insight.

**Clarity**: The paper is clearly written, well structured and easy to understand.

**Significance**:  The question asked by the paper are significant as it further clarifies the mystery of ICL especially regarding limitations to OOD tasks.

### Weaknesses
 - In section 2, it would be helpful to further clarify what is existing knowledge and what is a new contribution. In fact, I think the presentation would be cleaner if Section 2 and Section 4 were combined into a unified presentation.
- The explanation of the retrieval version of the Llama-2-7B task was hard to understand, it would be helpful to clarify that section
- The conclusion that LLMs cannot learn OOD tasks because its ability to learn abstract concepts from context can be attributed to retrieval felt like a jump in conclusion: see questions).
- I did not understand what hypothesis the experiment in Figure 5 was trying to test and a more clear explanation of why this experiment is useful and what the hypothesis is as an analogy to real world use case would be helpful. It seems like a really whacky OOD task that I am not sure is representative.

### Questions
1. In section 4, the authors demonstrate model selection within the pre-training task distribution. Can you connect this to your results in section 2, i.e. does the transformer get the same error as Gradient descent with the function class that gets the lowest error in Figure 7?
2. What causes the sudden increase in performance after context length size 10 in Figure 6B
3. What do you precisely mean by the claim that "the ability of ICL to perform abstract label classification may not serve as an evidence of learning new tasks."? In this abstract label classification task, learning new tasks is the same as being able to classify OOD labels. This is something you show that models are capable of doing if pre-trained on enough diversity of abstract labels tasks (green line in Figure 4c). It seems like this presents evidence that (in a limited context) transformers can learn new OOD tasks.
4. Can you please explain the motivation behind the experiment in Figure 5 better.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper conducts a series of empirical studies on synthetic tasks aimed to characterize the ability of transformers to generalize to unseen function families using in-context learning (ICL). It finds that while ICL allows generalization to new tasks from known function families, it fails to generalize to tasks from unseen function families instead predicting solutions in terms of the known function families encountered during training that achieve the lowest test-error. It further demonstrates that the strong in-context retrieval ability of transformers can sometimes give a misleading impression of out-of-distribution generalization.

### Strengths
- Characterizing the out-of-distribution generalization ability of in-context learning is an important problem with potential impact
- The experiments are well-designed to investigate the respective hypotheses
- The paper does a good job at referencing and contextualizing existing related work

### Weaknesses
 - The presentation of the paper could be improved, in particular I found section 4.2 hard to follow (see questions) and with the many different experiments often following prior work it was difficult to identify what findings were novel and specific to this paper.
- The theoretical results heavily borrow from [1] (but the paper makes this very transparent)


### Questions
- It is not clear to me whether the Llama2 OOD synthetic word classification task in section 3.3 fails due to a lack in OOD generalization or because of other factors that make this task difficult. One control would be to train a model explicitly on this ICL task to see if it is solvable when it is in-distribution. Would it make sense to run such a control?
- I found Section 4.2 and Figure 8 and Figure 9 hard to read and understand. What exactly is shown in the last row of both of these figures? Why are the losses so high here throughout? I am probably misunderstanding this plot but I would have expected to see that the pretrained ICL model achieves the same loss as the corresponding PT task with the lowest test error.
- Would it be possible to show the loss plots on a log scale (especially Figure 7) to get a better understanding how close the different methods are to each other? Many of the plots contain relatively large values (e.g. due to double descent) which make it difficult to assess how close the best models perform at small loss values. Maybe they could be added to the appendix.
- Are the y-ticklabels of Figure 7b+c correct, i.e. is the loss 10x higher for these tasks? If so, why is that the case?

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
This paper studied OoD performance with in-context learning in Transformers. The notion of OoD was both with respect to the ground-truth data-generating process at inference time and the distribution of inputs. The main finding is that Transformers do not generalize in these OoD settings, and instead make predictions in accordance with the in-distribution task from the pre-training distribution that achieves the lowest test error on the novel OoD task. This core finding holds when considering simple regression tasks (e.g., linear and quadratic regression), retrieval tasks, and mixtures of tasks.

### Strengths
1. The experimental setups are quite easily to follow and well-explained.
2. The tasks introduced in Section 3.3 are quite interesting, as they constitute a simple and meaningful task that we would want a model to generalize to, but we are confident that no such task could have accidentally appeared in the training data.

### Weaknesses
1. The core results are to a large extent unsurprising, and don’t clearly tell us anything new. Transformers are essentially just deep neural network (DNN) sequence models, and we know that DNNs don’t generalize out-of-distribution in the absence of the right kinds of inductive biases. Why, then, would we expect a Transformer to generalize in the OoD settings studied in this paper? For instance, would anyone have ever genuinely expected a Transformer trained on (x,y) sequences with a linear relationship to then generalize to (x,y) sequences with quadratic relationships? I expect that the answer is no, and that almost everyone familiar with the deep learning literature will be unsurprised by the empirical findings in Sections 2, 3, and 4. Lack of unexpected results is my primary critique of this paper.
2. This work did not engage with the dominant theory of ICL: that it does Bayes-optimal prediction. This is particularly surprising, since the Bayes-optimal prediction framework seems to account for all of the results. To account for Section 2: the Transformer learns a prior over the pre-training tasks and so when confronted with a new one, the best it can do is implement the function with non-zero prior that best explains the novel OoD data. To account for Section 4: the learned task prior includes a prior over task classes, and given some context the posterior is higher over the tasks that are consistent with that context.
3. Several typos and ungrammatical sentences throughout the paper that make it more difficult to read. For example, there is even a typo in a subsection title “3.3 REAL-WORLD LLMS MAT NOT NECESSARILY IN-CONTEXT LEARN NEW TASKS”. The paper requires a thorough proofread.

### Questions
1. Which findings in particular do the authors believe are genuinely surprising to most deep learning researchers?
2. What findings from the paper can’t be explained through the theoretical Bayes-optimal prediction framework for ICL?

### Soundness
3

### Presentation
2

### Contribution
1
