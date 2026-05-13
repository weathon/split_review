# Leveraging Human Revisions for Improving Text-to-Layout Models

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Learning from human feedback has shown success in aligning large, pretrained models with human values. Prior works have mostly focused on learning from high-level labels, such as preferences between pairs of model outputs. On the other hand, many domains could benefit from more involved, detailed feedback, such as revisions, explanations, and reasoning of human users. Our work proposes using nuanced feedback through the form of human revisions for stronger alignment. In this paper, we ask expert designers to fix layouts generated from a generative layout model that is pretrained on a large-scale dataset of mobile screens. Then, we train a reward model based on how human designers revise these generated layouts. With the learned reward model, we optimize our model with reinforcement learning from human feedback (RLHF). Our method, Revision-Aware Reward Models ($\method$), allows a generative text-to-layout model to produce more modern, designer-aligned layouts, showing the potential for utilizing human revisions and stronger forms of feedback in improving generative models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to train a reward model from human designer revisions on generated layouts by a pre-trained layout model. Then, they optimizer the down-stream model by RLHF with the trained reward model. In this way, RARE aligns the model with human preference to produce more designer-aligned layout.

### Strengths
1. This paper proposes a novel approach to integrate different human feedbacks into model training, i.e., the step-by-step revision sequences. 
2. The reward is designed to correlate with revision time, which provides better signals than binary comparison rewards.

### Weaknesses
1. Though the paper presents a new notion of human feedback, i.e., revision sequences, its application to layout generation makes its applicability quite constrained. The first time I read the abstract, I thought the paper seemed to propose a general methodology for RLHF. After going through the paper, I realized that the proposed reward training is only specifically designed for the text-to-layout generation domain.
2.	The evaluation is not sound to me. In section, the major quantitative evaluation results are presented in Table 1; the remaining evaluation are mainly shown by generative examples. All of results are about one task. More quantitative evaluation evidence can make the conclusion sounder.
3.	The presentation can be improved. The equation (4) can be confusing. It will be better to list them following time ordering.

### Questions
Can authors provide more details of the CLAY dataset, like its statistics?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes improving the layout generator model with human revision feedback. The work experiments with using the time-taken by human editor, distance between the revision, sft, and binary preferences to test improving the model RLHF.

### Strengths
The paper investigates using more nuanced feedback rather than binary preference, which is a less explored area of research.

### Weaknesses
The papers outline is not in a typical format, the dataset description comes later, I struggled to imaging the dataset while reading the experiments section without reading the dataset description before.

The equations used in the paper aren't fully explained and in some places the symbols used in the equation and the description are inconsistent. I did not get a full understanding of the background reading the paper because of this. Maybe the authors can reduce the size of the figures or move them to the appendix section to get more space.

The experiment aren't rigorous and the results were not analyzed properly
- The explanation of why the Chamfer distance did worse than even the preference-based model isn't convincing. The appendix section shows that Chamfer models were trained by much more iterations in all the steps (49000 vs 2000) than all the other models, could it be just that the Chamfer model just got overfitted? To analyze the problem the author should compare chamfer vs time distance distributions and/or have more comparable training iteration numbers to start with.
- Since the proposed approach performs similarly to the preference-based model, the authors should investigate more into this with more random seeds to start with.

### Questions
Although this is a more recent work, it might be worth looking into this work which also looks into using human revision information https://arxiv.org/abs/2310.05857.

Can you train without RL? Like what is done in the paper? It probably needs alignment between the human edits (which element got changed into what).

I am surprised that there were no guidelines for humans who revised the layout. Have you seen any undesirable edits in the dataset?

Although it isn't completely clear, I am assuming you are using every edit by a person on the layout as a separate edit. It might be worth clustering some of them.

According to the description, reward model predicts the time/distance between the revisions. Does it then mean that it is a penalty model rather than a reward model?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper collects a dataset of sequences of human designers revising model-generated mobile app layouts. The paper proposes a method called RARE to learn a reward model based on the collected data and use the reward model to perform RLHF finetuning on a pre-trained layout generation model. Experimental results show that the proposed method is better than simple finetuning or other reward models.

