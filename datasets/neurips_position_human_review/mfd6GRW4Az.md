# Machine Unlearning Doesn't Do What You Think:  Lessons for Generative AI Policy and Research

- Decision: Accept (Oral)
- Scores: 4, 7, 7

## Abstract
"Machine unlearning" is a popular proposed solution for mitigating the existence of content in an AI model that is problematic for legal or moral reasons, including privacy, copyright, safety, and more. For example, unlearning is often invoked as a solution for removing the effects of specific information from a generative-AI model's parameters, e.g., a particular individual's personal data or the inclusion of copyrighted content in the model's training data. Unlearning is also proposed as a way to prevent a model from generating targeted types of information in its outputs, e.g., generations that closely resemble a particular individual's data or reflect the concept of "Spiderman." Both of these goals--the targeted removal of information from a model and the targeted suppression of information from a model's outputs--present various technical and substantive challenges. We provide a framework for ML researchers and policymakers to think rigorously about these challenges, identifying several mismatches between the goals of unlearning and feasible implementations. These mismatches explain why unlearning is not a general-purpose solution for circumscribing generative-AI model behavior in service of broader positive impact.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This paper proposes a position that the understanding of machine unlearning should be rectified in terms of the generative AI policy. The paper first revisits the two goals of machine unlearning: removal and suppression, and highlight they are very hard to achieve in general cases. Then the paper identifies several "mismatches" between the goal and the feasible implementations. The paper also studies this issue in US Copyright and finally gives some insights for ML research and AI policy.

### Strengths
This paper is clear and easy to follow. The discussion is accessible to broad readers that are not familiar with machine unlearning or even machine learning. This paper is based on strong case analysis, and deep understanding of generative AI policy. It's timely in the era of generative AI. I think it's quite insightful for decision making for government.

### Weaknesses
I have several concerns:

1. This paper may not catch many eyes in NeurIPS community, though it will be beneficial for AI policy makers. In my understanding, ML community cares more about technical issues for topics like machine unlearning, but this paper focuses more on the application-wise issues. I am not sure if ML community are willing to deliver a solid "application" or "system" for target information removal and suppression in real applications in real world, but I think this must be a minor focus among ML community.
2. I am not very convinced by the discussion of mismatches. The feasible implementation does not exist for the time being doesn't necessarily means the goal cannot be achieved. Instead, it shows there is much room for improvement.
3. To me (personally as a ML practitioner), it seems to lack deep or strong technical insights. The part of "Takeaways for ML research" doesn't bring me excitement, and I have an impression that those claims are just correct and easy to accept, but not impressive.
4. I think the paper should gives more references on misunderstanding of machine unlearning. Without such evidence, the critique risks addressing an unsubstantiated or "strawman" position.

### Questions
I don't have questions.

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The position paper discusses the complexities of machine unlearning presents an argument that there is a disconnect or mismatch between how unlearning works against the way it is claimed by people to be one of the solutions in addressing issues such as copyright infringement (as well as safety, privacy, etc) in modern generative AI models. The discussion centers around two aspects of unlearning namely targeted suppression and removal of information from the model. The authors emphasize that these two concepts are not interchangeable which may further confuse if propagated as a form of compliance with ongoing legislation related to removing/suppressing/filtering copyrighted content from AI models. To strengthen the support for the main argument, the authors structure the paper by discussing evolving motivations of machine unlearning, five main conceptual mismatches in the motivation of using unlearning against how it actually works, and further cover how said mismatches complicates its application using the US copyright law as a use case. The authors end the discussion with a set of takeaways targeted for both technical and policy people on how to move forward with machine unlearning as a form of method for compliance to policies.

### Strengths
The position paper has several key strengths that I appreciate:

First, I think overall topic and the authors position is an appropriate venue for the position paper track. Although I don’t work on unlearning, I’m particularly aware of the noise this field makes across discussions in social media platforms whether it actually works or not (to remove specific information or content from learning models). I believe this paper will introduce a more realistic viewpoint to the discussion in the ML community (if it has not already).

The paper presents a strong combination of perspectives on the technical and policy implications of machine unlearning gives a more balanced discussion on the authors’ position with unlearning. Given that government agencies around the world are rushing for drafting regulations and policies on protecting data privacy and intellectual property, I have a feeling this paper might be influential in their decisions, hence a solid reason to reserve a slot to be presented in conference.

To some extent, the paper is informative for people with basic knowledge of how AI works. You also don’t need to be an expert in policy to understand the nuances as these are all presented clearly in the paper.

### Weaknesses
The position of the paper could have been made more clear cut and direct (e.g., stating “Machine unlearning is inherently an insufficient method for meeting legal requirements in data protection and in removing data from an AI  model” or something more appropriate) rather than taking a more implicit angle from what I’m picking by how the authors discuss the arguments. Some readers might misinterpret the current challenges and uncertainties in the legal aspect discussed in the paper (e.g., copyright infringement) as something that confounds the direction of machine unlearning research, hence might say the position of the paper is also unclear/uncertain/highly dependent on legal interpretation. Thus, I think there is a need for a stronger articulation of the position.

I would like to see better framing of alternative views discussing where machine learning may potentially serve as the sole or main solution to certain problems (e.g., forcing models to unlearn illegal content such as sexual content involving a minor). While I do get the importance of emphasizing and supporting the position, a more balanced discussion on the alternative views is needed for the paper.

### Questions
While unlearning research will continue to progress, we are doubtful that full compliance will be achieved in the future. → Is this an assumption that unlearning should always be used in complement or on top of other methods for removing/analyzing presence of targeted content? I’m quite confused by this statement.

In what specific edge cases is machine unlearning a feasible solution to be used alone? Or is this applicable only if it’s not towards compliance to legal requirements?

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
The paper is a wake up call about control of information in the AI era, and how society at large (mainly policymakers and courts) has to manage it.

The position of the paper is that UNlearning in AI models does not work as policymakers expect, and that the term UNlearning is measleading at this stage of AI development. 

Authors describe why unlearning is needed (Sec. 2), how it is currently implemented (Sec. 3), current limitations of such implementations (Section 4), impact on US Copyright law (as an example, Sec. 5). The paper ends with Sec. 6: recommendations on how policymakers should adjust their expectations.  

The main techniques for AI unlearning are "targeted removal" and "targeted suppression". Authors address both of them in different scenarios and stress 5 "unsolvable" mistmatches between unlearning Motivations and Methods (listed in Sec. 4).  

Their example on US-copyright law shows that there are no general-purpose solutions to constrain generative AI models and that the certainty of erasure/removal is unattainable, as AI models are inherently probabilistic. Policymakers should be warned of limitations (and costs) of using unlearning methods for compliance.

### Strengths
The paper raises a relevant issue in AI: how can we remove information from an AI model. 

The analysis is detailed and clear on the technical and practical aspects barring a full compliance  to a removal order. 

It is definitely targeting the attention of policymakers, lawyers, and judges, as it is educating them on the randomness of AI. This is a huge problem in itself, as expectations among that set of professionals are more clear cut, they have to answer questions such as "is a given event a copyright infringement or not?".

### Weaknesses
In some sense, AI models may be interpreted as tools in the hands of users, like a knife or a gun. Following up with this approach, it would seem natural to discuss how can we elaborate a set of social rules on how to use AI in a legal setting. Should we have a "certification" process for AI models, with warning labels? 
Even though, this is not the core of the position paper, I think this part of the discussion is missing.

### Questions
I have a provocative one: why do policymakers have such great expectations on the unlearning capacity of AI models?
Should we ask the AI model whether the accurrence is indeed copyright violation?

### Presentation
4
