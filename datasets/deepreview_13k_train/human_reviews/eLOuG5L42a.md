# MindSet: Vision. A toolbox for testing DNNs on key psychological experiments

- Decision: Reject
- Scores: 3, 8, 3, 3, 8

## Abstract
Multiple benchmarks have been developed to assess the alignment between deep neural networks (DNNs) and human vision. In almost all cases these benchmarks are observational in the sense they are composed of behavioural and brain responses to naturalistic images that have not been manipulated to test hypotheses regarding how DNNs or humans perceive and identify objects. Here we introduce the toolbox \textit{MindSet: Vision}, consisting of a collection of image datasets and related scripts designed to test DNNs on 30 psychological findings. In all experimental conditions, the stimuli are systematically manipulated to test specific hypotheses regarding human visual perception and object recognition. We test ResNet-152 on each of these methods as an example of how the toolbox can be used.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
They authors introduce MindSet, a benchmark of image datasets and experiments to compare visual perception of humans and models. The benchmark spans multiple levels of perception, from low and mid-level vision to object recognition and visual reasoning. What differentiates this benchmark from others is that it combines experimental manipulations with each image dataset. For example, in a version of a same/different task that's been studied over the years, the authors test the task as they change object features, such as the color, open/closed-ness of the shapes, etc. The benchmark is comprehensive, albeit scattershot, and the authors also discuss a variety of ways to evaluate models on their benchmark.

**Update**

After discussing with the authors, I've decided to keep my score. I think they have great points about how NeuroAI should shift incorporate a broader set of psychological experiments as well as perturbations to build the next generation of models of biological vision. I also think that the experiments and datasets described in this paper could be one part of that story. But I disagree with the authors that the current paper constitutes a sufficient work package for ICLR. What I would have liked to see are benchmarks on the TIMM library (https://github.com/huggingface/pytorch-image-models) to show empirically how today's models, designed by computer scientists, respond on these experiments. The authors point out that some of that work has been done in the past, but there is not central benchmark for these models, and the authors must back up their claims of misalignment and failure of today's models with evidence. I believe the bar for publication in a journal/conference that is not a review should be experiments like these, even if they are null results. If those experiments were here I would recommend acceptance. As they are not, I do not think this paper should go through and will keep my score where it is.

### Strengths
I really like the emphasis on perturbation, which is an essential missing ingredient in popular benchmarks like BrainScore. This indeed appears to be the main — and IMO a powerful — motivation for the paper. To push computational vision and neuroscience into a new and more effective regime for modeling brain data.

The benchmark itself is comprised of many different interesting experiments taken from psychology and neuroscience. I appreciate the goal of searching for a single model that can explain everything from lightness illusions to visual reasoning.

### Weaknesses
The biggest problem with this paper is that it does not make a clear contribution. None of the experiments are novel. There's no actual benchmarking done on models. It's a scattershot approach which is probably the only way this could be done, but there's no control across the different benchmarks — i.e., a single set of visual primitives used to test low-and mid-level vision and visual illusions vs. another set for shape/object recognition. I don't know what to take from this paper other than it's reasonably argued that the current state-of-the-art is insufficient and perturbations would be a better way of advancing models of human vision. Not much more to say than this. What the paper needs is the following:

- A large scale survey of existing models. How well do they capture human data for each experiment?
- If there's no positive result in existing models, provide a model that has a positive result.
- Ideally, and as mentioned above, data is held constant while you change task. For example, could you test relational vs. coordinate change, NAP vs. MP, Muller-Lyer illusion using the same constituent visual components? That is, the number of "on" pixels is the same in each example, but the perceptual effect those pixels have is fundamentally different? This would at least make it possible to plot the experimental results of each of these experiments against each other. This is more of a thought than a must have, given the wide variety of experiments, but IMO it is an essential part of testing models in order to ensure that task rather than statistics are driving a given result.

Another problem I see is in the similarity judgement analysis summarized in Fig 2. The authors use euclidean distance between stimuli to compare their representations at different layers of a network. Why use this instead of the decoder method? There's no reason why euclidean distance is the "right" metric for making decisions at a given layer. Moreover, I don't believe that the bar-and-whisker plots back up the authors' assertion of a difference in same/different shape conditions in early vs. late layers.

### Questions
See weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MindSet a toolbox for testing DNNs on more than 30 psychological findings.  Including  test for low-level vision,  and high level vision such as visual illusions  and  shape and object recognition. This toolbox, will help authors test on a controlled environment how brain-like are these.

### Strengths
I really appreciate the effort that went into creating this toolbox. I think it could greatly benefit the community, especially since many recent tests have focused increasingly on performance in neural alignment, often overlooking functional alignment beyond accuracy alone. The presentation is well-executed, and I particularly enjoyed the failure modes discussed in the supplementary material. My only suggestion would be to consider moving some of these examples into the main text to further highlight the value of this toolbox.

