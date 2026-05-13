# Truth-value judgment in language models: belief directions are context sensitive

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Recent work has demonstrated that the latent spaces of large language models (LLMs) contain directions predictive of the truth of sentences.
Multiple methods recover such directions and build probes that are described as getting at a model's ``knowledge'' or ``beliefs''.
We investigate this phenomenon, looking closely at the impact of \textit{context} on the probes.
Our experiments establish where in the LLM the probe's predictions can be described as being \textit{conditional} on the preceding (related) sentences.
Specifically, we quantify the responsiveness of the probes to the presence of (negated) supporting and contradicting sentences, and score the probes on their consistency.
We also perform a causal intervention experiment, investigating whether moving the representation of a premise along these \textit{belief directions} influences the position of the hypothesis along that same direction.
We find that the probes we test are generally context sensitive, but that contexts which should not affect the truth often still impact the probe outputs.
Our experiments show that the type of errors depend on the layer, the (type of) model, and the kind of data.
Finally, our results suggest that belief directions are (one of the) causal mediators in the inference process that incorporates in-context information.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Previous work has shown that LLMs contain representations of "truth" or "belief" in their residual stream that can predict whether the model considers standalone statements true or false. This paper extends this line of research by investigating how these belief directions behave when statements appear with preceding context ("premises"). The authors propose and evaluate four "consistency error" metrics to characterize how truth/belief representations respond to context. They also conduct causal experiments, modulating the "truth" representation of the contextual premises, and showing that this has a causal influence on the resulting "truth" representation of the later statement.

### Strengths
- Strong causal intervention results
  - Section 4.2 displays an interesting experiment, where modulating the truth representation on the early premise can influence the truth representation on the later hypothesis. This is a creative experiment, and makes for an interesting result.

- Thorough experimental analysis
  - The authors break down the data by training dataset (no-prem vs pos-prem), evaluation dataset, and many other dimensions, while also displaying the data in a coherent manner.
  - The authors also conduct experiments to investigate base models vs instruction-tuned models.

### Weaknesses
 - Unclear motivation
  - I felt that the problem of studying the effect of context on representations of belief was not sufficiently motivated. The introduction briefly discusses hallucinations, but the connection was not made clear.
  - I think the paper could be improved by strengthening its discussion of motivation, and articulating why the problem is important to study.

- Technical presentation could be improved
  - In particular, I found error metrics E3 and E4 difficult to understand and interpret. I think the paper would benefit from a clearer and simpler explanation of these metrics.
  - I found it unclear why the "premise effect" is using affirmative premises, rather than, say true premises, or entailing premises, etc.

### Questions
1. The introduction states that "Working towards the mitigation of this type of hallucination requires understanding the impact of context on belief probes.", where "this type" refers to hallucination "characterized by inconsistency". What is hallucination characterized by inconsistency, and how is it related to studying the context-dependence of belief probes?
    - Overall, I had trouble understanding the larger motivation behind this work, and elaborating on this sentence could clarify why the subject is impactful.

2. In section 3.1, the authors claim that CCR outperforms CCS ("similar performance with more stable convergence, without the need to train multiple probes"). Can data / experiments be provided (perhaps in an appendix, if not critical to the understanding of the paper) to support this claim?

3. In section 3.3, why is the "premise effect" computed using the affirmative premise $q^+$? Why not the negative premise $q^-$, or a mix of both? Or why not use true premises vs false premises, or entailing vs contradictory premises?

4. Is it possible that there is a distinction between the true label (whether a statement is true or false in actuality) vs the model's believed label (whether the model thinks/believes a statement is true or false)? If this is possible, is it a concern for the supervised probe training techniques?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors argue that belief directions in large language models are sensitive to context. They provide empirical evidence for this with data consisting of premises and hypotheses.

### Strengths
They address an important question: whether belief directions depend on context. They conduct extensive experiments to support their argument.

### Weaknesses
The authors compute all probabilities $p$ and error scores using learned linear probes. However, this approach is questionable without validating two key assumptions: (1) there exists a global probability distribution $P_\lambda(X)$ for belief, and (2) the learned linear probes correctly capture this probability distribution. Before conducting experiments, the authors should validate these assumptions by thoroughly checking how the linear probes perform on both context and labels, as well as verifying probe accuracy. It's even possible that the linear probes might capture concepts other than belief, such as sentiment. Given multiple candidates for linear probes, validation is necessary. 

