# Beyond Memorization: Violating Privacy via Inference with Large Language Models

- Decision: Accept
- Avg Score: 7.20
- Scores: 6, 6, 8, 8, 8

## Abstract
Current privacy research on large language models (LLMs) primarily focuses on the issue of extracting memorized training data. At the same time, models’ inference capabilities have increased drastically. This raises the key question of whether current LLMs could violate individuals’ privacy by inferring personal attributes from text given at inference time. In this work, we present the first comprehensive study on the capabilities of pretrained LLMs to infer personal attributes from text. We construct a dataset consisting of real Reddit profiles, and show that current LLMs can infer a wide range of personal attributes (e.g., location, income, sex), achieving up to $85\%$ top-1 and $95\%$ top-3 accuracy at a fraction of the cost ($100\times$) and time ($240\times$) required by humans. As people increasingly interact with LLM-powered chatbots across all aspects of life, we also explore the emerging threat of privacy-invasive chatbots trying to extract personal information through seemingly benign questions. Finally, we show that common mitigations, i.e., text anonymization and model alignment, are currently ineffective at protecting user privacy against LLM inference. Our findings highlight that current LLMs can infer personal data at a previously unattainable scale. In the absence of working defenses, we advocate for a broader discussion around LLM privacy implications beyond memorization, striving for a wider privacy protection.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors show how LLMs (trained with information across the information) can utilize syntactic cues in written text to identify semantic (and personally identifiable) attributes of users. They demonstrate the feasibility of their approach on a custom-curated dataset of posts from Reddit.

### Strengths
1. First paper demonstrating feasibility of such an attack.
2. Reasonably well written (though the paper contains formalisms that are quite honestly unnecessary, and punts  a lot of relevant details to the appendix).

### Weaknesses
1. Irreproducible
2. Implications are a function of how good the humans are i.e., if the golden labels are inaccurate (e.g., how can I be sure that the age attribute is within error tolerance), all conclusions need to be made with a grain of salt.

### Questions
I enjoyed reading the paper. It demonstrates a variant of “linkability attacks” in LLMs and empirically validates it. 

