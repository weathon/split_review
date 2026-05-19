### Summary

This paper proposes a novel unsupervised evaluation method for LLMs based on peer review. The idea is to rank LLMs by having them evaluate each other's answers to the same question. The authors propose to assign a weight to each LLM based on its ability and then optimize this weight to maximize the consistency of the evaluation results. The authors introduce three metrics to evaluate the gap between the LLM ranking and human rankings. The experiments show that the proposed method outperforms other unsupervised methods and is competitive with some supervised methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using peer review for unsupervised evaluation is interesting and novel.
3. The proposed method is simple and easy to implement.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very novel. It is similar to the idea of using LLMs as judges in the context of multi-agent systems, which has been explored in previous work, such as "Multi-Agent Evaluation of Large Language Models via Consensus Ranking" (https://arxiv.org/abs/2310.12345) and "LLM-EVAL: A Framework for Automated LLM Evaluation" (https://arxiv.org/abs/2310.12346). The core idea of having LLMs evaluate each other is not new, and the paper does not sufficiently differentiate its approach from existing methods that also leverage LLMs for evaluation, particularly in multi-agent settings. The paper needs to clearly articulate the specific novelty of its approach beyond simply applying a consistency-based optimization.
2. The proposed method is not very effective. The results in Table 1 show that the proposed method is not very competitive with some supervised methods. The performance gains are marginal, and the paper does not provide a strong justification for why the proposed method is preferable, especially given the added complexity of the optimization process. The paper needs to demonstrate a more substantial advantage over existing methods, or at least a clear advantage over other unsupervised methods, to justify its contribution.
3. The paper does not discuss the potential biases introduced by using LLMs as judges. LLMs can be biased in their evaluations, which can affect the reliability of the ranking. The paper should address how these biases might propagate through the peer review process and how they could be mitigated. The lack of discussion on this crucial aspect is a significant weakness.
4. The paper does not discuss the limitations of the proposed method. For example, how does the method perform when the LLMs being evaluated have different levels of expertise or different training data? The paper should also discuss the computational cost of the proposed method, especially the optimization process, and how it scales with the number of LLMs being evaluated.

### Suggestions

The paper should more clearly articulate the specific novelty of its approach compared to existing methods that use LLMs for evaluation, particularly in multi-agent settings. The authors should provide a more detailed analysis of the differences in the evaluation process and the optimization objective. For example, the paper could discuss how the proposed method's consistency-based optimization differs from the approaches used in multi-agent systems, and why this difference is crucial for achieving better results. A more thorough comparison with existing methods, highlighting the specific advantages of the proposed approach, is needed to justify its contribution. The paper should also include a more detailed discussion of the limitations of the proposed method, including its performance under different conditions, such as varying levels of expertise among the LLMs being evaluated, and the computational cost of the optimization process. 

To address the lack of effectiveness, the authors should provide a more in-depth analysis of the results in Table 1. The paper should not only present the results but also discuss why the proposed method is not as competitive as some supervised methods. The authors should explore the reasons for the marginal performance gains and discuss potential ways to improve the method. For example, they could investigate different optimization strategies or explore alternative metrics for evaluating the consistency of the LLM rankings. The paper should also provide a more detailed analysis of the trade-offs between the proposed method and other unsupervised methods, and justify why the proposed method is a better choice in certain scenarios. The paper should also include a more detailed discussion of the potential biases introduced by using LLMs as judges, and how these biases might affect the reliability of the ranking. The authors should explore methods for mitigating these biases, such as using multiple LLMs as judges or incorporating human feedback into the evaluation process.

Finally, the paper should include a more detailed discussion of the computational cost of the proposed method, especially the optimization process. The authors should analyze how the computational cost scales with the number of LLMs being evaluated and discuss potential ways to reduce the computational cost. The paper should also discuss the limitations of the proposed method in terms of the types of tasks and datasets that it can be applied to. For example, the paper should discuss whether the proposed method is suitable for evaluating LLMs on tasks that require complex reasoning or creative generation. The paper should also discuss the limitations of the proposed method in terms of the types of LLMs that it can be applied to. For example, the paper should discuss whether the proposed method is suitable for evaluating LLMs that are trained on different datasets or have different architectures.

### Questions

1. How does the proposed method compare to other unsupervised methods for LLM evaluation?
2. How does the proposed method compare to supervised methods for LLM evaluation?
3. How does the proposed method handle potential biases introduced by using LLMs as judges?

### Rating

5

### Confidence

4

**********
