# The other you in black mirror: first steps from chatbots to personalized LLM clones

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable abilities in a wide
variety of generic tasks. Here we investigate whether it is possible to use LLMs
to partially replicate cognitive aspects of an individual by fine-tuning an LLM
with personal data. Our model, A-clone, built on the pretrained Llama3-70B, was
fine-tuned with a private English dataset from one volunteer referred to as A throughout. We
evaluated A-clone in two ways. First, using 701 open-ended questions, we gathered
responses from A, A-clone, other LLMs, and A’s family members imitating A.
We conducted a Turing-like test where 31 participants with varying degrees of
familiarity with A attempted to identify A’s real answers in a question-and-answer
task. Human participants identified the genuine responses from A 55% ± 7%
of the time, just over chance levels. A-clone outperformed all other baselines
in mimicking adequate responses from A. Second, we compared the outputs
of A-Clone with the ground truth from A in 10 psychological, moral, career,
political tendency, and general knowledge tests, containing 484 questions altogether.
A-Clone demonstrated a strong correlation with A’s responses. This work provides
an initial, proof-of-principle, evaluation of the possibility of mimicking the
responses of an individual, opening doors to many real-world applications but
also raising potential privacy and safety concerns about digital clones. The code
and data can be found in this link.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The researchers behind this paper developed an LLM model called A-clone, which is built on pretrained LLMs and further fine-tuned with a private dataset from a single volunteer referred to as A, without applying any anonymization techniques. They utilized the pretrained model Llama3-70B, combining fine-tuning with QLoRA. It is important to note that they conducted the experiments using prompts without modifying the model's architecture. The model was evaluated in two ways. First, they gathered responses from A, A-clone, other LLMs, and A's family members attempting to mimic A. A Turing-like test was conducted with 31 participants, who had varying degrees of familiarity with A, to determine if they could correctly identify A's genuine answers in a Q&A task. The participants correctly identified A's real responses 55\% ± 7\% of the time, which is just above chance. A-clone outperformed all other baselines in replicating A's responses. In the second evaluation, they compared A-clone's answers to A's across 10 tests covering topics such as psychology, morality, career, political views, and general knowledge, consisting of a total of 484 questions. A-clone's answers demonstrated a high level of agreement with A's responses.

### Strengths
To the best of my knowledge, the main strength of this work is that it uses real email data spanning a 20-year period from a single individual. This provides a strong foundation for developing a realistic personalized LLM.

