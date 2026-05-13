# How Transformers Solve Propositional Logic Problems: A Mechanistic Analysis

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Large language models (LLMs) have shown amazing performance on tasks that require planning and reasoning. Motivated by this, we investigate the internal mechanisms that underpin a network's ability to perform complex logical reasoning. We first construct a synthetic propositional logic problem that serves as a concrete test-bed for network training and evaluation. Crucially, this problem demands nontrivial planning to solve. We perform our study on two fronts. First, we pursue an understanding of precisely how a three-layer transformer, trained from scratch and attains perfect test accuracy, solves this problem. We are able to identify certain ``planning'' and ``reasoning'' mechanisms in the network that necessitate cooperation between the attention blocks to implement the desired logic. Second, we study how pretrained LLMs, namely Mistral-7B and Gemma-2-9B, solve this problem. We characterize their reasoning circuits through causal intervention experiments, providing necessity and sufficiency evidence for the circuits. We find evidence suggesting that the two models' latent reasoning strategies are surprisingly similar, and human-like. Overall, our work systemically uncovers novel aspects of small and large transformers, and continues the study of how they plan and reason.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a mechanistic analysis of how LLMs solve reasoning problems in propositional logic.
The authors first construct a problem template in which the correct reasoning must go through either a "LogOp chain" or a "Linear chain", where each problem instance randomly selects which chain to use.
Then, the authors analyze the behavior of a small GPT-2-like model on such problems and identify the behavior of each layer and each head.
Moreover, the authors use linear probing and activation patching to analyze the behavior of Mistral-7b on this dataset and find that there are four types of attention heads critical to logical decision-making.
This paper presents techniques with which researchers can better understand the reasoning mechanism of LLMs.

### Strengths
This paper presents an interesting experiment setup and thorough analysis.
I appreciate the pairing of small-model and large-model experiments: the small-model case lets one perform a more exhaustive analysis that then informs intuition for analyzing the large-model setting.
Of particular interest are the authors' findings for the four kinds of attention heads for Mistral-7b, and this is useful for better informing future directions.
Moreover, the techniques introduced for analyzing Mistral-7b would also be useful for other researchers.

### Weaknesses
The paper discusses many technical details with insufficient references to figures or mathematics.
This means that the reader can easily get lost.


For example, I had trouble following the technical details of Section 3.
I suspect this is because the paper assumes familiarity with the standard transformer architecture and uses terminology like "layer-2 embedding" and "layer-3 attention" without first introducing a reference figure or some mathematical definitions --- thus increasing the mental load on the reader.
For accessibility and clarity, I would greatly appreciate a figure with which key vocabularies are defined.
This is feasible because a 3-layer, 3-head model is quite small, and the Section 3 text makes heavy reference to many of these components.
Crucially, the 3-point description of the mechanism in Section 3.2 would benefit from such a reference figure.


Adding arrows on the lines would help readability in Figure 3.


Section 4.2's causal mediation analysis is hard to follow, and I think some examples would help the reader.

### Questions
What does Figure 2 show?

What was the motivating intuition that the first token (before CoT) might be important?

### Soundness
3

### Presentation
1

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper provides an analysis into how transformers may solve propositional logic problems which require some degree of reasoning and/or planning using the rules of logic to check whether a given statement is entailed using the provided facts. The authors investigate two different kinds of transformers. The first kind is a vanilla 3-layer 3-head transformer trained from scratch to solve such problems. The second is an investigation into the Mistral-7B LLM which has been trained on a large amount of data and seems to exhibit reasoning capabilities.

For the problem setup, the paper proposes a simple propositional logic problem with two different types. In the first type, two separate implication chains are connected together by a logical operator (assuming conjunction or disjunction since it is not clearly mentioned and these appear in lines 290-291). Thus, the antecedent is two chains of implications connected by an operator. The query is the consequent (a single proposition) and the query asks the truth value using the rules of inference. Similarly, the linear chain is simply a sequence of implications whose consequent is again a single symbol. 

The QUERY token is the terminating node of the chain and in this paper seems to be a single proposition.

The paper trains a decoder-only transformer s.t. it attains 100% accuracy on the training set. It is unclear whether there is a test set since their is no mention of it. The LogOp chain is queried 80% of the time with the linear one being the remainder. Their evaluation consists of a string match where an answer is correct iff all output tokens exactly match the ground truth.

The authors then analyze the cosine similarity of the Query token for the LogOp and Linear chains and find that there exist special routing chains that existing depending upon whether a LogOp or Linear chain is being queried. One interesting ablation here is that for linear chains of length 3, the answer is already available at layer 2. The authors train a classifier using the output of this layer and show that it is able to achieve 97%  accuracy. The same ablation or data for the LogOp is not mentioned however and instead a separate analysis is performed.

