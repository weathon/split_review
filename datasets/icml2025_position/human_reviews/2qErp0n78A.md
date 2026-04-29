## Human Reviewer 1

### Questions
1. How can the Common Abstract Topologies be used to solve the problem you discussed in Example 1?
2. As the terminology of "causal" in NLP is fundamentally different from the concept of causal in causality, e.g., "causal attention" in NLP does not refer to anything related to intervention/counterfactual, it would be beneficial to clarify this early in the paper.
3. In Claim 3 "Instrumentalism is all you need", how does it relate to instrumental variable in the context of causal inference? This claim of "x is all you need" also contradicts with the author's own statement in earlier sections that they are not claiming "causality is all you need".

### Rating
1

### Confidence
3

---

## Human Reviewer 2

### Questions
- What do you mean by spurious correlation?

### Rating
3

### Confidence
4

---

## Human Reviewer 3

### Questions
(1)- The authors describe how causality could be used to systematically address many flaws found across LLM benchmarks and understand the reasoning abilities of the models. We consider these ideas could be generalized to address similar flaws across machine learning benchmarks. What modifications/adaptations would be required to address machine learning benchmarks in general?

(2)- The authors describe different Common Abstract Topologies and list examples that could be modeled with them. We suggest the authors provide a complete example at the Appendix to illustrate how such phenomena could be implemented in CATs and used as a template for future benchmarks. 

(3)- Did the authors consider what a potential implementation of the CATs and benchmarks would look like? Would such an implementation allow for some automatic validations regarding the causal relationships expressed in the CATs and the actual benchmark implementation? To what extent would the CATs define or validate the benchmark? What would be the specific building blocks for a benchmark specification based on the proposed idea and examples?

(4)- The authors may be interested in the following: CATs for data generative processes could be used in domains where privacy or sensitive data are a concern and data cannot be shared. By creating a generative process grounded in causal relations, data that complies with the causal relationships could be created, and data sharing (other than the synthetically created) could be prevented. This would also make such benchmarks be a step closer to the vision outlined by Jensen Huang at the SIEPR Economic Summit in 2024 (https://www.youtube.com/watch?v=cEg8cOx7UZk)

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Questions
Questions:
- One counterpoint to the proposed position is that the added complexity and flexibility in framing the problem will result in more cherry picking and ‘conclusion-first’ analysis, as has often plagued causality research where there are often few common benchmarks/reference points and researchers construct their own experiments to suit their method. How do the the authors propose to mitigate against this?
- Please could you address the points and questions raised above in 'Weaknesses'?

Minor points:
- Figure 2: causal may not necessarily used in the authors’ context (e.g. 'causal autoregressive models')

### Rating
3

### Confidence
3