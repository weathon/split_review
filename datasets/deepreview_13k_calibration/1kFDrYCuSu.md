# PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Foundation models trained on internet-scale data benefit from extensive alignment to human preferences before deployment. However, existing methods typically assume a homogeneous preference shared by all individuals, overlooking the diversity inherent in human values. In this work, we propose a general reward modeling framework for pluralistic alignment (PAL), which incorporates diverse preferences from the ground up. PAL has a modular design that leverages commonalities across users while catering to individual personalization, enabling efficient few-shot localization of preferences for new users. Extensive empirical evaluation demonstrates that PAL matches or outperforms state-of-the-art methods on both text-to-text and text-to-image tasks: on Reddit TL;DR Summary, PAL is 1.7% more accurate for seen users and 36% more accurate for unseen users compared to the previous best method, with 100× less parameters. On Pick-a-Pic v2, PAL is 2.5% more accurate than the best method with 156× fewer learned parameters. Finally, we provide theoretical analysis for generalization of rewards learned via PAL framework showcasing the reduction in number of samples needed per user.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
While it is well-known that humans have diverse preferences, most foundation model alignment methods assume homogeneous preference across all users. The authors propose a novel reward modeling framework to capture shared as well as personalized preferences to enable pluralistic alignment. The method's ability to combine global and individual preferences allows the method to perform well without requiring an overwhelming number of samples for each persona. The method is also demonstrated to outperform homogeneous reward models when diverse preferences are introduced to the evaluation dataset.

### Strengths
1. The method addresses the problem of pluralistic alignment, which is currently unaddressed by most alignment methods.
2. The method has a native flexibility to adjust the shared and personalized portions of the modeled preference.
3. The method complements existing alignment methods.
4. The paper rigorously explores the behavior of the method through simulated experiments and the results are visualized clearly, as are the algorithms. The experimental setup is clearly documented.
5. The method converges quickly to capture the preferences of unseen users

### Weaknesses
It does not seem like there is a benchmark that reflects real use cases that can highlight the benefits of having a heterogeneous model; both Reddit TL;DR and Pick-a-Filter are both semi-synthesized datasets that artificially accentuates the diversity of human preference. This calls into question whether pluralistic alignment is a valuable problem to solve.

### Questions
1. Are there benchmarks curated with real world data that can highlight the benefits of pluralistic alignment?
2. In section D.3.2, it is mentioned that the choice of foundation model greatly impacts the performance of the proposed method. It would be great to do an ablation study to investigate whether this effect is observed with other alignment methods as well.
3. When should one opt for either PAL A or PAL B?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper tackles the issue of personalized reward modeling. The authors recognize that different users may not generate a consistent preference across different context-sample pairs. They propose two novel modeling method that represent preference with a latent reward function. PAL-A assumes the reward of a sample-context pair is determined by its distance to the user's ideal point in a latent space. It further assumes that the ideal points of a population lies in the convex hull of several supporting points in the latent space, and we can recover an individual's personalized preference through weighted average of supporting points. PAL-B represents preference as unknown preference mapping, and commonalities are similarly modeled as a convex combination of K prototypical mapping.

The author conducted extensive experiments on both NLP and T2I generation domain, achieving SOTA results

### Strengths
The paper challenges a commonly overlooked assumption in the alignment literature, that individuals' may have a different preference.  The proposed two approaches are novel and clearly differentiates from existing works (e.g. KTO), which treat such inconsistencies as noises in preference data.  The presentation is clear and easy to follow, with motivations and formulations of the proposed method covered in detail. The experiments showed strong performance of the proposed method. Moreover, the proposed method can be trained on a single consumer grade GPU whereas the baselines are trained on multiple A100s.

### Weaknesses
1.Some experiment details are lossy and not well-documented.  Presentation is a bit unclear. For example, while the authors clearly documented the choice of base model and training data on Pick-v2 results (table 3), such information is not included in Pick-v1 (table 2). **What is the base model for results in table 2? Is it vanilla CLIP-H or PickScore?**

