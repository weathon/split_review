# Data-Juicer Sandbox: A Comprehensive Suite for Multimodal Data-Model Co-development

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
The emergence of large-scale multi-modal generative models has drastically advanced artificial intelligence, introducing unprecedented levels of performance and functionality. 
However, optimizing these models remains challenging due to historically isolated paths of model-centric and data-centric developments, leading to suboptimal outcomes and inefficient resource utilization. 
In response, we present a novel sandbox suite tailored for integrated data-model co-development. This sandbox provides a comprehensive experimental platform, enabling rapid iteration and insight-driven refinement of both data and models. 
Our proposed ``Probe-Analyze-Refine'' workflow, validated through applications on state-of-the-art LLaVA-like and DiT-based models, yields significant performance boosts, such as topping the VBench leaderboard. 
We also uncover fruitful insights gleaned from exhaustive benchmarks, shedding light on the critical interplay between data quality, diversity, and model behavior.md}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a sandbox suite designed for integrated data-model co-development, promoting efficient experimentation. The proposed "Probe-Analyze-Refine" workflow demonstrates notable performance improvements on the VBench leaderboard. Overall, the work presents a practical solution to optimizing multimodal models effectively.

### Strengths
- The paper is generally easy to follow, the presentation of the idea is clear.
- Co-developing data + model pipeline is a valid idea and meaningful to explore
- The insights in section 5 are interesting.

### Weaknesses
 - I found the langauge of the paper often involves exaggeration and flashy vocabulary, and it is too much for an academic paper which sometimes make it hard to read. I suggests authors use more plain and clean language. 
- More experiments need to prove the effectiveness of the method, e.g. for the image-to-text tasks, is there any evaluation results demontrating the effectiveness of the method?
- in section 5.4: "advancing from the 40k data pool used in Section 5 to a significantly more voluminous dataset, approximately 22× larger...", does that mean the performance in tab 2 is achieved with much larger training data than other baselines? 
- Is there any ablation done for tab 2, to provide insights on whether the proposed method is data efficient?

### Questions
- in section 5.4: "advancing from the 40k data pool used in Section 5 to a significantly more voluminous dataset, approximately 22× larger...", does that mean the performance in tab 2 is achieved with much larger training data than other baselines? 
- Is there any ablation done for tab 2, to provide insights on whether the proposed method is data efficient?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces an innovative open-source sandbox suite for collaborative development of multimodal data and generative models. IT presents a progressive workflow for data-model development, demonstrating significant performance improvements in image understanding and video generation. Extensive evaluations reveal valuable insights for future multimodal generative models development.

### Strengths
- The introduction of an open-source sandbox suite enables more efficient and well-planned data processing and model training processes
- The observations provided are valuable insights that could guide other researchers in their work

### Weaknesses
 - The paper could benefit from more discussions on how Data-Juicer differs from existing workflows/infrastructure
- I'm also curious to learn whether Data-Juicer is easily adaptable for potential changes/development in the field

### Questions
- discussions on how Data-Juicer differs from existing workflows/infrastructure
- Is Data-Juicer easily adaptable for potential changes/development in the field?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a sandbox tool that allows rapid testing and analysis of multiple datasets in the training of machine learning models. It contains multiple classes that provide filtering operations and other evaluative capabilities. The paper also proposes a workflow named "Probe-Analyze-Refine". It first creates equal sized data subsets by slicing data on percentile ranks based off various data-related metrics. It then trains and evaluates models on external benchmarks to identify the best data splits, defined as the best performance on the benchmarks. It also attempts to combine the filtering operations in an attempt to create better training subsets. The paper then performs a study and presents various observations of their experiments.

### Strengths
The paper introduces an open-sourced tool that may be useful to the community. It demonstrates its utility by performing some data experiments; by training MGM-2B models on different slices of the original data, the authors draw conclusions about the effectiveness of various data slices. While the takeaways are not surprising, they help the community by being experiment validations of some long-held “common-knowledge”.

### Weaknesses
The paper needs to decide if it is trying to introduce the Data Juicer Sandbox platform or to derive insights from data tests. It starts off introducing the Sandbox and, as a reader, I expected to understand the various functionalities and automation it offers. However, it doesn’t go into details about its implementation (e.g., perhaps some code optimization of the data process), demonstrate how it helps the users (e.g., maybe the user has to write only 4 lines of code instead of 50), or even the terminology (e.g., workflow, behavior, and capabilities from Lines 125—126 are not defined and the relationship between them is unclear). It then abruptly switches to introducing how to do data splits and training models on them to test their impact on the final performance of the models. The rest of the paper then elaborates on different ways to combine filters in attempts to obtain a final data subset that will result in more efficient training and a better final model. Without understanding the focus of the paper, it is difficult to judge its overall contribution.

