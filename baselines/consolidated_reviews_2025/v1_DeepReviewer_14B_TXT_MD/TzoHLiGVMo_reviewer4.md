### Summary

This paper proposes a Transformer-based model to perform symbolic regression on dynamical systems. The authors propose a novel data generation pipeline to create a large training dataset. The authors also propose a novel benchmark dataset to evaluate the proposed method. The experimental results show that the proposed method outperforms the existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The experimental results show that the proposed method outperforms the existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only evaluated on two benchmark datasets. It is unclear how it would perform on other datasets or in real-world applications.
- The authors do not provide a detailed analysis of the limitations of the proposed method. It is important to understand the limitations of a method in order to determine its applicability to different problems.

### Suggestions

The paper would benefit from a more thorough investigation into the generalizability of the proposed method. While the authors have demonstrated strong performance on the two benchmark datasets, it is crucial to assess its robustness across a wider range of dynamical systems. Specifically, the authors should consider evaluating the method on datasets with varying degrees of complexity, noise levels, and system parameters. This could involve incorporating datasets from different scientific domains or generating synthetic datasets with controlled variations. Furthermore, it would be valuable to explore the method's performance when applied to systems with higher dimensionality or more complex interactions between variables. Such an analysis would provide a more comprehensive understanding of the method's strengths and weaknesses and its potential for real-world applications.

In addition to evaluating the method on more diverse datasets, the authors should also provide a more detailed analysis of its limitations. This should include a discussion of the types of dynamical systems for which the method is likely to perform well and those for which it may struggle. For example, it would be useful to investigate the method's sensitivity to the choice of hyperparameters, the length of the input trajectory, and the presence of noise or outliers in the data. The authors should also consider exploring the method's ability to handle systems with non-smooth or discontinuous dynamics. A thorough analysis of these limitations would help to establish the boundaries of the method's applicability and provide valuable guidance for future research.

Finally, the authors should consider comparing their method to other state-of-the-art approaches for symbolic regression of dynamical systems. While the authors have shown that their method outperforms existing methods on the two benchmark datasets, it is important to provide a more comprehensive comparison to other techniques. This could involve comparing the method to other machine learning-based approaches, as well as traditional methods for system identification. Such a comparison would help to contextualize the performance of the proposed method and highlight its unique advantages and disadvantages. Furthermore, it would be beneficial to explore the computational cost of the proposed method compared to other approaches, as this is an important factor to consider when applying the method to real-world problems.

### Questions

- How does the proposed method compare to other state-of-the-art methods for symbolic regression of dynamical systems?
- What are the limitations of the proposed method in terms of the types of dynamical systems that it can handle effectively?
- How does the performance of the proposed method vary with the length of the solution trajectory?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