### Weaknesses
Perhaps my only question is that it seems that is largely synthetic images on black and white,  which makes it more controllable, but not sure if this would also constrain the kind of models and training routines that can be used in the test, because most models would be trained on complicated backgrounds, such as naturalistic scenes.

### Questions
* Would the types of images in the benchmark constrain the kinds of models or training data that people can use, given that most models are usually trained on more crowded scenarios?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This is a very interesting and well timed paper that introduced a dataset full of interesting psychological visual phenomena to test and compare humans and machines in a more precise and well-rounded manner than just accuracy/performance on a classification dataset (which is classical in computer vision & machine learning). The paper is extremely well written and articulated the need for a dataset like this one, and the authors do a spectacular job in citing all the relevant literature in this new type of "NeuroAI" wave where humans and DNN's are being compared. The only main weakness I see is that I wish there were more evaluations, or at least one solid one which is why I have reserved my vote for a marginally above threshold. Nevertheless, I do think that all in all this paper should be accepted provided a more extensive evaluation of at least one Neural Network with more detail -- that I did not see in the Appendix (although the Appendix does do a great job in covering all the vision science phenomena and illusions that are to be studied/tested by humans and machines).

----------

**Upgrade*

I have downgraded by score to 3 after reading all the reviews from different reviewers and I think the consesus holds that even though the papers intention is very insightful and unique, the lack of experiments and empirical validation for human-machine visual alignment undersells the true potential value of this paper. I think adding those basic experiments (only even 1 to 3 architectures) can put it at a high Oral-worthy position for a future CV/ML conference.

### Strengths
* The paper is extremely well written. Despite having a background at the intersection of human and machine vision as a reviewer and being quite familiar with nearly all the works cited, the authors have done a great job in articulating why this dataset is important **for machine vision & computer vision** hence the proper fit for ICLR.
* The paper covers a lot of great literature at the intersection of machine vision and human vision, in addition to papers that try to link both phenomena. I think this paper could serve as a great "reference" to read for many early graduate students who would like to learn more about the topic that the authors are exploring and justifying its importance.
* The rigor in which the paper all 30 psychological findings in the main body and appendix is superb.

### Weaknesses
The greatest weakness I see in this paper is that there is little to no evaluations. There is barely only two figures to evaluate the ResNet-152, and the paper leaves me with a bittersweet feeling of wanting to know how well did the ResNet-152 do compared to the average human on the collection of all the images in the toolbox. Without a more thorough evaluation, it's difficult to empirically assess the claim that standard models struggle with these perceptual phenomena. The current evaluation is insufficient to demonstrate the limitations of existing models on the proposed dataset, which is a crucial aspect of the paper's contribution. The lack of a comprehensive benchmark makes it hard to gauge the true value of the dataset for the computer vision community.

### Questions
Is there anyway we can get a figure of how the ResNet-152 does for all 30 psychological findings, as if we could get a row of 1 model entry as if this was Brain-Score? I think this would really drive the paper home and come full circle so that readers from computer vision and machine learning who do not know anything about neuroscience (or assume that machines see just like humans) -- can be surprised and find this paper even more valuable.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work provides Python code to generate controllable visual stimulus sets from 30 well-known cognitive psychology experiments. The underlying motivation is to provide a hypothesis-driven approach for comparing neural networks to human vision, as an alternative to benchmarking with natural image datasets and associated behavioral or neural responses (e.g., BrainScore). The work also introduces three alternative methods for evaluating model predictions, accompanied by example Python implementations.

### Strengths
1. Bridging cognitive psychology and neural network research is a laudable goal. Curating experimental results and making them accessible to the neural network research community is an effective way to achieve this and clearly establishes the motivation for this contribution.

2. The collection of stimulus sets is extensive and diverse.

3. Based on my review, the codebase appears well-designed, well-organized, and well-documented. The paper itself is also clearly written.

### Weaknesses
1) The paper describes "datasets"; however, it contains no actual, complete data—only stimuli and stimulus generation scripts. In behavioral research, data typically includes, at a minimum, temporally ordered pairs of stimuli and empirical human responses. Generating stimuli is only the first step.

   A major hurdle in comparing human behavior with neural network models is obtaining high-quality human behavioral data collected in controlled settings. This hurdle is particularly challenging for researchers from engineering departments, where institutional infrastructure and practical know-how for conducting in-person human experiments are often lacking. Since data sharing is relatively new in experimental psychology, many classical results are available only as aggregate data (e.g., bar charts or ANOVA outcomes) rather than as recordings of human responses at the single-trial, single-participant level. Such raw responses may be essential for testing new hypotheses and evaluating statistical significance and reliability.

   Currently, the lack of associated behavioral data severely limits the potential impact of this contribution. For comparison, consider the works by Robert Geirhos et al. on robustness to transformations. These works have been impactful not only for their research questions but also for providing large-scale human response data as a community resource.