Moreover, the superior performance of pos-prem probes might simply result from training data containing premises, making it an out-of-distribution issue for no-prem probes. It's possible that none of the linear probes they identified truly represent belief linearly, or that no global linear probe for belief exists. They need to provide a clear definition of "belief".

### Questions
1. This paper should give a clear explanation of the notation. For example:
 - What is the definition of $\lambda$ and $X$ in $P_\lambda(X)$ in line 143?
 - What is $\sigma$ in line 146?
 - Is $\theta$ a unit vector in line 162?
 - What are $Q^+$ and $Q^-$ in line 202?
2. Why is there no bias term in the belief probes?
3. Why do you propose Contrast Consistent Reflection (CCR)? What is the advantage of this method in this paper?
4. If you want to deal with conditional beliefs $P_\lambda(H|q)$, why don't you learn the probe for $p(h|q)$ directly by using several hypotheses for a given premise? It is unclear whether the error score computed by the global probability $P_\lambda(h)$ directly corresponds to the conditional distribution.
5. What does "mean-normalized" mean in line 288? Also, how did you calibrate the probes? Please provide mathematical details for them.
6. In Table 2, why is $p(h)$ around 0.5? Is this because you use both $h^+$ and $h^-$ and $p(h) = \frac{1}{2}(1-p(h^-) + p(h^+))$? Then, why are they sometimes not exactly 0.5?
7. Table 2 shows the mean probabilities. What are the variance probabilities for each cell?
8. How did you compute premise sensitivity in Figure 2?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the extent to which LLMs display the right sort of context sensitivity when they come to represent their own belief in the content of statements they are prompted with. A family of belief probing methods are used, including a novel variant of an existing method that seems to be more stable. In experiments with Llama2-7b and Llama2-13b, the authors find that models are sensitive to context, though they are also sensitive to irrelevant context in ways that might be concerning.

### Strengths
1. The core question of context/premise sensitivity is important and should play a role in future discussions of models making truth value judgments. This paper provides a very useful framework for thinking about this, with associated metrics.

2. The new method, Contrast Consistent Reflection, seems like a genuine improvement over its predecessor Contrast Consistent Search.

3. The experimental results are rich and reported in detail.

### Weaknesses
1. The space of methods explored seems very narrow. All of them just seek a single direction that correlates with the model distinguishing sentences from their negations. In turn, the results don't really clearly distinguish among these methods (except perhaps for section 4.2). It's unclear to me whether this is representative of the space of possible models for this problem, or whether we might get much clearer results with different methods. Specifically, the methods all rely on linear probes, which may be insufficient to capture the nuances of how the model represents belief. It's possible that non-linear methods, or methods that consider the geometry of the representation space, might reveal more about the underlying mechanisms.

2. One of the core results is that there is no evidence that scaling is a factor here. True enough, but only two model sizes were tested, and they are not very different in size (7B and 13B). Thus, this has to be a very weak conclusion indeed, for many reasons. The difference between 7B and 13B parameters is not substantial enough to draw strong conclusions about scaling trends. It would be important to test models that span a wider range of sizes, including much larger models, to make any claims about the effect of scaling on context sensitivity.

### Questions
1. Paragraph 1 of the paper does something that is already common in the papers in this area: it blurs together (1) belief in statement from (2) the truth of the statements themselves. I do not see how it could be appropriate in these context to act as if models could latently represent (2), except insofar as their beliefs happen to align with reality. Am I missing something? I ask because I think this does shape the broader significance the work can have.

2. In the Marks and Tegmark paper, it seems like there is much more structure in the layers than we see in any of the results in this paper. Am I misinterpreting the results from either or both papers?

3. The experiment in section 4.2 is in many ways the most interesting, and it suggests that the logistic regression method is less good than the others at identifying causal efficacious features for truth. Is there a way to characterize the strength of the overall effects in Figure 4 and in turn to quantify the extent to which LR is worse?

### Soundness
4

### Presentation
3

### Contribution
3
