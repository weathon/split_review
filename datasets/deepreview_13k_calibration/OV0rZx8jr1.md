# Debiasing Online Preference Learning via Preference Feature Preservation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
While various preferred features determine human preferences, current preference learning frameworks for large language models (LLMs) simplify them with binary pairwise comparisons and scalar rewards. This simplification could make LLMs' responses biased to mostly preferred features such as longer responses which would be exacerbated in online learning scenarios as the biases can be accumulate continuously throughout the iterations.
To address these challenges, we propose a novel framework called PFP (Preference Feature Preservation).  The key idea of PFP is maintaining the distribution of human preference features throughout the online preference learning process. Specifically, PFP first trains a feature classifier using the existing offline pairwise human preference data. 
Then, using this classifier and the distribution preserving optimization, PFP maps appropriate preference features for each input instruction during online learning. 
Lastly, PFP trains LLM using the existing preference learning framework, by incorporating the preference feature of each data into system prompts and enabling LLM to explicitly handle various human preferences. Our experiments demonstrate that PFP successfully mitigates the bias in preference features that arise during online learning, and achieves superior performance compared to previous preference learning methods on general benchmarks including AlpacaEval 2.0 and MT-Bench. We also observe that PFP almost resolves a length bias issue, a long-standing problem of online preference learning, even though it was not specifically designed to tackle this.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the bias problem as the online preference alignment takes place. The paper is motivated by the bias towards lengthy responses and proposes a system-prompt engineering-based solution. Since system prompts can be combinatorial explosive space, they only try to learn certain attributes (tone, informativeness, etc) and subattributes within them. This makes every instruction and response pair a function of 5 sub-attributes in total. Now, given the input and attribute data, they learn a mapping, which predicts the attributes that can lead to favoring certain responses. 

Having learned this distribution, to create a new dataset for alignment, they first calibrate it with the prior distribution (average distribution over these attributes) for the given training data. Followed by calibration, they generate the new system prompts and then align the model. 

Several ablation studies are conducted to show the efficacy of the proposed method.

### Strengths
I like the number of ablations that are being performed, and the comparison with other length-controlled generation-based baselines. The experimental setup seems to be complete.

### Weaknesses
- Notations in this paper can be heavily improved, in particular for the FE part. I think one should use vector notation for the label space, and simplex to denote output of the FE network. 
- I am still not fully sure about the motivation of this work. Can authors highlight cases where certain reward models prefer lengthy responses despite having incorrect answers? In my belief, as long as the answer is correct, and if the system prompt doesn't have instruction to be precise (succinct), then there is nothing wrong in long generations (other than the computation aspect)
- How is length-controlled generation done? 
- Why should SELFEE work? To my understanding, it is some sort of pseudo-labeling based on its current state. If the model is not good enough to begin with, then wouldn't it exacerbate the biases (or if it is incorrect for certain prompts)?
- I am not sure why the output adjustment is needed. Can authors perform a study showing its use? 
- In Fig 4, why is it bad that the distribution for the preference feature is changing (that is KL divergence increasing). I am not fully sure why should that be linked with longer-generation
- Can authors run an experiment that just adds "being concise" in the system prompt, as another baseline?

### Questions
Refer to the weakness.

Post rebuttal: I’m increasing my scores.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel framework, PFP (Preference Feature Preservation), aimed at mitigating biases that arise in the preference learning process of LLMs.

### Strengths
The paper introduces a unique approach, Preference Feature Preservation (PFP), for managing bias in preference learning. By explicitly incorporating preference features in the system prompts and maintaining feature distribution, it provides a fresh angle on bias mitigation that has not been explored in existing work.

### Weaknesses
The paper introduces a set of predefined preference features, categorizing them into five distinct classes, which provides a structured framework for evaluating human preferences in various dimensions. However, in the main results, the experiments appear to primarily focus on addressing the length bias issue, leaving it unclear whether similar attention was given to the other identified preference classes. Were any experiments conducted to examine these additional preference aspects?

Furthermore, the evaluation results, including those from AlpacaEval and MT-Bench, rely on GPT-4 as the evaluator. This raises a question about the potential variability in the results due to using GPT-4 for evaluation, particularly since its responses can introduce variance. For the results shown in the paper, i didn't see the significant improvement compared with other baselines, only 1%~2% difference for AlpacaEval, pretty close for MT-Bench.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel framework, PFP (Preference Feature Preservation), which addresses the issue of bias in large language models (LLMs) during online preference learning. The core content revolves around the innovative approach of maintaining the distribution of human preference features throughout the online learning process. This is achieved by training a feature classifier on existing offline pairwise human preference data, mapping appropriate preference features for each input instruction during online learning, and incorporating these features into system prompts for LLM training. The experiments indicate that PFP successfully mitigates bias in preference features and outperforms previous methods on general benchmarks like AlpacaEval 2.0 and MT-Bench, also nearly resolving the length bias issue.