### Weaknesses
 I noticed some errors in the presentation of the text, as well as certain aspects of the experimental stage that could have been improved. While the work has a solid foundation, I feel that both the presentation and the development of the experiments were somewhat rushed. Below, I will outline the specific points I identified. I should also mention that the methodology and the creation of the model, called A-clone, do not appear particularly unique to me. The novelty of this work seems to derive primarily from the data, which could potentially impact the model's quality. In the related works section, you mention several papers that, in my opinion, could have influenced and improved your experimental setup. However, it seems that these works were not utilized. It gives the impression that you referenced these papers more for citation purposes than to fully understand them and build upon their ideas.

  A) Presentation
    
  A1) While it is clear from reading the text that your data are in English, this should be explicitly mentioned in both the abstract and the introduction.
    
  A2) Typos
    
  A2.1) Since you used the abbreviation LLM for Large Language Models (see line 034), you should consistently use this abbreviation throughout the text. Therefore, please revise the text in lines 081, 092, 113, 159, 427, 488, and others.
    
  A2.2) The same applies to the abbreviation Supervised Fine-tuning (see line 112). Please correct the term on line 125.
    
  A2.3) In several instances, you did not correctly apply spaces, particularly near references. Please review and correct this in lines 083, 088, 089, 098, 099, 101, 102, 204, 209, 248, and so on.

  A3) As mentioned in the author guidelines (see https://iclr.cc/Conferences/2025/AuthorGuide), you are encouraged to include a Reproducibility Statement at the end of the main text. This statement should detail the efforts made to ensure reproducibility and include any necessary information for those wishing to replicate your results.
    
  B) Experimental
    
  B1) In the introduction (lines 042-046), you mention that A-clone is fine-tuned exclusively with private personal data from a typical individual, but you do not mention whether you obtained permission to use that data. Additionally, I did not find any statement from this individual indicating their approval for the use of their data.
    
  B2) Admittedly, your experiment is quite interesting, as I have not come across any similar studies in the literature that involve email data collected over a 20-year period from a single user. However, I believe the experiment is limited by the small number of users you selected. While it may be relatively straightforward to clone the characteristics of a single user from an LLM, if your experiment had involved two or more users, it would be harder to guarantee that the approach is effective. In practice, such a tool should be tested on large datasets from various users. This is where an LLM’s capability to distinguish individual characteristics would be most valuable, and generally distinguish if this model overfits the data or really understands the character of a person.


  B3) Regarding the anonymization of the data, you mention in lines 104-107 that in most cases, the data are anonymized and difficult to trace, which is why you chose not to apply any anonymization technique. However, in my view, anonymization is essential to protect the privacy of the data, especially in your case, where the data span a 20-year period. Failing to implement anonymization could encourage both the academic community and the industry to overlook this crucial aspect of user privacy.
    
  B4) Another point I raised concerns the questions you asked the LLM and compared to the ground truth of person A. It’s important to examine the distribution of topics in these questions. For example, in the paper "Does GPT-4 pass the Turing test?" by Cameron R. Jones and Benjamin K. Bergen (2024), which you reference, the authors use a variety of question types, ranging from personal information to general knowledge. This approach helps determine whether the LLM truly understands the personality and behavior of the person or simply overfits to their data. In the same paper, authors gave an option to tester volunteers to explain why they believed a certain response was generated by an AI, which could provide you with further insights into the quality of your model. You mention in lines 137-148 that you use a variety of questions to cover a wide range of topics. Please add a plot that shows the distribution of questions topics to wrong/correct response prediction of tester volunteers.

  B5) Related Works Section
    
  B5.1) In general, it seems that many papers can be added since personalized LLMs are a broad topic. For instance, regarding the Turing test, if you refer to the paper 'Cameron R. Jones and Benjamin K. Bergen. Does gpt-4 pass the turing test?, 2024.' you mentioned, there is much richer literature that explains what it entails. I believe it would be beneficial to include a brief paragraph explaining the Turing test and suggesting additional papers for readers who want more detailed information.
    
  B5.2) It would be helpful to include a paragraph in the related works section discussing the application of personalized LLMs. Additionally, you could mention potential applications of your model in the introduction to provide more context for its relevance.
    
  B5.3) To the best of my knowledge, it seems you have omitted some recent papers related to personalized LLMs that would be valuable to include in the related works section. Examples include "Leveraging LLM Reasoning Enhances Personalized Recommender Systems" (Tsai et al.), "How Good are LLMs in Generating Personalized Advertisements?" (Meguellati et al.), and "Doing Personal LAPS: LLM-Augmented Dialogue Construction for Personalized Multi-Session Conversational Search" (Joko et al.).
    
  B5.4) In the introduction, it would be useful to mention the most relevant works related to your paper and clearly state what distinguishes your work from others in the field.

