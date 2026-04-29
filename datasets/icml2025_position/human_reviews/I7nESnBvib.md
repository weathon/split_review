## Human Reviewer 1

### Questions
My questions are derived from the list of weaknesses above:

1. Can you clarify what your position is? Do you only focus on causal discovery (what the title suggests to me) or causality at large (what the content suggests to me)?
2. What is (a clear formulation/example of) the alternative view you are you are arguing against?
3. What would be a concrete recommendation you derive from your position? By concrete, I mean something that a researcher could start investigating (eg, a project idea or a research question).

### Rating
3

### Confidence
3

---

## Human Reviewer 2

### Questions
__Q1.__ Regarding weakness W1,  a relevant question is, how can practitioners deal with these intrinsic obstacles? Can we design more relaxed causal queries that might nevertheless be useful in practice? Consider, for instance, the requirement that the answers to the core XAI questions be accurate and complete. This requirement is quite stringent. It is possible that relaxing these requirements still produces answers that are practically useful even though they are not ideal.

__Q2.__  How does your classification scheme relate to terminology such as 'global' and 'local' queries? (e.g., Barcelo et al., 2020)
For instance, are global input queries "model based" or "data based"? It seems they could be categorized either way.

__Q3.__ Is the notation in Definition 3.1, bullet point 3 meant as follows? $\mathbf{F} = \\{ f_V : V \in \mathbf{V} \\}$.
If so, you might want to use this standard notation instead. If not, perhaps a clarification is needed.

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Questions
Minor question: how does the SCM structure handle exogenous but observed variables (e.g. for me, the time that the sun rises in the morning)?

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Questions
Can the authors provide a simple definition of causality up-front to help interpret all the claims that come later? It is not always clear to me what methods the authors consider to be causal or not. Dimensionality reduction is even described as 'aligning closely with the principles of causal discovery'. So what methods are *not* causal? If the claim of the paper is that taking a causal approach will help us, then causality has to have a definition that actually has teeth, and excludes certain lines of work. 

Relatedly, the authors seem to acknowledge that there are many cases where non-causal methods are appropriate for XAI problems. So in what way does this causal framework unify the whole field? (e.g. "In light of these challenges,correlation-based explanations (e.g., feature importances, saliency maps) may suffice when the goal is to detect patterns, biases, or anomalies rather than to enable interventions.")

I am confused by the 6 question framework. Q1 and Q2 claim to be about the data generating process and yet the methods discussed (attention and DR) are about internal model mechanisms and a way of *describing* data structure, but not explaining how it is generated. Furthermore, I don't think XAI is actually used to try to explain how data is *generated*. It wouldn't make sense to analyze models in isolation to try to understand the processes in the real world that created the data (and it is simply a different problem than what XAI focuses on).

Furthermore Q4 asks about the how the model's internal functions work yet the methods listed don't analyze the internal mechanisms of the models. The attention analysis listed under Qs 1&2 is actually more appropriate as a means of explain internal model mechanisms (as are many other methods from mechanistic interpretability). 

The authors talk about the difficulty of causal discovery. In the case of understanding a trained network, however, we have direct access to the causal model - it is the trained network itself. So it doesn't seem like causal discovery itself is the challenge (and in that way, XAI is not just causal discovery in disguise). Rather, the challenge of XAI is how to create the right abstractions and approximations that are useful for a person or use-case, but don't deviate too much so as not to provide accurate intuitions. The authors talk about this need to find the right concepts that 'align with human mental models', but it is not at clear how this would be evaluated within the causal framework. If our understanding of a model is defined in terms of abstract approximations to what the model is actually doing, how do we evaluate our understanding based on observational, interventional, and counterfactual data? Essentially, we will create a causal graph where the Fs have no real counterpart in the real model. 

In total, the paper acknowledges many of the challenges of XAI, but doesn't make clear how causality is uniquely well-suited to help us tackle them. In fact, I think there are many sentences in the paper where removing the word 'causal' would hardly change the meaning. I would like to have a clearer understanding of taking this framing helps, beyond just a label.

### Rating
3

### Confidence
4