The next analysis is that of Mistral 7B where the authors use causal mediation analysis and looks for differences in activation function values between the two type of queries and provide insights from these results as well. The authors provide some soft out-of-distribution (OOD) analyses here by swapping locations of linear rule for tokens.

### Strengths
S1. The paper makes a detailed insight into the reasoning capabilities of transformers.

S2. The paper is generally well-written and the topic is important for the broader AI community. 

S3. The paper shows that transformers can (within reason) learn to reason since they appear to have planning circuits.

S4. The techniques employed are intuitive and convincing.

### Weaknesses
W1. The data model is quite simple and I am not sure if this analysis can provide a definite answer to a broader claim of whether LLMs can reason. While I appreciate the simplicity it is not clear why a transformer would not be able to perfectly learn such a simple data model. A single perception can learn the AND truth table so I am not sure why such a data model was selected. The propositional logic problems are essentially a series of implications, and the model is trained to predict the final consequent. This setup, while controlled, doesn't fully capture the complexities of real-world reasoning where multiple premises and more intricate logical structures are involved. The lack of negation, quantifiers, or more complex logical operators limits the scope of the analysis.

W2. One complaint in the writing is that it is absolutely unclear whether there exists a train and test set. This forms a major part of the paper so I was surprised that it was not included. I am not sure if 100% accuracy is on the training set or the test set? Was there any OOD data?
What is the size of the training set? The data model is quite simple (no negations as well) and it would not take many samples to learn such a function I think.

W3. Ablation 3.2.2. is interesting but fails to provide accuracy for the LogOp chain. The hypothesis would make sense if that has low accuracy. Similarly, there is no data on reasoning lengths or reasoning chains of length 4, 2 etc. These ablations would provide more insights into the capabilities IMO. Do you have any data with a linear chain like $p_1 \rightarrow \ldots \rightarrow p_n$.

W4. Implications and Bi-conditions do not really exist in logic in the strict sense since they can be expressed using and, not, and or. Have the authors performed OOD tests that can replace one of the $a \rightarrow b$ statements with $\neg a \lor b$.

### Questions
Thank you for your detailed examination. This is quite interesting work. Please address my comments in the weaknesses. Im happy to discuss further. I hope the authors can resolve my concerns.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the features that allow transformers and LLMs to reason about problems formulated in propositional logic. It also tries to derive some general lessons from these findings.

### Strengths
The authors manage to put their research in context and describe to some detail the current state of the art.

### Weaknesses
1) The authors are able to identify some feature of small transformers and Mistral-7B, an LLMs, which seem to facilitate learning and solving problems in propositional logic. But the actual impact of these features is not exactly clear. Specifically, while the authors point to certain attention heads or embedding layer activations, the causal link between these features and the model's logical reasoning ability remains weak. It's unclear if these features are necessary or sufficient for the observed behavior. Also, at the end of the introduction the authors discuss a set of assumptions they make, in order to keep the problem at hand tractable, which however impact on the generality and significance of their findings.

2) The type of problems as described in Sec. 2 is rather specific and restricted. The propositional logic problems considered are quite simple, involving a limited set of logical connectives and a fixed structure. This raises concerns about whether the findings generalize to more complex propositional logic problems, or even to other forms of logical reasoning. So, the value of the contribution is somewhat limited.

3) The significance of the results obtained in the paper is not clear. I'd say that the methodology itself is not clear: what insight are to be obtained by analysing the structure of transformers? Moreover, the usefulness and applicability of such results is not clear either. The evidence discovered seems to be mainly anecdoctic, pointing to very specific feature of the architectures, whose meaning or interpretation is quite obscure. The authors do not provide a clear framework for how these specific architectural features contribute to the overall reasoning process, nor do they show how these findings can be used to improve or debug models.

### Questions
1) The authors say that "these models exhibit deep language understanding and generation skills". It is not clear in which sense the understand of language that LLMs have is deep, as it is mainly next token prediction.

2) In the answer on p. 3, it appears that "V implies E; E TRUE". It is not clear to me why E should be true. Also, it is not required that E is true to derive A.

3) It is not clear what the authors mean when they say that "the transformer mentally process the context and plan its answer". In what sense can we assign a mind to transformers?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors explore the mechanisms by which LLMs/transformers solve propositional logic problems. They work in two steps: first, they train a small transformer (3-layer 3-head) on a very specific propositional logic problems, to study in detail how transformers work, before considering a large pre-trained LLM (Mistral 7B) and trying to replicate their findings. The authors claim a very precise and human-like reasoning process (p4, section 3.2) for the transformer they trained.

### Strengths
Strengths:

S1. To understand how LLMs/transformers generalize symbolic problem is a very timely and interesting topic. 

S2. The overall protocol to first test a small transformer then a larger LLM makes perfect sense.

