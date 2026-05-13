# ArtWhisperer: A Dataset for Characterizing Human-AI Interactions in Artistic Creations

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
In this work, we investigate how people use text-to-image models to generate desired target images. To study this interaction, we created ArtWhisperer, an online game where users are given a target image and are tasked with iteratively finding a prompt that creates a similar-looking image as the target. 
Through this game, we recorded over 50,000 human-AI interactions; each interaction corresponds to one text prompt created by a user and the corresponding generated image. 
The majority of these are repeated interactions where a user iterates to find the best prompt for their target image, making this a unique sequential dataset for studying human-AI collaborations. 
In an initial analysis of this dataset, we identify several characteristics of prompt interactions and user strategies. 
People submit diverse prompts and are able to discover a variety of text descriptions that generate similar images. Interestingly, prompt diversity does not decrease as users find better prompts.
We further propose a new metric to quantify AI model \emph{steerability} using our dataset. We define steerability as the expected number of interactions required to adequately complete a task. We estimate this value by fitting a Markov chain for each target task and calculating the expected time to reach an adequate score.
We  quantify and compare AI steerability across different types of target images and two different models, finding that images of cities and nature are more steerable than artistic and fantasy images.
We also evaluate popular vision-language models to assess their image understanding and ability to incorporate feedback.
These findings provide insights into human-AI interaction behavior, present a concrete method of assessing AI steerability, and demonstrate the general utility of the ArtWhisperer dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates human-AI interactions in the context of text to image generation models. The paper presents a gamified experimental setup called “ArtWhisperer”, where a subject is provided with a target image. The subject’s goal is to iteratively prompt the model to successfully generate an image similar to the given target image. 

The paper presents analyses of the experimental data, and defines a metric called “steerability”, which captures the human subject’s difficulty of generating an image via prompting.

### Strengths
1. The experimental data of goal-driven prompt-interactions appears to be unique, and of potential interest to the generative AI community.

2. The overall experimental setup seems reasonable — the generated images are evaluated against *generated* images; not real images. The controlled setting, is especially good, and provides important additional insights about the overall task.

3. The paper clearly discusses the major limitation of the experimental setup — relatively low (although positive) correlation between human notions of similarity and the automatic score. This is first identified via a different experimental setup, and the consequence of the mismatch is quantified via a steerability score on a smaller set of images based on human-provided similarity scores. The difference in steerability scores on this smaller subset is not too large. This is promising, and improves confidence about the overall validity of the conclusions based on experiments with automatic scores.

4. The paper analyses the data to describe findings that may be of interest to researchers and practitioners working on human-AI interaction applications. Specifically, the study of steerability is quite relevant for creative AI applications.

### Weaknesses
1. Prompt engineering is now a topic of interest for people who wish to efficiently generate usable content from conditional generative models. My hypothesis is that, “Steerability”, i.e., the ease of generating the target image, depends on the amount of experience of the user. It would be great if the authors discuss how they might be able to decouple the influence of returning users who potentially have the ability to efficiently “steer” the generative model via better prompts.

2. Apart from the prompting experience, a person’s knowledge of the contents of the target image could also play a role in steerability. Especially in cases of a famous person, famous landmark, famous city, etc. There appear to be some person-specific confounding factors that affect steerability, which the paper doesn’t seem to address. It appears that the rationale for this is that, with a large enough population of users, such person-specific effects might be negligible. However, it would be nice if these confounding factors were explicitly identified and discussed.

3. “Image specificity” (Jas et al., CVPR 2014) measures the extent to which human captions that describe an image, varies across people. The observation that target images containing specific landmarks are more steerable than abstract images, appears to allude to a similar concept. Of course, the idea of steerability involves additional complexity of the generative model, and the human’s understanding of prompting. However, it seems possible that images with high “specificity” might lend themselves to be more steerable. It would be great to discuss this further.

4. The mismatch between human notions of similarity and the automatic metric makes the experimental setup suboptimal, and data a little more complicated to draw conclusions from. Please see “Questions” for specific concerns regarding the mismatch.

### Questions
1. Were there comments / feedback from users that elicited insight regarding their strategy? Specifically regarding the incongruity between human similarity notions and automatically computed similarity score? E.g., did certain persons try to maximise the automatic score while others maximised their own perception of similarity?

2. Was there an incentive for high score? E.g., additional reward? Do we know that people were taking the task “seriously”, and not just experimenting / exploring?

3. What is the score distribution between each generated image (and the target image) — that are generated from the same prompt? Is there any insight into the variance in matching score across different random seeds of the model (keeping the prompt constant)

