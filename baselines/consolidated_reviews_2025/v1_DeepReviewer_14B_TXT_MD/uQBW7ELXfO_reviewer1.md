### Summary

The paper proposes to use adversarial training for the Schrodinger Bridge problem to tackle the image-to-image translation problem. The approach is shown to outperform several other popular methods for this problem.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and the approach is well-motivated. The results are strong and outperform several baselines.

### Weaknesses

#### Some Related Works

[1] Path Integral Sampler: A Stochastic Control Approach to Sampling
[2] Unbiased Path Integral Sampler via Stochastic Optimal Control
[3] Neural Optimal Transport

#### comment

My main concern is the novelty of the approach. The idea of using adversarial training for the Schrodinger Bridge problem is not new. It was proposed in the Path Integral Sampler (PIS) paper [1] and its unbiased variant [2]. The difference between the current paper and the PIS line of work is that the current paper applies the approach to the image-to-image translation problem only. In comparison, the PIS paper proposed it as a general sampling approach. In fact, the current paper cites the PIS paper only in the context of the image-to-image translation experiments. The theoretical results in Theorem 1 also seem similar to the ones in the PIS paper, but I lack expertise in the area to judge the novelty. Can the authors comment on the novelty of their approach compared to PIS?

The experimental results on the two shells dataset are interesting. However, I would be more interested in seeing the results on some high-dimensional sampling tasks. For example, the authors can consider sampling Gaussian or non-Gaussian distributions, as in the PIS paper. The current results only show that the proposed method outperforms a method that is only applicable to low-dimensional problems. Hence, it is not clear what is the exact problem that the proposed method is solving. Is it sampling? If it is, the authors should demonstrate that the method can sample from challenging, high-dimensional distributions. If the method is not for sampling, then what is the problem that the method is solving, and why do we need it?

Regarding the image-to-image translation experiments, the authors should include the results of DIODE as a baseline. The current results are not very convincing because the proposed method is a multi-step diffusion approach, while the baselines are one-step approaches. The comparison is not fair. Can the authors include the results of a multi-step diffusion approach like DIODE [3]?

### Suggestions

The core issue with this paper is the lack of clarity regarding its contribution and the limited scope of its experimental validation. While the authors propose using adversarial training for the Schrodinger Bridge problem, this idea is not novel, as it has been explored in the Path Integral Sampler (PIS) papers. The current work seems to apply this idea to the image-to-image translation problem, but the authors do not clearly articulate the advantages of their approach over existing methods, especially in the context of sampling. The theoretical novelty of Theorem 1 is also questionable, as it appears similar to results in the PIS paper, and the authors themselves lack the expertise to make a definitive judgment. To address this, the authors should provide a more detailed comparison of their theoretical results with those in the PIS papers, highlighting any key differences or extensions. Furthermore, the authors should clearly state whether their method is intended for sampling or image-to-image translation, and justify their choice of experiments based on this clarification.

If the method is intended for sampling, the experimental section needs significant expansion. The current experiments on the two shells dataset are insufficient to demonstrate the method's capability in high-dimensional spaces. The authors should include experiments on more challenging sampling tasks, such as sampling from high-dimensional Gaussian or non-Gaussian distributions, as done in the PIS paper. This would provide a more comprehensive evaluation of the method's sampling performance and allow for a more direct comparison with PIS. The authors should also clarify why they chose to focus on image-to-image translation, given that the core idea is a general sampling approach. If the method is primarily for image-to-image translation, then the authors should focus on demonstrating its advantages over existing image-to-image translation methods, rather than comparing it to general sampling methods.

Finally, the image-to-image translation experiments need to be more robust. The current comparison with one-step approaches is not fair, as the proposed method is a multi-step diffusion approach. The authors should include a comparison with other multi-step diffusion approaches, such as DIODE, to provide a more balanced evaluation. This would help to determine whether the proposed method offers any advantages over existing state-of-the-art image-to-image translation methods. The authors should also provide a more detailed analysis of the results, including a discussion of the strengths and weaknesses of their method compared to the baselines. Without these additional experiments and analysis, it is difficult to assess the true value of the proposed method.

### Questions

1. What is the novelty of the proposed approach compared to the PIS paper?
2. Can the authors include the results of some high-dimensional sampling tasks?
3. Can the authors include the results of DIODE?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
