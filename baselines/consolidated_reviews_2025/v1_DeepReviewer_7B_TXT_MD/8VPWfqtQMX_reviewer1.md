### Summary

This paper proposes a new domain generalization method based on in-context learning. The proposed method, ICRM, uses a transformer to predict the label of the next input based on the previous inputs. The authors claim that this approach allows the model to learn from the context of previous inputs, enabling it to adapt to new environments more effectively. The authors provide theoretical analysis and empirical results to support their claims.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed ICRM method is novel and interesting. It provides a new perspective on domain generalization by using in-context learning.
2. The authors provide a theoretical analysis to support the effectiveness of ICRM.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Domain adaptation under target shift
[2] A survey on domain generalization

#### comment

1. The paper lacks a detailed discussion of the relationship between ICRM and existing domain generalization methods, particularly those that address target shift. The authors should clarify how ICRM differs from methods like DANN, CDAN, and MCD, which also aim to learn domain-invariant representations. A more thorough comparison, both conceptually and empirically, is needed to establish the novelty and advantages of ICRM.
2. The theoretical analysis relies on strong assumptions, such as the existence of an amortization function and the validity of the Bayes optimal risk minimizer. These assumptions may not hold in real-world scenarios, and the authors should discuss the limitations of these assumptions and their potential impact on the practical applicability of ICRM.
3. The empirical evaluation is limited to a few datasets and does not include a comprehensive comparison with state-of-the-art domain generalization methods. The authors should evaluate ICRM on a wider range of datasets and compare it with more recent and competitive methods to demonstrate its effectiveness.

### Suggestions

The paper would benefit significantly from a more detailed discussion of how ICRM relates to existing domain generalization techniques, especially those addressing target shift. The current discussion is too brief and does not adequately address the nuances of methods like DANN, CDAN, and MCD. A deeper analysis should explore the specific mechanisms by which ICRM learns domain-invariant representations, and how these mechanisms compare to those of existing methods. For instance, the authors could discuss whether ICRM learns similar feature representations or if it relies on different inductive biases. Furthermore, a more thorough empirical comparison is needed, including a wider range of datasets and a more detailed analysis of the performance of ICRM under different levels of domain shift. This would help to better understand the strengths and weaknesses of ICRM compared to existing methods.

The theoretical analysis, while providing some insights, relies on strong assumptions that need further justification. The authors should discuss the implications of these assumptions and their potential impact on the practical applicability of ICRM. For example, the assumption of an amortization function may not hold in many real-world scenarios, and the authors should discuss how this might affect the performance of ICRM. Similarly, the validity of the Bayes optimal risk minimizer is a strong assumption that may not be achievable in practice. The authors should discuss the limitations of these assumptions and their potential impact on the practical applicability of ICRM. It would be beneficial to explore the sensitivity of ICRM to violations of these assumptions, perhaps through additional experiments or theoretical analysis.

Finally, the empirical evaluation needs to be significantly expanded to include a wider range of datasets and a more comprehensive comparison with state-of-the-art domain generalization methods. The current evaluation is limited to a few datasets and does not provide a clear picture of the effectiveness of ICRM compared to other recent methods. The authors should consider including more challenging datasets and comparing ICRM with more competitive baselines. This would help to better understand the strengths and weaknesses of ICRM and its potential for practical applications. Furthermore, the authors should provide a more detailed analysis of the performance of ICRM under different experimental settings, such as varying the number of context samples or the degree of domain shift.

### Questions

See weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