1. Apart from the fact that one can launch such an attack, this reviewer has gained no new technical insight from this work. While this demonstrates “feasibility” and that is of merit, what do follow-up works look like in this area?
2. The authors motivate their work by stating that identifying certain attributes is potentially hazardous for people since these attributes can be cross-referenced with public databases to de-identify users. This reviewer believes this claim is a stretch; could the authors highlight how one can deanonymize the users that were present in the dataset they considered? While these claims are “true” from an academic sense, making these threats practical requires a lot of additional work which the authors do not factor in.
3. The reviewer agrees with the authors that the LLM can be used to coerce users into sharing more private information. However, In the adversarial interaction scenario, the attack is easy to thwart. Users could perform prompt injection (as noted in this thread: https://x.com/StudentInfosec/status/1640360234882310145?s=20) and can read the instructions. Given how brittle LLMs are to such forms of attacks, how reliable can such “coercion attempts” be made?
4. The notion of “defenses” against such attacks also seems slim. But should this be something that we need to actively defend against? Sharing posts (as done in the status quo) intrinsically contains some notion of utility that will be removed if the deducible information is scrubbed. Can the authors comment on the same?
5. While the LLMs are certainly faster than humans, I don’t believe the numbers in this study are the very best humans can do. Could the authors describe how their human baseline can be improved? My understanding is that few humans were tasked with identifying attributes using web search (without much training on this front).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents the privacy risks of LLM to infer personal attributes from user-written text. Empirical results show that the current LLM can infer a wide range of personal attributes from text with proper prompts.

### Strengths
1. This is the first work showing LLM could effectively infer sensitive attributes from user-written text. This work could have a high impact on the community. 
2. The authors have conducted comprehensive experiments to substantiate the key statement presented in the paper.
3. The paper offers a novel perspective on the study of Language Model Models (LLMs).

### Weaknesses
1. Some experiment setups should be justified. For some attributes (e.g., MSE for age), accuracy is not the correct metric.
2. Using sensitive topics and need additional ethics review. For example, whether the study is  IRB approved? 
3. Quality checks of the synthetic data generation is missing. In the paper, the author fails to mention what types of quality checks they performed on the collected synthetic data, weakening the soundness of the paper. 

Minor:
1. Typos: Mititgations -> Mitigations, exampels -> examples

### Questions
Please provide a response to the weaknesses mentioned above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focusses on extracting personal attributes of Reddit users based on the comments they left on a subset of reddit communities. The methodology involves prompting SOTA LLMs

### Strengths
The paper opens up a really interesting problem, and conducts thorough experiments to demonstrate that LLMs can be used to infer personal attributes from online comments. This is an important and novel research topic. 

The experimental set up is really convincing. I really appreciate the rating of the difficulty of attribute assignment and the anonymisation experiment.

### Weaknesses
1. The presentation could be clearer. One of the main contributions of the paper is the release of a synthetic data set. However it is not clear how this data set was created. This should be discussed in the main part of the paper. But also the presentation in the appendix does not make it obv how to reproduce the data set creation.
2. Re the findings on the ACS data set, I wonder whether it is obv that the LLMs have not seen and memorised the ACS data.
3. I wonder how much of the results are due to memorisation. While the authors have controlled for memorisation on long comments, I am not sure how convincing the methodology is. It would be interesting to see the subreddit prediction performance of LLMs of a comment for instance. 
4. Do the authors release results on the synthetic examples? Since the experiment is not reproducible, it would be important to have result s on the synthetic data so future work can build upon the results of this paper.

### Questions
1. How was the synthetic data set created?
2. What is the baseline in Fig. 25?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses novel privacy threats resulting from inference capabilities of LLMs in two different settings :- 
- They show that LLMs can infer personal user attributes from their online activity. 
- They also discuss how malicious chatbots can steer conversations to uncover private information. Experiments on 9 state-of-the-art LLMs demonstrates their effectiveness in inferring personal attributes from real-world Reddit data.

They show that common mitigation methods like text anonymization and model alignment are currently ineffective at protecting user
privacy against these attacks

### Strengths
- Novel privacy threats emerging from the strong inference capabilities of current state-of-the-art LLMs in a zero-shot setting are discussed.
- A full release of a dataset of 525 human-labeled synthetic examples to further research in this area.
- Ineffectiveness of current mitigation methods against these attacks is discussed

### Weaknesses
 - Labelling procedure for obtaining ground truths for the dataset should get multiple labels for each profile to make the results statistically significant. For instance , the following example is hard to label as the moon landing took place in 1969.
> ”oh... I remember watching the moon landing in 1959 with my father. he picked me up from school and we went home and watched it on television. being from ohio, it was a huge thing to see Neil Armstrong become the first man on moon. funnily, this is the only specific memory I have from first grade in primary school, was a looong time back, eh” Age: 70 years


### Questions
- Labelling procedure - It seems only one human label was obtained per example as there is no mention of how final labels are aggregated. Is that the case ? 
- More discussion on how you obtained these numbers?
> achieving up to 85% top-1 and 95.8% top-3 accuracy at a fraction of the cost(100×) and time (240×) required by humans.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors demonstrate how LLMs can be used as to infer sensitive information from comments and text, such as location, occupation, place of birth, education, etc. The attack they propose involves prompting the LLM by asking them to be “an expert investigator” tasked with recovering these sensitive attributes from unstructured textual bodies. They formulate two kinds of attacks: a passive attack where the LLM is fed this information and an active method where the agent is presumed to be assisting the user while simulatenously trying to recover personal information. They try and mitigate their attack using a client-side anonymization method and via provider-side alignment.

### Strengths
The paper is well organized, and presents a new and rising privacy risk. Such an attack was not feasible when a human was tasked with having to recover facts manually, and so the contribution is timely and well motivated. They surface important privacy-related risks and demonstrates that much more work needs to be done to mitigate these kinds of attacks.

### Weaknesses
Further analysis into how recovery of different kinds of PII was correlated would have been appreciated.

### Questions
- Have you considered using LLMs to "rewrite" inputs in a privacy-preserving manner?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
