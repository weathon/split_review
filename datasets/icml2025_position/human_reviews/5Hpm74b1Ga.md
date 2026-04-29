## Human Reviewer 1

### Questions
See Strengths And Weaknesses.

### Rating
3

### Confidence
4

---

## Human Reviewer 2

### Questions
Can you clarify what the potentially fundamental limitations in learning from large-scale data in context are (page 4)?

The preliminary evaluationt that PFNs fail to satisfy the Marginale property is interesting. It would be interesting what this implies for the stated positions that PFNs are the future for Bayesian inference. In particular, while traditional Bayesian inference methods (assuming a good variational approximation, long enough MCMC chains) should satisfy the marginale property, do you have a suggestion why PFNs do not satisfy it, such as due to the pre-training nature, or more because of the model architecture limitation.

The authors argue that PFNs struggle with heterogeneous data. Can this be accounted for by including synthetic data with such distributional features into the pre-training dataset? As written, it sounds like this is more due to the encoder not able to adapt to the varying feature distribubutions due to architectural limits.

### Rating
3

### Confidence
3

---

## Human Reviewer 3

### Questions
In equation 1, what is $\phi$? Is it a typo?

### Rating
4

### Confidence
3