### Strengths
- The paper collects high-quality datasets from expert app layout designers. The dataset could be important for the community. 
- The method is simple but effective. 
- The proposed method is much more effective than simple finetuning.

### Weaknesses
 - The novelty might be limited. It seems that the novel part of the method is how training samples are constructed from the collected dataset to train RARE. Other parts like the diffusion models and RLHF are similar to existing work.
- I am not quite convinced by sec. 4.2 on the reward model pretraining. The construction of pretraining data seems a bit too heuristic and are not grounded on any reasonable arguments/observations. Why do you assume dropping needs 1 time step, revised elements needs 2 time step, and added element needs 3 time steps? The parameters for each operation, e.g. resize 0.5-2 times have no explanation as well.
- Limited evaluation metrics. Previous work has considered other metrics like NLL, Coverage, or Overlap. Are these reasonable metrics for the experiments considered in this paper? If not, are there other possible metrics beyond FID? Is it reasonable to conduct user study to make the results more convincing?

### Questions
Table 1 implies that RARE and Preference has the same FID, yet Fig. 6 shows that RARE is better than Preference. Is it the case that RARE is better than Preference for most of the evaluation samples? If so, why do these methods have the same FID?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Revision-Aware Reward Models (RARE), which leverages human revisions to strengthen alignment in the context of generative layout models for mobile screens. The authors involve expert designers in fixing layouts generated by a pretrained generative layout model and train a reward model based on how these designers revise the generated layouts. By optimizing the model using reinforcement learning from human feedback (RLHF) with the learned reward model, RARE can enhance the generative model's ability to produce modern, designer-aligned layouts. On a dataset of 276 corrected UI Layouts from designers, the authors compare the proposed method with Supervised Finetuning (SF), Preference Reward + RLHF, Chamfer Distance + RLHF, and the results show the potential of the method quantitatively and qualitatively.

### Strengths
1. The proposed method focuses on utilizing nuanced feedback, such as corrections, explanations, and reasoning, to enhance generative models. While prior works have primarily relied on high-level labels, the authors' emphasis on more involved feedback represents a novel perspective. By introducing the concept of Revision-Aware Reward Models (RARE) and applying it to generative layout models, the research offers a unique contribution to the field.

2. The involvement of expert designers in fixing layouts generated by a pretrained model adds credibility to the evaluation process. The training of a reward model based on human revisions and the subsequent optimization of the generative model using reinforcement learning demonstrate a rigorous and systematic approach. The reported results strengthen the overall quality of the work.

3. Overall, the paper is well-written and easy to follow. It provides a clear explanation of the research objectives and the proposed methodology. The authors effectively communicate the significance of utilizing nuanced feedback and human revisions in improving generative models.

### Weaknesses
1. The analysis of the dataset used in this work is not comprehensive. It would benefit the research to provide an overview of the dataset, including its characteristics and why the proposed method is well-suited for this specific dataset. Additionally, to ensure the generalizability and robustness of the proposed approach, it is crucial to evaluate its performance on diverse datasets or domains. Conducting experiments with the RARE approach on different types of layouts, such as web or desktop interfaces, would provide a more comprehensive understanding of its effectiveness and applicability in various contexts.

2. While human revisions are utilized to train the reward model, there is a notable absence of analysis or insights into the specific patterns, reasoning, or design principles underlying these revisions. Gaining a deeper understanding of the factors driving the revisions made by human designers would offer valuable insights for further improving the generative model. Conducting a thorough analysis of the revisions, such as identifying common patterns or design choices, would enrich the understanding of the alignment between human values and generative outputs and provide guidance for refining the model's performance.

3. The qualitative results presented in the paper lack detailed analysis, as only a few examples are provided. To strengthen the research, it would be beneficial to offer expert opinions and insights to support and explain why the results obtained with the RARE approach are considered good.

4. Some minor typos are present in the paper, such as in section 5.2, paragraph 2, where the first sentence contains two instances of the word "that."

### Questions
1. What is the size of the collected dataset?
2. For the qualitative results, are there any implications derived?
3. As the data collection involves human subjects, is the study proved by IRB?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
