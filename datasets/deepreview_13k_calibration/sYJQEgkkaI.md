# Rethinking The Reliability of Representation Engineering in Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Inspired by cognitive neuroscience, representation engineering (RepE) seeks to connect the neural activities within large language models (LLMs) to their behaviors, providing a promising pathway towards transparent AI.
Despite its successful applications under many contexts, the connection established by RepE is not always reliable, as it implicitly assumes that LLMs will consistently follow the roles assigned in the instructions during neural activities collection.
When this assumption is violated, observed correlations between the collected neural activities and model behaviors may not be causal due to potential confounding biases, thereby compromising the reliability of RepE.
We identify this key limitation and propose CAusal Representation Engineering (CARE), a principled framework that employs matched-pair trial design to control for confounders.
By isolating the impact of confounders on neural activities and model behaviors, CARE grounds the connection in causality, allowing for more reliable interpretations and control of LLMs.
Extensive empirical evaluations across various aspects of safety demonstrate the effectiveness of CARE compared to the original RepE implementation, particularly in controlling model behaviors, highlighting the importance of causality in developing transparent and trustworthy AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a framework to isolate the impact of confunding factors on correlations between neural activities and model behaviors. The identification of spurious correlations makes causal relation between neural activities and model behaviors more reliable and accurate.

### Strengths
- This paper has focused on an interesting problem in LLM interpretability, as the spurious correlations between neural activities and model behaviors is not fully explored yet. 
- The proposed framework adopts the philosophy of matched-pair trial design, which helps to filter out the data involved in confunding factors. 
- The experiments are comprehensive to demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The "spurious correlations" in safety-relevant biases could also caused by alignment fine-tuning. It would be more persuasive if the authors can provide more evidence to show the existence of spurious correlations in other cases.
- The failure of instruction following can hardly be treated to confounding factors as mentioned before.

### Questions
- What is the percentage of data with confunding factors when evaluating baseline methods?
- Could you please explain why LR is the worst performing model in baseline experiments in terms of manipulation score? Since it usually performs better in intervention tasks compare to mean differences. Is it because of too few data points i.e. stimulus pairs?
- Typo in Table 3, "Manipuation Score".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes an improvement to the representation engineering (RepE) analysis of LLMs. In the original RepE, different treatments are applied to the LLM inputs, and the resulting difference in the activation is taken as the effect of the treatment. This paper observes that the treatment is sometimes unsuccessful, resulting in unfaithful explanations. Thus, this paper proposes to use an external mechanism, such as a content moderation tool for safety analysis, to filter out inputs that do not lead to the targeted behavior change. Experimental analysis showing that this simple modification improves the RepE analysis quality.

### Strengths
This paper contains a simple yet effective idea. 

The paper is fairly well-written. 

Different ways to identify the linear safety templates are used and compared in the experiments.

### Weaknesses
While I am not very familiar with the RepE work, in my opinion the proposed modification seems to be incremental and too straightforward. Therefore, given the popularity of the original RepE work, I would defer to other reviewers in assessing whether such proposals have been made before in the literature. 

I find the paper writing being unnecessarily complicated by the analogy to neuroscience, and sometimes even the causality machinery. The study of network activations have a long history in interpretability, dating back to (at least) the TCAV work [1]. As such, I am concerned that the neuroscience analogy does not facilitate understanding, but instead could cause further confusion. 

For causality, I am not sure if the filtering approach truly leads to the desired causality. Even without filtering (as in the original RepE method), the activation may still have a causal effect on the behavior, just that the effect is not strong enough to be observed. With filtering and pairing, it is possible that the activation and the model behavior difference are both caused by the instruction, so that the activation does not causally explain the behavior difference.


### Questions
In addition to the weaknesses listed above, I have a question about the description in Line 134-136 to create P(Y_x). Doesn't data selection approach create a conditional distribution P(y|x), rather than an interventional distribution? If this creates the interventional distribution, what is the operation that creates the conditional distribution?

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
3

### Summary
This paper introduces CARE, a framework aimed at improving the reliability of representation engineering in large language models. The authors identify a key limitation in current RepE methods - the implicit assumption that models consistently follow assigned roles during neural activity collection. To address this, they propose using matched-pair trial design with content moderation models to control for confounding factors.

### Strengths
Strengths:

- The paper identifies a genuine limitation in RepE and proposes a creative solution using matched-pair trials and content moderation.
-  Demonstrates clear improvements over baselines, particularly in manipulation scores (98.46% for safe manipulations).
-  Tests the method across multiple tasks and provides detailed ablation studies.
- The work has immediate applications for improving AI safety and transparency.

### Weaknesses
The paper's fundamental theoretical weakness lies in its assumption about matched-pair trials in neural networks in my opinion. The authors propose matching inputs (text prompts) to identify and control for confounding factors. However, they fail to address several critical theoretical issues:

- a) Neural Network Non-linearity:

No insight is provided that similar inputs lead to meaningfully "matched" representations in deep networks. The non-linear transformations through multiple transformer layers could amplify small input differences. What are the bounds on how representation differences scale with input differences across network depth

