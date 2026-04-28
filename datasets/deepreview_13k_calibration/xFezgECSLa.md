# On the Design and Analysis of LLM-Based Algorithms

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
We initiate a formal investigation into the design and analysis of LLM-based algorithms,
i.e.~algorithms that contain one or multiple calls of large language models (LLMs) as sub-routines and critically rely on the capabilities of LLMs.
While LLM-based algorithms, ranging from basic LLM calls with prompt engineering to complicated LLM-powered agent systems and compound AI systems, have achieved remarkable empirical success,
the design and optimization of them have mostly relied on heuristics and trial-and-errors,
which is largely due to a lack of formal and analytical study for these algorithms.
To fill this gap, we start by identifying the computational-graph representation of LLM-based algorithms, the design principle of task decomposition, and some key abstractions,
which then facilitate our formal analysis for the accuracy and efficiency of LLM-based algorithms, 
despite the black-box nature of LLMs.
Through extensive analytical and empirical investigation in a series of case studies,
we demonstrate that the proposed framework is broadly applicable to a wide range of scenarios
and diverse patterns of LLM-based algorithms,
such as parallel, hierarchical and recursive task decomposition.
Our proposed framework holds promise for advancing LLM-based algorithms, 
by revealing the reasons behind curious empirical phenomena, 
guiding the choices of hyperparameters,
predicting the empirical performance of algorithms,
and inspiring new algorithm design.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper is about a formal investigation into the design and analysis of LLM-based algorithms, i.e. algorithms that contain one or multiple calls of large language models (LLMs) as sub-routines and critically rely on the capabilities of LLMs

### Strengths
The stated objectives of the paper are excellent if they can be achieved.

### Weaknesses
The paper does not seem to deliver very much of the stated contributions. Proposition 1 is the key result, and it is quite weak.

The real issue is that a computation graph is a precise mathematical object that uniquely defines a computation, whereas this LLM-based computation graph is neither precise nor does it uniquely define a computation. The lack of uniqueness stems from the non-determinism of any LLM-based call.
As a consequence, how can one compare a "normal" computation graph with this LLM-based computation graph?
Further, the analysis should be stochastic (with expected complexity), rather than the proposed deterministic complexity. An LLM is inherently stochastic, so one cannot specify the outcome of an LLM call as a deterministic object.

The paper states: use “accuracy” to refer to the broader concept of “quality”, and an “error metric” can be any metric that measures how much the output of an algorithm deviates from certain criteria."

Where do the costs come from in  C(prefilling), C(decoding)?

It seems like all of these costs are just qualitative.

hypothetically categorize LLMs into two types: Type-1 LLMs are only prone to the first failure mode, while Type-2 LLMs are prone to both

Too much speculation in this article

It seems like the article builds up to Proposition 1,and then we ask "so what!". This is a pretty weak conclusion, and it does not even look like to has much strength as a formal mathematical expression.

### Questions
Please clarify if  all of the defined costs are just qualitative. 

If they are not, how does one define a metric to assign values and to update the values?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper attempts to formalize cost and accuracy analysis of LLM-based algorithms .

### Strengths
The paper advocated analysis of LLM-based algorithms.

### Weaknesses
The theoretical part proposes a framework for analysis which looks like a simplistic variant of analysis of parallel algorithms, something one learns during undergrad CS studies. The 'empirical' evaluation in the body of the paper is just a qualitative description of application of the proposed (rather standard) methodology to a few problems. There is 'numerical evaluation' in the appendix, which is not convincing and lacks detail.

While I welcome the idea of systematic analysis of algorithms, including LLM-based ones, the paper lacks both theoretical novelty and empirical justification. Significant effort has to be spent to bring this paper to the level of a publication at a major conference such as ICLR.

### Questions
What part of your analysis is applicable exclusively to LLMs rather than to any parallel algorithm using external resource?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a framework to formally investigate LLM-based algorithms,
allowing to assess accuracy and efficiency. The authors describe their
framework and instantiate a few different LLM-based algorithms, which they then
analyze.

### Strengths
The paper tackles an interesting and important problem.

### Weaknesses
First, the paper is far too long for a conference format (the appendix is twice
as long as the main paper and includes sections that should be part of the main
paper, like related work). This paper would be more suitable as a journal paper.

With regards to the proposed evaluation framework, very little of it seems to be
specific to LLMs, or rather the LLM-specific parts are provided by the
investigator. It seems that this would be difficult in practice -- how would I
characterize the capabilities of any given LLM in a way that allows to determine
what the output would be for a given prompt?

The insights the analyses in the paper provide are very generic: "the optimal
value of m that minimizes costs might depend on the choices of cost metrics and
assumptions of LLM inference service, among other factors", "the minimum error
of the overall algorithm might be obtained by some intermediate value of m that
achieves a balance between these two failure modes", "each option of retrieval
has its own pros and cons". None of these are actionable, and it is unclear that
the proposed framework is necessary to obtain them. It is unclear whether other
insights are generally true, in particular "since a smaller value of m makes
each sub-task easier, it is reasonable to expect that the overall error E(y)
with this metric will also become smaller as m decreases" -- while the
individual errors might decrease, combining multiple steps potentially compounds
individual errors, resulting in an overall increase in error.

Other parts of the proposed framework are unclear. Section 3.3 describes the
answer being generated by majority voting, but the correct answer appears only
once. Dividing the input text into chunks, it seems that there would be a lot of
incorrect and "don't know" answers and, hopefully, a single correct one (for the
chunk that did contain the answer). How can majority voting possibly return the
correct result in this case?

