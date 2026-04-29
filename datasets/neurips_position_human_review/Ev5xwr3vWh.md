# Stop the Nonconsensual Use of Nude Images in Research

- Decision: Accept (Oral)
- Scores: 5, 9, 7

## Abstract
In order to train, test, and evaluate nudity detection models, machine learning researchers typically rely on nude images scraped from the Internet. Our research finds that this content is collected and, in some cases, subsequently \emph{distributed} by researchers without consent, leading to potential misuse and exacerbating harm against the subjects depicted. \textbf{This position paper argues that the distribution of nonconsensually collected nude images by researchers perpetuates image-based sexual abuse and that the machine learning community should stop the nonconsensual use of nude images in research.} To characterize the scope and nature of this problem, we conducted a systematic review of papers published in computing venues that collect and use nude images. Our results paint a grim reality: norms around the usage of nude images are sparse, leading to a litany of problematic practices like distributing and publishing nude images with uncensored faces, and intentionally collecting and sharing abusive content. We conclude with a call-to-action for publishing venues and a vision for research in nudity detection that balances user agency with concrete research objectives.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper argues that the ML community should stop the nonconsensual use of nude images in research, as it constitutes a form of image-based sexual abuse. The authors systematically reviews 155 publications and find that researchers routinely scrape, share, and distribute millions of nude images without the subjects' consent. To fix the problem, the authors advocate for a ban on publication of papers which utilize these datasets, as well as a participatory data-trust model.

### Strengths
1. The authors conduct a fairly thorough meta-analysis of prior works which utilize nude images.

2. The paper outlines concrete and actionable next steps to fix the problem -- a venue ban, synthetic data, and a new model for data governance.

3. The paper is generally well-written and easy to understand.

### Weaknesses
The authors do not sufficiently make a distinction between the origin and type of nude images that may exist: (1) CSAM, (2) images originally created and distributed in a non-consensual way (e.g. upskirting), (3) images created and publicly distributed in a consensual way (e.g. Onlyfans, Pornhub, some Reddit forums), but where researchers have not obtained proper license for their use, (4) images created and distributed in a consensual way, and which have been licensed for ML models (e.g. a company licensing data from Reddit, or professional performers releasing content under permissive licences). To my understanding, possession of (1) is certainly illegal in all jurisdictions, possession of (2) is illegal in many jurisdictions, (3) is a matter of copyright law. These are certainly objectionable. However, I do not see an issue with the use of (4). It does not appear that the authors have distinguished between these categories in their meta-analysis.

The authors focus most of their attention on dedicated nudity datasets, but the presence of nudity in large general multimodal datasets like LAION, which have much higher impact, and what should be done about it, is limited.

The authors have not included an alternative views section.

### Questions
1. What should be done about the datasets that have already been collected and which are public online?

2. What is the scope of the proposed venue ban? For example, LAION-5B has been found to contain CSAM. Should we ban this dataset (or similar) from being published? Should we ban papers which propose a new vision-language model which use this dataset for pre-training? Should we ban any papers which use OpenCLIP?

3. How do you handle images legally distributed under permissive licenses which allow for ML training?

4. The authors mention that "Studies on other social media platforms have found that users are largely unaware that their “public” posts could be used for research". If these users agreed to license their images for research when signing up for the website, shouldn't the onus be on either the users to understand what they're signing up for, or the social media company to make their policies clearer? Why does the ML researcher have to obtain consent again from these users, which is not at all scalable?

5. The major ML conferences (e.g. NeurIPS, ICML, ICLR) all have the ability for reviewers to request ethics reviews. Do you think this mechanism is sufficient to mitigate the publication of these works?

### Presentation
3

---

## Human Reviewer 2

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
This paper argues for stopping the use of non-consensual nude images in machine learning. First, the paper shows that a certain subset of the research community does engage in this practice through both usage and distribution of such images. Additionally, the paper argues that the potential upsides of such work does not outweigh the serious breaches of consent and it calls for stronger action by publishing venues to curb these practices.

### Strengths
1) Tackles an important but often overlooked aspect of ML research 

2) The arguments are on the whole quite well supported by evidence

### Weaknesses
I wouldn’t call it a weakness per se, but I’m not sure about the claim in the paper that GenAI is less harmful. Often to train the GenAI models, such images need to exist in the dataset and I’m sure some of sexually explicit images are indeed collected and trained on non-consensually. Further, since such models can leak training data and are simultaneously quite good at compositional semantics they can create versions of the likeness of people in various scenarios that the person may not consent to even _if_ they have given consent to use the original image. It would be great if the authors could discuss these situations further.

### Questions
See weaknesses

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper argues for the stopping of nonconsensual use of nude images when training machine learning models to detect nude images (possibly in online settings). The paper is a systematic review of collected works in the ML literature that make advances on this task, with the reviews focused on whether they address the issue of privacy in using nude images available online/image-based sexual assault.  

The paper summarizes collection and distribution practices, arguing that current approaches to curate nude images for ML research is inherently IBSA, and that the content being collected itself engages in IBSA. The paper also presents a position on various ethics research considerations that authors should consider when conducting studies in this realm.

Finally, the paper calls for a new model of data governance and generating data; namely, they authors argue that researchers should take care to verify that nude images produced by GenAI tools do not resemble nude images of real people in the training data. Authors also argue to lean into people's willingness to share sensitive data under a guarantee of privacy to reach the same objectives, instead of relying on publicly available data, which they argue perpetrates harm.

### Strengths
This paper is extremely thorough. The methodology of assessing the ML literature on use of publicly available nude images is well done. I thought the data collection and distribution practices brought this systematic review together, highlighting the potential issues with using publicly available nude images. The methods were clearly defined, and the discussion was appropriate.

### Weaknesses
I thought the one major flaw was that there was minimal, if any, consideration of alternative viewpoints. One simple alternative viewpoint may be a more nuanced take -- that certain nude images available on the internet are indeed ``fair game,'' as there is almost surely consent from the person whose nude images they are.

### Questions
I am curious if you considered introducing nuance into the evaluation of different sources of nude images (i.e. whether there is a high probability the nude image is meant for ad hoc distribution and that using it in ML research is alright).

### Presentation
3