- b) Causal Identification/claims:

The paper lacks formal criteria for when their matching procedure successfully isolates causal effects and if found it should provide discussion of potential hidden confounders that could violate the matching assumptions. Missing analysis of how representation distributions shift under their interventions.


- Methodology:


a) Evaluation Circularity:

Using similar types of models for filtering and evaluation could amplify shared biases. No discussion of how to validate results independent of content moderation assumptions.

b) Manipulation vs Termination:

Large unexplained gap between manipulation success (98.46%) and termination scores (~58%). This suggests either redundant causal pathways or methodological issues. Can you elaborate on this?

### Questions
- Can you provide some theoretical guarantees/insights for when input matching implies representation matching?

- Do you have a sense of what might explain the significant gap between manipulation scores (98%) and termination scores (58%)? Does this suggest redundant causal pathways?

- How sensitive are your results to the choice of content moderation model? Did you perform any ablation studies.

### Soundness
2

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
5

### Summary
The paper follows up on work on representation engineering (RepE) which shows that activations of language models can be used to interpret and steer their behaviours. The main contribution is filtering the activations collected to find the intervention vector in the LAT methodology proposed in the original RepE paper, removing instances where the model does not follow the instructions provided using Llamaguard. The experiments are principled, focusing on causal evaluations of manipulation and termination in the RepE paper, using the ALERT dataset for studying diverse behaviours rigorously, and showing the effect of varying crucial design choices like the modelling method, number of samples used, number of layers, and the intervention intensity coefficient.

### Strengths
1. This work does a great job of rigorously analysing the design choices of the LAT methodology proposed in the RepE paper, which has higher importance because this is done poorly in the original RepE paper. This can be useful for practitioners seeking to apply RepE.

2. The paper is well written and easy to follow, barring some concerns regarding how the contributions are positioned mentioned below.

### Weaknesses
1. The main contribution of this work is limited, with its impact decreasing over time. The paper shows the importance of filtering instances where the model does not follow instructions before finding the LAT vector. The importance of this contribution is diluted as models get better at instruction following, as lesser samples would be filtered.

2. The contribution can seem misleading based on the writeup of the paper, as it does not properly contextualise the new contributions on top of the original RepE paper. For example: 

a) The abstract/intro make it sound like matched-pair trial design is a contribution of this work. However, the RepE paper already uses this setup without making the connection to the naming convention used in control trial design. The only contribution seems to be filtering out the cases where the model fails to follow the instruction.

b) Manipulation and Termination are already studied as evaluations in RepE (see Figure 12 in Section 5). Lines 98-100 and Section 3.4 (especial L240-242) make it sound like these are contributions of this work, which is not true.

c) It is unclear how BASE (”using pseudo-labels based on predefined roles in the instructions, without requiring the text stimuli pairs to be comparable in content”) accurately reflects the methodology in RepE. To the best of my knowledge, RepE also uses contrastive minimal pair prompts to collect the stimuli, differing only in the behaviour to ablate.

Usually one would do this in the related work section. However, L280 in related work section just says:  "Our work builds on RepE, focusing on interpreting LLM behaviors using neural activities within the representation space", but this is exactly what RepE does so its not clear what this work builds on top. The only marginal contribution I can see is labelling model responses using llama-guard and filtering to the ones that follow the desired instructions before performing RepE, which is weak as pointed in W1.

3) The headline figure (which is Figure 2, as Figure 1 doesn't convey much information) is hard to interpret. It is unclear what the task is in figure 2 i.e. what is RepE being used for, which dataset, how many classes is the classification over etc. It is also unclear what the “RepE” method refers to. RepE is the paper whereas LAT is the method proposed in the paper.  Finally, at this point in the paper, it is unclear what is ‘inconsistent behaviour’ it would be useful to provide a concrete example in the intro, before figure 2.

### Questions
1. What percentage of prompts do different LLMs not follow the instructions for? How does this vary based on the model's instruction following capabilities, and scaling?

2. Have you considered submitting this work to the ICLR Blogpost track or TMLR? I think these venues are more suitable for work like this with rigorous analysis and reproduction, but limited technical novelty or new ideas. 

3. Line 133-134 is unclear. why is it infeasible to intervene on neural activities? How is intervene defined here can you be more specific? The original RepE paper does one form of intervention, by adding the vector found using LAT to the representation, why does this not count?

4. In section 3.3 on modelling, the linear model setup described is supervised, whereas RepE also focuses on unsupervised methods. It would be nice to make it explicit why this design choice was made. 

5 (typo/minor). Section 5 L308-310 references are broken.


**Update after discussion phase**: I thank the authors for the detailed discussion. After extensive followups, the authors confirmed that the only 'confounding factor' being controlled for here is the model not always following instructions. This is the only methodological contribution of this paper on top of the original Representation Engineering paper, and the rest is causal and neuroscience motivation. Thus I stick with my original review and score.

### Soundness
3

### Presentation
4

### Contribution
1