### Questions
See weaknesses.

Update after responses: Thank you for your responses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The aim of the paper is to analyze the behavior of LLM-based algorithms, specifically their theoretical "accuracy" and cost. The authors present LLM-based algorithms as computational graphs consisting of LLM queries and non-LLM computations that capture the data flow and allow for analysis via dynamic aggregation. The proposed framework is described in Section 2. Then, Sections 3.0-3.1 provide an abstract analysis of a map-reduce pattern, which is followed by special examples of counting and retrieval. In Section 4, a hierarchical decomposition pattern is analyzed on an example of determining a value of a variable. Finally, Section 5 analyses an example composed of recursive queries.

### Strengths
I like the proposed idea of analyzing the LLM-based algorithms as computational graphs. It's definitely the most natural way, similarly to analyzing standard algorithms and data flow.

### Weaknesses
The main problem of that paper is that, in my opinion, there is no takeaway from it. The proposed analysis mostly ends on framing the selected patterns as computational graphs, showing a basic bound, sometimes followed by a very generic statements like "so there is a tradeoff, period". I do think that we should have a principled way of analyzing LLM-based algorithms and the proposed framework looks promising, but little was done to use it. To be more precise:

- In Section 3 you analyze the map-reduce pattern, and in my opinion the most interesting things happen here.
    - You derive (or rather state since it is straightforward) the bound on the cost (Equation 4). Then, you use it to show (actually state) that it is minimized at $m=min(n, \bar m)$. Yes, I agree that if the cost is linear or sub-linear with respect to the input, the best idea is to use as large chunks as possible (again, rather a straightforward statement).
    - Then, you derive a bound on the cost with quadratic complexity and find a minimizer for that, which is approximately $L_{sys}$. This is actually interesting and surely non-trivial, but sadly no further discussion is provided. The lack of discussion makes it unclear how this result should be interpreted or used in practice. For example, what are the practical implications of this result for choosing chunk sizes in real-world LLM applications?
    - Then, you analyze the parallel setting. Although the analysis is sound, I was a bit disappointed when I understood the key takeaway: "when m is very big, the cost increases if we make it even bigger; when m is very small, the costs increases if make it even smaller". Unfortunately, I find it straightforward -- there is always a tradeoff in the size of distributed computation parts and using too small or too big is never a good idea. The analysis does not provide any specific guidance on how to determine the optimal chunk size in a given scenario, which is a crucial practical concern.
    - Then, you state that the cost is minimized by $m\asymp n/p$. That would be interesting, but I cannot find any justification for that statement. The derivation of this result is not clearly explained, and it is not obvious how this result is derived from the previous analysis.
    - Also, the asymptotic notation you use is a bit hard to parse. The only variable that has unbounded support is n, which should make other variables either constants or implicit functions of n, which is not specified directly. It looks like you take asymptotic of m, although it's bounded by n. The lack of clarity in the asymptotic notation makes it difficult to understand the precise meaning of the results.
    - The "implication" in line 323 literally states that "The optimal value of m might depend on various factors, period". This statement is too vague and does not provide any actionable insights.
    - Section 3.2 applies the derived formulas to a counting example. However, (1) the cost analysis is little beyond simply rewriting the formulas, (2) the takeaway is again straightforward (overall counting error is smaller if chunks are smaller). The analysis does not provide any new insights beyond what is already known about the relationship between chunk size and error in counting tasks.
    - Section 3.3 describes clearly the needle-in-a-haystack example. But then, equally clearly states the conclusion "the optimal value of m is a tradeoff, it can't be too big or too small period". Please, explain me why any kind of analysis is needed to make such a claim?

- In Section 4 you decribe the hierarchical decomposition pattern. Now, there are two listed conclusions: (1) reasoning has much lower cost than retrieval, (2) making the algorithm sequential or parallel has pros and cons. Although I agree with both, at the same time I don't see how did your framework help you derive those. They were not conclusions, you stated both during analysis and that's fine, since both need no explanation. But then, again, you haven't shown benefits of using your framework.

- In Section 5 you analyze recursive decomposition and state a bound on the error (and that's literally all). The question is: why do we need that bound? Is it helpful in any way? Why there is no discussion?

- As detailed, although I like the high-level idea of the framework, the paper shows no significant usage of it. Having said that, I'd be happy to be proven wrong, so I'm open to the discussion.

Other comments:

- I suggest adding a brief example of any LLM-based algorithm in the beginning. Initially I thought more about algorithms like Dijkstra, so specifying that with a simple one-sentence example would be helpful.
- It takes 4 pages until you start any analysis. I suggest making the initial descriptions (in fact, everything) much more concise, since the framework you propose is rather simple (which is a benefit), but then reading 4 pages of "how to decompose an algorithm into a computation graph" sounds much too lengthy.
- It's a bit confusing that you name the paragraphs the same way in sections 2.3 and 3.1. If you repeat the same names in Section 2 (which is introducing the framework), then in 3.1 it sounds like an unintended repetition at first glance.
- Figure 13 is actually very helpful in understanding the description. Please move it to the main text, even one of them, even smaller.
- The paper is missing a discussion of limitations and related works.

### Questions
Please list the non-trivial takeaways stemming from your analysis. How does it influence the design of LLM-guided algorithms? What does it explain in those we already have? How does it contribute to the field? Please be precise.

### Soundness
3

### Presentation
2

### Contribution
1