Overall, the paper can also benefit from simpler and cleaner presentation; words like “bespoke” (L125) can be eliminated without changing the meaning of the sentences. Some of the figures can benefit from subfigures and subcaptions. The grammar can improve but this is relatively minor.

### Questions
1.	L91-92: Is there a source for “traditional data-centric or model-centric strategies … resource misallocation”?
2.	Does the Data-Juicer sandbox require specific infrastructure/machines or does it work out-of-the-box in any computing environment or hardware (e.g., with TPUs)?
3.	Many companies/research labs have their own workflow for scaling data processing and training. They also study scaling laws and various data filters. What are the advantages of using Data-Juicer sandbox compared to their customized process? How can you improve to coax them to join your open-sourced framework/project?
4.	Are the "data processing operators (OPs)" defined in the article (e.g., on L186) simply data filters?
5.	Is there a reason why the data is sorted into three equal sized pools (L210 – L211) instead of just 2? Why not have 4 or 5 buckets? It would suffice to explain your rationale for your choice.
6.	How is “size of the data pool” defined? What happens if the filter results in less than required amount of data (e.g., “size” set to 200k but the result of filtering is 100k)? Please explain the terms clearer.
7. Is there a fixed computing budget for training a model on each data slice? If so, how is it defined (e.g., time budget or number of TFLOPS)?
8.	How is the “expansion rate” (L416) defined? If it means duplicating the data slice, please just mention it as such. Duplicating the data slice essentially means that the model has been trained for more epochs. Is it then fair to compare 2 models when the number of epochs trained are different?
9. How do you ensure that the models are "done" training?
10.	Related to the above question, it may be good to illustrate the training convergence of some of models on different data slices.
11. Overall, it would be good to consider the interaction between data, models, and compute instead of only the former 2.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In their work, authors develop a method for co-development of multi-modal data and generative models. Data Juicer Sandbox defines a pipeline for composing data from available data pools by testing various data processing operators (OP) with regard to how those improve the quality of dataset composition for model training. This probe-analyse-refine workflow computes various stats by applying OPs to data pools and employing low cost model training to compute evals on trained models, taking the OPs leading to top performing evals for combining those OPs to create datasets at larger scales, which should further boost model training. Authors test their approach on MiniGemini (image-to-text), EasyAnimate and T2V-Turbo (text-to-video) and ModelScope, evaluating model performance on benchmarks like MMBench and VBench to provide evidence that dataset composition procedure leads to performant models. Authors conclude that observed model performance delivers evidence for the effectiveness of the prooposed data-model co-development framework.

UPDATE: score raised to 5 after rebuttal following experiments with CLIP and providing info on compute involved in video modelling experiments.

### Strengths
Authors address important question of how to systematically search for operations that improve dataset quality, composing datasets that result in stronger models when used for training. The workflow is open-sourced, and the study seems reproducible.

### Weaknesses
Central weakness is that the study attempts to make a strong claim (the presented pipeline for data-model co-development leading to dataset and model improvement) while not having proper validation via model comparison. Authors take models on a fixed reference scale and make a comparison to their method. No attempt is made to match compute or scales when doing comparison, which makes model comparison inconclusive. Authors do not attempt to derive a scaling law over model and data scales involved in their pipeline, which would at least help to understand whether claim of model improvement is consistent across at least a modest scale span. Without such experiments, evidence is weak and strong claims for general usefulness are not substantiated enough.

Important citations of previous works that attempt to design methods for systematic search of better datasets are missing. Just few examples: [DataComp, NeurIPS 2023](https://openreview.net/forum?id=dVaWCDMBof), [MetaCLIP, ICLR 2024](https://openreview.net/forum?id=5BCFlnfE1g). In DataComp for instance it is demonstrated how data and model quality should be measured across scale span.

Further weakness is paper organization. Many important experimental and method workflow design decisions and also important result details are shifted to supplementary, so that large fraction of main part reads like a coarse overview. To assess the work, reader has to go to Appendix, as main text seems to be insufficient.

### Questions
Why - instead of taking models that are rather not yet well established as references - do authors not take strong open reference models,  eg openCLIP, Stable Diffusion, etc, and show the strength of their approach by demonstrating how to obtain eg stronger CLIP models across various scales? That would give the method much better support, as CLIP is a strong reference trained across various open data with measurements across scales already available. That would be a clear way to show benefits if authors method would provide evidence for obtaining strong CLIP models compared to existing well established references using their data operations search procedure, deriving a scaling law for their method.

### Soundness
2

### Presentation
2

### Contribution
3