### Questions
The questions I present in this section are closely related to the Weaknesses section where I share my thoughts, so please review both parts.
    
 1) In lines 201-2023, you mention that the responses generated by the LLM in the first prompt were quite long and easily detected and that you later adjusted the length. Have you tried examining the correlation between person A's ground truth responses and A-clone's responses? For example, you could use metrics such as ROUGE-1, ROUGE-L, Persona F1, and Win rate, as suggested in the paper you referenced, "Kai Zhang, Lizhi Qing, Yangyang Kang, and Xiaozhong Liu. Personalized LLM Response Generation with Parameterized Memory Injection" (2024).
    
  2) In lines 198-200, you state that, based on the questions you provided to A and A-clone, the test volunteers (such as A's family) had to predict which response belonged to A. Why didn’t you ask the test volunteers to come up with a set of questions they wanted to test, and then have both A and A-clone respond to those questions, incorporating them into the evaluation process? For example, in the paper you referenced, "Daniel Jannai, Amos Meron, Barak Lenz, Yoav Levine, and Yoav Shoham. Human or Not? A Gamified Approach to the Turing Test" (2023), they describe strategies that helped participants identify whether they were interacting with a chatbot or a human. Having such information for your model would provide deeper insights into its abilities.
    
  3) In lines 203-208, you mention that you applied an SVM to determine if person A’s responses were easily recognized based only on length, with an accuracy of 0.48. Have you considered using a state-of-the-art classification model? In my opinion, this accuracy doesn’t provide much information, given that you used a simple classifier like SVM.
    
  4) In line 770, regarding Table 2, you present some statistics related to the experiment. Did you perform any correlation tests to identify trends between the variables (e.g., gender, age range, etc.) and the test volunteers’ responses? For instance, it’s possible that individuals with a PhD level of education might be better at discerning whether something was generated by an AI.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates whether an LLM can replicate an individual's language style by learning from that person's language corpus, which is an interesting topic. The authors trained an LLM called "A-clone" using a corpus collected from an individual referred to as A. They designed a series of experiments, including Turing-like tests and psychological assessments, to gather responses from both A and A-clone. Thirty-one participants, each with varying degrees of familiarity with A, were asked to differentiate between the responses of A and A-clone. The study concluded that A-clone's responses showed a strong correlation with those of A.

### Strengths
1. The topic of this paper is fascinating and important, focusing on whether an LLM can learn a person’s tone, memory, personality, values, and perspective.
2. The experimental design, which involved 31 participants with varying levels of familiarity with A to distinguish between the responses of A and A-clone, is also good.

### Weaknesses
Although the current experimental setup produces interesting results, it is limited in fully supporting the paper's claims. Since the model is trained only on corpus A, it's unclear if the findings apply beyond this single individual. Expanding the experiments to include language data from other individuals and training corresponding LLM clones would strengthen the conclusions. Without this, as the authors note, the results remain preliminary. A broader evaluation would provide stronger evidence for the LLM’s ability to mimic individual language styles more generally.

Specifically, the lack of diversity in the training data raises concerns about the model's ability to generalize. The model might be overfitting to the specific linguistic patterns of individual A, and it is unclear how well it would perform with individuals who have different linguistic styles, backgrounds, or levels of expressiveness. The current evaluation also does not explore the model's robustness to variations in input, such as different question types or phrasing. These limitations restrict the scope of the conclusions that can be drawn from this study.

### Questions
1. What is the source of the 701 Turing test questions? Could you provide background information on how these questions were collected?
2. The distribution of the 28 participants appears unbalanced, particularly concerning the 'Relationship Category.' The proportion of 'family' participants is too low. Additionally, having only 'stranger' and 'academic' categories, aside from 'family,' seems unreasonable.
3. Could Figure 2’s confusion matrix be presented such that the sum of all cells equals 1?

### Soundness
2

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
4

### Summary
The paper studies the current capabilities of a LLM to mimic a human individual after it has been finetuned on a set of personal data. In particular, Llama3-70B, finetuned on 38000 Q&A pairs extracted from e-mails, is evaluated on its answers to ~700 questions as well as a wide range of personality tests. The study finds that humans (n=31) with varying degrees of knowledge about the mimicked individual in a (static) Turing test setup have difficulty distinguishing between the LLM and the answers given by the mimicked individual.

### Strengths
- The problem is interesting and relevant. The idea of mimicking an individual via an LLM that is finetuned on personal data is also a realistic threat. Already, LLM-based applications are heavily used by nefarious actors to trick people (scam mails, telecalls, etc.)
- The setup of the human study seems sensible and contains a wide variety of sanity checks (whether individuals are aware, questions to test for basic LLM answers such as the LLM giving code)
- Baselines are overall sensible. However, it is unclear to the reviewer how to interpret the "followed by the relevant book chapter" in the GPT-4o baseline. The description before sounded like this is static. However, this sounds like it could be query-specific. If it is not dynamic, it might be interesting to have this as a new baseline that tries only to pull out the most relevant information for the Q/A set or book to answer the respective question (as done in RAGs).
- Results show that humans have difficulty detecting the real human across both tests (and include relevant standard deviations and overall certainties). The split of the two different types of tests is interesting, and the split by familiarity was generally a useful ablation (see points given below).

