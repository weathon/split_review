## Human Reviewer 1

### Questions
1. Line 378: Why Meta prompts serve as task-specific templates and are customized for individual samples? This seems to contradict with section 4.1.1.
2. Line 436: What do external resources, meta-knowledge-based assessments, and flexible sampling mechanisms mean? Please explain these methods in details. 
3. Typo: "flexiable" in line 436.

### Rating
3

### Confidence
4

---

## Human Reviewer 2

### Questions
See Strengths And Weaknesses

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Questions
1. Metareasoning has been a part of computer science/artificial intelligence research for the last several decades. Let me provide just one, probably biased, citation: https://dl.acm.org/doi/10.5555/3020652.3020691, which however cites many relevant works and is cited by followups. Does the framework of rational metareasoning suit the needs of your proposed approach? 

2. In connection with the above, here is a work https://arxiv.org/abs/2410.05563 (the same as in the strengths/weaknesses, the link is to the paper) that seemingly develops rational metareasoning framework for LLMs. What is missing in this work? How is this work related to your position?

3. You propose a Bayesian framework in terms of straightforward Bayesian modeling, and connect it with reinforcement learning. A modern tool for tackling similar problems is causal reasoning, which you do not seem to mention. What makes you think that pure Bayesian inference rather than causality calculus, is the right choice?

4. You argue in favor of rewards-based reinforcement learning, technically, even if these are metarewards reflecting the quality of reasoning as a whole. It appears from the current literature that rewards-based reasoning is not flexible/powerful enough for tasks you are discussing, and emergent concepts such as CURL (concave utility reinforcement learning) find their applications in the context of LMM. Are rewards crucial for your proposed framework? How CURL, for example, would fit instead of rewards?

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Questions
- What are the benefits of the advocated framework over current reasoning models trained via RL such as DeepSeek R1?
- Could you produce a concrete example for the Meta-Reasoning framework, implementing both the inference and learning process?

### Rating
2

### Confidence
3