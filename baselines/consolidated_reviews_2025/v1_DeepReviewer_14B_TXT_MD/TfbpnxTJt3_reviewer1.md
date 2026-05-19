### Summary

The paper proposes to address the challenge of federated learning in the presence of noisy labels. The paper also assumes that the dataset is open-set, i.e., the datasets across clients have non-overlapping label space. The proposed method is based on loss correction using "contrastive labels". The paper provides theoretical results on the privacy guarantee of the algorithm and the effectiveness. The paper also provides experimental results to support the method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper provides theoretical results on the privacy guarantee and effectiveness.
2. The paper provides experimental results to support the method.

### Weaknesses

#### Some Related Works


#### comment

1. The problem setting of the paper is not convincing enough. Although it provides one example of virus variants, it is hard to imagine a realistic scenario where the datasets are open-set and have label noise at the same time. The assumption of non-overlapping label spaces across clients seems overly restrictive and not representative of typical federated learning scenarios. It's unclear how this setting would arise in practice, especially when combined with label noise. The virus example is also not very compelling, as one would expect some overlap in the variants across different regions.
2. The novelty of the method is limited. The main idea is to use loss correction with "contrastive labels". The use of negative labels to counteract noisy labels is not new, and the paper does not adequately demonstrate a significant advancement over existing methods. The core mechanism of using a second, "contrastive" label to adjust the loss function appears to be a straightforward application of existing contrastive learning techniques, rather than a novel contribution.
3. The writing of the paper can be improved. For example, the introduction is not well written. It is hard to follow the motivation of the problem setting.

### Suggestions

The paper needs to provide a more compelling justification for its problem setting. The current open-set, non-overlapping label space assumption is not well-motivated and seems unrealistic in most practical federated learning scenarios. The authors should either provide more realistic examples or consider a more general setting where label spaces have some overlap. For instance, instead of assuming completely disjoint label spaces, the authors could explore a scenario where clients have different distributions over a shared set of labels, which would be more representative of real-world data heterogeneity. Furthermore, the paper should clearly articulate why the combination of open-set data and noisy labels is a unique challenge that requires a specific approach, rather than being addressable by existing methods for either open-set learning or noisy label learning independently. The authors should also consider the impact of the non-overlapping assumption on the applicability of their method in real-world scenarios.

The paper should also clarify the novelty of the proposed method. The use of contrastive labels for loss correction is not a novel idea, and the paper needs to clearly articulate how its approach differs from existing methods. The authors should provide a more detailed comparison with existing contrastive learning techniques and explain how their method is specifically tailored to the federated learning setting with noisy labels. The theoretical analysis should also be more detailed, explaining how the specific choice of contrastive labels leads to improved performance compared to other possible choices. The paper should also provide a more thorough discussion of the limitations of the proposed method and the scenarios where it might not be effective. For example, how does the method perform when the noise is not random but rather systematic or adversarial?

Finally, the paper needs to improve its writing, particularly the introduction. The motivation for the problem setting should be clearly stated, and the paper should be more accessible to a broader audience. The introduction should clearly explain the challenges of federated learning with noisy labels and open-set data, and why the proposed method is needed. The authors should also consider reorganizing the paper to improve the flow of ideas and make it easier to follow. For example, the theoretical results should be presented in a more intuitive way, with clear explanations of the key assumptions and implications. The experimental section should also be expanded to include more diverse datasets and comparisons with more baseline methods.

### Questions

What is the main challenge of the problem setting of the paper? Is it just for theoretical completion of the idea that the algorithm can work with certain guarantee?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