S3. The first claim on a routing signal between logOp and Linear chains is convincing. (figure 2)

### Weaknesses
Weakness:

W1. The biggest shortcoming lies in the problem chosen. While Mistral 7B  generalizes from what it learnt, this is simply not the case of the transformers the authors trained, because the logical problems is overly simplistic: from what I understood, there are at most 10 cases considered, up to renaming of variables, and each of these cases is seen around 100.000 times by the transformer ( with different variable names). Hence, there is no generalization of reasoning, just a classification of which of the (at most 10) cases is witnesses (this is actually even partially backed-up by the own author experiments), and copy of the associated answer (among 10), with a correct instantiation of variable names. Far away from the advertised “solving of propositional problem” study in the title.

The at most 10 cases: 

-the query symbol (A in the example) is in the linear chain, and the first symbol is true in Facts (A true).

-the query symbol (A in the example) is in the linear chain, and the first symbol is false in Facts (A false).


-the query symbol (A in the example) is in the LogOp, the operator is "and", and both first symbols are true (A true).

-the query symbol (A in the example) is in the LogOp, the operator is "and", and top input symbols is false in Fact (the other is true) (A false).

-the query symbol (A in the example) is in the LogOp, the operator is "and", and bottom input m symbol is false in Fact  (the other is true) (A false).

-the query symbol (A in the example) is in the LogOp, the operator is "and", and both input symbol are false in Fact  (A false).


-the query symbol (A in the example) is in the LogOp, the operator is "or", and both first symbols are true (A true).

-the query symbol (A in the example) is in the LogOp, the operator is "or", and top input symbols is true in Fact (the other is false) (A true).

-the query symbol (A in the example) is in the LogOp, the operator is "or", and bottom input symbol is true in Fact  (the other is false) (A true).

-the query symbol (A in the example) is in the LogOp, the operator is "or", and both input symbol are false in Fact  (A false).


Hence, the transformer does not learn to generalize, it just learns to check symbols at different places for equality, following at most 10 different patterns.

The fact that there is a strong routing as shown in Figure 2 is thus extremely unsurprising.

Actually, there seems to be more routing hidden in figure 2 (but not as clear as the logOp/Linear chain), e.g. whether "and"/"or" is the logical operator.

W2 (Edit: partially fixed) another important issue, the fact that there is no precise definition of the very logical problem considered (see questions below). One revealing case, the simple example of formula page 3 is incorrect:
Answer: …. "V implies E, E true" … , which is incorrect as "Facts: V False".
Also, “minimal” (proofs) should be defined and used correctly. There are at least different 2 reasonable definitions of minimality.

Some Questions:
Q1- Is there exactly one LogOp and exactly one Linear Chain. (It is what I guess after reading 6 pages, but this is not precisely explicitated, whereas this is a crucial information to understand the transformer being trained).
Q2 - Can some symbol be common between the LogOp and the Linear chain, in particular the final (query) symbol? If yes, then the 10+ sentences with "*the* linear case" and "*the* LogOp" case should be rewritten.

W3 Other claims on the transformers are much less convincing. For instance, 
-(partially fixed) evidence 2 is a very weak evidence. This test can only tell whether the information you are looking for is present or not in the layer. So yes, the information is present in the third layer, but this is hardly surprising: it is obviously present in the input, and probably in every layer. And also probably in layers even for the linear case.
We would need to see such data (% of accuracy for classification) on other layers/cases, and also on other variables. (Relative) Comparison of the % of accuracy could give some indication on what is encoded in the last layer, absolute value (97%) is not conclusive.

-evidence 1c is not compatible with h_route being >0 or <0 depending on the case. Overall, the very precise protocol from the transformer seems a big stretch from the evidence.

W4 The case of Mistral 7B does not really confirm the findings on the trained transformers (which is not surprising, because the training process for the trained transformer cannot generalize, or only to choose variable names to output, not to solve the logical problem).
Question Q3: The logical formula checked for Mistal 7B is actually even restricted to shorter chains (lenght 2) than for the transformer (size 3). Why?

To sum up, it is an interesting problem, but the realisation is pretty weak and cannot be used to conclude much about how LLMs solve a logical problem. Hence, I recommend to reject the paper.

### Questions
Q1- Is there exactly one LogOp and exactly one Linear Chain. (It is what I guess after reading 6 pages, but this is not precisely explicitated, whereas this is a crucial information to understand the transformer being trained).
=> answer is yes.

Q2 - Can some symbol be common between the LogOp and the Linear chain, in particular the final (query) symbol? If yes, then the 10+ sentences with "*the* linear case" and "*the* LogOp" case should be rewritten.
=> answer is no.

Q3 - Why is Mistral 7B only queried with length 2 queries?

### Soundness
4

### Presentation
2

### Contribution
2