### Strengths
1. Originality: The introduction of the PFP framework is a novel approach to addressing bias in online preference learning for large language models (LLMs). This approach to nearly resolving the length bias issue, which has been a long-standing problem in online preference learning.
2. Rigorous Experimental Design: The paper presents a well-structured set of experiments that validate the effectiveness of the PFP framework. The use of established benchmarks like AlpacaEval 2.0 and MT-Bench adds to the credibility of the results.
3. Significance: The paper's contribution to reducing bias in AI systems is significant. By addressing bias in LLMs, the research has implications for the ethical deployment of AI, which is a critical concern in the field.

### Weaknesses
1. Diversity of tasks: The paper primarily uses AlpacaEval 2.0 and MT-Bench for evaluation. While these are established benchmarks, the use of additional or more diverse datasets could strengthen the claims of the framework's effectiveness. For example, the preference features of math or coding tasks may be different, the author should give more insights on various tasks.
2. Comparative Analysis with State-of-the-Art Methods: The paper compares PFP with SFT, DPO and Iterative DPO but does not include a comparison with the latest state-of-the-art methods in bias mitigation for LLMs. Including comparisons with cutting-edge preference learning methods would provide a clearer picture of PFP's performance relative to the most advanced techniques.

### Questions
The paper assumes a predefined set of preference features based on certain definitions and classifications. These assumptions may not cover the full spectrum of human preferences, and the preference features of math or coding tasks may be different. How to choose the most proper preference features for different tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a method to mitigate biases that arise during LM alignment -- focusing specifically on online DPO. Authors propose a new framework (PFP) to maintain the ‘distribution of human preferences’ throughout the training process, as they argue that it usually shifts during online DPO optimization.

### Strengths
- Addressing biases underlying human preference data is an important problem.
- Experimental results are strong, and the approach is interpretable.

### Weaknesses
1. The motivation for the proposed method is unclear, and its description often confusing. Examples:
  - On what basis can we assume to distill the full complexity of human preferences down to discrete unsupervised feature dimensions? The assumption that human preference can be effectively represented by a small set of discrete features is not well-justified. While prior work has explored feature extraction, the leap to assuming these features capture the full complexity of preference is significant and requires more rigorous justification. The method's reliance on predefined, discrete features may oversimplify the nuanced and context-dependent nature of human preferences, potentially leading to a loss of critical information.
  - What is the motivation behind the process of distribution preservation (paragraph starting L254)? The rationale behind preserving the distribution of preference features is not clearly articulated. It is unclear why maintaining the distribution of extracted features from the initial dataset is crucial for mitigating biases during online learning. The explanation lacks a clear connection to how this preservation directly addresses the problem of shifting preferences during online DPO optimization. A more detailed explanation of how this distribution preservation specifically counteracts the emergence of biases is needed.
  - Paragraph starting L173: i am very familiar with this literature but find this explanation confusing. Missing related works here: mention SLiC-HF (Zhao et al., 2023) and online DPO (Calandriello et al., 2023).
  - L307: how can you change the system prompt to be only one of $(s_1, s_2)$? Surely the response which does not correspond to the chosen system prompt is going to be worse? The method of sampling a single system prompt from a pair and treating the corresponding response as preferred while the other is dispreferred is questionable. This approach does not account for the possibility that both responses could be of varying quality, and it is unclear how this sampling method avoids introducing additional bias or noise into the training process.
 - Importantly, the method proposed involves many modeling choices that are not properly ablated, which makes it tricky to know whether all are needed. Some of the following modeling steps are ablated but most are not thoroughly evaluated:
   - Quality of the feature classifier. The quality of the feature classifier is not rigorously evaluated, despite its central role in the proposed method. The accuracy of the classifier directly impacts the reliability of the extracted preference features and, consequently, the effectiveness of the entire framework. A thorough evaluation of the classifier's performance, including its limitations and potential biases, is essential.
   - Performance of the distribution matching step
   - Synthesizing system prompt from preference features (see positioning wrt related works below)
   - Double system prompt sampling (see Q above)
   - Curriculum learning via temperature scheduling
  - examples of grammatical issues/ typos:
    - L147: beginning of the sentence
    - L246
    - L248: 'auxiliarly'

2. The experimental setup is weak.
- Weak positioning wrt. rest of the literature. For example, why not compare to prompt optimization strategies such as OPRO (Yang et al., 2023) and RLCD (Yang et al 2024)? The lack of comparison to prompt optimization strategies like OPRO and RLCD is a significant oversight. These methods also aim to improve model performance through prompt manipulation, and a comparison would provide valuable insights into the relative strengths and weaknesses of the proposed approach. Without such comparisons, it is difficult to assess the novelty and effectiveness of the method in the context of existing techniques.
- Since the motivation is to avoid biases, this method requires rigorous evaluation on a task with specific biases... Here we only measure for length bias. Could authors not consider an experimental setting with a clearer bias? Does your approach then accentuate biases present in the preference data? The evaluation is limited by its focus on length bias. The method's effectiveness in mitigating other types of biases is not demonstrated. A more comprehensive evaluation using datasets with known biases would be necessary to validate the method's claim of bias mitigation. It is also unclear whether the method might inadvertently amplify existing biases within the preference data.

### Questions
See above.

### Soundness
2

### Presentation
1

### Contribution
2
