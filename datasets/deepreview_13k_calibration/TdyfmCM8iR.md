# Latent Concept-based Explanation of NLP Models

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Interpreting and understanding the predictions made by deep learning models poses a formidable challenge due to their inherently opaque nature. Many previous efforts to explain these predictions rely on input features, specifically, the words within NLP models. However, such explanations are often less informative due to the discrete nature of the words and their lack of contextual verbosity. To address this limitation, we introduce Latent Concept Attribution (\LACOAT{}), which generates explanations for predictions based on latent concepts. Our intuition is that a word can exhibit multiple facets depending on the context in which it is used. Therefore, given a word in context, the latent space derived from our training process reflects a specific facet of that word. \LACOAT{} functions by mapping the representations of salient input words into the training latent space, enabling it to provide latent  context-based explanations of the prediction.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes latent concept attribution method, which works by (1) discovering concepts from a corpus based on hierarchical clustering of representations (2) selecting tokens that has high importance in the sentence (3) mapping selected tokens to extracted concepts with a trained classifier (4) generating natural language explanations with concepts and LLMs. Experiments show that the proposed approach produces plausible explanations.

### Strengths
- Explaining LLM predictions with concepts and natural language is an interesting research direction which is beneficial to broader users of NLP systems.
- Break-down evaluation of each component in the proposed method in Sec. 3.3 is useful.

### Weaknesses
 **In the current state, the most significant weakness of the paper is the experiments.**

- The paper lacks comparison to other explanation algorithms in the experiments.
- The quality of the generated natural language explanation is evaluated with case studies only.

 I understand that evaluation of explanation-based algorithms are tricky, especially for natural language explanations that the authors study. To evaluate utility of explanations, the authors can perform human evaluation. Here I suggest some baselines and ablation studies (1) generating rationales with LLMs (Plausifier in Sec. 2.4) directly based on inputs and predictions (2) skipping the conceptmapper, and directly generating explanations with extracted salient words (in Sec. 2.2) and LLMs. For evaluation of utility, there is a number of references such as [1].

[1] Sun et al. Investigating the Benefits of Free-Form Rationales, 2022

I also hope to see quantitive evaluation of faithfulness, which is crucial for explanation algorithms, but is not quite intuitive for generative explanations. I hope to hear author's thoughts about this.

**The advantage of concept-based explanation to other attribution-based algorithms is not clear from the experiments.** 

In introduction, the authors claim that a limitation of attribution methods is because of "multi-facet of words in different contexts". I hope to see the point supported by case studies in experiments.

**Experiments are on sequence tagging and classification tasks only**

I wonder whether concept-based explanations are applicable to more complex reasoning tasks, like reading comprehension and commonsense reasoning. In this case, what explanation outputs do the authors expect?

### Questions
Following my points mentioned in the weakness, I hope authors can address:
1. What is the plan for evaluating practical utility and faithfulness of the generated explanations?
2. How can the approach be applied to more complicated NLP tasks such as reading comprehension and commonsense reasoning?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a latent concept attribution method called LACOAT that goes through a set of modules and generates explanations for predictions based on latent concepts. Their method hinges on the fact that words can have different contextualized senses and they assume the latent spaces of models utilize this.

### Strengths
1) The motivation is sound. I understand and buy the fact that we need our models to be able to explain predictions for numerous reasons and having a way to do this via the latent concepts the model has encoded is a great way to try and do this.

### Weaknesses
1) I think a major weakness of the overall method is poor scalability. Clustering at scale would be quite expensive and large pretrained datasets are in the 3T total token range (e.g. Dolma) which would definitely be infeasible. The computational cost of clustering high-dimensional latent representations for such massive datasets is a significant hurdle. Furthermore, the method's reliance on fine-tuning for each task before extracting latent concepts limits its applicability to scenarios where pre-trained models are used directly without task-specific adaptation.

2) I think the experimentation could be extended. POS and sentiment are very small and relatively simple. The types of models that you're fine-tuning are also not very broad (no decoder only models like GPT here). What happens when you evaluate on an NLI task? Could you extend this to work on a task like question answering and evaluate that? The current experiments do not adequately demonstrate the method's robustness across diverse tasks and model architectures. The lack of evaluation on more complex tasks like NLI or question answering limits the generalizability of the findings. Additionally, the absence of decoder-only models in the evaluation raises concerns about the method's applicability to a broader range of models.

3) It's really hard for me to figure out the appropriate baselines here, which I think is a potential weakness. It's hard for me to contextualize the results you have. The lack of clear baselines makes it difficult to assess the effectiveness of the proposed method. Without comparisons to existing explanation techniques, it is challenging to determine whether the method provides a significant improvement over existing approaches.

### Questions
1) How would/could you modify your algorithm to work with a pretrained LM without exhaustive fine-tuning on a target task?

2) If you have some resource limitations, but wanted to scale up these experiments to a much larger model (e.g 1.5B parameter model), would this be straight forward to do? Could you fine-tune on a subset?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper attempts to explain a model's prediction using latent concepts. The proposed approach is comprised of a few loosely connected components including concept discoverer, prediction attributor, concept mapper, and plausifyer. Concept discoverer clusters words while disambiguating them based on their senses using the training data. Prediction attributor uses either a set of handcrafted rules, or integrated gradient. The experiments evaluate each component and examples are provided throughout the paper.

### Strengths
- S1. The paper raises an interesting question about ambiguous natural language explanation and tries to disambiguate the sense (latent concept).
- S2. The paper provides examples and experiments.

### Weaknesses
 - W1. The components are loosely connected, which isn't necessarily a bad thing by itself. However, each component is either simplistic or an existing approach.
- W2. The evaluation is done with automatically generated labels, and in this particular case, they can be deceptive because of the last layer assumption used to generate them. Also, if they are the targets, one can just adopt the method used to generated labels to replace the proposed method.
- W3. The evaluation is limited to simplistic tasks only.

### Questions
- Q1: Why do you use squared Euclidean distance which is not a metric?
- Q2: How is this different from topic modeling, or many other word sense disambiguation especially as other components are mostly direct application of existing approaches?
- Q3: What are the examples of the ambiguity handled with the concepts in the evaluation? Are they apparent with the input text?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
