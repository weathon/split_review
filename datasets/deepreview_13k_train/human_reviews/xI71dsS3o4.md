# (Mis)Fitting Scaling Laws: A Survey of Scaling Law Fitting Techniques in Deep Learning

- Decision: Accept
- Scores: 5, 5, 8, 5

## Abstract
Modern foundation models rely heavily on using scaling laws to guide crucial training decisions. Researchers often extrapolate the optimal architecture and hyper parameters settings from smaller training runs by describing the relationship between, loss, or task performance, and scale. All components of this process vary, from the specific equation being fit, to the training setup, to the optimization method. Each of these factors may affect the fitted law, and therefore, the conclusions of a given study. We discuss discrepancies in the conclusions that several prior works reach, on questions such as the optimal token to parameter ratio. We augment this discussion with our own analysis of the critical impact that changes in specific details may effect in a scaling study, and the resulting altered conclusions. Additionally, we survey over 50 papers that study scaling trends: while 45 of these papers quantify these trends using a power law, most under-report crucial details needed to reproduce their findings. To mitigate this, we we propose a checklist for authors to consider while contributing to scaling law research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper surveyed/ more than 50 papers about the scaling law of language models. Authors discussed different aspects of scaling law including fitting forms, model training, data extraction, and fitting optimization. Based on that, authors provided a checklist, which helps to transparent settings for reproducible results in future research. Experiments also were conducted to verify their replication and analyses.

### Strengths
This paper has several strengths:
- This paper considers a timely topic, the scaling law of language models. Understanding this topic will help to effectively train LLMs, avoiding resource overuse. 
- Authors discussed the discrepancies in experiment settings of different papers and empirically verified it. Results are aligned with previous works.
- Authors open-sourced their code to reproduce results which benefits the community since the source code is usually absent from previous papers.

### Weaknesses
Despite these strengths, this paper has several weaknesses:
- The scale of the model in experiments is not big enough. Authors consider only models with less than 400M params, ignoring the existence of larger models with billions of params. The experiments should include models that span a much wider range of parameter counts to properly validate the scaling laws. The current range is insufficient to extrapolate to the larger models that are of primary interest in the field. The lack of larger models limits the conclusions that can be drawn about the general applicability of the identified scaling laws.
- The writing in some parts of the main paper causes confusion. E.g., Section 5 is about data extraction after training, I was confused by which kind of data could be extracted. The term 'data extraction' is vague and does not clearly indicate what is being extracted from the trained models. It is unclear whether this refers to model weights, activations, or some other form of data. This lack of clarity makes it difficult to understand the methodology and replicate the experiments.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors survey a large corpus of papers that involve scaling laws, and find that many papers underreport necessary details for reproducibility, which they demonstrate with experiments that demonstrate a large variability depending on those exact choices of details. They propose a checklist for authors to consider when publishing scaling laws.

### Strengths
The paper gives a good overview of many papers on scaling laws, and nicely categorizes the important steps: functional form, training setup, data(points) extraction, curve fitting. The checklist provides a clear way of reproducibility and quality assessment of scaling experiments. I think the topic of scaling law studies is important and relevant, and the writing is clear.

### Weaknesses
The main concern for me is the following: what is the main goal the authors are trying to convey? To me, there are two obvious takeaways, which is 1) changes to the scaling law setup can change the results drastically, and 2) previous papers very much underreport crucial details. However, both of these things are rather clear already to the community and also illustrated by published papers: for example, point 1) is shown by Porian et al., and point 2) is a broader critique of reproducibility problems, which (unfortunately) is a generic problem. I do not see a clear and actionable interpretation beyond that. For instance, how do the different choices of fitting actually affect the scaling laws? (The assessment is mostly just “the results vary dramatically” — but how?) What should I as a researcher now do for my future scaling studies, having read your paper, beyond using the checklist? Are there clearly ‘wrong’ or ‘right’ choices? Was there a most predictive scaling law (e.g. when you leave out some experiments as a validation set)?

To be clear, I very much believe there is merit in a survey or pointing out these problems; as it stands, however, the paper is foremost “just” a survey, and I am not convinced this merits publishing at the conference.

Some additional comments: 
 * The paper template says ICLR 2024
 * The Figures are unfortunately of low quality (very pixelated), especially considering the fact that it’s natural to zoom in to compare the many lines and details. I suggest the authors include the pdf forms for proper rendering.

### Questions
I have already listed direct questions in the section above, and I would be open to discuss this in the rebuttal. I hope the authors see the comments to be constructive, and can clarify or improve the distinctive value of the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work revisits scaling laws and factors influencing the results reported in recent papers. The paper takes a "review approach", outlining some of the debates in recent literature as well as common strategies. To draw conclusions and emphasize their points, the last pages are dedicated to an in-depth analysis by the authors on small to moderate size transformers.

### Strengths
I really like this paper and think it is of great value for the community to "recap" scaling law results and provide a critical discussion, complemented by experiments showing which factors matter when choosing a scaling law. It was really a pleasant read, quality of writing is good and the motivation clear.

### Weaknesses
One could maybe claim the paper is not too constructive, as it shows that choices (optimizer, fitting method, lr annealing, data) matter when fitting a scaling law: there is no correct answer. However, this conclusion demystifies the topic, which I like very much: there is no magic, just common choices and "usual" results. This said, there are a couple of very minor points.

1) Proposing a checklist is helpful, but, as the authors themselves seem to hint, the number of factors to account for is potentially infinite. What about Adam beta2? What about weight decay? What about hybrid algorithms? What about qk norm and new tricks? The reality this paper points out is that, indeed, such choices matter, and I do not think any checklist can be conclusive. The checklist, while useful as a starting point, risks giving a false sense of completeness, potentially overlooking crucial, subtle interactions between these hyperparameters and the scaling behavior. For example, the interplay between weight decay and learning rate schedule can significantly impact the effective regularization and thus the observed scaling exponent, which is not easily captured by a simple checklist item.

2) section 7.1: why did you decide to set alpha=beta?

3) The paper lacks a bit of conclusions: what should researchers do? should we trust scaling laws? what are the things that hold true despite changing the setting? Is there some practical rule for scaling that holds approximately in your experiments? (would have been interesting alpha and beta)

typo spot: "was was" in the abstract, repetition.

### Questions
-

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a survey on the fitting of scaling laws, and argue that current practices are lacking in scientific rigor. Apart from an extensive survey, the authors presents a reproducibility checklist, and compare 51 papers to this checklist. They generally find that important details are underreported, e.g. the method to calculate model parameters might not be given. They also provide a replication study of Hoffman, using data extracted from the paper PDF and data they’ve collected themselves. Here they find that subtle choices in the curve fitting can result in significantly different conclusions.

### Strengths
- Scaling laws is an important topic, and scientific rigor here can benefit the research community.
- The authors illustrate how subtle choices in the curve fitting can cause significant results
- Section 7 is great.

### Weaknesses
 - Significant parts of the papers are dedicated to a survey. I’m not sure survey papers are the right fit for ICLR main track.
- There are not so many empirical results. The paper focuses heavily on a checklist and a replication study, but lacks a broader set of empirical investigations to support the claims about the impact of different fitting choices. The replication study, while valuable, is limited in scope and does not explore a wide range of models or datasets. The paper would benefit from more extensive empirical validation of the proposed checklist and its impact on the reliability of scaling law analysis.


### Questions
- could you provide explicit recommendation regarding how to perform the curve fitting? I think this is different from a checklist which allows reproduction. 
- Could you expand section 7?

### Soundness
3

### Presentation
2

### Contribution
2