Without this knowledge, it is hard to evaluate the claim on parameter efficiency. For example, if v1 results are reported via a model that is fine-tuned on Pick-v1 embedding, then it is hard to argue that the model is more parameter efficient since it starts with a fully fine-tuned model. Overall, presentation wise, I think it would make more sense to add table 2 as an extra column in table 3, which would reduce many confusions on the setup.

2.Results on Pick-a-Filter are unconvincing.

2.1  Pickscore baseline is missing. While the authors claim that they cannot compare PickScore as its training set overlaps with Pick-a-Filter’s val set. However, this can be trivially fixed be eliminating the overlapped examples, which the authors already did for table 3. Why not do the same? Alternatively, given the large samples of pick-a-pick v2, it is not hard to construct a custom validation split that does not overlap with the training data of PickScore.

**Please either eliminate the overlapping examples from the Pick-a-Filter validation set and include PickScore as a baseline, or
construct a custom validation split from Pick-a-Pic v2 that doesn't overlap with PickScore's training data, and use this for comparison, or justify why these options are not possible**


2.2 The red and blue filter examples seems too rival, and I suspect the obvious color differences will overshadow the "commonalities" in preference.  I think the key benefits of the proposed method that it captures both the "common preferences" and "individual variations". However, for the color filters, but a naive color classifier may also achieve high accuracy in this example. It is unclear if the proposed method offer any benefits. Such comparison is required.

This is also highlighted in Fig 4, where differences in low beta region is unclear (side note: presentation wise this figure needs improvement. It is hard to tell which line is higher). I think the low beta region might be more representative of the actual discrepancies in human preferences. However, as Pickscore baseline is missing from Figure 4 (See comments in 2.1), it is hard to tell if PAL offer any benefits in this region. I image a proper pickscore comparison would be a flat line that resembles CLIP and HPSv2. The question is whether the line of PickScore would be higher than PAL in low beta region.

**I would highly appreciate it if the authors can provide more discussions on significance of results on Pick-a-Filter, particularly on the non-linear improvement in Figure 4.** It may seem that the model just collapse to a color classifier at high beta region.  **Authors should discuss if PAL is simply collapsing to a color classifier. I suggest authors compare PAL against a naive color classifier. I'm open to other means/discussion on this topic as well.**

### Questions
See weakness. Additional questions are

1. Why Reddit experiments did not include results of PAL-A? Am I missing anything?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The PAL framework aims to capture diverse human preferences from internet-scale data trained foundational models for pluralistic alignment. The modular design of the framework allows it to leverage commonalities among users while providing personalized services to each user, achieving efficient few-shot localization of preferences for new users. Through extensive empirical evaluation, PAL has demonstrated performance that matches or exceeds the state-of-the-art methods in both text-to-text and text-to-image tasks.

### Strengths
1. The PAL framework enables personalized reward modeling with fewer samples, which is highly beneficial for data collection and model training, especially when data annotation costs are high.
2. PAL has shown superior performance across multiple tasks, not only surpassing or matching the accuracy of existing state-of-the-art methods but also significantly reducing the number of parameters, demonstrating dual advantages in efficiency and effectiveness.
3. The paper not only provides empirical evaluations but also theoretical analyses, proving the sample complexity of PAL in generalizing to new users and unseen samples, providing a solid theoretical foundation for the model's reliability and effectiveness.

### Weaknesses
1. Figure 1, as the first graph of the paper, is somewhat confusing, with pasted images and formulas that are unclear. There is a lack of a clear caption explanation, and the introduction does not provide specific details, making it difficult to understand the meaning of the symbols in the graph or the order in which to view them.
2. The modeling of user preferences in the paper mainly focuses on the preference for summary length, which may not cover a broader range of personalized preferences. The preference distribution of seen and unseen users is limited to the preference for the length of summaries and may not be comprehensive enough.
3. The datasets used in the paper may lack sufficient diversity, which limits the model's generalization capabilities in a broader range of scenarios.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