4. “The intuition here is that t*1_i is more representative of the types of images we may expect given the fixed prompt, p*_i .” — the intuition here is unfortunately not clear to this reader. Could the authors please elaborate? Thanks!

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a dataset for understanding prompt tailoring in image generation. To collect the data, they introduced a game collecting 51k interactions across 2k papers, with a smaller group of paid users. The game is driven by two datasources AI Pompts and Wikipedia which they align using CLIP embeddings to select optimal plausible query images. From the game, they identify Markov chain approach to the steerability of user prompts. The authors envisage the dataset can be used to improve the outputs of image generation methods but also as a synthetic test setting using tailored NLP methods to test the response.

### Strengths
- Prompt engineering is a difficult problem to capture which the authors have proposed a method to achieve future analytical comparisons of methods.
- The dataset seems to be sufficient to capture user insights as the authors identify steerability is achievable.
- The use of multiple data sources to drive the method is good, especially as real world image captions do not contain the content description. However, the authors fail to quantify the performance, and they do not elaborate in the evaluation of the two sources.

### Weaknesses
 - It would be better to be clearer about the controlled collection earlier, simply paid and unpaid would avoid assumptions of how this was performed.
- The authors are missing a comparison of how true the distribution of generated images is to the original images as the Wikipedia captions in general don't describe the content so highly likely they do not match the original image. A quantitative evaluation of this is important otherwise it makes the choice of Wikipedia not relevant and does not increase validity over using any source.
- Authors should avoid re-using mathematical notation x_i changes through section 2. Although in general x is re-used in changing context throughout the paper.
- Lack of discussion on participant characteristics how was gender, race & ethnicity balanced? 
- Steerability contribution is well received, however, this would have more validity if was tested on a different model to confirm the insights, two versions of StableDiffusion provide limited insight.

### Questions
- How was bias addressed during data collection?
- How do the results on steerability differ between the two input datasets?
- Does the influence of unpaid/paid effect the outcomes?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This dataset studies how people interact with text-to-image models to generate desired target images. Particularly, during the data collection, the job of human is to iteratively re-fine the text prompt (only) to create a similar-looking image (to a given reference). Such a procedure traces the trajectory of human in making creative art using text-to-image model, and presents a unique sequential dataset for studying human-AI collaboration.

Then this paper perform analysis on the collected dataset, and find that user is able to discover a variety of text description that generates similar images, with the trajectory of user queries of similar diversity along the search. Then they propose a metric to quantify the steerability of AI, which is the expected number of interaction required to adequately complete a task.

### Strengths
- The paper is well presented, the motivation, data collection, experiments are clearly written. There is abundant details to understand the quality of the data, the distribution of user trajectory, the domain of data, etc.

### Weaknesses
 - It's unclear to me on how we could utilize the study done in this paper to improve research in text-to-image generation modeling, or Human AI interaction research. I saw some direction from the conclusion but those can be drawn without studying the research presented in this paper.

 - In the section about AI-generated images, it seems like from this seed selection procedure, you are only choosing the target image based on how easy it could be re-created using the prompt (and different random seeds). The criteria is not encouraging the aesthetic of the image, nor alignment between image and target prompts?

### Questions
- In the section about AI-generated images, it seems like from this seed selection procedure, you are only choosing the target image based on how easy it could be re-created using the prompt (and different random seeds). The criteria is not encouraging the aesthetic of the image, nor alignment between image and target prompts? 
- What is IRB approval?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to study how people write prompts for generating a target image with text-to-image models. The authors have collected the ArtWhisperer dataset that includes the different iterations of prompts a user tries out in generating the images, and from this dataset they have observed that different, diverse prompts can be used to generate an image. They also propose a metric for quantifying the steerability of the target image generation task.

### Strengths
* The paper addresses an interesting problem that has not been really investigated by other researchers in depth.
* The dataset will be made available to the public. To the best of my knowledge, no comparable dataset exists.
* The authors have followed responsible research practices (getting IRB approval, handling user data/privacy properly).
* The work is well written and easy to follow.
* The discussed future use cases including synthetic prompting and fully automated evaluation of t2i models would be relevant to many real-world applications.

### Weaknesses
 * The work does not investigate the behavior of users with malevolent intent (the authors acknowledge this), as their actions may not align with those of good actors. The users are assumed to be the latter (or at least, homogeneous in that respect), and the observations made in this paper are based upon that assumption.
* I would be interested to see more discussion/applications of how to take these noted observations of user behavior, steerability, and prompts and apply them to an existing problem. These insights could have possible implications for model training/evaluation in the future.
* There may have been returning users on a day-to-day basis, so it’s feasible that a user became more experienced with prompting over time, which would thus affect steerability. The authors however did not collect this type of data, so it’s not possible to observe this.

### Questions
1. Do the authors have any sense for how user behavior may differ with other t2i models? For example, does the quality of the model (i.e., its ability to generate high-quality imagery) affect the results?
2. Did the authors consider enabling users to adjust the model parameters (e.g. the seed)? This could potentially enable the user to generate an image that is even closer to the target, and could also be useful in future applications highlighted in the Discussion section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