2) The theoretical contextualization of this work is relatively narrow and one-sided. The authors motivate their approach by referencing the 2022 BBS target paper by Bowers et al., reiterating some of its arguments (e.g., "...competing on observational datasets that do not
support any conclusions regarding the mechanistic similarity of DNNs and brains"). However, the current paper does not substantially engage with any of the counter-arguments presented in the 29 responses to the Bowers et al. paper. Scientific debate is essential, but it can only be productive when effort is made to consider opposing views.

### Questions
1. In my opinion, for this work to be complete and ready for publication, each task should be accompanied by human data, either collected by the authors or curated from open data repositories. This data should be provided in both raw format and aggregated by condition. If the effects are strong and unequivocal, obtaining the relevant data should be straightforward. If the interpretation of the experimental outcomes is more complicated, the availability of detailed behavioral data becomes even more important. I believe that such a substantial revision would make this work highly impactful for the field.

2. A complete description of each experiment should also include experiment-specific instructions for both experimenters and participants, as well as the expected results according to alternative hypotheses. An experiment in psychology is more than just a set of stimuli.

3. Will training a neural network directly to imitate human performance in these tasks produce a model that the authors consider valid? If not, it may be worthwhile to specify the appropriate training distribution for each task.

4. In this context, it might be worthwhile for the authors to discuss the recent paper by Marcel Binz et al., "Centaur: A Foundation Model of Human Cognition," which appears to take a direct data-fitting approach.

Minor: There are multiple issues in the bibliography, including duplicated entries and papers already published in conferences cited as arXiv preprints.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a toolbox for creating 30 static visual tasks to test specific hypotheses about the capabilities of DNNs in comparison to the human visual system, for example how a DNN performs when subjected to crowding. Like the well-established Brain-Score benchmark, this toolbox provides a collection of visual tasks on which any DNN could be evaluated. Unlike Brain-Score, the authors propose to not simply evaluate models on observational data and aggregate performance to obtain a ranking, but to explicitly test specific hypotheses about the abilities of the models, which should be simplified by the proposed toolbox.

### Strengths
The paper is well-written and technically sound, as is the code. The proposed tasks are all sensible (and could be extended to include new tasks, should the need arise) and reflect the field well, so the toolbox could be of great practical utility. Because the toolbox makes evaluating models on these different hypothesis tests easy, there is a good chance that it will indeed be used to evaluate new models, which would be beneficial for the community. The core point that the authors want to raise (about testing specific hypotheses, instead of predicting observational data) is also valid and meaningfully adds to the discourse about human-DNN alignment.

### Weaknesses
The main weakness of the paper is the lack of experiments and results. The authors only present the toolbox and superficially evaluate a ResNet-152, but they do not derive any new findings or concretely outline how this could be done, which would greatly increase the perceived utility of the toolbox. For example, the paper could have included a more thorough analysis of how different architectures perform across the various tasks, highlighting specific strengths and weaknesses of each model in relation to the proposed hypothesis tests. This would have provided a more compelling demonstration of the toolbox's capabilities. Another issue is the lack of human reference data: While it is generally known that humans are e.g. sensitive to crowding, the toolbox is missing human reference performance for the default set of stimuli that the authors provide. This makes it difficult to directly compare model performance to human performance, which is a key goal of the work. Ideally, the authors would have included a baseline of human performance on each task, perhaps through a small-scale psychophysics study. However, such data could over time be collected and contributed by the community.

### Questions
The work presented here is done well, and the decision to accept or reject ultimately comes down to whether one believes that the implementation of this toolbox is a sufficient contribution.

I propose to accept the paper, because I can imagine the practical value in having such a standardized toolbox. It will at least save the community some work, and if standardized procedures for generating these stimuli emerge, results could become more directly comparable. Furthermore, the authors argue for an alternative paradigm in how to evaluate human-machine alignment, which I deem a valuable intellectual contribution, even though this point remains a bit vague. Elaborating more on what this would entail could improve the paper. Overall, the paper does feel a bit thin, lacking both evaluations of a relevant suite of models and human reference data. While the latter might be too much to ask, evaluating a few models (e.g. models scoring high on Brain-Score or human-vs-machine) would have been interesting and justified the submission to ICLR better.

As a general point of discussion: In principle, these tasks could be integrated into Brain-Score, if there was human data to compare models to. While I understand that the authors are (for fair reasons) skeptical of the Brain-Score methodology of averaging performance, it would still be valuable to at least reflect this dimension of human-DNN-(mis)alignment on Brain-Score as well, even if it just highlights how none of the models that do well on predicting neural data show human-like performance on these tasks.


### Nitpicks
* in line 49, there seems to be a broken citation
* in line 108, there should be a space: "to understand"
* in the README of the repository, the link to ImageNet classification is broken (because it should be imagenet_ood_classification)

### Soundness
3

### Presentation
4

### Contribution
3
