## Human Reviewer 1

### Questions
Questions:
- In Section 5.2, the authors suggest that System-2 requires new supervised paradigms (e.g., supervision of programs or unsupervised learning), but in reality, obtaining program-level supervised data can be very difficult. How does the paper address this challenge? What are the specific strategies for unsupervised program learning?
- Is there a clear boundary between what tasks are suitable for System-1 and System-2, and if not, does this blur the applicability of the framework?
- Distilling System 2 into System 1 is another approach that bridges System 1 and System 2. Is it possible to analyze whether an approach like this could bring additions to the framework proposed in the paper?

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Questions
None

### Rating
1

### Confidence
4

---

## Human Reviewer 3

### Questions
1) In the beginning of the paper, the authors argue that 'scaling data size would not ensure the ability to handle increased complexity'. But while this is tangentially touched upon in the rest of the paper, only in the conclusion is scaling again mentioned, saying "We argue that scaling current deep learning approaches is insufficient". Is there a part of the paper I am overlooking, or is there a place where a concrete argument is made that scaling data size woud not ensure the ability to handle increased complexity? If so, it would be good to emphasise, and elaborate on this claim, as this seems central to the paper's position.

2) It would be useful to clarify the necessity of System2 with regards to the 'Aha' moment present in DeepSeek's architecture, showing the emergence of System2 reasoning by pure RL training on a large enough model, without any need for program synthesis approaches that the authors argue for.

3) Isn't the example of multiplication (in section 2.) contrived, in the sense that existing LLMs *do* learn full algorithms for multiplying multi-digit numbers? That is, they do learn how to phrase the problem as Python code, which can then be called and executed externally. This mirrors what humans do: we can learn the algorithm, and execute it on an external system, such as a calculator, but neither humans nor LLMs can multiply multi-digit numbers with ease, suggesting a discrepancy between the asserted difference of System2 reasoning in humans, and LLMs.

Smaller questions:

3) The position stated in the first line of abstract is different than the one in the title. Do you wish to emphasise/argue a property of System2 reasoning, or emphasise/argue that System2 needs to be be introdued as a paradigm?

4) Sec 5.4 "When we built System-2...". It sounds like the authors are referring to the community building system2 approaches, and not themselves? It might be worth clarifying the intent there

### Rating
3

### Confidence
4

---

## Human Reviewer 4

### Questions
What is the normative consequence of researchers using kolmogorov complexity rather than concepts from compositionality literature?

### Rating
2

### Confidence
3