### Weaknesses
 - The actual data used is somewhat unclear. I understand from a data privacy perspective why information about the used data is limited but 38000 Q&A pairs from e-mails is an insufficient description to understand the data distribution. It would be nice to have at least a length / rough topic distribution to make more sense of the data. Additionally this could help relating the content that the LLM was trained on to the questions asked in the tests.
- I would not consider 20 years of e-mail data from one individual as a "small" dataset (for this particular task). It would make sense to here ablate over how much data is needed for the LLM to "mimic" well enough as this significantly impacts the applicability of such a threat.
- In the reviewer's opinion, this submission would strongly benefit from a dedicated ethics section. In particular, it is unclear whether people sending mails to $\mathcal{A}$ are aware of their data being used for finetuning a language model (which, depending on jurisdiction, can be an issue). Further, a more detailed discussion of the points at the bottom of page 9 can be found here.
- The personality test results could be explained/contextualized further. Notably, to me, it seems like that while the human tests (e.g., Fig. 5) strongly prefer $\mathcal{A}-clone$, o1 with a basic ICL setup previously used for GPT-4o, significantly outperforms $\mathcal{A}$ across almost all categories - this discrepancy in performance seems unexplained in the work so far. Could this be due to different question setups or human judgment not being directly aligned with questions in such personality tests?
- As the paper acknowledges, the Turing test is static, and several of the questions are quite general in nature (e.g., "Does AI represent a major threat to humanity?"). One thing that would benefit the study here is to cluster questions into more fine-grained groups, e.g., (1) Does the LLM actually perform transfer learning by being able to trick people on questions where no samples have been in the training data /but rather it extrapolated personal traits of the individual) (2) Does it perform better on more subject-oriented questions or more personal questions, etc? This would probably also strengthen the familiarity with $\mathcal{A}$ ablation, where one would expect to see stronger trends within certain subcategories.

### Questions
- Could the authors provide more details on the training data?
- Could the authors further describe the results on the personality tests?
- Could the authors give more details about question distributions in the Turing tests?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores creating and evaluating "A-clone", a personalized large language model designed to mimic a specific individual's responses. The authors fine-tune Llama3-70B using a private dataset of emails and interviews from the individual. They evaluate A-clone through Turing-like tests with human participants and comparisons with psychological test responses. Evaluators struggle to distinguish between A-clone and the actual individual, outperforming other baselines. Psychological tests show strong correlations between A-clone's responses and the individual's. The paper provides a proof-of-concept for a personalized LLM while highlighting the importance of addressing associated risks and ethical considerations.

### Strengths
- The paper convincingly evaluates A-clone, demonstrating that it responds very similarly to the individual.
- Real human evaluators used, with a variety of familiarities with A.
- Good set of baselines: compares A-clone not only to other LLMs (GPT-4o, Llama3-Instruct) but also to responses from the individual's family members.

### Weaknesses
 - A significant existing body of works exists looking at tuning models to emulate particular characters or personas such as Li et al, 2023 (https://arxiv.org/abs/2308.09597) and Zhou et al, 2023 (https://arxiv.org/abs/2311.16832).
- The fine-tuning techniques used are not interesting or novel. 
- The authors do not attempt fine-tuning other models besides Llama 3 70B.
- The authors do not describe a process for generating or selecting the evaluations questions that ensures they are distinct from the email and interview data used for training.

### Questions
- What criteria did you use to select the open-ended questions for the Turing-like tests?
- How did you ensure there was no data leakage between the training set and the evaluation questions? Did you use any methods to check for similarity or overlap between the training and evaluation datasets?

### Soundness
3

### Presentation
3

### Contribution
2
